# -*- coding: utf-8 -*-
"""Testes do parser NAG (offline, com fixture HTML).

Protege contra: mudanca silenciosa de layout, regressao no parse de numero BR,
mapeamento de praca quebrado. Roda sem rede e sem ScraperAPI.
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sources.nag_fisico import _parse_num_br, _praca_slug, iter_tabelas  # noqa: E402


FIXTURE = """
<html><body>
<div class="table-content">
  <h3>Fechamento: 10/06/2026</h3>
  <table>
    <tr><th>Praça</th><th>Cotação Atual (R$/t)</th><th>Variação (%)</th></tr>
    <tr><td>Média Rio Grande do Sul (Clicmercado)</td><td>1.710,00</td><td>0,00</td></tr>
    <tr><td>Mato Grosso (IMEA)</td><td>1.562,59</td><td>-1,64</td></tr>
  </table>
</div>
<div class="table-content">
  <h3>Fechamento: 10/06/2026</h3>
  <table>
    <tr><th>Praça</th><th>Cotação Atual (R$/t)</th><th>Variação (%)</th></tr>
    <tr><td>Duplicada mobile</td><td>999,99</td><td>0,00</td></tr>
  </table>
</div>
<div class="table-content">
  <h3>Fechamento: 09/06/2026</h3>
  <table>
    <tr><th>Mês</th><th>US$/tonelada curta</th><th>Variação</th></tr>
    <tr><td>Junho/26</td><td>+0,05</td><td>0,00</td></tr>
  </table>
</div>
</body></html>
"""


class TestParseNumBR(unittest.TestCase):
    def test_milhar_br(self):
        self.assertEqual(_parse_num_br("1.710,00"), 1710.0)

    def test_negativo(self):
        self.assertEqual(_parse_num_br("-1,64"), -1.64)

    def test_positivo_com_sinal(self):
        self.assertEqual(_parse_num_br("+0,05"), 0.05)

    def test_vazio_e_traco(self):
        self.assertIsNone(_parse_num_br(""))
        self.assertIsNone(_parse_num_br("-"))
        self.assertIsNone(_parse_num_br("N/A"))

    def test_porcentagem(self):
        self.assertEqual(_parse_num_br("12,5%"), 12.5)


class TestPracaSlug(unittest.TestCase):
    def test_pracas_conhecidas(self):
        self.assertEqual(_praca_slug("Média Rio Grande do Sul (Clicmercado)"), "rs_media")
        self.assertEqual(_praca_slug("Mato Grosso (IMEA)"), "mt_imea")
        self.assertEqual(_praca_slug("Rondonópolis/MT (BCSP)"), "rondonopolis_mt")

    def test_fallback_generico_estavel(self):
        self.assertEqual(_praca_slug("Ponta Grossa/PR"), "ponta_grossa_pr")


class TestIterTabelas(unittest.TestCase):
    def test_dedup_por_data_e_ordem(self):
        tabelas = list(iter_tabelas(FIXTURE))
        datas = [d for d, _ in tabelas]
        # 2 tabelas de 10/06 (dup desktop/mobile) viram 1; 09/06 entra
        self.assertEqual(datas, ["2026-06-10", "2026-06-09"])

    def test_max_fechamentos(self):
        tabelas = list(iter_tabelas(FIXTURE, max_fechamentos=1))
        self.assertEqual(len(tabelas), 1)

    def test_celulas_da_primeira_tabela(self):
        _, tb = next(iter(iter_tabelas(FIXTURE)))
        rows = tb.find_all("tr")
        cells = [c.get_text(strip=True) for c in rows[1].find_all("td")]
        self.assertIn("Rio Grande do Sul", cells[0])
        self.assertEqual(_parse_num_br(cells[1]), 1710.0)


if __name__ == "__main__":
    unittest.main()
