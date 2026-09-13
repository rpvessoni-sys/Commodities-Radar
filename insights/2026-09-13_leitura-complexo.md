---
data: 2026-09-13
titulo: "Domingo sem pregão novo (última sessão negociada segue sendo sexta-feira 11/09): a leitura de hoje corrige números de fechamento, volume e heating oil usados erroneamente ontem e revela que a margem de biodiesel americana não recuou — bateu recorde da janela (US$2,135/galão, +3,30%) — uma divergência real entre o preço do óleo caindo em Chicago e sua economia de demanda melhorando; farelo segue com o ratio Far/Soj acima de 80% pela fila auto-gerada, mas por margem mais estreita do que o descrito ontem, e a soja mantém tendência de alta com o primeiro sinal técnico de reversão genuíno da janela, agora mais extremo do que se pensava"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT — linhas brutas da sessão de 2026-09-11 (sexta-feira, quarto pregão pleno desde a reabertura de 08/09; hoje, sábado 12 e domingo 13/09, não há pregão): soja (ZSX26, venc. nov/26) abertura 1.330,00, máxima 1.335,25, mínima 1.293,00, fechamento **1.296,50** USD cts/bushel, volume **162.475** contratos; farelo (ZMV26, venc. out/26) abertura 349,30, máxima 350,60, mínima 344,70, fechamento **346,80** USD/short ton, volume 30.816 contratos; óleo (ZLV26, venc. out/26) abertura 71,57, máxima 71,72, mínima 69,05, fechamento **69,19** USD cts/lb, volume 32.345 contratos. Curva futura em 11/09 — soja: set/26 1.296,00, nov/26 (base) 1.296,50, jan/27 1.312,00, mar/27 1.318,75, mai/27 1.325,00, jul/27 1.328,50; farelo: set/26 347,00, out/26 (base) 346,80, dez/26 352,80, jan/27 354,70, mar/27 356,10, mai/27 356,90; óleo: set/26 69,01, out/26 (base) 69,19, dez/26 69,68, jan/27 69,99, mar/27 70,19, mai/27 70,24
  - CME NYMEX heating oil (HO=F) — 2026-09-11: abertura 5,1481, máxima 5,1664, mínima 4,9380, fechamento **4,9593** USD/galão, volume 62.190 contratos. Nota: o dump não traz fechamento/máxima/mínima/volume de heating oil para 10/09 (apenas abertura, 4,7964) — ver Honestidade
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, ISF, ISO, margem biodiesel, paridade BR) — 2026-09-11: crush margin **2,2755** USD/bushel, far_soj_ratio_pct **80,25%**, oil_share_pct **49,94%**, oil_meal_spread_usd_bu **-0,0187**, ISF (Índice de Sobra de Farelo) 60/100, ISO (Índice de Suporte do Óleo) 80/100, paridade BR soja **R$145,54/saca**, biodiesel: custo_oleo 5,1893 USD/galão, receita 8,1243 USD/galão, margem **2,135** USD/galão. Comparação 10/09: crush margin 2,2458, ratio 78,95%, oil share 50,46%, oil-meal spread +0,1419, paridade R$150,23, margem biodiesel 2,0667
  - **Auditoria numérica publicada hoje em separado** — [[2026-09-13_correcao-numeros-sessao-11set-farelo-oleo]]: os valores acima (fechamento soja/farelo/óleo, volume, heating oil, ratio, oil share, oil-meal spread, margem biodiesel) divergem dos usados em [[2026-09-12_leitura-complexo]] e em [[2026-09-12_ratio-far-soj-rompe-80-pela-primeira-vez]]; esta leitura usa os valores do dump de hoje, corroborados independentemente pela própria fila de julgamento auto-gerada (itens `alerta-movimento_forte-soja_cbot-2026-09-11` e `alerta-movimento_forte-oleo_cbot-2026-09-11`) e pela consistência aritmética interna dos indicadores
  - BCB PTAX — 2026-09-11: USD/BRL 5,0918, EUR/BRL 5,9085, Selic diária 0,05166% a.a. (séries SGS 1, 21619, 11); 2026-09-10: USD/BRL 5,1149
  - CFTC COT Managed Money, Swap Dealers e Producer/Merchant — corte de 2026-09-08 (ainda o mais recente disponível, tratando novamente `release-cftc_cot-2026-09-08`, já com cinco dias corridos de defasagem frente à sessão de 11/09): farelo net long managed money 157.689 contratos (+0,32% vs 01/09), long -2,86%, short -26,73% — cobertura de vendida, não convicção nova; óleo net long 91.711 contratos (-8,13% vs 01/09), short +17,14%; soja net long 257.258 contratos (+9,51% vs 01/09), long +8,42% — dinheiro novo comprado. Open interest: soja 1.070.401 (+4,17%), farelo 667.618 (+2,86%), óleo 601.961 (-1,16%)
  - CEPEA/ESALQ Soja Paranaguá e Paraná interior via NAG, e físico de farelo (MT/IMEA, Rondonópolis, RS) — última leitura ainda 2026-09-09, agora **4 dias corridos** sem atualização própria (10, 11, 12 e 13/09); prêmios export Paranaguá (farelo +0,12 USD/short ton, óleo +0,10 cts/lb) congelados desde 27/08, **17 dias corridos**
  - USDA Crop Progress — corte de 2026-09-06: 12% excelente / 46% boa / 9% ruim (G/E 58%), inalterado desde 30/08; próximo corte esperado segunda-feira 14/09 (amanhã)
  - USDA WASDE — release de 2026-09-11, tratando novamente `release-usda_wasde-2026-09-11`: apenas tabela de farelo (Argentina, Brasil, China parcial), comparando agosto vs setembro/2026; sem tabelas de soja em grão nem de óleo, sem dados dos EUA — ver Honestidade
  - NOPA — fila `release-nopa-2026-09-12` (novo carimbo, mesmo conteúdo): `monthly_status` seguiu em 0,0 bool (paywall) em 2026-09-12, sexto dia seguido do mesmo falso positivo desde 27/08
  - ABIOVE projeções mensais — balanços set-dez/2026, sem revisão nesta janela
  - NOAA CPC ENSO — El Niño Advisory, inalterado até 2026-09-12
  - MPOB — carimbo 2026-09-12, parser sem números extraídos (mesma barreira, 3.457 caracteres)
  - BCBA (Argentina) — carimbo 2026-09-09, scraper acessa a página mas não encontra links de relatório
  - INMET — previsão para **2026-09-13 (HOJE)**: queda de temperatura e aumento de nebulosidade/chuva frente à véspera em praticamente todos os pontos monitorados — Cuiabá/MT 32°C/24°C (chuva isolada, ante 37°C/27°C em 12/09), Sinop/MT 39°C/23°C, Sorriso/MT 39°C/23°C, Lucas do Rio Verde/MT 39°C/23°C (todos "muitas nuvens", sem chuva mencionada), Rio Verde/GO 35°C/22°C; no Sul, resfriamento mais acentuado — Cascavel/PR 19°C/13°C (ante 29°C/17°C em 12/09, com pancadas de chuva isoladas), Maringá/PR 23°C/17°C (chuva e trovoadas isoladas), Passo Fundo/RS 16°C/9°C (chuva isolada, sem menção de geada)
  - Notícias Agrícolas/Canal Rural + FarmProgress RSS — 2026-09-12: "0 items lidos, 0 mantidos", terceiro dia seguido de falha ou pausa total de coleta (10, 11 e 12/09)
  - system/tributario_watch.toml (lido como referência, não editado) — `atualizado_em` 2026-06-05 em todos os 10 eventos catalogados, **100 dias corridos** sem revisão humana frente a hoje (13/09) — marco redondo
  - Forecasts estatísticos internos (bandas 7d/30d) — geração de 2026-09-12, alvos 19/09 (7d) e 12/10 (30d); viés "altista" em soja, farelo e óleo nos dois horizontes, calculado sobre o fechamento de 11/09 — ver Honestidade
  - Fila de julgamento (carimbada 2026-09-12 no briefing, 11 itens) — tratados nesta leitura: `alerta-quebra_resistencia-soja_cbot-2026-09-11`, `alerta-movimento_forte-soja_cbot-2026-09-11`, `alerta-quebra_suporte-oleo_cbot-2026-09-11`, `alerta-movimento_forte-oleo_cbot-2026-09-11`, `alerta-quebra_resistencia-farelo_cbot-2026-09-11`, `alerta-quebra_suporte-complexo_soja-2026-09-11`, `ratio-zona-2026-09-11`, `release-usda_wasde-2026-09-11`, `release-nopa-2026-09-12`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`
  - Cruza com [[2026-09-12_leitura-complexo]] (leitura de ontem, cujos números de sessão são corrigidos aqui), [[2026-09-12_ratio-far-soj-rompe-80-pela-primeira-vez]] (insight dedicado ao rompimento do ratio, também corrigido), [[2026-09-09_d90-ratio-far-soj-reverte-na-vespera]] (veredito D+90) e [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (tese original)
status: ativa
vies: [bull-soja, neutral-farelo, bear-oleo_soja]
---

## Visão geral

Hoje é domingo, 13/09/2026, e não houve pregão na CBOT (bolsa de grãos de Chicago onde
soja, farelo e óleo de soja são negociados em contratos futuros) nem sábado nem hoje — a
última sessão negociada continua sendo sexta-feira, 11/09/2026, o quarto pregão pleno
desde a reabertura de terça-feira 08/09. Isso significa que o "dado do dia" de hoje é, na
prática, o mesmo dado do dia de ontem. Mas esta leitura tem um trabalho importante a
fazer antes de reafirmar qualquer tese: ao conferir os números que a leitura de ontem
([[2026-09-12_leitura-complexo]]) usou contra as linhas brutas que o dump de hoje
efetivamente traz para aquela mesma sessão de 11/09, várias divergências apareceram — no
fechamento da soja, do farelo, do óleo, no volume negociado, no heating oil (diesel de
aquecimento americano, cujo preço entra na receita do biodiesel) e, por consequência, no
ratio Far/Soj, no oil share e na margem de biodiesel. Essa auditoria está registrada com
todo o detalhe em um insight próprio,
[[2026-09-13_correcao-numeros-sessao-11set-farelo-oleo]], e esta leitura já incorpora os
valores corrigidos — corroborados de forma independente pela própria fila de julgamento
do sistema (que é gerada automaticamente a partir do banco de indicadores, não por este
analista): os itens `alerta-movimento_forte-soja_cbot-2026-09-11` e
`alerta-movimento_forte-oleo_cbot-2026-09-11` citam literalmente as variações corretas
(-2,68% e -3,11%, respectivamente) usando os fechamentos corretos (1.296,50 e 69,19).

Recapitulando o mecanismo básico do complexo para quem não acompanha o dia a dia: a soja
em grão, ao ser esmagada ("crush", o processo industrial que separa o grão em farelo e
óleo), vira dois produtos com demandas muito diferentes — farelo (concentrado de proteína
para ração animal) e óleo (alimentação humana e, cada vez mais, biodiesel). O "crush
margin" mede, em dólares por bushel (unidade agrícola americana de ~27,2 kg de soja),
quanto sobra para a esmagadora depois de vender farelo + óleo e pagar a soja. O "oil
share" (fatia do valor total do crush que vem do óleo) diz qual dos dois produtos está
"pagando a conta": alto = óleo manda e farelo vira subproduto barato (o "Índice de Sobra
de Farelo", ISF, capta isso do lado baixista do farelo); baixo = o farelo sustenta o crush
e o óleo perde força relativa (o "Índice de Suporte do Óleo", ISO, é o espelho). O ratio
Far/Soj (preço do farelo dividido pelo da soja, normalizado em percentual) mede a mesma
ideia de forma mais direta: abaixo de 80% o farelo está "abundante" (viés baixista); entre
80% e 87% ele está em zona "neutra"; acima de 87% fica "apertado" (viés altista).

Com os números corrigidos, o quadro da sessão de 11/09 é o seguinte: soja caiu **-2,68%**
(de 1.332,25 para 1.296,50, CME CBOT — mais forte do que os -2,50% descritos ontem),
farelo caiu **-1,08%** (de 350,60 para 346,80 — mais forte do que os -0,80% descritos
ontem) e óleo caiu **-3,11%** (de 71,41 para 69,19 — um pouco menos forte do que os -3,22%
descritos ontem). A ordem de queda continua a mesma (óleo > soja > farelo em módulo), e o
farelo continua sendo, proporcionalmente, o mais resiliente dos três — mas as magnitudes
exatas mudam a leitura fina de quanto essa resiliência vale. O ratio Far/Soj fechou em
**80,25%** (não 80,32%), ainda o primeiro fechamento acima de 80% desde a abertura da tese
de abundância de farelo em 11/06/2026, mas por uma margem de apenas 0,25 ponto percentual
acima do limiar — bem mais estreita do que os 0,32 ponto percentual anteriormente
reportados. O oil share fechou em **49,94%** (não 49,84%) — ainda a primeira leitura
abaixo de 50% da janela, mas a apenas 0,06 ponto percentual do limiar, uma margem quase
inexistente. O oil-meal spread virou negativo, mas para **-0,0187** USD/bushel (não
-0,0495) — um empate técnico entre óleo e farelo dentro do crush, não uma vitória clara do
farelo como a leitura de ontem descreveu.

O achado mais importante desta auditoria, porém, está no óleo: a leitura de ontem
descreveu a margem de biodiesel americana recuando -5,11% (para US$1,961/galão) por causa
de um suposto colapso do heating oil. Os números corretos mostram o oposto: a margem de
biodiesel fechou em **US$2,135/galão**, uma alta de **+3,30%** sobre 10/09, o valor mais
alto de toda a janela visível do dump (superando 04/09, 08/09, 09/09 e 10/09) e a terceira
alta diária consecutiva. O mecanismo real: o custo do óleo como insumo caiu -3,11% junto
com o próprio preço do óleo em Chicago — e como óleo é custo (não receita) para quem
produz biodiesel, um óleo mais barato **melhora** a margem do produtor, não piora. Isso
significa que a queda do óleo em Chicago na sexta-feira aconteceu **apesar de**, não
**por causa de**, uma deterioração da economia de biodiesel americana — uma divergência
real entre o preço (caindo, com leitura técnica bearish) e um dos principais fundamentos
de demanda do óleo (biodiesel, melhorando) que a leitura de ontem não capturou. Esse ponto
é desenvolvido com profundidade na seção Óleo abaixo e rebaixa a convicção do viés
baixista de "moderado a forte" para "moderado".

**Leitura de uma linha**: o pivô do complexo continua sendo a realocação de valor entre
farelo e óleo dentro do crush, e o ratio Far/Soj ainda fecha (por pouco) acima de 80% pela
primeira vez em 92+1 dias de tese — mas por margens mais estreitas do que se pensava em
quase todas as métricas, exceto uma: a divergência entre o preço do óleo e sua margem de
biodiesel, que é maior e mais clara do que qualquer leitura anterior havia notado.
Confiança **moderada**: ainda um único dia de dado fresco (agora "envelhecido" por dois
dias corridos de fim de semana sem negociação), sem confirmação de COT contemporâneo (o
corte mais recente é de 08/09, cinco dias antes da sessão que estamos analisando) nem de
reação do físico brasileiro (congelado desde 09/09).

## Soja

**Viés: bull, moderado (mantido de ontem) — a tendência de fundo desde a reabertura segue
intacta e a folga sobre a resistência de 1.180 continua ampla, mas a sessão de 11/09,
agora com o fechamento corrigido, mostra um sinal de reversão técnica ainda mais extremo
do que o descrito ontem: o fechamento não ficou a 6 pontos da mínima do dia, ficou a
apenas 3,50 pontos — um fechamento no oitavo inferior do próprio range.**

O que sustenta a tese:

- **A folga técnica sobre a resistência de referência continua ampla.** Soja CBOT fechou
  em **1.296,50** USD cts/bushel em 11/09/2026 (CME CBOT), uma queda de **-2,68%** frente
  aos 1.332,25 do dia anterior — mais forte do que os -2,50% reportados ontem, porque o
  fechamento correto (1.296,50) é mais baixo do que o valor usado (1.299,00); ver
  [[2026-09-13_correcao-numeros-sessao-11set-farelo-oleo]]. A fila de julgamento confirma
  esse fechamento como "acima da resistência de 1.180,00"
  (`alerta-quebra_resistencia-soja_cbot-2026-09-11`), com folga de **9,87%** — ligeiramente
  menor do que os 10,08% calculados ontem com o número errado, mas ainda um colchão
  confortável. A própria fila também confirma a variação diária exata
  (`alerta-movimento_forte-soja_cbot-2026-09-11`, "-2.68% ... de 1332.25 para 1296.50").
- **A queda, mesmo maior do que se pensava, ainda não desfaz a tendência de fundo.** -2,68%
  é a maior queda diária em módulo desde a reabertura, mas segue menor do que a alta de
  +1,70% de 10/09 ou o acumulado desde 08/09. A curva futura segue em contango regular:
  set/26 1.296,00 → nov/26 (base) 1.296,50 → jan/27 1.312,00 → mar/27 1.318,75 → mai/27
  1.325,00 → jul/27 1.328,50 (CME CBOT, 11/09) — sem inversão nem distorção pontual, o que
  sugere ajuste de curto prazo, não repreciﬁcação estrutural.
- **O COT de 08/09 (ainda o mais fresco disponível, agora com cinco dias corridos de
  defasagem) mostrou os fundos ampliando fortemente a convicção compradora na semana
  anterior a esta queda.** Managed money net long em soja saltou de 234.920 para **257.258
  contratos** (+9,51%, CFTC COT), com o long subindo +8,42% e o short subindo apenas
  +1,20% — dinheiro novo entrando, não cobertura. O open interest também cresceu (+4,17%),
  reforçando participação genuína. Essa foto é de cinco dias antes da sessão analisada —
  ainda mais desatualizada agora do que era na leitura de ontem, mas segue sendo o único
  retrato de convicção institucional disponível.
- **O câmbio amorteceu, mas não anulou, a queda para quem vende em reais.** USD/BRL fechou
  em **5,0918** (BCB PTAX, 11/09), uma queda de -0,45% sobre os 5,1149 de 10/09. Como o
  CBOT caiu mais forte (-2,68%) do que o câmbio ajudou (-0,45%), a paridade em reais da
  soja (CBOT × câmbio, sem basis) recuou de **R$150,23/saca** para **R$145,54/saca**
  (indicators, 11/09) — uma queda de **-3,12%** (mais forte do que os -2,94% calculados
  ontem com o número errado), maior em módulo do que a própria queda em dólar, porque os
  dois efeitos trabalharam na mesma direção contra o vendedor brasileiro.
- **A condição da lavoura americana segue estável.** USDA Crop Progress permanece no corte
  de 06/09 (12% excelente + 46% boa, "ruim" 9%, G/E 58%), idêntico a 30/08. Próximo corte
  esperado amanhã, segunda-feira 14/09.

**O que invalida / risco:**

- **O padrão técnico da sessão de 11/09 é, com o número corrigido, ainda mais preocupante
  para o lado comprado do que a leitura de ontem descreveu.** Fechamento em 1.296,50,
  apenas **3,50 pontos** (0,27%) acima da mínima do dia (1.293,00) — contra máxima de
  1.335,25 (amplitude total de 42,25 pontos) — um fechamento no **8,3% inferior** do
  próprio range, não nos "6,00 pontos / 14%" descritos ontem. Um fechamento tão perto da
  mínima, depois de uma nova máxima da janela no dia anterior, é um sinal técnico de
  reversão/distribuição ainda mais nítido do que o já registrado ontem. O volume da sessão
  foi de **162.475 contratos** (CME CBOT) — este número, por si, não tem uma base de
  comparação confiável no dump para calcular variação percentual frente a 10/09 (a linha
  bruta de volume de soja de 10/09 não está presente nesta janela), então esta leitura não
  reafirma a comparação "+62,3% sobre ontem" feita na véspera — ver Honestidade.
- **Crush margin segue comprimido, com pequena melhora.** Fechou em **US$2,2755/bushel**
  em 11/09 (indicators), ainda **-8,98%** abaixo do referencial de US$2,50 monitorado pela
  fila (`alerta-quebra_suporte-complexo_soja-2026-09-11`, que arredonda para "2.28") — a
  11ª sessão seguida abaixo do referencial, com a distância encolhendo frente aos -9,97%
  de 10/09.
- **Nível técnico a vigiar:** um fechamento de volta abaixo de 1.180 ainda desfaria
  formalmente o rompimento; com a folga em 9,87%, esse cenário segue distante.
- **O COT mais fresco (08/09) tem agora cinco dias corridos de defasagem** frente à sessão
  de 11/09 — não há como saber se os fundos que ampliaram a posição comprada já começaram
  a vender, o que seria consistente com o padrão técnico de reversão observado.

**Leitura operacional:** para quem está comprado, a tendência de fundo (rompimento de
agosto, folga de ~10%, fundos institucionalmente mais comprados segundo o COT de 08/09)
ainda não foi desfeita, mas o padrão técnico da sessão de 11/09 — agora confirmado como
ainda mais extremo do que se pensava — é motivo genuíno para reduzir tamanho de posição ou
apertar stop. Para quem opera o lado vendido, a próxima sessão de negociação (segunda-feira
14/09, a primeira depois do fim de semana) é o teste mais imediato: uma continuação da
queda confirmaria o padrão de reversão, justificando uma posição tática vendida com stop
acima de 1.335,25; uma recuperação rápida sugeriria realização de lucro pontual, não o
início de uma correção maior.

## Farelo

**Viés: neutro (mantido de ontem) — o ratio Far/Soj ainda fecha acima de 80% pela primeira
vez desde a abertura da tese de abundância em 11/06/2026, mas por uma margem mais estreita
do que a leitura de ontem descreveu em quase todos os indicadores de apoio. O evento é
real (a própria fila confirma a mudança de zona), mas mais marginal do que se pensava —
suficiente para manter "neutro, sob teste", não para reforçar a convicção nessa mudança.**

O que sustenta a virada (ou pelo menos suspende a tese anterior):

- **O ratio Far/Soj cruzou para cima de 80% — mas por 0,25 ponto percentual, não 0,32.**
  Fechou em **80,25%** em 11/09/2026 (indicators), ante 78,95% em 10/09 — um salto de
  **+1,30 ponto percentual** (não +1,37 como descrito ontem). A fila de julgamento
  capturou o evento como `ratio-zona-2026-09-11`, descrevendo a transição de zona
  "comprimido" (<80%, farelo abundante) para "neutro" (80-87%). O mecanismo: quando os
  três produtos caem juntos mas o farelo cai bem menos (-1,08% vs -2,68% da soja), o
  numerador do ratio perde menos valor do que o denominador, e o ratio sobe mesmo com o
  farelo em queda nominal.
- **Os índices sintéticos ISF e ISO se moveram na mesma direção do ratio — isso não mudou
  com a correção.** ISF caiu de 80 para **60** (indicators, 11/09) e ISO caiu de 100 para
  **80** — a primeira mudança em quatro sessões em ambos, exatamente como descrito ontem.
  Estas duas métricas são as únicas que batem integralmente entre a leitura de ontem e os
  números corrigidos hoje.
- **O oil-meal spread virou negativo — mas por uma margem quase inexistente.** Fechou em
  **-0,0187** USD/bushel em 11/09 (indicators), ante +0,1419 em 10/09 — ainda a primeira
  leitura negativa da janela, mas -0,0187 é uma diferença muito pequena entre óleo e
  farelo dentro do crush (não os -0,0495 descritos ontem, quase três vezes maior). Na
  prática, óleo e farelo terminaram a sessão de 11/09 quase empatados em valor relativo
  dentro do crush, não com o farelo "vencendo com folga" como a leitura de ontem sugeriu.
- **O oil share caiu abaixo de 50% — mas por uma margem de apenas 0,06 ponto
  percentual.** Fechou em **49,94%** em 11/09 (indicators), ante 50,46% em 10/09 — a
  primeira leitura abaixo de 50% da janela, mas tecnicamente quase um empate (o farelo
  responde por 50,06% do valor do crush, não 50,16% como calculado ontem).
- **O físico brasileiro segue completamente congelado.** A última leitura disponível
  continua sendo 09/09 (farelo MT/IMEA R$1.875,45/ton, congelado desde 04/09; prêmio
  export Paranaguá +0,12 USD/short ton, congelado desde 27/08, agora **17 dias corridos**
  até hoje 13/09). O mercado físico doméstico ainda não teve qualquer chance de precificar
  a mudança de regime sugerida pelos indicadores de Chicago.

**Trata a fila `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
(recorrente 🔴) e `-D+90` (recorrente 🔴):** ambos seguem tecnicamente "vencidos" no
sistema de fila. O D+90 foi tratado em profundidade em
[[2026-09-09_d90-ratio-far-soj-reverte-na-vespera]] (concluindo "não invalidada") e o
gatilho de invalidação daquele próprio veredito foi revisitado em
[[2026-09-12_ratio-far-soj-rompe-80-pela-primeira-vez]] (concluindo "disparou
tecnicamente, mas insuficiente para inverter a tese — rebaixar para neutro"). Esta leitura
mantém essa classificação, com a ressalva de que a margem de evidência é mais estreita do
que aquele insight descreveu — ver
[[2026-09-13_correcao-numeros-sessao-11set-farelo-oleo]] para o detalhe completo da
correção.

**O que ainda pesa contra tratar isso como confirmado — e mantém o viés em "neutro", não
"bull-farelo":**

- **É um único dia de dado fresco, e agora envelhecido por dois dias sem pregão.** O
  padrão desta mesma janela mostrou pelo menos duas aproximações de 80% (79,76% em 04/09,
  79,08%/79,06% em 09/09) que foram revertidas na sessão seguinte. A diferença desta vez é
  que o ratio fechou **acima**, mas por uma margem (0,25 p.p.) que é, proporcionalmente,
  menor do que a distância que separou as aproximações anteriores do próprio nível de 80%.
- **O COT mais fresco (08/09) tem cinco dias corridos de defasagem e mostra sinal misto.**
  O net long de managed money em farelo ficou praticamente estável (+0,32%), mas via
  cobertura de posição vendida (short -26,73%), não via long novo (-2,86%) — uma leitura
  mais fraca de convicção compradora nova do que seria um net long crescendo por entrada
  de long.
- **O WASDE de setembro trouxe uma revisão estrutural na direção oposta, ainda que
  pequena.** Exportação de farelo argentino 2026/27 revisada de 2,89 para **2,99 milhões
  de toneladas** (USDA WASDE, edição de setembro vs agosto) — mais oferta exportável do
  segundo maior exportador mundial de farelo é um vetor baixista estrutural de médio
  prazo, oposto ao sinal de preço de curto prazo. Para o Brasil, produção/exportação/
  esmagamento de farelo seguem praticamente inalterados (8,0 / 0,2 / 7,1 milhões de
  toneladas). Esta janela do dump segue sem tabelas de soja em grão nem de óleo do WASDE
  de setembro.
- **O físico brasileiro não confirmou nada** (ver acima).

**Leitura operacional:** para quem está vendido em farelo (ou no spread Far/Soj vendido),
o gatilho de invalidação definido desde junho tecnicamente ocorreu, mas a margem de
evidência de apoio (ratio +1,30 p.p., oil share -0,06 p.p., oil-meal spread -0,0187) é
mais estreita do que parecia ontem — reforça a recomendação de reduzir tamanho, não de
fechar a posição às cegas, e de esperar por um segundo fechamento consecutivo acima de 80%
como confirmação mais robusta. Para quem está comprado em farelo ou no spread, a sessão de
11/09 segue sendo a primeira confirmação de preço e estrutura a favor da posição desde a
reabertura, mas por uma margem pequena o bastante para não apostar tamanho maior sem o
apoio do físico brasileiro ou de um COT contemporâneo.

## Óleo

**Viés: bear, moderado (rebaixado de "moderado a forte") — o preço caiu com força e o
fechamento ficou ainda mais perto da mínima do dia do que se pensava, mas o achado mais
importante desta leitura é que a margem de biodiesel americana não recuou: bateu recorde
da janela. Essa divergência entre preço (bearish) e fundamento de demanda via biodiesel
(bullish) é motivo suficiente para reduzir a convicção do viés baixista, sem invertê-lo.**

O que pesa contra a tese (o lado do preço e da estrutura de crush):

- **Queda forte, com fechamento ainda mais perto do piso do range do que o descrito
  ontem.** Óleo CBOT fechou em **69,19** USD cts/lb em 11/09/2026 (CME CBOT), **-3,11%**
  sobre os 71,41 de 10/09 — confirmado pela própria fila de julgamento
  (`alerta-movimento_forte-oleo_cbot-2026-09-11`, citando exatamente "-3.11% ... de 71.41
  para 69.19"). O contrato negociou entre 69,05 e 71,72 (amplitude de 2,67 pontos) e
  fechou a apenas **0,14** acima da mínima do dia — 5,2% do range a partir do fundo, um
  fechamento no piso absoluto. A fila também confirma a quebra do suporte de 72,00
  (`alerta-quebra_suporte-oleo_cbot-2026-09-11`), com a distância agora em **-3,90%**.
- **O Índice de Suporte do Óleo (ISO) recuou do teto da escala pela primeira vez em quatro
  sessões.** Caiu de **100 para 80** (indicators, 11/09) — ainda um nível historicamente
  alto, mas a leitura é de enfraquecimento da força estrutural do óleo dentro do crush,
  não de reversão completa.
- **Oil share e oil-meal spread confirmam perda de força relativa do óleo — por margem
  pequena.** Oil share caiu de 50,46% para **49,94%** (a 0,06 p.p. do empate). Oil-meal
  spread virou de +0,1419 para **-0,0187** USD/bushel (perto de zero, não um sinal forte).
  Ver seção Farelo para o detalhe — a mensagem aqui é a mesma, espelhada: o óleo perdeu a
  primeira posição dentro do crush pela primeira vez na janela, mas por uma margem
  estreita.

**O que sustenta um piso genuíno para a tese — a divergência mais importante do dia:**

- **A margem de biodiesel americana não recuou: bateu o recorde da janela.** Fechou em
  **US$2,135/galão** (indicators, 11/09), uma alta de **+3,30%** sobre os US$2,0667 de
  10/09 — a terceira alta diária consecutiva e o valor mais alto visível em toda a janela
  do dump (acima de 04/09: 1,7385; 08/09: 1,6663; 09/09: 1,91; 10/09: 2,0667). O mecanismo:
  o custo do óleo como insumo do biodiesel caiu para **US$5,1893/galão** (7,5 lb ×
  69,19 cts/lb), uma queda de -3,11% em linha com a própria queda do óleo em Chicago — e
  como óleo é **custo**, não receita, para o produtor de biodiesel, um óleo mais barato
  **melhora** a margem. A receita modelada caiu bem menos (-1,19%, para US$8,1243/galão)
  do que o custo, e o resultado líquido foi margem melhor, não pior — o oposto exato do
  que a leitura de ontem descreveu (que apontava um colapso do heating oil derrubando a
  margem em -5,11%; ver
  [[2026-09-13_correcao-numeros-sessao-11set-farelo-oleo]] para a auditoria completa desse
  erro). O heating oil (CME NYMEX, HO=F) de fato fechou em **4,9593** USD/galão em 11/09
  — um dado direto e sourced, sem qualquer evidência no dump de um "colapso" de -7% como
  descrito ontem.
- **Isso é uma divergência real entre preço e fundamento, não um detalhe técnico.** O óleo
  caiu -3,11% em Chicago no mesmo dia em que a economia do biodiesel americano — um dos
  seus principais canais de demanda estrutural — melhorou para o melhor nível da janela.
  Isso sugere que a queda de preço de 11/09 foi dirigida por outra coisa (posicionamento
  técnico, realização de lucro depois da forte alta de 10/09, ou pressão vendedora ligada
  à queda geral do complexo) e não por uma deterioração de fundamento de demanda — o que
  reduz a convicção de que esta seja o início de uma tendência baixista mais duradoura, e
  é o principal motivo desta leitura para rebaixar o viés de "moderado a forte" para
  "moderado".
- **A curva futura de médio prazo do óleo segue precificando um patamar acima do contrato
  próximo.** Set/26 69,01 → out/26 (base) 69,19 → dez/26 69,68 → jan/27 69,99 → mar/27
  70,19 → mai/27 70,24 (CME CBOT, 11/09) — os contratos mais distantes seguem acima do
  contrato-base, sugerindo que o mercado futuro trata a queda de hoje como algo a ser
  parcialmente recuperado no médio prazo.
- **O RIN D4 (crédito de biocombustível renovável americano) segue estável**, sem
  novidade regulatória nesta janela.
- **O COT de 08/09 já mostrava os fundos reduzindo exposição líquida ao óleo antes desta
  queda** (net long -8,13%, CFTC COT), o que significa que parte do ajuste de
  posicionamento já estava em curso antes da sessão de 11/09.

**Leitura operacional:** para quem está vendido em óleo direcional, o preço e a estrutura
técnica (fechamento no piso do range, quebra de suporte, ISO recuando) seguem dando
suporte à posição, mas a divergência com a margem de biodiesel (em recorde da janela)
é um argumento genuíno para não aumentar tamanho e vigiar de perto uma possível
recuperação técnica — se o mercado começar a precificar a melhora de margem, o
movimento pode reverter rápido. Para quem está comprado em óleo direcional, a tese ganhou
um argumento fundamentalista real hoje (biodiesel em máxima da janela) que não existia na
leitura de ontem, ainda que o preço e a técnica sigam contra a posição no curtíssimo
prazo. Para quem opera o spread farelo-óleo dentro do crush, a sessão de 11/09 foi
favorável ao farelo por uma margem pequena — não a vitória folgada descrita ontem — o que
sugere um spread mais equilibrado do que extremo, e portanto menos atrativo para abrir
posição nova nesse spread neste momento específico.

## Spreads e crush (leitura de complexo)

A sessão de 11/09 foi a primeira, desde a reabertura, em que os três produtos do complexo
caíram juntos — mas, como em toda leitura de complexo, o que importa é a velocidade
relativa. Com os números corrigidos: farelo -1,08%, soja -2,68%, óleo -3,11% (CME CBOT,
11/09) — a ordem de queda (óleo > soja > farelo, em módulo) é a mesma reportada ontem, mas
as magnitudes mudam a leitura fina de "quem ganhou a rodada": o farelo caiu bem menos que
os outros dois, mas a distância entre farelo e soja (1,60 p.p.) é menor do que a distância
entre soja e óleo (0,43 p.p.), o que já indica que o movimento dentro do crush (farelo vs
óleo) foi mais estreito do que a queda direcional do complexo como um todo. O resultado
agregado: ratio Far/Soj **80,25%** (+1,30 p.p., primeiro fechamento acima de 80% desde
11/06/2026), oil share **49,94%** (primeira leitura abaixo de 50% da janela, por margem
mínima), oil-meal spread **-0,0187** USD/bushel (primeira leitura negativa da janela, mas
próxima de zero), ISF **60/100** (caindo de 80) e ISO **80/100** (caindo de 100). Cinco
indicadores diferentes, calculados de formas distintas a partir dos mesmos três preços,
todos se movendo na mesma direção no mesmo dia — isso continua sendo uma coincidência
estrutural que merece peso, mas as margens de cada um são mais estreitas do que a leitura
de ontem descreveu, e isso deve moderar a confiança no "farelo vencendo com folga" sem
descartar o evento em si.

O crush margin fechou em **US$2,2755/bushel** (11/09, indicators), uma alta de +1,32%
sobre 10/09, e segue a 11ª sessão consecutiva abaixo do referencial de US$2,50 monitorado
pela fila (`alerta-quebra_suporte-complexo_soja-2026-09-11`, que arredonda para "2.28"),
com a distância percentual encolhendo de -9,97% para -8,98%.

O COT de 08/09 (cinco dias corridos de defasagem frente à sessão analisada) segue sendo o
único retrato de posicionamento disponível: fundos ampliando fortemente a convicção
compradora em soja (net long +9,51%, com long subindo mais que short — dinheiro novo),
reduzindo a convicção compradora em óleo (net long -8,13%, com short subindo +17,14% —
cautela crescente já visível antes da queda de 11/09) e mantendo o net long em farelo
praticamente estável via cobertura de posição vendida, não via long novo. O próximo corte
(posições de 15/09, esperado por volta de 18/09) é o primeiro que poderá dizer se os
fundos reagiram à sessão de 11/09 de fato.

Do lado dos fundamentos brasileiros de médio prazo (ABIOVE, sem revisão nesta janela), o
balanço projetado mostra o esvaziamento sazonal esperado: estoque final de soja recuando
de 7.912 mil toneladas (set/26) para 1.890 mil toneladas (dez/26), produção de farelo
caindo de 2.129 para 1.659 mil toneladas no mesmo período, exportação de farelo recuando
de 1.100 para 700 mil toneladas — uma trajetória que tende a aliviar a oferta doméstica de
farelo ao longo do próximo trimestre, um vetor de médio prazo que **não** aponta na mesma
direção que o cruzamento do ratio acima de 80% de curto prazo (que seria mais consistente
com farelo ficando mais escasso/caro). Essa tensão entre o dado de preço de curto prazo e
a trajetória de balanço da ABIOVE segue sem resolução — mais um motivo para não superestimar
a força do sinal de 11/09, já que suas margens de apoio são mais estreitas do que se pensava.

## Lente fiscal/regulatória BR

Antes de fechar qualquer tese de preço BR, os vetores tributários/regulatórios vivos que
pesam no complexo — todos do `system/tributario_watch.toml`, cujo carimbo mais recente
(`atualizado_em`) em todos os 10 eventos catalogados é 2026-06-05, ou seja, **100 dias
corridos sem revisão humana** frente a hoje (13/09) — um marco redondo que reforça a
necessidade de checar esse arquivo manualmente em algum momento próximo:

- **MP 1.363/2026** (id `MP-1363-2026`, subvenção diesel fóssil R$1,12/L, vigente até
  31/12/2026): barateia o diesel fóssil no mix B15 (mistura obrigatória de 15% de
  biodiesel), reduzindo a competitividade relativa do biodiesel e a demanda doméstica por
  óleo de soja — vetor estrutural de baixa para óleo, sem mudança de status. Este vetor
  reforça o viés bear-óleo por um mecanismo regulatório doméstico completamente diferente
  da divergência preço-vs-margem observada em Chicago hoje — os dois vetores (BR
  regulatório e US biodiesel) apontam, neste momento, em direções opostas para o óleo: o
  BR pressiona a demanda doméstica para baixo, enquanto a economia de biodiesel americana
  melhora. É um lembrete de que "o óleo" é, na verdade, dois mercados de demanda distintos
  (biodiesel BR e biodiesel US) que nem sempre se movem juntos.
- **B16 (id `B16-CNPE-2026`, elevação da mistura obrigatória de biodiesel para 16%)**
  segue "adiado", resultado esperado por volta de novembro/2026. Upside represado (~436
  mil toneladas de demanda potencial adicional de óleo), não corrente.
- **Isenção de PIS/Cofins do biodiesel na mistura** (id `PISCOFINS-BIODIESEL-ISENCAO`):
  vigência registrada até 31/07/2026 — já **44 dias corridos vencida** frente a
  13/09/2026, sem registro de prorrogação ou expiração.
- **MP 1.358/2026** (subvenção gasolina R$0,89/L): vigência registrada até 11/07/2026,
  agora **64 dias corridos vencida**.
- **STJ REsp 2.165.276** (id `STJ-RESP-2165276`, crédito de PIS/Cofins sobre soja em
  biodiesel, direção "alta" para soja/óleo): sem novidade nesta janela.
- **EPA RFS 2026/2027** (id `EPA-RFS-2026-2027`, mandato de biocombustível americano,
  vigente desde 15/06/2026, direção "alta" para óleo): sustenta o RIN D4, estável — o
  arcabouço regulatório segue intacto, consistente com a melhora de margem de biodiesel
  observada hoje.
- **Crédito 45Z** (id `45Z-CLEAN-FUEL`, em tramitação, direção "mista"): sem novidade.
- **Indonésia — Danantara** (id `DANANTARA-INDONESIA`) e **levy de exportação PMK
  9/2026** (id `INDONESIA-LEVY-PMK9`): a assunção plena da centralização da exportação de
  palma pela Indonésia tinha alvo 01/09/2026 — já se passaram **12 dias** sem confirmação.
  Catalisador de alta represado para óleo (via substituição com palma).
- **Indonésia B50** (id `INDONESIA-B50`, monitorando, direção "alta"): sem novidade.

## Riscos e eventos próximos

- **A sessão de segunda-feira 14/09** é o primeiro pregão desde a reversão de 11/09 e o
  teste mais imediato de continuidade (ou não) do sinal técnico de reversão em soja e
  óleo. Uma continuação da queda em ambos confirmaria o padrão; uma recuperação rápida
  sugeriria realização de lucro pontual.
- **Confirmação (ou não) de um segundo fechamento acima de 80% no ratio Far/Soj** — dado
  que a margem de apoio (0,25 p.p.) é estreita, uma reversão de volta para baixo de 80% na
  próxima sessão é um cenário plausível, não descartável.
- **O COT de 08/09 está cinco dias corridos atrasado frente ao preço** — o próximo corte
  (posições de 15/09, esperado por volta de 18/09) é o primeiro que poderá confirmar
  reação dos fundos.
- **Reação (ou ausência) do físico brasileiro de farelo e óleo**, congelado desde 09/09
  (farelo, 4 dias) e 27/08 (prêmios export, 17 dias).
- **Se a margem de biodiesel americana continuar em máxima da janela**, isso é um
  argumento crescente contra a continuidade da queda do óleo em Chicago — vigiar se o
  mercado começa a precificar essa divergência.
- **USDA Crop Progress semanal**: próximo corte esperado amanhã, segunda-feira 14/09.
- **USDA WASDE de setembro**: ainda incompleto nesta janela (só farelo Argentina/Brasil) —
  monitorar se as tabelas de soja em grão, óleo e EUA aparecem nos próximos dias.
- **NOPA mensal** (`release-nopa-2026-09-12`): sexto dia seguido do mesmo falso positivo
  de paywall na fila.
- **Confirmação da centralização plena da exportação de palma pela Danantara** — alvo
  01/09, já 12 dias passados.
- **Vigência da isenção PIS/Cofins do biodiesel** (44 dias vencida) e **MP 1.358/2026 da
  gasolina** (64 dias vencida) — checar notícia de renovação/expiração.
- **Clima**: previsão de 13/09 (hoje) mostra resfriamento e aumento de nebulosidade/chuva
  frente à véspera em praticamente todos os pontos monitorados, tanto no núcleo produtor
  de Mato Grosso (Cuiabá 32°C/24°C, ante 37°C/27°C ontem) quanto no Sul (Cascavel 19°C/13°C,
  ante 29°C/17°C; Passo Fundo 16°C/9°C, sem menção de geada) — pano de fundo para a janela
  de plantio da safra 2026/27 que se aproxima, ainda sem impacto direto sobre soja em si
  (não plantada na região). Vale monitorar se o resfriamento no Sul evolui para risco de
  geada tardia nos próximos boletins.
- **Marco de 100 dias sem revisão humana do `tributario_watch.toml`** — momento oportuno
  para uma checagem manual dos 10 eventos catalogados, dado que ao menos dois (isenção
  PIS/Cofins biodiesel, MP 1.358/2026) já estão vencidos sem registro de renovação.

## Honestidade

- **A leitura de 12/09 usou números de fechamento, volume e heating oil que divergem dos
  presentes no dump de hoje para a mesma sessão de 11/09.** A auditoria completa,
  produto por produto e métrica por métrica, com as fontes que corroboram cada valor
  corrigido, está em
  [[2026-09-13_correcao-numeros-sessao-11set-farelo-oleo]]. Não é possível determinar, com
  os dados disponíveis, se a causa foi uma revisão upstream do dado entre a geração dos
  dois dumps ou um erro de leitura anterior — esta leitura usa os valores do dump de hoje
  por serem corroborados independentemente pela fila de julgamento (autogerada a partir do
  banco, não escrita por este analista) e por serem internamente consistentes entre si
  (ex.: margem de biodiesel = receita - custo_óleo - custo industrial fecha exatamente).
- **O volume de negociação da soja em 10/09 não está disponível nesta janela do dump**,
  então esta leitura não reafirma a comparação "volume +62,3% sobre o dia anterior" feita
  pela leitura de 12/09 — não há como verificar essa conta com os dados hoje disponíveis.
- **O dump de hoje não contém as linhas brutas de CME CBOT para soja e óleo na data de
  10/09** (mesmo gap identificado nas leituras anteriores) — os valores de soja (1.332,25)
  e óleo (71,41) usados como base de comparação vêm das fórmulas dos indicadores
  sintéticos de 10/09, não de uma linha de preço bruta própria daquele dia.
- **O dump de hoje também não contém fechamento/máxima/mínima/volume de heating oil para
  10/09** (apenas a abertura, 4,7964 USD/galão) — não é possível calcular a variação
  percentual do heating oil entre 10/09 e 11/09 com uma base de fechamento própria; esta
  leitura cita apenas o fechamento de 11/09 (4,9593) como fato isolado, sourced
  diretamente da linha bruta CME NYMEX.
- **O WASDE de setembro (`release-usda_wasde-2026-09-11`) está incompleto nesta janela do
  dump** — apenas farelo (Argentina, Brasil parcial, China parcial), sem soja em grão, óleo
  de soja, nem dados dos EUA.
- **O COT de 08/09 tem agora cinco dias corridos de defasagem** frente à sessão de 11/09 —
  não há como confirmar se a posição dos fundos mudou em resposta à reversão de preço.
  Próximo corte esperado por volta de 18/09.
- **Percentil histórico de posicionamento COT não está disponível no briefing** — toda
  leitura de "fundos comprando/vendendo" usa variação semana a semana de contratos
  absolutos, não percentil histórico.
- **`tributario_watch.toml` sem atualização há 100 dias corridos** — pelo menos dois
  vetores (isenção PIS/Cofins do biodiesel, MP 1.358/2026) já passaram da vigência
  registrada sem nota de renovação ou expiração. Tratados como "status desconhecido
  pós-vigência".
- **NOPA segue inacessível** (paywall) — sexta "release" seguida sem dado novo de fato.
- **A ausência de itens de notícia em 10, 11 e 12/09 ("0 items lidos, 0 mantidos")** é
  registrada como falha ou pausa de coleta da fonte RSS, não como ausência real de notícia
  relevante no mercado.
- **A previsão INMET para 13/09 é previsão meteorológica, não medição de precipitação
  real** — a ausência de menção a "geada" no boletim de hoje para Passo Fundo/RS é
  indicativa, não confirmação de que o risco de geada tardia está afastado.
- **Prêmios de exportação (Paranaguá) e o físico de farelo/soja BR seguem sem atualização
  própria desde 09/09** (4 dias corridos) — não é possível afirmar se isso reflete mercado
  físico genuinamente parado ou apenas defasagem normal de publicação.
- **MPOB (palma Malásia) segue com parser quebrado** — nenhum dado de produção/estoque de
  palma malaia disponível.
- **BCBA (Argentina) segue sem links de relatório detectados** — nenhum dado de safra ou
  exportação argentina disponível.
- **Os forecasts estatísticos internos (bandas 7d/30d) foram gerados sobre o fechamento de
  11/09**, com viés "altista" atribuído aos três produtos — isso reflete extrapolação
  estatística de tendência recente (MA20 + volatilidade + slope), não uma reavaliação
  fundamentalista da reversão de 11/09 nem da divergência preço-margem do óleo discutida
  nesta leitura; tratado aqui como referência estatística, não como leitura própria desta
  análise.
- **A fila de julgamento continua listando os dois itens de revisão do ratio Far/Soj (D+7
  e D+90) como "vencidos"**, mesmo com o D+90 já tratado em profundidade em 09/09 e
  revisitado em 12/09 — aparenta ser, como observado em leituras anteriores, um eco do
  sistema de geração de fila que não lê de volta os insights já escritos para marcar a
  revisão como encerrada.
