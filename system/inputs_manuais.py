# -*- coding: utf-8 -*-
"""Ponte da camada MANUAL pro pipeline (inclusive na nuvem).

Problema que resolve: preco fisico do usuario, curva do consultor (call do Fabio)
e parametros (RIN D4 etc) so existiam onde o usuario DIGITAVA — invisiveis pro
GitHub Actions. Agora vivem num arquivo versionado `inputs_manuais.toml` na raiz:
o usuario edita, da git push, e a nuvem aplica no proximo run.

Fonte da verdade = o TOML. `sync()` faz upsert idempotente no DB reusando as
funcoes que ja existem (precos_fisicos.add_preco, curvas.set_curva,
params_user.set_param). Roda cedo no pipeline (antes dos indicadores), porque
fisico/params alimentam calculos.

Nao toca em dado AUTOMATICO: fisico manual entra como tipo_posicao do bloco
(default 'compra', aceita 'venda' p/ o trader que opera os dois lados — separado
do indicador CEPEA via UNIQUE), curva entra como fonte='stonex'.

CLI:
    python main.py inputs sync     # aplica o TOML no DB
    python main.py inputs show     # mostra o que o TOML contem
"""
from datetime import date
from pathlib import Path

import config

TOML_PATH = Path(config.ROOT) / "inputs_manuais.toml"

PRODUTOS_FISICO = {"soja", "farelo", "oleo_soja"}
PRODUTOS_CURVA = {"soja", "farelo", "oleo", "oleo_soja", "óleo"}


def _parse(texto: str) -> dict:
    """Parse PURO do TOML em listas normalizadas (sem tocar no DB) — testavel.

    Retorna {'fisico': [...], 'curva': [...], 'param': [...], 'erros': [...]}.
    Blocos invalidos viram erro (string) em vez de quebrar.
    """
    import tomllib
    out = {"fisico": [], "curva": [], "param": [], "erros": []}
    try:
        dados = tomllib.loads(texto)
    except Exception as e:
        out["erros"].append(f"TOML invalido: {e}")
        return out

    for i, b in enumerate(dados.get("fisico", [])):
        try:
            prod = str(b["produto"]).strip()
            if prod not in PRODUTOS_FISICO:
                raise ValueError(f"produto '{prod}' invalido")
            tipo = str(b.get("tipo", "compra")).strip().lower()
            if tipo not in ("compra", "venda"):
                raise ValueError(f"tipo '{tipo}' invalido (use 'compra' ou 'venda')")
            out["fisico"].append({
                "data": str(b["data"]),
                "produto": prod,
                "praca": str(b["praca"]).strip(),
                "tipo": tipo,
                "valor": float(b["valor"]),
                "valor_usd": float(b["valor_usd"]) if b.get("valor_usd") is not None else None,
                "obs": b.get("obs"),
            })
        except Exception as e:
            out["erros"].append(f"[[fisico]] #{i+1}: {e}")

    for i, b in enumerate(dados.get("curva", [])):
        try:
            prod = str(b["produto"]).strip()
            if prod not in PRODUTOS_CURVA:
                raise ValueError(f"produto '{prod}' invalido")
            out["curva"].append({
                "produto": prod,
                "venc": str(b["venc"]).strip().upper(),
                "valor": float(b["valor"]),
                "detalhe": b.get("detalhe"),
            })
        except Exception as e:
            out["erros"].append(f"[[curva]] #{i+1}: {e}")

    for i, b in enumerate(dados.get("param", [])):
        try:
            out["param"].append({
                "chave": str(b["chave"]).strip(),
                "valor": float(b["valor"]),
                "unidade": b.get("unidade"),
                "fonte": b.get("fonte"),
            })
        except Exception as e:
            out["erros"].append(f"[[param]] #{i+1}: {e}")

    return out


def sync(verbose: bool = True) -> dict:
    """Le o TOML e aplica no DB (upsert idempotente). No-op se o arquivo nao existe."""
    if not TOML_PATH.exists():
        if verbose:
            print(f"[inputs] {TOML_PATH.name} nao existe — nada a aplicar.")
        return {"fisico": 0, "curva": 0, "param": 0, "erros": []}

    parsed = _parse(TOML_PATH.read_text(encoding="utf-8"))

    import precos_fisicos as pf
    import curvas as cv
    import params_user as pu

    n_fis = n_cur = n_par = 0
    for f in parsed["fisico"]:
        try:
            pf.add_preco(
                date.fromisoformat(f["data"]), f["praca"], f["valor"],
                produto=f["produto"], tipo_posicao=f.get("tipo", "compra"),
                valor_usd_sc=f["valor_usd"], observacao=f.get("obs"),
            )
            n_fis += 1
        except Exception as e:
            parsed["erros"].append(f"fisico {f.get('produto')}/{f.get('praca')}: {e}")

    for c in parsed["curva"]:
        try:
            cv.set_curva("stonex", c["produto"], c["venc"], c["valor"],
                         fonte_detalhe=c.get("detalhe"))
            n_cur += 1
        except Exception as e:
            parsed["erros"].append(f"curva {c.get('produto')}/{c.get('venc')}: {e}")

    for p in parsed["param"]:
        try:
            pu.set_param(p["chave"], p["valor"], unidade=p.get("unidade"), fonte=p.get("fonte"))
            n_par += 1
        except Exception as e:
            parsed["erros"].append(f"param {p.get('chave')}: {e}")

    if verbose:
        print(f"[inputs] aplicados: {n_fis} fisico, {n_cur} curva, {n_par} param"
              + (f" — {len(parsed['erros'])} erro(s)" if parsed["erros"] else ""))
        for e in parsed["erros"]:
            print(f"  ! {e}")

    return {"fisico": n_fis, "curva": n_cur, "param": n_par, "erros": parsed["erros"]}


# ============================================================
# CLI
# ============================================================

def cli(args):
    action = getattr(args, "inputs_action", "sync")
    if action == "show":
        if not TOML_PATH.exists():
            print(f"{TOML_PATH.name} nao existe.")
            return
        parsed = _parse(TOML_PATH.read_text(encoding="utf-8"))
        print(f"\n{TOML_PATH.name}:")
        print(f"  {len(parsed['fisico'])} fisico, {len(parsed['curva'])} curva, "
              f"{len(parsed['param'])} param")
        for f in parsed["fisico"]:
            print(f"  fisico  {f['data']} {f['produto']:<10} {f['praca']:<14} {f['tipo']:<7} {f['valor']}")
        for c in parsed["curva"]:
            print(f"  curva   stonex {c['produto']:<10} {c['venc']:<5} {c['valor']}")
        for p in parsed["param"]:
            print(f"  param   {p['chave']:<32} {p['valor']}")
        if parsed["erros"]:
            print("  ERROS:")
            for e in parsed["erros"]:
                print(f"   ! {e}")
    else:
        sync()


if __name__ == "__main__":
    sync()
