# -*- coding: utf-8 -*-
"""Entrypoint do radar na NUVEM (GitHub Actions) — substitui o Task Scheduler local.

Dois modos, SEPARADOS POR FREQUENCIA DO DADO (decisao 2026-06-16):

  --mode intraday   (a cada 15 min, 24/7)
      SO o que flutua sempre: CBOT (Yahoo) + cambio (BCB). Sao gratis e o CBOT
      negocia quase 24h (Globex). Recalcula indicadores (crush, oil share,
      ratio Far/Soj) + alertas + HTML + alerta-na-hora. Em hora de mercado
      fechado o re-fetch so devolve o mesmo (idempotente, sem custo).

  --mode daily      (1x/dia, pos-fechamento)
      Varredura COMPLETA (run_all): tambem as fontes PERIODICAS — fisico que
      publica 1x/dia (CEPEA/NAG) e fundamentos (WASDE/NOPA/ABIOVE/COT/clima),
      que so trazem dado novo no dia da release. + forecast + dump + resumo.
      Bater nelas a cada 30 min seria desperdicio (e queima de credito ScraperAPI).

Uso local pra testar:
    .venv\\Scripts\\python.exe cloud_run.py --mode intraday
    .venv\\Scripts\\python.exe cloud_run.py --mode daily

Variaveis de ambiente (no Actions vem dos Secrets; local vem do .env):
    SCRAPER_API_KEY, NASS_API_KEY   — coleta
    TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID — resumo/alerta (opcional)
"""
import argparse
import io
import os
import sys
from datetime import datetime

# UTF-8 no stdout (Actions usa Linux/utf-8; local Windows precisa)
try:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")
except Exception:
    pass

import config
import db
import indicators as indicators_mod
import alerts_technical
import forecast as forecast_mod
import synth_daily
import notify_html
import notify_markdown
from sources import registry


# Dados que FLUTUAM SEMPRE (API direta, gratis) — rodam a cada 30 min, 24/7.
# Tudo o mais (fisico CEPEA/NAG diario + fundamentos WASDE/NOPA/COT/... periodicos)
# fica no modo daily, na cadencia de quem publica.
FREE_INTRADAY = ["cme_cbot", "bcb"]


def _log(msg):
    print(f"[cloud {datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)


def _horas_desde_ultima_ok(fonte: str) -> float:
    """Horas desde a última coleta OK desta fonte (1e9 se nunca). (utilitario)."""
    try:
        with db.connect() as conn:
            row = conn.execute(
                "SELECT MAX(inicio) FROM coletas_log WHERE fonte=? AND status='ok'",
                (fonte,),
            ).fetchone()
        if not row or not row[0]:
            return 1e9
        return (datetime.now() - datetime.fromisoformat(row[0])).total_seconds() / 3600.0
    except Exception:
        return 1e9


def _coletar(fonte: str):
    try:
        r = registry.run_one(fonte)
        _log(f"  {fonte:<18} {r.get('status','?'):<8} "
             f"fetched={r.get('fetched','-')} saved={r.get('saved','-')}")
        return r
    except Exception as e:
        _log(f"  {fonte:<18} ERRO {type(e).__name__}: {e}")
        return {"source": fonte, "status": "error", "error": str(e)}


def _pos_coleta(gerar_forecast: bool, gerar_dump: bool):
    """Indicadores → alertas → (forecast) → HTML → (dump)."""
    _log("indicadores...")
    try:
        indicators_mod.calculate_all()
    except Exception as e:
        _log(f"  indicadores ERRO: {e}")

    _log("alertas...")
    try:
        alertas = alerts_technical.check_alerts()
        if alertas:
            alerts_technical.save_alerts(alertas)
        _log(f"  {len(alertas)} alerta(s)")
    except Exception as e:
        _log(f"  alertas ERRO: {e}")

    if gerar_forecast:
        _log("forecast 7d/30d...")
        try:
            forecast_mod.gerar_forecasts()
            forecast_mod.resolver_realizados()
        except Exception as e:
            _log(f"  forecast ERRO: {e}")

    _log("HTML...")
    try:
        content = synth_daily.generate_structured_report()
        notify_markdown.write_daily(content)
        out = notify_html.gerar_html()
        _log(f"  HTML: {out}")
    except Exception as e:
        _log(f"  HTML ERRO: {e}")
        raise  # HTML é o produto — se falhar, o run deve ficar vermelho

    if gerar_dump:
        try:
            dump = synth_daily.generate_full_dump()
            (config.DATA_DIR / "last_dump.md").write_text(dump, encoding="utf-8")
        except Exception as e:
            _log(f"  dump ERRO: {e}")

    # Alerta na hora: pinga o Telegram se surgiu sinal novo de severidade alta
    _log("alerta na hora (fila)...")
    try:
        import alerts_push
        n = alerts_push.enviar_novos()
        _log(f"  {n} alerta(s) novo(s) push" if n else "  nada novo (ou Telegram off)")
    except Exception as e:
        _log(f"  alerta push ERRO (nao critico): {e}")


def run_intraday():
    _log("MODO INTRADAY — só o que flutua sempre (CBOT + câmbio), a cada 15 min 24/7")
    for f in FREE_INTRADAY:
        _coletar(f)

    # Input físico via Telegram: lê mensagens novas do dono e grava em precos_fisicos
    # ANTES do _pos_coleta, pra o físico já entrar no HTML deste run.
    try:
        import telegram_input
        n = telegram_input.poll_and_apply()
        if n:
            _log(f"  {n} input(s) físico via Telegram")
    except Exception as e:
        _log(f"  telegram_input ERRO (nao critico): {e}")

    _pos_coleta(gerar_forecast=False, gerar_dump=False)

    # Pulso CBOT: linha compacta de precos (farelo/soja/oleo + ratio) a cada run
    # de 15 min DENTRO do pregao de graos (dia util, ~10h30-16h20 BRT). Fora: no-op.
    try:
        import daily_summary
        r = daily_summary.pulso_intraday()
        if r.get("enviado"):
            _log("  pulso CBOT enviado")
    except Exception as e:
        _log(f"  pulso CBOT ERRO (nao critico): {e}")

    # Cobertura do resumo: se ja passou ~19h BRT (22 UTC) e o resumo ainda nao saiu
    # hoje, o intraday garante o envio (1x/dia, deduplicado) — assim o resumo NAO
    # depende do job 'daily' do pinger disparar; os runs intraday (15 min) cobrem.
    try:
        from datetime import timezone
        if datetime.now(timezone.utc).hour >= 22:
            import daily_summary
            r = daily_summary.enviar_diario_uma_vez()
            if r.get("enviado"):
                _log("  resumo do dia enviado pelo intraday (cobertura)")
    except Exception as e:
        _log(f"  resumo intraday ERRO (nao critico): {e}")

    # Healthcheck: o intraday roda muito mais que o daily, então é o lugar certo
    # pra perceber que o daily parou (pinger/PAT morto) e avisar no Telegram (1x/dia).
    try:
        import healthcheck
        if healthcheck.checar_daily():
            _log("  healthcheck: daily atrasado — aviso enviado no Telegram")
    except Exception as e:
        _log(f"  healthcheck ERRO (nao critico): {e}")

    _log("intraday OK")


def run_daily():
    _log("MODO DAILY — varredura completa + forecast + resumo")
    for r in registry.run_all():
        st = r.get("status", "?")
        if st != "disabled":
            _log(f"  {r.get('source','?'):<18} {st:<8} "
                 f"fetched={r.get('fetched','-')} saved={r.get('saved','-')}")

    _pos_coleta(gerar_forecast=True, gerar_dump=True)

    _log("resumo do dia...")
    try:
        import daily_summary
        daily_summary.enviar_diario_uma_vez(forcar=True)  # daily canônico: sempre envia + marca
    except Exception as e:
        _log(f"  resumo ERRO (não crítico): {e}")

    # Batimento: marca que o daily rodou agora, pro healthcheck do intraday vigiar.
    try:
        import healthcheck
        healthcheck.marcar_daily()
    except Exception as e:
        _log(f"  heartbeat ERRO (nao critico): {e}")

    _log("daily OK")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["intraday", "daily"], default="intraday")
    args = ap.parse_args()

    config.ensure_dirs()
    db.init_db()  # idempotente (CREATE TABLE IF NOT EXISTS) — cobre runner novo

    # Camada manual (preco fisico, curva do consultor, params) vinda do TOML
    # versionado — antes dos indicadores, pois fisico/params alimentam calculos.
    try:
        import inputs_manuais
        inputs_manuais.sync()
    except Exception as e:
        _log(f"inputs_manuais falhou (nao critico): {e}")

    if args.mode == "daily":
        run_daily()
    else:
        run_intraday()


if __name__ == "__main__":
    main()
