---
data: 2026-07-10
titulo: "O dump de hoje revisa retroativamente dois pilares técnicos da semana — o ratio Far/Soj reaparece em 80,9% (acima do gatilho <80% que sustentava o bear-farelo desde 11/06) e a soja recua a 1.170,00 cts/bu, de volta abaixo do rompimento de 1.180,00 — coincidindo com o sumiço do contrato julho/26 (N26) das curvas de soja e farelo, o que aponta para efeito de rolagem de contrato como explicação mais provável (não confirmada); tudo isso às vésperas do vencimento da MP 1.358 e sem que o sistema tenha, em nenhum momento, uma fonte de dados de WASDE para arbitrar a dúvida"
tags: [complexo, auto-claude]
fontes:
  - CBOT CME (ZSQ26/ZMQ26/ZLQ26 + curva forward completa + HO=F) — sessão de 2026-07-10 (volume atipicamente baixo nas três pernas)
  - BCB PTAX — último dado publicado 2026-07-09 (USD/BRL 5,1329; EUR/BRL 5,872; Selic 0,052531% a.a.), usado por T+1 no cálculo de paridade de hoje
  - CEPEA/ESALQ Paranaguá e Paraná interior via NAG — último dado disponível 2026-07-09
  - NAG Físico BR (farelo MT/IMEA, RS, Rondonópolis; prêmios export PGUA farelo/óleo) — 2026-07-09
  - CFTC COT Managed Money — 2026-06-30 (décimo dia sem atualização nova, sem captar nenhuma sessão de julho)
  - USDA Crop Progress — 2026-07-05 (sem atualização desde a leitura de ontem; próximo relatório semanal ~13/07)
  - NOAA CPC ENSO — 2026-07-10 (El Niño Advisory, sem mudança)
  - ABIOVE projeções mensais — balanços ago-dez/2026 (farelo/óleo/soja), sem alteração frente à leitura anterior
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, ISF/ISO, paridade BR) — 2026-07-10, com recálculo retroativo relevante de 2026-07-09 (ver Honestidade #1)
  - MPOB — 2026-07-10 (25º dia consecutivo sem números extraídos, desde 16/jun)
  - NOPA — 2026-07-10 (fila `release-nopa-2026-07-10`; monthly_status inacessível)
  - system/tributario_watch.toml — eventos MP-1358-2026, MP-1363-2026, PISCOFINS-BIODIESEL-ISENCAO, STJ-RESP-2165276, B16-CNPE-2026, EPA-RFS-2026-2027, 45Z-CLEAN-FUEL, DANANTARA-INDONESIA (todos `atualizado_em` 2026-06-05, sem mudança de status há 35 dias)
  - Notícias Agrícolas / Farm Progress — 160 itens lidos, 5 mantidos em 2026-07-10 (headline de agronomia, sem driver de preço novo)
  - Forecasts estatísticos internos — 2026-07-10 (recalibrados com o spot de hoje)
  - Cruza com [[2026-07-09_leitura-complexo]], [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]], [[2026-05-26_subvencao-fossil-aperta-biodiesel]] (checkpoint D+45 vence hoje, ver Lente Fiscal), [[2026-05-26_pis-cofins-biodiesel-explica-mercado-fisico-fraco]], [[2026-05-26_b16-bullish-farelo]], [[2026-05-26_curva-forward-cbot-oleo-desacopla]]
status: ativa
vies: [neutral-soja, bear-farelo, bear-oleo_soja]
---

## Visão geral

O complexo soja é uma fábrica com uma matéria-prima única — a soja em grão — e dois
produtos de saída fabricados em proporção fixa a cada bushel esmagado: o **farelo** (a
fração proteica, ~78% da massa, vira ração animal) e o **óleo degomado** (a fração de
gordura, ~18-20% da massa, vira óleo de cozinha e biodiesel). Quem decide o ritmo de
esmagamento é a esmagadora, olhando a **crush margin** (valor de farelo + óleo produzidos
por bushel, menos o custo daquele bushel de soja) e o **oil share** (a fração desse valor
capturada pelo óleo). Quando o óleo "paga o crush" a esmagadora tem incentivo a esmagar a
pleno vapor para capturar o valor do óleo e "deixa sobrar" farelo como subproduto menos
desejado, pressionando seu preço relativo. O **ratio Far/Soj** (preço do farelo dividido
pelo preço da soja, na mesma base) é o termômetro dessa dinâmica: abaixo de 80% o farelo
está "abundante" frente à soja, acima de 87% estaria "apertado".

**Hoje, 10/07/2026, é um dia que exige cautela redobrada antes de qualquer conclusão,
porque o próprio dump de dados reescreveu, silenciosamente, dois números que sustentavam as
teses táticas da semana inteira.** Primeiro: o ratio Far/Soj de HOJE fecha em **80,9%**
(indicadores, 10/07/2026) — acima do limiar de 80% que, desde 11/06/2026
([[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]), vinha sendo tratado como o
gatilho central do bear-farelo estrutural. O detalhe crítico é que o MESMO dump de hoje, ao
recalcular o dia de ontem (09/07), também mostra o ratio em **80,85%** — ou seja, usando os
números internamente consistentes de hoje, o ratio está acima de 80% há **duas sessões
seguidas**, quando a leitura de ontem, usando os números que tinha disponíveis NAQUELE
momento, reportou 78,62% para o mesmo dia 09/07 (quarto fechamento seguido abaixo de 80%).
Segundo, e na mesma direção: a soja (ZSQ26.CBT) fechou hoje em **1.170,00 cts/bu**, e o
dump de hoje recalcula o fechamento de ontem (09/07) para **1.177,75 cts/bu** — ambos
ABAIXO do nível técnico de 1.180,00 que vinha sendo celebrado como "rompimento consolidado"
nas últimas quatro leituras (a leitura de ontem, com os números que tinha então, reportou
1.186,00 para o mesmo dia). **As duas reversões têm a mesma impressão digital**: o contrato
de julho/26 (N26), que aparecia nas curvas forward de farelo e soja em todas as leituras
recentes, **desapareceu por completo da curva de hoje para essas duas commodities** —
consistente com uma rolagem do contrato "spot" de referência de N26 (julho, vencendo) para
Q26 (agosto) acontecendo exatamente entre 09/07 e 10/07. Como N26 negociava com prêmio
sobre Q26 em ambas as pernas (farelo N26 319,50 vs Q26 317,40 no dump de ontem; soja N26
1.197,00 vs Q26 1.186,00), uma troca mecânica de qual contrato conta como "preço de
referência" — sem nenhuma nova informação fundamental — bastaria para produzir exatamente
o tipo de "queda" e "reversão de ratio" observados hoje. **Esta é uma hipótese, não uma
confirmação** (não há como auditar o código de geração dos indicadores a partir deste
briefing), e por isso a tese estrutural do farelo NÃO está sendo abandonada hoje, mas a
confiança cai de forma acentuada — ver Honestidade #1 e #2 para o detalhamento completo.

**Leitura de uma linha:** o pivô do complexo continua sendo a crush margin, que hoje bate
**2,9256 USD/bu** (indicadores, 10/07/2026), a QUINTA alta seguida e o maior nível de toda
a série documentada desde 06/07 — isso significa que, independentemente de qual contrato
está sendo usado como referência de preço, a esmagadora segue com forte incentivo a
esmagar a pleno vapor, o que sustenta a oferta física de farelo e óleo de forma
inequívoca. A maior convicção de hoje é justamente essa: a crush em alta consistente é o
único fio condutor que não depende da rolagem de contrato para ser lido. Confiança BAIXA
hoje nos dois níveis técnicos mais citados nas últimas semanas (ratio <80% e rompimento de
1.180,00 na soja) — não porque tenham sido refutados por fundamento novo, mas porque o
próprio dado que os define mudou de definição de um dia para o outro. Confiança
MODERADA-ALTA na crush margin em expansão e no bear-óleo tático (curva em backwardation,
suporte 72,00 ainda intacto por boa margem sob os números de hoje). Nenhuma tese foi
"confirmada" nem "invalidada" hoje por fundamento fresco — o WASDE de julho, esperado desde
a leitura de 08/07, simplesmente **não existe como fonte de dados neste sistema** (ver
Honestidade #3), o que significa que a pergunta que a fila vem fazendo há um mês
("WASDE mudou o quadro?") pode nunca ser respondida pelos dados internos do Radar.

---

## Soja

**Viés: neutro, com viés técnico levemente baixista contaminado por incerteza de dado —
fechamento de 1.170,00 cts/bu (-0,66% frente ao valor revisado de ontem), de volta ABAIXO
do nível de 1.180,00 que vinha sendo tratado como rompimento consolidado, mas o próprio
recuo pode ser em parte artefato de rolagem de contrato**

### O que sustenta a tese

A soja de agosto (ZSQ26.CBT) abriu em **1.179,00**, fez mínima em **1.170,00**, máxima em
**1.181,25** e fechou em **1.170,00 cts/bu** (CBOT CME, 10/07/2026, volume **2.802
contratos** — um volume muito baixo, ver Honestidade #4). Frente ao valor de 09/07 no MESMO
dump de hoje (1.177,75 cts/bu, usado também no cálculo da crush margin de ontem), a
variação foi de **-7,75 cts (-0,66%)**. O ponto central da leitura de hoje é que essa
comparação "dia a dia consistente" (1.177,75 → 1.170,00) já mostra a soja abaixo de
1.180,00 em AMBAS as sessões — divergindo do que a leitura de ontem registrou, em tempo
real, para o mesmo dia 09/07 (1.186,00, quarto fechamento consecutivo acima do nível). A
curva forward de hoje reforça a suspeita de rolagem: o contrato de julho (N26), que
aparecia em toda leitura desde 06/07 com prêmio sobre agosto (Q26), **sumiu por completo da
curva de soja hoje** — a tabela de vencimentos passa a ser Q26 (spot) → U26 (set) → X26
(nov) → F27 (jan/27) → H27 (mar/27), sem nenhuma menção a N26. Isso é coerente com o
contrato de julho ter expirado/rolado no intervalo entre os dois dumps, e se o "preço de
referência" dos indicadores mudou de N26 para Q26 nesse meio tempo, o "recuo" observado
pode refletir, ao menos parcialmente, a diferença estrutural de preço entre os dois
vencimentos (N26 negociava 1.197,00 vs Q26 1.186,00 no dump de ontem, um gap de +11,00 cts)
e não uma venda real do mercado.

**A curva forward de hoje (10/07/2026)**:

| Vencimento | Código | Preço (cts/bu) | Var. vs Ago |
|---|---|---|---|
| Agosto/26 | Q26 | 1.170,00 | — (spot) |
| Setembro/26 | U26 | 1.162,50 | −7,50 |
| Novembro/26 | X26 | 1.173,75 | +3,75 |
| Janeiro/27 | F27 | 1.187,75 | +17,75 |
| Março/27 | H27 | 1.192,50 | +22,50 |

A curva segue em contango normal de Q26 em diante (+22,50 cts até mar/27, +1,9%), sem sinal
de aperto físico — o formato geral da curva (ignorando o contrato N26 que sumiu) é coerente
com o que já vinha sendo documentado nas leituras anteriores.

**O câmbio (BCB PTAX) publicou novo dado para 09/07/2026: USD/BRL 5,1329**, ante 5,1552 em
08/07 — uma **retomada da apreciação do real** (-0,43%), revertendo a pausa de um dia
observada ontem. O EUR/BRL também recuou, de 5,8749 para 5,872 — movimento marginal, mesma
direção. **A paridade em reais oficial (indicadores, 10/07/2026) caiu para R$ 132,40/saca
60kg** (CBOT 1.170,00 cts × PTAX 5,1329 BRL/USD, sem básis) — uma queda de -R$ 0,87/saca
(-0,65%) frente aos R$ 133,27 recalculados para ontem, movendo-se na mesma direção do CBOT
(o real mais forte reforça, não compensa, a queda do grão em dólar). **O básis físico do
porto segue sendo o dado mais forte e mais consistente da leitura de soja, agora pelo quinto
dia seguido de ampliação:** a soja Paranaguá (CEPEA/ESALQ via NAG, 09/07/2026) fechou em
**R$ 140,25/saca**, uma leve queda de -0,11% frente aos R$ 140,40 de 08/07 — a primeira
variação negativa depois de quatro altas seguidas (139,01 em 06/07 → 139,71 em 07/07 →
140,40 em 08/07 → **140,25 em 09/07**) — mas, como a paridade teórica caiu mais forte que o
próprio preço físico, o **básis (prêmio do porto sobre a paridade) na verdade AUMENTA**: R$
140,25 − R$ 132,40 = **+R$ 7,85/saca (+5,9%)**, o maior prêmio de toda a série documentada,
superando os R$ 5,61/saca de ontem em **+40%**. É importante registrar a mesma ressalva que
a leitura de ontem já havia levantado para o salto anterior: parte desse alargamento reflete
uma defasagem de calendário (o CEPEA de 09/07 ainda não capturou a queda do CBOT de hoje,
10/07), não necessariamente um novo patamar de demanda física — mas a direção (básis
crescente, porto pagando cada vez mais acima do "preço justo" teórico) já se repete pela
quinta sessão seguida, o que reduz a chance de ser puro ruído de defasagem. A soja Paraná
interior (NAG, 09/07/2026) fechou em **R$ 132,69/saca** (+0,13% frente a 08/07), e, usando a
paridade de HOJE (mais baixa), o interior passa a negociar **acima** da paridade teórica em
+R$ 0,29/saca — uma inversão frente ao desconto de -R$ 0,58 que valia ontem, embora essa
comparação misture um preço físico de ontem com uma paridade de hoje e deva ser lida com
cautela.

**A colheita argentina segue encerrada em 98%**, produção mantida em 50,1 milhões de
toneladas (Canal Rural, 27/06/2026, sem atualização) — teto estrutural regional inalterado.
BCBA segue acessível via scraper mas sem links de relatório detectado (10/07/2026, sem
mudança).

**O posicionamento dos fundos (COT, CFTC) segue no dado de 30/06/2026**, agora **décimo dia
sem atualização** e ainda sem captar nenhuma parte do movimento de julho: managed money net
long em soja em **+38.149 contratos** (long 133.396, short 95.247), fração do open interest
de 898.681 em **4,25%** — posição net comprada modesta, sem indicação de extremo.

**A condição de lavoura americana (USDA Crop Progress, 05/07/2026)** segue em 53% good + 11%
excellent = **64% bom-ou-melhor**, 6% poor — sem atualização desde a leitura anterior; o
próximo relatório semanal (~13/07) é o teste direto do driver "calor nos EUA" que sustentou
parte do rali das últimas semanas.

**Os forecasts estatísticos internos (10/07/2026, recalibrados)** recuaram, coerente com o
fechamento mais fraco: central 7d = **1.188,36 cts/bu** (bandas 1.129,59-1.247,13), viés
**altista**, descendo dos 1.200,32 de ontem. Central 30d = **1.255,81 cts/bu** (bandas
1.134,15-1.377,48), viés **altista**, também recuando frente a 1.258,92 ontem. O modelo
estatístico continua projetando alta em ambos os horizontes mesmo com o recuo técnico do
dia — uma divergência entre "nível quebrado" (leitura técnica de hoje, sob suspeita de
artefato) e "tendência ainda de alta" (leitura estatística) que só reforça a recomendação de
cautela antes de declarar qualquer reversão.

### O que invalida / risco para a soja

- **Se o próximo pregão (contrato Q26, sem ambiguidade de rolagem) confirmar fechamento
  abaixo de 1.170,00 pela segunda vez seguida**, aí sim o recuo de hoje deixaria de ser
  suspeito de artefato e passaria a ser um sinal técnico genuíno de perda do rompimento.
- **Nenhum WASDE está disponível neste sistema para confirmar ou negar a narrativa de
  "oferta grande"** — ver Honestidade #3. A pergunta que vem sendo levantada há semanas
  segue, e provavelmente seguirá, sem resposta pelos dados internos do Radar.
- **A condição de lavoura (64% bom-ou-melhor, 05/07) piorar no relatório de ~13/07.**
- **O básis físico em Paranaguá (R$ 7,85/sc sobre a paridade, novo máximo da série) se
  dissipar** quando o CEPEA finalmente capturar a queda do CBOT de hoje — merece
  confirmação, não é ainda uma leitura estrutural fechada.
- **O contrato N26 reaparecer na curva de amanhã** (o que indicaria que o sumiço de hoje foi
  um problema pontual de coleta, não uma rolagem real) — isso ajudaria a confirmar ou
  descartar a hipótese de artefato mecânico levantada nesta leitura.

### Leitura operacional — soja

Dado o grau de incerteza sobre se o recuo de hoje é real ou um artefato de rolagem de
contrato, a recomendação é **não tratar 1.170,00 como uma quebra confirmada de suporte nem
apostar contra ela até o próximo pregão trazer um dado limpo (sem mudança de contrato de
referência) para comparar**. Para quem opera o papel, isso significa reduzir o tamanho de
qualquer posição direcional nova até a poeira baixar — nem o bull tático dos últimos dias
nem um novo bear tático têm hoje uma base de dado confiável o suficiente para justificar
convicção alta. Para quem tem física para fixar, o básis de Paranaguá bateu novo recorde
(R$ 140,25 vs R$ 132,40 de paridade, +R$ 7,85/saca) — mesmo com a ressalva de defasagem de
calendário, seguir travando parte do volume físico nesse nível continua sendo a leitura
operacional de maior convicção da seção de soja hoje, muito mais do que qualquer aposta
direcional no papel.

---

## Farelo

**Viés: bear estrutural mantido, mas com confiança rebaixada de forma acentuada — o ratio
Far/Soj de hoje fecha em 80,9% e o de ontem (recalculado no mesmo dump) em 80,85%, ambos
ACIMA do limiar de 80% que definia o gatilho original da tese desde 11/06/2026, tratando a
fila `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` (VENCIDA)**

### Tratando a fila `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`

A pergunta que a fila cobra, agora marcada como VENCIDA: "ratio fechou <80%? WASDE mudou o
quadro? NOPA confirmou crush?" **Resposta honesta de hoje: usando os números do dump de
HOJE, a resposta ao primeiro item é NÃO — o ratio está acima de 80% nas duas últimas
sessões — mas essa resposta contradiz diretamente o que a própria leitura de ontem reportou
para o mesmo dia (78,62%), e a diferença é grande demais (2,2 pontos percentuais) para ser
tratada como ruído de arredondamento.** A tabela abaixo mostra a trajetória do ratio nas
duas óticas — a que cada leitura reportou no dia, e a que o dump de hoje recalcula
retroativamente:

| Data-base | Ratio citado na leitura daquele dia | Ratio no dump de hoje (10/07) |
|---|---|---|
| 11/jun | 81,4% | — (não recalculado hoje) |
| 06/jul | 79,28% | 79,28% |
| 07/jul | 79,46% | 79,46% |
| 08/jul | 79,11% (depois revisado para 78,52%) | 78,52% |
| 09/jul | **78,62%** | **80,85%** |
| 10/jul | — | **80,90%** |

As três primeiras linhas (06 a 08/07) são estáveis entre leituras — a revisão relevante
aparece exatamente na virada de 08→09/07, o mesmo ponto em que o contrato N26 desaparece da
curva forward do farelo (ver seção Soja acima para o mesmo fenômeno). **A hipótese mais
provável é que o "preço spot" usado no cálculo do ratio rolou de N26 (jul/26, que fechava a
319,50 no dump de ontem) para Q26 (ago/26, 317,40) em algum ponto entre os dois dumps, e
como o denominador (soja) também rolou na mesma janela, o efeito líquido sobre a razão não é
trivial de prever sem ver o código** — mas o fato de a reversão ser tão grande e tão
sincronizada com o sumiço de N26 em DUAS pernas (farelo e soja) no mesmo dia torna a
explicação de "dado real mudou" pouco provável. **O protocolo original de 11/06/2026
definia o gatilho como "ratio sustentado abaixo de 80% por 2-3 pregões consecutivos"** — sob
os números de hoje, essa condição não está mais sendo satisfeita (o ratio está ACIMA de 80%
há duas sessões), mas dado o histórico de revisões documentado nesta série (ver Honestidade
#1), a leitura de hoje trata esse desenvolvimento como **um alerta de baixa confiança, não
como uma reversão confirmada da tese**. Quanto aos outros dois itens da fila: **o WASDE
segue inexistente como fonte neste sistema** (Honestidade #3) e **a NOPA segue com
`monthly_status` em 0,0 bool** (indicadores, 10/07/2026), a mesma barreira de membership
pago documentada desde meados de junho, agora por 26 dias seguidos — a fila de hoje traz
`release-nopa-2026-07-10`, mas sem dado interpretável, igual aos dias anteriores.

**A crush margin subiu para 2,9256 USD/bu** (Board Crush: farelo 315,50 + óleo 69,86 − soja
1.170,00; indicadores, 10/07/2026), uma alta de **+1,00%** frente aos 2,8965 recalculados
para 09/07. A série completa usando os valores mais frescos de hoje: 2,4974 (06/jul) →
2,5638 (07/jul) → 2,7316 (08/jul) → 2,8965 (09/jul) → **2,9256 (10/jul)**, a **quinta alta
consecutiva** e uma recuperação acumulada de **+17,2%** desde a mínima local de 06/07. Este
é o dado que MAIS resiste à dúvida sobre rolagem de contrato, porque é uma margem (diferença
entre preços), não um nível absoluto, e a trajetória de alta é monotônica e consistente nas
cinco sessões — o sinal fundamental por trás dele não muda: a esmagadora segue com forte
incentivo a esmagar a pleno vapor, o que sustenta a oferta física de farelo e é coerente com
(não contraria) a tese estrutural bearish, independentemente de qual contrato está sendo
usado como referência de preço.

**As praças físicas de farelo no Brasil (NAG, 09/07/2026)** seguem essencialmente estáveis:
Rondonópolis mantém **R$ 1.620,00/ton** (mesmo valor e mesma variação de +4,52% já registrada
em 08/07 — ou seja, o preço NÃO subiu de novo hoje, apenas manteve o patamar alcançado
anteontem, ao contrário do que uma leitura apressada da "var 4,52%" repetida poderia
sugerir). MT/IMEA segue estável em R$ 1.554,53/ton e RS em R$ 1.640,00/ton. O prêmio de
exportação do farelo em Paranaguá segue em **+0,05 USD/sht** (julho/26) — inalterado,
confirmando que o Brasil segue sem vantagem de preço para exportar farelo.

**Os dados projetados da ABIOVE (sem alteração desde a leitura anterior)** continuam
mostrando a exportação de farelo brasileiro recuando pela metade entre agosto e
dezembro/2026: 1.400 → 1.100 → 850 → 800 → 700 mil t, sem queda proporcional no estoque
final projetado (1.224 → 1.016 → 1.100 → 1.101 → 1.016 mil t). O mecanismo segue intacto e é
o pilar mais sólido da tese estrutural, porque não depende de nenhum contrato futuro CBOT:
menos saída pelo porto empurra o excedente de farelo para o mercado interno de ração,
pressionando o preço doméstico.

**A curva forward do farelo (10/07/2026)**:

| Vencimento | Código | Preço (USD/sht) | Var. vs Ago |
|---|---|---|---|
| Agosto/26 | Q26 | 315,50 | — (spot) |
| Setembro/26 | U26 | 312,30 | −3,20 |
| Outubro/26 | V26 | 310,00 | −5,50 |
| Dezembro/26 | Z26 | 313,30 | −2,20 |
| Janeiro/27 | F27 | 315,00 | −0,50 |

Outubro (V26, 310,00) permanece o vencimento mais descontado, coincidindo com o pico
sazonal de esmagamento simultâneo Brasil + Argentina (ABIOVE projeta 2.143 mil t de
esmagamento BR em outubro). A curva segue com formato coerente ao que já vinha sendo
documentado, descontado o sumiço de N26.

**O posicionamento dos fundos (COT, ainda em 30/06/2026, décimo dia sem atualização)**
mantém o quadro já descrito: managed money **long em 110.069 contratos (18,7% do OI)** vs
**short em 105.329 contratos (17,9% do OI)**, um **net long de apenas 4.740 contratos
(0,8% do OI de 588.519)** — os fundos estão essencialmente equilibrados no farelo, não
"vendidos" de forma extrema, o que deixa pouca munição de short-covering para um eventual
rali de curto prazo caso o ratio realmente tenha revertido.

**O forecast estatístico do farelo (10/07/2026)** segue destoando da tese fundamentalista,
e hoje a divergência aumenta: central 7d = **319,01 USD/sht** (bandas 304,60-333,43), viés
**altista**, subindo dos 313,69 de ontem mesmo com o spot mais baixo — o modelo está lendo
a reversão do ratio como sinal de força, não de fraqueza. Central 30d = **332,86 USD/sht**
(bandas 303,02-362,70), viés **altista**, subindo de 324,56 ontem. **A tensão entre modelo
estatístico (altista) e tese fundamentalista (bearish) é hoje o maior ponto de atenção da
seção de farelo** — justamente no dia em que o gatilho técnico que sustentava o bear
estrutural (ratio <80%) deixou de se confirmar nos dados mais frescos.

### O que invalida / risco para o farelo

- **O ratio Far/Soj permanecer acima de 80% num próximo pregão limpo (sem mudança de
  contrato de referência entre um dump e outro):** se confirmado, esse seria o primeiro
  sinal genuíno de reversão da tese estrutural aberta em 11/06 — o item de maior atenção
  desta leitura.
- **O forecast de 7d e 30d seguirem altistas e a divergência frente à tese fundamentalista
  continuar aumentando** (319,01 e 332,86 hoje, ambos subindo).
- **NOPA seguir inacessível indefinidamente** (26 dias) — sem confirmação direta de
  esmagamento americano.
- **WASDE nunca aparecer como fonte de dado neste sistema** — ver Honestidade #3; a fila
  vem cobrando essa confirmação há um mês sem que exista canal de dados para respondê-la.
- **Crush margin em alta pela quinta sessão seguida (+17,2% acumulado):** sustenta a oferta
  de farelo por ora, mas em algum ponto pode se tornar ela própria um sinal de esmagamento
  excessivo, com efeitos ambíguos sobre volatilidade.

### Leitura operacional — farelo

A tese nascida em 11/06/2026 segue sendo tratada como estruturalmente válida (a ABIOVE
projeta queda de exportação sem queda proporcional de estoque, e a crush margin em expansão
sustenta a oferta), mas **o gatilho técnico original (ratio sustentado <80%) não está mais
confirmado sob os dados de hoje, e a razão mais provável é um artefato de rolagem de
contrato, não uma mudança de fundamento**. Para quem opera o spread de convergência (long
farelo/short soja, ou o crush completo), a recomendação de hoje é **reduzir o tamanho da
posição tática ligada estritamente ao nível "ratio <80%"** até o próximo pregão trazer um
dado limpo, sem abandonar a tese estrutural mais ampla (ABIOVE + crush). Os fundos estão
equilibrados (net 0,8% do OI), então não há pressão de posicionamento extremo em nenhuma
direção que force uma reação rápida. Referência de stop para posição vendida em preço
absoluto: 319-321 USD/sht (ajustada para cima frente à faixa de 314-316 sugerida ontem, dado
que o forecast de 7d de hoje já projeta banda alta em 333,43).

---

## Óleo

**Viés: bear tático mantido, com urgência tática reduzida frente à leitura de ontem — o
óleo fechou em 69,86 cts/lb, essencialmente estável frente ao valor revisado de ontem
(69,92), e a distância até a resistência 72,00 volta a ser confortável (-4,25%), revertendo
a leitura de ontem que via o nível "a 1,4% de distância", tratando a fila
`alerta-quebra_suporte-oleo_cbot-2026-07-10`**

### Tratando a fila `alerta-quebra_suporte-oleo_cbot-2026-07-10`

O óleo de agosto (ZLQ26.CBT) abriu em **70,08**, fez máxima de **70,42**, mínima de
**69,43** e fechou em **69,86 cts/lb** (CBOT CME, 10/07/2026, volume **3.507 contratos**) —
frente ao valor de 09/07 no MESMO dump de hoje (69,92, usado na crush de ontem), a variação
foi de apenas **-0,09%**, um dia essencialmente lateral. A pergunta operacional da fila —
confirma ou muda a tese? — **confirma o nível (ainda abaixo de 72,00), mas desfaz a leitura
de "quase testando a resistência" que a leitura de ontem havia construído em cima do
fechamento de 71,01 daquele dia.** Usando os números internamente consistentes de hoje, a
distância até 72,00 é de **-4,25%** (não -1,4% como reportado ontem) — uma diferença grande
demais para ser só o efeito natural de um dia de baixa; é mais um sintoma da mesma revisão
retroativa documentada nas seções de soja e farelo, ainda que o óleo tenha uma peculiaridade
que os outros dois não têm: **o contrato de julho (N26) NÃO desapareceu da curva do óleo
hoje** (segue cotado a 70,68, com prêmio sobre o spot Q26) — diferente de soja e farelo, cujo
N26 sumiu por completo. Isso enfraquece um pouco a hipótese de "rolagem simultânea nas três
pernas" como explicação única, e sugere que o fenômeno pode ser específico de cada
commodity ou até de cada dia de coleta — mais um motivo para tratar toda a comparação entre
leituras de dias diferentes com cautela redobrada esta semana (ver Honestidade #1 e #2).

**A margem de biodiesel americano está em 0,6599 USD/galão** (indicadores, 10/07/2026:
receita 6,6994 = HO 3,5344 + 1,5×RIN 2,11; custo 6,0395 = óleo 5,2395 + industrial 0,80),
uma queda de -4,7% frente aos 0,6926 recalculados para 09/07 — ainda dentro da faixa de
conforto de 0,50-0,80 USD/gal já documentada (0,5814 em 06/07 → 0,5225 em 07/07 → 0,7088 em
08/07 → 0,6926 em 09/07 → **0,6599 hoje**). O heating oil (HO=F) recuou de 3,5716 (fechamento
09/07) para **3,5344** hoje (-1,04%), e também caiu intradia (abertura 3,5606 → fechamento
3,5344, -0,74%) — uma leve pressão baixista adicional sobre a margem, mas sem sair da faixa
de conforto.

**A curva forward do óleo (10/07/2026)** mantém backwardation clara a partir do spot:

| Vencimento | Código | Preço (cts/lb) | Var. vs Ago |
|---|---|---|---|
| Julho/26 | N26 | 70,68 | +0,82 |
| Agosto/26 | Q26 | 69,86 | — (spot) |
| Setembro/26 | U26 | 69,40 | −0,46 |
| Outubro/26 | V26 | 68,81 | −1,05 |
| Dezembro/26 | Z26 | 68,54 | −1,32 |
| Janeiro/27 | F27 | 68,38 | −1,48 |

A curva caindo -1,48 cts/lb (-2,1%) de agosto a janeiro/27 é praticamente idêntica em
magnitude à de ontem — segue sendo o argumento técnico mais consistente para manter posição
vendida de médio prazo via carry, e é um dos poucos elementos da leitura de óleo que não
depende da ambiguidade de rolagem (a curva inteira está disponível hoje, N26 incluso).

**O posicionamento dos fundos (COT, ainda em 30/06/2026, décimo dia sem atualização)**
mantém o quadro de de-risking já descrito: managed money **long em 128.014 contratos**,
**short em 36.068**, **net long de +91.946 contratos (14,6% do OI de 630.035)** — ainda a
posição mais assimétrica das três pernas do complexo, uma queda de -10,9% frente a 23/06 que
antecedeu o rali do início de julho — décimo dia sem dado fresco para medir a reação dos
fundos à semana.

**O Índice de Suporte do Óleo (ISO) permanece em 100/100 (5/5 condições)**, agora o décimo
primeiro dia seguido nesse patamar desde a virada de 01/07 (indicadores, 10/07/2026) —
mantendo a hipótese de efeito calendário já discutida em leituras anteriores (ver
Honestidade #5).

**O pano de fundo regulatório global segue inalterado desde 05/06/2026**
(`system/tributario_watch.toml`, sem novos `atualizado_em` há 35 dias): EPA Final RFS
2026/2027 sustenta o RIN D4, o crédito 45Z tende a favorecer óleo doméstico americano, e a
Indonésia mantém a exportação de palma centralizada via Danantara mais o levy de exportação
de CPO — mas segue impossível quantificar porque o MPOB está inacessível há 25 dias
consecutivos (3.439 caracteres de HTML sem números extraídos, 10/07/2026).

### O que invalida / risco para o óleo

- **Um fechamento limpo (sem ambiguidade de rolagem) acima de 70,68 (o nível de N26 hoje) ou
  perto de 72,00 num próximo pregão** reabriria o teste de resistência que a leitura de
  ontem via como iminente — hoje esse risco está mais distante, mas não eliminado.
- **A margem de biodiesel, mesmo dentro da faixa de conforto, segue sendo o canal de
  transmissão entre custo do óleo e demanda** — uma queda adicional de heating oil
  reduziria a folga rapidamente.
- **RIN D4 real acima de 2,40 USD/RIN** (o modelo usa 2,11 fixo): incerteza estrutural
  bidirecional, sem novo dado hoje.
- **Dados de palma malaia (MPOB) inacessíveis há 25 dias consecutivos** — segue impossível
  avaliar o efeito de El Niño ou das restrições indonésias sobre o prêmio de substituição.
- **WASDE inexistente como fonte neste sistema** — o item "menos esmagamento futuro → menos
  óleo produzido" segue sem canal de confirmação (Honestidade #3).

### Leitura operacional — óleo

O viés segue bear tático, mas com menos urgência do que a leitura de ontem sugeria: a
distância até a resistência 72,00 volta a ser confortável (-4,25%) e a curva forward segue
em backwardation consistente, o argumento técnico mais robusto (porque não depende da
ambiguidade de rolagem) para manter exposição vendida de médio prazo via carry. Para quem
está posicionado vendido, não há necessidade de apertar o stop tanto quanto a leitura de
ontem recomendava — referência de stop pode voltar para 71,00-72,00 cts/lb. Para quem opera
o oil share (hoje em 52,54%, praticamente estável frente a 52,41% ontem), o viés estrutural
continua favorecendo manter exposição ao óleo dentro do crush frente ao farelo, já que a
margem de biodiesel segue confortável e o ISO em 100/100 pelo décimo primeiro dia.

---

## Spreads e crush — leitura de complexo

### Crush margin: 2,9256 USD/bu — quinta alta seguida, +17,2% desde a mínima de 06/07

A crush está em **2,9256 USD/bu** (Board Crush: farelo 315,50 + óleo 69,86 − soja 1.170,00;
indicadores, 10/07/2026), subindo +1,00% frente aos 2,8965 recalculados para 09/07 — a
quinta alta consecutiva usando os valores mais frescos disponíveis: 2,4974 (06/jul) →
2,5638 (07/jul) → 2,7316 (08/jul) → 2,8965 (09/jul) → **2,9256 (10/jul)**, uma recuperação
acumulada de **+17,2%** em cinco sessões desde a mínima local de 06/07. Este é o dado mais
confiável de toda a leitura de hoje, porque é uma margem entre preços (menos sensível ao
efeito de qual contrato específico está sendo usado como referência) e porque a trajetória
é monotônica: reduz de forma consistente o risco de a esmagadora reduzir ritmo de
esmagamento no curto prazo, sustentando a oferta física de farelo e óleo simultaneamente.

### Ratio Far/Soj: 80,9% — acima do limiar de 80% pela segunda sessão seguida sob os dados de hoje, mas com histórico recente de revisão que pede cautela

Como detalhado na seção de Farelo, o ratio de hoje (80,90%) e o de ontem recalculado no
mesmo dump (80,85%) estão ambos acima do gatilho original de <80% que sustentava o
bear-farelo desde 11/06. A magnitude da reversão entre 08/07 (78,52%) e 09/07 (80,85%, já
dentro do mesmo dump de hoje) é grande demais para tratar como ruído, e coincide
exatamente com o desaparecimento do contrato N26 das curvas de farelo e soja — a leitura de
hoje trata isso como alerta de baixa confiança sobre o nível técnico, não como reversão
fundamentalista confirmada, tratando a fila
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`.

### Oil share: 52,54% — estável, sem tendência direcional clara na semana

O oil share está em 52,54% hoje, ante 52,41% recalculado para ontem (+0,13 p.p.) — dentro do
mesmo dump de hoje, a série da semana é 51,99% (06/jul) → 52,03% (07/jul) → 53,15% (08/jul)
→ 52,41% (09/jul) → **52,54% (10/jul)**, um padrão de vaivém em torno de 52-53%, não uma
tendência monotônica de alta como leituras anteriores haviam descrito — outro sinal de que
a série recente ganhou ruído adicional.

### Oil-meal spread: 0,7436 USD/bu — segunda alta seguida sob os números de hoje

O oil-meal spread (contribuição do óleo menos a do farelo por bushel) subiu para 0,7436 ante
0,7084 recalculados para ontem — um avanço de +5,0%, mas a série completa do dump de hoje
(0,5698 em 06/07 → 0,5885 em 07/07 → 0,9229 em 08/07 → 0,7084 em 09/07 → 0,7436 hoje) mostra
oscilação, não uma trajetória limpa — coerente com o mesmo ruído de rolagem documentado nas
outras métricas.

### ISF em 80/100, ISO em 100/100 — décimo primeiro pregão seguido no mesmo patamar

O Índice de Sobra de Farelo (ISF) está em 80/100 (4/5 condições) e o Índice de Suporte do
Óleo (ISO) em 100/100 (5/5) — o mesmo patamar desde 01/07/2026, agora o décimo primeiro dia
consecutivo.

### O que os índices dizem juntos em 10/07/2026

ISF 80/100 + ISO 100/100 (ambos estáveis, efeito calendário) + ratio Far/Soj de volta acima
de 80% sob os dados de hoje (mas com confiança baixa dado o histórico de revisão) + oil share
sem tendência clara (52-53%, vaivém) + crush margin em alta pela quinta sessão seguida
(+17,2% acumulado, o dado mais confiável da leitura) + margem de biodiesel dentro da faixa
de conforto + soja de volta abaixo de 1.180,00 (também sob suspeita de artefato) + farelo com
fundamentos ABIOVE inalterados (exportação recuando, estoque sustentado) + óleo com urgência
tática reduzida frente à resistência 72,00:

**A leitura de hoje é de "dado contaminado, fundamento intacto".** O desenvolvimento mais
importante do dia não é uma mudança de tese, mas a descoberta de que dois níveis técnicos
centrais da semana (ratio <80% e rompimento de 1.180,00) dependem de uma definição de
"contrato spot" que parece ter mudado entre um dump e outro, sem aviso e sem explicação
disponível nos dados. A régua de gestão de risco deve subir, não pela direção do mercado,
mas pela qualidade do dado — até que um pregão limpo (com o mesmo contrato de referência do
dia anterior) confirme se as reversões são reais ou mecânicas, a recomendação geral é reduzir
o tamanho de posições táticas ancoradas nesses dois níveis específicos, mantendo as teses
estruturais mais amplas (ABIOVE farelo, backwardation óleo, crush em expansão) que não
dependem dessa ambiguidade.

---

## Lente fiscal e regulatória BR

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L) — vence AMANHÃ
(11/07/2026, fila `trib-MP-1358-2026-2026-07-11`).** Sem mudança desde a última leitura
(`system/tributario_watch.toml`, evento MP-1358-2026, `atualizado_em` 2026-06-05, status
"tramitacao", `proximo_marco` = "Deliberação comissão mista", `proximo_data` = 2026-07-11) —
o monitor tributário está parado há 35 dias sem nenhuma atualização de status, mesmo com o
vencimento batendo na porta. A MP ressarce PIS/Cofins/Cide da gasolina e do diesel, mantendo
o combustível fóssil artificialmente mais barato — o mesmo espírito da MP 1.363/2026
(subsídio de R$ 1,12/L ao diesel, vigente até 31/12/2026, já tratada em
[[2026-05-26_subvencao-fossil-aperta-biodiesel]]). O mecanismo de transmissão para o
complexo soja é indireto mas real: enquanto o combustível fóssil segue subsidiado, a
competitividade relativa do biodiesel dentro do mix B15 mandatório permanece pressionada,
mantendo a margem da indústria de biodiesel (maior consumidora industrial de óleo de soja no
Brasil) mais apertada do que teria sem a subvenção ao concorrente fóssil. Se a MP caducar sem
conversão em lei amanhã, é um sinal (fraco, mas real) de perda de fôlego político do pacote
pró-fóssil — levemente positivo para a competitividade do biodiesel e, por extensão, para a
demanda industrial de óleo de soja; se for convertida ou prorrogada, reforça o quadro de
pressão já documentado desde maio. **Este é o evento mais imediato de toda a leitura de
hoje** — resolve-se em menos de 24 horas.

**Checkpoint D+45 de [[2026-05-26_subvencao-fossil-aperta-biodiesel]] vence exatamente
HOJE (10/07/2026).** O insight original programou, para esta data, quatro perguntas: as MPs
1.340/1.349/1.358 foram convertidas em lei pelo Congresso ou caducaram? A Petrobras manteve
adesão à subvenção? O leilão/contratação bilateral ANP de biodiesel saiu com que prêmio? A
Frente Parlamentar do Biodiesel propôs ADI formal? **Nenhuma dessas perguntas pode ser
respondida com os dados deste briefing** — o monitor tributário não tem atualização desde
05/06/2026 (35 dias) e nenhuma das fontes públicas rastreadas pelo sistema (ABIOVE, NAG,
notícias) trouxe informação sobre votação, adesão da Petrobras ou leilão ANP. Fica
registrado como uma lacuna de acompanhamento explícita — o checkpoint formal do próprio
sistema venceu sem resposta, e a decisão responsável é reconhecer isso e não especular sobre
o resultado.

**Isenção PIS/Cofins biodiesel — vencimento em 31/07/2026, 21 dias.** Sem sinalização
pública de renovação até hoje (evento PISCOFINS-BIODIESEL-ISENCAO, `atualizado_em`
2026-06-05, sem mudança). O checkpoint D+45 desse insight ([[2026-05-26_pis-cofins-biodiesel-
explica-mercado-fisico-fraco]]) já venceu (09/07/2026) sem resposta, como já registrado na
leitura de ontem — segue sem resposta hoje também.

**B16 — sem data, travado em B15.** Sem mudança de status (evento B16-CNPE-2026,
`atualizado_em` 2026-06-05, status "adiado", sem `proximo_data`).

**MP 1.363/2026 (subsídio ao diesel fóssil) — em vigor até 31/12/2026.** Sem alteração.
Bearish estrutural persistente para a demanda incremental de óleo de soja no mercado
doméstico brasileiro.

**STJ REsp 2.165.276/2026 — crédito PIS/Cofins para esmagadoras.** Sem alteração. Bullish
para a soja/óleo (alívio de custo de entrada para biodiesel) e, por extensão, incentivo a
mais esmagamento — coerente com mais oferta de co-produtos, reforçando a leitura bearish do
farelo.

**Câmbio (PTAX) publicou novo dado para 09/07/2026 (5,1329 BRL/USD), retomando a apreciação
do real** — já tratado na seção de Soja. O impacto fiscal indireto (real mais forte reduz a
paridade de exportação em reais, pressionando margem de quem exporta em dólar e vende custo
em real) segue neutro-a-levemente-negativo para o produtor doméstico, sem mudança de regime.

**Pano de fundo regulatório global (EUA e Indonésia) segue dando suporte estrutural ao
óleo, sem contradizer o viés bearish tático** — detalhado na seção Óleo.

---

## Riscos e eventos próximos

**Vencimento da MP 1.358/2026 — AMANHÃ, 11/07/2026, fila `trib-MP-1358-2026-2026-07-11`.**
O evento mais imediato de toda a leitura — deliberação da comissão mista é o marco a
monitorar.

**Checkpoint D+45 de [[2026-05-26_subvencao-fossil-aperta-biodiesel]] — vence hoje,
10/07/2026, sem dado disponível para respondê-lo** (ver Lente Fiscal).

**A ambiguidade de rolagem de contrato (N26→Q26) documentada nesta leitura é, ela própria,
o principal risco de curto prazo para a qualidade da leitura dos próximos dias** — até que
um pregão traga dados limpos e comparáveis, qualquer leitura "dia a dia" de soja e farelo
deve ser tratada com cautela redobrada.

**WASDE — inexistente como fonte de dados neste sistema (ver Honestidade #3).** A fila vem
cobrando confirmação do WASDE desde meados de junho; este briefing não tem, nunca teve, e
aparentemente não terá canal para captar esse dado. Recomenda-se avaliar, fora desta
leitura, se vale a pena adicionar uma fonte USDA WASDE ao sistema, dado quanto peso a
narrativa dos últimos 30 dias colocou nessa confirmação pendente.

**Isenção PIS/Cofins biodiesel — vencimento 31/07/2026 (21 dias).** Sem sinalização de
renovação até agora.

**COT CFTC — dado de 30/06/2026, décimo dia sem atualização.** A próxima leitura é o teste
real de como o "dinheiro grande" reagiu a toda a semana de julho, incluindo o rali, a pausa e
a reversão de hoje.

**USDA Crop Progress — próximo relatório semanal (~13/07)** é o teste direto da narrativa de
"calor nos EUA" que sustentou parte do rali da soja, sem atualização desde 05/07.

**NOPA — segue inacessível** (fila `release-nopa-2026-07-10` tratada aqui, sem dado
interpretável), 26º dia sem crush americano confirmado por fonte primária.

**MPOB — 25 dias consecutivos sem números de palma extraídos**, mantendo cego o efeito da
Indonésia e do El Niño sobre o prêmio de substituição do óleo de soja.

---

## Honestidade

O que não foi possível validar neste briefing de 10/07/2026, onde a confiança é baixa ou há
lacunas materiais:

**1. A revisão retroativa dos indicadores entre dumps de dias diferentes, já documentada em
leituras anteriores, atingiu hoje um novo patamar de gravidade: ela reverteu a direção de
DOIS níveis técnicos centrais da semana.** O ratio Far/Soj para 09/07/2026 foi reportado
como 78,62% pela leitura daquele dia, mas o dump de hoje recalcula o MESMO dia para 80,85% —
uma diferença de +2,23 pontos percentuais que muda a conclusão de "abaixo do gatilho de 80%"
para "acima dele". Da mesma forma, o fechamento da soja em 09/07 foi reportado como 1.186,00
cts/bu (acima do nível de 1.180,00) pela leitura daquele dia, mas o dump de hoje recalcula o
mesmo dia para 1.177,75 cts/bu (abaixo do nível). Ambas as reversões coincidem com o
desaparecimento do contrato de julho/26 (N26) das curvas forward de farelo e soja no dump de
hoje — um indício forte, mas não confirmado, de que o "preço de referência" usado nos
indicadores rolou de N26 para Q26 entre os dois dumps. Esta leitura optou por usar,
consistentemente, os números do dump de HOJE para todas as comparações dia-a-dia (por serem
internamente consistentes entre si), mas isso significa que as conclusões táticas da leitura
de ontem (ratio comprimido pela quarta vez, rompimento de 1.180,00 mantido pela quarta vez)
não se sustentam sob os dados de hoje — e essa reversão foi tratada explicitamente, não
carregada adiante sem verificação.

**2. A mesma janela de tempo (08→09/07) NÃO produziu o mesmo padrão no óleo** — o contrato
N26 do óleo segue cotado normalmente hoje (70,68 cts/lb, com prêmio sobre o spot), diferente
de farelo e soja. Isso enfraquece a hipótese de uma rolagem simples e uniforme nas três
pernas do complexo, e significa que a explicação real pode ser mais específica (por
commodity, ou até por dia de coleta de dados) do que a hipótese de "rolagem de contrato"
consegue capturar por completo. Esta leitura apresenta a hipótese de rolagem como a mais
provável, não como uma certeza.

**3. Nenhuma fonte de dados WASDE existe neste briefing, em nenhuma das 15 categorias de
dados públicos listadas (abiove, bcb, bcba, cepea_paranagua, cepea_rss, cftc_cot, cme_cbot,
indicators, inmet, mpob, nag_fisico, noaa_cpc, nopa, noticias_rss, usda_crop_progress).** As
últimas quatro leituras (07/07 a 09/07) mencionaram repetidamente o "WASDE de julho" como
catalisador esperado "amanhã ou depois de amanhã" — mas não há, e aparentemente nunca houve,
um canal de coleta de dados WASDE neste sistema. Isso significa que a expectativa
repetidamente citada de "o WASDE vai confirmar ou negar a tese" não pode ser resolvida pelos
dados internos do Radar, e deveria ter sido sinalizada como lacuna estrutural antes, não
apenas hoje. Registro isso como a lacuna mais importante identificada nesta leitura.

**4. Volume de negociação atipicamente baixo nas três pernas do CBOT hoje** — farelo com
apenas 1.069 contratos (ante 28.903 no mesmo contrato Q26 ontem, uma queda de -96%), soja
com 2.802 e óleo com 3.507, todos muito abaixo dos volumes típicos de dias anteriores
(dezenas de milhares de contratos). Não há explicação disponível nos dados para essa queda —
pode refletir liquidez ainda migrando para o novo contrato de referência pós-rolagem, uma
sessão de coleta parcial/antecipada, ou baixa atividade de sexta-feira — mas o volume baixo
por si só é um motivo adicional para não superinterpretar as variações de preço de hoje como
sinal direcional forte.

**5. A atribuição da virada do ISF/ISO ao efeito calendário ABIOVE segue sem confirmação
direta no banco de dados**, mantida como inferência lógica bem fundamentada (agora reforçada
pela estabilidade de onze sessões seguidas no mesmo patamar), não uma verificação de código.

**6. O checkpoint D+45 de [[2026-05-26_subvencao-fossil-aperta-biodiesel]] venceu hoje
(10/07/2026) sem que o monitor tributário (`system/tributario_watch.toml`) tenha sido
atualizado desde 05/06/2026 (35 dias)** — não foi possível responder a nenhuma das quatro
perguntas de revisão programada daquele insight a partir dos dados disponíveis neste
briefing. Fica registrado como lacuna de acompanhamento, não como confirmação nem
invalidação da tese.

**7. COT com defasagem de dez dias em relação a toda a semana de julho.** O dado mais recente
(30/06/2026) não captura nenhuma parte do rali do início de julho, da pausa do meio da
semana, nem da reversão técnica de hoje.

**8. Palma malaia (MPOB) — 25 dias consecutivos sem dados numéricos** (16/jun a
10/07/2026). O parser continua retornando apenas ~3.439 chars de HTML sem valores extraídos.

**9. RIN D4 como parâmetro fixo (2,11 USD/RIN) segue sendo uma fonte relevante de incerteza
do modelo de biodiesel**, sem novo dado hoje.

**10. Percentis históricos de COT não calculados** — os 91.946 net longs em óleo, 4.740 em
farelo e 38.149 em soja seguem lidos apenas em nível absoluto e como fração do open interest
corrente, sem série histórica completa para calibrar se estão em zona extrema.

**11. BCBA Argentina — sem relatórios de esmagamento/exportação acessíveis via scraper**
(page_fetched=1,0 mas sem links de relatório, 10/07/2026, sem atualização).

**12. Dados de clima INMET (BR) não foram usados como driver desta leitura.** Julho é
entressafra da soja brasileira (colheita já concluída, plantio só em outubro) — monitoramento
de rotina, sem relevância direta para a tese de preço neste momento do calendário agrícola.

*Nenhum número foi inventado ou estimado além do que consta no briefing de 10/07/2026 e nos
insights anteriores referenciados. A contribuição central desta leitura foi identificar que a
revisão retroativa dos indicadores — já um padrão conhecido nas leituras anteriores — hoje
reverteu a DIREÇÃO de dois níveis técnicos que vinham sustentando as teses táticas mais
citadas da semana (ratio Far/Soj <80% e rompimento de 1.180,00 na soja), muito provavelmente
por efeito de rolagem do contrato de referência de N26 para Q26, e tratar essa reversão com a
cautela que ela exige — nem ignorando o dado novo, nem tratando-o como confirmação
definitiva de mudança de fundamento. Ao mesmo tempo, o único fio condutor que atravessa a
semana sem ambiguidade é a crush margin, em quinta alta consecutiva e maior nível da série —
o sinal mais confiável de todos: a esmagadora segue rodando a pleno vapor, sustentando a
oferta física de farelo e óleo, independentemente de qual contrato está sendo usado como
referência de preço em cada dump.*
