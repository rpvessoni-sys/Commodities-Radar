---
data: 2026-09-24
titulo: "Corrigidos os números da sessão de 23/09 (farelo e soja caíram, não subiram, e a margem de biodiesel despencou -13,2% em vez de subir), o ratio Far/Soj ainda assim fecha em 84,30% — sua terceira alta consecutiva real, a menor distância já vista do teto 'apertado' de 87% — mantendo o farelo como o motor de alta do complexo e o óleo pressionado por queda real de margem de biodiesel, enquanto a soja recua -0,60% sobre volume finalmente saudável (117 mil contratos), encerrando de vez a falsa leitura de 'baixa liquidez' que dominou as últimas três leituras diárias"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT — sessão de **2026-09-23** (a mais recente disponível; corrigida frente ao que a leitura de ontem usou — ver [[2026-09-24_correcao-numeros-sessao-23set-fim-do-artefato-de-baixa-liquidez]]): soja (ticker ZSX26.CBT, venc. nov/26) abertura 1.324,75, máxima 1.327,25, mínima 1.311,00, fechamento **1.317,50**, volume **117.139 contratos**; farelo (ticker ZMZ26.CBT, venc. dez/26) abertura 370,70, máxima 373,40, mínima 367,70, fechamento **370,20**, volume **89.807 contratos**; óleo (ticker ZLZ26.CBT, venc. dez/26) abertura 67,95, máxima 68,21, mínima 67,03, fechamento **67,71**, volume **89.625 contratos**. Curva futura em 23/09 — soja: nov/26 (base) 1.317,50 → jan/27 1.333,00 → mar/27 1.341,50 → mai/27 1.349,00 → jul/27 1.353,50 (contango regular, levemente achatando no fim da curva); farelo: out/26 370,00 → dez/26 (base) 370,20 → jan/27 370,10 → mar/27 369,10 → mai/27 368,70 (backwardation leve nos meses mais distantes, -0,41% de dez/26 a mai/27); óleo: out/26 67,19 → dez/26 (base) 67,71 → jan/27 67,95 → mar/27 68,14 → mai/27 68,31 (contango regular, +1,66% de dez/26 a mai/27)
  - CME NYMEX heating oil (HO=F) — **2026-09-23**: abertura 4,6777, máxima 4,6875, mínima 4,6266, fechamento **4,6336** USD/galão, volume **859 contratos** — queda real de -6,24% frente aos 4,9421 de 22/09 (não a estabilidade que a leitura de ontem registrou por causa de um dado então duplicado); volume genuinamente baixo mesmo após a correção geral do resto da curva (ver Honestidade e [[2026-09-24_correcao-numeros-sessao-23set-fim-do-artefato-de-baixa-liquidez]])
  - Indicadores sintéticos internos (`indicators`) — **2026-09-23**: crush margin **US$2,4175/bushel** (farelo 370,20 + óleo 67,71 − soja 1.317,50); ratio Far/Soj **84,30%**; oil share **47,77%**; oil-meal spread **-0,6963 USD/bushel**; ISF (Índice de Sobra de Farelo) 60/100; ISO (Índice de Suporte do Óleo) 80/100; paridade BR da soja **R$149,34/saca** (CBOT 1.317,50 × USD/BRL 5,1414, agora com PTAX do próprio dia — ver Honestidade); margem de biodiesel US **US$1,9204/galão** (receita 7,7986 = HO 4,63 + 1,5×RIN 2,11; custo 5,8782 = óleo 5,0782 + industrial 0,80), queda de -13,23% frente aos 2,2131 de 22/09. Série corrigida dos últimos dias — ratio Far/Soj: 18/09 82,53% → 21/09 83,22% → 22/09 83,90% → 23/09 **84,30%**; oil share: 18/09 48,75% → 21/09 48,31% → 22/09 47,81% → 23/09 **47,77%** (mínima real da janela); margem biodiesel: 17/09 2,2927 → 18/09 2,3063 → 21/09 2,0908 → 22/09 2,2131 → 23/09 **1,9204** (maior queda diária desta janela, -13,23%)
  - BCB PTAX — **2026-09-23** (dado do próprio dia disponível pela primeira vez em três leituras, resolvendo o lag reportado ontem): USD/BRL **5,1414** (alta de +0,49% frente aos 5,1161 de 22/09), EUR/BRL 5,8576, Selic diária 0,050788% a.a. (séries SGS 1, 21619, 11) — o real enfraqueceu no mesmo dia em que a soja em Chicago caiu, um efeito parcialmente compensatório sobre a paridade em reais
  - NAG físico BR (`nag_fisico`) — **2026-09-23**: farelo Rondonópolis/MT (BCSP) **R$2.200,00/ton, var 0,0% — terceira leitura seguida no mesmo patamar (21, 22 e 23/09), a confirmação física mais sólida desta série**; farelo Mato Grosso/IMEA **R$1.982,28/ton, var 0,0% — quarta leitura seguida sem mudança (18, 21, 22 e 23/09)**, uma sequência que começa a levantar a mesma suspeita de estagnação de fonte já vista antes na série do RS (ver Honestidade); farelo média Rio Grande do Sul (Clicmercado) **R$2.130,00/ton, var +14,52% — ROMPE o congelamento de 14 dias corridos em R$1.860,00/ton** (08 a 22/09) que as três últimas leituras vinham registrando como suspeito, e o novo valor passa a ficar ACIMA do IMEA, embora ainda abaixo de Rondonópolis; soja Paraná interior (CEPEA/ESALQ via NAG) R$155,07/saca (-0,28% frente a 22/09); prêmio export farelo Paranaguá 0,12 USD/short_ton (congelado desde 08/09, agora **16 dias corridos**); prêmio export óleo Paranaguá 0,1 cts/lb (mesmo congelamento, 16 dias)
  - CEPEA/ESALQ Soja Paranaguá (via NAG) — **2026-09-23**: R$161,65/saca (-0,17% frente a 22/09); spread Paranaguá−Paraná interior de R$6,58/saca (161,65 − 155,07), um pouco mais largo que os R$6,43 de 22/09 (+2,33%)
  - CEPEA RSS — contagem de itens sobe para 109 em 24/09 (de 106 em 22-23/09), mas sem novo corpo de headline relevante capturado; a última manchete com corpo de texto ainda é a de 18/09
  - Notícias Agrícolas/Canal Rural/Farm Progress (RSS) — DADO NOVO nesta leitura: headline de **2026-09-23** (Canal Rural): "Produtor segura a soja, mercado freia e preços têm movimentos distintos; confira as cotações" — narrativa de retenção de venda pelo produtor coincidindo com o próprio recuo real de -0,60% da soja em Chicago nesta mesma sessão (sem corpo de texto disponível neste dump, ver Soja e Honestidade); headline de 22/09 (Farm Progress) "Shrinking supplies keep prospects for $14 soybeans on table" segue como a mais recente do lado americano; contagem de 24/09 registra 160 itens lidos e apenas 2 mantidos (queda frente aos 5 de dias anteriores)
  - CFTC COT Managed Money — corte de **2026-09-15** (sem corte novo; próximo corte é o de posições de 22/09, esperado por volta de 25-26/09, ou seja, nos próximos 1-2 dias): farelo net long 183.111 contratos (+16,12% vs 08/09); óleo net long 101.480 (+10,65%); soja net long 241.501 (-6,13%)
  - USDA Crop Progress — corte de **2026-09-20** (ainda o mais recente, quatro dias de idade): 12% excelente / 46% boa (G/E 58%), 10% pobre, colheita 2025/26 em **12% concluída**
  - USDA WASDE — edição de **2026-09-11** (sem edição nova, agora 13 dias de idade): farelo Argentina 2026/27 exportação 2,99 mi t; farelo Brasil 2025/26 exportação 0,2 mi t
  - NOPA — item de fila `release-nopa-2026-09-24`: `monthly_status` em 0,0 bool (paywall, sem dado novo, mesmo padrão de todas as leituras anteriores)
  - ABIOVE projeções mensais — balanços out-dez/2026, sem revisão nesta janela: produção de farelo BR caindo 2.142,97 (out) → 1.977,59 (nov) → 1.659,04 (dez) mil t; exportação de farelo BR caindo 850 → 800 → 700 mil t no mesmo período; estoque final de soja BR caindo 5.720,77 (out) → 3.658,99 (nov) → 1.889,91 (dez) mil t, consumo do esmagamento seguindo forte
  - NOAA CPC ENSO — El Niño Advisory, inalterado (carimbo 2026-09-24)
  - MPOB — carimbo 2026-09-24, parser sem números extraídos (mesma barreira há semanas)
  - INMET — previsão para **2026-09-24 (HOJE)**: Cascavel/PR 25°C/13°C "muitas nuvens"; Maringá/PR 24°C/15°C "muitas nuvens"; Passo Fundo/RS 23°C/10°C com **nova menção de possibilidade de geada** pela manhã; núcleo de Mato Grosso — Cuiabá 37°C/21°C, Sinop 38°C/23°C, Sorriso 37°C/24°C, Lucas do Rio Verde 37°C/23°C, todos com pancadas de chuva e trovoadas isoladas; Rio Verde/GO 34°C/18°C com pancadas de chuva e trovoadas — calor mais intenso que ontem no núcleo produtor de MT, com chuva convectiva típica do início da janela de plantio da safra 2026/27
  - system/tributario_watch.toml (lido como referência, não editado) — `atualizado_em` 2026-06-05 em todos os 10 eventos catalogados, **111 dias corridos** sem revisão humana frente a hoje (24/09)
  - Forecasts estatísticos internos (bandas 7d/30d) — geração de **2026-09-24**, sobre o fechamento corrigido de 23/09, alvos 01/10 e 24/10: viés "altista" em soja e farelo nos dois horizontes; óleo em "lateral" (7d) e **"baixista"** (30d) — segunda geração seguida com essa configuração (extrapolação estatística, não fundamentalista — ver Honestidade)
  - Fila de julgamento — 2026-09-24, 7 itens: `alerta-quebra_resistencia-soja_cbot-2026-09-23`, `alerta-quebra_suporte-oleo_cbot-2026-09-23`, `alerta-quebra_resistencia-farelo_cbot-2026-09-23`, `alerta-quebra_suporte-complexo_soja-2026-09-23`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`, `release-nopa-2026-09-24`
  - Cruza com [[2026-09-24_correcao-numeros-sessao-23set-fim-do-artefato-de-baixa-liquidez]] (auditoria completa da revisão de dados desta sessão, entrega separada de hoje), [[2026-09-23_leitura-complexo]] (leitura de ontem, cujos números de sessão foram revisados), [[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]] (padrão de revisão do HO=F documentado em ocorrências anteriores), [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (tese original do ratio, nível de abertura 81,4%) e [[2026-09-17_ratio-far-soj-supera-nivel-de-abertura-da-tese-original-quarta-sessao]] (veredito de invalidação técnica da tese baixista de junho, D+7 e D+90 já fechados)
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
farelo vira o motor de rentabilidade do esmagador). Hoje, **84,30%** (indicators, 2026-09-23),
o complexo segue na zona neutra, mas a apenas **2,70 pontos percentuais** do teto "apertado" —
a menor distância já registrada nesta série de leituras diárias, batendo o recorde anterior de
2,72 p.p. de ontem.

**O que muda hoje, quinta-feira 24/09, não é a direção do complexo — é a base de dados sobre a
qual essa direção se apoia.** Ao preparar esta leitura, cruzei os fechamentos e volumes usados
pela leitura de ontem contra as linhas brutas que o dump de hoje traz para a mesma sessão de
23/09, e eles não batem em farelo, soja, óleo nem heating oil. O achado completo está registrado
em separado em [[2026-09-24_correcao-numeros-sessao-23set-fim-do-artefato-de-baixa-liquidez]];
aqui vai o resumo que importa para a leitura de hoje.

**Achado 1 — o "regime de baixa liquidez" que as leituras de 21, 22 e 23/09 descreveram como um
fato de mercado não existiu em soja, farelo e óleo: era um artefato de captura de dado.** Os
volumes reais da sessão de 23/09, agora confirmados de forma independente pela fila de
julgamento autogerada (que usa o mesmo banco de indicadores), são **117.139 contratos em soja,
89.807 em farelo e 89.625 em óleo** — 30 vezes maiores que os 3.843/2.996/2.986 usados na
leitura de ontem, e plenamente comparáveis às sessões historicamente líquidas desta série (a
referência de 18/09 era 108.222/113.303/67.046). O mecanismo mais provável é o mesmo já
documentado duas vezes antes nesta série (11/09 e 15/09): o dado mais recente do dump às vezes
captura uma leitura intraday parcial em vez do fechamento consolidado, e a geração seguinte do
briefing traz a correção. A diferença desta vez é que a correção também mudou o **sinal** do
movimento em dois pontos importantes, não apenas a magnitude.

**Achado 2 — farelo caiu, não subiu, na sessão de 23/09 (-0,13%, não +0,43%), e soja caiu mais
do que o farelo (-0,60%), não ficou estável.** Isso significa que a "terceira alta consecutiva
do farelo" que a leitura de ontem descrevia como um movimento de força absoluta não aconteceu —
o que aconteceu, e que segue sendo verdade com os números corrigidos, é que o farelo caiu MENOS
que a soja, o que ainda empurra o ratio Far/Soj para cima (82,53% → 83,22% → 83,90% → **84,30%**,
agora uma trajetória real de três altas consecutivas). A tese bull-farelo sobrevive, mas muda de
natureza: não é mais sobre força absoluta do farelo, é sobre força relativa do farelo dentro do
crush — uma distinção operacional relevante (ver Farelo, abaixo).

**Achado 3 — a margem de biodiesel americana não deu um pequeno repique de +1,17%: ela caiu
-13,23%, a maior queda diária desta janela, porque o heating oil (HO=F) que alimenta essa
fórmula de fato despencou -6,24% (de 4,9421 para 4,6336 USD/galão), e não ficou estável como
sugeria o par de valores então duplicado.** Esse era o contraponto mais frágil da leitura de
ontem contra a tese bear-óleo — e ele simplesmente não existe nos dados reais. O sinal real
reforça, não enfraquece, a tese bear-óleo.

**O que não muda: o volume do heating oil (HO=F) especificamente segue genuinamente baixo (859
contratos em 23/09, apenas 3,1% dos 27.344 de 22/09) mesmo depois da correção geral do resto da
curva** — diferente de soja, farelo e óleo, que se revelaram plenamente líquidos assim que os
números corretos chegaram, o HO=F parece ter tido, de fato, uma sessão pouco negociada, ou ainda
carrega o mesmo problema de captura que os outros quatro instrumentos já tiveram corrigido.
Como esse fechamento alimenta diretamente a margem de biodiesel usada na tese de óleo, ele
mantém, sozinho, o mesmo grau de ceticismo metodológico que a série vinha aplicando ao complexo
inteiro.

**Leitura de uma linha**: o pivô do complexo continua sendo o ratio Far/Soj, hoje em 84,30% — a
menor distância já vista do teto "apertado" de 87%, agora confirmada por dados de sessão
plenamente líquida, não por um artefato de baixo volume. Maior convicção: bull-farelo, sustentado
por três altas consecutivas reais do ratio e por uma terceira confirmação física em Rondonópolis
(R$2.200/ton), mais uma nova confirmação em RS (que rompeu 14 dias de congelamento e saltou
+14,52%). Segunda maior convicção: bear-óleo, agora reforçada por uma queda real (não um repique
fictício) de -13,23% na margem de biodiesel americana. Confiança geral na magnitude exata dos
movimentos de farelo e heating oil segue com uma reserva pontual (ver Honestidade), mas a
confiança na direção do complexo como um todo está mais alta hoje do que em qualquer uma das
últimas três leituras, porque a base de dados finalmente bate com a fila autogerada em todos os
quatro instrumentos de maior volume.

## Soja

**Viés: neutro, mantido — mas a natureza do "neutro" muda: a sessão de 23/09, revisada, mostra
um recuo real de -0,60% sobre volume finalmente saudável (117.139 contratos, o maior desta
janela), não mais a quase-estabilidade de baixíssimo volume que a leitura de ontem registrava.**

O que sustenta a tese (lado altista):

- **A soja segue folgadamente acima da resistência de referência de 1.180,00** (fila
  `alerta-quebra_resistencia-soja_cbot-2026-09-23`: fechamento 1.317,50 vs. nível 1.180,00),
  uma folga de **+11,65%** — menor que os +12,39% calculados ontem com o fechamento então
  incorreto de 1.326,25, mas ainda uma folga ampla, sem qualquer sinal de risco de reversão
  técnica no curto prazo.
- **A curva futura permanece em contango regular**: nov/26 (base) 1.317,50 → jan/27 1.333,00 →
  mar/27 1.341,50 → mai/27 1.349,00 → jul/27 1.353,50 (CME CBOT, 23/09) — o mercado a termo
  segue precificando preços mais altos à frente, com a inclinação levemente achatando nos meses
  mais distantes (+1,18% nov→jan, +0,33% mai→jul) — coerente com um contango "normal", não uma
  aposta agressiva em alta futura.
- **Manchete de Farm Progress (22/09, via `noticias_rss`): "Shrinking supplies keep prospects
  for $14 soybeans on table"** segue como o contraponto altista mais forte do lado americano —
  uma narrativa de aperto de oferta sustentando um cenário de preço-alvo de US$14/bushel, ainda
  acima do fechamento atual de US$13,175/bushel equivalente a 1.317,50 cts. O corpo da notícia
  segue indisponível neste sistema (ver Honestidade).
- **A curva de crop progress (corte de 20/09, ainda o mais recente) mostra condição estável em
  G/E 58%** — a safra americana não está se deteriorando na reta final do ciclo, apesar da
  colheita já avançando (12% concluída em 20/09, dobrando frente aos 6% de 13/09).

**O que invalida / risco:**

- **A sessão de 23/09, corrigida, mostra a soja caindo -0,60% (de 1.325,50 para 1.317,50),
  não subindo +0,09% como a leitura de ontem registrava** — a manchete nova de 23/09 do Canal
  Rural ("Produtor segura a soja, mercado freia e preços têm movimentos distintos") é
  qualitativamente coerente com esse recuo real: um mercado que "freia" depois de uma sequência
  de altas, com o produtor brasileiro retendo a venda em vez de acelerá-la diante de um CBOT
  mais fraco.
- **O COT de 15/09, ainda o mais recente, mostrou os fundos reduzindo net long em soja em
  -6,13%** (de 257.258 para 241.501 contratos), com short subindo — o único das três pernas do
  complexo em que o COT mais recente aponta para *menos* convicção compradora dos fundos. O
  próximo corte (posições de 22/09) é esperado por volta de **25-26/09 — nos próximos 1 a 2
  dias**, o mais próximo que este monitoramento já esteve de uma atualização de posicionamento.
- **A queda de -0,60% de hoje ocorre sobre o range intradiário mais amplo desta janela recente
  (1.311,00-1.327,25, 1,22% de amplitude)**, um sinal de que o mercado voltou a negociar de
  forma ativa (consistente com o volume de 117.139 contratos), não um movimento marginal — a
  informação carregada por essa sessão é mais confiável do que a de qualquer uma das três
  sessões anteriores, mas a direção agora é de recuo, não de estabilidade.
- **Nível técnico a vigiar:** um fechamento de volta abaixo de 1.180 desfaria formalmente o
  rompimento; com a folga em +11,65%, esse cenário segue distante, mas a folga encolheu frente
  a ontem.

**Leitura operacional:** a soja recuou de forma real e sobre volume saudável — o primeiro
movimento desta janela que carrega informação confiável sobre a intenção efetiva do mercado, em
vez de um fechamento de baixa liquidez. Para quem está comprado, a folga técnica de +11,65%
acima da resistência de 1.180 e o contango da curva seguem sustentando a posição estrutural, mas
o recuo real de hoje, somado à redução de net long dos fundos desde 15/09 e à manchete de
"produtor segura a soja" (que sugere resistência do lado da oferta doméstica em vender, não
necessariamente força de preço), pede cautela para reforçar posição no fechamento de hoje
especificamente. Para quem opera vendido, o recuo de -0,60% sobre volume real é o primeiro
gatilho tático desta janela que merece ser levado a sério — mas ainda dentro de uma folga técnica
ampla o suficiente (+11,65%) para não representar reversão de tendência. O evento mais relevante
para os próximos dias é o corte de COT de 25-26/09, o primeiro capaz de confirmar se a redução de
net long vista em 15/09 se tornou uma tendência mais ampla de realização de lucro pelos fundos.

## Farelo

**Viés: bull, mantido — mas agora apoiado em dados de sessão plenamente líquida, não em um
artefato de baixo volume. O farelo caiu na sessão de 23/09, mas caiu menos que a soja, e o ratio
Far/Soj completou sua terceira alta consecutiva real, com a maior confirmação física desta série
(três praças brasileiras diferentes mostrando aperto ao mesmo tempo).**

O que sustenta a tese:

- **O ratio Far/Soj fechou em 84,30% hoje** (indicators, sessão de 23/09), a terceira alta
  seguida real (82,53% em 18/09 → 83,22% em 21/09 → 83,90% em 22/09 → **84,30%** hoje), a maior
  leitura desta série e a distância mais curta já registrada até o território "apertado" (87%):
  apenas **2,70 pontos percentuais**. Isso mantém o ratio **+2,90 pontos percentuais** acima do
  nível de abertura da tese baixista original de 11/06/2026
  (81,4%, [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]) — o veredito de invalidação
  técnica dessa tese, fechado em
  [[2026-09-17_ratio-far-soj-supera-nivel-de-abertura-da-tese-original-quarta-sessao]], segue de
  pé — trata `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` e
  `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`: ambas seguem aparecendo
  como "vencidas" na fila porque o sistema não lê de volta os insights já publicados, mas o
  veredito de ambas já está fechado desde 17/09; resta em aberto apenas a revisão de D+180,
  programada para 2026-12-08.
- **O físico de farelo em Rondonópolis/MT (fonte BCSP, via NAG) segue em R$2.200,00/ton pela
  TERCEIRA leitura seguida (21, 22 e 23/09, var 0,0% nas três)** — a confirmação mais sólida
  desta série de que o salto de +8,37% visto em 21/09 (de R$2.030,00 para R$2.200,00) não foi
  um evento de um único dia, mas um novo patamar consolidado.
- **A praça física da média do Rio Grande do Sul (Clicmercado) rompeu hoje o congelamento de 14
  dias corridos** (08 a 22/09, sempre em R$1.860,00/ton) e saltou **+14,52% para
  R$2.130,00/ton** — a terceira praça física distinta a mostrar movimento de aperto em dias
  próximos, e agora a segunda mais alta das três monitoradas (acima do IMEA, ainda abaixo de
  Rondonópolis). Esse salto precisa ser lido com uma reserva: é a primeira leitura nesse novo
  patamar depois de duas semanas parado, então ainda não há uma segunda confirmação de que o
  valor se sustenta (ver Honestidade) — mas a coincidência temporal com o aperto já confirmado
  em Rondonópolis e no ratio Far/Soj torna a hipótese de "correção de uma fonte que não estava
  atualizando" mais plausível do que "ruído".
- **O oil share caiu para 47,77% hoje** (de 47,81% ontem, 48,75% em 18/09) — a mínima real desta
  janela de leituras, o espelho direto do farelo ganhando protagonismo relativo dentro do valor
  total gerado pelo crush.
- **O oil-meal spread fechou em -0,6963 USD/bushel hoje** (de -0,6842 ontem, -0,385 em 18/09) —
  a maior distância real já registrada nesta série entre o valor do farelo e o valor do óleo,
  em termos de bushel-equivalente.
- **O farelo segue folgadamente acima da resistência histórica de 325,00** (fila
  `alerta-quebra_resistencia-farelo_cbot-2026-09-23`: 370,20 vs. 325,00), folga de **+13,91%**.
- **O COT de 15/09 mostrou os fundos com net long em farelo em 183.111 contratos (+16,12%
  frente a 08/09)** — ainda o dado de posicionamento mais recente.
- **A trajetória sazonal da ABIOVE para o Brasil continua apontando para alívio de oferta
  doméstica de farelo à frente**, sem revisão nesta janela: produção projetada caindo de 2.142,97
  mil t (out/26) para 1.977,59 (nov/26) e 1.659,04 mil t (dez/26); exportação de 850 para 800 e
  700 mil t no mesmo período.

**O que invalida / risco:**

- **A própria natureza do movimento de hoje mudou de sinal frente ao que a leitura de ontem
  descrevia**: o farelo caiu -0,13% na sessão de 23/09 (não subiu +0,43%). O ratio Far/Soj só
  sobe porque a soja caiu ainda mais (-0,60%) — a tese, portanto, é sobre força *relativa* do
  farelo dentro do crush, não força absoluta do produto isoladamente. Quem está comprado
  diretamente em farelo (sem o hedge via ratio ou spread) precisa ter clareza dessa distinção: o
  produto em si perdeu valor nominal na última sessão disponível.
- **O IMEA/MT segue com o mesmo valor exato (R$1.982,28/ton) por quatro leituras seguidas** (18,
  21, 22 e 23/09) — um padrão de estagnação de fonte que já foi visto antes nesta série (com o
  RS, que hoje finalmente se moveu) e que merece o mesmo grau de suspeita: sem uma quinta leitura
  mostrando movimento, não é possível confirmar se o IMEA está genuinamente estável ou apenas sem
  atualizar (ver Honestidade).
- **O salto do RS de hoje é uma leitura isolada, sem segunda confirmação ainda** — o mesmo
  cuidado metodológico aplicado a qualquer movimento de um único dia nesta série.
- **O prêmio de exportação de farelo em Paranaguá segue congelado em 0,12 USD/short_ton há 16
  dias corridos** (desde 08/09) — se o aperto físico doméstico fosse amplo e sustentado, seria
  razoável esperar, eventualmente, algum reflexo no canal de exportação FOB; essa confirmação
  ainda não apareceu.
- **A curva futura de farelo mostra uma leve inversão (backwardation) nos meses mais distantes**:
  dez/26 (base) 370,20 → jan/27 370,10 → mar/27 369,10 → mai/27 368,70 (-0,41% de dez/26 a
  mai/27) — o mercado a termo não está precificando um aperto estrutural que se estenda
  indefinidamente; é consistente com a trajetória sazonal de alívio de oferta da ABIOVE.
- **Os índices sintéticos ISF e ISO seguem travados em 60/100 e 80/100**, sem reação a mais de
  dez dias de oscilação do ratio e do crush margin.

**Leitura operacional:** a tendência estrutural de farelo relativamente mais forte que a soja
segue intacta, e hoje ganha o reforço mais sólido desta série — três praças físicas brasileiras
distintas (Rondonópolis pela terceira vez, RS rompendo o congelamento, e o próprio ratio Far/Soj
em máxima) apontando na mesma direção, sobre volume de futuro finalmente confirmado como
saudável. Para quem está comprado no spread Far/Soj (a forma mais limpa de capturar esta tese,
já que o farelo em si caiu em termos absolutos na última sessão), o gatilho mais sólido é a
continuidade do ratio acima de 84% com uma segunda leitura de RS confirmando o novo patamar
físico. Para quem está comprado em farelo direcionalmente (sem hedge), vale reconhecer que a
última sessão foi de queda nominal, ainda que dentro de uma tendência maior de alta relativa. Para
quem está vendido, o nível técnico (370,20, folga de +13,91% sobre a resistência) e o calendário
sazonal da ABIOVE seguem desfavoráveis à tese de queda; a leve inversão da curva futura nos meses
mais distantes é o único argumento a favor de não perseguir o movimento no vencimento mais
distante.

## Óleo

**Viés: bear, reforçado — quarta sessão seguida abaixo do suporte técnico, com o oil share em
mínima real da janela e, o achado mais importante de hoje, uma queda REAL de -13,23% na margem
de biodiesel americana, não o pequeno repique que a leitura de ontem registrava sobre um dado
então duplicado.**

O que sustenta a tese:

- **Óleo fechou em 67,71 USD cts/lb hoje**, uma queda de -0,31% frente aos 67,92 de ontem,
  aprofundando a distância abaixo do suporte de referência de 72,00 (fila
  `alerta-quebra_suporte-oleo_cbot-2026-09-23`: **-5,96%**, a maior desta série).
- **A margem de biodiesel americana caiu para US$1,9204/galão hoje, uma queda de -13,23% frente
  aos US$2,2131 de ontem — a maior queda diária de toda esta janela de leituras.** Essa queda é
  real: o heating oil (HO=F) que alimenta o lado da receita da fórmula despencou de 4,9421 para
  **4,6336 USD/galão (-6,24%)**, uma sessão de fato mais fraca, e não a estabilidade que um par
  de valores então duplicado sugeria ontem (ver [[2026-09-24_correcao-numeros-sessao-23set-fim-do-artefato-de-baixa-liquidez]]).
  O contraponto altista mais frágil da leitura de ontem — "a margem está se recuperando" — não
  existe nos dados reais; o sinal correto reforça a tese bear.
- **O oil share caiu para 47,77% hoje** (de 47,81% ontem, 48,75% em 18/09) — mínima real desta
  janela, o óleo perdendo participação no valor total gerado pelo crush pela quarta sessão
  seguida.
- **O oil-meal spread fechou em -0,6963 USD/bushel** (de -0,6842 ontem, -0,385 em 18/09) — o
  óleo cada vez mais atrás do farelo em termos de valor por bushel-equivalente.
- **O ISO (Índice de Suporte do Óleo) segue em 80/100**, sem melhora.
- **O forecast estatístico interno de 30 dias segue em "baixista"** (segunda geração seguida
  nessa configuração) — extrapolação de tendência, não fundamentalista, mas coerente com a
  deterioração real do oil share e da margem de biodiesel.
- **A lente fiscal brasileira segue estruturalmente desfavorável, sem mudança hoje**: a MP
  1.363/2026 (subvenção ao diesel fóssil, vigente até 31/12/2026) segue plenamente vigente; a
  isenção de PIS/Cofins do biodiesel na mistura está agora **55 dias corridos vencida** (vigência
  até 31/07/2026) sem sinal de renovação.

**O que sustenta um contraponto — mas agora com um grau de reserva bem menor que ontem:**

- **O volume real de HO=F em 23/09 (859 contratos) é genuinamente baixo mesmo depois da correção
  geral do resto da curva** — apenas 3,1% dos 27.344 contratos de 22/09. Diferente de soja,
  farelo e óleo, cujo volume se revelou saudável assim que os números corretos chegaram, o HO=F
  parece ter tido, de fato, uma sessão pouco negociada em 23/09, ou ainda carrega o mesmo tipo de
  problema de captura que os outros contratos já tiveram corrigido. Isso significa que o
  fechamento de 4,6336 usado na margem de biodiesel de hoje ainda merece um grau de ceticismo
  metodológico — mas, diferente de ontem, esse ceticismo é sobre a magnitude exata da queda
  (-6,24%), não sobre a direção (o valor não é mais suspeito de ser uma cópia idêntica do dia
  anterior).
- **O RIN D4 (crédito de biocombustível renovável americano) permanece constante na fórmula
  interna** — nenhuma variação real de política regulatória americana explicaria a queda de
  margem de hoje; ela vem inteiramente do lado do heating oil.
- **A curva futura de médio prazo segue em contango regular**: out/26 67,19 → dez/26 (base)
  67,71 → jan/27 67,95 → mar/27 68,14 → mai/27 68,31 — sem sinal de reprecificação estrutural
  de curto prazo, o que contrasta com a leve inversão vista na curva do farelo.
- **Catalisadores de alta represados, ainda não correntes**: B16 (elevação da mistura de
  biodiesel para 16%) segue "adiado", resultado esperado por volta de novembro/2026; a
  centralização da exportação de palma pela Indonésia via Danantara, que tinha alvo de assunção
  plena em 01/09/2026, já soma **23 dias** de atraso sem confirmação — ambos seguem como upside
  represado, não corrente.

**Leitura operacional:** o quadro técnico (abaixo do suporte de 72,00 pela quarta sessão seguida,
oil share em mínima real da janela) e, agora, um fundamento REAL de queda de margem de biodiesel
(-13,23%, não um repique) reforçam o lado vendido direcional com mais convicção do que a leitura
de ontem conseguia sustentar. Para quem está vendido, o nível técnico e o calendário fiscal (MP
1.363 vigente até dezembro, isenção PIS/Cofins já 55 dias vencida) seguem sustentando a posição,
agora sem o contraponto frágil de uma margem de biodiesel em "recuperação" que nunca existiu de
fato. Para quem está comprado ou avalia entrar, o argumento mais forte contra a tese bear
continua sendo uma confirmação de HO=F com volume saudável mostrando a margem de biodiesel
subindo de forma consistente — o que este dump não entrega hoje; ao contrário, entrega o oposto.
Para quem opera o spread farelo-óleo dentro do crush, o oil-meal spread fechou em -0,6963
USD/bushel, perto do ponto mais extremo já registrado nesta série (mesmo com os números
corrigidos) — um nível que merece atenção como possível zona de mean-reversion, mas sem qualquer
sinal técnico de reversão ainda presente.

## Spreads e crush (leitura de complexo)

O ratio Far/Soj fechou em **84,30%** hoje, a terceira alta consecutiva real (82,53% → 83,22% →
83,90% → 84,30%, de 18 a 23/09) e a maior leitura já registrada nesta série — dentro da zona
neutra (80-87%), mas a apenas **2,70 pontos percentuais** do teto "apertado" (87%) e a **4,30
pontos** do piso "abundante" (80%), a menor distância ao teto já registrada nesta série de
leituras diárias. O oil share, em **47,77%**, mostra o óleo respondendo por menos da metade do
valor gerado no esmagamento, numa trajetória de queda quase monotônica desde 48,75% em 18/09
(48,75% → 48,31% → 47,81% → 47,77%). O crush margin, em **US$2,4175/bushel**, segue abaixo do
piso de referência de US$2,50 monitorado pela fila (`alerta-quebra_suporte-complexo_soja-2026-09-23`,
distância de **-3,30%**), com uma recuperação frente aos 2,3716 de ontem (+1,94%), mas ainda
distante do piso e oscilando num intervalo estreito (2,3584-2,4175) desde 18/09 — sinal de
estabilização abaixo do nível de referência, não de recuperação em curso.

Os dois índices compostos por contagem de condições — ISF (60/100) e ISO (80/100) — seguem
travados no mesmo patamar desde 11/09, agora há mais de treze dias corridos sem qualquer reação,
apesar de o ratio e o oil share terem se movido de forma expressiva e consistente nesse período
— o lembrete de sempre nesta série de que esses índices específicos reagem a mudanças de regime
estrutural, não a oscilações de curto e médio prazo dentro da mesma faixa.

O que muda hoje, sem alterar a leitura direcional de nenhuma dessas três métricas, é que a
confiança na magnitude exata dos movimentos agora é MAIOR, não menor, do que na leitura de ontem
— porque os números corrigidos batem com a fila autogerada em farelo, soja, óleo e crush margin
simultaneamente, algo que não acontecia nas três leituras anteriores. A confirmação física
tripla do lado do farelo (Rondonópolis pela terceira vez, IMEA congelado mas ainda no patamar
alto, RS rompendo 14 dias de estagnação) é, hoje, o conjunto de evidências mais robusto de toda
esta série — vem de três fontes de mercado físico brasileiro distintas, não do futuro de Chicago.

O COT de 15/09, ainda o dado de posicionamento mais recente nove dias depois, retrata os fundos
com net long ampliado em farelo (+16,12%) e óleo (+10,65%) e reduzido em soja (-6,13%) — o
próximo corte (posições de 22/09), esperado por volta de **25-26/09 (nos próximos 1-2 dias)**,
é o evento mais imediato desta janela inteira, capaz de dizer se os mesmos fundos já realizaram
lucro nas correções recentes ou se ampliaram ainda mais as posições de farelo e óleo diante do
quadro físico e fiscal descrito nesta leitura.

## Lente fiscal/regulatória BR

Antes de fechar qualquer tese de preço BR, os vetores tributários/regulatórios vivos que pesam
no complexo — todos do `system/tributario_watch.toml`, cujo carimbo mais recente
(`atualizado_em`) em todos os 10 eventos catalogados é 2026-06-05, ou seja, **111 dias corridos
sem revisão humana** frente a hoje (24/09):

- **MP 1.363/2026** (id `MP-1363-2026`, subvenção diesel fóssil R$1,12/L, vigente até
  31/12/2026): barateia o diesel fóssil no mix B15 (mistura obrigatória de 15% de biodiesel),
  reduzindo a competitividade relativa do biodiesel e a demanda doméstica por óleo de soja —
  vetor estrutural de baixa para óleo, plenamente vigente, sem mudança de status.
- **B16 (id `B16-CNPE-2026`, elevação da mistura obrigatória de biodiesel para 16%)** segue
  "adiado", resultado esperado por volta de novembro/2026. Upside represado (~436 mil toneladas
  de demanda potencial adicional de óleo), não corrente.
- **Isenção de PIS/Cofins do biodiesel na mistura** (id `PISCOFINS-BIODIESEL-ISENCAO`):
  vigência registrada até 31/07/2026 — já **55 dias corridos vencida** frente a 24/09/2026, sem
  registro de prorrogação ou expiração.
- **MP 1.358/2026** (subvenção gasolina R$0,89/L): vigência registrada até 11/07/2026, agora
  **75 dias corridos vencida**.
- **STJ REsp 2.165.276** (id `STJ-RESP-2165276`, crédito de PIS/Cofins sobre soja em biodiesel,
  direção "alta" para soja/óleo): sem novidade nesta janela.
- **EPA RFS 2026/2027** (id `EPA-RFS-2026-2027`, mandato de biocombustível americano, direção
  "alta" para óleo): sustenta o RIN D4, estável, e o RIN permanece constante na fórmula interna
  de margem de biodiesel usada por este sistema — a queda de margem de hoje vem inteiramente do
  heating oil, não de mudança regulatória.
- **Crédito 45Z** (id `45Z-CLEAN-FUEL`, em tramitação, direção "mista"): sem novidade.
- **Indonésia — Danantara** (id `DANANTARA-INDONESIA`) e **levy de exportação PMK 9/2026** (id
  `INDONESIA-LEVY-PMK9`): a assunção plena da centralização da exportação de palma pela
  Indonésia tinha alvo 01/09/2026 — já se passaram **23 dias** sem confirmação. Catalisador de
  alta represado para óleo (via substituição com palma) — ainda sem dado de MPOB disponível para
  monitorar diretamente (parser continua quebrado, ver Honestidade).
- **Indonésia B50** (id `INDONESIA-B50`, monitorando, direção "alta"): sem novidade.

Nenhum desses vetores muda a leitura de preço de hoje isoladamente — mas, em conjunto, eles
seguem reforçando a mesma assimetria já descrita em leituras anteriores: o mercado interno
brasileiro tem múltiplos desincentivos correntes ao óleo (MP 1.363 plenamente vigente, isenção
PIS/Cofins já 55 dias vencida) e múltiplos catalisadores de alta represados, não correntes (B16,
Danantara, B50). O óleo brasileiro segue mais fraco estruturalmente até que algum dos vetores
represados vire fato concreto — e a lacuna crescente de 111 dias sem revisão humana do catálogo
tributário é, em si, um risco operacional recorrente nesta série.

## Riscos e eventos próximos

- **Confirmação de uma segunda leitura do físico de farelo RS no novo patamar de R$2.130/ton** —
  hoje é a primeira leitura depois de 14 dias de congelamento; uma segunda confirmação eleva
  substancialmente a convicção na tese de aperto físico tripla.
- **Confirmação (ou ruptura) do padrão de estagnação do IMEA/MT**, agora em quatro leituras
  seguidas no mesmo valor exato (R$1.982,28/ton) — se uma quinta leitura repetir o valor, passa a
  merecer o mesmo tratamento de suspeita já aplicado ao RS antes de hoje.
- **Volume do heating oil (HO=F)** — única métrica que a correção geral de hoje NÃO resolveu
  (859 contratos em 23/09, ainda anormalmente baixo); a próxima sessão é o teste de se este é um
  problema pontual do ticker ou algo mais estrutural.
- **Próximo corte de COT (posições de 22/09), esperado por volta de 25-26/09 — nos próximos 1-2
  dias.** O evento mais imediato desta janela; primeiro capaz de confirmar se os fundos que
  ampliaram net long em farelo e óleo (COT de 15/09) já realizaram lucro ou ampliaram ainda mais
  as posições, e se a redução de net long em soja se acentuou.
- **USDA Crop Progress**: próximo corte esperado por volta de 27-28/09.
- **Nível técnico a vigiar em farelo:** volta abaixo de 325,00 desfaria o rompimento (folga
  atual +13,91%).
- **Nível técnico a vigiar em soja:** volta abaixo de 1.180,00 desfaria o rompimento (folga
  atual +11,65%, encolhendo frente aos +12,39% de ontem devido à correção de dados).
- **Nível técnico a vigiar em óleo:** recuperação acima de 72,00 desfaria a leitura de suporte
  rompido (distância atual -5,96%).
- **Crush margin:** retorno acima de US$2,50/bushel encerraria a leitura de suporte rompido
  monitorada pela fila (distância atual -3,30%, com uma recuperação de +1,94% frente a ontem).
- **Prêmio de exportação de farelo e óleo em Paranaguá**, congelado há 16 dias corridos.
- **NOPA mensal**: mais um "release" sem dado novo de fato (paywall), agora referenciado como
  `release-nopa-2026-09-24`.
- **Confirmação da centralização plena da exportação de palma pela Danantara** — alvo 01/09, já
  23 dias passados sem confirmação.
- **Vigência da isenção PIS/Cofins do biodiesel** (55 dias vencida) e **MP 1.358/2026 da
  gasolina** (75 dias vencidos) — checar notícia de renovação/expiração.
- **Marco de 111 dias sem revisão humana do `tributario_watch.toml`**.
- **Detalhamento das manchetes recentes** ("produtor segura a soja" de 23/09 e "$14 soybeans" de
  22/09) — monitorar se a fonte RSS traz o corpo do texto ou números concretos nas próximas
  atualizações.
- **Revisão de D+180 da tese original do ratio Far/Soj**, programada para 2026-12-08.
- **Possível repetição do padrão de revisão retroativa de dados** — este é o terceiro episódio
  em duas semanas (11/09, 15/09, 23/09); a partir de hoje, qualquer fechamento do dia mais
  recente do dump deveria ser tratado como sujeito a possível revisão de SINAL, não apenas de
  magnitude, até a geração seguinte confirmar (ver
  [[2026-09-24_correcao-numeros-sessao-23set-fim-do-artefato-de-baixa-liquidez]]).

## Honestidade

- **O achado mais importante desta leitura está registrado em separado**: os fechamentos e
  volumes de farelo, soja e óleo usados pela leitura de ontem para a sessão de 23/09 eram
  parciais — o dump de hoje traz farelo e soja mais BAIXOS (não mais altos) e volumes 30 vezes
  maiores, e a margem de biodiesel caiu -13,2% em vez de subir +1,17%, porque o heating oil que
  alimenta essa fórmula realmente caiu -6,24%. Ver
  [[2026-09-24_correcao-numeros-sessao-23set-fim-do-artefato-de-baixa-liquidez]] para a auditoria
  completa, produto por produto. Esta leitura usa exclusivamente os números corrigidos.
- **O volume de HO=F em 23/09 (859 contratos) segue genuinamente baixo mesmo após a correção
  geral do resto da curva** — apenas 3,1% dos 27.344 de 22/09. Diferente de soja, farelo e óleo,
  que se revelaram plenamente líquidos, este instrumento específico ainda carrega incerteza sobre
  se é uma sessão real de baixo volume ou um problema de captura ainda não corrigido para este
  ticker.
- **O IMEA/MT segue com o mesmo valor exato (R$1.982,28/ton) por quatro leituras seguidas** (18,
  21, 22 e 23/09) — um padrão que, se persistir por mais uma leitura, merece o mesmo tratamento
  de suspeita de estagnação de fonte que o RS carregou até hoje (quando finalmente se moveu).
- **O salto do RS para R$2.130,00/ton é uma leitura isolada**, a primeira depois de 14 dias de
  congelamento em R$1.860,00/ton — ainda sem segunda confirmação de que o novo patamar se
  sustenta.
- **Este é o terceiro episódio de revisão retroativa de dados de sessão em duas semanas** (11/09,
  15/09, 23/09) — desta vez com uma característica nova: a correção mudou o SINAL do movimento em
  farelo e na margem de biodiesel, não apenas a magnitude, como nos dois episódios anteriores.
- **As manchetes de notícia recentes estão disponíveis apenas como título** — nem o corpo da
  manchete "Produtor segura a soja..." (23/09) nem o de "Shrinking supplies..." (22/09) estão
  disponíveis neste dump. Não é possível citar números de fonte primária para validar nenhuma das
  duas narrativas com precisão.
- **O corte de COT `release-cftc_cot-2026-09-15` segue sendo o dado de posicionamento mais
  recente**, agora nove dias corridos depois do corte. O próximo corte (posições de 22/09,
  esperado 25-26/09) resolve essa lacuna nos próximos 1-2 dias.
- **Percentil histórico de posicionamento COT não está disponível no briefing** — toda leitura
  de "fundos comprando/vendendo" nesta série usa variação absoluta semana a semana de contratos,
  não percentil histórico.
- **O item de fila `release-nopa-2026-09-24` é mais uma repetição sem dado novo** — o mesmo
  padrão de todas as leituras anteriores desde que este monitoramento começou (paywall,
  `monthly_status` em 0,0 bool).
- **`tributario_watch.toml` sem atualização há 111 dias corridos** — pelo menos dois vetores
  (isenção PIS/Cofins do biodiesel, MP 1.358/2026) já passaram da vigência registrada sem nota
  de renovação ou expiração.
- **A previsão INMET para 24/09 é previsão meteorológica, não medição de precipitação ou
  temperatura real** — as menções a "chuva", "pancadas" e "trovoadas isoladas" são indicativas do
  boletim, não confirmação de que o evento ocorreu ou ocorrerá; a menção de geada em Passo
  Fundo/RS pela manhã tem vínculo fraco com a tese de preço de soja, já que o plantio no RS
  normalmente só começa em outubro/novembro.
- **MPOB (palma Malásia) segue com parser quebrado** — nenhum dado de produção/estoque de palma
  malaia disponível, o que impede monitorar diretamente o catalisador represado da centralização
  de exportação indonésia (Danantara).
- **Não há seção `bcba` (Argentina) neste dump** — nenhum dado direto de safra ou exportação
  argentina disponível além do que já vem consolidado pelo WASDE (edição de 11/09, 13 dias de
  idade).
- **Os forecasts estatísticos internos (bandas 7d/30d) foram gerados hoje sobre o fechamento
  corrigido de 23/09** — o viés "altista" em soja e farelo e o "baixista" em óleo (30d) refletem
  extrapolação estatística de tendência (MA20 + volatilidade + slope), não uma reavaliação
  fundamentalista; esta leitura mantém farelo em bull, soja em neutro e óleo em bear a partir da
  análise qualitativa, coerente com essas bandas mas independente delas.
- **A fila de julgamento volta a listar as revisões D+7 e D+90 da tese de 11/06 como "vencidas"**
  — o veredito de ambas já foi fechado em
  [[2026-09-17_ratio-far-soj-supera-nivel-de-abertura-da-tese-original-quarta-sessao]]; o sistema
  de fila não lê de volta os insights publicados para marcar a revisão como encerrada. Nenhuma
  ação nova é necessária sobre essas duas revisões específicas.
