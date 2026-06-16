"""Helper para fazer requests via API Scraper (atualmente ScraperAPI).

Uso em coletores que precisam contornar bloqueios anti-bot (Cloudflare, WAF, geo-restriction).

Configuracao no .env:
    SCRAPER_API_KEY=xxx
    SCRAPER_PROVIDER=scraperapi    # default

Custo: ScraperAPI cobra 1 credit por request sem JS, 10 com JS render.
Tier gratuito: 1000 credits/mes.

Uso em coletor:
    from .scraper import fetch_via_scraper
    r = fetch_via_scraper("https://site-bloqueado.com/dados", country="br")
    # r e um requests.Response — parse normal
"""
import os
import requests


def _get_provider():
    raw = os.getenv("SCRAPER_PROVIDER", "scraperapi")
    # tolera "scraperapi   # comentario" no .env
    return raw.split("#")[0].strip().lower()


def _get_key():
    return os.getenv("SCRAPER_API_KEY", "").strip()


def fetch_via_scraper(
    url: str,
    render: bool = False,
    country: str | None = None,
    premium: bool = False,
    timeout: int = 90,
) -> requests.Response:
    """Faz request via API Scraper.

    Args:
        url: URL alvo
        render: True para renderizar JavaScript (10x mais caro)
        country: ISO code do pais para proxy geo-localizado ("br", "us", "uk")
        premium: usar proxies premium (mais caros, mais resistentes a bloqueio)
        timeout: timeout em segundos

    Returns:
        requests.Response com o conteudo da URL alvo
    """
    api_key = _get_key()
    if not api_key:
        raise RuntimeError(
            "SCRAPER_API_KEY nao configurada em .env. "
            "Registrar em https://www.scraperapi.com/ e adicionar a chave."
        )

    provider = _get_provider()

    if provider == "scraperapi":
        params = {
            "api_key": api_key,
            "url": url,
            "render": "true" if render else "false",
        }
        if country:
            params["country_code"] = country
        if premium:
            params["premium"] = "true"
        scraper_endpoint = "http://api.scraperapi.com/"
        return requests.get(scraper_endpoint, params=params, timeout=timeout)

    elif provider == "scrapingbee":
        params = {
            "api_key": api_key,
            "url": url,
            "render_js": "true" if render else "false",
        }
        if country:
            params["country_code"] = country
        return requests.get(
            "https://app.scrapingbee.com/api/v1/", params=params, timeout=timeout
        )

    elif provider == "zenrows":
        params = {
            "apikey": api_key,
            "url": url,
            "js_render": "true" if render else "false",
        }
        if country:
            params["proxy_country"] = country
        if premium:
            params["premium_proxy"] = "true"
        return requests.get("https://api.zenrows.com/v1/", params=params, timeout=timeout)

    else:
        raise NotImplementedError(
            f"Provider '{provider}' nao suportado. "
            f"Suportados: scraperapi, scrapingbee, zenrows. "
            f"Editar system/sources/scraper.py para adicionar outros."
        )


def is_configured() -> bool:
    """True se ha credencial valida configurada."""
    return bool(_get_key())


def status() -> dict:
    """Retorna dict com info do scraper (sem expor a key)."""
    key = _get_key()
    return {
        "provider": _get_provider(),
        "configured": bool(key),
        "key_preview": (key[:4] + "***" + key[-4:]) if len(key) > 8 else "***",
    }
