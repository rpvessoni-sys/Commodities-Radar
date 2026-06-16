"""Backfill historico do CFTC COT (Commitments of Traders) — 2021 a 2025.

Baixa os ZIPs anuais do relatorio disaggregated futures-only e grava as mesmas
metricas que o coletor semanal (sources/cftc_cot.py):
- open_interest, managed_money_long/short/net, producer_long/short, swap_long/short

Escopo: apenas complexo soja (soja_cbot, oleo_cbot, farelo_cbot), igual ao coletor.
Gravacao: INSERT OR IGNORE em dados_publicos com fonte='cftc_cot' — semanas de
2026 ja existem no DB e nao sao tocadas (anos diferentes, sem colisao).

Uso (a partir de system/):
    .venv\\Scripts\\python.exe backfill_cot.py
"""
from collections import defaultdict
import csv
import io
import json
import sys
import zipfile

# Fix SSL no Windows: AVG intercepta HTTPS, truststore usa o cert store do OS
try:
    import truststore
    truststore.inject_into_ssl()
except ImportError:
    pass

import requests

import db

FONTE = "cftc_cot"
ANOS = [2021, 2022, 2023, 2024, 2025]

# URL primaria + padrao alternativo do site da CFTC (mesmo arquivo, path antigo)
URL_PATTERNS = [
    "https://www.cftc.gov/files/dea/history/fut_disagg_txt_{ano}.zip",
    "https://www.cftc.gov/sites/default/files/files/dea/history/fut_disagg_txt_{ano}.zip",
]

# Mesmo mapeamento do coletor sources/cftc_cot.py (escopo 2026-05-26: so soja)
MARKETS = {
    "SOYBEANS - CHICAGO BOARD OF TRADE": "soja_cbot",
    "SOYBEAN OIL - CHICAGO BOARD OF TRADE": "oleo_cbot",
    "SOYBEAN MEAL - CHICAGO BOARD OF TRADE": "farelo_cbot",
}

# Mesmos campos do coletor. Swap short tem underscore duplo no header da CFTC;
# mantemos fallback com underscore simples por seguranca em arquivos antigos.
METRICAS_MAP = {
    "open_interest": ["Open_Interest_All"],
    "managed_money_long": ["M_Money_Positions_Long_All"],
    "managed_money_short": ["M_Money_Positions_Short_All"],
    "producer_long": ["Prod_Merc_Positions_Long_All"],
    "producer_short": ["Prod_Merc_Positions_Short_All"],
    "swap_long": ["Swap_Positions_Long_All"],
    "swap_short": ["Swap__Positions_Short_All", "Swap_Positions_Short_All"],
}


def baixar_zip_ano(ano):
    """Baixa o ZIP anual e devolve (texto_csv, url_usada, bytes). 404 tenta padrao alternativo."""
    erros = []
    for pattern in URL_PATTERNS:
        url = pattern.format(ano=ano)
        try:
            r = requests.get(url, timeout=120)
            r.raise_for_status()
            z = zipfile.ZipFile(io.BytesIO(r.content))
            nome_txt = z.namelist()[0]
            with z.open(nome_txt) as f:
                raw = f.read().decode("utf-8", errors="replace")
            return raw, url, len(r.content), nome_txt
        except Exception as e:
            erros.append(f"{url} -> {type(e).__name__}: {e}")
    raise RuntimeError(f"Nenhuma URL funcionou para {ano}: " + " | ".join(erros))


def parse_valor(raw_val):
    """Campos de posicao da CFTC sao counts inteiros, sem decimais."""
    raw_val = (raw_val or "").strip()
    if not raw_val:
        return None
    try:
        return float(raw_val.replace(",", ""))
    except ValueError:
        return None


def parse_ano(raw_csv, ano):
    """Parseia o TXT do ano e devolve lista de records no schema do coletor."""
    reader = csv.DictReader(io.StringIO(raw_csv))
    records = []
    semanas_vistas = defaultdict(set)

    for row in reader:
        market = (row.get("Market_and_Exchange_Names") or "").strip()
        if market not in MARKETS:
            continue

        commodity = MARKETS[market]
        data_ref = (row.get("Report_Date_as_YYYY-MM-DD") or "").strip()
        if not data_ref:
            # Fallback p/ arquivos antigos que so tem MM/DD/YYYY
            alt = (row.get("Report_Date_as_MM_DD_YYYY") or "").strip()
            if alt and "/" in alt:
                mm, dd, yyyy = alt.split("/")
                data_ref = f"{yyyy}-{mm.zfill(2)}-{dd.zfill(2)}"
        if not data_ref:
            continue

        valores = {}
        for nome, campos in METRICAS_MAP.items():
            valor = None
            for campo in campos:
                valor = parse_valor(row.get(campo))
                if valor is not None:
                    break
            if valor is not None:
                valores[nome] = valor
                records.append({
                    "data_referencia": data_ref,
                    "tipo": "posicionamento",
                    "commodity": commodity,
                    "metrica": nome,
                    "valor": valor,
                    "unidade": "contratos",
                    "contexto": market,
                })

        if "managed_money_long" in valores and "managed_money_short" in valores:
            net = valores["managed_money_long"] - valores["managed_money_short"]
            records.append({
                "data_referencia": data_ref,
                "tipo": "posicionamento",
                "commodity": commodity,
                "metrica": "managed_money_net",
                "valor": net,
                "unidade": "contratos",
                "contexto": f"{market} — long - short",
            })

        semanas_vistas[commodity].add(data_ref)

    return records, semanas_vistas


def gravar(records):
    """INSERT OR IGNORE em dados_publicos, mesmo formato do base.py save_to_db."""
    saved = 0
    with db.connect() as conn:
        for r in records:
            cursor = conn.execute(
                """
                INSERT OR IGNORE INTO dados_publicos
                (fonte, data_referencia, tipo, commodity, metrica, valor, unidade, contexto, raw_json)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    FONTE,
                    r.get("data_referencia"),
                    r.get("tipo", "indef"),
                    r.get("commodity"),
                    r.get("metrica", "valor"),
                    r.get("valor"),
                    r.get("unidade"),
                    r.get("contexto"),
                    None,
                ),
            )
            if cursor.rowcount > 0:
                saved += 1
    return saved


def main():
    total_fetched = 0
    total_saved = 0
    semanas_por_commodity = defaultdict(set)

    for ano in ANOS:
        try:
            raw, url, nbytes, nome_txt = baixar_zip_ano(ano)
        except RuntimeError as e:
            print(f"[{ano}] ERRO download: {e}")
            continue

        records, semanas = parse_ano(raw, ano)
        saved = gravar(records)
        total_fetched += len(records)
        total_saved += saved
        for c, datas in semanas.items():
            semanas_por_commodity[c].update(datas)

        semanas_str = ", ".join(f"{c}={len(d)}" for c, d in sorted(semanas.items()))
        print(f"[{ano}] {url} ({nbytes:,} bytes, {nome_txt}) -> "
              f"{len(records)} records, {saved} gravados | semanas: {semanas_str}")

    print()
    print(f"TOTAL: {total_fetched} records parseados, {total_saved} gravados (INSERT OR IGNORE)")

    # Sumario direto do DB pos-backfill
    with db.connect() as conn:
        print("\n-- DB pos-backfill (fonte=cftc_cot, semanas distintas por commodity):")
        for row in conn.execute(
            """
            SELECT commodity, COUNT(DISTINCT data_referencia) AS semanas,
                   MIN(data_referencia) AS de, MAX(data_referencia) AS ate, COUNT(*) AS linhas
            FROM dados_publicos
            WHERE fonte = ? AND commodity IN ('soja_cbot', 'oleo_cbot', 'farelo_cbot')
            GROUP BY commodity
            """,
            (FONTE,),
        ):
            print(f"   {row['commodity']}: {row['semanas']} semanas "
                  f"({row['de']} a {row['ate']}), {row['linhas']} linhas")

        print("\n-- Sanidade: managed_money_net farelo_cbot na ultima semana do backfill (2025):")
        for row in conn.execute(
            """
            SELECT data_referencia, valor FROM dados_publicos
            WHERE fonte = ? AND commodity = 'farelo_cbot' AND metrica = 'managed_money_net'
              AND data_referencia < '2026-01-01'
            ORDER BY data_referencia DESC LIMIT 1
            """,
            (FONTE,),
        ):
            print(f"   {row['data_referencia']}: {row['valor']:.0f} contratos")

        print("\n-- Sanidade: primeira semana de 2026 ja existente no DB (do coletor semanal):")
        for row in conn.execute(
            """
            SELECT data_referencia, valor FROM dados_publicos
            WHERE fonte = ? AND commodity = 'farelo_cbot' AND metrica = 'managed_money_net'
              AND data_referencia >= '2026-01-01'
            ORDER BY data_referencia ASC LIMIT 1
            """,
            (FONTE,),
        ):
            print(f"   {row['data_referencia']}: {row['valor']:.0f} contratos")


if __name__ == "__main__":
    sys.exit(main() or 0)
