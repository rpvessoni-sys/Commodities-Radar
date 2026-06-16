"""Sintese diaria — versao SEM Claude API.

Gera relatorio estruturado em markdown a partir do que esta no DB.
Para sintese NARRATIVA, voce abre o Claude Code e pede: "le o ultimo dump em
data/last_dump.md e sintetize". Claude Code (que voce ja paga) faz a sintese
usando contexto completo dos relatorios + memoria do projeto.

Esse design evita custo de API extra e mantem privacidade (dados nunca saem
da maquina exceto via Claude Code que voce ja autorizou).
"""
from datetime import date
from pathlib import Path
import json

# Fix SSL no Windows: usar o cert store nativo do OS via truststore
# (mesmo padrao de sources/base.py — AVG quebra SSL sem isso)
try:
    import truststore
    truststore.inject_into_ssl()
except ImportError:
    pass

import config
import db


def generate_structured_report(target_date: date | None = None) -> str:
    """Snapshot executivo diario em markdown a partir do DB publico.

    Sem LLM — so SQL + formatacao. Fontes: dados_publicos (cme_cbot, bcb,
    indicators, nag_fisico) + alertas tecnicos do dia. Serie relatorios_stonex
    foi ENCERRADA em 2026-06-05; aparece so como bloco historico condicional.
    Ausencia de qualquer dado vira '—' — nunca crasha.
    """
    target = target_date or date.today()

    with db.connect() as conn:
        cbot = {
            "soja_cbot": _fechamento_com_variacao(conn, "soja_cbot", target),
            "farelo_cbot": _fechamento_com_variacao(conn, "farelo_cbot", target),
            "oleo_cbot": _fechamento_com_variacao(conn, "oleo_cbot", target),
        }
        ptax = _ultimo_registro(conn, "bcb", "usd_brl_ptax", "valor", target)
        indicadores = {
            m: _ultimo_registro(conn, "indicators", "complexo_soja", m, target)
            for m in ("crush_margin_usd_bu", "oil_share_pct", "far_soj_ratio_pct")
        }
        premio_farelo = _ultimo_registro(conn, "nag_fisico", "farelo_paranagua", "premio_usd_sht", target)
        premio_oleo = _ultimo_registro(conn, "nag_fisico", "oleo_paranagua", "premio_cts_lb", target)
        farelo_pracas = [
            ("Rondonopolis/MT (BCSP)", _ultimo_registro(conn, "nag_fisico", "farelo_fisico_br", "preco_brl_ton_rondonopolis_mt", target)),
            ("Mato Grosso (IMEA)", _ultimo_registro(conn, "nag_fisico", "farelo_fisico_br", "preco_brl_ton_mt_imea", target)),
            ("Media RS (Clicmercado)", _ultimo_registro(conn, "nag_fisico", "farelo_fisico_br", "preco_brl_ton_rs_media", target)),
        ]
        stonex_rows = conn.execute(
            """
            SELECT tipo, data_publicacao FROM relatorios_stonex
            WHERE date(data_publicacao) >= date(?, '-7 days')
            ORDER BY data_publicacao DESC, tipo
            """,
            (target.isoformat(),),
        ).fetchall()

    alertas = _alertas_do_dia(target)

    lines = []
    lines.append(f"# Daily — {target.isoformat()}")
    lines.append("")
    lines.append("_Snapshot executivo do complexo soja — 100% fontes publicas._")
    lines.append("")

    # --- Fechamentos CBOT (serie continua = front month) ---
    lines.append("## Fechamentos CBOT (front month)")
    lines.append("")
    lines.append("| Contrato | Fechamento | Var vs pregao anterior | Pregao |")
    lines.append("|---|---|---|---|")
    rotulos = [
        ("soja_cbot", "Soja (cts/bu)"),
        ("farelo_cbot", "Farelo (USD/sht)"),
        ("oleo_cbot", "Oleo (cts/lb)"),
    ]
    for chave, rotulo in rotulos:
        f = cbot[chave]
        if f is None:
            lines.append(f"| {rotulo} | — | — | — |")
        else:
            lines.append(f"| {rotulo} | {_fmt(f['valor'])} | {_fmt_variacao(f)} | {f['data']} |")
    lines.append("")

    # --- Cambio ---
    lines.append("## Cambio")
    lines.append("")
    if ptax:
        lines.append(f"- USD/BRL PTAX: **{_fmt(ptax['valor'], 4)}** ({ptax['data_referencia']}, fonte BCB)")
    else:
        lines.append("- USD/BRL PTAX: —")
    lines.append("")

    # --- Indicadores derivados ---
    lines.append("## Indicadores do complexo")
    lines.append("")
    crush = indicadores["crush_margin_usd_bu"]
    oil_share = indicadores["oil_share_pct"]
    far_soj = indicadores["far_soj_ratio_pct"]
    lines.append("| Indicador | Valor | Leitura |")
    lines.append("|---|---|---|")
    lines.append(f"| Crush margin (USD/bu) | {_fmt(crush['valor']) if crush else '—'} | board crush CBOT |")
    lines.append(f"| Oil share (%) | {_fmt(oil_share['valor']) if oil_share else '—'} | participacao do oleo no valor do crush |")
    zona = _zona_far_soj(far_soj["valor"] if far_soj else None)
    lines.append(f"| Farelo/Soja ratio (%) | {_fmt(far_soj['valor']) if far_soj else '—'} | {zona} |")
    if far_soj:
        lines.append("")
        lines.append(f"_Ratio referencia {far_soj['data_referencia']} — zonas: <80 abundante, 80-87 transicao, >=87 apertado._")
    lines.append("")

    # --- Fisico / premios Paranagua (NAG) ---
    lines.append("## Premios Paranagua e farelo fisico BR (NAG)")
    lines.append("")
    if premio_farelo:
        lines.append(f"- Premio farelo PGUA: **{_fmt(premio_farelo['valor'])} USD/sht** ({premio_farelo['data_referencia']})")
    else:
        lines.append("- Premio farelo PGUA: —")
    if premio_oleo:
        lines.append(f"- Premio oleo PGUA: **{_fmt(premio_oleo['valor'])} cts/lb** ({premio_oleo['data_referencia']})")
    else:
        lines.append("- Premio oleo PGUA: —")
    lines.append("")
    lines.append("Farelo fisico — 3 pracas (BRL/ton):")
    lines.append("")
    lines.append("| Praca | Preco | Data |")
    lines.append("|---|---|---|")
    for nome, reg in farelo_pracas:
        if reg:
            lines.append(f"| {nome} | {_fmt(reg['valor'])} | {reg['data_referencia']} |")
        else:
            lines.append(f"| {nome} | — | — |")
    lines.append("")

    # --- Alertas tecnicos do dia ---
    lines.append("## Alertas tecnicos do dia")
    lines.append("")
    if alertas:
        for a in alertas:
            lines.append(f"- [{a.get('tipo', '?')}] {a.get('msg', '(sem mensagem)')}")
    else:
        lines.append("_Sem alertas tecnicos hoje._")
    lines.append("")

    # --- Bloco historico StoneX (serie encerrada — so aparece se houver registro recente) ---
    if stonex_rows:
        lines.append("## Historico StoneX (ultimos 7 dias)")
        lines.append("")
        for r in stonex_rows:
            lines.append(f"- {r['tipo']} — {r['data_publicacao']}")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("_Gerado automaticamente de fontes publicas (CBOT/BCB/NAG/CEPEA); sem conteudo StoneX._")
    lines.append("")

    return "\n".join(lines)


def _fmt(valor, casas: int = 2) -> str:
    """Formata float com N casas; None vira '—'."""
    if valor is None:
        return "—"
    return f"{valor:.{casas}f}"


def _fmt_variacao(fech: dict) -> str:
    """Formata variacao absoluta + percentual vs pregao anterior."""
    if fech.get("delta") is None:
        return "—"
    return f"{fech['delta']:+.2f} ({fech['pct']:+.2f}%)"


def _zona_far_soj(pct) -> str:
    """Zona do ratio farelo/soja: <80 abundante, 80-87 transicao, >=87 apertado."""
    if pct is None:
        return "—"
    if pct < 80:
        return "abundante (<80)"
    if pct < 87:
        return "transicao (80-87)"
    return "apertado (>=87)"


def _ultimo_registro(conn, fonte: str, commodity: str, metrica: str, target: date) -> dict | None:
    """Ultimo registro (valor nao-nulo) ate a data alvo. None se nao houver."""
    row = conn.execute(
        """
        SELECT data_referencia, valor, unidade, contexto
        FROM dados_publicos
        WHERE fonte = ? AND commodity = ? AND metrica = ?
          AND valor IS NOT NULL AND data_referencia <= ?
        ORDER BY data_referencia DESC LIMIT 1
        """,
        (fonte, commodity, metrica, target.isoformat()),
    ).fetchone()
    return dict(row) if row else None


def _fechamento_com_variacao(conn, commodity: str, target: date) -> dict | None:
    """Ultimo fechamento CBOT (serie continua front month) + variacao vs pregao anterior."""
    rows = conn.execute(
        """
        SELECT data_referencia, valor
        FROM dados_publicos
        WHERE fonte = 'cme_cbot' AND commodity = ? AND metrica = 'fechamento'
          AND valor IS NOT NULL AND data_referencia <= ?
        ORDER BY data_referencia DESC LIMIT 4
        """,
        (commodity, target.isoformat()),
    ).fetchall()
    # Dedup por data (defensivo caso haja mais de um tipo por pregao)
    vistos = []
    for r in rows:
        if not vistos or r["data_referencia"] != vistos[-1]["data_referencia"]:
            vistos.append(r)
        if len(vistos) == 2:
            break
    if not vistos:
        return None
    out = {"data": vistos[0]["data_referencia"], "valor": vistos[0]["valor"], "delta": None, "pct": None}
    if len(vistos) == 2 and vistos[1]["valor"]:
        out["delta"] = vistos[0]["valor"] - vistos[1]["valor"]
        out["pct"] = out["delta"] / vistos[1]["valor"] * 100
    return out


def _alertas_do_dia(target: date) -> list[dict]:
    """Le data/alerts_technical.json e filtra alertas com data == alvo.

    Formato real do arquivo: {"gerado_em": iso, "alertas": [{commodity, tipo,
    data, valor_atual, nivel, delta, msg}]}. Qualquer problema => lista vazia.
    """
    path = config.DATA_DIR / "alerts_technical.json"
    if not path.exists():
        return []
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []
    alertas = payload.get("alertas") or []
    return [a for a in alertas if isinstance(a, dict) and a.get("data") == target.isoformat()]


def generate_full_dump(target_date: date | None = None) -> str:
    """Briefing consolidado da BASE PUBLICA pra leitura do Claude em sessao.

    Reune dados publicos (14d) + forecasts ativos + notas manuais do consultor
    (shared/from_consultor), com ponteiro pro que fazer. A serie de relatorios
    StoneX foi ENCERRADA em 2026-06-05 e nao entra mais aqui.
    """
    target = target_date or date.today()

    insights_consultor = _read_consultor_files(config.SHARED_FROM_INSIGHTS)
    notas_call = _read_consultor_files(config.SHARED_FROM_NOTAS)

    lines = []
    lines.append(f"# Briefing consolidado — {target.isoformat()}")
    lines.append("")
    lines.append("_Base 100% publica (CBOT/BCB/CEPEA/NAG/USDA/COT/clima) + notas manuais do consultor._")
    lines.append("")
    lines.append("## O que fazer com este briefing")
    lines.append("")
    lines.append("- **Tratar a fila de julgamento** (camada de LEITURA): rode `python main.py queue`, "
                 "siga `system/prompts/treat_queue.txt` e escreva so `insights/*.md` (com `vies:`).")
    lines.append("- **Sintese narrativa do dia** (opcional): siga `system/prompts/synthesize_daily.txt`.")
    lines.append("- Numeros SEMPRE com fonte + data. Aplicar a lente tributaria BR antes de concluir tese de preco.")
    lines.append("- NUNCA escrever em numero/indicador/DB/alerts_config — opiniao so vai pra `insights/*.md`.")
    lines.append("")
    lines.append(f"Notas manuais disponiveis: {len(insights_consultor)} do consultor · {len(notas_call)} de call.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Dados publicos
    publicos = _read_dados_publicos(target)
    if publicos:
        lines.append("# DADOS PUBLICOS (ultimos 14 dias)")
        lines.append("")
        for fonte, registros in publicos.items():
            lines.append(f"## {fonte}")
            lines.append("")
            for r in registros[:50]:  # cap pra nao explodir
                ctx = f" ({r['contexto']})" if r['contexto'] else ""
                lines.append(f"- {r['data_referencia']} | {r['commodity']} | {r['metrica']}: {r['valor']} {r['unidade'] or ''}{ctx}")
            lines.append("")
            lines.append("---")
            lines.append("")

    # Forecasts ativos
    forecasts = _read_forecasts(target)
    if forecasts:
        lines.append("# FORECASTS ATIVOS (bandas estatisticas)")
        lines.append("")
        lines.append("Bandas calculadas via MA20+volatilidade+slope curto. Claude Code DEVE refinar com drivers fundamentais.")
        lines.append("")
        lines.append("| Geracao | Horizonte | Alvo | Commodity | Spot ref | Baixo | Central | Alto | Vies |")
        lines.append("|---|---|---|---|---|---|---|---|---|")
        for f in forecasts:
            spot = f.get("spot_ref") or "?"
            lines.append(
                f"| {f['data_geracao']} | {f['horizonte_dias']}d | {f['data_alvo']} | "
                f"{f['commodity']} | {spot} | "
                f"{f['valor_baixo']:.2f} | {f['valor_central']:.2f} | {f['valor_alto']:.2f} | "
                f"{f['vies']} |"
            )
        lines.append("")
        lines.append("---")
        lines.append("")

    if insights_consultor:
        lines.append("# INSIGHTS DO CONSULTOR")
        lines.append("")
        for f in insights_consultor:
            lines.append(f"## {f['nome']}")
            lines.append("")
            lines.append(f["conteudo"])
            lines.append("")
            lines.append("---")
            lines.append("")

    if notas_call:
        lines.append("# NOTAS DE CALL")
        lines.append("")
        for f in notas_call:
            lines.append(f"## {f['nome']}")
            lines.append("")
            lines.append(f["conteudo"])
            lines.append("")
            lines.append("---")
            lines.append("")

    return "\n".join(lines)


def _read_consultor_files(folder: "Path") -> list[dict]:
    """Le todos arquivos .md/.txt da pasta (ignora subpastas processed/)."""
    if not folder.exists():
        return []
    files = []
    for ext in ("*.md", "*.txt"):
        files.extend(folder.glob(ext))
    out = []
    for f in sorted(files, reverse=True):
        out.append({
            "nome": f.name,
            "conteudo": f.read_text(encoding="utf-8", errors="replace"),
        })
    return out


def _read_forecasts(target: date) -> list[dict]:
    """Le forecasts ativos (data_alvo >= hoje) ordenados por horizonte."""
    out = []
    with db.connect() as conn:
        cur = conn.execute(
            """
            SELECT f.data_geracao, f.horizonte_dias, f.data_alvo, f.commodity, f.metrica,
                   f.valor_baixo, f.valor_central, f.valor_alto, f.vies,
                   (SELECT valor FROM dados_publicos
                      WHERE fonte='cme_cbot' AND commodity=f.commodity AND metrica='fechamento'
                        AND data_referencia <= f.data_geracao
                      ORDER BY data_referencia DESC LIMIT 1) as spot_ref
            FROM forecasts f
            WHERE date(f.data_alvo) >= ?
              AND date(f.data_geracao) >= date(?, '-3 days')
            ORDER BY f.data_geracao DESC, f.horizonte_dias, f.commodity
            """,
            (target.isoformat(), target.isoformat()),
        )
        for r in cur:
            d = dict(r)
            d["spot_ref"] = f"{d['spot_ref']:.2f}" if d['spot_ref'] else "n/d"
            out.append(d)
    return out


def _read_dados_publicos(target: date) -> dict:
    """Le ultimos 14 dias de dados_publicos, agrupados por fonte."""
    out = {}
    with db.connect() as conn:
        cursor = conn.execute(
            """
            SELECT fonte, data_referencia, commodity, metrica, valor, unidade, contexto
            FROM dados_publicos
            WHERE data_referencia >= date(?, '-14 days')
              AND metrica != 'fetch_error'
              AND metrica != 'parse_error'
            ORDER BY fonte, data_referencia DESC, commodity, metrica
            """,
            (target.isoformat(),),
        )
        for row in cursor:
            fonte = row["fonte"]
            if fonte not in out:
                out[fonte] = []
            out[fonte].append(dict(row))
    return out
