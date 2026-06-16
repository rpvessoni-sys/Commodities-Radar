# Commodities Radar — Sistema

Hub Python de análise de **soja, farelo e óleo de soja** (físico BR + CBOT).
100% fontes públicas + inputs manuais. Produto final = HTML diário de 6 abas
(`reports/latest.html`, atalho Desktop "Radar Daily").

> 🛑 **Extração de relatórios StoneX é PROIBIDA desde 2026-06-05.** Não recriar
> downloader, parser de PDF, ingest de email ou bookmarklet. O que continua
> permitido: call semanal com o consultor + anotação manual (`curva set`,
> `param set`) e insights de leitura própria.

## Setup (primeira vez)

```powershell
cd commodities-radar/system
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env       # preencher SCRAPER_API_KEY e NASS_API_KEY
python main.py init
.\setup_scheduler.ps1        # registra as 7 tasks no Task Scheduler
```

**Sem API key da Anthropic.** Síntese narrativa e insights automáticos são
feitos via Claude Code (sessão), não via API.

## Comandos do dia a dia

```powershell
$env:PYTHONIOENCODING="utf-8"            # SEMPRE (caveat #1)

python main.py status                    # saúde: fontes, inputs, forecasts, marcos fiscais
python main.py run                       # pipeline completo: public → indicators → alerts → forecast → synth → dump
python main.py public --source cme_cbot  # só 1 coletor (--list pra ver todos)
python main.py synth                     # regenera HTML + snapshot pro consultor
python main.py fisico add                # input manual de preços físicos (atalho "Input Fisico")
python main.py tributario list           # monitor fiscal/regulatório (sync após editar o TOML)
python main.py insight new "Titulo"      # novo insight de estudo
python main.py curva set stonex --produto oleo --venc N26 --valor 75.5 --detalhe "call Fabio"
python main.py premios list              # histórico de prêmios (série encerrada, só leitura)
```

## Testes

```powershell
python -m unittest discover -s tests     # 32 testes, ~0.1s, sem rede
```

Cobrem: parser NAG (fixture offline), frontmatter/`vies` dos insights, banda
estatística do forecast, validação dos catálogos TOML (`tributario_watch`,
`alerts_config` — typo de enum vira erro de teste).

## Estrutura

```
system/
├── main.py                orquestrador CLI (run/status/public/synth/fisico/tributario/insight/curva)
├── config.py              .env + paths
├── db.py / schema.sql     SQLite (data/radar.db)
├── sources/               coletores públicos
│   ├── registry.py          registro central (16 ativos)
│   ├── cme_cbot.py          CBOT via Yahoo (front + 6 vencimentos)
│   ├── nag_fisico.py        farelo 3 praças + prêmios PGUA + soja PR interior (Notícias Agrícolas)
│   ├── cepea_paranagua.py   indicador CEPEA soja porto (via NAG)
│   └── ...                  bcb, cepea_rss, usda_wasde, nopa, abiove, anec, mpob, bcba, cftc_cot, clima, notícias
├── indicators.py          crush margin, oil share, ratio Far/Soj, paridades BR
├── alerts_technical.py    níveis de alerts_config.toml (recalibrar quando o regime muda)
├── forecast.py            bandas MA20+vol 7d/30d + resolução (hit banda/direção)
├── tributario.py          monitor fiscal (tributario_watch.toml → DB → HTML)
├── insights.py            insights .md com frontmatter (status, tags, vies)
├── curvas.py              framework 4 curvas (CBOT real · StoneX manual · Claude · média)
├── notify_html.py         HTML 6 abas — PRODUTO FINAL (ver ../ARCHITECTURE_HTML.md)
├── synth_daily.py         report estruturado + dump pro Claude Code
├── prompts/
│   ├── synthesize_daily.txt    síntese narrativa diária
│   └── generate_insights.txt   insights automáticos pós-varredura (tag auto-claude)
├── tests/                 unittest (ver acima)
└── *.ps1                  run_radar, setup_scheduler, backup_db, input_fisico, new_insight
```

## Automação (Task Scheduler)

7 tasks `CommoditiesRadar_*` (registrar com `setup_scheduler.ps1`, listar com `-List`):
Morning 07h `run` · Evening 19h CBOT · Indicators 20h · Alerts 20h15 ·
Night 22h `run` · Friday 18h COT · Backup sáb 23h.

## Fluxo com Claude Code

1. `python main.py run` (ou aguardar o scheduler)
2. Abrir Claude Code no raiz do projeto:
   - Síntese: _"le data/last_dump.md e gera sintese diaria seguindo system/prompts/synthesize_daily.txt"_
   - Pós-varredura: _"gera insights da varredura"_ → segue `prompts/generate_insights.txt`
     (máx 1-3, tag `auto-claude`, frontmatter `vies:` alimenta os Drivers do HTML)

## Troubleshooting

- **Acento quebrado/UnicodeEncodeError** → `$env:PYTHONIOENCODING="utf-8"` (o run_radar.ps1 já seta)
- **ModuleNotFoundError** → ative o venv: `.venv\Scripts\activate`
- **SQLite lock** → OneDrive sincronizando; se recorrente, mover projeto pra `C:\Dev\`
- **Coletor NAG quebrou** → rodar testes (`tests/test_nag_fisico.py`) pra confirmar se é layout novo; ver `coletas_log` e o card "Saúde das fontes" no HTML
- **Deltas do físico sumiram** → seus inputs têm >3 dias; rode `fisico add`
