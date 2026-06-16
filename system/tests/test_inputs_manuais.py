# -*- coding: utf-8 -*-
"""Testes do parser da camada manual (inputs_manuais._parse) — puro, sem DB."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from inputs_manuais import _parse  # noqa: E402


TOML_OK = """
[[fisico]]
data = "2026-06-15"
produto = "farelo"
praca = "paranagua_pr"
valor = 1750.0
obs = "real"

[[fisico]]
data = "2026-06-15"
produto = "soja"
praca = "rancharia_sp"
valor = 124.5

[[curva]]
produto = "oleo"
venc = "n26"
valor = 75.5
detalhe = "Fabio 15/jun"

[[param]]
chave = "rin_d4"
valor = 2.2
fonte = "call"
"""


class TestParse(unittest.TestCase):
    def setUp(self):
        self.p = _parse(TOML_OK)

    def test_contagens(self):
        self.assertEqual(len(self.p["fisico"]), 2)
        self.assertEqual(len(self.p["curva"]), 1)
        self.assertEqual(len(self.p["param"]), 1)
        self.assertEqual(self.p["erros"], [])

    def test_fisico_campos(self):
        f = self.p["fisico"][0]
        self.assertEqual(f["produto"], "farelo")
        self.assertEqual(f["valor"], 1750.0)
        self.assertEqual(f["obs"], "real")
        self.assertIsNone(self.p["fisico"][1]["valor_usd"])

    def test_curva_venc_uppercase(self):
        self.assertEqual(self.p["curva"][0]["venc"], "N26")

    def test_param(self):
        self.assertEqual(self.p["param"][0]["chave"], "rin_d4")
        self.assertEqual(self.p["param"][0]["valor"], 2.2)

    def test_produto_invalido_vira_erro_nao_crash(self):
        p = _parse('[[fisico]]\ndata="2026-06-15"\nproduto="milho"\npraca="x"\nvalor=1.0\n')
        self.assertEqual(len(p["fisico"]), 0)
        self.assertEqual(len(p["erros"]), 1)
        self.assertIn("milho", p["erros"][0])

    def test_toml_invalido_nao_crash(self):
        p = _parse("isto não é toml válido [[[")
        self.assertTrue(p["erros"])

    def test_vazio(self):
        p = _parse("")
        self.assertEqual(p["fisico"], [])
        self.assertEqual(p["erros"], [])


if __name__ == "__main__":
    unittest.main()
