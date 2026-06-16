"""Heurísticas auditáveis pra gerar a "curva Claude" sobre dados do projeto.

Aplica regras EXPLÍCITAS em cima da curva CBOT real, ajustando ± por
vencimento conforme:
  - Margem biodiesel americano (driver óleo)
  - Tag de insights ativos (tese B16, esmagamento, etc)
  - Far/Soj ratio atual (driver farelo)
  - Posição na curva (horizonte 6m+ recebe ajustes maiores que front-month)

NÃO É RECOMENDAÇÃO. É leitura sistemática que serve como TERCEIRO PONTO DE
COMPARAÇÃO com o mercado real (CBOT) e com a opinião do consultor (StoneX).

Toda heurística aqui é AUDITÁVEL — você lê o código e contesta a regra.
A função `gerar_e_salvar` produz a curva e grava `razoes` (lista de strings)
junto com cada valor, pra você ver POR QUE Claude pegou cada ajuste.

Versão atual: v1 (2026-05-26).
"""
from datetime import date
import db
import insights as ins_mod
from curvas import set_curva, _get_cbot_valor


VERSAO = "heuristica_v1_2026-05-26"


def _get_indicador_atual(commodity: str, metrica: str) -> float | None:
    """Lê último valor de um indicador derivado em dados_publicos."""
    with db.connect() as conn:
        cur = conn.execute(
            """
            SELECT valor FROM dados_publicos
            WHERE fonte='indicators' AND commodity=? AND metrica=?
            ORDER BY data_referencia DESC LIMIT 1
            """,
            (commodity, metrica),
        )
        row = cur.fetchone()
        return row["valor"] if row else None


def _tags_insights_ativos() -> set[str]:
    """Conjunto de tags presentes em insights com status=ativa."""
    tags = set()
    for ins in ins_mod.list_insights():
        if ins.get("status") == "ativa":
            for t in ins.get("tags", []):
                tags.add(t.lower())
    return tags


def _curva_cbot_vigente(commodity: str) -> list[tuple[str, float]]:
    """Retorna [(vencimento, valor)] da curva CBOT atual pro commodity."""
    with db.connect() as conn:
        cur = conn.execute(
            """
            SELECT metrica, valor, MAX(data_referencia) as ultima
            FROM dados_publicos
            WHERE fonte='cme_cbot' AND commodity=?
              AND metrica LIKE 'fechamento_%' AND metrica != 'fechamento'
            GROUP BY metrica
            ORDER BY metrica
            """,
            (commodity,),
        )
        out = []
        for r in cur:
            venc = r["metrica"].replace("fechamento_", "")
            out.append((venc, r["valor"]))
        return out


def _peso_horizonte(idx: int, total: int) -> float:
    """Peso crescente conforme o vencimento se afasta do front-month.

    Heurística: ajustes Claude têm MENOS força no front-month (que é
    chumbado no mercado real) e MAIS força nos vencimentos distantes
    (onde há mais incerteza e espaço pra tese se materializar).

    Ex: total=6 vencs → pesos [0.2, 0.4, 0.6, 0.8, 1.0, 1.2]
    """
    if total <= 1:
        return 1.0
    return 0.2 + (idx / (total - 1)) * 1.0


# ============================================================
# Regras por commodity
# ============================================================

def _regras_oleo(cbot_valor: float, idx_venc: int, total_vencs: int,
                tags_ativas: set, margem_bio: float | None) -> tuple[float, list[str]]:
    """Retorna (ajuste_pct, razoes) pra óleo de soja."""
    ajuste = 0.0
    razoes = []
    peso = _peso_horizonte(idx_venc, total_vencs)

    # Regra 1: Margem biodiesel americano (driver principal segundo Fabio)
    if margem_bio is not None:
        if margem_bio < 0:
            ajuste -= 4.0 * peso
            razoes.append(f"margem biodiesel NEGATIVA (${margem_bio:.2f}/gal) → óleo CBOT pressionado a cair")
        elif margem_bio < 0.5:
            ajuste -= 2.0 * peso
            razoes.append(f"margem biodiesel apertada (${margem_bio:.2f}/gal < $0.5) → óleo deve ceder")
        elif margem_bio >= 1.5:
            ajuste += 1.0 * peso
            razoes.append(f"margem biodiesel confortável (${margem_bio:.2f}/gal) → óleo sustentado")

    # Regra 2: Tese B16 ativa → demanda BR puxa global indiretamente
    if "b16" in tags_ativas or "biodiesel" in tags_ativas:
        ajuste += 0.8 * peso
        razoes.append("tese B16/biodiesel ativa → demanda interna BR aperta oferta global")

    # Regra 3: Esmagamento BR alto → mais óleo gerado → bearish global
    if "esmagamento" in tags_ativas:
        ajuste -= 0.5 * peso
        razoes.append("esmagamento BR em recorde → mais óleo na oferta global")

    return ajuste, razoes


def _regras_farelo(cbot_valor: float, idx_venc: int, total_vencs: int,
                   tags_ativas: set) -> tuple[float, list[str]]:
    """Retorna (ajuste_pct, razoes) pra farelo de soja."""
    ajuste = 0.0
    razoes = []
    peso = _peso_horizonte(idx_venc, total_vencs)

    # Regra 1: Esmagamento BR recorde → mais farelo no mercado → pressão pra baixo
    if "esmagamento" in tags_ativas:
        ajuste -= 1.5 * peso
        razoes.append("esmagamento BR recorde → mais farelo no mercado")

    # Regra 2: Tese B16 (acelera esmagamento) reforça queda do farelo
    if "b16" in tags_ativas:
        ajuste -= 1.0 * peso
        razoes.append("B16 acelera esmagamento → mais farelo (cadeia)")

    return ajuste, razoes


def _regras_soja(cbot_valor: float, idx_venc: int, total_vencs: int,
                 tags_ativas: set) -> tuple[float, list[str]]:
    """Retorna (ajuste_pct, razoes) pra soja em grão.

    Heurística conservadora: soja CBOT é direcionada por demanda global
    (China) + S/U americano. Sem indicador forte que justifique divergência,
    Claude segue CBOT.
    """
    ajuste = 0.0
    razoes = ["heurística conservadora: soja segue CBOT (sem driver disruptivo nos insights)"]
    return ajuste, razoes


# ============================================================
# Função principal
# ============================================================

def gerar_e_salvar(data_ref: date | None = None) -> int:
    """Gera curva Claude pros 3 produtos do complexo soja e grava no DB.

    Retorna número de predições geradas/atualizadas.
    """
    data_ref = data_ref or date.today()
    tags_ativas = _tags_insights_ativos()
    margem_bio = _get_indicador_atual("biodiesel_us", "margem_usd_galao")

    total = 0
    for commodity in ["soja_cbot", "farelo_cbot", "oleo_cbot"]:
        cbot_curva = _curva_cbot_vigente(commodity)
        if not cbot_curva:
            continue
        total_vencs = len(cbot_curva)

        for idx, (venc, valor_cbot) in enumerate(cbot_curva):
            if commodity == "soja_cbot":
                ajuste_pct, razoes = _regras_soja(valor_cbot, idx, total_vencs, tags_ativas)
            elif commodity == "farelo_cbot":
                ajuste_pct, razoes = _regras_farelo(valor_cbot, idx, total_vencs, tags_ativas)
            elif commodity == "oleo_cbot":
                ajuste_pct, razoes = _regras_oleo(valor_cbot, idx, total_vencs, tags_ativas, margem_bio)
            else:
                continue

            valor_claude = valor_cbot * (1 + ajuste_pct / 100)
            set_curva(
                fonte="claude",
                commodity=commodity,
                vencimento=venc,
                valor=round(valor_claude, 2),
                data_ref=data_ref,
                fonte_detalhe=VERSAO,
                razoes=razoes,
                observacao=f"ajuste {ajuste_pct:+.2f}% vs CBOT ({len(razoes)} razão(ões))",
            )
            total += 1

    return total


if __name__ == "__main__":
    n = gerar_e_salvar()
    print(f"Curva Claude v1 gerada: {n} predições")
