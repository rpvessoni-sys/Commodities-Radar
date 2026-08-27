---
data: 2026-08-27
titulo: "O apagão de 20 dias termina: soja rompe 1.180 com força (+8,9% no gap), farelo rompe 325 (+7,7%), mas o óleo aprofunda a quebra de 72,00 até 66,40 — e a crush margin, espremida pelos dois lados, rompe o suporte de 2,50 pela primeira vez confirmada em preço real"
tags: [complexo, auto-claude, apagao-resolvido]
fontes:
  - CME CBOT (ZSX26 soja / ZMV26 farelo / ZLV26 óleo) — sessão de 2026-08-27, PRIMEIRO fechamento genuinamente novo desde 2026-08-06; abertura 1.261,00, máxima 1.264,50, mínima 1.256,00, fechamento 1.260,75 USD cts/bushel para soja; farelo abertura 333,10, máxima 336,70, mínima 333,10, fechamento 334,90 USD/short ton; óleo abertura 67,08, máxima 67,08, mínima 65,70, fechamento 66,40 USD cts/lb
  - CME CBOT — sessão de 2026-08-26 (farelo fechamento 332,00; heating oil fechamento 4,2600 USD/galão) — segunda sessão nova disponível para farelo e heating oil, mas SEM linha de soja/óleo nesse carimbo no dump (ver Honestidade)
  - CME NYMEX heating oil (HO=F) — 2026-08-27 fechamento 4,0907 USD/galão, -3,98% frente a 26/08 (4,2600)
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, paridade BR, ISF, ISO) — série diária COMPLETA e nova de 2026-08-20 a 2026-08-27, oito carimbos reais consecutivos
  - BCB PTAX — série diária nova de 2026-08-13 a 2026-08-26 (USD/BRL fechou em 5,1604 em 26/08, câmbio VALORIZANDO desde a máxima local de 5,2236 em 14/08, -1,21%)
  - CEPEA/ESALQ Soja Paranaguá via NAG — série nova 2026-08-20 a 2026-08-26, fechou em R$ 154,57/saca (26/08, var. +0,57%)
  - CEPEA/ESALQ Soja Paraná interior via NAG — série nova 2026-08-24 a 2026-08-26, fechou em R$ 148,00/saca (26/08, var. +1,31%)
  - NAG Físico BR — série nova 2026-08-24 a 2026-08-26: farelo MT/IMEA R$ 1.726,20/ton (estável nos 3 carimbos), Rondonópolis/MT R$ 1.870,00/ton (26/08, +1,08% frente aos dois dias anteriores), RS média R$ 1.860,00/ton (estável); prêmios export PGUA farelo +0,12 USD/short ton e óleo +0,10 cts/lb, ambos "mês Agosto/26", carimbo 26/08
  - CFTC COT Managed Money, Swap Dealers e Producer/Merchant — corte de 2026-08-18, PRIMEIRO corte novo desde 28/07 (21 dias de atraso recuperados de uma vez)
  - USDA Crop Progress — dois cortes novos: 2026-08-16 (12% excelente/49% boa/8% ruim) e 2026-08-23 (12% excelente/48% boa/9% ruim), ambos posteriores ao corte de 02/08 citado na leitura anterior (11%/52%/7%)
  - USDA WASDE — segue ausente da janela deste briefing
  - NOPA — fila `release-nopa-2026-08-27`, `monthly_status` continua em 0,0 bool (paywall, sem mudança)
  - ABIOVE projeções mensais — balanços set-dez/2026, mesmos valores do dump anterior, sem atualização de mês-base
  - NOAA CPC ENSO — carimbo 2026-08-27 (El Niño Advisory, inalterado)
  - MPOB — carimbo 2026-08-27 (3.456 caracteres, parser sem números extraídos, mesma barreira)
  - INMET — previsões para 2026-08-27, calor acima de 30°C em Cascavel/PR, Maringá/PR, Rio Verde/GO, Cuiabá/MT, Sinop/MT, Lucas do Rio Verde/MT e Sorriso/MT (até 40°C no Mato Grosso), chuva isolada só em Passo Fundo/RS
  - Notícias Agrícolas/Canal Rural RSS — três manchetes na janela: "USDA aponta estoques apertados para milho e cenário confortável para soja" (27/08), "Alta em Chicago impulsiona negócios e leva soja perto de R$ 160 nos portos" (26/08) e "Midwest flooding threatens corn and soybean yields" (Farm Progress, 24/08); mais "Conab divulga resultado preliminar de propostas para armazenagem de farelo de soja" (Canal Rural, 26/08)
  - Forecasts estatísticos internos (bandas 7d/30d, MA20+volatilidade+slope) — geração nova de 2026-08-27, alvos 03/09 (7d) e 26/09 (30d), viés "altista" nas três pernas
  - system/tributario_watch.toml (lido como referência, não editado) — sem novo carimbo visível neste dump, ver Lente fiscal
  - Fila de julgamento — 2026-08-27, 7 itens: `alerta-quebra_resistencia-soja_cbot-2026-08-27`, `alerta-quebra_suporte-oleo_cbot-2026-08-27`, `alerta-quebra_resistencia-farelo_cbot-2026-08-27`, `alerta-quebra_suporte-complexo_soja-2026-08-27`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, `trib-DANANTARA-INDONESIA-2026-09-01`, `release-nopa-2026-08-27`
  - Cruza com [[2026-08-25_leitura-complexo]] (última leitura antes do apagão terminar — não existe leitura de 2026-08-26 porque o dump daquele dia ainda estava represado) e com a tese original [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (checkpoint D+7, agora tratado nesta leitura)
status: ativa
vies: [bull-soja, bull-farelo, bear-oleo_soja]
---

## Visão geral

O complexo soja é, mecanicamente, uma fábrica com uma única matéria-prima (a
soja em grão) e dois produtos de saída em proporção fixa por bushel esmagado:
o **farelo** (a fração proteica, ração animal) e o **óleo degomado** (a fração
de gordura, usada em óleo de cozinha e biodiesel). A esmagadora decide o ritmo
de esmagamento olhando dois números calculados em dólares na CBOT (Chicago
Board of Trade, a bolsa de referência mundial para os três contratos): a
**crush margin** (farelo + óleo, por bushel, menos o custo daquele bushel de
soja — a "conta" que sobra pra fábrica) e o **oil share** (a fatia dessa
margem capturada pelo óleo). O **ratio Far/Soj** (preço do farelo dividido
pelo preço da soja, normalizado pela conversão 1 bushel = 33,33 short tons
equivalentes de farelo) mede a mesma dinâmica por outro ângulo: abaixo de 80%
o farelo está "abundante" — zona baixista de farelo —, acima de 87% está
"apertado" — zona altista.

**A notícia mais importante desta leitura não é sobre nenhuma das três pernas
do complexo: é que o apagão de dado que dominou dezenove leituras seguidas
(07/08 a 25/08, sempre travado no fechamento de quinta-feira 06/08) finalmente
terminou.** O briefing de hoje traz, pela primeira vez em quase três semanas,
uma sessão de CBOT genuinamente nova (2026-08-27), uma série de indicadores
completa e diária cobrindo oito pregões reais (20 a 27/08), um corte de COT
novo (18/08, recuperando 21 dias de atraso de uma vez) e dois cortes de USDA
Crop Progress que nunca tinham aparecido nas leituras anteriores (16/08 e
23/08). Isso muda o regime desta leitura: em vez de reafirmar, pela vigésima
vez, que não há dado para julgar, esta é a primeira leitura em três semanas
que pode responder à pergunta que ficou em aberto durante todo o hiato — o
que o mercado fez enquanto o pipeline estava parado.

A resposta, em uma frase: **o complexo abriu com gap de alta em soja e farelo,
mas o óleo continuou caindo — e a crush margin, espremida entre um custo de
matéria-prima subindo mais rápido do que os dois produtos de saída somados,
finalmente rompeu para baixo do nível de alerta de 2,50 USD/bushel.** Soja
fechou hoje em 1.260,75 cts/bushel, **+8,92% acima** do último fechamento
conhecido antes do apagão (1.157,50, 06/08) — um salto que confirma o alerta
da fila `alerta-quebra_resistencia-soja_cbot-2026-08-27` (fechamento 1.260,75
vs. resistência técnica de 1.180,00, rompida com folga de 6,8%). O farelo
seguiu na mesma direção, +7,68% (311,00 → 334,90), confirmando
`alerta-quebra_resistencia-farelo_cbot-2026-08-27` (vs. resistência 325,00).
O óleo, ao contrário, caiu mais um pouco: -1,78% (67,60 → 66,40),
aprofundando a quebra do suporte técnico de 72,00 já identificada nas
leituras anteriores — hoje o gatilho reaparece formalmente como
`alerta-quebra_suporte-oleo_cbot-2026-08-27`. O resultado dessa divergência
(soja subindo mais que farelo, óleo caindo) é que a crush margin — a "conta"
da esmagadora — caiu de 2,7030 USD/bu (06/08) para 2,0643 USD/bu (27/08),
**-23,6%**, rompendo pela primeira vez em preço real confirmado o nível de
alerta de 2,50, disparando `alerta-quebra_suporte-complexo_soja-2026-08-27`.
Mecanicamente: quando o preço da soja sobe mais rápido do que a soma de
farelo e óleo, cada bushel esmagado entrega menos "sobra" pra indústria —
mesmo com farelo e óleo em níveis de preço absolutos elevados, se a
matéria-prima subiu ainda mais, a margem aperta. **Leitura de uma linha:** o
pivô do complexo hoje é a reabertura do pipeline revelando um mercado que se
moveu com força durante o apagão — soja e farelo em rali de alta convicção,
óleo em fraqueza estrutural que se aprofundou, e a crush margin finalmente
confirmando, com dado real, o rompimento que só se podia especular durante as
três semanas de hiato. Confiança alta na direção dos três movimentos (dado
real, não estimado); confiança moderada sobre o timing exato de quando cada
perna se moveu dentro da janela represada, porque o dump de CBOT ainda não
trouxe a série intermediária completa (ver Honestidade).

---

## Soja

**Viés: bull confirmado por rompimento técnico com volume real, sustentado
por leitura estrutural mista (condição de lavoura piorando nos EUA + notícia
de estoque "confortável" no mesmo dia).** Trata
`alerta-quebra_resistencia-soja_cbot-2026-08-27` (fato: 1.260,75 vs. nível
1.180,00, 2026-08-27). Último fechamento: 1.260,75 cts/bushel (CBOT, ticker
ZSX26.CBT, contrato nov/26, 2026-08-27).

### O que sustenta a tese

**O rompimento da resistência de 1.180,00 vem com folga confortável (+6,8%
acima do nível) e não é um evento de um único candle isolado — é a
materialização de um gap de +8,92% acumulado desde o último preço confirmado
antes do apagão (1.157,50, 06/08).** Abertura de hoje 1.261,00, máxima
1.264,50, mínima 1.256,00, fechamento 1.260,75 — candle estreito (amplitude
de apenas 8,50 pontos) fechando praticamente na abertura, sugerindo que o
grosso do movimento de alta já havia ocorrido nas sessões anteriores
represadas, e hoje o mercado consolida em patamar elevado em vez de continuar
subindo agressivamente. **Mecanismo:** depois de treze sessões reais
represadas (identificadas nas leituras anteriores como risco de "gap
explosivo" quando o pipeline normalizasse), o mercado absorveu esse
movimento de uma vez — exatamente o cenário de risco que a leitura de
2026-08-25 descrevia como hipótese ilustrativa, mas na direção oposta à
hipótese ilustrada ali (que especulava queda, não alta). O volume de hoje
(15.045 contratos no contrato nov/26) é a primeira leitura de liquidez real
em três semanas — sem histórico comparável imediato no mesmo dump para
julgar se está acima ou abaixo da média, mas presente e substancial.

**A curva futura de hoje segue em contango regular, sem sinal de aperto de
oferta prompt — mesmo formato observado antes do apagão, agora em patamar
mais alto.** U26 (set/26) 1.247,75, X26 (nov/26) 1.260,75, F27 (jan/27)
1.275,25, H27 (mar/27) 1.280,75, K27 (mai/27) 1.285,25 — cada vencimento mais
distante vale mais que o anterior. **Mecanismo e leitura:** contango
persistente mesmo após um rali de quase 9% indica que o mercado não está
precificando escassez imediata de soja disponível — o movimento de alta
parece mais ligado a um reprecificação de risco (clima americano, ver
abaixo) distribuída ao longo da curva do que a um aperto pontual de
disponibilidade física de curtíssimo prazo.

**A condição da lavoura americana, medida pelo USDA Crop Progress, vem
piorando de forma consistente nos dois cortes novos que este briefing
finalmente trouxe.** Bom+excelente caiu de 63% (corte de referência anterior,
02/08: 11% excelente + 52% boa) para 61% (16/08: 12%+49%) e para 60%
(23/08: 12%+48%) — e a fração "ruim" subiu de 7% para 8% e depois 9% no mesmo
intervalo. **Mecanismo:** o USDA mede a condição da lavoura semanalmente
durante o ciclo de desenvolvimento; uma deterioração de 3 pontos percentuais
em bom+excelente ao longo de três semanas, mesmo que pequena em termos
absolutos, é o tipo de sinal que sustenta prêmio de risco de clima quando
combinado com notícia concreta de evento adverso — que é exatamente o que a
manchete da Farm Progress de 24/08 trouxe: **"Midwest flooding threatens
corn and soybean yields"** — enchentes no meio-oeste americano ameaçando
produtividade de milho e soja. Esta é a primeira manchete com conteúdo
climático concreto (não apenas título sem corpo, como as manchetes anteriores
sobre Mato Grosso) capturada por este pipeline em várias leituras, e ajuda a
explicar o timing do rali: um choque de oferta real durante a janela do
apagão é consistente com o tamanho do gap observado.

**Ao mesmo tempo, a manchete do próprio dia de hoje qualifica esse otimismo
de baixa oferta: "USDA aponta estoques apertados para milho e cenário
confortável para soja" (Canal Rural, 27/08/2026).** **Mecanismo e leitura —
tensão que esta análise não resolve sem o corpo da notícia (headline: None,
sem texto):** se o USDA está descrevendo estoques "confortáveis" de soja no
mesmo relatório que citaria os riscos de enchente, o rali de preço pode estar
mais ligado à correção de milho (que puxa toda a cesta de grãos por
correlação, sem fundamento de oferta próprio em soja) do que a um aperto
genuíno de balanço de soja. Essa é a principal divergência a resolver na
próxima leitura, se o corpo completo da notícia ou o WASDE (ainda ausente
desta janela) trouxerem mais detalhe.

**O câmbio moveu na direção oposta ao que normalmente reforçaria um rali de
soja em dólar: o real VALORIZOU ao longo da janela toda, de 5,2236 (14/08)
para 5,1604 (26/08, PTAX/BCB), -1,21% em 8 pregões.** **Mecanismo:** com o
CBOT subindo quase 9% e o câmbio caindo (menos dólares por real), a paridade
teórica em reais sobe menos do que subiria se o câmbio tivesse ficado parado
ou se depreciado — a valorização cambial trabalha contra parte do ganho em
dólar para quem vende soja fisicamente no Brasil. Ainda assim, a paridade
teórica (sem prêmio de basis) fechou em **R$ 143,43/saca** (indicators, CBOT
1.260,75 cts × USD/BRL 5,1604, 27/08) — bem acima da paridade da última
leitura pré-apagão (R$ 130,54/saca, 06/08), um ganho de +9,87% mesmo com o
vento contrário cambial, porque o movimento do CBOT (+8,92%) dominou. A
notícia "Alta em Chicago impulsiona negócios e leva soja perto de R$ 160 nos
portos" (Canal Rural, 26/08) é coerente com essa leitura: o preço físico em
Paranaguá (CEPEA/ESALQ via NAG) fechou em **R$ 154,57/saca (26/08)**, um
prêmio de **+7,79%** sobre a paridade teórica do mesmo dia (R$ 143,52/saca) —
prêmio de porto saudável e em linha com o padrão observado nas leituras
anteriores ao apagão.

**O posicionamento do COT chegou com o primeiro corte novo em 21 dias — data
de 2026-08-18, dez dias antes do fechamento de hoje — e mostra concentração
comprada especulativa ainda relevante, mas ligeiramente MENOR do que na
última fotografia (28/07).** Managed money net long em soja: 151.782
contratos (long 197.446, short 45.664), 15,34% do open interest de 989.729 —
ante 160.479 contratos (15,73% do OI) no corte anterior. Swap dealers: net
long 104.029 (swap long 141.218, swap short 37.189) — praticamente estável
frente aos 105.940 anteriores. Somando as duas categorias especulativas, o
net long combinado é de **~255.811 contratos**, uma redução de -4,0% frente
aos ~266.419 do corte anterior, compensado pelos produtores/comerciais
(producer long 311.979, producer short 585.645, net -273.666, vendido, hedge
de produção física). **Mecanismo e leitura:** essa é a fotografia de 18/08 —
ou seja, ainda ANTES do grosso do rali que levou o preço a 1.260,75 (o corte
mais provável para capturar o movimento completo, referente a 25/08, ainda
não está nesta janela). Uma redução modesta de posição comprada especulativa
justamente na semana anterior a um rali de quase 9% é compatível com dois
cenários: (1) o rali começou depois do corte de 18/08 e pegou o mercado
"leve" de posição especulativa, deixando mais espaço para novos compradores
entrarem; ou (2) parte do rali já ocorria antes de 18/08 e o managed money
já vinha realizando lucro parcial. Sem o corte de 25/08 (ainda pendente),
esta leitura não consegue distinguir as duas hipóteses.

### O que invalida / risco para a soja

- **O corte de COT de 25/08 (ainda ausente) mostrar redução agressiva
  (não apenas modesta) de posição comprada especulativa** durante o próprio
  rali — sinalizaria realização de lucro em vez de entrada de dinheiro novo,
  enfraquecendo a sustentação do movimento.
- **O corpo completo da manchete "cenário confortável para soja" (27/08)
  aparecer com números de estoque que contradigam o tom de aperto sugerido
  pela piora de condição de lavoura** — resolveria a tensão em favor de uma
  leitura mais bearish de fundamento, mesmo com o preço tecnicamente
  rompido para cima.
- **Um fechamento de volta abaixo de 1.180,00** — reverteria formalmente o
  rompimento de hoje.
- **O WASDE finalmente ser publicado** (ausente há mais de 46 dias na
  leitura anterior, situação não resolvida nesta janela) e mostrar balanço
  de oferta/demanda que contradiga a leitura de aperto climático.
- **A condição de lavoura (USDA Crop Progress) reverter a tendência de piora
  no próximo corte semanal** — enfraqueceria o argumento de prêmio de risco
  climático como driver do rali.

### Leitura operacional — soja

Para quem opera os dois lados, o rompimento de 1.180,00 com volume real e
amplo suporte fundamental (enchente confirmada no meio-oeste americano,
condição de lavoura em piora consistente há três cortes) é o tipo de sinal
técnico que justifica respeitar a nova tendência de alta no curto prazo, com
stop lógico abaixo da mínima de hoje (1.256,00) para quem entrar comprado no
rompimento, ou abaixo de 1.180,00 (nível rompido, que vira suporte na teoria
técnica clássica) para quem quiser dar mais espaço à posição. Para quem
avalia o lado vendido, a tensão entre a manchete de "estoque confortável" e a
piora de condição de lavoura é o ponto a resolver antes de vender contra a
tendência — vender um rompimento confirmado sem uma tese de reversão clara é
historicamente o lado mais caro do trade. Para quem opera o físico
brasileiro, a paridade em reais subiu quase 10% mesmo com a valorização
cambial recente, e o prêmio de porto em Paranaguá segue saudável (+7,79%
sobre a paridade) — ambiente favorável para quem tem originação represada
para vender, mas a valorização do real (se continuar) é um vento contrário a
monitorar para quem depende do câmbio para reforçar o ganho em dólar.

---

## Farelo

**Viés: bull tático confirmado por rompimento técnico, mas em tensão direta
com o pano de fundo estrutural (ISF ainda em 60/100, ABIOVE mostrando
exportação em queda) — o rali de preço não invalida a tese estrutural de
"farelo sobra", mas exige atualização do timing.** Trata
`alerta-quebra_resistencia-farelo_cbot-2026-08-27` (fato: 334,90 vs. nível
325,00, 2026-08-27) e `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
(ver seção dedicada abaixo). Último fechamento: 334,90 USD/short ton (CBOT,
ticker ZMV26.CBT, contrato out/26, 2026-08-27).

### D+7 finalmente respondido: o ratio ficou abaixo de 80% — mas o farelo em preço absoluto subiu, não caiu

A tese original ([[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]])
tinha dois pilares: (1) o ratio Far/Soj cairia abaixo de 80% "em 1-2 semanas"
a partir de 11/06 (compressão de 83,3%→81,4% em 4 pregões); e (2) o farelo em
preço absoluto continuaria fraco, perto da mínima de 52 semanas de então
(293 USD/sht, com o contrato jul/26 em 303,60). O checkpoint D+7 formal caiu
em 18/06/2026 e ficou **70 dias vencido** até hoje, sem que nenhuma leitura
conseguisse confirmar ou refutar o pilar (1) por falta de dado — até agora.
**Com a série de indicadores voltando a atualizar diariamente (20 a 27/08),
esta leitura pode finalmente responder: o ratio Far/Soj ficou consistentemente
ABAIXO de 80% em todos os oito carimbos reais desta janela** — 77,30%
(20/08), 77,57% (21/08), 79,20% (24/08), 78,46% (25/08), 78,95% (26/08) e
79,69% (27/08, hoje). **O pilar (1) da tese original está, portanto,
tecnicamente confirmado** — o ratio nunca subiu de volta para a zona neutra
nesta janela. Mas o pilar (2) falhou: o farelo, em preço absoluto, não ficou
perto de mínimas — **fechou hoje em 334,90 USD/sht, +10,3% acima do contrato
de referência da tese original (303,60, 11/06)** e rompendo, não testando,
resistência técnica (325,00). **Mecanismo da divergência:** um ratio baixo
(farelo "abundante" frente à soja) é compatível com farelo subindo em termos
absolutos, desde que a soja suba ainda mais rápido — que é exatamente o que
aconteceu: soja subiu +8,92% desde 06/08 contra +7,68% do farelo, uma
proporção que empurra o ratio para baixo mesmo com as duas pernas em alta
conjunta. **Leitura para o status da tese:** classificar como **parcialmente
confirmada, com o vetor de preço absoluto invertido frente à expectativa
original** — o "spread far÷soj comprimindo" se confirmou pela métrica do
ratio, mas não trouxe o farelo pra baixo em dólares por tonelada como a tese
de 11/06 esperava; quem operou a tese via posição direta vendida em farelo
(em vez de via o ratio ou o spread relativo) teria perdido dinheiro apesar do
ratio ter se comportado como previsto. Adicionalmente, um dos gatilhos que
"invalidariam" a tese original já se cumpriu: **a crush margin caiu abaixo de
2,50 USD/bushel** (ver abaixo) — o próprio texto de 11/06 alertava que isso
faria "a esmagadora tirar o pé, oferta de farelo secar", um vetor que passa a
competir com a leitura estrutural de sobra (ISF). Próximo marco formal:
D+90 em 2026-09-09, agora a **13 dias**.

### O que sustenta a leitura de hoje

**O rompimento de 325,00 vem com o mesmo padrão de gap observado na soja:
+7,68% acumulado desde o último fechamento pré-apagão (311,00, 06/08).**
Candle de hoje: abertura 333,10, máxima 336,70, mínima 333,10, fechamento
334,90 — fechamento próximo da máxima do dia (86% do range), sinal de
força compradora que persiste até o fim do pregão, não apenas um gap de
abertura que já se esgotou. A curva futura segue em contango: U26 (set/26)
330,40, V26 (out/26) 334,90, Z26 (dez/26) 341,10, F27 (jan/27) 343,60, H27
(mar/27) 346,10 — sem sinal de aperto de disponibilidade prompt, o mesmo
padrão observado na soja.

**A crush margin rompeu o nível de alerta de 2,50 USD/bushel pela primeira
vez em dado real confirmado — 2,0643 USD/bu hoje, -23,6% frente aos 2,7030
de 06/08 — e a queda foi consistente ao longo de toda a semana real
disponível, não um evento de um único dia.** Série completa: 2,4905 (20/08)
→ 2,2999 (21/08) → 2,2665 (24/08) → 2,1909 (25/08) → 2,0964 (26/08) → 2,0643
(27/08, hoje) — queda em cinco das seis sessões, -17,1% acumulado só nesta
janela conhecida. **Mecanismo:** a crush margin (farelo + óleo menos soja,
em USD/bushel) caiu apesar de farelo estar em alta absoluta porque a soja
(o custo) subiu proporcionalmente mais rápido do que a soma dos dois
produtos — o óleo, em particular, caiu enquanto a soja subia, um duplo
aperto sobre a margem. Isso confirma, com atraso mas de forma direta, um dos
gatilhos que a própria tese de 11/06 apontava como fator que reduziria oferta
de farelo (esmagadora com menos incentivo a esmagar) — uma força que, se
persistir, trabalha CONTRA a tese estrutural de "farelo sobra" ao reduzir o
volume ofertado, não a favor dela.

**O Índice de Sobra de Farelo (ISF) caiu de 80/100 (06/08 e also 26/08) para
60/100 hoje — a primeira mudança de valor deste índice estrutural em toda a
série de leituras desde pelo menos 31/07.** **Mecanismo e leitura:** o ISF
mede 5 condições estruturais de excesso de oferta de farelo; cair de 4/5
para 3/5 condições atendidas significa que pelo menos uma das condições que
sustentava "sobra relevante" deixou de se verificar no dado de hoje — mais
consistente com o farelo ganhando força relativa (coerente com o
rompimento técnico) do que com o quadro de excesso permanecendo inalterado.
Este é o primeiro movimento genuíno do ISF em toda a série de leituras
diárias — um sinal que merece monitoramento no próximo carimbo para
verificar se é ruído de um dia ou início de uma reversão de regime.

**O oil-meal spread virou negativo hoje pela primeira vez em toda a janela
disponível: -0,0638 USD/bu (27/08), depois de fechar positivo em todas as
seis sessões anteriores conhecidas — 0,8371 (20/08) → 0,5929 (21/08) → 0,2882
(24/08) → 0,3256 (25/08) → 0,1034 (26/08) → -0,0638 (27/08, hoje).**
**Mecanismo:** o oil-meal spread mede quanto o óleo vale a mais que o farelo
dentro da margem de crush; a sequência inteira mostra o farelo ganhando
terreno relativo sessão após sessão até finalmente ultrapassar o óleo hoje —
o farelo, pela primeira vez nesta série de dados, "manda" mais que o óleo
dentro do valor total do crush. É o sinal tático mais forte e mais
consistente desta leitura, com seis pontos de dado consecutivos na mesma
direção antes da inversão de sinal.

**O posicionamento do COT em farelo (corte de 18/08, mesma limitação de
timing da soja: antecede o grosso do rali) mostra concentração comprada
especulativa estável a ligeiramente maior que a fotografia anterior.**
Managed money net long: 83.315 contratos (long 129.318, short 46.003),
13,79% do open interest de 604.433 — abaixo dos 87.696 (14,11% do OI)
anteriores. Swap dealers: net long 120.803 (swap long 127.778, swap short
6.975) — ACIMA dos 112.525 anteriores. Somando as duas categorias, o net
long combinado é de **~204.118 contratos**, praticamente estável frente aos
~200.221 do corte de 28/07 (+2,0%). **Mecanismo e leitura:** ao contrário da
soja (que mostrou redução modesta), o farelo manteve — e no caso dos swap
dealers, ampliou — a posição especulativa comprada mesmo com o preço já
subindo desde 06/08. Isso é munição para o lado comprado no curto prazo (o
posicionamento não está "gordo" a ponto de sugerir exaustão iminente), mas
também é o mesmo argumento estrutural das leituras anteriores: se o
catalisador estrutural (ISF, ABIOVE) eventualmente dominar, há posição
especulativa relevante a liquidar.

**Notícia da Conab sobre armazenagem de farelo (Canal Rural, 26/08) — sem
número no corpo da manchete (headline: None) — sinaliza atenção
governamental ao tema logístico de estocagem de farelo, mas não é
quantificável nesta janela.**

**As projeções ABIOVE seguem sem alteração, mostrando exportação de farelo
brasileiro caindo de 1.100 mil toneladas em setembro/2026 para 700 mil
toneladas em dezembro/2026 (-36% em três meses) — driver estrutural de mais
longo prazo que independe do rali técnico de curto prazo.** Prêmio de
exportação em Paranaguá também segue perto de zero: +0,12 USD/short ton
(NAG, carimbo 26/08, "mês Agosto/26") — mercado externo ainda não paga
prêmio suficiente para puxar farelo brasileiro para o porto.

**As praças físicas de farelo no Brasil (NAG) mostram Rondonópolis/MT
subindo +1,08% (26/08, R$ 1.870,00/ton) enquanto MT/IMEA (R$ 1.726,20/ton) e
RS (R$ 1.860,00/ton) seguem estáveis nos três carimbos disponíveis
(24-26/08)** — leitura de físico mais firme, coerente com o rompimento
técnico do CBOT, mas ainda sem confirmação de uma tendência ampla nas
praças (apenas uma das três subiu).

### O que invalida / risco para o farelo

- **O ISF voltar a 80/100 no próximo carimbo** — indicaria que a queda para
  60/100 hoje foi ruído de um dia, não início de reversão estrutural.
- **O oil-meal spread voltar a positivo na próxima sessão** — a inversão de
  hoje teria durado apenas um dia, enfraquecendo a leitura de "farelo
  passou a mandar no crush".
- **A crush margin continuar caindo abaixo de 2,00 USD/bu** — aprofundaria o
  aperto sobre a esmagadora e poderia começar a reduzir ritmo de
  esmagamento de forma mais visível, reduzindo oferta de farelo (vetor que
  reforça o preço, mas contradiz o ISF).
- **O corte de COT de 25/08 mostrar redução agressiva de posição comprada**
  — mudaria a leitura de "posição estável" para "início de liquidação".
- **Um fechamento de volta abaixo de 325,00** — reverteria o rompimento de
  hoje.

### Leitura operacional — farelo

Para quem opera o ratio Far/Soj ou o spread far÷soj, o D+7 finalmente
respondeu de forma mista: o ratio confirmou a compressão prevista (<80% em
todos os oito carimbos), mas o preço absoluto do farelo subiu, não caiu — um
lembrete de que operar via preço absoluto vendido é uma aposta diferente de
operar via ratio ou spread relativo, mesmo quando o racional fundamental é o
mesmo. Para quem está comprado no rompimento técnico de hoje, o ISF caindo
de 80 para 60 e o oil-meal spread virando negativo pela primeira vez são
sinais táticos que sustentam a posição no curto prazo, com stop lógico
abaixo de 325,00 (nível rompido). Para quem pensa no lado estruturalmente
vendido (ISF ainda em 60/100, não zero; ABIOVE mostrando exportação em
queda continuada), a crush margin rompendo 2,50 é o dado mais importante a
monitorar nos próximos dias: se a esmagadora efetivamente reduzir ritmo em
resposta à margem apertada, a oferta de farelo cai, e isso é um vetor que
favoreceria MAIS alta, não reversão — a tese estrutural bear-farelo de
longo prazo (ABIOVE, exportação) e o sinal tático de hoje (rompimento,
oil-meal spread negativo) apontam, pela primeira vez em semanas, na MESMA
direção de curto prazo, mesmo que por motivos mecânicos diferentes.

---

## Óleo

**Viés: bear estrutural reforçado — o óleo é a única das três pernas que NÃO
participou do rali, e o dado novo (COT, ISO) mostra o mercado especulativo
reduzindo exposição comprada na mesma direção do preço.** Trata
`alerta-quebra_suporte-oleo_cbot-2026-08-27` (fato: 66,40 vs. nível 72,00,
2026-08-27). Último fechamento: 66,40 cts/lb (CBOT, ticker ZLV26.CBT,
contrato out/26, 2026-08-27).

### O que sustenta a tese

**Enquanto soja e farelo romperam resistências com gaps de alta de quase
+9% e quase +8%, o óleo caiu -1,78% na mesma janela (67,60 → 66,40) e
aprofundou a distância abaixo do suporte técnico de 72,00 — agora -7,78%
abaixo do nível, frente a -6,11% na última leitura pré-apagão.**
**Mecanismo:** essa divergência de magnitude e direção entre as três pernas
é o dado mais informativo desta leitura sobre o óleo — não é apenas "o
complexo subiu e o óleo subiu menos"; o óleo efetivamente caiu enquanto os
outros dois subiram com força, uma dissociação que aponta para um driver
específico do óleo (biodiesel, palma, regulatório) atuando na direção
oposta ao driver que moveu soja e farelo (provavelmente clima/oferta
americana).

**O candle de hoje fecha longe da máxima: abertura 67,08 (que também foi a
máxima do dia), mínima 65,70, fechamento 66,40 — um candle que abriu no
topo e cedeu ao longo do pregão, terminando a 51,7% do range, mais fraco do
que os candles de soja e farelo do mesmo dia.**

**A curva futura segue em contango moderado, ao contrário do padrão de
backwardation observado na última leitura pré-apagão (06/08).** U26 (set/26)
66,23, V26 (out/26) 66,40, Z26 (dez/26) 66,73, F27 (jan/27) 66,80, H27
(mar/27) 66,93 — formato normal, sem inversão. **Mecanismo e leitura:** a
mudança de backwardation para contango durante o apagão é, em si, um dado
relevante — sugere que a pressão de curtíssimo prazo que sustentava a
inversão da curva (identificada nas leituras anteriores como possível reflexo
de incerteza regulatória BR ou pressão de oferta de palma) diminuiu de
intensidade, mesmo com o preço em nível mais baixo. Não há dado intermediário
para saber exatamente quando essa transição ocorreu dentro da janela
represada.

**O Índice de Suporte do Óleo (ISO) caiu de 100/100 para 80/100 hoje — a
primeira mudança deste índice estrutural em toda a série de leituras, no
mesmo dia em que o ISF do farelo também mudou (80→60).** **Mecanismo:** o
ISO mede 5 condições estruturais que sustentam o óleo como o "dono" do valor
do crush; perder uma condição (5/5→4/5) no mesmo dia em que o farelo ganha
força relativa (oil-meal spread virando negativo) é consistente e reforça,
por dois ângulos independentes, a mesma leitura: o óleo está perdendo, ainda
que modestamente, participação na margem de crush.

**A margem de biodiesel americana caiu na maior parte da janela conhecida,
acompanhando a queda do heating oil mais do que a queda do próprio óleo.**
Série: 1,4955 USD/galão (20/08) → 1,6481 (21/08, pico) → 1,5882 (24/08) →
1,5313 (25/08) → 1,5745 (26/08) → 1,4757 (27/08, hoje) — queda de -6,3% na
sessão de hoje sozinha. **Mecanismo:** a margem de biodiesel usa a receita de
heating oil (HO) + RIN D4 menos o custo do óleo; o heating oil caiu -3,98%
entre 26/08 e 27/08 (4,2600 → 4,0907 USD/galão) — uma queda maior, em termos
percentuais, do que a queda do próprio óleo de soja no mesmo dia (-1,78%
frente a 06/08, mas o comparativo dia-a-dia 26→27/08 do óleo não está
disponível nesta janela porque o dump de 26/08 não trouxe linha de óleo, ver
Honestidade). Ainda assim, a direção é clara: o insumo energético (heating
oil, ligado a diesel e combustíveis fósseis) caiu mais rápido que o óleo
vegetal, comprimindo a margem do biodiesel americano e reduzindo o incentivo
de demanda desse canal para o óleo de soja — um vetor bearish adicional que
ajuda a explicar por que o óleo não acompanhou o rali de soja e farelo.

**As projeções ABIOVE de exportação de óleo brasileiro seguem sem alteração,
mostrando queda de 110 mil toneladas em setembro/2026 para 21 mil em
novembro/2026 (-81% em dois meses) — driver estrutural que independe do
movimento técnico de curto prazo e reforça a leitura de oferta represada no
mercado interno.**

**O posicionamento do COT em óleo (corte de 18/08) mostra a redução mais
acentuada das três pernas do complexo — managed money net long caiu de
107.898 contratos (16,60% do OI, corte de 28/07) para 91.233 contratos
(14,61% do OI, corte de 18/08), -15,5%.** Swap dealers também recuaram, de
forma mais modesta: net long de 84.593 contratos (swap long 96.063, swap
short 11.470), ante 88.407 anteriores, -4,3%. Somando as duas categorias, o
net long combinado caiu de ~196.305 para ~175.826 contratos, -10,4%.
**Mecanismo e leitura:** esta é a única das três pernas em que TODAS as
categorias especulativas reduziram exposição comprada no corte mais recente
disponível — managed money (mais sensível a sinal técnico) reduzindo pelo
segundo corte seguido (já vinha caindo -10,27% no corte anterior), e agora
os swap dealers (posição mais estrutural) acompanhando a mesma direção pela
primeira vez nesta série. É o quadro de posicionamento mais coerente com o
preço observado: dinheiro especulativo saindo do lado comprado enquanto o
preço cai e rompe suporte — sem a tensão "preço caindo mas posição comprada
intacta" que caracterizava leituras anteriores.

### O que invalida / risco para o óleo

- **O ISO voltar a 100/100 no próximo carimbo** — indicaria que a queda para
  80/100 hoje foi pontual.
- **A curva voltar a backwardation** — reverteria a leitura de alívio de
  pressão de curtíssimo prazo observada hoje.
- **Um fechamento consistente de volta acima de 72,00** — romperia a
  sequência de fraqueza técnica.
- **O corte de COT de 25/08 mostrar managed money voltando a comprar** —
  mudaria a leitura de "posição saindo" para "fundo técnico local".
- **A isenção PIS/Cofins do biodiesel ser confirmada como renovada** — ver
  Lente fiscal, reduziria o vetor bearish de custo doméstico.
- **A assunção plena da centralização de exportação de palma pela Danantara
  (Indonésia, 01/09/2026) reduzir a oferta de palma disponível** — suporte
  estrutural de substituição para o óleo de soja que ainda não aparece
  refletido no preço.

### Leitura operacional — óleo

Para quem está vendido desde a quebra do suporte de 72,00, o dado de hoje
reforça a posição: o óleo é a única perna do complexo que não participou do
rali, o COT mostra dinheiro especulativo saindo do lado comprado em todas as
categorias pela primeira vez, e o ISO confirma perda (ainda que pequena) de
domínio estrutural sobre o crush. Stop lógico segue acima de 72,00 (suporte
rompido, que vira resistência) ou, para quem quer um nível mais próximo,
acima da máxima de hoje (67,08). Para quem opera o oil-meal spread (comprado
em farelo contra vendido em óleo, ou vice-versa), a inversão do spread para
negativo pela primeira vez em toda a série, combinada com ISF caindo e ISO
caindo no mesmo dia, é o alinhamento mais forte já visto nesta janela entre
sinal tático e estrutural — ambos numa única direção: farelo relativamente
mais forte, óleo relativamente mais fraco. Para quem considera posição
comprada contrária (aposta em reversão), o único argumento de peso é o
retorno da curva a contango (alívio de pressão de curto prazo) e o suporte
estrutural potencial da Danantara — mas nenhum dos dois aparece ainda
confirmado em preço.

---

## Spreads e crush (leitura de complexo)

**Ratio Far/Soj: 79,69% hoje, dentro de uma faixa de 77,30%-79,69% ao longo
de toda a semana real conhecida (20-27/08), nunca tocando a zona neutra
(≥80%) — o pilar (1) da tese do D+7 confirmado, com trajetória de recuperação
gradual rumo ao limiar (subiu em 5 das 6 sessões da janela).** Se a trajetória
de alta continuar, o ratio pode cruzar de volta para a zona neutra nas
próximas sessões — o que encerraria formalmente a fase "abundante" que vigora
desde pelo menos 20/08 (e provavelmente desde bem antes, dado o apagão).

**Crush margin: 2,0643 USD/bu hoje, -23,6% frente ao último dado pré-apagão
e -17,1% só na janela de seis sessões conhecidas (20-27/08) — primeiro
rompimento confirmado do nível de alerta de 2,50 USD/bu em toda a série de
leituras.** Este é o evento estrutural mais concreto desta leitura: uma
esmagadora operando com margem de papel abaixo do gatilho histórico de
alerta tem, na prática, menos incentivo econômico para manter ritmo de
esmagamento no nível atual — o desdobramento a monitorar é se essa margem
comprimida começa a se refletir em dado de esmagamento real (ABIOVE, NOPA)
nos próximos meses.

**Oil share: 49,78% hoje, caindo de 50,35% (26/08) e cruzando abaixo de 50%
pela primeira vez na janela conhecida — o óleo deixou de capturar a maioria
do valor do crush hoje, ainda que por margem pequena (49,78% vs. 50,22% do
farelo).** Série completa: 52,02% (21/08) → 50,99% (24/08) → 51,12% (25/08)
→ 50,35% (26/08) → 49,78% (27/08) — queda consistente em todas as sessões,
o segundo indicador (depois do oil-meal spread) a confirmar a mesma direção.

**Oil-meal spread: -0,0638 USD/bu hoje, primeira leitura negativa da série,
depois de cair continuamente desde 0,8371 (20/08) — queda acumulada de
mais de 100% (de positivo para negativo) em seis sessões.**

**ISF caiu de 80/100 para 60/100 e ISO caiu de 100/100 para 80/100, ambos no
mesmo dia (27/08) — a primeira mudança de qualquer um dos dois índices
estruturais em toda a série de leituras desde pelo menos 31/07.** Os dois
movimentos apontam na mesma direção (farelo ganhando espaço relativo, óleo
perdendo) e reforçam-se mutuamente: como os dois índices são calculados a
partir de condições relacionadas (crush margin, oil share, e outras métricas
do mesmo complexo), não é surpreendente que se movam juntos, mas é a primeira
vez que o fazem nesta série de dados, o que aumenta a confiança de que é
sinal genuíno, não ruído de um indicador isolado.

**O que os índices dizem juntos hoje:** pela primeira vez em toda a série de
leituras, o sinal tático (oil-meal spread negativo, oil share <50%, ISF/ISO
se movendo juntos) e a mecânica de curto prazo (crush margin rompendo 2,50,
farelo rompendo resistência com mais força relativa que antes) apontam na
MESMA direção: o farelo está ganhando terreno dentro do crush, e o óleo está
perdendo. Isso não invalida a tese estrutural de mais longo prazo sobre a
oferta de farelo (ABIOVE ainda mostra exportação em queda), mas descreve uma
mudança de regime tático que, se persistir por mais sessões, merece
reavaliação da magnitude do viés bear-farelo estrutural de longo prazo. Para
quem opera o spread far÷soj ou o próprio oil-meal spread, hoje é o primeiro
dia, em toda esta série, em que vale a pena considerar reduzir exposição
vendida em farelo relativo ao óleo, dado o alinhamento raro entre sinal
tático e estrutural na mesma direção.

---

## Lente fiscal e regulatória BR

**Isenção PIS/Cofins do biodiesel (`PISCOFINS-BIODIESEL-ISENCAO`,
`vigencia_ate` 2026-07-31) — este dump não trouxe nenhuma atualização de
status sobre este vetor, e o monitor tributário
(`system/tributario_watch.toml`) não aparece com novo carimbo nesta janela.**
**Mecanismo e leitura, sem mudança de fundo:** se a isenção caducou sem
renovação, o custo de produção do biodiesel brasileiro sobe, pressionando a
demanda doméstica de óleo de soja como insumo — um vetor bearish direto para
o óleo que segue sem confirmação de status, agora com o apagão de dado
técnico resolvido mas o apagão fiscal ainda não.

**Vetor da Indonésia com prazo mais próximo de todo o painel: a assunção
plena da centralização estatal de exportação de palma pela Danantara está
marcada para 2026-09-01, agora a apenas 5 dias.** Trata
`trib-DANANTARA-INDONESIA-2026-09-01` (fila). **Mecanismo:** se o fundo
soberano indonésio efetivamente centralizar e reduzir o fluxo de exportação
de óleo de palma, o óleo de soja ganha suporte estrutural via substituição —
mas, como observado na seção Óleo, o mercado hoje precifica o óleo em queda
e a curva em contango normal, sem sinal de que esse suporte já esteja sendo
antecipado. Com o prazo a apenas 5 dias e o pipeline de dado finalmente
voltando a atualizar, esta é a variável fiscal com maior probabilidade de
gerar movimento de preço verificável na próxima semana de leituras.

**MP 1.363/2026 — subsídio ao diesel fóssil (R$ 1,12/L), em vigor até
31/12/2026, sem alteração nesta janela.** Bearish estrutural persistente para
o óleo via competição do biodiesel com diesel fóssil subsidiado no mix B15.

**B16 — sem data, travado em B15, sem mudança de status nesta janela.** Cada
+1pp de mistura obrigatória de biodiesel puxaria demanda adicional de óleo de
soja para o mercado interno, mas o CNPE segue sem nova convocação visível
neste dump.

**STJ REsp 2.165.276/2026 — crédito PIS/Cofins para esmagadoras sobre soja
usada em biodiesel, sem alteração nesta janela.** Bullish para soja/óleo
(alívio de custo de entrada), ainda não vinculante.

**A crush margin rompendo 2,50 USD/bu (ver seção Spreads e crush) interage
diretamente com a lente fiscal: se o subsídio ao diesel fóssil e a incerteza
sobre a isenção do biodiesel já pressionam a demanda de óleo pelo canal
doméstico, uma margem de esmagamento comprimida reduz simultaneamente o
incentivo de oferta — dois vetores bearish de demanda e neutro-a-bearish de
oferta que, juntos, aumentam o peso da pergunta em aberto sobre a isenção
PIS/Cofins como a verificação fiscal mais urgente desta janela.**

---

## Riscos e eventos próximos

**O pipeline de dado voltou a atualizar — mas a série ainda tem uma lacuna:
o dump de CBOT de 2026-08-26 trouxe fechamento apenas para farelo e heating
oil, sem linha correspondente para soja e óleo naquele mesmo carimbo.**
Monitorar se o próximo dump preenche essa lacuna ou se a janela de "últimos
14 dias" do sistema simplesmente não reteve essas duas linhas por limite de
espaço — sem impacto na leitura de hoje (que usa o fechamento de 27/08,
completo nas três pernas), mas relevante para reconstruir a trajetória exata
dentro do apagão em leituras futuras.

**O corte de COT referente a 2026-08-25 (a primeira fotografia que captura o
grosso do rali de +8,9% em soja) ainda não está disponível — o corte mais
recente (18/08) antecede o movimento principal.** Quando esse corte chegar,
o ponto mais relevante a checar é se a redução modesta de posição
especulativa em soja (-4,0%) e a estabilidade em farelo (+2,0%) e óleo
(-10,4%) observadas no corte de 18/08 se acentuaram, revertem, ou se dinheiro
novo entrou durante o próprio rali.

**O ISF e o ISO mudaram de valor pela primeira vez em toda a série de
leituras (ISF 80→60, ISO 100→80) — a próxima atualização é a primeira
oportunidade de confirmar se é início de uma reversão de regime estrutural
ou ruído de um único carimbo.**

**A crush margin rompeu 2,50 USD/bu — monitorar se a esmagadora reduz ritmo
de esmagamento nos próximos dados ABIOVE/NOPA como consequência mecânica
esperada de margem comprimida.**

**A assunção plena da centralização de exportação de palma pela Danantara
(Indonésia) está marcada para 2026-09-01, a 5 dias** — potencial catalisador
para o óleo que ainda não aparece precificado.

**O D+90 da tese original do ratio Far/Soj vence em 2026-09-09, a 13 dias**
— checkpoint formal para reavaliar se o spread far÷soj reverteu ou seguiu
comprimindo, agora com dado real disponível para essa avaliação pela
primeira vez desde o D+7.

**A isenção PIS/Cofins do biodiesel segue sem confirmação de status, e o
monitor tributário do sistema não trouxe novo carimbo nesta janela** — segue
sendo a verificação manual mais urgente do conjunto fiscal.

**O USDA Crop Progress mostrou piora em dois cortes novos consecutivos
(16/08 e 23/08) — o próximo corte (nominalmente referente a 30/08) é a
primeira chance de saber se a tendência de deterioração continua.**

**A manchete "cenário confortável para soja" (27/08) segue sem corpo de
texto — buscar a matéria completa ou o WASDE (ainda ausente) para resolver a
tensão com a piora de condição de lavoura.**

**O WASDE segue fora da janela deste briefing** — o catalisador fundamental
mais capaz de confirmar ou contradizer a leitura de aperto de oferta
americana que esta análise atribui ao rali de soja.

**MPOB — sem números de palma extraídos, mesma barreira de longa data,
agora ainda mais relevante com o prazo da Danantara a 5 dias.**

**NOPA — fila `release-nopa-2026-08-27` sinaliza novo carimbo, mas o
`monthly_status` segue em 0,0 bool (paywall), sem alternativa de dado
primário sobre o crush americano.**

---

## Honestidade

**O que não foi possível validar nesta janela, por ordem de gravidade:**

1. **A trajetória exata de preço dentro do apagão (07-26/08).** Esta leitura
   sabe o ponto de partida (06/08) e o ponto de chegada (27/08) com precisão,
   mas não tem a série intermediária completa de CBOT para soja e óleo — o
   dump de 26/08 só trouxe farelo e heating oil. Não é possível saber se o
   movimento de +8,92% em soja e -1,78% em óleo ocorreu de forma gradual ao
   longo de treze sessões represadas ou concentrado em poucos dias — os
   indicadores sintéticos (crush margin, ratio, oil share) SIM têm série
   diária completa desde 20/08, o que parcialmente mitiga essa lacuna para
   as métricas derivadas, mas não para os preços absolutos de CBOT de soja e
   óleo entre 07 e 19/08.
2. **O COT de 25/08, a primeira fotografia que capturaria o posicionamento
   especulativo durante o próprio rali de soja/farelo** — o corte disponível
   (18/08) antecede o movimento principal.
3. **O WASDE, ausente desta janela** — permanece o relatório fundamental
   mais importante do calendário agrícola americano sem atualização
   verificável por este pipeline.
4. **O status da isenção PIS/Cofins do biodiesel** — sem novo carimbo do
   monitor tributário nesta janela, a lacuna identificada nas leituras
   anteriores permanece sem resolução.
5. **O corpo completo da manchete "USDA aponta... cenário confortável para
   soja" (27/08)** — headline sem texto (`headline: None`), tratada como
   sinal direcional (bullish milho / neutro-a-bearish fundamento de soja),
   não como dado quantitativo.
6. **MPOB (palma Malásia)** — página acessível, mas sem números extraídos
   pelo parser, agora especialmente relevante com o prazo da Danantara a
   apenas 5 dias.
7. **Se a queda do ISF (80→60) e do ISO (100→80) é sinal genuíno de início
   de reversão estrutural ou ruído de um único carimbo** — é a primeira vez
   que qualquer um dos dois índices muda de valor em toda a série de
   leituras conhecida, e uma única observação não permite diferenciar as
   duas hipóteses com confiança.

Nenhum número foi inventado nesta leitura: todo dado usa exclusivamente os
carimbos presentes no briefing de 2026-08-27, e as comparações contra o
período pré-apagão usam exclusivamente o último fechamento confirmado de
06/08 (citado nas dezenove leituras anteriores) como base de cálculo. A
confiança mais alta desta leitura recai sobre a direção dos três movimentos
de preço (soja e farelo em alta, óleo em baixa) e sobre a série completa de
indicadores sintéticos (20-27/08), porque ambos vêm de dado real e recente.
A confiança mais baixa recai sobre a atribuição causal exata do rali de
soja/farelo (enchente no meio-oeste vs. correlação com milho vs. outro fator
não capturado neste briefing) e sobre a trajetória intermediária de preço
dentro do próprio apagão, que esta leitura não tem como reconstruir com o
dado disponível.
