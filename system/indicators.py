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

    # ---- Índices sintéticos (Onda 2): grava o VALOR (0-100) p/ série/alertas ----
    try:
        idx = compute_indices_sinteticos(target)
        with db.connect() as conn:
            for key, metrica in (("sobra_farelo", "indice_sobra_farelo"),
                                 ("suporte_oleo", "indice_suporte_oleo")):
                v = idx.get(key, {}).get("valor")
                if v is not None:
                    conn.execute(
                        """INSERT OR REPLACE INTO dados_publicos
                           (fonte, data_referencia, tipo, commodity, metrica, valor, unidade, contexto)
                           VALUES ('indicators', ?, 'indicator', 'complexo_soja', ?, ?, '0-100', ?)""",
                        (target.isoformat(), metrica, v,
                         f"{idx[key]['label']} ({idx[key]['n_ativos']}/{idx[key]['n_aval']} condições)"),
                    )
        results["indices"] = 2
    except Exception as e:
        results["errors"].append(f"indices: {e}")

    results["total_calculados"] = len(novos)
    return results


# ============================================================
# Índices sintéticos (Onda 2) — 0-100 por CONTAGEM de condições.
# Sem pesos mágicos: cada condição é um booleano claro e auditável; o índice é
# a % de condições ATIVAS sobre as AVALIÁVEIS (condição sem dado = None, não conta).
# ============================================================

def _banda_sobra(v: int) -> tuple[str, str]:
    """Sobra de farelo: alto = mais pressão baixista no farelo."""
    if v <= 25:
        return "sem sobra relevante", "bull"      # pouca pressão = sustenta farelo
    if v <= 50:
        return "pressão moderada", "warn"
    if v <= 75:
        return "sobra relevante", "bear"
    return "forte pressão baixista no farelo", "bear"


def _banda_suporte(v: int) -> tuple[str, str]:
    """Suporte do óleo: alto = óleo mais sustentado (bull óleo)."""
    if v <= 25:
        return "óleo sem suporte", "bear"
    if v <= 50:
        return "suporte fraco", "warn"
    if v <= 75:
        return "suporte relevante", "bull"
    return "óleo domina o crush", "bull"


def _montar_indice(condicoes: list, banda_fn) -> dict:
    avaliaveis = [c for c in condicoes if c[1] is not None]
    ativos = [c for c in avaliaveis if c[1]]
    valor = round(100.0 * len(ativos) / len(avaliaveis)) if avaliaveis else None
    if valor is None:
        label, vies = "dados insuficientes", "neutral"
    else:
        label, vies = banda_fn(valor)
    return {"valor": valor, "label": label, "vies": vies,
            "n_ativos": len(ativos), "n_aval": len(avaliaveis), "condicoes": condicoes}


def compute_indices_sinteticos(target: date | None = None) -> dict:
    """Índice de Sobra de Farelo + Índice de Suporte do Óleo (0-100, contagem de
    condições). Lê o último valor de cada componente já no DB. Retorna o detalhe
    (condições ON/OFF) pra auditar no HTML — não inventa peso."""
    target = target or date.today()
    iso = target.isoformat()
    with db.connect() as conn:
        def latest(fonte, commodity, metrica):
            r = conn.execute(
                "SELECT valor FROM dados_publicos WHERE fonte=? AND commodity=? AND metrica=? "
                "AND valor IS NOT NULL AND data_referencia<=? ORDER BY data_referencia DESC LIMIT 1",
                (fonte, commodity, metrica, iso)).fetchone()
            return r["valor"] if r else None

        def abiove_mes(commodity, metrica):
            # ABIOVE projeta por mês (datas futuras) — pega o mês do target, senão o mais próximo
            r = conn.execute(
                "SELECT valor FROM dados_publicos WHERE fonte='abiove' AND commodity=? AND metrica=? "
                "AND strftime('%Y-%m', data_referencia)=? AND valor IS NOT NULL LIMIT 1",
                (commodity, metrica, target.strftime("%Y-%m"))).fetchone()
            if r:
                return r["valor"]
            r = conn.execute(
                "SELECT valor FROM dados_publicos WHERE fonte='abiove' AND commodity=? AND metrica=? "
                "AND valor IS NOT NULL ORDER BY ABS(julianday(data_referencia)-julianday(?)) LIMIT 1",
                (commodity, metrica, iso)).fetchone()
            return r["valor"] if r else None

        def abiove_avg(commodity, metrica):
            rows = conn.execute(
                "SELECT valor FROM dados_publicos WHERE fonte='abiove' AND commodity=? AND metrica=? "
                "AND valor IS NOT NULL", (commodity, metrica)).fetchall()
            vals = [r["valor"] for r in rows]
            return sum(vals) / len(vals) if vals else None

        crush = latest("indicators", "complexo_soja", "crush_margin_usd_bu")
        oil_share = latest("indicators", "complexo_soja", "oil_share_pct")
        bio_margem = latest("indicators", "biodiesel_us", "margem_usd_galao")
        ho = latest("cme_cbot", "heating_oil_cbot", "fechamento")
        premio_far = latest("nag_fisico", "farelo_paranagua", "premio_usd_sht")
        rin = pu.get_param("rin_d4")
        rin_v = rin["valor"] if rin else None
        esmag_mes = abiove_mes("soja_brasil", "esmagamento")
        esmag_avg = abiove_avg("soja_brasil", "esmagamento")
        far_fim, far_ini = abiove_mes("farelo_brasil", "estoque_final"), abiove_mes("farelo_brasil", "estoque_inicial")
        ole_fim, ole_ini = abiove_mes("oleo_brasil", "estoque_final"), abiove_mes("oleo_brasil", "estoque_inicial")

    cond_sobra = [
        ("Crush margin alto (esmagadora roda full)",
         (crush >= 2.0) if crush is not None else None,
         f"{crush:.2f} USD/bu" if crush is not None else "sem dado"),
        ("Oil share alto (farelo vira sobra)",
         (oil_share >= 50) if oil_share is not None else None,
         f"{oil_share:.1f}%" if oil_share is not None else "sem dado"),
        ("Esmagamento BR acima da média",
         (esmag_mes > esmag_avg) if (esmag_mes is not None and esmag_avg) else None,
         f"{esmag_mes:.0f} vs média {esmag_avg:.0f} mil t" if (esmag_mes is not None and esmag_avg) else "sem ABIOVE"),
        ("Prêmio export farelo fraco (não disputa)",
         (premio_far <= 5) if premio_far is not None else None,
         f"{premio_far:.2f} US$/sht" if premio_far is not None else "sem dado"),
        ("Estoque de farelo subindo (acumula)",
         (far_fim > far_ini) if (far_fim is not None and far_ini is not None) else None,
         f"fim {far_fim:.0f} vs ini {far_ini:.0f} mil t" if (far_fim is not None and far_ini is not None) else "sem ABIOVE"),
    ]
    cond_sup = [
        ("Oil share alto (óleo manda no crush)",
         (oil_share >= 50) if oil_share is not None else None,
         f"{oil_share:.1f}%" if oil_share is not None else "sem dado"),
        ("Margem biodiesel positiva",
         (bio_margem > 0) if bio_margem is not None else None,
         f"{bio_margem:.2f} US$/gal" if bio_margem is not None else "sem dado"),
        ("RIN D4 firme (≥1,5)",
         (rin_v >= 1.5) if rin_v is not None else None,
         f"{rin_v:.2f}" if rin_v is not None else "sem dado"),
        ("Estoque de óleo caindo (aperta)",
         (ole_fim < ole_ini) if (ole_fim is not None and ole_ini is not None) else None,
         f"fim {ole_fim:.0f} vs ini {ole_ini:.0f} mil t" if (ole_fim is not None and ole_ini is not None) else "sem ABIOVE"),
        ("Heating oil firme (≥3,0)",
         (ho >= 3.0) if ho is not None else None,
         f"{ho:.2f} US$/gal" if ho is not None else "sem dado"),
    ]
    return {"sobra_farelo": _montar_indice(cond_sobra, _banda_sobra),
            "suporte_oleo": _montar_indice(cond_sup, _banda_suporte)}


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
