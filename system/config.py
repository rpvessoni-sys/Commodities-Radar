"""Carrega configuracao do .env e expoe caminhos do projeto."""
import os
from pathlib import Path
from dotenv import load_dotenv

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

load_dotenv(HERE / ".env")

# IMAP/StoneX removidos em 2026-06-11 — extracao de relatorios proibida desde 2026-06-05.

# --- Anthropic ---
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
DAILY_MODEL = os.getenv("DAILY_MODEL", "claude-sonnet-4-6")

# --- Paths ---
DATA_DIR = (HERE / os.getenv("DATA_DIR", "../data")).resolve()
REPORTS_DIR = (HERE / os.getenv("REPORTS_DIR", "../reports")).resolve()
SHARED_DIR = (HERE / os.getenv("SHARED_DIR", "../shared")).resolve()

PUBLIC_CACHE = DATA_DIR / "public_sources"
PRICES_DIR = DATA_DIR / "prices"
DB_PATH = DATA_DIR / "radar.db"

# Shared with consultor (sub-pastas)
SHARED_FROM_INSIGHTS = SHARED_DIR / "from_consultor" / "insights"
SHARED_FROM_NOTAS = SHARED_DIR / "from_consultor" / "notas_call"
SHARED_TO_SNAPSHOTS = SHARED_DIR / "to_consultor" / "snapshots_diarios"
SHARED_TO_TESES = SHARED_DIR / "to_consultor" / "teses_ativas"
SHARED_TO_ALERTS = SHARED_DIR / "to_consultor" / "alerts"
SHARED_TO_PERGUNTAS = SHARED_DIR / "to_consultor" / "perguntas_pendentes"

DAILY_REPORT_HOUR = int(os.getenv("DAILY_REPORT_HOUR", "6"))


def ensure_dirs():
    for d in [
        DATA_DIR, REPORTS_DIR,
        PUBLIC_CACHE, PRICES_DIR,
        SHARED_FROM_INSIGHTS, SHARED_FROM_NOTAS,
        SHARED_TO_SNAPSHOTS, SHARED_TO_TESES, SHARED_TO_ALERTS, SHARED_TO_PERGUNTAS,
    ]:
        d.mkdir(parents=True, exist_ok=True)
