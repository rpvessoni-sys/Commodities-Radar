# -*- coding: utf-8 -*-
"""Testes do gerador de graficos SVG inline (charts_svg).

Protege contra: crash em casos degenerados, ticks de eixo nao redondos,
nivel que nao expande o range do Y, rotulo sem escape HTML, None na serie.
Roda sem rede e sem dependencia externa (so stdlib).
"""
import sys
import unittest
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from charts_svg import bar_spread, line_chart, sparkline  # noqa: E402


def _serie(valores, inicio="2026-01-01", passo_dias=1):
    """Monta [(data_iso, valor)] diaria (ou espacada) a partir de inicio."""
    d0 = date.fromisoformat(inicio)
    return [((d0 + timedelta(days=i * passo_dias)).isoformat(), v)
            for i, v in enumerate(valores)]


class TestSparkline(unittest.TestCase):
    def test_degenerados_retornam_vazio(self):
        self.assertEqual(sparkline([]), "")
        self.assertEqual(sparkline([1.0]), "")
        self.assertEqual(sparkline([None, None, 2.0]), "")  # so 1 valido
        self.assertEqual(sparkline([5.0, 5.0, 5.0]), "")    # range zero

    def test_estrutura_basica(self):
        svg = sparkline([1.0, 3.0, 2.0])
        self.assertIn("<svg", svg)
        self.assertIn("<polyline", svg)
        self.assertIn('fill="none"', svg)
        self.assertIn('r="2.5"', svg)  # circulo no ultimo ponto
        self.assertIn("var(--accent)", svg)

    def test_cor_customizada(self):
        self.assertIn("var(--bull)", sparkline([1.0, 2.0], cor="var(--bull)"))

    def test_none_filtrado_sem_crash(self):
        svg = sparkline([1.0, None, 2.0, None, 3.0])
        self.assertIn("<polyline", svg)
        self.assertIn("<circle", svg)


class TestLineChart(unittest.TestCase):
    def test_serie_curta_retorna_vazio(self):
        self.assertEqual(line_chart([]), "")
        self.assertEqual(line_chart(_serie([100.0])), "")
        self.assertEqual(line_chart(_serie([100.0, None])), "")  # 1 valido

    def test_estrutura_basica(self):
        svg = line_chart(_serie([100.0, 105.0, 103.0, 110.0]))
        for trecho in ("<svg", "<polyline", "<path", "<circle", 'r="3"',
                       'stroke-width="2"', 'opacity="0.08"'):
            self.assertIn(trecho, svg)

    def test_none_filtrado_sem_crash(self):
        svg = line_chart(_serie([100.0, None, 105.0, None, 110.0]))
        self.assertIn("<polyline", svg)

    def test_ticks_redondos(self):
        # serie 0..97: ticks devem cair em 25/50/75 ou 20/40/60/80
        svg = line_chart(_serie([float(v) for v in range(98)]))
        tem_25 = all(">{}<".format(t) in svg for t in (25, 50, 75))
        tem_20 = all(">{}<".format(t) in svg for t in (20, 40, 60, 80))
        self.assertTrue(tem_25 or tem_20,
                        "ticks do eixo Y nao sao numeros redondos")

    def test_nivel_tracejado_e_expande_range(self):
        svg = line_chart(_serie([100.0 + i for i in range(11)]),
                         niveis={"suporte 90": 90.0})
        self.assertIn('stroke-dasharray="5 3"', svg)
        self.assertIn("suporte 90", svg)
        self.assertIn("var(--warn)", svg)
        # nivel abaixo da serie expande o eixo: tick 90 aparece
        self.assertIn(">90<", svg)

    def test_fmt_valor_respeitado(self):
        svg = line_chart(_serie([100.0, 110.0]),
                         fmt_valor=lambda v: "R$ {:.1f}".format(v))
        self.assertIn("R$ 110.0", svg)  # anotacao do ultimo ponto

    def test_datas_curtas_dd_mm(self):
        svg = line_chart(_serie([100.0, 105.0, 102.0], inicio="2026-03-01"))
        self.assertIn("01/03", svg)  # cobre < 120 dias -> DD/MM

    def test_datas_longas_mm_aa(self):
        svg = line_chart(_serie([100.0 + i for i in range(10)],
                                passo_dias=30))  # ~270 dias
        self.assertIn("01/26", svg)  # >= 120 dias -> MM/AA

    def test_label_y_vertical_com_escape(self):
        svg = line_chart(_serie([1.0, 2.0]), label_y="US$/t <bruto>")
        self.assertIn("rotate(-90)", svg)
        self.assertIn("US$/t &lt;bruto&gt;", svg)
        self.assertNotIn("<bruto>", svg)


class TestBarSpread(unittest.TestCase):
    def test_vazio_retorna_vazio(self):
        self.assertEqual(bar_spread([]), "")
        self.assertEqual(bar_spread([("x", None)]), "")

    def test_misto_bull_e_bear(self):
        svg = bar_spread([("JUL/26", 12.5), ("AGO/26", -3.0), ("SET/26", 5.0)])
        self.assertIn("var(--bull)", svg)
        self.assertIn("var(--bear)", svg)
        self.assertIn("JUL/26", svg)
        self.assertIn("<rect", svg)

    def test_todos_positivos_sem_bear(self):
        svg = bar_spread([("A", 1.0), ("B", 2.0), ("C", 3.0)])
        self.assertIn("var(--bull)", svg)
        self.assertNotIn("var(--bear)", svg)

    def test_escape_de_rotulo(self):
        svg = bar_spread([("A&B <x>", 1.0), ("C", -1.0)])
        self.assertIn("A&amp;B &lt;x&gt;", svg)
        self.assertNotIn("<x>", svg)


if __name__ == "__main__":
    unittest.main()
