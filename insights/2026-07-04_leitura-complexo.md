---
data: 2026-07-04
titulo: "Sábado do 4 de julho trava o pregão pela segunda sessão seguida, mas o real aprecia (PTAX 5,1717) e o físico de soja em Paranaguá sobe pelo terceiro pregão consecutivo (R$ 135,45/sc); o salto de +10% no farelo físico de Rondonópolis, que vinha sendo monitorado como possível mudança estrutural, se desfaz integralmente — e a MP 1.358 (subvenção fóssil à gasolina) entra na semana decisiva antes do vencimento em 11/jul, mesma data do WASDE"
tags: [complexo, auto-claude]
fontes:
  - CBOT CME (ZSQ26/ZMQ26/ZLQ26 + curva forward completa) — sem sessão nova; último fechamento oficial (settlement) segue sendo 2026-07-02 (soja 1.136,25 cts/bu, farelo 305,50 USD/sht, óleo 66,77 cts/lb)
  - CBOT CME HO=F (heating oil) — sessão eletrônica de 2026-07-03, dado **revisado** frente ao usado na leitura de ontem (ver Honestidade #1)
  - BCB PTAX — 2026-07-03 (USD/BRL 5,1717; EUR/BRL 5,9154) — dado novo, real aprecia frente ao dólar
  - CEPEA/ESALQ Paranaguá via NAG — 2026-07-03 (R$ 135,45/sc, var +0,27%)
  - NAG Físico BR (farelo MT/IMEA, RS, Rondonópolis; prêmio PGUA farelo/óleo; soja Paraná interior) — 2026-07-03
  - CFTC COT Managed Money — 2026-06-23 (11º dia sem publicação nova, ver Riscos)
  - USDA Crop Progress — 2026-06-28 (sem atualização nova)
  - NOAA CPC ENSO — 2026-07-04 (El Niño Advisory, sem mudança)
  - ABIOVE projeções mensais — coleta recente (balanços ago-dez/2026, farelo/óleo/soja), sem alteração
  - Indicadores sintéticos (crush, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel) — base 2026-07-02 (sem sessão nova para recalcular); ISF/ISO — 2026-07-04
  - MPOB — 2026-07-04 (19º dia consecutivo sem números extraídos)
  - NOPA — 2026-07-04 (33º+ dia consecutivo inacessível; fila `release-nopa-2026-07-04`)
  - system/tributario_watch.toml — evento MP-1358-2026, vigência até 2026-07-11
  - Notícias Agrícolas / Farm Progress RSS — 2026-07-03/04 (sem manchete nova relevante hoje)
  - Forecasts estatísticos internos — 2026-07-04
  - Cruza com [[2026-07-03_leitura-complexo]], [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]], [[2026-05-26_subvencao-fossil-aperta-biodiesel]], [[2026-05-26_pis-cofins-biodiesel-explica-mercado-fisico-fraco]], [[2026-05-26_b16-bullish-farelo]], [[2026-05-26_curva-forward-cbot-oleo-desacopla]]
status: ativa
vies: [neutral-soja, bear-farelo, bear-oleo]
---

## Visão geral

O complexo soja é, na prática, uma fábrica com uma matéria-prima (a soja em grão) e dois
produtos de saída gerados em proporção fixa a cada bushel esmagado: o **farelo** (fração
proteica, vira ingrediente de ração animal) e o **óleo degomado** (fração de gordura, vira
óleo de cozinha e, cada vez mais, biodiesel). Quem decide o ritmo de esmagamento é a
esmagadora, olhando para a **crush margin** — o valor de mercado do farelo + óleo
produzidos por um bushel, menos o custo daquele bushel de soja. Hoje, **2026-07-04, é o
próprio feriado do 4 de julho** (cai num sábado neste calendário) — nos Estados Unidos os
mercados estão fechados por completo, sem nenhuma sessão eletrônica sequer. É a **segunda
sessão seguida sem fechamento novo** de soja, farelo ou óleo na CBOT: a de ontem (sexta,
03/jul) foi o feriado *observado*, com pregão do complexo agrícola fechado mas uma janela
eletrônica fina no heating oil (HO); hoje é o feriado *de fato*, fim de semana completo,
sem nenhuma cotação nova em lugar nenhum do book. O último fechamento oficial (settlement)
que temos para julgar o mercado de papel segue sendo o de **02/07/2026**: soja em 1.136,25
cts/bu, farelo em 305,50 USD/sht, óleo em 66,77 cts/lb — os mesmos números que sustentaram
a leitura de ontem, porque nada mudou no book desde então.

**O que sustenta a leitura de hoje, então, não é preço novo — é o físico brasileiro e o
calendário fiscal, que não param no feriado americano.** Três fatos novos, genuínos e não
derivados de correção de dado, chegaram no dump de hoje: primeiro, **o câmbio apreciou** —
a PTAX (BCB, 03/07/2026) caiu para **5,1717 BRL/USD**, de 5,1945 em 02/07 (-0,44%), o
movimento mais forte de real em uma única leitura desta série recente; segundo, **a soja
física em Paranaguá subiu pelo terceiro pregão consecutivo**, para **R$ 135,45/saca**
(CEPEA/ESALQ via NAG, 03/07/2026, var +0,27%), consolidando uma trajetória de alta que já
soma três dias (133,58 → 134,32 → 135,08 → 135,45); terceiro, e mais relevante para quem
vinha monitorando o físico do farelo, **o salto de +10% no preço de Rondonópolis/MT — que
duas leituras seguidas trataram como possível sinal de mudança regional — se desfez por
completo**: caiu de volta para R$ 1.500/ton (NAG, 03/07/2026), de R$ 1.650 nos dois
pregões anteriores. Essa reversão confirma a hipótese, já levantada com ceticismo nas
leituras de 01 e 02/jul, de que o patamar de R$ 1.650 era ruído de coleta pontual em
Rondonópolis, não um reposicionamento estrutural de basis regional — o preço voltou
exatamente ao nível de onde havia saltado.

O pivô do complexo continua sendo o mesmo de toda a semana passada: a tensão entre um
**óleo estruturalmente dominante no crush** — o Índice de Suporte do Óleo (ISO, mede em
escala 0-100 quantas das 5 condições estruturais favorecem o óleo dentro do crush) segue
em **100/100** hoje (indicadores, 04/07/2026), o quarto pregão seguido nesse patamar — e
um **farelo estruturalmente sobrando** — o Índice de Sobra de Farelo (ISF, mesma lógica,
mas para condições que empurram o farelo para baixo) segue em **80/100** (4/5 condições),
também estável há quatro sessões. Na prática: como o óleo "paga a conta" do crush (é a
fração mais valiosa hoje, muito puxada pela demanda de biodiesel nos EUA), a esmagadora
aceita vender o farelo pelo preço que o mercado oferecer — e o mercado está oferecendo
cada vez menos, com o **ratio Far/Soj** (o preço do farelo dividido pelo da soja, na mesma
base — mede se o farelo está "caro" ou "barato" frente ao grão que o origina; abaixo de
80% é farelo abundante, acima de 87% é farelo apertado) travado em **80,66%** desde o
fechamento de 02/jul, a apenas 0,66 ponto percentual do gatilho psicológico de 80% que a
fila de julgamento cobra há 23 dias (tratado em detalhe na seção Farelo, id
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`).

O segundo fato que merece atenção do trader hoje não é de mercado, é de **calendário
fiscal**: a fila de julgamento traz o item `trib-MP-1358-2026-2026-07-11`, apontando que a
**MP 1.358/2026** — que subvenciona gasolina em até R$ 0,89/L e diesel em R$ 0,35/L,
ressarcindo PIS/Cofins/Cide do combustível fóssil — tem **vigência até 11/07/2026**, e o
próximo marco é a **deliberação da comissão mista**, travada em regime de urgência desde
27/06 (`system/tributario_watch.toml`, evento MP-1358-2026). Essa data, **daqui a 7 dias**,
coincide quase exatamente com o **WASDE de julho** (~10/07) — dois catalisadores no mesmo
intervalo de uma semana, um de oferta/demanda física (WASDE) e outro de política de
preços relativos combustível fóssil vs. biocombustível (MP 1.358), tratado em detalhe na
Lente Fiscal.

**Leitura de uma linha:** sem sessão nova de mercado, a estrutura do complexo continua
intacta — bear-farelo estrutural com o ratio Far/Soj a um passo do gatilho de 80% (maior
convicção da casa), bear-óleo tático confirmado abaixo do suporte-virou-resistência de
72,00, e soja neutra aguardando o WASDE — mas dois fatos genuínos do dia (real apreciando
e reversão do físico de Rondonópolis) e uma reta final fiscal de sete dias (MP 1.358 +
WASDE) merecem monitoramento redobrado na semana que reabre o pregão (06-10/jul).
Confiança alta na tese estrutural do farelo e na leitura do óleo abaixo do suporte;
confiança moderada em soja, que só será testada com volume pleno na próxima semana; e uma
nova ocorrência do padrão de revisão de dado intraday-para-settlement, agora atingindo o
heating oil de ontem (ver Honestidade #1).

---

## Soja

**Viés: neutro — sem sessão nova (fim de semana do feriado de 4 de julho); o câmbio
apreciou (PTAX 5,1717, -0,44%) e o físico de Paranaguá subiu pelo terceiro pregão seguido
(R$ 135,45/sc); forecast de 30 dias segue altista, o de 7 dias segue lateral**

### O que sustenta a leitura

A soja de agosto (ZSQ26.CBT) segue **travada no fechamento oficial de 02/07/2026**:
**1.136,25 cts/bu**, abertura 1.132,50, máxima 1.142,75, mínima 1.131,50, sobre volume de
30.203 contratos (CBOT CME) — o mesmo dado assentado que a leitura de ontem já havia
tratado e corrigido. Não há pregão hoje (04/07, sábado, feriado de fato) nem houve pregão
para o complexo agrícola ontem (03/07, feriado observado) — a sequência de dois pregões
consecutivos sem nova cotação é a mais longa desta série de leituras diárias desde que o
monitoramento começou. A retomada plena só ocorre na semana de 06-10/07 (ver Riscos).

**O fato genuíno do dia para a soja é cambial, não de bolsa.** A PTAX (BCB, 03/07/2026)
recuou para **5,1717 BRL/USD**, de 5,1945 em 02/07 — uma apreciação do real de **0,44%**,
o movimento cambial mais forte de uma única leitura nesta série recente (para efeito de
comparação, as últimas variações diárias ficaram todas abaixo de 0,1%). Como a soja
brasileira é precificada em dólar mas negociada e fixada em reais, um real mais forte
**reduz** a paridade em BRL/saca calculada a partir do CBOT, mesmo sem nenhuma mudança no
preço em dólar — isso é bearish para quem vende soja física no Brasil e neutro-a-levemente-
bullish para quem já vendeu e vai importar insumos, mas o efeito líquido de curto prazo
para o produtor/trader de grão é de **paridade mais baixa em reais**. O sistema não gerou
um novo indicador `soja_paridade_br` para 03/07 no dump de hoje (o último registrado
continua sendo 130,12 BRL/sc, base 02/07) — por isso esta leitura **não inventa** um novo
número recalculado (ver Honestidade #2), mas o sinal direcional é claro: com o CBOT
travado em 1.136,25 e a PTAX caindo para 5,1717, a paridade em reais tende a ficar
**abaixo** dos 130,12 registrados oficialmente, não acima.

**Apesar disso, o físico de Paranaguá subiu, e subiu de forma consistente.** A soja física
em Paranaguá (CEPEA/ESALQ via NAG, **03/07/2026**) fechou em **R$ 135,45/saca** (var
+0,27%), o **terceiro pregão consecutivo de alta**: 133,58 (30/jun) → 134,32 (01/jul) →
135,08 (02/jul) → **135,45 (03/jul)** — um ganho acumulado de +1,87 BRL/sc (+1,40%) em
quatro pregões, mesmo com o câmbio trabalhando contra a paridade de papel nos últimos dois
dias. O mecanismo mais provável é que o físico de exportação reflete a demanda real de
embarque no porto, que não depende de o CBOT ter fechado ou não — compradores
internacionais seguem pagando mais por soja pronta para embarcar em Paranaguá,
independentemente do feriado americano. Esse descolamento (físico subindo enquanto o
papel está parado e o câmbio aprecia) é um sinal moderadamente positivo para a demanda de
exportação brasileira, mas precisa de confirmação: como o CBOT está congelado, não dá para
saber se o físico está de fato ganhando basis ou só repetindo inércia de poucos dias de
coleta em mercado fino.

**No interior do Paraná, o movimento também foi de alta:** a soja Paraná interior (NAG,
03/07/2026) subiu para **R$ 127,87 → 128,41/saca** (var +0,42%), a quarta alta seguida
(126,61 em 24/jun → 127,43 em 30/jun → 127,87 em 02/jul → 128,41 em 03/jul). Como a
paridade de papel (indicador oficial, base 02/jul) está em 130,12, o interior do Paraná
segue com desconto de -1,71 BRL/sc frente à paridade — mais estreito que o -2,25
recalculado ontem, uma modesta recuperação de basis interno, mesmo com a paridade oficial
ainda não capturando a apreciação cambial de 03/jul (que, se incorporada, estreitaria
ainda mais esse desconto, dado que reduziria o valor da própria paridade).

**As condições de lavoura americana seguem sem atualização nova.** O USDA Crop Progress
mais recente continua sendo o de 28/06/2026: 65% good/excellent (10% excellent + 55%
good), 6% poor, 96% emergido. O relatório de segunda-feira (06/07) tem risco real de
atraso por causa do feriado (ver Riscos) — o mercado pode reabrir na terça (07/07) sem o
Crop Progress semanal atualizado, deixando a leitura de condição de lavoura ainda mais
defasada exatamente na semana que antecede o WASDE. O El Niño Advisory segue confirmado
(NOAA CPC, **04/07/2026**), sem mudança de status pelo quarto dia — estatisticamente
associado a umidade acima do normal no Corn Belt durante o florescimento (segunda
quinzena de julho), o que tende a reduzir o prêmio de risco climático embutido no preço.

**O posicionamento dos fundos (COT de 23/06/2026, CFTC — 11º dia sem publicação nova, ver
Riscos)** segue mostrando managed money net long em soja de +36.986 contratos (3,7% do
open interest de 1.006.834) — inalterado, sem confirmação de como os fundos reagiram ao
rali pós-USDA de 30/jun-02/jul nem à apreciação cambial de hoje.

**Os forecasts estatísticos internos (04/07/2026, gerados com o mesmo spot de 1.136,25 por
não haver sessão nova)** mostram: central 7d = **1.137,54 cts/bu** (bandas 1.087,43-
1.187,65), viés **lateral**; central 30d = **1.144,21 cts/bu** (bandas 1.040,47-1.247,95),
viés **altista** — praticamente idênticos aos de ontem, como esperado sem preço novo para
recalibrar o modelo.

### O que invalida / risco para a soja

- **A ausência de duas sessões seguidas esconder um movimento que só aparecerá na
  reabertura de terça (07/07):** sem pregão desde 02/07, a primeira leitura confiável só
  vem com a normalização de liquidez, e o mercado pode abrir com gap depois de dois dias
  de notícia acumulada (cambial, física, fiscal).
- **WASDE de julho (~10/07/2026) reverter a leitura de "oferta grande":** catalisador
  mais importante da semana, coincide com o vencimento da MP 1.358.
- **Onda de calor no Corn Belt na segunda quinzena de julho** (florescimento): sem sinal
  nos dados disponíveis, mas segue o principal risco climático de curto prazo.
- **Apreciação cambial continuar:** se a PTAX seguir caindo, a paridade em reais cai junto
  mesmo com o CBOT parado — pressão bearish silenciosa sobre quem vende soja física no
  Brasil, independente do que acontecer em Chicago.
- **Basis de Paranaguá reverter a sequência de três altas:** ainda sem confirmação de que
  é ganho estrutural de basis ou inércia de mercado fino em feriado.

### Leitura operacional — soja

Com dois pregões seguidos sem preço novo, não há o que operar no papel hoje — a leitura
correta é de espera ativa, monitorando os dois sinais genuínos que chegaram (câmbio
apreciando, físico de Paranaguá subindo pelo terceiro dia). Para quem tem posição física,
a apreciação do real é o dado mais acionável: reduz a paridade em reais mesmo sem o CBOT
se mexer, o que pode justificar acelerar fixação se o objetivo for capturar o nível atual
antes de uma eventual continuação da valorização cambial. O catalisador que decide a tese
nas próximas duas semanas continua sendo o WASDE de julho (~10/jul), e a semana que vem
(06-10/jul) é a primeira com volume pleno para testar se o rali pós-USDA (agora
recalculado para +12,00 cts/bu em dois pregões, por Honestidade da leitura de ontem) tem
continuidade, reverte, ou é revisado por dado outra vez.

---

## Farelo

**Viés: bear estrutural — ratio Far/Soj travado em 80,66% desde 02/jul, seguindo a apenas
0,66 p.p. do gatilho de 80% (tratando novamente a fila
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, agora D+23 sem
confirmação); o salto físico de Rondonópolis se desfez por completo, removendo o único
contraponto que vinha sendo monitorado**

### O que sustenta a tese bear

O farelo de agosto (ZMQ26.CBT) segue travado no fechamento oficial de 02/07/2026: **305,50
USD/sht**, abertura 306,60, máxima 309,20, mínima 305,10, volume 29.331 contratos — sem
sessão nova hoje nem ontem para o complexo agrícola.

**Tratando novamente a fila `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-
farelo-D+7`,** que volta a aparecer na fila de julgamento pelo terceiro dia seguido: a
tese original (11/06/2026) projetou o ratio Far/Soj cruzando 80% "em 1-2 semanas"; o
checkpoint formal D+7 caiu em 18/06/2026 e nunca foi fechado oficialmente. Hoje,
**D+23 da origem** (11/jun → 04/jul), sem sessão nova de preço, o ratio **permanece
exatamente onde estava**: 80,66% (base 02/07/2026, o último fechamento oficial
disponível). A trajetória completa segue sendo:

| Data | Ratio Far/Soj | Evento |
|---|---|---|
| 11/jun | 81,4% | origem da tese (compressão rápida) |
| 26/jun | 80,30% | ponto mais próximo do cruzamento até então |
| 29/jun | 81,43% | reverte para cima (pré-USDA) |
| 30/jun | 81,09% | pós-USDA, recuando |
| 01/jul | 80,82% | segue recuando em direção a 80% |
| 02/jul | 80,66% | terceiro recuo consecutivo, 2º valor mais próximo de 80% da série |
| 03-04/jul | 80,66% (sem sessão) | mercado fechado — nível mantido, não testado |

**O veredito de honestidade sobre esta fila, hoje:** o gatilho operacional (ratio
sustentado abaixo de 80% por 2-3 pregões consecutivos) segue **não confirmado 23 dias
após a origem da tese** — mas o nível está tão perto (0,66 p.p.) que basta **um único
fechamento de continuidade** na reabertura de terça-feira (07/07) para, dependendo da
magnitude, potencialmente completar o gatilho já na primeira sessão pós-feriado. Dado que
o D+7 formal já venceu há mais de duas semanas sem fechamento definitivo, a recomendação
operacional desta leitura é: **tratar o D+7 como encerrado sem confirmação plena**, manter
o monitoramento diário até a reabertura, e preservar o checkpoint D+90 (09/09/2026) como
horizonte formal de avaliação da tese original — sem abrir um novo ciclo de revisão D+7
redundante enquanto o mercado seguir fechado.

**O contraponto físico que vinha sendo monitorado nas duas últimas leituras — o salto de
+10% em Rondonópolis/MT — se desfez integralmente.** O preço voltou para **R$ 1.500,00/ton**
(NAG, 03/07/2026), do patamar de R$ 1.650,00 sustentado em 01 e 02/07/2026. Isso é o
oposto do que a leitura de ontem apontava como risco ("dois pregões consecutivos aumentam
a confiança no movimento") — na verdade, o terceiro dado disponível **reverteu** o sinal,
confirmando a hipótese, já levantada com ceticismo nas leituras anteriores, de que o
patamar de R$ 1.650 era ruído de coleta pontual (possivelmente um preço cotado fora de
padrão, ou um erro de captura de página), não um reposicionamento genuíno de basis
regional. O mecanismo por trás dessa checagem é simples: um movimento estrutural de basis
regional (por exemplo, gargalo logístico ou pico de demanda pontual de ração em Rondonópolis)
tende a se sustentar ou se acentuar; um movimento que aparece e desaparece em três
pregões, sem nenhuma notícia ou evento explicativo no briefing, é mais consistente com
ruído de coleta. **Este item sai do radar de risco estrutural do farelo.**

**As demais praças físicas seguem estáveis:** MT/IMEA subiu para **R$ 1.554,53/ton**
(NAG, 03/07/2026, var +0,66%), de R$ 1.544,35 nos três pregões anteriores — a primeira
variação em quase duas semanas nessa praça, uma alta discreta mas genuína. RS segue
travado em R$ 1.640/ton (var 0,0%, inalterado desde pelo menos 22/06). O prêmio de
exportação do farelo em Paranaguá segue em **+0,05 USD/sht** (NAG, 03/07/2026, mês de
referência julho/26) — praticamente nulo, confirmando que o Brasil segue sem vantagem
competitiva de preço sobre a Argentina, que concluiu 98% da colheita com 50,1 milhões de
toneladas (Canal Rural, 27/06/2026, dado mais recente disponível).

**Os dados projetados da ABIOVE (coleta recente, sem alteração desde a última leitura)
seguem mostrando a exportação de farelo brasileiro recuando pela metade entre agosto e
dezembro/2026:** 1.400 mil t (agosto) → 1.100 (setembro) → 850 (outubro) → 800 (novembro)
→ **700 mil t (dezembro)**, uma queda de -50% no ritmo de escoamento externo em quatro
meses, com o estoque final projetado de farelo subindo de 1.016 mil t (setembro) para
1.224 (agosto, base) antes de recuar apenas gradualmente para 1.015 (dezembro) — o
estoque doméstico não desincha na velocidade que a queda de exportação sozinha sugeriria.
Este continua sendo o driver mais concreto e menos sujeito a ruído de dado intraday desta
tese, porque não depende do fechamento diário da CBOT nem do feriado americano.

**A curva forward do farelo (02/07/2026, sem alteração desde ontem, mercado fechado):**

| Vencimento | Código | Preço (USD/sht) | Var. vs Ago |
|---|---|---|---|
| Julho/26 | N26 | 307,70 | +2,20 |
| Agosto/26 | Q26 | 305,50 | — (spot) |
| Setembro/26 | U26 | 303,10 | −2,40 |
| Outubro/26 | V26 | 301,40 | −4,10 |
| Dezembro/26 | Z26 | 304,40 | −1,10 |
| Janeiro/27 | F27 | 306,00 | +0,50 |

O outubro (V26) segue testando a região de 300-305 USD/sht, coincidindo com o pico
sazonal de esmagamento simultâneo Brasil + Argentina (ABIOVE projeta 2.846 mil t de
esmagamento em outubro, o maior mês do ano) — o mercado de futuros continua precificando
o farelo mais fraco no 4º trimestre.

**O posicionamento dos fundos (COT de 23/06/2026, sem atualização nova — 11º dia)** segue
sendo o dado mais revelador disponível: managed money net long de apenas +12.359
contratos, com longs em 110.276 e **shorts em 97.917** (15,8% do open interest de 619.446
em posições vendidas de managed money) — os fundos mantêm posição vendida ativa. Sem COT
novo desde antes do rali pós-USDA, ainda não há como confirmar se essa posição mudou.

**Tratando a fila `release-nopa-2026-07-04`:** o sistema volta a registrar um pull da NOPA,
agora com data de 04/07/2026. O briefing confirma: `nopa | monthly_status: 0.0 bool`
(indicadores, 04/07/2026) — o relatório mensal de crush americano da NOPA (National
Oilseed Processors Association) segue inacessível por exigir membership pago, agora o
**33º+ dia consecutivo** nessa condição. O "release" que a fila sinaliza é apenas uma nova
tentativa de coleta, não um dado novo interpretável — a lacuna persiste (ver Honestidade).

### O que invalida / risco para o farelo

- **Ratio Far/Soj romper 80% de forma sustentada (2-3 pregões consecutivos abaixo):**
  hoje travado em 80,66%, sem sessão para testar — a reabertura de terça (07/07) é o
  primeiro teste real depois de dois dias parado tão perto do gatilho.
- **Rondonópolis reverter de novo para cima:** com o dado de hoje, a leitura mais honesta
  é que o salto foi ruído, não sinal — mas vale uma quarta observação antes de descartar
  de vez.
- **MT/IMEA continuar subindo:** a alta de +0,66% em 03/jul, a primeira em quase duas
  semanas nessa praça, merece uma segunda confirmação antes de virar tese.
- **Crush margin voltar a comprimir de forma sustentada abaixo de 2,50 USD/bu:** hoje (base
  02/07) em 2,7032, sem dado novo para testar continuidade.
- **WASDE de julho (~10/jul) reduzir a área de soja americana de forma expressiva:** menos
  esmagamento no 4T26 → menos farelo global, risco de short squeeze nos 97.917 contratos
  vendidos por fundos — catalisador cai na mesma semana do vencimento da MP 1.358.

### Leitura operacional — farelo

O bear-farelo estrutural segue com a maior convicção da leitura. Hoje, o fato mais
relevante para quem monitora o spread de convergência (long farelo/short soja) é que o
único contraponto físico que vinha sendo levantado como risco — o salto de Rondonópolis —
desapareceu, reforçando a leitura estrutural sem nenhum ruído físico a compensar. Para
quem já está posicionado no short estrutural de farelo, a régua de stop de referência
segue em 308-310 USD/sht (mantida da leitura anterior, sem novo dado para revisar). Para
quem quer montar o spread Far/Soj de convergência, a régua operacional continua a mesma —
aguardar ruptura confirmada abaixo de 80% por 2-3 pregões — mas com o ratio parado a 0,66
p.p. do gatilho há dois dias, a reabertura de terça-feira (07/07) é o primeiro teste real
dessa confirmação em quase uma semana.

---

## Óleo

**Viés: bear tático confirmado — fechamento oficial de 66,77 cts/lb segue abaixo do
suporte-virou-resistência 72,00 (fila `alerta-quebra_suporte-oleo_cbot-2026-07-02`, sem
sessão nova para testar); heating oil revisado em alta forte na sessão fina de 03/jul, mas
sem indicador oficial de margem recalculado para capturar o efeito (ver Honestidade)**

### Tratando a fila `alerta-quebra_suporte-oleo_cbot-2026-07-02`

O alerta segue ativo na fila de hoje, com o mesmo fato: óleo fechando em 66,77 cts/lb,
abaixo do nível de referência 72,00. A pergunta operacional: confirma ou muda a tese?

**Confirma — sem nenhum dado novo que a contradiga.** O óleo de agosto (ZLQ26.CBT) segue
travado no fechamento oficial de 02/07/2026: **66,77 cts/lb**, abertura 66,80, máxima
67,58, mínima 66,12, volume 65.270 contratos. Sem sessão nova nem hoje nem ontem para o
complexo agrícola, o suporte de 72,00 continua rompido há mais de duas semanas e segue
funcionando como resistência — a tese não tem novo dado de preço para ser testada, mas
também não tem novo dado para ser invalidada.

**O fato que exige atenção redobrada é o heating oil, revisado em alta forte na sessão
fina de ontem.** O dado assentado (settlement) de 03/07/2026 mostra o HO fechando em
**3,2566 USD/galão** (CME), com abertura 3,1793, máxima 3,2585, mínima 3,1663, sobre
volume de 7.117 contratos — valores **diferentes** dos usados na leitura de ontem
(abertura 3,1793 igual, mas fechamento 3,1802, volume 1.575). A revisão traz o fechamento
**0,0764 USD/galão mais alto** (+2,40%) e o volume **4,5 vezes maior** do que o número
intraday usado ontem (ver Honestidade #1 — é o terceiro dia seguido em que este padrão de
revisão intraday-para-settlement aparece no briefing, agora atingindo o heating oil em vez
do complexo agrícola). Como o heating oil é o principal componente de receita do
biodiesel americano (a margem = receita de HO + 1,5×RIN D4, menos o custo do óleo de
soja + custo industrial), uma alta de +2,4% no HO, **se sustentada**, tende a melhorar a
margem de biodiesel na próxima leitura com sessão de óleo — mas o sistema não gerou um
novo indicador `margem_usd_galao` para 03/07 (o mais recente segue sendo 0,5395, base
02/07), porque o cálculo depende também do preço do óleo de soja, que não teve sessão
nova. **Esta leitura não recalcula esse número por conta própria** — seria inventar um
dado fora do briefing — mas registra o sinal direcional: o input de receita do biodiesel
subiu, o que é um fator a favor de uma eventual recuperação de margem quando o mercado
reabrir, ainda que sem confirmação numérica hoje.

**A curva forward do óleo (02/07/2026, sem alteração desde ontem) mantém backwardation
clara:**

| Vencimento | Código | Preço (cts/lb) | Var. vs Ago |
|---|---|---|---|
| Julho/26 | N26 | 66,95 | +0,18 |
| Agosto/26 | Q26 | 66,77 | — (spot) |
| Setembro/26 | U26 | 66,34 | −0,43 |
| Outubro/26 | V26 | 65,81 | −0,96 |
| Dezembro/26 | Z26 | 65,43 | −1,34 |
| Janeiro/27 | F27 | 65,33 | −1,44 |

A curva caindo -1,44 cts/lb de agosto a janeiro/27 continua sendo o argumento técnico mais
forte para manter posição vendida de médio prazo: quem rola a posição mês a mês colhe esse
carry independentemente da direção do preço à vista.

**O posicionamento dos fundos (COT de 23/06/2026, sem atualização nova — 11º dia)** segue
sendo o maior risco de reversão mecânica do complexo: managed money net long de +103.206
contratos, representando 15,7% do open interest de 658.976 — a maior exposição relativa
das três pernas. Sem dado novo do COT, ainda não há como confirmar se o desmonte
observado nas semanas anteriores continuou.

**O Índice de Suporte do Óleo (ISO) permanece em 100/100 (5/5 condições)** hoje
(indicadores, 04/07/2026), o **quarto pregão seguido** nesse patamar desde a virada de
01/07. Quatro sessões consecutivas — agora cobrindo integralmente a primeira semana de
julho — seguem reforçando a hipótese de que a virada de 80 para 100 foi um efeito de
calendário (rolagem do mês-alvo de comparação ABIOVE de junho para julho), e não uma
mudança real de fundamento, mas continua sendo uma inferência lógica, não uma confirmação
direta (ver Honestidade).

### O que invalida / risco para o óleo

- **Heating oil sustentar a alta revisada de +2,4% quando o óleo de soja voltar a
  negociar:** se o HO continuar firme, a margem de biodiesel tem espaço para recuperar
  acima da faixa 0,50-0,80 USD/gal — o principal fator de possível alívio para a tese
  bear, ainda sem confirmação numérica.
- **Margem de biodiesel ultrapassar 0,80 USD/gal de forma sustentada:** último dado oficial
  (0,5395, base 02/07) está mais perto do piso da faixa 0,50-0,80 do que do teto.
- **RIN D4 real acima de 2,40 USD/RIN** (o modelo usa 2,11 fixo): incerteza estrutural
  bidirecional já sinalizada em leituras anteriores, sem novo dado hoje.
- **Dados de palma malaia (MPOB) inacessíveis há 19 dias consecutivos** (ver Honestidade)
  — se a produção de palma estiver caindo por El Niño, o óleo de soja ganharia prêmio de
  substituição global, o que seria altista.
- **WASDE de julho reduzir a área de soja americana:** menos esmagamento futuro nos EUA →
  menos óleo produzido → altista para os contratos de novembro em diante.
- **Exportação de óleo brasileiro projetada pela ABIOVE caindo de 110 mil t (setembro) para
  45 (outubro) e 21 (novembro)** — mais óleo represado internamente (bearish doméstico) ou
  mais disponibilidade para o mandato B15 (efeito ambíguo).

### Leitura operacional — óleo

O viés segue bear tático, com a quebra do suporte 72,00 sem nenhum dado novo para
contestá-la. O carry negativo da curva forward continua favorecendo posição vendida de
médio prazo (referência de stop em torno de 69,50-70,00 cts/lb, mantida da leitura
anterior). O ponto de atenção real para os próximos dias é o heating oil: a alta revisada
de +2,4% na sessão fina de 03/jul é o primeiro sinal, ainda não confirmado em margem, de
que o piso da faixa de conforto do biodiesel (0,50 USD/gal) pode não ser testado tão cedo
— vale acompanhar de perto o primeiro fechamento de óleo de soja da semana que vem para
ver se a margem recalculada confirma ou desmente esse sinal. Alvo primário do short
seguindo os forecasts (central 7d = 64,31 cts/lb, indicadores, 04/07/2026): zona de 64-66
cts/lb. Alvo secundário (central 30d = 55,22): 55-58 cts/lb, mas esse cenário exige que a
margem de biodiesel não recupere com o HO mais forte — monitorar diariamente antes de
assumir esse alvo como base.

---

## Spreads e crush — leitura de complexo

### Crush margin: 2,7032 USD/bu (base 02/jul, sem sessão nova) — segue em leve compressão

A crush segue travada em **2,7032 USD/bu** (Board Crush: farelo 305,50 + óleo 66,77 −
soja 1.136,25; indicadores, 02/07/2026) — a trajetória recente (3,0657 em 29/jun → 2,8056
em 30/jun → 2,7200 em 01/jul → 2,7032 em 02/jul) segue de leve compressão, ainda
comodamente acima do patamar narrativo de "alívio de esmagamento" (~2,50 USD/bu), mas sem
dado novo para confirmar continuidade.

### Ratio Far/Soj: 80,66% (base 02/jul) — travado a 0,66 p.p. do gatilho, D+23 da tese sem confirmação

Como detalhado na seção de Farelo (tratando a fila `revisao-2026-06-11...D+7`), o ratio
segue em 80,66%, sem sessão para testar o cruzamento de 80%. É o valor mais próximo do
gatilho de toda a série desde a origem da tese (11/jun), atrás apenas do mínimo de 80,30%
tocado em 26/jun. O gatilho operacional do spread de convergência (long farelo/short soja)
permanece **não confirmado**, mas parado à menor distância possível da confirmação há dois
pregões seguidos.

### Oil share: 52,22% (base 02/jul) — estável

O oil share segue em 52,22%, praticamente igual aos 52,20% de 01/jul — o óleo ainda domina
o crush (>50%), sem sinal de queda acelerada rumo a 50%.

### Oil-meal spread: 0,6237 USD/bu (base 02/jul) — estável

O oil-meal spread (contribuição do óleo menos a do farelo por bushel) segue em 0,6237
USD/bu, praticamente igual aos 0,6193 de 01/jul — óleo e farelo mantendo suas posições
relativas dentro do crush.

### ISF em 80/100, ISO em 100/100 — quarto pregão seguido no novo patamar

O Índice de Sobra de Farelo (ISF) segue em 80/100 (4/5 condições) e o Índice de Suporte
do Óleo (ISO) em 100/100 (5/5) — o mesmo patamar desde 01/jul, agora o **quarto** pregão
consecutivo, cobrindo integralmente a primeira semana de julho. A estabilidade por quatro
sessões seguidas reforça a hipótese de que a virada foi um efeito mecânico da rolagem do
mês-alvo de comparação ABIOVE (junho → julho), não uma mudança real de fundamento — mas
segue sendo uma inferência lógica, não uma confirmação direta (ver Honestidade).

### O que os índices dizem juntos em 04/07/2026

ISF 80/100 (efeito calendário, quarta confirmação) + ISO 100/100 (idem) + ratio 80,66%
(travado a 0,66 p.p. do gatilho, sem sessão para testar) + oil share 52,22% (estável) +
oil-meal spread 0,6237 USD/bu (estável) + crush 2,7032 USD/bu (leve compressão) + margem
biodiesel 0,5395 USD/gal (base 02/jul, sem captura ainda da alta do HO revisado) + COT
(103k net longs em óleo, 12k em farelo com 98k shorts ativos, 37k em soja, todos de 23/jun,
11º dia sem atualização) + exportação de farelo ABIOVE caindo pela metade até dezembro
(1.400 → 700 mil t) + reversão completa do salto de Rondonópolis + real apreciando
(PTAX 5,1717) + físico de Paranaguá subindo pelo terceiro pregão (R$ 135,45/sc) + heating
oil revisado em alta forte na sessão fina de 03/jul + fim de semana do 4 de julho parando
o pregão pela segunda sessão seguida:

A leitura de hoje é de **estrutura intacta, sem teste de preço, com dois sinais físicos
genuínos (câmbio e Paranaguá) e um sinal técnico ainda não confirmado (heating oil) a
observar na reabertura.** Nenhum desses fatos muda a direção das teses estruturais
(bear-farelo, bear-óleo tático, soja neutra) — mas o ratio Far/Soj parado a um passo do
gatilho, combinado com a reversão do único contraponto físico do farelo (Rondonópolis) e
com um heating oil mais forte que pode aliviar a margem de biodiesel, deixa a reabertura
de terça-feira (07/07) como o momento mais carregado de sinais desta semana inteira para
decidir a direção tática de curto prazo do complexo.

---

## Lente fiscal e regulatória BR

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L) entra na semana
decisiva antes do vencimento em 11/07/2026 (fila `trib-MP-1358-2026-2026-07-11`).** A MP
ressarce PIS/Cofins/Cide da gasolina e do diesel, mantendo o combustível fóssil
artificialmente mais barato — o mesmo mecanismo, em espírito, da MP 1.363/2026 (subsídio
de R$ 1,12/L ao diesel, vigente até 31/12/2026, já tratada em
[[2026-05-26_subvencao-fossil-aperta-biodiesel]]), mas com foco específico na gasolina e
com **vigência que expira em 7 dias**. O próximo marco é a **deliberação da comissão
mista**, travada em regime de urgência desde 27/06/2026
(`system/tributario_watch.toml`, evento MP-1358-2026) — ou o Congresso delibera e
converte (ou rejeita) a MP até 11/07, ou ela caduca por decurso de prazo. O mecanismo de
transmissão para o complexo soja é indireto mas real: enquanto o combustível fóssil segue
subsidiado, a competitividade relativa do biodiesel dentro do mix B15 mandatório
permanece pressionada (o mix é 85% diesel mineral + 15% biodiesel; se o diesel mineral
fica mais barato via subvenção, o biodiesel não ganha proporcionalmente, e a indústria de
biodiesel — maior consumidora industrial de óleo de soja no Brasil — segue com margem
mais apertada do que teria sem a subvenção ao concorrente fóssil). **Este marco cai
praticamente na mesma semana do WASDE de julho (~10/07)** — dois catalisadores
relevantes, um de oferta/demanda física e outro de política de preços relativos,
concentrados no mesmo intervalo de sete dias. Se a MP 1.358 caducar sem conversão em lei,
é um sinal (fraco, mas real) de que o pacote pró-fóssil pode perder fôlego político —
levemente positivo para a competitividade do biodiesel e, por extensão, para a demanda
industrial de óleo de soja; se for convertida, reforça o quadro de pressão que já vem
sendo documentado desde maio.

**Isenção PIS/Cofins biodiesel — vencimento em 31/07/2026, 27 dias.** Sem sinalização
pública do MAPA ou MINFRA sobre renovação até hoje (04/07/2026). O checkpoint D+45 desse
insight (10/07/2026,
[[2026-05-26_pis-cofins-biodiesel-explica-mercado-fisico-fraco]]) cai em 6 dias,
coincidindo com o WASDE e com o vencimento da MP 1.358 — a semana de 06-10/jul concentra
três marcos relevantes ao mesmo tempo (WASDE, MP 1.358, checkpoint D+45 PIS/Cofins).

**B16 — sem data, travado em B15.** Sem mudança de status desde a última leitura.

**MP 1.363/2026 (subsídio ao diesel fóssil) — em vigor até 31/12/2026, faltam ~180 dias.**
Sem alteração. Bearish estrutural persistente para a demanda incremental de óleo de soja
no mercado doméstico brasileiro, na medida em que mantém o diesel mineral artificialmente
mais competitivo frente ao biodiesel para consumo voluntário acima do mandato.

**STJ REsp 2.165.276/2026 — crédito PIS/Cofins para esmagadoras.** Sem alteração desde a
última leitura. Estruturalmente bearish para o farelo — incentiva mais esmagamento, mais
oferta de co-produtos, coerente com a exportação de farelo ABIOVE projetada em queda.

**PTAX 5,1717 BRL/USD (BCB, 03/07/2026).** O real apreciou 0,44% frente ao dólar (de
5,1945 em 02/07) e também apreciou frente ao euro (5,9154 vs 5,9472 de 02/07, -0,53%) —
desta vez um movimento consistente entre os dois pares, ao contrário da divergência
observada na leitura anterior, o que dá mais confiança de que é um movimento genuíno de
fortalecimento do real, não ruído isolado de um par cambial. Com o CBOT ainda travado em
1.136,25 e essa PTAX mais forte, a paridade em reais tende a recuar frente aos R$ 130,12/sc
oficialmente registrados (base 02/07) — o sistema não gerou o indicador recalculado para
03/07 (ver Honestidade #2), mas a direção é clara: câmbio mais forte pressiona a paridade
para baixo, mesmo com o físico de Paranaguá subindo.

---

## Riscos e eventos próximos

**Feriado de 4 de julho (hoje, sábado) — segunda sessão seguida sem pregão do complexo
agrícola.** A reabertura plena ocorre na semana de 06-10/07, com a primeira sessão real na
terça-feira 07/07 (a segunda-feira 06/07 também é dia útil normal nos EUA, então o mercado
deve reabrir já na segunda). É a primeira oportunidade de testar se o ratio Far/Soj
(travado a 0,66 p.p. do gatilho de 80%), a reversão de Rondonópolis, a apreciação cambial
e a alta revisada do heating oil têm continuidade ou se dissolvem como ruído de fim de
semana longo.

**Semana de 06-10/07 concentra três marcos fiscais/fundamentalistas no mesmo intervalo:**
WASDE de julho (~10/07), vencimento da MP 1.358 (11/07, deliberação de comissão mista) e
checkpoint D+45 da tese PIS/Cofins biodiesel (10/07). Rara concentração de catalisadores
— vale reservar atenção redobrada para essa semana específica.

**Divergência de dado intraday vs. settlement — terceira ocorrência consecutiva, agora no
heating oil.** As leituras de 02/jul e 03/jul já haviam notado revisões nos preços do
complexo agrícola (01/jul e 02/jul, respectivamente); hoje a revisão atinge o heating oil
de 03/jul (fechamento revisado de 3,1802 para 3,2566 USD/gal, volume de 1.575 para 7.117
contratos). O padrão agora atravessa três leituras seguidas e dois mercados diferentes
(agrícola e energia) — reforça a hipótese de que é uma característica sistemática do
pipeline de coleta (provavelmente a diferença entre um pull intraday no dia da sessão e o
settlement oficial que chega no dia seguinte), não um evento isolado. Vale reportar ao
responsável técnico do robô.

**COT CFTC — 11º dia sem publicação nova.** O dado mais recente continua sendo o de
23/06/2026. Esse dado é crítico para calibrar se os 103k net longs em óleo, 12k em farelo
(com 98k shorts) e 37k em soja mudaram desde o USDA de 30/06 e o rali subsequente.

**USDA Crop Progress — sem atualização nova, risco de atraso no relatório de segunda
(06/07) pelo feriado.**

**WASDE de julho — ~10/07/2026 (6 dias).** Primeiro WASDE pós-Acreage/Stocks, coincide com
o vencimento da MP 1.358 e o checkpoint D+45 da tese PIS/Cofins.

**Ratio Far/Soj em 80,66% — travado a 0,66 p.p. do gatilho de 80% há dois pregões seguidos
sem sessão para testar.** Item de maior sensibilidade operacional imediata do complexo;
monitorar o primeiro fechamento da reabertura com atenção redobrada.

**Reversão de Rondonópolis/MT — sai do radar de risco estrutural, mas vale uma quarta
observação antes de descartar de vez o episódio.**

---

## Honestidade

O que não foi possível validar neste briefing de 04/07/2026, onde a confiança é baixa ou
há lacunas materiais:

**1. Terceira ocorrência consecutiva de divergência intraday vs. settlement, agora no
heating oil.** O fechamento de 03/07/2026 usado na leitura de ontem (HO 3,1802 USD/gal,
volume 1.575 contratos) não confere com o dado assentado que chega no dump de hoje (HO
3,2566 USD/gal, volume 7.117 contratos) — uma diferença de +0,0764 USD/gal (+2,4%) e
volume 4,5x maior. Esta leitura usou o valor revisado (settlement) de hoje para toda
menção ao heating oil, mas **não recalculou** a margem de biodiesel de 03/jul com esse
valor corrigido combinado ao óleo de soja, porque o preço do óleo de soja não teve sessão
nova em 03/jul e o sistema não gerou esse indicador combinado — recalcular por conta
própria seria inventar um número fora do briefing. O padrão de revisão já atravessa três
leituras seguidas (01/jul revisado em 02/jul; 02/jul revisado em 03/jul; agora o HO de
03/jul revisado em 04/jul) e agora dois mercados diferentes — reforça que é sistemático,
não um evento isolado.

**2. Paridade em reais (`soja_paridade_br`) não foi recalculada pelo sistema para
03/07/2026 apesar de a PTAX ter mudado de forma material (-0,44%).** O último indicador
oficial continua sendo 130,12 BRL/sc (base 02/07/2026, calculado com PTAX 5,1945). Esta
leitura registra a direção do efeito (paridade deve cair com o real mais forte) mas
**não estima um novo número**, porque não há confirmação de que a fórmula exata (peso da
saca, arredondamentos) usada pelo sistema produziria o mesmo resultado se replicada
manualmente — o número oficial só aparecerá quando o sistema recalcular.

**3. A atribuição da virada do ISF/ISO ao efeito calendário ABIOVE não pôde ser
confirmada por consulta direta ao banco de dados.** O ambiente de execução deste insight
não tem acesso ao banco SQLite do sistema (apenas ao dump `briefing/latest.md`), então a
conclusão de que a rolagem do mês de referência (junho→julho) é a causa da inversão dos
índices — reforçada hoje pela estabilidade do novo patamar por quatro pregões seguidos —
é uma inferência lógica bem fundamentada, mas não uma verificação direta linha a linha do
código.

**4. NOPA — dado inacessível pelo 33º+ dia consecutivo** (fila `release-nopa-2026-07-04`
tratada aqui). `monthly_status = 0.0 bool` (indicadores, 04/07/2026). O esmagamento
americano de junho/2026 segue sem fonte primária acessível.

**5. Palma malaia (MPOB) — 19 dias consecutivos sem dados numéricos** (16/jun a
04/07/2026). O parser continua retornando apenas 3.428 chars de HTML sem valores
extraídos. Sem os preços de CPO na BMD, não é possível quantificar o efeito do El Niño
sobre a produção de palma nem o prêmio de substituição para o óleo de soja americano.

**6. RIN D4 como parâmetro fixo (2,11 USD/RIN) segue sendo a maior fonte de incerteza do
modelo de biodiesel.** Não há dado de mercado secundário no briefing para confirmar se o
valor real mudou.

**7. COT com defasagem de 11 dias em relação ao evento USDA e ao rali subsequente.** O
dado mais recente segue sendo de 23/06/2026 — deixa às cegas a leitura de como os fundos
reagiram ao movimento de preço mais relevante do trimestre e à apreciação cambial de hoje.

**8. BCBA Argentina — sem relatórios de esmagamento/exportação acessíveis via scraper**
(page_fetched=1,0 mas sem links de relatório, 04/07/2026). O ritmo de processamento
argentino pós-colheita (50,1 mi t) é estimado por notícia, não medido por fonte primária.

**9. Percentis históricos de COT não calculados** — os 103k net longs em óleo, 12k em
farelo (com 98k shorts) e 37k em soja são grandes em termos absolutos, mas sem série
histórica completa para calibrar percentil.

**10. O feed CEPEA RSS não atualiza a contagem de itens desde 30/06/2026** (101 itens),
quatro dias sem refresh — não afeta os preços físicos (que vêm de fonte separada, NAG),
mas é uma lacuna de cobertura de notícias que vale registrar.

**11. A reversão do salto de Rondonópolis/MT permanece sem explicação causal no
briefing** — sabemos que o preço saiu de R$ 1.500 para R$ 1.650 (01-02/jul) e voltou para
R$ 1.500 (03/jul), mas não há nenhuma notícia ou evento que explique nem o salto nem a
reversão. A leitura mais honesta é "ruído de coleta provável", não uma certeza.

*Nenhum número foi inventado ou estimado além do que consta no briefing de 04/07/2026 e
nos insights anteriores referenciados. A maior contribuição desta leitura foi separar com
cuidado os dois tipos de fato do dia — o que é genuinamente novo (câmbio, físico de
Paranaguá, reversão de Rondonópolis, heating oil revisado) do que é apenas ausência de
sessão (soja/farelo/óleo travados no fechamento de 02/07) — e resistir à tentação de
recalcular indicadores (paridade, margem de biodiesel) que o próprio sistema não gerou
para os dias sem sessão do complexo agrícola. O bear-farelo estrutural (ratio Far/Soj a
0,66 p.p. do gatilho, exportação ABIOVE em queda) e o bear-óleo tático (confirmado abaixo
do suporte 72,00) seguem com a base de dados mais sólida desta leitura; a soja neutra e o
efeito da apreciação cambial sobre a paridade têm confiança moderada, pendente de
confirmação numérica na reabertura da próxima semana.*
