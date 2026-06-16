"""Coletor BCB (Banco Central do Brasil) — API SGS.

API publica: https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados/ultimos/{n}?formato=json

Series de interesse:
- 1     USD/BRL PTAX venda (diario)
- 11    Selic taxa diaria
- 433   IPCA 12 meses
- 21619 EUR/BRL PTAX venda
"""
from datetime import date, timedelta
from .base import BaseCollector

SERIES = {
    1: ("usd_brl_ptax", "preco", "BRL/USD"),
    11: ("selic_diaria", "macro", "% a.a."),
    433: ("ipca_12m", "macro", "%"),
    21619: ("eur_brl_ptax", "preco", "BRL/EUR"),
}


class BCBCollector(BaseCollector):
    source_name = "bcb"
    cadence = "daily"
    description = "Cambio USD/EUR PTAX, Selic, IPCA via API BCB SGS"
    enabled = True

    def fetch(self):
        try:
            import requests
        except ImportError:
            raise RuntimeError("requests nao instalado")

        results = []
        for codigo, (commodity, tipo, unidade) in SERIES.items():
            url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados/ultimos/10?formato=json"
            try:
                r = requests.get(url, timeout=15)
                r.raise_for_status()
                rows = r.json()
            except Exception as e:
                results.append({
                    "data_referencia": date.today().isoformat(),
                    "tipo": "erro",
                    "commodity": commodity,
                    "metrica": "fetch_error",
                    "valor": None,
                    "contexto": f"{type(e).__name__}: {e}",
                })
                continue

            for row in rows:
                data_br = row.get("data", "")
                # data formato DD/MM/YYYY
                try:
                    dia, mes, ano = data_br.split("/")
                    data_iso = f"{ano}-{mes}-{dia}"
                except ValueError:
                    continue
                try:
                    valor = float(row.get("valor", "0").replace(",", "."))
                except (ValueError, AttributeError):
                    continue
                results.append({
                    "data_referencia": data_iso,
                    "tipo": tipo,
                    "commodity": commodity,
                    "metrica": "valor",
                    "valor": valor,
                    "unidade": unidade,
                    "contexto": f"sgs={codigo}",
                    "raw": {"sgs_code": codigo, "data_br": data_br},
                })

        return results
