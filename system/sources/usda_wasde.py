"""Coletor USDA WASDE — World Agricultural Supply and Demand Estimates.

Release: mensal 9-12.
Fonte estavel: Cornell University Library archive (usda.library.cornell.edu).

Padrao URL:
- https://usda.library.cornell.edu/concern/publications/3t945q76s (pagina indice)
- PDFs/XLS em /sites/default/release-files/{id}/wasde{MMYY}[v2].{pdf,xls}

Sheets de interesse no XLS:
- Page 15: U.S. Soybeans and Products Supply and Use (Domestic)
- Page 28: World Soybean Supply and Use ★★★ (Brasil, Argentina, EUA, China)
- Page 29: World Soybean Meal Supply and Use
- Page 30: World Soybean Oil Supply and Use

Cada sheet tem 3 anos-safra: ano anterior, ano corrente Est., proximo ano Proj.
Colunas: Beginning Stocks, Production, Imports, Domestic Crush, Domestic Total, Exports, Ending Stocks
Unidade: Million Metric Tons (mi t)
"""
import re
from datetime import date
from pathlib import Path

from .base import BaseCollector
import config


SOY_SHEETS = {
    "Page 28": ("soja", "World Soybean Supply and Use"),
    "Page 29": ("farelo", "World Soybean Meal Supply and Use"),
    "Page 30": ("oleo", "World Soybean Oil Supply and Use"),
}

PAISES_ALVO = [
    "World",
    "World Less China",
    "United States",
    "Total Foreign",
    "Major Exporters",
    "Argentina",
    "Brazil",
    "Paraguay",
    "Major Importers",
    "China",
    "European Union",
    "Southeast Asia",
    "Mexico",
]

COLUNAS_PADRAO = [
    "beginning_stocks",
    "production",
    "imports",
    "domestic_crush",
    "domestic_total",
    "exports",
    "ending_stocks",
]


class UsdaWasdeCollector(BaseCollector):
    source_name = "usda_wasde"
    cadence = "monthly"
    description = "USDA WASDE — Brasil/Argentina/EUA/China supply demand soja/farelo/oleo"
    enabled = True

    def fetch(self):
        try:
            import requests
            from bs4 import BeautifulSoup
            import xlrd
        except ImportError as e:
            raise RuntimeError(f"Dependencia faltando: {e}")

        headers = {"User-Agent": "Mozilla/5.0 Chrome/120.0"}

        # 1) Buscar pagina indice Cornell pra achar XLS mais recente
        try:
            r = requests.get(
                "https://usda.library.cornell.edu/concern/publications/3t945q76s",
                headers=headers, timeout=30,
            )
            r.raise_for_status()
            soup = BeautifulSoup(r.text, "lxml")
        except Exception as e:
            return self._erro(f"Cornell index: {type(e).__name__}: {e}")

        # Achar link XLS mais recente (formato Mes DD YYYY-xls)
        link_xls = None
        data_release = None
        for a in soup.find_all("a", href=True):
            txt = a.get_text(strip=True)
            href = a["href"]
            if href.endswith(".xls") and "wasde" in href.lower():
                m = re.match(r"(\w{3})\s+(\d{2})\s+(\d{4})-xls", txt)
                if m and link_xls is None:
                    link_xls = href
                    data_release = f"{m.group(3)}-{self._mes_num(m.group(1))}-{m.group(2)}"
                    break

        if not link_xls:
            return self._erro("Nenhum link XLS encontrado na pagina Cornell")

        # 2) Baixar XLS
        if link_xls.startswith("/"):
            link_xls = "https://usda.library.cornell.edu" + link_xls
        try:
            r = requests.get(link_xls, headers=headers, timeout=60)
            r.raise_for_status()
            xls_bytes = r.content
        except Exception as e:
            return self._erro(f"Download XLS: {type(e).__name__}: {e}")

        # Salvar copia local
        out_path = config.DATA_DIR / f"wasde_{data_release or 'latest'}.xls"
        out_path.write_bytes(xls_bytes)

        # 3) Parsear sheets de soja
        try:
            wb = xlrd.open_workbook(file_contents=xls_bytes)
        except Exception as e:
            return self._erro(f"Abrir XLS: {type(e).__name__}: {e}")

        results = []

        for sheet_name, (produto, titulo) in SOY_SHEETS.items():
            if sheet_name not in wb.sheet_names():
                continue
            sheet = wb.sheet_by_name(sheet_name)
            parsed = self._parse_sheet(sheet, produto, data_release or date.today().isoformat())
            results.extend(parsed)

        # Metadado da release
        results.append({
            "data_referencia": data_release or date.today().isoformat(),
            "tipo": "metadata",
            "commodity": "wasde",
            "metrica": "release",
            "valor": 1,
            "unidade": "bool",
            "contexto": f"WASDE release {data_release} | xls em {out_path.name}",
            "raw": {"url": link_xls, "local": str(out_path)},
        })

        return results

    def _parse_sheet(self, sheet, produto: str, data_release: str) -> list[dict]:
        """Le uma sheet WASDE e extrai linhas por pais x ano-safra.

        Heuristica:
        - Linhas com ano-safra (ex: '2024/25', '2026/27 Proj.') atualizam ano_safra_atual
        - Linhas com nome de pais (ex: 'Brazil', '    Argentina') atualizam pais_atual
        - Linhas com primeira cell vazia + 'May/Apr' em col 1 sao continuacao do ultimo pais
          (com revisao mensal — comum para projecao do ano corrente)
        - Valores numericos em col 2-8 sao as 7 metricas (Beginning Stocks, Production, etc)
        """
        results = []
        ano_safra_atual = None
        pais_atual = None
        forma_atual = None

        for row_idx in range(sheet.nrows):
            cells = []
            for c in range(sheet.ncols):
                val = sheet.cell_value(row_idx, c)
                if isinstance(val, str):
                    val = val.strip()
                cells.append(val)

            primeira_cell = str(cells[0]) if cells else ""

            # Detectar ano-safra (ex: "2024/25", "2025/26 Est.", "2026/27 Proj.")
            m_ano = re.match(r"(\d{4})/(\d{2,4})", primeira_cell)
            if m_ano:
                ano1 = m_ano.group(1)
                ano2 = m_ano.group(2)
                if len(ano2) == 2:
                    ano2 = ano1[:2] + ano2
                ano_safra_atual = f"{ano1}/{ano2}"
                pais_atual = None
                forma_atual = None
                continue

            # Detectar pais
            pais_match = None
            for p in PAISES_ALVO:
                if primeira_cell.lower().lstrip() == p.lower() or primeira_cell.lstrip().startswith(p):
                    pais_match = p
                    break

            if pais_match:
                pais_atual = pais_match
                # reset forma quando muda pais (cada pais pode ter Apr/May propria)
                forma_atual = None

            # Detectar revisao mensal (Apr/May) em col 1
            forma_cell = str(cells[1]).strip() if len(cells) > 1 else ""
            if forma_cell in ("Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar"):
                forma_atual = forma_cell

            if not pais_atual or not ano_safra_atual:
                continue

            # Valores em col 2-8 (apos col 0 nome pais, col 1 mes/vazio)
            valores = cells[2:2 + len(COLUNAS_PADRAO)]

            for idx, metrica in enumerate(COLUNAS_PADRAO):
                if idx >= len(valores):
                    break
                val = valores[idx]
                if isinstance(val, (int, float)) and val != 0:
                    pais_slug = pais_atual.lower().replace(" ", "_")
                    suffix = f"_{forma_atual.lower()}" if forma_atual else ""
                    commodity = f"{produto}_{pais_slug}"
                    metrica_full = f"{metrica}_{ano_safra_atual}{suffix}"
                    results.append({
                        "data_referencia": data_release,
                        "tipo": "supply_demand",
                        "commodity": commodity,
                        "metrica": metrica_full,
                        "valor": float(val),
                        "unidade": "mi_t",
                        "contexto": f"WASDE {produto} | {pais_atual} | {ano_safra_atual}{f' [{forma_atual}]' if forma_atual else ''}",
                    })

        return results

    def _mes_num(self, abrev: str) -> str:
        meses = {
            "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
            "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
            "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12",
        }
        return meses.get(abrev, "01")

    def _erro(self, msg: str) -> list[dict]:
        return [{
            "data_referencia": date.today().isoformat(),
            "tipo": "erro",
            "commodity": "wasde",
            "metrica": "fetch_error",
            "valor": None,
            "contexto": msg,
        }]
