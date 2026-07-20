---
data: 2026-07-20
titulo: "Primeira sessão de pregão genuinamente nova desde sexta-feira: soja reabre com salto de +1,70% e estende o rompimento de 1.180,00 para +2,86%, mas o próprio tamanho desse movimento comprime a crush margin em -4,5% e aprofunda o ratio Far/Soj para 79,27% — confirmação tática da soja e do farelo chega no mesmo dado, enquanto o óleo tem o primeiro dia de fechamento abaixo da abertura desde o rali de sexta"
tags: [complexo, auto-claude]
fontes:
  - CBOT CME (ZSU26 soja / ZMU26 farelo / ZLU26 óleo + curva forward completa Q26-H27) — sessão de 2026-07-20 (segunda-feira, primeira sessão de pregão genuinamente nova e independente desde o fechamento de sexta-feira 17/07, com o fim de semana de 18-19/07 sem negociação do complexo agrícola)
  - CME heating_oil_cbot (HO=F) — fechamento de 2026-07-20 (3,999 USD/galão), primeira sessão completa depois do gap de abertura de domingo (19/07) documentado na leitura anterior
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, paridade BR, ISF, ISO) — recalculados sobre a sessão de 2026-07-20
  - BCB PTAX — 2026-07-20 (USD/BRL 5,0894, EUR/BRL 5,808), primeira publicação desde a sexta-feira 17/07 (5,1176)
  - CEPEA/ESALQ Paranaguá e Paraná interior via NAG — 2026-07-20 (suporte Paranaguá R$ 142,65/saca, var +1,16%; Paraná interior R$ 135,73/saca, var +1,21%)
  - NAG Físico BR (farelo MT/IMEA, RS, Rondonópolis; prêmios export PGUA farelo/óleo) — 2026-07-20
  - CFTC COT Managed Money — ainda referência 2026-07-14, sem atualização (próximo corte ~21/07, publicação ~24/07)
  - USDA Crop Progress — **atualizado para 2026-07-19** (13% excelente + 53% boa + 6% ruim = 66% bom-ou-excelente), primeira atualização em 8 dias frente a 2026-07-12 (65%)
  - USDA WASDE — ainda 2026-07-10 (só farelo Argentina/Brasil/China parcial), sem publicação nova
  - NOPA — 2026-07-20, `monthly_status` continua inacessível (paywall), fila `release-nopa-2026-07-20`
  - ABIOVE projeções mensais — balanços ago-dez/2026 (farelo/óleo/soja), sem alteração frente às leituras anteriores
  - NOAA CPC ENSO — 2026-07-20 (El Niño Advisory, sem mudança)
  - MPOB — 2026-07-20 (parser sem números extraídos, 3.439 caracteres, 11º dia consecutivo com o mesmo conteúdo, 10/07 a 20/07)
  - BCBA — 2026-07-20 (acessível, sem links de relatório detectados, mesmo padrão)
  - Notícias Agrícolas/Canal Rural/Farm Progress RSS — 2026-07-20 (160 itens lidos, 9 mantidos; manchete "Well-timed rain pushes soybeans through July heat", Farm Progress)
  - Forecasts estatísticos internos — 2026-07-20 (sexta geração seguida com as seis bandas simultaneamente em viés altista, spot ref atualizado pela primeira vez desde sexta-feira)
  - system/tributario_watch.toml — MP-1358-2026 (vigência formal encerrada há 9 dias, status ainda "tramitação"), PIS/COFINS-BIODIESEL-ISENCAO (vence em 11 dias), MP-1363-2026, STJ-RESP-2165276, B16-CNPE-2026, EPA-RFS-2026-2027, 45Z-CLEAN-FUEL, DANANTARA-INDONESIA, INDONESIA-B50, INDONESIA-LEVY-PMK9 — todos `atualizado_em` 2026-06-05 (45 dias sem atualização do monitor)
  - Cruza com [[2026-07-19_leitura-complexo]], [[2026-07-17_leitura-complexo]], [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (checkpoint D+7, tratado abaixo — agora 32 dias vencido)
status: ativa
vies: [bull-soja, bear-farelo, bull-oleo_soja]
---

> **Nota de proveniência:** hoje, segunda-feira 20/07/2026, é a primeira sessão de
> pregão genuinamente nova e independente do complexo agrícola desde o fechamento
> de sexta-feira (17/07) — o fim de semana de 18-19/07 não trouxe negociação real,
> só reprocessamentos da mesma vela (documentados nas duas leituras anteriores).
> Isso muda o caráter desta leitura: pela primeira vez em três dias, cada número
> citado abaixo é dado de mercado fresco, não uma nova geração do mesmo dado de
> sexta. E o resultado é decisivo — a soja abriu em 1.200,00 e fechou em 1.213,75
> (+1,70% frente ao fechamento de sexta, que a esta altura do pipeline está
> consolidado em 1.193,50), estendendo a distância acima da resistência de
> 1.180,00 de +2,86%. O farelo subiu também (+1,14%), mas menos que a soja em
> termos proporcionais — e é exatamente essa diferença de magnitude que empurrou
> o ratio Far/Soj para 79,27% (mais fundo na zona "abundante") e, ao mesmo tempo,
> **comprimiu a crush margin em -4,48%**, de 3,1735 para 3,0315 USD/bushel. O
> óleo foi a exceção do dia: fechou praticamente estável (-0,23%), mas com o
> primeiro fechamento abaixo da abertura desde o rali de sexta-feira, depois de
> abrir perto da máxima (74,29) e devolver a maior parte do ganho intradiário. A
> seção Visão geral explica o mecanismo por trás dessa aparente contradição —
> soja subindo, ratio caindo e crush comprimindo no mesmo dia — e cada seção de
> commodity destrincha o driver específico.

## Visão geral

O complexo soja é uma fábrica com uma única matéria-prima (a soja em grão) e
dois produtos de saída em proporção fixa por bushel esmagado: o **farelo**
(fração proteica, ~78% da massa, vira ração animal) e o **óleo degomado**
(fração de gordura, ~18-20% da massa, vira óleo de cozinha e biodiesel). Quem
decide o ritmo de esmagamento é a esmagadora, olhando a **crush margin**
(valor de farelo + óleo por bushel, menos o custo daquele bushel de soja,
medido na CBOT — Chicago Board of Trade, a bolsa de referência mundial para
esses contratos) e o **oil share** (fração desse valor capturada pelo óleo).
Quando o oil share sobe, o óleo passa a "pagar o crush" sozinho, e o farelo
vira, cada vez mais, um subproduto que a esmagadora aceita vender barato só
para liberar o óleo — é esse mecanismo que está por trás do **ratio Far/Soj**
(preço do farelo dividido pelo preço da soja, normalizado pela conversão
bushel↔short ton, "sht"): quando cai abaixo de 80%, o farelo está
historicamente "abundante" frente à soja, e o spread tende a comprimir (é um
spread de mean-reversion — comprimido demais tende a esticar de volta,
esticado demais tende a comprimir).

**O que aconteceu hoje é um exemplo didático de como o crush reage a um
choque assimétrico na perna de entrada (a soja), e não nas pernas de saída.**
A soja fechou em 1.213,75 cts/bushel (CBOT, sessão de 20/07/2026), um salto
de +1,70% frente ao fechamento consolidado de sexta-feira (1.193,50) — a
primeira confirmação genuinamente independente do rompimento da resistência
de 1.180,00 que as duas últimas leituras vinham tratando com cautela por
falta de uma sessão nova. O farelo também subiu (320,70, +1,14%), mas em
proporção menor que a soja. Como o ratio Far/Soj mede o farelo *relativo* à
soja, e a crush margin mede o valor dos produtos *menos* o custo da soja, o
resultado aritmético de "soja sobe mais que os produtos" é duplo e na mesma
direção: o ratio cai (para 79,27%, aprofundando a zona de "farelo abundante")
e a crush margin comprime (para 3,0315 USD/bu, -4,48% no dia) — mesmo com
farelo e óleo positivos ou estáveis em termos absolutos. É um lembrete
importante para quem opera o complexo: nem toda alta da soja é boa notícia
para quem está posicionado no crush, porque o crush é definido pela margem
entre os produtos e o insumo, não pelo nível absoluto de nenhuma das três
pernas isoladamente. O óleo, por sua vez, teve o dia mais fraco da semana
passada: fechou praticamente estável (-0,23%) mas abriu perto da máxima
(74,29, quase a máxima do dia de 74,60) e devolveu a maior parte do ganho ao
longo da sessão, fechando em 73,76 — o primeiro fechamento abaixo da abertura
desde o forte rali de sexta-feira, e a primeira confirmação real (não mais
especulação de baixo volume) de que o gap de queda do heating oil de domingo
se sustentou: o heating oil fechou hoje em 3,999 USD/galão, ante 4,06 na
sexta, uma queda real de -1,55% que já pressiona a margem de biodiesel
americana (0,832 USD/gal, -5,97% no dia). **O que mudou hoje:** três coisas
de uma vez — (1) a soja teve sua primeira confirmação tática independente do
rompimento de 1.180,00 (trata `alerta-quebra_resistencia-soja_cbot-2026-07-20`);
(2) o ratio Far/Soj teve sua primeira sessão de pregão real abaixo de 80%
desde que a revisão D+7 da tese estrutural do farelo venceu, encerrando de
fato o período de espera por confirmação independente (trata
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, hoje 32
dias vencida); e (3) o USDA Crop Progress foi atualizado pela primeira vez em
8 dias, mostrando uma lavoura americana ligeiramente melhor (66%
bom-ou-excelente, ante 65% na semana passada), um contraponto de fundo,
embora pequeno, à tese tática de alta da soja. **Leitura de uma linha:** o
pivô do complexo hoje é a mecânica do crush — a soja subiu mais que farelo e
óleo juntos, o que valida taticamente o rompimento e o ratio comprimido, mas
também é, ele mesmo, o motivo pelo qual a margem de esmagamento cedeu; convicção
moderada-alta em soja e farelo (agora com confirmação de sessão real), e
moderada em óleo (a tese estrutural de oil share/ISO segue intacta, mas o
dia de hoje foi o primeiro sinal tático de fricção desde o rali de sexta).

---

## Soja

**Viés: bull tático (convicção moderada-alta, agora com a primeira
confirmação de uma sessão de pregão genuinamente independente). Fechou em
1.213,75 cts/bushel na sessão de 20/07/2026 (CBOT, ticker ZSU26.CBT,
vencimento set/26), 2,86% acima da resistência de 1.180,00. Trata
`alerta-quebra_resistencia-soja_cbot-2026-07-20`.**

### O que sustenta a tese

**A vela de hoje é a primeira confirmação real do rompimento que as duas
últimas leituras trataram com cautela por falta de sessão nova.** Abertura
1.200,00, fechamento 1.213,75 (+13,75, +1,15% no dia), mínima 1.197,00,
máxima 1.221,50, volume 19.348 contratos (CBOT, 20/07/2026). O fechamento
ficou a 68,4% do range do dia contado a partir da mínima ((1.213,75-1.197,00)
÷ (1.221,50-1.197,00)) — força real, mas sem fechar colado à máxima, o que
sugere alguma realização de lucro perto do topo, não um rompimento sem
qualquer resistência. Frente ao fechamento de sexta-feira, agora consolidado
em 1.193,50 cts/bu (indicadores, 17/07/2026, usado no cálculo de crush e
paridade daquele dia), o ganho de hoje é de +20,25 pontos (+1,70%) — o
próprio tamanho do salto é o que resolve, de forma independente, a pergunta
em aberto nas duas últimas leituras: o rompimento de 1.180,00 sobreviveria a
uma sessão nova? A resposta de hoje é sim, e com folga maior (2,86% acima do
nível, ante os 2,08%-1,15% discutidos anteriormente sobre a mesma sessão de
sexta em diferentes gerações de dado).

**A curva forward ganhou seu primeiro movimento genuíno da semana.**
Agosto/26 (Q26) 1.223,00 → Setembro/26 (U26, contrato de referência/spot)
1.213,75 (desconto de -9,25, -0,76%) → Novembro/26 (X26) 1.225,00 (recupera
+11,25 sobre setembro, +0,93%) → Janeiro/27 (F27) 1.238,75 (+13,75 sobre
novembro, +1,12%) → Março/27 (H27) 1.238,75 (idêntico a janeiro, sem prêmio
adicional). O formato de "sorriso" (desconto no meio da curva, prêmio na
ponta longa) permanece intacto, e agora reflete uma sessão de fato negociada
hoje — não é mais uma repetição do formato observado nas leituras de
domingo.

**A paridade teórica em reais subiu para R$ 136,18/saca 60kg** (indicadores,
CBOT 1.213,75 cts × PTAX 5,0894 USD/BRL de 20/07/2026), um ganho de +1,53
(+1,14%) frente aos R$ 134,65/saca de sexta-feira (PTAX 5,1176). É importante
notar o mecanismo cambial aqui: o real se apreciou (USD/BRL caiu de 5,1176
para 5,0894, -0,55%) no mesmo dia em que a soja em dólar subiu +1,70% — os
dois efeitos vão na mesma direção para o exportador brasileiro (mais dólares
por bushel, e cada dólar vale um pouco menos em reais, mas o efeito dólar
domina), resultando em ganho líquido de +1,14% na paridade. Comparando com o
físico de Paranaguá hoje (R$ 142,65/saca, CEPEA/ESALQ via NAG, var +1,16%
frente a sexta): um prêmio de R$ 6,47/saca (+4,75%) do físico sobre a
paridade teórica. **Nota de honestidade sobre este número:** as leituras
anteriores (domingo) vinham documentando uma sequência de compressão desse
prêmio (4,68% → 3,81% → 3,78%) calculada sobre um fechamento de sexta-feira
que, à época, estava registrado em 1.204,50 — um valor que o pipeline
posteriormente revisou para 1.193,50 (o número usado hoje pelos próprios
indicadores). Como a base de comparação mudou sob o capô, não é seguro tratar
o salto de 3,78% para 4,75% como uma reversão real da tendência de
compressão; é mais correto tratar o prêmio de hoje (4,75%) como um novo ponto
de partida, medido sobre dados de sessão real, e recomeçar a série de
comparação a partir de amanhã.

**A soja no Paraná interior (CEPEA/ESALQ via NAG) fechou em R$ 135,73/saca**
(var +1,21% no dia), um desconto de -0,33% frente à paridade teórica de
R$ 136,18/saca — coerente com o custo logístico normal entre o interior e o
porto, e sem sinal de estresse ou aperto na base doméstica.

**O USDA Crop Progress foi atualizado pela primeira vez em 8 dias, com a
publicação referente a 19/07/2026: 13% excelente + 53% boa + 6% ruim = 66%
da lavoura americana em condição boa-ou-excelente**, ante 65% (12% excelente
+ 53% boa) na semana anterior (12/07/2026) — uma melhora de +1 ponto
percentual, concentrada na categoria "excelente" (12%→13%), com "boa" e
"ruim" estáveis. O mecanismo é direto: uma lavoura em condição ligeiramente
melhor do que a semana passada aponta para uma produtividade potencialmente
maior na colheita de 2026/27 (que ainda está em formação vegetativa nos
EUA neste momento do calendário), o que é, no fundamento, um contraponto de
oferta à tese de alta tática de hoje — mas o efeito é pequeno (apenas 1pp) e
não muda o sinal técnico do rompimento. A notícia do dia (Farm Progress,
20/07/2026: "Well-timed rain pushes soybeans through July heat") é
consistente com esse número: chuva bem distribuída durante o calor de julho
ajudou a lavoura a atravessar a fase crítica de enchimento de grãos sem
estresse hídrico severo — o mesmo mecanismo que explica a melhora marginal
do Crop Progress.

**O COT (CFTC) permanece com o mesmo dado de referência, 14/07/2026, sem
atualização.** Managed money net long em soja em +75.191 contratos (7,48% do
open interest de 1.004.746), ante +69.579 contratos (7,13% do OI de 975.954)
em 07/07/2026 — crescimento de dinheiro novo comprado, mas o dado ainda não
cobre a semana do rompimento de 17/07 nem a sessão de hoje. O próximo corte
(~21/07, publicação ~24/07) é o que vai mostrar se os fundos anteciparam ou
seguiram o movimento.

**Os forecasts estatísticos internos (20/07/2026, primeira geração calculada
sobre o novo spot de 1.213,75)** seguem altistas: central 7d = 1.238,47
cts/bu (bandas 1.186,73-1.290,21); central 30d = 1.333,08 cts/bu (bandas
1.225,97-1.440,20). É a sexta sessão seguida (contando as leituras de
domingo sobre dado repetido) em que as seis bandas do sistema (soja, farelo
e óleo, 7d e 30d) fecham simultaneamente em viés altista — mas hoje é a
primeira vez, desde sexta-feira, que o spot de referência do modelo é
genuinamente novo.

### O que invalida / risco para a soja

- **Um fechamento amanhã de volta abaixo de 1.197,00 (mínima de hoje) ou
  1.180,00 (resistência/suporte)** reabriria o cenário de teste, mesmo depois
  da confirmação de hoje.
- **O prêmio físico de Paranaguá sobre a paridade (hoje 4,75%) voltar a
  comprimir nas próximas sessões** — sem série comparável anterior confiável
  (ver nota de honestidade acima), este número precisa de 2-3 dias de dado
  fresco antes de virar um sinal de tendência.
- **O COT de 21/07 (publicação ~24/07) mostrar que os fundos não
  acompanharam o rompimento**, ou pior, começaram a vender.
- **O Crop Progress continuar melhorando nas próximas semanas** (66% hoje,
  ante 65% na semana passada) — reforçaria o argumento de oferta potencial
  maior, indo na direção contrária à tese tática de alta.
- **A notícia de expansão de área para a safra 2026/27** (mencionada em
  leituras anteriores, sem números concretos ainda) segue como contraponto
  estrutural de médio prazo a monitorar, sem relação direta com a tese
  tática de hoje.

### Leitura operacional — soja

A confirmação de hoje é o evento mais importante da semana para quem opera
soja direcional: depois de duas leituras de fim de semana pedindo cautela
por falta de uma sessão nova, a reabertura trouxe um salto de +1,70% que
estende o rompimento para 2,86% acima de 1.180,00, com volume normal
(19.348 contratos, dentro da faixa recente) e fechamento na porção superior
do range do dia. Isso favorece manter ou reforçar posição comprada alinhada
ao rompimento, com 1.180,00 seguindo como referência de stop lógica e
1.197,00 (mínima de hoje) como um stop mais próximo e mais conservador para
quem quer proteger o ganho do dia. Para quem está vendido contra o
rompimento, a sessão de hoje é o sinal mais forte até agora de que a tese
vendida precisa de um novo argumento fundamental (o Crop Progress ligeiramente
melhor é o único contraponto disponível, e é pequeno) para se sustentar. O
evento mais importante da próxima sessão é o COT de sexta (~24/07), que vai
mostrar se os fundos compraram durante a semana do rompimento.

---

## Farelo

**Viés: bear (estrutural mantido, tático agora confirmado por uma sessão de
pregão genuinamente nova e independente — pela primeira vez desde que a
revisão D+7 da tese original venceu). O ratio Far/Soj fechou em 79,27%
(indicadores, farelo 320,70 ÷ soja 1.213,75, base normalizada), aprofundando
-0,44 ponto percentual frente aos 79,71% de sexta-feira. Trata
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
(revisão vencida há 32 dias — ver abaixo) e `release-nopa-2026-07-20`.**

### O que sustenta a tese

**O farelo subiu em termos absolutos, mas menos que a soja — e é essa
diferença de magnitude que aprofundou o ratio.** Fechamento 320,70 USD/short
ton (CBOT, ticker ZMU26.CBT, sessão de 20/07/2026), abertura 318,30, mínima
316,70, máxima 324,10, volume 17.636 contratos — um ganho de +2,40 (+0,75%)
na sessão e de +3,60 (+1,14%) frente ao fechamento de sexta (317,10). Em
termos absolutos, isso é uma alta, não uma queda. Mas o ratio Far/Soj mede o
farelo *relativo* à soja (farelo ÷ (soja × 33,33), a conversão de bushel para
short ton) — como a soja subiu +1,70% no mesmo dia, quase 0,6 ponto
percentual a mais que o farelo, o ratio caiu de 79,71% para 79,27%,
**aprofundando a zona "abundante" (abaixo de 80%) pela primeira vez numa
sessão de pregão real desde que o gatilho original foi identificado.**

**Tratando `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`:**
a revisão programada da tese original (insight
[[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]) tinha data-alvo
18/06/2026 — hoje, 20/07/2026, ela está **32 dias vencida**. As três
perguntas da fila, agora respondidas com dado de sessão real pela primeira
vez: (1) o ratio fechou abaixo de 80%? **Sim, e hoje é a primeira
confirmação com uma sessão de pregão genuinamente independente** (as leituras
de fim de semana citavam 79,75%/79,71% sobre a mesma sessão de sexta,
reprocessada três vezes; hoje, 79,27%, é um número novo, calculado sobre
compra e venda reais de segunda-feira). (2) O WASDE mudou o quadro? **Não**,
segue parado em 10/07/2026, cobrindo apenas farelo (Argentina, Brasil,
China), sem nenhum dado de soja em grão ou óleo, e sem nenhum dado dos
Estados Unidos. (3) O NOPA confirmou o esmagamento? **Não** — trata
`release-nopa-2026-07-20`: o NOPA (National Oilseed Processors Association,
dado mensal de esmagamento americano) segue com `monthly_status` em 0,0
bool, a mesma barreira de assinatura paga documentada desde meados de junho,
agora mais de um mês sem alternativa de dado primário. Com a resposta (1)
agora satisfeita por uma sessão real, e (2)/(3) ainda pendentes, esta revisão
pode ser considerada tecnicamente encerrada no critério tático (ratio <80%
confirmado de forma independente), mas o critério fundamentalista completo
(WASDE + NOPA) segue em aberto — recomenda-se reabrir formalmente a tese como
"confirmada taticamente, pendente de confirmação fundamentalista" nos
próximos checkpoints (D+90 em 09/09/2026, D+180 em 08/12/2026).

**A crush margin comprimiu -4,48% no dia, de 3,1735 para 3,0315 USD/bushel**
(Board Crush: farelo 320,70 + óleo 73,76 − soja 1.213,75) — a maior queda de
um dia em toda a janela de 14 dias visível no briefing, quebrando quatro
sessões seguidas de alta (3,0001 em 14/07 → 3,0045 em 15/07 → 3,0866 em
16/07 → 3,1735 em 17/07 → **3,0315 em 20/07**). O mecanismo é o mesmo já
descrito na Visão geral: a soja, o insumo, subiu mais rápido que a soma dos
dois produtos, o que mecanicamente reduz a margem de esmagamento no cálculo
de board crush, mesmo com farelo e óleo positivos ou estáveis. Isso não
invalida a tese estrutural do farelo (que depende de oferta/demanda física,
não do board crush diário), mas é um dado tático relevante: se a crush
margin continuar comprimindo, o incentivo de curto prazo da esmagadora para
processar a pleno vapor diminui, o que — com defasagem de semanas — poderia
eventualmente aliviar a pressão de oferta de farelo que hoje sustenta a tese
bear.

**A trajetória projetada da ABIOVE (Associação Brasileira das Indústrias de
Óleos Vegetais, projeções mensais, sem alteração) segue sendo o pilar mais
sólido do argumento estrutural, porque não depende do preço do dia.** A
exportação de farelo brasileiro projetada cai de 1.400 mil toneladas em
agosto/2026 para 700 mil toneladas em dezembro/2026 (queda de 50% em quatro
meses), enquanto a produção cai de forma bem mais suave (2.285,06 → 1.659,04
mil toneladas no mesmo período, -27,4%) — menos farelo saindo pelo porto, com
produção caindo bem menos que a exportação, empurra o volume excedente para
o mercado interno de ração, pressionando o preço doméstico.

**As praças físicas de farelo no Brasil (NAG, 20/07/2026) mostram um sinal
misto que merece registro sem sobre-interpretação.** Mato Grosso/IMEA
permanece estável em R$ 1.602,80/ton (var 0,0%), Rio Grande do Sul estável em
R$ 1.640,00/ton, mas Rondonópolis/MT saltou para R$ 1.650,00/ton (var
+3,13% frente a R$ 1.600,00 na leitura anterior) — um movimento pontual e
localizado (uma única praça, sem confirmação nas outras duas) que não deve
ser lido como reversão da tese estrutural, mas é o primeiro sinal físico de
alta em várias sessões e vale monitorar se se repete. O prêmio de exportação
em Paranaguá segue em +0,05 USD/short_ton (julho/26, NAG), agora 17 dias
corridos sem qualquer variação desde 03/07/2026 — reforçando a suspeita
(já registrada em leituras anteriores) de que pode ser um dado de fonte não
atualizada, não um preço de mercado genuinamente parado (ver Honestidade).

**O Índice de Sobra de Farelo (ISF) permanece em 80/100 (4 de 5 condições
estruturais)**, inalterado desde pelo menos 01/07/2026 — reforça que é um
índice calculado sobre condições estruturais (ABIOVE, crush, oferta), não
sobre o fechamento do dia, e por isso não reage ao ruído tático de hoje.

**O oil-meal spread (óleo menos farelo, por bushel) comprimiu para 1,0582
USD/bu**, ante 1,1561 (17/07) — uma queda de -8,47%, terceira leitura
mostrando o farelo "recuperando terreno relativo" frente ao óleo depois do
pico de divergência de sexta-feira. Mede, de outro ângulo, a mesma mecânica
de "soja subiu mais que os produtos" que comprimiu a crush margin.

**O COT de 14/07/2026, sem atualização, mantém o mesmo contraponto relevante
à tese bear.** Managed money net long em farelo em +46.576 contratos (7,77%
do open interest de 599.353), ante +18.722 contratos (3,14% do OI de
595.447) em 07/07/2026 — mais que dobrou em uma semana. Continua sendo o dado
mais direto disponível hoje contra uma posição vendida em farelo outright.

**O forecast estatístico do farelo (20/07/2026, primeira geração sobre o
novo spot)** segue com viés altista: central 7d = 326,47 USD/sht (bandas
313,55-339,40); central 30d = 348,06 USD/sht (bandas 321,30-374,82). O
modelo estatístico (que reage a momentum de preço recente, não a
fundamentos) segue na direção oposta à tese fundamentalista ABIOVE + ratio —
uma divergência que já vem sendo documentada há várias leituras e que
reforça a recomendação de tratar o forecast estatístico como um sinal de
momentum, não como uma leitura fundamentalista concorrente.

### O que invalida / risco para o farelo

- **A crush margin continuar comprimindo nas próximas sessões** — se a
  esmagadora reduzir o ritmo de processamento em resposta a uma margem menor,
  o excedente de farelo que sustenta a tese ABIOVE pode diminuir com
  defasagem.
- **O ratio Far/Soj voltar acima de 80% numa próxima sessão** — a distância
  atual (0,73 ponto percentual) ainda é pequena.
- **O salto pontual de Rondonópolis (+3,13%) se repetir nas outras praças**
  — se Mato Grosso e Rio Grande do Sul também subirem nas próximas sessões,
  seria um sinal físico de alívio da abundância que merece nova leitura.
- **O COT de 21/07 (publicação ~24/07) mostrar os fundos continuando a
  aumentar o net long em farelo** — reforçaria o risco de squeeze numa
  posição vendida direcional.
- **NOPA seguir inacessível indefinidamente**, sem confirmação do
  esmagamento americano para os checkpoints D+90 (09/09/2026) e D+180
  (08/12/2026).

### Leitura operacional — farelo

Hoje é o dia mais importante da tese bear-farelo desde que ela foi
formulada: pela primeira vez, o ratio abaixo de 80% e a compressão da crush
margin vêm de uma sessão de pregão real, não de reprocessamento de dado
antigo. Isso justifica tratar o gatilho tático como confirmado e reabrir
formalmente a revisão D+7 vencida com o critério tático satisfeito — mas a
compressão simultânea da crush margin é um alerta de que o próprio mecanismo
que gera a abundância de farelo (esmagamento a pleno vapor) pode perder
força se a soja continuar subindo mais rápido que os produtos. Para quem
opera farelo outright vendido, a confirmação de hoje é o sinal mais forte
até agora, mas o COT (fundos dobrando net long em uma semana) segue como o
principal risco de squeeze. Para quem prefere o veículo mais defensável — o
spread farelo/soja ou o crush completo, em vez de direcional puro —, a
compressão do oil-meal spread (-8,47% no dia) e da própria crush margin
(-4,48%) sugerem que a divergência farelo-fraco/óleo-forte, que vinha se
esticando havia dias, começou a reverter um pouco hoje — vale reavaliar o
tamanho da posição relativa antes de adicionar.

---

## Óleo

**Viés: bull estrutural mantido (oil share e ISO seguem no teto), mas com o
primeiro sinal tático de fricção desde o rali de sexta-feira. Fechou em
73,76 cts/lb na sessão de 20/07/2026, praticamente estável no dia (-0,23%
frente ao fechamento de sexta, 73,93), mas abrindo perto da máxima (74,29) e
devolvendo a maior parte do ganho intradiário. O oil share caiu ligeiramente
para 53,49% e o Índice de Suporte do Óleo (ISO) segue em 100/100.**

### O que sustenta a tese

**A vela de hoje é a primeira do complexo, desde sexta-feira, a fechar
abaixo da abertura.** Fechamento 73,76 cts/lb (CBOT, ticker ZLU26.CBT,
20/07/2026), abertura 74,29 (muito perto da máxima do dia, 74,60), mínima
72,80 — o preço abriu forte, tocou a máxima no início da sessão e devolveu a
maior parte do ganho ao longo do dia, fechando em 53,3% do range
((73,76-72,80) ÷ (74,60-72,80)), praticamente no meio. Não é uma reversão
violenta (a queda de -0,23% frente a sexta é pequena), mas é o primeiro dia,
depois do salto de +3,29% de sexta-feira documentado nas leituras anteriores,
em que o óleo não fechou perto da máxima da sessão — um padrão técnico de
"perda de fôlego" que merece atenção, sem ainda constituir um sinal de
reversão de tendência.

**A curva forward mantém a mesma backwardation (desconto crescente nos
vencimentos mais distantes) das leituras anteriores, agora sobre dado de
sessão real.** Agosto/26 (Q26) 74,60 → Setembro/26 (U26, spot) 73,76 (-0,84,
-1,13%) → Outubro/26 (V26) 72,76 (-1,00, -1,36%) → Dezembro/26 (Z26) 72,09
(-0,67, -0,93%) → Janeiro/27 (F27) 71,70 (-0,39, -0,54%) — uma queda total de
-2,90 cts/lb (-3,89%) de agosto a janeiro/27. A assinatura de força
concentrada no vencimento mais próximo, em vez de re-precificação estrutural
de toda a curva, segue intacta.

**A margem de biodiesel americano comprimiu para 0,832 USD/galão** (receita
7,164 = heating oil 4,00 + 1,5×RIN 2,11; custo 6,33 = óleo 5,532 + industrial
0,80), uma queda de -5,97% frente aos 0,8848 de sexta-feira. **Este é o dado
mais importante da seção óleo hoje**, porque confirma, com uma sessão de
fato negociada, o que o gap eletrônico de domingo só sugeria com baixo
volume: o heating oil (o principal componente de receita do biodiesel
americano, junto com o RIN D4) fechou hoje em 3,999 USD/galão (abertura
4,002, máxima 4,002, mínima 3,995, volume muito baixo de apenas 109
contratos — a própria liquidez baixa do heating oil hoje é um sinal de que o
mercado de energia está com pouca convicção direcional), uma queda real de
-1,55% frente ao fechamento de sexta (4,06). A tensão de mecanismo já
documentada em leituras anteriores continua válida e agora fica mais visível:
o óleo de soja é ao mesmo tempo o produto que sobe na CBOT (bullish para o
papel) e o principal insumo de custo do biodiesel (bearish para a margem de
quem processa) — hoje, com o óleo estável e o heating oil caindo, é a
margem que sofre mais.

**O Índice de Suporte do Óleo (ISO) permanece em 100/100 (5 de 5 condições)**,
inalterado desde pelo menos 01/07/2026 — reforça que a tese estrutural (óleo
dominando o valor do crush) não é afetada pela oscilação tática de um único
dia.

**O oil share caiu ligeiramente para 53,49%** (indicadores, 20/07/2026),
ante 53,83% em 17/07 — uma queda de -0,34 ponto percentual, coerente com o
óleo ficando estável enquanto o farelo subiu mais em termos absolutos hoje;
o óleo segue, ainda assim, capturando a maior fatia do valor do crush
(acima de 50%), sem qualquer sinal de perda da liderança estrutural.

**O COT de 14/07/2026, sem atualização, mantém o óleo como a perna mais
"concorrida" das três em termos de posicionamento.** Managed money net long
em +107.945 contratos (16,92% do open interest de 638.102), ante +84.919
contratos (13,22% do OI de 642.514) em 07/07/2026 — um aumento de +23.026
contratos (+27,1%) na semana. Com o net long em ~17% do OI (o mais alto das
três pernas), a posição comprada no óleo segue sendo a mais crowded do
complexo — e, com o primeiro dia de fechamento fraco de hoje, o risco de que
esse posicionamento concentrado amplifique uma eventual correção sobe de
relevância.

**O forecast estatístico do óleo (20/07/2026, primeira geração sobre o novo
spot)** mantém o viés altista: central 7d = 74,88 cts/lb (bandas
70,20-79,56); central 30d = 79,55 cts/lb (bandas 69,86-89,23).

### O que invalida / risco para o óleo

- **Um fechamento abaixo de 72,76 (o vencimento de outubro na curva de
  hoje) ou de 72,80 (mínima de hoje)** reabriria o cenário de correção mais
  concretamente do que a mera perda de fôlego observada hoje.
- **O heating oil continuar caindo nas próximas sessões**, aprofundando a
  compressão da margem de biodiesel (já -5,97% hoje) e reduzindo o incentivo
  econômico a processar óleo de soja em biodiesel nos EUA.
- **O posicionamento dos fundos (net long em 16,92% do OI, o mais
  concorrido das três pernas) sofrer uma reversão** quando o próximo COT
  chegar (~24/07) — com o primeiro dia fraco de preço já registrado, o risco
  de uma correção mais abrupta liderada por liquidação de posição comprada
  aumenta.
- **MPOB seguir inacessível** — impossível avaliar o efeito do El Niño ou
  das restrições/levy indonésias sobre o prêmio de substituição via palma.
  Hoje é o 11º dia consecutivo com o mesmo conteúdo sem números extraídos.

### Leitura operacional — óleo

O óleo segue sendo a tese estruturalmente mais forte do complexo (oil share
acima de 50%, ISO no teto de 100/100), mas hoje registrou o primeiro sinal
tático de fricção desde o rali de sexta-feira: abriu perto da máxima e
fechou no meio do range, com a margem de biodiesel comprimindo de forma real
(não mais especulativa) por causa da queda confirmada do heating oil. Para
quem está comprado direcional em óleo desde o rompimento de sexta, a sessão
de hoje não é um sinal de saída, mas justifica apertar o stop para perto da
mínima de hoje (72,80) em vez de manter a folga mais ampla usada na semana
passada. Para quem opera exposição relativa dentro do crush, a compressão do
oil-meal spread (-8,47% no dia) sugere que a divergência entre as duas
pernas, que vinha se esticando, teve sua primeira pausa — vale reavaliar o
tamanho da posição antes de adicionar a favor do óleo relativo ao farelo. O
evento mais importante da próxima sessão para esta tese é dose dupla: a
trajetória do heating oil ao longo da semana (se a queda de hoje continuar,
a pressão sobre a margem de biodiesel se aprofunda) e o COT de sexta
(~24/07), que vai testar se o posicionamento mais concorrido do complexo
começou a ceder.

---

## Spreads e crush — leitura de complexo

### Crush margin: 3,0315 USD/bu — maior queda de um dia da janela, quebrando quatro altas seguidas

A crush margin caiu -4,48% no dia (de 3,1735 para 3,0315 USD/bu), a maior
queda de um dia em toda a janela de 14 dias visível no briefing, encerrando
uma sequência de quatro sessões seguidas de alta (3,0001 em 14/07 → 3,0045
em 15/07 → 3,0866 em 16/07 → 3,1735 em 17/07 → **3,0315 em 20/07**). O
mecanismo, explicado na Visão geral e nas seções de soja/farelo: a soja
(insumo) subiu +1,70% no dia, mais que a soma ponderada dos ganhos de
farelo (+1,14%) e óleo (-0,23%), o que mecanicamente reduz a margem do
board crush. Isso não significa que o incentivo de esmagamento desapareceu
— 3,0315 USD/bu ainda é um valor histórico saudável — mas é o primeiro sinal
de que o ritmo de aceleração da margem, que vinha subindo havia quatro
sessões, pode estar se revertendo.

### Ratio Far/Soj: 79,27% — primeira confirmação de sessão real abaixo de 80%

O achado tático central desta leitura de segunda-feira: pela primeira vez
desde que o cruzamento abaixo de 80% foi identificado, o ratio caiu ainda
mais (79,71% sexta → 79,27% hoje) sobre uma sessão de pregão genuinamente
nova e independente, não sobre reprocessamento do mesmo dado. Trata
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` (agora
32 dias vencida, critério tático considerado satisfeito — ver seção Farelo).
A distância abaixo do limiar de 80% está agora em 0,73 ponto percentual, a
maior desde 15/07 (79,92%).

### Oil share: 53,49% — leve recuo, óleo segue capturando a maior fatia do crush

Recuo de -0,34 ponto percentual frente a sexta-feira (53,83% → 53,49%),
coerente com o óleo estável e o farelo subindo mais em termos absolutos
hoje. O óleo segue, ainda assim, dominando a fatia de valor do crush, sem
qualquer sinal de perda da liderança estrutural que sustenta o ISO em
100/100.

### Oil-meal spread: 1,0582 USD/bu — compressão de -8,47%, farelo recupera terreno relativo

Queda de -8,47% no dia (1,1561 → 1,0582 USD/bu), a maior compressão de um
dia nesta janela — mede, de outro ângulo, a mesma mecânica "soja subiu mais
que os produtos" que comprimiu a crush margin, e sugere que a divergência
farelo-fraco/óleo-forte que caracterizou a sessão de sexta-feira teve sua
primeira pausa real hoje.

### Margem de biodiesel: 0,832 USD/gal — confirmação real da compressão, heating oil fecha em queda

A margem caiu -5,97% no dia, confirmando com dado de sessão real (não mais
o gap especulativo de domingo) que o heating oil (3,999 USD/galão hoje,
ante 4,06 na sexta, -1,55%) está pressionando a margem de biodiesel
americano — o principal canal pelo qual o óleo de soja CBOT (que sobe) e a
economia de quem processa biodiesel (que aperta) entram em tensão.

### COT: sem atualização — óleo segue disparado o mais concorrido

O dado de 14/07/2026 segue sem atualização, a um dia do próximo corte
(~21/07, publicação ~24/07). Como fração do open interest, o óleo é
disparado o mais concorrido (16,92% vs 7,77% do farelo e 7,48% da soja) — o
posicionamento confirma o bull-óleo estrutural desta leitura, mas também é
o maior fator de risco de reversão abrupta, especialmente depois do
primeiro dia de fechamento fraco registrado hoje.

### ISF em 80/100, ISO em 100/100 — inalterados, confirmam que a mudança de hoje é tática, não estrutural

O Índice de Sobra de Farelo (4/5 condições) e o Índice de Suporte do Óleo
(5/5 condições) permanecem exatamente nos mesmos níveis de semanas
anteriores, mesmo com toda a movimentação tática de hoje (ratio, crush
margin, oil-meal spread) — a confirmação mais clara de que os índices
sintéticos capturam condições estruturais (ABIOVE, oferta, crush), e o que
mudou hoje foi puramente a mecânica de preço de uma única sessão.

### O que os índices dizem juntos em 20/07/2026

ISF 80/100 + ISO 100/100 (ambos inalterados, condições estruturais intactas)
+ ratio Far/Soj confirmado abaixo de 80% pela primeira vez numa sessão real
(79,27%) + crush margin e oil-meal spread comprimindo no dia por causa do
próprio tamanho do rali da soja + oil share em leve recuo mas ainda acima de
50% + margem de biodiesel comprimindo de forma confirmada (não mais
especulativa) + COT ainda mostrando fundos mais posicionados em óleo do que
em qualquer outra perna — formam um quadro em que a tese estrutural do
complexo (esmagamento incentivado, óleo dominando o valor, farelo abundante)
segue intacta, mas a mecânica tática de curto prazo (a soja subindo mais
rápido que os produtos) já começou a comprimir as métricas de spread que
mediam a divergência entre as pernas. Isso não inverte nenhuma das três
teses de preço, mas é o primeiro sinal, nesta janela, de que o próximo
movimento relevante pode vir da normalização dos spreads, não da extensão
deles.

---

## Lente fiscal e regulatória BR

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L) — a
vigência formal (`vigencia_ate` 11/07/2026) venceu há 9 dias, e o monitor
tributário segue sem qualquer atualização de status** (system/tributario_watch.toml,
evento MP-1358-2026, `atualizado_em` 2026-06-05, status ainda "tramitacao").
Enquanto o combustível fóssil segue subsidiado, a competitividade relativa
do biodiesel dentro do mix B15 mandatório fica pressionada — um vetor
regulatório independente da margem de biodiesel americana (que hoje
comprimiu -5,97% por conta própria, via heating oil), somando dois
headwinds distintos sobre a mesma economia de processamento.

**Isenção PIS/Cofins biodiesel — vencimento em 31/07/2026, agora a 11
dias.** Sem sinalização pública de renovação até hoje (evento
PISCOFINS-BIODIESEL-ISENCAO, `atualizado_em` 2026-06-05, sem mudança). Com a
margem de biodiesel americana comprimindo de forma confirmada hoje (0,832
USD/gal, -5,97%) e o vencimento da isenção brasileira a apenas 11 dias, o
cenário de "duplo headwind" (custo tributário potencial no Brasil + margem
apertada nos EUA) segue relevante e ganha urgência — é o vetor tributário
mais próximo de um desfecho concreto nesta leitura.

**B16 — sem data, travado em B15.** Sem mudança de status (evento
B16-CNPE-2026, `atualizado_em` 2026-06-05, status "adiado"). Testes técnicos
do FNDCT com resultado esperado ~nov/2026 — realista só fim de 2026/início
de 2027.

**MP 1.363/2026 (subsídio ao diesel fóssil, R$ 1,12/L) — em vigor até
31/12/2026.** Sem alteração. Bearish estrutural persistente para a demanda
incremental de óleo de soja no mercado doméstico brasileiro.

**STJ REsp 2.165.276/2026 — crédito PIS/Cofins para esmagadoras.** Sem
alteração. Bullish para soja/óleo (alívio de custo de entrada para
biodiesel) e, por extensão, incentivo a mais esmagamento — em tensão direta
com a compressão de hoje na crush margin (o alívio de custo tributário é
estrutural e de longo prazo; a compressão de hoje é tática e de curtíssimo
prazo).

**Vetores dos EUA e Indonésia, revisitados (sem mudança de status,
`atualizado_em` 2026-06-05 em todos):** EPA-RFS-2026-2027 (volumes recordes
de biocombustível, BBD 8,86→9,07 bi RINs, sustentando estruturalmente o RIN
D4 e o óleo CBOT — o RIN D4 usado no cálculo da margem de biodiesel segue
fixo em 2,11 USD/RIN, ver Honestidade); 45Z-CLEAN-FUEL (regra proposta que
tiraria insumo importado da elegibilidade ao crédito, favorecendo óleo de
soja doméstico americano); DANANTARA-INDONESIA (centralização estatal da
exportação de palma, assunção plena da cadeia alvo em 01/09/2026 — risco de
menor saldo exportável de palma, suporte ao óleo de soja por substituição);
INDONESIA-B50 (retórica agressiva mas quota flat — provável B45 em 2026,
B50 pleno só 2027-28); INDONESIA-LEVY-PMK9 (imposto de exportação de CPO até
12,5% desde 01/03, encarecendo palma e favorecendo substituição por óleo de
soja). Todos esses vetores seguem, em conjunto, num sentido estruturalmente
bullish para o óleo de soja via substituição de palma — mas seguem
inverificáveis pelo lado dos dados de mercado (MPOB inacessível há 11 dias
consecutivos, ver Honestidade).

**O monitor tributário como um todo está há 45 dias sem qualquer
atualização** (`atualizado_em` 2026-06-05 em todos os dez eventos
rastreados) — o intervalo segue crescendo em um momento em que dois vetores
(MP 1.358 e a isenção PIS/Cofins) têm datas de vencimento formal já vencida
ou a apenas 11 dias. Vale sinalizar este ponto, mais uma vez, como
prioridade de manutenção do sistema, independentemente da leitura de preço.

---

## Riscos e eventos próximos

**O COT (CFTC) — dado de 14/07/2026 segue sendo o mais recente, a um dia do
próximo corte (~21/07, publicação normal ~24/07).** É o evento mais
importante da semana: vai mostrar se os fundos compraram soja e farelo
durante a semana do rompimento e do cruzamento do ratio, e se o
posicionamento mais concorrido do complexo (óleo, 16,92% do OI) começou a
ceder depois do primeiro dia de fechamento fraco registrado hoje.

**A isenção PIS/Cofins do biodiesel vence em 31/07/2026, agora a 11 dias**,
sem sinalização de renovação — o vetor tributário mais próximo de um
desfecho concreto nesta leitura, coincidindo com uma margem de biodiesel
americana que já comprime por conta própria.

**A trajetória do heating oil ao longo da semana** é o driver mais imediato
para a tese do óleo: a queda confirmada de hoje (3,999, -1,55% frente a
sexta) já pressiona a margem de biodiesel; uma continuação da queda
aprofundaria essa pressão.

**Se a crush margin continuar comprimindo nas próximas sessões**, vale
monitorar se o ritmo de esmagamento reportado pela ABIOVE/NOPA (quando
acessível) começa a desacelerar — o mecanismo estrutural do farelo depende
de esmagamento a pleno vapor, e a queda de -4,48% de hoje é o primeiro sinal
tático nessa direção, ainda sem confirmação fundamentalista.

**NOPA — segue inacessível** (fila `release-nopa-2026-07-20` tratada aqui,
sem dado interpretável), sem crush americano confirmado por fonte primária.

**MPOB — sem números de palma extraídos há 11 dias consecutivos**, mantendo
cego o efeito do El Niño e dos vetores regulatórios indonésios sobre o
prêmio de substituição do óleo de soja.

**Checkpoints futuros da tese estrutural do farelo (ABIOVE)** — D+90 em
09/09/2026 e D+180 em 08/12/2026 (insight
[[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]) — a revisão D+7,
agora 32 dias vencida, tem hoje seu critério tático satisfeito (ratio <80%
confirmado numa sessão real), mas ainda sem confirmação de fundamentos
(WASDE, NOPA); os checkpoints estruturais seguem o critério de mais alta
confiança para julgar a tese ao longo do tempo.

---

## Honestidade

O que não foi possível validar neste briefing de 20/07/2026, onde a
confiança é baixa ou há lacunas materiais:

**1. O fechamento de sexta-feira (17/07) usado como base de comparação para
os números de hoje é, ele mesmo, resultado de revisões de pipeline
documentadas nas duas leituras anteriores.** As leituras de domingo
registraram o fechamento de soja de sexta-feira em 1.204,50 cts/bu (terceira
geração de dado, tida como estável); os indicadores de hoje, porém, calculam
a paridade e a crush de 17/07 usando 1.193,50 cts/bu — um valor 11 pontos
mais baixo. Isso significa que ao menos uma revisão adicional ocorreu entre
a última leitura (19/07) e a geração de dados usada hoje, sem qualquer
sinalização explícita no dump. Todos os cálculos de variação percentual
desta leitura usam consistentemente o valor de 1.193,50 (o mesmo usado pelos
indicadores de hoje), mas isso significa que comparações de tendência que
atravessam essa fronteira (como o prêmio físico/paridade, tratado na seção
Soja) podem estar comparando bases inconsistentes — tratado com nota
explícita naquela seção.

**2. O prêmio de exportação de farelo em Paranaguá (+0,05 USD/sht) e o de
óleo (+0,08 cts/lb) estão no mesmo valor exato desde pelo menos 03/07/2026**
(NAG, agora 17 dias corridos sem variação de nenhum centavo) — não é
possível distinguir se isso reflete um mercado de exportação genuinamente
parado ou um valor que não está sendo atualizado de fato na fonte.

**3. O salto pontual do farelo físico em Rondonópolis/MT (+3,13% no dia,
para R$ 1.650,00/ton) não é confirmado pelas outras duas praças (Mato
Grosso/IMEA e Rio Grande do Sul, ambas estáveis)** — tratado como um dado
localizado, não como sinal de reversão da tese estrutural, mas vale
monitorar se se repete nas próximas sessões.

**4. O COT (CFTC) segue com dado de referência 14/07/2026, sem
atualização.** Nem a semana do rompimento da soja (17/07) nem a sessão de
hoje (20/07) estão refletidas no posicionamento dos fundos — o próximo
relatório (dado esperado ~21/07, publicação ~24/07) é o teste genuíno mais
importante em aberto.

**5. Percentis históricos de COT não calculados** — os números de
14/07/2026 são lidos apenas em nível absoluto e como fração do open
interest corrente (soja 7,48%, farelo 7,77%, óleo 16,92%), sem série
histórica completa para calibrar se algum desses níveis está objetivamente
"esticado" no sentido histórico.

**6. O WASDE segue cobrindo apenas farelo (Argentina, Brasil, China
parcial), sem nenhum dado de soja em grão ou óleo de soja, em qualquer
geografia, e sem nenhum dado dos Estados Unidos** — sem atualização desde
10/07/2026. A pergunta central sobre "oferta grande de soja" segue sem canal
de resposta interno.

**7. NOPA (fila `release-nopa-2026-07-20`) segue com `monthly_status` em
0,0 bool** — mesma barreira de assinatura paga documentada desde meados de
junho, agora com mais de um mês sem alternativa de dado primário sobre o
esmagamento americano. A "novidade" sinalizada pela fila é apenas a data de
coleta, não um dado genuinamente interpretável.

**8. Palma malaia (MPOB) segue sem números extraídos, agora por 11 dias
consecutivos com o mesmo conteúdo exato (3.439 caracteres, de 10/07 a
20/07/2026)** — a persistência do byte count idêntico sugere, possivelmente,
uma página que não está mais sendo servida com conteúdo atualizado (e não
apenas um parser incompatível). Continua impossível avaliar o efeito do El
Niño ou dos vetores regulatórios indonésios sobre o prêmio de substituição
do óleo de soja.

**9. Clima INMET (BR) não foi usado como driver desta leitura.** Julho é
entressafra da soja brasileira (colheita concluída, plantio só em outubro)
— sem relevância direta para a tese de preço neste momento do calendário
agrícola, embora o El Niño Advisory (NOAA CPC, inalterado desde pelo menos
03/07/2026) permaneça relevante para a expectativa da safra de plantio de
outubro/26 e para o clima do Sudeste Asiático (palma).

**10. BCBA Argentina — sem relatórios de esmagamento/exportação acessíveis
via scraper** (page_fetched=1,0 mas sem links de relatório, 20/07/2026, sem
mudança).

**11. RIN D4 como parâmetro fixo (2,11 USD/RIN) segue sendo uma fonte
relevante de incerteza do modelo de biodiesel**, sem novo dado hoje — a
margem calculada em 0,832 USD/gal usa esse valor fixo; se o RIN de mercado
estiver, na realidade, diferente de 2,11, tanto a margem quanto o ISO podem
estar mal calibrados, independentemente da compressão real documentada
hoje via heating oil.

**12. O volume do heating oil de hoje é extremamente baixo (109 contratos,
ante ~32.681 na sexta-feira)** — mesmo sendo um fechamento de sessão
regular (não mais o gap eletrônico de domingo), essa liquidez baixa
enfraquece um pouco a confiança de que o nível de 3,999 reflete um consenso
de mercado amplo, e não apenas alguns poucos negócios. Recomenda-se
confirmar a queda com mais uma sessão antes de tratá-la como tendência
consolidada.

*Nenhum número foi inventado ou estimado além do que consta no briefing de
20/07/2026 e nos insights anteriores referenciados. A contribuição central
desta leitura foi identificar que a primeira sessão de pregão genuinamente
nova desde sexta-feira confirmou, de forma independente, tanto o rompimento
da soja quanto o cruzamento do ratio Far/Soj abaixo de 80% — mas revelou, ao
mesmo tempo, que o próprio tamanho do movimento da soja comprimiu a crush
margin e o oil-meal spread, uma mecânica que não inverte nenhuma das três
teses de preço, mas que é o primeiro sinal, nesta janela, de que os spreads
podem estar prestes a normalizar depois de várias sessões de esticamento.*
