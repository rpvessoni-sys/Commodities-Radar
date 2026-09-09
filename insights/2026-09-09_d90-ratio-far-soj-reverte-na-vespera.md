---
data: 2026-09-09
titulo: "Revisão D+90 da tese do ratio Far/Soj: a abundância de farelo prevista em 11/06 não foi invalidada — o primeiro preço fresco em quatro dias devolveu o ratio para 78,28%, mais longe de 80% do que estava havia duas semanas"
tags: [farelo, ratio-far-soj, spread, revisao, auto-claude]
fontes:
  - Tese original — [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (11/06/2026): ratio Far/Soj 81,4% comprimindo de 83,3% em 4 pregões, prêmio export de farelo em Paranaguá zerado (+0,05 USD/sht, NAG 10/06), crush margin em recorde de US$ 3,78/bushel com oil share 55,4% — viés baixista no farelo (`bear-farelo`), com revisões programadas em D+7 (18/06), D+90 (09/09) e D+180 (08/12)
  - CME CBOT (ZMV26 farelo / ZSX26 soja) — 2026-09-08: farelo fechamento 343,60 USD/short ton (-1,32% vs 04/09), soja fechamento 1.316,75 USD cts/bushel (+0,53% vs 04/09) — primeiro pregão desde a pausa de feriado de 04-07/09
  - Indicadores sintéticos internos — far_soj_ratio_pct 2026-09-08: 78,28% (indicators), ante 79,76% em 04/09, 79,45% em 03/09, 78,51% em 02/09; ISF (índice de sobra de farelo) e ISO (índice de suporte do óleo) 2026-09-08: 80/100 e 100/100, revertendo cinco sessões (03-07/09) travadas em 60/100 e 80/100
  - CFTC COT Managed Money — corte 2026-09-01: net long farelo 157.179 contratos (+63,83% vs 25/08), net long óleo 99.823 contratos (+17,28% vs 25/08) — 8 dias corridos de defasagem frente a hoje, sem confirmação de como os fundos reagiram à reversão de preço de 08/09
  - NAG Físico BR — 2026-09-08: farelo MT/IMEA R$ 1.875,45/ton, prêmio export Paranaguá +0,12 USD/short ton, ambos congelados desde pelo menos 27/08 (12 dias corridos), sem reação visível à queda do farelo em Chicago
  - ABIOVE projeções mensais (sem revisão nesta janela): produção de farelo recuando de 2.129 mil t (set/26) para 1.659 mil t (dez/26), exportação de farelo recuando de 1.100 para 700 mil t no mesmo período
  - Fila de julgamento 2026-09-08 — `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` (🔴 vencida) e `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90` (🟡 vencendo em 1 dia, ou seja hoje)
  - Cruza com [[2026-09-09_leitura-complexo]] (leitura diária de hoje, que trata a mesma reversão em nível de complexo) e com [[2026-09-08_leitura-complexo]] (leitura de ontem, que documentou a aproximação de 79,76% na véspera)
status: ativa
vies: [bear-farelo]
---

## Por que este insight existe separado da leitura diária

A tese aberta em 11/06/2026
([[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]) previa três marcos de
revisão: D+7 (18/06), D+90 (09/09) e D+180 (08/12). Hoje, 09/09/2026, é a data exata do
marco D+90 — e, por coincidência de calendário, é também o primeiro dia em que a leitura
diária dispõe de um preço fresco (o fechamento de 08/09) depois de quatro dias corridos
sem pregão. Essa coincidência dá a este marco um peso maior do que o de uma revisão
qualquer: a decisão sobre se a tese de 90 dias se confirmou ou não está sendo tomada
exatamente no primeiro momento em que o mercado teve chance de reagir depois de uma pausa
prolongada. Por isso este insight aprofunda o veredito em um documento próprio, além de
tratá-lo na leitura-complexo do dia.

## O que a tese original previa

Em 11/06/2026, com o ratio Far/Soj em 81,4% (comprimindo rapidamente de 83,3% quatro
pregões antes), o prêmio de exportação do farelo em Paranaguá zerado (+0,05 USD/short
ton, NAG 10/06 — abaixo do custo de colocar o farelo no mercado externo, o que empurra
toda a oferta excedente para o mercado doméstico) e o crush margin em recorde histórico
de US$ 3,78/bushel com oil share de 55,4% (a esmagadora processando a pleno vapor para
capturar o valor do óleo, e "aceitando" vender farelo barato como subproduto), a leitura
original concluiu: **o ratio deve continuar comprimindo, cruzando para a zona abaixo de
80% ("abundante") em 1-2 semanas, com viés baixista no farelo (`bear-farelo`)**. O
mecanismo central é simples de entender: quando a esmagadora tem um motivo forte para
processar soja (o óleo pagando bem a conta), ela produz farelo como consequência, não
como objetivo — e o excesso de farelo gerado por essa lógica precisa achar comprador a
qualquer preço, o que empurra o preço relativo do farelo para baixo frente à soja. Isso é
exatamente o que o ratio Far/Soj mede.

## O que aconteceu nos 90 dias, e o que o preço fresco de hoje confirma

Ao longo dos 90 dias corridos entre 11/06 e 09/09, o ratio Far/Soj passou a maior parte
do tempo abaixo de 80% — a zona que a própria definição do indicador chama de
"abundante" (indicators: "<80 abundante, >=87 apertado"). As leituras diárias mais
recentes (02 a 07/09) registraram uma recuperação de curto prazo: o ratio subiu de 78,51%
(02/09) para 79,76% (04/09), a **0,24 ponto percentual** de cruzar o patamar de 80% pela
primeira vez desde o início da tese — e, junto com essa recuperação, os índices sintéticos
ISF (índice de sobra de farelo) e ISO (índice de suporte do óleo) haviam recuado de 80/100
para 60/100 e ficado parados nesse nível por cinco carimbos de data seguidos (03 a
07/09), um padrão que a leitura de ontem descreveu como "o quadro mais favorável à
convergência desde a abertura da tese".

O primeiro fechamento fresco desde então — a sessão de 08/09/2026, a primeira negociada
depois da pausa de feriado de 04-07/09 — respondeu a essa expectativa de forma direta e
na direção contrária. O farelo caiu -1,32% (343,60 USD/short ton, CME CBOT), a soja subiu
+0,53% (1.316,75 USD cts/bushel), e o ratio recuou para **78,28%** (indicators, 08/09) —
não apenas deixando de cruzar 80%, mas se afastando dele mais do que em qualquer ponto
das duas semanas anteriores: a distância até 80%, que era de 0,24 p.p. na sexta-feira,
reabriu para **1,72 ponto percentual**. Ao mesmo tempo, o ISF saltou de volta para 80/100
("forte pressão baixista no farelo", 4 de 5 condições atendidas) e o ISO para 100/100
("óleo domina o crush", 5 de 5 condições) — o nível máximo da escala, mais alto até do que
o patamar 80/100 registrado no início de setembro.

## O veredito

Tomando os 90 dias corridos como um todo, e não apenas o dia isolado da revisão: **a
tese original de 11/06/2026 — abundância estrutural de farelo, ratio comprimido, viés
baixista — não foi invalidada**. O ratio Far/Soj esteve, na esmagadora maioria das
sessões cobertas pelas leituras diárias desde então, abaixo do patamar de 80%, e a única
aproximação real desse patamar (79,76% em 04/09) durou poucas sessões e foi revertida no
exato momento em que o mercado teve a primeira chance real de reagir a dados novos. O
mecanismo original — crush margin favorecendo o processamento de soja pelo lado do óleo,
com o farelo sobrando como subproduto — segue coerente com o que se observa hoje: o oil
share voltou a 50,55% (indicators, 08/09), de volta acima de 50% depois de ter caído
para 49,73% na sexta-feira, e o oil-meal spread virou de -0,0825 para **+0,1672**
USD/bushel na mesma sessão — o óleo, de novo, valendo mais do que o farelo dentro da conta
do crush, o núcleo do argumento de junho.

Isso não significa que a tese tenha se confirmado com margem de segurança confortável.
A aproximação de 79,76% mostrou que o mercado, por um momento, testou a hipótese de uma
normalização mais rápida do que a prevista — e essa hipótese só foi desfeita quando o
preço voltou a negociar. Um trader que tivesse fechado a posição bear-farelo na sexta-
feira, avaliando a aproximação de 80% como sinal de que a tese havia se esgotado, teria
saído antes do veredito favorável de hoje. A lição operacional é que a proximidade de um
nível técnico, sem confirmação de fechamento além dele, não é o mesmo que o nível ter
sido cruzado — e a ausência de pregão por quatro dias corridos escondeu, até hoje, se a
recuperação tinha substância ou era apenas o resultado de um mercado sem negociação
reagindo a notícias antigas.

## O que ainda pesa contra o veredito, e não deve ser ignorado

- **O COT de 01/09 (8 dias de defasagem) mostrou os fundos ampliando fortemente a
  posição comprada em farelo na semana anterior à queda de hoje** — net long saltando
  +63,83% (95.953 → 157.179 contratos, CFTC COT), com desmonte de posição vendida
  (-37,60%) e crescimento de open interest (+6,68%), sinais de convicção nova entrando
  no mercado, não apenas rotação. Se essa convicção persistiu além de 01/09, a queda de
  hoje pode ser uma correção dentro de uma tendência de fundo que os dados de
  posicionamento ainda não capturam. O próximo corte (posições de 08/09) só sai por
  volta de 11/09 — depois da data desta revisão.
- **O físico brasileiro de farelo não mostrou nenhuma reação** à queda de Chicago:
  MT/IMEA, Rondonópolis e a média do RS seguem exatamente nos mesmos níveis desde 04/09
  (NAG, 08/09), e o prêmio de exportação em Paranaguá está congelado há 12 dias corridos.
  Isso pode significar defasagem normal de repasse, ou pode significar que o mercado
  físico doméstico não compartilha da leitura bearish que a CBOT sinalizou hoje.
- **O volume da sessão de 08/09 (25.777 contratos em farelo, CME CBOT) é um dado de
  participação a monitorar** — não há, nesta janela do dump, o número exato de volume da
  última sessão plena antes da pausa para comparação direta, o que limita quanto se pode
  inferir sobre a força relativa deste pregão de reabertura.
- **Os fundamentos de médio prazo (ABIOVE) continuam trabalhando na direção oposta ao
  veredito de curto prazo**: a produção de farelo projetada recua de 2.129 mil toneladas
  (set/26) para 1.659 mil toneladas (dez/26), e a exportação de 1.100 para 700 mil
  toneladas no mesmo horizonte — uma desaceleração da oferta doméstica de farelo que, se
  confirmada, tende a apoiar uma recuperação futura do ratio, mesmo que o veredito de
  hoje, no horizonte de dias, tenha sido desfavorável a essa recuperação.

## Encaminhamento

Este insight não substitui nem revisa formalmente o arquivo original
([[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]), que permanece com seu
próprio calendário de revisões (`status: revisada`, próxima checagem D+180 em
2026-12-08). O que este documento registra é o veredito factual do marco D+90 na data em
que ele vencia: a tese de abundância de farelo/viés baixista segue de pé, reforçada pelo
primeiro dado de preço fresco disponível exatamente no dia da revisão, mas com a ressalva
de que a aproximação de 80% observada em setembro mostra que a margem de confiança não é
tão ampla quanto os índices sintéticos, isoladamente, sugeriam durante os cinco dias sem
pregão. Para o trader que opera os dois lados: hoje é o primeiro dia, desde o início de
setembro, em que abrir ou reforçar uma posição bear-farelo (ou vender o spread Far/Soj)
tem preço, ratio e estrutura de crush alinhados na mesma direção — mas ainda sem
confirmação de COT fresco nem de reação do físico brasileiro.
