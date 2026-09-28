---
data: 2026-09-28
titulo: "Primeira sessão real desde sexta-feira: farelo cai -0,78% e soja -0,11% enquanto óleo sobe +0,41%, derrubando o ratio Far/Soj pela segunda sessão seguida (84,80% pico em 24/09 → 84,38% em 25/09 → 83,82% hoje) e levando o oil share a uma máxima da janela (48,06%) — mas o volume de hoje (6.537 contratos em soja, 1.676 em farelo, 1.743 em óleo) e um heating oil com abertura/máxima/mínima idênticas às de ontem repetem, ponto a ponto, o padrão de dado provisório já documentado nesta série, então bull-farelo, bull-soja e bear-óleo seguem mantidos, mas com a confirmação real adiada para o dump de amanhã"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT — sessão de **2026-09-28** (primeira sessão nova desde sexta-feira 25/09; segunda e domingo não têm pregão). Soja (ticker ZSX26.CBT, venc. nov/26): abertura 1.319,00, máxima 1.320,00, mínima 1.313,75, fechamento **1.317,50**, volume **6.537 contratos**. Farelo (ticker ZMZ26.CBT, venc. dez/26): abertura 371,00, máxima 371,00, mínima 368,10, fechamento **368,10**, volume **1.676 contratos** — nota que abertura=máxima e mínima=fechamento, ou seja, a sessão inteira registrada é uma reta descendente sem nenhum repique de volta, um padrão tipicamente associado a captura parcial/intradiária, não a um pregão completo. Óleo (ticker ZLZ26.CBT, venc. dez/26): abertura 68,00, máxima 68,18, mínima 67,79, fechamento **68,12**, volume **1.743 contratos**
  - Curva futura em 28/09 — soja: nov/26 (base) 1.317,50 → jan/27 1.330,75 → mar/27 1.338,25 → mai/27 1.345,25 → jul/27 1.350,75 (contango regular, +2,52% da base a jul/27); farelo: out/26 371,90 → dez/26 (base) 368,10 → jan/27 367,40 → mar/27 366,30 → mai/27 366,30 (backwardation, -0,49% de dez/26 a mai/27, e out/26 com prêmio de +1,03% sobre dez/26 — a curva de farelo mais próxima segue precificando aperto físico de curtíssimo prazo, mesmo com o ratio recuando); óleo: out/26 67,54 → dez/26 (base) 68,12 → jan/27 68,32 → mar/27 68,55 → mai/27 68,71 (contango regular, +0,87% de dez/26 a mai/27)
  - CME NYMEX heating oil (HO=F) — sessão de **2026-09-28**: abertura 4,5891, máxima 4,6075, mínima 4,5100, fechamento **4,5327**, volume **3.054 contratos**. Comparado à sessão de **2026-09-27** no mesmo dump (abertura 4,5891, máxima 4,6075, mínima 4,5100, fechamento 4,5561, volume 2.411): abertura, máxima e mínima são **idênticas, casa decimal por casa decimal**, entre os dois dias — só o fechamento (-0,51%) e o volume (+26,7%) mudam. É o mesmo padrão de OHLC duplicado já documentado três vezes em [[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]] e reencontrado em [[2026-09-24_correcao-numeros-sessao-23set-fim-do-artefato-de-baixa-liquidez]], agora numa quarta ocorrência
  - Indicadores sintéticos internos (`indicators`), sessão de 28/09: ratio Far/Soj **83,82%** (farelo 368,10/sht ÷ (soja 1.317,50cts × 33,33)); oil share **48,06%** (valor óleo 7,49 / total 15,59); crush margin **US$2,4164/bushel** (farelo 368,10 + óleo 68,12 − soja 1.317,50); oil-meal spread **-0,605 USD/bushel**; paridade BR da soja **R$151,01/saca** (CBOT 1.317,50 × USD/BRL 5,1991 — PTAX ainda a de sexta-feira 25/09, sem cotação nova hoje); margem de biodiesel US **US$1,7887/galão** (receita 7,6977 [HO 4,53 + 1,5×RIN 2,11] − custo 5,9087 [óleo 5,109 + industrial 0,80]); ISF (Índice de Sobra de Farelo) e ISO (Índice de Suporte do Óleo) seguem em 60/100 e 80/100, carimbo repetido também em 28/09. Série do ratio Far/Soj 24-28/09 (dias já fechados, sem revisão nesta janela): **84,80% (pico, 24/09)** → 84,38% (25/09) → **83,82% (28/09, segundo recuo seguido, -0,56 p.p. hoje e -0,98 p.p. desde o pico)**; oil share na mesma janela: 47,56% (24/09) → 47,76% (25/09) → **48,06% (28/09, nova máxima da janela)**; oil-meal spread: -0,7623 (24/09) → -0,6996 (25/09) → **-0,605 (28/09, terceira melhora seguida para o óleo)**
  - BCB PTAX — sem cotação nova: a mais recente segue sendo **2026-09-25**, USD/BRL **5,1991**, EUR/BRL 5,928, Selic diária 0,050788% a.a. (séries SGS 1, 21619, 11) — três dias corridos sem atualização (sábado, domingo e a própria segunda-feira 28/09, cujo dump foi aparentemente gerado antes da publicação da PTAX do dia)
  - CEPEA/ESALQ Soja Paranaguá (via NAG) e NAG físico BR (`nag_fisico`) — sem leitura nova: os últimos valores seguem sendo os de **2026-09-25** (Paranaguá R$161,00/saca; Paraná interior R$154,38/saca; farelo Mato Grosso/IMEA R$1.996,41/ton; farelo Rondonópolis/MT R$2.200,00/ton; farelo média RS R$2.130,00/ton; prêmio export farelo Paranaguá 0,12 USD/short_ton; prêmio export óleo Paranaguá 0,1 cts/lb, ambos congelados desde 08/09, agora **20 dias corridos**). Cruzando o físico ainda de sexta com a paridade recalculada de hoje (R$151,01/saca) dá um basis nominal de **R$9,99/saca** — número que mistura um preço físico de três dias atrás com uma paridade de hoje, portanto tratado aqui apenas como referência aproximada, não como basis real do dia (ver Honestidade)
  - CFTC COT Managed Money — sem corte novo: o mais recente segue sendo o de **2026-09-22**, agora com **6 dias corridos de idade** — farelo net long 191.087 contratos (+4,36% vs 15/09); óleo net long 92.137 (-9,21%); soja net long 265.159 (+9,80%). Próximo corte esperado para posições de 29/09, a publicar por volta de 02/10
  - USDA Crop Progress — sem corte novo: ainda o de **2026-09-20** (agora **8 dias de idade**), 12% excelente / 46% boa (G/E 58%), 10% pobre, colheita 12% concluída; a janela de "por volta de 27-28/09" citada nas duas últimas leituras como data provável do próximo corte já passou sem que o dado aparecesse
  - USDA WASDE — **ausente do dump pela terceira leitura seguida**
  - NOPA — item de fila `release-nopa-2026-09-28`: `monthly_status` em 0,0 bool, mesmo padrão de paywall de todas as leituras desde o início deste monitoramento
  - ABIOVE projeções mensais — balanços out-dez/2026, sem revisão frente à leitura anterior: produção de farelo BR caindo 2.142,97 (out) → 1.977,59 (nov) → 1.659,04 (dez) mil t; exportação de farelo BR caindo 850 → 800 → 700 mil t; estoque final de soja BR caindo 5.720,77 (out) → 3.658,99 (nov) → 1.889,91 (dez) mil t
  - Notícias Agrícolas/Canal Rural/Farm Progress (RSS) — a manchete mais recente com corpo de texto é de **2026-09-27** (Canal Rural: "Trump e Xi no radar: soja fica à espera de mudanças que podem mexer com o comércio global"); contagem de itens de 28/09 registra 160 itens lidos e 3 mantidos (era 2 em 26 e 27/09)
  - NOAA CPC ENSO — El Niño Advisory, inalterado (carimbo 2026-09-28)
  - MPOB — carimbo 2026-09-28, parser sem números extraídos, página de 3.181 chars (mesmo tamanho desde 24/09)
  - INMET — previsão para **2026-09-28 (HOJE)**: calor no núcleo de Mato Grosso sobe mais um degrau frente a ontem — Cuiabá 42°C/26°C (era 41°C/25°C), Sinop e Sorriso 41°C/26°C e 40°C/26°C, Lucas do Rio Verde 41°C/26°C; Rio Verde/GO estável em 38°C/22°C; Cascavel/PR e Maringá/PR em 35°C, ambos com "pancadas de chuva e trovoadas" previstas; Passo Fundo/RS 22°C/16°C, também com pancadas de chuva e trovoadas previstas — mesmo padrão de calor forte no núcleo produtor + chuva prevista no sul já descrito ontem, coerente com o pano de fundo El Niño
  - system/tributario_watch.toml (lido como referência, não editado) — `atualizado_em` 2026-06-05 em todos os 10 eventos catalogados, **115 dias corridos** sem revisão humana frente a hoje (28/09)
  - Forecasts estatísticos internos (bandas 7d/30d) — geração de **2026-09-28**, sobre o fechamento de hoje, alvos 05/10 e 28/10: farelo "altista" nos dois horizontes; óleo "baixista" nos dois horizontes; soja "lateral" em 7d e "altista" em 30d — extrapolação estatística, não fundamentalista (ver Honestidade)
  - Fila de julgamento — 2026-09-28, 7 itens: `alerta-quebra_resistencia-soja_cbot-2026-09-28`, `alerta-quebra_suporte-oleo_cbot-2026-09-28`, `alerta-quebra_resistencia-farelo_cbot-2026-09-28`, `alerta-quebra_suporte-complexo_soja-2026-09-28`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`, `release-nopa-2026-09-28`
  - Cruza com [[2026-09-27_leitura-complexo]] (leitura anterior, base direta de comparação), [[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]] e [[2026-09-24_correcao-numeros-sessao-23set-fim-do-artefato-de-baixa-liquidez]] (documentação do padrão de dado provisório, agora numa nova ocorrência), [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (tese original do ratio) e [[2026-09-17_ratio-far-soj-supera-nivel-de-abertura-da-tese-original-quarta-sessao]] e [[2026-09-09_d90-ratio-far-soj-reverte-na-vespera]] (invalidação técnica já fechada da tese de junho)
status: ativa
vies: [bull-farelo, bull-soja, bear-oleo_soja]
---

## Visão geral

O complexo soja gira em torno do "crush" — o esmagamento industrial que transforma a soja em
grão em dois produtos com destinos econômicos diferentes: farelo (o resíduo proteico, quase
todo destinado a ração animal, principalmente aves e suínos) e óleo (usado em alimentação
humana e, cada vez mais, em biodiesel). Quem "paga a conta" do esmagamento — ou seja, qual dos
dois produtos concentra mais valor econômico e por isso comanda a decisão de esmagar mais ou
menos soja — é medido pelo "oil share": a fatia percentual do valor total gerado pelo crush que
vem do óleo. Quando o oil share sobe, é o óleo que sustenta a margem da indústria, e o farelo
tende a "sobrar" como subproduto que precisa ser escoado a qualquer preço; quando o oil share
cai, é o farelo que paga a conta, e ele fica relativamente mais valorizado. O termômetro direto
dessa disputa é o ratio Far/Soj — o preço do farelo dividido pelo da soja, em percentual: abaixo
de 80% o farelo está "abundante" (leitura baixista para farelo); entre 80% e 87%, zona "neutra";
acima de 87%, "apertado" (leitura altista para farelo).

**Hoje é a primeira sessão de mercado real desde sexta-feira 25/09** — sábado e domingo não têm
pregão, e a leitura de ontem (domingo) foi inteiramente dedicada a documentar como o fechamento
de sexta ainda estava sendo revisado três dias depois. A boa notícia é que hoje, finalmente, há
um movimento de preço genuíno para analisar: farelo caiu de 371,00 para **368,10** (-0,78%),
soja caiu de 1.319,00 para **1.317,50** (-0,11%) e óleo **subiu** de 67,84 para **68,12**
(+0,41%) — a primeira sessão desta janela de 14 dias em que óleo e farelo se movem em direções
opostas com folga (óleo sobe enquanto farelo cai). O efeito direto no crush é visível: o oil
share salta para **48,06%** (era 47,76% na sexta), a máxima de toda a janela observada, e o
ratio Far/Soj recua pela **segunda sessão consecutiva** desde o pico de 24/09 — de 84,80%
(pico) para 84,38% (25/09) e agora **83,82%** hoje, um recuo acumulado de quase um ponto
percentual (-0,98 p.p.) em apenas duas sessões de mercado. Na mesma direção, o oil-meal spread
(a diferença entre o valor do óleo e o do farelo, em bushel-equivalente) melhora pela terceira
sessão seguida para o lado do óleo: -0,7623 (24/09) → -0,6996 (25/09) → **-0,605** (hoje). Se
esse movimento se confirmar e persistir, é o primeiro sinal genuíno — não apenas um ruído de
revisão de dado — de que a "pausa" do ratio desde o pico de 24/09 pode estar virando reversão
de fato, o que reforçaria bear-óleo/farelo-relativo no curtíssimo prazo, mesmo que não mude
ainda o quadro estrutural que sustenta bull-farelo desde junho.

**Só que há um "mas" grande, e ele é o fio condutor desta leitura.** O volume de hoje é
anormalmente baixo nos três contratos — 6.537 contratos em soja, 1.676 em farelo e 1.743 em
óleo — contra os 105-140 mil contratos das sessões já revisadas e "confirmadas" desta mesma
janela (ex.: farelo em 25/09 fechou com 105.415 contratos depois de sucessivas revisões). Em
farelo, a sessão de hoje também tem a característica peculiar de abertura=máxima e
mínima=fechamento — ou seja, uma reta descendente sem nenhum repique registrado, um padrão
mais consistente com uma captura parcial de pregão do que com um dia inteiro de negociação. E
o heating oil (HO=F, o insumo que alimenta a margem de biodiesel americana) repete hoje, pela
quarta vez documentada nesta série, o padrão de abertura/máxima/mínima **idênticas, casa
decimal por casa decimal**, às da sessão anterior (27/09), com apenas o fechamento e o volume
mudando — exatamente o sintoma que precedeu, em três ocorrências anteriores
([[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]],
[[2026-09-24_correcao-numeros-sessao-23set-fim-do-artefato-de-baixa-liquidez]]), uma revisão
relevante de preço e uma correção de volume de mais de uma ordem de grandeza nos dias
seguintes. Isso não invalida o movimento de hoje — mas significa que a queda do ratio Far/Soj,
a alta do oil share e a melhora do oil-meal spread, por mais coerentes que sejam entre si, ainda
não podem ser tratadas como fato consolidado: a experiência recente deste monitoramento é que
exatamente este tipo de sessão (volume baixo, OHLC duplicado no insumo auxiliar) costuma ser
revisada, às vezes de forma a mudar o sinal da variação.

**Leitura de uma linha**: o pivô do complexo continua sendo o ratio Far/Soj, que hoje mostra o
primeiro indício de reversão real desde o pico de 24/09 (dois recuos seguidos, -0,98 p.p.
acumulado, com oil share em máxima da janela) — mas construído sobre uma sessão com volume 30 a
60 vezes menor do que o padrão de sessões já confirmadas e um heating oil com OHLC duplicado do
dia anterior, então a confirmação real só vem no dump de amanhã. Bull-farelo, bull-soja e
bear-óleo seguem mantidos nesta leitura porque nenhum dos pilares estruturais (física BR,
ABIOVE, COT de 22/09, técnico) mudou — mas a convicção no farelo e no óleo, especificamente,
está mais baixa hoje do que ontem, por causa da qualidade do dado, não por causa de um fato
novo de mercado. Confiança: média para soja e farelo (pilares estruturais intactos, mas sessão
do dia não confirmada), baixa para a leitura direcional específica de hoje em farelo/óleo (ver
Honestidade). Trata as quatro quebras técnicas da fila
(`alerta-quebra_resistencia-soja_cbot-2026-09-28`, `alerta-quebra_suporte-oleo_cbot-2026-09-28`,
`alerta-quebra_resistencia-farelo_cbot-2026-09-28`, `alerta-quebra_suporte-complexo_soja-2026-09-28`)
nas seções abaixo; as duas revisões "vencidas" da tese de junho
(`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` e `-D+90`) na seção
Farelo, ambas já fechadas desde 17/09; e o release de NOPA (`release-nopa-2026-09-28`) na seção
Honestidade, mais uma vez sem dado real por trás do paywall.

## Soja

**Viés: bull, mantido — a sessão de hoje é uma queda pequena (-0,11%) que, mesmo sem o desconto
de qualidade de dado, não seria suficiente para mudar a leitura técnica ou de posicionamento;
com o desconto, é ruído dentro da margem de incerteza da própria captura.**

O que sustenta a tese:

- **O corte de COT de 22/09 (CFTC, ainda o mais recente, agora com 6 dias corridos de idade)
  mostra os fundos com net long em soja de 265.159 contratos, alta de +9,80% frente aos
  241.501 de 15/09** — a reversão de convicção dos fundos já tratada em profundidade nas
  leituras anteriores, sem corte mais novo hoje para confirmar se persiste. A composição:
  managed money long subiu +6,43% (para 300.742) e o short caiu -13,38% (para 35.583); os
  produtores ampliaram o short em +2,24% (para 650.281) — coerente com mais originação/venda
  física à medida que a colheita americana avança (12% concluída em 20/09, USDA Crop
  Progress, corte agora com 8 dias de idade, sem atualização apesar de a janela "27-28/09" já
  ter passado).
- **A soja fechou hoje em 1.317,50, folgadamente acima da resistência de referência de
  1.180,00** (fila `alerta-quebra_resistencia-soja_cbot-2026-09-28`) — uma folga de
  **+11,65%**, praticamente igual à folga de +11,78% de sexta-feira; a queda de -0,11% no dia
  não muda a leitura técnica em nada relevante.
- **A paridade em reais da soja recalcula para R$151,01/saca hoje** (CBOT 1.317,50 × USD/BRL
  5,1991, PTAX ainda de sexta-feira, sem cotação nova) — queda de -0,11% frente aos R$151,18
  de sexta, inteiramente explicada pela variação do CBOT, já que o câmbio não teve leitura
  nova.
- **A curva futura permanece em contango regular**: nov/26 (base) 1.317,50 → jan/27 1.330,75
  → mar/27 1.338,25 → mai/27 1.345,25 → jul/27 1.350,75 (+2,52% da base a jul/27) — o mercado
  a termo segue precificando preços mais altos à frente, sem sinal de reprecificação de baixa.
- **A manchete mais recente do noticiário (Canal Rural, 27/09) coloca o comércio EUA-China no
  radar** — "Trump e Xi no radar: soja fica à espera de mudanças que podem mexer com o
  comércio global" — sem detalhamento numérico no corpo capturado pelo RSS, mas um lembrete de
  que o canal de exportação para a China segue sendo o principal vetor de risco/upside
  bilateral não capturado por nenhum indicador quantitativo deste briefing.

**O que invalida / risco:**

- **O basis físico em Paranaguá não pôde ser recalculado de forma limpa hoje**: a última
  leitura de preço físico (CEPEA/ESALQ Paranaguá) é de sexta-feira, R$161,00/saca, e cruzá-la
  com a paridade de hoje (R$151,01/saca) dá um basis nominal de R$9,99/saca — mas essa conta
  mistura um preço físico de três dias atrás com uma paridade calculada sobre o fechamento de
  hoje, então não deve ser lida como o basis real do dia (ver Honestidade). A compressão
  genuína do basis (documentada nas leituras anteriores, caindo de R$11,40/saca em 24/09 para
  R$9,82/saca em 25/09) segue sem confirmação de continuidade.
- **O WASDE segue ausente do dump pela terceira leitura seguida** — sem esse insumo, a leitura
  de soja e farelo fica mais dependente de COT e técnico, e menos de fundamento de balanço
  direto (ver Honestidade).
- **O regime de El Niño (NOAA CPC, inalterado) segue associado a chuvas acima da média no sul
  do Brasil**, e o boletim do INMET de hoje mantém a previsão de "pancadas de chuva e
  trovoadas" em Passo Fundo/RS pela segunda leitura seguida — um vetor de médio prazo que
  tende a favorecer a produtividade da safra brasileira 2026/27, pesando contra qualquer tese
  de escassez estrutural de soja no horizonte à frente.
- **Nível técnico a vigiar:** um fechamento de volta abaixo de 1.180 desfaria formalmente o
  rompimento; com a folga em +11,65%, esse cenário segue distante.
- **A própria sessão de hoje pode ser revisada amanhã** — dado o volume anormalmente baixo
  (6.537 contratos, ordem de grandeza de sessão "provisória" nesta série, não de sessão
  "confirmada"), o fechamento de 1.317,50 deve ser tratado como preliminar.

**Leitura operacional:** a queda de -0,11% de hoje não é, por si só, motivo para alterar
posição — a tese segue apoiada na reversão de convicção dos fundos (COT de 22/09) e na
paridade em reais, com o nível técnico de 1.180 como referência de invalidação distante. Para
quem está comprado, manter ou ampliar a posição estrutural segue fazendo sentido; para quem
opera vendido, a compressão do basis físico (ainda não confirmada com dado fresco) e o regime
de El Niño seguem sendo os únicos argumentos disponíveis, nenhum deles um gatilho técnico
imediato. O corte de COT de posições de 29/09 (esperado por volta de 02/10) é o próximo evento
capaz de confirmar se a reversão de convicção dos fundos continua.

## Farelo

**Viés: bull, mantido — mas esta é a leitura de farelo com a convicção mais baixa desde que o
ratio Far/Soj rompeu a zona apertada em setembro: o segundo recuo consecutivo do ratio desde o
pico de 24/09 é o primeiro sinal de reversão real (não apenas revisão de dado) desta janela,
mesmo que os pilares estruturais (física BR, ABIOVE, COT) ainda não tenham mudado.**

O que sustenta a tese:

- **A confirmação física no Brasil segue tripla e sem mudança** (última leitura ainda de
  sexta-feira, sem publicação de praça neste início de semana no dump de hoje): farelo
  Rondonópolis/MT (BCSP) em R$2.200,00/ton; farelo média Rio Grande do Sul (Clicmercado) em
  R$2.130,00/ton; farelo Mato Grosso/IMEA em R$1.996,41/ton — os três níveis físicos que
  sustentam a tese de aperto doméstico seguem intactos, ainda que sem atualização hoje.
- **O farelo fechou (versão de hoje) em 368,10, folgadamente acima da resistência histórica de
  325,00** (fila `alerta-quebra_resistencia-farelo_cbot-2026-09-28`), folga de **+13,26%** —
  menor do que a folga de +14,15% de sexta-feira, já que o fechamento de hoje caiu -0,78% frente
  à sexta, mas ainda uma folga ampla.
- **A trajetória sazonal da ABIOVE para o Brasil continua apontando para alívio de oferta
  doméstica de farelo à frente**, sem revisão nesta janela: produção projetada caindo de
  2.142,97 mil t (out/26) para 1.977,59 (nov/26) e 1.659,04 mil t (dez/26); exportação de 850
  para 800 e 700 mil t no mesmo período — menos farelo brasileiro disponível para exportar nos
  próximos meses é, estruturalmente, um vetor de suporte de médio prazo ao preço relativo do
  farelo.
- **O COT de 22/09 (ainda o mais recente) mostra os fundos com net long em farelo de 191.087
  contratos, alta de +4,36% frente a 15/09**, sem novidade hoje por falta de corte mais
  recente.
- **A curva futura de curtíssimo prazo (out/26 371,90) segue com prêmio sobre a base de
  dez/26 (368,10, +1,03%)** — o mercado a termo mais próximo ainda paga um pequeno prêmio pelo
  farelo de entrega mais imediata, coerente com aperto físico de curto prazo, mesmo com o
  ratio recuando.
- **A revisão `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` e a
  `-D+90`, listadas como "vencidas" na fila de hoje, seguem com veredito já fechado**: o ratio
  ultrapassou o nível de abertura da tese original (81,4% em 11/06/2026,
  [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]) desde
  [[2026-09-17_ratio-far-soj-supera-nivel-de-abertura-da-tese-original-quarta-sessao]], e a
  revisão de D+90 já foi formalizada em
  [[2026-09-09_d90-ratio-far-soj-reverte-na-vespera]]. Mesmo com o ratio de hoje (83,82%) mais
  próximo do nível de abertura de junho do que em qualquer outra sessão desde 17/09, ele ainda
  fica **+2,42 pontos percentuais acima** dos 81,4% originais — nenhuma ação nova é necessária
  sobre essas duas revisões específicas; resta em aberto apenas o marco de D+180, programado
  para 2026-12-08 (71 dias à frente).

**O que invalida / risco — o item mais importante de hoje:**

- **O ratio Far/Soj recua pela segunda sessão consecutiva desde o pico de 24/09**: 84,80%
  (pico) → 84,38% (25/09) → **83,82% (hoje)**, um recuo acumulado de -0,98 ponto percentual em
  duas sessões de mercado — o maior recuo de dois dias observado desde que o ratio começou a
  subir estruturalmente em agosto/setembro. Isso ainda deixa o ratio dentro da zona neutra
  (80-87%), agora a 3,18 pontos do teto "apertado" e apenas 3,82 pontos do piso "abundante" —
  ou seja, mais próximo do centro da banda neutra do que em qualquer sessão desde o início de
  setembro. Se esse recuo continuar por mais 2-3 sessões, a leitura bull-farelo desta série
  precisará ser reavaliada com mais rigor.
- **O oil share salta para 48,06% hoje, a máxima de toda a janela de 14 dias observada**
  (contra 47,56% na mínima de 24/09) — o espelho exato do recuo do ratio: o óleo está, pela
  primeira vez nesta janela, capturando mais da metade relativa do valor incremental do crush
  no dia a dia, o que tende a reduzir a pressão para o farelo "sobrar" no curtíssimo prazo.
- **O oil-meal spread melhora pela terceira sessão seguida para o lado do óleo**: -0,7623
  (24/09) → -0,6996 (25/09) → **-0,605 (hoje)** — uma tendência mais persistente do que um
  ponto isolado, e o principal contraponto quantitativo à tese bull-farelo nesta leitura.
- **Mas todo esse movimento vem de uma sessão com volume de apenas 1.676 contratos em farelo**
  — uma ordem de grandeza abaixo dos 105-140 mil contratos das sessões já confirmadas nesta
  mesma janela — **e com abertura=máxima e mínima=fechamento**, ou seja, sem nenhum repique
  registrado ao longo do dia. Esse é exatamente o tipo de sessão que, no histórico recente
  deste monitoramento, tende a ser revisada (às vezes invertendo o sinal da variação, como
  ocorreu em [[2026-09-24_correcao-numeros-sessao-23set-fim-do-artefato-de-baixa-liquidez]]).
  A leitura bear para o ratio de hoje deve, portanto, ser tratada como preliminar.
- **A curva futura de médio prazo segue em backwardation**: dez/26 (base) 368,10 → jan/27
  367,40 → mar/27 366,30 → mai/27 366,30 (-0,49% de dez/26 a mai/27) — o mercado a termo segue
  sem precificar um aperto estrutural que se estenda muito além do curtíssimo prazo.
- **O prêmio de exportação de farelo em Paranaguá segue congelado em 0,12 USD/short_ton há 20
  dias corridos** (desde 08/09) — se o aperto físico doméstico fosse amplo e sustentado a
  ponto de pressionar também o canal de exportação, seria razoável esperar, eventualmente,
  algum reflexo no FOB; essa confirmação ainda não apareceu.
- **Os índices sintéticos ISF e ISO seguem travados em 60/100 e 80/100**, agora **17 dias
  corridos** sem qualquer reação desde 11/09, apesar de o ratio e o oil share terem se movido
  de forma expressiva nesse período — mais um sinal de que esses índices compostos reagem com
  defasagem grande a movimentos de preço.

**Leitura operacional:** a tendência de fundo (física BR ainda intacta, embora sem atualização
hoje; ratio ainda a 3,18 pontos do teto "apertado"; COT de 22/09 ainda comprador; ABIOVE
sazonal favorável) segue justificando manter posição comprada em farelo ou no spread Far/Soj —
mas hoje é o primeiro dia em que a recomendação vem com uma ressalva explícita de tamanho: o
recuo do ratio por dois dias seguidos, mesmo que a segunda perna venha de dado ainda não
confirmado, é o tipo de sinal que merece redução de tamanho de posição nova (não liquidação da
posição estrutural) até a sessão de amanhã confirmar se o recuo persiste com volume saudável.
Para quem está vendido no farelo ou no spread, hoje é o primeiro dia desta janela em que o
argumento técnico de curto prazo (ratio recuando, oil share subindo, oil-meal melhorando) tem
alguma tração — mas apoiado num dado que a própria leitura de hoje trata como preliminar.

## Óleo

**Viés: bear, mantido — mas com o contraponto mais forte desta janela: pela primeira vez em
14 dias, óleo fecha em alta (+0,41%) no mesmo dia em que farelo cai, o oil share atinge máxima
da janela e o oil-meal spread melhora pela terceira sessão seguida, tudo a favor do óleo — só
que construído sobre a mesma sessão de baixo volume que pesa sobre a leitura de farelo.**

O que sustenta a tese:

- **O corte de COT de 22/09 (ainda o mais recente, agora 6 dias de idade) mostra os fundos com
  net long em óleo de 92.137 contratos, queda de -9,21% frente aos 101.480 de 15/09** — o maior
  movimento relativo de redução de convicção entre as três pernas do complexo nesta rodada de
  COT, e ainda o dado de posicionamento mais forte a favor da tese bear, sem corte mais recente
  para confirmar se a tendência de corte continuou na semana de 22-26/09.
- **Óleo fechou hoje em 68,12, abaixo do suporte de referência de 72,00** (fila
  `alerta-quebra_suporte-oleo_cbot-2026-09-28`), distância de **-5,39%** — ligeiramente menor
  (mais próxima do suporte) do que a distância de -5,78% de sexta, já que o preço subiu
  +0,41% no dia, mas ainda tecnicamente abaixo do nível rompido.
- **O ISO (Índice de Suporte do Óleo) segue em 80/100**, sem melhora, carimbo repetido em
  28/09.
- **O forecast estatístico interno segue em "baixista" nos dois horizontes (7d e 30d)** —
  extrapolação de tendência, não fundamentalista.
- **A lente fiscal brasileira segue estruturalmente desfavorável, sem mudança hoje**: a MP
  1.363/2026 (subvenção ao diesel fóssil, vigente até 31/12/2026) segue plenamente vigente; a
  isenção de PIS/Cofins do biodiesel na mistura está agora **59 dias corridos vencida**
  (vigência até 31/07/2026) sem sinal de renovação (ver Lente fiscal/regulatória BR).

**O que sustenta um contraponto — reforçado hoje, mas com ressalva de dado:**

- **O oil share salta para 48,06% hoje, a máxima da janela de 14 dias**, e o oil-meal spread
  melhora pela terceira sessão seguida (-0,7623 → -0,6996 → **-0,605**) — os dois indicadores
  de complexo que mais diretamente medem a força relativa do óleo dentro do crush apontam,
  hoje, na mesma direção altista para o óleo pela primeira vez de forma consistente nesta
  janela.
- **Óleo fechou em alta (+0,41%) no mesmo dia em que farelo caiu -0,78%** — a primeira vez
  nesta janela de 14 dias em que as duas pernas se movem em direções opostas com folga
  perceptível, em vez de subir ou cair juntas puxadas pelo movimento geral da soja.
- **A margem de biodiesel americana calculada para hoje é de US$1,7887/galão**, queda de
  -8,82% frente aos US$1,9617 de sexta-feira — mas essa queda vem inteiramente do heating oil
  (HO=F), cujo fechamento de hoje (4,5327) tem abertura, máxima e mínima **idênticas** às da
  sessão de ontem (27/09, 4,5891/4,6075/4,5100) — o quarto caso documentado nesta série do
  padrão de OHLC duplicado que precedeu revisões relevantes em três ocorrências anteriores
  ([[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]],
  [[2026-09-24_correcao-numeros-sessao-23set-fim-do-artefato-de-baixa-liquidez]]). Esta queda
  de margem, portanto, deve ser tratada como o dado mais frágil de toda a leitura de hoje — não
  porque a direção esteja necessariamente errada, mas porque o insumo que a gera já mudou de
  valor de fechamento três vezes para uma única sessão em ocorrências anteriores.
- **O RIN D4 (crédito de biocombustível renovável americano) permanece constante na fórmula
  interna** — toda a variação de margem, nesta e nas leituras anteriores, vem do heating oil,
  cuja instabilidade de captura é o problema, não uma mudança de política.
- **A curva futura de médio prazo segue em contango regular**: out/26 67,54 → dez/26 (base)
  68,12 → jan/27 68,32 → mar/27 68,55 → mai/27 68,71 (+0,87% de dez/26 a mai/27) — sem sinal de
  reprecificação estrutural de baixa no médio prazo.
- **Catalisadores de alta represados, ainda não correntes**: B16 segue "adiado", resultado
  esperado por volta de novembro/2026; a centralização da exportação de palma pela Indonésia
  via Danantara, que tinha alvo de assunção plena em 01/09/2026, já soma **27 dias** de atraso
  sem confirmação — ambos seguem como upside represado, não corrente.

**Leitura operacional:** o quadro técnico (abaixo do suporte de 72,00) e o COT (o corte mais
agressivo de net long das três pernas) seguem sustentando o lado vendido direcional — mas hoje
é o primeiro dia desta janela em que os indicadores de complexo (oil share, oil-meal spread) e
o próprio preço se movem consistentemente contra a tese bear, não a favor dela. Para quem está
vendido, a recomendação é manter a posição apoiada no técnico e no COT (nenhum dos dois mudou
hoje), mas não adicionar posição nova só com base no quadro de hoje, e vigiar de perto se o
oil share e o oil-meal spread confirmam a força do óleo amanhã com volume saudável. Para quem
está comprado ou avalia entrar, hoje é o dia com o argumento mais forte a favor de uma pausa
na tese bear desde que este monitoramento começou a acompanhar o ratio Far/Soj de perto — ainda
que apoiado, em parte, num heating oil cuja confiabilidade de captura segue sendo o ponto mais
fraco de toda a leitura. Para quem opera o spread farelo-óleo dentro do crush, hoje é o
primeiro dia em que vale considerar reduzir exposição comprada no spread (farelo vs. óleo) até
a confirmação de amanhã, dado que os três indicadores relevantes (ratio, oil share, oil-meal
spread) se moveram juntos contra essa posição.

## Spreads e crush (leitura de complexo)

O ratio Far/Soj, recalculado hoje, mostra o segundo recuo consecutivo desde o pico de 24/09:
83,22% (21/09) → 83,90% (22/09) → 84,36% (23/09) → **84,80% (pico, 24/09)** → 84,38% (25/09) →
**83,82% (hoje, -0,56 p.p. no dia e -0,98 p.p. desde o pico)** — ainda dentro da zona neutra
(80-87%), agora a 3,18 pontos percentuais do teto "apertado" e 3,82 pontos do piso "abundante",
mais perto do centro da banda do que em qualquer sessão desde o início de setembro. O oil share
espelha o mesmo movimento na direção oposta: mínima de 47,56% em 24/09, subindo para 47,76% em
25/09 e agora **48,06% hoje**, a máxima de toda a janela. O crush margin recalcula para
**US$2,4164/bushel** (era US$2,4344 na sexta, -0,74%), ainda abaixo do piso de referência de
US$2,50 monitorado pela fila (`alerta-quebra_suporte-complexo_soja-2026-09-28`, distância agora
de **-3,34%**, maior do que os -2,62% de sexta-feira — o crush está, hoje, mais comprimido, não
menos, apesar de o ratio estar recuando, porque a queda de farelo pesa mais no crush do que a
alta de óleo).

**A leitura de complexo mais importante de hoje é que, pela primeira vez nesta janela, três
indicadores independentes (ratio Far/Soj, oil share, oil-meal spread) se movem de forma
coerente e simultânea a favor do óleo e contra o farelo, numa sessão de mercado real (não um
fim de semana sem pregão).** Isso é qualitativamente diferente das oscilações de décimos de
ponto percentual vistas em sessões anteriores, que eram, em grande parte, ruído de revisão de
dado sobre um mesmo dia. Mas a sessão que produz esse sinal tem volume 30 a 60 vezes menor do
que as sessões já confirmadas desta mesma janela, farelo com um padrão de reta descendente sem
repique (abertura=máxima, mínima=fechamento) e o heating oil repetindo pela quarta vez o padrão
de OHLC duplicado que precedeu revisões relevantes em ocorrências anteriores
([[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]],
[[2026-09-24_correcao-numeros-sessao-23set-fim-do-artefato-de-baixa-liquidez]]). A leitura mais
honesta possível é: o sinal é real o suficiente para justificar cautela tática (reduzir
posições novas no spread Far/Soj, não liquidar a posição estrutural), mas não é ainda um sinal
confirmado o suficiente para virar a tese estrutural de bull-farelo/bear-óleo que vem sendo
sustentada por física BR, ABIOVE e COT desde antes desta sessão.

O COT de 22/09, ainda o dado de posicionamento mais recente seis dias depois, retrata os fundos
com net long ampliado em farelo (+4,36%) e soja (+9,80%) e reduzido em óleo (-9,21%) — sem
novidade hoje, e ainda o alinhamento de posicionamento mais coerente com a tese estrutural
já descrita nesta série, mesmo que o preço do dia tenha se movido na direção oposta à do óleo
nessa foto de posicionamento. Os dois índices compostos por contagem de condições — ISF
(60/100) e ISO (80/100) — seguem travados no mesmo patamar desde 11/09, agora **17 dias
corridos** sem qualquer reação, apesar de o ratio e o oil share terem se movido de forma
expressiva nesse período — um lembrete de que esses índices sintéticos reagem com defasagem
grande, e não devem ser usados como gatilho de curtíssimo prazo.

## Lente fiscal/regulatória BR

Antes de fechar qualquer tese de preço BR, os vetores tributários/regulatórios vivos que pesam
no complexo — todos do `system/tributario_watch.toml`, cujo carimbo mais recente
(`atualizado_em`) em todos os 10 eventos catalogados é 2026-06-05, ou seja, **115 dias corridos
sem revisão humana** frente a hoje (28/09):

- **MP 1.363/2026** (id `MP-1363-2026`, subvenção diesel fóssil R$1,12/L, vigente até
  31/12/2026): barateia o diesel fóssil no mix B15 (mistura obrigatória de 15% de biodiesel),
  reduzindo a competitividade relativa do biodiesel e a demanda doméstica por óleo de soja —
  vetor estrutural de baixa para óleo, plenamente vigente, sem mudança de status.
- **B16 (id `B16-CNPE-2026`, elevação da mistura obrigatória de biodiesel para 16%)** segue
  "adiado", resultado esperado por volta de novembro/2026. Upside represado (~436 mil
  toneladas de demanda potencial adicional de óleo), não corrente — e, se confirmado, é
  justamente o tipo de catalisador que poderia inverter de vez a leitura de oil share que hoje
  aponta para cima por razões de mercado internacional (heating oil, biodiesel US), não por
  demanda doméstica brasileira ainda.
- **Isenção de PIS/Cofins do biodiesel na mistura** (id `PISCOFINS-BIODIESEL-ISENCAO`):
  vigência registrada até 31/07/2026 — já **59 dias corridos vencida** frente a 28/09/2026,
  sem registro de prorrogação ou expiração.
- **MP 1.358/2026** (subvenção gasolina R$0,89/L): vigência registrada até 11/07/2026, agora
  **79 dias corridos vencida**.
- **STJ REsp 2.165.276** (id `STJ-RESP-2165276`, crédito de PIS/Cofins sobre soja em biodiesel,
  direção "alta" para soja/óleo): sem novidade nesta janela.
- **EPA RFS 2026/2027** (id `EPA-RFS-2026-2027`, mandato de biocombustível americano, direção
  "alta" para óleo): sustenta o RIN D4, estável, e o RIN permanece constante na fórmula interna
  de margem de biodiesel — a queda de margem observada hoje vem inteiramente do heating oil
  (ainda sob suspeita de dado provisório, ver Honestidade), não de mudança regulatória.
- **Crédito 45Z** (id `45Z-CLEAN-FUEL`, em tramitação, direção "mista"): sem novidade.
- **Indonésia — Danantara** (id `DANANTARA-INDONESIA`) e **levy de exportação PMK 9/2026** (id
  `INDONESIA-LEVY-PMK9`): a assunção plena da centralização da exportação de palma pela
  Indonésia tinha alvo 01/09/2026 — já se passaram **27 dias** sem confirmação. Catalisador de
  alta represado para óleo (via substituição com palma) — ainda sem dado de MPOB disponível
  para monitorar diretamente (parser continua quebrado, ver Honestidade).
- **Indonésia B50** (id `INDONESIA-B50`, monitorando, direção "alta"): sem novidade.

Nenhum desses vetores muda a leitura de preço de hoje isoladamente — mas, em conjunto, eles
seguem reforçando a mesma assimetria já descrita em leituras anteriores: o mercado interno
brasileiro tem múltiplos desincentivos correntes ao óleo (MP 1.363 plenamente vigente, isenção
PIS/Cofins já 59 dias vencida) e múltiplos catalisadores de alta represados, não correntes
(B16, Danantara, B50). O movimento de hoje a favor do óleo (oil share, oil-meal spread) vem
inteiramente de fatores de mercado internacional (heating oil, biodiesel americano), não de
qualquer mudança nesse quadro fiscal brasileiro — que segue, sem exceção, desfavorável ao óleo
doméstico. A lacuna de 115 dias sem revisão humana do catálogo tributário segue sendo, em si,
um risco operacional recorrente: qualquer um destes vetores pode ter mudado de status na
realidade sem que este sistema tenha como saber.

## Riscos e eventos próximos

- **O item mais importante a monitorar amanhã: se a sessão de hoje (28/09) for revisada no
  dump de 29/09**, especialmente se a revisão inverter o sinal do movimento farelo-vs-óleo
  (como já ocorreu com a sessão de 23/09 em
  [[2026-09-24_correcao-numeros-sessao-23set-fim-do-artefato-de-baixa-liquidez]]) — isso seria
  decisivo para saber se o recuo do ratio Far/Soj de hoje é real ou artefato de captura.
- **Retorno de um heating oil (HO=F) com abertura/máxima/mínima estáveis entre gerações** —
  esta é a quarta ocorrência documentada do padrão de OHLC duplicado nesta série; ainda não há
  registro de uma sessão em que o padrão não tenha sido seguido de revisão de preço.
- **Próximo corte de COT** (posições de 29/09, esperado por volta de 02/10) — o próximo dado
  capaz de confirmar se a reversão de convicção em soja, o aumento em farelo e o corte em óleo
  da rodada de 22/09 continuaram na semana que já passou.
- **USDA Crop Progress**: a janela "por volta de 27-28/09" para o próximo corte já passou sem
  o dado aparecer — se não vier no próximo dump, vale investigar se houve mudança na
  cadência de publicação do USDA.
- **Retorno do WASDE ao dump** — ausente pela terceira leitura seguida.
- **Confirmação/atualização do basis físico em Paranaguá** — a última leitura física é de
  sexta-feira; a próxima publicação de praça (esperada ainda hoje ou amanhã) é necessária para
  recalcular o basis real, já que o cálculo de hoje mistura dias diferentes.
- **Nível técnico a vigiar em farelo:** volta abaixo de 325,00 desfaria o rompimento (folga
  atual +13,26%).
- **Nível técnico a vigiar em soja:** volta abaixo de 1.180,00 desfaria o rompimento (folga
  atual +11,65%).
- **Nível técnico a vigiar em óleo:** recuperação acima de 72,00 encerraria a leitura de
  suporte rompido (distância atual -5,39%, a menor desde que o suporte foi rompido).
- **Crush margin:** retorno acima de US$2,50/bushel encerraria a leitura de suporte rompido
  monitorada pela fila (distância atual -3,34%, mais comprimida do que sexta-feira).
- **Prêmio de exportação de farelo e óleo em Paranaguá**, congelado há 20 dias corridos.
- **NOPA mensal**: mais um "release" sem dado novo de fato (paywall), agora referenciado como
  `release-nopa-2026-09-28`.
- **Confirmação da centralização plena da exportação de palma pela Danantara** — alvo 01/09,
  já 27 dias passados sem confirmação.
- **Vigência da isenção PIS/Cofins do biodiesel** (59 dias vencida) e **MP 1.358/2026 da
  gasolina** (79 dias vencidos) — checar notícia de renovação/expiração.
- **Marco de 115 dias sem revisão humana do `tributario_watch.toml`**.
- **Revisão de D+180 da tese original do ratio Far/Soj**, programada para 2026-12-08 (71 dias
  à frente) — o recuo do ratio de hoje é o primeiro movimento desta janela que, se persistir,
  aproximaria essa revisão de um veredito mais cedo do que o esperado.
- **Persistência da chuva prevista em Cascavel/PR, Maringá/PR e Passo Fundo/RS** — segunda
  leitura seguida com menção efetiva de pancada de chuva (não só "possibilidade").

## Honestidade

- **O achado central desta leitura é que o movimento de preço de hoje — o mais coerente e
  potencialmente mais importante desta janela para a tese farelo-vs-óleo — vem de uma sessão
  com fortes indícios de captura parcial, não de um pregão completo.** O volume é 30 a 60 vezes
  menor do que o das sessões já confirmadas (soja 6.537 vs. ~117-140 mil; farelo 1.676 vs.
  ~89-105 mil; óleo 1.743 vs. ~88-89 mil), farelo fecha com abertura=máxima e mínima=fechamento
  (reta descendente sem repique), e o heating oil repete pela quarta vez documentada nesta
  série o padrão de abertura/máxima/mínima idênticas à sessão anterior. Nas três ocorrências
  anteriores desse padrão de HO=F, e na ocorrência análoga de farelo/soja/óleo em 23/09
  ([[2026-09-24_correcao-numeros-sessao-23set-fim-do-artefato-de-baixa-liquidez]]), a geração
  seguinte do dump revisou o preço (às vezes invertendo o sinal da variação) e corrigiu o
  volume em mais de uma ordem de grandeza. Não há garantia de que o mesmo ocorrerá desta vez,
  mas a probabilidade histórica dentro desta série é alta o suficiente para tratar toda a
  leitura direcional de hoje — especialmente a queda do ratio Far/Soj e a alta do oil share —
  como preliminar até o dump de amanhã confirmar ou revisar os números.
- **O basis físico de Paranaguá calculado nesta leitura (R$9,99/saca) mistura um preço físico
  de sexta-feira (25/09) com uma paridade calculada sobre o fechamento de hoje (28/09)** —
  não é uma medida limpa de basis do dia, e é apresentado apenas como referência aproximada.
- **A PTAX usada hoje (5,1991) é a de sexta-feira** — o dump de hoje não trouxe cotação nova de
  câmbio, possivelmente porque foi gerado antes da publicação do BCB para 28/09; toda conversão
  BRL desta leitura carrega essa defasagem.
- **A margem de biodiesel americana de hoje (US$1,7887/galão) depende do heating oil (HO=F)
  cujo OHLC está duplicado em relação a ontem** — a queda de -8,82% frente a sexta-feira deve
  ser tratada com a mesma cautela que a leitura de 27/09 já aplicou à revisão anterior deste
  mesmo insumo.
- **O WASDE segue ausente do dump pela terceira leitura consecutiva** — não está claro se é
  falha temporária de captura ou mudança na disponibilidade da fonte.
- **Percentil histórico de posicionamento COT não está disponível no briefing** — toda leitura
  de "fundos comprando/vendendo" nesta série usa variação absoluta semana a semana de
  contratos, não percentil histórico; não é possível dizer se o net long atual de farelo, soja
  ou óleo está em nível historicamente esticado ou ainda distante de extremos.
- **O item de fila `release-nopa-2026-09-28` é mais uma repetição sem dado novo** — o mesmo
  padrão de todas as leituras anteriores desde que este monitoramento começou (paywall,
  `monthly_status` em 0,0 bool).
- **`tributario_watch.toml` sem atualização há 115 dias corridos** — pelo menos dois vetores
  (isenção PIS/Cofins do biodiesel, MP 1.358/2026) já passaram da vigência registrada sem nota
  de renovação ou expiração.
- **A previsão do INMET para 28/09 é previsão meteorológica, não medição de precipitação ou
  temperatura real** — a menção a "pancadas de chuva e trovoadas" em Cascavel/PR, Maringá/PR e
  Passo Fundo/RS é indicativa do boletim, não confirmação de que o evento ocorreu ou ocorrerá.
- **MPOB (palma Malásia) segue com parser quebrado** — nenhum dado de produção/estoque de
  palma malaia disponível, o que impede monitorar diretamente o catalisador represado da
  centralização de exportação indonésia (Danantara).
- **Não há seção `bcba` (Argentina) neste dump** — nenhum dado direto de safra ou exportação
  argentina disponível, e ainda sem WASDE para consolidar indiretamente esse dado.
- **Os forecasts estatísticos internos (bandas 7d/30d) foram gerados hoje sobre o fechamento
  de 28/09 ora sob suspeita de captura parcial** — o viés "altista" em farelo e "baixista" em
  óleo (ambos horizontes) refletem extrapolação estatística de tendência (MA20 + volatilidade +
  slope), não uma reavaliação fundamentalista, e herdam a mesma incerteza do dado de origem.
- **Os índices ISF e ISO ganharam um carimbo em 2026-09-28 no dump de hoje**, repetindo os
  mesmos valores de 60/100 e 80/100 já vigentes desde 11/09 — tratado aqui como continuidade,
  não como confirmação nova.
- **A fila de julgamento volta a listar as revisões D+7 e D+90 da tese de 11/06 como
  "vencidas"** — o veredito de ambas já foi fechado em
  [[2026-09-17_ratio-far-soj-supera-nivel-de-abertura-da-tese-original-quarta-sessao]] e
  reafirmado em [[2026-09-09_d90-ratio-far-soj-reverte-na-vespera]]; o sistema de fila não lê de
  volta os insights publicados para marcar a revisão como encerrada. Nenhuma ação nova é
  necessária sobre essas duas revisões específicas.
- **Em resumo: esta é uma leitura com um sinal potencialmente importante (a primeira reversão
  coerente de três indicadores de complexo a favor do óleo em 14 dias), mas o sinal repousa
  inteiramente sobre uma sessão de mercado com as mesmas características que, em quatro
  ocorrências anteriores nesta série, precederam revisão de dado.** A recomendação operacional
  desta leitura reflete essa tensão: cautela tática, não mudança de tese estrutural.
