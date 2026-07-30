---
data: 2026-07-30
titulo: "Sessão de acomodação técnica: a soja (1.171,75 cts/bu, CBOT 2026-07-30, -0,36%) sobe intradia até 1.181,25 — acima do piso rompido ontem em 1.180,00 — mas é rejeitada e fecha 0,70% abaixo dele, enquanto o USD/BRL cai -0,93% (para 5,0739) fortalecendo o real e derrubando a paridade teórica em -1,30%; o farelo (317,50, -0,13%) mantém o ratio Far/Soj em 81,29%, quarta sessão seguida sem confirmar de forma robusta o rompimento de 80% que a fila reabre outra vez; e o óleo (68,27, -0,57%) aprofunda para a quarta sessão consecutiva a quebra do suporte de 72,00 (agora -5,18% abaixo, a mais funda desta janela) na véspera exata do vencimento da isenção PIS/Cofins do biodiesel (31/07), justo quando a margem de biodiesel americana devolve boa parte do salto revisado de ontem (-13,30%, para 1,3747 USD/galão) por causa do tombo do heating oil (-5,50%)"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT (ZSU26 soja / ZMU26 farelo / ZLU26 óleo) — sessão de 2026-07-30
  - CME heating_oil_cbot (HO=F) — sessão de 2026-07-30 (volume 34 contratos, print anômalo — ver Honestidade)
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, paridade BR, Índice de Sobra de Farelo, Índice de Suporte do Óleo) — 2026-07-30, com a linha 2026-07-29 recalculada (soja 1.176,00 e heating oil 4,3701, ambos diferentes dos valores usados na leitura de ontem — ver Honestidade)
  - BCB PTAX — 2026-07-30 (USD/BRL 5,0739, EUR/BRL 5,8467, Selic diária 0,052531% a.a.)
  - CEPEA/ESALQ Paranaguá via NAG — 2026-07-30 (suporte R$ 145,29/saca, var -1,04%)
  - CEPEA/ESALQ Paraná interior via NAG — 2026-07-30 (R$ 137,82/saca, var -0,85%)
  - NAG Físico BR (farelo MT/IMEA R$ 1.669,72/ton estável; Rondonópolis R$ 1.650,00/ton estável; RS R$ 1.640,00/ton estável; prêmios export PGUA farelo +0,05 USD/sht e óleo +0,08 cts/lb, ambos inalterados) — 2026-07-30
  - CFTC COT Managed Money — corte de 2026-07-21 (ainda o mais recente; próximo corte referente a 28/07, publicação normal ~31/07, agora a apenas 1 dia)
  - USDA Crop Progress — ainda 2026-07-26 (11% excelente + 52% boa + 7% ruim), sem corte novo
  - USDA WASDE — ausente da janela de 14 dias deste briefing, agora 20 dias de atraso desde o último dado (10/07/2026) — ver Honestidade
  - NOPA — fila `release-nopa-2026-07-30`, `monthly_status` continua em 0,0 bool (paywall), mesma barreira desde meados de junho
  - ABIOVE projeções mensais — balanços ago-dez/2026 (farelo/óleo/soja), sem alteração
  - NOAA CPC ENSO — 2026-07-30 (El Niño Advisory, inalterado desde pelo menos 16/07/2026)
  - MPOB — 2026-07-30 (21º dia consecutivo com o mesmo conteúdo exato de 3.439 caracteres, parser sem números extraídos)
  - BCBA Argentina — 2026-07-30 (nova tentativa após 7 dias de hiato desde 22/07; página acessível, ainda sem links de relatório detectados)
  - Notícias Agrícolas/Farm Progress RSS — 2026-07-30 (160 itens lidos, 5 mantidos; manchete "Limit waterhemp seed in soybeans with weeding by hand", farmprogress.com, sem conteúdo de preço)
  - Forecasts estatísticos internos — 2026-07-30 (spot ref já reflete o fechamento de hoje: soja 1.171,75 / farelo 317,50 / óleo 68,27; viés "altista" nas três — ver Honestidade)
  - system/tributario_watch.toml (lido apenas como referência, não editado) — 10 eventos, `atualizado_em` 2026-06-05 (55 dias sem atualização); trata `trib-PISCOFINS-BIODIESEL-ISENCAO-2026-07-31`
  - Cruza com [[2026-07-29_leitura-complexo]] (cuja leitura central é parcialmente revisada aqui), [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (D+7 reaberto de novo e ainda não confirmado — ver abaixo)
status: ativa
vies: [bear-soja, neutral-farelo, bear-oleo_soja]
---

## Visão geral

O complexo soja é uma fábrica com uma única matéria-prima (a soja em grão) e
dois produtos de saída em proporção fixa por bushel esmagado: o **farelo**
(fração proteica, ~78% da massa, vira ração animal) e o **óleo degomado**
(fração de gordura, ~18-20% da massa, vira óleo de cozinha e biodiesel). Quem
decide o ritmo de esmagamento é a esmagadora, olhando a **crush margin**
(valor de farelo + óleo por bushel, menos o custo daquele bushel de soja,
medido na CBOT — Chicago Board of Trade, a bolsa de referência mundial para
esses contratos) e o **oil share** (fração desse valor capturada pelo óleo).
O **ratio Far/Soj** (preço do farelo dividido pelo preço da soja, normalizado
pela conversão bushel↔short ton) mede o mesmo crush por outro ângulo: abaixo
de 80% o farelo está historicamente "abundante" frente à soja (zona bear);
acima de 87%, "apertado" (zona bull); entre os dois, zona neutra de
**mean-reversion** (opera nos dois lados do book).

**A sessão de hoje foi, em contraste marcante com o tombo generalizado de
ontem, uma sessão de acomodação — mas com um detalhe técnico que muda a
leitura do que aconteceu ontem.** A soja caiu apenas -0,36% (1.171,75
cts/bushel, CBOT, ante 1.176,00 no fechamento revisado de ontem — ver
Honestidade), o farelo caiu -0,13% (317,50 USD/short ton, ante 317,90) e o
óleo caiu -0,57% (68,27 cts/lb, ante 68,66). Números pequenos à primeira
vista, mas dois eventos dentro do dia carregam mais informação do que a
variação de fechamento sozinha sugere. **Primeiro: a soja subiu, dentro do
próprio pregão, até 1.181,25 — ou seja, tocou e ultrapassou por uma margem
pequena o nível de 1.180,00 que ela mesma havia rompido para baixo ontem
(quando caiu -2,49% e fechou a apenas 3,4% do range) — e foi vendida de
volta, fechando em 1.171,75, 0,70% ABAIXO daquele mesmo nível.** Esse é o
padrão técnico clássico de "retest e rejeição": um suporte que se rompe
tende, na sessão seguinte, a ser testado por baixo como nova resistência; se
o preço não consegue se sustentar acima dele, a rejeição reforça — não
enfraquece — a leitura de que o rompimento foi real. Foi exatamente isso que
aconteceu hoje, e é o desenvolvimento técnico mais importante da sessão para
a soja. **Segundo: o câmbio hoje trabalhou contra a soja em reais de forma
muito mais direta do que ontem** — o USD/BRL caiu -0,93% (BCB PTAX,
2026-07-30, para 5,0739, ante 5,1217 ontem), rompendo a sequência recente de
altas do dólar; como o CBOT também caiu, os dois efeitos se somaram na mesma
direção pela primeira vez em várias sessões, e a paridade teórica em reais
despencou -1,30% (para R$ 131,07/saca). O farelo, por sua vez, manteve o
ratio Far/Soj em 81,29% (indicators, 2026-07-30) — a quarta sessão seguida
(contando 07-27 a 07-30, com os dados revisados disponíveis hoje) em que o
indicador nunca fecha de forma inequívoca abaixo de 80%, apesar de ter
chegado extremamente perto duas vezes (80,09% e 80,01%, ambos revisados). E
o óleo estendeu pela quarta sessão seguida a quebra do suporte técnico de
72,00, fechando 68,27 — **5,18% abaixo do nível, a distância mais profunda
desta janela observada** — exatamente na véspera do vencimento da isenção
PIS/Cofins do biodiesel (31/07, a 1 dia). **Leitura de uma linha:** o pivô do
complexo hoje é o óleo, cuja quebra técnica se aprofunda pela quarta sessão
seguida às vésperas de um catalisador fiscal concreto e imediato; a maior
convicção desta leitura é que a rejeição da soja no retest de 1.180,00
reforça, tecnicamente, a tese bear tática aberta ontem; confiança
moderada-alta para soja e óleo (ambos com desenvolvimentos técnicos claros
e coerentes com a tese aberta ontem), e confiança baixa-a-moderada para
qualquer leitura direcional definitiva em farelo — o gatilho tático da tese
estrutural (ratio <80%) segue, pela quarta vez, sem confirmação robusta.

---

## Soja

**Viés: bear tático, reforçado por um padrão técnico de retest-e-rejeição —
a soja fechou 1.171,75 cts/bushel (CBOT, ticker ZSU26.CBT, -0,36% sobre o
fechamento revisado de ontem de 1.176,00), depois de subir intradia até
1.181,25 (0,11% acima do nível de 1.180,00 rompido ontem) e ser vendida de
volta para fechar 0,70% abaixo dele.** Nenhum item da fila de julgamento de
hoje trata explicitamente da soja (os quatro itens tratam óleo, o ratio
Far/Soj, o tributário do biodiesel e o NOPA) — esta leitura trata o
desenvolvimento técnico da soja como material por julgamento próprio, dando
sequência ao mesmo critério usado ontem.

### O que sustenta a tese

**A sessão foi de abertura no fechamento revisado de ontem, alta inicial até
a máxima, e venda de volta até fechar no terço inferior do range — um
padrão de retest técnico com rejeição.** Abertura 1.176,00 (gap zero sobre o
fechamento revisado de ontem, o mesmo padrão de abertura sem gap observado
em sessões recentes), máxima 1.181,25 (o ponto mais alto da sessão, tocado
depois da abertura), mínima 1.168,00 (um novo patamar, abaixo do fechamento
de ontem) e fechamento em 1.171,75. **Mecanismo e leitura:** o range do dia
foi de 13,25 cts (1.181,25-1.168,00); o fechamento ficou a 3,75 cts acima da
mínima, ou seja, em **28,3% do range** — no terço inferior, um fechamento
fraco, ainda que não tão extremo quanto o de ontem (3,4% do range). O ponto
central é a máxima do dia: 1.181,25 está tecnicamente ACIMA do nível de
1.180,00 que a soja rompeu para baixo ontem — ou seja, o mercado testou de
volta, dentro do próprio pregão, o nível recém-rompido, como seria esperado
num "retest" clássico de suporte-virado-resistência. **O preço não conseguiu
se sustentar ali e foi vendido de volta**, fechando 0,70% abaixo do nível.
Isso é, tecnicamente, uma confirmação adicional (não uma invalidação) da
tese de rompimento aberta ontem: um suporte rompido que resiste ao teste por
cima, na sessão seguinte, tende a reforçar sua nova função de resistência.
Se a próxima sessão repetir o padrão (teste e rejeição em torno de
1.180,00), a configuração técnica ficará ainda mais sólida para o lado
vendedor. O volume foi de 30.193 contratos; este briefing não traz, na
janela consultada, o OHLCV de soja de 29/07/2026 na tabela `cme_cbot` (só o
fechamento aparece, indiretamente, via a seção `indicators` — ver
Honestidade), então esta leitura não pode comparar o volume de hoje com o de
ontem, apenas registrar o nível absoluto.

**O câmbio, hoje, trabalhou CONTRA a soja em reais de forma mais direta do
que em qualquer sessão recente — rompendo a sequência de altas do dólar
documentada nas últimas leituras.** USD/BRL PTAX fechou em 5,0739 (BCB,
2026-07-30), queda de -0,93% sobre 5,1217 de ontem. Olhando a sequência
completa de pregões (pulando fins de semana): 5,0666 (24/07) → 5,1005
(27/07, +0,67%) → 5,1177 (28/07, +0,34%) → 5,1217 (29/07, +0,08%) → **5,0739
(30/07, -0,93%)** — três altas seguidas encerradas hoje com a maior queda
percentual em um único dia desde a mínima local de 5,0638 em 22/07/2026.
**Mecanismo:** a paridade teórica em reais (CBOT convertido pelo câmbio, sem
considerar basis/frete/ágio local) é `preço CBOT em cts × PTAX`; como o CBOT
caiu -0,36% e o câmbio caiu -0,93%, os dois efeitos hoje trabalharam **na
mesma direção** (diferente de ontem, quando iam em sentidos opostos e quase
se cancelavam) — a paridade calculada despencou para **R$ 131,07/saca**
(indicators, 2026-07-30: CBOT 1.171,75 cts × USD/BRL 5,0739), ante R$ 132,79
em 29/07 (revisado), uma queda de **-1,30%**, maior que a queda isolada do
papel. **Para quem opera a paridade em reais, isso é o desenvolvimento
cambial mais relevante da semana**: o real vinha se depreciando desde 22/07,
e hoje reverteu com força — se essa reversão persistir, ela passa a ser uma
pressão baixista adicional e independente do CBOT sobre o preço em reais da
soja, do farelo e do óleo, todos precificados via a mesma conversão.

**A base física em Paranaguá caiu bem menos que a paridade teórica pela
terceira sessão seguida — o prêmio de exportação segue alargando, agora no
maior nível desta janela observada.** CEPEA/ESALQ Soja Paranaguá (via NAG)
fechou em R$ 145,29/saca hoje, queda de -1,04% sobre R$ 146,81 de ontem —
uma fração menor que a queda de -1,30% da paridade teórica. Com a paridade
caindo para R$ 131,07, o **prêmio de exportação sobre a paridade subiu para
+10,85%** ((145,29-131,07)÷131,07), ante +10,56% no cálculo equivalente de
ontem com os dados revisados (146,81 vs paridade 132,79) — um alargamento de
quase 0,3 ponto percentual, dando sequência à trajetória de alargamento
documentada nas últimas leituras (que oscilou entre +7% e +9,7% ao longo de
julho antes de saltar para a casa dos 10% nesta semana). **Mecanismo e
leitura:** o mercado físico de exportação em Paranaguá segue, pela terceira
sessão seguida, não replicando integralmente o movimento do papel — nem para
baixo ontem (quando caiu menos que a queda do papel) nem hoje (quando também
caiu menos que a queda da paridade). Esta análise continua sem conseguir
distinguir com os dados disponíveis entre as duas hipóteses já levantadas
ontem: (a) demanda física de exportação genuinamente firme e descolada do
papel, um sinal estrutural bullish para quem vende físico; ou (b) atraso na
atualização do preço CEPEA/ESALQ frente ao movimento do CBOT e do câmbio. O
físico do Paraná interior também caiu menos que a paridade teórica (R$
137,82/saca, -0,85%) — reforçando que ambas as praças físicas seguem
absorvendo os choques do papel e do câmbio de forma mais moderada.

**A curva forward manteve a mesma pequena inversão de calendário no
vencimento mais próximo, com amplitude estável.** Agosto/26 (Q26) 1.175,00 →
Setembro/26 (U26, spot) 1.171,75 → Novembro/26 (X26) 1.188,50 → Janeiro/27
(F27) 1.202,75 → Março/27 (H27) 1.207,75. Agosto segue precificado ACIMA do
spot de setembro (+0,28%, ante +0,19% ontem) — a mesma inversão técnica de
calendário observada nas últimas leituras, com uma leve reabertura hoje. Da
parte de trás da curva em diante (U26→X26→F27→H27) a forma de contango segue
idêntica à documentada nos últimos dias — nenhum sinal novo de estresse
físico embutido.

**O COT de 21/07/2026 (CFTC, ainda o mais recente) seguia mostrando fundos
extremamente comprados em soja** — managed money net long de +130.505
contratos, 12,49% do open interest de 1.045.077 contratos. Nenhum dado novo
chegou hoje; o próximo corte (referente a 28/07, publicação normal ~31/07)
está agora a apenas **1 dia** — o teste mais direto de se essa posição
começou a ser desmontada depois de dois dias seguidos de fraqueza (tombo de
ontem + rejeição técnica de hoje).

**Os forecasts estatísticos internos (2026-07-30)**, recalculados com o
fechamento de hoje (1.171,75), seguem etiquetados como "altista": central 7d
= 1.190,12 cts/bu (bandas 1.131,82-1.248,42); central 30d = 1.245,27 cts/bu
(bandas 1.124,57-1.365,96). Esta leitura mantém o mesmo tratamento das
últimas sessões: o modelo (média móvel de 20 dias + volatilidade + inclinação
de curto prazo) é usado apenas como referência de banda estatística, não
como argumento de tese — ele não incorpora o padrão de retest-e-rejeição
documentado acima nem o câmbio.

**A manchete do dia (Farm Progress, 30/07/2026, "Limit waterhemp seed in
soybeans with weeding by hand") é de manejo agronômico, sem qualquer
conteúdo de preço ou oferta** — ao contrário das manchetes recentes sobre
"safra recorde" (27/07, 29/07), hoje não há sinal editorial adicional sobre
o tamanho da safra americana para incorporar a esta leitura.

### O que invalida / risco para a soja

- **Um fechamento consistente acima de 1.180,00** nas próximas sessões
  desfaria a leitura de retest-e-rejeição de hoje — o teste de hoje foi
  intradiário, e uma segunda tentativa bem-sucedida de romper e se sustentar
  acima do nível mudaria o quadro técnico de volta para o lado comprado.
- **O próximo corte do COT (28/07, publicação ~31/07, agora a 1 dia)
  mostrar se os fundos, extremamente comprados na foto de 21/07 (net long
  +130.505 contratos, 12,49% do open interest), já começaram a liquidar** —
  o teste mais aguardado desta janela para as três pernas.
- **O câmbio reverter a queda de hoje** — se o USD/BRL retomar a trajetória
  de alta das últimas semanas, a pressão baixista adicional sobre a paridade
  em reais desaparece, e a soja em reais volta a depender só do CBOT.
- **O prêmio de exportação em Paranaguá (agora +10,85%, novo máximo da
  janela) comprimir subitamente** — se o físico "alcançar" o papel e o
  câmbio de uma vez, isso indicaria que a demanda física não estava, de
  fato, blindada, e reforçaria a leitura bear.

### Leitura operacional — soja

O quadro de hoje é de **confirmação técnica via retest-e-rejeição**, um
desenvolvimento que reforça, e não enfraquece, a tese bear tática aberta
ontem. Para quem já está vendido desde o rompimento de ontem, a sessão de
hoje é um sinal de continuidade: o nível de 1.180,00 foi testado por cima e
rejeitado, com um novo stop lógico posicionável acima da máxima de hoje
(1.181,25) em vez de precisar recuar para a máxima de ontem (1.209,75),
apertando o risco da posição. Para quem está comprado, o retest fracassado
de hoje é um segundo sinal de alerta em dois dias — a tese de que o
rompimento de ontem foi "só um ajuste técnico pontual" perde força a cada
sessão em que o preço não retoma o nível. Para quem opera o câmbio como
perna adicional, a reversão do USD/BRL hoje (-0,93%) é, em si, um evento
a monitorar: se ela persistir, adiciona uma pressão baixista independente
do papel sobre a paridade em reais — relevante para quem trava operações via
paridade teórica. Para quem opera o book relativo entre papel e físico, o
prêmio de exportação em Paranaguá seguindo em máxima da janela (+10,85%) é,
pela terceira sessão seguida, uma operação de convergência potencial
(comprar basis físico contra vender papel), com o mesmo risco já apontado
ontem de que o físico simplesmente ainda não tenha reagido.

---

## Farelo

**Viés: neutro tático, dentro de uma tese estrutural bear ainda intacta — o
ratio Far/Soj fechou em 81,29% (indicators, 2026-07-30), a quarta sessão
seguida (07-27 a 07-30, usando os dados revisados disponíveis hoje) em que
o indicador nunca confirma de forma robusta o rompimento da zona
"comprimida" (<80%) que a tese estrutural de [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]
monitora desde 11/06/2026.** Trata `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
(reaberto de novo pela fila de hoje, pela mesma razão da última leitura — o
fato citado no texto do gatilho, "Ratio Far/Soj 81,4%", segue essencialmente
igual ao valor real de fechamento tanto de ontem quanto de hoje).

### O gatilho estrutural segue sem confirmação — agora pela quarta sessão

**Olhando a sequência com os dados mais atuais disponíveis nesta consulta
(alguns já revisados uma ou duas vezes em relação ao que foi reportado nas
leituras dos próprios dias), o ratio Far/Soj nunca fechou de forma
inequívoca abaixo de 80% em nenhuma das últimas quatro sessões — embora
tenha chegado extremamente perto duas vezes.** 07-27: 80,09% → 07-28: 80,01%
(revisado — a leitura de 28/07 original reportou 79,96%, abaixo do piso, mas
os dados revisados disponíveis desde 29/07 colocam esse fechamento acima de
80%) → 07-29: 81,10% (revisado — a leitura de 29/07 original reportou
81,34%, usando um fechamento de soja de 1.174,75 que o dump de hoje revisa
para 1.176,00) → **07-30: 81,29%**. Em nenhum desses quatro fechamentos,
usando os dados mais recentes disponíveis, o ratio jamais fechou
comprovadamente abaixo de 80% — as duas ocasiões em que pareceu ter
acontecido (79,96% em 28/07, segundo o dado daquele dia) foram, em ambos os
casos, revertidas por revisões de dados no dia seguinte. **Esta leitura
trata isso como um padrão relevante o suficiente para recomendar cautela
redobrada sobre a velocidade de confirmação deste gatilho tático
específico**: sete semanas e meia depois da compressão inicial de 11/06
(83,3%→81,4% em quatro pregões), o indicador segue "testando" o piso de 80%
repetidamente, sem nunca ter fechado de forma robusta e sustentada do outro
lado dele. Isso não invalida a tese estrutural mais lenta (ver abaixo), mas
esta análise considera que o gatilho tático de preço específico (ratio <80%)
está, na prática, mais próximo de "não confirmado até o momento" do que de
"testando ativamente" — uma recalibração de expectativa em relação às
leituras anteriores.

### O que sustenta a leitura de hoje

**O movimento do ratio hoje foi, de novo, puramente relativo — o farelo
caiu menos que a soja, mas ambos caíram.** Farelo CBOT (ZMU26.CBT) abriu em
318,80 (0,28% acima do fechamento revisado de ontem, um pequeno gap
positivo), fez máxima de 319,90 e mínima de 315,40, fechando em 317,50 —
queda de -0,13% no dia. O fechamento equivale a 46,7% do range
((317,50-315,40)÷(319,90-315,40)) — praticamente no meio, um comportamento
morno, tipicamente neutro, sem viés direcional forte dentro da própria
sessão. O volume foi de 28.072 contratos — bem abaixo dos 57.169 registrados
em 29/07 nos dados revisados disponíveis hoje (que diferem, por sua vez, dos
47.456 contratos citados na leitura de ontem — outra revisão de dados, ver
Honestidade), uma queda de -50,9% no volume dia a dia usando os números mais
atuais — a sessão de menor participação em farelo desta janela recente,
coerente com uma sessão de baixa convicção direcional isolada, mesmo com o
ratio se mantendo estável em torno de 81%.

**A curva forward de farelo segue em contango normal e completo, sem
qualquer sinal de inversão de calendário** — diferente da soja e do óleo,
que mantêm suas respectivas distorções técnicas (ver seções específicas).
Agosto/26 (Q26) 314,10 → Setembro/26 (U26, spot) 317,50 → Outubro/26 (V26)
318,20 → Dezembro/26 (Z26) 322,70 → Janeiro/27 (F27) 325,20 — uma curva
inteiramente crescente, do vencimento mais próximo ao mais distante, sem
nenhum ponto fora de ordem. **Mecanismo:** essa forma "normal" de curva é
consistente com o excedente estrutural de farelo no Brasil (ver ABIOVE
abaixo) não estar gerando nenhum estresse físico de curtíssimo prazo capaz
de inverter o calendário — ao contrário do óleo, cuja curva em
backwardation aponta para um aperto físico relativo mais imediato.

**O COT de 21/07/2026 (CFTC, ainda o mais recente) segue mostrando managed
money extremamente comprado em farelo** — net long de 73.476 contratos
(11,89% do open interest de 618.289 contratos). Com o ratio ainda
confortavelmente na zona neutra hoje (81,29%), essa posição comprada não
está, por ora, posicionada contra um gatilho tático de preço confirmado —
apenas contra a tese estrutural mais lenta (ABIOVE, ISF). O corte de 28/07
(publicação ~31/07, agora a 1 dia) é o dado mais aguardado para ver se essa
posição já começou a ser reduzida.

**A crush margin recuou ligeiramente hoje, para 2,7772 USD/bushel (-0,33%
sobre o valor revisado de ontem de 2,7864)** — Board Crush: farelo 317,50 +
óleo 68,27 − soja 1.171,75; sequência recente (07-27: 2,8426 → 07-28: 2,7365
→ 07-29: 2,7864 revisado → **07-30: 2,7772**). **Mecanismo:** hoje as três
pernas caíram em proporções mais parecidas entre si do que ontem — a soja
(custo) caiu -0,36%, e a soma farelo+óleo (receita, em pontos absolutos:
317,90+68,66=386,56 ontem revisado vs 317,50+68,27=385,77 hoje, -0,20%) caiu
uma fração menos — o resultado líquido é uma crush praticamente estável,
oscilando numa faixa estreita entre 2,74 e 2,84 USD/bu nas últimas quatro
sessões, sem uma tendência direcional clara emergindo. A crush segue
folgada em termos absolutos, distante do nível de alerta histórico citado em
leituras passadas (<2,50 USD/bu).

**O oil-meal spread caiu para 0,5247 USD/bushel** (ante 0,5588 no valor
revisado de ontem, -6,10%) — dando sequência à trajetória de compressão
documentada nas últimas leituras (07-27: 0,7469 → 07-28: 0,6468 → 07-29:
0,5588 revisado → **07-30: 0,5247**), agora quatro sessões seguidas de
queda usando a série de dados mais consistente disponível. **Mecanismo:** o
óleo caiu -0,57% enquanto o farelo caiu apenas -0,13% — o farelo continua
ganhando terreno relativo sobre o óleo dentro do valor do crush. Como já
notado nas leituras anteriores, isso significa que o farelo está
relativamente FORTE frente ao óleo (spread comprimindo) ao mesmo tempo em
que permanece dentro da zona neutra frente à soja (ratio em 81,29%, não
abaixo de 80%) — a leitura "farelo bear" segue dependendo inteiramente de
contra qual perna a comparação é feita.

**As praças físicas de farelo no Brasil (NAG) seguem totalmente estáveis
hoje** — Mato Grosso/IMEA R$ 1.669,72/ton (var 0,0%), Rondonópolis R$
1.650,00/ton (var 0,0%) e RS R$ 1.640,00/ton (var 0,0%), nos mesmos níveis
documentados há mais de uma semana. O prêmio de exportação em Paranaguá
segue zerado em +0,05 USD/short ton, agora **27 dias corridos sem variação**
desde 03/07/2026 — o pilar mais persistente e, nesta leitura, o mais
importante da tese estrutural: o mercado internacional segue simplesmente
não pagando o suficiente para tirar farelo do Brasil, então o excedente
continua represado no mercado interno independentemente de qualquer
oscilação diária do ratio.

**O Índice de Sobra de Farelo (ISF) permanece em 80/100 (4 de 5 condições
estruturais), com print de 30/07/2026** — inalterado desde pelo menos
01/07/2026, sem qualquer relação mecânica com o ratio tático (o índice usa
critérios estruturais que não se moveram hoje). **A trajetória ABIOVE**
(sem alteração) segue mostrando a exportação de farelo brasileiro projetada
caindo de 1.400 mil toneladas em agosto/2026 para 700 mil toneladas em
dezembro/2026 (-50% em quatro meses), com produção caindo bem menos
(2.285,06 → 1.659,04 mil toneladas, -27,4%) — o excedente estrutural segue
intacto e continua sendo, nesta leitura, um pilar bem mais sólido para uma
eventual tese bear-farelo do que o ratio tático, que segue, pela quarta
sessão seguida, sem confirmar um fechamento robusto abaixo de 80%.

### O que invalida / risco para o farelo

- **O ratio Far/Soj precisa fechar de forma robusta e repetida abaixo de
  80% para validar qualquer tese tática bear** — depois de quatro sessões
  testando o piso sem uma confirmação que sobreviva à revisão de dados do
  dia seguinte, esta leitura reforça a recomendação de tratar qualquer
  fechamento pontual perto de 80% com ceticismo até 2-3 sessões consecutivas
  confirmarem o mesmo lado do piso nos dados já revisados.
- **A crush margin, se voltar a subir com força**, pode incentivar a
  esmagadora a acelerar o ritmo de esmagamento — aumentando a oferta física
  de farelo e reforçando a tese estrutural ABIOVE/ISF de excedente.
- **O próximo corte do COT (28/07, publicação ~31/07, agora a 1 dia)**
  mostrar os fundos vendendo ou comprando mais em farelo — muda o peso
  relativo entre o argumento estrutural (bear) e o posicionamento
  especulativo.
- **O prêmio de exportação em Paranaguá sair de zero** depois de 27 dias
  parado — o pilar mais persistente da tese estrutural, mas também o que,
  se quebrar, mais mudaria o quadro.

### Leitura operacional — farelo

Depois de quatro sessões seguidas sem confirmação robusta do rompimento
tático, esta leitura recomenda manter o farelo como **neutro tático dentro
de uma tese estrutural bear ainda válida, mas não confirmada por gatilho de
preço**. Para quem monta posições com base no ratio Far/Soj isolado, o
padrão dos últimos quatro dias — testar o piso, quase romper, ser revisado
de volta para cima — é, em si, uma informação: este indicador específico
está exigindo uma margem de segurança maior do que o normal antes de
qualquer entrada tática. Para quem opera o oil-meal spread, a compressão
por quatro sessões seguidas (-6,10% hoje, a mais recente de uma sequência
consistente) segue sendo a expressão mais limpa e menos sujeita a revisão
da força relativa do farelo dentro do complexo — capturar farelo contra
óleo continua sendo, nesta leitura, mais robusto tecnicamente do que
capturar farelo contra soja isoladamente.

---

## Óleo

**Viés: bear tático, com a quebra técnica se aprofundando pela quarta sessão
seguida — o óleo fechou em 68,27 cts/lb (-0,57% sobre o fechamento revisado
de ontem de 68,66), agora **5,18% abaixo** do suporte de 72,00 (ante -4,65%
ontem, -2,28% em 28/07) — a distância mais profunda desta janela observada —
enquanto a margem de biodiesel americana devolveu boa parte do salto
revisado de ontem, caindo -13,30% hoje, para 1,3747 USD/galão.** Trata
`alerta-quebra_suporte-oleo_cbot-2026-07-30` (quarta confirmação consecutiva
do rompimento, e a mais profunda até agora).

### O que sustenta a tese

**A sessão de hoje foi de fechamento no terço inferior do range, dando
sequência ao padrão fraco das últimas sessões.** Abertura 68,65 (gap
essencialmente zero sobre o fechamento revisado de ontem, -0,01%), máxima
69,12 (tocada cedo, sem sustentação), mínima 67,98 (um novo patamar, abaixo
do fechamento de ontem) e fechamento em 68,27 — **25,4% do range**
((68,27-67,98)÷(69,12-67,98)). **Mecanismo e leitura:** pela quarta sessão
seguida (27/07, 28/07, 29/07, hoje) o óleo fecha na porção inferior do seu
range diário, um padrão de venda persistente sem recompra relevante que
sustente uma reversão técnica. O volume foi de 41.545 contratos; este
briefing não traz o OHLCV de óleo de 29/07/2026 na janela consultada (mesma
limitação de truncamento observada para a soja — ver Honestidade), então
não é possível comparar volumes dia a dia para o óleo nesta leitura.

**A margem de biodiesel americana, pelo quarto dia seguido o dado mais
importante e menos óbvio desta sessão para o óleo, inverteu de direção
hoje — uma queda expressiva, mas cujo mecanismo aponta para o heating oil,
não para o óleo de soja em si.** Custo do óleo: 5,1202 USD/galão (7,5 lb ×
68,27 cts/lb), ante 5,1495 no valor revisado de ontem (-0,57%, seguindo a
queda do preço do óleo). Receita: 7,2949 USD/galão (heating oil 4,1299 +
1,5×RIN D4 2,11), ante 7,5351 no valor revisado de ontem (-3,19%). Margem:
**1,3747 USD/galão**, ante 1,5856 no valor revisado de ontem (-13,30%).
**Mecanismo:** o custo do óleo caiu apenas -0,57%, mas a receita caiu
-3,19% — a diferença inteira vem do heating oil, que despencou -5,50% hoje
(4,3701→4,1299, note-se: o valor de 4,3701 usado aqui para ontem é ele
próprio uma revisão do que o dump de ontem trazia, 4,2223 — ver
Honestidade). Como o componente do RIN D4 é fixo (2,11 USD/RIN), a queda
absoluta da receita (0,2402 USD/galão) é idêntica à queda absoluta do
heating oil — uma relação mecânica exata que confirma que **a reversão da
margem hoje é inteiramente uma história de heating oil, não de deterioração
da demanda de biodiesel por óleo de soja em si.** Em termos absolutos, a
margem de hoje (1,3747) segue acima dos níveis observados em 24/07 (1,0354)
e 27/07 (1,1629) — não é um colapso, é a devolução parcial de um salto que,
uma vez revisado, era ainda maior do que o reportado ao vivo ontem.

**O heating oil (HO=F) trouxe hoje outro print de volume extremamente baixo
— mas o dado de ontem, agora revisado, confirma de forma direta a suspeita
levantada nas últimas três leituras.** O volume de hoje veio com apenas
**34 contratos** — um nível tão anômalo quanto os das sessões anteriores.
**O ponto mais importante, porém, é retrospectivo: o volume de 29/07/2026,
reportado na leitura de ontem como 70 contratos, aparece no dump de hoje
como 20.424 contratos — uma revisão de quase 292 vezes o valor original.**
Isso confirma, com um caso concreto, a hipótese levantada nas três últimas
leituras de que os prints de volume de heating oil chegam preliminares e são
revisados substancialmente para cima em dumps subsequentes. **Esta leitura
trata o print de hoje (34 contratos) com a mesma expectativa: é
provavelmente um número preliminar, e não deve ser usado como evidência de
baixa liquidez real no mercado de heating oil.** O preço de fechamento, por
outro lado, não mostrou até agora o mesmo padrão de revisão retroativa tão
grande quanto o volume — mas dado que o preço de ontem (4,2223 na leitura de
ontem) também foi revisado hoje para 4,3701 (uma diferença de +3,5%, bem
menor que a do volume, mas não desprezível), esta leitura recomenda tratar o
fechamento de hoje do heating oil (4,1299) com uma margem de cautela
adicional, inclusive no cálculo da margem de biodiesel que depende dele.

**O Índice de Suporte do Óleo (ISO) permanece em 100/100 (5 de 5
condições), com print de 30/07/2026** — a tese estrutural (óleo dominando o
valor do crush) segue formalmente intacta, sem nenhuma alteração apesar da
quarta sessão seguida de quebra técnica do preço.

**O oil share caiu para 51,81%** (ante 51,92% no valor revisado de ontem,
-0,11 ponto percentual) — dando sequência à trajetória de queda documentada
nas últimas leituras (52,52% em 27/07 → 52,19% em 28/07 → 51,92% em 29/07
revisado → **51,81%** hoje), a um ritmo mais lento que nas sessões
anteriores, mas ainda na mesma direção, agora bem abaixo da faixa de
53,0-53,5% em que o indicador oscilou até 22/07/2026. **Mecanismo:** o óleo
caiu -0,57% enquanto o farelo caiu apenas -0,13%, encolhendo ainda mais a
fração de valor do crush capturada pelo óleo. A distância entre esta leitura
tática (oil share em queda persistente) e a estrutural (ISO travado em 100)
segue crescendo, sem ainda um gatilho formal de revisão do índice.

**O COT de 21/07/2026 (CFTC, ainda o mais recente) seguia mostrando o óleo
como a perna mais concorrida das três** — managed money com 143.159
contratos comprados, 18,17% do open interest de 661.652 contratos (ante
12,49% em soja e 11,89% em farelo). Com quatro sessões seguidas de quebra
técnica desde a foto de 21/07 (27/07, 28/07, 29/07 e hoje), a pressão sobre
esse posicionamento comprado é, nesta leitura, a mais alta das três pernas —
o corte de COT de 31/07 (agora a 1 dia) é o dado mais aguardado para esta
perna especificamente.

**A curva forward manteve a backwardation, com forma preservada e amplitude
estável.** Agosto/26 (Q26) 68,49 → Setembro/26 (U26, spot) 68,27 (-0,22,
-0,32%) → Outubro/26 (V26) 67,71 (-0,56, -0,82%) → Dezembro/26 (Z26) 67,30
(-0,41, -0,61%) → Janeiro/27 (F27) 67,15 (-0,15, -0,22%) — uma queda total de
-1,34 cts/lb (-1,96%) de agosto a janeiro/27, uma amplitude ligeiramente
menor que os -2,27% observados ontem, mas ainda claramente em
backwardation, sinalizando aperto físico relativo de curto prazo sem sinal
de estresse agudo adicional.

### O que invalida / risco para o óleo

- **Um fechamento abaixo de 67,98** (mínima de hoje) confirmaria uma quinta
  sessão seguida de fraqueza técnica e reforçaria a leitura de que a quebra
  de suporte não é mais um evento pontual, mas uma tendência estabelecida.
- **O heating oil (HO=F) precisa urgentemente de uma sessão de volume
  normal e estável** — depois de quatro sessões seguidas de prints anômalos
  (278→23.447 revisado; 788→20.424 revisado; 34 hoje), esta leitura reforça
  a recomendação de cautela máxima com qualquer leitura de convicção baseada
  em volume recente deste instrumento, e nota que agora até o PREÇO de
  ontem já mostrou uma revisão não trivial (+3,5%).
- **O oil share continuar caindo abaixo de 51,81%** por mais sessões —
  reforçaria a leitura de perda estrutural de participação do óleo no valor
  do crush, o indicador tático mais próximo de contradizer o ISO 100/100.
- **O próximo corte do COT (28/07, publicação ~31/07, agora a 1 dia)
  confirmar liquidação no net long mais concorrido das três pernas (18,17%
  do OI)** — com quatro sessões seguidas de quebra técnica desde a foto de
  21/07, este é o teste mais direto e mais aguardado desta janela.
- **A isenção PIS/Cofins do biodiesel expirar em 31/07 sem renovação** (ver
  Lente fiscal), agora a apenas **1 dia**, sem nenhuma atualização do
  monitor tributário há 55 dias — um vetor bearish direto para a demanda
  doméstica de óleo, independente do CBOT e da margem americana.
- **MPOB seguir inacessível** (21º dia consecutivo) — mantém cego o efeito
  de eventuais movimentos no prêmio de substituição via palma.

### Leitura operacional — óleo

O óleo segue sendo a perna com a tensão mais explícita entre técnico e
fundamento, e hoje a balança pendeu ligeiramente mais para o lado técnico:
quarta sessão seguida de quebra do suporte de 72,00, a mais profunda até
agora, ao mesmo tempo em que a margem de biodiesel — o principal
contraponto fundamentalista das últimas leituras — devolveu boa parte do
salto revisado de ontem, ainda que por um mecanismo (heating oil, não
demanda de óleo de soja) que não necessariamente enfraquece o argumento de
demanda física. Para quem está comprado direcional, a sequência de quatro
quebras seguidas, cada uma mais funda que a anterior, e agora sem o reforço
da melhora de margem de ontem, é motivo concreto para reduzir exposição ou
apertar o stop para a mínima de hoje (67,98) — o quadro de hoje pesa mais
para o lado vendedor do que o de ontem. Para quem opera vendido ou tático
short, a mínima de hoje (67,98) é a referência de entrada mais recente, com
stop acima da máxima do dia (69,12); o vencimento da isenção PIS/Cofins
amanhã (31/07) é o catalisador mais próximo e mais concreto de toda esta
leitura, e uma posição short tática ganha um argumento fundamentalista
adicional se a isenção expirar sem renovação. Para quem opera o crush ou o
oil-meal spread, a compressão pela quarta sessão seguida (ver Farelo) segue
sendo a expressão mais limpa e consistente da tensão entre as duas pernas de
saída do esmagamento — favorável ao lado "farelo forte / óleo fraco" dentro
do crush, com o oil share reforçando a mesma leitura de forma independente.

---

## Spreads e crush — leitura de complexo

### Ratio Far/Soj: 81,29% — quarta sessão seguida sem confirmar o rompimento de 80% que a fila insiste em reabrir

Com os dados mais atuais disponíveis nesta consulta, o ratio nunca fechou de
forma inequívoca abaixo de 80% em nenhuma das últimas quatro sessões
(07-27: 80,09% → 07-28: 80,01% revisado → 07-29: 81,10% revisado → **07-30:
81,29%**), embora tenha chegado extremamente perto duas vezes. A fila de
hoje reabriu, mais uma vez, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
— o mesmo item reaberto na leitura de ontem, citando essencialmente o mesmo
valor de ratio ("81,4%"). Esta leitura recomenda tratar esse gatilho tático
específico como formalmente não confirmado até segunda ordem, sem prejuízo
da tese estrutural mais lenta (ABIOVE/ISF), que segue intacta e é discutida
de forma independente na seção Farelo. O checkpoint D+90 (2026-09-09)
permanece como o próximo marco formal de revisão da tese completa.

### Crush margin: 2,7772 USD/bu — estabilidade numa faixa estreita, sem tendência clara

Recuou -0,33% no dia (2,7864 → 2,7772, valores revisados/atuais), a quarta
sessão seguida oscilando dentro de uma faixa relativamente estreita (2,74 a
2,84 USD/bu). O mecanismo de hoje foi de três pernas caindo em proporções
mais parecidas entre si do que em sessões anteriores — sem o desequilíbrio
acentuado (soja caindo muito mais rápido que farelo+óleo, ou vice-versa) que
caracterizou os últimos dias. A crush segue folgada em termos absolutos,
distante do nível de alerta histórico citado em leituras passadas
(<2,50 USD/bu).

### Oil share: 51,81% — sexta sessão seguida de queda (contando a sequência revisada), ritmo mais lento

Caiu -0,11 ponto percentual (51,92% → 51,81%, valores revisados/atuais),
estendendo a sequência de quedas iniciada quando o indicador saiu da faixa
estreita de 53,0-53,5% em que oscilou até 22/07. O ritmo de queda de hoje é
bem mais lento que o de sessões anteriores (que chegou a -0,32pp em um único
dia), mas a direção persistente segue sendo o padrão mais consistente desta
janela observada para qualquer indicador do crush. Ainda não é uma ruptura
estrutural (o ISO permanece 100/100).

### Oil-meal spread: 0,5247 USD/bu — quarta compressão seguida

Caiu -6,10% no dia (0,5588 → 0,5247, valores revisados/atuais), a quarta
sessão seguida de compressão nesta métrica. O farelo segue ganhando terreno
relativo sobre o óleo dentro do valor do crush — a expressão mais
consistente e menos sujeita a revisão de qualquer indicador do complexo
nesta janela.

### Margem de biodiesel: 1,3747 USD/gal — devolve parte do salto revisado de ontem, mecanismo é o heating oil, não o óleo

Caiu -13,30% no dia (1,5856 → 1,3747, valores revisados/atuais). Ao
contrário da queda do preço do óleo (-0,57%, pequena), a queda da margem
veio quase inteiramente do heating oil (-5,50%), com o RIN D4 fixo (2,11
USD/RIN) explicando por que a queda absoluta da receita reproduz
exatamente a queda absoluta do heating oil. Em termos absolutos, a margem
de hoje segue acima dos níveis do início da semana (24/07: 1,0354; 27/07:
1,1629) — uma devolução parcial, não um colapso.

### COT: corte de 21/07, ainda o mais recente — agora a apenas 1 dia do próximo corte

O corte de 21/07/2026 mostrava fundos extremamente comprados nas três
pernas (net long +73.476 farelo/11,89% OI, +120.246 óleo/18,17% OI,
+130.505 soja/12,49% OI). Nenhum dado novo chegou hoje. O próximo corte
(referente a 28/07, publicação normal ~31/07) está agora a apenas **1 dia**
e é, para as três pernas, o teste mais direto de se a posição especulativa
esticada já começou a ser desmontada — ganha relevância adicional depois de
quatro dias seguidos de fraqueza técnica em óleo e de um episódio de
retest-e-rejeição em soja hoje.

### ISF em 80/100, ISO em 100/100 — ambos inalterados, prints de 30/07

Os dois índices sintéticos, que captam condições estruturais (não a
mecânica tática de preço intradiário), permanecem exatamente nos mesmos
níveis desde pelo menos 01/07/2026. Eles não se moveram apesar da quarta
quebra seguida do óleo e da estabilidade do ratio na zona neutra — coerente
com sua natureza estrutural.

### O que os índices dizem juntos em 30/07/2026

ISF 80/100 + ISO 100/100 (ambos inalterados) + ratio Far/Soj na zona neutra
pelo quarto dia seguido, sem confirmar o rompimento tático que a fila
insiste em reabrir (81,29%) + crush margin estável numa faixa estreita
(2,7772, -0,33%) + oil share no menor nível desta janela (51,81%, sexta
queda seguida em ritmo mais lento) + oil-meal spread na quarta compressão
seguida (-6,10%) + margem de biodiesel devolvendo parte de um salto
revisado (-13,30%, mecanismo é o heating oil) + COT ainda parado no corte de
21/07 (fundos extremamente comprados nas três pernas, posição testada por
quatro dias seguidos de fraqueza técnica em óleo, ainda não confirmada como
desmontada) formam, juntos, um quadro de **acomodação técnica generalizada
depois do tombo de ontem, mas com o óleo isolado como a perna que mais
aprofunda sua própria fraqueza** — a soja teve um episódio técnico
relevante (retest e rejeição em 1.180,00) sem grande variação de
fechamento, o farelo segue estável dentro da zona neutra pela quarta
sessão, e o óleo é a única perna que registrou hoje um novo extremo da
janela (quebra mais profunda do suporte). O próximo corte do COT (31/07, a
1 dia) é o dado que mais provavelmente resolve parte desta complexidade.

---

## Lente fiscal e regulatória BR

**Isenção PIS/Cofins biodiesel — vencimento em 31/07/2026, agora a apenas 1
dia, ainda sem sinalização pública de renovação** (evento
PISCOFINS-BIODIESEL-ISENCAO, `atualizado_em` 2026-06-05, sem mudança desde
então — agora 55 dias sem atualização do monitor). Trata
`trib-PISCOFINS-BIODIESEL-ISENCAO-2026-07-31`, sinalizado pela fila de hoje
com a tag `[1d]`, o vetor tributário de maior prioridade de monitoramento no
momento, agora no limite. **O mecanismo:** a isenção incide na saída do
biodiesel; se expirar sem renovação, o custo tributário efetivo da produção
sobe, o que tende a reduzir a margem de biodiesel doméstica (distinta da
margem americana calculada nesta leitura, que hoje recuou -13,30% por causa
do heating oil, não do regime tributário brasileiro) e, por extensão,
pressionar a demanda por óleo de soja como insumo dentro do mix B15
mandatório — um vetor bearish direto para o óleo doméstico, independente do
que aconteça no CBOT ou na margem americana. **A proximidade do vencimento
(1 dia) sem qualquer atualização do monitor tributário nos últimos 55 dias é
o ponto de maior tensão desta leitura para o óleo** — não há como saber, a
partir dos dados disponíveis neste briefing, se uma prorrogação já está
sendo negociada ou se a expiração é o cenário-base; esta leitura trata a
falta de sinal como neutro-a-levemente-bearish por omissão (ausência de
notícia de renovação às vésperas do vencimento tende a ser lida pelo mercado
como risco, não como não-evento).

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L) —
vigência formal venceu há 19 dias (`vigencia_ate` 11/07/2026), sem qualquer
atualização de status.** Enquanto o combustível fóssil segue formalmente
subsidiado (sem confirmação de que o subsídio de fato terminou), a
competitividade relativa do biodiesel dentro do mix B15 mandatório segue
pressionada.

**B16 — sem data, travado em B15**, sem mudança de status. Testes técnicos
do FNDCT com resultado esperado ~nov/2026 — realista só fim de 2026/início
de 2027.

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
(centralização estatal da exportação de palma, plena em 01/09/2026);
INDONESIA-B50 (provável B45 em 2026, B50 pleno só 2027-28);
INDONESIA-LEVY-PMK9 (imposto de exportação de CPO até 12,5%, encarecendo
palma). Conjunto estruturalmente bullish para óleo de soja via substituição
de palma, mas inverificável pelo lado de mercado (MPOB inacessível há 21
dias, ver Honestidade).

**O monitor tributário como um todo está há 55 dias sem qualquer
atualização** — o intervalo se mantém exatamente no dia do vencimento da
isenção PIS/Cofins (1 dia). Prioridade máxima de manutenção do sistema,
independentemente da leitura de preço de hoje.

---

## Riscos e eventos próximos

**A isenção PIS/Cofins do biodiesel vence em 31/07/2026, agora a apenas 1
dia**, sem sinalização de renovação — prioridade máxima de monitoramento até
a resolução (fila `trib-PISCOFINS-BIODIESEL-ISENCAO-2026-07-31`), e o
catalisador concreto mais próximo de toda esta leitura.

**O próximo corte do COT (referente a 28/07/2026, publicação normal
~31/07/2026)**, agora a apenas 1 dia, é o dado mais aguardado de toda esta
janela para as três pernas — vai mostrar se os fundos que compraram
agressivamente na semana de 21/07 começaram a vender depois de quatro dias
seguidos de fraqueza técnica em óleo e um episódio de retest-e-rejeição em
soja hoje.

**O ratio Far/Soj precisa de 2-3 fechamentos consecutivos claramente de um
lado do piso de 80% para gerar qualquer confiança tática** — depois de
quatro sessões seguidas sem uma confirmação que sobreviva à revisão de
dados do dia seguinte, esta leitura mantém a recomendação de tratar
qualquer leitura pontual deste indicador com ceticismo redobrado.

**O nível de 1.180,00 na soja, testado por cima e rejeitado hoje, precisa de
uma segunda tentativa de rompimento para mudar o quadro técnico** — se a
próxima sessão repetir o padrão de teste-e-rejeição, a configuração para o
lado vendedor fica ainda mais sólida; um fechamento sustentado acima do
nível desfaria a leitura.

**O heating oil (HO=F) está na quarta sessão seguida de volume anômalo**
(278 revisado para 23.447; depois 788 revisado para 20.424; depois 34 hoje)
— o caso concreto de revisão de ontem (70→20.424, quase 292x) confirma a
suspeita já levantada nas últimas três leituras; esta série de leituras
mantém a máxima cautela com qualquer leitura de convicção baseada em volume
recente de heating oil, e agora estende essa cautela também ao preço (que
mostrou uma revisão de +3,5% para a sessão de ontem).

**NOPA — fila `release-nopa-2026-07-30` sinaliza um novo "release", mas o
dado segue inacessível** (`monthly_status` em 0,0 bool, mesma barreira de
assinatura paga desde meados de junho) — sem crush americano confirmado por
fonte primária, agora há quase sete semanas.

**MPOB — sem números de palma extraídos há 21 dias consecutivos**, mantendo
cego o efeito do El Niño e dos vetores regulatórios indonésios sobre o
prêmio de substituição do óleo de soja.

**O WASDE segue fora da janela de 14 dias deste briefing**, agora **20 dias
de atraso** desde o último dado (10/07/2026) — nenhuma pergunta de tese que
dependa do WASDE pode ser respondida a partir deste briefing.

---

## Honestidade

O que não foi possível validar neste briefing de 30/07/2026, e uma série de
revisões materiais em relação à leitura de ontem, onde a confiança é baixa
ou há lacunas relevantes:

**1. Múltiplos valores usados na leitura de 29/07/2026 foram revisados no
dump de hoje.** O fechamento de soja de 29/07 usado ontem (1.174,75)
aparece hoje, via a seção `indicators`, recalculado a partir de um valor de
1.176,00 — uma revisão pequena (+0,11%), mas que, combinada com outras,
altera os indicadores derivados: a crush margin de 29/07 (reportada ontem
como 2,8110) recalcula hoje para 2,7864; o ratio Far/Soj de 29/07
(reportado ontem como 81,34%) recalcula para 81,10%; o oil-meal spread
(reportado como 0,5445) recalcula para 0,5588; o oil share (reportado como
51,87%) recalcula para 51,92%; e a paridade em reais (reportada como
R$ 132,64/saca) recalcula para R$ 132,79. Nenhuma dessas revisões muda a
direção qualitativa das conclusões de ontem, mas todas confirmam, mais uma
vez, que o fechamento mais recente de qualquer dump deve ser tratado como
preliminar até aparecer de forma estável num dump subsequente — o quarto dia
seguido em que este padrão é identificado nesta série de leituras.

**2. O heating oil (HO=F) trouxe a confirmação mais concreta até agora do
padrão de revisão de volume suspeitado nas últimas três leituras: o volume
de 29/07/2026, reportado ontem como 70 contratos, aparece hoje como 20.424
contratos — uma revisão de quase 292 vezes.** O preço de fechamento de
29/07 também foi revisado (de 4,2223 para 4,3701, +3,5%) — menor que a
revisão de volume, mas a primeira vez nesta janela em que o PREÇO de
heating oil (não só o volume) mostra uma revisão não trivial. O print de
hoje (34 contratos) deve, por extensão do mesmo padrão, ser tratado como
preliminar e sujeito a revisão substancial para cima em dumps futuros.

**3. O volume de farelo de 29/07/2026 também foi revisado** — de 47.456
contratos (reportado na leitura de ontem) para 57.169 contratos no dump de
hoje (+20,5%) — mais um caso do mesmo padrão de revisão retroativa de
volumes, desta vez numa perna que não havia mostrado esse comportamento
antes.

**4. Os dados de OHLCV (abertura/máxima/mínima/fechamento/volume) de soja e
óleo para 29/07/2026 não estão disponíveis na tabela `cme_cbot` desta
janela de 14 dias** — apenas os valores de fechamento aparecem,
indiretamente, via a seção `indicators`. Esta é a mesma limitação
identificada nas duas últimas leituras para datas anteriores, agora
confirmada como um padrão estrutural recorrente na forma como o dump de 14
dias trunca a tabela `cme_cbot` — não um evento isolado. Como consequência,
esta leitura não pode comparar volumes de soja e óleo entre sessões
recentes, apenas citar o nível absoluto do dia mais atual.

**5. O veredito desta leitura sobre a soja — de que o retest e a rejeição
em 1.180,00 é o desenvolvimento técnico mais relevante do dia — é uma
interpretação própria desta análise, não um alerta gerado pelo sistema.** A
fila de julgamento de hoje não sinalizou nenhum evento de nível técnico para
a soja (apenas para o óleo). Esta leitura optou por tratar o episódio como
material por julgamento analítico, dando sequência ao mesmo critério
aplicado ontem.

**6. A manchete do dia (Farm Progress, 30/07/2026) é de manejo agronômico
("weeding by hand"), sem qualquer conteúdo de preço ou oferta** — ao
contrário das manchetes recentes sobre "safra recorde", hoje não há sinal
editorial adicional para incorporar a esta leitura.

**7. O USDA Crop Progress permanece no corte de 26/07/2026 (11%/52%/7%),
sem atualização nova nesta janela** — o próximo corte semanal é o dado a
acompanhar.

**8. O WASDE permanece completamente fora da janela de 14 dias deste
briefing** — agora 20 dias de atraso desde o último dado (10/07/2026).
Nenhuma pergunta de tese que dependa do WASDE pode ser respondida a partir
deste briefing.

**9. NOPA (fila `release-nopa-2026-07-30`) segue com `monthly_status` em
0,0 bool** — mesma barreira de assinatura paga documentada desde meados de
junho, agora com quase sete semanas sem alternativa de dado primário sobre
o esmagamento americano, apesar de a fila ter sinalizado um "release" novo.

**10. Palma malaia (MPOB) segue sem números extraídos, agora por 21 dias
consecutivos com o mesmo conteúdo exato (3.439 caracteres)** — a
persistência do byte count idêntico segue sugerindo, possivelmente, uma
página que não está mais sendo servida com conteúdo atualizado.

**11. O COT (CFTC) segue no corte de 21/07/2026, uma terça-feira — não
cobre nenhuma das últimas quatro sessões (27/07, 28/07, 29/07 e 30/07)** —
o próximo corte (28/07, publicação normal ~31/07, agora a 1 dia) é o
primeiro capaz de capturar a reação dos fundos aos últimos dias de mercado.

**12. Percentis históricos de COT não calculados** — os números de
21/07/2026 seguem lidos apenas em nível absoluto e como fração do open
interest corrente, sem série histórica completa para calibrar se o
posicionamento estava objetivamente "esticado" no sentido histórico.

**13. Clima INMET (BR) não foi usado como driver de preço desta leitura.**
Julho/agosto é entressafra da soja brasileira (colheita concluída, plantio
só em outubro) — sem relevância direta para a tese de preço neste momento
do calendário agrícola.

**14. BCBA Argentina — nova tentativa de coleta hoje (30/07/2026), depois
de um hiato de 7 dias desde 22/07/2026, mas ainda sem relatórios de
esmagamento/exportação acessíveis via scraper** — o hiato foi preenchido no
dado, mas o conteúdo permanece igualmente inacessível.

**15. RIN D4 como parâmetro fixo (2,11 USD/RIN) segue sendo uma fonte
relevante de incerteza do modelo de biodiesel** — a queda de margem de hoje
(-13,30%) depende inteiramente da combinação heating oil mais barato e óleo
ligeiramente mais barato, não de qualquer mudança no RIN em si.

**16. Os forecasts estatísticos internos (30/07/2026) mantiveram o rótulo
"altista" para as três commodities** — esta leitura não usa esses forecasts
como argumento de tese, apenas como referência de banda estatística; eles
não incorporam o padrão de retest-e-rejeição da soja nem a reversão
cambial documentados nesta leitura.

**17. O prêmio de exportação em Paranaguá (+10,85% sobre a paridade
teórica) é o maior desta janela observada, agora pela terceira sessão
seguida em expansão, mas esta leitura ainda não tem como determinar se
reflete demanda física genuinamente mais firme ou um atraso na atualização
do preço CEPEA/ESALQ frente ao papel e ao câmbio** — as duas hipóteses têm
implicações opostas para a tese de soja e só serão distinguíveis com
atualizações futuras.

*Nenhum número foi inventado ou estimado além do que consta no briefing de
30/07/2026 e nos insights anteriores referenciados. A contribuição central
desta leitura foi (1) identificar o padrão técnico de retest-e-rejeição na
soja em torno do nível de 1.180,00, tratando-o como reforço, e não
enfraquecimento, da tese de rompimento aberta ontem; (2) documentar que o
gatilho tático do ratio Far/Soj (<80%) segue sem confirmação robusta pela
quarta sessão seguida, recomendando uma recalibração de expectativa sobre
sua velocidade de confirmação; (3) decompor o mecanismo pelo qual a
reversão da margem de biodiesel hoje (-13,30%) é inteiramente uma história
de heating oil, não de deterioração da demanda por óleo de soja; (4)
confirmar, com um caso concreto de revisão (70→20.424 contratos, quase
292x), a suspeita levantada nas últimas três leituras sobre a
confiabilidade dos dados de volume de heating oil, estendendo a mesma
cautela agora também ao preço; e (5) registrar a proximidade máxima (1 dia)
de dois catalisadores concretos e simultâneos — o vencimento da isenção
PIS/Cofins do biodiesel e a publicação do próximo corte de COT — como o
ponto de maior tensão informacional de toda esta janela observada.*
