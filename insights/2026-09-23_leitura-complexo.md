---
data: 2026-09-23
titulo: "Terceira sessão seguida de alta no ratio Far/Soj (84,28%, a maior desde o pico de 84,4% em 17/09) aprofunda o bull-farelo e empurra o bear-óleo a novos extremos da janela (oil share em mínima de 47,61%, spread oleo-farelo no mais negativo já visto), mas farelo e heating oil voltam a fechar 22/09 e 23/09 com abertura/máxima/mínima/volume idênticos — quinta ocorrência do mesmo padrão de dado suspeito documentado nesta série — sobre um pano de fundo de liquidez anormalmente baixa em toda a curva (2,6% a 4,8% do volume normal) que já dura cinco sessões seguidas, enquanto a soja segue neutra, comprimida num range de 0,36% e volume de apenas 3.843 contratos"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT — sessão de **2026-09-23** (quarta-feira): soja (ticker ZSX26.CBT, venc. nov/26) abertura 1.324,75, máxima 1.327,25, mínima 1.322,50, fechamento **1.326,25**, volume **3.843 contratos**; farelo (ticker ZMZ26.CBT, venc. dez/26) abertura 370,70, máxima 373,00, mínima 369,30, fechamento **372,60**, volume **2.996 contratos**; óleo (ticker ZLZ26.CBT, venc. dez/26) abertura 67,95, máxima 68,02, mínima 67,58, fechamento **67,72**, volume **2.986 contratos**. Curva futura em 23/09 — soja: nov/26 (base) 1.326,25 → jan/27 1.342,25 → mar/27 1.349,50 → mai/27 1.355,75 → jul/27 1.359,25; farelo: out/26 371,40 → dez/26 (base) 372,60 → jan/27 372,50 → mar/27 372,00 → mai/27 371,80 (leve backwardation nos meses mais distantes); óleo: out/26 67,17 → dez/26 (base) 67,72 → jan/27 67,99 → mar/27 68,20 → mai/27 68,36
  - CME CBOT — sessão de **2026-09-22** (referência de comparação, mesma fonte `cme_cbot`, dump de hoje): farelo abertura 370,70, máxima 373,00, mínima 369,30, fechamento **371,00**, volume **2.996 contratos**; heating oil (HO=F) abertura 4,7026, máxima 4,7274, mínima 4,6688, fechamento 4,6812, volume **2.189 contratos** — **farelo e heating oil de 22/09 têm abertura, máxima, mínima E volume idênticos, byte a byte, aos de 23/09** (só o fechamento difere em cada par); soja e óleo NÃO exibem essa duplicação — não há sequer uma linha bruta de `cme_cbot` para soja/óleo em 22/09 neste dump, e os fechamentos de 23/09 (1.326,25 e 67,72) diferem de forma plausível dos fechamentos indicados via `indicators` para 22/09 (1.325,00 e 67,88) (ver Visão geral e Honestidade)
  - CME NYMEX heating oil (HO=F) — **2026-09-23**: abertura 4,7026, máxima 4,7274, mínima 4,6688, fechamento **4,6920** USD/galão, volume **2.189 contratos** — mesma anomalia de duplicação de abertura/máxima/mínima/volume frente a 22/09 descrita acima, quinta ocorrência documentada do padrão (ver Honestidade e [[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]])
  - Indicadores sintéticos internos (`indicators`) — **2026-09-23**: crush margin **US$2,3839/bushel** (farelo 372,60 + óleo 67,72 − soja 1.326,25); ratio Far/Soj **84,28%**; oil share **47,61%**; oil-meal spread **-0,748 USD/bushel**; ISF (Índice de Sobra de Farelo) 60/100; ISO (Índice de Suporte do Óleo) 80/100; paridade BR da soja **R$149,59/saca** (CBOT 1.326,25 × USD/BRL 5,1161, sem basis, PTAX ainda a de 22/09 — ver Honestidade); margem de biodiesel US **US$1,978/galão** (receita 7,857 = HO 4,69 + 1,5×RIN 2,11; custo 5,879 = óleo 5,079 + industrial 0,80). Comparação **2026-09-22**: crush margin 2,3788; ratio 84,00%; oil share 47,78%; oil-meal spread -0,6952; margem biodiesel 1,9552; paridade BR 149,45. Série completa dos últimos dias — ratio Far/Soj: 16/09 83,06% → 17/09 84,40% → 18/09 82,53% → 21/09 83,22% → 22/09 84,00% → 23/09 **84,28%**; oil share: 17/09 48,22% → 18/09 48,75% → 21/09 48,31% → 22/09 47,78% → 23/09 **47,61%** (mínima da janela); margem biodiesel: 17/09 2,2927 → 18/09 2,3063 → 21/09 2,0908 → 22/09 1,9552 → 23/09 **1,978** (pequeno repique dentro de tendência de queda de -13,7% desde o pico de 18/09)
  - BCB PTAX — última publicação ainda **2026-09-22**: USD/BRL **5,1161** (alta de +0,09% frente aos 5,1117 de 21/09), EUR/BRL 5,8487, Selic diária 0,050788% a.a. (séries SGS 1, 21619, 11); sem PTAX de 23/09 neste dump (lag normal de publicação, ver Honestidade)
  - NAG físico BR (`nag_fisico`) — última atualização ainda **2026-09-22** (sem ponto novo de 23/09, lag normal de um dia): farelo Rondonópolis/MT (BCSP) **R$2.200,00/ton, var 0,0% frente a 21/09 — segunda leitura seguida no novo patamar, confirmando que o salto de +8,37% (de R$2.030 em 18/09 para R$2.200 em 21/09) se sustentou**; farelo Mato Grosso/IMEA R$1.982,28/ton (var 0,0%, mesmo valor desde 18/09); farelo média Rio Grande do Sul (Clicmercado) R$1.860,00/ton (var 0,0%, valor idêntico de 08/09 a 22/09 — **14 dias corridos**, ver Honestidade); soja Paraná interior (CEPEA/ESALQ via NAG) R$155,50/saca (+0,15% frente a 21/09); prêmio export farelo Paranaguá 0,12 USD/short_ton (congelado desde 08/09, 14 dias corridos); prêmio export óleo Paranaguá 0,1 cts/lb (mesmo congelamento)
  - CEPEA/ESALQ Soja Paranaguá (via NAG) — **2026-09-22**: R$161,93/saca (+0,25% frente a 21/09); spread Paranaguá−Paraná interior de R$6,43/saca (161,93 − 155,50), levemente mais largo que os R$6,26 de 21/09 — sinal marginal de demanda de exportação um pouco mais firme
  - CEPEA RSS — contagem de itens sobe para 106 em 22/09 e 23/09 (de 103 em 20-21/09), mas sem novo corpo de headline relevante capturado; a última manchete com corpo de texto ainda é a de 18/09 ("SOJA/CEPEA: Participação do farelo na 'crush margin' aumenta no BR e nos EUA")
  - Notícias Agrícolas/Canal Rural/Farm Progress (RSS) — headline de **2026-09-22**, DADO NOVO nesta leitura: "Shrinking supplies keep prospects for $14 soybeans on table" (Farm Progress) — narrativa de aperto de oferta americana sustentando um cenário de preço-alvo alto para a soja, sem corpo de texto disponível neste dump (ver Soja e Honestidade); headline de 21/09 (Canal Rural) "Preços de soja sobem de R$1 a R$2 por saca nas praças do Brasil" segue como a mais recente do lado brasileiro; item de contagem de 23/09 registra 160 itens lidos e 5 mantidos, mas sem o texto desses itens
  - CFTC COT Managed Money — corte de **2026-09-15** (sem corte novo; próximo corte é o de posições de 22/09, esperado por volta de 25-26/09): farelo net long 183.111 contratos (+16,12% vs 08/09); óleo net long 101.480 (+10,65%); soja net long 241.501 (-6,13%)
  - USDA Crop Progress — corte de **2026-09-20** (o mais recente, chegou desde a leitura de 22/09): 12% excelente / 46% boa (G/E 58%, estável frente ao corte anterior), 10% pobre (+1p.p. frente aos 9% de 13/09), colheita 2025/26 em **12% concluída** (dobrou frente aos 6% de 13/09, ritmo normal de avanço de calendário)
  - USDA WASDE — edição de **2026-09-11** (sem edição nova): farelo Argentina 2026/27 exportação 2,99 mi t; farelo Brasil 2025/26 exportação 0,2 mi t
  - NOPA — item de fila `release-nopa-2026-09-23`: `monthly_status` em 0,0 bool (paywall, sem dado novo, mesmo padrão de todas as leituras anteriores)
  - ABIOVE projeções mensais — balanços out-dez/2026, sem revisão nesta janela
  - NOAA CPC ENSO — El Niño Advisory, inalterado (carimbo 2026-09-23)
  - MPOB — carimbo 2026-09-23, parser sem números extraídos (mesma barreira há semanas)
  - BCBA (Argentina) — carimbo mais recente ainda 2026-09-09, scraper acessa a página mas não encontra links de relatório
  - INMET — previsão para **2026-09-23 (HOJE)**: Cascavel/PR 25°C/9°C "poucas nuvens"; Maringá/PR 22°C/13°C "muitas nuvens"; Passo Fundo/RS 18°C/5°C com **menção de geada** pela manhã; núcleo de Mato Grosso — Cuiabá 31°C/22°C, Sinop 36°C/24°C, Sorriso 36°C/25°C, Lucas do Rio Verde 36°C/23°C, todos "muitas nuvens" com chuva isolada/pancadas; Rio Verde/GO 32°C/22°C com pancadas de chuva
  - system/tributario_watch.toml (lido como referência, não editado) — `atualizado_em` 2026-06-05 em todos os 10 eventos catalogados, **110 dias corridos** sem revisão humana frente a hoje (23/09)
  - Forecasts estatísticos internos (bandas 7d/30d) — geração de **2026-09-23**, sobre o fechamento de hoje, alvos 30/09 e 23/10: viés "altista" em soja e farelo nos dois horizontes; óleo muda de "altista" (30d, gerado em 22/09) para **"baixista"** (30d, gerado em 23/09) — primeira vez que a banda de 30 dias do óleo vira baixista nesta série (extrapolação estatística, não fundamentalista — ver Honestidade)
  - Fila de julgamento — 2026-09-23, 7 itens: `alerta-quebra_resistencia-soja_cbot-2026-09-23`, `alerta-quebra_suporte-oleo_cbot-2026-09-23`, `alerta-quebra_resistencia-farelo_cbot-2026-09-23`, `alerta-quebra_suporte-complexo_soja-2026-09-23`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`, `release-nopa-2026-09-23`
  - Cruza com [[2026-09-22_leitura-complexo]] (leitura de ontem, primeira a documentar a duplicação de OHLC em farelo+HO=F), [[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]] (padrão de revisão do HO=F documentado em três ocorrências anteriores, hoje na quinta ocorrência), [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (tese original do ratio, nível de abertura 81,4%) e [[2026-09-17_ratio-far-soj-supera-nivel-de-abertura-da-tese-original-quarta-sessao]] (veredito de invalidação técnica da tese baixista de junho, D+7 e D+90 já fechados)
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
farelo vira o motor de rentabilidade do esmagador). Hoje, **84,28%** (indicators, 2026-09-23),
o complexo segue na zona neutra, mas cada vez mais perto do teto "apertado" — a apenas 2,72
pontos percentuais de distância, a menor desta série de leituras diárias, e a terceira alta
consecutiva do ratio (82,53% em 18/09 → 83,22% em 21/09 → 84,00% em 22/09 → 84,28% hoje).

**O que muda hoje, quarta-feira 23/09, é duplo: o movimento de preço em si (farelo mais
forte, óleo mais fraco, ambos em níveis mais extremos que ontem) e uma nova confirmação de
que o problema de qualidade de dado identificado ontem não foi pontual, e sim um padrão
recorrente que já vai na quinta ocorrência.**

**Achado 1 — o ratio Far/Soj sobe pela terceira sessão seguida e se aproxima do pico local de
17/09.** O fechamento de farelo de hoje, 372,60 USD/short_ton, é uma alta de +0,43% frente
aos 371,00 de ontem; o de soja, 1.326,25 USD/bushel, subiu apenas +0,09% frente aos 1.325,00;
e o de óleo, 67,72 USD cts/lb, caiu -0,24% frente aos 67,88. O resultado líquido é um ratio
Far/Soj de 84,28% — ainda abaixo do pico local de 84,40% visto em 17/09, mas a trajetória das
últimas três sessões (83,22% → 84,00% → 84,28%) é uma escalada consistente, sem nenhuma
sessão de recuo no meio do caminho. Ao mesmo tempo, o oil share caiu para **47,61%**, uma
nova mínima desta janela de leituras (a mínima anterior era 47,78%, de ontem), e o oil-meal
spread (a diferença de valor por bushel entre óleo e farelo) ficou ainda mais negativo,
em -0,748 USD/bushel (de -0,6952 ontem) — o farelo nunca esteve tão à frente do óleo, em
termos relativos, nesta série de leituras.

**Achado 2 — farelo e heating oil voltam a fechar dois dias seguidos com abertura, máxima,
mínima e volume idênticos, byte a byte; apenas o fechamento muda.** A linha bruta do farelo
(`cme_cbot`, ticker ZMZ26.CBT) mostra abertura 370,70, máxima 373,00, mínima 369,30 e volume
2.996 contratos tanto em 22/09 quanto em 23/09 — só os fechamentos diferem (371,00 → 372,60).
O heating oil (HO=F) repete o mesmo padrão: abertura 4,7026, máxima 4,7274, mínima 4,6688 e
volume 2.189 contratos idênticos nos dois dias, só o fechamento varia (4,6812 → 4,6920). Essa
é a mesma anomalia documentada pela primeira vez em três ocorrências isoladas do HO=F (ver
[[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]]) e, ontem, estendida ao farelo em
[[2026-09-22_leitura-complexo]] — hoje é a **quinta ocorrência** do mesmo padrão, e a segunda
vez seguida em que farelo e HO=F são afetados juntos. O mecanismo mais provável continua
sendo o mesmo: o dado capturado não representa duas sessões de pregão plenas e distintas, mas
sim a mesma "foto" de faixa de negociação sendo relida com apenas o campo de cotação corrente
(fechamento) atualizando — o que é estatisticamente incompatível com dois pregões genuínos e
independentes de contratos líquidos. É importante notar, porém, uma diferença relevante frente
a ontem: **soja e óleo não exibem esse padrão** — não há sequer uma linha bruta de `cme_cbot`
para esses dois tickers em 22/09 neste dump (só sobrevive o valor já calculado via
`indicators`), e o fechamento de óleo de hoje (67,72) é plausivelmente distinto do de ontem
(67,88), sem qualquer sinal de duplicação. Isso sugere que o problema de captura é específico
de como o sistema lê ZMZ26.CBT e HO=F, não um problema generalizado do pipeline inteiro.

**Achado 3 — a liquidez de toda a curva segue anormalmente baixa, agora pela quinta sessão
seguida.** Os volumes de hoje — soja 3.843, farelo 2.996, óleo 2.986, heating oil 2.189 —
representam **3,6%, 2,6%, 4,5% e 4,8%**, respectivamente, do volume da última sessão
plenamente líquida já registrada nesta série de leituras (18/09: 108.222, 113.303, 67.046 e
45.315 contratos, ver [[2026-09-22_leitura-complexo]]). Diferente do achado 2 (que afeta só
farelo e HO=F), este padrão de baixa liquidez atinge os quatro contratos por igual e já dura
desde pelo menos 21/09 — cinco sessões seguidas sem uma única leitura de volume saudável. Isso
não invalida os níveis técnicos (os fechamentos de hoje são reais o suficiente para os
gatilhos da fila continuarem corretos em termos de onde o preço está), mas reduz a convicção
com que qualquer leitura de "confirmação de tendência por volume" deveria ser tratada nesta
janela inteira, não apenas no dia de hoje.

Esses três achados, juntos, não mudam a direção das teses que já vinham se consolidando —
farelo mais forte, óleo mais fraco, soja no meio — mas justificam manter os três vieses já
estabelecidos (bull-farelo, neutral-soja, bear-oleo_soja) com uma leitura de convicção
direcional reforçada (o movimento de hoje é o terceiro dia seguido na mesma direção, não um
evento isolado) combinada com uma leitura de confiança estatística reduzida (baixa liquidez
persistente + duplicação de dado em dois dos quatro contratos).

**Leitura de uma linha**: o pivô do complexo continua sendo o ratio Far/Soj, hoje em 84,28% —
a maior leitura desde o pico de 84,40% de 17/09, e a apenas 2,72 pontos percentuais do
território "apertado" (87%). Maior convicção: bull-farelo, agora sustentado por três sessões
consecutivas de alta do ratio e por uma segunda confirmação física de aperto doméstico
(Rondonópolis/MT mantendo o patamar de R$2.200/ton). Confiança geral na magnitude exata do
movimento de hoje especificamente (não na tendência das últimas semanas) segue **reduzida**
pela combinação de baixa liquidez generalizada e pela duplicação de dado em farelo/HO=F — o
dono deveria continuar tratando os fechamentos de farelo e HO=F com o mesmo ceticismo
metodológico já aplicado nas duas leituras anteriores, mas pode depositar mais confiança nos
fechamentos de soja e óleo, que não exibem o mesmo padrão de duplicação hoje.

## Soja

**Viés: neutro, mantido — terceira sessão seguida de variação mínima (+0,09%), comprimida num
range intradiário de apenas 0,36% sobre o menor volume desta janela (3.843 contratos), com um
contraponto altista qualitativo novo do lado americano e um pano de fundo técnico e sazonal
que segue sem definição clara de direção.**

O que sustenta a tese (lado altista):

- **A soja segue folgadamente acima da resistência de referência de 1.180,00** (fila
  `alerta-quebra_resistencia-soja_cbot-2026-09-23`: fechamento 1.326,25 vs. nível 1.180,00),
  uma folga de **+12,39%**, a maior desta série recente, e sem qualquer sinal de risco de
  reversão técnica no curto prazo.
- **A curva futura permanece em contango regular, com inclinação praticamente idêntica à de
  ontem**: nov/26 (base) 1.326,25 → jan/27 1.342,25 → mar/27 1.349,50 → mai/27 1.355,75 →
  jul/27 1.359,25 (CME CBOT, 23/09) — o mercado a termo segue precificando preços mais altos à
  frente, sem sinal de reversão estrutural embutido na curva.
- **Manchete nova de Farm Progress (22/09, via `noticias_rss`): "Shrinking supplies keep
  prospects for $14 soybeans on table"** — uma narrativa de aperto de oferta americana
  sustentando um cenário de preço-alvo elevado (US$14/bushel, bem acima do fechamento atual de
  US$13,26/bushel equivalente a 1.326,25 cts). O corpo da notícia não está disponível neste
  sistema (ver Honestidade), então não é possível validar a tese de "shrinking supplies" com um
  número de fonte primária (estoque, produção revisada), mas a direção do título é coerente com
  o viés altista de curto prazo do forecast estatístico interno (7d e 30d, ambos "altista").
- **A curva de crop progress trouxe seu primeiro corte novo em duas semanas** (ver risco
  abaixo para a leitura completa): condição estável em G/E 58% é, isoladamente, um dado neutro
  a levemente positivo — mostra que a safra americana não está se deteriorando na reta final do
  ciclo, apesar da colheita já avançando.

**O que invalida / risco:**

- **O corte de USDA Crop Progress de 20/09, o primeiro em duas semanas, trouxe um sinal misto,
  não puramente altista.** Excelente e boa condição ficaram estáveis (12% e 46%, G/E 58%
  inalterado frente a 13/09), mas a categoria "pobre" subiu de 9% para 10% (+1 p.p.) — uma
  piora marginal na cauda inferior da distribuição de qualidade — e a colheita avançou de 6%
  para 12% da área, dobrando em uma semana, um ritmo de calendário normal que, em si, não é
  nem altista nem baixista, mas que encurta a janela em que qualquer notícia de dano de lavoura
  ainda pode se materializar em preço (quanto mais colhido, menos exposição a risco climático
  remanescente).
- **O COT de 15/09, ainda o mais recente, mostrou os fundos reduzindo net long em soja em
  -6,13%** (de 257.258 para 241.501 contratos), com short subindo — o único das três pernas do
  complexo em que o COT mais recente aponta para *menos* convicção compradora dos fundos, não
  mais. Oito dias depois desse corte, ainda não há um novo dado de posicionamento (próximo
  corte, de posições de 22/09, esperado por volta de 25-26/09) para dizer se esse movimento se
  acentuou ou reverteu.
- **O volume de hoje (3.843 contratos) é apenas 3,6% do volume da última sessão plena
  documentada (108.222, em 18/09)**, e o range intradiário (1.322,50-1.327,25, 0,36% de
  amplitude) é o mais estreito de toda a série recente — o fechamento de +0,09% de hoje carrega
  muito pouca informação nova sobre a real intenção do mercado (ver Visão geral e Honestidade).
- **Nível técnico a vigiar:** um fechamento de volta abaixo de 1.180 desfaria formalmente o
  rompimento; com a folga em +12,39%, esse cenário segue distante.

**Leitura operacional:** com preço praticamente estável pela terceira sessão seguida e volume
no menor patamar já visto nesta série, não há gatilho técnico novo para agir hoje — o range de
apenas 0,36% intradiário é estreito demais para servir de referência tática em qualquer
direção. Para quem está comprado, a folga técnica de +12,39% acima da resistência de 1.180 e o
contango da curva seguem sustentando a posição estrutural, mas o par de contrapontos (COT já
mostrando fundos mais cautelosos desde 15/09 e a piora marginal na categoria "pobre" do crop
progress) sugere manter o dimensionamento atual sem reforçar apenas com base no fechamento de
hoje. Para quem opera vendido, o range de hoje (1.322,50-1.327,25) é estreito demais para
qualquer leitura de rompimento intradiário ter significado nesse volume — vale esperar a
normalização da liquidez, e monitorar de perto o próximo corte de COT (25-26/09), que é o
primeiro capaz de confirmar se a redução de net long dos fundos vista em 15/09 se tornou uma
tendência ou foi um ajuste pontual.

## Farelo

**Viés: bull, reforçado — terceira sessão consecutiva de alta do ratio Far/Soj, aproximando-se
do pico local de 17/09, com uma segunda confirmação física de que o aperto doméstico em
Rondonópolis se sustentou, mas a confiança na magnitude exata do movimento de hoje segue
reduzida pela duplicação de OHLC/volume frente a ontem (ver Visão geral).**

O que sustenta a tese:

- **O ratio Far/Soj fechou em 84,28% hoje** (indicators), a terceira alta seguida (83,22% em
  21/09 → 84,00% em 22/09 → 84,28% hoje), a maior leitura desde o pico local de 84,40% de
  17/09 e a distância mais curta já registrada desta série até o território "apertado" (87%):
  apenas **2,72 pontos percentuais**. Isso amplia a distância acima do nível de abertura da
  tese baixista original de 11/06/2026 (81,4%, [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]])
  para **+2,88 pontos percentuais** — o veredito de invalidação técnica dessa tese, fechado em
  [[2026-09-17_ratio-far-soj-supera-nivel-de-abertura-da-tese-original-quarta-sessao]], segue de
  pé e, a cada sessão em que o ratio se mantém acima de 81,4%, fica mais distante de qualquer
  risco de reversão para o cenário original — trata
  `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` e
  `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`: ambas seguem aparecendo
  como "vencidas" na fila porque o sistema não lê de volta os insights já publicados, mas o
  veredito de ambas já está fechado desde 17/09; resta em aberto apenas a revisão de D+180,
  programada para 2026-12-08.
- **O físico de farelo em Rondonópolis/MT (fonte BCSP, via NAG) segue em R$2.200,00/ton pela
  segunda leitura seguida (21/09 e 22/09, var 0,0% entre as duas)** — a confirmação de que o
  salto de +8,37% visto em 21/09 (de R$2.030,00 para R$2.200,00) não foi um evento de um único
  dia, mas um novo patamar que se sustentou por, no mínimo, mais uma leitura. Combinado com o
  salto de +3,68% do IMEA em 18/09, são duas praças físicas distintas mostrando aperto
  doméstico em dias próximos — evidência mais consistente de um movimento real do que qualquer
  leitura isolada seria.
- **O oil share caiu para 47,61% hoje** (de 47,78% ontem, 48,75% em 18/09) — uma nova mínima
  desta janela de leituras, o espelho direto do farelo ganhando protagonismo relativo dentro do
  valor total gerado pelo crush.
- **O oil-meal spread ficou ainda mais negativo, em -0,748 USD/bushel** (de -0,6952 ontem,
  -0,385 em 18/09) — a maior distância já registrada nesta série entre o valor do farelo e o
  valor do óleo, em termos de bushel-equivalente.
- **O farelo segue folgadamente acima da resistência histórica de 325,00** (fila
  `alerta-quebra_resistencia-farelo_cbot-2026-09-23`: 372,60 vs. 325,00), folga de +14,65%, a
  maior desta série.
- **O COT de 15/09 mostrou os fundos com net long em farelo em 183.111 contratos (+16,12%
  frente a 08/09)** — ainda o dado de posicionamento mais recente, mas a maior variação
  percentual de toda a série de posicionamento disponível.
- **A trajetória sazonal da ABIOVE para o Brasil continua apontando para alívio de oferta
  doméstica de farelo à frente**, sem revisão nesta janela: produção projetada caindo de 2.143
  mil t (out/26) para 1.978 (nov/26) e 1.659 mil t (dez/26); exportação de 850 para 800 e 700
  mil t no mesmo período.

**O que invalida / risco:**

- **A sessão de futuro de hoje repete a anomalia de dado descrita na Visão geral**: abertura
  (370,70), máxima (373,00), mínima (369,30) e volume (2.996 contratos) idênticos, byte a byte,
  aos de 22/09 — só o fechamento mudou (371,00 → 372,60, +0,43%). Isso significa que a
  "confirmação" de hoje de que o ratio segue subindo se apoia num par de fechamentos de baixa
  liquidez (2.996 contratos, apenas 2,6% do volume de 18/09), não numa sessão plena — o nível
  técnico está confirmado, mas a convicção estatística por trás dele é menor do que parece, e
  esta é a quinta vez que esse padrão específico se repete (ver [[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]]).
- **A terceira praça física monitorada (RS, fonte Clicmercado) segue completamente parada em
  R$1.860,00/ton por 14 dias corridos, de 08/09 a 22/09** — sem nenhum ponto de dado novo desde
  então, o que reforça a suspeita, já registrada em leituras anteriores, de que essa fonte
  específica simplesmente não está atualizando (ver Honestidade). Sem essa terceira praça em
  movimento, o quadro físico brasileiro de farelo tem confirmação de 2 de 3 fontes, não de 3 de
  3.
- **O prêmio de exportação de farelo em Paranaguá segue congelado em 0,12 USD/short_ton há 14
  dias corridos** (desde 08/09) — se o aperto físico doméstico fosse amplo e sustentado, seria
  razoável esperar, eventualmente, algum reflexo no canal de exportação FOB; essa confirmação
  ainda não apareceu.
- **A curva futura de farelo mostra uma leve inversão (backwardation) nos meses mais distantes**:
  jan/27 372,50 → mar/27 372,00 → mai/27 371,80 — uma diferença pequena (-0,19% entre jan/27 e
  mai/27), mas que sugere que o mercado a termo não está precificando um aperto estrutural que
  se estenda indefinidamente; é consistente com a trajetória sazonal de alívio de oferta da
  ABIOVE citada acima (oferta brasileira de farelo caindo ao longo do 4º trimestre).
- **Os índices sintéticos ISF e ISO seguem travados em 60/100 e 80/100**, sem reação a mais de
  dez dias de oscilação do ratio e do crush margin — o contraponto de sempre nesta série: esses
  índices reagem a mudanças de regime estrutural, não a movimentos de curto prazo, então sua
  inércia não deve ser lida como desconfirmação da tese.

**Leitura operacional:** a tendência estrutural de farelo mais forte segue intacta e ganhou
hoje seu terceiro reforço consecutivo (ratio em alta pela terceira sessão, segunda confirmação
física em Rondonópolis), o suficiente para manter o viés bull-farelo com convicção reforçada
frente a ontem. Mas a repetição, pela quinta vez, da anomalia de volume/OHLC no futuro pede a
mesma cautela de sempre em dias de baixa liquidez: para quem está comprado em farelo ou no
spread Far/Soj comprado, o gatilho mais sólido continua sendo uma sessão de volume normalizado
confirmando a continuidade acima de 84%, ou uma terceira leitura de físico (IMEA ou
Rondonópolis) que mostre o novo patamar se sustentando ainda mais. Para quem está vendido, o
nível técnico (372,60, folga de +14,65% sobre a resistência) e o calendário sazonal da ABIOVE
seguem desfavoráveis à tese de queda; a única fresta de dúvida é a leve inversão da curva
futura nos meses mais distantes, que sugere que o mercado a termo já espera alguma normalização
de oferta ao longo do 4º trimestre — um argumento para não perseguir o movimento com posição
adicional no vencimento mais distante, mesmo mantendo convicção no front-month.

## Óleo

**Viés: bear, reforçado — quarta sessão seguida abaixo do suporte técnico, com o oil share em
mínima da janela e o oil-meal spread no ponto mais negativo já registrado, mas o cenário segue
sujeito à mesma reserva sobre liquidez anormalmente baixa que afeta todo o complexo.**

O que sustenta a tese:

- **Óleo fechou em 67,72 USD cts/lb hoje**, uma queda de -0,24% frente aos 67,88 de ontem,
  aprofundando a distância abaixo do suporte de referência de 72,00 (fila
  `alerta-quebra_suporte-oleo_cbot-2026-09-23`: -5,94%, a maior desta série — a trajetória de
  distância vem piorando sessão a sessão: -4,38% em 21/09 → -5,72% em 22/09 → -5,94% hoje).
- **O oil share caiu para 47,61% hoje, uma nova mínima desta janela** (de 47,78% ontem, 48,75%
  em 18/09) — o óleo perde, progressivamente, participação no valor total gerado pelo crush.
- **O oil-meal spread atingiu -0,748 USD/bushel, o ponto mais negativo já registrado nesta
  série** — o óleo nunca esteve tão atrás do farelo, em termos de valor por bushel-equivalente,
  desde que este indicador começou a ser acompanhado de perto.
- **O ISO (Índice de Suporte do Óleo) segue em 80/100**, sem melhora — os índices compostos
  continuam sem sinalizar qualquer reversão de regime a favor do óleo.
- **O forecast estatístico interno de 30 dias virou de "altista" (gerado em 22/09) para
  "baixista" (gerado em 23/09)** — a primeira vez nesta série que essa banda estatística de
  médio prazo aponta para baixo em vez de para cima ou lateral; é extrapolação de tendência
  (MA20 + volatilidade + slope), não uma reavaliação fundamentalista, mas é coerente com a
  deterioração progressiva do oil share e do oil-meal spread descrita acima.
- **A lente fiscal brasileira segue estruturalmente desfavorável, sem mudança hoje**: a MP
  1.363/2026 (subvenção ao diesel fóssil, R$1,12/L, vigente até 31/12/2026) segue plenamente
  vigente, barateando o fóssil no mix B15 e reduzindo a competitividade do biodiesel; a isenção
  de PIS/Cofins do biodiesel na mistura está **54 dias corridos vencida** (vigência registrada
  até 31/07/2026) sem sinal de renovação — ver seção Lente fiscal/regulatória BR.

**O que sustenta um contraponto — e por que a leitura de hoje pede a mesma cautela de ontem:**

- **A margem de biodiesel americana de hoje ficou em US$1,978/galão, uma alta de +1,17% frente
  aos 1,9552 de ontem** — um pequeno repique dentro de uma tendência de queda mais ampla (de
  2,2927 em 17/09 para 1,978 hoje, uma queda acumulada de -13,72% em quatro sessões). Esse
  número se apoia diretamente no fechamento de HO=F de hoje (4,6920 USD/galão), que **repete a
  mesma anomalia de duplicação de OHLC/volume frente a 22/09 já descrita na Visão geral** —
  abertura (4,7026), máxima (4,7274), mínima (4,6688) e volume (2.189 contratos) idênticos aos
  de ontem, só o fechamento variando. **Como na leitura de ontem, nenhuma conclusão sobre a
  "força" ou "convicção" da sessão de HO=F de hoje deveria ser tirada apenas do volume ou do
  range** — mas, diferente de ontem, o próprio valor do fechamento (a única variável que
  realmente muda entre os dois dias) mostra uma pequena recuperação, não uma nova perna de
  queda, então o repique de margem é, na melhor das hipóteses, um dado provisório mas
  direcionalmente plausível.
- **O RIN D4 (crédito de biocombustível renovável americano) permanece constante na fórmula
  interna** — nenhuma variação real de política regulatória americana explicaria uma mudança na
  margem hoje.
- **A curva futura de médio prazo segue em contango regular**: out/26 67,17 → dez/26 (base)
  67,72 → jan/27 67,99 → mar/27 68,20 → mai/27 68,36 — sem sinal de reprecificação estrutural
  de curto prazo, o que contrasta com a leve inversão vista na curva do farelo.
- **Catalisadores de alta represados, ainda não correntes**: B16 (elevação da mistura de
  biodiesel para 16%, ~436 mil toneladas de demanda adicional potencial de óleo) segue
  "adiado", com resultado esperado por volta de novembro/2026; a centralização da exportação de
  palma pela Indonésia via Danantara, que tinha alvo de assunção plena em 01/09/2026, já soma
  **22 dias** de atraso sem confirmação — ambos seguem como upside represado, não corrente, para
  o óleo (ver Lente fiscal/regulatória BR).

**Leitura operacional:** o quadro técnico (abaixo do suporte de 72,00 pela quarta sessão
seguida, oil share em mínima da janela, oil-meal spread no ponto mais negativo já visto) e a
lente fiscal seguem favoráveis ao lado vendido direcional, e a virada da banda estatística de
30 dias para "baixista" reforça esse quadro, mesmo sem valor fundamentalista próprio. Para quem
está vendido, o nível técnico e o calendário fiscal (MP 1.363 vigente até dezembro, isenção
PIS/Cofins já 54 dias vencida) seguem sustentando a posição, agora com um argumento técnico
adicional (oil share e oil-meal spread em extremos da janela) que não depende do HO=F suspeito.
Para quem está comprado ou avalia entrar, o argumento mais forte contra a tese bear seguiria
sendo uma confirmação de HO=F com volume saudável mostrando a margem de biodiesel realmente
subindo de forma consistente — o que este dump não entrega hoje, ainda que o pequeno repique de
+1,17% seja, no mínimo, um sinal de que a queda não está se acelerando. Para quem opera o
spread farelo-óleo dentro do crush, o oil-meal spread fechou em -0,748 USD/bushel, o ponto mais
extremo já registrado nesta série — um nível que merece atenção como possível zona de
mean-reversion, mas sem qualquer sinal técnico de reversão ainda presente.

## Spreads e crush (leitura de complexo)

O ratio Far/Soj fechou em **84,28%** hoje, a terceira alta consecutiva (83,22% → 84,00% →
84,28%, de 21 a 23/09) e a maior leitura desde o pico local de 84,40% em 17/09 — dentro da zona
neutra (80-87%), mas a apenas **2,72 pontos percentuais** do teto "apertado" (87%) e a **4,28
pontos** do piso "abundante" (80%), a menor distância ao teto já registrada nesta série de
leituras diárias. O oil share, em **47,61%**, mostra o óleo respondendo por menos da metade do
valor gerado no esmagamento pela sétima sessão seguida com esse dado disponível, numa trajetória
de queda quase monotônica desde o pico local de 48,75% em 18/09 (48,75% → 48,31% → 47,78% →
47,61%). O crush margin, em **US$2,3839/bushel**, segue abaixo do piso de referência de US$2,50
monitorado pela fila (`alerta-quebra_suporte-complexo_soja-2026-09-23`, distância de -4,64%),
com uma leve recuperação frente aos 2,3788 de ontem (+0,21%), mas ainda distante do piso e sem
tendência clara de retorno — desde 18/09, o crush margin oscilou entre 2,3584 e 2,3983, um
intervalo estreito que sugere estabilização abaixo do nível de referência, não uma recuperação
em curso.

Os dois índices compostos por contagem de condições — ISF (60/100) e ISO (80/100) — seguem
travados no mesmo patamar desde 11/09, agora por mais de doze dias corridos sem qualquer reação,
apesar de o ratio e o oil share terem se movido de forma expressiva e consistente nesse período
— o lembrete de sempre nesta série de que esses índices específicos reagem a mudanças de regime
estrutural, não a oscilações de curto e médio prazo dentro da mesma faixa.

O que muda hoje, sem alterar a leitura direcional de nenhuma dessas três métricas, é que a
confiança na magnitude exata do movimento de farelo (e, por extensão, do ratio e do oil-meal
spread, que dependem do fechamento de farelo) segue reduzida pela quinta ocorrência do padrão
de duplicação de OHLC — mas a direção do movimento (farelo mais forte, óleo mais fraco) já foi
confirmada de forma consistente em três sessões seguidas, o que reduz o peso desse problema de
qualidade de dado na leitura direcional, mesmo mantendo cautela sobre a magnitude precisa. A
segunda confirmação física do lado do farelo (Rondonópolis segurando o patamar de R$2.200 por
uma segunda leitura) é, hoje como ontem, o dado mais sólido de todo o conjunto — vem de uma
fonte de mercado físico brasileiro, não do futuro de baixa liquidez em Chicago.

O COT de 15/09, ainda o dado de posicionamento mais recente oito dias depois, retrata os fundos
ampliando net long em farelo (+16,12%) e óleo (+10,65%) e reduzindo em soja (-6,13%) — o próximo
corte (posições de 22/09, esperado por volta de 25-26/09) é o primeiro capaz de dizer se os
mesmos fundos já realizaram lucro nas correções da semana passada ou se ampliaram ainda mais as
posições de farelo e óleo diante do quadro físico e fiscal descrito nesta leitura, e será
particularmente relevante para testar se a leitura de óleo (fundos comprados, mas preço caindo)
já começou a se resolver via liquidação de posição.

## Lente fiscal/regulatória BR

Antes de fechar qualquer tese de preço BR, os vetores tributários/regulatórios vivos que pesam
no complexo — todos do `system/tributario_watch.toml`, cujo carimbo mais recente
(`atualizado_em`) em todos os 10 eventos catalogados é 2026-06-05, ou seja, **110 dias corridos
sem revisão humana** frente a hoje (23/09):

- **MP 1.363/2026** (id `MP-1363-2026`, subvenção diesel fóssil R$1,12/L, vigente até
  31/12/2026): barateia o diesel fóssil no mix B15 (mistura obrigatória de 15% de biodiesel),
  reduzindo a competitividade relativa do biodiesel e a demanda doméstica por óleo de soja —
  vetor estrutural de baixa para óleo, plenamente vigente, sem mudança de status.
- **B16 (id `B16-CNPE-2026`, elevação da mistura obrigatória de biodiesel para 16%)** segue
  "adiado", resultado esperado por volta de novembro/2026. Upside represado (~436 mil toneladas
  de demanda potencial adicional de óleo), não corrente.
- **Isenção de PIS/Cofins do biodiesel na mistura** (id `PISCOFINS-BIODIESEL-ISENCAO`):
  vigência registrada até 31/07/2026 — já **54 dias corridos vencida** frente a 23/09/2026, sem
  registro de prorrogação ou expiração. Cada dia adicional sem notícia de renovação aumenta a
  incerteza de planejamento tributário do setor de biodiesel, um vetor de custo indireto sobre a
  demanda por óleo.
- **MP 1.358/2026** (subvenção gasolina R$0,89/L): vigência registrada até 11/07/2026, agora
  **74 dias corridos vencida**.
- **STJ REsp 2.165.276** (id `STJ-RESP-2165276`, crédito de PIS/Cofins sobre soja em biodiesel,
  direção "alta" para soja/óleo): sem novidade nesta janela.
- **EPA RFS 2026/2027** (id `EPA-RFS-2026-2027`, mandato de biocombustível americano, direção
  "alta" para óleo): sustenta o RIN D4, estável, e o RIN permanece constante na fórmula interna
  de margem de biodiesel usada por este sistema.
- **Crédito 45Z** (id `45Z-CLEAN-FUEL`, em tramitação, direção "mista"): sem novidade.
- **Indonésia — Danantara** (id `DANANTARA-INDONESIA`) e **levy de exportação PMK 9/2026** (id
  `INDONESIA-LEVY-PMK9`): a assunção plena da centralização da exportação de palma pela
  Indonésia tinha alvo 01/09/2026 — já se passaram **22 dias** sem confirmação. Catalisador de
  alta represado para óleo (via substituição com palma) — ainda sem dado de MPOB disponível para
  monitorar diretamente (parser continua quebrado, ver Honestidade).
- **Indonésia B50** (id `INDONESIA-B50`, monitorando, direção "alta"): sem novidade.

Nenhum desses vetores muda a leitura de preço de hoje isoladamente — mas, em conjunto, eles
seguem reforçando a mesma assimetria já descrita em leituras anteriores: o mercado interno
brasileiro tem múltiplos desincentivos correntes ao óleo (MP 1.363 plenamente vigente, isenção
PIS/Cofins já 54 dias vencida) e múltiplos catalisadores de alta represados, não correntes (B16,
Danantara, B50). O óleo brasileiro segue mais fraco estruturalmente até que algum dos vetores
represados vire fato concreto — e a lacuna crescente de 110 dias sem revisão humana do catálogo
tributário é, em si, um risco operacional: qualquer mudança de status desses vetores nas últimas
três semanas e meia simplesmente não seria capturada por este sistema até uma checagem manual.

## Riscos e eventos próximos

- **Confirmação (ou repetição) do padrão de OHLC duplicado em farelo/HO=F** — esta é a quinta
  ocorrência documentada; se o padrão persistir por mais uma sessão, deixa de ser tratável como
  anomalia pontual e passa a exigir uma correção estrutural na captura desses dois tickers
  específicos (ZMZ26.CBT e HO=F), possivelmente revisando a lógica de captura/timing do
  scraper.
- **Persistência do regime de baixa liquidez em toda a curva** — cinco sessões seguidas (21 a
  23/09) com volumes entre 2,6% e 4,8% do nível de referência de 18/09; a próxima sessão com
  volume normalizado é o primeiro teste de se este é um efeito de calendário (proximidade de
  vencimento, feriados no exterior) ou algo mais estrutural na fonte de dado.
- **USDA Crop Progress**: próximo corte esperado por volta de 27-28/09 (semana encerrada em
  27/09); o corte de 20/09 já chegou, então a cadência voltou ao normal depois do hiato de duas
  semanas registrado em leituras anteriores.
- **Confirmação (ou reversão) da estabilidade do físico de farelo em Rondonópolis/MT** — a
  próxima atualização do NAG é o teste de se o patamar de R$2.200/ton se mantém por uma terceira
  leitura seguida.
- **Próximo corte de COT (posições de 22/09), esperado por volta de 25-26/09.** Primeiro capaz
  de confirmar se os fundos que ampliaram net long em farelo e óleo (COT de 15/09) já realizaram
  lucro ou ampliaram ainda mais as posições, e se a redução de net long em soja se acentuou.
- **Nível técnico a vigiar em farelo:** volta abaixo de 325,00 desfaria o rompimento (folga
  atual +14,65%).
- **Nível técnico a vigiar em soja:** volta abaixo de 1.180,00 desfaria o rompimento (folga
  atual +12,39%).
- **Nível técnico a vigiar em óleo:** recuperação acima de 72,00 desfaria a leitura de suporte
  rompido (distância atual -5,94%, a maior desta série).
- **Crush margin:** retorno acima de US$2,50/bushel encerraria a leitura de suporte rompido
  monitorada pela fila (distância atual -4,64%, oscilando num intervalo estreito desde 18/09,
  sem tendência clara de recuperação).
- **Prêmio de exportação de farelo e óleo em Paranaguá**, congelado há 14 dias corridos (desde
  08/09) — se o aperto físico de MT for real e amplo, esperar eventualmente refletido também
  nesse prêmio FOB.
- **NOPA mensal**: mais um "release" sem dado novo de fato (paywall), agora referenciado como
  `release-nopa-2026-09-23`.
- **Confirmação da centralização plena da exportação de palma pela Danantara** — alvo 01/09, já
  22 dias passados sem confirmação.
- **Vigência da isenção PIS/Cofins do biodiesel** (54 dias vencida) e **MP 1.358/2026 da
  gasolina** (74 dias vencidos) — checar notícia de renovação/expiração.
- **Marco de 110 dias sem revisão humana do `tributario_watch.toml`** — pelo menos dois vetores
  (isenção PIS/Cofins biodiesel, MP 1.358/2026) já vencidos sem registro de renovação.
- **Detalhamento das manchetes recentes** ("$14 soybeans" de 22/09 e a manchete de alta física
  brasileira de 21/09) — monitorar se a fonte RSS traz o corpo do texto ou números concretos nas
  próximas atualizações.
- **Revisão de D+180 da tese original do ratio Far/Soj**, programada para 2026-12-08.
- **Virada da banda estatística de 30 dias do óleo para "baixista"** — primeira ocorrência nesta
  série; acompanhar se as próximas gerações do forecast confirmam ou revertem essa mudança de
  sinal.

## Honestidade

- **A anomalia mais relevante desta leitura, pela quinta vez consecutiva: farelo e heating oil
  fecham hoje com abertura, máxima, mínima e volume idênticos, byte a byte, aos de ontem —
  apenas o fechamento muda.** Documentada pela primeira vez em três ocorrências isoladas do
  HO=F ([[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]]), estendida ao farelo ontem
  ([[2026-09-22_leitura-complexo]]), e hoje repetida de forma idêntica para os dois contratos
  juntos. Esta leitura tratou os níveis de fechamento como válidos para fins de nível técnico e
  de direção (a fila os reporta e os gatilhos de resistência/suporte continuam corretos em
  termos de onde o preço está), mas rebaixou explicitamente a confiança em qualquer argumento
  que dependesse da qualidade da sessão em si (volume, confirmação de tendência por range) —
  especialmente na leitura de óleo, onde a margem de biodiesel de hoje se apoia diretamente no
  HO=F afetado. É digno de nota que soja e óleo NÃO exibiram esse padrão hoje (não há sequer uma
  linha bruta de `cme_cbot` para eles em 22/09 neste dump para efeito de comparação, mas os
  fechamentos de 23/09 desses dois contratos são plausíveis e distintos dos de ontem) — o que
  sugere que o problema de captura é específico a como o sistema lê os tickers ZMZ26.CBT e
  HO=F, não generalizado a todo o pipeline.
- **Os volumes dos quatro contratos monitorados (soja 3.843, farelo 2.996, óleo 2.986, heating
  oil 2.189) estão entre 2,6% e 4,8% do volume da última sessão plena documentada** (18/09:
  108.222, 113.303, 67.046 e 45.315, respectivamente, valor citado com base na leitura de
  22/09, já que a linha bruta de 18/09 não está mais visível na janela deste dump) — esse regime
  de baixa liquidez já dura, no mínimo, desde 21/09, cinco sessões seguidas, o que é uma faixa de
  tempo maior do que a de qualquer anomalia pontual documentada até aqui nesta série.
- **USDA Crop Progress trouxe seu primeiro corte novo (20/09) depois de duas semanas de hiato**
  — resolve parcialmente a lacuna reportada nas duas últimas leituras, mas o corte em si já tem
  três dias de idade frente a hoje (23/09); não há explicação no briefing para o hiato anterior
  de duas semanas, então não se sabe se ele foi uma limitação pontual da fonte ou algo que pode
  se repetir.
- **O físico de farelo na média do Rio Grande do Sul (fonte Clicmercado) segue com o mesmo valor
  exato (R$1.860,00/ton) em todos os pontos de dados visíveis do dump, de 08/09 a 22/09** — 14
  dias corridos de valor idêntico dígito a dígito, o que segue sendo estatisticamente muito
  improvável para uma série de preço físico genuíno e reforça a suspeita, já registrada em
  leituras anteriores, de que essa fonte específica não está atualizando de fato.
- **As manchetes de notícia recentes estão disponíveis apenas como título** — nem o corpo da
  manchete "Shrinking supplies keep prospects for $14 soybeans on table" (22/09) nem o da
  manchete brasileira de 21/09 estão disponíveis neste dump; o item de contagem de 23/09
  (`noticias | items_fetched`, 5 itens mantidos) também não traz o texto desses itens. Não é
  possível citar números de fonte primária para validar a tese de "shrinking supplies" com
  precisão.
- **O corte de COT `release-cftc_cot-2026-09-15` segue sendo o dado de posicionamento mais
  recente**, agora oito dias corridos depois do corte. O próximo corte (posições de 22/09,
  esperado 25-26/09) resolve essa lacuna.
- **Percentil histórico de posicionamento COT não está disponível no briefing** — toda leitura
  de "fundos comprando/vendendo" nesta série usa variação absoluta semana a semana de contratos,
  não percentil histórico.
- **O item de fila `release-nopa-2026-09-23` é mais uma repetição sem dado novo** — o mesmo
  padrão de todas as leituras anteriores desde que este monitoramento começou (paywall,
  `monthly_status` em 0,0 bool).
- **`tributario_watch.toml` sem atualização há 110 dias corridos** — pelo menos dois vetores
  (isenção PIS/Cofins do biodiesel, MP 1.358/2026) já passaram da vigência registrada sem nota
  de renovação ou expiração.
- **A previsão INMET para 23/09 é previsão meteorológica, não medição de precipitação ou
  temperatura real** — as menções a "chuva", "chuva isolada", "pancadas" e "geada" são
  indicativas do boletim, não confirmação de que o evento ocorreu ou ocorrerá; a menção de
  geada em Passo Fundo/RS pela manhã é relevante sobretudo para culturas de inverno já
  estabelecidas na região, já que o plantio de soja no RS normalmente só começa em
  outubro/novembro — o vínculo direto com a tese de preço de soja é, portanto, fraco nesta data.
- **Sem PTAX de 23/09 neste dump** — o cálculo de paridade da soja brasileira de hoje reusa o
  USD/BRL de 22/09 (5,1161), um lag normal de publicação (a PTAX de hoje costuma sair mais tarde
  no dia), não uma anomalia.
- **Sem ponto novo de NAG físico BR para 23/09** — os valores de farelo/soja físico citados
  nesta leitura são os de 22/09, a atualização mais recente disponível; lag normal de um dia.
- **MPOB (palma Malásia) segue com parser quebrado** — nenhum dado de produção/estoque de palma
  malaia disponível, o que impede monitorar diretamente o catalisador represado da centralização
  de exportação indonésia (Danantara).
- **BCBA (Argentina) segue sem links de relatório detectados**, com o carimbo mais recente ainda
  em 09/09 — nenhum dado de safra ou exportação argentina disponível além do que já vem
  consolidado pelo WASDE.
- **Os forecasts estatísticos internos (bandas 7d/30d) foram gerados hoje sobre o fechamento de
  23/09** — o viés "altista" em soja e farelo e a virada para "baixista" em óleo (30d) refletem
  extrapolação estatística de tendência (MA20 + volatilidade + slope), não uma reavaliação
  fundamentalista; esta leitura mantém farelo em bull, soja em neutro e óleo em bear a partir da
  análise qualitativa, coerente com a virada da banda estatística no caso do óleo, mas
  independente dela.
- **A fila de julgamento volta a listar as revisões D+7 e D+90 da tese de 11/06 como "vencidas"**
  — o veredito de ambas já foi fechado em
  [[2026-09-17_ratio-far-soj-supera-nivel-de-abertura-da-tese-original-quarta-sessao]]; o sistema
  de fila não lê de volta os insights publicados para marcar a revisão como encerrada. Nenhuma
  ação nova é necessária sobre essas duas revisões específicas.
