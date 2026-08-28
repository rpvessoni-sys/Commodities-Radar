---
data: 2026-08-28
titulo: "Soja sobe pelo terceiro pregão e o óleo salta +2,2% no mesmo dia em que o farelo cede -0,63% em volume 95% menor — mas o dado mais importante de hoje é uma REVISÃO retroativa: os números de 27/08 recalculados neste briefing apagam a 'virada estrutural do crush' (ISF, ISO, oil-meal spread e oil share) que sustentou a leitura de ontem"
tags: [complexo, auto-claude, revisao-de-dado]
fontes:
  - CME CBOT (ZSX26 soja / ZMV26 farelo / ZLV26 óleo) — sessão de 2026-08-28: soja abertura 1.270,00, máxima 1.279,50, mínima 1.270,00, fechamento 1.272,00 USD cts/bushel, volume 14.756 contratos; farelo abertura 333,10, máxima 334,60, mínima 331,40, fechamento 332,30 USD/short ton, volume 3.105 contratos; óleo abertura 69,12, máxima 70,02, mínima 68,93, fechamento 69,73 USD cts/lb, volume 6.608 contratos
  - CME CBOT — sessão de 2026-08-27 (farelo fechamento 334,40 USD/sht, volume 59.717 contratos; heating oil fechamento 4,2787 USD/galão, volume 19.765 contratos) — SEM linha própria de soja/óleo nesta janela do dump (ver Honestidade); valores de soja (1.268,00) e óleo (68,23) de 27/08 reconstruídos via indicators/crush margin, não via linha direta de CBOT
  - CME NYMEX heating oil (HO=F) — 2026-08-28 fechamento 4,1600 USD/galão, -2,78% frente a 27/08 (4,2787)
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, paridade BR, ISF, ISO) — carimbos diários de 2026-08-24 a 2026-08-28, com REVISÃO retroativa dos valores de 26-27/08 frente ao que a leitura de 2026-08-27 havia citado (ver Honestidade — divergência central desta leitura)
  - BCB PTAX — série 2026-08-14 a 2026-08-27 (USD/BRL fechou em 5,1642 em 27/08, ainda sem carimbo de 28/08 nesta janela — defasagem de um dia, ver Honestidade)
  - CEPEA/ESALQ Soja Paranaguá via NAG — série 2026-08-20 a 2026-08-27, fechou em R$ 155,05/saca (27/08, var. +0,31%)
  - CEPEA/ESALQ Soja Paraná interior via NAG — série 2026-08-24 a 2026-08-27, fechou em R$ 149,21/saca (27/08, var. +0,82%)
  - NAG Físico BR — carimbos 2026-08-24 a 2026-08-27, sem variação frente à leitura anterior: farelo MT/IMEA R$ 1.726,20/ton (estável), Rondonópolis/MT R$ 1.870,00/ton (estável desde 26/08), RS média R$ 1.860,00/ton (estável); prêmios export PGUA farelo +0,12 USD/short ton e óleo +0,10 cts/lb, "mês Agosto/26", carimbo 27/08
  - CFTC COT Managed Money, Swap Dealers e Producer/Merchant — corte de 2026-08-18, sem corte novo nesta janela (mesma limitação de timing já descrita na leitura anterior, ainda sem captar o rali)
  - USDA Crop Progress — sem corte novo nesta janela; dado mais recente segue sendo 2026-08-23 (12% excelente / 48% boa / 9% ruim), já tratado na leitura de 27/08
  - USDA WASDE — segue ausente da janela deste briefing
  - NOPA — fila `release-nopa-2026-08-28`, `monthly_status` continua em 0,0 bool (paywall, sem mudança)
  - ABIOVE projeções mensais — balanços set-dez/2026, mesmos valores da leitura anterior, sem atualização de mês-base
  - NOAA CPC ENSO — carimbo 2026-08-28 (El Niño Advisory, inalterado)
  - MPOB — carimbo 2026-08-28 (3.456 caracteres, parser sem números extraídos, mesma barreira)
  - INMET — calor extremo no Mato Grosso em 29/08 (até 41°C em Sinop/MT, 40°C em Cuiabá/MT, Lucas do Rio Verde/MT e Sorriso/MT), chuva isolada em Passo Fundo/RS (mín. 15°C) e pancadas de chuva com trovoadas em Cascavel/PR em 28/08
  - Notícias Agrícolas/Canal Rural RSS — carimbo 2026-08-28 registra "1 mantido (soja/farelo/oleo)" mas sem headline impresso nesta janela do dump (ver Honestidade); manchetes anteriores (27/08 e 26/08) já tratadas na leitura de ontem
  - Forecasts estatísticos internos (bandas 7d/30d, MA20+volatilidade+slope) — geração nova de 2026-08-28, alvos 04/09 (7d) e 27/09 (30d), viés "altista" em soja e farelo nos dois horizontes, óleo "lateral" no 7d e "altista" no 30d
  - system/tributario_watch.toml (lido como referência, não editado) — sem novo carimbo visível neste dump, ver Lente fiscal
  - Fila de julgamento — 2026-08-28, 7 itens: `alerta-quebra_resistencia-soja_cbot-2026-08-28`, `alerta-quebra_suporte-oleo_cbot-2026-08-28`, `alerta-quebra_resistencia-farelo_cbot-2026-08-28`, `alerta-quebra_suporte-complexo_soja-2026-08-28`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, `trib-DANANTARA-INDONESIA-2026-09-01`, `release-nopa-2026-08-28`
  - Cruza com [[2026-08-27_leitura-complexo]] (leitura anterior, cujos números de 27/08 para ISF/ISO/oil-meal spread/oil share este briefing revisa) e com a tese original [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (checkpoint D+90 em 09/09, agora a 12 dias)
status: ativa
vies: [bull-soja, bull-farelo, bear-oleo_soja]
---

## Visão geral

O complexo soja é, mecanicamente, uma fábrica com uma única matéria-prima (a
soja em grão) e dois produtos de saída em proporção fixa por bushel esmagado:
o **farelo** (a fração proteica, usada em ração animal) e o **óleo degomado**
(a fração de gordura, usada em óleo de cozinha e biodiesel). Quem decide o
ritmo de esmagamento é a esmagadora, olhando dois números calculados em
dólares na CBOT (Chicago Board of Trade, a bolsa de referência mundial para
os três contratos): a **crush margin** (farelo + óleo, por bushel, menos o
custo daquele bushel de soja — a "conta" que sobra pra fábrica) e o **oil
share** (a fatia dessa margem capturada pelo óleo, historicamente a perna que
"manda" no valor do crush). O **ratio Far/Soj** (preço do farelo dividido
pelo preço da soja, normalizado pela conversão de 1 bushel em 33,33 short
tons equivalentes de farelo) mede a mesma dinâmica por outro ângulo: abaixo
de 80% o farelo está "abundante" — zona baixista de farelo —, acima de 87%
está "apertado" — zona altista. Hoje o ratio está em **78,37%** (indicators,
28/08) — dentro da zona abundante desde pelo menos 20/08, sem nunca cruzar de
volta para os 80%.

**A notícia mais importante desta leitura não é sobre nenhuma das três
pernas: é uma revisão retroativa dos próprios indicadores do sistema, que
muda a interpretação do que aconteceu em 27/08.** A leitura de ontem
descreveu um "primeiro sinal de virada estrutural" no crush — o Índice de
Sobra de Farelo (ISF) caindo de 80 para 60, o Índice de Suporte do Óleo (ISO)
caindo de 100 para 80, o oil-meal spread virando negativo pela primeira vez
(-0,0638 USD/bu) e o oil share cruzando abaixo de 50% (49,78%), todos no
carimbo de 27/08. **O dump de hoje recalcula esse mesmo dia (27/08) com
valores diferentes: ISF 80,0, ISO 100,0, oil-meal spread +0,1485 USD/bu
(positivo) e oil share 50,5% (acima de 50%)** — nenhum dos quatro sinais de
"virada" sobrevive à revisão. Nesta leitura, o farelo NÃO tomou o comando da
margem de crush em nenhum momento da janela conhecida; o óleo seguiu
dominando o valor do crush o tempo todo. Isso não significa que a leitura
anterior estava "errada" com o dado que tinha disponível — significa que o
pipeline revisou o carimbo depois de publicado, um comportamento que passa a
exigir mais cautela ao tratar qualquer leitura de "primeira vez na série"
como definitiva antes de um segundo carimbo confirmar (ver Honestidade,
ponto 1, para o detalhe completo).

Sobre o preço em si, hoje foi um dia de divergência dentro do complexo: soja
subiu terceiro pregão seguido (1.268,00 → 1.272,00, **+0,32%**, CBOT 28/08),
o óleo saltou **+2,20%** (68,23 → 69,73) — o maior movimento percentual do
dia entre as três pernas — e o farelo recuou **-0,63%** (334,40 → 332,30),
o único dos três a fechar em queda, e o fez com o volume mais baixo desde que
o pipeline voltou a atualizar: apenas **3.105 contratos**, contra 59.717 no
pregão anterior (-94,8%). Isso confirma três alertas técnicos que já estavam
ativos (soja acima de 1.180,00, farelo acima de 325,00, óleo abaixo de
72,00) e mantém o quarto (crush margin abaixo de 2,50 USD/bu, hoje em 2,2609,
ainda **-9,6%** abaixo do gatilho, mas em recuperação de dois pregões
seguidos desde o piso local de 26/08). **Leitura de uma linha:** o pivô do
complexo hoje não é o movimento de preço (modesto e misto), mas a
constatação de que a "virada tática" anunciada ontem não é sustentada pelos
mesmos indicadores recalculados hoje — o óleo segue estruturalmente mais
fraco em preço absoluto (abaixo do suporte técnico) mas domina a margem de
crush como sempre dominou, e o farelo segue tecnicamente rompido para cima
mas perdendo força a cada pregão (volume caindo, ratio recuando, ISF
mostrando 80/100 sem qualquer sinal de folga). Confiança alta no preço de
fechamento de hoje (dado real, três linhas completas de CBOT); confiança
baixa na narrativa de "regime mudando no crush", porque a única evidência
dela (o carimbo de 27/08 da leitura anterior) não resiste à revisão do
próprio dump de hoje.

---

## Soja

**Viés: bull, terceiro fechamento em alta desde a reabertura do pipeline,
sustentado por rompimento técnico ainda com folga ampla e por convergência de
tendência entre preço físico BR, curva futura e viés dos forecasts
internos.** Trata `alerta-quebra_resistencia-soja_cbot-2026-08-28` (fato:
1.272,00 vs. nível 1.180,00, 2026-08-28). Último fechamento: 1.272,00 cts/bushel
(CBOT, ticker ZSX26.CBT, contrato nov/26, 2026-08-28).

### O que sustenta a tese

**O fechamento de hoje está 7,80% acima da resistência técnica de 1.180,00 —
folga maior do que a de ontem (6,8%) — e representa o terceiro avanço
consecutivo desde a reabertura do pipeline em 27/08 (1.268,00 → 1.272,00,
+0,32% no dia).** Candle de hoje: abertura 1.270,00, máxima 1.279,50, mínima
1.270,00, fechamento 1.272,00 — abriu na mínima do dia e fechou perto da
metade do range (23% acima da abertura, mas 79% abaixo da máxima), sugerindo
que o mercado testou um pico intradiário (1.279,50) e recuou parte do
caminho antes do fechamento. Volume de 14.756 contratos (28/08) — sem
comparação direta com 27/08 nesta janela (linha de soja ausente no dump de
ontem, ver Honestidade), mas em linha com o volume observado no dia da
reabertura (15.045 contratos, 27/08, citado na leitura anterior).

**A curva futura segue em contango regular, o mesmo padrão observado em
27/08, sem sinal de aperto de oferta prompt.** U26 (set/26) 1.260,75, X26
(nov/26) 1.272,00, F27 (jan/27) 1.287,00, H27 (mar/27) 1.292,50, K27 (mai/27)
1.296,50 — cada vencimento mais distante vale mais que o anterior, e a
inclinação da curva ficou ligeiramente mais acentuada frente a ontem (a
diferença X26→K27 subiu de 24,50 para 24,50 pontos, estável em termos
absolutos, mas sobre uma base de preço mais alta). **Mecanismo e leitura:**
contango persistente mesmo após dois pregões adicionais de alta reforça a
leitura de que o mercado não está precificando escassez física imediata — o
movimento segue parecendo mais uma reprecificação de risco distribuída ao
longo da curva (clima americano, ver abaixo) do que um aperto pontual de
disponibilidade de curtíssimo prazo.

**Não há corte novo de USDA Crop Progress nesta janela — o dado mais recente
segue sendo o corte de 23/08 (12% excelente, 48% boa, 9% ruim), já tratado na
leitura anterior como piora consistente em relação ao corte de 02/08
(11%/52%/7%).** Sem atualização, a leitura de hoje não pode confirmar se a
tendência de deterioração de lavoura continuou ou estabilizou — o próximo
corte (nominalmente referente a 30/08) segue sendo o dado a monitorar. A
INMET, por outro lado, trouxe um dado novo relevante: previsão de calor
extremo no Mato Grosso para 29/08 — **41°C em Sinop/MT, 40°C em Cuiabá/MT,
Lucas do Rio Verde/MT e Sorriso/MT** — enquanto Cascavel/PR registrou
pancadas de chuva com trovoadas em 28/08 e Passo Fundo/RS mantém previsão de
chuva isolada com mínima de 15°C para 29/08. **Mecanismo:** o Mato Grosso já
colheu sua safra de verão nesta época do calendário agrícola brasileiro
(a soja no MT é, tipicamente, colhida entre fevereiro e maio), então o calor
extremo ali tem menor relevância direta para a safra de grãos em
desenvolvimento — o dado de clima mais relevante para preço no curto prazo
continua sendo o americano (USDA Crop Progress), que não tem atualização
nesta janela.

**O câmbio segue sem carimbo de 28/08 nesta janela do dump — o último dado
de PTAX/BCB disponível é 5,1642 (27/08), o mesmo valor usado no cálculo de
paridade de hoje.** Isso significa que a paridade teórica de hoje
(indicators, **R$ 144,82/saca**, CBOT 1.272,00 × USD/BRL 5,1642, 28/08) usa
câmbio de um dia atrás — uma limitação estrutural do dado (PTAX publica com
defasagem), não um problema desta leitura específica. Ainda assim, a
paridade subiu **+0,32%** frente a 27/08 (R$ 144,36/saca), acompanhando
exatamente a variação do CBOT em dólar, já que o câmbio usado nos dois
cálculos é o mesmo. O preço físico em Paranaguá (CEPEA/ESALQ via NAG) fechou
em **R$ 155,05/saca (27/08, var. +0,31%)** — um prêmio de **+7,40%** sobre a
paridade teórica do mesmo dia (R$ 144,36/saca) — prêmio de porto saudável,
em linha com o padrão observado na leitura anterior (+7,79%) e ligeiramente
menor. O preço físico no interior do Paraná (CEPEA/ESALQ Paraná interior via
NAG) também subiu, fechando em **R$ 149,21/saca (27/08, +0,82%)** — quarta
alta seguida na série conhecida (146,31 em 24/08 → 146,08 em 25/08, uma
queda pontual → 148,00 em 26/08 → 149,21 em 27/08), consolidando uma
tendência de alta consistente no físico do interior que acompanha o
movimento do CBOT.

**O posicionamento do COT segue sem corte novo — o dado mais recente
continua sendo 18/08, já analisado em profundidade na leitura anterior
(managed money net long em soja: 151.782 contratos, 15,34% do open interest,
uma fotografia anterior ao grosso do rali).** Sem corte novo, não há como
esta leitura avançar a pergunta em aberto de ontem — se o rali começou
depois de 18/08 (mercado "leve" de posicionamento) ou se parte dele já
ocorria antes (managed money realizando lucro). O corte de 25/08 permanece
pendente.

**Os forecasts estatísticos internos, gerados hoje com base MA20 +
volatilidade + slope de curto prazo, mantêm viés "altista" nos dois
horizontes para soja.** Banda 7d (alvo 04/09): piso 1.242,61, central
1.304,50, teto 1.366,39 — o piso da banda já está abaixo do fechamento de
hoje (1.272,00), e o centro da banda (1.304,50) implica alta adicional de
+2,56% sobre o fechamento atual. Banda 30d (alvo 27/09): piso 1.299,59,
central 1.427,72, teto 1.555,85 — note que o PISO da banda de 30 dias
(1.299,59) já está acima do fechamento de hoje, o que é matematicamente
consistente com um modelo que projeta continuação de tendência (slope
positivo) mas que carrega o viés estrutural de qualquer banda estatística
baseada em momentum recente: ela tende a extrapolar a força observada, não a
antecipar reversões. **Mecanismo e leitura:** o forecast deve ser lido como
"o que a tendência recente sugere se persistir", não como previsão
independente — é um insumo consistente com o viés técnico bull desta leitura,
mas que carrega o mesmo risco de qualquer extrapolação de momentum.

### O que invalida / risco para a soja

- **O corte de COT de 25/08 (ainda ausente) mostrar redução agressiva de
  posição comprada especulativa** durante o rali — sinalizaria realização de
  lucro em vez de entrada de dinheiro novo.
- **O próximo corte de USDA Crop Progress (nominalmente 30/08) reverter a
  tendência de piora** dos dois cortes anteriores — enfraqueceria o
  argumento de prêmio de risco climático.
- **Um fechamento de volta abaixo de 1.180,00** — reverteria formalmente o
  rompimento técnico.
- **O WASDE finalmente ser publicado** (ausente há mais de 47 dias) e
  mostrar balanço de oferta/demanda que contradiga a leitura de aperto de
  oferta americana.
- **O corpo completo da manchete "cenário confortável para soja" (27/08,
  ainda sem texto nesta janela)** trazer números de estoque que
  contradigam a leitura de aperto sugerida pela piora recente de lavoura.

### Leitura operacional — soja

Para quem opera comprado, o terceiro fechamento em alta seguido, com folga
crescente sobre a resistência rompida (7,80% hoje vs. 6,8% ontem) e curva em
contango normal (sem sinal de exaustão de oferta prompt que costuma preceder
reversões abruptas), sustenta manter a posição com stop lógico abaixo da
mínima de hoje (1.270,00) para quem quer proteção apertada, ou abaixo de
1.180,00 (nível rompido) para quem prefere dar mais espaço. Para quem avalia
o lado vendido, a ausência de corte novo de Crop Progress e de COT deixa a
tese sem munição fresca para contestar a tendência — vender contra um
rompimento que já acumula três pregões de confirmação, sem gatilho de
reversão concreto, segue sendo o lado mais caro do trade. Para quem opera o
físico brasileiro, o prêmio de porto em Paranaguá (+7,40% sobre a paridade)
segue saudável e a série do interior do Paraná mostra quarta alta seguida —
ambiente favorável para originação represada, com o câmbio (ainda que
defasado um dia no dado) mostrando real relativamente estável desde a
recuperação de 26/08.

---

## Farelo

**Viés: bull tático ainda vigente, mas visivelmente perdendo força — preço
caiu -0,63% hoje em volume 94,8% menor que o pregão anterior, o ratio
Far/Soj recuou de volta para o menor nível da janela recente, e a revisão
dos indicadores de 27/08 (ver Visão geral) remove o único sinal que sugeria
o farelo ganhando espaço estrutural dentro do crush.** Trata
`alerta-quebra_resistencia-farelo_cbot-2026-08-28` (fato: 332,30 vs. nível
325,00, 2026-08-28) e retoma `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
(ver seção dedicada abaixo). Último fechamento: 332,30 USD/short ton (CBOT,
ticker ZMV26.CBT, contrato out/26, 2026-08-28).

### D+7 já respondido, D+90 a 12 dias — atualização rápida com o dado de hoje

A tese original ([[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]])
já teve seu checkpoint D+7 tratado em profundidade na leitura de 27/08: o
ratio confirmou a compressão prevista (abaixo de 80% em toda a janela
conhecida desde 20/08), mas o preço absoluto do farelo subiu, não caiu,
invalidando parcialmente o segundo pilar da tese original. O item de fila
`revisao-...-D+7` reaparece hoje simplesmente porque continua tecnicamente
vencido (venceu em 18/06, sem campo de status para "já tratado" nesta fila) —
não há fato novo que mude a leitura de ontem sobre o D+7 especificamente.
**O dado de hoje é relevante para o próximo checkpoint, o D+90 (2026-09-09,
agora a 12 dias):** o ratio fechou em **78,37%** hoje, o menor valor da
janela de cinco pregões com dado (79,20% em 24/08 → 78,46% em 25/08 →
78,93% em 26/08 → 79,12% em 27/08 → **78,37% em 28/08**) — depois de três
pregões consecutivos de recuperação gradual (24→27/08), o ratio caiu de
volta hoje, encerrando qualquer leitura de "trajetória linear rumo a 80%".
**Mecanismo:** o ratio caiu porque farelo (-0,63%) recuou mais do que soja
subiu proporcionalmente pouco (+0,32%) — o denominador (soja) cresceu mais
devagar que o numerador caiu, mas em direções que empurram o ratio pra
baixo de qualquer forma (farelo mais barato relativo à soja). Para o D+90,
isso mantém o pilar (1) da tese original (ratio comprimido) tecnicamente
intacto, sem sinal de reversão para a zona neutra a 12 dias do prazo.

### O que sustenta a leitura de hoje

**O farelo é a única das três pernas do complexo que fechou em queda hoje —
-0,63% (334,40 → 332,30) — e fez isso no menor volume desde a reabertura do
pipeline: 3.105 contratos, contra 59.717 no pregão anterior, uma queda de
-94,8%.** Candle de hoje: abertura 333,10, máxima 334,60, mínima 331,40,
fechamento 332,30 — abriu praticamente na máxima do dia e fechou perto da
mínima (28% do range acima da mínima), um candle de fechamento fraco, ao
contrário do padrão de fechamento forte observado em 27/08 (86% do range).
**Mecanismo e leitura:** volume 95% menor combinado com um candle que cede
ao longo do pregão é o tipo de combinação que sugere falta de convicção
nova — o mercado não está ativamente vendendo farelo com volume, está
simplesmente sem comprador agressivo o suficiente para sustentar o nível de
ontem. Isso não invalida o rompimento técnico (332,30 ainda está 2,25% acima
da resistência de 325,00), mas reduz a confiança de que o movimento tem
força para continuar sem um novo catalisador.

**A curva futura segue em contango: U26 (set/26) 328,40, V26 (out/26)
332,30, Z26 (dez/26) 339,20, F27 (jan/27) 341,30, H27 (mar/27) 343,00** — sem
sinal de aperto de disponibilidade prompt, mesmo padrão de ontem.

**A crush margin recuperou-se pelo segundo pregão seguido, saindo do piso da
janela (2,0855 USD/bu, 26/08) para 2,2609 USD/bu hoje — uma alta de +8,4% em
dois pregões — mas segue -9,6% abaixo do nível de alerta de 2,50.** Série
completa da janela: 2,2999 (21/08) → 2,2665 (24/08) → 2,1909 (25/08) →
**2,0855 (26/08, piso)** → 2,1821 (27/08) → **2,2609 (28/08)**.
**Mecanismo:** a recuperação dos últimos dois pregões foi puxada
principalmente pelo lado do óleo (que subiu +2,20% hoje, ver seção Óleo),
não pelo farelo (que caiu -0,63%) — ou seja, a margem está melhorando apesar
do farelo, não por causa dele. Isso é coerente com o quadro revisado de
domínio do óleo sobre o crush (ver abaixo): quando o óleo sobe, a margem
melhora mais do que quando o farelo sobe, porque o óleo captura fatia maior
do valor total.

**O Índice de Sobra de Farelo (ISF), recalculado neste dump para 27/08 e
28/08, mostra 80,0/100 nos dois carimbos — sem qualquer sinal de folga
estrutural, ao contrário do que a leitura anterior havia registrado para
27/08 (60,0/100).** **Mecanismo e leitura:** com o ISF de volta a 80/100
(4 das 5 condições de "sobra" atendidas), a leitura estrutural de longo
prazo — farelo abundante, pressão baixista persistente — segue integralmente
válida, sem o alívio que a leitura de ontem havia identificado. Isso reforça
a tese estrutural bear-farelo de médio prazo (ABIOVE, exportação em queda,
ver abaixo) e contrasta com o viés tático bull desta leitura (preço ainda
acima da resistência rompida) — a mesma tensão "tático vs. estrutural" que
já vinha sendo descrita nas leituras anteriores, agora sem o contraponto que
o ISF de 60 havia sugerido por um dia.

**O oil-meal spread, também recalculado, fechou hoje em +0,3597 USD/bu — o
MAIOR valor positivo de toda a janela de cinco pregões com dado (0,2882 em
24/08 → 0,3256 em 25/08 → 0,0891 em 26/08 → 0,1485 em 27/08 revisado →
0,3597 em 28/08), não o valor negativo que a leitura anterior havia
registrado para 27/08.** **Mecanismo:** o spread mede quanto o óleo vale a
mais que o farelo dentro da margem de crush — o valor de hoje (o mais alto
da série) mostra o óleo ampliando, não reduzindo, sua vantagem relativa
sobre o farelo, na direção oposta ao que a leitura de ontem havia
interpretado como "farelo ganhando terreno".

**O posicionamento do COT segue sem corte novo (18/08), mesma limitação já
descrita — sem dado fresco para avançar a leitura de posicionamento
especulativo em farelo.**

**As projeções ABIOVE seguem inalteradas, confirmando exportação de farelo
brasileiro caindo de 1.100 mil toneladas em setembro/2026 para 850 mil em
outubro, 800 mil em novembro e 700 mil toneladas em dezembro/2026 (-36% em
três meses) — driver estrutural que independe do movimento técnico de curto
prazo.** Prêmio de exportação em Paranaguá segue perto de zero: +0,12
USD/short ton (NAG, carimbo 27/08, "mês Agosto/26") — mercado externo ainda
não paga prêmio suficiente para puxar farelo brasileiro para o porto.

**As praças físicas de farelo no Brasil (NAG, carimbo 27/08) seguem estáveis
nos três pontos monitorados: MT/IMEA R$ 1.726,20/ton, Rondonópolis/MT R$
1.870,00/ton, RS R$ 1.860,00/ton — sem novo movimento desde 26/08.** Ausência
de movimento no físico é coerente com a leitura de queda em volume baixo no
CBOT hoje: nenhum dos dois mercados (físico BR, futuro CBOT) mostra
convicção nova nesta sessão.

### O que invalida / risco para o farelo

- **O ISF cair novamente abaixo de 80/100 num próximo carimbo confirmado
  (não revisado depois)** — voltaria a sustentar a leitura de alívio
  estrutural, desta vez com mais confiança por não depender de um único
  carimbo isolado.
- **O volume de farelo continuar em níveis baixos (abaixo de 5.000
  contratos) nos próximos pregões** — reforçaria a leitura de falta de
  convicção por trás do nível técnico ainda rompido.
- **A crush margin continuar recuperando e romper de volta acima de 2,50**
  — aliviaria o incentivo da esmagadora para reduzir ritmo, reforçando a
  oferta de farelo (vetor baixista adicional).
- **O ratio Far/Soj continuar caindo abaixo de 78%** — aprofundaria a leitura
  de farelo abundante frente à soja.
- **Um fechamento de volta abaixo de 325,00** — reverteria o rompimento
  técnico ainda vigente.

### Leitura operacional — farelo

Para quem está comprado no rompimento técnico, o nível de preço (332,30,
ainda 2,25% acima de 325,00) segue tecnicamente válido, mas o volume de hoje
(o mais baixo desde a reabertura do pipeline) é motivo para reduzir o
tamanho da posição ou apertar o stop — um rompimento sustentado por pouco
volume é mais vulnerável a reversões rápidas do que um sustentado por fluxo
forte. Stop lógico segue em 325,00 (nível rompido). Para quem pensa no lado
estruturalmente vendido, o dado de hoje é o mais favorável de toda a janela
recente: o ISF voltou a 80/100 (sem folga), o oil-meal spread está no maior
valor positivo da série (óleo dominando, não o farelo), e a ABIOVE segue
mostrando exportação em queda continuada — a tese estrutural bear-farelo de
médio prazo ganhou de volta, hoje, o suporte de indicador que havia perdido
por um dia na leitura anterior. Para quem opera o spread far÷soj, a leitura
de hoje pede cautela: a "janela de convergência" identificada ontem (farelo
ganhando espaço) não é confirmada pelos dados recalculados — o spread mais
seguro continua sendo o original da tese de 11/06 (farelo relativamente mais
fraco que a soja), não o inverso.

---

## Óleo

**Viés: bear estrutural mantido — preço segue abaixo do suporte técnico —
mas com um bounce tático de +2,20% hoje, o maior movimento percentual do dia
entre as três pernas, e com o quadro revisado do crush (ISF, ISO, oil share,
oil-meal spread) confirmando que o óleo nunca deixou de dominar o valor da
margem.** Trata `alerta-quebra_suporte-oleo_cbot-2026-08-28` (fato: 69,73 vs.
nível 72,00, 2026-08-28). Último fechamento: 69,73 cts/lb (CBOT, ticker
ZLV26.CBT, contrato out/26, 2026-08-28).

### O que sustenta a tese

**O óleo subiu +2,20% hoje (68,23 → 69,73), reduzindo a distância abaixo do
suporte técnico de 72,00 de -5,25% (implícito no fechamento de 27/08) para
-3,15% hoje — uma recuperação parcial, mas ainda dentro da zona de ruptura
técnica.** Candle de hoje: abertura 69,12, máxima 70,02, mínima 68,93,
fechamento 69,73 — candle de corpo cheio fechando perto da máxima (89% do
range), o candle mais forte das três pernas hoje, ao contrário do padrão
observado na leitura anterior (quando o óleo tinha o candle mais fraco do
dia). **Mecanismo e leitura:** essa é uma inversão notável frente ao padrão
de divergência que caracterizou a reabertura do pipeline (soja e farelo
subindo, óleo caindo) — hoje é o óleo que lidera em termos percentuais,
ainda que a partir de um nível de preço tecnicamente rompido.

**A curva futura segue em contango moderado, com uma mudança de formato
sutil frente a ontem: hoje F27 (69,94) e H27 (69,91) estão ligeiramente
ABAIXO de Z26 (70,00), uma leve inflexão no meio da curva que não estava
presente no formato estritamente crescente de 27/08.** U26 (set/26) 69,41,
V26 (out/26) 69,73, Z26 (dez/26) 70,00, F27 (jan/27) 69,94, H27 (mar/27)
69,91. **Mecanismo:** a curva ainda não está em backwardation (os vencimentos
distantes seguem acima do prompt), mas o achatamento entre dez/26 e mar/27
é consistente com um mercado que já não está precificando alta contínua e
acelerada além do curto prazo — uma leitura neutra a levemente cautelosa
sobre o próprio bounce de hoje.

**O Índice de Suporte do Óleo (ISO), recalculado neste dump para 27/08 e
28/08, mostra 100,0/100 nos dois carimbos — domínio total do óleo sobre o
crush em todas as 5 condições monitoradas, sem a queda para 80/100 que a
leitura anterior havia identificado para 27/08.** O oil share, também
revisado, ficou em 50,5% (27/08) e subiu para **51,2% hoje (28/08)** — o
óleo captura maioria do valor do crush nos dois carimbos, sem o cruzamento
abaixo de 50% que a leitura anterior havia descrito. **Mecanismo e leitura:**
o quadro revisado é mais consistente com o comportamento histórico
observado em toda a série de leituras deste sistema (o óleo dominando o
crush de forma praticamente constante) do que com a "primeira mudança de
regime" que a leitura de ontem via — o bounce de preço de hoje (+2,20%) é
coerente com esse domínio estrutural reafirmado, não surpreendente à luz
dele.

**A margem de biodiesel americana caiu de forma acentuada hoje: 1,2952
USD/galão (28/08), -15,15% frente a 27/08 (1,5264) — a maior queda de um
único dia em toda a janela conhecida.** **Mecanismo:** a margem usa a
receita de heating oil (HO) + 1,5x RIN D4 menos o custo do óleo de soja; hoje
os dois lados da equação se moveram contra o biodiesel simultaneamente — o
heating oil caiu -2,78% (4,2787 → 4,1600 USD/galão, NYMEX) reduzindo a
receita, enquanto o próprio óleo de soja subiu +2,20%, encarecendo o
insumo. Esse é o vetor mais claramente bearish para o óleo desta leitura: o
canal de demanda via biodiesel americano ficou -15,15% menos rentável em um
único pregão, mesmo com o preço do óleo subindo — o bounce de preço de hoje
não veio acompanhado de suporte de demanda pelo lado energético, veio
apesar dele.

**As projeções ABIOVE de exportação de óleo brasileiro seguem inalteradas:
110 mil toneladas em setembro/2026 caindo para 45 mil em outubro e 21 mil em
novembro/2026 (-81% em dois meses) — driver estrutural que reforça a leitura
de oferta represada no mercado interno, independente do movimento técnico
de curto prazo.**

**O posicionamento do COT segue sem corte novo (18/08), mesma limitação já
descrita na leitura anterior — o corte mais recente já mostrava a redução
mais acentuada das três pernas (managed money net long -15,5% frente ao
corte anterior), mas antecede o movimento de preço desta semana.**

### O que invalida / risco para o óleo

- **O ISO cair de volta abaixo de 100/100 num próximo carimbo confirmado
  (não revisado depois)** — voltaria a sugerir perda de domínio estrutural,
  desta vez com mais confiança.
- **Um fechamento consistente de volta acima de 72,00** — romperia a
  sequência de fraqueza técnica, especialmente relevante depois do bounce de
  hoje.
- **A margem de biodiesel continuar caindo** — aprofundaria a pressão sobre
  a demanda doméstica americana, vetor bearish adicional.
- **O corte de COT de 25/08 mostrar managed money voltando a comprar** —
  mudaria a leitura de "posição saindo" para "fundo técnico local",
  reforçando o bounce de hoje.
- **A isenção PIS/Cofins do biodiesel ser confirmada como renovada** — ver
  Lente fiscal, reduziria o vetor bearish de custo doméstico.
- **A assunção plena da centralização de exportação de palma pela Danantara
  (Indonésia, 01/09/2026, agora a 4 dias) reduzir a oferta de palma
  disponível** — suporte estrutural de substituição que ainda não aparece
  refletido no preço.

### Leitura operacional — óleo

Para quem está vendido desde a quebra do suporte de 72,00, o bounce de hoje
(+2,20%, o candle mais forte do dia entre as três pernas) é o primeiro sinal
que pede atenção redobrada, mesmo que o nível técnico continue rompido
(-3,15% abaixo do suporte). A combinação de ISO em 100/100 (domínio
estrutural do óleo sobre o crush) com uma margem de biodiesel em forte queda
(-15,15% hoje) é mista: o primeiro dado é levemente bullish tático (óleo
capturando mais valor), o segundo é bearish de demanda — não há alinhamento
claro que justifique aumentar convicção vendida hoje. Stop lógico segue
acima de 72,00 (suporte rompido, que vira resistência) ou, para quem quer um
nível mais próximo, acima da máxima de hoje (70,02). Para quem opera o
oil-meal spread, o valor de hoje (+0,3597 USD/bu, o maior da série
conhecida) é o oposto do que a leitura anterior sugeria — favorece manter
posição comprada em óleo relativo ao farelo, não o inverso, dado que o dado
recalculado mostra o óleo ampliando vantagem, não perdendo-a. Para quem
considera reversão (comprado no bounce de hoje), o argumento mais forte é
justamente essa reafirmação do domínio estrutural do óleo no crush somada à
proximidade do prazo da Danantara (4 dias) — mas o vetor de demanda via
biodiesel (margem caindo -15,15%) pesa contra, e nenhum dos dois está
confirmado em um segundo pregão ainda.

---

## Spreads e crush (leitura de complexo)

**Ratio Far/Soj: 78,37% hoje, o menor valor da janela de cinco pregões com
dado (79,20% em 24/08 → 78,46% em 25/08 → 78,93% em 26/08 → 79,12% em 27/08
→ 78,37% em 28/08), encerrando a trajetória de recuperação gradual que a
leitura anterior havia identificado (alta em 5 das 6 sessões até 27/08).**
O ratio segue dentro da zona "abundante" (<80%) desde pelo menos 20/08, sem
nunca tocar a zona neutra — o pilar (1) da tese de 11/06 permanece
tecnicamente confirmado a 12 dias do checkpoint D+90 (09/09).

**Crush margin: 2,2609 USD/bu hoje, recuperando pelo segundo pregão seguido
desde o piso da janela (2,0855, 26/08) — alta de +8,4% em dois dias — mas
ainda -9,6% abaixo do nível de alerta de 2,50.** A recuperação foi puxada
majoritariamente pelo óleo (+2,20% hoje) e não pelo farelo (-0,63%),
reforçando o quadro em que o óleo domina a composição da margem: quando ele
sobe, a margem melhora mais visivelmente do que quando o farelo sobe
sozinho.

**Oil share: 51,2% hoje, subindo de 50,5% (27/08, valor revisado) — o óleo
captura maioria do valor do crush nos dois carimbos mais recentes, sem o
cruzamento abaixo de 50% que a leitura anterior havia descrito para 27/08.**

**Oil-meal spread: +0,3597 USD/bu hoje, o maior valor positivo de toda a
janela de cinco pregões com dado — nenhuma leitura negativa aparece nos
dados recalculados desta janela.**

**ISF em 80,0/100 e ISO em 100,0/100 nos dois carimbos mais recentes
(27-28/08) — nenhuma mudança de valor nesta janela recalculada, ao contrário
da "primeira mudança da série" que a leitura anterior havia registrado.**

**O que os índices dizem juntos hoje:** depois da revisão retroativa dos
números de 27/08, o quadro do crush volta a ser o mesmo observado em quase
toda a série de leituras deste sistema desde pelo menos 31/07: o óleo domina
o valor da margem (oil share >50%, oil-meal spread positivo, ISO em 100),
enquanto o farelo permanece estruturalmente "abundante" pela métrica do
ratio (<80%) e pelo ISF (80/100, 4 de 5 condições de sobra atendidas). A
divergência tática de preço (farelo tecnicamente rompido para cima e acima
de resistência; óleo tecnicamente rompido para baixo e abaixo de suporte)
segue vigente e não é contraditada pelos índices estruturais — ela
simplesmente não é reforçada pela "virada" que a leitura anterior havia
identificado. Para quem opera o spread far÷soj ou o oil-meal spread, a
leitura mais defensável com o dado de hoje é a original da tese de 11/06:
farelo relativamente mais fraco que soja (ratio comprimido), óleo dominando
o crush — não a inversão tática que a leitura de ontem sugeria por um único
carimbo, hoje recalculado.

---

## Lente fiscal e regulatória BR

**Isenção PIS/Cofins do biodiesel (`PISCOFINS-BIODIESEL-ISENCAO`,
`vigencia_ate` 2026-07-31) — sem atualização de status nesta janela; o
monitor tributário (`system/tributario_watch.toml`) não traz novo carimbo.**
**Mecanismo e leitura, sem mudança de fundo:** se a isenção caducou sem
renovação, o custo de produção do biodiesel brasileiro sobe, pressionando a
demanda doméstica de óleo de soja como insumo — vetor bearish direto para o
óleo que segue sem confirmação de status, agora reforçado pela queda de
-15,15% na margem de biodiesel AMERICANA observada hoje (um mercado
diferente, mas o mesmo tipo de pressão sobre o canal de demanda via
biocombustível em geral).

**Vetor da Indonésia com prazo mais próximo do painel: a assunção plena da
centralização estatal de exportação de palma pela Danantara está marcada
para 2026-09-01, agora a apenas 4 dias.** Trata `trib-DANANTARA-INDONESIA-2026-09-01`
(fila). **Mecanismo:** se o fundo soberano indonésio efetivamente
centralizar e reduzir o fluxo de exportação de óleo de palma, o óleo de soja
ganha suporte estrutural via substituição — o bounce de +2,20% do óleo hoje
não tem, nesta janela, nenhuma evidência textual (notícia, headline) que o
vincule à Danantara, mas o prazo cada vez mais próximo (4 dias) aumenta a
probabilidade de que o evento gere alguma reação de preço verificável nas
próximas leituras, para o lado bullish do óleo.

**MP 1.363/2026 — subsídio ao diesel fóssil (R$ 1,12/L), em vigor até
31/12/2026, sem alteração nesta janela.** Bearish estrutural persistente
para o óleo via competição do biodiesel com diesel fóssil subsidiado no mix
B15.

**B16 — sem data, travado em B15, sem mudança de status nesta janela.**

**STJ REsp 2.165.276/2026 — crédito PIS/Cofins para esmagadoras sobre soja
usada em biodiesel, sem alteração nesta janela.** Bullish para soja/óleo
(alívio de custo de entrada), ainda não vinculante.

**A crush margin em recuperação (2,0855 → 2,2609 em dois pregões, ver Spreads
e crush) interage com a lente fiscal de forma ambígua: se a margem continuar
melhorando, o incentivo da esmagadora para reduzir ritmo de esmagamento
diminui — o que sustentaria oferta de farelo e óleo, mas também reduz a
urgência de qualquer resposta de oferta ao aperto fiscal doméstico sobre o
biodiesel.** A verificação mais urgente do conjunto fiscal segue sendo o
status da isenção PIS/Cofins, sem novo carimbo há múltiplas leituras
consecutivas.

---

## Riscos e eventos próximos

**A revisão retroativa dos indicadores de 27/08 (ISF, ISO, oil-meal spread,
oil share) é, em si, um risco de processo a monitorar: se o pipeline
continuar revisando carimbos já publicados, leituras futuras precisam tratar
qualquer "primeira mudança da série" com cautela até um segundo carimbo
confirmar o valor sem revisão.** Ver Honestidade para o detalhe completo da
divergência.

**O corte de COT referente a 2026-08-25 (a primeira fotografia que
capturaria o posicionamento especulativo durante o rali de soja/farelo)
segue ausente — o corte mais recente (18/08) antecede o movimento
principal.**

**O próximo corte de USDA Crop Progress (nominalmente 30/08) é a primeira
chance de saber se a tendência de piora de lavoura (dois cortes consecutivos
de deterioração) continua.**

**A crush margin recuperou dois pregões seguidos (2,0855 → 2,2609) mas segue
abaixo do gatilho de 2,50 — monitorar se a recuperação continua ou se o piso
de 26/08 volta a ser testado.**

**A assunção plena da centralização de exportação de palma pela Danantara
(Indonésia) está marcada para 2026-09-01, a 4 dias** — potencial catalisador
para o óleo que ainda não aparece plenamente precificado.

**O D+90 da tese original do ratio Far/Soj vence em 2026-09-09, a 12 dias**
— checkpoint formal para reavaliar se o spread far÷soj reverteu ou seguiu
comprimindo.

**A isenção PIS/Cofins do biodiesel segue sem confirmação de status** —
segue sendo a verificação manual mais urgente do conjunto fiscal.

**A margem de biodiesel americana caiu -15,15% hoje — monitorar se a queda
continua ou se foi um evento de um único dia (heating oil recuando enquanto
óleo sobe).**

**O volume de farelo caiu -94,8% hoje frente ao pregão anterior — monitorar
se o volume normaliza ou se a falta de liquidez persiste, o que aumentaria
a fragilidade de qualquer nível técnico no contrato.**

**O WASDE segue fora da janela deste briefing** — o catalisador fundamental
mais capaz de confirmar ou contradizer a leitura de aperto de oferta
americana atribuída ao rali de soja.

**MPOB — sem números de palma extraídos, mesma barreira de longa data, agora
ainda mais relevante com o prazo da Danantara a 4 dias.**

**NOPA — fila `release-nopa-2026-08-28` sinaliza novo carimbo, mas o
`monthly_status` segue em 0,0 bool (paywall), sem alternativa de dado
primário sobre o crush americano.**

---

## Honestidade

**O que não foi possível validar nesta janela, por ordem de gravidade:**

1. **Divergência entre os indicadores de 27/08 citados na leitura anterior e
   os indicadores de 27/08 recalculados neste dump — a divergência mais
   importante desta leitura.** A leitura de 2026-08-27 registrou, para o
   carimbo de 27/08: ISF 60,0/100 (caindo de 80), ISO 80,0/100 (caindo de
   100), oil-meal spread -0,0638 USD/bu (negativo, primeira vez na série) e
   oil share 49,78% (abaixo de 50%, primeira vez na série). O dump de hoje,
   para o MESMO carimbo (27/08), traz: ISF 80,0/100, ISO 100,0/100,
   oil-meal spread +0,1485 USD/bu (positivo) e oil share 50,5% (acima de
   50%). Também há divergência nos preços absolutos de soja e óleo em
   27/08: a leitura anterior citou fechamento de soja em 1.260,75 e óleo em
   66,40 (com candle completo: abertura, máxima, mínima); o dump de hoje,
   via a fórmula da crush margin ("Board Crush: farelo 334,40 + oleo 68,23 −
   soja 1268,00"), implica soja em 1.268,00 e óleo em 68,23 para o mesmo
   dia — sem trazer uma linha própria de CBOT para soja/óleo em 27/08 que
   permita confirmar qual dos dois conjuntos de números é o correto. Esta
   leitura optou por usar os valores do PRÓPRIO dump de hoje (mais recente)
   como base para todos os cálculos e comparações, mas não tem como
   confirmar de forma independente se a revisão reflete uma correção
   legítima de um erro anterior, uma atualização de fonte, ou se é o dado de
   hoje que está desalinhado. Recomenda-se investigar a causa da divergência
   fora do escopo desta leitura (o prompt veda alterar código/indicadores).
2. **A linha de CBOT para soja e óleo em 27/08 segue ausente do dump de
   hoje** (o dump de hoje só traz farelo e heating oil para 27/08 na seção
   `cme_cbot`) — os valores de soja e óleo em 27/08 usados nesta leitura são
   reconstruídos indiretamente via a fórmula da crush margin em
   `indicators`, não observados diretamente.
3. **O PTAX/BCB de 28/08 ainda não está disponível nesta janela** — a
   paridade de hoje usa câmbio de 27/08 (5,1642), uma defasagem estrutural
   de publicação, não um erro desta leitura.
4. **O corte de COT de 25/08**, que capturaria o posicionamento especulativo
   durante o rali, segue ausente — o corte disponível (18/08) antecede o
   movimento principal.
5. **O WASDE, ausente desta janela** — segue sendo o relatório fundamental
   mais importante do calendário agrícola americano sem atualização
   verificável por este pipeline.
6. **O status da isenção PIS/Cofins do biodiesel** — sem novo carimbo do
   monitor tributário nesta janela.
7. **A notícia mantida no RSS de hoje (28/08, "1 mantido")** não trouxe
   headline visível nesta janela do dump — não foi possível avaliar seu
   conteúdo ou relevância.
8. **MPOB (palma Malásia)** — página acessível, mas sem números extraídos
   pelo parser, agora especialmente relevante com o prazo da Danantara a
   apenas 4 dias.

Nenhum número foi inventado nesta leitura: todos os valores usam
exclusivamente os carimbos presentes no briefing de 2026-08-28, com a
ressalva explícita, no ponto 1 acima, de que os valores de 27/08 usados
aqui são os do dump de HOJE (que revisa os da leitura anterior), não os
citados na leitura de 27/08. A confiança mais alta desta leitura recai sobre
os fechamentos de CBOT de hoje (soja, farelo, óleo — dado real e completo
para as três pernas) e sobre a direção dos índices de crush no carimbo de
hoje (28/08, não sujeito a nenhuma revisão observada até o momento). A
confiança mais baixa recai sobre qualquer comparação que dependa dos valores
de 27/08 para ISF/ISO/oil-meal spread/oil share/preço de soja e óleo,
justamente pela divergência identificada no ponto 1 — e sobre a atribuição
causal do bounce de +2,20% do óleo hoje, para o qual esta leitura não
encontrou nenhuma notícia ou evento textual que explique o movimento além
do próprio reposicionamento técnico e do domínio estrutural do óleo no
crush.
