---
data: 2026-07-21
titulo: "Ratio Far/Soj volta para 80,3% (zona neutra) e desfaz em um único pregão a confirmação tática do farelo de ontem, enquanto a soja devolve -0,43% do rally mas segue 2,56% acima da resistência 1.180,00, e o óleo tem o segundo fechamento fraco seguido com a margem de biodiesel comprimindo -4,59%"
tags: [complexo, auto-claude]
fontes:
  - CBOT CME (ZSU26 soja / ZMU26 farelo / ZLU26 óleo + curva forward Q26-H27) — sessão de 2026-07-21
  - CME heating_oil_cbot (HO=F) — fechamento de 2026-07-21 (4,041 USD/galão, volume de apenas 26 contratos)
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, paridade BR, ISF, ISO) — 2026-07-21, com comparação contra os mesmos indicadores de 2026-07-20
  - BCB PTAX — 2026-07-21 (USD/BRL 5,078, EUR/BRL 5,793)
  - CEPEA/ESALQ Paranaguá e Paraná interior via NAG — 2026-07-21 (suporte Paranaguá R$ 144,17/saca, var +1,07%; Paraná interior R$ 136,77/saca, var +0,77%)
  - NAG Físico BR (farelo MT/IMEA, RS, Rondonópolis; prêmios export PGUA farelo/óleo) — 2026-07-21
  - CFTC COT Managed Money — ainda referência 2026-07-14, sem atualização (hoje, 21/07, é o próprio dia de corte semanal; publicação normal ~24/07)
  - USDA Crop Progress — ainda 2026-07-19 (13% excelente + 53% boa + 6% ruim = 66% bom-ou-excelente), sem nova publicação
  - USDA WASDE — ainda 2026-07-10 (só farelo Argentina/Brasil/China parcial), sem publicação nova
  - NOPA — 2026-07-21, `monthly_status` continua inacessível (paywall), fila `release-nopa-2026-07-21`
  - ABIOVE projeções mensais — balanços ago-dez/2026 (farelo/óleo/soja), sem alteração frente às leituras anteriores
  - NOAA CPC ENSO — 2026-07-21 (El Niño Advisory, sem mudança)
  - MPOB — 2026-07-21 (parser sem números extraídos, 3.439 caracteres, 12º dia consecutivo com o mesmo conteúdo, 10/07 a 21/07)
  - BCBA — 2026-07-21 (acessível, sem links de relatório detectados, mesmo padrão)
  - Notícias Agrícolas/Canal Rural/Farm Progress RSS — 2026-07-21 (160 itens lidos, 5 mantidos; manchete "Sojicultores ainda esperam por preços melhores; negócios não andam e dia é fraco para a soja", Canal Rural)
  - Forecasts estatísticos internos — 2026-07-21 (sétima geração seguida com as seis bandas simultaneamente em viés altista)
  - system/tributario_watch.toml (lido apenas como referência, não editado) — MP-1358-2026, PIS/COFINS-BIODIESEL-ISENCAO, MP-1363-2026, STJ-RESP-2165276, B16-CNPE-2026, EPA-RFS-2026-2027, 45Z-CLEAN-FUEL, DANANTARA-INDONESIA, INDONESIA-B50, INDONESIA-LEVY-PMK9 — todos `atualizado_em` 2026-06-05 (46 dias sem atualização do monitor)
  - Cruza com [[2026-07-20_leitura-complexo]], [[2026-07-19_leitura-complexo]], [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (checkpoint D+7, tratado abaixo — hoje 33 dias vencido)
status: ativa
vies: [bull-soja, neutral-farelo, bull-oleo_soja]
---

> **Nota de proveniência:** o dump de hoje (terça-feira, 21/07/2026) tem uma
> lacuna que vale registrar antes de qualquer número: a seção bruta `cme_cbot`
> só traz os preços OHLC completos de farelo e heating oil para o dia anterior
> (20/07), sem os valores brutos de soja e óleo daquela sessão — a comparação
> de hoje contra 20/07 para essas duas pernas usa o fechamento **implícito**
> nos indicadores sintéticos (a fórmula de crush margin de 20/07, que cita
> "farelo 321,20 + óleo 73,82 − soja 1.215,50", é a única fonte pública do
> fechamento de soja daquele dia neste dump). Isso já é a **quarta versão**
> distinta do fechamento de soja de referência num intervalo de poucos dias
> (1.204,50 → 1.213,75 → 1.215,50, cada uma vinda de uma geração diferente do
> pipeline) — tratado com mais detalhe na seção Honestidade. Feita essa
> ressalva, os fatos de hoje: a soja fechou em 1.210,25 cts/bushel, devolvendo
> -0,43% frente ao fechamento implícito de ontem, mas ainda 2,56% acima da
> resistência de 1.180,00 (trata `alerta-quebra_resistencia-soja_cbot-2026-07-21`).
> O farelo, ao contrário, subiu +0,87% no dia — e é essa divergência de sinal
> entre as duas pernas (soja caindo, farelo subindo) que empurrou o ratio
> Far/Soj de volta para 80,31%, cruzando de novo para cima do limiar de 80%
> que ontem, pela primeira vez, tinha sido confirmado abaixo numa sessão real
> (trata `ratio-zona-2026-07-21` e a revisão vencida
> `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`). O óleo
> teve o segundo fechamento fraco seguido, com a margem de biodiesel
> comprimindo mais uma vez.

## Visão geral

O complexo soja é uma fábrica com uma única matéria-prima (a soja em grão) e
dois produtos de saída em proporção fixa por bushel esmagado: o **farelo**
(fração proteica, ~78% da massa, vira ração animal) e o **óleo degomado**
(fração de gordura, ~18-20% da massa, vira óleo de cozinha e biodiesel). Quem
decide o ritmo de esmagamento é a esmagadora, olhando a **crush margin**
(valor de farelo + óleo por bushel, menos o custo daquele bushel de soja,
medido na CBOT — Chicago Board of Trade, a bolsa de referência mundial para
esses contratos) e o **oil share** (fração desse valor capturada pelo óleo).
Quando o oil share sobe, o óleo passa a "pagar o crush" sozinho, e o farelo
vira, cada vez mais, um subproduto que a esmagadora aceita vender barato só
para liberar o óleo — é esse mecanismo que está por trás do **ratio Far/Soj**
(preço do farelo dividido pelo preço da soja, normalizado pela conversão
bushel↔short ton, "sht"): quando cai abaixo de 80%, o farelo está
historicamente "abundante" frente à soja e o spread tende a comprimir; quando
sobe acima de 87%, o farelo está "apertado"; entre os dois, o sistema chama
de zona "neutra". É um spread de **mean-reversion** — funciona nos dois
lados: comprimido demais tende a esticar de volta, esticado demais tende a
comprimir.

**O que aconteceu hoje é o espelho exato do mecanismo descrito na leitura de
ontem — só que invertido.** Ontem, a soja subiu mais que farelo e óleo
juntos, o que mecanicamente comprimiu o ratio Far/Soj e a crush margin (a
soja é o denominador do ratio e o custo na crush margin; quando o custo sobe
mais rápido que os produtos, os dois indicadores caem, mesmo com farelo e
óleo positivos). Hoje, o padrão se inverteu: a soja fechou em 1.210,25
cts/bushel (CBOT, sessão de 21/07/2026), uma queda de -0,43% frente ao
fechamento implícito de ontem (1.215,50), enquanto o farelo subiu para 324,00
USD/short ton (+0,87% no dia). Como o ratio mede farelo *relativo* à soja, e
a crush margin mede o valor dos produtos *menos* o custo da soja, o resultado
aritmético de "farelo sobe enquanto soja cai" é duplo e na mesma direção: o
ratio subiu (de 79,28% para 80,31%, cruzando de volta para a zona "neutra") e
a crush margin se expandiu (de 3,0316 para 3,0951 USD/bushel, +2,09%). **Isso
é exatamente o inverso do que a leitura de ontem descreveu como um sinal de
alívio estrutural para o farelo** — e é por isso que o fechamento de hoje
desfaz, num único pregão, a confirmação tática que tinha acabado de ser
validada pela primeira vez em uma sessão de mercado real. O óleo, por sua
vez, teve o segundo fechamento fraco seguido: caiu -0,62% no dia, fechando
abaixo tanto da abertura quanto do fechamento de ontem, com a margem de
biodiesel americana comprimindo mais uma vez (-4,59%, depois de -5,97% ontem)
— uma sequência de dois dias que começa a parecer menos ruído e mais um
padrão tático de fricção sobre a tese estrutural do óleo. **O que mudou
hoje:** três coisas — (1) o ratio Far/Soj voltou a cruzar acima de 80%, na
segunda sessão seguida em que o limiar é testado em direções opostas (trata
`ratio-zona-2026-07-21`); (2) a revisão D+7 da tese estrutural do farelo, já
33 dias vencida, ganha uma reviravolta relevante: o critério tático que
"tinha sido satisfeito" ontem não sobreviveu nem uma sessão (trata
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`); e (3) a
soja segue confortavelmente acima da resistência de 1.180,00 (2,56%), mesmo
devolvendo parte do ganho de ontem (trata
`alerta-quebra_resistencia-soja_cbot-2026-07-21`). **Leitura de uma linha:**
o pivô do complexo hoje é a lição de que o ratio Far/Soj, perto de um número
redondo como 80%, é um limiar ruidoso e fácil de cruzar nos dois sentidos em
sessões consecutivas — convicção moderada em soja (tese tática intacta, mas
com o primeiro dia de devolução desde o rompimento), baixa-moderada em
farelo (a tese estrutural via ABIOVE/ISF segue de pé, mas o sinal tático
virou de bear para neutro em 24 horas) e moderada em óleo (a tese estrutural
segue intacta, mas dois dias seguidos de fricção tática merecem atenção
redobrada na próxima sessão).

---

## Soja

**Viés: bull tático mantido, porém com o primeiro dia de devolução desde a
confirmação do rompimento. Fechou em 1.210,25 cts/bushel na sessão de
21/07/2026 (CBOT, ticker ZSU26.CBT, vencimento set/26), 2,56% acima da
resistência de 1.180,00. Trata `alerta-quebra_resistencia-soja_cbot-2026-07-21`.**

### O que sustenta a tese

**A vela de hoje é a primeira desde o rompimento a fechar abaixo do
fechamento anterior, mas sem quebrar nenhum nível relevante.** Abertura
1.210,00, fechamento 1.210,25 (+0,25, +0,02% no dia — essencialmente estável
frente à própria abertura), mínima 1.204,75, máxima 1.217,50, volume 25.502
contratos (CBOT, 21/07/2026). O fechamento ficou em 43,1% do range do dia
contado a partir da mínima ((1.210,25-1.204,75) ÷ (1.217,50-1.204,75)) — uma
posição de fechamento na metade inferior do range, sinal de que a sessão
começou testando a máxima (1.217,50, muito perto da abertura) e foi perdendo
força ao longo do pregão. Frente ao fechamento implícito de ontem (1.215,50
cts/bu, ver nota de proveniência sobre a origem desse número), o resultado é
uma queda de -5,25 pontos (-0,43%) — pequena, mas é o primeiro dia negativo
desde a confirmação do rompimento na sessão de 20/07. **Isso não invalida a
tese tática**: o preço segue 2,56% acima da resistência de 1.180,00 e a
mínima de hoje (1.204,75) ainda está 24,75 pontos acima desse nível — mas é o
tipo de dia que merece ser monitorado de perto na sequência, porque é o
primeiro sinal, ainda que pequeno, de que o ímpeto do rompimento pode estar
perdendo velocidade.

**A curva forward mantém o formato de "sorriso" já documentado em leituras
anteriores, mas com uma leve compressão na ponta curta.** Agosto/26 (Q26)
1.218,50 → Setembro/26 (U26, contrato de referência/spot) 1.210,25 (desconto
de -8,25, -0,68%) → Novembro/26 (X26) 1.222,25 (recupera +11,75 sobre
setembro, +0,97%) → Janeiro/27 (F27) 1.236,00 (+13,75 sobre novembro, +1,13%)
→ Março/27 (H27) 1.238,00 (+2,00 sobre janeiro, +0,16%, praticamente estável).
O desconto do contrato spot frente ao mês anterior (agosto) se aprofundou
ligeiramente (-0,68% hoje ante -0,76% ontem, mudança pequena), e o prêmio da
ponta longa (janeiro/27 sobre novembro) se manteve praticamente no mesmo
patamar (+1,13% hoje vs +1,12% ontem) — a curva, no conjunto, não mudou de
formato, só absorveu a mesma pequena devolução do spot.

**A paridade teórica em reais recuou para R$ 135,49/saca 60kg** (indicadores,
CBOT 1.210,25 cts × PTAX 5,078 USD/BRL de 21/07/2026), uma queda de -0,89
(-0,65%) frente aos R$ 136,38/saca implícitos de ontem (PTAX 5,0894). O
mecanismo cambial aqui reforça a queda em dólar: o real se apreciou
ligeiramente (USD/BRL caiu de 5,0894 para 5,078, -0,22%) no mesmo dia em que
a soja em dólar caiu -0,43% — os dois efeitos vão na mesma direção (menos
dólares por bushel, e cada dólar vale um pouco menos em reais), resultando
numa queda líquida maior na paridade (-0,65%) do que a queda isolada da soja
em dólar. **O físico de Paranaguá, porém, foi na direção contrária**: fechou
em R$ 144,17/saca (CEPEA/ESALQ via NAG, var +1,07% no dia) — um prêmio de R$
8,68/saca (+6,41%) sobre a paridade teórica, ante um prêmio de
aproximadamente 4,60% no dia anterior. **Esse é um dado relevante e que
destoa do resto da leitura de hoje**: enquanto o papel (CBOT + câmbio)
recuou, o físico do porto se esticou ainda mais para cima, alargando o
prêmio numa direção que sugere demanda física firme em Paranaguá
independente do movimento do papel — coerente com a notícia do dia (Canal
Rural, 21/07/2026: "Sojicultores ainda esperam por preços melhores; negócios
não andam e dia é fraco para a soja"), que descreve produtores segurando a
soja na esperança de preços melhores, reduzindo a oferta disponível no
mercado físico justamente no dia em que o papel cede. **Nota de honestidade
sobre este número:** como o próprio fechamento de soja de ontem usado como
base já passou por múltiplas revisões (ver Honestidade), a comparação exata
do tamanho do prêmio entre os dois dias deve ser tratada com cautela; o sinal
qualitativo (físico resistindo mais que o papel) é o que fica.

**A soja no Paraná interior (CEPEA/ESALQ via NAG) fechou em R$ 136,77/saca**
(var +0,77% no dia), um prêmio de +R$ 1,28 (+0,94%) sobre a paridade teórica
de R$ 135,49/saca — dentro da faixa normal de custo logístico entre o
interior e o porto, sem sinal de estresse ou aperto na base doméstica além do
já visto no prêmio de Paranaguá.

**O USDA Crop Progress segue parado em 19/07/2026** (13% excelente + 53% boa
+ 6% ruim = 66% bom-ou-excelente), sem atualização nova desde a leitura de
ontem. A próxima publicação semanal é esperada por volta de 26/07/2026.

**O COT (CFTC) permanece com o mesmo dado de referência, 14/07/2026.**
Managed money net long em soja em +75.191 contratos (7,48% do open interest
de 1.004.746), ante +69.579 contratos (7,13% do OI de 975.954) em
07/07/2026. **Hoje, 21/07/2026, é o próprio dia de corte da semana** que vai
determinar o próximo relatório (publicação normal ~24/07) — esse relatório
vai mostrar, pela primeira vez, se os fundos compraram durante a semana do
rompimento de 17/07 e da confirmação de 20/07, ou se a devolução de hoje já
tem alguma correspondência em fluxo de posição.

**Os forecasts estatísticos internos (21/07/2026)** seguem altistas: central
7d = 1.237,36 cts/bu (bandas 1.185,38-1.289,35); central 30d = 1.337,85
cts/bu (bandas 1.230,22-1.445,47) — praticamente estáveis frente a ontem,
ainda a favor do viés de alta, mas o modelo reage a momentum recente, não a
fundamentos, e ainda não reflete a devolução do dia com peso significativo.

### O que invalida / risco para a soja

- **Um fechamento amanhã abaixo de 1.204,75 (mínima de hoje) ou de 1.180,00
  (resistência/suporte)** encerraria a leitura tática de continuidade e
  reabriria o cenário de teste do rompimento.
- **A devolução de hoje se repetir amanhã**, formando uma sequência de dois
  dias de fraqueza — a diferença entre "pausa saudável" e "início de
  reversão" só fica clara com mais uma sessão.
- **O prêmio físico de Paranaguá (hoje 6,41% sobre a paridade) continuar
  esticando** sem correspondência no papel — pode sinalizar um mercado físico
  descolado por retenção do produtor (ver notícia do dia), o que é bullish
  para a base mas não necessariamente para o CBOT.
- **O COT de 21/07 (publicação ~24/07) mostrar que os fundos começaram a
  vender** durante a semana da devolução.
- **O Crop Progress, quando atualizado (~26/07), mostrar nova melhora** na
  condição da lavoura americana — reforçaria o argumento de oferta potencial
  maior, contrário à tese tática de alta.

### Leitura operacional — soja

O dia de hoje é o primeiro teste real de disciplina desde a confirmação do
rompimento: uma devolução pequena (-0,43%) e um fechamento na metade inferior
do range, mas sem qualquer quebra de nível relevante (1.204,75 e 1.180,00
seguem intactos). Para quem está comprado alinhado ao rompimento, não há
motivo para reduzir posição hoje, mas vale apertar a atenção — se amanhã
repetir um fechamento fraco ou testar 1.204,75, a tese tática perde força
real, não apenas cosmética. 1.180,00 segue como stop lógico de fundo;
1.204,75 (mínima de hoje) é a referência mais próxima e mais conservadora.
Para quem está vendido contra o rompimento, o dia de hoje é o primeiro
argumento tático a favor da posição em uma semana, mas ainda pequeno demais
para justificar convicção — o evento decisivo continua sendo o COT de sexta
(~24/07).

---

## Farelo

**Viés: neutro tático (a confirmação bear de ontem não sobreviveu à sessão de
hoje), estrutural ainda bear via ABIOVE/ISF. O ratio Far/Soj fechou em
80,31% (indicadores, farelo 324,00 ÷ soja 1.210,25, base normalizada),
subindo +1,03 ponto percentual frente aos 79,28% de ontem e cruzando de volta
para a zona "neutra" (80-87%). Trata `ratio-zona-2026-07-21` e a revisão
vencida `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`.**

### O que sustenta a tese

**O farelo subiu com força relativa hoje, e é essa força — não uma queda da
soja isolada — que reverteu o ratio.** Fechamento 324,00 USD/short ton
(CBOT, ticker ZMU26.CBT, sessão de 21/07/2026), abertura 319,40, mínima
318,20, máxima 325,40, volume 26.981 contratos — um ganho de +4,60 (+1,44%)
frente à própria abertura e de +2,80 (+0,87%) frente ao fechamento de ontem
(321,20). O fechamento ficou em 80,6% do range do dia
((324,00-318,20)÷(325,40-318,20)) — um candle forte, fechando perto da
máxima, o oposto do padrão de fechamento fraco que a soja mostrou hoje. Como
o ratio Far/Soj mede farelo *relativo* à soja, e hoje o farelo subiu enquanto
a soja caiu, o efeito nos dois indicadores é reforçado na mesma direção: o
ratio subiu de 79,28% para 80,31% (+1,03pp), cruzando de volta para cima do
limiar de 80% que **ontem, pela primeira vez em uma sessão real de mercado,
tinha sido confirmado abaixo**.

**Tratando `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`:**
a revisão programada da tese original (insight
[[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]) tinha data-alvo
18/06/2026 — hoje, 21/07/2026, ela está **33 dias vencida**. A leitura de
ontem (20/07) havia marcado o critério tático ("ratio fecha <80% numa sessão
real") como satisfeito pela primeira vez, com o ratio em 79,28%. **O
fechamento de hoje desfaz essa confirmação em uma única sessão**: o ratio
voltou para 80,31%, de volta à zona "neutra" da própria régua do sistema
(<80% abundante/bear, 80-87% neutro, ≥87% apertado/bull). Em apenas duas
sessões de pregão real, o ratio cruzou o limiar de 80% duas vezes, em
direções opostas (79,71%→79,28%→80,31%) — o que é, em si, o achado mais
importante desta leitura sobre a revisão vencida: **80% não está se
mostrando um limiar de régime estável, e sim um número redondo fácil de
cruzar em qualquer direção com uma única sessão de volatilidade normal.**
Isso muda a recomendação prática: ao invés de tratar o cruzamento de ontem
como confirmação definitiva do critério tático, a leitura correta agora é
que o critério tático segue **inconclusivo por whipsaw**, e os critérios
fundamentalistas (WASDE mudou o quadro? NOPA confirmou o esmagamento?) seguem
sem resposta — WASDE parado desde 10/07/2026 (só farelo Argentina/Brasil/
China, sem nenhum dado de soja ou óleo, e sem nenhum dado dos EUA); NOPA
(fila `release-nopa-2026-07-21`) segue com `monthly_status` em 0,0 bool, a
mesma barreira de assinatura paga documentada desde meados de junho, agora
com mais de um mês sem alternativa de dado primário. Recomenda-se **não
fechar esta revisão** até que o ratio passe 2-3 sessões consecutivas de um só
lado do limiar, ou até que WASDE/NOPA tragam um dado fundamentalista novo —
os checkpoints estruturais D+90 (09/09/2026) e D+180 (08/12/2026) seguem
sendo o critério de mais alta confiança.

**A crush margin se expandiu +2,09% no dia, de 3,0316 para 3,0951 USD/bushel**
(Board Crush: farelo 324,00 + óleo 73,36 − soja 1.210,25) — revertendo quase
por completo a compressão de -4,48% registrada ontem. O mecanismo é o mesmo
já descrito na Visão geral, só que invertido: hoje o farelo subiu enquanto a
soja (o insumo) caiu, o que mecanicamente expande a margem de esmagamento no
cálculo de board crush. **O padrão dos últimos dois dias — crush comprimindo
quando a soja lidera de forma isolada, crush expandindo quando os produtos
lideram — é o exemplo mais didático desta semana de como a margem de
esmagamento depende da relação entre as três pernas, não do nível absoluto
de nenhuma delas.**

**A trajetória projetada da ABIOVE (sem alteração) segue sendo o pilar mais
sólido do argumento estrutural, porque não depende do preço do dia.** A
exportação de farelo brasileiro projetada cai de 1.400 mil toneladas em
agosto/2026 para 700 mil toneladas em dezembro/2026 (queda de 50% em quatro
meses), enquanto a produção cai de forma bem mais suave (2.285,06 → 1.659,04
mil toneladas no mesmo período, -27,4%) — menos farelo saindo pelo porto, com
produção caindo bem menos que a exportação, empurra o volume excedente para
o mercado interno de ração, pressionando o preço doméstico. Esse mecanismo
estrutural não muda com o ruído tático de hoje.

**As praças físicas de farelo no Brasil (NAG, 21/07/2026) ficaram
completamente estáveis**, sem variação em nenhuma das três: Mato Grosso/IMEA
R$ 1.602,80/ton (var 0,0%), Rio Grande do Sul R$ 1.640,00/ton (var 0,0%), e
Rondonópolis/MT R$ 1.650,00/ton (var 0,0%) — o salto pontual de Rondonópolis
registrado ontem (+3,13%) **se manteve no novo patamar, sem reverter, mas
também sem se propagar para as outras duas praças**, reforçando a leitura de
que foi um ajuste localizado, não o início de uma tendência ampla de alta
física. O prêmio de exportação em Paranaguá segue em +0,05 USD/short_ton
(julho/26, NAG), agora **18 dias corridos sem qualquer variação** desde
03/07/2026 — o mesmo sinal de possível estagnação de fonte já registrado em
leituras anteriores (ver Honestidade).

**O Índice de Sobra de Farelo (ISF) permanece em 80/100 (4 de 5 condições
estruturais)**, inalterado desde pelo menos 01/07/2026 — mais uma vez, a
confirmação de que o índice captura condições estruturais (ABIOVE, crush,
oferta), não o ruído tático do ratio de um único dia.

**O oil-meal spread (óleo menos farelo, por bushel) comprimiu ainda mais, para
0,9416 USD/bu**, ante 1,0538 ontem — uma queda de -10,65%, a maior compressão
de um dia nesta janela, e a segunda queda seguida (depois de -8,47% ontem).
Mede, de outro ângulo, o mesmo mecanismo: o farelo está recuperando terreno
relativo ao óleo por duas sessões seguidas.

**O COT de 14/07/2026, sem atualização, mantém o mesmo contraponto relevante
à tese bear.** Managed money net long em farelo em +46.576 contratos (7,77%
do open interest de 599.353) — mais que dobrado frente à semana anterior
(+18.722 em 07/07). Continua sendo o dado mais direto disponível hoje contra
uma posição vendida em farelo outright, e ganha relevância adicional depois
do whipsaw do ratio: se os fundos seguirem comprando farelo, a tese bear
estrutural pode enfrentar squeeze antes mesmo de a fundamentação (WASDE/NOPA)
aparecer.

**O forecast estatístico do farelo (21/07/2026)** segue com viés altista:
central 7d = 329,69 USD/sht (bandas 316,51-342,87); central 30d = 351,53
USD/sht (bandas 324,24-378,82) — o modelo estatístico (que reage a momentum
de preço recente, não a fundamentos) segue na direção oposta à tese
fundamentalista ABIOVE, uma divergência já documentada há várias leituras.

### O que invalida / risco para o farelo

- **O ratio Far/Soj cruzar de volta abaixo de 80% e permanecer ali por 2-3
  sessões seguidas** — só assim o critério tático da revisão D+7 pode ser
  considerado de fato confirmado, dado o whipsaw dos últimos dois dias.
- **A crush margin continuar se expandindo** — se a esmagadora acelerar o
  ritmo de processamento em resposta a uma margem maior, o excedente de
  farelo projetado pela ABIOVE pode chegar mais rápido do que o calendário
  sugere.
- **O COT de 21/07 (publicação ~24/07) mostrar os fundos continuando a
  aumentar o net long em farelo** — com a posição já mais que dobrada em uma
  semana, o risco de squeeze numa posição vendida direcional cresce.
- **O salto de Rondonópolis se propagar para Mato Grosso e Rio Grande do
  Sul** nas próximas sessões — seria o primeiro sinal físico amplo de alívio
  da abundância.
- **NOPA seguir inacessível indefinidamente**, sem confirmação do
  esmagamento americano para os checkpoints D+90 (09/09/2026) e D+180
  (08/12/2026).

### Leitura operacional — farelo

O whipsaw do ratio nos últimos dois pregões é, em si, a informação mais
acionável desta seção: quem tratou o cruzamento de ontem como sinal
definitivo para reforçar uma posição vendida em farelo outright levou uma
reversão completa em 24 horas. A recomendação prática muda de "critério
tático confirmado" (leitura de ontem) para "critério tático inconclusivo,
aguardando 2-3 sessões de confirmação de um só lado do limiar" — e, com o
COT mostrando fundos dobrando net long em uma semana, a assimetria de risco
para quem está vendido direcional em farelo aumentou, não diminuiu, desde
ontem. Para quem prefere o veículo mais defensável — o spread farelo/soja ou
o crush completo, em vez de direcional puro —, a compressão adicional do
oil-meal spread (-10,65% hoje, depois de -8,47% ontem, duas quedas seguidas)
é o dado mais consistente da semana: farelo ganhando força relativa ao óleo
por dois dias seguidos é um padrão mais confiável do que o próprio ratio
Far/Soj, que se mostrou ruidoso demais para operar sozinho perto de 80%.

---

## Óleo

**Viés: bull estrutural mantido (oil share e ISO seguem no teto), mas com o
segundo dia seguido de fricção tática — a primeira sequência de dois dias
fracos desde o rali que iniciou o movimento. Fechou em 73,36 cts/lb na sessão
de 21/07/2026, uma queda de -0,62% frente ao fechamento de ontem (73,82). O
oil share caiu ligeiramente para 53,1% e o Índice de Suporte do Óleo (ISO)
segue em 100/100.**

### O que sustenta a tese

**A vela de hoje é a segunda seguida a fechar abaixo tanto da abertura quanto
do fechamento anterior.** Fechamento 73,36 cts/lb (CBOT, ticker ZLU26.CBT,
21/07/2026), abertura 73,82 (a mesma marca do fechamento de ontem), mínima
72,70, máxima 74,32 — o preço abriu no nível de ontem, chegou a testar a
máxima (74,32) cedo na sessão, e devolveu a maior parte do ganho ao longo do
pregão, fechando em 40,7% do range do dia
((73,36-72,70)÷(74,32-72,70)) — um fechamento na metade inferior, mais fraco
até que o de ontem (53,3%). Dois dias seguidos de fechamento na metade
inferior do range, depois do forte rali da semana passada, começam a formar
um padrão técnico de perda de fôlego mais consistente do que um evento
isolado — ainda sem constituir uma reversão de tendência, mas merecendo
atenção redobrada na próxima sessão.

**A curva forward aprofundou ligeiramente a backwardation (desconto crescente
nos vencimentos mais distantes).** Agosto/26 (Q26) 74,23 → Setembro/26 (U26,
spot) 73,36 (-0,87, -1,17%) → Outubro/26 (V26) 72,29 (-1,07, -1,46%) →
Dezembro/26 (Z26) 71,56 (-0,73, -1,01%) → Janeiro/27 (F27) 71,18 (-0,38,
-0,53%) — uma queda total de -3,05 cts/lb (-4,11%) de agosto a janeiro/27,
ligeiramente mais acentuada que os -3,89% de ontem. A assinatura de força
concentrada no vencimento mais próximo, em vez de reprecificação estrutural
de toda a curva, segue intacta, mas a inclinação da curva está, dia após dia,
ficando um pouco mais negativa.

**A margem de biodiesel americano comprimiu pela segunda sessão seguida, para
0,904 USD/galão** (receita 7,206 = heating oil 4,041 + 1,5×RIN 2,11; custo
6,302 = óleo 5,502 + industrial 0,80), uma queda de -4,59% frente aos 0,9475
de ontem (que já tinha caído -5,97% frente à sexta-feira). **Duas quedas
seguidas de magnitude parecida (-5,97% e -4,59%) formam um padrão mais
robusto do que um evento isolado.** O heating oil (o principal componente de
receita do biodiesel americano, junto com o RIN D4) fechou hoje em 4,041
USD/galão, ante 4,119 ontem — uma queda real de -1,89%. **Mas o dado que mais
chama atenção hoje é a liquidez: o volume do heating oil foi de apenas 26
contratos**, ainda mais baixo que os já tímidos 109 de ontem — a menor
liquidez de toda a janela visível no briefing. Isso enfraquece
significativamente a confiança de que o nível de 4,041 reflete um consenso
de mercado amplo, e reforça a recomendação (já feita ontem) de tratar essa
série com cautela redobrada até que o volume normalize.

**O Índice de Suporte do Óleo (ISO) permanece em 100/100 (5 de 5 condições)**,
inalterado desde pelo menos 01/07/2026 — a tese estrutural (óleo dominando o
valor do crush) segue intacta e não é afetada pela fricção tática de dois
dias.

**O oil share caiu ligeiramente para 53,1%** (indicadores, 21/07/2026), ante
53,47% ontem — uma queda de -0,37 ponto percentual, terceira queda seguida
(53,83%→53,47%→53,1%), coerente com o farelo ganhando força relativa ao óleo
nos últimos dois pregões (ver seção Farelo, oil-meal spread). O óleo segue,
ainda assim, capturando a maior fatia do valor do crush (acima de 50%), sem
qualquer sinal de perda da liderança estrutural — mas a tendência de curto
prazo, pela primeira vez em semanas, é de leve recuo, não de expansão.

**O COT de 14/07/2026, sem atualização, mantém o óleo como a perna mais
"concorrida" das três.** Managed money net long em +107.945 contratos
(16,92% do open interest de 638.102) — o mais alto das três pernas por larga
margem. Com dois dias seguidos de fechamento fraco já registrados, o risco de
que esse posicionamento concentrado amplifique uma eventual correção segue
sendo o maior fator de risco de curto prazo para a tese, e o relatório de
sexta (~24/07) será o primeiro teste real.

**O forecast estatístico do óleo (21/07/2026)** mantém o viés altista:
central 7d = 74,92 cts/lb (bandas 70,27-79,56); central 30d = 80,87 cts/lb
(bandas 71,25-90,49) — ainda não reflete com peso os dois dias seguidos de
fraqueza tática.

### O que invalida / risco para o óleo

- **Um fechamento abaixo de 72,70 (mínima de hoje) ou de 72,29 (vencimento de
  outubro na curva de hoje)** reabriria o cenário de correção mais
  concretamente do que a mera perda de fôlego observada nos últimos dois
  dias.
- **O heating oil continuar caindo com volume tão baixo** — a combinação de
  queda de preço e liquidez mínima (26 contratos hoje) é o pior cenário para
  confiabilidade de sinal: pode ser um movimento real ou um artefato de baixa
  negociação, e só mais sessões normais de volume vão esclarecer.
- **O posicionamento dos fundos (net long em 16,92% do OI, o mais concorrido
  das três pernas) sofrer uma reversão** quando o próximo COT chegar (~24/07)
  — com dois dias fracos de preço já registrados, o risco de uma correção
  mais abrupta liderada por liquidação de posição comprada aumenta a cada
  sessão.
- **MPOB seguir inacessível** — impossível avaliar o efeito do El Niño ou das
  restrições/levy indonésias sobre o prêmio de substituição via palma. Hoje é
  o 12º dia consecutivo com o mesmo conteúdo sem números extraídos.

### Leitura operacional — óleo

A tese estrutural do óleo (oil share acima de 50%, ISO no teto de 100/100)
segue de pé, mas a fricção tática que começou ontem se estendeu por mais uma
sessão — dois fechamentos seguidos na metade inferior do range, depois do
forte rali da semana passada, é um padrão que já justifica cautela tática
mesmo sem qualquer quebra de nível técnico. Para quem está comprado
direcional em óleo desde o rompimento, a recomendação de ontem (apertar o
stop para perto da mínima do dia) segue válida e ganha urgência: a mínima de
hoje (72,70) é a referência mais próxima. Para quem opera exposição relativa
dentro do crush, a compressão do oil-meal spread por dois dias seguidos
(-8,47% ontem, -10,65% hoje) é o sinal mais consistente da semana de que a
divergência óleo-forte/farelo-fraco, que caracterizou o rali anterior, está
se revertendo de forma mais estrutural do que tática — vale reduzir, não
aumentar, exposição relativa a favor do óleo neste momento. O evento mais
importante da próxima sessão continua sendo dose dupla: a trajetória do
heating oil (com volume tão baixo hoje, a próxima sessão de volume normal é
que vai confirmar ou desmentir a queda) e o COT de sexta (~24/07), que vai
testar se o posicionamento mais concorrido do complexo começou a ceder depois
de dois dias de preço fraco.

---

## Spreads e crush — leitura de complexo

### Crush margin: 3,0951 USD/bu — expansão de +2,09%, reverte quase toda a compressão de ontem

A crush margin subiu +2,09% no dia (de 3,0316 para 3,0951 USD/bu),
recuperando quase por completo a queda de -4,48% registrada ontem. O
mecanismo, explicado na Visão geral e nas seções de soja/farelo: hoje o
farelo (+0,87%) e o óleo (-0,62%, mas partindo de um oil-meal spread menor)
combinados superaram a queda da soja (-0,43%, o insumo), o que mecanicamente
amplia a margem do board crush. O padrão dos últimos dois dias — soja
liderando isoladamente comprime a margem; produtos recuperando terreno a
expande — é o exemplo mais claro desta semana de como a crush margin
depende da relação entre as três pernas, não do nível absoluto de nenhuma
delas isoladamente.

### Ratio Far/Soj: 80,31% — cruzou de volta para a zona neutra, desfazendo a confirmação de ontem

O achado tático central desta leitura: em apenas duas sessões de pregão real,
o ratio cruzou o limiar de 80% duas vezes, em direções opostas (79,71% sexta
→ 79,28% ontem → **80,31% hoje**). Trata `ratio-zona-2026-07-21` e a revisão
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` (agora 33
dias vencida, critério tático agora tratado como **inconclusivo por whipsaw**,
não mais como confirmado — ver seção Farelo). A lição prática: 80% se mostrou
um limiar ruidoso, fácil de cruzar com uma única sessão de volatilidade
normal — recomenda-se exigir 2-3 sessões consecutivas do mesmo lado antes de
tratar qualquer cruzamento como sinal de régime.

### Oil share: 53,1% — terceira queda seguida, óleo ainda domina mas perde força marginal

Recuo de -0,37 ponto percentual frente a ontem (53,47%→53,1%), a terceira
queda seguida (53,83%→53,47%→53,1%) desde 17/07. O óleo segue, ainda assim,
capturando a maior fatia de valor do crush (acima de 50%), mas a tendência de
curto prazo, pela primeira vez em semanas, é de recuo consistente, não de
expansão — coerente com o oil-meal spread comprimindo por dois dias seguidos.

### Oil-meal spread: 0,9416 USD/bu — segunda compressão seguida, farelo recupera terreno relativo

Queda de -10,65% no dia (1,0538→0,9416 USD/bu), a maior compressão de um dia
nesta janela, depois de -8,47% ontem — duas quedas seguidas, o padrão mais
consistente desta leitura sobre a relação entre as duas pernas de produto. Mede,
de outro ângulo, a mesma mecânica que expandiu a crush margin: o farelo está
ganhando força relativa ao óleo por dois pregões seguidos.

### Margem de biodiesel: 0,904 USD/gal — segunda compressão seguida, mas com liquidez mínima no heating oil

A margem caiu -4,59% no dia, depois de -5,97% ontem — duas quedas seguidas
de magnitude parecida. Mas o volume do heating oil de hoje (26 contratos,
ante 109 ontem) é o mais baixo da janela, o que exige cautela redobrada antes
de tratar essa sequência como tendência consolidada em vez de ruído de baixa
liquidez.

### COT: sem atualização, mas hoje é o dia do corte — óleo segue disparado o mais concorrido

O dado de 14/07/2026 segue sendo o mais recente. Hoje, 21/07/2026, é o
próprio dia de corte da semana que vai gerar o próximo relatório (publicação
normal ~24/07) — o evento mais importante da semana para as três pernas,
mas especialmente para o óleo (16,92% do OI, disparado o mais concorrido) e
para o farelo (posição comprada dos fundos mais que dobrada na semana
anterior), dado o whipsaw de preço e do ratio nos últimos dois dias.

### ISF em 80/100, ISO em 100/100 — inalterados, confirmam que o whipsaw de hoje é tático, não estrutural

O Índice de Sobra de Farelo (4/5 condições) e o Índice de Suporte do Óleo
(5/5 condições) permanecem exatamente nos mesmos níveis de semanas
anteriores, mesmo com o cruzamento duplo do ratio Far/Soj em dois dias — a
confirmação mais clara de que os índices sintéticos capturam condições
estruturais (ABIOVE, oferta, crush), e o que mudou nos últimos dois dias foi
puramente a mecânica de preço, ora com a soja liderando, ora com os produtos
liderando.

### O que os índices dizem juntos em 21/07/2026

ISF 80/100 + ISO 100/100 (ambos inalterados, condições estruturais intactas)
+ ratio Far/Soj de volta à zona neutra depois de um whipsaw de duas sessões
(79,71%→79,28%→80,31%) + crush margin e oil-meal spread revertendo quase
totalmente a compressão de ontem + oil share em terceira queda seguida mas
ainda acima de 50% + margem de biodiesel comprimindo pela segunda vez seguida
(porém com volume de heating oil na mínima da janela) + COT ainda sem
atualização no próprio dia do corte semanal — formam um quadro em que a tese
estrutural do complexo (esmagamento incentivado, óleo dominando o valor,
farelo abundante) segue intacta, mas a mecânica tática de curto prazo virou
de "soja lidera e comprime os spreads" para "produtos lideram e expandem os
spreads" em apenas 24 horas. A lição mais importante para quem opera o
complexo esta semana: os spreads perto de limiares redondos (ratio em 80%)
estão se mostrando voláteis demais para tratar um único cruzamento como sinal
definitivo — o COT de sexta (~24/07) é o próximo dado capaz de resolver essa
ambiguidade com evidência de posicionamento, não apenas de preço.

---

## Lente fiscal e regulatória BR

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L) — a
vigência formal (`vigencia_ate` 11/07/2026) venceu há 10 dias, e o monitor
tributário segue sem qualquer atualização de status** (system/tributario_watch.toml,
evento MP-1358-2026, `atualizado_em` 2026-06-05, status ainda "tramitacao").
Enquanto o combustível fóssil segue subsidiado, a competitividade relativa do
biodiesel dentro do mix B15 mandatório fica pressionada — um vetor
regulatório independente da margem de biodiesel americana (que hoje
comprimiu -4,59% por conta própria, via heating oil), somando dois
headwinds distintos sobre a mesma economia de processamento.

**Isenção PIS/Cofins biodiesel — vencimento em 31/07/2026, agora a apenas 10
dias.** Sem sinalização pública de renovação até hoje (evento
PISCOFINS-BIODIESEL-ISENCAO, `atualizado_em` 2026-06-05, sem mudança). Com a
margem de biodiesel americana comprimindo pela segunda sessão seguida (0,904
USD/gal, -4,59%) e o vencimento da isenção brasileira a apenas 10 dias, o
cenário de "duplo headwind" (custo tributário potencial no Brasil + margem
apertada nos EUA) segue relevante e ganha urgência crescente — é o vetor
tributário mais próximo de um desfecho concreto nesta leitura, e o mais
importante a monitorar nos próximos dez dias.

**B16 — sem data, travado em B15.** Sem mudança de status (evento
B16-CNPE-2026, `atualizado_em` 2026-06-05, status "adiado"). Testes técnicos
do FNDCT com resultado esperado ~nov/2026 — realista só fim de 2026/início
de 2027.

**MP 1.363/2026 (subsídio ao diesel fóssil, R$ 1,12/L) — em vigor até
31/12/2026.** Sem alteração. Bearish estrutural persistente para a demanda
incremental de óleo de soja no mercado doméstico brasileiro.

**STJ REsp 2.165.276/2026 — crédito PIS/Cofins para esmagadoras.** Sem
alteração. Bullish para soja/óleo (alívio de custo de entrada para
biodiesel) e, por extensão, incentivo a mais esmagamento — em tensão com a
expansão de hoje na crush margin, que já sinaliza incentivo de curto prazo
crescente independentemente do alívio tributário estrutural.

**Vetores dos EUA e Indonésia, revisitados (sem mudança de status,
`atualizado_em` 2026-06-05 em todos):** EPA-RFS-2026-2027 (volumes recordes
de biocombustível, BBD 8,86→9,07 bi RINs, sustentando estruturalmente o RIN
D4 e o óleo CBOT — o RIN D4 usado no cálculo da margem de biodiesel segue
fixo em 2,11 USD/RIN, ver Honestidade); 45Z-CLEAN-FUEL (regra proposta que
tiraria insumo importado da elegibilidade ao crédito, favorecendo óleo de
soja doméstico americano); DANANTARA-INDONESIA (centralização estatal da
exportação de palma, assunção plena da cadeia alvo em 01/09/2026 — risco de
menor saldo exportável de palma, suporte ao óleo de soja por substituição);
INDONESIA-B50 (retórica agressiva mas quota flat — provável B45 em 2026,
B50 pleno só 2027-28); INDONESIA-LEVY-PMK9 (imposto de exportação de CPO até
12,5% desde 01/03, encarecendo palma e favorecendo substituição por óleo de
soja). Todos esses vetores seguem, em conjunto, num sentido estruturalmente
bullish para o óleo de soja via substituição de palma — mas seguem
inverificáveis pelo lado dos dados de mercado (MPOB inacessível há 12 dias
consecutivos, ver Honestidade).

**O monitor tributário como um todo está há 46 dias sem qualquer
atualização** (`atualizado_em` 2026-06-05 em todos os dez eventos
rastreados) — o intervalo segue crescendo em um momento em que dois vetores
(MP 1.358, já vencida há 10 dias, e a isenção PIS/Cofins, a 10 dias do
vencimento) têm datas formais já vencidas ou criticamente próximas. Vale
sinalizar este ponto, mais uma vez, como prioridade de manutenção do sistema,
independentemente da leitura de preço.

---

## Riscos e eventos próximos

**O COT (CFTC) — hoje, 21/07/2026, é o próprio dia de corte da semana.** É o
evento mais importante dos próximos dias: a publicação normal (~24/07) vai
mostrar se os fundos compraram ou venderam soja, farelo e óleo durante a
semana que incluiu tanto a devolução de hoje na soja quanto o whipsaw do
ratio Far/Soj — o primeiro dado de posicionamento capaz de arbitrar se o
sinal de preço desta semana tem ou não correspondência em fluxo real de
fundos.

**A isenção PIS/Cofins do biodiesel vence em 31/07/2026, agora a 10 dias**,
sem sinalização de renovação — o vetor tributário mais próximo de um
desfecho concreto nesta leitura, coincidindo com uma margem de biodiesel
americana que já comprime por conta própria pela segunda sessão seguida.

**A trajetória do heating oil com volume tão baixo (26 contratos hoje)** é o
dado mais frágil desta leitura e o mais urgente de confirmar: se a próxima
sessão trouxer volume normal e a queda persistir, a pressão sobre a margem de
biodiesel ganha muito mais credibilidade; se o volume normalizar e o preço
reverter, a queda de hoje deve ser tratada como ruído de baixa liquidez.

**O ratio Far/Soj precisa de mais 2-3 sessões para resolver o whipsaw** —
tanto a leitura tática do farelo quanto a revisão D+7 vencida dependem de o
ratio se estabilizar de um lado do limiar de 80% por mais de uma sessão.

**NOPA — segue inacessível** (fila `release-nopa-2026-07-21` tratada aqui,
sem dado interpretável), sem crush americano confirmado por fonte primária.

**MPOB — sem números de palma extraídos há 12 dias consecutivos**, mantendo
cego o efeito do El Niño e dos vetores regulatórios indonésios sobre o
prêmio de substituição do óleo de soja.

**Checkpoints futuros da tese estrutural do farelo (ABIOVE)** — D+90 em
09/09/2026 e D+180 em 08/12/2026 (insight
[[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]) — a revisão D+7,
agora 33 dias vencida, teve seu critério tático revertido em 24 horas (ver
seção Farelo) e segue sem confirmação de fundamentos (WASDE, NOPA); os
checkpoints estruturais seguem o critério de mais alta confiança para julgar
a tese ao longo do tempo.

---

## Honestidade

O que não foi possível validar neste briefing de 21/07/2026, onde a
confiança é baixa ou há lacunas materiais:

**1. O fechamento de soja de 20/07/2026 usado como base de comparação para os
números de hoje é, ele mesmo, uma quarta versão distinta do mesmo dado ao
longo de gerações sucessivas do pipeline.** As leituras de fim de semana
registraram 1.204,50; a leitura de 20/07 registrou 1.213,75 (a primeira
sessão "genuinamente nova"); os indicadores usados hoje, por sua vez,
calculam a crush margin e o ratio de 20/07 usando 1.215,50 — um valor 1,75
ponto mais alto ainda. Isso é a terceira revisão documentada do mesmo
fechamento em poucos dias, sem qualquer sinalização explícita no dump. Todos
os cálculos de variação desta leitura usam consistentemente o valor de
1.215,50 (o mesmo usado pelos indicadores de hoje), mas comparações de
tendência que atravessam essa fronteira devem ser lidas com essa ressalva em
mente.

**2. A seção bruta `cme_cbot` do dump de hoje não traz os preços OHLC de soja
e óleo para a sessão de 20/07/2026** — apenas farelo e heating oil aparecem
com dado bruto completo daquele dia. A comparação de hoje contra ontem para
soja e óleo depende inteiramente do fechamento implícito na fórmula de crush
margin dos indicadores, não de uma confirmação direta da fonte primária CME
para aquele dia específico.

**3. O volume do heating oil caiu para apenas 26 contratos hoje, ante já
baixos 109 ontem** — a menor liquidez de toda a janela de 14 dias visível no
briefing. A confiança na leitura de "queda real do heating oil pressionando
a margem de biodiesel" precisa de pelo menos mais uma sessão de volume
normal para ser tratada como sinal de mercado amplo, e não como um artefato
de poucos negócios.

**4. O prêmio de exportação de farelo em Paranaguá (+0,05 USD/sht) e o de
óleo (+0,08 cts/lb) estão no mesmo valor exato desde pelo menos 03/07/2026**
(NAG, agora 18 dias corridos sem variação de nenhum centavo) — não é possível
distinguir se isso reflete um mercado de exportação genuinamente parado ou um
valor que não está sendo atualizado de fato na fonte.

**5. O COT (CFTC) segue com dado de referência 14/07/2026.** Hoje é
literalmente o dia do corte semanal seguinte, mas nenhum dado novo está
disponível ainda — o relatório esperado (~24/07) é o teste genuíno mais
importante em aberto para resolver o whipsaw do ratio e a devolução da soja.

**6. Percentis históricos de COT não calculados** — os números de 14/07/2026
são lidos apenas em nível absoluto e como fração do open interest corrente
(soja 7,48%, farelo 7,77%, óleo 16,92%), sem série histórica completa para
calibrar se algum desses níveis está objetivamente "esticado" no sentido
histórico.

**7. O WASDE segue cobrindo apenas farelo (Argentina, Brasil, China
parcial), sem nenhum dado de soja em grão ou óleo de soja, em qualquer
geografia, e sem nenhum dado dos Estados Unidos** — sem atualização desde
10/07/2026. A pergunta central da revisão D+7 vencida ("o WASDE mudou o
quadro?") segue sem canal de resposta interno.

**8. NOPA (fila `release-nopa-2026-07-21`) segue com `monthly_status` em 0,0
bool** — mesma barreira de assinatura paga documentada desde meados de junho,
agora com mais de um mês sem alternativa de dado primário sobre o
esmagamento americano. A "novidade" sinalizada pela fila é apenas a data de
coleta, não um dado genuinamente interpretável.

**9. Palma malaia (MPOB) segue sem números extraídos, agora por 12 dias
consecutivos com o mesmo conteúdo exato (3.439 caracteres, de 10/07 a
21/07/2026)** — a persistência do byte count idêntico sugere, possivelmente,
uma página que não está mais sendo servida com conteúdo atualizado. Continua
impossível avaliar o efeito do El Niño ou dos vetores regulatórios
indonésios sobre o prêmio de substituição do óleo de soja.

**10. Clima INMET (BR) não foi usado como driver desta leitura.** Julho é
entressafra da soja brasileira (colheita concluída, plantio só em outubro) —
sem relevância direta para a tese de preço neste momento do calendário
agrícola, embora o El Niño Advisory (NOAA CPC, inalterado desde pelo menos
03/07/2026) permaneça relevante para a expectativa da safra de plantio de
outubro/26 e para o clima do Sudeste Asiático (palma). O boletim INMET de
amanhã (22/07) traz previsão de chuva forte e possível granizo no Paraná/Rio
Grande do Sul — sem relevância de oferta agora (entressafra), mas vale
observar se afeta logística de escoamento no curto prazo.

**11. BCBA Argentina — sem relatórios de esmagamento/exportação acessíveis
via scraper** (page_fetched=1,0 mas sem links de relatório, 21/07/2026, sem
mudança).

**12. RIN D4 como parâmetro fixo (2,11 USD/RIN) segue sendo uma fonte
relevante de incerteza do modelo de biodiesel**, sem novo dado hoje — a
margem calculada em 0,904 USD/gal usa esse valor fixo; se o RIN de mercado
estiver, na realidade, diferente de 2,11, tanto a margem quanto o ISO podem
estar mal calibrados, independentemente da compressão real documentada hoje
via heating oil.

**13. O whipsaw do ratio Far/Soj (79,71%→79,28%→80,31% em três sessões) é, em
si, um sinal de que o limiar de 80% pode não ser um régime estável e sim um
número redondo ruidoso** — esta leitura recomenda tratar qualquer cruzamento
futuro com a mesma cautela, exigindo confirmação de 2-3 sessões antes de
atualizar a tese, uma lição metodológica tão importante quanto qualquer dado
numérico desta janela.

*Nenhum número foi inventado ou estimado além do que consta no briefing de
21/07/2026 e nos insights anteriores referenciados. A contribuição central
desta leitura foi identificar que o cruzamento do ratio Far/Soj abaixo de 80%
"confirmado" ontem não sobreviveu a uma segunda sessão de pregão — um
whipsaw que reverte a leitura tática do farelo e recomenda tratar a revisão
D+7 (já 33 dias vencida) como ainda inconclusiva, ao mesmo tempo em que a
soja teve seu primeiro dia de devolução desde o rompimento e o óleo somou um
segundo dia seguido de fricção tática, com o heating oil operando em volume
mínimo.*
