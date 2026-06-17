"""Gera relatorio diario em HTML estruturado para visualizacao no navegador.

Le dados do DB e renderiza HTML com:
- Snapshot atual (preco CBOT + paridade BR)
- Forecasts 7d/30d
- Alertas tecnicos
- Eventos calendarizados
- Atrasos StoneX
- Perguntas fixas (StoneX WhatsApp, consultor, forecasts vencendo)

Seções narrativas (resumo executivo, 5 insights, drivers) ficam como
placeholders preenchidos pelo Claude Code quando voce abrir o Claude Code
e pedir refinamento.
"""
import json
import re
from datetime import date, datetime, timedelta
from pathlib import Path

import config
import db
import precos_fisicos as pf
import insights as ins_mod
import curvas as cv_mod
import tributario as trib_mod
import charts_svg as ch


# Fatores de conversao USD CBOT → BRL na unidade BR padrao
# Formula: valor_cbot × fator × USD_BRL = BRL/unidade_br
#
# - Soja:   cents/bu × 0.022046      × USD/BRL = BRL/sc60kg
#     1 bushel = 60 lb = 27,2155 kg
#     1 saca BR = 60 kg → 1 saca = 60/27,2155 = 2,2046 bu
#     cents/bu × (2,2046 bu/sc) / (100 cents/USD) = USD/sc = cents/bu × 0,022046
#
# - Farelo: USD/short_ton × 1.10231  × USD/BRL = BRL/ton métrica
#     1 short ton = 907,185 kg → 1 ton métrica = 1/0,907185 = 1,10231 short ton
#
# - Oleo:   cents/lb × 22.0462       × USD/BRL = BRL/ton métrica
#     1 ton = 2204,62 lb → cents/lb × 2204,62 / 100 cents/USD = USD/ton métrica
PARIDADES = {
    "soja_cbot":   {"fator": 0.022046,         "unidade_br": "/sc"},
    "farelo_cbot": {"fator": 1 / 0.907185,     "unidade_br": "/ton"},
    "oleo_cbot":   {"fator": 22.0462,          "unidade_br": "/ton"},
}


def gerar_html(target_date: date | None = None) -> Path:
    target = target_date or date.today()
    dados = _coletar_dados(target)
    html = _renderizar(dados)
    out = config.REPORTS_DIR / f"{target.isoformat()}_daily.html"
    out.write_text(html, encoding="utf-8")
    # Atalho 'latest.html' sempre aponta pro relatorio mais recente
    latest = config.REPORTS_DIR / "latest.html"
    latest.write_text(html, encoding="utf-8")
    return out


# ============================================================
# Coleta de dados do DB
# ============================================================

def _coletar_dados(target: date) -> dict:
    base = {
        "target": target,
        "now": datetime.now(),
        "snapshot": _get_snapshot(target),
        "forecasts": _get_forecasts_ativos(target),
        "alertas_tecnicos": _get_alertas_tecnicos(),
        "noticias": _get_noticias_filtradas(target),
        "fisico_br": _get_fisico_br(target),
        "far_soj": _get_far_soj_ratio(target),
        "crush_matrix": _get_crush_matrix(target),
        "biodiesel_us": _get_biodiesel_margin(target),
        "insights_estudo": ins_mod.list_insights(),
        "curva_forward": _get_curva_forward(target),
        "eventos": _get_eventos_proximos(target),
        "tributario": trib_mod.get_monitor(target),
        "tese_ativa": _get_tese_ativa(),
        "wasde_br": _get_wasde_brasil(),
        "saude_fontes": _get_saude_fontes(),
        "forecast_calib": _get_forecast_calibracao(),
        "cot": _get_cot_posicionamento(),
        "revisoes_pendentes": _get_revisoes_pendentes(target),
        "graficos": _get_series_graficos(target),
        "fila_pendentes": _get_fila_pendentes(target),
    }
    # Geracao narrativa heuristica (baseada em regras sobre os dados)
    base["resumo_executivo"] = _gerar_resumo_executivo(base)
    base["insights"] = _gerar_insights(base)
    base["drivers"] = _gerar_drivers(base)
    base["conviccao"] = _gerar_conviccao(base)
    return base


def _get_wasde_brasil() -> dict:
    """Pega projecao WASDE Brasil 26/27 (producao soja/farelo/oleo)."""
    out = {}
    with db.connect() as conn:
        for commodity, key in [("soja_brazil", "soja"),
                                ("farelo_brazil", "farelo"),
                                ("oleo_brazil", "oleo")]:
            cur = conn.execute(
                """
                SELECT valor FROM dados_publicos
                WHERE fonte='usda_wasde' AND commodity=?
                  AND metrica='production_2026/2027_may'
                LIMIT 1
                """,
                (commodity,),
            )
            row = cur.fetchone()
            if row:
                out[key] = row["valor"]
    return out


# Cadencia esperada por fonte (dias) e tolerancia antes de marcar atraso.
# Fontes mensais NAO devem ficar vermelhas por design (licao dos alertas ruidosos).
_CADENCIA_FONTES = {
    "cme_cbot": (1, 3), "bcb": (1, 4), "cepea_rss": (1, 4),
    "cepea_paranagua": (1, 5), "nag_fisico": (1, 5),
    "inmet": (1, 3), "noaa_cpc": (1, 5),
    "noticias_rss": (1, 4),
    "anec": (7, 10), "bcba": (7, 10), "cftc_cot": (7, 10),
    "usda_crop_progress": (7, 12),
    "abiove": (31, 40), "mpob": (31, 40), "nopa": (31, 50),
    "usda_wasde": (31, 40),
}


def _get_saude_fontes() -> list[dict]:
    """Ultima execucao de cada coletor do registry, classificada vs cadencia esperada.

    Itera sobre o registry (fonte de verdade do que esta ativo) e cruza com
    coletas_log (quando o coletor RODOU de fato). data_referencia nao serve:
    fontes como ABIOVE gravam projecoes com data futura. Coletores legados que
    sairam do registry (ex. 'cepea' antigo) nao aparecem — nao sao atraso.
    """
    from sources import registry as _reg

    ultimas = {}
    with db.connect() as conn:
        cur = conn.execute(
            """
            SELECT fonte, MAX(inicio) ultima, status, registros_saved, erro
            FROM coletas_log
            GROUP BY fonte
            """
        )
        for r in cur:
            ultimas[r["fonte"]] = dict(r)

    out = []
    hoje = datetime.now()
    for src in _reg.list_all():
        fonte = src["source"]
        log = ultimas.get(fonte)
        cadencia, tolerancia = _CADENCIA_FONTES.get(fonte, (7, 14))

        if not src["enabled"]:
            estado, ultima, dias, registros, erro = "desativada", "—", None, None, ""
        elif log is None:
            estado, ultima, dias, registros, erro = "erro", "nunca rodou", None, None, ""
        else:
            ultima = (log["ultima"] or "")[:16].replace("T", " ")
            try:
                dias = (hoje - datetime.fromisoformat(log["ultima"])).days
            except (ValueError, TypeError):
                dias = None
            registros = log["registros_saved"]
            erro = (log["erro"] or "")[:120]
            if log["status"] not in (None, "ok"):
                estado = "erro"
            elif dias is not None and dias > tolerancia:
                estado = "atrasada"
            else:
                estado = "ok"

        out.append({
            "fonte": fonte,
            "ultima": ultima,
            "dias": dias,
            "estado": estado,
            "registros": registros,
            "erro": erro,
            "cadencia": cadencia,
        })

    # problemas primeiro, depois ok, desativadas no fim
    ordem = {"erro": 0, "atrasada": 1, "ok": 2, "desativada": 3}
    out.sort(key=lambda f: (ordem.get(f["estado"], 9), f["fonte"]))
    return out


def _get_forecast_calibracao() -> list[dict]:
    """Hit-rate observado dos forecasts resolvidos, por horizonte.

    Exposto no HTML por honestidade de modelo: bandas z=1.5 prometem ~87%
    de cobertura teorica; o realizado diz se da pra confiar nelas.
    """
    out = []
    with db.connect() as conn:
        cur = conn.execute(
            """
            SELECT horizonte_dias, COUNT(*) n,
                   SUM(hit) hits_banda, SUM(hit_direcional) hits_dir
            FROM forecasts
            WHERE valor_realizado IS NOT NULL
            GROUP BY horizonte_dias
            ORDER BY horizonte_dias
            """
        )
        for r in cur:
            n = r["n"] or 0
            out.append({
                "horizonte": r["horizonte_dias"],
                "n": n,
                "banda_pct": round(100.0 * (r["hits_banda"] or 0) / n, 0) if n else None,
                "dir_pct": round(100.0 * (r["hits_dir"] or 0) / n, 0) if n else None,
            })
    return out


def _get_snapshot(target: date) -> dict:
    """Snapshot CBOT atual + paridades BR + indicadores."""
    out = {}
    with db.connect() as conn:
        # Preços CBOT mais recentes + variação D-1 + contexto 52 semanas
        for commodity in ["soja_cbot", "farelo_cbot", "oleo_cbot"]:
            rows = conn.execute(
                """
                SELECT data_referencia, valor FROM dados_publicos
                WHERE fonte='cme_cbot' AND commodity=? AND metrica='fechamento'
                ORDER BY data_referencia DESC LIMIT 2
                """,
                (commodity,),
            ).fetchall()
            if not rows:
                continue
            info = {"valor": rows[0]["valor"], "data": rows[0]["data_referencia"]}
            if len(rows) == 2 and rows[1]["valor"]:
                info["delta"] = rows[0]["valor"] - rows[1]["valor"]
                info["delta_pct"] = info["delta"] / rows[1]["valor"] * 100
            # Range/percentil 52 semanas — depende do backfill 5y; com série
            # curta (<60 pregões) fica omitido pra não dar percentil enganoso
            est = conn.execute(
                """
                SELECT MIN(valor) lo, MAX(valor) hi, COUNT(*) n,
                       SUM(CASE WHEN valor <= ? THEN 1 ELSE 0 END) abaixo
                FROM dados_publicos
                WHERE fonte='cme_cbot' AND commodity=? AND metrica='fechamento'
                  AND data_referencia >= date(?, '-365 days')
                """,
                (info["valor"], commodity, info["data"]),
            ).fetchone()
            if est and est["n"] and est["n"] >= 60:
                info["min52"], info["max52"] = est["lo"], est["hi"]
                info["pct52"] = 100.0 * est["abaixo"] / est["n"]
            out[commodity] = info

        # Cambio USD/BRL
        cur = conn.execute(
            """
            SELECT data_referencia, valor FROM dados_publicos
            WHERE fonte='bcb' AND commodity='usd_brl_ptax' AND metrica='valor'
            ORDER BY data_referencia DESC LIMIT 1
            """
        )
        row = cur.fetchone()
        out["usd_brl"] = {"valor": row["valor"], "data": row["data_referencia"]} if row else None

        # Crush margin
        cur = conn.execute(
            """
            SELECT data_referencia, valor FROM dados_publicos
            WHERE fonte='indicators' AND commodity='complexo_soja' AND metrica='crush_margin_usd_bu'
            ORDER BY data_referencia DESC LIMIT 1
            """
        )
        row = cur.fetchone()
        out["crush_margin"] = {"valor": row["valor"], "data": row["data_referencia"]} if row else None

        # Oil share
        cur = conn.execute(
            """
            SELECT data_referencia, valor FROM dados_publicos
            WHERE fonte='indicators' AND commodity='complexo_soja' AND metrica='oil_share_pct'
            ORDER BY data_referencia DESC LIMIT 1
            """
        )
        row = cur.fetchone()
        out["oil_share"] = {"valor": row["valor"], "data": row["data_referencia"]} if row else None

        # Paridade BR (calculada pelo indicators)
        cur = conn.execute(
            """
            SELECT data_referencia, valor FROM dados_publicos
            WHERE fonte='indicators' AND commodity='soja_paridade_br' AND metrica='brl_saca_paridade'
            ORDER BY data_referencia DESC LIMIT 1
            """
        )
        row = cur.fetchone()
        out["soja_brl_paridade"] = {"valor": row["valor"], "data": row["data_referencia"]} if row else None

        # CFTC managed money net soja
        cur = conn.execute(
            """
            SELECT data_referencia, valor FROM dados_publicos
            WHERE fonte='cftc_cot' AND commodity='soja_cbot' AND metrica='managed_money_net'
            ORDER BY data_referencia DESC LIMIT 2
            """
        )
        cftc_rows = list(cur)
        if cftc_rows:
            out["cftc_net"] = {"valor": cftc_rows[0]["valor"], "data": cftc_rows[0]["data_referencia"]}
            if len(cftc_rows) > 1 and cftc_rows[1]["valor"]:
                delta = (cftc_rows[0]["valor"] - cftc_rows[1]["valor"]) / cftc_rows[1]["valor"] * 100
                out["cftc_net"]["delta_pct"] = delta

        # USDA Crop Progress soja % planted (mais recente)
        cur = conn.execute(
            """
            SELECT data_referencia, valor FROM dados_publicos
            WHERE fonte='usda_crop_progress' AND commodity='soybeans_eua' AND metrica='pct_planted'
            ORDER BY data_referencia DESC LIMIT 1
            """
        )
        row = cur.fetchone()
        out["plantio_soja_eua"] = {"valor": row["valor"], "data": row["data_referencia"]} if row else None

    # Calcular paridades em R$ (CBOT × câmbio)
    usd_brl = out["usd_brl"]["valor"] if out.get("usd_brl") else None
    if usd_brl:
        for key in ["soja_cbot", "farelo_cbot", "oleo_cbot"]:
            if key in out:
                fator = PARIDADES[key]["fator"]
                val_cbot = out[key]["valor"]
                out[key]["brl"] = val_cbot * fator * usd_brl

        # Crush margin em R$/ton soja
        # Formula: $/bu × 36.7437 (bu/MT) × USD/BRL = R$/MT
        if out.get("crush_margin"):
            cm_usd_bu = out["crush_margin"]["valor"]
            out["crush_margin"]["brl_ton"] = cm_usd_bu * 36.7437 * usd_brl

    return out


def _get_forecasts_ativos(target: date) -> list[dict]:
    """Forecasts gerados recentemente com data_alvo no futuro."""
    out = []
    with db.connect() as conn:
        cur = conn.execute(
            """
            SELECT data_geracao, horizonte_dias, data_alvo, commodity,
                   valor_baixo, valor_central, valor_alto, vies
            FROM forecasts
            WHERE date(data_alvo) >= ?
              AND date(data_geracao) >= date(?, '-2 days')
            ORDER BY commodity, horizonte_dias
            """,
            (target.isoformat(), target.isoformat()),
        )
        for r in cur:
            out.append(dict(r))
    return out


# Nomes humanos das series alertaveis (alertas e KPIs)
_LABEL_COMMODITY = {
    "soja_cbot": "Soja CBOT", "farelo_cbot": "Farelo CBOT", "oleo_cbot": "Óleo CBOT",
    "usd_brl_ptax": "USD/BRL PTAX", "complexo_soja": "Crush margin",
    "farelo_paranagua": "Prêmio farelo PGUA", "oleo_paranagua": "Prêmio óleo PGUA",
}

# Leitura de mercado por (commodity, tipo de quebra) — classe = sinal de preço
# bull/bear (não 'bom/ruim pro comprador'); USD/BRL é neutro (só desloca paridades).
_ALERTA_LENTE = {
    ("farelo_cbot", "quebra_suporte"): ("bear", "farelo rompeu o suporte — momentum de baixa; spread far÷soj tende a comprimir vs soja"),
    ("farelo_cbot", "quebra_resistencia"): ("bull", "farelo rompeu a resistência — momentum de alta; spread far÷soj tende a esticar vs soja"),
    ("complexo_soja", "quebra_suporte"): ("bull", "crush recuou abaixo do suporte — esmagadora desacelera, menos farelo/óleo novo (suporte aos produtos)"),
    ("complexo_soja", "quebra_resistencia"): ("bear", "crush rompeu a resistência — esmagamento a fundo, mais farelo/óleo ofertado (pressão nos produtos)"),
    ("usd_brl_ptax", "quebra_resistencia"): ("neutral", "dólar rompeu — paridades em R$ sobem mesmo com o CBOT parado"),
    ("usd_brl_ptax", "quebra_suporte"): ("neutral", "real firme — paridades em R$ recuam mesmo com o CBOT parado"),
    ("oleo_cbot", "quebra_suporte"): ("bear", "óleo rompeu o suporte — momentum de baixa; pode comprimir o crush e o oil share"),
}


def _get_alertas_tecnicos() -> list[dict]:
    """Alertas do JSON reconciliados com a config VIVA.

    O JSON e gerado pelo alerts_technical (scheduler); se os niveis do
    alerts_config.toml mudaram depois (recalibracao), alerta de nivel antigo
    e ruido — descarta. Licao de 2026-06-11: JSON da manha citava resistencia
    2,00 horas depois do TOML ir pra 4,25.
    """
    path = config.DATA_DIR / "alerts_technical.json"
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        alertas = data.get("alertas", [])
    except Exception:
        return []

    niveis = _niveis_alerta()
    out = []
    for a in alertas:
        tipo = a.get("tipo", "")
        comm = a.get("commodity", "")
        cfg = niveis.get(comm) or {}
        if tipo == "quebra_suporte" and a.get("nivel") is not None:
            if cfg.get("suporte") is not None and abs(cfg["suporte"] - a["nivel"]) > 1e-9:
                continue  # nivel recalibrado apos a geracao do JSON — stale
        elif tipo == "quebra_resistencia" and a.get("nivel") is not None:
            if cfg.get("resistencia") is not None and abs(cfg["resistencia"] - a["nivel"]) > 1e-9:
                continue
        # Enriquecer pra renderizacao humana
        a["label"] = _LABEL_COMMODITY.get(comm, comm)
        lente = _ALERTA_LENTE.get((comm, tipo))
        if lente:
            a["lente_classe"], a["lente_texto"] = lente
        out.append(a)
    return out


def _get_curva_forward(target: date) -> dict:
    """Lê curva forward 4 fontes: CBOT real + StoneX (manual) + Claude (heurística) + Média.

    Pesos da média: CBOT 50%, StoneX 30%, Claude 20% (configurável aqui).
    Se StoneX vazio, redistribui peso: CBOT 70%, Claude 30%.
    """
    PESOS = {"cbot": 0.50, "stonex": 0.30, "claude": 0.20}

    out = {}
    ORDEM_MES = "FGHJKMNQUVXZ"

    def _key_ordenacao(codigo: str) -> tuple:
        try:
            letra = codigo[0]
            yr = int(codigo[1:])
            return (yr, ORDEM_MES.index(letra) + 1)
        except (ValueError, IndexError):
            return (99, 99)

    LABEL_MES = {"F":"jan","G":"fev","H":"mar","J":"abr","K":"mai","M":"jun",
                 "N":"jul","Q":"ago","U":"set","V":"out","X":"nov","Z":"dez"}

    with db.connect() as conn:
        for commodity in ["soja_cbot", "farelo_cbot", "oleo_cbot"]:
            # === 1. CBOT real (dados_publicos) ===
            cur = conn.execute(
                """
                SELECT metrica, valor, unidade
                FROM dados_publicos
                WHERE fonte='cme_cbot' AND commodity=?
                  AND metrica LIKE 'fechamento_%' AND metrica != 'fechamento'
                GROUP BY metrica HAVING MAX(data_referencia)
                ORDER BY metrica
                """,
                (commodity,),
            )
            cbot_por_venc = {}
            unidade = "?"
            for r in cur:
                codigo = r["metrica"].replace("fechamento_", "")
                cbot_por_venc[codigo] = r["valor"]
                unidade = r["unidade"]

            # === 2. StoneX (curvas_predicao fonte=stonex) ===
            stonex_raw = cv_mod.latest_por_fonte("stonex", commodity)
            stonex_por_venc = {v: r["valor"] for v, r in stonex_raw.items()}

            # === 3. Claude (curvas_predicao fonte=claude) ===
            claude_raw = cv_mod.latest_por_fonte("claude", commodity)
            claude_por_venc = {v: r["valor"] for v, r in claude_raw.items()}
            claude_razoes = {v: (json.loads(r["razoes"]) if r.get("razoes") else [])
                             for v, r in claude_raw.items()}

            # Lista todos os vencimentos disponíveis (união)
            todos_venc = set(cbot_por_venc) | set(stonex_por_venc) | set(claude_por_venc)
            venc_sorted = sorted(todos_venc, key=_key_ordenacao)

            vencs = []
            for codigo in venc_sorted:
                cbot_v = cbot_por_venc.get(codigo)
                stonex_v = stonex_por_venc.get(codigo)
                claude_v = claude_por_venc.get(codigo)

                # Cálculo da média ponderada (ignora fontes vazias e redistribui)
                pares = []
                if cbot_v is not None:
                    pares.append(("cbot", cbot_v, PESOS["cbot"]))
                if stonex_v is not None:
                    pares.append(("stonex", stonex_v, PESOS["stonex"]))
                if claude_v is not None:
                    pares.append(("claude", claude_v, PESOS["claude"]))
                media_v = None
                if pares:
                    soma_peso = sum(p[2] for p in pares)
                    media_v = sum(v * p / soma_peso for _, v, p in pares)

                # Deltas StoneX e Claude vs CBOT
                stonex_delta_pct = None
                if cbot_v and stonex_v is not None:
                    stonex_delta_pct = ((stonex_v - cbot_v) / cbot_v) * 100
                claude_delta_pct = None
                if cbot_v and claude_v is not None:
                    claude_delta_pct = ((claude_v - cbot_v) / cbot_v) * 100

                letra = codigo[0] if codigo else "?"
                yr = codigo[1:] if len(codigo) > 1 else ""
                label = f"{LABEL_MES.get(letra, '?')}/{yr}"

                vencs.append({
                    "codigo": codigo,
                    "label": label,
                    "cbot": cbot_v,
                    "stonex": stonex_v,
                    "claude": claude_v,
                    "media": media_v,
                    "stonex_delta_pct": stonex_delta_pct,
                    "claude_delta_pct": claude_delta_pct,
                    "claude_razoes": claude_razoes.get(codigo, []),
                    "unidade": unidade,
                })

            out[commodity] = vencs

    out["_pesos"] = PESOS
    return out


def _get_biodiesel_margin(target: date) -> dict:
    """Margem biodiesel americano e sensibilidades.

    Tese StoneX 25mai 2026: o que sustenta o preço do óleo soja CBOT hoje é
    a margem do biodiesel via demanda RIN. Se margem cair, óleo cai.

    Conta:
        receita = HO Chicago + 1.5 × RIN D4
        custo   = 7.5 × óleo_cents_lb/100 + custo_industrial
        margem  = receita − custo
    """
    import params_user as pu

    rin = pu.get_param("rin_d4") or {}
    custo_ind = pu.get_param("custo_industrial_biodiesel_us") or {}
    yield_oleo = pu.get_param("yield_oleo_lb_per_galao") or {}
    yield_rin = pu.get_param("yield_rin_per_galao") or {}

    out = {
        "rin_d4": rin,
        "custo_industrial": custo_ind,
        "yield_oleo": yield_oleo,
        "yield_rin": yield_rin,
        "margem": None,
        "receita": None,
        "custo_total": None,
        "custo_oleo": None,
        "ho_chicago": None,
        "oleo_cents_lb": None,
        "data": None,
        "sensibilidade": [],
        "alerta": None,
    }

    with db.connect() as conn:
        # Pega HO + óleo mais recentes do mesmo dia (preferindo data mais recente)
        cur = conn.execute(
            """
            SELECT data_referencia, commodity, valor FROM dados_publicos
            WHERE fonte='cme_cbot' AND metrica='fechamento'
              AND commodity IN ('heating_oil_cbot','oleo_cbot')
            ORDER BY data_referencia DESC, commodity
            """
        )
        por_data = {}
        for r in cur:
            por_data.setdefault(r["data_referencia"], {})[r["commodity"]] = r["valor"]

        # Acha primeira data com os dois preços
        for d, p in por_data.items():
            if "heating_oil_cbot" in p and "oleo_cbot" in p:
                out["ho_chicago"] = p["heating_oil_cbot"]
                out["oleo_cents_lb"] = p["oleo_cbot"]
                out["data"] = d
                break

    if not (out["ho_chicago"] and out["oleo_cents_lb"] and rin and custo_ind):
        return out

    ho = out["ho_chicago"]
    oleo = out["oleo_cents_lb"]
    rin_v = rin["valor"]
    custo_ind_v = custo_ind["valor"]
    yo = yield_oleo["valor"]
    yr = yield_rin["valor"]

    receita = ho + yr * rin_v
    custo_oleo = yo * (oleo / 100.0)
    custo_total = custo_oleo + custo_ind_v
    margem = receita - custo_total

    out["receita"] = receita
    out["custo_oleo"] = custo_oleo
    out["custo_total"] = custo_total
    out["margem"] = margem

    # Sensibilidades: o que acontece com a margem se cada input variar
    sens = []
    # Óleo soja +5 cts/lb (alta)
    sens.append({
        "input": "Óleo soja +5 cts/lb",
        "novo_margem": margem - (yo * 5.0 / 100.0),
        "delta": -(yo * 5.0 / 100.0),
    })
    # Óleo soja -5 cts/lb (queda)
    sens.append({
        "input": "Óleo soja −5 cts/lb",
        "novo_margem": margem + (yo * 5.0 / 100.0),
        "delta": +(yo * 5.0 / 100.0),
    })
    # HO -10% (petróleo cai forte)
    sens.append({
        "input": "Heating Oil −10%",
        "novo_margem": margem - (ho * 0.10),
        "delta": -(ho * 0.10),
    })
    # RIN -20% (alívio político)
    sens.append({
        "input": "RIN D4 −20%",
        "novo_margem": margem - (yr * rin_v * 0.20),
        "delta": -(yr * rin_v * 0.20),
    })
    out["sensibilidade"] = sens

    # Alerta
    if margem < 0:
        out["alerta"] = ("bear", "🚨 Margem NEGATIVA — esmagamento biodiesel deve reduzir, "
                                  "tese bullish do óleo soja em risco crítico.")
    elif margem < 0.5:
        out["alerta"] = ("warn", "⚠ Margem apertada (<$0,5/gal) — pequenas variações já tiram lucro. "
                                  "Tese bullish do óleo enfraquece.")
    elif margem >= 1.5:
        out["alerta"] = ("bull", "✅ Margem confortável — biodiesel rodando lucrativo, "
                                   "demanda RIN sustentada, óleo soja com piso firme.")
    else:
        out["alerta"] = ("neutral", "Margem saudável dentro da faixa $0,5-1,5/gal. "
                                      "Tese bullish do óleo soja mantida.")

    return out


def _get_far_soj_ratio(target: date) -> dict:
    """Ratio Far/Soj (farelo ÷ soja) atual + histórico + zona do spread.

    Convenção IDÊNTICA à matriz crush: far_pct = farelo_usd_sht / (soja_usd_bu × 33,333).
    Zonas do SPREAD: <80% comprimido (farelo barato vs soja), 80-87% neutro, >=87% esticado.
    Leitura de trader: extremo do spread far÷soj → mean-reversion nos dois lados (não é
    'hora de comprar'). Lê o indicador `far_soj_ratio_pct` calculado em indicators.py.
    """
    with db.connect() as conn:
        cur = conn.execute(
            """
            SELECT data_referencia, valor FROM dados_publicos
            WHERE fonte='indicators' AND commodity='complexo_soja'
              AND metrica='far_soj_ratio_pct' AND data_referencia <= ?
            ORDER BY data_referencia DESC LIMIT 30
            """,
            (target.isoformat(),),
        )
        rows = [(r["data_referencia"], r["valor"]) for r in cur]

    if not rows:
        return {"disponivel": False}

    atual_data, atual = rows[0]
    ref = rows[5][1] if len(rows) > 5 else rows[-1][1]
    delta = atual - ref

    if atual < 80:
        zona, zona_label, zona_cor = "comprimido", "🟢 spread comprimido — farelo barato vs soja", "var(--bull)"
    elif atual < 87:
        zona, zona_label, zona_cor = "neutro", "🟡 spread neutro — sem extremo", "var(--warn)"
    else:
        zona, zona_label, zona_cor = "esticado", "🔴 spread esticado — farelo caro vs soja", "var(--bear)"

    return {
        "disponivel": True,
        "data": atual_data,
        "atual": atual,
        "delta_5d": delta,
        "zona": zona,
        "zona_label": zona_label,
        "zona_cor": zona_cor,
        "dist_77": atual - 77.0,
        "historico": rows[:14],
    }


def _get_fila_pendentes(target: date) -> int:
    """Quantos sinais pedem leitura do Claude (camada de julgamento). 0 se nada/erro."""
    try:
        import queue_emit
        return queue_emit.count_pendentes(target)
    except Exception:
        return 0


def _get_series_graficos(target: date) -> dict:
    """Séries temporais pros gráficos SVG (backfill 5y tornou isso possível).

    Tudo em ordem cronológica CRESCENTE (contrato do charts_svg.line_chart).
    """
    out = {"farelo_52s": [], "sparks": {}, "ratio": [], "cot_net_farelo": []}
    with db.connect() as conn:
        # Farelo 52 semanas (gráfico principal do Dashboard)
        rows = conn.execute(
            """
            SELECT data_referencia, valor FROM dados_publicos
            WHERE fonte='cme_cbot' AND commodity='farelo_cbot' AND metrica='fechamento'
              AND valor IS NOT NULL AND data_referencia >= date(?, '-365 days')
            ORDER BY data_referencia ASC
            """,
            (target.isoformat(),),
        ).fetchall()
        out["farelo_52s"] = [(r["data_referencia"], r["valor"]) for r in rows]

        # Sparklines dos KPIs: últimos 30 pregões por commodity
        for comm in ("farelo_cbot", "soja_cbot", "oleo_cbot"):
            rows = conn.execute(
                """
                SELECT valor FROM (
                    SELECT data_referencia, valor FROM dados_publicos
                    WHERE fonte='cme_cbot' AND commodity=? AND metrica='fechamento'
                      AND valor IS NOT NULL
                    ORDER BY data_referencia DESC LIMIT 30
                ) ORDER BY data_referencia ASC
                """,
                (comm,),
            ).fetchall()
            out["sparks"][comm] = [r["valor"] for r in rows]

        # Ratio Far/Soj (série curta — indicador existe desde mai/26)
        rows = conn.execute(
            """
            SELECT data_referencia, valor FROM dados_publicos
            WHERE fonte='indicators' AND commodity='complexo_soja'
              AND metrica='far_soj_ratio_pct' AND valor IS NOT NULL
            ORDER BY data_referencia ASC
            """
        ).fetchall()
        out["ratio"] = [(r["data_referencia"], r["valor"]) for r in rows]

        # COT: managed money net do farelo, 5 anos
        rows = conn.execute(
            """
            SELECT data_referencia, valor FROM dados_publicos
            WHERE fonte='cftc_cot' AND commodity='farelo_cbot'
              AND metrica='managed_money_net' AND valor IS NOT NULL
            ORDER BY data_referencia ASC
            """
        ).fetchall()
        out["cot_net_farelo"] = [(r["data_referencia"], r["valor"]) for r in rows]
    return out


def _get_revisoes_pendentes(target: date, janela_dias: int = 7) -> list[dict]:
    """Revisões de insight vencidas ou vencendo em até `janela_dias`.

    Cobra as datas D+7/D+90/D+180 dos insights ativos — sem cobrança visível
    o ciclo de revisão morre (caso tese_journal, abandonado em maio).
    """
    out = []
    limite = target.toordinal() + janela_dias
    for ins in ins_mod.list_insights():
        if (ins.get("status") or "").lower() not in ("ativa", "revisada"):
            continue
        for rev in ins.get("revisoes") or []:
            try:
                d_rev = date.fromisoformat(rev["data"])
            except (ValueError, TypeError):
                continue
            if d_rev.toordinal() <= limite:
                out.append({
                    "insight": ins.get("titulo") or ins["slug"],
                    "slug": ins["slug"],
                    "label": rev["label"],
                    "data": rev["data"],
                    "vencida": d_rev <= target,
                    "texto": rev.get("texto", ""),
                })
    out.sort(key=lambda r: r["data"])
    return out


def _render_revisoes(revisoes: list[dict]) -> str:
    if not revisoes:
        return ""
    itens = []
    for r in revisoes:
        badge = ('<span class="badge bear">VENCIDA</span>' if r["vencida"]
                 else '<span class="badge warn">vence em breve</span>')
        texto = f' — <span class="muted-small">{r["texto"]}</span>' if r["texto"] else ""
        itens.append(
            f'<li><strong>{r["label"]} em {r["data"]}</strong> {badge} · '
            f'{r["insight"][:80]}{texto}</li>'
        )
    return f"""
    <h2>Revisões de insight na fila <span class="tag">D+N programados</span></h2>
    <div class="card">
      <ul style="margin:0;padding-left:18px">{''.join(itens)}</ul>
      <p class="muted-small" style="margin:8px 0 0">
        Revisar = reler o insight, confrontar com o preço atual e atualizar o
        status (ativa → revisada/arquivada) no arquivo em <code>insights/</code>.
      </p>
    </div>"""


def _get_cot_posicionamento() -> dict:
    """Posição dos fundos (COT/CFTC, semanal) com percentil de ~5 anos.

    Backfill 2021-2025 feito em 2026-06-11 (283 semanas/commodity). Leitura:
    managed money em percentil extremo + preço na direção contrária = risco de
    desmonte da posição (move forte); percentil baixo = combustível de
    short-covering. Informação de contexto, não sinal isolado.
    """
    out = {"disponivel": False, "commodities": []}
    NOMES = {"farelo_cbot": "Farelo (ZM)", "oleo_cbot": "Óleo (ZL)", "soja_cbot": "Soja (ZS)"}
    with db.connect() as conn:
        for comm, nome in NOMES.items():
            rows = conn.execute(
                """
                SELECT data_referencia, valor FROM dados_publicos
                WHERE fonte='cftc_cot' AND commodity=? AND metrica='managed_money_net'
                  AND valor IS NOT NULL
                ORDER BY data_referencia DESC LIMIT 280
                """,
                (comm,),
            ).fetchall()
            if len(rows) < 8:
                continue
            atual, anterior = rows[0], rows[1]
            serie = [r["valor"] for r in rows]
            pct = 100.0 * sum(1 for v in serie if v <= atual["valor"]) / len(serie)

            oi_rows = conn.execute(
                """
                SELECT valor FROM dados_publicos
                WHERE fonte='cftc_cot' AND commodity=? AND metrica='open_interest'
                  AND valor IS NOT NULL
                ORDER BY data_referencia DESC LIMIT 5
                """,
                (comm,),
            ).fetchall()
            oi_atual = oi_rows[0]["valor"] if oi_rows else None
            oi_delta4 = (oi_rows[0]["valor"] - oi_rows[-1]["valor"]) if len(oi_rows) >= 5 else None

            out["commodities"].append({
                "nome": nome,
                "slug": comm,
                "data": atual["data_referencia"],
                "net": atual["valor"],
                "delta_sem": atual["valor"] - anterior["valor"],
                "percentil": pct,
                "n_semanas": len(serie),
                "oi": oi_atual,
                "oi_delta4": oi_delta4,
            })
    out["disponivel"] = bool(out["commodities"])
    return out


def _render_cot(cot: dict, chart_svg: str = "") -> str:
    """Card 'Posição dos fundos (COT)' — contexto semanal de posicionamento."""
    if not cot.get("disponivel"):
        return ""
    linhas = []
    leitura_farelo = ""
    for c in cot["commodities"]:
        if c["percentil"] >= 85:
            extremo = f'<span style="color:var(--bear)">p{c["percentil"]:.0f} — comprados perto do máximo histórico</span>'
        elif c["percentil"] <= 15:
            extremo = f'<span style="color:var(--bull)">p{c["percentil"]:.0f} — vendidos perto do máximo histórico</span>'
        else:
            extremo = f'p{c["percentil"]:.0f}'
        oi_txt = "—"
        if c["oi"] is not None:
            oi_txt = f'{c["oi"]/1000:.0f}k'
            if c["oi_delta4"] is not None:
                seta = "▲" if c["oi_delta4"] > 0 else "▼"
                oi_txt += f' <span class="muted-small">({seta}{abs(c["oi_delta4"])/1000:.0f}k em 4 sem)</span>'
        linhas.append(
            f'<tr><td style="text-align:left">{c["nome"]}</td>'
            f'<td class="hist-val">{c["net"]/1000:+.1f}k</td>'
            f'<td class="hist-val">{c["delta_sem"]/1000:+.1f}k</td>'
            f'<td>{extremo}</td>'
            f'<td>{oi_txt}</td></tr>'
        )
        if c["slug"] == "farelo_cbot":
            if c["percentil"] >= 85:
                leitura_farelo = ("Fundos historicamente comprados em farelo com preço perto da mínima: "
                                  "posição que não está sendo paga — desmonte (venda) empurraria o preço "
                                  "ainda mais pra baixo. Viés de preço baixista enquanto a posição não vira.")
            elif c["percentil"] <= 15:
                leitura_farelo = ("Fundos vendidos ao extremo em farelo: short-covering (recompra forçada) "
                                  "vira combustível de alta — chão pode estar próximo.")
    leitura_html = (f'<p class="muted-small" style="margin:8px 0 0">🧭 <strong>Leitura (farelo):</strong> '
                    f'{leitura_farelo}</p>') if leitura_farelo else ""
    data_ref = cot["commodities"][0]["data"]
    n_sem = cot["commodities"][0]["n_semanas"]
    return f"""
    <div class="card">
      <table class="hist-table">
        <thead><tr><th style="text-align:left">mercado</th><th>managed money net</th>
        <th>Δ semana</th><th>percentil ({n_sem} sem ≈ 5 anos)</th><th>contratos em aberto</th></tr></thead>
        <tbody>{''.join(linhas)}</tbody>
      </table>
      {leitura_html}
      {f'<div class="chart-card" style="margin-top:10px">{chart_svg}<p class="muted-small" style="margin:4px 0 0">Managed money net em FARELO — 5 anos. Acima de zero = fundos comprados.</p></div>' if chart_svg else ''}
      <p class="muted-small" style="margin:6px 0 0">
        COT (Commitments of Traders, CFTC) — posições de fundos (managed money) nos futuros,
        divulgado às sextas com dados de terça. Dado de {data_ref}. Percentil sobre o
        histórico desde 2021 (backfill público CFTC).
      </p>
    </div>"""


def _get_crush_matrix(target: date) -> dict:
    """Matriz de cenários do crush margin (Board Crush) — Soja × Far/Soj × Oil share.

    Para cada combinação calcula:
      - farelo_usd_sht: preço farelo implícito (USD/short ton)
      - oleo_cents_lb: preço óleo implícito (cents/lb)
      - crush_usd_bu: crush margin (USD/bushel)

    Convenções:
      - 1 bushel soja = 60 lb → 44 lb farelo + 11 lb óleo após esmagamento
      - 1 short ton = 2000 lb → fator 33,069 USD/bu × USD/short_ton
      - Crush = (44/2000 × farelo USD/sht) + (11/100 × óleo cts/lb) − soja USD/bu
      - Oil share = valor_óleo / (valor_óleo + valor_farelo)

    Identifica também a "célula real" (mais próxima do mercado atual) pra destacar.
    """
    SOJA_BUCKETS = [11.00, 11.50, 12.00, 12.50]  # USD/bu
    FAR_SOJ_PCTS = [0.77, 0.82, 0.87]            # relação farelo/soja
    OIL_SHARES   = [0.47, 0.50, 0.53]            # % do valor que vem do óleo

    # Convenção da indústria: 1 bushel = 60 lb nominal, 1 short ton = 2000 lb
    # → USD/bu × (2000/60) = USD/short ton equivalente soja
    BU_TO_SHT = 2000.0 / 60.0   # = 33.333
    FARELO_LB_PER_BU = 44
    OLEO_LB_PER_BU = 11

    def calcula(soja_usd_bu: float, far_pct: float, oil_share: float):
        soja_usd_sht = soja_usd_bu * BU_TO_SHT
        farelo_usd_sht = soja_usd_sht * far_pct
        farelo_value_bu = (FARELO_LB_PER_BU / 2000.0) * farelo_usd_sht
        # Oil share: valor_oleo = valor_total × oil_share; valor_farelo = total × (1-oil_share)
        # => valor_oleo = valor_farelo × oil_share / (1 - oil_share)
        oleo_value_bu = farelo_value_bu * oil_share / (1 - oil_share)
        oleo_cents_lb = oleo_value_bu * 100.0 / OLEO_LB_PER_BU
        crush_usd_bu = farelo_value_bu + oleo_value_bu - soja_usd_bu
        return {
            "farelo_usd_sht": farelo_usd_sht,
            "oleo_cents_lb": oleo_cents_lb,
            "crush_usd_bu": crush_usd_bu,
        }

    blocos = []
    for oil_share in OIL_SHARES:
        rows = []
        for soja in SOJA_BUCKETS:
            cells = []
            for far_pct in FAR_SOJ_PCTS:
                cells.append({
                    "far_pct": far_pct,
                    **calcula(soja, far_pct, oil_share),
                })
            rows.append({"soja": soja, "cells": cells})
        blocos.append({"oil_share": oil_share, "rows": rows})

    # Mercado atual: identifica célula mais próxima
    atual = {"soja_usd_bu": None, "far_pct": None, "oil_share": None, "crush_real": None}
    with db.connect() as conn:
        cur = conn.execute(
            """
            SELECT commodity, valor FROM dados_publicos
            WHERE fonte='cme_cbot' AND metrica='fechamento'
              AND commodity IN ('soja_cbot','farelo_cbot','oleo_cbot')
            GROUP BY commodity
            HAVING MAX(data_referencia)
            """
        )
        precos = {r["commodity"]: r["valor"] for r in cur}

    soja_cts = precos.get("soja_cbot")          # cents/bu
    farelo = precos.get("farelo_cbot")          # USD/short ton
    oleo = precos.get("oleo_cbot")              # cents/lb

    if soja_cts and farelo and oleo:
        soja_usd_bu_real = soja_cts / 100.0
        far_pct_real = farelo / (soja_usd_bu_real * BU_TO_SHT)
        valor_oleo = oleo * OLEO_LB_PER_BU / 100.0
        valor_farelo = farelo * FARELO_LB_PER_BU / 2000.0
        valor_total = valor_oleo + valor_farelo
        oil_share_real = valor_oleo / valor_total if valor_total else None
        crush_real = valor_oleo + valor_farelo - soja_usd_bu_real

        # Acha bucket mais proximo
        def nearest(value, options):
            return min(range(len(options)), key=lambda i: abs(options[i] - value))

        atual = {
            "soja_usd_bu": soja_usd_bu_real,
            "far_pct": far_pct_real,
            "oil_share": oil_share_real,
            "crush_real": crush_real,
            "farelo_usd_sht": farelo,
            "oleo_cents_lb": oleo,
            "i_soja": nearest(soja_usd_bu_real, SOJA_BUCKETS),
            "i_far":  nearest(far_pct_real, FAR_SOJ_PCTS),
            "i_oil":  nearest(oil_share_real, OIL_SHARES) if oil_share_real else None,
        }

    return {
        "soja_buckets": SOJA_BUCKETS,
        "far_soj_pcts": FAR_SOJ_PCTS,
        "oil_shares": OIL_SHARES,
        "blocos": blocos,
        "atual": atual,
    }


def _get_fisico_br(target: date) -> dict:
    """Latest preços físicos BR por produto × praça + prêmio vs paridade CBOT.

    Retorna dict com chave 'produtos': cada produto (soja/farelo/oleo_soja)
    tem suas praças (Rancharia + Paranaguá), paridade CBOT calculada na unidade
    certa do produto, prêmio físico − paridade, indicador suporte (se houver),
    spread Paranaguá−Rancharia, e série histórica 14d.
    """
    # Cambio USD/BRL (compartilhado entre todos os produtos)
    with db.connect() as conn:
        cur = conn.execute(
            """
            SELECT valor FROM dados_publicos
            WHERE fonte='bcb' AND commodity='usd_brl_ptax' AND metrica='valor'
            ORDER BY data_referencia DESC LIMIT 1
            """
        )
        row = cur.fetchone()
        usd_brl = row["valor"] if row else None

    # Mapeamento produto → (commodity CBOT, fator de conversão para unidade BR)
    # Já existe PARIDADES no topo do arquivo
    PRODUTO_CBOT_MAP = {
        "soja":      {"cbot": "soja_cbot",   "fator": PARIDADES["soja_cbot"]["fator"],   "unidade": "sc60kg"},
        "farelo":    {"cbot": "farelo_cbot", "fator": PARIDADES["farelo_cbot"]["fator"], "unidade": "ton"},
        "oleo_soja": {"cbot": "oleo_cbot",   "fator": PARIDADES["oleo_cbot"]["fator"],   "unidade": "ton"},
    }

    out = {"produtos": {}, "alerta_idade": False, "usd_brl": usd_brl}

    for produto_slug, meta_prod in pf.PRODUTOS_META.items():
        cbot_meta = PRODUTO_CBOT_MAP[produto_slug]
        pinfo = {
            "label": meta_prod["label"],
            "unidade": meta_prod["unidade"],
            "unidade_display": meta_prod["unidade_display"],
            "pracas": {},
            "indicador": None,
            "paridade_cbot_brl": None,
            "premio": {},     # praca_slug → prêmio (físico − paridade)
            "spread_pr_rc_brl": None,
            "basis_usd_bu_paranagua": None,  # só soja
            "serie_14d": [],
        }

        # 1. Compras (input manual) por praça
        latest_compra = pf.latest_per_praca(produto=produto_slug, tipo_posicao="compra")
        for slug, row in latest_compra.items():
            serie = pf.serie_praca(slug, produto=produto_slug, days=30, tipo_posicao="compra")
            prev = next((r for r in serie if r["data"] < row["data"]), None)
            var_brl = var_pct = None
            data_anterior = None
            if prev and prev.get("valor_brl_sc") and row.get("valor_brl_sc"):
                var_brl = row["valor_brl_sc"] - prev["valor_brl_sc"]
                var_pct = (var_brl / prev["valor_brl_sc"]) * 100
                data_anterior = prev["data"]
            try:
                data_dt = datetime.fromisoformat(row["data"]).date()
                idade = (target - data_dt).days
            except Exception:
                idade = 999

            pinfo["pracas"][slug] = {
                "nome": pf.PRACAS_PADRAO.get(slug, {}).get("nome", slug),
                "data": row["data"],
                "idade_dias": idade,
                "valor_brl": row.get("valor_brl_sc"),
                "valor_usd": row.get("valor_usd_sc"),
                "var_brl": var_brl,
                "var_pct": var_pct,
                "data_anterior": data_anterior,
                "observacao": row.get("observacao"),
                "tipo_posicao": row.get("tipo_posicao"),
            }
            if idade > 5:
                out["alerta_idade"] = True

        # 2. Indicador suporte (Paranaguá, só soja por enquanto)
        indicadores = pf.latest_per_praca(produto=produto_slug, tipo_posicao="indicador")
        ind_pr = indicadores.get("paranagua_pr")
        if ind_pr:
            pinfo["indicador"] = {
                "data": ind_pr["data"],
                "valor_brl": ind_pr["valor_brl_sc"],
                "observacao": ind_pr.get("observacao"),
            }

        # 3. Paridade CBOT na unidade do produto
        with db.connect() as conn:
            cur = conn.execute(
                """
                SELECT valor FROM dados_publicos
                WHERE fonte='cme_cbot' AND commodity=? AND metrica='fechamento'
                ORDER BY data_referencia DESC LIMIT 1
                """,
                (cbot_meta["cbot"],),
            )
            row = cur.fetchone()
            cbot_valor = row["valor"] if row else None

        if cbot_valor and usd_brl:
            paridade = cbot_valor * cbot_meta["fator"] * usd_brl
            pinfo["paridade_cbot_brl"] = paridade
            for slug, p in pinfo["pracas"].items():
                if p.get("valor_brl"):
                    pinfo["premio"][slug] = p["valor_brl"] - paridade

            # Basis técnico US$/bu — só soja (farelo/oleo medidos em US$/ton já são diretos)
            if produto_slug == "soja":
                pr = pinfo["pracas"].get("paranagua_pr", {})
                if pr.get("valor_usd"):
                    usd_bu_paranagua = pr["valor_usd"] / 2.20462
                    usd_bu_cbot = cbot_valor * 0.01
                    pinfo["basis_usd_bu_paranagua"] = usd_bu_paranagua - usd_bu_cbot

        # 4. Spread Paranaguá − Rancharia (compra)
        pr_v = pinfo["pracas"].get("paranagua_pr", {}).get("valor_brl")
        rc_v = pinfo["pracas"].get("rancharia_sp", {}).get("valor_brl")
        if pr_v and rc_v:
            pinfo["spread_pr_rc_brl"] = pr_v - rc_v

        # 4b. Cotações públicas (NAG) — comparação externa vs input manual.
        # Passa valor E data da compra PGUA: delta só vale com datas comparáveis.
        manual_pgua = pinfo["pracas"].get("paranagua_pr") or {}
        pinfo["publicas"] = _get_cotacoes_publicas(
            produto_slug, cbot_valor, usd_brl, cbot_meta["fator"],
            manual_valor=manual_pgua.get("valor_brl"),
            manual_data=manual_pgua.get("data"),
        )

        # 5. Série histórica 14 dias (data → {praca: valor})
        serie_dict = {}
        for slug in ("paranagua_pr", "rancharia_sp"):
            for r in pf.serie_praca(slug, produto_slug, days=14, tipo_posicao="compra"):
                d = r["data"]
                if d not in serie_dict:
                    serie_dict[d] = {"data": d, "paranagua": None, "rancharia": None, "spread": None}
                if slug == "paranagua_pr":
                    serie_dict[d]["paranagua"] = r["valor_brl_sc"]
                else:
                    serie_dict[d]["rancharia"] = r["valor_brl_sc"]
        for d, row in serie_dict.items():
            if row["paranagua"] and row["rancharia"]:
                row["spread"] = row["paranagua"] - row["rancharia"]
        pinfo["serie_14d"] = sorted(serie_dict.values(), key=lambda x: x["data"], reverse=True)

        out["produtos"][produto_slug] = pinfo

    return out


# Praças públicas do farelo na página NAG (slug no DB → nome de exibição)
_NAG_PRACAS_FARELO = [
    ("rs_media", "Média RS (Clicmercado)"),
    ("mt_imea", "Mato Grosso (IMEA)"),
    ("rondonopolis_mt", "Rondonópolis/MT (BCSP)"),
]


# Janela máxima (dias) entre a data da cotação pública e a data do input manual
# pra mostrar delta direto. Acima disso a comparação mistura épocas (ex: compra
# de 25/mai vs mercado de 10/jun com crash no meio) e vira aviso de atualização.
_MAX_DIAS_COMPARACAO = 3


def _get_cotacoes_publicas(produto_slug: str, cbot_valor, usd_brl, fator,
                           manual_valor=None, manual_data=None) -> list[dict]:
    """Cotações físicas públicas (fonte nag_fisico) pra comparar com o input manual.

    - farelo: 3 praças em R$/t direto + FOB Paranaguá implícito via prêmio NAG
    - óleo:   FOB Paranaguá implícito via prêmio NAG (cts/lb sobre CBOT BO)
    - soja:   nada aqui (o indicador CEPEA Paranaguá já cumpre o papel)

    FOB implícito = (CBOT + prêmio) × fator × USD/BRL — mesma conta da paridade,
    com o prêmio público no lugar do prêmio StoneX descontinuado.

    Delta vs compra: calculado SOMENTE se a compra manual tem no máximo
    _MAX_DIAS_COMPARACAO dias de defasagem vs a cotação pública. Senão o dict
    carrega `comparacao_suspensa` com a idade, e o renderer pede atualização.
    """
    out = []

    def _delta_info(data_publica: str, valor_publico: float) -> dict:
        """Delta vs compra manual, com guarda de datas comparáveis."""
        if manual_valor is None or not manual_data:
            return {}
        try:
            gap = abs((date.fromisoformat(data_publica[:10])
                       - date.fromisoformat(manual_data[:10])).days)
        except (ValueError, TypeError):
            return {}
        if gap <= _MAX_DIAS_COMPARACAO:
            return {"delta_vs_manual": valor_publico - manual_valor,
                    "gap_dias": gap, "manual_data": manual_data[:10]}
        return {"comparacao_suspensa": True, "gap_dias": gap,
                "manual_data": manual_data[:10]}

    with db.connect() as conn:
        def _ultimo(commodity, metrica):
            cur = conn.execute(
                """
                SELECT data_referencia, valor FROM dados_publicos
                WHERE fonte='nag_fisico' AND commodity=? AND metrica=?
                  AND valor IS NOT NULL
                ORDER BY data_referencia DESC LIMIT 1
                """,
                (commodity, metrica),
            )
            return cur.fetchone()

        if produto_slug == "soja":
            # Interior PR (praça real do usuário — Araucária) + spread vs porto.
            # O porto (CEPEA Paranaguá) já aparece como "indicador suporte" na
            # linha da praça; aqui entra o interior pra fechar a logística.
            interior = _ultimo("soja_parana_interior", "preco_brl_sc")
            if interior:
                item = {
                    "nome": "CEPEA Paraná interior",
                    "valor_brl": interior["valor"],
                    "data": interior["data_referencia"], "tipo": "praca",
                }
                cur2 = conn.execute(
                    """
                    SELECT valor FROM dados_publicos
                    WHERE fonte='cepea_paranagua' AND metrica='preco_suporte_brl_sc'
                      AND data_referencia=? AND valor IS NOT NULL
                    LIMIT 1
                    """,
                    (interior["data_referencia"],),
                )
                porto = cur2.fetchone()
                if porto:
                    item["spread_porto"] = porto["valor"] - interior["valor"]
                out.append(item)

        elif produto_slug == "farelo":
            for slug, nome in _NAG_PRACAS_FARELO:
                row = _ultimo("farelo_fisico_br", f"preco_brl_ton_{slug}")
                if row:
                    out.append({
                        "nome": nome, "valor_brl": row["valor"],
                        "data": row["data_referencia"], "tipo": "praca",
                    })
            premio = _ultimo("farelo_paranagua", "premio_usd_sht")
            if premio and cbot_valor and usd_brl:
                fob = (cbot_valor + premio["valor"]) * fator * usd_brl
                # Serie 14d do premio: a VIRADA dele (zero → positivo relevante)
                # e o sinal de que o export voltou a disputar o farelo = chao
                # no preco interno. Evidencia central da tese "farelo despejado".
                hist = conn.execute(
                    """
                    SELECT data_referencia, valor FROM dados_publicos
                    WHERE fonte='nag_fisico' AND commodity='farelo_paranagua'
                      AND metrica='premio_usd_sht' AND valor IS NOT NULL
                    ORDER BY data_referencia DESC LIMIT 14
                    """
                ).fetchall()
                out.append({
                    "nome": "Paridade export PGUA (CBOT+prêmio)",
                    "valor_brl": fob, "data": premio["data_referencia"],
                    "tipo": "fob_implicito", "premio": premio["valor"],
                    "premio_unidade": "US$/sht",
                    "premio_historico": [(r["data_referencia"], r["valor"]) for r in hist],
                    **_delta_info(premio["data_referencia"], fob),
                })

        elif produto_slug == "oleo_soja":
            premio = _ultimo("oleo_paranagua", "premio_cts_lb")
            if premio and cbot_valor and usd_brl:
                fob = (cbot_valor + premio["valor"]) * fator * usd_brl
                out.append({
                    "nome": "Paridade export PGUA (CBOT+prêmio)",
                    "valor_brl": fob, "data": premio["data_referencia"],
                    "tipo": "fob_implicito", "premio": premio["valor"],
                    "premio_unidade": "cts/lb",
                })
    return out


def _get_noticias_filtradas(target: date, limit: int = 8) -> list[dict]:
    """Noticias recentes filtradas apenas para soja, farelo e oleo de soja.

    Agrega qualquer fonte do tipo='noticia' (cepea_rss, noticias_agricolas, etc),
    pegando titulo, descricao e link do raw_json.
    """
    FONTE_LABEL = {
        "cepea_rss": "CEPEA",
        "noticias_rss": "RSS",
        "g1_agro": "G1 Agro",
        "canal_rural": "Canal Rural",
        "farm_progress": "FarmProgress",
    }
    out = []
    with db.connect() as conn:
        cur = conn.execute(
            """
            SELECT data_referencia, commodity, fonte, contexto, raw_json
            FROM dados_publicos
            WHERE tipo='noticia'
              AND commodity IN ('soja','farelo','oleo_soja')
              AND date(data_referencia) >= date(?, '-10 days')
            ORDER BY data_referencia DESC, id DESC
            LIMIT ?
            """,
            (target.isoformat(), limit),
        )
        for r in cur:
            ctx = r["contexto"] or ""
            titulo = ctx.split("|", 1)[0].strip() if "|" in ctx else ctx[:120]
            link = ctx.split("|", 1)[1].strip() if "|" in ctx else ""
            descricao = ""
            feed_source = None
            if r["raw_json"]:
                try:
                    j = json.loads(r["raw_json"])
                    titulo = j.get("title") or titulo
                    descricao = j.get("description") or ""
                    link = j.get("link") or link
                    feed_source = j.get("source")  # ex: g1_agro, farm_progress
                except Exception:
                    pass
            fonte_slug = feed_source or r["fonte"]
            out.append({
                "data": r["data_referencia"],
                "commodity": r["commodity"],
                "fonte": FONTE_LABEL.get(fonte_slug, fonte_slug),
                "titulo": titulo,
                "descricao": descricao,
                "link": link,
            })
    return out


def _get_eventos_proximos(target: date) -> list[dict]:
    """Lista hardcoded de eventos esperados nos proximos 14 dias."""
    eventos = [
        ("USDA Crop Progress + Export Inspections", 2, ["mon"]),  # toda segunda
        ("USDA Export Sales semanal", 2, ["thu"]),                # toda quinta
        ("CFTC COT report", 2, ["fri"]),                          # toda sexta
        ("Cattle on Feed", 1, ["last_friday_month"]),
    ]

    # Eventos fixos importantes (calendario estatico)
    eventos_fixos = [
        (date(2026, 6, 11), "WASDE Junho", 3),
        (date(2026, 6, 15), "NOPA Crush Maio", 3),
        (date(2026, 6, 30), "USDA Acreage 2026", 2),
        (date(2026, 7, 1), "B50 Indonesia entra em vigor", 3),
    ]

    out = []
    hoje = target
    fim = target + timedelta(days=14)

    # Eventos semanais (proximas 2 semanas)
    for delta in range(1, 15):
        d = hoje + timedelta(days=delta)
        wd = d.weekday()  # 0=seg, 4=sex
        if wd == 0:  # segunda
            out.append({"data": d, "nome": "USDA Crop Progress + Export Inspections", "estrelas": 2})
        elif wd == 3:  # quinta
            out.append({"data": d, "nome": "USDA Export Sales semanal", "estrelas": 1})
        elif wd == 4:  # sexta
            out.append({"data": d, "nome": "CFTC COT report", "estrelas": 2})

    # Eventos fixos
    for d, nome, estrelas in eventos_fixos:
        if hoje <= d <= fim:
            out.append({"data": d, "nome": nome, "estrelas": estrelas})

    out.sort(key=lambda x: x["data"])
    return out[:8]


def _get_tese_ativa() -> dict | None:
    """Tese viva = insight mais recente com status 'ativa' (preferindo os com vies).

    Corrigido 2026-06-11: antes lia o ultimo arquivo do tese_journal/ (fluxo
    abandonado em maio) e exibia tese de 22/mai como ativa por 3 semanas.
    """
    # 'revisada' = tese viva que recebeu correção (mesma convenção dos Drivers)
    ativos = [i for i in ins_mod.list_insights()
              if (i.get("status") or "").lower() in ("ativa", "revisada")]
    if not ativos:
        return None
    # list_insights ja ordena por data DESC; prioriza tese direcional (com vies)
    com_vies = [i for i in ativos if i.get("vies")]
    escolhido = (com_vies or ativos)[0]
    return {
        "nome": escolhido.get("titulo") or escolhido["slug"],
        "slug": escolhido["slug"],
        "arquivo": escolhido.get("arquivo", ""),
        "data": escolhido.get("data", ""),
        "vies": escolhido.get("vies") or [],
    }


# ============================================================
# Renderizacao HTML
# ============================================================

def _fmt_brl(v: float) -> str:
    return f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def _fmt_usd(v: float, decimais: int = 2) -> str:
    return f"$ {v:,.{decimais}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def _fmt_num(v: float, decimais: int = 2) -> str:
    """Numero pt-BR (virgula decimal, ponto milhar)."""
    return f"{v:,.{decimais}f}".replace(",", "X").replace(".", ",").replace("X", ".")


_MESES_PT = ["janeiro","fevereiro","março","abril","maio","junho",
             "julho","agosto","setembro","outubro","novembro","dezembro"]


def _data_pt(d: date) -> str:
    return f"{d.day} de {_MESES_PT[d.month - 1]} de {d.year}"


def _renderizar(d: dict) -> str:
    s = d["snapshot"]
    now = d["now"]
    target = d["target"]

    # === Gráficos SVG (backfill 5y) ===
    g = d.get("graficos") or {}
    niveis_cfg = _niveis_alerta()
    farelo_niveis = {}
    cfg_far = niveis_cfg.get("farelo_cbot") or {}
    if cfg_far.get("suporte"):
        farelo_niveis[f"suporte {cfg_far['suporte']:.0f}"] = cfg_far["suporte"]
    if cfg_far.get("resistencia"):
        farelo_niveis[f"resistência {cfg_far['resistencia']:.0f}"] = cfg_far["resistencia"]
    farelo52_svg = ch.line_chart(
        g.get("farelo_52s") or [], width=860, height=240,
        niveis=farelo_niveis, label_y="USD/short ton",
        fmt_valor=lambda v: f"{v:,.0f}",
    )
    ratio_svg = ch.line_chart(
        g.get("ratio") or [], width=860, height=170,
        niveis={"comprimido 80": 80.0, "esticado 87": 87.0},
        label_y="%", cor="var(--warn)",
        fmt_valor=lambda v: f"{v:.1f}",
    )
    cot_svg = ch.line_chart(
        g.get("cot_net_farelo") or [], width=860, height=190,
        niveis={"neutro 0": 0.0}, label_y="contratos (mil)",
        cor="var(--bull)",
        fmt_valor=lambda v: f"{v / 1000:+.0f}k",
    )
    sparks = {comm: ch.sparkline(vals) for comm, vals in (g.get("sparks") or {}).items()}

    # === Snapshot KPIs (farelo + ratio primeiro, no grid + sparklines) ===
    kpis_html = _render_kpis(s, d["far_soj"], sparks)
    # === Mesa do dia (camada decisória: confiança + semáforo + invalidação) ===
    mesa_html = _render_mesa_do_dia(d)
    # === O que mudou desde ontem + sinais contraditórios (camada decisória) ===
    mudou_html = _render_o_que_mudou(d["target"])
    contradicoes_html = _render_contradicoes(_gerar_contradicoes(d))
    # === Índices sintéticos (Onda 2): sobra de farelo + suporte do óleo ===
    indices_html = _render_indices_sinteticos(d["target"])
    # === Forecasts table (fail-closed: sem viés direcional se calibração ruim) ===
    _calib = [c for c in (d.get("forecast_calib") or []) if c.get("n")]
    _dir_confiavel = (min(c["dir_pct"] for c in _calib) >= 55) if _calib else True
    fcasts_html = _render_forecasts(d["forecasts"], s, _dir_confiavel)
    # === Calibracao observada dos forecasts (honestidade do modelo) ===
    calib_html = _render_forecast_calib(d["forecast_calib"])
    # === Alertas ===
    alertas_html = _render_alertas(d["alertas_tecnicos"])
    # === Revisões de insight vencendo (fila D+N) ===
    revisoes_html = _render_revisoes(d["revisoes_pendentes"])
    # === Saude das fontes (coletas_log) ===
    saude_html = _render_saude_fontes(d["saude_fontes"])
    # === Eventos ===
    eventos_html = _render_eventos(d["eventos"])
    # === Monitor Tributario/Regulatorio ===
    tributario_html = _render_tributario(d["tributario"])
    # === Noticias filtradas (soja/farelo/oleo) ===
    noticias_html = _render_noticias(d["noticias"])
    # === Mercado fisico BR (Rancharia + Paranagua) ===
    fisico_html = _render_fisico(d["fisico_br"])
    # === Ratio Far/Soj (spread farelo÷soja — leitura de trader) ===
    far_soj_html = _render_far_soj(d["far_soj"])
    # === Matriz de cenarios crush margin ===
    crush_matrix_html = _render_crush_matrix(d["crush_matrix"])
    # === Margem biodiesel americano (tese StoneX 25mai 2026) ===
    biodiesel_html = _render_biodiesel_margin(d["biodiesel_us"])
    # === Posicionamento dos fundos (COT/CFTC com percentil 5 anos) ===
    cot_html = _render_cot(d["cot"], cot_svg)
    # === Curva forward CBOT (soja/farelo/óleo - múltiplos vencimentos) ===
    curva_html = _render_curva_forward(d["curva_forward"])
    # === Insights de estudo (markdown files em insights/) ===
    insights_estudo_html = _render_insights_estudo(d["insights_estudo"])
    # === Tese ativa link ===
    tese_html = _render_tese(d["tese_ativa"])

    css = _CSS

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Commodities Radar — Daily — {target.strftime("%d/%m/%Y")}</title>
<style>{css}</style>
</head>
<body>
<div class="container">

  <header>
    <h1>🌾 Commodities Radar — Daily</h1>
    <div class="meta">
      <strong>{_data_pt(target)}</strong> · {_dia_semana_pt(target)} ·
      Snapshot gerado às {now.strftime("%H:%M")} BRT
    </div>
  </header>

  <nav class="tabs" id="tabs">
    <button class="tab-btn active" data-tab="dashboard">📊 Dashboard</button>
    <button class="tab-btn" data-tab="fisico">💰 Mercado Físico</button>
    <button class="tab-btn" data-tab="analise">🧮 Análise Quantitativa</button>
    <button class="tab-btn" data-tab="forecast">📅 Forecasts &amp; Eventos</button>
    <button class="tab-btn" data-tab="noticias">📰 Notícias &amp; Tese</button>
    <button class="tab-btn" data-tab="insights">💡 Insights</button>
  </nav>

  <!-- =============== ABA 1: DASHBOARD =============== -->
  <section class="tab-pane active" id="tab-dashboard">
    {_render_fila_banner(d.get("fila_pendentes", 0))}
    {mesa_html}
    <h2>Snapshot atual <span class="tag">último fechamento CBOT</span></h2>
    <div class="kpis">{kpis_html}</div>

    <h2>Resumo executivo <span class="tag">auto-gerado</span></h2>
    <div class="card">
      <p class="lead" id="resumo-executivo">{d["resumo_executivo"]}</p>
    </div>

    {f'<h2>O que mudou desde ontem <span class="tag">D-1 · indicadores do complexo</span></h2>{mudou_html}' if mudou_html else ''}

    {f'<h2>Sinais contraditórios <span class="tag">leitura de mesa</span></h2>{contradicoes_html}' if contradicoes_html else ''}

    <h2>Farelo CBOT — 52 semanas <span class="tag">série contínua front-month · níveis do alerta</span></h2>
    <div class="card chart-card">
      {farelo52_svg if farelo52_svg else '<p class="muted-small">Série insuficiente — rode o backfill.</p>'}
      <p class="muted-small" style="margin:6px 0 0">
        Série front-month contínua (tem salto na rolagem de contrato — boa pra nível e
        tendência, não pra retorno exato). Linhas tracejadas = níveis do <code>alerts_config</code>.
      </p>
    </div>

    <details class="card chart-card">
      <summary style="cursor:pointer"><strong>📐 Ratio Far/Soj — histórico do indicador</strong>
        <span class="muted-small">(régua: &lt;80 comprimido · 80-87 neutro · ≥87 esticado)</span></summary>
      {ratio_svg if ratio_svg else '<p class="muted-small">Série curta demais.</p>'}
    </details>

    <h2>Insights críticos <span class="tag">auto-gerado</span></h2>
    <ul class="insights">{_render_insights(d["insights"])}</ul>

    <h2>Alertas técnicos ativos</h2>
    {alertas_html}

    {revisoes_html}

    {saude_html}
  </section>

  <!-- =============== ABA 2: MERCADO FÍSICO =============== -->
  <section class="tab-pane" id="tab-fisico">
    <h2>Mercado físico BR <span class="tag">soja · farelo · óleo · input manual</span></h2>
    {fisico_html}
  </section>

  <!-- =============== ABA 3: ANÁLISE QUANTITATIVA =============== -->
  <section class="tab-pane" id="tab-analise">
    {f'<h2>Índices sintéticos <span class="tag">sobra de farelo · suporte do óleo · contagem de condições</span></h2>{indices_html}' if indices_html else ''}

    <h2>Ratio Farelo/Soja <span class="tag">spread farelo÷soja · mean-reversion</span></h2>
    {far_soj_html}

    <h2>Matriz de cenários — Crush margin <span class="tag">stress test soja × farelo × óleo</span></h2>
    {crush_matrix_html}

    <h2>Curva forward CBOT <span class="tag">próximos vencimentos · contango/backwardation</span></h2>
    {curva_html}

    <h2>Margem biodiesel americano <span class="tag">driver atual do óleo soja CBOT</span></h2>
    {biodiesel_html}

    <h2>Posição dos fundos — COT <span class="tag">semanal · percentil desde 2021</span></h2>
    {cot_html}

    <h2>Drivers ativos por commodity <span class="tag">auto-gerado · dados + tributário + insights</span></h2>
    {_render_drivers_por_produto(d["drivers"])}
  </section>

  <!-- =============== ABA 4: FORECASTS & EVENTOS =============== -->
  <section class="tab-pane" id="tab-forecast">
    <h2>Forecast 7d / 30d <span class="tag">bandas estatísticas MA20+vol</span></h2>
    <div class="card" style="padding:6px 14px 14px">{fcasts_html}{calib_html}</div>

    <h2>Eventos calendarizados — próximos 14 dias</h2>
    <div class="card">{eventos_html}</div>

    <h2>Monitor Tributário/Regulatório <span class="tag">vetores fiscais · soja/farelo/óleo</span></h2>
    {tributario_html}
  </section>

  <!-- =============== ABA 6: INSIGHTS DE ESTUDO =============== -->
  <section class="tab-pane" id="tab-insights">
    <h2>Insights de estudo <span class="tag">resumos executivos · mais recente primeiro</span></h2>
    {insights_estudo_html}
  </section>

  <!-- =============== ABA 5: NOTÍCIAS & TESE =============== -->
  <section class="tab-pane" id="tab-noticias">
    <h2>Notícias recentes <span class="tag">soja · farelo · óleo de soja</span></h2>
    <div class="card">{noticias_html}</div>

    <h2>Perguntas pra hoje</h2>
    <div class="card">
      <ul class="questions">
        <li>
          <div class="check"></div>
          <div>
            <strong>O que a StoneX está dizendo no WhatsApp hoje?</strong><br>
            <span class="muted-small">Verifica na comunidade oficial. Se houver post relevante, copia em <code>shared/from_consultor/insights/</code>.</span>
          </div>
        </li>
        <li>
          <div class="check"></div>
          <div>
            <strong>Algo novo do consultor pela call/WhatsApp?</strong><br>
            <span class="muted-small">Registrar em <code>shared/from_consultor/notas_call/</code>.</span>
          </div>
        </li>
        <li>
          <div class="check"></div>
          <div>
            <strong>Forecasts vencendo essa semana?</strong><br>
            <span class="muted-small">Sistema auto-avalia conforme <code>data_alvo</code> chega — ver <code>python main.py forecast --resolve</code>.</span>
          </div>
        </li>
        {tese_html}
      </ul>
    </div>
  </section>

  <footer>
    Gerado por <strong>Commodities Radar</strong> · pipeline rodando seg-sex 07:00 e 22:00<br>
    Dados: CME · BCB · CFTC · USDA WASDE/NASS · ABIOVE · CEPEA RSS · NOAA · Inmet · MPOB · StoneX (corporativo)<br>
    Para refinar seções narrativas: abra Claude Code, peça síntese deste HTML.
  </footer>

</div>
<script>
// Sistema de abas com persistência via localStorage + URL hash
(function() {{
  const STORAGE_KEY = 'radar_active_tab';
  const tabs = document.querySelectorAll('.tab-btn');
  const panes = document.querySelectorAll('.tab-pane');

  function activate(tabName) {{
    if (!tabName) return;
    tabs.forEach(t => t.classList.toggle('active', t.dataset.tab === tabName));
    panes.forEach(p => p.classList.toggle('active', p.id === 'tab-' + tabName));
    try {{ localStorage.setItem(STORAGE_KEY, tabName); }} catch (e) {{}}
    if (location.hash !== '#' + tabName) {{
      history.replaceState(null, '', '#' + tabName);
    }}
    // Scroll suave pro topo da aba
    window.scrollTo({{ top: 0, behavior: 'smooth' }});
  }}

  // Click handlers
  tabs.forEach(t => t.addEventListener('click', () => activate(t.dataset.tab)));

  // Decide aba inicial: hash da URL > localStorage > default 'dashboard'
  let initial = 'dashboard';
  const hash = (location.hash || '').replace('#', '');
  const valid = ['dashboard', 'fisico', 'analise', 'forecast', 'noticias', 'insights'];
  if (valid.includes(hash)) {{
    initial = hash;
  }} else {{
    try {{
      const stored = localStorage.getItem(STORAGE_KEY);
      if (valid.includes(stored)) initial = stored;
    }} catch (e) {{}}
  }}
  activate(initial);

  // Listener pra mudança de hash (botões voltar/avançar do browser)
  window.addEventListener('hashchange', () => {{
    const h = (location.hash || '').replace('#', '');
    if (valid.includes(h)) activate(h);
  }});

  // Atalhos de teclado: 1-6 troca de aba
  document.addEventListener('keydown', (e) => {{
    if (e.target.matches('input, textarea')) return;
    const n = parseInt(e.key, 10);
    if (n >= 1 && n <= 6) activate(valid[n - 1]);
  }});
}})();
</script>
</body>
</html>
"""


def _render_insights(insights: list[dict]) -> str:
    if not insights:
        return '<li><em>Sem insights gerados.</em></li>'
    items = []
    for i in insights:
        klass = i.get("tipo", "neutral")
        icon = i.get("icon", "•")
        items.append(f'<li class="{klass}"><span class="icon">{icon}</span>{i["texto"]}</li>')
    return "\n".join(items)


_FONTE_DRIVER_ICON = {"dado": "📊", "tributario": "⚖️", "insight": "💡"}


def _render_drivers(drivers: list[dict]) -> str:
    if not drivers:
        return '<li><em>Sem drivers identificados.</em></li>'
    items = []
    for dr in drivers:
        horizon = dr.get("horizon", "")
        horizon_html = f' <span class="horizon">{horizon}</span>' if horizon else ""
        icon = _FONTE_DRIVER_ICON.get(dr.get("fonte", ""), "")
        icon_html = f'<span title="fonte: {dr.get("fonte", "")}">{icon}</span> ' if icon else ""
        items.append(f'<li>{icon_html}{dr["texto"]}{horizon_html}</li>')
    return "\n".join(items)


def _render_drivers_por_produto(drivers: dict) -> str:
    """Um bloco por commodity, cada um com colunas bull/bear."""
    blocos = []
    for slug, label in _DRIVER_PRODUTOS:
        grupo = drivers.get(slug) or {}
        bull = grupo.get("bull") or []
        bear = grupo.get("bear") or []
        if not bull and not bear:
            continue
        blocos.append(f"""
      <div class="produto-card">
        <h3>{label}</h3>
        <div class="two-col drivers">
          <div class="card bull">
            <h3>↗ Bullish (alta)</h3>
            <ul>{_render_drivers(bull)}</ul>
          </div>
          <div class="card bear">
            <h3>↘ Bearish (queda)</h3>
            <ul>{_render_drivers(bear)}</ul>
          </div>
        </div>
      </div>""")
    legenda = ('<p class="muted-small" style="margin-top:4px">'
               '📊 regra sobre dados · ⚖️ Monitor Tributário · 💡 insight ativo com '
               '<code>vies:</code> no frontmatter — tudo recalculado a cada synth, nada hard-coded.</p>')
    return f'<div class="card">{"".join(blocos)}{legenda}</div>'


def _kpi_change_line(info: dict, fmt_delta, cor_direcao: bool = True) -> str:
    """Linha 'change' do KPI: variação D-1 com seta + range/percentil 52 semanas.

    cor_direcao=True (padrão): cor = DIREÇÃO do preço (subiu=verde, caiu=vermelho),
    convenção de mercado — sem julgamento de 'bom/ruim'. Igual pra toda commodity,
    porque o trader opera os dois lados (long e short).
    """
    partes = []
    if info.get("delta") is not None:
        d, dp = info["delta"], info.get("delta_pct", 0.0)
        seta = "▼" if d < 0 else ("▲" if d > 0 else "•")
        if cor_direcao and d != 0:
            cor = "var(--bull)" if d > 0 else "var(--bear)"
            partes.append(f'<span style="color:{cor}">{seta} {fmt_delta(abs(d))} ({dp:+.1f}%)</span>')
        else:
            partes.append(f"{seta} {fmt_delta(abs(d))} ({dp:+.1f}%)")
    if info.get("min52") is not None:
        partes.append(
            f'52s: {fmt_delta(info["min52"])}–{fmt_delta(info["max52"])} '
            f'· p{info["pct52"]:.0f}'
        )
    return " · ".join(partes) if partes else f'fechamento {info.get("data", "")}'


def _render_fila_banner(n: int) -> str:
    """Gatilho da camada de julgamento: avisa que há sinais pedindo leitura do Claude."""
    if not n:
        return ""
    plural = "leitura pendente" if n == 1 else "leituras pendentes"
    return f"""
    <div class="card" style="border-left:3px solid var(--accent);background:rgba(59,130,246,0.10);margin-bottom:16px">
      <strong>🔔 {n} {plural}</strong> — sinais que pedem interpretação.
      <span class="muted-small">Abra o Claude no projeto e diga
      <em>"lê a fila de julgamento e trata"</em> (ou rode <code>main.py queue</code> pra ver).
      A leitura vira insight e atualiza os Drivers.</span>
    </div>"""


def _render_kpis(s: dict, far_soj: dict | None = None, sparks: dict | None = None) -> str:
    """KPIs do complexo: farelo + ratio Far/Soj primeiro (o spread que o trader
    acompanha de perto), depois soja/óleo/crush, e contexto semanal
    (oil share/CFTC/plantio) por último. A cor da variação = direção do preço
    (subiu=verde, caiu=vermelho). sparks = SVGs de 30 pregões por commodity."""
    cards = []
    niveis = _niveis_alerta()
    sparks = sparks or {}

    def _spark(comm):
        svg = sparks.get(comm) or ""
        return f'<div class="spark">{svg}</div>' if svg else ""

    # 1. FARELO — tint neutro (como as demais); a cor vai na variação, por direção
    if "farelo_cbot" in s:
        farelo = s["farelo_cbot"]
        brl_html = ""
        if "brl" in farelo:
            brl_html = f'<div class="brl">{_fmt_brl(farelo["brl"])}/ton</div>'
        cards.append(f"""
        <div class="kpi neutral">
          <div class="label">Farelo CBOT (ZM)</div>
          <div class="value">{_fmt_usd(farelo["valor"])}<span class="unit">/short ton</span></div>
          {brl_html}
          <div class="change">{_kpi_change_line(farelo, lambda v: _fmt_num(v, 2))}</div>
          {_spark("farelo_cbot")}
        </div>""")

    # 2. RATIO FAR/SOJ (spread farelo÷soja — cor pela zona do spread)
    if far_soj and far_soj.get("disponivel"):
        fs = far_soj
        zona_klass = {"comprimido": "bull", "neutro": "warn", "esticado": "bear"}.get(fs["zona"], "neutral")
        delta_txt = ""
        if fs.get("delta_5d") is not None:
            seta = "▼" if fs["delta_5d"] < 0 else "▲"
            delta_txt = f"{seta} {abs(fs['delta_5d']):.1f}pp em 5 pregões · "
        cards.append(f"""
        <div class="kpi {zona_klass}">
          <div class="label">Ratio Far/Soj</div>
          <div class="value">{_fmt_num(fs["atual"], 1)}<span class="unit"> %</span></div>
          <div class="change">{delta_txt}{fs["zona_label"]}</div>
        </div>""")

    # 3. Soja
    if "soja_cbot" in s:
        soja = s["soja_cbot"]
        brl_html = ""
        if "brl" in soja:
            brl_html = f'<div class="brl">{_fmt_brl(soja["brl"])}/sc</div>'
        cards.append(f"""
        <div class="kpi neutral">
          <div class="label">Soja CBOT (ZS)</div>
          <div class="value">{_fmt_usd(soja["valor"]/100)}<span class="unit">/bu</span></div>
          {brl_html}
          <div class="change">{_kpi_change_line(soja, lambda v: _fmt_num(v / 100, 2))}</div>
          {_spark("soja_cbot")}
        </div>""")

    # 4. Óleo — suporte vem do alerts_config (não mais hard-coded)
    if "oleo_cbot" in s:
        oleo = s["oleo_cbot"]
        brl_html = ""
        if "brl" in oleo:
            brl_html = f'<div class="brl">{_fmt_brl(oleo["brl"])}/ton</div>'
        sup_oleo = (niveis.get("oleo_cbot") or {}).get("suporte", 72.0)
        klass = "bear" if oleo["valor"] < sup_oleo * 1.05 else "neutral"
        cards.append(f"""
        <div class="kpi {klass}">
          <div class="label">Óleo CBOT (ZL)</div>
          <div class="value">{_fmt_num(oleo["valor"], 2)}<span class="unit"> cts/lb</span></div>
          {brl_html}
          <div class="change">{_kpi_change_line(oleo, lambda v: _fmt_num(v, 2))}</div>
          {_spark("oleo_cbot")}
        </div>""")

    # 5. Crush margin — níveis lidos do alerts_config.toml (fim do "$2,00" fixo)
    if "crush_margin" in s and s["crush_margin"]:
        cm = s["crush_margin"]
        cfg_cm = niveis.get("complexo_soja") or {}
        sup, res = cfg_cm.get("suporte", 2.5), cfg_cm.get("resistencia", 4.25)
        if cm["valor"] > res:
            klass, warn_text = "warn", f"⚠ acima de {_fmt_usd(res)} — expansão além do recorde"
        elif cm["valor"] < sup:
            klass, warn_text = "warn", f"⚠ abaixo de {_fmt_usd(sup)} — esmagadora tira o pé"
        else:
            klass = "neutral"
            warn_text = f"zona gorda histórica (alerta: <{_fmt_usd(sup)} ou >{_fmt_usd(res)})"
        brl_html = ""
        if "brl_ton" in cm:
            brl_html = f'<div class="brl">{_fmt_brl(cm["brl_ton"])}/ton</div>'
        cards.append(f"""
        <div class="kpi {klass}">
          <div class="label">Crush margin</div>
          <div class="value">{_fmt_usd(cm["valor"])}<span class="unit">/bu</span></div>
          {brl_html}
          <div class="change">{warn_text}</div>
        </div>""")

    # 6. USD/BRL
    if s.get("usd_brl"):
        cards.append(f"""
        <div class="kpi neutral">
          <div class="label">USD/BRL PTAX</div>
          <div class="value">{_fmt_num(s["usd_brl"]["valor"], 4)}</div>
          <div class="change">data {s["usd_brl"]["data"]}</div>
        </div>""")

    # === Contexto semanal (não muda a leitura do dia) ===
    if s.get("oil_share"):
        cards.append(f"""
        <div class="kpi neutral">
          <div class="label">Oil share <span class="unit">(contexto)</span></div>
          <div class="value">{_fmt_num(s["oil_share"]["valor"], 1)}<span class="unit"> %</span></div>
          <div class="change">vs média histórica 33% — óleo paga o crush</div>
        </div>""")

    if s.get("cftc_net"):
        cftc = s["cftc_net"]
        delta_str = ""
        if "delta_pct" in cftc:
            sign = "+" if cftc["delta_pct"] >= 0 else ""
            delta_str = f" — {sign}{_fmt_num(cftc['delta_pct'], 1)}% vs semana anterior"
        cards.append(f"""
        <div class="kpi neutral">
          <div class="label">CFTC net long soja <span class="unit">(semanal)</span></div>
          <div class="value">{cftc["valor"]/1000:.0f}k<span class="unit"> contratos</span></div>
          <div class="change">{cftc["data"]}{delta_str}</div>
        </div>""")

    if s.get("plantio_soja_eua"):
        p = s["plantio_soja_eua"]
        cards.append(f"""
        <div class="kpi neutral">
          <div class="label">Plantio soja EUA <span class="unit">(semanal)</span></div>
          <div class="value">{p["valor"]:.0f}<span class="unit"> %</span></div>
          <div class="change">semana {p["data"]}</div>
        </div>""")

    return "\n".join(cards)


def _render_forecasts(forecasts: list[dict], snapshot: dict, dir_confiavel: bool = True) -> str:
    if not forecasts:
        return "<p>Sem forecasts ativos. Rode <code>python main.py forecast</code>.</p>"

    # Agrupar por commodity
    por_commodity = {}
    for f in forecasts:
        por_commodity.setdefault(f["commodity"], {})[f["horizonte_dias"]] = f

    rows = []
    nomes = {
        "soja_cbot": "Soja CBOT",
        "farelo_cbot": "Farelo CBOT",
        "oleo_cbot": "Óleo CBOT",
    }

    for commodity in ["soja_cbot", "farelo_cbot", "oleo_cbot"]:
        if commodity not in por_commodity:
            continue
        f7 = por_commodity[commodity].get(7)
        f30 = por_commodity[commodity].get(30)
        if not f7 or not f30:
            continue

        # Spot do snapshot
        spot_val = snapshot.get(commodity, {}).get("valor", 0)
        if commodity == "soja_cbot":
            spot_str = _fmt_usd(spot_val / 100)
        elif commodity == "oleo_cbot":
            spot_str = f"{spot_val:.2f} cts"
        else:
            spot_str = _fmt_usd(spot_val)

        # Bandas
        def _band(f, comm):
            if comm == "soja_cbot":
                return f"<span class=\"lo\">{_fmt_usd(f['valor_baixo']/100)}</span> <span class=\"mid\">{_fmt_usd(f['valor_central']/100)}</span> <span class=\"hi\">{_fmt_usd(f['valor_alto']/100)}</span>"
            elif comm == "oleo_cbot":
                return f"<span class=\"lo\">{f['valor_baixo']:.2f}</span> <span class=\"mid\">{f['valor_central']:.2f}</span> <span class=\"hi\">{f['valor_alto']:.2f}</span>"
            else:
                return f"<span class=\"lo\">{_fmt_usd(f['valor_baixo'])}</span> <span class=\"mid\">{_fmt_usd(f['valor_central'])}</span> <span class=\"hi\">{_fmt_usd(f['valor_alto'])}</span>"

        vies = f7["vies"]
        if dir_confiavel:
            badge_klass = "bull" if vies == "altista" else ("bear" if vies == "baixista" else "neutral")
            badge_html = f'<span class="badge {badge_klass}">{vies}</span>'
        else:
            # Fail-closed: acerto direcional do modelo baixo -> nao destaca direcao, so range.
            badge_html = '<span class="badge neutral" title="calibração direcional baixa — use só o range">só range</span>'

        rows.append(f"""
        <tr>
          <td class="commodity">{nomes[commodity]}</td>
          <td class="band">{spot_str}</td>
          <td class="band">{_band(f7, commodity)}</td>
          <td class="band">{_band(f30, commodity)}</td>
          <td>{badge_html}</td>
        </tr>""")

    return f"""
    <table>
      <thead>
        <tr>
          <th>Commodity</th><th>Spot</th><th>7d</th><th>30d</th><th>Viés</th>
        </tr>
      </thead>
      <tbody>{"".join(rows)}</tbody>
    </table>
    """


def _render_alertas(alertas: list[dict]) -> str:
    if not alertas:
        return '<div class="card"><p>Sem alertas técnicos no momento.</p></div>'

    items = []
    for a in alertas:
        tipo = a.get("tipo", "alerta").replace("_", " ")
        label = a.get("label") or a.get("commodity", "")
        # Mensagem humana: valor e nivel formatados quando disponiveis
        if a.get("valor_atual") is not None and a.get("nivel") is not None:
            direcao = "abaixo do suporte" if a.get("tipo") == "quebra_suporte" else "acima da resistência"
            corpo = f"{label} fechou em <strong>{_fmt_num(a['valor_atual'], 2)}</strong> — {direcao} {_fmt_num(a['nivel'], 2)}"
        elif a.get("delta_pct") is not None:
            corpo = f"{label} variou <strong>{a['delta_pct']:+.2f}%</strong> no dia"
        else:
            corpo = a.get("msg", "")
        lente_html = ""
        if a.get("lente_texto"):
            cls = a.get("lente_classe", "neutral")
            icone = "🟢" if cls == "bull" else ("🔴" if cls == "bear" else "⚪")
            lente_html = (f'<br><span class="muted-small">{icone} Leitura: '
                          f'{a["lente_texto"]}</span>')
        items.append(f"""
        <div class="card alert">
          <p style="margin:0"><strong>🚨 {tipo.upper()}</strong> — {corpo}{lente_html}</p>
        </div>""")
    return "\n".join(items)


_ESTADO_FONTE_STYLE = {
    "ok":         ("●", "var(--bull)"),
    "atrasada":   ("●", "var(--warn)"),
    "erro":       ("●", "var(--bear)"),
    "desativada": ("○", "#777"),
}


def _render_saude_fontes(fontes: list[dict]) -> str:
    """Mini-card de saúde dos coletores: última execução vs cadência esperada."""
    if not fontes:
        return ""

    problemas = [f for f in fontes if f["estado"] in ("atrasada", "erro")]
    linhas = []
    for f in fontes:
        dot, cor = _ESTADO_FONTE_STYLE.get(f["estado"], ("●", "#777"))
        dias_txt = f"{f['dias']}d atrás" if f["dias"] is not None else "—"
        detalhe = ""
        if f["estado"] == "atrasada":
            detalhe = f' <span class="muted-small">(esperado a cada ~{f["cadencia"]}d)</span>'
        elif f["estado"] == "erro" and f["erro"]:
            detalhe = f' <span class="muted-small">{f["erro"]}</span>'
        linhas.append(
            f'<tr><td><span style="color:{cor}">{dot}</span> {f["fonte"]}</td>'
            f'<td>{f["ultima"]}</td><td>{dias_txt}</td>'
            f'<td>{f["registros"] if f["registros"] is not None else "—"}{detalhe}</td></tr>'
        )

    resumo = ("✅ todas as fontes dentro da cadência esperada" if not problemas else
              f'⚠️ <strong>{len(problemas)} fonte(s) fora da cadência:</strong> '
              + ", ".join(f["fonte"] for f in problemas)
              + " — veja se o run <code>daily</code> rodou no GitHub Actions "
                "(ou se a fonte mudou de cadência/quebrou)")

    return f"""
    <details class="card">
      <summary style="cursor:pointer"><strong>🩺 Saúde das fontes</strong>
        <span class="muted-small">{resumo}</span></summary>
      <table class="hist-table" style="margin-top:10px">
        <thead><tr><th style="text-align:left">fonte</th><th>última coleta</th>
        <th>há quanto</th><th>salvos</th></tr></thead>
        <tbody>{"".join(linhas)}</tbody>
      </table>
      <p class="muted-small" style="margin:8px 0 0">
        Baseado em <code>coletas_log</code> (quando o coletor rodou), não em
        <code>data_referencia</code> (que tem projeções futuras, ex. ABIOVE).
        Fontes semanais/mensais não acusam atraso dentro da cadência própria.
      </p>
    </details>"""


def _render_forecast_calib(calib: list[dict]) -> str:
    """Linha de honestidade do modelo: cobertura observada das bandas vs teórica."""
    if not calib:
        return ""
    partes = []
    for c in calib:
        if not c["n"]:
            continue
        partes.append(
            f"banda {c['horizonte']}d: <strong>{c['banda_pct']:.0f}%</strong> "
            f"(n={c['n']}) · direção {c['dir_pct']:.0f}%"
        )
    if not partes:
        return ""
    horizontes_sem = [h for h in (7, 30) if h not in {c["horizonte"] for c in calib}]
    extra = f" · {'/'.join(str(h) + 'd' for h in horizontes_sem)}: sem resolvidos ainda" if horizontes_sem else ""
    return f"""
    <p class="muted-small" style="margin-top:8px">
      📐 <strong>Calibração observada</strong> (vs ~87% teórica da banda z=1.5):
      {" · ".join(partes)}{extra}.
      Hit baixo = bandas subestimam quebras de regime (ex.: crash de 04/jun) —
      use as bandas como referência de range calmo, não como limite de risco.
    </p>"""


def _render_tributario(t: dict) -> str:
    """Card do Monitor Tributário/Regulatório, agrupado por jurisdição."""
    if not t.get("disponivel"):
        return ('<div class="card"><p class="muted-small">Sem eventos no monitor. '
                'Rode <code>main.py tributario sync</code>.</p></div>')

    # Paleta do TEMA DARK (corrigido 2026-06-11: a versão original usava cores
    # de tema claro — fundo #fafafa, badges pastel — e o título ficava cinza
    # claro sobre branco, ilegível). Tudo via CSS vars do :root agora.
    STATUS_STYLE = {
        "vigente":     ("em vigor", "var(--bull)", "var(--bull-bg)"),
        "tramitacao":  ("tramitando", "var(--accent)", "rgba(59,130,246,0.15)"),
        "adiado":      ("adiado", "var(--bear)", "var(--bear-bg)"),
        "monitorando": ("monitorando", "var(--warn)", "var(--warn-bg)"),
        "encerrado":   ("encerrado", "var(--muted)", "var(--surface2)"),
    }
    DIR_STYLE = {
        "alta":   ("▲ altista", "var(--bear)"),
        "baixa":  ("▼ baixista", "var(--bull)"),
        "misto":  ("◆ misto", "var(--warn)"),
        "neutro": ("● neutro", "var(--neutral)"),
    }

    r = t["resumo"]
    resumo_html = (
        f'<div class="muted-small" style="margin-bottom:12px;">'
        f'<strong>{r["total"]}</strong> vetores sob vigilância · '
        f'<span style="color:var(--bear);">▲ {r.get("alta",0)} altistas</span> · '
        f'<span style="color:var(--bull);">▼ {r.get("baixa",0)} baixistas</span> · '
        f'<span style="color:var(--warn);">◆ {r.get("misto",0)} mistos</span> · '
        f'<span style="color:var(--neutral);">● {r.get("neutro",0)} neutros</span> '
        f'<br><em>altista/baixista = efeito esperado no preço do complexo. O trader lê os dois '
        f'lados: alta favorece quem está comprado, baixa quem está vendido.</em></div>'
    )

    grupos_html = []
    for g in t["grupos"]:
        itens = []
        for e in g["eventos"]:
            st_label, st_cor, st_bg = STATUS_STYLE.get(
                e.get("status"), (e.get("status", ""), "var(--muted)", "var(--surface2)"))
            dir_label, dir_cor = DIR_STYLE.get(
                e.get("direcao"), (e.get("direcao", ""), "var(--neutral)"))
            impacto = e.get("impacto", "")
            produtos = (e.get("produtos") or "").replace(",", " · ")
            venc = e.get("vigencia_ate")
            venc_html = f' · <span class="muted-small">vence {venc}</span>' if venc else ""
            marco = e.get("proximo_marco") or ""
            marco_data = e.get("proximo_data")
            marco_data_html = f" ({marco_data})" if marco_data else ""
            marco_html = (f'<div class="muted-small" style="margin-top:4px;">⏭ <strong>próximo:</strong> '
                          f'{marco}{marco_data_html}</div>') if marco else ""
            fonte = e.get("fonte_url") or ""
            fonte_html = f' · <a href="{fonte}" target="_blank">fonte</a>' if fonte else ""
            itens.append(f"""
            <div style="border-left:3px solid {dir_cor};padding:10px 14px;margin-bottom:10px;background:var(--surface2);border-radius:0 8px 8px 0;">
              <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap;">
                <span style="background:{st_bg};color:{st_cor};font-size:0.72em;font-weight:700;padding:2px 8px;border-radius:6px;text-transform:uppercase;letter-spacing:.3px;">{st_label}</span>
                <span style="color:{dir_cor};font-weight:600;font-size:0.8em;">{dir_label}</span>
                <span class="muted-small">{impacto} · {produtos}</span>
              </div>
              <div style="font-weight:600;margin:6px 0 3px;color:var(--text);">{e.get("titulo","")}</div>
              <div class="muted-small">{e.get("mecanismo","")}</div>
              {marco_html}
              <div class="muted-small" style="margin-top:3px;">{venc_html}{fonte_html}</div>
            </div>""")
        grupos_html.append(
            f'<h4 style="margin:14px 0 8px;">{g["label"]}</h4>{"".join(itens)}'
        )

    return f"""
    <div class="card">
      {resumo_html}
      {"".join(grupos_html)}
      <p class="muted-small" style="margin-top:10px;">Catálogo curado em
      <code>system/tributario_watch.toml</code> · atualizar:
      <code>main.py tributario sync</code></p>
    </div>
    """


def _render_eventos(eventos: list[dict]) -> str:
    if not eventos:
        return "<p>Sem eventos nos próximos 14 dias.</p>"

    items = []
    for e in eventos:
        d = e["data"]
        if isinstance(d, date):
            dia = d.strftime("%a %d/%m")
        else:
            dia = str(d)
        estrelas = "★" * e.get("estrelas", 1)
        items.append(f"""
        <li>
          <span class="date">{dia}</span>
          <span class="name">{e["nome"]}</span>
          <span class="stars">{estrelas}</span>
        </li>""")
    return f'<ul class="events">{"".join(items)}</ul>'


def _render_insights_estudo(insights: list[dict]) -> str:
    """Lista cards de insights ordenados por data DESC."""
    if not insights:
        return """
        <div class="card">
          <p>Nenhum insight de estudo ainda.</p>
          <p class="muted-small">
            Crie um novo: <code>python main.py insight new "Título do insight"</code><br>
            Ou adicione um arquivo .md na pasta <code>insights/</code> (ver convenção em <code>insights/README.md</code>).
          </p>
        </div>"""

    STATUS_BADGE = {
        "ativa": '<span class="badge bull">ativa</span>',
        "revisada": '<span class="badge neutral">revisada</span>',
        "arquivada": '<span class="badge bear">arquivada</span>',
    }

    cards = []
    for i in insights:
        # Idade do insight
        idade = ""
        if i.get("data_dt"):
            dias = (date.today() - i["data_dt"]).days
            if dias == 0:
                idade = '<span class="badge bull">hoje</span>'
            elif dias == 1:
                idade = '<span class="badge neutral">ontem</span>'
            elif dias < 7:
                idade = f'<span class="badge neutral">há {dias}d</span>'
            elif dias < 30:
                idade = f'<span class="badge neutral">há {dias//7}sem</span>'
            else:
                idade = f'<span class="muted-small">há {dias//30}m</span>'

        # Tags como pills
        tags_html = ""
        if i["tags"]:
            tags_html = " ".join(
                f'<span class="insight-tag">{t}</span>' for t in i["tags"]
            )

        # Resumo executivo como lista
        if i["resumo"]:
            resumo_items = "".join(f"<li>{r}</li>" for r in i["resumo"])
            resumo_html = f'<ul class="insight-resumo">{resumo_items}</ul>'
        else:
            resumo_html = '<p class="muted-small">(sem resumo executivo no .md)</p>'

        # Próximas ações pendentes
        acoes_html = ""
        pendentes = [a for a in i["proximas_acoes"] if not a["done"]]
        if pendentes:
            acoes_items = "".join(
                f'<li>☐ {a["texto"]}</li>' for a in pendentes[:4]
            )
            extra = f" (+{len(pendentes)-4})" if len(pendentes) > 4 else ""
            acoes_html = f"""
            <details class="insight-acoes">
              <summary>📋 {len(pendentes)} ação(ões) pendente(s){extra}</summary>
              <ul>{acoes_items}</ul>
            </details>"""

        # Fontes
        fontes_html = ""
        if i["fontes"]:
            fontes_str = " · ".join(i["fontes"][:3])
            extra = f" (+{len(i['fontes'])-3})" if len(i["fontes"]) > 3 else ""
            fontes_html = f'<div class="muted-small" style="margin-top:8px">📚 {fontes_str}{extra}</div>'

        status_html = STATUS_BADGE.get(i["status"], i["status"])
        arquivo_rel = Path(i["arquivo"]).name

        cards.append(f"""
        <article class="insight-card">
          <header class="insight-head">
            <div class="insight-meta">
              <span class="insight-date">{i["data"] or '—'}</span>
              {idade}
              {status_html}
            </div>
            <h3 class="insight-title">{i["titulo"]}</h3>
            <div class="insight-tags">{tags_html}</div>
          </header>
          {resumo_html}
          {acoes_html}
          {fontes_html}
          <div class="muted-small" style="margin-top:10px;font-family:monospace;font-size:11px">
            📄 <code>{arquivo_rel}</code> ·
            abrir: <code>python main.py insight open {Path(i["arquivo"]).stem}</code>
          </div>
        </article>""")

    return f"""
    <p class="muted-small">
      Resumos executivos de estudos pessoais. Cada insight é um arquivo .md em
      <code>insights/</code> com lifecycle (criação, revisão D+90/D+180, arquivamento).
      Mais recente primeiro.
    </p>
    <div class="insight-list">{"".join(cards)}</div>
    <p class="muted-small" style="margin-top:14px">
      Criar novo: <code>python main.py insight new "Título do insight"</code> ·
      Listar: <code>python main.py insight list</code> ·
      Abrir: <code>python main.py insight open &lt;slug&gt;</code>
    </p>"""


def _render_curva_forward(curva: dict) -> str:
    """4 fontes: CBOT real + StoneX manual + Claude heurístico + Média ponderada.

    Cada commodity vira sub-bloco com tabela mostrando os 4 valores por vencimento
    e os deltas % vs CBOT real. Divergências fortes (>3%) ganham badge de alerta.
    """
    PRODUTOS_META = {
        "soja_cbot": {"label": "Soja em grão", "unidade": "cts/bu", "fmt": ",.2f"},
        "farelo_cbot": {"label": "Farelo de soja", "unidade": "USD/sht", "fmt": ",.2f"},
        "oleo_cbot": {"label": "Óleo de soja", "unidade": "cts/lb", "fmt": ",.2f"},
    }
    pesos = curva.get("_pesos", {"cbot": 0.5, "stonex": 0.3, "claude": 0.2})

    def _fmt_val(v, fmt):
        if v is None:
            return '<span class="muted-small">—</span>'
        return f"{v:{fmt}}"

    def _fmt_delta(d):
        if d is None:
            return ""
        cls = "bull" if d > 0 else ("bear" if d < 0 else "neutral")
        sinal = "+" if d > 0 else ""
        return f'<span class="badge {cls}" style="font-size:10px">{sinal}{d:.1f}%</span>'

    blocos = []
    for commodity, meta in PRODUTOS_META.items():
        vencs = curva.get(commodity, [])
        if not vencs:
            blocos.append(f"""
            <div class="curva-block">
              <h3>{meta['label']} <span class="muted-small">({meta['unidade']})</span></h3>
              <p class="muted-small">Sem dados forward CBOT.</p>
            </div>""")
            continue

        # Conta presença StoneX/Claude pra mostrar avisos
        has_stonex = any(v["stonex"] is not None for v in vencs)
        has_claude = any(v["claude"] is not None for v in vencs)

        avisos = []
        if not has_stonex:
            avisos.append('<span class="muted-small">⚠ StoneX vazio — input via <code>main.py curva set stonex</code></span>')
        if not has_claude:
            avisos.append('<span class="muted-small">⚠ Claude vazio — rode <code>main.py curva generate</code></span>')

        rows = []
        for v in vencs:
            stonex_cell = f'{_fmt_val(v["stonex"], meta["fmt"])} {_fmt_delta(v["stonex_delta_pct"])}'
            claude_cell = f'{_fmt_val(v["claude"], meta["fmt"])} {_fmt_delta(v["claude_delta_pct"])}'

            # Razões da Claude num title (tooltip nativo)
            razoes = v.get("claude_razoes") or []
            if razoes and v["claude"] is not None:
                title = " | ".join(razoes[:3])
                claude_cell = f'<span title="{title}" style="cursor:help">{claude_cell}</span>'

            rows.append(
                f'<tr>'
                f'<td class="hist-date">{v["codigo"]}</td>'
                f'<td class="hist-date muted-small">{v["label"]}</td>'
                f'<td class="hist-val">{_fmt_val(v["cbot"], meta["fmt"])}</td>'
                f'<td class="hist-val">{stonex_cell}</td>'
                f'<td class="hist-val">{claude_cell}</td>'
                f'<td class="hist-val" style="background:rgba(255,255,255,0.03)">{_fmt_val(v["media"], meta["fmt"])}</td>'
                f'</tr>'
            )

        avisos_html = " &nbsp;·&nbsp; ".join(avisos)
        avisos_block = f'<div style="margin:4px 0 8px">{avisos_html}</div>' if avisos else ""

        # Spread de calendário (estrutura da curva CBOT real) — o termômetro de
        # escassez que uma mesa lê antes do preço absoluto. Inversão (curto acima
        # do longo) = mercado pagando pra ter AGORA = aperto; carry = folga.
        spreads_block = ""
        com_cbot = [v for v in vencs if v.get("cbot") is not None]
        if len(com_cbot) >= 2:
            front, ultimo = com_cbot[0], com_cbot[-1]
            sp_total = ultimo["cbot"] - front["cbot"]
            sp_pct = sp_total / front["cbot"] * 100 if front["cbot"] else 0
            if sp_pct <= -0.8:
                estrutura, cor_e = "INVERSÃO — mercado paga pra ter agora (aperto no curto prazo)", "var(--bear)"
            elif sp_pct >= 0.8:
                estrutura, cor_e = "CARRY — diferido mais caro (mercado folgado, sem prêmio por pressa)", "var(--bull)"
            else:
                estrutura, cor_e = "FLAT — curva sem sinal de aperto nem carrego relevante", "var(--muted)"
            sp_prox = ""
            if len(com_cbot) >= 3:
                v2 = com_cbot[1]
                sp_prox = (f' · {front["codigo"]}→{v2["codigo"]}: '
                           f'{v2["cbot"] - front["cbot"]:+.2f}')
            # Mini-barras dos spreads consecutivos (visualiza o desenho da curva)
            barras = ""
            if len(com_cbot) >= 3:
                items = [(f'{a["codigo"]}→{b["codigo"]}', b["cbot"] - a["cbot"])
                         for a, b in zip(com_cbot, com_cbot[1:])]
                barras_svg = ch.bar_spread(items, width=300,
                                           height=18 * len(items) + 12)
                if barras_svg:
                    barras = f'<div style="margin-top:4px">{barras_svg}</div>'
            spreads_block = (
                f'<p class="muted-small" style="margin:6px 0 0">📐 <strong>Estrutura:</strong> '
                f'{front["codigo"]}→{ultimo["codigo"]}: {sp_total:+.2f} {meta["unidade"]} '
                f'({sp_pct:+.1f}%){sp_prox} — <span style="color:{cor_e}">{estrutura}</span></p>'
                f'{barras}'
            )

        blocos.append(f"""
        <div class="curva-block-wide">
          <div class="curva-head">
            <h3>{meta['label']} <span class="muted-small">({meta['unidade']})</span></h3>
          </div>
          {avisos_block}
          <table class="hist-table curva-table-4">
            <thead>
              <tr>
                <th>Venc</th>
                <th>Mês</th>
                <th title="Cotação real CBOT (Yahoo Finance)">CBOT real</th>
                <th title="Curva indicativa do consultor StoneX (input manual)">StoneX</th>
                <th title="Heurística automática auditável — não recomendação">Claude</th>
                <th title="Média ponderada: CBOT 50% + StoneX 30% + Claude 20%">Média</th>
              </tr>
            </thead>
            <tbody>{"".join(rows)}</tbody>
          </table>
          {spreads_block}
        </div>""")

    pesos_str = (f"CBOT <strong>{pesos['cbot']*100:.0f}%</strong> · "
                 f"StoneX <strong>{pesos['stonex']*100:.0f}%</strong> · "
                 f"Claude <strong>{pesos['claude']*100:.0f}%</strong>")

    return f"""
    <div class="card">
      <p class="muted-small">
        Comparação de 4 leituras da curva forward: <strong>CBOT real</strong> (mercado, objetivo) ·
        <strong>StoneX</strong> (consultor, opinião do especialista) ·
        <strong>Claude</strong> (heurística automática auditável, NÃO recomendação) ·
        <strong>Média ponderada</strong> ({pesos_str}). Δ% mostra divergência vs CBOT.
        Passe o mouse sobre o valor Claude pra ver as razões da heurística.
      </p>
      <div class="curva-grid-4">{"".join(blocos)}</div>
      <p class="muted-small" style="margin-top:10px">
        ⚠ <strong>Curva Claude é modelo heurístico em <code>system/claude_forecast.py</code></strong> —
        regras explícitas auditáveis. Não substitui análise profissional do consultor.
        Atualizar StoneX: <code>python main.py curva set stonex --produto X --venc Y --valor Z</code>.
      </p>
    </div>"""


def _render_biodiesel_margin(b: dict) -> str:
    """Card 'Margem biodiesel americano' — decomposição + sensibilidades + alerta."""
    if b.get("margem") is None:
        return """
        <div class="card">
          <p>Margem biodiesel indisponível — falta Heating Oil ou óleo soja recente.</p>
          <p class="muted-small">Pra gravar/atualizar RIN D4:
          <code>python main.py param set rin_d4 2.11 --fonte "StoneX 28mai"</code></p>
        </div>"""

    margem = b["margem"]
    cls = "bull" if margem >= 1.5 else ("bear" if margem < 0.5 else "neutral")
    alerta_cls, alerta_msg = b.get("alerta") or ("neutral", "")

    # Sensibilidades
    sens_rows = []
    for s in b["sensibilidade"]:
        nm = s["novo_margem"]
        d_v = s["delta"]
        cls_d = "bull" if d_v > 0 else ("bear" if d_v < -0.3 else "neutral")
        cls_m = "bull" if nm >= 1.5 else ("bear" if nm < 0.5 else "neutral")
        sinal = "+" if d_v > 0 else ""
        sens_rows.append(
            f'<tr>'
            f'<td>{s["input"]}</td>'
            f'<td><span class="badge {cls_d}">{sinal}${d_v:.2f}</span></td>'
            f'<td><span class="badge {cls_m}">${nm:.2f}/gal</span></td>'
            f'</tr>'
        )

    # Notas sobre params
    rin_p = b["rin_d4"]
    custo_p = b["custo_industrial"]
    rin_note = ""
    if rin_p:
        tag = "[DEFAULT]" if rin_p.get("is_default") else f"[{rin_p.get('fonte','manual')}]"
        rin_note = f' <span class="muted-small">{tag}</span>'

    return f"""
    <div class="card">
      <p class="muted-small">
        Tese StoneX 25mai 2026: o que sustenta o preço do óleo soja CBOT hoje é a margem
        do biodiesel americano via demanda RIN. Se margem cair, esmagamento reduz e óleo cai.
        Conta: <strong>receita (HO + 1,5×RIN) − custo (7,5×óleo + custo industrial)</strong>.
      </p>

      <div class="bio-grid">
        <div class="bio-block">
          <div class="bio-label">Margem atual</div>
          <div class="bio-margem badge {cls}">${margem:+.2f}/gal</div>
          <div class="muted-small">{b['data']}</div>
        </div>
        <div class="bio-block">
          <div class="bio-label">Receita</div>
          <div class="bio-val">${b['receita']:.2f}/gal</div>
          <div class="muted-small">HO ${b['ho_chicago']:.2f} + 1,5×RIN ${rin_p['valor']:.2f}{rin_note}</div>
        </div>
        <div class="bio-block">
          <div class="bio-label">Custo total</div>
          <div class="bio-val">${b['custo_total']:.2f}/gal</div>
          <div class="muted-small">óleo ${b['custo_oleo']:.2f} + industrial ${custo_p['valor']:.2f}</div>
        </div>
      </div>

      <div class="bio-alerta bio-{alerta_cls}">{alerta_msg}</div>

      <details class="fisico-serie">
        <summary>🎯 Sensibilidade — o que move a margem?</summary>
        <table class="hist-table">
          <thead><tr><th>Cenário</th><th>Impacto</th><th>Margem resultante</th></tr></thead>
          <tbody>{"".join(sens_rows)}</tbody>
        </table>
        <p class="muted-small" style="margin:8px 4px 0">
          Atualizar premissas: <code>python main.py param set rin_d4 X --fonte "StoneX YYMMM"</code> ·
          <code>python main.py param list</code>
        </p>
      </details>
    </div>"""


def _render_far_soj(fs: dict) -> str:
    """Card do ratio Far/Soj: valor atual, zona, tendência, escala visual, histórico."""
    if not fs.get("disponivel"):
        return ('<div class="card"><p class="muted-small">Sem dados de ratio Far/Soj '
                '(faltam preços CBOT de soja+farelo). Rode <code>main.py indicators</code>.</p></div>')

    atual = fs["atual"]
    delta = fs["delta_5d"]
    lo, hi = 72.0, 90.0
    pos = max(0.0, min(100.0, (atual - lo) / (hi - lo) * 100))
    w_v = (80 - lo) / (hi - lo) * 100
    w_a = (87 - 80) / (hi - lo) * 100
    w_r = (hi - 87) / (hi - lo) * 100

    # spread far÷soj: cor por direção do ratio (caindo=verde/comprimindo, subindo=vermelho)
    if delta < -0.05:
        seta, dcor, dtxt = "↓", "var(--bull)", "spread comprimindo (farelo cede vs soja)"
    elif delta > 0.05:
        seta, dcor, dtxt = "↑", "var(--bear)", "spread esticando (farelo ganha de soja)"
    else:
        seta, dcor, dtxt = "→", "#888", "estável"

    if fs["zona"] == "comprimido":
        interp = ("<strong>Spread comprimido</strong>: farelo barato vs soja. Mean-reversion favorece a "
                  "convergência — leitura clássica de <strong>long farelo / short soja</strong> (ou crush "
                  "comprado). Risco: o spread pode comprimir ainda mais se o óleo seguir dominando o crush.")
    elif fs["zona"] == "neutro":
        interp = (f"<strong>Spread neutro</strong> — sem extremo de valor. Falta <strong>{fs['dist_77']:.1f} pp</strong> "
                  f"pra zona comprimida (&lt;80%). Sem assimetria clara de mean-reversion; operar por "
                  f"momentum/nível em vez do spread.")
    else:
        interp = ("<strong>Spread esticado</strong>: farelo caro vs soja. Mean-reversion favorece o lado "
                  "inverso — <strong>short farelo / long soja</strong> (ou crush vendido).")

    hist_rows = "".join(
        f"<tr><td>{d}</td><td style='text-align:right'>{v:.2f}%</td></tr>"
        for d, v in fs["historico"]
    )

    return f"""
    <div class="card">
      <div style="display:flex;align-items:baseline;gap:18px;flex-wrap:wrap;">
        <div style="font-size:2.6em;font-weight:700;line-height:1;">{atual:.1f}%</div>
        <div>
          <div style="font-weight:600;color:{fs['zona_cor']};">{fs['zona_label']}</div>
          <div class="muted-small" style="color:{dcor};">{seta} {delta:+.2f} pp em ~5 pregões — {dtxt}</div>
        </div>
      </div>

      <div style="position:relative;margin:26px 0 40px;">
        <div style="display:flex;height:26px;border-radius:5px;overflow:hidden;font-size:0.72em;font-weight:600;">
          <span style="width:{w_v:.1f}%;background:rgba(16,185,129,0.22);color:#6ee7b7;display:flex;align-items:center;justify-content:center;">&lt;80 comprimido</span>
          <span style="width:{w_a:.1f}%;background:rgba(245,158,11,0.20);color:#fcd34d;display:flex;align-items:center;justify-content:center;">80–87 neutro</span>
          <span style="width:{w_r:.1f}%;background:rgba(239,68,68,0.20);color:#fca5a5;display:flex;align-items:center;justify-content:center;">≥87 esticado</span>
        </div>
        <div style="position:absolute;left:{pos:.1f}%;top:-4px;transform:translateX(-50%);text-align:center;">
          <div style="font-size:1.1em;line-height:1;">▼</div>
          <div style="font-size:0.74em;font-weight:700;white-space:nowrap;">atual {atual:.1f}%</div>
        </div>
      </div>

      <p class="muted-small">{interp}</p>

      <details>
        <summary>Histórico ({len(fs['historico'])} pregões)</summary>
        <table style="width:auto;font-size:0.85em;margin-top:8px;">
          <thead><tr><th>Data</th><th style="text-align:right">Far/Soj</th></tr></thead>
          <tbody>{hist_rows}</tbody>
        </table>
      </details>

      <p class="muted-small" style="margin-top:10px;">Convenção: farelo (USD/short ton) ÷ (soja USD/bu × 33,33) —
      mesma da matriz crush abaixo. Leitura de spread: ratio baixo = farelo barato vs soja, alto = caro;
      mean-reversion vale nos dois sentidos.</p>
    </div>
    """


def _render_crush_matrix(m: dict) -> str:
    """Matriz 3 oil shares × 4 sojas × 3 far_pcts = 36 células de crush margin.

    Cores: verde >2.5, amarelo 1-2.5, vermelho <1.
    Célula real do mercado destacada com borda.
    """
    if not m or not m.get("blocos"):
        return '<div class="card"><p>Matriz indisponível — falta cotação CBOT recente.</p></div>'

    atual = m.get("atual", {})
    i_oil_real = atual.get("i_oil")
    i_soja_real = atual.get("i_soja")
    i_far_real = atual.get("i_far")

    bloco_principal_html = ""   # bloco do oil share atual do mercado
    blocos_alternativos = []    # os 2 outros oil shares (cenários hipotéticos)
    for bi, bloco in enumerate(m["blocos"]):
        oil_share = bloco["oil_share"]
        oil_pct = int(round(oil_share * 100))
        # Label do oilshare
        if oil_pct <= 47:
            oil_tag = "óleo desvalorizado"
        elif oil_pct >= 53:
            oil_tag = "óleo valorizado (biodiesel forte)"
        else:
            oil_tag = "equilíbrio histórico"

        # Tabela: header com 3 far_pcts, linhas = 4 sojas
        header_cells = "".join(
            f'<th class="crush-h">{int(p*100)}%</th>' for p in m["far_soj_pcts"]
        )
        rows_html = []
        for ri, row in enumerate(bloco["rows"]):
            cells_html = []
            for ci, cell in enumerate(row["cells"]):
                crush = cell["crush_usd_bu"]
                oleo = cell["oleo_cents_lb"]
                # Cor por faixa
                if crush >= 2.5:
                    cls = "crush-green"
                elif crush >= 1.0:
                    cls = "crush-yellow"
                else:
                    cls = "crush-red"
                # Destaque célula real
                marker = ""
                if (bi == i_oil_real and ri == i_soja_real and ci == i_far_real):
                    cls += " crush-real"
                    marker = '<div class="crush-marker">● mercado atual</div>'
                farelo_sht = cell["farelo_usd_sht"]
                cells_html.append(
                    f'<td class="crush-cell {cls}">'
                    f'<div class="crush-val">{crush:+.2f}</div>'
                    f'<div class="crush-sub">óleo {oleo:.1f}¢/lb</div>'
                    f'<div class="crush-sub">farelo ${farelo_sht:.0f}/sht</div>'
                    f'{marker}'
                    f'</td>'
                )
            soja_label = f"{row['soja']:.2f}"
            quebra_tag = ' <span class="crush-sub">(Quebra EUA)</span>' if row["soja"] >= 12.5 else ""
            rows_html.append(
                f'<tr><th class="crush-row-h">Soja ${soja_label}{quebra_tag}</th>{"".join(cells_html)}</tr>'
            )

        bloco_html_str = f"""
        <div class="crush-block">
          <h3>Oil share {oil_pct}% <span class="muted-small">— {oil_tag}</span></h3>
          <table class="crush-table">
            <thead>
              <tr>
                <th class="crush-corner">Soja \\ Far÷Soj</th>
                {header_cells}
              </tr>
            </thead>
            <tbody>{"".join(rows_html)}</tbody>
          </table>
        </div>"""
        if bi == i_oil_real:
            bloco_principal_html = bloco_html_str
        else:
            blocos_alternativos.append(bloco_html_str)

    # Se nao identificou oil share do mercado (sem CBOT), mostra os 3
    if not bloco_principal_html:
        bloco_principal_html = "".join([bloco_principal_html] + blocos_alternativos)
        blocos_alternativos = []

    # Detalhes colapsáveis pros outros 2 oil shares (cenários alternativos)
    cenarios_alt_html = ""
    if blocos_alternativos:
        cenarios_alt_html = f"""
        <details class="fisico-serie">
          <summary>🔬 Ver outros cenários de oil share — stress test "e se?"</summary>
          {"".join(blocos_alternativos)}
        </details>"""

    # Sumário do mercado atual
    atual_html = ""
    if atual.get("soja_usd_bu"):
        atual_html = f"""
        <div class="crush-real-info">
          <strong>Mercado atual:</strong>
          Soja <strong>${atual['soja_usd_bu']:.2f}/bu</strong> ·
          Farelo <strong>${atual['farelo_usd_sht']:.1f}/sht</strong> ·
          Óleo <strong>{atual['oleo_cents_lb']:.1f}¢/lb</strong> ·
          Far/Soj <strong>{atual['far_pct']*100:.1f}%</strong> ·
          Oil share <strong>{atual['oil_share']*100:.1f}%</strong> ·
          Crush real <strong>${atual['crush_real']:+.2f}/bu</strong>
        </div>"""

    # ============================================================
    # Bloco dedicado FARELO (Soja × Far÷Soj, independente de oil share)
    # Replica a tabela superior da planilha StoneX.
    # Cor por NÍVEL de preço do farelo (não é lente de comprador):
    #   verde = farelo barato em termos absolutos / vermelho = caro
    # ============================================================
    far_header = "".join(f'<th class="crush-h">{int(p*100)}%</th>' for p in m["far_soj_pcts"])
    far_rows = []
    # Pega o farelo de qualquer um dos blocos (não depende de oil share)
    bloco_qq = m["blocos"][0]
    for ri, row in enumerate(bloco_qq["rows"]):
        far_cells = []
        for ci, cell in enumerate(row["cells"]):
            farelo = cell["farelo_usd_sht"]
            # Cor por nível de preço absoluto do farelo
            if farelo < 290:
                cls_f = "crush-green"
            elif farelo < 310:
                cls_f = "crush-yellow"
            else:
                cls_f = "crush-red"
            marker_f = ""
            if ri == i_soja_real and ci == i_far_real:
                cls_f += " crush-real"
                marker_f = '<div class="crush-marker">● mercado atual</div>'
            far_cells.append(
                f'<td class="crush-cell {cls_f}">'
                f'<div class="crush-val">${farelo:.0f}</div>'
                f'<div class="crush-sub">USD/sht ton</div>'
                f'{marker_f}'
                f'</td>'
            )
        soja_label = f"{row['soja']:.2f}"
        quebra_tag = ' <span class="crush-sub">(Quebra EUA)</span>' if row["soja"] >= 12.5 else ""
        far_rows.append(
            f'<tr><th class="crush-row-h">Soja ${soja_label}{quebra_tag}</th>{"".join(far_cells)}</tr>'
        )
    farelo_bloco_html = f"""
        <div class="crush-block">
          <h3>Farelo implícito ÷ Soja (US$/short ton)
            <span class="muted-small">— preço do farelo dado o preço da soja e a relação far÷soj</span>
          </h3>
          <table class="crush-table">
            <thead>
              <tr>
                <th class="crush-corner">Soja \\ Far÷Soj</th>
                {far_header}
              </tr>
            </thead>
            <tbody>{"".join(far_rows)}</tbody>
          </table>
          <p class="muted-small" style="margin:6px 4px 0">
            Independe de oil share (só depende de soja × ratio far÷soj). Cor por
            <strong>nível de preço do farelo</strong>:
            <span class="badge bull">verde &lt;$290</span> barato ·
            <span class="badge neutral">amarelo $290-310</span> intermediário ·
            <span class="badge bear">vermelho ≥$310</span> caro.
          </p>
        </div>"""

    return f"""
    <div class="card">
      <p class="muted-small">
        Stress test do <strong>crush margin</strong> (board crush USDA: 44 lb farelo + 11 lb óleo
        por bushel) sob 3 eixos: <strong>preço soja CBOT</strong>, <strong>relação farelo÷soja</strong>
        (&lt;80% farelo abundante, ≥87% apertado) e <strong>oil share</strong> (% do valor do crush
        vindo do óleo). Cor: <span class="badge bull">verde ≥$2.5</span>
        <span class="badge neutral">amarelo $1-2.5</span>
        <span class="badge bear">vermelho &lt;$1</span>.
      </p>
      {atual_html}
      <div class="crush-grid">
        {farelo_bloco_html}
        {bloco_principal_html}
      </div>
      {cenarios_alt_html}
      <p class="muted-small" style="margin-top:10px">
        Use a matriz pra: (1) decidir quando esmagar ou reduzir turno;
        (2) ver pra onde o crush migra se sua tese se confirmar;
        (3) calcular preço-alvo do óleo dado outras premissas.
      </p>
    </div>"""


def _render_fisico(fisico: dict) -> str:
    """3 sub-cards (1 por produto): cada um com Rancharia + Paranaguá + prêmio CBOT."""
    produtos = fisico.get("produtos") or {}
    if not produtos:
        return """
        <div class="card">
          <p>Nenhum preço físico ainda — use <code>python main.py fisico add</code> pra inputar.</p>
        </div>"""

    alerta_html = ""
    if fisico.get("alerta_idade"):
        idades = [info.get("idade_dias", 0)
                  for pr in produtos.values()
                  for info in (pr.get("pracas") or {}).values()
                  if isinstance(info.get("idade_dias"), int) and info["idade_dias"] < 900]
        pior = max(idades) if idades else 0
        alerta_html = f"""
        <div class="muted-small" style="margin-top:8px;color:var(--warn)">
          ⚠ Seus inputs manuais têm até <strong>{pior} dias</strong> — acima de 3 dias os
          deltas vs mercado ficam suspensos (comparar épocas diferentes engana).
          Atualize via <code>python main.py fisico add</code> (atalho "Input Fisico" no Desktop).
        </div>"""

    cards = []
    for produto_slug, pinfo in produtos.items():
        cards.append(_render_fisico_produto(produto_slug, pinfo))

    return f"""
    <div class="card">
      {''.join(cards)}
      {alerta_html}
      <p class="muted-small" style="margin-top:14px">
        Auditoria: <code>python main.py fisico historico</code> ·
        Export CSV: <code>python main.py fisico export [--historico]</code> ·
        Inputar: <code>python main.py fisico add</code> (atalho "Input Fisico" no Desktop)
      </p>
    </div>"""


def _render_fisico_produto(slug: str, p: dict) -> str:
    """Sub-card de 1 produto (soja, farelo, óleo)."""
    label = p["label"]
    unidade = p["unidade_display"]   # ex: 'R$/sc 60kg' ou 'R$/tonelada'
    # Sufixo curto pra exibir após valores: '/sc' ou '/t'
    sufixo = "/sc" if p["unidade"] == "sc60kg" else "/t"

    pracas = p.get("pracas") or {}
    has_any = bool(pracas)
    if not has_any and p.get("indicador") is None:
        return f"""
        <div class="produto-card">
          <h3>{label} <span class="muted-small">— {unidade}</span></h3>
          <p class="muted-small">Sem registro. Input: <code>python main.py fisico add --produto {slug}</code></p>
        </div>"""

    # Render cada praça (ordem: Paranaguá primeiro, depois Rancharia)
    rows_html = []
    for praca_slug in ("paranagua_pr", "rancharia_sp"):
        info = pracas.get(praca_slug)
        if not info or info.get("valor_brl") is None:
            rows_html.append(f"""
            <div class="fisico-row" style="opacity:0.55">
              <div class="fisico-head">
                <span class="fisico-praca">{pf.PRACAS_PADRAO.get(praca_slug, {}).get('nome', praca_slug)}</span>
                <span class="muted-small">sem registro</span>
              </div>
              <div class="fisico-valor muted-small">—</div>
            </div>""")
            continue

        idade = info["idade_dias"]
        if idade == 0:
            idade_badge = '<span class="badge bull">hoje</span>'
        elif idade == 1:
            idade_badge = '<span class="badge neutral">D-1</span>'
        elif idade <= 3:
            idade_badge = f'<span class="badge neutral">D-{idade}</span>'
        else:
            # Âmbar (warn) = problema de QUALIDADE DE DADO (input velho), não
            # sinal de mercado — vermelho fica reservado pra movimento de preço
            idade_badge = f'<span class="badge warn">D-{idade} ⚠ dado velho</span>'

        brl_fmt = _fmt_brl(info["valor_brl"])
        usd_part = ""
        if info.get("valor_usd"):
            unidade_usd = "/sc" if p["unidade"] == "sc60kg" else "/t"
            usd_part = f' <span class="muted-small">US$ {info["valor_usd"]:,.2f}{unidade_usd}</span>'

        var_html = ""
        if info.get("var_brl") is not None:
            v = info["var_brl"]; vp = info["var_pct"]
            cls = "bull" if v > 0 else ("bear" if v < 0 else "neutral")
            sinal = "+" if v > 0 else ""
            var_html = (
                f'<span class="badge {cls}">{sinal}R$ {v:,.2f} '
                f'({sinal}{vp:.1f}%) vs {info["data_anterior"]}</span>'
            )

        # Nota: removida a linha "Prêmio físico vs CBOT" em R$/unidade.
        # Métrica confusa porque (a) inclui efeito câmbio, (b) não é como o mercado
        # expressa prêmio (cents/bu pra soja, USD/sht pra farelo, cents/lb pra óleo),
        # e (c) gera números absurdos pra óleo (CBOT descolado do físico mundial).
        # O prêmio público (NAG Paranaguá) entra no bloco "Cotações públicas" abaixo,
        # na unidade nativa do mercado (US$/sht farelo, cts/lb óleo).

        obs_html = ""
        if info.get("observacao"):
            obs_html = f'<div class="muted-small" style="margin-top:4px">📝 {info["observacao"]}</div>'

        # Indicador suporte CEPEA — só no card de Paranaguá quando houver
        indicador_html = ""
        if praca_slug == "paranagua_pr":
            ind = p.get("indicador")
            if ind and ind.get("valor_brl") is not None:
                ind_brl = ind["valor_brl"]
                diff_html = ""
                if info.get("valor_brl"):
                    diff = info["valor_brl"] - ind_brl
                    # Referência de preço (não vantagem de compra): badge neutro,
                    # só posiciona seu físico vs o indicador CEPEA.
                    rotulo = "abaixo" if diff < 0 else ("acima" if diff > 0 else "igual a")
                    diff_html = (
                        f' <span class="badge neutral">seu físico {_fmt_brl(abs(diff))}{sufixo} '
                        f'{rotulo} do indicador</span>'
                    )
                indicador_html = (
                    f'<div class="fisico-indicador">'
                    f'<span class="muted-small">📊 <strong>Indicador suporte CEPEA</strong> ({ind["data"]}):</span> '
                    f'<span class="hist-val">{_fmt_brl(ind_brl)}{sufixo}</span>'
                    f'{diff_html}'
                    f'</div>'
                )

        rows_html.append(f"""
        <div class="fisico-row">
          <div class="fisico-head">
            <span class="fisico-praca">{info["nome"]}</span>
            <span class="muted-small">compra · {info["data"]}</span>
            {idade_badge}
          </div>
          <div class="fisico-valor">{brl_fmt}<span class="muted-small">{sufixo}</span>{usd_part}</div>
          <div class="fisico-var">{var_html}</div>
          {obs_html}
          {indicador_html}
        </div>""")

    # Bloco "Cotações públicas" — referências de mercado (NAG) com data em toda
    # linha. Delta vs compra SÓ quando as datas são comparáveis (<=3 dias de gap);
    # compra velha vs mercado de hoje mistura épocas e engana (lição de 11/jun:
    # compra de 25/mai vs FOB de 10/jun com crash de 04/jun no meio).
    publicas = p.get("publicas") or []
    publicas_html = ""
    if publicas:
        linhas_pub = []
        notas = []
        for q in publicas:
            extra = ""
            if q.get("spread_porto") is not None:
                sp = q["spread_porto"]
                extra = (f'<span class="muted-small">porto PGUA {"+" if sp >= 0 else "−"}'
                         f'{_fmt_brl(abs(sp))}{sufixo} vs interior (custo logístico)</span>')
            elif q.get("tipo") == "fob_implicito":
                sinal_p = "+" if q["premio"] >= 0 else ""
                extra = (f'<span class="muted-small">prêmio {sinal_p}{q["premio"]:.2f} '
                         f'{q["premio_unidade"]} s/ CBOT</span>')
                # Spread export × interno (só farelo; óleo é descolado do interno).
                # Cor por DIREÇÃO do preço interno: export acima = puxa pra cima (bull).
                if slug == "farelo":
                    if q.get("delta_vs_manual") is not None:
                        dv = q["delta_vs_manual"]
                        cls_dv = "bull" if dv > 0 else "bear"
                        sinal_dv = "+" if dv > 0 else "−"
                        rotulo = ("export acima do interno — puxa preço"
                                  if dv > 0 else "export abaixo do interno — oferta sobra dentro")
                        extra += (f' <span class="badge {cls_dv}">{sinal_dv}{_fmt_brl(abs(dv))}{sufixo} '
                                  f'vs seu físico ({q.get("manual_data", "?")}) · {rotulo}</span>')
                    elif q.get("comparacao_suspensa"):
                        notas.append(
                            f'⚠️ <strong>Comparação suspensa:</strong> seu físico PGUA é de '
                            f'{q.get("manual_data", "?")} ({q.get("gap_dias", "?")} dias antes '
                            f'desta cotação) — mercado mexeu no meio. Atualize via '
                            f'<code>main.py fisico add</code> (atalho "Input Fisico") '
                            f'pra reativar o delta.')
                elif slug == "oleo_soja":
                    notas.append(
                        'Paridade export = (CBOT+prêmio)×câmbio — é a referência pra quem '
                        'opera óleo CBOT/export. O degomado interno opera descolado: são dois '
                        'mercados, não confundir um com o outro.')
            linhas_pub.append(
                f'<tr><td style="text-align:left">{q["nome"]}</td>'
                f'<td class="hist-val">{_fmt_brl(q["valor_brl"])}{sufixo}</td>'
                f'<td class="muted-small">{q["data"]}</td><td>{extra}</td></tr>'
            )
        notas_html = "".join(f'<p class="muted-small" style="margin:6px 0 0">{n}</p>'
                             for n in notas)
        # Histórico do prêmio export (a virada = gatilho de chão no interno)
        premio_hist_html = ""
        fob_q = next((q for q in publicas if q.get("premio_historico")), None)
        if fob_q and len(fob_q["premio_historico"]) >= 2:
            linhas_h = "".join(
                f'<tr><td class="hist-date">{dt}</td>'
                f'<td class="hist-val">{v:+.2f}</td></tr>'
                for dt, v in fob_q["premio_historico"]
            )
            premio_hist_html = f"""
          <details class="fisico-serie">
            <summary>📈 Prêmio export PGUA — {len(fob_q["premio_historico"])} fechamento(s)
              <span class="muted-small">(virada pra positivo relevante = export volta a disputar = chão no interno)</span></summary>
            <table class="hist-table">
              <thead><tr><th>data</th><th>{fob_q["premio_unidade"]} s/ CBOT</th></tr></thead>
              <tbody>{linhas_h}</tbody>
            </table>
          </details>"""
        publicas_html = f"""
        <div class="fisico-serie">
          <span class="muted-small">🌐 <strong>Referências de mercado</strong> (Notícias Agrícolas, auto)</span>
          <table class="hist-table" style="margin-top:6px">
            <thead><tr><th style="text-align:left">referência</th><th>valor</th>
            <th>fechamento</th><th></th></tr></thead>
            <tbody>{''.join(linhas_pub)}</tbody>
          </table>
          {notas_html}
          {premio_hist_html}
        </div>"""

    # Linha de rodapé: paridade CBOT + spread + basis us$/bu (só soja)
    rodape_parts = []
    if p.get("paridade_cbot_brl") is not None:
        rodape_parts.append(
            f'<strong>Paridade CBOT:</strong> {_fmt_brl(p["paridade_cbot_brl"])}{sufixo}'
        )
    if p.get("spread_pr_rc_brl") is not None:
        s = p["spread_pr_rc_brl"]
        sinal = "+" if s > 0 else ""
        # Sem badge de cor: spread entre praças é informação de logística,
        # não é sinal de preço por si só
        rodape_parts.append(
            f'<strong>Spread PR−Rancharia:</strong> '
            f'<span class="hist-val">{sinal}{_fmt_brl(abs(s)) if s >= 0 else "−" + _fmt_brl(abs(s))}{sufixo}</span>'
        )
    if p.get("basis_usd_bu_paranagua") is not None:
        b = p["basis_usd_bu_paranagua"]
        cls = "bull" if b > 0 else "bear"
        sinal = "+" if b > 0 else ""
        rodape_parts.append(
            f'<strong>Basis (US$/bu):</strong> '
            f'<span class="badge {cls}">{sinal}{b:.2f}</span>'
        )
    rodape_html = ""
    if rodape_parts:
        rodape_html = f'<div class="fisico-spread">{" &nbsp;|&nbsp; ".join(rodape_parts)}</div>'

    # Série histórica 14d (compactada num <details>)
    serie_html = ""
    serie = p.get("serie_14d") or []
    if len(serie) > 1:
        linhas = []
        for row in serie:
            png = _fmt_brl(row["paranagua"]) if row["paranagua"] else "—"
            rch = _fmt_brl(row["rancharia"]) if row["rancharia"] else "—"
            spread_v = row["spread"]
            if spread_v is not None:
                cls = "bull" if spread_v > 0 else "bear"
                spread_disp = f'<span class="badge {cls}">R$ {spread_v:+,.2f}</span>'
            else:
                spread_disp = '<span class="muted-small">—</span>'
            linhas.append(
                f'<tr><td class="hist-date">{row["data"]}</td>'
                f'<td class="hist-val">{png}</td>'
                f'<td class="hist-val">{rch}</td>'
                f'<td class="hist-val">{spread_disp}</td></tr>'
            )
        serie_html = f"""
        <details class="fisico-serie">
          <summary>📈 Histórico {len(serie)} dia(s) — {label.lower()}</summary>
          <table class="hist-table">
            <thead><tr><th>Data</th><th>Paranaguá ({sufixo})</th><th>Rancharia ({sufixo})</th><th>Spread</th></tr></thead>
            <tbody>{"".join(linhas)}</tbody>
          </table>
        </details>"""

    return f"""
    <div class="produto-card">
      <h3>{label} <span class="muted-small">— {unidade}</span></h3>
      <div class="fisico-grid">{''.join(rows_html)}</div>
      {publicas_html}
      {rodape_html}
      {serie_html}
    </div>"""


def _render_noticias(noticias: list[dict]) -> str:
    if not noticias:
        return "<p>Sem notícias recentes para soja, farelo ou óleo.</p>"
    COMM_LABEL = {"soja": "soja", "farelo": "farelo", "oleo_soja": "óleo"}
    items = []
    for n in noticias:
        comm = COMM_LABEL.get(n["commodity"], n["commodity"])
        descricao = (n.get("descricao") or "").strip()
        # Remove cabecalho redundante tipo "Cepea, 25/05/2026 –"
        if descricao and "–" in descricao[:30]:
            descricao = descricao.split("–", 1)[1].strip()
        elif descricao and "-" in descricao[:30]:
            descricao = descricao.split("-", 1)[1].strip()
        link = n.get("link") or ""
        fonte = n.get("fonte") or ""
        titulo_html = (
            f'<a href="{link}" target="_blank" rel="noopener">{n["titulo"]}</a>'
            if link else n["titulo"]
        )
        descricao_html = (
            f'<p class="news-desc">{descricao}</p>' if descricao else ""
        )
        items.append(f"""
        <li class="news-item">
          <div class="news-head">
            <span class="badge neutral">{comm}</span>
            <span class="news-source">{fonte}</span>
            <span class="news-date">{n["data"]}</span>
          </div>
          <div class="news-title">{titulo_html}</div>
          {descricao_html}
        </li>""")
    return f'<ul class="news-list">{"".join(items)}</ul>'


def _render_tese(tese: dict | None) -> str:
    if not tese:
        return ""
    vies_html = ""
    if tese.get("vies"):
        vies_html = " · ".join(f'<code>{v}</code>' for v in tese["vies"])
        vies_html = f' <span class="muted-small">({vies_html})</span>'
    return f"""
      <li>
        <div class="check"></div>
        <div>
          <strong>Tese ativa: {tese["nome"]}</strong>{vies_html}<br>
          <span class="muted-small">Insight de {tese.get("data", "?")} — detalhe na aba 💡 Insights
          (<code>insights/{tese.get("slug", "")}.md</code>).</span>
        </div>
      </li>"""


def _dia_semana_pt(d: date) -> str:
    nomes = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
    return nomes[d.weekday()]


# ============================================================
# Geracao narrativa heuristica — usa regras sobre os dados.
# Substitui placeholders manuais por texto factual gerado automaticamente.
# Quando Claude Code abrir e refinar, sobrescreve com versao mais elaborada.
# ============================================================

def _niveis_alerta() -> dict:
    """Níveis de suporte/resistência do alerts_config.toml (fonte única da
    verdade — evita hard-code de nível em texto narrativo, que apodrece
    quando o TOML é recalibrado)."""
    try:
        import tomllib
        with open(Path(__file__).parent / "alerts_config.toml", "rb") as f:
            cfg = tomllib.load(f)
        return {n["commodity"]: n for n in cfg.get("niveis", [])}
    except Exception:
        return {}


# ============================================================
# Camada decisória (Onda 1): convicção + confiança + Mesa do dia
# ============================================================

_CONV_PRODUTOS = [("soja", "Soja", "soja_cbot"),
                  ("farelo", "Farelo", "farelo_cbot"),
                  ("oleo_soja", "Óleo", "oleo_cbot")]


def _conv_label(s: int) -> str:
    return {3: "alta forte", 2: "alta", 1: "leve alta", 0: "neutro/misto",
            -1: "leve baixa", -2: "baixa", -3: "baixa forte"}.get(s, "neutro")


def _gerar_conviccao(d: dict) -> dict:
    """Score de convicção por commodity = (drivers de alta − drivers de baixa),
    limitado a [-3,+3]. Determinístico, reusa _gerar_drivers (que já cruza dado +
    tributário + insights). NEUTRO: é a inclinação de preço (long/short) e quão
    forte — NÃO ordem de compra/venda. A decisão fica com o trader."""
    drivers = d.get("drivers") or {}
    out = {}
    for slug, nome, snap_key in _CONV_PRODUTOS:
        dd = drivers.get(slug) or {}
        bull = dd.get("bull") or []
        bear = dd.get("bear") or []
        score = max(-3, min(3, len(bull) - len(bear)))
        out[slug] = {"nome": nome, "snap_key": snap_key, "score": score,
                     "label": _conv_label(score), "bull": bull, "bear": bear}
    return out


def _confianca_leitura(d: dict) -> tuple[str, list[str]]:
    """Confiança GLOBAL da leitura = saúde das fontes críticas + calibração
    direcional do forecast. Honestidade estatística > falsa precisão.
    Retorna (nivel, motivos). nivel: alta | media | baixa | suspensa."""
    estados = {f["fonte"]: f["estado"] for f in (d.get("saude_fontes") or [])}
    motivos = []
    nivel = "alta"
    core_off = [f for f in ("cme_cbot", "bcb") if estados.get(f) in ("erro", "atrasada")]
    fund_off = [f for f in ("usda_wasde", "abiove") if estados.get(f) == "erro"]
    if core_off:
        nivel = "suspensa"
        motivos.append("preço/câmbio fora (" + ", ".join(core_off) + ")")
    elif fund_off:
        nivel = "baixa"
        motivos.append("fundamento S&D indisponível (" + ", ".join(fund_off) + ")")
    calib = [c for c in (d.get("forecast_calib") or []) if c.get("n")]
    if calib:
        dir_pct = min(c["dir_pct"] for c in calib)
        if dir_pct < 55:
            motivos.append(f"forecast com acerto direcional baixo ({dir_pct:.0f}%) — use range, não direção")
            if nivel == "alta":
                nivel = "media"
    if not motivos:
        motivos.append("fontes de preço OK e calibração razoável")
    return nivel, motivos


_CONF_STYLE = {"alta": ("🟢", "var(--bull)"), "media": ("🟡", "var(--warn)"),
               "baixa": ("🟠", "var(--bear)"), "suspensa": ("🔴", "var(--bear)")}


def _linha_invalidacao(d: dict, conv: dict) -> str:
    """1 linha: o nível técnico que VIRA a leitura do produto de maior convicção."""
    candidatos = {k: v for k, v in conv.items() if v["score"] != 0}
    if not candidatos:
        return ""
    slug = max(candidatos, key=lambda k: abs(candidatos[k]["score"]))
    c = candidatos[slug]
    cfg = _niveis_alerta().get(c["snap_key"]) or {}
    if c["score"] > 0:  # viés de alta → vira se perder o suporte
        sup = cfg.get("suporte")
        if sup:
            return f"<strong>Vira</strong> se {c['nome']} perder o suporte {_fmt_num(sup, 2)}."
    else:  # viés de baixa → vira se romper a resistência
        res = cfg.get("resistencia")
        if res:
            return f"<strong>Vira</strong> se {c['nome']} romper a resistência {_fmt_num(res, 2)}."
    return ""


def _render_mesa_do_dia(d: dict) -> str:
    """Bloco-síntese no topo do Dashboard: confiança dos dados + semáforo por
    produto (viés/score + drivers a observar) + o que invalida. Leitura em 30s."""
    conv = d.get("conviccao") or {}
    if not conv:
        return ""
    nivel, motivos = _confianca_leitura(d)
    icone, cor = _CONF_STYLE.get(nivel, ("⚪", "var(--muted)"))

    linhas = []
    for slug, nome, snap_key in _CONV_PRODUTOS:
        c = conv.get(slug)
        if not c:
            continue
        score = c["score"]
        if score > 0:
            chip_cor, sinal = "var(--bull)", f"+{score}"
        elif score < 0:
            chip_cor, sinal = "var(--bear)", f"{score}"
        else:
            chip_cor, sinal = "var(--muted)", "0"
        obs = []
        if c["bull"]:
            obs.append("▲ " + c["bull"][0]["texto"])
        if c["bear"]:
            obs.append("▼ " + c["bear"][0]["texto"])
        obs_html = "<br>".join(f'<span class="muted-small">{o}</span>' for o in obs) \
            or '<span class="muted-small">sem driver ativo</span>'
        linhas.append(
            f'<tr><td style="font-weight:600">{nome}</td>'
            f'<td style="text-align:center"><span style="display:inline-block;min-width:2.2em;'
            f'padding:2px 8px;border-radius:6px;background:{chip_cor};color:#fff;font-weight:700">{sinal}</span></td>'
            f'<td style="color:{chip_cor};font-weight:600">{c["label"]}</td>'
            f'<td>{obs_html}</td></tr>'
        )

    inval = _linha_invalidacao(d, conv)
    motivos_html = " · ".join(motivos)
    return f"""
    <div class="card" style="border-left:3px solid {cor};">
      <div style="display:flex;align-items:baseline;gap:10px;flex-wrap:wrap;margin-bottom:8px">
        <strong style="font-size:1.05em">🧭 Mesa do dia</strong>
        <span style="color:{cor};font-weight:700">{icone} confiança {nivel}</span>
        <span class="muted-small">{motivos_html}</span>
      </div>
      <table class="hist-table" style="margin:0">
        <thead><tr><th style="text-align:left">produto</th><th>viés</th>
        <th>leitura</th><th style="text-align:left">o que observar</th></tr></thead>
        <tbody>{"".join(linhas)}</tbody>
      </table>
      <p class="muted-small" style="margin:8px 0 0">
        Viés = drivers de alta − de baixa (escala −3…+3), <strong>leitura de preço</strong>
        long/short, não ordem de compra. {inval}
      </p>
    </div>"""


def _trend5_pct(commodity: str) -> float | None:
    """Variação % nos últimos ~5 pregões de uma commodity CBOT (None se faltar série)."""
    with db.connect() as conn:
        rows = conn.execute(
            """SELECT valor FROM dados_publicos WHERE fonte='cme_cbot'
               AND commodity=? AND metrica='fechamento' AND valor IS NOT NULL
               ORDER BY data_referencia DESC LIMIT 6""",
            (commodity,),
        ).fetchall()
    if len(rows) >= 2 and rows[-1]["valor"]:
        return (rows[0]["valor"] - rows[-1]["valor"]) / rows[-1]["valor"] * 100
    return None


# (label, fonte, commodity, metrica, casas, sufixo, frase_sobe, frase_desce)
_MUDOU_SPECS = [
    ("Ratio Far/Soj", "indicators", "complexo_soja", "far_soj_ratio_pct", 1, "%",
     "spread esticando (farelo ganha de soja)", "spread comprimindo (farelo cede vs soja)"),
    ("Oil share", "indicators", "complexo_soja", "oil_share_pct", 1, "%",
     "óleo ganha peso no crush", "óleo cede peso no crush"),
    ("Crush margin", "indicators", "complexo_soja", "crush_margin_usd_bu", 2, " USD/bu",
     "esmagamento mais rentável", "esmagamento menos rentável"),
    ("USD/BRL", "bcb", "usd_brl_ptax", "valor", 4, "",
     "real mais fraco — sobe a paridade em R$", "real mais forte — pressiona a paridade em R$"),
]


def _render_o_que_mudou(target: date) -> str:
    """Tabela 'o que mudou desde ontem': indicadores-chave do complexo, D-1, leitura neutra."""
    linhas = []
    with db.connect() as conn:
        for label, fonte, comm, metrica, casas, sufixo, sobe, desce in _MUDOU_SPECS:
            rows = conn.execute(
                """SELECT valor FROM dados_publicos WHERE fonte=? AND commodity=? AND metrica=?
                   AND valor IS NOT NULL AND data_referencia<=?
                   ORDER BY data_referencia DESC LIMIT 2""",
                (fonte, comm, metrica, target.isoformat()),
            ).fetchall()
            if not rows:
                continue
            hoje = rows[0]["valor"]
            ontem = rows[1]["valor"] if len(rows) > 1 else None
            if ontem is None:
                d_txt, leitura, cor = "—", "sem referência D-1", "var(--muted)"
            else:
                # Δ sobre os valores ARREDONDADOS p/ bater com as colunas exibidas
                # (senão 79,8→80,0 mostraria Δ+0,1 e parece erro).
                delta = round(hoje, casas) - round(ontem, casas)
                eps = 10 ** (-casas) / 2
                if delta > eps:
                    leitura, cor = sobe, "var(--bull)"
                elif delta < -eps:
                    leitura, cor = desce, "var(--bear)"
                else:
                    leitura, cor = "estável", "var(--muted)"
                sinal = "+" if delta >= 0 else ""
                d_txt = f'<span style="color:{cor}">{sinal}{_fmt_num(delta, casas)}</span>'
            ontem_txt = (_fmt_num(ontem, casas) + sufixo) if ontem is not None else "—"
            linhas.append(
                f'<tr><td style="font-weight:600">{label}</td>'
                f'<td class="hist-val">{ontem_txt}</td>'
                f'<td class="hist-val">{_fmt_num(hoje, casas)}{sufixo}</td>'
                f'<td class="hist-val">{d_txt}</td>'
                f'<td><span class="muted-small" style="color:{cor}">{leitura}</span></td></tr>'
            )
    if not linhas:
        return ""
    return f"""
    <div class="card">
      <table class="hist-table" style="margin:0">
        <thead><tr><th style="text-align:left">indicador</th><th>ontem</th>
        <th>hoje</th><th>Δ</th><th style="text-align:left">leitura</th></tr></thead>
        <tbody>{"".join(linhas)}</tbody>
      </table>
      <p class="muted-small" style="margin:6px 0 0">Δ vs último valor anterior (D-1).
      Preços de farelo/soja/óleo já estão no snapshot acima.</p>
    </div>"""


def _gerar_contradicoes(d: dict) -> list[dict]:
    """Detecta TENSÕES entre sinais (leitura de mesa): onde os indicadores não
    apontam todos pro mesmo lado. Cada uma: o conflito + a implicação pro trader.
    100% derivado de dados já no DB (convicção, ratio, oil share, COT)."""
    out = []
    conv = d.get("conviccao") or {}
    fs = d.get("far_soj") or {}
    s = d.get("snapshot") or {}
    oil_share = (s.get("oil_share") or {}).get("valor")
    pct_cot = {c["slug"]: c["percentil"] for c in (d.get("cot") or {}).get("commodities", [])}
    soja_sc = (conv.get("soja") or {}).get("score", 0)
    far_sc = (conv.get("farelo") or {}).get("score", 0)
    zona = fs.get("zona")

    if soja_sc > 0 and far_sc < 0:
        out.append({
            "titulo": "Soja com viés de alta × farelo de baixa",
            "explicacao": "O óleo concentra o valor do crush; o farelo sai como sobra do esmagamento.",
            "implicacao": "Spread far÷soj tende a seguir comprimido — convergência (long farelo/short soja) tem vento contra enquanto o óleo dominar.",
        })

    t_far = _trend5_pct("farelo_cbot")
    if zona == "comprimido" and t_far is not None and t_far < -1:
        out.append({
            "titulo": "Farelo barato vs soja × ainda caindo no CBOT",
            "explicacao": f"Spread comprimido (valor de mean-reversion), mas o farelo cai {t_far:+.1f}% em 5 pregões (faca caindo).",
            "implicacao": "O valor existe, mas falta exaustão — esperar virada de momentum antes de apostar na convergência.",
        })

    p_oleo = pct_cot.get("oleo_cbot")
    if oil_share is not None and oil_share >= 50 and p_oleo is not None and p_oleo >= 85:
        out.append({
            "titulo": "Óleo dominando o crush × fundos comprados no extremo",
            "explicacao": f"Oil share {oil_share:.1f}% (óleo manda) e managed money no percentil {p_oleo:.0f} de 5 anos.",
            "implicacao": "A tendência pode durar, mas a assimetria piora: notícia ruim de RIN/diesel/palma vira realização rápida.",
        })

    p_far = pct_cot.get("farelo_cbot")
    if zona == "comprimido" and p_far is not None and 15 < p_far < 85:
        out.append({
            "titulo": "Spread comprimido × posicionamento sem extremo",
            "explicacao": f"Farelo barato vs soja, mas os fundos estão no percentil {p_far:.0f} (sem capitulação técnica).",
            "implicacao": "A oportunidade de spread existe, mas pode faltar o empurrão de um extremo de posicionamento.",
        })

    return out


def _render_contradicoes(contras: list[dict]) -> str:
    if not contras:
        return ""
    itens = []
    for c in contras:
        itens.append(
            f'<div style="margin:0 0 10px">'
            f'<strong>⚠ {c["titulo"]}</strong><br>'
            f'<span class="muted-small">{c["explicacao"]}</span><br>'
            f'<span class="muted-small">→ <em>{c["implicacao"]}</em></span></div>'
        )
    return f"""
    <div class="card">
      {"".join(itens)}
      <p class="muted-small" style="margin:2px 0 0">Tensões entre sinais — onde a leitura
      não é unânime. Pensar como mesa, não seguir um indicador só.</p>
    </div>"""


_VIES_CSS = {"bull": "var(--bull)", "bear": "var(--bear)", "warn": "var(--warn)", "neutral": "var(--muted)"}


def _render_indices_sinteticos(target: date) -> str:
    """Índice de Sobra de Farelo + Suporte do Óleo (0-100, contagem de condições).
    Mostra o número, a banda e a LISTA de condições ON/OFF — auditável, sem caixa-preta."""
    import indicators
    try:
        idx = indicators.compute_indices_sinteticos(target)
    except Exception:
        return ""
    metas = [
        ("sobra_farelo", "Índice de Sobra de Farelo",
         "quanto o mercado tende a gerar farelo acima da absorção (pressão baixista no farelo)"),
        ("suporte_oleo", "Índice de Suporte do Óleo",
         "quantos pilares de sustentação do óleo estão ativos"),
    ]
    cards = []
    for key, titulo, sub in metas:
        ix = idx.get(key)
        if not ix or ix.get("valor") is None:
            continue
        cor = _VIES_CSS.get(ix["vies"], "var(--muted)")
        v = ix["valor"]
        conds = []
        for nome, ativo, detalhe in ix["condicoes"]:
            if ativo is None:
                mark, c = "—", "var(--muted)"
            elif ativo:
                mark, c = "●", cor
            else:
                mark, c = "○", "var(--muted)"
            conds.append(
                f'<li style="margin:2px 0"><span style="color:{c}">{mark}</span> {nome} '
                f'<span class="muted-small">({detalhe})</span></li>'
            )
        cards.append(f"""
        <div class="card" style="flex:1;min-width:300px">
          <h3 style="margin:0 0 6px">{titulo}</h3>
          <div style="display:flex;align-items:baseline;gap:10px;flex-wrap:wrap">
            <span style="font-size:2.2em;font-weight:700;color:{cor};line-height:1">{v}</span>
            <span style="color:{cor};font-weight:600">{ix['label']}</span>
            <span class="muted-small">{ix['n_ativos']}/{ix['n_aval']} condições ativas</span>
          </div>
          <div style="height:8px;border-radius:4px;background:var(--surface2);margin:8px 0 10px;overflow:hidden">
            <div style="height:100%;width:{v}%;background:{cor}"></div>
          </div>
          <p class="muted-small" style="margin:0 0 6px">{sub}</p>
          <ul style="margin:0;padding:0;list-style:none;font-size:0.92em">{''.join(conds)}</ul>
        </div>""")
    if not cards:
        return ""
    return f'<div style="display:flex;gap:14px;flex-wrap:wrap">{"".join(cards)}</div>'


def _gerar_resumo_executivo(d: dict) -> str:
    """Resumo em 3 frases rotuladas: Mercado / Farelo / Leitura.

    Reescrito 2026-06-11 (revisão trader) e reenquadrado 2026-06-17 (lente de
    trader, não de comprador). CFTC e WASDE moram nos Insights críticos logo
    abaixo — aqui só o que muda a leitura de hoje.
    """
    s = d["snapshot"]
    fs = d.get("far_soj") or {}
    niveis = _niveis_alerta()

    frases = []

    # 1. Mercado — estado do complexo em 1 frase
    cm = (s.get("crush_margin") or {}).get("valor")
    oshare = (s.get("oil_share") or {}).get("valor")
    if cm is not None and oshare is not None and oshare >= 50 and cm > 2:
        frases.append(
            f"<strong>Mercado:</strong> complexo partido — o óleo paga o crush "
            f"(oil share {_fmt_num(oshare, 1)}%, margem {_fmt_usd(cm)}/bu) e o farelo sai como sobra."
        )
    elif cm is not None:
        estado = "gordo" if cm > 2 else ("normal" if cm > 0.8 else "apertado")
        sufixo = f", oil share {_fmt_num(oshare, 1)}%." if oshare is not None else "."
        frases.append(f"<strong>Mercado:</strong> crush {estado} ({_fmt_usd(cm)}/bu){sufixo}")

    # 2. Farelo — a única frase carregada de números, em farelo
    farelo = s.get("farelo_cbot") or {}
    if farelo.get("valor"):
        delta_txt = f" ({farelo['delta_pct']:+.1f}% no dia)" if farelo.get("delta_pct") is not None else ""
        pct_txt = f", percentil {farelo['pct52']:.0f} das 52 semanas" if farelo.get("pct52") is not None else ""
        brl_txt = f" ≈ {_fmt_brl(farelo['brl'])}/t paridade" if farelo.get("brl") else ""
        ratio_txt = f"; ratio Far/Soj {_fmt_num(fs['atual'], 1)}%" if fs.get("disponivel") else ""
        frases.append(
            f"<strong>Farelo:</strong> {_fmt_usd(farelo['valor'])}/sht"
            f"{delta_txt}{pct_txt}{brl_txt}{ratio_txt}."
        )

    # 3. Leitura — o que os dados dizem (informação, não ordem de compra/venda)
    if fs.get("disponivel"):
        res_farelo = (niveis.get("farelo_cbot") or {}).get("resistencia", 325)
        if fs["zona"] == "comprimido":
            leitura = ("spread Far/Soj comprimido — farelo historicamente barato vs grão "
                       "(mean-reversion favorece convergência)")
        elif fs["zona"] == "neutro" and (fs.get("delta_5d") or 0) < 0:
            leitura = "spread comprimindo rumo à zona &lt;80% — acompanhar de perto"
        elif fs["zona"] == "neutro":
            leitura = "spread em zona neutra, sem extremo de valor"
        else:
            leitura = ("spread Far/Soj esticado — farelo caro vs grão "
                       "(mean-reversion favorece o lado inverso)")
        frases.append(
            f"<strong>Leitura:</strong> {leitura}; referência técnica: o farelo CBOT "
            f"superar {_fmt_num(res_farelo, 0)} USD/sht (resistência configurada) muda o quadro."
        )

    return " ".join(frases) if frases else "<em>Dados insuficientes para resumo automático.</em>"


def _gerar_insights(d: dict) -> list[dict]:
    """Lista de 3-6 insights baseados em regras sobre os dados."""
    s = d["snapshot"]
    out = []

    # 1. Crush margin alto (nível econômico fixo $2,00 = "zona gorda" histórica;
    # NÃO confundir com o nível de ALERTA do alerts_config, que marca mudança de tese)
    cm = s.get("crush_margin", {}).get("valor")
    if cm and cm > 2.0:
        out.append({
            "tipo": "warn",
            "icon": "🔥",
            "texto": (
                f"<strong>Crush margin {_fmt_usd(cm)}/bu</strong> em zona historicamente "
                f"gorda (>$2,00 vs média $0,40–0,80). Esmagadoras ULTRA rentáveis = rodam full = "
                f"pressão sobre farelo+óleo em 4–6 semanas."
            ),
        })

    # 2. Paridade BR
    soja_brl = s.get("soja_brl_paridade", {}).get("valor")
    usd_brl = s.get("usd_brl", {}).get("valor")
    if soja_brl and usd_brl:
        out.append({
            "tipo": "neutral",
            "icon": "📊",
            "texto": (
                f"<strong>Soja BR paridade {_fmt_brl(soja_brl)}/sc</strong> (CBOT × câmbio sem basis). "
                f"USD/BRL em {_fmt_num(usd_brl, 4)}."
            ),
        })

    # 3. Plantio EUA
    plantio = s.get("plantio_soja_eua", {}).get("valor")
    plantio_data = s.get("plantio_soja_eua", {}).get("data")
    if plantio:
        if plantio < 30:
            estado = "<strong>atrasado</strong> — pode dar suporte temporário aos preços"
            tipo = "bull"
        elif plantio > 90:
            estado = "praticamente concluído — atenção vai pra condição/clima"
            tipo = "neutral"
        else:
            estado = "em ritmo normal"
            tipo = "neutral"
        out.append({
            "tipo": tipo,
            "icon": "🇺🇸",
            "texto": (
                f"<strong>Plantio soja EUA: {plantio:.0f}%</strong> em {plantio_data} — {estado}. "
                f"Próxima leitura USDA Crop Progress segunda."
            ),
        })

    # 4. CFTC
    cftc = s.get("cftc_net", {})
    if cftc.get("delta_pct") is not None:
        d_pct = cftc["delta_pct"]
        if d_pct < -2:
            out.append({
                "tipo": "bear",
                "icon": "📉",
                "texto": (
                    f"<strong>CFTC managed money soja</strong>: {cftc['valor']/1000:.0f}k net long em {cftc['data']}, "
                    f"caiu {_fmt_num(d_pct, 1)}% vs semana anterior — sinal técnico de topo. Próximo COT sexta."
                ),
            })
        elif d_pct > 2:
            out.append({
                "tipo": "bull",
                "icon": "📈",
                "texto": (
                    f"<strong>CFTC managed money soja</strong>: {cftc['valor']/1000:.0f}k net long, "
                    f"+{_fmt_num(d_pct, 1)}% vs sem — fundos seguem comprando."
                ),
            })

    # 5. Noticia mais recente da soja
    for n in d.get("noticias", []):
        if n["commodity"] == "soja":
            fonte = n.get("fonte") or "RSS"
            out.append({
                "tipo": "neutral",
                "icon": "🌎",
                "texto": (
                    f"<strong>{fonte} {n['data']}</strong>: \"{n['titulo']}\". "
                    f"Acompanhar sentimento BR."
                ),
            })
            break

    # 6. Oleo proximo do suporte
    oleo = s.get("oleo_cbot", {}).get("valor")
    if oleo and oleo < 75:
        out.append({
            "tipo": "bear",
            "icon": "⚠",
            "texto": (
                f"<strong>Óleo CBOT em {_fmt_num(oleo, 2)} cts/lb</strong> — testando suporte psicológico de 72. "
                f"Quebra abre caminho para 68/65."
            ),
        })

    return out[:6]  # cap em 6


_DRIVER_PRODUTOS = [("soja", "🌱 Soja em grão"),
                    ("farelo", "🥣 Farelo de soja"),
                    ("oleo_soja", "🛢️ Óleo de soja degomado")]


def _gerar_drivers(d: dict) -> dict:
    """Drivers bull/bear POR commodity (soja/farelo/oleo_soja), 100% data-driven.

    Reescrito 2026-06-11 — a versão anterior tinha fatos hard-coded da varredura
    de 05/jun que apodreciam no código. Agora 3 fontes vivas:
      (a) regras quantitativas sobre snapshot/DB (recalculam a cada synth)
      (b) Monitor Tributário: eventos vigentes/tramitando com produtos+direção
      (c) insights ativos com frontmatter `vies: [bull-farelo, bear-oleo_soja]`
    Perspectiva NEUTRA de mercado (alta = bullish preço) — a leitura de spread
    do farelo (far÷soj) fica no card Far/Soj.
    """
    out = {slug: {"bull": [], "bear": []} for slug, _ in _DRIVER_PRODUTOS}
    s = d["snapshot"]

    def add(prod, lado, texto, horizon, fonte):
        out[prod][lado].append({"texto": texto, "horizon": horizon, "fonte": fonte})

    def trend5(commodity):
        """Variação % nos últimos ~5 pregões."""
        with db.connect() as conn:
            rows = conn.execute(
                """
                SELECT valor FROM dados_publicos
                WHERE fonte='cme_cbot' AND commodity=? AND metrica='fechamento'
                ORDER BY data_referencia DESC LIMIT 6
                """,
                (commodity,),
            ).fetchall()
        if len(rows) >= 2 and rows[-1]["valor"]:
            return (rows[0]["valor"] - rows[-1]["valor"]) / rows[-1]["valor"] * 100
        return None

    # ---------- (a) regras quantitativas ----------
    cm = (s.get("crush_margin") or {}).get("valor")
    if cm is not None and cm > 2.0:
        add("farelo", "bear",
            f"Crush margin {_fmt_usd(cm)}/bu — esmagamento a fundo despeja farelo (subproduto)",
            "CP/MP", "dado")
        add("soja", "bull",
            f"Crush {_fmt_usd(cm)}/bu sustenta demanda da esmagadora pelo grão",
            "CP", "dado")
    elif cm is not None and cm < 0.8:
        add("farelo", "bull",
            f"Crush margin {_fmt_usd(cm)}/bu apertado — esmagadora reduz ritmo, menos farelo novo",
            "CP/MP", "dado")

    oshare = (s.get("oil_share") or {}).get("valor")
    if oshare is not None and oshare >= 50:
        add("oleo_soja", "bull",
            f"Oil share {oshare:.1f}% — óleo comanda o valor do crush",
            "MP", "dado")
        add("farelo", "bear",
            f"Oil share {oshare:.1f}%: esmagadora aceita farelo barato pra capturar o óleo",
            "MP", "dado")

    fs_atual = (d.get("far_soj") or {}).get("atual")
    if fs_atual:
        if fs_atual < 80:
            add("farelo", "bear",
                f"Ratio Far/Soj {fs_atual:.1f}% — farelo historicamente barato vs grão",
                "CP", "dado")
        elif fs_atual >= 87:
            add("farelo", "bull",
                f"Ratio Far/Soj {fs_atual:.1f}% — farelo aperta vs grão",
                "CP", "dado")

    for prod, comm, nome_c in (("soja", "soja_cbot", "Soja"),
                               ("farelo", "farelo_cbot", "Farelo"),
                               ("oleo_soja", "oleo_cbot", "Óleo")):
        t = trend5(comm)
        if t is not None and abs(t) >= 2:
            add(prod, "bull" if t > 0 else "bear",
                f"{nome_c} CBOT {t:+.1f}% em 5 pregões — momentum de {'alta' if t > 0 else 'baixa'}",
                "CP", "dado")

    # FOB export do farelo vs interno (cotação pública NAG)
    fb = (((d.get("fisico_br") or {}).get("produtos") or {})
          .get("farelo") or {}).get("publicas") or []
    fob = next((q for q in fb if q.get("tipo") == "fob_implicito"), None)
    if fob and fob.get("delta_vs_manual") is not None:
        dv = fob["delta_vs_manual"]
        if dv < -20:
            add("farelo", "bear",
                f"FOB Paranaguá {_fmt_brl(abs(dv))}/t ABAIXO do interno — export não compete, oferta sobra dentro",
                "CP", "dado")
        elif dv > 50:
            add("farelo", "bull",
                f"FOB Paranaguá {_fmt_brl(dv)}/t ACIMA do interno — esmagadora prefere exportar, aperta o interno",
                "CP", "dado")

    # Virada do prêmio export PGUA: saindo de ~0 pra positivo relevante = a
    # demanda externa voltou a disputar o farelo = chão no preço interno
    hist_prem = (fob or {}).get("premio_historico") or []
    if len(hist_prem) >= 2:
        delta_prem = hist_prem[0][1] - hist_prem[-1][1]
        if delta_prem >= 2.0:
            add("farelo", "bull",
                f"Prêmio export PGUA subiu {delta_prem:+.2f} US$/sht em {len(hist_prem)} fechamentos — export voltando a disputar",
                "CP", "dado")
        elif delta_prem <= -2.0:
            add("farelo", "bear",
                f"Prêmio export PGUA caiu {delta_prem:+.2f} US$/sht — export ainda mais fora do jogo",
                "CP", "dado")

    margem_bio = (d.get("biodiesel_us") or {}).get("margem")
    if isinstance(margem_bio, (int, float)):
        if margem_bio > 0.30:
            add("oleo_soja", "bull",
                f"Margem biodiesel US positiva (US$ {margem_bio:.2f}/gal) — demanda por óleo firme",
                "CP", "dado")
        elif margem_bio < 0:
            add("oleo_soja", "bear",
                f"Margem biodiesel US negativa (US$ {margem_bio:.2f}/gal) — produtor tira o pé",
                "CP", "dado")

    wasde = d.get("wasde_br", {})
    if wasde.get("soja", 0) >= 175:
        add("soja", "bear",
            f"WASDE: safra BR projetada {_fmt_num(wasde['soja'], 0)} mi t — oferta estrutural pesada",
            "MP", "dado")

    # ---------- (b) Monitor Tributário (produtos + direção por evento) ----------
    try:
        for ev in trib_mod.list_eventos():
            if ev.get("status") not in ("vigente", "tramitacao"):
                continue
            if ev.get("direcao") not in ("alta", "baixa"):
                continue
            prods = [p.strip() for p in (ev.get("produtos") or "").split(",") if p.strip()]
            lado = "bull" if ev["direcao"] == "alta" else "bear"
            marcador = " (tramitando)" if ev["status"] == "tramitacao" else ""
            for p in prods:
                if p in out:
                    add(p, lado, f"{ev['titulo']}{marcador}", "MP", "tributario")
    except Exception:
        pass  # monitor vazio/não sincronizado não derruba o HTML

    # ---------- (c) insights ativos com frontmatter vies ----------
    for ins in (d.get("insights_estudo") or []):
        if (ins.get("status") or "").lower() not in ("ativa", "revisada"):
            continue
        vies = ins.get("vies") or []
        if isinstance(vies, str):
            vies = [vies]
        for token in vies:
            m = re.match(r"^(bull|bear)-(soja|farelo|oleo_soja)$", str(token).strip())
            if m:
                add(m.group(2), m.group(1),
                    f"Insight: {ins.get('titulo', '')[:90]}",
                    "MP", "insight")

    return out


# ============================================================
# CSS (mesmo do exemplo manual aprovado)
# ============================================================

_CSS = """
  :root{
    --bg:#0b1220; --surface:#121a2c; --surface2:#1a2440; --border:#22304f;
    --text:#e7ecf3; --muted:#9aa6b8; --accent:#3b82f6;
    --bull:#10b981; --bull-bg:#0f3024;
    --bear:#ef4444; --bear-bg:#3a1416;
    --warn:#f59e0b; --warn-bg:#3a2a0d;
    --neutral:#64748b;
  }
  *{box-sizing:border-box}
  body{margin:0;background:var(--bg);color:var(--text);font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Inter,system-ui,sans-serif;line-height:1.55;font-size:15px}
  .container{max-width:1180px;margin:0 auto;padding:24px 20px 80px}
  header{margin-bottom:24px;padding-bottom:16px;border-bottom:1px solid var(--border)}
  header h1{margin:0 0 4px;font-size:24px;font-weight:700;letter-spacing:-0.3px}
  header .meta{color:var(--muted);font-size:13px}
  header .meta strong{color:var(--text)}
  h2{margin:32px 0 12px;font-size:17px;font-weight:600;letter-spacing:-0.2px;display:flex;align-items:center;gap:8px;padding-bottom:6px;border-bottom:1px solid var(--border)}
  h2 .tag{font-size:11px;padding:2px 8px;border-radius:6px;background:var(--surface2);color:var(--muted);font-weight:500;border-bottom:none}
  .kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-bottom:8px}
  .kpi{background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:14px 16px;transition:border-color .15s ease}
  .kpi:hover{border-color:var(--accent)}
  .kpi .spark{margin-top:8px;opacity:.85;line-height:0}
  .kpi .spark svg{display:block;max-width:100%}
  .chart-card svg{display:block;max-width:100%;height:auto}
  .chart-card{overflow-x:auto}
  details.card summary{outline:none}
  details.card[open] summary{margin-bottom:10px}
  .kpi .label{color:var(--muted);font-size:11px;text-transform:uppercase;letter-spacing:.5px;margin-bottom:4px}
  .kpi .value{font-size:22px;font-weight:700;letter-spacing:-0.5px}
  .kpi .unit{color:var(--muted);font-size:12px;font-weight:400;margin-left:4px}
  .kpi .change{font-size:12px;margin-top:2px;color:var(--muted)}
  .kpi .brl{display:inline-block;margin-top:6px;padding:3px 9px;background:rgba(59,130,246,0.13);border:1px solid rgba(59,130,246,0.30);border-radius:6px;color:#bfdbfe;font-size:13px;font-weight:600;font-family:'SF Mono',Menlo,Consolas,monospace}
  .kpi.bull{border-left:3px solid var(--bull)}
  .kpi.bear{border-left:3px solid var(--bear)}
  .kpi.warn{border-left:3px solid var(--warn)}
  .kpi.neutral{border-left:3px solid var(--neutral)}
  .card{background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:18px 20px;margin-bottom:16px}
  .card.alert{border:1px solid var(--warn);background:linear-gradient(180deg,var(--warn-bg) 0%,var(--surface) 60%)}
  .lead{font-size:15px;line-height:1.65}
  .two-col{display:grid;grid-template-columns:1fr 1fr;gap:14px}
  @media (max-width:760px){.two-col{grid-template-columns:1fr}}
  .insights{list-style:none;padding:0;margin:0}
  .insights li{padding:10px 12px;border-radius:8px;background:var(--surface2);margin-bottom:8px;border-left:3px solid var(--accent)}
  .insights li.bull{border-left-color:var(--bull)}
  .insights li.bear{border-left-color:var(--bear)}
  .insights li.warn{border-left-color:var(--warn)}
  .drivers .card h3{margin:0 0 10px;font-size:14px;font-weight:600}
  .drivers .card.bull h3{color:var(--bull)}
  .drivers .card.bear h3{color:var(--bear)}
  .drivers ul{margin:0;padding-left:18px}
  .drivers li{margin-bottom:6px;font-size:14px}
  .horizon{display:inline-block;font-size:10px;padding:1px 6px;border-radius:4px;background:var(--surface);color:var(--muted);margin-left:6px;vertical-align:middle}
  table{width:100%;border-collapse:collapse;margin-top:8px;font-size:13px}
  th{text-align:left;padding:8px 10px;background:var(--surface2);color:var(--muted);font-weight:500;text-transform:uppercase;font-size:11px;letter-spacing:.5px;border-bottom:1px solid var(--border)}
  td{padding:10px;border-bottom:1px solid var(--border)}
  tr:last-child td{border-bottom:none}
  tr:hover td{background:var(--surface2)}
  .commodity{font-weight:600}
  .band{font-family:'SF Mono',Menlo,Consolas,monospace;font-size:12px}
  .band .lo,.band .hi{color:var(--muted)}
  .band .mid{color:var(--text);font-weight:600;padding:0 4px}
  .badge{display:inline-block;padding:2px 8px;border-radius:6px;font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.3px}
  .badge.bull{background:var(--bull-bg);color:var(--bull)}
  .badge.bear{background:var(--bear-bg);color:var(--bear)}
  .badge.neutral{background:var(--surface2);color:var(--muted)}
  .badge.warn{background:var(--warn-bg);color:var(--warn)}  /* dado velho/qualidade — não é sinal de mercado */
  .events{list-style:none;padding:0;margin:0}
  .events li{display:flex;align-items:center;padding:8px 12px;border-radius:8px;background:var(--surface2);margin-bottom:6px}
  .events .date{font-weight:600;width:90px;color:var(--text);font-size:13px}
  .events .name{flex:1;font-size:14px}
  .events .stars{color:var(--warn);font-size:13px;letter-spacing:1px}
  .news-list{list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:10px}
  .news-item{padding:12px 14px;background:var(--surface2);border-radius:10px;border-left:3px solid var(--accent)}
  .news-head{display:flex;align-items:center;gap:8px;margin-bottom:6px;flex-wrap:wrap}
  .news-source{font-size:11px;font-weight:600;color:var(--accent);text-transform:uppercase;letter-spacing:.4px}
  .news-date{font-size:11px;color:var(--muted);margin-left:auto;font-family:monospace}
  .news-title{font-size:15px;font-weight:600;color:var(--text);margin-bottom:4px;line-height:1.3}
  .news-title a{color:var(--text);text-decoration:none;border-bottom:1px dotted var(--muted)}
  .news-title a:hover{color:var(--accent);border-bottom-color:var(--accent)}
  .news-desc{font-size:13px;color:var(--muted);line-height:1.5;margin:6px 0 0;text-align:justify}
  .fisico-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:14px}
  .fisico-row{padding:14px;background:var(--surface2);border-radius:10px;border-left:3px solid var(--accent)}
  .fisico-head{display:flex;align-items:center;gap:10px;margin-bottom:8px;flex-wrap:wrap}
  .fisico-praca{font-size:15px;font-weight:700;color:var(--text)}
  .fisico-valor{font-size:24px;font-weight:700;color:var(--text);margin:4px 0;font-family:monospace}
  .fisico-var{margin-top:6px;font-size:13px}
  .fisico-spread{padding:10px 14px;background:var(--surface2);border-radius:8px;margin-top:8px;font-size:14px;display:flex;align-items:center;gap:10px;flex-wrap:wrap}
  .fisico-indicador{margin-top:8px;padding:8px 10px;background:rgba(0,0,0,0.15);border-radius:6px;font-size:13px;border-left:2px solid var(--muted);display:flex;align-items:center;gap:8px;flex-wrap:wrap}
  .crush-real-info{padding:10px 14px;background:var(--surface2);border-radius:8px;margin-bottom:14px;font-size:14px;border-left:3px solid var(--accent)}
  .crush-grid{display:flex;flex-direction:column;gap:18px}
  .crush-block h3{margin:4px 0 8px;font-size:15px;color:var(--accent);font-weight:600}
  .crush-table{width:100%;border-collapse:separate;border-spacing:4px;font-size:13px}
  .crush-corner{background:transparent;text-align:left;padding:6px 10px;color:var(--muted);font-weight:500;font-size:11px;text-transform:uppercase;letter-spacing:.3px}
  .crush-h{background:var(--surface2);color:var(--muted);padding:6px 10px;border-radius:6px;text-align:center;font-size:12px;font-weight:600;text-transform:uppercase;letter-spacing:.3px}
  .crush-row-h{background:var(--surface2);color:var(--text);padding:8px 12px;text-align:left;font-weight:600;border-radius:6px;font-size:13px}
  .crush-cell{padding:8px 6px;text-align:center;border-radius:6px;position:relative}
  .crush-val{font-size:15px;font-weight:700;font-family:monospace}
  .crush-sub{font-size:10px;opacity:0.8;margin-top:2px;font-family:monospace;font-weight:400}
  .crush-green{background:#1a4d2e;color:#5cd9a3}
  .crush-yellow{background:#665a1c;color:#ffd866}
  .crush-red{background:#5c2024;color:#ff7a85}
  .crush-real{outline:2px solid var(--accent);outline-offset:-2px}
  .crush-marker{position:absolute;top:-8px;left:50%;transform:translateX(-50%);background:var(--accent);color:#000;font-size:9px;padding:2px 6px;border-radius:8px;font-weight:700;white-space:nowrap;letter-spacing:.3px}
  .bio-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:14px 0}
  .bio-block{padding:14px;background:var(--surface2);border-radius:10px;text-align:center}
  .bio-label{font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.3px;font-weight:600;margin-bottom:8px}
  .bio-margem{font-size:24px;font-weight:700;font-family:monospace;display:inline-block;padding:6px 14px;border-radius:8px}
  .bio-val{font-size:20px;font-weight:700;font-family:monospace;color:var(--text)}
  .bio-alerta{padding:12px 16px;border-radius:8px;font-size:14px;margin:8px 0;font-weight:500}
  .bio-bull{background:var(--bull-bg);color:var(--bull);border-left:3px solid var(--bull)}
  .bio-bear{background:var(--bear-bg);color:var(--bear);border-left:3px solid var(--bear)}
  .bio-warn{background:rgba(255,200,80,0.15);color:#ffb84d;border-left:3px solid #ffb84d}
  .bio-neutral{background:var(--surface2);color:var(--muted);border-left:3px solid var(--muted)}
  /* ============== ABAS (TABS) ============== */
  .tabs{display:flex;gap:6px;margin:18px 0 20px;padding:6px;background:var(--surface);border-radius:12px;border:1px solid var(--border);overflow-x:auto;flex-wrap:nowrap;position:sticky;top:0;z-index:50;backdrop-filter:blur(8px)}
  .tab-btn{flex:1;min-width:fit-content;padding:10px 16px;background:transparent;color:var(--muted);border:none;border-radius:8px;font-size:14px;font-weight:600;cursor:pointer;transition:all .15s ease;font-family:inherit;white-space:nowrap}
  .tab-btn:hover{color:var(--text);background:var(--surface2)}
  .tab-btn.active{background:var(--accent);color:#fff}
  .tab-btn.active:hover{background:var(--accent);color:#fff}
  .tab-pane{display:none;animation:fadeIn .2s ease}
  .tab-pane.active{display:block}
  @keyframes fadeIn{from{opacity:0;transform:translateY(4px)}to{opacity:1;transform:none}}
  /* Fallback se JS estiver off: mostra tudo */
  .no-js .tab-pane{display:block !important}
  .no-js .tabs{display:none}
  @media (max-width:700px){.tab-btn{font-size:12px;padding:8px 10px}}
  /* ============== INSIGHTS DE ESTUDO ============== */
  .insight-list{display:flex;flex-direction:column;gap:18px}
  .insight-card{padding:18px 20px;background:var(--surface2);border-radius:12px;border-left:3px solid var(--accent)}
  .insight-head{margin-bottom:12px}
  .insight-meta{display:flex;align-items:center;gap:10px;margin-bottom:6px;flex-wrap:wrap}
  .insight-date{font-family:monospace;font-size:12px;color:var(--muted);font-weight:600}
  .insight-title{margin:0 0 8px;font-size:18px;font-weight:700;color:var(--text);line-height:1.3}
  .insight-tags{display:flex;flex-wrap:wrap;gap:6px;margin-top:4px}
  .insight-tag{display:inline-block;padding:3px 10px;background:var(--surface);border-radius:12px;font-size:11px;color:var(--accent);font-weight:500;border:1px solid var(--border)}
  .insight-resumo{margin:8px 0;padding-left:20px;line-height:1.6;color:var(--text)}
  .insight-resumo li{margin-bottom:5px}
  .insight-acoes{margin-top:10px;padding:8px 12px;background:var(--surface);border-radius:8px}
  .insight-acoes summary{cursor:pointer;font-weight:600;color:var(--warn);font-size:13px}
  .insight-acoes ul{margin:8px 0 4px;padding-left:18px;font-size:13px}
  .insight-acoes li{margin-bottom:3px}
  /* ============== CURVA FORWARD CBOT ============== */
  .curva-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px;margin-top:12px}
  .curva-block{padding:14px;background:var(--surface2);border-radius:10px;border-left:3px solid var(--accent)}
  .curva-head{display:flex;align-items:center;justify-content:space-between;gap:8px;flex-wrap:wrap}
  .curva-block h3{margin:0 0 4px;font-size:14px;color:var(--accent);font-weight:600}
  .curva-table{font-size:12px;width:100%}
  .curva-table th{font-size:10px}
  .curva-table td{padding:5px 6px}
  .curva-grid-4{display:flex;flex-direction:column;gap:14px;margin-top:12px}
  .curva-block-wide{padding:14px;background:var(--surface2);border-radius:10px;border-left:3px solid var(--accent)}
  .curva-block-wide h3{margin:0 0 6px;font-size:14px;color:var(--accent);font-weight:600}
  .curva-table-4{width:100%;font-size:12px}
  .curva-table-4 th{font-size:10px;text-align:center;padding:6px 4px}
  .curva-table-4 td{padding:6px 4px;text-align:center}
  @media (max-width:700px){.bio-grid{grid-template-columns:1fr}}
  .produto-card{margin-bottom:22px;padding-bottom:14px;border-bottom:1px dashed var(--border)}
  .produto-card:last-of-type{border-bottom:none;margin-bottom:0}
  .produto-card h3{margin:4px 0 12px;font-size:16px;color:var(--accent);font-weight:600}
  .fisico-serie{margin-top:12px;padding:8px 12px;background:var(--surface2);border-radius:8px}
  .fisico-serie summary{cursor:pointer;font-weight:600;color:var(--accent);padding:4px 0}
  .hist-table{width:100%;border-collapse:collapse;margin-top:10px;font-size:13px}
  .hist-table th{text-align:left;padding:6px 8px;color:var(--muted);font-weight:600;border-bottom:1px solid var(--border);text-transform:uppercase;font-size:11px;letter-spacing:.3px}
  .hist-table td{padding:6px 8px;border-bottom:1px solid var(--border)}
  .hist-table tr:last-child td{border-bottom:none}
  .hist-date{font-family:monospace;color:var(--muted)}
  .hist-val{font-family:monospace;font-weight:600}
  @media (max-width:700px){.fisico-grid{grid-template-columns:1fr}}
  .questions{list-style:none;padding:0;margin:0}
  .questions li{padding:10px 12px;background:var(--surface2);border-radius:8px;margin-bottom:6px;display:flex;align-items:flex-start;gap:10px}
  .questions .check{flex-shrink:0;width:18px;height:18px;border-radius:4px;border:2px solid var(--muted);margin-top:2px}
  .questions strong{color:var(--accent)}
  .lateness-item{display:flex;justify-content:space-between;align-items:center;padding:8px 12px;background:var(--bear-bg);border:1px solid var(--bear);border-radius:8px;margin-bottom:6px}
  .lateness-item .name{font-weight:500}
  .lateness-item .hours{color:var(--bear);font-weight:600;font-family:monospace}
  .muted-small{color:var(--muted);font-size:13px}
  footer{margin-top:48px;padding-top:20px;border-top:1px solid var(--border);color:var(--muted);font-size:12px;text-align:center}
  footer a{color:var(--accent);text-decoration:none}
  code{background:var(--surface2);padding:1px 5px;border-radius:4px;font-size:12px}
"""


if __name__ == "__main__":
    p = gerar_html()
    print(f"HTML em {p}")
