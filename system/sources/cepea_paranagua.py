"""Coletor Indicador CEPEA/ESALQ Soja Paranagua via Noticias Agricolas.

Descoberto em 2026-05-25.

A pagina cepea.org.br tem Cloudflare que bloqueia mesmo com ScraperAPI premium,
mas o Noticias Agricolas espelha o numero oficial CEPEA em tabela estruturada
acessivel via scraper padrao (1 credit/dia, ~30/mes).

URL: https://www.noticiasagricolas.com.br/cotacoes/soja/soja-indicador-cepea-esalq-porto-paranagua

Estrategia:
- Buscar pagina HTML via ScraperAPI
- Parsear tabela "Fechamento: DD/MM/AAAA" com colunas (Data, Valor R$, Variacao %)
- Salvar em precos_fisicos como tipo_posicao='indicador' (preserva o input manual
  do usuario, que vem com tipo='compra' separado pela UNIQUE constraint)
- Captura os 3-5 fechamentos mais recentes pra backfill em caso de gap

O numero salvo aqui serve como PRECO DE SUPORTE/REFERENCIA, nao substitui o input
manual de compra do usuario. Ambos aparecem lado a lado no card HTML.
"""
import re
from datetime import datetime, date
from .base import BaseCollector
from .scraper import fetch_via_scraper, is_configured


URL = "https://www.noticiasagricolas.com.br/cotacoes/soja/soja-indicador-cepea-esalq-porto-paranagua"


class CepeaParanaguaCollector(BaseCollector):
    source_name = "cepea_paranagua"
    cadence = "daily"
    description = "Indicador CEPEA/ESALQ Soja Paranagua (via Noticias Agricolas) — preco suporte"
    enabled = True

    def fetch(self):
        if not is_configured():
            raise NotImplementedError(
                "cepea_paranagua: SCRAPER_API_KEY nao configurada"
            )
        try:
            from bs4 import BeautifulSoup
        except ImportError:
            raise RuntimeError("beautifulsoup4 nao instalado")

        try:
            r = fetch_via_scraper(URL, render=False, timeout=90)
            if r.status_code != 200:
                raise RuntimeError(f"HTTP {r.status_code}")
        except Exception as e:
            return [{
                "data_referencia": date.today().isoformat(),
                "tipo": "erro",
                "commodity": "soja_paranagua",
                "metrica": "fetch_error",
                "valor": None,
                "contexto": f"{type(e).__name__}: {e}",
            }]

        soup = BeautifulSoup(r.text, "html.parser")
        results = []

        # A pagina tem N tabelas, cada uma = 1 dia de fechamento
        # Estrutura tipica:
        #   <table>
        #     <tr><th>Data</th><th>Valor R$</th><th>Variação (%)</th></tr>
        #     <tr><td>22/05/2026</td><td>129,62</td><td>-0,02</td></tr>
        #   </table>
        tables = soup.find_all("table")
        dias_capturados = set()
        for t in tables:
            rows = t.find_all("tr")
            if len(rows) < 2:
                continue
            # Confere header
            header = [c.get_text(strip=True).lower() for c in rows[0].find_all(["th", "td"])]
            if not header or "data" not in header[0]:
                continue
            # Linha de valor
            cells = [c.get_text(strip=True) for c in rows[1].find_all(["td"])]
            if len(cells) < 2:
                continue

            data_str = cells[0]
            m = re.match(r"(\d{2})/(\d{2})/(\d{4})", data_str)
            if not m:
                continue
            data_iso = f"{m.group(3)}-{m.group(2)}-{m.group(1)}"
            if data_iso in dias_capturados:
                continue
            dias_capturados.add(data_iso)

            valor_brl = _parse_num_br(cells[1])
            variacao = _parse_num_br(cells[2]) if len(cells) > 2 else None
            if valor_brl is None:
                continue

            results.append({
                "data_referencia": data_iso,
                "tipo": "indicador",
                "commodity": "soja_paranagua",
                "metrica": "preco_suporte_brl_sc",
                "valor": valor_brl,
                "unidade": "BRL/saca",
                "contexto": f"CEPEA/ESALQ Soja Paranagua via NAG (var {variacao}%)" if variacao is not None else "CEPEA/ESALQ Soja Paranagua via NAG",
                "raw": {
                    "fonte": "Noticias Agricolas (espelho CEPEA/ESALQ oficial)",
                    "url": URL,
                    "variacao_pct": variacao,
                    "data_original": data_str,
                },
            })

            if len(results) >= 5:  # cap em 5 dias mais recentes
                break

        if not results:
            return [{
                "data_referencia": date.today().isoformat(),
                "tipo": "erro",
                "commodity": "soja_paranagua",
                "metrica": "parse_error",
                "valor": None,
                "contexto": "Nenhuma tabela com formato (Data,R$,Var%) encontrada — layout NAG pode ter mudado",
            }]

        # Espelha tambem em precos_fisicos (praca='paranagua_pr', tipo='indicador')
        # para aparecer no card do mercado fisico ao lado do input manual de compra.
        # Salva via uma segunda passagem em save_to_db sobreescrita abaixo.
        return results

    def save_to_db(self, records: list[dict]) -> int:
        """Override: alem de dados_publicos, popula precos_fisicos.tipo='indicador'."""
        saved = super().save_to_db(records)

        # Inserir tambem em precos_fisicos como tipo_posicao='indicador'
        # (separa do input manual de compra do usuario via UNIQUE constraint).
        import db
        inserted_fisicos = 0
        with db.connect() as conn:
            for r in records:
                if r.get("tipo") != "indicador" or r.get("valor") is None:
                    continue
                data_iso = r["data_referencia"]
                valor = r["valor"]
                conn.execute(
                    """
                    INSERT INTO precos_fisicos
                        (data, praca, produto, tipo_posicao, valor_brl_sc, observacao)
                    VALUES (?, 'paranagua_pr', 'soja', 'indicador', ?, ?)
                    ON CONFLICT(data, praca, produto, tipo_posicao) DO UPDATE SET
                        valor_brl_sc = excluded.valor_brl_sc,
                        observacao = excluded.observacao
                    """,
                    (data_iso, valor, "CEPEA/ESALQ via Noticias Agricolas (auto)"),
                )
                inserted_fisicos += 1
        return saved + inserted_fisicos


def _parse_num_br(s: str) -> float | None:
    """Parse num formato BR (1.234,56 ou -0,30 ou +0,02)."""
    if not s:
        return None
    s = s.strip().replace("+", "").replace("%", "").strip()
    if not s or s in ("-", "—", "N/A"):
        return None
    # BR: '129,62' ou '1.234,56'
    if "," in s and "." in s:
        s = s.replace(".", "").replace(",", ".")
    elif "," in s:
        s = s.replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None
