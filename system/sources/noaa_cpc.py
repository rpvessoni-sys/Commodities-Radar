"""Coletor NOAA CPC — clima EUA + status ENSO global.

Fonte: https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso_advisory/

Dados-chave:
- ENSO Alert System Status (La Nina Advisory / El Nino Watch / Neutral)
- ONI (Oceanic Nino Index)
"""
import re
from datetime import date
from .base import BaseCollector


class NoaaCpcCollector(BaseCollector):
    source_name = "noaa_cpc"
    cadence = "monthly"
    description = "NOAA CPC — status ENSO (La Nina/Neutral/El Nino) e discussao mensal"
    enabled = True

    def fetch(self):
        try:
            import requests
            from bs4 import BeautifulSoup
        except ImportError:
            raise RuntimeError("requests/bs4 nao instalado")

        results = []
        headers = {"User-Agent": "Mozilla/5.0 commodities-radar/1.0"}

        # ENSO Discussion (texto principal)
        url_disc = "https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso_advisory/ensodisc.shtml"
        try:
            r = requests.get(url_disc, headers=headers, timeout=30)
            r.raise_for_status()
            soup = BeautifulSoup(r.text, "lxml")
            texto = soup.get_text(separator="\n")

            # ENSO Alert System Status
            # Padroes: "ENSO Alert System Status: La Nina Advisory" / "Final La Nina Advisory" / etc
            match_status = re.search(
                r"ENSO\s+Alert\s+System\s+Status[:\s]+([^\n]{3,80})",
                texto,
                re.IGNORECASE,
            )
            status_text = match_status.group(1).strip() if match_status else "Indeterminado"

            # Classificar
            status_norm = "neutral"
            if "la nina" in status_text.lower():
                status_norm = "la_nina"
            elif "el nino" in status_text.lower():
                status_norm = "el_nino"

            results.append({
                "data_referencia": date.today().isoformat(),
                "tipo": "clima_macro",
                "commodity": "enso",
                "metrica": "status",
                "valor": {"la_nina": -1.0, "neutral": 0.0, "el_nino": 1.0}.get(status_norm, 0.0),
                "unidade": "categorico",
                "contexto": f"ENSO Alert: {status_text}",
                "raw": {"status_text": status_text, "status_norm": status_norm},
            })

            # Tentar extrair ONI da discussao
            # Padrao: "ONI value of X.XC" ou similar
            match_oni = re.search(r"(?:ONI|Nino[\s-]3\.4)[^\n]*?([+-]?\d+\.\d+)\s*(?:°?C|Celsius)", texto, re.IGNORECASE)
            if match_oni:
                try:
                    oni = float(match_oni.group(1))
                    results.append({
                        "data_referencia": date.today().isoformat(),
                        "tipo": "clima_macro",
                        "commodity": "enso",
                        "metrica": "oni",
                        "valor": oni,
                        "unidade": "C anomalia",
                        "contexto": "Oceanic Nino Index (ENSO discussion)",
                    })
                except ValueError:
                    pass

        except Exception as e:
            results.append({
                "data_referencia": date.today().isoformat(),
                "tipo": "erro",
                "commodity": "enso",
                "metrica": "fetch_error",
                "valor": None,
                "contexto": f"{type(e).__name__}: {e}",
            })

        return results
