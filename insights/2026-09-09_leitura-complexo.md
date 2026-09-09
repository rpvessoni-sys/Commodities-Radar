---
data: 2026-09-09
titulo: "O primeiro preço fresco em quatro dias reverte a narrativa da semana — farelo cai, óleo sobe, e o ratio Far/Soj se afasta de 80% bem no dia em que a revisão D+90 da tese original vencia"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT (ZSX26 soja / ZMV26 farelo / ZLV26 óleo) — sessão de 2026-09-08 (terça-feira), a primeira negociada desde a sexta-feira 04/09. Soja: abertura 1.315,25, máxima 1.321,25, mínima 1.304,00, fechamento 1.316,75 USD cts/bushel, volume 126.269 contratos. Farelo: abertura 348,30, máxima 348,80, mínima 341,30, fechamento 343,60 USD/short ton, volume 25.777 contratos. Óleo: abertura 69,25, máxima 70,31, mínima 68,73, fechamento 70,24 USD cts/lb, volume 17.491 contratos. Curva futura em 08/09 — soja: set/26 1.297,75, nov/26 (base) 1.316,75, jan/27 1.332,50, mar/27 1.339,25, mai/27 1.344,50, jul/27 1.345,50; farelo: set/26 341,20, out/26 (base) 343,60, dez/26 350,10, jan/27 353,10, mar/27 355,50, mai/27 357,20; óleo: out/26 (base) 70,24, dez/26 70,73, jan/27 70,95, mar/27 71,09, mai/27 71,14
  - CME CBOT 2026-09-04 (sexta-feira, última sessão de referência antes da pausa, conforme reproduzida no briefing de 2026-09-08 e na leitura [[2026-09-08_leitura-complexo]]) — soja fechamento 1.309,75 (volume 167.214), farelo fechamento 348,20 (volume 27.570), óleo fechamento 68,89 (volume 32.370), heating oil fechamento 4,5402 USD/galão
  - CME NYMEX heating oil (HO=F) — 2026-09-08: abertura 4,6205, máxima 4,6415, mínima 4,6205, fechamento 4,6343 USD/galão, volume 119 contratos; 2026-09-07: fechamento 4,6646, volume 12.055; 2026-09-06 (domingo, reabertura): abertura 4,5804, máxima 4,5950, mínima 4,5659, volume 497, sem campo de fechamento nesta janela do dump
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, ISF, ISO, margem biodiesel, paridade BR) — 2026-09-08, primeiro recálculo com insumo de preço fresco desde 2026-09-04
  - BCB PTAX — 2026-09-08: USD/BRL 5,0856, EUR/BRL 5,913, Selic diária 0,05166% a.a. (séries SGS 1, 21619, 11), primeira publicação nova desde 04/09
  - CEPEA/ESALQ Soja Paranaguá via NAG — 2026-09-08: R$ 160,46/saca (var -0,25%)
  - CEPEA/ESALQ Soja Paraná interior via NAG — 2026-09-08: R$ 152,23/saca (var +0,09%)
  - NAG Físico BR — 2026-09-08: farelo MT/IMEA R$ 1.875,45/ton (var 0,0%, congelado desde 04/09), Rondonópolis/MT R$ 1.900,00/ton (congelado), RS média R$ 1.860,00/ton (congelado); prêmios export Paranaguá farelo +0,12 USD/short ton e óleo +0,10 cts/lb, ambos congelados desde pelo menos 2026-08-27 (12 dias corridos)
  - CFTC COT Managed Money, Swap Dealers e Producer/Merchant — corte de 2026-09-01 (terça-feira), sem atualização nesta janela, agora 8 dias corridos de defasagem frente a hoje
  - USDA Crop Progress — novo corte, semana encerrada em 2026-09-06: 12% excelente / 46% boa / 9% ruim (G/E 58%), idêntico ao corte anterior de 2026-08-30; defasagem cai de 9 para 3 dias corridos
  - USDA WASDE — ausente da janela deste briefing
  - NOPA — fila `release-nopa-2026-09-08`; `monthly_status` segue em 0,0 bool (paywall) em todas as datas do dump, de 2026-08-27 a 2026-09-08
  - ABIOVE projeções mensais — balanços set-dez/2026, sem revisão nesta janela
  - NOAA CPC ENSO — El Niño Advisory, inalterado até 2026-09-08
  - MPOB — carimbo 2026-09-08, parser sem números extraídos (mesma barreira, 3.456 caracteres)
  - BCBA (Argentina) — carimbo 2026-09-08, scraper acessa a página mas não encontra links de relatório
  - INMET — previsão para 2026-09-09 (HOJE): chuva e trovoadas generalizadas no núcleo produtor de Mato Grosso e Goiás (Cuiabá 35°C/24°C, Sinop 36°C/23°C, Sorriso 35°C/23°C, Lucas do Rio Verde 36°C/23°C, Rio Verde/GO 32°C/21°C) e no Sul (Cascavel/PR 21°C/16°C, Maringá/PR 23°C/17°C, Passo Fundo/RS 24°C/11°C — sem menção de geada no boletim de hoje, ao contrário dos dias anteriores)
  - Notícias Agrícolas/Canal Rural + FarmProgress RSS — 2026-09-08: "160 items lidos, 5 mantidos (soja/farelo/oleo)", manchete "Why September may be a turning point for soybeans" (FarmProgress)
  - CEPEA RSS — 2026-09-08: 103 itens parseados, sem manchete legível nova; última manchete disponível permanece a de 04/09 ("Alta dos preços ganha força no início de setembro")
  - system/tributario_watch.toml (lido como referência, não editado) — `atualizado_em` 2026-06-05 em todos os 10 eventos catalogados, agora 96 dias sem revisão
  - Forecasts estatísticos internos (bandas 7d/30d, MA20+volatilidade+slope) — geração de 2026-09-08, alvos 15/09 (7d) e 08/10 (30d); viés "altista" em soja e farelo nos dois horizontes, "lateral" no óleo em 7d e "altista" em 30d, calculado sobre o fechamento fresco de 08/09
  - Fila de julgamento — carimbada 2026-09-08 no briefing, 7 itens; tratados nesta leitura: `alerta-quebra_resistencia-soja_cbot-2026-09-08`, `alerta-quebra_suporte-oleo_cbot-2026-09-08`, `alerta-quebra_resistencia-farelo_cbot-2026-09-08`, `alerta-quebra_suporte-complexo_soja-2026-09-08`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, `release-nopa-2026-09-08`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`
  - Cruza com [[2026-09-08_leitura-complexo]] (leitura de ontem, que documentou cinco sessões de estabilidade estrutural favorável ao farelo) e com [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (tese original do spread Far/Soj, cuja revisão D+90 vence hoje) e com [[2026-09-09_d90-ratio-far-soj-reverte-na-vespera]] (aprofundamento dedicado ao veredito da revisão D+90)
status: ativa
vies: [bull-soja, bear-farelo, bull-oleo_soja]
---

## Visão geral

Hoje, quarta-feira 09/09/2026, o briefing traz pela primeira vez em quatro dias um
fechamento genuinamente fresco: a sessão de terça-feira 08/09, a primeira negociada na
CBOT (bolsa de grãos de Chicago) desde a sexta-feira 04/09, depois do fim de semana e do
feriado duplo de segunda (Labor Day nos EUA e Independência do Brasil, coincidência de
calendário). E esse primeiro preço fresco não confirmou a narrativa que vinha se
consolidando havia cinco sessões — ele a inverteu. Para quem não acompanha o dia a dia:
a soja em grão vira, na esmagadora (o processo de "crush"), dois produtos com demandas
diferentes — farelo (proteína para ração animal) e óleo (alimentação humana e biodiesel).
O crush margin mede, em dólares por bushel (unidade agrícola americana, ~27,2 kg de
soja), quanto sobra para quem esmaga depois de vender farelo + óleo e pagar a soja. O
oil share (fatia do valor total do crush que vem do óleo, os dois somando 100%) diz qual
dos dois produtos está "pagando a conta" da esmagadora: quando o oil share sobe, o óleo
manda e o farelo vira insumo residual, mais barato, "sobra" — daí o índice sintético
interno "Índice de Sobra de Farelo" (ISF). Quando o oil share cai, o farelo passa a
sustentar o crush e o óleo perde força relativa, o que o índice espelhado "Índice de
Suporte do Óleo" (ISO) capta pelo lado inverso. O ratio Far/Soj (preço do farelo dividido
pelo preço da soja, normalizado) é a métrica clássica de mercado para a mesma ideia:
abaixo de 80% o farelo está "abundante" (barato relativo à soja, viés baixista); a partir
de 87% ele está "apertado" (caro relativo à soja, viés altista).

Nas últimas cinco leituras diárias (03 a 07/09), com o mercado sem negociar desde
sexta-feira, o ratio Far/Soj vinha subindo (78,51% → 79,45% → 79,76%) e os índices
sintéticos ISF/ISO estavam parados em 60/100 e 80/100 havia cinco carimbos de data
seguidos — um quadro que a leitura de ontem descreveu como "o mais favorável à
convergência" desde a abertura da tese, na véspera exata do vencimento da revisão formal
D+90 (2026-09-09, hoje) da tese de compressão do spread Far/Soj aberta em 11/06/2026
(`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`). O primeiro
fechamento fresco, o de 08/09, respondeu de forma direta a essa expectativa — mas na
direção contrária à que vinha se desenhando: farelo caiu -1,32% (CME CBOT), óleo subiu
+1,96%, o ratio Far/Soj recuou de 79,76% para **78,28%** (indicators, 08/09) — afastando-
se do patamar de 80%, não se aproximando dele — e os índices sintéticos romperam a
persistência de cinco sessões, saltando de 60/80 para **80/100** (ISF/ISO, indicators,
08/09). Em outras palavras: no dia exato em que a tese de convergência precisava de
confirmação, o mercado real votou pelo cenário oposto. **Leitura de uma linha**: o pivô do
complexo continua sendo a realocação de valor entre farelo e óleo dentro do crush, mas
hoje esse pivô girou de volta para o óleo — bear-farelo, bull-óleo — exatamente no dia da
revisão formal, enquanto a soja segue com viés altista moderado, agora com a primeira
confirmação de preço fresco desde o rompimento técnico de julho. Confiança **moderada**
(não alta): é uma única sessão, com volume abaixo do que se vê em pregões plenos de dia
útil nas três pernas, e ainda sem COT fresco para confirmar se os fundos acompanharam o
movimento.

## Soja

**Viés: bull, moderado — primeiro fechamento fresco desde o rompimento confirma a folga
técnica sobre a resistência de julho, com alta modesta mas real, mesmo com o real se
valorizando frente ao dólar.**

O que sustenta a tese:

- **O rompimento técnico de julho passou pelo primeiro teste real de preço e resistiu.**
  Soja CBOT fechou em 1.316,75 USD cts/bushel em 08/09/2026 (CME CBOT), **+0,53%** sobre
  os 1.309,75 de 04/09 — a primeira variação de preço da semana, depois de quatro dias
  corridos sem pregão. A folga sobre a resistência de 1.180,00 monitorada pela fila
  (`alerta-quebra_resistencia-soja_cbot-2026-09-08`) ampliou-se para **11,59%**, ante
  10,99% na sexta. O contrato negociou entre 1.304,00 e 1.321,25 (máxima/mínima, CME
  CBOT) — um range de 17,25 pontos (~1,3% do preço) — e fechou perto do topo do range,
  sinal de que compradores absorveram as vendas ao longo da sessão em vez de perder
  força no fechamento.
- **O volume da reabertura ficou abaixo do volume da última sessão plena, o que pede
  cautela sobre a força do movimento.** 126.269 contratos em 08/09 (CME CBOT) contra
  167.214 em 04/09 — uma queda de **-24,5%**. É normal um primeiro pregão pós-feriado
  vir mais fino, mas isso significa que a alta de +0,53% não teve a mesma convicção de
  participação que o pregão anterior, e o mercado ainda não testou a resistência com
  volume pleno desde o rompimento original.
- **O câmbio trabalhou CONTRA o produtor brasileiro nesta janela, ao contrário da
  leitura de ontem.** USD/BRL fechou 08/09 em 5,0856 (BCB PTAX), **-0,78%** sobre os
  5,1253 de 04/09 — o real se valorizou. A paridade em reais da soja (CBOT × câmbio, sem
  basis) fechou em **R$ 147,63/saca** (indicators, 08/09), uma queda de -0,24% mesmo com
  a soja em dólar subindo +0,53% — o mecanismo inverso ao de sexta-feira: agora é a
  valorização do real que compensa (e supera) o ganho em Chicago. É o mesmo lembrete de
  sempre, na direção oposta: para quem vende em reais, a combinação dos dois preços
  manda, não cada um isolado.
- **O físico exportador confirma a mesma divergência.** CEPEA/ESALQ Soja Paranaguá (via
  NAG) fechou 08/09 em R$ 160,46/saca, -0,25% sobre 160,87 — recuo coerente com a
  valorização cambial, mesmo com o dólar em alta em Chicago. Já o físico do Paraná
  interior (via NAG) subiu ligeiramente, R$ 152,23/saca (+0,09% sobre 152,10) — os dois
  físicos praticamente estáveis, absorvendo o cabo de guerra entre CBOT em alta e real
  mais forte.
- **A condição da lavoura americana recebeu confirmação fresca e ficou estável.** USDA
  Crop Progress divulgou um novo corte, referente à semana encerrada em 2026-09-06,
  mostrando "boa+excelente" (G/E) em **58%** (12% excelente + 46% boa, "ruim" em 9%) —
  exatamente igual ao corte anterior de 30/08. A defasagem cai de 9 para **3 dias
  corridos**, a mais curta desde o início desta série de leituras. O mecanismo: a
  estabilização (nem piora nem melhora) reduz o risco de um choque de revisão de
  produtividade no próximo relatório, mas também não reforça ativamente a tese — é um
  pilar neutro que deixou de ser um risco de deterioração acelerada.

**O que invalida / risco:**

- **O volume fraco da reabertura é o principal ponto de atenção.** Uma alta de +0,53%
  com -24,5% de volume não é o tipo de confirmação que dissipa dúvida sobre a força do
  rompimento; um pregão pleno nos próximos dias, com volume normalizado, é o teste que
  ainda falta.
- **O crush margin caiu para a mínima da janela, agora oitava sessão seguida abaixo do
  referencial de US$ 2,50** monitorado pela fila
  (`alerta-quebra_suporte-complexo_soja-2026-09-08`): fechou em **US$ 2,1181/bushel**
  (08/09), **-15,28%** abaixo do referencial — pior que os -14,37% de sexta. Uma margem
  de esmagamento comprimida por período prolongado tende a reduzir o incentivo da
  indústria para processar soja, o que no médio prazo pesa sobre a demanda física por
  grão — ainda que, como será detalhado nas seções Farelo e Óleo, a composição da
  compressão trocou de lado nesta sessão.
- **Nível técnico a vigiar:** um fechamento de volta abaixo de 1.180 desfaria o
  rompimento; a folga (11,59%) segue confortável e agora testada por preço fresco, não
  apenas congelada.

**Leitura operacional:** o primeiro teste de preço desde o rompimento validou a tese sem
contestá-la, mas sem convicção plena de volume — não há gatilho para reduzir posição
comprada, mas também não há motivo para aumentar agressivamente com esse nível de
participação. Para quem opera o lado vendido isoladamente em soja, ainda não há sinal de
reversão técnica; o nível a vigiar continua sendo 1.180. Do ponto de vista de câmbio, quem
opera a paridade em reais (long soja BRL) precisa notar que o real se valorizou justamente
no dia em que o grão subiu em dólar — umande equilíbrio que reduz a magnitude do ganho em
reais e é um lembrete de que a tese de soja em BRL depende dos dois lados, não só de
Chicago.

## Farelo

**Viés: bear, moderado — a primeira sessão negociada em quatro dias inverteu a recuperação
que vinha se desenhando havia duas semanas, e o fez exatamente no dia do vencimento da
revisão formal D+90 da tese original de abundância. Ainda acima da resistência técnica de
325, mas a estrutura por trás do preço virou contra o farelo nesta sessão.**

O que pressiona a tese, na sessão fresca de hoje:

- **O preço recuou depois de quatro dias de estabilidade congelada.** Farelo CBOT fechou
  em 343,60 USD/short ton em 08/09/2026 (CME CBOT), **-1,32%** sobre os 348,20 de 04/09
  — a primeira variação negativa desde a sequência de altas de 02-03/09. O contrato
  negociou entre 341,30 e 348,80 (mínima/máxima, CME CBOT) e fechou perto da mínima do
  dia, sinal de pressão vendedora que se intensificou ao longo da sessão, não o
  contrário. A folga sobre a resistência de 325,00
  (`alerta-quebra_resistencia-farelo_cbot-2026-09-08`) ainda é de **5,72%**, mas encolheu
  frente aos 7,14% de sexta.
- **O ratio Far/Soj reverteu a recuperação de duas sessões e se afastou do patamar-chave
  de 80%.** Fechou em **78,28%** em 08/09 (indicators), ante 79,76% em 04/09 — um recuo
  de **-1,48 ponto percentual** na primeira sessão fresca, desfazendo mais da metade do
  ganho acumulado de +1,25 p.p. que havia sustentado a expectativa de convergência.
  A distância até 80% voltou a abrir para **1,72 ponto percentual**, mais do que o
  sêtuplo da distância de sexta-feira (0,24 p.p.). Na definição do próprio indicador
  (<80% = "abundante", >=87% = "apertado"), o farelo permanece — e se reafirma — na zona
  de abundância, não na de transição para escassez.
- **Os índices sintéticos romperam cinco sessões de estabilidade, e na direção
  contrária à esperada.** O Índice de Sobra de Farelo (ISF) saltou de 60/100 ("sobra
  relevante", 3 de 5 condições atendidas) para **80/100** ("forte pressão baixista no
  farelo", 4 de 5 condições, indicators, 08/09) — o mesmo nível que havia aparecido
  brevemente em 01-02/09 antes da melhora recente. O mecanismo: o índice combina sinais
  de preço, ratio e estrutura de crush; quando mais condições apontam simultaneamente
  para excesso de oferta de farelo, o índice sobe, e ele subiu justamente na sessão em
  que o preço caiu e o ratio recuou.
- **O oil-meal spread virou de negativo para positivo em uma única sessão.** Fechou em
  **+0,1672 USD/bushel** em 08/09 (indicators, valor do óleo menos valor do farelo),
  revertendo os -0,0825 de 04/09 — um giro de +0,2497 USD/bushel. Isso significa que,
  dentro do crush, o óleo voltou a "pagar a conta" mais do que o farelo — o oposto exato
  da leitura que vinha sustentando a tese de farelo forte / óleo fraco.
- **O físico brasileiro ainda não reagiu — o que deixa uma pergunta aberta, não uma
  confirmação.** Farelo MT/IMEA (NAG) permaneceu em R$ 1.875,45/ton em 08/09 (var 0,0%),
  o mesmo nível desde 04/09; Rondonópolis (R$ 1.900,00/ton) e a média do RS (R$
  1.860,00/ton) também congelados. O prêmio de exportação em Paranaguá segue travado em
  +0,12 USD/short ton há pelo menos 12 dias corridos (desde 27/08, NAG). Ou seja, o
  movimento de queda em Chicago ainda não tem contrapartida visível no físico
  doméstico — pode ser apenas defasagem normal de repasse, ou pode ser sinal de que o
  físico brasileiro está mais firme do que a CBOT sugere; os dados disponíveis não
  permitem decidir qual.

**Trata a fila `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
(seguindo 🔴 VENCIDA no briefing):** já são **90 dias corridos** desde o alerta original
de 11/06/2026. O corte D+7 (18/06/2026) pedia checar se o ratio havia fechado abaixo de
80% — e, olhando a trajetória completa da janela coberta pelas leituras diárias, o ratio
passou a esmagadora maioria dos 90 dias abaixo de 80% (na zona "abundante"), com a
aproximação de 79,76% em 04/09 tendo sido a única vez, nesta janela de dados, em que
chegou a menos de 0,25 p.p. do patamar. A sessão fresca de hoje reafirma que essa
aproximação não se converteu em rompimento.

**Trata também `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`, que
vence HOJE, 2026-09-09:** o veredito, com o primeiro dado de preço fresco disponível
exatamente no dia da revisão, é que a tese original de 11/06/2026 — farelo abundante,
ratio comprimido, viés baixista estrutural — **não foi invalidada** pelos 90 dias
corridos. Pelo contrário: depois de uma recuperação de duas semanas que reduziu a
distância até 80% para quase zero, o primeiro fechamento fresco pós-pausa devolveu essa
distância para 1,72 p.p. e reforçou os índices sintéticos na mesma direção (ISF 80, ISO
100, oil-meal spread positivo). Esta leitura trata o veredito com mais profundidade em
[[2026-09-09_d90-ratio-far-soj-reverte-na-vespera]], mas o resumo operacional é: a
melhora observada em setembro foi real, mas não suficiente, e a primeira sessão de teste
puxou o quadro de volta para o lado da tese original.

**O que invalida / risco:** o contraponto mais relevante continua sendo o COT, agora com
**8 dias corridos de defasagem** — o corte de 01/09 mostrava o net long de managed money
em farelo tendo saltado +63,83% na semana anterior (95.953 → 157.179 contratos, CFTC
COT), o maior salto proporcional das três pernas. Se os fundos mantiveram essa convicção
comprada, a queda de preço de hoje pode ser uma correção técnica dentro de uma tendência
de alta ainda intacta do ponto de vista de posicionamento, não uma reversão de fundo. O
próximo corte (posições de 08/09) só sai por volta de sexta-feira 11/09 — dois dias
depois de hoje, mas ao menos mais perto do que a defasagem de 7 dias que vigorava até
ontem.

**Leitura operacional:** para quem está comprado em farelo diretamente, a sessão de hoje
é o primeiro sinal de alerta real desde o rompimento de agosto — a folga técnica ainda
existe (5,72%), mas encolheu, e a estrutura (ratio, ISF, oil-meal spread) virou contra a
posição na mesma sessão. Não é gatilho de saída forçada, mas é motivo para revisar o
tamanho da posição e vigiar se a queda de hoje ganha continuidade ou é ruído de um único
pregão de reabertura com volume abaixo do normal. Para quem opera o spread Far/Soj (long
farelo / short soja), o veredito da revisão D+90 pesa contra manter essa perna com a
convicção da semana passada — a assimetria que parecia se abrir a favor da convergência
se fechou de novo. Para quem quer iniciar posição vendida em farelo, hoje oferece o
primeiro dado de preço e estrutura alinhados nessa direção desde o início de setembro,
mas ainda sem confirmação de um segundo pregão nem de COT fresco.

## Óleo

**Viés: bull, moderado — depois de três quedas seguidas na fita antiga (04/09), a primeira
sessão fresca trouxe uma recuperação firme, com os índices estruturais saltando para o
patamar de dominância plena do óleo no crush. Ainda abaixo do suporte técnico rompido em
agosto, mas a composição interna do movimento virou a favor do óleo.**

O que sustenta a virada:

- **A queda de três sessões (fita de 02-04/09) foi interrompida com uma alta relevante na
  primeira sessão fresca.** Óleo CBOT fechou em 70,24 USD cts/lb em 08/09/2026 (CME
  CBOT), **+1,96%** sobre os 68,89 de 04/09 — a maior variação diária do complexo nesta
  sessão. O contrato negociou entre 68,73 e 70,31 (mínima/máxima, CME CBOT) e fechou
  muito perto do topo do range, sinal de compra concentrada ao longo do pregão. Mesmo
  assim, o fechamento de 70,24 permanece **2,44%** abaixo do suporte de 72,00 rompido em
  agosto (`alerta-quebra_suporte-oleo_cbot-2026-09-08`) — a recuperação foi real, mas
  não desfez o rompimento técnico.
- **A curva futura acompanhou a alta em toda a extensão.** Base (out/26) 70,24 → dez/26
  70,73 → jan/27 70,95 → mar/27 71,09 → mai/27 71,14 (CME CBOT, 08/09) — um contango
  moderado e coerente, sem distorção pontual isolada no contrato-base, o que reforça que
  o movimento de alta não é um efeito técnico de rolagem, mas reprecificação de toda a
  estrutura a termo.
- **Oil share e oil-meal spread revertem de forma nítida, com os índices sintéticos
  saltando para a dominância plena.** O oil share fechou em **50,55%** em 08/09
  (indicators) — de volta acima de 50% depois de quatro sessões consecutivas abaixo
  desse nível (51,17% em 01/09 até 49,73% em 04/09). O Índice de Suporte do Óleo (ISO)
  saltou de 80/100 para **100/100** — "óleo domina o crush", agora com as 5 de 5
  condições monitoradas atendidas (indicators, 08/09), o nível máximo da escala. O
  oil-meal spread, como já descrito na seção Farelo, virou de -0,0825 para **+0,1672**
  USD/bushel — o óleo voltou a valer mais do que o farelo dentro da conta do crush.
- **A margem de biodiesel americana recuou ligeiramente, mas por um motivo que reforça a
  leitura de força do óleo, não de fraqueza de demanda.** Margem de 1,7313 USD/galão em
  08/09, ante 1,7385 em 04/09 (indicators) — uma queda marginal de -0,41%. O mecanismo:
  o custo do óleo como insumo do biodiesel subiu para US$ 5,268/galão (7,5 lb × 70,24
  cts/lb), refletindo exatamente a alta do óleo em Chicago — ou seja, a margem cedeu
  porque o insumo ficou mais caro (sinal de força do óleo), não porque a receita (heating
  oil + crédito RIN) tenha caído. O heating oil (diesel de aquecimento americano,
  referência de receita do biodiesel) fechou 08/09 em 4,6343 USD/galão (CME NYMEX
  HO=F) — uma queda de -0,65% sobre 4,6646 de 07/09, mas ainda **+2,07%** acima do
  fechamento de sexta-feira (4,5402), então parte do salto do fim de semana persiste.
- **O RIN D4 (crédito de biocombustível, EPA) segue estável.** 1,5×RIN = 2,11 USD/galão
  embutido no cálculo de receita em 08/09 (indicators) — o arcabouço regulatório do EPA
  RFS 2026/2027 (`EPA-RFS-2026-2027`, vigente desde 15/06/2026) permanece intacto.

**O que invalida / risco:**

- **O volume da alta de hoje também ficou abaixo do padrão de um pregão pleno.** 17.491
  contratos em 08/09 (CME CBOT) contra 32.370 em 04/09 — queda de **-45,9%**, a maior
  entre as três pernas do complexo. É o segundo sinal (depois da soja e do farelo) de que
  a reabertura, embora direcional, ainda não teve participação plena — o que pede um
  segundo pregão de confirmação antes de tratar a virada como consolidada.
- **O COT de 01/09, com 8 dias de defasagem, ainda mostra os fundos líquidos compradores
  em óleo (+17,28% net long na semana anterior, CFTC COT), um dado anterior às quedas de
  03-04/09 e à alta de hoje.** Não há como saber, com os dados disponíveis, se essa
  posição comprada já capturou parte do movimento de hoje ou se os fundos reduziram
  exposição durante a queda e agora perderam o repique.
- **Nível técnico a vigiar:** a reconquista e sustentação de 72,00 (o suporte rompido em
  agosto) seria a confirmação técnica que falta; por ora, a alta de hoje ainda opera
  dentro da faixa rompida.

**Leitura operacional:** para quem está vendido em óleo direcional, a sessão de hoje é o
primeiro sinal de alerta real desde o rompimento de suporte — os índices estruturais
(oil share, ISO, oil-meal spread) reverteram em conjunto com o preço, o que é uma
confirmação mais forte do que apenas um dia de alta isolada. Ainda não é motivo para
zerar a posição vendida (o nível técnico de 72,00 segue intacto como referência), mas é
motivo para reduzir o tamanho ou apertar o stop. Para quem opera o spread farelo-óleo
dentro do crush (long farelo / short óleo em valor relativo), a assimetria que sustentava
essa perna na semana passada se inverteu nesta sessão — o trade oposto (long óleo / short
farelo, ou vender o spread) ganhou o primeiro dia de evidência a favor, tratando `id`
`alerta-quebra_suporte-oleo_cbot-2026-09-08` como um nível que segue rompido, mas cada vez
mais próximo de ser reconquistado.

## Spreads e crush (leitura de complexo)

O primeiro pregão fresco em quatro dias fez o que a ausência de preço não podia fazer:
testou, de uma só vez, todos os pilares estruturais que vinham sustentando a tese de
farelo forte / óleo fraco — e o resultado foi uma reversão simultânea em todos eles, não
apenas no preço isolado de uma perna. O oil share saltou de 49,73% (04/09) para **50,55%**
(08/09, indicators), voltando para o lado do óleo depois de quatro sessões abaixo de 50%.
O oil-meal spread girou de -0,0825 para **+0,1672** USD/bushel. E os índices sintéticos
ISF/ISO, que haviam sustentado o patamar 60/80 por cinco carimbos de data consecutivos
(03 a 07/09), saltaram juntos para **80/100** na primeira sessão de teste — a mudança de
regime que a persistência anterior sugeria ser "estrutural" durou exatamente até o
primeiro preço fresco chegar.

O crush margin fechou em US$ 2,1181/bushel em 08/09 (-1,06% sobre 04/09), a oitava sessão
seguida abaixo do referencial de US$ 2,50
(`alerta-quebra_suporte-complexo_soja-2026-09-08`), **-15,28%** abaixo desse nível — a
pior leitura da janela. Mas a composição da compressão trocou de lado: agora é o farelo
que cai (-1,32%) enquanto o óleo sobe (+1,96%) — o oposto exato do padrão descrito nas
leituras anteriores, em que o óleo puxava a compressão para baixo e o farelo praticamente
não se movia. Ou seja, o crush continua comprimido, mas por um motivo diferente do que
vinha sendo reportado: hoje é o farelo que pesa contra a margem, não o óleo.

O ratio Far/Soj, tratado em detalhe na seção Farelo, encerrou a sessão em 78,28%,
devolvendo a maior parte do avanço das duas semanas anteriores e reabrindo a distância
até 80% para 1,72 ponto percentual. Para quem opera o spread Far/Soj, o quadro de hoje é o
inverso do que a leitura de ontem descrevia: em vez de "o quadro mais favorável à
convergência desde a abertura da tese", agora se tem a primeira sessão de dado fresco
confirmando que a tese original de abundância de farelo (aberta em 11/06/2026) segue de
pé no dia exato da sua revisão formal D+90. A tensão que as leituras anteriores registravam
— COT ainda líquido comprador em óleo, sem contrapartida vendida simétrica — permanece sem
solução, mas agora aponta na mesma direção do preço e da estrutura, não contra eles: se os
fundos mantiveram a posição comprada em óleo até 01/09, a alta de hoje é coerente com essa
convicção, ao contrário da leitura anterior, em que a convicção comprada em óleo
contrariava a fraqueza de preço observada.

Do lado dos fundamentos brasileiros de médio prazo (ABIOVE, projeções mensais para
set-dez/2026, sem revisão nesta janela), o balanço projetado continua mostrando o
esvaziamento sazonal esperado: estoque final de soja recuando de 7.912 mil toneladas
(set/26) para 5.721 (out/26), 3.659 (nov/26) e 1.890 mil toneladas (dez/26), a produção de
farelo caindo de 2.129 para 1.659 mil toneladas no mesmo período, e a exportação de
farelo recuando de 1.100 para 700 mil toneladas — uma trajetória que, se confirmada, tende
a aliviar a oferta doméstica de farelo ao longo do próximo trimestre. Esse é um fator de
médio prazo que atua a favor de uma eventual recuperação futura do ratio Far/Soj, mesmo
que a leitura de curto prazo de hoje tenha caminhado na direção contrária — os dois
horizontes (dias vs. meses) não precisam concordar no sinal para ambos serem válidos.

## Lente fiscal/regulatória BR

Antes de fechar qualquer tese de preço BR, os vetores tributários/regulatórios vivos que
pesam no complexo — todos do `system/tributario_watch.toml`, cujo carimbo mais recente
(`atualizado_em`) em todos os 10 eventos catalogados é 2026-06-05, ou seja, **96 dias sem
revisão humana**:

- **MP 1.363/2026** (id `MP-1363-2026`, subvenção diesel fóssil R$ 1,12/L, vigente até
  31/12/2026): barateia o diesel fóssil no mix B15, reduzindo a competitividade relativa
  do biodiesel e a demanda doméstica por óleo de soja — vetor estrutural de baixa para
  óleo, direção "baixa" no cadastro, sem mudança de status. Não confundir com a margem de
  biodiesel AMERICANA (mercado e mecanismo diferentes), que hoje cedeu ligeiramente por
  causa do próprio óleo mais caro, não por fraqueza de demanda (ver seção Óleo).
- **B16 (id `B16-CNPE-2026`, elevação da mistura de biodiesel para 16%)** segue "adiado"
  — resultado dos testes técnicos esperado por volta de novembro/2026. Upside represado
  (~436 mil toneladas de demanda potencial adicional de óleo, direção "alta" no
  cadastro), não corrente. Com o oil share hoje de volta acima de 50% (50,55%), um
  estímulo futuro de demanda por óleo via B16 encontraria um cenário estrutural já mais
  favorável ao óleo do que o observado na semana passada.
- **Isenção de PIS/Cofins do biodiesel na mistura** (id `PISCOFINS-BIODIESEL-ISENCAO`):
  vigência registrada até 31/07/2026 — já **40 dias corridos vencida** frente a
  09/09/2026, sem qualquer registro de prorrogação ou expiração no arquivo. Status
  tratado como "desconhecido pós-vigência", não como fato de vigência ou caducidade.
- **MP 1.358/2026** (subvenção gasolina R$ 0,89/L): vigência registrada até 11/07/2026,
  agora **60 dias corridos vencida**, mesma lacuna de informação sobre renovação.
- **STJ REsp 2.165.276** (id `STJ-RESP-2165276`, crédito de PIS/Cofins sobre soja em
  biodiesel sob suspensão tributária, direção "alta" para soja/óleo): alívio de custo
  pontual, não vinculante, sem novidade nesta janela.
- **EPA RFS 2026/2027** (id `EPA-RFS-2026-2027`, mandato de biocombustível americano,
  vigente desde 15/06/2026, direção "alta" para óleo): sustenta o RIN D4, estável — o
  arcabouço regulatório segue intacto e ajuda a explicar por que a margem de biodiesel
  americana continua acima de US$ 1,70/galão mesmo com o custo do óleo em alta hoje.
- **Crédito 45Z** (id `45Z-CLEAN-FUEL`, em tramitação, direção "mista"): sem novidade.
- **Indonésia — Danantara** (id `DANANTARA-INDONESIA`) e **levy de exportação PMK 9/2026**
  (id `INDONESIA-LEVY-PMK9`): a assunção plena da centralização da exportação de palma
  pela Indonésia tinha alvo 01/09/2026 — já se passaram **8 dias** sem qualquer notícia
  neste dump confirmando execução. Catalisador de alta represado para óleo (via
  substituição com palma), não invalidado nem confirmado; a alta do óleo de hoje não tem
  nenhuma ligação identificável com esse vetor no dado disponível.
- **Indonésia B50** (id `INDONESIA-B50`, monitorando, direção "alta"): sem novidade nesta
  janela.

## Riscos e eventos próximos

- **Confirmação (ou reversão) do movimento de hoje na próxima sessão** — depois de um
  dia de reversão em todas as três pernas com volume abaixo do normal, o próximo
  fechamento é o teste mais imediato: se farelo continuar caindo e óleo continuar
  subindo com volume normalizado, a virada ganha peso estrutural; se o movimento de hoje
  reverter, ele fica catalogado como ruído de reabertura de um único pregão fino.
- **Próximo corte CFTC COT** — posições de terça 08/09, publicação estimada por volta de
  sexta 11/09 (inferência a partir do calendário semanal do CFTC, não confirmada no
  briefing) — o primeiro dado de posicionamento que vai mostrar se os fundos
  acompanharam ou não a reversão de hoje. É o dado mais aguardado desta janela para
  validar ou contestar a leitura estrutural.
- **USDA Crop Progress semanal**: novo corte já recebido (semana de 06/09, G/E 58%,
  estável); o próximo é esperado na segunda-feira 14/09.
- **USDA WASDE**: ausente da janela; catalisador potencial de revisão de balanço mundial.
- **NOPA mensal** (`release-nopa-2026-09-08`): mensagem de paywall idêntica em todas as
  datas do dump — o gap de dado de crush americano segue sem solução.
- **Confirmação (ou não) da centralização plena da exportação de palma pela Danantara**
  — marco-alvo era 01/09, já se passaram 8 dias.
- **Vigência da isenção PIS/Cofins do biodiesel** (40 dias vencida) e **MP 1.358/2026 da
  gasolina** (60 dias vencida) — checar notícia de renovação/expiração antes de assumir
  qualquer tese de custo de combustível BR.
- **Clima**: previsão de 09/09 (hoje) mantém chuva e trovoadas generalizadas no núcleo
  produtor de Mato Grosso e Goiás, e no Sul (Cascavel/PR, Maringá/PR, Passo Fundo/RS) sem
  menção de geada no boletim — indicativo de transição mais consolidada para a
  primavera no Rio Grande do Sul, relevante como pano de fundo para a janela de plantio
  da safra 2026/27 que se aproxima, ainda sem impacto direto sobre a soja (ainda não
  plantada na região).

## Honestidade

- **O primeiro fechamento fresco em quatro dias trouxe volume abaixo do normal nas três
  pernas** (soja -24,5%, farelo dado indisponível para comparação direta nesta janela do
  dump mas citado via leitura anterior, óleo -45,9%, todos vs. 04/09, CME CBOT) — a
  reversão de direção é real e coerente entre preço e índices estruturais, mas a
  participação reduzida de um primeiro pregão pós-feriado pede confirmação em uma
  segunda sessão antes de tratar o giro como definitivamente consolidado.
- **O COT de 01/09 tem agora 8 dias corridos de defasagem frente a hoje (09/09), e o
  próximo corte (posições de 08/09) só será publicado depois de mais alguns dias** — não
  há como saber, com os dados disponíveis, se os fundos que estavam líquidos compradores
  em óleo e vendendo posição curta em farelo até 01/09 mantiveram, ampliaram ou
  reduziram essas posições diante da reversão de preço de hoje.
- **Percentil histórico de posicionamento COT não está disponível no briefing** — toda
  leitura de "fundos comprando/vendendo" usa variação semana a semana de contratos
  absolutos, não percentil histórico.
- **`tributario_watch.toml` sem atualização há 96 dias** — pelo menos dois vetores
  (isenção PIS/Cofins do biodiesel, MP 1.358/2026) já passaram da data de vigência
  registrada sem nota de renovação ou expiração. Tratados como "status desconhecido
  pós-vigência", não como fato de caducidade real.
- **NOPA segue inacessível** (paywall) — nova "release" carimbada em 08/09 não trouxe
  dado novo; tratado como falso positivo repetido na fila, não como dado novo relevante.
- **USDA WASDE ausente** da janela — nenhuma leitura de balanço mundial oficial
  atualizado disponível.
- **A comparação de volume de farelo entre 04/09 e 08/09 usa o valor de 04/09 reproduzido
  no briefing anterior (27.570 contratos), não confirmado diretamente neste dump** — o
  número está sourced de forma indireta (via a leitura de ontem, que por sua vez o
  extraiu do CME CBOT), não de uma linha própria deste dump.
- **A previsão INMET para 09/09 é previsão meteorológica, não medição de precipitação
  real** — a ausência de menção a "geada" no boletim de hoje para Passo Fundo/RS é
  tratada como sinal indicativo de moderação do frio, não como confirmação de que a
  geada efetivamente cessou; não há dado comparativo direto de geada no dump de hoje para
  contrastar com dias anteriores.
- **Prêmios de exportação (Paranaguá, farelo e óleo) seguem congelados há pelo menos 12
  dias corridos** (desde 27/08) — não dá para saber se isso reflete mercado físico export
  realmente parado ou limitação de atualização da fonte (NAG).
- **O físico brasileiro de farelo (MT/IMEA, Rondonópolis, RS) ainda não mostrou nenhuma
  reação à queda do farelo em Chicago hoje** — pode ser defasagem normal de repasse ou
  sinal de força relativa do físico doméstico; os dados não permitem decidir.
- **MPOB (palma Malásia) segue com parser quebrado** — nenhum dado de produção/estoque de
  palma malaia disponível para cruzar com a tese de substituição via Indonésia.
- **BCBA (Argentina) segue sem links de relatório detectados pelo scraper** — nenhum dado
  de safra ou exportação argentina disponível nesta janela.
- **A reversão simultânea de preço e de todos os índices estruturais em uma única sessão
  é um padrão forte, mas uma única observação** — o registro histórico desta série de
  leituras mostra que mudanças de regime "confirmadas" por múltiplas sessões (como o
  patamar 60/80 que durou cinco dias) também podem reverter em um único pregão de dado
  fresco; isso não invalida a leitura de hoje, mas pede a mesma cautela que se pediria de
  qualquer sinal baseado em um só dia de preço.
