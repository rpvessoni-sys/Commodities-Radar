---
data: 2026-07-13
titulo: "Primeira sessão real da semana: soja rompe para nova máxima intraday (1.208,75) mas fecha em candle de rejeição perto da mínima (1.197,25), óleo recupera 0,79% mas segue preso abaixo de 72,00 (71,02), farelo fecha a 3ª sessão consecutiva com o ratio Far/Soj acima de 80% (80,46%) confirmando o fechamento do checkpoint D+7 — mas câmbio, físico BR, básis Paranaguá e o Crop Progress do USDA, todos esperados para hoje, ainda não atualizaram"
tags: [complexo, auto-claude]
fontes:
  - CBOT CME (ZSQ26/ZMQ26/ZLQ26 + curva forward completa + HO=F) — sessão de 2026-07-13, primeira sessão nova desde 2026-07-10 (sexta-feira)
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, ISF/ISO, paridade BR) — recalculados com preço de 2026-07-13, câmbio ainda de 2026-07-10
  - BCB PTAX — último dado disponível 2026-07-10 (USD/BRL 5,1088), sem publicação nova até o fechamento deste briefing em 2026-07-13
  - CEPEA/ESALQ Paranaguá e Paraná interior via NAG — último dado disponível 2026-07-10, sem atualização
  - NAG Físico BR (farelo MT/IMEA, RS, Rondonópolis; prêmios export PGUA farelo/óleo) — último dado disponível 2026-07-10, sem atualização
  - CFTC COT Managed Money — dado de referência 2026-07-07, sem atualização (próxima publicação normal ~2026-07-17)
  - USDA Crop Progress — 2026-07-05, sem atualização (relatório semanal esperado hoje, 2026-07-13, ainda não presente no dump)
  - USDA WASDE — 2026-07-10 (cobre apenas farelo Argentina/Brasil/China parcial), fila `release-usda_wasde-2026-07-10`
  - NOPA — 2026-07-13, `monthly_status` inacessível, fila `release-nopa-2026-07-13`
  - ABIOVE projeções mensais — balanços ago-dez/2026 (farelo/óleo/soja), sem alteração
  - NOAA CPC ENSO — 2026-07-13 (El Niño Advisory, sem mudança)
  - MPOB — 2026-07-13 (parser sem números extraídos, streak de ~29 dias)
  - BCBA — 2026-07-13 (acessível, sem links de relatório detectados)
  - Notícias Agrícolas / Farm Progress RSS — 2026-07-13 (160 itens lidos, 5 mantidos; destaque "Soybean prices need poor weather, exports to China", farmprogress.com)
  - Forecasts estatísticos internos — 2026-07-13 (recalibrados com o novo spot)
  - system/tributario_watch.toml — MP-1358-2026 (`vigencia_ate` 2026-07-11, já vencida há 2 dias, status ainda "tramitacao", `atualizado_em` 2026-06-05), MP-1363-2026, PISCOFINS-BIODIESEL-ISENCAO (vence em 18 dias), STJ-RESP-2165276, B16-CNPE-2026 — todos `atualizado_em` 2026-06-05
  - Cruza com [[2026-07-12_leitura-complexo]], [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (checkpoint D+7, reafirmado hoje com dado novo), [[2026-05-26_subvencao-fossil-aperta-biodiesel]], [[2026-05-26_pis-cofins-biodiesel-explica-mercado-fisico-fraco]], [[2026-05-26_b16-bullish-farelo]], [[2026-05-26_curva-forward-cbot-oleo-desacopla]]
status: ativa
vies: [bull-soja, neutral-farelo, bear-oleo_soja]
---

## Visão geral

O complexo soja funciona como uma fábrica com uma única matéria-prima — a soja em
grão — e dois produtos de saída fabricados em proporção fixa a cada bushel esmagado: o
**farelo** (a fração proteica, ~78% da massa, vira ração animal) e o **óleo degomado**
(a fração de gordura, ~18-20% da massa, vira óleo de cozinha e biodiesel). Quem decide o
ritmo de esmagamento é a esmagadora, olhando a **crush margin** (o valor de farelo +
óleo produzidos por bushel, menos o custo daquele bushel de soja, medida na CBOT —
Chicago Board of Trade, a bolsa onde soja/farelo/óleo são negociados como futuros) e o
**oil share** (a fração desse valor capturada pelo óleo). Hoje, segunda-feira 13/07/2026,
é a **primeira sessão de fato nova desde sexta-feira 10/07** — depois de dois dias sem
pregão (sábado e domingo), os três preços do complexo se moveram de verdade: soja fechou
em 1.197,25 cts/bu (+0,46% sobre sexta), farelo em 321,10 USD/short_ton (+0,22%) e óleo
em 71,02 cts/lb (+0,79%) (CBOT, 13/07/2026). O detalhe importante está dentro da vela do
dia, não só no fechamento: a soja abriu em 1.200,50, subiu até uma nova máxima de
1.208,75 (o topo mais alto de toda a série recente) e devolveu quase todo o ganho
intradiário para fechar em 1.197,25, a poucos pontos da mínima do dia (1.194,00) — um
padrão técnico de **candle de rejeição** (abertura acima do fechamento, com pavio
superior longo), que costuma sinalizar hesitação compradora exatamente no momento em
que o preço testa uma extensão de alta. O rompimento da resistência de 1.180,00 segue
tecnicamente confirmado (fechamento ainda 1,46% acima dela), mas a mecânica da sessão
pede cautela: o mercado testou preço mais alto e foi vendido de volta.

No farelo, o **ratio Far/Soj** (preço do farelo dividido pelo preço da soja, na mesma
base — abaixo de 80% indica farelo "abundante" frente à soja, acima de 87% indica
"aperto", entre os dois é zona neutra) fechou hoje em 80,46% (indicadores, 13/07/2026),
a **terceira sessão consecutiva** acima de 80% (09/07: 80,85%; 10/07: 80,65%; 13/07:
80,46%) — o que consolida, com dado novo e genuíno (não um simples arrasto de fim de
semana), o fechamento do checkpoint D+7 da tese de 11/06/2026 que a leitura de ontem já
havia declarado editorialmente encerrado (tratando `revisao-2026-06-11_ratio-81-prepara-
janela-de-tranches-farelo-D+7`, ainda listada como VENCIDA na fila de hoje porque o
arquivo original de 11/06 não é editado por esta rotina). No óleo, o Índice de Suporte
do Óleo (ISO) segue em 100/100 (indicadores, 13/07/2026) e o preço recuperou 0,79% no
dia, mas continua abaixo do nível de resistência/suporte técnico de 72,00 (71,02 cts/lb,
tratando `alerta-quebra_suporte-oleo_cbot-2026-07-13`) — a curva forward permanece em
backwardation limpa (agosto 71,02 → janeiro/27 69,34, uma queda de -1,68 cts/lb ao longo
da curva), o argumento técnico mais consistente do complexo.

**O que mudou hoje de fato:** os três preços se moveram pela primeira vez desde
sexta-feira, e o resultado líquido é "sobe tudo, mas com qualidades diferentes" — soja
com sinal de exaustão técnica no topo, óleo recuperando terreno sem sair da zona
baixista, farelo consolidando (não revertendo) a saída da zona de "abundância". Ao mesmo
tempo, quatro fontes que deveriam ter atualizado numa segunda-feira útil continuam
travadas na sexta-feira ou antes: câmbio (PTAX), físico BR (NAG), básis de Paranaguá
(CEPEA) e o relatório semanal de Crop Progress do USDA, que a leitura de ontem apontava
como o "teste real" de hoje e que simplesmente não chegou ainda. **Leitura de uma
linha:** o pivô do complexo continua sendo a soja, mas a convicção no bull tático caiu de
moderada-alta para moderada — o rompimento de 1.180,00 segue de pé, porém a vela de hoje
é a primeira evidência técnica concreta de que o rali pode estar perdendo fôlego, e o
teste fundamental que confirmaria ou desmentiria isso (Crop Progress) ainda não
apareceu.

---

## Soja

**Viés: bull tático mantido, porém com a primeira evidência técnica de exaustão desde o
rompimento — soja fechou em 1.197,25 cts/bu (13/07/2026), 1,46% acima da resistência de
1.180,00, mas devolveu a maior parte do ganho intradiário depois de tocar uma nova
máxima de 1.208,75, fechando perto da mínima da sessão (1.194,00); trata
`alerta-quebra_resistencia-soja_cbot-2026-07-13`**

### O que sustenta a tese

**O nível técnico continua confirmado, mas a qualidade da sessão de hoje é pior do que a
de sexta.** O fechamento de 1.197,25 cts/bu (CBOT, 13/07/2026) fica 1,46% acima da
resistência de 1.180,00 e representa uma alta de +0,46% sobre o fechamento de sexta
(1.191,75, 10/07/2026) — no nível puro de preço, o rompimento segue de pé. Mas a
sessão abriu em 1.200,50, fez máxima de 1.208,75 (novo topo da série documentada desde
06/07) e caiu 11,50 cts (-0,95%) até fechar em 1.197,25, a apenas 3,25 cts acima da
mínima do dia (1.194,00). Esse padrão — abertura acima do fechamento, com um pavio
superior desproporcional ao corpo do candle — é o que analistas técnicos chamam de vela
de rejeição: o mercado testou um preço mais alto, encontrou vendedores suficientes para
devolver o ganho, e fechou perto do piso do dia. Isoladamente não inverte a tese (o
fechamento segue acima do nível-chave), mas é a primeira vela do tipo desde que o
rompimento começou a ser documentado em 06-07/07, e costuma preceder pausas ou
correções de curto prazo quando aparece logo após um movimento de alta esticado.

**A curva forward mudou de formato hoje**, com um detalhe técnico que merece registro: o
contrato de julho/26 (N26), presente na curva de soja em leituras anteriores (citado em
1.196,50 em 10/07/2026), **não aparece mais no dump de hoje** — sinal de que o contrato
mais próximo expirou/rolou, um evento normal de calendário (não um problema de
qualidade de dado, já que farelo e óleo, com vencimentos de contrato distintos,
mantêm sua estrutura). A curva atual (13/07/2026): Agosto/26 (Q26, spot) 1.197,25 →
Setembro/26 (U26) 1.186,00 (desconto de -11,25, -0,94%, o padrão sazonal normal de
pressão pré-colheita americana) → Novembro/26 (X26) 1.194,50 (recupera +8,50 sobre
setembro) → Janeiro/27 (F27) 1.208,25 (+13,75 sobre novembro) → Março/27 (H27) 1.210,25
(+2,00 sobre janeiro) — contango moderado na ponta longa, coerente com o formato já
documentado nas leituras anteriores, sem sinal de estresse de estoque físico imediato.

**O câmbio (PTAX) e a paridade em reais permanecem travados no dado de sexta-feira.** O
BCB não publicou PTAX novo até o fechamento deste briefing (última leitura,
5,1088 BRL/USD, 10/07/2026) — a paridade calculada hoje (R$ 134,84/saca 60kg,
indicadores, 13/07/2026) usa o preço novo da CBOT (1.197,25 cts) multiplicado pelo
câmbio antigo, então o número reflete só a variação de Chicago, não uma leitura completa
de paridade do dia. O mesmo vale para o básis físico em Paranaguá (CEPEA/ESALQ via NAG):
o último dado publicado continua sendo R$ 140,44/saca (10/07/2026), sem atualização
hoje — não é possível calcular o prêmio efetivo do porto sobre a paridade teórica de
hoje com dado limpo, porque um dos dois lados da conta (o físico) está parado há três
dias corridos.

**O posicionamento dos fundos (COT, CFTC) permanece no dado de referência 07/07/2026**
— managed money net long em +69.579 contratos (7,13% do open interest de 975.954), uma
alta de +82,4% frente à semana anterior (30/06), com swap dealers estruturalmente
comprados (net long de +115.704 contratos, 11,9% do OI) somando-se ao fluxo mais tático
do managed money — este quadro já foi detalhado a fundo na leitura de ontem
([[2026-07-12_leitura-complexo]]) e não tem atualização nova hoje; a próxima publicação
normal do COT sai sexta-feira, ~17/07/2026, e será o primeiro teste real de se essa
compra se manteve ao longo da semana de 13-17/07 — que é exatamente a semana em que a
vela de rejeição de hoje surgiu.

**A manchete de mercado mais relevante do dia (Notícias Agrícolas/Farm Progress RSS,
13/07/2026, 160 itens lidos, 5 mantidos) resume o risco embutido no rali: "Soybean
prices need poor weather, exports to China"** (farmprogress.com) — a leitura editorial
do próprio mercado americano é de que o nível atual de preço depende da continuidade de
dois catalisadores específicos (clima ruim nos EUA e retomada de compras chinesas), não
de um reequilíbrio estrutural de oferta e demanda. Isso é coerente com o WASDE (USDA
World Agricultural Supply and Demand Estimates) seguir sem cobertura de soja em grão
neste sistema (ver Honestidade) — o mercado está precificando uma narrativa de oferta
apertada que nenhuma fonte fundamental interna consegue confirmar ou refutar com número
direto.

**A condição de lavoura americana (USDA Crop Progress) permanece no dado de 05/07/2026**
(53% good + 11% excellent = 64% bom-ou-melhor, 6% poor) — **o relatório semanal que a
leitura de ontem apontava como o teste direto de hoje simplesmente não apareceu no
dump até o fechamento deste briefing.** Isso é uma lacuna material: a tese de "calor nos
EUA" citada nas manchetes dos últimos dias (ex.: "Soybeans rally on U.S. heat, China
sales", 06/07/2026) não pode ser confirmada nem refutada com dado fresco hoje, apesar de
ser justamente o dia em que o relatório deveria sair.

**Os forecasts estatísticos internos (13/07/2026)** reagiram ao novo preço com viés mais
altista: central 7d = 1.216,90 cts/bu (bandas 1.161,12-1.272,67), acima do central de
ontem (1.208,67); central 30d = 1.294,15 cts/bu (bandas 1.178,69-1.409,61), também acima
do de ontem (1.276,55). Vale notar que mesmo neste modelo com viés de alta, a banda
baixa de 7 dias (1.161,12) fica **abaixo** do nível de suporte técnico de 1.180,00 — ou
seja, o próprio modelo estatístico reconhece um cenário plausível de reversão total do
rompimento dentro do horizonte de uma semana, mesmo sem esse ser o cenário central.

### O que invalida / risco para a soja

- **Um fechamento amanhã (14/07) confirmando reversão abaixo de 1.180,00** transformaria
  a vela de rejeição de hoje em um sinal de topo confirmado, não apenas um alerta.
- **O Crop Progress atrasado, quando sair, mostrar melhora na condição de lavoura**
  (hoje em 64% bom-ou-melhor) removeria um dos pilares citados nas manchetes recentes
  para justificar o nível de preço.
- **O COT de sexta (~17/07) mostrar que o managed money vendeu na força** — a vela de
  rejeição de hoje é justamente o tipo de sessão que precede realização de lucro de
  fundos táticos.
- **A manchete "precisa de clima ruim e exportação pra China" se confirmar como
  consenso do mercado** — implica que o rali é condicional, não estrutural, e qualquer
  notícia de clima favorável ou desaceleração de compras chinesas tem potencial de
  reversão rápida.
- **PTAX e básis de Paranaguá seguirem sem atualizar** — sem eles, a leitura de paridade
  física BR permanece incompleta, limitando a confirmação do argumento de demanda física
  forte no porto que sustentou parte da tese nos últimos dias.

### Leitura operacional — soja

O viés tático de alta permanece tecnicamente válido — o fechamento ainda está acima de
1.180,00 —, mas a convicção cai de moderada-alta (leitura de ontem) para moderada: a
vela de rejeição de hoje é o primeiro sinal técnico concreto de hesitação desde o
rompimento, e chega justamente no dia em que o teste fundamental esperado (Crop
Progress) não se materializou. Para quem está comprado taticamente, faz sentido apertar
o stop de referência para perto de 1.194,00 (a mínima de hoje) em vez de manter o
antigo stop em 1.180,00 — um fechamento abaixo de 1.194,00 amanhã já seria um sinal de
alerta antes mesmo de testar o nível redondo. Para quem tem física para fixar, a
impossibilidade de calcular o básis de Paranaguá com dado fresco hoje (CEPEA parada há
três dias) recomenda esperar a atualização antes de tomar decisão de trava baseada
nesse indicador especificamente.

---

## Farelo

**Viés: neutro, com o checkpoint D+7 reafirmado por dado novo e genuíno — o ratio
Far/Soj fechou em 80,46% (13/07/2026), a terceira sessão consecutiva acima de 80%,
confirmando que o gatilho tático original (ratio sustentado <80%) segue sem se
confirmar, mesmo com a crush margin no maior nível da série; trata
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` e
`release-usda_wasde-2026-07-10`**

### O que sustenta a tese

**O ratio Far/Soj de hoje é o primeiro dado de dia útil desde o fechamento editorial do
checkpoint D+7 ontem, e reforça a conclusão.** Fechou em 80,46% (indicadores,
13/07/2026), calculado como farelo 321,10 USD/short_ton dividido pela soja 1.197,25
cts/bu (na mesma base) — a terceira sessão seguida acima de 80% (09/07: 80,85%; 10/07:
80,65%; 13/07: 80,46%), a mais longa sequência acima desse nível desde que a tese
original apostava justamente no oposto (ratio sustentado abaixo de 80%, sinalizando
farelo "abundante" frente à soja). A trajetória de queda suave dentro da própria zona
acima de 80% (80,85 → 80,65 → 80,46) sugere uma aproximação gradual de volta à fronteira
de 80%, mas ainda sem cruzá-la — o veredito do checkpoint (gatilho tático não
confirmado) permanece de pé com esta terceira confirmação.

**A crush margin (o valor de farelo + óleo produzido por bushel de soja esmagada, menos
o custo da soja, medido pela CBOT) fechou hoje em 2,9039 USD/bushel** (indicadores,
13/07/2026: farelo 321,10 + óleo 71,02 − soja 1.197,25), **o nível mais alto de toda a
série documentada nas últimas leituras** — 0,76% acima do fechamento de sexta (2,8819).
O mecanismo é direto: quanto maior a crush margin, maior o incentivo econômico da
esmagadora para processar soja a pleno vapor, porque cada bushel esmagado gera mais
valor combinado de farelo e óleo do que custou a soja em si. Uma crush margin em máxima
da série significa que a oferta física de farelo (subproduto do esmagamento) tende a
continuar generosa — o mecanismo estrutural por trás da tese ABIOVE (ver abaixo) —
mesmo que o preço relativo do farelo (o ratio) não esteja, no momento, em zona de
"abundância" segundo o critério técnico específico do checkpoint fechado ontem.

**A trajetória projetada da ABIOVE (Associação Brasileira das Indústrias de Óleos
Vegetais, projeções mensais, sem alteração frente à leitura anterior) continua sendo o
pilar mais sólido do argumento estrutural de médio prazo**, porque não depende do
ratio do dia nem de nenhum contrato CBOT. A exportação de farelo brasileiro projetada
cai de 1.400 mil toneladas em agosto/2026 para 700 mil toneladas em dezembro/2026 — uma
queda de exatamente 50% em quatro meses (ABIOVE, projeções mensais) — enquanto o estoque
final projetado não acompanha essa queda na mesma proporção, oscilando entre 1.000 e
1.224 mil toneladas ao longo de todo o período (1.224,23 em ago → 1.016,32 em set →
1.100,13 em out → 1.101,43 em nov → 1.015,52 em dez). O mecanismo de transmissão para o
preço doméstico é direto: se menos farelo sai pelo porto mas a produção continua
praticamente constante (2.285,06 → 2.128,55 → 2.142,97 → 1.977,59 → 1.659,04 mil
toneladas, uma queda suave, não um corte abrupto), o volume que deixa de ser exportado
precisa ser absorvido pelo mercado interno de ração — pressionando o preço doméstico ao
longo do segundo semestre. Esse mecanismo estrutural é o que sobrevive ao fechamento do
checkpoint tático, e seus próprios pontos de verificação (D+90 em 09/09/2026, D+180 em
08/12/2026) ainda estão vivos.

**Tratando `release-usda_wasde-2026-07-10` (ainda listado como não-interpretado na fila
de hoje, apesar de já ter sido detalhado na leitura de ontem):** os números de farelo do
WASDE (World Agricultural Supply and Demand Estimates, USDA) seguem congelados frente à
geração de junho — Brasil: produção 8,00 milhões de toneladas (mi t), exportação 0,19 mi
t, esmagamento doméstico 7,10 mi t (2026/2027, edição de julho, idêntico à de junho);
Argentina: produção 33,11 mi t, exportação 2,91 mi t, esmagamento doméstico 3,65 mi t
(idêntico). Não há revisão de alta nem de baixa nesta publicação para o balanço de
farelo — uma fonte estatisticamente "muda" neste recorte específico, o que reforça (por
ausência de contradição) o cenário ABIOVE descrito acima, mas não adiciona confirmação
direta nova.

**As praças físicas de farelo no Brasil (NAG) permanecem no último dado de sexta-feira**
(Mato Grosso/IMEA R$ 1.577,34/ton, Rondonópolis R$ 1.620,00/ton, RS R$ 1.640,00/ton,
10/07/2026) — sem atualização hoje, segunda-feira, o que normalmente deveria trazer
novo dado. O prêmio de exportação em Paranaguá segue em +0,05 USD/short_ton (julho/26,
NAG, 10/07/2026, inalterado há semanas) — o Brasil continua sem vantagem de preço para
exportar farelo, reforçando o mecanismo de absorção doméstica da tese ABIOVE, mas sem
nenhum dado físico novo para confirmar isso no dia de hoje especificamente.

**O forecast estatístico do farelo (13/07/2026)** subiu junto com o preço: central 7d =
325,30 USD/sht (bandas 311,88-338,72), acima do central de ontem (323,59); central 30d =
342,52 USD/sht (bandas 314,73-370,30), também acima (337,54 ontem). O modelo segue
divergindo da tese fundamentalista ABIOVE (o modelo reage ao preço recente, que subiu;
a ABIOVE aponta pressão estrutural baixista para o segundo semestre) — a mesma
contradição entre curto e médio prazo documentada na leitura de ontem, sem
reconciliação nova hoje.

### O que invalida / risco para o farelo

- **A tese estrutural ABIOVE deixar de se confirmar no físico ao longo do 2S/26** —
  continua sendo a invalidação mais relevante do único pilar que sobrevive ao
  fechamento do checkpoint tático.
- **O ratio Far/Soj continuar a trajetória de queda gradual (80,85 → 80,65 → 80,46) e
  cruzar novamente para baixo de 80% por 2-3 pregões** — reabriria um novo ciclo de
  teste tático, desta vez partindo de um nível já mais próximo da fronteira.
- **NOPA seguir inacessível indefinidamente** (ver abaixo) — sem confirmação direta do
  esmagamento americano, o checkpoint D+90 (09/09) corre o mesmo risco que o D+7 correu.
- **NAG físico BR seguir sem atualizar por mais dias úteis** — sem dado fresco de praça,
  a leitura de mercado físico doméstico fica cada vez mais defasada frente ao preço CBOT.

### Leitura operacional — farelo

Sem mudança frente à recomendação de ontem: para quem tinha posição vendida tática
ancorada estritamente no ratio <80%, a indicação permanece reduzir ou zerar essa perna —
o dado de hoje é a terceira confirmação consecutiva de que esse gatilho específico não
se sustentou. Para quem quer manter exposição à tese estrutural ABIOVE, o veículo mais
robusto continua sendo um spread de convergência (farelo/soja ou o crush completo) em
vez de posição direcional pura vendida, evitando ficar exposto a reversões técnicas de
curto prazo como a documentada nas últimas sessões. Vale monitorar de perto se o ratio
completa a aproximação gradual de volta a 80% nos próximos 2-3 pregões — se cruzar para
baixo de forma sustentada, reabre a tese tática original a partir de um novo ponto de
entrada.

---

## Óleo

**Viés: bear tático mantido, mas com sinal de recuperação parcial no dia — óleo fechou
em 71,02 cts/lb (13/07/2026), ainda abaixo do suporte de 72,00, mas subiu 0,79% sobre
sexta-feira, com a curva forward em backwardation e a margem de biodiesel comprimindo
pelo lado do custo; trata `alerta-quebra_suporte-oleo_cbot-2026-07-13`**

### O que sustenta a tese

**O óleo segue tecnicamente abaixo do suporte de 72,00, mas a distância diminuiu.**
Fechou em 71,02 cts/lb (CBOT, 13/07/2026), uma distância de -1,36% do nível de 72,00 —
menor que a distância de -2,14% documentada na sexta-feira (70,46 cts/lb). A sessão
abriu em 71,09, fez máxima de 71,49 e mínima de 70,86, um range estreito (0,63 cts) que
contrasta com o range bem mais largo da soja no mesmo dia — o óleo teve uma sessão de
recuperação modesta e contida, não uma reversão de tendência.

**A curva forward do óleo (13/07/2026) mantém backwardation limpa e coerente com as
leituras anteriores**: Agosto/26 (Q26, spot) 71,02 → Setembro/26 (U26) 70,50 (-0,52) →
Outubro/26 (V26) 69,89 (-0,61) → Dezembro/26 (Z26) 69,50 (-0,39) → Janeiro/27 (F27) 69,34
(-0,16) — uma queda de -1,68 cts/lb (-2,4%) de agosto a janeiro/27. Esse formato de curva
(preço mais alto no vencimento mais próximo, caindo nos vencimentos mais distantes) é o
argumento técnico mais robusto e mais estável de toda a leitura, porque reflete
diretamente a força da demanda física presente (biodiesel americano + exportação
brasileira) frente a uma expectativa de oferta mais confortável mais adiante — e não
depende de nenhuma ambiguidade de dado, já que a curva do óleo está limpa há semanas
(ver também [[2026-05-26_curva-forward-cbot-oleo-desacopla]]).

**A margem de biodiesel americano caiu para 0,6071 USD/galão** (indicadores, 13/07/2026:
receita 6,7336 = HO/heating oil (combustível equivalente ao diesel, usado como proxy de
receita) 3,57 + 1,5×RIN (Renewable Identification Number, o crédito regulatório do
programa RFS/EPA que subsidia biocombustível) 2,11; custo 6,1265 = óleo 5,3265 +
industrial 0,80) — uma queda de 4,2% frente à sexta-feira (0,6338), ainda dentro da
faixa de conforto de 0,50-0,80 USD/gal, mas comprimindo. O mecanismo por trás da queda é
importante: a receita subiu ligeiramente (6,7183 → 6,7336, +0,23%, puxada pelo próprio
heating oil que fechou em 3,57 hoje ante 3,55 na sexta), mas o custo subiu mais rápido
(5,2845 → 5,3265, +0,79%) porque o próprio óleo de soja (insumo do biodiesel) encareceu
no dia — ou seja, a compressão da margem hoje foi causada pelo lado do custo (o óleo
subindo), não por fraqueza do lado da receita. Isso é uma leitura sutil mas relevante:
o óleo mais caro é bom para quem vende óleo físico, mas espreme a rentabilidade de quem
o transforma em biodiesel, criando uma tensão interna dentro do próprio mecanismo que
sustenta a demanda industrial do produto.

**O Índice de Suporte do Óleo (ISO) permanece em 100/100 (5/5 condições)** (indicadores,
13/07/2026) — o mesmo patamar máximo documentado desde 01/07/2026, agora superando duas
semanas consecutivas sem qualquer sinal de enfraquecimento, apesar da compressão pontual
da margem de biodiesel hoje.

**O posicionamento dos fundos (COT, 07/07/2026)** permanece no dado de referência já
detalhado ontem — net long +84.919 contratos (13,22% do OI de 642.514), uma queda de
-7,6% frente à semana anterior, ainda a posição mais assimétrica das três pernas do
complexo, mas mostrando redução (não aumento) da aposta comprada na margem. Sem
atualização nova hoje; a próxima publicação (~17/07) é o teste real de se esse
de-risking continuou.

**O pano de fundo regulatório global permanece inalterado desde 05/06/2026**
(`system/tributario_watch.toml`, agora 39 dias sem atualização): EPA Final RFS
2026/2027 sustenta o RIN D4, o crédito 45Z tende a favorecer óleo doméstico americano, a
Indonésia mantém a exportação de palma centralizada via Danantara mais o levy de até
12,5% sobre CPO (crude palm oil) — mas o **MPOB (Malaysian Palm Oil Board) segue
inacessível**, com o parser retornando apenas ~3.439 caracteres de HTML sem números
extraídos (13/07/2026), agora no que parece ser o 29º dia consecutivo dessa barreira.

**O forecast estatístico do óleo (13/07/2026)** subiu ligeiramente mas mantém o viés
baixista: central 7d = 70,06 cts/lb (bandas 65,80-74,31), acima do central de ontem
(69,07) mas ainda abaixo do spot de hoje (71,02) — o modelo, mesmo reagindo à alta do
dia, projeta que parte do ganho de hoje será devolvida na próxima semana. Central 30d =
67,27 cts/lb (bandas 58,46-76,09), também acima do de ontem (64,72) mas seguindo abaixo
do spot. A curva forward (backwardation) e o modelo estatístico continuam apontando na
mesma direção — o caso mais consistente de todo o complexo.

### O que invalida / risco para o óleo

- **Um fechamento acima de 71,49 (máxima de hoje) ou perto de 72,00** reabriria o teste
  da resistência/suporte técnico, especialmente se acompanhado de recuperação da margem
  de biodiesel.
- **A margem de biodiesel (0,6071 USD/gal) continuar caindo em direção a ~0,50 USD/gal**
  (piso da faixa de conforto) reduziria progressivamente o incentivo doméstico americano
  ao óleo — a compressão de hoje já é o segundo dia seguido de queda na margem.
- **RIN D4 real acima ou abaixo do parâmetro fixo usado no modelo (2,11 USD/RIN)** —
  incerteza estrutural bidirecional, sem novo dado hoje.
- **MPOB seguir inacessível** — impossível avaliar o efeito de El Niño ou das
  restrições indonésias sobre o prêmio de substituição.
- **O COT da próxima sexta (~17/07) mostrar aceleração (não desaceleração) do
  de-risking** — reforçaria o bear tático; uma reversão para compra, ao contrário,
  contradiria a tese.

### Leitura operacional — óleo

Viés bear tático mantido, com a curva forward em backwardation como argumento técnico
mais robusto para manter exposição vendida de médio prazo via carry (ganho decorrente
da estrutura de preços decrescente ao longo dos vencimentos, não da direção do preço
à vista). A recuperação de hoje (+0,79%) e o menor range da sessão sugerem que o ritmo
de queda desacelerou, então a referência de stop para quem está posicionado vendido
sobe ligeiramente para 71,50-72,00 cts/lb (ante 71,00-72,00 na leitura anterior). Para
quem opera o oil share dentro do crush (52,51%, indicadores, 13/07/2026, estável frente
aos 52,37% de sexta), o viés estrutural segue favorecendo manter exposição relativa ao
óleo frente ao farelo — ISO em 100/100 e margem de biodiesel ainda positiva —, mas a
compressão da margem pelo lado do custo (óleo mais caro pressionando a rentabilidade do
biodiesel) é um sinal de que essa folga está encolhendo, e pede cautela para quem
quiser aumentar a exposição relativa a partir daqui.

---

## Spreads e crush — leitura de complexo

### Crush margin: 2,9039 USD/bu — novo máximo da série, sustenta o ritmo de esmagamento

A crush subiu para 2,9039 USD/bu (13/07/2026), o valor mais alto da série documentada
desde 06/07 (2,4974 → 2,5638 → 2,7316 → 2,8965 → 2,8819 → 2,9039), uma alta acumulada de
+16,3% na semana que passou mais o dia de hoje. Isso reforça, com um novo dado
independente, o incentivo de esmagamento a pleno vapor que alimenta diretamente o
mecanismo estrutural ABIOVE descrito na seção Farelo — quanto mais vale a pena esmagar,
mais farelo e óleo entram no mercado como subprodutos, ainda que o preço relativo de
cada um responda a dinâmicas distintas (farelo pressionado pelo excesso de oferta
doméstica projetada, óleo sustentado pela demanda de biodiesel).

### Ratio Far/Soj: 80,46% — terceira sessão consecutiva acima de 80%, checkpoint D+7 reafirmado

Como detalhado na seção de Farelo, o dado de hoje é a confirmação mais forte até agora
de que o gatilho tático da tese de 11/06/2026 não se sustentou: três sessões seguidas
(09, 10 e 13/07) fecharam acima de 80%, com uma trajetória de queda suave dentro dessa
faixa (80,85 → 80,65 → 80,46) que aproxima gradualmente o ratio da fronteira de 80% sem
cruzá-la. Trata novamente
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`.

### Oil share: 52,51% — estável, leve alta

Subiu ligeiramente de 52,37% (10/07) para 52,51% (13/07/2026) — dentro da faixa recente
de vaivém em torno de 52-53%, sem trajetória monotônica clara.

### Oil-meal spread: 0,748 USD/bu — alta de +6,6% no dia

Subiu de 0,7018 (10/07) para 0,748 USD/bu (13/07/2026) — o spread mede o valor do óleo
menos o valor do farelo por bushel, e a alta de hoje reflete o óleo subindo mais rápido
proporcionalmente (+0,79%) do que o farelo (+0,22%) na sessão, mesmo com o óleo em
patamar de preço absoluto mais baixo (bear tático) e o farelo em zona neutra.

### ISF em 80/100, ISO em 100/100 — patamar sustentado, agora superando duas semanas

O Índice de Sobra de Farelo (ISF) permanece em 80/100 (4/5 condições) e o Índice de
Suporte do Óleo (ISO) em 100/100 (5/5) (indicadores, 13/07/2026) — o mesmo patamar
documentado desde 01/07/2026, agora 13 dias consecutivos sem mudança de nível. Vale
notar a tensão entre esse índice composto (ISF ainda sinalizando pressão baixista no
farelo) e o ratio Far/Soj (que já saiu da zona de "abundância" há três sessões): são
métricas diferentes — o ISF é um índice de condições estruturais (produção, estoque,
exportação, calendário), enquanto o ratio é puramente um preço relativo do dia — e a
divergência entre os dois é exatamente o que caracteriza o momento atual do farelo:
estruturalmente ainda pressionado (ISF), mas taticamente não mais "barato" frente à
soja (ratio).

### O que os índices e o COT dizem juntos em 13/07/2026

ISF 80/100 + ISO 100/100 (ambos estáveis há 13 dias) + ratio Far/Soj em queda suave mas
ainda acima de 80% (terceira sessão, checkpoint tático fechado) + oil share em leve alta
(52,51%) + crush margin em máximo da série (+16,3% acumulado) + COT ainda no dado de
07/07 (sem atualização) formam um quadro coeso: **o complexo segue esmagando a pleno
vapor (crush em máxima), com o óleo capturando a maior fatia marginal do valor
adicional gerado hoje (oil-meal spread subindo) mesmo enquanto o preço absoluto do óleo
permanece abaixo do suporte técnico.** A leitura de hoje é a primeira com dado de preço
genuinamente novo desde sexta — e o resultado líquido é que nenhum dos três vieses
táticos (bull-soja, neutro-farelo, bear-óleo) mudou de direção, mas a intensidade de
cada um se moveu: soja perdeu convicção (vela de rejeição), farelo ganhou uma terceira
confirmação do fechamento do checkpoint, e óleo recuperou um pouco de terreno sem sair
da zona bear.

---

## Lente fiscal e regulatória BR

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L) — o
`vigencia_ate` era 11/07/2026, agora há 2 dias, e o monitor tributário segue sem
qualquer atualização de status** (`system/tributario_watch.toml`, evento MP-1358-2026,
`atualizado_em` 2026-06-05, status ainda "tramitacao", `proximo_marco` = "Deliberação
comissão mista", `proximo_data` = 2026-07-11, já vencida). Hoje é a primeira
segunda-feira útil desde o vencimento formal da MP, e é justamente o tipo de dia em que
o Congresso poderia se manifestar (diferente do fim de semana, quando não há sessão) —
mas nenhuma fonte pública rastreada pelo sistema (ABIOVE, NAG, notícias) confirma se a
MP caducou, foi prorrogada por novo decreto, ou foi convertida em lei. A MP ressarce
PIS/Cofins/Cide da gasolina e do diesel, mantendo o combustível fóssil artificialmente
mais barato — o mesmo espírito da MP 1.363/2026 (subsídio de R$ 1,12/L ao diesel,
vigente até 31/12/2026, já tratada em
[[2026-05-26_subvencao-fossil-aperta-biodiesel]]). O mecanismo de transmissão para o
complexo soja é indireto mas real: enquanto o combustível fóssil segue subsidiado, a
competitividade relativa do biodiesel dentro do mix B15 mandatório permanece
pressionada, mantendo a margem da indústria de biodiesel (maior consumidora industrial
de óleo de soja no Brasil) mais apertada do que teria sem a subvenção ao concorrente
fóssil — um mecanismo que ecoa a compressão de margem documentada hoje na seção Óleo,
ainda que por um canal distinto (custo do insumo, não subsídio ao concorrente). **Se a
MP de fato caducou sem conversão em lei, seria um sinal (fraco, mas real) de perda de
fôlego político do pacote pró-fóssil, levemente positivo para a competitividade do
biodiesel; se foi convertida ou prorrogada, reforça o quadro de pressão já documentado
desde maio.** Esta é a terceira leitura seguida (11/07, 12/07 e hoje) que registra essa
lacuna sem conseguir fechá-la — o fato de hoje ser dia útil e ainda assim não haver
atualização é, em si, um dado (fraco) de que o desfecho não está sendo tratado com
urgência pelo Congresso ou pelo Executivo.

**Isenção PIS/Cofins biodiesel — vencimento em 31/07/2026, agora a 18 dias.** Sem
sinalização pública de renovação até hoje (evento PISCOFINS-BIODIESEL-ISENCAO,
`atualizado_em` 2026-06-05, sem mudança). O checkpoint D+45 do insight relacionado
([[2026-05-26_pis-cofins-biodiesel-explica-mercado-fisico-fraco]]) já venceu sem
resposta, como registrado nas leituras anteriores. Com 18 dias até o vencimento formal,
este segue sendo o próximo relógio fiscal mais próximo a vigiar depois da MP 1.358.

**B16 — sem data, travado em B15.** Sem mudança de status (evento B16-CNPE-2026,
`atualizado_em` 2026-06-05, status "adiado", sem `proximo_data`).

**MP 1.363/2026 (subsídio ao diesel fóssil) — em vigor até 31/12/2026.** Sem alteração.
Bearish estrutural persistente para a demanda incremental de óleo de soja no mercado
doméstico brasileiro.

**STJ REsp 2.165.276/2026 — crédito PIS/Cofins para esmagadoras.** Sem alteração.
Bullish para a soja/óleo (alívio de custo de entrada para biodiesel) e, por extensão,
incentivo a mais esmagamento — coerente com o crush margin em máximo da série
documentado hoje.

**Câmbio (PTAX) e físico BR (NAG/CEPEA) seguem travados na sexta-feira (10/07/2026),
sem publicação nesta segunda-feira útil** — detalhado nas seções de Soja e Honestidade;
é o vetor de dado mais atrasado da leitura de hoje, porque não há razão de calendário
(feriado, fim de semana) para a ausência.

---

## Riscos e eventos próximos

**USDA Crop Progress — relatório semanal esperado hoje (13/07/2026) ainda não
apareceu no dump.** É o item mais urgente a verificar na próxima atualização do
sistema, já que a leitura de ontem apontava justamente para hoje como o teste direto da
narrativa de "calor nos EUA" citada nas manchetes recentes.

**Confirmação de PTAX, NAG físico BR e básis de Paranaguá (CEPEA) para 13/07/2026** —
nenhum dos três atualizou até o fechamento deste briefing, apesar de hoje ser dia útil
normal; monitorar a próxima geração do dump.

**Desfecho da MP 1.358/2026 — vigência formal encerrada há 2 dias (11/07), sem
confirmação.** Hoje foi o primeiro dia útil desde o vencimento; monitorar deliberação
da comissão mista e qualquer decreto de prorrogação nos próximos dias.

**Isenção PIS/Cofins biodiesel — vencimento 31/07/2026 (18 dias).** Sem sinalização de
renovação até agora.

**Próxima atualização do COT (~17/07/2026, sexta-feira)** — teste de se a rotação de
fundos documentada em 07/07 (comprando soja e farelo, reduzindo óleo) continuou ao
longo da semana de 13-17/07, que é também a semana em que surgiu a vela de rejeição de
hoje na soja.

**NOPA — segue inacessível** (fila `release-nopa-2026-07-13` tratada aqui, sem dado
interpretável), sem crush americano confirmado por fonte primária.

**MPOB — sem números de palma extraídos**, mantendo cego o efeito da Indonésia e do El
Niño sobre o prêmio de substituição do óleo de soja.

**Checkpoints futuros da tese estrutural do farelo (ABIOVE)** — D+90 em 09/09/2026 e
D+180 em 08/12/2026 (insight [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]),
agora reforçados por três sessões consecutivas (09, 10, 13/07) confirmando que o
checkpoint tático de curto prazo (D+7) não se sustentou.

**Confirmação técnica da soja amanhã (14/07)** — se a vela de rejeição de hoje for
seguida por um segundo dia de queda, o sinal de exaustão técnica ganha força; se a soja
recuperar e fizer nova máxima limpa, a vela de hoje foi apenas ruído dentro da
tendência de alta.

---

## Honestidade

O que não foi possível validar neste briefing de 13/07/2026, onde a confiança é baixa ou
há lacunas materiais:

**1. O USDA Crop Progress esperado para hoje não apareceu no dump.** A leitura de ontem
apontava explicitamente 13/07/2026 como a data do próximo relatório semanal — o dado
mais recente disponível continua sendo 05/07/2026 (64% bom-ou-melhor). Não há como
confirmar se a condição de lavoura americana melhorou, piorou ou ficou estável na
semana mais recente, apesar de ser exatamente o tipo de informação que validaria ou
invalidaria as manchetes recentes sobre "calor nos EUA".

**2. PTAX, NAG físico BR e CEPEA/Paranaguá não atualizaram nesta segunda-feira útil.**
Ao contrário do fim de semana (onde a ausência de dado é esperada por não haver
publicação), hoje é dia útil normal e essas três fontes deveriam ter novo dado. A
paridade BR calculada hoje (R$ 134,84/saca) mistura preço novo de CBOT com câmbio
antigo de sexta-feira, e não é possível calcular o básis físico de Paranaguá com dado
fresco em nenhum dos dois lados da conta.

**3. O fechamento do checkpoint D+7 da tese de 11/06/2026 continua sendo uma decisão
editorial desta rotina, não um mecanismo automático do sistema** — a fila voltou a
listar o mesmo item como VENCIDA hoje, mesmo após o fechamento explícito na leitura de
ontem, porque o arquivo original de 11/06 não foi editado (esta rotina escreve apenas
em `insights/`, sem tocar em insights antigos). O dado de hoje (terceira sessão acima de
80%) reforça a conclusão já registrada, mas o mecanismo de "fechar" formalmente um
checkpoint no sistema segue sendo apenas textual/editorial.

**4. O WASDE (fila `release-usda_wasde-2026-07-10`) segue cobrindo apenas farelo
(Argentina, Brasil, e duas linhas truncadas de China)** — sem nenhum dado de soja em
grão ou óleo de soja, em qualquer geografia, e sem nenhum dado dos Estados Unidos. A
pergunta central sobre "oferta grande de soja", relevante justamente para avaliar a
manchete de hoje ("precisa de clima ruim e exportação pra China"), segue sem canal de
resposta interno.

**5. NOPA (fila `release-nopa-2026-07-13`) segue com `monthly_status` em 0,0 bool** —
mesma barreira de assinatura paga documentada desde meados de junho, agora com quase um
mês sem alternativa de dado primário sobre o esmagamento americano.

**6. Percentis históricos de COT não calculados** — os números de 07/07/2026 (sem
atualização há uma semana) são lidos apenas em nível absoluto e como fração do open
interest corrente, sem série histórica completa para calibrar se estão em zona extrema
frente ao próprio histórico de cada contrato.

**7. Palma malaia (MPOB) segue sem números extraídos** (13/07/2026, mesmo texto de HTML
~3.439 caracteres sem valores, aproximando-se de um mês consecutivo) — impossível
avaliar o efeito de El Niño ou das restrições indonésias sobre o prêmio de substituição
do óleo de soja.

**8. A leitura da vela de rejeição da soja é uma interpretação técnica desta rotina, não
um cálculo automático do sistema** — o fato objetivo (abertura 1.200,50, máxima 1.208,75,
mínima 1.194,00, fechamento 1.197,25) está no dump; a classificação como "candle de
rejeição" e a inferência de hesitação compradora são leitura qualitativa baseada em
análise técnica padrão, não um indicador calculado internamente.

**9. Volume da sessão de hoje (6.813 contratos no ticker ZSQ26, CBOT, 13/07/2026) não
foi comparado com uma base equivalente de sexta-feira** — o dump não traz o volume do
mesmo ticker específico para 10/07 nesta geração, então não é possível afirmar com
número se o volume de hoje foi maior ou menor que o da sessão anterior, apenas registrar
o valor absoluto.

**10. BCBA Argentina — sem relatórios de esmagamento/exportação acessíveis via
scraper** (page_fetched=1,0 mas sem links de relatório, 13/07/2026, sem mudança desde
27/06/2026, colheita mantida em 98% concluída e 50,1 milhões de toneladas).

**11. RIN D4 como parâmetro fixo (2,11 USD/RIN) segue sendo uma fonte relevante de
incerteza do modelo de biodiesel**, sem novo dado hoje.

**12. Dados de clima INMET (BR) não foram usados como driver desta leitura.** Julho é
entressafra da soja brasileira (colheita já concluída, plantio só em outubro) —
monitoramento de rotina, sem relevância direta para a tese de preço neste momento do
calendário agrícola.

*Nenhum número foi inventado ou estimado além do que consta no briefing de 13/07/2026 e
nos insights anteriores referenciados. A contribuição central desta leitura foi
reconhecer a primeira sessão de preço genuinamente nova da semana, identificar o padrão
técnico de rejeição na soja (que reduz, mas não zera, a convicção do bull tático),
confirmar com um terceiro dado consecutivo o fechamento do checkpoint D+7 do farelo, e
registrar que quatro fontes que deveriam ter atualizado num dia útil normal (Crop
Progress, PTAX, NAG físico, CEPEA/Paranaguá) permaneceram travadas — uma lacuna mais
grave do que a do fim de semana, porque não tem justificativa de calendário.*
