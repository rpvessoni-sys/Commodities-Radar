---
data: 2026-07-09
titulo: "Ratio Far/Soj estabiliza em 78,62% (quarto fechamento seguido <80%, mas +0,10 p.p. frente à revisão de ontem) no mesmo dia em que a soja tem seu primeiro fechamento negativo do rali (-0,61%, ainda acima de 1.180) e o óleo aperta a segunda alta seguida rumo à resistência 72,00 (a 1,4% dela, a menor distância da série) — véspera do WASDE de julho e a dois dias do vencimento da MP 1.358"
tags: [complexo, auto-claude]
fontes:
  - CBOT CME (ZSQ26/ZMQ26/ZLQ26 + curva forward completa + HO=F) — sessão de 2026-07-09
  - BCB PTAX — último dado publicado 2026-07-08 (USD/BRL 5,1552; EUR/BRL 5,8749; Selic 0,052531% a.a.), usado por T+1 no cálculo de paridade de hoje
  - CEPEA/ESALQ Paranaguá e Paraná interior via NAG — último dado disponível 2026-07-08
  - NAG Físico BR (farelo MT/IMEA, RS, Rondonópolis; prêmios export PGUA farelo/óleo) — 2026-07-08
  - CFTC COT Managed Money — 2026-06-30 (nono dia sem atualização nova, sem captar o rali de 06-09/07)
  - USDA Crop Progress — 2026-07-05 (sem atualização desde a leitura de ontem; próximo relatório semanal ~13/07)
  - NOAA CPC ENSO — 2026-07-09 (El Niño Advisory, sem mudança)
  - ABIOVE projeções mensais — balanços ago-dez/2026 (farelo/óleo/soja), sem alteração
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, ISF/ISO, paridade BR) — 2026-07-09, com recálculo retroativo relevante de 2026-07-08 (ver Honestidade #1 e #2)
  - MPOB — 2026-07-09 (24º dia consecutivo sem números extraídos, desde 16/jun)
  - NOPA — 2026-07-09 (fila `release-nopa-2026-07-09`; monthly_status inacessível)
  - system/tributario_watch.toml — eventos MP-1358-2026, MP-1363-2026, PISCOFINS-BIODIESEL-ISENCAO, STJ-RESP-2165276, B16-CNPE-2026, EPA-RFS-2026-2027, 45Z-CLEAN-FUEL, DANANTARA-INDONESIA (todos `atualizado_em` 2026-06-05, sem mudança de status há 34 dias)
  - Notícias Agrícolas / Farm Progress — 160 itens lidos, 4 mantidos em 2026-07-09 (sem manchete específica destacada no dump para hoje)
  - Forecasts estatísticos internos — 2026-07-09 (recalibrados com o spot de hoje)
  - Cruza com [[2026-07-08_leitura-complexo]], [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]], [[2026-05-26_subvencao-fossil-aperta-biodiesel]], [[2026-05-26_pis-cofins-biodiesel-explica-mercado-fisico-fraco]], [[2026-05-26_b16-bullish-farelo]], [[2026-05-26_curva-forward-cbot-oleo-desacopla]]
status: ativa
vies: [bull-soja, bear-farelo, bear-oleo]
---

## Visão geral

O complexo soja funciona como uma fábrica com uma única matéria-prima (a soja em grão) e
dois produtos de saída fabricados em proporção fixa a cada bushel esmagado: o **farelo** (a
fração proteica, ~78% da massa, vira ração animal) e o **óleo degomado** (a fração de
gordura, ~18-20% da massa, vira óleo de cozinha e biodiesel). Quem decide o ritmo de
esmagamento é a esmagadora, olhando a **crush margin** (o valor de farelo + óleo produzidos
por um bushel, menos o custo daquele bushel de soja) e o **oil share** (a fração desse valor
capturada pelo óleo). Quando o óleo "paga o crush" — como vem acontecendo desde maio, com o
oil share subindo de forma consistente e hoje em 53,32% — a esmagadora tem incentivo a
esmagar a pleno vapor para capturar o valor do óleo, e "deixa sobrar" farelo como
subproduto menos desejado, pressionando seu preço relativo. O **ratio Far/Soj** (preço do
farelo dividido pelo preço da soja, na mesma base) é o termômetro dessa dinâmica: abaixo de
80% o farelo está "abundante" frente à soja (mercado incentivado a rodar o crush e aceitar
farelo mais barato), acima de 87% estaria "apertado" (o oposto).

**Hoje, 09/07/2026, é um dia de consolidação com três desenvolvimentos que merecem leitura
cuidadosa porque, juntos, mudam menos do que parecem à primeira vista.** Primeiro, o ratio
Far/Soj fechou em **78,62%** (indicadores, 09/07/2026) — tecnicamente o quarto fechamento
seguido abaixo de 80% (79,28% em 06/07, 79,46% em 07/07, 78,52% em 08/07 já revisado, 78,62%
hoje), mas a variação frente ao valor mais fresco de ontem é de apenas **+0,10 ponto
percentual**, um movimento lateral, não uma nova perna de compressão. É importante registrar
que o valor de ontem (08/07) mudou de forma material entre a leitura de ontem (79,11%) e o
recálculo de hoje (78,52%) — ver Honestidade #1 — então a comparação "dia a dia" mais
confiável é a que usa os dois números do dump de hoje (78,52% → 78,62%), e essa comparação
diz estabilidade, não confirmação de nova mínima. Segundo, a soja (ZSQ26.CBT) fechou em
**1.186,00 cts/bu**, ainda o quarto fechamento consecutivo acima do nível técnico de
1.180,00 (fila `alerta-quebra_resistencia-soja_cbot-2026-07-09`), mas pela primeira vez desde
o início do rali o fechamento foi **negativo no dia** (-0,61% frente aos 1.193,25 de ontem,
já usando os valores internamente consistentes do dump de hoje) — o rompimento segue de pé,
mas o ímpeto direcional esfriou. Terceiro, o óleo (ZLQ26.CBT) fechou em **71,01 cts/lb**,
ainda abaixo do suporte-virou-resistência 72,00 (fila `alerta-quebra_suporte-oleo_cbot-2026-
07-09`), mas essa é a **segunda alta consecutiva** (+0,23% hoje, depois de +2,16% ontem em
termos revisados) e o fechamento de hoje está a apenas **1,4% do nível de 72,00** — a menor
distância de toda a série desde a quebra do suporte, com a máxima intradiária (71,43)
chegando a 0,79% do nível.

**Leitura de uma linha:** o dia é de pausa tática em todas as três pernas — o ratio Far/Soj
parou de comprimir (estável perto de 78,6%), a soja teve seu primeiro dia vermelho do rali
sem perder o rompimento técnico, e o óleo consolidou a segunda alta seguida, chegando mais
perto do teste da resistência do que em qualquer sessão anterior. Nenhuma das três teses
estruturais (bear-farelo, bull-soja tático, bear-óleo tático) foi invalidada hoje, mas todas
perderam um pouco de ímpeto direcional no mesmo dia em que dois catalisadores relevantes se
aproximam: o WASDE de julho, esperado amanhã ou depois de amanhã (~10/07), e o vencimento da
MP 1.358 em 11/07. Confiança moderada-alta no bear-farelo estrutural (tese ainda intacta, mas
sem nova confirmação de compressão hoje); confiança moderada no bull-soja tático (rompimento
mantido, mas primeira pausa no ímpeto); confiança moderada no bear-óleo tático (tese ainda
válida no nível de preço, porém com a segunda sessão seguida de força relativa positiva,
agora a poucochíssima distância de testar a resistência).

---

## Soja

**Viés: bull tático, mas com a primeira pausa do rali — quarto fechamento consecutivo acima
de 1.180,00, porém primeiro dia de queda desde o rompimento (-0,61%), com o básis físico em
Paranaguá saltando para o maior prêmio da série**

### O que sustenta a tese

A soja de agosto (ZSQ26.CBT) abriu em 1.190,00, fez mínima em 1.185,25, máxima em 1.195,00 e
fechou em **1.186,00 cts/bu** (CBOT CME, 09/07/2026, volume **6.927 contratos**) — tratando
a fila `alerta-quebra_resistencia-soja_cbot-2026-07-09`. Frente ao fechamento de 08/07
(1.193,25 cts/bu, valor usado nos indicadores de crush de ontem e hoje, internamente
consistente), a variação do dia foi de **-7,25 cts (-0,61%)** — o primeiro fechamento
negativo desde que o rompimento de 1.180,00 começou a se consolidar (06/07: 1.184,00; 07/07:
1.193,75; 08/07: 1.193,25; **09/07: 1.186,00**). O ponto central da leitura de hoje é que
esse recuo **não desfaz o rompimento**: 1.186,00 segue **6,00 cts acima** do nível técnico de
1.180,00, mantendo o quarto fechamento seguido acima dele, mas é o primeiro dia em que a
soja não avança, o que pede atenção redobrada ao próximo pregão para saber se o rali ganha
fôlego de novo ou se 1.180,00 vira o novo piso de um range mais lateral. O volume de hoje
(6.927 contratos) é moderadamente inferior ao volume revisado de referência mais recente
disponível (7.558 contratos citados pela leitura de ontem para 08/07, ainda que esse número
específico não seja replicável a partir do dump de hoje — ver Honestidade #2) — uma queda
de participação coerente com um dia de consolidação, não de reversão.

**Sem manchete fresca específica sobre soja no dump de hoje** — a seção de notícias registra
apenas "160 itens lidos, 4 mantidos (soja/farelo/oleo)" em 09/07/2026, sem headline
destacada para o dia. O driver informacional mais recente continua sendo a combinação de
calor nos EUA + vendas para a China (Farm Progress, 06/07) e a manchete de exportação
"China buys soybeans" de 08/07 (Farm Progress, sem detalhamento de volume no dump) — nenhuma
atualização qualitativamente nova hoje.

**O câmbio (BCB PTAX) publicou novo dado para 08/07/2026: USD/BRL 5,1552**, ante 5,1458 em
07/07 — uma **leve reversão da apreciação do real** depois de cinco sessões seguidas de
queda do dólar (5,1950 em 01/jul → 5,1458 em 07/jul), com o dólar subindo +0,18% no último
dado disponível. É um movimento pequeno, mas quebra a sequência: o mecanismo cambial deixa
de reforçar a queda de paridade em reais e passa a ser neutro-a-levemente-positivo para a
paridade, ainda que o efeito dominante continue vindo do CBOT.

**A paridade em reais oficial (indicadores, 09/07/2026) recuou para R$ 134,79/saca60kg**
(CBOT 1.186,00 cts × PTAX 5,1552 BRL/USD, sem básis) — uma queda de -R$ 0,82/saca (-0,60%)
frente aos R$ 135,61 de ontem, movendo-se na mesma direção do CBOT (a leve alta do dólar não
foi suficiente para compensar a queda do grão). **O dado mais forte do dia está de novo no
físico do porto, e desta vez de forma mais acentuada:** a soja Paranaguá (CEPEA/ESALQ via
NAG, 08/07/2026) fechou em **R$ 140,40/saca**, subindo +0,49% frente aos R$ 139,71 de 07/07
— e esse valor está **R$ 5,61/saca ACIMA da paridade teórica** (R$ 134,79), o maior prêmio de
básis de toda a série documentada até aqui, superando os R$ 4,03/saca de ontem em **+39%**.
Esse é o dado mais relevante da leitura de soja hoje: o físico do porto sobe enquanto o CBOT
cai, ampliando de forma expressiva a desconexão entre o "preço justo" teórico e o que o
mercado de exportação paga de fato em Paranaguá — quarta leitura seguida de prêmio físico
crescente, e a mais expressiva delas. A soja Paraná interior (NAG, 08/07/2026) fechou em
**R$ 132,52/saca** (+0,36% frente a 07/07), reduzindo o desconto frente à paridade para -R$
2,27/saca (ante -R$ 3,64 em 07/07) — o interior também converge para cima, mas com menos
intensidade que o porto.

**A colheita argentina segue encerrada em 98%**, produção mantida em 50,1 milhões de
toneladas (Canal Rural, 27/06/2026, sem atualização) — teto estrutural regional inalterado.

**O posicionamento dos fundos (COT, CFTC) segue no dado de 30/06/2026**, agora nono dia
sem atualização e ainda sem captar qualquer parte do rali de 06-09/07: managed money net long
em soja em +38.149 contratos (long 133.396, short 95.247), fração do open interest de
898.681 em 4,25%. Continua sendo o dado mais defasado da leitura — a janela de reação dos
fundos ao rompimento, ao novo topo de ciclo e agora à primeira pausa segue cega.

**A curva forward (09/07/2026)** aprofunda a pequena inversão de curtíssimo prazo:

| Vencimento | Código | Preço (cts/bu) | Var. vs Ago |
|---|---|---|---|
| Julho/26 | N26 | 1.197,00 | +11,00 |
| Agosto/26 | Q26 | 1.186,00 | — (spot) |
| Setembro/26 | U26 | 1.177,00 | −9,00 |
| Novembro/26 | X26 | 1.187,00 | +1,00 |
| Janeiro/27 | F27 | 1.200,50 | +14,50 |
| Março/27 | H27 | 1.203,50 | +17,50 |

O contrato de julho (N26) negocia **+11,00 cts acima** do agosto (Q26), uma inversão maior
que os +3,00 cts de ontem — reforçando a leitura de que se trata de efeito de vencimento
(N26 saindo de cena) e não de um sinal de aperto físico real, já que o resto da curva (Q26 a
H27) mantém contango moderado e coerente (+17,50 cts, +1,5%, praticamente igual aos +16,75
de ontem). O contrato de setembro (U26, 1.177,00) negocia abaixo até do agosto — um "vale"
de meio de curva que provavelmente reflete a proximidade da nova safra americana entrando no
mercado a partir de outubro/novembro, sem indicar problema de oferta.

**Os forecasts estatísticos internos (09/07/2026, recalibrados) recuaram de forma notável
frente a ontem, acompanhando a pausa do dia:** central 7d = **1.200,32 cts/bu** (bandas
1.140,77-1.259,87), viés **altista**, mas o centro caiu frente aos 1.205,29 de ontem — o
modelo reduziu a expectativa de continuidade imediata do rali, coerente com o primeiro dia de
queda. O central 30d = **1.258,92 cts/bu** (bandas 1.135,65-1.382,20), viés **altista**,
ainda subindo frente a 1.250,66 ontem — o horizonte mais longo segue otimista mesmo com a
pausa de curto prazo, sugerindo que o modelo lê o recuo de hoje como ruído de curto prazo
dentro de uma tendência maior, não como reversão.

### O que invalida / risco para a soja

- **Se o próximo pregão confirmar mais um fechamento negativo,** o rompimento de 1.180,00
  passaria de "consolidado com força" para "testando o piso do range" — o gatilho mais
  imediato a observar.
- **WASDE de julho (~10/07/2026) reverter a leitura de "oferta grande":** cai literalmente
  amanhã ou depois de amanhã, na mesma semana do vencimento da MP 1.358 (ver Riscos).
- **A condição de lavoura (64% bom-ou-melhor, 05/07) piorar mais no relatório de ~13/07,**
  ainda sem dado novo desde a leitura de ontem.
- **O prêmio físico em Paranaguá (R$ 5,61/sc sobre a paridade, o maior da série) se dissipar
  de uma hora para outra:** quarta leitura seguida de prêmio crescente reduz a chance de ser
  ruído, mas um salto de +39% em um único dia também pode refletir defasagem de reporte
  (CEPEA de 08/07 vs CBOT de 09/07 já em queda) mais do que um novo patamar de demanda física
  — merece confirmação no próximo dado antes de tratar como estrutural.
- **A pequena inversão N26 > Q26 se aprofundar ainda mais ou se espalhar para o resto da
  curva:** indicaria efeito além do mecânico de vencimento.

### Leitura operacional — soja

O rompimento de 1.180,00 permanece de pé, mas hoje é o primeiro dia em que o teste é de
resistência psicológica da tese, não de continuidade. Para quem opera o papel, a
recomendação é não tratar a queda de -0,61% como sinal de reversão isolado — os forecasts de
7 e 30 dias seguem altistas — mas apertar a régua de observação no próximo pregão: uma
segunda queda seguida mudaria o tom da leitura de "pausa" para "perda de ímpeto". Para quem
tem física para fixar, o básis de Paranaguá bateu o maior prêmio da série (R$ 140,40 vs R$
134,79 de paridade, +R$ 5,61/saca) — mesmo com essa leitura pedindo confirmação (ver acima),
é a melhor janela de venda à vista documentada até aqui, e vale considerar travar parte do
volume físico nesse nível independentemente do que o CBOT fizer nos próximos dias. O
gatilho que decide os próximos dias continua sendo o WASDE de julho, agora imediatamente à
frente.

---

## Farelo

**Viés: bear estrutural, em pausa tática — ratio Far/Soj fechou em 78,62%, tecnicamente o
quarto fechamento seguido abaixo de 80%, mas com variação de apenas +0,10 p.p. frente ao
valor revisado de ontem (78,52%), tratando a fila `revisao-2026-06-11_ratio-81-prepara-
janela-de-tranches-farelo-D+7`, agora bem além do D+7 original e à véspera do WASDE que a
própria fila cobra como confirmação pendente**

### Tratando a fila `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`

A pergunta que a fila cobra, pela terceira vez consecutiva: "ratio fechou <80%? WASDE mudou
o quadro? NOPA confirmou crush?" **Resposta: sim ao primeiro (mais uma vez), mas com um
detalhe importante sobre a magnitude — os outros dois seguem pendentes, com o WASDE agora
literalmente a um ou dois dias de distância.** A trajetória completa do ratio, usando os
valores do dump de hoje (mais consistentes entre si que comparações entre leituras de dias
diferentes — ver Honestidade #1):

| Data-base | Ratio Far/Soj (dump de hoje) | Ratio citado na leitura daquele dia | Evento |
|---|---|---|---|
| 11/jun | 81,4% | 81,4% | origem da tese |
| 06/jul | 79,28% | 79,28% | primeiro fechamento abaixo de 80% |
| 07/jul | 79,46% | 79,46% (recalculado) | segundo fechamento seguido abaixo de 80% |
| 08/jul | **78,52%** | 79,11% (na época) | terceiro fechamento — **revisado para baixo hoje** |
| **09/jul** | **78,62%** | — | quarto fechamento — **estável frente à revisão de ontem** |

O protocolo original de 11/06/2026 (documentado em
[[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]) definia o gatilho como "ratio
sustentado abaixo de 80% por 2-3 pregões consecutivos" — esse critério já foi cumprido há
alguns dias e permanece cumprido hoje, mas o desenvolvimento de HOJE especificamente é de
**estabilização, não de aprofundamento**: o ratio nem comprimiu mais nem reverteu, ficou
essencialmente parado (78,52% → 78,62%, uma variação de +0,10 p.p. que está dentro do ruído
normal de arredondamento diário). **O WASDE ainda não mudou o quadro** (o próximo é
esperado para ~10/07, ou seja, já amanhã ou depois de amanhã — a janela mais apertada de
toda a série até aqui) e **a NOPA segue sem confirmar nada**: a fila de hoje traz mais um
item, `release-nopa-2026-07-09`, sinalizando "release novo" — mas o campo `monthly_status`
continua em **0,0 bool** (indicadores, 09/07/2026), a mesma barreira de membership pago
documentada desde início de junho, agora por 25 dias seguidos.

**A crush margin subiu para 2,7887 USD/bu** (Board Crush: farelo 310,80 + óleo 71,01 − soja
1.186,00; indicadores, 09/07/2026), uma alta de **+2,09%** frente aos 2,7316 recalculados
para 08/07. A série usando os valores mais frescos de hoje: 2,4974 (06/jul) → 2,5638 (07/jul)
→ 2,7316 (08/jul, revisado para cima frente ao 2,6073 citado na leitura de ontem — ver
Honestidade #2) → **2,7887 (09/jul)**, uma alta acumulada de **+11,7%** desde a mínima local
de 06/07. O sinal é de **recuperação sustentada da margem por quatro sessões seguidas**, mais
forte do que a leitura de ontem já havia identificado — reduzindo ainda mais o risco de
"esmagadora reduz ritmo" e reforçando o incentivo a continuar esmagando a pleno vapor, o que
sustenta a oferta de farelo no mercado e é coerente com (não contraria) a tese bearish
estrutural.

**As praças físicas de farelo no Brasil (NAG, 08/07/2026)** mostram o primeiro movimento
relevante em várias sessões: Rondonópolis subiu para **R$ 1.620,00/ton** (+4,52% frente a
07/07, que já tinha subido para R$ 1.550,00), uma alta acumulada de dois dias que quebra a
estabilidade lateral observada desde o início de julho. MT/IMEA segue estável em R$
1.554,53/ton e RS em R$ 1.640,00/ton. O prêmio de exportação do farelo em Paranaguá segue em
**+0,05 USD/sht** (julho/26) — inalterado, confirmando que o Brasil segue sem vantagem de
preço para exportar farelo, mesmo com a firmeza pontual do físico interno em Rondonópolis
(que é mais coerente com demanda regional de ração do que com um sinal de exportação).

**Os dados projetados da ABIOVE (sem alteração desde a leitura anterior)** continuam
mostrando a exportação de farelo brasileiro recuando pela metade entre agosto e
dezembro/2026: 1.400 → 1.100 → 850 → 800 → 700 mil t, sem queda proporcional no estoque
final projetado (1.224 → 1.016 → 1.100 → 1.101 → 1.015 mil t). O mecanismo segue intacto:
menos saída pelo porto empurra o excedente de farelo para o mercado interno de ração,
pressionando o preço doméstico — coerente com o ratio estruturalmente comprimido, mesmo sem
nova compressão hoje.

**A curva forward do farelo (09/07/2026)**:

| Vencimento | Código | Preço (USD/sht) | Var. vs Ago |
|---|---|---|---|
| Julho/26 | N26 | 313,90 | +3,10 |
| Agosto/26 | Q26 | 310,80 | — (spot) |
| Setembro/26 | U26 | 307,90 | −2,90 |
| Outubro/26 | V26 | 305,90 | −4,90 |
| Dezembro/26 | Z26 | 309,30 | −1,50 |
| Janeiro/27 | F27 | 310,80 | 0,00 |

Outubro (V26, 305,90) permanece o vencimento mais descontado — coincide com o pico sazonal
de esmagamento simultâneo Brasil + Argentina (ABIOVE projeta 2.846 mil t de esmagamento BR
em outubro). O contrato de janeiro/27 (F27) iguala exatamente o spot de agosto (310,80) —
curva praticamente achatada de ago/26 a jan/27 fora do vale sazonal de out/26.

**O posicionamento dos fundos (COT, ainda em 30/06/2026, sem atualização nova)** mantém o
quadro já descrito: managed money net long colapsado para +4.740 contratos (long 110.069,
short 105.329, 17,9% do OI de 588.519) — nono dia sem dado fresco para medir a reação dos
fundos ao ratio comprimido.

**O forecast estatístico do farelo (09/07/2026) recuou frente a ontem, na mesma direção da
pausa de preço:** central 7d = **313,69 USD/sht** (bandas 299,74-327,64), viés **altista**,
descendo de 317,54 ontem. Central 30d = **324,56 USD/sht** (bandas 295,68-353,45), viés
**altista**, também descendo de 327,16 ontem. **A tensão identificada nas leituras
anteriores permanece, mas atenuada**: o modelo estatístico ainda projeta alta em ambos os
horizontes, na contramão da tese fundamentalista bearish, mas o tamanho da divergência
diminuiu hoje pela primeira vez em várias sessões — sinal de que o próprio modelo está
lendo a estabilização de preço do dia, não uma reversão da divergência.

### O que invalida / risco para o farelo

- **O forecast de 7d e 30d seguirem altistas (313,69 e 324,56), mesmo que com menor
  intensidade:** a divergência entre modelo estatístico e tese fundamentalista persiste —
  segue sendo o item de maior atenção, ainda que hoje tenha encolhido, não crescido.
- **WASDE de julho (~10/jul, praticamente amanhã) reduzir a área de soja americana de forma
  expressiva:** menos esmagamento no 4T26 → menos farelo global, risco de aperto mesmo com
  os fundos vendidos — o catalisador mais próximo de toda a série.
- **Crush margin em alta por quatro sessões seguidas (+11,7% desde a mínima de 06/07):**
  sustenta a oferta de farelo por ora, mas se continuar subindo pode eventualmente estimular
  esmagamento agressivo o suficiente para gerar volatilidade de outro tipo (efeito ambíguo,
  a monitorar).
- **Alta física em Rondonópolis (+4,52% em 08/07, após +alta em 07/07):** se a firmeza se
  espalhar para MT/IMEA e RS nos próximos dias, seria o primeiro sinal de reversão da
  abundância física — ainda isolado demais para mudar a tese hoje.
- **NOPA seguir inacessível indefinidamente:** o "release novo" da fila de hoje não trouxe
  dado interpretável — a lacuna de confirmação direta de esmagamento americano persiste, 25
  dias seguidos.

### Leitura operacional — farelo

A tese nascida em 11/06/2026 segue confirmada estruturalmente (ratio abaixo de 80% pelo
quarto pregão), mas o desenvolvimento de hoje é de **pausa, não de aprofundamento** — a
variação de +0,10 p.p. frente ao valor revisado de ontem está dentro do ruído. Para quem
opera o spread de convergência (long farelo/short soja, ou o crush completo), a
recomendação é manter a posição estrutural, mas sem tratar o dia de hoje como um novo
gatilho de entrada — o sinal mais forte da série segue sendo a compressão acumulada desde
11/06, não o movimento marginal de hoje. O WASDE de amanhã (ou depois de amanhã) é o
evento que decide se a tese ganha confirmação fundamentalista externa (o item que falta
desde a origem) ou se abre espaço para reprecificação. Referência de stop para posição
vendida em preço absoluto: 314-316 USD/sht (levemente acima da faixa de 316-318 sugerida
ontem, dado que o preço de hoje, 310,80, está mais baixo e a banda alta do forecast de 7d
recuou para 327,64).

---

## Óleo

**Viés: bear tático, cada vez mais pressionado pela força relativa — fechamento de 71,01
cts/lb segue abaixo do suporte-virou-resistência 72,00 (fila `alerta-quebra_suporte-
oleo_cbot-2026-07-09`), mas é a SEGUNDA alta consecutiva do óleo e a menor distância da
resistência de toda a série (1,4%)**

### Tratando a fila `alerta-quebra_suporte-oleo_cbot-2026-07-09`

O óleo de agosto (ZLQ26.CBT) abriu em 70,65, fez máxima de 71,43, mínima de 70,58 e fechou em
**71,01 cts/lb** (CBOT CME, 09/07/2026, volume 7.450 contratos) — uma alta de **+0,23%**
frente ao fechamento de 08/07 (70,85, via indicadores). A pergunta operacional da fila —
confirma ou muda a tese? — **confirma no nível de preço, mas a fissura tática identificada
ontem se aprofunda**: o óleo está agora **apenas 1,39% abaixo** do nível de 72,00 (a menor
distância de toda a série desde a quebra do suporte; a máxima intradiária de hoje, 71,43,
chegou a **0,79%** do nível). É a segunda sessão seguida em que o óleo avança — o primeiro
par de altas consecutivas desde a quebra do suporte — e, embora hoje não tenha liderado a
alta percentual do complexo (a soja e o farelo caíram, então a comparação de "quem subiu
mais" não se aplica da mesma forma que ontem), o óleo foi a única das três pernas a fechar
em alta no dia. Ainda não é um teste da resistência, mas a trajetória das últimas duas
sessões (68,59 → 70,85 → 71,01) deixa a tese bear tática mais próxima de um teste real do
que em qualquer momento desde que o suporte foi rompido.

**A margem de biodiesel americano está em 0,6773 USD/galão** (indicadores, 09/07/2026:
receita 6,8031 = HO 3,6381 + 1,5×RIN 2,11; custo 6,1258 = óleo 5,3258 + industrial 0,80),
uma queda de -4,4% frente aos 0,7088 recalculados para 08/07. **Este número exige uma nota
de honestidade importante:** a leitura de ontem havia classificado a margem de 08/07 como
"colada no piso de 0,50 USD/gal" (citando 0,5177) e tratou isso como o gatilho tático mais
sensível do óleo. O dump de hoje recalcula o mesmo dia (08/07) para **0,7088** — uma
diferença de +37% frente ao valor usado ontem, decorrente de revisão tanto no heating oil
(3,3539 → 3,66) quanto no custo do óleo (5,20 → 5,31) usados no cálculo — ver Honestidade
#1 e #3. **Usando a série mais fresca e internamente consistente de hoje**, a margem está,
na verdade, no meio da faixa de conforto de 0,50-0,80 USD/gal já documentada (0,5814 em
06/07 → 0,5225 em 07/07 → 0,7088 em 08/07 → **0,6773 hoje**), não colada no piso. Isso
significa que o alerta de "piso de margem" da leitura de ontem não se sustenta sob os dados
de hoje — um exemplo direto de como a revisão retroativa dos indicadores pode mudar a
leitura tática de um dia para o outro, e por isso este item é rebaixado de "gatilho mais
sensível" para "acompanhar, sem urgência adicional" nesta leitura.

**A curva forward do óleo (09/07/2026)** mantém backwardation clara:

| Vencimento | Código | Preço (cts/lb) | Var. vs Ago |
|---|---|---|---|
| Agosto/26 | Q26 | 71,01 | — (spot) |
| Setembro/26 | U26 | 70,56 | −0,45 |
| Outubro/26 | V26 | 69,99 | −1,02 |
| Dezembro/26 | Z26 | 69,66 | −1,35 |
| Janeiro/27 | F27 | 69,55 | −1,46 |

A curva caindo -1,46 cts/lb (-2,06%) de agosto a janeiro/27 é praticamente idêntica em
magnitude aos -1,42 cts/lb de ontem — segue sendo o argumento técnico mais forte para manter
posição vendida de médio prazo via carry, mesmo com a segunda alta seguida do spot.

**O posicionamento dos fundos (COT, ainda em 30/06/2026, sem atualização nova)** mantém o
quadro de de-risking já descrito: managed money net long em +91.946 contratos (14,6% do OI),
uma queda de -10,9% frente a 23/06 que antecedeu o rali dos últimos pregões — nono dia sem
dado fresco.

**O Índice de Suporte do Óleo (ISO) permanece em 100/100 (5/5 condições)**, agora a décima
sessão seguida nesse patamar desde a virada de 01/07 (indicadores, 09/07/2026) — mantendo a
hipótese de efeito calendário já discutida em leituras anteriores (ver Honestidade #4).

**O pano de fundo regulatório global segue inalterado desde 05/06/2026**
(`system/tributario_watch.toml`, sem novos `atualizado_em` há 34 dias): EPA Final RFS
2026/2027 sustenta o RIN D4, o crédito 45Z tende a favorecer óleo doméstico americano, e a
Indonésia mantém a exportação de palma centralizada via Danantara mais o levy de exportação
de CPO — mas segue impossível quantificar porque o MPOB está inacessível há 24 dias
consecutivos.

### O que invalida / risco para o óleo

- **O óleo fechar em alta pela terceira sessão seguida amanhã:** se o padrão de força
  relativa se repetir, um teste real da resistência de 72,00 passa a ser o cenário mais
  provável, e não apenas um risco de cauda — a tese bear tática precisaria ser revisada
  formalmente.
- **A margem de biodiesel, mesmo revisada para o meio da faixa (0,6773), segue sendo o canal
  de transmissão entre o custo do óleo e o incentivo a demandar o insumo** — uma queda súbita
  de heating oil (HO=F caiu de 3,7131 na abertura para 3,6381 no fechamento hoje, -1,86% no
  próprio pregão) pode reverter a folga rapidamente.
- **RIN D4 real acima de 2,40 USD/RIN** (o modelo usa 2,11 fixo): incerteza estrutural
  bidirecional, sem novo dado hoje.
- **Dados de palma malaia (MPOB) inacessíveis há 24 dias consecutivos** — segue impossível
  avaliar o efeito de El Niño ou das restrições indonésias sobre o prêmio de substituição.
- **WASDE de julho (amanhã/depois de amanhã) reduzir a área de soja americana:** menos
  esmagamento futuro → menos óleo produzido → altista para os contratos de novembro em
  diante.

### Leitura operacional — óleo

O viés segue bear tático — a quebra do suporte 72,00 permanece confirmada, e o óleo ainda
não testou a resistência. Mas a sequência de duas altas seguidas (68,59 → 70,85 → 71,01),
com a distância ao nível de 72,00 caindo para apenas 1,4% (0,79% na máxima do dia), é o sinal
de força relativa mais forte de toda a série desde a quebra do suporte — mais forte do que
o observado ontem. Para quem está posicionado vendido, este é o momento de reduzir o
tamanho de posições adicionais e apertar o stop, não de ignorar o sinal: referência de stop
em 71,50-72,00 cts/lb (mais apertada que os 70,00-71,00 sugeridos ontem, refletindo a
proximidade real da resistência). A correção do alerta de margem de biodiesel (ver acima)
remove um argumento tático extra de baixa que a leitura de ontem havia usado — sem esse
argumento, o caso bear tático fica mais dependente pura e simplesmente do nível técnico
(72,00 ainda não rompido) e da curva forward em backwardation. Para quem opera o oil share
(hoje em 53,32%, subindo pelo terceiro dia seguido de 51,99% em 06/07), o viés estrutural
continua favorecendo manter exposição ao óleo dentro do crush frente ao farelo.

---

## Spreads e crush — leitura de complexo

### Crush margin: 2,7887 USD/bu — quarta alta seguida, +11,7% desde a mínima de 06/07

A crush está em **2,7887 USD/bu** (Board Crush: farelo 310,80 + óleo 71,01 − soja 1.186,00;
indicadores, 09/07/2026), subindo +2,09% frente aos 2,7316 recalculados para 08/07 — a
quarta alta consecutiva usando os valores mais frescos disponíveis: 2,4974 (06/jul) → 2,5638
(07/jul) → 2,7316 (08/jul) → **2,7887 (09/jul)**, uma recuperação acumulada de **+11,7%** em
quatro sessões desde a mínima local de 06/07. O sinal é de recuperação sustentada da margem
— reduz de forma consistente o risco de a esmagadora reduzir ritmo de esmagamento no curto
prazo, o que sustenta a oferta física de farelo e óleo simultaneamente (reforçando o
bear-farelo estrutural, sem contradizer o bear-óleo tático, ainda que este último esteja sob
pressão crescente da força relativa de preço).

### Ratio Far/Soj: 78,62% — quarto fechamento seguido abaixo de 80%, mas estável frente a ontem

Como detalhado na seção de Farelo, o ratio não aprofundou a compressão hoje — ficou
essencialmente parado frente ao valor revisado de ontem (78,52% → 78,62%, +0,10 p.p.). A
tese estrutural de 11/06 segue confirmada, mas o desenvolvimento de hoje é de estabilização,
não de nova confirmação, tratando a fila
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`.

### Oil share: 53,32% — subindo pelo terceiro dia seguido

O oil share está em 53,32%, subindo de 53,15% ontem e 52,03% em 07/07 (valores do dump de
hoje) — o óleo ampliando de forma consistente sua participação no valor total do crush, o
mecanismo estrutural por trás da força relativa de preço observada no óleo nos últimos dois
pregões.

### Oil-meal spread: 0,9735 USD/bu — quarto avanço seguido

O oil-meal spread (contribuição do óleo menos a do farelo por bushel) subiu para 0,9735 ante
0,9229 recalculados para ontem — um avanço de +5,5%, dando continuidade à trajetória de alta
que já vinha se acelerando (0,57 em 06/07 → 0,59 em 07/07 → 0,92 em 08/07 → 0,97 hoje,
usando a série revisada de hoje). É a mesma força — óleo ganhando valor relativo dentro do
crush — que sustenta tanto o bear-farelo estrutural quanto a fissura tática no bear-óleo.

### ISF em 80/100, ISO em 100/100 — décimo pregão seguido no mesmo patamar

O Índice de Sobra de Farelo (ISF) está em 80/100 (4/5 condições) e o Índice de Suporte do
Óleo (ISO) em 100/100 (5/5) — o mesmo patamar desde 01/07/2026, agora o décimo dia
consecutivo (contando os dias de calendário registrados no dump, incluindo os de mercado
fechado).

### O que os índices dizem juntos em 09/07/2026

ISF 80/100 + ISO 100/100 (ambos estáveis, efeito calendário) + ratio Far/Soj estável no
patamar comprimido (78,62%, quarto fechamento <80% mas sem nova compressão) + oil share
subindo pelo terceiro dia (53,32%) + oil-meal spread subindo pelo quarto dia (+5,5% hoje) +
crush margin em alta pelo quarto dia seguido (+11,7% acumulado) + margem de biodiesel de
volta ao meio da faixa de conforto após revisão (0,6773, não mais colada no piso) + soja com
seu primeiro fechamento negativo do rali, mas mantendo o rompimento de 1.180,00 + farelo
essencialmente estável no ratio + óleo com a segunda alta seguida, a apenas 1,4% da
resistência 72,00:

A leitura de hoje é de **pausa tática generalizada em todas as três pernas, sem
invalidação de nenhuma das teses estruturais.** O desenvolvimento mais importante do dia não
é um novo extremo, mas a convergência de sinais de consolidação: o ratio parou de comprimir,
a soja parou de subir, e o óleo consolidou sua segunda alta seguida. Isso é coerente com um
mercado que aguarda o próximo catalisador fundamental real — o WASDE de julho, esperado para
amanhã ou depois de amanhã, a primeira atualização de oferta/demanda desde que o rali
começou. A régua de gestão de risco deve permanecer alta às vésperas desse evento, dado que
nenhuma das teses táticas (bull-soja, bear-óleo) tem ainda o reforço de um dado
fundamentalista fresco — todas dependem, até aqui, de preço, câmbio, básis físico e
indicadores sintéticos, não de um novo balanço USDA.

---

## Lente fiscal e regulatória BR

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L) — vence em 2 dias
(11/07/2026, fila `trib-MP-1358-2026-2026-07-11`).** Sem mudança desde a última leitura
(`system/tributario_watch.toml`, evento MP-1358-2026, `atualizado_em` 2026-06-05, status
"tramitacao", `proximo_marco` = "Deliberação comissão mista", `proximo_data` = 2026-07-11) —
o monitor tributário está parado há 34 dias sem nenhuma atualização de status, mesmo com
dois vencimentos relevantes se aproximando nesta mesma semana (MP 1.358 em 2 dias, isenção
PIS/Cofins biodiesel em 22 dias). A MP ressarce PIS/Cofins/Cide da gasolina e do diesel,
mantendo o combustível fóssil artificialmente mais barato — o mesmo espírito da MP
1.363/2026 (subsídio de R$ 1,12/L ao diesel, vigente até 31/12/2026, já tratada em
[[2026-05-26_subvencao-fossil-aperta-biodiesel]]). O mecanismo de transmissão para o
complexo soja é indireto mas real: enquanto o combustível fóssil segue subsidiado, a
competitividade relativa do biodiesel dentro do mix B15 mandatório permanece pressionada,
mantendo a margem da indústria de biodiesel (maior consumidora industrial de óleo de soja no
Brasil) mais apertada do que teria sem a subvenção ao concorrente fóssil. Esse marco cai
agora um ou dois dias depois do WASDE de julho — a janela de 09-11/07 concentra dois
catalisadores relevantes em sequência quase simultânea. Se a MP 1.358 caducar sem conversão
em lei, é um sinal (fraco, mas real) de perda de fôlego político do pacote pró-fóssil —
levemente positivo para a competitividade do biodiesel e, por extensão, para a demanda
industrial de óleo de soja; se for convertida, reforça o quadro de pressão já documentado
desde maio.

**Isenção PIS/Cofins biodiesel — vencimento em 31/07/2026, 22 dias.** Sem sinalização
pública de renovação até hoje (`system/tributario_watch.toml`, evento
PISCOFINS-BIODIESEL-ISENCAO, `atualizado_em` 2026-06-05, sem mudança). O checkpoint D+45
desse insight ([[2026-05-26_pis-cofins-biodiesel-explica-mercado-fisico-fraco]]) já passou
(caiu em 09/07/2026, exatamente hoje) sem que o monitor tributário tenha sido atualizado com
nenhuma resposta às perguntas de revisão programada (Congresso votou reversão? Boletim
ABIOVE mostrou queda de esmagamento? Leilão/contratação bilateral ANP trouxe prêmio maior?).
Isso é uma lacuna de acompanhamento que vale registrar: o checkpoint formal do próprio
sistema venceu sem dado novo para respondê-lo — ver Honestidade #5.

**B16 — sem data, travado em B15.** Sem mudança de status (evento B16-CNPE-2026,
`atualizado_em` 2026-06-05, status "adiado", sem `proximo_data`).

**MP 1.363/2026 (subsídio ao diesel fóssil) — em vigor até 31/12/2026.** Sem alteração.
Bearish estrutural persistente para a demanda incremental de óleo de soja no mercado
doméstico brasileiro.

**STJ REsp 2.165.276/2026 — crédito PIS/Cofins para esmagadoras.** Sem alteração. Bullish
para a soja/óleo (alívio de custo de entrada para biodiesel) e, por extensão, incentivo a
mais esmagamento — coerente com mais oferta de co-produtos, reforçando a leitura bearish do
farelo.

**Câmbio (PTAX) publicou novo dado para 08/07/2026 (5,1552 BRL/USD), rompendo a sequência de
cinco sessões de apreciação do real** — já tratado na seção de Soja. O impacto fiscal
indireto (dólar levemente mais forte encarece marginalmente insumos importados da cadeia,
mas também sustenta um pouco mais a paridade de exportação em reais) segue neutro na margem,
sem mudança de regime.

**Pano de fundo regulatório global (EUA e Indonésia) segue dando suporte estrutural ao
óleo, sem contradizer o viés bearish tático** — detalhado na seção Óleo.

---

## Riscos e eventos próximos

**WASDE de julho — ~10/07/2026 (amanhã ou depois de amanhã).** Primeiro WASDE do mês, o
catalisador fundamentalista mais aguardado de toda a série recente, cai a um ou dois dias do
vencimento da MP 1.358 e exatamente no dia do checkpoint D+45 vencido da tese PIS/Cofins —
janela de catalisadores concentrada nos próximos 2-3 dias.

**Vencimento da MP 1.358/2026 — 11/07/2026 (2 dias), fila `trib-MP-1358-2026-2026-07-11`.**
Deliberação da comissão mista é o marco a monitorar.

**Isenção PIS/Cofins biodiesel — vencimento 31/07/2026 (22 dias).** Sem sinalização de
renovação até agora; checkpoint D+45 do insight original venceu hoje sem resposta do
monitor tributário (ver Lente Fiscal e Honestidade #5).

**COT CFTC — dado de 30/06/2026 ainda não captura nenhuma parte do rali de 06-09/07.** Nono
dia sem atualização — a próxima leitura é o teste real de como o "dinheiro grande" reagiu à
sequência inteira: rompimento da soja, compressão do ratio e a fissura de força relativa do
óleo.

**Óleo a apenas 1,4% da resistência 72,00, a menor distância de toda a série — o item
tático de maior atenção para o próximo pregão.** Uma terceira alta seguida tornaria um teste
real da resistência o cenário mais provável, não apenas um risco de cauda.

**Farelo com o quarto fechamento seguido do ratio abaixo de 80%, mas sem nova compressão
hoje — monitorar se o WASDE de amanhã reacende o movimento ou consolida a pausa.**

**USDA Crop Progress — próximo relatório semanal (~13/07) é o teste direto da narrativa de
"calor nos EUA" que sustentou parte do rali da soja, sem atualização desde 05/07.**

**NOPA — segue inacessível (fila `release-nopa-2026-07-09` tratada aqui, sem dado
interpretável apesar do "release novo" sinalizado), 25º dia sem crush americano confirmado
por fonte primária.**

**MPOB — 24 dias consecutivos sem números de palma extraídos**, mantendo cego o efeito da
Indonésia e do El Niño sobre o prêmio de substituição do óleo de soja.

---

## Honestidade

O que não foi possível validar neste briefing de 09/07/2026, onde a confiança é baixa ou há
lacunas materiais:

**1. O padrão de revisão retroativa de indicadores entre dumps de dias diferentes continua,
e hoje ele afetou uma conclusão tática relevante da leitura de ontem.** A leitura de 08/07
([[2026-07-08_leitura-complexo]]) registrou, para aquele dia, ratio Far/Soj em 79,11% e
margem de biodiesel em 0,5177 USD/gal (citando isso como "colada no piso de 0,50"). O dump de
hoje, ao recalcular a mesma data (08/07/2026), mostra ratio em 78,52% e margem de biodiesel
em 0,7088 USD/gal — diferenças de -0,75% e +37% respectivamente. A parte cambial (paridade em
reais) já tinha explicação conhecida (recálculo com PTAX mais fresca via T+1). **Mas essa
explicação não cobre a diferença nos preços de fechamento do CBOT em si nem no heating oil
(HO=F)**, que não dependem de câmbio — hoje ficou mais claro que a revisão afeta também o
heating oil (3,3539 → 3,66 USD/galão para o mesmo dia 08/07), sugerindo que o fenômeno é mais
amplo do que apenas os contratos de grão, possivelmente refletindo correção de settle após
publicação inicial em múltiplas fontes de preço. Esta leitura usa os números do dump de hoje
como referência para todas as comparações dia-a-dia, por serem internamente consistentes
entre si — mas isso significa que a leitura de ontem sobre a margem de biodiesel "colada no
piso" não se sustenta sob os dados de hoje, e foi corrigida na seção de Óleo acima.

**2. Volume de soja e óleo para 08/07/2026 não está disponível nas linhas visíveis do dump
de hoje.** Diferente do farelo (cujo volume de 08/07 aparece consistentemente), as linhas de
soja_cbot e oleo_cbot para 08/07 não constam no dump de hoje — apenas o dia mais recente
(09/07) tem OHLCV completo para as três commodities. A comparação de volume da soja citada
na seção operacional (6.927 hoje vs "7.558" citado pela leitura de ontem) usa um número que
vem de uma fonte diferente (o dump de 08/07, lido pela leitura daquele dia), não do dump de
hoje — deve ser tratada como referência aproximada, não como comparação estritamente
apples-to-apples.

**3. Margem de biodiesel revisada de 0,5177 (leitura de ontem) para 0,7088 (recálculo de
hoje) para a mesma data 08/07 — uma diferença de +37%, a maior discrepância de revisão
documentada até aqui na série.** Isso muda materialmente a leitura tática do óleo: o "gatilho
mais sensível" identificado ontem (margem colada no piso de 0,50) não existe nos dados de
hoje. Optou-se por confiar na série mais fresca (dump de hoje) e corrigir explicitamente a
leitura anterior, em vez de manter um alerta que os dados atuais não sustentam.

**4. A atribuição da virada do ISF/ISO ao efeito calendário ABIOVE segue sem confirmação
direta no banco de dados**, mantida como inferência lógica bem fundamentada (agora reforçada
pela estabilidade de dez sessões seguidas no mesmo patamar), não uma verificação de código.

**5. O checkpoint D+45 da tese PIS/Cofins ([[2026-05-26_pis-cofins-biodiesel-explica-mercado-
fisico-fraco]]) venceu hoje (09/07/2026) sem que o monitor tributário (`system/
tributario_watch.toml`) tenha sido atualizado desde 05/06/2026 (34 dias)** — não foi possível
responder às perguntas de revisão programada daquele insight (votação do Congresso, boletim
ABIOVE, prêmio de contratação bilateral ANP) a partir dos dados disponíveis neste briefing.
Fica registrado como lacuna de acompanhamento, não como confirmação nem invalidação da tese.

**6. COT com defasagem de nove dias em relação ao rali de 06-09/07/2026.** O dado mais
recente (30/06/2026) mostra os fundos reduzindo long em óleo e ampliando short em farelo, mas
não captura a reação a nenhuma sessão desta semana, incluindo a fissura de força relativa do
óleo, agora em sua segunda sessão.

**7. Palma malaia (MPOB) — 24 dias consecutivos sem dados numéricos** (16/jun a 09/07/2026).
O parser continua retornando apenas ~3.437 chars de HTML sem valores extraídos.

**8. RIN D4 como parâmetro fixo (2,11 USD/RIN) segue sendo a maior fonte de incerteza do
modelo de biodiesel**, especialmente relevante à luz da revisão do item 3 — um RIN D4 real
diferente do valor fixo mudaria materialmente qualquer leitura sobre "distância da margem ao
piso".

**9. Percentis históricos de COT não calculados** — os 91.946 net longs em óleo, 4.740 em
farelo (com 105.329 shorts) e 38.149 em soja seguem lidos apenas em nível absoluto e como
fração do open interest corrente, sem série histórica completa para calibrar se estão em
zona extrema.

**10. BCBA Argentina — sem relatórios de esmagamento/exportação acessíveis via scraper**
(page_fetched=1,0 mas sem links de relatório, 09/07/2026, sem atualização). O ritmo de
processamento argentino pós-colheita (50,1 mi t) é estimado por notícia, não medido por
fonte primária.

**11. Dados de clima INMET (BR) não foram usados como driver desta leitura.** Julho é
entressafra da soja brasileira (colheita já concluída, plantio só em outubro) — as
temperaturas de Cascavel/PR, Cuiabá/MT, Sinop/MT etc. no dump são monitoramento de rotina,
sem relevância direta para a tese de preço neste momento do calendário agrícola.

*Nenhum número foi inventado ou estimado além do que consta no briefing de 09/07/2026 e nos
insights anteriores referenciados. A maior contribuição desta leitura foi identificar que a
revisão retroativa dos indicadores (documentada desde leituras anteriores) desta vez alterou
uma conclusão tática concreta — a margem de biodiesel "colada no piso de 0,50" citada ontem
não se sustenta sob os dados de hoje (0,7088 revisado, contra 0,5177 original) — e corrigir
essa leitura explicitamente, em vez de carregá-la adiante sem verificação. Ao mesmo tempo, o
dia registra pausa tática coordenada nas três pernas do complexo (ratio estável, soja com
primeira queda do rali, óleo com segunda alta seguida rumo à resistência) às vésperas do
WASDE de julho — o catalisador fundamentalista que pode romper essa pausa em qualquer
direção.*
