---
data: 2026-09-12
titulo: "Sexta-feira de reversão no complexo: soja cai -2,50% fechando no piso do range em volume recorde (245.874 contratos), óleo desaba -3,22% fechando a 6 centavos da mínima do dia enquanto o salto de +7% do heating oil de quinta se desfaz quase por completo, e o ratio Far/Soj fecha em 80,32% — a primeira vez ACIMA de 80% desde a abertura da tese de abundância de farelo em 11/06/2026, cruzando para a zona 'neutro' junto com ISF, ISO, oil share e oil-meal spread se movendo todos na mesma direção pela primeira vez em toda a janela pós-reabertura"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT — sessão de 2026-09-11 (sexta-feira), quarto pregão pleno desde a reabertura de 08/09. Soja (ZSX26, venc. nov/26): abertura 1.330,00, máxima 1.335,25, mínima 1.293,00, fechamento 1.299,00 USD cts/bushel, volume 245.874 contratos. Farelo (ZMV26, venc. out/26): abertura 349,30, máxima 350,60, mínima 344,70, fechamento 347,80 USD/short ton, volume 31.757 contratos. Óleo (ZLV26, venc. out/26): abertura 71,57, máxima 71,72, mínima 69,05, fechamento 69,11 USD cts/lb, volume 22.112 contratos. Curva futura em 11/09 — soja: set/26 1.296,00, nov/26 (base) 1.299,00, jan/27 1.314,25, mar/27 1.321,25, mai/27 1.327,75, jul/27 1.330,25; farelo: set/26 349,30, out/26 (base) 347,80, dez/26 353,80, jan/27 355,70, mar/27 356,80, mai/27 357,40; óleo: set/26 70,66, out/26 (base) 69,11, dez/26 69,61, jan/27 69,90, mar/27 70,11, mai/27 70,18
  - CME NYMEX heating oil (HO=F) — 2026-09-11: máxima 4,9344, mínima 4,7408, fechamento 4,7792 USD/galão, volume 50.946 contratos. O campo "abertura" do dump (5,1481) está acima da própria máxima do dia (4,9344), uma inconsistência interna da linha bruta — tratada como artefato de reconciliação e não usada para calcular variação; ver Honestidade
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, ISF, ISO, margem biodiesel, paridade BR) — 2026-09-11, quarto recálculo com insumo de preço fresco desde a reabertura; base de comparação 2026-09-10 usa os valores embutidos nas próprias fórmulas dos indicadores daquele dia (farelo 350,60 / óleo 71,41 / soja 1.332,25), não uma soma de linhas brutas de CME CBOT de 10/09 — essas linhas não estão mais na janela de 14 dias deste dump; ver Honestidade
  - BCB PTAX — 2026-09-11: USD/BRL 5,0918, EUR/BRL 5,9085, Selic diária 0,05166% a.a. (séries SGS 1, 21619, 11); 2026-09-10: USD/BRL 5,1149, EUR/BRL 5,9481
  - CFTC COT Managed Money, Swap Dealers e Producer/Merchant — corte de 2026-09-08 (terça-feira), a primeira atualização desde 01/09, tratando a fila `release-cftc_cot-2026-09-08`: farelo net long managed money 157.689 contratos (+0,32% vs 01/09, 157.179→157.689), com long caindo -2,86% (178.183→173.079) e short caindo -26,73% (21.004→15.390) — cobertura de posição vendida, não convicção nova compradora; óleo net long 91.711 contratos (-8,13% vs 01/09, 99.823→91.711), long -3,19% e short +17,14% — fundos reduzindo exposição líquida ao óleo já antes da sessão de hoje; soja net long 257.258 contratos (+9,51% vs 01/09, 234.920→257.258), long +8,42% e short +1,20% — fundos ampliando convicção compradora na semana que antecedeu a reversão de hoje. Open interest: soja 1.070.401 (+4,17%), farelo 667.618 (+2,86%), óleo 601.961 (-1,16%). Este corte retrata posições de 08/09, três dias corridos antes da sessão de hoje (11/09) — ver Honestidade
  - CEPEA/ESALQ Soja Paranaguá via NAG — última leitura disponível ainda 2026-09-09: R$ 160,12/saca (var -0,21%); sem atualização própria para 10/09 nem 11/09 nesta janela (3 dias corridos sem publicação nova)
  - CEPEA/ESALQ Soja Paraná interior via NAG — última leitura disponível ainda 2026-09-09: R$ 152,43/saca (var +0,13%); mesma ausência de atualização
  - NAG Físico BR — última leitura disponível ainda 2026-09-09: farelo MT/IMEA R$ 1.875,45/ton (congelado desde 04/09), Rondonópolis/MT R$ 1.900,00/ton (congelado desde 31/08), RS média R$ 1.860,00/ton (congelado desde 28/08); prêmios export Paranaguá farelo +0,12 USD/short ton e óleo +0,10 cts/lb, ambos congelados desde 27/08 — 16 dias corridos até hoje (12/09)
  - USDA Crop Progress — corte mais recente, semana encerrada em 2026-09-06: 12% excelente / 46% boa / 9% ruim (G/E 58%), inalterado desde 30/08; próximo corte esperado segunda-feira 14/09
  - USDA WASDE — release de 2026-09-11 presente nesta janela do dump, tratando a fila `release-usda_wasde-2026-09-11`, mas **apenas com a tabela de farelo (meal) de Argentina e Brasil, comparando as edições de agosto e setembro/2026** — sem tabelas de soja em grão nem de óleo, e sem dado de EUA nesta janela; ver corpo do texto e Honestidade
  - NOPA — fila `release-nopa-2026-09-11`; `monthly_status` seguiu em 0,0 bool (paywall) em 2026-09-11, quinto dia seguido do mesmo falso positivo na fila desde 27/08
  - ABIOVE projeções mensais — balanços set-dez/2026, sem revisão nesta janela (mesmos números já usados desde 08 ou 09/09)
  - NOAA CPC ENSO — El Niño Advisory, inalterado até 2026-09-11
  - MPOB — carimbo 2026-09-11, parser sem números extraídos (mesma barreira, 3.457 caracteres)
  - BCBA (Argentina) — carimbo 2026-09-09, scraper acessa a página mas não encontra links de relatório
  - INMET — previsão para 2026-09-12 (HOJE): calor forte no núcleo produtor de Mato Grosso com nebulosidade e chuva isolada (Cuiabá 37°C/27°C, Sinop 39°C/23°C, Sorriso 38°C/22°C, Lucas do Rio Verde 39°C/22°C, Rio Verde/GO 36°C/20°C) e chuva com trovoadas no Sul sem menção de geada (Cascavel/PR 29°C/17°C, Maringá/PR 31°C/19°C, Passo Fundo/RS 19°C/13°C)
  - Notícias Agrícolas/Canal Rural + FarmProgress RSS — 2026-09-11: "0 items lidos, 0 mantidos (soja/farelo/oleo)", segundo dia seguido de falha ou pausa total de coleta (10 e 11/09)
  - CEPEA RSS — última leitura ainda 2026-09-09: 109 itens parseados; última manchete de preço disponível permanece a de 04/09 ("Alta dos preços ganha força no início de setembro")
  - system/tributario_watch.toml (lido como referência, não editado) — `atualizado_em` 2026-06-05 em todos os 10 eventos catalogados, agora **99 dias corridos** sem revisão humana frente a hoje (12/09)
  - Forecasts estatísticos internos (bandas 7d/30d, MA20+volatilidade+slope) — geração de 2026-09-11, alvos 18/09 (7d) e 11/10 (30d); viés "altista" em soja e farelo nos dois horizontes, "altista" no óleo em ambos (7d passou de "lateral" para "altista" nesta geração), calculado sobre o fechamento de 11/09 (que já é o fechamento em queda desta sessão — os forecasts, portanto, ainda não incorporam a reversão de hoje como direção nova, apenas como novo ponto de partida)
  - Fila de julgamento (carimbada 2026-09-11 no briefing, 11 itens) — tratados nesta leitura: `alerta-quebra_resistencia-soja_cbot-2026-09-11`, `alerta-quebra_suporte-oleo_cbot-2026-09-11`, `alerta-movimento_forte-oleo_cbot-2026-09-11`, `alerta-quebra_resistencia-farelo_cbot-2026-09-11`, `alerta-quebra_suporte-complexo_soja-2026-09-11`, `ratio-zona-2026-09-11`, `release-usda_wasde-2026-09-11`, `release-nopa-2026-09-11`, `release-cftc_cot-2026-09-08`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`
  - Cruza com [[2026-09-11_leitura-complexo]] (leitura de ontem, que descreveu o terceiro pregão com os três produtos subindo juntos e o óleo a -0,76% de reconquistar 72,00) e com [[2026-09-09_d90-ratio-far-soj-reverte-na-vespera]] (veredito da revisão D+90 da tese original do ratio Far/Soj, aberta em [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]], que definia o fechamento acima de 80% como o gatilho concreto de invalidação — ver insight separado publicado hoje, [[2026-09-12_ratio-far-soj-rompe-80-pela-primeira-vez]])
status: ativa
vies: [bull-soja, neutral-farelo, bear-oleo_soja]
---

## Visão geral

Hoje, sábado 12/09/2026 (dia de escrita; o dado mais fresco do briefing é o fechamento
de sexta-feira 11/09, o quarto pregão pleno na CBOT — bolsa de grãos de Chicago onde
soja, farelo e óleo de soja são negociados em contratos futuros — desde a reabertura de
terça-feira 08/09 após a pausa de feriado duplo). Recapitulando o mecanismo básico para
quem não acompanha o dia a dia: a soja em grão, ao ser esmagada ("crush", o processo
industrial que separa o grão em farelo e óleo), vira dois produtos com demandas muito
diferentes — farelo (concentrado de proteína para ração animal) e óleo (alimentação
humana e, cada vez mais, biodiesel). O "crush margin" mede, em dólares por bushel
(unidade agrícola americana de ~27,2 kg de soja), quanto sobra para a esmagadora depois
de vender farelo + óleo e pagar a soja. O "oil share" (fatia do valor total do crush que
vem do óleo) diz qual dos dois produtos está "pagando a conta": alto = óleo manda e
farelo vira subproduto barato (o que o índice sintético interno "Índice de Sobra de
Farelo", ISF, capta pelo lado baixista do farelo); baixo = o farelo sustenta o crush e o
óleo perde força relativa (o "Índice de Suporte do Óleo", ISO, capta o espelho disso). O
ratio Far/Soj (preço do farelo dividido pelo da soja, normalizado em percentual) é a
métrica clássica para a mesma ideia: abaixo de 80% o farelo está "abundante" (barato
relativo à soja, viés baixista); entre 80% e 87% ele entra em zona "neutra"; a partir de
87% fica "apertado" (caro relativo à soja, viés altista).

As últimas quatro leituras diárias descreveram uma sequência de vaivém seguida por uma
sessão em que os três produtos subiram juntos (10/09), com o óleo vencendo a disputa por
valor dentro do crush de forma mais clara do que em qualquer dia da janela, puxado por um
salto de aproximadamente +7% no heating oil (diesel de aquecimento americano, cujo preço
entra direto na conta de receita do biodiesel via a fórmula "receita = HO + 1,5×crédito
RIN D4"). A leitura de ontem já registrou, na seção Honestidade, a dúvida explícita sobre
se esse salto de heating oil era sustentável, dado que não havia notícia específica que o
explicasse. A resposta veio rápido: na sessão de hoje (11/09), o heating oil fechou em
**4,7792 USD/galão** (CME NYMEX), com máxima do dia em apenas 4,9344 — devolvendo quase
toda a alta anômala de quinta-feira. Com a receita de biodiesel caindo junto, a margem
recuou de US$ 2,0667/galão para **US$ 1,961/galão** (indicators, 11/09), uma queda de
**-5,11%** — o primeiro recuo da margem em três sessões, depois de dois recordes
consecutivos.

Mas o evento isolado mais importante do dia não foi o heating oil sozinho — foi o que
aconteceu simultaneamente nos três produtos do complexo, todos caindo, mas em
velocidades muito diferentes: soja **-2,50%** (de 1.332,25 para 1.299,00, CME CBOT),
óleo **-3,22%** (de 71,41 para 69,11 — o próprio texto da fila confirma essa variação
exata, `alerta-movimento_forte-oleo_cbot-2026-09-11`) e farelo apenas **-0,80%** (de
350,60 para 347,80). É a primeira sessão da janela pós-reabertura em que o farelo caiu
menos, em módulo, do que tanto a soja quanto o óleo — o farelo mostrou a maior
resiliência relativa do complexo justamente no dia em que tudo caiu. E é exatamente essa
diferença de velocidade que fez o ratio Far/Soj **fechar acima de 80% pela primeira vez
desde a abertura da tese de abundância de farelo, em 11/06/2026**: 80,32% hoje, ante
78,95% ontem — um avanço de **+1,37 ponto percentual em um único dia**, o maior
movimento diário do ratio em toda a janela recente. A própria fila de julgamento
classificou esse evento como `ratio-zona-2026-09-11`, descrevendo a mudança de zona de
"comprimido" para "neutro". Junto com o ratio, **todos** os outros indicadores de
complexo se moveram na mesma direção pela primeira vez em toda a janela: o Índice de
Sobra de Farelo (ISF) caiu de 80 para **60**, o Índice de Suporte do Óleo (ISO) caiu de
100 para **80**, o oil share caiu de 50,46% para **49,84%** (primeira vez abaixo de 50%
em toda a janela do dump) e o oil-meal spread virou de +0,1419 para **-0,0495**
USD/bushel (primeiro valor negativo da janela — ou seja, pela primeira vez em semanas o
farelo está "pagando mais" que o óleo dentro da conta do crush). Isso é relevante porque
as leituras anteriores haviam registrado, com desconfiança, que o ISF/ISO permaneciam
"parados" havia três sessões seguidas mesmo com preço oscilando — hoje, com um movimento
de preço grande o bastante, os índices finalmente se moveram, o que reforça a leitura de
que eles são calibrados para mudanças estruturais, não ruído diário, e que o movimento de
hoje passa esse teste.

Do lado técnico isolado, a sessão de soja também chama atenção por si só: fechamento em
1.299,00, apenas 6,00 pontos acima da mínima do dia (1.293,00) — um fechamento muito
fraco dentro do próprio range, o oposto exato do fechamento forte perto da máxima
observado ontem — e tudo isso em volume de **245.874 contratos**, o maior volume de toda
a janela pós-reabertura (+62,3% sobre os ~151.466 de ontem). Um fechamento fraco perto da
mínima, em volume recorde, depois de uma nova máxima da janela no dia anterior, é o
padrão técnico clássico de um dia de reversão/distribuição — não confirma sozinho o fim
da tendência de alta desde a reabertura, mas é o primeiro sinal de alerta técnico
genuíno desde que o rompimento começou. O óleo teve um comportamento ainda mais extremo:
fechou em 69,11, a apenas 0,06 acima da mínima do dia (69,05) — um fechamento no piso
absoluto do range, cancelando por completo a narrativa de ontem de "a 0,76% de
reconquistar o suporte de 72,00".

**Leitura de uma linha**: o pivô do complexo continua sendo a realocação de valor entre
farelo e óleo dentro do crush, mas hoje, pela primeira vez desde a abertura da tese em
11/06, essa realocação girou a favor do farelo e contra o óleo — coincidindo com o
primeiro fechamento do ratio Far/Soj acima de 80% de toda a tese, o gatilho de
invalidação explicitamente definido desde junho (tratado em profundidade em
[[2026-09-12_ratio-far-soj-rompe-80-pela-primeira-vez]]). Confiança **moderada**: é um
único dia de dado fresco, sem confirmação de COT contemporâneo (o corte mais recente
ainda é de 08/09, três dias antes desta sessão) nem de reação do físico brasileiro
(ainda travado desde 09/09), e o padrão histórico desta mesma janela mostrou pelo menos
duas aproximações de 80% que foram revertidas na sessão seguinte — a diferença desta vez
é que o nível não foi apenas tocado, foi **fechado acima**, o que muda o peso da
evidência, mas não a torna definitiva.

## Soja

**Viés: bull, moderado (rebaixado de forte) — a tendência de fundo desde a reabertura
segue intacta e a folga sobre a resistência de 1.180 continua larga, mas a sessão de
hoje foi o primeiro dia de reversão técnica genuína da janela: queda de -2,50%,
fechamento a 6 pontos da mínima do dia, e o maior volume de toda a série. É motivo para
reduzir convicção, não para inverter a tese.**

O que sustenta a tese:

- **A folga técnica sobre a resistência de referência continua muito ampla, mesmo após a
  queda.** Soja CBOT fechou em **1.299,00** USD cts/bushel em 11/09/2026 (CME CBOT), uma
  queda de **-2,50%** frente aos 1.332,25 (valor reconstruído via indicadores — ver
  Honestidade) do dia anterior. A fila de julgamento ainda classifica esse fechamento
  como "acima da resistência de 1.180,00" (`alerta-quebra_resistencia-soja_cbot-2026-09-11`),
  com folga de **10,08%** — ante 12,86% ontem, uma redução real, mas ainda um colchão
  confortável frente ao nível que definiu o rompimento de agosto.
- **A queda de hoje, isoladamente, não é grande o bastante para desfazer a tendência de
  fundo** — -2,50% é a maior queda diária em módulo desde a reabertura, mas ainda menor,
  em magnitude, do que a alta de +1,70% de ontem ou os +2,08% acumulados desde 08/09. O
  contrato segue, na curva futura, em contango regular: set/26 1.296,00 → nov/26 (base)
  1.299,00 → jan/27 1.314,25 → mar/27 1.321,25 → mai/27 1.327,75 → jul/27 1.330,25 (CME
  CBOT, 11/09) — sem inversão nem distorção pontual mesmo após a queda, o que sugere que o
  mercado não está precificando um evento de oferta/demanda estrutural novo, apenas um
  ajuste de curto prazo no contrato mais próximo.
- **O COT de 08/09 (o mais fresco disponível, tratando `release-cftc_cot-2026-09-08`)
  mostrou os fundos ampliando a convicção compradora na semana anterior a esta queda.**
  Managed money net long em soja saltou de 234.920 para **257.258 contratos** (+9,51%,
  CFTC COT), com o long subindo +8,42% (270.450→293.215) e o short subindo apenas +1,20%
  — ou seja, a alta de posição comprada veio de dinheiro novo entrando, não de cobertura
  de vendida. O open interest também cresceu (+4,17%, 1.027.541→1.070.401), reforçando que
  o rali da semana anterior teve participação genuína, não apenas rolagem de posição. Essa
  foto é de três dias antes da queda de hoje — ainda não sabemos se os fundos já
  começaram a reduzir essa posição recorde, mas ela dá um colchão de convicção
  institucional que não existia nas primeiras sessões pós-reabertura.
- **O câmbio amorteceu parcialmente a queda para quem vende em reais.** USD/BRL fechou em
  **5,0918** (BCB PTAX, 11/09), uma queda de -0,45% sobre os 5,1149 de 10/09 — o real se
  valorizou. Mesmo assim, como o CBOT caiu mais forte (-2,50%) do que o câmbio ajudou
  (-0,45%), a paridade em reais da soja (CBOT × câmbio, sem basis) recuou de **R$
  150,23/saca** para **R$ 145,82/saca** (indicators, 11/09) — uma queda de **-2,94%**,
  maior em módulo do que a própria queda em dólar, porque os dois efeitos (preço em dólar
  caindo, dólar mais fraco) trabalharam na mesma direção contra o vendedor brasileiro
  hoje, ao contrário de ontem quando trabalharam em direções opostas.
- **A condição da lavoura americana segue estável, sem novidade nesta janela.** USDA Crop
  Progress permanece no corte de 06/09 (12% excelente + 46% boa, "ruim" 9%, G/E 58%),
  idêntico a 30/08. O próximo corte é esperado segunda-feira 14/09.

**O que invalida / risco:**

- **O padrão técnico da sessão de hoje é, isoladamente, o mais preocupante para o lado
  comprado desde o início do rompimento.** Fechamento em 1.299,00, a apenas 6,00 pontos
  (0,46%) acima da mínima do dia (1.293,00) — contra máxima de 1.335,25 — um fechamento no
  quinto inferior do próprio range. Em volume de **245.874 contratos**, o maior de toda a
  janela pós-reabertura, **+62,3%** sobre os ~151.466 de ontem. A combinação "nova máxima
  seguida, no dia seguinte, de fechamento fraco perto da mínima em volume recorde" é um
  padrão técnico clássico de reversão de curto prazo (às vezes chamado de dia de
  distribuição): sugere que uma quantidade grande de contratos trocou de mãos exatamente
  no momento em que o preço virou de alta para baixa, o que pode indicar tomada de lucro
  coordenada depois de quatro sessões de alta desde a reabertura, ou o início de uma
  correção mais duradoura. Não há, nos dados disponíveis, como distinguir as duas
  hipóteses ainda — a próxima sessão (a ser negociada segunda-feira) é o teste mais
  imediato: uma continuação da queda confirmaria o padrão de reversão, enquanto uma
  recuperação rápida sugeriria que foi apenas realização de lucro pontual.
- **Crush margin segue comprimido, com pequena melhora.** Fechou em **US$ 2,2637/bushel**
  em 11/09 (indicators), ainda **-9,45%** abaixo do referencial de US$ 2,50 monitorado
  pela fila (`alerta-quebra_suporte-complexo_soja-2026-09-11`) — a 11ª sessão seguida
  abaixo do referencial, mas com a distância percentual encolhendo ligeiramente frente aos
  -9,97% de ontem.
- **Nível técnico a vigiar:** um fechamento de volta abaixo de 1.180 ainda desfaria
  formalmente o rompimento; com a folga em 10,08%, esse cenário segue distante, mas a
  margem de segurança encolheu pela primeira vez em quatro sessões.
- **O COT mais fresco (08/09) já tem três dias corridos de defasagem frente à sessão de
  hoje** — não há como saber se os fundos que ampliaram a posição comprada na semana
  anterior já começaram a vender na sessão de hoje, o que seria consistente com o padrão
  técnico de distribuição observado no preço.

**Leitura operacional:** para quem está comprado, a tendência de fundo (rompimento de
agosto, folga de 10%, fundos institucionalmente mais comprados segundo o COT de 08/09)
ainda não foi desfeita, mas o padrão técnico de hoje é o primeiro argumento genuíno para
reduzir tamanho de posição ou apertar stop, em vez de ignorar o sinal. Para quem opera o
lado vendido, hoje é o primeiro dia da janela pós-reabertura em que vale a pena reabrir
uma posição tática pequena, com stop acima da máxima de hoje (1.335,25) e alvo na
confirmação (ou não) de continuidade da queda na próxima sessão — sem, ainda, apostar
contra a tendência estrutural maior enquanto 1.180 não for ameaçado.

## Farelo

**Viés: neutro (rebaixado de bear moderado) — pela primeira vez desde a abertura da tese
de abundância em 11/06/2026, o ratio Far/Soj fechou acima de 80%, o gatilho de
invalidação definido explicitamente desde então. É um único dia, sem confirmação de COT
contemporâneo, mas o movimento veio acompanhado de TODOS os outros indicadores de
complexo na mesma direção — o que muda o peso da evidência o suficiente para tirar a
tese do território "bear confiante" e colocá-la em "neutro, sob teste".**

O que sustenta a virada (ou pelo menos a suspende a tese anterior):

- **O ratio Far/Soj cruzou para cima de 80% pela primeira vez em toda a vida da tese.**
  Fechou em **80,32%** em 11/09/2026 (indicators), ante 78,95% em 10/09 — um salto de
  **+1,37 ponto percentual**, o maior movimento diário do ratio em toda a janela
  recente. A fila de julgamento capturou esse evento como `ratio-zona-2026-09-11`,
  descrevendo a transição de zona "comprimido" (<80%, farelo abundante) para "neutro"
  (80-87%, na própria definição do indicador). O mecanismo: quando os três produtos caem
  juntos mas o farelo cai muito menos (-0,80% vs -2,50% da soja), o numerador do ratio
  (farelo) perde menos valor do que o denominador (soja), e o ratio sobe mesmo com o
  farelo em queda nominal — o espelho exato do mecanismo que vinha segurando o ratio
  abaixo de 80% desde junho. Esse cruzamento é tratado em profundidade, com todo o
  histórico da tese desde 11/06, em
  [[2026-09-12_ratio-far-soj-rompe-80-pela-primeira-vez]].
- **Os índices sintéticos, que estavam "travados" havia três sessões, se moveram na
  mesma direção do ratio — a primeira confirmação estrutural, não apenas de preço.** O
  Índice de Sobra de Farelo (ISF) caiu de **80 para 60** (indicators, 11/09: "sobra
  relevante, 3 de 5 condições", ante "forte pressão baixista, 4 de 5 condições"). As
  leituras dos últimos três dias haviam registrado, com desconfiança crescente, que nem
  quedas nem altas de preço moviam esse índice — hoje ele se moveu, o que sugere que a
  métrica realmente reage a mudanças de magnitude suficiente, não que esteja
  estruturalmente travada. Isso dá mais credibilidade ao movimento de hoje do que teria
  se fosse só o ratio de preço se movendo isolado.
- **O oil-meal spread virou negativo pela primeira vez em toda a janela do dump.** Fechou
  em **-0,0495** USD/bushel em 11/09 (indicators), ante +0,1419 em 10/09 — uma inversão de
  sinal completa. Na definição do indicador (positivo = óleo manda), um spread negativo
  significa que, na margem, o farelo está entregando mais valor por unidade dentro da
  conta do crush do que o óleo — o oposto exato da narrativa "óleo paga a conta, farelo
  sobra" que sustentou a tese de junho. É o dado mais direto de todos os citados aqui:
  não é uma leitura indireta via ratio, é a comparação de valor bruta entre os dois
  produtos, e ela mudou de sinal.
- **O oil share caiu abaixo de 50% pela primeira vez em toda a janela do dump.** Fechou em
  **49,84%** em 11/09 (indicators), ante 50,46% em 10/09 — a primeira leitura abaixo de
  50% desde pelo menos 08/09 (todas as leituras anteriores da janela estavam entre
  50,38% e 50,56%). Como farelo + óleo somam 100% por definição, isso significa
  literalmente que o farelo passou a responder por mais da metade do valor do crush
  (50,16%) pela primeira vez na janela — um detalhe estrutural que, sozinho, já seria
  notável, e que hoje aparece junto com todos os outros sinais.
- **O físico brasileiro segue completamente congelado, sem qualquer reação** — a última
  leitura disponível continua sendo 09/09 (farelo MT/IMEA R$ 1.875,45/ton, congelado desde
  04/09; prêmio export Paranaguá +0,12 USD/short ton, congelado desde 27/08, agora 16 dias
  corridos). Isso significa que, até onde os dados permitem ver, o mercado físico
  doméstico ainda não teve qualquer chance de precificar a mudança de regime sugerida
  pelos indicadores de Chicago hoje.

**Trata a fila `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
(recorrente 🔴) e `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`
(recorrente 🔴):** ambos os marcos de revisão seguem tecnicamente "vencidos" pelo sistema
de fila, mas o veredito de fundo do D+90 (entregue em profundidade em
[[2026-09-09_d90-ratio-far-soj-reverte-na-vespera]], reafirmando a tese de abundância) foi
diretamente desafiado pelo dado de hoje — o gatilho concreto de invalidação definido
naquele próprio veredito ("um fechamento acima de 80% pela primeira vez desde
11/06/2026") aconteceu agora. Este ponto é tratado com todo o histórico necessário no
insight dedicado publicado hoje,
[[2026-09-12_ratio-far-soj-rompe-80-pela-primeira-vez]], que também reavalia o D+180
(vencimento 08/12/2026) à luz deste evento.

**O que ainda pesa contra tratar isso como confirmado — e mantém o viés em "neutro", não
"bull-farelo":**

- **É um único dia de dado fresco.** O padrão desta mesma janela mostrou pelo menos duas
  aproximações de 80% (79,08% em 09/09, 79,06% também citado em leituras anteriores) que
  foram revertidas na sessão seguinte. A diferença desta vez é que o ratio não apenas se
  aproximou, fechou **acima** — um fato qualitativamente diferente — mas uma única sessão
  ainda não é uma tendência confirmada.
- **O COT mais fresco (08/09, tratando `release-cftc_cot-2026-09-08`) tem três dias
  corridos de defasagem e mostra um sinal misto, não uma confirmação clara.** O net long
  de managed money em farelo ficou praticamente estável (+0,32%, 157.179→157.689
  contratos), mas a composição mudou bastante: o short caiu -26,73% (21.004→15.390) muito
  mais do que o long caiu -2,86% (178.183→173.079) — isso é cobertura de posição vendida
  (short covering), não uma nova onda de convicção compradora entrando. Um net long
  estável construído por cobertura de venda é uma leitura mais fraca de "os fundos estão
  ficando bullish em farelo" do que seria um net long subindo por long novo entrando —
  e, de qualquer forma, esses dados são de três dias antes da sessão de hoje.
- **O WASDE de setembro (tratando `release-usda_wasde-2026-09-11`) trouxe uma revisão
  estrutural na direção oposta ao sinal de preço de hoje, ainda que pequena.** Para a
  Argentina, a projeção de exportação de farelo em 2026/27 subiu de 2,89 para **2,99
  milhões de toneladas** (USDA WASDE, edição de setembro vs agosto/2026) — uma alta de
  **+3,46%** na oferta exportável projetada de farelo argentino, o segundo maior
  exportador mundial do produto. Mais oferta projetada de farelo no mercado internacional
  é, estruturalmente, um vetor baixista de médio prazo para o preço relativo do farelo —
  o oposto do que o preço de hoje sugere no curto prazo. Para o Brasil, a mesma edição
  trouxe produção, exportação e esmagamento de farelo praticamente inalterados
  (8,0 / 0,2 / 7,1 milhões de toneladas, sem variação de agosto para setembro). Esta
  janela do dump não trouxe tabelas de soja em grão nem de óleo do WASDE de setembro — ver
  Honestidade.
- **O físico brasileiro não confirmou nada ainda** (ver acima) — se o mercado físico
  doméstico não repassar qualquer força para o farelo nos próximos dias, o movimento de
  hoje ficaria restrito ao papel em Chicago.

**Leitura operacional:** para quem está vendido em farelo (ou vendido no spread Far/Soj,
comprado em soja e vendido em farelo), hoje é o primeiro dia da tese inteira em que o
gatilho de invalidação definido desde junho efetivamente ocorreu — não é mais "quase
chegando", é um fechamento acima de 80%. A recomendação não é fechar a posição às cegas
com base em um único dia, mas reduzir tamanho e definir um critério de confirmação
explícito: um segundo fechamento consecutivo acima de 80% (o que nunca aconteceu na
janela) tornaria a invalidação muito mais robusta do que um evento isolado. Para quem
está comprado em farelo ou no spread, hoje foi a primeira confirmação de preço e
estrutura juntas a favor da posição desde a reabertura — mas ainda sem o apoio do físico
brasileiro nem de um COT contemporâneo, os dois elementos que fechariam o quadro.

## Óleo

**Viés: bear, moderado a forte — a sessão de hoje anulou por completo a narrativa de
ontem de "a 0,76% de reconquistar 72,00". O contrato caiu -3,22%, fechou a 6 centavos da
mínima do dia, o ISO recuou do teto da escala pela primeira vez em quatro sessões, e o
motor que sustentou a alta de ontem (o salto de heating oil) se desfez quase por
completo.**

O que pesa contra a tese (o quadro mais fraco do óleo desde a reabertura):

- **Queda forte, com fechamento no piso do range.** Óleo CBOT fechou em **69,11** USD
  cts/lb em 11/09/2026 (CME CBOT), **-3,22%** sobre os 71,41 de 10/09 (valor reconstruído
  via indicadores — ver Honestidade) — a maior queda diária de toda a série pós-
  reabertura, confirmada pela própria fila de julgamento
  (`alerta-movimento_forte-oleo_cbot-2026-09-11`, citando exatamente -3,22%). O contrato
  negociou entre 69,05 e 71,72 (mínima/máxima, CME CBOT) e fechou a apenas **0,06**
  acima da mínima do dia — um fechamento no piso absoluto do range, o oposto do
  fechamento forte perto da máxima observado ontem. A fila também confirma a quebra
  formal do suporte de 72,00
  (`alerta-quebra_suporte-oleo_cbot-2026-09-11`), com a distância agora em **-4,01%** —
  reabrindo a distância que havia se fechado para -0,76% ontem, e cancelando por completo
  a narrativa de "reconquista iminente" que era o ponto central da leitura de ontem.
- **O motor que sustentou a alta de ontem se desfez quase inteiramente.** O heating oil
  americano (cujo preço entra direto na receita de biodiesel) fechou em **4,7792
  USD/galão** (CME NYMEX, 11/09), com máxima do dia em apenas 4,9344 — devolvendo a maior
  parte do salto de aproximadamente +7% registrado na sessão de ontem. Como consequência
  direta, a margem de biodiesel americana recuou de US$ 2,0667/galão para **US$
  1,961/galão** (indicators, 11/09) — uma queda de **-5,11%**, o primeiro recuo depois de
  dois recordes consecutivos da série (08→09/09 e 09→10/09). O mecanismo de fundo: a
  leitura de ontem já havia registrado, na seção Honestidade, que "não há, nos dados
  disponíveis, nenhuma notícia ou evento específico que explique o tamanho do movimento"
  do heating oil — essa dúvida sobre sustentabilidade se confirmou como preocupação
  válida em apenas uma sessão, o que é um lembrete importante de que picos de um único
  dia sem justificativa fundamental identificada tendem a reverter.
- **O Índice de Suporte do Óleo (ISO) recuou do teto da escala pela primeira vez em
  quatro sessões.** Caiu de **100 para 80** (indicators, 11/09: "óleo domina o crush, 4 de
  5 condições", ante "5 de 5 condições" nos três dias anteriores). Diferente do ISF do
  farelo (que também se moveu hoje, mas de forma mais acentuada, de 80 para 60), o ISO
  ainda está em um nível historicamente alto (80/100) — a leitura aqui é de
  enfraquecimento da força estrutural do óleo, não de reversão completa.
- **Oil share e oil-meal spread confirmam a perda de força relativa do óleo dentro do
  crush.** O oil share caiu de 50,46% para **49,84%** — a primeira leitura abaixo de 50%
  em toda a janela do dump (ver seção Farelo para o detalhe). O oil-meal spread virou de
  +0,1419 para **-0,0495** USD/bushel — a primeira leitura negativa da janela, ou seja, o
  óleo passou a "pagar menos" que o farelo dentro da conta do crush pela primeira vez
  desde pelo menos 08/09.
- **O custo do insumo caiu junto com o preço, mas não o suficiente para segurar a
  margem.** O custo do óleo como insumo de biodiesel caiu para US$ 5,1833/galão (7,5 lb ×
  69,11 cts/lb), ante US$ 5,3558 em 10/09 — uma queda de -3,22%, coerente com a própria
  queda do óleo em Chicago. Mas a receita caiu ainda mais rápido (a queda do heating oil
  foi maior em termos absolutos do que a queda do custo do óleo), e o resultado líquido
  foi a margem menor descrita acima.

**O que ainda sustenta algum piso para a tese, e não deve ser ignorado:**

- **A curva futura de médio prazo do óleo segue precificando um patamar acima do contrato
  próximo.** Set/26 70,66 → out/26 (base) 69,11 → dez/26 69,61 → jan/27 69,90 → mar/27
  70,11 → mai/27 70,18 (CME CBOT, 11/09) — o contrato-base de outubro está, pela primeira
  vez na janela, abaixo até do contrato de setembro (70,66), uma leve inversão na ponta
  curtíssima da curva que pode refletir tanto ajuste técnico pontual quanto uma real
  reprecificação de curto prazo; os contratos mais distantes (dez/26 em diante) seguem
  acima do contrato-base, sugerindo que o mercado futuro trata a queda de hoje como algo
  a ser parcialmente recuperado no médio prazo, não como um novo patamar permanente.
- **O RIN D4 segue estável** — 1,5×RIN = 2,11 USD/galão embutido no cálculo de receita em
  11/09 (indicators), sem novidade regulatória; toda a queda de margem de hoje veio do
  heating oil, não de mudança no arcabouço de crédito.
- **O COT de 08/09 já mostrava os fundos reduzindo exposição líquida ao óleo antes desta
  queda** (net long -8,13%, 99.823→91.711 contratos, CFTC COT — ver seção Spreads), o que
  significa que parte do ajuste de posicionamento já estava em curso antes da sessão de
  hoje, não é uma surpresa completa de posicionamento.

**Leitura operacional:** para quem está vendido em óleo direcional, hoje foi o melhor dia
da série pós-reabertura — preço caindo com força, fechamento no piso do range, ISO
recuando do teto pela primeira vez, e o principal motor de alta (heating oil) se
desfazendo. O nível de -4,01% abaixo de 72,00 volta a ser o gatilho técnico mais
distante em vez do mais próximo. Para quem está comprado em óleo direcional, a tese
perdeu força significativamente: o argumento que resta é quase inteiramente a curva
futura de médio prazo (que segue acima do contrato-base) e o RIN D4 estável, não mais o
preço ou a margem americana de curtíssimo prazo. Para quem opera o spread farelo-óleo
dentro do crush, hoje foi o dia mais favorável ao farelo (e mais desfavorável ao óleo) de
toda a janela — reforçando a leitura de "neutro" para farelo e "bear" para óleo como as
duas pontas da mesma realocação de valor dentro do complexo.

## Spreads e crush (leitura de complexo)

A sessão de hoje foi a primeira, desde a reabertura, em que os três produtos do complexo
caíram juntos — mas, como em toda leitura de complexo, o que importa não é a direção
comum, é a velocidade relativa, e hoje essa velocidade relativa girou com clareza a favor
do farelo e contra o óleo. Farelo -0,80%, soja -2,50%, óleo -3,22% (CME CBOT, 11/09) — a
ordem de queda é exatamente invertida frente ao padrão observado em quase todas as
sessões anteriores da janela, nas quais o óleo tipicamente liderava os movimentos (para
cima ou para baixo) e o farelo seguia com menor amplitude. O resultado agregado: ratio
Far/Soj **80,32%** (+1,37 p.p., a maior variação diária da janela e o primeiro fechamento
acima de 80% desde 11/06/2026), oil share **49,84%** (primeira leitura abaixo de 50% da
janela), oil-meal spread **-0,0495** USD/bushel (primeira leitura negativa da janela), ISF
**60/100** (caindo de 80, primeira mudança em quatro sessões) e ISO **80/100** (caindo de
100, primeira mudança em quatro sessões). Cinco indicadores diferentes, calculados de
formas distintas a partir dos mesmos três preços, todos se movendo na mesma direção no
mesmo dia — isso é uma coincidência estrutural, não uma leitura isolada de um único
número, e é o principal motivo desta leitura para tratar o dia de hoje com mais peso do
que as aproximações anteriores de 80% que foram revertidas rapidamente.

O crush margin fechou em **US$ 2,2637/bushel** (11/09, indicators), uma alta de +0,80%
sobre 10/09, e segue a 11ª sessão consecutiva abaixo do referencial de US$ 2,50
monitorado pela fila (`alerta-quebra_suporte-complexo_soja-2026-09-11`), com a distância
percentual encolhendo de -9,97% para -9,45%. A pequena melhora veio da combinação: a
soja caiu mais forte (-2,50%) do que farelo (-0,80%) e óleo (-3,22%) somados ao custo
retirado do numerador — um mecanismo parecido com o observado em sessões anteriores em
que a queda do insumo (soja) supera a queda dos produtos, aliviando ligeiramente a
margem mesmo em um dia de preços em baixa generalizada.

O COT de 08/09 (tratando `release-cftc_cot-2026-09-08`, a primeira atualização desde
01/09) chega tarde demais para confirmar ou contradizer diretamente a reversão de hoje,
mas oferece um pano de fundo relevante: na semana que antecedeu esta sessão, os fundos
(managed money) ampliaram fortemente a convicção compradora em soja (net long +9,51%,
234.920→257.258 contratos, com long subindo mais que short — dinheiro novo, não apenas
cobertura), reduziram a convicção compradora em óleo (net long -8,13%, 99.823→91.711,
com short subindo +17,14% — os fundos já estavam ficando mais cautelosos com o óleo antes
da queda de hoje) e mantiveram o net long em farelo praticamente estável, mas via
cobertura de posição vendida, não via long novo (+0,32% no net, com short caindo -26,73%
e long caindo -2,86%). Ou seja: já havia, três dias antes da sessão de hoje, um sinal de
que os fundos estavam ficando relativamente menos otimistas com óleo do que com soja e
farelo — uma pista que, em retrospecto, é consistente com a direção da reversão de hoje
no óleo, ainda que não a explique por completo (a queda de soja hoje contradiz o apetite
comprador crescente do COT de 08/09, um ponto de tensão que só um corte mais fresco
resolveria).

Do lado dos fundamentos brasileiros de médio prazo (ABIOVE, projeções mensais para
set-dez/2026, sem revisão nesta janela), o balanço projetado continua mostrando o
esvaziamento sazonal esperado: estoque final de soja recuando de 7.912 mil toneladas
(set/26) para 1.890 mil toneladas (dez/26), a produção de farelo caindo de 2.129 para
1.659 mil toneladas no mesmo período, e a exportação de farelo recuando de 1.100 para 700
mil toneladas — uma trajetória que, se confirmada, tende a aliviar a oferta doméstica de
farelo ao longo do próximo trimestre, um vetor estrutural de médio prazo que **não**
aponta na mesma direção que o cruzamento do ratio acima de 80% de hoje (que seria mais
consistente com farelo ficando mais escasso/caro, não mais abundante). Essa tensão entre
o dado de preço de hoje e a trajetória de balanço da ABIOVE é registrada aqui como um
ponto de atenção, não resolvida — o insight dedicado
[[2026-09-12_ratio-far-soj-rompe-80-pela-primeira-vez]] trata essa tensão com mais
profundidade.

## Lente fiscal/regulatória BR

Antes de fechar qualquer tese de preço BR, os vetores tributários/regulatórios vivos que
pesam no complexo — todos do `system/tributario_watch.toml`, cujo carimbo mais recente
(`atualizado_em`) em todos os 10 eventos catalogados é 2026-06-05, ou seja, **99 dias sem
revisão humana** frente a hoje (12/09):

- **MP 1.363/2026** (id `MP-1363-2026`, subvenção diesel fóssil R$ 1,12/L, vigente até
  31/12/2026): barateia o diesel fóssil no mix B15 (mistura obrigatória de 15% de
  biodiesel no diesel vendido no Brasil), reduzindo a competitividade relativa do
  biodiesel e a demanda doméstica por óleo de soja — vetor estrutural de baixa para óleo,
  sem mudança de status. Este vetor reforça, não contradiz, o viés bear-óleo desta
  leitura, ainda que por um mecanismo (regulatório doméstico BR) completamente diferente
  do que derrubou o óleo hoje (reversão do heating oil americano).
- **B16 (id `B16-CNPE-2026`, elevação da mistura obrigatória de biodiesel para 16%)**
  segue "adiado" — resultado dos testes técnicos esperado por volta de novembro/2026.
  Upside represado (~436 mil toneladas de demanda potencial adicional de óleo), não
  corrente. Com o oil share caindo abaixo de 50% e o ISO recuando do teto hoje, um
  estímulo futuro de demanda por óleo via B16 encontraria, se e quando chegar, um cenário
  estrutural mais fraco para o óleo do que o observado nas sessões anteriores — o upside
  represado do B16 fica, relativamente, mais importante quanto mais fraco o quadro
  corrente do óleo.
- **Isenção de PIS/Cofins do biodiesel na mistura** (id `PISCOFINS-BIODIESEL-ISENCAO`):
  vigência registrada até 31/07/2026 — já **43 dias corridos vencida** frente a
  12/09/2026, sem qualquer registro de prorrogação ou expiração no arquivo. Status
  tratado como "desconhecido pós-vigência", não como fato de vigência ou caducidade.
- **MP 1.358/2026** (subvenção gasolina R$ 0,89/L): vigência registrada até 11/07/2026,
  agora **63 dias corridos vencida**, mesma lacuna de informação sobre renovação.
- **STJ REsp 2.165.276** (id `STJ-RESP-2165276`, crédito de PIS/Cofins sobre soja em
  biodiesel sob suspensão tributária, direção "alta" para soja/óleo): alívio de custo
  pontual, não vinculante, sem novidade nesta janela.
- **EPA RFS 2026/2027** (id `EPA-RFS-2026-2027`, mandato de biocombustível americano,
  vigente desde 15/06/2026, direção "alta" para óleo): sustenta o RIN D4, estável — o
  arcabouço regulatório segue intacto; a queda de margem de hoje foi 100% heating oil, não
  qualquer risco de mudança de crédito.
- **Crédito 45Z** (id `45Z-CLEAN-FUEL`, em tramitação, direção "mista"): sem novidade.
- **Indonésia — Danantara** (id `DANANTARA-INDONESIA`) e **levy de exportação PMK
  9/2026** (id `INDONESIA-LEVY-PMK9`): a assunção plena da centralização da exportação de
  palma pela Indonésia tinha alvo 01/09/2026 — já se passaram **11 dias** sem qualquer
  notícia neste dump confirmando execução. Catalisador de alta represado para óleo (via
  substituição com palma), não invalidado nem confirmado.
- **Indonésia B50** (id `INDONESIA-B50`, monitorando, direção "alta"): sem novidade nesta
  janela.

## Riscos e eventos próximos

- **Confirmação (ou não) do fechamento acima de 80% no ratio Far/Soj na próxima sessão**
  — é, hoje, o gatilho mais importante de todo o complexo. Um segundo fechamento seguido
  acima de 80% tornaria a mudança de regime muito mais robusta; uma reversão de volta
  para baixo de 80% reduziria o evento de hoje a mais uma aproximação revertida, como já
  aconteceu duas vezes nesta janela.
- **O COT de 08/09 já está três dias corrido atrasado frente ao preço** — o próximo corte
  (posições de 15/09, esperado por volta de 18/09) é o primeiro que poderá confirmar se os
  fundos reagiram à reversão de hoje ampliando posição vendida em óleo/farelo relativo, ou
  se trataram como ruído.
- **Reação (ou ausência de reação) do físico brasileiro de farelo e óleo**, congelado
  desde 09/09 (farelo) e 27/08 (prêmios export) — se o movimento de Chicago de hoje for
  genuíno, alguma reação no físico nos próximos dias seria esperada; a ausência dela
  seguiria sendo um sinal de que o mercado doméstico não compartilha (ainda) da leitura de
  Chicago.
- **Confirmação (ou reversão adicional) do heating oil americano** — depois de saltar +7%
  em uma sessão e devolver quase tudo na seguinte, uma terceira sessão de volatilidade
  extrema tornaria ainda mais difícil separar sinal de ruído nesse mercado correlato.
- **USDA Crop Progress semanal**: próximo corte esperado segunda-feira 14/09.
- **USDA WASDE de setembro**: esta janela trouxe apenas a tabela de farelo Argentina/
  Brasil; tabelas de soja em grão, óleo e EUA ainda não apareceram nesta janela do dump —
  monitorar se aparecem nos próximos dias, pois mudariam a leitura de balanço mundial.
- **NOPA mensal** (`release-nopa-2026-09-11`): quinto dia seguido do mesmo falso positivo
  de paywall na fila — o gap de dado de crush americano segue sem solução.
- **Confirmação (ou não) da centralização plena da exportação de palma pela Danantara**
  — marco-alvo era 01/09, já se passaram 11 dias.
- **Vigência da isenção PIS/Cofins do biodiesel** (43 dias vencida) e **MP 1.358/2026 da
  gasolina** (63 dias vencida) — checar notícia de renovação/expiração antes de assumir
  qualquer tese de custo de combustível BR.
- **Clima**: previsão de 12/09 (hoje) mantém calor forte em Mato Grosso (37-39°C de
  máxima) com chuva isolada, e chuva/trovoadas no Sul sem menção de geada — pano de fundo
  para a janela de plantio da safra 2026/27 que se aproxima, ainda sem impacto direto
  sobre a soja em si (ainda não plantada na região).
- **Sinal técnico de reversão em soja** (fechamento perto da mínima em volume recorde) —
  a próxima sessão (segunda-feira) é o teste mais imediato de continuidade ou não do
  padrão.

## Honestidade

- **O dump de hoje não contém as linhas brutas de CME CBOT para soja e óleo na data de
  10/09** — apenas farelo e heating oil (parcialmente) têm linha própria de preço para
  aquele dia. Os valores de soja (1.332,25) e óleo (71,41) usados como base de comparação
  nesta leitura foram reconstruídos a partir das fórmulas dos indicadores sintéticos de
  10/09 (`complexo_soja.crush_margin_usd_bu` e `biodiesel_us.custo_oleo_usd_galao`), não
  de uma linha de preço bruta própria — o mesmo tipo de gap identificado pelas duas
  últimas leituras diárias, agora recaindo sobre a data de 10/09. Isso introduz uma
  pequena margem de erro (histórico de 0,1-0,3% de divergência entre reconstrução e linha
  bruta observada em dias anteriores) nas variações percentuais de hoje que usam 10/09
  como base — não muda nenhuma conclusão direcional, mas é registrado por transparência.
- **A linha bruta de heating oil de 11/09 tem uma inconsistência interna**: o campo
  "abertura" (5,1481) está acima da própria "máxima" (4,9344) do dia, o que é
  logicamente impossível para uma série de preço bem formada (a máxima deveria ser maior
  ou igual à abertura). O valor de abertura muito provavelmente reflete o fechamento do
  pregão anterior carregado por um artefato de coleta, não o primeiro preço negociado na
  sessão de 11/09. Por isso, esta leitura não usa o campo "abertura" para calcular a
  variação percentual do heating oil no dia, apoiando-se em vez disso nos valores de
  receita/custo/margem já calculados pelos indicadores sintéticos (que são internamente
  consistentes) para descrever a queda da margem de biodiesel.
- **O WASDE de setembro (`release-usda_wasde-2026-09-11`) está incompleto nesta janela do
  dump** — contém apenas a tabela de farelo (meal) de Argentina e parcialmente Brasil e
  China, comparando as edições de agosto e setembro/2026. Não há, nesta janela, tabelas de
  soja em grão, óleo de soja, nem dados dos EUA (o maior produtor/exportador). A leitura
  do WASDE nesta seção fica, portanto, restrita ao fragmento disponível — qualquer
  conclusão de balanço mundial mais amplo exigiria as tabelas que não apareceram aqui.
- **O COT de 08/09 tem três dias corridos de defasagem frente à sessão de hoje (11/09)** —
  não há como confirmar se a posição dos fundos mudou entre 08/09 e 11/09 em resposta à
  reversão de preço desta sessão. O próximo corte semanal do CFTC é esperado por volta de
  18/09.
- **Percentil histórico de posicionamento COT não está disponível no briefing** — toda
  leitura de "fundos comprando/vendendo" usa variação semana a semana de contratos
  absolutos, não percentil histórico.
- **A magnitude "certa" de movimento necessária para deslocar o ISF/ISO permanece
  desconhecida** — hoje, pela primeira vez, um movimento de preço grande o bastante moveu
  ambos os índices (de 80→60 e 100→80, respectivamente), mas não há, nos dados
  disponíveis, uma fórmula exposta que permita calcular antecipadamente qual variação de
  preço seria necessária para repetir esse movimento.
- **`tributario_watch.toml` sem atualização há 99 dias** — pelo menos dois vetores
  (isenção PIS/Cofins do biodiesel, MP 1.358/2026) já passaram da data de vigência
  registrada sem nota de renovação ou expiração. Tratados como "status desconhecido
  pós-vigência", não como fato de caducidade real.
- **NOPA segue inacessível** (paywall) — nova "release" carimbada em 11/09 é o quinto
  falso positivo seguido na fila, sem dado novo de fato.
- **A ausência de itens de notícia em 10/09 e 11/09 ("0 items lidos, 0 mantidos")** é
  registrada como uma falha ou pausa de coleta da fonte RSS nesses dois dias, não como
  ausência real de notícia relevante no mercado.
- **A previsão INMET para 12/09 é previsão meteorológica, não medição de precipitação
  real** — a ausência de menção a "geada" no boletim de hoje para Passo Fundo/RS é
  tratada como sinal indicativo, não como confirmação de que a geada efetivamente cessou.
- **Prêmios de exportação (Paranaguá, farelo e óleo) e o físico de Paraná/Paranaguá
  seguem sem atualização própria desde 09/09** — não é possível afirmar se isso reflete
  mercado físico genuinamente parado ou apenas defasagem normal de publicação da fonte
  (NAG/CEPEA).
- **MPOB (palma Malásia) segue com parser quebrado** — nenhum dado de produção/estoque de
  palma malaia disponível para cruzar com a tese de substituição via Indonésia.
- **BCBA (Argentina) segue sem links de relatório detectados pelo scraper** — nenhum dado
  de safra ou exportação argentina disponível nesta janela.
- **Os forecasts estatísticos internos (bandas 7d/30d) foram gerados sobre o fechamento
  de 11/09**, ou seja, já incorporam a queda de hoje como novo ponto de partida — mas o
  viés "altista" atribuído a todos os três produtos nesses forecasts reflete
  extrapolação estatística de tendência recente (MA20 + volatilidade + slope), não uma
  reavaliação fundamentalista da reversão observada hoje; tratado aqui como referência
  estatística, não como leitura própria desta análise.
- **A fila de julgamento continua listando os dois itens de revisão do ratio Far/Soj
  (D+7 e D+90) como "vencidos" pela quinta vez seguida**, mesmo com o D+90 já tratado em
  profundidade em 09/09 — isso parece ser, como observado em leituras anteriores, um eco
  do sistema de geração de fila que não lê de volta os insights já escritos para marcar a
  revisão como encerrada. Tratado aqui como continuidade do mesmo veredito, com o
  desenvolvimento mais importante desde então (o cruzamento do ratio acima de 80%)
  registrado no insight dedicado publicado hoje.
