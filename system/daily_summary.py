# -*- coding: utf-8 -*-
"""Resumo executivo diario do complexo soja — texto curto pronto pra ler no
celular e pra colar no Claude pedindo interpretacao.

Envia via Telegram se TELEGRAM_BOT_TOKEN + TELEGRAM_CHAT_ID estiverem no ambiente
(Secrets do GitHub Actions); senao so escreve em disco e imprime.

Como criar o bot do Telegram (1x, ~2 min):
  1. No Telegram, fale com @BotFather → /newbot → escolha nome → ele te da um TOKEN
  2. Fale qualquer coisa com o seu bot novo (pra abrir conversa)
  3. Abra https://api.telegram.org/bot<TOKEN>/getUpdates → copie o "chat":{"id": ...}
  4. Guarde TOKEN e CHAT_ID nos Secrets do repo (TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID)
"""
import os
from datetime import date, datetime

import config
import db


def _ultimo_e_anterior(fonte, commodity, metrica):
    """(valor_mais_recente, valor_anterior, data_recente) — None se faltar."""
    with db.connect() as conn:
        rows = conn.execute(
            """
            SELECT data_referencia, valor FROM dados_publicos
            WHERE fonte=? AND commodity=? AND metrica=? AND valor IS NOT NULL
            ORDER BY data_referencia DESC LIMIT 2
            """,
            (fonte, commodity, metrica),
        ).fetchall()
    if not rows:
        return None, None, None
    atual = rows[0]["valor"]
    ant = rows[1]["valor"] if len(rows) > 1 else None
    return atual, ant, rows[0]["data_referencia"]


def _ind(metrica):
    v, _, _ = _ultimo_e_anterior("indicators", "complexo_soja", metrica)
    return v


def _seta(atual, ant):
    if atual is None or ant is None:
        return ""
    d = atual - ant
    if abs(d) < 1e-9:
        return "→"
    return "↑" if d > 0 else "↓"


def build_resumo(target: date | None = None) -> str:
    # Texto PURO (sem Markdown): titulos de insight/evento e nomes de metrica com
    # '_' '*' '[' quebram o parse do Telegram (HTTP 400 engolido). Mesma licao do
    # alerts_push (commit 8aad10d). Por isso nenhum '*'/'_' de formatacao aqui.
    target = target or date.today()
    L = [f"📊 Radar Soja — {target.strftime('%d/%m/%Y')}", ""]

    soja, soja_a, _ = _ultimo_e_anterior("cme_cbot", "soja_cbot", "fechamento")
    far, far_a, _ = _ultimo_e_anterior("cme_cbot", "farelo_cbot", "fechamento")
    oleo, oleo_a, _ = _ultimo_e_anterior("cme_cbot", "oleo_cbot", "fechamento")
    ptax, ptax_a, _ = _ultimo_e_anterior("bcb", "usd_brl_ptax", "valor")

    # Paridade CBOT -> BRL (mesmos fatores de notify_html.PARIDADES; constantes fisicas):
    #   soja cents/bu × 0,022046 = R$/sc60kg · farelo USD/sht × 1,10231 = R$/ton
    #   oleo cents/lb × 22,0462 = R$/ton — tudo × USD/BRL
    PARIDADE = {"soja": (0.022046, "/sc", 2),
                "farelo": (1 / 0.907185, "/ton", 0),
                "oleo": (22.0462, "/ton", 0)}

    def _fmt_brl(v, casas):
        s = f"{v:,.{casas}f}"  # en-US 1,234.50
        return s.replace(",", "X").replace(".", ",").replace("X", ".")  # BR 1.234,50

    def _brl(val, key):
        if val is None or ptax is None:
            return ""
        fator, un, casas = PARIDADE[key]
        return f"  ·  R$ {_fmt_brl(val * fator * ptax, casas)}{un}"

    if far is not None:
        d = f" ({far - far_a:+.2f})" if far_a is not None else ""
        L.append(f"Farelo {far:.2f} USD/sht {_seta(far, far_a)}{d}{_brl(far, 'farelo')}")
    if soja is not None:
        d = f" ({(soja - soja_a) / 100:+.2f})" if soja_a is not None else ""
        L.append(f"Soja {soja / 100:.2f} USD/bu {_seta(soja, soja_a)}{d}{_brl(soja, 'soja')}")
    if oleo is not None:
        d = f" ({oleo - oleo_a:+.2f})" if oleo_a is not None else ""
        L.append(f"Óleo {oleo:.2f} cts/lb {_seta(oleo, oleo_a)}{d}{_brl(oleo, 'oleo')}")
    if ptax is not None:
        L.append(f"USD/BRL {ptax:.4f} {_seta(ptax, ptax_a)}")

    L.append("")
    ratio = _ind("far_soj_ratio_pct")
    crush = _ind("crush_margin_usd_bu")
    oilsh = _ind("oil_share_pct")
    if ratio is not None:
        # Spread far÷soj na lente de trader (mean-reversion nos dois lados), nao "compra"
        if ratio < 80:
            zona = "🟢 spread comprimido (farelo barato vs soja)"
        elif ratio < 87:
            zona = "🟡 spread neutro"
        else:
            zona = "🔴 spread esticado (farelo caro vs soja)"
        L.append(f"Ratio Far/Soj {ratio:.1f}% — {zona}")
    if crush is not None:
        L.append(f"Crush {crush:.2f} USD/bu · oil share {oilsh:.1f}%"
                 if oilsh is not None else f"Crush {crush:.2f} USD/bu")

    # Alertas do dia
    try:
        import json
        af = config.DATA_DIR / "alerts_technical.json"
        if af.exists():
            data = json.loads(af.read_text(encoding="utf-8"))
            alerts = data if isinstance(data, list) else data.get("alertas", [])
            if alerts:
                L.append("")
                L.append(f"⚠️ {len(alerts)} alerta(s) técnico(s) hoje")
    except Exception:
        pass

    # Próximos marcos fiscais
    try:
        import tributario as trib
        hoje = target
        prox = [e for e in trib.list_eventos()
                if e.get("proximo_data")
                and 0 <= (date.fromisoformat(e["proximo_data"]) - hoje).days <= 7]
        if prox:
            L.append("")
            L.append("📅 Marcos 7d:")
            for e in sorted(prox, key=lambda x: x["proximo_data"])[:3]:
                L.append(f"  • {e['proximo_data']}: {e['titulo'][:55]}")
    except Exception:
        pass

    # Fila de julgamento — sinais que pedem leitura do Claude
    try:
        import queue_emit
        n_fila = queue_emit.count_pendentes(target)
        if n_fila:
            L.append("")
            L.append(f"🔔 {n_fila} leitura(s) pendente(s) — abra o Claude: \"lê a fila e trata\"")
    except Exception:
        pass

    L.append("")
    L.append("Abra o link do relatório pro detalhe; cole este resumo no Claude pra interpretar.")
    return "\n".join(L)


def enviar(target: date | None = None) -> dict:
    """Monta o resumo, salva em disco e envia via Telegram se configurado."""
    texto = build_resumo(target)

    # Sempre salva em disco (e na pasta do consultor)
    try:
        out = config.DATA_DIR / "resumo_dia.md"
        out.write_text(texto, encoding="utf-8")
    except Exception:
        pass

    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    chat = os.getenv("TELEGRAM_CHAT_ID", "").strip()
    if not token or not chat:
        print("[resumo] Telegram não configurado — só salvei em disco.\n")
        print(texto)
        return {"enviado": False, "motivo": "sem_telegram"}

    try:
        import requests
        # Texto puro (sem parse_mode): Markdown quebrava com '_' '*' '[' dinamicos.
        r = requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            json={"chat_id": chat, "text": texto},
            timeout=30,
        )
        ok = r.status_code == 200
        if ok:
            print("[resumo] Telegram enviado: True (HTTP 200)")
        else:
            # Logar o corpo torna o proximo silencio VISIVEL no log do Actions.
            print(f"[resumo] Telegram FALHOU HTTP {r.status_code}: {r.text[:300]}")
        return {"enviado": ok, "http": r.status_code}
    except Exception as e:
        print(f"[resumo] falha no envio Telegram: {e}")
        return {"enviado": False, "erro": str(e)}


def _fmt_brn(v, casas: int) -> str:
    """Número em formato BR (1.234,56). '—' se None."""
    if v is None:
        return "—"
    s = f"{v:,.{casas}f}"  # en-US 1,234.56
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def _serie_cbot(commodity: str) -> dict | None:
    """{ult, ant, abert} da commodity: último fechamento (vivo), fechamento anterior
    (D-1) e abertura do dia corrente. None se não houver preço."""
    with db.connect() as conn:
        rows = conn.execute(
            "SELECT data_referencia, valor FROM dados_publicos WHERE fonte='cme_cbot' "
            "AND commodity=? AND metrica='fechamento' AND valor IS NOT NULL "
            "ORDER BY data_referencia DESC LIMIT 2", (commodity,)).fetchall()
        if not rows:
            return None
        ult, data_ult = rows[0]["valor"], rows[0]["data_referencia"]
        ant = rows[1]["valor"] if len(rows) > 1 else None
        ab = conn.execute(
            "SELECT valor FROM dados_publicos WHERE fonte='cme_cbot' AND commodity=? "
            "AND metrica='abertura' AND data_referencia=? AND valor IS NOT NULL LIMIT 1",
            (commodity, data_ult)).fetchone()
    return {"ult": ult, "ant": ant, "abert": ab["valor"] if ab else None}


def build_pulso_cbot(target: date | None = None) -> str | None:
    """Pulso CBOT pro Telegram em BLOCOS VERTICAIS (mobile-friendly — linhas curtas,
    sem tabela larga que estoura no celular). Por commodity: bolinha de direção +
    último + variação do dia, e abaixo ant/abertura/unidade. Rodapé: dólar, Far/Soj,
    oil share, crush. None se não houver preço."""
    from datetime import timezone, timedelta
    target = target or date.today()
    # (rótulo, commodity, divisor p/ unidade de tela, casas, unidade)
    COMMS = [("Farelo", "farelo_cbot", 1.0, 2, "US$/sht"),
             ("Soja", "soja_cbot", 100.0, 2, "US$/bu"),
             ("Óleo", "oleo_cbot", 1.0, 2, "¢/lb")]
    blocos = []
    for nome, comm, div, casas, unid in COMMS:
        s = _serie_cbot(comm)
        if not s or s["ult"] is None:
            continue
        ult = s["ult"] / div
        ant = s["ant"] / div if s["ant"] is not None else None
        ab = s["abert"] / div if s["abert"] is not None else None
        if ant is not None and s["ant"]:
            va = ult - ant
            vp = (s["ult"] - s["ant"]) / s["ant"] * 100
            dot = "🟢" if va > 0 else ("🔴" if va < 0 else "⚪")
            sinal, sinal_p = ("+" if va >= 0 else "-"), ("+" if vp >= 0 else "-")
            var_s = f"{sinal}{_fmt_brn(abs(va), casas)} ({sinal_p}{_fmt_brn(abs(vp), 1)}%)"
        else:
            dot, var_s = "⚪", "—"
        blocos.append(
            f"{dot} <b>{nome}</b> {_fmt_brn(ult, casas)}  ·  {var_s}\n"
            f"<i>ant {_fmt_brn(ant, casas)} · abert {_fmt_brn(ab, casas)} · {unid}</i>"
        )
    if not blocos:
        return None

    ptax, _, _ = _ultimo_e_anterior("bcb", "usd_brl_ptax", "valor")
    ratio = _ind("far_soj_ratio_pct")
    oilsh = _ind("oil_share_pct")
    crush = _ind("crush_margin_usd_bu")
    l1 = " · ".join(p for p in [
        f"<b>Dólar</b> {_fmt_brn(ptax, 4)}" if ptax is not None else None,
        f"<b>Far/Soj</b> {_fmt_brn(ratio, 1)}%" if ratio is not None else None,
    ] if p)
    l2 = " · ".join(p for p in [
        f"<b>Oil share</b> {_fmt_brn(oilsh, 1)}%" if oilsh is not None else None,
        f"<b>Crush</b> {_fmt_brn(crush, 2)}" if crush is not None else None,
    ] if p)

    hhmm = (datetime.now(timezone.utc) - timedelta(hours=3)).strftime("%H:%M")
    partes = [f"<b>📈 Pulso CBOT · {hhmm} BRT</b>", "", "\n\n".join(blocos)]
    rod = "\n".join(p for p in [l1, l2] if p)
    if rod:
        partes += ["", rod]
    return "\n".join(partes)


def _em_pregao_cbot() -> bool:
    """True se for dia útil E dentro da janela do day session da CBOT (grãos).
    Janela 13:30–19:20 UTC (~10:30–16:20 BRT) cobre o pregão diurno em CDT/CST.
    Fora disso (overnight/fechado/fim de semana) não manda pulso."""
    from datetime import timezone
    now = datetime.now(timezone.utc)
    if now.weekday() >= 5:                      # 5=sáb, 6=dom — CBOT fechada
        return False
    m = now.hour * 60 + now.minute
    return (13 * 60 + 30) <= m <= (19 * 60 + 20)


def enviar_pulso_cbot(target: date | None = None) -> dict:
    """Envia o pulso CBOT no Telegram (parse_mode HTML — tabela <pre>). O conteúdo é
    só número + nome de commodity, sem <>& dinâmicos, então o HTML não quebra."""
    texto = build_pulso_cbot(target)
    if not texto:
        return {"enviado": False, "motivo": "sem_dado"}
    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    chat = os.getenv("TELEGRAM_CHAT_ID", "").strip()
    if not token or not chat:
        return {"enviado": False, "motivo": "sem_telegram"}
    try:
        import requests
        r = requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            json={"chat_id": chat, "text": texto, "parse_mode": "HTML"}, timeout=30,
        )
        if r.status_code != 200:
            print(f"[pulso] Telegram HTTP {r.status_code}: {r.text[:200]}")
        return {"enviado": r.status_code == 200, "http": r.status_code}
    except Exception as e:
        return {"enviado": False, "erro": str(e)}


def pulso_intraday(target: date | None = None) -> dict:
    """Pulso CBOT a cada ~30 min DENTRO do pregão. O intraday roda de 15 em 15, então
    deduplicamos por SLOT de 30 min (topo/fundo da hora) — 1 pulso por slot. Fora da
    janela do pregão: no-op."""
    from datetime import timezone
    if not _em_pregao_cbot():
        return {"enviado": False, "motivo": "fora_pregao"}
    now = datetime.now(timezone.utc)
    slot = "30" if now.minute >= 30 else "00"
    chave = f"pulso_{now.strftime('%Y%m%d_%H')}{slot}"
    try:
        with db.connect() as conn:
            conn.execute("CREATE TABLE IF NOT EXISTS pipeline_heartbeat "
                         "(evento TEXT PRIMARY KEY, ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
            if conn.execute("SELECT 1 FROM pipeline_heartbeat WHERE evento=?",
                            (chave,)).fetchone():
                return {"enviado": False, "motivo": "ja_enviado_slot"}
    except Exception:
        pass
    res = enviar_pulso_cbot(target)
    if res.get("enviado"):
        try:
            with db.connect() as conn:
                conn.execute("INSERT OR IGNORE INTO pipeline_heartbeat (evento) VALUES (?)", (chave,))
        except Exception:
            pass
    return res


def _resumo_ja_enviado(target: date) -> bool:
    chave = f"resumo_enviado_{target.isoformat()}"
    try:
        with db.connect() as conn:
            conn.execute("CREATE TABLE IF NOT EXISTS pipeline_heartbeat "
                         "(evento TEXT PRIMARY KEY, ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
            return conn.execute("SELECT 1 FROM pipeline_heartbeat WHERE evento=?",
                                (chave,)).fetchone() is not None
    except Exception:
        return False


def _marcar_resumo(target: date):
    chave = f"resumo_enviado_{target.isoformat()}"
    try:
        with db.connect() as conn:
            conn.execute("CREATE TABLE IF NOT EXISTS pipeline_heartbeat "
                         "(evento TEXT PRIMARY KEY, ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
            conn.execute("INSERT OR IGNORE INTO pipeline_heartbeat (evento) VALUES (?)", (chave,))
    except Exception:
        pass


def enviar_diario_uma_vez(target: date | None = None, forcar: bool = False) -> dict:
    """Envia o resumo no MÁXIMO 1×/dia-calendário (dedup no DB).

    Desacopla o resumo do run 'daily' pesado: o intraday (que roda a cada 15 min
    pelo pinger) chama isto após a hora-alvo, então o resumo SAI de forma confiável
    mesmo se o job 'daily' do pinger não disparar. forcar=True (usado pelo daily
    canônico) envia sempre e re-marca — bom pra teste manual."""
    target = target or date.today()
    if not forcar and _resumo_ja_enviado(target):
        return {"enviado": False, "motivo": "ja_enviado_hoje"}
    res = enviar(target)
    if res.get("enviado"):
        _marcar_resumo(target)
    return res


if __name__ == "__main__":
    enviar()
