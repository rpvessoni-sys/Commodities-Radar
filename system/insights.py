"""Gestão de insights de estudo (markdown files com frontmatter YAML).

Lê arquivos .md da pasta `insights/` no root do projeto. Cada arquivo segue:

    ---
    data: 2026-05-26
    titulo: B16 → bullish farelo (comprador)
    tags: [biodiesel, farelo, oleo_soja]
    fontes:
      - StoneX dashboard
      - Reunião Fabio Cruz
    status: ativa
    ---

    ## Resumo executivo
    - Ponto 1
    - Ponto 2

    ## Próximas ações
    - [ ] Ação 1

    ## Revisão programada
    - D+90: 2026-08-26

Sistema lista todos, ordena por data DESC, extrai o resumo executivo e
renderiza na aba 💡 Insights do HTML.

CLI:
    python main.py insight new "Título do insight"      # cria template novo
    python main.py insight list                         # lista todos
    python main.py insight open <slug>                  # abre no editor
"""
import re
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Iterable


INSIGHTS_DIR = Path(__file__).resolve().parent.parent / "insights"


def _slugify(text: str) -> str:
    """Converte 'B16 bullish farelo' em 'b16-bullish-farelo'."""
    s = text.lower()
    s = re.sub(r"[áàâãä]", "a", s)
    s = re.sub(r"[éèêë]", "e", s)
    s = re.sub(r"[íìîï]", "i", s)
    s = re.sub(r"[óòôõö]", "o", s)
    s = re.sub(r"[úùûü]", "u", s)
    s = re.sub(r"[ç]", "c", s)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s[:60]


def _parse_frontmatter(content: str) -> tuple[dict, str]:
    """Extrai YAML frontmatter (parser simples, não requer PyYAML)."""
    if not content.startswith("---"):
        return {}, content
    end = content.find("\n---", 3)
    if end < 0:
        return {}, content
    fm_raw = content[3:end].strip()
    body = content[end + 4:].lstrip("\n")

    fm = {}
    current_key = None
    current_list = None
    for line in fm_raw.split("\n"):
        if not line.strip():
            continue
        # Lista item (começa com "  - " ou "- ")
        if re.match(r"^\s*-\s+", line):
            item = re.sub(r"^\s*-\s+", "", line).strip()
            if current_list is not None:
                current_list.append(item)
            continue
        # Chave: valor
        m = re.match(r"^(\w+)\s*:\s*(.*)$", line)
        if m:
            key = m.group(1).strip()
            val = m.group(2).strip()
            # Valor inline lista: [a, b, c]
            if val.startswith("[") and val.endswith("]"):
                items = [x.strip() for x in val[1:-1].split(",") if x.strip()]
                fm[key] = items
                current_list = None
            elif val == "":
                # Lista que virá nas próximas linhas
                fm[key] = []
                current_list = fm[key]
            else:
                fm[key] = val
                current_list = None
            current_key = key
    return fm, body


def _extract_resumo_executivo(body: str) -> list[str]:
    """Pega a primeira seção '## Resumo executivo' como lista de bullets."""
    m = re.search(r"##\s*Resumo executivo\s*\n", body, re.IGNORECASE)
    if not m:
        return []
    start = m.end()
    # Pega até a próxima seção ## ou fim
    next_section = re.search(r"\n##\s+", body[start:])
    end = start + next_section.start() if next_section else len(body)
    section = body[start:end].strip()

    bullets = []
    for line in section.split("\n"):
        line = line.strip()
        if line.startswith("- ") or line.startswith("* "):
            bullets.append(line[2:].strip())
        elif line.startswith("• "):
            bullets.append(line[2:].strip())
    return bullets


def _extract_proximas_acoes(body: str) -> list[dict]:
    """Pega seção '## Próximas ações' — bullets com [ ] ou [x]."""
    m = re.search(r"##\s*Próximas ações\s*\n", body, re.IGNORECASE)
    if not m:
        return []
    start = m.end()
    next_section = re.search(r"\n##\s+", body[start:])
    end = start + next_section.start() if next_section else len(body)
    section = body[start:end].strip()

    out = []
    for line in section.split("\n"):
        line = line.strip()
        m_done = re.match(r"^- \[x\] (.+)$", line, re.IGNORECASE)
        m_todo = re.match(r"^- \[\s?\] (.+)$", line)
        if m_done:
            out.append({"texto": m_done.group(1), "done": True})
        elif m_todo:
            out.append({"texto": m_todo.group(1), "done": False})
    return out


def _extract_revisoes(body: str) -> list[dict]:
    """Pega a seção '## Revisão programada' — linhas `- **D+N**: YYYY-MM-DD ...`.

    Adicionado 2026-06-11: as datas de revisão eram texto morto (ninguém
    cobrava — foi assim que o tese_journal morreu). Agora viram fila visível
    no Dashboard e no `main.py status`.
    """
    m = re.search(r"##\s*Revisão programada\s*\n", body, re.IGNORECASE)
    if not m:
        return []
    start = m.end()
    next_section = re.search(r"\n##\s+", body[start:])
    end = start + next_section.start() if next_section else len(body)
    out = []
    for line in body[start:end].split("\n"):
        mm = re.match(r"^-\s+\*\*(D\+\d+)\*\*\s*:\s*(\d{4}-\d{2}-\d{2})\s*(?:—|-)?\s*(.*)$",
                      line.strip())
        if mm:
            out.append({"label": mm.group(1), "data": mm.group(2),
                        "texto": mm.group(3).strip()})
    return out


def list_insights() -> list[dict]:
    """Lista todos os insights, ordenados por (data DESC, mtime DESC).

    Empate de data: o arquivo mais recentemente criado/modificado vai pra cima.
    Garante que insights do mesmo dia respeitem ordem de criação real
    (e não a ordem alfabética do filename).
    """
    if not INSIGHTS_DIR.exists():
        return []
    out = []
    for f in INSIGHTS_DIR.glob("*.md"):
        if f.name.upper() == "README.MD":
            continue
        try:
            content = f.read_text(encoding="utf-8")
        except Exception:
            continue
        fm, body = _parse_frontmatter(content)
        # Data do frontmatter ou inferida do nome
        data_str = fm.get("data") or _infer_date_from_filename(f.name)
        try:
            data_dt = datetime.fromisoformat(data_str).date() if data_str else None
        except (ValueError, TypeError):
            data_dt = None
        try:
            mtime = f.stat().st_mtime
        except Exception:
            mtime = 0.0
        out.append({
            "arquivo": str(f),
            "slug": f.stem,
            "data": data_dt.isoformat() if data_dt else "",
            "data_dt": data_dt,
            "mtime": mtime,
            "titulo": fm.get("titulo") or f.stem.replace("-", " "),
            "tags": fm.get("tags") or [],
            "fontes": fm.get("fontes") or [],
            "status": fm.get("status") or "ativa",
            # vies: tokens direcao-produto (ex: [bull-farelo, bear-oleo_soja]) —
            # alimenta os Drivers ativos por commodity no HTML (2026-06-11)
            "vies": fm.get("vies") or [],
            "resumo": _extract_resumo_executivo(body),
            "proximas_acoes": _extract_proximas_acoes(body),
            "revisoes": _extract_revisoes(body),
            "body_md": body,
        })
    # Ordenação dupla: data primeiro, mtime como tiebreaker
    out.sort(key=lambda x: (x["data_dt"] or date.min, x["mtime"]), reverse=True)
    return out


def _infer_date_from_filename(fname: str) -> str | None:
    m = re.match(r"^(\d{4}-\d{2}-\d{2})_", fname)
    return m.group(1) if m else None


def create_insight(titulo: str, data_ref: date | None = None) -> Path:
    """Cria novo arquivo .md com template."""
    INSIGHTS_DIR.mkdir(parents=True, exist_ok=True)
    data_ref = data_ref or date.today()
    slug = _slugify(titulo)
    if not slug:
        slug = "insight"
    fname = f"{data_ref.isoformat()}_{slug}.md"
    path = INSIGHTS_DIR / fname
    if path.exists():
        # Sufixa com -2, -3 etc
        i = 2
        while (INSIGHTS_DIR / f"{data_ref.isoformat()}_{slug}-{i}.md").exists():
            i += 1
        path = INSIGHTS_DIR / f"{data_ref.isoformat()}_{slug}-{i}.md"

    d90 = (data_ref.replace(day=1) if data_ref.day > 28 else data_ref).toordinal() + 90
    from datetime import date as _date
    d90_str = _date.fromordinal(d90).isoformat()
    d180_str = _date.fromordinal(data_ref.toordinal() + 180).isoformat()

    template = f"""---
data: {data_ref.isoformat()}
titulo: {titulo}
tags: []
fontes:
  -
status: ativa
vies: []
---
<!-- vies: tokens direcao-produto que alimentam os Drivers do HTML.
     Ex: vies: [bear-farelo, bull-oleo_soja]. Produtos: soja|farelo|oleo_soja. -->


## Resumo executivo

- Ponto-chave 1 (uma linha curta)
- Ponto-chave 2
- Ponto-chave 3
- Conclusão / ação sugerida

## Contexto / dados

(texto livre, opcional)

## Pergunta-tese

O que precisa ser verdadeiro pra essa tese se confirmar:

-

## Próximas ações

- [ ] Ação 1
- [ ] Ação 2

## Revisão programada

- **D+90**: {d90_str} — revisar se mercado moveu na direção prevista
- **D+180**: {d180_str} — fechar ciclo, marcar status (acerto/erro/parcial)
"""
    path.write_text(template, encoding="utf-8")
    return path


# ============================================================
# CLI
# ============================================================

def cli_new(args):
    """Cria novo insight com template."""
    titulo = args.titulo
    if isinstance(titulo, list):
        titulo = " ".join(titulo)
    path = create_insight(titulo)
    print(f"OK criado: {path}")
    print()
    print("Abra no editor pra preencher:")
    print(f"  notepad \"{path}\"")
    print(f"  code \"{path}\"")
    if args.open:
        try:
            subprocess.Popen(["notepad", str(path)])
            print("(abrindo no Notepad)")
        except Exception as e:
            print(f"(nao consegui abrir editor: {e})")


def cli_list(args):
    insights = list_insights()
    if not insights:
        print("Sem insights ainda. Use 'python main.py insight new \"título\"' pra criar.")
        return
    print()
    print(f"  {len(insights)} insight(s):")
    print(f"  {'DATA':10s}  {'STATUS':10s}  {'TÍTULO':50s}  TAGS")
    print("  " + "-" * 100)
    for i in insights:
        tags = ", ".join(i["tags"][:3])
        print(f"  {i['data']:10s}  {i['status']:10s}  {i['titulo'][:50]:50s}  {tags}")


def cli_open(args):
    """Abre insight no editor por slug ou nome parcial."""
    insights = list_insights()
    matches = [i for i in insights if args.slug in i["slug"]]
    if not matches:
        print(f"Nenhum insight com slug parcial '{args.slug}'.")
        return
    if len(matches) > 1:
        print(f"Múltiplos matches:")
        for m in matches:
            print(f"  {m['slug']} ({m['data']})")
        return
    path = matches[0]["arquivo"]
    try:
        subprocess.Popen(["notepad", path])
        print(f"OK abrindo {path}")
    except Exception as e:
        print(f"Erro abrindo editor: {e}")
        print(f"Arquivo: {path}")
