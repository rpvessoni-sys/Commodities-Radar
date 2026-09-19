---
data: 2026-09-19
titulo: "Dia de reversão ampla no complexo: farelo tem a maior queda diária de toda a janela (-3,80%, para 354,70) e o ratio Far/Soj devolve quase todo o avanço dos últimos dias (-2,14 p.p., para 81,67%, a apenas 0,27 ponto do nível de abertura da tese baixista original de 81,4%), a soja rompe a sequência de altas com o primeiro fechamento negativo desde a reabertura de 11/09, e o óleo cai a nova mínima da janela repetindo pela terceira sessão seguida o padrão 'abre na máxima, vende o dia inteiro' — enquanto o COT de 15/09 (ainda anterior à reversão) mostrou fundos ampliando net long em farelo (+16,12%) e óleo (+10,65%) e reduzindo em soja (-6,12%), e o heating oil confirma pela terceira vez nesta série o mesmo padrão estrutural de dado provisório: fechamento revisado para cima e volume corrigido de ~180 para mais de 43 mil contratos"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT — sessão de **2026-09-18** (a mais recente com fechamento completo no dump de hoje; o cabeçalho do dump ainda está rotulado "2026-09-17", um dia atrás da data desta leitura — ver Honestidade sobre a defasagem normal de um dia, o mesmo padrão de todas as leituras anteriores): soja (ZSX26, venc. nov/26) abertura **1.317,50**, máxima **1.322,00**, mínima **1.300,00**, fechamento **1.303,00**, volume **108.222** contratos; farelo (ZMV26, venc. out/26) abertura **367,80**, máxima **369,40**, mínima **352,40**, fechamento **354,70**, volume **40.434** contratos; óleo (ZLV26, venc. out/26) abertura **68,70** (a própria máxima do dia), máxima 68,70, mínima **67,47**, fechamento **67,58**, volume **20.696** contratos. Curva futura em 18/09 — soja: nov/26 (base) 1.303,00, jan/27 1.319,50, mar/27 1.329,00, mai/27 1.336,25, jul/27 1.339,25; farelo: out/26 (base) 354,70, dez/26 358,60, jan/27 360,30, mar/27 361,40, mai/27 361,90; óleo: out/26 (base) 67,58, dez/26 68,13, jan/27 68,42, mar/27 68,57, mai/27 68,68
  - CME CBOT — sessão de **2026-09-17, como aparece revisada no dump de hoje** (usada como base de comparação "ontem"): soja fechamento **1.319,75** (curva: jan/27 1.336,25...), farelo fechamento **368,70**, óleo fechamento **68,68** — todos ligeiramente diferentes dos valores 1.319,50 / 368,40 / 68,53 usados na leitura de ontem ([[2026-09-18_leitura-complexo]]); ver Honestidade para a tabela completa de revisão
  - CME NYMEX heating oil (HO=F) — **2026-09-18**: abertura 4,8320, máxima 4,9398, mínima 4,7898, fechamento **4,8367** USD/galão, volume **37.512** contratos (volume normalizado, muito acima da faixa anômala de 179-203 contratos reportada nas três leituras anteriores para os mesmos dias, agora revistos — ver Honestidade e o insight dedicado desta data sobre o padrão estrutural de revisão do HO=F)
  - CME NYMEX heating oil (HO=F) — **2026-09-17, como aparece no dump de hoje**: fechamento **5,1139** USD/galão, volume **43.659** contratos — revisado frente aos 4,8284 USD/galão e 179 contratos usados na leitura de ontem (variação de preço +5,91%, variação de volume de +24.297%)
  - Indicadores sintéticos internos — **2026-09-18**: crush margin **2,2072** USD/bushel ("Board Crush: farelo 354,70 + óleo 67,58 − soja 1.303,00"), far_soj_ratio_pct **81,67%** ("farelo 354,70/sht ÷ (soja 1.303,00cts × 33,33)"), oil_share_pct **48,79%** ("valor óleo 7,43/total 15,24"), oil_meal_spread_usd_bu **-0,3696**, ISF (Índice de Sobra de Farelo) 60/100, ISO (Índice de Suporte do Óleo) 80/100, paridade BR soja **R$148,15/saca** (CBOT 1.303,00 × USD/BRL 5,1575, sem basis), biodiesel: custo_óleo 5,0685 USD/galão, receita 8,0017 USD/galão, margem **2,1332 USD/galão**
  - Indicadores sintéticos internos — **2026-09-17, valores como aparecem no dump de hoje** (revisados frente ao que a leitura de ontem usou para a mesma data): crush margin 2,4687, ratio 83,81%, oil share 48,22%, oil-meal spread -0,5566, paridade BR R$149,90, biodiesel: custo_óleo 5,151, receita 8,2789, margem **2,3279** (a leitura de ontem havia usado, para a mesma data, crush margin 2,4481, ratio 83,76%, oil share 48,19%, spread -0,5665, paridade R$149,87, margem de biodiesel **2,0537**, dita "a primeira queda depois de dois recordes, -15,2%" — ver Honestidade sobre como essa "queda" foi revisada para muito menor)
  - Indicadores sintéticos internos — série completa dos últimos cinco fechamentos disponíveis no dump de hoje (14, 15, 16, 17 e 18/09, seção `indicators`): farelo 350,20 → 360,10 → 360,90 → 368,70 → 354,70; ratio Far/Soj 80,55% → 81,92% → 81,99% → 83,81% → 81,67%; oil share 49,86% → 49,25% → 48,94% → 48,22% → 48,79%; oil-meal spread -0,0429 → -0,2354 → -0,3289 → -0,5566 → -0,3696; crush margin 2,3234 → 2,4215 → 2,3457 → 2,4687 → 2,2072; margem biodiesel 2,1028 → 2,386 → 2,4222 → 2,3279 → 2,1332
  - BCB PTAX — **2026-09-18**: USD/BRL **5,1575** (+0,10% vs 5,1521 de 17/09), EUR/BRL 5,9126 (-0,03% vs 5,9141), Selic diária 0,050788% a.a. (séries SGS 1, 21619, 11)
  - CFTC COT Managed Money — **corte de posições de 2026-09-15, dado novo desta janela** (`release-cftc_cot-2026-09-15`), quatro dias corridos de defasagem frente a hoje (19/09): farelo managed money long 195.227 (+12,80% vs 08/09), short 12.116 (-21,29%), net long 183.111 (+16,12%), open interest 683.474 (+2,38%); óleo long 126.365 (+5,23%), short 24.885 (-12,30%), net 101.480 (+10,65%), OI 605.960 (+0,66%); soja long 282.581 (-3,63%), short 41.080 (+14,25%), net 241.501 (-6,13%), OI 1.104.880 (+3,22%). Categoria "producer" (comercial): farelo producer_short subiu de 425.918 para 445.202 (+4,53%) e producer_long caiu de 106.964 para 93.936 (-12,18%); soja producer_long subiu de 291.532 para 323.727 (+11,04%)
  - CEPEA/ESALQ Soja Paranaguá e Paraná interior via NAG, e físico de farelo (MT/IMEA, Rondonópolis, RS) — última leitura ainda **2026-09-09**, agora **dez dias corridos** sem atualização própria frente a hoje; prêmios export Paranaguá (farelo +0,12 USD/short ton, óleo +0,10 cts/lb) seguem congelados desde 27/08, **23 dias corridos**
  - USDA Crop Progress — corte de 2026-09-13 (sem novo corte nesta janela, próximo esperado em 1-2 dias): 12% excelente / 46% boa / 9% ruim (G/E 58%, inalterado desde 30/08), colheita 2025/26 em **6% concluída**
  - USDA WASDE — release de 2026-09-11 (sem nova edição nesta janela, tabelas de soja em grão e óleo ainda ausentes), `release-usda_wasde-2026-09-11`: farelo Argentina 2026/27 exportação 2,99 milhões de toneladas (revisão ago→set já registrada); farelo Brasil 2025/26 exportação estável em 0,2 milhão de toneladas
  - NOPA — item de fila repetido hoje, `release-nopa-2026-09-18`: `monthly_status` em 0,0 bool (paywall, sem dado novo)
  - ABIOVE projeções mensais — balanços out-dez/2026, sem revisão nesta janela: produção de farelo recuando de 2.143 (out) para 1.978 (nov) e 1.659 mil t (dez); exportação de farelo de 850 para 800 e 700 mil t no mesmo período; óleo produção de 536 para 495 e 415 mil t; estoque final de soja de 5.721 para 3.659 e 1.890 mil t
  - NOAA CPC ENSO — El Niño Advisory, inalterado (carimbo 2026-09-18)
  - MPOB — carimbo 2026-09-18, parser sem números extraídos (mesma barreira há semanas)
  - BCBA (Argentina) — carimbo 2026-09-09, scraper acessa a página mas não encontra links de relatório
  - INMET — previsão para **2026-09-19 (HOJE)**: Cascavel/PR 22°C/16°C com pancadas de chuva, trovoadas e possível queda de granizo à noite; Maringá/PR 28°C/17°C pancadas de chuva e trovoadas; Passo Fundo/RS 19°C/14°C pancadas de chuva e trovoadas (mínima subiu de 8°C ontem para 14°C hoje, sem menção de geada); no núcleo produtor de Mato Grosso, Cuiabá 40°C/27°C (nuvens + chuva isolada), Sinop 41°C/24°C (chuva isolada), Sorriso 40°C/23°C (chuva isolada), Lucas do Rio Verde 41°C/25°C (chuva isolada), Rio Verde/GO 36°C/23°C (poucas nuvens pela manhã)
  - Notícias Agrícolas/Canal Rural + FarmProgress RSS — "0 items lidos, 0 mantidos" por nove dias corridos consecutivos (10 a 18/09), sem qualquer coleta nova desde o pico de 09/09 (160 lidos, 4 mantidos); sem visibilidade ainda sobre 19/09
  - system/tributario_watch.toml (lido como referência, não editado) — `atualizado_em` 2026-06-05 em todos os 10 eventos catalogados, **106 dias corridos** sem revisão humana frente a hoje (19/09)
  - Forecasts estatísticos internos (bandas 7d/30d) — geração de 2026-09-18, alvos 25/09 e 18/10: viés "altista" em soja, farelo e óleo nos dois horizontes
  - Fila de julgamento (carimbada 2026-09-18 no briefing, 9 itens) — tratados nesta leitura: `alerta-quebra_resistencia-soja_cbot-2026-09-18`, `alerta-quebra_suporte-oleo_cbot-2026-09-18`, `alerta-quebra_resistencia-farelo_cbot-2026-09-18`, `alerta-movimento_forte-farelo_cbot-2026-09-18`, `alerta-quebra_suporte-complexo_soja-2026-09-18`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`, `release-nopa-2026-09-18`, `release-cftc_cot-2026-09-15`
  - Cruza com [[2026-09-18_leitura-complexo]] (leitura de ontem, cujos números de 16 e 17/09 foram parcialmente revisados no dump de hoje — ver Honestidade), [[2026-09-17_ratio-far-soj-supera-nivel-de-abertura-da-tese-original-quarta-sessao]] e [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (tese original, nível de abertura do ratio 81,4%), [[2026-09-13_correcao-numeros-sessao-11set-farelo-oleo]] e [[2026-09-16_correcao-numeros-sessao-15set-ratio-salta-para-8191]] (precedentes diretos do padrão de revisão de dado que hoje ganha um terceiro registro, tratado em detalhe no insight dedicado [[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]])
status: ativa
vies: [bull-farelo, bull-soja, bear-oleo_soja]
---

## Visão geral

O complexo soja gira em torno do "crush" (esmagamento industrial): a soja em grão é
triturada e separada em farelo (concentrado proteico para ração animal, sobretudo aves e
suínos) e óleo (alimentação humana e, cada vez mais, biodiesel). Quem "manda" no crush é
definido pelo "oil share" — a fatia do valor total gerado pelo esmagamento que vem do óleo.
Oil share alto significa que a indústria esmaga atrás do valor do óleo, e o farelo "sobra"
como subproduto que precisa ser escoado a qualquer preço (o Índice de Sobra de Farelo, ISF,
mede esse lado). Oil share baixo é o oposto: o farelo passa a pagar a conta do esmagamento
e o óleo perde protagonismo relativo (o espelho é o Índice de Suporte do Óleo, ISO). O
termômetro mais direto dessa disputa é o ratio Far/Soj — preço do farelo dividido pelo
preço da soja, em percentual: abaixo de 80% o farelo está "abundante" (baixista); entre 80%
e 87% ele está "neutro"; acima de 87% ele fica "apertado" (altista). Depois de cinco sessões
seguidas subindo e aproximando-se cada vez mais da zona apertada — um movimento que as
últimas três leituras trataram como o fato mais relevante da janela —, hoje o ratio devolveu
quase todo esse avanço: caiu de **83,81%** (fechamento revisado de 17/09) para **81,67%**
(fechamento de 18/09), uma queda de **-2,14 pontos percentuais**, o maior recuo diário de
toda esta série, superando o próprio recorde de alta do dia anterior (+1,82 p.p., 16→17/09).
Em outras palavras: o indicador que vinha acelerando na direção altista pelo terceiro dia
seguido acelerou hoje, com a mesma intensidade, na direção contrária.

O que mudou hoje, especificamente, e como: farelo caiu **-3,80%** (354,70 ante 368,70 em
17/09, CME CBOT 18/09) — a maior queda percentual diária de toda a sequência iniciada em
11/09, superando em módulo o próprio recorde de alta de +2,83% (15/09). O padrão intradiário
reforça a leitura de reversão, não de simples realização de lucro marginal: farelo abriu em
367,80, chegou a uma máxima marginal de 369,40 (+0,43% sobre a abertura) e depois vendeu
ininterruptamente até 352,40 (mínima do dia, -4,21% sobre a máxima), fechando em 354,70 —
perto da mínima, com uma amplitude intradiária de 17 pontos (cerca de 4,6% do preço), a maior
faixa de negociação em um único dia de toda a janela. A soja, que havia fechado em "doji"
(indecisão) ontem depois de quatro sessões seguidas de alta, hoje rompeu essa indecisão para
o lado baixista: abriu em 1.317,50, tocou uma máxima de 1.322,00 (apenas +0,34% sobre a
abertura, uma extensão muito mais tímida que a de ontem) e caiu até 1.300,00, fechando em
1.303,00 — o **primeiro fechamento negativo da soja desde a reabertura de 11/09** (-1,27%
sobre 17/09), fechando perto da mínima do dia, não no meio do range. O óleo, por sua vez,
repetiu pela **terceira sessão seguida** o mesmo padrão intradiário identificado como
"inequivocamente vendedor" nas duas últimas leituras: abriu exatamente na máxima do dia
(68,70) e vendeu o pregão inteiro até uma nova mínima da janela, 67,47, fechando em 67,58
(-1,60% sobre 17/09) — a persistência desse padrão específico por três dias consecutivos é,
em si, uma evidência mais forte de pressão vendedora estrutural do que um único dia isolado
teria sido.

Um detalhe do mecanismo que merece explicação, porque é contraintuitivo: o oil share **subiu**
hoje, de 48,22% para 48,79% (+0,57 ponto), mesmo com o óleo caindo em preço absoluto. Isso não
significa que o óleo ficou fundamentalmente mais forte — significa que o farelo caiu ainda
mais rápido do que o óleo, então, dentro do total de valor gerado pelo crush (que caiu de
15,67 para 15,24, uma contração de -2,74%), a fatia relativa do óleo (que caiu apenas -1,59%,
de 7,55 para 7,43) cresceu simplesmente porque o denominador encolheu mais. O oil-meal spread
confirma a mesma mecânica pelo lado inverso: passou de -0,5566 para -0,3696 USD/bushel (menos
negativo, ou seja, comprimiu), porque farelo perdeu valor absoluto mais rápido que o óleo. É o
espelho exato do que vinha acontecendo nos últimos cinco dias (quando o farelo liderava a
alta e "carregava" o crush margin e o oil-meal spread na direção contrária) — hoje o mecanismo
girou 180 graus, mas o mecanismo em si é o mesmo: quem lidera o movimento do dia, para
qualquer lado, domina essas três métricas simultaneamente. O crush margin, que soma
farelo+óleo e subtrai soja, caiu de US$2,4687 para **US$2,2072/bushel** (-10,59%), a maior
queda diária percentual da série, e a distância abaixo do piso de referência de US$2,50
alargou-se de -2,08% (a menor já vista, ontem) para **-11,71%** hoje — a maior quebra desde
que esse piso passou a ser citado nesta série (fila `alerta-quebra_suporte-complexo_soja-2026-09-18`).

Há uma peça de informação genuinamente nova hoje, e ela conta uma história que antecede a
reversão: o corte de posicionamento do CFTC COT referente a **15/09** finalmente apareceu no
dump (`release-cftc_cot-2026-09-15`), depois de dez dias de defasagem citados repetidamente
nas últimas leituras. Como esse corte retrata posições de terça-feira, 15/09 — antes da
reversão de hoje —, ele não pode confirmar nem desmentir o movimento de agora, mas mostra
qual era a convicção dos fundos exatamente na fase de aceleração da alta: farelo net long
managed money subiu **+16,12%** (de 157.689 para 183.111 contratos), óleo **+10,65%** (de
91.711 para 101.480), enquanto a soja teve seu net long **reduzido em -6,13%** (de 257.258
para 241.501) — não por venda de posição comprada isoladamente, mas por uma combinação de
long caindo -3,63% e short subindo +14,25%, ou seja, os fundos não apenas venderam soja
comprada: também abriram posição vendida nova. Isso é notável porque aconteceu **durante** a
sequência de altas da soja (a soja subiu em quatro das cinco sessões antes do corte), o que
sugere que parte do mercado especulativo já estava mais cautelosa com a soja do que o preço
sozinho revelava — um alerta que hoje, com o primeiro fechamento negativo da soja, ganha
validação parcial, ainda que com a defasagem de tempo inerente ao COT.

Por fim, um segundo fio importante: pela **terceira vez** nesta série, o fechamento do
heating oil (HO=F) de uma sessão recente aparece revisado de forma material no dump do dia
seguinte — desta vez o de 17/09, de US$4,8284 (usado na leitura de ontem) para **US$5,1139**
(+5,91%), com o volume corrigido de **179 para 43.659 contratos** (mais de 240 vezes maior).
O padrão agora é claro e consistente nas três ocorrências (11/09: +3,77%; 16/09: +5,65%;
17/09: +5,91%) — sempre revisão para cima, sempre precedida de um volume artificialmente
baixo (na faixa de 180-200 contratos) que se corrige para a faixa normal (37-62 mil) só na
geração seguinte do dump. Este achado, por ser estrutural e recorrente (não um acidente
pontual), ganhou um insight dedicado hoje —
[[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]] — com a recomendação prática de
tratar sempre o fechamento de HO=F do dia mais recente do dump como provisório, e usar o de
T-1 ou T-2 para qualquer leitura de margem de biodiesel que exija confiança maior.

**Leitura de uma linha**: hoje é um dia de correção ampla, não (ainda) de reversão de tese —
farelo, soja e óleo caíram juntos, com o farelo liderando a maior queda diária de toda a
janela e devolvendo praticamente todo o avanço do ratio Far/Soj sobre o nível de abertura da
tese baixista original (81,4%, agora a apenas 0,27 ponto de distância, contra uma folga de
2,36 pontos ontem). Maior convicção: o viés continua **bull-farelo**, mas a confiança recua de
**forte** para **moderada** — a magnitude e a velocidade da reversão de hoje, justamente
quando a folga sobre a resistência (325,00) e sobre o nível de abertura da tese estavam mais
esticadas do que nunca, é o tipo de aviso que pede cautela, não descarte da tese. Confiança
**moderada e reduzida** na soja: o primeiro fechamento negativo desde 11/09 é exatamente o
gatilho que a leitura de ontem havia definido como o sinal a vigiar, e ele se confirmou.
Confiança **moderada e reforçada** no bear-óleo, com uma ressalva mais explícita de que o
argumento fundamentalista contrário (margem de biodiesel via heating oil) segue medido por um
instrumento cuja qualidade de dado é hoje uma questão comprovada, não hipotética.

## Soja

**Viés: bull, moderado e reduzido — a soja rompeu hoje a sequência de fechamentos em alta com
o primeiro fechamento negativo desde a reabertura de 11/09, exatamente o gatilho que a
leitura de ontem havia identificado como o sinal a vigiar para mudar a leitura de "pausa
saudável" para "possível esgotamento do rali".**

O que sustenta a tese:

- **A soja segue acima da resistência de referência de 1.180,00** (fila
  `alerta-quebra_resistencia-soja_cbot-2026-09-18`: fechamento 1.303,00 vs nível 1.180,00),
  uma folga de **+10,42%** — a menor desde a reabertura de 11/09 (a folga havia chegado a
  +12,86% na máxima intradiária de ontem), mas ainda uma distância confortável do nível de
  invalidação formal da tese.
- **A curva futura permanece em contango regular, sem sinal de distorção mesmo no dia de
  queda.** Em 18/09: nov/26 (base) 1.303,00 → jan/27 1.319,50 → mar/27 1.329,00 → mai/27
  1.336,25 → jul/27 1.339,25 (CME CBOT) — incrementos de +16,50 → +9,50 → +7,25 → +3,00 pontos
  entre vencimentos consecutivos, praticamente idênticos em forma aos de ontem (+16,75 →
  +9,50 → +6,50 → +3,25), o que indica que o mercado a termo não reprecificou de forma
  desproporcional o contrato mais distante — a queda de hoje foi concentrada no vencimento
  próximo, não um repricing estrutural de toda a curva.
- **A condição da lavoura americana segue estável, sem novo corte nesta janela.** USDA Crop
  Progress, corte de 13/09 (próximo esperado em 1-2 dias, por volta de 20-21/09): 12%
  excelente + 46% boa (G/E 58%, inalterado desde 30/08) e **6% da safra 2025/26 colhida**.
- **O câmbio trabalhou a favor do lado comprado em reais hoje, amortecendo parte da queda em
  dólares.** USD/BRL fechou em **5,1575** (BCB PTAX, 18/09), uma alta de +0,10% frente aos
  5,1521 de 17/09 (real um pouco mais fraco). Com a soja em dólar caindo -1,27%, a paridade
  brasileira (CBOT × câmbio, sem basis) recuou apenas **-1,17%**, de R$149,90 para
  **R$148,15/saca** (indicators, 18/09) — o câmbio absorveu cerca de um décimo da queda em
  dólar.
- **A previsão climática de hoje (19/09) traz uma frente de instabilidade mais organizada do
  que a de ontem, com chuva generalizada e um alerta pontual de granizo.** Cascavel/PR:
  máxima 22°C, mínima 16°C, "pancadas de chuva e trovoadas" com **possível queda de granizo à
  noite** (INMET, 19/09) — um risco agronômico concreto e específico (granizo pode destruir
  plântulas recém-emergidas) que não aparecia nas previsões dos dias anteriores. No núcleo
  produtor de Mato Grosso, o calor recua ligeiramente frente à previsão de ontem para hoje
  (Cuiabá 40°C, ante 42°C previstos ontem para hoje-de-ontem) mas mantém chuva isolada em
  Sinop, Sorriso, Lucas do Rio Verde — combinação de calor moderado e umidade tende a ser
  favorável à germinação da safra 2026/27 em plantio.
- **Em Passo Fundo/RS, a mínima prevista para hoje subiu de 8°C (previsão de ontem) para
  14°C (previsão de hoje)**, mantendo ausência de qualquer menção a geada — um risco que
  continua fora de cena, mas que vale monitorar à medida que a safra avança pelo Sul.

**O que invalida / risco:**

- **O primeiro fechamento negativo desde a reabertura de 11/09 aconteceu hoje** (-1,27%,
  fechando perto da mínima do dia, não no meio do range) — exatamente o segundo evento (depois
  do doji de ontem) que a leitura anterior havia definido como o gatilho para reclassificar o
  rali de "pausa saudável" para "possível esgotamento". Com dois dias seguidos sem fechamento
  em alta (um doji e agora uma queda real), a tese bull perde parte da força momentum que
  vinha sustentando a confiança "moderada-a-forte" das leituras anteriores.
- **O COT de 15/09 (`release-cftc_cot-2026-09-15`), mesmo sendo anterior à queda de hoje, já
  mostrava os fundos reduzindo net long em soja em -6,13%**, com short subindo +14,25% — uma
  combinação de realização de lucro e posicionamento vendido novo que precede e, em parte,
  ajuda a explicar o comportamento do preço nos dias seguintes. O próximo corte (posições de
  22/09, esperado por volta de 25-26/09) será decisivo para saber se esse movimento se
  acentuou durante a queda de hoje.
- **Nível técnico a vigiar:** um fechamento de volta abaixo de 1.180 desfaria formalmente o
  rompimento; com a folga ainda em +10,42%, esse cenário segue distante, mas encolheu quase 2
  pontos percentuais em dois dias (de +12,86% na máxima de ontem para +10,42% hoje).
- **Nenhuma linha nova de WASDE para soja em grão ou balanço mundial nesta janela** — a tabela
  de 11/09 ainda só traz farelo.

**Leitura operacional:** para quem está comprado, hoje é o primeiro dia da janela em que a
tese pede reavaliação ativa, não apenas proteção parcial de ganho — o padrão de dois dias sem
alta (doji + queda real) combinado com o COT já mostrando fundos reduzindo convicção antes da
queda é o conjunto de evidências mais desfavorável ao lado comprado desde a reabertura, mesmo
que o nível de invalidação formal (1.180) ainda esteja distante. Reduzir tamanho ou apertar
stop perto da mínima de hoje (1.300,00) é mais defensável agora do que ontem. Para quem opera
o lado vendido, a queda de hoje é o primeiro dado técnico realmente favorável desde a
reabertura — ainda sem quebra do nível de 1.180, mas com margem para testar uma entrada
tática com stop acima da máxima de hoje (1.322,00), monitorando de perto se a próxima sessão
confirma ou reverte o movimento.

## Farelo

**Viés: bull, moderado (rebaixado de forte) — a maior queda diária de toda a janela, no
exato momento em que o ratio estava mais próximo da zona "apertada" e a folga sobre a
resistência mais esticada de toda a série, é um aviso que a tese precisa absorver sem
descartar, dado que o pano de fundo estrutural (ABIOVE, COT pré-reversão, curva futura) não
mudou.**

O que sustenta a tese:

- **O ratio Far/Soj, mesmo depois da queda de hoje, fechou em 81,67% (indicators, 18/09)** —
  ainda dentro da zona "neutra" (80% a 87%), ainda acima do limiar de 80% pela sexta sessão
  seguida (80,25% em 11/09 → 80,55% em 14/09 → 81,92% em 15/09 → 81,99% em 16/09 → 83,81% em
  17/09, revisado → **81,67%** em 18/09). A distância até o nível de abertura da tese baixista
  original (81,4%, [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]) encolheu para
  apenas **+0,27 ponto percentual** — a menor folga desde que a sequência de reversão
  começou, e um recuo abrupto frente aos +2,36 pontos de ontem. Isso não invalida o veredito
  de reversão já registrado em
  [[2026-09-17_ratio-far-soj-supera-nivel-de-abertura-da-tese-original-quarta-sessao]] (o
  ratio segue, tecnicamente, acima do nível de abertura), mas reduz a margem de segurança
  dessa leitura a praticamente zero — um sexto dia de queda levaria o ratio de volta abaixo
  de 81,4% e reabriria a discussão sobre se a "reversão" foi definitiva ou um episódio
  temporário dentro de uma faixa mais ampla.
- **O farelo segue acima da resistência histórica de 325,00** (fila
  `alerta-quebra_resistencia-farelo_cbot-2026-09-18`: 354,70 vs 325,00), uma folga de
  **+9,14%** — ainda expressiva, mas a menor desde 15/09, depois de ter chegado a +13,35%
  ontem. A "extensão já alcançada" citada como risco técnico nas últimas duas leituras se
  materializou hoje na forma de uma correção real, não apenas hipotética.
- **A trajetória sazonal da ABIOVE para o Brasil continua apontando para alívio de oferta
  doméstica de farelo, sem revisão nesta janela**: produção projetada caindo de 2.143 mil t
  (out/26) para 1.978 (nov/26) e 1.659 mil t (dez/26); exportação de 850 para 800 e 700 mil t
  no mesmo período — o pano de fundo estrutural de médio prazo não se alterou com a queda de
  um dia.
- **O COT de 15/09 (pré-reversão) mostrou os fundos ampliando net long em farelo em
  +16,12%** (de 157.689 para 183.111 contratos), com managed money long subindo +12,80% e
  short caindo -21,29% — a maior variação percentual de net long de toda a série de COT
  disponível até aqui. Esse dado, por ser de terça-feira (antes da queda de sexta), não pode
  confirmar que os fundos mantiveram essa posição durante a reversão de hoje, mas mostra que
  a convicção institucional estava, até três dias atrás, claramente na direção altista — o
  próximo corte (posições de 22/09) é o primeiro capaz de dizer se a queda de hoje já provocou
  realização de lucro por parte desses mesmos fundos.
- **A curva futura do farelo mantém a mesma inclinação achatada de curto prazo já observada
  em leituras anteriores**: out/26 (base) 354,70 → dez/26 358,60 (+3,90) → jan/27 360,30
  (+1,70) → mar/27 361,40 (+1,10) → mai/27 361,90 (+0,50) — ainda em contango regular, sem
  sinal de que o mercado a termo esteja precificando a queda de hoje como o início de uma
  reversão estrutural (se estivesse, seria mais comum ver o contango se esticar ou a curva
  próxima cair proporcionalmente mais que a distante, o que não ocorreu aqui).

**O que a queda de hoje expõe como risco — e por que a confiança recua para moderada:**

- **A queda de -3,80% é a maior de toda a janela em módulo, maior até que o próprio maior
  ganho diário (+2,83%, 15/09).** Combinada com a maior queda diária do ratio (-2,14 p.p.,
  também recorde da série), essa é a evidência tecnicamente mais forte já registrada contra a
  continuidade linear da tese — mesmo que o nível estrutural (ratio ainda >80%, ainda acima
  do nível de abertura) permaneça intacto.
- **Os índices sintéticos ISF e ISO seguem travados em 60/100 e 80/100**, agora oito dias
  corridos sem qualquer mudança desde 11/09, apesar de o ratio ter subido e caído mais de 2
  pontos percentuais em dias consecutivos — os limiares que disparam essas métricas compostas
  continuam distantes do comportamento observado.
- **O físico brasileiro segue completamente congelado — agora dez dias corridos.** Última
  leitura ainda 09/09 (farelo MT/IMEA R$1.875,45/ton; prêmio export Paranaguá +0,12 USD/short
  ton, congelado desde 27/08, já 23 dias corridos). Nenhuma reação do mercado físico doméstico
  à volatilidade de Chicago desta semana pôde ser observada.
- **O WASDE de setembro segue como contraponto estrutural de médio prazo**: exportação de
  farelo argentino 2026/27 em **2,99 milhões de toneladas** (`release-usda_wasde-2026-09-11`,
  sem mudança nesta janela).
- **A extensão sobre a resistência de 325,00, mesmo reduzida para +9,14%, ainda deixa espaço
  para uma continuação da correção** antes que o nível de invalidação técnica (325,00) entre
  em jogo — um segundo dia seguido de queda de magnitude semelhante à de hoje levaria a folga
  a menos de 5%.

**Leitura operacional:** para quem está comprado em farelo (ou no spread Far/Soj comprado —
farelo comprado/soja vendido), hoje é o primeiro dia da janela em que reduzir tamanho ou
proteger ganho é claramente mais defensável do que adicionar posição — a maior queda diária
da série, justamente no ponto de maior extensão, é o tipo de sinal técnico que normalmente
precede pelo menos uma segunda sessão de teste antes de qualquer retomada. Para quem está
vendido em farelo, hoje é a primeira oportunidade tática real desde 11/09 — mas com uma
ressalva importante: o nível estrutural do ratio (81,67%, ainda >80%) e o pano de fundo
sazonal da ABIOVE não mudaram, então uma entrada vendida aqui é mais defensável como operação
tática de reversão de curto prazo do que como aposta de que a tese de fundo (farelo
estruturalmente mais apertado até dezembro) esteja invalidada.

## Óleo

**Viés: bear, moderado e reforçado — terceira sessão seguida com o mesmo padrão intradiário
"abre na máxima, vende o dia inteiro", uma nova mínima da janela, e o argumento
fundamentalista contrário (margem de biodiesel) agora comprovadamente medido por um
instrumento de qualidade de dado frágil, documentada em detalhe pela terceira vez.**

O que sustenta a tese (preço e estrutura de crush):

- **Óleo fechou em 67,58 USD cts/lb (CME CBOT, 18/09)**, queda de -1,60% frente aos 68,68
  (valor de 17/09 revisado). O padrão intradiário repete, pela terceira sessão consecutiva, a
  mesma assinatura identificada nas duas últimas leituras como "inequivocamente vendedor":
  o óleo **abriu no próprio topo do dia** (68,70) e vendeu ininterruptamente até uma nova
  mínima da janela, **67,47** (-1,79% sobre a abertura), fechando em 67,58 — recuperando
  apenas 0,16% da mínima antes do sino de fechamento. Volume de 20.696 contratos, dentro da
  faixa histórica recente. A fila confirma a permanência abaixo do suporte de 72,00
  (`alerta-quebra_suporte-oleo_cbot-2026-09-18`), com a distância agora em **-6,14%** — a
  maior desde a reabertura da tese de correção, ampliando os -4,82% de ontem.
- **A persistência do padrão "abre na máxima" por três sessões seguidas (16, 17 e 18/09) é,
  por si só, uma evidência mais forte de pressão vendedora estrutural do que qualquer sessão
  isolada** — em cada uma dessas três sessões, o primeiro negócio do dia foi também o melhor
  preço do dia, o que descreve um mercado em que a demanda compradora não consegue nem sequer
  sustentar o nível de abertura, historicamente um padrão associado a fluxo de venda
  institucional distribuindo posição ao longo do pregão, não apenas ruído.
- **O ISO (Índice de Suporte do Óleo) segue em 80/100**, sem recuperação nem novo recuo desde
  10/09 — os índices compostos continuam sem sinalizar qualquer mudança de regime, mesmo com
  três sessões seguidas do mesmo padrão vendedor.

**O que sustenta um piso parcial para a tese — e por que a evidência de hoje pede cautela
redobrada, agora com uma terceira confirmação da fragilidade do dado usado para medi-la:**

- **A "margem recorde de biodiesel" citada nas leituras de 16 e 17/09 precisa, mais uma vez,
  ser recalibrada — e desta vez para um valor bem menos dramático do que o descrito ontem.**
  O heating oil (HO=F) de 17/09, usado ontem como US$4,8284/galão (implicando a "primeira
  queda depois de dois recordes, de -15,2%" na margem, para US$2,0537/galão), aparece hoje
  revisado para **US$5,1139/galão** (+5,91%). Com esse valor, a margem de biodiesel real de
  17/09 não foi US$2,0537, e sim **US$2,3279/galão** — uma queda de apenas **-3,89%** frente
  ao recorde revisado de 16/09 (US$2,4222), não os -15,2% descritos ontem. O dado fresco de
  **hoje** (18/09) mostra o heating oil em US$4,8367 (-5,42% sobre a base revisada de 17/09) e
  a margem caindo para **US$2,1332/galão**, uma queda adicional de -8,36% — a margem de
  biodiesel americana está de fato em uma trajetória de queda por dois dias seguidos (-11,93%
  acumulado desde o pico revisado de 16/09), mas a magnitude real é bem menor do que a
  narrativa de ontem sugeria.
- **A boa notícia, pela primeira vez nesta série: o volume do HO=F voltou à normalidade.**
  37.512 contratos hoje e 43.659 em 17/09 (revisado), ambos dentro ou perto da faixa histórica
  saudável (a referência de 11/09, antes do início da anomalia, era 62.190). Isso é
  consistente com a hipótese, já registrada em leituras anteriores, de que o contrato entra
  no dump com um print provisório de baixíssimo volume (na faixa de 180-200) no dia da própria
  sessão, e só recebe o fechamento e o volume completos 1-2 dias depois. Ver o insight
  dedicado [[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]] para o detalhamento
  completo das três ocorrências e a recomendação prática de tratar o HO=F do dia mais recente
  do dump sempre como provisório.
- **A curva futura de médio prazo segue em contango regular**, sem mudança relevante de forma
  frente a ontem: out/26 (base) 67,58 → dez/26 68,13 (+0,55) → jan/27 68,42 (+0,29) → mar/27
  68,57 (+0,15) → mai/27 68,68 (+0,11) — incrementos decrescentes, praticamente idênticos em
  proporção aos de ontem, sem sinal de que o mercado a termo esteja reprecificando a queda de
  hoje como estrutural.
- **O RIN D4 (crédito de biocombustível renovável americano) continua constante na fórmula
  interna** — toda a variação de hoje e de ontem na margem de biodiesel vem de heating oil e
  do próprio óleo, não de qualquer mudança real no valor do crédito RIN.

**Leitura operacional:** para quem está vendido em óleo direcional, o quadro técnico
continua sendo o mais favorável de toda a janela — três sessões seguidas do mesmo padrão
"abre na máxima, vende o dia inteiro", com nova mínima hoje e distância recorde abaixo do
suporte de 72,00. A diferença frente às duas leituras anteriores é que o principal
contra-argumento fundamentalista (a "margem recorde de biodiesel") perde ainda mais força,
não porque a margem tenha se recuperado, mas porque ficou comprovado que o instrumento que a
mede vinha exagerando tanto os recordes de alta quanto as quedas subsequentes. Para quem está
comprado em óleo direcional, a única leitura defensável hoje é aguardar uma quebra clara do
padrão "abre na máxima" (por exemplo, um fechamento acima da abertura) antes de considerar
reforçar posição. Para quem opera o spread farelo-óleo dentro do crush (farelo vendido/óleo
comprado, apostando em mean-reversion), a compressão de hoje no oil-meal spread (de -0,5566
para -0,3696) é o primeiro movimento a favor dessa posição desde que o spread começou a se
esticar — mas ainda distante do nível de reabertura (-0,0187 em 11/09), então a operação
segue com espaço técnico, não com o alvo já alcançado.

## Spreads e crush (leitura de complexo)

A janela de seis sessões desde a reabertura do fim de semana (11, 14, 15, 16, 17 e 18/09) —
usando os valores como aparecem consolidados no dump de hoje — mostra uma reversão clara na
sessão mais recente, depois de uma aceleração altista nas cinco sessões anteriores: farelo
346,80 → 350,20 → 360,10 → 360,90 → 368,70 → 354,70; óleo 69,19 → 69,65 → 69,88 → 69,19 →
68,68 → 67,58 (CME CBOT/indicators, valores conforme aparecem hoje no dump). O ratio Far/Soj:
80,25% → 80,55% → 81,92% → 81,99% → 83,81% → **81,67%**, com o recuo de 17→18/09 (-2,14 p.p.)
sendo o maior movimento diário — em qualquer direção — de toda a sequência, superando o de
16→17/09 (+1,82 p.p.). O oil share: 49,94% → 49,86% → 49,25% → 48,94% → 48,22% → **48,79%**,
subindo hoje pela primeira vez em seis sessões, não porque o óleo se fortaleceu, mas porque o
farelo caiu proporcionalmente mais. O oil-meal spread: -0,0187 → -0,0429 → -0,2354 → -0,3289
→ -0,5566 → **-0,3696** USD/bushel, comprimindo hoje pela primeira vez desde a reabertura,
pelo mesmo motivo.

Essa combinação — os três indicadores matematicamente independentes revertendo
simultaneamente na sessão mais recente, depois de cinco dias acelerando na direção contrária
— é o tipo de sincronia que, em qualquer uma das duas direções, tende a refletir um
reajuste genuíno de expectativas do mercado, não ruído aleatório em uma métrica isolada. Os
dois índices compostos por contagem de condições — ISF (60/100) e ISO (80/100) — permanecem
travados no mesmo patamar desde 11/09, agora o oitavo dia corrido sem qualquer mudança, o
mesmo contraponto já registrado nas últimas cinco leituras: os limiares desses índices
específicos não reagem a oscilações de curto prazo, mesmo quando essas oscilações são as
maiores já registradas na série, em qualquer direção.

O crush margin fechou em **US$2,2072/bushel** (indicators, 18/09), a maior queda diária da
sequência (-10,59%, superando o próprio recorde de queda anterior) — a distância abaixo do
piso de referência de US$2,50 alargou-se de -2,08% (17/09, a menor já registrada) para
**-11,71%** hoje, a maior quebra desde que esse piso passou a ser citado nesta série (fila
`alerta-quebra_suporte-complexo_soja-2026-09-18`). O mecanismo: farelo caiu -3,80% sozinho o
suficiente para mais do que compensar a queda simultânea de -1,60% do óleo, com a soja também
caindo -1,27% no meio — o espelho exato do que aconteceu na leitura de ontem, quando foi a
alta do farelo que puxou o crush margin para cima apesar do óleo caindo.

O COT de 15/09 (`release-cftc_cot-2026-09-15`), a primeira atualização de posicionamento em
dez dias, retrata os fundos ampliando net long em farelo (+16,12%) e óleo (+10,65%) e
reduzindo em soja (-6,13%) — um instantâneo de terça-feira que precede a reversão de hoje e
não pode confirmá-la ou desmenti-la diretamente, mas estabelece a base de comparação para o
próximo corte (posições de 22/09, esperado por volta de 25-26/09), que será o primeiro capaz
de dizer se os mesmos fundos que ampliaram farelo e óleo na semana passada já começaram a
realizar lucro com a queda de hoje. Do lado dos fundamentos brasileiros de médio prazo
(ABIOVE, sem revisão nesta janela), o balanço projetado continua mostrando o esvaziamento
sazonal esperado de oferta de farelo entre outubro e dezembro/26 — uma trajetória que segue
apoiando um ratio estruturalmente mais alto no médio prazo, independentemente da correção de
curto prazo observada hoje.

## Lente fiscal/regulatória BR

Antes de fechar qualquer tese de preço BR, os vetores tributários/regulatórios vivos que
pesam no complexo — todos do `system/tributario_watch.toml`, cujo carimbo mais recente
(`atualizado_em`) em todos os 10 eventos catalogados é 2026-06-05, ou seja, **106 dias
corridos sem revisão humana** frente a hoje (19/09):

- **MP 1.363/2026** (id `MP-1363-2026`, subvenção diesel fóssil R$1,12/L, vigente até
  31/12/2026): barateia o diesel fóssil no mix B15 (mistura obrigatória de 15% de
  biodiesel), reduzindo a competitividade relativa do biodiesel e a demanda doméstica por
  óleo de soja — vetor estrutural de baixa para óleo, sem mudança de status. Esse desincentivo
  brasileiro é independente da margem de biodiesel americana e ajuda a explicar por que o
  óleo brasileiro segue sob pressão mesmo quando a margem americana se recupera.
- **B16 (id `B16-CNPE-2026`, elevação da mistura obrigatória de biodiesel para 16%)** segue
  "adiado", resultado esperado por volta de novembro/2026. Upside represado (~436 mil
  toneladas de demanda potencial adicional de óleo), não corrente.
- **Isenção de PIS/Cofins do biodiesel na mistura** (id `PISCOFINS-BIODIESEL-ISENCAO`):
  vigência registrada até 31/07/2026 — já **50 dias corridos vencida** frente a 19/09/2026,
  sem registro de prorrogação ou expiração.
- **MP 1.358/2026** (subvenção gasolina R$0,89/L): vigência registrada até 11/07/2026, agora
  **70 dias corridos vencida**.
- **STJ REsp 2.165.276** (id `STJ-RESP-2165276`, crédito de PIS/Cofins sobre soja em
  biodiesel, direção "alta" para soja/óleo): sem novidade nesta janela.
- **EPA RFS 2026/2027** (id `EPA-RFS-2026-2027`, mandato de biocombustível americano, direção
  "alta" para óleo): sustenta o RIN D4, estável, e o RIN permanece constante na fórmula
  interna de margem de biodiesel usada por este sistema.
- **Crédito 45Z** (id `45Z-CLEAN-FUEL`, em tramitação, direção "mista"): sem novidade.
- **Indonésia — Danantara** (id `DANANTARA-INDONESIA`) e **levy de exportação PMK 9/2026**
  (id `INDONESIA-LEVY-PMK9`): a assunção plena da centralização da exportação de palma pela
  Indonésia tinha alvo 01/09/2026 — já se passaram **18 dias** sem confirmação. Catalisador de
  alta represado para óleo (via substituição com palma) — sem dado de MPOB disponível para
  monitorar diretamente.
- **Indonésia B50** (id `INDONESIA-B50`, monitorando, direção "alta"): sem novidade.

Nenhum desses vetores muda a leitura de preço de hoje isoladamente — mas, em conjunto, eles
reforçam a assimetria já descrita no óleo: o mercado interno brasileiro tem múltiplos
desincentivos correntes (MP 1.363, isenção PIS/Cofins vencida) e múltiplos catalisadores de
alta represados, não correntes (B16, Danantara, B50). Essa configuração é independente da
queda de hoje na margem de biodiesel americana — o óleo brasileiro segue mais fraco
estruturalmente até que algum dos vetores represados vire fato concreto, e o vetor de baixa
mais imediato (MP 1.363) permanece plenamente vigente.

## Riscos e eventos próximos

- **Próximo corte de COT (posições de 22/09), esperado por volta de 25-26/09.** Depois de o
  corte de 15/09 mostrar fundos ampliando net long em farelo e óleo e reduzindo em soja, este
  será o primeiro capaz de confirmar se a reversão de hoje já provocou realização de lucro por
  parte dos mesmos fundos, especialmente em farelo, onde a convicção institucional era a mais
  forte de toda a série disponível.
- **Uma segunda sessão seguida de queda em farelo, soja ou óleo** seria o primeiro sinal
  técnico de que a correção de hoje é o início de algo mais persistente, não apenas um dia de
  realização de lucro depois de uma extensão recorde. Um ratio Far/Soj de volta abaixo de
  81,4% (o nível de abertura da tese baixista original) reabriria formalmente a discussão
  sobre a validade da "reversão" documentada nas últimas leituras.
- **Nível técnico a vigiar em farelo:** volta abaixo de 325,00 desfaria o rompimento (folga
  atual +9,14%, a menor desde 15/09).
- **Nível técnico a vigiar em soja:** volta abaixo de 1.180,00 desfaria o rompimento (folga
  atual +10,42%, a menor desde a reabertura).
- **Reação (ou ausência) do físico brasileiro de farelo e óleo**, congelado desde 09/09 (dez
  dias) e 27/08 (prêmios export, 23 dias) — a volatilidade desta semana em Chicago ainda não
  tem qualquer contrapartida observável no mercado físico doméstico.
- **USDA Crop Progress semanal**: próximo corte esperado em 1-2 dias, por volta de 20-21/09.
- **USDA WASDE**: a tabela de setembro (11/09) ainda só traz farelo — monitorar se as tabelas
  de soja em grão e óleo aparecem nos próximos dias desta mesma edição, ou apenas em outubro.
- **NOPA mensal**: mais um "release" sem dado novo de fato (paywall).
- **Confirmação da centralização plena da exportação de palma pela Danantara** — alvo 01/09,
  já 18 dias passados sem confirmação.
- **Vigência da isenção PIS/Cofins do biodiesel** (50 dias vencida) e **MP 1.358/2026 da
  gasolina** (70 dias vencida) — checar notícia de renovação/expiração.
- **Clima**: previsão de hoje (19/09) traz alerta pontual de granizo em Cascavel/PR à noite,
  além de chuva isolada persistente no núcleo produtor de Mato Grosso — pano de fundo relevante
  para a janela de plantio da safra 2026/27; ausência de menção a geada em Passo Fundo/RS
  (mínima subindo de 8°C para 14°C na previsão) mantém esse risco pontual fora de cena.
- **Marco de 106 dias sem revisão humana do `tributario_watch.toml`** — pelo menos dois
  vetores (isenção PIS/Cofins biodiesel, MP 1.358/2026) já vencidos sem registro de renovação,
  seguem sem checagem manual.
- **Terceira confirmação do padrão de revisão do heating oil (HO=F)** — ver insight dedicado
  [[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]]; monitorar se o fechamento de
  hoje (18/09, US$4,8367, volume já normalizado em 37.512) se mantém estável no dump de
  amanhã, o que ajudaria a confirmar que a normalização do volume é o fator que resolve a
  fragilidade, não apenas uma coincidência.

## Honestidade

- **A sessão de hoje (19/09) ainda não tem fechamento próprio de CME CBOT nesta janela do
  dump** — o mais recente disponível é o de 18/09 (sexta-feira), o que é esperado e normal (a
  sessão americana de hoje só fecharia após o horário de geração deste briefing). O cabeçalho
  do dump usado por este sistema ainda está rotulado "Briefing consolidado — 2026-09-18", um
  dia atrás da data desta leitura (2026-09-19) — o mesmo padrão observado em todas as leituras
  anteriores desta série, em que a leitura do dia D é sempre escrita sobre o fechamento de
  mercado de D-1.
- **Os números da sessão de 17/09 aparecem revisados no dump de hoje frente ao que a leitura
  de ontem usou** — a quarta ocorrência documentada desse padrão nesta série
  ([[2026-09-13_correcao-numeros-sessao-11set-farelo-oleo]],
  [[2026-09-16_correcao-numeros-sessao-15set-ratio-salta-para-8191]], e o próprio
  [[2026-09-18_leitura-complexo]] documentando a revisão de 16/09). A tabela completa:

  | Métrica (17/09) | Usado na leitura de ontem | No dump de hoje | Variação |
  |---|---|---|---|
  | Soja CBOT fechamento | 1.319,50 | 1.319,75 | +0,02% |
  | Farelo CBOT fechamento | 368,40 | 368,70 | +0,08% |
  | Óleo CBOT fechamento | 68,53 | 68,68 | +0,22% |
  | Heating oil (HO=F) fechamento | 4,8284 | **5,1139** | **+5,91%** |
  | Heating oil (HO=F) volume | 179 | **43.659** | **+24.297%** |
  | Ratio Far/Soj | 83,76% | 83,81% | +0,05 p.p. |
  | Oil share | 48,19% | 48,22% | +0,03 p.p. |
  | Oil-meal spread | -0,5665 | -0,5566 | menos negativo |
  | Crush margin | 2,4481 | 2,4687 | +0,84% |
  | Paridade BR soja | R$149,87 | R$149,90 | +0,02% |
  | Margem biodiesel US | US$2,0537 (dito "-15,2%, 1ª queda") | **US$2,3279 (-3,89% real)** | **+13,35%** |

  Como nas duas ocorrências mais recentes, as revisões de soja, farelo, óleo, ratio, oil
  share, oil-meal spread e crush margin são pequenas (todas abaixo de 0,9% em módulo) e não
  mudam nenhuma conclusão direcional da leitura de ontem. A revisão relevante está de novo
  isolada no **heating oil** (+5,91% no preço, +24.297% no volume) e no seu efeito amplificado
  sobre a margem de biodiesel (o que ontem foi descrito como uma queda de -15,2%, a "primeira
  depois de dois recordes", na realidade foi uma queda de apenas -3,89%). Esta é a terceira
  ocorrência do mesmo padrão (11/09: +3,77%; 16/09: +5,65%; 17/09: +5,91%, sempre para cima,
  sempre com volume inicial na faixa de 180-200 contratos corrigido para dezenas de milhares
  na geração seguinte) — o suficiente para tratá-lo como estrutural, não acidental, e por isso
  ganhou o insight dedicado [[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]]. Esta
  leitura trata o valor mais recente (o do dump de hoje) como mais confiável, seguindo a mesma
  lógica de verificação cruzada das ocorrências anteriores, e recomenda formalmente que
  qualquer leitura de margem de biodiesel baseada no fechamento de HO=F do dia mais recente do
  dump seja tratada como provisória até a geração seguinte confirmar o valor.
- **O corte de COT `release-cftc_cot-2026-09-15` é o primeiro dado de posicionamento novo em
  dez dias**, mas retrata terça-feira, 15/09 — quatro dias antes de hoje e três antes da
  reversão de 18/09. Não há como confirmar se os fundos que ampliaram farelo/óleo e reduziram
  soja mantiveram essa postura durante a queda de sexta-feira; essa é uma lacuna real que só o
  próximo corte (22/09, esperado 25-26/09) resolve.
- **Percentil histórico de posicionamento COT não está disponível no briefing** — toda leitura
  de "fundos comprando/vendendo" nesta série usa variação absoluta semana a semana de
  contratos, não percentil histórico.
- **O item de fila `release-nopa-2026-09-18` é mais uma repetição sem dado novo** — o mesmo
  padrão de todas as leituras anteriores desde que este monitoramento começou (paywall,
  `monthly_status` em 0,0 bool).
- **`tributario_watch.toml` sem atualização há 106 dias corridos** — pelo menos dois vetores
  (isenção PIS/Cofins do biodiesel, MP 1.358/2026) já passaram da vigência registrada sem nota
  de renovação ou expiração.
- **A ausência de itens de notícia com qualquer conteúdo chega a nove dias corridos
  consecutivos (10 a 18/09)**, sem visibilidade ainda sobre a coleta de 19/09 nesta janela do
  dump — registrado como falha ou pausa de coleta da fonte RSS, não como ausência real de
  notícia relevante no mercado.
- **A previsão INMET para 19/09 é previsão meteorológica, não medição de precipitação ou
  temperatura real** — as menções a "chuva", "chuva isolada" e o alerta de "possível queda de
  granizo" em Cascavel/PR são indicativas do boletim, não confirmação de que ocorreram
  efetivamente.
- **Prêmios de exportação (Paranaguá) e o físico de farelo/soja BR seguem sem atualização
  própria desde 09/09** (dez dias corridos) — não é possível afirmar se isso reflete mercado
  físico genuinamente parado ou apenas defasagem normal de publicação da fonte NAG.
- **MPOB (palma Malásia) segue com parser quebrado** — nenhum dado de produção/estoque de
  palma malaia disponível, o que impede monitorar diretamente o catalisador represado da
  centralização de exportação indonésia (Danantara).
- **BCBA (Argentina) segue sem links de relatório detectados** — nenhum dado de safra ou
  exportação argentina disponível além do que já vem consolidado pelo WASDE.
- **Os forecasts estatísticos internos (bandas 7d/30d) foram gerados em 18/09 sobre o
  fechamento dessa mesma sessão**, ou seja, ainda não incorporam a reversão de hoje nem a
  geração seguinte capturará plenamente — o viés "altista" nos três produtos reflete
  extrapolação estatística de tendência (MA20 + volatilidade + slope) da janela anterior à
  queda, não uma reavaliação fundamentalista; esta leitura mantém farelo e soja em bull e óleo
  em bear a partir da análise qualitativa, não das bandas estatísticas.
- **A fila de julgamento voltou a listar os dois itens de revisão do ratio Far/Soj (D+7 e
  D+90) como "vencidos"**, o mesmo eco de geração já documentado em leituras anteriores (09,
  12, 15, 16, 17 e 18/09). O veredito de reversão técnica dado em
  [[2026-09-17_ratio-far-soj-supera-nivel-de-abertura-da-tese-original-quarta-sessao]] segue
  válido tecnicamente (o ratio de hoje, 81,67%, ainda está acima do nível de abertura de
  81,4%), mas a margem de segurança dessa leitura caiu para +0,27 ponto — a mais estreita já
  registrada — e merece reavaliação explícita se a próxima sessão também recuar. A revisão de
  D+180, programada para 08/12/2026 pela tese original, ainda não venceu.
