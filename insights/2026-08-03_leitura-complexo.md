---
data: 2026-08-03
titulo: "Reversão ampla na reabertura da semana — óleo salta +2,26% e fecha a 95,8% da máxima do dia mesmo abaixo do suporte técnico de 72,00, soja recupera de uma mínima nova (1.158,50) puxada por manchete de flash sale USDA para China e comprador não identificado, e o ratio Far/Soj volta a comprimir (80,57%) sem confirmar a zona <80% — o D+7 do gatilho tático completa 46 dias vencido"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT (ZSU26 soja / ZMU26 farelo / ZLU26 óleo) — sessão de 2026-08-03, primeira sessão completa após o fim de semana, com abertura/máxima/mínima/fechamento/volume próprios (a mais líquida das três é o óleo, 35.940 contratos)
  - CME NYMEX heating oil (HO=F) — 2026-08-03, fechamento 3,8704 USD/galão, volume de apenas 26 contratos — tratado com cautela extrema (ver Óleo e Honestidade)
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, paridade BR, Índice de Sobra de Farelo, Índice de Suporte do Óleo) — recalculados com o fechamento de 2026-08-03
  - BCB PTAX — 2026-08-03 (USD/BRL 5,0723, EUR/BRL 5,8382, Selic diária 0,052531% a.a.)
  - CEPEA/ESALQ Soja Paranaguá via NAG — 2026-08-03 (R$ 144,04/saca, var -0,6%)
  - CEPEA/ESALQ Soja Paraná interior via NAG — 2026-08-03 (R$ 136,66/saca, var -0,44%)
  - NAG Físico BR — 2026-08-03 (farelo MT/IMEA R$ 1.675,10/ton; Rondonópolis R$ 1.700,00/ton; RS R$ 1.640,00/ton, os três com var 0,0%; prêmios export PGUA farelo +0,05 USD/sht e óleo +0,08 cts/lb, agora rotulados "mês Agosto/26")
  - CFTC COT Managed Money — corte de 2026-07-28 (sem corte novo nesta janela; o próximo, referente a 2026-08-04, só sai por volta de 2026-08-07)
  - USDA Crop Progress — corte rotulado 2026-08-02 com os MESMOS valores do corte de 2026-07-26 (11% excelente / 52% boa / 7% ruim) — tratado como pendente de confirmação, não como segunda semana genuinamente estável (ver Honestidade)
  - USDA WASDE — ausente da janela, 24 dias de atraso desde o último dado (2026-07-10)
  - NOPA — fila `release-nopa-2026-08-03`, `monthly_status` continua em 0,0 bool (paywall)
  - ABIOVE projeções mensais — balanços ago-dez/2026, sem alteração frente ao dump anterior
  - NOAA CPC ENSO — 2026-08-03 (El Niño Advisory, inalterado)
  - MPOB — 2026-08-03 (mesmo conteúdo de 3.439 caracteres, parser sem números extraídos)
  - BCBA Argentina — última leitura confirmada 2026-08-02 (acessível, sem links de relatório); sem carimbo novo de 2026-08-03 neste dump
  - Notícias Agrícolas/Farm Progress/Canal Rural RSS — 2026-08-03 (160 itens lidos, 8 mantidos; manchete "USDA Exports: China, unknown buyer soybeans, Aug. 3, 2026", farmprogress.com/marketing/flash-sales — sem corpo de texto extraído, ver Honestidade)
  - system/tributario_watch.toml (lido como referência, não editado) — `atualizado_em` 2026-06-05, agora 59 dias sem atualização; evento `PISCOFINS-BIODIESEL-ISENCAO` com `vigencia_ate` 2026-07-31 — hoje é o primeiro dia de expediente público desde o vencimento
  - Cruza com [[2026-08-02_leitura-complexo]], [[2026-08-01_leitura-complexo]] e [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (tese original do D+7, tratada abaixo)
status: ativa
vies: [bull-soja, neutral-farelo, neutral-oleo_soja]
---

## Visão geral

O complexo soja é, mecanicamente, uma fábrica com uma única matéria-prima
(a soja em grão) e dois produtos de saída em proporção fixa por bushel
esmagado: o **farelo** (a fração proteica, ~78% da massa, vira ração
animal) e o **óleo degomado** (a fração de gordura, ~18-20% da massa, vira
óleo de cozinha e biodiesel). Quem decide o ritmo de esmagamento é a
esmagadora, olhando dois números: a **crush margin** (o valor de farelo +
óleo por bushel, menos o custo daquele bushel de soja, todos medidos na
CBOT — Chicago Board of Trade, a bolsa de referência mundial para esses
três contratos) e o **oil share** (a fração desse valor capturada
especificamente pelo óleo). Quando o oil share sobe, o óleo "manda" no
crush — a esmagadora esmaga pela margem do óleo e aceita vender o farelo
mais barato, porque o farelo virou, na prática, o subproduto que sobra. O
**ratio Far/Soj** (preço do farelo dividido pelo preço da soja, normalizado
pela conversão bushel↔short ton) mede a mesma dinâmica por outro ângulo:
abaixo de 80% o farelo está historicamente "abundante" frente à soja —
zona baixista para o farelo —, acima de 87% está "apertado" — zona
altista —, e entre os dois fica a zona neutra de mean-reversion (o preço
tende a voltar pro meio quando se afasta demais de um extremo).

**Hoje, 2026-08-03, segunda-feira, foi a primeira sessão completa de
pregão desde a sexta-feira 31/07 — e ela trouxe o movimento de preço mais
forte e mais amplo desta série de leituras em várias semanas.** As três
pernas abriram em queda e, em graus diferentes, reverteram para fechar
perto da máxima do dia. O destaque é o **óleo**: abriu a 66,99 cts/lb,
caiu até 66,51 (nova mínima, abaixo até da mínima de sexta), e fechou em
**68,78 cts/lb**, um salto de **+2,26%** frente ao fechamento revisado de
sexta (67,26) e a **95,8% do range do dia** ((68,78-66,51)÷(68,88-66,51))
— um candle de reversão quase perfeito, com volume de 35.940 contratos,
o mais líquido dos três hoje. A **soja** teve o mesmo desenho em escala
menor: abriu a 1.167,00, tocou uma mínima nova de **1.158,50** (abaixo da
mínima de sexta, 1.164,00) e fechou em **1.174,00**, **+0,28%** sobre
sexta e a 83,8% do range do dia. O **farelo** subiu de forma mais discreta,
+0,13%, para 315,30 USD/short ton, fechando a 76,1% do range. O gatilho
mais plausível para o salto de soja é uma manchete do próprio dia, ainda
sem corpo de texto extraído neste briefing: "USDA Exports: China, unknown
buyer soybeans" (Farm Progress, 03/08/2026) — o sistema diário de flash
sales do USDA, que só dispara quando uma venda isolada ultrapassa 100 mil
toneladas para um destino único num único dia. Tratado com a cautela
devida (ver Honestidade), esse é o tipo de notícia que historicamente move
o CBOT de soja no mesmo pregão. **Mas nem tudo caminhou junto**: a margem
de biodiesel americana, que sustenta parte da demanda de óleo como
insumo, **caiu -25,3%** hoje (de 1,4420 para **1,0769** USD/galão),
puxada por um heating oil (HO=F) que fechou a 3,8704 USD/galão com
**apenas 26 contratos negociados** — o volume mais baixo já visto nesta
série, tratado aqui como print não confiável, não como sinal fundamental
(ver Óleo e Honestidade). **Leitura de uma linha:** o pivô do complexo
hoje é uma reversão técnica ampla, mais forte no óleo, coincidindo com uma
notícia de demanda de exportação ainda não confirmada em detalhe; a maior
convicção desta leitura é que o movimento de preço de hoje é
genuinamente novo e relevante, mas nenhuma das teses estruturais de médio
prazo (óleo dominando o crush, farelo estruturalmente sobrando) foi
desfeita por uma única sessão; confiança moderada — alta para a leitura
técnica (dados de fechamento sólidos, volumes normais em soja/farelo/óleo),
baixa para a leitura fundamental do dia (heating oil sem liquidez,
manchete de exportação sem tonelagem confirmada).

---

## Soja

**Viés: bull tático — reversão de uma mínima nova para um fechamento
acima do fechamento de sexta, com posição de 83,8% do range do dia,
possivelmente puxada por uma manchete de exportação ainda não detalhada.**
Fechamento: 1.174,00 cts/bushel (CBOT, ticker ZSU26.CBT, 2026-08-03).

### O que sustenta a tese

**A sessão abriu fraca, testou uma mínima abaixo da mínima de sexta e
reverteu com força.** Abertura 1.167,00, mínima **1.158,50** (abaixo dos
1.164,00 de sexta — ou seja, o mercado ainda tentou empurrar o preço para
baixo antes de reverter), máxima 1.177,00, fechamento **1.174,00**. A
posição do fechamento dentro do range (83,8%) é a mais forte desta série
recente — comparável, em desenho, à reversão do óleo no mesmo pregão.
Ainda assim, **a resistência de 1.180,00**, identificada nas leituras
anteriores como o nível que romperia a sequência de máximas decrescentes,
segue intocada: a máxima de hoje (1.177,00) chegou perto, mas não
ultrapassou. O volume de 23.488 contratos é saudável, sem sinal de
liquidez anômala.

**A manchete do dia é o elemento genuinamente novo desta leitura.** "USDA
Exports: China, unknown buyer soybeans, Aug. 3, 2026" (Farm Progress,
via RSS Notícias Agrícolas, 03/08/2026) — o formato do título ("China,
unknown buyer") sugere que o relatório diário de flash sales do USDA
registrou vendas para dois destinos no mesmo dia, um identificado como
China e outro não identificado. **Mecanismo:** o sistema de flash sales
só dispara alerta quando uma venda isolada ultrapassa 100 mil toneladas
métricas para um único destino num único dia — é, por desenho, um sinal
de demanda concentrada e relevante, historicamente um dos catalisadores
mais diretos de alta intradiária no CBOT de soja. Se a contraparte "China"
for confirmada, é um dado ainda mais relevante: as leituras dos últimos
dias mencionavam repetidamente a incerteza sobre o retorno chinês às
compras de soja americana como o principal vetor de cauda altista para a
soja. Esta leitura trata a manchete como o candidato mais forte para
explicar a reversão de hoje, mas **não converte isso em certeza**: o
briefing não trouxe tonelagem, preço ou confirmação oficial USDA-FAS, só
o título da notícia (ver Honestidade).

**Câmbio e paridade BR seguem favoráveis à soja em reais, mas o prêmio de
exportação comprimiu.** USD/BRL PTAX fechou em 5,0723 (BCB, 2026-08-03),
-0,10% frente a sexta (5,0773) — um real ligeiramente mais forte, que
reduz (marginalmente) a atratividade da paridade em reais para quem
compara com o físico. Ainda assim, a paridade teórica em reais subiu para
**R$ 131,28/saca** (indicators, CBOT 1.174,00 cts × USD/BRL 5,0723),
**+0,18%** sobre sexta (131,05) — o efeito do CBOT mais alto superou o
efeito do câmbio mais forte. Do lado físico, a CEPEA/ESALQ Soja Paranaguá
(via NAG) recuou para **R$ 144,04/saca** (2026-08-03, var -0,6%), e a
Soja Paraná interior caiu para R$ 136,66/saca (var -0,44%). Cruzando os
dois lados, o **prêmio de exportação via Paranaguá comprimiu de +10,58%
para +9,72%** ((144,04-131,28)÷131,28) — o físico de exportação ficou
relativamente mais barato frente ao papel hoje, na direção oposta à
notícia de demanda chinesa: se a manchete de flash sale for confirmada,
seria de esperar o prêmio físico subir, não cair, o que é um ponto de
atenção (ver O que invalida).

**O posicionamento do COT (CFTC, corte de 28/07/2026) segue sendo o
retrato mais recente — nenhum corte novo hoje.** O managed money net long
em soja estava em 160.479 contratos (15,73% do open interest de
1.020.108), após uma alta de +22,97% na semana anterior ao corte, num
período em que o preço ainda rondava o topo recente (fechamento de 28/07:
1.204,75). Entre esse fechamento e a mínima de hoje (1.158,50), a soja
caiu -3,84% — uma fatia relevante da posição comprada reforçada naquela
semana ainda estava, até a reversão de hoje, com prejuízo de papel. A
recuperação de hoje até 1.174,00 reduz essa dor (-2,55% frente ao
fechamento de 28/07, ante -3,84% na mínima), mas não a elimina — o risco
de liquidação forçada de posição comprada segue latente até o próximo
corte do COT (referente a 04/08, publicado por volta de 07/08).

### O que invalida / risco para a soja

- **A manchete "China, unknown buyer" não se confirmar como venda de
  volume relevante**, ou o buyer "unknown" não ser um destino
  genuinamente novo — nesse caso, a reversão de hoje perde seu candidato
  mais forte de explicação fundamental e passa a ser tratada como técnica
  pura (short covering pós-mínima nova).
- **A resistência de 1.180,00 seguir intocada** em sessões futuras —
  mantém o padrão de máximas decrescentes mesmo com o fechamento mais
  forte de hoje.
- **O prêmio de exportação físico continuar comprimindo** em vez de subir
  — divergiria do que se esperaria de uma notícia de demanda chinesa
  genuína.
- **A posição comprada esticada do COT de 28/07 (15,73% do OI) se
  desmontar de forma desordenada** caso o preço volte a cair antes do
  próximo corte (07/08).
- **O câmbio abrir mais forte** — reduziria a paridade em reais
  independentemente do que acontecer no CBOT.

### Leitura operacional — soja

Para quem opera os dois lados: a reversão de hoje, saindo de uma mínima
nova, é o tipo de candle que tecnicamente justifica reduzir ou zerar
posição vendida tática aberta na sequência de máximas decrescentes das
últimas sessões — o stop natural para quem ficou vendido é a máxima de
hoje (1.177,00) ou, mais conservador, o rompimento de 1.180,00. Para quem
busca posição comprada nova, o ideal é confirmar a manchete de flash sale
antes de aumentar exposição — comprar apenas no preço, sem saber a
tonelagem real por trás da notícia, é apostar na interpretação, não no
fato. A recomendação mais concreta é **checar o relatório diário de
exportação do USDA-FAS (flash sales) antes da abertura de amanhã**, já
que é o único elemento genuinamente qualitativo em aberto nesta leitura.

---

## Farelo

**Viés: neutro — alta modesta de preço (+0,13%) convivendo com uma nova
leve compressão do ratio Far/Soj, que segue sem confirmar a zona <80%
mesmo 46 dias depois do checkpoint formal do D+7.** Trata
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` (fila
de hoje) e `release-nopa-2026-08-03` (mesmo bloqueio, ver abaixo).
Fechamento: 315,30 USD/short ton (CBOT, ticker ZMU26.CBT, 2026-08-03).

### O D+7 chega a 46 dias vencido — o ratio se aproxima, mas não confirma

A tese original ([[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]])
apostava que a compressão rápida do ratio em junho (83,3%→81,4% em 4
pregões) levaria à zona comprimida (<80%) "em 1-2 semanas". O checkpoint
formal caiu em 18/06/2026; hoje, 03/08/2026, são **46 dias corridos**
sem que o ratio tenha fechado de forma robusta abaixo de 80%. O dado de
hoje, porém, é o mais próximo do piso em várias sessões: o ratio caiu de
**80,69% (31/07, revisado) para 80,57% (03/08)**, uma compressão de
-0,12 ponto percentual. **Mecanismo do movimento de hoje:** apesar de o
farelo ter subido em termos absolutos (+0,13%), a soja subiu mais em
termos relativos ao denominador do ratio (a soja fechou +0,28% e a
manchete de exportação chinesa reforça o numerador do lado errado para o
farelo) — o ratio caiu porque o denominador (soja) correu mais rápido que
o numerador (farelo), não porque o farelo ficou mais barato em dólares.
Essa é exatamente a mecânica que sustenta a tese estrutural: quando a
soja sobe puxada por demanda de grão inteiro (exportação, e não por
demanda de farelo), o crush overhead aumenta e o farelo relativo fica
ainda mais "sobrando". O próximo marco formal continua sendo o D+90
(2026-09-09, a 37 dias de hoje).

### O que sustenta a leitura de hoje

**Crush margin e oil-meal spread subiram junto com o rali de óleo — mas
isso é bullish para a margem da esmagadora, não para o farelo em si.**
Crush margin de **2,7624 USD/bushel** (farelo 315,30 + óleo 68,78 − soja
1.174,00), **+5,48%** sobre sexta (2,6189) — folga maior sobre o nível de
alerta histórico (<2,50 USD/bu), reduzindo a pressão imediata sobre a
esmagadora. O oil-meal spread (óleo menos farelo, em USD/bushel) saltou
**+33,64%**, de 0,4708 para **0,6292 USD/bushel** — a maior alta em um
único dia desta série, mas o movimento é quase inteiramente explicado
pelo salto do óleo (+2,26%), não por fraqueza do farelo. **Mecanismo:**
quanto maior o oil-meal spread, mais a esmagadora é incentivada a
continuar esmagando pela margem do óleo, o que mantém o fluxo de farelo
saindo da fábrica no mesmo ritmo — reforça, e não alivia, a tese
estrutural de que o farelo é o subproduto que sobra.

**As praças físicas de farelo no Brasil (NAG) seguem completamente
travadas, mesmo na reabertura de segunda-feira.** Mato Grosso/IMEA em R$
1.675,10/ton, Rondonópolis/MT em R$ 1.700,00/ton e RS em R$ 1.640,00/ton
— todas com var 0,0% hoje, o mesmo valor de sexta-feira. É notável que
nem mesmo a reabertura da semana tenha movido essas três referências,
enquanto a soja física (Paranaguá e Paraná interior) se moveu
normalmente no mesmo dia — um sinal de que o mercado físico de farelo BR
está com liquidez ainda mais baixa que o normal, ou simplesmente sem
pressão de repreficação de nenhum dos dois lados. O prêmio de exportação
em Paranaguá segue zerado em **+0,05 USD/short ton**, agora rotulado
"mês Agosto/26" — ou seja, o indicador atravessou a virada do mês de
referência (julho→agosto) sem qualquer variação, reforçando que este é o
pilar mais persistente e mais tempo parado desta tese estrutural bear.

**O Índice de Sobra de Farelo (ISF) permanece em 80/100 (4 de 5
condições estruturais)**, o mesmo valor de todas as sessões recentes,
confirmando que nenhum insumo estrutural novo (ABIOVE, condições de
crush de mais longo prazo) mudou hoje. As projeções ABIOVE seguem
mostrando a exportação de farelo brasileiro caindo de 1.400 mil
toneladas em agosto/2026 para 700 mil toneladas em dezembro/2026, uma
queda de -50% em quatro meses (ABIOVE projeções mensais, sem alteração
frente ao dump anterior) — o driver estrutural mais lento e mais
persistente desta tese, independente do ruído tático do ratio.

**`release-nopa-2026-08-03` (fila de hoje) sinaliza um novo carimbo, mas
o `monthly_status` permanece em 0,0 bool** — a mesma barreira de
assinatura paga documentada desde meados de junho, agora quase 8 semanas
sem alternativa de dado primário sobre o crush americano. Tratado como
item da fila resolvido (sem conteúdo novo para incorporar), não como
pendência de leitura.

### O que invalida / risco para o farelo

- **O ratio Far/Soj precisa fechar de forma robusta e repetida abaixo de
  80%** — hoje chegou mais perto (80,57%), mas ainda não confirmou; um
  fechamento amanhã abaixo de 80% seria o primeiro teste real em 46 dias.
- **A manchete de exportação de soja (se confirmada como venda grande)
  puxar o numerador do ratio ainda mais para baixo** nos próximos dias,
  adiando de novo a confirmação.
- **O prêmio de exportação em Paranaguá sair de zero** depois de mais de
  um mês parado — quanto mais tempo passa, maior a chance de que a
  próxima variação seja abrupta.
- **As praças físicas travadas (MT/IMEA, Rondonópolis, RS) começarem a se
  mover de forma abrupta** quando a liquidez normalizar — o
  represamento de preço por várias sessões seguidas tende a se resolver
  com um salto, não com uma caminhada suave.

### Leitura operacional — farelo

Para quem opera o oil-meal spread ou o crush como posição relativa, o
salto de hoje (+33,64%) foi impulsionado pelo óleo, não por fraqueza do
farelo — não é, por si só, um sinal de entrada nova no spread, mas
reforça que a esmagadora segue com todo incentivo a manter o ritmo de
crush. Para quem monitora o ratio Far/Soj como gatilho tático (long
farelo/short soja ou vice-versa na convergência), 80,57% ainda não é
80% — a recomendação desta leitura continua sendo tratar qualquer
fechamento futuro perto do piso com ceticismo até sobreviver a uma
revisão do dia seguinte, dado o histórico de revisões nesta série.

---

## Óleo

**Viés: neutro com forte viés tático de alta — a reversão de preço mais
expressiva da sessão (+2,26%, fechando a 95,8% do range), mas ainda
abaixo do suporte técnico de 72,00 e com a margem de biodiesel em queda
acentuada num print de heating oil de liquidez quase nula.** Trata
`alerta-quebra_suporte-oleo_cbot-2026-08-03` (fato: 68,78 vs nível
72,00). Fechamento: 68,78 cts/lb (CBOT, ticker ZLU26.CBT, 2026-08-03).

### O que sustenta a tese (e o que a contradiz, no mesmo dia)

**Tecnicamente, hoje foi o dia mais forte do óleo em toda esta janela de
leituras.** Abertura 66,99, mínima **66,51** (nova mínima, abaixo dos
66,66 de sexta), máxima 68,88, fechamento **68,78** — um candle de
reversão em V quase perfeito, fechando a apenas 0,10 cts/lb da máxima do
dia. O volume de 35.940 contratos é o mais alto dos três legs hoje, o que
dá mais peso ao movimento do que se fosse um salto de baixa liquidez. Em
termos de nível, porém, **68,78 continua -4,47% abaixo do suporte técnico
de 72,00** que a fila de julgamento monitora desde 31/07 — a quebra de
suporte não foi desfeita, apenas testada e (por ora) sustentada de baixo
para cima.

**A contradição do dia está na margem de biodiesel americana, que caiu
-25,3% mesmo com o óleo mais caro.** Margem = receita (heating oil +
1,5×RIN D4) menos custo (óleo de soja + fator industrial fixo de 0,80).
O custo subiu para **5,1585 USD/galão** (+2,26%, acompanhando o óleo mais
caro — mecanicamente, óleo mais caro é custo mais alto pra quem fabrica
biodiesel). Mas a receita **caiu** para **7,0354 USD/galão** (-3,44%
sobre sexta), porque o heating oil (HO=F) — metade da receita, a outra
metade é o RIN D4, fixo em 2,11 USD/RIN — fechou a **3,8704 USD/galão**,
bem abaixo do fechamento revisado de sexta (4,1215). O resultado é a
margem de biodiesel caindo para **1,0769 USD/galão**, a mais baixa desta
série recente. **Só que esse número de heating oil negociou apenas 26
contratos hoje** — o volume mais baixo já visto nesta série (o recorde
anterior de baixa liquidez, 1.010-1.138 contratos no fim de semana, já
havia sido tratado como anômalo). Esta leitura trata a margem de
biodiesel de hoje como **não confirmada**: o custo (lado óleo) é
confiável, porque vem de um contrato com 35.940 contratos negociados; a
receita (lado heating oil) não é, porque vem de um contrato com liquidez
quase nula, possivelmente um artefato de rolagem de contrato futuro ou
falha de coleta (ver Honestidade). Não dá para afirmar hoje que a margem
de biodiesel genuinamente comprimiu -25% — apenas que o número calculado
caiu, com uma ressalva de confiabilidade forte.

**O Índice de Suporte do Óleo (ISO) permanece em 100/100 (5 de 5
condições)**, o mesmo valor de todas as sessões recentes — a tese
estrutural (óleo dominando o valor do crush) segue formalmente intacta.
É importante não confundir as duas coisas: o ISO mede QUEM CAPTURA MAIS
VALOR dentro do crush (óleo vs. farelo), não se o preço do óleo está caro
ou barato em termos absolutos ou se está acima/abaixo de um suporte
técnico — hoje as três leituras (ISO em máximo, preço rompendo pra cima
dentro de uma estrutura ainda abaixo do suporte, e margem de biodiesel
caindo por um dado suspeito) coexistem sem se contradizer tecnicamente,
mas exigem cuidado para não misturar os planos.

**Sem COT novo nesta janela** — o corte de 28/07/2026 segue sendo a
fotografia mais recente, mostrando os fundos reduzindo o net long em
óleo (-10,27% na semana, para 16,60% do open interest) durante a própria
sequência de quebra técnica que estava em curso naquela semana — ao
contrário do padrão de "compra na fraqueza" visto em soja e farelo. Do
fechamento de 28/07 (70,14) até a mínima de hoje (66,51), o óleo havia
caído -5,18%; a recuperação até 68,78 reduz essa distância para -1,94%.
Como o book especulativo em óleo tinha, proporcionalmente, menos posição
comprada "presa" em prejuízo do que soja e farelo, o espaço para um
short-covering rápido como o de hoje é consistente com o posicionamento
observado no corte de 28/07.

### O que invalida / risco para o óleo

- **O heating oil confirmar amanhã, com volume normal, um nível
  genuinamente mais fraco que o fechamento revisado de sexta (4,1215)** —
  validaria a compressão da margem de biodiesel como um sinal real, não
  como ruído de liquidez.
- **O heating oil reverter para perto de 4,10-4,12 com volume normal** —
  nesse caso, o print de hoje (3,8704, 26 contratos) deve ser descartado
  como artefato, e a margem de biodiesel recalculada ficaria muito mais
  próxima da de sexta.
- **Um fechamento consistente de volta abaixo de 66,51 (mínima de hoje)**
  desfaria a leitura de reversão e devolveria o óleo à sequência de
  quebra técnica.
- **A isenção PIS/Cofins do biodiesel seguir sem renovação após a
  reabertura de expediente público de hoje** (ver Lente fiscal) — o teste
  real deste vetor começa agora.
- **O oil share continuar em níveis elevados (52,17% hoje) sem tradução
  em alta sustentada de preço** — mantém a tese estrutural sem validar a
  tese de preço.

### Leitura operacional — óleo

Para quem estava vendido na sequência de quebra de suporte, a reversão de
hoje — volume saudável, fechamento a 95,8% do range — é o primeiro sinal
técnico real para considerar reduzir ou proteger a posição, com stop
natural abaixo da mínima de hoje (66,51). Para quem busca comprado tático,
a entrada faz mais sentido acima da máxima de hoje (68,88) do que no
fechamento, dado que o nível de 72,00 (suporte rompido, agora resistência
a testar) ainda está distante e a margem de biodiesel — um dos pilares
fundamentais que sustentariam uma alta mais duradoura — está em dúvida
por causa do heating oil de liquidez anômala. A recomendação mais
concreta é **não tratar a margem de biodiesel de hoje (1,0769) como
número definitivo até o heating oil negociar com volume normal amanhã**.

---

## Spreads e crush (leitura de complexo)

**Ratio Far/Soj: 80,57% (03/08), compressão de -0,12pp sobre sexta,
ainda sem confirmar a zona <80% — D+7 formal vencido há 46 dias.** O
movimento de hoje é tecnicamente na direção certa para a tese estrutural
bear do farelo (mais perto do piso), mas puxado pela alta da soja
(possível notícia de exportação), não por fraqueza do farelo em si — um
detalhe que importa para quem confia no ratio como gatilho de convergência:
o "motor" da compressão de hoje foi o numerador errado.

**Crush margin: 2,7624 USD/bu, +5,48% sobre sexta — folga maior sobre o
nível de alerta (<2,50 USD/bu).** O rali de óleo puxou a margem para
cima com força; a esmagadora tem hoje mais espaço de manobra do que em
qualquer sessão recente desta série.

**Oil share: 52,17%, +0,53pp sobre sexta — o óleo capturou ainda mais
fatia do valor do crush hoje**, consistente com seu desempenho de preço
muito mais forte que o do farelo na mesma sessão.

**Oil-meal spread: 0,6292 USD/bu, +33,64% no dia — a maior alta em um
único pregão desta série**, refletindo quase inteiramente o salto do
óleo.

**Heating oil: fechamento fraco (3,8704) com volume quase nulo (26
contratos) — tratado como não confiável, não como sinal fundamental.**
Este é o único ponto de fricção genuína entre a leitura técnica de hoje
(bullish, especialmente no óleo) e a leitura fundamental derivada dela
(margem de biodiesel em queda) — a fricção existe porque o dado que
sustentaria a leitura fundamental tem qualidade duvidosa, não porque as
duas leituras sejam inerentemente incompatíveis.

**ISF em 80/100, ISO em 100/100 — ambos inalterados.** Nenhum insumo
estrutural novo (ABIOVE, condições de crush) entrou no cálculo hoje;
ambos os índices sintéticos continuam medindo a mesma fotografia
estrutural (farelo estruturalmente abundante, óleo estruturalmente
dominante no valor do crush) que vinha sendo descrita nas leituras
anteriores.

**O que os índices dizem juntos hoje:** o complexo teve, na sessão de
hoje, seu movimento de preço mais forte e mais amplo em várias semanas —
mas as métricas estruturais (ISF, ISO, ABIOVE) não se moveram, porque
elas capturam dinâmicas de mais longo prazo (safra, exportação,
sazonalidade do crush) que uma única sessão de reversão técnica não
altera. A leitura mais honesta é que hoje foi um dia de repreciação
tática relevante dentro de uma estrutura que continua, por enquanto,
inalterada.

---

## Lente fiscal e regulatória BR

**Isenção PIS/Cofins do biodiesel (`PISCOFINS-BIODIESEL-ISENCAO`,
`vigencia_ate` 2026-07-31) — hoje, 2026-08-03, segunda-feira, é o
primeiro dia de expediente público desde o vencimento.** Sábado e domingo
não contam para fins administrativos; hoje é o teste real. O briefing de
hoje não trouxe nenhuma manchete específica sobre renovação ou
caducidade da isenção — o RSS trouxe 8 itens mantidos, mas nenhum sobre
este tema específico. **Mecanismo e leitura:** se a isenção de fato
caducou sem renovação, o custo de produção do biodiesel brasileiro sobe
(a saída deixa de ser isenta), o que reduz a competitividade do
biodiesel dentro do mix mandatório e pressiona a demanda de óleo de soja
como insumo doméstico — um vetor bearish direto para o óleo, distinto e
adicional a qualquer coisa que aconteça no CBOT. Como o monitor
tributário (`system/tributario_watch.toml`) está parado desde
2026-06-05 (**59 dias sem atualização**), esta leitura não pode confirmar
nem descartar a caducidade — é o item de verificação manual mais urgente
desta janela.

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L)
— vigência formal venceu há 23 dias** (`vigencia_ate` 11/07/2026), sem
qualquer atualização de status no monitor.

**MP 1.363/2026 — subsídio ao diesel fóssil (R$ 1,12/L), em vigor até
31/12/2026, sem alteração.** Bearish estrutural persistente: enquanto o
diesel fóssil segue subsidiado no mix B15, o biodiesel via óleo de soja
compete em desvantagem — o mesmo vetor de todas as leituras recentes,
agora potencialmente reforçado se a isenção PIS/Cofins também tiver
caducado.

**B16 — sem data, travado em B15, sem mudança de status.** Cada +1pp de
mistura obrigatória de biodiesel puxaria demanda adicional de óleo de
soja para o mercado interno (~+436 mil toneladas no B16 pleno), mas o
CNPE segue sem nova convocação.

**STJ REsp 2.165.276/2026 — crédito PIS/Cofins para esmagadoras sobre
soja usada em biodiesel, sem alteração.** Bullish para soja/óleo (alívio
de custo de entrada), mas ainda não vinculante (não é decisão
repetitiva).

**Vetores dos EUA e Indonésia, sem mudança de status desde 2026-06-05:**
EPA-RFS-2026-2027 (volumes recordes de biocombustível, sustentando o
RIN D4 fixo em 2,11 USD/RIN usado na margem de biodiesel); 45Z-CLEAN-FUEL
(regra que favoreceria óleo de soja doméstico americano frente a insumo
importado); DANANTARA-INDONÉSIA (centralização estatal da exportação de
palma, plena em 01/09/2026, agora a 29 dias); INDONESIA-B50 (provável
B45 em 2026, B50 pleno só 2027-28); INDONESIA-LEVY-PMK9 (imposto de
exportação de CPO até 12,5%, encarecendo palma). Conjunto
estruturalmente bullish para óleo de soja via substituição de palma, mas
inverificável pelo lado de mercado (MPOB inacessível, ver Honestidade).

**O monitor tributário como um todo está há 59 dias sem qualquer
atualização** — prioridade de manutenção do sistema, e especialmente
relevante hoje, primeiro dia útil após o vencimento da isenção
PIS/Cofins.

---

## Riscos e eventos próximos

**A manchete de flash sale ("China, unknown buyer") precisa de
confirmação de conteúdo e tonelagem** — é o candidato mais forte para
explicar a reversão de soja de hoje, mas segue sem corpo de texto neste
briefing.

**O heating oil precisa negociar com volume normal amanhã** para validar
ou descartar o print de hoje (3,8704, 26 contratos) e a margem de
biodiesel calculada a partir dele (1,0769, -25,3%).

**A isenção PIS/Cofins do biodiesel — hoje é o primeiro dia de
expediente público desde o vencimento (31/07)** — item de verificação
manual mais urgente desta janela.

**O ratio Far/Soj está em 80,57%, o mais próximo do piso de 80% em várias
sessões, com o D+7 formal vencido há 46 dias** — monitorar se o
movimento de hoje tem continuidade ou se reverte com o ratio puxado pela
soja, não pelo farelo.

**O suporte técnico do óleo (72,00) segue rompido, agora a -4,47%, mas
testado de baixo para cima hoje com volume saudável** — a reabertura de
amanhã é o teste real de continuidade da reversão.

**O próximo corte do COT (referente a 04/08/2026) só é publicado por
volta de 07/08/2026** — até lá, sem novo dado de posicionamento para
testar se o desmonte identificado no corte de 28/07 está se resolvendo
por recuperação de preço (como hoje sugere) ou segue latente.

**O USDA Crop Progress rotulado 2026-08-02 trouxe os MESMOS valores do
corte de 26/07 — provavelmente um artefato de coleta, não uma segunda
semana genuinamente estável** (ver Honestidade); o corte real da semana
que termina em 02/08 costuma ser publicado na segunda-feira à tarde
(horário dos EUA), possivelmente após o fechamento deste dump.

**NOPA — fila `release-nopa-2026-08-03` sinaliza novo "release", mas o
dado segue inacessível**, agora quase 8 semanas sem alternativa de dado
primário sobre o crush americano.

**MPOB — sem números de palma extraídos, mesma barreira de longa data.**

**O WASDE segue fora da janela deste briefing, agora 24 dias de
atraso** desde o último dado (10/07/2026).

---

## Honestidade

O que não foi possível validar neste briefing de 2026-08-03, e os pontos
onde a confiança é baixa:

**1. A manchete "USDA Exports: China, unknown buyer soybeans, Aug. 3,
2026" (Farm Progress) não veio com corpo de texto, tonelagem ou
confirmação USDA-FAS neste briefing.** Esta leitura trata a manchete como
o candidato mais plausível para explicar a reversão de soja de hoje, por
coincidência de data e pelo padrão histórico de flash sales moverem o
CBOT no mesmo pregão — mas isso é inferência, não fato confirmado. Não
foi inventado nenhum número de tonelagem ou preço de venda.

**2. O heating oil (HO=F) de 2026-08-03 fechou com apenas 26 contratos de
volume — o mais baixo já registrado nesta série, abaixo mesmo dos 1.010-
1.138 contratos do fim de semana já qualificados como anômalos.** Esta
leitura usa o número calculado de margem de biodiesel (1,0769 USD/galão,
-25,3%) porque é o que o indicador interno gerou a partir do dado
disponível, mas sinaliza explicitamente, em três seções acima, que este
número específico não deve ser tratado como confirmado até o heating oil
negociar com volume normal.

**3. O ratio Far/Soj (80,57%) segue sem fechar abaixo de 80% pela
sétima-plus sessão observada desde o checkpoint formal do D+7
(18/06/2026), agora 46 dias vencido.** Esta leitura não conclui que a
tese original falhou — apenas que ela não se confirmou dentro do prazo
tático original, e mantém o D+90 (2026-09-09) como próximo marco formal.

**4. O USDA Crop Progress rotulado 2026-08-02 trouxe valores idênticos
ao corte de 26/07/2026 (11%/52%/7%).** Como o relatório semanal
normalmente é publicado às segundas-feiras à tarde (horário dos EUA), é
mais provável que este dump tenha sido coletado antes da publicação real
da semana — esta leitura NÃO trata isso como uma segunda semana
genuinamente estável de condição de lavoura, e recomenda reconferir no
próximo dump.

**5. A isenção PIS/Cofins do biodiesel — sem confirmação de renovação ou
caducidade neste briefing.** O monitor tributário está 59 dias sem
atualização; esta leitura não presume nenhum dos dois cenários.

**6. O WASDE permanece completamente fora da janela deste briefing** —
agora 24 dias de atraso desde o último dado (10/07/2026).

**7. NOPA (`release-nopa-2026-08-03`) segue com `monthly_status` em 0,0
bool** — mesma barreira de assinatura paga, quase 8 semanas sem
alternativa de dado primário.

**8. Palma malaia (MPOB) segue sem números extraídos**, mesmo conteúdo
de 3.439 caracteres.

**9. O COT (CFTC) de 28/07/2026 segue sendo o dado de posicionamento
mais recente** — nenhum corte novo nesta janela; o próximo sai por volta
de 07/08/2026. Percentis históricos de COT não foram calculados (mesma
limitação de leituras anteriores).

**10. BCBA Argentina não trouxe carimbo de 2026-08-03 neste dump** — a
última leitura confirmada é de 2026-08-02 (acessível, sem links de
relatório detectados); esta leitura não presume continuidade da série de
sessões consecutivas sem um carimbo novo.

**11. Clima INMET (BR) não foi usado como driver de preço** — agosto é
entressafra da soja brasileira, sem relevância direta neste momento do
calendário agrícola.

**12. Os forecasts estatísticos internos (bandas 7d/30d geradas em
2026-08-03) não foram usados como driver desta leitura** — são bandas
MA20+volatilidade+slope, mecânicas, sem incorporar a leitura qualitativa
de hoje (manchete de exportação, heating oil suspeito); ficam registradas
no briefing, mas esta leitura não as toma como fonte de tese.

*Nenhum número foi inventado ou estimado além do que consta no briefing
de 2026-08-03 e nos insights anteriores referenciados. A contribuição
central desta leitura foi (1) identificar e explicar mecanicamente a
reversão ampla de preço da sessão de hoje, mais forte no óleo; (2)
separar explicitamente a leitura técnica confiável (fechamentos e
volumes de soja/farelo/óleo, todos com volume normal) da leitura
fundamental de baixa confiança (margem de biodiesel calculada sobre um
heating oil de 26 contratos); (3) tratar os três itens da fila de
julgamento de hoje — `alerta-quebra_suporte-oleo_cbot-2026-08-03`,
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` e
`release-nopa-2026-08-03` — no contexto específico da primeira sessão
completa pós-fim de semana; e (4) sinalizar a manchete de flash sale
como o principal ponto cego qualitativo desta leitura, sem inventar
tonelagem ou confirmação que o briefing não trouxe.*
