---
data: 2026-09-22
titulo: "Farelo estica pela terceira sessão seguida (ratio Far/Soj em 83,13%) e ganha uma segunda confirmação física em Rondonópolis/MT (+8,37%), óleo segue abaixo do suporte técnico com a margem de biodiesel apoiada num heating oil de dado suspeito, e soja fecha praticamente estável — mas a sessão inteira de 22/09 carrega um alerta de qualidade de dado mais grave que qualquer sinal de preço: volumes de 1 a 4% do normal e cotações de abertura/máxima/mínima de farelo e heating oil idênticas, byte a byte, ao dia anterior"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT — sessão de **2026-09-22** (terça-feira): soja (ticker ZSX26.CBT, venc. nov/26) abertura 1.327,00, máxima 1.328,50, mínima 1.325,75, fechamento **1.327,75**, volume **4.041 contratos**; farelo (ticker ZMZ26.CBT, venc. dez/26) abertura 367,60, máxima 368,60, mínima 367,30, fechamento **367,90**, volume **1.410 contratos**; óleo (ticker ZLZ26.CBT, venc. dez/26) abertura 68,95, máxima 69,20, mínima 68,77, fechamento **68,93**, volume **952 contratos**. Curva futura em 22/09 — soja: nov/26 (base) 1.327,75 → jan/27 1.343,50 → mar/27 1.350,75 → mai/27 1.357,00 → jul/27 1.360,75; farelo: out/26 366,00 → dez/26 (base) 367,90 → jan/27 368,20 → mar/27 368,20 → mai/27 368,40; óleo: out/26 68,28 → dez/26 (base) 68,93 → jan/27 69,16 → mar/27 69,18 → mai/27 69,32
  - CME CBOT — sessão de **2026-09-21** (referência de comparação, mesma fonte `cme_cbot`): farelo abertura 367,60, máxima 368,60, mínima 367,30, fechamento **367,70**, volume **1.410 contratos** — **abertura, máxima, mínima e volume idênticos, byte a byte, aos de 22/09** (ver Visão geral e Honestidade); os fechamentos de soja e óleo de 21/09 não aparecem mais como linha bruta neste dump (rolaram para fora da janela de 14 dias do `cme_cbot`), só sobrevivem via os indicadores já calculados naquele dia (soja 1.327,00; óleo 68,79)
  - CME NYMEX heating oil (HO=F) — **2026-09-22**: abertura 4,7088, máxima 4,7250, mínima 4,7000, fechamento **4,7249** USD/galão, volume **294 contratos**; **2026-09-21**: abertura 4,7088, máxima 4,7250, mínima 4,7000, fechamento 4,7054, volume **294 contratos** — mesma anomalia de duplicação exata de abertura/máxima/mínima/volume entre os dois dias, só o fechamento varia (+0,41%); volume de 294 contratos é ~0,65% dos 45.315 vistos na sessão cheia de 18/09 (ver Honestidade)
  - Indicadores sintéticos internos (`indicators`) — **2026-09-22**: crush margin **US$2,3986/bushel** (farelo 367,90 + óleo 68,93 − soja 1.327,75); ratio Far/Soj **83,13%**; oil share **48,37%**; oil-meal spread **-0,5115 USD/bushel**; ISF (Índice de Sobra de Farelo) 60/100; ISO (Índice de Suporte do Óleo) 80/100; paridade BR da soja **R$149,63/saca** (CBOT 1.327,75 × USD/BRL 5,1117, sem basis); margem de biodiesel US **US$1,9201/galão** (receita 7,89 = HO 4,72 + 1,5×RIN 2,11; custo 5,97 = óleo 5,17 + industrial 0,80). Comparação **2026-09-21**: crush margin 2,3863; ratio 83,13%; oil share 48,33%; oil-meal spread -0,5225; margem biodiesel 1,9111; paridade BR 149,54 (mesmo USD/BRL 5,1117)
  - BCB PTAX — última publicação **2026-09-21**: USD/BRL **5,1117** (queda de -0,89% frente aos 5,1575 de 18/09 — real mais forte), EUR/BRL 5,8626, Selic diária 0,050788% a.a. (séries SGS 1, 21619, 11); sem PTAX de 22/09 neste dump (publicação de hoje ainda não capturada — lag normal, ver Honestidade)
  - NAG físico BR (`nag_fisico`) — **2026-09-21**: farelo Rondonópolis/MT (BCSP) **R$2.200,00/ton (+8,37% frente aos R$2.030,00 de 16-18/09, DADO NOVO relevante, ver Farelo)**; farelo Mato Grosso/IMEA R$1.982,28/ton (var 0,0%, mesmo valor desde 18/09); farelo média Rio Grande do Sul (Clicmercado) R$1.860,00/ton (var 0,0%, valor idêntico em toda a janela visível do dump desde 08/09 — 14 dias corridos, ver Honestidade); soja Paraná interior (CEPEA/ESALQ via NAG) R$155,26/saca (+0,05%); prêmio export farelo Paranaguá 0,12 USD/short_ton (congelado desde 08/09, 14 dias corridos); prêmio export óleo Paranaguá 0,1 cts/lb (mesmo congelamento)
  - CEPEA/ESALQ Soja Paranaguá (via NAG) — **2026-09-21**: R$161,52/saca (var -0,23% frente a 18/09); spread Paranaguá−Paraná interior de R$6,26/saca (161,52 − 155,26), um prêmio de porto dentro do padrão recente
  - CEPEA RSS — headline de **2026-09-18**, ainda a mais recente com corpo relevante: "SOJA/CEPEA: Participação do farelo na 'crush margin' aumenta no BR e nos EUA" — confirmação qualitativa direta, de fonte especializada, do mesmo movimento que o ratio Far/Soj e o oil share vêm mostrando numericamente (ver Farelo)
  - Notícias Agrícolas/Canal Rural (RSS) — headline de **2026-09-21**, DADO NOVO nesta leitura: "Preços de soja sobem de R$1 a R$2 por saca nas praças do Brasil; confira as cotações do dia" (Canal Rural) — sem corpo de texto disponível além do título (ver Soja e Honestidade); item de contagem `noticias | items_fetched` de **2026-09-22** registra 160 itens lidos e 3 mantidos, mas sem o texto desses 3 itens neste dump (ver Honestidade)
  - CFTC COT Managed Money — corte de **2026-09-15** (sem corte novo; próximo corte é o de posições de 22/09, esperado por volta de 25-26/09): farelo net long 183.111 contratos (+16,12% vs 08/09); óleo net long 101.480 (+10,65%); soja net long 241.501 (-6,13%)
  - USDA Crop Progress — corte de **2026-09-13** (sem corte novo pela SEGUNDA segunda-feira seguida — o corte de 21/09 também não apareceu, ver Honestidade): 12% excelente / 46% boa (G/E 58%), colheita 2025/26 em 6% concluída
  - USDA WASDE — edição de **2026-09-11** (sem edição nova): farelo Argentina 2026/27 exportação 2,99 mi t; farelo Brasil 2025/26 exportação 0,2 mi t
  - NOPA — item de fila `release-nopa-2026-09-22`: `monthly_status` em 0,0 bool (paywall, sem dado novo, mesmo padrão de todas as leituras anteriores)
  - ABIOVE projeções mensais — balanços out-dez/2026, sem revisão nesta janela
  - NOAA CPC ENSO — El Niño Advisory, inalterado (carimbo 2026-09-22)
  - MPOB — carimbo 2026-09-22, parser sem números extraídos (mesma barreira há semanas)
  - BCBA (Argentina) — carimbo 2026-09-09 (mais antigo, sem atualização), scraper acessa a página mas não encontra links de relatório
  - INMET — previsão para **2026-09-22 (HOJE)**: sem menção de granizo em nenhuma das oito praças monitoradas (diferente de 21/09, quando Cascavel/PR e Passo Fundo/RS traziam risco de granizo — ver Soja); Cascavel/PR 21°C/8°C com "pancadas de chuva e trovoadas isoladas"; Maringá/PR 24°C/16°C, mesmo padrão; Passo Fundo/RS 15°C/4°C, "muitas nuvens"/"poucas nuvens" sem menção de precipitação forte; núcleo de Mato Grosso — Cuiabá 35°C/26°C (recuo frente aos 37°C de 21/09), Sinop 38°C/25°C, Sorriso 38°C/25°C, Lucas do Rio Verde 38°C/26°C, todos "muitas nuvens" com chuva isolada/trovoadas; Rio Verde/GO 37°C/21°C
  - system/tributario_watch.toml (lido como referência, não editado) — `atualizado_em` 2026-06-05 em todos os 10 eventos catalogados, **109 dias corridos** sem revisão humana frente a hoje (22/09)
  - Forecasts estatísticos internos (bandas 7d/30d) — geração de **2026-09-22**, sobre o fechamento de hoje, alvos 29/09 e 22/10: viés "altista" em soja e farelo nos dois horizontes, "lateral" em óleo no horizonte de 7 dias e "altista" no de 30 dias (extrapolação estatística, não fundamentalista — ver Honestidade)
  - Fila de julgamento — 2026-09-22, 7 itens: `alerta-quebra_resistencia-soja_cbot-2026-09-22`, `alerta-quebra_suporte-oleo_cbot-2026-09-22`, `alerta-quebra_resistencia-farelo_cbot-2026-09-22`, `alerta-quebra_suporte-complexo_soja-2026-09-22`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`, `release-nopa-2026-09-22`
  - Cruza com [[2026-09-21_leitura-complexo]] (leitura de ontem, primeiro dia com a hipótese de HO=F fraco), [[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]] (padrão de revisão do HO=F documentado em três ocorrências anteriores, hoje testado por uma anomalia mais extrema — ver Honestidade), [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (tese original do ratio, nível de abertura 81,4%) e [[2026-09-17_ratio-far-soj-supera-nivel-de-abertura-da-tese-original-quarta-sessao]] (veredito de invalidação técnica da tese baixista de junho, D+7 e D+90 já fechados)
status: ativa
vies: [bull-farelo, neutral-soja, bear-oleo_soja]
---

## Visão geral

O complexo soja gira em torno do "crush" (esmagamento industrial): a soja em grão é
triturada e separada em farelo (concentrado proteico para ração animal, sobretudo aves e
suínos) e óleo (alimentação humana e, cada vez mais, biodiesel). Quem "manda" no crush é
definido pelo "oil share" — a fatia do valor total gerado pelo esmagamento que vem do óleo.
Oil share alto significa que a indústria esmaga atrás do valor do óleo, e o farelo "sobra"
como subproduto que precisa ser escoado a qualquer preço, pressionando seu preço para baixo.
Oil share baixo é o oposto: o farelo passa a pagar a conta do esmagamento e o óleo perde
protagonismo relativo. O termômetro mais direto dessa disputa é o ratio Far/Soj — preço do
farelo dividido pelo preço da soja, em percentual: abaixo de 80% o farelo está "abundante"
(baixista); entre 80% e 87% ele está "neutro"; acima de 87% ele fica "apertado" (altista, o
farelo vira o motor de rentabilidade do esmagador). Hoje, **83,13%** (indicators,
2026-09-22), o complexo segue na zona neutra, mas mais perto do teto "apertado" (87%) do que
do piso "abundante" (80%) — e o oil share, em **48,37%**, confirma o óleo respondendo por
menos da metade do valor do crush pela sexta sessão seguida em que essa métrica fica
disponível.

**O que muda hoje, terça-feira 22/09, não é a direção do preço — é a confiança que se pode
ter nele.** Farelo, soja e óleo fecharam praticamente estáveis frente a ontem (+0,05%,
+0,06% e +0,20%, respectivamente), o que já seria pouco notável por si só. O que exige
atenção é que essa estabilidade vem acompanhada de dois sinais de qualidade de dado mais
graves do que qualquer coisa já registrada nesta série:

**Achado 1 — farelo e heating oil fecham hoje com abertura, máxima, mínima e volume
idênticos, byte a byte, aos de ontem.** A linha bruta do farelo (`cme_cbot`, ticker
ZMZ26.CBT) mostra abertura 367,60, máxima 368,60, mínima 367,30 e volume 1.410 contratos
tanto em 21/09 quanto em 22/09 — os únicos dois números que diferem entre os dois dias são
os fechamentos (367,70 → 367,90). O mesmo padrão, ainda mais completo, aparece no heating
oil (HO=F): abertura 4,7088, máxima 4,7250, mínima 4,7000 e volume 294 contratos idênticos
nos dois dias, só o fechamento varia (4,7054 → 4,7249). Estatisticamente, é praticamente
impossível que quatro campos de um contrato futuro líquido — abertura, máxima, mínima e
volume — fechem exatamente iguais em duas sessões de pregão diferentes, a menos que o dado
não represente, de fato, duas sessões novas e completas, e sim a mesma "foto" (o mesmo
snapshot de sessão) sendo relida com apenas o campo de "último preço" (fechamento/cotação
corrente) atualizando. O mecanismo mais provável é o mesmo já mapeado três vezes em
[[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]] para o HO=F isoladamente — um
print antecipado ou uma leitura de cotação em tempo real capturada fora do horário de
fechamento oficial — mas hoje o problema aparece de forma mais extrema (campos idênticos,
não apenas um viés de revisão) e se estende ao farelo, que não fazia parte do padrão
documentado anteriormente.

**Achado 2 — os volumes de todos os quatro contratos monitorados estão entre 0,65% e 3,7%
do que se via normalmente há poucos dias.** Soja fechou com **4.041 contratos** de volume;
farelo, **1.410**; óleo, **952**; heating oil, **294**. Para comparação, a sessão de
18/09/2026 (a última com volume "normal" documentado em leituras anteriores) teve 108.222
contratos em soja, 113.303 em farelo, 67.046 em óleo e 45.315 em heating oil — ou seja, o
volume de hoje representa **3,7%** do normal em soja, **1,2%** em farelo, **1,4%** em óleo e
apenas **0,65%** em heating oil. Um volume tão baixo, replicado nos quatro contratos ao
mesmo tempo, reforça a leitura de que a sessão de hoje pode não estar sendo capturada em seu
horário de fechamento pleno — o que significa que os rompimentos técnicos listados na fila
de julgamento de hoje (soja acima de 1.180, farelo acima de 325, óleo abaixo de 72, crush
abaixo de 2,50) continuam válidos em nível, mas devem ser lidos como confirmados por um
preço de baixa liquidez, não por um fechamento pleno e amplamente negociado.

Esses dois achados não mudam a direção das teses que já vinham se consolidando nas últimas
duas semanas — farelo mais forte, óleo mais fraco, soja no meio — mas mudam o grau de
convicção com que se deve tratar o movimento específico de hoje. Por isso, o corpo desta
leitura mantém os três vieses já estabelecidos (bull-farelo, neutral-soja, bear-oleo_soja),
apoiando-se preferencialmente nos dados de sessões anteriores com volume saudável (18/09) e
tratando o incremento de hoje como direcionalmente coerente, mas não como confirmação de
alta conclusividade.

**Leitura de uma linha**: o pivô do complexo continua sendo o ratio Far/Soj, hoje em 83,13%
— dentro da zona neutra, mas cada vez mais perto do território apertado (87%), agora reforçado
por uma segunda praça física brasileira (Rondonópolis/MT, +8,37%) confirmando aperto
doméstico de farelo, mesmo que a confirmação não seja simultânea entre as fontes. Maior
convicção: bull-farelo, moderado a reforçado. Confiança geral na leitura de hoje
especificamente (não na tendência das últimas duas semanas) é **reduzida** pela anomalia de
volume e OHLC duplicado descrita acima — o dono deveria tratar o fechamento de 22/09 com o
mesmo ceticismo que já se aplicava ao HO=F isoladamente, agora estendido a farelo e, em
menor grau (por volume baixo, ainda que sem duplicação confirmada de OHLC), a soja e óleo.

## Soja

**Viés: neutro, mantido — preço praticamente estável (+0,06%) sobre volume anormalmente
baixo, com um contraponto físico favorável (manchete de alta de R$1-2/saca no Brasil) e um
contraponto técnico desfavorável (segunda semana seguida sem corte de Crop Progress).**

O que sustenta a tese (lado altista):

- **A soja segue folgadamente acima da resistência de referência de 1.180,00** (fila
  `alerta-quebra_resistencia-soja_cbot-2026-09-22`: fechamento 1.327,75 vs. nível 1.180,00),
  uma folga de **+12,52%** — a maior desta série recente, e distante de qualquer risco de
  reversão técnica no curto prazo.
- **A curva futura permanece em contango regular e, hoje, um pouco mais inclinada**: nov/26
  (base) 1.327,75 → jan/27 1.343,50 → mar/27 1.350,75 → mai/27 1.357,00 → jul/27 1.360,75
  (CME CBOT, 22/09) — o mercado a termo segue precificando preços mais altos à frente, sem
  qualquer sinal de reversão estrutural embutido na curva.
- **Manchete nova do Canal Rural (21/09, via `noticias_rss`): "Preços de soja sobem de R$1 a
  R$2 por saca nas praças do Brasil"** — confirmação qualitativa direta de alta no mercado
  físico brasileiro, coerente com o movimento visto no dado quantificável mais próximo
  disponível: a soja Paraná interior (CEPEA/ESALQ via NAG) fechou em R$155,26/saca em 21/09
  (+0,05% frente a 18/09), uma alta pequena mas positiva. O corpo da notícia não está
  disponível neste sistema (ver Honestidade), então não é possível confirmar a magnitude
  exata de "R$1 a R$2" citada no título com um número de fonte primária, mas a direção bate
  com o dado do CEPEA.
- **O câmbio trabalhou a favor da paridade brasileira apesar de o real ter se fortalecido**:
  o USD/BRL PTAX caiu de 5,1575 (18/09, BCB) para **5,1117 (21/09, -0,89%)** — um real mais
  forte tende, isoladamente, a pressionar para baixo o valor em reais de uma commodity
  cotada em dólar. Mas como o CBOT subiu mais rápido (+1,86% de 18/09 a 22/09) do que o real
  se valorizou, a paridade brasileira da soja ainda avançou, de R$148,21/saca (18/09) para
  **R$149,63/saca (22/09, indicators)**, um ganho de +0,96% no período — o mecanismo aqui é
  que o efeito Chicago dominou o efeito câmbio, mas por uma margem que se estreitaria
  rapidamente se o real continuasse a se apreciar sem acompanhamento do CBOT.

**O que invalida / risco:**

- **O USDA Crop Progress não traz corte novo pela SEGUNDA segunda-feira seguida.** O corte
  mais recente ainda é o de 13/09 (12% excelente + 46% boa, G/E 58%, 6% colhido); nem o
  corte esperado em 21/09 nem qualquer atualização de hoje aparecem neste dump — uma lacuna
  que já dura nove dias corridos sem novo dado de condição de lavoura americana, o dobro do
  ciclo semanal normal (ver Honestidade).
- **O COT de 15/09, ainda o mais recente, mostrou os fundos reduzindo net long em soja em
  -6,13%** (de 257.258 para 241.501 contratos), com short subindo. Sete dias depois desse
  corte, ainda não há um novo dado de posicionamento (próximo corte, de posições de 22/09,
  esperado por volta de 25-26/09) para dizer se o movimento se acentuou.
- **O volume de hoje (4.041 contratos) é apenas 3,7% do volume da última sessão plena
  documentada (108.222, em 18/09)** — o fechamento de +0,06% de hoje carrega muito pouca
  informação nova sobre a real intenção do mercado, e não deveria ser tratado como
  confirmação de continuidade de tendência (ver Visão geral e Honestidade).
- **A leitura CEPEA de Paranaguá (export) foi na direção oposta à do interior**: R$161,52/
  saca em 21/09, uma queda de -0,23% frente a 18/09, enquanto o interior do Paraná subiu
  +0,05% — o spread porto-interior estreitou ligeiramente (de R$6,63 para R$6,26/saca),
  um sinal, ainda pequeno, de que a demanda de exportação pode estar um pouco menos
  aquecida do que a demanda doméstica nesta janela específica.
- **Nível técnico a vigiar:** um fechamento de volta abaixo de 1.180 desfaria formalmente o
  rompimento; com a folga em +12,52%, esse cenário segue distante.

**Leitura operacional:** com preço estável e volume anormalmente baixo, não há gatilho
técnico novo para agir hoje — o único movimento de convicção seria reagir a um corte de Crop
Progress que, pela segunda semana seguida, não chegou. Para quem está comprado, a folga
técnica de +12,52% acima da resistência de 1.180 e o contango da curva seguem sustentando a
posição estrutural, mas o par de contrapontos qualitativos (manchete de alta física no Brasil
vs. COT já mostrando fundos mais cautelosos e Crop Progress atrasado) sugere manter o
dimensionamento atual sem reforçar apenas com base no fechamento de hoje. Para quem opera
vendido, a mínima e a máxima de hoje (1.325,75 e 1.328,50) são referências táticas estreitas
demais para servir de gatilho de entrada num dia de volume tão baixo — vale esperar a
normalização do volume antes de tratar qualquer rompimento intradiário como sinal.

## Farelo

**Viés: bull, moderado a reforçado — o ratio Far/Soj estica pela terceira sessão de dados
disponível e ganha uma segunda confirmação física (Rondonópolis/MT), mas a confiança na
sessão específica de hoje é reduzida pela anomalia de dado no futuro (ver Visão geral).**

O que sustenta a tese:

- **O ratio Far/Soj fechou em 83,13% em 22/09** (indicators), estável frente aos 83,13% de
  21/09 e em alta frente aos 82,53% de 18/09 — a terceira leitura seguida acima de 83%,
  ampliando a distância acima do nível de abertura da tese baixista original de 11/06/2026
  (81,4%, [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]) para **+1,73 pontos
  percentuais**. O veredito de invalidação técnica dessa tese, fechado em
  [[2026-09-17_ratio-far-soj-supera-nivel-de-abertura-da-tese-original-quarta-sessao]],
  segue de pé e, a cada sessão em que o ratio se mantém acima de 81,4%, fica mais distante
  de qualquer risco de reversão para o cenário original — trata
  `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` e
  `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`: ambas seguem
  aparecendo como "vencidas" na fila porque o sistema não lê de volta os insights já
  publicados, mas o veredito de ambas já está fechado desde 17/09 (D+7 parcialmente
  confirmada no curto prazo, D+90 confirmada por margem estreita e às vésperas de reverter);
  resta em aberto apenas a revisão de D+180, programada para 2026-12-08.
- **NOVO: o físico de farelo em Rondonópolis/MT (fonte BCSP, via NAG) saltou de R$2.030,00
  para R$2.200,00/ton em 21/09 — uma alta de +8,37%**, a maior variação percentual de
  qualquer praça física de farelo nesta série de leituras. É a segunda praça física
  brasileira, depois do salto de +3,68% do IMEA em 18/09 (documentado em
  [[2026-09-21_leitura-complexo]]), a mostrar um movimento de alta relevante em poucos dias
  — ainda que em datas diferentes, não simultâneas. O mecanismo mais provável, como já
  discutido para o caso do IMEA, é doméstico: aperto de originação física pronto-entrega,
  concorrência entre fábricas de ração por volume, ou ajuste pontual de frete/logística no
  polo esmagador de Mato Grosso — fatores que não aparecem no contrato futuro internacional.
  Duas praças físicas distintas (IMEA e BCSP/Rondonópolis) mostrando saltos relevantes em
  dias próximos, mesmo que não no mesmo dia, é uma evidência mais forte de aperto físico
  real do que um único salto isolado seria — mas ainda não é uma confirmação ampla, porque a
  terceira praça monitorada (RS/Clicmercado) segue completamente parada (ver risco abaixo).
- **CEPEA confirma qualitativamente o mesmo mecanismo, de fonte especializada e independente
  do próprio sistema**: a headline de 18/09 (`cepea_rss`) — "SOJA/CEPEA: Participação do
  farelo na 'crush margin' aumenta no BR e nos EUA" — descreve, em linguagem de mercado, o
  exato movimento que o ratio Far/Soj e o oil share vêm capturando numericamente há duas
  semanas: o farelo ganhando peso relativo no valor gerado pelo esmagamento, tanto no Brasil
  quanto nos EUA. É raro ter uma fonte de mercado terceira confirmando, no mesmo período, a
  mesma leitura que os indicadores internos já vinham sinalizando.
- **O oil share caiu para 48,37% em 22/09** (de 48,75% em 18/09) — o óleo responde por cada
  vez menos do valor total do crush, o espelho direto do farelo ganhando protagonismo.
- **O farelo segue folgadamente acima da resistência histórica de 325,00** (fila
  `alerta-quebra_resistencia-farelo_cbot-2026-09-22`: 367,90 vs. 325,00), folga de +13,20%,
  a maior desta série.
- **O COT de 15/09 mostrou os fundos com net long em farelo em 183.111 contratos (+16,12%
  frente a 08/09)** — ainda o dado de posicionamento mais recente, mas a maior variação
  percentual de toda a série de posicionamento disponível.
- **A trajetória sazonal da ABIOVE para o Brasil continua apontando para alívio de oferta
  doméstica de farelo à frente**, sem revisão nesta janela: produção projetada caindo de
  2.143 mil t (out/26) para 1.978 (nov/26) e 1.659 mil t (dez/26); exportação de 850 para 800
  e 700 mil t no mesmo período.

**O que invalida / risco:**

- **A sessão de futuro de hoje carrega a anomalia de dado descrita na Visão geral**: abertura
  (367,60), máxima (368,60), mínima (367,30) e volume (1.410 contratos) idênticos, byte a
  byte, aos de 21/09 — só o fechamento mudou (367,70 → 367,90, +0,05%). Isso significa que a
  "confirmação" de hoje de que o ratio segue acima de 83% se apoia num fechamento de baixa
  liquidez (1.410 contratos, 1,2% do volume de 18/09), não numa sessão plena — o nível
  técnico está confirmado, mas a convicção estatística por trás dele é menor do que parece.
- **A terceira praça física monitorada (RS, fonte Clicmercado) segue completamente parada em
  R$1.860,00/ton por 14 dias corridos, de 08/09 a 21/09** — sete a mais pontos de dados
  idênticos dígito a dígito desde a última leitura, o que reforça a suspeita, já registrada
  em [[2026-09-21_leitura-complexo]], de que essa fonte específica simplesmente não está
  atualizando (ver Honestidade). Sem essa terceira praça em movimento, o quadro físico
  brasileiro de farelo tem confirmação de 2 de 3 fontes, não de 3 de 3.
- **O prêmio de exportação de farelo em Paranaguá segue congelado em 0,12 USD/short_ton há
  14 dias corridos** (desde 08/09) — se o aperto físico doméstico fosse amplo e sustentado,
  seria razoável esperar, eventualmente, algum reflexo no canal de exportação FOB; essa
  confirmação ainda não apareceu.
- **Os índices sintéticos ISF e ISO seguem travados em 60/100 e 80/100**, sem reação a mais
  de dez dias de oscilação do ratio e do crush margin — o contraponto de sempre nesta série:
  esses índices reagem a mudanças de regime estrutural, não a movimentos de curto prazo,
  então sua inércia não deve ser lida como desconfirmação da tese.

**Leitura operacional:** a tendência estrutural de farelo mais forte segue intacta e ganhou
hoje um reforço genuíno (segunda praça física em movimento, confirmação qualitativa da
CEPEA), o suficiente para manter o viés bull-farelo, inclusive com leve reforço de convicção
frente a ontem. Mas a anomalia de volume/OHLC no futuro de hoje pede a mesma cautela de
sempre em dias de baixa liquidez: para quem está comprado em farelo ou no spread Far/Soj
comprado, não é o momento de aumentar posição só com base no fechamento de hoje — o gatilho
mais sólido seria uma sessão de volume normalizado confirmando a continuidade acima de 83%,
ou uma atualização do físico de IMEA/Rondonópolis que mostre o novo patamar se sustentando.
Para quem está vendido, o nível técnico (367,90, folga de +13,20% sobre a resistência) e o
calendário sazonal da ABIOVE seguem desfavoráveis à tese de queda; a estrutura do complexo
não deu, até aqui, nenhum sinal de reversão.

## Óleo

**Viés: bear, moderado — segue abaixo do suporte técnico e perdendo participação no crush,
mas o argumento de margem de biodiesel de hoje se apoia num heating oil com o problema de
dado mais grave desta série, o que exige tratar a leitura fundamentalista de hoje com cautela
extra.**

O que sustenta a tese:

- **Óleo fechou em 68,93 USD cts/lb em 22/09**, uma alta pequena (+0,20%) frente aos 68,79
  de 21/09, mas ainda **abaixo do suporte de referência de 72,00** (fila
  `alerta-quebra_suporte-oleo_cbot-2026-09-22`: distância de -4,26%).
  A série de fechamentos permanece comprimida bem abaixo do nível de suporte desde a
  reabertura de meados de setembro.
- **O oil share caiu para 48,37% (22/09), de 48,75% (18/09)** — o óleo perde,
  progressivamente, participação no valor total gerado pelo crush, o espelho exato do ganho
  de espaço do farelo descrito acima.
- **O ISO (Índice de Suporte do Óleo) segue em 80/100**, sem melhora — os índices compostos
  continuam sem sinalizar qualquer reversão de regime a favor do óleo.
- **A lente fiscal brasileira segue estruturalmente desfavorável, sem mudança hoje**: a MP
  1.363/2026 (subvenção ao diesel fóssil, R$1,12/L, vigente até 31/12/2026) segue plenamente
  vigente, barateando o fóssil no mix B15 e reduzindo a competitividade do biodiesel; a
  isenção de PIS/Cofins do biodiesel na mistura está **53 dias corridos vencida** (vigência
  registrada até 31/07/2026) sem sinal de renovação — ver seção Lente fiscal/regulatória BR.

**O que sustenta um contraponto — e por que a leitura de hoje pede cautela redobrada:**

- **A margem de biodiesel americana de 22/09 ficou em US$1,9201/galão, uma alta de +0,47%
  frente aos 1,9111 de 21/09** — não há, no dado de margem em si, sinal de colapso adicional
  hoje. Mas esse número se apoia diretamente no fechamento de HO=F de hoje (4,7249 USD/
  galão), e é exatamente aqui que mora o problema mais sério de qualidade de dado desta
  leitura: **a linha bruta do HO=F em 22/09 tem abertura (4,7088), máxima (4,7250), mínima
  (4,7000) e volume (294 contratos) idênticos, byte a byte, aos de 21/09** — só o fechamento
  mudou (4,7054 → 4,7249). Combinado com um volume de apenas 294 contratos (0,65% dos 45.315
  vistos em 18/09), isso é uma versão mais extrema do padrão de baixa liquidez já documentado
  três vezes em [[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]] — lá, o padrão
  era "fechamento revisado para cima 1-2 dias depois"; aqui, é "os quatro campos que deveriam
  variar entre sessões diferentes não variam". Isso sugere que o dado pode não representar,
  de fato, uma sessão nova e fechada, e sim uma releitura do mesmo snapshot com apenas o
  último preço negociado (ou cotado) atualizando. **Nenhuma leitura de margem de biodiesel
  construída sobre o HO=F de hoje deveria ser tratada como confirmação de piso ou de teto
  para o óleo** — é, na melhor das hipóteses, uma leitura provisória com confiança bem mais
  baixa do que a de dias anteriores.
- **O RIN D4 (crédito de biocombustível renovável americano) permanece constante na fórmula
  interna** — nenhuma variação real de política regulatória americana explicaria uma mudança
  na margem hoje.
- **A curva futura de médio prazo segue em contango regular**: out/26 68,28 → dez/26 (base)
  68,93 → jan/27 69,16 → mar/27 69,18 → mai/27 69,32 — sem sinal de reprecificação
  estrutural de curto prazo.
- **Catalisadores de alta represados, ainda não correntes**: B16 (elevação da mistura de
  biodiesel para 16%, ~436 mil toneladas de demanda adicional potencial de óleo) segue
  "adiado", com resultado esperado por volta de novembro/2026; a centralização da exportação
  de palma pela Indonésia via Danantara, que tinha alvo de assunção plena em 01/09/2026, já
  soma **21 dias** de atraso sem confirmação — ambos seguem como upside represado, não
  corrente, para o óleo (ver Lente fiscal/regulatória BR).

**Leitura operacional:** o quadro técnico (abaixo do suporte de 72,00, oil share em queda,
ISO travado em 80) e a lente fiscal seguem favoráveis ao lado vendido direcional — mas, ao
contrário de dias anteriores, a leitura de hoje não deveria se apoiar no número de margem de
biodiesel como argumento de convicção adicional, dado o problema de dado no HO=F. Para quem
está vendido, o nível técnico e o calendário fiscal (MP 1.363 vigente até dezembro, isenção
PIS/Cofins já vencida) seguem sustentando a posição sem necessidade do argumento de margem
de hoje. Para quem está comprado ou avalia entrar, o argumento mais forte contra a tese bear
seguiria sendo uma confirmação de HO=F com volume saudável mostrando a margem realmente em
alta — o que este dump não entrega hoje. Para quem opera o spread farelo-óleo dentro do
crush, o oil-meal spread fechou em -0,5115 USD/bushel (indicators, 22/09), ligeiramente menos
negativo que os -0,5225 de ontem, mas dentro da mesma faixa das últimas duas semanas.

## Spreads e crush (leitura de complexo)

O ratio Far/Soj fechou em **83,13%** (22/09), estável frente a ontem e em alta frente aos
82,53% de 18/09 — dentro da zona neutra (80-87%), a **3,87 pontos percentuais** do teto
"apertado" (87%) e a **3,13 pontos** do piso "abundante" (80%), ou seja, hoje ligeiramente
mais perto do território apertado do que do abundante, pela primeira vez nesta métrica de
distância desde que a série de leituras diárias começou a acompanhá-la de perto. O oil
share, em **48,37%**, mostra o óleo respondendo por menos da metade do valor gerado no
esmagamento pela sexta sessão seguida com esse dado disponível — uma tendência consistente
de perda de protagonismo do óleo dentro do crush. O crush margin, em **US$2,3986/bushel**,
segue abaixo do piso de referência de US$2,50 monitorado pela fila
(`alerta-quebra_suporte-complexo_soja-2026-09-22`, distância de -4,06%), mas em recuperação
gradual desde os 2,3584 de 18/09 (+1,70% em duas sessões) — um sinal, ainda modesto, de que
a margem do esmagador para de comprimir ainda mais, sem que isso represente, por ora, um
retorno acima do piso de referência.

Os dois índices compostos por contagem de condições — ISF (60/100) e ISO (80/100) — seguem
travados no mesmo patamar desde 11/09, agora por mais de dez dias corridos sem qualquer
reação, apesar de o ratio e o crush margin terem oscilado de forma expressiva nesse período
— o lembrete de sempre nesta série de que esses índices específicos reagem a mudanças de
regime estrutural, não a oscilações de curto prazo dentro da mesma faixa.

O que muda hoje, sem alterar a leitura direcional de nenhuma dessas três métricas, é a
confiança que se deve depositar no dado do dia especificamente: com farelo fechando sobre
apenas 1.410 contratos de volume (a mesma abertura/máxima/mínima de ontem) e o HO=F que
alimenta a margem de biodiesel apresentando a mesma anomalia, o crush de hoje deve ser lido
como direcionalmente coerente com a tendência das últimas duas semanas (farelo mais forte,
óleo mais fraco), mas não como um novo ponto de dado plenamente confiável por si só. A
segunda confirmação física do lado do farelo (Rondonópolis, +8,37%) é, hoje, o dado mais
sólido de todo o conjunto — vem de uma fonte de mercado físico brasileiro, não do futuro de
baixa liquidez em Chicago.

O COT de 15/09, ainda o dado de posicionamento mais recente sete dias depois, retrata os
fundos ampliando net long em farelo (+16,12%) e óleo (+10,65%) e reduzindo em soja (-6,13%)
— o próximo corte (posições de 22/09, esperado por volta de 25-26/09) é o primeiro capaz de
dizer se os mesmos fundos já realizaram lucro nas correções da semana passada ou se
ampliaram ainda mais as posições de farelo e óleo diante do quadro físico e fiscal descrito
nesta leitura.

## Lente fiscal/regulatória BR

Antes de fechar qualquer tese de preço BR, os vetores tributários/regulatórios vivos que
pesam no complexo — todos do `system/tributario_watch.toml`, cujo carimbo mais recente
(`atualizado_em`) em todos os 10 eventos catalogados é 2026-06-05, ou seja, **109 dias
corridos sem revisão humana** frente a hoje (22/09):

- **MP 1.363/2026** (id `MP-1363-2026`, subvenção diesel fóssil R$1,12/L, vigente até
  31/12/2026): barateia o diesel fóssil no mix B15 (mistura obrigatória de 15% de biodiesel),
  reduzindo a competitividade relativa do biodiesel e a demanda doméstica por óleo de soja —
  vetor estrutural de baixa para óleo, plenamente vigente, sem mudança de status.
- **B16 (id `B16-CNPE-2026`, elevação da mistura obrigatória de biodiesel para 16%)** segue
  "adiado", resultado esperado por volta de novembro/2026. Upside represado (~436 mil
  toneladas de demanda potencial adicional de óleo), não corrente.
- **Isenção de PIS/Cofins do biodiesel na mistura** (id `PISCOFINS-BIODIESEL-ISENCAO`):
  vigência registrada até 31/07/2026 — já **53 dias corridos vencida** frente a 22/09/2026,
  sem registro de prorrogação ou expiração. Cada dia adicional sem notícia de renovação
  aumenta a incerteza de planejamento tributário do setor de biodiesel, um vetor de custo
  indireto sobre a demanda por óleo.
- **MP 1.358/2026** (subvenção gasolina R$0,89/L): vigência registrada até 11/07/2026, agora
  **73 dias corridos vencida**.
- **STJ REsp 2.165.276** (id `STJ-RESP-2165276`, crédito de PIS/Cofins sobre soja em
  biodiesel, direção "alta" para soja/óleo): sem novidade nesta janela.
- **EPA RFS 2026/2027** (id `EPA-RFS-2026-2027`, mandato de biocombustível americano, direção
  "alta" para óleo): sustenta o RIN D4, estável, e o RIN permanece constante na fórmula
  interna de margem de biodiesel usada por este sistema.
- **Crédito 45Z** (id `45Z-CLEAN-FUEL`, em tramitação, direção "mista"): sem novidade.
- **Indonésia — Danantara** (id `DANANTARA-INDONESIA`) e **levy de exportação PMK 9/2026**
  (id `INDONESIA-LEVY-PMK9`): a assunção plena da centralização da exportação de palma pela
  Indonésia tinha alvo 01/09/2026 — já se passaram **21 dias** sem confirmação. Catalisador
  de alta represado para óleo (via substituição com palma) — ainda sem dado de MPOB
  disponível para monitorar diretamente (parser continua quebrado, ver Honestidade).
- **Indonésia B50** (id `INDONESIA-B50`, monitorando, direção "alta"): sem novidade.

Nenhum desses vetores muda a leitura de preço de hoje isoladamente — mas, em conjunto, eles
seguem reforçando a mesma assimetria já descrita em leituras anteriores: o mercado interno
brasileiro tem múltiplos desincentivos correntes ao óleo (MP 1.363 plenamente vigente,
isenção PIS/Cofins já 53 dias vencida) e múltiplos catalisadores de alta represados, não
correntes (B16, Danantara, B50). O óleo brasileiro segue mais fraco estruturalmente até que
algum dos vetores represados vire fato concreto.

## Riscos e eventos próximos

- **Confirmação (ou não) de que a anomalia de OHLC duplicado/volume anormalmente baixo de
  hoje é um problema pontual de captura ou algo mais estrutural** — a próxima geração do
  dump, com volumes normalizados, é o primeiro teste direto. Se o padrão se repetir amanhã
  (farelo e/ou heating oil novamente com abertura/máxima/mínima idênticas ao dia anterior),
  isso deixaria de ser um evento pontual e passaria a exigir tratamento como falha
  sistemática da fonte de dado (ver Honestidade).
- **USDA Crop Progress sem corte novo há duas segundas-feiras seguidas** (14/09 e 21/09 sem
  atualização, ainda no corte de 13/09) — o próximo corte esperado é o de 28/09; se essa
  lacuna persistir, passa a ser um problema de fonte, não de calendário.
- **Confirmação (ou reversão) do salto de +8,37% do físico de farelo em Rondonópolis/MT** —
  a próxima atualização do NAG é o teste de se esse é um sinal real de aperto doméstico
  generalizado ou mais um evento pontual de uma única fonte, como discutido para o caso do
  IMEA.
- **Próximo corte de COT (posições de 22/09), esperado por volta de 25-26/09.** Primeiro
  capaz de confirmar se os fundos que ampliaram net long em farelo e óleo (COT de 15/09) já
  realizaram lucro ou ampliaram ainda mais as posições.
- **Nível técnico a vigiar em farelo:** volta abaixo de 325,00 desfaria o rompimento (folga
  atual +13,20%).
- **Nível técnico a vigiar em soja:** volta abaixo de 1.180,00 desfaria o rompimento (folga
  atual +12,52%).
- **Nível técnico a vigiar em óleo:** recuperação acima de 72,00 desfaria a leitura de
  suporte rompido (distância atual -4,26%).
- **Crush margin:** retorno acima de US$2,50/bushel encerraria a leitura de suporte rompido
  monitorada pela fila (distância atual -4,06%, mas em recuperação desde 18/09).
- **Prêmio de exportação de farelo e óleo em Paranaguá**, congelado há 14 dias corridos
  (desde 08/09) — se o aperto físico de MT for real e amplo, esperar eventualmente refletido
  também nesse prêmio FOB.
- **NOPA mensal**: mais um "release" sem dado novo de fato (paywall), agora referenciado
  como `release-nopa-2026-09-22`.
- **Confirmação da centralização plena da exportação de palma pela Danantara** — alvo 01/09,
  já 21 dias passados sem confirmação.
- **Vigência da isenção PIS/Cofins do biodiesel** (53 dias vencida) e **MP 1.358/2026 da
  gasolina** (73 dias vencidos) — checar notícia de renovação/expiração.
- **Marco de 109 dias sem revisão humana do `tributario_watch.toml`** — pelo menos dois
  vetores (isenção PIS/Cofins biodiesel, MP 1.358/2026) já vencidos sem registro de renovação.
- **Detalhamento das manchetes sobre alta física da soja no Brasil (Canal Rural, 21/09) e das
  3 notícias mantidas em 22/09** — monitorar se a fonte RSS traz o corpo do texto ou números
  concretos nas próximas atualizações.
- **Revisão de D+180 da tese original do ratio Far/Soj**, programada para 2026-12-08.

## Honestidade

- **A anomalia mais séria desta leitura: farelo e heating oil fecham hoje com abertura,
  máxima, mínima e volume idênticos, byte a byte, aos de ontem — apenas o fechamento
  muda.** Isso é estatisticamente incompatível com duas sessões de pregão distintas de
  contratos líquidos e sugere fortemente que o dado capturado hoje não representa uma sessão
  nova e fechada, mas sim uma releitura do mesmo snapshot de 21/09 com apenas um campo de
  "cotação corrente" atualizando. Esta leitura tratou os níveis de fechamento como válidos
  para fins de nível técnico (a fila os reporta e os gatilhos de resistência/suporte
  continuam corretos em termos de onde o preço está), mas rebaixou explicitamente a confiança
  em qualquer argumento que dependesse da qualidade da sessão em si (volume, confirmação de
  tendência) — especialmente na leitura de óleo, onde a margem de biodiesel de hoje se apoia
  diretamente no HO=F suspeito.
- **Os volumes de todos os quatro contratos monitorados (soja 4.041, farelo 1.410, óleo 952,
  heating oil 294) estão entre 0,65% e 3,7% do volume da última sessão plena documentada
  (18/09: 108.222, 113.303, 67.046 e 45.315, respectivamente)** — mesmo nos dois contratos
  sem duplicação confirmada de OHLC (soja e óleo, porque as linhas brutas de 21/09 não
  sobreviveram na janela deste dump para comparação direta), o volume por si só já é baixo
  o suficiente para reduzir a confiança em tratar o fechamento de hoje como representativo.
- **As linhas brutas de `cme_cbot` para soja e óleo em 21/09 não aparecem mais neste dump** —
  só sobrevivem indiretamente, via os valores já usados nos indicadores calculados naquele
  dia (soja 1.327,00; óleo 68,79). Isso significa que não foi possível verificar
  diretamente, nesta janela, se soja e óleo também exibiam a mesma duplicação de
  abertura/máxima/mínima/volume observada em farelo e heating oil — a hipótese de que a
  anomalia é mais ampla (afetando os quatro contratos) é plausível dado o padrão de volume
  baixo generalizado, mas não está confirmada com o mesmo rigor para soja e óleo quanto está
  para farelo e heating oil.
- **USDA Crop Progress não traz corte novo pela segunda segunda-feira seguida** (nem 14/09
  nem 21/09 aparecem; o corte mais recente ainda é o de 13/09) — não há, no briefing, uma
  explicação para essa ausência recorrente; pode ser uma limitação da fonte para esses
  cortes específicos ou um atraso de captura que se repete.
- **O físico de farelo na média do Rio Grande do Sul (fonte Clicmercado) segue com o mesmo
  valor exato (R$1.860,00/ton) em todos os pontos de dados visíveis do dump, de 08/09 a
  21/09** — agora 14 dias corridos de valor idêntico dígito a dígito, o que segue sendo
  estatisticamente muito improvável para uma série de preço físico genuíno e reforça a
  suspeita, já registrada em leituras anteriores, de que essa fonte específica não está
  atualizando de fato.
- **As manchetes de notícia de hoje e de ontem estão disponíveis apenas como título** — o
  corpo do texto da manchete do Canal Rural sobre alta de R$1-2/saca (21/09) não está no
  dump, e o item de contagem de 22/09 (`noticias | items_fetched`, 3 itens mantidos) não
  traz o texto desses 3 itens. Não é possível citar números de fonte primária para
  quantificar exatamente a alta física mencionada no título.
- **O corte de COT `release-cftc_cot-2026-09-15` segue sendo o dado de posicionamento mais
  recente**, agora sete dias corridos depois do corte. O próximo corte (posições de 22/09,
  esperado 25-26/09) resolve essa lacuna.
- **Percentil histórico de posicionamento COT não está disponível no briefing** — toda
  leitura de "fundos comprando/vendendo" nesta série usa variação absoluta semana a semana de
  contratos, não percentil histórico.
- **O item de fila `release-nopa-2026-09-22` é mais uma repetição sem dado novo** — o mesmo
  padrão de todas as leituras anteriores desde que este monitoramento começou (paywall,
  `monthly_status` em 0,0 bool).
- **`tributario_watch.toml` sem atualização há 109 dias corridos** — pelo menos dois vetores
  (isenção PIS/Cofins do biodiesel, MP 1.358/2026) já passaram da vigência registrada sem
  nota de renovação ou expiração.
- **A previsão INMET para 22/09 é previsão meteorológica, não medição de precipitação ou
  temperatura real** — as menções a "chuva", "chuva isolada" e "trovoadas" são indicativas do
  boletim, não confirmação de que o evento ocorreu ou ocorrerá.
- **Sem PTAX de 22/09 neste dump** — o cálculo de paridade da soja brasileira de hoje reusa o
  USD/BRL de 21/09 (5,1117), um lag normal de publicação (a PTAX de hoje costuma sair mais
  tarde no dia), não uma anomalia.
- **MPOB (palma Malásia) segue com parser quebrado** — nenhum dado de produção/estoque de
  palma malaia disponível, o que impede monitorar diretamente o catalisador represado da
  centralização de exportação indonésia (Danantara).
- **BCBA (Argentina) segue sem links de relatório detectados**, com o carimbo mais recente
  ainda em 09/09 — nenhum dado de safra ou exportação argentina disponível além do que já
  vem consolidado pelo WASDE.
- **Os forecasts estatísticos internos (bandas 7d/30d) foram gerados hoje sobre o fechamento
  de 22/09** — o viés "altista" em soja e farelo e "lateral"/"altista" em óleo reflete
  extrapolação estatística de tendência (MA20 + volatilidade + slope), não uma reavaliação
  fundamentalista; esta leitura mantém farelo em bull, soja em neutro e óleo em bear a partir
  da análise qualitativa, não das bandas estatísticas — e, dada a anomalia de dado descrita
  acima, essas bandas hoje se apoiam num fechamento de baixa confiabilidade.
- **A fila de julgamento volta a listar as revisões D+7 e D+90 da tese de 11/06 como
  "vencidas"** — o veredito de ambas já foi fechado em
  [[2026-09-17_ratio-far-soj-supera-nivel-de-abertura-da-tese-original-quarta-sessao]]; o
  sistema de fila não lê de volta os insights publicados para marcar a revisão como
  encerrada. Nenhuma ação nova é necessária sobre essas duas revisões específicas.
