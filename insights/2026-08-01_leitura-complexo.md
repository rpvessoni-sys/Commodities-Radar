---
data: 2026-08-01
titulo: "Sábado sem pregão novo (mercado fechado), mas a revisão do fechamento de sexta-feira aprofunda a leitura bear do óleo (suporte 72,00 rompido agora a -6,58%, ante -6,29% no print preliminar) e revela uma compressão muito mais forte do oil-meal spread (-9,32% no dia, ante -3,18% visto ontem com o número ainda preliminar) — enquanto o ratio Far/Soj, também revisado, se afasta de novo do piso de 80% (80,69%, ante 80,55% preliminar), reforçando que o gatilho tático da tese `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` segue sem confirmação 44 dias após o prazo formal; no pano de fundo, a isenção PIS/Cofins do biodiesel completa hoje sua primeira sessão útil vencida sem qualquer sinal de renovação, e o noticiário abre uma frente nova e ainda opaca — um 'tarifaço' que o Radar Rural associa aos desafios da safra de soja brasileira, sem detalhe de conteúdo disponível neste briefing"
tags: [complexo, auto-claude, fim-de-semana, revisao-dados]
fontes:
  - CME CBOT (ZSU26 soja / ZMU26 farelo / ZLU26 óleo / HO=F heating oil) — sessão de 2026-07-31 (última sessão de pregão; mercado fechado em 2026-08-01, sábado), com os valores de fechamento, máxima, mínima e volume REVISADOS no dump de hoje frente ao que constava no dump usado por [[2026-07-31_leitura-complexo]] — ver corpo do texto e Honestidade para o detalhe completo de cada revisão
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, paridade BR) recalculados com os valores revisados de 2026-07-31, comparados à série 2026-07-27→2026-07-30 (não revisada nesta janela)
  - Índice de Sobra de Farelo e Índice de Suporte do Óleo — reimpressos com carimbo de 2026-08-01, valores inalterados (80/100 e 100/100) frente ao carimbo de 2026-07-31, confirmando que nenhum insumo estrutural novo entrou no cálculo durante o fim de semana
  - BCB PTAX — última leitura 2026-07-31 (USD/BRL 5,0773, EUR/BRL 5,849, Selic diária 0,052531% a.a.); sem publicação nova em 2026-08-01 (sábado, sem expediente bancário)
  - CEPEA/ESALQ Soja Paranaguá via NAG — última leitura 2026-07-31 (R$ 144,91/saca), sem atualização de fim de semana
  - CEPEA/ESALQ Soja Paraná interior via NAG — última leitura 2026-07-31 (R$ 137,27/saca)
  - NAG Físico BR — última leitura 2026-07-31 (farelo MT/IMEA R$ 1.675,10/ton; Rondonópolis R$ 1.700,00/ton; RS R$ 1.640,00/ton; prêmios export PGUA farelo +0,05 USD/sht e óleo +0,08 cts/lb, ambos inalterados há 29 dias corridos desde 2026-07-03)
  - CFTC COT Managed Money — corte de 2026-07-28, sem corte novo nesta janela (o próximo corte, referente a 2026-08-04, só é publicado por volta de 2026-08-07); usado apenas como contexto de posicionamento carregado da leitura anterior, não como dado novo
  - USDA Crop Progress — ainda no corte de 2026-07-26 (11% excelente + 52% boa + 7% ruim), sem publicação nova de fim de semana (cadência semanal normal, próximo corte esperado por volta de segunda-feira 2026-08-03)
  - USDA WASDE — ausente da janela deste briefing, agora 22 dias de atraso desde o último dado (2026-07-10)
  - NOPA — fila `release-nopa-2026-08-01`, `monthly_status` continua em 0,0 bool (paywall), mesma barreira desde meados de junho, agora ~7 semanas
  - ABIOVE projeções mensais — balanços ago-dez/2026 (farelo/óleo/soja), sem alteração
  - NOAA CPC ENSO — 2026-08-01 (El Niño Advisory, inalterado desde pelo menos 16/07/2026)
  - MPOB — 2026-08-01 (conteúdo idêntico de 3.439 caracteres, parser sem números extraídos, agora o 23º dia consecutivo nesse estado)
  - BCBA Argentina — 2026-08-01 (3ª sessão seguida acessível via scraper, ainda sem links de relatório detectados)
  - Notícias Agrícolas/Farm Progress/Canal Rural RSS — 2026-08-01 (160 itens lidos, 8 mantidos; manchete nova "Radar Rural debate reação do Brasil ao tarifaço e desafios da safra de soja", canalrural.com.br, sem corpo de texto extraído neste briefing — tratada com cautela, ver Honestidade)
  - INMET — previsão para 2026-08-02 nas praças monitoradas (Cascavel/PR, Maringá/PR, Passo Fundo/RS, Rio Verde/GO, Cuiabá/MT, Sinop/MT, Sorriso/MT, Lucas do Rio Verde/MT); entressafra da soja brasileira, sem relevância direta de preço nesta época do calendário agrícola
  - Forecasts estatísticos internos — geração de 2026-08-01, spot ref idêntico ao fechamento revisado de 2026-07-31 (viés "altista" nas três — ver Honestidade)
  - system/tributario_watch.toml (lido apenas como referência, não editado) — `atualizado_em` 2026-06-05, agora 57 dias sem atualização; evento `PISCOFINS-BIODIESEL-ISENCAO` com `vigencia_ate` 2026-07-31, hoje é o 1º dia corrido após o vencimento
  - Cruza com [[2026-07-31_leitura-complexo]] (leitura da sessão que está sendo revisada aqui) e [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (tese original do D+7, tratada abaixo)
status: ativa
vies: [bear-soja, neutral-farelo, bear-oleo_soja]
---

## Visão geral

O complexo soja é, mecanicamente, uma fábrica com uma única matéria-prima (a
soja em grão) e dois produtos de saída em proporção fixa por bushel esmagado:
o **farelo** (a fração proteica, ~78% da massa, vira ração animal) e o
**óleo degomado** (a fração de gordura, ~18-20% da massa, vira óleo de
cozinha e biodiesel). Quem decide o ritmo de esmagamento é a esmagadora,
olhando a **crush margin** (o valor de farelo + óleo por bushel, menos o
custo daquele bushel de soja, todos medidos na CBOT — Chicago Board of
Trade, a bolsa de referência mundial para esses três contratos) e o **oil
share** (a fração desse valor capturada especificamente pelo óleo). O
**ratio Far/Soj** (preço do farelo dividido pelo preço da soja, normalizado
pela conversão bushel↔short ton) mede o mesmo crush por outro ângulo: abaixo
de 80% o farelo está historicamente "abundante" frente à soja — zona bear —,
acima de 87% está "apertado" — zona bull —, e entre os dois fica a zona
neutra de mean-reversion.

**Hoje, 2026-08-01, é sábado — não houve pregão novo na CBOT, e não
haverá até a reabertura de segunda-feira, 2026-08-03.** Isso muda o tipo de
leitura que cabe fazer: não existe uma "sessão de hoje" para narrar. O que
existe, e que faz esta leitura ser mais do que uma repetição de
[[2026-07-31_leitura-complexo]], é que **o dump de dados de hoje trouxe os
valores de fechamento, máxima, mínima e volume da sessão de sexta-feira
(31/07) REVISADOS** frente ao que estava disponível ontem — um padrão já
documentado nas leituras anteriores (o fechamento "ao vivo" de qualquer
sessão costuma ser preliminar e é ajustado no dump do dia seguinte). A
revisão de hoje não é cosmética: ela muda a magnitude de praticamente todos
os indicadores derivados. O fechamento do óleo caiu de 67,47 (valor usado
ontem) para **67,26 cts/lb** — a distância abaixo do suporte técnico de
72,00 passa de -6,29% para **-6,58%**, a mais profunda já registrada nesta
série de leituras. O farelo, ao contrário, foi revisado PARA CIMA, de 314,50
para **314,90 USD/short ton** — um movimento pequeno, mas que, cruzado com o
óleo mais fraco, faz o **oil-meal spread** (óleo menos farelo, em USD por
bushel) comprimir muito mais do que se via ontem: de 0,5192 (30/07) para
**0,4708** (31/07 revisado), uma queda de **-9,32%** no dia — o TRIPLO da
compressão de -3,18% calculada ontem com o número ainda preliminar. A soja
também foi revisada, de 1.171,25 para **1.170,75 cts/bushel**, uma diferença
pequena (-0,04%) mas que empurra o fechamento para uma posição mais fraca
dentro do range do dia (44,3% do range, ante os 47,5% calculados ontem). O
**ratio Far/Soj**, recalculado com os três valores revisados, fecha em
**80,69%** — mais LONGE do piso de 80% do que os 80,55% vistos ontem, não
mais perto — o que reforça, com um dado mais "final" que o de ontem, a
leitura já dada de que o gatilho tático da revisão vencida
(`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`) segue
sem confirmação. **Leitura de uma linha:** o pivô do complexo hoje não é um
movimento de preço novo — é a confirmação, via revisão de dados, de que a
sessão de sexta foi, na versão final, ainda mais desfavorável ao óleo (tanto
em nível quanto em posicionamento dentro do próprio range) do que parecia
ontem, e ligeiramente mais neutra para o ratio Far/Soj do que se pensava;
maior convicção nesta leitura é a de que o óleo segue sendo, de forma cada
vez mais nítida a cada revisão, a perna mais fraca das três; confiança
moderada, dado que o fim de semana não traz nenhum fato novo de mercado para
testar essa leitura antes da reabertura de segunda-feira.

---

## Soja

**Viés: bear tático moderado — mesma direção de [[2026-07-31_leitura-complexo]],
levemente reforçada pela revisão do fechamento, que passou de 1.171,25 para
1.170,75 cts/bushel (CBOT, ticker ZSU26.CBT, sessão de 2026-07-31, a última
disponível).** Não há pregão novo para analisar hoje (mercado fechado,
sábado) — a análise abaixo trata do que a revisão de dados muda na leitura
da mesma sessão já coberta ontem, e do que fica em aberto até a reabertura
de segunda-feira.

### O que sustenta a tese

**A revisão do fechamento troca um dia tecnicamente "neutro" (0,00% sobre a
abertura) por um dia tecnicamente "levemente negativo" (-0,04%), sem alterar
máxima, mínima ou a leitura de resistência em 1.180,00.** Abertura 1.171,25
(inalterada), máxima 1.179,25 (inalterada, seguindo sem sequer tocar o nível
de 1.180,00 — o mesmo padrão de máximas decrescentes já descrito ontem,
1.181,25 em 30/07 → 1.179,25 em 31/07), mínima 1.164,00 (inalterada) e
fechamento revisado para **1.170,75**, 0,5 cts abaixo do valor usado ontem.
**Mecanismo:** com o fechamento mais baixo, a posição do fechamento dentro
do range do dia cai de 47,5% para **44,3%** ((1.170,75-1.164,00)÷
(1.179,25-1.164,00)) — ainda no terço médio, mas mais perto do terço
inferior do que se via com o número preliminar. Isso não muda
qualitativamente a leitura técnica (o nível de 1.180,00 segue sendo o ponto
mais relevante, não o fechamento em si), mas remove qualquer leitura
residual de "dia neutro" que o 0,00% original sugeria — na versão final dos
dados, a sessão de sexta foi, por pouco, uma sessão de leve fraqueza, não de
equilíbrio perfeito. O volume também foi revisado, de 21.839 para **32.247
contratos** (+47,7%) — um ajuste para cima relevante, que aproxima o volume
de sexta da faixa mais líquida vista em outras sessões desta janela, e reduz
a leitura de "convicção direcional baixa por volume fraco" que constava
ontem.

**O câmbio não tem publicação nova de fim de semana — a leitura de paridade
usa o mesmo par CBOT revisado × PTAX de sexta-feira.** USD/BRL PTAX fechou
em 5,0773 (BCB, 2026-07-31), sem dado novo em 2026-08-01 (sábado, sem
expediente bancário — a próxima PTAX só sai na reabertura). Com o CBOT
revisado para 1.170,75, a **paridade teórica em reais** recalcula para
**R$ 131,05/saca** (indicators, valor de 2026-07-31 já revisado: CBOT
1.170,75 cts × USD/BRL 5,0773), ligeiramente abaixo dos R$ 131,10/saca
calculados ontem com o CBOT ainda preliminar (-0,04%) — um ajuste pequeno,
mecânico, sem significado direcional novo por si só.

**O prêmio de exportação em Paranaguá, recalculado com a paridade revisada,
fica marginalmente maior do que o número reportado ontem, mas dentro da
mesma leitura de compressão inicial.** CEPEA/ESALQ Soja Paranaguá (via NAG)
segue em R$ 144,91/saca (última leitura, 2026-07-31, sem publicação de fim
de semana). Com a paridade revisada em R$ 131,05, o **prêmio de exportação
recalcula para +10,58%** ((144,91-131,05)÷131,05), ante os +10,53% já
computados ontem com a paridade preliminar (131,10) — uma diferença de
apenas +0,05 ponto percentual, mecânica pura da revisão do denominador, sem
qualquer leitura nova de tendência. A leitura de ontem — de que a pequena
compressão do prêmio observada entre 30/07 e 31/07 pode ser o primeiro sinal
de convergência física-papel, ou apenas ruído — segue sem poder ser testada
até a próxima publicação de CEPEA/ESALQ, esperada apenas na reabertura de
segunda-feira.

**A curva forward, recalculada com os valores revisados de sexta, mostra
outra pequena inversão de calendário no vencimento mais próximo — o oposto
do que a leitura preliminar de ontem havia descrito.** Agosto/26 (Q26)
1.172,00 → Setembro/26 (U26, spot) 1.170,75 → Novembro/26 (X26) 1.187,50 →
Janeiro/27 (F27) 1.201,25 → Março/27 (H27) 1.204,75 → Maio/27 (K27) 1.210,50.
Com os números revisados, Agosto volta a ficar **1,25 cts (+0,11%) ACIMA**
do spot de setembro — ontem, com o fechamento ainda preliminar, a leitura
havia sido de Agosto ligeiramente ABAIXO do spot (-0,04%), descrita como uma
"normalização parcial". A revisão de hoje desfaz essa leitura: a pequena
inversão técnica no vencimento mais próximo, documentada como recorrente nas
leituras anteriores, continua presente. É um efeito pequeno e, isoladamente,
não altera a tese — mas serve de lembrete de que qualquer leitura baseada no
fechamento "ao vivo" de uma sessão deve ser tratada como preliminar até o
dump do dia seguinte, e às vezes até o dump de dois dias depois.

**O COT de 28/07/2026 (CFTC) segue sendo o dado de posicionamento mais
recente — não há corte novo nesta janela, e o próximo (referente a
04/08/2026) só sai por volta de 07/08/2026.** A leitura de ontem continua
válida como pano de fundo: entre 21/07 e 28/07, o managed money net long em
soja subiu +22,97% (de 130.505 para 160.479 contratos, 15,73% do open
interest), majoritariamente via cobertura de posição vendida, numa semana em
que o preço ainda estava perto do topo recente (fechamento de 28/07:
1.204,75). Do fechamento de 28/07 até o fechamento revisado de hoje
(1.170,75), a soja caiu **-2,82%** (recalculado com o valor revisado de
sexta, ante os -2,78% calculados ontem) — uma fatia relevante da posição
comprada reforçada naquela semana específica segue, portanto, com prejuízo
de papel, um risco de liquidação forçada que esta leitura mantém como o
principal vetor de cauda baixista para a soja, sem nenhum dado novo neste
fim de semana para confirmá-lo ou descartá-lo.

**Os forecasts estatísticos internos**, gerados hoje (2026-08-01) com o
fechamento revisado como spot ref (1.170,75), seguem etiquetados "altista":
central 7d = 1.181,23 cts/bu (bandas 1.125,05-1.237,42); central 30d =
1.209,78 cts/bu (bandas 1.093,46-1.326,09) — praticamente idênticos aos
gerados ontem, como esperado já que o spot de referência mudou muito pouco.
Como sempre, esta leitura trata o modelo apenas como referência de banda
estatística, não como argumento de tese.

**A manchete nova do dia (Canal Rural, 01/08/2026, "Radar Rural debate
reação do Brasil ao tarifaço e desafios da safra de soja") menciona um
"tarifaço" associado à safra de soja, mas o briefing não trouxe corpo de
texto — apenas o título e o link.** Esta leitura não tem, a partir do que
está disponível, como determinar se o tarifaço mencionado é uma tarifa
americana sobre produtos brasileiros, uma medida brasileira, ou algo já
tratado em leituras anteriores sob outro nome — é tratado com cautela
explícita na seção Honestidade e listado como o item de verificação manual
mais urgente antes da reabertura de segunda-feira, dado o potencial de
impacto direto sobre o fluxo de exportação de soja brasileira caso confirme
alguma medida tarifária relevante.

### O que invalida / risco para a soja

- **Um fechamento consistente e sustentado acima de 1.180,00** na reabertura
  de segunda-feira desfaria a leitura de máximas decrescentes — a série de
  testes fracassados precisa, em algum momento, ser rompida por uma
  tentativa bem-sucedida.
- **O conteúdo do "tarifaço" citado na manchete de hoje, quando conhecido,**
  pode mudar materialmente esta leitura para qualquer direção — é o maior
  ponto cego desta janela.
- **O posicionamento especulativo esticado do COT de 28/07 (net long em
  15,73% do OI) se desmontar de forma desordenada** na reabertura, se o
  preço abrir em queda — risco de liquidação forçada inalterado desde
  ontem, ainda sem novo dado para calibrá-lo.
- **O câmbio abrir a semana em alta forte** — sem publicação de PTAX no fim
  de semana, não há como saber se a estabilização cambial de sexta teve
  continuidade.

### Leitura operacional — soja

Sem pregão novo, não há ação tática nova a tomar hoje — a leitura
operacional de ontem permanece válida como referência para a reabertura de
segunda: quem está vendido desde o rompimento de 29/07 pode considerar o
nível revisado de 1.179,25 (máxima de sexta) como referência de stop, um
pouco mais apertada do que a máxima de 1.181,25 de dois dias atrás. Quem
está comprado segue exposto ao risco de posicionamento identificado no COT
de 28/07 — um risco que não teve chance de se resolver (nem para pior, nem
para melhor) durante o fim de semana. A recomendação mais concreta desta
leitura para quem opera soja é de ordem prática: **checar o conteúdo do
"tarifaço" citado na manchete de hoje antes da abertura de segunda-feira**,
já que é o único elemento genuinamente novo (não uma revisão de dado já
conhecido) desta janela, e seu conteúdo real permanece desconhecido a partir
deste briefing.

---

## Farelo

**Viés: neutro tático dentro de uma tese estrutural bear ainda intacta — o
ratio Far/Soj, recalculado com os valores revisados da sessão de
2026-07-31, fecha em 80,69%, MAIS LONGE do piso de 80% do que os 80,55% já
reportados ontem, não mais perto.** Trata
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` (a fila
de hoje sinaliza novamente este item como revisão vencida — o checkpoint
formal de 18/06/2026 já passou há **44 dias**) e, indiretamente, o fato de
não haver COT novo nesta janela.

### O D+7 segue vencido — a revisão de hoje reforça, não enfraquece, esse veredito

A tese original ([[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]])
apostava que a compressão rápida do ratio em junho indicaria a zona
comprimida (<80%) "em 1-2 semanas". [[2026-07-31_leitura-complexo]] já havia
tratado o D+7 (18/06/2026) como formalmente encerrado sem confirmação, dado
que o ratio nunca havia fechado de forma robusta abaixo de 80% em seis
sessões observadas. **A revisão de hoje não muda esse veredito — ao
contrário, o reforça:** o valor final de 31/07 (80,69%) ficou mais distante
do piso do que o valor preliminar usado ontem (80,55%), o que significa que,
na versão "definitiva" dos dados disponível até agora, a sessão de sexta foi
ainda menos favorável à tese tática bear do ratio do que parecia no
fechamento ao vivo. Isso não muda a tese estrutural mais lenta (ABIOVE,
Índice de Sobra de Farelo — inalterada, ver abaixo), mas reforça a
recomendação já dada de tratar qualquer teste pontual do piso de 80% com
ceticismo, exigindo 2-3 fechamentos consecutivos e CONFIRMADOS (não apenas
prints ao vivo) antes de qualquer calibração de convicção tática. O próximo
marco formal de revisão da tese completa segue sendo o D+90 (2026-09-09,
daqui a 39 dias).

### O que sustenta a leitura de hoje

**A revisão do fechamento de farelo foi, isoladamente, positiva para o
preço (314,50 → 314,90, +0,13%) — mas irrelevante para a tese, porque o que
move o ratio é a comparação farelo-soja, e a soja também caiu na revisão.**
Farelo CBOT (ZMU26.CBT): abertura 317,50 (inalterada), máxima 319,90
(inalterada), mínima 312,30 (inalterada), fechamento revisado para
**314,90** — uma queda de **-0,82%** no dia (ante -0,94% com o valor
preliminar de ontem). A posição do fechamento dentro do range sobe de 29,3%
para **34,2%** ((314,90-312,30)÷(319,90-312,30)) — ainda no terço inferior,
mas menos fraco do que a leitura preliminar sugeria. O volume também foi
revisado para cima, de 27.533 para **30.297 contratos** (+10,0%).

**A crush margin, recalculada com os três valores revisados, cai ainda mais
do que o -5,01% já registrado ontem como a maior queda diária desta
janela.** Board Crush revisado: farelo 314,90 + óleo 67,26 − soja 1.170,75 =
**2,6189 USD/bushel**, ante 2,7667 (30/07, valor não revisado) — uma queda
de **-5,34%**, ligeiramente mais funda do que o -5,01% calculado ontem com
os números ainda preliminares de sexta. **Mecanismo:** a diferença vem
inteiramente do óleo, cujo fechamento foi revisado para baixo (68,22 usado
ontem como base de comparação não muda; o que muda é o valor de 31/07, de
67,47 para 67,26) — o óleo mais fraco na versão final dos dados puxa a
receita do crush (farelo+óleo) para baixo com mais força do que se sabia
ontem. Em termos absolutos, a margem revisada (2,6189) segue acima do nível
de alerta histórico citado em leituras passadas (<2,50 USD/bu), mas a folga
sobre esse nível — 0,1189 USD/bu — é a menor já registrada nesta série de
leituras, mais apertada ainda do que a folga já reduzida calculada ontem.

**O oil-meal spread é o indicador mais impactado pela revisão de hoje: a
compressão de sexta-feira, vista ontem como -3,18%, revisa para -9,32% —
quase o triplo.** Série revisada (27/07 a 31/07, últimos dois valores
recalculados): 0,7469 → 0,6468 → 0,5588 → 0,5192 (30/07, não revisado) →
**0,4708** (31/07, revisado, ante 0,5027 usado ontem). **Mecanismo da
revisão:** o farelo de sexta foi revisado para CIMA (314,50→314,90) enquanto
o óleo foi revisado para BAIXO (67,47→67,26) — os dois movimentos empurram o
spread na mesma direção (farelo relativamente mais forte, óleo relativamente
mais fraco), e a combinação dos dois efeitos, mesmo pequenos isoladamente,
produz uma compressão bem maior do que qualquer um deles sozinho explicaria.
**Esta é a quinta sessão seguida de compressão do oil-meal spread, e agora,
com o dado final, a mais forte desta janela em termos percentuais** — mais
uma confirmação, com dado mais confiável que o de ontem, de que o valor do
crush está migrando na direção "farelo relativamente mais forte / óleo mais
fraco" dentro da soma farelo+óleo.

**A curva forward de farelo, recalculada com os valores revisados, segue em
contango normal e completo — a forma da curva não muda com a revisão, só o
nível.** Agosto/26 (Q26) 312,20 → Setembro/26 (U26, spot) 314,90 →
Outubro/26 (V26) 316,60 → Dezembro/26 (Z26) 321,20 → Janeiro/27 (F27) 323,50
→ Março/27 (H27) 325,70 — todos os pontos revisados ligeiramente para cima
frente aos valores preliminares usados ontem (Q26 311,00→312,20; U26
314,50→314,90; V26 316,20→316,60; Z26 320,90→321,20; F27 323,20→323,50), mas
a forma — inteiramente crescente do vencimento mais próximo ao mais distante
— permanece idêntica. Consistente com o excedente estrutural de farelo no
Brasil (ABIOVE, ver abaixo) não gerar nenhum estresse físico de curtíssimo
prazo capaz de inverter o calendário.

**As praças físicas de farelo no Brasil (NAG) não têm publicação de fim de
semana — os últimos valores disponíveis seguem sendo os de sexta-feira,
31/07/2026, sem alteração.** Mato Grosso/IMEA em R$ 1.675,10/ton,
Rondonópolis/MT em R$ 1.700,00/ton (o salto de +3,03% documentado ontem
segue sem confirmação ou desmentido — ainda um único ponto de dado, ver
Honestidade) e RS em R$ 1.640,00/ton. O prêmio de exportação em Paranaguá
segue zerado em +0,05 USD/short ton, agora **29 dias corridos sem
variação** desde 03/07/2026 — o pilar mais persistente da tese estrutural.

**O Índice de Sobra de Farelo (ISF) foi reimpresso hoje com carimbo de
2026-08-01, permanecendo em 80/100 (4 de 5 condições estruturais)** —
idêntico ao carimbo de 31/07/2026, confirmando que nenhum insumo novo
entrou no cálculo durante o fim de semana (o índice não reage a
posicionamento ou preço intradiário, apenas a condições estruturais mais
lentas como as projeções ABIOVE, que também seguem sem alteração nesta
janela: exportação de farelo brasileiro caindo de 1.400 mil toneladas em
agosto/2026 para 700 mil toneladas em dezembro/2026, -50% em quatro meses).

### O que invalida / risco para o farelo

- **O ratio Far/Soj precisa fechar de forma robusta e repetida abaixo de
  80% — com dados JÁ REVISADOS, não apenas prints ao vivo — para validar
  qualquer tese tática bear.** A revisão de hoje é um lembrete concreto de
  por que essa exigência importa: o valor preliminar de ontem (80,55%)
  estava mais perto do piso do que o valor final (80,69%).
- **A posição comprada reforçada pelo COT de 28/07 (net long em 14,11% do
  OI) se desmontar de forma desordenada** na reabertura de segunda — risco
  inalterado desde ontem, sem dado novo para recalibrá-lo neste fim de
  semana.
- **O salto isolado de Rondonópolis (+3,03%, 30/07→31/07) se confirmar como
  tendência** quando o mercado físico voltar a publicar na segunda-feira —
  ainda um único ponto de dado.
- **O prêmio de exportação em Paranaguá sair de zero** depois de 29 dias
  parado.

### Leitura operacional — farelo

Sem sessão nova e sem publicação física de fim de semana, não há ação
tática adicional a tomar hoje. A revisão de dados reforça a recomendação já
dada ontem: tratar qualquer fechamento futuro perto do piso de 80% com
ceticismo até que ele sobreviva à revisão do dia seguinte — o padrão de
"quase romper, voltar" já dura mais de um mês, e agora há uma demonstração
concreta, dentro desta própria leitura, de que o número preliminar pode
mudar de lado da fronteira relevante de um dia para o outro. Para quem opera
o oil-meal spread, a compressão revisada (-9,32%, a mais forte desta janela)
é o sinal mais limpo e mais robusto — nesta leitura — de que a força
relativa do farelo dentro do crush está genuinamente aumentando, não apenas
um artefato de arredondamento.

---

## Óleo

**Viés: bear, e a revisão de dados de hoje aprofunda a leitura em vez de
suavizá-la — o fechamento de 2026-07-31 revisa de 67,47 para 67,26 cts/lb,
levando a distância abaixo do suporte técnico de 72,00 de -6,29% (valor
usado ontem) para -6,58% (valor final), a mais profunda já registrada nesta
série de leituras.** Trata `alerta-quebra_suporte-oleo_cbot-2026-07-31`
(fila de hoje repete o mesmo alerta, agora com o valor final e mais
negativo) e a ausência de COT novo nesta janela.

### O que sustenta a tese

**A revisão piora a leitura em dois eixos ao mesmo tempo: o nível do
fechamento cai, e a posição do fechamento dentro do range também cai.**
Abertura 68,22 (inalterada), máxima 68,23 (inalterada — a sessão nunca
testou o lado de cima de forma real, como já descrito ontem), mínima 66,66
(inalterada) e fechamento revisado para **67,26** (ante 67,47 usado ontem).
**Mecanismo:** a posição do fechamento dentro do range cai de 51,6%
(cálculo de ontem) para **38,2%** ((67,26-66,66)÷(68,23-66,66)) — uma
diferença de mais de 13 pontos percentuais, que muda a leitura de "um pouco
acima do meio do range" (ontem) para "claramente no terço inferior" (hoje,
com o dado final). Isso é uma correção material: a leitura de ontem já
descrevia a sessão como fraca, mas a versão revisada mostra que ela foi mais
fraca ainda do que o print ao vivo indicava. O volume também foi revisado
para baixo, de 65.946 para **48.109 contratos** (-27,1%) — ainda o maior
volume das três pernas do complexo nesta sessão, mas menos dominante do que
parecia ontem.

**A margem de biodiesel americana, recalculada com os valores revisados de
óleo e heating oil, é revisada para baixo — a melhora que a leitura de
ontem descrevia como "modesta" fica ainda mais modesta.** Custo do óleo:
**5,0445 USD/galão** (7,5 lb × 67,26 cts/lb), ante os 5,0603 calculados
ontem com o óleo ainda preliminar (-0,31% adicional). Receita: **7,2865
USD/galão** (heating oil 4,1215 + 1,5×RIN D4 2,11), MUITO menor que os
7,3586 calculados ontem — porque o heating oil, também revisado, caiu de
4,1936 (valor usado ontem, já uma vez revisado) para **4,1215** (-1,72%
adicional). Margem final: **1,4420 USD/galão**, ante os 1,4984 calculados
ontem — uma revisão para baixo de **-3,76%** na margem, que desfaz boa parte
da "recuperação parcial" que a leitura de ontem descrevia como um
contraponto fundamentalista modesto à queda do óleo. **Mecanismo:** tanto o
custo quanto a receita caíram na revisão, mas a receita caiu mais rápido
(-1,0% ante o valor de ontem) do que o custo (-0,3%) — o oposto da dinâmica
que havia melhorado a margem entre 30/07 e o print preliminar de 31/07.
**Para a tese do óleo, a revisão remove parte do contraponto altista que
constava ontem**: a margem de biodiesel americana, na versão final dos
dados, está mais fraca do que se pensava, não mais forte.

**O heating oil (HO=F) é, mais uma vez, a fonte de maior incerteza desta
janela — a revisão de hoje aprofunda tanto a queda de preço quanto o
colapso de volume já documentados nas últimas leituras.** O fechamento de
31/07 revisa de 4,1936 (valor já revisado usado ontem) para **4,1215 USD/
galão**, uma queda adicional de -1,72%. O volume revisa de 38.271 contratos
(valor que ontem parecia, pela primeira vez em várias sessões, "normal")
para **12.325 contratos** — uma queda de **-67,8%**, de volta à mesma ordem
de grandeza anômala documentada nas quatro sessões antes de ontem (278, 788,
70, 34 contratos). **Esta leitura trata isso como confirmação de que a
"normalização" descrita ontem foi ilusória**: o número de 38.271 contratos,
que parecia mais plausível, era ele próprio ainda preliminar e sujeito a
revisão — e a revisão foi na direção de voltar ao padrão anômalo, não de
confirmar a normalização. A cautela recomendada nas últimas cinco leituras
sobre qualquer conclusão de convicção baseada neste instrumento específico
permanece — e esta leitura a reforça, em vez de suavizá-la.

**O Índice de Suporte do Óleo (ISO) foi reimpresso hoje com carimbo de
2026-08-01, permanecendo em 100/100 (5 de 5 condições)** — idêntico ao
carimbo de 31/07/2026, confirmando que a tese estrutural (óleo dominando o
valor do crush) segue formalmente intacta apesar da revisão de preço mais
negativa. **O oil share, recalculado com os valores revisados, cai mais do
que se sabia ontem:** de 51,79% (30/07) para **51,64%** (31/07 revisado,
ante 51,75% calculado ontem) — uma queda de -0,15 ponto percentual no dia
final, quase quatro vezes maior que os -0,04pp calculados com o número
preliminar. Ainda a sexta sessão seguida de queda, mas agora num ritmo que,
com o dado revisado, não é mais "o mais lento desta sequência" como a
leitura de ontem descrevia — é comparável às quedas de sessões anteriores.

**A curva forward de óleo, recalculada, mantém a backwardation (prêmio de
entrega mais próxima sobre entrega mais distante), com amplitude
praticamente igual à calculada ontem.** Agosto/26 (Q26) 67,12 →
Setembro/26 (U26, spot) 67,26 → Outubro/26 (V26) 67,04 → Dezembro/26 (Z26)
66,90 → Janeiro/27 (F27) 66,85 → Março/27 (H27) 66,70. Do spot de setembro a
janeiro/27, uma queda de -0,61% — muito próxima dos -0,74% calculados ontem
com os valores preliminares, e ainda bem menor que os -1,96% e -2,27%
documentados em sessões anteriores desta janela. **A leitura de ontem
permanece válida:** o prêmio de entrega próxima está encolhendo, sugerindo
que a fraqueza de preço é mais uma história de papel (posicionamento, ver
COT) do que de um novo choque de aperto físico imediato — coerente com o
ISO seguir travado em 100/100.

**Não há COT novo nesta janela** — o corte de 28/07/2026 segue sendo a
fotografia mais recente de posicionamento, mostrando os fundos já
reduzindo o net long em óleo (-10,27%, para 16,60% do open interest) durante
a própria sequência de quebra técnica já em curso naquela semana, ao
contrário do padrão de "compra na fraqueza" visto em soja e farelo. Do
fechamento de 28/07/2026 (70,14) até o fechamento revisado de hoje (67,26),
o óleo caiu **-4,11%** (recalculado com o valor final, ante os -3,81%
calculados ontem) — a leitura de que o book especulativo em óleo tem,
proporcionalmente, menos posição comprada "presa" em prejuízo recente do
que soja e farelo permanece o argumento mais construtivo desta tese bear,
ainda sem dado novo para testá-lo.

### O que invalida / risco para o óleo

- **Um fechamento abaixo de 66,66 (mínima de sexta) na reabertura de
  segunda** confirmaria uma sexta sessão seguida de fraqueza técnica.
- **O heating oil precisa de volume estável e CONFIRMADO por pelo menos duas
  revisões seguidas** antes que esta leitura trate qualquer print de volume
  como indicativo de normalização do mecanismo de reporte — o episódio de
  hoje (38.271→12.325 na revisão) é evidência direta de por que esse padrão
  de cautela continua necessário.
- **A isenção PIS/Cofins do biodiesel seguir sem renovação após a
  reabertura de segunda-feira** (ver Lente fiscal) seria a confirmação mais
  concreta do catalisador fiscal já sinalizado.
- **O oil share continuar caindo** — a revisão de hoje já mostrou que o
  ritmo da queda pode ser maior do que os números preliminares sugerem.
- **A backwardation continuar comprimindo até desaparecer.**
- **MPOB seguir inacessível** (agora 23º dia consecutivo).

### Leitura operacional — óleo

A revisão de dados de hoje não muda a direção da tese bear-óleo — ela a
reforça em quase todos os eixos: suporte rompido mais fundo (-6,58%),
fechamento mais fraco dentro do range (38,2%, não 51,6%), margem de
biodiesel americana mais fraca (1,4420, não 1,4984), oil share caindo mais
rápido (-0,15pp, não -0,04pp) e volume de heating oil de volta ao padrão
anômalo depois de uma sessão em que parecia ter normalizado. Para quem está
comprado direcional, isso é um argumento adicional — não novo em direção,
mas mais forte em magnitude — para tratar a reabertura de segunda-feira com
cautela, especialmente se o preço abrir abaixo de 66,66. Para quem está
vendido ou tático short, a referência de entrada mais recente continua
sendo a mínima de sexta (66,66, inalterada pela revisão), com stop acima da
máxima do dia (68,23, também inalterada). Como não há pregão novo, esta
leitura não recomenda nenhuma ação adicional além de reavaliar o
dimensionamento de risco à luz da magnitude maior (não da direção) revelada
pela revisão de hoje.

---

## Spreads e crush — leitura de complexo

### Ratio Far/Soj: 80,69% (revisado) — mais longe do piso do que se sabia ontem, D+7 seguindo vencido há 44 dias

A revisão do fechamento de 31/07 empurra o ratio de 80,55% (valor
preliminar usado em [[2026-07-31_leitura-complexo]]) para **80,69%** —
mais distante do piso de 80%, não mais perto. Olhando a série (27/07:
80,09% → 28/07: 80,01% → 29/07: 81,10% → 30/07: 81,25% → 31/07: **80,69%**,
revisado), o indicador segue nunca tendo fechado de forma inequívoca abaixo
de 80% em nenhuma das seis sessões observadas, e o dado mais recente e mais
confiável (por já ter passado por uma revisão) reforça essa leitura. A fila
de hoje sinaliza `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
novamente como revisão vencida — 44 dias além do checkpoint formal de
18/06/2026. Esta leitura mantém o gatilho tático como não confirmado, sem
prejuízo da tese estrutural mais lenta (ABIOVE/ISF), que segue intacta. O
D+90 (2026-09-09) é o próximo marco formal, a 39 dias de hoje.

### Crush margin: 2,6189 USD/bu (revisado) — a maior queda diária desta janela fica ainda maior

A revisão aprofunda a queda diária de -5,01% (valor preliminar) para
**-5,34%** (2,7667→2,6189), continuando a ser a maior variação diária de
crush margin desta série de leituras. A folga sobre o nível de alerta
histórico (<2,50 USD/bu) cai para 0,1189 USD/bu — a mais apertada já
registrada nesta janela.

### Oil share: 51,64% (revisado) — sexta queda seguida, agora num ritmo maior do que se pensava

A revisão troca uma queda diária de -0,04pp (valor preliminar, "o mais
lento desta sequência") por uma queda de **-0,15pp** (51,79%→51,64%) — ainda
a sexta sessão seguida de queda, mas num ritmo comparável, não menor, ao das
sessões anteriores.

### Oil-meal spread: 0,4708 USD/bu (revisado) — a compressão mais forte desta janela, quase o triplo do que se via ontem

A revisão é a mais dramática desta leitura: de -3,18% (valor preliminar,
0,5192→0,5027) para **-9,32%** (0,5192→0,4708) — a quinta sessão seguida de
compressão, e agora, com o dado final, a maior queda percentual de um único
dia registrada nesta métrica em toda a janela observada.

### Margem de biodiesel: 1,4420 USD/gal (revisado) — a recuperação de ontem foi, em grande parte, um artefato do dado preliminar

A margem revisada (1,4420) fica **abaixo**, não acima, da margem de 30/07
(1,4579) — uma variação de -1,09%, revertendo a leitura de "+2,78%,
recuperação parcial" que constava em [[2026-07-31_leitura-complexo]] com os
dados ainda preliminares. Mecanismo: tanto o heating oil quanto o óleo
foram revisados para baixo, mas a receita (que depende do heating oil e do
RIN fixo) caiu proporcionalmente mais do que o custo.

### Sem COT novo, sem publicação de PTAX/CEPEA/NAG de fim de semana

Nenhum desses fluxos de dado publica aos sábados — a leitura de
posicionamento e de físico BR permanece exatamente a mesma descrita em
[[2026-07-31_leitura-complexo]], sem informação nova para testá-la.

### ISF em 80/100, ISO em 100/100 — reimpressos hoje, valores inalterados

Ambos os índices sintéticos foram recarimbados com a data de 2026-08-01,
mas mantêm exatamente os mesmos valores do carimbo de 31/07/2026 — confirma
que nenhum insumo estrutural novo (ABIOVE, condições de crush de mais
longo prazo) entrou no cálculo durante o fim de semana.

### O que os índices dizem juntos em 2026-08-01

ISF 80/100 + ISO 100/100 (ambos reimpressos, inalterados) + ratio Far/Soj
revisado para 80,69% (mais longe do piso do que se sabia ontem, D+7
formalmente vencido há 44 dias) + crush margin na maior queda diária desta
janela, agora -5,34% (revisado, ante -5,01%) + oil share na sexta queda
seguida, agora em ritmo comparável às anteriores (-0,15pp revisado, não
-0,04pp) + oil-meal spread na compressão mais forte desta janela em termos
percentuais (-9,32% revisado, quase o triplo do -3,18% preliminar) + margem
de biodiesel revisada para BAIXO da margem do dia anterior (-1,09%,
revertendo a leitura de recuperação de ontem) formam, juntos, um quadro
onde **a revisão de dados de sexta-feira não muda a direção de nenhuma
tese desta janela, mas aumenta a magnitude de quase todas as leituras bear
do crush — em especial no óleo e no oil-meal spread — e reduz a magnitude
do único contraponto altista técnico que constava ontem (a recuperação da
margem de biodiesel americana).** Combinado com a ausência completa de
dado novo de posicionamento, físico BR ou câmbio neste fim de semana, esta
leitura recomenda tratar a reabertura de segunda-feira como o primeiro
teste real de todas essas leituras revisadas contra preço ao vivo.

---

## Lente fiscal e regulatória BR

**Isenção PIS/Cofins biodiesel — venceu ontem, 31/07/2026 (sexta-feira),
sem qualquer sinalização pública de renovação nos dados disponíveis; hoje,
2026-08-01 (sábado), é o primeiro dia corrido após o vencimento, e o
silêncio de hoje tem um significado diferente do silêncio de ontem.**
(evento `PISCOFINS-BIODIESEL-ISENCAO`, `atualizado_em` 2026-06-05, agora
**57 dias sem atualização** do monitor). **Mecanismo e leitura:** ontem, o
vencimento acontecia no mesmo dia da consulta — o silêncio podia
simplesmente refletir o fato de o dia ainda estar em curso. Hoje, sábado,
o silêncio é estruturalmente menos informativo, não mais: repartições
públicas brasileiras não costumam publicar atos normativos aos sábados, e o
Diário Oficial da União tem edição extraordinária apenas em casos de
urgência. **Esta leitura trata o silêncio de hoje como neutro por
inatividade do calendário administrativo, não como sinal adicional de que a
isenção expirou sem renovação** — o teste real só vem com a reabertura do
expediente público, esperada na segunda-feira, 2026-08-03. Se a
segunda-feira também passar sem sinal de prorrogação, aí sim a leitura muda
de "neutro por inatividade" para "sinal concreto de que a isenção
efetivamente caducou" — um vetor bearish direto para a demanda de óleo de
soja como insumo do biodiesel doméstico brasileiro, distinto e adicional a
qualquer coisa que aconteça no CBOT.

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L) —
vigência formal venceu há 21 dias (`vigencia_ate` 11/07/2026), sem qualquer
atualização de status.** Enquanto o combustível fóssil segue formalmente
subsidiado (sem confirmação de que o subsídio de fato terminou), a
competitividade relativa do biodiesel dentro do mix B15 mandatório segue
pressionada.

**B16 — sem data, travado em B15**, sem mudança de status.

**MP 1.363/2026 (subsídio ao diesel fóssil, R$ 1,12/L) — em vigor até
31/12/2026**, sem alteração. Bearish estrutural persistente para a demanda
incremental de óleo de soja no mercado doméstico brasileiro.

**STJ REsp 2.165.276/2026 — crédito PIS/Cofins para esmagadoras**, sem
alteração. Bullish para soja/óleo (alívio de custo de entrada para
biodiesel), independente da mecânica tática de curto prazo do crush.

**Vetores dos EUA e Indonésia, sem mudança de status desde 2026-06-05:**
EPA-RFS-2026-2027 (volumes recordes de biocombustível, sustentando o RIN
D4 usado na margem de biodiesel, fixo em 2,11 USD/RIN); 45Z-CLEAN-FUEL
(regra que favoreceria óleo de soja doméstico americano); DANANTARA-INDONESIA
(centralização estatal da exportação de palma, plena em 01/09/2026, agora a
31 dias); INDONESIA-B50 (provável B45 em 2026, B50 pleno só 2027-28);
INDONESIA-LEVY-PMK9 (imposto de exportação de CPO até 12,5%, encarecendo
palma). Conjunto estruturalmente bullish para óleo de soja via substituição
de palma, mas inverificável pelo lado de mercado (MPOB inacessível há 23
dias, ver Honestidade).

**O monitor tributário como um todo está há 57 dias sem qualquer
atualização.** Prioridade máxima de manutenção do sistema, independentemente
da leitura de preço de hoje — e ainda mais relevante neste fim de semana
específico, dado o vencimento da isenção PIS/Cofins ocorrer exatamente
dentro dessa janela de inatividade do monitor.

**Nota de cautela sobre a manchete do dia:** a notícia "Radar Rural debate
reação do Brasil ao tarifaço e desafios da safra de soja" (Canal Rural,
01/08/2026) pode ser relevante para esta lente fiscal/regulatória — um
"tarifaço" pode ser tanto uma medida americana sobre produtos brasileiros
quanto uma resposta tarifária brasileira — mas, sem corpo de texto
disponível neste briefing, esta leitura não incorpora nenhum conteúdo
específico dela à análise. Tratada apenas como item de verificação manual
prioritário (ver Honestidade e Riscos).

---

## Riscos e eventos próximos

**A reabertura da CBOT na segunda-feira, 2026-08-03, é o primeiro teste real
de todas as leituras revisadas nesta análise** — em especial a distância
mais funda do óleo abaixo do suporte de 72,00 (-6,58%) e a compressão mais
forte já vista do oil-meal spread (-9,32%).

**A isenção PIS/Cofins do biodiesel segue sem sinal de renovação; a
reabertura de expediente público de segunda-feira é o primeiro momento em
que o silêncio deixa de ser explicável por inatividade de calendário** — o
item de verificação manual mais urgente desta janela.

**O conteúdo real da manchete sobre o "tarifaço" (Canal Rural, 01/08/2026)
é desconhecido a partir deste briefing** — segundo item de verificação
manual prioritário, dado o potencial de impacto direto sobre o fluxo de
exportação de soja brasileira.

**O próximo corte do COT (referente a 04/08/2026) só é publicado por volta
de 07/08/2026** — até lá, a divergência de posicionamento entre pernas
identificada no corte de 28/07 (soja e farelo mais comprados e mais
vulneráveis; óleo já reduzindo exposição) segue sem novo dado para
confirmar se está se resolvendo por desmonte, recuperação de preço, ou
ambos.

**O ratio Far/Soj está, com o dado revisado, mais longe do piso de 80% do
que se pensava — mas o D+7 formal segue vencido há 44 dias sem confirmação**
— monitorar o D+90 (2026-09-09) como próximo marco formal.

**O USDA Crop Progress deve trazer corte novo por volta de segunda-feira,
2026-08-03** (cadência semanal normal desde o último corte de 26/07).

**NOPA — fila `release-nopa-2026-08-01` sinaliza um novo "release", mas o
dado segue inacessível** (`monthly_status` em 0,0 bool), agora ~7 semanas
sem alternativa de dado primário sobre o crush americano.

**MPOB — sem números de palma extraídos há 23 dias consecutivos.**

**O WASDE segue fora da janela deste briefing, agora 22 dias de atraso**
desde o último dado (10/07/2026).

---

## Honestidade

O que não foi possível validar neste briefing de 2026-08-01, e os pontos
onde a confiança é baixa ou há lacunas relevantes:

**1. Não houve pregão novo hoje — 2026-08-01 é sábado, mercado fechado.**
Toda a análise de preço desta leitura trata da mesma sessão de 31/07/2026
já coberta em [[2026-07-31_leitura-complexo]], agora com valores revisados.
Esta leitura não inventa nem estima nenhum movimento de preço para hoje —
onde a leitura de ontem falava de "a sessão de hoje", esta leitura fala
explicitamente de "a sessão de sexta, revisada".

**2. A manchete "Radar Rural debate reação do Brasil ao tarifaço e desafios
da safra de soja" (Canal Rural, 01/08/2026) foi citada nesta leitura apenas
pelo título — o briefing não trouxe corpo de texto, e esta análise não tem
como saber o que o tarifaço mencionado envolve, sua origem (EUA, Brasil, ou
terceiro país) ou sua magnitude.** Tratado como o item de verificação
manual de maior prioridade desta janela, mas nenhum conteúdo além do título
foi incorporado à leitura de tese.

**3. As revisões de dados documentadas nesta leitura (CBOT OHLCV + todos os
indicadores derivados da sessão de 31/07) seguem o mesmo padrão já
registrado em leituras anteriores (heating oil revisado em até ~292x em
episódios passados) — não há garantia de que os valores de hoje, tratados
aqui como "revisados" e mais confiáveis que os de ontem, não sejam eles
próprios revisados de novo no próximo dump.** Esta leitura trata a versão
de hoje como a mais recente disponível, não como definitiva.

**4. O heating oil (HO=F) teve, na revisão de hoje, tanto o preço quanto o
volume revisados para baixo de forma expressiva (fechamento -1,72%, volume
-67,8%)** — a leitura de ontem, que descrevia o volume de sexta como
"o mais normal desta janela", não se sustentou na revisão. Esta análise
trata o instrumento como não confiável para leitura de convicção até que
um valor sobreviva a pelo menos duas revisões consecutivas sem alteração
material.

**5. O salto físico de farelo em Rondonópolis/MT (+3,03% em 31/07, para R$
1.700,00/ton) segue sem confirmação ou desmentido** — não há publicação de
fim de semana para testar se o movimento teve continuidade ou foi
revertido.

**6. O USDA Crop Progress permanece no corte de 26/07/2026 (11%/52%/7%)**,
dentro da cadência semanal normal; o próximo corte é esperado por volta de
segunda-feira.

**7. O WASDE permanece completamente fora da janela deste briefing** —
agora 22 dias de atraso desde o último dado (10/07/2026).

**8. NOPA (fila `release-nopa-2026-08-01`) segue com `monthly_status` em
0,0 bool** — mesma barreira de assinatura paga, ~7 semanas sem alternativa
de dado primário.

**9. Palma malaia (MPOB) segue sem números extraídos**, mesmo conteúdo
exato de 3.439 caracteres, agora 23º dia consecutivo.

**10. O COT (CFTC) de 28/07/2026 segue sendo o dado de posicionamento mais
recente — nenhum corte novo nesta janela.** A leitura de risco de
liquidação forçada em soja/farelo, e de exposição comprada relativamente
mais "aliviada" em óleo, é herdada integralmente de
[[2026-07-31_leitura-complexo]], sem possibilidade de teste adicional até
07/08/2026.

**11. Percentis históricos de COT não calculados** — mesma limitação
documentada nas leituras anteriores.

**12. Clima INMET (BR) não foi usado como driver de preço** — julho/agosto
é entressafra da soja brasileira, sem relevância direta neste momento do
calendário agrícola.

**13. BCBA Argentina — 3ª sessão seguida acessível via scraper (30/07,
31/07, 01/08), ainda sem relatórios de esmagamento/exportação extraíveis.**

**14. O monitor tributário (`system/tributario_watch.toml`) está há 57 dias
sem atualização** — o vencimento da isenção PIS/Cofins caiu exatamente
dentro dessa janela de inatividade do monitor, o que esta leitura já
sinalizou como prioridade máxima de manutenção do sistema em leituras
anteriores.

**15. Os forecasts estatísticos internos (2026-08-01) mantiveram o rótulo
"altista" para as três commodities** — gerados a partir do fechamento
revisado, mas sem incorporar nenhuma das leituras qualitativas desta
análise (revisões, ausência de pregão, tarifaço não detalhado).

*Nenhum número foi inventado ou estimado além do que consta no briefing de
2026-08-01 e nos insights anteriores referenciados. A contribuição central
desta leitura foi (1) identificar e decompor, item por item, as revisões de
dados da sessão de 31/07/2026 frente aos valores preliminares usados em
[[2026-07-31_leitura-complexo]] — em especial a compressão do oil-meal
spread revisando de -3,18% para -9,32% e a margem de biodiesel revertendo
de uma "recuperação" de +2,78% para uma queda de -1,09% —, tratando essas
revisões como o conteúdo analítico central de um dia sem pregão novo; (2)
recalibrar a distância do óleo abaixo do suporte técnico de 72,00 para
-6,58% (a mais funda desta janela) e a posição do fechamento do óleo dentro
do range do dia para 38,2% (ante os 51,6% calculados com o dado
preliminar); (3) tratar os três itens da fila de julgamento de hoje —
`alerta-quebra_suporte-oleo_cbot-2026-07-31`,
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` e
`release-nopa-2026-08-01` — no contexto específico de um fim de semana sem
dado novo de mercado; (4) recalibrar o significado do silêncio sobre a
isenção PIS/Cofins do biodiesel, distinguindo entre "silêncio por
inatividade de calendário" (hoje, sábado) e "silêncio como sinal" (a partir
de segunda-feira, se persistir); e (5) sinalizar explicitamente, sem
inventar conteúdo, a manchete nova sobre o "tarifaço" como o maior ponto
cego desta janela e o item de verificação manual mais urgente antes da
reabertura de segunda-feira.*
