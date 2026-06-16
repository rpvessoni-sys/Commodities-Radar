# Handoff — próxima conversa

> Última atualização: **2026-06-11** (sessão "Melhoria contínua").
> Handoff anterior (2026-05-26) ficou obsoleto — este substitui por completo.

## 🚀 SPRINT "BASE DE INFORMAÇÃO" (2026-06-11, 4ª rodada — pós revisão trader)

Decisão de produto: usuário **NÃO está operando** — sistema é base de informação/aprendizado.
A onda P0 da revisão (plano de tranches, cadastro de exposição, "Ação do dia") foi ADIADA
até ele operar; implementou-se o que enriquece a leitura sem pedir input:

1. **Backfill 5 anos CBOT** (`system/backfill_cbot.py`, one-shot idempotente): 4.929 pregões
   2021-2026 (ZM/ZS/ZL/HO, série front-month contínua — saltos de rolagem documentados no contexto).
2. **Backfill COT 2021-2025** (`system/backfill_cot.py`): 6.264 registros, 283 semanas/commodity.
3. **3 bugs da revisão corrigidos**: tese ativa agora deriva do insight vivo (status ativa/revisada,
   preferindo com vies); snapshot do consultor virou executivo real do DB público (1,4KB);
   KPI crush + alertas leem níveis do alerts_config (alertas com nível divergente da config = descartados).
4. **KPIs reordenados na lente do comprador**: farelo + ratio Far/Soj primeiro, variação D-1
   (farelo caindo = verde), range/percentil 52 semanas; oil share/CFTC/plantio viraram "contexto".
5. **Resumo executivo em 3 frases rotuladas**: Mercado / Pro comprador / Leitura (~50 palavras).
6. **Card COT** (aba Análise): managed money net + Δ semana + percentil 5 anos + open interest,
   com leitura pro comprador. **Hoje: farelo p94 — fundos comprados perto do máximo histórico
   com preço fraco = desmonte é risco baixista; paciência tem amparo.**
7. **Spreads de calendário** no card curva (front→último, classificação carry/flat/inversão).
8. **Histórico 14d do prêmio export PGUA** (colapsável) + driver de virada (±2 US$/sht).
9. **Fila de revisões D+N**: insights.py parseia "## Revisão programada"; Dashboard e
   `main.py status` cobram revisões vencendo em ≤7 dias (D+7 do ratio-81 = 18/jun na fila).
10. **Cores do físico corrigidas**: pagar abaixo do indicador = verde; dado velho = âmbar
    (badge warn novo); spread entre praças sem julgamento.

⚠️ **ACHADO DE MERCADO do backfill**: farelo 303,60 = **percentil 57** da série contínua de
52 semanas (mín real 260,70 em 2025) — o "perto da mínima 52sem (293)" valia só pro contrato
atual. Insight ratio-81 atualizado (status revisada): tese de tranches agora apoia-se em
ratio + prêmio zerado + estrutura do crush + COT p94, SEM o argumento de preço absoluto raro.

36 testes OK (`python -m unittest discover -s tests`).

## 🔧 MELHORIA CONTÍNUA 2026-06-11 (ciclo PDCA aplicado)

**Diagnóstico encontrou e o ciclo corrigiu:**

1. **Projeto agora tem GIT** (`git init` na raiz, 2 commits: baseline + limpeza). `.gitignore` exclui `data/`, `reports/`, `inbox/`, `shared/`, `.venv`, `.env` (chaves ScraperAPI/NASS). Identidade local genérica (`Usuario <usuario@radar.local>`) — trocar se quiser. Antes não havia versionamento nenhum (OneDrive não é rollback).
2. **Código morto de extração deletado** (10 arquivos, −1.633 linhas): ingest_stonex, parse_stonex, parse_pdf, parse_premios_portos, check_missing, daemon_watcher(.py/.ps1), daemon.py, stonex_catalog.toml, bookmarklet.html. `premios list` foi internalizado no main.py (só leitura do histórico). config.py perdeu bloco IMAP/INBOX/STONEX_RAW. pypdf e watchdog desinstalados e fora do requirements.
3. **Alertas recalibrados** (`alerts_config.toml`): níveis pré-crash geravam ruído diário (crush 3,78 vs resistência 2,00 disparava todo pregão). Regra nova: **nível de alerta = preço que muda a tese**. Níveis atuais: soja 1100/1180, óleo 72/80, farelo 290/325, USD 4,90/5,30, crush 2,50/4,25.
4. **Forecast: hit-rate exposto no HTML** — banda 7d acertou só 46% (n=24) vs ~87% teórica; direção 8%. NÃO é bug (verificado caso a caso): o modelo ma20_vol_bands foi atropelado pela quebra de regime de 04/jun (slope altista por inércia enquanto o mercado desabava). Linha de "Calibração observada" agora aparece no card de forecast — bandas são range de mercado calmo, não limite de risco.
5. **Card "Saúde das fontes" no Dashboard**: registry × coletas_log, cadência esperada por fonte, sem falso-positivo de fonte mensal. Detecta automação parada e coletor com erro.
6. **run_radar.ps1 com PYTHONIOENCODING=utf-8** — sob Task Scheduler o Python escrevia cp1252 no pipe e podia quebrar com acento (caveat #1).

**2ª rodada do mesmo dia (pedido do usuário):**

1. **Cotações públicas no Mercado Físico** — novo coletor `nag_fisico` (Notícias Agrícolas, 3 págs/dia via ScraperAPI): farelo físico em 3 praças (Média RS, MT IMEA, Rondonópolis) + **prêmio farelo Paranaguá (US$/sht)** + **prêmio óleo Paranaguá (cts/lb)** — o prêmio público substitui o sinal perdido dos PDFs StoneX. Card do físico mostra bloco "🌐 Cotações públicas" com FOB implícito e, no farelo, badge na lente do comprador ("export não compete" = verde). No óleo só nota (FOB export descolado do degomado interno — não comparar direto).
2. **Drivers ativos POR COMMODITY** — reescrito do zero: a versão antiga tinha fatos hard-coded da varredura de 05/jun apodrecendo no código. Agora 1 bloco por produto (soja/farelo/óleo) com 3 fontes vivas: 📊 regras quantitativas (crush, oil share, ratio, momentum 5 pregões, FOB vs interno, margem biodiesel, WASDE BR), ⚖️ Monitor Tributário (eventos com produtos+direção), 💡 insights ativos com `vies:`.
3. **Insights automáticos** — convenção em `system/prompts/generate_insights.txt`: após varredura, Claude Code lê `last_dump.md` + insights existentes e gera 1-3 insights com tag `auto-claude` e frontmatter `vies: [bear-farelo, ...]` (que alimenta os Drivers sozinho). Template do `insight new` já traz o campo. **1º insight auto criado: `2026-06-11_ratio-81-prepara-janela-de-tranches-farelo.md`** (ratio 81,4% + FOB zerado = janela de tranches se armando; revisão D+7 em 18/jun).

**3ª rodada do mesmo dia ("melhoria contínua até zerar os tokens"):**

1. **CEPEA soja Paraná INTERIOR** no `nag_fisico` (4ª página NAG) — praça real do usuário (Araucária/PR). Bloco de referências da soja mostra interior + **spread porto−interior** (~R$ 6,7/sc em 10/jun, custo logístico).
2. **Guarda de datas na comparação física** (correção do feedback "ficou confuso"): delta vs sua compra SÓ com gap ≤3 dias entre as datas; acima disso vira "⚠️ Comparação suspensa: sua compra é de DD/mm (N dias antes)" + CTA `fisico add`. Bloco renomeado "Referências de mercado" com coluna de data em toda linha; "FOB implícito" → "Paridade export PGUA (CBOT+prêmio)". Driver "export não compete" respeita a mesma guarda.
3. **Suite de testes** (32 testes, `python -m unittest discover -s tests`, ~0,1s, offline): parser NAG com fixture HTML, frontmatter/vies dos insights, banda do forecast, validação dos catálogos TOML (typo de enum em tributario_watch vira erro de teste). Refactor: `iter_tabelas()` puro em nag_fisico (parse sem rede).
4. **`main.py status`** — saúde no terminal: fontes com cadência, idade dos inputs manuais (alerta "VELHO" >3d), forecasts (banda observada), próximos marcos tributários 30d.
5. **Snapshot diário automático pro consultor**: `synth` agora copia o daily.md pra `shared/to_consultor/snapshots_diarios/` (antes a pasta nunca era alimentada). Falta só compartilhar `shared/` no OneDrive (pendência antiga do usuário).
6. **README do system reescrito** (o antigo ainda ensinava bookmarklet/ingest/check StoneX) + **schema.sql sem as 4 tabelas-fantasma** (dados_extraidos/precos/teses/eventos — 0 linhas, 0 referências; DROP no DB vivo foi bloqueado por permissão, inofensivo, ficam vazias) + **backup manual do DB** feito (data/backups/radar_2026-06-11.db).
7. **Coerência narrativa**: resumo executivo agora lê suporte/resistência do `alerts_config.toml` (fim do hard-code que apodrecia); insight do crush não alega mais "alerta disparado em $2,00" (resistência atual é 4,25 — $2,00 ficou como referência econômica de "zona gorda", explicitado no comentário).
8. **`far_soj_ratio_pct` virou função pura** em indicators.py com teste do caso real de 11/jun (81,39%) + fronteira de zona — a métrica central do comprador está protegida contra regressão (35 testes no total).
9. **WASDE jun**: coletor rodou 13h e 13h15 e Cornell ainda espelhava o de maio (saved 0) — a run noturna 22h pega, ou rodar `public --source usda_wasde` manualmente no fim da tarde. **Pós-WASDE: revisar o insight do ratio (D+7 já marca isso).**

**⚠️ PENDENTE — AÇÃO DO USUÁRIO (1 comando):** as 7 tasks `CommoditiesRadar_*` **NÃO existem** no Task Scheduler — descoberto no diagnóstico que as coletas só rodam manualmente (04, 08 e 09/jun ficaram sem coleta; CBOT se salva por backfill do yfinance, mas CEPEA Paranaguá/PTAX/notícias perdem os dias). O registro foi bloqueado por permissão na sessão. Rodar:
```powershell
cd C:\Users\Usuario\OneDrive\Desktop\Program\commodities-radar\system
powershell -ExecutionPolicy Bypass -File .\setup_scheduler.ps1
# valida: .\setup_scheduler.ps1 -List
```

## 🛑 MUDANÇA ESTRUTURAL — Extração StoneX PROIBIDA (2026-06-05)

A validação de ToS resultou em **NÃO**: extração de resultados dos relatórios StoneX não é mais permitida. Ajustes aplicados nesta sessão:

**Removido:**
- `stonex_pdf_downloader.py` deletado + Playwright desinstalado do venv (cache de browsers da máquina ficou — motoparts usa)
- CLI: `stonex-pdf`, `ingest`, `check`, `premios import` removidos
- `cmd_run` não chama mais ingest/check — pipeline agora: `public → indicators → alerts → forecast → synth → dump`
- HTML: cards "Prêmios StoneX por contrato" e "Relatórios StoneX em atraso" removidos

**Mantido (legítimo):**
- Dados históricos no DB (premios_portos até 25/mai, relatorios_stonex) — `main.py premios list` consulta
- Call semanal com Fabio + anotação manual de números falados: `curva set stonex`, `param set`
- Insights manuais de leitura própria do usuário
- Coluna "StoneX" no card 4 curvas (é input manual de call, não extração)

**Compensação de sinal:**
- Basis implícito da soja sai automático: CEPEA Paranaguá vs paridade CBOT (card físico)
- Farelo/óleo: prêmio vs paridade calculado quando usuário inputa via `fisico add`
- Perguntar pro Fabio na call os números que antes vinham do PDF (prêmios por contrato)

## 🎯 O QUE É O SISTEMA HOJE

Radar de **soja, farelo e óleo de soja** (complexo soja APENAS), 100% fontes públicas + inputs manuais. Produto final = HTML diário de 6 abas (`reports/latest.html`, atalho Desktop "Radar Daily"). Task Scheduler roda seg-sex (Morning 07h `run`, Evening 19h `public cme_cbot`, Indicators 20h, Alerts 20h15, Night 22h `run`, Friday 18h COT, Backup sáb 23h).

**Perspectiva do usuário: COMPRADOR DE FARELO** (ração, B2B). Farelo caindo = bom.

## 📊 SNAPSHOT (11/jun/2026 — fechamento mais recente no DB)

| Indicador | Valor | Leitura |
|---|---|---|
| Soja CBOT jul | 1.119,00 ¢/bu | Queda continua (clima US bom + China travada) |
| Farelo CBOT jul | **303,60 USD/sht** | Caiu mais 3% desde 05/jun; mínima 52sem é 293 |
| Óleo CBOT jul | 75,34 ¢/lb | Firme perto da máxima (RFS + 45Z) |
| Crush margin | US$ 3,78/bu | Esmagadora segue a 100% |
| Oil share | 55,4% | Óleo manda no crush, subindo |
| **Ratio Far/Soj** | **81,4%** | **Comprimiu de 83,3 → 81,4 em uma semana — caminhando pra zona de compra (<80%)** |
| USD/BRL PTAX | ~5,04 | Real firme |

⚠️ **WASDE de junho sai HOJE 11/jun (~13h BRT)** — primeiro gatilho da fila. Ler óleo soja S/U US 26/27 + estoque mundial.

**Tese ativa (comprador de farelo):** complexo PARTIDO — óleo forte (EUA/biodiesel) vs farelo fraco (subproduto despejado). Queda do farelo está ACONTECENDO (−US$12 em 2 pregões 3-4/jun, FOB Paranaguá em mínima histórica), mas ratio Far/Soj não comprimiu (soja caiu junto). **Recomendação: compra em tranches aproveitando preço absoluto baixo, sem esperar ratio 77%.** Risco principal: China destravar compras e levantar o complexo todo.

## 📦 SESSÃO 2026-06-05 — o que foi entregue

1. **Varredura completa** (5 agentes web + coleta sistema): insight-síntese em `insights/2026-06-05_varredura-completa-complexo-soja.md` com snapshot, 5 eixos, reconciliação de teses e 6 gatilhos
2. **Card Ratio Far/Soj** (aba Análise, topo): `far_soj_ratio_pct` em indicators.py, régua visual de zonas, tendência na perspectiva do comprador, histórico 14 pregões
3. **Monitor Tributário/Regulatório** (aba Forecasts): catálogo `system/tributario_watch.toml` (10 vetores) → `eventos_tributarios` → card agrupado por jurisdição. CLI `tributario {sync|list}`. Auto-sync no synth.
4. **Correções factuais em 2 insights** (status `revisada` + bloco de atualização no topo): subvenção fóssil (MP 1.363 nova, R$1,12/L até dez; atribuição MP corrigida; sem ADI formal) e PIS/Cofins (isenção PRORROGADA até 31/jul, não revogada; leilão ANP não existe desde 2022; aperto fiscal NÃO trava esmagamento — óleo escoa via exportação +105%)
5. **Remoção StoneX** (ver topo)

**Insights ativos (8 arquivos em `insights/`):** b16-bullish-farelo · esmagamento-recorde · curva-forward-oleo-desacopla · pis-cofins (revisada) · subvencao-fossil (revisada) · stonex-mensal-mai (último da série — descontinuada) · varredura-completa-05jun

## 👀 GATILHOS PRÓXIMAS 2-4 SEMANAS

1. **WASDE 11/jun** — estoque óleo soja US/mundial 26/27 (aperto confirma óleo forte?)
2. **MPOB maio ~10/jun** — estoques palma
3. **NOPA maio ~15/jun** — esmagamento US manteve +11% YoY?
4. **RFS entra em vigor 15/jun** — repasse no RIN D4
5. **MP 1.358 (gasolina)** — deliberação Congresso até 11/jul
6. **Isenção PIS/Cofins biodiesel** — vence 31/jul (renova?)
7. **Ratio Far/Soj** — comprime de 83% pra <80%?
8. **China** — destravou compras de soja US? (risco altista pro complexo)

## 🚀 COMANDOS

```powershell
cd C:\Users\Usuario\OneDrive\Desktop\Program\commodities-radar\system
$env:PYTHONIOENCODING="utf-8"

.\.venv\Scripts\python.exe main.py run                    # pipeline completo
.\.venv\Scripts\python.exe main.py public --source cme_cbot   # só CBOT
.\.venv\Scripts\python.exe main.py tributario list        # monitor fiscal
.\.venv\Scripts\python.exe main.py tributario sync        # após editar tributario_watch.toml
.\.venv\Scripts\python.exe main.py fisico add             # input físico manual
.\.venv\Scripts\python.exe main.py curva set stonex --produto oleo --venc N26 --valor 75.5 --detalhe "Fabio call"
.\.venv\Scripts\python.exe main.py insight new "Titulo"   # novo insight
.\.venv\Scripts\python.exe main.py premios list           # histórico (só leitura)
start "C:\Users\Usuario\OneDrive\Desktop\Radar Daily.lnk" # abre HTML
```

## 📋 FILA (prioridade sugerida)

0. **Registrar Task Scheduler** (1 comando, ver seção Melhoria Contínua acima) — sem isso o sistema não coleta sozinho
1. **Pós-WASDE 11/jun**: rodar varredura curta (CBOT + ler WASDE óleo) e atualizar insight varredura ou criar novo
2. **Call Fabio**: (a) prêmios por contrato falados em call → `curva set` / anotação; (b) validar basis Paranaguá real (varredura achou ~−11,4 ¢/lb, relatório StoneX antigo sugeria ~20 ¢/lb — divergência aberta); (c) onde StoneX vê o ratio Far/Soj indo; (d) quanto do esmagamento BR depende de export de óleo vs biodiesel interno
3. **Monitor tributário Tier 2** (futuro, opcional): coletores automáticos (APIs Câmara/Senado, RSS Planalto, calendário leilões) — hoje o catálogo é manual
4. **Card "Balanço óleo soja BR"** trimestral (produção/consumo/export YoY via ABIOVE) — proposto no insight stonex-mensal
5. **Compartilhar `shared/` no OneDrive** com consultor (pendência antiga, 5 min manual)

## ⚠️ CAVEATS

1. `PYTHONIOENCODING=utf-8` sempre no PowerShell (run_radar.ps1 já seta sozinho desde 2026-06-11)
2. OneDrive pode dar lock no SQLite — se quebrar, mover pra `C:\Dev\`
3. **NÃO recriar nenhum mecanismo de extração StoneX** (downloader, parser de PDF novo, ingest de email) — proibido desde 2026-06-05. Os módulos foram DELETADOS em 2026-06-11 (recuperáveis só no commit baseline do git, não recuperar).
4. ScraperAPI: usado só pra fontes públicas com anti-bot (CEPEA via Notícias Agrícolas)
5. Memória persistente: `project_commodities_radar.md` + regra `feedback_lente_tributaria_br.md` (lente fiscal ANTES de concluir tese BR)
6. **Git existe desde 2026-06-11** — commitar mudanças de código com mensagem decente; `data/`, `reports/` e `.env` são ignorados por design
7. ARCHITECTURE_HTML.md: atualizar SEMPRE que mexer em card/aba (regra foi violada em 06-05 com Far/Soj e Tributário; corrigido retroativamente em 06-11)
