"""Coletor CFTC COT (Commitments of Traders) — posicao dos fundos.

Release: toda sexta-feira ~15:30 NY (dados de terca da semana anterior).

Fonte: ZIP anual em https://www.cftc.gov/files/dea/history/fut_disagg_txt_2026.zip
Formato: TXT/CSV com 191 colunas (disaggregated futures only).

Markets cobertos:
- SOYBEANS — CHICAGO BOARD OF TRADE
- SOYBEAN MEAL — CHICAGO BOARD OF TRADE
- SOYBEAN OIL — CHICAGO BOARD OF TRADE
- CORN — CHICAGO BOARD OF TRADE
- WHEAT-SRW — CHICAGO BOARD OF TRADE

Metricas extraidas (por commodity, por semana):
- open_interest        (total contratos abertos)
- managed_money_long   (fundos comprados)
- managed_money_short  (fundos vendidos)
- managed_money_net    (long - short)
- producer_long        (hedgers/produtores)
- producer_short
- swap_long
- swap_short
"""
from datetime import date, datetime
import io
import csv
import zipfile

from .base import BaseCollector


# ESCOPO (2026-05-26): apenas complexo soja. CORN e WHEAT removidos.
MARKETS = {
    "SOYBEANS - CHICAGO BOARD OF TRADE": "soja_cbot",
    "SOYBEAN OIL - CHICAGO BOARD OF TRADE": "oleo_cbot",
    "SOYBEAN MEAL - CHICAGO BOARD OF TRADE": "farelo_cbot",
}


class CFTCCotCollector(BaseCollector):
    source_name = "cftc_cot"
    cadence = "weekly"
    description = "CFTC COT — posicao fundos em soja/farelo/oleo (sex 15:30 NY)"
    enabled = True

    def fetch(self):
        try:
            import requests
        except ImportError:
            raise RuntimeError("requests nao instalado")

        url = f"https://www.cftc.gov/files/dea/history/fut_disagg_txt_{date.today().year}.zip"

        try:
            r = requests.get(url, timeout=60)
            r.raise_for_status()
            z = zipfile.ZipFile(io.BytesIO(r.content))
            with z.open(z.namelist()[0]) as f:
                raw = f.read().decode("utf-8", errors="replace")
        except Exception as e:
            return [{
                "data_referencia": date.today().isoformat(),
                "tipo": "erro",
                "commodity": "cftc",
                "metrica": "fetch_error",
                "valor": None,
                "contexto": f"{type(e).__name__}: {e}",
            }]

        reader = csv.DictReader(io.StringIO(raw))
        results = []

        for row in reader:
            market = row.get("Market_and_Exchange_Names", "").strip()
            if market not in MARKETS:
                continue

            commodity = MARKETS[market]
            data_ref = row.get("Report_Date_as_YYYY-MM-DD", "").strip()
            if not data_ref:
                continue

            metricas_map = {
                "open_interest": "Open_Interest_All",
                "managed_money_long": "M_Money_Positions_Long_All",
                "managed_money_short": "M_Money_Positions_Short_All",
                "producer_long": "Prod_Merc_Positions_Long_All",
                "producer_short": "Prod_Merc_Positions_Short_All",
                "swap_long": "Swap_Positions_Long_All",
                "swap_short": "Swap__Positions_Short_All",
            }

            valores = {}
            for nome, campo in metricas_map.items():
                raw_val = row.get(campo, "").strip()
                try:
                    valor = float(raw_val.replace(",", "").replace(".", "")) if raw_val else None
                    # CFTC nao usa decimais nesses campos, sao counts
                    if valor is not None:
                        valores[nome] = valor
                        results.append({
                            "data_referencia": data_ref,
                            "tipo": "posicionamento",
                            "commodity": commodity,
                            "metrica": nome,
                            "valor": valor,
                            "unidade": "contratos",
                            "contexto": market,
                        })
                except (ValueError, AttributeError):
                    pass

            # Calcular net positions
            if "managed_money_long" in valores and "managed_money_short" in valores:
                net = valores["managed_money_long"] - valores["managed_money_short"]
                results.append({
                    "data_referencia": data_ref,
                    "tipo": "posicionamento",
                    "commodity": commodity,
                    "metrica": "managed_money_net",
                    "valor": net,
                    "unidade": "contratos",
                    "contexto": f"{market} — long - short",
                })

        return results
