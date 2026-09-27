---
data: 2026-09-27
titulo: "Fim de semana sem sessão nova no CBOT, mas o dump de hoje entrega a TERCEIRA geração de números para a sessão de 25/09: farelo, óleo e soja mantêm abertura/máxima/mínima idênticas às da leitura de ontem, porém fechamento e volume mudam nos três contratos ao mesmo tempo (farelo 370,60→371,00; óleo 67,82→67,84; soja 1.320,00→1.319,00), recalculando o ratio Far/Soj de 84,23% para 84,38% — o recuo desde o pico de 24/09 (84,80%) fica menor do que a leitura de ontem registrou (0,42 p.p., não 0,57) — e revertendo parte da queda na margem de biodiesel americana (de US$1,8584 'confirmados' ontem para US$1,9617 hoje, a terceira cifra distinta para o mesmo dia, sobre um heating oil (HO=F) cuja abertura/máxima/mínima também mudaram de novo, não só o fechamento); o COT segue sem corte novo (ainda o de 22/09, agora com 5 dias de idade) e a fila repete as quatro quebras técnicas e o release pago da NOPA — mantendo bull-soja, bull-farelo e bear-óleo intactos na direção, com a lição de honestidade mais dura desta série até aqui: mesmo um dado já chamado de 'confirmado' numa leitura publicada pode mudar de novo na geração seguinte"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT — **sem sessão nova**: hoje é domingo (27/09) e o mercado não opera desde a sexta-feira 25/09; a última sessão do dump continua sendo a de **2026-09-25**, mas com números revisados pela TERCEIRA vez desde que essa sessão fechou (ver Honestidade). Versão atual (dump de hoje): soja (ticker ZSX26.CBT, venc. nov/26) abertura 1.317,50, máxima 1.320,50, mínima 1.297,50, fechamento **1.319,00**, volume **140.637 contratos**; farelo (ticker ZMZ26.CBT, venc. dez/26) abertura 370,70, máxima 372,40, mínima 365,00, fechamento **371,00** (campo `fechamento_Z26` do mesmo ticker bate exatamente, sem discrepância interna), volume **105.415 contratos**; óleo (ticker ZLZ26.CBT, venc. dez/26) abertura 67,55, máxima 67,89, mínima 66,65, fechamento **67,84**, volume **88.388 contratos**. Em todos os três contratos, abertura/máxima/mínima são **idênticas, casa decimal por casa decimal**, às usadas na leitura de ontem ([[2026-09-26_leitura-complexo]]) — só o fechamento e o volume mudaram, nos três ao mesmo tempo: soja 1.320,00→1.319,00 (−0,08%) com volume 180.479→140.637 (−22,1%); farelo 370,60→371,00 (+0,11%) com volume 94.390→105.415 (+11,7%); óleo 67,82→67,84 (+0,03%) com volume 99.658→88.388 (−11,3%)
  - CME CBOT — sessão de **2026-09-24**, sem mudança de preço frente à leitura de ontem (farelo abertura 369,00, máxima 376,90, mínima 368,00, fechamento 372,40), mas com o volume revisado de novo: **105.415 contratos** hoje, o mesmo número exato usado para a sessão de 25/09 no mesmo contrato (ver Honestidade) — coincidência que soma-se ao padrão já monitorado nesta série
  - Curva futura em 25/09 (dump de hoje) — soja: nov/26 (base) 1.319,00 → jan/27 1.332,50 → mar/27 1.339,50 → mai/27 1.346,25 → jul/27 1.350,75 (contango regular, praticamente idêntico ao de ontem); farelo: out/26 373,90 → dez/26 (base) 371,00 → jan/27 369,80 → mar/27 368,30 → mai/27 367,90 (backwardation suave, -0,84% de dez/26 a mai/27); óleo: out/26 67,26 → dez/26 (base) 67,84 → jan/27 68,05 → mar/27 68,26 → mai/27 68,43 (contango regular, +0,87% de dez/26 a mai/27)
  - CME NYMEX heating oil (HO=F) — sessão de **2026-09-25**, terceira versão distinta desde o fechamento: abertura **4,7850** (era 4,5700 na leitura de ontem), máxima **4,8433** (era 4,5961), mínima **4,5190** (era 4,3789), fechamento **4,6847** (era 4,5799, +2,29%), volume **33.058 contratos** (era 62.876, -47,4%) — desta vez a revisão atinge também abertura/máxima/mínima, não só o fechamento (ver Honestidade); sessão de **2026-09-24**: preço idêntico ao já revisado ontem (abertura 4,8289, máxima 5,0614, mínima 4,6687, fechamento 4,7303), mas volume revisado outra vez de 41.371 para **33.058 contratos** (-20,1%) — o mesmo valor de volume que aparece hoje para 25/09
  - Indicadores sintéticos internos (`indicators`), 09-25 recalculado sobre os fechamentos da terceira geração: ratio Far/Soj **84,38%** (era 84,23% na leitura de ontem, +0,15 p.p.); oil share **47,76%** (era 47,78%, praticamente estável); crush margin **US$2,4344/bushel** (era US$2,4134, +0,87%); oil-meal spread **-0,6996 USD/bushel** (era -0,693, estável); paridade BR da soja **R$151,18/saca** (era R$151,30, CBOT 1.319,00 × USD/BRL 5,1991); margem de biodiesel US **US$1,9617/galão** (era US$1,8584 — a terceira cifra distinta publicada para o mesmo dia: 1,8314 no dump do próprio 25/09, 1,8584 no dump de 26/09, e agora 1,9617 no dump de hoje). Série do ratio Far/Soj 21-25/09, sem mudança nos dias já fechados: 83,22% → 83,90% → 84,36% → **84,80% (pico, 24/09)** → **84,38% (25/09, recuo de 0,42 p.p., menor do que os 0,57 calculados ontem)**; oil share na mesma janela: 47,81% → 47,78% → **47,56% (mínima, 24/09)** → **47,76% (25/09)**; ISF (Índice de Sobra de Farelo) 60/100 e ISO (Índice de Suporte do Óleo) 80/100 seguem travados, com carimbo repetido também em **2026-09-27**
  - BCB PTAX — sem cotação nova (fim de semana): a mais recente segue sendo **2026-09-25**, USD/BRL **5,1991**, EUR/BRL 5,928, Selic diária 0,050788% a.a. (séries SGS 1, 21619, 11) — mesma base cambial já usada na leitura de ontem
  - CEPEA/ESALQ Soja Paranaguá (via NAG) — sem leitura nova (fim de semana): a mais recente segue **2026-09-25**, R$161,00/saca (-0,52% frente a 24/09); soja Paraná interior R$154,38/saca; spread Paranaguá-interior R$6,62/saca — com a paridade CBOT-implícita revisada hoje para R$151,18/saca, o basis físico real (Paranaguá menos paridade) recalcula para **R$9,82/saca** (era R$9,70 na leitura de ontem, usando a paridade então vigente de R$151,30) — ainda uma compressão de -13,9% frente aos R$11,40/saca de 24/09, mas ligeiramente menor do que os -14,9% calculados ontem
  - NAG físico BR (`nag_fisico`) — sem leitura nova (fim de semana, praças não publicam): os últimos valores seguem sendo os de **2026-09-25** já tratados ontem — farelo Mato Grosso/IMEA R$1.996,41/ton; farelo Rondonópolis/MT (BCSP) R$2.200,00/ton, quinta leitura seguida no mesmo valor (21 a 25/09); farelo média Rio Grande do Sul (Clicmercado) R$2.130,00/ton, terceira leitura seguida (23 a 25/09); prêmio export farelo Paranaguá 0,12 USD/short_ton, congelado há **19 dias corridos** (desde 08/09); prêmio export óleo Paranaguá 0,1 cts/lb, mesmo congelamento
  - CFTC COT Managed Money — **sem corte novo**: o mais recente segue sendo o de **2026-09-22**, agora com **5 dias corridos de idade**, o mesmo já analisado em profundidade na leitura de ontem — farelo net long 191.087 contratos (+4,36% vs 15/09); óleo net long 92.137 (-9,21%); soja net long 265.159 (+9,80%). Próximo corte esperado para posições de 29/09, a divulgar por volta de 02/10 (padrão semanal da CFTC de publicar toda sexta-feira as posições da terça-feira anterior)
  - USDA Crop Progress — sem corte novo: ainda o de **2026-09-20** (agora **7 dias de idade**), 12% excelente / 46% boa (G/E 58%), 10% pobre, colheita 12% concluída; o próximo corte, já esperado para "por volta de 27-28/09" nas duas últimas leituras, cai exatamente em cima da janela de hoje e amanhã
  - USDA WASDE — **segue ausente do dump pela segunda leitura seguida**; nem mesmo a edição defasada de 11/09 aparece (ver Honestidade)
  - NOPA — item de fila `release-nopa-2026-09-27`: `monthly_status` em 0,0 bool, o mesmo padrão de paywall de todas as leituras anteriores desde o início deste monitoramento
  - ABIOVE projeções mensais — balanços out-dez/2026, sem revisão nesta janela frente à leitura de ontem: produção de farelo BR caindo 2.142,97 (out) → 1.977,59 (nov) → 1.659,04 (dez) mil t; exportação de farelo BR caindo 850 → 800 → 700 mil t; estoque final de soja BR caindo 5.720,77 (out) → 3.658,99 (nov) → 1.889,91 (dez) mil t
  - Notícias Agrícolas/Canal Rural/Farm Progress (RSS) — sem manchete nova com corpo de texto: a mais recente segue sendo a de **2026-09-25** (Farm Progress, "Late-season rain offers final soybean yield bump"); contagem de itens de 27/09 registra 160 itens lidos e 2 mantidos, igual a 26/09
  - CEPEA RSS — contagem de itens recua para **101 em 27/09** (de 104 em 26/09 e 106 em 25/09), sem corpo de headline novo; a última manchete com texto completo segue sendo a de 18/09
  - NOAA CPC ENSO — El Niño Advisory, inalterado (carimbo 2026-09-27)
  - MPOB — carimbo 2026-09-27, parser sem números extraídos, mesmo tamanho de página (3.181 chars) das duas leituras anteriores
  - INMET — previsão para **2026-09-27 (HOJE)**: calor sobe mais um degrau no núcleo de Mato Grosso e agora também no Paraná frente à previsão de ontem — Cuiabá 41°C/25°C (era 38°C), Sinop e Sorriso 40°C/25°C (estável), Lucas do Rio Verde 40°C/26°C (era 39°C), Rio Verde/GO 38°C/23°C (era 35°C); Cascavel e Maringá/PR sobem a 35°C/18-19°C (eram 33°C); Passo Fundo/RS, em vez de "possibilidade de chuva isolada", passa a registrar **"muitas nuvens com pancadas de chuva e trovoadas isoladas"** — o primeiro boletim desta janela com menção efetiva a pancada de chuva prevista, não apenas possibilidade, coerente com o pano de fundo El Niño de chuvas acima da média no sul do Brasil
  - system/tributario_watch.toml (lido como referência, não editado) — `atualizado_em` 2026-06-05 em todos os 10 eventos catalogados, **114 dias corridos** sem revisão humana frente a hoje (27/09)
  - Forecasts estatísticos internos (bandas 7d/30d) — geração de **2026-09-27**, sobre o fechamento revisado de 25/09, alvos 04/10 e 27/10: viés "altista" em farelo nos dois horizontes e em soja no horizonte de 30d (7d em "lateral"); óleo em "baixista" nos dois horizontes — extrapolação estatística, não fundamentalista (ver Honestidade)
  - Fila de julgamento — 2026-09-27, 7 itens: `alerta-quebra_resistencia-soja_cbot-2026-09-25`, `alerta-quebra_suporte-oleo_cbot-2026-09-25`, `alerta-quebra_resistencia-farelo_cbot-2026-09-25`, `alerta-quebra_suporte-complexo_soja-2026-09-25`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`, `release-nopa-2026-09-27`
  - Cruza com [[2026-09-26_leitura-complexo]] (leitura de ontem, base direta de comparação para toda a revisão de dados de hoje), [[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]] e [[2026-09-24_correcao-numeros-sessao-23set-fim-do-artefato-de-baixa-liquidez]] (documentação do mesmo padrão estrutural de revisão, agora em sua ocorrência mais persistente), [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (tese original do ratio) e [[2026-09-17_ratio-far-soj-supera-nivel-de-abertura-da-tese-original-quarta-sessao]] e [[2026-09-09_d90-ratio-far-soj-reverte-na-vespera]] (invalidação técnica já fechada da tese de junho)
status: ativa
vies: [bull-farelo, bull-soja, bear-oleo_soja]
---

## Visão geral

O complexo soja gira em torno do "crush" — o esmagamento industrial que separa a soja em
grão em dois produtos com destinos econômicos diferentes: farelo (o resíduo proteico,
usado quase todo em ração animal, sobretudo aves e suínos) e óleo (usado em alimentação
humana e, cada vez mais, em biodiesel). Quem manda no crush é definido pelo "oil share" —
a fatia do valor total gerado pelo esmagamento que vem do óleo. Quando o oil share é alto,
a indústria esmaga soja atrás do valor do óleo, e o farelo sai como subproduto que precisa
ser escoado a qualquer preço, pressionando seu preço relativo para baixo; quando o oil
share cai, o farelo passa a pagar a conta do esmagamento e o óleo perde protagonismo. O
termômetro dessa disputa é o ratio Far/Soj — o preço do farelo dividido pelo da soja, em
percentual: abaixo de 80% o farelo está "abundante" (baixista); entre 80% e 87%, "neutro";
acima de 87%, "apertado" (altista para o farelo).

**Hoje é domingo — não há sessão nova no CBOT, e a próxima só volta amanhã, segunda-feira
28/09.** Isso, por si só, tornaria esta uma leitura de continuidade pura. Mas o dump de
hoje traz uma novidade que não é de mercado, e sim de qualidade de dado, e ela é grande o
suficiente para ser o fio condutor de toda a leitura: **a sessão de 25/09 — a mesma sessão
que a leitura de ontem já havia tratado como "confirmada", depois de duas rodadas prévias
de revisão nos dias 24 e 25/09 — voltou a mudar.** Farelo, óleo e soja mostram hoje
abertura, máxima e mínima **idênticas, casa decimal por casa decimal**, às usadas na
leitura de ontem — mas o fechamento e o volume dos três contratos mudaram ao mesmo tempo:
soja caiu de 1.320,00 para **1.319,00** (-0,08%) com o volume recuando de 180.479 para
**140.637 contratos** (-22,1%); farelo subiu de 370,60 para **371,00** (+0,11%) com o
volume subindo de 94.390 para **105.415 contratos** (+11,7%); óleo subiu de 67,82 para
**67,84** (+0,03%) com o volume recuando de 99.658 para **88.388 contratos** (-11,3%). Em
magnitude de preço, cada mudança isolada é pequena — mas o fato de as três pernas do
complexo mudarem simultaneamente, numa sessão que já havia sido chamada de "confirmada"
publicamente, é o dado mais importante desta leitura em termos de o quanto se pode confiar
na palavra "confirmado" nesta série (ver Honestidade).

**O heating oil (HO=F) — o insumo que alimenta a margem de biodiesel americana e, por
extensão, parte da tese de óleo — sofreu uma revisão ainda maior.** Não foram só o
fechamento e o volume que mudaram: a abertura foi de 4,5700 para **4,7850** (+4,71%), a
máxima de 4,5961 para **4,8433** (+5,38%), a mínima de 4,3789 para **4,5190** (+3,20%), o
fechamento de 4,5799 para **4,6847** (+2,29%), e o volume de 62.876 para **33.058
contratos** (-47,4%). É a terceira versão distinta do preço de fechamento deste mesmo dia
que este monitoramento registra: 4,5214 no dump gerado no próprio dia 25/09, 4,5799 no
dump de 26/09, e agora 4,6847 no dump de hoje. Como consequência direta, a margem de
biodiesel americana calculada para 25/09 também já teve três valores publicados
diferentes: US$1,8314 (leitura de 25/09), US$1,8584 (leitura de 26/09, uma correção que
piorava a margem) e agora **US$1,9617** (leitura de hoje, uma correção que melhora a
margem frente ao número de ontem, mas que ainda fica abaixo dos US$2,0290 confirmados de
24/09). O mesmo recálculo, em cascata, muda o ratio Far/Soj de 25/09 de 84,23% (usado
ontem) para **84,38%** hoje — o que, na prática, reduz o tamanho do recuo desde o pico de
24/09 (84,80%) de 0,57 ponto percentual (calculado ontem) para **0,42 ponto percentual**
(calculado hoje). A leitura direcional não muda — o ratio segue dentro da zona neutra
(80-87%), a 2,62 pontos do teto "apertado" — mas o tamanho exato da "pausa" que a leitura
de ontem descrevia como o primeiro sinal de possível reversão fica, ele mesmo, mais
incerto do que parecia.

**Sem sessão nova de mercado e sem corte novo de COT (o mais recente segue sendo o de
22/09, agora com 5 dias de idade, o mesmo já analisado a fundo ontem), a segunda coisa que
muda hoje é o clima em Mato Grosso e no Paraná.** O boletim do INMET para hoje mostra calor
subindo mais um degrau frente a ontem em quase todos os pontos monitorados (Cuiabá 41°C,
era 38°C; Rio Verde/GO 38°C, era 35°C; Cascavel e Maringá/PR 35°C, eram 33°C) e, pela
primeira vez nesta janela de 14 dias, Passo Fundo/RS troca a "possibilidade de chuva
isolada" por uma previsão efetiva de **"muitas nuvens com pancadas de chuva e trovoadas
isoladas"** — coerente com o regime de El Niño (chuva acima da média no sul do Brasil) que
já vinha sendo citado como pano de fundo estrutural favorável à safra brasileira 2026/27.
Nenhum desses dois vetores (revisão de dado, clima) muda a direção de nenhuma das três
pernas hoje — mas o segundo é o tipo de dado que, se persistir ao longo da semana de
plantio, começa a valer a pena acompanhar com mais atenção.

**Leitura de uma linha**: o pivô do complexo continua sendo o ratio Far/Soj, agora
recalculado em 84,38% — a pausa desde o pico de 24/09 (84,80%) é real, mas menor do que a
leitura de ontem media, porque o próprio dado de origem ainda estava mudando. Maior
convicção segue em bull-farelo (física BR estável, ratio ainda perto do teto, COT de
22/09 ainda comprando); bear-óleo segue sustentado pelo quadro técnico e pelo COT (o corte
mais agressivo de net long das três pernas), mas com o driver da margem de biodiesel
enfraquecido nesta leitura pela terceira revisão consecutiva do HO=F; bull-soja mantido
pela mesma reversão de COT de 22/09 já tratada ontem, sem reforço novo hoje por falta de
sessão de mercado. Trata as quatro quebras técnicas da fila
(`alerta-quebra_resistencia-soja_cbot-2026-09-25`, `alerta-quebra_suporte-oleo_cbot-2026-09-25`,
`alerta-quebra_resistencia-farelo_cbot-2026-09-25`, `alerta-quebra_suporte-complexo_soja-2026-09-25`)
nas seções abaixo, sobre os valores agora revisados pela terceira vez; as duas revisões
"vencidas" da tese de junho (`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
e `-D+90`) na seção Farelo, ambas já fechadas desde 17/09; e o release de NOPA
(`release-nopa-2026-09-27`) na seção Honestidade, mais uma vez sem dado real por trás do
paywall.

## Soja

**Viés: bull, mantido — sem sessão de mercado nova e sem corte de COT novo, a tese segue
apoiada inteiramente na mesma reversão de convicção dos fundos (corte de 22/09) já
descrita na leitura de ontem; o único dado novo de hoje (a revisão do fechamento de
25/09 para 1.319,00) é de magnitude tão pequena que não altera nada na leitura técnica ou
de paridade.**

O que sustenta a tese:

- **O corte de COT de 22/09 (CFTC, ainda o mais recente, agora com 5 dias corridos de
  idade) mostra os fundos com net long em soja de 265.159 contratos, alta de +9,80% frente
  aos 241.501 de 15/09** — a reversão de convicção já tratada em profundidade na leitura de
  ontem, sem novidade hoje porque não há corte mais recente. A composição segue a mesma:
  managed money long subiu +6,43% (para 300.742) e o short caiu -13,38% (para 35.583); os
  produtores (hedge natural do produtor físico) ampliaram o short em +2,24% (para 650.281)
  — coerente com mais originação/venda física à medida que a colheita americana avança
  (12% concluída em 20/09, USDA Crop Progress, corte agora com 7 dias de idade).
- **A soja fechou (na versão agora revisada pela terceira vez da sessão de 25/09) em
  1.319,00, folgadamente acima da resistência de referência de 1.180,00** (fila
  `alerta-quebra_resistencia-soja_cbot-2026-09-25`) — uma folga de **+11,78%**,
  essencialmente igual à folga de +11,86% calculada ontem sobre o fechamento então vigente
  de 1.320,00; a revisão de -0,08% no fechamento não muda a leitura técnica em nada
  relevante.
- **A paridade em reais da soja recalcula para R$151,18/saca hoje** (CBOT 1.319,00 × USD/BRL
  5,1991, mesma PTAX de sexta-feira, sem cotação nova no fim de semana) — uma queda
  marginal de -0,08% frente aos R$151,30 usados ontem, inteiramente explicada pela revisão
  do fechamento do CBOT, não por qualquer movimento novo de câmbio ou de mercado.
- **A curva futura permanece em contango regular**, com valores quase idênticos aos de
  ontem: nov/26 (base) 1.319,00 → jan/27 1.332,50 → mar/27 1.339,50 → mai/27 1.346,25 →
  jul/27 1.350,75 — o mercado a termo segue precificando preços mais altos à frente.
- **A curva de crop progress (corte de 20/09, agora 7 dias de idade) segue mostrando
  condição estável em G/E 58%** — a safra americana não deteriorou na reta final do ciclo,
  com a colheita avançando (12% concluída); o próximo corte, esperado "por volta de
  27-28/09" desde a leitura de dois dias atrás, cai exatamente na janela de hoje/amanhã.

**O que invalida / risco:**

- **O basis físico em Paranaguá segue comprimido**: com a paridade CBOT-implícita
  recalculada para R$151,18/saca, o basis (preço físico de Paranaguá R$161,00/saca menos
  paridade) fica em **R$9,82/saca**, ainda uma compressão de -13,9% frente aos R$11,40/saca
  de 24/09 (a leitura de ontem havia calculado -14,9%, usando a paridade então vigente de
  R$151,30) — o sinal de divergência entre físico brasileiro e tela de Chicago segue de pé,
  apenas com magnitude ligeiramente menor após a revisão. Sem leitura física nova neste fim
  de semana para confirmar se a compressão persiste ou reverte.
- **A manchete de Farm Progress (25/09) sobre chuva tardia sustentando produtividade da
  soja americana segue sem seguimento** — nenhuma notícia nova apareceu no fim de semana
  (contagem de 27/09 igual à de 26/09: 160 itens lidos, 2 mantidos, nenhum novo).
- **O WASDE segue ausente do dump pela segunda leitura seguida** — sem esse insumo, a
  leitura de soja e farelo fica mais dependente de COT e técnico, e menos de fundamento de
  balanço direto (ver Honestidade).
- **O regime de El Niño (NOAA CPC, inalterado) segue associado a chuvas acima da média no
  sul do Brasil**, e o boletim do INMET de hoje traz a primeira menção efetiva de pancada
  de chuva prevista em Passo Fundo/RS nesta janela — um vetor de médio prazo que tende a
  favorecer a produtividade da safra brasileira 2026/27, pesando contra qualquer tese de
  escassez estrutural de soja no horizonte à frente.
- **Nível técnico a vigiar:** um fechamento de volta abaixo de 1.180 desfaria formalmente o
  rompimento; com a folga em +11,78%, esse cenário segue distante.

**Leitura operacional:** sem sessão de mercado e sem corte de COT novo neste fim de semana,
não há gatilho novo para mudar a posição — a recomendação operacional é a mesma da leitura
de ontem: para quem está comprado, manter ou ampliar a posição estrutural apoiada na
reversão de convicção dos fundos (COT de 22/09) e na paridade em reais, com o nível técnico
de 1.180 como referência de invalidação distante. Para quem opera vendido, a compressão do
basis físico em Paranaguá (agora R$9,82/saca) e o regime de El Niño seguem sendo os únicos
argumentos disponíveis, nenhum deles um gatilho técnico. O corte de COT de posições de
29/09 (esperado por volta de 02/10) é o próximo evento capaz de confirmar se a reversão de
convicção dos fundos continua ou já foi só um ajuste pontual.

## Farelo

**Viés: bull, mantido — a revisão de hoje reduz o tamanho do recuo do ratio Far/Soj desde o
pico de 24/09 (de 0,57 para 0,42 ponto percentual), o que reforça, e não enfraquece, a
leitura de que a pausa é técnica, não uma reversão de tendência.**

O que sustenta a tese:

- **O ratio Far/Soj recalcula para 84,38% hoje** (era 84,23% na leitura de ontem, sobre o
  mesmo dia 25/09) — a distância ao pico de 24/09 (84,80%) cai de 0,57 para **0,42 ponto
  percentual**, e o ratio segue **+2,98 pontos percentuais** acima do nível de abertura da
  tese baixista original de 11/06/2026 (81,4%,
  [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]], agora **108 dias corridos**
  atrás) — trata `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` e
  `-D+90`: ambas seguem aparecendo como "vencidas" na fila de hoje, mas o veredito de ambas
  já está fechado desde
  [[2026-09-17_ratio-far-soj-supera-nivel-de-abertura-da-tese-original-quarta-sessao]] e
  reafirmado pela revisão formal de D+90 em
  [[2026-09-09_d90-ratio-far-soj-reverte-na-vespera]]. Nenhuma ação nova é necessária sobre
  essas duas revisões específicas; resta em aberto apenas o marco de D+180, programado para
  2026-12-08 (72 dias à frente).
- **O farelo fechou (versão agora revisada pela terceira vez) em 371,00, folgadamente acima
  da resistência histórica de 325,00** (fila `alerta-quebra_resistencia-farelo_cbot-2026-09-25`),
  folga de **+14,15%** — ligeiramente maior do que a folga de +14,03% calculada ontem, já
  que a revisão de hoje elevou o fechamento (era 370,60, agora 371,00, +0,11%).
- **A confirmação física no Brasil segue tripla e sem mudança neste fim de semana** (nenhuma
  praça publica preço sábado/domingo): farelo Rondonópolis/MT (BCSP) em R$2.200,00/ton pela
  quinta leitura seguida (21 a 25/09); farelo média Rio Grande do Sul (Clicmercado) em
  R$2.130,00/ton pela terceira leitura seguida (23 a 25/09); farelo Mato Grosso/IMEA em
  R$1.996,41/ton, ainda a única leitura no novo patamar depois de cinco leituras travadas.
- **O oil share, recalculado, fica em 47,76% em 25/09** (era 47,78% ontem, uma diferença de
  apenas 0,02 ponto percentual, essencialmente dentro do ruído) — o farelo segue
  respondendo por mais da metade do valor gerado no crush.
- **O oil-meal spread recalcula para -0,6996 USD/bushel** (era -0,693 ontem, também dentro
  do ruído) — a distância entre o valor do farelo e o do óleo, em bushel-equivalente, segue
  historicamente ampla.
- **A trajetória sazonal da ABIOVE para o Brasil continua apontando para alívio de oferta
  doméstica de farelo à frente**, sem revisão nesta janela: produção projetada caindo de
  2.142,97 mil t (out/26) para 1.977,59 (nov/26) e 1.659,04 mil t (dez/26); exportação de
  850 para 800 e 700 mil t no mesmo período.
- **O COT de 22/09 (ainda o mais recente) mostra os fundos com net long em farelo de
  191.087 contratos, alta de +4,36% frente a 15/09**, sem novidade hoje por falta de corte
  mais recente.

**O que invalida / risco:**

- **A magnitude exata da revisão de hoje é, ela mesma, o risco mais concreto desta
  leitura**: é a terceira vez que o fechamento de 25/09 muda de valor entre gerações do
  dump (371,50/371,80 no dia, depois 370,60, agora 371,00), e não há garantia de que a
  próxima geração não traga uma quarta versão. Ver Honestidade para o detalhamento completo
  do padrão.
- **O prêmio de exportação de farelo em Paranaguá segue congelado em 0,12 USD/short_ton há
  19 dias corridos** (desde 08/09) — se o aperto físico doméstico fosse amplo e sustentado
  a ponto de pressionar também o canal de exportação, seria razoável esperar, eventualmente,
  algum reflexo no FOB; essa confirmação ainda não apareceu.
- **A curva futura de farelo segue em backwardation (inversão)**: dez/26 (base) 371,00 →
  jan/27 369,80 → mar/27 368,30 → mai/27 367,90 (-0,84% de dez/26 a mai/27) — o mercado a
  termo segue sem precificar um aperto estrutural que se estenda indefinidamente.
- **Os índices sintéticos ISF e ISO seguem travados em 60/100 e 80/100**, agora **16 dias
  corridos** sem qualquer reação desde 11/09, apesar de o ratio e o oil share terem se
  movido de forma expressiva nesse período.
- **O volume revisado da sessão de 24/09 (105.415 contratos) é, hoje, idêntico ao volume
  revisado da sessão de 25/09** — o mesmo número exato aparecendo em dois dias distintos
  para o mesmo contrato é, no mínimo, um ponto de atenção adicional sobre a robustez da
  captura de volume nesta série (ver Honestidade).

**Leitura operacional:** sem sessão de mercado nova, a recomendação operacional não muda
frente à leitura de ontem — para quem está comprado no spread Far/Soj ou diretamente em
farelo, a tendência de fundo (física BR estável em três praças, ratio ainda a 2,62 pontos
do teto "apertado", COT de 22/09 ainda comprador) segue justificando manter ou reforçar a
posição. A novidade de hoje é, na prática, uma boa notícia para a convicção na tendência:
o recuo do ratio desde o pico de 24/09 acaba de ficar menor (0,42 p.p., não 0,57), o que
reduz — não aumenta — o peso do argumento de que a pausa de 25/09 seria o início de uma
reversão. Para quem está vendido, o calendário sazonal da ABIOVE e o nível técnico seguem
desfavoráveis; a inversão da curva futura nos meses mais distantes e o prêmio de exportação
congelado seguem sendo os únicos argumentos a favor de cautela em posições compradas de
prazo mais longo.

## Óleo

**Viés: bear, mantido — mas com o driver mais recente da tese (a margem de biodiesel
americana) enfraquecido, não reforçado, pela revisão de hoje: a margem calculada para
25/09 sobe de US$1,8584 para US$1,9617, a terceira cifra distinta publicada para o mesmo
dia, sobre um HO=F cuja abertura, máxima e mínima também foram revisadas, não só o
fechamento.**

O que sustenta a tese:

- **O corte de COT de 22/09 (ainda o mais recente, agora 5 dias de idade) mostra os fundos
  com net long em óleo de 92.137 contratos, queda de -9,21% frente aos 101.480 de 15/09**
  — o maior movimento relativo entre as três pernas do complexo nesta rodada de COT, sem
  novidade hoje por falta de corte mais recente, mas ainda o dado de posicionamento mais
  forte a favor da tese bear.
- **Óleo fechou (versão revisada pela terceira vez) em 67,84 na sessão de 25/09, abaixo do
  suporte de referência de 72,00** (fila `alerta-quebra_suporte-oleo_cbot-2026-09-25`),
  distância de **-5,78%** — essencialmente igual à distância de -5,81% calculada ontem, já
  que a revisão de hoje moveu o fechamento em apenas +0,03% (67,82→67,84).
- **O oil share recalcula para 47,76%** (era 47,78% ontem, diferença desprezível) — o óleo
  segue respondendo por menos da metade do valor gerado no crush.
- **O oil-meal spread recalcula para -0,6996 USD/bushel** (era -0,693 ontem) — o óleo
  cada vez mais atrás do farelo em valor por bushel-equivalente.
- **O ISO (Índice de Suporte do Óleo) segue em 80/100**, sem melhora, com carimbo repetido
  em 27/09.
- **O forecast estatístico interno segue em "baixista" nos dois horizontes (7d e 30d)** —
  extrapolação de tendência, não fundamentalista.
- **A lente fiscal brasileira segue estruturalmente desfavorável, sem mudança hoje**: a MP
  1.363/2026 (subvenção ao diesel fóssil, vigente até 31/12/2026) segue plenamente vigente;
  a isenção de PIS/Cofins do biodiesel na mistura está agora **58 dias corridos vencida**
  (vigência até 31/07/2026) sem sinal de renovação.

**O que sustenta um contraponto — reforçado hoje pela revisão do HO=F:**

- **A margem de biodiesel americana calculada para 25/09 sobe para US$1,9617/galão** (era
  US$1,8584 na leitura de ontem, +5,55%) — a terceira cifra distinta publicada para este
  mesmo dia (1,8314 → 1,8584 → **1,9617**). Isso significa que a conclusão da leitura de
  ontem — de que a margem havia caído -8,41% frente a 24/09 — não se sustenta na versão de
  hoje: recalculada, a queda frente aos US$2,0290 confirmados de 24/09 é de apenas
  **-3,32%**, bem menor. A margem de 25/09 ainda fica abaixo da de 24/09, então a tendência
  de deterioração de curto prazo segue de pé — mas o tamanho exato dessa deterioração já
  foi revisado três vezes, e a direção do erro desta vez foi a oposta da vez anterior
  (ontem, a revisão havia piorado a margem frente ao número original; hoje, ela melhora).
  Este é o contraponto mais frágil desta leitura — não porque a tese bear esteja errada, mas
  porque o dado que a sustenta especificamente nesta métrica segue instável (ver
  Honestidade).
- **O RIN D4 (crédito de biocombustível renovável americano) permanece constante na fórmula
  interna** — toda a variação de margem, nesta e nas leituras anteriores, vem do heating
  oil, cuja instabilidade de captura é o problema, não uma mudança de política.
- **A curva futura de médio prazo segue em contango regular**: out/26 67,26 → dez/26 (base)
  67,84 → jan/27 68,05 → mar/27 68,26 → mai/27 68,43 (+0,87% de dez/26 a mai/27) — sem
  sinal de reprecificação estrutural de baixa no médio prazo.
- **Catalisadores de alta represados, ainda não correntes**: B16 segue "adiado", resultado
  esperado por volta de novembro/2026; a centralização da exportação de palma pela
  Indonésia via Danantara, que tinha alvo de assunção plena em 01/09/2026, já soma **26
  dias** de atraso sem confirmação — ambos seguem como upside represado, não corrente.

**Leitura operacional:** o quadro técnico (abaixo do suporte de 72,00) e o COT (o corte
mais agressivo de net long das três pernas) seguem sustentando o lado vendido direcional,
sem novidade hoje por falta de sessão de mercado. Mas o driver mais recente e mais citado
nas últimas leituras — a margem de biodiesel — acaba de perder força como argumento
independente: sua terceira revisão em três dias mostra que o número específico de 25/09 não
é confiável o suficiente para justificar, sozinho, reforço de posição vendida hoje. Para
quem está vendido, a recomendação é manter a posição apoiada no técnico e no COT — ambos
não dependem do HO=F — e tratar a margem de biodiesel como um indicador a ser reavaliado
apenas quando o dado parar de mudar de geração em geração. Para quem está comprado ou
avalia entrar, a suavização da queda de margem (de -8,41% para -3,32% frente a 24/09) é, na
prática, o argumento mais forte a favor de uma pausa na tese bear que apareceu nesta série
em várias sessões — ainda que apoiado num dado que a própria leitura reconhece como
instável. Para quem opera o spread farelo-óleo dentro do crush, o oil-meal spread
recalculado (-0,6996) segue em zona extrema, mas sem mudança de magnitude relevante frente
a ontem.

## Spreads e crush (leitura de complexo)

O ratio Far/Soj, recalculado hoje, mostra uma trajetória de pico e recuo mais suave do que
a leitura de ontem registrava: 83,22% (21/09) → 83,90% (22/09) → 84,36% (23/09) → **84,80%
(pico, 24/09)** → **84,38% (25/09, recuo de 0,42 p.p., não 0,57 como calculado ontem)** —
ainda dentro da zona neutra (80-87%), a 2,62 pontos percentuais do teto "apertado" e 4,38
pontos do piso "abundante". O oil share espelha o mesmo movimento, com a mesma suavização:
mínima de 47,56% em 24/09, recuo a **47,76%** em 25/09 (era 47,78% ontem). O crush margin
recalcula para **US$2,4344/bushel** (era US$2,4134 ontem, +0,87%), ainda abaixo do piso de
referência de US$2,50 monitorado pela fila (`alerta-quebra_suporte-complexo_soja-2026-09-25`,
distância agora de **-2,62%**, menor do que os -3,46% calculados ontem).

**A leitura de complexo mais importante de hoje é metodológica, não direcional: a
"confirmação" de dado, nesta série, deixou de ser um estado final e passou a ser, na
prática, apenas o rótulo da versão mais recente disponível em cada dia.** A sessão de 25/09
já havia sido tratada como provisória (na própria leitura do dia 25/09), depois como
confirmada (na leitura de 26/09), e hoje muda pela terceira vez — com abertura, máxima e
mínima permanecendo estáveis nos três contratos de ágio (soja, farelo, óleo), mas
fechamento e volume mudando nos três ao mesmo tempo. Isso é uma evolução do padrão já
documentado em [[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]] e
[[2026-09-24_correcao-numeros-sessao-23set-fim-do-artefato-de-baixa-liquidez]]: naquelas
ocorrências, a revisão típica trocava um dia com OHLC inteiramente duplicado do dia
anterior por um dia com OHLC saudável e distinto — um evento que, uma vez ocorrido,
parecia se encerrar. O que se vê agora é diferente e mais preocupante: mesmo depois de uma
sessão já ter passado por esse ciclo completo (do provisório ao "confirmado"), o
fechamento e o volume continuam mudando numa terceira geração, sem que a abertura, a
máxima e a mínima também mudem — ou seja, o mecanismo de captura parece estar ainda
ajustando o preço de fechamento e a contagem de volume dias depois do OHLC intradiário já
estar estável. No caso do HO=F (heating oil), a instabilidade é ainda maior: mesmo a
abertura, a máxima e a mínima mudaram nesta terceira geração, não apenas o fechamento e o
volume — o insumo menos estável de todo este monitoramento, com três valores de fechamento
diferentes já publicados para o mesmo dia (4,5214 → 4,5799 → 4,6847).

O COT de 22/09, ainda o dado de posicionamento mais recente cinco dias depois, retrata os
fundos com net long ampliado em farelo (+4,36%) e soja (+9,80%) e reduzido em óleo (-9,21%)
— sem novidade hoje, mas ainda o alinhamento de posicionamento mais coerente com a tese de
preço já descrita nesta série. Os dois índices compostos por contagem de condições — ISF
(60/100) e ISO (80/100) — seguem travados no mesmo patamar desde 11/09, agora **16 dias
corridos** sem qualquer reação, apesar de o ratio e o oil share terem se movido de forma
expressiva nesse período.

## Lente fiscal/regulatória BR

Antes de fechar qualquer tese de preço BR, os vetores tributários/regulatórios vivos que
pesam no complexo — todos do `system/tributario_watch.toml`, cujo carimbo mais recente
(`atualizado_em`) em todos os 10 eventos catalogados é 2026-06-05, ou seja, **114 dias
corridos sem revisão humana** frente a hoje (27/09), mais um dia do que ontem:

- **MP 1.363/2026** (id `MP-1363-2026`, subvenção diesel fóssil R$1,12/L, vigente até
  31/12/2026): barateia o diesel fóssil no mix B15 (mistura obrigatória de 15% de
  biodiesel), reduzindo a competitividade relativa do biodiesel e a demanda doméstica por
  óleo de soja — vetor estrutural de baixa para óleo, plenamente vigente, sem mudança de
  status.
- **B16 (id `B16-CNPE-2026`, elevação da mistura obrigatória de biodiesel para 16%)** segue
  "adiado", resultado esperado por volta de novembro/2026. Upside represado (~436 mil
  toneladas de demanda potencial adicional de óleo), não corrente.
- **Isenção de PIS/Cofins do biodiesel na mistura** (id `PISCOFINS-BIODIESEL-ISENCAO`):
  vigência registrada até 31/07/2026 — já **58 dias corridos vencida** frente a
  27/09/2026, sem registro de prorrogação ou expiração.
- **MP 1.358/2026** (subvenção gasolina R$0,89/L): vigência registrada até 11/07/2026,
  agora **78 dias corridos vencida**.
- **STJ REsp 2.165.276** (id `STJ-RESP-2165276`, crédito de PIS/Cofins sobre soja em
  biodiesel, direção "alta" para soja/óleo): sem novidade nesta janela.
- **EPA RFS 2026/2027** (id `EPA-RFS-2026-2027`, mandato de biocombustível americano,
  direção "alta" para óleo): sustenta o RIN D4, estável, e o RIN permanece constante na
  fórmula interna de margem de biodiesel — a variação de margem observada hoje vem
  inteiramente do heating oil, ainda instável (ver Honestidade), não de mudança
  regulatória.
- **Crédito 45Z** (id `45Z-CLEAN-FUEL`, em tramitação, direção "mista"): sem novidade.
- **Indonésia — Danantara** (id `DANANTARA-INDONESIA`) e **levy de exportação PMK 9/2026**
  (id `INDONESIA-LEVY-PMK9`): a assunção plena da centralização da exportação de palma
  pela Indonésia tinha alvo 01/09/2026 — já se passaram **26 dias** sem confirmação.
  Catalisador de alta represado para óleo (via substituição com palma) — ainda sem dado de
  MPOB disponível para monitorar diretamente (parser continua quebrado, ver Honestidade).
- **Indonésia B50** (id `INDONESIA-B50`, monitorando, direção "alta"): sem novidade.

Nenhum desses vetores muda a leitura de preço de hoje isoladamente — mas, em conjunto,
eles seguem reforçando a mesma assimetria já descrita em leituras anteriores: o mercado
interno brasileiro tem múltiplos desincentivos correntes ao óleo (MP 1.363 plenamente
vigente, isenção PIS/Cofins já 58 dias vencida) e múltiplos catalisadores de alta
represados, não correntes (B16, Danantara, B50). O óleo brasileiro segue mais fraco
estruturalmente até que algum dos vetores represados vire fato concreto — e a lacuna
crescente de 114 dias sem revisão humana do catálogo tributário é, em si, um risco
operacional recorrente nesta série: qualquer um destes vetores pode ter mudado de status
na realidade sem que este sistema tenha como saber.

## Riscos e eventos próximos

- **Se o fechamento e o volume da sessão de 25/09 mudarem uma quarta vez na próxima geração
  do dump**, isso deixa de ser um evento pontual e passa a valer o mesmo tratamento de
  "padrão estrutural" já aplicado ao HO=F em
  [[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]] — mas agora estendido aos
  próprios contratos de soja, farelo e óleo, não apenas ao heating oil.
- **Retorno de um HO=F com abertura/máxima/mínima estáveis entre gerações** — até agora, é
  o único insumo desta série em que mesmo o intradiário (não só o fechamento) segue mudando
  três dias depois da sessão.
- **Reabertura do mercado amanhã (segunda-feira, 28/09)** — a primeira sessão nova desde
  sexta-feira, capaz de trazer o primeiro movimento de preço real da semana e testar se os
  níveis técnicos vigiados (soja 1.180, farelo 325, óleo 72, crush margin 2,50) seguem
  respeitados.
- **Próximo corte de COT** (posições de 29/09, esperado por volta de 02/10) — o próximo
  dado capaz de confirmar se a reversão de convicção em soja e o corte em óleo da rodada de
  22/09 são o início de uma nova tendência de posicionamento ou um ajuste pontual.
- **USDA Crop Progress**: próximo corte esperado "por volta de 27-28/09" — cai exatamente
  na janela de hoje/amanhã.
- **Retorno do WASDE ao dump** — ausente pela segunda leitura seguida.
- **Compressão do basis físico em Paranaguá** (agora R$9,82/saca, recalculado) — checar se
  a divergência entre físico e tela persiste ou se corrige na próxima leitura física
  (segunda-feira).
- **Nível técnico a vigiar em farelo:** volta abaixo de 325,00 desfaria o rompimento (folga
  atual +14,15%).
- **Nível técnico a vigiar em soja:** volta abaixo de 1.180,00 desfaria o rompimento (folga
  atual +11,78%).
- **Nível técnico a vigiar em óleo:** recuperação acima de 72,00 desfaria a leitura de
  suporte rompido (distância atual -5,78%).
- **Crush margin:** retorno acima de US$2,50/bushel encerraria a leitura de suporte rompido
  monitorada pela fila (distância atual -2,62%).
- **Prêmio de exportação de farelo e óleo em Paranaguá**, congelado há 19 dias corridos.
- **NOPA mensal**: mais um "release" sem dado novo de fato (paywall), agora referenciado
  como `release-nopa-2026-09-27`.
- **Confirmação da centralização plena da exportação de palma pela Danantara** — alvo
  01/09, já 26 dias passados sem confirmação.
- **Vigência da isenção PIS/Cofins do biodiesel** (58 dias vencida) e **MP 1.358/2026 da
  gasolina** (78 dias vencidos) — checar notícia de renovação/expiração.
- **Marco de 114 dias sem revisão humana do `tributario_watch.toml`**.
- **Revisão de D+180 da tese original do ratio Far/Soj**, programada para 2026-12-08 (72
  dias à frente).
- **Persistência da chuva prevista em Passo Fundo/RS** — primeira menção efetiva de pancada
  de chuva (não só "possibilidade") nesta janela; vale acompanhar se o padrão se repete nos
  próximos boletins.

## Honestidade

- **O achado central desta leitura é que a palavra "confirmado", usada nas duas últimas
  leituras para descrever o fechamento de 25/09, não se sustentou.** A leitura de 26/09
  já havia registrado essa sessão como plenamente corrigida (volume saudável, OHLC distinto
  do dia anterior) depois de uma correção anterior que havia mudado tanto o dia 24/09
  quanto o 25/09. O dump de hoje muda o fechamento e o volume dos três contratos (soja,
  farelo, óleo) mais uma vez, mantendo abertura/máxima/mínima estáveis. Isso significa que,
  pelo menos para esta sessão específica, o processo de captura ainda não havia se
  estabilizado mesmo dois dias depois de o dado ter sido tratado como final numa leitura
  publicada — um nível de instabilidade maior do que qualquer ocorrência anterior desta
  série, porque desta vez a instabilidade sobreviveu a um ciclo completo de
  "suspeita→confirmação" já documentado.
- **O heating oil (HO=F) é o caso mais extremo: já são três valores de fechamento
  publicados para o mesmo dia (25/09) — 4,5214, depois 4,5799, agora 4,6847 — e, desta
  vez, mesmo a abertura, a máxima e a mínima mudaram**, não só o fechamento. Isso é
  qualitativamente diferente do padrão anterior (onde só o fechamento variava e o resto do
  OHLC ficava duplicado). Não há, neste momento, nenhuma base para prever se uma quarta
  geração trará um quarto valor ainda diferente.
- **A direção do erro introduzido pela revisão mudou de sentido entre ontem e hoje.** A
  revisão de ontem havia tornado a margem de biodiesel mais bearish do que o número
  provisório original sugeria (a leitura de 25/09 registrava 1,8314; a de 26/09, revisando
  para baixo o HO=F, calculou 1,8584 como "queda de -8,41%" frente a 24/09). A revisão de
  hoje inverte essa direção: revisando o HO=F para cima, a margem recalcula para 1,9617 —
  uma queda de apenas -3,32% frente a 24/09, bem menor. Ou seja, em três gerações, o mesmo
  dado passou de "moderadamente bearish" para "muito bearish" e agora para "levemente
  bearish" — a direção qualitativa (queda frente a 24/09) se manteve nas três versões, mas
  a magnitude oscilou o suficiente para mudar a força do argumento operacional.
- **O volume revisado de farelo em 24/09 (105.415 contratos) é, no dump de hoje,
  numericamente idêntico ao volume revisado de farelo em 25/09 (também 105.415)** — dois
  dias distintos, com OHLC diferente entre si, mas volume idêntico até o último dígito. O
  mesmo padrão aparece no heating oil: volume de 33.058 contratos tanto em 24/09 quanto em
  25/09 no dump de hoje. Isso pode ser coincidência estatística, mas, dado o histórico desta
  série de encontrar exatamente esse tipo de repetição como sintoma de captura problemática,
  é tratado aqui como um sinal de atenção, não como confirmação de anomalia.
- **O WASDE segue ausente do dump pela segunda leitura consecutiva** — não está claro se é
  falha temporária de captura ou mudança na disponibilidade da fonte.
- **Percentil histórico de posicionamento COT não está disponível no briefing** — toda
  leitura de "fundos comprando/vendendo" nesta série usa variação absoluta semana a semana
  de contratos, não percentil histórico; não é possível dizer se o net long atual de
  farelo, soja ou óleo está em nível historicamente esticado ou ainda distante de extremos.
- **O item de fila `release-nopa-2026-09-27` é mais uma repetição sem dado novo** — o mesmo
  padrão de todas as leituras anteriores desde que este monitoramento começou (paywall,
  `monthly_status` em 0,0 bool).
- **`tributario_watch.toml` sem atualização há 114 dias corridos** — pelo menos dois
  vetores (isenção PIS/Cofins do biodiesel, MP 1.358/2026) já passaram da vigência
  registrada sem nota de renovação ou expiração.
- **A previsão INMET para 27/09 é previsão meteorológica, não medição de precipitação ou
  temperatura real** — a menção a "pancadas de chuva e trovoadas isoladas" em Passo Fundo/RS
  é indicativa do boletim, não confirmação de que o evento ocorreu ou ocorrerá.
- **MPOB (palma Malásia) segue com parser quebrado** — nenhum dado de produção/estoque de
  palma malaia disponível, o que impede monitorar diretamente o catalisador represado da
  centralização de exportação indonésia (Danantara).
- **Não há seção `bcba` (Argentina) neste dump** — nenhum dado direto de safra ou
  exportação argentina disponível, e ainda sem WASDE para consolidar indiretamente esse
  dado.
- **Os forecasts estatísticos internos (bandas 7d/30d) foram gerados hoje sobre o
  fechamento de 25/09 ora revisado pela terceira vez** — o viés "altista" em farelo e
  "baixista" em óleo (ambos horizontes) refletem extrapolação estatística de tendência
  (MA20 + volatilidade + slope), não uma reavaliação fundamentalista, e herdam a mesma
  incerteza do dado de origem.
- **Os índices ISF e ISO ganharam um carimbo em 2026-09-27 no dump de hoje**, repetindo os
  mesmos valores de 60/100 e 80/100 já vigentes desde 11/09 — tratado aqui como
  continuidade, não como confirmação nova.
- **A fila de julgamento volta a listar as revisões D+7 e D+90 da tese de 11/06 como
  "vencidas"** — o veredito de ambas já foi fechado em
  [[2026-09-17_ratio-far-soj-supera-nivel-de-abertura-da-tese-original-quarta-sessao]] e
  reafirmado em [[2026-09-09_d90-ratio-far-soj-reverte-na-vespera]]; o sistema de fila não
  lê de volta os insights publicados para marcar a revisão como encerrada. Nenhuma ação
  nova é necessária sobre essas duas revisões específicas.
- **Sem sessão de mercado, sem corte de COT e sem leitura física nova, boa parte desta
  leitura é, por natureza, uma auditoria de qualidade de dado sobre a sessão de 25/09, não
  uma reavaliação fundamentalista nova** — o viés de todas as três pernas permanece o mesmo
  da leitura de ontem porque não surgiu nenhum fato novo de mercado capaz de mudá-lo, e não
  porque a tese tenha sido reafirmada por dados frescos hoje.
