---
data: 2026-07-03
titulo: "Feriado de 4 de julho (observado nesta sexta) trava o pregão do complexo — sem novo fechamento em soja/farelo/óleo —, mas a liquidação oficial de 02/jul revisa para baixo o preço de farelo e para cima o de óleo frente ao que a leitura de ontem publicou, e o ratio Far/Soj corrigido (80,66%, não 81,24%) volta a comprimir rumo ao gatilho de 80% em vez de se afastar dele"
tags: [complexo, auto-claude]
fontes:
  - CBOT CME (ZSQ26/ZMQ26/ZLQ26 + curva forward completa) — fechamento OFICIAL (settlement) de 2026-07-02, que revisa os valores intraday usados na leitura de 2026-07-02 (ver Honestidade #1 — a divergência mais material das últimas leituras)
  - CBOT CME HO=F (heating oil) — sessão eletrônica de 2026-07-03 (volume 1.575 contratos, muito abaixo do padrão de ~50 mil; feriado de 4 de julho observado nos EUA nesta sexta-feira, sem sessão para o complexo soja)
  - BCB PTAX — 2026-07-02 (USD/BRL 5,1945; EUR/BRL 5,9472)
  - CEPEA/ESALQ Paranaguá via NAG — 2026-07-02 (R$ 135,08/sc, var +0,57%)
  - NAG Físico BR (farelo MT/IMEA, RS, Rondonópolis; prêmio PGUA farelo/óleo; soja Paraná interior) — 2026-07-02
  - CFTC COT Managed Money — 2026-06-23 (10º dia sem publicação nova, ver Riscos)
  - USDA Crop Progress — 2026-06-28 (sem atualização nova)
  - NOAA CPC ENSO — 2026-07-03 (El Niño Advisory)
  - INMET — 2026-07-03 (praças MT/PR/RS/GO)
  - ABIOVE projeções mensais — coleta recente (balanços ago-dez/2026, farelo/óleo/soja)
  - Indicadores sintéticos (crush, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel) — 2026-07-02; ISF/ISO — 2026-07-03
  - MPOB — 2026-07-03 (18º dia consecutivo sem números extraídos)
  - NOPA — 2026-07-03 (32º+ dia consecutivo inacessível)
  - Notícias Agrícolas / Farm Progress RSS — 2026-07-02/03
  - Forecasts estatísticos internos — 2026-07-03
  - Cruza com [[2026-07-02_leitura-complexo]], [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]], [[2026-05-26_pis-cofins-biodiesel-explica-mercado-fisico-fraco]], [[2026-05-26_subvencao-fossil-aperta-biodiesel]], [[2026-05-26_b16-bullish-farelo]], [[2026-05-26_curva-forward-cbot-oleo-desacopla]]
status: ativa
vies: [neutral-soja, bear-farelo, bear-oleo]
---

## Visão geral

O complexo soja funciona como uma fábrica com uma matéria-prima (a soja em grão) e dois
produtos de saída, gerados na mesma proporção fixa a cada bushel esmagado: o **farelo**
(a fração proteica, vira ingrediente de ração animal) e o **óleo degomado** (a fração de
gordura, vira óleo de cozinha e, cada vez mais, biodiesel). Quem decide o ritmo de
esmagamento é a esmagadora, olhando para a **crush margin** — o valor de mercado do
farelo + óleo produzidos por um bushel, menos o custo daquele bushel de soja. Hoje é um
dia atípico para julgar esse mecanismo: **os Estados Unidos observam o feriado de 4 de
julho nesta sexta-feira** (o dia 4 cai num sábado, então a bolsa fecha antecipadamente
o pregão do complexo agrícola) — não há fechamento novo de soja, farelo ou óleo na CBOT
hoje. A única cotação que aparece com data de hoje é o heating oil (HO=F), que negocia
quase 24 horas por dia em mercado eletrônico e por isso registrou uma sessão fina de
apenas **1.575 contratos** (CME, 03/jul/2026) — uma fração dos ~51 mil contratos de
volume normal — praticamente andando de lado (abertura 3,1793, fechamento 3,1802 USD/gal).
Não há sinal direcional a extrair daí.

**O verdadeiro fato do dia não é de mercado — é de dado.** O dump de hoje traz o
fechamento **oficial (settlement)** da sessão de 02/07/2026, e ele diverge de forma
material dos números que a leitura de ontem publicou como sendo o fechamento daquele
mesmo dia. A leitura de 02/jul descreveu soja fechando em 1.138,50 cts/bu, farelo em
308,30 e óleo em 66,65, todos com volume muito baixo (soja 3.661, farelo 1.524, óleo
4.204 contratos) — e interpretou isso como uma sessão de véspera de feriado, com pouca
liquidez. O dado assentado que chega hoje mostra outra realidade: soja fechou em
**1.136,25 cts/bu**, farelo em **305,50 USD/sht**, óleo em **66,77 cts/lb** — e, mais
importante, com volumes **normais/robustos** (soja 30.203, farelo 29.331, óleo 65.270
contratos, CBOT CME, 02/07/2026), muito acima do que a leitura de ontem registrou. Ou
seja: a sessão de 02/jul não foi de liquidez fraca — foi uma sessão cheia, e o número
de baixo volume publicado ontem veio de um recorte intraday capturado antes do book
fechar. Esse detalhe importa porque muda a confiança que se deve depositar no
fechamento de 02/jul: com volume pleno confirmado, ele é **mais** confiável do que a
leitura de ontem supôs, não menos — só que os níveis de preço, e por consequência todos
os indicadores derivados (crush, ratio Far/Soj, oil share, margem de biodiesel), mudam.
Essa é a maior divergência de dado já registrada nesta série de leituras diárias e está
detalhada, linha a linha, na seção Honestidade #1 — mas o efeito prático já está
incorporado nas seções de Soja, Farelo, Óleo e Spreads abaixo, todas recalculadas com o
dado assentado.

A consequência mais relevante da correção é no **ratio Far/Soj** — o preço do farelo
dividido pelo da soja, na mesma base, que mede se o farelo está "caro" ou "barato" frente
ao grão que o origina. Valores baixos (<80%) sinalizam farelo abundante/barato; valores
altos (≥87%) sinalizam farelo apertado. A leitura de ontem, usando o dado intraday, tinha
o ratio subindo para 81,24% e concluiu que ele estava **se afastando** do gatilho
psicológico de 80%. Com o dado assentado de hoje, o ratio de 02/jul foi na verdade
**80,66%** — o terceiro recuo consecutivo (81,09% em 30/jun → 80,82% em 01/jul → 80,66%
em 02/jul) e o segundo valor mais próximo de 80% em toda a série observada desde a
origem da tese em 11/jun (só o mínimo de 80,30%, tocado em 26/jun, ficou mais perto).
Isso inverte o sinal: a compressão do ratio **está retomando**, não revertendo — o que
é exatamente o que a fila de julgamento de hoje cobra ao marcar a revisão D+7 da tese
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` como **vencida**
(tratada em detalhe na seção Farelo). O segundo efeito da correção é no **oil share**
(a fração do valor do crush que vem do óleo): a leitura de ontem via cinco pregões
seguidos de queda, projetando o cruzamento de 50% em cerca de oito sessões. O dado
assentado mostra o oil share de 02/jul em 52,22%, praticamente **estável** frente aos
52,20% de 01/jul (+0,02 p.p.) — a sequência de queda, na verdade, estagnou. E o terceiro
efeito é na **margem de biodiesel americana**: em vez de recuperar para 0,6197 USD/gal
como a leitura de ontem descreveu, o dado assentado mostra a margem **caindo** para
0,5395 USD/gal (de 0,5811 em 01/jul) — uma queda de -7,2%, não uma recuperação de +6,6%.

**O que sustenta a leitura de hoje, então, é uma combinação rara: nenhuma sessão nova de
preço, mas uma correção de dado que muda a inclinação de três indicadores-chave.** O
pivô do complexo continua sendo o mesmo da véspera — a tensão entre um óleo estrutural-
mente dominante no crush (o Índice de Suporte do Óleo segue em 100/100, 5/5 condições,
pelo terceiro pregão seguido) e um farelo estruturalmente sobrando (Índice de Sobra do
Farelo em 80/100, 4/5, também estável há três sessões) — mas o ratio Far/Soj corrigido
mostra que essa tensão está mais perto de um ponto de inflexão operacional (o gatilho de
80%) do que a leitura de ontem sugeriu. A maior convicção da casa segue sendo o
**bear-farelo estrutural** (exportação ABIOVE projetada caindo pela metade até dezembro,
detalhada na seção Farelo), agora reforçado por um ratio que volta a se aproximar do
nível de entrada do spread de convergência. O **bear-óleo tático** segue confirmado —
o fechamento de 66,77 cts/lb permanece abaixo do suporte-virou-resistência de 72,00 (fila
`alerta-quebra_suporte-oleo_cbot-2026-07-02`, tratada na seção Óleo) — e ganha um dado
de reforço com a correção: a margem de biodiesel caindo, não subindo. A **soja** segue
neutra, com o ganho de dois pregões agora recalculado para +12,00 cts/bu (não +14,25) e
concentrado majoritariamente no pregão de 01/jul, não no de 02/jul. Confiança alta na
tese estrutural do farelo e na leitura do óleo abaixo do suporte; confiança moderada na
inflexão de alta da soja, ainda mais cautelosa depois da correção de dado; e uma nota de
honestidade importante sobre a qualidade do pipeline de dados intraday vs. settlement,
que já é a segunda ocorrência do mesmo tipo de divergência em duas leituras seguidas.

---

## Soja

**Viés: neutro — ganho de dois pregões pós-USDA recalculado para +12,00 cts/bu (não
+14,25 cts/bu como reportado ontem), concentrado no pregão de 01/jul; hoje não há sessão
nova (feriado de 4 de julho observado); forecast de 30 dias segue altista, o de 7 dias
segue lateral**

### O que sustenta a leitura

A soja de agosto (ZSQ26.CBT) fechou **oficialmente** em **1.136,25 cts/bu** no pregão de
02/07/2026 (CBOT CME, dado assentado no dump de hoje), com abertura 1.132,50, máxima
1.142,75 e mínima 1.131,50, sobre volume de **30.203 contratos** — muito acima dos 3.661
contratos que a leitura de ontem havia registrado para essa mesma sessão (ver Honestidade
#1). O fechamento assentado (1.136,25) é **2,25 cts/bu mais baixo** do que o valor
intraday usado ontem (1.138,50). Recalculando a sequência dos três últimos pregões com o
dado corrigido: 1.124,25 (30/jun, pós-USDA Acreage/Quarterly Stocks) → 1.133,25 (01/jul,
+9,00) → **1.136,25 (02/jul, +3,00)** — um ganho acumulado de **+12,00 cts/bu (+1,07%)**
em dois pregões, menor que os +14,25 cts/bu (+1,27%) publicados ontem, e com a maior
parte do movimento (+9,00 dos +12,00, ou 75% do ganho) concentrada no pregão de 01/jul,
não distribuída igualmente entre os dois dias como a leitura anterior descreveu. Isso não
muda a direção da tese — a soja segue em viés de alta tática desde o USDA — mas reduz a
magnitude e a "aceleração" que a leitura de ontem viu no segundo pregão.

**Hoje, 03/07/2026, é dia de feriado observado nos EUA** (Independence Day, 4 de julho,
que cai num sábado neste calendário) — não há pregão novo do complexo agrícola. A única
cotação com data de hoje no dump é o heating oil eletrônico, que não é usado para julgar
soja diretamente, mas confirma o padrão: volume de apenas 1.575 contratos (CME,
03/07/2026) ante o padrão de ~50 mil, o mercado efetivamente parado.

**A curva forward de soja (02/07/2026, recalculada com o spot corrigido):**

| Vencimento | Código | Preço (cts/bu) | Var. vs Ago |
|---|---|---|---|
| Julho/26 | N26 | 1.131,75 | −4,50 |
| Agosto/26 | Q26 | 1.136,25 | — (spot) |
| Setembro/26 | U26 | 1.136,00 | −0,25 |
| Novembro/26 | X26 | 1.147,75 | +11,50 |
| Janeiro/27 | F27 | 1.162,25 | +26,00 |
| Março/27 | H27 | 1.168,25 | +32,00 |

O contango de novembro sobre agosto está em **+11,50 cts/bu**, mais comprimido do que os
+15,50 calculados ontem com o spot errado, e bem mais comprimido que os +20,00 de dois
dias atrás. A curva mais achatada é consistente com o spot corrigido ser mais baixo
(1.136,25 vs 1.138,50): o contrato-frente cedeu um pouco mais do que os vencimentos
distantes, então o carry relativo aumentou ligeiramente. O contrato de julho (N26), que
já havia saído da tela na leitura de ontem, reaparece hoje no dump — mas a 1.131,75,
abaixo do spot de agosto, um padrão mecânico de vencimento próximo (liquidação de
posição, não sinal de mercado).

**As condições de lavoura americana seguem sem atualização nova.** O USDA Crop Progress
mais recente continua sendo o de 28/06/2026: 65% good/excellent (10% excellent + 55%
good), 6% poor, 96% emergido — uma leve deterioração frente aos 66% G/E (10+56) e 5%
poor de 21/06/2026, mas com a emergência avançando de 93% para 96%. O relatório da
próxima segunda-feira (06/07) pode atrasar por causa do feriado (ver Riscos). O El Niño
Advisory segue confirmado (NOAA CPC, 03/07/2026), sem mudança de status — estatistica-
mente associado a umidade acima do normal no Corn Belt durante o florescimento (segunda
quinzena de julho), reduzindo o prêmio de risco climático que o mercado precisaria pagar
por proteção antecipada.

**No Brasil, a paridade recalculada é mais baixa do que a leitura de ontem publicou, mas
o físico de Paranaguá subiu de verdade.** A PTAX mais recente (BCB, 02/07/2026) ficou em
**5,1945 BRL/USD**, praticamente estável frente aos 5,1950 de 01/07 (-0,0005, -0,01%) —
o câmbio não é o fator do dia. Com o CBOT corrigido (1.136,25) e essa PTAX, a paridade
recalculada é **130,12 BRL/sc** (indicadores, 02/07/2026) — mais baixa que os 130,39
publicados ontem (que usavam o spot intraday errado de 1.138,50), mas ainda **acima**
dos 129,79 de 01/07/2026 (+0,33 BRL/sc no dia). A soja física em Paranaguá (CEPEA/ESALQ
via NAG, **02/07/2026, dado novo e genuíno, não afetado pela revisão do CBOT**) subiu
para **R$ 135,08/sc** (+0,57% no dia, ante R$ 134,32 em 01/07) — o ganho absoluto (+0,76
BRL/sc) foi maior que o da paridade de papel (+0,33 BRL/sc) nesse mesmo intervalo. O
resultado é que o **basis de exportação implícito (Paranaguá menos paridade) na verdade
ampliou de +4,53 BRL/sc (01/jul, recalculado) para +4,96 BRL/sc hoje** — o oposto da
leitura de ontem, que via o basis comprimindo para +3,93 (um número construído sobre a
paridade inflada pelo spot intraday errado). Com o dado corrigido, a leitura correta é:
o físico de Paranaguá está acompanhando ou até superando o papel, não ficando para trás
— um sinal levemente mais positivo para a demanda de exportação brasileira do que a
leitura anterior sugeriu. No interior do Paraná (NAG, 02/07/2026), a soja subiu para
R$ 127,87/sc (+0,04%), permanecendo **abaixo** da paridade recalculada (130,12) — um
desconto de -2,25 BRL/sc, que é na verdade **mais estreito** que o -2,57 publicado ontem
(efeito da correção da paridade), mas que continua a trajetória genuína de alargamento
observada nos últimos três pregões usando apenas dados não revisados: -0,87 (30/jun) →
-1,97 (01/jul) → -2,25 (02/jul) — o físico do interior paranaense segue perdendo terreno
para o papel, mesmo com a correção.

**O posicionamento dos fundos (COT de 23/06/2026, CFTC — 10º dia sem publicação nova,
ver Riscos)** mostra managed money net long em soja de +36.986 contratos (3,7% do open
interest de 1.006.834) — inalterado, sem dado novo para confirmar se os fundos
participaram do rali de dois pregões pós-USDA ou se o movimento veio de outro tipo de
player (comercial, produtor).

**Os forecasts estatísticos internos (03/07/2026, gerados com o spot corrigido de
1.136,25, idêntico ao de ontem por não haver sessão nova hoje)** mostram: central 7d =
**1.137,54 cts/bu** (bandas 1.087,70-1.187,38), viés **lateral**; central 30d =
**1.144,21 cts/bu** (bandas 1.041,03-1.247,40), viés **altista** — ambos praticamente
idênticos aos gerados ontem (1.139,64 e 1.146,36, respectivamente), com a pequena
diferença explicada apenas pela correção do spot de entrada. O modelo, puramente
estatístico e sem fundamento embutido, mantém a leitura de "sem tendência forte
confirmada no curto prazo, mas inclinação de alta capturada na janela de 30 dias".

### O que invalida / risco para a soja

- **A ausência de sessão nova hoje esconder um movimento que só aparecerá na reabertura
  da próxima semana:** sem pregão, não há como testar se o rali de dois dias tem
  continuidade — a primeira leitura confiável só vem com a normalização de liquidez na
  semana de 06-10/jul.
- **WASDE de julho (~10/07/2026) reverter a leitura de "oferta grande":** se o USDA
  cortar área ou produção de forma expressiva, reforça a alta; se confirmar oferta
  ampla, o rali recalculado (+12,00 cts/bu, menor do que se pensava) perde ainda mais
  força relativa.
- **Onda de calor no Corn Belt na segunda quinzena de julho** (florescimento): sem sinal
  nos dados disponíveis, mas segue o principal risco climático de curto prazo.
- **Basis Paranaguá-paridade reverter a ampliação de hoje:** o basis corrigido (+4,96
  BRL/sc) é mais saudável do que se pensava ontem, mas ainda é um dado de apenas um
  pregão — precisa de confirmação.
- **China anunciando compras relevantes de soja americana:** nenhum sinal disso no
  noticiário monitorado hoje.

### Leitura operacional — soja

Com a correção de dado, o viés de alta tática em soja fica um pouco mais modesto do que
a leitura de ontem descreveu — o ganho de dois pregões é real, mas menor (+12,00 cts/bu,
não +14,25) e concentrado no primeiro dos dois pregões, não em ambos igualmente. Para
quem opera os dois lados, isso não muda a direção da tese, mas reduz a convicção de que
o movimento está "acelerando" — a leitura mais honesta é "ganho pós-USDA que perdeu
fôlego no segundo pregão, e hoje sequer teve pregão para testar continuidade". Quem tem
posição física pode reavaliar fixação parcial no basis de Paranaguá, que na verdade
ampliou hoje (+4,96 BRL/sc, recalculado) — um dado mais favorável à originação do que a
leitura de ontem sugeria, ainda que o nível absoluto (R$ 135,08/sc) continue abaixo dos
R$ 140+ que tipicamente destravam fixação em volume. O catalisador que decide a tese nas
próximas duas semanas continua sendo o WASDE de julho (~10/jul), e a semana que vem
(06-10/jul) é a primeira com volume pleno para validar ou desmentir o rali.

---

## Farelo

**Viés: bear estrutural — a correção de dado mostra o ratio Far/Soj retomando a
compressão rumo ao gatilho de 80% (80,66% em 02/jul corrigido, não 81,24% como
reportado ontem), tratando a revisão D+7 vencida da fila
(`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`); exportação ABIOVE
projetada seguindo em queda pela metade até dezembro; Rondonópolis sustenta o salto de
físico por segundo pregão consecutivo**

### O que sustenta a tese bear

O farelo de agosto (ZMQ26.CBT) fechou **oficialmente** em **305,50 USD/sht** no pregão
de 02/07/2026 (CBOT CME, dado assentado), com abertura 306,60, máxima 309,20 e mínima
305,10, sobre volume de **29.331 contratos** — de novo, muito acima dos 1.524 contratos
que a leitura de ontem havia registrado. O fechamento assentado é **2,80 USD/sht mais
baixo** que o valor intraday usado ontem (308,30). Recalculando a sequência: 303,90
(30/jun) → 305,30 (01/jul, +1,40) → **305,50 (02/jul, +0,20)** — um ganho acumulado de
apenas **+1,60 USD/sht (+0,53%)** em dois pregões, muito menor que os +4,40 (+1,45%)
publicados ontem, e com o pregão de 02/jul praticamente estagnado (+0,20, não +3,00
como se pensava). Essa correção muda o quadro tático do farelo de forma relevante: o
que parecia um rali de dois dias concentrado e forte era, na realidade, um pequeno
repique de um dia (01/jul) seguido de estabilidade (02/jul).

**Tratando a fila `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`,**
marcada como **vencida** hoje: a tese original (11/06/2026) projetou o ratio Far/Soj
cruzando 80% "em 1-2 semanas"; o checkpoint formal D+7 caiu em 18/06/2026 e nunca foi
oficialmente fechado — hoje, D+22 da origem (11/jun → 03/jul), o sistema volta a
cobrar esse julgamento. A trajetória completa, agora **recalculada com o dado assentado
de 02/jul**:

| Data | Ratio Far/Soj | Evento |
|---|---|---|
| 11/jun | 81,4% | origem da tese (compressão rápida) |
| 26/jun | 80,30% | ponto mais próximo do cruzamento até então |
| 29/jun | 81,43% | reverte para cima (pré-USDA) |
| 30/jun | 81,09% | pós-USDA, recuando |
| 01/jul | 80,82% | segue recuando em direção a 80% |
| 02/jul | **80,66%** | **corrigido — terceiro recuo consecutivo, 2º valor mais próximo de 80% da série** |

Com o dado intraday que a leitura de ontem usou, o ratio de 02/jul aparecia em 81,24% —
uma reversão para cima que "afastava" o gatilho. Com o dado assentado, o ratio real foi
**80,66%**, ou seja, a compressão **não reverteu**: são três pregões seguidos de recuo
(81,09% → 80,82% → 80,66%), e o nível de hoje está a apenas 0,66 p.p. do gatilho
psicológico de 80% — a segunda maior proximidade de toda a série, atrás apenas do
mínimo de 80,30% tocado em 26/jun. O veredito de honestidade sobre a fila, corrigido:
**o gatilho de spread (ratio sustentado abaixo de 80% por 2-3 pregões) segue não
confirmado 22 dias após a origem da tese, mas a trajetória de aproximação está ativa
de novo**, ao contrário do que a leitura de ontem concluiu. Isso reforça, não enfraquece,
a tese estrutural bear-farelo, e aproxima — sem ainda confirmar — o gatilho operacional
do spread de convergência (long farelo / short soja). O checkpoint D+90 (09/09/2026)
permanece como horizonte formal de avaliação da tese original.

**Tratando a fila `release-nopa-2026-07-03`:** o sistema volta a identificar um item
NOPA, agora com data de 03/07/2026. O briefing confirma: `nopa | monthly_status: 0.0
bool` (indicadores, 03/07/2026) — o relatório mensal de crush americano da NOPA
(National Oilseed Processors Association) segue inacessível por exigir membership
pago, pelo menos o **32º dia consecutivo** nessa condição. Sem dado novo para
interpretar; a lacuna persiste (ver Honestidade).

**O oil share, recalculado com o dado assentado, na verdade estagnou em vez de continuar
caindo.** A leitura de ontem via 51,94% em 02/jul, o quinto pregão seguido de queda, e
projetava o teste de 50% em cerca de oito sessões. O dado corrigido mostra o oil share
de 02/jul em **52,22%** (indicadores, 02/07/2026) — praticamente estável frente aos
52,20% de 01/07 (+0,02 p.p.), interrompendo a sequência de queda que vinha desde 29/jun
(53,12% → 52,41% → 52,20% → 52,22%). O mecanismo segue o mesmo — o óleo ainda domina o
crush (>50%), então a esmagadora "paga a conta" com o óleo e aceita vender o farelo pelo
preço que o mercado oferecer — mas a corrida rumo a 50% que a leitura de ontem descrevia
como iminente, na realidade, não está em curso no momento: o oil share estabilizou no
patamar de ~52% pelos últimos dois pregões. Isso não muda a tese estrutural (o farelo
continua sendo o "resto" do crush), mas remove um argumento de urgência que a leitura
anterior havia levantado.

**Os dados projetados da ABIOVE (coleta recente, sem alteração desde a última leitura)
seguem mostrando a exportação de farelo brasileiro recuando pela metade entre agosto e
dezembro/2026:** 1.400 mil t (agosto) → 1.100 (setembro) → 850 (outubro) → 800
(novembro) → **700 mil t (dezembro)** — uma queda de -50% no ritmo de escoamento
externo em quatro meses, mesmo com a produção mensal projetada permanecendo em patamar
elevado (2.285 mil t em agosto caindo para 1.659 em dezembro, proporcionalmente menos
acentuada que a exportação). O mecanismo é direto: se a produção de farelo cai menos
rápido que a exportação, mais farelo fica represado no mercado doméstico brasileiro no
2º semestre — pressão baixista adicional sobre o físico interno, independentemente do
que acontecer no CBOT. O estoque final projetado de farelo sobe de 1.016 mil t
(setembro) para 1.224 (agosto, base) antes de recuar apenas gradualmente para 1.015
(dezembro) — o estoque doméstico não desincha na velocidade que a queda de exportação
sozinha sugeriria, reforçando a leitura de sobra estrutural. Este é o driver mais
concreto e menos sujeito a ruído de dado intraday desta tese — não depende do
fechamento diário da CBOT.

**O prêmio de exportação do farelo em Paranaguá segue em +0,05 USD/sht** (NAG,
02/07/2026, mês de referência julho/26) — praticamente nulo, confirmando que o Brasil
não tem vantagem competitiva de preço sobre a Argentina, que concluiu 98% da colheita
com 50,1 milhões de toneladas (Canal Rural, 27/06/2026, dado mais recente disponível) e
processará essa soja com logística mais barata via Rio Paraná/San Lorenzo.

**As cotações físicas do farelo no Brasil confirmam que o salto de Rondonópolis não foi
ruído de um dia.** MT/IMEA segue travado em R$ 1.544,35/ton (NAG, 02/07/2026, inalterado
desde pelo menos 22/06) e RS em R$ 1.640/ton (também inalterado) — mas **Rondonópolis/MT
sustentou o novo patamar de R$ 1.650,00/ton (var 0,0% frente a 01/07)**, segunda leitura
seguida nesse nível após o salto de +10% registrado em 01/07 (de R$ 1.500 para R$
1.650). Como as outras duas praças seguem paradas, esse ainda não é um movimento
regional — mas dois pregões consecutivos no novo patamar aumentam a probabilidade de
que seja um reposicionamento real de basis local (possivelmente logístico ou de
demanda pontual em Rondonópolis) e não um erro de coleta isolado. Continua sendo
monitorado, agora com peso maior de confirmação, sem ainda ser incorporado como
reversão da tese bear estrutural.

**A curva forward do farelo (02/07/2026, recalculada com o spot corrigido):**

| Vencimento | Código | Preço (USD/sht) | Var. vs Ago |
|---|---|---|---|
| Julho/26 | N26 | 307,70 | +2,20 |
| Agosto/26 | Q26 | 305,50 | — (spot) |
| Setembro/26 | U26 | 303,10 | −2,40 |
| Outubro/26 | V26 | 301,40 | −4,10 |
| Dezembro/26 | Z26 | 304,40 | −1,10 |
| Janeiro/27 | F27 | 306,00 | +0,50 |

O contrato de janeiro/27 (F27), que ontem havia fechado "colado" no spot de agosto
(coincidência tratada com ceticismo na leitura anterior), hoje aparece com um preço
diferente (306,00 vs 305,50 do spot) — um sinal de que aquele "empate" de ontem era
mesmo um artefato de baixíssima liquidez/cotação travada, não uma leitura genuína de
curva plana no longo prazo, como já se suspeitava. O outubro (V26) segue testando a
região de 300-305 USD/sht, coincidindo com o pico sazonal de esmagamento simultâneo
Brasil + Argentina (ABIOVE projeta 2.846 mil t de esmagamento em outubro, o maior mês
do ano) — o mercado de futuros continua precificando o farelo mais fraco no 4º
trimestre.

**O posicionamento dos fundos (COT de 23/06/2026, sem atualização nova — 10º dia)**
segue como o dado mais revelador disponível: managed money net long de apenas +12.359
contratos, com longs em 110.276 e **shorts em 97.917** (15,8% do open interest de
619.446 em posições vendidas de managed money) — os fundos mantêm posição vendida
ativa. Sem COT novo, não é possível confirmar se essa posição mudou nas duas semanas
seguintes ao USDA de 30/06.

### O que invalida / risco para o farelo

- **Ratio Far/Soj romper 80% de forma sustentada (2-3 pregões consecutivos abaixo):**
  hoje, com o dado corrigido, o ratio está em 80,66% e recuando pelo terceiro pregão
  seguido — o mais perto do gatilho desde 26/jun. Monitorar o próximo fechamento (só
  disponível na reabertura pós-feriado) com atenção redobrada.
- **Oil share retomar a queda para baixo de 50%:** hoje estagnado em 52,22% (dois
  pregões estáveis), removendo a urgência que a leitura anterior via — mas se voltar a
  cair, o teste de 50% muda o mecanismo central da tese bear.
- **Crush margin voltar a comprimir de forma sustentada abaixo de 2,50 USD/bu:** hoje
  (recalculado) em 2,7032, ainda em leve queda (-0,62% no dia), não estabilizada como a
  leitura de ontem descreveu.
- **WASDE de julho (~10/jul) reduzir a área de soja americana de forma expressiva:**
  menos esmagamento no 4T26 → menos farelo global, risco de short squeeze nos 97.917
  contratos vendidos por fundos.
- **Rondonópolis/MT reverter o novo patamar:** dois pregões consecutivos aumentam a
  confiança no movimento, mas ainda não há explicação disponível no briefing — uma
  reversão rápida sugeriria evento pontual, não estrutural.

### Leitura operacional — farelo

O bear-farelo estrutural segue com a maior convicção da leitura, e hoje ganha reforço em
dois pontos: o ratio Far/Soj corrigido está retomando a aproximação do gatilho de 80%
(não se afastando, como se pensava ontem), e a exportação ABIOVE projetada caindo pela
metade até dezembro continua sendo o driver mais sólido, imune à correção de dado da
CBOT. Para quem já está posicionado no short estrutural, o fechamento corrigido de
305,50 (não 308,30) dá mais folga frente à zona de stop de referência 308-310 USD/sht
do que a leitura de ontem sugeria — vale reavaliar essa referência com o dado assentado.
Para quem quer montar o spread Far/Soj de convergência (long farelo/short soja), a
régua operacional segue a mesma — aguardar ruptura confirmada abaixo de 80% por 2-3
pregões — mas hoje essa confirmação ficou **mais próxima**, não mais distante: com o
ratio em 80,66% e recuando, um único pregão de continuidade na direção certa poderia
completar o gatilho assim que o mercado reabrir.

---

## Óleo

**Viés: bear tático confirmado — fechamento corrigido de 66,77 cts/lb (fila
`alerta-quebra_suporte-oleo_cbot-2026-07-02`) segue abaixo do suporte-virou-resistência
72,00; a margem de biodiesel, recalculada, caiu (não subiu) para 0,5395 USD/gal**

### Tratando a fila `alerta-quebra_suporte-oleo_cbot-2026-07-02`

O alerta de hoje reporta óleo fechando em 66,77 cts/lb, abaixo do nível de referência
72,00. A pergunta operacional: confirma ou muda a tese?

**Confirma a quebra estrutural — e o dado corrigido mostra o óleo levemente mais forte
do que se pensava, mas ainda preso abaixo do suporte.**

O óleo de agosto (ZLQ26.CBT) fechou **oficialmente** em **66,77 cts/lb** no pregão de
02/07/2026 (CBOT CME, dado assentado), com abertura 66,80, máxima 67,58 e mínima 66,12,
sobre volume de **65.270 contratos** — de novo, muito acima dos 4.204 contratos
registrados ontem. O fechamento assentado é **0,12 cts/lb mais alto** que o valor
intraday usado ontem (66,65) — o único dos três produtos em que a correção trabalha a
favor do preço, não contra. Recalculando: 66,93 (30/jun) → 66,69 (01/jul, -0,24) →
**66,77 (02/jul, +0,08)** — uma pequena recuperação no segundo pregão, coerente com a
leitura de "pausa técnica" que a leitura de ontem já havia identificado, ainda que com
números diferentes. O suporte de 72,00 continua rompido há mais de duas semanas e
segue funcionando como resistência — a essência da tese não muda com a correção.

**A margem de biodiesel americana, recalculada, caiu em vez de recuperar.** A leitura de
ontem reportou 0,6197 USD/galão para 02/jul, uma recuperação frente aos 0,5811 de
01/jul. O dado assentado de hoje mostra a margem em **0,5395 USD/galão** (indicadores,
02/07/2026: receita 6,3472 [HO 3,18 + 1,5×RIN 2,11] − custo 5,8077 [óleo 5,0077 + ind.
0,80]) — uma **queda** de -7,2% frente aos 0,5811 de ontem, não uma alta de +6,6%. A
série completa e recalculada: 0,3367 (26/jun) → 0,5322 (29/jun) → 0,6621 (30/jun) →
0,5811 (01/jul) → **0,5395 (02/jul)** — depois do pico de 30/jun, a margem vem
recuando por dois pregões seguidos, não um pregão de queda seguido de recuperação como a
leitura anterior descreveu. Isso é uma nuance bearish para o óleo: a margem segue
dentro da faixa de 0,50-0,80 USD/gal (a zona em que compradores voluntários de blending,
que operam acima do mandato B15, tendem a reforçar demanda), mas está se aproximando do
piso dessa faixa, não subindo em direção ao teto de 0,80 como a leitura de ontem
sugeria. A correção também alcança o heating oil (HO): o fechamento real de 02/jul foi
**3,1822 USD/gal** (CME, dado assentado), não os 3,2535 publicados ontem — uma diferença
de -0,0713 (-2,2%) que explica boa parte da revisão da margem, já que o HO é o principal
componente de receita do biodiesel.

**A curva forward do óleo (02/07/2026), recalculada com o spot corrigido, mantém
backwardation clara:**

| Vencimento | Código | Preço (cts/lb) | Var. vs Ago |
|---|---|---|---|
| Julho/26 | N26 | 66,95 | +0,18 |
| Agosto/26 | Q26 | 66,77 | — (spot) |
| Setembro/26 | U26 | 66,34 | −0,43 |
| Outubro/26 | V26 | 65,81 | −0,96 |
| Dezembro/26 | Z26 | 65,43 | −1,34 |
| Janeiro/27 | F27 | 65,33 | −1,44 |

A curva caindo -1,44 cts/lb de agosto a janeiro/27 (~0,24 cts/lb por mês de carry, um
pouco menos íngreme que o -0,31/mês calculado ontem com o spot errado) continua sendo o
argumento técnico mais forte para manter posição vendida de médio prazo: o shortista que
rola a posição mês a mês colhe esse carry independentemente da direção do preço à
vista.

**O posicionamento dos fundos (COT de 23/06/2026, sem atualização nova — 10º dia)**
segue sendo o maior risco de reversão mecânica do complexo: managed money net long de
+103.206 contratos, representando 15,7% do open interest de 658.976 — a maior exposição
relativa das três pernas. Sem dado novo do COT, não há como confirmar se o desmonte
observado nas semanas anteriores continuou durante e depois da sessão de maior volume do
trimestre (30/jun).

**O Índice de Suporte do Óleo (ISO) permanece em 100/100 (5/5 condições)** hoje
(indicadores, 03/07/2026), o **terceiro pregão seguido** nesse patamar desde a virada de
01/07 (quando subiu de 80/100) — mais um dia de estabilidade que reforça a hipótese,
levantada em leituras anteriores, de que a virada foi um efeito de calendário (rolagem
do mês-alvo de comparação ABIOVE de junho para julho), não uma mudança real de
fundamento. Três sessões consecutivas no novo patamar é uma amostra maior do que as duas
disponíveis ontem, mas segue sendo uma inferência lógica, não uma confirmação direta
(ver Honestidade).

### O que invalida / risco para o óleo

- **Margem de biodiesel ultrapassar 0,80 USD/gal de forma sustentada:** hoje em 0,5395,
  recuando dentro da faixa 0,50-0,80, mais perto do piso do que a leitura de ontem
  descreveu. Uma continuação da queda aproximaria o mercado do patamar em que a demanda
  voluntária de blending esfria, não do patamar em que ela se intensifica.
- **RIN D4 real acima de 2,40 USD/RIN** (o modelo usa 2,11 fixo): incerteza estrutural
  bidirecional já sinalizada em leituras anteriores, sem novo dado hoje.
- **Dados de palma malaia (MPOB) inacessíveis há 18+ dias consecutivos** (ver
  Honestidade) — se a produção de palma estiver caindo por El Niño, o óleo de soja
  ganharia prêmio de substituição global, o que seria altista.
- **WASDE de julho reduzir a área de soja americana:** menos esmagamento futuro nos EUA
  → menos óleo produzido → altista para os contratos de novembro em diante, impacto
  limitado no spot de agosto.
- **Exportação de óleo brasileiro projetada pela ABIOVE caindo de 110 mil t (setembro)
  para 45 (outubro) e 21 (novembro)** — menos óleo saindo do Brasil pode significar mais
  óleo represado internamente (bearish doméstico) ou mais disponibilidade para o
  mandato B15 (efeito ambíguo, precisa de mais dado).
- **B16 no Brasil antes de dezembro/2026:** ainda sem data no CNPE (ver Lente fiscal) —
  baixa probabilidade no horizonte de 2026, mas catalisador imediato de alta se ocorrer.

### Leitura operacional — óleo

O viés segue bear tático, com a quebra do suporte 72,00 confirmada por múltiplos
fechamentos consecutivos abaixo — inclusive o dado corrigido de hoje, que na verdade é
ligeiramente mais alto (66,77 vs 66,65 intraday), mas isso não muda a leitura estrutural.
O carry negativo da curva forward continua favorecendo posição vendida de médio prazo
(referência de stop em torno de 69,50-70,00 cts/lb, mantida da leitura anterior). A
correção da margem de biodiesel — caindo, não subindo — remove parte do argumento de
"piso de demanda se firmando" que a leitura de ontem havia levantado; a leitura mais
honesta hoje é que a margem está confortável dentro da faixa 0,50-0,80, mas caminhando
para o piso, não para o teto. Alvo primário do short seguindo os forecasts (central 7d =
64,31 cts/lb, indicadores, 03/07/2026): zona de 64-66 cts/lb. Alvo secundário (central
30d = 55,22): 55-58 cts/lb, mas esse cenário exige que a margem de biodiesel não
continue caindo — monitorar diariamente antes de assumir esse alvo como base.

---

## Spreads e crush — leitura de complexo

### Crush margin: 2,7032 USD/bu (corrigido) — segue em leve compressão, não estabilizada

A crush fechou em **2,7032 USD/bu** (Board Crush: farelo 305,50 + óleo 66,77 − soja
1.136,25; indicadores, 02/07/2026) — um valor **corrigido** frente aos 2,7291 publicados
ontem (que usavam os preços intraday errados). Com o dado assentado, a trajetória
recente é: 3,0657 (29/jun) → 2,8056 (30/jun) → 2,7200 (01/jul) → **2,7032 (02/jul,
-0,62%)** — a crush segue em leve queda, não estabilizada como a leitura de ontem
descreveu (que via um pequeno ganho de +0,3%). A magnitude da diferença é pequena, e a
crush segue comodamente acima do patamar narrativo de "alívio de esmagamento" (~2,50
USD/bu) — mas a direção correta é de continuidade da compressão suave, não de pausa.

### Ratio Far/Soj: 80,66% (corrigido) — retoma a compressão rumo ao gatilho de 80%, D+22 da tese sem confirmação

Como detalhado na seção de Farelo (tratando a fila `revisao-2026-06-11...D+7`, marcada
vencida hoje), o dado corrigido mostra o ratio em 80,66% no fechamento de 02/jul — o
terceiro recuo consecutivo (81,09% → 80,82% → 80,66%) e o segundo valor mais próximo do
gatilho de 80% em toda a série desde a origem da tese (11/jun). A leitura de ontem, com
o dado intraday, via o ratio subindo para 81,24% e concluía que ele se afastava do
gatilho — o dado assentado inverte essa conclusão. O gatilho operacional do spread de
convergência (long farelo/short soja) permanece **não confirmado**, mas hoje está mais
próximo, não mais distante, da confirmação.

### Oil share: 52,22% (corrigido) — estagnou, não continuou caindo

O dado corrigido mostra o oil share de 02/jul em 52,22%, praticamente igual aos 52,20%
de 01/jul (+0,02 p.p.) — interrompendo, na leitura correta, a sequência de queda que a
versão intraday sugeria estar em curso desde 29/jun. O óleo ainda domina o crush (>50%),
e a proximidade de 50% que preocupava a leitura de ontem perde urgência com a correção —
mas o item segue sendo o de maior sensibilidade estrutural do complexo e merece
monitoramento diário assim que o mercado reabrir.

### Oil-meal spread: 0,6237 USD/bu (corrigido) — estável, não em queda acelerada

O oil-meal spread (contribuição do óleo menos a do farelo por bushel), recalculado, ficou
em **0,6237 USD/bu** (indicadores, 02/07/2026) — praticamente igual aos 0,6193 de 01/jul
(+0,7%), não uma queda de -11,4% para 0,5489 como a leitura de ontem descreveu. A mesma
correção que afeta o oil share afeta este indicador, pela mesma mecânica: com os preços
assentados, óleo e farelo mantiveram suas posições relativas dentro do crush praticamente
estáveis entre 01/jul e 02/jul.

### ISF em 80/100, ISO em 100/100 — terceiro pregão seguido no novo patamar, hipótese de calendário reforçada

O Índice de Sobra de Farelo (ISF) segue em 80/100 (4/5 condições) e o Índice de Suporte
do Óleo (ISO) em 100/100 (5/5) — o mesmo patamar de 01/jul e 02/jul, agora o **terceiro**
pregão consecutivo desde a inversão observada em 01/jul. A estabilidade por três sessões
seguidas, já cobrindo o mês de julho inteiro, reforça a hipótese de que a virada foi um
efeito mecânico da rolagem do mês-alvo de comparação ABIOVE (junho → julho), e não uma
mudança real de fundamento — mas segue sendo uma inferência lógica, não uma confirmação
direta (ver Honestidade).

### O que os índices dizem juntos em 03/07/2026 (com a correção de dado incorporada)

ISF 80/100 (efeito calendário, terceira confirmação) + ISO 100/100 (idem) + ratio
80,66% corrigido (retomando a aproximação do gatilho de spread) + oil share 52,22%
corrigido (estagnado, não em colapso) + oil-meal spread 0,6237 USD/bu corrigido
(estável) + crush 2,7032 USD/bu corrigido (leve compressão contínua) + margem
biodiesel 0,5395 USD/gal corrigida (caindo, não recuperando) + COT (103k net longs em
óleo, 12k em farelo com 98k shorts ativos, 37k em soja, todos de 23/jun, 10º dia sem
atualização) + exportação de farelo ABIOVE caindo pela metade até dezembro (1.400 → 700
mil t) + Rondonópolis sustentando +10% por dois pregões + feriado de 4 de julho parando
o pregão hoje:

A leitura de hoje é, essencialmente, de **reconciliação de dado, não de novo movimento
de mercado**. Sem sessão nova, o "furo" do dia é a descoberta de que a sessão de 02/jul
— que a leitura anterior descreveu como fraca em liquidez e com farelo/soja subindo mais
forte que o óleo recuperando — foi, na realidade, uma sessão de volume pleno com um
padrão de preço sutilmente diferente: farelo e soja subiram bem menos do que se pensava,
o óleo subiu (não ficou estável), a crush comprimiu (não estabilizou), o ratio Far/Soj
retomou a queda rumo ao gatilho (não se afastou dele), o oil share estagnou (não
continuou caindo) e a margem de biodiesel caiu (não recuperou). Nenhuma dessas correções
muda a direção das teses estruturais (bear-farelo, bear-óleo tático, soja neutra) — mas
juntas, elas aproximam o complexo de um ponto de decisão operacional mais rápido do que
a leitura de ontem sugeria, especialmente no spread Far/Soj.

---

## Lente fiscal e regulatória BR

**Isenção PIS/Cofins biodiesel — 28 dias para o vencimento (31/07/2026).** Prazo fiscal
mais crítico do mês, inalterado desde a última leitura: a isenção de PIS/Cofins na saída
do biodiesel (concedida em abril/2026, prorrogada até 31/07/2026 por decreto de 29/mai)
elimina o direito de creditar o PIS/Cofins pago na entrada (compra de óleo de soja) —
transformando um crédito recuperável em custo efetivo (~R$ 1,35 bi/ano para o setor,
estimativa documentada em
[[2026-05-26_pis-cofins-biodiesel-explica-mercado-fisico-fraco]]). Sem sinalização
pública do MAPA ou MINFRA sobre renovação até hoje (03/07/2026). O checkpoint D+45 desse
insight (10/07/2026) cai em 7 dias, coincidindo quase exatamente com o WASDE de julho.

**B16 — sem data, travado em B15.** A reunião do CNPE que discutiria antecipação do B16
segue sem nova convocação desde o cancelamento de maio/2026. Testes técnicos do FNDCT
previstos para novembro-dezembro de 2026. Sem mudança de status.

**MP 1.363/2026 (subsídio ao diesel fóssil) — em vigor até 31/12/2026, faltam ~181
dias.** O subsídio de ~R$ 1,12/litro no diesel fóssil mantém o combustível mineral
artificialmente mais barato, reduzindo a competitividade do biodiesel para consumo
voluntário acima do mandato B15. Bearish estrutural persistente para a demanda
incremental de óleo de soja no mercado doméstico brasileiro.

**STJ REsp 2.165.276/2026 — crédito PIS/Cofins para esmagadoras.** Decisão de
21/05/2026 (unânime, 2ª Turma, não vinculante) que permite crédito de PIS/Cofins na
compra de soja sob suspensão fiscal, melhorando a margem econômica das esmagadoras em
~R$ 0,08-0,12/kg de farelo processado. Estruturalmente bearish para o farelo — incentiva
mais esmagamento, mais oferta de co-produtos. Coerente com a exportação de farelo ABIOVE
projetada em queda (mais oferta doméstica represada).

**PTAX 5,1945 BRL/USD (BCB, 02/07/2026).** O real ficou praticamente estável frente ao
USD (-0,01% no dia), mas depreciou frente ao EUR (5,9472 vs 5,9145 de 01/07, +0,55%) —
uma divergência entre pares que não é acompanhada de nenhum evento cambial relevante no
briefing e não deve ser sobre-interpretada. Com o CBOT corrigido (1.136,25) e essa taxa,
a paridade calculada de R$ 130,12/sc segue abaixo do físico de Paranaguá (R$ 135,08/sc)
— basis positivo de exportação de +4,96 BRL/sc, na verdade **ampliando** frente ao +4,53
recalculado de ontem (ver seção Soja para a correção completa do basis).

---

## Riscos e eventos próximos

**Feriado de 4 de julho (Independence Day observado nesta sexta) — sem sessão hoje para
o complexo agrícola.** O dia 4 cai num sábado neste calendário; a bolsa americana
observa o feriado em 03/07 (hoje). A retomada plena do pregão ocorre na semana de
06-10/07 — a primeira oportunidade real de testar se o rali de soja/farelo (agora
recalculado para uma magnitude menor) e a compressão do ratio Far/Soj têm continuidade.

**Divergência de dado intraday vs. settlement — segunda ocorrência em duas leituras
seguidas.** A leitura de 02/jul já havia notado uma revisão de dado para os preços de
01/jul; hoje a revisão, maior em magnitude, afeta os preços de 02/jul (soja -2,25,
farelo -2,80, óleo +0,12 cts/lb frente ao que fora publicado). Vale documentar esse
padrão como um risco operacional do próprio pipeline de leitura — decisões tomadas com
base em números intraday do dia da publicação podem precisar de revisão no dia seguinte
(ver Honestidade #1).

**COT CFTC — 10º dia sem publicação nova.** O dado mais recente continua sendo o de
23/06/2026 — mais uma semana sem atualização, atraso provavelmente ligado ao feriado de
4 de julho. Esse dado é crítico para calibrar se os 103k net longs em óleo, 12k em
farelo (com 98k shorts) e 37k em soja mudaram desde o USDA de 30/06 e o rali
subsequente (agora de magnitude menor do que se pensava).

**USDA Crop Progress — sem atualização nova.** O dado mais recente segue sendo
28/06/2026; o relatório de segunda-feira (06/07) também pode atrasar pelo feriado.

**WASDE de julho — ~10/07/2026 (7 dias).** Primeiro WASDE pós-Acreage/Stocks, e agora
também o primeiro grande catalisador fundamentalista depois da correção de dado desta
semana — vai revelar se o mercado realmente repreçou para cima (mesmo que em magnitude
menor que a inicialmente reportada) ou se o movimento perde força. Coincide quase
exatamente com o checkpoint D+45 da tese fiscal PIS/Cofins (10/07/2026).

**Isenção PIS/Cofins biodiesel — 31/07/2026 (28 dias).** Monitorar MAPA/MINFRA sobre
renovação.

**Florescimento da soja americana — segunda quinzena de julho.** Período de maior
sensibilidade climática. El Niño Advisory ativo e lavoura em 65% good/excellent (dado de
28/06, sem atualização) — baseline favorável, mas qualquer convergência de modelos para
calor extremo pode mover a soja em 40-80 cts/bu.

**Ratio Far/Soj em 80,66% (corrigido) — monitorar o cruzamento de 80% assim que o
pregão reabrir.** Terceiro recuo consecutivo, o mais perto do gatilho desde 26/jun —
item de maior sensibilidade operacional imediata do complexo.

**Rondonópolis/MT sustentando +10% por dois pregões — monitorar terceira confirmação.**
Se mantido na reabertura, passa a ser tratado como sinal físico regional, não mais como
ponto isolado.

---

## Honestidade

O que não foi possível validar neste briefing de 03/07/2026, onde a confiança é baixa
ou há lacunas materiais:

**1. A divergência mais material desta série de leituras: os preços de fechamento de
02/07/2026 usados na leitura de ontem (soja 1.138,50, farelo 308,30, óleo 66,65, todos
sobre volumes baixos de 3.661/1.524/4.204 contratos) não conferem com o dado assentado
que chega no dump de hoje (soja 1.136,25, farelo 305,50, óleo 66,77, sobre volumes
normais de 30.203/29.331/65.270 contratos).** As diferenças são: soja -2,25 cts/bu,
farelo -2,80 USD/sht, óleo +0,12 cts/lb — e os volumes revisados são de 8 a 19 vezes
maiores que os publicados ontem. A explicação mais provável, coerente com o padrão já
documentado na leitura de 02/jul (Honestidade #2 daquela leitura, sobre uma revisão
menor nos preços de 01/jul), é que a leitura de ontem foi gerada com um pull
intraday/pré-settlement do CBOT, e o dump de hoje reflete o fechamento oficial já
assentado. Esta leitura usou, de forma consistente, os valores do dump de hoje (03/jul)
para todos os recálculos — crush, ratio Far/Soj, oil share, oil-meal spread, margem de
biodiesel, curvas forward e paridade BRL — e refez a narrativa de cada seção com o dado
corrigido. O leitor deve saber que esta é a **segunda ocorrência consecutiva** desse
tipo de divergência (01/jul revisado na leitura de 02/jul; 02/jul revisado nesta
leitura), o que sugere um padrão sistemático no pipeline de coleta, não um evento
isolado — vale reportar ao responsável técnico do robô, já que esta leitura não pode (e
não deve) alterar código/indicadores.

**2. A atribuição da virada do ISF/ISO ao efeito calendário ABIOVE não pôde ser
confirmada por consulta direta ao banco de dados.** O ambiente de execução deste insight
não tem acesso ao banco SQLite do sistema (apenas ao dump `briefing/latest.md`), então a
conclusão de que a rolagem do mês de referência (junho→julho) é a causa da inversão dos
índices — reforçada hoje pela estabilidade do novo patamar por três pregões seguidos — é
uma inferência lógica bem fundamentada, mas não uma verificação direta linha a linha do
código.

**3. NOPA — dado inacessível pelo 32º+ dia consecutivo** (fila `release-nopa-2026-07-03`
tratada aqui). `monthly_status = 0.0 bool` (indicadores, 03/07/2026). O esmagamento
americano de junho/2026 segue sem fonte primária acessível.

**4. Palma malaia (MPOB) — 18+ dias consecutivos sem dados numéricos.** O parser
continua retornando apenas 3.428 chars de HTML sem valores extraídos (16/jun a
03/07/2026). Sem os preços de CPO na BMD, não é possível quantificar o efeito do El Niño
sobre a produção de palma nem o prêmio de substituição para o óleo de soja americano.

**5. RIN D4 como parâmetro fixo (2,11 USD/RIN) segue sendo a maior fonte de incerteza do
modelo de biodiesel.** Não há dado de mercado secundário no briefing para confirmar se o
valor real mudou após a expansão do mandato RFS (15/06/2026).

**6. COT com defasagem de 10 dias em relação ao evento USDA e ao rali subsequente
(agora de magnitude recalculada, menor que a inicialmente publicada).** O dado mais
recente segue sendo de 23/06/2026 — deixa às cegas a leitura de como os fundos reagiram
ao movimento de preço mais relevante do trimestre.

**7. BCBA Argentina — sem relatórios de esmagamento/exportação acessíveis via scraper**
(page_fetched=1,0 mas sem links de relatório, 03/07/2026). O ritmo de processamento
argentino pós-colheita (50,1 mi t) é estimado por notícia, não medido por fonte
primária.

**8. Percentis históricos de COT não calculados** — os 103k net longs em óleo, 12k em
farelo (com 98k shorts) e 37k em soja são grandes em termos absolutos, mas sem série
histórica completa para calibrar percentil.

**9. Dados do físico BR defasados um pregão** (CEPEA/ESALQ Paranaguá e NAG mais recentes
são de 02/07/2026, não de 03/07). Padrão recorrente já documentado em leituras
anteriores.

**10. O salto de +10% no farelo físico de Rondonópolis/MT permanece sem explicação
disponível no briefing**, mesmo após a segunda confirmação (01/07 e 02/07 no mesmo
patamar) — pode ser evento logístico real ou coincidência de coleta em duas leituras
seguidas. Registrado com peso maior, mas ainda não incorporado como sinal confirmado de
tendência regional.

**11. INMET (clima BR, 03/07/2026) foi consultado mas não tem relevância direta para a
tese de preço de soja neste momento do calendário** — o Brasil está fora da janela de
plantio/desenvolvimento da soja (que começa em setembro-outubro), então a variação de
temperatura entre praças (Passo Fundo/RS com mínima de 1°C, quase geada, vs. Sorriso/MT
a 34°C máxima) reflete o inverno normal, sem sinal de estresse relevante para a próxima
safra. Mencionado por completude, não incorporado à tese.

*Nenhum número foi inventado ou estimado além do que consta no briefing de 03/07/2026 e
nos insights anteriores referenciados. A maior contribuição desta leitura foi identificar
e corrigir uma divergência material entre o dado intraday usado ontem e o fechamento
oficial que chega hoje — o bear-farelo estrutural (exportação ABIOVE em queda, ratio
Far/Soj retomando a aproximação do gatilho de 80%) e o bear-óleo tático (confirmado
abaixo do suporte 72,00, margem de biodiesel corrigida em queda) têm a base de dados
mais sólida desta leitura; a magnitude do rali de soja/farelo tem confiança reduzida
frente à leitura anterior, por ter sido recalculada para baixo pela correção de dado —
a confirmação real só virá com a reabertura de volume pleno na semana de 06-10/jul,
coincidindo com o WASDE.*
