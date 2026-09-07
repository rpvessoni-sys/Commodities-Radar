---
data: 2026-09-07
titulo: "Terceiro dia corrido sem pregão novo — hoje é Labor Day nos EUA (feriado federal, CBOT/CME fechados) — e o relógio da revisão D+90 do spread Far/Soj chega a 2 dias, com ISF/ISO fechando a quarta sessão seguida em 60/80 e o ratio Far/Soj a 0,24 ponto percentual de 80%"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT (ZSX26 soja / ZMV26 farelo / ZLV26 óleo) — última sessão negociada: 2026-09-04 (sexta-feira). Soja: abertura 1.316,00, máxima 1.320,75, mínima 1.305,75, fechamento 1.309,75 USD cts/bushel, volume 105.402 contratos. Farelo: abertura 349,00, máxima 350,80, mínima 345,50, fechamento 348,20 USD/short ton, volume 25.282 contratos. Óleo: abertura 69,30, máxima 69,67, mínima 67,77, fechamento 68,89 USD cts/lb, volume 28.237 contratos. Curva futura em 04/09 — soja: set/26 1.293,75, nov/26 (base) 1.309,75, jan/27 1.325,00, mar/27 1.330,25, mai/27 1.334,50, jul/27 1.335,25; farelo: set/26 345,30, out/26 (base) 348,20, dez/26 355,10, jan/27 358,00, mar/27 359,60, mai/27 360,30; óleo: set/26 68,78, out/26 (base) 68,89, dez/26 69,27, jan/27 69,43, mar/27 69,55, mai/27 69,60
  - CME NYMEX heating oil (HO=F) — 2026-09-04: abertura 4,5976, fechamento 4,5402, máxima 4,6026, mínima 4,4338 USD/galão, volume 39.031 contratos; reabertura fina de domingo 2026-09-06: abertura 4,5804, máxima 4,5950, mínima 4,5659 USD/galão, volume 410 contratos (sem campo "fechamento" — sessão de baixíssima liquidez, ~1% do volume de sexta)
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, ISF, ISO, margem biodiesel, paridade BR) — série 2026-08-31 a 2026-09-06 (os cálculos de 05 e 06/09 repetem os insumos de preço de 04/09, sem pregão novo desde então)
  - BCB PTAX — 2026-09-04: USD/BRL 5,1253, EUR/BRL 5,9546, Selic diária 0,05166% a.a. (séries SGS 1, 21619, 11), sem publicação em 05-07/09 (fim de semana + feriado bancário nos EUA não impede PTAX no Brasil, mas o dump não traz linha nova)
  - CEPEA/ESALQ Soja Paranaguá via NAG — 2026-09-04: R$ 160,87/saca (var +0,46%)
  - CEPEA/ESALQ Soja Paraná interior via NAG — 2026-09-04: R$ 152,10/saca (var +0,28%)
  - NAG Físico BR — 2026-09-04: farelo MT/IMEA R$ 1.875,45/ton (var +4,44%), Rondonópolis/MT R$ 1.900,00/ton (congelado desde 31/08), RS média R$ 1.860,00/ton (congelado em toda a janela de 14 dias do dump); prêmios export Paranaguá farelo +0,12 USD/short ton e óleo +0,10 cts/lb, ambos congelados desde pelo menos 26/08
  - CFTC COT Managed Money, Swap Dealers e Producer/Merchant — corte de 2026-09-01 (terça-feira), inalterado desde a leitura anterior; comparação com o corte de 2026-08-25
  - USDA Crop Progress — corte de 2026-08-30 (12% excelente / 46% boa / 9% ruim), sem atualização nova; comparação com 2026-08-23 (12%/48%/9%)
  - USDA WASDE — ausente da janela deste briefing
  - NOPA — fila `release-nopa-2026-09-06`; `monthly_status` segue em 0,0 bool (paywall) em todas as datas do dump, de 2026-08-27 a 2026-09-06
  - ABIOVE projeções mensais — balanços set-dez/2026, sem revisão nesta janela
  - NOAA CPC ENSO — El Niño Advisory, inalterado de 2026-08-27 a 2026-09-06
  - MPOB — carimbo 2026-09-06, parser sem números extraídos (mesma barreira)
  - BCBA (Argentina) — carimbo 2026-09-06, scraper acessa a página mas não encontra links de relatório
  - INMET — previsão para 2026-09-07 (hoje): Mato Grosso/Goiás com pancadas de chuva e trovoadas isoladas mantidas em todo o núcleo produtor (Cuiabá 31°C/16°C, Sinop 36°C/18°C, Sorriso 36°C/20°C, Lucas do Rio Verde 34°C/17°C, Rio Verde/GO 30°C/20°C); no Sul, Cascavel/PR sobe para 21°C/6°C (ante 17°C/? em 06/09) e Maringá/PR 22°C/10°C seguem nublados sem menção de chuva, enquanto Passo Fundo/RS registra geada pela manhã (17°C/0°C, "Poucas nuvens com geada")
  - Notícias Agrícolas/Canal Rural + FarmProgress RSS — 2026-09-06: "160 items lidos, 6 mantidos (soja/farelo/oleo)", sem headline legível nova no dump para essa data; última manchete disponível segue sendo a de 05/09 ("Cepea: Soja e boi gordo sustentam ganhos na semana; milho perde fôlego", Canal Rural)
  - system/tributario_watch.toml (lido como referência, não editado) — `atualizado_em` 2026-06-05 em todos os 10 eventos catalogados, agora 94 dias sem revisão
  - Forecasts estatísticos internos (bandas 7d/30d, MA20+volatilidade+slope) — geração de 2026-09-06, alvos 13/09 (7d) e 06/10 (30d); viés "altista" em soja, farelo e óleo nos dois horizontes, calculado sobre o mesmo fechamento de 04/09
  - Fila de julgamento — carimbada 2026-09-06 no briefing, 7 itens; tratados nesta leitura: `alerta-quebra_resistencia-soja_cbot-2026-09-04`, `alerta-quebra_suporte-oleo_cbot-2026-09-04`, `alerta-quebra_resistencia-farelo_cbot-2026-09-04`, `alerta-quebra_suporte-complexo_soja-2026-09-04`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, `release-nopa-2026-09-06`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`
  - Cruza com [[2026-09-06_leitura-complexo]] (leitura de ontem, que documentou a terceira sessão seguida de persistência do ISF/ISO) e com [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (tese original do spread Far/Soj, cuja revisão D+90 vence em 2 dias)
status: ativa
vies: [bull-soja, bull-farelo, bear-oleo_soja]
---

## Visão geral

Hoje, segunda-feira 07/09/2026, é **Labor Day nos Estados Unidos** — o feriado federal
que cai sempre na primeira segunda-feira de setembro (calendário oficial, não um dado do
briefing) — e por isso a CBOT (bolsa de grãos de Chicago) e a NYMEX não tiveram pregão
pleno hoje. É por isso que o dump de hoje continua trazendo, como último fechamento
oficial de soja, farelo e óleo, a sexta-feira 04/09: já é o **terceiro dia corrido sem
sessão nova** (sábado, domingo e agora a segunda-feira de feriado). A única exceção é o
heating oil (diesel de aquecimento, o combustível de referência para o cálculo da margem
de biodiesel americana), que teve uma reabertura de domingo à noite (carimbada 06/09)
com volume de apenas 410 contratos — cerca de 1% do volume de sexta — e sem sequer um
campo de "fechamento" preenchido, sinal de que foi um pregão eletrônico fino, não uma
sessão plena. Na prática, para o trader, isso significa que **todos os níveis técnicos e
indicadores derivados citados hoje ainda são o retrato de sexta-feira**; o primeiro teste
real de preço só deve vir amanhã, terça-feira 08/09, quando os EUA voltam a operar.

Para quem não acompanha o dia a dia: a soja em grão vira, na esmagadora (o processo de
"crush"), dois produtos com demandas diferentes — farelo (proteína para ração animal) e
óleo (alimentação humana e biodiesel). O crush margin mede, em dólares por bushel (uma
unidade de medida agrícola americana, ~27,2 kg de soja), quanto sobra para quem esmaga
depois de vender farelo + óleo e pagar a soja; é o incentivo econômico bruto para a
indústria continuar processando. O oil share (fatia do valor total do crush que vem do
óleo, os dois somando 100%) diz qual dos dois produtos está "pagando a conta" da
esmagadora naquele momento: quando o oil share sobe, o óleo manda no crush e o farelo
vira insumo residual, mais barato, "sobra" — daí o nome do índice sintético interno
"Índice de Sobra de Farelo" (ISF). Quando o oil share cai, a lógica inverte: o farelo
passa a sustentar o crush e o óleo perde força relativa, o que o índice espelhado
"Índice de Suporte do Óleo" (ISO) capta pelo lado inverso. O ratio Far/Soj (preço do
farelo dividido pelo preço da soja, normalizado) é a métrica clássica de mercado para a
mesma ideia: abaixo de 80% o farelo está "abundante" (barato relativo à soja); a partir
de 87% ele está "apertado" (caro relativo à soja, sinal de escassez).

Mesmo sem preço novo, dois relógios continuam correndo e é isso que dá substância à
leitura de hoje. Primeiro: os índices sintéticos ISF e ISO, que romperam o patamar
anterior em 03/09 (saindo de 80/100 para 60/80), **fecharam a quarta sessão seguida
parados exatamente em 60/100 e 80/100** (indicators, carimbos de 03, 04, 05 e 06/09) —
quatro leituras de datas diferentes com o mesmo valor é evidência mais forte de mudança
estrutural do que as três sessões documentadas ontem. Segundo, e mais urgente: a revisão
D+90 da tese de compressão do spread Far/Soj (aberta em 11/06/2026,
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`) vence em
**2026-09-09 — faltam apenas 2 dias corridos** a partir de hoje. O ratio Far/Soj fechou
04/09 em 79,76% (indicators), a **0,24 ponto percentual** do patamar de 80% que definiria
convergência técnica da tese. **Leitura de uma linha**: o pivô do complexo continua sendo
a realocação de valor do óleo para o farelo dentro do crush — bull-farelo, bear-óleo —
agora entrando na reta final antes do prazo formal de revisão da tese de três meses,
enquanto a soja mantém viés altista moderado sustentado por folga técnica e câmbio;
confiança geral **moderada-alta**, reduzida pela ausência total de preço novo há três
dias e por um COT que já soma 6 dias de defasagem.

## Soja

**Viés: bull, moderado — sem novidade de preço pelo terceiro dia seguido, mas nenhum dos
pilares da tese de alta foi contestado, e a condição de lavoura americana segue com viés
de piora marginal como pano de fundo fundamentalista.**

O que sustenta a tese:

- **A folga sobre o rompimento técnico de julho segue larga e intacta.** Soja CBOT
  fechou em 1.309,75 USD cts/bushel em 04/09/2026 (CME CBOT), **10,99%** acima da
  resistência de 1.180,00 monitorada pela fila
  (`alerta-quebra_resistencia-soja_cbot-2026-09-04`). Como não houve pregão desde então
  — nem sábado, nem domingo, nem hoje (Labor Day) — essa distância é exatamente a mesma
  de sexta-feira, o que também quer dizer que nenhum evento testou essa margem de
  segurança em três dias corridos.
- **O câmbio, no último dado disponível, seguia trabalhando a favor do produtor
  brasileiro.** USD/BRL fechou 04/09 em 5,1253 (BCB PTAX), +0,57% sobre 03/09 (5,0962).
  A paridade em reais da soja (CBOT × câmbio, sem basis) fechou em **R$ 147,99/saca**
  (indicators, 04/09) — mesmo com a soja em dólar caindo -0,49% naquele pregão (de
  1.316,25 para 1.309,75), a paridade em reais quase não recuou porque a desvalorização
  do real compensou a queda em Chicago. É o lembrete mecânico de sempre: para quem
  vende em reais, o que importa é a combinação dos dois preços, não cada um isolado.
- **O físico exportador confirma o mesmo movimento.** CEPEA/ESALQ Soja Paranaguá (via
  NAG) fechou 04/09 em R$ 160,87/saca, +0,46% sobre 160,14 — alta coerente com a
  reversão cambial de sexta. O físico do Paraná interior (via NAG) também subiu, R$
  152,10/saca (+0,28% sobre 151,68).
- **A condição da lavoura americana seguiu piorando marginalmente na última leitura
  semanal disponível**, um fator fundamentalista de sustentação, não de preço direto.
  USDA Crop Progress de 30/08/2026 mostrou a soma "boa+excelente" (G/E, o indicador-
  resumo mais usado pelo mercado) em **58%** (12% excelente + 46% boa), ante **60%** em
  23/08/2026 (12% + 48%) — queda de 2 pontos percentuais na fração "boa", com a fração
  "ruim" estável em 9%. O mecanismo: quanto pior a condição relatada pelo USDA perto da
  fase de enchimento de grãos, maior o risco de revisão de produtividade para baixo nos
  próximos relatórios — um viés de fundo levemente altista que independe de câmbio ou
  posicionamento de fundos.

**O que invalida / risco:**

- **A ausência de pregão novo corta dos dois lados, e hoje é o dia mais "sem fato" da
  semana.** Nenhum pilar foi contestado, mas nenhum também foi reforçado por um evento
  de mercado novo desde sexta-feira. A folga de 10,99% é idêntica à de sexta, não uma
  folga "crescente" — segunda-feira (Labor Day) foi um não-evento por definição de
  calendário, e o teste real só vem amanhã.
- **O crush margin segue na mínima da janela, agora seis sessões seguidas abaixo do
  referencial de US$ 2,50** monitorado pela fila
  (`alerta-quebra_suporte-complexo_soja-2026-09-04`): fechou em US$ 2,1408/bushel
  (04/09), **-14,37%** abaixo do referencial. Isso é um freio de fundo — se a margem de
  esmagamento continuar comprimida, a esmagadora tem menos incentivo para processar
  soja, reduzindo no médio prazo a demanda física por grão — ainda que, como será
  detalhado na seção Óleo, a origem específica da compressão seja o óleo, não a soja.
- **Nível técnico a vigiar:** um fechamento de volta abaixo de 1.180 desfaria o
  rompimento; a folga (10,99%) é confortável, mas congelada há três dias.
- **Efeito colateral do feriado americano sobre o calendário de dados:** o USDA Crop
  Progress semanal normalmente sai na tarde de segunda-feira (horário dos EUA); como
  hoje é feriado federal, é razoável esperar (calendário do USDA, não confirmado neste
  dump) que o corte desta semana saia terça-feira, 08/09, em vez de hoje — o que
  atrasaria em um dia a atualização do dado de 30/08, hoje já com 8 dias de defasagem.

**Leitura operacional:** não há gatilho técnico novo para reduzir posição comprada — a
tese de rompimento segue intacta e sem contestação por três dias corridos. Para quem
opera o lado vendido, a soja isoladamente segue sem sinal de reversão. O ponto mais
acionável desta janela sem pregão é de calendário: amanhã, terça-feira, traz o primeiro
teste pós-feriado de todos os níveis técnicos do complexo, com o mercado americano tendo
ficado três dias corridos sem conseguir reagir a nenhuma notícia do fim de semana.

## Farelo

**Viés: bull, forte — sem preço novo pelo terceiro dia seguido, mas o ratio Far/Soj está
a apenas 0,24 ponto percentual de cruzar o patamar de 80% que definiria a "convergência"
da tese de três meses, e a revisão formal dessa tese vence em apenas 2 dias.**

O que sustenta a tese (na fita, congelada desde sexta):

- **O preço estabilizou depois do salto da véspera, sem sinal de desmonte.** Farelo
  CBOT fechou em 348,20 USD/short ton em 04/09/2026, -0,11% sobre 03/09 (348,60) — uma
  variação quase nula depois de uma sessão de alta relevante em 03/09 (+1,66% sobre
  342,90 de 02/09). A folga sobre a resistência de 325,00
  (`alerta-quebra_resistencia-farelo_cbot-2026-09-04`) ficou em **7,14%**.
- **A curva futura segue estável, sem sinal de desmonte da estrutura de firmeza.**
  Set/26 345,30 → out/26 (base) 348,20 → dez/26 355,10 → jan/27 358,00 → mar/27 359,60
  → mai/27 360,30 (CME CBOT, 04/09) — contango moderado e sem distorções, coerente com
  expectativa de firmeza sustentada, não de um pico isolado.
- **O ratio Far/Soj encadeou a segunda alta seguida e está muito perto do patamar-chave
  de 80%.** Fechou em **79,76%** em 04/09 (indicators), ante 79,45% em 03/09 e 78,51%
  em 02/09 — depois de ter caído de 78,87% (31/08) para 78,51% (02/09), o ratio
  reverteu e subiu por duas sessões consecutivas, um ganho acumulado de +1,25 ponto
  percentual em dois pregões. **Faltam apenas 0,24 ponto percentual** para o ratio
  cruzar 80%, o limiar que a tese original de 11/06/2026 chamou de zona "apertada" e
  que define, na prática, se a convergência esperada nesta revisão será considerada
  confirmada ou não. Como não houve pregão novo, esse número está congelado exatamente
  onde estava sexta-feira — a proximidade não cresceu, mas também não recuou.
- **O físico brasileiro deu o maior salto da janela.** Farelo MT/IMEA (NAG) fechou em
  R$ 1.875,45/ton em 04/09, +4,44% sobre os R$ 1.795,68 nos quais ficou travado desde
  28/08 — o segundo salto desse tamanho em menos de duas semanas (o primeiro foi o
  próprio movimento de 1.726,20 para 1.795,68 em 28/08, +4,03%). Rondonópolis/MT (R$
  1.900,00/ton) e a média do RS (R$ 1.860,00/ton) seguem congelados.
- **O COT de 01/09, agora com 6 dias de defasagem, segue sendo o dado de posicionamento
  mais forte do complexo, mesmo sem confirmação recente.** O net long de managed money
  em farelo saltou **+63,83%** na semana encerrada em 01/09 (de 95.953 para 157.179
  contratos, CFTC COT, vs. corte de 25/08) — o maior salto proporcional das três pernas
  (soja +17,06%, óleo +17,28%). A posição vendida dos fundos em farelo caiu **-37,60%**
  (de 33.662 para 21.004 contratos) — boa parte do movimento foi desmonte de posição
  vendida (recompra para zerar/inverter), sinal de mudança de convicção tipicamente mais
  forte do que compra de posição nova. O open interest total em farelo também cresceu
  +6,68% (608.353 → 649.027 contratos), mostrando entrada de capital novo, não apenas
  rotação entre posições existentes.

**Trata a fila `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
(seguindo 🔴 VENCIDA no briefing):** a tese original de 11/06/2026 previa convergência
do ratio Far/Soj para a zona 80-87% em D+7 — vencida há muito tempo. Já são **88 dias
corridos** desde o alerta original (11/06 a 07/09), e o ratio, depois de meses abaixo de
80%, está a 0,24 ponto percentual de cruzar esse patamar pela primeira vez desde então —
o mais perto que a tese chegou de uma confirmação técnica direta.

**Trata também `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`:**
vence em **2026-09-09**, faltam **2 dias corridos** a partir de hoje (07/09) — a janela
mais estreita desde a abertura da tese. O quadro que chega à revisão é o mesmo que
sustentou a leitura de ontem, sem deterioração nem confirmação adicional: duas sessões
seguidas de alta do ratio antes do fim de semana, o COT de 01/09 mostrando fluxo de
fundos migrando para farelo antes dessa recuperação, e o ISF/ISO agora sustentando o
novo patamar por **quatro** sessões seguidas (uma a mais que ontem). Se amanhã
(terça-feira, primeiro pregão pós-feriado) trouxer uma alta do ratio suficiente para
cruzar 80%, a revisão de 09/09 encontraria a tese tecnicamente confirmada; se o ratio
recuar ou ficar estável abaixo de 80%, a revisão registraria "convergência parcial, não
confirmada". A decisão será tomada com apenas UM pregão de margem (terça-feira) entre
hoje e o vencimento.

**O que invalida / risco:** toda a força da tese desde sexta vem de dados que já
existiam antes do fim de semana e do feriado — não há confirmação nova há três dias
corridos. O maior risco específico continua sendo o próprio COT: o corte de 01/09 é uma
fotografia de seis dias atrás, e o próximo corte (posições de 08/09) só sai na sexta
11/09, dois dias depois do vencimento da revisão D+90. Ou seja, **a decisão sobre a tese
em 09/09 será tomada sem o dado de posicionamento mais recente** — risco de julgamento
que se mantém sem solução.

**Leitura operacional:** para quem está comprado em farelo diretamente, a folga técnica
(7,14%) e a proximidade do ratio ao patamar de 80% sustentam manter a posição sem
gatilho de redução. Para quem opera o spread Far/Soj (long farelo / short soja, ou o
crush apostando na compressão), esta é a última janela antes do vencimento formal da
revisão: restam efetivamente um único pregão (terça-feira) para o ratio se mover antes
da data de corte de 09/09. Isso argumenta por decidir o tamanho da posição com base no
que já se sabe agora — ratio a 0,24pp de 80%, ISF/ISO estruturalmente sustentando o novo
patamar por quatro leituras seguidas — em vez de esperar uma confirmação de preço ou de
COT que pode não chegar a tempo.

## Óleo

**Viés: bear, moderado a forte — terceira queda seguida (na fita de sexta) sustentada
por quatro sessões de estabilidade nos índices estruturais, mas ainda sem confirmação de
que os fundos desmontaram a posição comprada que tinham até 01/09.**

O que sustenta o lado vendido / cético:

- **Três quedas seguidas, com desaceleração de magnitude.** Óleo CBOT fechou em 68,89
  USD cts/lb em 04/09/2026, -1,06% sobre 03/09 (69,63) — depois de -2,50% em 02/09 e
  -1,43% em 03/09, somando -4,91% acumulados desde o fechamento de 01/09 (72,45). A
  magnitude diária vem diminuindo (-2,50% → -1,43% → -1,06%), consistente com perda de
  momentum, mas a mínima de 04/09 (67,77) ficou **4,32%** abaixo do suporte de 72,00
  rompido três sessões antes (`alerta-quebra_suporte-oleo_cbot-2026-09-04`).
- **A curva futura inteira recuou de forma ampla em 04/09** — base (out/26) -1,06%,
  dez/26 e além com quedas semelhantes — reforçando que o movimento não é isolado do
  contrato-base, mas uma reprecificação de toda a estrutura a termo.
- **Oil share e oil-meal spread aprofundam a divergência, e agora com QUATRO sessões de
  confirmação.** O oil share fechou em **49,73%** em 04/09 (indicators) — a segunda
  sessão seguida abaixo de 50% e a quarta queda seguida desde 01/09 (51,17% → 50,74% →
  49,97% → 49,73%). O oil-meal spread (valor do óleo menos valor do farelo, em
  USD/bushel) aprofundou o território negativo para **-0,0825** em 04/09, ante -0,0099
  em 03/09. Mas o dado mais importante é que os índices sintéticos ISF (60/100) e ISO
  (80/100) ficaram **parados por uma quarta sessão seguida** (03, 04, 05 e 06/09,
  indicators) — a persistência por quatro carimbos de data diferentes eleva ainda mais
  a confiança de que a mudança estrutural identificada no início da semana passada é
  duradoura, não ruído de um pregão isolado.
- **O COT de 01/09 (agora 6 dias de defasagem) mostra os fundos ainda líquidos
  compradores em óleo, um contraponto que segue sem resolução.** O net long de managed
  money em óleo cresceu +17,28% (85.116 → 99.823 contratos, CFTC COT), com a posição
  vendida caindo -16,85% (29.132 → 24.223). Como o corte é anterior às quedas de
  03-04/09, é plausível que parte dessas posições compradas já esteja no vermelho —
  mas isso **não está confirmado neste dump**, e o próximo corte (posições de 08/09) só
  sai depois de mais uma semana.

O que ainda sustenta o lado comprado / a cautela contra vender:

- **A margem de biodiesel americana segue melhorando, não piorando — tendência que já
  soma cinco sessões.** Margem de 1,7385 USD/galão em 04/09, ante 1,7364 em 03/09
  (indicators) — alta marginal de +0,12%, mas o quadro de médio prazo é mais nítido:
  desde 31/08 (1,5480), a margem subiu **+12,31%** acumulados, mesmo com o óleo caindo
  em quatro das cinco sessões do período. O mecanismo: o custo do óleo como insumo caiu
  mais rápido (-1,06% em 04/09, refletindo a própria queda do óleo) do que a receita
  (-0,69%, puxada pela queda do heating oil, de referência ~4,59 em 03/09 para 4,5402
  em 04/09 USD/galão, CME NYMEX HO=F) — óleo mais barato barateia o principal insumo do
  blender de biodiesel americano, um amortecedor estrutural contra a leitura de que a
  fraqueza do óleo reflita destruição de demanda de biodiesel nos EUA. A reabertura fina
  de domingo (06/09) do heating oil, com abertura em 4,5804 USD/galão — entre a mínima
  (4,4338) e o fechamento (4,5402) de sexta —, não muda essa leitura por si só, dado o
  volume irrisório (410 contratos) e a ausência de um fechamento oficial para essa
  sessão.
- **O RIN D4 (crédito de biocombustível, EPA) segue estável.** 1,5×RIN = 2,11 USD/galão
  embutido no cálculo de receita em 03/09 e 04/09 (indicators) — o arcabouço
  regulatório do EPA RFS 2026/2027 (`EPA-RFS-2026-2027`, vigente desde 15/06/2026)
  segue intacto e sustentando esse número.
- **O catalisador Danantara segue pendente, agora 6 dias após o marco-alvo.** A
  assunção plena da centralização da exportação de palma pela Indonésia
  (`DANANTARA-INDONESIA`, tributario_watch.toml) tinha alvo 01/09/2026 — já se passaram
  6 dias sem qualquer notícia neste dump confirmando execução. Segue como catalisador de
  alta represado, não invalidado nem confirmado.

**O que invalida / risco:** o contraponto mais forte contra a tese bear segue sendo o
COT — fundos líquidos compradores em óleo até 01/09 é, no mínimo, sinal de que o
"dinheiro grande" não via a queda como início de tendência estrutural até aquela data.
Como o próximo corte (posições de 08/09) só sai na sexta 11/09, o mercado vai operar
ainda mais uma semana sem saber se essa convicção comprada resistiu às quedas adicionais
de 03-04/09 ou se já começou a ceder. Para o lado comprado, o nível a vigiar é se o
preço reconquista e sustenta acima de 67,77 (mínima de 04/09) já na reabertura de
terça-feira.

**Leitura operacional:** a divergência estrutural farelo-forte / óleo-fraco dentro do
crush segue sendo o trade mais bem sustentado do complexo — agora com quatro sessões de
confirmação dos índices sintéticos, não apenas preço. Para quem opera direcional
vendido em óleo, isso sustenta manter posição, mas o tamanho deveria continuar
respeitando o sinal contraditório do COT (ainda sem confirmação de desmonte). Para quem
opera o spread farelo-óleo (long farelo / short óleo em valor relativo dentro do crush),
a assimetria de posicionamento — COT forte a favor do farelo, ausente do lado vendido em
óleo — permanece um argumento para dimensionar a perna comprada com mais convicção do
que a vendida.

## Spreads e crush (leitura de complexo)

A ausência de pregão novo — agora por três dias corridos, incluindo o feriado de hoje —
não pausou a validação da tese estrutural, ao contrário: prorrogou-a por mais uma
sessão sem reversão, o que é em si um dado. O oil share caiu pela quarta sessão seguida,
de 51,17% (01/09) para **49,73% (04/09)**, e os índices sintéticos ISF/ISO, que
romperam o patamar anterior em 03/09, sustentaram o novo nível (60/100 e 80/100) por
**quatro carimbos de data consecutivos** (03, 04, 05 e 06/09) — a persistência por
múltiplas leituras, mesmo sem preço novo entre a segunda e a quarta, é o tipo de
evidência que separa uma mudança estrutural de um ruído de um único pregão.

O crush margin atingiu US$ 2,1408/bushel em 04/09 (-1,16% sobre 03/09), a sexta sessão
seguida abaixo do referencial de US$ 2,50
(`alerta-quebra_suporte-complexo_soja-2026-09-04`), **-14,37%** abaixo desse nível. A
composição segue a mesma lógica das leituras anteriores: o farelo praticamente não caiu
(-0,11%), enquanto o óleo puxou o total para baixo (-1,06%) — a compressão do crush tem
origem identificável no óleo, não uma fraqueza difusa nas duas pernas simultaneamente.

O ratio Far/Soj, por sua vez, encadeou a segunda alta seguida e fechou a 0,24 ponto
percentual do patamar de 80% — a menor distância desde que a tese de compressão do
spread foi aberta em 11/06/2026. Para quem opera o spread Far/Soj, a combinação destes
três fatos — ratio a uma fração de ponto de 80%, ISF/ISO sustentando por quatro
sessões, e COT de 01/09 mostrando fundos migrando para farelo antes da virada de preço —
monta o quadro mais favorável à tese de convergência desde seu início, exatamente na
janela em que a revisão formal D+90 vence (09/09, faltam **2 dias**). A tensão que esta
leitura não resolve, e que se repete de leituras anteriores, é que o mesmo COT mostra os
fundos ainda líquidos compradores em óleo (+17,28%) — a divergência de preço e de
índices estruturais entre farelo e óleo ainda não tem, pelo menos até 01/09, uma
contrapartida simétrica de posicionamento vendido em óleo. O spread está mais bem
sustentado do lado comprado (farelo) do que do lado vendido (óleo).

Do lado dos fundamentos brasileiros de médio prazo (ABIOVE, projeções mensais para
set-dez/2026, sem revisão nesta janela), o balanço projetado mostra o estoque final de
soja no Brasil recuando de 7.912 mil toneladas em set/26 para 5.721 (out/26), 3.659
(nov/26) e 1.890 mil toneladas (dez/26) — o esvaziamento sazonal esperado do carregamento
da safra 25/26 à medida que exportação e esmagamento consomem o excedente antes da
colheita da safra 26/27. Do lado do farelo, a produção projetada também recua ao longo do
período (2.128 → 2.143 → 1.978 → 1.659 mil toneladas, set→dez/26) na mesma cadência de
desaceleração do esmagamento, enquanto a exportação projetada cai de 1.100 mil toneladas
(set/26) para 700 mil toneladas (dez/26) — uma trajetória que, se confirmada, tende a
aliviar a oferta doméstica de farelo ao longo do próximo trimestre e é, portanto, um
fator a favor da tese de recuperação do ratio Far/Soj no horizonte de meses, não apenas
de dias.

## Lente fiscal/regulatória BR

Antes de fechar qualquer tese de preço BR, os vetores tributários/regulatórios vivos que
pesam no complexo — todos do `system/tributario_watch.toml`, cujo carimbo mais recente
(`atualizado_em`) em todos os 10 eventos catalogados é 2026-06-05, ou seja, **94 dias
sem revisão humana**:

- **MP 1.363/2026** (id `MP-1363-2026`, subvenção diesel fóssil R$ 1,12/L, vigente até
  31/12/2026): barateia o diesel fóssil no mix B15, reduzindo a competitividade relativa
  do biodiesel e a demanda doméstica por óleo de soja — vetor estrutural de baixa para
  óleo, direção "baixa" no cadastro, sem mudança de status. Não confundir com a margem
  de biodiesel AMERICANA (mercado e mecanismo diferentes), que hoje segue em trajetória
  de alta (ver seção Óleo).
- **B16 (id `B16-CNPE-2026`, elevação da mistura de biodiesel para 16%)** segue
  "adiado" — resultado dos testes técnicos esperado por volta de novembro/2026. Upside
  represado (~436 mil toneladas de demanda potencial adicional de óleo, direção "alta"
  no cadastro), não corrente. Com o oil share hoje em 49,73%, um estímulo futuro de
  demanda por óleo via B16 teria efeito ainda mais visível sobre esse indicador do que
  teria em um cenário de oil share alto.
- **Isenção de PIS/Cofins do biodiesel na mistura** (id `PISCOFINS-BIODIESEL-ISENCAO`):
  vigência registrada até 31/07/2026 — já **38 dias corridos vencida** frente a
  07/09/2026, sem qualquer registro de prorrogação ou expiração no arquivo. Status
  tratado como "desconhecido pós-vigência", não como fato de vigência ou caducidade.
- **MP 1.358/2026** (subvenção gasolina R$ 0,89/L): vigência registrada até 11/07/2026,
  agora **58 dias corridos vencida**, mesma lacuna de informação sobre renovação.
- **STJ REsp 2.165.276** (id `STJ-RESP-2165276`, crédito de PIS/Cofins sobre soja em
  biodiesel sob suspensão tributária, direção "alta" para soja/óleo): alívio de custo
  pontual, não vinculante, sem novidade nesta janela.
- **EPA RFS 2026/2027** (id `EPA-RFS-2026-2027`, mandato de biocombustível americano,
  vigente desde 15/06/2026, direção "alta" para óleo): sustenta o RIN D4, estável há
  pelo menos cinco sessões — o arcabouço segue intacto e explica parte da resiliência da
  margem de biodiesel americana mesmo com o óleo caindo.
- **Crédito 45Z** (id `45Z-CLEAN-FUEL`, em tramitação, direção "mista"): sem novidade.
- **Indonésia — Danantara** (id `DANANTARA-INDONESIA`) e **levy de exportação PMK
  9/2026** (id `INDONESIA-LEVY-PMK9`): tratados na seção Óleo — marco-alvo (01/09) já 6
  dias vencido sem confirmação de execução, catalisador represado, não invalidado.
- **Indonésia B50** (id `INDONESIA-B50`, monitorando, direção "alta"): sem novidade
  nesta janela — retórica oficial de meta jul/26 seguia, no último cadastro, contestada
  por quota flat e capacidade insuficiente, com expectativa mais realista de B45 em
  2026 e B50 pleno só em 2027-28.

## Riscos e eventos próximos

- **Reabertura de terça-feira, 08/09** — primeiro teste real de todos os níveis
  técnicos (soja 1.180, farelo 325, óleo 72, crush margin 2,50, mínima do óleo 67,77)
  depois de TRÊS dias corridos sem negociação plena (sábado, domingo e o feriado de
  Labor Day de hoje); risco de gap de abertura em qualquer direção, potencialmente
  amplificado pelo acúmulo de um dia extra de fim de semana prolongado.
- **Revisão D+90 da tese do ratio Far/Soj**
  (`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`), vencendo em
  **2026-09-09**, faltam **2 dias**. O ratio está a 0,24 ponto percentual de 80% — resta
  efetivamente um único pregão (terça-feira) antes do prazo formal de revisão.
- **Próximo corte CFTC COT** — posições de terça 08/09, publicação estimada por volta de
  sexta 11/09 (inferência a partir do calendário semanal do CFTC, não confirmada no
  briefing) — chega DEPOIS do vencimento da revisão D+90, o que significa que a decisão
  de 09/09 será tomada sem o dado de posicionamento mais atual.
- **USDA Crop Progress semanal**: normalmente publicado segunda-feira à tarde (horário
  EUA); como hoje é feriado federal (Labor Day), é razoável esperar atraso para
  terça-feira, 08/09 (inferência de calendário, não confirmada no briefing) —
  atualizaria o dado de 30/08 (12%/46%/9%, G/E 58%), já com 8 dias de defasagem frente a
  hoje.
- **Confirmação (ou não) da centralização plena da exportação de palma pela
  Danantara** — marco-alvo era 01/09, já se passaram 6 dias.
- **NOPA mensal** (`release-nopa-2026-09-06`): mensagem de paywall idêntica em todas as
  datas do dump de 27/08 a 06/09 (pelo menos 11 dias corridos) — o gap de dado de crush
  americano segue sem solução, e a nova "release" carimbada em 06/09 não trouxe
  informação adicional além do mesmo aviso de acesso pago.
- **USDA WASDE**: ausente da janela; catalisador potencial de revisão de balanço
  mundial.
- **Vigência da isenção PIS/Cofins do biodiesel** (38 dias vencida) e **MP 1.358/2026 da
  gasolina** (58 dias vencida) — checar notícia de renovação/expiração antes de assumir
  qualquer tese de custo de combustível BR.
- **Persistência (ou reversão) do oil share abaixo de 50% e do oil-meal spread
  negativo** — quatro e duas sessões seguidas respectivamente, com o ISF/ISO agora
  sustentando o novo patamar por quatro carimbos de data; a tendência até aqui é de
  aprofundamento e consolidação, não de reversão.
- **Clima**: previsão de 07/09 (hoje) mantém chuva e trovoadas isoladas no núcleo
  produtor de Mato Grosso e Goiás (Cuiabá, Sinop, Sorriso, Lucas do Rio Verde, Rio
  Verde/GO) — relevante para a janela de plantio da safra 2026/27 que se aproxima. No
  Sul, Cascavel/PR recupera temperatura (21°C/6°C ante o dia anterior) e Passo Fundo/RS
  segue registrando geada (mínima de 0°C) — indicativo de que a transição para a
  primavera ainda não se completou no Rio Grande do Sul, sem relevância direta para a
  soja (ainda não plantada na região).

## Honestidade

- **Não houve pregão pleno em Chicago desde sexta-feira, 04/09 — hoje, segunda-feira
  07/09, é o terceiro dia corrido sem sessão, e é feriado federal americano (Labor Day),
  primeira segunda-feira de setembro.** Essa identificação de feriado é inferência de
  calendário geral, não um dado extraído do briefing — está sendo usada apenas para
  explicar a ausência de dado novo, não como fato de mercado citável com fonte interna.
  Todos os preços, curvas futuras e indicadores derivados (crush margin, ratio, oil
  share) citados nesta leitura repetem os insumos do fechamento de sexta. O que esta
  leitura acrescenta em relação à de ontem é interpretação de tempo decorrido (contagem
  de dias, prazos de revisão, persistência de índices sintéticos por mais um carimbo de
  data) e não uma nova leitura de mercado.
- **A expectativa de atraso do USDA Crop Progress para terça-feira também é inferência
  de calendário (feriado de hoje), não confirmada no briefing** — se o relatório sair
  hoje por algum motivo, ou se atrasar além de terça, esta leitura não teria como saber.
- **O COT de 01/09 tem agora 6 dias de defasagem frente a hoje (07/09).** Toda a leitura
  sobre "fundos sustentando a migração para farelo" segue sendo uma inferência de
  sequência temporal (o corte é anterior às altas do ratio em 03-04/09), não uma
  confirmação direta — e o próximo corte (08/09) só será publicado depois do vencimento
  da revisão D+90 (09/09), criando uma lacuna de informação relevante para essa decisão.
- **Percentil histórico de posicionamento COT não está disponível no briefing** — toda
  leitura de "fundos comprando/vendendo" usa variação semana a semana de contratos
  absolutos, não percentil histórico; não sabemos se o net long atual de farelo (157.179
  contratos) está em nível historicamente esticado ou ainda modesto.
- **`tributario_watch.toml` sem atualização há 94 dias** — pelo menos dois vetores
  (isenção PIS/Cofins do biodiesel, MP 1.358/2026) já passaram da data de vigência
  registrada sem nota de renovação ou expiração. Tratados como "status desconhecido
  pós-vigência", não como fato de caducidade real.
- **NOPA segue inacessível** (paywall) — mensagem idêntica em pelo menos 11 datas
  consecutivas do dump, inclusive uma nova "release" carimbada em 06/09 que não trouxe
  dado novo; tratado como falso positivo repetido na fila, não como dado novo relevante.
- **USDA WASDE ausente** da janela — nenhuma leitura de balanço mundial oficial
  atualizado disponível.
- **Forecasts estatísticos internos (bandas 7d/30d) gerados em 06/09 embutem viés
  "altista" nas três pernas, inclusive no óleo** — mas usam MA20+volatilidade+slope
  sobre o mesmo fechamento de 04/09 usado nesta leitura, sem incorporar
  qualitativamente a divergência estrutural farelo-vs-óleo. O viés "altista" do forecast
  de óleo não deve ser lido como contradição da leitura bear de curto prazo desta
  análise — são horizontes e métodos diferentes.
- **MPOB (palma Malásia) segue com parser quebrado** — nenhum dado de produção/estoque
  de palma malaia disponível para cruzar com a tese de substituição via Indonésia.
- **BCBA (Argentina) segue sem links de relatório detectados pelo scraper** — nenhum
  dado de safra ou exportação argentina disponível nesta janela.
- **A previsão INMET para 07/09 é previsão meteorológica, não medição de precipitação
  real** — a menção a "pancadas de chuva" nos boletins de Cuiabá/Sinop/Lucas do Rio
  Verde/Sorriso/Rio Verde é tratada como chuva PREVISTA no boletim, não como confirmação
  de que choveu ou vai chover de fato.
- **Prêmios de exportação (Paranaguá, farelo e óleo) seguem congelados em toda a janela
  de 14 dias do dump** (pelo menos desde 26/08) — não dá para saber se isso reflete
  mercado físico export realmente parado ou limitação de atualização da fonte (NAG).
- **A reabertura fina do heating oil em 06/09 (410 contratos, sem fechamento oficial)
  não foi tratada como sinal de direção** — volume baixo demais e ausência de campo de
  fechamento tornam esse dado não confiável para qualquer conclusão de tendência.
- **A tensão entre o COT bullish em óleo (+17,28% net long até 01/09) e a leitura bear
  de preço/estrutura desta análise permanece o ponto de maior incerteza qualitativa** —
  não há como saber, com os dados disponíveis, se os fundos já reduziram essa posição
  comprada em reação às quedas de 03-04/09, ou se estavam comprando a correção. Essa
  ambiguidade não deve ser resolvida por especulação; fica registrada como aberta.
