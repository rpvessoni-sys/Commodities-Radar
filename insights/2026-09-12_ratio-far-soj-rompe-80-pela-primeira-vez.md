---
data: 2026-09-12
titulo: "O gatilho de invalidação da tese de abundância de farelo, aberta em 11/06/2026 e reafirmada no veredito D+90 de 09/09, finalmente ocorreu: o ratio Far/Soj fechou em 80,32% em 11/09 — o primeiro fechamento acima de 80% em 92 dias corridos de tese — mas sem confirmação de COT contemporâneo nem de reação do físico brasileiro, e com o WASDE de setembro revisando a oferta exportável de farelo argentino para cima"
tags: [farelo, ratio-far-soj, spread, revisao, auto-claude]
fontes:
  - Tese original — [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (11/06/2026): ratio Far/Soj 81,4% comprimindo de 83,3% em 4 pregões, prêmio export de farelo em Paranaguá zerado (+0,05 USD/sht, NAG 10/06), crush margin em recorde de US$ 3,78/bushel com oil share 55,4% — viés baixista no farelo (`bear-farelo`), com revisões programadas em D+7 (18/06), D+90 (09/09) e D+180 (08/12), e com o gatilho de invalidação definido explicitamente como "um fechamento do ratio acima de 80% pela primeira vez desde a abertura da tese"
  - Veredito D+90 — [[2026-09-09_d90-ratio-far-soj-reverte-na-vespera]] (09/09/2026): concluiu que a tese "não foi invalidada" após 90 dias corridos, com o ratio tendo oscilado entre 78,25% e 79,76% sem nunca fechar acima de 80% — e reafirmou o mesmo gatilho de invalidação para revisões futuras
  - CME CBOT — sessão de 2026-09-11: farelo (ZMV26) fechamento 347,80 USD/short ton (-0,80% vs 10/09), soja (ZSX26) fechamento 1.299,00 USD cts/bushel (-2,50% vs 10/09), óleo (ZLV26) fechamento 69,11 USD cts/lb (-3,22% vs 10/09) — quarto pregão pleno desde a reabertura de 08/09, primeira sessão em que os três produtos caem juntos, com o farelo caindo proporcionalmente muito menos que os outros dois
  - Indicadores sintéticos internos — far_soj_ratio_pct 2026-09-11: **80,32%** (indicators), ante 78,95% em 10/09, 79,06% em 09/09, 78,25% em 08/09 — o primeiro fechamento acima de 80% desde a abertura da tese em 11/06/2026 (92 dias corridos); ISF (índice de sobra de farelo) caiu de 80/100 para **60/100** e ISO (índice de suporte do óleo) caiu de 100/100 para **80/100**, ambos pela primeira vez em quatro sessões; oil share caiu de 50,46% para **49,84%**, primeira leitura abaixo de 50% de toda a janela pós-reabertura; oil-meal spread virou de +0,1419 para **-0,0495** USD/bushel, primeira leitura negativa da janela
  - CFTC COT Managed Money — corte de 2026-09-08 (a primeira atualização desde 01/09): net long farelo 157.689 contratos (+0,32% vs 01/09), mas com long caindo -2,86% (178.183→173.079) e short caindo -26,73% (21.004→15.390) — cobertura de posição vendida, não convicção compradora nova; net long óleo 91.711 contratos (-8,13% vs 01/09), com short subindo +17,14%; net long soja 257.258 contratos (+9,51% vs 01/09), com long subindo +8,42% — dinheiro novo. Este corte é de três dias corridos antes da sessão de 11/09 que produziu o cruzamento de 80%, portanto não pode confirmar nem contradizer diretamente esse evento específico
  - USDA WASDE, edição de setembro/2026 (release de 11/09, tratando `release-usda_wasde-2026-09-11`) — farelo Argentina 2026/27: exportação revisada de 2,89 para **2,99 milhões de toneladas** (+3,46%, edição de agosto vs setembro), produção mantida em 33,11 milhões de toneladas; farelo Brasil 2026/27: produção, exportação e esmagamento domésticos praticamente inalterados (8,0 / 0,2 / 7,1 milhões de toneladas). Esta janela do dump não trouxe tabelas de soja em grão nem de óleo de soja do WASDE de setembro
  - ABIOVE projeções mensais (sem revisão nesta janela): produção de farelo recuando de 2.129 mil t (set/26) para 1.659 mil t (dez/26), exportação de farelo recuando de 1.100 para 700 mil t no mesmo período — trajetória de alívio de oferta doméstica de farelo no próximo trimestre
  - NAG Físico BR — última leitura ainda 2026-09-09: farelo MT/IMEA R$ 1.875,45/ton (congelado desde 04/09), prêmio export Paranaguá +0,12 USD/short ton (congelado desde 27/08, 16 dias corridos até hoje) — nenhuma reação visível do físico a qualquer movimento de Chicago desde então
  - Fila de julgamento 2026-09-11 — `ratio-zona-2026-09-11` (🟡, "Ratio Far/Soj entrou na zona 'neutro' (80,3%, era 'comprimido' 79,0%)"), `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` (🔴, recorrente) e `-D+90` (🔴, recorrente)
  - Cruza com [[2026-09-12_leitura-complexo]] (leitura diária de hoje, que trata a mesma reversão em nível de complexo) e com [[2026-09-11_leitura-complexo]] (leitura de ontem, que documentou o terceiro pregão com os três produtos subindo juntos)
status: ativa
vies: [neutral-farelo]
---

## Por que este insight existe separado da leitura diária

A tese aberta em 11/06/2026
([[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]) definiu um gatilho de
invalidação explícito e binário: "um fechamento do ratio Far/Soj acima de 80% pela
primeira vez desde a abertura da tese". Esse gatilho sobreviveu intacto por 92 dias
corridos — inclusive resistindo a duas aproximações reais (79,76% em 04/09 e 79,08%/
79,06% em 09/09, ambas revertidas na sessão seguinte) — e foi reafirmado, sem
modificação, no veredito da revisão D+90
([[2026-09-09_d90-ratio-far-soj-reverte-na-vespera]]) publicado há apenas dois dias. Hoje,
11/09/2026, esse gatilho binário efetivamente disparou: o ratio fechou em **80,32%**. Um
evento definido com tanta clareza, ocorrendo tão pouco tempo depois do veredito que o
reafirmou, merece um documento próprio que trate a pergunta com todo o peso que ela exige
— não apenas mais um parágrafo dentro da leitura diária — sem deixar de reconhecer, com
honestidade, que um único fechamento acima de um nível não é, por si só, prova de que a
tese de fundo mudou.

## O que a tese original previa, e o que o veredito D+90 já havia dito

Em 11/06/2026, com o ratio em 81,4% comprimindo rapidamente, prêmio export de farelo
zerado e crush margin em recorde histórico com oil share de 55,4%, a leitura original
concluiu que a esmagadora tinha um motivo forte para processar soja pelo lado do óleo, e
que o farelo resultante — produzido como consequência, não como objetivo — precisaria
achar comprador a qualquer preço, empurrando o ratio para baixo de 80% em 1-2 semanas.
Isso se confirmou: ao longo dos 92 dias entre 11/06 e 09/09, o ratio passou a esmagadora
maioria do tempo abaixo de 80%, e o veredito D+90 concluiu, dois dias atrás, que a tese
"não foi invalidada", com a ressalva explícita de que "a aproximação de 79,76% mostrou
que o mercado, por um momento, testou a hipótese de uma normalização mais rápida do que a
prevista" e que "a margem de confiança não é tão ampla quanto os índices sintéticos,
isoladamente, sugeriam".

## O que mudou entre o veredito de 09/09 e hoje

Depois do veredito D+90, o ratio seguiu o padrão de oscilação dentro da zona de
abundância por mais duas sessões: 78,95% em 10/09 (recuando de 79,06% em 09/09, quando a
soja subiu mais rápido que o farelo em um dia de alta conjunta). A sessão de hoje,
11/09/2026, rompeu esse padrão de forma diferente das anteriores: em vez de os três
produtos subirem ou caírem juntos com magnitudes parecidas, **farelo caiu -0,80%, soja
caiu -2,50% e óleo caiu -3,22%** (CME CBOT) — a primeira sessão da janela pós-reabertura
em que a ordem de queda favorece tão claramente o farelo. O mecanismo aritmético é
direto: o ratio é farelo dividido por soja (normalizado); quando o farelo cai bem menos
que a soja, o ratio sobe mesmo com o farelo em queda nominal. O resultado: **80,32%**, um
salto de +1,37 ponto percentual em um único dia — o maior movimento diário do ratio em
toda a janela recente, e o primeiro fechamento acima de 80% desde 11/06/2026.

O que torna este evento diferente das duas aproximações anteriores (que a própria
revisão D+90 tratou como "testadas e revertidas") é que, desta vez, o ratio não apenas se
aproximou do nível — ele fechou **acima**. Isso é qualitativamente diferente de tocar um
nível e recuar no mesmo dia ou no seguinte. E, pela primeira vez em toda a janela, esse
movimento veio acompanhado de **todos** os outros indicadores de complexo se movendo na
mesma direção no mesmo dia:

- **ISF (Índice de Sobra de Farelo):** 80 → **60** (indicators, 11/09) — a primeira
  mudança em quatro sessões consecutivas em que o índice havia permanecido travado em
  80/100 mesmo com o preço oscilando em ambas as direções. Isso é relevante porque as
  leituras diárias anteriores (08, 09 e 10/09) haviam registrado, com desconfiança
  crescente, a possibilidade de que o ISF fosse "pesado demais" para reagir a qualquer
  coisa que não fosse uma mudança estrutural de fato. O movimento de hoje sugere que a
  métrica reage, sim, quando o movimento de preço é grande o bastante — o que dá mais
  crédito à ideia de que hoje passou esse teste de magnitude.
- **ISO (Índice de Suporte do Óleo):** 100 → **80** (indicators, 11/09) — mesmo padrão,
  espelhado.
- **Oil share:** 50,46% → **49,84%** (indicators, 11/09) — a primeira leitura abaixo de
  50% em toda a janela do dump (todas as leituras anteriores, de pelo menos 08/09 em
  diante, estiveram entre 50,38% e 50,56%). Como farelo e óleo somam 100% por construção,
  isso significa que o farelo passou a responder por 50,16% do valor total do crush —
  ultrapassando o óleo pela primeira vez na janela.
- **Oil-meal spread:** +0,1419 → **-0,0495** USD/bushel (indicators, 11/09) — a primeira
  leitura negativa de toda a janela. Esta é, das cinco métricas, a mais direta: não é uma
  razão nem um índice composto, é a diferença bruta de valor entre óleo e farelo dentro
  do crush. Ela virou de sinal.

Cinco métricas diferentes, construídas de formas matematicamente distintas a partir dos
mesmos três preços brutos, todas se movendo na mesma direção no mesmo dia, é um padrão de
coerência interna que nenhuma das aproximações anteriores de 80% (04/09, 09/09) exibiu —
naquelas ocasiões, o ratio se moveu, mas ISF/ISO ficaram travados. Isso é o argumento mais
forte a favor de tratar o evento de hoje com mais peso do que os anteriores.

## Por que, mesmo assim, o veredito aqui é "neutro sob teste", não "tese invalidada"

- **Um único fechamento não é uma tendência.** O próprio histórico desta tese mostra dois
  episódios de aproximação de 80% (79,76% em 04/09 e 79,08%/79,06% em 09/09) que foram
  revertidos na sessão seguinte. O padrão-base, portanto, é de reversão rápida. Tratar o
  evento de hoje como confirmação definitiva exigiria, no mínimo, um segundo fechamento
  consecutivo acima de 80% — o que nunca aconteceu nesta janela e ainda não aconteceu
  agora.
- **O COT mais fresco (08/09) é de três dias antes do evento e mostra um sinal ambíguo,
  não uma confirmação.** O net long de managed money em farelo ficou praticamente parado
  (+0,32%), mas a composição — short caindo -26,73% muito mais rápido que long caindo
  -2,86% — é consistente com cobertura de posição vendida (fundos que já estavam vendidos
  em farelo fechando essas posições), não com convicção compradora nova entrando. Isso é
  uma leitura mais fraca do que seria um net long crescendo por long novo. E, de qualquer
  forma, o corte é anterior ao evento que estamos avaliando — o próximo corte (esperado
  por volta de 18/09) é o primeiro que poderá dizer se os fundos reagiram à sessão de
  hoje.
- **O WASDE de setembro trouxe uma revisão estrutural na direção oposta, ainda que
  modesta.** A projeção de exportação de farelo argentino para 2026/27 subiu de 2,89 para
  **2,99 milhões de toneladas** (USDA WASDE, edição de setembro vs agosto) — mais oferta
  exportável de farelo no maior concorrente direto do Brasil no mercado internacional é,
  estruturalmente, um vetor que tende a pressionar o preço relativo do farelo para baixo
  no médio prazo, não para cima. Este dado por si só não invalida o movimento de preço de
  hoje (que é de curtíssimo prazo), mas é um contraponto fundamentalista genuíno que pesa
  contra a ideia de tratar o cruzamento de 80% como o início de uma escassez estrutural de
  farelo.
- **A trajetória da ABIOVE para o Brasil também não aponta, por ora, para escassez.** A
  produção de farelo projetada recua de 2.129 mil toneladas (set/26) para 1.659 mil
  toneladas (dez/26) — uma queda sazonal esperada, mas que reflete principalmente menor
  esmagamento (safra em final de ciclo), não um choque de demanda que justificasse um
  ratio estruturalmente mais alto. É possível reconciliar isso com o ratio subindo (menos
  oferta relativa de farelo empurra o ratio para cima, mesmo sem choque de demanda), mas
  os dados não permitem, por ora, separar as duas explicações com confiança.
- **O físico brasileiro não mostrou nenhuma reação.** Farelo MT/IMEA, Rondonópolis e RS
  seguem exatamente nos mesmos níveis desde 04/09 e 28/08 (NAG, última leitura 09/09), e o
  prêmio de exportação em Paranaguá está congelado há 16 dias corridos. Se o mercado
  físico doméstico não repassar qualquer força para o farelo nos próximos dias, o
  movimento de hoje permanece restrito ao papel em Chicago — um cenário que já ocorreu
  antes nesta mesma tese (o papel se movendo sem o físico acompanhar).

## O veredito

Tomando tudo isso em conjunto: o gatilho de invalidação definido em 11/06/2026 e
reafirmado no veredito D+90 de 09/09/2026 **disparou tecnicamente hoje** — é a primeira
vez, em 92 dias corridos de tese, que o ratio Far/Soj fecha acima de 80%. Isso é um fato,
não uma interpretação, e esta leitura o registra como tal. Mas o disparo do gatilho não
é, por si só, prova de que a tese de abundância estrutural de farelo (o mecanismo:
crush favorecendo o processamento pelo lado do óleo, com farelo sobrando como
subproduto) deixou de valer — é prova de que, pela primeira vez, o mercado testou esse
nível com força suficiente para fechar além dele, algo que não havia acontecido nas duas
tentativas anteriores. A combinação de cinco indicadores diferentes se movendo juntos dá
a este evento mais peso estrutural do que os anteriores, mas a ausência de confirmação em
COT contemporâneo, a ausência de reação do físico brasileiro, e uma revisão do WASDE
apontando para mais oferta de farelo argentino no médio prazo são, juntos, motivo
suficiente para não tratar isso como uma inversão completa de tese.

**Decisão de classificação:** rebaixar o farelo de `bear-farelo` (vigente desde
11/06/2026) para **`neutral-farelo`** — não elevá-lo a `bull-farelo`. A tese de
abundância perde a confiança que tinha, mas não há, ainda, evidência fundamentalista
(COT, físico, WASDE) suficiente para justificar o oposto (escassez de farelo). "Neutro"
reflete literalmente a própria definição do indicador para a zona 80-87%, e reflete
também o estado real da evidência: dividida, não unânime.

## O que confirmaria (ou desfaria) esta mudança de classificação

- **Confirmação de tese mudando de fato:** um segundo fechamento consecutivo acima de
  80% (o que nunca ocorreu nesta janela) seria o primeiro sinal de que este não é apenas
  um evento de um dia; um fechamento acima de 87% (zona "apertada") exigiria reavaliar o
  viés para `bull-farelo` de forma mais decisiva.
- **Desfazendo a mudança:** um fechamento de volta abaixo de 80% na próxima sessão
  reduziria o evento de hoje ao terceiro episódio de "toque e recuo" da janela — o que,
  dado o histórico, é um cenário que não pode ser descartado.
- **O COT de 15/09** (esperado por volta de 18/09) é o primeiro dado de posicionamento
  capaz de confirmar ou contradizer diretamente a leitura de hoje.
- **Qualquer reação do físico brasileiro de farelo** (MT/IMEA, Rondonópolis, RS, prêmio
  export Paranaguá) nos próximos dias, hoje ainda completamente ausente, seria o segundo
  pilar de confirmação fundamentalista que falta.

## Encaminhamento

Este insight não substitui nem revisa formalmente o arquivo original
([[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]), que segue com seu próprio
calendário de revisões (`status: revisada`, D+180 em 2026-12-08) — mas atualiza o
registro factual mais importante desde então: o gatilho de invalidação definido naquela
tese ocorreu, pela primeira vez, na sessão de 11/09/2026. Para o trader que opera os dois
lados: hoje não é dia de virar totalmente comprado em farelo com base em um único
fechamento, mas é o primeiro dia, desde 11/06, em que reduzir ou zerar uma posição
estrutural vendida em farelo (ou no spread Far/Soj vendido) tem justificativa concreta —
o gatilho que a própria tese definia como razão para reavaliar aconteceu. A recomendação
operacional é reduzir tamanho e monitorar a confirmação (segundo fechamento acima de 80%,
COT de 15/09, reação do físico) antes de tratar isso como uma inversão de tese completa e
duradoura.
