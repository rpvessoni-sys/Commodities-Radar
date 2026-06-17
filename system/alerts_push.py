# -*- coding: utf-8 -*-
"""Alerta na hora — pinga o Telegram quando aparece um sinal NOVO de severidade
alta na fila de julgamento (cruzou um limiar AGORA), sem esperar o resumo diario.

Roda dentro do intraday (a cada 30 min no pregao). Dedup pelo id estavel do item
da fila: cada cruzamento avisa UMA vez, nao a cada run. Estado em alertas_enviados
(viaja no cache do Actions). No-op se TELEGRAM_BOT_TOKEN/CHAT_ID nao estiverem no
ambiente — nesse caso o badge no dash ja cobre o aviso.
"""
import os

import db
import queue_emit


def _ensure_table():
    with db.connect() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS alertas_enviados (
                fingerprint TEXT PRIMARY KEY,
                enviado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )


def _ja_enviado(fp: str) -> bool:
    with db.connect() as conn:
        return conn.execute(
            "SELECT 1 FROM alertas_enviados WHERE fingerprint=?", (fp,)
        ).fetchone() is not None


def _marcar(fp: str):
    with db.connect() as conn:
        conn.execute("INSERT OR IGNORE INTO alertas_enviados (fingerprint) VALUES (?)", (fp,))


def _telegram(texto: str) -> bool:
    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    chat = os.getenv("TELEGRAM_CHAT_ID", "").strip()
    if not token or not chat:
        return False
    try:
        import requests
        # Texto PURO (sem parse_mode): a evidencia tem nomes de metrica com '_'
        # (far_soj_ratio_pct, soja_cbot) que quebram o Markdown do Telegram (400).
        r = requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            json={"chat_id": chat, "text": texto},
            timeout=30,
        )
        return r.status_code == 200
    except Exception:
        return False


def enviar_novos(target=None, severidades=("alta",)) -> int:
    """Envia Telegram pros itens NOVOS (ainda nao avisados) da fila nas severidades
    dadas. Retorna quantos enviou. No-op (0) se Telegram nao estiver configurado."""
    if not (os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
            and os.getenv("TELEGRAM_CHAT_ID", "").strip()):
        return 0

    _ensure_table()
    enviados = 0
    for it in queue_emit.build_queue(target):
        if it.get("severidade") not in severidades:
            continue
        fp = it.get("id")
        if not fp or _ja_enviado(fp):
            continue
        msg = (
            f"🔴 Radar — sinal novo\n"
            f"{it.get('titulo','')}\n\n"
            f"{it.get('evidencia','')}\n\n"
            f"Leitura: {it.get('pergunta','')}\n"
            f"➜ abra o Claude no projeto: \"lê a fila de julgamento e trata\""
        )
        if _telegram(msg):
            _marcar(fp)
            enviados += 1
    return enviados


if __name__ == "__main__":
    n = enviar_novos()
    print(f"[alerts_push] {n} alerta(s) novo(s) enviado(s)"
          if n else "[alerts_push] nada novo (ou Telegram nao configurado)")
