---
data: 2026-08-07
titulo: "O ratio Far/Soj sobe de volta para 80,60% invertendo a compressão de ontem — farelo mais firme e soja mais fraca no mesmo pregão, um movimento genuíno contra a tese do D+7 —, enquanto a curva do óleo aprofunda a inversão em backwardation pela segunda sessão seguida (o aperto concentrado no fim da curva, não no início), e a manchete do dia expõe a tensão entre o preço recorde da soja em Mato Grosso e o aperto de margem da indústria brasileira de esmagamento"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT (ZSU26 soja / ZMU26 farelo / ZLU26 óleo) — sessão de 2026-08-06 (quinta-feira), a mais recente disponível neste briefing (lido em 2026-08-07)
  - CME NYMEX heating oil (HO=F) — 2026-08-06, fechamento 3,7691 USD/galão, volume 234 contratos
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, paridade BR, Índice de Sobra de Farelo, Índice de Suporte do Óleo) — recalculados com o fechamento de 2026-08-06
  - BCB PTAX — carimbo mais recente 2026-08-05 (USD/BRL 5,1154); sem atualização de PTAX para 2026-08-06 neste briefing, ver Honestidade
  - CEPEA/ESALQ Soja Paranaguá via NAG — carimbo mais recente 2026-08-05, R$ 144,91/saca (var +0,55%); sem carimbo novo para 2026-08-06
  - CEPEA/ESALQ Soja Paraná interior via NAG — carimbo mais recente 2026-08-05, R$ 136,73/saca
  - NAG Físico BR — carimbo mais recente 2026-08-05 (farelo MT/IMEA R$ 1.675,10/ton congelado desde 31/07; Rondonópolis/MT R$ 1.700,00/ton congelado desde 31/07; RS R$ 1.800,00/ton, salto de 05/08 ainda sem segunda leitura de confirmação); prêmios export PGUA farelo/óleo também sem carimbo novo, último em 2026-08-04 (farelo +0,05 USD/sht; óleo +0,08 cts/lb, "mês Agosto/26")
  - CFTC COT Managed Money — corte de 2026-07-28 (sem corte novo nesta janela; o próximo, referente a 2026-08-04, é esperado por volta de hoje, 2026-08-07, mas ainda não está neste briefing)
  - USDA Crop Progress — corte rotulado 2026-08-02, mesmos valores do corte de 2026-07-26 (11% excelente / 52% boa / 7% ruim), agora pela quarta leitura seguida sem mudança
  - USDA WASDE — ausente da janela, agora 28 dias de atraso desde o último dado (2026-07-10)
  - NOPA — fila `release-nopa-2026-08-06`, `monthly_status` continua em 0,0 bool (paywall), mais de 8 semanas sem alternativa de dado primário
  - ABIOVE projeções mensais — balanços ago-dez/2026, sem alteração frente ao dump anterior (exportação de farelo caindo de 1.400 para 700 mil t entre agosto e dezembro; exportação de óleo caindo de 110 para 21 mil t entre setembro e novembro; esmagamento mensal projetado em queda de 2.827 mil t em setembro para 2.204 mil t em dezembro)
  - NOAA CPC ENSO — 2026-08-06 (El Niño Advisory, inalterado)
  - MPOB — 2026-08-06 (mesmo conteúdo de 3.439 caracteres, parser sem números extraídos)
  - BCBA Argentina — 2026-08-06 (acessível, sem links de relatório detectados, mesmo padrão de sessões recentes)
  - INMET — previsão para 2026-08-06: chuva/trovoada em Cascavel e Maringá (PR) e Passo Fundo (RS, risco de granizo); calor seco em Cuiabá, Lucas do Rio Verde, Rio Verde (GO), Sinop e Sorriso (MT, 35-37°C, poucas nuvens)
  - Notícias Agrícolas/Canal Rural RSS — 2026-08-06 (160 itens lidos, 4 mantidos; manchete "Soja em Mato Grosso atinge maior preço do ano, mas indústria enfrenta desafios", canalrural.com.br — headline sem número extraído, ver Honestidade)
  - system/tributario_watch.toml (lido como referência, não editado) — `atualizado_em` 2026-06-05, agora 63 dias sem atualização; evento `PISCOFINS-BIODIESEL-ISENCAO` com `vigencia_ate` 2026-07-31, hoje é o 5º dia útil desde o vencimento
  - Cruza com [[2026-08-05_leitura-complexo]], [[2026-08-04_leitura-complexo]] e [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (tese original do D+7, revisada abaixo)
status: ativa
vies: [neutral-soja, bear-farelo, bear-oleo_soja]
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
sobe, o óleo "manda" no crush — a esmagadora aceita vender o farelo mais
barato porque o que sustenta a decisão de esmagar é a margem do óleo, e o
farelo vira, na prática, o subproduto que sobra. O **ratio Far/Soj** (preço
do farelo dividido pelo preço da soja, normalizado pela conversão
bushel↔short ton) mede a mesma dinâmica por outro ângulo: abaixo de 80% o
farelo está historicamente "abundante" frente à soja — zona baixista para o
farelo —, acima de 87% está "apertado" — zona altista —, e entre os dois fica
a zona neutra de mean-reversion (o preço tende a voltar pro meio quando se
afasta demais de um extremo).

**A sessão de referência de hoje é a de 2026-08-06, quinta-feira — o
fechamento mais recente disponível neste briefing, lido em 2026-08-07,
sexta-feira.** A soja fechou em **1.157,50 cts/bushel** (CBOT, ticker
ZSU26.CBT), praticamente parada frente ao fechamento de ontem (1.158,25,
**-0,06%**), com uma amplitude de apenas **2,75 pontos** (máxima 1.158,50,
mínima 1.155,75) — a menor amplitude desta série de leituras, ainda mais
estreita que os já apertados 13,00 pontos de ontem. O farelo, ao contrário,
fechou em **311,00 USD/short ton** (ticker ZMU26.CBT), **+0,10%** sobre
ontem (310,70) — um movimento pequeno em termos absolutos, mas que, somado à
queda da soja, produz um efeito mecânico relevante: **o ratio Far/Soj subiu
de 80,47% para 80,60%** (indicators, 2026-08-06), uma alta de +0,13 ponto
percentual que **inverte exatamente a compressão de ontem** — e, ao contrário
dos dias em que o ratio se movia "pelo motivo errado" (o denominador soja
oscilando mais que o farelo), hoje os dois lados empurram na mesma direção
bearish-para-o-farelo: o farelo subiu (numerador maior) e a soja caiu
(denominador menor), ambos elevando o ratio. Trata
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` (fila de
hoje) — a tese de compressão segue tecnicamente não confirmada, e o
movimento de hoje é uma contraprova genuína, não um artefato. O óleo fechou
em **67,60 cts/lb** (ticker ZLU26.CBT), **-0,21%**, seguindo abaixo do
suporte técnico de 72,00 — trata `alerta-quebra_suporte-oleo_cbot-2026-08-06`
(fila de hoje) — e a curva futura, que ontem virou backwardation pela
primeira vez nesta série, **aprofundou a inversão hoje**: o spread entre o
contrato mais próximo (Q26, 67,85) e o mais distante (H27, 66,88) abriu de
0,82 para **0,97 cts/lb** (+18,3%), mas o motor dessa ampliação foi o **fim**
da curva enfraquecendo (H27 caiu 0,16, de 67,04 para 66,88) muito mais do que
o início se firmando (Q26 praticamente parado, -0,01). O dia também trouxe a
manchete "Soja em Mato Grosso atinge maior preço do ano, mas indústria
enfrenta desafios" (Canal Rural, 06/08/2026) — sem número extraído, mas que
aponta um mecanismo plausível e coerente com os dados disponíveis: o físico
brasileiro pode estar subindo mais rápido que o CBOT, apertando a margem
*real* de esmagamento doméstica (que depende do custo local da soja) mesmo
com a crush margin *de papel* (calculada em CBOT, 2,703 USD/bushel hoje)
seguindo folgada. **Leitura de uma linha:** o pivô do complexo hoje é a
divergência entre uma soja tecnicamente inerte no papel (CBOT quase parado,
menor amplitude da série) e um físico brasileiro que a manchete descreve como
fazendo máxima do ano, com o farelo mostrando um sinal tático que contradiz
a tese estrutural de "sobra" pela primeira vez em várias sessões, e o óleo
aprofundando sua inversão de curva pelo fim, não pelo início; maior convicção
desta leitura está no mecanismo do ratio (movimento hoje é genuíno nos dois
lados, verificável); confiança moderada para a leitura de backwardation do
óleo, cujo mecanismo (fim da curva cedendo) é observável mas cuja causa é
hipótese, não fato confirmado; confiança baixa para qualquer tese direcional
nova da soja a partir de um dia de amplitude recorde de estreiteza, e uma
ressalva importante de qualidade de dado (ver Honestidade) reduz a confiança
nos volumes e nas máximas/mínimas informados para farelo hoje.

---

## Soja

**Viés: neutro — segunda sessão seguida de consolidação extrema no papel
(CBOT), com a menor amplitude desta série de leituras, mas acompanhada por
uma manchete de físico brasileiro que, se confirmada, aponta para uma
dinâmica de preço doméstico mais forte do que a paridade sugere.**
Fechamento: 1.157,50 cts/bushel (CBOT, ticker ZSU26.CBT, 2026-08-06).

### O que sustenta a tese

**A sessão foi ainda mais estreita que a de ontem, que já era a mais
apertada da série.** Abertura 1.157,25, máxima **1.158,50**, mínima
**1.155,75**, fechamento **1.157,50** — uma amplitude de apenas **2,75
pontos**, menos de um quarto dos 13,00 pontos de ontem e uma fração dos
ranges de 30-50 pontos que caracterizaram as sessões de reversão em
03-04/08. O fechamento a 63,6% do range ((1.157,50-1.155,75)÷2,75) fica no
terço superior, mas com um range tão estreito esse dado carrega pouco peso
direcional. **Mecanismo:** dois dias seguidos de amplitude comprimida,
sem notícia de demanda chinesa nova (ver abaixo) e sem catalisador
fundamental fresco (WASDE ausente há 28 dias, COT parado há 10 dias),
sugerem um mercado tecnicamente "represado", aguardando o próximo gatilho
de dado — seja o COT desta sexta-feira, seja uma manchete de exportação, seja
o WASDE, sempre que voltar a ser publicado.

**A curva futura segue em contango regular, com um pequeno deslocamento
paralelo para baixo frente a ontem.** Q26 (ago/26) 1.151,75, U26 (set/26)
1.157,50, X26 (nov/26) 1.175,75, F27 (jan/27) 1.191,00, H27 (mar/27)
1.197,00, K27 (mai/27) 1.205,25 — cada vencimento mais distante vale mais
que o anterior, mantendo o desenho de mercado sem aperto de oferta prompt.
Comparado à curva de ontem (Q26 1.152,00, U26 1.158,25, X26 1.176,75, F27
1.191,50, H27 1.198,00, K27 1.206,50), cada ponto caiu entre 0,25 e 1,25
pontos — um deslocamento paralelo, não uma mudança de formato: o spread
entre o contrato mais distante e o mais próximo (K27-Q26) ficou em 53,50
hoje contra 54,50 ontem, uma diferença de apenas 1,00 ponto, essencialmente
estável. **Mecanismo:** um contango que se desloca em paralelo (sem
esticar nem comprimir o spread) indica que o mercado não mudou sua leitura
relativa de curto vs. longo prazo — só recalibrou o nível absoluto
ligeiramente para baixo, coerente com um dia de baixa convicção
direcional. Isso contrasta com o óleo, cuja curva não apenas está invertida
mas também está se esticando (ver seção Óleo).

**O câmbio não trouxe informação nova hoje — a paridade em reais foi
calculada com o PTAX de ontem, sem atualização.** O BCB não publicou um
novo carimbo de PTAX para 2026-08-06 neste briefing; o último disponível
segue sendo **5,1154 BRL/USD (2026-08-05)**. A paridade teórica em reais
(sem prêmio de basis) recuou para **R$ 130,54/saca** (indicators, CBOT
1.157,50 cts × USD/BRL 5,1154), **-0,06%** sobre ontem (130,62) — um
movimento pequeno e mecânico, que reflete apenas a leve queda da soja em
CBOT, já que o câmbio usado é literalmente o mesmo número de ontem. **Isso
é relevante para quem opera a paridade como referência**: qualquer
movimento cambial genuíno de 2026-08-06 (se houve) ainda não está
capturado neste número — ver Honestidade.

**A manchete do dia muda o ângulo da narrativa: pela primeira vez nesta
série recente, o destaque não é sobre CBOT nem sobre demanda chinesa, mas
sobre o físico brasileiro.** "Soja em Mato Grosso atinge maior preço do ano,
mas indústria enfrenta desafios" (Canal Rural, 06/08/2026) — o item veio
como headline puro, sem corpo de texto nem número extraído neste briefing
(campo `headline: None`). **Mecanismo e leitura, com a devida cautela
epistêmica (mesma ressalva já aplicada a manchetes sem número nesta série):**
se o preço físico da soja em Mato Grosso está de fato fazendo máxima do ano,
isso é consistente com o prêmio de exportação de Paranaguá que, na última
leitura confiável (05/08), estava em torno de +10,94% sobre a paridade
teórica — ou seja, o físico brasileiro já vinha pagando um prêmio elevado
frente ao CBOT convertido, e a manchete de hoje pode ser a continuação desse
movimento. **O que a manchete acrescenta é a segunda metade da frase — "mas
a indústria enfrenta desafios"** — um mecanismo direto: se o custo local da
soja (matéria-prima) sobe mais rápido que os preços locais de farelo e óleo
(que, pelos dados físicos disponíveis, estão congelados: MT/IMEA parado em
R$ 1.675,10/ton desde 31/07), a margem de esmagamento *real* no Brasil
comprime — mesmo que a crush margin *de papel*, calculada inteiramente em
CBOT (farelo + óleo − soja, todos em dólares/Chicago), continue folgada em
2,703 USD/bushel hoje. Este é um ponto de desconexão entre o indicador
sintético que o robô calcula (referência internacional) e a realidade
operacional que a manchete descreve (referência doméstica) — vale a pena o
dono cruzar essa manchete com o basis físico que efetivamente pratica na
sua praça antes de tratar a crush margin CBOT como proxy direta da margem
brasileira.

**O posicionamento do COT (CFTC, corte de 28/07/2026) segue sendo o retrato
mais recente — nenhum corte novo hoje, e o próximo, referente a 04/08/2026,
é esperado por volta de hoje (sexta-feira, 07/08), mas ainda não está
neste briefing.** O managed money net long em soja estava em 160.479
contratos (15,73% do open interest de 1.020.108), após uma alta de +22,97%
na semana anterior ao corte, com o preço na época rondando o topo recente
(fechamento de 28/07: 1.204,75). A soja de hoje (1.157,50) está -3,93%
abaixo desse nível — distância praticamente igual à de ontem (-3,86%), sem
piora nem alívio relevante.

**A seleção de notícias do dia (4 de 160 itens mantidos) segue entre as
mais enxutas da série** — um sinal, ainda que indireto, de baixo fluxo de
notícia fundamentalista específica do complexo hoje, reforçando a leitura
de "mercado represado aguardando catalisador".

### O que invalida / risco para a soja

- **A manchete de máxima do ano em Mato Grosso ganhar um número
  verificável** (em R$/saca ou R$/ton, com fonte e data) — hoje ela entra
  nesta leitura apenas como headline qualitativo; um número confirmado
  mudaria a magnitude da leitura sobre o basis físico brasileiro.
- **Um fechamento definitivo fora do range recorde-estreito de hoje**
  (acima de 1.158,50 ou abaixo de 1.155,75) — romperia dois dias seguidos
  de consolidação e definiria direção.
- **O COT de sexta-feira (referente a 04/08) mostrar uma redução
  relevante do net long dos fundos** — indicaria que o "give-back" da
  semana de 28/07 já vinha em curso antes mesmo da consolidação técnica
  destes dois últimos pregões.
- **O câmbio (PTAX) trazer um carimbo novo com movimento relevante** —
  a paridade de hoje está calculada sobre um dado de ontem; um USD/BRL
  materialmente diferente mudaria a leitura de paridade retroativamente.
- **O WASDE finalmente voltar a ser publicado** (28 dias de atraso) —
  seria o primeiro dado fundamental fresco de oferta/demanda americana em
  quase um mês.

### Leitura operacional — soja

Para quem opera os dois lados, dois dias seguidos de amplitude comprimida
(13,00 pontos ontem, 2,75 hoje) sugerem que o mercado está em compressão de
volatilidade, não em tendência — historicamente, esse tipo de padrão
antecede um movimento mais amplo quando o catalisador aparece, mas não dá
para prever a direção a partir da compressão em si. O range de hoje
(1.155,75-1.158,50) é a referência mais próxima de suporte/resistência para
a abertura de amanhã, com o range de ontem (1.148,75-1.161,75) como
referência secundária mais ampla. Para quem acompanha o físico brasileiro,
a manchete de máxima do ano em Mato Grosso — ainda sem número — é um sinal
para buscar confirmação direta na praça antes de qualquer decisão de
originação: se verdadeira, reforça a tese de prêmio físico elevado já
documentada em 05/08 (+10,94% sobre a paridade teórica); a leitura
operacional recomendada é usar o basis prático do dono, não a paridade
CBOT×PTAX pura, para decisões desta semana, dado que o PTAX usado no cálculo
está defasado em um dia.

---

## Farelo

**Viés: bear estrutural, mas com um sinal tático que hoje contradiz
diretamente a tese — o ratio Far/Soj subiu, não comprimiu, e o motor foi
genuinamente o farelo (mais firme) e a soja (mais fraca) ao mesmo tempo.**
Trata `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
(fila de hoje) e `release-nopa-2026-08-06` (fila de hoje, mesma barreira de
sempre, ver abaixo). Fechamento: 311,00 USD/short ton (CBOT, ticker
ZMU26.CBT, 2026-08-06).

### O D+7 chega a 50 dias vencido — e hoje o farelo entrega o sinal oposto ao de ontem

A tese original ([[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]])
apostava que a compressão rápida do ratio em junho (83,3%→81,4% em 4
pregões) levaria à zona comprimida (<80%) "em 1-2 semanas". O checkpoint
formal (D+7) caiu em 18/06/2026; hoje, 07/08/2026, são **50 dias corridos**
sem confirmação do fechamento abaixo de 80% — dois dias a mais que os 48
registrados na leitura de ontem. **O que muda hoje é que o sinal se inverte
de forma igualmente genuína ao de ontem, mas na direção oposta.** Ontem
(05/08), o ratio comprimiu de 80,96% para 80,47% porque o farelo caiu mais
que a soja — pela primeira vez em três sessões, um movimento "pelo motivo
certo" (segundo a tese original, que prevê o farelo perdendo valor relativo
por "sobra"). **Hoje o movimento se inverte, e pelo motivo simétrico:** o
farelo subiu +0,10% (310,70→311,00) enquanto a soja caiu -0,06%
(1.158,25→1.157,50) — os dois lados do ratio se moveram na direção que
**afasta** o farelo da zona "abundante", elevando o ratio de 80,47% para
**80,60%** (indicators, 2026-08-06), uma alta de +0,13 ponto percentual.
Isso não invalida a tese estrutural de longo prazo (o Índice de Sobra de
Farelo permanece em 80/100 e as projeções ABIOVE de exportação em queda
seguem intactas, ver abaixo), mas é uma contraprova tática direta ao sinal
de ontem — a recomendação desta leitura é a mesma reforçada: **um único
pregão em qualquer direção não confirma tendência**; o padrão dos últimos
três dias (soja-liderado em 03-04, farelo-liderado a favor da tese em 05,
farelo-liderado contra a tese em 06) mostra um ratio genuinamente
bidirecional no curto prazo, sem uma sequência consistente. O próximo marco
formal continua sendo o D+90 (2026-09-09, a 33 dias de hoje).

### O que sustenta a leitura de hoje

**A crush margin estabilizou, revertendo a queda mais acentuada de ontem.**
Crush margin de **2,703 USD/bushel** (farelo 311,00 + óleo 67,60 − soja
1.157,50), praticamente igual a ontem (2,7043, **-0,05%**) — depois da
queda de -3,21% registrada de 04/08 para 05/08. **Mecanismo:** hoje farelo
subiu e óleo caiu, mas a soja também caiu — os três movimentos
aproximadamente se cancelam no cálculo da margem, resultando em
estabilidade. 2,703 USD/bu segue **folgada** frente ao nível de alerta
histórico (<2,50 USD/bu) — a esmagadora não tem, pelo indicador CBOT, sinal
de que precise reduzir ritmo de esmagamento por aperto de margem (contraste
com a leitura de margem *doméstica* discutida na seção Soja).

**O oil-meal spread recuou -3,57%, de 0,616 para 0,594 USD/bushel — a queda
mais acentuada desta pequena série recente.** O oil share também cedeu, de
52,16% para **52,08%** (indicators, 2026-08-06) — uma queda pequena em
termos absolutos (-0,08 ponto percentual), mas na mesma direção do
oil-meal spread. **Mecanismo:** como o óleo caiu (-0,21%) e o farelo subiu
(+0,10%) no mesmo pregão, o valor relativo capturado pelo óleo dentro do
crush encolheu e o do farelo cresceu — o oposto exato do padrão que
sustentaria a tese "óleo manda, farelo sobra" no curto prazo. Isso é
coerente com o movimento do ratio Far/Soj (mesmo mecanismo, ângulos
diferentes) e reforça que hoje foi, tecnicamente, um dia de farelo
relativamente forte dentro do complexo — mesmo que as métricas estruturais
de mais longo prazo (ISF, ABIOVE) não tenham se movido.

**O Índice de Sobra de Farelo (ISF) permanece em 80/100 (4 de 5 condições
estruturais) pelo oitavo pregão consecutivo** (30/07 a 06/08, todos com o
mesmo valor). As projeções ABIOVE seguem mostrando a exportação de farelo
brasileiro caindo de 1.400 mil toneladas em agosto/2026 para 700 mil
toneladas em dezembro/2026, uma queda de -50% em quatro meses (ABIOVE
projeções mensais, sem alteração frente ao dump anterior) — e, pela
primeira vez nesta leitura, vale registrar também o esmagamento mensal
projetado: 2.827 mil t em setembro caindo para 2.204 mil t em dezembro
(ABIOVE, -22% no período), um recuo estrutural na oferta de farelo (e de
óleo) que se soma à queda de exportação como driver de mais longo prazo,
descolado do ruído tático diário do ratio.

**Prêmio de exportação em Paranaguá segue sem carimbo novo hoje** — a
última leitura permanece em 2026-08-04 (+0,05 USD/short ton, "mês
Agosto/26"), agora com **três dias corridos** sem atualização. **Mecanismo,
sem mudança:** um prêmio de exportação perto de zero por semanas seguidas
significa que o mercado externo não paga o suficiente acima do preço
doméstico para justificar direcionar farelo brasileiro para o porto — o
farelo fica represado internamente, pressão estrutural de baixa que reforça
o mecanismo por trás do ISF, independente do vaivém tático do ratio.

**As praças físicas de farelo no Brasil (NAG) não trouxeram carimbo novo
hoje** — o último dado disponível segue sendo o de 2026-08-05: Mato
Grosso/IMEA congelado em R$ 1.675,10/ton desde 31/07, Rondonópolis/MT
congelado em R$ 1.700,00/ton desde 31/07, e o Rio Grande do Sul no salto de
R$ 1.640,00→1.800,00/ton registrado ontem, ainda **sem uma segunda leitura
de confirmação**. Como esta série já vinha recomendando, um único pregão
pós-congelamento de sete dias não é suficiente para tratar R$ 1.800,00/ton
como o novo preço de referência — hoje, sem dado físico novo de nenhuma
praça, essa recomendação permanece inalterada e sem progresso.

**`release-nopa-2026-08-06` (fila de hoje) sinaliza novo carimbo, mas o
`monthly_status` permanece em 0,0 bool** — mesma barreira de assinatura
paga documentada desde meados de junho, agora mais de 8 semanas sem
alternativa de dado primário sobre o crush americano. Tratado como item da
fila resolvido (sem conteúdo novo para incorporar), não como pendência de
leitura.

### O que invalida / risco para o farelo

- **O ratio Far/Soj confirmar a alta de hoje amanhã** — se o farelo seguir
  subindo relativo à soja por mais de uma sessão, a leitura precisaria
  reconsiderar a força tática do viés bear-farelo, mesmo com o pano de
  fundo estrutural (ISF, ABIOVE) inalterado.
- **O salto do físico no RS (R$ 1.640→1.800/ton) se confirmar com um
  segundo carimbo** no mesmo patamar — validaria uma correção real de
  represamento, não uma anomalia de coleta.
- **O prêmio de exportação em Paranaguá sair de zero** depois de mais de
  um mês parado — mudaria o cálculo de competitividade externa que
  sustenta o ISF.
- **A manchete de "indústria enfrenta desafios" em Mato Grosso se traduzir
  em redução de ritmo de esmagamento local** — reduziria a oferta de
  farelo na origem, um vetor altista que hoje só existe como hipótese
  qualitativa, sem número.
- **A crush margin cair de forma mais persistente** rumo ao nível de
  alerta (<2,50 USD/bu) — reduziria o incentivo da esmagadora a manter
  ritmo de esmagamento.

### Leitura operacional — farelo

Para quem monitora o ratio Far/Soj como gatilho tático, o movimento de hoje
é um lembrete direto de por que esta série insiste em exigir confirmação de
múltiplas sessões: ontem o farelo liderou a compressão "pelo motivo certo",
hoje ele liderou a reversão com igual nitidez mecânica — os dois dias juntos
mostram um ratio tecnicamente limpo (sem artefato de denominador), mas
bidirecional. A recomendação operacional não muda: aguardar uma sequência
de mais de um pregão na mesma direção antes de tratar qualquer nível como
sinal robusto para posições de convergência. Para quem opera o físico de
farelo no RS, a ausência de dado novo hoje mantém a mesma recomendação de
ontem — não tratar R$ 1.800,00/ton como preço de mercado confirmado sem uma
segunda leitura. Para quem opera o oil-meal spread ou o crush como posição
relativa, a queda de -3,57% no spread hoje (e o oil share recuando 0,08pp)
é o dado mais consistente do dia a favor de uma posição tática de farelo
relativamente mais forte — mas, dado o tamanho pequeno do movimento em
termos absolutos, não é ainda um sinal para posição de convicção alta.

---

## Óleo

**Viés: bear estrutural com a quebra técnica confirmada e a inversão de
curva se aprofundando — sexto pregão ou mais seguido abaixo do suporte
72,00, agora com a curva futura em backwardation por dois pregões seguidos
e o spread entre pontas se alargando.** Trata
`alerta-quebra_suporte-oleo_cbot-2026-08-06` (fato: 67,60 vs nível 72,00).
Fechamento: 67,60 cts/lb (CBOT, ticker ZLU26.CBT, 2026-08-06).

### O que sustenta a tese

**O óleo fechou perto da mínima do dia, num candle de viés vendedor claro
mesmo com range pequeno.** Abertura 67,75, máxima **67,89**, mínima 67,57,
fechamento **67,60** — um candle que fecha a apenas **9,4% do range**
((67,60-67,57)÷(67,89-67,57)), o fechamento proporcionalmente mais fraco
desta série de leituras recentes: o mercado testou a máxima cedo e devolveu
quase tudo, fechando a 0,03 cts/lb da mínima do dia. Em nível, **67,60 está
-6,11% abaixo do suporte técnico de 72,00** que a fila de julgamento
monitora desde 31/07 — a distância aumentou frente a ontem (-5,92%,
calculada sobre o fechamento de 67,74). Nenhum dos fechamentos desta janela
recente rompeu a mínima de 07/31 (67,26), então esta não é uma mínima
absoluta do período, mas é a continuação de uma tendência de baixa que
começou em 68,79 (03/08) e já soma três sessões seguidas de queda.

**A curva futura, que ontem virou backwardation pela primeira vez nesta
série, aprofundou a inversão hoje — e o mecanismo por trás do
aprofundamento é revelador.** Os fechamentos por vencimento hoje: Q26
(ago/26) 67,85, U26 (set/26) 67,60, V26 (out/26) 67,30, Z26 (dez/26) 67,06,
F27 (jan/27) 67,00, H27 (mar/27) 66,88 — sequência decrescente e regular,
igual à de ontem em formato. O spread entre a ponta curta (Q26) e a ponta
longa (H27) abriu de **0,82 para 0,97 cts/lb** (+18,3% de aprofundamento).
**O que este dado acrescenta à leitura de ontem é a origem do movimento:**
comparando ponto a ponto com a curva de ontem (Q26 67,86, U26 67,74, V26
67,46, Z26 67,22, F27 67,12, H27 67,04), o contrato mais próximo (Q26) ficou
essencialmente parado (67,86→67,85, -0,01), enquanto o mais distante (H27)
caiu 0,16 (67,04→66,88) — e os vencimentos intermediários caíram em
progressão (U26 -0,14, V26 -0,16, Z26 -0,16, F27 -0,12). **Mecanismo:** a
backwardation de ontem poderia, em tese, refletir um aperto genuíno de
curto prazo (o mercado pagando mais pelo óleo disponível agora). O padrão
de hoje sugere outra leitura, complementar: o que está se movendo não é a
ponta curta subindo (o que reforçaria a leitura de aperto imediato), mas
sim a ponta longa cedendo — ou seja, o mercado está descontando cada vez
mais o óleo entregue daqui a 6-7 meses (fev/mar 2027) relativo ao de hoje.
Isso é mais consistente com uma expectativa de mais oferta ou mais pressão
regulatória chegando nos meses seguintes (por exemplo, a centralização
Danantara da exportação de palma indonésia, com alvo de assunção plena em
01/09/2026, a 25 dias de hoje — ver Lente fiscal) do que com um aperto de
disponibilidade imediata. As duas leituras não são excludentes, mas o dado
de hoje pesa mais para a segunda.

**A margem de biodiesel americana subiu, mas o dado que a sustenta segue
sob suspeita — hoje por dois motivos distintos, ver Honestidade.** O custo
(lado óleo) caiu para **5,07 USD/galão** (-0,21%, acompanhando a queda do
óleo CBOT). A receita caiu para **6,9341 USD/galão** (-0,08%), porque o
heating oil (HO=F) fechou em **3,7691 USD/galão**, **-0,15%** sobre o
fechamento de ontem (3,7749, conforme o próprio dump de hoje). O resultado
é a margem de biodiesel subindo para **1,0641 USD/galão**, **+0,44%** sobre
ontem (1,0594) — a margem sobe porque o custo caiu proporcionalmente mais
que a receita, não porque a receita melhorou. O volume do heating oil hoje
é de **234 contratos**, uma melhora expressiva frente aos 45 contratos
citados na leitura de ontem para a sessão anterior — mas, como o campo de
abertura do heating oil de hoje (3,7924) é idêntico, casa decimal por casa
decimal, ao valor registrado sob o carimbo "2026-08-05" neste mesmo dump
(ver Honestidade), esta leitura trata a melhora de volume com reserva, não
como confirmação de normalização de liquidez.

**O Índice de Suporte do Óleo (ISO) permanece em 100/100 (5 de 5 condições)
pelo oitavo pregão consecutivo** (30/07 a 06/08, todos com o mesmo valor) —
a tese estrutural (óleo dominando o valor do crush) segue formalmente
intacta, mesmo com o oil share tendo recuado ligeiramente hoje (52,16%→
52,08%, ver seção Farelo). Como já observado em leituras anteriores, o ISO
mede quem captura mais valor dentro do crush, não se o preço está caro ou
barato frente a um nível técnico — as duas leituras (ISO no máximo, preço
em tendência de baixa, curva cada vez mais invertida) coexistem sem se
contradizer tecnicamente.

**As projeções ABIOVE de exportação de óleo brasileiro reforçam a leitura
de oferta represada no mercado interno.** Exportação de óleo caindo de 110
mil toneladas em setembro/2026 para 45 mil em outubro e 21 mil em
novembro/2026 — uma queda de -80% em dois meses (ABIOVE projeções mensais,
sem alteração frente ao dump anterior). **Mecanismo:** menos óleo saindo
para exportação significa mais óleo represado no mercado doméstico
brasileiro — um vetor que, no médio prazo, pressiona o basis físico interno
para baixo (mesmo mecanismo estrutural do ISF para o farelo, mas do lado do
óleo), reforçando o quadro de pressão baixista de mais longo prazo que
complementa a leitura técnica de curto prazo.

**Sem COT novo nesta janela** — o corte de 28/07/2026 segue sendo a
fotografia mais recente, mostrando os fundos com net long em óleo de
107.898 contratos (16,60% do open interest de 650.041), depois de uma
redução de -10,27% na semana anterior ao corte — a única das três pernas em
que o book especulativo já reduzia exposição comprada antes da queda de
preço das últimas sessões. O próximo corte (referente a 04/08) é esperado
por volta de hoje, sexta-feira, mas ainda não está neste briefing.

### O que invalida / risco para o óleo

- **A curva futura voltar a contango** — se os vencimentos distantes
  (Z26, F27, H27) voltarem a valer mais que os próximos, tanto a leitura
  de aperto de curto prazo quanto a de desconto de longo prazo perderiam
  sustentação, e a backwardation destes dois pregões seria tratada como
  evento isolado.
- **A ponta longa da curva (H27) parar de ceder e estabilizar** —
  interromperia o mecanismo específico identificado hoje (aprofundamento
  pelo fim da curva, não pelo início).
- **O heating oil confirmar volume genuinamente normal por mais de uma
  sessão** — validaria a melhora de hoje (234 contratos) como real, não
  como possível artefato de coleta.
- **Um fechamento consistente de volta acima de 68,55** (máxima da sessão
  de 05/08) — romperia a sequência de fechamentos fracos e abriria espaço
  para reteste do suporte de 72,00.
- **A isenção PIS/Cofins do biodiesel seguir sem renovação** — hoje é o 5º
  dia útil desde o vencimento (31/07), ainda sem confirmação (ver Lente
  fiscal).

### Leitura operacional — óleo

Para quem está vendido desde a quebra do suporte 72,00, o desenho de hoje —
fechamento a 9,4% do range (o mais fraco desta série), sexto pregão ou mais
seguido abaixo do nível, e uma curva futura cuja inversão se aprofunda pelo
enfraquecimento da ponta longa — reforça manter posição vendida tática, com
stop lógico acima de 68,55. A leitura de que o aprofundamento da
backwardation vem do fim da curva, não do início, é operacionalmente
relevante para quem opera spreads de calendário: um spread que se abre
porque a ponta longa cede (não porque a ponta curta sobe) favorece
estruturas que vendem os vencimentos mais distantes contra os próximos
(vende F27/H27, compra Q26/U26) apostando que o desconto de longo prazo
persista ou se aprofunde, o inverso da leitura que faria sentido se o
movimento fosse liderado pela ponta curta. Para quem considera nova posição
comprada, a recomendação segue reforçada: **não tratar a margem de
biodiesel calculada hoje como número confiável** — mesmo com o volume do
heating oil aparentemente melhorando (234 vs 45 contratos), a coincidência
exata entre o valor de abertura de hoje e o valor registrado sob o carimbo
de ontem neste mesmo dump é motivo concreto para ceticismo adicional (ver
Honestidade), não para alívio.

---

## Spreads e crush (leitura de complexo)

**Ratio Far/Soj: 80,60% (06/08), alta de +0,13pp sobre ontem — reversão
direta da compressão de 05/08, com o mesmo grau de "limpeza" mecânica (os
dois lados do ratio se movendo na mesma direção), só que no sentido
oposto.** Como discutido na seção Farelo, isso não invalida a tese
estrutural do D+7/D+90, mas reforça que o ratio, no curto prazo, é
genuinamente bidirecional — a recomendação operacional permanece: exigir
confirmação por mais de uma sessão seguida na mesma direção antes de tratar
qualquer nível como sinal robusto.

**Crush margin: 2,703 USD/bu, -0,05% sobre ontem — estabilizou depois da
queda de -3,21% do pregão anterior.** Farelo (receita) subiu, óleo
(receita) e soja (custo) caíram — o resultado líquido é uma margem
praticamente inalterada, ainda folgada acima do nível de alerta (<2,50
USD/bu).

**Oil share: 52,08%, recuo de -0,08pp sobre ontem (52,16%) — a maior
variação diária desta métrica em várias sessões**, ainda que pequena em
termos absolutos. Consistente com o óleo perdendo valor relativo ao farelo
no crush hoje, na mesma direção do ratio Far/Soj e do oil-meal spread.

**Oil-meal spread: 0,594 USD/bu, -3,57% no dia — a queda mais acentuada
desta pequena série recente**, reforçando que hoje foi, tecnicamente, um
dia de farelo relativamente mais forte e óleo relativamente mais fraco
dentro da divisão de valor do crush.

**Heating oil: fechamento de 3,7691 (-0,15%) com volume de 234 contratos —
melhora expressiva frente aos 45 contratos da sessão anterior, mas com uma
ressalva de qualidade de dado que reduz a confiança nessa leitura de
melhora (ver Honestidade).** A leitura técnica das três pernas principais
(soja, farelo, óleo) segue sólida pelos fechamentos, que batem com o cálculo
independente da seção `indicators`; a leitura de volumes e máximas/mínimas
de hoje, especialmente para farelo, não.

**ISF em 80/100, ISO em 100/100 — ambos inalterados pelo oitavo pregão
seguido.** Nenhum insumo estrutural novo entrou no cálculo hoje, mas as
projeções ABIOVE de esmagamento mensal (2.827 mil t em setembro caindo para
2.204 mil t em dezembro, -22%) reforçam o pano de fundo de menor oferta
futura de farelo e óleo no Brasil, um driver de mais longo prazo que
complementa esses índices sem alterá-los diretamente.

**A curva futura do óleo aprofundou a backwardation pelo segundo pregão
seguido, enquanto soja e farelo seguem em contango regular (apenas com
deslocamento paralelo de nível, sem mudança de formato).** Esta é a
divergência estrutural mais persistente desta pequena série de leituras —
duas sessões já é mais do que a série exigia para tratar como "sinal a
acompanhar de perto" em vez de evento isolado, mas ainda não é suficiente
para uma tese de convicção alta sobre a causa (aperto de curto prazo vs.
desconto de longo prazo — ver seção Óleo).

**O que os índices dizem juntos hoje:** o complexo teve uma sessão de
sinais mistos e, em certo sentido, mutuamente contraditórios entre farelo e
óleo — o farelo mostrando força relativa tática (ratio subindo, oil share
caindo, oil-meal spread caindo) no mesmo pregão em que o óleo aprofunda sua
fraqueza técnica e sua inversão de curva. As métricas estruturais (ISF,
ISO, ABIOVE) seguem, pelo oitavo pregão, inalteradas — capturam dinâmicas
de mais longo prazo que um dia de movimento tático não altera. A leitura
mais honesta é que hoje foi um dia de "ruído direcionalmente coerente
dentro do crush" (farelo para cima, óleo para baixo, ambos batendo no ratio
e no oil-meal spread na mesma direção), mas que ainda não tem confirmação
de mais de uma sessão para ser tratado como mudança de regime.

---

## Lente fiscal e regulatória BR

**Isenção PIS/Cofins do biodiesel (`PISCOFINS-BIODIESEL-ISENCAO`,
`vigencia_ate` 2026-07-31) — hoje, 2026-08-07, é o 5º dia útil de
expediente público desde o vencimento** (03/08 seg = 1º, 04/08 ter = 2º,
05/08 qua = 3º, 06/08 qui = 4º, 07/08 sex = 5º). O RSS de hoje trouxe
apenas 4 itens mantidos, nenhum sobre este tema específico — a lacuna de
confirmação persiste, agora há uma semana útil inteira. **Mecanismo e
leitura, sem mudança frente às últimas sessões:** se a isenção caducou sem
renovação, o custo de produção do biodiesel brasileiro sobe, reduzindo a
competitividade do biodiesel dentro do mix mandatório e pressionando a
demanda de óleo de soja como insumo doméstico — vetor bearish direto para o
óleo, e um candidato a explicar (parcialmente) por que a ponta longa da
curva do óleo está cedendo mais que a curta (ver seção Óleo): se o mercado
já espera esse custo mais alto pesando sobre os meses seguintes, isso
apareceria primeiro nos vencimentos mais distantes, exatamente o padrão
observado hoje. Com o monitor tributário (`system/tributario_watch.toml`)
parado desde 2026-06-05 (**63 dias sem atualização**), esta leitura segue
sem poder confirmar nem descartar a caducidade — mantém-se como o item de
verificação manual mais urgente desta janela, agora no 5º dia útil.

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L) —
vigência formal venceu há 27 dias** (`vigencia_ate` 11/07/2026), sem
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
que favoreceria óleo de soja doméstico americano frente a insumo importado,
pendente de regra final do Treasury/IRS); DANANTARA-INDONÉSIA
(centralização estatal da exportação de palma, assunção plena prevista para
01/09/2026, agora a **25 dias**); INDONESIA-B50 (provável B45 em 2026, B50
pleno só 2027-28); INDONESIA-LEVY-PMK9 (imposto de exportação de CPO até
12,5%, encarecendo palma). Conjunto estruturalmente bullish para óleo de
soja via substituição de palma, mas inverificável pelo lado de mercado
(MPOB inacessível, ver Honestidade) — e em tensão direta com a
backwardation observada na curva do óleo, cuja ponta longa (justamente os
vencimentos que incluiriam o período pós-assunção plena da Danantara) está
cedendo, não subindo — o mercado, pelos dados de curva disponíveis, ainda
não está precificando esse suporte estrutural.

**O monitor tributário como um todo está há 63 dias sem qualquer
atualização** — prioridade de manutenção do sistema, especialmente
relevante agora que a isenção PIS/Cofins completa uma semana útil vencida
sem confirmação de status.

---

## Riscos e eventos próximos

**O COT (CFTC) referente a 04/08/2026 é esperado por volta de hoje,
sexta-feira 07/08, mas ainda não está neste briefing** — será o primeiro
dado de posicionamento fresco em 10 dias, e vai mostrar como os fundos
reagiram à consolidação técnica dos últimos pregões e ao give-back
documentado desde 28/07.

**A manchete de máxima do ano na soja em Mato Grosso precisa de um número
verificável** — hoje ela entra na leitura apenas como headline qualitativo;
buscar confirmação em fonte primária (CEPEA/IMEA/consultoria) antes de
tratar como driver quantitativo.

**O ratio Far/Soj subiu de volta para 80,60% depois de comprimir ontem —
monitorar se a reversão de hoje se confirma amanhã** (o que enfraqueceria
ainda mais a tese do D+7, agora a 50 dias vencida) ou se é apenas um
soluço de um dia dentro de uma tendência de compressão mais lenta.

**A backwardation da curva do óleo aprofundou pela segunda sessão seguida,
com o mecanismo específico de hoje sendo a ponta longa cedendo** — dois
dias já justificam acompanhamento diário mais próximo: se a ponta curta
começar a subir também, reforça leitura de aperto imediato; se a ponta
longa continuar cedendo sozinha, reforça leitura de desconto de expectativa
futura (biodiesel BR, palma asiática).

**O suporte técnico do óleo (72,00) segue rompido, agora a -6,11%** — a
reabertura de segunda-feira é o próximo teste.

**O heating oil melhorou em volume (234 vs 45 contratos), mas com uma
ressalva de qualidade de dado que impede tratar isso como confirmação de
liquidez normal** — ver Honestidade.

**A isenção PIS/Cofins do biodiesel completa o 5º dia útil sem
confirmação de status** — item de verificação manual mais urgente desta
janela, agora uma semana útil inteira vencida.

**O salto do físico de farelo no RS (R$ 1.640→1.800/ton) segue sem segunda
leitura de confirmação** — nenhuma praça física trouxe carimbo novo hoje.

**O USDA Crop Progress rotulado 2026-08-02 segue com os MESMOS valores do
corte de 26/07** (ver Honestidade), agora pela quarta leitura seguida; o
próximo corte, referente à semana de 09/08, deve sair na segunda-feira
seguinte (10/08).

**NOPA — fila `release-nopa-2026-08-06` sinaliza novo "release", mas o
dado segue inacessível**, agora mais de 8 semanas sem alternativa de dado
primário sobre o crush americano.

**MPOB — sem números de palma extraídos, mesma barreira de longa data.**

**O WASDE segue fora da janela deste briefing, agora 28 dias de atraso**
desde o último dado (10/07/2026).

**Danantara (Indonésia) assume plenamente a cadeia de exportação de palma
em 01/09/2026, a 25 dias de hoje** — monitorar se a curva do óleo CBOT
começa a precificar esse suporte estrutural, especialmente na ponta longa,
que hoje está se movendo na direção oposta.

---

## Honestidade

O que não foi possível validar neste briefing de 2026-08-06 (lido em
2026-08-07), e os pontos onde a confiança é baixa:

**1. Achado concreto de qualidade de dado: os campos de máxima, mínima e
volume do farelo CBOT para 2026-08-06 são idênticos, casa decimal por casa
decimal, aos mesmos campos registrados sob o carimbo "2026-08-05" neste
mesmo dump** (maxima 311,29998779296875, minima 310,3999938964844, volume
236,0 — os três valores batem exatamente entre as duas datas). O campo de
abertura também é idêntico entre as duas datas (310,79998779296875); apenas
o fechamento difere genuinamente (311,00 vs 310,70001220703125). O mesmo
padrão aparece no heating oil: a abertura de hoje (3,7923998832702637) é
idêntica à abertura registrada sob "2026-08-05" neste dump. **Esta leitura
trata isso como evidência concreta de um provável problema de pipeline
(dado de máxima/mínima/volume/abertura carregado de uma sessão anterior sem
atualização, não uma coincidência de mercado)** — os fechamentos, que
batem de forma independente com os valores usados na seção `indicators`
(farelo 311,00, óleo 67,60, soja 1.157,50), são tratados como confiáveis;
as máximas, mínimas e volumes de farelo e heating oil de hoje, não.
Recomenda-se verificação técnica direta da fonte (`main.py` / scraper CME).

**2. Os volumes de farelo, óleo, soja e heating oil informados neste dump
para as sessões de 05-06/08 (236, 593, 384 e 234 contratos,
respectivamente) são uma a duas ordens de grandeza menores que os volumes
citados na leitura de 05/08 para a mesma sessão de 05/08 (farelo 25.064,
óleo 21.090, soja 18.818 contratos).** Combinado com o achado do item 1,
esta leitura não usa os volumes de hoje como sinal de convicção técnica ou
de liquidez, ao contrário do padrão adotado em leituras anteriores — a
magnitude da diferença é grande demais para ser tratada como ruído normal,
e pequena demais em evidência direta para afirmar uma causa específica
(mudança de fonte, campo diferente, sessão parcial). Recomenda-se
verificação técnica.

**3. O prêmio de exportação de Paranaguá (soja) e o CEPEA Paraná interior
não trouxeram carimbo novo em 2026-08-06** — a comparação apples-to-apples
que foi possível em 05/08 (ambos os números do mesmo dia) não está
disponível hoje; qualquer menção ao prêmio físico nesta leitura parte do
último carimbo (05/08), não de um dado do dia.

**4. O salto do físico de farelo no Rio Grande do Sul (R$ 1.640,00/ton →
R$ 1.800,00/ton, registrado em 05/08) segue sem uma segunda leitura de
confirmação** — nenhuma praça física trouxe carimbo novo hoje, então esta
leitura não pode nem confirmar nem descartar o nível como represamento
resolvido ou anomalia de coleta.

**5. A manchete "Soja em Mato Grosso atinge maior preço do ano, mas
indústria enfrenta desafios" (Canal Rural, 06/08/2026) veio apenas como
título no RSS, sem corpo de texto, número ou metodologia neste briefing**
(campo `headline: None`). Esta leitura trata a manchete como um dado
qualitativo, com fonte e data, mas não tem como verificar o nível de preço
citado nem o que especificamente a "indústria" está enfrentando.

**6. O PTAX (BCB) não trouxe carimbo novo para 2026-08-06** — a paridade
em reais calculada hoje usa o câmbio de 2026-08-05 (5,1154 BRL/USD); um
movimento cambial genuíno de hoje, se houve, não está capturado neste
número.

**7. A curva futura do óleo aprofundando a backwardation, com o mecanismo
específico (ponta longa cedendo mais que a ponta curta), é tratada nesta
leitura como um dado técnico observável (todos os seis vencimentos vêm do
mesmo dump de 2026-08-06), mas a interpretação causal proposta — ligação
com incerteza regulatória de biodiesel BR ou expectativa de mais oferta de
palma via Danantara — é uma hipótese desta leitura, não um fato confirmado
por nenhuma fonte do briefing.** Nenhum dado de palma (MPOB bloqueado) ou
de biodiesel BR (monitor tributário parado) permite confirmar essa hipótese
diretamente.

**8. O ratio Far/Soj (80,60%) segue sem fechar abaixo de 80%, agora 50 dias
depois do checkpoint formal do D+7 (18/06/2026), e hoje se moveu na direção
CONTRÁRIA à tese.** Esta leitura não conclui que a tese original foi
invalidada — apenas que o sinal de hoje é uma contraprova tática tão
genuína quanto o sinal a favor de ontem, e mantém o D+90 (2026-09-09) como
próximo marco formal.

**9. O USDA Crop Progress rotulado 2026-08-02 trouxe, pelo quarto dump
seguido, valores idênticos ao corte de 26/07/2026 (11%/52%/7%).** Esta
leitura não trata isso como quatro semanas genuinamente estáveis de
condição de lavoura, e reforça a recomendação de reconferir no próximo
corte esperado (semana de 09/08, publicação em torno de 10/08).

**10. A isenção PIS/Cofins do biodiesel — sem confirmação de renovação ou
caducidade neste briefing, agora no 5º dia útil desde o vencimento.** O
monitor tributário está 63 dias sem atualização; esta leitura não presume
nenhum dos dois cenários.

**11. O WASDE permanece completamente fora da janela deste briefing** —
agora 28 dias de atraso desde o último dado (10/07/2026).

**12. NOPA (`release-nopa-2026-08-06`) segue com `monthly_status` em 0,0
bool** — mesma barreira de assinatura paga, mais de 8 semanas sem
alternativa de dado primário.

**13. Palma malaia (MPOB) segue sem números extraídos**, mesmo conteúdo de
3.439 caracteres.

**14. O COT (CFTC) de 28/07/2026 segue sendo o dado de posicionamento mais
recente** — nenhum corte novo nesta janela; o próximo, referente a
04/08/2026, é esperado por volta de hoje. Percentis históricos de COT não
foram calculados (mesma limitação de leituras anteriores).

**15. Clima INMET (BR) não foi usado como driver de preço** — agosto é
entressafra da soja brasileira, sem relevância direta neste momento do
calendário agrícola, mesmo com risco de granizo sinalizado para Passo
Fundo/RS e calor seco em Mato Grosso.

**16. Os forecasts estatísticos internos (bandas 7d/30d geradas em
2026-08-06) não foram usados como driver desta leitura** — são bandas
MA20+volatilidade+slope, mecânicas (soja 7d "baixista"/30d "baixista",
farelo 7d "lateral"/30d "baixista", óleo 7d "baixista"/30d "baixista"), sem
incorporar a leitura qualitativa de hoje; ficam registradas no briefing,
mas esta leitura não as toma como fonte de tese.

*Nenhum número foi inventado ou estimado além do que consta no briefing de
2026-08-06 e nos insights anteriores referenciados. A contribuição central
desta leitura foi (1) identificar e explicar que a alta do ratio Far/Soj de
hoje é uma contraprova genuína e mecanicamente simétrica à compressão de
ontem, não um artefato — farelo mais firme e soja mais fraca no mesmo
pregão, ambos empurrando o ratio para longe da zona "abundante"; (2)
identificar que o aprofundamento da backwardation do óleo hoje foi liderado
pela ponta longa da curva cedendo, não pela ponta curta subindo, uma
distinção mecânica relevante para a leitura de aperto de curto prazo vs.
desconto de expectativa futura; (3) identificar e documentar, com evidência
numérica concreta (valores idênticos casa decimal por casa decimal entre
carimbos de datas diferentes no mesmo dump), um provável problema de
qualidade de dado nos campos de máxima/mínima/volume do farelo e na
abertura do heating oil, reduzindo a confiança nesses campos específicos
sem descartar os fechamentos, que permanecem consistentes com o cálculo
independente da seção `indicators`; (4) sinalizar a manchete de máxima do
ano na soja em Mato Grosso como um mecanismo plausível para explicar a
tensão entre crush margin de papel (CBOT) e margem real de esmagamento
doméstica, sem inventar o número que a manchete não forneceu; e (5) tratar
os três itens da fila de julgamento de hoje —
`alerta-quebra_suporte-oleo_cbot-2026-08-06`,
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` e
`release-nopa-2026-08-06` — no contexto específico desta sessão, sem
inventar tonelagem, confirmação ou percentil que o briefing não trouxe.*
