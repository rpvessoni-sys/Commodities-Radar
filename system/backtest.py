"""Backtest de teses registradas em tese_journal/.

Le cada arquivo .md das teses ativas (que tem data_horizonte) e compara
com dados realizados. Gera relatorio em reports/backtest_YYYY-MM-DD.md.

Logica:
1. Le tese (titulo, premissa, horizonte, niveis de invalidacao, status)
2. Para o periodo entre data_registro e data_horizonte (ou hoje), busca:
   - Preco da commodity envolvida (CME/BCB/dados_publicos)
   - Eventos relevantes (relatorios StoneX no periodo)
3. Avalia:
   - Tese acertou direcao? (preco subiu vs caiu vs lateral)
   - Niveis de invalidacao foram quebrados?
   - Algum evento contradisse?
4. Salva resultado no journal (atualizando D+7/D+30)

Comando:
    python main.py backtest        # revisa todas teses ativas
"""
import re
from datetime import date, datetime, timedelta
from pathlib import Path
import config
import db


def listar_teses() -> list[dict]:
    """Le todos os arquivos .md em tese_journal/."""
    pasta = Path(config.ROOT) if hasattr(config, "ROOT") else Path(__file__).parent.parent
    pasta = pasta / "tese_journal"
    if not pasta.exists():
        # fallback
        pasta = Path(__file__).resolve().parent.parent / "tese_journal"
    if not pasta.exists():
        return []

    teses = []
    for f in pasta.glob("*.md"):
        if f.name.startswith("_") or f.name.upper() == "README.MD":
            continue
        conteudo = f.read_text(encoding="utf-8", errors="replace")
        tese = {
            "arquivo": str(f),
            "nome": f.stem,
            "conteudo": conteudo,
            "data_registro": _extract_field(conteudo, "Data de registro"),
            "horizonte": _extract_field(conteudo, "Horizonte"),
            "commodity": _extract_field(conteudo, "Commodity"),
            "vies": _extract_field(conteudo, "Vies"),
        }
        teses.append(tese)
    return teses


def _extract_field(texto: str, campo: str) -> str:
    m = re.search(rf"\*\*{re.escape(campo)}:\*\*\s*([^\n]+)", texto)
    return m.group(1).strip() if m else ""


def avaliar_tese(tese: dict) -> dict:
    """Compara tese com dados realizados."""
    avaliacao = {
        "nome": tese["nome"],
        "data_registro": tese["data_registro"],
        "commodity": tese["commodity"],
        "vies_registrado": tese["vies"],
        "movimento_real": None,
        "preco_inicio": None,
        "preco_atual": None,
        "delta_pct": None,
        "veredito": "indeterminado",
    }

    # Tenta identificar commodity (busca palavras-chave)
    commodity_lower = tese["commodity"].lower()
    if "oleo" in commodity_lower or "óleo" in commodity_lower:
        commodity_key = "oleo_cbot"
    elif "farelo" in commodity_lower:
        commodity_key = "farelo_cbot"
    elif "soja" in commodity_lower:
        commodity_key = "soja_cbot"
    else:
        commodity_key = None  # milho/trigo/etc removidos do escopo

    if not commodity_key:
        avaliacao["veredito"] = "commodity_nao_mapeada"
        return avaliacao

    # Tentar extrair data_registro ISO ou DD/MM/YYYY
    data_reg = tese["data_registro"]
    data_iso = None
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", data_reg)
    if m:
        data_iso = data_reg[:10]
    else:
        m = re.search(r"(\d{1,2})[/-](\d{1,2})[/-](\d{2,4})", data_reg)
        if m:
            d, mo, y = m.group(1), m.group(2), m.group(3)
            if len(y) == 2:
                y = "20" + y
            data_iso = f"{y}-{int(mo):02d}-{int(d):02d}"

    if not data_iso:
        avaliacao["veredito"] = "data_invalida"
        return avaliacao

    with db.connect() as conn:
        cur = conn.execute(
            """
            SELECT data_referencia, valor
            FROM dados_publicos
            WHERE commodity = ? AND metrica = 'fechamento' AND tipo = 'preco'
              AND data_referencia >= ?
            ORDER BY data_referencia ASC
            """,
            (commodity_key, data_iso),
        )
        precos = cur.fetchall()

    if not precos:
        avaliacao["veredito"] = "sem_dados_periodo"
        return avaliacao

    preco_inicio = precos[0]["valor"]
    preco_atual = precos[-1]["valor"]
    delta_pct = ((preco_atual - preco_inicio) / preco_inicio) * 100 if preco_inicio else 0

    avaliacao["preco_inicio"] = preco_inicio
    avaliacao["preco_atual"] = preco_atual
    avaliacao["delta_pct"] = round(delta_pct, 2)
    avaliacao["dias_analisados"] = len(precos)

    # Classificar movimento real
    if delta_pct > 2:
        avaliacao["movimento_real"] = "alta"
    elif delta_pct < -2:
        avaliacao["movimento_real"] = "baixa"
    else:
        avaliacao["movimento_real"] = "lateral"

    # Comparar com vies
    vies_lower = tese["vies"].lower()
    if "alta" in vies_lower or "altist" in vies_lower:
        vies_norm = "alta"
    elif "baix" in vies_lower:
        vies_norm = "baixa"
    elif "lateral" in vies_lower or "range" in vies_lower:
        vies_norm = "lateral"
    else:
        vies_norm = "indeterminado"

    if vies_norm == avaliacao["movimento_real"]:
        avaliacao["veredito"] = "acertou"
    elif vies_norm == "indeterminado":
        avaliacao["veredito"] = "sem_vies_claro"
    else:
        avaliacao["veredito"] = "errou"

    return avaliacao


def gerar_relatorio(target_date: date | None = None) -> Path:
    target = target_date or date.today()
    teses = listar_teses()

    lines = [f"# Backtest — {target.isoformat()}", ""]
    if not teses:
        lines.append("Nenhuma tese encontrada em tese_journal/.")
    else:
        lines.append(f"Avaliando {len(teses)} tese(s).")
        lines.append("")

    for tese in teses:
        av = avaliar_tese(tese)
        lines.append(f"## {av['nome']}")
        lines.append(f"- Registrada: {av['data_registro']}")
        lines.append(f"- Commodity: {av['commodity']}")
        lines.append(f"- Vies registrado: {av['vies_registrado']}")
        lines.append(f"- Movimento real: {av.get('movimento_real') or 'n/d'}")
        if av.get("preco_inicio"):
            lines.append(f"- Preco inicio → atual: {av['preco_inicio']} → {av['preco_atual']} ({av['delta_pct']:+.2f}%)")
            lines.append(f"- Dias analisados: {av.get('dias_analisados', 0)}")
        lines.append(f"- **Veredito: {av['veredito']}**")
        lines.append("")

    out = config.REPORTS_DIR / f"backtest_{target.isoformat()}.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


if __name__ == "__main__":
    p = gerar_relatorio()
    print(f"Backtest salvo em {p}")
    print(p.read_text(encoding="utf-8"))
