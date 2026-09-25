---
data: 2026-09-25
titulo: "O ratio Far/Soj fecha em 84,64% pela quarta sessão consecutiva de alta (83,22% → 83,90% → 84,36% → 84,59% → 84,64%), a menor distância já vista do teto 'apertado' de 87% (2,36 p.p.), mas farelo e heating oil voltam a mostrar exatamente o padrão de fechamento suspeito (abertura/máxima/mínima/volume idênticos ao dia anterior, só o 'último preço' mudando) já documentado três vezes nesta série — mantendo bull-farelo e bear-óleo com convicção intacta na direção, e uma reserva nova sobre a magnitude exata de hoje, enquanto a soja fica neutra e de olho numa manchete ainda não numerada de compras chinesas"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT — sessão de **2026-09-25** (a mais recente do dump de hoje): soja (ticker ZSX26.CBT, venc. nov/26) abertura 1.317,50, máxima 1.318,25, mínima 1.316,00, fechamento **1.316,75**, volume **3.441 contratos**; farelo (ticker ZMZ26.CBT, venc. dez/26) abertura 370,70, máxima 372,40, mínima 370,40, fechamento **371,50** (campo `fechamento_Z26` do mesmo ticker traz 371,80 — discrepância interna, ver Honestidade), volume **830 contratos**; óleo (ticker ZLZ26.CBT, venc. dez/26) abertura 67,55, máxima 67,66, mínima 67,39, fechamento **67,40**, volume **584 contratos**. Curva futura em 25/09 — soja: nov/26 (base) 1.316,75 → jan/27 1.330,50 → mar/27 1.338,25 → mai/27 1.345,50 → jul/27 1.351,00 (contango regular, achatando no fim: +1,04% nov→jan, +0,41% mai→jul); farelo: out/26 376,60 → dez/26 (base) 371,50/371,80 → jan/27 370,10 → mar/27 368,30 → mai/27 367,70 (backwardation, -1,02% de dez/26 a mai/27, mais acentuada que a de ontem); óleo: out/26 66,74 → dez/26 (base) 67,40 → jan/27 67,63 → mar/27 67,99 → mai/27 68,30 (contango regular, +1,34% de dez/26 a mai/27)
  - CME CBOT — sessão de **2026-09-24** (nova nesta janela, apenas farelo e heating oil capturados — soja e óleo não aparecem no recorte de 14 dias do dump de hoje): farelo abertura 370,70, máxima 372,40, mínima 370,40, fechamento **371,20**, volume **830 contratos** — abertura, máxima, mínima e volume **idênticos byte a byte** aos de 25/09, só o fechamento difere (ver Honestidade)
  - CME NYMEX heating oil (HO=F) — **2026-09-25**: abertura 4,5700, máxima 4,5850, mínima 4,5100, fechamento **4,5214** USD/galão, volume **372 contratos** — mesmíssimo padrão: abertura, máxima, mínima e volume idênticos aos de 24/09 (fechamento 4,5171), só o último preço mudou (+0,10%)
  - Indicadores sintéticos internos (`indicators`) — **2026-09-25**: crush margin **US$2,4195/bushel** (farelo 371,50 + óleo 67,40 − soja 1.316,75); ratio Far/Soj **84,64%**; oil share **47,57%**; oil-meal spread **-0,759 USD/bushel** (mínima real desta série); ISF (Índice de Sobra de Farelo) 60/100; ISO (Índice de Suporte do Óleo) 80/100; paridade BR da soja **R$150,36/saca** (CBOT 1.316,75 × USD/BRL 5,1795); margem de biodiesel US **US$1,8314/galão** (receita 7,6864 = HO 4,52 + 1,5×RIN 2,11; custo 5,86 = óleo 5,055 + industrial 0,80), alta de +0,53% frente aos 1,8218 de ontem — primeiro repique em três sessões, mas construído sobre o mesmo HO=F de captura suspeita (ver Óleo e Honestidade). Série do ratio Far/Soj nos últimos cinco carimbos: 21/09 83,22% → 22/09 83,90% → 23/09 84,36% → 24/09 84,59% → 25/09 **84,64%** — quarta alta consecutiva real; oil share na mesma janela: 48,31% → 47,81% → 47,78% → 47,61% → **47,57%**, mínima monotônica
  - BCB PTAX — **2026-09-24** (defasagem normal de 1 dia): USD/BRL **5,1795** (+0,74% frente aos 5,1414 de 23/09, segunda alta seguida do dólar), EUR/BRL 5,8906, Selic diária 0,050788% a.a. (séries SGS 1, 21619, 11) — o real voltou a enfraquecer, compensando parte da estabilidade do CBOT sobre a paridade em reais
  - CEPEA/ESALQ Soja Paranaguá (via NAG) — **2026-09-24**: R$161,84/saca (+0,12% frente a 23/09); spread Paranaguá−Paraná interior de R$6,73/saca (161,84 − 155,11), levemente mais largo que os R$6,58 de ontem
  - NAG físico BR (`nag_fisico`) — **2026-09-24**: farelo Mato Grosso/IMEA **R$1.982,28/ton, var 0,0% — QUINTA leitura seguida sem mudança (18, 21, 22, 23 e 24/09)**, cruzando o limiar que a leitura de ontem havia definido como gatilho de suspeita de estagnação de fonte (ver Honestidade); farelo Rondonópolis/MT (BCSP) **R$2.200,00/ton, var 0,0% — quarta leitura seguida** (21, 22, 23 e 24/09), a confirmação física mais consolidada desta série; farelo média Rio Grande do Sul (Clicmercado) **R$2.130,00/ton, var 0,0% — SEGUNDA leitura seguida no novo patamar**, a primeira confirmação real de que o salto de +14,52% de ontem não foi um evento isolado; soja Paraná interior (CEPEA/ESALQ via NAG) R$155,11/saca (+0,03% frente a 23/09); prêmio export farelo Paranaguá 0,12 USD/short_ton (congelado há **17 dias corridos**, desde 08/09); prêmio export óleo Paranaguá 0,1 cts/lb (mesmo congelamento, 17 dias)
  - CEPEA RSS — contagem de itens recua para 106 em 25/09 (de 109 em 24/09), sem novo corpo de headline capturado; a última manchete com corpo de texto ainda é a de 18/09 ("Participação do farelo na 'crush margin' aumenta no BR e nos EUA")
  - Notícias Agrícolas/Canal Rural/Farm Progress (RSS) — item mais recente ainda é o de **2026-09-24** (Farm Progress): "USDA Exports: China buys soybeans" (https://www.farmprogress.com/marketing/flash-sales) — headline nova, potencialmente o dado mais relevante para a tese de soja desta semana, mas sem tonelagem, contraparte nem corpo de texto disponíveis neste dump (ver Soja e Honestidade); contagem de 25/09 registra 160 itens lidos e apenas 3 mantidos
  - CFTC COT Managed Money — corte de **2026-09-15, agora 10 dias corridos de idade** (sem corte novo; o corte de posições de 22/09, que as leituras de ontem e anteontem projetavam para 25-26/09, ainda NÃO apareceu neste dump apesar de hoje já ser 25/09): farelo net long 183.111 contratos (+16,12% vs 08/09); óleo net long 101.480 (+10,65%); soja net long 241.501 (-6,13%)
  - USDA Crop Progress — corte de **2026-09-20** (agora 5 dias de idade): 12% excelente / 46% boa (G/E 58%), 10% pobre, colheita 2025/26 em **12% concluída**; próximo corte esperado por volta de 27-28/09
  - USDA WASDE — edição de **2026-09-11** (agora 14 dias de idade, sem edição nova): farelo Argentina 2026/27 exportação 2,99 mi t; farelo Brasil 2025/26 exportação 0,2 mi t
  - NOPA — item de fila `release-nopa-2026-09-25`: `monthly_status` em 0,0 bool (paywall, sem dado novo, mesmo padrão de todas as leituras anteriores desde o início deste monitoramento)
  - ABIOVE projeções mensais — balanços out-dez/2026, sem revisão nesta janela: produção de farelo BR caindo 2.142,97 (out) → 1.977,59 (nov) → 1.659,04 (dez) mil t; exportação de farelo BR caindo 850 → 800 → 700 mil t no mesmo período; estoque final de soja BR caindo 5.720,77 (out) → 3.658,99 (nov) → 1.889,91 (dez) mil t
  - NOAA CPC ENSO — El Niño Advisory, inalterado (carimbo 2026-09-25)
  - MPOB — carimbo 2026-09-25, parser sem números extraídos (mesma barreira há semanas)
  - INMET — previsão para **2026-09-25 (HOJE)**: núcleo de Mato Grosso sob calor mais intenso que ontem — Lucas do Rio Verde 41°C/24°C, Sinop 40°C/24°C, Sorriso 39°C/25°C, Cuiabá 36°C/25°C, todos com "possibilidade de chuva isolada"; Rio Verde/GO 34°C/21°C, mesma condição; Paraná (Cascavel 29°C/15°C, Maringá 29°C/17°C) e Passo Fundo/RS (27°C/13°C) sem menção de geada hoje, ao contrário de ontem
  - system/tributario_watch.toml (lido como referência, não editado) — `atualizado_em` 2026-06-05 em todos os 10 eventos catalogados, **112 dias corridos** sem revisão humana frente a hoje (25/09)
  - Forecasts estatísticos internos (bandas 7d/30d) — geração de **2026-09-25**, sobre o fechamento de 25/09, alvos 02/10 e 25/10: viés "altista" em farelo nos dois horizontes e em soja no horizonte de 30d (7d virou "lateral"); óleo em "baixista" nos dois horizontes — extrapolação estatística, não fundamentalista (ver Honestidade)
  - Fila de julgamento — 2026-09-25, 7 itens: `alerta-quebra_resistencia-soja_cbot-2026-09-25`, `alerta-quebra_suporte-oleo_cbot-2026-09-25`, `alerta-quebra_resistencia-farelo_cbot-2026-09-25`, `alerta-quebra_suporte-complexo_soja-2026-09-25`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`, `release-nopa-2026-09-25`
  - Cruza com [[2026-09-24_leitura-complexo]] (leitura de ontem, base de comparação para toda a série), [[2026-09-24_correcao-numeros-sessao-23set-fim-do-artefato-de-baixa-liquidez]] (auditoria da última correção confirmada), [[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]] (documentação do padrão de captura suspeita que reaparece hoje) e [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (tese original do ratio, já invalidada tecnicamente desde [[2026-09-17_ratio-far-soj-supera-nivel-de-abertura-da-tese-original-quarta-sessao]])
status: ativa
vies: [bull-farelo, neutral-soja, bear-oleo_soja]
---

## Visão geral

O complexo soja gira em torno do "crush" — o esmagamento industrial que separa a soja em
grão em dois produtos com destinos econômicos diferentes: farelo (o resíduo proteico,
usado quase todo em ração animal, sobretudo aves e suínos) e óleo (usado em alimentação
humana e, cada vez mais, em biodiesel). Quem manda no crush, em cada momento, é definido
pelo "oil share" — a fatia do valor total gerado pelo esmagamento que vem do óleo. Quando
o oil share é alto, a indústria esmaga soja principalmente atrás do valor do óleo, e o
farelo sai como subproduto que precisa ser escoado a qualquer preço — pressionando seu
preço relativo para baixo. Quando o oil share cai, é o contrário: o farelo passa a pagar
a conta do esmagamento, e o óleo perde protagonismo relativo. O termômetro mais direto
dessa disputa é o ratio Far/Soj — o preço do farelo dividido pelo preço da soja, em
percentual: abaixo de 80% o farelo está "abundante" (baixista); entre 80% e 87% ele está
na zona "neutra"; acima de 87% ele fica "apertado" (altista, o farelo vira o motor de
rentabilidade do esmagador, porque sobra menos farelo do que o mercado de ração precisa).

Hoje, **25/09**, o ratio Far/Soj fechou em **84,64%** (indicators), a quarta alta
consecutiva real desta janela — 83,22% (21/09) → 83,90% (22/09) → 84,36% (23/09) → 84,59%
(24/09) → 84,64% hoje — e a menor distância já registrada nesta série até o teto
"apertado" de 87%: apenas **2,36 pontos percentuais**. O oil share, em espelho direto
dessa mesma disputa, caiu para **47,57%**, uma nova mínima monotônica (48,31% → 47,81% →
47,78% → 47,61% → 47,57% na mesma janela de cinco sessões) — o óleo respondendo por menos
da metade do valor gerado no esmagamento pela quinta sessão seguida. **O que sustenta
essa perna do complexo é a soja praticamente estável** (1.318,00 em 23/09 → 1.316,50 em
24/09 → 1.316,75 hoje, uma oscilação de apenas 0,11% em três sessões) **enquanto o farelo
continua a se valorizar mais rápido, relativamente, do que a soja** — a mesma distinção
operacional destacada ontem: isto é uma tese de força relativa do farelo dentro do crush,
não (ainda) de força absoluta isolada do produto.

**O que muda hoje não é a direção do complexo, e sim um alerta de qualidade de dado que
pede cautela específica sobre a magnitude exata dos números de hoje.** Ao cruzar as
linhas brutas de farelo e do heating oil (HO=F, usado na fórmula de margem de biodiesel)
para a sessão de 25/09 contra as de 24/09, a abertura, a máxima, a mínima e o volume são
**idênticos, casa decimal por casa decimal**, entre os dois dias — só o "fechamento"
muda (farelo: 371,20 → 371,50; HO=F: 4,5171 → 4,5214). Esse é exatamente o padrão já
documentado três vezes nesta série (11/09, 15/09/16/09, 17/09 — consolidado em
[[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]]) e reencontrado agora pela
quarta vez, na sessão mais recente ([[2026-09-24_correcao-numeros-sessao-23set-fim-do-artefato-de-baixa-liquidez]]
documentou o episódio anterior, na sessão de 23/09). O volume de hoje em farelo (830
contratos) e em óleo (584 contratos) e soja (3.441 contratos) está entre **30 e 150 vezes
menor** do que o volume confirmado saudável da última sessão plenamente corrigida (23/09:
89.807 farelo, 89.625 óleo, 117.139 soja) — um sinal forte de que os dados de hoje ainda
refletem uma captura parcial/antecipada, não o fechamento consolidado, e que uma correção
para cima ou para baixo é provável na próxima geração do dump.

**Isso não invalida a tese — separa duas perguntas diferentes.** A pergunta "a tendência
é real?" tem múltiplas confirmações independentes do print de hoje: a série do ratio
Far/Soj é uma trajetória suave de quatro sessões (não depende de um único fechamento
isolado); a confirmação física tripla no Brasil (Rondonópolis, IMEA, RS) vem do mercado
físico, não de Chicago; e a última sessão plenamente corrigida (23/09) já confirmava a
mesma direção com volume saudável. A pergunta "o número exato de hoje é confiável?" tem
resposta diferente: não, com a mesma reserva metodológica que esta série já aplicou três
vezes antes ao heating oil e agora se estende, pela primeira vez, ao próprio farelo (e,
por extensão, ao ratio Far/Soj calculado sobre ele). **Leitura de uma linha**: o pivô do
complexo continua sendo o ratio Far/Soj, a 2,36 pontos percentuais do teto "apertado" —
maior convicção em bull-farelo, sustentada por evidência multi-fonte que não depende do
print de hoje; segunda maior convicção em bear-óleo, reforçada pelo oil share em mínima e
pela lente fiscal BR, mas com o mesmo grau de reserva sobre a magnitude exata da margem
de biodiesel de hoje; soja em neutro, essencialmente lateral há três sessões, com uma
manchete nova de compras chinesas ainda sem número para confirmar. Trata as quatro
quebras técnicas da fila (`alerta-quebra_resistencia-soja_cbot-2026-09-25`,
`alerta-quebra_suporte-oleo_cbot-2026-09-25`, `alerta-quebra_resistencia-farelo_cbot-2026-09-25`,
`alerta-quebra_suporte-complexo_soja-2026-09-25`) nas seções abaixo, e as duas revisões
"vencidas" da tese de junho (`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
e `-D+90`) na seção Farelo — ambas já fechadas desde 17/09.

## Soja

**Viés: neutro, mantido — três sessões essencialmente laterais (1.318,00 → 1.316,50 →
1.316,75, variação total de apenas 0,11%) sobre volume hoje anormalmente baixo (3.441
contratos, sem termo de comparação direto no dump para 24/09), com uma manchete nova e
potencialmente relevante ainda sem número que a confirme.**

O que sustenta a tese (lado altista):

- **A soja segue folgadamente acima da resistência de referência de 1.180,00** (fila
  `alerta-quebra_resistencia-soja_cbot-2026-09-25`: fechamento 1.316,75 vs. nível
  1.180,00), uma folga de **+11,59%** — essencialmente estável frente aos +11,65% de
  ontem, sem qualquer sinal de risco de reversão técnica no curto prazo.
- **Manchete nova de Farm Progress (24/09, via `noticias_rss`): "USDA Exports: China buys
  soybeans"** — potencialmente o dado mais relevante para a tese altista de soja desta
  semana inteira, porque toca diretamente no maior driver estrutural de demanda que falta
  para validar preços mais altos (a China é o maior comprador mundial de soja, e o
  mercado americano vem monitorando com atenção qualquer sinal de retomada de compras
  depois de um ciclo de tensão comercial). O problema é que este dump não traz tonelagem,
  contraparte comercial nem corpo de texto — é impossível, a partir daqui, dizer se é um
  lote residual ou uma retomada de peso (ver Honestidade). Ainda assim, a coincidência
  temporal com a manchete de 22/09 da mesma fonte ("Shrinking supplies keep prospects for
  $14 soybeans on table") começa a formar um padrão qualitativo de duas notícias
  americanas seguidas apontando para o mesmo lado altista, mesmo sem números.
- **A curva futura permanece em contango regular**: nov/26 (base) 1.316,75 → jan/27
  1.330,50 → mar/27 1.338,25 → mai/27 1.345,50 → jul/27 1.351,00 (CME CBOT, 25/09) — o
  mercado a termo segue precificando preços mais altos à frente, com a inclinação
  achatando nos meses mais distantes (+1,04% nov→jan, +0,41% mai→jul), o mesmo padrão de
  contango "normal" de ontem.
- **A curva de crop progress (corte de 20/09, agora 5 dias de idade) segue mostrando
  condição estável em G/E 58%** — a safra americana não deteriorou na reta final do
  ciclo, com a colheita avançando (12% concluída em 20/09).

**O que invalida / risco:**

- **A soja está de fato lateral, não subindo** — três fechamentos seguidos dentro de uma
  banda de 1,50 ponto (1.318,00 → 1.316,50 → 1.316,75), a menor amplitude de variação
  registrada nesta série em três sessões consecutivas. Se a manchete de compras chinesas
  fosse um evento de peso comparável ao que moveu o mercado em ocasiões anteriores, seria
  razoável esperar alguma reação de preço mais visível — sua ausência é, por si, uma
  informação (ou o lote é pequeno, ou o mercado já havia precificado a expectativa).
- **O COT de 15/09, ainda o mais recente, mostrou os fundos reduzindo net long em soja em
  -6,13%** (de 257.258 para 241.501 contratos) — o único das três pernas do complexo em
  que o posicionamento mais recente aponta para menos convicção compradora. **O corte de
  posições de 22/09, que as duas últimas leituras projetavam para 25-26/09, ainda NÃO
  chegou neste dump**, apesar de hoje já ser 25/09 — o evento mais aguardado desta janela
  segue pendente.
- **O volume de hoje (3.441 contratos) é uma fração pequena do volume saudável confirmado
  na última sessão plenamente corrigida (117.139 em 23/09)** — mesmo sem um valor de
  24/09 para comparação direta neste dump, a magnitude por si só levanta a mesma suspeita
  de captura parcial já discutida na Visão Geral; o fechamento de 1.316,75 deve ser tratado
  como provisório, não definitivo.
- **A manchete "Produtor segura a soja..." de 23/09 (Canal Rural), tratada ontem, ainda não
  tem seguimento** — sem indicação de se a retenção do produtor brasileiro persiste ou
  cedeu nos últimos dois dias.
- **Nível técnico a vigiar:** um fechamento de volta abaixo de 1.180 desfaria formalmente
  o rompimento; com a folga em +11,59%, esse cenário segue distante.

**Leitura operacional:** a soja está de fato em compasso de espera — três sessões
essencialmente planas, sem o reforço de convicção que um volume saudável ou um número
concreto de compras chinesas trariam. Para quem está comprado, a folga técnica ampla
(+11,59% sobre 1.180) e o contango da curva seguem favoráveis à manutenção da posição
estrutural, mas não há, hoje, um gatilho novo forte o bastante para justificar reforço —
a manchete de compras chinesas é promissora, mas inconclusiva sem tonelagem. Para quem
opera vendido, a lateralização de três sessões e a redução de net long dos fundos desde
15/09 são os únicos fios de esperança no momento, ainda distantes de qualquer nível
técnico de reversão. O evento mais aguardado — o corte de COT de posições de 22/09 —
segue sem aparecer, e é o gatilho mais provável de destravar direção nos próximos dias.

## Farelo

**Viés: bull, mantido com convicção intacta na direção — quarta alta consecutiva real do
ratio Far/Soj, agora a apenas 2,36 pontos percentuais do teto "apertado", com confirmação
física quádrupla no Brasil — mas com uma reserva nova e específica sobre a magnitude
exata do fechamento de hoje em Chicago, por conta do padrão de captura suspeita que
reaparece pela quarta vez nesta série.**

O que sustenta a tese:

- **O ratio Far/Soj fechou em 84,64% hoje** (indicators, sessão de 25/09), a quarta alta
  seguida real (83,22% em 21/09 → 83,90% em 22/09 → 84,36% em 23/09 → 84,59% em 24/09 →
  **84,64%** hoje) — a maior leitura desta série inteira e a distância mais curta já
  registrada até o território "apertado" (87%): apenas **2,36 pontos percentuais**. Isso
  mantém o ratio **+3,24 pontos percentuais** acima do nível de abertura da tese baixista
  original de 11/06/2026 (81,4%, [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]])
  — trata `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` e
  `-D+90`: ambas seguem aparecendo como "vencidas" na fila de hoje, mas o veredito de
  ambas já está fechado desde
  [[2026-09-17_ratio-far-soj-supera-nivel-de-abertura-da-tese-original-quarta-sessao]]
  (invalidação técnica da tese baixista de junho) e reafirmado pela revisão formal de
  D+90 em [[2026-09-09_d90-ratio-far-soj-reverte-na-vespera]]. Nenhuma ação nova é
  necessária sobre essas duas revisões específicas; resta em aberto apenas o marco de
  D+180, programado para 2026-12-08.
- **O físico de farelo em Rondonópolis/MT (fonte BCSP, via NAG) segue em R$2.200,00/ton
  pela QUARTA leitura seguida (21, 22, 23 e 24/09, var 0,0% em todas)** — o patamar mais
  consolidado desta série inteira.
- **A praça física da média do Rio Grande do Sul (Clicmercado) confirmou hoje, pela
  SEGUNDA vez, o novo patamar de R$2.130,00/ton (var 0,0% frente a 23/09)** — a primeira
  confirmação real de que o salto de +14,52% registrado ontem, depois de 14 dias de
  congelamento, não foi um evento isolado de reprecificação de uma fonte parada. Com essa
  segunda leitura, a confirmação física do aperto de farelo no Brasil passa a vir de
  **três praças distintas simultaneamente** (Rondonópolis, RS e, com a ressalva abaixo,
  o próprio IMEA/MT).
- **O oil share caiu para 47,57% hoje** (de 47,61% ontem, 48,31% em 21/09) — mínima
  monotônica desta janela de cinco sessões, o espelho direto do farelo ganhando
  protagonismo relativo dentro do valor total gerado pelo crush.
- **O oil-meal spread fechou em -0,759 USD/bushel hoje** (de -0,7447 ontem, -0,5313 em
  21/09) — a maior distância real já registrada nesta série entre o valor do farelo e o
  valor do óleo, em termos de bushel-equivalente, aprofundando-se por quatro sessões
  seguidas.
- **O farelo segue folgadamente acima da resistência histórica de 325,00** (fila
  `alerta-quebra_resistencia-farelo_cbot-2026-09-25`: 371,50 vs. 325,00), folga de
  **+14,31%**, a maior desta série.
- **O COT de 15/09 mostrou os fundos com net long em farelo em 183.111 contratos
  (+16,12% frente a 08/09)** — ainda o dado de posicionamento mais recente; o corte de
  22/09, esperado nos últimos dois dias, ainda não chegou.
- **A trajetória sazonal da ABIOVE para o Brasil continua apontando para alívio de oferta
  doméstica de farelo à frente**, sem revisão nesta janela: produção projetada caindo de
  2.142,97 mil t (out/26) para 1.977,59 (nov/26) e 1.659,04 mil t (dez/26); exportação de
  850 para 800 e 700 mil t no mesmo período — um vetor de médio prazo que, se confirmado,
  tende a sustentar o ratio Far/Soj em patamares elevados à frente, na mesma direção da
  tese de curto prazo.

**O que invalida / risco:**

- **O fechamento de hoje em Chicago (371,50, ou 371,80 pelo campo alternativo
  `fechamento_Z26` do mesmo contrato — ver Honestidade) deve ser tratado como provisório.**
  A abertura (370,70), a máxima (372,40), a mínima (370,40) e o volume (830 contratos) do
  dump de hoje são **idênticos, até a última casa decimal, aos de ontem (24/09)** — só o
  "último preço" mudou. Esse é o mesmo padrão que, nas três ocorrências anteriores desta
  série no heating oil, foi revisado 1-2 dias depois com uma mudança de preço de até
  ±5,9% e uma correção de volume de mais de duas ordens de magnitude
  ([[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]]). Se o padrão se repetir,
  o ratio Far/Soj de hoje (84,64%, calculado sobre este mesmo fechamento) também está
  sujeito a revisão — para cima ou para baixo — na próxima geração do dump.
- **O IMEA/MT chegou à QUINTA leitura seguida com o mesmo valor exato (R$1.982,28/ton:
  18, 21, 22, 23 e 24/09)** — cruzando o limiar que a própria leitura de ontem havia
  definido como gatilho de suspeita ("se uma quinta leitura repetir o valor, passa a
  merecer o mesmo tratamento de suspeita de estagnação de fonte que o RS carregou até
  ontem"). Diferente do RS, que se moveu e depois confirmou o novo patamar, o IMEA agora
  é o candidato mais forte desta série a estar simplesmente parado por falta de
  atualização da fonte, não por estabilidade real de mercado — o que significa que a
  "confirmação física tripla" mencionada acima tem, na prática, dois pilares fortes
  (Rondonópolis, RS) e um pilar duvidoso (IMEA).
- **O prêmio de exportação de farelo em Paranaguá segue congelado em 0,12 USD/short_ton
  há 17 dias corridos** (desde 08/09) — se o aperto físico doméstico fosse amplo e
  sustentado, seria razoável esperar, eventualmente, algum reflexo no canal de exportação
  FOB; essa confirmação ainda não apareceu.
- **A curva futura de farelo aprofundou a inversão (backwardation) nos meses mais
  distantes**: dez/26 (base) 371,50 → jan/27 370,10 → mar/27 368,30 → mai/27 367,70
  (-1,02% de dez/26 a mai/27, mais acentuada que os -0,41% de ontem) — o mercado a termo
  segue sem precificar um aperto estrutural que se estenda indefinidamente, coerente com a
  trajetória sazonal de alívio de oferta da ABIOVE, mas o aprofundamento da inversão nos
  últimos dois dias é, em si, um dado a monitorar.
- **Os índices sintéticos ISF e ISO seguem travados em 60/100 e 80/100**, agora há mais de
  catorze dias corridos sem qualquer reação, apesar de o ratio e o oil share terem se
  movido de forma expressiva e consistente nesse período.

**Leitura operacional:** a tendência estrutural de farelo relativamente mais forte que a
soja segue intacta e, na direção, ganha reforço adicional hoje (quarta alta consecutiva do
ratio, segunda confirmação do RS). Mas a magnitude exata do movimento de hoje em Chicago
carrega uma reserva concreta que não existia ontem — o mesmo tipo de reserva que, nas três
ocorrências anteriores no heating oil, precedeu uma revisão de preço relevante. Para quem
está comprado no spread Far/Soj (a forma mais limpa de capturar esta tese), a recomendação
operacional muda pouco: a tendência de fundo (RS confirmado, Rondonópolis consolidado,
ratio subindo pelo quarto dia) sustenta manter ou reforçar a posição, mas o dimensionamento
de qualquer entrada nova hoje especificamente deveria descontar a possibilidade de que o
preço de referência mude na próxima geração do dump. Para quem está comprado em farelo
direcionalmente, o nível técnico (371,50, folga de +14,31% sobre a resistência de 325) seria
favorável mesmo numa eventual revisão para baixo de pequena magnitude. Para quem está
vendido, tanto o nível técnico quanto o calendário sazonal da ABIOVE seguem desfavoráveis
à tese de queda; a inversão crescente da curva futura nos meses mais distantes é o único
argumento a favor de não perseguir o movimento no vencimento mais distante.

## Óleo

**Viés: bear, mantido — quinta sessão seguida abaixo do suporte técnico, oil share em
nova mínima, mas com a mesma reserva de dado que hoje se estende ao farelo: a margem de
biodiesel repicou ligeiramente (+0,53%), porém construída sobre um HO=F cujo padrão de
captura de hoje é idêntico ao que precedeu as três revisões anteriores desta série.**

O que sustenta a tese:

- **Óleo fechou em 67,40 USD cts/lb hoje**, estável frente aos 67,47 de ontem (-0,10%),
  aprofundando a distância abaixo do suporte de referência de 72,00 (fila
  `alerta-quebra_suporte-oleo_cbot-2026-09-25`: **-6,39%**).
- **O oil share caiu para 47,57% hoje** (de 47,61% ontem, 48,31% em 21/09) — mínima
  monotônica desta janela, o óleo perdendo participação no valor total gerado pelo crush
  pela quinta sessão seguida.
- **O oil-meal spread fechou em -0,759 USD/bushel** (de -0,7447 ontem, -0,5313 em 21/09) —
  o óleo cada vez mais atrás do farelo em termos de valor por bushel-equivalente, o
  extremo mais negativo já registrado nesta série.
- **O ISO (Índice de Suporte do Óleo) segue em 80/100**, sem melhora.
- **O forecast estatístico interno segue em "baixista" nos dois horizontes (7d e 30d)** —
  extrapolação de tendência, não fundamentalista, mas coerente com a deterioração real do
  oil share.
- **A lente fiscal brasileira segue estruturalmente desfavorável, sem mudança hoje**: a MP
  1.363/2026 (subvenção ao diesel fóssil, vigente até 31/12/2026) segue plenamente
  vigente; a isenção de PIS/Cofins do biodiesel na mistura está agora **56 dias corridos
  vencida** (vigência até 31/07/2026) sem sinal de renovação.

**O que sustenta um contraponto — com uma reserva de dado que hoje é maior, não menor,
do que ontem:**

- **A margem de biodiesel americana subiu para US$1,8314/galão hoje, um repique de
  +0,53% frente aos US$1,8218 de ontem** — a primeira alta em três sessões (2,0908 em
  21/09 → 2,2131 em 22/09 → 2,0557 em 23/09 → 1,8218 em 24/09 → **1,8314** hoje). Mas essa
  leitura precisa vir com a mesma reserva aplicada ao farelo: o HO=F de hoje (4,5214 USD/
  galão, volume 372 contratos) tem abertura, máxima, mínima e volume **idênticos aos de
  ontem**, só o fechamento mudou — exatamente o padrão que, nas três ocorrências
  anteriores desta série, precedeu uma revisão de preço de até +5,9%. Se a revisão vier
  para cima (o viés histórico das três ocorrências passadas), a margem de biodiesel real
  pode estar mais alta do que os US$1,8314 aqui registrados — o que enfraqueceria, não
  reforçaria, a tese bear no curto prazo. Este é o contraponto mais frágil desta leitura,
  e desta vez a fragilidade é sobre a direção da revisão, não só a magnitude.
- **O RIN D4 (crédito de biocombustível renovável americano) permanece constante na
  fórmula interna** — nenhuma variação real de política regulatória americana explicaria
  o repique de margem de hoje; ele vem inteiramente do lado do heating oil, com todas as
  ressalvas acima.
- **A curva futura de médio prazo segue em contango regular**: out/26 66,74 → dez/26
  (base) 67,40 → jan/27 67,63 → mar/27 67,99 → mai/27 68,30 (+1,34% de dez/26 a mai/27) —
  sem sinal de reprecificação estrutural de curto prazo.
- **Catalisadores de alta represados, ainda não correntes**: B16 (elevação da mistura de
  biodiesel para 16%) segue "adiado", resultado esperado por volta de novembro/2026; a
  centralização da exportação de palma pela Indonésia via Danantara, que tinha alvo de
  assunção plena em 01/09/2026, já soma **24 dias** de atraso sem confirmação — ambos
  seguem como upside represado, não corrente.

**Leitura operacional:** o quadro técnico (abaixo do suporte de 72,00 pela quinta sessão
seguida, oil share em mínima) e o calendário fiscal (MP 1.363 vigente até dezembro,
isenção PIS/Cofins já 56 dias vencida) seguem sustentando o lado vendido direcional. Mas o
repique de +0,53% na margem de biodiesel de hoje, ainda que pequeno, é o primeiro sinal em
três sessões na direção contrária à tese — e ele vem justamente no dia em que o HO=F que
alimenta essa margem mostra o mesmo padrão de captura suspeita que, historicamente, tende
a ser revisado para cima. Para quem está vendido, a recomendação é manter a posição
apoiada no quadro técnico e fiscal, que não dependem do HO=F, mas monitorar a próxima
geração do dump antes de reforçar com base especificamente na margem de biodiesel. Para
quem está comprado ou avalia entrar, o argumento mais forte a favor de uma reversão da
tese bear é justamente este: se o padrão histórico se repetir e o HO=F for revisado para
cima na próxima sessão, a margem de biodiesel pode confirmar uma recuperação real, não
apenas um repique de dado ruidoso. Para quem opera o spread farelo-óleo dentro do crush, o
oil-meal spread fechou em -0,759 USD/bushel, o extremo mais negativo já registrado nesta
série — uma zona que começa a chamar atenção como possível candidata a mean-reversion,
ainda sem qualquer sinal técnico de reversão presente.

## Spreads e crush (leitura de complexo)

O ratio Far/Soj fechou em **84,64%** hoje, a quarta alta consecutiva real (83,22% →
83,90% → 84,36% → 84,59% → 84,64%, de 21 a 25/09) e a maior leitura já registrada nesta
série — dentro da zona neutra (80-87%), mas a apenas **2,36 pontos percentuais** do teto
"apertado" (87%) e a **4,64 pontos** do piso "abundante" (80%), a menor distância ao teto
já registrada nesta série de leituras diárias. O oil share, em **47,57%**, mostra o óleo
respondendo por menos da metade do valor gerado no esmagamento, numa trajetória de queda
monotônica desde 48,31% em 21/09. O crush margin, em **US$2,4195/bushel**, segue abaixo do
piso de referência de US$2,50 monitorado pela fila (`alerta-quebra_suporte-complexo_soja-2026-09-25`,
distância de **-3,22%**), recuando ligeiramente frente aos 2,4231 de ontem (-0,15%), e
segue oscilando num intervalo estreito (2,3716-2,4323 desde 22/09) — sinal de
estabilização abaixo do nível de referência, não de recuperação em curso nem de
deterioração acelerada.

Os dois índices compostos por contagem de condições — ISF (60/100) e ISO (80/100) —
seguem travados no mesmo patamar desde 11/09, agora há mais de catorze dias corridos sem
qualquer reação, apesar de o ratio e o oil share terem se movido de forma expressiva e
consistente nesse período — o lembrete de sempre nesta série de que esses índices
específicos reagem a mudanças de regime estrutural, não a oscilações de curto e médio
prazo dentro da mesma faixa.

**O que muda hoje na leitura de complexo é metodológico, não direcional**: pela primeira
vez nesta série, o mesmo padrão de captura suspeita que já forçou três correções no
heating oil (HO=F) aparece também no farelo — o insumo direto do ratio Far/Soj, a métrica
mais central de toda esta leitura diária. Isso não muda a conclusão de que o complexo
está estruturalmente inclinado para bull-farelo/bear-óleo (essa conclusão se apoia em
múltiplas fontes independentes: física BR, trajetória de cinco sessões do ratio, ABIOVE),
mas adiciona uma camada de ceticismo específica sobre o valor exato do fechamento de hoje
que deve ser carregada para a leitura de amanhã — se o padrão se confirmar novamente
amanhã, passa a valer o mesmo tratamento de "padrão estrutural, não acidental" que este
sistema já aplicou ao HO=F em [[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]],
agora estendido ao contrato de farelo.

O COT de 15/09, ainda o dado de posicionamento mais recente dez dias depois, retrata os
fundos com net long ampliado em farelo (+16,12%) e óleo (+10,65%) e reduzido em soja
(-6,13%). O corte de posições de 22/09, que as duas últimas leituras projetavam para
25-26/09, **ainda não apareceu neste dump apesar de hoje já ser 25/09** — o evento de
posicionamento mais aguardado desta janela segue pendente, e é o dado mais capaz de
confirmar (ou desmentir) se os fundos ampliaram convicção em farelo e óleo diante do
quadro físico e fiscal aqui descrito, ou se já começaram a realizar lucro.

## Lente fiscal/regulatória BR

Antes de fechar qualquer tese de preço BR, os vetores tributários/regulatórios vivos que
pesam no complexo — todos do `system/tributario_watch.toml`, cujo carimbo mais recente
(`atualizado_em`) em todos os 10 eventos catalogados é 2026-06-05, ou seja, **112 dias
corridos sem revisão humana** frente a hoje (25/09):

- **MP 1.363/2026** (id `MP-1363-2026`, subvenção diesel fóssil R$1,12/L, vigente até
  31/12/2026): barateia o diesel fóssil no mix B15 (mistura obrigatória de 15% de
  biodiesel), reduzindo a competitividade relativa do biodiesel e a demanda doméstica por
  óleo de soja — vetor estrutural de baixa para óleo, plenamente vigente, sem mudança de
  status.
- **B16 (id `B16-CNPE-2026`, elevação da mistura obrigatória de biodiesel para 16%)**
  segue "adiado", resultado esperado por volta de novembro/2026. Upside represado (~436
  mil toneladas de demanda potencial adicional de óleo), não corrente.
- **Isenção de PIS/Cofins do biodiesel na mistura** (id `PISCOFINS-BIODIESEL-ISENCAO`):
  vigência registrada até 31/07/2026 — já **56 dias corridos vencida** frente a
  25/09/2026, sem registro de prorrogação ou expiração.
- **MP 1.358/2026** (subvenção gasolina R$0,89/L): vigência registrada até 11/07/2026,
  agora **76 dias corridos vencida**.
- **STJ REsp 2.165.276** (id `STJ-RESP-2165276`, crédito de PIS/Cofins sobre soja em
  biodiesel, direção "alta" para soja/óleo): sem novidade nesta janela.
- **EPA RFS 2026/2027** (id `EPA-RFS-2026-2027`, mandato de biocombustível americano,
  direção "alta" para óleo): sustenta o RIN D4, estável, e o RIN permanece constante na
  fórmula interna de margem de biodiesel usada por este sistema — o repique de margem de
  hoje vem inteiramente do heating oil (com a ressalva de captura já descrita), não de
  mudança regulatória.
- **Crédito 45Z** (id `45Z-CLEAN-FUEL`, em tramitação, direção "mista"): sem novidade.
- **Indonésia — Danantara** (id `DANANTARA-INDONESIA`) e **levy de exportação PMK 9/2026**
  (id `INDONESIA-LEVY-PMK9`): a assunção plena da centralização da exportação de palma
  pela Indonésia tinha alvo 01/09/2026 — já se passaram **24 dias** sem confirmação.
  Catalisador de alta represado para óleo (via substituição com palma) — ainda sem dado de
  MPOB disponível para monitorar diretamente (parser continua quebrado, ver Honestidade).
- **Indonésia B50** (id `INDONESIA-B50`, monitorando, direção "alta"): sem novidade.

Nenhum desses vetores muda a leitura de preço de hoje isoladamente — mas, em conjunto,
eles seguem reforçando a mesma assimetria já descrita em leituras anteriores: o mercado
interno brasileiro tem múltiplos desincentivos correntes ao óleo (MP 1.363 plenamente
vigente, isenção PIS/Cofins já 56 dias vencida) e múltiplos catalisadores de alta
represados, não correntes (B16, Danantara, B50). O óleo brasileiro segue mais fraco
estruturalmente até que algum dos vetores represados vire fato concreto — e a lacuna
crescente de 112 dias sem revisão humana do catálogo tributário é, em si, um risco
operacional recorrente nesta série: qualquer um destes vetores pode ter mudado de status
na realidade sem que este sistema tenha como saber.

## Riscos e eventos próximos

- **Confirmação (ou revisão) do fechamento de hoje em farelo e no HO=F**, dado o padrão
  de abertura/máxima/mínima/volume idênticos ao dia anterior — o teste mais imediato
  desta janela inteira, capaz de mudar tanto o valor exato do ratio Far/Soj quanto o da
  margem de biodiesel de hoje.
- **Próximo corte de COT (posições de 22/09), esperado desde 25-26/09 e ainda não
  chegado** — o evento de posicionamento mais aguardado; primeiro capaz de confirmar se os
  fundos ampliaram ou realizaram lucro nas posições de farelo e óleo desde 15/09, e se a
  redução de net long em soja se acentuou.
- **Tonelagem e contraparte da manchete "China buys soybeans" (24/09, Farm Progress)** —
  sem esse número, a manchete permanece uma indicação qualitativa, não um dado
  operacionalizável.
- **Confirmação (ou ruptura) do padrão de estagnação do IMEA/MT**, agora em cinco leituras
  seguidas no mesmo valor exato (R$1.982,28/ton) — cruzou o limiar de suspeita definido
  ontem; uma sexta leitura repetida reforçaria a hipótese de fonte parada, não de mercado
  estável.
- **USDA Crop Progress**: próximo corte esperado por volta de 27-28/09.
- **Nível técnico a vigiar em farelo:** volta abaixo de 325,00 desfaria o rompimento
  (folga atual +14,31%).
- **Nível técnico a vigiar em soja:** volta abaixo de 1.180,00 desfaria o rompimento
  (folga atual +11,59%).
- **Nível técnico a vigiar em óleo:** recuperação acima de 72,00 desfaria a leitura de
  suporte rompido (distância atual -6,39%).
- **Crush margin:** retorno acima de US$2,50/bushel encerraria a leitura de suporte
  rompido monitorada pela fila (distância atual -3,22%).
- **Prêmio de exportação de farelo e óleo em Paranaguá**, congelado há 17 dias corridos.
- **NOPA mensal**: mais um "release" sem dado novo de fato (paywall), agora referenciado
  como `release-nopa-2026-09-25`.
- **Confirmação da centralização plena da exportação de palma pela Danantara** — alvo
  01/09, já 24 dias passados sem confirmação.
- **Vigência da isenção PIS/Cofins do biodiesel** (56 dias vencida) e **MP 1.358/2026 da
  gasolina** (76 dias vencidos) — checar notícia de renovação/expiração.
- **Marco de 112 dias sem revisão humana do `tributario_watch.toml`**.
- **Revisão de D+180 da tese original do ratio Far/Soj**, programada para 2026-12-08.
- **Se o padrão de captura suspeita se repetir amanhã em farelo pela segunda vez seguida**,
  passa a valer o mesmo tratamento de "padrão estrutural" já aplicado ao HO=F — um
  candidato natural a um insight dedicado, à parte da leitura diária.

## Honestidade

- **O achado central desta leitura é um alerta de qualidade de dado, não uma correção
  confirmada.** A abertura, a máxima, a mínima e o volume do farelo e do heating oil
  (HO=F) na sessão de 25/09 são idênticos, até a última casa decimal, aos de 24/09 — só
  o fechamento mudou. Isso é consistente com o padrão de captura parcial já documentado
  três vezes nesta série ([[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]]),
  mas, diferente da correção de 23/09
  ([[2026-09-24_correcao-numeros-sessao-23set-fim-do-artefato-de-baixa-liquidez]]), esta
  leitura NÃO tem um dado corrigido para comparar — apenas a suspeita fundamentada. Os
  números de hoje (ratio Far/Soj 84,64%, margem de biodiesel 1,8314) são os únicos
  disponíveis e são usados nesta leitura como a melhor estimativa corrente, mas devem ser
  tratados como provisórios até a próxima geração do dump.
- **O campo `fechamento_Z26` do farelo (371,80) diverge do campo `fechamento` genérico do
  mesmo contrato/ticker ZMZ26.CBT (371,50)** — uma inconsistência interna nova, distinta
  da questão de volume acima, dentro do próprio dump de hoje. Esta leitura usa 371,50 (o
  campo `fechamento` padrão, na mesma convenção usada para soja e óleo, onde os dois
  campos batem) como referência primária, mas registra a divergência para o caso de a
  próxima geração do dump reconciliar os dois valores de forma diferente.
- **Pequenas revisões residuais nos números históricos seguem aparecendo entre gerações
  do dump** — por exemplo, o ratio Far/Soj de 23/09 usado nesta leitura (84,36%, via
  indicators de hoje) difere em 0,06 ponto do valor citado pela leitura de ontem para a
  mesma data (84,30%), e o fechamento de soja embutido na fórmula de crush margin de
  23/09 também mudou ligeiramente entre gerações (1.317,50 na leitura de ontem, 1.318,00
  no dump de hoje). Nenhuma dessas diferenças muda a leitura qualitativa (a trajetória de
  alta do ratio permanece idêntica em ambas as versões), mas registram que mesmo dados
  "já fechados" desta série carregam ruído residual de até ~0,3-0,5 ponto entre gerações.
- **O IMEA/MT atingiu cinco leituras seguidas no mesmo valor exato** (R$1.982,28/ton) —
  cruzando o limiar de suspeita que a própria leitura de ontem havia definido. Tratada
  nesta leitura como provável estagnação de fonte, não confirmação de mercado físico
  estável, mas sem certeza absoluta.
- **A manchete "China buys soybeans" (24/09, Farm Progress) está disponível apenas como
  título** — sem tonelagem, contraparte ou corpo de texto, não é possível avaliar o peso
  real desse dado para a tese de soja.
- **O corte de COT `release-cftc_cot-2026-09-15` segue sendo o dado de posicionamento
  mais recente**, agora dez dias corridos depois do corte, apesar de duas leituras
  seguidas projetarem a chegada do corte de 22/09 para hoje ou amanhã.
- **Percentil histórico de posicionamento COT não está disponível no briefing** — toda
  leitura de "fundos comprando/vendendo" nesta série usa variação absoluta semana a
  semana de contratos, não percentil histórico.
- **O item de fila `release-nopa-2026-09-25` é mais uma repetição sem dado novo** — o
  mesmo padrão de todas as leituras anteriores desde que este monitoramento começou
  (paywall, `monthly_status` em 0,0 bool).
- **`tributario_watch.toml` sem atualização há 112 dias corridos** — pelo menos dois
  vetores (isenção PIS/Cofins do biodiesel, MP 1.358/2026) já passaram da vigência
  registrada sem nota de renovação ou expiração.
- **A previsão INMET para 25/09 é previsão meteorológica, não medição de precipitação ou
  temperatura real** — as menções a "possibilidade de chuva isolada" são indicativas do
  boletim, não confirmação de que o evento ocorreu ou ocorrerá.
- **MPOB (palma Malásia) segue com parser quebrado** — nenhum dado de produção/estoque de
  palma malaia disponível, o que impede monitorar diretamente o catalisador represado da
  centralização de exportação indonésia (Danantara).
- **Não há seção `bcba` (Argentina) neste dump** — nenhum dado direto de safra ou
  exportação argentina disponível além do que já vem consolidado pelo WASDE (edição de
  11/09, agora 14 dias de idade).
- **Os forecasts estatísticos internos (bandas 7d/30d) foram gerados hoje sobre o
  fechamento de 25/09** — que, pela própria ressalva acima, é provisório; o viés
  "altista" em farelo e "baixista" em óleo (ambos horizontes) refletem extrapolação
  estatística de tendência (MA20 + volatilidade + slope), não uma reavaliação
  fundamentalista, e herdam a mesma incerteza do dado de origem.
- **A fila de julgamento volta a listar as revisões D+7 e D+90 da tese de 11/06 como
  "vencidas"** — o veredito de ambas já foi fechado em
  [[2026-09-17_ratio-far-soj-supera-nivel-de-abertura-da-tese-original-quarta-sessao]] e
  reafirmado em [[2026-09-09_d90-ratio-far-soj-reverte-na-vespera]]; o sistema de fila não
  lê de volta os insights publicados para marcar a revisão como encerrada. Nenhuma ação
  nova é necessária sobre essas duas revisões específicas.
