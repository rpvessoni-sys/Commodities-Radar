# SUPER HANDOFF — Commodities Radar (atualizado 2026-06-22)

> Substitui versões anteriores. Histórico antigo fica no git.
> **Produto:** https://rpvessoni-sys.github.io/Commodities-Radar/#dashboard (atualiza sozinho na nuvem)
> **Repo:** github.com/rpvessoni-sys/Commodities-Radar (PÚBLICO)
> **Perfil do dono:** TRADER de soja, farelo e óleo degomado — opera os DOIS lados (long e short). Leitura SEMPRE neutra de preço (viés/spread/mean-reversion). NUNCA "comprador de farelo".

---

## 🔧 SESSÃO 2026-06-22 — Auditoria dos sinais + 2 fixes grandes (no ar)

O dono achou que "os sinais estavam errados". Auditoria adversarial (workflow, 34 achados confirmados) **confirmou** e corrigi:

**A) Farelo congelado + cascata (commit `7896f52`).** O farelo CBOT (ZM=F) ficava **preso no fechamento de 18/jun** enquanto soja/óleo andavam (intraday sobrescrevia o close bom do daily com print travado do Yahoo). Como crush, ratio Far/Soj, oil share e a Mesa derivam do farelo, **todos davam leitura falsa** ("farelo barato", "crush quebrou suporte", "Farelo −3") — sem aviso, porque a Saúde das fontes media frescor por FONTE, não por commodity. Fix = detector único **`indicators.cbot_freshness(conn)`** (perna defasada OU travada/delta-0) ligado em: KPI ("⚠ travado desde DD/mês" em vez de 0,00%), ratio (aviso em vez de "farelo barato"), crush ("leitura parcial"), Mesa (segura o score, rebaixa confiança), alertas técnicos (não dispara em perna travada), e **guard anti-carry no `cme_cbot.py`** (não grava fechamento repetido do dia em formação). NÃO mexe nas fórmulas (calibração intacta). Teste novo `tests/test_freshness.py`.

**B) Bucket de lógica (commit `09f92f1`).** Score da Mesa ganhou **cap de momentum** (óleo não fica +3 "alta forte" caindo −10%; segura em +1); alerta do **crush por delta absoluto** (`variacao_abs_alert=0.50`, fim do −18% ruidoso); insight do óleo **condicional ao preço** ("ROMPEU 72" quando abaixo); crush insight reconhece os 2 níveis ($2,00 vs $2,50); "O que mudou" usa **datas reais** (não ontem/hoje). Forecast direcional (15% acerto) **já falha-fechado certo** ("só range") — sem mudança; modelo fraco = tarefa separada.

**Validação:** 64 testes OK; `radar.yml` 60 runs sem falha (7896f52 confirmado verde ao vivo); Fase 2 produziu PR #4 (06-20) e #5 (06-21) **limpos** (1 commit, só insights/, guard verde) — o desastre de 06-19 não repetiu. PRs #4/#5 leem CBOT 06-18 (fim de semana, complexo consistente em 06-18 — NÃO contaminados pela cascata). Dono mergeou os 2.

**C) Radar mostra a leitura POR COMMODITY (`a51ce70`).** O card da aba 💡 Insights mostrava "(sem resumo executivo)" pras leituras auto-claude (elas têm `## Soja/## Farelo/## Óleo`, não `## Resumo executivo`). Agora `insights.py` extrai por commodity (direção do frontmatter `vies` + rótulo + a **Leitura operacional**/call) + Visão geral; `notify_html._render_insight_commodities` exibe 🟢/🔴 por commodity. Texto escapado (`<80%` não quebra). **Nota do dono: a leitura auto-claude é boa MAS verbosa/genérica e tem especificidades regulatórias não-verificáveis (STJ REsp, nº WASDE) — pendente reescrever o prompt pra nascer ENXUTA e afiada.**

**D) ENTREGA da leitura no Telegram (`6eaf448`).** A leitura ficava presa no PR — o dono nunca recebia. `system/notify_leitura.py` formata (título + visão geral + 🟢/🔴 por commodity com viés+call + link) e manda pro Telegram. `leitura.yml` ganhou passo que envia após abrir o PR (futuras chegam sozinhas). Workflow manual **`enviar-leitura.yml`** (Run workflow) = preview na hora de uma leitura existente.

**E) AGENDA de check-up (`83bbbee`).** `system/checkup.py` certifica cada fonte: rodou? (coletas_log vs cadência) e EXTRAIU dado real? (MAX data_referencia não-nula — pega ANEC/stub que "roda mas não traz número") + frescor CBOT por commodity. `checkup.yml`: restaura o `radar.db` do cache (read-only), roda diário ~23h30 BRT (silencioso se OK, alerta se problema, 2ª feira = relatório completo) + botão manual. Coleta certificada hoje (16 fontes rodaram 2026-06-23).

**F) AUTO-MERGE ligado + fix do check-up (2026-06-23).** O dono ligou o auto-merge: `leitura.yml` ganhou passo `gh pr merge --squash --delete-branch` que mergeia a leitura no main automaticamente — **só se tocar apenas `insights/`** (guard inline via merge-base; senão aborta e deixa pro dono). Link do Telegram passou a apontar pro `blob/main`. E o `checkup.yml` falhou no 1º run (exit 1: só instalava `requests`, mas `config` precisa de `python-dotenv` e o registry importa os coletores) → corrigido pra `pip install -r requirements.txt` (igual radar.yml) + cache pip. **Ciclo 100% automático agora:** coleta → leitura → Telegram → auto-merge no main → aparece no radar; check-up diário certifica.

**Aberto / próximos:** (1) **prompt enxuto da Fase 2** (o grande, melhora a qualidade na origem); (2) revisão visual do site (FOCO 3 D); (3) bucket de lógica "deeper" (modelo de forecast 15%).

---

## ▶️ PRÓXIMA CONVERSA — COMECE AQUI

A sessão de 17–19/jun foi enorme e fechou 5 frentes grandes. **O que ficou pendente pra retomar:**
1. **Revisão item a item do site** — o dono queria passar tela por tela validando o visual da camada nova (Mesa do dia, índices, etc.). Não chegamos a fazer.
2. **FOCO 3 — Roadmap** (detalhado embaixo): display de venda no físico · Onda 3 (fontes novas) · durabilidade do bot de input.
3. **Confirmar** que ABIOVE/WASDE coletam na nuvem (o fix do openpyxl/xlrd) — o briefing já mostra os dados, mas vale checar um run daily.

**A rotina diária do dono agora inclui:** aprovar o PR de leitura que o Claude autônomo abre (~30 seg no celular). Ver "Fase 2" abaixo.

---

## ✅ O QUE A SESSÃO ENTREGOU (tudo na nuvem, validado)

**1. Lente comprador → TRADER** (dashboard + Telegram + prompts da Fase 2): KPIs por direção de preço; Ratio Far/Soj virou **sinal de spread** (comprimido/neutro/esticado, mean-reversion nos dois lados); tributário/alertas/resumo/físico/matriz/drivers/insight neutralizados.

**2. BUG do preço congelado CONSERTADO:** `save_to_db` usava `INSERT OR IGNORE` → o 1º preço da madrugada travava o dia todo. Virou **upsert** (`ON CONFLICT DO UPDATE`) → o preço acompanha o mercado a cada coleta.

**3. Onda 0:** `openpyxl`+`xlrd` no requirements (ABIOVE/WASDE coletavam NADA na nuvem); Telegram texto puro + log de falha; **healthcheck** (avisa no Telegram se o daily não roda >26h); 2 casas decimais nos alertas; cron `*/30`→`*/15`; `queue_emit` dispara alerta nos DOIS extremos do spread.

**4. Onda 1 — camada decisória** (topo do Dashboard): **🧭 Mesa do dia** (confiança alta/média/baixa/suspensa + semáforo por produto com score de convicção −3…+3 + linha de invalidação); **O que mudou desde ontem** (D-1); **Sinais contraditórios**; **fail-closed** do forecast ("só range" se acerto direcional <55%).

**5. Onda 2 — índices sintéticos** (aba Análise): **Índice de Sobra de Farelo** + **Índice de Suporte do Óleo** (0-100 por contagem de condições auditáveis). Reusam o ABIOVE que estava órfão.

**6. Físico aceita VENDA** no `inputs_manuais.toml` (`tipo = "venda"`; antes travado em compra).

**7. Telegram:**
- **Resumo diário** robusto — desacoplado do run `daily` pesado (qualquer run após 22 UTC manda 1×/dia, deduplicado), pra não depender do pinger.
- **📈 Pulso CBOT** — a cada **30 min no pregão** (~10h30–16h20 BRT, dia útil): blocos verticais (mobile) por commodity com último/anterior/abertura/variação + dólar/Far-Soj/oil share/crush. `daily_summary.build_pulso_cbot`.
- **🤖 Bot de input físico** (`telegram_input.py`) — o run intraday lê suas mensagens via `getUpdates` e grava em `precos_fisicos`. Gramática: `[compra|venda] <soja|farelo|oleo> <porto|rancharia> <valor>`. Comandos `fisico` (mostra o atual) e `ajuda`. Persiste no DB (durável via cache + backup diário; **commit-back no .toml = hardening futuro**, FOCO 3).

**8. FASE 2 — Claude autônomo (LIGADA E FUNCIONANDO):** ver seção dedicada abaixo.

---

## 🤖 FASE 2 — LEITURA AUTÔNOMA DO CLAUDE (está rodando)

**O que é:** todo dia, na nuvem do GitHub (sem o PC do dono, nos tokens da assinatura **Max**), o Claude lê o briefing e produz uma **LEITURA COMPLETA do complexo** (análise por commodity com "o que sustenta a tese" destrinchado, riscos, leitura operacional long/short, spreads/crush, lente fiscal, honestidade), abrindo um **PR** que o dono aprova do celular.

**Como funciona (encanamento):**
- O robô (`radar.yml`, modo daily) escreve `briefing/latest.md` = **dump do dia + fila de julgamento** e **commita** (precisa de `permissions: contents: write` no job — já está). É o que a Routine lê (ela roda em clone sem o DB).
- O workflow **`.github/workflows/leitura.yml`** roda às **23 UTC** (+ botão manual): gate de custo (só chama o Claude se a fila tiver item) → `anthropics/claude-code-action@v1` → o Claude segue **`system/prompts/routine_julgamento.txt`** (o prompt da leitura completa, reescrito 19/jun pra PROFUNDIDADE) → escreve `insights/AAAA-MM-DD_leitura-complexo.md` → abre PR na branch `claude/insights-DATA`.
- **`guard-leitura.yml`** reprova qualquer PR `claude/` que toque fora de `insights/` (calibração nunca é tocada).
- **Fix de 19/jun (commit c9fc2b7) — encanamento à prova de re-run:** o `leitura.yml` agora (a) **pula se `claude/insights-<data>` já existe** no remoto (idempotência — antes o cron + um "Run workflow" manual empilhavam 2 commits "leitura DATA" na mesma branch); (b) injeta a data no prompt e manda o agente cortar a branch **sempre de `origin/main` fresco** (`git checkout -B`), eliminando o conflito por base velha; (c) reforça "SÓ `insights/`" no prompt. E o `guard` passou a comparar **`merge-base..head`** em vez de `base..head` (antes "zerava" quando o main avançava nos mesmos arquivos e deixava arquivo proibido escapar).

**Auth = assinatura Max** (NÃO API, sem cobrança extra): secret **`CLAUDE_CODE_OAUTH_TOKEN`** no repo, gerado com `claude setup-token`. **⚠️ O token vale 1 ANO (renovar ~jun/2027).** Se o workflow falhar com erro de auth, é só regenerar e atualizar o secret.

**Detalhe do `setup-token` (o dono usa o app empacotado/MSIX, o `claude` não fica no PATH):** rodar com o caminho real
`& "C:\Users\Usuario\AppData\Local\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude\claude-code\<versao>\claude.exe" setup-token`
(o `<versao>` muda a cada update do Claude Code; achar pelo `Get-Process claude | Select Path` ou pela pasta). O comando abre o navegador → login Max → imprime o token (`sk-ant-oat...`) → vai no secret.

**Permissões do workflow que foram necessárias (lições):** `contents: write` + `pull-requests: write` + **`id-token: write`** (OIDC da auth OAuth) no job; e `claude_args: --allowedTools Bash,Edit,Write,Read,Glob,Grep` (sem isso o agente toma `permission_denials` e não escreve nem abre PR).

**Custo:** ~$1 equivalente/run (placar do SDK, NÃO é fatura — sai da cota Max). 1 run/dia + gate (pula dias sem fila).

**Rotina do dono:** abrir o PR no celular → ler → merge → o site regenera com Drivers/score novos. (Auto-merge só se um dia confiar.)

**Histórico (resolvido 19/jun):** o PR de `claude/insights-2026-06-19` ficou travado (conflito em `leitura.yml` + 2 commits "leitura DATA" empilhados). Diagnóstico: o *conteúdo* dos insights estava bom (números batiam com o briefing) — o que quebrou foi o encanamento (ver fix c9fc2b7 acima). Branch deletada/PR abandonado por escolha do dono. O próximo run sai limpo e mergeável. Se o PR #2 antigo (versão rasa) ainda estiver aberto, fechar sem merge + deletar a branch.

---

## 🎯 FOCO 3 — Roadmap aberto (em ordem de valor)

### A) Físico: DISPLAY de venda (curto)
O input já aceita venda, mas o card físico (`_render_fisico_produto` via `latest_per_praca(tipo_posicao="compra")`) só mostra COMPRA. Estender pra mostrar os dois lados. (O bot `fisico` já mostra os dois no Telegram.)

### B) Durabilidade do bot de input (curto)
Hoje o físico do bot grava só no DB (durável na prática, mas some num wipe de cache). Hardening = commit-back do físico no `inputs_manuais.toml` (mesma capacidade do briefing-publish). Decidir se vale.

### C) Onda 3 — Fontes novas (backlog em `FONTES_CANDIDATAS_2026-06-16.md`)
ANP biodiesel BR (gap nº1 do óleo) · USDA FAS Export Sales (sinal China; chave grátis) · ComexStat/MDIC por NCM · Argentina FOB (datos.gob.ar) · SIFRECA frete · **NASS_API_KEY** (Crop Progress já existe, falta a secret) · parser ANEC (hoje é stub) · milho ZC=F (meal/corn).

### D) Revisão visual do site (o dono pediu)
Passar item a item nas telas validando densidade/cor/ordem da camada nova.

---

## 🗺️ ARQUITETURA (resumo)

- **Coleta:** GitHub Actions (`radar.yml`), 2 modos via `cloud_run.py`: `intraday` (**a cada 15 min**, 24/7: CBOT+câmbio → indicadores → HTML → pulso CBOT [30min/pregão] → alerta-na-hora → input físico via Telegram → healthcheck) e `daily` (~19h BRT: varredura completa + forecast + dump + **briefing** + resumo).
- **Disparo:** pinger **cron-job.org** (cron nativo do GitHub é best-effort). **PAT expira 31/dez/2026.**
- **Publicação:** HTML → GitHub Pages. DB → cache do Actions + backup diário (NÃO no git). `briefing/latest.md` SIM vai no git (commit-back do daily).
- **Camada manual:** `inputs_manuais.toml` (físico compra/venda, curva, params) → `sync()` aplica.
- **Camada de julgamento:** robô = FATO; Claude = LEITURA (`insights/*.md` com `vies:`). **Fase 1** (sessão paga, "lê a fila de julgamento e trata") + **Fase 2** (autônoma, LIGADA).

### Testes & comandos
- `cd system; $env:PYTHONIOENCODING="utf-8"` sempre.
- `.venv\Scripts\python.exe -m unittest discover -s tests` → **60 testes**.
- `main.py synth` (HTML do DB) · `main.py indicators` (recalcula + índices) · `main.py dump` (gera o dump) · `main.py queue` (fila) · `cloud_run.py --mode intraday|daily`.

---

## ⚠️ CAVEATS / GOTCHAS
1. **Token Max da Fase 2 vence em ~jun/2027** (`claude setup-token` de novo). **PAT do pinger vence 31/dez/2026.**
2. **`claude` não está no PATH** (app empacotado) — usar o caminho `...AppData\Local\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude\claude-code\<versao>\claude.exe`.
3. **Cron do GitHub é preguiçoso** — confiar no pinger cron-job.org. Healthcheck avisa se o daily morrer.
4. **PROIBIDO** recriar extração StoneX (marca d'água com e-mail corporativo). Fontes 100% públicas. Scraping CME/barchart = ToS (só spot-check manual, nunca coletor).
5. **Repo é PÚBLICO** (sem segredo no repo; tudo em Secrets).
6. **git commit no PowerShell:** mensagem longa quebra — usar vários `-m` de uma linha (ou `git -m` via bash).
7. **`print` em probe local** é cp1252 (Windows) — `≥`/emoji quebram; usar `PYTHONIOENCODING=utf-8`. Não afeta o HTML (UTF-8).
8. **Commit-back do daily faz o `main` avançar** todo dia (radar-bot) — antes de commitar local, `git pull --ff-only`.
8b. **Re-rodar a leitura no MESMO dia** (workflow_dispatch) agora é **pulado** pela trava de idempotência se `claude/insights-<data>` já existir — pra forçar um novo run no mesmo dia, **delete a branch antes** (`git push origin --delete claude/insights-<data>`).
9. Memória do projeto: `project_commodities_radar.md`. Preferência de estilo: `feedback_analise_detalhada.md` (deliverable analítico = PROFUNDO/explicativo; UI/alerta = compacto).

## 📂 Docs no repo
`FLUXO_JULGAMENTO.md` (camada de leitura + Fase 2) · `FONTES_CANDIDATAS_2026-06-16.md` (backlog) · `REVISAO_TRADER_2026-06-11.md` (⚠ a Onda P0 dela é lente de COMPRADOR — reenquadrar antes de usar) · `ARCHITECTURE_HTML.md` · `DEPLOY_NUVEM.md`.
