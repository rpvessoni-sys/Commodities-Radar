# SUPER HANDOFF — Commodities Radar (atualizado 2026-06-17)

> Substitui versões anteriores. Histórico antigo fica no git.
> **Produto:** https://rpvessoni-sys.github.io/Commodities-Radar/#dashboard (atualiza sozinho na nuvem)
> **Repo:** github.com/rpvessoni-sys/Commodities-Radar (PÚBLICO)
> **Perfil do dono:** TRADER de soja, farelo e óleo degomado — compra E vende (long e short). NÃO é comprador de farelo. Toda leitura é neutra (viés/spread/mean-reversion nos dois lados).

---

## ▶️ PRÓXIMA CONVERSA — COMECE AQUI

O dono vai **revisar item a item o que aparece no site** (validar visual/densidade/ordem da camada nova). Acompanhe-o nessa revisão. Depois, o roadmap aberto está no FOCO 3 abaixo.

**Sessão de 17/06 foi enorme** — entregue e no ar (commits `1c3a33e` → `2c95794` + prompts):
- **Lente comprador → TRADER** (dashboard inteiro): KPIs por direção de preço; Ratio Far/Soj virou **sinal de spread** (comprimido/neutro/esticado, mean-reversion); tributário/alertas/resumo/físico/matriz/drivers/insight neutralizados; prompts da camada de leitura reescritos.
- **BUG do preço congelado CONSERTADO** (era a maior dor): `save_to_db` usava `INSERT OR IGNORE` + chave única do dia → o 1º preço da madrugada travava o dia inteiro. Virou **upsert (last-write-wins)** → agora o preço acompanha o mercado a cada coleta. Validado vs barchart ao vivo.
- **Onda 0** (consertos): `openpyxl`+`xlrd` no requirements (ABIOVE/WASDE coletavam NADA na nuvem); Telegram texto puro + log de falha; `queue_emit` dispara alerta nos DOIS extremos do spread; **healthcheck** (avisa no Telegram se o daily não roda >26h); 2 casas decimais nos alertas; cron `*/30`→`*/15`.
- **Onda 1** (camada decisória, no topo do Dashboard): **🧭 Mesa do dia** (confiança alta/média/baixa/suspensa + semáforo por produto com score de convicção −3…+3 + linha de invalidação); **O que mudou desde ontem** (D-1 dos indicadores); **Sinais contraditórios** (detector de tensões de mesa); **fail-closed** do forecast ("só range" se acerto direcional <55%).
- **Onda 2** (aba Análise): **Índice de Sobra de Farelo** + **Índice de Suporte do Óleo** (0-100 por contagem de condições auditáveis, sem pesos mágicos). Reusam o ABIOVE que estava órfão. Hoje: Sobra 100 (5/5), Suporte 80 (4/5).
- **Input físico aceita `venda`** no `inputs_manuais.toml` (antes travado em compra).

---

## ⚠️ VERIFICAÇÃO PENDENTE (o dono precisa fazer / confirmar)

1. **ABIOVE/WASDE coletam na nuvem agora?** O fix do `openpyxl`/`xlrd` subiu — confirmar num run `daily` real (Actions → log do step "Rodar pipeline (daily)" → `abiove`/`usda_wasde` com `saved>0`). Era a descoberta nº1: estavam mortos por falta de dependência.
2. **Telegram / disparo:** o resumo só sai se o `daily` rodar, e o disparo real depende do **pinger cron-job.org** (cron nativo do GitHub é best-effort). Conferir no painel cron-job.org se os 2 jobs (`radar-intraday`, `radar-daily`) estão habilitados e o **PAT** (expira **31/dez/2026**) está válido. O healthcheck agora avisa se o daily morrer.
3. **`gh` CLI:** o dono instalou GitHub Desktop, não o CLI. Se instalar o `gh` CLI e reabrir o terminal, o Claude consegue disparar runs e ler logs direto.

---

## 🎯 FOCO 3 — Roadmap aberto (em ordem de valor)

### A) Físico: DISPLAY de venda (curto)
O input já aceita `venda`, mas o card físico (`_get_fisico_br`/`_render_fisico_produto` via `latest_per_praca(tipo_posicao="compra")`) só mostra COMPRA. Estender pra mostrar os dois lados (compra e venda) por praça/produto.

### B) Onda 3 — Fontes novas de alto valor (precisam de coletor novo)
Backlog verificado em `FONTES_CANDIDATAS_2026-06-16.md`. Prioridade:
- **ANP biodiesel BR** (gap nº1 do óleo degomado — CSV público; share óleo soja vs sebo; destrava §9.6 e o painel biodiesel BR).
- **USDA FAS Export Sales** (sinal China; API JSON, chave grátis → secret).
- **ComexStat/MDIC por NCM** (export farelo/óleo por porto; POST JSON via ScraperAPI).
- **Argentina FOB** (datos.gob.ar, CSV diário → spread BR×AR direto).
- **SIFRECA** frete (decompõe o basis no PR).
- **NASS_API_KEY** (Crop Progress já existe, só falta a secret).
- **Parser ANEC** (hoje é stub, só guarda links — falta baixar XLSX e extrair embarques → Pressão Exportadora).
- **Milho ZC=F** (1 ticker no `cme_cbot.py`) se quiser meal/corn ratio (§8.3/§9.5).

### C) Fase 2 — Claude lendo SEMPRE, agendado, sem consumir conversa (só tokens)
Tudo desenhado, falta ativar. Mecanismo = **Claude Code Routine** (agente agendado headless), roda 1×/dia num clone fresco, lê um briefing, escreve `insights/*.md` com viés, abre PR (o dono aprova do celular). Artefatos JÁ existem: `system/prompts/routine_julgamento.txt` (já reescrito p/ trader) + `.github/workflows/guard-leitura.yml` (CI que barra PR fora de `insights/`). Passos de ativação:
1. **Bloqueio técnico nº1:** o robô precisa **publicar o briefing no git** — adicionar ao `radar.yml` (modo daily) um passo que escreve `data/last_dump.md` (+ a fila `queue_emit.render_markdown`) em `briefing/latest.md` e commita (precisa `permissions: contents: write`). Sem isso a Routine acorda sem entrada. Snippet base em `FLUXO_JULGAMENTO.md` §Fase 2.
2. Instalar o **Claude GitHub App** no repo + criar a **Routine** (prompt = `routine_julgamento.txt`, schedule ~20-21h BRT, 1h após o daily).
3. Gate de custo: só chamar se a fila tiver item (hoje 0 é comum). PR revisável (não auto-merge até confiar).

### D) StoneX — padrão SEGURO (sem código novo)
Extração PROIBIDA (PDFs têm marca d'água com o e-mail corporativo → rastro de vazamento). Padrão certo: **o dono lê e escreve um resumo curto COM AS PRÓPRIAS PALAVRAS** (tese destilada: direção, fatores, níveis) numa nota em `shared/from_consultor/` — sem citar StoneX, sem verbatim, sem o PDF. O `synth_daily` já varre essa pasta e injeta como "leitura de consultoria"; o Claude lê o **resumo do dono** (tokens sobre o texto dele, nunca o documento). Níveis de curva entram no slot manual `[[curva]]` do `inputs_manuais.toml`. **Nunca** baixar/parsear/colar o relatório.

### E) Itens que decidimos NÃO fazer (governança de time, overkill p/ trader solo)
Cadastro YAML formal de fonte, aba metodologia versionada, score de convicção de 11 componentes com pesos, plano de tranches/cobertura (lente de comprador), carimbo de origem em cada número, regime detection do forecast, parser pesado de Argentina/weather score completo.

---

## 🗺️ ESTADO DO SISTEMA (arquitetura)

- **Coleta:** GitHub Actions (`.github/workflows/radar.yml`), 2 modos via `system/cloud_run.py`:
  - `intraday` (a cada **15 min**, 24/7): só CBOT (Yahoo) + câmbio (BCB) → indicadores → HTML → alerta-na-hora → **healthcheck**. Auto-fallback ScraperAPI se o Yahoo bloquear.
  - `daily` (~19h BRT): varredura completa (físico CEPEA/NAG + WASDE/NOPA/COT/ABIOVE/MPOB/clima) + forecast + dump + resumo Telegram + **heartbeat**.
- **Disparo:** pinger **cron-job.org** (o cron nativo do GitHub é não-confiável). PAT expira 31/dez/2026.
- **Publicação:** HTML → GitHub Pages. Estado (radar.db) vive no **cache do Actions** + backup diário (NÃO no git).
- **Camada manual:** `inputs_manuais.toml` (raiz, versionado) — preço físico (compra E venda), curva do consultor (`[[curva]]`), params (RIN). Edita + push → nuvem aplica via `inputs_manuais.sync()`.
- **Camada de julgamento (FATO vs LEITURA):** robô = FATO; Claude = LEITURA (`insights/*.md` com `vies:`). Fase 1 ativa (sessão paga, frase-gatilho "lê a fila de julgamento e trata"). Fase 2 pronta, não ativada (FOCO 3.C).

### Testes & comandos
- `cd system; $env:PYTHONIOENCODING="utf-8"` sempre.
- `.venv\Scripts\python.exe -m unittest discover -s tests` → **60 testes**.
- `main.py synth` (gera HTML do DB, sem coletar) · `main.py indicators` (recalcula + índices) · `main.py run` (pipeline completo local) · `main.py queue` (fila) · `cloud_run.py --mode intraday|daily`.

---

## ⚠️ CAVEATS / GOTCHAS
1. **Preço "repetindo" agora é raro** — o upsert conserta o congelamento. Se repetir, é mercado fechado (sem trade novo) ou o run não rodou (ver healthcheck).
2. **Cron do GitHub é preguiçoso** — confiar no pinger cron-job.org.
3. **Dados não estão no git** (cache do Actions) — pré-requisito se algo exigir dado versionado (ex: backtest longo, ou o briefing da Fase 2).
4. **PROIBIDO** recriar extração StoneX (marca d'água). Fontes 100% públicas. Scraping de CME/barchart também é ToS — só spot-check manual, nunca coletor.
5. **PAT expira 31/dez/2026** (renovar antes; cron-job.org notifica falha por e-mail).
6. **Repo é PÚBLICO** (dado de mercado + insights visíveis; segredos só no GitHub Secrets).
7. **git commit no PowerShell:** mensagem longa quebra com here-string/aspas — usar vários `-m` de uma linha (como nesta sessão).
8. **`print` em probe local:** stdout Windows é cp1252 — caracteres como `≥` quebram; usar `$env:PYTHONIOENCODING="utf-8"`. (Não afeta o HTML, que é UTF-8.)
9. Memória do projeto: `project_commodities_radar.md` (perfil trader + histórico de decisões).

## 📂 Docs no repo
`FLUXO_JULGAMENTO.md` (camada de leitura + Fase 2) · `FONTES_CANDIDATAS_2026-06-16.md` (backlog de fontes) ·
`REVISAO_TRADER_2026-06-11.md` (⚠ a Onda P0 dela é lente de COMPRADOR — reenquadrar antes de usar) ·
`ARCHITECTURE_HTML.md` (estrutura das abas) · `DEPLOY_NUVEM.md` (deploy).
