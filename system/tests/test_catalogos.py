# -*- coding: utf-8 -*-
"""Validacao dos catalogos TOML editados a mao (tributario_watch, alerts_config).

Esses arquivos sao a 'fonte da verdade' editavel — um typo de status/direcao
quebraria silenciosamente o Monitor Tributario e os Drivers. Aqui vira erro de teste.
"""
import sys
import tomllib
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

SYSTEM = Path(__file__).resolve().parent.parent

STATUS_VALIDOS = {"vigente", "tramitacao", "adiado", "monitorando", "encerrado"}
DIRECOES_VALIDAS = {"alta", "baixa", "neutro", "misto"}
PRODUTOS_VALIDOS = {"soja", "farelo", "oleo_soja"}
CAMPOS_OBRIGATORIOS = {"id", "titulo", "tipo", "jurisdicao", "status",
                       "impacto", "direcao", "produtos", "mecanismo"}


class TestTributarioWatch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(SYSTEM / "tributario_watch.toml", "rb") as f:
            cls.catalogo = tomllib.load(f)
        cls.eventos = cls.catalogo.get("evento", [])

    def test_tem_eventos(self):
        self.assertGreaterEqual(len(self.eventos), 5)

    def test_campos_obrigatorios(self):
        for ev in self.eventos:
            faltando = CAMPOS_OBRIGATORIOS - set(ev.keys())
            self.assertFalse(faltando, f"{ev.get('id', '?')}: faltam {faltando}")

    def test_enums_validos(self):
        for ev in self.eventos:
            self.assertIn(ev["status"], STATUS_VALIDOS, ev["id"])
            self.assertIn(ev["direcao"], DIRECOES_VALIDAS, ev["id"])
            for p in ev["produtos"]:
                self.assertIn(p, PRODUTOS_VALIDOS, f"{ev['id']}: produto '{p}'")

    def test_ids_unicos(self):
        ids = [ev["id"] for ev in self.eventos]
        self.assertEqual(len(ids), len(set(ids)), "id duplicado no catalogo")

    def test_datas_iso(self):
        import re
        iso = re.compile(r"^\d{4}-\d{2}-\d{2}$")
        for ev in self.eventos:
            for campo in ("vigencia_ate", "proximo_data", "atualizado_em"):
                v = ev.get(campo, "")
                if v:
                    self.assertRegex(v, iso, f"{ev['id']}.{campo}='{v}' nao e ISO")


class TestAlertsConfig(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(SYSTEM / "alerts_config.toml", "rb") as f:
            cls.cfg = tomllib.load(f)
        cls.niveis = cls.cfg.get("niveis", [])

    def test_tem_niveis(self):
        self.assertGreaterEqual(len(self.niveis), 4)

    def test_suporte_abaixo_da_resistencia(self):
        for n in self.niveis:
            self.assertLess(n["suporte"], n["resistencia"], n["commodity"])

    def test_variacao_positiva(self):
        for n in self.niveis:
            self.assertGreater(n.get("variacao_dia_pct_alert", 3.0), 0)


if __name__ == "__main__":
    unittest.main()
