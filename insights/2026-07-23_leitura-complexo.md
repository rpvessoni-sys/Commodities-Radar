---
data: 2026-07-23
titulo: "Depois de dois pregões de rompimento, as três pernas do complexo fazem máxima intradiária nova e revertem para fechar perto da mínima do dia — farelo é o mais fraco (-0,36%, 11,9% do range) e o ratio Far/Soj recua pela primeira vez em três sessões (80,65%→80,24%), quebrando a sequência que confirmaria a reversão da tese estrutural ABIOVE, enquanto soja e óleo seguram os níveis rompidos mas sem força de continuação"
tags: [complexo, auto-claude]
fontes:
  - CBOT CME (ZSU26 soja / ZMU26 farelo / ZLU26 óleo + curva forward completa Q26-H27) — sessão de 2026-07-23
  - CME heating_oil_cbot (HO=F) — fechamento de 2026-07-23 (4,2531 USD/galão, volume de apenas 29 contratos — retorno à baixíssima liquidez após os 451 contratos de 22/07)
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, paridade BR, ISF, ISO) — 2026-07-23, com comparação contra os mesmos indicadores recalculados para 2026-07-22 dentro do próprio dump de hoje
  - BCB PTAX — 2026-07-23 (USD/BRL 5,0807, EUR/BRL 5,7788)
  - CEPEA/ESALQ Paranaguá e Paraná interior via NAG — 2026-07-23 (suporte Paranaguá R$ 147,47/saca, var +1,39%; Paraná interior R$ 139,28/saca, var +1,04%)
  - NAG Físico BR (farelo MT/IMEA, RS, Rondonópolis; prêmios export PGUA farelo/óleo) — 2026-07-23
  - CFTC COT Managed Money — ainda referência 2026-07-14, sem atualização (o corte de 21/07 tem publicação normal esperada para amanhã, ~24/07)
  - USDA Crop Progress — ainda 2026-07-19 (13% excelente + 53% boa + 6% ruim = 66% bom-ou-excelente), sem nova publicação
  - USDA WASDE — ainda 2026-07-10 (só farelo Argentina/Brasil/China parcial), sem publicação nova
  - NOPA — fila `release-nopa-2026-07-23`, `monthly_status` continua em 0,0 bool (paywall)
  - ABIOVE projeções mensais — balanços ago-dez/2026 (farelo/óleo/soja), sem alteração frente às leituras anteriores
  - NOAA CPC ENSO — 2026-07-23 (El Niño Advisory, sem mudança)
  - MPOB — 2026-07-23 (parser sem números extraídos, 3.439 caracteres, agora 14º dia consecutivo com o mesmo conteúdo, 10/07 a 23/07)
  - BCBA — 2026-07-23 (acessível, sem links de relatório detectados, mesmo padrão)
  - Notícias Agrícolas/Canal Rural/Farm Progress RSS — 2026-07-23 (160 itens lidos, 5 mantidos; manchete mantida sem número de preço, "Don't rely on stem appearance for soybean harvest timing", Farm Progress)
  - Forecasts estatísticos internos — 2026-07-23 (nona geração seguida com as seis bandas simultaneamente em viés altista)
  - system/tributario_watch.toml (lido apenas como referência, não editado) — MP-1358-2026 (`vigencia_ate` 11/07/2026, 12 dias vencida), PIS/COFINS-BIODIESEL-ISENCAO (`vigencia_ate` 31/07/2026, 8 dias restantes), MP-1363-2026, STJ-RESP-2165276, B16-CNPE-2026, EPA-RFS-2026-2027, 45Z-CLEAN-FUEL, DANANTARA-INDONESIA, INDONESIA-B50, INDONESIA-LEVY-PMK9 — todos `atualizado_em` 2026-06-05 (48 dias sem atualização do monitor)
  - Cruza com [[2026-07-22_leitura-complexo]], [[2026-07-21_leitura-complexo]], [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (checkpoint D+7, tratado abaixo — hoje 35 dias vencido)
status: ativa
vies: [neutral-soja, neutral-farelo, neutral-oleo_soja]
---

> **Nota de proveniência:** antes de qualquer análise, é preciso registrar duas
> pequenas divergências no recálculo do passado — o mesmo sintoma documentado
> em praticamente todas as leituras recentes desta série. Primeiro, a soja: a
> leitura de ontem (22/07) registrou o fechamento daquele dia em 1.225,75
> cts/bushel; o recálculo de hoje, embutido na fórmula de crush margin dos
> indicadores ("farelo 329,60 + óleo 74,53 − soja 1.226,00"), usa 1.226,00 —
> uma diferença de 0,25 ponto, pequena e dentro do padrão já visto. Segundo, o
> óleo: a leitura de ontem registrou o fechamento de 22/07 em 74,39 cts/lb; o
> recálculo de hoje usa 74,53 — uma diferença de 0,14 cts/lb, **maior que as
> divergências anteriores desta série** (que giravam em torno de 0,01-0,25 em
> soja e nunca haviam passado de casas decimais no óleo). Não há como saber, a
> partir deste briefing, se a causa é um ajuste de fonte (ex.: troca de
> ticker/contrato de referência) ou apenas arredondamento acumulado — mas o
> tamanho do desvio no óleo justifica registrar isso com mais destaque que nas
> notas anteriores (ver Honestidade, item 1). Por consistência interna, todos
> os deltas desta leitura usam os valores de 22/07 **tal como recalculados
> dentro do próprio dump de hoje** (soja 1.226,00 / óleo 74,53). Feita a
> ressalva, os fatos de hoje: as três pernas do complexo fizeram **máxima
> intradiária acima da máxima de ontem** — soja 1.236,00 (vs 1.227,75 ontem),
> farelo 333,60 (vs 332,60 ontem), óleo 75,48 (vs 74,59 ontem) — mas as três
> **fecharam no terço inferior do próprio range do dia**: soja a 32,7% do
> range, farelo a 11,9%, óleo a 15,5%. É a assinatura clássica de um rompimento
> que perde fôlego no dia seguinte: preço testa e supera a máxima anterior,
> mas os vendedores (ou realização de lucro de quem comprou no rompimento)
> dominam a segunda metade do pregão. O farelo foi o único a fechar **em
> queda absoluta** no dia (328,40, -0,36% frente a ontem); soja e óleo
> fecharam essencialmente estáveis (+0,14% e +0,03%, respectivamente). O
> ratio Far/Soj, que havia subido por duas sessões seguidas (79,28%→80,37%→
> 80,65%) — e que a leitura de ontem tratou como "a uma sessão de confirmar a
> reversão da tese bear estrutural" — **recuou hoje para 80,24%** (trata
> `alerta-quebra_resistencia-farelo_cbot-2026-07-23` e a revisão
> `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, hoje
> 35 dias vencida). Isso significa que a terceira sessão que faltava não veio
> na direção que confirmaria a reversão — veio na direção oposta.

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
bushel↔short ton, "sht"): abaixo de 80% o farelo está historicamente
"abundante" frente à soja (zona bear); acima de 87%, "apertado" (zona bull);
entre os dois, zona "neutra". É um spread de **mean-reversion** — funciona
nos dois lados.

**Hoje é o dia em que o rali de duas sessões perdeu o fôlego.** As três
pernas fizeram máxima intradiária mais alta que a de ontem — a soja tocou
1.236,00 cts/bushel (CBOT, 23/07/2026), o farelo tocou 333,60 USD/short ton,
o óleo tocou 75,48 cts/lb — o que confirma que o apetite comprador do
rompimento ainda existe. Mas as três fecharam devolvendo a maior parte do
ganho intradiário: soja fechou a apenas 32,7% do range do dia, farelo a
11,9%, óleo a 15,5%. Esse tipo de vela (máxima nova, fechamento perto da
mínima) é normalmente lido como um sinal de exaustão de curtíssimo prazo, não
necessariamente de reversão de tendência — mas é o primeiro dia, desde o
início do rompimento em 20-22/07, em que as três pernas mostram esse padrão
ao mesmo tempo. O farelo foi o mais fraco: fechou em 328,40, -0,36% frente a
ontem, a primeira queda absoluta depois de dois dias de alta. Como o ratio
Far/Soj mede farelo *relativo* à soja, e hoje o farelo caiu enquanto a soja
ficou praticamente estável, o ratio recuou de 80,65% para 80,24% (-0,41
ponto percentual) — quebrando a sequência de duas altas seguidas que a
leitura de ontem descreveu como "a primeira confirmação de dois dias na
mesma direção desta janela" e que precisava de uma terceira sessão para
virar sinal estabelecido. **A terceira sessão chegou hoje, mas na direção
oposta.** Isso não invalida a tese tática de ontem por si só (o ratio segue
acima de 80% pela terceira sessão seguida, e o preço do farelo segue acima
da resistência rompida de 325,00), mas devolve o quadro a uma ambiguidade
maior do que a leitura de ontem havia deixado — em vez de confirmar a
reversão da tese estrutural bear (ABIOVE), o dado de hoje é consistente com
um mercado que ainda não decidiu se o rompimento de farelo tem
sustentação. **O que mudou hoje:** (1) as três pernas fizeram máxima
intradiária nova mas fecharam no terço inferior do range, um padrão de
exaustão simultânea inédito nesta janela; (2) o farelo caiu de forma
absoluta pela primeira vez em três sessões, e o ratio Far/Soj recuou em vez
de confirmar a terceira alta seguida (trata
`alerta-quebra_resistencia-farelo_cbot-2026-07-23` e a revisão
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`); (3) a
soja e o farelo seguem tecnicamente acima dos níveis de resistência rompidos
(1.180,00 e 325,00, respectivamente — trata
`alerta-quebra_resistencia-soja_cbot-2026-07-23` e
`alerta-quebra_resistencia-farelo_cbot-2026-07-23`), mas sem o "seguimento"
de preço que caracterizaria um rompimento saudável; (4) a margem de
biodiesel americano se expandiu +11,1%, mas puxada por um heating oil de
liquidez baixíssima (29 contratos, revertendo a normalização de ontem); e
(5) o prêmio físico de soja em Paranaguá continuou esticando sobre a
paridade teórica (de 6,27% para 7,24%), o risco que a leitura de ontem havia
sinalizado para a tese de soja. **Leitura de uma linha:** o pivô do complexo
hoje é, de novo, o farelo — mas desta vez pela negativa: convicção baixa
(neutra) nas três pernas, porque o dado mais aguardado da semana (o rompimento
de farelo se sustentar por uma terceira sessão consecutiva na mesma direção)
não se confirmou, e o mercado inteiro mostrou sinais de exaustão tática no
mesmo dia — a recomendação geral é reduzir convicção direcional e aguardar o
COT de amanhã (~24/07) antes de tratar qualquer um dos três rompimentos como
confirmado ou encerrado.

---

## Soja

**Viés: neutro tático — o rompimento de 1.180,00 segue de pé (fechou em
1.227,75, ainda 4,05% acima do nível), mas a sessão de hoje é a primeira,
desde o início do rompimento, a mostrar um padrão de rejeição (máxima nova,
fechamento no terço inferior do range). Trata
`alerta-quebra_resistencia-soja_cbot-2026-07-23`.**

### O que sustenta a tese

**A vela de hoje inverte o padrão da vela de ontem.** Abertura 1.229,25,
fechamento 1.227,75 (-1,50, -0,12% frente à própria abertura), mínima
1.223,75, máxima 1.236,00, volume 23.896 contratos (CBOT, ticker ZSU26.CBT,
23/07/2026). O fechamento ficou em 32,7% do range do dia
((1.227,75-1.223,75)÷(1.236,00-1.223,75)) — o oposto do padrão de ontem
(90,7% do range, a vela mais decidida da semana). A máxima de hoje
(1.236,00) superou a máxima de ontem (1.227,75, valor recalculado dentro do
dump de hoje) em +8,25 pontos, ou seja, o apetite comprador testou um nível
mais alto e foi rejeitado — o preço abriu perto do meio do range de ontem,
subiu, tocou uma máxima nova, e devolveu praticamente todo o ganho
intradiário até fechar essencialmente no mesmo patamar da abertura. Frente
ao fechamento de ontem (1.226,00, ver nota de proveniência), o ganho líquido
foi de apenas +1,75 pontos (+0,14%) — uma fração do +1,26% de ontem e do
+3,87% acumulado desde o rompimento original de 1.180,00. **Isso não
invalida o rompimento** (o fechamento de hoje segue 4,05% acima de
1.180,00, ((1.227,75-1.180,00)÷1.180,00)), mas é o primeiro dado, desde
20/07, que sugere que o ritmo de valorização está desacelerando de forma
mais nítida do que a simples "pausa saudável" que a leitura de ontem já
havia atribuído à sessão de 21/07.

**A curva forward manteve a estrutura, mas com sinais de acomodação.**
Agosto/26 (Q26) 1.235,00 → Setembro/26 (U26, contrato de referência/spot)
1.227,75 (desconto de -7,25, -0,59%) → Novembro/26 (X26) 1.241,00 (recupera
+13,25 sobre setembro, +1,08%) → Janeiro/27 (F27) 1.254,00 (+13,00 sobre
novembro, +1,05%) → Março/27 (H27) 1.253,25 (-0,75, -0,06%, praticamente
estável). O desconto do spot frente ao mês anterior praticamente não mudou
(-0,59% hoje ante -0,57% ontem), e o prêmio da ponta longa também ficou
estável (+1,05% hoje vs +1,11% ontem) — a curva não reagiu à rejeição
intradiária de hoje, o que é coerente com um movimento de fechamento pontual
(realização de lucro/venda técnica) e não com uma reprecificação de
expectativa de oferta futura.

**A paridade teórica em reais subiu para R$ 137,52/saca 60kg** (indicadores,
CBOT 1.227,75 cts × PTAX 5,0807 USD/BRL de 23/07/2026), um ganho de +0,65
(+0,48%) frente aos R$ 136,87/saca implícitos de ontem — um ganho
proporcionalmente maior que o ganho em dólar (+0,14%), porque o câmbio
trabalhou na mesma direção desta vez: o real se desvalorizou (USD/BRL subiu
de 5,0638 para 5,0807, +0,33%) no mesmo dia em que a soja em dólar também
subiu, ainda que marginalmente. **O físico de Paranaguá continuou a esticar
o prêmio sobre o papel, e desta vez de forma mais acentuada.** Fechou em R$
147,47/saca (CEPEA/ESALQ via NAG, var +1,39% no dia — a maior variação
diária física desta janela recente), um prêmio de R$ 9,95/saca (+7,24%)
sobre a paridade teórica — ante um prêmio de +6,27% ontem, um alargamento de
quase 1 ponto percentual em uma única sessão. **Este é exatamente o gatilho
de risco que a leitura de ontem havia identificado** ("o prêmio físico de
Paranaguá voltar a esticar sem correspondência no papel") — hoje o papel
também subiu, mas muito menos (+0,14%) que o físico (+1,39%), reabrindo o
descolamento. Isso pode refletir um mercado exportador fisicamente mais
apertado do que o CBOT sozinho sugere (originação, logística, competição por
carga para embarque), mas também pode ser ruído de um único dia — a
disciplina desta série de leituras recomenda tratar como sinal a confirmar,
não como fato estabelecido, até que se repita.

**A soja no Paraná interior (CEPEA/ESALQ via NAG) fechou em R$ 139,28/saca**
(var +1,04% no dia), um prêmio de +R$ 1,76 (+1,28%) sobre a paridade teórica
de R$ 137,52/saca — também alargou frente ao prêmio de +0,71% de ontem, mas
com magnitude bem menor que o alargamento em Paranaguá, permanecendo dentro
da faixa normal de custo logístico interno.

**O USDA Crop Progress segue parado em 19/07/2026** (13% excelente + 53% boa
+ 6% ruim = 66% bom-ou-excelente), sem atualização nova. A próxima
publicação semanal é esperada por volta de 26/07/2026.

**O COT (CFTC) permanece com o mesmo dado de referência, 14/07/2026.**
Managed money net long em soja em +75.191 contratos (7,48% do open interest
de 1.004.746). A publicação normal do corte de 21/07 (~24/07, amanhã) é o
primeiro dado de posicionamento capaz de dizer se os fundos compraram
durante a janela inteira de volatilidade — rompimento, confirmação,
devolução parcial, novo rali, e agora a rejeição de hoje.

**Os forecasts estatísticos internos (23/07/2026)** seguem altistas: central
7d = 1.255,27 cts/bu (bandas 1.202,78-1.307,75); central 30d = 1.358,78
cts/bu (bandas 1.250,12-1.467,44) — ambos deslocados marginalmente para cima
frente a ontem, mas o modelo reage a médias móveis e momentum recente de
vários dias, não à rejeição de uma única sessão — vale lembrar que esse
viés estatístico não incorpora, por construção, o formato da vela de hoje.

### O que invalida / risco para a soja

- **Um fechamento amanhã abaixo de 1.223,75 (mínima de hoje)** seria o
  primeiro fechamento consecutivo mais baixo desde o rompimento, reforçando
  o sinal de exaustão.
- **Um fechamento abaixo de 1.180,00 (resistência/suporte original)**
  encerraria por completo a leitura tática de continuidade.
- **O COT de 21/07 (publicação amanhã, ~24/07) mostrar que os fundos
  venderam** ou ficaram de lado durante a semana inteira do rompimento —
  reduziria ainda mais a confiança de que o movimento tem lastro em fluxo
  real.
- **O prêmio físico de Paranaguá (hoje 7,24% sobre a paridade, ante 6,27%
  ontem) continuar esticando por uma segunda sessão** — confirmaria um
  descolamento genuíno entre físico e papel, não apenas ruído de um dia.

### Leitura operacional — soja

A sessão de hoje introduz a primeira dúvida tática desde o rompimento
original: o preço fez máxima nova mas não conseguiu sustentá-la, fechando
essencialmente onde abriu. Para quem está comprado alinhado ao rompimento,
não há motivo para reduzir posição hoje com base apenas nesta vela — o nível
estrutural (1.180,00) segue muito distante (+4,05%) e a mínima de hoje
(1.223,75) é a referência tática mais próxima para um stop mais apertado, se
desejado. Mas a recomendação é elevar a atenção: se amanhã repetir o padrão
de hoje (máxima nova, fechamento fraco) ou fechar abaixo de 1.223,75, a
combinação de dois dias de rejeição seria um sinal mais forte de que o
rompimento perdeu o ímpeto. Para quem está vendido contra o rompimento, a
sessão de hoje é o primeiro dado tático a favor da posição desde 20/07 — mas
ainda insuficiente, isoladamente, para justificar aumento de exposição
vendida; o COT de amanhã é o próximo dado que deve pesar mais na decisão.

---

## Farelo

**Viés: neutro — o rompimento de 325,00 segue tecnicamente de pé (fechou em
328,40, 1,05% acima do nível), mas foi o único dos três a fechar em queda
absoluta hoje (-0,36%), e o ratio Far/Soj recuou pela primeira vez em três
sessões, quebrando a sequência que confirmaria a reversão da tese estrutural
bear. Estrutural, ainda bear via ABIOVE/ISF. Trata
`alerta-quebra_resistencia-farelo_cbot-2026-07-23` e a revisão
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`.**

### O que sustenta a tese

**O farelo fez máxima nova, mas fechou abaixo do próprio ponto de abertura —
a vela mais fraca das três pernas hoje.** Fechamento 328,40 USD/short ton
(CBOT, ticker ZMU26.CBT, sessão de 23/07/2026), abertura 329,00, mínima
327,70, máxima 333,60, volume 35.574 contratos — uma queda de -0,60 (-0,18%)
frente à própria abertura e de -1,20 (-0,36%) frente ao fechamento de ontem
(329,60). O fechamento ficou em 11,9% do range do dia
((328,40-327,70)÷(333,60-327,70)) — o mais fraco entre as três commodities
hoje, e um contraste direto com os 67,0% de ontem. A máxima de hoje (333,60)
superou a máxima de ontem (332,60) em +1,00 — ou seja, o mercado testou um
nível ainda mais alto do que o rompimento de ontem e foi rejeitado com mais
força relativa do que soja e óleo. Tecnicamente, o nível de 325,00 (a
resistência rompida em 22/07) segue respeitado como suporte — a mínima de
hoje (327,70) ficou 2,70 pontos acima dele — mas a margem de segurança
encolheu frente aos 323,50 de sobra que havia ontem.

**O ratio Far/Soj recuou pela primeira vez em três sessões, e é o dado mais
importante desta leitura.** A sequência completa nesta janela: 79,28%
(20/07) → 80,37% (21/07) → 80,65% (22/07) → **80,24% (23/07)**. A leitura de
ontem definiu explicitamente o critério para tratar a reversão da tese
estrutural bear como confiável: "uma terceira sessão consecutiva acima de
80% e em alta". **A terceira sessão veio hoje — mas na direção contrária: o
ratio segue acima de 80% (terceiro dia seguido), porém caiu, não subiu.**
Isso significa que o critério tático definido pela própria disciplina desta
série de leituras **não foi satisfeito**: o padrão de "dois dias seguidos na
mesma direção" que parecia estar prestes a virar sinal estabelecido foi
interrompido antes de completar a terceira confirmação. O ratio permanece,
tecnicamente, dentro da zona "neutra" (entre 80% e 87%) e acima do piso
psicológico de 80% — mas o recuo de hoje é consistente tanto com uma pausa
de curto prazo dentro de uma tendência de alta ainda intacta, quanto com o
início de uma volta ao padrão de compressão que a tese original de 11/06
previa (ratio <80%, farelo "abundante"). Nenhuma das duas leituras pode ser
descartada com o dado de hoje isoladamente.

**Tratando `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`:**
a revisão programada da tese original (insight
[[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]), com data-alvo
18/06/2026, está hoje **35 dias vencida**. A tese original apostava em três
pilares: ratio comprimindo para <80% (o "gatilho" tático), prêmio de
exportação zerado (ainda verdadeiro — ver abaixo) e estrutura de crush
favorecendo o óleo (também ainda verdadeiro, ver seção Óleo). **O pilar
tático segue sem se resolver em qualquer direção**: depois de dois dias
sugerindo que o critério estava mais perto de invalidado, o dado de hoje
devolve incerteza — o ratio nunca chegou a fechar abaixo de 80% nesta
janela inteira (o mínimo foi 79,28% em 20/07, que ficou abaixo por apenas
uma sessão antes de reverter para cima), mas também não completou a
confirmação de alta que a colocaria definitivamente do lado oposto da tese
original. A avaliação honesta, depois de 35 dias e mais um dia de dado novo,
é que **o pilar tático desta revisão permanece tecnicamente indefinido** —
nem confirmado, nem invalidado — e os critérios fundamentalistas (WASDE,
parado desde 10/07; NOPA, ainda com `monthly_status` em 0,0 bool) continuam
sem resposta. Os checkpoints estruturais D+90 (09/09/2026) e D+180
(08/12/2026) seguem sendo o critério de mais alta confiança para julgar a
tese ABIOVE ao longo do tempo.

**A crush margin contraiu -1,31% no dia, de 3,1895 para 3,1478 USD/bushel**
(Board Crush: farelo 328,40 + óleo 74,55 − soja 1.227,75) — a primeira
contração depois de duas expansões seguidas. O mecanismo: o farelo caiu
(-0,36%) enquanto a soja (o insumo) subiu (+0,14%), o que mecanicamente
reduz a margem — o oposto do incentivo de aceleração de esmagamento
descrito ontem. Um único dia de contração não desfaz o argumento estrutural
(a margem segue historicamente elevada, acima de 3,00 USD/bu há várias
sessões), mas é coerente com a fraqueza relativa do farelo hoje.

**O oil-meal spread (óleo menos farelo, por bushel) se expandiu +3,02% para
0,9757 USD/bu**, ante 0,9471 ontem — a primeira expansão depois de duas
sessões de compressão desacelerada. O mecanismo é simétrico ao da crush
margin: o óleo ficou praticamente estável (+0,03%) enquanto o farelo caiu
(-0,36%), então o óleo ganhou terreno relativo. Isso é consistente com o
oil share também subindo ligeiramente (ver seção Óleo) — o dia de hoje
reverteu, ainda que de forma marginal, a tendência de "farelo recuperando
espaço sobre o óleo" que dominou a segunda metade da semana passada.

**A trajetória projetada da ABIOVE (sem alteração) segue sendo o pilar mais
sólido do argumento estrutural, porque não depende do preço do dia.** A
exportação de farelo brasileiro projetada cai de 1.400 mil toneladas em
agosto/2026 para 700 mil toneladas em dezembro/2026 (-50% em quatro meses),
enquanto a produção cai de forma bem mais suave (2.285,06 → 1.659,04 mil
toneladas no mesmo período, -27,4%) — menos farelo saindo pelo porto, com
produção caindo bem menos que a exportação, empurra o volume excedente para
o mercado interno de ração. Esse mecanismo estrutural não é afetado pelo
recuo tático de hoje, nem pelo rompimento tático dos últimos dias.

**As praças físicas de farelo no Brasil (NAG, 23/07/2026) seguem
completamente estáveis, agora por prazos ainda mais longos.** Mato
Grosso/IMEA em R$ 1.602,80/ton está parado há 7 dias (desde 17/07, var
1,61% naquele dia); Rio Grande do Sul em R$ 1.640,00/ton está parado desde
o início desta janela de observação (14/07 ou antes); e Rondonópolis/MT em
R$ 1.650,00/ton completa o 4º dia seguido nesse patamar (desde o salto de
+3,13% em 20/07). O prêmio de exportação em Paranaguá segue em +0,05
USD/short ton (julho/26, NAG), agora **20 dias corridos sem qualquer
variação** desde 03/07/2026 — o físico exportador segue tão parado quanto na
tese original de 11/06/2026 ("prêmio de exportação zerado"), o pilar que
mais resiste ao whipsaw do preço-papel, e o mais consistente com a tese
estrutural bear.

**O Índice de Sobra de Farelo (ISF) permanece em 80/100 (4 de 5 condições
estruturais)**, inalterado desde pelo menos 01/07/2026 — mais uma
confirmação de que o índice captura condições estruturais (ABIOVE, crush,
oferta), não a mecânica tática de preço de curto prazo, que hoje devolveu
parte do ganho relativo do farelo.

**O COT de 14/07/2026, sem atualização, mantém o mesmo contraponto relevante
à tese bear.** Managed money net long em farelo em +46.576 contratos (7,77%
do open interest de 599.353) — mais que dobrado frente a semanas anteriores.
Com o preço de hoje recuando e o ratio revertendo, a leitura do COT de
amanhã (~24/07) ganha ainda mais peso: se mostrar que os fundos continuaram
comprando farelo mesmo na semana da rejeição de hoje, o quadro de squeeze
potencial descrito ontem permanece vivo; se mostrar realização de lucro,
reforçaria a leitura de que o rompimento de 325,00 foi, ao menos em parte,
movimento técnico de curto prazo.

**O forecast estatístico do farelo (23/07/2026)** segue com viés altista:
central 7d = 334,95 USD/sht (bandas 321,46-348,44); central 30d = 360,03
USD/sht (bandas 332,11-387,95) — ambos ligeiramente acima de ontem, mas,
como no caso da soja, o modelo reage a médias de vários dias e não captura o
formato de rejeição da vela de hoje.

### O que invalida / risco para o farelo

- **Um fechamento amanhã abaixo de 325,00** desfaria de vez o sinal tático
  do rompimento, com a margem de segurança já reduzida hoje (mínima de
  327,70, apenas 2,70 pontos acima do nível).
- **O ratio fechar amanhã abaixo de 80%** devolveria o quadro tático
  integralmente a favor da tese estrutural bear original, encerrando a
  ambiguidade dos últimos quatro pregões.
- **O COT de 21/07 (publicação amanhã, ~24/07) mostrar os fundos reduzindo
  o net long em farelo** — coerente com a fraqueza de hoje, reforçaria a
  leitura de que o movimento dos últimos dias foi tático, não estrutural.
- **A crush margin continuar contraindo** — reduziria o incentivo de
  esmagamento no curto prazo, um sinal levemente bullish para o preço do
  farelo no curtíssimo prazo, mas neutro a bearish para a tese estrutural de
  excedente no médio prazo (menos esmagamento agora pode significar mais
  estoque acumulado depois).
- **NOPA seguir inacessível indefinidamente**, sem confirmação do
  esmagamento americano para os checkpoints D+90 (09/09/2026) e D+180
  (08/12/2026).

### Leitura operacional — farelo

Depois de dois dias em que a recomendação prática apontava para reduzir a
posição vendida direcional, o dado de hoje devolve a ambiguidade e recomenda
pausa, não uma nova mudança de direção. Para quem já havia reduzido ou
migrado a posição vendida estrutural (ABIOVE) para um veículo de spread
(farelo/soja ou crush completo), como recomendado ontem, não há motivo para
reverter essa decisão só com o dado de hoje — mas também não há motivo para
recompor a posição vendida outright ainda, já que o ratio segue acima de
80% e a resistência de 325,00 segue, tecnicamente, respeitada como suporte.
Para quem está comprado tático desde o rompimento de ontem, o dado de hoje é
um alerta direto: a vela de rejeição (fechamento a 11,9% do range) é o tipo
de sinal que, historicamente, precede ou uma pausa mais longa ou uma
reversão — 325,00 (suporte técnico) e a mínima de hoje (327,70) são as
referências mais próximas para apertar o stop. O COT de amanhã (~24/07) e o
fechamento de amanhã, juntos, são os dois dados que devem resolver essa
ambiguidade — a mesma conclusão da leitura de ontem, mas agora com um dado a
mais (a rejeição de hoje) empurrando ligeiramente o equilíbrio de volta para
o lado cauteloso.

---

## Óleo

**Viés: bull estrutural mantido (oil share ainda acima de 50%, ISO no teto de
100/100), mas a sessão tática de hoje também mostrou rejeição — máxima nova
(75,48) seguida de fechamento a apenas 15,5% do range. Fechou em 74,55
cts/lb, praticamente estável frente ao fechamento de ontem (74,53,
recalculado hoje, ver nota de proveniência).**

### O que sustenta a tese

**A vela de hoje reverte o padrão forte de ontem, mas de forma menos extrema
que farelo e soja em termos de queda absoluta.** Fechamento 74,55 cts/lb
(CBOT, ticker ZLU26.CBT, 23/07/2026), abertura 74,53, mínima 74,38, máxima
75,48 — um ganho de +0,02 (+0,03%) frente à própria abertura e também de
+0,02 (+0,03%) frente ao fechamento de ontem. O fechamento ficou em 15,5% do
range do dia ((74,55-74,38)÷(75,48-74,38)) — o oposto dos 89,5% de ontem, e
o segundo pior fechamento relativo das três pernas hoje (atrás apenas do
farelo). A máxima de hoje (75,48) superou a máxima de ontem (74,59) em
+0,89, um teste de nível mais alto que também foi rejeitado. **A diferença
central frente ao farelo é que o óleo, apesar da rejeição intradiária, não
chegou a fechar em queda absoluta** — ficou tecnicamente estável, o que
preserva, por pouco, a leitura de continuidade da estrutura de alta desde o
rompimento anterior.

**A curva forward aprofundou ainda mais a backwardation (desconto crescente
nos vencimentos mais distantes), mantendo o padrão já documentado em
leituras anteriores.** Agosto/26 (Q26) 75,44 → Setembro/26 (U26, spot) 74,55
(-0,89, -1,18%) → Outubro/26 (V26) 73,61 (-0,94, -1,26%) → Dezembro/26 (Z26)
72,85 (-0,76, -1,03%) → Janeiro/27 (F27) 72,36 (-0,49, -0,67%) — uma queda
total de -3,08 cts/lb (-4,08%) de agosto a janeiro/27, praticamente igual
aos -4,14% de ontem. A força segue concentrada no vencimento mais próximo —
a mesma assinatura de aperto físico de curto prazo mais do que
reprecificação estrutural de toda a curva, inalterada pela rejeição tática
de hoje.

**A margem de biodiesel americano se expandiu +11,1% no dia, para 1,0268
USD/galão** (receita 7,4181 = heating oil 4,2531 + 1,5×RIN 2,11; custo
6,3913 = óleo 5,5913 + industrial 0,80), ante 0,9240 ontem. **É importante
destrinchar o mecanismo, porque ele é o oposto do de ontem e também tem uma
bandeira de confiabilidade relevante.** O custo do óleo praticamente não se
moveu (5,5913 vs 5,5897 ontem, +0,03%) — coerente com o fechamento
essencialmente estável do CBOT hoje. Toda a expansão da margem veio do lado
da receita: o heating oil subiu +2,51% (de 4,1488 para 4,2531 USD/galão).
**Só que esse movimento do heating oil veio com volume de apenas 29
contratos hoje** — uma reversão à baixíssima liquidez documentada em duas
das três últimas leituras, depois de uma única sessão (ontem) em que o
volume havia normalizado para 451 contratos. Um salto de preço de +2,51% em
apenas 29 contratos negociados tem confiabilidade muito baixa como sinal de
mercado — é o tipo de movimento que pode ser resultado de um único negócio
de tamanho pequeno movendo o último preço, não de um reequilíbrio genuíno de
oferta e demanda de heating oil. **A expansão de margem de hoje, portanto,
deve ser tratada com ceticismo até a próxima sessão confirmar (ou não) o
nível com volume mais representativo** (ver Honestidade).

**O Índice de Suporte do Óleo (ISO) permanece em 100/100 (5 de 5 condições)**,
inalterado desde pelo menos 01/07/2026 — a tese estrutural (óleo dominando o
valor do crush) segue intacta e não foi abalada pela rejeição tática de
hoje.

**O oil share subiu ligeiramente para 53,16%** (indicadores, 23/07/2026),
ante 53,07% ontem — um ganho de +0,09 ponto percentual, a primeira alta
depois de quatro quedas seguidas documentadas nas leituras anteriores
(53,83%→53,47%→53,09%→53,02%→**53,16%**). A magnitude é pequena, mas a
mudança de direção (de queda para alta) é coerente com o óleo tendo ficado
estável enquanto o farelo caiu hoje — o óleo capturou, relativamente, mais
uma fração marginal do valor do crush.

**O COT de 14/07/2026, sem atualização, mantém o óleo como a perna mais
"concorrida" das três.** Managed money net long em +107.945 contratos
(16,92% do open interest de 638.102) — o mais alto das três pernas por larga
margem. Com a rejeição tática de hoje, esse posicionamento concentrado
segue sendo o maior fator de risco estrutural de médio prazo — um
posicionamento tão assimétrico é mais vulnerável a uma correção mais aguda
se o COT de amanhã mostrar sinais de realização de lucro generalizada em
toda a franja especulativa.

**O forecast estatístico do óleo (23/07/2026)** mantém o viés altista:
central 7d = 76,56 cts/lb (bandas 71,85-81,27); central 30d = 84,17 cts/lb
(bandas 74,41-93,92) — ligeiramente acima de ontem, mas, como nas outras
pernas, sem captar o formato de rejeição da vela de hoje.

### O que invalida / risco para o óleo

- **Um fechamento abaixo de 74,38 (mínima de hoje)** seria o primeiro
  fechamento em queda absoluta desde a retomada de ontem, abrindo espaço
  para reavaliar a leitura tática.
- **O posicionamento dos fundos (net long em 16,92% do OI, o mais concorrido
  das três pernas) sofrer uma reversão** quando o próximo COT chegar
  (~24/07, amanhã) — o risco estrutural de médio prazo mais relevante,
  agora reforçado pela rejeição tática de hoje.
- **A expansão de margem de biodiesel de hoje (+11,1%) não se confirmar
  amanhã com volume normal de heating oil** — se o próximo fechamento
  reverter o nível de 4,2531 USD/galão, ficaria claro que o dado de hoje foi
  um artefato de baixa liquidez, não um sinal genuíno de demanda.
- **MPOB seguir inacessível** — impossível avaliar o efeito do El Niño ou
  das restrições/levy indonésias sobre o prêmio de substituição via palma.
  Hoje é o 14º dia consecutivo com o mesmo conteúdo sem números extraídos.

### Leitura operacional — óleo

O fechamento de hoje é o menos conclusivo dos últimos dias: a rejeição
intradiária foi tão pronunciada quanto a do farelo e a da soja, mas o preço
não chegou a fechar em queda absoluta, preservando tecnicamente a
continuidade desde o rompimento anterior. Para quem está comprado direcional
em óleo, a recomendação é manter a posição, mas apertar a atenção ao nível
de 74,38 (mínima de hoje) como referência tática mais próxima — um
fechamento abaixo dele amanhã mudaria o quadro. Para quem opera exposição
relativa dentro do crush, a reversão do oil-meal spread para expansão
(+3,02% hoje, depois de duas sessões de compressão desacelerada) sugere que
a divergência farelo-forte/óleo-fraco documentada na semana passada pode
estar, de fato, revertendo — mas um único dia não é suficiente para tratar
isso como tendência restabelecida. O ponto mais importante da leitura de
hoje para quem acompanha o canal de demanda: a expansão de margem de
biodiesel via heating oil de baixíssima liquidez (29 contratos) é um dado
que não deveria, por si só, mudar nenhuma decisão de posição — é a mesma
lição de honestidade metodológica que a leitura de dois dias atrás já havia
precisado aplicar ao mesmo dado, na direção oposta.

---

## Spreads e crush — leitura de complexo

### Crush margin: 3,1478 USD/bu — primeira contração depois de duas expansões seguidas

A crush margin caiu -1,31% no dia (de 3,1895 para 3,1478 USD/bu), revertendo
as duas expansões seguidas dos dois dias anteriores. O mecanismo: o farelo
caiu (-0,36%) enquanto a soja (o insumo) subiu (+0,14%) — o oposto do padrão
que vinha incentivando aceleração de esmagamento. Um único dia de contração,
partindo de um nível historicamente elevado, não desfaz o argumento
estrutural de que a margem segue favorável ao processamento.

### Ratio Far/Soj: 80,24% — recuo pela primeira vez em três sessões, quebra a sequência de confirmação

O achado tático central desta leitura: depois de duas altas seguidas
(79,28%→80,37%→80,65%) que a leitura de ontem tratou como "a uma sessão de
confirmar a reversão da tese estrutural bear", o ratio de hoje recuou para
80,24% — a terceira sessão chegou, mas na direção contrária à que
confirmaria a reversão. Trata `alerta-quebra_resistencia-farelo_cbot-2026-07-23`
e a revisão `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
(agora 35 dias vencida, pilar tático permanece tecnicamente indefinido — ver
seção Farelo). O ratio segue tecnicamente acima de 80% pelo terceiro dia
seguido, mas a trajetória mudou de crescente para decrescente, devolvendo
ambiguidade ao quadro tático.

### Oil share: 53,16% — primeira alta depois de quatro quedas seguidas

Ganho de +0,09 ponto percentual frente a ontem (53,07%→53,16%), interrompendo
a sequência de quatro quedas seguidas (53,83%→53,47%→53,09%→53,02%→53,16%)
desde 17/07. A magnitude é pequena, mas a mudança de direção é coerente com
o farelo tendo caído hoje enquanto o óleo ficou estável.

### Oil-meal spread: 0,9757 USD/bu — expansão de +3,02%, reverte a desaceleração de compressão

Alta de +3,02% no dia (0,9471→0,9757 USD/bu), a primeira expansão depois de
duas sessões de compressão marginal. O óleo ganhou terreno relativo sobre o
farelo hoje — coerente com o oil share também subindo e com o farelo tendo
sido a perna mais fraca da sessão.

### Margem de biodiesel: 1,0268 USD/gal — maior alta da janela recente, mas por heating oil de liquidez baixíssima

A margem subiu +11,13% no dia, a maior alta de uma sessão nesta janela — mas
ao contrário da normalização de volume documentada ontem (451 contratos), o
heating oil de hoje negociou apenas 29 contratos, o menor volume desde a
crise de liquidez das leituras anteriores a ontem. O dado de hoje deve ser
tratado com ceticismo até a próxima sessão confirmar o nível com volume
representativo — ver seção Óleo e Honestidade.

### COT: sem atualização, publicação normal amanhã (~24/07) — o evento mais aguardado, agora ainda mais decisivo

O dado de 14/07/2026 segue sendo o mais recente. A publicação normal
(~24/07, amanhã) vai mostrar, pela primeira vez, o posicionamento dos fundos
durante toda a janela de volatilidade — os dois rompimentos (soja, farelo),
a retomada do óleo, e agora a rejeição simultânea das três pernas hoje. É o
dado mais importante em aberto, e ganhou ainda mais peso depois da
ambiguidade introduzida pela sessão de hoje.

### ISF em 80/100, ISO em 100/100 — inalterados, a divergência com o preço tático do farelo perde força

O Índice de Sobra de Farelo (4/5 condições) e o Índice de Suporte do Óleo
(5/5 condições) permanecem exatamente nos mesmos níveis de semanas
anteriores. Para o farelo, a divergência entre o índice estrutural (ainda
bear) e o preço tático, que vinha crescendo nos últimos dois dias, **perdeu
força hoje** — o preço recuou, o ratio recuou, e a distância entre "o que o
índice diz" e "o que o preço tático está fazendo" diminuiu, mesmo que o
índice em si não tenha mudado. Para o óleo, a rejeição tática de hoje também
não contradiz o índice, que segue no teto.

### O que os índices dizem juntos em 23/07/2026

ISF 80/100 + ISO 100/100 (ambos inalterados) + ratio Far/Soj recuando pela
primeira vez em três sessões, quebrando a sequência de confirmação (80,65%→
80,24%) + crush margin contraindo pela primeira vez depois de duas expansões
+ oil-meal spread e oil share revertendo para expansão/alta (favorecendo o
óleo sobre o farelo) + margem de biodiesel na maior alta da janela, mas por
um mecanismo de baixíssima confiabilidade (heating oil com 29 contratos) +
COT ainda parado, aguardando a publicação de amanhã + as três pernas
fazendo máxima intradiária nova mas fechando no terço inferior do próprio
range — formam um quadro em que a mecânica tática de curtíssimo prazo, que
ontem parecia caminhar para confirmar uma inversão da tese estrutural do
farelo, hoje devolveu ambiguidade. A lição mais importante para quem opera o
complexo: depois de uma semana de rompimentos e confirmações, hoje é o
primeiro dia em que o mercado, como um todo, mostrou sinais de indecisão
simultânea nas três pernas — o COT de amanhã e o fechamento de amanhã devem,
juntos, dizer se isso foi uma pausa de um dia dentro de uma tendência maior,
ou o início de uma reversão mais ampla.

---

## Lente fiscal e regulatória BR

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L) — a
vigência formal (`vigencia_ate` 11/07/2026) venceu há 12 dias, e o monitor
tributário segue sem qualquer atualização de status** (system/tributario_watch.toml,
evento MP-1358-2026, `atualizado_em` 2026-06-05, status ainda "tramitacao").
Enquanto o combustível fóssil segue subsidiado, a competitividade relativa do
biodiesel dentro do mix B15 mandatório fica pressionada — um vetor
regulatório independente da margem de biodiesel americana (que hoje se
expandiu +11,1%, mas por um mecanismo de baixa confiabilidade — ver
Honestidade), somando incerteza sobre a economia de processamento em duas
geografias distintas.

**Isenção PIS/Cofins biodiesel — vencimento em 31/07/2026, agora a apenas 8
dias.** Sem sinalização pública de renovação até hoje (evento
PISCOFINS-BIODIESEL-ISENCAO, `atualizado_em` 2026-06-05, sem mudança). O
vetor tributário mais próximo de um desfecho concreto nesta leitura segue
sendo este — a proximidade da data (8 dias) contrasta com os 48 dias sem
qualquer atualização do monitor, um descompasso que vale sinalizar como
risco de execução: se a decisão sair de última hora, o sistema pode não
capturá-la a tempo de refletir na leitura do dia seguinte.

**B16 — sem data, travado em B15.** Sem mudança de status (evento
B16-CNPE-2026, `atualizado_em` 2026-06-05, status "adiado"). Testes técnicos
do FNDCT com resultado esperado ~nov/2026 — realista só fim de 2026/início
de 2027.

**MP 1.363/2026 (subsídio ao diesel fóssil, R$ 1,12/L) — em vigor até
31/12/2026.** Sem alteração. Bearish estrutural persistente para a demanda
incremental de óleo de soja no mercado doméstico brasileiro.

**STJ REsp 2.165.276/2026 — crédito PIS/Cofins para esmagadoras.** Sem
alteração. Bullish para soja/óleo (alívio de custo de entrada para
biodiesel) e, por extensão, incentivo a mais esmagamento — em tensão direta
com a contração da crush margin registrada hoje, que reduz o incentivo
tático de curto prazo mesmo com o alívio tributário estrutural intacto.

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
inverificáveis pelo lado dos dados de mercado (MPOB inacessível há 14 dias
consecutivos, ver Honestidade).

**O monitor tributário como um todo está há 48 dias sem qualquer
atualização** (`atualizado_em` 2026-06-05 em todos os dez eventos
rastreados) — o intervalo segue crescendo em um momento em que dois vetores
têm datas formais já vencidas ou criticamente próximas (MP 1.358, vencida há
12 dias; isenção PIS/Cofins, a 8 dias do vencimento). Vale sinalizar este
ponto, mais uma vez, como prioridade de manutenção do sistema,
independentemente da leitura de preço.

---

## Riscos e eventos próximos

**O COT (CFTC) — publicação normal esperada ~24/07/2026 (amanhã), referente
ao corte de 21/07.** É o evento mais importante dos próximos dias, e ganhou
ainda mais peso depois da sessão de hoje: vai mostrar se os fundos compraram
ou venderam soja, farelo e óleo durante a semana inteira — rompimentos
(soja em 20-22/07, farelo em 22/07), a retomada do óleo, e agora a rejeição
simultânea das três pernas em 23/07. O primeiro dado de posicionamento capaz
de arbitrar se o rali da semana teve correspondência em fluxo real de fundos
ou se a sessão de hoje já é o início da realização de lucro por parte dessa
mesma base especulativa.

**A isenção PIS/Cofins do biodiesel vence em 31/07/2026, agora a 8 dias**,
sem sinalização de renovação — o vetor tributário mais próximo de um
desfecho concreto nesta leitura.

**O ratio Far/Soj recuou hoje e precisa de definição nas próximas sessões**
— se recuar mais e fechar abaixo de 80%, a tese estrutural bear (ABIOVE)
ganha o primeiro dado tático a seu favor desde 17/07; se retomar a alta e
romper 80,65% (a máxima recente), a reversão da revisão D+7 volta a ganhar
força.

**A resistência de 325,00 no farelo, rompida em 22/07, precisa se sustentar
como suporte com margem de segurança menor que a de ontem** — a mínima de
hoje (327,70) está apenas 2,70 pontos acima do nível; um fechamento abaixo
dele desfaria o sinal tático mais concreto dos últimos dias.

**NOPA — segue inacessível** (fila `release-nopa-2026-07-23` tratada aqui,
sem dado interpretável, apenas nova data de coleta), sem crush americano
confirmado por fonte primária.

**MPOB — sem números de palma extraídos há 14 dias consecutivos**, mantendo
cego o efeito do El Niño e dos vetores regulatórios indonésios sobre o
prêmio de substituição do óleo de soja.

**Checkpoints futuros da tese estrutural do farelo (ABIOVE)** — D+90 em
09/09/2026 e D+180 em 08/12/2026 (insight
[[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]) — a revisão D+7,
agora 35 dias vencida, permanece com o pilar tático tecnicamente indefinido
(ver seção Farelo) e segue sem confirmação de fundamentos (WASDE, NOPA); os
checkpoints estruturais seguem o critério de mais alta confiança para julgar
a tese ao longo do tempo.

---

## Honestidade

O que não foi possível validar neste briefing de 23/07/2026, onde a
confiança é baixa ou há lacunas materiais:

**1. O fechamento de óleo de 22/07/2026 usado como base de comparação para
os números de hoje diverge da leitura de ontem por uma margem maior que o
padrão anterior.** A leitura de 22/07 registrou o fechamento daquele dia em
74,39 cts/lb; o recálculo de hoje, embutido na fórmula de crush margin dos
indicadores, usa 74,53 — uma diferença de 0,14 cts/lb. As divergências
anteriores nesta série giravam em torno de 0,01-0,25 pontos na soja, mas
nunca haviam sido tão grandes no óleo em termos proporcionais. Não é
possível, a partir deste briefing, determinar a causa exata (possível ajuste
de fonte, arredondamento acumulado, ou reprocessamento do pipeline) — mas o
tamanho do desvio justifica um alerta mais forte que o dado equivalente na
soja (1.225,75 vs 1.226,00, diferença de apenas 0,25). Todos os cálculos de
variação desta leitura usam consistentemente os valores recalculados dentro
do próprio dump de hoje (soja 1.226,00 / óleo 74,53), por consistência
interna.

**2. A seção bruta `cme_cbot` do dump de hoje não traz os preços OHLC de
soja e óleo para a sessão de 22/07/2026** — apenas farelo e heating oil
aparecem com dado bruto completo daquele dia, a mesma lacuna documentada nas
leituras anteriores. A comparação de hoje contra ontem para soja e óleo
depende inteiramente do fechamento implícito na fórmula de crush margin dos
indicadores, não de uma confirmação direta da fonte primária CME para
aquele dia específico — o que também explica, em parte, a divergência do
item 1 acima.

**3. O volume do heating oil voltou a cair para 29 contratos hoje**, ante
451 ontem — a normalização observada em 22/07 não se sustentou. A alta de
+2,51% no heating oil de hoje, que respondeu por toda a expansão de +11,1%
na margem de biodiesel, tem confiabilidade baixa por causa desse volume — o
mesmo problema documentado nas leituras anteriores a ontem, agora de volta.
Este é o alerta de menor confiança mais relevante desta leitura, porque
afeta diretamente um número (margem de biodiesel) citado nas seções Óleo e
Lente fiscal.

**4. O prêmio de exportação de farelo em Paranaguá (+0,05 USD/sht) e o de
óleo (+0,08 cts/lb) estão no mesmo valor exato desde pelo menos 03/07/2026**
(NAG, agora 20 dias corridos sem variação de nenhum centavo) — não é
possível distinguir se isso reflete um mercado de exportação genuinamente
parado ou um valor que não está sendo atualizado de fato na fonte.

**5. Os níveis de resistência/suporte de 1.180,00 (soja) e 325,00 (farelo)
são alertas gerados pelo sistema de calibração interna, cuja metodologia de
definição de nível não é visível a partir deste briefing** — esta leitura
trata os níveis como dado (o sistema já os fiscaliza automaticamente), sem
poder validar de forma independente os critérios técnicos usados para
calibrá-los.

**6. O COT (CFTC) segue com dado de referência 14/07/2026.** O corte
seguinte (21/07) já ocorreu, mas a publicação (~24/07, amanhã) ainda não
está disponível — é o teste genuíno mais importante em aberto para resolver
se a rejeição desta sessão (soja, farelo e óleo fechando no terço inferior
do range após fazer máxima nova) tem correspondência em posicionamento real
de fundos ou é apenas ruído técnico de um dia.

**7. Percentis históricos de COT não calculados** — os números de
14/07/2026 são lidos apenas em nível absoluto e como fração do open interest
corrente (soja 7,48%, farelo 7,77%, óleo 16,92%), sem série histórica
completa para calibrar se algum desses níveis está objetivamente "esticado"
no sentido histórico.

**8. O WASDE segue cobrindo apenas farelo (Argentina, Brasil, China
parcial), sem nenhum dado de soja em grão ou óleo de soja, em qualquer
geografia, e sem nenhum dado dos Estados Unidos** — sem atualização desde
10/07/2026. A pergunta central da revisão D+7 vencida ("o WASDE mudou o
quadro?") segue sem canal de resposta interno.

**9. NOPA (fila `release-nopa-2026-07-23`) segue com `monthly_status` em 0,0
bool** — mesma barreira de assinatura paga documentada desde meados de
junho, agora com quase um mês e meio sem alternativa de dado primário sobre
o esmagamento americano. A "novidade" sinalizada pela fila é apenas a data
de coleta, não um dado genuinamente interpretável — o mesmo padrão das
leituras anteriores.

**10. Palma malaia (MPOB) segue sem números extraídos, agora por 14 dias
consecutivos com o mesmo conteúdo exato (3.439 caracteres, de 10/07 a
23/07/2026)** — a persistência do byte count idêntico sugere, possivelmente,
uma página que não está mais sendo servida com conteúdo atualizado. Continua
impossível avaliar o efeito do El Niño ou dos vetores regulatórios
indonésios sobre o prêmio de substituição do óleo de soja.

**11. Clima INMET (BR) não foi usado como driver de preço desta leitura.**
Julho é entressafra da soja brasileira (colheita concluída, plantio só em
outubro) — sem relevância direta para a tese de preço neste momento do
calendário agrícola. A manchete mantida no dia (Farm Progress, 23/07/2026,
sobre não confiar na aparência do caule para cronometrar a colheita) não traz
número de preço ou de área e por isso não foi tratada como driver — segue a
regra de nunca inventar ou inferir magnitude além do que consta no
briefing. O El Niño Advisory (NOAA CPC, inalterado desde pelo menos
03/07/2026) permanece relevante para a expectativa da safra de plantio de
outubro/26 e para o clima do Sudeste Asiático (palma).

**12. BCBA Argentina — sem relatórios de esmagamento/exportação acessíveis
via scraper** (page_fetched=1,0 mas sem links de relatório, 23/07/2026, sem
mudança).

**13. RIN D4 como parâmetro fixo (2,11 USD/RIN) segue sendo uma fonte
relevante de incerteza do modelo de biodiesel**, sem novo dado hoje — a
margem calculada em 1,0268 USD/gal usa esse valor fixo; combinado com a
baixa liquidez do heating oil (item 3), a margem de hoje deve ser tratada
como a leitura de menor confiança entre todos os indicadores sintéticos
citados nesta análise.

**14. O ratio Far/Soj recuar hoje, depois de duas sessões de alta, é o dado
mais importante desta leitura, e permanece tecnicamente indefinido** — esta
leitura recomenda não tratar nem a alta de dois dias, nem o recuo de hoje,
como sinal definitivo em qualquer direção, até que o preço confirme um lado
por pelo menos duas sessões consecutivas a partir de agora. Aplicar esse
padrão de forma consistente, inclusive quando o dado do dia complica em vez
de simplificar a leitura anterior, é o que preserva a credibilidade
metodológica desta série.

*Nenhum número foi inventado ou estimado além do que consta no briefing de
23/07/2026 e nos insights anteriores referenciados. A contribuição central
desta leitura foi identificar que, depois de dois pregões de rompimento nas
três pernas do complexo, a sessão de 23/07 mostrou o primeiro sinal de
exaustão simultânea — máxima intradiária nova seguida de fechamento no
terço inferior do range em soja, farelo e óleo — com o farelo sendo a perna
mais fraca (única a fechar em queda absoluta) e o ratio Far/Soj recuando
pela primeira vez em três sessões, quebrando exatamente a sequência de
confirmação que a leitura de ontem havia definido como critério para tratar
a reversão da tese estrutural bear do farelo como estabelecida. Ao mesmo
tempo, a expansão de +11,1% na margem de biodiesel americano, embora
numericamente a maior da janela recente, foi sinalizada como pouco confiável
por depender de um heating oil negociado em apenas 29 contratos.*
