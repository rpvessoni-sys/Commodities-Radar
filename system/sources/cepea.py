"""Coletor CEPEA/ESALQ — indicadores de precos fisicos BR.

Acessado via ScraperAPI (CEPEA tem anti-bot que bloqueia requests diretas).

Indicadores principais (URLs):
- Soja:         https://www.cepea.esalq.usp.br/br/indicador/soja.aspx
- Milho:        https://www.cepea.esalq.usp.br/br/indicador/milho.aspx
- Boi gordo:    https://www.cepea.esalq.usp.br/br/indicador/boi-gordo.aspx
- Cafe:         https://www.cepea.esalq.usp.br/br/indicador/cafe.aspx

Estrutura HTML:
- Tabela com classe ".imagenet-table" ou similar contendo serie diaria
- Colunas: Data | Valor R$ | Variacao % | Valor US$ | Variacao US$ %
"""
import re
from datetime import datetime, date
from .base import BaseCollector
from .scraper import fetch_via_scraper, is_configured


INDICADORES = {
    "soja": "https://www.cepea.esalq.usp.br/br/indicador/soja.aspx",
    "milho": "https://www.cepea.esalq.usp.br/br/indicador/milho.aspx",
    # Adicionar mais quando precisar — cada um custa 1 credit/request
}


class CepeaCollector(BaseCollector):
    source_name = "cepea"
    cadence = "daily"
    description = "CEPEA/ESALQ — indicador soja/milho (BLOQUEADO: Cloudflare timeout mesmo com scraper render+premium)"
    enabled = False  # ScraperAPI basic NAO consegue passar pelo Cloudflare do CEPEA em 300s

    def fetch(self):
        # TESTADO 2026-05-21:
        # - sem render: timeout em 120s
        # - render=True: timeout em 180s
        # - render=True + premium=True: timeout em 300s
        # ScraperAPI plano basico nao tem ultra_premium nem velocidade suficiente.
        #
        # Alternativas para preco fisico BR:
        # 1. Email subscription CEPEA (gratuita) — parsear via IMAP, mais estavel
        # 2. StoneX "Premios nos Portos" + tabelas semanais cobrem grande parte
        # 3. Mercados Agricolas, Noticias Agricolas (acessiveis sem bloqueio)
        # 4. Scraper plano superior (ultra_premium ~75 credits/req) ou Apify
        if not is_configured():
            raise NotImplementedError(
                "CEPEA via scraper: SCRAPER_API_KEY nao configurada no .env"
            )

        try:
            from bs4 import BeautifulSoup
        except ImportError:
            raise RuntimeError("beautifulsoup4 nao instalado")

        results = []

        for commodity, url in INDICADORES.items():
            try:
                # render=True necessario: CEPEA tem Cloudflare challenge que exige JS
                # Custo: 10 credits/request (vs 1 sem render) — cabe em free tier
                r = fetch_via_scraper(url, render=True, timeout=180)
                if r.status_code != 200:
                    raise RuntimeError(f"HTTP {r.status_code}: {r.text[:200]}")
                soup = BeautifulSoup(r.text, "lxml")
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

            # Tabela do indicador — geralmente tem class "imagenet-table"
            tables = soup.find_all("table")
            tabela_indicador = None
            for t in tables:
                # Procura tabela com "R$" no thead
                txt = t.get_text()
                if "R$" in txt and "US$" in txt:
                    tabela_indicador = t
                    break

            if not tabela_indicador:
                results.append({
                    "data_referencia": date.today().isoformat(),
                    "tipo": "erro",
                    "commodity": commodity,
                    "metrica": "parse_error",
                    "valor": None,
                    "contexto": "Tabela com R$/US$ nao encontrada no HTML",
                })
                continue

            rows = tabela_indicador.find_all("tr")
            registros_extraidos = 0

            for row in rows:
                cells = [c.get_text(strip=True) for c in row.find_all("td")]
                if len(cells) < 3:
                    continue

                # Espera-se algo como ['21/05/2026', '147.85', '+0.34', '28.92', '+0.12']
                data_str = cells[0]
                if not re.match(r"\d{2}/\d{2}/\d{4}", data_str):
                    continue
                try:
                    dia, mes, ano = data_str.split("/")
                    data_iso = f"{ano}-{mes}-{dia}"
                except ValueError:
                    continue

                # Valor BRL — coluna 1
                valor_brl = _parse_num(cells[1]) if len(cells) > 1 else None
                if valor_brl is not None:
                    results.append({
                        "data_referencia": data_iso,
                        "tipo": "preco",
                        "commodity": commodity,
                        "metrica": "valor_brl",
                        "valor": valor_brl,
                        "unidade": "BRL/saca" if commodity != "boi-gordo" else "BRL/@",
                        "contexto": f"CEPEA/ESALQ {commodity}",
                    })
                    registros_extraidos += 1

                # Valor USD — coluna 3 ou 4 (depende do indicador)
                for col_idx in (3, 2):
                    if col_idx < len(cells):
                        valor_usd = _parse_num(cells[col_idx])
                        if valor_usd is not None and valor_usd != valor_brl:
                            results.append({
                                "data_referencia": data_iso,
                                "tipo": "preco",
                                "commodity": commodity,
                                "metrica": "valor_usd",
                                "valor": valor_usd,
                                "unidade": "USD/saca" if commodity != "boi-gordo" else "USD/@",
                                "contexto": f"CEPEA/ESALQ {commodity}",
                            })
                            break

                if registros_extraidos >= 15:  # cap em ~15 dias mais recentes
                    break

        return results


def _parse_num(s: str) -> float | None:
    if not s:
        return None
    s = s.strip().replace("+", "").replace("%", "").strip()
    # BR format: 1.234,56 → 1234.56
    if "," in s and "." in s:
        s = s.replace(".", "").replace(",", ".")
    elif "," in s:
        s = s.replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None
