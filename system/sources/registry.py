"""Registry central de todos os coletores conhecidos."""
from . import (
    cme_cbot,
    bcb,
    cftc_cot,
    cepea,
    cepea_email,
    cepea_rss,
    cepea_paranagua,
    nag_fisico,
    noticias_rss,
    nopa,
    usda_wasde,
    usda_crop_progress,
    conab,
    abiove,
    anec,
    bcba,
    noaa_cpc,
    inmet,
    mpob,
)

COLLECTORS = [
    # === PRECOS / FUTUROS / CAMBIO ===
    cme_cbot.CMECollector,
    bcb.BCBCollector,
    # === POSICIONAMENTO ===
    cftc_cot.CFTCCotCollector,
    # === PRECO FISICO BR ===
    cepea_rss.CepeaRssCollector,    # ✅ ATIVO — RSS via ScraperAPI
    cepea_paranagua.CepeaParanaguaCollector,  # ✅ ATIVO — preço suporte CEPEA Paranaguá via NAG
    nag_fisico.NagFisicoCollector,  # ✅ ATIVO (2026-06-11) — farelo físico por praça + prêmios farelo/óleo Paranaguá via NAG
    noticias_rss.NoticiasRssCollector,  # ✅ ATIVO — G1 Agro + Canal Rural + FarmProgress
    cepea.CepeaCollector,           # disabled — Cloudflare bloqueia pagina indicador
    cepea_email.CepeaEmailCollector, # disabled — alternativa via IMAP nao mais necessaria
    # === ESMAGAMENTO / SUPPLY-DEMAND ===
    nopa.NopaCollector,
    usda_wasde.UsdaWasdeCollector,
    usda_crop_progress.UsdaCropProgressCollector,
    conab.ConabCollector,
    abiove.AbioveCollector,
    anec.AnecCollector,
    bcba.BcbaCollector,
    # === CLIMA / MACRO ===
    noaa_cpc.NoaaCpcCollector,
    inmet.InmetCollector,
    # === COMPETIDOR (OLEO PALMA) ===
    mpob.MpobCollector,
]


def list_all():
    return [
        {
            "source": c.source_name,
            "cadence": c.cadence,
            "description": c.description,
            "enabled": c.enabled,
        }
        for c in COLLECTORS
    ]


def run_all() -> list[dict]:
    results = []
    for cls in COLLECTORS:
        if not cls.enabled:
            results.append({"source": cls.source_name, "status": "disabled"})
            continue
        results.append(cls().run())
    return results


def run_one(source_name: str) -> dict:
    for cls in COLLECTORS:
        if cls.source_name == source_name:
            return cls().run()
    return {"source": source_name, "status": "not_found"}
