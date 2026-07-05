---
data: 2026-07-05
titulo: "Domingo sem pregão revela que o próprio fechamento assentado de 02/jul foi revisado no dump de hoje (farelo 305,20 e ratio Far/Soj 80,74%, não mais 305,50/80,66%) — a estrutura segue intacta (bear-farelo D+24 sem confirmação do rompimento de 80%, bear-óleo tático sob o suporte 72,00, soja neutra) enquanto a MP 1.358 entra na semana final (6 dias) antes do vencimento em 11/jul, coincidindo com o WASDE"
tags: [complexo, auto-claude]
fontes:
  - CBOT CME (ZSQ26/ZMQ26/ZLQ26 + curva forward completa) — settlement de 2026-07-02, **valores revisados** frente ao que a leitura de 04/jul usou (ver Honestidade #1): soja 1.134,00 cts/bu (era 1.136,25), farelo 305,20 USD/sht (era 305,50), óleo 66,90 cts/lb (era 66,77)
  - CBOT CME HO=F (heating oil) — settlement de 2026-07-03 (3,2566 USD/galão), **estável** frente ao dado já usado ontem — primeira confirmação sem revisão em quatro leituras
  - BCB PTAX — 2026-07-03 (USD/BRL 5,1717; EUR/BRL 5,9154), sem publicação no fim de semana (sáb/dom não são dias úteis)
  - CEPEA/ESALQ Paranaguá via NAG — 2026-07-03 (R$ 135,45/sc, var +0,27%), sem coleta no fim de semana
  - NAG Físico BR (farelo MT/IMEA, RS, Rondonópolis; prêmio PGUA farelo/óleo; soja Paraná interior) — 2026-07-03
  - CFTC COT Managed Money — 2026-06-23 (12º dia sem publicação nova, ver Riscos)
  - USDA Crop Progress — 2026-06-28 (sem atualização nova)
  - NOAA CPC ENSO — 2026-07-05 (El Niño Advisory, sem mudança)
  - ABIOVE projeções mensais — coleta recente (balanços ago-dez/2026, farelo/óleo/soja), sem alteração
  - Indicadores sintéticos (crush, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel) — recalculados com base no settlement revisado de 02/07; ISF/ISO — 2026-07-05
  - MPOB — 2026-07-05 (20º dia consecutivo sem números extraídos, desde 16/jun)
  - NOPA — 2026-07-05 (fila `release-nopa-2026-07-05`; monthly_status inacessível)
  - system/tributario_watch.toml — eventos MP-1358-2026 (vigência até 2026-07-11), MP-1363-2026, PISCOFINS-BIODIESEL-ISENCAO, STJ-RESP-2165276, B16-CNPE-2026, EPA-RFS-2026-2027, 45Z-CLEAN-FUEL, DANANTARA-INDONESIA, INDONESIA-B50, INDONESIA-LEVY-PMK9
  - Notícias Agrícolas / Farm Progress RSS — 2026-07-05 (160 itens lidos, 6 mantidos, sem manchete nova específica de hoje)
  - Forecasts estatísticos internos — 2026-07-05 (mesmo spot-base de 02/07, sem sessão nova para recalibrar)
  - Cruza com [[2026-07-04_leitura-complexo]], [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]], [[2026-05-26_subvencao-fossil-aperta-biodiesel]], [[2026-05-26_pis-cofins-biodiesel-explica-mercado-fisico-fraco]], [[2026-05-26_b16-bullish-farelo]], [[2026-05-26_curva-forward-cbot-oleo-desacopla]]
status: ativa
vies: [neutral-soja, bear-farelo, bear-oleo]
---

## Visão geral

O complexo soja funciona, na prática, como uma fábrica com uma única matéria-prima (a
soja em grão) e dois produtos de saída fabricados em proporção fixa a cada bushel
esmagado: o **farelo** (a fração proteica, ~78% da massa, vira ingrediente de ração
animal) e o **óleo degomado** (a fração de gordura, ~18-20% da massa, vira óleo de
cozinha e, cada vez mais, biodiesel). Quem decide o ritmo de esmagamento é a esmagadora,
olhando para a **crush margin** — o valor de mercado do farelo + óleo produzidos por um
bushel de soja, menos o custo daquele bushel. Hoje, **domingo, 05/07/2026**, os mercados
americanos seguem fechados: é a **terceira sessão seguida sem fechamento novo** de soja,
farelo ou óleo na CBOT (sexta 03/jul foi feriado observado do 4 de julho; sábado 04/jul e
domingo 05/jul são fim de semana). A retomada plena só ocorre na segunda-feira, 06/07.

**O fato mais importante do dump de hoje não é de mercado — é sobre a própria qualidade do
dado.** O sistema trouxe, para a mesma data-base de 02/07/2026, valores diferentes dos que
a leitura de ontem (04/07) usou: o fechamento oficial da soja de agosto passou de 1.136,25
para **1.134,00 cts/bu**, o do farelo de 305,50 para **305,20 USD/sht**, e o do óleo de
66,77 para **66,90 cts/lb** — com volumes também revisados (soja: 30.203 → **43.860**
contratos; farelo: 29.331 → **21.083**; óleo: 65.270 → **46.162**). Como consequência
direta, o **ratio Far/Soj** recalculado sobe ligeiramente de 80,66% para **80,74%** e a
**crush margin** de 2,7032 para **2,7334 USD/bu** — pequenos ajustes que não mudam nenhuma
conclusão direcional, mas confirmam, pela quarta vez em cinco leituras consecutivas, que o
pipeline de coleta revisa retroativamente o próprio settlement "oficial" alguns dias depois
do fechamento (tratado em detalhe na Honestidade #1). Esta leitura usa, em todo o corpo do
texto, os **valores revisados de hoje** — por serem os mais recentes disponíveis — e não os
que a leitura de ontem publicou.

O pivô do complexo continua sendo o mesmo de toda a semana passada: a tensão entre um
**óleo estruturalmente dominante no crush** — o Índice de Suporte do Óleo (ISO, escala
0-100, mede quantas das 5 condições estruturais favorecem o óleo dentro do crush) segue em
**100/100** hoje (indicadores, 05/07/2026), o quinto pregão seguido nesse patamar — e um
**farelo estruturalmente sobrando** — o Índice de Sobra de Farelo (ISF, mesma lógica, mas
para condições que empurram o farelo para baixo) segue em **80/100** (4/5 condições),
também estável há cinco sessões. Na prática: como o óleo é a fração mais valiosa do crush
hoje (puxado pela demanda de biodiesel americano), a esmagadora aceita vender o farelo pelo
preço que o mercado oferecer — e o mercado está oferecendo cada vez menos, com o **ratio
Far/Soj** (o preço do farelo dividido pelo da soja, na mesma base; abaixo de 80% é farelo
abundante, acima de 87% é farelo apertado) em **80,74%**, ainda **0,74 ponto percentual**
acima do gatilho psicológico de 80% que a fila de julgamento cobra há **24 dias** (tratado
em detalhe na seção Farelo, id `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`).

O segundo fato relevante do dia não é de mercado, é de **calendário fiscal**: a fila de
julgamento traz o item `trib-MP-1358-2026-2026-07-11`, apontando que restam **6 dias**
para o vencimento da **MP 1.358/2026** (subvenção de PIS/Cofins/Cide sobre a gasolina, R$
0,89/L, e diesel, R$ 0,35/L). O próximo marco é a deliberação da comissão mista, travada
em regime de urgência desde 27/06 (`system/tributario_watch.toml`). Essa data coincide
quase exatamente com o **WASDE de julho** (~10/07) e com o checkpoint D+45 da tese
PIS/Cofins-biodiesel (10/07) — três catalisadores concentrados na mesma semana de reabertura
do pregão (tratado na Lente Fiscal).

**Leitura de uma linha:** sem sessão nova de mercado pelo terceiro pregão seguido, a
estrutura do complexo continua intacta — bear-farelo estrutural com o ratio Far/Soj a
menos de um ponto percentual do gatilho de 80% (maior convicção da casa, agora D+24 sem
confirmação plena), bear-óleo tático confirmado abaixo do suporte-virou-resistência de
72,00, e soja neutra aguardando o WASDE — mas a revisão retroativa do próprio settlement de
02/jul (agora afetando pela primeira vez os três contratos agrícolas simultaneamente, não
só um mercado isolado) exige cautela redobrada sobre qualquer número "fechado" antes de a
liquidez plena voltar na segunda-feira. Confiança alta na tese estrutural do farelo e na
leitura do óleo abaixo do suporte; confiança moderada em soja, que só será testada com
volume pleno a partir de 06/07; confiança baixa em qualquer leitura de magnitude exata
(ratio, crush, paridade) enquanto o padrão de revisão de dado persistir.

---

## Soja

**Viés: neutro — terceira sessão seguida sem pregão (feriado observado + fim de semana);
câmbio seguindo apreciado desde sexta (PTAX 5,1717) e físico de Paranaguá no maior nível da
série recente (R$ 135,45/sc); forecast de 30 dias segue altista, o de 7 dias segue lateral**

### O que sustenta a leitura

A soja de agosto (ZSQ26.CBT) está travada no fechamento revisado de 02/07/2026: **1.134,00
cts/bu** (abertura 1.132,50, máxima 1.142,75, mínima 1.131,50, volume 43.860 contratos —
CBOT CME, ver Honestidade #1 sobre a revisão desses números). Não há pregão nem hoje
(05/07, domingo) nem ontem (04/07, sábado) nem anteontem (03/07, feriado observado do 4 de
julho para o complexo agrícola) — a retomada plena ocorre apenas na segunda-feira, 06/07.

**O fato genuíno mais recente para a soja segue sendo cambial, de sexta-feira.** A PTAX
(BCB, 03/07/2026) está em **5,1717 BRL/USD**, ante 5,1945 em 02/07 — uma apreciação do real
de 0,44%, sem atualização no fim de semana (o BCB não publica PTAX em dias não-úteis). Como
a soja brasileira é precificada em dólar mas negociada e fixada em reais, um real mais
forte **reduz** a paridade em BRL/saca calculada a partir do CBOT, mesmo sem nenhuma
mudança no preço em dólar. O indicador oficial `soja_paridade_br` mais recente no briefing
segue sendo **129,86 BRL/saca60kg**, mas calculado com o CBOT de 1.134,00 cts **e a PTAX
antiga de 5,1945** (indicadores, 02/07/2026) — ou seja, o sistema ainda não combinou o
câmbio mais forte de 03/07 com o preço do grão. A direção do efeito é clara (paridade tende
a ficar abaixo dos 129,86 registrados oficialmente quando as duas pontas forem recalculadas
juntas), mas esta leitura **não estima um novo número** por conta própria (ver Honestidade
#2) — seria inventar um dado fora do briefing.

**O físico de Paranaguá segue no patamar mais alto da série recente.** A soja física em
Paranaguá (CEPEA/ESALQ via NAG, **03/07/2026**) fechou em **R$ 135,45/saca** (var +0,27%),
consolidando uma trajetória de três altas seguidas: 133,58 (30/jun) → 134,32 (01/jul) →
135,08 (02/jul) → 135,45 (03/jul) — um ganho acumulado de +1,87 BRL/sc (+1,40%) em quatro
pregões. Sem coleta no fim de semana, este continua sendo o valor de referência até
terça-feira. O mecanismo mais provável é que o físico de exportação reflete a demanda real
de embarque no porto, que não depende do fechamento do CBOT: compradores internacionais
seguem pagando mais por soja pronta para carregar em Paranaguá, independentemente do
feriado americano. Esse descolamento (físico subindo enquanto o papel está parado e o
câmbio aprecia) é moderadamente positivo para a leitura de demanda de exportação
brasileira, mas ainda carece de confirmação de que é ganho estrutural de basis — e não
apenas inércia de poucos pregões em mercado fino de feriado.

**No interior do Paraná, o movimento também foi de alta:** a soja Paraná interior (NAG,
03/07/2026) fechou em **R$ 128,41/saca** (var +0,42%), a quarta alta seguida (126,61 em
24/jun → 127,43 em 30/jun → 127,87 em 02/jul → 128,41 em 03/jul). Frente à paridade oficial
de 129,86 (ainda não recalculada com a PTAX de sexta), o interior do Paraná está com
desconto de **-1,45 BRL/sc** — mais estreito que os -2,25 de duas leituras atrás, uma
recuperação gradual de basis interno que tende a ficar ainda mais estreita quando (e se) a
paridade oficial incorporar o câmbio mais forte, já que isso reduziria o próprio valor de
referência.

**As condições de lavoura americana seguem sem atualização.** O USDA Crop Progress mais
recente continua sendo o de 28/06/2026: 65% good/excellent (10% excellent + 55% good), 6%
poor, 96% emergido — sem piora nem melhora relevante frente ao 21/06 (66% good/excellent,
93% emergido). O relatório de segunda-feira (06/07) corre risco real de atraso por causa do
feriado (ver Riscos). O El Niño Advisory segue confirmado (NOAA CPC, **05/07/2026**), sem
mudança de status — estatisticamente associado a umidade acima do normal no Corn Belt
durante o florescimento (segunda quinzena de julho), o que tende a reduzir o prêmio de
risco climático embutido no preço da nova safra americana. Vale notar que o calendário
brasileiro de plantio (safra 2026/27, setembro a março) está em entressafra agora — os
dados do INMET de hoje (Cascavel/PR, Passo Fundo/RS, Maringá/PR, entre outros, 06/07/2026)
mostram temperaturas de inverno (6-19°C no Sul, 16-36°C no Centro-Oeste), sem relevância
direta para a formação da safra atual, que já foi colhida; o clima brasileiro só volta a
pesar na tese quando a janela de plantio da 26/27 se aproximar (ago-set).

**A colheita argentina está praticamente concluída.** Notícia mais recente (Canal Rural,
27/06/2026) confirma 98% de colheita com produção mantida em 50,1 milhões de toneladas — a
Argentina não deve gerar mais surpresa de oferta relevante nesta safra, o que retira um
vetor de incerteza de curto prazo (mas mantém o país como concorrente pleno de exportação
pelos próximos meses, pressão relevante para a seção de Farelo, dado o baixo prêmio de
exportação brasileiro).

**O posicionamento dos fundos (COT de 23/06/2026, CFTC — 12º dia sem publicação nova, ver
Riscos)** segue mostrando managed money net long em soja de **+36.986 contratos** (long
142.168, short 105.182; 3,7% do open interest de 1.006.834) — inalterado, sem confirmação
de como os fundos reagiram ao rali pós-USDA de fim de junho nem à apreciação cambial desta
semana.

**Os forecasts estatísticos internos (05/07/2026, gerados com o mesmo spot revisado de
1.134,00, sem sessão nova para recalibrar)** mostram: central 7d = **1.135,44 cts/bu**
(bandas 1.085,73-1.185,16), viés **lateral**; central 30d = **1.142,07 cts/bu** (bandas
1.039,15-1.244,99), viés **altista** — próximos dos de ontem, com pequenas variações
mecânicas decorrentes apenas da revisão do spot-base.

### O que invalida / risco para a soja

- **Três sessões seguidas sem preço novo esconderem um movimento que só aparece na
  reabertura de segunda (06/07):** o mercado pode abrir com gap depois de dias de notícia
  acumulada (cambial, física, fiscal, e a própria revisão de dado).
- **WASDE de julho (~10/07/2026) reverter a leitura de "oferta grande":** catalisador mais
  importante da semana, coincide com o vencimento da MP 1.358.
- **Onda de calor no Corn Belt na segunda quinzena de julho** (florescimento): sem sinal
  nos dados disponíveis, mas segue o principal risco climático de curto prazo para a nova
  safra americana.
- **Apreciação cambial continuar:** se a PTAX seguir caindo na reabertura, a paridade em
  reais cai junto mesmo com o CBOT parado — pressão bearish silenciosa sobre quem vende
  soja física no Brasil.
- **Basis de Paranaguá reverter a sequência de altas:** ainda sem confirmação de que é
  ganho estrutural ou inércia de mercado fino em feriado.

### Leitura operacional — soja

Com três pregões seguidos sem preço novo, não há o que operar no papel hoje — a leitura
correta é de espera ativa. Para quem tem posição física, a apreciação do real desde
sexta-feira é o dado mais acionável: reduz a paridade em reais mesmo sem o CBOT se mexer, o
que pode justificar acelerar fixação para quem quer capturar o nível atual antes de uma
eventual continuação da valorização cambial. O catalisador que decide a tese nas próximas
duas semanas continua sendo o WASDE de julho (~10/jul), e a segunda-feira (06/07) é a
primeira sessão com chance real de testar se o rali pós-USDA (que passou por duas rodadas
de revisão de dado nesta série) tem continuidade, reverte, ou é revisado outra vez.

---

## Farelo

**Viés: bear estrutural — ratio Far/Soj recalculado em 80,74% (base 02/jul revisada), a
0,74 p.p. do gatilho de 80%, tratando novamente a fila
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, agora **D+24** sem
confirmação plena; a reversão do salto físico de Rondonópolis segue confirmada há dois
pregões**

### O que sustenta a tese bear

O farelo de agosto (ZMQ26.CBT) está travado no fechamento revisado de 02/07/2026: **305,20
USD/sht** (abertura 306,60, máxima 309,20, mínima 305,10, volume 21.083 contratos — CBOT
CME, ver Honestidade #1). Sem sessão nova há três pregões para o complexo agrícola.

**Tratando novamente a fila `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-
farelo-D+7`,** que volta a aparecer na fila de julgamento pelo quarto dia seguido: a tese
original (11/06/2026) projetou o ratio Far/Soj cruzando 80% "em 1-2 semanas"; o checkpoint
formal D+7 caiu em 18/06/2026 e nunca foi fechado oficialmente. Hoje, **D+24 da origem**
(11/jun → 05/jul), sem sessão nova de preço, o ratio recalculado com o settlement revisado
de 02/07 está em **80,74%** — ligeiramente mais alto (mais longe do gatilho) do que os
80,66% que a leitura de ontem havia registrado com o dado então disponível. A trajetória
completa, agora com os valores mais recentes de cada data-base:

| Data-base | Ratio Far/Soj | Evento |
|---|---|---|
| 11/jun | 81,4% | origem da tese (compressão rápida) |
| 26/jun | 80,30% | ponto mais próximo do cruzamento até então |
| 29/jun | 81,43% | reverte para cima (pré-USDA) |
| 30/jun | 81,09% | pós-USDA, recuando |
| 01/jul | 80,82% | segue recuando em direção a 80% |
| 02/jul | 80,74% | valor revisado hoje (era 80,66% na leitura de 04/jul) |
| 03-05/jul | sem sessão | mercado fechado — nível não testado |

**O veredito de honestidade sobre esta fila, hoje:** o gatilho operacional (ratio sustentado
abaixo de 80% por 2-3 pregões consecutivos) segue **não confirmado 24 dias após a origem da
tese**, e o pequeno ajuste do recálculo de hoje (80,66% → 80,74%) mostra que a distância até
o gatilho é sensível ao próprio processo de revisão de dado — reforçando que só um
fechamento de continuidade robusto, e não uma leitura isolada de duas casas decimais,
deveria confirmar o rompimento. Mantendo a recomendação já registrada na leitura de ontem:
**tratar o D+7 como encerrado sem confirmação plena**, preservar o checkpoint D+90
(09/09/2026) como horizonte formal de avaliação da tese original, e monitorar diariamente
até a reabertura de segunda-feira (06/07) — o primeiro teste real de continuidade em quase
uma semana.

**A reversão do salto físico de Rondonópolis/MT segue confirmada, sem sinal de retorno.** O
preço mais recente (NAG, 03/07/2026) permanece em **R$ 1.500,00/ton**, do patamar de R$
1.650,00 sustentado em 01 e 02/07/2026 — a segunda leitura seguida em que o nível fica
estável no valor mais baixo. Isso reforça a hipótese, já levantada nas duas leituras
anteriores, de que o salto de R$ 1.650 foi ruído de coleta pontual (possivelmente um preço
cotado fora de padrão), não um reposicionamento genuíno de basis regional. Sem sessão nova
no fim de semana, não há um quarto ponto de dado para reforçar ainda mais essa conclusão,
mas o padrão de dois pregões consecutivos no nível revertido é suficiente para manter este
item **fora do radar de risco estrutural do farelo**.

**As demais praças físicas seguem estáveis.** MT/IMEA está em **R$ 1.554,53/ton** (NAG,
03/07/2026, var +0,66% frente aos R$ 1.544,35 sustentados nos três pregões anteriores) — a
primeira variação em quase duas semanas nessa praça, uma alta discreta mas genuína, sem
nova observação no fim de semana para confirmar continuidade. RS segue travado em R$
1.640/ton (var 0,0%, inalterado desde pelo menos 22/06). O prêmio de exportação do farelo
em Paranaguá permanece em **+0,05 USD/sht** (NAG, 03/07/2026, mês de referência julho/26) —
praticamente nulo, confirmando que o Brasil segue sem vantagem competitiva de preço sobre a
Argentina, que concluiu 98% da colheita com 50,1 milhões de toneladas (Canal Rural,
27/06/2026).

**Os dados projetados da ABIOVE (coleta recente, sem alteração) seguem mostrando a
exportação de farelo brasileiro recuando pela metade entre agosto e dezembro/2026:** 1.400
mil t (agosto) → 1.100 (setembro) → 850 (outubro) → 800 (novembro) → **700 mil t
(dezembro)**, uma queda de -50% no ritmo de escoamento externo em quatro meses. O estoque
final projetado de farelo, no entanto, **não desincha proporcionalmente**: recua de 1.224
mil t (agosto) para 1.016 (setembro), mas depois **sobe** para 1.100 (outubro) e 1.101
(novembro), só voltando a cair para 1.015 mil t em dezembro — ou seja, mesmo com a
exportação caindo pela metade, o estoque doméstico projetado termina o ano praticamente no
mesmo nível de setembro. Esse é o driver mais concreto e menos sujeito a ruído de dado
intraday desta tese, porque não depende do fechamento diário da CBOT nem do feriado
americano: o mecanismo é que, com menos saída pelo porto, o farelo produzido em excesso
(puxado pelo crush favorável ao óleo) precisa ser absorvido pelo mercado interno de ração,
que historicamente não tem elasticidade para compensar toda a queda de exportação — o
resultado é pressão de preço doméstico, coerente com a leitura estrutural bearish.

**A curva forward do farelo (02/07/2026, valores revisados, ver Honestidade #1):**

| Vencimento | Código | Preço (USD/sht) | Var. vs Ago |
|---|---|---|---|
| Julho/26 | N26 | 307,70 | +2,50 |
| Agosto/26 | Q26 | 305,20 | — (spot) |
| Setembro/26 | U26 | 303,00 | −2,20 |
| Outubro/26 | V26 | 301,30 | −3,90 |
| Dezembro/26 | Z26 | 304,40 | −0,80 |
| Janeiro/27 | F27 | 305,90 | +0,70 |

O outubro (V26) segue testando a região de 300-305 USD/sht, coincidindo com o pico sazonal
de esmagamento simultâneo Brasil + Argentina (ABIOVE projeta 2.846 mil t de esmagamento em
outubro, o maior mês do ano) — o mercado de futuros continua precificando o farelo mais
fraco no 4º trimestre.

**O posicionamento dos fundos (COT de 23/06/2026, sem atualização — 12º dia)** segue sendo
o dado mais revelador disponível: managed money net long de apenas **+12.359 contratos**,
com longs em 110.276 e **shorts em 97.917** (15,8% do open interest de 619.446 em posições
vendidas de managed money) — os fundos mantêm posição vendida ativa. Sem COT novo desde
antes do rali pós-USDA, ainda não há como confirmar se essa posição mudou com o movimento
de preço do fim de junho.

**Tratando a fila `release-nopa-2026-07-05`:** o sistema volta a registrar uma tentativa de
coleta da NOPA, agora datada de 05/07/2026. O briefing confirma: `nopa | monthly_status:
0.0 bool` (indicadores, 05/07/2026) — o relatório mensal de crush americano da NOPA
(National Oilseed Processors Association) segue inacessível por exigir membership pago, já
há mais de um mês. O "release" que a fila sinaliza é apenas uma nova tentativa de coleta,
não um dado novo interpretável — a lacuna persiste (ver Honestidade #4).

### O que invalida / risco para o farelo

- **Ratio Far/Soj romper 80% de forma sustentada (2-3 pregões consecutivos abaixo):** hoje
  em 80,74% (revisado), sem sessão para testar — a reabertura de segunda (06/07) é o
  primeiro teste real depois de três dias parado perto do gatilho.
- **Rondonópolis reverter de novo para cima:** com dois pregões seguidos no nível revertido
  (R$ 1.500), o risco de retomada do salto está mais baixo, mas ainda vale confirmação
  contínua.
- **MT/IMEA continuar subindo:** a alta de +0,66% em 03/jul, a primeira em quase duas
  semanas nessa praça, merece uma segunda confirmação antes de virar tese.
- **Crush margin voltar a comprimir de forma sustentada abaixo de 2,50 USD/bu:** hoje (base
  02/07 revisada) em 2,7334, sem dado novo para testar continuidade.
- **WASDE de julho (~10/jul) reduzir a área de soja americana de forma expressiva:** menos
  esmagamento no 4T26 → menos farelo global, risco de short squeeze nos 97.917 contratos
  vendidos por fundos — catalisador cai na mesma semana do vencimento da MP 1.358.
- **Estoque doméstico de farelo projetado pela ABIOVE não desinchar como a queda de
  exportação sugere:** se a demanda interna de ração não absorver o excedente, a pressão
  de preço físico tende a se intensificar, não a aliviar.

### Leitura operacional — farelo

O bear-farelo estrutural segue com a maior convicção da leitura. O fato mais relevante para
quem monitora o spread de convergência (long farelo/short soja) é que o único contraponto
físico que vinha sendo levantado como risco — o salto de Rondonópolis — permanece revertido
por dois pregões seguidos, reforçando a leitura estrutural sem ruído físico a compensar.
Para quem já está posicionado no short estrutural de farelo, a régua de stop de referência
segue em 308-310 USD/sht (mantida da leitura anterior, sem novo dado para revisar). Para
quem quer montar o spread Far/Soj de convergência, a régua operacional continua a mesma —
aguardar ruptura confirmada abaixo de 80% por 2-3 pregões — mas com o ratio parado a menos
de um ponto percentual do gatilho há três dias sem sessão, a reabertura de segunda-feira
(06/07) é o primeiro teste real dessa confirmação em quase uma semana. Vale nota de cautela
adicional: como o próprio nível do ratio já foi revisado uma vez (80,66% → 80,74%) sem
nenhuma sessão nova de mercado, um eventual "rompimento" na reabertura merece confirmação
por pelo menos dois fechamentos antes de ser tratado como sinal operacional, não um.

---

## Óleo

**Viés: bear tático confirmado — fechamento revisado de 66,90 cts/lb segue abaixo do
suporte-virou-resistência 72,00 (fila `alerta-quebra_suporte-oleo_cbot-2026-07-02`, sem
sessão nova para testar); heating oil de 03/jul confirmado estável em 3,2566 USD/galão pela
primeira vez em quatro leituras, sem indicador oficial de margem recalculado para capturar
o efeito (ver Honestidade #1)**

### Tratando a fila `alerta-quebra_suporte-oleo_cbot-2026-07-02`

O alerta segue ativo na fila de hoje, agora com o valor revisado: óleo fechando em **66,90
cts/lb**, abaixo do nível de referência 72,00. A pergunta operacional: confirma ou muda a
tese?

**Confirma — sem nenhum dado novo que a contradiga, e com uma margem ligeiramente maior de
distância do suporte rompido do que na leitura de ontem.** O óleo de agosto (ZLQ26.CBT)
está travado no fechamento revisado de 02/07/2026: **66,90 cts/lb** (abertura 66,80,
máxima 67,58, mínima 66,12, volume 46.162 contratos — CBOT CME, ver Honestidade #1). Sem
sessão nova há três pregões, o suporte de 72,00 continua rompido há mais de duas semanas e
segue funcionando como resistência — a tese não tem novo dado de preço para ser testada,
mas também não tem novo dado para ser invalidada.

**O heating oil, pela primeira vez em quatro leituras, não foi revisado.** O dado assentado
(settlement) de 03/07/2026 mostra o HO fechando em **3,2566 USD/galão** (CME), com abertura
3,1793, máxima 3,2585, mínima 3,1663, volume 7.117 contratos — **exatamente os mesmos
valores** que a leitura de ontem já havia usado. Isso é uma notícia metodológica positiva:
depois de três ocorrências consecutivas de revisão intraday-para-settlement (duas no
complexo agrícola, uma no próprio heating oil), este é o primeiro dado que se mantém
estável entre duas leituras — mesmo que, ironicamente, tenha sido a própria base agrícola
(soja/farelo/óleo de 02/jul) que se revisou desta vez (ver Honestidade #1). Como o heating
oil é o principal componente de receita do biodiesel americano (a margem = receita de HO +
1,5×RIN D4, menos o custo do óleo de soja + custo industrial), o fechamento em 3,2566 —
**+2,34% acima dos 3,1822 de 02/07** — segue sendo um fator potencialmente favorável a uma
recuperação de margem quando o óleo de soja voltar a negociar. O sistema ainda não gerou um
indicador `margem_usd_galao` combinando o HO de 03/07 com um preço de óleo de soja mais
recente (o último indicador oficial segue sendo 0,5297 USD/gal, base 02/07, calculado com
óleo a 66,90 cts/lb e HO a 3,18 USD/gal) — esta leitura registra o sinal direcional sem
recalcular por conta própria.

**A curva forward do óleo (02/07/2026, valores revisados) mantém backwardation clara:**

| Vencimento | Código | Preço (cts/lb) | Var. vs Ago |
|---|---|---|---|
| Julho/26 | N26 | 66,87 | −0,03 |
| Agosto/26 | Q26 | 66,90 | — (spot) |
| Setembro/26 | U26 | 66,45 | −0,45 |
| Outubro/26 | V26 | 65,93 | −0,97 |
| Dezembro/26 | Z26 | 65,56 | −1,34 |
| Janeiro/27 | F27 | 65,42 | −1,48 |

A curva caindo -1,48 cts/lb de agosto a janeiro/27 continua sendo o argumento técnico mais
forte para manter posição vendida de médio prazo: quem rola a posição mês a mês colhe esse
carry independentemente da direção do preço à vista. Note-se que julho (N26, 66,87) já
negocia **abaixo** de agosto (Q26, 66,90) — uma pequena inversão dentro da própria ponta
curta da curva, coerente com backwardation moderada no front.

**O pano de fundo regulatório global segue reforçando a demanda de biodiesel como piso
estrutural da tese, mesmo com o preço tático em baixa.** O EPA Final RFS 2026/2027 (vigente
desde 15/06/2026, `system/tributario_watch.toml`, evento EPA-RFS-2026-2027) elevou os
volumes de biomassa-baseada em diesel (BBD) de 8,86 para 9,07 bilhões de RINs, com
realocação de 70% das isenções pequenas refinarias (SRE) — um salto de +61% ano contra ano
que sustenta o valor do RIN D4 (fixado em 2,11 USD/RIN no modelo interno) e, por extensão,
a receita do biodiesel americano. Em paralelo, a proposta do crédito 45Z (Clean Fuel
Production, em tramitação, audiência pública em 28/05) tende a excluir insumo importado da
elegibilidade — se confirmada, isso reforça a demanda por óleo de soja **doméstico**
americano especificamente (bullish para o CBOT), ao mesmo tempo em que libera sebo
brasileiro de volta ao mercado interno (efeito indireto, potencialmente aliviando o custo
de insumo do biodiesel brasileiro no 2S/26). Do lado do óleo de palma, a Indonésia
concentrou a exportação de CPO sob o fundo estatal Danantara desde 01/06 e mantém um levy
de exportação de até 12,5% (PMK 9/2026, vigente) — ambos encarecem a palma no mercado
internacional e favorecem o óleo de soja por substituição, ainda que sem poder ser
quantificado aqui porque o MPOB segue inacessível (ver Honestidade #5). Nenhum desses
fatores muda o viés tático de curto prazo (preço abaixo do suporte, curva em backwardation),
mas ajudam a explicar por que a tese bear é tratada como **tática**, e não estrutural, ao
contrário do farelo.

**O posicionamento dos fundos (COT de 23/06/2026, sem atualização — 12º dia)** segue sendo
o maior risco de reversão mecânica do complexo: managed money net long de **+103.206**
contratos, representando 15,7% do open interest de 658.976 — a maior exposição relativa das
três pernas. Sem dado novo do COT, ainda não há como confirmar se o desmonte observado nas
semanas anteriores continuou.

**O Índice de Suporte do Óleo (ISO) permanece em 100/100 (5/5 condições)** hoje
(indicadores, 05/07/2026), o **quinto pregão seguido** nesse patamar desde a virada de
01/07. Cinco sessões consecutivas — agora cobrindo a primeira semana de julho inteira mais
o fim de semana — seguem reforçando a hipótese de que a virada de 80 para 100 foi um efeito
de calendário (rolagem do mês-alvo de comparação ABIOVE de junho para julho), e não uma
mudança real de fundamento, mas continua sendo uma inferência lógica, não uma confirmação
direta (ver Honestidade #3).

### O que invalida / risco para o óleo

- **Heating oil sustentar o nível de 3,2566 quando o óleo de soja voltar a negociar:** se
  o HO continuar firme, a margem de biodiesel tem espaço para recuperar acima da faixa
  0,50-0,80 USD/gal — o principal fator de possível alívio para a tese bear.
- **Margem de biodiesel ultrapassar 0,80 USD/gal de forma sustentada:** último dado oficial
  (0,5297, base 02/07) está mais perto do piso da faixa 0,50-0,80 do que do teto.
- **RIN D4 real acima de 2,40 USD/RIN** (o modelo usa 2,11 fixo): incerteza estrutural
  bidirecional já sinalizada em leituras anteriores, sem novo dado hoje.
- **Dados de palma malaia (MPOB) inacessíveis há 20 dias consecutivos** (ver Honestidade
  #5) — se a produção de palma estiver caindo por El Niño ou pelas restrições indonésias,
  o óleo de soja ganharia prêmio de substituição global, o que seria altista.
- **WASDE de julho reduzir a área de soja americana:** menos esmagamento futuro nos EUA →
  menos óleo produzido → altista para os contratos de novembro em diante.
- **Exportação de óleo brasileiro projetada pela ABIOVE caindo de 110 mil t (setembro) para
  45 (outubro) e 21 (novembro)** — mais óleo represado internamente (bearish doméstico) ou
  mais disponibilidade para o mandato B15 (efeito ambíguo).
- **45Z e Danantara se concretizarem em volume relevante:** ambos são bullish para o óleo
  de soja americano por vias diferentes (proteção de insumo doméstico e restrição de oferta
  de palma), mas nenhum tem cronograma confirmado ainda.

### Leitura operacional — óleo

O viés segue bear tático, com a quebra do suporte 72,00 sem nenhum dado novo para
contestá-la. O carry negativo da curva forward continua favorecendo posição vendida de
médio prazo (referência de stop em torno de 69,50-70,00 cts/lb, mantida da leitura
anterior). O ponto de atenção real para os próximos dias é o heating oil: o nível de 3,2566
agora **confirmado estável** (não mais um dado intraday sujeito a revisão) é o primeiro
sinal consistente de que o piso da faixa de conforto do biodiesel (0,50 USD/gal) pode não
ser testado tão cedo — vale acompanhar de perto o primeiro fechamento de óleo de soja da
semana que vem para ver se a margem recalculada confirma esse sinal. Alvo primário do short
seguindo os forecasts (central 7d = 64,43 cts/lb, indicadores, 05/07/2026): zona de 64-66
cts/lb. Alvo secundário (central 30d = 55,34): 55-58 cts/lb, mas esse cenário exige que a
margem de biodiesel não recupere com o HO mais forte — monitorar diariamente antes de
assumir esse alvo como base. Para quem opera o oil share (fração do valor do crush
capturada pelo óleo, hoje em 52,29%), o viés estrutural segue favorecendo manter exposição
ao óleo dentro do crush frente ao farelo, mesmo com o preço absoluto do óleo em baixa
tática — a dominância relativa dentro do crush é outra dimensão da tese, distinta do nível
de preço isolado.

---

## Spreads e crush — leitura de complexo

### Crush margin: 2,7334 USD/bu (base 02/jul, revisada) — segue em leve compressão

A crush está em **2,7334 USD/bu** (Board Crush: farelo 305,20 + óleo 66,90 − soja 1.134,00;
indicadores, 02/07/2026, valores revisados — ver Honestidade #1). A trajetória recente
(3,0657 em 29/jun → 2,8056 em 30/jun → 2,7200 em 01/jul → 2,7334 em 02/jul) segue de leve
compressão, ainda comodamente acima do patamar narrativo de "alívio de esmagamento" (~2,50
USD/bu), mas sem dado novo desde 02/jul para confirmar continuidade.

### Ratio Far/Soj: 80,74% (base 02/jul, revisada) — travado a 0,74 p.p. do gatilho, D+24 da tese sem confirmação

Como detalhado na seção de Farelo (tratando a fila `revisao-2026-06-11...D+7`), o ratio
está em 80,74%, sem sessão para testar o cruzamento de 80%. O gatilho operacional do spread
de convergência (long farelo/short soja) permanece **não confirmado**, mas parado à menor
distância possível da confirmação há três pregões seguidos sem sessão.

### Oil share: 52,29% (base 02/jul, revisado) — estável

O oil share está em 52,29%, praticamente igual aos 52,20-52,41% da semana anterior — o óleo
ainda domina o crush (>50%), sem sinal de queda acelerada rumo a 50%.

### Oil-meal spread: 0,6446 USD/bu (base 02/jul, revisado) — estável

O oil-meal spread (contribuição do óleo menos a do farelo por bushel) está em 0,6446
USD/bu, na mesma faixa da semana anterior (0,6193-0,891) — óleo e farelo mantendo suas
posições relativas dentro do crush, com o óleo seguindo dominante.

### ISF em 80/100, ISO em 100/100 — quinto pregão seguido no novo patamar

O Índice de Sobra de Farelo (ISF) está em 80/100 (4/5 condições) e o Índice de Suporte do
Óleo (ISO) em 100/100 (5/5) — o mesmo patamar desde 01/jul, agora o **quinto** pregão
consecutivo, cobrindo a primeira semana de julho inteira mais o fim de semana. A
estabilidade por cinco sessões reforça a hipótese de que a virada foi um efeito mecânico da
rolagem do mês-alvo de comparação ABIOVE (junho → julho), não uma mudança real de
fundamento — mas segue sendo uma inferência lógica, não uma confirmação direta (ver
Honestidade #3).

### O que os índices dizem juntos em 05/07/2026

ISF 80/100 (efeito calendário, quinta confirmação) + ISO 100/100 (idem) + ratio 80,74%
(revisado hoje, travado a 0,74 p.p. do gatilho, sem sessão para testar) + oil share 52,29%
(estável) + oil-meal spread 0,6446 USD/bu (estável) + crush 2,7334 USD/bu (leve compressão)
+ margem biodiesel 0,5297 USD/gal (base 02/jul, sem captura ainda do HO estável em 3,2566)
+ COT (103k net longs em óleo, 12k em farelo com 98k shorts ativos, 37k em soja, todos de
23/jun, 12º dia sem atualização) + exportação de farelo ABIOVE caindo pela metade até
dezembro (1.400 → 700 mil t) sem o estoque doméstico desinchar na mesma proporção +
reversão confirmada do salto de Rondonópolis (dois pregões seguidos) + real apreciado desde
sexta (PTAX 5,1717) + físico de Paranaguá no maior nível da série (R$ 135,45/sc) + heating
oil confirmado estável em 3,2566 pela primeira vez em quatro leituras + terceira sessão
seguida sem pregão do complexo agrícola:

A leitura de hoje é de **estrutura intacta, sem teste de preço, com a própria base de dado
do dia 02/jul revisada retroativamente** (o evento mais notável do dump de hoje) **e um
heating oil que, pela primeira vez, se mostra estável entre duas leituras.** Nenhum desses
fatos muda a direção das teses estruturais (bear-farelo, bear-óleo tático, soja neutra) —
mas a combinação de um ratio Far/Soj parado a menos de um ponto percentual do gatilho com
uma revisão de dado que já moveu esse mesmo ratio em 0,08 p.p. sem nenhuma sessão nova de
mercado reforça que qualquer leitura de "rompimento" na reabertura de segunda-feira (06/07)
precisa de confirmação por mais de um fechamento antes de virar sinal operacional.

---

## Lente fiscal e regulatória BR

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L) entra na última
semana antes do vencimento em 11/07/2026 (fila `trib-MP-1358-2026-2026-07-11`, faltam **6
dias**).** A MP ressarce PIS/Cofins/Cide da gasolina e do diesel, mantendo o combustível
fóssil artificialmente mais barato — o mesmo mecanismo, em espírito, da MP 1.363/2026
(subsídio de R$ 1,12/L ao diesel, vigente até 31/12/2026, já tratada em
[[2026-05-26_subvencao-fossil-aperta-biodiesel]]), mas com foco específico na gasolina e
com vigência que expira em menos de uma semana. O próximo marco é a **deliberação da
comissão mista**, travada em regime de urgência desde 27/06/2026
(`system/tributario_watch.toml`, evento MP-1358-2026) — ou o Congresso delibera e converte
(ou rejeita) a MP até 11/07, ou ela caduca por decurso de prazo. O mecanismo de transmissão
para o complexo soja é indireto mas real: enquanto o combustível fóssil segue subsidiado, a
competitividade relativa do biodiesel dentro do mix B15 mandatório permanece pressionada (o
mix é 85% diesel mineral + 15% biodiesel; se o diesel mineral fica mais barato via
subvenção, o biodiesel não ganha proporcionalmente, e a indústria de biodiesel — maior
consumidora industrial de óleo de soja no Brasil — segue com margem mais apertada do que
teria sem a subvenção ao concorrente fóssil). **Este marco cai na mesma semana do WASDE de
julho (~10/07)** — dois catalisadores relevantes, um de oferta/demanda física e outro de
política de preços relativos, concentrados no mesmo intervalo de dias. Se a MP 1.358
caducar sem conversão em lei, é um sinal (fraco, mas real) de que o pacote pró-fóssil pode
perder fôlego político — levemente positivo para a competitividade do biodiesel e, por
extensão, para a demanda industrial de óleo de soja; se for convertida, reforça o quadro de
pressão já documentado desde maio.

**Isenção PIS/Cofins biodiesel — vencimento em 31/07/2026, 26 dias.** Sem sinalização
pública do MAPA ou MINFRA sobre renovação até hoje (05/07/2026,
`system/tributario_watch.toml`, evento PISCOFINS-BIODIESEL-ISENCAO). O checkpoint D+45
desse insight (10/07/2026, [[2026-05-26_pis-cofins-biodiesel-explica-mercado-fisico-fraco]])
cai em 5 dias, coincidindo com o WASDE e com o vencimento da MP 1.358 — a semana de
06-10/jul concentra três marcos relevantes ao mesmo tempo.

**B16 — sem data, travado em B15.** Sem mudança de status desde a última leitura (evento
B16-CNPE-2026, status "adiado", sem `proximo_data`).

**MP 1.363/2026 (subsídio ao diesel fóssil) — em vigor até 31/12/2026.** Sem alteração.
Bearish estrutural persistente para a demanda incremental de óleo de soja no mercado
doméstico brasileiro, na medida em que mantém o diesel mineral artificialmente mais
competitivo frente ao biodiesel para consumo voluntário acima do mandato.

**STJ REsp 2.165.276/2026 — crédito PIS/Cofins para esmagadoras.** Sem alteração desde a
última leitura. Estruturalmente bearish para o farelo — ao reduzir o custo tributário de
entrada da soja usada em biodiesel, incentiva mais esmagamento, mais oferta de co-produtos
(farelo incluído), coerente com a exportação de farelo ABIOVE projetada em queda.

**PTAX 5,1717 BRL/USD (BCB, 03/07/2026) — sem publicação no fim de semana.** O real
apreciou 0,44% frente ao dólar (de 5,1945 em 02/07) e também apreciou frente ao euro
(5,9154 vs 5,9472 de 02/07, -0,53%) — movimento consistente entre os dois pares, o que dá
mais confiança de que é um fortalecimento genuíno do real, não ruído isolado de um par
cambial. Com o CBOT ainda travado em 1.134,00 (revisado) e essa PTAX mais forte, a paridade
em reais tende a recuar frente aos R$ 129,86/sc oficialmente registrados (base 02/07, com
PTAX antiga de 5,1945) — o sistema não gerou o indicador recalculado combinando as duas
pontas mais recentes (ver Honestidade #2), mas a direção é clara: câmbio mais forte
pressiona a paridade para baixo, mesmo com o físico de Paranaguá subindo.

**Pano de fundo regulatório global (EUA e Indonésia) segue dando suporte estrutural ao
óleo, sem contradizer o viés bearish tático.** O EPA Final RFS 2026/2027 (vigente desde
15/06) e o crédito 45Z em tramitação (EUA) sustentam o valor do RIN D4 e favorecem o óleo
de soja doméstico americano; a centralização da exportação de palma pela Indonésia via
Danantara (desde 01/06) e o levy de exportação de CPO até 12,5% (PMK 9/2026, vigente)
encarecem a palma e favorecem o óleo de soja por substituição global — nenhum desses
fatores é BR-específico, mas todos operam no mesmo canal de demanda que sustenta o piso do
óleo, mesmo com o preço tático em baixa (detalhado na seção Óleo).

---

## Riscos e eventos próximos

**Terceira sessão seguida sem pregão do complexo agrícola (03-05/07).** A reabertura plena
ocorre na segunda-feira, 06/07 — dia útil normal nos EUA (o feriado de 4 de julho já foi
observado na sexta-feira 03/07). É a primeira oportunidade de testar se o ratio Far/Soj
(travado a 0,74 p.p. do gatilho de 80%), a reversão de Rondonópolis, a apreciação cambial e
o heating oil estável têm continuidade ou se dissolvem como ruído de fim de semana longo.

**Semana de 06-10/07 concentra três marcos fiscais/fundamentalistas no mesmo intervalo:**
WASDE de julho (~10/07), vencimento da MP 1.358 (11/07, deliberação de comissão mista) e
checkpoint D+45 da tese PIS/Cofins biodiesel (10/07). Rara concentração de catalisadores —
vale reservar atenção redobrada para essa semana específica.

**Padrão de revisão retroativa de dado — quarta ocorrência em cinco leituras, agora
atingindo os três contratos agrícolas ao mesmo tempo.** As leituras de 02/jul, 03/jul e
04/jul já haviam notado revisões pontuais (complexo agrícola em duas ocasiões, heating oil
em uma); hoje a revisão atinge simultaneamente soja, farelo e óleo do próprio 02/07,
enquanto o heating oil de 03/07 se mantém estável pela primeira vez. O padrão atravessa
quatro leituras seguidas — reforça a hipótese de que é uma característica sistemática do
pipeline de coleta (provavelmente a diferença entre um pull intraday e o settlement oficial
que chega dias depois), não um evento isolado. Vale reportar ao responsável técnico do
robô.

**COT CFTC — 12º dia sem publicação nova.** O dado mais recente continua sendo o de
23/06/2026. Esse dado é crítico para calibrar se os 103k net longs em óleo, 12k em farelo
(com 98k shorts) e 37k em soja mudaram desde o USDA de 30/06 e o rali subsequente.

**USDA Crop Progress — sem atualização nova, risco de atraso no relatório de segunda
(06/07) pelo feriado.**

**WASDE de julho — ~10/07/2026 (5 dias).** Primeiro WASDE pós-Acreage/Stocks, coincide com
o vencimento da MP 1.358 e o checkpoint D+45 da tese PIS/Cofins.

**Ratio Far/Soj em 80,74% (revisado) — travado a 0,74 p.p. do gatilho de 80% há três
pregões seguidos sem sessão para testar.** Item de maior sensibilidade operacional imediata
do complexo; monitorar o primeiro fechamento da reabertura com atenção redobrada, exigindo
mais de um fechamento de confirmação antes de tratar como rompimento (dada a sensibilidade
do valor a revisões de dado observada hoje).

**Reversão de Rondonópolis/MT — confirmada por dois pregões, segue fora do radar de risco
estrutural.**

---

## Honestidade

O que não foi possível validar neste briefing de 05/07/2026, onde a confiança é baixa ou há
lacunas materiais:

**1. Quarta ocorrência de revisão retroativa de dado em cinco leituras — desta vez atingindo
os três contratos agrícolas simultaneamente, e não mais um mercado isolado.** O fechamento
de 02/07/2026 usado nas leituras de 03/jul e 04/jul (soja 1.136,25 cts/bu, farelo 305,50
USD/sht, óleo 66,77 cts/lb, com volumes de 30.203/29.331/65.270 contratos respectivamente)
não confere com o dado assentado que chega no dump de hoje (soja 1.134,00, farelo 305,20,
óleo 66,90, volumes 43.860/21.083/46.162). Esta leitura usou os valores de hoje — os mais
recentes disponíveis — em todo o corpo do texto, e recalculou os indicadores derivados
(ratio Far/Soj, crush margin, oil share, oil-meal spread) a partir deles, exatamente como o
próprio briefing os apresenta (indicadores, 02/07/2026). Não há como saber, a partir do
dump disponível, se este é o valor final ou se haverá uma quinta revisão amanhã — o padrão
já atravessa quatro leituras seguidas e agora cobre os três contratos do complexo agrícola
ao mesmo tempo, o que é mais abrangente do que as ocorrências anteriores (que afetavam um
mercado por vez). Em contrapartida, o heating oil de 03/07 se manteve estável pela primeira
vez em quatro leituras — um dado a favor de que o processo de revisão tem um prazo de
"assentamento" após o qual o valor para de mudar, mas isso ainda não pôde ser confirmado
para o complexo agrícola. Vale reportar ao responsável técnico do robô.

**2. Paridade em reais (`soja_paridade_br`) não foi recalculada pelo sistema combinando o
CBOT revisado de 02/07 com a PTAX mais recente de 03/07.** O último indicador oficial
continua sendo 129,86 BRL/sc (base 02/07/2026, calculado com PTAX 5,1945, já desatualizada
frente aos 5,1717 de 03/07). Esta leitura registra a direção do efeito (paridade deve cair
com o real mais forte) mas **não estima um novo número**, porque não há confirmação de que
a fórmula exata (peso da saca, arredondamentos) usada pelo sistema produziria o mesmo
resultado se replicada manualmente — o número oficial só aparecerá quando o sistema
recalcular.

**3. A atribuição da virada do ISF/ISO ao efeito calendário ABIOVE não pôde ser confirmada
por consulta direta ao banco de dados.** O ambiente de execução deste insight não tem
acesso ao banco SQLite do sistema (apenas ao dump `briefing/latest.md`), então a conclusão
de que a rolagem do mês de referência (junho→julho) é a causa da inversão dos índices —
reforçada hoje pela estabilidade do novo patamar por cinco pregões seguidos — é uma
inferência lógica bem fundamentada, mas não uma verificação direta linha a linha do código.

**4. NOPA — dado inacessível há mais de um mês** (fila `release-nopa-2026-07-05` tratada
aqui). `monthly_status = 0.0 bool` (indicadores, 05/07/2026). O esmagamento americano de
junho/2026 segue sem fonte primária acessível.

**5. Palma malaia (MPOB) — 20 dias consecutivos sem dados numéricos** (16/jun a
05/07/2026). O parser continua retornando apenas 3.428 chars de HTML sem valores extraídos.
Sem os preços de CPO na BMD, não é possível quantificar o efeito do El Niño nem das
restrições regulatórias indonésias (Danantara, levy PMK 9/2026) sobre a produção e o
prêmio de substituição para o óleo de soja americano — apenas o mecanismo qualitativo pôde
ser descrito (seção Óleo e Lente Fiscal).

**6. RIN D4 como parâmetro fixo (2,11 USD/RIN) segue sendo a maior fonte de incerteza do
modelo de biodiesel.** Não há dado de mercado secundário no briefing para confirmar se o
valor real mudou, apesar do EPA Final RFS ter elevado os volumes obrigatórios desde 15/06.

**7. COT com defasagem de 12 dias em relação ao evento USDA e ao rali subsequente.** O dado
mais recente segue sendo de 23/06/2026 — deixa às cegas a leitura de como os fundos
reagiram ao movimento de preço mais relevante do trimestre e à apreciação cambial da
semana.

**8. BCBA Argentina — sem relatórios de esmagamento/exportação acessíveis via scraper**
(page_fetched=1,0 mas sem links de relatório, 05/07/2026). O ritmo de processamento
argentino pós-colheita (50,1 mi t) é estimado por notícia, não medido por fonte primária.

**9. Percentis históricos de COT não calculados** — os 103k net longs em óleo, 12k em
farelo (com 98k shorts) e 37k em soja são grandes em termos absolutos, mas sem série
histórica completa para calibrar percentil.

**10. O feed CEPEA RSS não atualiza a contagem de itens desde 30/06/2026** (101 itens),
mais de cinco dias sem refresh — não afeta os preços físicos (que vêm de fonte separada,
NAG), mas é uma lacuna de cobertura de notícias que vale registrar.

**11. A reversão do salto de Rondonópolis/MT permanece sem explicação causal no
briefing** — sabemos que o preço saiu de R$ 1.500 para R$ 1.650 (01-02/jul) e voltou para
R$ 1.500 (03-04 dias seguidos), mas não há nenhuma notícia ou evento que explique nem o
salto nem a reversão. A leitura mais honesta continua sendo "ruído de coleta provável", não
uma certeza.

*Nenhum número foi inventado ou estimado além do que consta no briefing de 05/07/2026 e nos
insights anteriores referenciados. A maior contribuição desta leitura foi identificar e
documentar com transparência a revisão retroativa do próprio settlement de 02/07 — que
moveu os três contratos agrícolas e os indicadores derivados sem nenhuma sessão nova de
mercado — e usar consistentemente os valores mais recentes do dump de hoje em vez de
misturar dados de leituras anteriores já superadas. O bear-farelo estrutural (ratio Far/Soj
a 0,74 p.p. do gatilho, exportação ABIOVE em queda sem desinchar o estoque doméstico) e o
bear-óleo tático (confirmado abaixo do suporte 72,00, com o heating oil agora estável)
seguem com a base de dados mais sólida desta leitura; a soja neutra e o efeito da
apreciação cambial sobre a paridade têm confiança moderada, pendente de confirmação
numérica na reabertura de segunda-feira (06/07).*
