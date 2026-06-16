"""Escreve relatorio diario em markdown."""
from datetime import date
from pathlib import Path

import config


def write_daily(content: str, target_date: date | None = None) -> Path:
    target = target_date or date.today()
    config.REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    out_path = config.REPORTS_DIR / f"{target.isoformat()}_daily.md"
    # synth ja inclui header proprio; nao duplicar
    out_path.write_text(content, encoding="utf-8")
    return out_path
