# -*- coding: utf-8 -*-
"""Teste do detector de frescor por commodity (perna CBOT travada/defasada).

Cobre o bug real de jun/2026: farelo ZM=F preso no fechamento de 18/jun enquanto
soja/oleo andaram — crush/ratio/oil-share/Mesa herdavam o numerador velho sem aviso.
"""
import sqlite3
import sys
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from indicators import cbot_freshness  # noqa: E402


def _conn_com(linhas):
    """sqlite :memory: com dados_publicos minimo; linhas = (commodity, data, valor)."""
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    conn.execute(
        "CREATE TABLE dados_publicos (fonte TEXT, data_referencia TEXT, tipo TEXT, "
        "commodity TEXT, metrica TEXT, valor REAL)"
    )
    for commodity, data_ref, valor in linhas:
        conn.execute(
            "INSERT INTO dados_publicos (fonte, data_referencia, tipo, commodity, metrica, valor) "
            "VALUES ('cme_cbot', ?, 'preco', ?, 'fechamento', ?)",
            (data_ref, commodity, valor),
        )
    return conn


class TestCbotFreshness(unittest.TestCase):
    def test_perna_defasada_marca_stale(self):
        # Farelo preso em 18/jun; soja/oleo andaram ate 19/jun -> farelo defasado.
        conn = _conn_com([
            ("soja_cbot", "2026-06-18", 1122.75), ("soja_cbot", "2026-06-19", 1147.0),
            ("oleo_cbot", "2026-06-18", 69.69), ("oleo_cbot", "2026-06-19", 66.66),
            ("farelo_cbot", "2026-06-12", 301.30), ("farelo_cbot", "2026-06-18", 301.30),
        ])
        fr = cbot_freshness(conn, date(2026, 6, 22))
        self.assertTrue(fr["farelo_cbot"]["stale"])
        self.assertFalse(fr["soja_cbot"]["stale"])
        self.assertFalse(fr["oleo_cbot"]["stale"])
        self.assertEqual(fr["farelo_cbot"]["ref_date"], "2026-06-19")

    def test_perna_travada_delta_zero(self):
        # Farelo com data corrente mas valor repetido (clobber do intraday) e o
        # resto do complexo se moveu -> travado.
        conn = _conn_com([
            ("soja_cbot", "2026-06-19", 1140.0), ("soja_cbot", "2026-06-22", 1147.0),
            ("oleo_cbot", "2026-06-19", 67.0), ("oleo_cbot", "2026-06-22", 66.5),
            ("farelo_cbot", "2026-06-19", 301.30), ("farelo_cbot", "2026-06-22", 301.30),
        ])
        fr = cbot_freshness(conn, date(2026, 6, 22))
        self.assertTrue(fr["farelo_cbot"]["stale"])
        self.assertFalse(fr["soja_cbot"]["stale"])

    def test_tudo_fresco_nao_marca(self):
        conn = _conn_com([
            ("soja_cbot", "2026-06-19", 1140.0), ("soja_cbot", "2026-06-22", 1147.0),
            ("oleo_cbot", "2026-06-19", 67.0), ("oleo_cbot", "2026-06-22", 66.5),
            ("farelo_cbot", "2026-06-19", 300.0), ("farelo_cbot", "2026-06-22", 303.5),
        ])
        fr = cbot_freshness(conn, date(2026, 6, 22))
        self.assertFalse(any(fr[c]["stale"] for c in fr))

    def test_dia_chato_todos_flat_nao_falso_positivo(self):
        # Se NINGUEM se moveu (delta 0 em todos), nao e sinal de trava -> nao stale.
        conn = _conn_com([
            ("soja_cbot", "2026-06-19", 1140.0), ("soja_cbot", "2026-06-22", 1140.0),
            ("oleo_cbot", "2026-06-19", 67.0), ("oleo_cbot", "2026-06-22", 67.0),
            ("farelo_cbot", "2026-06-19", 300.0), ("farelo_cbot", "2026-06-22", 300.0),
        ])
        fr = cbot_freshness(conn, date(2026, 6, 22))
        self.assertFalse(any(fr[c]["stale"] for c in fr))


if __name__ == "__main__":
    unittest.main()
