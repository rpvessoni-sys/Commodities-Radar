"""Forecast 7d/30d para soja, farelo e oleo (CBOT + paridade BR).

Metodologia (hibrida):
1. **Bandas estatisticas** (este modulo): MA20 + volatilidade + tendencia linear curta.
   Garante uma faixa razoavel ancorada em dados.
2. **Narrativa contextual** (gerada pelo Claude Code lendo last_dump.md):
   refina o vies baseado em drivers fundamentais (WASDE, CFTC, clima, etc).

Salva resultados em tabela `forecasts` para backtest posterior.

Comando:
    python main.py forecast               # gera forecast atual (7d + 30d)
    python main.py forecast --resolve     # preenche realizados de forecasts vencidos
"""
import math
from datetime import date, timedelta, datetime
from statistics import mean, stdev

import config
import db


# ESCOPO (2026-05-26): apenas complexo soja. Milho removido.
COMMODITIES_ALVO = [
    "soja_cbot",
    "farelo_cbot",
    "oleo_cbot",
]


def gerar_forecasts(target_date: date | None = None) -> dict:
    """Gera bandas estatisticas para horizontes 7d e 30d. Salva no DB."""
    target = target_date or date.today()
    saved = 0
    errors = []

    for commodity in COMMODITIES_ALVO:
        historico = _buscar_historico(commodity, target, dias=60)
        if len(historico) < 8:
            errors.append(f"{commodity}: historico curto demais ({len(historico)} obs, precisa >=8)")
            continue

        for horizonte_dias in (7, 30):
            data_alvo = target + timedelta(days=horizonte_dias)
            banda = _calcular_banda(historico, horizonte_dias)
            premissas = (
                f"Base: ultimas {len(historico)} obs. "
                f"Spot={banda['spot']:.2f}, MA20={banda['ma20']:.2f}, "
                f"vol_anual={banda['vol_anual']*100:.1f}%, "
                f"slope_20={banda['slope']:+.4f}/dia."
            )

            try:
                with db.connect() as conn:
                    conn.execute(
                        """
                        INSERT OR REPLACE INTO forecasts
                        (data_geracao, horizonte_dias, data_alvo, commodity, metrica,
                         valor_baixo, valor_central, valor_alto, vies, metodo, premissas)
                        VALUES (?, ?, ?, ?, 'fechamento', ?, ?, ?, ?, 'ma20_vol_bands', ?)
                        """,
                        (
                            target.isoformat(),
                            horizonte_dias,
                            data_alvo.isoformat(),
                            commodity,
                            round(banda["baixo"], 4),
                            round(banda["central"], 4),
                            round(banda["alto"], 4),
                            banda["vies"],
                            premissas,
                        ),
                    )
                saved += 1
            except Exception as e:
                errors.append(f"{commodity} {horizonte_dias}d: {e}")

    return {"saved": saved, "errors": errors, "data_geracao": target.isoformat()}


def _buscar_historico(commodity: str, ate_data: date, dias: int = 60) -> list[tuple[str, float]]:
    """Retorna [(data, fechamento), ...] em ordem cronologica crescente."""
    with db.connect() as conn:
        cur = conn.execute(
            """
            SELECT data_referencia, valor
            FROM dados_publicos
            WHERE fonte='cme_cbot' AND commodity=? AND metrica='fechamento'
              AND data_referencia <= date(?)
              AND data_referencia >= date(?, '-' || ? || ' days')
            ORDER BY data_referencia ASC
            """,
            (commodity, ate_data.isoformat(), ate_data.isoformat(), dias),
        )
        return [(r["data_referencia"], r["valor"]) for r in cur]


def _calcular_banda(historico: list[tuple[str, float]], horizonte_dias: int) -> dict:
    """Calcula banda baixo/central/alto via MA20 + vol + slope."""
    precos = [p for _, p in historico]
    spot = precos[-1]

    # MA20 (ou MA(n) se nao tiver 20)
    n_ma = min(20, len(precos))
    ma20 = mean(precos[-n_ma:])

    # Retornos log diarios
    retornos = []
    for i in range(1, len(precos)):
        if precos[i-1] > 0 and precos[i] > 0:
            r = math.log(precos[i] / precos[i-1])
            retornos.append(r)

    vol_diaria = stdev(retornos) if len(retornos) > 1 else 0.01
    vol_anual = vol_diaria * math.sqrt(252)

    # Slope linear curto (20d) — quanto preco mexe por dia
    x = list(range(min(20, len(precos))))
    y = precos[-len(x):]
    slope = _slope(x, y)

    # Projecao central: spot + slope * dias (tendencia linear curta)
    # Mas suavizada por mean-reversion para MA20
    drift = slope * horizonte_dias
    mean_revert = (ma20 - spot) * min(horizonte_dias / 40.0, 0.5)  # 50% revert em 40d
    central = spot + drift + mean_revert

    # Banda: vol * sqrt(horizonte/252) * z (z=1.5 = ~87% confidence)
    sigma_horizonte = spot * vol_diaria * math.sqrt(horizonte_dias)
    z = 1.5
    baixo = central - z * sigma_horizonte
    alto = central + z * sigma_horizonte

    # Vies
    if abs(drift + mean_revert) / spot < 0.005:
        vies = "lateral"
    elif central > spot:
        vies = "altista"
    else:
        vies = "baixista"

    return {
        "spot": spot,
        "ma20": ma20,
        "vol_anual": vol_anual,
        "slope": slope,
        "central": central,
        "baixo": baixo,
        "alto": alto,
        "vies": vies,
    }


def _slope(x: list[float], y: list[float]) -> float:
    """Regressao linear simples — retorna slope (b1)."""
    n = len(x)
    if n < 2:
        return 0.0
    mx = mean(x)
    my = mean(y)
    num = sum((x[i] - mx) * (y[i] - my) for i in range(n))
    den = sum((x[i] - mx) ** 2 for i in range(n))
    return num / den if den != 0 else 0.0


def resolver_realizados(target_date: date | None = None) -> dict:
    """Para forecasts com data_alvo <= hoje e sem realizado, busca preco real e preenche.

    Retorna stats: total revisado, hit_banda, hit_direcional.
    """
    target = target_date or date.today()
    revisados = 0
    hits_banda = 0
    hits_direcional = 0

    with db.connect() as conn:
        # Pega forecasts pendentes
        cur = conn.execute(
            """
            SELECT id, data_geracao, horizonte_dias, data_alvo, commodity, metrica,
                   valor_baixo, valor_central, valor_alto, vies
            FROM forecasts
            WHERE data_alvo <= ?
              AND valor_realizado IS NULL
            ORDER BY data_alvo
            """,
            (target.isoformat(),),
        )
        pendentes = list(cur)

    for f in pendentes:
        # Busca preco real
        realizado = _preco_realizado(f["commodity"], f["data_alvo"])
        if realizado is None:
            continue

        # Hit na banda?
        hit_banda = f["valor_baixo"] <= realizado <= f["valor_alto"]

        # Hit direcional? (precisamos do spot da data_geracao para comparar)
        spot_geracao = _preco_realizado(f["commodity"], f["data_geracao"])
        hit_direcional = None
        if spot_geracao is not None:
            move_real = realizado - spot_geracao
            move_proj = f["valor_central"] - spot_geracao
            if f["vies"] == "lateral":
                hit_direcional = abs(move_real / spot_geracao) < 0.02
            else:
                hit_direcional = (move_real > 0 and move_proj > 0) or (move_real < 0 and move_proj < 0)

        erro_pct = ((realizado - f["valor_central"]) / f["valor_central"]) * 100 if f["valor_central"] else None

        with db.connect() as conn:
            conn.execute(
                """
                UPDATE forecasts
                SET valor_realizado=?, hit=?, hit_direcional=?, erro_pct=?, data_realizacao=?
                WHERE id=?
                """,
                (
                    realizado,
                    1 if hit_banda else 0,
                    1 if hit_direcional else 0 if hit_direcional is not None else None,
                    round(erro_pct, 4) if erro_pct is not None else None,
                    target.isoformat(),
                    f["id"],
                ),
            )

        revisados += 1
        if hit_banda:
            hits_banda += 1
        if hit_direcional:
            hits_direcional += 1

    return {
        "revisados": revisados,
        "hits_banda": hits_banda,
        "hits_direcional": hits_direcional,
        "hit_rate_banda": hits_banda / revisados if revisados > 0 else None,
        "hit_rate_direcional": hits_direcional / revisados if revisados > 0 else None,
    }


def _preco_realizado(commodity: str, data: str) -> float | None:
    """Busca preco mais proximo da data (ate 5 dias antes)."""
    with db.connect() as conn:
        cur = conn.execute(
            """
            SELECT valor FROM dados_publicos
            WHERE fonte='cme_cbot' AND commodity=? AND metrica='fechamento'
              AND data_referencia <= ?
              AND data_referencia >= date(?, '-5 days')
            ORDER BY data_referencia DESC
            LIMIT 1
            """,
            (commodity, data, data),
        )
        row = cur.fetchone()
        return row["valor"] if row else None


def listar_forecasts_recentes(limit: int = 20) -> list[dict]:
    """Retorna forecasts mais recentes para display."""
    with db.connect() as conn:
        cur = conn.execute(
            """
            SELECT data_geracao, horizonte_dias, data_alvo, commodity, metrica,
                   valor_baixo, valor_central, valor_alto, vies,
                   valor_realizado, hit, hit_direcional, erro_pct
            FROM forecasts
            ORDER BY data_geracao DESC, horizonte_dias, commodity
            LIMIT ?
            """,
            (limit,),
        )
        return [dict(r) for r in cur]
