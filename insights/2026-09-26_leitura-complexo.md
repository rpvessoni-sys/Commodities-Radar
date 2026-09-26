---
data: 2026-09-26
titulo: "A sessão de 25/09 chega hoje com volume finalmente saudável (soja 180.479, farelo 94.390, óleo 99.658 contratos) fechando o alerta de captura parcial que a leitura de ontem havia levantado — mas os números confirmados mudam a história fina: o ratio Far/Soj não subiu pela quarta sessão seguida como o dado provisório sugeria, ele picou em 84,80% no dia 24/09 e recuou para 84,23% no dia 25/09, e o mesmo recuo aparece em espelho no oil share, no crush margin e na margem de biodiesel americana (que caiu, não subiu como o dado suspeito de ontem indicava); ao mesmo tempo chega o corte de COT de 22/09 — o primeiro em dez dias — mostrando fundos ampliando net long em farelo (+4,36%) e revertendo com força a redução da semana anterior em soja (+9,80%, superando o patamar de 08/09), enquanto cortam net long em óleo (-9,21%), o maior movimento relativo das três pernas; isso muda a soja de neutro para bull, mantém bull-farelo com convicção reforçada por uma pausa saudável e não uma reversão, e aprofunda bear-óleo com a confirmação de posicionamento que faltava — tudo isso no mesmo dia em que o WASDE desaparece por completo do dump e o monitor tributário completa 113 dias corridos sem revisão humana"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT — sessão de **2026-09-25**, agora com dado consolidado (volume normal, OHLC distinto do dia anterior): soja (ticker ZSX26.CBT, venc. nov/26) abertura 1.317,50, máxima 1.320,50, mínima 1.297,50, fechamento **1.320,00**, volume **180.479 contratos**; farelo (ticker ZMZ26.CBT, venc. dez/26) abertura 370,70, máxima 372,40, mínima **365,00**, fechamento **370,60** (campo `fechamento_Z26` do mesmo ticker agora **bate exatamente** com o campo `fechamento` genérico — a divergência interna de ontem, 371,50 vs 371,80, desapareceu), volume **94.390 contratos**; óleo (ticker ZLZ26.CBT, venc. dez/26) abertura 67,55, máxima 67,89, mínima 66,65, fechamento **67,82**, volume **99.658 contratos**. Curva futura em 25/09 — soja: nov/26 (base) 1.320,00 → jan/27 1.333,00 → mar/27 1.339,50 → mai/27 1.346,75 → jul/27 1.351,00 (contango regular, +0,98% nov→jan, +0,32% mai→jul); farelo: out/26 373,20 → dez/26 (base) 370,60 → jan/27 369,40 → mar/27 368,20 → mai/27 368,00 (backwardation suave, -0,70% de out/26 a dez/26 e -0,70% de dez/26 a mai/27); óleo: out/26 67,25 → dez/26 (base) 67,82 → jan/27 68,02 → mar/27 68,25 → mai/27 68,41 (contango regular, +0,85% out→dez, +0,87% dez→mai)
  - CME CBOT — sessão de **2026-09-24**, também revisada nesta janela frente ao que o dump de ontem mostrava: farelo abertura **369,00** (era 370,70), máxima **376,90** (era 372,40), mínima **368,00** (era 370,40), fechamento **372,40** (era 371,20), volume **96.901 contratos** (era 830) — todos os campos mudaram, exceto a máxima permanecer coincidentemente próxima; heating oil (HO=F) abertura **4,8289** (era 4,5700), máxima **5,0614** (era 4,5850), mínima **4,6687** (era 4,5100), fechamento **4,7303** (era 4,5171), volume **41.371 contratos** (era 372) — a mesma magnitude de revisão, ver Honestidade
  - CME NYMEX heating oil (HO=F) — **2026-09-25**: abertura 4,5700, máxima 4,5961, mínima 4,3789, fechamento **4,5799** USD/galão, volume **62.876 contratos** — OHLC agora **distinto** do de 24/09 em todos os campos, resolvendo o padrão de duplicação que persistia há semanas nesta série
  - Indicadores sintéticos internos (`indicators`), série completa 21-25/09 recalculada sobre os fechamentos agora confirmados: ratio Far/Soj 83,22% (21/09) → 83,90% (22/09) → 84,36% (23/09) → **84,80% (24/09, pico da série)** → **84,23% (25/09, recuo de -0,57 p.p.)**; oil share 47,81% (22/09) → 47,78% (23/09) → **47,56% (24/09, mínima)** → **47,78% (25/09, retorno ao nível de 23/09)**; crush margin US$2,3716 (22/09) → 2,4323 (23/09) → **2,4483 (24/09, pico)** → **2,4134 (25/09)**; oil-meal spread -0,6842 (22/09) → -0,6941 (23/09) → **-0,7623 (24/09, mínima)** → **-0,693 (25/09)**; margem de biodiesel US US$2,2131 (22/09) → 2,0557 (23/09) → 2,0290 (24/09) → **US$1,8584 (25/09, nova mínima da janela)**; ISF (Índice de Sobra de Farelo) 60/100 e ISO (Índice de Suporte do Óleo) 80/100 seguem travados, agora com carimbo adicional em **2026-09-26** repetindo os mesmos valores; paridade BR da soja R$149,50 (22/09) → 149,39 (23/09) → 150,44 (24/09) → **R$151,30/saca (25/09)**, CBOT 1.320,00 × USD/BRL 5,1991
  - BCB PTAX — **2026-09-25**: USD/BRL **5,1991** (+0,38% frente aos 5,1795 de 24/09), quarta alta consecutiva do dólar desde 21/09 (5,1117 → 5,1161 → 5,1414 → 5,1795 → 5,1991, +1,71% acumulado), EUR/BRL 5,928, Selic diária 0,050788% a.a. (séries SGS 1, 21619, 11)
  - CEPEA/ESALQ Soja Paranaguá (via NAG) — **2026-09-25**: R$161,00/saca (-0,52% frente a 24/09, a maior queda diária desta janela), interrompendo três altas seguidas; soja Paraná interior (CEPEA/ESALQ via NAG) R$154,38/saca (-0,47%) — spread Paranaguá−interior R$6,62/saca (era R$6,73 em 24/09, -1,6%); basis físico real (Paranaguá menos paridade CBOT-implícita) recuou de R$11,40/saca (24/09) para **R$9,70/saca (25/09), -14,9%**, mesmo com a paridade CBOT subindo — sinal de que o físico não acompanhou a alta de Chicago e do câmbio na mesma proporção
  - NAG físico BR (`nag_fisico`) — **2026-09-25**: farelo Mato Grosso/IMEA **R$1.996,41/ton (+0,71%)** — a primeira variação real depois de cinco leituras seguidas travadas em R$1.982,28 (18, 21, 22, 23 e 24/09), resolvendo a favor do mercado físico a suspeita de fonte parada levantada nas duas últimas leituras; farelo Rondonópolis/MT (BCSP) **R$2.200,00/ton, var 0,0% — quinta leitura seguida** (21 a 25/09), o patamar mais consolidado desta série; farelo média Rio Grande do Sul (Clicmercado) **R$2.130,00/ton, var 0,0% — terceira leitura seguida** no novo patamar (23, 24 e 25/09), reforçando que o salto de +14,52% de 23/09 é estrutural, não ruído; prêmio export farelo Paranaguá 0,12 USD/short_ton (congelado há **17 dias corridos**, desde 08/09, no dado mais recente de 25/09); prêmio export óleo Paranaguá 0,1 cts/lb (mesmo congelamento)
  - CFTC COT Managed Money — **novo corte de 2026-09-22** (o primeiro em dez dias, chegando afinal): farelo net long **191.087 → 191.087 contratos, +4,36%** frente aos 183.111 de 15/09 (long 202.722, +3,84%; short 11.635, -3,97%; open interest 657.637, -3,78%); óleo net long **92.137 contratos, -9,21%** frente a 101.480 de 15/09 (long 119.764, -5,22%; short 27.627, +11,02%; OI 605.458, -0,08%); soja net long **265.159 contratos, +9,80%** frente a 241.501 de 15/09 (long 300.742, +6,43%; short 35.583, -13,38%; OI 1.114.328, +0,86%) — a reversão de soja supera inclusive o patamar implícito de 08/09 (~257.258), fechando a "semana de redução" citada nas leituras anteriores; produtores (hedge comercial) reduziram short em farelo (431.785, -3,01% frente a 445.202) e em óleo (369.724, -4,10% frente a 385.536), mas ampliaram short em soja (650.281, +2,24% frente a 636.056)
  - USDA Crop Progress — sem corte novo, ainda o de **2026-09-20** (agora 6 dias de idade): 12% excelente / 46% boa (G/E 58%), 10% pobre, colheita 12% concluída; próximo corte esperado por volta de 27-28/09
  - USDA WASDE — **nenhuma linha aparece no dump de hoje** (nenhuma edição, nem antiga nem nova) — a seção que na leitura de ontem ainda citava a edição de 11/09 desapareceu por completo desta janela de 14 dias, ver Honestidade
  - NOPA — item de fila `release-nopa-2026-09-26`: `monthly_status` em 0,0 bool (paywall, sem dado novo, mesmo padrão de todas as leituras desde o início deste monitoramento)
  - ABIOVE projeções mensais — balanços out-dez/2026, sem revisão nesta janela frente à leitura de ontem: produção de farelo BR caindo 2.142,97 (out) → 1.977,59 (nov) → 1.659,04 (dez) mil t; exportação de farelo BR caindo 850 → 800 → 700 mil t; estoque final de soja BR caindo 5.720,77 (out) → 3.658,99 (nov) → 1.889,91 (dez) mil t
  - Notícias Agrícolas/Canal Rural/Farm Progress (RSS) — manchete mais recente com corpo de texto ainda é a de **2026-09-25** (Farm Progress): "Late-season rain offers final soybean yield bump" (https://www.farmprogress.com/soybean/late-season-rain-offers-final-soybean-yield-bump) — chuva tardia sustentando o potencial de produtividade da safra americana; a manchete "USDA Exports: China buys soybeans" (24/09), citada ontem, segue sem tonelagem ou contraparte; contagem de 26/09 registra 160 itens lidos e apenas 2 mantidos, nenhum com corpo novo
  - CEPEA RSS — contagem de itens recua para 104 em 26/09 (de 106 em 25/09), sem corpo de headline novo; a última manchete com texto completo segue sendo a de 18/09
  - NOAA CPC ENSO — El Niño Advisory, inalterado (carimbo 2026-09-26) — regime historicamente associado a chuvas acima da média no sul do Brasil, um pano de fundo estrutural de oferta que tende a favorecer a safra 2026/27, coerente com a manchete de 19/09 sobre a Conab projetando novo recorde de produção brasileira
  - MPOB — carimbo 2026-09-26, parser sem números extraídos (mesma barreira há semanas)
  - INMET — previsão para **2026-09-26 (HOJE)**: calor segue intenso no núcleo de Mato Grosso — Sinop 40°C/24°C, Lucas do Rio Verde 39°C/25°C (ambos com "possibilidade de chuva isolada"), Cuiabá e Sorriso 38°C, Rio Verde/GO 35°C; o calor agora também se espalha ao Paraná (Cascavel e Maringá, ambos 33°C, ante 29-30°C em 25/09) e Passo Fundo/RS chega a 30°C com "possibilidade de chuva isolada" — nenhuma menção de geada; período coincide com a fase de plantio da safra 2026/27, ainda não crítico para produtividade
  - system/tributario_watch.toml (lido como referência, não editado) — `atualizado_em` 2026-06-05 em todos os 10 eventos catalogados, **113 dias corridos** sem revisão humana frente a hoje (26/09)
  - Forecasts estatísticos internos (bandas 7d/30d) — geração de **2026-09-26**, sobre o fechamento de 25/09 (o mesmo que alimenta esta leitura), alvos 03/10 e 26/10: viés "altista" em farelo nos dois horizontes e em soja no horizonte de 30d (7d em "lateral"); óleo em "baixista" nos dois horizontes — extrapolação estatística, não fundamentalista (ver Honestidade)
  - Fila de julgamento — 2026-09-26, 7 itens: `alerta-quebra_resistencia-soja_cbot-2026-09-25`, `alerta-quebra_suporte-oleo_cbot-2026-09-25`, `alerta-quebra_resistencia-farelo_cbot-2026-09-25`, `alerta-quebra_suporte-complexo_soja-2026-09-25`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`, `release-nopa-2026-09-26`
  - Cruza com [[2026-09-25_leitura-complexo]] (leitura de ontem, base de comparação para toda a revisão de dados desta série), [[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]] e [[2026-09-24_correcao-numeros-sessao-23set-fim-do-artefato-de-baixa-liquidez]] (documentação do padrão de captura parcial reencontrado e agora resolvido), [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (tese original do ratio) e [[2026-09-17_ratio-far-soj-supera-nivel-de-abertura-da-tese-original-quarta-sessao]] e [[2026-09-09_d90-ratio-far-soj-reverte-na-vespera]] (invalidação técnica já fechada da tese de junho)
status: ativa
vies: [bull-farelo, bull-soja, bear-oleo_soja]
---

## Visão geral

O complexo soja gira em torno do "crush" — o esmagamento industrial que separa a soja em
grão em dois produtos com destinos econômicos diferentes: farelo (o resíduo proteico,
usado quase todo em ração animal, sobretudo aves e suínos) e óleo (usado em alimentação
humana e, cada vez mais, em biodiesel). Quem manda no crush é definido pelo "oil share" —
a fatia do valor total gerado pelo esmagamento que vem do óleo. Quando o oil share é alto,
a indústria esmaga soja atrás do valor do óleo, e o farelo sai como subproduto que precisa
ser escoado a qualquer preço, pressionando seu preço relativo para baixo; quando o oil
share cai, o farelo passa a pagar a conta do esmagamento e o óleo perde protagonismo. O
termômetro dessa disputa é o ratio Far/Soj — o preço do farelo dividido pelo da soja, em
percentual: abaixo de 80% o farelo está "abundante" (baixista); entre 80% e 87%, "neutro";
acima de 87%, "apertado" (altista para o farelo).

**O que muda hoje, em primeiro lugar, é uma confirmação de dado, não uma nova sessão de
mercado.** A leitura de ontem ([[2026-09-25_leitura-complexo]]) já havia sinalizado, com
uma reserva explícita, que a abertura, a máxima, a mínima e o volume do farelo e do
heating oil na sessão de 25/09 eram idênticos aos de 24/09 — só o "fechamento" mudava —,
um padrão de captura parcial já visto três vezes antes nesta série
([[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]]). O dump de hoje resolve essa
suspeita e confirma que ela estava correta: a sessão de 25/09 chega agora com volume
plenamente saudável (soja 180.479, farelo 94.390, óleo 99.658 contratos — o maior volume
de toda esta janela de cinco sessões) e com um OHLC totalmente distinto do de 24/09. Mas a
revisão não afetou só o dia 25 — o próprio dia 24/09, que ontem ainda aparecia com volume
de apenas 830 contratos em farelo, hoje aparece com **96.901 contratos** e um fechamento
diferente (372,40, contra os 371,20 mostrados ontem). Ou seja: os dois últimos dias
inteiros de dados de farelo e heating oil que esta série vinha usando eram provisórios, e
só agora, com a geração de hoje, ambos se consolidam.

**Isso muda a história fina do complexo, mesmo sem mudar sua direção estrutural.** Com os
números provisórios de ontem, o ratio Far/Soj parecia estar em sua quarta alta consecutiva
(83,22% → 83,90% → 84,36% → 84,59% → 84,64%), a distância mais curta já registrada ao teto
"apertado" de 87%. Com os números confirmados de hoje, a trajetória real é outra: o ratio
**picou em 84,80% no dia 24/09** — mais alto do que o número provisório de ontem sugeria
para aquele dia — **e recuou para 84,23% no dia 25/09** — mais baixo do que os 84,64%
provisórios. O mesmo padrão de "pico em 24/09, recuo em 25/09" se repete, em espelho, no
oil share (mínima de 47,56% em 24/09, retorno a 47,78% em 25/09), no crush margin (pico de
US$2,4483 em 24/09, recuo a US$2,4134 em 25/09) e no oil-meal spread (mínima de -0,7623 em
24/09, recuo a -0,693 em 25/09). E o mesmo vale para a margem de biodiesel americana: a
leitura de ontem, usando o HO=F provisório, registrava um "repique" de +0,53% no dia 25/09
— hoje, com o HO=F confirmado (fechamento 4,5799, ante os 4,5171 do dado provisório),
essa margem sai negativa: **US$1,8584/galão, uma queda de -8,41% frente aos US$2,0290
confirmados de 24/09**, e a nova mínima de toda a janela. O "repique" de ontem não
sobreviveu à revisão — o padrão real é de queda, não de recuperação.

**A segunda mudança relevante de hoje é a chegada do corte de COT (Commitments of
Traders, o relatório semanal da CFTC que mostra como os fundos — "managed money" — estão
posicionados) referente a 22/09**, o primeiro em dez dias e o evento de posicionamento
mais aguardado pelas duas últimas leituras. Ele confirma e amplia a tese de farelo (net
long dos fundos sobe **+4,36%** frente a 15/09), aprofunda a tese de baixa em óleo (net
long cai **-9,21%**, o maior movimento relativo das três pernas) e, o mais notável,
**reverte com força a redução de convicção em soja que vinha sendo destacada como o único
sinal fraco da tese altista**: o net long em soja sobe **+9,80%**, superando inclusive o
patamar implícito de 08/09. Essa combinação — fundos comprando farelo e soja, vendendo
óleo — é o alinhamento de posicionamento mais coerente com a tese de preço já descrita
nesta série em várias leituras anteriores, e é a razão concreta pela qual a soja migra
hoje de neutro para bull.

**Leitura de uma linha**: o pivô do complexo continua sendo o ratio Far/Soj, agora em
84,23% depois de picar em 84,80% — uma pausa que a confirmação de dado revela ser real,
não uma reversão de tendência, porque o COT de 22/09 mostra os fundos ainda comprando
farelo e vendendo óleo no mesmo período. Maior convicção em bull-farelo, reforçada por
confirmação física tripla (Rondonópolis, RS e agora o IMEA, que finalmente se moveu) e
por posicionamento de fundos; convicção crescente em bear-óleo, com a margem de biodiesel
confirmando queda (não repique) e o COT mostrando o corte mais agressivo de net long das
três pernas; soja passa a bull, sustentada pela reversão de COT e pela paridade em reais
subindo, mas com uma reserva nova sobre o basis físico, que comprimiu enquanto o CBOT e o
câmbio subiam. Trata as quatro quebras técnicas da fila
(`alerta-quebra_resistencia-soja_cbot-2026-09-25`, `alerta-quebra_suporte-oleo_cbot-2026-09-25`,
`alerta-quebra_resistencia-farelo_cbot-2026-09-25`, `alerta-quebra_suporte-complexo_soja-2026-09-25`)
nas seções abaixo, com os valores agora confirmados; as duas revisões "vencidas" da tese
de junho (`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` e `-D+90`)
na seção Farelo, ambas já fechadas desde 17/09; e o release de NOPA
(`release-nopa-2026-09-26`) na seção Honestidade, mais uma vez sem dado real por trás do
paywall.

## Soja

**Viés: bull — mudança frente ao neutro de ontem, sustentada pela reversão de convicção
dos fundos no COT de 22/09 (o dado novo mais forte desta leitura) e pela paridade em reais
em alta pelo quarto pregão seguido, com uma reserva concreta sobre a compressão do basis
físico em Paranaguá.**

O que sustenta a tese:

- **O corte de COT de 22/09 (CFTC, primeiro corte em dez dias) mostra os fundos com net
  long em soja de 265.159 contratos, alta de +9,80% frente aos 241.501 de 15/09** — a
  reversão completa da redução de -6,13% que a leitura de 25/09 havia identificado como o
  único sinal fraco da tese altista, e que agora supera até o patamar implícito de 08/09
  (~257.258 contratos). A composição também ajuda: managed money long subiu +6,43% (para
  300.742) e o short caiu -13,38% (para 35.583) — o corte veio tanto de compra nova quanto
  de fechamento de posições vendidas, o sinal mais limpo de convicção comprada renovada. Do
  lado comercial, os produtores (hedge natural do produtor físico) ampliaram o short em
  +2,24% (para 650.281) — coerente com mais originação/venda física à medida que a colheita
  americana avança (12% concluída em 20/09, USDA Crop Progress).
- **A soja fechou confirmadamente em 1.320,00 hoje (dado revisado da sessão de 25/09,
  CME CBOT), folgadamente acima da resistência de referência de 1.180,00** (fila
  `alerta-quebra_resistencia-soja_cbot-2026-09-25`) — uma folga de **+11,86%**, a maior
  desta série, e um fechamento superior ao provisório de 1.316,75 usado na leitura de
  ontem (+0,25%).
- **A paridade em reais da soja subiu para R$151,30/saca hoje** (CBOT 1.320,00 × USD/BRL
  5,1991), a quarta alta seguida (R$149,50 em 22/09 → 149,39 em 23/09 → 150,44 em 24/09 →
  **151,30** hoje, +1,20% acumulado) — combinando CBOT em alta com real mais fraco: o
  dólar subiu pelo quarto pregão seguido frente ao real (5,1117 em 21/09 → 5,1991 em
  25/09, +1,71% acumulado, BCB PTAX), reforçando a paridade em cima de dois vetores
  simultâneos, não apenas um.
- **A curva futura permanece em contango regular**: nov/26 (base) 1.320,00 → jan/27
  1.333,00 → mar/27 1.339,50 → mai/27 1.346,75 → jul/27 1.351,00 (CME CBOT, 25/09) — o
  mercado a termo segue precificando preços mais altos à frente.
- **A curva de crop progress (corte de 20/09, agora 6 dias de idade) segue mostrando
  condição estável em G/E 58%** — a safra americana não deteriorou na reta final do
  ciclo, com a colheita avançando (12% concluída).

**O que invalida / risco:**

- **O basis físico em Paranaguá comprimiu -14,9% em uma única sessão** (R$11,40/saca em
  24/09 para **R$9,70/saca em 25/09** — o preço físico de Paranaguá caiu -0,52% no mesmo
  dia em que a paridade CBOT-implícita subiu +0,57%). Isso é um sinal de divergência: o
  mercado físico brasileiro não acompanhou a alta de Chicago e do câmbio na mesma
  proporção — possivelmente reflexo de mais oferta física entrando no canal de exportação
  (fim de safra/estoques de passagem) ou de demanda de exportação mais fraca na margem. O
  spread Paranaguá-Paraná interior também comprimiu (R$6,73 para R$6,62/saca, -1,6%).
- **Manchete nova de Farm Progress (25/09): "Late-season rain offers final soybean yield
  bump"** — chuva tardia sustentando o potencial de produtividade da safra americana, um
  contraponto direto à tese altista: mais chuva na reta final do ciclo tende a reforçar
  produtividade, não reduzi-la. Sem número de bushels/acre no dump, mas o sentido
  qualitativo pesa contra o lado comprado.
- **A manchete "China buys soybeans" (24/09, Farm Progress), tratada ontem como o dado
  potencialmente mais relevante da semana, segue sem tonelagem ou contraparte** — dois dias
  depois, ainda não é possível avaliar se foi um lote residual ou uma retomada de peso.
- **O regime de El Niño (NOAA CPC, inalterado) é historicamente associado a chuvas acima
  da média no sul do Brasil**, um pano de fundo estrutural que tende a favorecer a
  produtividade da safra brasileira 2026/27 — coerente com a manchete de 19/09 da Conab
  projetando novo recorde de produção. Este é um vetor de médio prazo (safra que só será
  colhida a partir de janeiro/27), mas pesa contra qualquer tese de escassez estrutural de
  soja no horizonte 2026/27.
- **O WASDE, fonte-chave de balanço de oferta e demanda, desapareceu por completo do dump
  de hoje** — nenhuma edição aparece, nem mesmo a defasada de 11/09 citada ontem. Sem esse
  insumo, a leitura de soja fica mais dependente de COT e técnico, e menos de fundamento de
  balanço direto (ver Honestidade).
- **Nível técnico a vigiar:** um fechamento de volta abaixo de 1.180 desfaria formalmente o
  rompimento; com a folga em +11,86%, esse cenário segue distante.

**Leitura operacional:** a mudança de convicção nos fundos (COT de 22/09) é o dado mais
forte para o lado comprado desde que este monitoramento começou a registrar redução de net
long em soja — reverte a única fragilidade identificada na leitura anterior e vem
acompanhada de paridade em reais em alta por vetores duplos (CBOT + câmbio). Para quem está
comprado, isso é reforço concreto para manter ou ampliar a posição estrutural, com o nível
técnico de 1.180 como referência de invalidação distante. Para quem opera vendido, a
compressão do basis físico em Paranaguá e a manchete de chuva favorável nos EUA são os
únicos fios de argumento no momento — nenhum dos dois é, por si, um gatilho técnico de
reversão, mas ambos merecem monitoramento nos próximos dias, especialmente se o basis
continuar comprimindo com o CBOT subindo (um sinal de que o físico brasileiro pode estar
mais fraco do que a tela sugere). O spread Far/Soj segue sendo a forma mais limpa de expor
a diferença entre as duas pernas sem tomar risco direcional puro em soja.

## Farelo

**Viés: bull, mantido — a confirmação de dado de hoje revela que o pico do ratio Far/Soj
foi maior do que se pensava (84,80% em 24/09, não 84,64%) e que o recuo de 25/09 (84,23%)
é uma pausa dentro de uma tendência que o COT de 22/09 confirma que os fundos ainda
compram, não uma reversão.**

O que sustenta a tese:

- **O corte de COT de 22/09 mostra os fundos ampliando net long em farelo para 191.087
  contratos, alta de +4,36% frente aos 183.111 de 15/09** — o quinto dado de posicionamento
  consecutivo apontando na mesma direção desde que esta série começou a monitorar o tema. A
  composição é limpa: managed money long subiu +3,84% (para 202.722) e o short caiu -3,97%
  (para 11.635); o open interest total caiu -3,78% (para 657.637), sugerindo que parte do
  movimento veio de liquidação de posições vendidas por outros participantes, não apenas de
  compra nova de fundos. Do lado comercial, os produtores reduziram short em -3,01% (para
  431.785) — coerente com menos pressão vendedora física, o espelho do aperto de oferta
  doméstica de farelo.
- **O ratio Far/Soj, com os números agora confirmados, picou em 84,80% no dia 24/09** —
  mais alto do que qualquer leitura provisória já registrada nesta série — **e recuou para
  84,23% no dia 25/09**, ainda a apenas **2,77 pontos percentuais** do teto "apertado" de
  87% e a 4,23 pontos do piso "abundante" de 80%. Isso mantém o ratio **+2,83 pontos
  percentuais** acima do nível de abertura da tese baixista original de 11/06/2026 (81,4%,
  [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]) — trata
  `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` e `-D+90`: ambas
  seguem aparecendo como "vencidas" na fila de hoje, mas o veredito de ambas já está
  fechado desde
  [[2026-09-17_ratio-far-soj-supera-nivel-de-abertura-da-tese-original-quarta-sessao]] e
  reafirmado pela revisão formal de D+90 em
  [[2026-09-09_d90-ratio-far-soj-reverte-na-vespera]]. Nenhuma ação nova é necessária sobre
  essas duas revisões específicas; resta em aberto apenas o marco de D+180, programado para
  2026-12-08.
- **O físico de farelo do Mato Grosso/IMEA finalmente se moveu hoje: R$1.996,41/ton,
  +0,71%** — a primeira variação real depois de cinco leituras seguidas travadas em
  R$1.982,28 (18 a 24/09), resolvendo a favor do mercado a suspeita de fonte parada que as
  duas últimas leituras haviam levantado. Com esse movimento, a confirmação física do
  aperto de farelo no Brasil passa a vir de **três praças distintas e agora todas ativas**
  (Rondonópolis em R$2.200/ton pela quinta leitura seguida, RS em R$2.130/ton pela terceira
  leitura seguida, e IMEA subindo depois de cinco leituras estáveis).
- **O oil share caiu para uma mínima de 47,56% em 24/09**, mais baixo do que qualquer
  leitura provisória anterior, antes de recuar a 47,78% em 25/09 (mesmo nível de 23/09) —
  ainda assim, o farelo segue respondendo por mais da metade do valor gerado no crush.
- **O oil-meal spread atingiu -0,7623 USD/bushel em 24/09**, o extremo mais negativo já
  registrado nesta série, antes de recuar a -0,693 em 25/09 — a distância entre o valor do
  farelo e o do óleo, em termos de bushel-equivalente, segue historicamente ampla mesmo
  após o recuo.
- **O farelo fechou confirmadamente em 370,60 na sessão de 25/09, folgadamente acima da
  resistência histórica de 325,00** (fila `alerta-quebra_resistencia-farelo_cbot-2026-09-25`),
  folga de **+14,03%**.
- **A trajetória sazonal da ABIOVE para o Brasil continua apontando para alívio de oferta
  doméstica de farelo à frente**, sem revisão nesta janela: produção projetada caindo de
  2.142,97 mil t (out/26) para 1.977,59 (nov/26) e 1.659,04 mil t (dez/26); exportação de
  850 para 800 e 700 mil t no mesmo período — um vetor de médio prazo que, se confirmado,
  tende a sustentar o ratio Far/Soj em patamares elevados à frente.

**O que invalida / risco:**

- **O ratio recuou 0,57 ponto percentual entre 24/09 e 25/09 (84,80% → 84,23%)** — a
  primeira pausa real desta série depois de uma sequência de altas. Isoladamente, uma única
  sessão de recuo não desfaz a tendência, especialmente com o COT de 22/09 confirmando
  fundos ainda comprando farelo, mas é o primeiro dado, desde que este monitoramento
  começou a acompanhar o ratio diariamente, que aponta para baixo em vez de para cima — vale
  a pena checar se a sessão seguinte confirma continuação da alta ou um início de reversão.
- **O prêmio de exportação de farelo em Paranaguá segue congelado em 0,12 USD/short_ton há
  17 dias corridos** (desde 08/09) — se o aperto físico doméstico fosse amplo e sustentado
  a ponto de pressionar também o canal de exportação, seria razoável esperar, eventualmente,
  algum reflexo no FOB; essa confirmação ainda não apareceu.
- **A curva futura de farelo segue em backwardation (inversão)**: dez/26 (base) 370,60 →
  jan/27 369,40 → mar/27 368,20 → mai/27 368,00 (-0,70% de dez/26 a mai/27) — o mercado a
  termo segue sem precificar um aperto estrutural que se estenda indefinidamente, coerente
  com a trajetória sazonal de alívio de oferta da ABIOVE.
- **Os índices sintéticos ISF e ISO seguem travados em 60/100 e 80/100**, agora também com
  um carimbo repetido em 26/09 — mais de quinze dias corridos sem qualquer reação, apesar
  de o ratio e o oil share terem se movido de forma expressiva nesse período.
- **O open interest total de farelo caiu -3,78% entre 15/09 e 22/09** — parte do movimento
  de alta do net long dos fundos pode refletir liquidação de posições vendidas de outros
  participantes (produtores, por exemplo, que também reduziram short em -3,01%) mais do que
  entrada líquida de capital novo no mercado.

**Leitura operacional:** a tendência estrutural de farelo mais forte, relativamente, do que
a soja segue intacta, e o COT de 22/09 é a confirmação de posicionamento que faltava — os
fundos seguem comprando farelo mesmo depois do pico técnico de 24/09. Para quem está
comprado no spread Far/Soj (a forma mais limpa de capturar esta tese), a recomendação
operacional é manter a posição: a tendência de fundo (IMEA finalmente confirmando o aperto,
Rondonópolis e RS consolidados, COT ainda comprador) é mais forte do que uma única sessão
de recuo no ratio. Para quem está comprado em farelo direcionalmente, o nível técnico
(370,60, folga de +14,03% sobre a resistência de 325) segue amplamente favorável. Para quem
está vendido, tanto o nível técnico quanto o calendário sazonal da ABIOVE seguem
desfavoráveis à tese de queda; a inversão da curva futura nos meses mais distantes e o
prêmio de exportação congelado são os únicos argumentos a favor de cautela em posições
compradas de prazo mais longo. O recuo do ratio em 25/09 é o primeiro ponto de dado a
monitorar de perto na próxima sessão — se se repetir, passa a merecer tratamento como
possível início de reversão, não apenas pausa.

## Óleo

**Viés: bear, reforçado — o COT de 22/09 traz a confirmação de posicionamento que faltava
(o corte mais agressivo de net long das três pernas do complexo), e a margem de biodiesel
americana, agora com dado confirmado, cai em vez de subir como o número provisório de
ontem sugeria.**

O que sustenta a tese:

- **O corte de COT de 22/09 mostra os fundos cortando net long em óleo para 92.137
  contratos, queda de -9,21% frente aos 101.480 de 15/09** — o maior movimento relativo
  entre as três pernas do complexo nesta rodada de COT, e uma reversão do que vinha sendo
  ampliação de net long nas semanas anteriores. A composição reforça o sinal bear: managed
  money long caiu -5,22% (para 119.764) e o short subiu +11,02% (para 27.627) — fundos
  reduzindo posição comprada e abrindo posição vendida ao mesmo tempo, não apenas realizando
  lucro parcial.
- **A margem de biodiesel americana, com o HO=F agora confirmado, fechou em US$1,8584/galão
  em 25/09 — uma queda de -8,41% frente aos US$2,0290 confirmados de 24/09**, e a nova
  mínima de toda a janela de cinco sessões (2,0908 em 21/09 → 2,2131 em 22/09 → 2,0557 em
  23/09 → 2,0290 em 24/09 → **1,8584** em 25/09). Isso inverte a leitura de ontem, que — com
  o HO=F ainda provisório — registrava um "repique" de +0,53% no dia; a versão confirmada
  mostra o oposto: queda acelerando, não recuperação. O heating oil em si caiu -3,18% entre
  24/09 e 25/09 (fechamento confirmado 4,5799, ante 4,7303 em 24/09) — a fonte primária da
  margem se deteriorou de fato, não por artefato de captura.
- **Óleo fechou confirmadamente em 67,82 na sessão de 25/09, abaixo do suporte de
  referência de 72,00** (fila `alerta-quebra_suporte-oleo_cbot-2026-09-25`), distância de
  **-5,81%** — abaixo do suporte há pelo menos cinco sessões consecutivas, a mesma
  contagem já indicada pela leitura de ontem, agora sobre um fechamento revisado que
  confirma a mesma conclusão.
- **O oil share atingiu uma mínima de 47,56% em 24/09** antes de recuar a 47,78% em 25/09 —
  mesmo com o recuo, o óleo segue respondendo por menos da metade do valor gerado no crush.
- **O oil-meal spread atingiu -0,7623 USD/bushel em 24/09**, o extremo mais negativo já
  registrado nesta série — o óleo cada vez mais atrás do farelo em valor por
  bushel-equivalente, mesmo após o recuo parcial a -0,693 em 25/09.
- **O ISO (Índice de Suporte do Óleo) segue em 80/100**, sem melhora, com carimbo repetido
  em 26/09.
- **O forecast estatístico interno segue em "baixista" nos dois horizontes (7d e 30d)** —
  extrapolação de tendência, não fundamentalista, mas coerente com a deterioração real do
  oil share e agora também com o COT.
- **A lente fiscal brasileira segue estruturalmente desfavorável, sem mudança hoje**: a MP
  1.363/2026 (subvenção ao diesel fóssil, vigente até 31/12/2026) segue plenamente
  vigente; a isenção de PIS/Cofins do biodiesel na mistura está agora **57 dias corridos
  vencida** (vigência até 31/07/2026) sem sinal de renovação.

**O que sustenta um contraponto:**

- **A curva futura de médio prazo segue em contango regular**: out/26 67,25 → dez/26 (base)
  67,82 → jan/27 68,02 → mar/27 68,25 → mai/27 68,41 (+0,87% de dez/26 a mai/27) — sem
  sinal de reprecificação estrutural de baixa no médio prazo.
- **O RIN D4 (crédito de biocombustível renovável americano) permanece constante na fórmula
  interna** — nenhuma variação real de política regulatória americana explicaria a queda
  de margem de hoje; ela vem inteiramente do lado do heating oil, agora confirmado.
- **Catalisadores de alta represados, ainda não correntes**: B16 (elevação da mistura de
  biodiesel para 16%) segue "adiado", resultado esperado por volta de novembro/2026; a
  centralização da exportação de palma pela Indonésia via Danantara, que tinha alvo de
  assunção plena em 01/09/2026, já soma **25 dias** de atraso sem confirmação — ambos
  seguem como upside represado, não corrente.
- **Os produtores (hedge comercial) reduziram short em óleo em -4,10%** (para 369.724,
  frente a 385.536 em 15/09) — um sinal secundário de menos pressão vendedora física, ainda
  que os fundos especulativos estejam claramente do lado vendedor na margem.

**Leitura operacional:** o quadro técnico (abaixo do suporte de 72,00 há cinco sessões), o
COT (o corte mais agressivo de net long das três pernas) e a margem de biodiesel confirmada
em queda convergem hoje para reforçar a tese vendida, depois de uma leitura de ontem que
havia introduzido dúvida justamente sobre a margem de biodiesel. Para quem está vendido, a
recomendação é manter ou reforçar a posição, apoiada agora em três fontes independentes
(técnico, COT e margem, todas confirmadas) em vez de apenas duas. Para quem está comprado ou
avalia entrar, os catalisadores represados (B16, Danantara) seguem sendo o argumento
central — nenhum se tornou corrente hoje, mas o atraso crescente da Danantara (25 dias) é,
em si, uma fonte de risco de reversão súbita caso a Indonésia anuncie a centralização
plena. Para quem opera o spread farelo-óleo dentro do crush, o oil-meal spread recuou de
sua mínima histórica (-0,7623 em 24/09) para -0,693 em 25/09 — uma zona ainda extrema, mas
que começa a merecer atenção como candidata a mean-reversion caso o recuo continue nas
próximas sessões.

## Spreads e crush (leitura de complexo)

O ratio Far/Soj, com os números agora confirmados, mostra uma trajetória de pico e recuo
que os dados provisórios de ontem não revelavam: 83,22% (21/09) → 83,90% (22/09) → 84,36%
(23/09) → **84,80% (24/09, pico da série)** → **84,23% (25/09)** — ainda dentro da zona
neutra (80-87%), mas a 2,77 pontos percentuais do teto "apertado" e a 4,23 pontos do piso
"abundante". O oil share espelha o mesmo movimento: mínima de 47,56% em 24/09, recuo a
47,78% em 25/09. O crush margin segue abaixo do piso de referência de US$2,50 monitorado
pela fila (`alerta-quebra_suporte-complexo_soja-2026-09-25`, fechamento confirmado de
US$2,4134, distância de **-3,46%**), depois de picar em US$2,4483 em 24/09 — o mesmo
padrão de pico-e-recuo presente em todos os quatro indicadores sintéticos do crush
simultaneamente.

**A leitura de complexo mais importante de hoje é que esse pico-e-recuo, sozinho, não
seria suficiente para mudar a tese — mas o COT de 22/09, chegando no mesmo dia, resolve a
ambiguidade a favor da continuidade, não da reversão.** Os fundos ampliaram net long em
farelo (+4,36%) e cortaram net long em óleo (-9,21%) na mesma semana em que o ratio Far/Soj
atingia seu pico da série (24/09) — ou seja, o posicionamento dos fundos estava sendo
construído exatamente na direção que a série já vinha documentando, e o recuo do dia
seguinte (25/09) é mais consistente com uma pausa técnica normal do que com um sinal de que
os fundos estejam revertendo convicção. Os dois índices compostos por contagem de condições
— ISF (60/100) e ISO (80/100) — seguem travados no mesmo patamar desde 11/09, agora também
com um carimbo repetido em 26/09, mais de quinze dias corridos sem qualquer reação, apesar
de o ratio e o oil share terem se movido de forma expressiva e consistente nesse período —
o lembrete de sempre nesta série de que esses índices específicos reagem a mudanças de
regime estrutural, não a oscilações de curto e médio prazo dentro da mesma faixa.

**O segundo ponto de complexo é metodológico**: a confirmação de hoje fecha, pela quarta
vez, o ciclo de suspeita-e-confirmação que esta série já documentou repetidamente desde
[[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]] — dado provisório com OHLC
duplicado e volume anormalmente baixo aparece em uma geração do dump, e a geração seguinte
o substitui por um dado com volume saudável e OHLC distinto. Desta vez, o padrão afetou
dois dias inteiros (24/09 e 25/09) simultaneamente, e a magnitude da revisão foi
relativamente pequena em termos de preço (farelo 371,20→372,40 em 24/09, +0,32%; farelo
371,50→370,60 em 25/09, -0,24%) mas enorme em termos de volume (mais de cem vezes maior em
ambos os dias). O aprendizado operacional segue o mesmo de sempre: tratar o fechamento do
dia mais recente do dump como provisório até a geração seguinte confirmar, especialmente
quando o volume está muito abaixo do padrão histórico da mesma janela.

## Lente fiscal/regulatória BR

Antes de fechar qualquer tese de preço BR, os vetores tributários/regulatórios vivos que
pesam no complexo — todos do `system/tributario_watch.toml`, cujo carimbo mais recente
(`atualizado_em`) em todos os 10 eventos catalogados é 2026-06-05, ou seja, **113 dias
corridos sem revisão humana** frente a hoje (26/09), um dia a mais do que ontem:

- **MP 1.363/2026** (id `MP-1363-2026`, subvenção diesel fóssil R$1,12/L, vigente até
  31/12/2026): barateia o diesel fóssil no mix B15 (mistura obrigatória de 15% de
  biodiesel), reduzindo a competitividade relativa do biodiesel e a demanda doméstica por
  óleo de soja — vetor estrutural de baixa para óleo, plenamente vigente, sem mudança de
  status.
- **B16 (id `B16-CNPE-2026`, elevação da mistura obrigatória de biodiesel para 16%)** segue
  "adiado", resultado esperado por volta de novembro/2026. Upside represado (~436 mil
  toneladas de demanda potencial adicional de óleo), não corrente.
- **Isenção de PIS/Cofins do biodiesel na mistura** (id `PISCOFINS-BIODIESEL-ISENCAO`):
  vigência registrada até 31/07/2026 — já **57 dias corridos vencida** frente a
  26/09/2026, sem registro de prorrogação ou expiração.
- **MP 1.358/2026** (subvenção gasolina R$0,89/L): vigência registrada até 11/07/2026,
  agora **77 dias corridos vencida**.
- **STJ REsp 2.165.276** (id `STJ-RESP-2165276`, crédito de PIS/Cofins sobre soja em
  biodiesel, direção "alta" para soja/óleo): sem novidade nesta janela.
- **EPA RFS 2026/2027** (id `EPA-RFS-2026-2027`, mandato de biocombustível americano,
  direção "alta" para óleo): sustenta o RIN D4, estável, e o RIN permanece constante na
  fórmula interna de margem de biodiesel usada por este sistema — a queda de margem de
  hoje vem inteiramente do heating oil (agora confirmado), não de mudança regulatória.
- **Crédito 45Z** (id `45Z-CLEAN-FUEL`, em tramitação, direção "mista"): sem novidade.
- **Indonésia — Danantara** (id `DANANTARA-INDONESIA`) e **levy de exportação PMK 9/2026**
  (id `INDONESIA-LEVY-PMK9`): a assunção plena da centralização da exportação de palma
  pela Indonésia tinha alvo 01/09/2026 — já se passaram **25 dias** sem confirmação.
  Catalisador de alta represado para óleo (via substituição com palma) — ainda sem dado de
  MPOB disponível para monitorar diretamente (parser continua quebrado, ver Honestidade).
- **Indonésia B50** (id `INDONESIA-B50`, monitorando, direção "alta"): sem novidade.

Nenhum desses vetores muda a leitura de preço de hoje isoladamente — mas, em conjunto,
eles seguem reforçando a mesma assimetria já descrita em leituras anteriores: o mercado
interno brasileiro tem múltiplos desincentivos correntes ao óleo (MP 1.363 plenamente
vigente, isenção PIS/Cofins já 57 dias vencida) e múltiplos catalisadores de alta
represados, não correntes (B16, Danantara, B50). O óleo brasileiro segue mais fraco
estruturalmente até que algum dos vetores represados vire fato concreto — e a lacuna
crescente de 113 dias sem revisão humana do catálogo tributário é, em si, um risco
operacional recorrente nesta série: qualquer um destes vetores pode ter mudado de status
na realidade sem que este sistema tenha como saber.

## Riscos e eventos próximos

- **Confirmação (ou nova revisão) dos fechamentos de 24/09 e 25/09** — ambos já mudaram uma
  vez entre as gerações de ontem e de hoje; embora o volume atual pareça saudável, ainda não
  há uma terceira geração do dump para confirmar que os valores de hoje são definitivamente
  finais.
- **Se o recuo do ratio Far/Soj em 25/09 (84,80% → 84,23%) se estender por uma segunda
  sessão seguida**, passa a merecer tratamento como possível início de reversão da
  tendência de alta, não apenas pausa técnica — o dado mais importante a vigiar na próxima
  geração do dump.
- **Retorno do WASDE ao dump** — a fonte desapareceu por completo nesta janela; sem ela, a
  leitura de soja e farelo fica mais dependente de COT e técnico.
- **Compressão do basis físico em Paranaguá** (R$11,40 → R$9,70/saca, -14,9% em uma
  sessão) — checar se a divergência entre físico e tela persiste ou se corrige nos
  próximos dias.
- **Tonelagem e contraparte da manchete "China buys soybeans" (24/09, Farm Progress)** —
  sem esse número, a manchete permanece uma indicação qualitativa, não um dado
  operacionalizável.
- **Próximo corte de COT** (posições após 22/09), que deve confirmar se a reversão de
  convicção em soja e o corte em óleo desta rodada são o início de uma nova tendência de
  posicionamento ou um ajuste pontual.
- **USDA Crop Progress**: próximo corte esperado por volta de 27-28/09.
- **Nível técnico a vigiar em farelo:** volta abaixo de 325,00 desfaria o rompimento
  (folga atual +14,03%).
- **Nível técnico a vigiar em soja:** volta abaixo de 1.180,00 desfaria o rompimento
  (folga atual +11,86%).
- **Nível técnico a vigiar em óleo:** recuperação acima de 72,00 desfaria a leitura de
  suporte rompido (distância atual -5,81%).
- **Crush margin:** retorno acima de US$2,50/bushel encerraria a leitura de suporte
  rompido monitorada pela fila (distância atual -3,46%).
- **Prêmio de exportação de farelo e óleo em Paranaguá**, congelado há 17 dias corridos.
- **NOPA mensal**: mais um "release" sem dado novo de fato (paywall), agora referenciado
  como `release-nopa-2026-09-26`.
- **Confirmação da centralização plena da exportação de palma pela Danantara** — alvo
  01/09, já 25 dias passados sem confirmação.
- **Vigência da isenção PIS/Cofins do biodiesel** (57 dias vencida) e **MP 1.358/2026 da
  gasolina** (77 dias vencidos) — checar notícia de renovação/expiração.
- **Marco de 113 dias sem revisão humana do `tributario_watch.toml`**.
- **Revisão de D+180 da tese original do ratio Far/Soj**, programada para 2026-12-08.

## Honestidade

- **O achado central desta leitura é uma confirmação de dado, não uma correção
  isolada, e ela alterou uma conclusão qualitativa da leitura de ontem.** Com o HO=F
  provisório, a leitura de 25/09 havia registrado um "repique" de +0,53% na margem de
  biodiesel; com o HO=F confirmado hoje, a margem cai -8,41% frente ao dia anterior. Isso
  significa que uma conclusão específica da leitura de ontem (o contraponto mais frágil
  daquela análise) não se sustentou — o padrão de captura suspeita, mais uma vez, se
  confirmou como estrutural, mas desta vez sabemos a direção exata do erro que ele
  introduziu (o dado provisório enviesava a leitura para menos bearish em óleo do que a
  realidade).
- **A revisão não afetou apenas o fechamento — afetou o volume por mais de cem vezes e, em
  alguns campos, também a máxima e a mínima.** Farelo em 24/09: volume de 830 para 96.901
  contratos; em 25/09: volume de 830 para 94.390. Isso é consistente com o padrão já
  documentado em [[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]] e
  [[2026-09-24_correcao-numeros-sessao-23set-fim-do-artefato-de-baixa-liquidez]], mas é a
  primeira vez que o padrão afeta dois dias inteiros de uma só vez, e a primeira vez que
  esta série consegue comparar diretamente o "antes" e o "depois" com ambos os números
  documentados em leituras publicadas.
- **O WASDE desapareceu por completo do dump de hoje** — nem a edição defasada de 11/09,
  citada em todas as leituras anteriores desde então, aparece mais. Não está claro se isso
  é uma falha temporária de captura ou uma mudança na disponibilidade da fonte; até a
  próxima geração do dump, esta leitura trata a ausência como um buraco de dado, não como
  "sem novidade".
- **O campo `fechamento_Z26` do farelo, que ontem divergia do campo `fechamento` genérico
  (371,80 vs 371,50), hoje bate exatamente (370,60 em ambos)** — a inconsistência interna
  específica de ontem se resolveu, mas não há confirmação de que o mecanismo que a causou
  não possa se repetir.
- **O IMEA/MT finalmente se moveu depois de cinco leituras travadas**, resolvendo a favor
  do mercado físico a suspeita de fonte parada levantada nas duas últimas leituras — mas
  seguimos sem um segundo movimento independente para confirmar que a nova leitura
  (R$1.996,41/ton) não é, ela mesma, um evento isolado.
- **A manchete "China buys soybeans" (24/09, Farm Progress) e a manchete de chuva tardia
  (25/09) estão disponíveis apenas como título** — sem tonelagem, corpo de texto ou
  contexto adicional, não é possível avaliar o peso real de nenhuma das duas para a tese de
  soja.
- **Percentil histórico de posicionamento COT não está disponível no briefing** — toda
  leitura de "fundos comprando/vendendo" nesta série usa variação absoluta semana a semana
  de contratos, não percentil histórico; não é possível dizer se o net long atual de
  farelo, soja ou óleo está em nível historicamente esticado ou ainda distante de extremos.
- **O item de fila `release-nopa-2026-09-26` é mais uma repetição sem dado novo** — o mesmo
  padrão de todas as leituras anteriores desde que este monitoramento começou (paywall,
  `monthly_status` em 0,0 bool).
- **`tributario_watch.toml` sem atualização há 113 dias corridos** — pelo menos dois
  vetores (isenção PIS/Cofins do biodiesel, MP 1.358/2026) já passaram da vigência
  registrada sem nota de renovação ou expiração.
- **A previsão INMET para 26/09 é previsão meteorológica, não medição de precipitação ou
  temperatura real** — as menções a "possibilidade de chuva isolada" são indicativas do
  boletim, não confirmação de que o evento ocorreu ou ocorrerá.
- **MPOB (palma Malásia) segue com parser quebrado** — nenhum dado de produção/estoque de
  palma malaia disponível, o que impede monitorar diretamente o catalisador represado da
  centralização de exportação indonésia (Danantara).
- **Não há seção `bcba` (Argentina) neste dump** — nenhum dado direto de safra ou
  exportação argentina disponível, e agora também sem WASDE para consolidar indiretamente
  esse dado.
- **Os forecasts estatísticos internos (bandas 7d/30d) foram gerados hoje sobre o mesmo
  fechamento de 25/09 usado nesta leitura** — o viés "altista" em farelo e "baixista" em
  óleo (ambos horizontes) refletem extrapolação estatística de tendência (MA20 +
  volatilidade + slope), não uma reavaliação fundamentalista.
- **Os índices ISF e ISO ganharam um carimbo em 2026-09-26 no dump de hoje**, repetindo os
  mesmos valores de 60/100 e 80/100 já vigentes desde 11/09 — não está claro se isso reflete
  um recálculo real sobre o fechamento mais recente ou apenas uma reafirmação agendada do
  mesmo valor; tratado aqui como continuidade, não como confirmação nova.
- **A fila de julgamento volta a listar as revisões D+7 e D+90 da tese de 11/06 como
  "vencidas"** — o veredito de ambas já foi fechado em
  [[2026-09-17_ratio-far-soj-supera-nivel-de-abertura-da-tese-original-quarta-sessao]] e
  reafirmado em [[2026-09-09_d90-ratio-far-soj-reverte-na-vespera]]; o sistema de fila não
  lê de volta os insights publicados para marcar a revisão como encerrada. Nenhuma ação
  nova é necessária sobre essas duas revisões específicas.
