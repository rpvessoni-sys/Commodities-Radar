---
data: 2026-07-11
titulo: "Com N26 de volta às curvas de soja e farelo (dado limpo, sem ambiguidade de rolagem), a fila confirma os dois alertas técnicos pendentes — soja rompeu 1.180,00 (fechou 1.191,75) e óleo perdeu 72,00 (fechou 70,46) — e o COT, atualizado pela primeira vez em oito sessões (dado de 07/07), mostra fundos comprando soja (+82% na semana) e farelo (+295%) e reduzindo óleo (-7,6%); o ratio Far/Soj fechou acima de 80% em duas sessões consecutivas e limpas, derrubando a confiança no gatilho tático que sustentava o bear-farelo desde 11/06, mesmo com o fundamento ABIOVE intacto; o WASDE apareceu como fonte pela primeira vez mas só traz farelo Argentina/Brasil (sem revisão jun→jul) e nenhum dado de soja ou óleo dos EUA"
tags: [complexo, auto-claude]
fontes:
  - CBOT CME (ZSQ26/ZMQ26/ZLQ26 + curva forward completa + HO=F) — sessão de 2026-07-10 (última sessão disponível; 2026-07-11 é sábado, sem pregão)
  - CFTC COT Managed Money — dado de referência 2026-07-07 (primeira atualização em oito sessões, publicada 2026-07-10)
  - BCB PTAX — 2026-07-10 (USD/BRL 5,1088; EUR/BRL 5,8434; Selic 0,052531% a.a.)
  - CEPEA/ESALQ Paranaguá e Paraná interior via NAG — 2026-07-10
  - NAG Físico BR (farelo MT/IMEA, RS, Rondonópolis; prêmios export PGUA farelo/óleo) — 2026-07-10
  - USDA Crop Progress — 2026-07-05 (sem atualização; próximo relatório semanal ~2026-07-13)
  - NOAA CPC ENSO — 2026-07-11 (El Niño Advisory, sem mudança)
  - ABIOVE projeções mensais — balanços ago-dez/2026 (farelo/óleo/soja), sem alteração
  - USDA WASDE — 2026-07-10 (nova fonte no briefing; cobre apenas farelo Argentina/Brasil, e China parcial)
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, ISF/ISO, paridade BR) — 2026-07-10/11
  - MPOB — 2026-07-11 (sem números extraídos, mesmo bloqueio de semanas anteriores)
  - NOPA — 2026-07-11 (monthly_status inacessível, fila `release-nopa-2026-07-11`)
  - system/tributario_watch.toml — eventos MP-1358-2026 (vence hoje), MP-1363-2026, PISCOFINS-BIODIESEL-ISENCAO, STJ-RESP-2165276, B16-CNPE-2026, EPA-RFS-2026-2027, 45Z-CLEAN-FUEL, DANANTARA-INDONESIA, INDONESIA-B50, INDONESIA-LEVY-PMK9 (todos `atualizado_em` 2026-06-05)
  - Forecasts estatísticos internos — 2026-07-11 (recalibrados com o spot de 2026-07-10)
  - Cruza com [[2026-07-10_leitura-complexo]], [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]], [[2026-05-26_subvencao-fossil-aperta-biodiesel]], [[2026-05-26_pis-cofins-biodiesel-explica-mercado-fisico-fraco]], [[2026-05-26_b16-bullish-farelo]]
status: ativa
vies: [bull-soja, neutral-farelo, bear-oleo_soja]
---

## Visão geral

O complexo soja é uma fábrica com uma matéria-prima única — a soja em grão — e dois
produtos de saída fabricados em proporção fixa a cada bushel esmagado: o **farelo**
(fração proteica, ~78% da massa, vira ração animal) e o **óleo degomado** (fração de
gordura, ~18-20% da massa, vira óleo de cozinha e biodiesel). Quem decide o ritmo de
esmagamento é a esmagadora, olhando a **crush margin** (valor de farelo + óleo
produzidos por bushel, menos o custo daquele bushel de soja, medida na CBOT — Chicago
Board of Trade, a bolsa onde soja/farelo/óleo são negociados como futuros) e o **oil
share** (a fração desse valor capturada pelo óleo). Quando o óleo "paga o crush" a
esmagadora tem incentivo a esmagar a pleno vapor para capturar o valor do óleo e "deixa
sobrar" farelo como subproduto menos desejado, pressionando seu preço relativo. O
**ratio Far/Soj** (preço do farelo dividido pelo preço da soja, na mesma base) é o
termômetro dessa dinâmica: abaixo de 80% o farelo está "abundante" frente à soja, acima
de 87% estaria "apertado" — a faixa entre 80% e 87% é uma zona neutra, nem sobra nem
aperto claros.

**Hoje, 11/07/2026 (sábado, sem pregão novo — a última sessão disponível é a de
sexta-feira, 10/07), a leitura resolve a ambiguidade de dado que dominou a leitura de
ontem.** O contrato de julho/26 (N26), que havia desaparecido das curvas forward de
soja e farelo no dump usado ontem, **reapareceu hoje em ambas** — cotado a 1.196,50
cts/bu (soja) e 320,60 USD/short_ton (farelo), ambos com prêmio normal sobre o contrato
de agosto (Q26), que é hoje o "spot" de referência. O fechamento de 10/07 recalculado
neste dump é **soja 1.191,75 cts/bu, farelo 320,40 USD/sht e óleo 70,46 cts/lb** —
valores sensivelmente mais altos que os 1.170,00 / 315,50 / 69,86 usados na leitura de
ontem para a MESMA data-base. Com N26 de volta e um dado internamente consistente, os
dois alertas 🔴 da fila de hoje se confirmam sem ambiguidade: a **soja fechou ACIMA da
resistência de 1.180,00** (`alerta-quebra_resistencia-soja_cbot-2026-07-10`) e o
**óleo fechou ABAIXO do suporte de 72,00** (`alerta-quebra_suporte-oleo_cbot-2026-07-10`).
O segundo grande desenvolvimento do dia é o **COT (Commitment of Traders, relatório
semanal da CFTC — Commodity Futures Trading Commission — sobre o posicionamento dos
fundos)**, que finalmente atualizou depois de oito sessões travado em 30/06: o dado
novo, de referência 07/07/2026, mostra os fundos ("managed money") **comprando soja
(net long +82% na semana) e farelo (+295%, saindo de quase zero) e reduzindo a posição
comprada em óleo (-7,6%)** — uma rotação real de capital dentro do complexo. Isso
coincide com o **ratio Far/Soj fechando acima de 80% em duas sessões consecutivas e
agora limpas** (80,85% em 09/07 e 80,65% em 10/07, sem a ambiguidade de revisão
retroativa que contaminou a leitura de ontem), o que **derruba a confiança no gatilho
técnico específico** que vinha sustentando a tese de bear-farelo desde 11/06/2026
(`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`) — mesmo com o
fundamento estrutural da ABIOVE (Associação Brasileira das Indústrias de Óleos
Vegetais) intacto. Por fim, o **WASDE (World Agricultural Supply and Demand Estimates,
relatório mensal do USDA sobre oferta e demanda agrícola) apareceu pela primeira vez
como fonte de dado neste briefing** (`release-usda_wasde-2026-07-10`) — mas só traz
balanço de **farelo** para Argentina e Brasil (mais duas linhas truncadas da China),
sem nenhum número de soja ou óleo, e sem revisão de junho para julho nos números que
existem.

**Leitura de uma linha:** o pivô do complexo hoje é a resolução do dado — os dois
alertas técnicos da fila (soja acima de 1.180, óleo abaixo de 72,00) deixam de ser
suspeitos de artefato e passam a ser leituras confiáveis, e o COT finalmente fresco
mostra o "dinheiro grande" comprando o grão e o farelo enquanto reduz o óleo. Maior
convicção: a soja tem hoje o alinhamento mais forte de toda a semana entre nível
técnico, posicionamento de fundos e modelo estatístico, todos apontando para cima.
Confiança MODERADA-ALTA no bull-soja tático e no bear-óleo tático (curva em
backwardation, ISO em 100/100, mas margem de biodiesel perdendo folga). Confiança
BAIXA-MODERADA na tese estrutural de bear-farelo no curtíssimo prazo — o gatilho
técnico específico (ratio <80%) falhou com dado limpo, ainda que o argumento
ABIOVE (exportação caindo pela metade sem queda proporcional de estoque) siga de pé
como pano de fundo de médio prazo. O WASDE, esperado há um mês como catalisador,
chegou pela metade: farelo sim, soja e óleo continuam mudos.

---

## Soja

**Viés: bull tático — fechamento de 1.191,75 cts/bu confirma, com dado limpo (sem
ambiguidade de rolagem), o rompimento da resistência de 1.180,00, reforçado por fundos
comprando net long +82% na semana (COT, 07/07/2026), tratando a fila
`alerta-quebra_resistencia-soja_cbot-2026-07-10`**

### Tratando a fila `alerta-quebra_resistencia-soja_cbot-2026-07-10`

A soja de agosto (ZSQ26.CBT) abriu em **1.179,00**, fez mínima em **1.170,00**, máxima
em **1.197,25** e fechou em **1.191,75 cts/bu** (CBOT CME, 10/07/2026, volume **59.159
contratos** — um volume robusto, revertendo por completo o volume anormalmente baixo
documentado ontem, o que por si só já é um sinal de que a sessão de hoje é mais
confiável). Frente ao valor de 09/07 no mesmo dump (1.177,75 cts/bu), a variação foi de
**+14,00 cts (+1,19%)**. A resposta direta à pergunta da fila — "confirma ou muda a
tese?" — é que **confirma**: com o contrato de julho (N26) de volta à curva, cotado a
**1.196,50 cts/bu** com prêmio normal de +4,75 cts sobre o spot Q26, não há mais
ambiguidade sobre qual contrato está sendo usado como referência. O nível de 1.180,00
foi rompido de forma limpa.

**A curva forward de hoje (10/07/2026, agora completa)**:

| Vencimento | Código | Preço (cts/bu) | Var. vs Ago |
|---|---|---|---|
| Julho/26 | N26 | 1.196,50 | +4,75 |
| Agosto/26 | Q26 | 1.191,75 | — (spot) |
| Setembro/26 | U26 | 1.181,25 | −10,50 |
| Novembro/26 | X26 | 1.190,75 | −1,00 |
| Janeiro/27 | F27 | 1.204,75 | +13,00 |
| Março/27 | H27 | 1.207,50 | +15,75 |

A curva não é um contango puro: há um desconto de setembro (U26, pré-colheita
americana) frente a agosto, seguido de recuperação em novembro (X26, mês de colheita)
e alta mais firme até jan/mar-27 — um formato coerente com a sazonalidade normal da
safra americana, sem sinal de aperto físico imediato nem de esvaziamento de estoque.

**O câmbio (BCB PTAX) publicou 5,1088 BRL/USD para 10/07/2026**, ante 5,1329 em 09/07
— nova apreciação do real (**-0,47%**), a terceira sessão seguida de fortalecimento
cambial. O EUR/BRL também recuou, de 5,872 para 5,8434 (-0,49%), mesma direção. **A
paridade em reais oficial (indicadores, 10/07/2026) ficou em R$ 134,23/saca 60kg**
(CBOT 1.191,75 cts × PTAX 5,1088 BRL/USD, sem básis) — uma leve alta de +0,72% frente
aos R$ 133,27 de 09/07, com o efeito da soja mais cara em dólar superando o efeito do
real mais forte. **O básis físico do porto segue sendo o dado mais consistente da
leitura de soja**: a soja Paranaguá (CEPEA/ESALQ via NAG, 10/07/2026) fechou em **R$
140,44/saca** (+0,14% frente aos R$ 140,25 de 09/07) — comparando com a paridade teórica
de hoje, o **básis (prêmio do porto sobre a paridade) fica em +R$ 6,21/saca (+4,6%)**,
recuando um pouco frente aos +R$ 6,98/saca de 09/07 (usando a paridade de 09/07,
R$133,27), mas ainda claramente elevado frente à série da semana: **+R$ 4,29 (07/07) →
+R$ 4,79 (08/07) → +R$ 6,98 (09/07) → +R$ 6,21 (10/07)** — um alargamento líquido de
quase 45% do básis ao longo da semana, mesmo com a pequena reversão do último dia. A
soja Paraná interior (NAG, 10/07/2026) fechou em **R$ 132,58/saca** (-0,08% frente a
09/07) — abaixo da paridade teórica de hoje em **-R$ 1,65/saca**, um desconto (diferente
do porto), coerente com o interior tipicamente pagando menos que o ponto de exportação.

**A colheita argentina segue encerrada em 98%**, produção mantida em 50,1 milhões de
toneladas (Canal Rural, 27/06/2026, sem atualização) — teto estrutural regional
inalterado. BCBA segue acessível via scraper mas sem links de relatório detectado
(11/07/2026, sem mudança).

**O posicionamento dos fundos (COT, CFTC) finalmente atualizou, depois de oito sessões
travado em 30/06/2026** — o dado novo tem referência **07/07/2026** e é o
desenvolvimento mais importante desta seção: managed money **long em 146.672
contratos, short em 77.093, net long em +69.579 contratos** — um salto de **+82,4%**
frente aos +38.149 contratos de 30/06 (long 133.396, short 95.247). Como fração do
open interest, o net long subiu de **4,25% para 7,13%** do OI (975.954 contratos) —
ainda longe de um extremo histórico (não há série de percentis calculada, ver
Honestidade), mas uma mudança de magnitude relevante numa única semana de referência,
e que precede exatamente a semana em que o CBOT rompeu a resistência de 1.180,00.

**A condição de lavoura americana (USDA Crop Progress, 05/07/2026)** segue em 53% good
+ 11% excellent = **64% bom-ou-melhor**, 6% poor — sem atualização desde a leitura
anterior; o próximo relatório semanal (~13/07) é o teste direto do driver "calor nos
EUA" que vinha sendo citado como parte do rali.

**Os forecasts estatísticos internos (11/07/2026, recalibrados com o fechamento de
hoje)** subiram, coerente com o rompimento técnico: central 7d = **1.208,67 cts/bu**
(bandas 1.148,17-1.269,17), viés **altista**, subindo dos 1.188,36 da geração de
10/07. Central 30d = **1.276,55 cts/bu** (bandas 1.151,31-1.401,80), viés **altista**,
também subindo frente a 1.255,81. Hoje é o primeiro dia da semana em que nível técnico,
posicionamento de fundos e modelo estatístico apontam todos na mesma direção — o
alinhamento mais forte do complexo neste momento.

### O que invalida / risco para a soja

- **Um fechamento limpo abaixo de 1.180,00 no próximo pregão útil** (segunda-feira,
  13/07, já sem qualquer ambiguidade de rolagem, dado que N26 voltou) seria a primeira
  quebra genuína do nível — hoje esse risco está mais distante do que ontem, mas segue
  sendo o gatilho técnico a vigiar.
- **Nenhum WASDE de soja (EUA, Brasil ou Argentina) está disponível neste sistema** —
  o WASDE que apareceu hoje cobre apenas farelo (ver seção Farelo e Honestidade #1). A
  pergunta "oferta grande" que vem sendo levantada há semanas segue sem resposta.
- **A condição de lavoura (64% bom-ou-melhor, 05/07) piorar no relatório de ~13/07.**
- **O básis físico em Paranaguá (+R$ 6,21/sc) se dissipar** — já mostrou uma pequena
  reversão de -10% frente ao pico de ontem; se continuar recuando, enfraquece o
  argumento de demanda física forte no porto.
- **O COT (07/07) ser um pico isolado** — a próxima atualização (~14/07) precisa
  confirmar que os fundos continuaram comprando ao longo da semana corrente (06 a
  10/07), que ainda não está capturada neste dado.

### Leitura operacional — soja

Com o rompimento de 1.180,00 confirmado por dado limpo e reforçado por fundos
comprando net long +82% na semana, a leitura de hoje suporta um viés tático de alta no
papel, com stop de referência agora bem definido logo abaixo de 1.180,00 (um
fechamento limpo abaixo desse nível, sem ambiguidade de rolagem, inverteria a leitura).
A convicção não é máxima porque falta a confirmação fundamental do WASDE de soja, que
segue ausente do sistema — o movimento de hoje é majoritariamente técnico e de fluxo
(COT), não fundamentalista. Para quem tem física para fixar, o básis de Paranaguá
segue historicamente elevado (+R$ 6,21/saca sobre a paridade), mesmo com a pequena
reversão do dia — continuar travando parte do volume físico nesses níveis segue sendo
a leitura operacional de maior convicção da seção.

---

## Farelo

**Viés: neutro tático (rebaixado de bear estrutural) — o ratio Far/Soj fechou acima de
80% em duas sessões consecutivas e agora limpas (80,85% em 09/07, 80,65% em 10/07), e
o COT mostra fundos comprando farelo net long +295% na semana, derrubando a confiança
no gatilho técnico que sustentava o bear desde 11/06/2026, ainda que o fundamento
ABIOVE (exportação caindo pela metade sem queda proporcional de estoque) permaneça
intacto no médio prazo — tratando a fila
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` (VENCIDA)**

### Tratando a fila `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`

A revisão cobra três perguntas: "ratio fechou <80%? WASDE mudou o quadro? NOPA
confirmou crush?" **Resposta de hoje, com dado limpo:**

**1) O ratio NÃO fechou abaixo de 80% — pelo contrário, fechou consistentemente ACIMA,
por duas sessões seguidas, usando agora números internamente consistentes entre datas
diferentes (não mais uma revisão retroativa do mesmo dia).** A série completa da
semana, toda ela recalculada sob o dump de hoje: **79,28% (06/07) → 79,46% (07/07) →
78,52% (08/07) → 80,85% (09/07) → 80,65% (10/07)**. O protocolo original de 11/06/2026
definia o gatilho de bear como "ratio sustentado abaixo de 80% por 2-3 pregões
consecutivos" — o que de fato ocorreu entre 06 e 08/07 (três sessões abaixo de 80%),
mas nas duas sessões seguintes o ratio inverteu para o lado oposto, também por duas
sessões consecutivas. Diferente de ontem, essa leitura não depende de comparar o
"mesmo dia" sob dois dumps diferentes — são duas datas-base distintas (09/07 e 10/07)
dentro do MESMO dump de hoje, o que dá muito mais confiança de que o movimento é real,
não um artefato de rolagem. Reforça essa confiança o fato de o contrato N26 do farelo
ter reaparecido na curva de hoje (fechamento **320,60 USD/sht**, com prêmio sobre o
spot Q26 de 320,40) — o mesmo padrão de resolução observado na soja.

**2) O WASDE apareceu como fonte pela primeira vez neste briefing** (fila
`release-usda_wasde-2026-07-10`), mas **não mudou o quadro do farelo**: comparando a
geração de junho/2026 com a de julho/2026 (WASDE, 10/07/2026), os números de farelo
para Brasil e Argentina estão **congelados, sem revisão**: farelo Brasil — produção
8,00 mi t (jun e jul), exportação 0,19 mi t (jun e jul), esmagamento doméstico 7,10 mi
t (jun e jul), estoque inicial 0,19 mi t (jun e jul); farelo Argentina — produção 33,11
mi t (jun e jul), exportação 2,91 mi t (jun e jul), esmagamento doméstico 3,65 mi t
(jun e jul). **Resposta: não, o WASDE de julho não revisou o balanço de farelo BR/ARG
frente a junho** — uma publicação "quieta" nesse recorte específico. Importante: essa
fonte **não cobre soja nem óleo em nenhuma geografia**, e a cobertura de farelo da
China aparece truncada em apenas duas linhas (estoque inicial 2024/25 e 2025/26, sem
produção/exportação/esmagamento) — ver Honestidade #1 para o detalhamento da lacuna.

**3) A NOPA (National Oilseed Processors Association, associação que publica o
esmagamento mensal americano) segue com `monthly_status` em 0,0 bool** (indicadores,
11/07/2026) — a mesma barreira de assinatura paga documentada desde meados de junho. A
fila traz `release-nopa-2026-07-11`, mas sem dado interpretável, igual aos dias
anteriores. **Resposta: não, a NOPA não confirmou o crush americano.**

**Síntese da fila:** o gatilho técnico específico (ratio <80% sustentado) **falhou**
com dado agora confiável — não porque o fundamento tenha mudado (WASDE ficou mudo,
NOPA segue inacessível), mas porque o próprio preço relativo farelo/soja se moveu
contra a tese nas duas últimas sessões. Isso não invalida o argumento estrutural da
ABIOVE (ver abaixo), mas rebaixa significativamente a confiança na oportunidade tática
de curto prazo que o gatilho original apontava.

**A crush margin fechou em 2,8819 USD/bu** (Board Crush: farelo 320,40 + óleo 70,46 −
soja 1.191,75; indicadores, 10/07/2026), uma **queda de -0,50%** frente aos 2,8965 de
09/07 — a série completa da semana, usando os valores consistentes de hoje: **2,4974
(06/07) → 2,5638 (07/07) → 2,7316 (08/07) → 2,8965 (09/07) → 2,8819 (10/07)**, uma alta
líquida de **+15,4%** na semana, mas com o último dia interrompendo o que a leitura de
ontem havia descrito como "cinco altas seguidas" — essa descrição foi baseada em
números que o próprio sistema já revisou hoje (ver Honestidade #3). Mesmo com a leve
queda do último dia, o nível segue perto do topo da série documentada, sustentando o
incentivo de esmagamento a pleno vapor.

**As praças físicas de farelo no Brasil (NAG, 10/07/2026)** mostram o primeiro
movimento real em semanas: **Mato Grosso/IMEA subiu para R$ 1.577,34/ton (+1,47%)**,
saindo do patamar estável de R$ 1.554,53/ton que vigorava desde 07/07. Rondonópolis
mantém **R$ 1.620,00/ton** (estável) e RS **R$ 1.640,00/ton** (estável, mesmo valor há
semanas). O prêmio de exportação do farelo em Paranaguá segue em **+0,05 USD/sht**
(julho/26, inalterado) — o Brasil continua sem vantagem de preço para exportar farelo.
A alta em MT é pontual (um dia) e pode refletir demanda sazonal de ração, mas é digna
de nota porque tensiona, ainda que levemente, a narrativa de "farelo sobrando" no
mercado físico doméstico — vale acompanhar se vira tendência.

**Os dados projetados da ABIOVE (sem alteração desde a leitura anterior)** continuam
mostrando a exportação de farelo brasileiro recuando pela metade entre agosto e
dezembro/2026: 1.400 → 1.100 → 850 → 800 → 700 mil t, sem queda proporcional no estoque
final projetado (1.224 → 1.016 → 1.100 → 1.101 → 1.016 mil t). Esse mecanismo é o pilar
mais sólido da tese estrutural bearish, porque não depende de nenhum contrato CBOT nem
do ratio do dia: menos saída pelo porto empurra o excedente de farelo para o mercado
interno de ração, pressionando o preço doméstico ao longo do segundo semestre — esse
argumento segue de pé, mesmo com o gatilho tático de hoje enfraquecido.

**A curva forward do farelo (10/07/2026, agora completa com N26)**:

| Vencimento | Código | Preço (USD/sht) | Var. vs Ago |
|---|---|---|---|
| Julho/26 | N26 | 320,60 | +0,20 |
| Agosto/26 | Q26 | 320,40 | — (spot) |
| Setembro/26 | U26 | 317,20 | −3,20 |
| Outubro/26 | V26 | 315,20 | −5,20 |
| Dezembro/26 | Z26 | 318,70 | −1,70 |
| Janeiro/27 | F27 | 320,60 | +0,20 |

Outubro (V26, 315,20) permanece o vencimento mais descontado, coincidindo com o pico
sazonal de esmagamento simultâneo Brasil + Argentina — coerente com a leitura de
semanas anteriores.

**O posicionamento dos fundos (COT, agora atualizado para 07/07/2026)** é o
desenvolvimento mais relevante desta seção: managed money **long em 115.831
contratos, short em 97.109, net long em +18.722 contratos** — um salto de **+295%**
frente aos +4.740 contratos (praticamente neutro) de 30/06. Como fração do OI, o net
long subiu de **0,81% para 3,14%** (OI de 595.447). Os fundos deixaram de estar
"equilibrados" e passaram a inclinar, de forma moderada, para o lado comprado — um
movimento coerente com (e provavelmente parte da causa de) o ratio ter cruzado de
volta acima de 80%.

**O forecast estatístico do farelo (11/07/2026)** segue destoando da tese
fundamentalista ABIOVE: central 7d = **323,59 USD/sht** (bandas 309,01-338,16), viés
**altista**, subindo dos 319,01 da geração de ontem. Central 30d = **337,54 USD/sht**
(bandas 307,36-367,71), viés **altista**, subindo de 332,86. Diferente de ontem, hoje
essa divergência entre modelo (altista) e ABIOVE (bearish estrutural) tem o reforço de
dados reais e não-ambíguos — ratio acima de 80% e fundos comprando — o que muda a
leitura de "tensão a monitorar" para "sinal tático que pesa contra a posição vendida
de curto prazo".

### O que invalida / risco para o farelo

- **O ratio Far/Soj voltar a fechar abaixo de 80% num próximo pregão** devolveria o
  gatilho tático original — hoje esse risco é real, dado que o ratio está apenas
  0,65 p.p. acima do limiar.
- **A ABIOVE (exportação caindo pela metade sem queda proporcional de estoque) se
  confirmar no físico ao longo do 2S/26** — o argumento estrutural mais sólido da tese
  bearish segue intacto e pode reafirmar-se independentemente do ratio de curto prazo.
- **O COT de 07/07 ser um pico isolado, não uma tendência** — a próxima atualização
  (~14/07) precisa confirmar continuidade da compra dos fundos.
- **NOPA seguir inacessível indefinidamente** — sem confirmação direta de esmagamento
  americano.
- **WASDE nunca trazer soja/óleo dos EUA** — mesmo tendo aparecido hoje, a cobertura é
  parcial (só farelo BR/ARG) e a pergunta mais relevante para o complexo (oferta de
  soja) segue sem canal de resposta.
- **A alta física em MT/IMEA (+1,47%) virar tendência**, o que enfraqueceria ainda mais
  a narrativa de sobra doméstica de farelo.

### Leitura operacional — farelo

O gatilho técnico específico que embasava posição vendida tática desde 11/06 (ratio
sustentado <80%) **não está mais confirmado, e hoje o dado é limpo o suficiente para
levar essa leitura a sério** — diferente de ontem, quando a reversão era suspeita de
artefato. Para quem opera posição vendida tática ancorada estritamente nesse gatilho, a
recomendação é **reduzir ou zerar essa perna agora**, sem abandonar a tese estrutural
mais ampla (ABIOVE), que segue de pé como pano de fundo de médio prazo e pode
reafirmar-se ao longo do segundo semestre à medida que a exportação de fato recuar. Para
quem quer manter exposição à tese estrutural, prefira operar via spread de convergência
(farelo/soja ou o crush completo) em vez de posição direcional pura vendida em farelo —
isso limita o risco de ser pego pelo mesmo tipo de reversão técnica observada esta
semana. Referência de stop para quem ainda mantém posição vendida: 322-324 USD/sht
(acima do fechamento de hoje, dado que o forecast de 7d já projeta banda alta de
338,16).

---

## Óleo

**Viés: bear tático mantido e confirmado com dado limpo — fechamento de 70,46 cts/lb,
abaixo do suporte de 72,00 por uma distância de -2,14%, com a curva forward em
backwardation e o COT mostrando fundos reduzindo net long (-7,6% na semana), tratando a
fila `alerta-quebra_suporte-oleo_cbot-2026-07-10`**

### Tratando a fila `alerta-quebra_suporte-oleo_cbot-2026-07-10`

O óleo de agosto (ZLQ26.CBT) abriu em **70,08**, fez máxima de **70,85**, mínima de
**69,43** e fechou em **70,46 cts/lb** (CBOT CME, 10/07/2026, volume **42.472
contratos** — volume normal, também revertendo o volume anômalo de ontem). Frente ao
valor de 09/07 no mesmo dump (69,92), a variação foi de **+0,77%**, uma leve alta no
dia que não muda a conclusão da fila: **confirma** — o óleo segue abaixo do suporte
técnico de 72,00, com uma distância de **-2,14%** (mais apertada que os -4,25% que a
leitura de ontem havia calculado, mas isso é esperado dado que o preço revisado de
ontem, 69,86, era mais baixo que o de hoje). O contrato de julho (N26) do óleo **nunca
desapareceu da curva** — segue cotado a **70,86 cts/lb**, com prêmio normal sobre o
spot Q26 — o óleo é a única das três pernas que não teve o problema de rolagem
documentado nesta semana, o que reforça a leitura de que o fenômeno em soja/farelo foi
específico dessas duas pernas, não um problema sistêmico do briefing.

**A margem de biodiesel americano caiu para 0,6338 USD/galão** (indicadores,
10/07/2026: receita 6,7183 = HO 3,5533 + 1,5×RIN 2,11; custo 6,0845 = óleo 5,2845 +
industrial 0,80), uma queda de **-8,5%** frente aos 0,6926 de 09/07 — ainda dentro da
faixa de conforto de 0,50-0,80 USD/gal já documentada, mas se aproximando do piso: 0,5814
(06/07) → 0,5225 (07/07) → 0,7088 (08/07) → 0,6926 (09/07) → **0,6338 (10/07)**. O
heating oil (HO=F) fechou em **3,5533** (10/07/2026), praticamente estável frente à
abertura de 3,5606 (-0,2% intradia) — sem grande pressão adicional, mas a margem perdeu
folga principalmente pelo custo do óleo mais alto (5,2845 vs 5,2440 em 09/07).

**A curva forward do óleo (10/07/2026)** mantém backwardation clara a partir do spot:

| Vencimento | Código | Preço (cts/lb) | Var. vs Ago |
|---|---|---|---|
| Julho/26 | N26 | 70,86 | +0,40 |
| Agosto/26 | Q26 | 70,46 | — (spot) |
| Setembro/26 | U26 | 69,92 | −0,54 |
| Outubro/26 | V26 | 69,33 | −1,13 |
| Dezembro/26 | Z26 | 68,98 | −1,48 |
| Janeiro/27 | F27 | 68,84 | −1,62 |

A curva caindo -1,62 cts/lb (-2,3%) de agosto a janeiro/27 é praticamente idêntica em
magnitude à documentada em leituras anteriores — segue sendo o argumento técnico mais
robusto para manter posição vendida de médio prazo via carry, porque não depende de
nenhuma ambiguidade de dado (a curva do óleo está limpa há dias).

**O posicionamento dos fundos (COT, agora atualizado para 07/07/2026)** mostra
de-risking contínuo: managed money **long em 119.996 contratos, short em 35.077, net
long em +84.919 contratos** — uma **queda de -7,6%** frente aos +91.946 contratos de
30/06. Como fração do OI, o net long recuou de **14,59% para 13,22%** (OI de 642.514) —
ainda a posição mais assimétrica das três pernas do complexo, de longe, mas
continuando a tendência de redução que já vinha sendo documentada nas leituras
anteriores.

**O Índice de Suporte do Óleo (ISO) permanece em 100/100 (5/5 condições)** (indicadores,
11/07/2026), mantendo a hipótese de efeito calendário/estrutural já discutida em
leituras anteriores (ver Honestidade).

**O pano de fundo regulatório global segue inalterado desde 05/06/2026**
(`system/tributario_watch.toml`, sem novos `atualizado_em` há 36 dias): EPA Final RFS
2026/2027 sustenta o RIN D4, o crédito 45Z tende a favorecer óleo doméstico americano,
a Indonésia mantém a exportação de palma centralizada via Danantara mais o levy de
exportação de CPO (crude palm oil, óleo de palma bruto) de até 12,5% — mas segue
impossível quantificar porque o **MPOB (Malaysian Palm Oil Board) está inacessível**,
com o parser retornando apenas ~3.439 caracteres de HTML sem números extraídos
(11/07/2026, mesmo bloqueio de semanas anteriores).

**O forecast estatístico do óleo (11/07/2026)** subiu ligeiramente mas mantém o viés
baixista: central 7d = **69,07 cts/lb** (bandas 64,88-73,26), viés **baixista**, ante
68,51 na geração de ontem. Central 30d = **64,72 cts/lb** (bandas 56,06-73,39), viés
**baixista**, ante 64,15. O modelo estatístico e a curva forward seguem alinhados na
mesma direção — o caso mais consistente de todo o complexo hoje.

### O que invalida / risco para o óleo

- **Um fechamento limpo acima de 70,86 (nível de N26 hoje) ou perto de 72,00** num
  próximo pregão reabriria o teste da resistência.
- **A margem de biodiesel, hoje em 0,6338, cair abaixo de ~0,50 USD/gal** (piso da
  faixa de conforto) reduziria o incentivo doméstico americano ao óleo — a margem já
  perdeu 8,5% de folga no último dia.
- **RIN D4 real acima ou abaixo do parâmetro fixo usado no modelo (2,11 USD/RIN)** —
  incerteza estrutural bidirecional, sem novo dado hoje.
- **Dados de palma malaia (MPOB) seguirem inacessíveis** — impossível avaliar o efeito
  de El Niño ou das restrições indonésias sobre o prêmio de substituição.
- **O COT continuar mostrando redução de net long na próxima atualização (~14/07)** —
  aceleraria o de-risking já documentado.

### Leitura operacional — óleo

O viés segue bear tático, e hoje com mais confiança do que ontem, dado que o dado está
limpo (sem ambiguidade de rolagem) e a curva forward em backwardation continua sendo o
argumento técnico mais robusto para manter exposição vendida de médio prazo via carry.
Referência de stop para quem está posicionado vendido: 71,00-72,00 cts/lb. Para quem
opera o oil share dentro do crush (hoje em 52,37%, praticamente estável frente a 52,41%
ontem), o viés estrutural segue favorecendo manter exposição relativa ao óleo frente ao
farelo — ISO em 100/100 e margem de biodiesel ainda positiva — mas a folga da margem
caiu 8,5% no último dia e o COT mostra os fundos reduzindo a aposta, dois sinais que
pedem cautela para quem quiser aumentar essa exposição relativa a partir daqui.

---

## Spreads e crush — leitura de complexo

### Crush margin: 2,8819 USD/bu — alta líquida de +15,4% na semana, mas com o último dia interrompendo a sequência

A crush está em **2,8819 USD/bu** (Board Crush: farelo 320,40 + óleo 70,46 − soja
1.191,75; indicadores, 10/07/2026), uma queda de -0,50% frente aos 2,8965 de 09/07. A
série completa da semana, usando os valores consistentes de hoje: **2,4974 (06/07) →
2,5638 (07/07) → 2,7316 (08/07) → 2,8965 (09/07) → 2,8819 (10/07)** — alta líquida de
**+15,4%**, mas o último dia rompe o que a leitura de ontem descrevia como uma
sequência ininterrupta de altas (ver Honestidade #3). O sinal de fundo não muda: a
crush segue perto do topo da série documentada, sustentando o incentivo de esmagamento
a pleno vapor e, por extensão, a oferta física de farelo e óleo.

### Ratio Far/Soj: 80,65% — acima de 80% por duas sessões consecutivas e limpas, falhando o gatilho tático do bear-farelo

Como detalhado na seção de Farelo, o ratio de 09/07 (80,85%) e de 10/07 (80,65%) — as
duas dentro do MESMO dump de hoje, sem a ambiguidade de revisão retroativa que
contaminou a leitura de ontem — confirmam que o farelo cruzou de volta para a zona
"não mais abundante" (>80%). Isso derruba a confiança no gatilho técnico específico que
sustentava o bear-farelo desde 11/06, tratando a fila
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, mesmo com o
fundamento ABIOVE (exportação caindo, estoque sustentado) permanecendo intacto no
médio prazo.

### Oil share: 52,37% — estável, sem tendência direcional clara na semana

O oil share está em 52,37% hoje, ante 52,41% em 09/07 (-0,04 p.p.) — a série da semana
(52,03% em 07/07 → 53,15% em 08/07 → 52,41% em 09/07 → 52,37% em 10/07) mostra
vaivém em torno de 52-53%, sem tendência monotônica clara.

### Oil-meal spread: 0,7018 USD/bu — leve queda, dentro da faixa recente

O oil-meal spread (contribuição do óleo menos a do farelo por bushel) está em 0,7018
hoje, ante 0,7084 em 09/07 (-0,9%) — a série da semana (0,5885 em 07/07 → 0,9229 em
08/07 → 0,7084 em 09/07 → 0,7018 em 10/07) segue oscilando, sem trajetória limpa.

### ISF em 80/100, ISO em 100/100 — patamar sustentado

O Índice de Sobra de Farelo (ISF) está em 80/100 (4/5 condições) e o Índice de Suporte
do Óleo (ISO) em 100/100 (5/5) — o mesmo patamar documentado desde 01/07/2026
(indicadores, 11/07/2026).

### O que os índices e o COT dizem juntos em 11/07/2026

ISF 80/100 + ISO 100/100 (ambos estáveis, efeito calendário) + ratio Far/Soj acima de
80% por duas sessões limpas (falha do gatilho tático bear-farelo, fundamento ABIOVE
intacto) + oil share sem tendência clara (52-53%, vaivém) + crush margin perto do topo
da série (+15,4% na semana, com leve recuo no último dia) + margem de biodiesel
perdendo folga (-8,5% no último dia, ainda dentro da faixa de conforto) + soja
confirmando rompimento de 1.180,00 com dado limpo + óleo confirmando perda de 72,00
com dado limpo + **COT mostrando rotação real: fundos comprando soja (+82%) e farelo
(+295%) enquanto reduzem óleo (-7,6%) na semana até 07/07**:

**A leitura de hoje é de "dado resolvido, complexo em rotação".** O desenvolvimento
mais importante do dia é que a ambiguidade de dado que dominou a leitura de ontem foi
resolvida — N26 voltou às curvas de soja e farelo, os dois alertas técnicos da fila se
confirmaram com dado limpo, e o COT (finalmente atualizado) mostra o "dinheiro grande"
girando dentro do complexo: comprando o grão e seu subproduto proteico, reduzindo a
aposta no óleo. A régua de gestão de risco pode voltar ao normal — a cautela extra
recomendada ontem por qualidade de dado não se aplica mais hoje —, mas a régua
direcional deve se ajustar: a tese estrutural do farelo (ABIOVE) segue de pé no médio
prazo, mas o gatilho tático de curto prazo que a acompanhava deixou de funcionar, e a
soja ganhou o alinhamento mais forte de convicção de toda a semana.

---

## Lente fiscal e regulatória BR

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L) — vence HOJE
(11/07/2026, fila `trib-MP-1358-2026-2026-07-11`).** Sem mudança desde a última
leitura (`system/tributario_watch.toml`, evento MP-1358-2026, `atualizado_em`
2026-06-05, status "tramitacao", `proximo_marco` = "Deliberação comissão mista",
`proximo_data` = 2026-07-11, `vigencia_ate` = 2026-07-11) — o monitor tributário está
parado há 36 dias sem nenhuma atualização de status, mesmo com o vencimento formal
ocorrendo hoje, num sábado, o que por si só reduz a chance de uma deliberação
legislativa efetiva nesta data específica (o Congresso tipicamente não delibera aos
sábados) — mais provável é que a definição, se houver, ocorra em dias úteis próximos.
A MP ressarce PIS/Cofins/Cide da gasolina e do diesel, mantendo o combustível fóssil
artificialmente mais barato — o mesmo espírito da MP 1.363/2026 (subsídio de R$
1,12/L ao diesel, vigente até 31/12/2026, já tratada em
[[2026-05-26_subvencao-fossil-aperta-biodiesel]]). O mecanismo de transmissão para o
complexo soja é indireto mas real: enquanto o combustível fóssil segue subsidiado, a
competitividade relativa do biodiesel dentro do mix B15 mandatório permanece
pressionada, mantendo a margem da indústria de biodiesel (maior consumidora industrial
de óleo de soja no Brasil) mais apertada do que teria sem a subvenção ao concorrente
fóssil. Se a MP caducar sem conversão em lei, é um sinal (fraco, mas real) de perda de
fôlego político do pacote pró-fóssil — levemente positivo para a competitividade do
biodiesel e, por extensão, para a demanda industrial de óleo de soja; se for
convertida ou prorrogada, reforça o quadro de pressão já documentado desde maio. Como
o monitor tributário não capturou nenhuma atualização, esta leitura não pode confirmar
o desfecho — fica como item a verificar na próxima leitura.

**Isenção PIS/Cofins biodiesel — vencimento em 31/07/2026, 20 dias.** Sem sinalização
pública de renovação até hoje (evento PISCOFINS-BIODIESEL-ISENCAO, `atualizado_em`
2026-06-05, sem mudança). O checkpoint D+45 desse insight
([[2026-05-26_pis-cofins-biodiesel-explica-mercado-fisico-fraco]]) já venceu em
09/07/2026 sem resposta, como registrado nas duas últimas leituras — segue sem
resposta hoje também.

**B16 — sem data, travado em B15.** Sem mudança de status (evento B16-CNPE-2026,
`atualizado_em` 2026-06-05, status "adiado", sem `proximo_data`).

**MP 1.363/2026 (subsídio ao diesel fóssil) — em vigor até 31/12/2026.** Sem
alteração. Bearish estrutural persistente para a demanda incremental de óleo de soja
no mercado doméstico brasileiro.

**STJ REsp 2.165.276/2026 — crédito PIS/Cofins para esmagadoras.** Sem alteração.
Bullish para a soja/óleo (alívio de custo de entrada para biodiesel) e, por extensão,
incentivo a mais esmagamento — coerente com mais oferta de co-produtos, reforçando o
argumento estrutural (não tático) do farelo.

**Câmbio (PTAX) em 5,1088 BRL/USD (10/07/2026), terceira sessão seguida de apreciação
do real** — já tratado na seção de Soja. O impacto fiscal indireto (real mais forte
reduz a paridade de exportação em reais, pressionando margem de quem exporta em dólar
e vende custo em real) segue neutro-a-levemente-negativo para o produtor doméstico,
sem mudança de regime.

**Pano de fundo regulatório global (EUA e Indonésia) segue dando suporte estrutural ao
óleo, sem contradizer o viés bearish tático** — detalhado na seção Óleo.

---

## Riscos e eventos próximos

**Vencimento da MP 1.358/2026 — HOJE, 11/07/2026, fila `trib-MP-1358-2026-2026-07-11`,
sem confirmação de desfecho neste briefing.** O evento fiscal mais imediato da leitura
de hoje — monitorar deliberação da comissão mista nos próximos dias úteis.

**Próxima atualização do COT (~14/07/2026)** — o teste real de se a compra de fundos em
soja (+82%) e farelo (+295%) e a redução em óleo (-7,6%) documentadas hoje continuaram
ao longo da semana corrente (06 a 10/07), ainda não capturada pelo dado de 07/07.

**Isenção PIS/Cofins biodiesel — vencimento 31/07/2026 (20 dias).** Sem sinalização de
renovação até agora.

**USDA Crop Progress — próximo relatório semanal (~13/07)** é o teste direto da
narrativa de "calor nos EUA", sem atualização desde 05/07.

**NOPA — segue inacessível** (fila `release-nopa-2026-07-11` tratada aqui, sem dado
interpretável), sem crush americano confirmado por fonte primária.

**MPOB — sem números de palma extraídos**, mantendo cego o efeito da Indonésia e do El
Niño sobre o prêmio de substituição do óleo de soja.

**WASDE — apareceu hoje pela primeira vez, mas só com farelo BR/Argentina (fila
`release-usda_wasde-2026-07-10` tratada aqui).** Monitorar se o próximo relatório
mensal do USDA (WASDE de agosto, tipicamente ~12/08) traz cobertura mais completa,
incluindo soja e óleo — a pergunta sobre "oferta grande de soja" segue sem canal de
resposta interno até lá.

---

## Honestidade

O que não foi possível validar neste briefing de 11/07/2026, onde a confiança é baixa
ou há lacunas materiais:

**1. O WASDE apareceu pela primeira vez como fonte de dado neste sistema hoje
(`release-usda_wasde-2026-07-10`), mas a cobertura é parcial e restrita.** Os únicos
dados presentes são de **farelo** — Argentina (série completa 2024/25 a 2026/27) e
Brasil (série completa 2024/25 a 2026/27) — mais duas linhas truncadas de China
(apenas estoque inicial 2024/25 e 2025/26, sem produção, exportação ou esmagamento).
**Não há nenhum dado de soja em grão nem de óleo de soja, em nenhuma geografia,** e
não há dados dos Estados Unidos em nenhum produto. Isso significa que a pergunta
central que a fila vem levantando há um mês — "o WASDE confirma a narrativa de oferta
grande de soja?" — segue sem resposta, e a expectativa de que o WASDE resolveria essa
questão precisa ser recalibrada: mesmo com a fonte agora existindo, ela pode nunca
cobrir soja/óleo/EUA neste sistema. Isso deveria ter sido sinalizado nas leituras
anteriores como possibilidade — o WASDE, quando chegou, chegou incompleto.

**2. A revisão do fechamento de 10/07/2026 entre o dump usado na leitura de ontem
(soja 1.170,00, farelo 315,50, óleo 69,86) e o dump de hoje (soja 1.191,75, farelo
320,40, óleo 70,46) para a MESMA data-base não tem explicação disponível nas fontes.**
A hipótese mais provável, reforçada pelo retorno do contrato N26 às curvas de soja e
farelo hoje (com preços coerentes com os do dump de hoje), é que o dado usado ontem
capturou um instantâneo intradiário ou pré-fechamento, e o de hoje reflete o
fechamento oficial definitivo — mas isso é uma inferência razoável, não uma
confirmação de código (não há acesso ao pipeline de coleta a partir deste briefing).

**3. A narrativa de "crush margin em cinco altas consecutivas" descrita na leitura de
ontem não se sustenta sob os números revisados de hoje** — a série recalculada mostra
alta nas primeiras quatro sessões (06 a 09/07) seguida de uma leve queda na quinta
(09→10/07, -0,50%). A direção geral da semana (alta líquida de +15,4%) permanece
válida, mas o detalhe específico de "sequência ininterrupta" não resiste à revisão de
dado — registro isso para não carregar adiante uma descrição que os dados de hoje já
não sustentam com exatidão.

**4. NOPA segue com `monthly_status` em 0,0 bool** (indicadores, 11/07/2026) — mesma
barreira de assinatura paga documentada desde meados de junho, sem novo dado hoje.

**5. Percentis históricos de COT não calculados** — os números de 07/07/2026 (net long
soja +69.579, farelo +18.722, óleo +84.919) são lidos apenas em nível absoluto e como
fração do open interest corrente, sem série histórica completa para calibrar se estão
em zona extrema frente ao próprio histórico de cada contrato.

**6. O COT de 07/07/2026 tem 4 dias de defasagem frente à data de hoje** — captura a
terça-feira da semana passada, mas não captura nenhuma sessão da semana corrente (06 a
10/07/2026), incluindo o próprio rompimento de 1.180,00 na soja que esta leitura
discute. A confirmação de que a compra de fundos continuou ao longo da semana só virá
na próxima atualização (~14/07).

**7. Palma malaia (MPOB) segue sem números extraídos** (11/07/2026, mesmo texto de
HTML ~3.439 caracteres sem valores) — impossível avaliar o efeito de El Niño ou das
restrições indonésias sobre o prêmio de substituição do óleo de soja.

**8. Monitor tributário (`system/tributario_watch.toml`) sem atualização de status
desde 05/06/2026 — 36 dias —, mesmo com o vencimento formal da MP 1.358/2026 ocorrendo
hoje.** Nenhuma fonte pública rastreada pelo sistema (ABIOVE, NAG, notícias) confirmou
o desfecho da deliberação da comissão mista.

**9. O checkpoint D+45 de [[2026-05-26_subvencao-fossil-aperta-biodiesel]] venceu em
10/07/2026 sem resposta** (já registrado na leitura de ontem) — segue sem resposta
hoje, sem fonte nova disponível para as quatro perguntas de revisão programada daquele
insight.

**10. Dados de clima INMET (BR) não foram usados como driver desta leitura.** Julho é
entressafra da soja brasileira (colheita já concluída, plantio só em outubro) —
monitoramento de rotina, sem relevância direta para a tese de preço neste momento do
calendário agrícola.

**11. RIN D4 como parâmetro fixo (2,11 USD/RIN) segue sendo uma fonte relevante de
incerteza do modelo de biodiesel**, sem novo dado hoje.

**12. BCBA Argentina — sem relatórios de esmagamento/exportação acessíveis via
scraper** (page_fetched=1,0 mas sem links de relatório, 11/07/2026, sem atualização).

*Nenhum número foi inventado ou estimado além do que consta no briefing de 11/07/2026 e
nos insights anteriores referenciados. A contribuição central desta leitura foi
resolver a ambiguidade de dado que dominou a leitura de ontem — o contrato N26 voltou
às curvas de soja e farelo, os dois alertas técnicos da fila (soja acima de 1.180,
óleo abaixo de 72,00) se confirmaram com dado limpo, e o COT finalmente atualizado
revelou uma rotação real de fundos dentro do complexo (comprando soja e farelo,
reduzindo óleo). Ao mesmo tempo, o WASDE — esperado há um mês como o catalisador que
resolveria a questão da oferta de soja — chegou hoje, mas incompleto: só farelo,
Argentina e Brasil, sem soja nem óleo, sem nenhum dado dos Estados Unidos. Essa lacuna
específica, não a qualidade geral do dado, é hoje o limite mais importante da leitura.*
