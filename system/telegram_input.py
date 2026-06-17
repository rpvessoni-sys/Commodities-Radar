# -*- coding: utf-8 -*-
"""Input de preço físico pelo Telegram (sem servidor: poll no run intraday).

O sistema é 100% cron (GitHub Actions), sem processo ligado 24/7 — então o bot não
"escuta" em tempo real. A cada run intraday (~15 min) este módulo chama getUpdates,
lê as mensagens NOVAS do dono (TELEGRAM_CHAT_ID), interpreta e grava o físico em
precos_fisicos (DB). Volume real ~1x/dia, então quase todo poll vem vazio (barato).
Responde confirmação no Telegram. Latência de até ~15 min — irrelevante p/ físico.

Gramática (ordem livre):  [compra|venda] <soja|farelo|oleo> <porto|rancharia> <valor>
  soja porto 122,50            -> compra soja Paranaguá R$ 122,50/sc
  venda farelo rancharia 1850  -> venda  farelo Rancharia R$ 1.850/t
Comandos:  fisico (mostra o físico atual) · ajuda (formato)

Estado (offset do getUpdates) em bot_state. Só processa o chat do dono.
Persistência: grava no DB precos_fisicos (durável via cache do Actions + backup diário).
"""
import os
import time
from datetime import date

import db
import precos_fisicos as pf

PRACA_ALIAS = {
    "porto": "paranagua_pr", "paranagua": "paranagua_pr", "paranaguá": "paranagua_pr",
    "pgua": "paranagua_pr", "paranagua_pr": "paranagua_pr",
    "rancharia": "rancharia_sp", "rancha": "rancharia_sp", "rc": "rancharia_sp",
    "rancharia_sp": "rancharia_sp",
}
PRODUTO_ALIAS = {
    "soja": "soja", "graos": "soja", "grão": "soja", "grao": "soja",
    "farelo": "farelo", "fm": "farelo",
    "oleo": "oleo_soja", "óleo": "oleo_soja", "oleo_soja": "oleo_soja", "degomado": "oleo_soja",
}
TIPO_ALIAS = {
    "compra": "compra", "comprar": "compra", "compro": "compra",
    "venda": "venda", "vender": "venda", "vendo": "venda",
}
NOME = {"soja": "soja", "farelo": "farelo", "oleo_soja": "óleo"}
NOME_PRACA = {"paranagua_pr": "Paranaguá", "rancharia_sp": "Rancharia"}
UNID = {"soja": "R$/sc", "farelo": "R$/t", "oleo_soja": "R$/t"}
# faixas típicas (sanity check de digitação) — fora disso avisa, mas grava
FAIXA = {"soja": (50, 400), "farelo": (800, 4000), "oleo_soja": (3000, 12000)}


def _fmt(v) -> str:
    if v is None:
        return "—"
    s = f"{v:,.2f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def _parse_valor(w: str):
    """Número BR/US, tratando milhar BR (1.850 / 7.200) que o _parse_num confunde."""
    w = w.strip()
    if "." in w and "," not in w:
        a, _, b = w.partition(".")
        if a.isdigit() and len(b) == 3 and b.isdigit():
            w = a + b
    return pf._parse_num(w)


def parse_fisico_msg(texto: str) -> dict:
    """Interpreta uma mensagem. Retorna {ok,...} | {cmd:...} | {erro:...}."""
    t = (texto or "").strip().lower()
    if not t:
        return {"cmd": "ignore"}
    p0 = t.replace("/", " ").split()[0]
    if p0 in ("ajuda", "help", "?", "start", "menu"):
        return {"cmd": "ajuda"}
    if p0 in ("fisico", "físico", "status", "posicao", "posição"):
        return {"cmd": "status"}
    tipo = produto = praca = valor = None
    for w in t.replace("/", " ").split():
        if produto is None and w in PRODUTO_ALIAS:
            produto = PRODUTO_ALIAS[w]
        elif praca is None and w in PRACA_ALIAS:
            praca = PRACA_ALIAS[w]
        elif tipo is None and w in TIPO_ALIAS:
            tipo = TIPO_ALIAS[w]
        elif valor is None:
            n = _parse_valor(w)
            if n is not None:
                valor = n
    if produto and praca and valor is not None and valor > 0:
        return {"ok": True, "produto": produto, "praca": praca,
                "tipo": tipo or "compra", "valor": valor}
    faltou = []
    if not produto:
        faltou.append("produto (soja/farelo/óleo)")
    if not praca:
        faltou.append("praça (porto/rancharia)")
    if valor is None or valor <= 0:
        faltou.append("valor")
    return {"erro": "faltou " + ", ".join(faltou)}


def _send(texto: str):
    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    chat = os.getenv("TELEGRAM_CHAT_ID", "").strip()
    if not token or not chat:
        return
    try:
        import requests
        requests.post(f"https://api.telegram.org/bot{token}/sendMessage",
                      json={"chat_id": chat, "text": texto}, timeout=30)
    except Exception:
        pass


def _state_get(chave):
    try:
        with db.connect() as conn:
            conn.execute("CREATE TABLE IF NOT EXISTS bot_state (chave TEXT PRIMARY KEY, valor TEXT)")
            r = conn.execute("SELECT valor FROM bot_state WHERE chave=?", (chave,)).fetchone()
        return r["valor"] if r else None
    except Exception:
        return None


def _state_set(chave, valor):
    try:
        with db.connect() as conn:
            conn.execute("CREATE TABLE IF NOT EXISTS bot_state (chave TEXT PRIMARY KEY, valor TEXT)")
            conn.execute("INSERT INTO bot_state (chave, valor) VALUES (?, ?) "
                         "ON CONFLICT(chave) DO UPDATE SET valor=excluded.valor", (chave, str(valor)))
    except Exception:
        pass


def _ajuda_texto() -> str:
    return ("📥 Input de físico:\n"
            "<produto> <praça> <valor>\n\n"
            "produtos: soja · farelo · óleo\n"
            "praças: porto · rancharia\n\n"
            "ex: soja porto 122,50\n"
            "ex: farelo rancharia 1850\n"
            "ex: venda óleo porto 7200\n\n"
            "ver o que está registrado: fisico")


def _status_texto() -> str:
    linhas = ["📋 Seu físico (último por praça):"]
    achou = False
    try:
        with db.connect() as conn:
            for prod in ("soja", "farelo", "oleo_soja"):
                for praca in ("paranagua_pr", "rancharia_sp"):
                    r = conn.execute(
                        "SELECT valor_brl_sc v, tipo_posicao t, data d FROM precos_fisicos "
                        "WHERE produto=? AND praca=? ORDER BY data DESC, id DESC LIMIT 1",
                        (prod, praca)).fetchone()
                    if r and r["v"] is not None:
                        achou = True
                        linhas.append(f"{NOME[prod]} {NOME_PRACA[praca]}: {_fmt(r['v'])} {UNID[prod]} "
                                      f"({r['t']}, {r['d'][5:]})")
    except Exception as e:
        return f"erro ao ler físico: {e}"
    if not achou:
        linhas.append("(nada registrado ainda)")
    return "\n".join(linhas)


def poll_and_apply(target: date | None = None) -> int:
    """Lê mensagens novas do dono via getUpdates e aplica o físico. Retorna quantos
    inputs gravou. No-op se Telegram não configurado. Chamado no run intraday."""
    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    chat = os.getenv("TELEGRAM_CHAT_ID", "").strip()
    if not token or not chat:
        return 0
    target = target or date.today()

    offset = _state_get("tg_offset")
    params = {"timeout": 0}
    if offset:
        try:
            params["offset"] = int(offset) + 1
        except (ValueError, TypeError):
            pass
    try:
        import requests
        resp = requests.get(f"https://api.telegram.org/bot{token}/getUpdates",
                            params=params, timeout=30)
        data = resp.json()
    except Exception:
        return 0
    if not isinstance(data, dict) or not data.get("ok"):
        return 0

    aplicados = 0
    last = None
    agora = time.time()
    for upd in data.get("result", []):
        last = upd.get("update_id")
        msg = upd.get("message") or upd.get("edited_message") or {}
        if str(msg.get("chat", {}).get("id")) != chat:
            continue                                   # só o dono
        if agora - (msg.get("date") or 0) > 86400:
            continue                                   # >24h = backlog velho, ignora
        r = parse_fisico_msg(msg.get("text", ""))
        if r.get("cmd") == "status":
            _send(_status_texto())
        elif r.get("cmd") == "ajuda":
            _send(_ajuda_texto())
        elif r.get("cmd") == "ignore":
            pass
        elif r.get("ok"):
            try:
                pf.add_preco(target, r["praca"], r["valor"], produto=r["produto"],
                             tipo_posicao=r["tipo"], observacao="via Telegram")
                lo, hi = FAIXA.get(r["produto"], (0, 1e12))
                aviso = "  ⚠ valor incomum, confere?" if not (lo <= r["valor"] <= hi) else ""
                _send(f"✅ registrado — {r['tipo']} · {NOME[r['produto']]} · {NOME_PRACA[r['praca']]} · "
                      f"{_fmt(r['valor'])} {UNID[r['produto']]} · {target.strftime('%d/%m')}{aviso}")
                aplicados += 1
            except Exception as e:
                _send(f"⚠️ erro ao gravar: {e}")
        elif r.get("erro"):
            _send(f"não entendi — {r['erro']}.\nex: soja porto 122,50  ·  digite ajuda")

    if last is not None:
        _state_set("tg_offset", last)
    return aplicados


if __name__ == "__main__":
    print(f"[telegram_input] {poll_and_apply()} input(s) aplicado(s)")
