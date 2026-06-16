# -*- coding: utf-8 -*-
"""Entrypoint do radar na NUVEM (GitHub Actions) — substitui o Task Scheduler local.

Dois modos (escolhidos pelo cron que disparou):

  --mode intraday   (a cada 30 min, durante o pregao)
      Fontes GRATIS (CBOT via Yahoo + cambio BCB) SEMPRE.
      Fontes PAGAS (CEPEA/NAG via ScraperAPI) so se nao rodaram nas ultimas
      PAID_MIN_HORAS (default 4h) — elas publicam 1x/dia, entao verificar a cada
      30 min sem trava queimaria ~5 mil creditos/mes a toa. A trava da o dado
      mais fresco que a fonte permite, sem desperdicio.
      Recalcula indicadores (crush, oil share, ratio Far/Soj) + alertas + HTML.

  --mode daily      (1x/dia, pos-fechamento)
      Varredura COMPLETA (todas as fontes, inclui fundamentos: WASDE, NOPA,
      ABIOVE, COT, clima) + forecast 7d/30d + HTML + dump + resumo do dia.

Uso local pra testar:
    .venv\\Scripts\\python.exe cloud_run.py --mode intraday
    .venv\\Scripts\\python.exe cloud_run.py --mode daily

Variaveis de ambiente (no Actions vem dos Secrets; local vem do .env):
    SCRAPER_API_KEY, NASS_API_KEY   — coleta
    PAID_MIN_HORAS                  — trava das fontes pagas no intraday (default 4)
    TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID — resumo diario (opcional)
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


# Fontes que custam ZERO (API direta) — rodam a cada 30 min sem dó
FREE_INTRADAY = ["cme_cbot", "bcb"]
# Fontes que custam crédito ScraperAPI — verificadas no intraday mas com trava
PAID_GUARDED = ["nag_fisico", "cepea_paranagua", "cepea_rss", "noticias_rss"]


def _log(msg):
    print(f"[cloud {datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)


def _horas_desde_ultima_ok(fonte: str) -> float:
    """Horas desde a última coleta OK desta fonte (1e9 se nunca)."""
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


def run_intraday():
    paid_min = float(os.getenv("PAID_MIN_HORAS", "4"))
    _log(f"MODO INTRADAY — grátis sempre, pagas se >{paid_min:g}h desde a última")

    for f in FREE_INTRADAY:
        _coletar(f)

    for f in PAID_GUARDED:
        h = _horas_desde_ultima_ok(f)
        if h >= paid_min:
            _coletar(f)
        else:
            _log(f"  {f:<18} skip (rodou há {h:.1f}h < {paid_min:g}h — sem fechamento novo)")

    _pos_coleta(gerar_forecast=False, gerar_dump=False)
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
        daily_summary.enviar()
    except Exception as e:
        _log(f"  resumo ERRO (não crítico): {e}")

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
