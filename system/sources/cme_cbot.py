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


def _fetch_chart(url: str, headers: dict, timeout: int = 15) -> dict:
    """Busca o chart do Yahoo. Se o IP direto for bloqueado (comum em datacenter
    como o GitHub Actions), tenta de novo via ScraperAPI (IP residencial). Levanta
    excecao so se AMBOS falharem — o caller registra o erro normalmente."""
    import requests
    try:
        r = requests.get(url, headers=headers, timeout=timeout)
        r.raise_for_status()
        return r.json()
    except Exception:
        # Fallback: mesma URL via ScraperAPI (so se a chave estiver configurada)
        from .scraper import fetch_via_scraper, is_configured
        if not is_configured():
            raise
        r = fetch_via_scraper(url, render=False, timeout=90)
        if r.status_code != 200:
            raise RuntimeError(f"scraper HTTP {r.status_code}")
        return r.json()


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


# Roll: quantos dias antes do MES DE ENTREGA o mercado ja migrou pro proximo
# contrato (aprox. do roll por volume / first notice day do complexo soja). Ex: em
# 23/jun o julho ja rolou pro agosto — igual o Barchart mostra como contrato ativo.
ROLL_DIAS = 12
_MES_NUM = {c: m for m, c in MES_CME.items()}   # 'N' -> 7


def _front_contract(commodity: str, ref: date | None = None) -> tuple[str, str, str] | None:
    """Contrato ATIVO (front) = o vencimento liquido mais proximo, ROLANDO pro
    proximo quando faltam <= ROLL_DIAS pro mes de entrega. Devolve (ticker, codigo,
    label) ou None. Existe porque o simbolo continuo do Yahoo (ZL=F/ZS=F) rola
    ERRADO perto do vencimento (em 23/jun o ZL=F retornava o contrato de dezembro)."""
    ref = ref or date.today()
    for ticker, codigo, label in _proximos_vencimentos(commodity, n=4, ref=ref):
        mes = _MES_NUM.get(codigo[:1])
        try:
            ano = 2000 + int(codigo[1:])
        except ValueError:
            continue
        if mes and (date(ano, mes, 1) - ref).days > ROLL_DIAS:
            return (ticker, codigo, label)
    vs = _proximos_vencimentos(commodity, n=1, ref=ref)
    return vs[0] if vs else None


def _serie_ohlc(ticker, commodity, unidade, headers, start_ts, end_ts) -> list[dict] | None:
    """Serie diaria OHLC de um ticker (com guard anti-carry). None se nao houver
    dado utilizavel — o caller tenta o fallback (=F)."""
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{quote(ticker)}"
           f"?period1={start_ts}&period2={end_ts}&interval=1d")
    try:
        data = _fetch_chart(url, headers)
    except Exception:
        return None
    try:
        chart = data["chart"]["result"][0]
        timestamps = chart.get("timestamp", []) or []
        ind = chart.get("indicators", {}).get("quote", [{}])[0]
        opens, highs = ind.get("open", []), ind.get("high", [])
        lows, closes, volumes = ind.get("low", []), ind.get("close", []), ind.get("volume", [])
    except (KeyError, IndexError, TypeError):
        return None
    if not any(c is not None for c in closes):
        return None
    # Guard anti-carry: nao gravar o fechamento da ultima barra (dia em formacao)
    # se repetir exatamente o anterior (cotacao travada do Yahoo).
    idx_close = [j for j in range(len(timestamps)) if j < len(closes) and closes[j] is not None]
    skip_close_i = idx_close[-1] if (len(idx_close) >= 2 and closes[idx_close[-1]] == closes[idx_close[-2]]) else None
    out = []
    for i, ts in enumerate(timestamps):
        try:
            data_ref = datetime.fromtimestamp(ts).date().isoformat()
        except (ValueError, OSError):
            continue
        for metrica, lista, un in (("abertura", opens, unidade), ("maxima", highs, unidade),
                                   ("minima", lows, unidade), ("fechamento", closes, unidade),
                                   ("volume", volumes, "contratos")):
            if i >= len(lista) or lista[i] is None:
                continue
            if metrica == "fechamento" and i == skip_close_i:
                continue
            out.append({"data_referencia": data_ref, "tipo": "preco", "commodity": commodity,
                        "metrica": metrica, "valor": float(lista[i]), "unidade": un,
                        "contexto": f"ticker={ticker}", "raw": {"ticker": ticker, "ts": ts}})
    return out or None


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

        # ====== FRONT-MONTH = CONTRATO ATIVO (o numero do Barchart) ======
        # O simbolo continuo do Yahoo (ZS=F/ZM=F/ZL=F) rola ERRADO perto do
        # vencimento — em 23/jun o ZL=F vinha do contrato de DEZEMBRO e o ZS=F de
        # NOVEMBRO. Buscamos o CONTRATO ATIVO explicito (ex ZLQ26.CBT), que bate com
        # o Barchart. Fallback pro =F so se o contrato ativo nao tiver dado.
        FRONT = [("soja_cbot", "USD/bushel", "ZS=F"),
                 ("farelo_cbot", "USD/short_ton", "ZM=F"),
                 ("oleo_cbot", "USD_cts/lb", "ZL=F")]
        for commodity, unidade, fallback in FRONT:
            fc = _front_contract(commodity)
            tentativas = ([fc[0]] if fc else []) + [fallback]
            serie = None
            for tk in tentativas:
                serie = _serie_ohlc(tk, commodity, unidade, headers, start_ts, end_ts)
                if serie:
                    break
            if serie:
                results.extend(serie)
            else:
                results.append({
                    "data_referencia": date.today().isoformat(), "tipo": "erro",
                    "commodity": commodity, "metrica": "fetch_error", "valor": None,
                    "contexto": f"front {tentativas} sem dado (Yahoo+ScraperAPI falharam)",
                })

        # Heating oil — =F mesmo (mercado distinto, sem roll do complexo soja)
        serie_ho = _serie_ohlc("HO=F", "heating_oil_cbot", "USD/galão", headers, start_ts, end_ts)
        if serie_ho:
            results.extend(serie_ho)

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
                    data = _fetch_chart(url, headers)
                except Exception:
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
