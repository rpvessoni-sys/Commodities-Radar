---
data: 2026-08-05
titulo: "Farelo lidera a compressão do ratio Far/Soj pela primeira vez em dias (80,47%, o mais próximo do piso <80% desta janela) enquanto o óleo confirma quebra técnica com a curva futura virando backwardation e o físico de farelo no RS rompe uma semana de congelamento com salto de +9,76%"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT (ZSU26 soja / ZMU26 farelo / ZLU26 óleo) — sessão de 2026-08-05, volumes: farelo 25.064 contratos (mais líquido), óleo 21.090, soja 18.818
  - CME NYMEX heating oil (HO=F) — 2026-08-05, fechamento 3,7805 USD/galão, volume de 45 contratos (baixa liquidez, ver Honestidade)
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, paridade BR, Índice de Sobra de Farelo, Índice de Suporte do Óleo) — recalculados com o fechamento de 2026-08-05
  - BCB PTAX — 2026-08-05 (USD/BRL 5,1154, EUR/BRL 5,9062, Selic diária 0,052531% a.a.)
  - CEPEA/ESALQ Soja Paranaguá via NAG — 2026-08-05, R$ 144,91/saca (var +0,55%) — carimbo do mesmo dia, primeira comparação apples-to-apples com a paridade papel em várias sessões
  - CEPEA/ESALQ Soja Paraná interior via NAG — 2026-08-05, R$ 136,73/saca (var +0,51%)
  - NAG Físico BR — 2026-08-05 (farelo MT/IMEA R$ 1.675,10/ton, var 0,0%; Rondonópolis/MT R$ 1.700,00/ton, var 0,0%; RS média R$ 1.800,00/ton — salto vs R$ 1.640,00 congelado desde 2026-07-27); prêmios export PGUA farelo/óleo sem carimbo novo hoje, último em 2026-08-04 (farelo +0,05 USD/sht; óleo +0,08 cts/lb, "mês Agosto/26")
  - CFTC COT Managed Money — corte de 2026-07-28 (sem corte novo nesta janela; o próximo, referente a 2026-08-04, só sai por volta de 2026-08-07)
  - USDA Crop Progress — corte rotulado 2026-08-02, mesmos valores do corte de 2026-07-26 (11% excelente / 52% boa / 7% ruim), agora pela terceira leitura seguida sem mudança
  - USDA WASDE — ausente da janela, agora 26 dias de atraso desde o último dado (2026-07-10)
  - NOPA — fila `release-nopa-2026-08-05`, `monthly_status` continua em 0,0 bool (paywall)
  - ABIOVE projeções mensais — balanços ago-dez/2026, sem alteração frente ao dump anterior
  - NOAA CPC ENSO — 2026-08-05 (El Niño Advisory, inalterado)
  - MPOB — 2026-08-05 (mesmo conteúdo de 3.439 caracteres, parser sem números extraídos)
  - BCBA Argentina — 2026-08-05 (acessível, sem links de relatório detectados, mesmo padrão de sessões recentes)
  - INMET — previsão para 2026-08-06: chuva/trovoada em Cascavel e Maringá (PR) e Passo Fundo (RS, risco de granizo); calor seco em Cuiabá, Lucas do Rio Verde, Rio Verde (GO), Sinop e Sorriso (MT, 35-37°C, poucas nuvens)
  - Notícias Agrícolas/Canal Rural RSS — 2026-08-05 (160 itens lidos, 3 mantidos; manchete "Datagro prevê alta de 1,5% na produção de soja na safra 26/27", canalrural.com.br)
  - system/tributario_watch.toml (lido como referência, não editado) — `atualizado_em` 2026-06-05, agora 61 dias sem atualização; evento `PISCOFINS-BIODIESEL-ISENCAO` com `vigencia_ate` 2026-07-31, hoje é o 3º dia útil desde o vencimento
  - Cruza com [[2026-08-04_leitura-complexo]], [[2026-08-03_leitura-complexo]], [[2026-08-02_leitura-complexo]] e [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (tese original do D+7, tratada abaixo)
status: ativa
vies: [neutral-soja, bear-farelo, bear-oleo_soja]
---

## Visão geral

O complexo soja é, mecanicamente, uma fábrica com uma única matéria-prima (a
soja em grão) e dois produtos de saída em proporção fixa por bushel esmagado:
o **farelo** (a fração proteica, ~78% da massa, vira ração animal) e o **óleo
degomado** (a fração de gordura, ~18-20% da massa, vira óleo de cozinha e
biodiesel). Quem decide o ritmo de esmagamento é a esmagadora, olhando dois
números: a **crush margin** (o valor de farelo + óleo por bushel, menos o
custo daquele bushel de soja, todos medidos na CBOT — Chicago Board of Trade,
a bolsa de referência mundial para esses três contratos) e o **oil share** (a
fração desse valor capturada especificamente pelo óleo). Quando o oil share
sobe, o óleo "manda" no crush — a esmagadora aceita vender o farelo mais
barato porque o que sustenta a decisão de esmagar é a margem do óleo, e o
farelo vira, na prática, o subproduto que sobra. O **ratio Far/Soj** (preço
do farelo dividido pelo preço da soja, normalizado pela conversão
bushel↔short ton) mede a mesma dinâmica por outro ângulo: abaixo de 80% o
farelo está historicamente "abundante" frente à soja — zona baixista para o
farelo —, acima de 87% está "apertado" — zona altista —, e entre os dois fica
a zona neutra de mean-reversion (o preço tende a voltar pro meio quando se
afasta demais de um extremo).

**Hoje, 2026-08-05, quarta-feira, foi um dia de consolidação na soja, mas com
um sinal genuinamente novo no farelo e uma confirmação estrutural no óleo.**
A soja fechou em **1.158,25 cts/bushel** (CBOT, ticker ZSU26.CBT), praticamente
inalterada frente ao fechamento de ontem (1.158,75, **-0,04%**), depois de
abrir exatamente no fechamento de ontem, testar uma máxima de 1.161,75 e
devolver para uma mínima de 1.148,75 — um dia de amplitude estreita (13,00
pontos) que fecha a 73,1% do range, no terço superior, sem repetir o padrão
de reversão forte das duas sessões anteriores. O farelo, ao contrário, caiu
de forma mais consistente: fechamento de **310,70 USD/short ton**
(ticker ZMU26.CBT), **-0,64%** sobre ontem (312,70). **O que torna isso
relevante é o mecanismo por trás do ratio Far/Soj**: como o farelo caiu mais
em termos percentuais do que a soja hoje, o ratio comprimiu de **80,96% para
80,47%** (indicators, 2026-08-05) — uma queda de -0,49 ponto percentual que,
pela primeira vez em várias sessões, foi **genuinamente originada pelo
farelo**, não pela soja (nas duas sessões anteriores documentadas em
[[2026-08-04_leitura-complexo]], o ratio se moveu por causa do denominador
errado). Trata `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
(fila de hoje) — o valor de 80,47% é o mais próximo do piso <80% desta janela
de 14 dias do briefing. O óleo fechou em **67,74 cts/lb** (ticker ZLU26.CBT),
**-0,67%**, seguindo abaixo do suporte técnico de 72,00 — trata
`alerta-quebra_suporte-oleo_cbot-2026-08-05` (fila de hoje) — e, pela
primeira vez nesta série de leituras, a curva futura do óleo (Q26 67,86 →
U26 67,74 → V26 67,46 → Z26 67,22 → F27 67,12 → H27 67,04) está em
**backwardation** (contratos mais distantes valendo menos), enquanto soja e
farelo seguem em contango normal (curvas crescentes). No físico brasileiro,
o farelo no Rio Grande do Sul rompeu uma semana de congelamento total: de
R$ 1.640,00/ton (parado desde 27/07) para **R$ 1.800,00/ton** hoje, um salto
de **+9,76%** — o dado físico mais expressivo do dia, tratado com cautela
metodológica na seção Honestidade. **Leitura de uma linha:** o pivô do
complexo hoje é a divergência entre a calmaria da soja (dia de amplitude
estreita, sem tese nova) e dois sinais estruturais que se moveram de forma
mais "limpa" nas outras duas pernas — o ratio comprimindo pelo motivo certo
no farelo, e a curva do óleo invertendo enquanto o preço confirma a quebra
técnica —; maior convicção desta leitura está no mecanismo do ratio (farelo
efetivamente mais fraco que soja hoje, dado consistente e verificável);
confiança moderada para o salto do físico no RS, que carece de confirmação
por não ter histórico de volatilidade recente; confiança baixa para
extrapolar qualquer tese direcional da soja a partir de um dia de range
estreito sem notícia nova de peso.

---

## Soja

**Viés: neutro tático — dia de amplitude estreita (13,00 pontos, a menor
desta série de leituras recentes), fechamento praticamente idêntico ao de
ontem, sem notícia de demanda chinesa nova pela primeira vez em várias
sessões e substituída por um headline de oferta interna brasileira.**
Fechamento: 1.158,25 cts/bushel (CBOT, ticker ZSU26.CBT, 2026-08-05).

### O que sustenta a tese

**A sessão foi de consolidação, não de continuidade do padrão de reversão
das duas sessões anteriores.** Abertura 1.158,75 (exatamente no fechamento
de ontem — gap zero, sinal de que o mercado não trouxe viés direcional
overnight), máxima **1.161,75** (bem abaixo da resistência de 1.180,00
identificada em leituras anteriores e também abaixo das máximas testadas nos
dois últimos pregões, 1.177,00), mínima 1.148,75, fechamento **1.158,25**.
A amplitude do dia (13,00 pontos) é a menor das últimas cinco sessões
documentadas nesta série — um contraste direto com o padrão de "teste de
resistência + reversão forte" que caracterizou 2026-08-03 e 2026-08-04.
O fechamento a 73,1% do range (acima do meio, mas sem fazer máxima nova)
sugere um dia de digestão, não de definição de tendência. O volume de
18.818 contratos é o mais baixo dos três legs hoje e também abaixo do
volume médio das sessões recentes (23-24 mil contratos) — consistente com
um dia de menor convicção direcional, não de liquidez anômala a ponto de
gerar alerta.

**A curva futura da soja segue em contango consistente, sem sinais de
inversão.** Q26 (ago/26) 1.152,00, U26 (set/26) 1.158,25, X26 (nov/26)
1.176,75, F27 (jan/27) 1.191,50, H27 (mar/27) 1.198,00, K27 (mai/27)
1.206,50 — cada vencimento mais distante vale mais que o anterior, o
desenho clássico de um mercado de armazenagem sem aperto de oferta prompt.
**Mecanismo:** contango crescente e regular (sem "corcova" nem inversão)
indica que o mercado não está precificando escassez física iminente da
soja — é consistente com a fase de entressafra brasileira e estoques
americanos ainda sendo processados, e contrasta com o desenho invertido
que aparece no óleo (ver seção Óleo).

**O câmbio favoreceu de leve a paridade em reais, mas o efeito foi pequeno
frente à quase estabilidade do papel.** USD/BRL PTAX fechou em **5,1154**
(BCB, 2026-08-05), **+0,20%** frente a ontem (5,1053) — o real desvalorizou
ligeiramente. A paridade teórica em reais (sem prêmio de basis) subiu para
**R$ 130,62/saca** (indicators, CBOT 1.158,25 cts × USD/BRL 5,1154),
**+0,15%** sobre ontem (130,42) — um movimento pequeno, coerente com a
soja praticamente parada e o câmbio com variação modesta.

**O físico de exportação trouxe, pela primeira vez em várias sessões, um
carimbo do MESMO DIA que a paridade — permitindo uma comparação real, não
defasada.** CEPEA/ESALQ Soja Paranaguá (via NAG) fechou em **R$ 144,91/saca**
hoje, **+0,55%** sobre ontem (144,12) — ambos os números (144,91 físico e
130,62 paridade) são de 2026-08-05. O prêmio físico sobre a paridade teórica
fica em **+10,94%** ((144,91-130,62)÷130,62), o maior desta série recente de
leituras e, pela primeira vez, calculado sem a ressalva de defasagem de
datas que marcou as últimas comparações. **Mecanismo:** esse prêmio mede
quanto o mercado físico de exportação em Paranaguá paga acima do que a
soja "deveria valer" convertendo o CBOT pelo câmbio puro, sem transporte,
armazenagem ou custo portuário — um prêmio consistentemente na casa de
9-11% ao longo das últimas sessões sugere que a demanda física por soja
brasileira pronta para embarque segue firme mesmo em entressafra, ou que a
oferta disponível para pronta entrega está mais escassa do que a média
histórica desse basis sugeriria. A soja Paraná interior seguiu o mesmo
movimento, fechando em **R$ 136,73/saca**, **+0,51%** sobre ontem (136,03).

**O posicionamento do COT (CFTC, corte de 28/07/2026) segue sendo o retrato
mais recente — nenhum corte novo hoje.** O managed money net long em soja
estava em 160.479 contratos (15,73% do open interest de 1.020.108), após
uma alta de +22,97% na semana anterior ao corte. Sem dado novo, essa
posição segue como pano de fundo: os fundos entraram nesse corte com uma
posição comprada relativamente esticada, construída num período em que o
preço rondava o topo recente (fechamento de 28/07: 1.204,75). A soja de
hoje (1.158,25) está -3,86% abaixo desse nível — a mesma distância de
"dor" documentada ontem, sem piora nem alívio adicional no dia de hoje.

**A notícia do dia muda de assunto: pela primeira vez em várias sessões,
não há manchete sobre compra chinesa — a manchete do dia é sobre oferta
brasileira.** "Datagro prevê alta de 1,5% na produção de soja na safra
26/27" (Canal Rural, 05/08/2026) — a consultoria privada Datagro projeta
alta de 1,5% na produção brasileira da PRÓXIMA safra (2026/27, que será
plantada em setembro-outubro de 2026 e colhida a partir de janeiro de
2027). **Mecanismo:** esse é um dado de oferta futura, não de demanda
imediata — não compete diretamente com o prêmio físico de exportação
observado hoje em Paranaguá (que reflete a safra atual, já em entressafra),
mas é um sinalizador estrutural de médio prazo: mais produção esperada para
26/27 é, na margem, um fator baixista para a curva mais distante da soja
(coerente com o contango já observado, que precifica os vencimentos de
2027 mais altos em termos nominais, mas sem incorporar ainda pressão de
oferta de uma safra recorde). Vale notar que apenas 3 dos 160 itens do RSS
de hoje foram mantidos como relevantes para soja/farelo/óleo — a menor
seleção desta série de leituras, sugerindo um dia de baixo fluxo de notícia
fundamentalista específica do complexo.

### O que invalida / risco para a soja

- **Uma manchete de demanda chinesa retornar com tonelagem USDA-FAS
  confirmada** — a ausência de notícia hoje não significa ausência de
  demanda; a lacuna de headline pode se reverter a qualquer momento e
  reacender o driver que dominou as últimas sessões.
- **O prêmio físico de Paranaguá (+10,94% hoje) recuar de forma abrupta**
  quando/se a oferta doméstica aumentar — hoje é a primeira leitura
  apples-to-apples desse prêmio em várias sessões, então uma reversão
  desse nível precisaria ser confirmada por pelo menos mais um dia de dado
  fresco antes de ser tratada como mudança de tendência.
- **Um fechamento definitivo fora do range estreito de hoje** (acima de
  1.161,75 ou abaixo de 1.148,75) — romperia a consolidação e definiria
  direção para os próximos pregões.
- **A previsão da Datagro (safra 26/27 +1,5%) ganhar corroboração de outras
  consultorias ou do próprio USDA** quando o WASDE finalmente voltar a
  ser publicado (26 dias de atraso hoje) — reforçaria o viés de oferta
  maior na curva distante.
- **O câmbio reverter para um real mais forte** justamente se o CBOT
  ficar mais fraco — combinação que aprofundaria a paridade em reais sem
  qualquer mudança na oferta/demanda física.

### Leitura operacional — soja

Para quem opera os dois lados, o dia de hoje não oferece um gatilho técnico
novo: a amplitude estreita e o fechamento perto de ontem sugerem que o
mercado aguarda o próximo catalisador — seja uma manchete de exportação
confirmada, seja o corte do COT de 07/08, seja o WASDE (ainda sem data
neste briefing). Para quem está posicionado a partir das reversões dos
últimos dois pregões, este é um dia de manutenção, não de ação: o range de
hoje (1.148,75-1.161,75) vira a referência mais próxima de suporte/resistência
para a abertura de amanhã. Para quem acompanha o basis físico de exportação,
o prêmio de +10,94% calculado hoje com dados do mesmo dia é o número mais
confiável desta série recente para avaliar se vale a pena originar física
para Paranaguá versus vender no mercado futuro — mas a recomendação é
aguardar pelo menos mais uma leitura de dado fresco antes de tratar esse
nível como "o novo normal" do prêmio.

---

## Farelo

**Viés: bear tático com conviccão moderada — o ratio Far/Soj comprimiu hoje
pela primeira vez em dias por causa do próprio farelo (não da soja), e o
Índice de Sobra de Farelo permanece no mesmo nível estrutural há sete
pregões seguidos.** Trata `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
(fila de hoje) e `release-nopa-2026-08-05` (fila de hoje, mesmo bloqueio de
sempre, ver abaixo). Fechamento: 310,70 USD/short ton (CBOT, ticker
ZMU26.CBT, 2026-08-05).

### O D+7 chega a 48 dias vencido — e hoje, pela primeira vez, o motor é o farelo

A tese original ([[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]])
apostava que a compressão rápida do ratio em junho (83,3%→81,4% em 4
pregões) levaria à zona comprimida (<80%) "em 1-2 semanas". O checkpoint
formal (D+7) caiu em 18/06/2026; hoje, 05/08/2026, são **48 dias corridos**
sem confirmação do fechamento abaixo de 80%. **O que muda hoje é a
qualidade do sinal, não apenas o nível.** Nas duas sessões anteriores
documentadas em [[2026-08-04_leitura-complexo]], o ratio se moveu
por causa da soja (numerador errado): em 03/08 a soja subia mais que o
farelo, empurrando o ratio para baixo "por acidente"; em 04/08 a soja caía
mais que o farelo, empurrando o ratio para cima, também "por acidente".
**Hoje o padrão se inverte de forma genuína**: a soja ficou praticamente
parada (-0,04%) enquanto o farelo caiu de forma mais consistente (-0,64%)
— o numerador (farelo) encolheu, não o denominador (soja) que se expandiu
relativamente. O ratio caiu de **80,96% para 80,47%** (indicators,
2026-08-05), uma queda de -0,49 ponto percentual que é, pela primeira vez
em três sessões, atribuível ao próprio farelo enfraquecendo — exatamente o
mecanismo que a tese original de junho previa (farelo "sobrando" e cedendo
preço relativo à soja). **Ainda assim, 80,47% permanece acima do limiar de
80% que definiria a zona "abundante"** — a tese segue tecnicamente não
confirmada, mas o dado de hoje é qualitativamente mais forte a favor dela
do que qualquer um dos últimos dois pregões. O próximo marco formal
continua sendo o D+90 (2026-09-09, a 35 dias de hoje).

### O que sustenta a leitura de hoje

**A crush margin recuou -3,21%, revertendo parte da melhora de ontem —
farelo e óleo caindo mais rápido, em conjunto, do que a soja.** Crush margin
de **2,7043 USD/bushel** (farelo 310,70 + óleo 67,74 − soja 1.158,25),
ante 2,7939 ontem. **Mecanismo:** como a soja (custo) ficou praticamente
parada enquanto farelo e óleo (receita) caíram, a margem da esmagadora
encolheu — o oposto exato do que aconteceu ontem, quando a soja caiu mais
que farelo+óleo e a margem melhorou apesar da queda geral de preços. Mesmo
assim, 2,7043 USD/bu segue **folgada** frente ao nível de alerta histórico
(<2,50 USD/bu) — não há sinal de que a esmagadora precise reduzir ritmo de
esmagamento por aperto de margem.

**O oil-meal spread recuou -1,06%, de 0,6226 para 0,616 USD/bushel** — uma
queda modesta, terceira sessão seguida de oscilação nesse spread sem
direção clara de médio prazo. O oil share seguiu **essencialmente
inalterado, 52,16% hoje vs 52,16% ontem** (o valor absoluto do óleo caiu de
7,50 para 7,45 e o total de 14,38 para 14,29, mas a proporção não se
moveu) — reforça a leitura de que a divisão de valor dentro do crush entre
óleo e farelo segue estável, mesmo com o vaivém técnico das últimas
sessões em ambos os produtos.

**As praças físicas de farelo no Brasil (NAG) trouxeram o dado mais
notável do dia: o Rio Grande do Sul rompeu uma semana inteira de
congelamento.** Mato Grosso/IMEA seguiu travado em R$ 1.675,10/ton (var
0,0%, mesmo valor desde 31/07) e Rondonópolis/MT também parado em
R$ 1.700,00/ton (var 0,0%, mesmo valor desde 31/07). Mas a média do Rio
Grande do Sul (Clicmercado, via NAG) saltou de **R$ 1.640,00/ton — nível em
que estava parada desde pelo menos 27/07 (sete pregões seguidos com var
0,0%) — para R$ 1.800,00/ton hoje, um salto de +9,76%**. **Mecanismo e
leitura:** este é exatamente o tipo de movimento que a leitura de ontem
antecipava como risco ("o represamento tende a se resolver com um salto
quando a liquidez normalizar, não com uma caminhada suave") — mas um único
salto isolado, sem um segundo dia de confirmação, não permite distinguir
entre (a) uma correção real de preço represada por falta de atualização de
mercado, e (b) uma anomalia pontual de coleta de dados (a mesma cautela
metodológica que esta série já aplica ao heating oil, ver Óleo e
Honestidade). Tratado aqui como o evento físico mais relevante do dia, mas
sem tese direcional definitiva até uma segunda leitura confirmar o novo
patamar.

**O Índice de Sobra de Farelo (ISF) permanece em 80/100 (4 de 5 condições
estruturais) pelo sétimo pregão consecutivo** (30/07 a 05/08, todos com o
mesmo valor), inalterado. As projeções ABIOVE seguem mostrando a
exportação de farelo brasileiro caindo de 1.400 mil toneladas em agosto/2026
para 700 mil toneladas em dezembro/2026, uma queda de -50% em quatro meses
(ABIOVE projeções mensais, sem alteração frente ao dump anterior) — o driver
estrutural mais lento e mais persistente desta tese, à margem do ruído
tático diário do ratio.

**Prêmio de exportação em Paranaguá segue sem carimbo novo hoje** — a
última leitura permanece em 2026-08-04 (+0,05 USD/short ton, "mês
Agosto/26"), o mesmo nível "zerado" que sustentava o pilar original da
tese de junho ("exportar não compete, o farelo sobra no mercado
doméstico"). **Mecanismo:** um prêmio de exportação perto de zero por
semanas seguidas significa que o mercado externo não está pagando o
suficiente acima do preço doméstico para justificar direcionar farelo
brasileiro para o porto — o farelo fica represado internamente, pressão
estrutural de baixa que não aparece diretamente no CBOT, mas que reforça
o mecanismo por trás do ISF.

**`release-nopa-2026-08-05` (fila de hoje) sinaliza novo carimbo, mas o
`monthly_status` permanece em 0,0 bool** — mesma barreira de assinatura
paga documentada desde meados de junho, agora sem alternativa de dado
primário sobre o crush americano há mais de 8 semanas. Tratado como item
da fila resolvido (sem conteúdo novo para incorporar), não como pendência
de leitura.

### O que invalida / risco para o farelo

- **O ratio Far/Soj não confirmar a compressão de hoje amanhã** — um único
  dia de farelo liderando a queda não é, por si só, uma tendência; a
  recomendação desta leitura é a mesma de sempre: exigir mais de uma
  sessão seguida na mesma direção antes de tratar como sinal robusto.
- **O salto do físico no RS (+9,76%) se revelar um problema de coleta**,
  não uma correção real de preço represado — nesse caso, o dado de hoje
  precisaria ser descartado como driver da leitura de farelo físico.
- **O salto do físico no RS se confirmar e se espalhar para MT/IMEA e
  Rondonópolis**, que seguem congelados — indicaria uma correção de
  represamento generalizada, não isolada ao Sul.
- **O prêmio de exportação em Paranaguá sair de zero** depois de mais de
  um mês parado — mudaria o cálculo de competitividade externa que
  sustenta o ISF.
- **A crush margin cair de forma mais persistente** rumo ao nível de
  alerta (<2,50 USD/bu) — reduziria o incentivo da esmagadora a manter
  ritmo de esmagamento, encolhendo a oferta de farelo na origem.

### Leitura operacional — farelo

Para quem monitora o ratio Far/Soj como gatilho tático (long farelo/short
soja ou vice-versa na convergência), o movimento de hoje é o primeiro em
várias sessões que reforça geneticamente a tese de compressão — mas a
recomendação segue sendo a mesma: uma sessão isolada não substitui a
confirmação de mais de um pregão seguido na mesma direção, especialmente
depois de duas sessões recentes em que o ratio se moveu pelo motivo
"errado". Para quem opera o físico de farelo no RS, o salto de hoje
(R$ 1.640→1.800/ton) merece verificação direta antes de qualquer decisão
de originação ou hedge baseada nesse nível — não é prudente tratar um
único pregão pós-congelamento de sete dias como o novo preço de mercado
sem confirmação. Para quem opera o oil-meal spread ou o crush como posição
relativa, a estabilidade do oil share (52,16% pelo segundo dia seguido, na
prática) sugere que não há sinal novo de mudança estrutural na divisão de
valor dentro do crush — o spread segue mais como reflexo do vaivém técnico
diário do que uma oportunidade de posição nova.

---

## Óleo

**Viés: bear estrutural com quebra técnica confirmada — quinto (ou mais)
pregão seguido abaixo do suporte 72,00, agora acompanhado por uma curva
futura que virou backwardation, um sinal que soja e farelo não mostram.**
Trata `alerta-quebra_suporte-oleo_cbot-2026-08-05` (fato: 67,74 vs nível
72,00). Fechamento: 67,74 cts/lb (CBOT, ticker ZLU26.CBT, 2026-08-05).

### O que sustenta a tese

**O óleo caiu de forma consistente, fechando no terço inferior do range do
dia.** Abertura 68,13, máxima **68,55**, mínima 67,37, fechamento **67,74**
— um candle que fecha a apenas 31,4% do range ((67,74-67,37)÷(68,55-67,37)),
um dia de viés vendedor mais linear do que os candles de reversão das
sessões anteriores (que abriam perto do topo e devolviam quase tudo; hoje
o óleo simplesmente não conseguiu sustentar a máxima e fechou perto da
mínima, sem o mesmo padrão de "falha de rompimento" das últimas sessões).
Em nível, **67,74 está -5,92% abaixo do suporte técnico de 72,00** que a
fila de julgamento monitora desde 31/07 — a distância aumentou levemente
frente a ontem (usando o fechamento de 68,20 do dia anterior, conforme a
tabela de indicadores, a distância era de -5,28%). O volume de 21.090
contratos é saudável, o segundo mais alto dos três legs hoje.

**Pela primeira vez nesta série de leituras, a curva futura do óleo está
em backwardation — o oposto do desenho de soja e farelo.** Os fechamentos
por vencimento hoje: Q26 (ago/26) 67,86, U26 (set/26) 67,74, V26 (out/26)
67,46, Z26 (dez/26) 67,22, F27 (jan/27) 67,12, H27 (mar/27) 67,04 — cada
vencimento mais distante vale MENOS que o anterior, uma sequência
decrescente e regular. **Mecanismo:** backwardation em commodities
normalmente sinaliza aperto de oferta no curto prazo relativo ao longo
prazo — o mercado paga mais pelo óleo disponível agora do que pelo óleo
de daqui a alguns meses. Isso pode parecer contraditório com a tese bear
de preço absoluto, mas as duas leituras não se excluem: o nível absoluto
do óleo pode estar caindo (quebra de suporte) ao mesmo tempo em que a
curva relativa entre vencimentos reflete uma expectativa de que a pressão
baixista se intensifique ainda mais nos meses seguintes (dez/26 a mar/27) —
por exemplo, se o mercado espera mais oferta de palma malaia/indonésia
entrando no período, ou se a incerteza regulatória do biodiesel americano
(isenção PIS/Cofins no Brasil, 45Z-CLEAN-FUEL nos EUA, ambos sem definição
— ver Lente fiscal) pesa mais sobre a demanda futura do que sobre a
demanda imediata. Isso contrasta diretamente com o contango regular de
soja e farelo (ver seções anteriores), tornando o óleo a única das três
pernas com uma estrutura de curva invertida hoje — um dado que merece
monitoramento nos próximos pregões para ver se a backwardation se aprofunda
(reforçando aperto de curto prazo) ou se dissolve (voltando a contango,
sinal de normalização).

**A margem de biodiesel americana subiu, mas segue construída sobre um
heating oil de liquidez baixa pela quarta sessão seguida.** O custo (lado
óleo) caiu para **5,0805 USD/galão** (-0,67%, acompanhando a queda do
óleo CBOT). A receita subiu para **6,9455 USD/galão** (+0,14%), porque o
heating oil (HO=F) fechou em **3,7805 USD/galão**, **+1,23%** sobre o
fechamento de ontem (3,7347) — mas negociando apenas **45 contratos**,
uma fração do volume normal e na mesma faixa anômala das últimas três
sessões (26, depois 48, agora 45 contratos). O resultado é a margem de
biodiesel subindo para **1,065 USD/galão**, **+4,36%** sobre o número já
sinalizado como não confiável ontem (1,0205) — mas ainda bem abaixo do
patamar de uma semana atrás (1,4579 em 30/07, 1,442 em 31/07), um recuo de
cerca de -27% em uma semana se comparado a esses níveis. **Esta leitura
trata a margem de biodiesel como não confirmada pela quarta sessão
seguida** — o lado do custo (óleo, 21.090 contratos) é confiável, o lado
da receita (heating oil, 45 contratos) segue não sendo, e a série já
qualifica esse padrão de múltiplos dias de baixíssima liquidez como
possível problema de coleta, não apenas ruído pontual (ver Honestidade).
O RIN D4 embutido na receita (2,11 USD/RIN) é um parâmetro fixo do
indicador — reflete o mandato EPA-RFS-2026-2027 (vigente desde 15/06/2026,
sem novo evento) e não é um dado de mercado observado diariamente.

**O Índice de Suporte do Óleo (ISO) permanece em 100/100 (5 de 5
condições) pelo sétimo pregão consecutivo** (30/07 a 05/08, todos com o
mesmo valor), inalterado — a tese estrutural (óleo dominando o valor do
crush) segue formalmente intacta. Como já observado em leituras
anteriores, o ISO mede quem captura mais valor dentro do crush, não se o
preço está caro ou barato frente a um nível técnico — hoje as duas
leituras (ISO no máximo, preço fazendo nova mínima de fechamento em várias
sessões, curva em backwardation) coexistem sem se contradizer
tecnicamente: o óleo pode dominar a margem de crush relativa e, ao mesmo
tempo, estar em tendência de queda de preço absoluto.

**Sem COT novo nesta janela** — o corte de 28/07/2026 segue sendo a
fotografia mais recente, mostrando os fundos com net long em óleo de
107.898 contratos (16,60% do open interest de 650.041), depois de uma
redução de -10,27% na semana anterior ao corte — a única das três pernas
em que o book especulativo já reduzia exposição comprada antes da queda
de preço das últimas sessões. Isso ajuda a explicar por que o óleo segue
mostrando o desenho técnico mais volátil e agora também o mais
estruturalmente diferente (backwardation) das três pernas.

### O que invalida / risco para o óleo

- **A curva futura voltar a contango** — se os vencimentos distantes
  (Z26, F27, H27) voltarem a valer mais que os próximos, a leitura de
  aperto de curto prazo perderia sustentação e a backwardation de hoje
  seria tratada como evento isolado.
- **O heating oil confirmar, com volume genuinamente normal (não apenas
  "menos anômalo"), um nível consistente com o de hoje** — validaria a
  melhora da margem de biodiesel como sinal real pela primeira vez em
  quatro sessões.
- **Quatro dias seguidos de heating oil com volume muito baixo (26, 48, 45
  contratos) se revelarem um problema de coleta de dados**, não um padrão
  real de mercado — nesse caso, toda a série recente de margem de
  biodiesel precisaria ser reavaliada.
- **Um fechamento consistente de volta acima de 68,55 (máxima de hoje)** —
  romperia a sequência de fechamentos fracos e abriria espaço para
  reteste do suporte de 72,00.
- **A isenção PIS/Cofins do biodiesel seguir sem renovação** — hoje é o 3º
  dia útil desde o vencimento (31/07), ainda sem confirmação (ver Lente
  fiscal).

### Leitura operacional — óleo

Para quem está vendido desde a quebra do suporte 72,00, o desenho de hoje
— fechamento no terço inferior do range, quinto pregão seguido abaixo do
nível, e agora uma curva futura em backwardation que sugere o mercado não
está esperando alívio de preço no curto prazo — reforça manter ou
adicionar posição vendida tática, com stop lógico acima de 68,55 (máxima
de hoje). A backwardation em si é um dado operacional relevante para quem
opera spreads de calendário no óleo: com o contrato mais próximo valendo
mais que os distantes, a estrutura favorece quem vende o spread
(vende Q26/U26, compra F27/H27) apostando que a inversão se normalize, ou
quem simplesmente prefere manter posição direcional no contrato mais
líquido/próximo em vez de rolar para vencimentos distantes que carregam
desconto. Para quem considera nova posição comprada, a recomendação segue
sendo a mesma das últimas sessões, reforçada: **não tratar a margem de
biodiesel calculada nas últimas quatro sessões como número definitivo até
o heating oil negociar com volume claramente normal**, e monitorar se a
backwardation se aprofunda ou dissolve nos próximos pregões antes de
assumir que reflete um aperto físico real.

---

## Spreads e crush (leitura de complexo)

**Ratio Far/Soj: 80,47% (05/08), queda de -0,49pp sobre ontem — o valor
mais próximo da zona <80% desta janela de 14 dias, e a primeira sessão em
que a compressão foi genuinamente liderada pelo farelo, não pela soja.**
Como discutido na seção Farelo, isso é qualitativamente diferente das duas
sessões anteriores, em que o "motor" do movimento era sempre a soja. Ainda
assim, um único pregão não é suficiente para declarar a tese do D+7/D+90
confirmada — a recomendação operacional é a mesma de sempre: exigir
confirmação por mais de uma sessão seguida na mesma direção e pelo mesmo
motivo antes de tratar como sinal robusto.

**Crush margin: 2,7043 USD/bu, -3,21% sobre ontem — reverteu a melhora de
ontem, mas segue folgada acima do nível de alerta (<2,50 USD/bu).** A
esmagadora perdeu um pouco de espaço de manobra hoje porque farelo e óleo
(receita) caíram mais rápido, em conjunto, do que a soja (custo, que ficou
praticamente parada) — o oposto exato da dinâmica de ontem.

**Oil share: 52,16%, praticamente idêntico a ontem (52,16%)** — mesmo com
o óleo caindo -0,67% e o farelo -0,64% hoje, a proporção do valor do crush
capturada pelo óleo não se moveu, sinal de que a queda de preço de hoje
afetou as duas pernas do crush de forma proporcionalmente parecida, sem
mudar a relação de valor entre elas.

**Oil-meal spread: 0,616 USD/bu, -1,06% no dia** — terceira sessão seguida
de oscilação modesta sem direção clara de médio prazo, consistente com um
movimento técnico de curto prazo em ambas as pernas, não uma mudança
estrutural na relação óleo-farelo.

**Heating oil: fechamento de 3,7805 (+1,23%) com volume de 45 contratos —
quarta sessão seguida com liquidez muito abaixo do normal.** Esta é a
mesma fricção documentada nas últimas três leituras, agora mais persistente
ainda: a leitura técnica das três pernas principais (soja, farelo, óleo —
todas com volume normal hoje) é sólida; a leitura fundamental que depende
do heating oil (margem de biodiesel) não é, porque o dado que a sustenta
segue com liquidez anômala há quatro pregões seguidos.

**ISF em 80/100, ISO em 100/100 — ambos inalterados pelo sétimo pregão
seguido.** Nenhum insumo estrutural novo (ABIOVE, condições de crush)
entrou no cálculo hoje.

**A curva futura do óleo virou backwardation enquanto soja e farelo seguem
em contango — a primeira divergência estrutural de curva nesta série de
leituras.** Isso é um dado novo que merece acompanhamento próprio nos
próximos dias: se persistir ou se aprofundar, é um sinal de que o mercado
de óleo está precificando dinâmicas de oferta/demanda (talvez ligadas a
palma asiática ou biodiesel americano/brasileiro) que ainda não aparecem
nas curvas de soja e farelo.

**O que os índices dizem juntos hoje:** o complexo teve, na sessão de
hoje, uma divergência interna clara entre a soja (calmaria técnica, sem
tese nova) e as outras duas pernas, que trouxeram cada uma um sinal
qualitativamente novo — o ratio comprimindo pelo motivo certo no farelo, e
a curva invertendo no óleo. As métricas estruturais (ISF, ISO, ABIOVE, oil
share) seguem, pelo sétimo pregão, inalteradas — elas capturam dinâmicas
de mais longo prazo que um dia de movimento técnico não altera. A leitura
mais honesta é que hoje foi o primeiro dia em várias sessões em que farelo
e óleo mostraram sinais tecnicamente mais "limpos" (motor correto no
ratio, estrutura de curva nova) do que a soja, que segue de lado
aguardando o próximo catalisador de notícia ou dado oficial.

---

## Lente fiscal e regulatória BR

**Isenção PIS/Cofins do biodiesel (`PISCOFINS-BIODIESEL-ISENCAO`,
`vigencia_ate` 2026-07-31) — hoje, 2026-08-05, é o 3º dia útil de
expediente público desde o vencimento.** O RSS de hoje trouxe apenas 3
itens mantidos (a menor seleção desta série), nenhum sobre este tema
específico — a lacuna de confirmação persiste. **Mecanismo e leitura, sem
mudança frente às últimas sessões:** se a isenção caducou sem renovação, o
custo de produção do biodiesel brasileiro sobe, reduzindo a
competitividade do biodiesel dentro do mix mandatório e pressionando a
demanda de óleo de soja como insumo doméstico — vetor bearish direto para
o óleo, e um candidato a explicar (parcialmente) por que a curva distante
do óleo está em desconto (backwardation) se o mercado já antecipa esse
custo mais alto para os meses seguintes. Com o monitor tributário
(`system/tributario_watch.toml`) parado desde 2026-06-05 (**61 dias sem
atualização**), esta leitura segue sem poder confirmar nem descartar a
caducidade — mantém-se como o item de verificação manual mais urgente
desta janela, agora há três dias úteis.

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L) —
vigência formal venceu há 25 dias** (`vigencia_ate` 11/07/2026), sem
qualquer atualização de status no monitor.

**MP 1.363/2026 — subsídio ao diesel fóssil (R$ 1,12/L), em vigor até
31/12/2026, sem alteração.** Bearish estrutural persistente: enquanto o
diesel fóssil segue subsidiado no mix B15, o biodiesel via óleo de soja
compete em desvantagem — reforçado se a isenção PIS/Cofins também tiver
caducado.

**B16 — sem data, travado em B15, sem mudança de status.** Cada +1pp de
mistura obrigatória de biodiesel puxaria demanda adicional de óleo de soja
para o mercado interno (~+436 mil toneladas no B16 pleno), mas o CNPE
segue sem nova convocação.

**STJ REsp 2.165.276/2026 — crédito PIS/Cofins para esmagadoras sobre soja
usada em biodiesel, sem alteração.** Bullish para soja/óleo (alívio de
custo de entrada), mas ainda não vinculante (não é decisão repetitiva).

**Vetores dos EUA e Indonésia, sem mudança de status desde 2026-06-05:**
EPA-RFS-2026-2027 (volumes recordes de biocombustível, sustentando o RIN D4
fixo em 2,11 USD/RIN usado na margem de biodiesel); 45Z-CLEAN-FUEL (regra
que favoreceria óleo de soja doméstico americano frente a insumo importado,
pendente de regra final do Treasury/IRS); DANANTARA-INDONÉSIA
(centralização estatal da exportação de palma, plena em 01/09/2026, agora
a 27 dias); INDONESIA-B50 (provável B45 em 2026, B50 pleno só 2027-28);
INDONESIA-LEVY-PMK9 (imposto de exportação de CPO até 12,5%, encarecendo
palma). Conjunto estruturalmente bullish para óleo de soja via substituição
de palma, mas inverificável pelo lado de mercado (MPOB inacessível, ver
Honestidade) — e potencialmente em tensão com a backwardation observada
hoje na curva do óleo, que sugere o mercado não está (ainda) precificando
esse suporte estrutural nos vencimentos mais distantes.

**O monitor tributário como um todo está há 61 dias sem qualquer
atualização** — prioridade de manutenção do sistema, especialmente
relevante agora que a isenção PIS/Cofins completa três dias úteis vencida
sem confirmação de status.

---

## Riscos e eventos próximos

**A ausência de manchete de compra chinesa hoje, pela primeira vez em
várias sessões, é em si um ponto de atenção** — monitorar se é uma pausa
temporária no fluxo de notícia ou o início de um período mais seco de
demanda declarada, o que mudaria o pano de fundo que sustentou grande
parte do debate recente sobre soja.

**A previsão da Datagro de alta de 1,5% na produção de soja 26/27** é um
driver de médio prazo a acompanhar — vale checar se outras consultorias
(StoneX, AgRural, Conab) convergem ou divergem dessa estimativa nas
próximas semanas, e se o WASDE (quando voltar a ser publicado) trouxer
um número comparável para a safra brasileira.

**O salto do físico de farelo no RS (R$ 1.640→1.800/ton, +9,76%) precisa
de confirmação** — um segundo pregão no mesmo patamar (ou próximo)
validaria a correção; um recuo de volta perto de 1.640 sugeriria anomalia
pontual de coleta.

**A curva futura do óleo em backwardation é um sinal novo a acompanhar
diariamente** — se se aprofundar (Q26 se distanciando ainda mais de H27),
reforça a leitura de aperto de curto prazo; se dissolver e voltar a
contango, indica que o desenho de hoje foi um evento de curto prazo, não
uma mudança estrutural de expectativa.

**O heating oil precisa negociar com volume claramente normal** — quatro
sessões seguidas de liquidez muito baixa (26, 48, 45 contratos) tornam a
margem de biodiesel não confirmável desde 2026-08-02/03.

**A isenção PIS/Cofins do biodiesel segue sem confirmação de status**,
agora no 3º dia útil desde o vencimento (31/07) — item de verificação
manual mais urgente desta janela.

**O ratio Far/Soj caiu para 80,47%, o mais próximo da zona <80% em várias
sessões, com o D+7 formal vencido há 48 dias** — monitorar se o movimento
de hoje é o início de uma compressão mais duradoura ou apenas um dia
isolado.

**O suporte técnico do óleo (72,00) segue rompido, agora a -5,92%** — a
reabertura de amanhã é o próximo teste, com atenção adicional à evolução
da backwardation da curva.

**O próximo corte do COT (referente a 04/08/2026) só é publicado por volta
de 07/08/2026** — até lá, sem novo dado de posicionamento para testar como
os fundos reagiram ao give-back de 04/08 e à consolidação de hoje.

**O USDA Crop Progress rotulado 2026-08-02 segue com os MESMOS valores do
corte de 26/07** (ver Honestidade), agora pela terceira leitura seguida; o
próximo corte, referente à semana de 09/08, deve sair na segunda-feira
seguinte (10/08).

**NOPA — fila `release-nopa-2026-08-05` sinaliza novo "release", mas o
dado segue inacessível**, agora mais de 8 semanas sem alternativa de dado
primário sobre o crush americano.

**MPOB — sem números de palma extraídos, mesma barreira de longa data.**

**O WASDE segue fora da janela deste briefing, agora 26 dias de atraso**
desde o último dado (10/07/2026).

---

## Honestidade

O que não foi possível validar neste briefing de 2026-08-05, e os pontos
onde a confiança é baixa:

**1. O salto do físico de farelo no Rio Grande do Sul (R$ 1.640,00/ton →
R$ 1.800,00/ton, +9,76%), depois de sete pregões seguidos sem qualquer
variação, é o dado mais incerto desta leitura.** Não há como distinguir,
com os dados deste briefing, entre uma correção real de mercado
represada e uma anomalia pontual de coleta (fonte Clicmercado via NAG).
Esta leitura usa o número como está reportado, mas recomenda explicitamente
aguardar confirmação por um segundo pregão antes de tratar R$ 1.800,00/ton
como o novo nível de referência do físico gaúcho.

**2. A curva futura do óleo em backwardation (Q26 67,86 → H27 67,04) é
tratada nesta leitura como um dado técnico observável e verificável (todos
os seis vencimentos vêm do mesmo dump de 2026-08-05), mas a interpretação
causal proposta — ligação com incerteza regulatória de biodiesel ou
expectativa de mais oferta de palma — é uma hipótese desta leitura, não um
fato confirmado por nenhuma fonte do briefing. Nenhum dado de palma (MPOB
bloqueado) ou de biodiesel BR (monitor tributário parado) permite
confirmar essa hipótese diretamente.

**3. O heating oil (HO=F) de 2026-08-05 fechou com 45 contratos de
volume — quarta sessão seguida de liquidez muito abaixo do que esta série
já qualificou como normal (26, 48, 45 contratos nas últimas três
sessões).** Esta leitura usa o número calculado de margem de biodiesel
(1,065 USD/galão, +4,36%) porque é o que o indicador interno gerou a
partir do dado disponível, mas reforça, pela quarta vez, que esse padrão é
candidato a problema de coleta de dados, não apenas ruído pontual —
recomenda-se verificação técnica da fonte.

**4. O ratio Far/Soj (80,47%) segue sem fechar abaixo de 80%, agora 48
dias depois do checkpoint formal do D+7 (18/06/2026).** Esta leitura não
conclui que a tese original se confirmou — apenas que o movimento de hoje
foi qualitativamente mais consistente com o mecanismo original (farelo
liderando) do que os das duas sessões anteriores, e mantém o D+90
(2026-09-09) como próximo marco formal.

**5. O USDA Crop Progress rotulado 2026-08-02 trouxe, pelo terceiro dump
seguido, valores idênticos ao corte de 26/07/2026 (11%/52%/7%).** Esta
leitura não trata isso como três semanas genuinamente estáveis de condição
de lavoura, e reforça a recomendação de reconferir no próximo corte
esperado (semana de 09/08, publicação em torno de 10/08) — a persistência
do mesmo valor por múltiplos dumps seguidos aumenta a suspeita de atraso
de atualização na fonte, não de estabilidade real.

**6. A isenção PIS/Cofins do biodiesel — sem confirmação de renovação ou
caducidade neste briefing, agora no 3º dia útil desde o vencimento.** O
monitor tributário está 61 dias sem atualização; esta leitura não presume
nenhum dos dois cenários.

**7. O prêmio de exportação PGUA de farelo e óleo não trouxe carimbo novo
em 2026-08-05** — o cálculo desta leitura que referencia esses números
parte do último carimbo disponível (2026-08-04), não de uma leitura do
mesmo dia, e é sinalizado como tal no corpo do texto. Diferente do físico
de exportação da soja (Paranaguá), que hoje teve, pela primeira vez em
várias sessões, um carimbo do mesmo dia da paridade — uma melhora pontual
de qualidade de dado que vale destacar.

**8. O WASDE permanece completamente fora da janela deste briefing** —
agora 26 dias de atraso desde o último dado (10/07/2026).

**9. NOPA (`release-nopa-2026-08-05`) segue com `monthly_status` em 0,0
bool** — mesma barreira de assinatura paga, mais de 8 semanas sem
alternativa de dado primário.

**10. Palma malaia (MPOB) segue sem números extraídos**, mesmo conteúdo
de 3.439 caracteres.

**11. O COT (CFTC) de 28/07/2026 segue sendo o dado de posicionamento mais
recente** — nenhum corte novo nesta janela; o próximo sai por volta de
07/08/2026. Percentis históricos de COT não foram calculados (mesma
limitação de leituras anteriores).

**12. Clima INMET (BR) não foi usado como driver de preço** — agosto é
entressafra da soja brasileira, sem relevância direta neste momento do
calendário agrícola, mesmo com risco de granizo sinalizado para Passo
Fundo/RS amanhã (06/08) e calor seco em Mato Grosso.

**13. A previsão da Datagro (safra 26/27, +1,5% de produção) veio apenas
como título de manchete no RSS, sem corpo de texto, metodologia ou
comparação-base explícita neste briefing.** Esta leitura trata o número
como um dado de manchete, com fonte e data, mas não tem como verificar a
base de comparação (safra 25/26 estimada por quem, em que nível) nem o
racional da consultoria.

**14. Os forecasts estatísticos internos (bandas 7d/30d geradas em
2026-08-05) não foram usados como driver desta leitura** — são bandas
MA20+volatilidade+slope, mecânicas (soja 7d "lateral"/30d "baixista",
farelo 7d "lateral"/30d "altista", óleo 7d "baixista"/30d "baixista"), sem
incorporar a leitura qualitativa de hoje (consolidação na soja, ratio
farelo-liderado, backwardation no óleo); ficam registradas no briefing,
mas esta leitura não as toma como fonte de tese.

*Nenhum número foi inventado ou estimado além do que consta no briefing de
2026-08-05 e nos insights anteriores referenciados. A contribuição central
desta leitura foi (1) identificar que a compressão do ratio Far/Soj de hoje
foi, pela primeira vez em três sessões, genuinamente originada pelo farelo,
não pela soja, e explicar o mecanismo dessa distinção; (2) identificar e
explicar a curva futura do óleo virando backwardation — o primeiro sinal
estrutural de curva divergente entre óleo e as outras duas pernas nesta
série de leituras; (3) sinalizar o salto físico de farelo no RS (+9,76%
após sete pregões congelados) como o dado físico mais relevante do dia,
com a devida ressalva sobre confirmação pendente; (4) separar a leitura
técnica confiável (fechamentos e volumes de soja/farelo/óleo, todos
normais) da leitura fundamental de baixa confiança (margem de biodiesel
calculada sobre heating oil com volume muito baixo pela quarta sessão
seguida); e (5) tratar os três itens da fila de julgamento de hoje —
`alerta-quebra_suporte-oleo_cbot-2026-08-05`,
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` e
`release-nopa-2026-08-05` — no contexto específico desta sessão, sem
inventar tonelagem, confirmação ou percentil que o briefing não trouxe.*
