"""Coletor de cotacoes fisicas publicas de farelo, oleo e soja via Noticias Agricolas.

Criado em 2026-06-11 (melhoria continua: comparacao publica vs input manual).

4 paginas (1 credit ScraperAPI cada, ~120/mes):
1. Farelo fisico por praca (R$/t): Media RS (Clicmercado), MT (IMEA), Rondonopolis (BCSP)
   https://www.noticiasagricolas.com.br/cotacoes/soja/farelo-de-soja
2. Premio farelo Paranagua (US$/short ton sobre CBOT SM)
   https://www.noticiasagricolas.com.br/cotacoes/soja/soja-premio-farelo-de-soja-paranagua-pr
3. Premio oleo Paranagua (cts/lb sobre CBOT BO)
   https://www.noticiasagricolas.com.br/cotacoes/soja/soja-premio-oleo-de-soja-paranagua-pr
4. Indicador CEPEA/ESALQ soja PARANA interior (R$/sc 60kg) — praca do usuario (Araucaria/PR)
   https://www.noticiasagricolas.com.br/cotacoes/soja/indicador-cepea-esalq-soja-parana

Os premios Paranagua sao o substituto PUBLICO do sinal que se perdeu com a
saida dos PDFs StoneX (2026-06-05): FOB implicito = (CBOT + premio) x fator x USD/BRL.

Estrutura das paginas (sondada 2026-06-11): cada <table> = 1 dia, precedida
do texto "Fechamento: DD/MM/AAAA"; container class 'table-content'.
"""
import re
from datetime import date
from .base import BaseCollector
from .scraper import fetch_via_scraper, is_configured


URL_FARELO_PRACAS = "https://www.noticiasagricolas.com.br/cotacoes/soja/farelo-de-soja"
URL_PREMIO_FARELO = "https://www.noticiasagricolas.com.br/cotacoes/soja/soja-premio-farelo-de-soja-paranagua-pr"
URL_PREMIO_OLEO = "https://www.noticiasagricolas.com.br/cotacoes/soja/soja-premio-oleo-de-soja-paranagua-pr"
URL_SOJA_PARANA = "https://www.noticiasagricolas.com.br/cotacoes/soja/indicador-cepea-esalq-soja-parana"

# label da praca na pagina → slug estavel no DB
_PRACA_PATTERNS = [
    (re.compile(r"rio grande do sul", re.I), "rs_media"),
    (re.compile(r"rondon[oó]polis", re.I), "rondonopolis_mt"),
    (re.compile(r"mato grosso", re.I), "mt_imea"),
]

MAX_FECHAMENTOS = 3  # backfill leve por pagina


class NagFisicoCollector(BaseCollector):
    source_name = "nag_fisico"
    cadence = "daily"
    description = "Farelo fisico por praca + premios farelo/oleo Paranagua (Noticias Agricolas)"
    enabled = True

    def fetch(self):
        if not is_configured():
            raise NotImplementedError("nag_fisico: SCRAPER_API_KEY nao configurada")
        try:
            from bs4 import BeautifulSoup  # noqa: F401
        except ImportError:
            raise RuntimeError("beautifulsoup4 nao instalado")

        results = []
        results += self._fetch_farelo_pracas()
        results += self._fetch_premio(
            URL_PREMIO_FARELO, commodity="farelo_paranagua",
            metrica="premio_usd_sht", unidade="USD/short_ton",
            label="Premio farelo Paranagua (NAG)",
        )
        results += self._fetch_premio(
            URL_PREMIO_OLEO, commodity="oleo_paranagua",
            metrica="premio_cts_lb", unidade="cts/lb",
            label="Premio oleo Paranagua (NAG)",
        )
        results += self._fetch_soja_parana()
        if not results:
            return [{
                "data_referencia": date.today().isoformat(),
                "tipo": "erro",
                "commodity": "nag_fisico",
                "metrica": "parse_error",
                "valor": None,
                "contexto": "Nenhuma tabela parseada nas 3 paginas — layout NAG pode ter mudado",
            }]
        return results

    # ------------------------------------------------------------------

    def _tabelas_com_data(self, url: str):
        """Busca a pagina e delega o parse pra iter_tabelas (testavel offline)."""
        r = fetch_via_scraper(url, render=False, timeout=90)
        if r.status_code != 200:
            raise RuntimeError(f"HTTP {r.status_code} em {url}")
        yield from iter_tabelas(r.text)

    def _fetch_farelo_pracas(self) -> list[dict]:
        out = []
        try:
            for data_iso, tb in self._tabelas_com_data(URL_FARELO_PRACAS):
                for row in tb.find_all("tr")[1:]:
                    cells = [c.get_text(strip=True) for c in row.find_all("td")]
                    if len(cells) < 2:
                        continue
                    praca_label = cells[0]
                    valor = _parse_num_br(cells[1])
                    variacao = _parse_num_br(cells[2]) if len(cells) > 2 else None
                    if valor is None:
                        continue
                    slug = _praca_slug(praca_label)
                    out.append({
                        "data_referencia": data_iso,
                        "tipo": "preco",
                        "commodity": "farelo_fisico_br",
                        "metrica": f"preco_brl_ton_{slug}",
                        "valor": valor,
                        "unidade": "BRL/ton",
                        "contexto": f"{praca_label} via NAG"
                                    + (f" (var {variacao}%)" if variacao is not None else ""),
                        "raw": {"praca": praca_label, "url": URL_FARELO_PRACAS,
                                "variacao_pct": variacao},
                    })
        except Exception as e:
            out.append(_erro("farelo_fisico_br", e))
        return out

    def _fetch_premio(self, url: str, commodity: str, metrica: str,
                      unidade: str, label: str) -> list[dict]:
        """Premio Paranagua: 1 linha por tabela (mes front), valor sobre CBOT."""
        out = []
        try:
            for data_iso, tb in self._tabelas_com_data(url):
                rows = tb.find_all("tr")
                if len(rows) < 2:
                    continue
                cells = [c.get_text(strip=True) for c in rows[1].find_all("td")]
                if len(cells) < 2:
                    continue
                mes_label = cells[0]
                valor = _parse_num_br(cells[1])
                if valor is None:
                    continue
                out.append({
                    "data_referencia": data_iso,
                    "tipo": "premio",
                    "commodity": commodity,
                    "metrica": metrica,
                    "valor": valor,
                    "unidade": unidade,
                    "contexto": f"{label} — mes {mes_label}",
                    "raw": {"mes": mes_label, "url": url},
                })
        except Exception as e:
            out.append(_erro(commodity, e))
        return out


    def _fetch_soja_parana(self) -> list[dict]:
        """Indicador CEPEA/ESALQ soja Parana INTERIOR (R$/sc) — praca do usuario.

        Complementa o cepea_paranagua (porto): o spread porto-interior PR e
        informacao de logistica/oportunidade pra quem compra em Araucaria.
        Tabela: (Data, Valor R$/sc 60kg, Variacao %) — valor em cells[1].
        """
        out = []
        try:
            for data_iso, tb in self._tabelas_com_data(URL_SOJA_PARANA):
                rows = tb.find_all("tr")
                if len(rows) < 2:
                    continue
                cells = [c.get_text(strip=True) for c in rows[1].find_all("td")]
                if len(cells) < 2:
                    continue
                valor = _parse_num_br(cells[1])
                variacao = _parse_num_br(cells[2]) if len(cells) > 2 else None
                if valor is None:
                    continue
                out.append({
                    "data_referencia": data_iso,
                    "tipo": "indicador",
                    "commodity": "soja_parana_interior",
                    "metrica": "preco_brl_sc",
                    "valor": valor,
                    "unidade": "BRL/saca",
                    "contexto": "CEPEA/ESALQ Soja Parana interior via NAG"
                                + (f" (var {variacao}%)" if variacao is not None else ""),
                    "raw": {"url": URL_SOJA_PARANA, "variacao_pct": variacao},
                })
        except Exception as e:
            out.append(_erro("soja_parana_interior", e))
        return out


def iter_tabelas(html: str, max_fechamentos: int = MAX_FECHAMENTOS):
    """Itera (data_iso, table) das tabelas precedidas de 'Fechamento: DD/MM/AAAA'.

    Funcao pura (recebe HTML, sem rede) — testavel offline com fixture.
    Paginas NAG duplicam a tabela do dia (desktop/mobile): dedup por data.
    """
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    vistos = set()
    for tb in soup.find_all("table"):
        prev = tb.find_previous(string=re.compile(r"Fechamento:\s*\d{2}/\d{2}/\d{4}"))
        if not prev:
            continue
        m = re.search(r"(\d{2})/(\d{2})/(\d{4})", prev)
        if not m:
            continue
        data_iso = f"{m.group(3)}-{m.group(2)}-{m.group(1)}"
        if data_iso in vistos:
            continue
        vistos.add(data_iso)
        yield data_iso, tb
        if len(vistos) >= max_fechamentos:
            return


def _praca_slug(label: str) -> str:
    for pat, slug in _PRACA_PATTERNS:
        if pat.search(label):
            return slug
    # fallback: slug generico estavel
    s = re.sub(r"[^a-z0-9]+", "_", label.lower()).strip("_")
    return s[:30] or "praca"


def _erro(commodity: str, e: Exception) -> dict:
    return {
        "data_referencia": date.today().isoformat(),
        "tipo": "erro",
        "commodity": commodity,
        "metrica": "fetch_error",
        "valor": None,
        "contexto": f"{type(e).__name__}: {e}",
    }


def _parse_num_br(s: str) -> float | None:
    """Parse num formato BR (1.234,56 ou -0,30 ou +0,02)."""
    if not s:
        return None
    s = s.strip().replace("+", "").replace("%", "").strip()
    if not s or s in ("-", "—", "N/A"):
        return None
    if "," in s and "." in s:
        s = s.replace(".", "").replace(",", ".")
    elif "," in s:
        s = s.replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None
