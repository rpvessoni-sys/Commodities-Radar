# -*- coding: utf-8 -*-
"""Resumo executivo diario do complexo soja — texto curto pronto pra ler no
celular e pra colar no Claude pedindo interpretacao.

Envia via Telegram se TELEGRAM_BOT_TOKEN + TELEGRAM_CHAT_ID estiverem no ambiente
(Secrets do GitHub Actions); senao so escreve em disco e imprime.

Como criar o bot do Telegram (1x, ~2 min):
  1. No Telegram, fale com @BotFather → /newbot → escolha nome → ele te da um TOKEN
  2. Fale qualquer coisa com o seu bot novo (pra abrir conversa)
  3. Abra https://api.telegram.org/bot<TOKEN>/getUpdates → copie o "chat":{"id": ...}
  4. Guarde TOKEN e CHAT_ID nos Secrets do repo (TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID)
"""
import os
from datetime import date, datetime

import config
import db


def _ultimo_e_anterior(fonte, commodity, metrica):
    """(valor_mais_recente, valor_anterior, data_recente) — None se faltar."""
    with db.connect() as conn:
        rows = conn.execute(
            """
            SELECT data_referencia, valor FROM dados_publicos
            WHERE fonte=? AND commodity=? AND metrica=? AND valor IS NOT NULL
            ORDER BY data_referencia DESC LIMIT 2
            """,
            (fonte, commodity, metrica),
        ).fetchall()
    if not rows:
        return None, None, None
    atual = rows[0]["valor"]
    ant = rows[1]["valor"] if len(rows) > 1 else None
    return atual, ant, rows[0]["data_referencia"]


def _ind(metrica):
    v, _, _ = _ultimo_e_anterior("indicators", "complexo_soja", metrica)
    return v


def _seta(atual, ant, lente_comprador=False):
    if atual is None or ant is None:
        return ""
    d = atual - ant
    if abs(d) < 1e-9:
        return "→"
    sobe = d > 0
    # lente do comprador de farelo: queda = bom (verde ↓)
    return ("↑" if sobe else "↓")


def build_resumo(target: date | None = None) -> str:
    target = target or date.today()
    L = [f"📊 *Radar Soja* — {target.strftime('%d/%m/%Y')}", ""]

    soja, soja_a, _ = _ultimo_e_anterior("cme_cbot", "soja_cbot", "fechamento")
    far, far_a, _ = _ultimo_e_anterior("cme_cbot", "farelo_cbot", "fechamento")
    oleo, oleo_a, _ = _ultimo_e_anterior("cme_cbot", "oleo_cbot", "fechamento")
    ptax, ptax_a, _ = _ultimo_e_anterior("bcb", "usd_brl_ptax", "valor")

    if far is not None:
        L.append(f"*Farelo* {far:.2f} USD/sht {_seta(far, far_a)} "
                 f"({(far-far_a):+.2f})" if far_a else f"*Farelo* {far:.2f} USD/sht")
    if soja is not None:
        L.append(f"*Soja* {soja/100:.2f} USD/bu {_seta(soja, soja_a)}")
    if oleo is not None:
        L.append(f"*Óleo* {oleo:.2f} cts/lb {_seta(oleo, oleo_a)}")
    if ptax is not None:
        L.append(f"*USD/BRL* {ptax:.4f} {_seta(ptax, ptax_a)}")

    L.append("")
    ratio = _ind("far_soj_ratio_pct")
    crush = _ind("crush_margin_usd_bu")
    oilsh = _ind("oil_share_pct")
    if ratio is not None:
        if ratio < 80:
            zona = "🟢 zona de compra"
        elif ratio < 87:
            zona = "🟡 transição"
        else:
            zona = "🔴 caro"
        L.append(f"*Ratio Far/Soj* {ratio:.1f}% — {zona}")
    if crush is not None:
        L.append(f"*Crush* {crush:.2f} USD/bu · *oil share* {oilsh:.1f}%"
                 if oilsh is not None else f"*Crush* {crush:.2f} USD/bu")

    # Alertas do dia
    try:
        import json
        af = config.DATA_DIR / "alerts_technical.json"
        if af.exists():
            data = json.loads(af.read_text(encoding="utf-8"))
            alerts = data if isinstance(data, list) else data.get("alertas", [])
            if alerts:
                L.append("")
                L.append(f"⚠️ {len(alerts)} alerta(s) técnico(s) hoje")
    except Exception:
        pass

    # Próximos marcos fiscais
    try:
        import tributario as trib
        hoje = target
        prox = [e for e in trib.list_eventos()
                if e.get("proximo_data")
                and 0 <= (date.fromisoformat(e["proximo_data"]) - hoje).days <= 7]
        if prox:
            L.append("")
            L.append("📅 *Marcos 7d:*")
            for e in sorted(prox, key=lambda x: x["proximo_data"])[:3]:
                L.append(f"  • {e['proximo_data']}: {e['titulo'][:55]}")
    except Exception:
        pass

    L.append("")
    L.append("_Abra o link do relatório pro detalhe; cole este resumo no Claude pra interpretar._")
    return "\n".join(L)


def enviar(target: date | None = None) -> dict:
    """Monta o resumo, salva em disco e envia via Telegram se configurado."""
    texto = build_resumo(target)

    # Sempre salva em disco (e na pasta do consultor)
    try:
        out = config.DATA_DIR / "resumo_dia.md"
        out.write_text(texto, encoding="utf-8")
    except Exception:
        pass

    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    chat = os.getenv("TELEGRAM_CHAT_ID", "").strip()
    if not token or not chat:
        print("[resumo] Telegram não configurado — só salvei em disco.\n")
        print(texto)
        return {"enviado": False, "motivo": "sem_telegram"}

    try:
        import requests
        r = requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            json={"chat_id": chat, "text": texto, "parse_mode": "Markdown"},
            timeout=30,
        )
        ok = r.status_code == 200
        print(f"[resumo] Telegram enviado: {ok} (HTTP {r.status_code})")
        return {"enviado": ok, "http": r.status_code}
    except Exception as e:
        print(f"[resumo] falha no envio Telegram: {e}")
        return {"enviado": False, "erro": str(e)}


if __name__ == "__main__":
    enviar()
