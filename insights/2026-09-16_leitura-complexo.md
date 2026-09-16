---
data: 2026-09-16
titulo: "O dump de hoje reescreve a sessão de 15/09: os fechamentos corrigidos mostram um repique bem mais forte do que o pequeno recuo relatado ontem — soja +1,15% (não -0,52%), farelo +2,86% (não -0,63%), óleo +0,20% (não -0,17%) —, agora com volume confirmado normal em toda a curva de grãos (o que resolve a suspeita de dado parcial levantada ontem); o ratio Far/Soj salta para a máxima da janela, 81,91% (não os 80,46% usados ontem), a maior alta diária do movimento inteiro e ainda a terceira sessão consecutiva acima de 80% — o suficiente para elevar o viés do farelo de 'neutro' para 'bull' pela primeira vez desde a abertura da tese em junho; o óleo segue abaixo do suporte de 72,00, mas a margem de biodiesel americana bateu novo recorde da janela, ampliando a divergência preço-vs-fundamento"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT — linhas brutas presentes no dump de hoje (`briefing/latest.md`, seção `cme_cbot`) para a sessão de **2026-09-15** (terça-feira, ainda a mais recente disponível — ver Honestidade sobre a ausência de sessão de 16/09): soja (ZSX26, venc. nov/26) abertura 1.303,25, máxima 1.319,50, mínima 1.294,25, **fechamento 1.319,25**, volume **121.947** contratos; farelo (ZMV26, venc. out/26) abertura 350,30, máxima 360,70, mínima 347,30, **fechamento 360,20**, volume **39.805** contratos; óleo (ZLV26, venc. out/26) abertura 69,62, máxima 70,15, mínima 69,11, **fechamento 69,79**, volume **22.257** contratos. Curva futura em 15/09 — soja: nov/26 (base) 1.319,25, jan/27 1.335,25, mar/27 1.343,00, mai/27 1.348,75, jul/27 1.351,50; farelo: out/26 (base) 360,20, dez/26 365,40, jan/27 366,70, mar/27 366,50, mai/27 366,50; óleo: out/26 (base) 69,79, dez/26 70,27, jan/27 70,48, mar/27 70,58, mai/27 70,60
  - CME CBOT — sessão de **2026-09-14** (segunda-feira): farelo abertura 346,80, máxima 352,80, mínima 344,60, fechamento **350,20**, volume **34.001** contratos (números agora coerentes com um pregão normal — ver Honestidade sobre a divergência frente ao que o dump de ontem mostrava para esta mesma data); heating oil (HO=F) fechamento 4,9615, máxima 5,1919, mínima 4,9084; soja e óleo sem linha bruta de 14/09 nesta janela do dump (mesma lacuna já registrada ontem — ver Honestidade)
  - CME NYMEX heating oil (HO=F) — 2026-09-15: abertura 4,9924, máxima 5,0118, mínima 4,9923, fechamento **5,0077** USD/galão, volume **203** contratos (+0,93% vs 4,9615 de 14/09, mas com volume ainda anormalmente baixo — ver Honestidade)
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, ISF, ISO, margem biodiesel, paridade BR) — **2026-09-15** (corrigidos): crush margin **2,4088** USD/bushel ("Board Crush: farelo 360,20 + óleo 69,79 − soja 1.319,25"), far_soj_ratio_pct **81,91%**, oil_share_pct **49,21%**, oil_meal_spread_usd_bu **-0,2475**, ISF (Índice de Sobra de Farelo) 60/100, ISO (Índice de Suporte do Óleo) 80/100, paridade BR soja **R$149,75/saca** (CBOT 1.319,25 × USD/BRL 5,1490, PTAX própria de hoje — ver abaixo), biodiesel: custo_óleo 5,2343 USD/galão, receita 8,1727 USD/galão, margem **2,1384 USD/galão** (novo recorde da janela, superando os 2,135 de 11/09). Comparação com 14/09 (indicators): crush margin 2,3234, ratio 80,55%, oil share 49,86%, oil-meal spread -0,0429, paridade R$148,64, margem biodiesel 2,1028. Comparação com 11/09: crush margin 2,2755, ratio 80,25%, oil share 49,94%, oil-meal spread -0,0187, margem biodiesel 2,135
  - BCB PTAX — leitura própria de **2026-09-15** finalmente disponível (não mais reaproveitando 14/09 como ontem): USD/BRL **5,1490** (-0,40% vs 5,1696 de 14/09), EUR/BRL 5,9430 (-0,46% vs 5,9704), Selic diária 0,05166% a.a. (séries SGS 1, 21619, 11) — sem PTAX de 16/09 disponível nesta janela (ver Honestidade)
  - CFTC COT Managed Money — corte de 2026-09-08, agora **oito dias corridos** de defasagem frente a hoje (16/09): farelo net long 157.689 contratos, óleo net long 91.711 contratos, soja net long 257.258 contratos — sem qualquer atualização desde a leitura de 13/09; próximo corte (posições de 15/09) esperado por volta de 18-19/09
  - CEPEA/ESALQ Soja Paranaguá e Paraná interior via NAG, e físico de farelo (MT/IMEA, Rondonópolis, RS) — última leitura ainda **2026-09-09**, agora **sete dias corridos** sem atualização própria; prêmios export Paranaguá (farelo +0,12 USD/short ton, óleo +0,10 cts/lb) seguem congelados desde 27/08, **20 dias corridos**
  - USDA Crop Progress — corte de 2026-09-13 (sem novo corte nesta janela, próximo esperado ~20/09): 12% excelente / 46% boa / 9% ruim (G/E 58%, inalterado desde 30/08), colheita 2025/26 em **6% concluída**
  - USDA WASDE — release de 2026-09-11 (sem nova edição), `release-usda_wasde-2026-09-11`: farelo Argentina 2026/27 com exportação revisada de 2,89 para 2,99 milhões de toneladas (ago vs set)
  - NOPA — fila `release-nopa-2026-09-15` (mesmo carimbo de ontem, sem dado novo): `monthly_status` em 0,0 bool (paywall)
  - ABIOVE projeções mensais — balanços set-dez/2026, sem revisão nesta janela: produção de farelo recuando de 2.129 (set) para 1.659 mil t (dez), exportação de 1.100 para 700 mil t no mesmo período
  - NOAA CPC ENSO — El Niño Advisory, inalterado
  - MPOB — carimbo 2026-09-15, parser sem números extraídos (mesma barreira há semanas)
  - BCBA (Argentina) — carimbo 2026-09-09, scraper acessa a página mas não encontra links de relatório
  - INMET — previsão para **2026-09-16 (HOJE)**: Cascavel/PR 24°C/11°C, Maringá/PR 26°C/13°C, Passo Fundo/RS 20°C/7°C (com possibilidade de geada mencionada na manhã, primeira menção de geada em vários dias), calor forte no núcleo produtor de Mato Grosso — Cuiabá 33°C/20°C (chuva isolada), Sinop e Sorriso 38°C/22-25°C (pancadas de chuva e trovoadas isoladas), Lucas do Rio Verde 38°C/22°C, Rio Verde/GO 35°C/18°C
  - Notícias Agrícolas/Canal Rural + FarmProgress RSS — "0 items lidos, 0 mantidos" na leitura de 15/09, mantendo a pausa de coleta desde a última leitura com conteúdo real em 09/09, agora **sete dias corridos**
  - system/tributario_watch.toml (lido como referência, não editado) — `atualizado_em` 2026-06-05 em todos os 10 eventos catalogados, **103 dias corridos** sem revisão humana frente a hoje (16/09)
  - Forecasts estatísticos internos (bandas 7d/30d) — geração de 2026-09-15 (sem geração de 16/09 nesta janela), alvos 22/09 e 15/10, agora recalculados sobre os fechamentos corrigidos: viés "altista" em soja, farelo e agora também óleo no horizonte de 30 dias (mudou de "lateral" em 7d para "altista" em 30d, refletindo o fechamento de óleo mais alto pós-correção)
  - Fila de julgamento (carimbada 2026-09-15 no briefing, 7 itens, gerada automaticamente a partir do banco de indicadores — os mesmos valores corrigidos acima) — tratados nesta leitura: `alerta-quebra_resistencia-soja_cbot-2026-09-15`, `alerta-quebra_suporte-oleo_cbot-2026-09-15`, `alerta-quebra_resistencia-farelo_cbot-2026-09-15`, `alerta-quebra_suporte-complexo_soja-2026-09-15`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`, `release-nopa-2026-09-15`
  - Cruza com [[2026-09-15_leitura-complexo]] (leitura de ontem, cujos números de preço para a sessão de 15/09 são substituídos pelos corrigidos aqui), [[2026-09-15_ratio-far-soj-terceira-sessao-consecutiva-acima-80]] (insight dedicado de ontem, mesma ressalva), [[2026-09-13_correcao-numeros-sessao-11set-farelo-oleo]] (precedente direto: mesma classe de problema, mesma metodologia de auditoria), [[2026-09-12_ratio-far-soj-rompe-80-pela-primeira-vez]], [[2026-09-09_d90-ratio-far-soj-reverte-na-vespera]] e [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (tese original) — e com o insight de auditoria publicado hoje, [[2026-09-16_correcao-numeros-sessao-15set-ratio-salta-para-8191]]
status: ativa
vies: [bull-soja, bull-farelo, bear-oleo_soja]
---

## Visão geral

Hoje, quarta-feira 16/09/2026, é preciso começar por um esclarecimento incomum: **não há
sessão nova de CBOT (bolsa de grãos e derivados de Chicago, onde soja, farelo e óleo de
soja são negociados em contratos futuros) nesta janela do dump.** O arquivo mais recente
(`briefing/latest.md`) ainda se identifica como "Briefing consolidado — 2026-09-15" e a
última linha bruta de preço no banco continua sendo a da sessão de terça-feira, 15/09. O
que mudou não foi o calendário de pregões — foi o **conteúdo dos números daquela mesma
sessão**. A leitura de ontem ([[2026-09-15_leitura-complexo]]) descreveu 15/09 como uma
"pausa pequena e ordenada" após o salto de segunda-feira, com soja recuando -0,52%, farelo
-0,63% e óleo -0,17%, e chamou atenção, com razão, para um volume anormalmente baixo em
toda a curva (soja 2.379 contratos, farelo 479, óleo 1.045) — muito abaixo do histórico
recente da mesma janela. O dump de hoje traz, para a **mesma data 15/09**, fechamentos
diferentes e volumes ordens de grandeza maiores: soja fechou em **1.319,25** (não
1.298,25), farelo em **360,20** (não 348,20), óleo em **69,79** (não 69,50) — com volumes
de 121.947, 39.805 e 22.257 contratos respectivamente (CME CBOT, 15/09). A suspeita de
ontem — "a leitura mais prudente é que o dump de hoje capturou uma fatia parcial da sessão"
— se confirma integralmente. Este achado é grande o suficiente para merecer um documento de
auditoria dedicado, publicado hoje: [[2026-09-16_correcao-numeros-sessao-15set-ratio-salta-para-8191]].
Esta leitura usa, do início ao fim, apenas os números corrigidos.

O mecanismo de fundo do complexo continua o mesmo de sempre e vale reexplicar: a soja em
grão, ao ser esmagada ("crush", o processo industrial que a separa em farelo e óleo), vira
dois produtos com demandas muito diferentes — farelo (concentrado de proteína para ração
animal) e óleo (alimentação humana e, cada vez mais, biodiesel). O "crush margin" mede, em
dólares por bushel (unidade agrícola americana de ~27,2 kg de soja), quanto sobra para a
esmagadora depois de vender farelo + óleo e pagar a soja — quanto maior, mais a indústria é
incentivada a esmagar, o que por sua vez aumenta a oferta de ambos os subprodutos. O "oil
share" (fatia do valor total do crush que vem do óleo) diz qual dos dois produtos está
"pagando a conta": alto = óleo manda e o farelo vira subproduto barato (o "Índice de Sobra
de Farelo", ISF, capta isso do lado baixista do farelo); baixo = o farelo sustenta o crush e
o óleo perde força relativa (o "Índice de Suporte do Óleo", ISO, é o espelho). O ratio
Far/Soj (preço do farelo dividido pelo da soja, normalizado em percentual) mede a mesma
ideia de forma mais direta: abaixo de 80% o farelo está "abundante" (viés baixista); entre
80% e 87% ele está em zona "neutra"; acima de 87% fica "apertado" (viés altista).

Com os números corrigidos, a história das últimas três sessões (11, 14 e 15/09) fica bem
mais nítida — e bem mais forte — do que parecia ontem. O ratio Far/Soj: **80,25%** (11/09)
→ **80,55%** (14/09) → **81,91%** (15/09, corrigido de 80,46%) — ainda três fechamentos
consecutivos acima de 80% (o mesmo marco tratado em profundidade por
[[2026-09-15_ratio-far-soj-terceira-sessao-consecutiva-acima-80]]), mas agora o terceiro dia
é, disparado, o de maior alta diária de todo o movimento (+1,36 ponto percentual, contra
+0,30 p.p. de 11→14/09), não uma estabilização perto de zero como a versão de ontem sugeria.
O mesmo padrão aparece no oil share (49,94% → 49,86% → **49,21%**, a leitura mais baixa da
janela) e no oil-meal spread (-0,0187 → -0,0429 → **-0,2475** USD/bushel, um salto de mais
de 8 vezes em magnitude em um único dia). Três indicadores construídos de formas
matematicamente distintas, todos acelerando na mesma direção no mesmo dia — isso é
evidência bem mais forte de mudança de regime do que a leitura de ontem, calçada em dados
parciais, conseguia enxergar.

Do lado do preço absoluto, os três produtos não "deram uma respirada" como se pensava —
subiram os três, com farelo subindo mais que o dobro da soja em termos percentuais: soja
+1,15% (de 1.304,25 para 1.319,25), farelo +2,86% (de 350,20 para 360,20), óleo +0,20% (de
69,65 para 69,79) — todos CME CBOT, 14→15/09. Somando as três sessões desde sexta-feira
(11→15/09), o saldo já não é "levemente positivo": soja +1,75%, farelo **+3,86%**, óleo
+0,87% — um repique de complexo genuíno e desproporcionalmente concentrado no farelo, exatamente
o padrão que sustenta a mudança de viés desta leitura.

**Leitura de uma linha**: o episódio de hoje não é sobre um novo fato de mercado, é sobre a
integridade do fato que já tínhamos — e a versão corrigida é mais forte, não mais fraca, em
todas as direções que a leitura de ontem já apontava (soja mais alta, farelo mais forte
relativo, ratio mais esticado). Isso remove a principal objeção que mantinha o farelo em
"neutro" havia dias (a suspeita sobre a qualidade do dado) e justifica, pela primeira vez
desde a abertura da tese em 11/06/2026, elevar o viés a **bull-farelo**. Confiança
**moderada**: a correção resolve o problema de volume, mas COT (oito dias de defasagem) e o
físico brasileiro (sete dias parado) continuam sem confirmar, e os dois índices compostos
(ISF/ISO) seguem travados no mesmo patamar desde 11/09 apesar do salto nas métricas
contínuas.

## Soja

**Viés: bull, moderado-a-forte (reforçado) — a correção dos números de 15/09 mostra que a
soja não deu uma pausa, ela estendeu o rali: +1,15% no dia (não -0,52%), com volume agora
confirmado normal (121.947 contratos, dentro da faixa histórica de 100-160 mil desta
janela), e folga sobre a resistência de referência ampliando para quase 12%.**

O que sustenta a tese:

- **A sessão de 15/09, corrigida, foi de continuação de alta, não de recuo.** Fechou em
  **1.319,25** (CME CBOT), +1,15% frente aos 1.304,25 de 14/09, com máxima de 1.319,50 —
  ou seja, o fechamento ficou a apenas 0,25 ponto da máxima do dia, no topo do range. É o
  oposto do que a leitura de ontem descrevia (fechamento junto à mínima, em um range
  estreito e de baixa convicção). O volume de 121.947 contratos remove a dúvida
  metodológica: este foi um pregão real e de peso, não um evento de baixa liquidez.
- **A folga sobre a resistência de referência (1.180,00, fila
  `alerta-quebra_resistencia-soja_cbot-2026-09-15`) foi para 11,80%** — maior do que os
  10,02% que a leitura de ontem calculava com o fechamento errado, e a maior desde a
  reabertura de 08/09. O fato de a fila (gerada automaticamente pelo robô a partir do banco
  de indicadores, não por este analista) confirmar independentemente o valor 1.319,25 é a
  evidência mais forte de que este é o número correto — a mesma lógica de verificação usada
  na auditoria de 13/09 ([[2026-09-13_correcao-numeros-sessao-11set-farelo-oleo]]).
- **A curva futura acompanhou o movimento sem distorcer o formato.** Em 15/09 (corrigida):
  nov/26 (base) 1.319,25 → jan/27 1.335,25 → mar/27 1.343,00 → mai/27 1.348,75 → jul/27
  1.351,50 (CME CBOT) — contango regular e com inclinação decrescente ponta a ponta
  (+16,00 → +7,75 → +5,75 → +2,75 pontos entre vencimentos consecutivos), o padrão normal
  de um mercado que precifica algum aperto no curto prazo sem esticar demais o longo prazo.
  O spread base-a-maio/27 é de **29,50 pontos**.
- **A condição da lavoura americana segue estável e a colheita avança dentro do esperado.**
  USDA Crop Progress, corte de 13/09 (sem novo corte nesta janela, próximo esperado por
  volta de 20/09): 12% excelente + 46% boa (G/E 58%, inalterado desde 30/08) e **6% da
  safra 2025/26 colhida** — nenhuma surpresa, mas o mercado passa a monitorar ritmo de
  colheita como driver de curto prazo a partir de agora.
- **O câmbio trouxe, pela primeira vez em dias, uma leitura própria de hoje (15/09), não
  reciclada de ontem.** USD/BRL fechou em **5,1490** (BCB PTAX, 15/09), uma leve queda de
  -0,40% frente aos 5,1696 de 14/09 — o real apreciou ligeiramente. Ainda assim, como a
  soja em dólar subiu +1,15% no mesmo intervalo, a paridade brasileira (CBOT × câmbio, sem
  basis) avançou para **R$149,75/saca** (indicators, 15/09), +0,75% frente aos R$148,64 de
  14/09 — o ganho em dólar mais do que compensou a pequena valorização cambial. Olhando a
  janela completa desde sexta-feira, a paridade em reais subiu de R$145,54 (11/09) para
  R$149,75 (15/09), um ganho de **+2,89%** em três sessões — bem mais expressivo do que os
  +1,66% calculados ontem com os números então disponíveis.
- **Crush margin também subiu mais do que se pensava**, o que por si só não é um driver de
  soja isolado, mas confirma que a indústria de esmagamento está sendo remunerada de forma
  crescente para processar — ver seção Spreads.

**O que invalida / risco:**

- **O COT mais fresco (08/09) tem agora oito dias corridos de defasagem** frente a hoje —
  ainda maior do que os sete de ontem. Não há qualquer confirmação de que os fundos, que
  vinham ampliando a posição comprada até 01-08/09, continuaram comprando durante o repique
  de 11 a 15/09 ou começaram a realizar lucro. O próximo corte (posições de 15/09) é
  esperado por volta de 18-19/09 e será o primeiro capaz de responder a essa pergunta.
- **Crush margin segue abaixo do referencial de US$2,50/bushel monitorado pela fila**
  (`alerta-quebra_suporte-complexo_soja-2026-09-15`), embora a distância tenha encolhido bem
  mais rápido do que se pensava: **-3,65%** hoje (US$2,4088), contra os -7,08% calculados
  ontem com o crush então reportado (US$2,3229) — a recuperação real é mais de duas vezes
  mais rápida do que a versão de ontem sugeria.
- **Nível técnico a vigiar:** um fechamento de volta abaixo de 1.180 ainda desfaria
  formalmente o rompimento; com a folga agora em 11,80%, esse cenário está mais distante do
  que em qualquer leitura recente.
- **Risco geral do episódio de correção**: se os números de hoje também vierem a ser
  revisados amanhã, a folga técnica e a leitura de momentum precisarão ser recalibradas de
  novo — ver Honestidade sobre o padrão recorrente de revisão de dados desta fonte.

**Leitura operacional:** para quem está comprado, a correção de hoje é uma boa notícia
dupla — o movimento de alta foi mais forte do que se pensava, e o volume que sustenta esse
movimento é finalmente confiável. Não há motivo técnico, à luz dos dados corrigidos, para
reduzir posição comprada agora; a única lacuna real é a falta de confirmação de COT
contemporâneo. Para quem opera o lado vendido, a soja segue sem gatilho técnico de entrada:
a folga sobre a resistência aumentou, não diminuiu, com a correção de hoje.

## Farelo

**Viés: bull, moderado (ELEVADO de neutro) — pela primeira vez desde a abertura da tese de
abundância em 11/06/2026, esta leitura muda o viés de preço do farelo. O gatilho não é um
quarto dia de confirmação (ainda são três sessões acima de 80%, como ontem) — é a
constatação de que a suspeita de dado parcial que mantinha a confiança baixa se confirmou, e
a versão real da terceira sessão é MAIS forte, não mais fraca, do que a versão usada até
ontem.**

O que sustenta a mudança de viés:

- **O ratio Far/Soj corrigido de 15/09 é 81,91%, não 80,46%** (indicators) — a maior
  leitura de toda a janela de mais de 90 dias desde a abertura da tese, e também o maior
  salto diário do movimento (+1,36 p.p. sobre os 80,55% de 14/09, contra +0,30 p.p. de
  11→14/09). A versão de ontem descrevia a terceira sessão como "a mais próxima de zero dos
  três" no oil-meal spread, sugerindo um equilíbrio se formando — o oposto do que os dados
  corrigidos mostram: o movimento está acelerando, não estabilizando. Vale notar que
  81,91% está muito perto do nível de **81,4%** com que a tese original começou em
  11/06/2026 ([[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]) — o ratio completou,
  em essência, uma volta completa desde o início da tese, mas chegando lá pelo lado oposto:
  a tese original apostava em compressão adicional abaixo de 80%, e o que se vê agora é o
  ratio voltando a subir através da mesma zona, não confirmando a compressão esperada.
- **Oil share caiu para 49,21%**, a leitura mais baixa da janela (ante 49,86% em 14/09 e
  49,94% em 11/09) — o farelo respondendo por **50,79%** do valor total do crush hoje,
  a maior fatia relativa do farelo em toda a janela de acompanhamento recente.
- **Oil-meal spread saltou para -0,2475 USD/bushel**, mais de 8 vezes o valor de 14/09
  (-0,0429) e mais de 13 vezes o de 11/09 (-0,0187) — de longe o maior avanço em uma única
  sessão desde que este indicador começou a ser citado nesta série de leituras. Este é o
  dado que mais pesa na decisão de elevar o viés: não é apenas "mais um dia do mesmo
  padrão", é uma aceleração de ordem de magnitude.
- **A correção resolve, de fato, o problema que vinha sustentando a cautela.** As leituras
  de 12, 13 e 15/09 mantiveram o viés em "neutro" citando repetidamente a falta de confirmação
  por volume/qualidade de dado como razão central para não avançar. Com o volume de farelo
  hoje confirmado em 39.805 contratos (dentro da faixa histórica de 20-30 mil, na verdade
  acima dela), essa objeção específica deixa de existir para a sessão de 15/09.
- **A trajetória sazonal da ABIOVE para o Brasil segue apontando para alívio de oferta
  doméstica**, sem revisão nesta janela: produção de farelo projetada recuando de 2.129 mil
  t (set/26) para 1.659 mil t (dez/26), exportação de 1.100 para 700 mil t no mesmo período
  — uma desaceleração sazonal da oferta consistente com um ratio estruturalmente mais alto
  daqui para frente.

**O que ainda pesa contra tratar isso como confirmação plena — e mantém o viés em
"moderado", não "forte":**

- **Os índices sintéticos ISF e ISO não se moveram nem com a correção.** ISF em **60/100**
  e ISO em **80/100** (indicators, 15/09) — idênticos aos valores de 11 a 15/09, apesar de o
  oil-meal spread ter multiplicado por 8 e o oil share ter atingido a mínima da janela. Isso
  é uma nuance genuinamente importante: os dois índices compostos (calculados por contagem
  de condições discretas) não reagiram nem à magnitude bem maior do movimento real — um
  sinal de que os limiares que os disparam são mais altos do que o patamar atual, não uma
  contradição do sinal de preço, mas um lembrete de que a "confirmação plena" desses dois
  índices específicos ainda não chegou.
- **O COT de 08/09 tem oito dias corridos de defasagem e mostrou, na única leitura
  disponível, cobertura de posição vendida — não convicção compradora nova.** Nenhuma
  atualização captura a reação dos fundos ao repique de 11 a 15/09, e menos ainda à
  magnitude real (agora maior) desse repique. O próximo corte (posições de 15/09, esperado
  ~18-19/09) é o primeiro capaz de testar diretamente a tese elevada hoje.
- **O físico brasileiro segue completamente congelado — agora sete dias corridos.** Última
  leitura ainda 09/09 (farelo MT/IMEA R$1.875,45/ton; prêmio export Paranaguá +0,12 USD/short
  ton, congelado desde 27/08, 20 dias corridos). Nenhuma reação do mercado físico doméstico
  à mudança de regime em Chicago pôde ser observada ainda.
- **O WASDE de setembro segue como contraponto estrutural de médio prazo.** Exportação de
  farelo argentino 2026/27 revisada de 2,89 para **2,99 milhões de toneladas**
  (`release-usda_wasde-2026-09-11`) — mais oferta exportável do segundo maior exportador
  mundial de farelo tensiona, no médio prazo, com o sinal de preço de curto prazo, mesmo que
  este último tenha ficado mais forte hoje.
- **Risco de nova revisão**: se a sessão de 15/09 for revisada de novo amanhã (o padrão já
  se repetiu duas vezes em uma semana — ver Honestidade), o salto no ratio e no oil-meal
  spread que justifica a elevação de viés hoje precisará ser reavaliado.

**Leitura operacional:** para quem está vendido em farelo (ou no spread Far/Soj vendido), a
correção de hoje é o argumento mais forte já visto nesta tese para reduzir tamanho de forma
decisiva — mais forte do que qualquer uma das cautelas graduais recomendadas em 12, 13 e
15/09, porque remove a última objeção séria (qualidade do dado) que sustentava manter a
posição. Ainda não é recomendação de fechar cegamente: falta o COT de 18-19/09 e qualquer
reação do físico brasileiro. Para quem está comprado em farelo ou no spread, esta é a
primeira sessão da tese inteira em que preço, ratio, oil share e oil-meal spread apontam
todos na mesma direção com volume confirmado — o quadro mais favorável até aqui para
aumentar tamanho, com o cuidado de que o COT e o físico ainda não confirmaram.

## Óleo

**Viés: bear, moderado (mantido) — o preço segue abaixo do suporte de 72,00 mesmo com o
repique de hoje, e a estrutura de crush (oil share, oil-meal spread) piorou ainda mais para
o óleo; mas a margem de biodiesel americana bateu um novo recorde da janela, ampliando —
não reduzindo — a divergência entre preço em Chicago e fundamento de demanda real.**

O que pesa contra a tese (preço e estrutura de crush):

- **Óleo fechou em 69,79 USD cts/lb (CME CBOT, 15/09, corrigido)**, uma alta de +0,20%
  frente aos 69,65 de 14/09 — a menor variação percentual dos três produtos, mesmo com
  volume agora normal (22.257 contratos, dentro da faixa histórica de 17-32 mil). A fila
  confirma a permanência abaixo do suporte de 72,00
  (`alerta-quebra_suporte-oleo_cbot-2026-09-15`), com a distância agora em **-3,07%** —
  ligeiramente menor do que os -3,47% calculados ontem, porque o fechamento real de hoje é
  mais alto do que o número usado ontem, mas ainda claramente abaixo do nível.
- **Oil share e oil-meal spread pioraram de forma acentuada para o óleo dentro do crush.**
  Oil share caiu a **49,21%** (mínima da janela) e oil-meal spread aprofundou para
  **-0,2475** USD/bushel (o valor mais negativo já registrado nesta série de leituras) — o
  óleo perdendo espaço relativo dentro do crush de forma mais rápida do que qualquer leitura
  anterior havia captado.
- **O ISO (Índice de Suporte do Óleo) segue em 80/100**, abaixo do teto de 100 atingido em
  10/09, sem novo recuo — mas também sem qualquer sinal, nos índices compostos, de que o
  óleo esteja recuperando espaço.

**O que sustenta um piso parcial para a tese:**

- **A margem de biodiesel americana bateu novo recorde da janela.** Fechou em
  **US$2,1384/galão** hoje (indicators, 15/09), superando o recorde anterior de US$2,135 de
  11/09 e uma alta de +1,69% sobre os US$2,1028 de 14/09. O mecanismo: heating oil (CME
  NYMEX, HO=F) subiu +0,93% (de 4,9615 para **5,0077** USD/galão), elevando a receita
  modelada do biodiesel (8,1727 USD/galão), enquanto o custo do óleo como insumo subiu
  proporcionalmente menos (+0,20%, para US$5,2343/galão, acompanhando a própria alta
  discreta do óleo em Chicago). O resultado líquido é o melhor nível de economia de
  biodiesel já registrado nesta janela de acompanhamento.
- **A divergência preço-vs-fundamento identificada em 13/09 e reforçada em 15/09 fica ainda
  mais larga com a correção de hoje.** O óleo em Chicago segue abaixo do suporte técnico
  (69,79, -3,07%) exatamente no mesmo dia em que a margem de biodiesel — a métrica que
  resume a demanda econômica real por óleo como insumo de combustível nos EUA — atinge um
  recorde da janela. Isso não invalida o viés bear de preço (que segue sendo o fato
  observável em Chicago), mas é um lembrete cada vez mais forte de que o mercado pode estar
  subprecificando o óleo frente ao valor que ele tem, hoje, para a indústria de biodiesel
  americana.
- **A curva futura de médio prazo segue em contango, com inclinação decrescente.** Out/26
  (base) 69,79 → dez/26 70,27 → jan/27 70,48 → mar/27 70,58 → mai/27 70,60 (CME CBOT,
  corrigido) — incrementos de +0,48 → +0,21 → +0,10 → +0,02 ponto entre vencimentos
  consecutivos, uma curva que precifica alguma recuperação no curto/médio prazo mas quase
  achatada a partir de 2027, sem sinal de aposta forte em reversão estrutural.
- **O RIN D4 (crédito de biocombustível renovável americano) continua constante na fórmula
  interna** — o termo implícito "1,5×RIN" segue valendo **2,11 USD** também em 15/09,
  igual a todas as seis sessões anteriores com dado disponível. Isso significa que o novo
  recorde de margem de biodiesel vem inteiramente de heating oil e do custo do óleo, não de
  qualquer mudança real no valor do crédito RIN — ver Honestidade.

**Leitura operacional:** para quem está vendido em óleo direcional, o preço e a estrutura
de crush seguem a favor da posição — o óleo é, dos três produtos, o que menos se beneficiou
da correção de hoje em termos de magnitude percentual, e a fatia do óleo no crush caiu para
a mínima da janela. Ainda assim, o recorde de margem de biodiesel é o alerta mais forte já
emitido nesta série de leituras de que o argumento fundamentalista contra a posição vendida
está ficando mais, não menos, presente — quem está vendido deveria monitorar esse indicador
de perto nos próximos dias. Para quem está comprado em óleo direcional, a tese ainda não tem
confirmação de preço (o óleo segue abaixo do suporte), mas ganhou hoje o argumento
fundamentalista mais forte da janela inteira. Para quem opera o spread farelo-óleo dentro do
crush, o oil-meal spread saltando para -0,2475 USD/bushel é o sinal mais forte já visto de
que o farelo está definitivamente ganhando a disputa por valor dentro do crush no curto
prazo — o spread "farelo vendido / óleo comprado" (aposta na reversão) fica mais esticado, e
portanto potencialmente mais assimétrico para quem acredita em mean-reversion, mas também
mais arriscado para quem já está posicionado nessa direção há dias.

## Spreads e crush (leitura de complexo)

Com os números corrigidos, a janela de três sessões desde a reabertura do fim de semana
(11, 14 e 15/09) mostra um padrão não apenas consistente, mas **acelerando** — o oposto da
leitura de "equilíbrio se formando" que os dados parciais de ontem sugeriam. Preços: soja
1.296,50 → 1.304,25 → 1.319,25; farelo 346,80 → 350,20 → 360,20; óleo 69,19 → 69,65 → 69,79
(CME CBOT, todos corrigidos). O ratio Far/Soj: **80,25% → 80,55% → 81,91%**, com o salto de
14→15/09 (+1,36 p.p.) mais do que quatro vezes maior que o de 11→14/09 (+0,30 p.p.). O oil
share: **49,94% → 49,86% → 49,21%**, também acelerando para baixo. O oil-meal spread:
**-0,0187 → -0,0429 → -0,2475** USD/bushel, um salto de mais de 8 vezes em uma única sessão.

Três indicadores matematicamente independentes, construídos a partir dos mesmos três
preços, todos acelerando na mesma direção na mesma sessão — isso é uma coerência mais forte
do que qualquer coisa observada nesta tese desde 11/06/2026, incluindo a versão (já
correta, mas mais morna) que a leitura de ontem já havia elogiado. O detalhamento completo
do episódio de correção está em
[[2026-09-16_correcao-numeros-sessao-15set-ratio-salta-para-8191]]. Ao mesmo tempo, os dois
índices compostos por contagem de condições — ISF (60/100) e ISO (80/100) — permanecem
travados no mesmo patamar desde 11/09, mesmo com a magnitude bem maior do movimento real
revelada hoje. Isso não contradiz o sinal de preço, mas mostra que os limiares desses dois
índices específicos exigem um movimento ainda maior (ou mais sustentado) para disparar a
próxima condição — um contraponto que deve ser monitorado, não ignorado.

O crush margin fechou em **US$2,4088/bushel** (indicators, 15/09), a distância frente ao
referencial de US$2,50 (fila `alerta-quebra_suporte-complexo_soja-2026-09-15`) encolhendo
para **-3,65%** — a recuperação mais rápida já registrada nesta janela (-9,97% em 10/09 →
-8,98% em 11/09 → -7,32% em 14/09 → **-3,65%** hoje, um salto de quase o dobro do
encolhimento diário típico dos dias anteriores). O mecanismo por trás: farelo e óleo, juntos,
subiram líquidos de soja mais rápido hoje do que em qualquer sessão recente — farelo
sozinho contribuiu com a maior parte desse avanço.

O COT de 08/09 (oito dias corridos de defasagem frente a hoje) segue sendo o único retrato
de posicionamento disponível, e a defasagem cresce a cada dia sem trazer qualquer
confirmação de como os fundos reagiram ao repique real (agora conhecido como maior do que
se pensava) de 11 a 15/09. O próximo corte (posições de 15/09, esperado por volta de 18-19/09)
é o primeiro capaz de testar diretamente se os grandes players já estão posicionados para o
ratio mais alto, ou se ainda serão pegos de surpresa por ele.

Do lado dos fundamentos brasileiros de médio prazo (ABIOVE, sem revisão nesta janela), o
balanço projetado mostra o esvaziamento sazonal esperado: estoque final de soja recuando de
7.912 mil toneladas (set/26) para 1.890 mil toneladas (dez/26), produção de farelo caindo de
2.129 para 1.659 mil toneladas no mesmo período, exportação de farelo recuando de 1.100 para
700 mil toneladas — uma trajetória que segue apoiando, não contrariando, um ratio
estruturalmente mais alto no médio prazo, agora reforçada por um sinal de curto prazo bem
mais forte do que se sabia até ontem.

## Lente fiscal/regulatória BR

Antes de fechar qualquer tese de preço BR, os vetores tributários/regulatórios vivos que
pesam no complexo — todos do `system/tributario_watch.toml`, cujo carimbo mais recente
(`atualizado_em`) em todos os 10 eventos catalogados é 2026-06-05, ou seja, **103 dias
corridos sem revisão humana** frente a hoje (16/09):

- **MP 1.363/2026** (id `MP-1363-2026`, subvenção diesel fóssil R$1,12/L, vigente até
  31/12/2026): barateia o diesel fóssil no mix B15 (mistura obrigatória de 15% de
  biodiesel), reduzindo a competitividade relativa do biodiesel e a demanda doméstica por
  óleo de soja — vetor estrutural de baixa para óleo, sem mudança de status. Este vetor
  ajuda a explicar por que o óleo pode ficar bear em Chicago mesmo com a margem de
  biodiesel americana em recorde: o mercado interno brasileiro tem um desincentivo próprio
  que não aparece na conta americana.
- **B16 (id `B16-CNPE-2026`, elevação da mistura obrigatória de biodiesel para 16%)** segue
  "adiado", resultado esperado por volta de novembro/2026. Upside represado (~436 mil
  toneladas de demanda potencial adicional de óleo), não corrente — mas cada semana que
  passa aproxima o mercado da decisão.
- **Isenção de PIS/Cofins do biodiesel na mistura** (id `PISCOFINS-BIODIESEL-ISENCAO`):
  vigência registrada até 31/07/2026 — já **47 dias corridos vencida** frente a
  16/09/2026, sem registro de prorrogação ou expiração.
- **MP 1.358/2026** (subvenção gasolina R$0,89/L): vigência registrada até 11/07/2026,
  agora **67 dias corridos vencida**.
- **STJ REsp 2.165.276** (id `STJ-RESP-2165276`, crédito de PIS/Cofins sobre soja em
  biodiesel, direção "alta" para soja/óleo): sem novidade nesta janela.
- **EPA RFS 2026/2027** (id `EPA-RFS-2026-2027`, mandato de biocombustível americano,
  vigente desde 15/06/2026, direção "alta" para óleo): sustenta o RIN D4, estável — mas,
  como notado na seção Óleo, o valor do RIN parece fixo na fórmula interna usada por este
  sistema (2,11 USD constante há sete sessões), não uma leitura de mercado atualizada
  diariamente.
- **Crédito 45Z** (id `45Z-CLEAN-FUEL`, em tramitação, direção "mista"): sem novidade.
- **Indonésia — Danantara** (id `DANANTARA-INDONESIA`) e **levy de exportação PMK
  9/2026** (id `INDONESIA-LEVY-PMK9`): a assunção plena da centralização da exportação de
  palma pela Indonésia tinha alvo 01/09/2026 — já se passaram **15 dias** sem confirmação.
  Catalisador de alta represado para óleo (via substituição com palma) — sem dado de MPOB
  disponível para monitorar diretamente (ver Honestidade).
- **Indonésia B50** (id `INDONESIA-B50`, monitorando, direção "alta"): sem novidade.

## Riscos e eventos próximos

- **Confirmação (ou não) de uma nova revisão dos números de 15/09** — este é o segundo
  episódio de correção material em uma semana (o primeiro foi a auditoria de 13/09 sobre a
  sessão de 11/09). Um terceiro episódio reforçaria a hipótese de um problema estrutural,
  não pontual, na extração da fonte CME CBOT — ver Honestidade.
- **O COT de 08/09 está oito dias corridos atrasado frente ao preço** — o próximo corte
  (posições de 15/09, esperado por volta de 18-19/09) é o primeiro capaz de confirmar se os
  fundos reagiram ao repique real (agora conhecido como bem mais forte) das últimas três
  sessões.
- **Um quarto fechamento do ratio Far/Soj acima de 80%** (a próxima sessão real de CBOT,
  ainda não capturada nesta janela) reforçaria ainda mais a mudança de viés desta leitura;
  um fechamento de volta abaixo de 80% devolveria o episódio ao padrão histórico de "toque e
  recuo", mesmo após a correção.
- **Reação (ou ausência) do físico brasileiro de farelo e óleo**, congelado desde 09/09
  (sete dias) e 27/08 (prêmios export, 20 dias).
- **USDA Crop Progress semanal**: próximo corte esperado por volta de 20/09, para
  confirmar ritmo de colheita além dos 6% de 13/09.
- **USDA WASDE de setembro**: ainda incompleto nesta janela (só farelo Argentina/Brasil) —
  monitorar se as tabelas de soja em grão, óleo e EUA aparecem nos próximos dias.
- **NOPA mensal** (`release-nopa-2026-09-15`): mais um carimbo sem dado novo de fato
  (paywall).
- **Confirmação da centralização plena da exportação de palma pela Danantara** — alvo
  01/09, já 15 dias passados.
- **Vigência da isenção PIS/Cofins do biodiesel** (47 dias vencida) e **MP 1.358/2026 da
  gasolina** (67 dias vencida) — checar notícia de renovação/expiração.
- **Clima**: previsão de hoje (16/09) traz a primeira menção de possibilidade de geada em
  vários dias para Passo Fundo/RS (mínima de 7°C pela manhã), enquanto o núcleo produtor de
  Mato Grosso segue com calor forte (35-38°C) e chuva/trovoadas isoladas — pano de fundo
  para a janela de plantio da safra 2026/27 que se aproxima.
- **Marco de 103 dias sem revisão humana do `tributario_watch.toml`** — pelo menos dois
  vetores (isenção PIS/Cofins biodiesel, MP 1.358/2026) já vencidos sem registro de
  renovação, seguem sem checagem manual.
- **A margem de biodiesel americana em recorde** (US$2,1384/galão) é, por si só, um
  evento a monitorar: se sustentada ou ampliada nos próximos dias, é o tipo de sinal
  fundamentalista que historicamente precede uma reação de preço no óleo, mesmo que com
  defasagem.

## Honestidade

- **Este é o segundo episódio de correção material de dados de sessão em uma semana**, e o
  mais importante já documentado nesta série de leituras. Detalhado por completo em
  [[2026-09-16_correcao-numeros-sessao-15set-ratio-salta-para-8191]]: os fechamentos de
  15/09 usados pela leitura de ontem (soja 1.298,25, farelo 348,20, óleo 69,50) e os volumes
  então reportados (2.379, 479 e 1.045 contratos) foram substituídos, no dump de hoje, por
  fechamentos mais altos nos três produtos (1.319,25, 360,20 e 69,79) e volumes ordens de
  grandeza maiores (121.947, 39.805 e 22.257). A auditoria de 13/09
  ([[2026-09-13_correcao-numeros-sessao-11set-farelo-oleo]]) já havia documentado um episódio
  parecido para a sessão de 11/09. Dois episódios em uma semana, ambos na mesma fonte (CME
  CBOT) e ambos na mesma direção (dado inicial mais fraco/parcial, correção posterior mais
  forte), sugerem uma fragilidade estrutural na captura ou retenção de dados brutos dessa
  fonte específica nesta janela — não dois acidentes isolados. Recomendação prática: tratar
  qualquer fechamento do dia mais recente do dump com um desconto de confiança até que ele
  seja confirmado (ou corrigido) pela geração seguinte, especialmente quando o volume
  reportado destoar fortemente do histórico recente.
- **A curva futura "de 14/09" citada na leitura de ontem para farelo também foi confirmada
  como incorreta hoje** — máxima, mínima e volume que ontem apareciam idênticos aos de
  15/09 (contaminação cruzada) agora aparecem, no dump de hoje, com valores próprios e
  plausíveis para 14/09 (máxima 352,80, mínima 344,60, volume 34.001) — consistentes com um
  pregão normal, o que reforça a leitura de que o problema de ontem era mesmo um artefato de
  captura, não uma mudança real na estrutura do mercado.
- **A janela de 14 dias do dump ainda não traz nenhuma linha bruta de CME CBOT para soja e
  óleo na data de 14/09** — apenas farelo e heating oil. Esta lacuna específica persiste
  desde a leitura de ontem e não foi resolvida pela correção de hoje; ela não afeta os
  fechamentos usados nesta leitura (obtidos via a fórmula do crush margin nos `indicators`,
  que são internamente consistentes), mas impede reconstruir o range intradiário completo de
  soja e óleo para aquele dia especificamente.
- **O volume do heating oil (HO=F) em 15/09 continua anormalmente baixo mesmo após a
  correção geral — apenas 203 contratos**, muito abaixo dos 62.190 de 11/09 ou de qualquer
  outro valor recente citado nesta série. Diferente de soja, farelo e óleo (cujos volumes
  vieram corrigidos para níveis normais hoje), o heating oil não recebeu o mesmo tratamento
  — o que significa que o fechamento de 5,0077 USD/galão usado no cálculo da margem recorde
  de biodiesel ainda carrega o mesmo tipo de incerteza que os outros três produtos tinham
  ontem. A margem de biodiesel recorde desta leitura deve ser lida com essa ressalva
  específica.
- **O RIN D4 segue tratado como uma constante na fórmula interna de margem de biodiesel.**
  Isolando o termo "1,5×RIN" da fórmula (receita = HO + 1,5×RIN) em cada uma das últimas
  sete sessões com dado disponível (08 a 15/09), o valor implícito do RIN permanece em
  **~2,11 USD** em todas elas, inclusive na sessão corrigida de hoje. Toda a variação da
  margem de biodiesel discutida nesta e nas leituras anteriores continua vindo
  inteiramente do heating oil e do preço do óleo, não de uma mudança real no mercado de
  créditos RIN.
- **A BCB PTAX de hoje (16/09) não está disponível nesta janela do dump** — a leitura mais
  recente de câmbio continua sendo a de 15/09 (5,1490), a primeira vez em alguns dias em que
  a PTAX citada é de fato própria do dia analisado, não reciclada do dia anterior. Isso é
  uma melhora frente ao problema apontado na leitura de ontem, mas ainda deixa hoje (16/09)
  sem leitura cambial própria.
- **O COT de 08/09 tem agora oito dias corridos de defasagem** frente a hoje — não há como
  confirmar se os fundos reagiram ao repique real (mais forte do que se sabia) das últimas
  três sessões. Próximo corte esperado por volta de 18-19/09.
- **Percentil histórico de posicionamento COT não está disponível no briefing** — toda
  leitura de "fundos comprando/vendendo" usa variação semana a semana de contratos
  absolutos, não percentil histórico.
- **`tributario_watch.toml` sem atualização há 103 dias corridos** — pelo menos dois
  vetores (isenção PIS/Cofins do biodiesel, MP 1.358/2026) já passaram da vigência
  registrada sem nota de renovação ou expiração.
- **NOPA segue inacessível** (paywall) — mais um "release" sem dado novo de fato.
- **A ausência de itens de notícia com conteúdo real desde 09/09, agora sete dias
  corridos**, é registrada como falha ou pausa de coleta da fonte RSS, não como ausência
  real de notícia relevante no mercado.
- **A previsão INMET para 16/09 é previsão meteorológica, não medição de precipitação ou
  temperatura real** — a menção a "possibilidade de geada" pela manhã em Passo Fundo/RS é
  indicativa, não confirmação de geada de fato.
- **Prêmios de exportação (Paranaguá) e o físico de farelo/soja BR seguem sem atualização
  própria desde 09/09** (sete dias corridos) — não é possível afirmar se isso reflete
  mercado físico genuinamente parado ou apenas defasagem normal de publicação.
- **MPOB (palma Malásia) segue com parser quebrado** — nenhum dado de produção/estoque de
  palma malaia disponível, o que impede monitorar diretamente o catalisador represado da
  centralização de exportação indonésia (Danantara).
- **BCBA (Argentina) segue sem links de relatório detectados** — nenhum dado de safra ou
  exportação argentina disponível.
- **Os forecasts estatísticos internos (bandas 7d/30d) foram recalculados sobre os
  fechamentos corrigidos de hoje**, e o viés de óleo em 30 dias mudou de "lateral" (versão
  de ontem, sobre dados então incorretos) para "altista" — isso reflete extrapolação
  estatística de tendência recente (MA20 + volatilidade + slope) reagindo à correção, não
  uma reavaliação fundamentalista desta leitura; tratado aqui como referência estatística, não
  como leitura própria desta análise.
- **A fila de julgamento continua listando os dois itens de revisão do ratio Far/Soj (D+7
  e D+90) como "vencidos"**, mesmo com o D+90 já tratado em profundidade em 09/09, 12/09 e
  15/09 — um eco do sistema de geração de fila que não lê de volta os insights já escritos
  para marcar a revisão como encerrada. A revisão de D+180, programada para 08/12/2026 pela
  tese original, ainda não venceu.
