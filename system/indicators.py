"""Indicadores derivados do complexo soja.

Le precos de `dados_publicos` (fonte=cme_cbot) e calcula:
- crush_margin (Board Crush)
- oil_share (% valor do oleo no crush)
- soja_brl_equiv (paridade CBOT × cambio BCB)
- oil_meal_spread (diferenca relativa entre oleo e farelo)
  (soja_milho_ratio removido em 2026-05-26 — escopo restrito ao complexo soja)
- biodiesel_us_margin (margem biodiesel americano USD/galao):
    receita = HO Chicago + 1.5 × RIN D4
    custo   = 7.5 × óleo_cents_lb/100 + custo_industrial
    margem  = receita − custo
    > Tese StoneX 25mai 2026: hoje o que sustenta o preço do óleo soja é
    a margem biodiesel via demanda RIN. Se margem cair, óleo cai.

Salva resultados em `dados_publicos` com fonte='indicators'.

Comando:
    python main.py indicators       # calcula indicadores diarios
"""
from datetime import date, timedelta
import config
import db
import params_user as pu


def far_soj_ratio_pct(farelo_usd_sht: float, soja_cents_bu: float) -> float:
    """Ratio Far/Soj — métrica central de decisão do comprador de farelo.

    Convenção idêntica à matriz crush: farelo USD/short ton ÷ (soja USD/bu
    × 33,333 bu→short ton) × 100. Zonas: <80 abundante (compra) · 80-87
    transição · >=87 apertado. Função pura — testada em tests/.
    """
    soja_usd_bu = soja_cents_bu / 100.0
    return farelo_usd_sht / (soja_usd_bu * (2000.0 / 60.0)) * 100.0


def calculate_all(target_date: date | None = None) -> dict:
    target = target_date or date.today()
    results = {"crush_margin": 0, "oil_share": 0, "soja_brl": 0, "spreads": 0, "errors": []}

    with db.connect() as conn:
        # Pegar ultimas 30 datas de fechamento CBOT (inclui Heating Oil)
        cur = conn.execute(
            """
            SELECT data_referencia, commodity, valor
            FROM dados_publicos
            WHERE fonte='cme_cbot' AND metrica='fechamento' AND tipo='preco'
              AND commodity IN ('soja_cbot','farelo_cbot','oleo_cbot','heating_oil_cbot')
              AND data_referencia >= date(?, '-30 days')
            ORDER BY data_referencia DESC
            """,
            (target.isoformat(),),
        )
        precos_por_data = {}
        for r in cur:
            d = r["data_referencia"]
            precos_por_data.setdefault(d, {})[r["commodity"]] = r["valor"]

        # Cambio BCB
        cur = conn.execute(
            """
            SELECT data_referencia, valor
            FROM dados_publicos
            WHERE fonte='bcb' AND commodity='usd_brl_ptax' AND metrica='valor'
              AND data_referencia >= date(?, '-30 days')
            ORDER BY data_referencia DESC
            """,
            (target.isoformat(),),
        )
        cambio_por_data = {r["data_referencia"]: r["valor"] for r in cur}

    novos = []

    for data_ref, precos in precos_por_data.items():
        soja = precos.get("soja_cbot")       # cents/bushel
        farelo = precos.get("farelo_cbot")   # USD/short ton
        oleo = precos.get("oleo_cbot")       # cents/lb
        # milho removido em 2026-05-26 (escopo restrito ao complexo soja)

        # ---- Crush margin (Board Crush) ----
        # Formula tradicional: (Farelo $/ton × 0.022) + (Oleo cts/lb × 11) - Soja $/bu
        # Em $/bu da soja
        if soja and farelo and oleo:
            soja_usd_bu = soja / 100  # cents to dollars
            farelo_usd_ton = farelo
            oleo_cts_lb = oleo
            crush_usd_bu = (farelo_usd_ton * 0.022) + (oleo_cts_lb * 11 / 100) - soja_usd_bu

            novos.append({
                "data_referencia": data_ref,
                "tipo": "indicator",
                "commodity": "complexo_soja",
                "metrica": "crush_margin_usd_bu",
                "valor": round(crush_usd_bu, 4),
                "unidade": "USD/bushel",
                "contexto": f"Board Crush: farelo {farelo:.2f} + oleo {oleo:.2f} − soja {soja:.2f}",
            })
            results["crush_margin"] += 1

            # ---- Oil share ----
            # % do valor do crush vindo do oleo
            valor_oleo = oleo_cts_lb * 11 / 100
            valor_farelo = farelo_usd_ton * 0.022
            valor_total = valor_oleo + valor_farelo
            if valor_total > 0:
                oil_share_pct = (valor_oleo / valor_total) * 100
                novos.append({
                    "data_referencia": data_ref,
                    "tipo": "indicator",
                    "commodity": "complexo_soja",
                    "metrica": "oil_share_pct",
                    "valor": round(oil_share_pct, 2),
                    "unidade": "%",
                    "contexto": f"valor oleo {valor_oleo:.2f} / total {valor_total:.2f}",
                })
                results["oil_share"] += 1

        # ---- Ratio Far/Soj (relação farelo/soja — MESMA convenção da matriz crush) ----
        # far_pct = farelo (USD/short ton) / (soja USD/bu × 33.333 bu→short ton)
        # Zonas: <80% farelo abundante (compra), 80-87% transição, >=87% apertado.
        # Para comprador de farelo: ratio caindo = farelo barateando vs soja = bom.
        if soja and farelo:
            far_soj_ratio = far_soj_ratio_pct(farelo, soja)
            novos.append({
                "data_referencia": data_ref,
                "tipo": "indicator",
                "commodity": "complexo_soja",
                "metrica": "far_soj_ratio_pct",
                "valor": round(far_soj_ratio, 2),
                "unidade": "%",
                "contexto": (
                    f"farelo {farelo:.2f}/sht ÷ (soja {soja:.2f}cts × 33.33) "
                    f"— <80 abundante, >=87 apertado"
                ),
            })
            results["spreads"] += 1

        # ---- Soja BR equiv (paridade CBOT × cambio) ----
        # CBOT cents/bu × 0.022046 × USD/BRL = BRL/saca60kg
        # (1 saca 60kg = 2.2046 bu; fator = 2.2046/100)
        usd_brl = cambio_por_data.get(data_ref)
        # se nao tem cambio no mesmo dia, usar ultimo disponivel
        if not usd_brl:
            for dias_atras in range(1, 5):
                dt = (date.fromisoformat(data_ref) - timedelta(days=dias_atras)).isoformat()
                if dt in cambio_por_data:
                    usd_brl = cambio_por_data[dt]
                    break

        if soja and usd_brl:
            soja_brl_saca = (soja * 0.022046) * usd_brl
            novos.append({
                "data_referencia": data_ref,
                "tipo": "indicator",
                "commodity": "soja_paridade_br",
                "metrica": "brl_saca_paridade",
                "valor": round(soja_brl_saca, 2),
                "unidade": "BRL/saca60kg",
                "contexto": f"CBOT {soja:.2f} cts × USD/BRL {usd_brl:.4f} (sem basis)",
            })
            results["soja_brl"] += 1

        # ---- Spread oil/meal (relativo) ----
        if farelo and oleo:
            # Spread = (oleo cts/lb × 11) − (farelo $/ton × 0.022) em $/bu equivalente
            spread_oil_meal = (oleo * 11 / 100) - (farelo * 0.022)
            novos.append({
                "data_referencia": data_ref,
                "tipo": "indicator",
                "commodity": "complexo_soja",
                "metrica": "oil_meal_spread_usd_bu",
                "valor": round(spread_oil_meal, 4),
                "unidade": "USD/bushel",
                "contexto": "Oleo - Farelo (positivo = oleo manda)",
            })
            results["spreads"] += 1

        # ---- Margem biodiesel americano (USD/galao) ----
        # Tese StoneX: principal driver atual do preço do óleo soja.
        # receita = HO Chicago + 1.5 × RIN D4
        # custo   = 7.5 × óleo cents_lb/100 + custo_industrial
        ho = precos.get("heating_oil_cbot")  # USD/galão
        if ho and oleo:
            rin = pu.get_param("rin_d4")
            custo_ind = pu.get_param("custo_industrial_biodiesel_us")
            yield_oleo = pu.get_param("yield_oleo_lb_per_galao")
            yield_rin = pu.get_param("yield_rin_per_galao")
            if all([rin, custo_ind, yield_oleo, yield_rin]):
                receita = ho + yield_rin["valor"] * rin["valor"]
                custo_oleo = yield_oleo["valor"] * (oleo / 100.0)
                custo_total = custo_oleo + custo_ind["valor"]
                margem = receita - custo_total
                novos.append({
                    "data_referencia": data_ref,
                    "tipo": "indicator",
                    "commodity": "biodiesel_us",
                    "metrica": "margem_usd_galao",
                    "valor": round(margem, 4),
                    "unidade": "USD/galão",
                    "contexto": (
                        f"receita {receita:.2f} (HO {ho:.2f} + 1.5×RIN {rin['valor']:.2f}) "
                        f"− custo {custo_total:.2f} (óleo {custo_oleo:.2f} + ind {custo_ind['valor']:.2f})"
                    ),
                })
                # Tambem grava componentes pra usar no HTML
                novos.append({
                    "data_referencia": data_ref, "tipo": "indicator",
                    "commodity": "biodiesel_us", "metrica": "receita_usd_galao",
                    "valor": round(receita, 4), "unidade": "USD/galão",
                    "contexto": f"HO {ho:.2f} + 1.5×RIN {rin['valor']:.2f}",
                })
                novos.append({
                    "data_referencia": data_ref, "tipo": "indicator",
                    "commodity": "biodiesel_us", "metrica": "custo_oleo_usd_galao",
                    "valor": round(custo_oleo, 4), "unidade": "USD/galão",
                    "contexto": f"7.5 lb × óleo {oleo:.2f} cts/lb",
                })
                results["spreads"] += 3

    # Save em batch
    with db.connect() as conn:
        for r in novos:
            try:
                conn.execute(
                    """
                    INSERT OR REPLACE INTO dados_publicos
                    (fonte, data_referencia, tipo, commodity, metrica, valor, unidade, contexto)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        "indicators",
                        r["data_referencia"],
                        r["tipo"],
                        r["commodity"],
                        r["metrica"],
                        r["valor"],
                        r["unidade"],
                        r["contexto"],
                    ),
                )
            except Exception as e:
                results["errors"].append(str(e))

    results["total_calculados"] = len(novos)
    return results


if __name__ == "__main__":
    out = calculate_all()
    print(f"Indicadores calculados:")
    print(f"  Crush margin: {out['crush_margin']}")
    print(f"  Oil share: {out['oil_share']}")
    print(f"  Soja BRL paridade: {out['soja_brl']}")
    print(f"  Spreads: {out['spreads']}")
    print(f"  Total: {out.get('total_calculados', 0)}")
    if out["errors"]:
        print(f"  Erros: {len(out['errors'])}")
