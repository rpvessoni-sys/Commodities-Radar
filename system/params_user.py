"""Parametros manuais editaveis pelo usuario.

Usado para premissas/cotacoes que nao tem coletor automatico mas o consultor
manda periodicamente (RIN D4, custo industrial biodiesel, cambio premissa, etc).

CLI:
    python main.py param set rin_d4 2.11 --unidade USD/gal --desc "RIN D4 biodiesel" --fonte "StoneX 25mai"
    python main.py param get rin_d4
    python main.py param list
    python main.py param delete rin_d4

Catalogo de parametros conhecidos (defaults sensatos se nao gravados):
"""
from datetime import datetime
import db


# Defaults usados em calculos quando o param nao foi setado
DEFAULTS = {
    "rin_d4": {
        "valor": 2.11,
        "unidade": "USD/galão",
        "descricao": "RIN D4 — crédito biodiesel americano (EPA semanal)",
        "fonte": "default (StoneX 25mai 2026)",
    },
    "custo_industrial_biodiesel_us": {
        "valor": 0.80,
        "unidade": "USD/galão",
        "descricao": "Custo industrial estimado por galão de biodiesel produzido",
        "fonte": "default (intervalo 0.6-1.0 conforme StoneX)",
    },
    "yield_oleo_lb_per_galao": {
        "valor": 7.5,
        "unidade": "lb/galão",
        "descricao": "Quantidade de óleo soja necessária por galão biodiesel",
        "fonte": "default StoneX",
    },
    "yield_rin_per_galao": {
        "valor": 1.5,
        "unidade": "RIN/galão",
        "descricao": "Quantidade de RINs gerados por galão biodiesel",
        "fonte": "default RFS (D4 biodiesel)",
    },
}


def set_param(chave: str, valor: float, unidade: str | None = None,
              descricao: str | None = None, fonte: str | None = None) -> None:
    """Insere ou atualiza um parametro."""
    # Se valores opcionais nao vierem, herda do DEFAULT se existir
    d = DEFAULTS.get(chave, {})
    unidade = unidade or d.get("unidade")
    descricao = descricao or d.get("descricao")
    fonte = fonte or d.get("fonte")

    with db.connect() as conn:
        conn.execute(
            """
            INSERT INTO params_user (chave, valor, unidade, descricao, fonte, atualizado_em)
            VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            ON CONFLICT(chave) DO UPDATE SET
                valor=excluded.valor,
                unidade=excluded.unidade,
                descricao=excluded.descricao,
                fonte=excluded.fonte,
                atualizado_em=CURRENT_TIMESTAMP
            """,
            (chave, valor, unidade, descricao, fonte),
        )


def get_param(chave: str, fallback_default: bool = True) -> dict | None:
    """Retorna parametro. Se nao gravado e fallback_default=True, retorna default."""
    with db.connect() as conn:
        cur = conn.execute(
            "SELECT chave, valor, unidade, descricao, fonte, atualizado_em FROM params_user WHERE chave=?",
            (chave,),
        )
        row = cur.fetchone()
    if row:
        return {
            "chave": row["chave"],
            "valor": row["valor"],
            "unidade": row["unidade"],
            "descricao": row["descricao"],
            "fonte": row["fonte"],
            "atualizado_em": row["atualizado_em"],
            "is_default": False,
        }
    if fallback_default and chave in DEFAULTS:
        d = DEFAULTS[chave]
        return {
            "chave": chave,
            "valor": d["valor"],
            "unidade": d.get("unidade"),
            "descricao": d.get("descricao"),
            "fonte": d.get("fonte"),
            "atualizado_em": None,
            "is_default": True,
        }
    return None


def list_params(include_defaults: bool = True) -> list[dict]:
    """Lista todos os parametros (gravados + defaults não sobrescritos)."""
    out = []
    seen = set()
    with db.connect() as conn:
        cur = conn.execute(
            "SELECT chave, valor, unidade, descricao, fonte, atualizado_em FROM params_user ORDER BY chave"
        )
        for r in cur:
            out.append({
                "chave": r["chave"],
                "valor": r["valor"],
                "unidade": r["unidade"],
                "descricao": r["descricao"],
                "fonte": r["fonte"],
                "atualizado_em": r["atualizado_em"],
                "is_default": False,
            })
            seen.add(r["chave"])
    if include_defaults:
        for k, d in DEFAULTS.items():
            if k not in seen:
                out.append({
                    "chave": k,
                    "valor": d["valor"],
                    "unidade": d.get("unidade"),
                    "descricao": d.get("descricao"),
                    "fonte": d.get("fonte"),
                    "atualizado_em": None,
                    "is_default": True,
                })
    return out


def delete_param(chave: str) -> bool:
    with db.connect() as conn:
        cur = conn.execute("DELETE FROM params_user WHERE chave=?", (chave,))
        return cur.rowcount > 0


# ============================================================
# CLI
# ============================================================

def cli_set(args):
    chave = args.chave
    if chave not in DEFAULTS and not args.descricao:
        print(f"[aviso] chave '{chave}' não está no catálogo DEFAULTS — adicione --desc pra documentar")
    set_param(chave, float(args.valor),
              unidade=args.unidade,
              descricao=args.descricao,
              fonte=args.fonte)
    p = get_param(chave)
    print(f"OK gravado: {p['chave']} = {p['valor']} {p['unidade'] or ''}"
          + (f"  ({p['fonte']})" if p['fonte'] else ""))


def cli_get(args):
    p = get_param(args.chave)
    if not p:
        print(f"[não encontrado] {args.chave}")
        return
    badge = "[DEFAULT]" if p["is_default"] else "[gravado]"
    print(f"{badge}  {p['chave']} = {p['valor']} {p['unidade'] or ''}")
    if p["descricao"]:
        print(f"  descrição: {p['descricao']}")
    if p["fonte"]:
        print(f"  fonte: {p['fonte']}")
    if p["atualizado_em"]:
        print(f"  atualizado em: {p['atualizado_em']}")


def cli_list(args):
    rows = list_params(include_defaults=not args.no_defaults)
    if not rows:
        print("Sem parâmetros.")
        return
    print()
    print(f"  {len(rows)} parâmetro(s) — [G] gravado, [D] default:")
    print(f"  {'STATUS':6s}  {'CHAVE':36s}  {'VALOR':>10s}  {'UNIDADE':14s}  FONTE")
    print("  " + "-" * 100)
    for p in rows:
        status = "[D]" if p["is_default"] else "[G]"
        valor = f"{p['valor']:.4f}" if p["valor"] is not None else "—"
        print(f"  {status:6s}  {p['chave']:36s}  {valor:>10s}  {(p['unidade'] or ''):14s}  {(p['fonte'] or '')[:40]}")


def cli_delete(args):
    ok = delete_param(args.chave)
    print(f"{'OK apagado (volta pro default se houver)' if ok else 'NAO encontrado'}: {args.chave}")
