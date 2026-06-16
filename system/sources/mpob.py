"""Coletor MPOB — Malaysian Palm Oil Board.

Release: mensal (~dia 10).
Fonte: https://bepi.mpob.gov.my/

Importante pelo lado da SOJA: palma e competidor direto do oleo de soja.
"""
import re
from datetime import date
from .base import BaseCollector


class MpobCollector(BaseCollector):
    source_name = "mpob"
    cadence = "monthly"
    description = "MPOB Malasia — producao/estoque/export palma (driver oleo de soja)"
    enabled = True

    def fetch(self):
        try:
            import requests
            from bs4 import BeautifulSoup
        except ImportError:
            raise RuntimeError("requests/bs4 nao instalado")

        results = []
        headers = {"User-Agent": "Mozilla/5.0 commodities-radar/1.0"}

        try:
            r = requests.get("https://bepi.mpob.gov.my/", headers=headers, timeout=30)
            r.raise_for_status()
            soup = BeautifulSoup(r.text, "lxml")
        except Exception as e:
            return [{
                "data_referencia": date.today().isoformat(),
                "tipo": "erro",
                "commodity": "palma_malasia",
                "metrica": "fetch_error",
                "valor": None,
                "contexto": f"{type(e).__name__}: {e}",
            }]

        # MPOB tem varias tabelas com dados mensais
        # Extrair texto da pagina principal e procurar numeros relevantes
        texto = soup.get_text(separator="\n", strip=True)

        # Procurar tabelas com dados mensais
        tables = soup.find_all("table")
        for i, t in enumerate(tables[:10]):
            cells = [c.get_text(strip=True) for c in t.find_all(["td", "th"])]
            if not cells:
                continue
            # Procurar palavras-chave
            t_text = " ".join(cells).lower()
            if any(k in t_text for k in ["production", "stocks", "export", "import", "palm"]):
                results.append({
                    "data_referencia": date.today().isoformat(),
                    "tipo": "metadata",
                    "commodity": "palma_malasia",
                    "metrica": f"tabela_{i}",
                    "valor": len(cells),
                    "unidade": "celulas",
                    "contexto": f"Tabela MPOB com {len(cells)} celulas: {' '.join(cells[:10])[:200]}",
                })

        # Tentar extrair valores numericos especificos
        # MPOB usa formato "X,XXX,XXX" para toneladas
        patterns = [
            (r"production[^\n]{0,40}?([\d,]+)\s*(?:t|tonn?es?)", "producao_mt"),
            (r"stocks?[^\n]{0,40}?([\d,]+)\s*(?:t|tonn?es?)", "estoque_mt"),
            (r"export[^\n]{0,40}?([\d,]+)\s*(?:t|tonn?es?)", "exportacao_mt"),
        ]

        for pat, label in patterns:
            for m in re.finditer(pat, texto, re.IGNORECASE):
                try:
                    valor = float(m.group(1).replace(",", ""))
                    ctx_start = max(0, m.start() - 50)
                    ctx = texto[ctx_start:m.end()].replace("\n", " ")[:200]
                    results.append({
                        "data_referencia": date.today().isoformat(),
                        "tipo": "supply_demand",
                        "commodity": "palma_malasia",
                        "metrica": label,
                        "valor": valor,
                        "unidade": "tonnes",
                        "contexto": ctx,
                    })
                except ValueError:
                    continue

        if not results:
            results.append({
                "data_referencia": date.today().isoformat(),
                "tipo": "metadata",
                "commodity": "palma_malasia",
                "metrica": "page_fetched",
                "valor": len(texto),
                "unidade": "chars",
                "contexto": "MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.",
            })

        # TODO: MPOB tem PDFs mensais com dados estruturados. Quando precisar
        # de granularidade real, baixar PDF do mes via /assets/files/STATISTICS/
        # e usar parse_pdf.py

        return results
