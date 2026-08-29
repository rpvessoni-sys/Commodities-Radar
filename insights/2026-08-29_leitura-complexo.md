---
data: 2026-08-29
titulo: "Soja rompe 1.180 pelo terceiro pregão e puxa o complexo inteiro para cima (1.287,75, +1,56% no dia) — mas o ratio Far/Soj sob 80% (79,84%) revela que é a SOJA subindo mais rápido, não o farelo fraco; o óleo salta 3,63% sem reconquistar o pivô de 72,00, e o COT (ainda de 25/08, pré-rali) mostra fundos reduzindo convicção justamente na perna que mais valorizou"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT (ZSX26 soja / ZMV26 farelo / ZLV26 óleo) — sessão de 2026-08-28: soja abertura 1.270,00, máxima 1.290,00, mínima 1.269,25, fechamento 1.287,75 USD cts/bushel, volume 153.472 contratos; farelo abertura 333,10, máxima 345,70, mínima 331,40, fechamento 342,70 USD/short ton, volume 46.745 contratos; óleo abertura 69,12, máxima 71,08, mínima 68,93, fechamento 70,71 USD cts/lb, volume 57.670 contratos
  - CME CBOT — sessão de 2026-08-27, presente neste dump SÓ para farelo (fechamento 334,40 USD/sht, volume 59.717) e heating oil (fechamento 4,2787 USD/galão); os fechamentos de soja (1.268,00) e óleo (68,23) de 27/08 usados nesta leitura vêm reconstruídos via `indicators` (crush margin), não de uma linha própria de CBOT — ver Honestidade sobre a revisão retroativa desses mesmos números
  - CME NYMEX heating oil (HO=F) — 2026-08-28 fechamento 4,2421 USD/galão, -0,85% frente a 27/08 (4,2787)
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, paridade BR, ISF, ISO) — série diária 2026-08-24 a 2026-08-29
  - BCB PTAX — série 2026-08-17 a 2026-08-28, USD/BRL fechou em 5,2005 (28/08, +0,70% frente a 27/08); real revertendo a valorização que vinha desde 18/08
  - CEPEA/ESALQ Soja Paranaguá via NAG — série 2026-08-20 a 2026-08-28, fechou em R$ 159,76/saca (28/08, var. +3,04%)
  - CEPEA/ESALQ Soja Paraná interior via NAG — série 2026-08-24 a 2026-08-28, fechou em R$ 151,32/saca (28/08, var. +1,41%)
  - NAG Físico BR — série 2026-08-24 a 2026-08-28: farelo MT/IMEA R$ 1.795,68/ton (28/08, +4,03% no dia, rompendo 5 dias de congelamento em R$ 1.726,20), Rondonópolis/MT R$ 1.870,00/ton (estável desde 26/08), RS média R$ 1.860,00/ton (estável); prêmios export PGUA farelo +0,12 USD/short ton e óleo +0,10 cts/lb, ambos congelados nos mesmos valores desde 24/08 (5 sessões sem mover mesmo com o board disparando — ver Honestidade)
  - CFTC COT Managed Money, Swap Dealers e Producer/Merchant — corte de 2026-08-25 (o mais recente disponível; ainda NÃO cobre as sessões de 27-28/08 que concentraram o rali — ver Honestidade)
  - USDA Crop Progress — corte de 2026-08-23 (12% excelente / 48% boa / 9% ruim), sem corte novo nesta janela
  - USDA WASDE — segue ausente da janela deste briefing
  - NOPA — fila `release-nopa-2026-08-29`, `monthly_status` continua em 0,0 bool (paywall, sem mudança)
  - ABIOVE projeções mensais — balanços set-dez/2026, mesmos valores da leitura anterior
  - NOAA CPC ENSO — carimbo 2026-08-29 (El Niño Advisory, inalterado)
  - MPOB — carimbo 2026-08-29 (3.456 caracteres, parser sem números extraídos, mesma barreira)
  - INMET — previsão para 2026-08-30: calor extremo e céu limpo no Mato Grosso (41°C em Sinop, 40°C em Cuiabá/Lucas do Rio Verde/Sorriso, 36-37°C em Rio Verde/GO e Maringá/PR), chuva isolada em Passo Fundo/RS (mín. 14°C) e pancadas com trovoadas em Cascavel/PR
  - Notícias Agrícolas/Canal Rural RSS — "Novo episódio do Soja Brasil aborda decisão do STF, clima e desafios para a nova safra" (29/08, sem detalhe do teor da decisão no briefing — ver Honestidade); "USDA aponta estoques apertados para milho e cenário confortável para soja" (27/08); "Alta em Chicago impulsiona negócios e leva soja perto de R$ 160 nos portos" (26/08)
  - Forecasts estatísticos internos (bandas 7d/30d, MA20+volatilidade+slope) — geração de 2026-08-29, alvos 05/09 (7d) e 28/09 (30d); viés "altista" em soja e farelo nos dois horizontes, óleo "lateral" no 7d e "altista" no 30d
  - system/tributario_watch.toml (lido como referência, não editado) — `atualizado_em` 2026-06-05 em todos os eventos, 85 dias sem revisão — ver Lente fiscal e Honestidade
  - Fila de julgamento — 2026-08-29, 8 itens: `alerta-quebra_resistencia-soja_cbot-2026-08-28`, `alerta-quebra_suporte-oleo_cbot-2026-08-28`, `alerta-movimento_forte-oleo_cbot-2026-08-28`, `alerta-quebra_resistencia-farelo_cbot-2026-08-28`, `alerta-quebra_suporte-complexo_soja-2026-08-28`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, `trib-DANANTARA-INDONESIA-2026-09-01`, `release-nopa-2026-08-29`
  - Cruza com [[2026-08-28_leitura-complexo]] (leitura anterior, cujos números "finais" de 27-28/08 este briefing revisa outra vez — ver Honestidade) e com a tese original [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (checkpoint D+7 vencido há 72 dias, tratado nesta leitura)
status: ativa
vies: [bull-soja, bull-farelo, neutral-oleo_soja]
---

## Visão geral

O complexo soja é, no fundo, uma fábrica: você compra soja em grão (a matéria-prima),
"esmaga" (crush) e sai com dois produtos — farelo (proteína, vai pra ração animal) e
óleo (vai pra alimentação e, cada vez mais, pra biodiesel). Quem financia essa fábrica é
o **crush margin**: o valor de venda de farelo + óleo, menos o custo da soja. Hoje
(28/08, dado mais novo do briefing) esse crush fechou em **US$ 2,44/bushel** — abaixo do
patamar de referência de US$ 2,50 (`alerta-quebra_suporte-complexo_soja-2026-08-28`), mas
na verdade **subindo** frente aos US$ 2,18 de ontem (indicators, 27/08→28/08, +11,8%). Ou
seja: o crush está comprimido em nível absoluto, mas está *melhorando*, não piorando — a
esmagadora está ganhando margem de novo, não perdendo.

Dentro desse crush, quem "manda" — quem puxa mais valor — está mudando de mão dia a dia.
O **oil share** (fatia do óleo no valor total do crush) fechou em **50,78%** (indicators,
28/08) — ligeiramente acima da metade, uma faixa apertada entre 50,3% e 51,1% nos últimos
cinco pregões. É um empate técnico: nem o óleo nem o farelo estão dominando com folga o
bolo de receita da esmagadora agora. Só que o **Índice de Suporte do Óleo (ISO)** — um
indicador sintético que soma 5 condições estruturais (margem de biodiesel, RIN D4,
heating oil, oil share e momentum) — está **travado em 100/100** desde pelo menos 24/08,
o teto da escala. Ao mesmo tempo o **Índice de Sobra de Farelo (ISF)** também está
travado em **80/100** (4 de 5 condições apontando pressão baixista no farelo) no mesmo
período. Isso soa contraditório à primeira vista — como pode o farelo estar "sobrando"
estruturalmente e, ao mesmo tempo, ter acabado de romper a resistência de 325 com um
salto de +2,48% no dia? A resposta está no **ratio Far/Soj**, o termômetro que mede o
preço do farelo relativo à soja (não o preço absoluto de nenhum dos dois): ele fechou em
**79,84%** hoje (indicators, 28/08), abaixo da linha de 80% que o próprio sistema rotula
como "abundante". O ratio vem subindo devagar nos últimos 4 pregões (78,46% → 79,84%,
+1,76%), mas segue preso na zona de abundância. O que isso ensina: o farelo está caro em
valor absoluto (342,70 USD/sht, maior nível do período recente) **porque a soja está
subindo ainda mais rápido** — não porque o farelo, isoladamente, esteja escasso ou
demandado. É a soja que está no comando do complexo hoje, não o farelo.

O que mudou hoje, em uma frase: soja rompeu a resistência de 1.180 pelo terceiro pregão
seguido e fechou em 1.287,75 (+1,56% no dia, CME CBOT 28/08), puxando farelo (+2,48%,
rompendo 325) e óleo (+3,63%, mas ainda 1,8% abaixo do pivô técnico de 72,00) juntos —
um movimento de "maré subindo levanta todos os barcos" mais do que uma reprecificação
independente de cada perna. O câmbio ajudou: o USD/BRL saltou +0,70% no mesmo dia (BCB
PTAX, 5,2005 em 28/08 vs 5,1642 em 27/08), amplificando o ganho em reais — a paridade
CBOT-implícita em saca subiu de R$ 144,36 para R$ 147,64 (+2,27%, mais que o próprio
avanço do CBOT em dólar). **Leitura de uma linha**: o pivô do complexo hoje é a soja
(não o farelo, não o óleo), a maior convicção é que o rali de soja é "de verdade" — tem
fundo comprado novo entrando via CFTC (ver seção Soja) — e o nível de confiança é
**médio**: o COT mais recente (25/08) ainda não enxerga as sessões de 27-28/08 que
concentraram o movimento, e os fechamentos de 27-28/08 já foram revisados uma vez entre
a leitura de ontem e esta (ver Honestidade). Trate os números de hoje como direcionalmente
corretos, não como definitivos.

## Soja

**Viés: bull, moderadamente forte.**

O que sustenta a tese:

- **Rompimento técnico confirmado em preço real.** Soja CBOT fechou em 1.287,75 USD
  cts/bushel em 28/08/2026 (CME CBOT), 9,1% acima da resistência de 1.180,00 que a fila
  de julgamento monitorava (`alerta-quebra_resistencia-soja_cbot-2026-08-28`). Esta é a
  terceira sessão consecutiva acima desse nível (27/08 já havia rompido, hoje consolida
  e avança mais +1,56% frente ao fechamento de ontem, 1.268,00 — reconstruído via
  indicators). Romper e CONSOLIDAR acima de um nível — em vez de romper e recuar no dia
  seguinte — é o que separa um rompimento técnico real de um "fakeout": aqui o mercado
  não só rompeu como voltou no dia seguinte e comprou mais.

- **Fundos entrando com dinheiro novo, não só cobrindo posição.** O corte CFTC COT de
  25/08/2026 (o mais recente do briefing) mostra managed money em soja com **long de
  239.335 contratos** (vs 197.446 em 18/08, +21,2%) e **short de 38.656** (vs 45.664,
  -15,3%) — o net long saltou de 151.782 para 200.679 contratos, **+32,2% em uma
  semana**. O que diferencia isso de um simples "short squeeze": o open interest total
  caiu levemente no mesmo período (972.531 vs 989.729 contratos, -1,7%) enquanto o long
  bruto dos fundos SUBIU dois dígitos — ou seja, não é só posição vendida saindo
  (cobertura), é dinheiro novo entrando comprado. Isso é o tipo de posicionamento que
  sustenta um movimento além de um repique técnico.

- **Câmbio reforçando o movimento, não competindo com ele.** O USD/BRL fechou a
  28/08/2026 em 5,2005 (BCB PTAX), +0,70% frente aos 5,1642 de 27/08 — revertendo a
  trajetória de valorização do real que vinha desde 18/08 (quando bateu 5,2043 e depois
  caiu até 5,1490 em 25/08). Como o trader normalmente pensa em paridade (CBOT × câmbio),
  um real mais fraco no mesmo dia em que o CBOT sobe é o cenário "os dois motores
  puxando pro mesmo lado": a paridade calculada (sem basis) saltou de R$ 144,36/saca
  (27/08) para R$ 147,64/saca (28/08), +2,27% — mais do que o próprio avanço em dólar do
  CBOT (+1,56%), porque o câmbio somou.

- **Físico brasileiro pagando prêmio sobre a paridade, de forma consistente — não é
  ruído de um dia.** O preço à vista em Paranaguá (CEPEA/ESALQ via NAG) fechou em R$
  159,76/saca em 28/08 (+3,04% no dia), R$ 12,12/saca ACIMA da paridade CBOT-implícita
  sem basis (R$ 147,64) — um basis físico positivo de ~8,2%. Ontem esse mesmo basis já
  estava em +7,4% (R$ 155,05 vs R$ 144,36). Basis positivo e CRESCENDO por dois dias
  seguidos é sinal de mercado físico apertado no porto — demanda de exportação
  competindo por originação — e não apenas o CBOT "empurrando" o preço interno. Reforça
  isso o prêmio do porto sobre o interior: Paranaguá (159,76) fechou R$ 8,44/saca acima
  do Paraná interior (151,32) em 28/08, ante um prêmio de R$ 5,84 em 27/08 — o prêmio
  portuário quase dobrou de tamanho (3,9% → 5,6%) num único pregão, evidência direta de
  puxada exportadora mais forte, não só repasse de CBOT.

- **Estoques brasileiros de soja apertando estruturalmente rumo ao fim de 2026.** Nas
  projeções mensais ABIOVE (dado do briefing, sem data de atualização nova nesta
  janela), o estoque final de soja no Brasil recua de 5.720,8 mil t (out/26) para
  3.658,9 mil t (nov/26) e 1.889,9 mil t (dez/26) — uma queda de ~67% em dois meses,
  reflexo natural do calendário (esmagamento consumindo o estoque de passagem antes da
  nova safra 2026/27). É movimento sazonal esperado, mas alimenta o pano de fundo de
  "sobra menor de soja disponível" que sustenta preço mais alto no fim de ano, coerente
  com o viés "altista" que os próprios forecasts internos (bandas 30d, ver abaixo)
  atribuem à soja.

- **USDA Crop Progress mostra leve deterioração, não force majeure, mas é um ingrediente
  a favor.** O corte de 23/08/2026 mostra a safra americana em 12% excelente / 48% boa /
  9% ruim, ante 12%/49%/8% em 16/08 — perda de 1 ponto percentual em "boa" e ganho de 1
  ponto em "ruim". Modesto, mas é a segunda semana seguida de leve piora, e a notícia de
  enchentes no Meio-Oeste ("Midwest flooding threatens corn and soybean yields",
  Farm Progress, 24/08) aponta na mesma direção — risco de produtividade, não colapso.

**O que invalida / risco:**

- O próprio COT usado acima é de 25/08 — ele NÃO enxerga as duas sessões (27 e 28/08)
  que concentraram o grosso do rali. Se o próximo corte (esperado por volta de 01/09)
  mostrar que os fundos já estavam no topo do seu apetite comprado e começaram a
  distribuir posição durante o próprio rali, a leitura de "dinheiro novo entrando" muda
  para "fundos já supridos, risco de realização".
- Notícia de 27/08 ("USDA aponta estoques apertados para milho e cenário confortável
  para soja") descreve exatamente o oposto do que o preço está fazendo — estoque
  "confortável" normalmente não é gatilho de rali de 9% sobre resistência. Ou o mercado
  está precificando outra coisa (câmbio, técnico, curto-covering) que não é balanço de
  oferta e demanda fundamentalista, ou a notícia está desatualizada frente ao que
  motivou o movimento — de qualquer forma, é uma dissonância que merece ceticismo.
- Reversão do câmbio: se o USD/BRL voltar a se valorizar (voltar à trajetória vista de
  18 a 25/08, quando caiu de 5,2043 para 5,1490), a paridade em reais perde um dos dois
  motores que a levaram para cima hoje.
- Nível técnico a vigiar: qualquer fechamento de volta abaixo de 1.180 desfaria o
  rompimento e devolveria a tese para neutro/bear.

**Leitura operacional:** para quem opera os dois lados, hoje não é dia de vender força
em soja — o rompimento tem consolidação (3ª sessão), fluxo de fundos comprando dinheiro
novo (não só cobertura) e dois motores (CBOT + câmbio) alinhados. O risco assimétrico é
justamente o oposto do movimento: se o próximo COT (dados de 01/09) mostrar fundos já
excessivamente comprados sem sustentação de fluxo físico adicional, positions long ficam
mais arriscadas de manter sem proteção. Quem quiser jogar contra o movimento deve esperar
um sinal técnico claro (perda de 1.180) e não tentar pegar o topo só porque "subiu muito,
muito rápido" — nada nos dados de hoje aponta exaustão ainda.

## Farelo

**Viés: bull na fita, mas com estrutura contraditória por baixo — leia como rali por
correlação com a soja, não por força própria.**

O que sustenta a tese (na fita):

- **Rompimento de resistência com volume relevante.** Farelo CBOT fechou em 342,70
  USD/short ton em 28/08/2026 (CME CBOT), 5,4% acima da resistência de 325,00
  (`alerta-quebra_resistencia-farelo_cbot-2026-08-28`), com +2,48% no dia (vs 334,40 em
  27/08) e volume de 46.745 contratos — abaixo do volume de 59.717 de 27/08, mas ainda
  assim relevante frente à média recente.

- **Cobertura de posição vendida agressiva no CFTC.** O corte de 25/08/2026 mostra
  managed money com short caindo de 46.003 para 33.662 contratos (-26,8% em uma semana)
  — a maior variação percentual entre as três pernas do complexo — enquanto o long ficou
  praticamente parado (129.318 → 129.615, +0,2%). Isso é o assinatura clássica de
  **short covering**, não de convicção compradora nova: quem estava vendido está saindo,
  mas quem já estava comprado não aumentou a aposta. É uma dinâmica mais frágil do que a
  vista em soja (onde o long bruto também cresceu dois dígitos).

- **Físico brasileiro reagindo com atraso, mas reagindo.** O farelo MT/IMEA (NAG via
  briefing) ficou congelado em R$ 1.726,20/ton por cinco sessões seguidas (24 a 27/08) e
  saltou para R$ 1.795,68/ton em 28/08 (+4,03%), fechando parte do gap para
  Rondonópolis/MT (R$ 1.870,00, estável) e RS média (R$ 1.860,00, estável). O interior
  mato-grossense estava defasado e está correndo atrás do resto do país — sinal de que o
  repasse do rali do CBOT está mesmo passando para o físico, não é só papel.

O que tensiona a tese (a estrutura por baixo):

- **O ratio Far/Soj segue na zona "abundante" (<80%).** Fechou em 79,84% em 28/08
  (indicators), a quarta sessão consecutiva abaixo de 80% desde pelo menos 24/08
  (79,20% → 78,46% → 78,93% → 79,12% → 79,84%). Isso mede o farelo RELATIVO à soja, não
  em valor absoluto — e diz que o farelo, comparado à soja, segue relativamente barato,
  mesmo depois do rompimento de hoje. A leitura correta não é "farelo forte", é "soja
  mais forte que farelo, mas os dois sobem juntos".
- **O Índice de Sobra de Farelo (ISF) segue travado em 80/100** (4 de 5 condições
  estruturais apontando pressão baixista) desde pelo menos 24/08, sem mudar mesmo com o
  rompimento técnico de hoje — o sistema interno não vê o quadro estrutural de oferta de
  farelo mudando, só o preço acompanhando a soja.
- **Prêmio de exportação em Paranaguá congelado.** +0,12 USD/short ton desde 24/08 (NAG,
  5 sessões sem se mexer), mesmo com o board subindo forte. Ou o dado está desatualizado
  (ver Honestidade), ou a competitividade do farelo brasileiro para exportação
  simplesmente não acompanhou o rali do papel — o que seria mais um sinal de que a
  "sobra" doméstica de farelo (ISF alto) segue intacta por trás do preço em alta.

**Revisão da fila `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`:**
esta revisão programada para D+7 (18/06/2026) está **72 dias vencida** — o hiato de
dados de CBOT que dominou o briefing entre meados de julho e 27/08 impediu qualquer
checkpoint no prazo. Tratando agora, com os dados disponíveis: a tese original (11/06)
apostava que o ratio comprimiria de 81,4% para abaixo de 80% "em 1-2 semanas", com viés
baixista no farelo em PREÇO ABSOLUTO. O ratio de fato está abaixo de 80% hoje (79,84%) —
a métrica de compressão SE CONFIRMOU, ainda que ~11 semanas depois do previsto, não 1-2.
Mas a segunda parte da tese — farelo caindo em valor absoluto — **foi invalidada**: o
farelo CBOT saiu de ~303,60 USD/sht (10/06, valor citado na tese original) para 342,70
hoje, alta de +12,9%. O mecanismo real foi diferente do previsto: não foi o farelo caindo
para comprimir o ratio, foi a SOJA subindo mais rápido que o farelo. Marco relevante
também citado na tese original: "crush margin desabar para <2,50 (alerta configurado) →
esmagadora tira o pé, oferta de farelo seca" — isso também aconteceu (crush em 2,44 hoje,
abaixo do próprio limiar citado em junho), o que teoricamente APOIA um farelo mais firme
adiante (menos esmagamento = menos farelo novo chegando ao mercado), um contraponto ao
ISF=80 que merece ser vigiado nas próximas semanas. **Conclusão da revisão**: tese de
ratio comprimido CONFIRMADA (mecanismo diferente do esperado); tese de farelo em queda
absoluta INVALIDADA pelo próprio mercado. Status a atualizar: revisada, sem encerrar —
o quadro estrutural (ISF 80, prêmio export congelado) ainda argumenta pela compressão
continuar, mas o preço absoluto está fazendo o oposto do que a tese de junho previa.

**O que invalida / risco adicional:** um novo corte de COT mostrando os fundos
"terminando" a cobertura de shorts (o short já caiu 27% em uma semana — tem menos
munição de cobertura sobrando) tiraria o principal motor recente do rali de farelo. Se o
ratio Far/Soj voltar a cair (não subir) nos próximos dias enquanto o preço absoluto segue
subindo, é sinal mais forte ainda de que farelo está sendo carregado pela soja, e
QUALQUER correção na soja tende a bater desproporcionalmente no farelo (ele não tem
motor próprio para segurar o nível).

**Leitura operacional:** o rali de farelo hoje é real em preço (rompeu 325, +2,48%), mas
a origem — short covering, não convicção nova — e a persistência do ratio abaixo de 80%
tornam essa perna a mais frágil das três para se manter comprado sem hedge. Para quem
opera o spread Far/Soj, a leitura de mean-reversion segue: o ratio comprimido (79,84%)
é historicamente uma zona de acumulação para posições que apostam em reversão (long
farelo / short soja, ou via crush) — mas o timing de junho já provou que "1-2 semanas"
vira "72 dias" facilmente; não force entrada achando que a reversão é iminente só porque
a métrica está esticada.

## Óleo

**Viés: neutro — batalha entre um repique forte de curto prazo e uma estrutura técnica
ainda quebrada, com fundamentos de médio prazo positivos e posicionamento de fundos
(desatualizado) ainda cético.**

O que sustenta o lado comprado:

- **O maior salto percentual do dia em qualquer das três pernas.** Óleo CBOT fechou em
  70,71 USD cts/lb em 28/08/2026 (CME CBOT), alta de +3,63% frente aos 68,23 de 27/08
  (`alerta-movimento_forte-oleo_cbot-2026-08-28`) — mais que o dobro da alta percentual
  da soja (+1,56%) e mais forte que o farelo (+2,48%). Em um dia de "maré subindo", o
  óleo foi o barco que subiu mais rápido.
- **Índice de Suporte do Óleo (ISO) no teto da escala: 100/100** (indicators, 24 a
  28/08, 5 de 5 condições estruturais favoráveis) — margem de biodiesel americana ainda
  positiva, RIN D4 sustentado, heating oil firme, oil share saudável e momentum técnico.
  É o indicador estrutural mais unânime de todo o briefing, sem uma única sessão de
  enfraquecimento na janela disponível.
- **Margem de biodiesel americana segue positiva, mesmo comprimindo.** Fechou em 1,3038
  USD/galão em 28/08 (indicators: receita 7,4071 = HO 4,24 + 1,5×RIN 2,11; custo 6,10 =
  óleo 5,30 + industrial 0,80), abaixo dos 1,5264 de 27/08 (-14,6%) — a compressão veio
  do CUSTO do óleo subindo (+3,63%, acompanhando o próprio CBOT) mais rápido que a
  receita (que caiu levemente, puxada pelo heating oil -0,85%). Mas o ponto central é
  que a margem CONTINUA POSITIVA e folgada (>US$ 1,30/galão) — não há sinal de que o
  biodiesel americano esteja perdendo economia de produção, só que o insumo (óleo de
  soja) ficou mais caro para o crushor comprar, o que é exatamente o mecanismo de um
  óleo em alta: quem compra o insumo paga mais.
- **Catalisador regulatório a 3 dias de distância.** A fila traz `trib-DANANTARA-
  INDONESIA-2026-09-01`: em 01/09/2026 (3 dias), a Indonésia completa a centralização da
  exportação de óleo de palma sob o fundo soberano Danantara (tributario_watch.toml,
  atualizado 05/06/2026, direção "alta" para óleo de soja, produtos ["oleo_soja"]). O
  mecanismo: se a nova estrutura estatal reduzir ou tornar mais burocrática a exportação
  de palma — o maior óleo vegetal do mundo em volume — o óleo de soja ganha espaço como
  substituto na demanda global de óleos comestíveis e industriais. Ainda é uma DATA-ALVO,
  não um resultado confirmado; o próprio evento no monitor está com dado de 85 dias sem
  atualização, então vale tratar como catalisador a monitorar, não como fato já
  precificado.
- **Levy de exportação da palma indonésia (até 12,5%, PMK 9/2026) segue vigente**
  (tributario_watch.toml, status "vigente", direção "alta" para óleo de soja) — encarece
  estruturalmente a palma no mercado internacional, o que sustenta o óleo de soja por
  substituição de forma permanente, não apenas no evento de 01/09.

O que sustenta o lado vendido / cético:

- **Ainda abaixo do pivô técnico de 72,00.** Mesmo com o salto de +3,63%, o fechamento de
  70,71 segue 1,8% abaixo do nível de 72,00 que a fila monitora como suporte perdido
  (`alerta-quebra_suporte-oleo_cbot-2026-08-28`). Tecnicamente, isso é um repique dentro
  de uma estrutura ainda quebrada, não uma reconquista confirmada — o nível a vigiar é se
  o próximo pregão consolida acima de 72,00 (reversão real) ou devolve o ganho (rali de
  short covering que esgotou o fôlego em um dia).
- **O COT mais recente (25/08) mostra fundos DIMINUINDO net long antes do próprio rali.**
  Managed money em óleo tinha long caindo de 116.669 para 114.248 contratos (-2,1%) e
  short SUBINDO de 25.436 para 29.132 (+14,5%) entre 18/08 e 25/08 — o net long recuou
  6,7% (91.233 → 85.116). É o oposto do que se viu em soja (fundos comprando mais) e
  farelo (fundos cobrindo short): em óleo, os fundos estavam reduzindo convicção
  comprada bem antes do salto de 27-28/08. O open interest também caiu mais que nas
  outras pernas (-4,4% na semana, 624.433 → 597.071) — sinal de posições sendo fechadas,
  não de entrada de capital novo. Isso não significa que o rali de hoje seja falso, mas
  significa que ele não tem, pelos dados disponíveis, uma fotografia de fundos
  comprando — pode estar sendo puxado por curto-covering recente que o COT ainda não
  capturou (a limitação de defasagem de 3-4 dias já discutida na seção de soja se aplica
  aqui com um peso extra, porque a foto pré-rali já ia na direção contrária).
- **Prêmio de exportação em Paranaguá congelado em +0,10 cts/lb desde 24/08** (NAG, 5
  sessões sem mudar), o mesmo padrão de estagnação visto no farelo — sinal de possível
  atraso na atualização do dado (ver Honestidade) mais do que uma leitura de mercado.

**O que invalida / risco:** para o lado comprado, um fechamento amanhã de volta abaixo
de ~69 (perto da abertura de hoje) devolveria todo o repique e confirmaria que foi
apenas um dia de cobertura técnica sem seguimento. Para o lado vendido, se o Índice de
Suporte do Óleo (travado em 100 há 5 sessões) começar a cair — por exemplo, se a margem
de biodiesel comprimir mais e virar negativa, ou se o heating oil romper para baixo — a
tese estrutural bullish perde sustentação. O evento Danantara em 01/09 é um catalisador
binário: se a Indonésia sinalizar QUALQUER atraso na centralização (histórico recente do
programa B50 indonésio, monitorando desde junho sem confirmação de execução plena, é
precedente de que anúncios ambiciosos nem sempre viram fato no prazo), o efeito bullish
esperado esfria rápido.

**Leitura operacional:** esta é a perna mais indefinida das três hoje — nem o trader
comprado nem o vendido tem o quadro completo a favor. Quem está comprado tem a favor o
ISO no teto e o catalisador Danantara em 3 dias; quem está vendido tem a favor o nível
técnico ainda não reconquistado e o COT (mesmo que defasado) mostrando fundos reduzindo
convicção. Não é dia de convicção direcional forte em óleo isolado — faz mais sentido
tratar como parte do spread (ver seção seguinte) do que como posição direcional pura, ou
aguardar a consolidação (ou não) acima de 72,00 antes de aumentar exposição em qualquer
direção.

## Spreads e crush (leitura de complexo)

Juntando as três leituras: o ratio Far/Soj em 79,84% (zona "abundante", <80%) e o oil
share em 50,78% dizem que, EM TERMOS RELATIVOS, a soja está cara frente ao farelo, e o
crush está quase empatado entre farelo e óleo como fonte de receita (nenhum dos dois
domina folgadamente o bolo). Já os dois índices sintéticos — ISF em 80 (sobra
estrutural de farelo) e ISO em 100 (domínio estrutural do óleo) — desenham um quadro
estrutural mais assimétrico: o sistema "acredita" mais na tese de suporte ao óleo do que
na tese de sobra do farelo, mesmo que o oil share bruto (50,78%) não mostre essa
assimetria tão claramente. A leitura de complexo mais honesta: o crush margin em 2,44
USD/bushel (abaixo do referencial de 2,50, mas SUBINDO nos últimos três pregões — 2,09 →
2,18 → 2,44) mostra uma esmagadora que está recuperando margem, não perdendo — e ela está
recuperando margem porque farelo (+2,48%) e óleo (+3,63%) subiram mais, em conjunto, do
que a soja (+1,56%) no mesmo pregão. Esse é o mecanismo prático por trás do número: o
crush sobe quando os produtos (farelo+óleo) valorizam mais rápido que o insumo (soja); e
foi exatamente isso que aconteceu hoje, apesar da soja ter sido a "notícia" do dia.

Para quem opera o spread Far/Soj especificamente: a compressão abaixo de 80% já dura
pelo menos 5 sessões (desde 24/08) sem reverter de forma consistente — o pequeno avanço
de 78,46% para 79,84% nos últimos 4 pregões é gradual, não um estouro. Trate como zona de
acumulação para quem monta a tese de reversão (farelo relativamente barato tende a se
recuperar frente à soja), mas sem timing definido — a experiência da tese original de
11/06/2026 (ver seção Farelo) mostra que "esticado" pode continuar esticado por meses.
Para quem opera o crush diretamente: o nível de 2,44 está abaixo do referencial histórico
de 2,50 mas em recuperação de 3 dias — não é o momento óbvio de vender crush (apostar em
mais compressão), é mais uma zona neutra até o próximo movimento direcional confirmar.

## Lente fiscal/regulatoria BR

Antes de fechar qualquer tese de preço BR, os vetores tributários/regulatórios vivos que
pesam no complexo — todos do `system/tributario_watch.toml`, cujo carimbo mais recente
(`atualizado_em`) em TODOS os eventos é 2026-06-05, ou seja, **85 dias sem revisão**; o
que segue é a leitura do estado desses vetores conforme cadastrados, sem confirmação de
que ainda reflitam a realidade regulatória de hoje:

- **MP 1.363/2026** (subvenção diesel fóssil R$ 1,12/L, vigente até 31/12/2026):
  barateia o diesel fóssil no mix B15, reduzindo a competitividade relativa do
  biodiesel e, por consequência, a demanda doméstica por óleo de soja — vetor de baixa
  para óleo, sem mudança de status nesta janela.
- **B16 (elevação da mistura de biodiesel para 16%)** segue "adiado" — CNPE cancelado em
  maio, testes técnicos com resultado esperado só por volta de novembro/2026. Enquanto
  não houver data, o mercado não deve precificar a demanda adicional de ~436 mil
  toneladas de óleo que o B16 implicaria — é upside represado, não upside corrente.
- **Isenção de PIS/Cofins do biodiesel na mistura**: o TOML registra vigência ATÉ
  31/07/2026 — data já passada frente aos 29/08/2026 de hoje, e sem qualquer registro de
  prorrogação ou expiração no arquivo (que não foi atualizado desde 05/06). Isso é uma
  lacuna real de informação: não se sabe, a partir dos dados disponíveis, se a isenção
  foi renovada, expirou, ou está em vácuo — se tiver expirado, é vetor de alta de custo
  para o biodiesel BR (portanto pressão de baixa sobre a demanda por óleo), mas isso
  NÃO pode ser afirmado sem confirmação — ver Honestidade.
- **STJ REsp 2.165.276** (crédito de PIS/Cofins sobre soja em biodiesel, vigente,
  direção "alta" para soja/óleo): decisão de maio favorável ao setor, mas não vinculante
  (não é repetitivo) — segue como alívio de custo pontual, não como precedente
  obrigatório para todo o setor.
- **EPA RFS 2026/2027** (mandato de biocombustível americano, vigente desde 15/06/2026,
  direção "alta" para óleo): volumes recordes de RINs (BBD saltando para 9,07 bilhões)
  sustentam a margem de biodiesel americana e, por extensão, o RIN D4 embutido no cálculo
  de margem citado na seção Óleo (1,5×RIN 2,11 = 3,165 USD/galão de receita, componente
  estável nos últimos 5 dias).
- **Crédito 45Z (Clean Fuel Production)**, em tramitação, direção "mista": se a regra
  final excluir insumo importado da elegibilidade, o óleo de soja DOMÉSTICO americano
  ganha (dobra o crédito implícito, ~US$ 0,50/galão), mas o sebo bovino brasileiro que
  hoje é exportado como insumo para biodiesel americano perderia esse mercado e voltaria
  para o blend doméstico brasileiro — o que, na margem, tira uma fatia de demanda do
  óleo de soja DENTRO do Brasil (sebo compete com óleo de soja no blend nacional). É um
  vetor que pode virar contra o óleo de soja BR mesmo sendo favorável ao óleo de soja
  americano — vale rastrear qual perna do mercado se está avaliando.
- **Indonésia — Danantara e levy de exportação (PMK 9/2026)**: já tratados na seção
  Óleo, ambos com direção "alta" para óleo de soja via substituição de palma.
- **Notícia de 29/08/2026** ("Novo episódio do Soja Brasil aborda decisão do STF, clima
  e desafios para a nova safra") menciona uma decisão do STF sem detalhar o teor no
  briefing, e não há nenhum evento STF cadastrado no tributario_watch.toml (só STJ) —
  não é possível avaliar o impacto dessa decisão específica com os dados disponíveis;
  fica como item para acompanhar, não para precificar.

## Riscos e eventos próximos

- **01/09/2026** — marco-alvo da centralização plena da exportação de palma pela
  Danantara (Indonésia), citado na fila `trib-DANANTARA-INDONESIA-2026-09-01`; vigiar se
  a assunção da cadeia se confirma no prazo ou escorrega (como já aconteceu com o B50
  indonésio).
- **Próximo corte CFTC COT** (esperado por volta de 01/09/2026, uma semana após o corte
  de 25/08 usado nesta leitura): é o dado que vai finalmente revelar se os fundos
  entraram comprados NAS sessões de rali (27-28/08) ou se ficaram de fora / venderam a
  força — ponto crítico para validar ou derrubar a leitura de "dinheiro novo" em soja.
- **NOPA mensal** (fila `release-nopa-2026-08-29`): segue atrás de paywall, sem
  confirmação do ritmo de esmagamento americano; StoneX ("Semanal de Óleos Vegetais")
  citada como fonte indireta possível, mas não disponível neste briefing.
- **USDA WASDE**: ausente da janela há bastante tempo; qualquer publicação nova é
  potencial catalisador de revisão de balanço mundial (oferta/demanda) que pode mudar
  o quadro inteiro do complexo de uma vez.
- **Vigência da isenção PIS/Cofins do biodiesel** (TOML aponta 31/07/2026, já vencida
  sem confirmação de prorrogação) — checar se há notícia de renovação/expiração antes de
  assumir qualquer tese de custo do biodiesel BR.
- **Clima**: calor extremo sem chuva no núcleo produtor de Mato Grosso (até 41°C em
  Sinop, INMET, previsão para 30/08) é relevante para a JANELA DE PLANTIO da safra
  2026/27 que se aproxima (setembro/outubro) — solo seco às vésperas do plantio é um
  vetor a monitorar, não ainda um problema confirmado de safra.

## Honestidade

- **Revisão retroativa de dados, de novo.** A leitura de ontem (`[[2026-08-28_leitura-
  complexo]]`) registrou os fechamentos de 28/08 como soja 1.272,00, farelo 332,30 e óleo
  69,73 — todos com a MESMA abertura (1.270,00 / 333,10 / 69,12) mas fechamentos
  DIFERENTES dos que este briefing agora traz para a mesma sessão de 28/08 (1.287,75 /
  342,70 / 70,71). Isso repete o padrão já flagrado na leitura de ontem, que por sua vez
  revisou os números de 27/08 citados em 27/08. Ou seja: os "fechamentos" mais recentes
  deste pipeline vêm sendo corrigidos para cima em pelo menos duas leituras seguidas
  antes de estabilizar. Trate o fechamento de 28/08 usado nesta leitura (1.287,75 /
  342,70 / 70,71) como o melhor dado disponível hoje, não como definitivo — é bem
  possível que a leitura de amanhã traga um ajuste novamente.
- **COT desatualizado frente ao movimento de preço.** O corte CFTC mais recente é de
  25/08/2026 — quatro dias corridos (dois pregões) atrás do fechamento de 28/08 usado
  nesta leitura. Toda a análise de posicionamento de fundos (soja comprando, farelo
  cobrindo short, óleo reduzindo net long) reflete o apetite dos fundos ANTES do rali de
  27-28/08, não durante ou depois. É a maior lacuna de informação desta leitura.
- **Prêmios de exportação (Paranaguá, farelo e óleo) congelados por 5 sessões seguidas**
  (+0,12 USD/sht e +0,10 cts/lb, idênticos de 24 a 28/08) enquanto o board CBOT subiu
  com força — não dá para saber, com os dados disponíveis, se isso reflete mercado
  físico realmente parado ou se é uma limitação de atualização da fonte (NAG). Tratado
  como sinal fraco nesta leitura, não como fato de mercado confirmado.
- **Decisão do STF mencionada na notícia de 29/08 não foi detalhada no briefing** — não
  há teor, não há vínculo claro a nenhum evento do tributario_watch.toml. Não foi
  inventado nenhum conteúdo para essa decisão nesta leitura.
- **tributario_watch.toml sem atualização há 85 dias** (todos os eventos com
  `atualizado_em = 2026-06-05`) — pelo menos dois vetores (isenção PIS/Cofins do
  biodiesel, vigência até 31/07; MP 1.358/2026, vigência até 11/07) já passaram da data
  de vigência registrada sem qualquer nota de renovação ou expiração no arquivo. Tratados
  como "status desconhecido pós-vigência", não como vigentes nem como expirados.
- **NOPA segue inacessível** (paywall) — nenhum número de esmagamento americano mensal
  confirmado nesta leitura nem nas últimas.
- **USDA WASDE ausente** da janela — nenhuma leitura de balanço mundial oficial
  atualizado disponível.
- **Percentil histórico de posicionamento COT não está disponível no briefing** — toda a
  leitura de "fundos comprando/vendendo" nesta análise é baseada em variação semana a
  semana de contratos absolutos (25/08 vs 18/08), não em percentil histórico (o próprio
  texto da rotina pede "COT + percentil", mas o dado de percentil não está no briefing
  hoje) — nenhum percentil foi inventado.
