"""Gestao do mercado fisico BR — input manual e leitura.

Praças padrão acompanhadas:
- rancharia_sp   → compra no balcão (interior oeste paulista)
- paranagua_pr   → exportação FOB (porto de referência)

Outras praças (futuro: rondonopolis_mt, sorriso_mt, passo_fundo_rs etc) podem
ser adicionadas sem mudança de schema — basta passar a string em --praca.

Fluxo:
  python main.py fisico add                    # interativo, default hoje + Rancharia + Paranaguá
  python main.py fisico add --praca paranagua_pr --valor 145.50
  python main.py fisico list                   # últimos 14 dias
  python main.py fisico import precos.csv      # bulk
  python main.py fisico delete --id 42         # apagar input errado
"""
import csv
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

import db


PRACAS_PADRAO = {
    "rancharia_sp": {
        "nome": "Rancharia/SP",
        "tipo_padrao": "compra",
        "descricao": "Preço de compra — interior oeste paulista",
        "fonte_dica": "consultor StoneX, cooperativa local, boletim regional",
    },
    "paranagua_pr": {
        "nome": "Paranaguá/PR",
        "tipo_padrao": "compra",
        "descricao": "Preço de compra — porto (referência exportação)",
        "fonte_dica": "StoneX prêmio nos portos, Cepea Paranaguá, Reuters",
    },
}

PRODUTOS = ["soja", "farelo", "oleo_soja"]
TIPOS_POSICAO = ["compra", "venda", "indicador"]

# Metadata por produto: unidade canonica + label amigavel + dica de fonte
PRODUTOS_META = {
    "soja": {
        "label": "Soja em grão",
        "unidade": "sc60kg",
        "unidade_display": "R$/sc 60kg",
        "usd_unidade_display": "US$/sc 60kg",
        "exemplo": "129,50  ou  129.50",
    },
    "farelo": {
        "label": "Farelo de soja",
        "unidade": "ton",
        "unidade_display": "R$/tonelada",
        "usd_unidade_display": "US$/tonelada",
        "exemplo": "1.850  ou  1850",
    },
    "oleo_soja": {
        "label": "Óleo de soja degomado",
        "unidade": "ton",
        "unidade_display": "R$/tonelada",
        "usd_unidade_display": "US$/tonelada",
        "exemplo": "5.200  ou  5200",
    },
}


def unidade_de(produto: str) -> str:
    return PRODUTOS_META.get(produto, {}).get("unidade", "sc60kg")


def _parse_num(s: str) -> float | None:
    """Parse numero BR ou US. Retorna None se vazio."""
    if not s:
        return None
    s = str(s).strip().replace(" ", "")
    if not s:
        return None
    # Formato BR: 1.234,56 → 1234.56
    if "," in s and "." in s:
        s = s.replace(".", "").replace(",", ".")
    elif "," in s:
        s = s.replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None


def add_preco(
    data_ref: date,
    praca: str,
    valor_brl_sc: float,
    produto: str = "soja",
    tipo_posicao: str | None = None,
    valor_usd_sc: float | None = None,
    observacao: str | None = None,
    unidade_medida: str | None = None,
) -> int:
    """Insere ou atualiza preço físico. Retorna id da linha.

    Apesar do nome legado `valor_brl_sc`/`valor_usd_sc`, esses campos guardam o
    valor na UNIDADE CANÔNICA do produto:
      - soja      → sc60kg
      - farelo    → ton
      - oleo_soja → ton
    A unidade efetiva fica em `unidade_medida` (deduzida se não passada).
    """
    tipo = tipo_posicao or PRACAS_PADRAO.get(praca, {}).get("tipo_padrao", "compra")
    unidade = unidade_medida or unidade_de(produto)
    with db.connect() as conn:
        conn.execute(
            """
            INSERT INTO precos_fisicos
                (data, praca, produto, tipo_posicao, valor_brl_sc, valor_usd_sc, unidade_medida, observacao)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(data, praca, produto, tipo_posicao) DO UPDATE SET
                valor_brl_sc=excluded.valor_brl_sc,
                valor_usd_sc=excluded.valor_usd_sc,
                unidade_medida=excluded.unidade_medida,
                observacao=excluded.observacao,
                criado_em=CURRENT_TIMESTAMP
            """,
            (data_ref.isoformat(), praca, produto, tipo, valor_brl_sc, valor_usd_sc, unidade, observacao),
        )
        cur = conn.execute(
            "SELECT id FROM precos_fisicos WHERE data=? AND praca=? AND produto=? AND tipo_posicao=?",
            (data_ref.isoformat(), praca, produto, tipo),
        )
        row = cur.fetchone()
        return row["id"] if row else 0


def list_recent(days: int = 14) -> list[dict]:
    """Retorna preços dos últimos N dias, ordenados por data DESC."""
    inicio = (date.today() - timedelta(days=days)).isoformat()
    with db.connect() as conn:
        cur = conn.execute(
            """
            SELECT id, data, praca, produto, tipo_posicao,
                   valor_brl_sc, valor_usd_sc, observacao, criado_em
            FROM precos_fisicos
            WHERE data >= ?
            ORDER BY data DESC, praca
            """,
            (inicio,),
        )
        return [dict(r) for r in cur]


def latest_per_praca(produto: str = "soja", tipo_posicao: str = "compra") -> dict[str, dict]:
    """Retorna preço mais recente por praça filtrado por tipo.

    Default: tipo='compra' (o input manual do usuario).
    Use tipo='indicador' pra pegar o preço de suporte automático (ex: CEPEA).
    """
    out = {}
    with db.connect() as conn:
        cur = conn.execute(
            """
            SELECT praca, MAX(data) as ultima_data
            FROM precos_fisicos
            WHERE produto = ? AND tipo_posicao = ?
            GROUP BY praca
            """,
            (produto, tipo_posicao),
        )
        pracas = {r["praca"]: r["ultima_data"] for r in cur}

        for praca, data_ult in pracas.items():
            cur = conn.execute(
                """
                SELECT * FROM precos_fisicos
                WHERE praca=? AND produto=? AND tipo_posicao=? AND data=?
                LIMIT 1
                """,
                (praca, produto, tipo_posicao, data_ult),
            )
            row = cur.fetchone()
            if row:
                out[praca] = dict(row)
    return out


def serie_praca(praca: str, produto: str = "soja", days: int = 30,
                tipo_posicao: str | None = "compra") -> list[dict]:
    """Série temporal de uma praça.

    Default: tipo='compra' (sua compra manual).
    tipo=None retorna todos os tipos (compra + indicador).
    """
    inicio = (date.today() - timedelta(days=days)).isoformat()
    sql = """
        SELECT data, valor_brl_sc, valor_usd_sc, tipo_posicao, observacao
        FROM precos_fisicos
        WHERE praca=? AND produto=? AND data >= ?
    """
    params = [praca, produto, inicio]
    if tipo_posicao:
        sql += " AND tipo_posicao = ?"
        params.append(tipo_posicao)
    sql += " ORDER BY data DESC"
    with db.connect() as conn:
        cur = conn.execute(sql, params)
        return [dict(r) for r in cur]


def delete_id(rec_id: int) -> bool:
    with db.connect() as conn:
        cur = conn.execute("DELETE FROM precos_fisicos WHERE id=?", (rec_id,))
        return cur.rowcount > 0


def historico(praca: str | None = None, days: int | None = None) -> list[dict]:
    """Le log de auditoria completo (INSERT/UPDATE_OLD/UPDATE_NEW/DELETE)."""
    sql = """
        SELECT id, registro_id, data, praca, produto, tipo_posicao,
               valor_brl_sc, valor_usd_sc, observacao, acao, capturado_em
        FROM precos_fisicos_historico
        WHERE 1=1
    """
    params = []
    if praca:
        sql += " AND praca = ?"
        params.append(praca)
    if days:
        sql += " AND date(capturado_em) >= date('now', ?)"
        params.append(f"-{days} days")
    sql += " ORDER BY capturado_em, id"
    with db.connect() as conn:
        cur = conn.execute(sql, params)
        return [dict(r) for r in cur]


def export_to_csv(
    path: Path,
    days: int | None = None,
    incluir_historico: bool = False,
) -> dict:
    """Exporta serie temporal para CSV.

    Modo default: snapshot atual (precos_fisicos) ordenado por data DESC.
    Modo incluir_historico=True: log completo de auditoria (precos_fisicos_historico).
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    if incluir_historico:
        rows = historico(days=days)
        cols = ["capturado_em", "acao", "registro_id", "data", "praca",
                "produto", "tipo_posicao", "valor_brl_sc", "valor_usd_sc", "observacao"]
    else:
        rows = list_recent(days=days or 3650)  # default 10 anos = "tudo"
        cols = ["id", "data", "praca", "produto", "tipo_posicao",
                "valor_brl_sc", "valor_usd_sc", "observacao", "criado_em"]

    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=cols)
        writer.writeheader()
        for r in rows:
            writer.writerow({k: r.get(k, "") for k in cols})

    return {"path": str(path), "rows": len(rows), "modo": "historico" if incluir_historico else "ativo"}


def import_csv(path: Path) -> dict:
    """Bulk import.

    Formato CSV esperado (header obrigatório):
        data,praca,produto,tipo_posicao,valor_brl_sc,valor_usd_sc,observacao

    Campos opcionais (podem ficar vazios): produto (default 'soja'),
    tipo_posicao (auto pela praça), valor_usd_sc, observacao.
    """
    if not path.exists():
        return {"status": "erro", "msg": f"arquivo nao encontrado: {path}"}

    inserted = 0
    updated = 0
    skipped = 0
    erros = []

    with path.open("r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, start=2):  # linha 1 = header
            try:
                data_ref = datetime.fromisoformat(row["data"].strip()).date()
                praca = row["praca"].strip()
                produto = (row.get("produto") or "soja").strip() or "soja"
                tipo = (row.get("tipo_posicao") or "").strip() or None
                valor_brl = _parse_num(row.get("valor_brl_sc", ""))
                valor_usd = _parse_num(row.get("valor_usd_sc", ""))
                obs = (row.get("observacao") or "").strip() or None

                if valor_brl is None and valor_usd is None:
                    skipped += 1
                    continue

                # Conta se já existia
                tipo_final = tipo or PRACAS_PADRAO.get(praca, {}).get("tipo_padrao", "indicador")
                with db.connect() as conn:
                    cur = conn.execute(
                        "SELECT 1 FROM precos_fisicos WHERE data=? AND praca=? AND produto=? AND tipo_posicao=?",
                        (data_ref.isoformat(), praca, produto, tipo_final),
                    )
                    existia = cur.fetchone() is not None

                add_preco(data_ref, praca, valor_brl, produto, tipo, valor_usd, obs)
                if existia:
                    updated += 1
                else:
                    inserted += 1
            except Exception as e:
                erros.append(f"linha {i}: {type(e).__name__}: {e}")

    return {
        "status": "ok",
        "inserted": inserted,
        "updated": updated,
        "skipped": skipped,
        "erros": erros,
    }


# ============================================================
# CLI interativa
# ============================================================

def _input(prompt: str, default: str | None = None) -> str:
    if default:
        prompt = f"{prompt} [{default}]: "
    else:
        prompt = f"{prompt}: "
    try:
        s = input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print()
        sys.exit(1)
    return s or (default or "")


def cli_add_interactive(args):
    """Modo interativo: pra cada praça, pergunta os 3 produtos (soja/farelo/óleo)."""
    print()
    print("=" * 70)
    print("  Commodities Radar — Input de PREÇOS DE COMPRA do complexo soja")
    print("=" * 70)
    print()
    print("  Vamos registrar os preços de COMPRA em 2 praças × 3 produtos:")
    print()
    print("    Praças:")
    print("      • Rancharia/SP  → compra no interior oeste paulista")
    print("      • Paranaguá/PR  → compra no porto (referência exportação)")
    print()
    print("    Produtos (cada um na sua unidade):")
    print("      • Soja em grão            — R$/saca 60kg   (ex: 129,50)")
    print("      • Farelo de soja          — R$/tonelada    (ex: 1.850 ou 1850)")
    print("      • Óleo de soja degomado   — R$/tonelada    (ex: 5.200 ou 5200)")
    print()
    print("    Cotação em US$ (opcional, só Paranaguá): ajuda a calcular basis vs CBOT.")
    print()
    print("  Como o sistema usa esses números:")
    print("    Calcula o PRÊMIO físico (preço de compra − paridade CBOT na unidade certa).")
    print("    Compara com indicador CEPEA quando houver. Mostra spread Paranaguá-Rancharia.")
    print("    Tudo grava no histórico imutável (audit preservado, mesmo se editar depois).")
    print()
    print("  ENTER pula qualquer campo. Pode reentrar depois com:")
    print("    python main.py fisico add --praca paranagua_pr --produto farelo --valor 1850")
    print()
    print("-" * 70)

    # Data
    hoje = date.today().isoformat()
    print()
    print("  Em que DATA são essas cotações?")
    print("    (Enter pra usar hoje; ou YYYY-MM-DD pra backfill de dia anterior)")
    data_str = _input("  Data", hoje)
    try:
        data_ref = datetime.fromisoformat(data_str).date()
    except ValueError:
        print(f"  [ERRO] Data inválida: '{data_str}' (esperado YYYY-MM-DD)")
        return
    print(f"  → data registrada: {data_ref.isoformat()}")

    # Loop pelas praças padrão × 3 produtos
    inseridos = []
    for praca_slug, meta_praca in PRACAS_PADRAO.items():
        print()
        print("=" * 70)
        print(f"  PRAÇA: {meta_praca['nome']}")
        print(f"  {meta_praca['descricao']}")
        print(f"  Fonte típica: {meta_praca.get('fonte_dica', '—')}")
        print("=" * 70)

        for produto_slug, meta_prod in PRODUTOS_META.items():
            print()
            print(f"  >> {meta_prod['label']}  ({meta_prod['unidade_display']})")
            valor_str = _input(
                f"     Preço de compra ({meta_prod['unidade_display']}) — Enter pra pular"
            )
            if not valor_str:
                print(f"     [pulado] {meta_prod['label']} em {meta_praca['nome']}")
                continue
            valor_brl = _parse_num(valor_str)
            if valor_brl is None:
                print(f"     [ERRO] Valor inválido: '{valor_str}'. Ex: {meta_prod['exemplo']}")
                continue

            # USD opcional só pra Paranaguá em todos os produtos
            valor_usd = None
            if praca_slug == "paranagua_pr":
                valor_usd_str = _input(
                    f"     Preço {meta_prod['usd_unidade_display']} — Enter pra pular"
                )
                valor_usd = _parse_num(valor_usd_str) if valor_usd_str else None
                if valor_usd_str and valor_usd is None:
                    print(f"     [aviso] USD inválido '{valor_usd_str}', ignorado")

            obs = _input("     Observação (fonte/contexto) — Enter pra deixar vazio")

            rec_id = add_preco(
                data_ref, praca_slug, valor_brl,
                produto=produto_slug,
                valor_usd_sc=valor_usd,
                observacao=obs or None,
            )
            inseridos.append({
                "praca": praca_slug,
                "produto": produto_slug,
                "brl": valor_brl,
                "usd": valor_usd,
                "unidade": meta_prod["unidade_display"],
                "id": rec_id,
            })
            usd_part = f"  /  US$ {valor_usd:,.2f}" if valor_usd else ""
            print(f"     ✓ gravado: {meta_prod['label']} = R$ {valor_brl:,.2f} ({meta_prod['unidade_display']}){usd_part}  (id #{rec_id})")

    # Resumo
    print()
    print("=" * 70)
    if not inseridos:
        print("  Nada inserido nessa sessão.")
    else:
        print(f"  ✓ {len(inseridos)} preço(s) gravado(s) em {data_ref.isoformat()}:")
        for r in inseridos:
            praca_nome = PRACAS_PADRAO[r["praca"]]["nome"]
            prod_label = PRODUTOS_META[r["produto"]]["label"]
            usd_part = f"  /  US$ {r['usd']:,.2f}" if r["usd"] else ""
            print(f"     • {praca_nome:18s} {prod_label:24s} R$ {r['brl']:,.2f} ({r['unidade']}){usd_part}")

        # Spread Paranaguá − Rancharia por produto
        print()
        for produto_slug, meta_prod in PRODUTOS_META.items():
            pr = next((r["brl"] for r in inseridos if r["praca"] == "paranagua_pr" and r["produto"] == produto_slug), None)
            rc = next((r["brl"] for r in inseridos if r["praca"] == "rancharia_sp" and r["produto"] == produto_slug), None)
            if pr is not None and rc is not None:
                spread = pr - rc
                sinal = "+" if spread >= 0 else ""
                obs_spread = "(esperado: frete + margem)" if spread > 0 else "(INVERTIDO — confira)"
                print(f"     Spread {meta_prod['label']} (Paranaguá − Rancharia): {sinal}R$ {spread:,.2f} ({meta_prod['unidade_display']})  {obs_spread}")

    print()
    print("  Próximos passos:")
    print("    Ver histórico:        python main.py fisico list --days 14")
    print("    Auditoria completa:   python main.py fisico historico")
    print("    Apagar erro:          python main.py fisico delete --id N")
    print("    Regerar HTML diário:  python main.py run")
    print("=" * 70)


def cli_add_flag(args):
    """Modo não-interativo via flags."""
    data_ref = (
        datetime.fromisoformat(args.data).date() if args.data else date.today()
    )
    produto = args.produto or "soja"
    meta = PRODUTOS_META.get(produto, PRODUTOS_META["soja"])
    rec_id = add_preco(
        data_ref,
        args.praca,
        float(args.valor),
        produto=produto,
        tipo_posicao=args.tipo,
        valor_usd_sc=float(args.valor_usd) if args.valor_usd else None,
        observacao=args.obs,
    )
    usd_part = f"  /  US$ {float(args.valor_usd):,.2f}" if args.valor_usd else ""
    print(f"OK gravado (id #{rec_id}): {data_ref} | {args.praca} | {meta['label']} "
          f"= R$ {float(args.valor):,.2f} ({meta['unidade_display']}){usd_part}")


def cli_list(args):
    days = args.days or 14
    rows = list_recent(days)
    if not rows:
        print(f"Sem registros nos últimos {days} dias.")
        return
    print()
    print(f"  Últimos {days} dias — {len(rows)} registro(s):")
    print(f"  {'ID':>4}  {'DATA':10s}  {'PRACA':16s}  {'PRODUTO':10s}  {'TIPO':16s}  {'R$/SC':>10s}  {'US$/SC':>10s}  OBS")
    print("  " + "-" * 110)
    for r in rows:
        brl = f"{r['valor_brl_sc']:,.2f}" if r['valor_brl_sc'] else "—"
        usd = f"{r['valor_usd_sc']:,.2f}" if r['valor_usd_sc'] else "—"
        obs = (r['observacao'] or "")[:30]
        print(f"  {r['id']:>4}  {r['data']:10s}  {r['praca']:16s}  {r['produto']:10s}  {r['tipo_posicao']:16s}  {brl:>10s}  {usd:>10s}  {obs}")


def cli_import(args):
    res = import_csv(Path(args.path))
    if res["status"] == "erro":
        print(f"ERRO: {res['msg']}")
        return
    print(f"OK: {res['inserted']} inseridos, {res['updated']} atualizados, {res['skipped']} pulados")
    if res["erros"]:
        print(f"  {len(res['erros'])} erros:")
        for e in res["erros"][:10]:
            print(f"    {e}")


def cli_delete(args):
    ok = delete_id(args.id)
    print(f"{'OK apagado' if ok else 'NAO encontrado'}: id #{args.id}")
    if ok:
        print("  Valor anterior preservado em precos_fisicos_historico (acao=DELETE).")


def cli_export(args):
    """Exporta CSV: ativo (default) ou completo com historico (--historico)."""
    default_dir = Path(__file__).resolve().parent.parent / "data" / "exports"
    default_name = (
        f"precos_fisicos_historico_{date.today().isoformat()}.csv"
        if args.historico else
        f"precos_fisicos_{date.today().isoformat()}.csv"
    )
    out_path = Path(args.out) if args.out else default_dir / default_name
    res = export_to_csv(out_path, days=args.days, incluir_historico=args.historico)
    print(f"OK exportado ({res['modo']}): {res['rows']} linhas → {res['path']}")


def cli_historico(args):
    """Mostra log de auditoria de um registro/praca."""
    rows = historico(praca=args.praca, days=args.days)
    if not rows:
        print("Sem eventos no historico.")
        return
    print()
    print(f"  Eventos de auditoria — {len(rows)} linha(s)")
    print(f"  {'CAPTURADO':19s}  {'ACAO':12s}  {'DATA':10s}  {'PRACA':16s}  {'R$/SC':>10s}  {'US$/SC':>10s}  OBS")
    print("  " + "-" * 110)
    for r in rows:
        brl = f"{r['valor_brl_sc']:,.2f}" if r['valor_brl_sc'] else "—"
        usd = f"{r['valor_usd_sc']:,.2f}" if r['valor_usd_sc'] else "—"
        obs = (r['observacao'] or "")[:30]
        cap = (r['capturado_em'] or "")[:19]
        print(f"  {cap:19s}  {r['acao']:12s}  {r['data']:10s}  {r['praca']:16s}  {brl:>10s}  {usd:>10s}  {obs}")
