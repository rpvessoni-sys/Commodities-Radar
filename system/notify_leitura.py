"""Entrega a LEITURA autônoma (insights/*.md) no Telegram, por commodity.

A leitura da Fase 2 ficava presa num PR do GitHub — o dono nunca recebia. Este
módulo formata a leitura (viés + a call por commodity, igual o radar mostra) e
manda pro Telegram, onde ele já recebe o pulso/resumo.

Uso:
    python notify_leitura.py <arquivo|slug>     # uma leitura específica
    python notify_leitura.py --latest           # a leitura mais recente
    opcional: --url <link>  ou  --blobbase <https://github.com/o/r/blob/branch>

Texto PURO (sem parse_mode) — nomes com '_'/'*' quebram o Markdown do Telegram.
No-op (só imprime o preview) se TELEGRAM_BOT_TOKEN/CHAT_ID não estiverem no ambiente.
"""
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import insights as ins  # noqa: E402

_EMOJI = {"bull": "🟢", "bear": "🔴", "neutro": "⚪"}
_LIMITE_TELEGRAM = 4000  # margem sob o teto de 4096


def build_msg(insight: dict, url: str = "") -> str:
    """Mensagem de Telegram: título + visão geral + 3 commodities (viés + call)."""
    L = []
    L.append(f"📊 Leitura do complexo — {insight.get('data') or '—'}")
    titulo = (insight.get("titulo") or "").strip().strip('"').strip()
    if titulo:
        L.append(titulo)
    visao = (insight.get("visao_geral") or "").strip()
    if visao:
        L += ["", visao]
    for c in insight.get("por_commodity", []):
        emoji = _EMOJI.get(c.get("direc"), "⚪")
        vl = (c.get("vies_label") or "").strip()
        cab = f"{emoji} {c['nome']}" + (f" — {vl}" if vl else "")
        L += ["", cab, c.get("explicacao", "")]
    if url:
        L += ["", f"📄 Leitura completa: {url}"]
    msg = "\n".join(L).strip()
    if len(msg) > _LIMITE_TELEGRAM:
        msg = msg[:_LIMITE_TELEGRAM].rstrip() + "…"
    return msg


def enviar(insight: dict, url: str = "") -> dict:
    msg = build_msg(insight, url)
    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    chat = os.getenv("TELEGRAM_CHAT_ID", "").strip()
    if not token or not chat:
        print("[leitura] Telegram não configurado — preview abaixo:\n")
        print(msg)
        return {"enviado": False, "motivo": "sem_telegram"}
    try:
        import requests
        r = requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            json={"chat_id": chat, "text": msg},
            timeout=30,
        )
        ok = r.status_code == 200
        print(f"[leitura] Telegram enviado: {ok} (HTTP {r.status_code})")
        if not ok:
            print(f"[leitura] corpo: {r.text[:300]}")
        return {"enviado": ok, "http": r.status_code}
    except Exception as e:
        print(f"[leitura] falha no envio: {e}")
        return {"enviado": False, "erro": str(e)}


def _carregar(arquivo: str | None, latest: bool) -> dict | None:
    todos = ins.list_insights()
    if latest:
        return todos[0] if todos else None
    if arquivo:
        alvo = Path(arquivo).stem
        for it in todos:
            if it["slug"] == alvo or Path(it["arquivo"]).name == Path(arquivo).name:
                return it
    return None


def _link(insight: dict, url: str, blobbase: str) -> str:
    if url:
        return url
    if blobbase:
        return f"{blobbase.rstrip('/')}/insights/{Path(insight['arquivo']).name}"
    return ""


if __name__ == "__main__":
    args = sys.argv[1:]

    def _opt(flag):
        if flag in args:
            i = args.index(flag)
            val = args[i + 1] if i + 1 < len(args) else ""
            del args[i:i + 2]
            return val
        return ""

    url = _opt("--url")
    blobbase = _opt("--blobbase")
    latest = "--latest" in args
    if latest:
        args.remove("--latest")
    arquivo = next((a for a in args if not a.startswith("--")), None)

    it = _carregar(arquivo, latest)
    if not it:
        print("[leitura] insight não encontrado (use --latest ou passe o arquivo/slug)")
        sys.exit(1)
    if not it.get("por_commodity"):
        print(f"[leitura] '{it['slug']}' não tem seções por commodity — nada a enviar.")
        sys.exit(0)
    enviar(it, _link(it, url, blobbase))
