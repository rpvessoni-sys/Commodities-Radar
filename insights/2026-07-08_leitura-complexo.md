---
data: 2026-07-08
titulo: "Terceiro fechamento seguido do ratio Far/Soj abaixo de 80% (79,11%) cimenta a tese bear-farelo de 11/06, enquanto a soja rompe 1.180 pela terceira vez consecutiva (1.196,00, novo topo do ciclo) com volume dobrando frente a ontem — mas o farelo perde 94% do volume do dia anterior e o óleo, apesar de ainda preso abaixo do suporte 72,00, entrega a maior alta percentual do complexo hoje (+1,11%), uma fissura tática que merece vigilância"
tags: [complexo, auto-claude]
fontes:
  - CBOT CME (ZSQ26/ZMQ26/ZLQ26 + curva forward completa + HO=F) — sessão de 2026-07-08
  - BCB PTAX — último dado publicado 2026-07-07 (USD/BRL 5,1458; EUR/BRL 5,8786; Selic 0,052531% a.a.), usado por T+1 no cálculo de paridade de hoje
  - CEPEA/ESALQ Paranaguá e Paraná interior via NAG — último dado disponível 2026-07-07
  - NAG Físico BR (farelo MT/IMEA, RS, Rondonópolis; prêmios export PGUA farelo/óleo) — 2026-07-07
  - CFTC COT Managed Money — 2026-06-30 (mesma leitura da série anterior, sem atualização nova)
  - USDA Crop Progress — 2026-07-05 (sem atualização desde a leitura de ontem, próximo relatório semanal ~13/07)
  - NOAA CPC ENSO — 2026-07-08 (El Niño Advisory, sem mudança)
  - ABIOVE projeções mensais — balanços ago-dez/2026 (farelo/óleo/soja), sem alteração
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, ISF/ISO, paridade BR) — 2026-07-08, com recálculo retroativo de 2026-07-07 (ver Honestidade #1)
  - MPOB — 2026-07-08 (23º dia consecutivo sem números extraídos, desde 16/jun)
  - NOPA — 2026-07-08 (fila `release-nopa-2026-07-08`; monthly_status inacessível)
  - system/tributario_watch.toml — eventos MP-1358-2026, MP-1363-2026, PISCOFINS-BIODIESEL-ISENCAO, STJ-RESP-2165276, B16-CNPE-2026, EPA-RFS-2026-2027, 45Z-CLEAN-FUEL, DANANTARA-INDONESIA, INDONESIA-B50, INDONESIA-LEVY-PMK9 (todos `atualizado_em` 2026-06-05, sem mudança de status)
  - Notícias Agrícolas / Farm Progress — 160 itens lidos, 4 mantidos em 2026-07-08 (sem manchete específica destacada no dump para hoje)
  - Forecasts estatísticos internos — 2026-07-08 (recalibrados com o spot de hoje)
  - Cruza com [[2026-07-07_leitura-complexo]], [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]], [[2026-05-26_subvencao-fossil-aperta-biodiesel]], [[2026-05-26_pis-cofins-biodiesel-explica-mercado-fisico-fraco]], [[2026-05-26_b16-bullish-farelo]], [[2026-05-26_curva-forward-cbot-oleo-desacopla]]
status: ativa
vies: [bull-soja, bear-farelo, bear-oleo]
---

## Visão geral

O complexo soja é uma fábrica com uma única matéria-prima (a soja em grão) e dois produtos
de saída fabricados em proporção fixa a cada bushel esmagado: o **farelo** (a fração proteica,
~78% da massa, vira ração animal) e o **óleo degomado** (a fração de gordura, ~18-20% da
massa, vira óleo de cozinha e biodiesel). Quem decide o ritmo de esmagamento é a esmagadora,
olhando a **crush margin** (o valor de farelo + óleo produzidos por um bushel, menos o custo
daquele bushel) e o **oil share** (a fração desse valor capturada pelo óleo). Quando o óleo
"paga o crush" — como vem acontecendo desde maio, com oil share girando em torno de 52% —, a
esmagadora tem incentivo a esmagar a pleno vapor para capturar o valor do óleo, e "deixa
sobrar" farelo como subproduto menos desejado. O **ratio Far/Soj** (preço do farelo dividido
pelo preço da soja, na mesma base) é o termômetro dessa dinâmica: abaixo de 80% o farelo está
"abundante" frente à soja, acima de 87% estaria "apertado".

**Hoje, 08/07/2026, é o dia da tripla confirmação com uma fissura tática nova.** Primeiro, o
ratio Far/Soj fechou em **79,11%** (indicadores, 08/07/2026) — o **terceiro fechamento seguido
abaixo de 80%**, ampliando a compressão iniciada em 06/07 (79,28%) e sustentada em 07/07
(79,46%, valor recalculado hoje — ver Honestidade #1). É o desenvolvimento mais robusto desde
que a tese nasceu em 11/06/2026 (fila `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-
farelo-D+7`, tratada abaixo): três sessões seguidas satisfazendo o protocolo original de
confirmação ("2-3 fechamentos consecutivos abaixo de 80%"). Segundo, a soja (ZSQ26.CBT) fechou
em **1.196,00 cts/bu**, o **terceiro fechamento consecutivo acima do nível técnico de 1.180,00**
(fila `alerta-quebra_resistencia-soja_cbot-2026-07-08`) e o **novo topo de todo o ciclo desde o
rompimento**, com o volume do dia (7.558 contratos) **mais que dobrando** frente ao volume
reportado pela leitura de ontem para 07/07 (3.640 contratos) — o exato sinal de participação
que a leitura de ontem apontava como faltante para validar tecnicamente o rompimento.

O terceiro fato é a fissura: **o óleo (ZLQ26.CBT) fechou em 69,35 cts/lb, subindo +1,11% no
dia** (de 68,59 em 07/07, via indicadores) — a **maior alta percentual das três pernas do
complexo hoje**, maior que a da própria soja (+0,19%) e contrastando com a queda do farelo
(-0,25%, de 316,20 para 315,40). Apesar disso, o óleo **segue fechado abaixo do suporte-virou-
resistência de 72,00** (fila `alerta-quebra_suporte-oleo_cbot-2026-07-08`) — a tese bear tática
não está invalidada, mas o dia em que o óleo lidera a alta do complexo, ainda que sem testar a
resistência, é um contraponto que merece registro e vigilância, não descarte.

O quarto fato é sobre volume do farelo: caiu de **37.840 contratos (07/07) para apenas 2.204
(08/07) — uma queda de -94,2%**, a comparação mais limpa do dia porque ambos os números vêm do
mesmo dump (sem o problema de revisão que afeta preços entre dumps de dias diferentes). Um
volume tão baixo no mesmo dia em que o ratio confirma pela terceira vez a compressão estrutural
é um alerta de liquidez: o movimento de preço do farelo hoje (-0,25%) carrega menos peso
informacional do que os movimentos anteriores da semana.

**Leitura de uma linha:** o dia consolida a tese estrutural mais forte da série (ratio Far/Soj
com três fechamentos seguidos abaixo de 80%, tese de 11/06 agora robustamente confirmada) e o
rompimento técnico da soja ganha a confirmação de volume que faltava — mas o óleo, mesmo preso
abaixo do suporte, lidera a alta percentual do dia, e o farelo confirma sua queda em volume
quase inexistente. Confiança alta no bear-farelo estrutural (a mais alta da série até aqui);
confiança moderada-alta no bull-soja tático (agora com volume a favor); confiança moderada no
bear-óleo tático (tese ainda intacta no nível de preço, mas com o primeiro sinal de força
relativa positiva desde a quebra do suporte).

---

## Soja

**Viés: bull tático, reforçado — terceiro fechamento consecutivo acima de 1.180,00, novo topo
do ciclo em 1.196,00, com volume dobrando frente ao dia anterior, resolvendo o principal risco
técnico (fraqueza de participação) que a leitura de ontem havia sinalizado**

### O que sustenta a tese

A soja de agosto (ZSQ26.CBT) abriu em 1.192,25, fez mínima em 1.191,50, máxima em 1.199,00 e
fechou em **1.196,00 cts/bu** (CBOT CME, 08/07/2026, volume **7.558 contratos**) — tratando a
fila `alerta-quebra_resistencia-soja_cbot-2026-07-08`. Frente ao fechamento de 07/07 (1.193,75
cts/bu, valor implícito no cálculo de crush margin dos indicadores de 07/07/2026), a alta do
dia foi de **+2,25 cts (+0,19%)** — um ganho pequeno em termos percentuais, mas que consolida o
**terceiro fechamento seguido acima do nível técnico de 1.180,00** (06/07: 1.184,00; 07/07:
1.193,75; 08/07: 1.196,00) e cria o **maior fechamento de todo o ciclo de alta**, superando o
próprio 1.193,75 de ontem. O dado mais relevante tecnicamente é o volume: **7.558 contratos
hoje contra os 3.640 que a leitura de 07/07 reportou para aquele pregão — um salto de
+107,6%**. É exatamente o oposto do padrão de "confirmação em volume fraco" que preocupava a
leitura anterior: hoje o mercado não apenas sustentou o nível, mas atraiu mais participação
para fazê-lo, o que dá ao rompimento uma base técnica mais sólida. (Nota de comparabilidade:
o número de 3.640 contratos para 07/07 vem da leitura de ontem, que usava o dump daquele dia;
o dump de hoje não republica o volume de soja de 07/07 nas linhas visíveis — ver Honestidade
#2 — então a magnitude exata do salto de participação deve ser lida com uma margem de cautela,
mas a direção do sinal, mais volume hoje que ontem, é consistente com o padrão observado.)

**Sem manchete fresca específica sobre soja no dump de hoje** — a seção de notícias registra
apenas "160 itens lidos, 4 mantidos (soja/farelo/oleo)" em 08/07/2026, sem headline destacada
para o dia (a última manchete explícita no dump é de 07/07, sobre edição genética de nematoide,
sem relevância direta de preço). Isso significa que o driver informacional mais recente
continua sendo a combinação de calor nos EUA + vendas para a China da manchete de 06/07
(Farm Progress) e a leve deterioração de condição de lavoura do USDA Crop Progress de 05/07
(64% bom-ou-melhor, -1 p.p. frente a 28/06) — nenhum dos dois teve atualização nova hoje, o
próximo relatório semanal de condição sai por volta de 13/07.

**O câmbio (BCB PTAX) publicou novo dado para 07/07/2026: USD/BRL 5,1458**, ante 5,1670 em
06/07 — a **quinta leitura seguida de apreciação do real** desde o início de julho: 5,1950
(01/jul) → 5,1945 (02/jul) → 5,1717 (03/jul) → 5,1670 (06/jul) → **5,1458 (07/jul)**, uma
queda acumulada de -0,95% no período. O mecanismo segue o mesmo descrito ontem: o rali da
soja não está sendo puxado por câmbio (que trabalha na direção contrária, real mais forte =
paridade em reais mais fraca, tudo mais constante), está sendo puxado integralmente pelo CBOT.

**A paridade em reais oficial (indicadores, 08/07/2026) subiu para R$ 135,68/saca60kg** (CBOT
1.196,00 cts × PTAX 5,1458 BRL/USD, sem básis) — um ganho de +R$ 0,26/saca (+0,19%) frente aos
R$ 135,42 recalculados para 07/07 (que usam a mesma PTAX de 5,1458, já disponível
retroativamente — ver Honestidade #1 para a explicação de por que os indicadores de dias
anteriores mudam quando uma PTAX mais fresca chega ao sistema). **O dado mais forte do dia
está de novo no físico do porto:** a soja Paranaguá (CEPEA/ESALQ via NAG, 07/07/2026) fechou
em **R$ 139,71/saca**, subindo +0,5% frente aos R$ 139,01 de 06/07 — e esse valor está **R$
4,03/saca ACIMA da paridade teórica** (R$ 135,68), um prêmio de básis ainda maior que o de
ontem (R$ 3,88/saca). O básis físico positivo em Paranaguá não é um evento pontual: já é a
terceira leitura seguida em que o físico do porto paga prêmio crescente sobre o "preço justo"
de conversão do CBOT — sinal consistente de demanda física de exportação disputando o produto
no porto. A soja Paraná interior (NAG, 07/07/2026) fechou em **R$ 132,04/saca** (+1,62% frente
a 06/07), reduzindo o desconto frente à paridade para -R$ 3,64/saca (ante -R$ 5,20 em 06/07) —
o interior também está convergindo para cima, não apenas o porto.

**A colheita argentina segue encerrada em 98%**, produção mantida em 50,1 milhões de toneladas
(Canal Rural, 27/06/2026, sem atualização) — segue sendo o teto estrutural regional, sem
mudança.

**O posicionamento dos fundos (COT, CFTC) segue no dado de 30/06/2026, sem atualização nova
desde a leitura de ontem** — managed money net long em soja em +38.149 contratos (long
133.396, short 95.247), fração do open interest de 898.681 em 4,25%. O dado é o mesmo de
ontem: um desalavancamento coletivo generalizado (OI caiu -10,7% frente a 23/06), não uma
aposta direcional nova, ainda sem captar a reação dos fundos ao rali dos últimos três pregões
(06-08/07).

**A curva forward (08/07/2026)** mantém contango moderado:

| Vencimento | Código | Preço (cts/bu) | Var. vs Ago |
|---|---|---|---|
| Julho/26 | N26 | 1.199,00 | +3,00 |
| Agosto/26 | Q26 | 1.196,00 | — (spot) |
| Setembro/26 | U26 | 1.187,25 | −8,75 |
| Novembro/26 | X26 | 1.197,25 | +1,25 |
| Janeiro/27 | F27 | 1.210,00 | +14,00 |
| Março/27 | H27 | 1.212,75 | +16,75 |

Nota-se que o contrato de julho (N26, o mais próximo do vencimento) negocia **acima** do
contrato de agosto (Q26) — uma pequena inversão (backwardation de curtíssimo prazo) que não
aparecia na curva de ontem, plausivelmente refletindo o efeito de vencimento se aproximando
(N26 é o front month saindo de cena) mais do que um sinal de aperto real de oferta. De agosto
a março/27 o contango segue moderado (+16,75 cts, +1,4%), levemente mais achatado que os
+23,50 cts (+2,0%) de ontem — a curva não está "gritando" escassez.

**Os forecasts estatísticos internos (08/07/2026, recalibrados) viraram de forma notável:**
central 7d = **1.205,29 cts/bu** (bandas 1.144,60-1.265,98), viés **altista** — o modelo
passou de tratar o fechamento de ontem como "centro esperado" (viés lateral, central 1.190,75)
para projetar alta adicional acima do fechamento de hoje. O central 30d = **1.250,66 cts/bu**
(bandas 1.125,03-1.376,30), viés **altista**, subindo de 1.218,97 ontem. Pela primeira vez na
série recente, o modelo estatístico de curto prazo (7d) concorda com a tese fundamentalista de
alta, em vez de tratá-la como já precificada.

### O que invalida / risco para a soja

- **O forecast de 7d (central 1.205,29) já embutir toda a expectativa de alta:** se o próximo
  pregão testar essa região sem romper, o rali perde o argumento estatístico de continuidade.
- **A pequena inversão N26 > Q26 na curva reverter para contango normal:** indicaria que o
  efeito observado hoje era mecânico (vencimento), não sinal de aperto físico.
- **WASDE de julho (~10/07/2026) reverter a leitura de "oferta grande":** cai na mesma semana
  do vencimento da MP 1.358 (ver Riscos), a três dias de distância.
- **A condição de lavoura (64% bom-ou-melhor, 05/07) piorar mais no relatório de ~13/07,**
  ainda sem dado novo desde a leitura de ontem.
- **O prêmio físico em Paranaguá (R$ 4,03/sc sobre a paridade, o maior da série) se dissipar
  de uma hora para outra:** três leituras seguidas de prêmio crescente reduzem a chance de ser
  ruído, mas ainda não é uma série longa o suficiente para tratar como estrutural.

### Leitura operacional — soja

O rompimento de 1.180,00 chega ao terceiro fechamento consecutivo, agora com o reforço de
volume que faltava: 7.558 contratos hoje, mais que o dobro do reportado para 07/07. Para quem
opera o papel, pela primeira vez o próprio forecast de 7 dias do sistema concorda com a
continuidade (central 1.205,29, acima do fechamento de hoje) — o trade deixa de depender
apenas da leitura fundamentalista (calor + China + básis físico) e passa a ter também o
argumento estatístico a favor. Para quem tem física para fixar, o básis de Paranaguá segue
pagando prêmio crescente sobre a paridade teórica (R$ 139,71 vs R$ 135,68, +R$ 4,03/saca) —
a melhor janela de venda à vista documentada na série, agora em sua terceira confirmação. O
gatilho que decide os próximos dias continua sendo duplo: (1) se o volume de hoje se repete
ou recua no próximo pregão, e (2) o WASDE de julho (~10/07), a três dias.

---

## Farelo

**Viés: bear estrutural, agora na confirmação mais forte da série — ratio Far/Soj fechou em
79,11% pelo TERCEIRO pregão consecutivo abaixo de 80% (06/07: 79,28%; 07/07: 79,46%; 08/07:
79,11%), tratando a fila `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`,
agora D+27; mas o dia fecha em volume que colapsou -94,2% frente a ontem, o que exige cautela
na leitura de magnitude do movimento**

### Tratando a fila `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`

A pergunta que a fila cobra, pela segunda vez consecutiva (ela reaparece na fila de hoje mesmo
após a leitura de ontem tê-la tratado como "confirmada"): "ratio fechou <80%? WASDE mudou o
quadro? NOPA confirmou crush?" **Resposta: sim ao primeiro de forma ainda mais robusta, os
outros dois seguem pendentes.** A trajetória completa do ratio, com o terceiro fechamento
consolidando a compressão:

| Data-base | Ratio Far/Soj | Evento |
|---|---|---|
| 11/jun | 81,4% | origem da tese |
| 01/jul | 80,82% | recuando, ainda acima de 80% |
| 02/jul | 80,66% | a 0,66 p.p. do gatilho |
| 03-05/jul | sem sessão | mercado fechado (feriado + fim de semana) |
| 06/jul | 79,28% | primeiro fechamento abaixo de 80% |
| 07/jul | 79,46% | segundo fechamento seguido abaixo de 80% (valor recalculado hoje, ver Honestidade #1) |
| **08/jul** | **79,11%** | **terceiro fechamento seguido abaixo de 80% — nova mínima do ciclo** |

O protocolo original de 11/06/2026 (documentado em
[[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]) definia o gatilho como "ratio
sustentado abaixo de 80% por 2-3 pregões consecutivos". Com três fechamentos seguidos e o
terceiro sendo a mínima do ciclo (79,11%, mais comprimido que os dois anteriores), a tese passa
de "confirmada" para **"confirmada com continuidade"** — o mercado não apenas cruzou o gatilho,
está aprofundando a compressão. **O WASDE ainda não mudou o quadro** (o próximo é ~10/07,
ainda três dias) e **a NOPA segue sem confirmar nada**: a fila de hoje traz um novo item,
`release-nopa-2026-07-08`, sinalizando "release novo" — mas o campo `monthly_status` continua
em **0,0 bool** (indicadores, 08/07/2026), a mesma barreira de membership pago documentada
desde o início de junho. O "release novo" da fila aparentemente reflete apenas uma atualização
de timestamp de coleta, não um dado interpretável novo (ver Honestidade #3).

**O mecanismo por trás da compressão de hoje é distinto dos dois dias anteriores.** Em 07/07 o
farelo tinha subido mais rápido que a soja no dia anterior (mecanismo de convergência lenta);
hoje o padrão se inverte de forma mais direta: **o farelo caiu -0,25% (316,20 → 315,40)
enquanto a soja subiu +0,19% (1.193,75 → 1.196,00)** — os dois lados da equação empurrando o
ratio para baixo simultaneamente, o mecanismo mais "limpo" de compressão observado até aqui na
série (antes, a compressão vinha de o farelo subir menos que a soja; hoje o farelo efetivamente
recuou em termos absolutos).

**A crush margin subiu para 2,6073 USD/bu** (Board Crush: farelo 315,40 + óleo 69,35 − soja
1.196,00; indicadores, 08/07/2026), uma alta de **+1,70%** frente aos 2,5638 recalculados para
07/07. Olhando a janela mais recente com os valores hoje disponíveis: 2,4974 (06/jul) → 2,5638
(07/jul) → **2,6073 (08/jul)**, uma recuperação de **+4,40%** em duas sessões desde a mínima
local de 06/07 — um quadro de estabilização/recuperação, não de compressão adicional (ver
Honestidade #1 para a ressalva sobre por que esse valor de 07/07 difere do citado na leitura
de ontem). Isso é relevante para o risco de "esmagadora reduz ritmo": com a crush se
recuperando, o incentivo a esmagar segue intacto, o que sustenta a oferta de farelo no mercado
— reforçando, não contrariando, a tese bearish de excesso de oferta.

**As praças físicas de farelo no Brasil (NAG, 07/07/2026)** seguem paradas: MT/IMEA em R$
1.554,53/ton (estável), Rondonópolis em R$ 1.550,00/ton (estável, sem a alta de +3,33% vista
entre 03 e 06/07), RS em R$ 1.640,00/ton (estável). O prêmio de exportação do farelo em
Paranaguá segue em **+0,05 USD/sht** (julho/26) — inalterado, confirmando que o Brasil segue
sem vantagem de preço para exportar farelo.

**Os dados projetados da ABIOVE (sem alteração desde a leitura anterior)** continuam mostrando
a exportação de farelo brasileiro recuando pela metade entre agosto e dezembro/2026: 1.400 →
1.100 → 850 → 800 → 700 mil t, sem queda proporcional no estoque final projetado (1.224 →
1.016 → 1.100 → 1.101 → 1.015 mil t). O mecanismo segue intacto: menos saída pelo porto
empurra o excedente de farelo para o mercado interno de ração, pressionando o preço doméstico
— coerente com a compressão do ratio confirmada pela terceira vez hoje.

**A curva forward do farelo (08/07/2026)** — nota-se que o vencimento de julho (N26) não
aparece nas linhas disponíveis do dump de hoje (ver Honestidade #4), então a curva visível
começa em agosto:

| Vencimento | Código | Preço (USD/sht) | Var. vs Ago |
|---|---|---|---|
| Agosto/26 | Q26 | 315,40 | — (spot) |
| Setembro/26 | U26 | 313,30 | −2,10 |
| Outubro/26 | V26 | 311,60 | −3,80 |
| Dezembro/26 | Z26 | 314,80 | −0,60 |
| Janeiro/27 | F27 | 315,90 | +0,50 |

Outubro (V26, 311,60) permanece o vencimento mais descontado — coincide com o pico sazonal de
esmagamento simultâneo Brasil + Argentina (ABIOVE projeta 2.846 mil t de esmagamento BR em
outubro).

**O posicionamento dos fundos (COT, ainda em 30/06/2026, sem atualização nova)** mantém o
quadro já descrito ontem: managed money net long colapsado para +4.740 contratos (long
110.069, short 105.329, 17,9% do OI de 588.519) — os fundos já vinham ampliando a aposta
vendida antes mesmo do ratio confirmar a compressão pela primeira vez, e a confirmação de hoje
(terceiro fechamento) reforça esse alinhamento sem que ainda haja dado fresco de COT para medir
se eles aumentaram a posição vendida na semana do rali.

**O forecast estatístico de 30 dias do farelo aprofundou a divergência com a tese
fundamentalista:** central 30d = **327,16 USD/sht** (08/07, bandas 297,88-356,45, viés
altista), subindo de 320,53 (07/07) e 312,43 (06/07, lateral) — a terceira alta seguida do
centro projetado, na mesma janela em que o ratio confirma compressão pela terceira vez. O
forecast de 7d também mudou: central **317,54 USD/sht** (08/07, bandas 303,39-331,68), viés
**altista**, revertendo do viés lateral que tinha ontem (central 314,60). **Esta é a tensão
mais importante da leitura de hoje**: o modelo estatístico (baseado em média móvel, volatilidade
e inclinação recente, sem fundamento embutido) está diretamente na contramão da tese
fundamentalista bearish em AMBOS os horizontes agora, não apenas no de 30 dias como em leituras
anteriores. Isso não invalida a tese — o ratio, a ABIOVE e o COT seguem alinhados no bear — mas
é um sinal de alerta crescente que merece acompanhamento muito próximo nas próximas sessões.

### O que invalida / risco para o farelo

- **O forecast de 7d E 30d terem virado altista simultaneamente (317,54 e 327,16):** a
  divergência entre modelo estatístico e tese fundamentalista se ampliou hoje, não reduziu —
  o item de maior atenção da leitura.
- **Volume de 2.204 contratos hoje, uma queda de -94,2% frente aos 37.840 de ontem:** um
  movimento de preço em volume tão baixo carrega menos convicção — se o próximo pregão
  reverter o ratio para cima em volume também baixo, a "confirmação" de hoje perde força
  retroativamente.
- **Crush margin em recuperação (+4,40% em duas sessões):** reduz o risco de a esmagadora
  reduzir ritmo, mas também significa que a compressão do ratio não está vindo de um farelo
  mais escasso — está vindo de o farelo ficar mais barato relativamente à soja mesmo com
  esmagamento sustentado, o que é consistente com a tese, mas vale monitorar se a margem
  continuar subindo até o ponto de estimular esmagamento agressivo demais (efeito ambíguo).
- **WASDE de julho (~10/jul) reduzir a área de soja americana de forma expressiva:** menos
  esmagamento no 4T26 → menos farelo global, risco de aperto mesmo com os fundos vendidos.
- **NOPA seguir inacessível indefinidamente:** o "release novo" da fila de hoje não trouxe
  dado interpretável — a lacuna de confirmação direta de esmagamento americano persiste.

### Leitura operacional — farelo

A tese nascida em 11/06/2026 está agora na sua confirmação mais robusta: três fechamentos
consecutivos do ratio Far/Soj abaixo de 80%, com o terceiro sendo a mínima do ciclo (79,11%),
e o mecanismo de hoje (farelo caindo em termos absolutos enquanto a soja sobe) é o sinal mais
"limpo" de compressão observado na série. Para quem opera o spread de convergência (long
farelo/short soja, ou o crush completo), a tese segue com viés de gerenciar continuidade, não
de aguardar confirmação adicional. O contraponto que exige atenção redobrada é o forecast
estatístico: pela primeira vez, tanto o horizonte de 7 dias quanto o de 30 dias viraram
altistas no mesmo dia em que o fundamento bearish se aprofunda — e o volume de hoje (2.204
contratos, -94,2%) é baixo demais para tratar o movimento de preço isolado como uma confirmação
de alta convicção por si só. A recomendação é a mesma de ontem, reforçada: não ampliar posição
de forma agressiva sem ver o próximo pregão confirmar tanto o ratio abaixo de 80% quanto um
volume mais robusto. Para quem já está posicionado no short estrutural em preço absoluto,
referência de stop em 316-318 USD/sht (a curva de forecast de 7d, com banda alta em 331,68,
sugere que um stop mais largo pode ser necessário se a divergência estatística se traduzir em
preço nos próximos dias).

---

## Óleo

**Viés: bear tático, ainda intacto no nível de preço, mas com a primeira fissura de força
relativa desde a quebra do suporte — fechamento de 69,35 cts/lb segue abaixo do suporte-virou-
resistência 72,00 (fila `alerta-quebra_suporte-oleo_cbot-2026-07-08`), mas a alta do dia
(+1,11%) foi a maior das três pernas do complexo, maior até que a da soja**

### Tratando a fila `alerta-quebra_suporte-oleo_cbot-2026-07-08`

O óleo de agosto (ZLQ26.CBT) abriu em 69,01, fez máxima de 69,75, mínima de 68,87 e fechou em
**69,35 cts/lb** (CBOT CME, 08/07/2026, volume 4.667 contratos) — uma alta de **+0,76 cts
(+1,11%)** frente ao fechamento de 07/07 (68,59, via indicadores). A pergunta operacional da
fila — confirma ou muda a tese? — **confirma no nível de preço, mas com um sinal tático novo**:
o óleo está **3,68% abaixo** do nível de 72,00 (menor distância percentual que os 5,63% de
ontem, já que o próprio óleo subiu mais que o suporte se moveu), e pela primeira vez desde a
quebra do suporte, o óleo **liderou a alta percentual do complexo no dia** — mais que a soja
(+0,19%) e muito mais que o farelo (que caiu -0,25%). Ainda não é um teste da resistência, mas
é o primeiro dia em que a força relativa do óleo dentro do complexo vira positiva de forma
clara, depois de semanas de a soja e o farelo puxarem o rali enquanto o óleo ficava para trás.

**A margem de biodiesel americano comprimiu para 0,5177 USD/galão** (indicadores, 08/07/2026:
receita 6,5189 = HO 3,3539 + 1,5×RIN 2,11; custo 6,00 = óleo 5,2012 + industrial 0,80), uma
queda de -0,9% frente aos 0,5225 recalculados para 07/07 — uma compressão bem mais modesta que
a de -10,1% entre 06/07 e 07/07 nos valores recalculados de hoje (ver Honestidade #1). O
mecanismo: tanto a receita (heating oil subiu de 3,3017 para **3,3539 USD/galão, +1,58%**)
quanto o custo (óleo subiu 1,11%) avançaram hoje, mas a receita cresceu proporcionalmente mais
que o custo em termos absolutos de contribuição, então a margem só cedeu marginalmente. Olhando
a janela recente com os valores de hoje: 0,5814 (06/jul) → 0,5225 (07/jul) → **0,5177 (08/jul)**
— dois recuos seguidos, agora **na borda inferior da faixa de conforto de 0,50-0,80 USD/gal**
já documentada em leituras anteriores, com apenas 0,018 USD/gal de folga sobre o piso de 0,50.
Esta é a margem mais comprimida da série recente e merece ser tratada como o gatilho tático de
maior sensibilidade agora, mais do que em qualquer leitura anterior.

**A curva forward do óleo (08/07/2026)** mantém backwardation clara:

| Vencimento | Código | Preço (cts/lb) | Var. vs Ago |
|---|---|---|---|
| Julho/26 | N26 | 69,47 | +0,12 |
| Agosto/26 | Q26 | 69,35 | — (spot) |
| Setembro/26 | U26 | 68,89 | −0,46 |
| Outubro/26 | V26 | 68,43 | −0,92 |
| Dezembro/26 | Z26 | 68,06 | −1,29 |
| Janeiro/27 | F27 | 67,93 | −1,42 |

A curva caindo -1,42 cts/lb (-2,0%) de agosto a janeiro/27 é levemente mais acentuada que os
-1,27 cts/lb de ontem — segue sendo o argumento técnico mais forte para manter posição vendida
de médio prazo via carry, mesmo com a alta pontual de hoje.

**O posicionamento dos fundos (COT, ainda em 30/06/2026, sem atualização nova)** mantém o
quadro de de-risking já descrito: managed money net long em +91.946 contratos (14,6% do OI),
uma queda de -10,9% frente a 23/06 que antecedeu o rali dos últimos pregões — sem dado fresco
para confirmar se os fundos aproveitaram a alta de hoje para reduzir ainda mais a posição ou
se estão recompondo.

**O Índice de Suporte do Óleo (ISO) permanece em 100/100 (5/5 condições)**, agora a nona sessão
seguida nesse patamar desde a virada de 01/07 (indicadores, 08/07/2026) — mantendo a hipótese
de efeito calendário já discutida em leituras anteriores (ver Honestidade #5).

**O pano de fundo regulatório global segue inalterado desde 05/06/2026**
(`system/tributario_watch.toml`, sem novos `atualizado_em`): EPA Final RFS 2026/2027 sustenta
o RIN D4, o crédito 45Z tende a favorecer óleo doméstico americano, e a Indonésia mantém a
exportação de palma centralizada via Danantara mais o levy de exportação de CPO — mas segue
impossível quantificar porque o MPOB está inacessível há 23 dias consecutivos.

### O que invalida / risco para o óleo

- **Margem de biodiesel em 0,5177 USD/gal, com apenas 0,018 de folga sobre o piso de 0,50:**
  o item de maior sensibilidade tática da leitura de hoje — se cair abaixo de 0,50 no próximo
  pregão, a pressão sobre o custo de produção de biodiesel aumenta e reduz o incentivo a
  consumir óleo como insumo, potencialmente pressionando ainda mais o preço.
- **O óleo ter liderado a alta percentual do complexo hoje:** primeiro sinal de força relativa
  positiva desde a quebra do suporte — se repetir por mais 1-2 sessões, pode anteceder um teste
  real da resistência de 72,00, o que mudaria a tese tática.
- **Heating oil não sustentar a alta de hoje (+1,58%):** se recuar amanhã enquanto o óleo segue
  subindo, a margem de biodiesel aperta ainda mais rápido.
- **RIN D4 real acima de 2,40 USD/RIN** (o modelo usa 2,11 fixo): incerteza estrutural
  bidirecional, sem novo dado hoje.
- **Dados de palma malaia (MPOB) inacessíveis há 23 dias consecutivos** — segue impossível
  avaliar o efeito de El Niño ou das restrições indonésias sobre o prêmio de substituição.
- **WASDE de julho reduzir a área de soja americana:** menos esmagamento futuro → menos óleo
  produzido → altista para os contratos de novembro em diante.

### Leitura operacional — óleo

O viés segue bear tático — a quebra do suporte 72,00 permanece confirmada, e o óleo ainda não
testou a resistência. Mas o dia de hoje registra o primeiro sinal de força relativa positiva
desde que o suporte foi rompido: o óleo subiu mais que a soja e mais que o farelo, na direção
oposta à liderança que vinha sendo da soja e do farelo nas últimas sessões. Isso não é motivo
para desmontar a tese bear tática — o nível de preço segue abaixo da resistência e a curva
forward segue em backwardation —, mas é motivo para reduzir o tamanho de posições vendidas
adicionais até ver se o padrão se repete. A margem de biodiesel, agora colada no piso de 0,50
USD/gal (0,5177, com apenas 0,018 de folga), é o gatilho tático mais sensível da leitura: uma
ruptura desse piso tende a coincidir com pressão adicional sobre o preço do óleo, mas também
pode ser o ponto em que a demanda industrial de biodiesel passa a competir mais agressivamente
pelo insumo, criando suporte de preço por outro canal. Referência de stop para posição vendida
em 70,00-71,00 cts/lb (ajustada para baixo frente aos 69,50-70,50 de ontem, dado o rali de
hoje). Para quem opera o oil share (hoje em 52,37%, subindo de 52,03% ontem), o viés estrutural
segue favorecendo manter exposição ao óleo dentro do crush frente ao farelo.

---

## Spreads e crush — leitura de complexo

### Crush margin: 2,6073 USD/bu — segunda alta seguida, +4,40% desde a mínima de 06/07

A crush está em **2,6073 USD/bu** (Board Crush: farelo 315,40 + óleo 69,35 − soja 1.196,00;
indicadores, 08/07/2026), subindo +1,70% frente aos 2,5638 recalculados para 07/07 — a segunda
alta consecutiva usando os valores do dump de hoje: 2,4974 (06/jul, mínima do ciclo recente) →
2,5638 (07/jul) → **2,6073 (08/jul)**, uma recuperação de +4,40% em duas sessões. O sinal é de
estabilização/recuperação da margem, não de compressão adicional — reduz o risco de a
esmagadora reduzir ritmo de esmagamento no curto prazo, o que sustenta a oferta física de
farelo e óleo simultaneamente (reforçando o bear-farelo, sem contradizer o bear-óleo tático).

### Ratio Far/Soj: 79,11% — TERCEIRO fechamento seguido abaixo de 80%, nova mínima do ciclo

Como detalhado na seção de Farelo, o ratio aprofundou a compressão hoje, com o mecanismo mais
"limpo" da série (farelo caindo em termos absolutos enquanto a soja sobe). É a confirmação mais
robusta da tese de 11/06 até aqui, tratando a fila
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`.

### Oil share: 52,37% — subindo pelo segundo dia

O oil share está em 52,37%, subindo de 52,03% ontem e 51,99% em 06/07 — o óleo ampliando
ligeiramente sua participação no valor total do crush, coerente com a força relativa positiva
observada no preço do óleo hoje.

### Oil-meal spread: 0,6897 USD/bu — salto expressivo

O oil-meal spread (contribuição do óleo menos a do farelo por bushel) saltou para 0,6897 ante
0,5885 recalculados para ontem — um avanço de +17,2%, o maior movimento de um dia para o outro
nesta métrica na série recente, refletindo diretamente a combinação de óleo subindo e farelo
caindo hoje.

### ISF em 80/100, ISO em 100/100 — nono pregão seguido no mesmo patamar

O Índice de Sobra de Farelo (ISF) está em 80/100 (4/5 condições) e o Índice de Suporte do Óleo
(ISO) em 100/100 (5/5) — o mesmo patamar desde 01/07/2026, agora o nono dia consecutivo
(contando os dias de calendário registrados no dump, incluindo os de mercado fechado).

### O que os índices dizem juntos em 08/07/2026

ISF 80/100 + ISO 100/100 (ambos estáveis, efeito calendário) + ratio Far/Soj na mínima do ciclo
pelo terceiro fechamento seguido (79,11%) + oil share subindo pelo segundo dia (52,37%) +
oil-meal spread saltando +17,2% + crush margin em recuperação (+4,40% em duas sessões) + margem
de biodiesel colada no piso de conforto (0,5177, folga de apenas 0,018) + soja rompendo 1.180
pela terceira vez seguida em volume forte (7.558 contratos, dobrando frente a ontem) + farelo
em volume quase inexistente (2.204, -94,2%) + óleo liderando a alta percentual do complexo pela
primeira vez desde a quebra do suporte:

A leitura de hoje é de **confirmação estrutural mais forte ainda no bear-farelo, com o bear-
óleo tático permanecendo intacto mas mostrando a primeira fissura de força relativa, e o
bull-soja tático ganhando o reforço de volume que faltava.** O desenvolvimento central da série
(o ratio comprimindo, agora pela terceira vez seguida) aprofunda-se exatamente no dia em que o
volume do próprio farelo despenca — um lembrete de que a magnitude do movimento de hoje deve
ser lida com desconto, mesmo que a direção estrutural (ratio, ABIOVE, COT) permaneça alinhada.
O contraponto mais importante da leitura, ampliado frente a ontem, é o forecast estatístico:
tanto o horizonte de 7 dias quanto o de 30 dias do farelo agora projetam alta, uma divergência
que cresce exatamente no dia em que o fundamento bearish mais se confirma — a régua de gestão
de risco deve continuar alta, não relaxar.

---

## Lente fiscal e regulatória BR

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L) — vence em 3 dias
(11/07/2026, fila `trib-MP-1358-2026-2026-07-11`).** Sem mudança desde a última leitura
(`system/tributario_watch.toml`, evento MP-1358-2026, `atualizado_em` 2026-06-05, status
"tramitacao", `proximo_marco` = "Deliberação comissão mista", `proximo_data` = 2026-07-11). A
MP ressarce PIS/Cofins/Cide da gasolina e do diesel, mantendo o combustível fóssil
artificialmente mais barato — o mesmo espírito da MP 1.363/2026 (subsídio de R$ 1,12/L ao
diesel, vigente até 31/12/2026, já tratada em
[[2026-05-26_subvencao-fossil-aperta-biodiesel]]). O mecanismo de transmissão para o complexo
soja é indireto mas real: enquanto o combustível fóssil segue subsidiado, a competitividade
relativa do biodiesel dentro do mix B15 mandatório permanece pressionada, mantendo a margem da
indústria de biodiesel (maior consumidora industrial de óleo de soja no Brasil) mais apertada
do que teria sem a subvenção ao concorrente fóssil. Esse marco cai três dias antes do WASDE de
julho (~10/07) e a apenas 20 dias do vencimento da isenção PIS/Cofins do biodiesel (31/07) —
a janela de 09-11/07 concentra dois catalisadores relevantes em sequência imediata. Se a MP
1.358 caducar sem conversão em lei, é um sinal (fraco, mas real) de perda de fôlego político do
pacote pró-fóssil — levemente positivo para a competitividade do biodiesel e, por extensão,
para a demanda industrial de óleo de soja; se for convertida, reforça o quadro de pressão já
documentado desde maio.

**Isenção PIS/Cofins biodiesel — vencimento em 31/07/2026, 23 dias.** Sem sinalização pública
de renovação até hoje (`system/tributario_watch.toml`, evento PISCOFINS-BIODIESEL-ISENCAO,
`atualizado_em` 2026-06-05, sem mudança). O checkpoint D+45 desse insight
([[2026-05-26_pis-cofins-biodiesel-explica-mercado-fisico-fraco]]) caiu em 09/07/2026 — a um
dia de distância — coincidindo com a janela de decisões da MP 1.358 e o WASDE.

**B16 — sem data, travado em B15.** Sem mudança de status (evento B16-CNPE-2026,
`atualizado_em` 2026-06-05, status "adiado", sem `proximo_data`).

**MP 1.363/2026 (subsídio ao diesel fóssil) — em vigor até 31/12/2026.** Sem alteração.
Bearish estrutural persistente para a demanda incremental de óleo de soja no mercado doméstico
brasileiro.

**STJ REsp 2.165.276/2026 — crédito PIS/Cofins para esmagadoras.** Sem alteração. Bullish para
a soja/óleo (alívio de custo de entrada para biodiesel) e, por extensão, incentivo a mais
esmagamento — coerente com mais oferta de co-produtos, reforçando a leitura bearish do farelo.

**Câmbio (PTAX) publicou novo dado para 07/07/2026 (5,1458 BRL/USD), a quinta sessão seguida
de apreciação do real** — já tratado na seção de Soja. O impacto fiscal indireto (real mais
forte reduz o custo em reais de insumos importados usados na cadeia, mas também reduz a
paridade de exportação em reais) segue neutro na margem, sem mudança de regime.

**Pano de fundo regulatório global (EUA e Indonésia) segue dando suporte estrutural ao óleo,
sem contradizer o viés bearish tático** — detalhado na seção Óleo.

---

## Riscos e eventos próximos

**WASDE de julho — ~10/07/2026 (2 dias).** Primeiro WASDE do mês, cai dois dias antes do
vencimento da MP 1.358 e um dia depois do checkpoint D+45 da tese PIS/Cofins — janela de três
catalisadores em sequência imediata (09-11/07).

**Vencimento da MP 1.358/2026 — 11/07/2026 (3 dias), fila `trib-MP-1358-2026-2026-07-11`.**
Deliberação da comissão mista é o marco a monitorar.

**Isenção PIS/Cofins biodiesel — vencimento 31/07/2026 (23 dias).** Sem sinalização de
renovação até agora.

**COT CFTC — dado de 30/06/2026 ainda não captura a reação dos fundos ao rali de 06-08/07.**
A próxima atualização é o teste real de como o "dinheiro grande" reagiu à terceira confirmação
do ratio, ao rompimento sustentado da soja e à fissura de força relativa do óleo.

**Forecast de 7d E 30d do farelo viraram altista simultaneamente hoje — a divergência entre
modelo estatístico e tese fundamentalista se ampliou, não reduziu, no dia da confirmação mais
forte do ratio.** É o item de maior atenção para as próximas 2-3 sessões.

**Margem de biodiesel em 0,5177 USD/gal, com apenas 0,018 de folga sobre o piso de 0,50 USD/gal
— o item de maior sensibilidade tática de curto prazo do óleo, mais urgente que em qualquer
leitura anterior.**

**Volume do farelo colapsou -94,2% hoje (2.204 vs 37.840 contratos) — monitorar se o próximo
pregão recupera participação ou se o mercado do farelo entrou em compasso de espera pré-WASDE.**

**USDA Crop Progress — próximo relatório semanal (~13/07) é o teste direto da narrativa de
"calor nos EUA" que sustentou parte do rali da soja, sem atualização desde 05/07.**

**NOPA — segue inacessível (fila `release-nopa-2026-07-08` tratada aqui, sem dado
interpretável apesar do "release novo" sinalizado), 23º dia sem crush americano confirmado por
fonte primária.**

**MPOB — 23 dias consecutivos sem números de palma extraídos**, mantendo cego o efeito da
Indonésia e do El Niño sobre o prêmio de substituição do óleo de soja.

---

## Honestidade

O que não foi possível validar neste briefing de 08/07/2026, onde a confiança é baixa ou há
lacunas materiais:

**1. O padrão de revisão retroativa de indicadores entre dumps de dias diferentes continua,
mas parte dele agora tem explicação mais clara.** A leitura de 07/07
([[2026-07-07_leitura-complexo]]) registrou, para aquele dia, soja em 1.186,25 cts/bu, farelo
em 313,50 USD/sht, óleo em 67,95 cts/lb, crush margin em 2,509 USD/bu e margem de biodiesel em
0,5612 USD/gal. O dump de hoje, ao recalcular a mesma data (07/07/2026), mostra soja em
1.193,75, farelo em 316,20, óleo em 68,59, crush margin em 2,5638 e margem de biodiesel em
0,5225 — valores sensivelmente diferentes em quase todos os campos, não apenas em paridade
cambial. Para a **paridade em reais** especificamente, uma parte da diferença tem explicação
plausível: os indicadores parecem recalcular o valor histórico usando a PTAX mais fresca
disponível no momento da geração do dump (T+1), então o valor de "07/07" muda quando a PTAX de
07/07 chega ao sistema — isso explica por que a paridade de 07/07 aparece diferente entre as
duas leituras. **Mas essa explicação não cobre a diferença nos preços de fechamento do CBOT em
si** (soja, farelo, óleo), que não dependem de câmbio — a causa dessa parte da discrepância
segue sem explicação acessível a partir do dump (possivelmente correção de settle após
publicação inicial, ou diferença entre preço intradiário e fechamento oficial). Como nas
leituras anteriores, esta leitura usa os números do dump de hoje como referência para todas as
comparações dia-a-dia, por serem internamente consistentes entre si — mas as variações
percentuais "08/07 vs 07/07" citadas aqui carregam essa incerteza de base.

**2. Volume de soja e óleo para 07/07/2026 não está disponível nas linhas visíveis do dump de
hoje.** A comparação de volume da soja (7.558 hoje vs "3.640" citado pela leitura de ontem) usa
um número que vem de uma fonte diferente (o dump de 07/07, lido pela leitura daquele dia), não
do dump de hoje — o dump de hoje republica apenas o volume de farelo para 07/07 (37.840,
confirmado, permitindo a comparação limpa de -94,2% usada na seção de Farelo). A direção do
sinal (mais volume na soja hoje que ontem) é consistente com o padrão observado, mas a
magnitude exata de +107,6% deve ser tratada com a mesma cautela do item 1.

**3. NOPA — fila sinalizou "release novo" (`release-nopa-2026-07-08`), mas o `monthly_status`
continua em 0,0 bool** (indicadores, 08/07/2026), a mesma barreira de membership pago
documentada desde início de junho. O "release novo" provavelmente reflete apenas um novo
timestamp de coleta do scraper, não um dado interpretável — não foi possível confirmar isso
além da leitura do campo `monthly_status`.

**4. Curva forward do farelo sem o vencimento de julho (N26) no dump de hoje.** Diferente de
ontem (quando N26 aparecia em 318,40), o dump de 08/07 não lista `fechamento_N26` para o
farelo — possivelmente porque o contrato de julho está próximo do vencimento/entrega e deixou
de ser cotado de forma regular, mas não há confirmação direta disso no dump.

**5. A atribuição da virada do ISF/ISO ao efeito calendário ABIOVE segue sem confirmação
direta no banco de dados**, mantida como inferência lógica bem fundamentada (agora reforçada
pela estabilidade de nove sessões seguidas no mesmo patamar), não uma verificação de código.

**6. COT com defasagem de mais de uma semana em relação ao rali de 06-08/07/2026.** O dado mais
recente (30/06/2026) mostra os fundos reduzindo long em óleo e ampliando short em farelo, mas
não captura a reação a esta semana inteira, incluindo a fissura de força relativa do óleo
observada hoje.

**7. Palma malaia (MPOB) — 23 dias consecutivos sem dados numéricos** (16/jun a 08/07/2026). O
parser continua retornando apenas ~3.437 chars de HTML sem valores extraídos.

**8. RIN D4 como parâmetro fixo (2,11 USD/RIN) segue sendo a maior fonte de incerteza do
modelo de biodiesel**, especialmente relevante agora que a margem calculada está colada no piso
de 0,50 USD/gal — um RIN D4 real diferente do valor fixo mudaria materialmente a leitura de
quão perto do piso a margem realmente está.

**9. Percentis históricos de COT não calculados** — os 91.946 net longs em óleo, 4.740 em
farelo (com 105.329 shorts) e 38.149 em soja seguem lidos apenas em nível absoluto e como
fração do open interest corrente, sem série histórica completa para calibrar se estão em zona
extrema.

**10. BCBA Argentina — sem relatórios de esmagamento/exportação acessíveis via scraper**
(page_fetched=1,0 mas sem links de relatório, 06/07/2026, sem atualização). O ritmo de
processamento argentino pós-colheita (50,1 mi t) é estimado por notícia, não medido por fonte
primária.

**11. Dados de clima INMET (BR) não foram usados como driver desta leitura.** Julho é
entressafra da soja brasileira (colheita já concluída, plantio só em outubro) — as
temperaturas de Cascavel/PR, Cuiabá/MT, Sinop/MT etc. no dump são monitoramento de rotina, sem
relevância direta para a tese de preço neste momento do calendário agrícola.

*Nenhum número foi inventado ou estimado além do que consta no briefing de 08/07/2026 e nos
insights anteriores referenciados. A maior contribuição desta leitura foi identificar que o
ratio Far/Soj chegou ao terceiro fechamento consecutivo abaixo de 80% (nova mínima do ciclo em
79,11%) exatamente no dia em que o volume do farelo colapsou -94,2% e o forecast estatístico
de 7 E 30 dias virou simultaneamente contra a tese — documentando, com a mesma transparência
das leituras anteriores, que confirmação estrutural e baixa liquidez/divergência estatística
podem coexistir no mesmo pregão, o que pede gestão de risco mais cautelosa, não menos, à medida
que a tese "confirma" repetidamente.*
