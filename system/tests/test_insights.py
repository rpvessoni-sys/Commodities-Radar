# -*- coding: utf-8 -*-
"""Testes do parser de frontmatter dos insights (inclui convencao vies)."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from insights import (_parse_frontmatter, _extract_resumo_executivo,  # noqa: E402
                      _extract_revisoes, _slugify)


DOC = """---
data: 2026-06-11
titulo: Ratio 81% abre janela
tags: [farelo, auto-claude]
fontes:
  - Sistema 11/jun
  - NAG 10/jun
status: ativa
vies: [bear-farelo, bull-oleo_soja]
---

## Resumo executivo

- Ponto um com numero 81,4%
- Ponto dois

## Outra secao

- nao deve entrar no resumo

## Revisão programada

- **D+7**: 2026-06-18 — ratio fechou <80%?
- **D+90**: 2026-09-09
- linha sem formato deve ser ignorada
"""


class TestFrontmatter(unittest.TestCase):
    def setUp(self):
        self.fm, self.body = _parse_frontmatter(DOC)

    def test_campos_escalares(self):
        self.assertEqual(self.fm["data"], "2026-06-11")
        self.assertEqual(self.fm["status"], "ativa")

    def test_lista_inline(self):
        self.assertEqual(self.fm["tags"], ["farelo", "auto-claude"])
        self.assertEqual(self.fm["vies"], ["bear-farelo", "bull-oleo_soja"])

    def test_lista_multilinha(self):
        self.assertEqual(len(self.fm["fontes"]), 2)
        self.assertIn("NAG 10/jun", self.fm["fontes"])

    def test_resumo_executivo_para_na_proxima_secao(self):
        bullets = _extract_resumo_executivo(self.body)
        self.assertEqual(len(bullets), 2)
        self.assertIn("81,4%", bullets[0])

    def test_sem_frontmatter_retorna_corpo_intacto(self):
        fm, body = _parse_frontmatter("# Sem frontmatter\ntexto")
        self.assertEqual(fm, {})
        self.assertTrue(body.startswith("# Sem"))

    def test_revisoes_programadas(self):
        revisoes = _extract_revisoes(self.body)
        self.assertEqual(len(revisoes), 2)
        self.assertEqual(revisoes[0]["label"], "D+7")
        self.assertEqual(revisoes[0]["data"], "2026-06-18")
        self.assertIn("ratio fechou", revisoes[0]["texto"])
        self.assertEqual(revisoes[1]["data"], "2026-09-09")


class TestSlugify(unittest.TestCase):
    def test_acentos_e_simbolos(self):
        self.assertEqual(_slugify("Ratio 81% → janela de COMPRA!"),
                         "ratio-81-janela-de-compra")


if __name__ == "__main__":
    unittest.main()
