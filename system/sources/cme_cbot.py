"""Coletor CME Group / CBOT — futuros do COMPLEXO SOJA + Heating Oil + CURVA FORWARD.

ESCOPO (decidido 2026-05-26): apenas produtos do complexo soja.
Milho (ZC=F) e Trigo (ZW=F) foram REMOVIDOS.

Via API publica Yahoo Finance (sem deps de curl_cffi, evita SSL issues no Windows).

FRONT-MONTH (usado pra paridade, indicadores, alertas):
- ZS=F  Soybean Futures (5,000 bushels)         cents/bushel
- ZM=F  Soybean Meal Futures (100 short tons)   USD/short_ton
- ZL=F  Soybean Oil Futures (60,000 lbs)        cents/lb
- HO=F  Heating Oil (NY Harbor ULSD)            USD/galão

CURVA FORWARD (próximos N vencimentos por commodity, salvos como
metrica='fechamento_<MES><ANO>', ex 'fechamento_N26'):
- Ticker Yahoo: ZS<MES><YR>.CBT, ZM<MES><YR>.CBT, ZL<MES><YR>.CBT
- Códigos mês CME: F=Jan G=Fev H=Mar J=Abr K=Mai M=Jun N=Jul Q=Ago U=Set V=Out X=Nov Z=Dez
- Soja líquidos: F H K N Q U X (e F do ano seguinte)
- Farelo líquidos: F H K N Q U V Z
- Óleo líquidos: F H K N Q U V Z
"""
from datetime import date, datetime, timedelta
from urllib.parse import quote

from .base import BaseCollector

TICKERS = {
    "ZS=F": ("soja_cbot", "USD/bushel"),
    "ZM=F": ("farelo_cbot", "USD/short_ton"),
    "ZL=F": ("oleo_cbot", "USD_cts/lb"),
    "HO=F": ("heating_oil_cbot", "USD/galão"),
}

# Códigos de mês CME
MES_CME = {1:"F", 2:"G", 3:"H", 4:"J", 5:"K", 6:"M", 7:"N", 8:"Q", 9:"U", 10:"V", 11:"X", 12:"Z"}

# Meses líquidos por produto (índices 1-12)
MESES_LIQUIDOS = {
    "soja_cbot":   [1, 3, 5, 7, 8, 9, 11],          # F H K N Q U X
    "farelo_cbot": [1, 3, 5, 7, 8, 9, 10, 12],      # F H K N Q U V Z
    "oleo_cbot":   [1, 3, 5, 7, 8, 9, 10, 12],      # F H K N Q U V Z
}

# Mapeia commodity → prefixo do ticker
PREFIXO_TICKER = {
    "soja_cbot": "ZS",
    "farelo_cbot": "ZM",
    "oleo_cbot": "ZL",
}


def _proximos_vencimentos(commodity: str, n: int = 6, ref: date | None = None) -> list[tuple[str, str, str]]:
    """Retorna lista de (ticker, codigo_contrato, label) para próximos N vencimentos.

    Ex: soja em mai/2026 -> [(ZSN26.CBT, N26, jul/26), (ZSQ26.CBT, Q26, ago/26), ...]
    """
    ref = ref or date.today()
    meses_liq = MESES_LIQUIDOS.get(commodity, [])
    prefixo = PREFIXO_TICKER.get(commodity, "")
    if not meses_liq or not prefixo:
        return []
    out = []
    ano, mes_atual = ref.year, ref.month
    # Itera meses futuros até pegar N vencimentos líquidos
    for offset in range(0, 24):
        m = ((mes_atual - 1 + offset) % 12) + 1
        y = ano + ((mes_atual - 1 + offset) // 12)
        if m not in meses_liq:
            continue
        codigo_mes = MES_CME[m]
        yr2 = y % 100
        codigo = f"{codigo_mes}{yr2:02d}"            # ex: N26
        ticker = f"{prefixo}{codigo}.CBT"            # ex: ZSN26.CBT
        nome_mes = ["jan","fev","mar","abr","mai","jun","jul","ago","set","out","nov","dez"][m-1]
        label = f"{nome_mes}/{yr2:02d}"
        out.append((ticker, codigo, label))
        if len(out) >= n:
            break
    return out


class CMECollector(BaseCollector):
    source_name = "cme_cbot"
    cadence = "daily"
    description = "Futuros CBOT (soja/farelo/óleo + HO) front-month + curva forward via Yahoo"
    enabled = True

    def fetch(self):
        try:
            import requests
        except ImportError:
            raise RuntimeError("requests nao instalado")

        results = []
        end_ts = int(datetime.now().timestamp())
        start_ts = int((datetime.now() - timedelta(days=15)).timestamp())

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/120.0 Safari/537.36",
            "Accept": "application/json",
        }

        for ticker, (commodity, unidade) in TICKERS.items():
            url = (
                f"https://query1.finance.yahoo.com/v8/finance/chart/{quote(ticker)}"
                f"?period1={start_ts}&period2={end_ts}&interval=1d"
            )
            try:
                r = requests.get(url, headers=headers, timeout=15)
                r.raise_for_status()
                data = r.json()
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

            try:
                chart = data["chart"]["result"][0]
                timestamps = chart.get("timestamp", [])
                indicators = chart.get("indicators", {}).get("quote", [{}])[0]
                opens = indicators.get("open", [])
                highs = indicators.get("high", [])
                lows = indicators.get("low", [])
                closes = indicators.get("close", [])
                volumes = indicators.get("volume", [])
            except (KeyError, IndexError, TypeError) as e:
                results.append({
                    "data_referencia": date.today().isoformat(),
                    "tipo": "erro",
                    "commodity": commodity,
                    "metrica": "parse_error",
                    "valor": None,
                    "contexto": f"{type(e).__name__}: {e}",
                })
                continue

            for i, ts in enumerate(timestamps):
                try:
                    data_ref = datetime.fromtimestamp(ts).date().isoformat()
                except (ValueError, OSError):
                    continue
                metricas = [
                    ("abertura", opens, unidade),
                    ("maxima", highs, unidade),
                    ("minima", lows, unidade),
                    ("fechamento", closes, unidade),
                    ("volume", volumes, "contratos"),
                ]
                for metrica, lista, un in metricas:
                    if i >= len(lista) or lista[i] is None:
                        continue
                    results.append({
                        "data_referencia": data_ref,
                        "tipo": "preco",
                        "commodity": commodity,
                        "metrica": metrica,
                        "valor": float(lista[i]),
                        "unidade": un,
                        "contexto": f"ticker={ticker}",
                        "raw": {"ticker": ticker, "ts": ts},
                    })

        # ====== CURVA FORWARD (próximos 6 vencimentos por commodity) ======
        # Salvo como metrica='fechamento_<CODIGO>' (ex: 'fechamento_N26')
        # Permite consultar curva inteira sem mudar schema.
        for commodity in ["soja_cbot", "farelo_cbot", "oleo_cbot"]:
            unidade = next(
                (u for tk, (c, u) in TICKERS.items() if c == commodity),
                "?"
            )
            for ticker_fwd, codigo, label in _proximos_vencimentos(commodity, n=6):
                url = (
                    f"https://query1.finance.yahoo.com/v8/finance/chart/{quote(ticker_fwd)}"
                    f"?period1={start_ts}&period2={end_ts}&interval=1d"
                )
                try:
                    r = requests.get(url, headers=headers, timeout=15)
                    r.raise_for_status()
                    data = r.json()
                except Exception as e:
                    # Vencimento pode não ter mercado ativo no Yahoo, ignora silencioso
                    continue

                try:
                    chart = data["chart"]["result"][0]
                    timestamps = chart.get("timestamp", []) or []
                    closes = chart.get("indicators", {}).get("quote", [{}])[0].get("close", []) or []
                except (KeyError, IndexError, TypeError):
                    continue

                # Pega só o último fechamento (curva é snapshot, não histórico)
                last_close = None
                last_ts = None
                for i in range(len(timestamps) - 1, -1, -1):
                    if i < len(closes) and closes[i] is not None:
                        last_close = closes[i]
                        last_ts = timestamps[i]
                        break
                if last_close is None:
                    continue

                try:
                    data_ref = datetime.fromtimestamp(last_ts).date().isoformat()
                except (ValueError, OSError, TypeError):
                    data_ref = date.today().isoformat()

                results.append({
                    "data_referencia": data_ref,
                    "tipo": "preco",
                    "commodity": commodity,
                    "metrica": f"fechamento_{codigo}",
                    "valor": float(last_close),
                    "unidade": unidade,
                    "contexto": f"ticker={ticker_fwd} venc={label}",
                    "raw": {"ticker": ticker_fwd, "codigo_contrato": codigo, "label": label},
                })

        return results
