"""Coletor NOPA — esmagamento EUA.

IMPORTANTE: NOPA Monthly Crush Reports sao **restritos a membros pagantes**
da associacao. Nao ha PDF publico mensal disponivel via web.

Estrategia adotada (2026-05-22):
1. Annual Crush Report (publico em wp-content/uploads/dlm_uploads/) — coletado aqui
2. Mensal: usuario consome via StoneX (Resumo Semanal Commodities + Semanal
   Oleos Vegetais sempre citam NOPA crush mensal)
3. Future-proof: bookmarklet poderia capturar qualquer pagina interna NOPA
   se o usuario for fazer login

Fonte: https://www.nopa.org/resources/nopa-monthly-crush-report/
"""
import re
from datetime import date
from .base import BaseCollector


class NopaCollector(BaseCollector):
    source_name = "nopa"
    cadence = "yearly"
    description = "NOPA — Annual Crush Report (publico). Mensal vem via StoneX."
    enabled = True

    def fetch(self):
        try:
            import requests
        except ImportError:
            raise RuntimeError("requests nao instalado")

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0"}

        # Buscar via wp-json os PDFs annual
        try:
            r = requests.get(
                "https://www.nopa.org/wp-json/wp/v2/media?search=crush&per_page=50",
                headers=headers, timeout=20,
            )
            r.raise_for_status()
            items = r.json()
        except Exception as e:
            return [{
                "data_referencia": date.today().isoformat(),
                "tipo": "erro",
                "commodity": "nopa",
                "metrica": "fetch_error",
                "valor": None,
                "contexto": f"{type(e).__name__}: {e}",
            }]

        results = []

        # Filtrar Annual Crush Reports
        annual_pdfs = []
        for item in items:
            title = item.get("title", {}).get("rendered", "")
            url = item.get("source_url", "")
            if "annual crush report" in title.lower() and url.endswith(".pdf"):
                m = re.search(r"(\d{4})", title)
                ano = int(m.group(1)) if m else None
                annual_pdfs.append({"ano": ano, "titulo": title, "url": url})

        # Registrar metadata dos annual reports encontrados
        for pdf in annual_pdfs:
            results.append({
                "data_referencia": f"{pdf['ano']}-12-31" if pdf["ano"] else date.today().isoformat(),
                "tipo": "metadata",
                "commodity": "nopa",
                "metrica": "annual_crush_report_url",
                "valor": pdf["ano"],
                "unidade": "ano",
                "contexto": f"{pdf['titulo']} | {pdf['url']}",
                "raw": pdf,
            })

        # Aviso sobre monthly
        results.append({
            "data_referencia": date.today().isoformat(),
            "tipo": "metadata",
            "commodity": "nopa",
            "metrica": "monthly_status",
            "valor": 0,
            "unidade": "bool",
            "contexto": "NOPA Monthly Crush Reports requerem membership pagante. "
                       "Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' "
                       "(que cita NOPA mensal nas analises).",
        })

        # TODO: baixar Annual Report mais recente, parsear via parse_pdf,
        # extrair: total crush ano, oil yield, meal yield, monthly breakdown se houver.
        return results
