# Arquitetura do HTML diário — Commodities Radar

> **Princípio central:** o HTML diário (`reports/latest.html`) é o **produto final** do sistema. Toda evolução de coleta, análise, estudo e tese converge pra ele.
>
> Última atualização: 2026-06-11 (5ª rodada — interface): primeiro upgrade VISUAL do
> relatório — módulo `system/charts_svg.py` (SVG puro em Python, zero JS/dependência,
> testado): gráfico do farelo 52 semanas com níveis do alerts_config (Dashboard),
> sparklines de 30 pregões nos KPIs de preço, managed money net 5 anos no card COT,
> ratio Far/Soj colapsável, mini-barras de spread na curva forward. CSS: h2 com
> separador, hover nos KPIs, charts responsivos. 4ª rodada (sprint base de informação):
> backfills 5y CBOT/COT, percentil 52s nos KPIs, card COT, resumo 3 frases, fila D+N.
> 3ª rodada anterior: — CEPEA soja Paraná INTERIOR no bloco de
> referências da soja (+ spread porto−interior); guarda de datas na comparação física
> (delta só com gap ≤3 dias, senão "comparação suspensa" + CTA); suite de testes
> (32, `python -m unittest discover -s tests`); `main.py status`; snapshot diário
> automático pro consultor em shared/. 2ª rodada: cotações públicas NAG, Drivers por
> commodity data-driven, insights automáticos (auto-claude + vies). 1ª rodada: Saúde
> das fontes, calibração observada do forecast, remoção StoneX.

## Por que essa estrutura existe

O Commodities Radar gera múltiplas camadas de informação (coleta CBOT, paridades BR, mercado físico manual, matriz crush, margem biodiesel, forecasts, notícias, alertas, tese). Tudo isso num único HTML monolítico ficou ilegível conforme novas análises foram adicionadas.

A solução: **HTML com 5 abas via JS minimal**, com cada aba tendo um propósito cognitivo distinto. Quem abre o HTML cai no Dashboard (visão de 30 segundos) e navega pras outras conforme a dúvida.

## Diretriz arquitetural

> **HTML evolui continuamente.** Toda nova análise, indicador, estudo ou módulo entra numa das 5 abas existentes — não cria aba nova sem critério forte. Adicionar conteúdo dentro da aba certa é preferível a fragmentar mais a navegação.

**Crescimento esperado:** cada aba pode receber novos blocos (cards, tabelas, gráficos) sem afetar as outras. A barreira de "muito conteúdo" foi resolvida pela divisão em abas — agora o limite é apenas relevância.

## As 6 abas e seus propósitos

### 📊 Dashboard (default ao abrir)
**Propósito:** visão executiva de 30 segundos. O que o usuário precisa saber antes de agir hoje.

**Conteúdo atual:**
- Snapshot CBOT (KPIs de soja, farelo, óleo, USD/BRL)
- Resumo executivo (auto-gerado por heurística sobre dados do DB)
- Insights críticos (lista bullet com ícones bull/bear/neutral)
- Alertas técnicos ativos (quebra de suporte/resistência, movimentos fortes; níveis em `alerts_config.toml` — regra: nível = preço que muda a tese, recalibrar quando o mercado migra de regime)
- Saúde das fontes (2026-06-11): `<details>` colapsável cruzando registry × `coletas_log` — última execução de cada coletor vs cadência esperada (`_CADENCIA_FONTES`), sem falso-positivo de fonte mensal. Detecta automação parada (Task Scheduler) e coletor com erro.

**Quando adicionar coisa aqui:** apenas se for sumarização de impacto imediato. Cuidado pra não inflar — o ponto é ser breve.

### 💰 Mercado Físico
**Propósito:** decisão operacional de compra do dia (você é comprador de farelo/soja/óleo).

**Conteúdo atual:**
- Cards dos 3 produtos (soja em grão, farelo, óleo de soja degomado)
- Cada produto: Rancharia/SP + Paranaguá/PR com preço atual, variação, indicador suporte CEPEA, observação
- Rodapé por produto: paridade CBOT, spread PR-Rancharia, basis US$/bu (soja)
- Histórico 14 dias colapsável por produto
- Links de comando rápido (auditoria, export, input)

- Cotações públicas por produto (2026-06-11): bloco automático do coletor `nag_fisico` (Notícias Agrícolas) — farelo em 3 praças (Média RS Clicmercado, MT IMEA, Rondonópolis BCSP) + FOB Paranaguá implícito via prêmio público (farelo US$/sht, óleo cts/lb sobre CBOT). No farelo, badge na perspectiva do comprador: FOB abaixo do interno = "export não compete" (verde). No óleo, sem comparação direta (FOB export é estruturalmente descolado do degomado interno — só nota).

**Quando adicionar:** novos preços de praça (Rondonópolis, Sorriso), cotações B3 físicas. (Prêmios StoneX saíram em 2026-06-05 — extração proibida; o prêmio público NAG Paranaguá assumiu o papel em 2026-06-11.)

### 🧮 Análise Quantitativa
**Propósito:** stress test, cenários "e se?", calibração de tese.

**Conteúdo atual:**
- Card Ratio Far/Soj (2026-06-05, topo da aba): métrica central de decisão do comprador de farelo — `far_soj_ratio_pct` (farelo USD/sht ÷ soja USD/bu × 33,33), régua visual de zonas (<80 compra · 80-87 transição · ≥87 caro), tendência 5 pregões, histórico 14 pregões
- Matriz de cenários crush margin:
  - Sub-bloco Farelo implícito × Soja (4 sojas × 3 far/soj)
  - Bloco oil share atual (inline) com crush + óleo + farelo
  - `<details>` cenários alternativos de oil share
- Margem biodiesel americano:
  - Receita / custo / margem por galão
  - Alerta colorido por faixa
  - Sensibilidades colapsáveis (óleo ±5cts, HO -10%, RIN -20%)
- Drivers ativos POR COMMODITY (reescrito 2026-06-11): um bloco por produto (soja/farelo/óleo), cada um com colunas bull/bear. 100% data-driven, zero fato hard-coded — 3 fontes vivas: 📊 regras quantitativas sobre o DB (crush, oil share, ratio, momentum 5 pregões, FOB export vs interno, margem biodiesel, WASDE BR), ⚖️ Monitor Tributário (eventos vigentes/tramitando com produtos+direção), 💡 insights ativos com frontmatter `vies: [bull-farelo, bear-oleo_soja, ...]`

**Quando adicionar:** tabela S/U americano × CBOT esperado, matriz cenários óleo (com biodiesel), análise tradeoff fertilizante vs soja, decomposição de crush por margem de cada planta.

### 📅 Forecasts & Eventos
**Propósito:** olhar pra frente — o que esperar nos próximos 7-30 dias e quando.

**Conteúdo atual:**
- Forecasts 7d/30d (bandas estatísticas MA20+vol) + linha de calibração observada (2026-06-11): hit-rate real das bandas vs 87% teórica — honestidade do modelo; usar bandas como range de mercado calmo, não como limite de risco
- Eventos calendarizados próximos 14 dias (USDA Crop Progress, WASDE, NOPA, CFTC COT)
- Monitor Tributário/Regulatório (2026-06-05): catálogo curado `tributario_watch.toml` → tabela `eventos_tributarios` → card agrupado por jurisdição (BR/EUA/Indonésia) com status, direção, mecanismo e próximo marco. Materializa a regra da lente tributária BR.

**Quando adicionar:** calendário de safras BR/EUA/Argentina, datas RFS/EPA, vencimentos de contratos B3, reuniões consultor.

### 📰 Notícias & Tese
**Propósito:** contexto narrativo + agenda pessoal de leitura/decisão.

**Conteúdo atual:**
- Notícias recentes filtradas (soja/farelo/óleo) de CEPEA + G1 Agro + Canal Rural + FarmProgress
- Perguntas pra hoje (StoneX WhatsApp, consultor, forecasts vencendo)
- Tese ativa (link pro markdown)

**Quando adicionar:** análises de bancos (Itaú BBA, Rabobank), comentários de mercado, calendário pessoal.

### 💡 Insights (criada 2026-05-26 · insights automáticos desde 2026-06-11)

**Fluxo automático (2026-06-11):** após cada varredura em sessão, Claude Code lê
`data/last_dump.md` + insights existentes e gera 1-3 insights seguindo
`system/prompts/generate_insights.txt`. Convenções: tag `auto-claude` obrigatória
(distingue do manual), frontmatter `vies: [direcao-produto]` alimenta os Drivers
por commodity, máximo 1-3 por varredura (se nada mudou, não cria), atualização de
tese existente EDITA o arquivo antigo em vez de criar duplicata.

**Propósito:** resumos executivos de estudos/análises **pessoais** com lifecycle (criação, revisão D+90/D+180, arquivamento). Distinto dos "Insights críticos" do Dashboard, que são auto-gerados por heurística.

**Conteúdo atual:**
- Cards listados por data DESC (mais recente primeiro)
- Cada card: título, data, idade ("hoje", "ontem", "há Nd/Nsem"), status (ativa/revisada/arquivada), tags pills
- Resumo executivo em bullets (extraído da seção `## Resumo executivo` do .md)
- Ações pendentes em `<details>` colapsável
- Fontes consultadas (rodapé)
- Caminho do arquivo .md + comando pra abrir

**Storage:** arquivos `.md` em `insights/<YYYY-MM-DD>_<slug>.md` com frontmatter YAML (data, titulo, tags, fontes, status). Versionável via OneDrive, editável em qualquer editor.

**CLI:**
- `python main.py insight new "Título"` — cria template
- `python main.py insight list` — lista todos
- `python main.py insight open <slug>` — abre no editor
- Atalho Desktop "Novo Insight" — fluxo guiado

**Justificativa pra criar 6ª aba** (violação aparente do princípio "não criar aba sem critério forte"): insights pessoais têm fluxo próprio de criação, revisão e arquivamento. Misturar com Notícias (fluxo externo) confundiria. Decisão validada pelo usuário em 2026-05-26.

**Quando adicionar:** novo insight surge a cada estudo/análise/conversa importante. Não deve virar diário de bordo — só registros com tese-conclusão clara.

## Recursos UX implementados

| Recurso | Comportamento |
|---|---|
| **Tab navigation sticky** | Fica fixa no topo durante scroll |
| **Persistência tripla** | URL hash + localStorage + default Dashboard |
| **Atalhos teclado** | `1` Dashboard · `2` Físico · `3` Análise · `4` Forecasts · `5` Notícias · `6` Insights |
| **Animação suave** | fadeIn 0.2s ao trocar de aba |
| **Mobile-friendly** | Abas scrollam horizontal em tela estreita |
| **Bookmark-ready** | `latest.html#analise` abre direto na aba 3 |
| **Browser history** | Botões voltar/avançar funcionam |
| **Fallback sem JS** | `.no-js` mostra tudo (degradação graceful) |
| **Zero deps externas** | Funciona offline, sem servidor |

## Como adicionar novo conteúdo

1. **Decida a aba certa.** Use o "Propósito" de cada uma como filtro. Se duas abas servem, escolha a de menor densidade atual.
2. **Crie o getter em `notify_html.py`** seguindo o padrão `_get_<nome>(target)` que retorna dict.
3. **Crie o renderer** seguindo `_render_<nome>(data) -> str` que retorna HTML.
4. **Conecte no `_coletar_dados`** adicionando ao dict.
5. **Insira no `_renderizar`** dentro da `<section class="tab-pane" id="tab-X">` correta.
6. **Adicione CSS específico** se precisar de classes novas (perto das classes correlatas).
7. **Teste regenerando**: `python -c "from notify_html import gerar_html; gerar_html()"`

## Princípios de design

1. **Card-based:** cada bloco lógico é um `.card` (consistência visual)
2. **Cores semânticas:**
   - `bull` (verde) = altista / favorável
   - `bear` (vermelho) = baixista / desfavorável
   - `neutral` (cinza) = sem viés
   - `warn` (amarelo) = atenção
3. **Densidade decrescente:** o número grande fica no topo (preço, margem), contexto vem abaixo (variação, fonte, observação)
4. **Colapsabilidade:** detalhes históricos, sensibilidades e cenários alternativos vão em `<details>` pra não poluir
5. **Comandos no rodapé:** cada bloco que tem CLI relacionada exibe o comando em `<code>` no rodapé pra autoatendimento
6. **Idade do dado visível:** badges `hoje` / `D-1` / `D-N ⚠` em qualquer dado time-sensitive
7. **Watermark/origem:** dados manuais com observação, dados auto com badge da fonte

## Roadmap de evolução (não implementado)

Mapeado em conversas anteriores, ordem de prioridade flexível:

- [ ] Parser do PDF "Prêmios nos Portos" (StoneX) → entra em **Mercado Físico** (prêmio real em cents/bu, USD/sht, cents/lb)
- [ ] Tabela S/U americano × preço CBOT esperado → entra em **Análise**
- [ ] Card "Cenário base StoneX" (filtros do Fabio aplicados) → entra em **Análise**
- [ ] Sinais auto de compra/venda farelo por zona Far/Soj → entra em **Mercado Físico**
- [ ] Coletor automático de RIN D4 (EPA semanal) → indicador atualiza margem biodiesel
- [ ] D-1 nos KPIs (variação vs ontem) → entra em **Dashboard**
- [ ] Tese de cenário (PDCA) interativa → entra em **Notícias & Tese**

## Pra discutir/decidir no futuro

- Quando criar **6ª aba**? Critério proposto: só se algum tópico exigir 3+ blocos próprios E não couber semanticamente em nenhuma das 5 atuais.
- **Múltiplos HTMLs** (1 por dia histórico)? Hoje só `latest.html` é mantido vivo, daily snapshots ficam em `reports/YYYY-MM-DD_daily.html`. Bom assim.
- **Modo escuro/claro:** atualmente força dark. Considerar toggle se incomodar em telas claras.
- **Compartilhar com consultor:** quando exportar HTML pro consultor, esconder dados sensíveis (preços de compra do usuário) automaticamente.

---

*Documento mantido junto com o código. Atualizar sempre que mexer na estrutura macro do HTML.*
