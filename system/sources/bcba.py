"""Coletor Bolsa de Cereales Buenos Aires — lavoura Argentina.

Fonte: https://www.bolsadecereales.com/estimaciones-agricolas
Acesso direto retorna 403 → usar ScraperAPI.
"""
from datetime import date
from .base import BaseCollector
from .scraper import fetch_via_scraper, is_configured


class BcbaCollector(BaseCollector):
    source_name = "bcba"
    cadence = "weekly"
    description = "Bolsa de Cereales (AR) — estimativas semanais SOJA via ScraperAPI"
    enabled = True

    def fetch(self):
        if not is_configured():
            raise NotImplementedError(
                "BCBA: requer ScraperAPI (site retorna 403 para requests diretas)."
            )

        try:
            from bs4 import BeautifulSoup
        except ImportError:
            raise RuntimeError("bs4 nao instalado")

        url = "https://www.bolsadecereales.com/estimaciones-agricolas"
        try:
            r = fetch_via_scraper(url, render=False, timeout=120)
            if r.status_code != 200:
                raise RuntimeError(f"HTTP {r.status_code}")
            soup = BeautifulSoup(r.text, "lxml")
        except Exception as e:
            return [{
                "data_referencia": date.today().isoformat(),
                "tipo": "erro",
                "commodity": "argentina",
                "metrica": "fetch_error",
                "valor": None,
                "contexto": f"{type(e).__name__}: {e}",
            }]

        results = []
        # Localizar PDFs/Excel dos relatorios semanais
        for a in soup.find_all("a", href=True):
            href = a["href"]
            texto = a.get_text(strip=True)
            if ".pdf" in href.lower() or ".xlsx" in href.lower():
                # ESCOPO (2026-05-26): apenas soja. Maiz/trigo descartados.
                if "soja" in texto.lower():
                    if href.startswith("/"):
                        href = "https://www.bolsadecereales.com" + href
                    results.append({
                        "data_referencia": date.today().isoformat(),
                        "tipo": "metadata",
                        "commodity": "argentina",
                        "metrica": "link_relatorio",
                        "valor": None,
                        "unidade": None,
                        "contexto": f"{texto} | {href}",
                        "raw": {"texto": texto, "href": href},
                    })

        if not results:
            results.append({
                "data_referencia": date.today().isoformat(),
                "tipo": "metadata",
                "commodity": "argentina",
                "metrica": "page_fetched",
                "valor": 1,
                "unidade": "bool",
                "contexto": "BCBA acessivel via scraper mas sem links de relatorio detectados.",
            })

        # TODO: baixar PDFs semanais, parsear via parse_pdf, extrair producao/area/condicao.
        return results
