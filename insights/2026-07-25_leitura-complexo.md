---
data: 2026-07-25
titulo: "Sábado sem pregão novo: o dump de hoje revisa a sessão de sexta (24/07) e muda a leitura em dois pontos materiais — a soja fecha ainda mais forte do que se pensava ontem (84,7% do range do dia, ante 77,8% relatado na leitura de 24/07) e o ratio Farelo/Soja, ao contrário do que se registrou ontem, na verdade RECUOU no dia (80,13%→80,02%), ficando a apenas 0,02 ponto percentual do piso de 80% que confirmaria a tese estrutural bear do farelo; o óleo, por sua vez, teve sua fraqueza isolada revisada para menos severa (11,6% do range, ante 2,7%); sem sessão nova hoje, a prioridade da leitura é reconciliar essas revisões e monitorar a fila até a reabertura de segunda-feira (27/07)"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT (ZSU26 soja / ZMU26 farelo / ZLU26 óleo + curva forward completa Q26-H27/F27) — sessão de 2026-07-24, conforme republicada (e revisada, ver Nota de proveniência) no dump de 2026-07-25
  - CME heating_oil_cbot (HO=F) — sessão de 2026-07-24, republicada e revisada no dump de 2026-07-25
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, paridade BR) — recorte de 2026-07-24 (revisado); Índice de Sobra de Farelo e Índice de Suporte do Óleo com print próprio de 2026-07-25
  - BCB PTAX — 2026-07-24 (USD/BRL 5,0666, EUR/BRL 5,7683); sem novo print para 2026-07-25 (fim de semana, sem pregão de câmbio)
  - CEPEA/ESALQ Paranaguá via NAG — 2026-07-24 (suporte R$ 148,37/saca, var +0,61%) — primeiro print de mesmo dia desta janela, resolve a defasagem citada na leitura de 24/07
  - CEPEA/ESALQ Paraná interior via NAG — 2026-07-24 (R$ 140,26/saca, var +0,70%) — idem, primeiro print de mesmo dia
  - NAG Físico BR (farelo MT/IMEA R$ 1.669,72/ton; Rondonópolis R$ 1.650,00/ton; RS R$ 1.640,00/ton; prêmios export PGUA farelo +0,05 USD/sht e óleo +0,08 cts/lb) — 2026-07-24, sem novo print para 2026-07-25 (fim de semana)
  - CFTC COT Managed Money — corte de 2026-07-21 (inalterado desde a leitura de 24/07; próximo corte 28/07, publicação normal ~31/07)
  - USDA Crop Progress — ainda 2026-07-19 (13% excelente + 53% boa + 6% ruim = 66% bom-ou-excelente); próxima publicação semanal esperada por volta de 26/07/2026
  - USDA WASDE — ainda 2026-07-10, sem publicação nova
  - NOPA — fila `release-nopa-2026-07-25`, `monthly_status` continua em 0,0 bool (paywall), sem dado interpretável novo
  - ABIOVE projeções mensais — balanços ago-dez/2026 (farelo/óleo/soja), sem alteração
  - NOAA CPC ENSO — 2026-07-25 (El Niño Advisory, inalterado desde pelo menos 03/07/2026)
  - MPOB — 2026-07-25 (parser sem números extraídos, 3.439 caracteres, 16º dia consecutivo com o mesmo conteúdo, 10/07 a 25/07)
  - BCBA — 2026-07-22 (última leitura do scraper, sem relatórios detectados, mesmo padrão há vários dias)
  - Notícias Agrícolas/Canal Rural/Farm Progress RSS — 2026-07-25 (160 itens lidos, 6 mantidos; manchete "Cepea: Soja, milho e boi gordo encerram semana com novas altas", Canal Rural, sem número de preço na manchete)
  - Forecasts estatísticos internos — 2026-07-25 (nova geração, spot ref já reflete os valores revisados de 24/07: soja 1.240,25 / farelo 330,80 / óleo 73,47)
  - system/tributario_watch.toml (lido apenas como referência, não editado) — 10 eventos, todos `atualizado_em` 2026-06-05 (50 dias sem atualização do monitor); trata `trib-PISCOFINS-BIODIESEL-ISENCAO-2026-07-31`
  - Cruza com [[2026-07-24_leitura-complexo]], [[2026-07-23_leitura-complexo]], [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (checkpoint D+7, tratado abaixo — hoje 37 dias vencido)
status: ativa
vies: [bull-soja, neutral-farelo, bear-oleo_soja]
---

> **Nota de proveniência (leitura desta série sobre um padrão recorrente, hoje
> confirmado pela segunda vez consecutiva):** a leitura de 24/07/2026 já havia
> documentado que a sessão de 23/07 chegou revisada no dump seguinte (soja
> 1.227,75→1.231,00; heating oil 4,2531→4,3416 com volume saltando de 29 para
> 25.967 contratos). **O dump de hoje repete exatamente esse padrão para a
> sessão de 24/07/2026**, que a leitura de ontem já havia analisado com os
> números do próprio dump de 24/07. Comparando o que a leitura de 24/07
> registrou contra o que o dump de hoje (25/07) traz para a mesma sessão de
> 24/07:
>
> | Métrica (24/07/2026) | Registrado na leitura de 24/07 | Revisado no dump de 25/07 | Delta |
> |---|---|---|---|
> | Soja, fechamento | 1.239,00 cts/bu | **1.240,25 cts/bu** | +1,25 (+0,10%) |
> | Farelo, fechamento | 331,10 USD/sht | **330,80 USD/sht** | -0,30 (-0,09%) |
> | Óleo, fechamento | 73,34 cts/lb | **73,47 cts/lb** | +0,13 (+0,18%) |
> | Heating oil, fechamento | 4,1311 USD/gal | **4,1806 USD/gal** | +0,0495 (+1,20%) |
> | Heating oil, volume | 41.488 contratos | **22.882 contratos** | -44,8% |
> | Farelo, volume | 35.887 contratos | **37.681 contratos** | +5,0% |
> | Ratio Far/Soj | 80,17% | **80,02%** | -0,15pp |
> | Crush margin | 2,9616 USD/bu | **2,9568 USD/bu** | -0,16% |
> | Oil share | 52,55% | **52,62%** | +0,07pp |
> | Oil-meal spread | 0,7832 USD/bu | **0,8041 USD/bu** | +2,67% |
> | Margem biodiesel US | 0,9956 USD/gal | **1,0354 USD/gal** | +4,0% |
>
> As magnitudes de hoje são pequenas em preço absoluto (todas abaixo de 1,2%),
> muito menores que a revisão anômala de heating oil de 23/07 (quase 900x em
> volume) — mas o volume de heating oil voltou a ser revisado para baixo de
> forma expressiva (-44,8%), o que reforça a recomendação já registrada
> ontem: **tratar qualquer leitura de volume de heating oil como provisória
> até a confirmação do dia seguinte.** Mais importante para a tese ativa: a
> revisão do **ratio Far/Soj** inverteu o sinal do movimento diário — a
> leitura de 24/07 registrou uma alta (+0,04pp) que sustentava a leitura
> "praticamente parado, mas ainda subindo"; o dado revisado de hoje mostra,
> na verdade, uma **queda** (-0,15pp), que deixa o ratio a apenas 0,02 ponto
> percentual do piso de 80% (ver seção Farelo e Spreads e crush). Por
> consistência interna, todos os números desta leitura para 24/07/2026 usam
> os valores **tal como revisados no dump de hoje** (soja 1.240,25 / farelo
> 330,80 / óleo 73,47 / HO 4,1806 / ratio 80,02%), não os valores publicados
> na leitura de ontem — o que explica por que alguns números aqui diferem
> ligeiramente dos citados em [[2026-07-24_leitura-complexo]].

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
dois, zona "neutra". É um spread de **mean-reversion** — funciona nos dois
lados, e é justamente essa fronteira de 80% que hoje está no centro da
leitura, como se explica abaixo.

**Hoje é sábado — não há pregão novo na CBOT** (a última sessão disponível
segue sendo a de sexta-feira, 24/07/2026; a próxima reabertura é
segunda-feira, 27/07/2026). O trabalho desta leitura de fim de semana é
outro: **o dump de hoje trouxe a sessão de sexta-feira revisada**, e essa
revisão muda a leitura em dois pontos que importam para quem opera o
complexo. **Primeiro, a boa notícia:** a soja, que a leitura de ontem já
descrevia como um fechamento forte (77,8% do range do próprio dia), está
revisada para um fechamento **ainda mais forte** — 1.240,25 cts/bushel, que
equivale a 84,7% do range de sexta ((1.240,25-1.225,00)÷(1.243,00-1.225,00)).
O óleo, que ontem foi descrito como a perna mais fraca do dia (fechamento a
apenas 2,7% da mínima), também foi revisado — para 73,47 cts/lb, ou 11,6% do
range do dia — ainda o pior fechamento relativo das três pernas, mas bem
menos extremo do que se pensava ontem. **Segundo, a notícia que exige
atenção redobrada:** o ratio Far/Soj, que a leitura de ontem descreveu como
"praticamente parado, com um pequeno ganho" (80,13%→80,17%), na verdade
**recuou** no dado revisado de hoje (80,13%→**80,02%**) — a segunda-feira
abre, portanto, com o ratio a apenas **0,02 ponto percentual** do piso de
80% que confirmaria a tese estrutural bear do farelo (ABIOVE/ISF), a
distância mais estreita de toda a janela observada. **O que muda hoje:** (1)
a soja ganha ainda mais margem de segurança sobre a resistência rompida de
1.180,00 (agora +5,10% de distância, usando o fechamento revisado); (2) o
ratio Far/Soj está, na prática, "encostado" no piso técnico que definiria a
tese bear, um detalhe que a leitura de ontem não captou por trabalhar com o
dado ainda não revisado; (3) os prêmios físicos de Paranaguá e Paraná
interior finalmente publicaram print de mesmo dia (24/07), resolvendo a
defasagem que as duas últimas leituras haviam sinalizado como lacuna; (4) a
notícia do dia (Canal Rural, 25/07) confirma que "soja, milho e boi gordo
encerram semana com novas altas" — uma leitura qualitativa consistente com
o fechamento forte da soja, sem número novo de preço; e (5) o COT (CFTC)
segue parado no corte de 21/07/2026 — nenhuma atualização de posicionamento
de fundos chega antes de 31/07. **Leitura de uma linha:** o pivô do
complexo segue sendo a soja, agora com ainda mais margem técnica a favor
depois da revisão; a maior fonte de tensão nova é o ratio Far/Soj
"encostado" no piso de 80%, que será o primeiro dado a observar na abertura
de segunda-feira; confiança moderada-alta para soja, baixa para farelo
(tensão entre COT bullish e ratio agora no limiar técnico), baixa-moderada
para óleo (fraqueza tática confirmada, porém mais branda do que se pensava).

---

## Soja

**Viés: bull tático — o fechamento de sexta-feira (24/07/2026), revisado
hoje para 1.240,25 cts/bushel, equivale a 84,7% do range do próprio dia
(ante os 77,8% registrados na leitura de ontem com o dado ainda não
revisado), reforçando o padrão de força que já havia revertido a rejeição
de quinta-feira. A distância sobre a resistência rompida de 1.180,00 se
amplia para +5,10%. O COT de 21/07 (ainda o mais recente, inalterado desde
ontem) confirma compra líquida de fundos de +73,6% na semana do rompimento.
Trata `alerta-quebra_resistencia-soja_cbot-2026-07-24`.**

### O que sustenta a tese

**A revisão de hoje reforça, não enfraquece, a leitura de força de
sexta-feira.** Abertura 1.229,50, fechamento revisado 1.240,25 (+10,75 frente
à abertura, +0,87%), mínima 1.225,00, máxima 1.243,00, volume 26.510
contratos (CBOT, ticker ZSU26.CBT, sessão de 24/07/2026, dado conforme
publicado no dump de 25/07/2026). O fechamento revisado ficou em **84,7% do
range do dia** ((1.240,25-1.225,00)÷(1.243,00-1.225,00)) — acima dos 77,8%
que a leitura de ontem havia calculado com o fechamento ainda não revisado
(1.239,00). Frente ao fechamento de quinta-feira (1.231,00, ver nota de
proveniência da leitura anterior), o ganho do dia foi de +9,25 pontos
(+0,75%). A resistência original de 1.180,00, rompida em meados de julho,
agora está **5,10% abaixo** do fechamento revisado de sexta
((1.240,25-1.180,00)÷1.180,00) — a maior distância de toda a janela de
acompanhamento desta série, um pouco maior do que os +5,0% calculados ontem
com o dado ainda não revisado.

**O COT (CFTC, corte de 21/07/2026) segue sendo o dado de maior peso desta
leitura para a soja, e não teve atualização nova hoje.** Managed money (a
categoria de fundos especulativos que mais se aproxima de posicionamento
direcional puro dentro do relatório) elevou a posição comprada de 145.930
para 180.163 contratos (+23,5%) e reduziu a posição vendida de 70.739 para
49.658 (-29,8%) na semana de 21/07 — o net long saltou de 75.191 para
130.505 contratos (+73,6%), e como fração do open interest (1.045.077
contratos) subiu de 7,48% para 12,49%. Esse dado já foi tratado em
profundidade na leitura de 24/07 e permanece, sem alteração, o principal
lastro fundamental por trás do rompimento — o próximo corte (28/07,
publicação normal ~31/07) é o primeiro capaz de dizer se essa compra se
sustentou durante a própria sessão de sexta-feira (24/07) e o fim de
semana.

**A curva forward manteve a estrutura de prêmio crescente nos vencimentos
mais distantes, agora com os valores revisados do spot.** Setembro/26 (U26,
spot) 1.240,25 → Novembro/26 (X26) 1.253,50 (+13,25 sobre o spot, +1,07%) →
Janeiro/27 (F27) 1.266,50 (+13,00 sobre novembro, +1,04%) → Março/27 (H27)
1.264,00 (-2,50, -0,20%, praticamente estável) — o mesmo padrão de contango
moderado e crescente documentado nas leituras recentes, sem sinal de
estresse ou inversão. Agosto/26 (Q26) fechou em 1.248,00, um prêmio de
+0,62% sobre o spot de setembro.

**A paridade teórica em reais, recalculada com o fechamento revisado, fica
em R$ 138,53/saca de 60kg** (indicadores, CBOT 1.240,25 cts × PTAX 5,0666
USD/BRL de 24/07/2026 — sem novo PTAX para 25/07, fim de semana sem pregão
de câmbio). **A novidade mais relevante da leitura de hoje para a soja é que
o físico de Paranaguá finalmente trouxe um print de mesmo dia (24/07):
R$ 148,37/saca (CEPEA/ESALQ via NAG, var +0,61%)**, resolvendo a defasagem
que as duas últimas leituras haviam sinalizado como lacuna de dados.
Comparando físico e paridade do mesmo dia pela primeira vez nesta janela, o
prêmio de exportação em Paranaguá fica em **+7,10%**
((148,37-138,53)÷138,53) — mais alto do que a aproximação de +6,56% que a
leitura de ontem havia calculado (comparando papel de hoje contra físico de
ontem), agora com a confiança adicional de ser uma comparação de mesmo dia.
O físico de Paraná interior também trouxe print de 24/07: R$ 140,26/saca
(var +0,70%), um prêmio de +1,25% sobre a paridade do mesmo dia — igualmente
mais confiável do que a comparação defasada de ontem. **O movimento de
Paranaguá é o quinto dia consecutivo de alta física** (07-20: 142,65 →
07-21: 144,17 → 07-22: 145,45 → 07-23: 147,47 → 07-24: **148,37**), uma
sequência ininterrupta que confirma, no mercado físico exportador, a mesma
força que o papel vem mostrando — um dado que reforça a convicção da tese
bull mais do que qualquer print isolado teria feito.

**O USDA Crop Progress segue parado em 19/07/2026** (13% excelente + 53% boa
+ 6% ruim = 66% bom-ou-excelente), sem atualização nova. A próxima
publicação semanal é esperada por volta de **26/07/2026 — ou seja, amanhã**,
o primeiro dado agrícola potencialmente novo da semana que se inicia.

**Os forecasts estatísticos internos (25/07/2026)**, recalculados a partir do
spot revisado de sexta, seguem altistas e deslocaram levemente para cima:
central 7d = 1.269,06 cts/bu (bandas 1.216,40-1.321,71); central 30d =
1.378,61 cts/bu (bandas 1.269,60-1.487,61) — ambos marginalmente acima da
geração de ontem, refletindo o spot revisado, sem mudança de viés.

### O que invalida / risco para a soja

- **Um fechamento de segunda-feira (27/07) abaixo de 1.225,00** (mínima de
  sexta) devolveria parte da força mostrada na última sessão e reabriria a
  dúvida tática.
- **Um fechamento abaixo de 1.180,00** (agora 5,10% de distância, a maior
  margem de segurança desta janela) encerraria por completo a leitura
  tática de continuidade — mas exigiria uma reversão muito mais expressiva
  do que qualquer coisa vista até agora.
- **O próximo corte do COT (28/07, publicação ~31/07) mostrar realização de
  lucro** depois do salto de +73,6% da semana de 21/07 — um recuo do net
  long, mesmo que o preço continue subindo, seria o primeiro sinal de que a
  compra de fundos já capturou a maior parte do movimento.
- **O prêmio físico de Paranaguá, agora confirmado em +7,10% sobre a
  paridade (mesmo dia, 24/07), continuar esticando** — reforçaria a leitura
  de mercado exportador fisicamente apertado; uma reversão brusca desse
  prêmio, por outro lado, seria o primeiro sinal de enfraquecimento da
  demanda de exportação.

### Leitura operacional — soja

A revisão de hoje não muda a leitura operacional da sessão de 24/07 — só a
reforça. Para quem está comprado alinhado ao rompimento, a distância maior
até o nível estrutural (1.180,00, agora a 5,10%) e a confirmação física
(quinto dia seguido de alta em Paranaguá) dão espaço para operar com o stop
tático na mínima de sexta (1.225,00) em vez de um stop mais apertado — não
há motivo para reduzir posição. Como não há pregão hoje, a única ação
prática é monitorar a abertura de segunda-feira contra os dois níveis
citados (1.225,00 tático e 1.180,00 estrutural) e acompanhar a publicação do
Crop Progress amanhã (26/07), o primeiro dado potencialmente novo da
semana. Para quem está vendido contra o rompimento, nada mudou desde ontem:
operar vendido soja neste momento significa apostar contra um movimento com
compra de fundos comprovada (COT) e agora também confirmação física
(Paranaguá) — o risco de uma posição vendida puramente tática segue elevado.

---

## Farelo

**Viés: neutro, mas com tensão tática crescente — o dado revisado de hoje
muda o sinal do movimento diário do ratio Far/Soj de alta (+0,04pp, leitura
de ontem) para queda (-0,15pp), deixando o ratio em 80,02%, a apenas 0,02
ponto percentual do piso de 80% que confirmaria a tese estrutural bear
(ABIOVE/ISF). O COT (21/07, inalterado) segue fortemente bullish (net long
+57,8% na semana). Trata `alerta-quebra_resistencia-farelo_cbot-2026-07-24`
e a revisão `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`.**

### O que sustenta a tese

**A vela de sexta-feira, com o fechamento revisado, fica ligeiramente mais
fraca do que a leitura de ontem havia descrito.** Fechamento revisado 330,80
USD/short ton (CBOT, ticker ZMU26.CBT, sessão de 24/07/2026), abertura
329,40, mínima 327,90, máxima 334,30, volume 37.681 contratos — um ganho de
+1,40 (+0,42%) frente à própria abertura, menor que o +0,52% calculado ontem
com o fechamento ainda não revisado (331,10). O fechamento revisado ficou em
**45,3% do range do dia** ((330,80-327,90)÷(334,30-327,90)) — abaixo dos
50,0% (exatamente o meio do range) que a leitura de ontem havia calculado,
um sinal ligeiramente mais fraco, embora ainda longe de configurar rejeição
clara. A resistência de 325,00, rompida em 22/07, segue respeitada como
suporte, com a mínima de sexta (327,90) 2,90 pontos acima dela — margem de
segurança estável frente aos dias anteriores.

**O ratio Far/Soj é o ponto mais importante desta leitura de fim de semana,
e o dado revisado inverte o sinal do dia.** A leitura de 24/07 registrou o
ratio subindo de 80,13% para 80,17% (+0,04pp) — um sinal, ainda que fraco,
de que o farelo ganhava terreno relativo sobre a soja. **O dado revisado no
dump de hoje mostra o oposto: o ratio caiu de 80,13% para 80,02% (-0,15pp)**
— a maior queda diária desde 20/07 (quando o ratio havia caído para 79,28%,
a mínima da janela) e o valor mais próximo do piso de 80% de toda a
sequência desde então (07-21: 80,37%; 07-22: 80,65%, máxima da janela;
07-23: 80,13%; 07-24 revisado: **80,02%**). O mecanismo por trás dessa queda
é o mesmo Board Crush de sempre: farelo (+0,42%) subiu proporcionalmente
menos do que a soja (+0,75%) na sessão, então o denominador (soja) cresceu
mais rápido que o numerador (farelo), comprimindo o ratio. **Isso é uma
informação tática de primeira ordem para segunda-feira**: o ratio está, na
prática, "encostado" no piso técnico que confirmaria a tese estrutural bear
original (ratio <80%) — um fechamento de segunda-feira abaixo de 80,00%
resolveria, ao menos taticamente, a ambiguidade que persiste desde 20/07, a
favor da tese estrutural (ABIOVE, ISF em 80/100).

**A revisão `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`,
com data-alvo original 18/06/2026, está hoje 37 dias vencida.** A tese
original apostava em ratio comprimindo para <80% (gatilho tático), prêmio de
exportação zerado (ainda verdadeiro — ver abaixo) e estrutura de crush
favorecendo o óleo (também ainda verdadeiro, embora tenha perdido força na
sessão de sexta — ver seção Óleo). **Com o ratio revisado de hoje a 0,02pp
do piso de 80%, esta é a primeira leitura desta série em que a tese tática
original está genuinamente "à beira" de se confirmar** — não confirmada
ainda (o fechamento de sexta ficou acima de 80%, ainda que por pouco), mas
mais próxima do que em qualquer sessão anterior da janela observada.

**O COT (CFTC, corte de 21/07/2026) segue fortemente bullish para o farelo,
sem atualização nova hoje, e a tensão com a tese estrutural bear
(ABIOVE/ISF) permanece — agora mais aguda dado o ratio no limiar.** Managed
money elevou a posição comprada de 119.347 para 130.152 contratos (+9,1%) e
reduziu a posição vendida de 72.771 para 56.676 (-22,1%) na semana de 21/07
— o net long saltou de 46.576 para 73.476 contratos (+57,8%), e como fração
do open interest (618.289 contratos) subiu de 7,77% para 11,89%. **A
configuração de hoje é exatamente a que a leitura de ontem descreveu como
"clássica de mercado dividido": fundos cada vez mais comprados contra um
ratio que está, agora, tecnicamente na fronteira do piso estrutural bear.**
Se o ratio romper 80% na abertura de segunda-feira, o teste mais direto será
justamente esse: os fundos que compraram pesado na semana de 21/07 mantêm
posição contra o sinal técnico bear, ou começam a vender.

**A crush margin, com os valores revisados, caiu -5,82% na sessão de sexta**
(de 3,1395 para 2,9568 USD/bushel — Board Crush: farelo 330,80 + óleo 73,47
− soja 1.240,25), muito próxima da queda de -5,67% que a leitura de ontem
havia calculado com o dado ainda não revisado, e segue sendo o menor valor
de toda a janela recente (07-20: 3,0316; 07-21: 3,1047; 07-22: 3,1895;
07-23: 3,1395; 07-24 revisado: **2,9568**). O mecanismo segue o mesmo: a
soja (o custo) subiu mais rápido do que a soma de farelo e óleo (a
receita).

**O oil-meal spread, com os valores revisados, comprimiu -18,1% para 0,8041
USD/bushel** (ante 0,9823 na quinta) — uma compressão um pouco menor do que
os -20,3% calculados ontem com o dado ainda não revisado, mas ainda a maior
compressão diária desta janela. O farelo segue ganhando terreno relativo
sobre o óleo dentro do valor do crush, mesmo com a magnitude revisada para
baixo.

**A trajetória projetada da ABIOVE (sem alteração) segue sendo o pilar mais
sólido do argumento estrutural, porque não depende do preço do dia.** A
exportação de farelo brasileiro projetada cai de 1.400 mil toneladas em
agosto/2026 para 700 mil toneladas em dezembro/2026 (-50% em quatro meses),
enquanto a produção cai de forma bem mais suave (2.285,06 → 1.659,04 mil
toneladas no mesmo período, -27,4%) — menos farelo saindo pelo porto, com
produção caindo bem menos que a exportação, empurra o volume excedente para
o mercado interno de ração.

**As praças físicas de farelo no Brasil (NAG) não têm print novo para
25/07/2026 — fim de semana, sem publicação.** O último dado segue sendo o
salto de Mato Grosso/IMEA em 24/07: +4,18% para R$ 1.669,72/ton, encerrando
sete dias parado em R$ 1.602,80. **Esse salto segue sem confirmação ou
reversão**, porque não há pregão físico hoje — o primeiro dado capaz de
confirmar (ou desmentir) se foi ruído de um dia ou início de uma mudança de
demanda doméstica só deve aparecer no dump de segunda-feira. Rondonópolis/MT
segue em R$ 1.650,00/ton (estável desde 20/07) e Rio Grande do Sul em
R$ 1.640,00/ton (estável desde pelo menos 14/07). O prêmio de exportação em
Paranaguá permanece em +0,05 USD/short ton (julho/26, NAG), agora **22 dias
corridos sem qualquer variação** desde 03/07/2026 — o canal de exportação
segue tão parado quanto na tese original de 11/06/2026, mesmo com o salto do
IMEA no mercado doméstico.

**O Índice de Sobra de Farelo (ISF) permanece em 80/100 (4 de 5 condições
estruturais), com print explícito de 25/07/2026** (indicadores) — o índice
segue sendo recalculado mesmo em dia sem pregão (é uma leitura de condições
estruturais, não de preço intradiário), e não mudou desde pelo menos
01/07/2026.

### O que invalida / risco para o farelo

- **Um fechamento de segunda-feira (27/07) abaixo de 325,00** desfaria o
  sinal tático do rompimento, mesmo com o COT bullish.
- **O ratio Far/Soj fechar segunda-feira abaixo de 80,00%** — dado que o
  valor revisado de hoje (80,02%) está a apenas 0,02pp desse piso, este é,
  agora, o gatilho técnico mais próximo de toda a janela observada para
  devolver o quadro tático integralmente à tese estrutural bear original.
- **O próximo corte do COT (28/07, publicação ~31/07) mostrar reversão do
  net long** — se os fundos que compraram nesta semana começarem a vender,
  a configuração de tensão entre COT e ABIOVE se resolveria a favor da tese
  estrutural bear.
- **O salto do físico em MT/IMEA (+4,18% em 24/07) não se confirmar na
  próxima publicação** — sem dado de fim de semana, esta é a primeira
  pendência a resolver na reabertura.
- **NOPA seguir inacessível**, sem confirmação do esmagamento americano para
  os checkpoints D+90 (09/09/2026) e D+180 (08/12/2026).

### Leitura operacional — farelo

O dado que muda a leitura operacional de hoje é o ratio Far/Soj revisado, não
o COT (que segue igual desde ontem). Para quem mantém posição vendida
estrutural, a recomendação segue a mesma das últimas sessões — manter a
tese via spread (farelo/soja ou crush completo) em vez de posição vendida
outright, dado o risco de "short squeeze" alimentado pelo COT bullish — mas
com o ratio agora a 0,02pp do piso de 80%, segunda-feira é a sessão mais
importante desta janela para essa tese: um fechamento abaixo de 80% seria o
primeiro sinal técnico claro a favor da posição estrutural desde
11/06/2026. Para quem está comprado tático desde o rompimento de 325,00, o
fechamento revisado no meio-baixo do range (45,3%) não é um sinal forte o
suficiente para aumentar posição, e a proximidade do ratio ao piso de 80% é
um motivo concreto para apertar o stop, não para relaxá-lo — a referência
tática mais próxima segue sendo a mínima de sexta (327,90) ou o nível
estrutural (325,00). A operação relativa de comprar farelo contra óleo
dentro do crush, sugerida na leitura de ontem pela compressão do oil-meal
spread, segue válida (compressão de -18,1% confirmada, mesmo com a
magnitude revisada para baixo), mas o mesmo dado que sustenta essa operação
(farelo perdendo menos do que a soja subiu) é o que também empurrou o ratio
Far/Soj para perto do piso — as duas leituras não são contraditórias, mas
merecem ser acompanhadas juntas na reabertura.

---

## Óleo

**Viés: bear tático, porém mais brando do que a leitura de ontem
registrou — o fechamento revisado de sexta-feira (73,47 cts/lb) equivale a
11,6% do range do dia, ante os 2,7% calculados ontem com o dado ainda não
revisado. Ainda a perna mais fraca do complexo na sessão de sexta, mas a
revisão retira parte da urgência tática que a leitura anterior atribuiu ao
movimento. Estrutural, segue bull via ISO 100/100 (print de 25/07) e COT
mais concorrido das três pernas (18,17% do OI, corte de 21/07, inalterado).**

### O que sustenta a tese

**A revisão de hoje suaviza, mas não reverte, a leitura de fraqueza isolada
de sexta-feira.** Fechamento revisado 73,47 cts/lb (CBOT, ticker ZLU26.CBT,
sessão de 24/07/2026), abertura 74,53, mínima 73,30, máxima 74,77 — uma
queda de -1,06 (-1,42%) frente à própria abertura e de -1,22 (-1,63%) frente
ao fechamento de quinta-feira (74,69). O fechamento revisado ficou em
**11,6% do range do dia** ((73,47-73,30)÷(74,77-73,30)) — ainda o pior
fechamento relativo das três commodities na sessão de sexta (soja 84,7%,
farelo 45,3%), mas significativamente menos extremo do que os 2,7%
calculados na leitura de ontem com o fechamento ainda não revisado (73,34).
Na prática, o óleo seguiu sendo a perna mais fraca do dia, mas não fechou
"colado" na mínima como a leitura anterior havia descrito — uma distinção
tática relevante: um fechamento a 2,7% do range sugere rejeição forte e
potencial continuidade de fraqueza; um fechamento a 11,6% ainda é fraco, mas
deixa mais espaço de dúvida sobre se o padrão é de rejeição ou apenas de um
dia lateral-a-fraco dentro de uma tendência mais ampla ainda positiva.

**A curva forward, com os valores de sexta, manteve a backwardation
(desconto crescente nos vencimentos mais distantes) documentada em leituras
anteriores.** Agosto/26 (Q26) 74,33 → Setembro/26 (U26, spot) 73,47 (-0,86,
-1,16%) → Outubro/26 (V26) 72,67 (-0,80, -1,09%) → Dezembro/26 (Z26) 72,01
(-0,66, -0,91%) → Janeiro/27 (F27) 71,56 (-0,45, -0,63%) — uma queda total de
-2,77 cts/lb (-3,73%) de agosto a janeiro/27, no mesmo padrão de aperto
físico de curto prazo mais do que reprecificação estrutural de toda a curva
já documentado nas leituras anteriores.

**A margem de biodiesel americano, com os valores revisados, caiu -6,28% na
sessão de sexta, para 1,0354 USD/galão** (receita 7,3456 = heating oil
4,1806 + 1,5×RIN 2,11; custo 6,3103 = óleo 5,5103 + industrial 0,80), ante
1,1048 na quinta-feira — uma queda bem menor do que os -9,88% que a leitura
de ontem havia calculado com o heating oil ainda não revisado (4,1311). O
mecanismo segue o mesmo descrito ontem: o custo do óleo caiu junto com o
CBOT (-1,42% em dólar), mas a receita caiu mais, puxada pelo heating oil —
só que, com o dado revisado, essa queda de receita é menor (heating oil
revisado para 4,1806, e não 4,1311). **O volume de heating oil também foi
revisado para baixo nesta sessão (41.488→22.882 contratos, -44,8%)** — uma
revisão expressiva, ainda que muito menor que a de 23/07 (quase 900x). Dado
o padrão que já se repete pela segunda vez consecutiva nesta série, a
recomendação desta leitura é tratar qualquer leitura de volume de heating
oil, mesmo quando aparentemente robusta, como sujeita a revisão relevante no
dia seguinte.

**O Índice de Suporte do Óleo (ISO) permanece em 100/100 (5 de 5 condições),
com print explícito de 25/07/2026** (indicadores) — a tese estrutural
(óleo dominando o valor do crush) segue formalmente intacta e o índice
continua sendo recalculado mesmo em dia sem pregão.

**O oil share, com o valor revisado, ficou em 52,62%** (ante 53,18% na
quinta) — uma queda de -0,56 ponto percentual, menor que os -0,63pp
calculados ontem, mas ainda o primeiro valor fora da faixa de 53,0-53,5% em
que o indicador vinha oscilando nos cinco pregões anteriores
(53,47%→53,09%→53,07%→53,18%→**52,62%**). A leitura direcional de ontem
(primeira queda tática fora da faixa recente) permanece válida, apenas com
a magnitude revisada para baixo.

**O COT (CFTC, corte de 21/07/2026) segue confirmando que o óleo é, de
longe, a perna mais concorrida das três — sem atualização nova hoje.**
Managed money elevou a posição comprada de 133.321 para 143.159 contratos
(+7,4%) e reduziu a posição vendida de 25.376 para 22.913 (-9,7%) — o net
long subiu de 107.945 para 120.246 contratos (+11,4% na semana), e como
fração do open interest (661.652 contratos) está em 18,17% — o mais alto
entre soja (12,49%) e farelo (11,89%). Esse posicionamento assimétrico segue
sendo, ao mesmo tempo, evidência de convicção de fundos na tese estrutural e
o maior fator de risco de uma correção mais aguda se o sentimento virar.

**Os forecasts estatísticos internos (25/07/2026)**, recalculados com o spot
revisado, mantêm o viés altista: central 7d = 75,89 cts/lb (bandas
71,24-80,54); central 30d = 84,51 cts/lb (bandas 74,89-94,14) — praticamente
inalterados frente à geração de ontem.

### O que invalida / risco para o óleo

- **Um fechamento de segunda-feira (27/07) abaixo de 73,30 (mínima de
  sexta)** confirmaria a primeira sequência de dois dias de fraqueza desde o
  início do rali, reforçando o sinal tático — agora um pouco mais brando
  depois da revisão, mas ainda o gatilho mais direto a observar.
- **O oil share continuar caindo abaixo de 52,62%** — se a tendência
  persistir por mais uma ou duas sessões, a narrativa estrutural de "óleo
  domina o crush" começaria a perder sustentação também no dado tático.
- **O próximo corte do COT (28/07, publicação ~31/07) mostrar realização de
  lucro no net long mais concorrido das três pernas (18,17% do OI)** — o
  risco estrutural de médio prazo mais relevante.
- **A isenção PIS/Cofins do biodiesel expirar em 31/07 sem renovação** (ver
  Lente fiscal) — um vetor bearish direto para a demanda doméstica de óleo,
  independente do CBOT.
- **MPOB seguir inacessível** — hoje é o 16º dia consecutivo com o mesmo
  conteúdo sem números extraídos, mantendo cego o efeito do El Niño e dos
  vetores regulatórios indonésios sobre o prêmio de substituição via palma.

### Leitura operacional — óleo

A revisão de hoje não muda a direção da leitura operacional de ontem, mas
reduz sua urgência. Para quem está comprado direcional, a recomendação
segue sendo reavaliar o tamanho da posição — a tese estrutural (ISO 100/100,
backwardation na curva, RIN D4/biodiesel) segue de pé, e o fechamento
revisado (11,6% do range, não mais 2,7%) sugere uma fraqueza tática real,
mas não necessariamente uma rejeição tão severa quanto a leitura de ontem
havia descrito; um stop na mínima de sexta (73,30) segue sendo a referência
mais próxima. Para quem opera vendido ou via spread, a operação relativa
"farelo forte / óleo fraco" (capturada pelo oil-meal spread, que comprimiu
-18,1% na sessão revisada) segue sendo a leitura mais atraente dentro do
complexo — mais do que uma posição outright vendida em óleo, que ainda
enfrentaria a tese estrutural (ISO, RIN D4) como vento contrário. Como não
há pregão hoje, a ação prática é aguardar a abertura de segunda-feira contra
o nível de 73,30 e observar se o oil share continua a série de quedas.

---

## Spreads e crush — leitura de complexo

### Crush margin: 2,9568 USD/bu (revisado) — ainda o menor valor da janela recente

Com os valores revisados de sexta-feira, a crush margin caiu -5,82% no dia
(de 3,1395 para 2,9568 USD/bu), muito próxima da queda de -5,67% calculada
ontem com o dado ainda não revisado, e segue sendo o menor valor de toda a
janela observada (07-20: 3,0316; 07-21: 3,1047; 07-22: 3,1895; 07-23:
3,1395; 07-24 revisado: **2,9568**). O mecanismo segue o mesmo: a soja (o
custo) subiu mais rápido do que a soma de farelo e óleo (a receita) na
sessão de sexta.

### Ratio Far/Soj: 80,02% (revisado) — a 0,02pp do piso de 80%, o dado mais importante desta leitura

**Este é o ponto central da leitura de hoje.** O valor revisado no dump de
25/07 mostra o ratio caindo de 80,13% para 80,02% na sessão de sexta — o
oposto do pequeno ganho (+0,04pp) que a leitura de 24/07 havia registrado
com o dado ainda não revisado. O ratio segue tecnicamente dentro da zona
"neutra" (entre 80% e 87%), mas pela margem mais estreita de toda a janela
observada desde 20/07 (79,28%→80,37%→80,65%→80,13%→**80,02%**) — a máxima
recente de 80,65% (22/07) segue intocada, mas a mínima de 79,28% (20/07)
está, pela primeira vez desde então, genuinamente ao alcance de um único
fechamento fraco. Trata `alerta-quebra_resistencia-farelo_cbot-2026-07-24`
e a revisão `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
(agora 37 dias vencida — ver seção Farelo).

### Oil share: 52,62% (revisado) — primeira queda fora da faixa recente, magnitude revisada para baixo

Queda de -0,56 ponto percentual frente a quinta-feira (53,18%→52,62%),
revisada para baixo frente aos -0,63pp calculados ontem, mas ainda o
primeiro valor fora da banda estreita de 53,0-53,5% em que o indicador vinha
oscilando nos cinco pregões anteriores. O óleo perdeu participação relativa
no valor do crush na sessão de sexta — coerente com a queda isolada do óleo
e a alta do farelo na mesma sessão, mesmo com as magnitudes revisadas.

### Oil-meal spread: 0,8041 USD/bu (revisado) — compressão de -18,1%, ainda a maior desta janela

Queda de -18,1% no dia (0,9823→0,8041 USD/bu), revisada para baixo frente
aos -20,3% calculados ontem, mas ainda de longe a maior variação diária
deste indicador na janela observada. O farelo ganhou terreno relativo sobre
o óleo de forma expressiva na sessão de sexta.

### Margem de biodiesel: 1,0354 USD/gal (revisado) — queda de -6,28%, menor que a inicialmente calculada

A margem caiu -6,28% no dia, uma queda bem menor do que os -9,88% calculados
ontem com o heating oil ainda não revisado. O volume de heating oil da
sessão também foi revisado para baixo (-44,8%, de 41.488 para 22.882
contratos) — a segunda revisão relevante de volume de heating oil desta
série em dois dias consecutivos (a primeira, de 23/07, foi de quase 900x).
Este padrão recorrente justifica tratar qualquer leitura de volume de
heating oil como provisória até a confirmação do dia seguinte.

### COT: corte de 21/07, ainda o mais recente — sem atualização nesta leitura

O corte de 21/07/2026 segue sendo o dado de posicionamento mais recente
disponível — mostra managed money comprando agressivamente as três pernas
na semana do rompimento: net long +73,6% em soja, +57,8% em farelo, +11,4%
em óleo. Em fração do open interest, óleo segue sendo a perna mais
concorrida (18,17%), seguida por soja (12,49%) e farelo (11,89%). Sem
sessão nova hoje, este dado permanece inalterado desde a leitura de ontem —
o próximo corte (28/07, publicação normal ~31/07) é o próximo capaz de
dizer se essa compra se sustentou.

### ISF em 80/100, ISO em 100/100 — ambos com print explícito de 25/07, inalterados

O Índice de Sobra de Farelo (4/5 condições) e o Índice de Suporte do Óleo
(5/5 condições) permanecem exatamente nos mesmos níveis, agora confirmados
por um print datado de hoje (25/07) mesmo sem pregão — esses índices captam
condições estruturais, não a mecânica tática de preço de curto prazo. Para
o farelo, a tensão entre o índice estrutural (ainda bear) e o COT
(fortemente bullish) permanece o ponto mais importante em aberto, agora
mais aguda porque o ratio tático está no limiar de 80%.

### O que os índices dizem juntos em 25/07/2026 (fim de semana, sessão de referência 24/07)

ISF 80/100 + ISO 100/100 (ambos com print de hoje, inalterados) + ratio
Far/Soj revisado para 80,02% (a 0,02pp do piso de 80%, o dado mais tenso
desta janela) + crush margin no menor nível da janela (2,9568 USD/bu,
revisado) + oil share fora da faixa recente (52,62%, revisado) + oil-meal
spread na maior compressão da janela (-18,1%, revisado) + COT ainda parado
no corte de 21/07 (compra maciça de fundos nas três pernas, mais
concentrada proporcionalmente em soja mas em nível absoluto mais
concentrada em óleo) + margem de biodiesel revisada para uma queda menor
(-6,28%, não -9,88%) — formam um quadro em que a revisão de dados de hoje,
tomada como um todo, é **modestamente favorável à soja, neutra a
levemente desfavorável ao óleo (fraqueza confirmada, porém mais branda), e
tacitamente mais tensa para o farelo**, porque o ratio — a métrica mais
citada nesta série para arbitrar a tese estrutural bear — está, pela
primeira vez, genuinamente ao alcance de confirmar essa tese num único
fechamento de segunda-feira. A lição mais importante desta leitura de fim de
semana: **os números "definitivos" de um dia de pregão, nesta série, não
são de fato definitivos até o dump do dia seguinte** — um padrão que já se
repetiu por dois dias consecutivos (23/07 revisado em 24/07; 24/07 revisado
em 25/07) e que deveria, a partir de agora, ser tratado como parte
estrutural do processo, não como anomalia pontual.

---

## Lente fiscal e regulatória BR

**Isenção PIS/Cofins biodiesel — vencimento em 31/07/2026, agora a apenas 6
dias, e ainda sem sinalização pública de renovação** (evento
PISCOFINS-BIODIESEL-ISENCAO, `atualizado_em` 2026-06-05, sem mudança desde
então). Trata `trib-PISCOFINS-BIODIESEL-ISENCAO-2026-07-31`. **O mecanismo:**
a isenção incide na saída do biodiesel; se expirar sem renovação em 31/07, o
custo tributário efetivo da produção de biodiesel sobe, o que tende a
reduzir a margem de biodiesel doméstica (distinta da margem americana
calculada nesta leitura, que usa RIN D4 e heating oil dos EUA) e, por
extensão, pressionar a demanda por óleo de soja como insumo dentro do mix
B15 mandatório — um vetor bearish direto para óleo, independente do que
acontecer no CBOT. **Com apenas 6 dias até o vencimento e o monitor
tributário há 50 dias sem qualquer atualização** (`atualizado_em`
2026-06-05 em todos os dez eventos rastreados), o risco de execução descrito
nas leituras anteriores (decisão de renovar saindo de última hora, como
ocorreu com a prorrogação anterior de 29/mai, e o sistema não capturando a
tempo) chega ao seu momento mais crítico — a próxima semana de pregão
(27-31/07) coincide exatamente com a janela final de decisão. Esta segue
sendo a leitura de maior prioridade de monitoramento tributário desta série,
agora com urgência máxima.

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L) — a
vigência formal (`vigencia_ate` 11/07/2026) venceu há 14 dias, e o monitor
tributário segue sem qualquer atualização de status** (evento MP-1358-2026,
`atualizado_em` 2026-06-05, status ainda "tramitacao"). Enquanto o
combustível fóssil segue subsidiado, a competitividade relativa do
biodiesel dentro do mix B15 mandatório fica pressionada.

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
contração da crush margin (agora no menor nível revisado da janela), que
reduz o incentivo tático de curto prazo mesmo com o alívio tributário
estrutural intacto.

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
soja). Esses vetores seguem, em conjunto, num sentido estruturalmente
bullish para o óleo de soja via substituição de palma — mas continuam
inverificáveis pelo lado dos dados de mercado (MPOB inacessível há 16 dias
consecutivos, ver Honestidade).

**O monitor tributário como um todo está há 50 dias sem qualquer
atualização** (`atualizado_em` 2026-06-05 em todos os dez eventos
rastreados) — o intervalo segue crescendo exatamente na semana em que a
isenção PIS/Cofins do biodiesel chega ao vencimento (6 dias). Vale
sinalizar este ponto, mais uma vez e com urgência máxima, como prioridade de
manutenção do sistema, independentemente da leitura de preço.

---

## Riscos e eventos próximos

**A isenção PIS/Cofins do biodiesel vence em 31/07/2026, agora a apenas 6
dias**, sem sinalização de renovação — o vetor tributário mais próximo de um
desfecho concreto nesta leitura, e a prioridade máxima de monitoramento até
a resolução, especialmente porque a janela de decisão coincide com a
semana de pregão que se abre segunda-feira (27-31/07).

**O ratio Far/Soj fecha a semana em 80,02% (revisado), a 0,02 ponto
percentual do piso de 80% que confirmaria a tese estrutural bear do
farelo** — a abertura de segunda-feira (27/07) é, portanto, a sessão mais
importante desta janela para essa tese específica, que segue sem resolução
tática desde 20/07 e cuja revisão D+7 (`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`)
está hoje 37 dias vencida.

**O próximo corte do COT (referente a 28/07/2026, publicação normal
~31/07/2026)** é o dado mais aguardado agora — vai mostrar se a compra
maciça de fundos documentada na semana de 21/07 se sustentou durante a
sessão de sexta-feira (24/07) e a semana que se abre, ou se já começou a
reverter.

**O USDA Crop Progress deve publicar nova leitura por volta de 26/07/2026 —
amanhã** — o primeiro dado potencialmente novo desta janela de fim de
semana, ainda antes da reabertura do pregão.

**O padrão de revisão de dados de um dia para o outro, agora confirmado por
dois dias consecutivos (23/07 revisado em 24/07; 24/07 revisado em 25/07),
deve ser tratado como estrutural do processo de coleta, não como anomalia
pontual** — recomenda-se, a partir desta leitura, sempre cruzar os números
de "ontem" citados em qualquer leitura contra os valores como aparecem no
dump do dia seguinte antes de tomar uma decisão tática baseada neles.

**NOPA — segue inacessível** (fila `release-nopa-2026-07-25` tratada aqui,
sem dado interpretável, apenas nova data de coleta), sem crush americano
confirmado por fonte primária.

**MPOB — sem números de palma extraídos há 16 dias consecutivos**, mantendo
cego o efeito do El Niño e dos vetores regulatórios indonésios sobre o
prêmio de substituição do óleo de soja.

---

## Honestidade

O que não foi possível validar neste briefing de 25/07/2026, onde a
confiança é baixa ou há lacunas materiais:

**1. A sessão de 24/07/2026 chegou revisada no dump de hoje, pela segunda
vez consecutiva que este padrão se repete nesta série.** Soja fechamento
1.239,00→1.240,25 (+0,10%); farelo 331,10→330,80 (-0,09%); óleo
73,34→73,47 (+0,18%); heating oil 4,1311→4,1806 (+1,20%) com volume
41.488→22.882 contratos (-44,8%). As magnitudes de preço são pequenas, mas
o efeito sobre o ratio Far/Soj foi qualitativamente relevante: o dado não
revisado sugeria um ratio subindo (+0,04pp); o dado revisado mostra o
ratio caindo (-0,15pp), com o valor final (80,02%) a apenas 0,02pp do piso
de 80%. Não é possível, a partir deste briefing, determinar a causa raiz da
revisão (ajuste de fonte, reprocessamento de pipeline, ou correção de
arredondamento acumulado), mas a repetição do padrão por dois dias seguidos
(a divergência anômala de 23/07 documentada na leitura de ontem, e agora
esta) sugere que se trata de uma característica estrutural do pipeline de
dados, não de um evento isolado. Recomenda-se, a partir de agora, tratar
todo número de "fechamento de hoje" citado em qualquer leitura desta série
como sujeito a revisão no dump do dia seguinte, e cruzar antes de agir sobre
níveis técnicos apertados (como o ratio Far/Soj está agora).

**2. Como no dia 24/07, a seção bruta `cme_cbot` deste dump não permite
confirmar de forma independente, por fonte primária, se a revisão de sexta
teve origem em correção de coleta ou em republicação legítima de dado
final** — esta leitura trata o valor mais recente do dump como o mais
confiável disponível, seguindo a mesma convenção estabelecida ontem.

**3. Sem pregão hoje (sábado), não há dado de preço novo a validar — toda a
análise desta leitura descreve a sessão de 24/07/2026 (sexta-feira), a mais
recente disponível.** A próxima sessão de referência é segunda-feira,
27/07/2026.

**4. O prêmio de exportação de farelo em Paranaguá (+0,05 USD/sht) e o de
óleo (+0,08 cts/lb) estão no mesmo valor exato desde pelo menos 03/07/2026**
(NAG, agora 22 dias corridos sem variação de nenhum centavo) — não é
possível distinguir se isso reflete um mercado de exportação genuinamente
parado ou um valor que não está sendo atualizado de fato na fonte.

**5. Os níveis de resistência/suporte de 1.180,00 (soja) e 325,00 (farelo)
são alertas gerados pelo sistema de calibração interna, cuja metodologia de
definição de nível não é visível a partir deste briefing** — esta leitura
trata os níveis como dado (o sistema já os fiscaliza automaticamente), sem
poder validar de forma independente os critérios técnicos usados para
calibrá-los.

**6. O COT (CFTC) segue no corte de 21/07/2026, uma terça-feira — não cobre
a sessão de sexta-feira (24/07) nem o fim de semana** — o próximo corte
(28/07, publicação normal ~31/07) é o primeiro capaz de capturar esse
período, incluindo a possível reação dos fundos ao ratio Far/Soj agora no
limiar técnico.

**7. Percentis históricos de COT não calculados** — os números de
21/07/2026 seguem lidos apenas em nível absoluto e como fração do open
interest corrente (soja 12,49%, farelo 11,89%, óleo 18,17%), sem série
histórica completa para calibrar se algum desses níveis está objetivamente
"esticado" no sentido histórico.

**8. O WASDE segue cobrindo apenas farelo (Argentina, Brasil, China
parcial), sem nenhum dado de soja em grão ou óleo de soja, em qualquer
geografia, e sem nenhum dado dos Estados Unidos** — sem atualização desde
10/07/2026. A pergunta central da revisão D+7 vencida ("o WASDE mudou o
quadro?") segue sem canal de resposta interno.

**9. NOPA (fila `release-nopa-2026-07-25`) segue com `monthly_status` em
0,0 bool** — mesma barreira de assinatura paga documentada desde meados de
junho, agora com mais de um mês e meio sem alternativa de dado primário
sobre o esmagamento americano. A "novidade" sinalizada pela fila é apenas a
data de coleta, não um dado genuinamente interpretável.

**10. Palma malaia (MPOB) segue sem números extraídos, agora por 16 dias
consecutivos com o mesmo conteúdo exato (3.439 caracteres, de 10/07 a
25/07/2026)** — a persistência do byte count idêntico segue sugerindo,
possivelmente, uma página que não está mais sendo servida com conteúdo
atualizado. Continua impossível avaliar o efeito do El Niño ou dos vetores
regulatórios indonésios sobre o prêmio de substituição do óleo de soja.

**11. Clima INMET (BR) não foi usado como driver de preço desta leitura.**
Julho é entressafra da soja brasileira (colheita concluída, plantio só em
outubro) — sem relevância direta para a tese de preço neste momento do
calendário agrícola. O El Niño Advisory (NOAA CPC, inalterado desde pelo
menos 03/07/2026) permanece relevante apenas para a expectativa da safra de
plantio de outubro/26 e para o clima do Sudeste Asiático (palma).

**12. A manchete de notícia do dia ("Cepea: Soja, milho e boi gordo
encerram semana com novas altas", Canal Rural, 25/07/2026) não traz número
de preço** e por isso não foi tratada como driver quantitativo — apenas
como confirmação qualitativa do tom da semana, seguindo a regra de nunca
inventar ou inferir magnitude além do que consta no briefing.

**13. BCBA Argentina — última leitura disponível é 22/07/2026**, sem
relatórios de esmagamento/exportação acessíveis via scraper, sem mudança de
padrão.

**14. RIN D4 como parâmetro fixo (2,11 USD/RIN) segue sendo uma fonte
relevante de incerteza do modelo de biodiesel**, sem novo dado hoje — a
margem calculada em 1,0354 USD/gal (revisada) usa esse valor fixo. O volume
de heating oil, revisado para baixo pela segunda vez em dois dias
consecutivos (-44,8% hoje, quase -900x em 23/07), segue sendo a maior fonte
de incerteza deste indicador específico.

**15. A proximidade do ratio Far/Soj ao piso de 80% (80,02%, revisado) é o
achado central desta leitura de fim de semana, e permanece sem confirmação
até o fechamento de segunda-feira (27/07)** — esta leitura recomenda não
tratar o valor revisado como confirmação da tese estrutural bear até que o
mercado efetivamente feche abaixo de 80% num pregão novo, apenas como o
gatilho técnico mais próximo de toda a janela observada.

*Nenhum número foi inventado ou estimado além do que consta no briefing de
25/07/2026 e nos insights anteriores referenciados. A contribuição central
desta leitura foi identificar que o padrão de revisão de dados documentado
pela primeira vez na leitura de 24/07/2026 (sessão de 23/07 revisada no dia
seguinte) se repetiu, desta vez para a sessão de 24/07/2026 — e que essa
revisão, embora pequena em magnitude de preço, inverteu o sinal direcional
do ratio Far/Soj (de alta para queda) e deixou esse indicador a apenas
0,02 ponto percentual do piso técnico de 80% que confirmaria a tese
estrutural bear do farelo, tornando a abertura de segunda-feira (27/07) a
sessão mais importante desta janela para essa tese específica. Também foi
possível, pela primeira vez nesta série, comparar o prêmio físico de
exportação em Paranaguá contra a paridade teórica usando dados de mesmo
dia (24/07 contra 24/07), resolvendo uma lacuna sinalizada nas duas leituras
anteriores.*
