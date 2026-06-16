"""Coletores de fontes publicas — Fase 2 do Commodities Radar.

Cada modulo nesta pasta implementa um coletor que herda de BaseCollector.
Lista de coletores conhecidos esta em sources.registry.

Uso:
    python main.py public                  # roda todos os habilitados
    python main.py public --source cme     # roda so o CME
    python main.py public --list           # lista todos disponiveis
"""
