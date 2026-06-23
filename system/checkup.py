"""Check-up das fontes — certifica que TUDO coleta dado ATUALIZADO e FIDEDIGNO.

Para cada fonte ativa do registry:
  - rodou recentemente? (coletas_log, vs cadência esperada)
  - extraiu dado de verdade? (registros salvos na janela — pega parser quebrado,
    fonte paga/stub que "roda" mas não traz número: MPOB, ANEC, BCBA…)
Mais o frescor CBOT POR commodity (reusa indicators.cbot_freshness — pega o farelo
travado que a saúde por-fonte não vê).

Manda um relatório pro Telegram (texto puro, reusa TELEGRAM_BOT_TOKEN/CHAT_ID).

Uso:
  python checkup.py            # default: relatório completo só 2ª feira ou se há problema
  python checkup.py --report   # força relatório completo
  python checkup.py --alert    # mods silencioso: só envia se houver problema
No-op (só imprime) sem secrets do Telegram.
"""
import os
import sys
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import db          # noqa: E402
import indicators  # noqa: E402

# Cadência esperada por fonte (dias) e tolerância — mesma régua do dashboard.
_CADENCIA = {
    "cme_cbot": (1, 3), "bcb": (1, 4), "cepea_rss": (1, 4),
    "cepea_paranagua": (1, 5), "nag_fisico": (1, 5), "inmet": (1, 3),
    "noaa_cpc": (1, 5), "noticias_rss": (1, 4),
    "anec": (7, 10), "bcba": (7, 10), "cftc_cot": (7, 10), "usda_crop_progress": (7, 12),
    "abiove": (31, 40), "mpob": (31, 40), "nopa": (31, 50), "usda_wasde": (31, 40),
}

_ICON = {"ok": "✅", "atrasada": "⚠️", "nao_extrai": "⚠️", "erro": "🔴", "desativada": "⚪"}
_PROBLEMA = ("erro", "atrasada", "nao_extrai")


def run_checkup(target: date | None = None) -> dict:
    target = target or date.today()
    from sources import registry as reg
    fontes = []
    with db.connect() as conn:
        logs = {}
        for r in conn.execute(
                "SELECT fonte, MAX(inicio) ult, status FROM coletas_log GROUP BY fonte"):
            logs[r["fonte"]] = dict(r)

        for src in reg.list_all():
            fonte = src["source"]
            cad, tol = _CADENCIA.get(fonte, (7, 14))
            if not src.get("enabled", True):
                fontes.append({"fonte": fonte, "estado": "desativada", "nota": "—"})
                continue
            log = logs.get(fonte)
            if not log or not log["ult"]:
                fontes.append({"fonte": fonte, "estado": "erro", "nota": "nunca rodou"})
                continue
            try:
                idade = (datetime.now() - datetime.fromisoformat(log["ult"])).days
            except (ValueError, TypeError):
                idade = None
            # Última data com VALOR REAL (não-nulo) — certifica que EXTRAIU dado,
            # não só que rodou. ABIOVE/projeções têm data futura → idade negativa
            # (não conta como velho, é projeção legítima).
            r2 = conn.execute(
                "SELECT MAX(data_referencia) d FROM dados_publicos "
                "WHERE fonte=? AND valor IS NOT NULL", (fonte,)).fetchone()
            ultima_data = r2["d"] if r2 else None
            idade_dado = None
            if ultima_data:
                try:
                    idade_dado = (target - date.fromisoformat(ultima_data[:10])).days
                except (ValueError, TypeError):
                    idade_dado = None
            if log["status"] not in (None, "ok"):
                estado, nota = "erro", str(log["status"])
            elif idade is not None and idade > tol:
                estado, nota = "atrasada", f"sem rodar há {idade}d (cadência {cad}d)"
            elif ultima_data is None:
                estado, nota = "nao_extrai", "roda mas nunca trouxe número (parser/fonte paga?)"
            elif idade_dado is not None and idade_dado > (cad + tol):
                estado, nota = "nao_extrai", f"último dado real de {ultima_data} ({idade_dado}d — parser parou?)"
            else:
                estado, nota = "ok", f"dado até {ultima_data}"
            fontes.append({"fonte": fonte, "estado": estado, "nota": nota})

        fresh = indicators.cbot_freshness(conn, target)
    cbot = [{"commodity": c.replace("_cbot", ""), "stale": v["stale"], "data": v["data"]}
            for c, v in fresh.items()]
    return {"data": target.isoformat(), "fontes": fontes, "cbot": cbot}


def tem_problema(res: dict) -> bool:
    return (any(f["estado"] in _PROBLEMA for f in res["fontes"])
            or any(c["stale"] for c in res["cbot"]))


def format_report(res: dict, full: bool = True) -> str:
    fontes = res["fontes"]
    probs = [f for f in fontes if f["estado"] in _PROBLEMA]
    cbot_stale = [c for c in res["cbot"] if c["stale"]]
    oks = [f for f in fontes if f["estado"] == "ok"]
    desat = [f["fonte"] for f in fontes if f["estado"] == "desativada"]

    L = [f"🩺 Check-up das fontes — {res['data']}"]
    if not probs and not cbot_stale:
        L.append(f"✅ Tudo OK — {len(oks)} fontes coletando dado atualizado; "
                 f"CBOT (soja/farelo/óleo) fresco.")
    else:
        L.append(f"⚠️ Atenção: {len(probs)} fonte(s)" +
                 (f" + {len(cbot_stale)} perna(s) CBOT" if cbot_stale else "") + ":")
        for c in cbot_stale:
            L.append(f"🔴 CBOT {c['commodity']}: travado desde {c['data']}")
        for f in probs:
            L.append(f"{_ICON[f['estado']]} {f['fonte']}: {f['nota']}")
    if full:
        if oks:
            L.append("")
            L.append("✅ OK: " + ", ".join(f["fonte"] for f in oks))
        if desat:
            L.append("⚪ desativadas: " + ", ".join(desat))
    return "\n".join(L)


def _enviar(msg: str) -> dict:
    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    chat = os.getenv("TELEGRAM_CHAT_ID", "").strip()
    if not token or not chat:
        print("[checkup] Telegram não configurado — relatório abaixo:\n")
        print(msg)
        return {"enviado": False, "motivo": "sem_telegram"}
    try:
        import requests
        r = requests.post(f"https://api.telegram.org/bot{token}/sendMessage",
                          json={"chat_id": chat, "text": msg}, timeout=30)
        ok = r.status_code == 200
        print(f"[checkup] Telegram enviado: {ok} (HTTP {r.status_code})")
        if not ok:
            print(f"[checkup] corpo: {r.text[:300]}")
        return {"enviado": ok, "http": r.status_code}
    except Exception as e:
        print(f"[checkup] falha no envio: {e}")
        return {"enviado": False, "erro": str(e)}


if __name__ == "__main__":
    res = run_checkup()
    problema = tem_problema(res)
    force_report = "--report" in sys.argv
    force_alert = "--alert" in sys.argv
    segunda = date.today().weekday() == 0   # heartbeat semanal na 2ª feira

    if force_alert:
        enviar, full = problema, False
    elif force_report:
        enviar, full = True, True
    else:  # default (cron diário): manda se há problema OU é 2ª (confirma que está vivo)
        enviar, full = (problema or segunda), (segunda or not problema)

    msg = format_report(res, full=full)
    if enviar:
        _enviar(msg)
    else:
        print("[checkup] sem problema e não é dia de relatório — nada enviado.\n")
        print(msg)
