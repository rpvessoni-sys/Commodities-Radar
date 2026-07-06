---
data: 2026-07-06
titulo: "Reabertura de segunda-feira traz o dia mais decisivo da série: soja dispara +2,73% e o ratio Far/Soj fecha, pela primeira vez desde a origem da tese em 11/jun, ABAIXO de 80% (80,03%) — mas ainda como leitura de UM único pregão, sem confirmação de continuidade; óleo permanece rompido abaixo do suporte 72,00 e a crush margin comprime mesmo com o rali, enquanto câmbio e físico BR seguem travados três dias atrás do papel"
tags: [complexo, auto-claude]
fontes:
  - CBOT CME (ZSQ26/ZMQ26/ZLQ26 + curva forward completa) — sessão de 2026-07-06, primeira sessão plena após três pregões fechados (feriado observado 03/jul + fim de semana 04-05/jul)
  - CBOT CME HO=F (heating oil) — settlement de 2026-07-06 (3,249 USD/galão)
  - BCB PTAX — último dado disponível é 2026-07-03 (USD/BRL 5,1717; EUR/BRL 5,9154); sem publicação de 06/jul no dump (ver Honestidade #1)
  - CEPEA/ESALQ Paranaguá via NAG — último dado disponível 2026-07-03 (R$ 135,45/sc), sem atualização de segunda-feira no dump
  - NAG Físico BR (farelo MT/IMEA, RS, Rondonópolis; prêmio PGUA farelo/óleo; soja Paraná interior) — último dado disponível 2026-07-03
  - CFTC COT Managed Money — 2026-06-23 (13º dia sem publicação nova, ver Riscos)
  - USDA Crop Progress — 2026-06-28 (sem atualização nova)
  - NOAA CPC ENSO — 2026-07-06 (El Niño Advisory, sem mudança)
  - ABIOVE projeções mensais — balanços ago-dez/2026 (farelo/óleo/soja), sem alteração
  - Indicadores sintéticos (crush, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, ISF/ISO) — 2026-07-06
  - MPOB — 2026-07-06 (21º dia consecutivo sem números extraídos, desde 16/jun)
  - NOPA — 2026-07-06 (fila `release-nopa-2026-07-06`; monthly_status inacessível)
  - system/tributario_watch.toml — eventos MP-1358-2026 (vigência até 2026-07-11), MP-1363-2026, PISCOFINS-BIODIESEL-ISENCAO, STJ-RESP-2165276, B16-CNPE-2026, EPA-RFS-2026-2027, 45Z-CLEAN-FUEL, DANANTARA-INDONESIA, INDONESIA-B50, INDONESIA-LEVY-PMK9
  - Notícias Agrícolas / Canal Rural — 2026-07-06 ("Soja dispara com dólar em alta e exportações antecipadas, aponta Cepea")
  - Forecasts estatísticos internos — 2026-07-06 (recalibrados com o spot de hoje)
  - Cruza com [[2026-07-05_leitura-complexo]], [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]], [[2026-05-26_subvencao-fossil-aperta-biodiesel]], [[2026-05-26_pis-cofins-biodiesel-explica-mercado-fisico-fraco]], [[2026-05-26_b16-bullish-farelo]], [[2026-05-26_curva-forward-cbot-oleo-desacopla]]
status: ativa
vies: [bull-soja, bear-farelo, bear-oleo]
---

## Visão geral

O complexo soja funciona como uma fábrica com uma única matéria-prima (a soja em grão) e
dois produtos de saída fabricados em proporção fixa a cada bushel esmagado: o **farelo** (a
fração proteica, ~78% da massa, vira ração animal) e o **óleo degomado** (a fração de
gordura, ~18-20% da massa, vira óleo de cozinha e biodiesel). Quem decide o ritmo de
esmagamento é a esmagadora, olhando a **crush margin** — o valor de mercado do farelo + óleo
produzidos por um bushel de soja, menos o custo daquele bushel. Quando o óleo paga mais que
o farelo dentro dessa conta (o que o sistema mede pelo **oil share**, a fração do valor do
crush capturada pelo óleo), a esmagadora esmaga a pleno vapor para capturar o óleo e "deixa
sobrar" farelo — motivo pelo qual o farelo, mesmo sendo o maior volume físico, tende a ficar
mais barato relativamente quando o óleo domina.

Hoje, **segunda-feira, 06/07/2026**, foi a primeira sessão plena de negociação depois de três
pregões seguidos fechados (feriado observado do 4 de julho na sexta 03/jul, mais o fim de
semana) — ou seja, o mercado teve três dias de notícia acumulada para processar de uma vez
só, e processou com um movimento forte: a **soja de agosto (ZSQ26.CBT) disparou +2,73% no
dia, de 1.136,25 para 1.167,25 cts/bu** (CBOT CME, 06/07/2026 vs fechamento de 02/07 — fila
`alerta-movimento_forte-soja_cbot-2026-07-06`), fechando muito perto da máxima do dia
(1.170,25) e arrastando farelo (+1,93%, para 311,40 USD/sht) e óleo (+1,81%, para 67,98
cts/lb) na mesma direção. É o movimento de um único dia mais forte de toda a série recente
de leituras.

**O segundo fato do dia, e o mais importante estruturalmente, é que o ratio Far/Soj — a
métrica que a fila de julgamento cobra desde 11/06/2026 (`revisao-2026-06-11_ratio-81-
prepara-janela-de-tranches-farelo-D+7`) — fechou hoje em 80,03%, pela PRIMEIRA VEZ abaixo do
gatilho psicológico de 80% desde que a tese nasceu, 25 dias atrás.** O ratio mede o preço do
farelo dividido pelo preço da soja (na mesma base): abaixo de 80% o farelo está "abundante"
frente à soja, acima de 87% está "apertado". A tese de 11/jun projetava esse cruzamento em
"1-2 semanas" e vinha girando em torno de 80,3%-81,4% havia mais de três semanas sem nunca
fechar abaixo da linha. Hoje fechou. **Mas é a leitura de um único pregão** — depois de três
dias sem sessão, não há como saber se é o início de uma ruptura sustentada ou um ajuste
técnico de um único dia que reverte amanhã; o próprio protocolo da tese original exige 2-3
fechamentos consecutivos abaixo de 80% para confirmar, e hoje é o primeiro, não o terceiro.

**O terceiro fato relevante é que a crush margin comprimiu MESMO com o rali generalizado de
preços** — caiu de 2,7032 para **2,6561 USD/bushel** (indicadores, 07-02 vs 06-07) porque a
soja (o custo) subiu proporcionalmente mais rápido que a soma farelo+óleo (a receita). Isso
é o mecanismo inverso do que normalmente se vê num rali de complexo: quando o grão lidera a
alta, a margem do esmagador aperta, não folga — um sinal, ainda que só de um dia, de que a
esmagadora pode ter menos incentivo a rodar a pleno vapor se esse padrão persistir.

**O quarto fato é sobre a qualidade do próprio dado do dia**: o câmbio (PTAX), o físico de
Paranaguá e as praças físicas de farelo no Brasil **ainda não têm atualização para
06/07/2026** no dump — o valor mais recente disponível para todos eles continua sendo
03/07/2026, três dias atrás. A notícia do dia (Canal Rural, **06/07/2026**) tem manchete
"Soja dispara com dólar em alta e exportações antecipadas, aponta Cepea" — ou seja, a fonte
jornalística já registra um dólar mais forte hoje, mas a série oficial de câmbio no sistema
ainda não capturou esse movimento (ver Honestidade #1). Isso significa que a paridade em
reais calculada hoje (R$ 133,08/saca) usa o CBOT de hoje só que combinado com o câmbio de
sexta-feira — um número que mistura um preço fresco com um câmbio desatualizado.

**Leitura de uma linha:** o dia mais decisivo da série recente — soja rompe para cima com
força (+2,73%), o ratio Far/Soj cruza 80% pela primeira vez em 25 dias mas ainda sem
confirmação de continuidade, o óleo segue rompido abaixo do suporte 72,00, e a crush margin
comprime apesar do rali. Confiança alta no bear-óleo tático (sem contestação há semanas);
confiança moderada-alta no bear-farelo estrutural (mais forte hoje que ontem, mas o
cruzamento do ratio precisa de 1-2 fechamentos adicionais); confiança moderada no
bull-tático de curto prazo da soja (movimento real e forte, mas sem mecanismo cambial/físico
atualizado para confirmar se é sustentável); confiança baixa em qualquer leitura fina de
paridade em reais enquanto câmbio e físico BR não atualizarem.

---

## Soja

**Viés: bull tático de curto prazo — alta de +2,73% no dia, a maior da série recente,
fechando perto da máxima; mas mecanismo de sustentação (câmbio, físico BR) ainda não
confirmado por dado fresco, e o forecast de 7 dias já classifica o novo nível como "lateral"
(ou seja, o próprio modelo vê o movimento de hoje como tendo esgotado, não iniciado, o
próximo tramo de alta)**

### O que sustenta a tese

A soja de agosto (ZSQ26.CBT) abriu em 1.140,25, fez mínima em 1.140,25 (ou seja, abriu na
mínima do dia), máxima em 1.170,25 e fechou em **1.167,25 cts/bu**, com volume de 15.278
contratos (CBOT CME, 06/07/2026) — uma alta de **+31,00 cts (+2,73%)** frente ao fechamento
de 02/07/2026 (1.136,25), tratando a fila `alerta-movimento_forte-soja_cbot-2026-07-06`. O
fato de o dia ter aberto na mínima e fechado a apenas 3 cts da máxima é tecnicamente
relevante: não houve reversão intradiária, foi compra sustentada do início ao fim do pregão
— um padrão mais consistente com fluxo de notícia genuína (câmbio + exportação, segundo a
manchete do dia) do que com um ajuste técnico de abertura de gap que se esvaziasse ao longo
do dia.

**A manchete do dia (Canal Rural via CEPEA, 06/07/2026)** atribui o movimento a "dólar em
alta e exportações antecipadas". O mecanismo, se confirmado: um dólar mais forte (real mais
fraco) eleva a paridade em reais da soja brasileira mesmo sem o CBOT se mexer, incentivando
o produtor brasileiro a segurar menos e vender mais rápido (fixação acelerada) — e
"exportações antecipadas" sugere que compradores internacionais estão adiantando embarques,
o que tende a apertar a disponibilidade física de curto prazo. **O problema é que a série
oficial de câmbio do sistema (PTAX, BCB) ainda não tem dado de 06/07/2026** — o último valor
publicado é de 03/07/2026 (5,1717 BRL/USD), que na verdade mostrava o real **se apreciando**
(vindo de 5,1945 em 02/07), o oposto do que a manchete de hoje descreve. Ou seja: há uma
inconsistência real entre o que a notícia relata (dólar subindo) e o que a última PTAX
oficial mostrava (dólar caindo) — a explicação mais provável é que o próprio câmbio virou de
direção entre sexta (03/07) e hoje (06/07), mas o sistema ainda não coletou o dado para
confirmar isso numericamente (ver Honestidade #1). Esta leitura registra a manchete como
sinal direcional qualitativo, não como número verificado.

**A paridade em reais oficial (indicadores, 06/07/2026) subiu para R$ 133,08/saca60kg**
(CBOT 1.167,25 cts × PTAX 5,1717 BRL/USD, sem basis), ante R$ 130,12 em 02/07 (CBOT 1.136,25
× PTAX 5,1945) — um ganho de **+2,96 BRL/saca (+2,28%)**. Mas note-se: **100% desse ganho
vem do CBOT mais alto, zero vem do câmbio**, porque o indicador usa a mesma PTAX de
03/07/2026 (5,1717) nos dois cálculos (o sistema ainda não tem PTAX mais nova para
recombinar). Se a manchete do dia estiver certa e o dólar realmente subiu hoje, a paridade
real (quando o câmbio for atualizado) deve ficar **ainda mais alta** do que os R$ 133,08
hoje mostrados — mas isso é inferência, não o número oficial (ver Honestidade #2).

**O físico de Paranaguá e o interior do Paraná seguem sem atualização, seu último valor
continua sendo 03/07/2026:** soja Paranaguá em R$ 135,45/saca (CEPEA/ESALQ via NAG, var
+0,27% frente a 02/jul) e soja Paraná interior em R$ 128,41/saca (NAG, var +0,42%) — ambos
no topo da sequência de altas já documentada na leitura de ontem (quatro altas seguidas em
cada série). Frente à paridade oficial recalculada de R$ 133,08, o interior do Paraná estaria
com desconto de -4,67 BRL/sc — mais largo que os -1,45 de sexta-feira, mas esse alargamento
é mecânico (paridade subiu com o CBOT, físico ainda não teve pregão novo para reagir) e não
deve ser lido como enfraquecimento de basis real até que o físico publique um valor de
06/07.

**As condições de lavoura americana seguem sem atualização** — USDA Crop Progress mais
recente permanece em 28/06/2026 (65% good/excellent, 6% poor, 96% emergido), sem o relatório
semanal que normalmente sairia hoje (risco de atraso pelo feriado, ver Riscos). O El Niño
Advisory segue confirmado (NOAA CPC, 06/07/2026), sem mudança de status.

**A colheita argentina segue encerrada em 98%** com produção mantida em 50,1 milhões de
toneladas (Canal Rural, 27/06/2026) — sem novo vetor de oferta relevante, mas mantendo a
Argentina como concorrente pleno de exportação nos próximos meses (relevante para o farelo,
ver seção seguinte).

**O posicionamento dos fundos (COT de 23/06/2026, CFTC — 13º dia sem publicação nova, ver
Riscos)** segue mostrando managed money net long em soja de **+36.986 contratos** (long
142.168, short 105.182; 3,7% do open interest de 1.006.834) — ainda sem confirmação de como
os fundos reagiram ao rali de hoje, que é justamente o tipo de movimento que costuma atrair
ou liquidar posição especulativa em volume.

**A curva forward (06/07/2026)** mostra contango moderado da frente ao longo:

| Vencimento | Código | Preço (cts/bu) | Var. vs Ago |
|---|---|---|---|
| Julho/26 | N26 | 1.160,00 | −7,25 |
| Agosto/26 | Q26 | 1.167,25 | — (spot) |
| Setembro/26 | U26 | 1.168,25 | +1,00 |
| Novembro/26 | X26 | 1.181,50 | +14,25 |
| Janeiro/27 | F27 | 1.195,75 | +28,50 |
| Março/27 | H27 | 1.200,25 | +33,00 |

Contango de +33,00 cts (+2,8%) de agosto a março/27 é consistente com custo de carregamento
normal, sem sinal de estresse de disponibilidade imediata (que apareceria como
backwardation) — a curva não está "gritando" escassez apesar do rali de hoje.

**Os forecasts estatísticos internos (06/07/2026, recalibrados com o spot de hoje)** mostram
algo importante para calibrar a força do movimento: central 7d = **1.167,85 cts/bu** (bandas
1.112,61-1.223,08), viés **lateral** — ou seja, o próprio modelo já classifica o nível pós-
rali de hoje como o centro esperado da próxima semana, não como ponto de partida para mais
alta de curto prazo. Já o central 30d = **1.179,51 cts/bu** (bandas 1.065,16-1.293,85), viés
**altista** — o modelo enxerga potencial de continuação apenas no horizonte mais longo.

### O que invalida / risco para a soja

- **O câmbio, quando finalmente atualizar, mostrar o real se apreciando (não depreciando)
  como a manchete sugere:** inverteria a leitura de que o dólar "empurrou" o rali de hoje,
  deixando o movimento inteiramente dependente do CBOT em si (fund buying, clima, ou fluxo
  técnico de reabertura pós-feriado).
- **WASDE de julho (~10/07/2026) reverter a leitura de "oferta grande":** catalisador mais
  importante da semana, coincide com o vencimento da MP 1.358.
- **Onda de calor no Corn Belt na segunda quinzena de julho** (florescimento): sem sinal nos
  dados disponíveis, mas segue o principal risco climático de curto prazo.
- **O forecast de 7d (central 1.167,85, já classificado como "lateral") se confirmar:** o
  próprio modelo estatístico não vê espaço para continuação imediata — quem entrar comprado
  esperando repetição do movimento de hoje está operando contra o próprio forecast de curto
  prazo do sistema.
- **Físico de Paranaguá, quando atualizar, não acompanhar a alta do papel:** confirmaria que
  o rali foi de CBOT/fundos, não de demanda física genuína no porto.

### Leitura operacional — soja

O movimento de hoje é grande o suficiente para justificar atenção, mas a estrutura de dados
disponível pede cautela antes de tratá-lo como início de tendência. Para quem opera o papel:
o forecast de 7 dias do próprio sistema já embute o nível de hoje como "central" — ou seja,
entrar comprado agora é apostar contra a mediana do modelo de curto prazo, um trade de
convicção alta em cima de notícia (câmbio + exportação), não de momentum estatístico. Para
quem tem física para fixar, a alta de hoje é uma janela concreta de preço melhor,
especialmente se a manchete de câmbio se confirmar amanhã (o que tornaria a paridade em
reais ainda mais favorável do que os R$ 133,08 hoje calculados com câmbio desatualizado). O
gatilho que decide a continuidade nos próximos dias é duplo: (1) a confirmação (ou não) do
câmbio mais fraco na PTAX de amanhã, e (2) o WASDE de julho (~10/07), que cai na mesma semana
do vencimento da MP 1.358.

---

## Farelo

**Viés: bear estrutural, agora mais próximo da confirmação — ratio Far/Soj fechou em 80,03%,
ABAIXO do gatilho de 80% pela primeira vez desde a origem da tese em 11/06/2026, tratando a
fila `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, agora D+25; mas é
o primeiro fechamento, não o segundo ou terceiro que o protocolo original exige**

### Tratando a fila `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`

A pergunta que a fila cobra: "ratio fechou <80%? WASDE mudou o quadro? NOPA confirmou
crush?" **Resposta parcial e o fato mais importante desta leitura: sim, o ratio fechou hoje
abaixo de 80% pela primeira vez — 80,03% (indicadores, 06/07/2026: farelo 311,40 USD/sht ÷
(soja 1.167,25 cts × 33,33)).** A trajetória completa desde a origem:

| Data-base | Ratio Far/Soj | Evento |
|---|---|---|
| 11/jun | 81,4% | origem da tese (compressão rápida) |
| 26/jun | 80,30% | ponto mais próximo do cruzamento até então |
| 29/jun | 81,43% | reverte para cima (pré-USDA) |
| 30/jun | 81,09% | pós-USDA, recuando |
| 01/jul | 80,82% | segue recuando |
| 02/jul | 80,66% | a 0,66 p.p. do gatilho |
| 03-05/jul | sem sessão | mercado fechado |
| **06/jul** | **80,03%** | **primeiro fechamento ABAIXO de 80%** |

**Por que isso ainda não é a confirmação plena da tese, apesar de ser o desenvolvimento mais
importante desde 11/06:** o protocolo original de 11/06/2026 (documentado em
[[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]) definiu o gatilho operacional como
"ratio sustentado abaixo de 80% por 2-3 pregões consecutivos", não uma leitura isolada. Hoje
é o **primeiro** fechamento abaixo da linha depois de três dias sem sessão — o mercado não
teve chance de testar continuidade ainda. O checkpoint formal D+7 (18/06) já havia sido
tratado como encerrado sem confirmação; o checkpoint D+90 (09/09/2026) segue sendo o
horizonte formal. **A recomendação desta leitura: tratar 80,03% como sinal de alerta máximo
(o mais próximo que a tese já chegou de se confirmar em 25 dias), mas aguardar o fechamento
de amanhã (07/07) antes de declarar rompimento operacional** — se amanhã fechar novamente
abaixo de 80%, a tese se confirma; se reverter para cima (como já aconteceu em 29/06, indo de
80,30% para 81,43% em três dias), o padrão de "quase rompe e volta" se repete pela segunda
vez.

**Por que o mecanismo aponta para baixo mesmo com o rali generalizado de hoje:** a soja (o
denominador do ratio) subiu +2,73% no dia, enquanto o farelo (o numerador) subiu apenas
+1,93% — o farelo simplesmente não acompanhou a força da soja, e é exatamente esse
descolamento de velocidade que empurra o ratio para baixo mesmo em dia de alta generalizada
de preços. Esse é um sinal estruturalmente mais forte do que um dia de queda absoluta do
farelo teria sido, porque mostra que a fraqueza é relativa (farelo perdendo para soja), não
apenas direcional.

**As praças físicas de farelo no Brasil ainda não têm atualização de hoje** — o último valor
disponível continua sendo 03/07/2026: MT/IMEA em R$ 1.554,53/ton (var +0,66% frente a
1.544,35 sustentados por três pregões), Rondonópolis em R$ 1.500,00/ton (segunda leitura
seguida no nível revertido, após o salto para R$ 1.650 em 01-02/jul), RS em R$ 1.640,00/ton
(estável desde pelo menos 22/06). O prêmio de exportação do farelo em Paranaguá permanece em
**+0,05 USD/sht** (NAG, 03/07/2026, mês de referência julho/26) — praticamente nulo,
confirmando que o Brasil segue sem vantagem competitiva de preço sobre a Argentina (colheita
98% concluída, 50,1 milhões de toneladas).

**Os dados projetados da ABIOVE (sem alteração) seguem mostrando a exportação de farelo
brasileiro recuando pela metade entre agosto e dezembro/2026:** 1.400 mil t (agosto) → 1.100
(setembro) → 850 (outubro) → 800 (novembro) → **700 mil t (dezembro)**, uma queda de -50% no
ritmo de escoamento externo em quatro meses. O estoque final projetado não desincha na mesma
proporção: recua de 1.224 mil t (agosto) para 1.016 (setembro), mas depois **sobe** para
1.100 (outubro) e 1.101 (novembro), só voltando a cair para 1.015 mil t em dezembro — mesmo
com a exportação caindo pela metade, o estoque doméstico projetado termina o ano
praticamente no mesmo nível de setembro. O mecanismo: com menos saída pelo porto, o farelo
produzido em excesso (puxado pelo crush favorável ao óleo) precisa ser absorvido pelo
mercado interno de ração, que historicamente não tem elasticidade para compensar toda a
queda de exportação — o resultado é pressão de preço doméstico, coerente com o ratio
rompendo para baixo hoje. A produção mensal de farelo projetada também recua ao longo do
ano: 2.285 mil t (agosto) → 2.129 (setembro) → 2.143 (outubro) → 1.978 (novembro) → 1.659
(dezembro) — a queda de produção acompanha (mas não resolve) a queda de exportação.

**A curva forward do farelo (06/07/2026)** subiu em bloco acompanhando o rali, mas manteve a
forma:

| Vencimento | Código | Preço (USD/sht) | Var. vs Ago |
|---|---|---|---|
| Julho/26 | N26 | 313,80 | +2,40 |
| Agosto/26 | Q26 | 311,40 | — (spot) |
| Setembro/26 | U26 | 309,40 | −2,00 |
| Outubro/26 | V26 | 308,00 | −3,40 |
| Dezembro/26 | Z26 | 311,10 | −0,30 |
| Janeiro/27 | F27 | 312,40 | +1,00 |

Outubro (V26, 308,00) segue sendo o vencimento mais fraco da curva — coincide com o pico
sazonal de esmagamento simultâneo Brasil + Argentina (ABIOVE projeta 2.846 mil t de
esmagamento de soja BR em outubro, o maior mês do ano) — o mercado de futuros continua
precificando o farelo mais fraco no 4º trimestre, mesmo após o rali de hoje ter elevado toda
a curva em nível absoluto.

**O posicionamento dos fundos (COT de 23/06/2026, sem atualização — 13º dia)** segue sendo o
dado mais revelador disponível: managed money net long de apenas **+12.359 contratos**, com
longs em 110.276 e **shorts em 97.917** (15,8% do open interest de 619.446 em posições
vendidas de managed money) — os fundos mantêm posição vendida ativa. Sem COT novo desde
antes do rali de hoje, não há como confirmar se essa posição vendida está sob pressão de
short-covering com o movimento de preço, ou se os fundos aumentaram a aposta baixista.

**Tratando a fila `release-nopa-2026-07-06`:** o sistema registra nova tentativa de coleta
da NOPA, agora datada de hoje. `monthly_status: 0.0 bool` (indicadores, 06/07/2026) — o
relatório mensal de crush americano da NOPA (National Oilseed Processors Association) segue
inacessível por exigir membership pago, há mais de um mês. Não há dado novo interpretável;
a lacuna persiste (ver Honestidade #4).

### O que invalida / risco para o farelo

- **Ratio Far/Soj reverter para cima amanhã (07/07), repetindo o padrão de 29/06:** o
  gatilho de confirmação exige 2-3 fechamentos consecutivos abaixo de 80%; hoje é apenas o
  primeiro.
- **Rondonópolis voltar a saltar para R$ 1.650/ton:** sem sessão nova desde 03/07 para
  confirmar se a reversão para R$ 1.500 se mantém.
- **Crush margin continuar comprimindo abaixo de 2,50 USD/bu:** hoje em 2,6561, caindo de
  2,7032 mesmo com o rali — se a tendência de compressão continuar, a esmagadora pode reduzir
  ritmo, o que tiraria oferta de farelo do mercado (efeito contrário ao bear estrutural).
- **WASDE de julho (~10/jul) reduzir a área de soja americana de forma expressiva:** menos
  esmagamento no 4T26 → menos farelo global, risco de short squeeze nos 97.917 contratos
  vendidos por fundos.
- **Estoque doméstico de farelo projetado pela ABIOVE não desinchar como a queda de
  exportação sugere:** reforça pressão, não alivia.

### Leitura operacional — farelo

O bear-farelo estrutural ganhou o desenvolvimento mais importante da série hoje: o ratio
Far/Soj finalmente cruzou 80% depois de 25 dias rondando a linha. Para quem opera o spread
de convergência (long farelo/short soja, ou o crush completo), a régua operacional agora é
clara e de curtíssimo prazo: **aguardar o fechamento de amanhã (07/07)**. Se confirmar
abaixo de 80% pela segunda vez seguida, a tese se torna operacional com alta convicção; se
reverter, o padrão de "quase rompe" se repete e o horizonte volta a ser o D+90 (09/09). Para
quem já está posicionado no short estrutural de farelo em preço absoluto, a régua de stop de
referência sobe para 313-315 USD/sht (ajustada para cima frente aos 308-310 anteriores, dado
o rali generalizado de hoje) — o nível absoluto subiu, mas a tese relativa (farelo perdendo
para soja) ficou mais forte, não mais fraca.

---

## Óleo

**Viés: bear tático confirmado — fechamento de 67,98 cts/lb segue abaixo do suporte-virou-
resistência 72,00 (fila `alerta-quebra_suporte-oleo_cbot-2026-07-06`), agora com mais de duas
semanas de rompimento; heating oil estável em torno de 3,25 USD/galão, mas a margem de
biodiesel comprimiu para 0,5156 USD/gal, o nível mais baixo desde 29/06**

### Tratando a fila `alerta-quebra_suporte-oleo_cbot-2026-07-06`

O alerta segue ativo, agora com o fechamento de hoje: óleo de agosto (ZLQ26.CBT) abriu em
67,24, fez máxima de 68,13, mínima de 67,17 e fechou em **67,98 cts/lb** (CBOT CME,
06/07/2026, volume 7.133 contratos) — uma alta de **+1,21 cts (+1,81%)** frente ao
fechamento de 02/07 (66,77), participando do rali generalizado do complexo, mas **sem
recuperar o suporte de 72,00**, que segue rompido e funcionando como resistência. A pergunta
operacional da fila — confirma ou muda a tese? — **confirma**: mesmo com o dia de maior alta
da série recente para o complexo inteiro, o óleo continua **5,58% abaixo** do nível de
72,00, um sinal de que a fraqueza estrutural do óleo é mais profunda do que o movimento de
um dia consegue reverter.

**A margem de biodiesel americano comprimiu para 0,5156 USD/galão** (indicadores, 06/07/2026:
receita 6,4141 = HO 3,249 + 1,5×RIN 2,11; custo 5,90 = óleo 5,0985 + industrial 0,80) — o
nível mais baixo desde 29/06/2026 (0,5322). A trajetória recente: 0,6621 (30/jun) → 0,5811
(01/jul) → 0,5395 (02/jul) → **0,5156 (06/jul)** — uma compressão de -22,1% em uma semana. O
mecanismo: o óleo de soja (o custo do biodiesel) subiu com o rali de hoje mais rápido do que
o heating oil (a receita) conseguiu acompanhar — o heating oil fechou em 3,249 USD/galão
(CME, 06/07/2026), praticamente estável frente aos 3,238 de 05/07 e levemente abaixo dos
3,2566 de 03/07. Como a margem de biodiesel é receita menos custo, e o custo (óleo) subiu
mais que a receita (HO+RIN), a margem aperta — o mesmo mecanismo de compressão observado na
crush margin do complexo inteiro. Isso é relevante porque a faixa de conforto do biodiesel
americano já vinha sendo descrita como 0,50-0,80 USD/gal nas leituras anteriores — hoje o
indicador está **a apenas 0,016 USD/gal do piso dessa faixa**, o mais perto que chegou desde
que a série começou a ser acompanhada.

**A curva forward do óleo (06/07/2026) manteve backwardation clara, mesmo após o rali:**

| Vencimento | Código | Preço (cts/lb) | Var. vs Ago |
|---|---|---|---|
| Julho/26 | N26 | 68,26 | +0,28 |
| Agosto/26 | Q26 | 67,98 | — (spot) |
| Setembro/26 | U26 | 67,57 | −0,41 |
| Outubro/26 | V26 | 67,10 | −0,88 |
| Dezembro/26 | Z26 | 66,77 | −1,21 |
| Janeiro/27 | F27 | 66,67 | −1,31 |

A curva caindo -1,31 cts/lb de agosto a janeiro/27 continua sendo o argumento técnico mais
forte para manter posição vendida de médio prazo: quem rola a posição mês a mês colhe esse
carry independentemente da direção do preço à vista. O fato de o front (N26, 68,26) negociar
**acima** do spot (Q26, 67,98) — diferente de leituras anteriores, quando N26 chegou a
negociar abaixo — sugere que parte do rali de hoje foi concentrado no vencimento mais
próximo, coerente com um movimento de curto prazo (cobertura técnica ou fluxo de reabertura)
mais do que uma reprecificação estrutural de toda a curva.

**O pano de fundo regulatório global segue reforçando a demanda de biodiesel como piso
estrutural, sem contradizer o viés tático de baixa.** O EPA Final RFS 2026/2027 (vigente
desde 15/06/2026) elevou os volumes obrigatórios de diesel de base biomassa de 8,86 para
9,07 bilhões de RINs — um salto de +61% ano contra ano que sustenta o valor do RIN D4 (fixado
em 2,11 USD/RIN no modelo interno). O crédito 45Z (Clean Fuel Production), em tramitação,
tende a excluir insumo importado da elegibilidade, o que reforçaria demanda por óleo
doméstico americano especificamente (bullish CBOT) e liberaria sebo brasileiro de volta ao
mercado interno. Do lado da palma, a Indonésia concentrou a exportação de CPO sob o fundo
estatal Danantara desde 01/06 e mantém levy de exportação de até 12,5% (PMK 9/2026) — ambos
encarecem a palma e favorecem o óleo de soja por substituição, mas sem poder ser
quantificado porque o MPOB segue inacessível há 21 dias (ver Honestidade #5).

**O posicionamento dos fundos (COT de 23/06/2026, sem atualização — 13º dia)** segue sendo o
maior risco de reversão mecânica do complexo: managed money net long de **+103.206**
contratos, representando 15,7% do open interest de 658.976 — a maior exposição relativa das
três pernas. Sem dado novo do COT, ainda não há como confirmar se essa posição historicamente
grande está sendo desmontada com a queda de preço das últimas semanas ou se persiste como
risco de long liquidation se o rali de hoje continuar.

**O Índice de Suporte do Óleo (ISO) permanece em 100/100 (5/5 condições)** hoje (indicadores,
06/07/2026), o **sexto pregão seguido** nesse patamar desde a virada de 01/07 — reforçando a
hipótese, já tratada em leituras anteriores, de que a virada de 80 para 100 foi um efeito de
calendário (rolagem do mês-alvo de comparação ABIOVE de junho para julho), não uma mudança
real de fundamento (ver Honestidade #3).

### O que invalida / risco para o óleo

- **Margem de biodiesel romper abaixo de 0,50 USD/gal:** hoje em 0,5156, a 0,016 do piso da
  faixa de conforto — o item de maior sensibilidade tática do óleo nesta leitura.
- **Heating oil não acompanhar uma eventual continuação de alta do óleo de soja:** se o óleo
  subir mais rápido que o HO de novo amanhã, a margem rompe o piso.
- **RIN D4 real acima de 2,40 USD/RIN** (o modelo usa 2,11 fixo): incerteza estrutural
  bidirecional, sem novo dado hoje.
- **Dados de palma malaia (MPOB) inacessíveis há 21 dias consecutivos** — se a produção de
  palma estiver caindo por El Niño ou pelas restrições indonésias, o óleo de soja ganharia
  prêmio de substituição global, o que seria altista.
- **WASDE de julho reduzir a área de soja americana:** menos esmagamento futuro nos EUA →
  menos óleo produzido → altista para os contratos de novembro em diante.
- **Exportação de óleo brasileiro projetada pela ABIOVE caindo de 110 mil t (setembro) para
  45 (outubro) e 21 (novembro):** mais óleo represado internamente (bearish doméstico) ou
  mais disponibilidade para o mandato B15 (efeito ambíguo).

### Leitura operacional — óleo

O viés segue bear tático, com a quebra do suporte 72,00 confirmada mesmo no dia de maior
alta da série para o complexo inteiro — um sinal de força relativa negativa que reforça a
tese, não a contesta. O ponto de maior atenção para amanhã é a margem de biodiesel: a
0,5156 USD/gal, ela está no ponto mais baixo desde 29/06 e a apenas centavos do piso da faixa
0,50-0,80 — se o heating oil não acompanhar uma eventual continuação do rali do óleo de soja,
a margem pode romper esse piso, o que historicamente tende a desestimular a demanda
industrial de biodiesel por óleo de soja (bearish adicional). O carry negativo da curva
forward continua favorecendo posição vendida de médio prazo (referência de stop ajustada
para 69,50-70,50 cts/lb, levemente acima da faixa anterior dado o rali de hoje). Alvo
primário do short seguindo os forecasts seria a zona em torno do central 7d recalibrado hoje
— ainda não disponível linha a linha no dump de indicadores, mas a leitura de ontem já
apontava 64-66 cts/lb como zona primária e 55-58 como secundária; ambos seguem válidos como
referência até a próxima atualização de forecast. Para quem opera o oil share (hoje em
52,19%, estável), o viés estrutural segue favorecendo manter exposição ao óleo dentro do
crush frente ao farelo, mesmo com margem de biodiesel comprimindo — a dominância relativa
dentro do crush (ISO 100/100) é uma dimensão distinta do nível de preço isolado ou da margem
de biodiesel especificamente.

---

## Spreads e crush — leitura de complexo

### Crush margin: 2,6561 USD/bu — comprime mesmo com o rali generalizado

A crush está em **2,6561 USD/bu** (Board Crush: farelo 311,40 + óleo 67,98 − soja 1.167,25;
indicadores, 06/07/2026), abaixo dos 2,7032 de 02/07 — uma compressão de -1,7% no primeiro
pregão pós-feriado, mesmo com os três componentes do complexo subindo em bloco. O mecanismo é
simples e importante: a soja (o custo do crush) subiu +2,73% no dia, enquanto farelo (+1,93%)
e óleo (+1,81%) subiram menos — a soma dos produtos não acompanhou a alta do insumo. Isso é
o tipo de dia que, se repetido, tira incentivo da esmagadora para rodar a pleno vapor
(menos oferta de farelo E óleo simultaneamente), um contraponto de médio prazo à leitura de
"farelo estruturalmente sobrando" — vale monitorar se a compressão continua nos próximos
pregões ou se é ruído de um único dia de rali desproporcional.

### Ratio Far/Soj: 80,03% — primeiro fechamento abaixo do gatilho de 80%, D+25 da tese sem confirmação plena

Como detalhado na seção de Farelo, o ratio rompeu 80% hoje pela primeira vez desde a origem
da tese (11/06). É o desenvolvimento central do dia para o complexo, mas ainda pendente de
confirmação por 1-2 fechamentos adicionais antes de ser tratado como sinal operacional
completo.

### Oil share: 52,19% — estável

O oil share está em 52,19%, praticamente igual aos 52,20-52,22% dos dias anteriores — o óleo
segue dominando o crush (>50%), sem sinal de mudança estrutural.

### Oil-meal spread: 0,627 USD/bu — estável

O oil-meal spread (contribuição do óleo menos a do farelo por bushel) está em 0,627 USD/bu,
na mesma faixa da semana anterior (0,619-0,677 USD/bu) — óleo e farelo mantendo suas
posições relativas dentro do crush.

### ISF em 80/100, ISO em 100/100 — sexto pregão seguido no mesmo patamar

O Índice de Sobra de Farelo (ISF) está em 80/100 (4/5 condições) e o Índice de Suporte do
Óleo (ISO) em 100/100 (5/5) — o mesmo patamar desde 01/07, agora o sexto pregão consecutivo
(contando os três dias sem sessão como "mantidos"). A estabilidade reforça a hipótese de
efeito calendário na virada de ISF/ISO ocorrida na virada do mês (ver Honestidade #3).

### O que os índices dizem juntos em 06/07/2026

ISF 80/100 + ISO 100/100 (ambos estáveis, efeito calendário) + ratio Far/Soj cruzando 80%
pela primeira vez em 25 dias (não confirmado) + oil share 52,19% (estável) + oil-meal spread
0,627 (estável) + crush comprimindo mesmo com rali (2,7032 → 2,6561) + margem de biodiesel no
piso mais baixo desde 29/06 (0,5156) + COT defasado 13 dias (103k net longs em óleo, 12k em
farelo com 98k shorts ativos, 37k em soja) + câmbio e físico BR três dias atrasados frente ao
CBOT + soja disparando +2,73% no dia:

A leitura de hoje é de **o dia mais decisivo da série recente, com o desenvolvimento mais
importante desde a origem da tese do farelo (ratio cruzando 80%), mas ainda pendente de
confirmação por falta de continuidade de sessão.** O rali generalizado de preços não mudou
nenhuma das teses estruturais — pelo contrário, tanto o farelo (perdendo relativamente para
a soja) quanto o óleo (não recuperando o suporte 72,00 mesmo no dia de maior alta) mostraram
força relativa negativa dentro do próprio movimento de alta, o que é uma confirmação mais
robusta das teses bearish do que um dia de preço estável teria dado. A crush comprimindo é o
contraponto a monitorar: se persistir, pode começar a tirar oferta física do mercado nas
próximas semanas.

---

## Lente fiscal e regulatória BR

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L) entra na semana do
vencimento, faltam 5 dias (11/07/2026, fila `trib-MP-1358-2026-2026-07-11`).** A MP
ressarce PIS/Cofins/Cide da gasolina e do diesel, mantendo o combustível fóssil
artificialmente mais barato — o mesmo mecanismo, em espírito, da MP 1.363/2026 (subsídio de
R$ 1,12/L ao diesel, vigente até 31/12/2026, já tratada em
[[2026-05-26_subvencao-fossil-aperta-biodiesel]]). O próximo marco é a **deliberação da
comissão mista**, travada em regime de urgência desde 27/06/2026
(`system/tributario_watch.toml`, evento MP-1358-2026) — ou o Congresso delibera e converte
(ou rejeita) a MP até 11/07, ou ela caduca por decurso de prazo. O mecanismo de transmissão
para o complexo soja é indireto mas real: enquanto o combustível fóssil segue subsidiado, a
competitividade relativa do biodiesel dentro do mix B15 mandatório permanece pressionada (o
mix é 85% diesel mineral + 15% biodiesel; se o diesel mineral fica mais barato via subvenção,
o biodiesel não ganha proporcionalmente, e a indústria de biodiesel — maior consumidora
industrial de óleo de soja no Brasil — segue com margem mais apertada do que teria sem a
subvenção ao concorrente fóssil). **Este marco cai na mesma semana do WASDE de julho
(~10/07)** — dois catalisadores relevantes, um de oferta/demanda física e outro de política
de preços relativos, concentrados no mesmo intervalo de dias. Se a MP 1.358 caducar sem
conversão em lei, é um sinal (fraco, mas real) de que o pacote pró-fóssil pode perder fôlego
político — levemente positivo para a competitividade do biodiesel e, por extensão, para a
demanda industrial de óleo de soja; se for convertida, reforça o quadro de pressão já
documentado desde maio.

**Isenção PIS/Cofins biodiesel — vencimento em 31/07/2026, 25 dias.** Sem sinalização
pública do MAPA ou MINFRA sobre renovação até hoje (06/07/2026,
`system/tributario_watch.toml`, evento PISCOFINS-BIODIESEL-ISENCAO). O checkpoint D+45 desse
insight (10/07/2026, [[2026-05-26_pis-cofins-biodiesel-explica-mercado-fisico-fraco]]) cai em
4 dias, coincidindo com o WASDE e com o vencimento da MP 1.358 — a semana de 06-10/jul
concentra três marcos relevantes ao mesmo tempo.

**B16 — sem data, travado em B15.** Sem mudança de status desde a última leitura (evento
B16-CNPE-2026, status "adiado", sem `proximo_data`).

**MP 1.363/2026 (subsídio ao diesel fóssil) — em vigor até 31/12/2026.** Sem alteração.
Bearish estrutural persistente para a demanda incremental de óleo de soja no mercado
doméstico brasileiro.

**STJ REsp 2.165.276/2026 — crédito PIS/Cofins para esmagadoras.** Sem alteração. Bearish
para o farelo — ao reduzir o custo tributário de entrada da soja usada em biodiesel,
incentiva mais esmagamento, mais oferta de co-produtos, coerente com a exportação de farelo
ABIOVE projetada em queda.

**Câmbio (PTAX) e físico BR seguem três dias atrasados frente ao rali do CBOT de hoje.** O
último dado oficial de câmbio é de 03/07/2026 (5,1717 BRL/USD, real se apreciando frente a
02/07), mas a manchete do dia (Canal Rural, 06/07/2026) já descreve um dólar mais forte hoje
— uma divergência que só será resolvida quando o sistema publicar a PTAX de segunda-feira
(ver Honestidade #1). Enquanto isso, qualquer leitura fina de paridade em reais ou de basis
interno deve ser tratada com cautela redobrada.

**Pano de fundo regulatório global (EUA e Indonésia) segue dando suporte estrutural ao óleo,
sem contradizer o viés bearish tático.** O EPA Final RFS 2026/2027 e o crédito 45Z em
tramitação (EUA) sustentam o valor do RIN D4 e favorecem o óleo de soja doméstico americano;
a centralização da exportação de palma pela Indonésia via Danantara e o levy de exportação de
CPO até 12,5% (PMK 9/2026) encarecem a palma e favorecem o óleo de soja por substituição
global (detalhado na seção Óleo).

---

## Riscos e eventos próximos

**O fechamento de amanhã (07/07) é o teste mais importante da semana para o ratio Far/Soj.**
Hoje fechou pela primeira vez abaixo de 80% (80,03%); se confirmar por um segundo pregão
seguido abaixo da linha, a tese bear-farelo estrutural passa de "quase confirmada" para
"confirmada operacionalmente" pela primeira vez em 25 dias.

**Semana de 06-10/07 concentra três marcos fiscais/fundamentalistas no mesmo intervalo:**
WASDE de julho (~10/07), vencimento da MP 1.358 (11/07, deliberação de comissão mista) e
checkpoint D+45 da tese PIS/Cofins biodiesel (10/07). Rara concentração de catalisadores —
vale reservar atenção redobrada.

**Câmbio (PTAX) e físico BR (CEPEA/NAG) com três dias de atraso frente ao CBOT.** A
divergência entre a manchete de hoje (dólar em alta) e a última PTAX oficial (real se
apreciando, dado de sexta) precisa ser resolvida com a publicação de amanhã.

**COT CFTC — 13º dia sem publicação nova.** O dado mais recente continua sendo o de
23/06/2026, deixando às cegas a leitura de como os fundos reagiram ao rali de hoje, o
movimento mais forte da série recente.

**USDA Crop Progress — sem atualização nova, risco de atraso no relatório desta semana pelo
feriado.**

**WASDE de julho — ~10/07/2026 (4 dias).** Primeiro WASDE pós-Acreage/Stocks, coincide com o
vencimento da MP 1.358 e o checkpoint D+45 da tese PIS/Cofins.

**Margem de biodiesel em 0,5156 USD/gal — o nível mais baixo desde 29/06, a poucos centavos
do piso da faixa de conforto (0,50-0,80).** Item de maior sensibilidade tática do óleo;
monitorar se o heating oil acompanha uma eventual continuação de alta do óleo de soja.

**Crush margin em compressão (2,7032 → 2,6561) mesmo com rali generalizado de preços.**
Contraponto de médio prazo à tese de "farelo sobrando" — se persistir, pode reduzir o ritmo
de esmagamento e tirar oferta física do mercado.

---

## Honestidade

O que não foi possível validar neste briefing de 06/07/2026, onde a confiança é baixa ou há
lacunas materiais:

**1. Câmbio (PTAX) sem atualização para 06/07/2026, mesmo sendo dia útil normal.** O último
dado oficial do BCB continua sendo de 03/07/2026 (5,1717 BRL/USD, real se apreciando frente a
02/07). A manchete do dia (Canal Rural, 06/07/2026, "Soja dispara com dólar em alta") sugere
que o dólar se fortaleceu hoje — o oposto da tendência que a última PTAX oficial mostrava —
mas esta leitura **não estima um novo valor de câmbio** por conta própria; registra apenas a
divergência qualitativa entre a notícia e o último dado numérico disponível, e recomenda
tratar qualquer leitura de paridade em reais com cautela até a publicação de amanhã.

**2. Paridade em reais (`soja_paridade_br`) de hoje mistura CBOT fresco com câmbio de três
dias atrás.** O indicador oficial (R$ 133,08/saca, base 06/07) usa a PTAX de 03/07/2026
(5,1717) porque não há PTAX mais recente disponível — 100% do movimento de +2,96 BRL/sc
frente a 02/07 vem do CBOT, zero do câmbio. Se a manchete de dólar mais forte se confirmar
amanhã, a paridade real (quando recalculada) deve ficar ainda mais alta do que os R$ 133,08
hoje mostrados, mas esta leitura não antecipa esse número.

**3. A atribuição da virada do ISF/ISO ao efeito calendário ABIOVE não pôde ser confirmada
por consulta direta ao banco de dados.** O ambiente de execução deste insight não tem acesso
ao banco SQLite do sistema (apenas ao dump `briefing/latest.md`), então a conclusão de que a
rolagem do mês de referência (junho→julho) é a causa da inversão dos índices — reforçada hoje
pela estabilidade do novo patamar por seis pregões seguidos — é uma inferência lógica bem
fundamentada, mas não uma verificação direta linha a linha do código.

**4. NOPA — dado inacessível há mais de um mês** (fila `release-nopa-2026-07-06` tratada
aqui). `monthly_status = 0.0 bool` (indicadores, 06/07/2026). O esmagamento americano de
junho/2026 segue sem fonte primária acessível.

**5. Palma malaia (MPOB) — 21 dias consecutivos sem dados numéricos** (16/jun a 06/07/2026).
O parser continua retornando apenas 3.428 chars de HTML sem valores extraídos. Sem os preços
de CPO na BMD, não é possível quantificar o efeito do El Niño nem das restrições
regulatórias indonésias sobre a produção e o prêmio de substituição para o óleo de soja
americano.

**6. RIN D4 como parâmetro fixo (2,11 USD/RIN) segue sendo a maior fonte de incerteza do
modelo de biodiesel.** Não há dado de mercado secundário no briefing para confirmar se o
valor real mudou, apesar do EPA Final RFS ter elevado os volumes obrigatórios desde 15/06.

**7. COT com defasagem de 13 dias em relação ao evento USDA de fim de junho e ao rali de
hoje.** O dado mais recente segue sendo de 23/06/2026 — deixa às cegas a leitura de como os
fundos reagiram tanto ao movimento de preço do fim de junho quanto ao de hoje, o mais forte
da série.

**8. Físico de Paranaguá, praças de farelo BR e prêmios de exportação (PGUA) sem atualização
para 06/07/2026** — todos travados em 03/07/2026. Qualquer leitura de basis interno hoje
(por exemplo, o desconto do interior do Paraná frente à paridade oficial) é mecanicamente
distorcida pela paridade ter subido com o CBOT enquanto o físico não teve pregão novo — não
deve ser lida como enfraquecimento genuíno de basis até confirmação com dado fresco.

**9. BCBA Argentina — sem relatórios de esmagamento/exportação acessíveis via scraper**
(page_fetched=1,0 mas sem links de relatório, 06/07/2026). O ritmo de processamento
argentino pós-colheita (50,1 mi t) é estimado por notícia, não medido por fonte primária.

**10. Percentis históricos de COT não calculados** — os 103k net longs em óleo, 12k em
farelo (com 98k shorts) e 37k em soja são grandes em termos absolutos, mas sem série
histórica completa para calibrar percentil.

*Nenhum número foi inventado ou estimado além do que consta no briefing de 06/07/2026 e nos
insights anteriores referenciados. A maior contribuição desta leitura foi identificar que o
ratio Far/Soj rompeu 80% pela primeira vez desde a origem da tese (11/06), tratando isso como
o desenvolvimento mais importante do dia sem, no entanto, declarar confirmação operacional
antes do protocolo original (2-3 fechamentos) ser satisfeito — e documentar com transparência
que o câmbio e o físico BR ainda não capturaram o rali de hoje, o que exige cautela redobrada
sobre qualquer leitura fina de paridade ou basis até a próxima atualização.*
