# -*- coding: utf-8 -*-
"""Auto-monitoramento do pipeline na nuvem.

Problema que isto resolve: o disparo do robo depende 100% de um pinger externo
(cron-job.org) + um PAT que expira. Se o pinger pausar ou o PAT morrer, o run
'daily' simplesmente NAO executa — o GitHub Actions nem registra erro (nao ha
run), o site congela no ultimo snapshot e ninguem percebe por dias.

Solucao: o 'daily' deixa um batimento (heartbeat) no DB ao terminar; o 'intraday'
(que roda com muito mais frequencia) confere esse batimento e, se o daily nao roda
ha tempo demais, dispara UM aviso por dia no Telegram. Transforma uma falha
invisivel num alerta acionavel.

O estado vive no radar.db (viaja no cache do Actions). Em cache novo/zerado o
heartbeat fica vazio -> nao alarma falso (so alerta quando um daily que JA rodou
fica obsoleto).
"""
import os
from datetime import datetime, date, timezone

import db

# daily roda 1x/dia (~19h BRT). >26h = pulou pelo menos um ciclo (folga p/ atraso do cron).
DAILY_MAX_HORAS = 26.0


def _ensure_table():
    with db.connect() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS pipeline_heartbeat (
                evento TEXT PRIMARY KEY,
                ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )


def marcar_daily():
    """Registra que o daily rodou AGORA (timestamp UTC explicito). Chamar no fim de run_daily()."""
    try:
        _ensure_table()
        ts = datetime.now(timezone.utc).isoformat()
        with db.connect() as conn:
            conn.execute(
                "INSERT INTO pipeline_heartbeat (evento, ts) VALUES ('daily', ?) "
                "ON CONFLICT(evento) DO UPDATE SET ts=excluded.ts",
                (ts,),
            )
    except Exception:
        pass  # heartbeat e best-effort; nunca derruba o run


def _horas_desde_daily():
    """Horas desde o ultimo daily. None se nunca registrou (cache novo).

    Compara em UTC dos dois lados — o runner da nuvem e UTC, mas local nao; cravar
    UTC evita o offset de fuso (ex: BRT daria -3h).
    """
    try:
        _ensure_table()
        with db.connect() as conn:
            row = conn.execute(
                "SELECT ts FROM pipeline_heartbeat WHERE evento='daily'"
            ).fetchone()
        if not row or not row[0]:
            return None
        ts = datetime.fromisoformat(row[0])
        if ts.tzinfo is None:
            ts = ts.replace(tzinfo=timezone.utc)  # tolera marca antiga (UTC naive)
        return (datetime.now(timezone.utc) - ts).total_seconds() / 3600.0
    except Exception:
        return None


def _telegram(texto: str) -> bool:
    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    chat = os.getenv("TELEGRAM_CHAT_ID", "").strip()
    if not token or not chat:
        return False
    try:
        import requests
        r = requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            json={"chat_id": chat, "text": texto},  # texto puro (sem parse_mode)
            timeout=30,
        )
        return r.status_code == 200
    except Exception:
        return False


def checar_daily() -> bool:
    """Se o daily nao roda ha > DAILY_MAX_HORAS, avisa no Telegram (no maximo 1x por
    dia-calendario, p/ nao spammar a cada intraday). Chamar dentro de run_intraday().
    Retorna True se enviou aviso."""
    horas = _horas_desde_daily()
    if horas is None or horas <= DAILY_MAX_HORAS:
        return False

    # Dedup: 1 aviso por dia. A propria tabela guarda a marca 'aviso_AAAA-MM-DD'.
    chave = f"aviso_daily_{date.today().isoformat()}"
    try:
        with db.connect() as conn:
            ja = conn.execute(
                "SELECT 1 FROM pipeline_heartbeat WHERE evento=?", (chave,)
            ).fetchone()
        if ja:
            return False
    except Exception:
        return False

    msg = (
        f"⚠️ Radar — o DAILY nao roda ha ~{horas:.0f}h (limite {DAILY_MAX_HORAS:.0f}h).\n"
        f"O site pode estar congelado no ultimo snapshot.\n"
        f"Cheque: GitHub Actions (existe run 'daily' recente?) e o pinger "
        f"cron-job.org (jobs habilitados? PAT valido?)."
    )
    if _telegram(msg):
        try:
            with db.connect() as conn:
                conn.execute(
                    "INSERT OR IGNORE INTO pipeline_heartbeat (evento) VALUES (?)", (chave,)
                )
        except Exception:
            pass
        return True
    return False


if __name__ == "__main__":
    h = _horas_desde_daily()
    print(f"[healthcheck] ultimo daily ha {h:.1f}h" if h is not None
          else "[healthcheck] sem heartbeat de daily ainda")
    if checar_daily():
        print("[healthcheck] aviso enviado")
