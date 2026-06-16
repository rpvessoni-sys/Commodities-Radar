"""Coletor Inmet — Instituto Nacional de Meteorologia (Brasil).

ATENCAO: o endpoint historico /estacao/{ini}/{fim}/{cod} esta retornando 204
em 2026-05-21. Esta implementacao usa o endpoint /previsao/{ibge_code} que
funciona e cobre os proximos ~4 dias para municipios chave do agro.

Para historico, ver TODO no final.
"""
from datetime import date, datetime
from .base import BaseCollector


# Codigos IBGE dos principais municipios produtores de soja BR
MUNICIPIOS = {
    "5107909": ("sorriso_mt", "Sorriso/MT"),
    "5105259": ("lucas_rio_verde_mt", "Lucas do Rio Verde/MT"),
    "5103403": ("cuiaba_mt", "Cuiaba/MT"),
    "5107925": ("sinop_mt", "Sinop/MT"),
    "5208707": ("rio_verde_go", "Rio Verde/GO"),
    "4104808": ("cascavel_pr", "Cascavel/PR"),
    "4115200": ("maringa_pr", "Maringa/PR"),
    "4314100": ("passo_fundo_rs", "Passo Fundo/RS"),
}


class InmetCollector(BaseCollector):
    source_name = "inmet"
    cadence = "daily"
    description = "Inmet — previsao 4 dias para municipios chave do agro (MT, PR, RS, GO)"
    enabled = True

    def fetch(self):
        try:
            import requests
        except ImportError:
            raise RuntimeError("requests nao instalado")

        results = []
        headers = {"User-Agent": "Mozilla/5.0 commodities-radar/1.0"}

        for cod_ibge, (commodity, label) in MUNICIPIOS.items():
            url = f"https://apiprevmet3.inmet.gov.br/previsao/{cod_ibge}"
            try:
                r = requests.get(url, headers=headers, timeout=20)
                r.raise_for_status()
                data = r.json()
            except Exception as e:
                results.append({
                    "data_referencia": date.today().isoformat(),
                    "tipo": "erro",
                    "commodity": commodity,
                    "metrica": "fetch_error",
                    "valor": None,
                    "contexto": f"{type(e).__name__}: {e} | {label}",
                })
                continue

            # Schema: {cod_ibge: {data_br: {manha/tarde/noite: {...}}}}
            previsoes = data.get(cod_ibge, {})
            for data_br, periodos in previsoes.items():
                try:
                    dia, mes, ano = data_br.split("/")
                    data_iso = f"{ano}-{mes}-{dia}"
                except (ValueError, AttributeError):
                    continue

                for periodo, info in periodos.items():
                    if not isinstance(info, dict):
                        continue
                    tmax = info.get("temp_max")
                    tmin = info.get("temp_min")
                    resumo = info.get("resumo", "")

                    if tmax is not None:
                        results.append({
                            "data_referencia": data_iso,
                            "tipo": "clima",
                            "commodity": commodity,
                            "metrica": f"temp_max_{periodo}",
                            "valor": float(tmax),
                            "unidade": "C",
                            "contexto": f"{label} — {resumo}",
                        })
                    if tmin is not None:
                        results.append({
                            "data_referencia": data_iso,
                            "tipo": "clima",
                            "commodity": commodity,
                            "metrica": f"temp_min_{periodo}",
                            "valor": float(tmin),
                            "unidade": "C",
                            "contexto": f"{label} — {resumo}",
                        })

        return results


# TODO endpoint historico:
# - apitempo.inmet.gov.br/estacao/{ini}/{fim}/{cod} retornou 204 em testes 2026-05-21
# - Investigar: pode ter mudado URL, ou precisar de auth, ou ter rate limit
# - Alternativas: BDMEP (portal.inmet.gov.br/dadoshistoricos) tem CSV downloads
#   mas requer download manual via web
# - Climatempo (pago) tem API estavel
