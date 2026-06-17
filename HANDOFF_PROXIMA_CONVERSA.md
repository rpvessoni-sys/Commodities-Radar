# SUPER HANDOFF — Commodities Radar (atualizado 2026-06-17)

> Substitui versões anteriores. Histórico antigo fica no git.
> **Produto:** https://rpvessoni-sys.github.io/Commodities-Radar/#dashboard (atualiza sozinho na nuvem)
> **Repo:** github.com/rpvessoni-sys/Commodities-Radar (PÚBLICO)

---

## ▶️ COMECE AQUI

### 0) MUDANÇA DE PERFIL — o usuário é TRADER, não comprador de farelo
Foi corrigido em 2026-06-17. O usuário **opera soja, óleo E farelo — compra E vende (long e short)**.
TODA a "lente do comprador de farelo" embutida no sistema está **errada de enquadramento** e precisa
virar **leitura neutra de mercado/trader**. Isso é o coração do refino do dashboard (FOCO 1 abaixo).

### Os 2 focos da próxima conversa
1. **Refinar os DADOS do dashboard** (a página #dashboard) — corrigir a lente (trader, não comprador) +
   melhorar profundidade/qualidade do que aparece.
2. **Refinar o que o TELEGRAM dispara** — o resumo diário e o alerta-na-hora.

---

## 🎯 FOCO 1 — Refino dos dados do DASHBOARD

A página tem 6 abas (Dashboard · Mercado Físico · Análise Quantitativa · Forecasts & Eventos ·
Notícias & Tese · Insights). O que precisa de trabalho:

### A) Virar a lente de COMPRADOR → TRADER (prioridade máxima)
Pontos onde está cravada a ótica de comprador (todos em `system/notify_html.py`, e geram no HTML):
- **KPIs**: o farelo usa `_kpi_change_line(..., lente_comprador=True)` → queda pinta VERDE ("bom pra comprar").
  Trader: cor = direção de preço (ou neutra), não "bom/ruim". Rever os 3.
- **Card Ratio Far/Soj**: hoje é "🟢 zona de compra <80 · 🟡 transição · 🔴 caro" (ótica de quem compra farelo).
  Trader: é um **sinal de SPREAD** (farelo caro/barato *vs* soja) → ler como trade de spread/crush e
  mean-reversion, nos dois sentidos, não "hora de comprar". Reescrever zonas/legenda/texto.
- **Mercado Físico**: badges "compra abaixo do indicador = verde", "export não compete = verde",
  "vs sua compra" → tudo comprador. Neutralizar (é referência de preço, não vantagem de compra).
- **Monitor Tributário** (aba Forecasts): frase "Você é comprador de farelo → baixista é favorável" → neutralizar
  (alta/baixa = efeito no preço; trader lê os dois lados). Em `_render_tributario`.
- **Resumo executivo** (`_gerar_resumo_executivo`): seção "Pro comprador" → "Leitura de mercado".
- **Drivers por commodity** (`_gerar_drivers`): já são bull/bear neutros (alta/baixa) — OK, só revisar textos
  que assumem comprador.
- **Insight de 11/jun** (`insights/2026-06-11_ratio-81...md`): todo escrito como comprador ("janela de tranches").
  Reescrever/arquivar na ótica de trader, e rever o `vies:`.
- **Óleo R$/ton no físico**: a ressalva "FOB export ≠ degomado interno" era pro comprador; pro TRADER que opera
  óleo CBOT, a paridade CBOT É o que importa — reavaliar se a ressalva ainda cabe.

### B) Qualidade/profundidade dos dados (depois da lente)
- **Verificar variação intraday**: confirmar que o preço VARIA entre capturas durante o pregão ativo
  (CBOT grãos: 08:30–13:20 CT = 10:30–15:20 BRT; pausa 07:45–08:30 CT). Ver caveat de "dado repetindo" abaixo.
- **Granularidade**: o coletor usa Yahoo `interval=1d` (barra diária; a barra de hoje atualiza com o último preço,
  delay ~15 min). Pra trader, avaliar se vale capturar barras intraday (15m/30m) — limitado pelo delay do Yahoo grátis.
- **Backlog de fontes** já pesquisado e verificado em `FONTES_CANDIDATAS_2026-06-16.md` (Argentina FOB,
  USDA Export Sales/China, ANP biodiesel, spreads, COT detalhado, etc.). Decidir o que entra.
- **Spreads como trade** (lente trader): crush spread, oil share, Far/Soj, calendário (já há 6 vencimentos no DB)
  — exibir como sinais operáveis, não só descritivos.

### C) ⚠️ Pré-requisito pro refino: os dados HOJE não sobem pro git
O `radar.db` vive no **cache do Actions** + backup artifact diário; o **git NÃO recebe os dados** (só código/insights;
o HTML vai pro Pages como artifact, não commitado). Se o refino exigir dados versionados/consultáveis no GitHub,
o 1º passo é adicionar **commit-back do DB/exports (CSV)** a cada run (muda o radar.yml pra `contents: write`).
**Decidir isso no começo do refino.**

---

## 📲 FOCO 2 — Refino do que o TELEGRAM dispara

Hoje saem **duas coisas** (canal já configurado: bot + chat_id `6111792165`, secrets no GitHub):

1. **Resumo diário** (`system/daily_summary.py`, roda no modo `daily` ~22h BRT): snapshot CBOT (com variação +
   **paridade R$**: soja R$/sc, farelo R$/ton, óleo R$/ton), USD/BRL, ratio Far/Soj+zona, crush+oil share, nº de
   leituras pendentes. Usa parse_mode Markdown.
2. **Alerta na hora** (`system/alerts_push.py`, roda no `intraday` a cada 15 min): manda 🔴 quando surge sinal NOVO
   de severidade ALTA na fila (`queue_emit`), dedup por id (avisa 1×). **Texto puro** (Markdown quebrava com `_` de
   nomes de métrica — já corrigido).

Refinos a discutir (lente trader):
- **O que merece alerta**: hoje só severidade 'alta' da fila (ratio cruzou zona, nível de tese rompido, etc.).
  Trader pode querer: movimento forte intraday por perna, cruzamento de spread (crush/Far/Soj), rompimento de nível
  nos dois sentidos. Ajustar `queue_emit` (regras) + `alerts_push` (severidades).
- **Formato/conteúdo**: o resumo é genérico — refinar pra trader (direção, spreads, níveis-chave, o que mudou).
  A frase do resumo ainda tem resquício de comprador? Revisar.
- **Cadência de alerta**: o intraday é 15 min → alerta chega em até ~15 min. Suficiente? (limitado pelo delay do Yahoo).
- **Markdown vs texto puro**: o resumo usa Markdown (funciona, mas frágil se entrar `_`/`*` em conteúdo dinâmico).
  Avaliar padronizar tudo em texto puro como o alerta.

---

## 🗺️ ESTADO ATUAL DO SISTEMA (pra retomar)

### Arquitetura (tudo na nuvem, sem o PC)
- **Coleta:** GitHub Actions (`.github/workflows/radar.yml`), 2 modos via `system/cloud_run.py`:
  - `intraday` (a cada 15 min): SÓ o que flutua sempre — **CBOT (Yahoo) + câmbio (BCB)** → indicadores → HTML →
    alerta-na-hora. Tem **auto-fallback**: se o Yahoo bloquear o IP, tenta via ScraperAPI sozinho.
  - `daily` (~22h BRT): **varredura completa** (run_all: físico CEPEA/NAG + fundamentos WASDE/NOPA/COT/ABIOVE/MPOB/
    clima) + forecast + dump + resumo Telegram.
- **Disparo (CRÍTICO):** o cron nativo do GitHub é **não-confiável** (atrasa/pula). Quem dispara de verdade é o
  **pinger cron-job.org**: 2 jobs — `radar-intraday` (15 min, `mode:intraday`) e `radar-daily` (22h BRT, `mode:daily`),
  via POST no `workflow_dispatch`. **PAT (token) expira 2026-12-31** → renovar antes.
- **Publicação:** HTML → GitHub Pages (#dashboard). Estado do DB → cache do Actions + artifact diário (NÃO no git).

### Camada de julgamento (FATO vs LEITURA) — Fase 1 ativa
- Robô = FATO (determinístico). Claude = LEITURA (opinião, em sessão paga, sem API).
- `system/queue_emit.py` emite a **fila de julgamento** (o que pede interpretação); `main.py queue` mostra.
- Frase-gatilho numa sessão Claude no repo: **"lê a fila de julgamento e trata"** (`system/prompts/treat_queue.txt`)
  → escreve só `insights/*.md` (com `vies: [bull/bear-produto]`, que alimenta os Drivers) → push → dash atualiza.
- **Fase 2 (Claude autônomo na nuvem) — pronta, NÃO ativada:** `routine_julgamento.txt` + `guard-leitura.yml`
  (CI que barra PR `claude/` fora de insights/). Ativar = instalar Claude GitHub App + criar Routine. Ver `FLUXO_JULGAMENTO.md`.

### Testes & comandos
- `cd system; $env:PYTHONIOENCODING="utf-8"` sempre.
- `.venv\Scripts\python.exe -m unittest discover -s tests` → **60 testes**.
- `main.py run` (pipeline completo local) · `main.py queue` (fila) · `main.py status` (saúde) ·
  `main.py inputs sync|show` (camada manual via `inputs_manuais.toml`) · `cloud_run.py --mode intraday|daily`.

### Inputs MANUAIS (não automatizar — é dado do trader)
`inputs_manuais.toml` (raiz, versionado): preço físico + curva do consultor + params (RIN D4). Edita + push → nuvem aplica.

---

## ⚠️ CAVEATS / GOTCHAS
1. **"Dado repetindo" ≠ bug** quando o CBOT está fechado (pausa 07:45–08:30 CT / fora do pregão) — sem trade, sem preço novo.
   Yahoo tem delay ~15 min; PTAX muda poucas vezes/dia. Validar que VARIA durante o pregão ativo.
2. **Cron do GitHub é preguiçoso** — confiar no pinger cron-job.org, não no `schedule` nativo.
3. **Dados não estão no git** (cache do Actions) — pré-requisito do FOCO 1.C.
4. **PROIBIDO** recriar extração StoneX. Fontes 100% públicas.
5. **PAT expira 31/dez/2026** (pinger para de funcionar se não renovar; cron-job.org pode notificar falha por e-mail).
6. **Repo é PÚBLICO** (dado de mercado + insights ficam visíveis; sem segredo no repo — secrets no GitHub Secrets).
7. **git commit com mensagem longa no PowerShell** quebra com here-string/aspas — usar `-m` de uma linha ou `-F arquivo`.
8. Memória do projeto: `project_commodities_radar.md` (tem a correção de perfil e todo o histórico de decisões).

## 📂 Docs no repo
`FLUXO_JULGAMENTO.md` (camada de leitura + Fase 2) · `FONTES_CANDIDATAS_2026-06-16.md` (backlog de fontes) ·
`REVISAO_TRADER_2026-06-11.md` (review estratégico) · `ARCHITECTURE_HTML.md` (estrutura das 6 abas) ·
`DEPLOY_NUVEM.md` (deploy GitHub Actions/Pages).
