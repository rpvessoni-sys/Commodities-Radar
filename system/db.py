"""SQLite helpers."""
import sqlite3
from contextlib import contextmanager
from pathlib import Path

import config

SCHEMA_PATH = Path(__file__).parent / "schema.sql"


def init_db():
    config.ensure_dirs()
    with connect() as conn:
        conn.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))


@contextmanager
def connect():
    conn = sqlite3.connect(config.DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()
