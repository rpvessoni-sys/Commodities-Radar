"""Coletor Conab — Companhia Nacional de Abastecimento (Brasil).

Boletim mensal de safras.

Fonte: https://www.conab.gov.br/info-agro/safras/serie-historica-das-safras
Acesso direto retorna 403 → usar ScraperAPI.
"""
from datetime import date
from .base import BaseCollector
from .scraper import fetch_via_scraper, is_configured


class ConabCollector(BaseCollector):
    source_name = "conab"
    cadence = "monthly"
    description = "Conab — safra BR (links de boletins; dado real via ABIOVE/WASDE/IBGE)"
    enabled = False

    def fetch(self):
        # SITUACAO 2026-05-22:
        # - Pagina principal /info-agro/safras/serie-historica-das-safras carrega
        #   normal (200) MAS os links de Excel/CSV sao renderizados via JS apos
        #   load (estrutura SPA do portal Conab).
        # - HTML estatico nao contem URLs dos arquivos.
        # - Sub-paths como /info-agro/safras/graos retornam 403.
        #
        # Solucoes alternativas (mais robustas):
        # 1. IBGE SIDRA (agregados oficiais soja BR): API JSON em
        #    https://servicodados.ibge.gov.br/api/v3/agregados/6588 (LSPA mensal)
        # 2. ABIOVE producao_entrega.xlsx ja capturado — cobre balanco BR mensal
        # 3. WASDE Brazil ja capturado — projecao por ano-safra
        # 4. Bookmarklet quando precisar de PDF especifico de boletim Conab
        #
        # Cobertura atual via ABIOVE + WASDE:
        # - Producao BR por ano-safra (WASDE)
        # - Esmagamento BR mensal (ABIOVE)
        # - Exportacao BR mensal (ABIOVE)
        # - Estoque BR mensal (ABIOVE)
        # Conab ficaria como redundancia + producao por UF (refino futuro).
        raise NotImplementedError(
            "Conab: site usa JS dinamico para listar boletins. "
            "Cobertura BR ja atendida por ABIOVE (mensal) + WASDE (anual)."
        )
