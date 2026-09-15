---
data: 2026-09-15
titulo: "O ratio Far/Soj fecha acima de 80% pela terceira sessão consecutiva (80,25% em 11/09, 80,55% em 14/09, 80,46% em 15/09) — o critério de confirmação definido em 12/09 (um segundo fechamento consecutivo) foi satisfeito e reforçado, mas ISF/ISO ficaram travados, o COT completa sete dias de defasagem e o físico brasileiro segue congelado há seis dias, então o veredito sobe de 'neutro sob teste' para 'neutro consolidado', não para 'bull-farelo'"
tags: [farelo, ratio-far-soj, spread, revisao, auto-claude]
fontes:
  - Tese original — [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (11/06/2026): ratio Far/Soj 81,4% comprimindo de 83,3% em 4 pregões, prêmio export de farelo em Paranaguá zerado (+0,05 USD/sht, NAG 10/06), crush margin em recorde de US$3,78/bushel com oil share 55,4% — viés baixista no farelo (`bear-farelo`), com gatilho de invalidação definido como "um fechamento do ratio acima de 80% pela primeira vez desde a abertura da tese" e revisões programadas em D+7 (18/06), D+90 (09/09) e D+180 (08/12)
  - Veredito D+90 — [[2026-09-09_d90-ratio-far-soj-reverte-na-vespera]] (09/09/2026): concluiu que a tese "não foi invalidada" após 90 dias corridos
  - Primeiro cruzamento — [[2026-09-12_ratio-far-soj-rompe-80-pela-primeira-vez]] (12/09/2026, tratando a sessão de 11/09): ratio fechou em 80,25% (número corrigido em [[2026-09-13_correcao-numeros-sessao-11set-farelo-oleo]]; o insight original de 12/09 usara 80,32%), o primeiro fechamento acima de 80% em 92 dias corridos — classificado como "neutro sob teste", não confirmação, com o critério explícito de que "um segundo fechamento consecutivo acima de 80%... seria o primeiro sinal de que isso não é apenas um evento de um dia"
  - Leitura de 13/09 — [[2026-09-13_leitura-complexo]]: manteve "neutro" com margens de apoio mais estreitas do que inicialmente descritas, sem sessão nova de preço (fim de semana)
  - CME CBOT — três sessões: 11/09 (sexta-feira) farelo 346,80 / soja 1.296,50 / óleo 69,19; 14/09 (segunda-feira) farelo 350,40 (+1,04%) / soja 1.305,00 (+0,66%) / óleo 69,62 (+0,62%); 15/09 (terça-feira, hoje) farelo 348,20 (-0,63%) / soja 1.298,25 (-0,52%) / óleo 69,50 (-0,17%)
  - Indicadores sintéticos internos — far_soj_ratio_pct: **80,25%** (11/09) → **80,55%** (14/09) → **80,46%** (15/09), indicators — três fechamentos consecutivos acima de 80%, o padrão mais longo desde a abertura da tese em 11/06/2026 (96 dias corridos até hoje); oil_share_pct: 49,94% → 49,84% → 49,95%, três leituras seguidas abaixo de 50%; oil_meal_spread_usd_bu: -0,0187 → -0,0506 → -0,0154 USD/bushel, três leituras negativas seguidas; ISF (índice de sobra de farelo) e ISO (índice de suporte do óleo) travados em 60/100 e 80/100 desde 11/09, sem novo movimento em 14/09 nem 15/09
  - CFTC COT Managed Money — corte de 2026-09-08 (mais recente disponível, agora sete dias corridos de defasagem frente à sessão de hoje): net long farelo 157.689 contratos (+0,32% vs 01/09, via cobertura de posição vendida, não long novo); nenhuma atualização desde então — não é possível confirmar se os fundos reagiram às três sessões de mudança de regime
  - USDA WASDE, edição de setembro/2026 (sem nova edição nesta janela, tratando novamente `release-usda_wasde-2026-09-11`): exportação de farelo argentino 2026/27 revisada de 2,89 para 2,99 milhões de toneladas — vetor estrutural de médio prazo na direção oposta ao sinal de preço
  - ABIOVE projeções mensais (sem revisão nesta janela): produção de farelo recuando de 2.129 mil t (set/26) para 1.659 mil t (dez/26), exportação de 1.100 para 700 mil t no mesmo período — trajetória de alívio de oferta doméstica de farelo, desta vez alinhada (não em tensão) com o sinal de preço de curto prazo
  - NAG Físico BR — última leitura ainda 2026-09-09: farelo MT/IMEA R$1.875,45/ton (congelado desde 04/09), prêmio export Paranaguá +0,12 USD/short ton (congelado desde 27/08, 19 dias corridos até hoje) — nenhuma reação visível do físico às três sessões de mudança em Chicago
  - Fila de julgamento 2026-09-15 — `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` (🔴, recorrente) e `-D+90` (🔴, recorrente)
  - Cruza com [[2026-09-15_leitura-complexo]] (leitura diária de hoje, que trata a mesma confirmação em nível de complexo e detalha, na seção Honestidade, um problema de qualidade de dado nos campos brutos de farelo de 14/09 e um volume anormalmente baixo na sessão de hoje — nenhum dos dois afeta os fechamentos usados aqui, que são consistentes entre as gerações do briefing)
status: ativa
vies: [neutral-farelo]
---

## Por que este insight existe separado da leitura diária

Em 12/09/2026, quando o ratio Far/Soj fechou acima de 80% pela primeira vez em 92 dias
corridos de tese, o insight dedicado daquele dia
([[2026-09-12_ratio-far-soj-rompe-80-pela-primeira-vez]]) definiu, de forma explícita e
verificável, o que faltava para tratar o evento como confirmação de mudança de regime, e
não apenas mais um "toque e recuo" como as duas aproximações anteriores (79,76% em 04/09 e
79,06%/79,08% em 09/09, ambas revertidas na sessão seguinte): *"um segundo fechamento
consecutivo acima de 80%... seria o primeiro sinal de que isso não é apenas um evento de
um dia"*. Esse critério foi satisfeito na segunda-feira 14/09 (80,55%) e, hoje,
15/09/2026, foi reforçado com um terceiro fechamento consecutivo (80,46%). Um evento
definido com esse nível de clareza, satisfeito duas vezes seguidas, merece um documento
próprio que atualize o veredito com todo o peso que a pergunta exige — a mesma lógica que
levou à criação do insight de 12/09 e do veredito D+90 de 09/09
([[2026-09-09_d90-ratio-far-soj-reverte-na-vespera]]).

## O que mudou desde o veredito de 12/09

O insight de 12/09 já reconhecia que cinco métricas diferentes (ratio, ISF, ISO, oil
share, oil-meal spread) haviam se movido juntas na sessão de 11/09 — um padrão de
coerência interna que nenhuma das aproximações anteriores de 80% havia exibido — mas
concluiu que um único dia não bastava, e rebaixou o farelo de `bear-farelo` para
`neutral-farelo`, não além disso. A pergunta em aberto era simples: o movimento teria
continuidade, ou seria mais um caso de "o papel se move sem confirmação, e reverte"?

A resposta, nas duas sessões seguintes, foi de continuidade — mas com uma nuance
importante que separa as métricas contínuas das métricas discretas:

- **Ratio Far/Soj**: 80,25% (11/09) → **80,55%** (14/09, o pico da janela) → **80,46%**
  (15/09, hoje) — três fechamentos seguidos acima de 80%, com uma pequena oscilação entre
  eles, mas sem qualquer aproximação de volta ao patamar de 80% que caracterizou as duas
  reversões anteriores. A distância mínima ao piso de 80% nas três sessões foi de 0,25
  ponto percentual (11/09); hoje, a distância é de 0,46 ponto — folga pequena, mas
  positiva nas três ocasiões.
- **Oil share**: 49,94% → 49,84% → **49,95%** — três leituras abaixo de 50%, oscilando
  dentro de uma banda muito estreita (0,11 ponto percentual de amplitude). O farelo
  responde por 50,05% a 50,16% do valor total do crush nas três sessões — uma inversão
  pequena, mas persistente, da relação que vigorou durante a maior parte da tese desde
  junho (óleo tipicamente acima de 50%).
- **Oil-meal spread**: -0,0187 → -0,0506 → **-0,0154** USD/bushel — a métrica mais direta
  (diferença bruta de valor entre óleo e farelo dentro do crush) permanece do lado do
  farelo nas três sessões, mas sem tendência de aprofundamento: o valor de hoje é o mais
  próximo de zero dos três, sugerindo que o "equilíbrio invertido" é real, porém instável e
  pequeno em magnitude — não uma virada estrutural agressiva.
- **ISF e ISO — as duas métricas que ficaram paradas.** ISF em 60/100 e ISO em 80/100
  desde 11/09, sem qualquer novo movimento em 14/09 nem hoje. Essas métricas são
  construídas por contagem de condições discretas (por exemplo, "3 de 5 condições
  atendidas"), não como um valor contínuo — e o fato de terem "saltado" em 11/09 e ficado
  paradas desde então sugere que a magnitude do movimento das últimas duas sessões, embora
  suficiente para manter o ratio, o oil share e o oil-meal spread do lado do farelo, não
  foi grande o bastante para acionar a próxima condição discreta de nenhum dos dois
  índices. Isso é um contraponto genuíno: se a mudança de regime fosse tão forte quanto o
  ratio sozinho sugere, seria razoável esperar que ISF e ISO também continuassem se
  movendo — e não continuaram.

## Por que o veredito sobe para "neutro consolidado", mas não para "bull-farelo"

**A favor de reconhecer uma confirmação real:**

- Três fechamentos consecutivos acima de 80% não têm precedente nesta tese — as duas
  aproximações anteriores nunca passaram de um único dia. O padrão-base de "toque e
  recuo" que dominou a janela de junho a setembro foi, na prática, rompido.
- Três métricas contínuas e matematicamente independentes (ratio, oil share, oil-meal
  spread) concordam na mesma direção nas mesmas três sessões — não é um artefato de uma
  única fórmula.
- A trajetória da ABIOVE para o Brasil (produção de farelo recuando de 2.129 para 1.659
  mil t entre set/26 e dez/26) deixou, pela primeira vez, de estar em tensão com o sinal de
  preço de curto prazo — os dois horizontes agora apontam na mesma direção.

**Contra tratar isso como inversão completa de tese:**

- **ISF e ISO não avançaram** nas últimas duas sessões — a magnitude do movimento, por
  ora, parece suficiente para sustentar a mudança inicial, mas não para aprofundá-la.
- **O COT de 08/09 tem sete dias corridos de defasagem** frente à sessão de hoje, o maior
  atraso desde a abertura da tese — não há qualquer confirmação de que os fundos, cuja
  última leitura mostrava cobertura de posição vendida (não convicção compradora nova),
  reagiram às três sessões de mudança de regime. O próximo corte (posições de 15/09,
  esperado por volta de 18/09) é o primeiro capaz de resolver essa lacuna.
- **O físico brasileiro está congelado há seis dias corridos** (última leitura 09/09) —
  nenhum sinal de que o mercado doméstico de farelo, prêmios de exportação ou basis
  reagiram a qualquer coisa que aconteceu em Chicago desde então.
- **O WASDE de setembro revisou a exportação de farelo argentino para cima** (2,89 → 2,99
  milhões de toneladas 2026/27) — um vetor estrutural de médio prazo que segue trabalhando
  contra a ideia de escassez de farelo, mesmo que o sinal de preço de curto prazo aponte
  para o lado oposto.
- **A própria definição do indicador trata a faixa 80-87% como "neutra"**, não "apertada"
  — o ratio segue a apenas 0,46 ponto percentual acima do piso dessa faixa, longe dos 87%
  que caracterizariam uma leitura genuinamente apertada e justificariam `bull-farelo`.
- **O volume da sessão de hoje foi anormalmente baixo** (479 contratos em farelo, uma
  fração dos 20-30 mil típicos desta janela — ver [[2026-09-15_leitura-complexo]],
  seção Honestidade) — o que reduz a confiança de que o fechamento de 80,46% de hoje
  reflita a liquidação plena do mercado, e recomenda aguardar volume normal antes de tratar
  a terceira confirmação como definitiva.

## O veredito

Tomando as três sessões em conjunto: o critério de confirmação definido em 12/09 — um
segundo fechamento consecutivo acima de 80% — foi satisfeito em 14/09 e reforçado hoje com
um terceiro. Isso é qualitativamente diferente das duas aproximações anteriores de 80%
(04/09 e 09/09), que nunca sustentaram o nível por mais de uma sessão. A classificação
sobe de **"neutro sob teste"** (12/09) para **"neutro consolidado"**: a tese de abundância
estrutural de farelo (`bear-farelo`, vigente de 11/06 a 12/09) permanece descartada, e a
confiança de que o farelo genuinamente saiu da zona "abundante" é agora mais alta do que
em qualquer ponto anterior da tese — mas a classificação **não** sobe para `bull-farelo`,
porque (a) o ratio segue dentro da própria zona "neutra" por definição, (b) os índices
compostos ISF/ISO não avançaram nas últimas duas sessões, (c) falta confirmação de COT
contemporâneo e do físico brasileiro, e (d) o volume anormalmente baixo da sessão de hoje
introduz uma reserva metodológica que não existia nas duas sessões anteriores.

**Decisão de classificação:** manter **`neutral-farelo`**, com nota de que a confiança
subiu de "sob teste" para "consolidada" — uma diferença relevante para dimensionamento de
posição, ainda que não para a direção do viés.

## O que elevaria isso a `bull-farelo`, e o que devolveria a `bear-farelo`

- **Elevando a confiança ainda mais:** um quarto fechamento consecutivo acima de 80% com
  volume normal confirmaria que a sessão de hoje não foi um artefato de baixa liquidez; um
  fechamento acima de 87% (zona "apertada", pela própria definição do indicador) exigiria
  reavaliar para `bull-farelo` de forma decisiva; um avanço do ISF para 40 ou menos (ou do
  ISO para 60 ou menos) mostraria que a magnitude do movimento finalmente ultrapassou o
  patamar que trava esses índices desde 11/09.
- **Desfazendo a mudança:** um fechamento de volta abaixo de 80% na próxima sessão
  reduziria a sequência atual a "três dias que também reverteram", ainda que com um
  precedente mais longo do que qualquer episódio anterior.
- **O COT de 15/09** (esperado por volta de 18/09) é o primeiro dado de posicionamento
  capaz de confirmar ou contradizer diretamente os últimos três fechamentos.
- **Qualquer reação do físico brasileiro** (MT/IMEA, Rondonópolis, RS, prêmio export
  Paranaguá), hoje ainda completamente ausente, seria o segundo pilar de confirmação
  fundamentalista que falta.

## Encaminhamento

Este insight não substitui nem revisa formalmente o arquivo original
([[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]), que segue com seu próprio
calendário de revisões (`status: revisada`, D+180 em 2026-12-08), nem o insight de 12/09
([[2026-09-12_ratio-far-soj-rompe-80-pela-primeira-vez]]), que documentou corretamente o
primeiro cruzamento e definiu o critério que este documento agora usa para atualizar o
veredito. Para o trader que opera os dois lados: a acumulação de três fechamentos
consecutivos acima de 80% é o quadro mais desfavorável a uma posição estrutural vendida em
farelo (ou no spread Far/Soj vendido) desde a abertura da tese em 11/06 — a recomendação é
reduzir tamanho de forma mais decisiva do que a cautela sugerida em 12 e 13/09. Ainda
assim, não é dia de virar comprado em farelo com convicção plena: faltam o COT de 18/09, a
reação do físico brasileiro, e confirmação de que o volume anormalmente baixo de hoje não
distorceu o terceiro fechamento.
