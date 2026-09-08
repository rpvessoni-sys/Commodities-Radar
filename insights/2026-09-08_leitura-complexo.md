---
data: 2026-09-08
titulo: "Quarto dia corrido sem fechamento novo, mas o mercado reabre HOJE — a revisão D+90 do spread Far/Soj vence amanhã, no mesmo dia em que o primeiro preço fresco desde sexta deve aparecer, com ISF/ISO fechando a quinta sessão seguida em 60/80 e o ratio a 0,24 ponto percentual de 80%"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT (ZSX26 soja / ZMV26 farelo / ZLV26 óleo) — última sessão negociada e capturada neste dump: 2026-09-04 (sexta-feira). Soja: abertura 1.316,00, máxima 1.320,75, mínima 1.305,75, fechamento 1.309,75 USD cts/bushel, volume 167.214 contratos. Farelo: abertura 349,00, máxima 350,80, mínima 345,50, fechamento 348,20 USD/short ton, volume 27.570 contratos. Óleo: abertura 69,30, máxima 69,67, mínima 67,77, fechamento 68,89 USD cts/lb, volume 32.370 contratos. Curva futura em 04/09 — soja: set/26 1.293,75, nov/26 (base) 1.309,75, jan/27 1.325,00, mar/27 1.330,25, mai/27 1.334,50, jul/27 1.335,25; farelo: set/26 345,30, out/26 (base) 348,20, dez/26 355,10, jan/27 358,00, mar/27 359,60, mai/27 360,30; óleo: set/26 68,78, out/26 (base) 68,89, dez/26 69,27, jan/27 69,43, mar/27 69,55, mai/27 69,60
  - CME NYMEX heating oil (HO=F) — reabertura de domingo 2026-09-06 (única sessão com carimbo depois de 04/09): abertura 4,5804, fechamento 4,6684, máxima 4,7249, mínima 4,5659 USD/galão, volume 12.054 contratos (agora COM campo de fechamento preenchido, ao contrário do dump de ontem — ver seção Óleo)
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, ISF, ISO, margem biodiesel, paridade BR) — série 2026-08-31 a 2026-09-07 (os cálculos de 05, 06 e 07/09 repetem os insumos de preço de 04/09, sem pregão novo desde então)
  - BCB PTAX — 2026-09-04: USD/BRL 5,1253, EUR/BRL 5,9546, Selic diária 0,05166% a.a. (séries SGS 1, 21619, 11), sem publicação nova em 05-08/09 no dump (fim de semana + feriado duplo — ver Visão geral)
  - CEPEA/ESALQ Soja Paranaguá via NAG — 2026-09-04: R$ 160,87/saca (var +0,46%), sem atualização em 05-07/09
  - CEPEA/ESALQ Soja Paraná interior via NAG — 2026-09-04: R$ 152,10/saca (var +0,28%), sem atualização em 05-07/09
  - NAG Físico BR — 2026-09-04: farelo MT/IMEA R$ 1.875,45/ton (var +4,44%), Rondonópolis/MT R$ 1.900,00/ton (congelado desde 31/08), RS média R$ 1.860,00/ton (congelado em toda a janela de 14 dias do dump); prêmios export Paranaguá farelo +0,12 USD/short ton e óleo +0,10 cts/lb, ambos congelados desde pelo menos 26/08
  - CFTC COT Managed Money, Swap Dealers e Producer/Merchant — corte de 2026-09-01 (terça-feira), agora com 7 dias corridos de defasagem frente a hoje; comparação com o corte de 2026-08-25
  - USDA Crop Progress — corte de 2026-08-30 (12% excelente / 46% boa / 9% ruim), agora com 9 dias corridos de defasagem; comparação com 2026-08-23 (12%/48%/9%)
  - USDA WASDE — ausente da janela deste briefing
  - NOPA — fila `release-nopa-2026-09-07`; `monthly_status` segue em 0,0 bool (paywall) em todas as datas do dump, de 2026-08-27 a 2026-09-07 (12 dias corridos seguidos)
  - ABIOVE projeções mensais — balanços set-dez/2026, sem revisão nesta janela
  - NOAA CPC ENSO — El Niño Advisory, inalterado de 2026-08-27 a 2026-09-07
  - MPOB — carimbo 2026-09-07, parser sem números extraídos (mesma barreira)
  - BCBA (Argentina) — carimbo 2026-09-07, scraper acessa a página mas não encontra links de relatório
  - INMET — previsão para 2026-09-08 (HOJE, dado genuinamente novo nesta janela): Mato Grosso/Goiás mantêm pancadas de chuva e trovoadas isoladas em todo o núcleo produtor (Cuiabá 34°C/19°C, Sinop 37°C/22°C, Sorriso 36°C/23°C, Lucas do Rio Verde 37°C/21°C, Rio Verde/GO 32°C/21°C — todos alguns graus mais quentes que 07/09); no Sul, Cascavel/PR sobe para 25°C/10°C com "poucas nuvens" (céu abrindo, ante "muitas nuvens" em 07/09) e Maringá/PR sobe para 24°C/14°C ("muitas nuvens"); Passo Fundo/RS ainda registra geada pela manhã, mas mais fraca (22°C/6°C, ante 22°C/6°C — mínima subiu frente aos 0°C mencionados na leitura de 06/09, sinal de moderação gradual do frio)
  - Notícias Agrícolas/Canal Rural + FarmProgress RSS — 2026-09-07: "160 items lidos, 6 mantidos (soja/farelo/oleo)", sem headline legível nova no dump para essa data pelo terceiro dia seguido; última manchete disponível segue sendo a de 05/09 ("Cepea: Soja e boi gordo sustentam ganhos na semana; milho perde fôlego", Canal Rural)
  - system/tributario_watch.toml (lido como referência, não editado) — `atualizado_em` 2026-06-05 em todos os 10 eventos catalogados, agora 95 dias sem revisão
  - Forecasts estatísticos internos (bandas 7d/30d, MA20+volatilidade+slope) — geração de 2026-09-07, alvos 14/09 (7d) e 07/10 (30d); viés "altista" em soja, farelo e óleo nos dois horizontes, calculado sobre o mesmo fechamento de 04/09
  - Fila de julgamento — carimbada 2026-09-07 no briefing, 7 itens; tratados nesta leitura: `alerta-quebra_resistencia-soja_cbot-2026-09-04`, `alerta-quebra_suporte-oleo_cbot-2026-09-04`, `alerta-quebra_resistencia-farelo_cbot-2026-09-04`, `alerta-quebra_suporte-complexo_soja-2026-09-04`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, `release-nopa-2026-09-07`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`
  - Cruza com [[2026-09-07_leitura-complexo]] (leitura de ontem, que documentou o terceiro dia corrido de paralisação) e com [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (tese original do spread Far/Soj, cuja revisão D+90 vence amanhã)
status: ativa
vies: [bull-soja, bull-farelo, bear-oleo_soja]
---

## Visão geral

Hoje, terça-feira 08/09/2026, o calendário de feriados finalmente libera a CBOT (bolsa de
grãos de Chicago) para operar de novo — mas o dump usado nesta leitura foi coletado ANTES
do fechamento de hoje, então os preços de soja, farelo e óleo aqui ainda são os de
sexta-feira 04/09/2026. Vale explicar por que a paralisação foi tão longa: sábado e
domingo são não-pregão em qualquer bolsa; segunda-feira 07/09 foi feriado federal nos
Estados Unidos (Labor Day, primeira segunda-feira de setembro) — e, por coincidência de
calendário, também é o feriado da Independência do Brasil, 7 de setembro. É por isso que
não só a CBOT ficou fechada, mas também as fontes físicas brasileiras (CEPEA/ESALQ via
NAG, NAG Físico BR, PTAX do Banco Central) não têm nenhuma atualização entre 04/09 e
08/09: os dois lados do complexo — o preço em dólar em Chicago e o preço em real no
Brasil — tiraram feriado no mesmo dia. Essa leitura de calendário é inferência (não um
dado extraído do briefing), mas explica de forma direta por que esta é a quinta leitura
diária seguida (05, 06, 07 e agora 08/09) apoiada no mesmo fechamento-base de sexta. A
exceção parcial é o heating oil (diesel de aquecimento americano, referência para o
cálculo da margem de biodiesel dos EUA), que operou em uma sessão fina no domingo 06/09
e, ao contrário do que constava no dump de ontem, agora aparece neste dump COM um campo
de fechamento preenchido (4,6684 USD/galão) — um dado novo que muda a leitura da margem
de biodiesel, detalhado na seção Óleo.

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

O que muda hoje, mesmo sem preço novo, é o relógio: a revisão D+90 da tese de compressão
do spread Far/Soj (aberta em 11/06/2026,
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`) vence **amanhã,
2026-09-09** — falta **1 dia corrido**. E há uma reviravolta que a leitura de ontem não
podia antecipar: como o pregão de hoje (08/09) é o primeiro desde sexta, o fechamento de
hoje deve aparecer no dump de amanhã — ou seja, pela primeira vez em quase uma semana, a
revisão formal da tese vai contar com um preço fresco no dia exato do vencimento, ao
invés de decidir "no escuro" como o COT (posicionamento de fundos) continuará fazendo
(o próximo corte, com posições de 08/09, só sai por volta de 11/09, dois dias depois do
prazo). Enquanto isso, os índices sintéticos ISF e ISO — que romperam o patamar anterior
em 03/09 — fecharam a **quinta sessão seguida** parados exatamente em 60/100 e 80/100
(indicators, carimbos de 03, 04, 05, 06 e 07/09), a persistência mais longa desde a
mudança estrutural. O ratio Far/Soj fechou 04/09 em 79,76% (indicators), a **0,24 ponto
percentual** do patamar de 80%. **Leitura de uma linha**: o pivô do complexo continua
sendo a realocação de valor do óleo para o farelo dentro do crush — bull-farelo,
bear-óleo — chegando à véspera do prazo formal de revisão da tese de três meses com o
quadro mais favorável à convergência desde sua abertura, enquanto a soja mantém viés
altista moderado sustentado por folga técnica e câmbio; confiança geral **moderada-alta**,
elevada ligeiramente frente a ontem pela expectativa concreta de dado fresco amanhã, mas
ainda limitada por um COT que já soma 7 dias de defasagem.

## Soja

**Viés: bull, moderado — quarto dia corrido sem preço novo, mas nenhum dos pilares da
tese de alta foi contestado, a condição de lavoura americana segue com viés de piora
marginal como pano de fundo fundamentalista, e o primeiro teste real de preço acontece
hoje mesmo (resultado só disponível amanhã).**

O que sustenta a tese:

- **A folga sobre o rompimento técnico de julho segue larga e intacta.** Soja CBOT
  fechou em 1.309,75 USD cts/bushel em 04/09/2026 (CME CBOT), **10,99%** acima da
  resistência de 1.180,00 monitorada pela fila
  (`alerta-quebra_resistencia-soja_cbot-2026-09-04`). Como não houve pregão desde então
  — sábado, domingo, o feriado duplo de segunda e a manhã de hoje antes da coleta deste
  dump —, essa distância é exatamente a mesma de sexta-feira: quatro dias corridos em que
  a margem de segurança não foi nem ampliada nem testada.
- **O câmbio, no último dado disponível, seguia trabalhando a favor do produtor
  brasileiro.** USD/BRL fechou 04/09 em 5,1253 (BCB PTAX), +0,57% sobre 03/09 (5,0962).
  A paridade em reais da soja (CBOT × câmbio, sem basis) fechou em **R$ 147,99/saca**
  (indicators, 04/09) — mesmo com a soja em dólar caindo -0,49% naquele pregão (de
  1.316,25 para 1.309,75), a paridade em reais quase não recuou porque a desvalorização
  do real compensou a queda em Chicago. É o lembrete mecânico de sempre: para quem vende
  em reais, o que importa é a combinação dos dois preços, não cada um isolado. Como a
  PTAX também não teve publicação nova no dump entre 05 e 08/09, essa paridade está
  igualmente congelada.
- **O físico exportador confirma o mesmo movimento, também congelado.** CEPEA/ESALQ
  Soja Paranaguá (via NAG) fechou 04/09 em R$ 160,87/saca, +0,46% sobre 160,14 — alta
  coerente com a reversão cambial de sexta. O físico do Paraná interior (via NAG)
  também subiu, R$ 152,10/saca (+0,28% sobre 151,68). Nenhum dos dois teve atualização
  em 05-07/09, o que é esperado dado que 07/09 é feriado tanto nos EUA quanto no Brasil.
- **A condição da lavoura americana seguiu piorando marginalmente na última leitura
  semanal disponível**, um fator fundamentalista de sustentação, não de preço direto.
  USDA Crop Progress de 30/08/2026 mostrou a soma "boa+excelente" (G/E, o indicador-
  resumo mais usado pelo mercado) em **58%** (12% excelente + 46% boa), ante **60%** em
  23/08/2026 (12% + 48%) — queda de 2 pontos percentuais na fração "boa", com a fração
  "ruim" estável em 9%. O mecanismo: quanto pior a condição relatada pelo USDA perto da
  fase de enchimento de grãos, maior o risco de revisão de produtividade para baixo nos
  próximos relatórios — um viés de fundo levemente altista que independe de câmbio ou
  posicionamento de fundos. Esse dado já soma **9 dias corridos de defasagem** frente a
  hoje, e como ontem foi feriado nos EUA, o corte semanal desta semana (normalmente
  publicado segunda à tarde) deve ter sua divulgação deslocada para hoje ou amanhã —
  ainda não confirmado neste dump.

**O que invalida / risco:**

- **A ausência de pregão novo corta dos dois lados, mas hoje é o dia em que isso muda.**
  Nenhum pilar foi contestado, mas nenhum também foi reforçado por um evento de mercado
  novo desde sexta-feira. A folga de 10,99% é idêntica à de sexta, não uma folga
  "crescente" — e hoje, terça-feira, é justamente o dia em que o mercado volta a operar;
  o resultado dessa primeira sessão pós-feriado só chega no dump de amanhã.
- **O crush margin segue na mínima da janela, agora sete sessões seguidas abaixo do
  referencial de US$ 2,50** monitorado pela fila
  (`alerta-quebra_suporte-complexo_soja-2026-09-04`): fechou em US$ 2,1408/bushel
  (04/09), **-14,37%** abaixo do referencial. Isso é um freio de fundo — se a margem de
  esmagamento continuar comprimida, a esmagadora tem menos incentivo para processar
  soja, reduzindo no médio prazo a demanda física por grão — ainda que, como será
  detalhado na seção Óleo, a origem específica da compressão seja o óleo, não a soja.
- **Nível técnico a vigiar:** um fechamento de volta abaixo de 1.180 desfaria o
  rompimento; a folga (10,99%) é confortável, mas congelada há quatro dias.

**Leitura operacional:** não há gatilho técnico novo para reduzir posição comprada — a
tese de rompimento segue intacta e sem contestação por quatro dias corridos. Para quem
opera o lado vendido, a soja isoladamente segue sem sinal de reversão. O ponto mais
acionável desta janela é de calendário: a sessão de hoje é o primeiro teste pós-feriado
de todos os níveis técnicos do complexo, com o mercado americano tendo ficado quatro
dias corridos sem conseguir reagir a nenhuma notícia do fim de semana — um gap de
abertura em qualquer direção é plausível, e o resultado só será visível na leitura de
amanhã.

## Farelo

**Viés: bull, forte — sem preço novo pelo quarto dia seguido, mas o ratio Far/Soj está a
apenas 0,24 ponto percentual de cruzar o patamar de 80% que definiria a "convergência" da
tese de três meses, e a revisão formal dessa tese vence AMANHÃ.**

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
  em 02/09 — depois de ter caído de 78,87% (31/08) para 78,51% (02/09), o ratio reverteu
  e subiu por duas sessões consecutivas, um ganho acumulado de +1,25 ponto percentual em
  dois pregões. **Faltam apenas 0,24 ponto percentual** para o ratio cruzar 80%, o limiar
  que a tese original de 11/06/2026 chamou de zona "apertada" e que define, na prática,
  se a convergência esperada nesta revisão será considerada confirmada ou não. Esse
  número está parado exatamente onde estava sexta-feira havia quatro sessões — a
  proximidade não cresceu, mas também não recuou.
- **O físico brasileiro deu o maior salto da janela.** Farelo MT/IMEA (NAG) fechou em
  R$ 1.875,45/ton em 04/09, +4,44% sobre os R$ 1.795,68 nos quais ficou travado desde
  28/08 — o segundo salto desse tamanho em menos de duas semanas (o primeiro foi o
  próprio movimento de 1.726,20 para 1.795,68 em 28/08, +4,03%). Rondonópolis/MT (R$
  1.900,00/ton) e a média do RS (R$ 1.860,00/ton) seguem congelados.
- **O COT de 01/09, agora com 7 dias de defasagem, segue sendo o dado de posicionamento
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
(seguindo 🔴 VENCIDA no briefing):** a tese original de 11/06/2026 previa convergência do
ratio Far/Soj para a zona 80-87% em D+7 (18/06) — vencida há muito tempo. Já são **89
dias corridos** desde o alerta original (11/06 a 08/09), e o ratio, depois de meses
abaixo de 80%, está a 0,24 ponto percentual de cruzar esse patamar pela primeira vez
desde então — o mais perto que a tese chegou de uma confirmação técnica direta.

**Trata também `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`:**
vence **amanhã, 2026-09-09** — falta **1 dia corrido**. O quadro que chega à véspera da
revisão é o mesmo que sustentou as duas últimas leituras, sem deterioração: duas sessões
seguidas de alta do ratio antes do fim de semana duplo, o COT de 01/09 mostrando fluxo de
fundos migrando para farelo antes dessa recuperação, e o ISF/ISO agora sustentando o novo
patamar por **cinco** sessões seguidas (uma a mais que ontem, a série mais longa desde a
ruptura de 03/09). A diferença real em relação à leitura de ontem é de calendário: o
pregão de hoje, terça-feira, é o primeiro desde sexta — e seu fechamento deve aparecer no
dump de amanhã, no mesmo dia em que a revisão D+90 será formalmente decidida. Se o
fechamento de hoje levar o ratio a cruzar 80%, a revisão encontraria a tese tecnicamente
confirmada com dado fresco em mãos; se o ratio recuar ou ficar estável abaixo de 80%
mesmo com preço novo, a revisão teria uma leitura mais conclusiva do que as anteriores —
ao contrário de ontem, quando o cenário era decidir sem nenhum preço novo disponível.

**O que invalida / risco:** o maior risco específico continua sendo o COT: o corte de
01/09 é uma fotografia de sete dias atrás, e o próximo corte (posições de 08/09) só sai
na sexta 11/09, dois dias depois do vencimento da revisão D+90. Ou seja, mesmo com o
alívio de ter um preço fresco amanhã, **a decisão sobre a tese em 09/09 ainda será
tomada sem o dado de posicionamento mais recente** — risco de julgamento que se mantém
sem solução, apenas parcialmente mitigado pelo dado de preço.

**Leitura operacional:** para quem está comprado em farelo diretamente, a folga técnica
(7,14%) e a proximidade do ratio ao patamar de 80% sustentam manter a posição sem
gatilho de redução. Para quem opera o spread Far/Soj (long farelo / short soja, ou o
crush apostando na compressão), hoje é o último pregão antes do vencimento formal da
revisão de amanhã — o movimento de preço de hoje é, portanto, o dado mais relevante que
ainda falta antes da decisão. Isso argumenta por acompanhar o fechamento de hoje de
perto: um cruzamento de 80% no ratio já nesta sessão daria à revisão de amanhã uma
confirmação direta, sem depender de inferência sobre dados congelados.

## Óleo

**Viés: bear, moderado a forte — terceira queda seguida (na fita de sexta) sustentada por
cinco sessões de estabilidade nos índices estruturais, mas com um contraponto novo: a
reabertura do heating oil de domingo, agora com fechamento oficial, mostrou alta firme
que reforça — não enfraquece — o amortecedor da margem de biodiesel americana.**

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
- **Oil share e oil-meal spread aprofundam a divergência, e agora com CINCO sessões de
  confirmação.** O oil share fechou em **49,73%** em 04/09 (indicators) — a segunda
  sessão seguida abaixo de 50% e a quarta queda seguida desde 01/09 (51,17% → 50,74% →
  49,97% → 49,73%). O oil-meal spread (valor do óleo menos valor do farelo, em
  USD/bushel) aprofundou o território negativo para **-0,0825** em 04/09, ante -0,0099
  em 03/09. Mas o dado mais importante é que os índices sintéticos ISF (60/100) e ISO
  (80/100) ficaram **parados por uma quinta sessão seguida** (03, 04, 05, 06 e 07/09,
  indicators) — a persistência por cinco carimbos de data diferentes eleva ainda mais a
  confiança de que a mudança estrutural identificada há duas semanas é duradoura, não
  ruído de um pregão isolado.
- **O COT de 01/09 (agora 7 dias de defasagem) mostra os fundos ainda líquidos
  compradores em óleo, um contraponto que segue sem resolução.** O net long de managed
  money em óleo cresceu +17,28% (85.116 → 99.823 contratos, CFTC COT), com a posição
  vendida caindo -16,85% (29.132 → 24.223). Como o corte é anterior às quedas de
  03-04/09, é plausível que parte dessas posições compradas já esteja no vermelho — mas
  isso **não está confirmado neste dump**, e o próximo corte (posições de 08/09) só sai
  depois de mais uma semana.

O que ainda sustenta o lado comprado / a cautela contra vender:

- **A reabertura do heating oil de domingo, agora com fechamento oficial confirmado,
  é um dado genuinamente novo e reforça o amortecedor da margem de biodiesel.** Ao
  contrário do que constava no dump de ontem (sessão fina sem campo de fechamento), este
  dump traz o fechamento pleno de 06/09: abertura 4,5804, máxima 4,7249, mínima 4,5659,
  **fechamento 4,6684 USD/galão** (CME NYMEX HO=F), com volume de 12.054 contratos — bem
  mais robusto que os 410 contratos mencionados ontem, ainda que abaixo do volume de um
  pregão pleno de dia útil (39.031 em 04/09). O fechamento de 4,6684 fica **2,82% ACIMA**
  do fechamento de sexta (4,5402) — ou seja, o principal insumo de receita do biodiesel
  americano (heating oil) subiu no fim de semana, o que, mantido o custo do óleo de soja
  parado no preço de sexta, tende a AMPLIAR a margem de biodiesel calculada no próximo
  dado oficial, não reduzi-la. O mecanismo: a margem de biodiesel é receita (heating oil
  + 1,5×RIN D4) menos custo (óleo de soja + custo industrial fixo); se o heating oil sobe
  e o óleo de soja não teve pregão para acompanhar, a conta pende para mais margem — um
  contraponto direto à leitura de que a fraqueza do óleo de soja reflita destruição de
  demanda de biodiesel.
- **A margem de biodiesel americana já vinha melhorando antes disso, em uma tendência de
  cinco sessões.** Margem de 1,7385 USD/galão em 04/09, ante 1,7364 em 03/09
  (indicators) — alta marginal de +0,12%, mas o quadro de médio prazo é mais nítido:
  desde 31/08 (1,5480), a margem subiu **+12,31%** acumulados, mesmo com o óleo caindo
  em quatro das cinco sessões do período. O mecanismo: o custo do óleo como insumo caiu
  mais rápido (-1,06% em 04/09, refletindo a própria queda do óleo) do que a receita
  caía naquele mesmo pregão — óleo mais barato barateia o principal insumo do blender de
  biodiesel americano, um amortecedor estrutural contra a leitura de que a fraqueza do
  óleo reflita destruição de demanda. O salto do heating oil no fim de semana reforça
  esse amortecedor em vez de contradizê-lo.
- **O RIN D4 (crédito de biocombustível, EPA) segue estável.** 1,5×RIN = 2,11 USD/galão
  embutido no cálculo de receita em 03/09 e 04/09 (indicators) — o arcabouço regulatório
  do EPA RFS 2026/2027 (`EPA-RFS-2026-2027`, vigente desde 15/06/2026) segue intacto e
  sustentando esse número.
- **O catalisador Danantara segue pendente, agora 7 dias após o marco-alvo.** A assunção
  plena da centralização da exportação de palma pela Indonésia
  (`DANANTARA-INDONESIA`, tributario_watch.toml) tinha alvo 01/09/2026 — já se passaram 7
  dias sem qualquer notícia neste dump confirmando execução. Segue como catalisador de
  alta represado, não invalidado nem confirmado.

**O que invalida / risco:** o contraponto mais forte contra a tese bear segue sendo o
COT — fundos líquidos compradores em óleo até 01/09 é, no mínimo, sinal de que o
"dinheiro grande" não via a queda como início de tendência estrutural até aquela data. O
salto do heating oil de domingo é um segundo contraponto, mais imediato: se ele se
confirmar como sinal de mercado de energia em alta (e não como ruído de sessão fina de
fim de semana), a margem de biodiesel deve subir ainda mais quando o óleo de soja voltar
a negociar hoje, o que tende a atrair demanda de blenders e sustentar o preço do óleo em
vez de aprofundar a queda. Como o próximo corte do COT (posições de 08/09) só sai na
sexta 11/09, o mercado vai operar mais uma semana sem saber se a convicção comprada dos
fundos resistiu às quedas de 03-04/09. Para o lado comprado, o nível a vigiar é se o
preço reconquista e sustenta acima de 67,77 (mínima de 04/09) já na reabertura de hoje.

**Leitura operacional:** a divergência estrutural farelo-forte / óleo-fraco dentro do
crush segue sendo o trade mais bem sustentado do complexo — agora com cinco sessões de
confirmação dos índices sintéticos, não apenas preço. Mas o salto do heating oil de
domingo é um sinal de alerta genuíno para quem está vendido em óleo direcional: se a
energia (diesel/heating oil) está subindo, isso historicamente arrasta o complexo de
óleos vegetais via substituição em biodiesel, e a sessão de hoje é o primeiro teste de
se esse contágio já está em curso. Para quem opera o spread farelo-óleo (long farelo /
short óleo em valor relativo dentro do crush), a assimetria de posicionamento — COT forte
a favor do farelo, ausente do lado vendido em óleo — permanece um argumento para
dimensionar a perna comprada com mais convicção do que a vendida; mas o tamanho da perna
vendida em óleo deveria ser revisto à luz do movimento do heating oil antes da abertura
de hoje.

## Spreads e crush (leitura de complexo)

A ausência de pregão novo — agora por quatro dias corridos, incluindo o feriado duplo de
ontem — não pausou a validação da tese estrutural; ao contrário, prorrogou-a por mais uma
sessão sem reversão, o que é em si um dado. O oil share caiu pela quarta sessão seguida,
de 51,17% (01/09) para **49,73% (04/09)**, e os índices sintéticos ISF/ISO, que romperam
o patamar anterior em 03/09, sustentaram o novo nível (60/100 e 80/100) por **cinco
carimbos de data consecutivos** (03, 04, 05, 06 e 07/09) — a persistência por múltiplas
leituras, mesmo sem preço novo entre a segunda e a quinta, é o tipo de evidência que
separa uma mudança estrutural de um ruído de um único pregão.

O crush margin atingiu US$ 2,1408/bushel em 04/09 (-1,16% sobre 03/09), a sétima sessão
seguida abaixo do referencial de US$ 2,50
(`alerta-quebra_suporte-complexo_soja-2026-09-04`), **-14,37%** abaixo desse nível. A
composição segue a mesma lógica das leituras anteriores: o farelo praticamente não caiu
(-0,11%), enquanto o óleo puxou o total para baixo (-1,06%) — a compressão do crush tem
origem identificável no óleo, não uma fraqueza difusa nas duas pernas simultaneamente. O
salto do heating oil no fim de semana (+2,82% sobre sexta) é o primeiro sinal externo que
pode começar a reverter essa composição já na sessão de hoje, se o óleo de soja acompanhar
a energia para cima.

O ratio Far/Soj, por sua vez, encadeou a segunda alta seguida e fechou a 0,24 ponto
percentual do patamar de 80% — a menor distância desde que a tese de compressão do
spread foi aberta em 11/06/2026. Para quem opera o spread Far/Soj, a combinação destes
fatos — ratio a uma fração de ponto de 80%, ISF/ISO sustentando por cinco sessões, COT
de 01/09 mostrando fundos migrando para farelo antes da virada de preço, e a expectativa
concreta de um fechamento novo hoje que alimentará a revisão de amanhã — monta o quadro
mais favorável à tese de convergência desde seu início, exatamente na véspera do
vencimento da revisão formal D+90 (09/09, falta **1 dia**). A tensão que esta leitura não
resolve, e que se repete de leituras anteriores, é que o mesmo COT mostra os fundos ainda
líquidos compradores em óleo (+17,28%) — a divergência de preço e de índices estruturais
entre farelo e óleo ainda não tem, pelo menos até 01/09, uma contrapartida simétrica de
posicionamento vendido em óleo. O spread está mais bem sustentado do lado comprado
(farelo) do que do lado vendido (óleo).

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
(`atualizado_em`) em todos os 10 eventos catalogados é 2026-06-05, ou seja, **95 dias sem
revisão humana**:

- **MP 1.363/2026** (id `MP-1363-2026`, subvenção diesel fóssil R$ 1,12/L, vigente até
  31/12/2026): barateia o diesel fóssil no mix B15, reduzindo a competitividade relativa
  do biodiesel e a demanda doméstica por óleo de soja — vetor estrutural de baixa para
  óleo, direção "baixa" no cadastro, sem mudança de status. Não confundir com a margem de
  biodiesel AMERICANA (mercado e mecanismo diferentes), que hoje segue em trajetória de
  alta, reforçada pelo salto do heating oil no fim de semana (ver seção Óleo).
- **B16 (id `B16-CNPE-2026`, elevação da mistura de biodiesel para 16%)** segue "adiado"
  — resultado dos testes técnicos esperado por volta de novembro/2026. Upside represado
  (~436 mil toneladas de demanda potencial adicional de óleo, direção "alta" no
  cadastro), não corrente. Com o oil share hoje em 49,73%, um estímulo futuro de demanda
  por óleo via B16 teria efeito ainda mais visível sobre esse indicador do que teria em
  um cenário de oil share alto.
- **Isenção de PIS/Cofins do biodiesel na mistura** (id `PISCOFINS-BIODIESEL-ISENCAO`):
  vigência registrada até 31/07/2026 — já **39 dias corridos vencida** frente a
  08/09/2026, sem qualquer registro de prorrogação ou expiração no arquivo. Status
  tratado como "desconhecido pós-vigência", não como fato de vigência ou caducidade.
- **MP 1.358/2026** (subvenção gasolina R$ 0,89/L): vigência registrada até 11/07/2026,
  agora **59 dias corridos vencida**, mesma lacuna de informação sobre renovação.
- **STJ REsp 2.165.276** (id `STJ-RESP-2165276`, crédito de PIS/Cofins sobre soja em
  biodiesel sob suspensão tributária, direção "alta" para soja/óleo): alívio de custo
  pontual, não vinculante, sem novidade nesta janela.
- **EPA RFS 2026/2027** (id `EPA-RFS-2026-2027`, mandato de biocombustível americano,
  vigente desde 15/06/2026, direção "alta" para óleo): sustenta o RIN D4, estável há
  pelo menos cinco sessões — o arcabouço segue intacto e explica parte da resiliência da
  margem de biodiesel americana mesmo com o óleo caindo.
- **Crédito 45Z** (id `45Z-CLEAN-FUEL`, em tramitação, direção "mista"): sem novidade.
- **Indonésia — Danantara** (id `DANANTARA-INDONESIA`) e **levy de exportação PMK 9/2026**
  (id `INDONESIA-LEVY-PMK9`): tratados na seção Óleo — marco-alvo (01/09) já 7 dias
  vencido sem confirmação de execução, catalisador represado, não invalidado.
- **Indonésia B50** (id `INDONESIA-B50`, monitorando, direção "alta"): sem novidade nesta
  janela — retórica oficial de meta jul/26 seguia, no último cadastro, contestada por
  quota flat e capacidade insuficiente, com expectativa mais realista de B45 em 2026 e
  B50 pleno só em 2027-28.

## Riscos e eventos próximos

- **Fechamento de hoje, terça-feira 08/09** — primeiro teste real de todos os níveis
  técnicos (soja 1.180, farelo 325, óleo 72, crush margin 2,50, mínima do óleo 67,77)
  depois de QUATRO dias corridos sem negociação plena (sábado, domingo, o feriado duplo
  de segunda e a manhã de hoje antes da coleta deste dump); risco de gap de abertura em
  qualquer direção, potencialmente amplificado pelo acúmulo de um fim de semana
  prolongado e pelo salto do heating oil no domingo.
- **Revisão D+90 da tese do ratio Far/Soj**
  (`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`), vencendo
  **amanhã, 2026-09-09** — falta **1 dia**. O ratio está a 0,24 ponto percentual de 80%;
  o fechamento de hoje deve ser o insumo de preço mais fresco disponível para essa
  decisão.
- **Próximo corte CFTC COT** — posições de terça 08/09, publicação estimada por volta de
  sexta 11/09 (inferência a partir do calendário semanal do CFTC, não confirmada no
  briefing) — chega DEPOIS do vencimento da revisão D+90, o que significa que a decisão
  de 09/09 ainda será tomada sem o dado de posicionamento mais atual, mesmo com preço
  fresco disponível.
- **USDA Crop Progress semanal**: normalmente publicado segunda-feira à tarde (horário
  EUA); como ontem foi feriado federal (Labor Day), é razoável esperar (inferência de
  calendário, não confirmada no briefing) que o corte desta semana saia hoje ou amanhã —
  atualizaria o dado de 30/08 (12%/46%/9%, G/E 58%), já com 9 dias de defasagem frente a
  hoje.
- **Confirmação (ou não) da centralização plena da exportação de palma pela Danantara**
  — marco-alvo era 01/09, já se passaram 7 dias.
- **NOPA mensal** (`release-nopa-2026-09-07`): mensagem de paywall idêntica em todas as
  datas do dump de 27/08 a 07/09 (pelo menos 12 dias corridos) — o gap de dado de crush
  americano segue sem solução, e a nova "release" carimbada em 07/09 não trouxe
  informação adicional além do mesmo aviso de acesso pago.
- **USDA WASDE**: ausente da janela; catalisador potencial de revisão de balanço mundial.
- **Vigência da isenção PIS/Cofins do biodiesel** (39 dias vencida) e **MP 1.358/2026 da
  gasolina** (59 dias vencida) — checar notícia de renovação/expiração antes de assumir
  qualquer tese de custo de combustível BR.
- **Persistência (ou reversão) do oil share abaixo de 50% e do oil-meal spread negativo**
  — quatro e duas sessões seguidas respectivamente (no dado de preço), com o ISF/ISO
  agora sustentando o novo patamar por cinco carimbos de data; a tendência até aqui é de
  aprofundamento e consolidação, mas o salto do heating oil de domingo é o primeiro
  contraponto de mercado de energia a essa leitura.
- **Clima**: previsão de 08/09 (hoje) mantém chuva e trovoadas isoladas no núcleo
  produtor de Mato Grosso e Goiás (Cuiabá, Sinop, Sorriso, Lucas do Rio Verde, Rio
  Verde/GO), com temperaturas alguns graus mais altas que ontem — relevante para a janela
  de plantio da safra 2026/27 que se aproxima. No Sul, Cascavel/PR e Maringá/PR sobem de
  temperatura com céu abrindo, e Passo Fundo/RS segue registrando geada pela manhã, mas
  já mais fraca que a de dois dias atrás — indicativo de transição gradual para a
  primavera no Rio Grande do Sul, sem relevância direta para a soja (ainda não plantada
  na região).

## Honestidade

- **O dump usado nesta leitura foi coletado antes do fechamento de hoje — todos os
  preços de soja, farelo e óleo aqui ainda são os de sexta-feira 04/09.** A
  identificação de que hoje, terça-feira 08/09, é o primeiro pregão desde então (depois
  de sábado, domingo e o feriado duplo de segunda) é inferência de calendário — inclusive
  a coincidência entre o Labor Day americano e o feriado da Independência do Brasil em
  7 de setembro não é um dado extraído do briefing, mas conhecimento de calendário geral
  usado apenas para explicar por que fontes americanas E brasileiras ficaram paralisadas
  no mesmo dia. Todos os preços, curvas futuras e indicadores derivados (crush margin,
  ratio, oil share) citados nesta leitura repetem os insumos do fechamento de sexta. O
  que esta leitura acrescenta em relação à de ontem é: (1) a reabertura do heating oil de
  domingo agora com fechamento oficial confirmado (dado genuinamente novo), (2) a
  previsão INMET de hoje (dado genuinamente novo), e (3) interpretação de tempo decorrido
  (contagem de dias, prazos de revisão, persistência de índices sintéticos por mais um
  carimbo de data).
- **A expectativa de que o Crop Progress e o fechamento da CBOT saiam hoje/amanhã é
  inferência de calendário, não confirmada no briefing** — se algum desses relatórios
  atrasar além do esperado, esta leitura não teria como saber com antecedência.
- **O COT de 01/09 tem agora 7 dias de defasagem frente a hoje (08/09).** Toda a leitura
  sobre "fundos sustentando a migração para farelo" segue sendo uma inferência de
  sequência temporal (o corte é anterior às altas do ratio em 03-04/09), não uma
  confirmação direta — e o próximo corte (08/09) só será publicado depois do vencimento
  da revisão D+90 (09/09), criando uma lacuna de informação relevante para essa decisão.
- **Percentil histórico de posicionamento COT não está disponível no briefing** — toda
  leitura de "fundos comprando/vendendo" usa variação semana a semana de contratos
  absolutos, não percentil histórico; não sabemos se o net long atual de farelo (157.179
  contratos) está em nível historicamente esticado ou ainda modesto.
- **`tributario_watch.toml` sem atualização há 95 dias** — pelo menos dois vetores
  (isenção PIS/Cofins do biodiesel, MP 1.358/2026) já passaram da data de vigência
  registrada sem nota de renovação ou expiração. Tratados como "status desconhecido
  pós-vigência", não como fato de caducidade real.
- **NOPA segue inacessível** (paywall) — mensagem idêntica em pelo menos 12 datas
  consecutivas do dump, inclusive uma nova "release" carimbada em 07/09 que não trouxe
  dado novo; tratado como falso positivo repetido na fila, não como dado novo relevante.
- **USDA WASDE ausente** da janela — nenhuma leitura de balanço mundial oficial
  atualizado disponível.
- **A reabertura do heating oil de domingo (06/09), embora agora com fechamento oficial,
  ainda teve volume de 12.054 contratos — menos de um terço do volume de um pregão pleno
  de dia útil (39.031 em 04/09).** O sinal de alta (+2,82%) é tratado como indicativo, não
  conclusivo, dado o volume ainda reduzido para uma sessão de domingo.
- **Forecasts estatísticos internos (bandas 7d/30d) gerados em 07/09 embutem viés
  "altista" nas três pernas, inclusive no óleo** — mas usam MA20+volatilidade+slope sobre
  o mesmo fechamento de 04/09 usado nesta leitura, sem incorporar qualitativamente a
  divergência estrutural farelo-vs-óleo. O viés "altista" do forecast de óleo não deve
  ser lido como contradição da leitura bear de curto prazo desta análise — são horizontes
  e métodos diferentes.
- **MPOB (palma Malásia) segue com parser quebrado** — nenhum dado de produção/estoque de
  palma malaia disponível para cruzar com a tese de substituição via Indonésia.
- **BCBA (Argentina) segue sem links de relatório detectados pelo scraper** — nenhum dado
  de safra ou exportação argentina disponível nesta janela.
- **A previsão INMET para 08/09 é previsão meteorológica, não medição de precipitação
  real** — a menção a "pancadas de chuva" nos boletins de Cuiabá/Sinop/Lucas do Rio
  Verde/Sorriso/Rio Verde é tratada como chuva PREVISTA no boletim, não como confirmação
  de que choveu ou vai chover de fato.
- **Prêmios de exportação (Paranaguá, farelo e óleo) seguem congelados em toda a janela de
  14 dias do dump** (pelo menos desde 26/08) — não dá para saber se isso reflete mercado
  físico export realmente parado ou limitação de atualização da fonte (NAG).
- **A tensão entre o COT bullish em óleo (+17,28% net long até 01/09) e a leitura bear de
  preço/estrutura desta análise permanece o ponto de maior incerteza qualitativa** — não
  há como saber, com os dados disponíveis, se os fundos já reduziram essa posição
  comprada em reação às quedas de 03-04/09, ou se estavam comprando a correção. Essa
  ambiguidade não deve ser resolvida por especulação; fica registrada como aberta.
