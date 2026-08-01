---
data: 2026-07-31
titulo: "Sessão de baixa liderada por farelo e óleo com a soja tecnicamente indecisa: soja (1.171,25 cts/bu, CBOT 2026-07-31, 0,00% no fechamento, mas com a máxima do dia — 1.179,25 — ficando pela primeira vez em 3 sessões SEM sequer tocar o nível de 1.180,00) fecha no meio do range enquanto farelo (314,50, -0,94%) e óleo (67,47, -1,10%) caem mais forte, derrubando a crush margin em -5,01% (para 2,6282 USD/bushel) e o ratio Far/Soj de volta a 80,55% (de 81,25% revisado ontem); o COT de 28/jul (CFTC, divulgado hoje pela primeira vez nesta janela) revela que os fundos AUMENTARAM o net long em soja (+22,97%, para 15,73% do open interest) e farelo (+19,35%, para 14,11%) via cobertura de posição vendida, na semana que antecedeu a queda de -2,78%/-2,12% que se seguiu até hoje, enquanto no óleo os fundos já vinham REDUZINDO o comprado (-10,27%) antes mesmo da 5ª sessão seguida de quebra do suporte técnico de 72,00 (agora -6,29% abaixo, a mais funda desta janela) — tudo isso no dia exato do vencimento da isenção PIS/Cofins do biodiesel, sem qualquer sinal de renovação em 56 dias"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT (ZSU26 soja / ZMU26 farelo / ZLU26 óleo / HO=F heating oil) — sessão de 2026-07-31, com a sessão de 2026-07-30 usada para comparação (valores revisados no dump de hoje)
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, paridade BR, Índice de Sobra de Farelo, Índice de Suporte do Óleo) — 2026-07-31, com a série 2026-07-27→2026-07-31 usada para contexto (única profundidade disponível nesta janela — ver Honestidade)
  - BCB PTAX — 2026-07-31 (USD/BRL 5,0773, EUR/BRL 5,849, Selic diária 0,052531% a.a.), comparado a 2026-07-30
  - CEPEA/ESALQ Soja Paranaguá via NAG — 2026-07-31 (R$ 144,91/saca, var -0,26%)
  - CEPEA/ESALQ Soja Paraná interior via NAG — 2026-07-31 (R$ 137,27/saca, var -0,40%)
  - NAG Físico BR — 2026-07-31 (farelo MT/IMEA R$ 1.675,10/ton, +0,32%; Rondonópolis R$ 1.700,00/ton, +3,03%; RS R$ 1.640,00/ton, estável; prêmios export PGUA farelo +0,05 USD/sht e óleo +0,08 cts/lb, ambos inalterados)
  - CFTC COT Managed Money — corte de 2026-07-28 (NOVO, primeira aparição nesta janela, trata a fila `release-cftc_cot-2026-07-28`), comparado ao corte anterior de 2026-07-21
  - USDA Crop Progress — ainda 2026-07-26 (11% excelente + 52% boa + 7% ruim), sem corte novo (5 dias, dentro da cadência semanal normal)
  - USDA WASDE — ausente da janela deste briefing, agora 21 dias de atraso desde o último dado (10/07/2026)
  - NOPA — fila `release-nopa-2026-07-31`, `monthly_status` continua em 0,0 bool (paywall), mesma barreira desde meados de junho
  - ABIOVE projeções mensais — balanços ago-dez/2026 (farelo/óleo/soja), sem alteração
  - NOAA CPC ENSO — 2026-07-31 (El Niño Advisory, inalterado desde pelo menos 16/07/2026)
  - MPOB — 2026-07-31 (conteúdo idêntico de 3.439 caracteres, parser sem números extraídos, agora o 22º dia consecutivo nesse estado segundo a continuidade documentada nas leituras anteriores)
  - BCBA Argentina — 2026-07-31 (2ª sessão seguida acessível após o hiato de 7 dias documentado ontem; ainda sem links de relatório detectados)
  - Notícias Agrícolas/Farm Progress RSS — 2026-07-31 (160 itens lidos, 7 mantidos; manchete "Why one storage plan won't work for both corn and soybeans", farmprogress.com, sem conteúdo de preço)
  - Forecasts estatísticos internos — 2026-07-31 (spot ref reflete o fechamento de hoje; viés "altista" nas três — ver Honestidade)
  - system/tributario_watch.toml (lido apenas como referência, não editado) — `atualizado_em` 2026-06-05, agora 56 dias sem atualização, no dia exato do vencimento (`vigencia_ate` 2026-07-31) do evento PISCOFINS-BIODIESEL-ISENCAO
  - Cruza com [[2026-07-30_leitura-complexo]] (leitura de ontem, parcialmente revisada aqui) e [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (D+7 formalmente vencido, tratado abaixo)
status: ativa
vies: [bear-soja, neutral-farelo, bear-oleo_soja]
---

## Visão geral

O complexo soja é, mecanicamente, uma fábrica com uma única matéria-prima (a
soja em grão) e dois produtos de saída em proporção fixa por bushel esmagado:
o **farelo** (a fração proteica, ~78% da massa, vira ração animal) e o
**óleo degomado** (a fração de gordura, ~18-20% da massa, vira óleo de
cozinha e biodiesel). Quem decide o ritmo de esmagamento é a esmagadora,
olhando a **crush margin** (o valor de farelo + óleo por bushel, menos o
custo daquele bushel de soja, todos medidos na CBOT — Chicago Board of
Trade, a bolsa de referência mundial para esses três contratos) e o **oil
share** (a fração desse valor capturada especificamente pelo óleo). O
**ratio Far/Soj** (preço do farelo dividido pelo preço da soja, normalizado
pela conversão bushel↔short ton) mede o mesmo crush por outro ângulo: abaixo
de 80% o farelo está historicamente "abundante" frente à soja — zona bear —,
acima de 87% está "apertado" — zona bull —, e entre os dois fica a zona
neutra de **mean-reversion**, onde o spread oscila nos dois sentidos e não
dá, sozinho, uma direção clara de preço.

**A sessão de hoje foi de baixa liderada claramente pelas duas pernas de
saída do esmagamento — farelo e óleo — com a soja presa no meio, incapaz de
se afirmar em qualquer direção.** A soja (CBOT, ticker ZSU26.CBT) fechou
exatamente onde abriu, 1.171,25 cts/bushel, 0,00% no dia (ante o fechamento
revisado de ontem de 1.172,25) — mas dentro do pregão fez máxima de 1.179,25
e mínima de 1.164,00, um range de 15,25 cts que terminou com o fechamento
quase no meio (47,5% do range). O detalhe técnico mais relevante do dia para
a soja é que essa máxima de 1.179,25 **ficou, pela primeira vez em três
sessões, sem sequer tocar o nível de 1.180,00** que a soja rompeu para baixo
em 29/07 e que vinha sendo testado por cima nas duas sessões seguintes
(1.181,25 em 30/07, ultrapassando o nível; hoje, 1.179,25, sem alcançá-lo) —
um padrão de **máximas decrescentes** que, tecnicamente, é uma confirmação
adicional de que o nível de 1.180,00 está se consolidando como resistência,
mesmo que o fechamento do dia, isoladamente, pareça neutro. Farelo (ZMU26.CBT)
caiu -0,94% (317,50→314,50 USD/short ton) e óleo (ZLU26.CBT) caiu -1,10%
(68,22→67,47 cts/lb) — as duas pernas do crush caindo mais que a soja fez a
**crush margin** despencar -5,01% no dia, para **2,6282 USD/bushel** (a
maior queda diária desta janela observada), e o **ratio Far/Soj** recuar de
volta para **80,55%** (de 81,25% revisado ontem) — a sexta sessão seguida em
que o indicador testa a vizinhança do piso de 80% sem nunca ter fechado de
forma inequívoca e sustentada do outro lado dele, o mesmo gatilho tático que
a fila de julgamento volta a cobrar hoje (`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`,
agora formalmente vencido desde 18/06/2026 — tratado em detalhe na seção
Farelo). O óleo, por sua vez, estendeu pela **quinta sessão seguida** a
quebra do suporte técnico de 72,00, fechando **6,29% abaixo dele** — a
distância mais funda desta janela — e a fila sinaliza isso de novo hoje
(`alerta-quebra_suporte-oleo_cbot-2026-07-31`). **O desenvolvimento mais
importante da sessão, no entanto, não veio do preço: veio do COT (CFTC) de
28/07/2026, divulgado hoje pela primeira vez nesta janela** (trata
`release-cftc_cot-2026-07-28`). Ele mostra que, entre 21/07 e 28/07 — uma
semana em que o preço da soja ainda estava alto (fechou 28/07 em 1.204,75) —
os fundos administrados (managed money) **aumentaram** o net long em soja em
+22,97% (para 15,73% do open interest, ante 12,49%) e em farelo em +19,35%
(para 14,11%, ante 11,89%), em ambos os casos majoritariamente via **cobertura
de posição vendida** (o managed money short caiu -21,15% em soja e -22,40%
em farelo) mais uma fatia de compra nova. Só que, **desde aquele fechamento
de 28/07 até hoje, a soja caiu -2,78% e o farelo caiu -2,12%** — ou seja, boa
parte dessa posição comprada reforçada está, neste exato momento, sentada em
prejuízo de papel. No óleo aconteceu o oposto: os fundos já vinham
**reduzindo** o net long (-10,27%, para 16,60% do OI, ante 18,17%) entre
21/07 e 28/07, antes mesmo de o óleo cair mais -3,81% entre 28/07 e hoje —
uma redução de exposição que, em retrospecto, evitou parte da dor que quem
ficou comprado em soja e farelo está sentindo agora. **Leitura de uma
linha:** o pivô do complexo hoje não é mais só o técnico do óleo (que segue
se aprofundando, agora pela quinta vez) — é o contraste entre um book
especulativo que ficou mais pesado em soja e farelo bem no topo do movimento
recente e um book de óleo que já vinha se descomprimindo antes da queda
continuar; a maior convicção desta leitura é que essa assimetria de
posicionamento aumenta o risco de um movimento de liquidação forçada
("stop-run") em soja/farelo caso o preço continue caindo, enquanto o óleo
tem, relativamente, menos gasolina especulativa represada do lado comprado
para alimentar uma queda adicional por esse canal específico; confiança
moderada-alta nessa leitura de posicionamento (dado concreto, novo, e
mecanicamente claro), e confiança moderada no viés direcional da soja
isoladamente, que hoje ficou tecnicamente mais neutra que nas duas sessões
anteriores.

---

## Soja

**Viés: bear tático moderado, mais fraco que nas duas últimas sessões — a
soja fechou 1.171,25 cts/bushel (CBOT, ticker ZSU26.CBT), exatamente igual
ao valor de abertura (0,00% no dia), depois de fazer máxima de 1.179,25 e
mínima de 1.164,00.** Nenhum item da fila de julgamento de hoje trata
explicitamente da soja de forma isolada (os cinco itens tratam óleo, o
ratio Far/Soj, o tributário do biodiesel, o NOPA e o COT) — mas o COT novo
(`release-cftc_cot-2026-07-28`) tem implicação direta e relevante para a
soja, tratada abaixo.

### O que sustenta a tese

**A sessão foi de abertura estável, alta inicial que não chegou a testar o
nível-chave de 1.180,00, venda até um novo patamar de mínima, e recuperação
final até fechar exatamente no nível de abertura — um dia de indecisão, mas
com um detalhe técnico que pesa ligeiramente para o lado vendedor.** Abertura
1.171,25 (0,00% sobre o fechamento revisado de ontem de 1.172,25, um gap
praticamente nulo), máxima 1.179,25 (tocada e vendida de volta), mínima
1.164,00 (um novo patamar, abaixo tanto da mínima de ontem — 1.168,00 — quanto
da mínima de anteontem) e fechamento em 1.171,25 — **47,5% do range**
((1.171,25-1.164,00)÷(1.179,25-1.164,00)), um fechamento em torno do meio,
sem viés forte de fechamento dentro do próprio pregão. **O ponto central,
porém, não é o fechamento — é a máxima.** Nas duas sessões anteriores, a
soja vinha testando por cima o nível de 1.180,00 (rompido para baixo em
29/07): em 30/07 a máxima chegou a 1.181,25, ultrapassando o nível antes de
ser rejeitada; hoje, a máxima ficou em 1.179,25, **0,75 cts ABAIXO de
1.180,00 — a primeira sessão em que o preço nem sequer tenta romper de volta
o nível.** Mecanicamente, isso é uma **máxima decrescente** (1.181,25 →
1.179,25) num contexto de teste de resistência: cada tentativa de recuperar
o nível rompido está ficando mais fraca que a anterior, o que — mesmo sem um
fechamento fortemente negativo hoje — reforça, e não enfraquece, a leitura
de que 1.180,00 está se consolidando como teto de curto prazo. O volume foi
de 21.839 contratos, o menor desta janela recente de OHLCV disponível (que
cobre apenas 30/07 e 31/07 nesta consulta — ver Honestidade), o que impede
uma comparação de convicção via volume mais ampla que dois dias.

**O câmbio hoje reverteu parcialmente a queda forte de ontem, voltando a
trabalhar (de forma modesta) contra a soja em reais.** USD/BRL PTAX fechou
em 5,0773 (BCB, 2026-07-31), alta de +0,07% sobre 5,0739 de ontem — depois
da queda de -0,93% registrada ontem, que havia sido o maior movimento
cambial de um único dia desta janela. **Mecanismo:** a paridade teórica em
reais (preço CBOT em cts × PTAX, sem considerar basis/frete/ágio local) hoje
ficou em **R$ 131,10/saca** (indicators, 2026-07-31: CBOT 1.171,25 cts ×
USD/BRL 5,0773), praticamente estável frente aos R$ 131,13/saca do dia
anterior (-0,02%, indicators, 2026-07-30 revisado) — como o CBOT ficou
estável e o câmbio subiu apenas 0,07%, os dois efeitos hoje quase se
cancelaram, resultando numa paridade essencialmente parada. Isso contrasta
com o movimento de ontem, quando CBOT e câmbio caíram juntos e derrubaram a
paridade em -1,30%. **Para quem opera a paridade em reais, o dia de hoje foi
de acomodação, não de novo choque** — o teste real de se a reversão cambial
de ontem tinha "pernas" para continuar ficou, por ora, sem resposta clara.

**A base física em Paranaguá caiu menos que a paridade teórica, mas o
prêmio de exportação comprimiu ligeiramente pela primeira vez em várias
sessões, depois de uma sequência de alargamento.** CEPEA/ESALQ Soja
Paranaguá (via NAG) fechou em R$ 144,91/saca hoje, queda de -0,26% sobre R$
145,29 de ontem. Com a paridade teórica praticamente parada (R$ 131,10,
-0,02%), o **prêmio de exportação sobre a paridade recuou para +10,53%**
((144,91-131,10)÷131,10), ante +10,80% no cálculo equivalente de ontem (usando
os valores revisados disponíveis hoje: 145,29 vs paridade 131,13) — uma
compressão de cerca de -0,27 ponto percentual, a primeira desde que a
sequência de alargamento começou. **Mecanismo e leitura:** o movimento é
pequeno e não inverte a tendência estrutural documentada nas últimas
leituras (o prêmio segue historicamente elevado, perto do teto da janela
observada), mas é o primeiro sinal, ainda que tênue, de que o físico pode
estar começando a "alcançar" o papel depois de várias sessões de
descolamento — uma das duas hipóteses já levantadas nas leituras anteriores
(a outra sendo simples atraso de atualização do preço CEPEA/ESALQ). O físico
do Paraná interior também caiu, -0,40% (R$ 137,27/saca) — um pouco mais que
a queda de Paranaguá, mas ainda moderado frente à volatilidade do papel.

**A curva forward mostrou uma pequena reversão da inversão de calendário
documentada nas últimas sessões.** Agosto/26 (Q26) 1.170,75 → Setembro/26
(U26, spot) 1.171,25 → Novembro/26 (X26) 1.188,25 → Janeiro/27 (F27) 1.201,75
→ Março/27 (H27) 1.205,25. Hoje, Agosto está **0,50 cts (-0,04%) ABAIXO** do
spot de setembro — nas duas últimas sessões, Agosto vinha precificado
LEVEMENTE ACIMA do spot (uma pequena inversão técnica de calendário
documentada como recorrente). A diferença de hoje é mínima e pode ser ruído,
mas, tomada ao pé da letra, ela representa uma normalização parcial da forma
da curva no vencimento mais próximo — sem, no entanto, nenhum sinal novo de
estresse físico na parte de trás da curva (U26→X26→F27→H27 seguem em
contango crescente, forma idêntica à documentada nos últimos dias).

**O COT novo de 28/07/2026 (CFTC, divulgado hoje, trata `release-cftc_cot-2026-07-28`)
é o dado mais relevante da sessão para a tese de soja, e aponta para um
posicionamento especulativo que ficou MAIS esticado, não menos, na semana
que antecedeu a fraqueza técnica dos últimos dias.** O managed money net
long subiu de +130.505 contratos (21/07, 12,49% do open interest de
1.045.077) para **+160.479 contratos (28/07, 15,73% do open interest de
1.020.108)** — um aumento de **+22,97%** em uma única semana, e o maior
salto percentual de net long documentado nesta série de leituras.
**Mecanismo:** o aumento veio de dois lados simultâneos — o managed money
long subiu +10,81% (180.163→199.637) e o managed money short caiu -21,15%
(49.658→39.158) — ou seja, houve tanto compra nova quanto cobertura de
posição vendida, um padrão de "short squeeze + fresh buying" que empurrou o
net long para o percentual mais alto do open interest desta janela. **O
detalhe crítico é o timing:** o fechamento de 28/07 (data de corte do
relatório) foi de 1.204,75 — ainda perto do topo recente. **Desde então, a
soja caiu -2,78% até o fechamento de hoje (1.171,25).** Isso significa que
uma fatia relevante da posição comprada reforçada nesta semana específica
está, neste momento, com prejuízo de papel — um ingrediente clássico para
um movimento de liquidação forçada (venda de posições compradas que viram
"stop" ou margem, empurrando o preço ainda mais para baixo) caso a fraqueza
técnica continue. Esta leitura considera este o principal risco de cauda
baixista para a soja no curto prazo, mais relevante do que qualquer sinal
isolado de preço desta sessão.

**Os forecasts estatísticos internos (2026-07-31)**, recalculados com o
fechamento de hoje (1.171,25), seguem etiquetados como "altista": central 7d
= 1.181,70 cts/bu (bandas 1.124,15-1.239,25); central 30d = 1.210,25 cts/bu
(bandas 1.091,11-1.329,39). Como nas leituras anteriores, esta análise trata
o modelo (média móvel de 20 dias + volatilidade + inclinação de curto prazo)
apenas como referência de banda estatística — ele não incorpora nem o padrão
de máximas decrescentes em torno de 1.180,00 nem o novo dado de COT.

**A manchete do dia (Farm Progress, 31/07/2026, "Why one storage plan won't
work for both corn and soybeans") é de manejo/armazenamento pós-colheita
americano, sem conteúdo direto de preço ou oferta agregada** — não altera
esta leitura.

### O que invalida / risco para a soja

- **Um fechamento consistente e sustentado acima de 1.180,00** desfaria a
  leitura de máximas decrescentes de hoje — a série de testes fracassados
  precisa, em algum momento, ser rompida por uma tentativa bem-sucedida para
  que o quadro técnico volte a favorecer o lado comprado.
- **O posicionamento especulativo esticado revelado pelo COT de 28/07 (net
  long em 15,73% do OI, o maior desta janela) se desmontar de forma
  desordenada** se o preço continuar caindo — o risco de liquidação forçada
  é, nesta leitura, o principal vetor de risco baixista adicional, mas
  também pode gerar um repique técnico abrupto se o desmonte for rápido e
  seguido de estabilização.
- **O câmbio retomar com força a trajetória de alta** — hoje a reversão de
  ontem (USD/BRL -0,93%) parou de se aprofundar (+0,07% hoje), mas ainda não
  há sinal de reversão de tendência mais ampla; se o dólar voltar a subir com
  força, a paridade em reais ganha suporte independente do CBOT.
- **O prêmio de exportação em Paranaguá continuar comprimindo** — a primeira
  queda desta janela (-0,27pp hoje) pode ser o início de uma convergência
  física-papel que, se confirmada, reduziria o suporte que o físico vinha
  dando à tese de demanda firme.

### Leitura operacional — soja

O quadro de hoje é de **indecisão técnica com um viés levemente vendedor
por baixo da superfície** — o fechamento neutro (0,00%) esconde uma máxima
decrescente que, tecnicamente, é mais coerente com continuação da fraqueza
do que com uma reversão. Para quem está vendido desde o rompimento de
29/07, a sessão de hoje não oferece um sinal novo forte, mas o padrão de
máximas cadentes em torno de 1.180,00 permite um ajuste de stop mais
apertado (acima de 1.179,25, em vez de 1.181,25) sem abrir mão de proteção
relevante. Para quem está comprado, o novo dado de COT é um alerta
concreto: o próprio posicionamento comprado que sustentaria uma tese
altista (fundos net long em 15,73% do OI, o maior desta janela) é também o
que mais expõe o mercado a uma liquidação técnica caso o preço não
estabilize — operar comprado agora significa operar, em parte, contra o
risco do próprio "crowd" especulativo que já está posicionado do mesmo
lado. Para quem opera o câmbio como perna adicional, a pausa na reversão de
ontem (USD/BRL quase estável hoje) sugere aguardar mais uma sessão antes de
assumir que a tendência de alta do dólar terminou. Para quem opera o book
relativo entre papel e físico, a pequena compressão do prêmio de exportação
hoje (-0,27pp, primeira desta janela) é o primeiro sinal, ainda fraco, de
que a operação de convergência (comprar basis físico contra vender papel)
discutida nas últimas leituras pode estar começando a se realizar — vale
monitorar se a compressão continua nas próximas sessões antes de tratá-la
como confirmada.

---

## Farelo

**Viés: neutro tático dentro de uma tese estrutural bear ainda intacta — o
ratio Far/Soj fechou em 80,55% (indicators, 2026-07-31), recuando de 81,25%
(valor revisado de ontem) e voltando a se aproximar do piso de 80% depois de
ter se afastado dele nas duas sessões anteriores.** Trata
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` (a fila
de hoje sinaliza este item como **revisão VENCIDA**: o checkpoint D+7 da
tese aberta em 11/06/2026 estava marcado para 18/06/2026 — já se passaram 43
dias além do prazo formal de revisão) e o COT novo
`release-cftc_cot-2026-07-28`.

### O D+7 da tese estrutural está formalmente vencido — o que aconteceu desde 11/06

A tese original ([[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]])
apostava que a compressão rápida do ratio (83,3%→81,4% em quatro pregões,
05/06→11/06) indicaria a zona comprimida (<80%) "em 1-2 semanas" — o
checkpoint D+7 (18/06/2026) deveria confirmar ou não essa velocidade. **Sete
semanas depois do prazo formal, com os dados disponíveis nesta janela de 14
dias (27/07 em diante), o ratio nunca fechou de forma robusta e sustentada
abaixo de 80%:** 80,09% (27/07) → 80,01% revisado (28/07) → 81,10% revisado
(29/07) → 81,25% revisado (30/07) → **80,55%** (31/07, hoje). O padrão é de
um indicador que oscila numa banda estreita entre ~80% e ~81,3%, tocando o
piso, afastando-se dele, e voltando a se aproximar — sem nunca consolidar de
um lado ou de outro. **Esta leitura trata o D+7 como formalmente encerrado
sem confirmação do gatilho tático de preço**: a velocidade de compressão
observada em junho (quatro pregões, -1,9pp) não se sustentou — o ratio levou
sete semanas para, na melhor das hipóteses, chegar perto do mesmo nível de
80% em que já estava perto em 28/06, sem nunca romper com convicção. Isso
**não invalida a tese estrutural mais lenta** (ABIOVE, Índice de Sobra de
Farelo — ver abaixo), que segue intacta e é o pilar mais sólido para
qualquer viés bear em farelo nesta leitura; mas o gatilho tático específico
de preço (ratio <80% como sinal de entrada) deve, na prática, ser tratado
como não confirmado, e o próximo marco formal de revisão da tese completa
segue sendo o D+90 (2026-09-09).

### O que sustenta a leitura de hoje

**O farelo caiu mais que a soja hoje, e foi essa diferença — não um
movimento absoluto de farelo isoladamente extremo — que derrubou o ratio.**
Farelo CBOT (ZMU26.CBT) abriu em 317,50 (0,00% sobre o fechamento de ontem,
sem gap), fez máxima de 319,90 e mínima de 312,30, fechando em 314,50 —
queda de **-0,94%** no dia. O fechamento equivale a 29,3%
((314,50-312,30)÷(319,90-312,30)) do range — no terço inferior, um
fechamento fraco. O volume foi de 27.533 contratos, praticamente estável
frente aos 57.610 contratos de ontem (dado revisado disponível hoje,
-52,2% — mas a base de comparação de ontem já havia sido revisada uma vez
antes, ver Honestidade da leitura de ontem) — ainda um volume relativamente
baixo dentro do padrão desta janela, coerente com uma sessão de baixa
convicção direcional mesmo com o movimento relativo de queda.

**A crush margin sofreu a maior queda diária desta janela — -5,01%, para
2,6282 USD/bushel — e o mecanismo aponta diretamente para farelo e óleo,
não para a soja.** Board Crush: farelo 314,50 + óleo 67,47 − soja 1.171,25 =
2,6282, ante 2,7667 no valor revisado de ontem (farelo 317,50 + óleo 68,22 −
soja 1.172,25). **Mecanismo:** a soma farelo+óleo (a receita do crush) caiu
de 385,72 para 381,97, uma queda de -0,97%, enquanto o custo (soja) caiu
apenas -0,09%. Como a crush margin é a diferença entre os dois, e a receita
caiu dez vezes mais rápido que o custo, a margem inteira absorveu quase todo
o movimento — uma dinâmica oposta à de dois dias atrás (27/07→28/07), quando
as três pernas se moviam em proporções mais parecidas. **Para quem monitora
o incentivo de esmagamento, este é o dado mais relevante do dia**: mesmo
depois da queda de hoje, a margem (2,6282) segue folgada frente ao nível de
alerta histórico citado em leituras passadas (<2,50 USD/bu) — não há, ainda,
sinal de que a esmagadora precise reduzir ritmo, mas a folga diminuiu.

**O oil-meal spread caiu para 0,5027 USD/bushel** (ante 0,5192 no valor
revisado de ontem, **-3,18%**) — a quinta sessão seguida de compressão
usando a série mais consistente disponível (27/07: 0,7469 → 28/07: 0,6468 →
29/07: 0,5588 → 30/07: 0,5192 revisado → **31/07: 0,5027**). **Mecanismo:**
apesar de o farelo ter caído MAIS que o óleo em termos percentuais hoje
(-0,94% vs -1,10% — na verdade o óleo caiu mais hoje), o spread ainda
comprimiu porque a base de comparação é em pontos absolutos de USD/bushel,
não percentual: farelo caiu 3,00 USD/sht (equivalente a 0,090 USD/bu na
conversão) enquanto óleo caiu 0,75 cts/lb (equivalente a 0,3375 USD/bu na
conversão de 45 lb/bu) — o óleo, apesar da queda percentual maior, ainda
carrega um peso em dólares por bushel bem maior que o farelo, então mesmo um
farelo relativamente "mais resistente" em pontos absolutos não interrompe a
tendência de compressão do spread. Esta é uma nuance importante: a leitura
"farelo forte / óleo fraco" pelo ângulo do oil-meal spread continua válida
em termos de dólares por bushel, mesmo num dia em que o óleo caiu menos em
pontos absolutos do que pareceria à primeira vista pela variação percentual.

**O COT de 28/07/2026 (CFTC, novo, trata `release-cftc_cot-2026-07-28`)
mostra o mesmo padrão de "short squeeze + compra nova" visto em soja,
proporcionalmente ainda mais forte.** O managed money net long em farelo
subiu de +73.476 contratos (21/07, 11,89% do OI de 618.289) para **+87.696
contratos (28/07, 14,11% do OI de 621.646)** — um aumento de **+19,35%**.
Diferente da soja, aqui o aumento veio quase inteiramente de cobertura de
posição vendida: o managed money long subiu apenas +1,17% (130.152→131.677),
enquanto o managed money short caiu **-22,40%** (56.676→43.981) — ou seja,
o movimento de 21/07 a 28/07 foi predominantemente fundos comprados
recomprando posições vendidas, não uma onda de compra nova convicta.
**Timing:** o fechamento de farelo em 28/07 foi de 321,30; desde então, até
hoje, o farelo caiu **-2,12%**. Assim como na soja, uma fatia da posição
comprada reforçada nesta janela está atualmente com prejuízo de papel — mas,
como o aumento veio mais de cobertura de vendidos do que de compra nova
convicta, o risco de uma liquidação forçada adicional é, nesta leitura,
proporcionalmente menor em farelo do que em soja, ainda que a direção do
risco seja a mesma.

**A curva forward de farelo segue em contango normal e completo, sem
qualquer sinal de inversão de calendário** — a mesma forma documentada nas
últimas sessões. Agosto/26 (Q26) 311,00 → Setembro/26 (U26, spot) 314,50 →
Outubro/26 (V26) 316,20 → Dezembro/26 (Z26) 320,90 → Janeiro/27 (F27)
323,20 — uma curva inteiramente crescente do vencimento mais próximo ao mais
distante. **Mecanismo:** essa forma "normal" segue consistente com o
excedente estrutural de farelo no Brasil (ABIOVE, ver abaixo) não gerar
nenhum estresse físico de curtíssimo prazo capaz de inverter o calendário —
ao contrário do óleo, cuja curva em backwardation aponta para um aperto
físico relativo mais imediato (ver seção Óleo).

**As praças físicas de farelo no Brasil (NAG) mostraram um movimento
divergente hoje que merece registro, ainda que com cautela.** Mato
Grosso/IMEA subiu para R$ 1.675,10/ton (+0,32% sobre R$ 1.669,72 de ontem,
o primeiro movimento depois de dias estáveis) e **Rondonópolis/MT saltou
para R$ 1.700,00/ton (+3,03% sobre R$ 1.650,00, estável há mais de uma
semana)** — um movimento expressivo e isolado numa única praça. RS
permaneceu estável em R$ 1.640,00/ton. **Esta leitura trata o salto de
Rondonópolis com cautela**: é um único ponto de dado, numa praça específica,
subindo justamente no dia em que o papel (CBOT farelo) caiu -0,94% — uma
divergência física-papel que pode refletir um evento de demanda pontual
local (ex.: uma originação específica, uma correção de atraso de
atualização) mais do que uma mudança de tendência ampla; sem mais dados,
não é possível distinguir as duas hipóteses. O prêmio de exportação em
Paranaguá segue zerado em +0,05 USD/short ton, agora **28 dias corridos sem
variação** desde 03/07/2026 — o pilar mais persistente e, nesta leitura,
ainda o mais importante da tese estrutural: o mercado internacional segue
simplesmente não pagando o suficiente para tirar farelo do Brasil.

**O Índice de Sobra de Farelo (ISF) permanece em 80/100 (4 de 5 condições
estruturais), com print de 31/07/2026** — inalterado desde pelo menos
01/07/2026. **A trajetória ABIOVE** (sem alteração nesta janela) segue
mostrando a exportação de farelo brasileiro projetada caindo de 1.400 mil
toneladas em agosto/2026 para 700 mil toneladas em dezembro/2026 (-50% em
quatro meses), com produção caindo bem menos (2.285,06 → 1.659,04 mil
toneladas, -27,4%) — o excedente estrutural segue intacto e continua sendo,
nesta leitura, um pilar bem mais sólido para uma eventual tese bear-farelo
do que o ratio tático, que segue, pela sexta sessão, sem confirmar um
fechamento robusto abaixo de 80%.

### O que invalida / risco para o farelo

- **O ratio Far/Soj precisa fechar de forma robusta e repetida abaixo de
  80% para validar qualquer tese tática bear** — com o D+7 formalmente
  vencido sem confirmação, esta leitura recomenda tratar o próximo teste do
  piso com o mesmo ceticismo das últimas seis sessões, aguardando 2-3
  fechamentos consecutivos do mesmo lado antes de calibrar convicção tática.
- **A posição comprada reforçada pelo COT de 28/07 (net long em 14,11% do
  OI) se desmontar de forma desordenada** se o farelo continuar caindo —
  mesmo com o aumento vindo mais de cobertura de vendidos do que de compra
  nova, a fatia comprada nesta janela específica já está com prejuízo desde
  o corte.
- **A crush margin, se voltar a subir com força**, pode incentivar a
  esmagadora a acelerar o ritmo de esmagamento — aumentando a oferta física
  de farelo e reforçando a tese estrutural ABIOVE/ISF de excedente.
- **O salto isolado de Rondonópolis (+3,03%) se confirmar como tendência**
  em outras praças nas próximas sessões — mudaria a leitura de "excedente
  estrutural" para uma possível reprecificação física localizada.
- **O prêmio de exportação em Paranaguá sair de zero** depois de 28 dias
  parado — o pilar mais persistente da tese estrutural, mas também o que,
  se quebrar, mais mudaria o quadro.

### Leitura operacional — farelo

Depois de seis sessões seguidas sem confirmação robusta do rompimento
tático — e com o D+7 da tese original agora formalmente vencido sem
resolução —, esta leitura mantém o farelo como **neutro tático dentro de
uma tese estrutural bear ainda válida, mas dependente de um gatilho de
preço que segue sem se confirmar.** Para quem monta posições com base no
ratio Far/Soj isolado, a recomendação é a mesma das últimas leituras: este
indicador específico está exigindo uma margem de segurança maior que o
normal antes de qualquer entrada tática — o padrão de "quase romper, voltar"
já dura mais de um mês. Para quem opera o oil-meal spread, a compressão pela
quinta sessão seguida (-3,18% hoje, mecanicamente explicada pelo peso maior
do óleo em dólares por bushel mesmo com queda percentual comparável) segue
sendo a expressão mais limpa da força relativa do farelo dentro do valor do
crush — capturar farelo contra óleo continua sendo, nesta leitura, mais
robusto do que capturar farelo contra soja isoladamente. Para quem opera o
book de posicionamento, o COT de hoje adiciona uma camada nova: o
"crowd" comprado em farelo cresceu na semana anterior à queda, majoritariamente
via cobertura de vendidos — um book mais leve de novos compradores
convictos do que em soja, mas ainda exposto ao mesmo risco direcional se a
fraqueza persistir.

---

## Óleo

**Viés: bear, com a quebra técnica se aprofundando pela quinta sessão
seguida — o óleo fechou em 67,47 cts/lb (-1,10% sobre o fechamento revisado
de ontem de 68,22), agora 6,29% abaixo do suporte de 72,00 (ante -5,25%
ontem, usando o valor revisado de 68,22) — a distância mais profunda desta
janela observada.** Trata `alerta-quebra_suporte-oleo_cbot-2026-07-31`
(quinta confirmação consecutiva do rompimento, a mais funda até agora) e o
COT novo `release-cftc_cot-2026-07-28`, que mostra um padrão de
posicionamento distinto e, para esta tese, favorável.

### O que sustenta a tese

**A sessão de hoje foi de fechamento no terço inferior do range, dando
sequência ao padrão fraco das últimas sessões, com uma nova mínima da
janela.** Abertura 68,22 (0,00% sobre o fechamento de ontem, sem gap),
máxima 68,23 (tocada cedo, praticamente na abertura, sem qualquer tentativa
de alta real), mínima 66,66 (um novo patamar mínimo desta janela) e
fechamento em 67,47 — **51,6% do range** ((67,47-66,66)÷(68,23-66,66)),
tecnicamente um pouco acima do meio, mas o dado mais relevante é que a
sessão sequer testou o lado de cima: a máxima de 68,23 ficou a apenas 0,01
cts da abertura, um dia de venda direta sem qualquer tentativa de repique.
O volume foi de 65.946 contratos, o maior das três pernas do complexo hoje e
consistente com convicção vendedora, não apenas ausência de compradores.

**A margem de biodiesel americana subiu ligeiramente hoje, mas a partir de
uma base já muito reduzida pelo colapso de ontem — uma recuperação parcial,
não uma reversão de tendência.** Custo do óleo: 5,0603 USD/galão (7,5 lb ×
67,47 cts/lb), ante 5,1165 no valor revisado de ontem (-1,10%, seguindo a
queda do preço do óleo). Receita: 7,3586 USD/galão (heating oil 4,1936 +
1,5×RIN D4 2,11), ante 7,3744 no valor revisado de ontem (-0,21%). Margem:
**1,4984 USD/galão**, ante 1,4579 no valor revisado de ontem (**+2,78%**).
**Mecanismo:** o custo do óleo caiu -1,10% (mais rápido que a receita, que
caiu apenas -0,21%), e essa diferença é o que abriu espaço para a margem
melhorar — não uma alta do heating oil (que na verdade caiu -0,38%, de
4,2094 para 4,1936), mas simplesmente o óleo ficando mais barato como
insumo mais rápido do que a receita do biodiesel caiu. Em termos absolutos,
a margem de hoje (1,4984) está de volta próxima ao nível de 29/07 (1,5856
revisado) e acima da margem de 30/07 (1,4579) — uma recuperação de parte da
grande queda de -13,30% registrada ontem, mas ainda longe de indicar um
novo regime de margem sustentavelmente mais alta. **Para a tese do óleo,
isto é um contraponto fundamentalista modesto**: a demanda de biodiesel via
margem não está se deteriorando adicionalmente hoje — mas a melhora vem do
lado errado (óleo mais barato como insumo), não de uma receita mais forte,
então não é, por si só, um argumento para comprar óleo.

**O heating oil (HO=F) trouxe hoje o volume mais "normal" desta janela
observada — um contraste forte com a sequência de prints anômalos das
últimas sessões, mas que esta leitura ainda trata com cautela dado o
histórico recente de revisões.** O volume de hoje veio em **38.271
contratos** — uma ordem de grandeza inteiramente diferente dos prints ao
vivo recentes (278, 788, 70, 34 contratos nas últimas quatro sessões,
segundo a documentação das leituras anteriores) e mais próxima da faixa dos
valores JÁ REVISADOS dessas mesmas sessões (20.424 e 23.447 contratos).
**Esta leitura não sabe, a partir dos dados disponíveis hoje, se isso
significa que o mecanismo de reporte finalmente normalizou ou se o print de
hoje também será revisado (para cima ou para baixo) no próximo dump** — dado
o padrão de revisões de até ~292 vezes documentado ontem, a cautela
recomendada nas últimas quatro leituras permanece válida também para o
número de hoje, ainda que ele pareça, à primeira vista, mais plausível. O
fechamento de heating oil hoje foi de 4,1936 USD/galão, queda de -0,38%
sobre o valor revisado de ontem (4,2094) — um movimento pequeno e, pela
primeira vez em várias sessões, sem qualquer sinal já visível de revisão
material.

**O Índice de Suporte do Óleo (ISO) permanece em 100/100 (5 de 5
condições), com print de 31/07/2026** — a tese estrutural (óleo dominando o
valor do crush) segue formalmente intacta, sem nenhuma alteração apesar da
quinta sessão seguida de quebra técnica do preço. **O oil share caiu para
51,75%** (ante 51,79% no valor revisado de ontem, -0,04 ponto percentual) —
a sexta sessão seguida de queda, mas no ritmo mais lento desta sequência
(52,52% em 27/07 → 52,19% em 28/07 → 51,92% em 29/07 → 51,79% em 30/07 →
**51,75%** hoje). A distância entre a leitura tática (oil share em queda
lenta, mas persistente) e a estrutural (ISO travado em 100) segue crescendo,
sem ainda um gatilho formal de revisão do índice.

**O COT de 28/07/2026 (CFTC, novo) mostra, para o óleo, um padrão
diametralmente oposto ao de soja e farelo — e, nesta leitura, o dado mais
importante para calibrar o risco remanescente da tese bear.** O managed
money net long em óleo **caiu** de +120.246 contratos (21/07, 18,17% do OI
de 661.652) para **+107.898 contratos (28/07, 16,60% do OI de 650.041)** —
uma queda de **-10,27%**. O managed money long caiu -8,54% (143.159→130.933)
enquanto o managed money short ficou praticamente estável (+0,53%,
22.913→23.035) — ou seja, a redução do net long veio de fundos vendendo
posições compradas, não de uma onda de venda nova a descoberto. **Mecanismo
e timing:** entre 21/07 e 28/07, o óleo já vinha em plena sequência de
quebra técnica (as três primeiras das cinco sessões documentadas nesta
série de leituras aconteceram justamente nessa janela) — os fundos, ao
contrário do que fizeram em soja e farelo, **já estavam reduzindo exposição
comprada durante a própria queda**, em vez de comprar a fraqueza ou cobrir
vendidos. Desde o fechamento de 28/07 (70,14) até hoje (67,47), o óleo caiu
mais -3,81%. **Esta leitura considera este o dado mais construtivo para a
tese bear-óleo entre os três COTs**: o book especulativo em óleo tem,
proporcionalmente, menos posição comprada "presa" em prejuízo recente do
que soja e farelo — o que reduz (não elimina) o risco de que a próxima
perna de baixa venha justamente de uma liquidação forçada adicional por
parte dos fundos, simplesmente porque já há menos posição comprada para
liquidar. Ainda assim, 16,60% do open interest em net long é um nível
elevado em termos absolutos frente às outras pernas do complexo.

**A curva forward manteve a backwardation, mas com amplitude comprimida
frente às últimas leituras — um sinal de que o aperto físico relativo pode
estar arrefecendo mesmo com o preço caindo.** Agosto/26 (Q26) 66,99 →
Setembro/26 (U26, spot) 67,47 → Outubro/26 (V26) 67,21 → Dezembro/26 (Z26)
67,05 → Janeiro/27 (F27) 66,97 — do spot de setembro a janeiro/27, uma queda
de -0,50 cts/lb (-0,74%), bem menor que os -1,96% (30/07) e -2,27% (29/07)
documentados nas leituras anteriores para o mesmo tipo de comparação.
**Mecanismo e leitura:** o mercado ainda paga um prêmio pela entrega mais
próxima frente à mais distante (backwardation), mas esse prêmio está
encolhendo — o que sugere que a queda de preço de hoje é mais uma história
de fraqueza generalizada do papel (e do desmonte de posição, ver COT acima)
do que de uma nova informação de aperto físico imediato. Isso é
mecanicamente consistente com a leitura de que o ISO (100/100, estrutural)
segue intacto — a estrutura de fundo do mercado físico não mudou — mas o
sinal técnico de curtíssimo prazo (a forma da curva) está, sim, perdendo um
pouco de força.

### O que invalida / risco para o óleo

- **Um fechamento abaixo de 66,66** (mínima de hoje) confirmaria uma sexta
  sessão seguida de fraqueza técnica e reforçaria a leitura de tendência
  estabelecida, não mais de evento pontual.
- **O heating oil (HO=F) precisa de mais uma ou duas sessões de volume
  estável na faixa de hoje (~38 mil contratos) para confirmar que o
  mecanismo de reporte normalizou** — até lá, esta leitura mantém a mesma
  cautela das últimas quatro sessões sobre qualquer leitura de convicção
  baseada nesse instrumento.
- **A isenção PIS/Cofins do biodiesel expirar hoje (31/07) sem renovação**
  (ver Lente fiscal) — o catalisador fiscal mais concreto e mais imediato
  de toda esta leitura, sem qualquer sinal de resolução nos dados
  disponíveis.
- **O oil share continuar caindo** por mais sessões, mesmo que em ritmo
  lento — reforçaria a leitura de perda estrutural gradual de participação
  do óleo no valor do crush, o indicador tático mais próximo de contradizer
  o ISO 100/100.
- **A backwardation continuar comprimindo até desaparecer** — se a curva
  perder de vez o prêmio de entrega próxima, o argumento de aperto físico
  relativo de curto prazo (hoje já mais fraco que há alguns dias) deixaria
  de sustentar qualquer contraponto altista técnico ao movimento de preço.
- **MPOB seguir inacessível** (agora ~22º dia consecutivo) — mantém cego o
  efeito de eventuais movimentos no prêmio de substituição via palma.

### Leitura operacional — óleo

O óleo segue sendo, nesta leitura, a perna com o quadro bear mais completo
das três — quinta sessão seguida de quebra do suporte de 72,00, a mais
funda até agora, um dia de venda direta sem tentativa de repique, e agora
reforçada por um dado de posicionamento que mostra os fundos já reduzindo
exposição comprada mesmo antes da queda recente se completar. Para quem
está comprado direcional, a combinação de quinta quebra consecutiva + COT
mostrando fundos já vendendo (não comprando a fraqueza) + vencimento da
isenção fiscal hoje sem sinal de renovação é um conjunto de sinais
concordantes, raro nesta série de leituras, para reduzir exposição ou
apertar o stop para a mínima de hoje (66,66). Para quem opera vendido ou
tático short, a mínima de hoje é a referência de entrada mais recente, com
stop acima da máxima do dia (68,23) — um stop relativamente apertado dado
que a sessão sequer testou o lado de cima. A vantagem adicional desta
leitura frente às anteriores é que o risco de "short squeeze" por
liquidação forçada de comprados parece, pelo COT, proporcionalmente menor
em óleo do que em soja/farelo — o que reduz um pouco o risco de uma reversão
técnica abrupta motivada por cobertura de posição vendida por parte de quem
já está comprado. Para quem opera o crush ou o oil-meal spread, a
compressão pela quinta sessão seguida (ver Farelo) segue sendo a expressão
mais limpa da tensão entre as duas pernas de saída do esmagamento —
favorável ao lado "farelo relativamente mais forte / óleo mais fraco", com
o oil share (ainda em queda, ainda que mais lenta) reforçando a mesma
leitura de forma independente.

---

## Spreads e crush — leitura de complexo

### Ratio Far/Soj: 80,55% — sexta sessão testando o piso de 80%, D+7 da tese formalmente vencido

O ratio recuou de 81,25% (revisado, 30/07) para **80,55%** hoje, voltando a
se aproximar do piso depois de duas sessões de afastamento. Olhando a série
completa disponível nesta janela (27/07: 80,09% → 28/07: 80,01% revisado →
29/07: 81,10% revisado → 30/07: 81,25% revisado → **31/07: 80,55%**), o
indicador nunca fechou de forma inequívoca abaixo de 80% em nenhuma das seis
sessões, apesar de ter chegado extremamente perto em três delas. A fila de
hoje sinaliza `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
como **revisão vencida** — o checkpoint formal de 18/06/2026 já passou há 43
dias sem que o gatilho tático (<80% sustentado) se confirmasse. Esta leitura
trata esse gatilho específico como não confirmado nesta janela, sem
prejuízo da tese estrutural mais lenta (ABIOVE/ISF), que segue intacta e
independente. O checkpoint D+90 (2026-09-09) permanece como o próximo marco
formal de revisão da tese completa.

### Crush margin: 2,6282 USD/bu — maior queda diária desta janela (-5,01%)

Recuou -5,01% no dia (2,7667 → 2,6282, valores revisados/atuais), a maior
variação diária de crush margin registrada nesta série de leituras recentes.
O mecanismo foi a receita do crush (farelo+óleo) caindo dez vezes mais
rápido (-0,97%) do que o custo (soja, -0,09%) — um desequilíbrio marcado
entre as pernas, diferente da estabilidade relativa observada em 30/07. A
crush segue folgada em termos absolutos, distante do nível de alerta
histórico citado em leituras passadas (<2,50 USD/bu), mas a folga hoje
diminuiu de forma mais visível do que em qualquer sessão recente.

### Oil share: 51,75% — sexta queda seguida, ritmo mais lento

Caiu -0,04 ponto percentual (51,79% → 51,75%, valores revisados/atuais), o
menor movimento diário desta sequência de seis quedas consecutivas desde
que o indicador saiu da faixa estreita de 53,0-53,5% em que oscilou até
22/07. A direção persistente segue sendo o padrão mais consistente desta
janela para qualquer indicador do crush, mesmo com o ritmo diário
desacelerando. Ainda não é uma ruptura estrutural (o ISO permanece 100/100).

### Oil-meal spread: 0,5027 USD/bu — quinta compressão seguida

Caiu -3,18% no dia (0,5192 → 0,5027, valores revisados/atuais), a quinta
sessão seguida de compressão nesta métrica. O mecanismo de hoje é sutil: em
pontos absolutos de USD/bushel, o óleo carrega um peso bem maior que o
farelo (conversão de 45 lb/bu vs 2.000 lb/short ton), então mesmo com o
óleo caindo percentualmente um pouco mais que o farelo hoje, o spread ainda
comprime porque o óleo domina o cálculo em termos de dólares por bushel — a
mesma mecânica que sustenta a leitura "farelo relativamente forte / óleo
fraco" dentro do valor do crush.

### Margem de biodiesel: 1,4984 USD/gal — recupera parte da queda de ontem, mas a partir do lado errado

Subiu +2,78% no dia (1,4579 → 1,4984, valores revisados/atuais). Ao
contrário do colapso de ontem (mecanismo: heating oil), a melhora de hoje
vem do custo do óleo caindo mais rápido (-1,10%) do que a receita
(-0,21%) — óleo mais barato como insumo, não uma receita de biodiesel mais
forte. Em termos absolutos, a margem de hoje está de volta próxima aos
níveis de 29/07 (1,5856 revisado), uma recuperação parcial que não muda o
quadro de fundo.

### COT: corte de 28/07 chegou hoje (trata `release-cftc_cot-2026-07-28`) — a divergência mais informativa desta leitura

O corte anterior (21/07) mostrava fundos extremamente comprados nas três
pernas. O corte novo de 28/07 revela uma **divergência marcante entre
pernas**: em soja e farelo, os fundos **aumentaram** o net long (+22,97% e
+19,35%, respectivamente) via cobertura de vendidos mais compra nova,
elevando a fração do open interest para 15,73% (soja) e 14,11% (farelo) —
os níveis mais altos desta janela — bem no momento em que o preço ainda
estava perto do topo recente (soja fechou 28/07 em 1.204,75; farelo em
321,30). Desde então, até hoje, soja caiu -2,78% e farelo caiu -2,12%,
deixando parte dessa posição comprada reforçada com prejuízo de papel. Em
óleo, o padrão foi oposto: os fundos **reduziram** o net long em -10,27%
(via venda de posição comprada, não short novo), para 16,60% do OI — uma
redução que aconteceu **durante** a própria sequência de quebra técnica já
em curso, não depois dela. Desde 28/07, o óleo caiu mais -3,81%. **Leitura
conjunta:** o book especulativo está, hoje, mais pesado e mais vulnerável a
uma liquidação forçada em soja e farelo do que em óleo — um dado que muda a
calibração de risco desta leitura em relação às leituras anteriores, que
tratavam as três pernas como igualmente "esticadas" com base no corte de
21/07.

### ISF em 80/100, ISO em 100/100 — ambos inalterados, prints de 31/07

Os dois índices sintéticos, que captam condições estruturais (não a
mecânica tática de preço intradiário), permanecem exatamente nos mesmos
níveis desde pelo menos 01/07/2026. Eles não se moveram apesar da quinta
quebra seguida do óleo, da maior queda diária de crush desta janela e da
revelação do novo COT — coerente com sua natureza estrutural, que não reage
a posicionamento especulativo ou a movimentos técnicos de curto prazo.

### O que os índices dizem juntos em 31/07/2026

ISF 80/100 + ISO 100/100 (ambos inalterados) + ratio Far/Soj de volta perto
do piso pela sexta sessão, com o D+7 da tese tática formalmente vencido sem
confirmação (80,55%) + crush margin na maior queda diária desta janela
(-5,01%, para 2,6282) + oil share na sexta queda seguida, agora em ritmo
mais lento (51,75%) + oil-meal spread na quinta compressão seguida (-3,18%)
+ margem de biodiesel recuperando parcialmente a partir do lado do custo,
não da receita (+2,78%, para 1,4984) + o COT novo de 28/07 revelando uma
divergência de posicionamento entre pernas (soja/farelo mais comprados e
mais vulneráveis; óleo já reduzindo exposição) formam, juntos, um quadro de
**deterioração ampla do valor do crush, liderada pelas duas pernas de
saída (farelo e óleo), com a soja tecnicamente indecisa e um book
especulativo que ficou mais desequilibrado exatamente no momento errado
para quem está comprado em soja e farelo.** O óleo segue como a perna
tecnicamente mais fraca em preço absoluto, mas — pela primeira vez nesta
série de leituras — também a que carrega, proporcionalmente, o
posicionamento especulativo comprado mais "aliviado" das três, o que reduz
(sem eliminar) o risco de uma reversão técnica por cobertura forçada de
vendidos.

---

## Lente fiscal e regulatória BR

**Isenção PIS/Cofins biodiesel — vence HOJE, 31/07/2026, sem qualquer
sinalização pública de renovação nos dados disponíveis neste briefing**
(evento PISCOFINS-BIODIESEL-ISENCAO, `atualizado_em` 2026-06-05, sem
mudança desde então — agora **56 dias sem atualização** do monitor, e o dia
exato do vencimento chegou sem resolução visível). Trata
`trib-PISCOFINS-BIODIESEL-ISENCAO-2026-07-31`, sinalizado pela fila de hoje
com a tag `[0d]` — o vetor tributário de maior prioridade de monitoramento
chega ao seu prazo final nesta própria sessão. **O mecanismo:** a isenção
incide na saída do biodiesel; se expirar sem renovação, o custo tributário
efetivo da produção sobe, o que tende a reduzir a margem de biodiesel
doméstica (distinta da margem americana calculada nesta leitura, que hoje
subiu +2,78% por um mecanismo de custo do óleo, não do regime tributário
brasileiro) e, por extensão, pressionar a demanda por óleo de soja como
insumo dentro do mix B15 mandatório — um vetor bearish direto para o óleo
doméstico, independente do que aconteça no CBOT ou na margem americana.
**Esta leitura não tem, a partir dos dados disponíveis (nem no monitor
tributário, nem nas manchetes do dia, que hoje trataram de armazenamento
agrícola americano, sem qualquer menção a biodiesel ou tributação
brasileira), como determinar se uma prorrogação já foi publicada hoje ou
se a isenção efetivamente expirou sem renovação** — o silêncio informacional
no dia exato do vencimento, após 56 dias sem atualização do monitor, é
tratado aqui como neutro-a-levemente-bearish por omissão, e como o item de
maior prioridade de verificação manual fora deste briefing antes da próxima
leitura.

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L) —
vigência formal venceu há 20 dias (`vigencia_ate` 11/07/2026), sem qualquer
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
de palma, mas inverificável pelo lado de mercado (MPOB inacessível há ~22
dias, ver Honestidade).

**O monitor tributário como um todo está há 56 dias sem qualquer
atualização** — o intervalo se mantém exatamente no dia do vencimento da
isenção PIS/Cofins. Prioridade máxima de manutenção do sistema,
independentemente da leitura de preço de hoje.

---

## Riscos e eventos próximos

**A isenção PIS/Cofins do biodiesel vence hoje, 31/07/2026**, sem
sinalização de renovação — item de verificação manual mais urgente fora
deste briefing antes da próxima leitura, e o catalisador fiscal mais
concreto de toda esta janela.

**O COT de 28/07/2026 chegou hoje e revelou uma divergência de
posicionamento relevante entre pernas** (soja e farelo mais comprados e mais
vulneráveis a liquidação forçada; óleo já reduzindo exposição) — o próximo
corte (referente a 04/08/2026, publicação normal ~07/08/2026) é o dado mais
aguardado para ver se essa divergência se resolve por desmonte em soja/farelo,
por recuperação de preço, ou por ambos.

**O ratio Far/Soj está na sexta sessão testando o piso de 80% sem
confirmação, com o D+7 da tese original formalmente vencido** — esta
leitura recomenda manter o mesmo ceticismo das últimas leituras sobre
qualquer fechamento pontual perto do piso, e monitorar o D+90 (2026-09-09)
como próximo marco formal.

**O nível de 1.180,00 na soja segue sem ser sequer testado por cima hoje**
(máxima de 1.179,25, a primeira em três sessões que não toca o nível) — uma
confirmação técnica adicional, ainda que sutil, de que o nível está se
consolidando como resistência; um fechamento sustentado acima dele
desfaria a leitura.

**O heating oil (HO=F) trouxe hoje o volume mais "normal" desta janela
(38.271 contratos)** depois de quatro sessões de prints anômalos — ainda
não é possível confirmar se o mecanismo de reporte normalizou ou se este
número também será revisado; mais uma ou duas sessões de volume estável
seriam necessárias para dar confiança a essa leitura.

**NOPA — fila `release-nopa-2026-07-31` sinaliza um novo "release", mas o
dado segue inacessível** (`monthly_status` em 0,0 bool, mesma barreira de
assinatura paga documentada desde meados de junho) — sem crush americano
confirmado por fonte primária, agora há quase sete semanas.

**MPOB — sem números de palma extraídos há aproximadamente 22 dias
consecutivos**, mantendo cego o efeito do El Niño e dos vetores regulatórios
indonésios sobre o prêmio de substituição do óleo de soja.

**O WASDE segue fora da janela deste briefing**, agora **21 dias de
atraso** desde o último dado (10/07/2026) — nenhuma pergunta de tese que
dependa do WASDE pode ser respondida a partir deste briefing.

---

## Honestidade

O que não foi possível validar neste briefing de 31/07/2026, e os pontos
onde a confiança é baixa ou há lacunas relevantes:

**1. A janela de OHLCV completo (`cme_cbot`) e a janela de indicadores
sintéticos (`indicators`) estão, nesta consulta, limitadas a apenas 2 e 5
dias, respectivamente — bem mais curtas do que os "últimos 14 dias" que o
cabeçalho do briefing anuncia.** A tabela `cme_cbot` trouxe OHLCV completo
apenas para 30/07 e 31/07; a seção `indicators` trouxe a série derivada
(crush, ratio, oil share etc.) apenas de 27/07 a 31/07. Isso significa que
esta leitura não pôde, por exemplo, obter o preço de fechamento exato da
soja/farelo/óleo em 21/07/2026 (data do corte anterior do COT) diretamente
deste briefing — a comparação de contexto de preço para o COT usou, em vez
disso, o fechamento de 28/07 (dentro da janela disponível) como ponto de
referência, uma escolha metodológica válida mas que não permite descrever
o movimento de preço completo entre 21/07 e 28/07 com a mesma precisão das
leituras anteriores que tiveram acesso a essas datas.

**2. O heating oil (HO=F) trouxe hoje um volume (38.271 contratos) muito
mais alto e "plausível" que os prints ao vivo das últimas quatro sessões
(278, 788, 70, 34) — mas dado o histórico de revisões de até ~292 vezes
documentado na leitura de ontem, esta análise não pode afirmar com
confiança que o mecanismo de reporte normalizou; o número de hoje também
pode ser revisado no próximo dump, para cima ou para baixo.**

**3. Múltiplos valores usados na leitura de 30/07/2026 foram revisados no
dump de hoje** — o fechamento de óleo de 30/07 (reportado ontem como 68,27)
aparece hoje como 68,22; o farelo de 30/07 permaneceu em 317,50 (sem
revisão desta vez); a soja de 30/07 (reportada ontem como 1.171,75) aparece
hoje como 1.172,25. Consequentemente, a crush margin de 30/07 (reportada
ontem como 2,7772) recalcula hoje para 2,7667; o ratio Far/Soj (reportado
como 81,29%) recalcula para 81,25%; o oil-meal spread (reportado como
0,5247) recalcula para 0,5192; o oil share (reportado como 51,81%) recalcula
para 51,79%. Nenhuma dessas revisões muda a direção qualitativa das
conclusões de ontem, mas confirmam, mais uma vez, que o fechamento mais
recente de qualquer dump deve ser tratado como preliminar.

**4. O prêmio de exportação em Paranaguá comprimiu ligeiramente hoje
(+10,80%→+10,53% sobre a paridade teórica) depois de várias sessões de
alargamento — esta leitura não tem como determinar, com um único ponto de
dado, se isso é o início de uma convergência física-papel ou apenas ruído
dentro da mesma tendência de alargamento.**

**5. O salto físico de farelo em Rondonópolis/MT (+3,03% no dia, para R$
1.700,00/ton) é um único ponto de dado numa única praça** — esta leitura
não tem como distinguir entre um evento de demanda local pontual e o início
de uma reprecificação física mais ampla, e não encontrou nenhuma notícia no
RSS do dia que explicasse o movimento.

**6. A manchete do dia (Farm Progress, 31/07/2026) é sobre armazenamento
pós-colheita de milho e soja nos EUA, sem qualquer conteúdo de preço ou
oferta agregada** — não há sinal editorial adicional para incorporar a esta
leitura.

**7. O USDA Crop Progress permanece no corte de 26/07/2026 (11%/52%/7%),
sem atualização nova nesta janela** — dentro da cadência semanal normal
(5 dias desde o último corte); o próximo corte é o dado a acompanhar.

**8. O WASDE permanece completamente fora da janela deste briefing** —
agora 21 dias de atraso desde o último dado (10/07/2026). Nenhuma pergunta
de tese que dependa do WASDE pode ser respondida a partir deste briefing.

**9. NOPA (fila `release-nopa-2026-07-31`) segue com `monthly_status` em
0,0 bool** — mesma barreira de assinatura paga documentada desde meados de
junho, agora com quase sete semanas sem alternativa de dado primário sobre
o esmagamento americano, apesar de a fila ter sinalizado um novo "release"
(que, neste caso, aparenta ser apenas uma atualização de data de coleta,
não de conteúdo).

**10. Palma malaia (MPOB) segue sem números extraídos**, com o mesmo
conteúdo exato de 3.439 caracteres documentado nas leituras anteriores —
consistente com uma página que possivelmente não está mais sendo servida
com conteúdo atualizado.

**11. O COT (CFTC) de 28/07/2026 é o dado mais novo, mas ainda cobre
apenas até uma terça-feira — não captura nenhuma das últimas três sessões
(29/07, 30/07, 31/07), que já mostraram parte da fraqueza de preço discutida
nesta leitura.** A leitura de posicionamento feita aqui é, portanto, uma
fotografia de uma semana atrás, usada para inferir risco de liquidação
futura — não uma confirmação de que a liquidação já está em curso.

**12. Percentis históricos de COT não calculados** — os números de
28/07/2026 seguem lidos apenas em nível absoluto e como fração do open
interest corrente, sem série histórica completa para calibrar se o novo
nível de net long (15,73% em soja, o mais alto desta janela) é
objetivamente extremo no sentido histórico de vários anos, ou apenas alto
dentro da janela recente observada por esta série de leituras.

**13. Clima INMET (BR) não foi usado como driver de preço desta leitura.**
Julho/agosto é entressafra da soja brasileira (colheita concluída, plantio
só em outubro) — sem relevância direta para a tese de preço neste momento
do calendário agrícola.

**14. BCBA Argentina — segunda sessão seguida acessível (30/07 e 31/07),
mas ainda sem relatórios de esmagamento/exportação extraíveis via
scraper** — o hiato de acesso foi resolvido, mas o conteúdo permanece
inacessível.

**15. RIN D4 como parâmetro fixo (2,11 USD/RIN) segue sendo uma fonte
relevante de incerteza do modelo de biodiesel** — a melhora de margem de
hoje (+2,78%) depende inteiramente do custo do óleo caindo mais rápido que
a receita, não de qualquer mudança no RIN em si.

**16. Os forecasts estatísticos internos (31/07/2026) mantiveram o rótulo
"altista" para as três commodities** — esta leitura não usa esses forecasts
como argumento de tese, apenas como referência de banda estatística; eles
não incorporam nem o padrão de máximas decrescentes da soja nem a
divergência de posicionamento revelada pelo COT novo.

*Nenhum número foi inventado ou estimado além do que consta no briefing de
31/07/2026 e nos insights anteriores referenciados. A contribuição central
desta leitura foi (1) identificar, a partir do COT de 28/07/2026 (divulgado
hoje pela primeira vez), uma divergência relevante de posicionamento entre
pernas — fundos aumentando net long em soja (+22,97%) e farelo (+19,35%) via
cobertura de vendidos justamente na semana anterior à queda de preço,
enquanto reduziam (-10,27%) o net long em óleo durante a própria quebra
técnica já em curso — e tratar essa divergência como o principal fator de
calibração de risco direcional desta janela; (2) documentar que o D+7 da
tese estrutural do ratio Far/Soj (aberta em 11/06/2026, checkpoint
18/06/2026) está formalmente vencido há 43 dias sem que o gatilho tático de
preço (<80% sustentado) se confirmasse, sem prejuízo da tese estrutural mais
lenta baseada em ABIOVE/ISF; (3) registrar a máxima decrescente da soja em
torno do nível de 1.180,00 (1.181,25→1.179,25) como uma confirmação técnica
adicional, ainda que sutil, da resistência que está se formando; (4)
decompor o mecanismo da maior queda diária de crush margin desta janela
(-5,01%), atribuindo-a à receita do crush caindo dez vezes mais rápido que
o custo; e (5) registrar a coincidência exata entre o vencimento da isenção
PIS/Cofins do biodiesel e o dia de hoje, sem qualquer sinal de resolução
disponível nos dados consultados.*
