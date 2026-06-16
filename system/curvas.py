"""Gestão de curvas de predição (StoneX manual + Claude heurístico).

Coexiste com a curva CBOT REAL (que vive em dados_publicos via cme_cbot).
Aqui ficam APENAS as curvas indicativas/preditivas:

  - fonte='stonex': cotação indicativa do consultor (input manual)
  - fonte='claude': heurística automática auditável (gerada por claude_forecast)

A curva CBOT real é o benchmark; estas duas são leituras sobrepostas.
A "curva média" é calculada on-the-fly no HTML, não armazenada.

CLI:
    python main.py curva set stonex --produto oleo --venc N26 --valor 72.5 --fonte "Fabio call 25mai"
    python main.py curva list                              # lista todas
    python main.py curva list --fonte stonex --commodity oleo_cbot
    python main.py curva generate                          # roda heurística Claude
    python main.py curva delete --id 42

Códigos de vencimento (CME): N26=jul/26, Q26=ago/26, U26=set/26, V26=out/26,
                              X26=nov/26, Z26=dez/26, F27=jan/27, H27=mar/27
"""
import json
from datetime import date
import db


COMMODITY_ALIASES = {
    "soja": "soja_cbot",
    "farelo": "farelo_cbot",
    "oleo": "oleo_cbot",
    "oleo_soja": "oleo_cbot",
    "óleo": "oleo_cbot",
    "soja_cbot": "soja_cbot",
    "farelo_cbot": "farelo_cbot",
    "oleo_cbot": "oleo_cbot",
}

FONTES_VALIDAS = ["stonex", "claude"]


def _normaliza_commodity(s: str) -> str:
    return COMMODITY_ALIASES.get(s.lower(), s.lower())


def _get_cbot_valor(commodity: str, vencimento: str) -> float | None:
    """Lê o valor CBOT real do mesmo vencimento (pra calcular ajuste %)."""
    with db.connect() as conn:
        cur = conn.execute(
            """
            SELECT valor FROM dados_publicos
            WHERE fonte='cme_cbot' AND commodity=? AND metrica=?
            ORDER BY data_referencia DESC LIMIT 1
            """,
            (commodity, f"fechamento_{vencimento}"),
        )
        row = cur.fetchone()
        return row["valor"] if row else None


def set_curva(
    fonte: str,
    commodity: str,
    vencimento: str,
    valor: float,
    data_ref: date | None = None,
    observacao: str | None = None,
    fonte_detalhe: str | None = None,
    razoes: list[str] | None = None,
) -> int:
    """Insere ou atualiza valor de uma curva (StoneX ou Claude)."""
    if fonte not in FONTES_VALIDAS:
        raise ValueError(f"fonte inválida '{fonte}'. Use: {FONTES_VALIDAS}")
    commodity = _normaliza_commodity(commodity)
    data_ref = data_ref or date.today()
    vencimento = vencimento.upper()

    cbot_real = _get_cbot_valor(commodity, vencimento)
    ajuste_pct = ((valor - cbot_real) / cbot_real) * 100 if cbot_real else None
    razoes_json = json.dumps(razoes, ensure_ascii=False) if razoes else None

    with db.connect() as conn:
        conn.execute(
            """
            INSERT INTO curvas_predicao
                (data_geracao, fonte, commodity, vencimento, valor,
                 ajuste_vs_cbot_pct, razoes, observacao, fonte_detalhe)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(data_geracao, fonte, commodity, vencimento) DO UPDATE SET
                valor=excluded.valor,
                ajuste_vs_cbot_pct=excluded.ajuste_vs_cbot_pct,
                razoes=excluded.razoes,
                observacao=excluded.observacao,
                fonte_detalhe=excluded.fonte_detalhe,
                criado_em=CURRENT_TIMESTAMP
            """,
            (data_ref.isoformat(), fonte, commodity, vencimento, valor,
             ajuste_pct, razoes_json, observacao, fonte_detalhe),
        )
        cur = conn.execute(
            "SELECT id FROM curvas_predicao WHERE data_geracao=? AND fonte=? AND commodity=? AND vencimento=?",
            (data_ref.isoformat(), fonte, commodity, vencimento),
        )
        row = cur.fetchone()
        return row["id"] if row else 0


def list_curvas(fonte: str | None = None, commodity: str | None = None,
                limite: int = 50) -> list[dict]:
    """Lista curvas mais recentes por (fonte, commodity, vencimento)."""
    sql = """
        SELECT id, data_geracao, fonte, commodity, vencimento, valor,
               ajuste_vs_cbot_pct, observacao, fonte_detalhe, razoes
        FROM curvas_predicao
        WHERE 1=1
    """
    params = []
    if fonte:
        sql += " AND fonte = ?"
        params.append(fonte)
    if commodity:
        sql += " AND commodity = ?"
        params.append(_normaliza_commodity(commodity))
    sql += " ORDER BY data_geracao DESC, fonte, commodity, vencimento LIMIT ?"
    params.append(limite)
    with db.connect() as conn:
        cur = conn.execute(sql, params)
        return [dict(r) for r in cur]


def latest_por_fonte(fonte: str, commodity: str) -> dict[str, dict]:
    """Curva mais recente de uma fonte/commodity: {vencimento: row}."""
    commodity = _normaliza_commodity(commodity)
    with db.connect() as conn:
        cur = conn.execute(
            """
            SELECT vencimento, MAX(data_geracao) as ultima
            FROM curvas_predicao
            WHERE fonte=? AND commodity=?
            GROUP BY vencimento
            """,
            (fonte, commodity),
        )
        ultimas = {r["vencimento"]: r["ultima"] for r in cur}
        out = {}
        for venc, data in ultimas.items():
            cur2 = conn.execute(
                """
                SELECT * FROM curvas_predicao
                WHERE fonte=? AND commodity=? AND vencimento=? AND data_geracao=?
                LIMIT 1
                """,
                (fonte, commodity, venc, data),
            )
            row = cur2.fetchone()
            if row:
                out[venc] = dict(row)
        return out


def delete_id(rec_id: int) -> bool:
    with db.connect() as conn:
        cur = conn.execute("DELETE FROM curvas_predicao WHERE id=?", (rec_id,))
        return cur.rowcount > 0


# ============================================================
# CLI
# ============================================================

def cli_set(args):
    fonte = args.fonte
    commodity = _normaliza_commodity(args.produto)
    venc = args.venc.upper()
    valor = float(args.valor)
    rec_id = set_curva(
        fonte, commodity, venc, valor,
        observacao=args.obs,
        fonte_detalhe=args.detalhe,
    )
    cbot = _get_cbot_valor(commodity, venc)
    aj_str = ""
    if cbot:
        ajuste = ((valor - cbot) / cbot) * 100
        sinal = "+" if ajuste > 0 else ""
        aj_str = f"  ({sinal}{ajuste:.2f}% vs CBOT {cbot:.2f})"
    print(f"OK [{fonte}] {commodity} {venc} = {valor}{aj_str}  (id #{rec_id})")


def cli_list(args):
    rows = list_curvas(fonte=args.fonte, commodity=args.commodity)
    if not rows:
        print("Sem curvas. Use 'main.py curva set' ou 'curva generate' pra criar.")
        return
    print()
    print(f"  {len(rows)} curva(s):")
    print(f"  {'ID':>4}  {'DATA':10s}  {'FONTE':7s}  {'COMMODITY':14s}  {'VENC':5s}  {'VALOR':>10s}  {'Δ CBOT':>8s}  DETALHE")
    print("  " + "-" * 100)
    for r in rows:
        ajuste = r["ajuste_vs_cbot_pct"]
        ajuste_str = f"{ajuste:+.2f}%" if ajuste is not None else "—"
        detalhe = (r["fonte_detalhe"] or "")[:30]
        print(f"  {r['id']:>4}  {r['data_geracao']:10s}  {r['fonte']:7s}  {r['commodity']:14s}  "
              f"{r['vencimento']:5s}  {r['valor']:>10.2f}  {ajuste_str:>8s}  {detalhe}")


def cli_delete(args):
    ok = delete_id(args.id)
    print(f"{'OK apagado' if ok else 'NAO encontrado'}: id #{args.id}")


def cli_generate(args):
    """Roda heurística Claude e popula curvas."""
    import claude_forecast as cf
    n = cf.gerar_e_salvar()
    print(f"OK heurística Claude rodou: {n} predições geradas/atualizadas.")
    print("Veja: python main.py curva list --fonte claude")
