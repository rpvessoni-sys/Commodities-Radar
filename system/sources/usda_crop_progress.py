"""Coletor USDA NASS Crop Progress — estagio e condicao da lavoura EUA.

Release: segunda ~16h NY (abril-novembro).

API NASS Quick Stats: https://quickstats.nass.usda.gov/api
Doc: https://www.nass.usda.gov/Quick_Stats/API/

Requer API key gratuita. Registrar em: https://quickstats.nass.usda.gov/api#param_define
Adicionar no .env: NASS_API_KEY=xxxxxxxx

Dados-chave:
- SOYBEANS - PROGRESS, MEASURED IN PCT PLANTED   (% plantado)
- SOYBEANS - PROGRESS, MEASURED IN PCT EMERGED   (% emergido)
- SOYBEANS - CONDITION, MEASURED IN PCT EXCELLENT (% condicao excelente)
- SOYBEANS - CONDITION, MEASURED IN PCT GOOD
- SOYBEANS - CONDITION, MEASURED IN PCT POOR
- SOYBEANS - PROGRESS, MEASURED IN PCT HARVESTED (set-nov)

ESCOPO (2026-05-26): apenas SOYBEANS. Corn removido (foco no complexo soja).
"""
import os
from datetime import date
from .base import BaseCollector


SHORT_DESCS = [
    "SOYBEANS - PROGRESS, MEASURED IN PCT PLANTED",
    "SOYBEANS - PROGRESS, MEASURED IN PCT EMERGED",
    "SOYBEANS - PROGRESS, MEASURED IN PCT HARVESTED",
    "SOYBEANS - CONDITION, MEASURED IN PCT EXCELLENT",
    "SOYBEANS - CONDITION, MEASURED IN PCT GOOD",
    "SOYBEANS - CONDITION, MEASURED IN PCT POOR",
]


class UsdaCropProgressCollector(BaseCollector):
    source_name = "usda_crop_progress"
    cadence = "weekly"
    description = "USDA NASS Crop Progress — estagio + condicao soja EUA"
    enabled = True

    def fetch(self):
        api_key = os.getenv("NASS_API_KEY", "").strip()
        if not api_key:
            raise NotImplementedError(
                "USDA Crop Progress: registre NASS_API_KEY em .env. "
                "Gratuita: https://quickstats.nass.usda.gov/api#param_define"
            )

        try:
            import requests
        except ImportError:
            raise RuntimeError("requests nao instalado")

        results = []
        current_year = date.today().year

        for short_desc in SHORT_DESCS:
            params = {
                "key": api_key,
                "short_desc": short_desc,
                "agg_level_desc": "NATIONAL",
                "year__GE": current_year - 1,
                "format": "JSON",
            }
            try:
                r = requests.get(
                    "https://quickstats.nass.usda.gov/api/api_GET/",
                    params=params, timeout=30,
                )
                r.raise_for_status()
                data = r.json()
            except Exception as e:
                results.append({
                    "data_referencia": date.today().isoformat(),
                    "tipo": "erro",
                    "commodity": "usda_nass",
                    "metrica": "fetch_error",
                    "valor": None,
                    "contexto": f"{short_desc}: {e}",
                })
                continue

            # commodity: SOYBEANS ou CORN
            commodity_raw = short_desc.split(" - ")[0].lower()
            commodity = f"{commodity_raw}_eua"

            # metrica: PCT_PLANTED / PCT_GOOD / etc
            descricao = short_desc.split(" - ", 1)[1] if " - " in short_desc else short_desc
            metrica = descricao.replace("PROGRESS, MEASURED IN PCT ", "pct_") \
                               .replace("CONDITION, MEASURED IN PCT ", "cond_pct_") \
                               .lower().replace(" ", "_")

            for row in data.get("data", []):
                week_ending = row.get("week_ending")
                if not week_ending:
                    continue
                try:
                    valor = float(row.get("Value", "").replace(",", ""))
                except (ValueError, AttributeError):
                    continue
                results.append({
                    "data_referencia": week_ending,
                    "tipo": "lavoura",
                    "commodity": commodity,
                    "metrica": metrica,
                    "valor": valor,
                    "unidade": "%",
                    "contexto": f"{short_desc}",
                })

        return results
