"""Orquestrador principal — CLI do Commodities Radar.

Uso:
    python main.py init         # cria estrutura + DB
    python main.py synth        # gera relatorio diario (markdown + HTML)
    python main.py run          # pipeline completo (public + indicators + alerts + forecast + synth)

2026-06-05: extração de relatórios StoneX descontinuada (ingest/check/stonex-pdf
removidos). Sistema roda 100% em fontes públicas + inputs manuais.
"""
import argparse
import sys
import io
from datetime import date
from pathlib import Path

# Forca stdout/stderr em UTF-8 (Windows default e cp1252)
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

import config
import db
import synth_daily
import notify_markdown
import notify_html
import indicators as indicators_mod
import alerts_technical
import backtest as backtest_mod
import forecast as forecast_mod
from sources import registry as sources_registry


def cmd_init(args):
    config.ensure_dirs()
    db.init_db()
    print("[init] estrutura criada")
    print(f"  DB:       {config.DB_PATH}")
    print(f"  data/:    {config.DATA_DIR}")
    print(f"  reports/: {config.REPORTS_DIR}")
    env_file = Path(__file__).parent / ".env"
    if not env_file.exists():
        print()
        print("[init] AVISO: .env nao existe. Copie .env.example para .env e preencha")


def cmd_synth(args):
    """Gera relatorio estruturado (sem LLM): markdown + HTML."""
    content = synth_daily.generate_structured_report()
    out_md = notify_markdown.write_daily(content)
    print(f"[synth] markdown em  {out_md}")
    try:
        out_html = notify_html.gerar_html()
        print(f"[synth] HTML em      {out_html}")
    except Exception as e:
        print(f"[synth] HTML falhou: {type(e).__name__}: {e}")

    # Copia o snapshot do dia pra pasta compartilhada com o consultor
    # (shared/to_consultor/snapshots_diarios — sincronizada via OneDrive).
    # So dados publicos + inputs proprios; nada de conteudo StoneX.
    try:
        import shutil
        if config.SHARED_TO_SNAPSHOTS.exists():
            destino = config.SHARED_TO_SNAPSHOTS / Path(out_md).name
            shutil.copyfile(out_md, destino)
            print(f"[synth] snapshot consultor em {destino}")
    except Exception as e:
        print(f"[synth] snapshot consultor falhou (nao critico): {e}")


def cmd_dump(args):
    """Gera dump completo para Claude Code processar."""
    content = synth_daily.generate_full_dump()
    out_path = config.DATA_DIR / "last_dump.md"
    out_path.write_text(content, encoding="utf-8")
    print(f"[dump] arquivo em {out_path}")
    print()
    print("Para sintese narrativa, abra o Claude Code no diretorio do projeto e peca:")
    print(f'  "le {out_path.name} e gera sintese diaria seguindo synthesize_daily.txt"')


def cmd_status(args):
    """Saude rapida no terminal: fontes, inputs manuais, forecasts, tributario."""
    from datetime import date as _date
    hoje = _date.today()

    print(f"\n=== RADAR STATUS — {hoje.isoformat()} ===")
    print(f"DB: {config.DB_PATH}")

    # 1. Fontes (mesma classificacao do card de saude do HTML)
    icones = {"ok": "+", "atrasada": "!", "erro": "X", "desativada": "."}
    fontes = notify_html._get_saude_fontes()
    problemas = [f for f in fontes if f["estado"] in ("atrasada", "erro")]
    print(f"\n--- Fontes ({len(fontes)}) "
          f"{'— todas na cadencia' if not problemas else f'— {len(problemas)} com problema'} ---")
    for f in fontes:
        marca = icones.get(f["estado"], "?")
        extra = f"  <-- {f['estado'].upper()}" if f["estado"] in ("atrasada", "erro") else ""
        idade = f"{f['dias']}d" if f["dias"] is not None else "—"
        print(f"  [{marca}] {f['fonte']:<20} {f['ultima'] or '—':<16}  ({idade}){extra}")

    # 2. Inputs manuais (idade por produto/praca, so tipo compra)
    print("\n--- Inputs manuais (fisico add) ---")
    with db.connect() as conn:
        rows = conn.execute(
            """
            SELECT produto, praca, MAX(data) data, valor_brl_sc
            FROM precos_fisicos WHERE tipo_posicao='compra'
            GROUP BY produto, praca ORDER BY produto, praca
            """
        ).fetchall()
    if not rows:
        print("  (nenhum input — rode fisico add)")
    for r in rows:
        idade = (hoje - _date.fromisoformat(r["data"])).days
        aviso = "  <-- VELHO (deltas suspensos)" if idade > 3 else ""
        print(f"  {r['produto']:<10} {r['praca']:<14} {r['data']} (D-{idade})  "
              f"R$ {r['valor_brl_sc']:.2f}{aviso}")

    # 3. Forecasts
    with db.connect() as conn:
        f = conn.execute(
            """
            SELECT COUNT(*) total,
                   SUM(CASE WHEN valor_realizado IS NULL THEN 1 ELSE 0 END) abertos,
                   SUM(hit) hits, SUM(CASE WHEN valor_realizado IS NOT NULL THEN 1 ELSE 0 END) resolvidos
            FROM forecasts
            """
        ).fetchone()
    pct = f"{100.0 * (f['hits'] or 0) / f['resolvidos']:.0f}%" if f["resolvidos"] else "n/d"
    print(f"\n--- Forecasts: {f['total']} gerados | {f['abertos']} abertos | "
          f"banda observada {pct} (n={f['resolvidos']}) ---")

    # 3b. Revisoes de insight vencendo (D+N)
    revisoes = notify_html._get_revisoes_pendentes(hoje, janela_dias=7)
    if revisoes:
        print(f"\n--- Revisoes de insight ({len(revisoes)}) ---")
        for r in revisoes:
            marca = "VENCIDA" if r["vencida"] else "em breve"
            print(f"  [{marca:^8}] {r['label']} {r['data']}  {r['insight'][:60]}")

    # 4. Tributario: proximos marcos 30d
    import tributario as trib
    proximos = [e for e in trib.list_eventos()
                if e.get("proximo_data")
                and 0 <= (_date.fromisoformat(e["proximo_data"]) - hoje).days <= 30]
    print(f"\n--- Tributario: proximos marcos 30d ({len(proximos)}) ---")
    for e in sorted(proximos, key=lambda x: x["proximo_data"]):
        print(f"  {e['proximo_data']}  {e['titulo'][:70]}")
    print()


def cmd_public(args):
    """Coleta dados de fontes publicas (USDA, NOPA, Conab, CEPEA, CME, etc)."""
    if args.list:
        print("[public] Coletores disponiveis:")
        for c in sources_registry.list_all():
            status = "ON " if c["enabled"] else "off"
            print(f"  [{status}] {c['source']:25s} ({c['cadence']:8s}) {c['description']}")
        return

    if args.source:
        print(f"[public] Rodando coletor '{args.source}'...")
        result = sources_registry.run_one(args.source)
        _print_collector_result(result)
        return

    print("[public] Rodando todos os coletores habilitados...")
    results = sources_registry.run_all()
    print()
    print(f"{'STATUS':10s} {'FONTE':25s} {'FETCHED':>8s} {'SAVED':>8s}  ERRO")
    print("-" * 80)
    for r in results:
        _print_collector_result(r, summary=True)


def _print_collector_result(result: dict, summary: bool = False):
    status = result.get("status", "?")
    fonte = result.get("source", "?")
    fetched = result.get("fetched", 0)
    saved = result.get("saved", 0)
    erro = result.get("error", "") or ""
    if not summary:
        print(f"  fonte:   {fonte}")
        print(f"  status:  {status}")
        print(f"  fetched: {fetched}")
        print(f"  saved:   {saved}")
        if erro:
            print(f"  erro:    {erro}")
    else:
        print(f"{status:10s} {fonte:25s} {fetched:>8d} {saved:>8d}  {erro[:50]}")


def cmd_indicators(args):
    """Calcula indicadores derivados (crush margin, oil share, etc)."""
    print("[indicators] calculando...")
    r = indicators_mod.calculate_all()
    print(f"  crush_margin:  {r['crush_margin']}")
    print(f"  oil_share:     {r['oil_share']}")
    print(f"  soja_brl:      {r['soja_brl']}")
    print(f"  spreads:       {r['spreads']}")
    print(f"  total salvos:  {r.get('total_calculados', 0)}")
    if r["errors"]:
        print(f"  erros: {len(r['errors'])}")


def cmd_alerts(args):
    """Verifica alertas tecnicos conforme alerts_config.toml."""
    alertas = alerts_technical.check_alerts()
    print(alerts_technical.format_alerts(alertas))
    if alertas:
        path = alerts_technical.save_alerts(alertas)
        print(f"\n[alerts] salvo em {path}")


def cmd_backtest(args):
    """Revisa teses ativas vs dados realizados."""
    p = backtest_mod.gerar_relatorio()
    print(f"[backtest] {p}")
    print()
    print(p.read_text(encoding="utf-8"))


def cmd_forecast(args):
    """Gera bandas de previsao 7d/30d ou resolve realizados."""
    if getattr(args, "resolve", False):
        print("[forecast] resolvendo forecasts vencidos...")
        r = forecast_mod.resolver_realizados()
        print(f"  revisados:        {r['revisados']}")
        print(f"  hit banda:        {r['hits_banda']} ({(r['hit_rate_banda'] or 0)*100:.1f}%)")
        print(f"  hit direcional:   {r['hits_direcional']} ({(r['hit_rate_direcional'] or 0)*100:.1f}%)")
    else:
        print("[forecast] gerando previsoes 7d e 30d...")
        r = forecast_mod.gerar_forecasts()
        print(f"  salvos:  {r['saved']}")
        if r["errors"]:
            print(f"  erros:   {len(r['errors'])}")
            for e in r["errors"]:
                print(f"    {e}")
        # Tambem resolve realizados pendentes
        rr = forecast_mod.resolver_realizados()
        if rr["revisados"]:
            print(f"  + {rr['revisados']} forecasts vencidos resolvidos (hit banda={rr['hits_banda']})")


def cmd_run(args):
    """Pipeline completo. Ordem importa: coleta → cálculo → HTML por último.

    Bug histórico (corrigido 2026-05-26): synth gerava HTML antes dos coletores,
    então o HTML refletia dados do dia anterior. Agora HTML vem por último.

    2026-06-05: ingest/check StoneX removidos do pipeline — extração de
    relatórios StoneX não é mais permitida. Fontes 100% públicas + inputs
    manuais (fisico add, curva set, param set).
    """
    cmd_public(args)        # 1. Coleta dados públicos (CBOT, BCB, CEPEA, etc)
    print()
    cmd_indicators(args)    # 2. Calcula indicadores derivados (crush, oil share, biodiesel margin)
    print()
    cmd_alerts(args)        # 3. Verifica alertas técnicos
    print()
    cmd_forecast(args)      # 4. Gera forecasts 7d/30d
    print()
    cmd_synth(args)         # 5. Gera HTML (agora com dados frescos)
    cmd_dump(args)          # 6. Gera dump pra Claude Code processar


def cmd_param(args):
    """Gerencia parametros manuais (RIN D4, custo industrial biodiesel, etc)."""
    import params_user as pu
    action = args.param_action
    if action == "set":
        pu.cli_set(args)
    elif action == "get":
        pu.cli_get(args)
    elif action == "list":
        pu.cli_list(args)
    elif action == "delete":
        pu.cli_delete(args)


def cmd_insight(args):
    """Gerencia insights de estudo (markdown files em insights/)."""
    import insights as ins_mod
    action = args.insight_action
    if action == "new":
        ins_mod.cli_new(args)
    elif action == "list":
        ins_mod.cli_list(args)
    elif action == "open":
        ins_mod.cli_open(args)


def cmd_curva(args):
    """Gerencia curvas de predicao (StoneX manual + Claude heuristico)."""
    import curvas
    action = args.curva_action
    if action == "set":
        curvas.cli_set(args)
    elif action == "list":
        curvas.cli_list(args)
    elif action == "generate":
        curvas.cli_generate(args)
    elif action == "delete":
        curvas.cli_delete(args)


def cmd_premios(args):
    """Consulta historico de premios por contrato/praca (serie encerrada 2026-06-05, so leitura)."""
    if args.premios_action != "list":
        return
    produto = args.produto or "soja"
    praca = args.praca or "paranagua"
    with db.connect() as conn:
        rows = conn.execute(
            """
            SELECT contrato, codigo_stonex, mes_label, tipo_op, valor,
                   variacao_diaria, unidade, data
            FROM premios_portos
            WHERE produto = ? AND praca = ?
              AND data = (
                SELECT MAX(data) FROM premios_portos
                WHERE produto = ? AND praca = ?
              )
            ORDER BY contrato, tipo_op
            """,
            (produto, praca, produto, praca),
        ).fetchall()
    if not rows:
        print(f"Sem premios pra {produto}/{praca} no historico (serie encerrada em 2026-06-05).")
        return
    print()
    print(f"  {produto.upper()} / {praca} (ultima data: {rows[0]['data']} — serie historica, sem atualizacao)")
    print(f"  {'CONTRATO':10s}  {'CODIGO':8s}  {'MES':12s}  {'TIPO':8s}  {'VALOR':>10s}  {'VAR':>8s}  UNIDADE")
    print("  " + "-" * 90)
    for r in rows:
        v = f"{r['valor']:+.2f}"
        var = f"{r['variacao_diaria']:+.2f}" if r["variacao_diaria"] is not None else "-"
        print(f"  {r['contrato']:10s}  {r['codigo_stonex']:8s}  {r['mes_label']:12s}  "
              f"{r['tipo_op']:8s}  {v:>10s}  {var:>8s}  {r['unidade']}")


def cmd_tributario(args):
    """Monitor Tributario/Regulatorio: vetores fiscais que afetam o complexo soja."""
    import tributario as trib
    action = args.tributario_action
    if action == "sync":
        out = trib.sync()
        print(f"[tributario] sincronizados {out['sincronizados']}, removidos {out['removidos']}")
    elif action == "list":
        eventos = trib.list_eventos(
            produto=getattr(args, "produto", None),
            status=getattr(args, "status", None),
        )
        if not eventos:
            print("Nenhum evento sob vigilancia (rode 'tributario sync').")
            return
        for e in eventos:
            print(f"  [{e['status']:11}] {e['jurisdicao']:9} {e['direcao']:6} {e['titulo']}")
            if e.get("mecanismo"):
                print(f"      {e['mecanismo']}")


def cmd_fisico(args):
    """Gestao manual de precos fisicos BR (Rancharia, Paranagua, etc)."""
    import precos_fisicos as pf
    action = args.fisico_action
    if action == "add":
        # interativo se nao passou --praca + --valor
        if not args.praca or not args.valor:
            pf.cli_add_interactive(args)
        else:
            pf.cli_add_flag(args)
    elif action == "list":
        pf.cli_list(args)
    elif action == "import":
        pf.cli_import(args)
    elif action == "delete":
        pf.cli_delete(args)
    elif action == "export":
        pf.cli_export(args)
    elif action == "historico":
        pf.cli_historico(args)


def main():
    parser = argparse.ArgumentParser(description="Commodities Radar — CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("init", help="cria estrutura + DB")

    sub.add_parser("synth", help="gera relatorio estruturado (sem LLM)")
    sub.add_parser("dump", help="dump completo para Claude Code sintetizar")

    p_pub = sub.add_parser("public", help="coleta dados de fontes publicas (USDA/NOPA/Conab/etc)")
    p_pub.add_argument("--source", help="rodar so um coletor (ex: cme_cbot)", default=None)
    p_pub.add_argument("--list", action="store_true", help="lista coletores disponiveis")

    sub.add_parser("indicators", help="calcula crush margin, oil share, spreads, paridade BR")
    sub.add_parser("alerts", help="verifica alertas tecnicos (suporte/resistencia/movimentos)")
    sub.add_parser("backtest", help="revisa teses ativas vs dados realizados")
    p_fcast = sub.add_parser("forecast", help="gera forecast 7d/30d ou resolve realizados")
    p_fcast.add_argument("--resolve", action="store_true", help="apenas atualiza realizados (sem gerar novos)")

    p_run = sub.add_parser("run", help="pipeline completo (ingest+synth+dump+check+public+indicators+alerts+forecast)")
    p_run.add_argument("--since", default=None)
    p_run.add_argument("--source", default=None)
    p_run.add_argument("--list", action="store_true")
    p_run.add_argument("--resolve", action="store_true")

    # === fisico: input manual de precos fisicos BR (Rancharia, Paranagua, etc) ===
    p_fis = sub.add_parser("fisico", help="input manual de precos fisicos BR (Rancharia/Paranagua/etc)")
    fis_sub = p_fis.add_subparsers(dest="fisico_action", required=True)
    p_fis_add = fis_sub.add_parser("add", help="adiciona preco (interativo se sem flags)")
    p_fis_add.add_argument("--praca", help="ex: rancharia_sp, paranagua_pr")
    p_fis_add.add_argument("--valor", help="R$/saca")
    p_fis_add.add_argument("--valor-usd", dest="valor_usd", help="US$/saca (opcional)")
    p_fis_add.add_argument("--data", help="YYYY-MM-DD (default: hoje)")
    p_fis_add.add_argument("--produto", help="soja|farelo|oleo_soja (default: soja)")
    p_fis_add.add_argument("--tipo", help="compra_balcao|exportacao_fob|indicador")
    p_fis_add.add_argument("--obs", help="observacao livre")

    p_fis_list = fis_sub.add_parser("list", help="lista precos recentes")
    p_fis_list.add_argument("--days", type=int, default=14)

    p_fis_imp = fis_sub.add_parser("import", help="importa CSV em lote")
    p_fis_imp.add_argument("path", help="caminho do CSV")

    p_fis_del = fis_sub.add_parser("delete", help="apaga registro por id (historico preservado)")
    p_fis_del.add_argument("--id", type=int, required=True)

    p_fis_exp = fis_sub.add_parser("export", help="exporta CSV (snapshot ativo ou historico completo)")
    p_fis_exp.add_argument("--out", help="caminho do CSV (default: data/exports/precos_fisicos_YYYY-MM-DD.csv)")
    p_fis_exp.add_argument("--days", type=int, default=None, help="ultimos N dias (default: tudo)")
    p_fis_exp.add_argument("--historico", action="store_true", help="exporta log de auditoria completo (INSERT/UPDATE/DELETE)")

    p_fis_hist = fis_sub.add_parser("historico", help="mostra log de auditoria")
    p_fis_hist.add_argument("--praca", help="filtra praca (ex: rancharia_sp)")
    p_fis_hist.add_argument("--days", type=int, default=None, help="ultimos N dias")

    # === param: parametros manuais (RIN D4, custo industrial biodiesel, etc) ===
    p_par = sub.add_parser("param", help="gerencia parametros manuais (RIN, custo industrial, etc)")
    par_sub = p_par.add_subparsers(dest="param_action", required=True)
    p_par_set = par_sub.add_parser("set", help="grava parametro")
    p_par_set.add_argument("chave", help="ex: rin_d4, custo_industrial_biodiesel_us")
    p_par_set.add_argument("valor")
    p_par_set.add_argument("--unidade")
    p_par_set.add_argument("--desc", dest="descricao")
    p_par_set.add_argument("--fonte")

    p_par_get = par_sub.add_parser("get", help="le um parametro")
    p_par_get.add_argument("chave")

    p_par_list = par_sub.add_parser("list", help="lista parametros (gravados + defaults)")
    p_par_list.add_argument("--no-defaults", action="store_true")

    p_par_del = par_sub.add_parser("delete", help="apaga parametro (volta pro default)")
    p_par_del.add_argument("chave")

    # === insight: gerencia insights de estudo (markdown) ===
    p_ins = sub.add_parser("insight", help="gerencia insights de estudo (markdown em insights/)")
    ins_sub = p_ins.add_subparsers(dest="insight_action", required=True)
    p_ins_new = ins_sub.add_parser("new", help="cria novo insight com template")
    p_ins_new.add_argument("titulo", nargs="+", help="titulo do insight (vira slug)")
    p_ins_new.add_argument("--open", action="store_true", help="abre no editor (notepad)")

    p_ins_list = ins_sub.add_parser("list", help="lista insights existentes")

    p_ins_open = ins_sub.add_parser("open", help="abre insight no editor")
    p_ins_open.add_argument("slug", help="slug parcial do arquivo")

    # === curva: gerencia curvas de predicao (StoneX manual + Claude heuristico) ===
    p_cv = sub.add_parser("curva", help="gerencia curvas de predicao (stonex/claude vs CBOT real)")
    cv_sub = p_cv.add_subparsers(dest="curva_action", required=True)

    p_cv_set = cv_sub.add_parser("set", help="grava ponto da curva (stonex ou claude)")
    p_cv_set.add_argument("fonte", choices=["stonex", "claude"])
    p_cv_set.add_argument("--produto", required=True, help="soja|farelo|oleo")
    p_cv_set.add_argument("--venc", required=True, help="N26, Q26, X26, F27 etc")
    p_cv_set.add_argument("--valor", required=True, help="preco indicativo")
    p_cv_set.add_argument("--obs", help="observacao livre")
    p_cv_set.add_argument("--detalhe", dest="detalhe", help="fonte_detalhe (ex: 'Fabio call 25mai')")

    p_cv_list = cv_sub.add_parser("list", help="lista curvas")
    p_cv_list.add_argument("--fonte", choices=["stonex", "claude"])
    p_cv_list.add_argument("--commodity", help="soja_cbot|farelo_cbot|oleo_cbot")

    p_cv_gen = cv_sub.add_parser("generate", help="roda heuristica Claude pros 3 produtos")

    p_cv_del = cv_sub.add_parser("delete", help="apaga por id")
    p_cv_del.add_argument("--id", type=int, required=True)

    # === status: saude rapida no terminal ===
    sub.add_parser("status", help="saude do sistema: fontes, inputs, forecasts, marcos tributarios")

    # === premios: consulta historico de premios StoneX (import descontinuado 2026-06-05) ===
    p_pr = sub.add_parser("premios", help="consulta historico de premios por contrato/praca (so leitura)")
    pr_sub = p_pr.add_subparsers(dest="premios_action", required=True)
    p_pr_lst = pr_sub.add_parser("list", help="lista ultimos premios (dados historicos no DB)")
    p_pr_lst.add_argument("--produto", help="soja|farelo|oleo_soja")
    p_pr_lst.add_argument("--praca", help="paranagua|golfo_eua|argentina")

    # === tributario: monitor fiscal/regulatorio do complexo soja ===
    p_trib = sub.add_parser("tributario", help="monitor tributario/regulatorio (MPs, STJ, RFS, 45Z, B16, palma)")
    trib_sub = p_trib.add_subparsers(dest="tributario_action", required=True)
    trib_sub.add_parser("sync", help="sincroniza tributario_watch.toml -> DB")
    p_trib_list = trib_sub.add_parser("list", help="lista eventos sob vigilancia")
    p_trib_list.add_argument("--produto", help="soja|farelo|oleo_soja")
    p_trib_list.add_argument("--status", help="vigente|tramitacao|adiado|monitorando")

    args = parser.parse_args()
    if not hasattr(args, "list"):
        args.list = False
    if not hasattr(args, "source"):
        args.source = None
    {
        "init": cmd_init,
        "synth": cmd_synth,
        "dump": cmd_dump,
        "public": cmd_public,
        "indicators": cmd_indicators,
        "alerts": cmd_alerts,
        "backtest": cmd_backtest,
        "forecast": cmd_forecast,
        "run": cmd_run,
        "fisico": cmd_fisico,
        "param": cmd_param,
        "insight": cmd_insight,
        "curva": cmd_curva,
        "status": cmd_status,
        "premios": cmd_premios,
        "tributario": cmd_tributario,
    }[args.cmd](args)


if __name__ == "__main__":
    main()
