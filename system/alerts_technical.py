"""Alertas tecnicos — detecta niveis criticos quebrados.

Config em alerts_config.toml:
- Por commodity, define suporte/resistencia e bandas de atencao
- Sistema verifica ultimas cotacoes vs niveis e gera alerta

Salva alertas em shared/to_consultor/alerts/ (compartilhado) e data/alerts.json.

Comando:
    python main.py alerts          # roda detector
"""
import json
import tomllib
from datetime import date, datetime
from pathlib import Path
import config
import db

CONFIG_PATH = Path(__file__).parent / "alerts_config.toml"


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        return {"niveis": []}
    with open(CONFIG_PATH, "rb") as f:
        return tomllib.load(f)


def check_alerts(target_date: date | None = None) -> list[dict]:
    target = target_date or date.today()
    cfg = load_config()
    alertas = []

    with db.connect() as conn:
        for nivel in cfg.get("niveis", []):
            commodity = nivel["commodity"]
            metrica = nivel.get("metrica", "fechamento")
            cur = conn.execute(
                """
                SELECT data_referencia, valor
                FROM dados_publicos
                WHERE commodity = ? AND metrica = ?
                  AND data_referencia >= date(?, '-7 days')
                ORDER BY data_referencia DESC
                LIMIT 5
                """,
                (commodity, metrica, target.isoformat()),
            )
            rows = cur.fetchall()
            if not rows:
                continue

            ultimo = rows[0]
            valor_atual = ultimo["valor"]
            data_atual = ultimo["data_referencia"]

            for tipo_nivel in ("suporte", "resistencia"):
                if tipo_nivel not in nivel:
                    continue
                level_value = nivel[tipo_nivel]
                # Detectar quebra
                if tipo_nivel == "suporte" and valor_atual < level_value:
                    alertas.append({
                        "commodity": commodity,
                        "tipo": "quebra_suporte",
                        "data": data_atual,
                        "valor_atual": valor_atual,
                        "nivel": level_value,
                        "delta": valor_atual - level_value,
                        "msg": f"{commodity} fechou em {valor_atual} — abaixo do suporte {level_value}",
                    })
                elif tipo_nivel == "resistencia" and valor_atual > level_value:
                    alertas.append({
                        "commodity": commodity,
                        "tipo": "quebra_resistencia",
                        "data": data_atual,
                        "valor_atual": valor_atual,
                        "nivel": level_value,
                        "delta": valor_atual - level_value,
                        "msg": f"{commodity} fechou em {valor_atual} — acima da resistencia {level_value}",
                    })

            # Variacao diaria
            if len(rows) >= 2:
                prev = rows[1]["valor"]
                if prev:
                    pct = ((valor_atual - prev) / prev) * 100
                    threshold = nivel.get("variacao_dia_pct_alert", 3.0)
                    if abs(pct) > threshold:
                        alertas.append({
                            "commodity": commodity,
                            "tipo": "movimento_forte",
                            "data": data_atual,
                            "valor_atual": valor_atual,
                            "valor_anterior": prev,
                            "delta_pct": round(pct, 2),
                            "msg": f"{commodity} variou {pct:+.2f}% no dia (de {prev} para {valor_atual})",
                        })

    return alertas


def save_alerts(alertas: list[dict]) -> Path:
    out = config.DATA_DIR / "alerts_technical.json"
    out.write_text(
        json.dumps(
            {"gerado_em": datetime.now().isoformat(), "alertas": alertas},
            ensure_ascii=False, indent=2,
        ),
        encoding="utf-8",
    )

    # Espelha em shared se houver alertas
    if alertas and config.SHARED_TO_ALERTS.exists():
        today = date.today().isoformat()
        out_shared = config.SHARED_TO_ALERTS / f"{today}_alerts_tecnicos.md"
        lines = [f"# Alertas tecnicos — {today}", ""]
        for a in alertas:
            lines.append(f"- **{a['tipo']}** | {a['commodity']} | {a['msg']}")
        out_shared.write_text("\n".join(lines), encoding="utf-8")

    return out


def format_alerts(alertas: list[dict]) -> str:
    if not alertas:
        return "Sem alertas tecnicos hoje."
    lines = [f"{len(alertas)} alerta(s) tecnico(s):"]
    for a in alertas:
        lines.append(f"  [{a['tipo']:20s}] {a['commodity']:25s} → {a['msg']}")
    return "\n".join(lines)
