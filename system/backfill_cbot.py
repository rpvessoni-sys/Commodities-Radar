"""Backfill 5 anos de fechamentos diarios CBOT (front-month continuo) via Yahoo Finance.

Script standalone (nao e coletor registrado). Uso, a partir de system/:
    .venv/Scripts/python.exe backfill_cbot.py

Grava em dados_publicos com fonte='cme_cbot', tipo='preco', metrica='fechamento',
mesmo formato do coletor diario (sources/cme_cbot.py). INSERT OR IGNORE: dias ja
gravados pelo coletor diario (fonte canonica, 2026) NAO sao sobrescritos.

A serie do Yahoo (ZS=F etc) e front-month continua: tem saltos nas datas de
rolagem de contrato. Aceitavel para analise macro de 5 anos.
"""
import json
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import quote

# Permite import de db/config quando rodado de qualquer cwd
sys.path.insert(0, str(Path(__file__).resolve().parent))

# Fix SSL no Windows (AVG intercepta HTTPS): usa cert store nativo do OS
try:
    import truststore
    truststore.inject_into_ssl()
except ImportError:
    pass

import requests

import db

# ticker Yahoo -> (commodity, unidade) - mesmas unidades do coletor cme_cbot.py
TICKERS = {
    "ZM=F": ("farelo_cbot", "USD/short_ton"),
    "ZS=F": ("soja_cbot", "USD/bushel"),
    "ZL=F": ("oleo_cbot", "USD_cts/lb"),
    "HO=F": ("heating_oil_cbot", "USD/galão"),
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    "Accept": "application/json",
}


def fetch_5y(ticker: str) -> tuple[list, list]:
    """Busca 5 anos de barras diarias no Yahoo. Retorna (timestamps, closes)."""
    url = (
        f"https://query1.finance.yahoo.com/v8/finance/chart/{quote(ticker)}"
        f"?range=5y&interval=1d"
    )
    r = requests.get(url, headers=HEADERS, timeout=30)
    r.raise_for_status()
    data = r.json()
    chart = data["chart"]["result"][0]
    timestamps = chart.get("timestamp", []) or []
    closes = chart.get("indicators", {}).get("quote", [{}])[0].get("close", []) or []
    return timestamps, closes


def main():
    resumo = []
    with db.connect() as conn:
        for ticker, (commodity, unidade) in TICKERS.items():
            try:
                timestamps, closes = fetch_5y(ticker)
            except Exception as e:
                print(f"[ERRO] {ticker} ({commodity}): {type(e).__name__}: {e}")
                continue

            contexto = (
                f"backfill 5y — serie front-month continua (saltos de rolagem), "
                f"ticker={ticker}"
            )
            gravados = 0
            ignorados = 0
            nulls = 0
            datas = []
            for i, ts in enumerate(timestamps):
                # Feriados retornam close null no Yahoo: pula
                if i >= len(closes) or closes[i] is None:
                    nulls += 1
                    continue
                try:
                    data_ref = datetime.fromtimestamp(ts).date().isoformat()
                except (ValueError, OSError):
                    continue
                cursor = conn.execute(
                    """
                    INSERT OR IGNORE INTO dados_publicos
                    (fonte, data_referencia, tipo, commodity, metrica, valor, unidade, contexto, raw_json)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        "cme_cbot",
                        data_ref,
                        "preco",
                        commodity,
                        "fechamento",
                        float(closes[i]),
                        unidade,
                        contexto,
                        json.dumps({"ticker": ticker, "ts": ts}, ensure_ascii=False),
                    ),
                )
                if cursor.rowcount > 0:
                    gravados += 1
                else:
                    ignorados += 1
                datas.append(data_ref)

            dmin = min(datas) if datas else "-"
            dmax = max(datas) if datas else "-"
            resumo.append((commodity, ticker, gravados, ignorados, nulls, dmin, dmax))
            print(
                f"{commodity:18s} ({ticker}): gravados={gravados} "
                f"ignorados={ignorados} nulls_pulados={nulls} range={dmin}..{dmax}"
            )

    print("\n== RESUMO BACKFILL CBOT 5Y ==")
    for commodity, ticker, g, ig, nu, dmin, dmax in resumo:
        print(
            f"{commodity}: {g} gravados, {ig} ja existiam (ignorados), "
            f"{nu} closes null pulados, datas {dmin} a {dmax}"
        )


if __name__ == "__main__":
    main()
