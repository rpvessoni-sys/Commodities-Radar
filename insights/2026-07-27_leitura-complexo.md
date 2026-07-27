---
data: 2026-07-27
titulo: "Segunda-feira de reversão ampla e de alto volume no complexo: soja (-3,45%), farelo (-3,11%) e óleo (-3,67%) caem juntos com volume MAIOR que sexta-feira nas três pernas — óleo rompe o suporte técnico de 72,00 cts/lb (confirmando o gap fino do heating oil de domingo), soja fecha exatamente na mínima do dia mas sem romper o piso estrutural de 1.180,00, e o ratio Farelo/Soja SOBE de 80,02% para 80,29%, afastando-se do piso pela primeira vez em seis sessões mesmo em dia de liquidação generalizada — enquanto a margem de biodiesel americana na verdade MELHORA (+0,78%) e a base física da soja em Paranaguá se alarga para +9,73% sobre a paridade, dois sinais que tensionam a leitura de que a queda de hoje seja um driver fundamental novo, e apontam mais para um desmonte técnico de posição comprada excessiva (COT) do que para uma mudança de tese estrutural"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT (ZSU26 soja / ZMU26 farelo / ZLU26 óleo) — sessão de 2026-07-27, primeira sessão regular após o fim de semana, volume acima do de sexta-feira (24/07) nas três pernas
  - CME heating_oil_cbot (HO=F) — print de 2026-07-27, volume 278 contratos (anormalmente baixo — ver Honestidade) e revisão de 2026-07-26 (fechamento 3,9841, volume 1.895)
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, paridade BR, Índice de Sobra de Farelo, Índice de Suporte do Óleo) — 2026-07-27
  - BCB PTAX — 2026-07-27 (USD/BRL 5,1005, EUR/BRL 5,8023, Selic diária 0,052531% a.a.)
  - CEPEA/ESALQ Paranaguá via NAG — 2026-07-27 (suporte R$ 147,75/saca, var -0,42%)
  - CEPEA/ESALQ Paraná interior via NAG — 2026-07-27 (R$ 140,58/saca, var +0,23%)
  - NAG Físico BR (farelo MT/IMEA R$ 1.669,72/ton estável; Rondonópolis R$ 1.650,00/ton estável; RS R$ 1.640,00/ton estável; prêmios export PGUA farelo +0,05 USD/sht e óleo +0,08 cts/lb, ambos inalterados) — 2026-07-27
  - CFTC COT Managed Money — corte de 2026-07-21 (ainda o mais recente; próximo corte referente a 28/07, publicação normal ~31/07)
  - USDA Crop Progress — dado NOVO nesta janela, publicado com data 2026-07-26 (11% excelente + 52% boa + 7% ruim, ante 13%/53%/6% em 19/07)
  - USDA WASDE — ainda 2026-07-10, sem atualização (17 dias)
  - NOPA — fila `release-nopa-2026-07-27`, `monthly_status` continua em 0,0 bool (paywall)
  - ABIOVE projeções mensais — balanços ago-dez/2026 (farelo/óleo/soja), sem alteração
  - NOAA CPC ENSO — 2026-07-27 (El Niño Advisory, inalterado desde pelo menos 03/07/2026)
  - MPOB — 2026-07-27 (18º dia consecutivo com o mesmo conteúdo, parser sem números extraídos)
  - BCBA Argentina — 2026-07-22 (5 dias sem atualização)
  - Notícias Agrícolas/Farm Progress RSS — 2026-07-27 (160 itens lidos, 8 mantidos; manchete nova "Is a record soybean crop in the works?", farmprogress.com)
  - Forecasts estatísticos internos — 2026-07-27 (nova geração, spot ref já reflete a queda: soja 1.197,50 / farelo 320,50 / óleo 70,77 — viés "altista" nas três, ver Honestidade sobre defasagem do modelo)
  - system/tributario_watch.toml (lido apenas como referência, não editado) — 10 eventos, `atualizado_em` 2026-06-05 (53 dias sem atualização); trata `trib-PISCOFINS-BIODIESEL-ISENCAO-2026-07-31`
  - Cruza com [[2026-07-26_leitura-complexo]], [[2026-07-25_leitura-complexo]], [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (checkpoint D+90 em 09/09/2026, revisitado hoje)
status: ativa
vies: [neutral-soja, neutral-farelo, bear-oleo_soja]
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
Quando o oil share sobe, o óleo passa a "pagar o crush" sozinho, e o farelo
vira, cada vez mais, um subproduto que a esmagadora aceita vender barato só
para liberar o óleo — é esse mecanismo que está por trás do **ratio Far/Soj**
(preço do farelo dividido pelo preço da soja, normalizado pela conversão
bushel↔short ton): abaixo de 80% o farelo está historicamente "abundante"
frente à soja (zona bear); acima de 87%, "apertado" (zona bull); entre os
dois, zona neutra e de **mean-reversion** (funciona nos dois lados do book).

**Hoje é a primeira sessão regular de pregão depois do fim de semana, e ela
trouxe a reversão mais violenta e mais bem-participada de toda a janela
observada por esta série.** As três pernas caíram juntas e forte: soja
-3,45% (de 1.240,25 para 1.197,50 cts/bushel), farelo -3,11% (de 330,80 para
320,50 USD/short ton) e óleo -3,67% (de 73,47 para 70,77 cts/lb) — todas
calculadas contra o fechamento de sexta-feira (24/07), que as duas últimas
leituras já haviam confirmado como estável por dois dumps seguidos. **O
detalhe que muda a leitura de "só mais uma correção" para "movimento técnico
relevante" é o volume: nas três pernas, o volume de hoje veio ACIMA do de
sexta-feira** (soja 31.854 vs 26.848, +18,7%; farelo 39.353 vs 35.887, +9,7%;
óleo 49.159 vs 46.086, +6,7%) — uma queda de alta convicção, não um ajuste
fino em mercado vazio. A soja fechou **exatamente na mínima do dia**
(1.197,50 = mínima = fechamento, 0% do range), o óleo fechou **a 3,7% do
fundo do range** (quase tão fraco quanto a soja), e o farelo, embora também
tenha fechado perto da mínima, foi relativamente o menos fraco dos três
(16,9% do range) — uma hierarquia de fraqueza que já antecipa a leitura por
perna abaixo. **O que sustenta o susto, porém, tem furos importantes.** O
óleo rompeu de fato o suporte técnico de 72,00 cts/lb, confirmando o gap fino
do heating oil de domingo que a leitura de ontem tratou como "sinal a
confirmar" — mas o próprio heating oil (o termômetro de energia usado para a
margem de biodiesel) mal se moveu hoje (3,9841→3,9862, +0,05%) e em volume de
apenas 278 contratos, o mais baixo de toda a janela; **a margem de biodiesel
americana, na verdade, MELHOROU** (1,0354→1,0435 USD/galão, +0,78%), porque o
custo do óleo caiu mais rápido do que a receita. E a soja, apesar do tombo,
**não rompeu o piso estrutural de 1.180,00** (ainda 1,48% de distância) e viu
a **base física em Paranaguá se alargar para +9,73%** sobre a paridade
teórica em reais — o físico caiu muito menos (-0,42%) do que o papel
(-3,45%), o que é evidência direta de que a demanda física exportadora não
capitulou junto com o CBOT. Some-se a isso que o COT de 21/07 (ainda o mais
recente) havia mostrado os fundos comprando as três pernas de forma
extremamente concentrada numa única semana (net long +73,6% em soja, +57,8%
em farelo, +11,4% em óleo) — a leitura mais direta deste conjunto de fatos é
que **hoje se pareceu mais com um desmonte técnico de posição comprada
excessiva e correlacionada entre as três pernas do que com uma mudança de
tese fundamental**, já que os pilares estruturais que sustentavam a alta
(ISO 100/100, crush ainda positivo, base física forte, ratio Far/Soj) não
se romperam — pelo contrário, o ratio Far/Soj **subiu** de 80,02% para
80,29%, o primeiro movimento de afastamento do piso de 80% em seis sessões,
justamente no dia em que se esperaria vê-lo romper para baixo se a queda
fosse "farelo liderando a baixa". **Leitura de uma linha:** o pivô do
complexo continua sendo a soja, mas hoje o pivô é técnico (1.180,00 segura
ou não) mais do que fundamental — o maior convicção desta leitura é que o
óleo é a perna que genuinamente mudou de regime técnico (suporte rompido,
fechamento na mínima), enquanto soja e farelo estão em zona de reteste de
suporte sem ruptura confirmada; confiança moderada para óleo (tático bear,
estrutura ainda intacta), baixa-moderada para soja e farelo (o desmonte de
hoje pode ser ruído de uma semana de COT esticado, ou o início de algo
maior — só a sessão de amanhã e o próximo COT, 28/07/publicação ~31/07, vão
dizer).

---

## Soja

**Viés: neutro, com viés tático bear muito forte contido por um piso
estrutural que ainda não cedeu.** A soja caiu -3,45% hoje (1.240,25 →
1.197,50 cts/bushel, CBOT, ticker ZSU26.CBT) e fechou exatamente na mínima
da sessão — o fechamento mais fraco (em termos de posição no range) de toda
a janela acompanhada por esta série. Ao mesmo tempo, o nível de 1.180,00 —
a antiga resistência rompida em meados de julho e citada nas leituras
recentes como piso estrutural — **não foi tocado nem testado**: o
fechamento de hoje está 1,48% acima dele. Trata `alerta-quebra_resistencia-soja_cbot-2026-07-27`
(o alerta confirma que o fechamento segue acima do nível 1.180,00, ou seja,
a estrutura de rompimento de julho continua tecnicamente de pé, apesar do
tombo do dia) e `alerta-movimento_forte-soja_cbot-2026-07-27` (a variação de
-3,45% no dia, de 1.240,25 para 1.197,50).

### O que sustenta a tese

**O tombo de hoje foi amplo, com volume mais alto que sexta e um fechamento
tecnicamente muito fraco.** Abertura 1.232,75 (já 0,60% abaixo do fechamento
de sexta, um gap de abertura moderado), máxima 1.236,75 (tocada logo no
início, sem retorno), mínima e fechamento coincidentes em 1.197,50 — ou
seja, o contrato vendeu de forma consistente a sessão inteira, sem nenhuma
recuperação, e fechou colado no pior preço do dia (0% do range
(1.197,50-1.197,50)÷(1.236,75-1.197,50)). O volume de 31.854 contratos ficou
18,7% acima do de sexta-feira (26.848, já confirmado) — isso é relevante
porque descarta a hipótese de "movimento fino, pouco confiável" que se
aplicou ao gap do heating oil de domingo: aqui há participação de mercado
real por trás da queda.

**Mesmo assim, o nível que definiria uma mudança de tese — 1.180,00 — não
foi rompido, e a distância até ele (1,48%) é a mesma ordem de grandeza da
distância que separava o fechamento de sexta da mínima de sexta (1,24%).**
Em outras palavras, o tombo de hoje consumiu quase toda a "folga" técnica
acumulada desde o rompimento de meados de julho, mas ainda não a esgotou.
Isso muda o caráter do nível: de "suporte confortavelmente distante" (leitura
de 26/07, 5,10% de distância) para "suporte na berlinda, a ser testado já na
próxima sessão de fraqueza".

**O COT de 21/07/2026 (CFTC, ainda o mais recente, sem atualização nova
hoje) é o dado-chave para entender POR QUE um tombo desta magnitude era
plausível mesmo sem notícia fundamental nova.** Na semana de 21/07, managed
money (fundos especulativos com posicionamento direcional) elevou a compra
de 145.930 para 180.163 contratos (+23,5%) e reduziu a venda de 70.739 para
49.658 (-29,8%) — o net long saltou de 75.191 para 130.505 contratos
(+73,6% em uma única semana), passando de 7,48% para 12,49% do open
interest (1.045.077 contratos). **Mecanismo:** uma compra desse tamanho
concentrada em uma semana deixa a posição "esticada" — qualquer notícia
neutra ou levemente negativa, ou mesmo a ausência de fluxo comprador novo
(nenhuma notícia hoje sustenta compra adicional), é suficiente para
provocar realização de lucro em massa, e realização de lucro em posição
comprada tende a ser mais abrupta do que a formação da posição, porque quem
está comprado vende ao mesmo tempo que novos vendedores entram — exatamente
o padrão de "queda com volume maior que a alta" observado hoje. O próximo
corte do COT (28/07, publicação normal ~31/07) é o dado que vai confirmar
ou desmentir essa leitura: se mostrar reversão de posição (net long caindo),
o desmonte técnico já começou a ser capturado pelos dados oficiais; se
mostrar posição ainda comprada, o tombo de hoje foi puramente intradiário
(retail/algo) e o quadro estrutural segue intacto.

**O USDA Crop Progress trouxe um dado genuinamente novo hoje, publicado com
data de 26/07/2026** (a leitura de ontem esperava essa publicação "nas
próximas 24-48 horas", e ela chegou): condição da lavoura americana de soja
em 11% excelente + 52% boa + 7% ruim, uma **piora marginal** frente ao corte
anterior de 19/07 (13% excelente + 53% boa + 6% ruim) — o bom-ou-excelente
caiu de 66% para 63% (-3 pontos percentuais), e o "ruim" subiu de 6% para
7%. **Mecanismo:** piora de condição de lavoura reduz a expectativa de
produtividade da safra americana, o que é estruturalmente BULLISH para
soja (menos oferta esperada) — o oposto direcional do que o preço fez hoje.
**Esta é a primeira tensão explícita desta leitura**: o único dado
fundamental novo do dia aponta para cima, não para baixo, o que reforça a
leitura de que o tombo de -3,45% foi predominantemente técnico/de
posicionamento, e não uma resposta a um dado de oferta/demanda.

**Uma notícia nova, sem corpo disponível neste briefing (apenas manchete),
pode estar relacionada ao tom do dia.** O Farm Progress publicou em
27/07/2026 a manchete "Is a record soybean crop in the works?" ("Está a
caminho uma safra recorde de soja?") — uma manchete que, tomada
isoladamente, sugere um enquadramento de área plantada elevada sustentando
um potencial recorde de produção, mesmo com a condição percentual em leve
queda (safras recordes historicamente dependem mais de área e clima na fase
de enchimento de grãos do que do instantâneo semanal de condição). **Esta
leitura NÃO trata essa manchete como driver quantitativo** — não há corpo de
matéria disponível, nem projeção numérica, apenas o título — mas registra
que é o tipo de narrativa que, se ganhar tração generalizada, tensiona
diretamente a tese bull construída nas últimas semanas em cima do
rompimento técnico e do COT comprador.

**A base física em Paranaguá, ao contrário do papel, quase não se moveu.**
CEPEA/ESALQ Soja Paranaguá fechou hoje em R$ 147,75/saca (via NAG, var
-0,42%) — a primeira queda depois de cinco altas consecutivas (142,65 →
144,17 → 145,45 → 147,47 → 148,37 → **147,75**), mas uma queda de apenas
0,42%, ínfima frente ao -3,45% do CBOT. **Mecanismo e leitura:** a paridade
teórica em reais recalculada para hoje é R$ 134,65/saca (CBOT 1.197,50 cts ×
PTAX USD/BRL 5,1005 de 27/07/2026, sem basis) — bem abaixo dos R$ 138,53 de
sexta, porque o CBOT caiu mais rápido do que o câmbio compensou (o USD/BRL
subiu de 5,0666 para 5,1005, +0,67%, o que amorteceu parte da queda em
reais, mas não o suficiente). Com o físico praticamente estável em R$
147,75, o **prêmio de exportação sobre a paridade saltou de +7,10% (sexta)
para +9,73% hoje** ((147,75-134,65)÷134,65) — o maior desta janela. **Esse
alargamento de base é o dado mais importante desta leitura para avaliar se a
queda do papel reflete algo real na demanda física**: se o comprador
exportador (majoritariamente chinês, ver notícias recentes desta série)
estivesse reagindo à mesma informação negativa que derrubou o CBOT, o
físico teria caído proporcionalmente também. Ele não caiu — o que sustenta a
leitura de "papel liderando a queda por motivo técnico/de posicionamento",
com o físico ainda sinalizando demanda de exportação firme. O físico de
Paraná interior, aliás, **subiu** hoje (R$ 140,58/saca, var +0,23%),
reforçando essa divergência.

**A curva forward manteve a estrutura de prêmio crescente nos vencimentos
mais distantes, agora com valores mais baixos em todos os pontos, mas a
FORMA da curva preservada.** Setembro/26 (U26, spot) 1.197,50 → Novembro/26
(X26) 1.211,50 (+14,00, +1,17%) → Janeiro/27 (F27) 1.225,00 (+13,50, +1,11%)
→ Março/27 (H27) 1.227,00 (+2,00, +0,16%) — o contango moderado e crescente
que já vinha sendo documentado nas leituras anteriores continua intacto na
FORMA, apenas deslocado para baixo em nível — um sinal de que o mercado não
está precificando estresse de curto prazo incomum (uma curva que "quebra"
sua forma tende a sinalizar pânico ou aperto físico pontual; aqui isso não
ocorre). Agosto/26 (Q26) fechou em 1.206,25, prêmio de +0,73% sobre o spot.

**Os forecasts estatísticos internos (27/07/2026)**, recalculados já com o
spot pós-queda (1.197,50), seguem etiquetados como "altista": central 7d =
1.231,13 cts/bu (bandas 1.172,97-1.289,28); central 30d = 1.345,07 cts/bu
(bandas 1.224,67-1.465,46). **Atenção**: esse modelo usa média móvel de 20
dias + volatilidade + inclinação de curto prazo — ele ainda carrega o
impulso ascendente das últimas semanas na média móvel, e é natural que o
rótulo "altista" pareça dissonante do tombo de hoje; esta leitura trata o
forecast como uma referência estatística de banda, não como uma previsão
fundamentada, e nota que ele tende a reagir com atraso a reversões abruptas
como a de hoje (ver Honestidade).

### O que invalida / risco para a soja

- **Um fechamento abaixo de 1.180,00** encerraria de fato a leitura de
  "suporte estrutural ainda de pé" — depois do tombo de hoje, essa distância
  caiu para apenas 1,48%, a menor desta janela, tornando esse o nível mais
  vigiado da segunda-feira em diante.
- **Um novo dia de queda com volume ainda mais alto que hoje** reforçaria a
  leitura de desmonte técnico em curso, não de ruído de um dia isolado.
- **O próximo corte do COT (28/07, publicação ~31/07) mostrar reversão do
  net long** — se os fundos que compraram +73,6% na semana de 21/07
  começarem a devolver posição, confirma que o tombo de hoje é o início da
  realização de lucro, não um evento isolado.
- **A base física em Paranaguá cair de forma mais acentuada nos próximos
  dias** — hoje ela mal se moveu (-0,42%), mas se o físico começar a
  acompanhar o papel proporcionalmente, a tese de "demanda física ainda
  firme" perde sustentação.
- **A manchete "recorde de safra" ganhar corpo com números concretos** (área
  plantada, projeção de produção) em vez de ficar só no título — hoje não há
  como avaliar isso além do título.

### Leitura operacional — soja

Depois de um tombo de alta convicção (volume maior que sexta, fechamento na
mínima), mas sem ruptura do piso estrutural (1.180,00, 1,48% de distância),
o quadro pede **neutralidade tática com viés de vigilância nos dois
lados**. Para quem está comprado desde o rompimento de julho: o argumento
para manter a posição (base física ainda forte, +9,73% de prêmio; curva
forward com forma preservada; ratio Far/Soj não confirmando farelo liderando
a baixa) ainda existe, mas o stop deveria ser reavaliado para perto de
1.180,00 — a folga que sustentava posições mais largas se esgotou muito
nesta única sessão. Para quem opera vendido tático: o próprio fechamento na
mínima e o volume elevado dão munição para uma posição vendida com stop
acima da máxima de hoje (1.236,75) ou, mais conservador, acima do
fechamento de sexta (1.240,25) — mas o risco central dessa operação é que o
COT de 21/07 e a base física ainda não confirmam mudança de tese
estrutural; é uma aposta em continuidade do desmonte técnico, não em
reversão fundamental. Para quem opera o book relativo, a divergência entre
papel (-3,45%) e físico (-0,42%) hoje é, em si, uma operação: comprar basis
(vender CBOT / comprar físico, ou equivalente sintético) capturou um
alargamento de quase 3 pontos percentuais de prêmio em um único dia.

---

## Farelo

**Viés: neutro — a queda de -3,11% no dia foi a menor das três pernas em
termos absolutos, e o dado mais importante da sessão foi que o ratio
Far/Soj SUBIU (não caiu) de 80,02% para 80,29%, o primeiro movimento de
afastamento do piso de 80% em seis sessões, incluindo hoje, dia de queda
generalizada. Isso é a antítese do que se esperaria se o farelo estivesse
liderando a baixa do complexo. Trata `alerta-movimento_forte-farelo_cbot-2026-07-27`
e revisita `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
(checkpoint D+90 em 09/09/2026, já reaberto pela leitura de 26/07 com
veredito de confirmação parcial).**

### O que sustenta a tese

**A queda de hoje foi ampla em volume, mas relativamente a mais suave das
três pernas e com o fechamento tecnicamente menos fraco.** Abertura 330,20
(apenas -0,18% abaixo do fechamento de sexta, o menor gap de abertura das
três commodities), mínima 318,20, máxima 331,80, fechamento 320,50 — uma
queda de -3,11% frente ao fechamento de sexta (330,80). O fechamento
equivale a 16,9% do range do dia ((320,50-318,20)÷(331,80-318,20)) — mais
fraco que o meio do range, mas nitidamente melhor do que a soja (0%) e o
óleo (3,7%). O volume de 39.353 contratos ficou 9,7% acima do de
sexta-feira (35.887) — participação de mercado real, não um ajuste fino.

**Vale registrar, como observação técnica desta leitura (não um alerta
gerado pelo sistema): a mínima de hoje (318,20) ficou abaixo do nível de
325,00, citado nas leituras recentes como suporte técnico** (a antiga
resistência rompida em 22/07). O fechamento de 320,50 também está abaixo de
325,00. O sistema não gerou um alerta específico de `quebra_suporte` para o
farelo hoje (apenas o de `movimento_forte`) — possivelmente porque o
calibrador de níveis usa outro critério de confirmação (ex.: fechamento vs.
intradia, ou uma margem de tolerância) que não é visível a partir deste
briefing; esta leitura registra o fato bruto (fechamento abaixo de 325,00)
como um dado a monitorar, sem reclassificar isso como um alerta formal do
sistema.

**O ratio Far/Soj é o dado mais importante da sessão, e ele foi na direção
OPOSTA à do preço absoluto do farelo.** Sequência da janela: 07-21: 80,37%
→ 07-22: 80,65% → 07-23: 80,13% → 07-24: 80,02% → **07-27: 80,29%**. Depois
de cinco sessões seguidas "encostado" no piso de 80% sem romper (documentado
nas duas últimas leituras como a tensão central do farelo), hoje o ratio se
afastou do piso, subindo 0,27 ponto percentual — **mesmo em um dia de queda
generalizada em que o farelo caiu -3,11% em termos absolutos.** **Mecanismo:**
o ratio é o preço do farelo dividido pelo preço da soja (normalizado); ele
sobe quando o farelo cai MENOS do que a soja, em termos proporcionais — e
foi exatamente isso que aconteceu hoje (farelo -3,11% vs soja -3,45%). Isso
significa que, dentro do desmonte de hoje, o mercado vendeu proporcionalmente
mais soja do que farelo — o oposto do padrão que a tese estrutural bear do
farelo (ABIOVE, Índice de Sobra de Farelo) preveria se estivesse ganhando
tração tática. **Veredito atualizado sobre a revisão D+7** (`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`,
formalmente fechada com "confirmação parcial" na leitura de 26/07, checkpoint
remarcado para D+90 em 09/09/2026): o movimento de hoje reforça, não
enfraquece, essa leitura de impasse — o ratio segue dentro da zona neutra
(80-87%) e, pela primeira vez em seis sessões, se afasta do piso em vez de
testá-lo, sugerindo que o mercado, mesmo sob estresse de liquidação, não
está tratando o farelo como o elo mais fraco do complexo agora.

**O COT de 21/07/2026 (CFTC, ainda o mais recente) seguia fortemente
bullish para o farelo antes do tombo de hoje** — managed money elevou a
compra de 119.347 para 130.152 contratos (+9,1%) e reduziu a venda de
72.771 para 56.676 (-22,1%), net long subindo de 46.576 para 73.476
contratos (+57,8% na semana), 11,89% do open interest (618.289 contratos).
Esse dado ainda não incorpora a sessão de hoje; o próximo corte (28/07,
publicação ~31/07) é o primeiro capaz de mostrar se esses fundos
participaram da venda de hoje ou se mantiveram posição.

**A crush margin caiu para o menor valor de toda a janela observada: 2,8607
USD/bushel** (Board Crush: farelo 320,50 + óleo 70,77 − soja 1.197,50; 07-23:
3,1395 → 07-24: 2,9568 → **07-27: 2,8607**, -3,25% no dia). O mecanismo
segue o mesmo de sempre: a soja (o custo) caiu menos, em termos absolutos de
pontos de bushel, do que a soma farelo+óleo (a receita) — mas em termos
PROPORCIONAIS a soja caiu mais rápido (-3,45% vs. farelo -3,11% e óleo
-3,67% combinados pesando menos no numerador do bushel). A crush segue
positiva e distante de zero, mas no menor nível da janela — uma pressão
adicional, ainda que marginal, sobre o apetite de esmagamento.

**O oil-meal spread caiu para 0,7337 USD/bushel** (ante 0,8041 na sexta,
-8,8%) — a compressão continua, com o farelo ganhando terreno relativo
sobre o óleo dentro do valor do crush pelo terceiro dado seguido nesta
direção, consistente com o ratio Far/Soj subindo.

**As praças físicas de farelo no Brasil (NAG) estão totalmente estáveis
hoje, sem nenhuma variação.** Mato Grosso/IMEA R$ 1.669,72/ton (var 0,0%,
confirmando o salto de +4,18% de 24/07 pelo terceiro dia seguido sem
reversão), Rondonópolis R$ 1.650,00/ton (estável desde 20/07) e RS R$
1.640,00/ton (estável desde pelo menos 14/07). O prêmio de exportação em
Paranaguá segue zerado em +0,05 USD/short ton — o mesmo valor exato desde
03/07/2026 (agora 24 dias corridos sem variação), o pilar mais persistente
da tese estrutural bear (exportar farelo não compete com o mercado
interno).

**O Índice de Sobra de Farelo (ISF) permanece em 80/100 (4 de 5 condições
estruturais), com print de 27/07/2026** — inalterado desde pelo menos
01/07/2026. **A trajetória ABIOVE (sem alteração)** segue mostrando a
exportação de farelo brasileiro projetada caindo de 1.400 mil toneladas em
agosto/2026 para 700 mil toneladas em dezembro/2026 (-50% em quatro meses),
com produção caindo bem menos (2.285,06 → 1.659,04 mil toneladas, -27,4%) —
o excedente segue sendo empurrado para o mercado interno de ração,
sustentando o pilar estrutural bear independentemente do preço diário.

### O que invalida / risco para o farelo

- **Um fechamento abaixo de 318,20** (mínima de hoje) sem um respiro técnico
  antes reforçaria a leitura de desmonte em curso também nesta perna.
- **O ratio Far/Soj devolver o ganho de hoje e fechar abaixo de 80,00%** —
  apesar do afastamento de hoje, o ratio ainda está muito perto do piso
  (0,29pp de distância de 80%, distância semelhante à observada nas
  sessões anteriores); um fechamento abaixo de 80% continuaria a ser o
  gatilho técnico mais relevante para a tese estrutural bear.
- **O próximo corte do COT (28/07, publicação ~31/07) mostrar realização
  de lucro no net long** — a configuração de tensão entre COT bullish e
  ABIOVE/ISF bearish, documentada nas últimas leituras, se resolveria a
  favor da tese estrutural bear se os fundos começarem a vender.
- **O salto do físico em MT/IMEA (+4,18% em 24/07) reverter** — segue
  sem sinal de reversão (terceiro dia estável), mas ainda não tem tempo
  suficiente de confirmação para ser tratado como definitivo.
- **NOPA seguir inacessível** para os checkpoints D+90 (09/09/2026) e D+180
  (08/12/2026) da revisão de 11/06 — trata `release-nopa-2026-07-27`, ainda
  sem dado interpretável (`monthly_status` 0,0 bool, mesma barreira de
  assinatura paga).

### Leitura operacional — farelo

O farelo hoje se comportou como a perna mais "defensiva" do trio — caiu
menos em termos absolutos e, mais importante, o ratio Far/Soj subiu em vez
de cair, o que é uma evidência tática direta contra a hipótese de que o
farelo estivesse liderando a venda. Para quem mantém posição vendida
estrutural (via ABIOVE/ISF), a recomendação segue sendo expressar a tese
via spread (farelo contra soja, ou crush completo) em vez de posição
vendida outright em farelo isolado — o risco de "short squeeze" documentado
nas leituras anteriores permanece, e o comportamento relativo de hoje
(farelo mais forte que soja dentro da queda) reforça esse cuidado. Para quem
opera o spread Far/Soj em si, hoje foi um dia favorável ao lado "farelo
forte / soja fraca" (long farelo, short soja, ou equivalente no ratio) — a
operação relativa de comprar farelo contra óleo dentro do crush (capturando
a compressão do oil-meal spread, -8,8% hoje) segue sendo, nesta leitura, a
forma mais equilibrada de expressar a tensão estrutural sem depender da
resolução binária do ratio.

---

## Óleo

**Viés: bear tático confirmado — o óleo rompeu o suporte técnico de 72,00
cts/lb, fechou a apenas 3,7% do fundo do range (o pior fechamento relativo
das três commodities) e caiu -3,67% no dia, a maior queda percentual do
trio. Isso confirma, na sessão regular de hoje, o gap fino do heating oil
de domingo que a leitura de ontem tratou como "sinal a confirmar, não a
operar". Mas a confirmação veio por outro canal: o próprio heating oil mal
se moveu hoje, e a margem de biodiesel americana na verdade MELHOROU
(+0,78%) — o que sugere que o driver de hoje foi mais o desmonte
correlacionado do complexo do que uma deterioração genuína da margem de
biodiesel. Trata `alerta-quebra_suporte-oleo_cbot-2026-07-27` e
`alerta-movimento_forte-oleo_cbot-2026-07-27`.**

### O que sustenta a tese

**A ruptura do suporte é a confirmação técnica mais clara desta leitura.**
Fechamento 70,77 cts/lb (CBOT, ticker ZLU26.CBT, sessão de 27/07/2026),
abaixo do nível de suporte de 72,00 citado pelo sistema — uma quebra de
1,71% abaixo do nível. Abertura 72,87 (já -0,82% abaixo do fechamento de
sexta, o maior gap de abertura das três commodities, consistente com o aviso
do gap de heating oil do fim de semana), máxima 72,87 (tocada só na
abertura, sem retorno — mesmo padrão de "vender o dia inteiro" visto na
soja), mínima 70,69, fechamento 70,77 — apenas 0,08 cts/lb acima da mínima,
ou **3,7% do range do dia** ((70,77-70,69)÷(72,87-70,69)), o fechamento
tecnicamente mais fraco das três pernas. O volume de 49.159 contratos ficou
6,7% acima do de sexta-feira (46.086) — participação real, não um ajuste
fino.

**Mas o mecanismo por trás da queda não é o que a leitura de ontem havia
antecipado.** O aviso de ontem apontava para o heating oil (o termômetro de
energia usado nesta série para calcular a margem de biodiesel americano)
como o canal de transmissão de uma possível pressão bearish sobre o óleo.
Hoje, porém, o heating oil praticamente não se moveu: fechamento de 3,9862
USD/galão, ante 3,9841 no print revisado de 26/07 (+0,05%, irrelevante), em
apenas **278 contratos de volume — o menor de toda a janela observada por
larga margem**, inclusive menor que os 1.895 contratos (revisados) do
próprio print fino de domingo. **Mecanismo e leitura:** se o driver fosse
mesmo energia (heating oil caindo, comprimindo a margem de biodiesel), o
óleo teria caído por um canal fundamental claro; como o heating oil ficou
estável, a queda do óleo hoje se explica melhor como parte do desmonte
correlacionado das três pernas do complexo (mesmo padrão de volume alto +
fechamento fraco visto na soja) do que como uma história de energia. Esta
leitura trata a confirmação do suporte técnico como real e válida (o preço
de fato rompeu 72,00, com volume), mas rejeita a hipótese de que o
mecanismo causal seja o heating oil — o dado não sustenta essa conexão hoje.

**A prova mais direta disso é a margem de biodiesel americana, que MELHOROU
hoje, não piorou.** Custo do óleo: 5,3077 USD/galão (7,5 lb × 70,77 cts/lb),
ante 5,5103 na sexta (-3,68%). Receita: 7,1512 USD/galão (heating oil 3,99 +
1,5×RIN D4 2,11), ante 7,3456 (-2,65%). Margem: **1,0435 USD/galão**, ante
1,0354 (+0,78%). **Mecanismo:** como o custo do óleo caiu proporcionalmente
mais rápido do que a receita (que depende do heating oil, hoje estável), a
margem de biodiesel — que é o que de fato sustenta a demanda estrutural por
óleo de soja como insumo — na verdade ficou mais atrativa hoje, não menos.
Essa é a tensão mais importante e menos óbvia desta leitura: **o preço do
óleo caiu, mas o incentivo econômico a usá-lo como insumo de biodiesel
aumentou** — um sinal de que a queda de hoje pode ser mais uma oportunidade
técnica de entrada para quem acompanha a tese estrutural do que uma mudança
de fundamento.

**O Índice de Suporte do Óleo (ISO) permanece em 100/100 (5 de 5
condições), com print de 27/07/2026** — a tese estrutural (óleo dominando o
valor do crush) segue formalmente intacta, sem nenhuma alteração apesar do
tombo técnico do dia.

**O oil share caiu para 52,47%** (ante 52,62% na sexta, -0,15 ponto
percentual) — a terceira sessão seguida abaixo da faixa de 53,0-53,5% em
que o indicador vinha oscilando até 22/07. É uma continuação da tendência já
documentada, não um novo choque, mas o acúmulo de três quedas seguidas
merece ser vigiado: se o oil share continuar cedendo, a narrativa estrutural
de "óleo domina o crush" perde força também no dado tático, não só no
absoluto do preço.

**O COT de 21/07/2026 (CFTC, ainda o mais recente) segue confirmando que o
óleo é, de longe, a perna mais concorrida das três** — antes do tombo de
hoje, managed money tinha 143.159 contratos comprados (18,17% do open
interest de 661.652 contratos), o maior percentual entre as três pernas
(soja 12,49%, farelo 11,89%). Esse posicionamento concentrado é, ao mesmo
tempo, a evidência de convicção estrutural dos fundos e o maior risco de uma
correção mais aguda quando o sentimento vira — como parece ter ocorrido
hoje. O próximo corte (28/07, publicação ~31/07) é o dado mais aguardado
para o óleo: vai mostrar se esses 143 mil contratos comprados começaram a
sair.

**A curva forward manteve a backwardation (desconto crescente nos
vencimentos mais distantes) com a forma preservada, apenas deslocada para
baixo.** Agosto/26 (Q26) 71,37 → Setembro/26 (U26, spot) 70,77 (-0,60,
-0,84%) → Outubro/26 (V26) 70,05 (-0,72, -1,02%) → Dezembro/26 (Z26) 69,53
(-0,52, -0,74%) → Janeiro/27 (F27) 69,32 (-0,21, -0,30%) — uma queda total
de -2,05 cts/lb (-2,87%) de agosto a janeiro/27, um pouco menos acentuada em
termos percentuais do que a documentada na leitura de sexta (-3,73%), mas
com a mesma forma geral de aperto físico de curto prazo relativamente aos
vencimentos futuros.

### O que invalida / risco para o óleo

- **Um fechamento amanhã abaixo de 70,69** (mínima de hoje) confirmaria a
  primeira sequência de dois dias de fraqueza desde o início do rali e
  consolidaria a ruptura de 72,00 como mudança de regime técnico, não
  apenas um evento isolado.
- **O heating oil (HO=F) mostrar movimento real na próxima sessão de
  volume normal** — hoje o print veio com apenas 278 contratos, o menor da
  janela; sem confirmação por volume, a hipótese de driver energético segue
  em aberto, não descartada.
- **O oil share continuar caindo abaixo de 52,47%** por mais uma ou duas
  sessões — reforçaria a leitura de perda estrutural de participação do
  óleo no valor do crush.
- **O próximo corte do COT (28/07, publicação ~31/07) confirmar
  liquidação no net long mais concorrido das três pernas (18,17% do OI)** —
  o teste mais direto da hipótese de "desmonte técnico" versus "mudança
  fundamental".
- **A isenção PIS/Cofins do biodiesel expirar em 31/07 sem renovação** (ver
  Lente fiscal), agora a apenas 4 dias — um vetor bearish direto para a
  demanda doméstica de óleo, independente do CBOT e da margem americana.
- **MPOB seguir inacessível** (18º dia consecutivo) — mantém cego o efeito
  de eventuais movimentos no prêmio de substituição via palma.

### Leitura operacional — óleo

O óleo é, nesta leitura, a perna que genuinamente mudou de caráter técnico
hoje — suporte rompido, fechamento no fundo do range, volume elevado — e é
a única das três pernas onde esta leitura recomenda tratar a quebra como
válida para fins operacionais imediatos. Para quem está comprado direcional,
a quebra de 72,00 com volume é motivo concreto para reduzir exposição ou
apertar o stop para a mínima de hoje (70,69); a divergência com a margem de
biodiesel (que melhorou) é um contraponto real, mas não suficiente, por si
só, para ignorar uma ruptura técnica confirmada por volume. Para quem opera
vendido ou tático short, o nível de 70,69 é a referência de entrada mais
recente, com stop acima da máxima de hoje (72,87) — mas vale ponderar que a
margem de biodiesel mais favorável e o ISO ainda em 100/100 significam que
essa é uma aposta em continuidade técnica de curto prazo, não em mudança de
tese estrutural. Para quem opera o crush ou o oil-meal spread, a
compressão do spread (-8,8% hoje, ver Farelo) segue sendo a expressão mais
equilibrada da tensão atual entre as duas pernas de saída do esmagamento.

---

## Spreads e crush — leitura de complexo

### Crush margin: 2,8607 USD/bu — novo menor valor da janela, mas ainda positivo

Caiu -3,25% no dia (2,9568 → 2,8607), o menor valor de toda a série
recente (07-20: 3,0316 → 07-21: 3,1047 → 07-22: 3,1895 → 07-23: 3,1395 →
07-24: 2,9568 → **07-27: 2,8607**). O mecanismo é sempre o mesmo: a soja
caiu proporcionalmente mais rápido do que a soma de farelo e óleo na sessão
de hoje. A crush segue folgada em termos absolutos (bem acima de zero, e
distante do nível de alerta de <2,50 USD/bu citado em leituras passadas),
mas a tendência de compressão nas últimas seis sessões é o dado a monitorar
para avaliar se a esmagadora começa a moderar o ritmo.

### Ratio Far/Soj: 80,29% — primeiro afastamento do piso de 80% em seis sessões

Este é o contraponto mais importante do dia. Depois de cinco sessões
seguidas testando o piso de 80% sem romper (79,28%→80,37%→80,65%→80,13%→
80,02%), hoje o ratio SUBIU para **80,29%** — mesmo em um dia de queda de
-3,45% na soja e -3,11% no farelo. Isso significa que, proporcionalmente,
o mercado vendeu mais soja do que farelo hoje, o oposto do padrão que
confirmaria a tese estrutural bear do farelo ganhando tração tática. A
revisão D+7 de 11/06 (`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`),
já formalmente encerrada como "confirmação parcial" pela leitura de 26/07
com checkpoint remarcado para D+90 (09/09/2026), tem no movimento de hoje
mais um dado a favor do impasse (estrutura bear ABIOVE/ISF ainda de pé, mas
gatilho tático do ratio <80% seguindo sem disparar, e hoje inclusive se
afastando).

### Oil share: 52,47% — terceira sessão seguida abaixo da faixa recente

Caiu -0,15 ponto percentual (52,62% → 52,47%), a terceira queda seguida
desde que o indicador saiu da faixa estreita de 53,0-53,5% em que oscilou
até 22/07. Ainda não é uma ruptura estrutural (o ISO permanece 100/100),
mas a persistência de três quedas seguidas merece registro como tendência a
confirmar.

### Oil-meal spread: 0,7337 USD/bu — compressão de -8,8%, terceira queda seguida

Caiu -8,8% no dia (0,8041 → 0,7337) — o farelo segue ganhando terreno
relativo sobre o óleo dentro do valor do crush, terceira sessão seguida
nessa direção, consistente com a subida do ratio Far/Soj.

### Margem de biodiesel: 1,0435 USD/gal — melhora de +0,78%, tensão direta com a queda do óleo

O único indicador desta leitura que se moveu na direção OPOSTA à do preço:
melhorou +0,78% (1,0354 → 1,0435 USD/gal) porque o custo do óleo caiu mais
rápido do que a receita (heating oil praticamente estável). É o dado mais
importante para entender que a queda do óleo hoje não foi, ao menos pelo
canal do biodiesel americano, uma deterioração fundamental.

### COT: corte de 21/07, ainda o mais recente — o dado mais aguardado desta janela

O corte de 21/07/2026 mostrava fundos extremamente comprados nas três
pernas (net long +73,6% soja, +57,8% farelo, +11,4% óleo na semana). O
tombo de hoje, de alta convicção e correlacionado nas três pernas, é
consistente com o início de uma realização de lucro dessa posição — mas só
o próximo corte (28/07, publicação normal ~31/07) vai confirmar. Esta é,
para todas as três pernas, a peça de informação mais aguardada por esta
leitura.

### ISF em 80/100, ISO em 100/100 — ambos inalterados, prints de 27/07

Os dois índices sintéticos, que captam condições estruturais (não a
mecânica tática de preço intradiário), permanecem exatamente nos mesmos
níveis desde pelo menos 01/07/2026. Eles não se moveram apesar do tombo de
hoje — o que é, em si, informativo: os pilares estruturais (excedente de
farelo, domínio do óleo no crush) não mudaram, o que reforça a leitura de
que hoje foi predominantemente um evento técnico/de posicionamento.

### O que os índices dizem juntos em 27/07/2026

ISF 80/100 + ISO 100/100 (ambos inalterados) + ratio Far/Soj subindo pela
primeira vez em seis sessões (80,29%) + crush margin no menor nível da
janela mas ainda positiva (2,8607) + oil share na terceira queda seguida
(52,47%) + oil-meal spread na maior compressão acumulada (-8,8% hoje,
terceira queda seguida) + margem de biodiesel melhorando (+0,78%,
divergindo da queda do óleo) + COT parado no corte de 21/07 (fundos
extremamente comprados nas três pernas, posição madura para realização de
lucro) formam um quadro coerente: **os pilares estruturais do complexo não
mudaram hoje, mas a posição especulativa que se acumulou na semana de 21/07
parece ter começado a ser desmontada, de forma correlacionada e com volume
real nas três pernas.** O óleo é a única perna em que a confirmação técnica
(ruptura de suporte) e o comportamento de preço (fechamento no fundo do
range) se alinham para justificar tratamento tático imediato; soja e farelo
estão em zona de reteste, não de ruptura confirmada.

---

## Lente fiscal e regulatória BR

**Isenção PIS/Cofins biodiesel — vencimento em 31/07/2026, agora a apenas 4
dias, ainda sem sinalização pública de renovação** (evento
PISCOFINS-BIODIESEL-ISENCAO, `atualizado_em` 2026-06-05, sem mudança desde
então). Trata `trib-PISCOFINS-BIODIESEL-ISENCAO-2026-07-31`. **O mecanismo:**
a isenção incide na saída do biodiesel; se expirar sem renovação, o custo
tributário efetivo da produção sobe, o que tende a reduzir a margem de
biodiesel doméstica (distinta da margem americana calculada nesta leitura,
que hoje melhorou, mas usa RIN D4 e heating oil dos EUA, não o regime
tributário brasileiro) e, por extensão, pressionar a demanda por óleo de
soja como insumo dentro do mix B15 mandatório — um vetor bearish direto para
o óleo doméstico, independentemente do que acontecer no CBOT. Com a semana
de vencimento em curso e o monitor tributário há 53 dias sem qualquer
atualização (`atualizado_em` 2026-06-05 em todos os dez eventos
rastreados), este segue sendo o vetor de maior prioridade de monitoramento
tributário — a decisão (renovar ou deixar expirar) deve sair nos próximos
quatro dias corridos.

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L) —
vigência formal venceu há 18 dias (`vigencia_ate` 11/07/2026), sem qualquer
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
biodiesel), em tensão com a crush margin no menor nível da janela — o
alívio tributário é estrutural, o aperto de crush é tático.

**Vetores dos EUA e Indonésia, sem mudança de status desde 2026-06-05:**
EPA-RFS-2026-2027 (volumes recordes de biocombustível, sustentando o RIN
D4 usado na margem de biodiesel, fixo em 2,11 USD/RIN); 45Z-CLEAN-FUEL
(regra que favoreceria óleo de soja doméstico americano); DANANTARA-INDONESIA
(centralização estatal da exportação de palma, plena em 01/09/2026);
INDONESIA-B50 (provável B45 em 2026, B50 pleno só 2027-28);
INDONESIA-LEVY-PMK9 (imposto de exportação de CPO até 12,5%, encarecendo
palma). Conjunto estruturalmente bullish para óleo de soja via substituição
de palma, mas inverificável pelo lado de mercado (MPOB inacessível há 18
dias, ver Honestidade).

**O monitor tributário como um todo está há 53 dias sem qualquer
atualização** — o intervalo cresce exatamente na semana do vencimento da
isenção PIS/Cofins (4 dias). Prioridade máxima de manutenção do sistema,
independentemente da leitura de preço de hoje.

---

## Riscos e eventos próximos

**A isenção PIS/Cofins do biodiesel vence em 31/07/2026, agora a apenas 4
dias**, sem sinalização de renovação — prioridade máxima de monitoramento
até a resolução.

**O próximo corte do COT (referente a 28/07/2026, publicação normal
~31/07/2026)** é, depois do tombo de hoje, o dado mais aguardado de toda
esta janela — vai mostrar se os fundos que compraram agressivamente as três
pernas na semana de 21/07 (net long +73,6% soja, +57,8% farelo, +11,4%
óleo) começaram a vender, confirmando (ou não) a hipótese central desta
leitura de que hoje foi um desmonte técnico de posição comprada esticada.

**O nível de 1.180,00 na soja está, pela primeira vez desde o rompimento de
julho, a menos de 1,5% de distância do fechamento** — a sessão de amanhã é
a mais importante desta janela para testar se o piso estrutural aguenta uma
segunda onda de venda.

**O heating oil (HO=F) precisa de uma sessão de volume normal para
confirmar (ou desmentir) se há de fato um driver energético por trás da
fraqueza do óleo** — o print de hoje veio com apenas 278 contratos, o mais
baixo da janela.

**O USDA Crop Progress publicou dado novo hoje (26/07)** mostrando piora
marginal de condição (66%→63% bom-ou-excelente) — o próximo corte semanal
(esperado por volta de 02/08) é o dado a acompanhar para ver se a piora
continua.

**NOPA — segue inacessível** (fila `release-nopa-2026-07-27` tratada aqui,
sem dado interpretável, apenas nova data de coleta), sem crush americano
confirmado por fonte primária.

**MPOB — sem números de palma extraídos há 18 dias consecutivos**, mantendo
cego o efeito do El Niño e dos vetores regulatórios indonésios sobre o
prêmio de substituição do óleo de soja.

---

## Honestidade

O que não foi possível validar neste briefing de 27/07/2026, onde a
confiança é baixa ou há lacunas materiais:

**1. O print de heating oil (HO=F) de hoje veio com apenas 278 contratos de
volume — o mais baixo de toda a janela observada, inclusive menor que o
print fino de domingo (1.895 contratos revisados)** — isso sugere fortemente
que o dado de 27/07 para heating oil é parcial/incompleto (possivelmente
capturando só uma fração da sessão), não uma sessão regular plena. Por
causa disso, esta leitura NÃO trata o heating oil como confirmado ou
desconfirmado hoje, e trata a queda do óleo de soja como explicada
principalmente pelo desmonte correlacionado do complexo, não por um canal
energético validado.

**2. O veredito desta leitura — de que o tombo de hoje é majoritariamente
um desmonte técnico de posição comprada (COT) e não uma mudança
fundamental — é uma interpretação, não um fato objetivo do briefing.** Os
argumentos de suporte (volume alto nas três pernas, base física da soja
praticamente estável, margem de biodiesel melhorando, ratio Far/Soj
subindo, ISF/ISO inalterados) são todos dados reais do briefing, mas a
síntese que os conecta a "desmonte técnico" é um julgamento desta análise.
O próximo corte do COT (28/07, publicação ~31/07) é o teste mais direto
dessa hipótese.

**3. A manchete "Is a record soybean crop in the works?" (Farm Progress,
27/07/2026) foi citada sem corpo de matéria disponível neste briefing** —
não há projeção numérica de área ou produção, apenas o título. Esta
leitura não usa essa manchete como pilar quantitativo de nenhuma tese,
apenas como registro qualitativo de uma narrativa que pode estar em tensão
com o bull case construído nas últimas semanas.

**4. O USDA Crop Progress de 26/07/2026 (11%/52%/7%) chegou com uma data
atípica (domingo) para o padrão usual de publicação (segunda-feira à tarde,
horário EUA) documentado em leituras anteriores** — esta leitura trata o
dado como válido (está no briefing, com fonte e data), mas registra a
atipicidade da data de publicação como um ponto que não foi possível
explicar a partir das fontes disponíveis.

**5. A observação de que a mínima do farelo hoje (318,20) ficou abaixo do
nível de suporte de 325,00 citado em leituras anteriores, sem que o sistema
gerasse um alerta de `quebra_suporte` equivalente ao do óleo, não foi
explicada por nenhuma fonte deste briefing** — pode refletir um critério de
calibração diferente (ex.: tolerância de fechamento vs. intradia) que não é
visível a partir daqui; esta leitura registra o fato bruto sem reclassificar
como alerta formal.

**6. Os forecasts estatísticos internos (27/07/2026) mantiveram o rótulo
"altista" para as três commodities mesmo após o tombo de hoje** — como o
modelo usa média móvel de 20 dias + volatilidade + inclinação de curto
prazo, ele tende a reagir com atraso a reversões abruptas de um único dia;
esta leitura não usa esses forecasts como argumento de tese, apenas como
referência de banda estatística, e registra explicitamente essa possível
defasagem.

**7. O prêmio de exportação de farelo em Paranaguá (+0,05 USD/sht) e o de
óleo (+0,08 cts/lb) estão no mesmo valor exato desde pelo menos 03/07/2026**
(NAG, agora 24 dias corridos sem variação de nenhum centavo) — não é
possível distinguir se isso reflete um mercado de exportação genuinamente
parado ou um valor que não está sendo atualizado de fato na fonte.

**8. O COT (CFTC) segue no corte de 21/07/2026, uma terça-feira — não cobre
a sessão de hoje (27/07) nem o fim de semana anterior** — o próximo corte
(28/07, publicação normal ~31/07) é o primeiro capaz de capturar a reação
dos fundos ao tombo de hoje.

**9. Percentis históricos de COT não calculados** — os números de
21/07/2026 seguem lidos apenas em nível absoluto e como fração do open
interest corrente, sem série histórica completa para calibrar se o
posicionamento estava objetivamente "esticado" no sentido histórico (apenas
na comparação semana-a-semana dentro desta janela).

**10. O WASDE segue cobrindo apenas farelo (Argentina, Brasil, China
parcial), sem nenhum dado de soja em grão ou óleo de soja, e sem nenhum
dado dos Estados Unidos, sem atualização desde 10/07/2026 (17 dias)** — a
pergunta "o WASDE mudou o quadro?" da revisão D+7 de 11/06 segue sem canal
de resposta interno.

**11. NOPA (fila `release-nopa-2026-07-27`) segue com `monthly_status` em
0,0 bool** — mesma barreira de assinatura paga documentada desde meados de
junho, agora com quase sete semanas sem alternativa de dado primário sobre
o esmagamento americano.

**12. Palma malaia (MPOB) segue sem números extraídos, agora por 18 dias
consecutivos com o mesmo conteúdo exato (3.439 caracteres, de 10/07 a
27/07/2026)** — a persistência do byte count idêntico segue sugerindo,
possivelmente, uma página que não está mais sendo servida com conteúdo
atualizado.

**13. Clima INMET (BR) não foi usado como driver de preço desta leitura.**
Julho é entressafra da soja brasileira (colheita concluída, plantio só em
outubro) — sem relevância direta para a tese de preço neste momento do
calendário agrícola.

**14. BCBA Argentina — última leitura disponível é 22/07/2026, agora 5 dias
sem atualização**, sem relatórios de esmagamento/exportação acessíveis via
scraper.

**15. RIN D4 como parâmetro fixo (2,11 USD/RIN) segue sendo uma fonte
relevante de incerteza do modelo de biodiesel** — a margem de 1,0435 USD/gal
calculada hoje, assim como todas as anteriores, depende desse valor fixo, o
que significa que toda a série de margem de biodiesel compartilha a mesma
fonte de incerteza estrutural.

*Nenhum número foi inventado ou estimado além do que consta no briefing de
27/07/2026 e nos insights anteriores referenciados. A contribuição central
desta leitura foi (1) documentar a reversão de alta convicção (volume acima
de sexta nas três pernas) que atingiu soja, farelo e óleo simultaneamente;
(2) identificar que o ratio Far/Soj se moveu na direção OPOSTA à intuição
ingênua (subiu, não caiu, mesmo com o farelo em queda absoluta),
atualizando o quadro de impasse da revisão D+7 de 11/06; (3) identificar e
explicitar a divergência entre a queda do óleo e a melhora da margem de
biodiesel americana, uma tensão que argumenta contra um driver fundamental
de energia por trás da queda do óleo hoje; e (4) sinalizar que o print de
heating oil de hoje tem volume baixo demais (278 contratos) para ser
tratado como confirmação plena do gap de domingo.*
