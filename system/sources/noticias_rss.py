"""Coletor generico de feeds RSS de noticias agro com filtro por commodity.

Descoberto em 2026-05-25 quando o usuario pediu noticias mais explicativas
e filtradas para soja/farelo/oleo de soja, alem do CEPEA.

Feeds configurados:
- G1 Agro (Globo, PT, 100 items)
- Canal Rural (PT, 10 items)
- FarmProgress (EN/US, 50 items)

Filtro: matching de keywords no TITULO (sinal mais forte que descricao).
Cada item vira 1 registro com tipo='noticia' e commodity em {soja, farelo, oleo_soja}.

Notas:
- Roda via ScraperAPI (1 credit por feed, 3 feeds = 3 credits/dia)
- HTML da description e limpo via BeautifulSoup
- Items duplicados (mesmo link) sao ignorados via INSERT OR IGNORE no DB
"""
import re
from datetime import date
from .base import BaseCollector
from .scraper import fetch_via_scraper, is_configured


FEEDS = [
    {
        "source": "g1_agro",
        "url": "https://g1.globo.com/rss/g1/economia/agronegocios/",
        "lang": "pt",
    },
    {
        "source": "canal_rural",
        "url": "https://www.canalrural.com.br/feed/",
        "lang": "pt",
    },
    {
        "source": "farm_progress",
        "url": "https://www.farmprogress.com/rss.xml",
        "lang": "en",
    },
]

# Keywords por commodity. Tem que aparecer no TITULO pra capturar.
# Ordem importa: farelo/oleo devem ser checados ANTES de soja
# (pra noticia sobre "farelo de soja" nao virar commodity=soja).
COMMODITY_KEYWORDS = [
    ("farelo", [
        r"\bfarelo\b",
        r"\bsoybean meal\b",
        r"\bsoymeal\b",
        r"\bsoy meal\b",
    ]),
    ("oleo_soja", [
        r"\b[óo]leo de soja\b",
        r"\bsoybean oil\b",
        r"\bsoyoil\b",
        r"\bsoy oil\b",
    ]),
    ("soja", [
        r"\bsoja\b",
        r"\bsoybean\b",
        r"\bsoybeans\b",
        r"\boleaginosa\b",
    ]),
]


class NoticiasRssCollector(BaseCollector):
    source_name = "noticias_rss"
    cadence = "daily"
    description = "Noticias agro filtradas (soja/farelo/oleo) — G1 Agro + Canal Rural + FarmProgress"
    enabled = True

    def fetch(self):
        if not is_configured():
            raise NotImplementedError(
                "noticias_rss: SCRAPER_API_KEY nao configurada"
            )
        try:
            from bs4 import BeautifulSoup
        except ImportError:
            raise RuntimeError("beautifulsoup4 nao instalado")

        results = []
        total_items = 0
        total_kept = 0

        for feed in FEEDS:
            try:
                r = fetch_via_scraper(feed["url"], render=False, timeout=90)
                if r.status_code != 200:
                    results.append({
                        "data_referencia": date.today().isoformat(),
                        "tipo": "erro",
                        "commodity": feed["source"],
                        "metrica": "fetch_error",
                        "valor": None,
                        "contexto": f"HTTP {r.status_code}",
                    })
                    continue
            except Exception as e:
                results.append({
                    "data_referencia": date.today().isoformat(),
                    "tipo": "erro",
                    "commodity": feed["source"],
                    "metrica": "fetch_error",
                    "valor": None,
                    "contexto": f"{type(e).__name__}: {e}",
                })
                continue

            soup = BeautifulSoup(r.text, "xml")
            items = soup.find_all("item")
            total_items += len(items)

            for item in items:
                parsed = self._parse_item(item, feed)
                if parsed:
                    results.append(parsed)
                    total_kept += 1

        # Metadata
        results.append({
            "data_referencia": date.today().isoformat(),
            "tipo": "metadata",
            "commodity": "noticias",
            "metrica": "items_fetched",
            "valor": float(total_items),
            "unidade": "items",
            "contexto": f"{total_items} items lidos, {total_kept} mantidos (soja/farelo/oleo)",
        })
        return results

    def _parse_item(self, item, feed: dict) -> dict | None:
        title = self._text(item, "title")
        link = self._text(item, "link")
        desc_raw = self._text(item, "description")
        pub = self._text(item, "pubDate")

        if not title:
            return None

        commodity = self._classifica(title)
        if not commodity:
            return None

        desc_clean = self._clean_html(desc_raw)[:500]
        data_iso = self._parse_pubdate(pub)

        return {
            "data_referencia": data_iso,
            "tipo": "noticia",
            "commodity": commodity,
            "metrica": "headline",
            "valor": None,
            "unidade": None,
            "contexto": f"{title} | {link}",
            "raw": {
                "title": title,
                "link": link,
                "description": desc_clean,
                "pubDate": pub,
                "source": feed["source"],
                "lang": feed["lang"],
            },
        }

    def _classifica(self, title: str) -> str | None:
        t = title.lower()
        for commodity, patterns in COMMODITY_KEYWORDS:
            for p in patterns:
                if re.search(p, t, re.IGNORECASE):
                    return commodity
        return None

    def _text(self, item, tag: str) -> str:
        el = item.find(tag)
        return el.get_text(strip=True) if el else ""

    def _clean_html(self, s: str) -> str:
        if not s:
            return ""
        # Remove tags HTML (img, figure, etc)
        s = re.sub(r"<[^>]+>", " ", s)
        # Decodifica entidades comuns
        replacements = {
            "&ndash;": "—", "&mdash;": "—", "&amp;": "&", "&nbsp;": " ",
            "&aacute;": "á", "&Aacute;": "Á", "&eacute;": "é", "&Eacute;": "É",
            "&iacute;": "í", "&oacute;": "ó", "&uacute;": "ú",
            "&atilde;": "ã", "&otilde;": "õ", "&ccedil;": "ç",
            "&acirc;": "â", "&ecirc;": "ê", "&ocirc;": "ô",
            "&agrave;": "à", "&quot;": '"', "&#39;": "'", "&apos;": "'",
            "&lt;": "<", "&gt;": ">",
        }
        for k, v in replacements.items():
            s = s.replace(k, v)
        # Colapsa whitespace
        s = re.sub(r"\s+", " ", s).strip()
        return s

    def _parse_pubdate(self, pub: str) -> str:
        if not pub:
            return date.today().isoformat()
        try:
            from email.utils import parsedate_to_datetime
            dt = parsedate_to_datetime(pub)
            return dt.date().isoformat()
        except Exception:
            return date.today().isoformat()
