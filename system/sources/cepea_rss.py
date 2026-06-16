"""Coletor CEPEA via RSS feed publico.

🎯 ESSE E O CAMINHO BOM: descoberto em 2026-05-25.

URL: https://www.cepea.org.br/rss.php
Conteudo: diarias de mercado, releases, opiniao (BR + EN)
Cobertura: soja, milho, boi, algodao, etanol, acucar, cafe, feijao, trigo,
           mandioca, ovos, frango, suinos, citros, hortifruti

O feed XML e bloqueado por Cloudflare em requests diretas (403/timeout),
mas passa via ScraperAPI sem render (1 credit/req). Roda 1x/dia → 30/mes.

Estrategia:
- Buscar feed
- Parse XML
- Filtrar commodities relevantes ao nosso escopo
- Salvar titulo, link, descricao, data de publicacao
- Extrair valor numerico quando aparecer no description (R$, US$, %)

Comparado ao plano original via email IMAP: dispensa subscription,
dispensa App Password Gmail, dispensa filtros Gmail. So precisa do scraper.
"""
import re
from datetime import datetime, date
from .base import BaseCollector
from .scraper import fetch_via_scraper, is_configured


RSS_URL = "https://www.cepea.org.br/rss.php"

# Mapeia palavras-chave do title CEPEA para nosso slug interno.
# ESCOPO (2026-05-26): apenas complexo soja. Notícias de outros produtos
# são DESCARTADAS (não viram registros no DB).
COMMODITY_MAP = {
    "SOJA": "soja",
    "FARELO": "farelo",
    "OLEO DE SOJA": "oleo_soja",
    "ÓLEO DE SOJA": "oleo_soja",
}


class CepeaRssCollector(BaseCollector):
    source_name = "cepea_rss"
    cadence = "daily"
    description = "CEPEA via RSS feed publico — diarias de mercado por commodity"
    enabled = True

    def fetch(self):
        if not is_configured():
            raise NotImplementedError(
                "CEPEA RSS via scraper: SCRAPER_API_KEY nao configurada"
            )

        try:
            from bs4 import BeautifulSoup
        except ImportError:
            raise RuntimeError("beautifulsoup4 nao instalado")

        try:
            r = fetch_via_scraper(RSS_URL, render=False, timeout=120)
            if r.status_code != 200:
                raise RuntimeError(f"HTTP {r.status_code}")
        except Exception as e:
            return [{
                "data_referencia": date.today().isoformat(),
                "tipo": "erro",
                "commodity": "cepea",
                "metrica": "fetch_error",
                "valor": None,
                "contexto": f"{type(e).__name__}: {e}",
            }]

        soup = BeautifulSoup(r.text, "xml")
        items = soup.find_all("item")
        if not items:
            return [{
                "data_referencia": date.today().isoformat(),
                "tipo": "erro",
                "commodity": "cepea",
                "metrica": "parse_error",
                "valor": None,
                "contexto": "RSS sem <item> — formato pode ter mudado",
            }]

        results = []
        for item in items:
            parsed = self._parse_item(item)
            if parsed:
                results.extend(parsed)

        # Registro de metadata
        results.append({
            "data_referencia": date.today().isoformat(),
            "tipo": "metadata",
            "commodity": "cepea",
            "metrica": "release_items",
            "valor": float(len(items)),
            "unidade": "items",
            "contexto": f"CEPEA RSS feed — {len(items)} itens parseados",
        })

        return results

    def _parse_item(self, item) -> list[dict]:
        """Le 1 <item> do RSS e retorna lista de registros (1 por commodity detectada)."""
        title = self._text(item, "title")
        link = self._text(item, "link")
        desc = self._text(item, "description")
        pub = self._text(item, "pubDate")

        # Detectar commodity pelo title (padrao: "COMMODITY/CEPEA: texto")
        commodity_slug = self._identifica_commodity(title)
        if not commodity_slug:
            return []  # ignora item nao mapeado

        # Extrair data de publicacao em ISO
        data_iso = self._parse_pubdate(pub)

        # Extrair primeira frase do description (resumo)
        desc_clean = self._limpa_html(desc)
        resumo_curto = desc_clean[:300]

        # Tentar extrair valor numerico (R$, US$, %)
        valores = self._extrai_valores(desc_clean)

        registros = []

        # Registro principal: a noticia em si
        registros.append({
            "data_referencia": data_iso,
            "tipo": "noticia",
            "commodity": commodity_slug,
            "metrica": "headline",
            "valor": None,
            "unidade": None,
            "contexto": f"{title} | {link}",
            "raw": {
                "title": title,
                "link": link,
                "description": resumo_curto,
                "pubDate": pub,
            },
        })

        # Registros adicionais: valores numericos extraidos
        for v in valores[:5]:  # cap em 5 valores por noticia pra evitar ruido
            registros.append({
                "data_referencia": data_iso,
                "tipo": "preco_referencia",
                "commodity": commodity_slug,
                "metrica": v["metrica"],
                "valor": v["valor"],
                "unidade": v["unidade"],
                "contexto": f"CEPEA RSS: {v['contexto'][:150]}",
            })

        return registros

    def _identifica_commodity(self, title: str) -> str | None:
        if not title:
            return None
        title_upper = title.upper()
        # Procurar antes do "/" ou ":" (padrao CEPEA)
        prefix = title_upper.split("/", 1)[0].strip()
        # Mapear prefixo direto
        if prefix in COMMODITY_MAP:
            return COMMODITY_MAP[prefix]
        # Fallback: procurar qualquer keyword no title
        for kw, slug in COMMODITY_MAP.items():
            if kw in title_upper:
                return slug
        return None

    def _parse_pubdate(self, pub: str) -> str:
        """Converte 'Fri, 22 May 2026 16:53:16 -0300' para ISO YYYY-MM-DD."""
        if not pub:
            return date.today().isoformat()
        try:
            # Formato RFC 2822
            from email.utils import parsedate_to_datetime
            dt = parsedate_to_datetime(pub)
            return dt.date().isoformat()
        except Exception:
            # Fallback: regex simples
            m = re.search(r"(\d{1,2})\s+(\w{3})\s+(\d{4})", pub)
            if m:
                meses = {"Jan":"01","Feb":"02","Mar":"03","Apr":"04","May":"05","Jun":"06",
                         "Jul":"07","Aug":"08","Sep":"09","Oct":"10","Nov":"11","Dec":"12"}
                dia = m.group(1).zfill(2)
                mes = meses.get(m.group(2), "01")
                ano = m.group(3)
                return f"{ano}-{mes}-{dia}"
            return date.today().isoformat()

    def _text(self, item, tag: str) -> str:
        el = item.find(tag)
        return el.get_text(strip=True) if el else ""

    def _limpa_html(self, s: str) -> str:
        """Decodifica entidades HTML basicas."""
        if not s:
            return ""
        replacements = {
            "&ndash;": "—",
            "&amp;": "&",
            "&nbsp;": " ",
            "&aacute;": "á", "&Aacute;": "Á",
            "&eacute;": "é", "&Eacute;": "É",
            "&iacute;": "í", "&Iacute;": "Í",
            "&oacute;": "ó", "&Oacute;": "Ó",
            "&uacute;": "ú", "&Uacute;": "Ú",
            "&atilde;": "ã", "&Atilde;": "Ã",
            "&otilde;": "õ", "&Otilde;": "Õ",
            "&ccedil;": "ç", "&Ccedil;": "Ç",
            "&acirc;": "â", "&ecirc;": "ê", "&ocirc;": "ô",
            "&agrave;": "à", "&ograve;": "ò",
            "&quot;": '"', "&#39;": "'",
        }
        for k, v in replacements.items():
            s = s.replace(k, v)
        return s

    def _extrai_valores(self, texto: str) -> list[dict]:
        """Extrai valores numericos do texto da news."""
        patterns = [
            (r"R\$\s*([\d.,]+)\s*/\s*(saca|kg|t|tonelada|caixa|litro|L|m³|@|cab|caca)",
             "preco_brl", "BRL"),
            (r"US\$\s*([\d.,]+)\s*/\s*(saca|kg|t|tonelada|bushel|bu|lb)",
             "preco_usd", "USD"),
            (r"([+-]?\d{1,3}[,.]?\d{0,2})\s*%",
             "variacao_pct", "%"),
            (r"(\d{1,3}(?:[.,]\d{3})*(?:[.,]\d+)?)\s*milh(?:[oõ]es)?\s*(?:de\s+)?(?:t|tonelada)",
             "volume_mi_t", "mi_t"),
            (r"(\d{1,3}(?:[.,]\d{3})*)\s*mil\s*(?:t|tonelada)",
             "volume_mil_t", "mil_t"),
        ]

        found = []
        for pattern, metrica, unidade in patterns:
            for m in re.finditer(pattern, texto, re.IGNORECASE):
                try:
                    raw = m.group(1).replace(".", "").replace(",", ".") if "," in m.group(1) else m.group(1).replace(",", "")
                    valor = float(raw)
                except ValueError:
                    continue
                ctx_start = max(0, m.start() - 60)
                ctx = texto[ctx_start:m.end() + 30].replace("\n", " ").strip()
                found.append({
                    "metrica": metrica,
                    "valor": valor,
                    "unidade": unidade,
                    "contexto": ctx,
                })
        return found
