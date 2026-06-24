# SUPER HANDOFF — Commodities Radar (atualizado 2026-06-22)

> Substitui versões anteriores. Histórico antigo fica no git.
> **Produto:** https://rpvessoni-sys.github.io/Commodities-Radar/#dashboard (atualiza sozinho na nuvem)
> **Repo:** github.com/rpvessoni-sys/Commodities-Radar (PÚBLICO)
> **Perfil do dono:** TRADER de soja, farelo e óleo degomado — opera os DOIS lados (long e short). Leitura SEMPRE neutra de preço (viés/spread/mean-reversion). NUNCA "comprador de farelo".

---

## 🔍 SESSÃO 2026-06-24 — Revisão item a item do Dashboard — ✅ COMPLETA (refino no ar)

> **▶️ PRÓXIMA CONVERSA — COMECE AQUI:** o **Dashboard** foi revisado item a item (12 partes) e o refino subiu pro `main` (deploy automático no próximo run do pipeline). **Próximo: aba 💰 Mercado Físico** — revisar item a item, MESMO método (o que traz / como traz / redundância no site / refino), atualizando este handoff a cada parte. **Pendências do Dashboard que ficaram:** Parte 3 (Snapshot — espera a chave do Barchart, gatilho "tenho a chave do Barchart") e Partes 7/8 (mover os gráficos pra Análise — fazer na fase da aba Análise).

**Modelo de trabalho (definido pelo dono):** parte a parte, EM SEQUÊNCIA, sem avançar nem misturar. Para CADA parte responder: (1) o que traz de informação; (2) como traz (mecanismo/fonte no código); (3) está mostrando em outro lugar DENTRO do próprio site? (redundância); (4) dá pra refinar a entrega? Handoff atualizado a cada etapa finalizada.

**Ordem das abas:** 📊 Dashboard → 💰 Físico → 🧮 Análise → 🧾 Forecasts → 📰 Notícias → 💡 Insights.

**Mapa das partes do Dashboard (sequência acordada):**
1. 🔔 Banner "N leitura(s) pendente(s)" ← ✅ REFINADO (a–d implementados; pendente commit/push)
2. 🧭 Mesa do dia (confiança + viés por produto) ← ✅ REFINADO (footer "explicado"; "o que observar" mantido a pedido do dono)
3. Snapshot — grid de KPIs (último fech. CBOT) ← 🔬 EM CURSO (ref: planilha Crush do Fabio; decisões + reliability registrados)
4. Resumo executivo (auto) ← ✅ REFINADO (virou "Leitura do dia" didática gerada pelo Claude diário)
5. O que mudou desde ontem (D-1) ← ✅ REFINADO (R1 zona no Ratio + R2 limiar de materialidade)
6. Sinais contraditórios ← ✅ REFINADO (texto didático nas 4 tensões; detecção segue determinística)
7. Gráfico Farelo 52 semanas (SVG) ← ➡️ MOVER pra aba Análise (decidido) + criar soja/óleo
8. Ratio Far/Soj — histórico (details) ← ➡️ MOVER pra aba Análise (decidido)
9. Insights críticos (auto) ← ✅ REMOVIDO (bloco redundante; aba "Insights de estudo" intacta)
10. Alertas técnicos ativos ← ✅ REFINADO (rótulo da base: "vs fechamento anterior")
11. Revisões de insight na fila (D+N) ← ✅ REFINADO (fix do truncamento word-safe)
12. Saúde das fontes (details) ← ✅ MANTER sem alteração (dono)

### ✅ Parte 1 — Banner 🔔 "N leitura(s) pendente(s)"
- **O que traz:** contagem de sinais que pedem LEITURA do Claude (camada de julgamento Fato→Leitura). Só renderiza se N≥1 (some quando a fila zera). É um CTA, não dado de mercado.
- **Como traz:** `notify_html._render_fila_banner(n)` (~linha 1911); `n = d["fila_pendentes"]` = `queue_emit.count_pendentes()` = itens severidade alta/media de `build_queue()` (determinístico, SEM LLM; 5 regras: ratio cruzou zona · nível de tese rompido · tributário ≤7d · release de fundamento ≤3d · revisão D+N de insight ≤7d). Mesmo número alimenta o resumo Telegram (`daily_summary.py:142`) e o alerta-na-hora (`alerts_push.py`).
- **Redundância no site:** o banner diz QUANTOS, não O QUÊ. O único item da fila com detalhe visível na MESMA aba é a revisão D+7 VENCIDA da Parte 11 ("Revisões de insight na fila") — quase certamente o MESMO sinal que o "1 pendente" conta, mas os dois não se conversam (topo = contagem sem conteúdo; base = conteúdo sem vínculo com o topo).
- **✅ REFINO IMPLEMENTADO (2026-06-24 — local, pendente commit/push):** reescrito `_render_fila_banner` em `notify_html.py` + novo getter `_get_fila_itens` (passa a LISTA da fila, não só a contagem `fila_pendentes`). O banner agora: (a) **lista cada item** com rótulo humano do tipo + título + "↳ O que decidir:" (a pergunta de leitura); (b) **se explica** em linguagem de leitor (o que é "leitura"/"tratar") e diz que **a leitura automática da Fase 2 já cuida** — não é mais só "abra o Claude"; (c) **cor por severidade** (🔴 alta=vermelho/`var(--bear)`, 🟡 média=âmbar/`var(--warn)`); (d) **carimbo "fila de DD/mmm"**. Escapa `<,>,&`. Mantém compat se receber `int`. **Só camada de render — calibração intacta.**
  - **Verificação:** `py_compile` ok · **64 testes OK** (`unittest discover`) · render com **DB real** confirmou que o "1 pendente" É a revisão D+7 VENCIDA da Parte 11 (mesma coisa em 2 lugares — redundância agora resolvida no topo).
- **Follow-up pequeno (NÃO é desta parte — fora de escopo):** o título do item vem **truncado em 55 chars** lá no `queue_emit.py:156` ("…spread far÷so"); corrigir no emissor depois (afeta também `main.py queue` e Telegram).
- **Decisão:** refinos rodados e verificados. **Falta commit/push** pro site (ação externa, repo público) — aguardando OK do dono.

### ✅ Parte 2 — 🧭 Mesa do dia
- **O que traz:** síntese de decisão em 30s — confiança global (alta/média/baixa/suspensa + motivos) · viés por produto (score −3…+3 + rótulo) · top driver ▲/▼ ("o que observar") · linha de invalidação.
- **Como traz:** `_render_mesa_do_dia` ← `_gerar_conviccao` (score = nº drivers bull − nº bear, clamp ±3; guards: perna CBOT travada→0, cap de momentum) + `_confianca_leitura` + `_linha_invalidacao`. Drivers de `_gerar_drivers` (dado/tributário/insight, cada um com `fonte`+`horizon`).
- **Veredito:** MANTER — é o melhor componente do dash. **R1 (ícones de procedência em "o que observar") CANCELADO** — dono prefere "o que observar" como está.
- **✅ REFINO IMPLEMENTADO (2026-06-24 — local, pendente commit/push):** reescrita a frase-rodapé pra linguagem de leitor (versão "explicada", escolhida pelo dono): *"Como ler: o viés é o **saldo de sinais** do produto — drivers de alta menos os de baixa, de −3 a +3. Mostra pra onde o preço tende e com que firmeza (long/short), **não** é ordem de compra/venda."* + `_linha_invalidacao` agora diz **"A leitura vira se o {produto} romper/perder o nível"** (antes "Vira" solto, sem sujeito). **Só texto — score/confiança/calibração INTACTOS.** Verificado: py_compile ok · render real da Mesa ok · **64 testes OK**.
- **Q&A registrado (forecast %):** o motivo "forecast acerto direcional X%" é **histórico/empírico** — `_get_forecast_calibracao` (`notify_html.py:200`): % das previsões JÁ RESOLVIDAS (data-alvo vencida, comparada com preço real) que acertaram a direção; recalc a cada synth; usa o PIOR horizonte; <55% → fail-closed "use range". 23% < 50% (moeda) = não confiar na direção. **Dono: está CERTO, NÃO alterar — serve de base pra calibração futura ("2ª parte").**

### 🔬 Parte 3 — 📊 Snapshot (EM CURSO — ref: planilha "Crush contas" do Fabio/StoneX)
**Planilha do dono (`Desktop/Crush.xlsx`, aba "Crush contas") decodificada — 6 blocos:** ① cotações vivas (Soja ZSN26 · Farelo ZMN26 · Óleo ZLN26 · Far/Soj · Oilshare · Crush mg) ② matriz Farelo implícito ÷ Soja ③ matriz Crush margin em **3 oilshares 50/53/56%** ④ **margem biodiesel como CURVA forward jul→dez** (receita HO+1,5×RIN − custo 7,5×óleo+industrial; custos abertos: operacional/metanol/logística/overhead; industrial=1,00) ⑤ crack spread / diesel renovável (gasolina RB / diesel HO / WTI) ⑥ **crush físico BR em R$** (farelo×yield + óleo×yield − custo − soja). **A fórmula do crush do Fabio = a nossa** (44 lb farelo + 11 lb óleo).

**DECISÕES (dono):**
1. **Cotações vivas:** mostrar SEMPRE o **contrato vigente** (hoje N26/jul), **rolando** no vencimento. *Já existe:* `sources/cme_cbot.py::_front_contract` (rola ~`ROLL_DIAS=12` antes do venc., busca contrato ativo explícito ZSN26.CBT pra bater com o Barchart) + abertura coletada + 5d derivado + guard anti-carry + `cbot_freshness` por commodity + fallback ScraperAPI. **Fonte REAL = Yahoo** (não Barchart). Caveat do projeto: scraping Barchart = ToS → usar só **API oficial como CONFERÊNCIA**.
2. **AJUSTAR p/ Fabio:** oil shares da matriz crush `47/50/53` → **`50/53/56`**; zonas Far/Soj `<80/80-87/≥87` → **`<80 / 85 / >90`**.
3. **Matrizes ② e ③:** manter.
4. **Margem biodiesel (aba Análise):** alinhar ao Fabio + **pré-salvar** (industrial `0,80→1,00`; estrutura forward; RIN/HO pendentes da fonte fiel).
5. **INSERIR — Crush físico BR em R$ (⑥):** ✅ dono curtiu muito (definir lugar: Análise ou perto do Físico).
6. **ADIAR até fonte fiel provada:** curva de biodiesel (dono gosta, mas "estamos falhando no básico" → reliability primeiro) e crack spread (⑤, aba Análise depois).

**Reliability — resposta ao dono ("como garantir leitura fidedigna?"):** a maior parte já existe (contrato ativo+roll, abertura, 5d, anti-carry, frescor por commodity, healthcheck). O que falta = (a) **2ª fonte de CONFERÊNCIA via Barchart-API oficial** (não scraping; 1×/dia; alerta se divergir >X%) + (b) **SELO visível no topo do Snapshot** (cotação DD/mm HH:MM · contrato N26 · ✓abertura ✓5d · ✅atualizada/⚠️travada), tirando a saúde do `<details>` do fim.

**🎨 VISUAL LOCKED (2026-06-24) — dono aprovou um mock polido ("achei mais bonito"):** (1) **barra de cabeçalho** "CBOT · Soja/Farelo/Óleo · Contrato vigente N26 · jul/26" + menu "…"; (2) **faixa de validação** (● cotações atualizadas · data/hora · **Mercado aberto/fechado** · 5d · Fonte Yahoo↔Barchart); (3) **"OS TRÊS INSUMOS"** = 3 cards (ícone em badge arredondado, nome+código ZSN26/ZMN26/ZLN26, preço grande+unidade, ▲/▼ vs abertura colorido, pill R$ paridade, barra 52sem com bolinha de percentil — âmbar se extremo, ex. óleo p87); (4) **"A CONTA DO CRUSH — O RESULTADO"** = 3 cards (Ratio Far/Soj c/ barra de zonas+marcador; Oil share c/ pill "média histórica 33%"; Crush margin c/ badge "zona gorda" + **barra 4 zonas** ruim/ok/zona-gorda/esticado, marcadores 2,50/3,26/4,25); (5) **CONTEXTO rebaixado** (USD/BRL · CFTC soja · Plantio EUA). **Respostas implícitas:** hierarquia OK · selo OK · **CFTC/plantio = REBAIXADOS, não removidos**.
**⚠️ Honestidade do selo:** só exibir "↔ confere Barchart" DEPOIS que a conferência via Barchart-API estiver ligada; até lá, só "Fonte: Yahoo". **Novos elementos a construir:** status Mercado aberto/fechado (horário de pregão CBOT, determinístico) + barra 4-zonas do crush.

**⛔ MUDANÇA DE RUMO (interrupção do dono, 2026-06-24):** o dono primeiro pediu "visual primeiro", mas LOGO EM SEGUIDA **EXIGIU que os dados sejam do BARCHART** ("exijo que seja do barchart"). Isso **descarta o Yahoo como fonte** — não basta "espelhar" o Barchart, ele quer o dado DO Barchart. Por isso o **build do visual foi PAUSADO** (eu estava prestes a inserir `_render_snapshot_v2`; NÃO cheguei a editar o código — só li). O selo "Fonte: Yahoo" não serve mais. **Scraping do site barchart.com = proibido (ToS, caveat #4)** → caminho legítimo = **API oficial do Barchart** (chave, possível custo, limites). Rodei um **workflow de pesquisa (`wf_d50383c5`)** sobre as opções reais: produtos de API/endpoints · custo & free-tier · ToS/licenciamento (incl. market-data CME) · cobertura front-month/roll/OHLC-com-abertura. **PRÓXIMO:** apresentar as opções ao dono (grátis serve? precisa pagar? quanto? precisa conta/chave?) → ele decide → aí (1) trocar/!somar a fonte Barchart no coletor, (2) construir o visual com selo honesto "Fonte: Barchart". Detalhes do `_render_snapshot_v2` planejado (cabeçalho + faixa + 3 insumos + a conta + contexto) já estão no VISUAL LOCKED acima — é só re-aplicar quando a fonte estiver definida.

**📊 PESQUISA BARCHART CONCLUÍDA (wf_d50383c5 — 4 frentes + verificação adversarial):**
- **Via oficial = Barchart OnDemand API** (REST, JSON/CSV, autentica com `apikey`). Scraping do site = PROIBIDO (confirmado nos ToS). Endpoint ideal: **`getQuoteEod`** (EOD: open/high/low/close/settlement/OI por dia — TEM abertura ✓). Histórico: `getHistory` type=daily/dailyNearest. Intraday: `getQuote` (campo `mode` R/I/D = real-time/delayed/EOD). Símbolos: **ZS*0 / ZM*0 / ZL*0**.
- **🔑 DECISÃO TÉCNICA *0 vs *1 (cravar c/ o dono):** `*0` = contrato MAIS ATIVO por open interest = **o que aparece na TELA do Barchart**; `*1` = nearest/front-month. **Divergem agora** (jun/26: `*1`=ZSN26 jul, `*0`=ZSX26 nov). Recomendado **`*1`** (nearest = o "N26 jul" que o dono citou). Roll no getHistory: `contractRoll=expiration|combined`, `daysToExpiration`.
- **❌ CUSTO (notícia ruim):** NÃO há free tier — morreu 31/12/2020; o US$49/mês não-comercial fechou junto (refutado na verificação). Preço NÃO-público, sob cotação (`solutions@barchart.com` / 312-566-9235). Ordem de grandeza: dezenas a ~centenas USD/mês (terceiros estimam ~US$500/mês, NÃO-oficial). NÃO está no RapidAPI (os ~US$25/75/150 são defaults genéricos do RapidAPI). Real-time exige exchange fees CME (caro) → **usar EOD/delayed** (mais barato; possível NonPro CBOT ~US$5/mês; CME reclassificou EOD→delayed pago em 2025). ToS: uso pessoal/interno sem redistribuir = permitido sob contrato.
- **▶️ AÇÃO DO DONO:** (1) decidir se paga + e-mail ao comercial Barchart (cotação EOD pessoal CBOT ZS/ZM/ZL: preço/limite/fees/trial) → obter `apikey`; (2) cravar `*0` vs `*1`. Claude se ofereceu pra redigir o e-mail.
- **🌉 BRIDGE Yahoo: REJEITADO pelo dono** ("não quero trabalhar com Yahoo — já tivemos problemas": preço congelado, cascata do farelo). **Decisão final: Barchart-only.**

**🟢 DECISÃO FINAL DA FONTE (2026-06-24):**
- **Fonte = Barchart OnDemand API, tier END-OF-DAY (`getQuoteEod`)**, símbolos **`ZS*1 / ZM*1 / ZL*1`**. Sem Yahoo.
- **Regra de roll (recomendação aceita):** `*1` nearest, mas **pulando os meses MAGROS da soja** (rola pro próximo LÍQUIDO: soja jan/mar/mai/jul/nov, pula ago/set → jul vai direto pra nov); farelo/óleo = nearest normal (líquidos todo mês); roll uns dias antes do *first notice* (`daysToExpiration`); **+ flag "pernas descasadas"** quando a soja rola pra safra nova antes do farelo/óleo (crush mistura velha×nova).
- **BLOQUEIO = a apikey** (ação do DONO: API é paga, sob cotação, sem self-serve/free tier). Entreguei no chat um **e-mail pronto** pra `solutions@barchart.com` (cotação EOD pessoal CBOT ZS/ZM/ZL: preço, limites, exchange fees CME/NonPro, trial).
- **▶️ PRÓXIMA SESSÃO (gatilho: "tenho a chave do Barchart"):** (1) ligar coletor Barchart `getQuoteEod` `*1`+roll-líquido (provavelmente novo `sources/barchart.py`; aposentar/desligar o `cme_cbot.py` Yahoo); (2) construir o `_render_snapshot_v2` (spec no VISUAL LOCKED acima) com selo real **"Fonte: Barchart"**; (3) verificar (py_compile + 64 testes + render real) e acumular no commit do Dashboard.
- **Stopgap opcional (se o dono pedir):** input manual das 3 cotações copiadas da tela do Barchart (100% Barchart, custo zero, sem Yahoo, mas manual) — ponte até a chave.

### ✅ Parte 4 — Resumo executivo → "Leitura do dia" (didática, gerada pelo Claude diário)
- **Decisão do dono:** NÃO remover/mesclar (minha sugestão inicial caiu). Quer o resumo **gerado pelo sistema, EXECUTIVO PORÉM DIDÁTICO ("mais ensina"), atualizado todo dia**. NÃO é reflexão manual — é a voz da máquina, mas explicando o porquê/mecanismo em linguagem de gente.
- **✅ IMPLEMENTADO (2026-06-24, local, pendente commit/push):** o topo do Dashboard agora puxa a **"Visão geral" da leitura auto-claude mais recente (Fase 2, ≤3 dias)** e renderiza como resumo didático, com selo **🧠 "Leitura do dia · Claude autônomo · DD/mmm"**; **fallback** pro template determinístico se não houver leitura fresca. Arquivos: `insights.py` (`_extract_visao_geral_full` + campo `visao_geral_didatica`), `notify_html.py` (`_resolver_resumo_executivo` + `_resumo_didatico_da_leitura`, trocado em `_coletar_dados`), e o prompt `prompts/routine_julgamento.txt` (seção "## Visao geral" reescrita pro tom "mais ensina"). **Só voz da Leitura — Fato/calibração intactos.**
- **Verificado:** py_compile ok · 64 testes OK · render real (DB) **já usa a leitura do Claude no topo**, não o template. ⚠️ O TOM "mais ensina" só aparece pleno no PRÓXIMO run diário da Fase 2 (a leitura atual foi escrita com o prompt antigo) — o dono vai querer iterar o tom vendo o resultado real. **Independe do Barchart.**

### ✅ Parte 5 — O que mudou desde ontem (D-1)
- **O que traz/como traz:** tabela de variação D-1 dos 4 indicadores do complexo (Ratio Far/Soj, Oil share, Crush, USD/BRL) via `_render_o_que_mudou` + `_MUDOU_SPECS`; Δ sobre valores arredondados, datas reais. **Veredito: MANTER** (info complementar — variação D-1, que o Snapshot não dá igual).
- **Achado:** (a) contradição — D-1 dizia Ratio "esticando" enquanto KPI/Mesa dizem "comprimido" (janelas diferentes, palavras opostas na mesma tela); (b) ruído ganhava leitura direcional (crush −0,01 → "menos rentável").
- **✅ IMPLEMENTADO (2026-06-24, local, pendente commit/push):** **R1** — Ratio usa frase neutra de movimento ("farelo ganhou/cedeu vs soja no dia") + situa na ZONA atual ("· segue comprimido", de `far_soj.zona`); passei `d` (não só `target`) ao `_render_o_que_mudou`. **R2** — limiar de materialidade por indicador (Ratio 0,3pp · Oil share 0,4pp · Crush 0,05 · USD/BRL 0,02); abaixo → "estável", sem narrativa de ruído. **Fato/calibração intactos.** Verificado: py_compile · 64 testes · render real → `['estável · segue comprimido','estável','estável','real mais fraco — sobe a paridade']`. Independe do Barchart.

### ✅ Parte 6 — Sinais contraditórios
- **O que traz/como traz:** `_gerar_contradicoes(d)` detecta TENSÕES entre sinais (4 regras determinísticas: convicção soja/farelo, zona do Ratio, oil share, COT percentis, momentum 5d) + `_render_contradicoes`. **Veredito: MANTER** — bloco mais bem-construído (baixa redundância, cruza preço×posicionamento). Dispara só quando há tensão; some se não houver.
- **✅ IMPLEMENTADO (2026-06-24, local, pendente commit/push):** a pedido do dono, deixei o texto das **4 tensões DIDÁTICO** — explica o mecanismo e traduz o jargão (crush, oil share, managed money, percentil "= mais comprados que X% da história", mean-reversion, capitulação, "faca caindo"). **Detecção segue determinística/auditável — só o texto mudou.** Verificado: py_compile · 64 testes · render real (óleo p96 + spread p52) didáticas.

### 🗂️ Partes 7 & 8 — DECISÃO: MOVER pra aba 🧮 Análise Quantitativa (não feito ainda)
- **Decisão do dono (2026-06-24):** tirar do Dashboard o **gráfico Farelo 52 semanas** (Parte 7) e o **Ratio Far/Soj histórico** (Parte 8); levar pra aba Análise e lá ter **3 gráficos de 52 semanas (soja, farelo, óleo)** no mesmo estilo + o histórico do Ratio. Declutter do Dashboard (objetivo de elegância).
- **A FAZER (fase da aba Análise / batch):** gerar as séries 52sem de soja e óleo (hoje só farelo tem; `charts_svg` + snapshot já têm min/max/série), mover os renders pra seção da Análise, remover do `tab-dashboard`. Cross-tab → não misturar com o Dashboard agora.

### ✅ Parte 9 — Insights críticos → REMOVIDO
- **Decisão do dono:** REMOVER o bloco — era o MAIS redundante do Dashboard (crush/paridade/plantio/CFTC/notícia já apareciam no Snapshot/Mesa/D-1/Sinais contraditórios/aba Notícias; valor novo era só níveis prospectivos + horizontes, que migram pra Mesa/Eventos).
- **✅ IMPLEMENTADO (2026-06-24, local, pendente commit/push):** removido o render (`<h2>Insights críticos</h2>` + `<ul class="insights">{_render_insights(...)}</ul>`, em `notify_html`) e a computação `base["insights"] = _gerar_insights(base)`. **A aba "💡 Insights de estudo" NÃO foi tocada** (é outra coisa — as leituras do Claude). Verificado: py_compile · 64 testes · HTML sem "Insights críticos", aba Insights intacta.
- **🧹 Código órfão (limpeza futura, sem pressa / pode entrar no reset final):** `_gerar_insights` (~115 linhas, `notify_html.py` ~3919) e `_render_insights` (~1812) ficaram sem uso — não afetam a saída; deletar numa passada de limpeza.

### ✅ Parte 10 — Alertas técnicos ativos
- **O que traz/como traz:** `_get_alertas_tecnicos` (lê `alerts_technical.json` + reconcilia com config vivo, descarta nível recalibrado) + `_render_alertas`. Event-driven (movimento forte / quebra de nível) + lente 🟢/🔴. **Veredito: MANTER** (baixa redundância — é "aconteceu agora").
- **Achado:** "MOVIMENTO FORTE — soja +2,90% no dia" (fechamento-a-fechamento) brigava com o KPI "+0,8% vs abertura" — duas %s do dia da mesma commodity sem rótulo de base.
- **✅ IMPLEMENTADO (2026-06-24, local, pendente commit/push):** R1 — o alerta de movimento forte agora diz **"…% no dia (vs fechamento anterior)"** (base confirmada no `alerts_technical`: pct close-to-close, `valor_atual` vs `valor_anterior`). Quebra de suporte/resistência NÃO ganha o rótulo (não é % diário). Mantido compacto (alerta=compacto). Verificado: py_compile · 64 testes · render. Independe do Barchart.
- *(Nota menor, fonte:)* o alerta não mostra DATA → quando resolver frescor/Barchart, carimbar a data (evita alerta velho parecer de hoje).

### ✅ Parte 11 — Revisões de insight na fila (D+N)
- **O que traz/como traz:** `_get_revisoes_pendentes` (revisões D+N vencidas/≤7d dos insights ativos) + `_render_revisoes`; some se vazio. Tracker de dívida de manutenção. **Veredito: MANTER** — tem o checklist de revisão específico do insight que o banner não tem.
- **Overlap conhecido:** a mesma revisão vencida aparece no banner do topo (Parte 1) E neste card — aceito como complementar (banner=alerta/CTA; card=agenda com as perguntas).
- **✅ FIX IMPLEMENTADO (2026-06-24, local, pendente commit/push):** truncamento do título corrigido — antes cortava no meio ("…viés baixi"), agora corta no limite da PALAVRA com "…" e só acima de 110 chars (títulos médios aparecem inteiros). Verificado: py_compile · 64 testes · render (médio completo, longo word-safe).

### ✅ Parte 12 — Saúde das fontes
- **Veredito do dono: MANTER sem alteração.** Conteúdo bom (cruza registry × `coletas_log`, ignora `data_referencia` enganosa, ordena problemas primeiro). O único ponto (ficar escondido num `<details>` recolhido justo quando importa) foi decidido **não mexer agora** — a visibilidade de topo virá pelo **selo de validação do Snapshot** (Parte 3, depende do Barchart). R1 (auto-abrir) NÃO aplicado, a pedido.

### 🚀 DASHBOARD — REVISÃO ITEM A ITEM COMPLETA (12/12) + SUBIU PRO MAIN
- **No `main` (commit desta sessão, 2026-06-24):** Partes **1, 2, 4, 5, 6, 10, 11 refinadas + 9 removida** + prompt da Fase 2 (`## Visao geral` didática). **Só camada de render/voz — Fato/calibração intactos; 64 testes OK.** O HTML ao vivo regenera no próximo run do pipeline (com dados frescos da nuvem). Arquivos: `system/notify_html.py`, `system/insights.py`, `system/prompts/routine_julgamento.txt`.
- **Pendências do Dashboard (NÃO feitas):** Parte 3 (Snapshot redesenhado — VISUAL LOCKED salvo acima; espera `apikey` Barchart → gatilho "tenho a chave do Barchart"); Partes 7/8 (mover Farelo 52sem + Ratio histórico pra Análise + criar soja/óleo).
- **🧹 Código órfão a limpar (sem pressa):** `_gerar_insights`/`_render_insights` em `notify_html.py` — sem uso após remover a Parte 9.
- **▶️ PRÓXIMA ABA: 💰 Mercado Físico** (revisar item a item, mesmo método).

### 📌 PENDÊNCIAS DO REFINO (decididas com o dono — fazer no momento certo, NÃO agora)
- **🏁 [MARCO DE ENCERRAMENTO — só DEPOIS de readequar TODAS as abas] RESET DO SISTEMA (apagar histórico, começar do zero).** O dono reforçou (2026-06-24): quer **resetar o sistema** pra os registros nascerem limpos — **não é só a calibração do forecast**; é o histórico que foi contaminado pela **era dos bugs** (cascata do farelo congelado etc.) e, provavelmente, **alinhar ao corte de fonte Yahoo→Barchart** (preço Yahoo antigo fica inconsistente com o Barchart novo). Escopo a definir na hora: `forecasts` (hit/miss), série de `indicators` da era buggada, e possivelmente **rebaseliar os preços no cutover do Barchart**. Frase do dono: *"resetar o sistema e começar do zero para ter registros mais limpos"*, **só quando finalizar toda a readequação**. (definir/criar o comando de reset + decidir o que preservar.)
- **[FAZER NA ABA 🧾 FORECASTS] `<details>` "acertos × erros — 14 dias".** Painel abre/esconde com o histórico dia-a-dia de acerto/erro do forecast — a versão rica de "explicar o 23%". Dado já existe na tabela `forecasts` (hit / hit_direcional + data). Dono curtiu. Fazer quando chegarmos na aba Forecasts (não misturar com o Dashboard agora).

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
