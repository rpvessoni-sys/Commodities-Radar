---
data: 2026-09-06
titulo: "Segundo domingo sem pregão novo desde o fechamento de sexta (04/09): o preço trava, mas o relógio não — a revisão D+90 do spread Far/Soj vence em 3 dias, o índice de Sobra de Farelo/Suporte de Óleo já soma TRÊS sessões seguidas parado em 60/80 (confirmação estrutural, não ruído de um dia), e o COT de 01/09 completa 5 dias de defasagem sem confirmação de que os fundos sustentaram a migração para farelo depois da virada do ratio"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT (ZSX26 soja / ZMV26 farelo / ZLV26 óleo) — última sessão negociada: 2026-09-04 (sexta-feira). Soja: abertura 1.316,00, máxima 1.320,75, mínima 1.305,75, fechamento 1.309,75 USD cts/bushel, volume 167.214 contratos. Farelo: abertura 349,00, máxima 350,80, mínima 345,50, fechamento 348,20 USD/short ton, volume 27.570 contratos. Óleo: abertura 69,30, máxima 69,67, mínima 67,77, fechamento 68,89 USD cts/lb, volume 32.370 contratos. Curva futura em 04/09 — soja: set/26 1.293,75, nov/26 (base) 1.309,75, jan/27 1.325,00, mar/27 1.330,25, mai/27 1.334,50, jul/27 1.335,25; farelo: set/26 345,30, out/26 (base) 348,20, dez/26 355,10, jan/27 358,00, mar/27 359,60, mai/27 360,30; óleo: set/26 68,78, out/26 (base) 68,89, dez/26 69,27, jan/27 69,43, mar/27 69,55, mai/27 69,60
  - CME NYMEX heating oil (HO=F) — 2026-09-04: abertura 4,5976, fechamento 4,5402, máxima 4,6026, mínima 4,4338 USD/galão, volume 39.031 contratos
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, ISF, ISO, margem biodiesel, paridade BR) — série 2026-08-31 a 2026-09-05 (o cálculo de 05/09 repete os insumos de preço de 04/09, sem pregão novo no fim de semana)
  - BCB PTAX — 2026-09-04: USD/BRL 5,1253, EUR/BRL 5,9546, Selic diária 0,05166% a.a. (séries SGS 1, 21619, 11), sem publicação em 05-06/09 (fim de semana)
  - CEPEA/ESALQ Soja Paranaguá via NAG — 2026-09-04: R$ 160,87/saca (var +0,46%)
  - CEPEA/ESALQ Soja Paraná interior via NAG — 2026-09-04: R$ 152,10/saca (var +0,28%)
  - NAG Físico BR — 2026-09-04: farelo MT/IMEA R$ 1.875,45/ton (var +4,44%), Rondonópolis/MT R$ 1.900,00/ton (congelado desde 31/08), RS média R$ 1.860,00/ton (congelado em toda a janela de 14 dias do dump); prêmios export Paranaguá farelo +0,12 USD/short ton e óleo +0,10 cts/lb, ambos congelados desde pelo menos 26/08 (todo o período coberto pelo dump)
  - CFTC COT Managed Money, Swap Dealers e Producer/Merchant — corte de 2026-09-01 (terça-feira), inalterado desde a leitura anterior; comparação com o corte de 2026-08-25
  - USDA Crop Progress — corte de 2026-08-30 (12% excelente / 46% boa / 9% ruim), sem atualização nova; comparação com 2026-08-23 (12%/48%/9%)
  - USDA WASDE — ausente da janela deste briefing
  - NOPA — fila `release-nopa-2026-09-05`; `monthly_status` segue em 0,0 bool (paywall) em todas as datas do dump, de 2026-08-27 a 2026-09-05
  - ABIOVE projeções mensais — balanços set-dez/2026, sem revisão nesta janela
  - NOAA CPC ENSO — El Niño Advisory, inalterado de 2026-08-27 a 2026-09-05
  - MPOB — carimbo 2026-09-05, parser sem números extraídos (mesma barreira)
  - BCBA (Argentina) — carimbo 2026-09-05, scraper acessa a página mas não encontra links de relatório
  - INMET — previsão para 2026-09-06 (hoje): núcleo de Mato Grosso com queda expressiva de temperatura frente ao boletim de ontem (Cuiabá 26°C/16°C hoje vs 37°C/27°C em 05/09) mantendo chuva e trovoadas isoladas; Sinop 36°C/19°C, Lucas do Rio Verde 34°C/18°C e Sorriso 35°C/22°C seguem com chuva prevista; no Sul, Passo Fundo/RS registra geada (11°C/1°C, "Claro com geada"), Cascavel/PR 16°C/4°C e Maringá/PR 19°C/10°C seguem com nebulosidade sem menção de chuva
  - Notícias Agrícolas/Canal Rural + FarmProgress RSS — 2026-09-05: "160 items lidos, 10 mantidos (soja/farelo/oleo)", headline legível: "Cepea: Soja e boi gordo sustentam ganhos na semana; milho perde fôlego" (Canal Rural)
  - system/tributario_watch.toml (lido como referência, não editado) — `atualizado_em` 2026-06-05 em todos os 10 eventos catalogados, agora 93 dias sem revisão
  - Forecasts estatísticos internos (bandas 7d/30d, MA20+volatilidade+slope) — geração de 2026-09-05, alvos 12/09 (7d) e 05/10 (30d); viés "altista" em soja, farelo e óleo nos dois horizontes, calculado sobre o mesmo fechamento de 04/09 (sem pregão novo para recalibrar)
  - Fila de julgamento — carimbada 2026-09-05 no briefing, 7 itens; tratados nesta leitura: `alerta-quebra_resistencia-soja_cbot-2026-09-04`, `alerta-quebra_suporte-oleo_cbot-2026-09-04`, `alerta-quebra_resistencia-farelo_cbot-2026-09-04`, `alerta-quebra_suporte-complexo_soja-2026-09-04`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, `release-nopa-2026-09-05`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`
  - Cruza com [[2026-09-05_leitura-complexo]] (leitura de ontem, que tratou o mesmo fechamento de sexta e introduziu o COT de 01/09 como primeira evidência de posicionamento) e com [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (tese original do spread Far/Soj, cuja revisão D+90 vence nesta semana)
status: ativa
vies: [bull-soja, bull-farelo, bear-oleo_soja]
---

## Visão geral

Hoje é domingo, 06/09/2026, e este é o **segundo dia corrido seguido sem pregão novo**
em Chicago — o dado de preço mais recente do briefing continua sendo o fechamento de
sexta-feira, 04/09. Isso muda a natureza do que dá para entregar hoje: não há um
"evento de mercado" novo para narrar, mas há um relógio que continua correndo por
baixo do preço parado — prazos de revisão de tese, contagens de dias de defasagem de
dados, e um índice estrutural que, ao ficar parado por uma terceira sessão seguida,
na verdade está dizendo algo (ver abaixo). Esta leitura trata o fechamento de sexta
como o fato de preço vigente e usa o tempo extra corrido desde então para atualizar o
que mudou de contexto, não de cotação.

Para quem não acompanha o dia a dia: a soja em grão vira, na esmagadora (o processo de
"crush"), dois produtos com demandas diferentes — farelo (proteína para ração animal)
e óleo (alimentação humana e biodiesel). O crush margin mede, em dólares por bushel
(uma unidade de medida agrícola americana, ~27,2 kg de soja), quanto sobra para quem
esmaga depois de vender farelo + óleo e pagar a soja; é o incentivo econômico bruto
para a indústria continuar processando. O oil share (fatia do valor total do crush que
vem do óleo, os dois somando 100%) diz qual dos dois produtos está "pagando a conta" da
esmagadora naquele momento. Quando o oil share sobe, o óleo manda no crush e o farelo
vira insumo residual, mais barato, "sobra" — daí o nome do índice sintético interno
"Índice de Sobra de Farelo" (ISF). Quando o oil share cai, a lógica inverte: o farelo
passa a sustentar o crush e o óleo perde força relativa, o que o índice espelhado
"Índice de Suporte do Óleo" (ISO) capta pelo lado inverso. O ratio Far/Soj (preço do
farelo dividido pelo preço da soja, normalizado) é a métrica clássica de mercado para a
mesma ideia: abaixo de 80% o farelo está "abundante" (barato relativo à soja); a partir
de 87% ele está "apertado" (caro relativo à soja, sinal de escassez).

Na sexta-feira, 04/09, a soja caiu -0,49% (de 1.316,25 para 1.309,75 USD cts/bushel,
CME CBOT) e o farelo praticamente empatou, -0,11% (de 348,60 para 348,20 USD/short
ton), enquanto o óleo caiu -1,06% (de 69,63 para 68,89 USD cts/lb) — a **terceira
sessão seguida de queda** no óleo, somando -4,91% acumulados desde o fechamento de
01/09 (72,45 → 68,89). O oil share fechou em **49,73%** (indicators, 04/09), a segunda
sessão seguida abaixo de 50% e a quarta queda seguida desde 01/09 (51,17% → 50,74% →
49,97% → 49,73%). O dado mais relevante para a leitura de hoje, porém, é outro: os dois
índices sintéticos ISF e ISO, que romperam o patamar anterior em 03/09 depois de duas
semanas travados, **ficaram parados pela terceira sessão seguida** em 60/100 e 80/100
(indicators, 03, 04 e 05/09) — três carimbos de data diferentes, mesmo valor. Isso
importa mecanicamente: um movimento que aparece uma vez pode ser ruído; um movimento
que se sustenta por três sessões consecutivas, mesmo sem preço novo empurrando, é
evidência de que a mudança estrutural identificada no início da semana (farelo forte,
óleo fraco dentro do crush) não é um solavanco passageiro. **Leitura de uma linha**: o
pivô do complexo continua sendo a realocação de valor do óleo para o farelo dentro do
crush — bull-farelo, bear-óleo — com o spread Far/Soj (`revisao-2026-06-11_ratio-81-
prepara-janela-de-tranches-farelo-D+90`) entrando na semana decisiva de sua tese de três
meses (vence em **3 dias**, 09/09), enquanto a soja mantém viés altista moderado
sustentado por folga técnica e câmbio, com confiança geral **moderada-alta**, reduzida
pela ausência de qualquer atualização de posicionamento (COT) ou de preço nos últimos
dois dias.

## Soja

**Viés: bull, moderado — sem novidade de preço, mas nenhum dos pilares da tese de alta
foi contestado, e o crop condition americano piorou marginalmente, um contraponto
fundamentalista que soma a favor.**

O que sustenta a tese:

- **A folga sobre o rompimento técnico de julho segue larga.** Soja CBOT fechou em
  1.309,75 USD cts/bushel em 04/09/2026 (CME CBOT), **10,99%** acima da resistência de
  1.180,00 monitorada pela fila (`alerta-quebra_resistencia-soja_cbot-2026-09-04`).
  Como não houve pregão desde então, essa distância está exatamente onde estava na
  sexta — mas o fato de o número não ter se movido em dois dias corridos (sábado e
  domingo) não é neutro: significa que não houve nenhum evento de mercado, dado
  macro ou notícia que tenha testado essa distância de segurança desde então.
- **O câmbio segue trabalhando a favor do produtor brasileiro no último dado
  disponível.** USD/BRL fechou 04/09 em 5,1253 (BCB PTAX), +0,57% sobre 03/09 (5,0962)
  — a reversão de uma sequência de cinco quedas seguidas do dólar. A paridade em reais
  da soja (CBOT × câmbio, sem basis) fechou em **R$ 147,99/saca** (indicators, 04/09),
  levemente acima dos R$ 147,88 do dia anterior mesmo com a soja em dólar caindo, porque
  a desvalorização do real mais que compensou a queda em Chicago — um lembrete de que,
  para o produtor que vende em reais, o que importa é a combinação dos dois preços, não
  cada um isoladamente.
- **O físico exportador confirma o mesmo movimento.** CEPEA/ESALQ Soja Paranaguá (via
  NAG) fechou 04/09 em R$ 160,87/saca, +0,46% sobre 160,14 — alta coerente com a
  reversão cambial. O físico do Paraná interior (via NAG) também subiu, R$ 152,10/saca
  (+0,28% sobre 151,68).
- **A condição da lavoura americana piorou ligeiramente na semana, um fator
  fundamentalista de sustentação, não de preço direto.** USDA Crop Progress de
  30/08/2026 mostrou a soma "boa+excelente" (G/E, o indicador-resumo mais usado pelo
  mercado) em **58%** (12% excelente + 46% boa), ante **60%** em 23/08/2026 (12% + 48%)
  — uma queda de 2 pontos percentuais na fração "boa", com a fração "ruim" estável em
  9%. O mecanismo: quanto pior a condição relatada pelo USDA perto da fase de enchimento
  de grãos, maior o risco de revisão de produtividade para baixo nos próximos relatórios
  — um viés de fundo levemente altista que se soma, sem depender do câmbio ou da
  posição de fundos, à tese de alta.

**O que invalida / risco:**

- **A ausência de pregão novo corta dos dois lados.** Nenhum dos pilares foi
  contestado, mas nenhum também foi reforçado por um novo fato de mercado — a folga de
  10,99% é a mesma de sexta, não uma folga "crescente". Segunda-feira, 07/09, será o
  primeiro teste real de todos os níveis técnicos depois de dois dias sem negociação, e
  carrega o risco típico de abertura pós-fim de semana (gap), positivo ou negativo.
- **O crush margin segue em mínima da janela, quinta sessão seguida abaixo do
  referencial de US$ 2,50** monitorado pela fila
  (`alerta-quebra_suporte-complexo_soja-2026-09-04`): fechou em US$ 2,1408/bushel
  (04/09), -14,37% abaixo do referencial. Isso é um freio de fundo — se a margem de
  esmagamento continuar comprimida, a esmagadora tem menos incentivo para processar
  soja, reduzindo no médio prazo a demanda física por grão — ainda que, como será
  detalhado na seção Óleo, a origem específica da compressão seja o óleo, não a soja.
- **Nível técnico a vigiar:** um fechamento de volta abaixo de 1.180 desfaria o
  rompimento; a folga (10,99%) é confortável, mas não cresceu desde sexta.

**Leitura operacional:** não há gatilho técnico novo para reduzir posição comprada —
a tese de rompimento segue intacta e sem contestação nos últimos dois dias. Para quem
opera o lado vendido, a soja isoladamente segue sem sinal de reversão. O ponto mais
acionável nesta janela sem pregão é de calendário, não de preço: segunda-feira traz o
primeiro teste pós-fim de semana de todos os níveis, e o corte semanal de Crop Progress
(normalmente publicado segunda à tarde, horário dos EUA) deve atualizar o dado de 30/08,
já com 7 dias de defasagem frente a hoje.

## Farelo

**Viés: bull, forte — sem preço novo para confirmar ou desmentir, mas o ratio Far/Soj
está a apenas 0,24 ponto percentual de cruzar o patamar de 80% que definiria a
"convergência" da tese de três meses, e a revisão formal dessa tese vence em 3 dias.**

O que sustenta a tese (na fita, congelada desde sexta):

- **O preço estabilizou depois do salto da véspera, sem sinal de desmonte.** Farelo
  CBOT fechou em 348,20 USD/short ton em 04/09/2026, -0,11% sobre 03/09 (348,60) — uma
  variação quase nula depois de uma sessão de alta relevante em 03/09 (+1,66% sobre
  342,90 de 02/09). A folga sobre a resistência de 325,00
  (`alerta-quebra_resistencia-farelo_cbot-2026-09-04`) ficou em **7,14%**.
- **A curva futura segue estável, sem sinal de desmonte da estrutura de firmeza.**
  Set/26 345,30 → out/26 (base) 348,20 → dez/26 355,10 → jan/27 358,00 → mar/27 359,60
  → mai/27 360,30 (CME CBOT, 04/09) — uma curva em contango moderado e sem distorções,
  coerente com expectativa de firmeza sustentada, não de um pico isolado.
- **O ratio Far/Soj encadeou a segunda alta seguida e está muito perto do patamar-chave
  de 80%.** Fechou em **79,76%** em 04/09 (indicators), ante 79,45% em 03/09 e 78,51%
  em 02/09 — depois de ter caído de 78,87% (31/08) para 78,51% (02/09), o ratio
  reverteu e subiu por duas sessões consecutivas, um ganho acumulado de +1,25 ponto
  percentual em dois pregões. **Faltam apenas 0,24 ponto percentual** para o ratio
  cruzar 80% — o limiar que a tese original de 11/06/2026 chamou de zona "apertada" e
  que define, na prática, se a convergência esperada nesta revisão será considerada
  confirmada ou não.
- **O físico brasileiro deu o maior salto da janela.** Farelo MT/IMEA (NAG) fechou em
  R$ 1.875,45/ton em 04/09, +4,44% sobre os R$ 1.795,68 nos quais ficou travado desde
  28/08 — o segundo salto desse tamanho em menos de duas semanas (o primeiro foi o
  próprio movimento de 1.726,20 para 1.795,68 em 28/08, +4,03%). Rondonópolis/MT (R$
  1.900,00/ton) e a média do RS (R$ 1.860,00/ton) seguem congelados — o RS, aliás,
  está congelado em toda a janela de 14 dias do dump, o que pode refletir tanto mercado
  físico regional realmente parado quanto limitação de atualização da fonte.
- **O COT de 01/09 (agora com 5 dias de defasagem) segue sendo o dado de posicionamento
  mais forte do complexo, mesmo sem confirmação recente.** O net long de managed money
  em farelo saltou **+63,83%** na semana encerrada em 01/09 (de 95.953 para 157.179
  contratos, CFTC COT, vs. corte de 25/08) — o maior salto proporcional das três pernas
  (soja +17,06%, óleo +17,28%). O detalhe mecânico mais relevante: a posição vendida dos
  fundos em farelo caiu **-37,60%** (de 33.662 para 21.004 contratos) — ou seja, boa
  parte do movimento foi desmonte de posição vendida (recompra para zerar/inverter), um
  sinal de mudança de convicção tipicamente mais forte do que compra de posição nova. O
  open interest total em farelo também cresceu +6,68% (608.353 → 649.027 contratos),
  mostrando entrada de capital novo, não apenas rotação entre posições existentes.

**Trata a fila `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
(seguindo 🔴 VENCIDA no briefing):** a tese original de 11/06/2026 previa convergência
do ratio Far/Soj para a zona 80-87% em D+7 — vencida há muito tempo. Já são **87 dias
corridos** desde o alerta original (11/06 a 06/09), e o ratio, depois de meses abaixo
de 80%, está agora a 0,24 ponto percentual de cruzar esse patamar pela primeira vez
desde então — o mais perto que a tese chegou de uma confirmação técnica direta.

**Trata também `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`:**
vence em **2026-09-09**, faltam **3 dias corridos** a partir de hoje (06/09). O cenário
mudou de forma mensurável nos últimos dias: duas sessões seguidas de alta do ratio, o
COT de 01/09 confirmando fluxo de fundos migrando para farelo antes mesmo dessa
recuperação, e o ISF/ISO sustentando o novo patamar por três sessões seguidas. Se
segunda-feira (07/09) ou terça (08/09) trouxerem mais uma alta do ratio suficiente para
cruzar 80%, a revisão de 09/09 encontraria a tese tecnicamente confirmada; se o ratio
recuar, a revisão registraria "convergência parcial, não confirmada" — o resultado
ainda está em aberto, mas a margem para virar é a menor desde o início do
monitoramento.

**O que invalida / risco:** toda a força da tese desde sexta vem de dados que já
existiam antes do fim de semana — não há confirmação nova. O maior risco específico é
o próprio COT: o corte de 01/09 é uma fotografia de cinco dias atrás, e o próximo corte
(posições de 08/09) só sai na sexta 11/09, dois dias depois do vencimento da revisão
D+90. Ou seja, **a decisão sobre a tese em 09/09 provavelmente terá que ser tomada sem
o dado de posicionamento mais recente** — um risco de julgamento a registrar
explicitamente.

**Leitura operacional:** para quem está comprado em farelo diretamente, a folga técnica
(7,14%) e a proximidade do ratio ao patamar de 80% sustentam manter a posição sem
gatilho de redução. Para quem opera o spread Far/Soj (long farelo / short soja, ou o
crush apostando na compressão), esta é a semana de maior tensão desde 11/06: a revisão
formal vence em 3 dias, o ratio está a uma fração de ponto do patamar de confirmação, e
o próximo dado de posicionamento (COT de 08/09) só chega depois do prazo — o que
argumenta por decidir o tamanho da posição com base no que já se sabe agora, em vez de
esperar uma confirmação que pode não chegar a tempo.

## Óleo

**Viés: bear, moderado a forte — terceira queda seguida sustentada por três sessões
de estabilidade nos índices estruturais (não mais um evento de um dia), mas ainda sem
confirmação de que os fundos desmontaram a posição comprada que tinham até 01/09.**

O que sustenta o lado vendido / cético:

- **Três quedas seguidas, com desaceleração de magnitude.** Óleo CBOT fechou em 68,89
  USD cts/lb em 04/09/2026, -1,06% sobre 03/09 (69,63) — depois de -2,50% em 02/09 e
  -1,43% em 03/09, somando -4,91% acumulados desde o fechamento de 01/09 (72,45). A
  magnitude diária vem diminuindo (-2,50% → -1,43% → -1,06%), mecanicamente consistente
  com perda de momentum, mas a mínima de 04/09 (67,77) ficou abaixo do suporte de 72,00
  rompido três sessões antes (`alerta-quebra_suporte-oleo_cbot-2026-09-04`), agora
  **4,32%** abaixo desse nível.
- **A curva futura inteira recuou de forma ampla em 04/09** — base (out/26) -1,06%,
  dez/26 e além com quedas semelhantes — reforçando que o movimento não é isolado do
  contrato-base, mas uma reprecificação de toda a estrutura a termo.
- **Oil share e oil-meal spread aprofundam a divergência, e agora com TRÊS sessões de
  confirmação, não apenas uma.** O oil share fechou em **49,73%** em 04/09 (indicators)
  — a segunda sessão seguida abaixo de 50% e a quarta queda seguida desde 01/09
  (51,17% → 50,74% → 49,97% → 49,73%). O oil-meal spread (valor do óleo menos valor do
  farelo, em USD/bushel) aprofundou o território negativo para **-0,0825** em 04/09,
  ante -0,0099 em 03/09 — uma queda adicional de -0,0726 em um único pregão. Mas o dado
  mais importante de hoje é que os índices sintéticos ISF (60/100) e ISO (80/100)
  ficaram **parados por uma terceira sessão seguida** (03, 04 e 05/09, indicators) — a
  persistência por três carimbos de data diferentes eleva a confiança de que a mudança
  estrutural identificada no início da semana é duradoura, não ruído de um pregão.
- **O COT de 01/09 (5 dias de defasagem) mostra os fundos ainda líquidos compradores em
  óleo, um contraponto que segue sem resolução.** O net long de managed money em óleo
  cresceu +17,28% (85.116 → 99.823 contratos, CFTC COT), com a posição vendida caindo
  -16,85% (29.132 → 24.223). Como o corte é anterior às quedas de 03-04/09, é plausível
  que parte dessas posições compradas já esteja no vermelho — mas isso **não está
  confirmado neste dump**, e o próximo corte (posições de 08/09) só sai depois de mais
  uma semana.

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
  fraqueza do óleo reflita destruição de demanda de biodiesel nos EUA.
- **O RIN D4 (crédito de biocombustível, EPA) segue estável.** 1,5×RIN = 2,11
  USD/galão embutido no cálculo de receita em 03/09 e 04/09 (indicators) — o arcabouço
  regulatório do EPA RFS 2026/2027 (`EPA-RFS-2026-2027`, vigente desde 15/06/2026)
  segue intacto e sustentando esse número.
- **O catalisador Danantara segue pendente, agora 5 dias após o marco-alvo.** A
  assunção plena da centralização da exportação de palma pela Indonésia
  (`DANANTARA-INDONESIA`, tributario_watch.toml) tinha alvo 01/09/2026 — já se passaram
  5 dias sem qualquer notícia neste dump confirmando execução. Segue como catalisador de
  alta represado, não invalidado nem confirmado.

**O que invalida / risco:** o contraponto mais forte contra a tese bear segue sendo o
COT — fundos líquidos compradores em óleo até 01/09 é, no mínimo, sinal de que o
"dinheiro grande" não via a queda como início de tendência estrutural até aquela data.
Como o próximo corte (posições de 08/09) só sai na sexta 11/09, o mercado vai operar
pelo menos mais uma semana sem saber se essa convicção comprada resistiu às quedas
adicionais de 03-04/09 ou se já começou a ceder. Para o lado comprado, o nível a vigiar
é se o preço reconquista e sustenta acima de 67,77 (mínima de 04/09) já na reabertura
de segunda-feira.

**Leitura operacional:** a divergência estrutural farelo-forte / óleo-fraco dentro do
crush segue sendo o trade mais bem sustentado do complexo — agora com três sessões de
confirmação dos índices sintéticos, não apenas preço. Para quem opera direcional
vendido em óleo, isso sustenta manter posição, mas o tamanho deveria continuar
respeitando o sinal contraditório do COT (ainda sem confirmação de desmonte). Para quem
opera o spread farelo-óleo (long farelo / short óleo em valor relativo dentro do
crush), a assimetria de posicionamento — COT forte a favor do farelo, ausente do lado
vendido em óleo — permanece um argumento para dimensionar a perna comprada com mais
convicção do que a vendida.

## Spreads e crush (leitura de complexo)

A ausência de pregão novo não pausou a validação da tese estrutural — ao contrário, a
prorrogou por mais duas sessões sem reversão, o que é em si um dado. O oil share caiu
pela quarta sessão seguida, de 51,17% (01/09) para **49,73% (04/09)**, e os índices
sintéticos ISF/ISO, que romperam o patamar anterior em 03/09, sustentaram o novo nível
(60/100 e 80/100) por **três carimbos de data consecutivos** (03, 04 e 05/09) — a
persistência por múltiplas leituras, mesmo sem preço novo entre a segunda e a terceira,
é o tipo de evidência que separa uma mudança estrutural de um ruído de um único pregão.

O crush margin atingiu US$ 2,1408/bushel em 04/09 (-1,16% sobre 03/09), a quinta sessão
seguida abaixo do referencial de US$ 2,50 (`alerta-quebra_suporte-complexo_soja-2026-
09-04`), -14,37% abaixo desse nível. A composição segue a mesma lógica das leituras
anteriores: o farelo praticamente não caiu (-0,11%), enquanto o óleo puxou o total para
baixo (-1,06%) — a compressão do crush tem origem identificável no óleo, não uma
fraqueza difusa nas duas pernas simultaneamente.

O ratio Far/Soj, por sua vez, encadeou a segunda alta seguida e fechou a 0,24 ponto
percentual do patamar de 80% — a menor distância desde que a tese de compressão do
spread foi aberta em 11/06/2026. Para quem opera o spread Far/Soj, a combinação destes
três fatos — ratio a uma fração de ponto de 80%, ISF/ISO sustentando por três sessões, e
COT de 01/09 mostrando fundos migrando para farelo antes da virada de preço — monta o
quadro mais favorável à tese de convergência desde seu início, exatamente na semana em
que a revisão formal D+90 vence (09/09, faltam 3 dias). A tensão que a leitura de hoje
não resolve, e que se repete de leituras anteriores, é que o mesmo COT mostra os fundos
ainda líquidos compradores em óleo (+17,28%) — a divergência de preço e de índices
estruturais entre farelo e óleo ainda não tem, pelo menos até 01/09, uma contrapartida
simétrica de posicionamento vendido em óleo. O spread está mais bem sustentado do lado
comprado (farelo) do que do lado vendido (óleo).

## Lente fiscal/regulatória BR

Antes de fechar qualquer tese de preço BR, os vetores tributários/regulatórios vivos
que pesam no complexo — todos do `system/tributario_watch.toml`, cujo carimbo mais
recente (`atualizado_em`) em todos os 10 eventos catalogados é 2026-06-05, ou seja,
**93 dias sem revisão humana**:

- **MP 1.363/2026** (id `MP-1363-2026`, subvenção diesel fóssil R$ 1,12/L, vigente até
  31/12/2026): barateia o diesel fóssil no mix B15, reduzindo a competitividade
  relativa do biodiesel e a demanda doméstica por óleo de soja — vetor estrutural de
  baixa para óleo, direção "baixa" no cadastro, sem mudança de status. Não confundir
  com a margem de biodiesel AMERICANA (mercado e mecanismo diferentes), que hoje segue
  em trajetória de alta (ver seção Óleo).
- **B16 (id `B16-CNPE-2026`, elevação da mistura de biodiesel para 16%)** segue
  "adiado" — resultado dos testes técnicos esperado por volta de novembro/2026. Upside
  represado (~436 mil toneladas de demanda potencial adicional de óleo, direção "alta"
  no cadastro), não corrente. Com o oil share hoje em 49,73%, um estímulo futuro de
  demanda por óleo via B16 teria efeito ainda mais visível sobre esse indicador do que
  teria em um cenário de oil share alto.
- **Isenção de PIS/Cofins do biodiesel na mistura** (id `PISCOFINS-BIODIESEL-ISENCAO`):
  vigência registrada até 31/07/2026 — já **37 dias corridos vencida** frente a
  06/09/2026, sem qualquer registro de prorrogação ou expiração no arquivo. Status
  tratado como "desconhecido pós-vigência", não como fato de vigência ou caducidade.
- **MP 1.358/2026** (subvenção gasolina R$ 0,89/L): vigência registrada até 11/07/2026,
  agora **57 dias corridos vencida**, mesma lacuna de informação sobre renovação.
- **STJ REsp 2.165.276** (id `STJ-RESP-2165276`, crédito de PIS/Cofins sobre soja em
  biodiesel sob suspensão tributária, direção "alta" para soja/óleo): alívio de custo
  pontual, não vinculante, sem novidade nesta janela.
- **EPA RFS 2026/2027** (id `EPA-RFS-2026-2027`, mandato de biocombustível americano,
  vigente desde 15/06/2026, direção "alta" para óleo): sustenta o RIN D4, estável há
  pelo menos duas sessões — o arcabouço segue intacto e explica parte da resiliência da
  margem de biodiesel americana mesmo com o óleo caindo.
- **Crédito 45Z** (id `45Z-CLEAN-FUEL`, em tramitação, direção "mista"): sem novidade.
- **Indonésia — Danantara** (id `DANANTARA-INDONESIA`) e **levy de exportação PMK
  9/2026** (id `INDONESIA-LEVY-PMK9`): tratados na seção Óleo — marco-alvo (01/09) já
  5 dias vencido sem confirmação de execução, catalisador represado, não invalidado.
- **Indonésia B50** (id `INDONESIA-B50`, monitorando, direção "alta"): sem novidade
  nesta janela — retórica oficial de meta jul/26 seguia, no último cadastro, contestada
  por quota flat e capacidade insuficiente, com expectativa mais realista de B45 em
  2026 e B50 pleno só em 2027-28.

## Riscos e eventos próximos

- **Reabertura de segunda-feira, 07/09** — primeiro teste real de todos os níveis
  técnicos (soja 1.180, farelo 325, óleo 72, crush margin 2,50, mínima do óleo 67,77)
  depois de dois dias sem negociação; risco de gap de abertura em qualquer direção.
- **Revisão D+90 da tese do ratio Far/Soj**
  (`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`), vencendo em
  **2026-09-09**, faltam **3 dias**. O ratio está a 0,24 ponto percentual de 80% — a
  janela mais estreita desde 11/06 para essa tese se confirmar tecnicamente.
- **Próximo corte CFTC COT** — posições de terça 08/09, publicação estimada por volta
  de sexta 11/09 (inferência a partir do calendário semanal do CFTC, não confirmada no
  briefing) — chega DEPOIS do vencimento da revisão D+90, o que significa que a decisão
  de 09/09 provavelmente será tomada sem o dado de posicionamento mais atual.
- **Confirmação (ou não) da centralização plena da exportação de palma pela
  Danantara** — marco-alvo era 01/09, já se passaram 5 dias.
- **NOPA mensal** (`release-nopa-2026-09-05`): mensagem de paywall idêntica em todas as
  datas do dump de 27/08 a 05/09 (pelo menos 10 dias corridos) — o gap de dado de crush
  americano segue sem solução.
- **USDA WASDE**: ausente da janela; catalisador potencial de revisão de balanço
  mundial.
- **USDA Crop Progress semanal**: próximo corte normalmente segunda-feira à tarde
  (horário EUA) — atualizaria o dado de 30/08 (12%/46%/9%, G/E 58%), já com 7 dias de
  defasagem frente a hoje.
- **Vigência da isenção PIS/Cofins do biodiesel** (37 dias vencida) e **MP 1.358/2026
  da gasolina** (57 dias vencida) — checar notícia de renovação/expiração antes de
  assumir qualquer tese de custo de combustível BR.
- **Persistência (ou reversão) do oil share abaixo de 50% e do oil-meal spread
  negativo** — quatro e duas sessões seguidas respectivamente, com o ISF/ISO agora
  sustentando o novo patamar por três carimbos de data; a tendência até aqui é de
  aprofundamento e consolidação, não de reversão.
- **Clima**: previsão de 06/09 (hoje) mostra queda expressiva de temperatura em
  Cuiabá/MT (de 37°C/27°C ontem para 26°C/16°C hoje) mantendo chuva prevista — sinal de
  frente fria cruzando o núcleo produtor de Mato Grosso às vésperas da janela de
  plantio da safra 2026/27, o que pode aliviar (se confirmado) o risco de atraso de
  plantio por solo seco mencionado em leituras anteriores. No Sul, Passo Fundo/RS
  registrou geada (mínima de 1°C) — relevante para culturas de inverno da região, não
  diretamente para a soja (ainda não plantada), mas indicativo de que a transição para
  a primavera ainda não se completou no Rio Grande do Sul.

## Honestidade

- **Não houve pregão novo em Chicago desde sexta-feira, 04/09 — hoje é o segundo dia
  corrido sem sessão.** Todos os preços, curvas futuras e indicadores derivados
  (crush margin, ratio, oil share) citados nesta leitura repetem os insumos do
  fechamento de sexta. O que esta leitura acrescenta em relação à de ontem é
  interpretação de tempo decorrido (contagem de dias, prazos de revisão, persistência
  de índices sintéticos por mais um carimbo de data) e não uma nova leitura de mercado
  — isso deve ficar explícito para quem for comparar as duas leituras esperando um fato
  de preço novo que não existe.
- **Inconsistência de dado identificada no dump bruto do CME/CBOT para farelo em
  03/09:** o campo "fechamento" (348,60 USD/short ton, mesmo ticker ZMV26.CBT) diverge
  do campo "fechamento_V26" (348,20) dentro da mesma linha de dados — os dois deveriam
  representar o mesmo contrato-base. Esta leitura usou o valor "fechamento" (348,60)
  por ser o que alimenta de forma consistente os indicadores derivados (crush margin,
  ratio Far/Soj) publicados para aquela data, mas a divergência em si é registrada como
  suspeita de qualidade de dado na fonte, não como fato limpo. Em 04/09 os dois campos
  batem (348,20 em ambos), então esse problema não afeta os números do dia de
  referência principal desta leitura.
- **O COT de 01/09 tem agora 5 dias de defasagem frente a hoje (06/09).** Toda a
  leitura sobre "fundos sustentando a migração para farelo" segue sendo uma inferência
  de sequência temporal (o corte é anterior às altas do ratio em 03-04/09), não uma
  confirmação direta — e o próximo corte (08/09) só será publicado depois do vencimento
  da revisão D+90 (09/09), criando uma lacuna de informação relevante para essa decisão.
- **Percentil histórico de posicionamento COT não está disponível no briefing** — toda
  leitura de "fundos comprando/vendendo" usa variação semana a semana de contratos
  absolutos, não percentil histórico; não sabemos se o net long atual de farelo
  (157.179 contratos) está em nível historicamente esticado ou ainda modesto.
- **`tributario_watch.toml` sem atualização há 93 dias** — pelo menos dois vetores
  (isenção PIS/Cofins do biodiesel, MP 1.358/2026) já passaram da data de vigência
  registrada sem nota de renovação ou expiração. Tratados como "status desconhecido
  pós-vigência", não como fato de caducidade real.
- **NOPA segue inacessível** (paywall) — mensagem idêntica em pelo menos 10 datas
  consecutivas do dump; tratado como falso positivo repetido na fila, não como dado
  novo relevante.
- **USDA WASDE ausente** da janela — nenhuma leitura de balanço mundial oficial
  atualizado disponível.
- **Forecasts estatísticos internos (bandas 7d/30d) gerados em 05/09 embutem viés
  "altista" nas três pernas, inclusive no óleo** — mas usam MA20+volatilidade+slope
  sobre o mesmo fechamento de 04/09 usado nesta leitura, sem incorporar
  qualitativamente a divergência estrutural farelo-vs-óleo. O viés "altista" do
  forecast de óleo não deve ser lido como contradição da leitura bear de curto prazo
  desta análise — são horizontes e métodos diferentes.
- **MPOB (palma Malásia) segue com parser quebrado** — nenhum dado de produção/estoque
  de palma malaia disponível para cruzar com a tese de substituição via Indonésia.
- **BCBA (Argentina) segue sem links de relatório detectados pelo scraper** — nenhum
  dado de safra ou exportação argentina disponível nesta janela.
- **A previsão INMET para 06/09 é previsão meteorológica, não medição de precipitação
  real** — a menção a "pancadas de chuva" nos boletins de Cuiabá/Sinop/Lucas do Rio
  Verde/Sorriso é tratada como chuva PREVISTA no boletim, não como confirmação de que
  choveu ou vai chover de fato.
- **Prêmios de exportação (Paranaguá, farelo e óleo) seguem congelados em toda a janela
  de 14 dias do dump** (pelo menos desde 26/08) — não dá para saber se isso reflete
  mercado físico export realmente parado ou limitação de atualização da fonte (NAG).
- **A tensão entre o COT bullish em óleo (+17,28% net long até 01/09) e a leitura bear
  de preço/estrutura desta análise permanece o ponto de maior incerteza qualitativa** —
  não há como saber, com os dados disponíveis, se os fundos já reduziram essa posição
  comprada em reação às quedas de 03-04/09, ou se estavam comprando a correção. Essa
  ambiguidade não deve ser resolvida por especulação; fica registrada como aberta.
