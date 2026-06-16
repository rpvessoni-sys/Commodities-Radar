"""Monitor Tributário/Regulatório — vetores fiscais que afetam o complexo soja.

Fonte da verdade: `tributario_watch.toml` (curado à mão).
`sync()` joga o catálogo pro DB (tabela `eventos_tributarios`), idempotente.
O HTML diário lê do DB via `get_monitor()`.

Comandos:
    python main.py tributario sync                 # TOML -> DB
    python main.py tributario list [--produto X] [--status Y]

Filosofia: tributário/regulatório é DRIVER DIRETO de preço de commodity BR,
não pano de fundo (ver memory feedback_lente_tributaria_br). Este monitor
mantém num lugar só todos os vetores em curso, com status e mecanismo.
"""
from __future__ import annotations

import json
import tomllib
from datetime import date
from pathlib import Path

import db

CATALOG_PATH = Path(__file__).parent / "tributario_watch.toml"

# Ordem de exibição por status (mais "quente" primeiro)
STATUS_ORDER = {"vigente": 0, "tramitacao": 1, "adiado": 2, "monitorando": 3, "encerrado": 4}

CAMPOS = [
    "id", "titulo", "tipo", "jurisdicao", "status", "impacto", "direcao",
    "produtos", "mecanismo", "vigencia_ate", "proximo_marco", "proximo_data",
    "fonte_url", "atualizado_em",
]


def load_catalog() -> list[dict]:
    """Lê o TOML curado e devolve lista de eventos (dicts)."""
    if not CATALOG_PATH.exists():
        return []
    with open(CATALOG_PATH, "rb") as f:
        data = tomllib.load(f)
    return data.get("evento", [])


def sync() -> dict:
    """Sincroniza o catálogo TOML -> tabela eventos_tributarios (INSERT OR REPLACE).

    Idempotente. Remove do DB os ids que sumiram do TOML (mantém DB = TOML).
    """
    db.init_db()  # garante que a tabela existe (schema.sql é IF NOT EXISTS)
    eventos = load_catalog()
    catalog_ids = {e["id"] for e in eventos}
    inseridos, removidos = 0, 0

    with db.connect() as conn:
        for e in eventos:
            produtos = e.get("produtos", [])
            produtos_csv = ",".join(produtos) if isinstance(produtos, list) else str(produtos)
            conn.execute(
                """
                INSERT OR REPLACE INTO eventos_tributarios
                (id, titulo, tipo, jurisdicao, status, impacto, direcao, produtos,
                 mecanismo, vigencia_ate, proximo_marco, proximo_data, fonte_url,
                 atualizado_em, dados_json)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                """,
                (
                    e["id"], e.get("titulo", ""), e.get("tipo", ""), e.get("jurisdicao", ""),
                    e.get("status", ""), e.get("impacto", ""), e.get("direcao", ""),
                    produtos_csv, e.get("mecanismo", ""), e.get("vigencia_ate") or None,
                    e.get("proximo_marco", ""), e.get("proximo_data") or None,
                    e.get("fonte_url", ""), e.get("atualizado_em") or None,
                    json.dumps(e, ensure_ascii=False),
                ),
            )
            inseridos += 1

        # Limpa ids que saíram do catálogo
        existing = {r["id"] for r in conn.execute("SELECT id FROM eventos_tributarios")}
        orfaos = existing - catalog_ids
        for oid in orfaos:
            conn.execute("DELETE FROM eventos_tributarios WHERE id=?", (oid,))
            removidos += 1

    return {"sincronizados": inseridos, "removidos": removidos}


def list_eventos(produto: str | None = None, status: str | None = None) -> list[dict]:
    """Lê eventos do DB, com filtros opcionais. Ordena por status (quente primeiro)."""
    q = "SELECT * FROM eventos_tributarios WHERE 1=1"
    params: list = []
    if produto:
        q += " AND produtos LIKE ?"
        params.append(f"%{produto}%")
    if status:
        q += " AND status = ?"
        params.append(status)
    with db.connect() as conn:
        rows = [dict(r) for r in conn.execute(q, params)]
    rows.sort(key=lambda r: (STATUS_ORDER.get(r.get("status"), 9), r.get("jurisdicao", "")))
    return rows


def get_monitor(target: date | None = None, auto_sync: bool = True) -> dict:
    """Estrutura agregada pro HTML: eventos agrupados + resumo de pressão.

    auto_sync=True ressincroniza do TOML antes de ler (edição no TOML reflete
    no próximo HTML sem passo manual).
    """
    if auto_sync:
        try:
            sync()
        except Exception:
            pass  # se falhar o sync, lê o que tiver no DB

    eventos = list_eventos()
    # Resumo de pressão sobre o preço do complexo
    resumo = {"alta": 0, "baixa": 0, "neutro": 0, "misto": 0, "total": len(eventos)}
    for e in eventos:
        resumo[e.get("direcao", "neutro")] = resumo.get(e.get("direcao", "neutro"), 0) + 1

    # Agrupa por jurisdição
    GRUPOS = [("BR", "🇧🇷 Brasil"), ("EUA", "🇺🇸 Estados Unidos"),
              ("Indonesia", "🌏 Internacional"), ("Argentina", "🌎 Argentina"),
              ("global", "🌐 Global")]
    grupos = []
    usados = set()
    for chave, label in GRUPOS:
        itens = [e for e in eventos if e.get("jurisdicao") == chave]
        for e in itens:
            usados.add(e["id"])
        if itens:
            grupos.append({"label": label, "eventos": itens})
    # Qualquer jurisdição não mapeada
    resto = [e for e in eventos if e["id"] not in usados]
    if resto:
        grupos.append({"label": "Outros", "eventos": resto})

    return {"disponivel": len(eventos) > 0, "grupos": grupos, "resumo": resumo}


if __name__ == "__main__":
    out = sync()
    print(f"[tributario] sincronizados {out['sincronizados']}, removidos {out['removidos']}")
    for e in list_eventos():
        print(f"  [{e['status']:11}] {e['jurisdicao']:9} {e['direcao']:6} {e['titulo']}")
