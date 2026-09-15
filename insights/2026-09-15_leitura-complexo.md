---
data: 2026-09-15
titulo: "O ratio Far/Soj fecha acima de 80% pela TERCEIRA sessão consecutiva (80,46% hoje, após 80,25% em 11/09 e 80,55% em 14/09) — a confirmação mais robusta desde a abertura da tese de junho de que o farelo deixou o regime de 'abundância' —, mas a sessão de hoje negociou com volume anormalmente baixo em toda a curva CBOT, o que exige tratar os fechamentos com cautela redobrada; soja segue firme acima da resistência de 1.180 mesmo após um recuo de -0,52%, e o óleo permanece abaixo do suporte de 72,00 com a margem de biodiesel americana recuperando parte do tombo de segunda-feira"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT — sessão de 2026-09-15 (terça-feira, a mais recente): soja (ZSX26, venc. nov/26) abertura 1.303,25, máxima 1.303,50, mínima 1.298,00, fechamento **1.298,25** USD cts/bushel, volume **2.379** contratos; farelo (ZMV26, venc. out/26) abertura 350,30, máxima 350,30, mínima 348,10, fechamento **348,20** USD/short ton, volume **479** contratos; óleo (ZLV26, venc. out/26) abertura 69,62, máxima 69,62, mínima 69,24, fechamento **69,50** USD cts/lb, volume **1.045** contratos. Curva futura em 15/09 — soja: nov/26 (base) 1.298,25, jan/27 1.314,25, mar/27 1.322,00, mai/27 1.329,00, jul/27 1.332,50; farelo: out/26 (base) 348,20, dez/26 354,40, jan/27 356,00, mar/27 356,70, mai/27 357,30; óleo: out/26 (base) 69,50, dez/26 70,03, jan/27 70,28, mar/27 70,42, mai/27 70,46
  - CME CBOT — sessão de 2026-09-14 (segunda-feira, primeiro pregão após o fim de semana): soja fechamento **1.305,00** (+0,66% vs 11/09), farelo fechamento **350,40** (+1,04% vs 11/09), óleo fechamento **69,62** (+0,62% vs 11/09) — closes tomados da tabela de `indicators` (crush margin, ratio) de 14/09, que permanecem idênticos entre a geração de ontem e a geração de hoje do briefing; ver Honestidade para a ressalva sobre os campos de abertura/máxima/mínima/volume de farelo e sobre a ausência de linhas brutas de soja/óleo para 14/09 nesta janela
  - CME NYMEX heating oil (HO=F) — 2026-09-15: abertura 4,7604, máxima 4,8196, mínima 4,7604, fechamento **4,8126** USD/galão, volume **510** contratos (+0,72% vs fechamento de 4,7780 em 14/09)
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, ISF, ISO, margem biodiesel, paridade BR) — 2026-09-15: crush margin **2,3229** USD/bushel, far_soj_ratio_pct **80,46%**, oil_share_pct **49,95%**, oil_meal_spread_usd_bu **-0,0154**, ISF (Índice de Sobra de Farelo) 60/100, ISO (Índice de Suporte do Óleo) 80/100, paridade BR soja **R$147,96/saca** (usando USD/BRL 5,1696, mesma PTAX de 14/09 — ver Honestidade), biodiesel: custo_óleo 5,2125 USD/galão, receita 7,9776 USD/galão, margem **1,9651** USD/galão. Comparação com 14/09: crush margin 2,317, ratio 80,55%, oil share 49,84%, oil-meal spread -0,0506, paridade R$148,73, margem biodiesel 1,9215. Comparação com 11/09: crush margin 2,2755, ratio 80,25%, oil share 49,94%, oil-meal spread -0,0187, margem biodiesel 2,135
  - BCB PTAX — última leitura ainda **2026-09-14**: USD/BRL 5,1696 (+1,53% vs 5,0918 de 11/09, sexta-feira — item de fila `alerta-movimento_forte-usd_brl_ptax-2026-09-14`), EUR/BRL 5,9704, Selic diária 0,05166% a.a. (séries SGS 1, 21619, 11); sem PTAX própria de 15/09 disponível nesta janela — ver Honestidade
  - CFTC COT Managed Money — corte de 2026-09-08, agora **sete dias corridos** de defasagem frente à sessão de hoje (15/09): farelo net long 157.689 contratos, óleo net long 91.711 contratos, soja net long 257.258 contratos — sem qualquer atualização desde a leitura de 13/09; ver seção Spreads e Honestidade
  - CEPEA/ESALQ Soja Paranaguá e Paraná interior via NAG, e físico de farelo (MT/IMEA, Rondonópolis, RS) — última leitura ainda **2026-09-09**, agora **6 dias corridos** sem atualização própria; prêmios export Paranaguá (farelo +0,12 USD/short ton, óleo +0,10 cts/lb) seguem congelados desde 27/08, **19 dias corridos**
  - USDA Crop Progress — corte de 2026-09-13: 12% excelente / 46% boa / 9% ruim (G/E 58%, inalterado desde 30/08), e pela primeira vez nesta janela do dump um número de **colheita: 6% concluída** (pct_harvested) — a safra americana 2025/26 começou a ser colhida
  - USDA WASDE — release de 2026-09-11 (sem nova edição nesta janela), tratando novamente `release-usda_wasde-2026-09-11`: farelo Argentina 2026/27 com exportação revisada de 2,89 para 2,99 milhões de toneladas (ago vs set), farelo Brasil praticamente estável; sem tabelas de soja em grão nem de óleo nesta janela
  - NOPA — fila `release-nopa-2026-09-15` (novo carimbo, mesmo conteúdo): `monthly_status` seguiu em 0,0 bool (paywall)
  - ABIOVE projeções mensais — balanços set-dez/2026, sem revisão nesta janela: produção de farelo recuando de 2.129 (set) para 1.659 mil t (dez), exportação de 1.100 para 700 mil t no mesmo período
  - NOAA CPC ENSO — El Niño Advisory, inalterado até 2026-09-15
  - MPOB — carimbo 2026-09-15, parser sem números extraídos (mesma barreira, 3.457 caracteres)
  - BCBA (Argentina) — carimbo 2026-09-09, scraper acessa a página mas não encontra links de relatório
  - INMET — previsão para **2026-09-15 (HOJE)**: retorno de temperaturas mais amenas frente ao resfriamento de 13/09 no Sul — Cascavel/PR 22°C/11°C (ante 19°C/13°C em 13/09), Maringá/PR 21°C/14°C, Passo Fundo/RS 19°C/8°C (sem menção de geada); no núcleo produtor de Mato Grosso, calor voltando a subir — Cuiabá 30°C/17°C, Sinop e Sorriso 36°C/19°C (ambos "muitas nuvens com chuva isolada"), Lucas do Rio Verde 36°C/19°C, Rio Verde/GO 33°C/21°C (com pancadas de chuva e trovoadas isoladas)
  - Notícias Agrícolas/Canal Rural + FarmProgress RSS — "0 items lidos, 0 mantidos" segue desde 10/09, agora **6 dias corridos** seguidos de falha ou pausa de coleta
  - system/tributario_watch.toml (lido como referência, não editado) — `atualizado_em` 2026-06-05 em todos os 10 eventos catalogados, **102 dias corridos** sem revisão humana frente a hoje (15/09)
  - Forecasts estatísticos internos (bandas 7d/30d) — geração de 2026-09-15, alvos 22/09 (7d) e 15/10 (30d); viés "altista" em soja e farelo nos dois horizontes, "lateral" em óleo no horizonte de 7d — calculado sobre o fechamento de hoje, ver Honestidade
  - Fila de julgamento (carimbada 2026-09-15 no briefing, 8 itens) — tratados nesta leitura: `alerta-quebra_resistencia-soja_cbot-2026-09-15`, `alerta-quebra_suporte-oleo_cbot-2026-09-15`, `alerta-quebra_resistencia-farelo_cbot-2026-09-15`, `alerta-movimento_forte-usd_brl_ptax-2026-09-14`, `alerta-quebra_suporte-complexo_soja-2026-09-15`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`, `release-nopa-2026-09-15`
  - Cruza com [[2026-09-13_leitura-complexo]] (última leitura diária publicada, que corrigiu os números da sessão de 11/09), [[2026-09-13_correcao-numeros-sessao-11set-farelo-oleo]] (auditoria numérica), [[2026-09-12_ratio-far-soj-rompe-80-pela-primeira-vez]] (primeiro fechamento acima de 80%, com os critérios de confirmação que a sessão de hoje agora satisfaz), [[2026-09-09_d90-ratio-far-soj-reverte-na-vespera]] (veredito D+90) e [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (tese original) — e com o insight dedicado publicado hoje, [[2026-09-15_ratio-far-soj-terceira-sessao-consecutiva-acima-80]]
status: ativa
vies: [bull-soja, neutral-farelo, bear-oleo_soja]
---

## Visão geral

Hoje, terça-feira 15/09/2026, a CBOT (bolsa de grãos e derivados de Chicago, onde soja,
farelo e óleo de soja são negociados em contratos futuros) teve sua segunda sessão desde
a virada de fim de semana, depois da sexta-feira 11/09 e da segunda-feira 14/09. O
complexo segue no meio do mesmo mecanismo de sempre: a soja em grão, ao ser esmagada
("crush", o processo industrial que a separa em farelo e óleo), vira dois produtos com
demandas muito diferentes — farelo (concentrado de proteína para ração animal) e óleo
(alimentação humana e, cada vez mais, biodiesel). O "crush margin" mede, em dólares por
bushel (unidade agrícola americana de ~27,2 kg de soja), quanto sobra para a esmagadora
depois de vender farelo + óleo e pagar a soja. O "oil share" (fatia do valor total do
crush que vem do óleo) diz qual dos dois produtos está "pagando a conta": alto = óleo
manda e o farelo vira subproduto barato (o "Índice de Sobra de Farelo", ISF, capta isso do
lado baixista do farelo); baixo = o farelo sustenta o crush e o óleo perde força relativa
(o "Índice de Suporte do Óleo", ISO, é o espelho). O ratio Far/Soj (preço do farelo
dividido pelo da soja, normalizado em percentual) mede a mesma ideia de forma mais direta:
abaixo de 80% o farelo está "abundante" (viés baixista); entre 80% e 87% ele está em zona
"neutra"; acima de 87% fica "apertado" (viés altista).

O fato mais importante desta leitura é este: o ratio Far/Soj fechou hoje em **80,46%**
(indicators, 15/09) — depois de 80,25% na sexta-feira 11/09 e 80,55% na segunda-feira
14/09. São **três fechamentos consecutivos acima de 80%**, algo que nunca havia
acontecido nos mais de 90 dias corridos desde a abertura da tese de abundância de farelo
em 11/06/2026 ([[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]). O insight
dedicado publicado em 12/09
([[2026-09-12_ratio-far-soj-rompe-80-pela-primeira-vez]]), quando o ratio cruzou 80% pela
primeira vez, definiu explicitamente o que faltava para tratar aquele evento como
confirmação de mudança de regime, não apenas um "toque e recuo" como as duas aproximações
anteriores (79,76% em 04/09 e 79,06%/79,08% em 09/09, ambas revertidas na sessão
seguinte): "um segundo fechamento consecutivo acima de 80%... seria o primeiro sinal de
que isso não é apenas um evento de um dia". Esse critério foi satisfeito na segunda-feira
e reforçado hoje com um terceiro. Este ponto é desenvolvido com todo o peso que merece em
um insight separado publicado hoje,
[[2026-09-15_ratio-far-soj-terceira-sessao-consecutiva-acima-80]], que também trata em
profundidade os dois itens de fila `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
e `-D+90` (ambos recorrentemente listados como "vencidos" pelo sistema, um eco da fila que
não lê de volta os insights já escritos, como observado em leituras anteriores).

Mas há uma segunda camada, igualmente importante, que impede tratar esses três dias como
prova definitiva: **a sessão de hoje negociou com volume anormalmente baixo em toda a
curva CBOT** — soja apenas 2.379 contratos (frente a uma média histórica de 100-160 mil
nesta mesma janela), farelo 479 contratos (frente a 20-30 mil), óleo 1.045 contratos
(frente a 17-32 mil) e heating oil 510 contratos. Não há feriado americano conhecido em
15/09/2026 que justifique um pregão tão fino, e o padrão de volume nos últimos dias já
vinha instável (heating oil, por exemplo, negociou 62.190 contratos em 11/09, 1.727 em
13/09 e valores residuais nos dias seguintes). A leitura mais prudente é que o dump de
hoje capturou uma fatia parcial da sessão (não a liquidação plena do dia), não que o
mercado genuinamente parou de negociar — mas, na dúvida, os fechamentos de hoje devem ser
tratados com um desconto de confiança extra até a próxima geração do briefing confirmar ou
corrigir esses números (o mesmo padrão de cautela que se provou necessário na auditoria de
13/09, [[2026-09-13_correcao-numeros-sessao-11set-farelo-oleo]], quando números de uma
sessão anterior precisaram ser corrigidos). Esta leitura detalha o achado com mais peso na
seção Honestidade.

Do lado do preço absoluto, os três produtos deram uma pequena "respirada" hoje depois do
salto de segunda-feira: soja recuou -0,52% (de 1.305,00 para 1.298,25), farelo recuou
-0,63% (de 350,40 para 348,20) e óleo recuou apenas -0,17% (de 69,62 para 69,50) — todos
CME CBOT, 15/09. É um recuo pequeno e ordenado, não uma reversão de tendência: a soja
segue **10,02%** acima da resistência de referência de 1.180,00 (fila
`alerta-quebra_resistencia-soja_cbot-2026-09-15`), o farelo segue **7,14%** acima da
resistência de 325,00 (`alerta-quebra_resistencia-farelo_cbot-2026-09-15`), e o óleo segue
**-3,47%** abaixo do suporte de 72,00 (`alerta-quebra_suporte-oleo_cbot-2026-09-15`).
Somando as três sessões desde sexta-feira (11→15/09), o saldo líquido é levemente positivo
em todos os três produtos (soja +0,13%, farelo +0,40%, óleo +0,45%), o que sugere
consolidação lateral em patamar mais alto, não reversão do movimento de alta que dominou a
reabertura de 08/09.

**Leitura de uma linha**: o pivô do complexo continua sendo a realocação de valor entre
farelo e óleo dentro do crush, e pela primeira vez desde junho essa realocação tem três
dias seguidos de confirmação de preço (ratio, oil share e oil-meal spread todos na mesma
direção nas três sessões) — mas o volume anormalmente baixo de hoje, a ausência de COT
contemporâneo (sete dias corridos de defasagem) e o físico brasileiro ainda congelado (seis
dias) seguem impedindo que essa confirmação vire convicção plena. Confiança **moderada**,
com uma ressalva metodológica nova e relevante sobre a qualidade do dado de hoje.

## Soja

**Viés: bull, moderado (mantido) — a folga sobre a resistência de 1.180 segue larga
(10,02%) e o padrão técnico de reversão que preocupava a leitura de 13/09 não se
confirmou: a sessão de segunda-feira rompeu a tendência de baixa com um fechamento forte
perto do topo do range, e o recuo de hoje é pequeno e ordenado, não uma retomada da
reversão.**

O que sustenta a tese:

- **A sessão de 14/09 respondeu ao teste anunciado pela leitura anterior — e respondeu a
  favor da alta.** A leitura de 13/09
  ([[2026-09-13_leitura-complexo]]) havia identificado a sessão de 11/09 como um
  fechamento perigosamente perto da mínima do dia (apenas 0,27% acima do piso do range) e
  apontou a segunda-feira 14/09 como "o teste mais imediato de continuidade (ou não) do
  sinal técnico de reversão". O resultado: soja abriu em 1.296,75, foi a 1.309,75 de
  máxima e a 1.292,00 de mínima, fechando em **1.305,00** (CME CBOT, 14/09) — um
  fechamento a apenas 1,04% da máxima do dia, no oitavo superior do próprio range. É o
  oposto exato do padrão de distribuição observado na sexta-feira: o mercado testou a
  fraqueza no início do pregão (mínima abaixo da abertura) e foi comprado agressivamente
  até o fechamento. Isso invalida, na prática, o sinal de reversão que vinha sendo
  monitorado havia dois dias.
- **A sessão de hoje (15/09) é uma pausa pequena e ordenada, não uma continuação de
  baixa.** Fechou em **1.298,25** (CME CBOT), -0,52% frente a 14/09, com abertura em
  1.303,25, máxima de 1.303,50 e mínima de 1.298,00 — um range de apenas 5,50 pontos
  (0,42% do preço), o mais estreito de toda a janela recente. O fechamento ficou
  praticamente na mínima do dia (0,25 ponto acima), mas dentro de um range tão apertado
  que isso tem pouco peso técnico por si só — a informação mais relevante do dia é a
  ausência de amplitude, não a posição do fechamento dentro dela (ver Honestidade sobre o
  volume anormalmente baixo desta sessão).
- **A folga técnica sobre a resistência de referência é ampla e resiliente.** Mesmo após o
  recuo de hoje, soja fecha **10,02%** acima dos 1.180,00 monitorados pela fila
  (`alerta-quebra_resistencia-soja_cbot-2026-09-15`) — uma folga maior, em pontos
  absolutos, do que a de 11/09 (9,87%), porque o ganho de segunda-feira (+0,66%) superou o
  recuo de hoje (-0,52%) em módulo.
- **A curva futura segue em contango regular, sem distorção.** Em 15/09: nov/26 (base)
  1.298,25 → jan/27 1.314,25 → mar/27 1.322,00 → mai/27 1.329,00 → jul/27 1.332,50 (CME
  CBOT) — o spread entre o contrato-base e maio/27 abriu ligeiramente para **30,75 pontos**
  (ante 29,50 em 14/09 e 28,50 em 11/09), uma inclinação um pouco mais acentuada da curva
  para frente, consistente com expectativa de aperto futuro, não de reversão.
- **A condição da lavoura americana segue estável, e a colheita 2025/26 começou.** USDA
  Crop Progress, corte de 13/09: 12% excelente + 46% boa (G/E 58%, idêntico a 06/09 e
  30/08) — mas, pela primeira vez nesta janela do dump, aparece um número de **colheita:
  6% concluída**. Isso não é, por si só, bullish nem bearish (é o início normal e esperado
  da temporada de colheita americana), mas marca a virada do calendário: dali em diante, a
  atenção do mercado começa a migrar de "condição da lavoura em pé" para "ritmo e
  qualidade de colheita" como driver de curto prazo, um tema a monitorar nas próximas
  semanas.
- **O câmbio segue depreciando o real e sustentando a paridade em reais.** USD/BRL fechou
  em **5,1696** (BCB PTAX, ainda datada de 14/09 — ver Honestidade), uma alta de **+1,53%**
  sobre os 5,0918 de 11/09 (fila `alerta-movimento_forte-usd_brl_ptax-2026-09-14`). O
  mecanismo direto para quem vende em reais: mesmo com a soja em dólar recuando -0,52% hoje
  frente a 14/09, a paridade brasileira (CBOT × câmbio, sem basis) só cedeu **-0,52%**
  também — de R$148,73/saca para **R$147,96/saca** (indicators, 15/09) — porque a PTAX de
  hoje é a mesma de ontem (não houve depreciação adicional, mas também nenhuma reversão do
  ganho cambial de segunda-feira). Olhando a janela completa desde sexta-feira, a paridade
  em reais subiu de R$145,54 (11/09) para R$147,96 (15/09), um ganho de **+1,66%** em três
  sessões — câmbio e CBOT reforçando-se mutuamente para o vendedor brasileiro.

**O que invalida / risco:**

- **O volume de hoje é baixo demais para validar plenamente o padrão técnico observado.**
  Apenas 2.379 contratos negociados (CME CBOT, 15/09) — uma fração do volume típico desta
  mesma janela (122.405 contratos chegaram a ser reportados para uma sessão recente). Um
  range de apenas 5,50 pontos com esse volume não permite distinguir entre "mercado
  genuinamente calmo" e "captura parcial de dados" — ver Honestidade.
- **O COT mais fresco (08/09) tem agora sete dias corridos de defasagem** frente à sessão
  de hoje — não há qualquer confirmação de que os fundos, que estavam ampliando fortemente
  a posição comprada até 01-08/09 (net long +9,51% na semana), continuaram comprando ou
  começaram a realizar lucro depois do forte rali de 08 a 14/09.
- **Crush margin segue comprimido, ainda que recuperando aos poucos.** Fechou em
  **US$2,3229/bushel** hoje (indicators), **-7,08%** abaixo do referencial de US$2,50
  monitorado pela fila (`alerta-quebra_suporte-complexo_soja-2026-09-15`) — a sexta leitura
  seguida abaixo do referencial nesta janela do dump (08 a 15/09), mas a distância vem
  encolhendo de forma consistente (-9,97% em 10/09 → -8,98% em 11/09 → -7,32% em 14/09 →
  -7,08% hoje).
- **Nível técnico a vigiar:** um fechamento de volta abaixo de 1.180 ainda desfaria
  formalmente o rompimento; com a folga em 10,02%, esse cenário segue distante, mas o
  spread entre soja e os outros dois produtos (ver seção Spreads) mostra que o complexo
  como um todo perdeu um pouco de tração nas últimas 48 horas.

**Leitura operacional:** para quem está comprado, a tendência de fundo permanece intacta
e ganhou um argumento técnico extra hoje: a reversão que preocupava a leitura de ontem foi
desfeita pela sessão de 14/09, não confirmada. Ainda assim, o volume anormalmente baixo de
hoje é motivo para não tratar o recuo de -0,52% como sinal de nada — nem de fraqueza, nem
de força — até a próxima sessão trazer volume normal. Para quem opera o lado vendido, a
soja não oferece, neste momento, um gatilho técnico de entrada: a folga sobre a resistência
é grande, a curva segue saudável e o único evento que se aproxima de um teste de baixa
(reversão de 11/09) já foi respondido com força compradora.

## Farelo

**Viés: neutro (mantido, mas com confiança crescente) — o ratio Far/Soj fechou acima de
80% pela TERCEIRA sessão consecutiva, a confirmação mais forte já observada desde a
abertura da tese de abundância em 11/06/2026. Isso ainda não justifica elevar o viés a
`bull-farelo` (o ratio segue dentro da própria zona "neutra" definida pelo indicador,
80-87%, e falta confirmação de COT e do físico brasileiro), mas a chance de este ser
apenas mais um "toque e recuo" como os episódios de 04/09 e 09/09 caiu substancialmente.**

O que sustenta a mudança de regime:

- **Três fechamentos consecutivos acima de 80% — nunca visto nesta janela de mais de 90
  dias.** Ratio Far/Soj: **80,25%** (11/09) → **80,55%** (14/09) → **80,46%** (15/09)
  (indicators). O critério de confirmação definido explicitamente pelo insight de 12/09
  ([[2026-09-12_ratio-far-soj-rompe-80-pela-primeira-vez]]) — "um segundo fechamento
  consecutivo acima de 80%... seria o primeiro sinal de que isso não é apenas um evento de
  um dia" — foi satisfeito em 14/09 e reforçado hoje com um terceiro. As duas aproximações
  anteriores de 80% nesta mesma janela (79,76% em 04/09, 79,06%/79,08% em 09/09) nunca
  passaram de um único dia antes de reverter; o padrão atual já é estruturalmente
  diferente. Este achado é desenvolvido com o peso que merece em
  [[2026-09-15_ratio-far-soj-terceira-sessao-consecutiva-acima-80]], que trata em
  profundidade os itens de fila `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
  e `-D+90`.
- **Oil share fechou abaixo de 50% pela terceira sessão seguida.** 49,94% (11/09) →
  49,84% (14/09) → **49,95%** (15/09) — o farelo respondendo por 50,05% a 50,16% do valor
  total do crush nas três sessões, ultrapassando o óleo de forma consistente pela primeira
  vez na janela. O pequeno recuo de hoje (49,95%, mais perto do empate do que 14/09) mostra
  que a virada não está se acelerando, mas também não está sendo desfeita.
- **Oil-meal spread negativo pela terceira sessão seguida, ainda que oscilando perto de
  zero.** -0,0187 (11/09) → -0,0506 (14/09) → **-0,0154** (15/09) USD/bushel — a métrica
  mais direta (diferença bruta entre valor do óleo e do farelo dentro do crush) segue do
  lado do farelo nas três sessões, mas sem tendência de aprofundamento: o valor de hoje é
  o mais próximo de zero dos três, sugerindo um equilíbrio instável, não uma vitória
  crescente do farelo.
- **O WASDE de setembro trouxe uma revisão estrutural na direção oposta — ainda vale
  como contraponto.** Exportação de farelo argentino 2026/27 revisada de 2,89 para **2,99
  milhões de toneladas** (USDA WASDE, edição de setembro vs agosto, `release-usda_wasde-2026-09-11`)
  — mais oferta exportável do segundo maior exportador mundial de farelo é um vetor
  baixista estrutural de médio prazo que segue tensionando com o sinal de preço de curto
  prazo.
- **A trajetória da ABIOVE para o Brasil aponta, por outro lado, para alívio de oferta
  doméstica.** Produção de farelo projetada recua de 2.129 mil t (set/26) para 1.659 mil t
  (dez/26), exportação de 1.100 para 700 mil t no mesmo período (ABIOVE projeções
  mensais, sem revisão nesta janela) — uma desaceleração sazonal da oferta que, se
  confirmada, tende a apoiar um ratio estruturalmente mais alto, alinhado com o
  movimento observado nas últimas três sessões.

**O que ainda pesa contra tratar isso como confirmado — e mantém o viés em "neutro", não
"bull-farelo":**

- **Os índices sintéticos ISF e ISO não avançaram mais — ficaram travados no mesmo
  patamar desde 11/09.** ISF em **60/100** e ISO em **80/100** (indicators) em todas as
  cinco leituras entre 11 e 15/09 (as de fim de semana sem preço novo, e as duas sessões
  negociadas). Isso é uma nuance importante: enquanto o ratio, o oil share e o oil-meal
  spread continuam confirmando o movimento dia após dia, os dois índices compostos
  (calculados por contagem de condições discretas, não de forma contínua) já deram seu
  "salto" inicial em 11/09 e não avançaram desde então — sugerindo que a mudança, até
  agora, ainda não é grande o suficiente para acionar a próxima condição discreta de
  nenhum dos dois índices.
- **O COT de 08/09 tem sete dias corridos de defasagem e mostrou, na única leitura
  disponível, cobertura de posição vendida — não convicção compradora nova.** O net long
  de managed money em farelo ficou praticamente estável (+0,32% frente a 01/09), via
  short caindo -26,73% muito mais rápido que long caindo -2,86%. O próximo corte (posições
  de 15/09, esperado por volta de 18/09) é o primeiro que poderá dizer se os fundos
  reagiram às três sessões de ratio acima de 80%.
- **O físico brasileiro segue completamente congelado — agora seis dias corridos.** A
  última leitura disponível continua sendo 09/09 (farelo MT/IMEA R$1.875,45/ton; prêmio
  export Paranaguá +0,12 USD/short ton, congelado desde 27/08, 19 dias corridos). O
  mercado físico doméstico não teve qualquer chance de reagir a três sessões de mudança de
  regime em Chicago.
- **O volume de hoje (479 contratos em farelo) é baixo demais para confirmar o
  fechamento de 80,46% com confiança plena** — ver Honestidade.

**Leitura operacional:** para quem está vendido em farelo (ou no spread Far/Soj vendido),
a acumulação de três fechamentos consecutivos acima de 80% é o quadro mais desfavorável à
posição desde a abertura da tese em junho — a recomendação é reduzir tamanho de forma mais
decisiva do que a cautela recomendada em 12/09 e 13/09, mas ainda sem fechar a posição às
cegas: falta o COT de 18/09 e qualquer reação do físico brasileiro para tratar isso como
inversão completa. Para quem está comprado em farelo ou no spread, esta é a primeira
janela da tese inteira em que três dias seguidos de preço e estrutura de crush apoiam a
posição — mas o volume anormalmente baixo de hoje é motivo para não aumentar tamanho
agora, esperando confirmação de volume normal na próxima sessão.

## Óleo

**Viés: bear, moderado (mantido) — o preço segue abaixo do suporte de 72,00 e recuou de
novo hoje, ainda que discretamente, mas a margem de biodiesel americana recuperou parte da
queda de segunda-feira, moderando (sem reverter) a divergência preço-vs-fundamento
identificada na leitura de 13/09.**

O que pesa contra a tese (preço e estrutura de crush):

- **Óleo fechou abaixo do suporte de referência pela terceira sessão seguida.** Fechou em
  **69,50** USD cts/lb hoje (CME CBOT, 15/09), -0,17% frente aos 69,62 de 14/09 — a
  variação diária mais discreta dos três produtos, mas ainda uma extensão da fraqueza. A
  fila confirma a quebra do suporte de 72,00 (`alerta-quebra_suporte-oleo_cbot-2026-09-15`),
  com a distância em **-3,47%**, ligeiramente maior do que os -3,31% de ontem porque o
  preço recuou mais um pouco.
- **O range de hoje foi o mais estreito da semana (0,38 ponto, de 69,24 a 69,62), com
  volume de apenas 1.045 contratos** — como nos outros dois produtos, um dado a tratar com
  cautela (ver Honestidade), mas que por ora não muda a leitura de preço deprimido perto do
  suporte.
- **Oil share e oil-meal spread confirmam, pela terceira sessão, perda de força relativa
  do óleo dentro do crush.** Oil share em 49,95% (ainda abaixo de 50%, ver seção Farelo
  para o detalhe espelhado) e oil-meal spread em -0,0154 USD/bushel (ainda negativo). O
  ISO (Índice de Suporte do Óleo) segue em **80/100**, abaixo do teto de 100 atingido em
  10/09, mas sem novo recuo desde 11/09.

**O que sustenta um piso parcial para a tese:**

- **A margem de biodiesel americana recuperou parte da queda de segunda-feira.** Fechou em
  **US$1,9651/galão** hoje (indicators, 15/09), uma alta de **+2,27%** sobre os US$1,9215
  de 14/09 — ainda bem abaixo do recorde de US$2,135/galão de 11/09 (sexta-feira), mas
  revertendo parte do tombo de -9,97% que a leitura de 13/09 havia atribuído inteiramente
  a uma queda do heating oil. O mecanismo: heating oil (CME NYMEX, HO=F) subiu +0,72% hoje
  (de 4,7780 para **4,8126** USD/galão), elevando a receita modelada do biodiesel, enquanto
  o custo do óleo como insumo caiu ligeiramente (-0,17%, para US$5,2125/galão, acompanhando
  a própria queda marginal do óleo em Chicago). Os dois efeitos — receita subindo, custo
  caindo — trabalharam juntos a favor da margem.
- **A divergência preço-vs-fundamento identificada em 13/09 persiste, mas de forma mais
  moderada do que naquele dia.** O óleo em Chicago segue no mesmo patamar deprimido desde
  sexta-feira (variação líquida de apenas +0,45% em três sessões), enquanto a margem de
  biodiesel oscilou entre 2,135 (recorde, 11/09), 1,9215 (tombo, 14/09) e 1,9651
  (recuperação parcial, 15/09) — uma trajetória de vaivém, não uma tendência clara em
  nenhuma das duas direções, o que reduz a força do argumento "o mercado está mal-precificando
  o óleo" sem eliminá-lo por completo.
- **A curva futura de médio prazo do óleo segue precificando um patamar acima do
  contrato próximo, embora com inclinação um pouco menos acentuada.** Out/26 (base) 69,50
  → dez/26 70,03 → jan/27 70,28 → mar/27 70,42 → mai/27 70,46 (CME CBOT, 15/09) — spread
  base-a-maio de **0,96** ponto, ante 1,06 em 14/09 e 1,05 em 11/09: uma leve compressão da
  curva para frente, consistente com o mercado revendo ligeiramente para baixo a
  expectativa de recuperação futura do óleo.
- **O RIN D4 (crédito de biocombustível renovável americano) parece ser tratado como
  constante na fórmula interna, não como dado de mercado atualizado diariamente** — ver
  Honestidade para o detalhe. Isso significa que toda a variação da margem de biodiesel
  observada nesta janela vem de heating oil e do preço do óleo, não de uma mudança real no
  valor do crédito RIN.

**Leitura operacional:** para quem está vendido em óleo direcional, o preço e a estrutura
seguem a favor da posição (terceiro fechamento abaixo do suporte, oil share e oil-meal
spread ainda do lado do farelo), mas a recuperação parcial da margem de biodiesel hoje é
um lembrete de que o argumento fundamentalista contra a posição vendida não desapareceu —
apenas ficou menos extremo do que na sexta-feira. Para quem está comprado em óleo
direcional, a tese segue sem confirmação de preço, mas ganhou hoje um pequeno reforço na
economia de biodiesel; ainda não o suficiente para justificar aumento de tamanho dado o
volume anormalmente baixo da sessão. Para quem opera o spread farelo-óleo dentro do crush,
a terceira sessão seguida com o farelo levemente à frente do óleo (oil-meal spread
negativo, ainda que perto de zero) sugere que o spread pode estar entrando em uma faixa de
equilíbrio mais duradoura, menos extrema do que a leitura de 12/09 chegou a descrever.

## Spreads e crush (leitura de complexo)

A janela de três sessões desde a reabertura do fim de semana (11, 14 e 15/09) mostra um
padrão consistente e, pela primeira vez desde junho, direcionalmente coerente: farelo
ganhando terreno relativo sobre soja e óleo em todas as três, ainda que com magnitudes
pequenas e, em alguns casos, oscilantes. Preços: soja 1.296,50 → 1.305,00 → 1.298,25;
farelo 346,80 → 350,40 → 348,20; óleo 69,19 → 69,62 → 69,50 (CME CBOT). O ratio Far/Soj —
farelo dividido pela soja, normalizado — capta isso de forma direta: **80,25% → 80,55% →
80,46%**, três fechamentos consecutivos acima do patamar de 80% que separa a zona
"abundante" (bearish para farelo) da zona "neutra". O oil share (fatia do valor do crush
que vem do óleo) espelha o mesmo movimento pelo lado do óleo: **49,94% → 49,84% → 49,95%**,
três leituras seguidas abaixo de 50%. E o oil-meal spread (diferença bruta de valor entre
óleo e farelo dentro do crush) confirma pela terceira vez: **-0,0187 → -0,0506 → -0,0154**
USD/bushel, todas negativas.

Três indicadores diferentes, construídos de formas matematicamente distintas a partir dos
mesmos três preços, concordando na mesma direção por três sessões seguidas — isso é o
padrão de coerência mais forte observado em toda a tese desde 11/06/2026, e é tratado com
profundidade no insight dedicado
[[2026-09-15_ratio-far-soj-terceira-sessao-consecutiva-acima-80]]. Ao mesmo tempo, os dois
índices compostos por contagem de condições — ISF (60/100) e ISO (80/100) — ficaram
travados nesse patamar desde 11/09, sem acompanhar a continuidade do movimento nas
métricas contínuas. Isso sugere que a mudança de regime, embora real e persistente, ainda
não atingiu a magnitude necessária para acionar a próxima condição discreta desses dois
índices — um contraponto útil para não superestimar a força do sinal.

O crush margin fechou em **US$2,3229/bushel** hoje (indicators), a sexta leitura seguida
(08 a 15/09, com exceção dos dias de fim de semana sem preço novo) abaixo do referencial
de US$2,50 monitorado pela fila (`alerta-quebra_suporte-complexo_soja-2026-09-15`), mas com
a distância encolhendo de forma consistente: -9,97% (10/09) → -8,98% (11/09) → -7,32%
(14/09) → **-7,08%** (hoje). O mecanismo por trás dessa recuperação lenta: farelo e óleo
vêm subindo, líquidos de soja, mais rápido do que a própria soja nas últimas sessões —
exatamente o que os outros indicadores de crush já vinham sinalizando.

O COT de 08/09 (sete dias corridos de defasagem frente à sessão de hoje) segue sendo o
único retrato de posicionamento disponível, e cada dia que passa sem atualização reduz
mais sua utilidade para avaliar se os fundos já reagiram às três sessões de mudança de
regime no ratio. O próximo corte (posições de 15/09, esperado por volta de 18/09) é o
primeiro capaz de confirmar ou contradizer diretamente o que os preços já mostram há três
dias.

Do lado dos fundamentos brasileiros de médio prazo (ABIOVE, sem revisão nesta janela), o
balanço projetado mostra o esvaziamento sazonal esperado: estoque final de soja recuando
de 7.912 mil toneladas (set/26) para 1.890 mil toneladas (dez/26), produção de farelo
caindo de 2.129 para 1.659 mil toneladas no mesmo período, exportação de farelo recuando
de 1.100 para 700 mil toneladas — uma trajetória que tende a apoiar, não contrariar, um
ratio estruturalmente mais alto no médio prazo. Isso é consistente, pela primeira vez em
semanas, com o sinal de preço de curto prazo — uma mudança em relação às leituras
anteriores, que descreviam essa tensão como não resolvida.

## Lente fiscal/regulatória BR

Antes de fechar qualquer tese de preço BR, os vetores tributários/regulatórios vivos que
pesam no complexo — todos do `system/tributario_watch.toml`, cujo carimbo mais recente
(`atualizado_em`) em todos os 10 eventos catalogados é 2026-06-05, ou seja, **102 dias
corridos sem revisão humana** frente a hoje (15/09):

- **MP 1.363/2026** (id `MP-1363-2026`, subvenção diesel fóssil R$1,12/L, vigente até
  31/12/2026): barateia o diesel fóssil no mix B15 (mistura obrigatória de 15% de
  biodiesel), reduzindo a competitividade relativa do biodiesel e a demanda doméstica por
  óleo de soja — vetor estrutural de baixa para óleo, sem mudança de status.
- **B16 (id `B16-CNPE-2026`, elevação da mistura obrigatória de biodiesel para 16%)**
  segue "adiado", resultado esperado por volta de novembro/2026. Upside represado (~436
  mil toneladas de demanda potencial adicional de óleo), não corrente.
- **Isenção de PIS/Cofins do biodiesel na mistura** (id `PISCOFINS-BIODIESEL-ISENCAO`):
  vigência registrada até 31/07/2026 — já **46 dias corridos vencida** frente a
  15/09/2026, sem registro de prorrogação ou expiração.
- **MP 1.358/2026** (subvenção gasolina R$0,89/L): vigência registrada até 11/07/2026,
  agora **66 dias corridos vencida**.
- **STJ REsp 2.165.276** (id `STJ-RESP-2165276`, crédito de PIS/Cofins sobre soja em
  biodiesel, direção "alta" para soja/óleo): sem novidade nesta janela.
- **EPA RFS 2026/2027** (id `EPA-RFS-2026-2027`, mandato de biocombustível americano,
  vigente desde 15/06/2026, direção "alta" para óleo): sustenta o RIN D4, estável — embora,
  como notado na seção Óleo e em Honestidade, o valor do RIN parece fixo na fórmula interna
  usada por este sistema, não uma leitura de mercado atualizada diariamente.
- **Crédito 45Z** (id `45Z-CLEAN-FUEL`, em tramitação, direção "mista"): sem novidade.
- **Indonésia — Danantara** (id `DANANTARA-INDONESIA`) e **levy de exportação PMK
  9/2026** (id `INDONESIA-LEVY-PMK9`): a assunção plena da centralização da exportação de
  palma pela Indonésia tinha alvo 01/09/2026 — já se passaram **14 dias** sem confirmação.
  Catalisador de alta represado para óleo (via substituição com palma) — sem dado de MPOB
  disponível para monitorar diretamente (ver Honestidade).
- **Indonésia B50** (id `INDONESIA-B50`, monitorando, direção "alta"): sem novidade.

## Riscos e eventos próximos

- **Confirmação (ou não) de volume normal na próxima sessão** — se o volume de hoje se
  repetir amanhã, isso passaria de anomalia pontual a padrão persistente, exigindo
  investigação mais profunda da fonte de dados (ver Honestidade).
- **O COT de 08/09 está sete dias corridos atrasado frente ao preço** — o próximo corte
  (posições de 15/09, esperado por volta de 18/09) é o primeiro capaz de confirmar se os
  fundos reagiram às três sessões consecutivas de ratio Far/Soj acima de 80%.
- **Um quarto fechamento consecutivo do ratio acima de 80%** elevaria ainda mais a
  confiança na mudança de regime; um fechamento de volta abaixo de 80% devolveria o evento
  ao padrão histórico de "toque e recuo", ainda que agora com três dias de sustentação
  prévia.
- **Reação (ou ausência) do físico brasileiro de farelo e óleo**, congelado desde 09/09
  (seis dias) e 27/08 (prêmios export, 19 dias).
- **USDA Crop Progress semanal**: agora que a colheita 2025/26 começou (6% em 13/09),
  monitorar o ritmo de avanço nas próximas semanas como novo driver de curto prazo.
- **USDA WASDE de setembro**: ainda incompleto nesta janela (só farelo Argentina/Brasil) —
  monitorar se as tabelas de soja em grão, óleo e EUA aparecem nos próximos dias.
- **NOPA mensal** (`release-nopa-2026-09-15`): mais um carimbo sem dado novo de fato
  (paywall).
- **Confirmação da centralização plena da exportação de palma pela Danantara** — alvo
  01/09, já 14 dias passados.
- **Vigência da isenção PIS/Cofins do biodiesel** (46 dias vencida) e **MP 1.358/2026 da
  gasolina** (66 dias vencida) — checar notícia de renovação/expiração.
- **Clima**: previsão de hoje (15/09) mostra retorno de temperaturas mais amenas no Sul
  após o resfriamento de 13/09, sem menção de geada em Passo Fundo/RS, e calor voltando a
  subir no núcleo produtor de Mato Grosso — pano de fundo para a janela de plantio da safra
  2026/27 que se aproxima.
- **Marco de 102 dias sem revisão humana do `tributario_watch.toml`** — pelo menos dois
  vetores (isenção PIS/Cofins biodiesel, MP 1.358/2026) já vencidos sem registro de
  renovação, seguem sem checagem manual.

## Honestidade

- **O volume negociado hoje (15/09) foi anormalmente baixo em todos os quatro
  instrumentos do dump** — soja 2.379 contratos (frente a valores de 100-160 mil vistos
  recentemente nesta mesma janela), farelo 479 (frente a 20-30 mil), óleo 1.045 (frente a
  17-32 mil) e heating oil 510. Não há feriado americano conhecido que justifique um pregão
  tão fino em 15/09/2026, uma terça-feira comum. A leitura mais provável é que o dump
  capturou uma fatia parcial da sessão, não a liquidação plena do dia — mas não há como
  confirmar isso com os dados disponíveis agora. Todos os fechamentos de hoje (e as leituras
  de nível técnico, ratio e crush derivadas deles) devem ser tratados com um desconto de
  confiança extra até a próxima geração do briefing confirmar ou revisar esses números.
- **Os campos brutos de farelo para a sessão de 14/09 (abertura, máxima, mínima, volume) e
  toda a curva futura de farelo para aquela data divergem entre a geração de ontem do
  briefing e a geração de hoje, de um jeito que sugere contaminação cruzada com os dados de
  15/09.** Especificamente: a máxima, mínima e volume agora atribuídos a 14/09
  (350,30 / 348,10 / 479 contratos) são **idênticos** aos de 15/09, e a curva futura de
  farelo "de 14/09" (F27 356,00, H27 356,70, K27 357,30) também bate exatamente com a curva
  de 15/09 — enquanto o fechamento (350,40) permaneceu estável entre as duas gerações. Por
  isso, esta leitura usa apenas o fechamento de 14/09 (confirmado por bater com o valor já
  usado no cálculo do crush margin e do ratio daquele dia, que não mudaram) e evita citar
  máxima/mínima/volume/curva futura "de 14/09" como fatos confiáveis — o mesmo tipo de
  problema de qualidade de dado já documentado na auditoria de 13/09
  ([[2026-09-13_correcao-numeros-sessao-11set-farelo-oleo]]).
- **A janela de 14 dias do dump não traz mais nenhuma linha bruta de CME CBOT para soja
  e óleo na data de 14/09** (apenas farelo e heating oil parcial) — diferente da geração
  de ontem, que trazia o conjunto completo. Isso reforça a suspeita de instabilidade na
  extração/retenção de dados brutos dessa fonte nesta janela específica.
- **O RIN D4 parece ser tratado como uma constante na fórmula interna de margem de
  biodiesel, não como um dado de mercado atualizado diariamente.** Ao isolar o termo
  "1,5×RIN" da fórmula (receita = HO + 1,5×RIN) em cada uma das últimas seis sessões com
  dado disponível (08 a 15/09), o valor implícito do RIN fica em **~2,11 USD** em todas
  elas, sem variação. Isso significa que toda a variação da margem de biodiesel discutida
  nesta e nas leituras anteriores vem inteiramente do heating oil e do preço do óleo, não
  de uma mudança real no mercado de créditos RIN — uma limitação metodológica do indicador
  que não havia sido explicitada com este nível de detalhe em leituras anteriores.
- **A BCB PTAX de hoje (15/09) não está disponível nesta janela do dump** — a paridade em
  reais da soja calculada hoje usa a mesma cotação de USD/BRL de 14/09 (5,1696), então a
  variação de -0,52% na paridade reflete inteiramente a variação do CBOT em dólar, não
  qualquer movimento cambial novo. Não é possível saber se o câmbio de fato ficou estável
  hoje ou se apenas a série de PTAX está atrasada.
- **O COT de 08/09 tem agora sete dias corridos de defasagem** frente à sessão de hoje —
  não há como confirmar se os fundos reagiram às três sessões consecutivas de ratio acima
  de 80%. Próximo corte esperado por volta de 18/09.
- **Percentil histórico de posicionamento COT não está disponível no briefing** — toda
  leitura de "fundos comprando/vendendo" usa variação semana a semana de contratos
  absolutos, não percentil histórico.
- **`tributario_watch.toml` sem atualização há 102 dias corridos** — pelo menos dois
  vetores (isenção PIS/Cofins do biodiesel, MP 1.358/2026) já passaram da vigência
  registrada sem nota de renovação ou expiração.
- **NOPA segue inacessível** (paywall) — mais um "release" sem dado novo de fato.
- **A ausência de itens de notícia desde 10/09 ("0 items lidos, 0 mantidos"), agora seis
  dias corridos**, é registrada como falha ou pausa de coleta da fonte RSS, não como
  ausência real de notícia relevante no mercado.
- **A previsão INMET para 15/09 é previsão meteorológica, não medição de precipitação
  real** — a ausência de menção a "geada" no boletim de hoje para Passo Fundo/RS é
  indicativa, não confirmação de que o risco de geada tardia está afastado.
- **Prêmios de exportação (Paranaguá) e o físico de farelo/soja BR seguem sem atualização
  própria desde 09/09** (seis dias corridos) — não é possível afirmar se isso reflete
  mercado físico genuinamente parado ou apenas defasagem normal de publicação.
- **MPOB (palma Malásia) segue com parser quebrado** — nenhum dado de produção/estoque de
  palma malaia disponível, o que impede monitorar diretamente o catalisador represado da
  centralização de exportação indonésia (Danantara).
- **BCBA (Argentina) segue sem links de relatório detectados** — nenhum dado de safra ou
  exportação argentina disponível.
- **Os forecasts estatísticos internos (bandas 7d/30d) foram gerados sobre o fechamento de
  hoje**, com viés "altista" atribuído a soja e farelo — isso reflete extrapolação
  estatística de tendência recente (MA20 + volatilidade + slope), não uma reavaliação
  fundamentalista desta leitura; tratado aqui como referência estatística, não como leitura
  própria desta análise, e potencialmente distorcido pelo volume anormal da sessão de hoje
  usada como base do cálculo.
- **A fila de julgamento continua listando os dois itens de revisão do ratio Far/Soj (D+7
  e D+90) como "vencidos"**, mesmo com o D+90 já tratado em profundidade em 09/09 e
  revisitado em 12/09 e novamente hoje — um eco do sistema de geração de fila que não lê de
  volta os insights já escritos para marcar a revisão como encerrada.
