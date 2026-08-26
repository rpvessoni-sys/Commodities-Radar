# -*- coding: utf-8 -*-
"""Teste do dead-man switch do pipeline (heartbeat.decidir).

Cobre o apagao real de 06/08 a 26/08/2026: o radar ficou 20 dias sem fechar um
run OK (job preso em "waiting" segurando o grupo de concorrencia) e ninguem foi
avisado. A regra aqui e a que transforma esse silencio em alarme.
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from heartbeat import decidir  # noqa: E402


class TestDecidir(unittest.TestCase):

    def test_pipeline_vivo_nao_alerta(self):
        alerta, msg = decidir(horas_parado=0.3, presos=[], max_horas=3, hora_utc=0)
        self.assertFalse(alerta)
        self.assertEqual(msg, "")

    def test_dentro_do_limite_nao_alerta(self):
        # cron do GitHub e best-effort: 2h de atraso ainda e normal
        alerta, _ = decidir(horas_parado=2.9, presos=[], max_horas=3, hora_utc=4)
        self.assertFalse(alerta)

    def test_primeira_deteccao_alerta_em_qualquer_hora(self):
        # acabou de estourar o limite -> passa mesmo em hora fora da janela anti-spam
        alerta, msg = decidir(horas_parado=3.5, presos=[], max_horas=3, hora_utc=7)
        self.assertTrue(alerta)
        self.assertIn("RADAR PARADO", msg)

    def test_apagao_longo_so_repete_de_4_em_4_horas(self):
        # o caso dos 20 dias: nao pode virar 24 mensagens/dia
        alerta_fora, _ = decidir(horas_parado=480, presos=[], max_horas=3, hora_utc=7)
        alerta_na_hora, _ = decidir(horas_parado=480, presos=[], max_horas=3, hora_utc=8)
        self.assertFalse(alerta_fora)
        self.assertTrue(alerta_na_hora)

    def test_sem_run_ok_conhecido_alerta(self):
        alerta, msg = decidir(horas_parado=None, presos=[], max_horas=3, hora_utc=8)
        self.assertTrue(alerta)
        self.assertIn("nenhum run bem-sucedido", msg)

    def test_lista_os_runs_presos_cancelados(self):
        presos = [{"numero": 5306, "status": "waiting", "horas": 480.0}]
        _, msg = decidir(horas_parado=480, presos=presos, max_horas=3, hora_utc=8)
        self.assertIn("#5306", msg)
        self.assertIn("waiting", msg)


if __name__ == "__main__":
    unittest.main()
