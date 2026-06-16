# -*- coding: utf-8 -*-
"""Teste da formula do ratio Far/Soj — a metrica central do comprador."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from indicators import far_soj_ratio_pct  # noqa: E402


class TestFarSojRatio(unittest.TestCase):
    def test_valor_de_11jun2026(self):
        # Caso real validado a mao: farelo 303.60 USD/sht, soja 1119.00 cts/bu
        # 303.60 / (11.19 x 33.333) = 81.39%
        self.assertAlmostEqual(far_soj_ratio_pct(303.60, 1119.00), 81.39, places=1)

    def test_fronteira_zona_compra(self):
        # ratio exatamente 80%: farelo = 0.80 x soja_usd_bu x 33.333
        soja = 1200.0  # cts/bu -> 12 USD/bu
        farelo = 0.80 * 12.0 * (2000.0 / 60.0)
        self.assertAlmostEqual(far_soj_ratio_pct(farelo, soja), 80.0, places=6)

    def test_proporcionalidade(self):
        # dobrar o farelo dobra o ratio; dobrar a soja corta pela metade
        base = far_soj_ratio_pct(300.0, 1100.0)
        self.assertAlmostEqual(far_soj_ratio_pct(600.0, 1100.0), base * 2, places=6)
        self.assertAlmostEqual(far_soj_ratio_pct(300.0, 2200.0), base / 2, places=6)


if __name__ == "__main__":
    unittest.main()
