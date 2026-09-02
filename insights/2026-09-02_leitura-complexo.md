---
data: 2026-09-02
titulo: "Terça-feira (01/09) confirma o rompimento em soja e farelo e finalmente resolve o óleo acima de 72,00 — mas o crush margin segue abaixo do suporte de 2,50 porque é a soja, não o farelo nem o óleo, quem lidera o rali"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT (ZSX26 soja / ZMV26 farelo / ZLV26 óleo) — sessão de 2026-09-01 (terça-feira), a mais recente do pipeline: soja abertura 1.291,25, máxima 1.320,50, mínima 1.290,00, fechamento 1.318,50 USD cts/bushel, volume 175.695 contratos; farelo abertura 337,20, máxima 346,30, mínima 336,10, fechamento 345,10 USD/short ton, volume 23.027 contratos; óleo abertura 71,50, máxima 72,76, mínima 71,50, fechamento 72,38 USD cts/lb, volume 38.557 contratos. Curva futura em 01/09: soja set/26 (U26) 1.304,00, nov/26 (X26, contrato-base) 1.318,50, jan/27 (F27) 1.333,50, mar/27 (H27) 1.337,75, mai/27 (K27) 1.342,50, jul/27 (N27) 1.342,75; farelo set/26 (U26) 342,00, out/26 (V26, contrato-base) 345,10, dez/26 (Z26) 351,90, jan/27 (F27) 354,20, mar/27 (H27) 355,20, mai/27 (K27) 356,40; óleo set/26 (U26) 72,05, out/26 (V26, contrato-base) 72,38, dez/26 (Z26) 72,62, jan/27 (F27) 72,57, mar/27 (H27) 72,54, mai/27 (K27) 72,35
  - CME CBOT — sessão de 2026-08-31 (segunda-feira), reconstruída via `indicators` (Board Crush embutido): soja fechamento 1.288,00 (flat vs sexta), farelo fechamento 338,60 (-1,14% vs sexta), óleo fechamento 70,83 (+0,01% vs sexta)
  - CME NYMEX heating oil (HO=F) — 2026-09-01: abertura 4,7045, máxima 4,7382, mínima 4,7045, fechamento 4,7180 USD/galão, volume 466 contratos (baixo, ver Honestidade); 2026-08-31 só tem abertura 4,4238 no dump (sem fechamento); referência de sexta-feira 28/08 (herdada da leitura anterior): fechamento 4,3567 USD/galão
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, paridade BR, ISF, ISO) — série completa 26/08 a 01/09 usada nesta leitura para reconstruir a trajetória da semana
  - BCB PTAX — 2026-09-01: USD/BRL 5,1570, EUR/BRL 5,9785, Selic diária 0,05166% a.a.; 2026-08-31: USD/BRL 5,1816; 2026-08-28: USD/BRL 5,2005 — três sessões seguidas de valorização do real
  - CEPEA/ESALQ Soja Paranaguá via NAG — 2026-09-01: R$ 161,14/saca (var +1,07%); 2026-08-31: R$ 159,44 (var -0,20%); 2026-08-28: R$ 159,76 (var +3,04%)
  - CEPEA/ESALQ Soja Paraná interior via NAG — 2026-09-01: R$ 153,06/saca (var +1,16%); 2026-08-31: R$ 151,31 (var -0,01%)
  - NAG Físico BR — 2026-09-01: farelo MT/IMEA R$ 1.795,68/ton (var 0,0%, congelado desde 31/08), Rondonópolis/MT R$ 1.900,00/ton (var 0,0%, congelado desde 31/08), RS média R$ 1.860,00/ton (congelado há várias sessões); prêmios export PGUA farelo +0,12 USD/short ton e óleo +0,10 cts/lb, ambos numericamente idênticos desde 24/08/2026 (agora sob rótulo "Setembro/26", mesmo valor de "Agosto/26") — 9 sessões seguidas sem se mexer, ver Honestidade
  - CFTC COT Managed Money, Swap Dealers e Producer/Merchant — corte de 2026-08-25, AINDA o mais recente disponível (nenhum corte novo neste dump); agora 8 dias corridos de defasagem frente ao fechamento de 01/09
  - USDA Crop Progress — corte de 2026-08-30 (12% excelente / 46% boa / 9% ruim), primeira deterioração da safra "boa" em semanas frente a 23/08 (12%/48%/9%)
  - USDA WASDE — segue ausente da janela deste briefing
  - NOPA — fila `release-nopa-2026-09-01` marca um release "novo", mas `monthly_status` segue em 0,0 bool (paywall), sem número de esmagamento americano mensal — ver Honestidade
  - ABIOVE projeções mensais — balanços set-dez/2026, mesmos valores da leitura anterior (estoque final de soja recuando de 7.912,1 mil t em set/26 para 1.889,9 mil t em dez/26)
  - NOAA CPC ENSO — carimbo 2026-09-01 (El Niño Advisory, inalterado desde pelo menos 27/08)
  - MPOB — carimbo 2026-09-01 (3.456 caracteres, parser sem números extraídos, mesma barreira de semanas atrás)
  - BCBA (Argentina) — carimbo 2026-09-01, scraper acessa a página mas não encontra links de relatório detectados (fonte estruturalmente sem dado, não uma falha pontual)
  - INMET — previsão para HOJE, 2026-09-02: núcleo produtor de Mato Grosso ainda quente (35°C em Cuiabá, 39°C em Sinop/Lucas do Rio Verde, 38°C em Sorriso, 34°C em Rio Verde/GO) mas agora com "pancadas de chuva isoladas" em vez do céu limpo dos dias anteriores; Sul com céu mais aberto (Cascavel/PR 24°C/11°C poucas nuvens, Maringá/PR 26°C/12°C poucas nuvens, Passo Fundo/RS 20°C/7°C poucas nuvens) — inversão do padrão de 31/08 (núcleo seco, Sul chuvoso)
  - Notícias Agrícolas/Canal Rural + FarmProgress RSS — 2026-09-01 registra "160 items lidos, 7 mantidos (soja/farelo/oleo)", com dois headlines visíveis: farelo — "Conab publica resultado final de credenciamento para venda de farelo de soja" (Canal Rural) e soja — "Soybean quality goes down, prices go up" (FarmProgress) — ver Honestidade sobre os outros 5 itens "mantidos" sem headline exposto
  - Forecasts estatísticos internos (bandas 7d/30d, MA20+volatilidade+slope) — geração de 2026-09-01, alvos 08/09 (7d) e 01/10 (30d); viés "altista" em soja e farelo nos dois horizontes, óleo "lateral" no 7d e "altista" no 30d
  - system/tributario_watch.toml (lido como referência, não editado) — `atualizado_em` 2026-06-05 em todos os eventos, agora **89 dias sem revisão** — ver Lente fiscal e Honestidade
  - Fila de julgamento — carimbada 2026-09-01 no briefing, 6 itens; tratados nesta leitura: `alerta-quebra_resistencia-soja_cbot-2026-09-01`, `alerta-quebra_resistencia-farelo_cbot-2026-09-01`, `alerta-quebra_suporte-complexo_soja-2026-09-01`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, `trib-DANANTARA-INDONESIA-2026-09-01`, `release-nopa-2026-09-01`
  - Cruza com [[2026-08-31_leitura-complexo]] (leitura de segunda-feira, que aguardava exatamente o fechamento de hoje para testar o rompimento e a margem de biodiesel)
status: ativa
vies: [bull-soja, bull-farelo, bull-oleo_soja]
---

## Visão geral

Hoje é terça-feira, 02/09/2026, e o briefing usado nesta leitura traz o dado que a leitura
de ontem estava literalmente esperando: o fechamento de 01/09/2026 em Chicago, o primeiro
teste real do rompimento técnico de sexta-feira (28/08) depois de um pregão de segunda-feira
(31/08) que, agora sabemos, foi de pausa — a soja ficou tecnicamente parada em 1.288,00 USD
cts/bushel (mesmo valor de sexta) e o farelo até recuou 1,14% para 338,60 USD/short ton,
enquanto o óleo mal se mexeu (70,83 vs 70,82). Terça-feira resolveu essa pausa com força:
soja fechou em **1.318,50 USD cts/bushel** (+2,37% sobre segunda), farelo em **345,10 USD/
short ton** (+1,92%) e óleo em **72,38 USD cts/lb** (+2,19%) — as três pernas do complexo
subindo juntas e de forma expressiva no mesmo pregão, algo que não acontecia com essa
sincronia desde o rali original de 27-28/08.

Para quem não acompanha o complexo diariamente, vale reforçar o mecanismo básico: a soja em
grão é a matéria-prima que entra numa esmagadora (crush) e sai como dois produtos com
demandas diferentes — farelo (proteína, vai para ração animal) e óleo (vai para alimentação
humana e, cada vez mais, biodiesel). O **crush margin** mede, em dólares por bushel (unidade
de volume da soja, ~27,2 kg), quanto sobra para quem opera a esmagadora depois de vender
farelo + óleo e pagar a soja. Dentro desse crush, o **oil share** (fatia do valor total que
vem do óleo) diz quem "manda": se o óleo paga mais que a metade do crush, ele domina a
decisão econômica da esmagadora; se o farelo "sobra" (produção alta, demanda relativamente
mais fraca), ele empurra o preço do crush para baixo mesmo com o board em alta. O terceiro
termômetro, o **ratio Far/Soj**, mede se o farelo está caro ou barato EM RELAÇÃO à soja — não
em valor absoluto — dividindo o valor do farelo pelo equivalente em soja.

E é exatamente aí que mora a informação mais importante desta terça-feira: apesar do rali
generalizado, o **crush margin fechou em US$ 2,369/bushel** (indicators, 01/09, Board Crush:
farelo 345,10 + óleo 72,38 − soja 1.318,50), a segunda sessão seguida ABAIXO do nível de
referência de US$ 2,50 monitorado pela fila (`alerta-quebra_suporte-complexo_soja-2026-09-01`)
e, na prática, marginalmente PIOR que os US$ 2,3605/bushel de segunda-feira. Ou seja: o
crush está preso numa faixa de US$ 2,36–2,37 nos últimos dois pregões, mesmo com farelo e
óleo em alta firme — porque a SOJA, a matéria-prima, está subindo ainda mais rápido que os
dois produtos somados. Essa é a leitura de hoje em uma frase: o complexo está em rali
generalizado, mas a soja é quem manda, o crush do esmagador aperta em vez de melhorar, e o
ratio Far/Soj caiu para **78,52%** (indicators, 01/09) — o menor nível da última semana
(79,77% em 28/08 → 78,87% em 31/08 → 78,52% em 01/09), aprofundando a zona "abundante"
(<80%) em vez de convergir para os 80-87% que a tese original de junho previa. O óleo,
enquanto isso, finalmente resolveu sua própria indefinição: fechou acima do pivô técnico de
72,00 pela primeira vez na janela observada, e a margem de biodiesel americana, que vinha
comprimindo havia mais de uma semana, deu um salto de +17,3% em dois pregões (de US$ 1,4102/
galão na sexta para US$ 1,6545/galão hoje) puxada por um heating oil (proxy de diesel nos
EUA) que subiu 8,3% no mesmo intervalo. **Leitura de uma linha**: o pivô do complexo segue
sendo a soja — ela lidera tanto o rali quanto o aperto do crush — a maior convicção é a de
que o rompimento técnico das três pernas está confirmado (o teste que faltava aconteceu e
passou), e o nível de confiança sobe de médio-baixo para **médio-alto**, com a ressalva de
que o COT (posicionamento dos fundos) segue cego para toda essa semana de rali.

## Soja

**Viés: bull, forte — rompimento confirmado por um pregão real de alta volume, câmbio e
físico BR reforçando, mas COT cego para a semana toda.**

O que sustenta a tese:

- **Rompimento técnico agora testado e confirmado por um pregão de verdade.** Soja CBOT
  fechou em 1.318,50 USD cts/bushel em 01/09/2026 (CME CBOT), 11,7% acima da resistência de
  1.180,00 monitorada pela fila (`alerta-quebra_resistencia-soja_cbot-2026-09-01`), com alta
  de +2,37% sobre o fechamento de segunda (1.288,00) em volume de 175.695 contratos — o maior
  volume de qualquer sessão de soja nesta janela de 14 dias do briefing. O mecanismo: volume
  alto em dia de alta forte, depois de uma sessão de pausa (segunda-feira ficou flat em
  1.288,00), é a assinatura clássica de "teste bem-sucedido" — o mercado parou, digeriu o
  nível, e decidiu seguir na mesma direção com convicção nova, não apenas inércia. Isso reduz
  materialmente a probabilidade de que o rompimento de sexta tenha sido um fakeout.
- **Curva futura em contango crescente até mai/27, sinal de que o mercado não trata a alta
  como pico isolado.** Nov/26 (contrato-base, X26) 1.318,50 → jan/27 (F27) 1.333,50 → mar/27
  (H27) 1.337,75 → mai/27 (K27) 1.342,50 → jul/27 (N27) 1.342,75 (CME CBOT, 01/09) — cada
  vencimento subsequente precifica um pouco mais caro que o anterior, um prêmio de 24,25
  pontos (1,8%) entre nov/26 e jul/27. O mecanismo: contango crescente ao longo da curva
  normalmente reflete expectativa de custo de carregamento (armazenagem, juros) MAIS uma
  leitura de que a oferta segue justa adiante, não apenas no contrato corrente — é
  estruturalmente diferente de uma alta pontual concentrada só no front month.
- **Câmbio comprimindo o ganho em dólar, mas sem competir com o movimento.** USD/BRL fechou
  01/09 em 5,1570 (BCB PTAX), a terceira queda seguida (5,2005 em 28/08 → 5,1816 em 31/08 →
  5,1570 em 01/09, -0,83% acumulado) — o real vem se valorizando junto com o rali de
  commodities, o que é o padrão típico quando o dólar global enfraquece (dólar mais fraco
  turbina commodities cotadas em USD e, ao mesmo tempo, aprecia moedas de países exportadores
  de commodities). Na prática, isso "rouba" um pouco do ganho em reais: a paridade
  CBOT-implícita em saca de 60kg subiu 1,88% (de R$ 147,13 em 31/08 para R$ 149,90 em 01/09,
  indicators — CBOT 1.318,50 × USD/BRL 5,1570), MENOS que os 2,37% de alta em dólar da soja
  CBOT no mesmo intervalo — mas ainda uma alta robusta em termos absolutos.
- **Físico brasileiro pagando prêmio ainda maior sobre a paridade.** CEPEA/ESALQ Soja
  Paranaguá (via NAG, principal porto exportador de grãos do Sul do Brasil) fechou 01/09 em
  R$ 161,14/saca (+1,07% sobre 31/08), R$ 11,24/saca (7,5%) acima da paridade CBOT-implícita
  de R$ 149,90 — basis físico positivo e em leve alta relativa (era 8,2% em 28/08, caiu
  temporariamente e volta a rondar a mesma faixa), sinal de que o mercado físico no porto
  segue mais apertado do que o papel indicaria sozinho. O prêmio do porto sobre o interior do
  Paraná (R$ 153,06/saca, CEPEA/ESALQ Paraná interior via NAG, +1,16%) é de R$ 8,08/saca
  (5,3%), levemente menor que os 5,6% de 28/08 — a diferença entre porto e interior está
  estável, o movimento de alta está sendo repassado de forma relativamente uniforme ao longo
  da cadeia física.
- **Primeiro sinal (ainda fraco) de deterioração na condição da lavoura americana, coincidindo
  com o rali.** USDA Crop Progress de 30/08/2026 mostra 12% excelente / 46% boa / 9% ruim,
  ante 12%/48%/9% em 23/08 — a fatia "boa" caiu 2 pontos percentuais, primeira piora
  perceptível em semanas. O mecanismo: menor percentual em condições boas/excelentes
  historicamente antecede revisões de queda na produtividade esperada pelo USDA nos relatórios
  de safra — não é ainda um dado de produção, mas é o tipo de sinal que costuma vir ANTES de
  uma revisão de balanço. Isso é corroborado por uma notícia da FarmProgress captada no RSS de
  01/09: "Soybean quality goes down, prices go up" — o próprio mercado americano está lendo o
  mesmo sinal.
- **Estoques brasileiros de soja seguem apertando estruturalmente rumo ao fim de 2026**
  (ABIOVE, sem atualização nesta janela): estoque final recuando de 7.912,1 mil toneladas
  (set/26, mês corrente) para 3.658,9 mil t (nov/26) e 1.889,9 mil t (dez/26) — parte é
  sazonalidade normal de fim de safra, mas reforça o pano de fundo de oferta mais curta.

**O que invalida / risco:**

- **O COT segue cego para a semana inteira do rali.** O corte de 25/08/2026 (Commodity
  Futures Trading Commission) — ainda o mais recente — mostrava managed money com net long de
  200.679 contratos (+32,2% sobre 18/08), mas não enxerga NENHUMA das sessões de 27/08 até
  01/09, que já são cinco pregões de alta acumulada. O próximo corte (posições de terça 01/09,
  publicação estimada por volta de sexta 04/09 pelo calendário semanal do CFTC — inferência,
  não confirmada no briefing) é o primeiro que vai revelar se dinheiro novo entrou DURANTE o
  rali ou se ele está sendo sustentado só por cobertura de vendidos e fluxo comercial.
- **Nível técnico a vigiar:** qualquer fechamento de volta abaixo de 1.180 desfaz o
  rompimento — mas com o preço agora 11,7% acima desse nível, a distância de segurança
  cresceu bastante desde sexta-feira (9,2%).
- **O crush margin abaixo de 2,50 é, em si, um sinal de que o rali da soja pode estar
  "esticado" frente aos seus próprios produtos.** Se o crush continuar comprimindo enquanto
  a soja sobe, esmagadoras tendem a reduzir ritmo de moagem (processar menos) para não operar
  no prejuízo relativo — o que, com o tempo, reduziria a demanda física por soja e poderia
  esfriar o próprio rali pela via da demanda interna de processamento.
- **A notícia de 28/08/2026 sobre uma decisão do STF (Supremo Tribunal Federal) mencionada no
  RSS segue sem teor detalhado no briefing** — risco de cauda não quantificável enquanto durar
  essa lacuna de informação.

**Leitura operacional:** o teste que a leitura de ontem esperava aconteceu e passou — o
trader comprado no rompimento ganha um argumento técnico mais forte hoje do que tinha ontem,
porque o mercado não devolveu a pausa de segunda, engoliu-a e seguiu subindo em volume
recorde da janela. Ainda assim, o hiato do COT chegou a 8 dias corridos sem ver nenhuma
sessão do rali — quem está comprado sem proteção deve manter o stop técnico já definido (por
exemplo, 1.180, ou um nível mais próximo tipo 1.288 para travar parte do ganho recente) e
não usar a confirmação de hoje como motivo para aumentar posição sem saber se há fôlego de
fundo por trás. Quem quer montar posição vendida contra o movimento segue sem sinal técnico
de exaustão — o argumento mais forte para cautela vendida não é técnico, é o crush margin
comprimindo, que sinaliza que o próprio mercado físico (via demanda de esmagamento) pode
começar a resistir a preços de soja tão altos relativamente a farelo e óleo.

## Farelo

**Viés: bull, moderado — rompimento confirmado na fita, mas a estrutura relativa (ratio
Far/Soj) piorou em vez de melhorar, reforçando que o farelo está sendo carregado pela soja,
não subindo por força própria.**

O que sustenta a tese (na fita):

- **Rompimento de resistência confirmado após a pausa de segunda.** Farelo CBOT fechou em
  345,10 USD/short ton em 01/09/2026, 6,2% acima da resistência de 325,00
  (`alerta-quebra_resistencia-farelo_cbot-2026-09-01`), com alta de +1,92% sobre segunda-feira
  (338,60) — recuperando integralmente a queda de -1,14% de segunda e fazendo nova máxima da
  janela.
- **Curva futura também em contango crescente**, de 342,00 (set/26) a 356,40 (mai/27, +4,2%
  entre pontas) — mercado precificando firmeza sustentada, não só um pico pontual.
- **Físico brasileiro estabilizado em patamar mais alto**, mesmo sem repasse novo hoje: farelo
  MT/IMEA (NAG, Instituto Mato Grossense de Economia Agropecuária) em R$ 1.795,68/ton, e
  Rondonópolis/MT em R$ 1.900,00/ton — ambos congelados desde 31/08, mas já tinham saltado de
  R$ 1.726,20 e R$ 1.870,00, respectivamente, no fim da semana passada. O físico local não
  recuou mesmo com o pregão de pausa de segunda-feira.

O que tensiona a tese (a estrutura por baixo, piorando, não apenas persistindo):

- **O ratio Far/Soj CAIU pela terceira sessão seguida, mesmo com o farelo em máxima da
  janela.** Fechou em 78,52% em 01/09 (indicators), abaixo dos 78,87% de segunda e dos 79,77%
  de sexta — ou seja, a compressão que vinha diminuindo (o ratio subindo gradualmente rumo a
  80%) inverteu de direção justamente no dia em que o farelo bateu máxima. O mecanismo é
  simples e importante: farelo subiu 1,92% no dia, mas a soja subiu 2,37% — como o ratio mede
  farelo relativo à soja, quando a soja sobe mais rápido o ratio cai mesmo com o farelo em
  alta absoluta. Isso é evidência direta, não inferência, de que é a soja quem está no
  comando: o farelo está sendo arrastado, não liderando.
- **O ISF (Índice de Sobra de Farelo) segue travado em 80/100** (4 de 5 condições
  estruturais apontando pressão baixista), sem uma única sessão de melhora na janela
  disponível — o sistema não vê o quadro estrutural de oferta de farelo mudando, mesmo com o
  board em máxima.
- **Prêmio de exportação em Paranaguá congelado em +0,12 USD/short ton desde 24/08/2026** —
  já são 9 sessões seguidas sem se mexer mesmo com o board subindo com força nos últimos dois
  pregões, um padrão de estagnação que persiste havia mais de uma semana e meia.

**Trata a fila `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`:** esse
item volta a aparecer na fila hoje, mas o fato NOVO de hoje é justamente o oposto do que a
tese original de 11/06/2026 previa — em vez de o ratio convergir para a zona 80-87%
("apertado"), ele está se afastando dela pela primeira vez em quatro sessões (79,77% → 78,87%
→ **78,52%**). A tese permanece "revisada, sem encerrar" como já registrado em
[[2026-08-31_leitura-complexo]]: o farelo subiu em valor absoluto (CBOT de ~303,60 USD/sht em
10/06 para 345,10 hoje, +13,7%) sem que o ratio relativo tenha convergido para a zona
apertada original — e agora, com o recuo de hoje, essa divergência entre "preço absoluto
sobe" e "ratio relativo cai" fica ainda mais nítida. São quase 12 semanas (83 dias corridos)
desde o alerta original, contra a janela de "1-2 semanas" que a tese previa — o precedente
mais forte deste briefing contra apressar timing em teses de reversão do ratio.

**O que invalida / risco:** se o ratio continuar caindo enquanto o preço absoluto do farelo
sobe, isso é, na prática, o mercado dizendo que o farelo é o passageiro, não o motorista, do
rali — qualquer correção de soja bateria desproporcionalmente no farelo (ele cairia mais
rápido do que subiu, proporcionalmente, revertendo o ratio para cima justamente numa queda de
preço, não numa alta).

**Leitura operacional:** o rompimento técnico está confirmado e reforça posições compradas
direcionais, mas para quem opera especificamente o spread Far/Soj (long farelo / short soja,
apostando em reversão do ratio para cima), hoje é um dia que trabalha CONTRA a tese, não a
favor — o ratio se afastou do topo do range recente. A zona de acumulação abaixo de 80%
segue tecnicamente válida como referência histórica, mas o timing continua sem sinal de
virada, e o precedente de "72+ dias de espera" pesa contra montar essa posição de forma
agressiva agora.

## Óleo

**Viés: bull, moderado — a divergência que marcava as últimas leituras (ISO em 100 mas
margem de biodiesel comprimindo) se resolveu a favor do lado comprado: o óleo finalmente
fechou acima do pivô técnico de 72,00 e a margem saltou com o heating oil.**

O que sustenta o lado comprado:

- **Fechamento acima do pivô técnico de 72,00 pela primeira vez na janela observada.** Óleo
  CBOT fechou em 72,38 USD cts/lb em 01/09/2026, alta de +2,19% sobre segunda-feira (70,83) —
  em leituras anteriores, o fechamento de sexta (70,82) era tratado como "repique dentro de
  estrutura ainda quebrada" justamente por ficar abaixo de 72,00
  (`alerta-quebra_suporte-oleo_cbot-2026-08-28`, já tratado); hoje esse nível foi reconquistado
  com folga (a mínima do dia, 71,50, já abriu acima do fechamento de segunda).
- **ISO travado em 100/100**, sem uma única sessão de enfraquecimento na janela — e agora
  reforçado por evidência de preço, não só de condições estruturais.
- **Margem de biodiesel americana saltou 17,3% em dois pregões, revertendo a compressão que
  vinha havia mais de uma semana.** Série: 1,5678 USD/galão (26/08) → 1,5264 (27/08) → 1,4102
  (28/08, o fundo da compressão) → 1,548 (31/08, +9,8%) → **1,6545 (01/09, +6,9%)** —
  recuperação de +17,3% desde o fundo de sexta, agora no maior nível de toda a janela. O
  mecanismo por trás dessa reversão: a margem de biodiesel é receita (heating oil + 1,5× valor
  do crédito RIN D4, o certificado que comprova mistura de biocombustível nos EUA) menos custo
  (óleo de soja + custo industrial fixo). O heating oil (HO=F, proxy de diesel americano —
  compõe a RECEITA) saltou de 4,3567 USD/galão (fechamento de sexta) para 4,7180 em 01/09,
  +8,3% — subindo MAIS RÁPIDO que o custo do óleo (que subiu 2,2% no mesmo intervalo, de 70,82
  para 72,38 cts/lb), o que expande a margem em vez de espremê-la. É a inversão exata do
  padrão da semana passada, quando o custo do óleo subia mais rápido que a receita.
- **Catalisador regulatório atingiu o marco-alvo ontem, mas sem confirmação no briefing.** A
  fila trouxe `trib-DANANTARA-INDONESIA-2026-09-01`: 01/09/2026 era o marco-alvo para a
  Indonésia completar a centralização da exportação de óleo de palma sob o fundo soberano
  Danantara (`tributario_watch.toml`, id `DANANTARA-INDONESIA`, atualizado 05/06/2026, direção
  "alta" para óleo de soja). O mecanismo: quanto mais centralizada/burocratizada fica a
  exportação do maior óleo vegetal do mundo em volume, mais espaço abre para o óleo de soja
  como substituto na demanda global (biodiesel e alimentação). Esse marco já passou (era
  ontem, hoje é 02/09), mas nenhuma notícia no RSS ou fonte deste briefing confirma se a
  centralização realmente se completou — tratar como catalisador que talvez tenha ocorrido,
  não como fato confirmado (ver Honestidade e o precedente do B50 abaixo).
- **Levy de exportação da palma indonésia (até 12,5%, PMK 9/2026, id
  `INDONESIA-LEVY-PMK9`) segue vigente**, sustentando o óleo de soja por substituição de forma
  permanente, independentemente do desfecho da Danantara.

O que ainda sustenta cautela / o lado cético:

- **A curva futura do óleo é praticamente plana e levemente decrescente nos vencimentos mais
  distantes** — diferente de soja e farelo, que estão em contango crescente até mai/27. Óleo:
  out/26 (V26, contrato-base) 72,38 → dez/26 (Z26) 72,62 (pico da curva) → jan/27 (F27) 72,57 →
  mar/27 (H27) 72,54 → mai/27 (K27) 72,35 (menor que o contrato-base). O mecanismo: quando a
  curva mostra queda modesta nos vencimentos mais distantes, o mercado está dizendo que espera
  a força atual PERSISTIR aproximadamente no nível de hoje, não se estender ou acelerar — uma
  leitura mais cautelosa do que a de soja e farelo, cujas curvas sobem de ponta a ponta.
- **COT de 25/08 (ainda sem atualização) mostrava fundos DIMINUINDO net long antes do próprio
  rali** — managed money com long caindo de 116.669 para 114.248 (-2,1%) e short subindo de
  25.436 para 29.132 (+14,5%) entre 18/08 e 25/08, net long recuando 6,7%. É o oposto do padrão
  em soja, e são 8 dias corridos sem atualização — a maior lacuna relativa das três pernas,
  porque é justamente aqui que a foto pré-rali contradizia o movimento que já dura uma semana.
- **Prêmio de exportação em Paranaguá congelado em +0,10 cts/lb desde 24/08/2026** — mesmo
  padrão de estagnação do farelo, 9 sessões seguidas.
- **Volume de heating oil muito baixo na sessão (466 contratos, ante 175.695 da soja e 38.557
  do próprio óleo)** — o salto de 8,3% no HO se apoia em liquidez fina, o que pede cautela
  antes de tratá-lo como confirmação definitiva de mudança de regime na receita do biodiesel
  (ver Honestidade).

**O que invalida / risco:** para o lado comprado, um fechamento de volta abaixo de ~70,80
devolveria a reconquista de hoje e reabriria a leitura de "repique dentro de estrutura
quebrada". Para o lado cético, se o heating oil devolver o salto de hoje (voltando para a
faixa de 4,40-4,50) enquanto o custo do óleo segue subindo, a margem de biodiesel volta a
comprimir e o argumento mais forte desta leitura desaparece. O evento Danantara, mesmo tendo
atingido seu marco-alvo ontem, é binário e sem confirmação: o precedente do B50 indonésio
(anúncios ambiciosos que escorregam na execução, id `INDONESIA-B50`) ensina que "marco-alvo
atingido no calendário" não é o mesmo que "assunção plena confirmada em relatório".

**Leitura operacional:** pela primeira vez nesta sequência de leituras, o óleo tem um
argumento técnico E um argumento de margem apontando na mesma direção (compra) ao mesmo
tempo — antes eram sinais contraditórios (ISO alto, margem comprimindo). Isso não elimina a
cautela: a curva futura mais achatada e o COT desatualizado e cético seguem pedindo tamanho de
posição moderado, não agressivo. Continua fazendo sentido operar óleo também como parte do
spread/crush (oil share subindo, 51,19% hoje vs 50,83% na sexta) além de qualquer aposta
direcional pura — o crush está premiando cada vez mais quem está posicionado no lado do óleo
dentro do complexo.

## Spreads e crush (leitura de complexo)

Juntando as três leituras de hoje: o ratio Far/Soj caiu para 78,52% (zona "abundante", <80%,
e agora se afastando dela) enquanto o oil share subiu para 51,19% — os dois indicadores
relativos concordam pela primeira vez em vários dias sobre a MESMA direção: o óleo está
ganhando espaço dentro do valor do crush, o farelo está perdendo espaço relativo, mesmo com
farelo em máxima absoluta da janela. O oil-meal spread (diferença direta entre valor do óleo
e valor do farelo, em USD/bushel) confirma: 0,1485 (27/08) → 0,2552 (28/08) → 0,3421 (31/08) →
**0,3696 (01/09)** — quarta alta seguida, sinal consistente de que o óleo está "vencendo" o
farelo dentro do crush a cada sessão. Os índices sintéticos (ISF 80, ISO 100) continuam
travados nos mesmos valores há muitas sessões — vale registrar que esses dois índices não se
moveram NENHUMA vez em toda a janela de 14 dias deste briefing, o que sugere que eles captam
condições estruturais de baixa frequência (thresholds binários), não o movimento contínuo de
preço — uma limitação a ter em mente ao usá-los como sinal de timing.

O crush margin, por sua vez, é a peça que não acompanha o otimismo das outras leituras: fechou
em US$ 2,369/bushel (01/09), a segunda sessão consecutiva abaixo do referencial de US$ 2,50, e
praticamente estagnado frente aos US$ 2,3605 de segunda — mesmo com farelo (+1,92%) e óleo
(+2,19%) subindo bem no dia. A conta é direta: farelo + óleo subiram, em conjunto, menos em
termos absolutos do que a soja subiu sozinha (soja +2,37% no dia, um salto maior em pontos
absolutos dado o tamanho do contrato). Para quem opera o crush diretamente, isso é um sinal
de que apostar em "crush melhora com o rali" não está se confirmando nesta semana — o crush
está andando de lado desde sexta-feira (2,45 → 2,36 → 2,37) enquanto o board sobe, e só
reverteria essa leitura com uma sessão em que farelo+óleo subissem proporcionalmente mais que
a soja. Para quem opera o spread Far/Soj, a compressão do ratio abaixo de 80% já dura pelo
menos 9 sessões (desde 24/08) e voltou a se aprofundar hoje em vez de convergir — reforça a
leitura de zona de acumulação sem timing definido, não um sinal de entrada iminente.

## Lente fiscal/regulatoria BR

Antes de fechar qualquer tese de preço BR, os vetores tributários/regulatórios vivos que
pesam no complexo — todos do `system/tributario_watch.toml`, cujo carimbo mais recente
(`atualizado_em`) em TODOS os eventos é 2026-06-05, ou seja, **89 dias sem revisão**:

- **MP 1.363/2026** (id `MP-1363-2026`, subvenção diesel fóssil R$ 1,12/L, vigente até
  31/12/2026): barateia o diesel fóssil no mix B15 (mistura de 15% de biodiesel ao diesel
  fóssil, obrigatória no Brasil), reduzindo a competitividade relativa do biodiesel e a
  demanda doméstica por óleo de soja — vetor de baixa para óleo, sem mudança de status.
- **B16 (id `B16-CNPE-2026`, elevação da mistura de biodiesel para 16%)** segue "adiado" — CNPE
  (Conselho Nacional de Política Energética) cancelou em maio, testes técnicos com resultado
  esperado só por volta de novembro/2026. Upside represado (~436 mil toneladas de óleo
  adicional de demanda potencial), não corrente — relevante para o horizonte 30d dos
  forecasts, que já embute viés altista em óleo, mas não deveria embutir o B16 antes de
  confirmação.
- **Isenção de PIS/Cofins do biodiesel na mistura** (id `PISCOFINS-BIODIESEL-ISENCAO`): o TOML
  registra vigência ATÉ 31/07/2026 — já **33 dias corridos vencida** frente aos 02/09/2026 de
  hoje, sem qualquer registro de prorrogação ou expiração no arquivo. Segue sendo uma lacuna
  real de informação (ver Honestidade), não uma leitura de preço.
- **MP 1.358/2026** (subvenção gasolina R$ 0,89/L): vigência registrada até 11/07/2026, agora
  **53 dias corridos vencida**, mesma lacuna de informação sobre renovação.
- **STJ REsp 2.165.276** (id `STJ-RESP-2165276`, crédito de PIS/Cofins sobre soja em biodiesel,
  vigente, direção "alta" para soja/óleo): alívio de custo pontual, não vinculante (não é
  decisão repetitiva, não obriga automaticamente outros casos semelhantes).
- **EPA RFS 2026/2027** (id `EPA-RFS-2026-2027`, mandato de biocombustível americano da
  Environmental Protection Agency, vigente desde 15/06/2026, direção "alta" para óleo): volumes
  recordes de RINs sustentam a margem de biodiesel americana — o salto de hoje na margem
  (+17,3% em dois pregões) acontece dentro desse arcabouço regulatório já vigente, não é um
  fato tributário novo, é o mercado repassando um mandato já existente.
- **Crédito 45Z** (id `45Z-CLEAN-FUEL`, Clean Fuel Production Credit americano, em tramitação,
  direção "mista"): se a regra final excluir insumo importado da elegibilidade, o óleo de soja
  DOMÉSTICO americano ganha, mas o sebo bovino brasileiro hoje exportado como insumo perderia
  esse mercado e voltaria para o blend doméstico americano — vetor que pode virar contra o
  óleo de soja BR mesmo sendo favorável ao óleo de soja americano.
- **Indonésia — Danantara** (id `DANANTARA-INDONESIA`) e **levy de exportação PMK 9/2026** (id
  `INDONESIA-LEVY-PMK9`): já tratados na seção Óleo, ambos direção "alta" para óleo de soja via
  substituição de palma. O marco-alvo da Danantara (01/09) já passou sem confirmação de
  execução no briefing.
- **Notícia de 28/08/2026 sobre uma decisão do STF** segue sem teor detalhado no briefing, e não
  há nenhum evento STF cadastrado no `tributario_watch.toml` (só STJ) — não é possível avaliar
  o impacto com os dados disponíveis; fica como item para acompanhar, não para precificar.

## Riscos e eventos próximos

- **Próximo corte CFTC COT** — posições de terça 01/09, com publicação estimada por volta de
  sexta 04/09 pelo calendário semanal do CFTC (inferência, não confirmada no briefing): é o
  dado que finalmente vai revelar se os fundos entraram comprados NAS cinco sessões de rali
  (27/08 a 01/09) ou ficaram de fora, agora com 8 dias corridos de defasagem acumulada — a
  maior lacuna de todo o período coberto por esta leitura.
- **Confirmação (ou não) da centralização plena da exportação de palma pela Danantara** —
  marco-alvo era 01/09, já passou; vigiar notícia confirmando execução ou, como no precedente
  do B50 indonésio (`INDONESIA-B50`), sinal de atraso.
- **NOPA mensal** (`release-nopa-2026-09-01`): a fila sinaliza um "release novo", mas o
  conteúdo (`monthly_status` 0,0 bool, paywall) é idêntico ao dos dias anteriores — não há
  confirmação real do ritmo de esmagamento americano ainda.
- **USDA WASDE**: ausente da janela há bastante tempo; qualquer publicação nova é catalisador
  potencial de revisão de balanço mundial, especialmente relevante depois do primeiro sinal de
  deterioração no Crop Progress de 30/08.
- **USDA Crop Progress semanal**: o próximo corte (normalmente às segundas à tarde, horário dos
  EUA) atualizaria o dado de 30/08 (12%/46%/9%) — vigiar se a deterioração de 2pp na condição
  "boa" continua ou foi ruído de uma semana.
- **Vigência da isenção PIS/Cofins do biodiesel** (TOML aponta 31/07/2026, agora 33 dias
  vencida sem confirmação de prorrogação) e **MP 1.358/2026 da gasolina** (53 dias vencida) —
  checar notícia de renovação/expiração antes de assumir qualquer tese de custo de combustível
  BR.
- **Clima**: janela de plantio da safra 2026/27 se aproxima (set/out); a previsão de hoje
  (02/09, INMET) mostra o núcleo produtor de Mato Grosso recebendo os primeiros sinais de
  chuva isolada depois de dias de céu limpo e calor extremo — se confirmado em campo (o
  briefing só traz previsão, não medição de precipitação real), é um alívio potencial para a
  umidade do solo às vésperas do plantio; o Sul, que vinha de chuva/trovoada, aparece hoje com
  céu mais aberto — inversão de padrão a confirmar nos próximos dias, não tendência
  estabelecida.
- **Confirmação (ou reversão) do salto de heating oil de hoje** — sessão de baixo volume (466
  contratos); se o próximo pregão confirmar o novo patamar (~4,70+), a margem de biodiesel
  segue sustentada; se devolver, a compressão da semana passada pode retomar e derrubar o ISO
  de 100 pela primeira vez na janela observada.

## Honestidade

- **O dado que faltava na leitura de ontem chegou, e resolveu o principal ponto em aberto —
  mas o crush margin virou o novo ponto de atenção.** A leitura de 31/08 esperava o fechamento
  de segunda-feira; este briefing traz não só esse fechamento (soja 1.288,00 flat, farelo
  338,60 -1,14%, óleo 70,83 flat) como também o de terça-feira (01/09, os números centrais
  desta leitura). Isso resolveu o "nada mudou" das últimas leituras, mas trouxe consigo um
  sinal novo (crush margin estagnado abaixo de 2,50 apesar do rali) que substitui a antiga
  lacuna como o principal fio solto do complexo.
- **Heating oil com volume muito baixo (466 contratos) no pregão que sustenta boa parte da
  tese de óleo/biodiesel de hoje.** O salto de +8,3% no HO é o único fio de evidência direta
  de que a receita do biodiesel melhorou — mas com liquidez tão fina, o número merece
  confirmação em pelo menos mais uma sessão antes de ser tratado como mudança de regime, não
  como ruído de um pregão fino.
- **`noticias_rss` registra "7 mantidos" em 01/09, mas apenas 2 headlines aparecem com texto
  legível no dump** (farelo: Conab/credenciamento; soja: FarmProgress/qualidade da safra) — os
  outros 5 itens "mantidos" não têm headline nem link visíveis nesta leitura. Nenhum conteúdo
  foi inventado para preencher essa lacuna.
- **COT desatualizado, agora com 8 dias corridos de defasagem** (corte de 25/08 frente ao
  fechamento de 01/09) — a maior lacuna desta leitura, e a que mais pesa contra qualquer tese
  de "convicção nova dos fundos" no rali desta semana.
- **Prêmios de exportação (Paranaguá, farelo e óleo) seguem congelados**, agora 9 sessões
  seguidas idênticas (desde 24/08) mesmo com o board em máxima da janela — não dá para saber
  se reflete mercado físico export realmente parado ou limitação de atualização da fonte
  (NAG).
- **Danantara: marco-alvo atingido no calendário (01/09), mas sem qualquer notícia ou dado no
  briefing confirmando execução real.** Tratado como catalisador pendente de confirmação, não
  como fato consumado — nenhum número foi inventado para preencher essa lacuna.
- **`tributario_watch.toml` sem atualização há 89 dias** — pelo menos dois vetores (isenção
  PIS/Cofins do biodiesel, vigência até 31/07; MP 1.358/2026, vigência até 11/07) já passaram
  da data de vigência registrada sem nota de renovação ou expiração. Tratados como "status
  desconhecido pós-vigência".
- **NOPA segue inacessível** (paywall) — o "release novo" sinalizado pela fila
  (`release-nopa-2026-09-01`) não trouxe nenhum número de esmagamento americano mensal
  confirmado; é um falso positivo de novidade, não um dado novo.
- **USDA WASDE ausente** da janela — nenhuma leitura de balanço mundial oficial atualizado
  disponível.
- **Percentil histórico de posicionamento COT não está disponível no briefing** — toda leitura
  de "fundos comprando/vendendo" nesta análise usa variação semana a semana de contratos
  absolutos, não percentil histórico. Nenhum percentil foi inventado.
- **MPOB (palma Malásia) segue com parser quebrado** (3.456 caracteres, sem números extraídos)
  — nenhum dado de produção/estoque de palma malaia disponível para cruzar com a tese de
  substituição via Indonésia.
- **BCBA (Argentina) segue sem links de relatório detectados pelo scraper** — nenhum dado de
  safra ou exportação argentina disponível nesta janela, mesmo com a página sendo
  tecnicamente acessível.
- **Notícia do INMET é previsão, não medição de precipitação real** — a leitura de "primeiro
  sinal de chuva no núcleo produtor" é uma previsão meteorológica para hoje (02/09), não uma
  confirmação de que choveu ou de quanto choveu; tratar como sinal a confirmar, não fato
  agronômico consumado.
