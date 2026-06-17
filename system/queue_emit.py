# -*- coding: utf-8 -*-
"""Fila de julgamento — emissor DETERMINISTICO (sem LLM) do que "pede leitura".

A camada de FATO (robo) coleta numeros e calcula indicadores. Esta funcao olha
o estado atual e lista os SINAIS que merecem INTERPRETACAO do Claude — nao a
opiniao em si, so o fato + a pergunta de leitura. O Claude (em sessao) le a fila,
trata, e escreve a opiniao em insights/*.md (camada de LEITURA, separada).

Por que efemera: a fila e regenerada a cada `main.py queue` a partir do DB; NAO
e commitada (data/ e gitignored, e versionar estado poluiria o repo). O "ja
tratei" mora no proprio insight (cita o id da fila no corpo).

Regras (conservadoras de proposito — comecar so com sinal alto, igual fizemos
com o alerts_config; afrouxar com calibracao):
  1. ratio Far/Soj cruzou banda de zona do spread (<80 comprimido / 80-87 neutro / >=87 esticado)
  2. nivel de tese rompido (alerts_config via alerts_technical.check_alerts)
  3. evento tributario com proximo marco em <=7 dias
  4. release de fundamento com data inedita (WASDE/NOPA/ABIOVE/COT) <=3 dias
  5. revisao programada de insight (D+N) vencendo em <=7 dias ou vencida

Comando: python main.py queue
"""
from datetime import date

import db
import alerts_technical
import tributario
import insights as ins_mod

_ORDEM_SEV = {"alta": 0, "media": 1, "baixa": 2}


def _zona_ratio(v: float) -> str:
    if v < 80:
        return "comprimido"
    if v < 87:
        return "neutro"
    return "esticado"


def build_queue(target: date | None = None) -> list[dict]:
    """Retorna lista de itens {id, tipo, severidade, titulo, evidencia, refs, pergunta}."""
    target = target or date.today()
    itens: list[dict] = []

    # --- Regra 1: ratio Far/Soj cruzou zona ---
    with db.connect() as conn:
        rows = conn.execute(
            """
            SELECT data_referencia, valor FROM dados_publicos
            WHERE fonte='indicators' AND commodity='complexo_soja'
              AND metrica='far_soj_ratio_pct' AND valor IS NOT NULL
            ORDER BY data_referencia DESC LIMIT 2
            """
        ).fetchall()
    if len(rows) >= 2:
        atual, ant = rows[0]["valor"], rows[1]["valor"]
        za, zp = _zona_ratio(atual), _zona_ratio(ant)
        if za != zp:
            # Trader opera mean-reversion nos DOIS lados: ambos os extremos do spread
            # (comprimido <80 = long farelo/short soja; esticado >=87 = o inverso) sao
            # acionaveis -> 'alta' (dispara o push). So a zona neutra fica 'media'.
            sev = "alta" if za in ("comprimido", "esticado") else "media"
            itens.append({
                "id": f"ratio-zona-{rows[0]['data_referencia']}",
                "tipo": "ratio_zona", "severidade": sev,
                "titulo": f"Ratio Far/Soj entrou na zona '{za}' ({atual:.1f}%, era '{zp}' {ant:.1f}%)",
                "evidencia": f"far_soj_ratio_pct {ant:.1f}% -> {atual:.1f}% em {rows[0]['data_referencia']} (indicators/DB)",
                "refs": "farelo",
                "pergunta": "Muda a leitura do spread Far/Soj (mean-reversion, os dois lados)?",
            })

    # --- Regra 2: nivel de tese rompido (alerts_config) ---
    try:
        for a in alerts_technical.check_alerts(target):
            nivel = a.get("nivel", a.get("valor_anterior", ""))
            va = a.get("valor_atual")
            va_s = f"{va:.2f}" if isinstance(va, (int, float)) else str(va)
            niv_s = f"{nivel:.2f}" if isinstance(nivel, (int, float)) else str(nivel)
            itens.append({
                "id": f"alerta-{a.get('tipo')}-{a.get('commodity')}-{a.get('data','')}",
                "tipo": "nivel_tese", "severidade": "alta",
                "titulo": a.get("msg", "nivel rompido"),
                "evidencia": f"{a.get('commodity')} = {va_s} vs nivel {niv_s} ({a.get('data')})",
                "refs": a.get("commodity", ""),
                "pergunta": "Confirma ou muda a tese? O que voce faria diferente sabendo disso?",
            })
    except Exception as e:
        itens.append(_erro("nivel_tese", e))

    # --- Regra 3: evento tributario com proximo marco <=7d ---
    try:
        for e in tributario.list_eventos():
            pd = e.get("proximo_data")
            if not pd:
                continue
            try:
                dias = (date.fromisoformat(pd) - target).days
            except (ValueError, TypeError):
                continue
            if 0 <= dias <= 7:
                eid = e.get("id") or (e.get("titulo", "ev")[:20])
                itens.append({
                    "id": f"trib-{eid}-{pd}",
                    "tipo": "tributario", "severidade": "media",
                    "titulo": f"[{dias}d] {e.get('titulo','')}",
                    "evidencia": f"proximo marco {pd}: {e.get('proximo_marco','')} "
                                 f"(direcao {e.get('direcao')}, status {e.get('status')})",
                    "refs": e.get("produtos", ""),
                    "pergunta": "Vira ou atualiza insight com vies?",
                })
    except Exception as e:
        itens.append(_erro("tributario", e))

    # --- Regra 4: release de fundamento com data inedita ---
    fundamentos = [("usda_wasde", "WASDE"), ("nopa", "NOPA"),
                   ("abiove", "ABIOVE"), ("cftc_cot", "COT")]
    with db.connect() as conn:
        for fonte, nome in fundamentos:
            r = conn.execute(
                "SELECT MAX(data_referencia) d FROM dados_publicos WHERE fonte=?",
                (fonte,),
            ).fetchone()
            if not r or not r["d"]:
                continue
            try:
                dias = (target - date.fromisoformat(r["d"][:10])).days
            except (ValueError, TypeError):
                continue
            if 0 <= dias <= 3:
                itens.append({
                    "id": f"release-{fonte}-{r['d'][:10]}",
                    "tipo": "release", "severidade": "media",
                    "titulo": f"{nome} novo ({r['d'][:10]})",
                    "evidencia": f"fonte {fonte} com data {r['d'][:10]} — coletado, ainda nao interpretado",
                    "refs": "complexo_soja",
                    "pergunta": "O numero muda o balanco/tese? Algo relevante pro farelo?",
                })

    # --- Regra 5: revisao de insight (D+N) vencendo <=7d ou vencida ---
    try:
        for ins in ins_mod.list_insights():
            if (ins.get("status") or "").lower() not in ("ativa", "revisada"):
                continue
            for rev in ins_mod._extract_revisoes(ins.get("body_md", "")):
                try:
                    dias = (date.fromisoformat(rev["data"]) - target).days
                except (ValueError, KeyError, TypeError):
                    continue
                if dias <= 7:
                    sev = "alta" if dias < 0 else "media"
                    venc = "VENCIDA" if dias < 0 else f"em {dias}d"
                    itens.append({
                        "id": f"revisao-{ins.get('slug','?')}-{rev.get('label','D')}",
                        "tipo": "revisao", "severidade": sev,
                        "titulo": f"Revisao {rev.get('label')} {venc}: {ins.get('titulo','')[:55]}",
                        "evidencia": f"{rev.get('label')} {rev.get('data')} — {(rev.get('texto') or '')[:80]}",
                        "refs": ",".join((ins.get("tags") or [])[:3]),
                        "pergunta": "A tese se confirmou? Atualizar status/insight.",
                    })
    except Exception as e:
        itens.append(_erro("revisao", e))

    itens.sort(key=lambda x: _ORDEM_SEV.get(x.get("severidade"), 3))
    return itens


def _erro(tipo: str, e: Exception) -> dict:
    return {
        "id": f"erro-{tipo}", "tipo": "erro", "severidade": "baixa",
        "titulo": f"[regra {tipo} falhou: {type(e).__name__}]",
        "evidencia": str(e)[:120], "refs": "", "pergunta": "ignorar (problema tecnico)",
    }


_SEV_ICON = {"alta": "🔴", "media": "🟡", "baixa": "⚪"}


def render_markdown(itens: list[dict], target: date | None = None) -> str:
    target = target or date.today()
    if not itens:
        return (f"# Fila de julgamento — {target.isoformat()}\n\n"
                "Nada pede leitura hoje. ✅ (o dash do robo segue 100% valido)")
    L = [f"# Fila de julgamento — {target.isoformat()}", "",
         f"**{len(itens)} item(ns).** Frase-gatilho: \"lê a fila de julgamento e trata\"", ""]
    for it in itens:
        L.append(f"## {_SEV_ICON.get(it['severidade'],'')} [{it['tipo']}] {it['titulo']}")
        L.append(f"- id: `{it['id']}`")
        L.append(f"- fato: {it['evidencia']}")
        if it.get("refs"):
            L.append(f"- refs: {it['refs']}")
        L.append(f"- leitura: {it['pergunta']}")
        L.append("")
    L.append("---")
    L.append("Trate só 🔴/🟡. Saída = `insights/*.md` (formato de generate_insights.txt, com `vies:`). "
             "Cite o `id` da fila no corpo do insight. Máx 1-3. Não duplicar insight recente.")
    return "\n".join(L)


def count_pendentes(target: date | None = None) -> int:
    """Quantos itens 'alta'/'media' (pro badge do dash e contagem no Telegram)."""
    return len([i for i in build_queue(target) if i.get("severidade") in ("alta", "media")])


if __name__ == "__main__":
    print(render_markdown(build_queue()))
