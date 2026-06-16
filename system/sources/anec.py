"""Coletor ANEC — Associacao Nacional dos Exportadores de Cereais.

Boletim semanal de embarques BR.

Fonte: https://anec.com.br/estatisticas/
"""
from datetime import date
from .base import BaseCollector


class AnecCollector(BaseCollector):
    source_name = "anec"
    cadence = "weekly"
    description = "ANEC — embarques semanais BR (soja, farelo) — escopo restrito ao complexo soja"
    enabled = True

    def fetch(self):
        try:
            import requests
            from bs4 import BeautifulSoup
        except ImportError:
            raise RuntimeError("requests/bs4 nao instalado")

        results = []
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "pt-BR,pt;q=0.9",
        }

        try:
            r = requests.get("https://anec.com.br/estatisticas/", headers=headers, timeout=30)
            r.raise_for_status()
            soup = BeautifulSoup(r.text, "lxml")
        except Exception as e:
            return [{
                "data_referencia": date.today().isoformat(),
                "tipo": "erro",
                "commodity": "anec",
                "metrica": "fetch_error",
                "valor": None,
                "contexto": f"{type(e).__name__}: {e}",
            }]

        # Listar links pra Excel/PDF mais recentes
        links_excel = []
        for a in soup.find_all("a", href=True):
            href = a["href"]
            if any(ext in href.lower() for ext in [".xlsx", ".xls", ".pdf"]):
                texto = a.get_text(strip=True)
                links_excel.append({"href": href, "texto": texto})

        if not links_excel:
            return [{
                "data_referencia": date.today().isoformat(),
                "tipo": "indicacao",
                "commodity": "anec",
                "metrica": "links_relatorios",
                "valor": 0,
                "unidade": "count",
                "contexto": "Nenhum link de relatorio encontrado na pagina /estatisticas/. Estrutura pode ter mudado.",
            }]

        # Salvar apenas indicacoes dos relatorios disponiveis (pra acesso posterior)
        for link in links_excel[:10]:
            results.append({
                "data_referencia": date.today().isoformat(),
                "tipo": "metadata",
                "commodity": "anec",
                "metrica": "link_relatorio",
                "valor": None,
                "unidade": None,
                "contexto": f"{link['texto']} | {link['href']}",
                "raw": link,
            })

        # TODO: baixar Excel mais recente, parsear via openpyxl, extrair embarques.
        # Por enquanto registra apenas indicacao dos links — implementacao do parser
        # Excel quando precisar do dado especifico.

        return results
