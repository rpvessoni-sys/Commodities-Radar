# -*- coding: utf-8 -*-
"""Dead-man switch do radar — vigia o PIPELINE, não as fontes.

Motivo (apagão de 06/08 a 26/08/2026): o job `deploy` de um run ficou preso em
`waiting` (environment github-pages) e, como o workflow inteiro tinha
`concurrency: radar-pipeline`, esse run travado segurou o grupo e TODOS os runs
seguintes foram cancelados na fila. 20 dias sem coleta. O `checkup.py` viu as
fontes velhas, mas ninguém viu o CANCELAMENTO EM SÉRIE — e o site, congelado,
não tinha como gritar.

Este vigia roda num workflow SEPARADO (concorrência própria, sem environment,
sem Pages), então ele sobrevive justamente ao tipo de falha que mata o radar:

  1. Pergunta à API do GitHub quando foi o ÚLTIMO run BEM-SUCEDIDO do radar.
  2. Se passou do limite (default 3h), manda alerta no Telegram.
  3. Se achar run preso (`waiting`/`in_progress`/`queued`) há mais que
     HEARTBEAT_STUCK_MIN (default 45 min), CANCELA via API — é isso que
     destrava o grupo de concorrência sozinho.

Uso:
    python heartbeat.py              # roda de verdade (precisa de GITHUB_TOKEN)
    python heartbeat.py --dry-run    # não cancela nada, não manda Telegram

Env: GITHUB_TOKEN, GITHUB_REPOSITORY, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID,
     HEARTBEAT_MAX_HORAS (3), HEARTBEAT_STUCK_MIN (45), HEARTBEAT_WORKFLOW (radar.yml)
"""
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

API = "https://api.github.com"
PRESO = ("waiting", "in_progress", "queued", "pending", "requested")


def _agora() -> datetime:
    return datetime.now(timezone.utc)


def _iso(s: str) -> datetime:
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def _req(url: str, token: str, method: str = "GET") -> dict:
    r = urllib.request.Request(url, method=method)
    r.add_header("Accept", "application/vnd.github+json")
    if token:
        r.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(r, timeout=60) as resp:
        corpo = resp.read()
    return json.loads(corpo) if corpo else {}


def decidir(horas_parado, presos, max_horas, hora_utc):
    """Pura (testável): devolve (alertar, texto). Sem rede, sem estado.

    horas_parado = None quando nunca houve run bem-sucedido conhecido.
    Anti-spam sem banco: durante o apagão só alerta de 4 em 4 horas (a hora do
    relógio decide), mas a PRIMEIRA detecção (< 1h além do limite) sempre passa.
    """
    parado = horas_parado is None or horas_parado > max_horas
    if not parado:
        return False, ""
    primeira = horas_parado is not None and horas_parado <= max_horas + 1
    if not primeira and hora_utc % 4 != 0:
        return False, ""

    if horas_parado is None:
        cab = "🔴 RADAR PARADO — nenhum run bem-sucedido encontrado"
    else:
        cab = f"🔴 RADAR PARADO há {horas_parado:.0f}h (limite {max_horas}h)"
    L = [cab, "O pipeline de coleta não fecha um run OK — o site e o banco estão congelados."]
    if presos:
        L.append("")
        L.append(f"Runs presos cancelados agora: {len(presos)}")
        for p in presos[:5]:
            L.append(f"  • #{p['numero']} {p['status']} há {p['horas']:.0f}h")
    L.append("")
    L.append("Abra: Actions → Commodities Radar (nuvem) → Run workflow (modo daily).")
    return True, "\n".join(L)


def _telegram(msg: str, dry: bool = False) -> bool:
    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    chat = os.getenv("TELEGRAM_CHAT_ID", "").strip()
    if dry or not token or not chat:
        print("[heartbeat] (sem envio) mensagem seria:\n" + msg)
        return False
    dados = json.dumps({"chat_id": chat, "text": msg}).encode()
    r = urllib.request.Request(f"https://api.telegram.org/bot{token}/sendMessage",
                               data=dados, method="POST")
    r.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(r, timeout=30) as resp:
            ok = resp.status == 200
    except urllib.error.URLError as e:
        print(f"[heartbeat] falha no Telegram: {e}")
        return False
    print(f"[heartbeat] Telegram enviado: {ok}")
    return ok


def main(argv) -> int:
    dry = "--dry-run" in argv
    repo = os.getenv("GITHUB_REPOSITORY", "rpvessoni-sys/Commodities-Radar")
    token = os.getenv("GITHUB_TOKEN", "").strip()
    wf = os.getenv("HEARTBEAT_WORKFLOW", "radar.yml")
    max_horas = float(os.getenv("HEARTBEAT_MAX_HORAS", "3"))
    stuck_min = float(os.getenv("HEARTBEAT_STUCK_MIN", "45"))
    agora = _agora()

    # 1) último run bem-sucedido
    horas_parado = None
    try:
        d = _req(f"{API}/repos/{repo}/actions/workflows/{wf}/runs?status=success&per_page=1", token)
        runs = d.get("workflow_runs") or []
        if runs:
            horas_parado = (agora - _iso(runs[0]["updated_at"])).total_seconds() / 3600
            print(f"[heartbeat] último run OK: {runs[0]['updated_at']} (há {horas_parado:.1f}h)")
        else:
            print("[heartbeat] nenhum run bem-sucedido encontrado")
    except urllib.error.HTTPError as e:
        print(f"[heartbeat] API falhou ({e.code}) — abortando sem alarme falso")
        return 0

    # 2) runs presos (é o que segura o grupo de concorrência) → cancelar
    presos = []
    for status in PRESO:
        try:
            d = _req(f"{API}/repos/{repo}/actions/workflows/{wf}/runs?status={status}&per_page=20", token)
        except urllib.error.HTTPError:
            continue
        for r in d.get("workflow_runs") or []:
            idade = (agora - _iso(r["run_started_at"] or r["created_at"])).total_seconds() / 60
            if idade < stuck_min:
                continue
            item = {"id": r["id"], "numero": r["run_number"], "status": r["status"], "horas": idade / 60}
            presos.append(item)
            if dry:
                print(f"[heartbeat] (dry) cancelaria run #{item['numero']} ({status}, {idade:.0f} min)")
                continue
            try:
                _req(f"{API}/repos/{repo}/actions/runs/{r['id']}/cancel", token, method="POST")
                print(f"[heartbeat] cancelado run #{item['numero']} ({status}, preso há {idade:.0f} min)")
            except urllib.error.HTTPError as e:
                print(f"[heartbeat] não consegui cancelar #{item['numero']}: HTTP {e.code}")

    alertar, msg = decidir(horas_parado, presos, max_horas, agora.hour)
    if alertar:
        _telegram(msg, dry=dry)
    elif horas_parado is not None and horas_parado <= max_horas:
        print("[heartbeat] pipeline vivo — nada a fazer.")
    else:
        print(f"[heartbeat] PARADO há {horas_parado:.0f}h, mas fora da janela anti-spam "
              f"(alerta a cada 4h) — sem novo aviso agora.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
