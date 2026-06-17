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


def build_pulso_cbot(target: date | None = None) -> str | None:
    """Linha compacta de pulso CBOT (1 linha) pro Telegram intraday.
    Ex: '📈 CBOT 14:30 BRT — Farelo 305.50 ↑ · Soja 11.32 ↑ · Óleo 71.60 ↓ · Far/Soj 79.7%'
    Setas = direção vs fechamento anterior (D-1). None se não houver preço."""
    from datetime import timezone, timedelta
    target = target or date.today()
    soja, soja_a, _ = _ultimo_e_anterior("cme_cbot", "soja_cbot", "fechamento")
    far, far_a, _ = _ultimo_e_anterior("cme_cbot", "farelo_cbot", "fechamento")
    oleo, oleo_a, _ = _ultimo_e_anterior("cme_cbot", "oleo_cbot", "fechamento")
    if far is None and soja is None and oleo is None:
        return None
    partes = []
    if far is not None:
        partes.append(f"Farelo {far:.2f} {_seta(far, far_a)}")
    if soja is not None:
        partes.append(f"Soja {soja / 100:.2f} {_seta(soja, soja_a)}")
    if oleo is not None:
        partes.append(f"Óleo {oleo:.2f} {_seta(oleo, oleo_a)}")
    ratio = _ind("far_soj_ratio_pct")
    if ratio is not None:
        partes.append(f"Far/Soj {ratio:.1f}%")
    hhmm = (datetime.now(timezone.utc) - timedelta(hours=3)).strftime("%H:%M")
    return f"📈 CBOT {hhmm} BRT — " + " · ".join(partes)


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
    """Envia o pulso CBOT no Telegram (texto puro). No-op se Telegram off ou sem dado."""
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
            json={"chat_id": chat, "text": texto}, timeout=30,
        )
        return {"enviado": r.status_code == 200, "http": r.status_code}
    except Exception as e:
        return {"enviado": False, "erro": str(e)}


def pulso_intraday(target: date | None = None) -> dict:
    """Pulso CBOT a cada run intraday DENTRO do pregão. Fora da janela: no-op."""
    if not _em_pregao_cbot():
        return {"enviado": False, "motivo": "fora_pregao"}
    return enviar_pulso_cbot(target)


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
