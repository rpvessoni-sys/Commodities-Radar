---
data: 2026-09-10
titulo: "Segundo pregão pós-pausa inverte o primeiro: farelo devolve parte da queda, óleo devolve parte do salto, e os índices estruturais (ISF/ISO) seguem travados em 80/100 sem confirmar nenhuma das duas reversões — enquanto a soja recua do topo do range pela primeira vez desde a reabertura, com volume caindo pelo segundo dia seguido"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT (ZSX26 soja / ZMV26 farelo / ZLV26 óleo) — sessão de 2026-09-09 (quarta-feira), segundo pregão pleno desde a reabertura de 08/09. Soja: abertura 1.317,00, máxima 1.320,75, mínima 1.305,50, fechamento 1.308,75 USD cts/bushel, volume 100.017 contratos (ticker ZSX26.CBT, venc. nov/26). Farelo: abertura 344,00, máxima 346,70, mínima 340,50, fechamento 345,00 USD/short ton, volume 32.199 contratos (ticker ZMV26.CBT, venc. out/26). Óleo: abertura 70,36, máxima 70,62, mínima 69,89, fechamento 70,04 USD cts/lb, volume 23.814 contratos (ticker ZLV26.CBT, venc. out/26). Curva futura em 09/09 — soja: set/26 1.298,00, nov/26 (base) 1.308,75, jan/27 1.324,50, mar/27 1.331,00, mai/27 1.336,75, jul/27 1.338,50; farelo: set/26 344,80, out/26 (base) 345,00, dez/26 351,30, jan/27 353,80, mar/27 355,60, mai/27 357,00; óleo: set/26 70,32, out/26 (base) 70,04, dez/26 70,53, jan/27 70,83, mar/27 71,06, mai/27 71,09
  - CME CBOT 2026-09-08 (terça-feira, primeiro pregão pós-pausa) — farelo fechamento 343,30 (volume 32.108, CME CBOT, dado bruto presente no dump). Soja (fechamento implícito 1.316,25) e óleo (fechamento implícito 70,22) **não têm linha bruta de CME CBOT nesta janela do dump** — os dois valores são reconstruídos a partir das fórmulas dos indicadores sintéticos de 08/09 (`soja_paridade_br` e `biodiesel_us.custo_oleo_usd_galao`, indicators), não de uma linha própria de preço; ver seção Honestidade
  - CME NYMEX heating oil (HO=F) — 2026-09-09: abertura 4,7964, máxima 4,8200, mínima 4,7964, fechamento 4,8017 USD/galão, volume 526 contratos. Valor embutido no cálculo de receita de biodiesel de 08/09 (indicators): ~4,57 USD/galão — alta implícita de ~+5% de 08/09 para 09/09
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, ISF, ISO, margem biodiesel, paridade BR) — 2026-09-09, segundo recálculo com insumo de preço fresco
  - BCB PTAX — 2026-09-09: USD/BRL 5,0979, EUR/BRL 5,9278, Selic diária 0,05166% a.a. (séries SGS 1, 21619, 11); 2026-09-08: USD/BRL 5,0856, EUR/BRL 5,913
  - CEPEA/ESALQ Soja Paranaguá via NAG — 2026-09-09: R$ 160,12/saca (var -0,21%), ante R$ 160,46/saca em 08/09
  - CEPEA/ESALQ Soja Paraná interior via NAG — 2026-09-09: R$ 152,43/saca (var +0,13%), ante R$ 152,23/saca em 08/09
  - NAG Físico BR — 2026-09-09: farelo MT/IMEA R$ 1.875,45/ton (var 0,0%, congelado desde 04/09 — 5º dia corrido sem variação), Rondonópolis/MT R$ 1.900,00/ton (congelado), RS média R$ 1.860,00/ton (congelado); prêmios export Paranaguá farelo +0,12 USD/short ton e óleo +0,10 cts/lb, ambos congelados desde 27/08 (13 dias corridos até 09/09, 14 até hoje 10/09)
  - CFTC COT Managed Money, Swap Dealers e Producer/Merchant — corte de 2026-09-01 (terça-feira), sem atualização nesta janela; 8 dias corridos de defasagem frente ao dado (09/09), 9 dias corridos frente a hoje (10/09)
  - USDA Crop Progress — corte mais recente, semana encerrada em 2026-09-06: 12% excelente / 46% boa / 9% ruim (G/E 58%), inalterado desde 30/08; defasagem de 4 dias corridos frente a hoje (10/09)
  - USDA WASDE — ausente da janela deste briefing
  - NOPA — fila `release-nopa-2026-09-09`; `monthly_status` segue em 0,0 bool (paywall) em todas as datas do dump, de 2026-08-27 a 2026-09-09 — terceiro dia seguido do mesmo falso positivo na fila
  - ABIOVE projeções mensais — balanços set-dez/2026, sem revisão nesta janela (mesmos números já usados em 08/09)
  - NOAA CPC ENSO — El Niño Advisory, inalterado até 2026-09-09
  - MPOB — carimbo 2026-09-09, parser sem números extraídos (mesma barreira, 3.456 caracteres)
  - BCBA (Argentina) — carimbo 2026-09-09, scraper acessa a página mas não encontra links de relatório
  - INMET — previsão para 2026-09-10 (HOJE): chuva e trovoadas generalizadas no núcleo produtor de Mato Grosso e Goiás (Cuiabá 37°C/24°C, Sinop 38°C/24°C, Sorriso 37°C/24°C, Lucas do Rio Verde 38°C/25°C, Rio Verde/GO 33°C/22°C) e no Sul (Cascavel/PR 25°C/16°C, Maringá/PR 28°C/21°C, Passo Fundo/RS 21°C/14°C — sem menção de geada)
  - Notícias Agrícolas/Canal Rural + FarmProgress RSS — 2026-09-09: "160 items lidos, 4 mantidos (soja/farelo/oleo)", manchete "New genetic weapon fights soybean cyst nematode" (FarmProgress, sem relevância direta de preço)
  - CEPEA RSS — 2026-09-09: 109 itens parseados (ante 103 em 08/09), sem manchete legível nova; última manchete de preço disponível permanece a de 04/09 ("Alta dos preços ganha força no início de setembro")
  - system/tributario_watch.toml (lido como referência, não editado) — `atualizado_em` 2026-06-05 em todos os 10 eventos catalogados, agora 97 dias corridos sem revisão humana frente a hoje (10/09)
  - Forecasts estatísticos internos (bandas 7d/30d, MA20+volatilidade+slope) — geração de 2026-09-09, alvos 16/09 (7d) e 09/10 (30d); viés "altista" em soja e farelo nos dois horizontes, "lateral" no óleo em 7d e "altista" no óleo em 30d, calculado sobre o fechamento de 09/09
  - Fila de julgamento (carimbada 2026-09-09 no briefing, 7 itens) — tratados nesta leitura: `alerta-quebra_resistencia-soja_cbot-2026-09-09`, `alerta-quebra_suporte-oleo_cbot-2026-09-09`, `alerta-quebra_resistencia-farelo_cbot-2026-09-09`, `alerta-quebra_suporte-complexo_soja-2026-09-09`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, `release-nopa-2026-09-09`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`
  - Cruza com [[2026-09-09_leitura-complexo]] (leitura de ontem, que documentou a primeira reversão pós-pausa: farelo caindo, óleo subindo) e com [[2026-09-09_d90-ratio-far-soj-reverte-na-vespera]] (veredito da revisão D+90 da tese original do ratio Far/Soj, aberta em [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]])
status: ativa
vies: [bull-soja, bear-farelo, neutral-oleo_soja]
---

## Visão geral

Hoje, quinta-feira 10/09/2026, o dado mais fresco do briefing é o fechamento de
quarta-feira 09/09 — o segundo pregão pleno na CBOT (bolsa de grãos de Chicago) desde a
reabertura de terça-feira 08/09, depois da pausa de quatro dias por causa do feriado
duplo (Labor Day nos EUA e Independência do Brasil). Para quem não acompanha o dia a
dia: quando a soja em grão é esmagada ("crush"), ela vira dois produtos com demandas
diferentes — farelo (proteína para ração animal) e óleo (alimentação humana e
biodiesel). O crush margin mede, em dólares por bushel (unidade agrícola americana,
~27,2 kg de soja), quanto sobra para a esmagadora depois de vender farelo + óleo e pagar
a soja. O oil share (fatia do valor total do crush que vem do óleo, farelo+óleo somando
100%) diz qual dos dois produtos está "pagando a conta": oil share alto = óleo manda e o
farelo vira insumo residual, mais barato, "sobra" — daí o índice sintético interno
"Índice de Sobra de Farelo" (ISF). Oil share baixo = o farelo sustenta o crush e o óleo
perde força relativa, o que o índice espelhado "Índice de Suporte do Óleo" (ISO) capta
pelo lado inverso. O ratio Far/Soj (preço do farelo dividido pelo preço da soja,
normalizado) é a métrica clássica de mercado para a mesma ideia: abaixo de 80% o farelo
está "abundante" (barato relativo à soja, viés baixista); a partir de 87% ele está
"apertado" (caro relativo à soja, viés altista).

A leitura de ontem registrou a primeira reversão de sinal desde a reabertura: no dia
08/09, o farelo caiu -1,32%, o óleo subiu +1,96%, e o ratio Far/Soj recuou de 79,76%
para 78,28% — um giro contra a recuperação de duas semanas que vinha se desenhando e que
coincidiu, quase ao dia, com o vencimento da revisão formal D+90 da tese de abundância
de farelo aberta em 11/06/2026. O dado de hoje é o segundo pregão pleno depois daquele
giro, e ele fez o oposto: farelo subiu +0,50% (343,30 → 345,00, CME CBOT), óleo caiu
-0,26% (70,22 → 70,04), e o ratio Far/Soj **recuperou** parte do terreno perdido,
subindo de 78,25% para **79,08%** (indicators, 09/09) — reduzindo a distância até 80% de
1,75 para **0,92 ponto percentual**. Em outras palavras: em dois pregões consecutivos
desde a reabertura, o complexo girou de lado duas vezes seguidas. O que NÃO girou foram
os índices sintéticos: o ISF (Índice de Sobra de Farelo) e o ISO (Índice de Suporte do
Óleo) permaneceram exatamente parados em 80/100 e 100/100 nas duas sessões (indicators,
08/09 e 09/09) — nenhuma das duas reversões de preço foi grande o suficiente para mudar
a leitura estrutural desses índices, que continuam descrevendo um crush dominado pelo
óleo e um farelo estruturalmente abundante, mesmo enquanto o preço bruto oscila para os
dois lados. A soja, por sua vez, teve seu primeiro dia de recuo desde a reabertura:
-0,57% (1.316,25 → 1.308,75), fechando perto do fundo do range diário pela primeira vez
nesta janela, com o volume caindo pelo **segundo** dia seguido (-24,5% no dia 1, mais
-20,8% no dia 2 — uma queda acumulada de participação de -40,2% frente à última sessão
plena pré-pausa). **Leitura de uma linha**: o pivô do complexo continua sendo a
realocação de valor entre farelo e óleo dentro do crush, mas depois de duas sessões
inteiras de dados frescos o placar está empatado — um dia para cada lado — e só os
índices estruturais (ainda travados a favor do óleo) e o ratio (ainda abaixo de 80%, mas
cada vez mais perto) dão alguma direção. Confiança **moderada-baixa**: com apenas duas
observações de preço fresco e o COT ainda com 9 dias de defasagem, tratar qualquer uma
das duas reversões diárias como "a tendência" seria prematuro.

## Soja

**Viés: bull, moderado — a folga técnica sobre a resistência de julho segue ampla, mas
hoje veio o primeiro recuo de preço desde a reabertura, com volume caindo pelo segundo
dia seguido, o que pede mais cautela do que a leitura de ontem sugeria.**

O que sustenta a tese:

- **A folga sobre o nível técnico de referência segue larga, mesmo após o recuo de
  hoje.** Soja CBOT fechou em 1.308,75 USD cts/bushel em 09/09/2026 (CME CBOT), **-0,57%**
  sobre os 1.316,25 (fechamento implícito) de 08/09 — o primeiro recuo desde a
  reabertura. Mesmo assim, a folga sobre a resistência de 1.180,00 monitorada pela fila
  (`alerta-quebra_resistencia-soja_cbot-2026-09-09`) permanece em **10,91%**, ante 11,59%
  no dia anterior — uma redução pequena, que não compromete o rompimento técnico de
  julho. O contrato negociou entre 1.305,50 e 1.320,75 (mínima/máxima, CME CBOT) e fechou
  a apenas 21% de distância do fundo do range — o primeiro fechamento fraco dentro do
  range desde a reabertura, ao contrário dos fechamentos próximos ao topo observados nos
  dois pregões anteriores.
- **O volume caiu pelo segundo dia consecutivo, e isso é o dado mais importante da
  sessão para quem avalia convicção.** 100.017 contratos em 09/09 (CME CBOT, ZSX26)
  contra 126.269 no primeiro pregão pós-pausa (08/09, citado via [[2026-09-09_leitura-
  complexo]]) — uma queda adicional de **-20,8%**. Juntando as duas sessões, a
  participação caiu -24,5% no dia 1 e mais -20,8% no dia 2, uma retração acumulada de
  **-40,2%** frente ao volume da última sessão plena pré-pausa (167.214 contratos em
  04/09). O mecanismo a observar: um rompimento técnico sustentado por volume decrescente
  é estruturalmente mais frágil do que um sustentado por volume crescente ou estável — a
  cada dia que passa sem um pregão de participação plena, fica mais difícil dizer se o
  nível de 1.308-1.320 reflete convicção real do mercado ou apenas ausência de vendedores
  agressivos em um book mais fino que o normal.
- **O câmbio trabalhou, líquido, a favor do produtor brasileiro nesta sessão, mas não o
  suficiente para compensar a queda em dólar.** USD/BRL fechou 09/09 em 5,0979 (BCB
  PTAX), **+0,24%** sobre os 5,0856 de 08/09 — o real se desvalorizou ligeiramente. Ainda
  assim, a paridade em reais da soja (CBOT × câmbio, sem basis) fechou em **R$
  147,09/saca** (indicators, 09/09), uma queda de -0,33% frente aos R$ 147,57 do dia
  anterior — o câmbio mais fraco ajudou, mas não anulou o efeito da queda de -0,57% em
  dólar. É o mesmo lembrete de sempre: para quem vende em reais, a combinação dos dois
  preços manda, não cada um isolado.
- **O físico exportador e o físico interior divergiram ligeiramente, um padrão que já
  apareceu antes nesta série.** CEPEA/ESALQ Soja Paranaguá (via NAG) fechou 09/09 em R$
  160,12/saca, -0,21% sobre 160,46 — coerente com a combinação de câmbio mais fraco e
  CBOT mais fraco. Já o físico do Paraná interior (via NAG) subiu, R$ 152,43/saca
  (+0,13% sobre 152,23) — um pequeno descolamento entre porto e interior que, isolado, não
  permite concluir mudança de tendência, mas mostra que o mercado físico brasileiro não
  está simplesmente replicando o movimento de Chicago 1:1.
- **A estrutura da curva futura segue em contango saudável, sem sinal de estresse.**
  Set/26 1.298,00 → nov/26 (base) 1.308,75 → jan/27 1.324,50 → mar/27 1.331,00 → mai/27
  1.336,75 → jul/27 1.338,50 (CME CBOT, 09/09) — uma progressão de carry regular, sem
  inversão nem distorção pontual. O mecanismo: contango consistente ao longo de toda a
  curva costuma refletir custo de carregamento normal, não um mercado precificando
  escassez imediata nem pânico de demanda — é um pano de fundo neutro-a-construtivo, não
  um sinal de alerta.
- **A condição da lavoura americana segue estável, sem novidade nesta janela.** USDA
  Crop Progress permanece no corte da semana encerrada em 06/09 (12% excelente + 46% boa,
  "ruim" 9%, G/E 58%), idêntico ao corte de 30/08. A defasagem frente a hoje (10/09) é de
  **4 dias corridos**. O próximo corte é esperado na segunda-feira 14/09.

**O que invalida / risco:**

- **A queda de volume por dois dias seguidos é o ponto de maior atenção da sessão.**
  Um segundo pregão pleno com queda adicional de participação (-20,8%) é um padrão
  diferente — e mais preocupante — do que um único dia fino de reabertura; se a
  tendência de volume decrescente continuar num terceiro pregão, a leitura muda de "book
  ainda normalizando" para "falta de convicção estrutural" no nível atual de preço.
- **O crush margin segue comprimido, embora melhorando.** Fechou em **US$
  2,2069/bushel** em 09/09 (indicators), **-11,72%** abaixo do referencial de US$ 2,50
  monitorado pela fila (`alerta-quebra_suporte-complexo_soja-2026-09-09`) — pior nível
  absoluto de compressão nominal, mas uma melhora relativa frente aos -15,28% de 08/09.
  Uma margem de esmagamento comprimida por período prolongado tende a reduzir o
  incentivo da indústria para processar soja, pesando sobre a demanda física por grão no
  médio prazo.
- **Nível técnico a vigiar:** um fechamento de volta abaixo de 1.180 desfaria o
  rompimento; a folga (10,91%) segue confortável, mas o fechamento perto do fundo do
  range de hoje é o primeiro sinal técnico, ainda que fraco, de perda de força
  compradora dentro do próprio pregão.

**Leitura operacional:** o segundo pregão pós-pausa trouxe o primeiro recuo de preço e a
segunda queda seguida de volume — sinais que, juntos, pedem mais cautela do que a
leitura de ontem sugeria, mas nenhum dos dois invalida o rompimento técnico em si. Não há
gatilho para reduzir posição comprada, mas também não há espaço para aumentar
agressivamente sem ver um pregão de volume normalizado confirmando o nível atual. Para
quem opera o lado vendido isoladamente, ainda não há sinal de reversão técnica — o nível
a vigiar continua sendo 1.180 — mas o fechamento fraco de hoje é o tipo de detalhe que
vale marcar e comparar com a próxima sessão. Para quem opera a paridade em reais, o real
mais fraco de hoje ajudou parcialmente a compensar a queda em dólar, mas não o
suficiente para evitar uma queda líquida na paridade.

## Farelo

**Viés: bear, moderado, mas com convicção reduzida — o preço subiu hoje, revertendo parte
da queda de ontem, e o ratio Far/Soj recuperou quase metade da distância até 80% numa
única sessão. A estrutura (ISF) não acompanhou a melhora, o que deixa a tese dividida
entre um preço que hoje favoreceu o farelo e um índice que continua descrevendo
abundância.**

O que pressiona a tese, mas com uma reversão parcial a favor do farelo hoje:

- **O preço subiu, revertendo mais de um terço da queda do dia anterior.** Farelo CBOT
  fechou em 345,00 USD/short ton em 09/09/2026 (CME CBOT), **+0,50%** sobre os 343,30 de
  08/09 — depois de uma queda de -1,32% no dia anterior, o saldo líquido dos dois
  pregões desde a reabertura ainda é negativo frente aos 348,20 de 04/09 (-0,92%
  acumulado), mas a direção de hoje foi de recuperação, não de continuação da queda. O
  contrato negociou entre 340,50 e 346,70 (mínima/máxima, CME CBOT) e fechou a 73% de
  distância do fundo do range — perto do topo, o oposto exato do fechamento perto da
  mínima observado ontem. A folga sobre a resistência de 325,00
  (`alerta-quebra_resistencia-farelo_cbot-2026-09-09`) subiu para **6,15%**, ante 5,72%
  no dia anterior.
- **O ratio Far/Soj recuperou quase metade da distância que havia se reaberto no dia
  anterior.** Fechou em **79,08%** em 09/09 (indicators), ante 78,25% em 08/09 — um
  avanço de **+0,83 ponto percentual** na segunda sessão fresca, desfazendo mais da
  metade do recuo de -1,48 p.p. registrado no dia anterior. A distância até 80% caiu de
  1,75 para **0,92 ponto percentual** — o ratio está, hoje, mais perto de cruzar 80% do
  que esteve em qualquer momento desde a aproximação de 79,76% em 04/09. Na definição do
  próprio indicador (<80% = "abundante", >=87% = "apertado"), o farelo segue
  tecnicamente na zona de abundância, mas cada vez mais perto da fronteira.
- **Os índices sintéticos, ao contrário do preço e do ratio, não se moveram nem um
  pouco.** O Índice de Sobra de Farelo (ISF) permaneceu em **80/100** ("forte pressão
  baixista no farelo", 4 de 5 condições, indicators, 09/09) — exatamente o mesmo valor
  de 08/09. O mecanismo: o índice combina múltiplos sinais discretos (contagem de
  condições atendidas, não um valor contínuo), o que pode explicar por que uma melhora
  de +0,83 p.p. no ratio não foi suficiente para mudar a contagem de condições — mas
  também levanta a pergunta genuína, sem resposta nos dados disponíveis, de quanto o
  ratio ainda precisaria subir para que o ISF de fato recuasse. Essa é uma lacuna
  metodológica a observar, não apenas um dado de mercado.
- **O oil-meal spread encolheu, coerente com o farelo subindo mais que o óleo hoje.**
  Fechou em **+0,1144 USD/bushel** em 09/09 (indicators), ante +0,1716 em 08/09 — uma
  queda de -33,3% no valor do spread, mas ainda positivo (o óleo segue "pagando mais" que
  o farelo dentro do crush). O movimento de hoje reduziu, mas não eliminou, a vantagem
  relativa do óleo dentro do crush observada ontem.
- **O físico brasileiro segue completamente congelado, agora pelo quinto dia
  corrido.** Farelo MT/IMEA (NAG) permaneceu em R$ 1.875,45/ton em 09/09 (var 0,0%), o
  mesmo nível desde 04/09; Rondonópolis (R$ 1.900,00/ton) e a média do RS (R$
  1.860,00/ton) também congelados. O prêmio de exportação em Paranaguá segue travado em
  +0,12 USD/short ton há 13 dias corridos (desde 27/08, NAG). Nem a queda de ontem nem a
  alta de hoje em Chicago tiveram qualquer contrapartida visível no físico doméstico —
  o que reforça a leitura de que o físico brasileiro de farelo está, por ora, isolado das
  oscilações diárias de Chicago, seja por defasagem de repasse, seja por dinâmica
  própria de oferta/demanda doméstica que os dados não permitem decompor.

**Trata a fila `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
(recorrente 🔴 VENCIDA):** mesma leitura das últimas semanas — o ratio passou a
esmagadora maioria dos 90+ dias desde 11/06/2026 abaixo de 80%, e a aproximação a esse
nível permanece episódica, não sustentada.

**Trata também `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`
(recorrente, sinalizada "em 0d" no briefing de 09/09 — o mesmo marco já vencido ontem):**
o veredito de fundo já foi entregue em profundidade em
[[2026-09-09_d90-ratio-far-soj-reverte-na-vespera]]: a tese original de abundância de
farelo **não foi invalidada** pelos 90 dias corridos. O dado de hoje é uma contra-
evidência parcial a esse veredito — o ratio subiu de volta para 79,08%, a **0,92 p.p.**
de cruzar 80% pela primeira vez desde a abertura da tese — mas não o suficiente para
reverter a conclusão, já que o ratio segue abaixo de 80% e o ISF (a métrica estrutural
mais "pesada" do sistema) não se moveu. A leitura operacional prática: quem está short
farelo (ou vendido no spread Far/Soj) não tem, com os dados de hoje, motivo para fechar a
posição, mas tem motivo para vigiar de perto o próximo pregão — se o ratio cruzar 80% em
qualquer uma das próximas sessões, esse seria o primeiro rompimento genuíno do patamar
desde 11/06/2026, e mudaria a tese de fato, não apenas a aproximação.

**O que invalida / risco:** o COT segue sendo o contraponto mais relevante, agora com
**9 dias corridos de defasagem** frente a hoje — o corte de 01/09 mostrava o net long de
managed money em farelo tendo saltado +63,83% na semana anterior (95.953 → 157.179
contratos, CFTC COT). Se os fundos mantiveram ou ampliaram essa convicção comprada ao
longo da semana, tanto a queda de 08/09 quanto a alta de 09/09 seriam apenas ruído dentro
de uma tendência de posicionamento que os dados ainda não capturam. O próximo corte
(posições de 08/09) é esperado por volta de sexta-feira 11/09 — amanhã.

**Leitura operacional:** para quem está vendido em farelo, a sessão de hoje é o primeiro
sinal de alerta desde o veredito da revisão D+90 — o preço subiu, o ratio se aproximou
mais de 80% do que em qualquer ponto da tese, e a folga técnica sobre a resistência de
325 aumentou. Não é motivo para fechar a posição (o ISF segue em 80/100 e o ratio segue
abaixo de 80%), mas é motivo genuíno para reduzir o tamanho ou apertar o stop, e para
tratar o cruzamento de 80% como o gatilho concreto que encerraria a tese, não apenas uma
aproximação. Para quem opera o spread Far/Soj (long farelo / short soja), o dia de hoje
foi o primeiro desde o veredito de ontem a favorecer essa perna. Para quem considera
abrir posição vendida nova em farelo, a oscilação de sinal em dois pregões seguidos
(queda, depois alta) pede uma terceira sessão de confirmação antes de tratar qualquer
direção como estabelecida.

## Óleo

**Viés: neutro — a alta de ontem foi parcialmente devolvida hoje, e o contrato segue
abaixo do suporte técnico rompido em agosto. Mas a margem de biodiesel americana saltou
para o nível mais alto da janela, um driver estrutural de demanda que não se refletiu no
preço de hoje — um descasamento que vale a pena vigiar de perto.**

O que pesa contra o preço, e o que sustenta a demanda de fundo:

- **A alta firme de ontem foi parcialmente devolvida.** Óleo CBOT fechou em 70,04 USD
  cts/lb em 09/09/2026 (CME CBOT), **-0,26%** sobre os 70,22 de 08/09 — depois de uma
  alta de +1,96% no dia anterior, o saldo dos dois pregões desde a reabertura ainda é
  positivo frente aos 68,89 de 04/09 (+1,67% acumulado), mas a direção de hoje foi de
  giveback, não de continuação da alta. O contrato negociou entre 69,89 e 70,62
  (mínima/máxima, CME CBOT) e fechou a apenas 21% de distância do fundo do range — um
  fechamento fraco, o oposto do fechamento perto do topo observado ontem. O fechamento de
  70,04 permanece **2,72%** abaixo do suporte de 72,00 rompido em agosto
  (`alerta-quebra_suporte-oleo_cbot-2026-09-09`) — mais distante do que os -2,44% de
  ontem.
- **Oil share e oil-meal spread recuaram ligeiramente, coerente com o giveback de
  preço.** O oil share fechou em **50,37%** em 09/09 (indicators), ante 50,56% em 08/09
  — uma queda de -0,19 p.p., ainda acima de 50% mas perdendo força pela primeira vez
  desde a reabertura. O oil-meal spread, como descrito na seção Farelo, encolheu de
  +0,1716 para **+0,1144** USD/bushel — o óleo segue valendo mais que o farelo dentro do
  crush, mas por uma margem menor que ontem.
- **O Índice de Suporte do Óleo (ISO), assim como o ISF do farelo, não se moveu.**
  Permaneceu em **100/100** — "óleo domina o crush", 5 de 5 condições atendidas
  (indicators, 09/09), o mesmo nível máximo de ontem. O giveback de preço de hoje não foi
  suficiente para tirar nenhuma condição da contagem — o mesmo tipo de descasamento entre
  índice discreto e preço contínuo observado no farelo, na direção oposta.
- **A margem de biodiesel americana saltou para o nível mais alto da janela, e o motivo
  reforça — não contradiz — a leitura de força estrutural do óleo.** Margem de **US$
  1,9137/galão** em 09/09, ante US$ 1,6663 em 08/09 (indicators) — uma alta de **+14,85%**
  em uma única sessão. Decompondo o mecanismo: a receita do biodiesel (heating oil +
  1,5× crédito RIN D4) subiu para US$ 7,9667/galão (ante US$ 7,7328 em 08/09), puxada
  quase inteiramente pelo heating oil — o diesel de aquecimento americano fechou em
  **4,8017 USD/galão** em 09/09 (CME NYMEX HO=F), uma alta implícita de aproximadamente
  **+5%** frente ao valor (~4,57 USD/galão) embutido no cálculo de receita de 08/09,
  enquanto o crédito RIN D4 (1,5× = 2,11 USD/galão) permaneceu estável. Ao mesmo tempo, o
  custo do óleo como insumo caiu ligeiramente para US$ 5,253/galão (7,5 lb × 70,04
  cts/lb), ante US$ 5,2665 em 08/09 — uma queda de -0,26%, refletindo a própria queda do
  óleo em Chicago hoje. Ou seja: os dois lados da conta jogaram a favor da margem — receita
  subindo com o diesel mais caro, custo caindo com o óleo mais barato — e o resultado foi
  a maior margem de biodiesel observada nesta série de leituras. **O mecanismo de fundo
  para o trader:** uma margem de biodiesel mais alta hoje é um incentivo para os
  produtores de biodiesel comprarem mais óleo de soja como insumo nas próximas semanas,
  mesmo que o preço do óleo na CBOT não tenha capturado esse incentivo ainda — é um
  indicador de demanda futura, não de preço presente, e o descasamento entre os dois
  (margem recorde, preço em queda) é justamente o tipo de divergência que merece
  acompanhamento nos próximos pregões.
- **O RIN D4 (crédito de biocombustível, EPA) segue estável.** 1,5×RIN = 2,11 USD/galão
  embutido no cálculo de receita em 09/09 (indicators) — o arcabouço regulatório do EPA
  RFS 2026/2027 (`EPA-RFS-2026-2027`, vigente desde 15/06/2026) permanece intacto e sem
  novidade.
- **A curva futura segue em contango moderado e coerente, sem distorção pontual.** Set/26
  70,32 → out/26 (base) 70,04 → dez/26 70,53 → jan/27 70,83 → mar/27 71,06 → mai/27 71,09
  (CME CBOT, 09/09) — a estrutura a termo não sinaliza nem estresse de curto prazo nem
  pânico de demanda.

**O que invalida / risco:**

- **Nível técnico a vigiar:** a reconquista e sustentação de 72,00 (o suporte rompido em
  agosto) seria a confirmação técnica que falta; o giveback de hoje afasta ainda mais o
  preço desse nível, ampliando a distância pela segunda sessão de dado fresco na direção
  oposta à recuperação.
- **O COT de 01/09, com 9 dias de defasagem, ainda mostra os fundos líquidos compradores
  em óleo (+17,28% net long na semana anterior, CFTC COT), um dado anterior às três
  últimas sessões (04, 08 e 09/09).** Não há como saber, com os dados disponíveis, se
  essa posição comprada já capturou o vaivém de preço dos últimos dias ou se os fundos
  ajustaram exposição de forma que os dados de preço ainda não refletem.
- **A divergência entre margem de biodiesel (recorde da janela) e preço à vista (em
  queda) pode simplesmente refletir defasagem normal — o mercado futuro de óleo
  precifica expectativa de demanda, não a margem instantânea de um único produtor
  marginal — mas também pode ser o primeiro sinal de que o mercado ainda não processou
  plenamente a alta do heating oil de hoje.** Um segundo dia de margem elevada sem
  reação de preço no óleo enfraqueceria essa leitura construtiva.

**Leitura operacional:** para quem está vendido em óleo direcional, o giveback de hoje é
uma confirmação parcial a favor da posição — o nível de 72,00 segue rompido e a distância
aumentou —, mas a margem de biodiesel em máxima da janela é um contra-argumento
estrutural que pede cautela antes de tratar a fraqueza de preço como decisiva. Não é
momento de aumentar posição vendida com convicção plena; é momento de vigiar se um
terceiro pregão confirma a fraqueza de preço ou se o mercado começa a repassar a força da
margem de biodiesel para o valor do contrato. Para quem opera o spread farelo-óleo dentro
do crush, o dia de hoje devolveu parte da vantagem que o óleo havia ganho ontem — mais um
capítulo de uma oscilação de dois dias sem direção clara ainda estabelecida.

## Spreads e crush (leitura de complexo)

O segundo pregão pleno desde a reabertura testou, de novo, os mesmos pilares estruturais
que o primeiro havia revertido — e desta vez o resultado foi uma reversão parcial na
direção oposta, não uma continuação. O oil share recuou de 50,56% (08/09) para **50,37%**
(09/09, indicators), devolvendo parte do ganho do dia anterior mas seguindo acima de 50%.
O oil-meal spread encolheu de +0,1716 para **+0,1144** USD/bushel — o óleo segue "pagando
mais" que o farelo dentro do crush, mas com menos folga do que ontem. E os índices
sintéticos ISF/ISO, que haviam saltado juntos de 60/80 para 80/100 na sessão anterior,
permaneceram **exatamente parados em 80/100** hoje (indicators, 09/09) — nem a alta do
farelo nem a queda do óleo de hoje foram suficientes para mover a leitura estrutural na
direção oposta. Esse é o dado mais importante desta seção: depois de duas sessões
consecutivas de reversão de preço em direções opostas, os índices que supostamente
capturam a "estrutura" do crush não se moveram nenhuma vez — o que levanta a pergunta
genuína (sem resposta nos dados disponíveis) de qual seria a magnitude de movimento
necessária, em qualquer direção, para de fato deslocar o ISF/ISO de seus patamares
atuais.

O crush margin fechou em US$ 2,2069/bushel em 09/09 (**+4,38%** sobre 08/09), a nona
sessão seguida abaixo do referencial de US$ 2,50
(`alerta-quebra_suporte-complexo_soja-2026-09-09`), mas com a distância percentual
encolhendo de -15,28% para **-11,72%** — a melhora, aqui, veio principalmente da queda da
soja (-0,57%) superando o efeito líquido de farelo subindo (+0,50%) e óleo caindo
(-0,26%): quando o insumo (soja) fica mais barato mais rápido do que os produtos
(farelo+óleo) caem no conjunto, a margem de esmagamento se recupera mesmo sem alta nos
produtos finais.

O ratio Far/Soj, tratado em detalhe na seção Farelo, encerrou a sessão em 79,08%,
recuperando **+0,83 ponto percentual** e reduzindo a distância até 80% para **0,92 ponto
percentual** — a maior proximidade desse patamar desde a aproximação original de 79,76%
em 04/09, que motivou a expectativa de convergência tratada em profundidade no veredito
D+90 de ontem ([[2026-09-09_d90-ratio-far-soj-reverte-na-vespera]]). A diferença central
frente àquele episódio é que, desta vez, o ratio está subindo depois de já ter sido
"testado" por um dia de preço fresco na direção contrária (a queda de 08/09) — ou seja,
não é mais uma aproximação construída em cima de dias sem pregão, mas uma recuperação
real dentro de um mercado já negociando ativamente. Isso não muda o veredito factual da
revisão D+90 (a tese de abundância "não foi invalidada" pelos 90 dias corridos), mas
reduz a margem de conforto desse veredito para o próximo pregão: um cruzamento de 80%
amanhã ou depois seria o primeiro rompimento genuíno do patamar em toda a vida da tese,
não apenas mais uma aproximação revertida.

Do lado dos fundamentos brasileiros de médio prazo (ABIOVE, projeções mensais para
set-dez/2026, sem revisão nesta janela), o balanço projetado continua mostrando o
esvaziamento sazonal esperado: estoque final de soja recuando de 7.912 mil toneladas
(set/26) para 5.721 (out/26), 3.659 (nov/26) e 1.890 mil toneladas (dez/26), a produção de
farelo caindo de 2.129 para 1.659 mil toneladas no mesmo período, e a exportação de
farelo recuando de 1.100 para 700 mil toneladas — uma trajetória que, se confirmada, tende
a aliviar a oferta doméstica de farelo ao longo do próximo trimestre e apoiar uma
recuperação futura do ratio Far/Soj por razões estruturais, independentemente de qual
lado vencer a oscilação diária de curto prazo.

## Lente fiscal/regulatória BR

Antes de fechar qualquer tese de preço BR, os vetores tributários/regulatórios vivos que
pesam no complexo — todos do `system/tributario_watch.toml`, cujo carimbo mais recente
(`atualizado_em`) em todos os 10 eventos catalogados é 2026-06-05, ou seja, **97 dias sem
revisão humana** frente a hoje (10/09):

- **MP 1.363/2026** (id `MP-1363-2026`, subvenção diesel fóssil R$ 1,12/L, vigente até
  31/12/2026): barateia o diesel fóssil no mix B15, reduzindo a competitividade relativa
  do biodiesel e a demanda doméstica por óleo de soja — vetor estrutural de baixa para
  óleo, direção "baixa" no cadastro, sem mudança de status. Não confundir com a margem de
  biodiesel AMERICANA (mercado e mecanismo diferentes), que hoje saltou +14,85% por
  causa do heating oil e do próprio óleo mais barato, não por qualquer efeito desta MP.
- **B16 (id `B16-CNPE-2026`, elevação da mistura de biodiesel para 16%)** segue "adiado"
  — resultado dos testes técnicos esperado por volta de novembro/2026. Upside represado
  (~436 mil toneladas de demanda potencial adicional de óleo, direção "alta" no
  cadastro), não corrente. Com o oil share hoje em 50,37% (ainda acima de 50%, mas
  recuando ligeiramente), um estímulo futuro de demanda por óleo via B16 encontraria um
  cenário estrutural moderadamente favorável, mas menos folgado do que o de ontem.
- **Isenção de PIS/Cofins do biodiesel na mistura** (id `PISCOFINS-BIODIESEL-ISENCAO`):
  vigência registrada até 31/07/2026 — já **41 dias corridos vencida** frente a
  10/09/2026, sem qualquer registro de prorrogação ou expiração no arquivo. Status
  tratado como "desconhecido pós-vigência", não como fato de vigência ou caducidade.
- **MP 1.358/2026** (subvenção gasolina R$ 0,89/L): vigência registrada até 11/07/2026,
  agora **61 dias corridos vencida**, mesma lacuna de informação sobre renovação.
- **STJ REsp 2.165.276** (id `STJ-RESP-2165276`, crédito de PIS/Cofins sobre soja em
  biodiesel sob suspensão tributária, direção "alta" para soja/óleo): alívio de custo
  pontual, não vinculante, sem novidade nesta janela.
- **EPA RFS 2026/2027** (id `EPA-RFS-2026-2027`, mandato de biocombustível americano,
  vigente desde 15/06/2026, direção "alta" para óleo): sustenta o RIN D4, estável — o
  arcabouço regulatório segue intacto e ajuda a explicar por que a margem de biodiesel
  americana pôde saltar +14,85% hoje sem qualquer risco de mudança de crédito.
- **Crédito 45Z** (id `45Z-CLEAN-FUEL`, em tramitação, direção "mista"): sem novidade.
- **Indonésia — Danantara** (id `DANANTARA-INDONESIA`) e **levy de exportação PMK 9/2026**
  (id `INDONESIA-LEVY-PMK9`): a assunção plena da centralização da exportação de palma
  pela Indonésia tinha alvo 01/09/2026 — já se passaram **9 dias** sem qualquer notícia
  neste dump confirmando execução. Catalisador de alta represado para óleo (via
  substituição com palma), não invalidado nem confirmado.
- **Indonésia B50** (id `INDONESIA-B50`, monitorando, direção "alta"): sem novidade nesta
  janela.

## Riscos e eventos próximos

- **Terceiro pregão de confirmação (ou não) da oscilação farelo/óleo** — depois de duas
  sessões consecutivas revertendo uma à outra, o próximo fechamento é o teste mais
  imediato: se o ratio Far/Soj cruzar 80% pela primeira vez desde 11/06/2026, isso
  encerraria de fato a tese de abundância; se reverter de novo, o padrão de "um dia para
  cada lado" ganha mais um capítulo, reforçando a leitura de que o mercado ainda está
  descobrindo preço pós-pausa, não estabelecendo tendência.
- **Próximo corte CFTC COT** — posições de terça 08/09, publicação estimada para amanhã,
  sexta-feira 11/09 (inferência a partir do calendário semanal do CFTC, não confirmada no
  briefing) — o primeiro dado de posicionamento que vai mostrar se os fundos
  acompanharam a queda de 08/09, a alta de 09/09, ou nenhuma das duas. É o dado mais
  aguardado desta janela para validar ou contestar a leitura estrutural do ISF/ISO.
- **USDA Crop Progress semanal**: próximo corte esperado na segunda-feira 14/09.
- **USDA WASDE**: ausente da janela; catalisador potencial de revisão de balanço mundial.
- **NOPA mensal** (`release-nopa-2026-09-09`): terceiro dia seguido do mesmo falso
  positivo de paywall na fila — o gap de dado de crush americano segue sem solução.
- **Confirmação (ou não) da centralização plena da exportação de palma pela Danantara**
  — marco-alvo era 01/09, já se passaram 9 dias.
- **Vigência da isenção PIS/Cofins do biodiesel** (41 dias vencida) e **MP 1.358/2026 da
  gasolina** (61 dias vencida) — checar notícia de renovação/expiração antes de assumir
  qualquer tese de custo de combustível BR.
- **Clima**: previsão de 10/09 (hoje) mantém chuva e trovoadas generalizadas no núcleo
  produtor de Mato Grosso e Goiás, com temperaturas altas (Cuiabá, Sinop, Sorriso e Lucas
  do Rio Verde entre 37-38°C de máxima) e no Sul (Cascavel/PR, Maringá/PR, Passo
  Fundo/RS) sem menção de geada — pano de fundo relevante para a janela de plantio da
  safra 2026/27 que se aproxima, ainda sem impacto direto sobre a soja (ainda não
  plantada na região).

## Honestidade

- **O dump de hoje não contém as linhas brutas de CME CBOT para soja e óleo na data de
  08/09** — apenas farelo e heating oil têm linha própria de preço para aquele dia
  (farelo fechamento 343,30, volume 32.108). Os valores de soja (1.316,25) e óleo (70,22)
  usados nas comparações desta leitura foram reconstruídos a partir das fórmulas dos
  indicadores sintéticos de 08/09 (`soja_paridade_br` e
  `biodiesel_us.custo_oleo_usd_galao`), não de uma linha de preço bruta própria — um gap
  real na janela de dados disponível, não um erro de leitura.
- **Pelo mesmo motivo, não há comparação direta de volume dia-a-dia para soja e óleo em
  08/09 nesta janela do dump** — os números de 126.269 (soja) e 17.491 (óleo) contratos
  usados como referência do primeiro pregão pós-pausa vêm citados via
  [[2026-09-09_leitura-complexo]] (leitura de ontem), não de uma linha própria deste
  dump.
- **O COT de 01/09 tem agora 9 dias corridos de defasagem frente a hoje, e cobre um
  período anterior a três sessões inteiras de preço fresco (04, 08 e 09/09)** — não há
  como saber, com os dados disponíveis, como os fundos reagiram a nenhuma das duas
  reversões diárias observadas até aqui.
- **Percentil histórico de posicionamento COT não está disponível no briefing** — toda
  leitura de "fundos comprando/vendendo" usa variação semana a semana de contratos
  absolutos, não percentil histórico.
- **A estabilidade total do ISF/ISO ao longo de duas sessões de preço em direções opostas
  é, ela mesma, um dado que merece registro, não apenas uma observação de passagem** — não
  há, nos dados disponíveis, uma forma de saber qual seria a magnitude de movimento de
  preço/ratio necessária para de fato deslocar esses índices discretos de seus patamares
  atuais (80/100 e 100/100). Isso não invalida os índices, mas pede cautela em tratá-los
  como sinal de alta frequência.
- **`tributario_watch.toml` sem atualização há 97 dias** — pelo menos dois vetores
  (isenção PIS/Cofins do biodiesel, MP 1.358/2026) já passaram da data de vigência
  registrada sem nota de renovação ou expiração. Tratados como "status desconhecido
  pós-vigência", não como fato de caducidade real.
- **NOPA segue inacessível** (paywall) — nova "release" carimbada em 09/09 é o terceiro
  falso positivo seguido na fila, sem dado novo de fato.
- **USDA WASDE ausente** da janela — nenhuma leitura de balanço mundial oficial
  atualizado disponível.
- **A previsão INMET para 10/09 é previsão meteorológica, não medição de precipitação
  real** — a ausência de menção a "geada" no boletim de hoje para Passo Fundo/RS é
  tratada como sinal indicativo, não como confirmação de que a geada efetivamente
  cessou.
- **Prêmios de exportação (Paranaguá, farelo e óleo) seguem congelados há 13-14 dias
  corridos** (desde 27/08) — não dá para saber se isso reflete mercado físico export
  realmente parado ou limitação de atualização da fonte (NAG).
- **O físico brasileiro de farelo (MT/IMEA, Rondonópolis, RS) segue sem nenhuma reação**
  tanto à queda de Chicago em 08/09 quanto à alta de 09/09 — cinco dias corridos sem
  variação, o que amplia a dúvida sobre se o físico doméstico está genuinamente
  desconectado da CBOT ou se a fonte (NAG) simplesmente não está atualizando esses
  pontos específicos.
- **MPOB (palma Malásia) segue com parser quebrado** — nenhum dado de produção/estoque de
  palma malaia disponível para cruzar com a tese de substituição via Indonésia.
- **BCBA (Argentina) segue sem links de relatório detectados pelo scraper** — nenhum dado
  de safra ou exportação argentina disponível nesta janela.
- **A fila de julgamento repete o item de revisão D+90 do ratio Far/Soj como "vencendo em
  0d" mesmo depois de o marco já ter sido tratado em profundidade ontem** — isto parece
  ser um eco do sistema de geração de fila (que provavelmente não lê de volta os
  insights já escritos em `insights/*.md` para marcar a revisão como encerrada), não uma
  nova revisão genuína. Tratado aqui como continuidade do mesmo veredito, com o dado
  novo de hoje (ratio subindo para 79,08%) incorporado como atualização, não como um
  novo ciclo de revisão independente.
- **A divergência entre a margem de biodiesel americana (máxima da janela) e o preço do
  óleo (em queda) nesta sessão é uma leitura interpretativa, não um fato medido
  diretamente** — o briefing não contém nenhum dado de fluxo de compra física de óleo por
  produtores de biodiesel que confirme se essa margem mais alta já está gerando demanda
  incremental.
