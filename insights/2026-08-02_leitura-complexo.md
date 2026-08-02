---
data: 2026-08-02
titulo: "Domingo sem pregão novo (CBOT fechada; grãos sem reabertura Globex captada neste dump) — o único dado genuinamente novo é um print PARCIAL e de volume anômalo do heating oil (3.978→4.0523, apenas 1.010 contratos) sugerindo abertura mais fraca para a semana; enquanto isso, a isenção PIS/Cofins do biodiesel completa o 2º dia corrido vencida sem qualquer sinal de renovação, e o gatilho tático `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` chega a 45 dias sem confirmação — a leitura seguirá dependente da reabertura de segunda-feira (2026-08-03) para qualquer conclusão nova de preço"
tags: [complexo, auto-claude, fim-de-semana, dado-parcial]
fontes:
  - CME CBOT (ZSU26 soja / ZMU26 farelo / ZLU26 óleo) — sem dado novo nesta janela; a última sessão completa disponível segue sendo 2026-07-31 (sexta-feira), já tratada em [[2026-07-31_leitura-complexo]] e revisada em [[2026-08-01_leitura-complexo]]
  - CME NYMEX heating oil (HO=F) — ÚNICO instrumento do briefing com carimbo de 2026-08-02: abertura 3,978, máxima 4,0642, mínima 3,97, fechamento (print) 4,0523 USD/galão, volume 1.010 contratos — tratado como print PARCIAL de reabertura de Globex, não como sessão fechada (ver Honestidade)
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, paridade BR) — nenhum recalculado com data de 2026-08-02; os últimos valores seguem cravados em 2026-07-31 (última sessão completa de soja/farelo/óleo)
  - Índice de Sobra de Farelo e Índice de Suporte do Óleo — reimpressos com carimbo de 2026-08-02, valores inalterados (80/100 e 100/100) frente ao carimbo de 2026-08-01
  - BCB PTAX — última leitura 2026-07-31 (USD/BRL 5,0773, EUR/BRL 5,849, Selic diária 0,052531% a.a.); sem publicação de fim de semana (2026-08-01 e 2026-08-02)
  - CEPEA/ESALQ Soja Paranaguá via NAG — última leitura 2026-07-31 (R$ 144,91/saca)
  - CEPEA/ESALQ Soja Paraná interior via NAG — última leitura 2026-07-31 (R$ 137,27/saca)
  - NAG Físico BR — última leitura 2026-07-31 (farelo MT/IMEA R$ 1.675,10/ton; Rondonópolis R$ 1.700,00/ton; RS R$ 1.640,00/ton; prêmios export PGUA farelo +0,05 USD/sht e óleo +0,08 cts/lb, ambos inalterados há 30 dias corridos desde 2026-07-03)
  - CFTC COT Managed Money — corte de 2026-07-28, sem corte novo (o próximo, referente a 2026-08-04, só sai por volta de 2026-08-07)
  - USDA Crop Progress — corte de 2026-07-26 (11% excelente + 52% boa + 7% ruim), sem publicação de fim de semana; próximo corte esperado por volta de 2026-08-03 (segunda-feira)
  - USDA WASDE — ausente da janela, agora 23 dias de atraso desde o último dado (2026-07-10)
  - NOPA — fila `release-nopa-2026-08-02`, `monthly_status` continua em 0,0 bool (paywall), mesma barreira desde meados de junho, agora ~7 semanas
  - ABIOVE projeções mensais — balanços ago-dez/2026 (farelo/óleo/soja), sem alteração
  - NOAA CPC ENSO — 2026-08-02 (El Niño Advisory, inalterado desde pelo menos 16/07/2026)
  - MPOB — 2026-08-02 (conteúdo idêntico de 3.439 caracteres, parser sem números extraídos, agora o 24º dia consecutivo nesse estado)
  - BCBA Argentina — 2026-08-02 (4ª sessão seguida acessível via scraper — 30/07, 31/07, 01/08, 02/08 —, ainda sem links de relatório detectados)
  - Notícias Agrícolas/Farm Progress/Canal Rural RSS — 2026-08-02 (160 itens lidos, 6 mantidos; SEM manchete específica extraída no dump de hoje, ao contrário de ontem — ver Honestidade)
  - INMET — previsão para 2026-08-03 nas praças monitoradas (Cascavel/PR, Maringá/PR, Passo Fundo/RS, Rio Verde/GO, Cuiabá/MT, Sinop/MT, Sorriso/MT, Lucas do Rio Verde/MT); entressafra da soja brasileira, sem relevância direta de preço nesta época do calendário agrícola
  - Forecasts estatísticos internos — sem geração nova de 2026-08-02 visível no dump (última geração 2026-08-01, spot ref 1.170,75/314,90/67,26, viés "altista" nas três — ver Honestidade)
  - system/tributario_watch.toml (lido apenas como referência, não editado) — `atualizado_em` 2026-06-05, agora 58 dias sem atualização; evento `PISCOFINS-BIODIESEL-ISENCAO` com `vigencia_ate` 2026-07-31, hoje é o 2º dia corrido após o vencimento
  - Cruza com [[2026-08-01_leitura-complexo]] (leitura de ontem, revisão da sessão de sexta) e [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (tese original do D+7, tratada abaixo)
status: ativa
vies: [bear-soja, neutral-farelo, bear-oleo_soja]
---

## Visão geral

O complexo soja funciona como uma fábrica de matéria-prima única com dois
produtos de saída em proporção fixa por bushel esmagado: o **farelo** (a
fração proteica, ~78% da massa, vira ração animal) e o **óleo degomado** (a
fração de gordura, ~18-20% da massa, vira óleo de cozinha e biodiesel). Quem
decide o ritmo de esmagamento é a esmagadora, olhando a **crush margin** (o
valor de farelo + óleo por bushel, menos o custo daquele bushel de soja,
todos medidos na CBOT — Chicago Board of Trade, a bolsa de referência
mundial para esses três contratos) e o **oil share** (a fração desse valor
capturada especificamente pelo óleo). O **ratio Far/Soj** (preço do farelo
dividido pelo preço da soja, normalizado pela conversão bushel↔short ton)
mede o mesmo crush por outro ângulo: abaixo de 80% o farelo está
historicamente "abundante" frente à soja — zona bear —, acima de 87% está
"apertado" — zona bull —, e entre os dois fica a zona neutra de
mean-reversion.

**Hoje, 2026-08-02, é domingo — não houve pregão novo de soja, farelo ou
óleo na CBOT, e este dump não captou nenhuma reabertura de Globex para essas
três pernas.** A última sessão completa disponível para as três continua
sendo sexta-feira, 31/07/2026, já tratada em [[2026-07-31_leitura-complexo]]
e revisada em [[2026-08-01_leitura-complexo]]. A diferença estrutural entre
a leitura de hoje e a de ontem é que **o dump de hoje trouxe um print,
mesmo que parcial, de um quarto instrumento correlato: o heating oil
(HO=F, NYMEX/CME), com carimbo de 2026-08-02** — abertura 3,978, máxima
4,0642, mínima 3,97, fechamento (print no momento da coleta) **4,0523
USD/galão**, com apenas **1.010 contratos** de volume. Esse número, tratado
com cautela extrema por esta leitura (ver Honestidade — o heating oil já
teve revisões de até ~292x em episódios passados desta série), aponta para
uma reabertura de Globex de domingo à noite (horário de Chicago) MAIS FRACA
do que o fechamento revisado de sexta (4,1215): o print atual está **-1,68%**
abaixo desse fechamento ((4,0523-4,1215)÷4,1215). Como o heating oil é a
metade "receita" da margem de biodiesel americana (a outra metade é o RIN
D4, fixo em 2,11 USD/RIN) — e a margem de biodiesel é um dos pilares que
sustentam o óleo de soja via demanda de insumo —, esse print, SE confirmado
amanhã com volume normal, seria um primeiro sinal de que a fraqueza de
energia fóssil que já vinha pressionando a margem (ver
[[2026-08-01_leitura-complexo]]) continua na virada da semana. Mas com
apenas 1.010 contratos negociados — uma fração ainda menor que os 12.325 já
qualificados como anômalos na sexta — **esta leitura não usa esse número
para calcular uma nova margem de biodiesel** (misturaria um preço de óleo
de sexta, congelado, com um preço de heating oil de domingo, parcial — os
indicadores internos não fizeram esse cálculo, e esta leitura não inventa
indicador que o robô não gerou). É tratado apenas como um dado de cor,
direcionalmente bearish para o contraponto fundamentalista do óleo, mas sem
peso de convicção até a reabertura plena de segunda-feira. No pano de
fundo regulatório, a isenção PIS/Cofins do biodiesel completa hoje o
**segundo dia corrido vencida** (venceu sexta, 31/07) sem qualquer sinal de
renovação — mas domingo, assim como sábado, é dia sem expediente público
brasileiro, então o silêncio segue sem poder ser lido como confirmação de
caducidade (ver Lente fiscal). **Leitura de uma linha:** o pivô do complexo
hoje não é preço novo de soja/farelo/óleo — é um print fraco e de baixíssima
liquidez do heating oil, mais dois dias adicionais (agora 45 no total)
sem confirmação do gatilho tático do ratio Far/Soj e dois dias sem sinal
sobre a isenção do biodiesel; maior convicção desta leitura continua sendo
a tese estrutural bear do óleo (ISO 100/100 mede domínio do óleo no valor
do crush, não força de preço — os dois coexistem); confiança baixa para
qualquer leitura tática nova, dado que nenhum dos três contratos principais
tem dado de preço além do já conhecido desde sexta.

---

## Soja

**Viés: bear tático moderado — herdado integralmente de
[[2026-08-01_leitura-complexo]], sem dado novo de preço para testá-lo ou
desafiá-lo.** Fechamento revisado de referência: 1.170,75 cts/bushel (CBOT,
ticker ZSU26.CBT, sessão de 2026-07-31, ainda a mais recente disponível).

### O que sustenta a tese

**Sem pregão novo, a leitura técnica de soja permanece exatamente a
descrita ontem: máximas decrescentes que ainda não tocaram 1.180,00.**
Sequência de máximas diárias: 1.181,25 (30/07) → 1.179,25 (31/07, valor
final revisado) — o nível de 1.180,00 segue como a resistência mais
relevante, ainda sem teste bem-sucedido. A mínima da última sessão
(1.164,00) e o fechamento (1.170,75) permanecem os níveis de referência
técnica mais recentes disponíveis para a reabertura de segunda-feira.

**Câmbio, paridade BR e prêmio de exportação seguem travados no valor de
sexta-feira, sem nenhuma publicação de fim de semana.** USD/BRL PTAX em
5,0773 (BCB, 2026-07-31); paridade teórica em reais em **R$ 131,05/saca**
(indicators, CBOT 1.170,75 cts × USD/BRL 5,0773); CEPEA/ESALQ Soja
Paranaguá (via NAG) em R$ 144,91/saca (2026-07-31); prêmio de exportação
recalculável em **+10,58%** ((144,91-131,05)÷131,05) — idêntico ao valor
já reportado ontem, porque nenhum dos três insumos (CBOT, PTAX, CEPEA) tem
publicação de sábado ou domingo. A leitura de convergência física-papel
mencionada em leituras anteriores segue sem poder ser testada até a
reabertura de segunda-feira.

**O COT de 28/07/2026 (CFTC) continua sendo o retrato mais recente de
posicionamento — nenhum corte novo nesta janela, e o próximo (referente a
04/08/2026) só sai por volta de 07/08/2026.** Entre 21/07 e 28/07, o
managed money net long em soja havia subido +22,97% (de 130.505 para
160.479 contratos, 15,73% do open interest), majoritariamente via cobertura
de posição vendida, numa semana em que o preço ainda estava perto do topo
recente (fechamento de 28/07: 1.204,75). Do fechamento de 28/07 até o
fechamento revisado de 31/07 (1.170,75), a soja caiu **-2,82%** — uma fatia
relevante da posição comprada reforçada naquela semana específica segue,
portanto, com prejuízo de papel até a reabertura de segunda, um risco de
liquidação forçada que esta leitura mantém como o principal vetor de cauda
baixista para a soja.

**A manchete sobre o "tarifaço" citada ontem (Canal Rural, 01/08/2026,
"Radar Rural debate reação do Brasil ao tarifaço e desafios da safra de
soja") não reaparece no dump de hoje — o RSS de 2026-08-02 trouxe 6 itens
mantidos, mas nenhum com título extraído neste briefing.** Isso não
significa que o assunto perdeu relevância; apenas que esta leitura não tem,
a partir do dump de hoje, nenhum dado adicional (nem confirmação, nem
desmentido, nem detalhe de conteúdo) sobre esse tema. Segue como o ponto
cego mais importante para a reabertura de segunda-feira, tratado com a
mesma cautela de ontem (ver Honestidade).

### O que invalida / risco para a soja

- **Um fechamento consistente e sustentado acima de 1.180,00** na reabertura
  de segunda-feira desfaria a leitura de máximas decrescentes.
- **O conteúdo do "tarifaço" mencionado ontem, quando conhecido,** pode
  mudar materialmente esta leitura para qualquer direção — permanece o
  maior ponto cego, agora há dois dias sem nenhum dado adicional sobre ele.
- **O posicionamento especulativo esticado do COT de 28/07 (net long em
  15,73% do OI) se desmontar de forma desordenada** na reabertura, se o
  preço abrir em queda.
- **O câmbio abrir a semana em alta forte** — sem publicação de PTAX no fim
  de semana, não há como saber se a estabilização cambial de sexta teve
  continuidade.
- **O heating oil confirmar amanhã, com volume normal, a fraqueza do print
  parcial de hoje** — não seria um driver direto de soja, mas reforçaria o
  quadro de energia fóssil fraca que pressiona o complexo via biodiesel.

### Leitura operacional — soja

Sem pregão novo, não há ação tática nova a tomar hoje. A referência tática
de ontem permanece válida para a reabertura de segunda: quem está vendido
desde o rompimento de 29/07 pode usar 1.179,25 (máxima de sexta, valor já
revisado) como referência de stop. Quem está comprado segue exposto ao
risco de posicionamento identificado no COT de 28/07, sem nenhuma
oportunidade de se resolver — nem para pior, nem para melhor — durante o
fim de semana. A recomendação mais concreta continua sendo de ordem
prática: **checar o conteúdo do "tarifaço" antes da abertura de
segunda-feira**, já que segue sendo o único elemento genuinamente
qualitativo (não uma repetição de dado já conhecido) em aberto nesta
janela, e seu conteúdo real permanece desconhecido a partir deste
briefing.

---

## Farelo

**Viés: neutro tático dentro de uma tese estrutural bear ainda intacta —
sem dado de preço novo, o ratio Far/Soj permanece no valor revisado de
80,69% (sessão de 31/07), mais longe do piso de 80% do que o print
preliminar de 80,55% já descartado ontem.** Trata
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` (a fila
de hoje sinaliza novamente este item — o checkpoint formal de 18/06/2026
chega hoje a **45 dias** de atraso) e `release-nopa-2026-08-02` (novo
carimbo de fila, mesmo bloqueio de sempre — ver abaixo).

### O D+7 chega a 45 dias vencido — nenhum dado novo para testá-lo

A tese original ([[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]])
apostava que a compressão rápida do ratio em junho indicaria a zona
comprimida (<80%) "em 1-2 semanas". O checkpoint formal caiu em
18/06/2026; hoje, 02/08/2026, são **45 dias corridos** sem que o ratio
tenha fechado de forma robusta e repetida abaixo de 80% em nenhuma das seis
sessões observadas desde então (27/07: 80,09% → 28/07: 80,01% → 29/07:
81,10% → 30/07: 81,25% → 31/07: 80,69%, revisado). Sem pregão novo hoje,
esta leitura não tem como acrescentar uma sétima observação — apenas
reforça a recomendação já dada de que qualquer teste futuro do piso de 80%
precisa sobreviver a pelo menos uma revisão de dado (não só o print ao
vivo) antes de qualquer calibração de convicção tática. O próximo marco
formal segue sendo o D+90 (2026-09-09, agora a **38 dias**).

### O que sustenta a leitura de hoje

**Sem novo fechamento de farelo, a crush margin, o oil share e o oil-meal
spread permanecem exatamente nos valores revisados de 31/07/2026 já
detalhados em [[2026-08-01_leitura-complexo]]:** crush margin **2,6189
USD/bushel** (farelo 314,90 + óleo 67,26 − soja 1.170,75), folga sobre o
nível de alerta histórico (<2,50 USD/bu) em apenas 0,1189 USD/bu, a mais
apertada da série; oil-meal spread **0,4708 USD/bushel**, após a
compressão de -9,32% na revisão de sexta, a mais forte da janela. Nenhum
desses números tem como se mover sem pregão novo — mas o print parcial e
fraco do heating oil (ver Visão geral) não afeta diretamente o farelo, que
não tem exposição a energia fóssil da mesma forma que o óleo.

**As praças físicas de farelo no Brasil (NAG) seguem sem publicação de fim
de semana.** Mato Grosso/IMEA em R$ 1.675,10/ton, Rondonópolis/MT em R$
1.700,00/ton (o salto de +3,03% documentado na sexta segue sem confirmação
ou desmentido, agora há dois dias) e RS em R$ 1.640,00/ton. O prêmio de
exportação em Paranaguá segue zerado em +0,05 USD/short ton, agora **30
dias corridos sem variação** desde 03/07/2026 — o pilar mais persistente
da tese estrutural bear, e o mais tempo que este indicador específico já
ficou parado nesta série de leituras.

**O Índice de Sobra de Farelo (ISF) foi reimpresso hoje com carimbo de
2026-08-02, permanecendo em 80/100 (4 de 5 condições estruturais)** —
idêntico ao carimbo dos dois dias anteriores, confirmando que nenhum
insumo estrutural novo (ABIOVE, condições de crush de mais longo prazo)
entrou no cálculo durante o fim de semana. As projeções ABIOVE seguem sem
alteração: exportação de farelo brasileiro caindo de 1.400 mil toneladas
em agosto/2026 para 700 mil toneladas em dezembro/2026, uma queda de -50%
em quatro meses — o driver estrutural mais lento e mais persistente desta
tese, independente de qualquer ruído de curto prazo no ratio.

**`release-nopa-2026-08-02` (fila de hoje) sinaliza um novo carimbo de
release do NOPA, mas o `monthly_status` permanece em 0,0 bool** — a mesma
barreira de assinatura paga documentada desde meados de junho, agora
~7 semanas sem alternativa de dado primário sobre o crush americano. Esta
leitura trata este item da fila como tratado (sem conteúdo novo para
incorporar), não como pendência de leitura.

### O que invalida / risco para o farelo

- **O ratio Far/Soj precisa fechar de forma robusta e repetida abaixo de
  80% — com dados JÁ REVISADOS — para validar qualquer tese tática bear.**
  Sem sessão nova hoje, essa exigência segue exatamente onde estava ontem.
- **A posição comprada reforçada pelo COT de 28/07 (net long em 14,11% do
  OI) se desmontar de forma desordenada** na reabertura de segunda.
- **O salto isolado de Rondonópolis (+3,03%, 30/07→31/07) se confirmar
  como tendência** quando o mercado físico voltar a publicar na
  segunda-feira.
- **O prêmio de exportação em Paranaguá sair de zero** depois de 30 dias
  parado — quanto mais tempo passa, maior a chance de que a próxima
  variação, quando vier, seja abrupta.

### Leitura operacional — farelo

Sem sessão nova e sem publicação física de fim de semana, não há ação
tática adicional a tomar hoje. A recomendação de ontem permanece: tratar
qualquer fechamento futuro perto do piso de 80% com ceticismo até que ele
sobreviva à revisão do dia seguinte. Para quem opera o oil-meal spread, a
compressão revisada de sexta (-9,32%) segue sendo o sinal mais limpo e mais
robusto desta janela de que a força relativa do farelo dentro do crush está
genuinamente aumentando — mas sem dado novo hoje para confirmar
continuidade.

---

## Óleo

**Viés: bear — sem pregão novo para soja/farelo/óleo, a distância abaixo do
suporte técnico de 72,00 permanece nos -6,58% já calculados com o
fechamento revisado de 31/07/2026 (67,26 cts/lb).** Trata
`alerta-quebra_suporte-oleo_cbot-2026-07-31` (a fila de hoje repete o mesmo
alerta, com o fato ainda no mesmo valor: 67,26 vs 72,00). O elemento
genuinamente novo desta leitura é o print parcial do heating oil, tratado
como cor direcional, não como confirmação.

### O que sustenta a tese

**A leitura técnica herda integralmente a revisão de ontem: fechamento
67,26 cts/lb, posição dentro do range de 38,2% (terço inferior), volume
revisado para 48.109 contratos.** Sem pregão novo, nenhum desses números
tem como se mover — a mínima de sexta (66,66) e a máxima (68,23) seguem
sendo as referências técnicas mais recentes para a reabertura de
segunda-feira.

**O heating oil (HO=F) trouxe, pela primeira vez nesta janela de fim de
semana, um print com carimbo de hoje — e ele é fraco, embora de liquidez
baixíssima.** Abertura 3,978, máxima 4,0642, mínima 3,97, fechamento (no
momento da coleta) **4,0523 USD/galão**, volume **1.010 contratos** —
-1,68% abaixo do fechamento revisado de sexta (4,1215) e um volume ainda
menor que os 12.325 contratos de sexta, que já haviam sido qualificados
como anômalos frente à faixa histórica de 27 mil+ vista em sessões
anteriores desta série. **Mecanismo:** heating oil é metade da receita do
biodiesel americano (a outra metade é o RIN D4, fixo em 2,11 USD/RIN); um
heating oil mais fraco, se confirmado, comprimiria ainda mais a margem de
biodiesel (já em 1,4420 USD/galão na revisão de sexta, abaixo dos 1,4579
de quinta) — um dos poucos contrapontos fundamentalistas que ainda restam
à tese bear do óleo. **Esta leitura NÃO recalcula a margem de biodiesel com
este número**, porque isso exigiria combinar um preço de óleo de sexta
(congelado) com um preço de heating oil de domingo (parcial) — uma mistura
de datas que os indicadores internos não fizeram e que esta leitura evita
por princípio (não inventar indicador). O print é registrado apenas como
sinal de alerta direcional para a reabertura de segunda-feira.

**O Índice de Suporte do Óleo (ISO) foi reimpresso hoje com carimbo de
2026-08-02, permanecendo em 100/100 (5 de 5 condições)** — idêntico aos
dois carimbos anteriores, confirmando que a tese estrutural (óleo dominando
o valor do crush) segue formalmente intacta apesar da fraqueza de preço.
É importante não confundir as duas coisas: o ISO mede QUEM CAPTURA MAIS
VALOR dentro do crush (óleo vs. farelo), não se o óleo está caro ou barato
em termos absolutos — as duas leituras (ISO alto + preço do óleo rompendo
suporte) são compatíveis e, de fato, coexistem nesta série há várias
sessões.

**Sem COT novo nesta janela** — o corte de 28/07/2026 segue sendo a
fotografia mais recente, mostrando os fundos já reduzindo o net long em
óleo (-10,27%, para 16,60% do open interest) durante a própria sequência de
quebra técnica em curso naquela semana, ao contrário do padrão de "compra
na fraqueza" visto em soja e farelo. Do fechamento de 28/07/2026 (70,14) até
o fechamento revisado de 31/07 (67,26), o óleo caiu -4,11% — a leitura de
que o book especulativo em óleo tem, proporcionalmente, menos posição
comprada "presa" em prejuízo recente do que soja e farelo permanece o
argumento mais construtivo desta tese bear.

### O que invalida / risco para o óleo

- **Um fechamento abaixo de 66,66 (mínima de sexta) na reabertura de
  segunda** confirmaria uma sexta sessão seguida de fraqueza técnica.
- **O heating oil confirmar amanhã, com volume normal, o nível fraco do
  print parcial de hoje (~4,05, ante 4,12 de sexta)** — reforçaria o
  vetor bearish sobre a margem de biodiesel; ao contrário, uma reversão
  para cima com volume normal esvaziaria o sinal de hoje como ruído de
  baixíssima liquidez.
- **A isenção PIS/Cofins do biodiesel seguir sem renovação após a
  reabertura de expediente público de segunda-feira** (ver Lente fiscal) —
  o teste real deste vetor só começa amanhã.
- **O oil share continuar caindo** (sexta sessão seguida na revisão de
  sexta, -0,15pp).
- **A backwardation continuar comprimindo até desaparecer.**
- **MPOB seguir inacessível** (agora 24º dia consecutivo).

### Leitura operacional — óleo

Sem pregão novo para soja/farelo/óleo, esta leitura não recomenda nenhuma
ação tática nova hoje — a referência de ontem permanece válida: quem está
vendido ou tático short pode usar a mínima de sexta (66,66) como referência
de entrada recente, com stop acima da máxima do dia (68,23). O único
elemento a monitorar ativamente até a reabertura é o heating oil: se o
print de 4,0523 (parcial, 1.010 contratos) sobreviver com volume mais
robusto na segunda-feira, é um argumento adicional — não novo em direção,
mas relevante em timing — para tratar a abertura da semana com cautela
extra do lado comprado. Se, ao contrário, o heating oil reverter para perto
de 4,12 com volume normal, o print de hoje deve ser descartado como ruído
de liquidez de domingo à noite, não como sinal.

---

## Spreads e crush — leitura de complexo

### Ratio Far/Soj: 80,69% (mesmo valor revisado de 31/07) — 45 dias sem confirmação do D+7

Sem sessão nova, o ratio permanece exatamente no valor revisado de sexta
(80,69%), mais distante do piso de 80% do que o print preliminar (80,55%)
já descartado. A fila de hoje sinaliza novamente
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` como
revisão vencida — agora **45 dias** além do checkpoint formal de
18/06/2026. O D+90 (2026-09-09) é o próximo marco formal, a **38 dias**
de hoje.

### Crush margin: 2,6189 USD/bu — folga mínima sobre o nível de alerta, sem dado novo para testar continuidade

Valor herdado de 31/07/2026, sem alteração possível sem pregão novo. A
folga sobre o nível de alerta histórico (<2,50 USD/bu) permanece em 0,1189
USD/bu, a mais apertada já registrada nesta série.

### Oil share: 51,64% — sexta queda seguida (na última sessão observada), sem dado novo hoje

Idem: valor herdado de 31/07/2026. A sexta sessão seguida de queda segue
sendo a última observação disponível até a reabertura.

### Oil-meal spread: 0,4708 USD/bu — compressão mais forte da janela, sem teste novo hoje

Idem: valor herdado de 31/07/2026, a maior compressão percentual de um
único dia (-9,32%) registrada nesta métrica em toda a série observada.

### Heating oil: primeiro print da semana é fraco e de liquidez anômala — vetor de atenção, não de convicção

O único dado genuinamente novo desta leitura de complexo é o print parcial
de heating oil (4,0523, -1,68% frente ao fechamento revisado de sexta,
apenas 1.010 contratos). Não é usado para recalcular margem de biodiesel
(mistura de datas), mas é registrado como o primeiro sinal — ainda que
frágil — de para onde a energia fóssil pode abrir a semana, relevante
porque o heating oil é metade da receita da margem de biodiesel que
sustenta parcialmente a demanda de óleo de soja como insumo.

### Sem COT novo, sem publicação de PTAX/CEPEA/NAG de fim de semana

Nenhum desses fluxos de dado publica aos domingos — a leitura de
posicionamento e de físico BR permanece exatamente a mesma descrita em
[[2026-08-01_leitura-complexo]], sem informação nova para testá-la.

### ISF em 80/100, ISO em 100/100 — reimpressos hoje, terceiro dia seguido sem alteração

Ambos os índices sintéticos foram recarimbados com a data de 2026-08-02,
mantendo exatamente os mesmos valores dos dois carimbos anteriores —
confirma que nenhum insumo estrutural novo entrou no cálculo neste fim de
semana estendido.

### O que os índices dizem juntos em 2026-08-02

ISF 80/100 + ISO 100/100 (ambos reimpressos, inalterados) + ratio Far/Soj
em 80,69% (mesmo valor revisado de sexta, D+7 formalmente vencido há 45
dias) + crush margin com a folga mais apertada da série (0,1189 USD/bu)
+ oil-meal spread na compressão mais forte da janela (-9,32% na última
sessão observada) seguem, todos, exatamente onde estavam ontem — não há
teste novo de preço para confirmar ou desafiar nenhum desses números. O
único elemento incremental é o print parcial e fraco do heating oil, que
esta leitura trata como um vetor de atenção para a reabertura de
segunda-feira, não como um dado com peso suficiente para mudar qualquer
conclusão de convicção. Combinado, o quadro do complexo neste domingo é de
**pausa completa de dado de preço nas três pernas principais, com um único
sinal de baixa liquidez apontando para o mesmo lado (bearish) que já vinha
sendo descrito desde sexta-feira** — a reabertura de segunda-feira é o
primeiro teste real de tudo isso.

---

## Lente fiscal e regulatória BR

**Isenção PIS/Cofins biodiesel — venceu sexta-feira, 31/07/2026; hoje,
2026-08-02 (domingo), é o segundo dia corrido após o vencimento, e o
silêncio de hoje ainda não pode ser lido como sinal.** (evento
`PISCOFINS-BIODIESEL-ISENCAO`, `atualizado_em` 2026-06-05, agora **58
dias sem atualização** do monitor). **Mecanismo e leitura:** assim como
sábado, domingo é dia sem expediente público brasileiro — repartições não
publicam atos normativos, e o Diário Oficial da União só tem edição
extraordinária em casos de urgência. Esta leitura mantém o mesmo critério
já estabelecido ontem: **o silêncio de hoje continua sendo neutro por
inatividade do calendário administrativo, não um sinal adicional de que a
isenção expirou sem renovação.** O teste real segue sendo a reabertura do
expediente público na segunda-feira, 2026-08-03. Se a segunda-feira também
passar sem sinal de prorrogação, a leitura muda de "neutro por
inatividade" para "sinal concreto de que a isenção efetivamente caducou"
— um vetor bearish direto para a demanda de óleo de soja como insumo do
biodiesel doméstico brasileiro, distinto e adicional a qualquer coisa que
aconteça no CBOT.

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L) —
vigência formal venceu há 22 dias (`vigencia_ate` 11/07/2026), sem
qualquer atualização de status.** Enquanto o combustível fóssil segue
formalmente subsidiado (sem confirmação de que o subsídio de fato
terminou), a competitividade relativa do biodiesel dentro do mix B15
mandatório segue pressionada.

**B16 — sem data, travado em B15**, sem mudança de status.

**MP 1.363/2026 (subsídio ao diesel fóssil, R$ 1,12/L) — em vigor até
31/12/2026**, sem alteração. Bearish estrutural persistente para a demanda
incremental de óleo de soja no mercado doméstico brasileiro — e, com o
diesel fóssil subsidiado E o heating oil americano (proxy de energia
fóssil global) mostrando um print fraco hoje, os dois vetores de energia
fóssil apontam, por caminhos independentes, na mesma direção bearish para
a competitividade do biodiesel via óleo de soja.

**STJ REsp 2.165.276/2026 — crédito PIS/Cofins para esmagadoras**, sem
alteração. Bullish para soja/óleo (alívio de custo de entrada para
biodiesel), independente da mecânica tática de curto prazo do crush.

**Vetores dos EUA e Indonésia, sem mudança de status desde 2026-06-05:**
EPA-RFS-2026-2027 (volumes recordes de biocombustível, sustentando o RIN
D4 usado na margem de biodiesel, fixo em 2,11 USD/RIN); 45Z-CLEAN-FUEL
(regra que favoreceria óleo de soja doméstico americano); DANANTARA-
INDONESIA (centralização estatal da exportação de palma, plena em
01/09/2026, agora a 30 dias); INDONESIA-B50 (provável B45 em 2026, B50
pleno só 2027-28); INDONESIA-LEVY-PMK9 (imposto de exportação de CPO até
12,5%, encarecendo palma). Conjunto estruturalmente bullish para óleo de
soja via substituição de palma, mas inverificável pelo lado de mercado
(MPOB inacessível há 24 dias, ver Honestidade).

**O monitor tributário como um todo está há 58 dias sem qualquer
atualização.** Prioridade máxima de manutenção do sistema, independentemente
da leitura de preço de hoje — e ainda mais relevante nesta janela
específica, dado o vencimento da isenção PIS/Cofins ter caído exatamente
dentro do período em que o monitor está inativo.

---

## Riscos e eventos próximos

**A reabertura da CBOT na segunda-feira, 2026-08-03, é o primeiro teste
real de todas as leituras desta janela de fim de semana** — em especial
se o suporte do óleo (72,00, atualmente -6,58% abaixo) continua se
afastando, e se o print fraco de heating oil de hoje se confirma com
volume normal ou se dissolve como ruído de baixa liquidez.

**A isenção PIS/Cofins do biodiesel segue sem sinal de renovação; a
reabertura de expediente público de segunda-feira é o primeiro momento em
que o silêncio deixa de ser explicável por inatividade de calendário** —
o item de verificação manual mais urgente desta janela.

**O conteúdo real da manchete sobre o "tarifaço" (Canal Rural, 01/08/2026)
permanece desconhecido — e o dump de hoje não trouxe nenhuma manchete nova
para complementá-lo** — segundo item de verificação manual prioritário,
dado o potencial de impacto direto sobre o fluxo de exportação de soja
brasileira.

**O próximo corte do COT (referente a 04/08/2026) só é publicado por volta
de 07/08/2026** — até lá, a divergência de posicionamento entre pernas
identificada no corte de 28/07 (soja e farelo mais comprados e mais
vulneráveis; óleo já reduzindo exposição) segue sem novo dado para
confirmar se está se resolvendo por desmonte, recuperação de preço, ou
ambos.

**O ratio Far/Soj está parado em 80,69% (valor revisado de sexta), com o
D+7 formal vencido há 45 dias sem confirmação** — monitorar o D+90
(2026-09-09) como próximo marco formal, a 38 dias.

**O USDA Crop Progress deve trazer corte novo por volta de segunda-feira,
2026-08-03** (cadência semanal normal desde o último corte de 26/07).

**NOPA — fila `release-nopa-2026-08-02` sinaliza um novo "release", mas o
dado segue inacessível** (`monthly_status` em 0,0 bool), agora ~7 semanas
sem alternativa de dado primário sobre o crush americano.

**MPOB — sem números de palma extraídos há 24 dias consecutivos.**

**O WASDE segue fora da janela deste briefing, agora 23 dias de atraso**
desde o último dado (10/07/2026).

---

## Honestidade

O que não foi possível validar neste briefing de 2026-08-02, e os pontos
onde a confiança é baixa ou há lacunas relevantes:

**1. Não houve pregão novo hoje para soja, farelo ou óleo — 2026-08-02 é
domingo, mercado fechado para essas três pernas neste dump.** Toda a
análise de preço dessas três commodities trata da mesma sessão de
31/07/2026 já coberta em [[2026-07-31_leitura-complexo]] e
[[2026-08-01_leitura-complexo]], sem nenhum valor novo. Esta leitura não
inventa nem estima nenhum movimento de preço para essas três pernas hoje.

**2. O print de heating oil (HO=F) com carimbo de 2026-08-02 é tratado
como PARCIAL, não como sessão fechada — o volume de apenas 1.010 contratos
é ainda menor que os 12.325 de sexta, já qualificados como anômalos frente
à faixa histórica de 27 mil+ desta série.** Esta leitura usa o número
apenas como cor direcional (heating oil mais fraco que o fechamento de
sexta) e explicitamente recusa-se a recalcular a margem de biodiesel
misturando esse preço parcial de domingo com o preço de óleo de sexta —
essa combinação de datas não foi feita pelos indicadores internos, e esta
leitura não gera indicador que o robô não gerou.

**3. A manchete "Radar Rural debate reação do Brasil ao tarifaço e
desafios da safra de soja" (Canal Rural, 01/08/2026), citada em
[[2026-08-01_leitura-complexo]], NÃO reaparece no dump de hoje — não há
manchete nova nem confirmação/desmentido do conteúdo daquela.** O RSS de
2026-08-02 registra 6 itens mantidos, mas nenhum título foi extraído para
este briefing. Tratado como o item de verificação manual de maior
prioridade desta janela, sem nenhum conteúdo novo incorporado.

**4. As revisões de dados já documentadas em leituras anteriores (heating
oil revisado em até ~292x em episódios passados) seguem sendo um lembrete
de que qualquer valor "final" pode ainda mudar no próximo dump** — os
valores de 31/07/2026 usados nesta leitura (crush margin, ratio Far/Soj,
oil share, oil-meal spread) já passaram por uma revisão (documentada em
[[2026-08-01_leitura-complexo]]), mas não há garantia de que sejam
definitivos.

**5. O salto físico de farelo em Rondonópolis/MT (+3,03% em 31/07, para
R$ 1.700,00/ton) segue sem confirmação ou desmentido** — não há
publicação de fim de semana para testar se o movimento teve continuidade
ou foi revertido.

**6. O USDA Crop Progress permanece no corte de 26/07/2026 (11%/52%/7%)**,
dentro da cadência semanal normal; o próximo corte é esperado por volta de
segunda-feira.

**7. O WASDE permanece completamente fora da janela deste briefing** —
agora 23 dias de atraso desde o último dado (10/07/2026).

**8. NOPA (fila `release-nopa-2026-08-02`) segue com `monthly_status` em
0,0 bool** — mesma barreira de assinatura paga, ~7 semanas sem
alternativa de dado primário.

**9. Palma malaia (MPOB) segue sem números extraídos**, mesmo conteúdo
exato de 3.439 caracteres, agora 24º dia consecutivo.

**10. O COT (CFTC) de 28/07/2026 segue sendo o dado de posicionamento
mais recente — nenhum corte novo nesta janela.** A leitura de risco de
liquidação forçada em soja/farelo, e de exposição comprada relativamente
mais "aliviada" em óleo, é herdada integralmente de
[[2026-08-01_leitura-complexo]], sem possibilidade de teste adicional até
07/08/2026.

**11. Percentis históricos de COT não calculados** — mesma limitação
documentada nas leituras anteriores.

**12. Clima INMET (BR) não foi usado como driver de preço** — julho/agosto
é entressafra da soja brasileira, sem relevância direta neste momento do
calendário agrícola.

**13. BCBA Argentina — 4ª sessão seguida acessível via scraper (30/07,
31/07, 01/08, 02/08), ainda sem relatórios de esmagamento/exportação
extraíveis.**

**14. O monitor tributário (`system/tributario_watch.toml`) está há 58
dias sem atualização** — o vencimento da isenção PIS/Cofins caiu
exatamente dentro dessa janela de inatividade do monitor, prioridade
máxima de manutenção do sistema já sinalizada em leituras anteriores.

**15. Os forecasts estatísticos internos não têm geração visível com
carimbo de 2026-08-02 neste dump** — a última geração disponível
(2026-08-01) mantinha o rótulo "altista" para as três commodities, gerado
a partir do fechamento revisado de sexta, sem incorporar nenhuma das
leituras qualitativas desta análise (ausência de pregão, print parcial de
heating oil, tarifaço não detalhado).

*Nenhum número foi inventado ou estimado além do que consta no briefing de
2026-08-02 e nos insights anteriores referenciados. A contribuição central
desta leitura foi (1) identificar o heating oil como o único instrumento
com dado de preço genuinamente novo nesta janela de fim de semana, tratando
seu print parcial (4,0523, -1,68% frente a sexta, apenas 1.010 contratos)
como sinal de atenção direcional sem recalcular indicadores derivados que
misturariam datas distintas; (2) atualizar a contagem de dias de todos os
gatilhos pendentes da fila e do monitor tributário (D+7 do ratio a 45 dias,
prêmio export farelo/óleo parado há 30 dias, isenção PIS/Cofins no 2º dia
corrido vencida, monitor tributário a 58 dias sem atualização, MPOB a 24
dias inacessível, WASDE a 23 dias de atraso); (3) tratar os três itens da
fila de julgamento de hoje —
`alerta-quebra_suporte-oleo_cbot-2026-07-31`,
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` e
`release-nopa-2026-08-02` — no contexto específico de um domingo sem dado
novo de mercado para as três pernas principais; e (4) sinalizar
explicitamente a ausência de manchete nova sobre o "tarifaço" no dump de
hoje, evitando tanto inventar conteúdo quanto presumir que o silêncio
resolve a pendência aberta ontem.*
