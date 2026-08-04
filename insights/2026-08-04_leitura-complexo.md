---
data: 2026-08-04
titulo: "Give-back generalizado: as três pernas fazem máxima nova e fecham perto da mínima do dia, apagando a reversão de ontem — mesmo com uma manchete que finalmente dá tonelagem à compra chinesa (1 milhão de t, segundo o g1) e outra manchete fresca de hoje repetindo 'China buys soybeans'; o ratio Far/Soj foge da zona <80% (80,97%) no dia em que o D+7 completa 47 dias vencido, e o óleo fecha abaixo do suporte 72,00 pela segunda sessão seguida"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT (ZSU26 soja / ZMU26 farelo / ZLU26 óleo) — sessão de 2026-08-04, com abertura/máxima/mínima/fechamento/volume próprios por commodity (a mais líquida hoje foi o óleo, 30.946 contratos, seguida da soja com 24.468 e do farelo com 20.335)
  - CME NYMEX heating oil (HO=F) — 2026-08-04, fechamento 3,7347 USD/galão, volume de 48 contratos — ainda tratado com cautela, ver Óleo e Honestidade
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, paridade BR, Índice de Sobra de Farelo, Índice de Suporte do Óleo) — recalculados com o fechamento de 2026-08-04
  - BCB PTAX — 2026-08-04 (USD/BRL 5,1053, EUR/BRL 5,8849, Selic diária 0,052531% a.a.)
  - CEPEA/ESALQ Soja Paranaguá via NAG — último carimbo 2026-08-03 (R$ 144,04/saca), sem atualização nova em 2026-08-04 (ver Honestidade)
  - CEPEA/ESALQ Soja Paraná interior via NAG — último carimbo 2026-08-03 (R$ 136,66/saca), sem atualização nova em 2026-08-04
  - NAG Físico BR — 2026-08-04 (farelo MT/IMEA R$ 1.675,10/ton; Rondonópolis R$ 1.700,00/ton; RS R$ 1.640,00/ton, os três com var 0,0% pelo 2º dia seguido); prêmios export PGUA farelo e óleo sem carimbo novo hoje, último em 2026-08-03 (farelo +0,05 USD/sht; óleo +0,08 cts/lb, "mês Agosto/26")
  - CFTC COT Managed Money — corte de 2026-07-28 (sem corte novo nesta janela; o próximo, referente a 2026-08-04, só sai por volta de 2026-08-07)
  - USDA Crop Progress — corte rotulado 2026-08-02 ainda com os MESMOS valores do corte de 2026-07-26 (11% excelente / 52% boa / 7% ruim) pelo 2º dump seguido — ver Honestidade
  - USDA WASDE — ausente da janela, agora 25 dias de atraso desde o último dado (2026-07-10)
  - NOPA — fila `release-nopa-2026-08-04`, `monthly_status` continua em 0,0 bool (paywall)
  - ABIOVE projeções mensais — balanços ago-dez/2026, sem alteração frente ao dump anterior
  - NOAA CPC ENSO — 2026-08-04 (El Niño Advisory, inalterado)
  - MPOB — 2026-08-04 (mesmo conteúdo de 3.439 caracteres, parser sem números extraídos)
  - BCBA Argentina — 2026-08-04 (acessível, sem links de relatório detectados, mesmo padrão de sessões recentes)
  - Notícias Agrícolas/Farm Progress/g1/Canal Rural RSS — 2026-08-04 (160 itens lidos, 8 mantidos; manchete "USDA Exports: China buys soybeans, Aug. 4, 2026", farmprogress.com/marketing/flash-sales, sem corpo de texto extraído) e manchete datada 2026-08-03 presente neste dump "China compra 1 milhão de toneladas de soja americana e amplia disputa entre Brasil e EUA pelo mercado chinês" (g1.globo.com/economia/agronegocios/noticia/2026/08/03/china-soja-eua.ghtml) — ver Honestidade sobre a origem desta última
  - system/tributario_watch.toml (lido como referência, não editado) — `atualizado_em` 2026-06-05, agora 60 dias sem atualização; evento `PISCOFINS-BIODIESEL-ISENCAO` com `vigencia_ate` 2026-07-31, hoje é o 2º dia útil de expediente público desde o vencimento
  - Cruza com [[2026-08-03_leitura-complexo]], [[2026-08-02_leitura-complexo]], [[2026-08-01_leitura-complexo]] e [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (tese original do D+7, tratada abaixo)
status: ativa
vies: [bear-soja, neutral-farelo, bear-oleo_soja]
---

## Visão geral

O complexo soja é, mecanicamente, uma fábrica com uma única matéria-prima (a
soja em grão) e dois produtos de saída em proporção fixa por bushel esmagado:
o **farelo** (a fração proteica, ~78% da massa, vira ração animal) e o **óleo
degomado** (a fração de gordura, ~18-20% da massa, vira óleo de cozinha e
biodiesel). Quem decide o ritmo de esmagamento é a esmagadora, olhando dois
números: a **crush margin** (o valor de farelo + óleo por bushel, menos o
custo daquele bushel de soja, todos medidos na CBOT — Chicago Board of Trade,
a bolsa de referência mundial para esses três contratos) e o **oil share** (a
fração desse valor capturada especificamente pelo óleo). Quando o oil share
sobe, o óleo "manda" no crush — a esmagadora esmaga pela margem do óleo e
aceita vender o farelo mais barato, porque o farelo virou, na prática, o
subproduto que sobra. O **ratio Far/Soj** (preço do farelo dividido pelo
preço da soja, normalizado pela conversão bushel↔short ton) mede a mesma
dinâmica por outro ângulo: abaixo de 80% o farelo está historicamente
"abundante" frente à soja — zona baixista para o farelo —, acima de 87% está
"apertado" — zona altista —, e entre os dois fica a zona neutra de
mean-reversion (o preço tende a voltar pro meio quando se afasta demais de um
extremo).

**Hoje, 2026-08-04, terça-feira, foi o espelho invertido de ontem.** Na
sessão de 2026-08-03 as três pernas haviam revertido de mínimas novas para
fechamentos perto da máxima do dia — o movimento de preço mais forte desta
série de leituras em várias semanas. Hoje o roteiro se repetiu ao contrário:
as três pernas **abriram perto do fechamento de ontem, fizeram uma máxima
nova acima da máxima de ontem — testando resistência — e então venderam com
força para fechar perto da mínima do dia**, devolvendo a maior parte do
ganho de ontem. A soja fechou em **1.158,25 cts/bushel** (CBOT, ticker
ZSU26.CBT, 2026-08-04), **-1,34%** frente ao fechamento de ontem (1.174,00),
com a máxima do dia (1.177,00) testando de novo — e de novo falhando em
romper — a resistência de 1.180,00 identificada nas leituras anteriores; o
fechamento ficou a apenas **24,2% do range do dia** ((1.158,25-1.152,25)÷
(1.177,00-1.152,25)), um candle de reversão bearish quase simétrico ao de
ontem. O farelo fechou em **312,60 USD/short ton**, **-0,86%**, também a
24,0% do range. O óleo fechou em **68,06 cts/lb**, **-1,05%**, a 20,2% do
range, depois de tocar uma máxima de 69,48 (acima da máxima de ontem, 68,88)
e devolver quase tudo — segue **abaixo do suporte técnico de 72,00**, agora
pela segunda sessão de fechamento consecutiva (trata
`alerta-quebra_suporte-oleo_cbot-2026-08-04`, fila de hoje). **O que torna
este dia genuinamente interessante é a divergência entre notícia e preço.**
O RSS de hoje trouxe uma manchete fresca, "USDA Exports: China buys
soybeans, Aug. 4, 2026" (Farm Progress, 04/08/2026) — desta vez atribuindo a
compra diretamente à China, sem a ambiguidade de "unknown buyer" de ontem.
E, neste mesmo dump, aparece uma manchete datada de ontem que não havia sido
incorporada na leitura anterior, do g1: "China compra 1 milhão de toneladas
de soja americana e amplia disputa entre Brasil e EUA pelo mercado chinês"
(g1.globo.com, 03/08/2026) — a primeira vez nesta série que uma manchete traz
**tonelagem explícita** para a compra chinesa. Em teoria, duas manchetes
seguidas confirmando demanda chinesa deveriam sustentar preço. Na prática, o
preço caiu nas três pernas hoje, com reversão técnica clara. **Leitura de
uma linha:** o pivô do complexo hoje é a falha da soja (e, por arrasto, de
farelo e óleo) em romper a resistência técnica mesmo diante de manchetes de
demanda cada vez mais explícitas — ou o mercado já havia precificado a
compra chinesa na alta de ontem ("sell the news"), ou a tonelagem/contraparte
de hoje ainda não está confirmada o suficiente para sustentar preço; maior
convicção desta leitura é que o padrão técnico (máxima nova + fechamento
perto da mínima, nas três pernas) é o dado mais confiável do dia; confiança
moderada — alta para os fechamentos e volumes (normais nas três pernas),
baixa para interpretar por que a notícia não sustentou o preço, e baixa
também para a origem exata da manchete do g1 (ver Honestidade).

---

## Soja

**Viés: bear tático — falha na segunda tentativa seguida de romper 1.180,00,
fechamento a apenas 24,2% do range do dia, devolvendo quase todo o ganho de
ontem, mesmo com manchetes de compra chinesa mais explícitas do que em
qualquer sessão recente.** Fechamento: 1.158,25 cts/bushel (CBOT, ticker
ZSU26.CBT, 2026-08-04).

### O que sustenta a tese

**A sessão testou a resistência e reverteu com a mesma força da reversão de
ontem, só que na direção oposta.** Abertura 1.174,50 (praticamente no
fechamento de ontem), máxima **1.177,00** (abaixo, por pouco, dos 1.180,00
identificados como resistência desde leituras anteriores, e abaixo até da
máxima de ontem, 1.177,00 — na prática, a mesma máxima repetida, sem
progresso), mínima 1.152,25, fechamento **1.158,25**. A posição do
fechamento no range (24,2%) é o espelho quase exato da posição de ontem
(83,8%), o que reforça a leitura de "dia de give-back": o mercado testou o
mesmo nível de cima, não conseguiu romper, e vendeu de volta praticamente
tudo. O volume de 24.468 contratos é normal, na mesma faixa do volume de
ontem (23.488) — não há sinal de liquidez anômala nem de um movimento
"fino" por baixa participação.

**A manchete de hoje é mais direta que a de ontem, mas ainda sem tonelagem
própria.** "USDA Exports: China buys soybeans, Aug. 4, 2026" (Farm Progress,
via RSS, 04/08/2026) — o título já não usa "unknown buyer": atribui a compra
diretamente à China. **Mecanismo:** como discutido na leitura de ontem, o
sistema de flash sales do USDA só dispara quando uma venda isolada ultrapassa
100 mil toneladas métricas para um destino único num único dia — é, por
desenho, sinal de demanda concentrada. Uma segunda manchete do gênero em dois
dias seguidos, agora nomeando China explicitamente, é um padrão que reforça
(não contradiz) a tese de que a demanda chinesa por soja americana está
voltando de forma mais consistente, não como evento isolado. **Mas o preço
não acompanhou**: se o mercado estivesse precificando a notícia de hoje como
fato novo e relevante, seria de esperar sustentação acima da abertura, não
uma reversão de -1,34% fechando perto da mínima. A leitura mais honesta é
que o mercado tratou a notícia de hoje como continuidade do que já havia
precificado ontem, e não como gatilho incremental — ou está aguardando
confirmação de tonelagem antes de reagir de novo (ver Honestidade sobre a
manchete do g1).

**Câmbio pesou contra a paridade em reais hoje, na direção oposta de
ontem.** USD/BRL PTAX fechou em **5,1053** (BCB, 2026-08-04), **+0,65%**
frente a ontem (5,0723) — o real desvalorizou, o que em tese favoreceria a
paridade em reais, mas o efeito foi ofuscado pela queda do CBOT: a paridade
teórica em reais caiu para **R$ 130,36/saca** (indicators, CBOT 1.158,25
cts × USD/BRL 5,1053), **-0,68%** sobre ontem (131,25) — a queda de -1,34%
no CBOT superou a alta de +0,65% no câmbio. Do lado físico, não há dado
novo hoje: a última leitura de CEPEA/ESALQ Soja Paranaguá (via NAG) segue
travada em **R$ 144,04/saca** (carimbo de 2026-08-03, sem atualização em
2026-08-04 neste dump) e a Soja Paraná interior segue em R$ 136,66/saca
(mesmo carimbo). Usando essa última leitura física contra a paridade de
hoje — uma comparação entre dias diferentes, tratada aqui com a ressalva
explícita de que não é apples-to-apples —, o prêmio aparente sobe para
**+10,49%** ((144,04-130,36)÷130,36), ante +9,72% de ontem; mas como o
numerador (físico) está congelado e não foi recalculado hoje, esse número
não deve ser lido como "o prêmio subiu hoje", apenas como reflexo aritmético
da queda do papel sem uma leitura física correspondente (ver Honestidade).

**O posicionamento do COT (CFTC, corte de 28/07/2026) segue sendo o retrato
mais recente — nenhum corte novo hoje.** O managed money net long em soja
estava em 160.479 contratos (15,73% do open interest de 1.020.108), após uma
alta de +22,97% na semana anterior ao corte (de 130.505 em 21/07, 12,49% do
OI então), construída num período em que o preço rondava o topo recente
(fechamento de 28/07: 1.204,75). Entre esse fechamento e o fechamento de
hoje (1.158,25), a soja caiu **-3,86%** — a reversão de ontem havia reduzido
essa distância para -2,55%, mas a devolução de hoje a levou de volta a quase
o mesmo patamar de dor de duas sessões atrás. Ou seja: **o give-back de hoje
não é apenas um detalhe técnico — ele apaga o alívio que a posição comprada
esticada do COT havia ganhado ontem**, mantendo o risco de liquidação
forçada latente até o próximo corte (referente a 04/08, publicado por volta
de 07/08).

### O que invalida / risco para a soja

- **A manchete de hoje ("China buys soybeans") ganhar tonelagem e
  confirmação USDA-FAS explícitas** — se vier volume grande e novo (não
  apenas continuidade do 1 milhão de toneladas já noticiado para 03/08), o
  padrão de "notícia boa, preço caindo" perderia força como argumento bear.
- **Um fechamento acima de 1.180,00** — romperia finalmente a resistência
  testada (e não rompida) em duas sessões seguidas (ontem 1.177,00, hoje
  1.177,00).
- **O câmbio reverter para um real mais forte** justamente quando o CBOT
  também cai — combinação que aprofundaria a queda da paridade em reais.
- **A posição comprada do COT de 28/07 (15,73% do OI) se desmontar de forma
  desordenada** — o give-back de hoje reaproxima o preço do nível em que
  essa posição estava sob maior pressão.
- **O físico de exportação (Paranaguá) recuar quando finalmente atualizar**,
  na direção do papel — confirmaria que o prêmio de +10,49% calculado hoje é
  só um artefato de dados desatualizados, não um sinal real de aperto físico.

### Leitura operacional — soja

Para quem opera os dois lados: o padrão de hoje — máxima repetida sem
progresso, fechamento perto da mínima — é o tipo de candle que
tecnicamente justifica manter ou reforçar posição vendida tática, com stop
lógico acima de 1.180,00 (a resistência que sobreviveu a duas tentativas
seguidas). Para quem está comprado desde a reversão de ontem, o rompimento
da mínima de hoje (1.152,25) é o nível que confirmaria a falha do rali e
justificaria reduzir exposição. Para quem considera nova posição comprada,
a recomendação desta leitura é a mesma de ontem, reforçada: **checar o
relatório diário de exportação do USDA-FAS (flash sales) antes de aumentar
exposição** — duas manchetes seguidas sem tonelagem própria (a de hoje) ou
com tonelagem de fonte secundária não-USDA (a de ontem, via g1) não
substituem a confirmação oficial.

---

## Farelo

**Viés: neutro — preço caiu de forma modesta (-0,86%), mas o ratio Far/Soj
se afastou da zona <80% pela primeira vez em várias sessões, no dia em que o
D+7 completa 47 dias vencido.** Trata
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` (fila de
hoje) e `release-nopa-2026-08-04` (fila de hoje, mesmo bloqueio de sempre,
ver abaixo). Fechamento: 312,60 USD/short ton (CBOT, ticker ZMU26.CBT,
2026-08-04).

### O D+7 chega a 47 dias vencido — e hoje o ratio se afasta, não se aproxima

A tese original ([[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]])
apostava que a compressão rápida do ratio em junho levaria à zona comprimida
(<80%) "em 1-2 semanas". O checkpoint formal caiu em 18/06/2026; hoje,
04/08/2026, são **47 dias corridos** sem confirmação. Ontem o ratio havia
chegado ao ponto mais próximo do piso em várias sessões (80,57%). **Hoje ele
subiu para 80,97%** (indicators, 2026-08-04), uma alta de **+0,36 ponto
percentual**, o maior afastamento da zona <80% em vários dias.
**Mecanismo:** o ratio é farelo dividido por soja (normalizado); como a soja
caiu mais em termos percentuais hoje (-1,34%) do que o farelo (-0,86%), o
denominador encolheu mais rápido que o numerador, e o ratio sobe mesmo com
o farelo também em queda absoluta. Isso é o oposto do que ontem sustentava a
tese: ontem a soja subia mais que o farelo (puxando o ratio para baixo,
"reforçando" a leitura estrutural); hoje a soja cai mais que o farelo
(puxando o ratio para cima, "atrasando" a leitura estrutural). Em nenhum dos
dois dias o movimento do ratio foi genuinamente originado por uma mudança de
oferta/demanda de farelo — em ambos, quem mandou foi a soja. O próximo marco
formal continua sendo o D+90 (2026-09-09, a 36 dias de hoje).

### O que sustenta a leitura de hoje

**Crush margin subiu de leve, mesmo com as três pernas em queda — a margem
da esmagadora não sofreu com o give-back de hoje.** Crush margin de
**2,7813 USD/bushel** (farelo 312,60 + óleo 68,06 − soja 1.158,25),
**+0,47%** sobre ontem (2,7682) — segue folgada frente ao nível de alerta
histórico (<2,50 USD/bu). **Mecanismo:** como a soja (o custo) caiu mais em
termos absolutos por bushel do que farelo e óleo somados (a receita)
caíram, a margem da esmagadora efetivamente melhorou num dia de preços mais
baixos — um lembrete de que "queda de preço" e "queda de margem de crush"
não são a mesma coisa.

**O oil-meal spread recuou -2,98%, de 0,6281 para 0,6094 USD/bushel** — a
esmagadora capturou um pouco menos de vantagem relativa do óleo sobre o
farelo hoje, revertendo parte do salto de +33,64% de ontem. O oil share
seguiu praticamente estável, **52,12% hoje vs 52,17% ontem (-0,05pp)** —
sinal de que, apesar do vaivém técnico das últimas duas sessões, a divisão
de valor dentro do crush entre óleo e farelo não mudou de forma
significativa.

**As praças físicas de farelo no Brasil (NAG) seguem completamente
travadas, agora pelo segundo dia seguido.** Mato Grosso/IMEA em R$
1.675,10/ton, Rondonópolis/MT em R$ 1.700,00/ton e RS em R$ 1.640,00/ton —
todas com var 0,0% hoje, repetindo exatamente os valores de ontem. Os
prêmios de exportação em Paranaguá (farelo e óleo) não trouxeram carimbo
novo hoje — a última leitura permanece em 2026-08-03 (+0,05 USD/short ton
farelo, +0,08 cts/lb óleo). **Mecanismo e leitura:** quanto mais tempo essas
referências físicas ficam paradas enquanto o papel (CBOT) se move em ambas
as direções, maior a distância acumulada entre preço físico e o que o papel
"deveria" implicar — esse represamento tende a se resolver com um salto
quando a liquidez normalizar, não com uma caminhada suave (ver riscos).

**O Índice de Sobra de Farelo (ISF) permanece em 80/100 (4 de 5 condições
estruturais)**, inalterado. As projeções ABIOVE seguem mostrando a
exportação de farelo brasileiro caindo de 1.400 mil toneladas em agosto/2026
para 700 mil toneladas em dezembro/2026, uma queda de -50% em quatro meses
(ABIOVE projeções mensais, sem alteração frente ao dump anterior) — o driver
estrutural mais lento e mais persistente desta tese, à margem do ruído
tático do ratio.

**`release-nopa-2026-08-04` (fila de hoje) sinaliza novo carimbo, mas o
`monthly_status` permanece em 0,0 bool** — mesma barreira de assinatura paga
documentada desde meados de junho, agora sem alternativa de dado primário
sobre o crush americano há mais de 8 semanas. Tratado como item da fila
resolvido (sem conteúdo novo para incorporar), não como pendência de
leitura.

### O que invalida / risco para o farelo

- **O ratio Far/Soj continuar se afastando de 80%** em vez de convergir —
  cada dia que passa sem confirmação, mais a tese tática original (D+7)
  perde relevância frente ao marco formal seguinte (D+90, 09/09).
- **As manchetes de demanda chinesa de soja se intensificarem**, puxando o
  numerador do ratio (soja) para cima de forma mais estrutural — isso
  comprimiria o ratio pelo lado "errado" outra vez, mascarando se o farelo
  em si está ou não sobrando.
- **As praças físicas travadas (MT/IMEA, Rondonópolis, RS) se moverem de
  forma abrupta** quando a liquidez normalizar, depois de dois dias
  seguidos sem qualquer variação.
- **O prêmio de exportação em Paranaguá sair de zero** depois de mais de um
  mês parado.

### Leitura operacional — farelo

Para quem monitora o ratio Far/Soj como gatilho tático (long farelo/short
soja ou vice-versa na convergência), o movimento de hoje (80,57%→80,97%) é
um passo para trás na tese de compressão — a recomendação desta leitura
segue sendo tratar qualquer aproximação futura de 80% com ceticismo até
sobreviver a mais de uma sessão seguida na mesma direção, dado que nas
últimas duas sessões o ratio se moveu por causa da soja, não do farelo, nos
dois sentidos. Para quem opera o oil-meal spread ou o crush como posição
relativa, a reversão parcial de hoje (-2,98%) depois do salto de ontem
(+33,64%) reforça que esse spread está mais sensível ao vaivém técnico do
óleo do que a qualquer mudança fundamental no farelo — não é, por si só, um
sinal de entrada nova.

---

## Óleo

**Viés: bear tático — segunda máxima maior que a anterior seguida de
reversão para fechamento perto da mínima, mantendo o fechamento abaixo do
suporte 72,00 pela segunda sessão seguida, com a margem de biodiesel ainda
calculada sobre um heating oil de liquidez muito abaixo do normal.** Trata
`alerta-quebra_suporte-oleo_cbot-2026-08-04` (fato: 68,06 vs nível 72,00).
Fechamento: 68,06 cts/lb (CBOT, ticker ZLU26.CBT, 2026-08-04).

### O que sustenta a tese (e a contradição que persiste)

**O óleo tentou romper mais alto do que ontem e falhou com ainda mais
força.** Abertura 68,81, máxima **69,48** (acima da máxima de ontem, 68,88 —
um progresso real, ao contrário da soja, que repetiu a mesma máxima),
mínima 67,70, fechamento **68,06** — um candle que abre perto do topo,
sobe, e devolve quase tudo, fechando a apenas 20,2% do range do dia. O
volume de 30.946 contratos é saudável e o mais alto dos três legs hoje,
dando peso ao movimento. Em nível, **68,06 está -5,47% abaixo do suporte
técnico de 72,00** que a fila de julgamento monitora desde 31/07 — a
distância aumentou frente a ontem (-4,47%), porque o preço caiu mais do que
o suporte se moveu (ele não se move; é um nível fixo).

**A margem de biodiesel americana caiu de novo, mas o heating oil segue com
volume muito abaixo do que se considera confiável nesta série.** O custo
(lado óleo) caiu para **5,1045 USD/galão** (-1,06%, acompanhando o óleo mais
barato). A receita caiu para **6,8997 USD/galão** (-2,02%), porque o
heating oil (HO=F) fechou em **3,7347 USD/galão**, -3,51% sobre o
fechamento de ontem (3,8704) — mas com apenas **48 contratos negociados**.
É quase o dobro do volume de ontem (26 contratos), mas ainda uma fração do
que séries anteriores já qualificaram como anômalo (os 1.010-1.138
contratos do fim de semana de duas semanas atrás já haviam sido tratados
como liquidez baixa demais para confiar). O resultado é a margem de
biodiesel caindo para **0,9952 USD/galão**, **-8,10%** sobre o número já
suspeito de ontem (1,0829). **Esta leitura trata a margem de biodiesel de
hoje como não confirmada pela segunda sessão seguida** — o lado do custo
(óleo, 30.946 contratos) é confiável, o lado da receita (heating oil, 48
contratos) não é. Duas sessões seguidas de heating oil com volume muito
abaixo do normal deixam de ser um evento isolado e passam a ser um padrão
que merece verificação de coleta, não apenas ceticismo pontual (ver
Honestidade).

**O Índice de Suporte do Óleo (ISO) permanece em 100/100 (5 de 5
condições)**, inalterado — a tese estrutural (óleo dominando o valor do
crush) segue formalmente intacta, na mesma linha do que já foi destacado
ontem: o ISO mede quem captura mais valor dentro do crush, não se o preço
está caro ou barato frente a um nível técnico. Hoje as duas leituras (ISO no
máximo, preço fazendo nova máxima intradiária mas fechando perto da mínima,
ainda abaixo do suporte) coexistem sem se contradizer tecnicamente.

**Sem COT novo nesta janela** — o corte de 28/07/2026 segue sendo a
fotografia mais recente, mostrando os fundos reduzindo o net long em óleo
em -10,27% na semana anterior ao corte (de 120.246 em 21/07, 18,17% do OI,
para 107.898 em 28/07, 16,60% do OI) — a única das três pernas em que o
book especulativo reduziu exposição comprada na semana que antecedeu o
corte, ao contrário do padrão de reforço visto em soja e farelo. Isso ajuda
a explicar por que o óleo tem mostrado o desenho técnico mais volátil das
três pernas nestas duas últimas sessões: com menos posição comprada
"presa", o espaço para movimentos rápidos em ambas as direções (rali de
ontem, give-back de hoje) é maior.

### O que invalida / risco para o óleo

- **O heating oil confirmar amanhã, com volume genuinamente normal (não
  apenas "menos anômalo"), um nível consistente com o de hoje** —
  validaria a compressão da margem de biodiesel como sinal real pela
  primeira vez em duas sessões.
- **Dois dias seguidos de heating oil com volume muito baixo (26, depois 48
  contratos) se revelarem um problema de coleta de dados**, não um padrão
  real de mercado — nesse caso, toda a série recente de margem de
  biodiesel precisaria ser reavaliada, não só o número de hoje.
- **Um fechamento consistente de volta abaixo de 67,70 (mínima de hoje)** —
  aprofundaria a sequência de quebra técnica.
- **A isenção PIS/Cofins do biodiesel seguir sem renovação** — hoje é o 2º
  dia útil desde o vencimento (31/07), ainda sem confirmação (ver Lente
  fiscal).
- **O oil share continuar estável (52,12% hoje) sem tradução em alta
  sustentada de preço** — mantém a tese estrutural sem validar a tese de
  preço, pelo segundo dia seguido.

### Leitura operacional — óleo

Para quem entrou comprado na reversão de ontem, o padrão de hoje —
máxima mais alta, fechamento perto da mínima, abaixo do suporte — é sinal
técnico de reduzir ou proteger a posição, com stop natural abaixo da
mínima de hoje (67,70). Para quem está vendido, a resistência de 69,48
(máxima de hoje) é o nível de referência para adicionar, já que o rompimento
de 72,00 segue distante e a margem de biodiesel — pilar fundamental que
sustentaria uma alta mais duradoura — segue sem confirmação por falta de
liquidez no heating oil. A recomendação mais concreta é a mesma de ontem,
reforçada: **não tratar a margem de biodiesel calculada nestas duas últimas
sessões (1,0769 e 0,9952) como números definitivos até o heating oil
negociar com volume claramente normal.**

---

## Spreads e crush (leitura de complexo)

**Ratio Far/Soj: 80,97% (04/08), alta de +0,36pp sobre ontem — o maior
afastamento da zona <80% em várias sessões, no dia em que o D+7 formal
completa 47 dias vencido.** O movimento de hoje é tecnicamente na direção
errada para a tese estrutural bear do farelo (mais longe do piso), assim
como o de ontem foi na direção certa — em ambos os casos o "motor" foi a
soja, não o farelo. Isso reforça o ponto operacional central desta leitura:
o ratio, nas últimas duas sessões, tem se movido por causa do numerador
errado, o que reduz a confiabilidade de usá-lo como gatilho tático de curto
prazo até que ele se mova de forma consistente por várias sessões seguidas.

**Crush margin: 2,7813 USD/bu, +0,47% sobre ontem — segue folgada acima do
nível de alerta (<2,50 USD/bu), e de forma notável, melhorou num dia em que
as três pernas caíram de preço.** A esmagadora tem hoje ainda mais espaço de
manobra, porque a soja (custo) caiu proporcionalmente mais que farelo+óleo
(receita).

**Oil share: 52,12%, -0,05pp sobre ontem — praticamente estável.** Depois de
duas sessões de forte movimento técnico no óleo (rali de +2,26% ontem,
give-back de -1,05% hoje), a fatia de valor que o óleo captura dentro do
crush mal se mexeu — sinal de que o vaivém de preço destas duas sessões foi
mais técnico/direcional do que uma mudança real na relação de valor entre
as duas pernas do crush.

**Oil-meal spread: 0,6094 USD/bu, -2,98% no dia — reverteu parte do salto de
ontem (+33,64%)**, também consistente com um movimento predominantemente
técnico e de curto prazo, não uma mudança na dinâmica estrutural
óleo-domina-o-crush.

**Heating oil: fechamento de 3,7347 (-3,51%) com volume de 48 contratos —
ainda tratado como não confiável, agora pelo segundo dia seguido.** Esta é
a mesma fricção de ontem, mais persistente: a leitura técnica das três
pernas principais (soja, farelo, óleo — todas com volume normal) é sólida;
a leitura fundamental que depende do heating oil (margem de biodiesel) não
é, porque o dado que a sustenta segue com liquidez anômala.

**ISF em 80/100, ISO em 100/100 — ambos inalterados pelo quarto dia
seguido.** Nenhum insumo estrutural novo (ABIOVE, condições de crush)
entrou no cálculo hoje.

**O que os índices dizem juntos hoje:** o complexo teve, na sessão de hoje,
o give-back quase espelhado do movimento de ontem — as três pernas testaram
níveis técnicos mais altos e reverteram para fechar perto da mínima, num
padrão coordenado que sugere um driver comum (provável realização de lucro
após o rali de ontem, ou simplesmente falha técnica na mesma resistência),
não um evento específico de crush. As métricas estruturais (ISF, ISO,
ABIOVE, oil share) seguem, como ontem, inalteradas — elas capturam
dinâmicas de mais longo prazo que duas sessões de vaivém técnico não
alteram. A leitura mais honesta é que o complexo está, nestas duas últimas
sessões, mais movido por técnica de curto prazo (testes de resistência,
give-back) do que por qualquer mudança fundamental — o que torna a
confirmação de tonelagem da manchete chinesa (ver Soja e Honestidade) o
elemento mais capaz de alterar esse quadro nos próximos dias.

---

## Lente fiscal e regulatória BR

**Isenção PIS/Cofins do biodiesel (`PISCOFINS-BIODIESEL-ISENCAO`,
`vigencia_ate` 2026-07-31) — hoje, 2026-08-04, é o 2º dia útil de
expediente público desde o vencimento.** O RSS de hoje trouxe 8 itens
mantidos, nenhum sobre este tema específico — mesma lacuna de ontem.
**Mecanismo e leitura, sem mudança frente a ontem:** se a isenção caducou
sem renovação, o custo de produção do biodiesel brasileiro sobe, reduzindo
a competitividade do biodiesel dentro do mix mandatório e pressionando a
demanda de óleo de soja como insumo doméstico — vetor bearish direto para
o óleo. Com o monitor tributário (`system/tributario_watch.toml`) parado
desde 2026-06-05 (**60 dias sem atualização**), esta leitura segue sem
poder confirmar nem descartar a caducidade — mantém-se como o item de
verificação manual mais urgente desta janela, agora há dois dias.

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L) —
vigência formal venceu há 24 dias** (`vigencia_ate` 11/07/2026), sem
qualquer atualização de status no monitor.

**MP 1.363/2026 — subsídio ao diesel fóssil (R$ 1,12/L), em vigor até
31/12/2026, sem alteração.** Bearish estrutural persistente: enquanto o
diesel fóssil segue subsidiado no mix B15, o biodiesel via óleo de soja
compete em desvantagem — reforçado se a isenção PIS/Cofins também tiver
caducado.

**B16 — sem data, travado em B15, sem mudança de status.** Cada +1pp de
mistura obrigatória de biodiesel puxaria demanda adicional de óleo de soja
para o mercado interno (~+436 mil toneladas no B16 pleno), mas o CNPE segue
sem nova convocação.

**STJ REsp 2.165.276/2026 — crédito PIS/Cofins para esmagadoras sobre soja
usada em biodiesel, sem alteração.** Bullish para soja/óleo (alívio de
custo de entrada), mas ainda não vinculante (não é decisão repetitiva).

**Vetores dos EUA e Indonésia, sem mudança de status desde 2026-06-05:**
EPA-RFS-2026-2027 (volumes recordes de biocombustível, sustentando o RIN D4
fixo em 2,11 USD/RIN usado na margem de biodiesel); 45Z-CLEAN-FUEL (regra
que favoreceria óleo de soja doméstico americano frente a insumo importado);
DANANTARA-INDONÉSIA (centralização estatal da exportação de palma, plena em
01/09/2026, agora a 28 dias); INDONESIA-B50 (provável B45 em 2026, B50
pleno só 2027-28); INDONESIA-LEVY-PMK9 (imposto de exportação de CPO até
12,5%, encarecendo palma). Conjunto estruturalmente bullish para óleo de
soja via substituição de palma, mas inverificável pelo lado de mercado
(MPOB inacessível, ver Honestidade).

**O monitor tributário como um todo está há 60 dias sem qualquer
atualização** — prioridade de manutenção do sistema, especialmente relevante
agora que a isenção PIS/Cofins completa dois dias úteis vencida sem
confirmação de status.

---

## Riscos e eventos próximos

**As duas manchetes de compra chinesa (a de hoje, "China buys soybeans",
sem tonelagem própria, e a de ontem, "1 milhão de toneladas" via g1) ainda
precisam de confirmação oficial USDA-FAS** — a divergência entre notícia
crescentemente bullish e preço caindo é o ponto mais importante a monitorar
nos próximos dias.

**O heating oil precisa negociar com volume claramente normal** — duas
sessões seguidas de liquidez muito baixa (26, depois 48 contratos) tornam
a margem de biodiesel não confirmável desde 2026-08-03.

**A isenção PIS/Cofins do biodiesel segue sem confirmação de status**, agora
no 2º dia útil desde o vencimento (31/07) — item de verificação manual mais
urgente desta janela.

**O ratio Far/Soj subiu para 80,97%, o mais longe da zona <80% em várias
sessões, com o D+7 formal vencido há 47 dias** — monitorar se o movimento
de hoje é o início de um afastamento mais duradouro ou apenas o reflexo da
queda pontual da soja.

**O suporte técnico do óleo (72,00) segue rompido, agora a -5,47%, testado
de cima para baixo hoje (máxima 69,48) sem conseguir se firmar acima dele**
— a reabertura de amanhã é o próximo teste de continuidade da quebra
técnica.

**O próximo corte do COT (referente a 04/08/2026) só é publicado por volta
de 07/08/2026** — até lá, sem novo dado de posicionamento para testar como
os fundos reagiram ao rali de 03/08 e ao give-back de hoje.

**O USDA Crop Progress rotulado 2026-08-02 trouxe, pelo segundo dump
seguido, os MESMOS valores do corte de 26/07** (ver Honestidade); o corte
real da semana que termina em 02/08 costuma ser publicado na segunda-feira
à tarde (horário dos EUA) — já deveria ter atualizado; monitorar no próximo
dump se o valor muda ou se a duplicação persiste por um terceiro dia,
sinalizando problema de coleta.

**NOPA — fila `release-nopa-2026-08-04` sinaliza novo "release", mas o dado
segue inacessível**, agora mais de 8 semanas sem alternativa de dado
primário sobre o crush americano.

**MPOB — sem números de palma extraídos, mesma barreira de longa data.**

**O WASDE segue fora da janela deste briefing, agora 25 dias de atraso**
desde o último dado (10/07/2026).

---

## Honestidade

O que não foi possível validar neste briefing de 2026-08-04, e os pontos
onde a confiança é baixa:

**1. A manchete "China compra 1 milhão de toneladas de soja americana"
(g1.globo.com, datada 2026-08-03) aparece pela primeira vez nesta série de
leituras hoje, mas com carimbo de ontem.** Não está claro se esta manchete
é genuinamente nova (surgiu depois do fechamento do dump de ontem) ou se
já estava disponível ontem e simplesmente não foi selecionada pela
amostragem do briefing (o dump mostra "8 itens mantidos" por dia, mas só
exibe um exemplo por combinação de data/commodity). Esta leitura trata a
tonelagem de 1 milhão de toneladas como um número presente no título da
notícia, com fonte e data, e portanto utilizável — mas não presume que o
mercado já a tinha precificado antes de hoje.

**2. A manchete "USDA Exports: China buys soybeans, Aug. 4, 2026" (Farm
Progress) não veio com corpo de texto, tonelagem ou confirmação USDA-FAS
neste briefing.** É tratada como o segundo dia seguido de manchete
relacionada a flash sale para a China, mas sem informação própria além do
título — a mesma limitação já registrada ontem para a manchete anterior.

**3. O heating oil (HO=F) de 2026-08-04 fechou com 48 contratos de
volume — quase o dobro de ontem (26), mas ainda muito abaixo do que esta
série já qualificou como liquidez normal.** Esta leitura usa o número
calculado de margem de biodiesel (0,9952 USD/galão, -8,10%) porque é o que
o indicador interno gerou a partir do dado disponível, mas sinaliza,
explicitamente, que duas sessões seguidas de baixíssima liquidez no
heating oil tornam esse padrão candidato a problema de coleta de dados, não
apenas ruído pontual — recomenda-se verificação técnica da fonte se o
padrão persistir amanhã.

**4. O ratio Far/Soj (80,97%) segue sem fechar abaixo de 80%, agora 47 dias
depois do checkpoint formal do D+7 (18/06/2026).** Esta leitura não conclui
que a tese original falhou — apenas que ela não se confirmou dentro do
prazo tático original, e mantém o D+90 (2026-09-09) como próximo marco
formal.

**5. O USDA Crop Progress rotulado 2026-08-02 trouxe, pelo segundo dump
seguido, valores idênticos ao corte de 26/07/2026 (11%/52%/7%).** Esta
leitura não trata isso como duas semanas genuinamente estáveis de condição
de lavoura, e reforça a recomendação de reconferir no próximo dump — a
persistência do mesmo valor por dois dumps seguidos aumenta a suspeita de
problema de coleta, não de estabilidade real.

**6. A isenção PIS/Cofins do biodiesel — sem confirmação de renovação ou
caducidade neste briefing, agora no 2º dia útil desde o vencimento.** O
monitor tributário está 60 dias sem atualização; esta leitura não presume
nenhum dos dois cenários.

**7. O prêmio de exportação físico da soja (Paranaguá, Paraná interior) e
os prêmios PGUA de farelo e óleo não trouxeram carimbo novo em
2026-08-04** — todos os cálculos de prêmio desta leitura que usam esses
números partem do último carimbo disponível (2026-08-03), não de uma
leitura do mesmo dia, e são sinalizados como tal no corpo do texto.

**8. O WASDE permanece completamente fora da janela deste briefing** —
agora 25 dias de atraso desde o último dado (10/07/2026).

**9. NOPA (`release-nopa-2026-08-04`) segue com `monthly_status` em 0,0
bool** — mesma barreira de assinatura paga, mais de 8 semanas sem
alternativa de dado primário.

**10. Palma malaia (MPOB) segue sem números extraídos**, mesmo conteúdo de
3.439 caracteres.

**11. O COT (CFTC) de 28/07/2026 segue sendo o dado de posicionamento mais
recente** — nenhum corte novo nesta janela; o próximo sai por volta de
07/08/2026. Percentis históricos de COT não foram calculados (mesma
limitação de leituras anteriores).

**12. Clima INMET (BR) não foi usado como driver de preço** — agosto é
entressafra da soja brasileira, sem relevância direta neste momento do
calendário agrícola.

**13. Os forecasts estatísticos internos (bandas 7d/30d geradas em
2026-08-04) não foram usados como driver desta leitura** — são bandas
MA20+volatilidade+slope, mecânicas (soja 7d "lateral"/30d "altista", farelo
7d/30d "altista", óleo 7d/30d "baixista"), sem incorporar a leitura
qualitativa de hoje (give-back técnico, manchetes de China, heating oil
suspeito); ficam registradas no briefing, mas esta leitura não as toma como
fonte de tese.

*Nenhum número foi inventado ou estimado além do que consta no briefing de
2026-08-04 e nos insights anteriores referenciados. A contribuição central
desta leitura foi (1) identificar e explicar mecanicamente o give-back
generalizado da sessão de hoje, espelho inverso da reversão de ontem; (2)
destacar a divergência entre notícia (cada vez mais explícita sobre compra
chinesa de soja) e preço (queda coordenada nas três pernas) como o ponto
central de atenção; (3) separar a leitura técnica confiável (fechamentos e
volumes de soja/farelo/óleo, todos normais) da leitura fundamental de baixa
confiança (margem de biodiesel calculada sobre heating oil com volume ainda
muito baixo, agora pelo segundo dia seguido); e (4) tratar os três itens da
fila de julgamento de hoje —
`alerta-quebra_suporte-oleo_cbot-2026-08-04`,
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` e
`release-nopa-2026-08-04` — no contexto específico desta sessão, sem
inventar tonelagem, confirmação ou percentil que o briefing não trouxe.*
