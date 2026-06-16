# -*- coding: utf-8 -*-
"""Testes da banda estatistica do forecast (funcao pura, sem DB)."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from forecast import _calcular_banda, _slope  # noqa: E402


def serie(valores):
    return [(f"2026-05-{i+1:02d}", v) for i, v in enumerate(valores)]


class TestCalcularBanda(unittest.TestCase):
    def test_ordem_baixo_central_alto(self):
        hist = serie([100 + i * 0.5 for i in range(26)])
        b = _calcular_banda(hist, 7)
        self.assertLess(b["baixo"], b["central"])
        self.assertLess(b["central"], b["alto"])

    def test_uptrend_vies_altista(self):
        hist = serie([100 + i * 2 for i in range(26)])  # alta forte
        b = _calcular_banda(hist, 7)
        self.assertEqual(b["vies"], "altista")
        self.assertGreater(b["central"], b["spot"])

    def test_downtrend_vies_baixista(self):
        hist = serie([200 - i * 2 for i in range(26)])
        b = _calcular_banda(hist, 7)
        self.assertEqual(b["vies"], "baixista")

    def test_flat_vies_lateral(self):
        # serie constante: slope 0, spot=MA20 → drift+revert ~0
        hist = serie([150.0] * 26)
        b = _calcular_banda(hist, 7)
        self.assertEqual(b["vies"], "lateral")

    def test_banda_alarga_com_horizonte(self):
        hist = serie([100 + (i % 3) for i in range(30)])  # com vol
        b7 = _calcular_banda(hist, 7)
        b30 = _calcular_banda(hist, 30)
        self.assertGreater(b30["alto"] - b30["baixo"], b7["alto"] - b7["baixo"])

    def test_mean_reversion_puxa_pra_ma20(self):
        # spot muito abaixo da MA20 → componente de reversao positivo
        hist = serie([150.0] * 25 + [100.0])
        b = _calcular_banda(hist, 7)
        # central deve ficar ACIMA do spot (puxado pra media), mesmo com slope negativo fraco
        self.assertGreater(b["ma20"], b["spot"])


class TestSlope(unittest.TestCase):
    def test_slope_linear_exato(self):
        x = list(range(10))
        y = [3 + 2 * i for i in x]
        self.assertAlmostEqual(_slope(x, y), 2.0, places=9)

    def test_slope_serie_curta(self):
        self.assertEqual(_slope([1], [5]), 0.0)


if __name__ == "__main__":
    unittest.main()
