---
data: 2026-09-21
titulo: "Chicago segue sem fechamento novo em grãos desde sexta-feira (18/09) e a reabertura de hoje ainda não aparece neste dump, mas dois dados frescos mudam o tabuleiro: o físico de farelo em Mato Grosso (IMEA) saltou +3,68% no mesmo dia em que o futuro caiu -3,42% (divergência que reforça o bull-farelo doméstico) e a primeira sessão de heating oil da semana — ainda sobre volume residual de 901 contratos — caiu -3,27%, um ingrediente bear-óleo novo, mas ainda a confirmar"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT — sessão de **2026-09-18** (sexta-feira; segue sendo o único fechamento de grãos disponível neste dump, mesmo hoje sendo segunda-feira 21/09 — ver Honestidade): soja (ticker ZSX26.CBT, venc. nov/26) abertura 1.317,50, máxima 1.322,00, mínima 1.300,00, fechamento **1.303,50**, volume 108.222 contratos; farelo (ticker ZMZ26.CBT, venc. dez/26) abertura 370,00, máxima 372,30, mínima 356,60, fechamento **358,60**, volume 113.303 contratos; óleo (ticker ZLZ26.CBT, venc. dez/26) abertura 69,17, máxima 69,20, mínima 68,01, fechamento **68,22**, volume 67.046 contratos. Curva futura em 18/09 — soja: nov/26 (base) 1.303,50 → jan/27 1.320,00 → mar/27 1.329,50 → mai/27 1.336,50 → jul/27 1.340,50; farelo: out/26 354,60 → dez/26 (base) 358,60 → jan/27 360,40 → mar/27 361,70 → mai/27 362,30; óleo: out/26 67,70 → dez/26 (base) 68,22 → jan/27 68,52 → mar/27 68,69 → mai/27 68,75
  - CME NYMEX heating oil (HO=F) — **2026-09-20** (domingo, primeira sessão eletrônica da semana capturada neste dump — DADO NOVO, ver Visão geral e Honestidade): abertura 4,9248, máxima 4,9615, mínima 4,8883, fechamento **4,8926** USD/galão, volume **901 contratos** (vs. 45.315 na sessão de 18/09 — cerca de 2% do volume típico, sinal de sessão ainda muito incipiente)
  - CME NYMEX heating oil (HO=F) — **2026-09-18** (fechamento revisado, referência de comparação): fechamento **5,0578** USD/galão, volume 45.315 contratos
  - Indicadores sintéticos internos (`indicators`) — série completa dos últimos cinco fechamentos com fórmula publicada (14 a 18/09, sem registro de ratio/crush/margem para 19 ou 20/09 porque não há preço novo de grãos nesse intervalo — ver Honestidade): farelo 356,20 → 365,40 → 365,60 → 371,30 → **358,60**; óleo 70,19 → 70,35 → 69,67 → 69,15 → **68,22**; soja 1.304,25 → 1.318,75 → 1.320,50 → 1.319,75 → **1.303,50**; ratio Far/Soj 81,93% → 83,12% → 83,06% → 84,40% → **82,53%**; oil share 49,05% → 48,79% → 48,22% → **48,75%**; oil-meal spread -0,3003 → -0,3795 → -0,5621 → **-0,385** USD/bushel; crush margin 2,5898 → 2,5019 → 2,5776 → **2,3584** USD/bushel; paridade BR soja 149,70 → 150,00 → 149,90 → **148,21** BRL/saca; margem biodiesel US 2,3508 → 2,3863 → 2,2927 → **2,3063** USD/galão (todos 14 a 18/09); ISF (Índice de Sobra de Farelo) e ISO (Índice de Suporte do Óleo) confirmados sem mudança em **2026-09-19 e 2026-09-20** (60/100 e 80/100, mesmo critério "3/5" e "4/5 condições" desde 11/09)
  - NAG físico BR (`nag_fisico`) — **2026-09-18**: farelo Mato Grosso/IMEA **R$1.982,28/ton (+3,68% frente a 16-17/09, DADO NOVO relevante, ver Farelo)**; farelo Rondonópolis/MT (BCSP) R$2.030,00/ton (var 0,0%, terceira sessão seguida flat); farelo média Rio Grande do Sul (Clicmercado) R$1.860,00/ton (var 0,0%, mesmo valor em toda a janela visível desde 08/09); soja Paraná interior (CEPEA/ESALQ via NAG) R$155,18/saca (+0,15%); prêmio export farelo Paranaguá 0,12 USD/short_ton (congelado desde 08/09, agora 13 dias corridos); prêmio export óleo Paranaguá 0,1 cts/lb (mesmo congelamento)
  - CEPEA/ESALQ Soja Paranaguá (via NAG) — **2026-09-18**: R$161,89/saca (var -0,08% frente a 17/09)
  - BCB PTAX — **2026-09-18** (última publicação; sem PTAX no fim de semana nem ainda hoje): USD/BRL **5,1575**, EUR/BRL 5,9126, Selic diária 0,050788% a.a. (séries SGS 1, 21619, 11)
  - CFTC COT Managed Money — corte de **2026-09-15** (sem corte novo; próximo corte 22/09, esperado por volta de 25-26/09): farelo net long 183.111 contratos (+16,12% vs 08/09); óleo net long 101.480 (+10,65%); soja net long 241.501 (-6,13%)
  - USDA Crop Progress — corte de **2026-09-13** (sem corte novo nesta janela; o corte semanal de hoje, segunda-feira 21/09, ainda não aparece neste dump — ver Honestidade): 12% excelente / 46% boa (G/E 58%), colheita 2025/26 em 6% concluída
  - USDA WASDE — edição de **2026-09-11** (sem edição nova): farelo Argentina 2026/27 exportação 2,99 mi t; farelo Brasil 2025/26 exportação 0,2 mi t
  - NOPA — item de fila `release-nopa-2026-09-20`: `monthly_status` em 0,0 bool (paywall, sem dado novo)
  - Notícias Agrícolas/Canal Rural (RSS) — headline de **2026-09-19**, DADO NOVO nesta leitura: "Conab diz que Brasil será, mais uma vez, o maior provedor de soja do mundo; quanto a produção deve crescer em 26/27?" (Canal Rural) — apenas título disponível, sem corpo de texto nem número (ver Soja e Honestidade)
  - ABIOVE projeções mensais — balanços out-dez/2026, sem revisão nesta janela
  - NOAA CPC ENSO — El Niño Advisory, inalterado (carimbo 2026-09-20)
  - MPOB — carimbo 2026-09-20, parser sem números extraídos (mesma barreira há semanas)
  - BCBA (Argentina) — carimbo 2026-09-09, scraper acessa a página mas não encontra links de relatório
  - INMET — previsão para **2026-09-21 (HOJE)**: Cascavel/PR 31°C/14°C, manhã e tarde "muitas nuvens com pancadas de chuva e trovoadas isoladas", noite com **possível queda de granizo** (risco que havia desaparecido da previsão de ontem); Maringá/PR 33°C/20°C, pancadas de chuva e trovoadas; Passo Fundo/RS 27°C/11°C, **"possível queda de granizo" nos três períodos do dia** e mínima caindo de 17°C (previsão de ontem) para 11°C; no núcleo de Mato Grosso, Cuiabá 37°C/24°C (recuo de 41°C ontem), Sinop 39°C/26°C, Sorriso 38°C/25°C, Lucas do Rio Verde 38°C/25°C (todos "muitas nuvens" com chuva isolada/trovoadas), Rio Verde/GO 36°C/23°C
  - system/tributario_watch.toml (lido como referência, não editado) — `atualizado_em` 2026-06-05 em todos os 10 eventos catalogados, **108 dias corridos** sem revisão humana frente a hoje (21/09)
  - Forecasts estatísticos internos (bandas 7d/30d) — geração de **2026-09-20**, sobre o fechamento de 18/09, alvos 27/09 e 20/10: viés "altista" em soja, farelo e óleo nos dois horizontes (extrapolação estatística, não fundamentalista — ver Honestidade)
  - Fila de julgamento (carimbada "2026-09-20" no briefing, 8 itens, mesmos fatos-base de 18/09 já tratados nas leituras de 19 e 20/09, todos revisitados nesta leitura à luz dos dados novos de hoje): `alerta-quebra_resistencia-soja_cbot-2026-09-18`, `alerta-quebra_suporte-oleo_cbot-2026-09-18`, `alerta-quebra_resistencia-farelo_cbot-2026-09-18`, `alerta-movimento_forte-farelo_cbot-2026-09-18`, `alerta-quebra_suporte-complexo_soja-2026-09-18`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`, `release-nopa-2026-09-20`
  - Cruza com [[2026-09-20_leitura-complexo]] (leitura de ontem, que já registrou a rolagem de contrato farelo/óleo para dezembro/26 e a quarta revisão do HO=F), [[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]] (as quatro ocorrências documentadas do padrão de revisão do HO=F, hoje com uma quinta observação a monitorar), [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (tese original do ratio, nível de abertura 81,4%) e [[2026-09-17_ratio-far-soj-supera-nivel-de-abertura-da-tese-original-quarta-sessao]] (veredito de invalidação técnica da tese baixista de junho)
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
farelo vira o motor de rentabilidade do esmagador). Hoje, 82,53% (última leitura disponível,
18/09), o complexo está no meio dessa zona neutra — nem sobra escancarada, nem aperto.

**Hoje é segunda-feira, 2026-09-21, e este dump ainda não traz nenhum fechamento novo de
soja, farelo ou óleo em Chicago** — o último preço de grãos disponível continua sendo o de
sexta-feira, 18/09. Isso é diferente do padrão do fim de semana (sábado/domingo sem pregão,
já documentado nas leituras de 19 e 20/09): hoje o pregão eletrônico já deveria estar em
andamento, mas a captura de dados deste sistema ainda não reflete isso para os três
contratos agrícolas — apenas o heating oil (HO=F, usado na fórmula da margem de biodiesel)
aparece com uma sessão nova, e mesmo essa sessão está claramente incipiente (ver abaixo).
Por isso, esta leitura trata os números de sexta como o "estado do mundo" vigente, mas
incorpora dois dados genuinamente novos que chegaram entre ontem e hoje e que merecem
tratamento completo, não apenas repetição do fechamento anterior.

**Achado 1 — a primeira sessão de heating oil da semana caiu -3,27%, mas sobre volume
residual.** O HO=F, cotado no NYMEX e usado como a perna de "receita" da fórmula interna de
margem de biodiesel americana, aparece pela primeira vez com uma linha datada de
**2026-09-20** (domingo): abertura 4,9248, máxima 4,9615, mínima 4,8883, fechamento
**4,8926 USD/galão** — uma queda de **-3,27%** frente ao fechamento revisado de sexta-feira
(5,0578). O detalhe que pede cautela: o volume dessa sessão é de apenas **901 contratos**,
contra 45.315 na sessão cheia de 18/09 — ou seja, cerca de **2% do volume típico**. Isso é
a assinatura clássica de uma sessão eletrônica ainda no início (o pregão de energia do NYMEX
reabre no domingo à noite, horário dos EUA, bem antes da reabertura dos contratos agrícolas
da CBOT), não um fechamento consolidado do dia. Como o próprio insight
[[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]] já documentou quatro vezes
seguidas (11, 16, 17 e 18/09) que o HO=F sofre revisão para cima em gerações posteriores do
dump, o valor de hoje (4,8926) deve ser tratado como **provisório** até a próxima geração
confirmar ou revisar — mas, direcionalmente, é o primeiro sinal da semana de energia mais
fraca, o que, se sustentado, comprime a receita da margem de biodiesel (a fórmula interna é
receita = HO + 1,5×RIN D4, custo = óleo + industrial) e reforça, de forma ainda tentativa, o
viés baixista em óleo.

**Achado 2 — o físico de farelo em Mato Grosso subiu +3,68% no mesmo dia em que o futuro
caiu -3,42%, uma divergência que não aparecia nas leituras anteriores.** O preço do farelo
físico em Mato Grosso, fonte IMEA (via NAG), passou de R$1.911,88/ton (estável em 16 e 17/09)
para **R$1.982,28/ton em 18/09 — uma alta de +3,68%** no mesmo dia exato em que o farelo
futuro em Chicago (contrato dezembro/26) caiu -3,42% (371,30 → 358,60). Essa é uma
divergência de quase **7,1 pontos percentuais entre o físico doméstico e o futuro
internacional na mesma sessão** — o tipo de descolamento que, quando real, costuma refletir
um fator de demanda ou logística puramente doméstico (aperto de originação local, custo de
frete, concorrência entre compradores de ração) que não tem correspondência no mercado
futuro de referência. Isso é tratado com destaque na seção Farelo abaixo, mas com uma
ressalva importante: **as outras duas praças físicas de farelo no mesmo dump (Rondonópolis/MT
via BCSP e a média do Rio Grande do Sul via Clicmercado) não mostram nenhum movimento — ambas
ficaram completamente flat** nas mesmas datas, o que levanta a possibilidade de o salto do
IMEA ser um evento pontual de uma única fonte, não uma confirmação ampla do mercado físico
brasileiro (ver Honestidade).

Com esses dois achados registrados, o retrato de sexta-feira (18/09) que segue sendo a
referência de preço vigente é o mesmo já descrito nas leituras anteriores: farelo -3,42%
(371,30 → 358,60), óleo -1,34% (69,15 → 68,22) e soja -1,23% (1.319,75 → 1.303,50), com o
ratio Far/Soj fechando em 82,53% — dentro da zona neutra (80-87%), mas ainda acima do nível
de abertura da tese baixista de junho (81,4%, com a ressalva de comparabilidade de contrato
já registrada em [[2026-09-20_leitura-complexo]]). O crush margin segue em US$2,3584/bushel,
abaixo do piso de referência de US$2,50 monitorado pela fila.

**Leitura de uma linha**: nada mudou no preço de grãos desde sexta — Chicago ainda não
reabriu neste dump —, mas os dois achados de hoje puxam o complexo em direções opostas: o
salto isolado do físico de farelo em MT reforça (ainda que com ressalva de confirmação) o
bull-farelo doméstico, enquanto a primeira sessão fraca de heating oil da semana acrescenta
um ingrediente bear-óleo novo, ainda que sobre volume residual e sujeito a revisão. O pivô do
complexo continua sendo o ratio Far/Soj, em 82,53% — dentro da zona neutra, mas mais perto do
território apertado (87%) do que do abundante (80%). Maior convicção: bull-farelo moderado,
hoje ligeiramente reforçado pelo dado físico de MT (com ressalva). Confiança em soja
permanece **neutra**, mantida da leitura anterior, sem informação de preço nova para mudar o
quadro — mas com um novo contraponto qualitativo (a manchete da Conab sobre recorde de oferta
brasileira) a monitorar. Bear-óleo segue moderado, hoje com um argumento técnico novo a favor
(HO=F fraco), mas provisório o suficiente para não elevar a convicção.

## Soja

**Viés: neutro, mantido da leitura anterior — sem preço novo em Chicago para confirmar ou
desmentir a queda de sexta-feira, e com um novo contraponto qualitativo (manchete de oferta
recorde da Conab) que pesa, ainda que sem número, para o lado baixista.**

O que sustenta a tese (lado altista):

- **A soja segue acima da resistência de referência de 1.180,00** (fila
  `alerta-quebra_resistencia-soja_cbot-2026-09-18`: fechamento 1.303,50 vs. nível 1.180,00),
  uma folga de **+10,47%** — distância confortável do nível de invalidação formal da tese,
  ainda sem qualquer novo fechamento que a teste.
- **A curva futura permanece em contango regular**: nov/26 (base) 1.303,50 → jan/27 1.320,00
  → mar/27 1.329,50 → mai/27 1.336,50 → jul/27 1.340,50 (CME CBOT, 18/09) — sem sinal de que o
  mercado a termo esteja precificando a queda de sexta como reversão estrutural.
- **A condição da lavoura americana segue estável**, sem novo corte nesta janela. USDA Crop
  Progress, corte de 13/09: 12% excelente + 46% boa (G/E 58%, inalterado desde 30/08), 6% da
  safra 2025/26 colhida. O corte semanal de **hoje, segunda-feira 21/09**, ainda não aparece
  neste dump (ver Honestidade) — é o primeiro catalisador concreto do dia a monitorar.
- **A previsão do núcleo produtor de Mato Grosso segue favorável à germinação**: Cuiabá,
  Sinop, Sorriso e Lucas do Rio Verde todos entre 37-39°C com "muitas nuvens" e chance de
  chuva isolada/trovoadas — o mesmo padrão de calor moderado com umidade que já vinha
  sustentando a leitura de plantio nas últimas semanas, hoje com máximas até 4°C mais amenas
  que ontem (Cuiabá recuou de 41°C para 37°C), o que reduz o risco de estresse térmico extremo
  sobre o plantio em curso.
- **O câmbio ainda não tem PTAX de hoje** (última publicação 18/09, USD/BRL 5,1575) — sem
  fator cambial novo para mover a paridade brasileira de soja, que segue em R$148,21/saca
  (indicators, 18/09).

**O que invalida / risco:**

- **A soja fechou em queda pela segunda sessão seguida na última leitura disponível** (doji de
  quinta seguido da queda de sexta): 1.304,25 (14/09) → 1.318,75 → 1.320,50 → 1.319,75 →
  **1.303,50 (-1,23%)** — desaceleração de momentum que segue sem confirmação ou desmentido
  por falta de pregão novo.
- **O COT de 15/09, ainda o mais recente, mostrou os fundos reduzindo net long em soja em
  -6,13%** (de 257.258 para 241.501 contratos), com short subindo +14,25% — o próximo corte
  (posições de 22/09, esperado 25-26/09) é o primeiro capaz de dizer se esse movimento se
  acentuou.
- **Manchete nova da Conab (via Canal Rural, 19/09, `noticias_rss`): "Conab diz que Brasil
  será, mais uma vez, o maior provedor de soja do mundo; quanto a produção deve crescer em
  26/27?"** — este sistema não tem acesso ao corpo da matéria, apenas ao título (ver
  Honestidade), então não é possível citar um número de área ou produção projetada. Ainda
  assim, o próprio enquadramento da manchete (Brasil mantendo a liderança global e produção
  "crescendo" em 26/27) é, em si, um sinal qualitativo de oferta abundante que pesa no sentido
  baixista de médio prazo para soja — o tipo de notícia que, historicamente, quando ganha
  números concretos (área plantada, produtividade projetada), costuma pressionar o prêmio de
  exportação brasileiro e, por relação de arbitragem, o próprio CBOT.
- **A previsão climática de hoje reintroduz risco de granizo no Sul, ausente na previsão de
  ontem**: Cascavel/PR volta a mostrar "possível queda de granizo" à noite (não constava na
  previsão de ontem para o mesmo dia), e Passo Fundo/RS mostra o mesmo risco nos três períodos
  do dia, com a mínima caindo de 17°C (previsão de ontem) para **11°C** hoje — o maior recuo
  de mínima em qualquer boletim desta série recente. Numa fase de semeadura, o risco maior de
  granizo/frio é sobre estabelecimento de estande (replantio localizado) mais do que sobre
  produtividade final, mas é um fator a monitorar caso se confirme na prática (o boletim é
  previsão, não medição — ver Honestidade).
- **Nível técnico a vigiar:** um fechamento de volta abaixo de 1.180 desfaria formalmente o
  rompimento; com a folga ainda em +10,47%, esse cenário segue distante.

**Leitura operacional:** sem preço novo em Chicago, não há ação concreta a tomar antes da
reabertura efetiva — mas o conjunto de evidências (dois fechamentos desfavoráveis seguidos,
COT já mostrando fundos mais cautelosos, e agora uma manchete de oferta recorde brasileira)
é o mais desfavorável ao lado comprado desde a reabertura de 11/09, mesmo sem nenhum dado
capaz de confirmar isso com preço. Para quem está comprado, o corte de Crop Progress de hoje
à tarde (horário americano) e a abertura efetiva do pregão são os dois catalisadores a vigiar
antes de qualquer decisão de reforçar posição — um gap de queda combinado com um corte de
condição pior seria o primeiro sinal técnico e fundamentalista simultâneo desde a reabertura
de setembro. Para quem opera vendido, a mínima de sexta (1.300,00) e a máxima de sexta
(1.322,00) seguem como referências de entrada/stop para uma operação tática, sem que a tese
estrutural de alta (acima de 1.180) esteja tecnicamente desfeita.

## Farelo

**Viés: bull, moderado — mantido, e hoje com um reforço tentativo vindo do físico de Mato
Grosso, ainda que sem confirmação das demais praças físicas monitoradas.**

O que sustenta a tese:

- **O físico de farelo em Mato Grosso (IMEA, via NAG) saltou +3,68% em 18/09, de R$1.911,88
  para R$1.982,28/ton** — no mesmo dia em que o futuro em Chicago caiu -3,42%. O mecanismo
  mais provável para esse tipo de descolamento é doméstico: originação mais apertada de
  farelo pronto-entrega no polo esmagador de MT, concorrência entre fábricas de ração por
  volume físico, ou um ajuste pontual de frete/logística que não tem contrapartida no
  contrato futuro internacional (que precifica entrega em Chicago, não em Rondonópolis ou
  Cuiabá). Esse tipo de divergência, quando se confirma em mais de uma sessão, tende a ser um
  sinal de que a demanda doméstica por farelo está mais forte do que o preço internacional
  sozinho sugere — coerente com a tese estrutural de "farelo apertado" que vem sendo
  construída desde a reabertura de 11/09. **Mas essa confirmação ainda não existe**: ver
  ressalva abaixo.
- **O ratio Far/Soj fechou em 82,53% em 18/09** — dentro da zona "neutra" (80-87%), acima do
  limiar de 80% pela sétima sessão seguida desde 11/09, e ainda acima do nível de abertura da
  tese baixista original de 11/06/2026 (81,4%, [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]),
  uma folga de +1,13 pontos percentuais. O veredito de invalidação técnica dessa tese, fechado
  em [[2026-09-17_ratio-far-soj-supera-nivel-de-abertura-da-tese-original-quarta-sessao]],
  segue de pé, com a ressalva de comparabilidade de contrato (rolagem de julho → outubro →
  dezembro/26) já registrada em [[2026-09-20_leitura-complexo]] — trata `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
  e `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`: ambas as revisões
  seguem "vencidas" no sentido de que a fila não lê o insight publicado, mas o veredito já
  está fechado e não muda hoje, por falta de preço novo.
- **O farelo segue acima da resistência histórica de 325,00** (fila
  `alerta-quebra_resistencia-farelo_cbot-2026-09-18`: 358,60 vs. 325,00), folga de +10,34%
  (com a mesma ressalva de rolagem de contrato).
- **A trajetória sazonal da ABIOVE para o Brasil continua apontando para alívio de oferta
  doméstica de farelo**, sem revisão nesta janela: produção projetada caindo de 2.143 mil t
  (out/26) para 1.978 (nov/26) e 1.659 mil t (dez/26); exportação de 850 para 800 e 700 mil t
  no mesmo período.
- **O COT de 15/09 mostrou os fundos ampliando net long em farelo em +16,12%** (de 157.689
  para 183.111 contratos) — a maior variação percentual de toda a série disponível, ainda o
  dado mais recente de posicionamento.

**O que invalida / risco:**

- **A alta do físico IMEA não é confirmada pelas outras duas praças físicas de farelo no
  mesmo dump.** Rondonópolis/MT (fonte BCSP) ficou flat em R$2.030,00/ton por três sessões
  seguidas (16, 17 e 18/09); a média do Rio Grande do Sul (fonte Clicmercado) ficou flat em
  R$1.860,00/ton em **toda a janela visível do dump, de 08/09 a 18/09** — sete pontos de dados
  idênticos, dígito a dígito, o que é estatisticamente improvável para uma série de preço
  físico genuíno e sugere que essa fonte específica pode estar simplesmente não atualizando
  (ver Honestidade). Sem uma segunda praça confirmando o movimento de MT, o salto de +3,68% do
  IMEA deve ser tratado como um sinal preliminar de uma única fonte, não como confirmação
  ampla de aperto físico nacional.
- **A queda de -3,42% do futuro em 18/09 é, mesmo numa base de contrato consistente, a maior
  queda percentual de todo o histórico recente da série** — o tipo de movimento que
  normalmente pede pelo menos uma sessão de confirmação antes de se assumir retomada da alta.
- **A rolagem de contrato (outubro → dezembro/26), explicada em [[2026-09-20_leitura-complexo]],
  segue exigindo cautela em qualquer comparação de nível absoluto** contra 325,00 ou contra os
  81,4% de abertura da tese de junho.
- **Os índices sintéticos ISF e ISO seguem travados em 60/100 e 80/100**, agora confirmados
  sem mudança em 19 e 20/09 — dez dias corridos desde 11/09 sem qualquer reação, apesar do
  ratio e do crush margin terem oscilado de forma expressiva nesse período.
- **O prêmio de exportação de farelo em Paranaguá segue congelado em 0,12 USD/short_ton há 13
  dias corridos** (desde 08/09) — nenhum sinal de aperto ou folga vindo do canal de exportação
  physical, o que também pesa contra tratar o salto do IMEA como um movimento de mercado
  amplo, já que um aperto real de originação doméstica costuma, mais cedo ou mais tarde,
  aparecer também no prêmio FOB.

**Leitura operacional:** sem pregão novo em Chicago, a postura recomendada segue a mesma da
leitura anterior — para quem está comprado em farelo ou no spread Far/Soj comprado, a
extensão já alcançada e a magnitude da correção de sexta pedem cautela e dimensionamento
reduzido até uma segunda sessão confirmar a continuidade da tese. O dado físico de MT, se
genuíno, é um argumento adicional a favor do lado comprado, mas a ausência de confirmação nas
outras duas praças recomenda não usá-lo como gatilho isolado de reforço de posição — vale a
pena monitorar se o IMEA mantém o novo patamar (R$1.982/ton) na próxima atualização ou se
recua, o que ajudaria a distinguir sinal de ruído. Para quem está vendido, a correção de
sexta no futuro segue sendo a janela tática mais clara, com o mesmo aviso de sempre: o nível
estrutural do ratio (ainda >80%, ainda acima da abertura da tese de junho) e o calendário
sazonal da ABIOVE não mudaram.

## Óleo

**Viés: bear, moderado — mantido, e hoje com um argumento técnico novo a favor (primeira
sessão de heating oil da semana em queda), mas tratado como provisório dado o volume residual
da sessão.**

O que sustenta a tese (preço e estrutura de crush):

- **Óleo fechou em 68,22 USD cts/lb em 18/09**, uma queda de -1,34% frente aos 69,15 de
  17/09. A fila confirma a permanência abaixo do suporte de referência de 72,00
  (`alerta-quebra_suporte-oleo_cbot-2026-09-18`), distância de -5,25% (com a mesma ressalva de
  rolagem de contrato discutida na seção Farelo).
- **NOVO: a primeira sessão de heating oil (HO=F) da semana, datada de 2026-09-20, fechou em
  4,8926 USD/galão — uma queda de -3,27% frente ao fechamento revisado de sexta (5,0578).**
  Como o HO=F é a perna de receita da fórmula interna de margem de biodiesel (receita = HO +
  1,5×RIN D4), uma queda sustentada nessa cotação, se confirmada com volume cheio, comprimiria
  a margem de biodiesel americana e reduziria o incentivo econômico de transformar óleo de
  soja em biodiesel — um mecanismo diretamente baixista para a demanda marginal de óleo. O
  detalhe que impede tratar isso como confirmado: o volume da sessão é de apenas 901
  contratos, ante 45.315 na sessão típica de 18/09 (cerca de 2% do normal) — uma amostra
  pequena demais para servir de base a uma margem recalculada com confiança. Some-se a isso o
  padrão já documentado quatro vezes em [[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]]
  de o HO=F ser revisado para cima em gerações posteriores do dump — se esse padrão se repetir
  uma quinta vez, o valor de hoje pode simplesmente ser corrigido para cima amanhã, esvaziando
  o argumento. Por isso, este achado entra como reforço tentativo do viés bear, não como novo
  pilar de convicção.
- **O ISO (Índice de Suporte do Óleo) segue em 80/100**, confirmado sem mudança em 19 e 20/09
  — os índices compostos continuam sem sinalizar mudança de regime, mas também não melhoram
  para o óleo.
- **A série de fechamentos de óleo em Chicago segue em trajetória de queda acelerada ao longo
  da semana**: 70,19 (14/09) → 70,35 → 69,67 → 69,15 → **68,22 (-1,34%)** — quatro das
  últimas quatro variações diárias negativas ou marginais.

**O que sustenta um piso parcial para a tese — e por que ainda não é definitivo:**

- **A margem de biodiesel de 18/09, com o HO=F revisado, ficou em US$2,3063/galão** — uma
  leve alta de +0,59% sobre os 2,2927 de 17/09, não a queda que uma leitura desatualizada
  havia sugerido (ver [[2026-09-20_leitura-complexo]] para o detalhamento completo da
  correção). Esse contra-argumento fundamentalista segue de pé — a margem não está em colapso
  —, mas o dado novo de hoje (HO=F caindo -3,27% na abertura da semana) é exatamente o tipo de
  movimento que, se confirmado, reverteria essa margem para baixo novamente. Se o HO=F
  fechar a semana perto de 4,89 em vez dos 5,06 usados no cálculo de 18/09, e o óleo em
  Chicago não cair na mesma proporção, a margem recalculada cairia — um cenário a confirmar,
  não um fato já registrado pelo sistema.
- **O RIN D4 (crédito de biocombustível renovável americano) continua constante na fórmula
  interna** — toda a variação da margem de biodiesel nesta janela vem de heating oil e do
  próprio óleo, não de qualquer mudança real no valor do crédito RIN.
- **A curva futura de médio prazo segue em contango regular**: out/26 67,70 → dez/26 (base)
  68,22 → jan/27 68,52 → mar/27 68,69 → mai/27 68,75 — sem sinal de reprecificação estrutural
  de curto prazo.

**A lente fiscal BR reforça o viés baixista estrutural, sem mudança hoje:** a MP 1.363/2026
(subvenção ao diesel fóssil, R$1,12/L, vigente até 31/12/2026) segue plenamente vigente,
barateando o fóssil no mix B15 e reduzindo a competitividade do biodiesel; a isenção de
PIS/Cofins do biodiesel na mistura está **52 dias corridos vencida** (vigência registrada até
31/07/2026) sem sinal de renovação — ver seção Lente fiscal/regulatória BR para o detalhamento
completo.

**Leitura operacional:** com o mercado de grãos ainda sem pregão novo neste dump, o quadro
técnico (fechamento abaixo do suporte de 72,00, ISO travado em 80, série de fechamentos em
queda) segue favorável ao lado vendido direcional, e o dado novo de heating oil acrescenta um
argumento a favor — mas, dado o volume residual e o histórico de revisão do HO=F, a
recomendação é aguardar a confirmação da próxima geração antes de tratar isso como reforço de
convicção. Para quem está vendido, a máxima de sexta-feira (69,20, contrato de dezembro)
segue como referência natural de stop; para quem está comprado, uma quebra clara do padrão
vendedor — por exemplo, um HO=F que se recupere de volta para perto de 5,00 com volume cheio
na reabertura de hoje — seria o primeiro sinal técnico a favor de reduzir a convicção
baixista. Para quem opera o spread farelo-óleo dentro do crush, o oil-meal spread fechou em
-0,385 USD/bushel em 18/09 (indicators), com a mesma ressalva de rolagem de contrato já
discutida.

## Spreads e crush (leitura de complexo)

O ratio Far/Soj, calculado sobre o contrato de dezembro/26 desde 19/09 (ver
[[2026-09-20_leitura-complexo]]), segue sem atualização própria desde 18/09: 82,53%, dentro
da zona neutra (80-87%), mas mais próximo do território "apertado" (87%) do que do
"abundante" (80%) — uma distância de 4,47 pontos percentuais até o teto da zona neutra contra
2,53 pontos até o piso. O oil share, em 48,75% (18/09), mostra o óleo ainda respondendo por
quase metade do valor gerado no esmagamento — uma fatia elevada historicamente, ainda que
tenha recuado de picos acima de 49% na semana. O crush margin, em US$2,3584/bushel, segue
abaixo do piso de referência de US$2,50 monitorado pela fila
(`alerta-quebra_suporte-complexo_soja-2026-09-18`), numa faixa (US$2,35-2,60/bushel) que se
repete há duas semanas sem tendência direcional clara.

O que muda hoje, sem alterar nenhuma dessas três métricas diretamente (porque nenhuma tem
preço novo), é a leitura de risco em torno delas: se o HO=F fraco da primeira sessão da
semana se confirmar, a pressão vem pelo lado do óleo (menos demanda de biodiesel, menos
suporte de preço); se o salto do físico de farelo em MT se confirmar nas próximas sessões
(e, idealmente, aparecer também no prêmio de exportação de Paranaguá, ainda congelado em
0,12 USD/short_ton), a pressão vem pelo lado do farelo (mais aperto doméstico, ratio subindo
em direção à zona apertada). Os dois sinais, se ambos se confirmarem, reforçariam
simultaneamente o mesmo viés já descrito nas leituras anteriores: farelo estruturalmente mais
forte, óleo estruturalmente mais fraco — ampliando, não revertendo, a disputa de "quem manda
no crush" já em curso desde meados de setembro.

Os dois índices compostos por contagem de condições — ISF (60/100) e ISO (80/100) — seguem
travados no mesmo patamar desde 11/09, agora confirmados sem mudança também em 19 e 20/09
(dez dias corridos), apesar de o ratio e o crush margin terem oscilado de forma expressiva
nesse período — o contraponto de sempre nesta série: os limiares desses índices específicos
não reagem a oscilações de curto prazo, apenas a mudanças de regime mais estruturais.

O COT de 15/09, ainda o dado de posicionamento mais recente seis dias depois, retrata os
fundos ampliando net long em farelo (+16,12%) e óleo (+10,65%) e reduzindo em soja (-6,13%)
— um instantâneo de terça-feira que precede a correção de sexta e estabelece a base de
comparação para o próximo corte (posições de 22/09, esperado por volta de 25-26/09), o
primeiro capaz de dizer se os mesmos fundos já começaram a realizar lucro na correção ou se
ampliaram ainda mais as posições de farelo e óleo diante do salto físico e da fraqueza do
heating oil, respectivamente.

## Lente fiscal/regulatória BR

Antes de fechar qualquer tese de preço BR, os vetores tributários/regulatórios vivos que
pesam no complexo — todos do `system/tributario_watch.toml`, cujo carimbo mais recente
(`atualizado_em`) em todos os 10 eventos catalogados é 2026-06-05, ou seja, **108 dias
corridos sem revisão humana** frente a hoje (21/09), um marco que passa a três dígitos há
apenas alguns dias:

- **MP 1.363/2026** (id `MP-1363-2026`, subvenção diesel fóssil R$1,12/L, vigente até
  31/12/2026): barateia o diesel fóssil no mix B15 (mistura obrigatória de 15% de biodiesel),
  reduzindo a competitividade relativa do biodiesel e a demanda doméstica por óleo de soja —
  vetor estrutural de baixa para óleo, plenamente vigente, sem mudança de status.
- **B16 (id `B16-CNPE-2026`, elevação da mistura obrigatória de biodiesel para 16%)** segue
  "adiado", resultado esperado por volta de novembro/2026. Upside represado (~436 mil
  toneladas de demanda potencial adicional de óleo), não corrente — quanto mais perto de
  novembro sem confirmação, maior o risco de o mercado começar a precificar esse catalisador
  antecipadamente, algo a monitorar nas próximas semanas.
- **Isenção de PIS/Cofins do biodiesel na mistura** (id `PISCOFINS-BIODIESEL-ISENCAO`):
  vigência registrada até 31/07/2026 — já **52 dias corridos vencida** frente a 21/09/2026,
  sem registro de prorrogação ou expiração. Cada dia adicional sem notícia de renovação
  aumenta a incerteza de planejamento tributário do setor de biodiesel, um vetor de custo
  indireto sobre a demanda por óleo.
- **MP 1.358/2026** (subvenção gasolina R$0,89/L): vigência registrada até 11/07/2026, agora
  **72 dias corridos vencida**.
- **STJ REsp 2.165.276** (id `STJ-RESP-2165276`, crédito de PIS/Cofins sobre soja em
  biodiesel, direção "alta" para soja/óleo): sem novidade nesta janela.
- **EPA RFS 2026/2027** (id `EPA-RFS-2026-2027`, mandato de biocombustível americano, direção
  "alta" para óleo): sustenta o RIN D4, estável, e o RIN permanece constante na fórmula
  interna de margem de biodiesel usada por este sistema.
- **Crédito 45Z** (id `45Z-CLEAN-FUEL`, em tramitação, direção "mista"): sem novidade.
- **Indonésia — Danantara** (id `DANANTARA-INDONESIA`) e **levy de exportação PMK 9/2026**
  (id `INDONESIA-LEVY-PMK9`): a assunção plena da centralização da exportação de palma pela
  Indonésia tinha alvo 01/09/2026 — já se passaram **20 dias** sem confirmação. Catalisador de
  alta represado para óleo (via substituição com palma) — ainda sem dado de MPOB disponível
  para monitorar diretamente (parser continua quebrado, ver Honestidade).
- **Indonésia B50** (id `INDONESIA-B50`, monitorando, direção "alta"): sem novidade.

Nenhum desses vetores muda a leitura de preço de hoje isoladamente — mas, em conjunto, eles
seguem reforçando a mesma assimetria já descrita em leituras anteriores: o mercado interno
brasileiro tem múltiplos desincentivos correntes ao óleo (MP 1.363 plenamente vigente,
isenção PIS/Cofins já 52 dias vencida) e múltiplos catalisadores de alta represados, não
correntes (B16, Danantara, B50). O óleo brasileiro segue mais fraco estruturalmente até que
algum dos vetores represados vire fato concreto — uma leitura que hoje ganha um reforço
técnico adicional (o HO=F fraco da abertura da semana), ainda que provisório.

## Riscos e eventos próximos

- **Reabertura efetiva de Chicago para grãos, hoje, segunda-feira 21/09** — este dump ainda
  não capturou essa sessão; é o primeiro pregão desde a queda de sexta em todas as três
  pernas. Um segundo fechamento seguido de queda seria o primeiro sinal técnico de que a
  correção é o início de algo mais persistente; uma recuperação devolveria parte da confiança
  perdida em soja e reforçaria a tese em farelo.
- **USDA Crop Progress semanal, esperado na tarde de hoje** (horário americano) — ainda não
  está neste dump. Cai no mesmo dia da reabertura, o que pode produzir dois catalisadores
  simultâneos no primeiro pregão da semana.
- **Confirmação (ou revisão) do fechamento de HO=F de 2026-09-20** — a próxima geração do
  dump é o teste direto de se o padrão de revisão documentado quatro vezes se repete pela
  quinta vez, ou se o valor de 4,8926 se mantém como estava.
- **Confirmação (ou reversão) do salto de +3,68% do físico de farelo em MT (IMEA)** — a
  próxima atualização do NAG é o teste de se esse é um sinal real de aperto doméstico ou um
  evento pontual de uma única fonte.
- **Próximo corte de COT (posições de 22/09), esperado por volta de 25-26/09.** Primeiro
  capaz de confirmar se os fundos que ampliaram net long em farelo e óleo (COT de 15/09) já
  realizaram lucro com a correção de sexta.
- **Nível técnico a vigiar em farelo:** volta abaixo de 325,00 desfaria o rompimento (com a
  ressalva de rolagem de contrato).
- **Nível técnico a vigiar em soja:** volta abaixo de 1.180,00 desfaria o rompimento (folga
  atual +10,47%).
- **Prêmio de exportação de farelo e óleo em Paranaguá**, congelado há 13 dias corridos (desde
  08/09) — se o aperto físico de MT for real, esperar eventualmente refletido também nesse
  prêmio FOB.
- **NOPA mensal**: mais um "release" sem dado novo de fato (paywall), agora referenciado como
  `release-nopa-2026-09-20`.
- **Confirmação da centralização plena da exportação de palma pela Danantara** — alvo 01/09,
  já 20 dias passados sem confirmação.
- **Vigência da isenção PIS/Cofins do biodiesel** (52 dias vencida) e **MP 1.358/2026 da
  gasolina** (72 dias vencidos) — checar notícia de renovação/expiração.
- **Marco de 108 dias sem revisão humana do `tributario_watch.toml`** — pelo menos dois
  vetores (isenção PIS/Cofins biodiesel, MP 1.358/2026) já vencidos sem registro de renovação.
- **Detalhamento da manchete da Conab** sobre oferta recorde brasileira 26/27 — monitorar se
  a fonte RSS traz o corpo do texto ou números concretos (área, produtividade) nas próximas
  atualizações.

## Honestidade

- **Hoje, 2026-09-21, é segunda-feira, e mesmo assim este dump não traz nenhum fechamento
  novo de soja, farelo ou óleo em Chicago** — o último preço de grãos disponível continua
  sendo o de sexta-feira, 18/09. Isso quebra o padrão dos dias anteriores (onde a ausência de
  dado novo era explicada pelo fim de semana sem pregão) e não há, no briefing, uma explicação
  para por que a reabertura de hoje ainda não aparece — pode ser simplesmente o horário de
  captura deste dump (antes do fechamento do pregão de grãos de hoje) ou uma limitação da
  fonte de dados para esses tickers especificamente. O cabeçalho do dump usado por este
  sistema ainda está rotulado "Briefing consolidado — 2026-09-20", um dia atrás da data desta
  leitura — o mesmo padrão de defasagem de um dia observado em todas as leituras anteriores
  desta série.
- **A sessão de heating oil (HO=F) datada de 2026-09-20 tem volume de apenas 901 contratos**,
  cerca de 2% do volume típico de uma sessão cheia (45.315 em 18/09) — um forte indício de que
  essa é uma sessão eletrônica ainda incipiente (o pregão de energia do NYMEX abre no domingo
  à noite, bem antes dos contratos agrícolas da CBOT), não um fechamento consolidado
  comparável aos anteriores. Combinado com o padrão de revisão já documentado quatro vezes em
  [[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]], esta leitura trata o valor de
  4,8926 USD/galão como provisório e sujeito a mudança na próxima geração — a leitura bear-óleo
  reforçada por esse dado é, por isso, tratada como tentativa, não como confirmação.
- **O salto de +3,68% do físico de farelo em Mato Grosso (fonte IMEA, via NAG) não é
  confirmado por nenhuma das outras duas praças físicas de farelo no mesmo dump**
  (Rondonópolis/MT via BCSP e a média do Rio Grande do Sul via Clicmercado, ambas
  completamente flat nas mesmas datas). Mais chamativo ainda: a série de RS aparece com o
  mesmo valor exato (R$1.860,00/ton) em **todos os pontos de dados visíveis do dump, de
  08/09 a 18/09** — sete leituras idênticas dígito a dígito, o que é estatisticamente muito
  improvável para uma série de preço físico genuíno e sugere que essa fonte específica (RS
  via Clicmercado) pode não estar atualizando de fato, um problema de qualidade de dado, não
  necessariamente um mercado real e parado. Isso não invalida o dado do IMEA (uma fonte
  diferente, com metodologia própria), mas reduz a confiança em tratá-lo como confirmação de
  um movimento amplo do mercado físico brasileiro de farelo.
- **A manchete da Conab sobre oferta recorde de soja brasileira (19/09, Canal Rural, via
  `noticias_rss`) está disponível apenas como título — o corpo do texto não está no dump.**
  Não é possível citar nenhum número de área, produtividade ou volume projetado para 2026/27;
  esta leitura tratou a manchete apenas como um sinal qualitativo de enquadramento (oferta
  abundante), não como um dado fundamentalista quantificável.
- **USDA Crop Progress ainda mostra o corte de 13/09 como o mais recente**, mesmo sendo hoje
  o dia em que o corte semanal costuma ser publicado (segunda-feira à tarde, horário
  americano) — não está claro se o corte de hoje simplesmente ainda não saiu no momento da
  captura deste dump ou se há alguma outra razão para a ausência.
- **O corte de COT `release-cftc_cot-2026-09-15` segue sendo o dado de posicionamento mais
  recente**, agora seis dias corridos depois do corte. O próximo corte (22/09, esperado
  25-26/09) resolve essa lacuna.
- **Percentil histórico de posicionamento COT não está disponível no briefing** — toda leitura
  de "fundos comprando/vendendo" nesta série usa variação absoluta semana a semana de
  contratos, não percentil histórico.
- **O item de fila `release-nopa-2026-09-20` é mais uma repetição sem dado novo** — o mesmo
  padrão de todas as leituras anteriores desde que este monitoramento começou (paywall,
  `monthly_status` em 0,0 bool).
- **`tributario_watch.toml` sem atualização há 108 dias corridos** — pelo menos dois vetores
  (isenção PIS/Cofins do biodiesel, MP 1.358/2026) já passaram da vigência registrada sem nota
  de renovação ou expiração.
- **A previsão INMET para 21/09 é previsão meteorológica, não medição de precipitação ou
  temperatura real** — as menções a "chuva", "chuva isolada", "trovoadas" e "possível queda de
  granizo" são indicativas do boletim, não confirmação de que o evento ocorreu ou ocorrerá. A
  reintrodução do risco de granizo em Cascavel/PR e Passo Fundo/RS hoje, ausente na previsão
  de ontem, também não é confirmação de que o evento vai de fato acontecer — apenas que o
  boletim de hoje passou a incluí-lo.
- **Prêmios de exportação (Paranaguá) seguem congelados em 0,12 USD/short_ton (farelo) e 0,1
  cts/lb (óleo) desde 08/09** — 13 dias corridos sem movimento, o que não é confirmado nem
  desmentido pelo salto do físico de MT, já que prêmio FOB e preço físico interno respondem a
  dinâmicas parcialmente distintas.
- **MPOB (palma Malásia) segue com parser quebrado** — nenhum dado de produção/estoque de
  palma malaia disponível, o que impede monitorar diretamente o catalisador represado da
  centralização de exportação indonésia (Danantara).
- **BCBA (Argentina) segue sem links de relatório detectados** — nenhum dado de safra ou
  exportação argentina disponível além do que já vem consolidado pelo WASDE.
- **Os forecasts estatísticos internos (bandas 7d/30d) foram gerados em 20/09, ainda sobre o
  fechamento de 18/09** — o viés "altista" nos três produtos reflete extrapolação estatística
  de tendência (MA20 + volatilidade + slope), não uma reavaliação fundamentalista; esta
  leitura mantém farelo em bull, soja em neutro e óleo em bear a partir da análise
  qualitativa, não das bandas estatísticas.
- **A fila de julgamento voltou a listar os mesmos oito itens já tratados nas leituras de 19 e
  20/09**, com a única mudança sendo o carimbo do item de NOPA (`release-nopa-2026-09-20`, um
  dia à frente do de ontem) — o sistema de fila não lê de volta os insights já publicados para
  marcar a revisão como encerrada. O veredito de invalidação técnica da tese de junho, dado em
  [[2026-09-17_ratio-far-soj-supera-nivel-de-abertura-da-tese-original-quarta-sessao]], segue
  válido. A revisão de D+180, programada para 08/12/2026 pela tese original, ainda não venceu.
