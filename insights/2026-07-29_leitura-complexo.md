---
data: 2026-07-29
titulo: "Quarta-feira de reversão ampla: a soja despenca -2,49% (1.174,75, CBOT 2026-07-29) e rompe de forma decisiva o piso técnico de 1.180,00 que havia resistido a todos os testes da semana passada, fechando praticamente na mínima do dia (3,4% do range) — arrastando farelo (-0,87%) e óleo (-2,12%), mas como a soja caiu proporcionalmente mais rápido que a soma farelo+óleo, a crush margin na verdade MELHOROU (+2,72%, para 2,8110 USD/bu) e o ratio Farelo/Soja saltou de volta para 81,34% (de 80,01% revisado ontem), devolvendo em uma única sessão o rompimento da zona 'comprimida' que a leitura de ontem havia tratado como confirmação tática da tese bear-farelo — enquanto o óleo estende a quebra do suporte de 72,00 pela terceira sessão seguida (68,65, mínima intradiária 68,50) mesmo com a margem de biodiesel americana disparando +14,58% para o maior nível desta janela (1,4385 USD/galão), e a isenção PIS/Cofins do biodiesel vence em apenas 2 dias sem qualquer sinalização de renovação"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT (ZSU26 soja / ZMU26 farelo / ZLU26 óleo) — sessão de 2026-07-29
  - CME heating_oil_cbot (HO=F) — sessão de 2026-07-29 (70 contratos, print anômalo — ver Honestidade)
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, paridade BR, Índice de Sobra de Farelo, Índice de Suporte do Óleo) — 2026-07-29, com a linha 2026-07-28 recalculada (soja 1.204,75 / farelo 321,30 / óleo 70,14, diferente dos valores citados na leitura de ontem — ver Honestidade)
  - BCB PTAX — 2026-07-29 (USD/BRL 5,1217, EUR/BRL 5,8305, Selic diária 0,052531% a.a.)
  - CEPEA/ESALQ Paranaguá via NAG — 2026-07-29 (suporte R$ 146,81/saca, var -0,73%)
  - CEPEA/ESALQ Paraná interior via NAG — 2026-07-29 (R$ 139,00/saca, var -0,73%)
  - NAG Físico BR (farelo MT/IMEA R$ 1.669,72/ton estável; Rondonópolis R$ 1.650,00/ton estável; RS R$ 1.640,00/ton estável; prêmios export PGUA farelo +0,05 USD/sht e óleo +0,08 cts/lb, ambos inalterados) — 2026-07-29
  - CFTC COT Managed Money — corte de 2026-07-21 (ainda o mais recente; próximo corte referente a 28/07, publicação normal ~31/07, agora a 2 dias)
  - USDA Crop Progress — ainda 2026-07-26 (11% excelente + 52% boa + 7% ruim), sem corte novo esta semana
  - USDA WASDE — ausente da janela de 14 dias deste briefing pelo segundo dia seguido (último dado 10/07/2026, agora 19 dias de atraso — ver Honestidade)
  - NOPA — fila `release-nopa-2026-07-29`, `monthly_status` continua em 0,0 bool (paywall), mesma barreira desde meados de junho
  - ABIOVE projeções mensais — balanços ago-dez/2026 (farelo/óleo/soja), sem alteração
  - NOAA CPC ENSO — 2026-07-29 (El Niño Advisory, inalterado desde pelo menos 15/07/2026)
  - MPOB — 2026-07-29 (20º dia consecutivo com o mesmo conteúdo exato de 3.439 caracteres, parser sem números extraídos)
  - BCBA Argentina — 2026-07-22 (7 dias sem atualização)
  - Notícias Agrícolas/Farm Progress RSS — 2026-07-29 (160 itens lidos, 8 mantidos; manchete "Why we shouldn't rule out a record soybean crop", farmprogress.com, sem conteúdo quantitativo)
  - Forecasts estatísticos internos — 2026-07-29 (spot ref já reflete o fechamento de hoje: soja 1.174,75 / farelo 318,50 / óleo 68,65; viés "altista" nas três, em clara defasagem frente ao tombo do dia — ver Honestidade)
  - system/tributario_watch.toml (lido apenas como referência, não editado) — 10 eventos, `atualizado_em` 2026-06-05 (55 dias sem atualização); trata `trib-PISCOFINS-BIODIESEL-ISENCAO-2026-07-31`
  - Cruza com [[2026-07-28_leitura-complexo]] (cuja leitura central é parcialmente corrigida aqui), [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (D+7 reaberto e ainda não confirmado — ver abaixo)
status: ativa
vies: [bear-soja, neutral-farelo, bear-oleo_soja]
---

## Visão geral

O complexo soja é uma fábrica com uma única matéria-prima (a soja em grão) e
dois produtos de saída em proporção fixa por bushel esmagado: o **farelo**
(fração proteica, ~78% da massa, vira ração animal) e o **óleo degomado**
(fração de gordura, ~18-20% da massa, vira óleo de cozinha e biodiesel). Quem
decide o ritmo de esmagamento é a esmagadora, olhando a **crush margin**
(valor de farelo + óleo por bushel, menos o custo daquele bushel de soja,
medido na CBOT — Chicago Board of Trade, a bolsa de referência mundial para
esses contratos) e o **oil share** (fração desse valor capturada pelo óleo).
O **ratio Far/Soj** (preço do farelo dividido pelo preço da soja, normalizado
pela conversão bushel↔short ton) mede o mesmo crush por outro ângulo:
abaixo de 80% o farelo está historicamente "abundante" frente à soja (zona
bear); acima de 87%, "apertado" (zona bull); entre os dois, zona neutra de
**mean-reversion** (opera nos dois lados do book). Um detalhe crucial para
ler o dia de hoje: a crush margin e o ratio Far/Soj **não se movem sempre na
mesma direção** — o ratio compara farelo com soja, a crush margin compara a
soma farelo+óleo com a soja; quando as três pernas caem juntas, mas em
proporções diferentes, os dois indicadores podem apontar para lados opostos,
exatamente o que aconteceu hoje.

**A sessão de hoje foi de tombo generalizado, mas desigual entre as pernas —
e é essa desigualdade, não a direção comum, que conta a história.** A soja
despencou -2,49% (1.174,75 cts/bushel, CBOT, ante 1.204,75 no fechamento
recalculado de ontem), o farelo caiu -0,87% (318,50 USD/short ton, ante
321,30) e o óleo caiu -2,12% (68,65 cts/lb, ante 70,14). A soja liderou a
queda por larga margem — quase três vezes a queda percentual do farelo — e
isso tem duas consequências que parecem contraditórias, mas não são. Primeiro,
como o **ratio** compara farelo (que caiu pouco) com soja (que caiu muito), o
ratio **subiu**, voltando a 81,34% e saindo da zona "comprimida" que a leitura
de ontem havia declarado rompida. Segundo, como a **crush margin** compara o
custo (soja, que caiu muito) com a receita combinada (farelo+óleo, que caiu
menos em termos absolutos), a crush margin **melhorou**, para 2,8110 USD/bu
(+2,72%), interrompendo a sequência de seis quedas seguidas documentada
ontem. **O evento técnico mais relevante do dia foi a soja rompendo, de
forma decisiva e com fechamento fraco (perto da mínima), o nível de
1.180,00** que resistiu a todos os testes da última semana — um
desenvolvimento que a fila de julgamento de hoje, curiosamente, não sinalizou
como alerta de nível técnico (só o óleo recebeu esse alerta hoje; ver
Honestidade). **Leitura de uma linha:** o pivô do complexo hoje é a soja, que
rompeu seu piso técnico com o pior fechamento relativo das três pernas e
arrastou o resto do complexo; a maior convicção desta leitura é que o
rompimento de 1.180,00 é o desenvolvimento mais acionável do dia (soja vira
tática bear); confiança moderada-alta para soja e óleo (ambos com quebras
técnicas + fechamento perto da mínima), e confiança baixa para uma leitura
direcional única em farelo — o ratio devolveu o rompimento de ontem em uma
única sessão, o que exige cautela redobrada sobre qualquer veredito tático
recente neste indicador (ver correção abaixo).

---

## Soja

**Viés: bear tático — a soja fechou 1.174,75 cts/bushel (CBOT, ticker
ZSU26.CBT, -2,49% sobre o fechamento recalculado de ontem de 1.204,75),
rompendo de forma decisiva o nível técnico de 1.180,00 que vinha sendo o
pivô mais vigiado desta série de leituras havia mais de uma semana, com
fechamento a apenas 3,4% do range do dia acima da mínima — um padrão de
fechamento muito fraco.** Nenhum item da fila de julgamento de hoje citou
explicitamente este rompimento (só o óleo recebeu alerta de nível técnico
hoje) — esta leitura o trata como o desenvolvimento mais relevante da sessão
de qualquer forma, por julgamento próprio, dado o tamanho do movimento e a
posição do fechamento dentro do range.

### O que sustenta a tese

**A sessão foi de abertura em alta seguida de venda contínua até o
fechamento — um padrão técnico clássico de reversão.** Abertura 1.207,00
(+0,19% sobre o fechamento de ontem — um gap positivo, sugerindo que o
mercado começou o dia sem sinal de fraqueza), máxima 1.209,75 (tocada logo
no início e nunca mais revisitada), mínima 1.173,50 (um novo patamar,
1,25 cts abaixo do fechamento) e fechamento em 1.174,75. **Mecanismo e
leitura:** o range do dia foi de 36,25 cts (1.209,75-1.173,50); o
fechamento ficou a apenas 1,25 cts acima da mínima, ou seja, em **3,4% do
range** — o contrato abriu perto da máxima do dia e foi vendido de forma
praticamente ininterrupta até fechar colado na mínima. Esse é o padrão
inverso do observado em 27/07 e 28/07 (fechamentos no terço ou meio superior
do range, indicando "compra na fraqueza"); hoje não houve recompra
perceptível — o vendedor dominou a sessão inteira. O volume foi de 36.260
contratos; este briefing não traz, na janela consultada, o volume de
soja de 27/07 nem de 28/07 (a tabela `cme_cbot` desta consulta, assim como
a de ontem, não chega às linhas de soja e óleo dessas duas datas — ver
Honestidade), então esta leitura não pode dizer se o volume de hoje veio
acima ou abaixo do das últimas sessões, apenas registrar o nível absoluto.

**O nível técnico de 1.180,00 — o pivô mais vigiado desta série de leituras
desde meados de julho — foi rompido hoje de forma inequívoca, tanto na
mínima quanto no fechamento.** A mínima de ontem (1.193,00) havia chegado a
apenas 1,10% de distância do nível sem tocá-lo; hoje a mínima (1.173,50)
ficou **0,55% ABAIXO** dele ((1.173,50-1.180,00)÷1.180,00), e o fechamento
(1.174,75) também fechou **0,44% abaixo** — o primeiro fechamento desta
janela observada abaixo do nível. **Isso inverte o quadro técnico descrito
na leitura de ontem**, que via a soja "consolidando tática de alta" acima da
resistência pelo segundo dia seguido, com a distância "aumentando, não
diminuindo". Hoje a distância não apenas diminuiu — o preço atravessou o
nível por completo, com folga, e fechou do lado errado dele. Um piso que
resistiu a múltiplos testes ao longo de mais de uma semana (as leituras
recentes documentaram testes em 27/07 e 28/07 sem rompimento) cedeu numa
única sessão de -2,49%.

**O câmbio, ao contrário do papel, trabalhou hoje a FAVOR da soja em reais —
mas não o suficiente para compensar o tombo do CBOT.** USD/BRL PTAX fechou
em 5,1217 (BCB, 2026-07-29), alta de +0,08% sobre 5,1177 de ontem — a quinta
alta seguida do dólar desde a mínima local de 5,0638 em 22/07, ainda que o
ritmo de alta tenha desacelerado bastante frente às sessões anteriores (que
chegaram a +0,34%). **Mecanismo:** a paridade teórica em reais (CBOT
convertido pelo câmbio, sem considerar basis/frete/ágio local) é
`preço CBOT em cts × PTAX`; como o CBOT caiu -2,49% e o câmbio subiu apenas
+0,08%, os dois efeitos quase não se cancelam — a paridade calculada
despencou para **R$ 132,64/saca** (indicators, 2026-07-29: CBOT 1.174,75
cts × USD/BRL 5,1217), ante R$ 135,93 em 28/07 (recalculado), uma queda de
**-2,42%** — praticamente todo o movimento veio do papel, o câmbio quase não
amorteceu a queda desta vez (diferente de ontem, quando os dois efeitos se
somaram na mesma direção; hoje eles vão em direções opostas, mas o câmbio é
pequeno demais para compensar).

**A base física em Paranaguá, em contraste marcante com o papel, quase não
se moveu — e isso alargou o prêmio de exportação para o maior nível desta
janela observada.** CEPEA/ESALQ Soja Paranaguá (via NAG) fechou em R$
146,81/saca hoje, queda de apenas -0,73% sobre R$ 147,89 de ontem — uma
fração pequena da queda de -2,42% da paridade teórica. Com a paridade caindo
para R$ 132,64, o **prêmio de exportação sobre a paridade saltou para
+10,68%** ((146,81-132,64)÷132,64), ante aproximadamente +8,80% no cálculo
equivalente de ontem (147,89 vs paridade 135,93) — um alargamento de quase 2
pontos percentuais em uma única sessão, o maior nível de prêmio desta janela
observada (que oscilou entre +7% e +9,7% nas leituras anteriores, chegando a
picos pontuais perto de +9,7%). **Mecanismo e leitura:** este é o dado mais
importante da sessão para quem opera basis físico — o mercado de exportação
em Paranaguá simplesmente não replicou o tombo do papel. Isso é consistente
com duas leituras possíveis, e esta análise não tem como distinguir qual
prevalece com os dados disponíveis: (a) a demanda física de exportação
continua excepcionalmente firme e desconectada do movimento especulativo do
papel, o que seria um sinal estrutural bullish para quem vende físico; ou
(b) o preço físico em Paranaguá simplesmente reage com atraso ao papel (é
atualizado uma vez ao dia, via CEPEA/ESALQ) e vai "alcançar" a queda do CBOT
na próxima atualização. O físico do Paraná interior também caiu pouco (R$
139,00/saca, -0,73%, coincidentemente a mesma variação percentual exata de
Paranaguá) — o que sugere que ambas as praças físicas estão, por ora,
absorvendo o choque do papel de forma bem mais moderada que o CBOT.

**A curva forward preservou a inversão de calendário no vencimento mais
próximo, mas com folga menor que ontem.** Agosto/26 (Q26) 1.177,00 →
Setembro/26 (U26, spot) 1.174,75 → Novembro/26 (X26) 1.191,50 → Janeiro/27
(F27) 1.205,75 → Março/27 (H27) 1.210,00. Agosto segue precificado ACIMA do
spot de setembro (+0,19%, ante +0,60% ontem) — a mesma pequena inversão
técnica de calendário observada nas últimas leituras, mas menos pronunciada
hoje, o que é esperado matematicamente: como o spot de setembro caiu -2,49%
enquanto agosto (mais próximo do vencimento, mais ancorado ao físico de
curtíssimo prazo) caiu menos em termos absolutos, a diferença percentual
entre os dois encolheu. Da parte de trás da curva em diante (U26→X26→F27→H27)
a forma de contango segue idêntica à documentada nos últimos dias — nenhum
sinal de estresse físico embutido além do já conhecido.

**Os forecasts estatísticos internos (2026-07-29)**, recalculados com o
fechamento de hoje (1.174,75), seguem etiquetados como "altista": central 7d
= 1.200,36 cts/bu (bandas 1.140,97-1.259,75); central 30d = 1.280,55 cts/bu
(bandas 1.157,60-1.403,49). **A defasagem deste modelo (média móvel de 20
dias + volatilidade + inclinação de curto prazo) nunca ficou tão evidente
nesta série de leituras quanto hoje** — o modelo aponta viés de alta no
mesmo dia em que a soja rompeu para baixo seu principal piso técnico com o
pior fechamento relativo das três pernas. Esta leitura trata o forecast
apenas como referência de banda estatística, não como argumento de tese (ver
Honestidade).

**A manchete do dia (Farm Progress, 29/07/2026, "Why we shouldn't rule out a
record soybean crop") carrega uma narrativa de oferta ampla, mas sem número
concreto atribuível a esta safra específica** — uma peça de opinião
levantando a possibilidade de safra recorde nos EUA, no mesmo tom de outras
manchetes recentes desta série ("Is a record soybean crop in the works?",
27/07). Não é um dado quantitativo citável, mas o padrão recorrente de
manchetes sobre "safra recorde" ao longo de julho é, em si, um sinal
qualitativo de que a narrativa de oferta ampla nos EUA vem ganhando espaço
editorial — coerente com (embora não prova de causalidade para) o tombo de
hoje.

### O que invalida / risco para a soja

- **Um fechamento de volta acima de 1.180,00** nas próximas sessões
  desfaria a leitura de rompimento — dado que o nível resistiu a múltiplos
  testes ao longo de mais de uma semana antes de ceder hoje, uma reversão
  rápida não pode ser descartada, especialmente se o tombo de hoje refletir
  mais um ajuste técnico pontual do que uma mudança de fundamento.
- **O próximo corte do COT (28/07, publicação ~31/07, agora a 2 dias)
  mostrar se os fundos, extremamente comprados na foto de 21/07 (net long
  +130.505 contratos, 12,49% do open interest), já começaram a liquidar** —
  um tombo de -2,49% com posição especulativa historicamente esticada é a
  configuração clássica de gatilho para liquidação forçada; se o corte
  mostrar isso já em curso, reforça a tese bear; se mostrar fundos ainda
  comprados, aumenta o risco de mais liquidação pela frente.
- **O prêmio de exportação em Paranaguá (agora +10,68%, o maior desta
  janela) comprimir na próxima atualização** — se o físico "alcançar" a
  queda do papel em vez de permanecer descolado, isso indicaria que a
  demanda física não estava, de fato, blindada contra o movimento de hoje.
- **O câmbio reverter a sequência de altas** (cinco dias seguidos desde
  22/07, embora desacelerando) — mais uma pressão altista sobre a paridade
  em reais desaparecendo se o USD/BRL cair.

### Leitura operacional — soja

O quadro de hoje é de **ruptura técnica com fechamento fraco** — o oposto do
"consolidação tática de alta" descrito ontem. Para quem está comprado desde
o rompimento de meados de julho, o rompimento de 1.180,00 com fechamento
perto da mínima é motivo concreto para reavaliar a posição: um stop lógico
já teria sido acionado hoje se posicionado logo abaixo de 1.180,00 (como
sugerido na leitura de ontem); quem usa stop mais largo, abaixo de 1.193,00
(a mínima de 28/07), também teria sido stopado, dado que a mínima de hoje
(1.173,50) ficou bem abaixo desse nível também. Para quem opera vendido
tático, a mínima de hoje (1.173,50) é a nova referência técnica, com stop
acima da máxima do dia (1.209,75) ou, mais conservador, acima do nível
recém-rompido de 1.180,00 — o fechamento perto da mínima e o volume do dia
dão alguma munição a essa leitura, mas a ressalva central é que o COT ainda
não confirmou se a posição comprada especulativa (esticada desde 21/07) já
está sendo desmontada; um short novo entra, portanto, antes da confirmação
mais importante desta janela (o corte de COT de 31/07). Para quem opera o
book relativo, o alargamento do prêmio de exportação em Paranaguá (de ~8,8%
para 10,68%) é, em si, uma operação de convergência — comprar basis físico
contra vender papel captura a divergência de hoje, com o risco de que o
físico simplesmente ainda não tenha reagido.

---

## Farelo

**Viés: neutro tático — o ratio Far/Soj voltou para 81,34% (indicators,
2026-07-29), saindo da zona "comprimida" (<80%) em que havia fechado
(marginalmente) na sessão anterior, e revertendo em uma única sessão o
rompimento que a leitura de ontem tratou como confirmação tática da tese
bear-farelo — mas a tese estrutural (ABIOVE, Índice de Sobra de Farelo,
prêmio de exportação zerado) permanece integralmente intacta e não se
moveu.** Trata `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
(reaberto pela fila de hoje, que já cita o valor de fechamento atual —
"Ratio Far/Soj 81,4%" — quase idêntico ao 81,34% calculado aqui).

### Correção importante em relação à leitura de ontem

**A leitura de 28/07/2026 declarou que o ratio havia fechado em 79,96%,
abaixo de 80%, confirmando taticamente o gatilho da tese estrutural aberta
em [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]].** O briefing de
hoje, ao recalcular os indicadores para a data de 28/07 usando os preços de
fechamento revisados daquela sessão (soja 1.204,75, não 1.204,00; farelo
321,30, não 320,90), chega a um valor diferente: **far_soj_ratio_pct de
80,01% para 28/07/2026** — um número que, por uma margem mínima (0,01 ponto
percentual), está **ACIMA** do piso de 80%, e portanto **dentro da zona
neutra, não da zona comprimida**. Em outras palavras: com os dados revisados
disponíveis nesta consulta, **o rompimento que a leitura de ontem declarou
como confirmação tática nunca ficou tecnicamente confirmado** — 79,96% era
um valor calculado sobre preços que, um dia depois, foram revisados para
cima o suficiente para colocar o ratio de volta (por pouquíssima margem) na
zona neutra. Esta análise trata isso como um ponto central de honestidade:
**a "confirmação com atraso de 47 dias" anunciada ontem foi, na melhor das
hipóteses, uma confirmação por uma margem de 0,04 ponto percentual em cima
de dados preliminares, e essa margem já não existe mais nos dados
revisados.** Hoje, de qualquer forma, o ratio subiu ainda mais, para 81,34%
— o que significa que, revisado ou não, o fechamento de hoje está
claramente na zona neutra, não na comprimida. O gatilho estrutural da tese
de 11/06 (ratio <80%) **segue, portanto, formalmente não confirmado por
nenhum fechamento robusto até o momento**, apesar de o preço ter oscilado
muito perto do piso repetidamente ao longo de julho.

### O que sustenta a leitura de hoje

**O movimento do ratio hoje foi puramente relativo — o farelo, isoladamente,
também caiu, só que menos que a soja.** Farelo CBOT (ZMU26.CBT) abriu em
321,30 (exatamente no fechamento revisado de ontem, gap zero — o mesmo
padrão de abertura sem gap observado em 28/07), fez máxima de 322,40 e
mínima de 315,00, fechando em 318,50 — queda de -0,87% no dia. O fechamento
equivale a 47,3% do range ((318,50-315,00)÷(322,40-315,00)) — praticamente
no meio, nem fraqueza nem força extrema, um comportamento bem mais morno que
o da soja (que fechou a 3,4% do range) e do óleo (5,75% do range, ver
abaixo). O volume foi de 47.456 contratos — abaixo dos 54.336 registrados em
28/07 (dado citável diretamente desta janela), uma queda de -12,6% no
volume, coerente com uma sessão de menor convicção direcional em farelo
isoladamente, mesmo com o ratio se movendo de forma expressiva.
**Mecanismo:** como o farelo caiu -0,87% e a soja caiu -2,49%, o numerador
do ratio encolheu bem menos que o denominador — o ratio sobe mesmo com o
farelo em queda absoluta, o espelho exato do mecanismo que derrubou o ratio
em 28/07 (quando a soja subia mais rápido que o farelo).

**A sequência recente do ratio, com os valores tal como aparecem neste
briefing (nota: sujeitos a revisão retroativa, como demonstrado acima),
mostra o padrão de teste-e-recuo se estendendo, não se resolvendo.** 07-24:
80,02% → 07-27: 80,09% → 07-28: 80,01% (revisado) → **07-29: 81,34%**. O
ratio passou a maior parte de julho oscilando numa faixa muito estreita ao
redor do piso de 80% (entre 79,96% e 80,65% nas últimas duas semanas, antes
da revisão), sem um único fechamento inequivocamente confirmado abaixo dele
que resistisse à revisão de dados do dia seguinte. **Isso não invalida a
tese estrutural** (ver abaixo), mas exige uma calibração de expectativas
sobre a velocidade de confirmação tática deste indicador específico: sete
semanas depois da compressão inicial de 11/06, o ratio segue tecnicamente
"testando" o piso, não "tendo rompido" de forma robusta.

**O COT de 21/07/2026 (CFTC, ainda o mais recente) mostrava managed money
extremamente comprado em farelo** — net long de 73.476 contratos (11,89% do
open interest de 618.289 contratos), alta de +57,8% na semana. Com o ratio
de volta à zona neutra hoje, a configuração de "posição não paga" fica
menos aguda do que estaria se o rompimento de ontem tivesse se confirmado —
um fundo comprado em farelo, com o ratio em 81,34% (zona neutra, não bear),
não está posicionado contra um sinal estrutural tático confirmado, apenas
contra a tese estrutural mais lenta (ABIOVE, ISF). O corte de 28/07
(publicação ~31/07, a 2 dias) segue sendo o dado mais aguardado para ver se
essa posição já começou a ser reduzida de qualquer forma.

**A crush margin subiu para 2,8110 USD/bushel hoje (+2,72%), interrompendo a
sequência de seis quedas seguidas documentada na leitura de ontem** (Board
Crush: farelo 318,50 + óleo 68,65 − soja 1.174,75; sequência 07-24: 2,9568 →
07-27: 2,8426 → 07-28: 2,7365 (revisado) → **07-29: 2,8110**, +2,72% no
dia). **Mecanismo:** a soja (o custo) caiu -2,49%, muito mais rápido do que
a soma farelo+óleo (a receita, em termos absolutos de pontos: 321,30+70,14 =
391,44 ontem vs 318,50+68,65 = 387,15 hoje, uma queda de apenas -1,10%) — a
crush se recupera porque o custo caiu proporcionalmente mais que a receita
combinada. **Este é o ponto mais contraintuitivo da leitura de hoje: em um
dia de queda generalizada nas três pernas, a economia do esmagador
melhorou**, não piorou — o oposto do que uma leitura superficial ("tudo
caiu, deve ser ruim para o crush") sugeriria. Um crush mais folgado tende a
incentivar, não desincentivar, o ritmo de esmagamento — um contraponto,
ainda tático, à preocupação levantada ontem sobre a esmagadora moderar o
ritmo.

**O oil-meal spread caiu para 0,5445 USD/bushel** (ante 0,6468 em 28/07,
-15,82%) — a sexta sessão seguida de compressão nesta métrica, e a maior
queda percentual em um único dia desta janela observada. **Mecanismo:** o
óleo caiu -2,12% enquanto o farelo caiu apenas -0,87% — o farelo ganha
terreno relativo sobre o óleo dentro do valor do crush. Mais uma vez, como
em 28/07, isso ilustra que "farelo bear" não é uma leitura uniforme: o
farelo está relativamente FRACO frente à soja hoje (ratio subindo, ou seja,
o farelo caiu menos que a soja — o que na verdade é uma leitura mais
NEUTRA/FORTE para farelo, não fraca) mas relativamente FORTE frente ao óleo
(oil-meal spread caindo, farelo perde menos valor que o óleo). Note que a
frase anterior mistura direções propositalmente para deixar explícito o
ponto: hoje o farelo foi, das três pernas, a que mais preservou valor em
termos relativos — o oposto do enquadramento "farelo fraco" que dominou a
leitura de ontem.

**As praças físicas de farelo no Brasil (NAG) seguem totalmente estáveis
hoje** — Mato Grosso/IMEA R$ 1.669,72/ton (var 0,0%), Rondonópolis R$
1.650,00/ton (var 0,0%) e RS R$ 1.640,00/ton (var 0,0%), todas nos mesmos
níveis documentados desde pelo menos 24/07 (MT/IMEA) e 20/07
(Rondonópolis). O prêmio de exportação em Paranaguá segue zerado em +0,05
USD/short ton, agora **26 dias corridos sem variação** desde 03/07/2026 —
o pilar mais persistente e, nesta leitura, o mais importante da tese
estrutural: o mercado internacional segue simplesmente não pagando o
suficiente para tirar farelo do Brasil, então o excedente continua
represado no mercado interno independentemente de qualquer oscilação diária
do ratio.

**O Índice de Sobra de Farelo (ISF) permanece em 80/100 (4 de 5 condições
estruturais), com print de 29/07/2026** — inalterado desde pelo menos
01/07/2026, e sem qualquer relação mecânica com o ratio tático (o índice usa
critérios estruturais que não se moveram hoje). **A trajetória ABIOVE**
(sem alteração) segue mostrando a exportação de farelo brasileiro projetada
caindo de 1.400 mil toneladas em agosto/2026 para 700 mil toneladas em
dezembro/2026 (-50% em quatro meses), com produção caindo bem menos
(2.285,06 → 1.659,04 mil toneladas, -27,4%) — o excedente estrutural segue
intacto e é, nesta leitura, um pilar bem mais sólido para uma eventual
tese bear-farelo do que o ratio tático, que se provou, nesta e na sessão
anterior, mais volátil e sujeito a revisão do que a leitura de ontem havia
tratado.

### O que invalida / risco para o farelo

- **O ratio Far/Soj precisa fechar de forma robusta e repetida abaixo de
  80% para validar qualquer tese tática bear** — depois de duas semanas
  testando o piso sem uma confirmação que sobreviva à revisão de dados do
  dia seguinte, esta leitura recomenda tratar qualquer fechamento pontual
  perto de 80% com ceticismo até 2-3 sessões consecutivas confirmarem o
  mesmo lado do piso.
- **A crush margin, se continuar melhorando**, pode incentivar a
  esmagadora a acelerar o ritmo de esmagamento — aumentando a oferta física
  de farelo e reforçando, não contrariando, a tese estrutural ABIOVE/ISF de
  excedente.
- **O próximo corte do COT (28/07, publicação ~31/07)** mostrar os fundos
  vendendo ou comprando mais em farelo — qualquer um dos dois sinais muda o
  peso relativo entre o argumento estrutural (bear) e o posicionamento
  especulativo.
- **O prêmio de exportação em Paranaguá sair de zero** depois de 26 dias
  parado — o pilar mais persistente da tese estrutural, mas também o que,
  se quebrar, mais mudaria o quadro.

### Leitura operacional — farelo

Depois da reversão de hoje, esta leitura recomenda tratar o farelo como
**neutro tático dentro de uma tese estrutural bear ainda válida, mas não
confirmada por gatilho de preço robusto**. Para quem já havia montado uma
posição vendida em farelo isolado ou no ratio Far/Soj com base na leitura de
ontem, o dado de hoje é um alerta direto: a "confirmação" citada ontem não
sobreviveu à revisão de dados nem à sessão seguinte, o que reforça a
recomendação, já feita ontem, de operar a tese via spread calibrado
(farelo vs. soja, ou farelo vs. óleo) em vez de posição direcional isolada,
com dimensionamento que tolere reversões de curto prazo enquanto a tese
estrutural (ABIOVE, ISF, prêmio zerado) continua a favor do lado bear no
médio prazo. Para quem opera o oil-meal spread especificamente, a
compressão de -15,82% hoje (farelo forte vs. óleo) é o sinal mais limpo e
direto desta sessão — capturar farelo contra óleo, e não farelo contra
soja, é a expressão que teve o movimento mais consistente e menos sujeito à
reversão observada no ratio Far/Soj.

---

## Óleo

**Viés: bear tático, com tensão estrutural mais aguda que ontem — o óleo
estendeu a quebra do suporte técnico de 72,00 cts/lb pela terceira sessão
seguida, fechando em 68,65 cts/lb (-2,12% sobre o fechamento revisado de
ontem de 70,14), com fechamento a apenas 5,75% do range acima da mínima do
dia — mas a margem de biodiesel americana disparou +14,58% no dia, para o
maior nível desta janela observada (1,4385 USD/galão), e o Índice de
Suporte do Óleo segue em 100/100.** Trata `alerta-quebra_suporte-oleo_cbot-2026-07-29`
(terceira confirmação consecutiva do rompimento, e a mais profunda: o
fechamento de hoje está 4,65% abaixo do nível de 72,00, ante -2,28% em
28/07).

### O que sustenta a tese

**A sessão de hoje foi de fechamento perto da mínima, o padrão mais fraco
observado nesta janela para o óleo.** Abertura 70,50 (+0,51% sobre o
fechamento de ontem, um pequeno gap positivo), máxima 71,11 (tocada cedo,
sem sustentação), mínima 68,50 (um novo patamar, bem abaixo do fechamento
de ontem) e fechamento em 68,65 — apenas 0,15 cts acima da mínima, ou
**5,75% do range do dia** ((68,65-68,50)÷(71,11-68,50)). **Mecanismo e
leitura:** diferente da recuperação parcial observada em 28/07 (fechamento
em 51,0% do range, "meio do range"), hoje o óleo fechou colado na mínima —
um padrão de venda contínua ao longo da sessão, sem recompra relevante, e
tecnicamente mais próximo de uma capitulação do que os dois dias
anteriores. O volume foi de 59.751 contratos, o maior das três pernas hoje
em termos absolutos; este briefing não traz o volume de óleo de 27/07 nem
28/07 na janela consultada (mesma limitação de truncamento observada para a
soja — ver Honestidade), então não é possível comparar volumes dia a dia
para o óleo nesta leitura.

**A margem de biodiesel americana é, pelo terceiro dia seguido, o dado mais
importante e menos óbvio desta sessão para o óleo — e hoje o movimento foi
o maior da série.** Custo do óleo: 5,1488 USD/galão (7,5 lb × 68,65
cts/lb), ante 5,2605 ontem (-2,12%, seguindo exatamente a queda do preço do
óleo). Receita: 7,3873 USD/galão (heating oil 4,2223 + 1,5×RIN D4 2,11),
ante 7,3159 ontem (+0,98% — desta vez a receita SUBIU, puxada pelo heating
oil, que fechou em 4,2223 ante 4,1509 ontem, +1,72%). Margem: **1,4385
USD/galão**, ante 1,2554 (+14,58%) — o maior valor observado nesta janela
(que vinha de 1,0354 em 24/07, 1,1048 em 23/07, 1,1629 em 27/07, 1,2554 em
28/07 — uma trajetória de melhora praticamente ininterrupta ao longo da
semana). **Mecanismo:** desta vez a melhora não veio só da queda do custo
(como em 27/07 e 28/07, quando a receita ficava praticamente estável) — o
heating oil subiu de forma relevante, então a melhora da margem hoje reflete
tanto um custo mais barato (óleo caindo) quanto uma receita mais rica
(energia subindo) ao mesmo tempo, os dois fatores reforçando o mesmo sinal
pela primeira vez nesta janela. **Esta é a tensão central da tese do óleo,
agora mais aguda**: o preço cai pelo terceiro dia seguido e fecha cada vez
mais perto da mínima, mas o incentivo econômico da indústria de biodiesel
americana a usar óleo de soja como insumo está no maior nível observado —
se essa divergência persistir, o argumento de que a fraqueza técnica está
descolada do fundamento de demanda de biodiesel fica mais forte, não mais
fraco.

**O heating oil (HO=F) trouxe hoje o print de volume mais baixo de toda a
janela observada — um novo mínimo depois de dois dias seguidos de
anomalias.** O volume de hoje veio com apenas **70 contratos** — abaixo dos
788 de ontem, que já eram considerados baixos, e muito abaixo dos 23.447
(revisados) de 27/07. **Isso estende para a terceira sessão seguida um
padrão de volume aparentemente incompleto no dado bruto de heating oil**: a
leitura de ontem já havia sinalizado, como ponto de honestidade, que o
print de 788 contratos poderia estar sujeito à mesma revisão que
transformou 278 em 23.447 contratos para 27/07. O print de hoje (70
contratos) é ainda mais extremo, reforçando a hipótese de que os dados de
heating oil dos últimos dias são preliminares e tendem a ser revisados
substancialmente para cima em dumps futuros — esta leitura usa o preço de
fechamento de hoje (4,2223) normalmente (o preço, ao contrário do volume,
não mostrou o mesmo padrão de revisão retroativa até agora), mas trata
qualquer leitura de convicção baseada em volume de heating oil recente com
cautela redobrada.

**O Índice de Suporte do Óleo (ISO) permanece em 100/100 (5 de 5
condições), com print de 29/07/2026** — a tese estrutural (óleo dominando o
valor do crush) segue formalmente intacta, sem nenhuma alteração apesar da
terceira sessão seguida de quebra técnica do preço.

**O oil share caiu para 51,87%** (ante 52,19% em 28/07, -0,32 ponto
percentual) — quinta sessão seguida de queda (52,62% em 24/07 → 52,52% em
27/07 → 52,19% em 28/07 → **51,87%** hoje), agora bem abaixo da faixa de
53,0-53,5% em que o indicador oscilou até 22/07, e o menor valor desta
janela observada. **Mecanismo:** o óleo caiu -2,12% enquanto o farelo caiu
apenas -0,87%, encolhendo a fração de valor do crush capturada pelo óleo.
A persistência desta queda (agora cinco leituras seguidas) segue sendo o
indicador tático mais próximo de contradizer a leitura estrutural do ISO
100/100 — ainda sem um gatilho formal de revisão do índice, mas a
distância entre a leitura tática (oil share caindo) e a estrutural (ISO
travado em 100) segue crescendo.

**O COT de 21/07/2026 (CFTC, ainda o mais recente) seguia mostrando o óleo
como a perna mais concorrida das três** — managed money com 143.159
contratos comprados, 18,17% do open interest de 661.652 contratos (ante
12,49% em soja e 11,89% em farelo). Com três sessões seguidas de quebra
técnica desde então (27/07, 28/07 e hoje), a pressão sobre esse
posicionamento comprado é, nesta leitura, a mais alta das três pernas — o
corte de COT de 31/07 é o dado mais aguardado para esta perna
especificamente.

**A curva forward manteve a backwardation, com forma preservada mas amplitude
ligeiramente menor.** Agosto/26 (Q26) 69,07 → Setembro/26 (U26, spot) 68,65
(-0,42, -0,61%) → Outubro/26 (V26) 68,03 (-0,62, -0,90%) → Dezembro/26 (Z26)
67,64 (-0,39, -0,57%) → Janeiro/27 (F27) 67,50 (-0,14, -0,21%) — uma queda
total de -1,57 cts/lb (-2,27%) de agosto a janeiro/27, ligeiramente menos
acentuada que os -2,82% observados ontem, mas ainda claramente em
backwardation (sinalizando aperto físico relativo de curto prazo, sem sinal
de estresse agudo adicional).

### O que invalida / risco para o óleo

- **Um fechamento abaixo de 68,50** (mínima de hoje) confirmaria uma quarta
  sessão seguida de fraqueza técnica e reforçaria a leitura de que a quebra
  de suporte não é mais um evento pontual.
- **O heating oil (HO=F) precisa urgentemente de uma sessão de volume
  normal e estável** — depois de três sessões seguidas de prints anômalos
  (278→23.447 revisado; 788; 70), esta leitura não trata os últimos dados
  de volume de heating oil como confiáveis, e recomenda cautela redobrada
  com qualquer leitura de convicção baseada neles até uma sessão de volume
  plausível (dezenas de milhares de contratos, como é típico do HO)
  aparecer sem necessidade de revisão.
- **O oil share continuar caindo abaixo de 51,87%** por mais sessões —
  reforçaria a leitura de perda estrutural de participação do óleo no valor
  do crush, o indicador tático mais próximo de contradizer o ISO 100/100.
- **O próximo corte do COT (28/07, publicação ~31/07) confirmar liquidação
  no net long mais concorrido das três pernas (18,17% do OI)** — com três
  sessões seguidas de quebra técnica desde a foto de 21/07, este é o teste
  mais direto e mais aguardado desta janela.
- **A isenção PIS/Cofins do biodiesel expirar em 31/07 sem renovação** (ver
  Lente fiscal), agora a apenas **2 dias**, sem nenhuma atualização do
  monitor tributário há 55 dias — um vetor bearish direto para a demanda
  doméstica de óleo, independente do CBOT e da margem americana.
- **MPOB seguir inacessível** (20º dia consecutivo) — mantém cego o efeito
  de eventuais movimentos no prêmio de substituição via palma.

### Leitura operacional — óleo

O óleo segue sendo a perna com a tensão mais explícita entre técnico e
fundamento, e hoje essa tensão ficou mais aguda dos dois lados
simultaneamente: terceira sessão seguida de fechamento abaixo do suporte de
72,00, com o pior padrão de fechamento (perto da mínima) das três sessões,
mas a margem de biodiesel no maior nível da janela, com melhora vinda tanto
da queda do custo quanto da alta da receita ao mesmo tempo. Para quem está
comprado direcional, a sequência de três quebras seguidas, cada uma mais
funda que a anterior, é motivo concreto para reduzir exposição ou apertar
o stop para a mínima de hoje (68,50); mas a força simultânea da margem de
biodiesel argumenta contra tratar a posição como definitivamente invalidada
no fundamento — o quadro é de tese estrutural sendo testada tecnicamente
com convicção crescente do lado vendedor, sem confirmação de que perdeu
sustentação de demanda real. Para quem opera vendido ou tático short, a
mínima de hoje (68,50) é a referência de entrada mais recente, com stop
acima da máxima do dia (71,11); o prazo de apenas 2 dias até o vencimento
da isenção PIS/Cofins (31/07) é agora o catalisador mais próximo e mais
concreto desta leitura inteira, e uma posição short tática ganha um
argumento fundamentalista adicional (não só técnico) se a isenção expirar
sem renovação. Para quem opera o crush ou o oil-meal spread, a compressão
de -15,82% hoje (ver Farelo) é a expressão mais limpa e consistente da
tensão entre as duas pernas de saída do esmagamento nesta sessão —
claramente favorável ao lado "farelo forte / óleo fraco" dentro do crush,
com o oil share reforçando a mesma leitura de forma independente.

---

## Spreads e crush — leitura de complexo

### Ratio Far/Soj: 81,34% — de volta à zona neutra, revertendo o rompimento tratado ontem como confirmado

Depois do fechamento de ontem (80,01% nos dados revisados — não 79,96% como
descrito na leitura de 28/07, ver correção na seção Farelo), o ratio subiu
hoje para 81,34%, saindo com folga da zona "comprimida" (<80%) e voltando à
zona neutra de mean-reversion (80-87%). O mecanismo do dia foi soja caindo
muito mais rápido (-2,49%) do que farelo (-0,87%) — o espelho exato do
mecanismo de 28/07 (soja subindo mais rápido que farelo). A fila de hoje
reabriu `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
citando o valor atual do ratio (~81,4%) diretamente no texto do gatilho —
esta leitura trata essa revisão como ainda **não confirmada**: sete semanas
e meia depois da compressão inicial de 11/06 (83,3%→81,4% em quatro
pregões), o ratio nunca fechou de forma robusta e sustentada abaixo de 80%.
O checkpoint D+90 (2026-09-09) permanece como o próximo marco formal de
revisão da tese completa, agora com uma calibração mais conservadora sobre
o que conta como "confirmação".

### Crush margin: 2,8110 USD/bu — recuperação de +2,72%, rompendo a sequência de seis quedas

Subiu +2,72% no dia (2,7365 → 2,8110, valores revisados/atuais),
interrompendo a sequência de compressão documentada ontem (07-24: 2,9568 →
07-27: 2,8426 → 07-28: 2,7365 → **07-29: 2,8110**). O mecanismo: a soja
caiu proporcionalmente muito mais rápido (-2,49%) do que a soma farelo+óleo
(-1,10% em pontos absolutos) — o crush melhora porque o custo cai mais
rápido que a receita combinada, mesmo com as duas pernas de saída também em
queda. A crush segue folgada em termos absolutos, distante do nível de
alerta histórico citado em leituras passadas (<2,50 USD/bu), e a
recuperação de hoje remove, ao menos por uma sessão, a preocupação
levantada ontem sobre a esmagadora moderar o ritmo de esmagamento.

### Oil share: 51,87% — quinta sessão seguida de queda, novo mínimo da janela

Caiu -0,32 ponto percentual (52,19% → 51,87%), estendendo a sequência de
quedas iniciada quando o indicador saiu da faixa estreita de 53,0-53,5% em
que oscilou até 22/07 (52,52% em 27/07 → 52,19% em 28/07 → **51,87%**
hoje). Ainda não é uma ruptura estrutural (o ISO permanece 100/100), mas a
distância entre a leitura tática e a estrutural segue crescendo — cinco
sessões seguidas na mesma direção é o padrão mais persistente desta janela
observada para qualquer indicador do crush.

### Oil-meal spread: 0,5445 USD/bu — compressão de -15,82%, a maior queda diária da janela

Caiu -15,82% no dia (0,6468 → 0,5445) — a sexta sessão seguida de
compressão e a maior variação percentual em um único dia observada nesta
métrica. O farelo segue ganhando terreno relativo sobre o óleo dentro do
valor do crush. **Importante, e ainda mais evidente hoje do que ontem**:
esse movimento é o oposto do ratio Far/Soj (que hoje mostra o farelo
GANHANDO terreno relativo à soja, não perdendo) — as duas métricas capturam
comparações diferentes e hoje apontam na MESMA direção favorável ao farelo
(fraco vs. soja em termos absolutos de queda menor = na verdade relativamente
forte; forte vs. óleo), o oposto exato da divergência observada em 28/07.
Isso reforça que qualquer leitura de "farelo bear" ou "farelo bull" precisa
sempre especificar contra qual perna a comparação é feita.

### Margem de biodiesel: 1,4385 USD/gal — terceira melhora seguida, +14,58% hoje, maior nível da janela

O indicador que mais diverge do preço do óleo nesta leitura: melhorou pela
terceira sessão seguida (07-27: +7,95% [1,1629→ implícito], 07-28: +7,95%,
07-29: +14,58%), com a melhora de hoje vindo tanto da queda do custo (óleo
mais barato) quanto da alta da receita (heating oil mais caro) ao mesmo
tempo — a primeira vez nesta janela em que os dois fatores reforçam a
mesma direção simultaneamente. É o dado mais importante para sustentar que
a fraqueza técnica do óleo nestas três últimas sessões pode não refletir
deterioração fundamental do lado da demanda de biodiesel americana.

### COT: corte de 21/07, ainda o mais recente — agora a apenas 2 dias do próximo corte

O corte de 21/07/2026 mostrava fundos extremamente comprados nas três
pernas (net long +73.476 farelo/11,89% OI, +120.246 óleo/18,17% OI,
+130.505 soja/12,49% OI). Nenhum dado novo chegou hoje. O próximo corte
(referente a 28/07, publicação normal ~31/07) está agora a apenas 2 dias e é,
para as três pernas, o teste mais direto de se a posição especulativa
esticada já começou a ser desmontada — ganha relevância adicional depois do
tombo de hoje em soja e óleo, que testa diretamente a resiliência desse
posicionamento comprado.

### ISF em 80/100, ISO em 100/100 — ambos inalterados, prints de 29/07

Os dois índices sintéticos, que captam condições estruturais (não a
mecânica tática de preço intradiário), permanecem exatamente nos mesmos
níveis desde pelo menos 01/07/2026. Eles não se moveram apesar da reversão
do ratio e da terceira quebra seguida do óleo hoje — coerente com sua
natureza estrutural, mas a distância entre o que os índices estruturais
apontam e o que a mecânica tática do dia mostrou (crush melhorando, ratio
subindo, oil share caindo) segue sendo o quadro central desta janela: os
fundamentos estruturais (ABIOVE, ISF, ISO) mudam pouco dia a dia, mas a
mecânica tática de preço oscila com muito mais amplitude e, como
demonstrado hoje, está sujeita a revisões que podem apagar em um dia o que
pareceu confirmado no dia anterior.

### O que os índices dizem juntos em 29/07/2026

ISF 80/100 + ISO 100/100 (ambos inalterados) + ratio Far/Soj de volta à
zona neutra (81,34%, revertendo o rompimento tratado ontem como confirmado)
+ crush margin recuperando (+2,72%, rompendo seis quedas seguidas) + oil
share no menor nível da janela (51,87%, quinta queda seguida) + oil-meal
spread na maior compressão diária (-15,82%) + margem de biodiesel no maior
nível da janela (+14,58%, terceira melhora seguida) + COT ainda parado no
corte de 21/07 (fundos extremamente comprados nas três pernas, posição
testada por dois dias consecutivos de tombo em soja e óleo, ainda não
confirmada como desmontada) formam, juntos, um quadro que **volta a se
dividir** depois da convergência parcial documentada ontem: a soja assume o
papel de perna mais fraca tecnicamente (rompeu piso, fechou na mínima), o
óleo estende sua própria fraqueza técnica isolada (terceira quebra seguida)
mas com fundamento de biodiesel cada vez mais forte, e o farelo — a perna
que ontem parecia mais definida como bear tático — é hoje, paradoxalmente,
a mais estável e a que mais preservou valor relativo das três. O próximo
corte do COT (31/07, a 2 dias) é o dado que mais provavelmente resolve
parte dessa complexidade, ao mostrar se o posicionamento comprado
historicamente esticado nas três pernas já está sendo desmontado depois de
dois dias seguidos de fraqueza em soja e óleo.

---

## Lente fiscal e regulatória BR

**Isenção PIS/Cofins biodiesel — vencimento em 31/07/2026, agora a apenas 2
dias, ainda sem sinalização pública de renovação** (evento
PISCOFINS-BIODIESEL-ISENCAO, `atualizado_em` 2026-06-05, sem mudança desde
então — agora 55 dias sem atualização do monitor). Trata
`trib-PISCOFINS-BIODIESEL-ISENCAO-2026-07-31`, sinalizado pela fila de hoje
com a tag `[2d]`, o vetor tributário de maior prioridade de monitoramento no
momento, agora ainda mais urgente. **O mecanismo:** a isenção incide na
saída do biodiesel; se expirar sem renovação, o custo tributário efetivo da
produção sobe, o que tende a reduzir a margem de biodiesel doméstica
(distinta da margem americana calculada nesta leitura, que hoje disparou
para o maior nível da janela, mas usa RIN D4 e heating oil dos EUA, não o
regime tributário brasileiro) e, por extensão, pressionar a demanda por
óleo de soja como insumo dentro do mix B15 mandatório — um vetor bearish
direto para o óleo doméstico, independentemente do que aconteça no CBOT ou
na margem americana. **A divergência entre uma margem americana disparando
(+14,58% hoje) e um risco tributário doméstico a 2 dias de se concretizar é
a tensão fiscal mais aguda desta leitura** — o óleo brasileiro pode estar
prestes a perder um benefício tributário exatamente no momento em que o
incentivo econômico americano ao biodiesel de soja está no pico desta
janela, dois sinais que apontam para direções opostas dependendo de qual
mercado (doméstico BR vs. exportação/referência internacional) se está
precificando.

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L) —
vigência formal venceu há 18 dias (`vigencia_ate` 11/07/2026), sem qualquer
atualização de status.** Enquanto o combustível fóssil segue formalmente
subsidiado (sem confirmação de que o subsídio de fato terminou), a
competitividade relativa do biodiesel dentro do mix B15 mandatório segue
pressionada.

**B16 — sem data, travado em B15**, sem mudança de status. Testes técnicos
do FNDCT com resultado esperado ~nov/2026 — realista só fim de 2026/início
de 2027.

**MP 1.363/2026 (subsídio ao diesel fóssil, R$ 1,12/L) — em vigor até
31/12/2026**, sem alteração. Bearish estrutural persistente para a demanda
incremental de óleo de soja no mercado doméstico brasileiro.

**STJ REsp 2.165.276/2026 — crédito PIS/Cofins para esmagadoras**, sem
alteração. Bullish para soja/óleo (alívio de custo de entrada para
biodiesel), em tensão direta com a crush margin — que hoje melhorou, então
o alívio tributário estrutural e a mecânica tática de curto prazo apontam,
pela primeira vez nesta janela, na mesma direção.

**Vetores dos EUA e Indonésia, sem mudança de status desde 2026-06-05:**
EPA-RFS-2026-2027 (volumes recordes de biocombustível, sustentando o RIN
D4 usado na margem de biodiesel, fixo em 2,11 USD/RIN); 45Z-CLEAN-FUEL
(regra que favoreceria óleo de soja doméstico americano); DANANTARA-INDONESIA
(centralização estatal da exportação de palma, plena em 01/09/2026);
INDONESIA-B50 (provável B45 em 2026, B50 pleno só 2027-28);
INDONESIA-LEVY-PMK9 (imposto de exportação de CPO até 12,5%, encarecendo
palma). Conjunto estruturalmente bullish para óleo de soja via substituição
de palma, mas inverificável pelo lado de mercado (MPOB inacessível há 20
dias, ver Honestidade).

**O monitor tributário como um todo está há 55 dias sem qualquer
atualização** — o intervalo cresce exatamente na semana do vencimento da
isenção PIS/Cofins (2 dias). Prioridade máxima de manutenção do sistema,
independentemente da leitura de preço de hoje.

---

## Riscos e eventos próximos

**A isenção PIS/Cofins do biodiesel vence em 31/07/2026, agora a apenas 2
dias**, sem sinalização de renovação — prioridade máxima de monitoramento
até a resolução (fila `trib-PISCOFINS-BIODIESEL-ISENCAO-2026-07-31`), e o
catalisador concreto mais próximo de toda esta leitura.

**O próximo corte do COT (referente a 28/07/2026, publicação normal
~31/07/2026)**, agora a apenas 2 dias, é o dado mais aguardado de toda esta
janela para as três pernas — vai mostrar se os fundos que compraram
agressivamente na semana de 21/07 (net long +73,6% soja, +57,8% farelo,
+11,4% óleo, todos na variação semanal) começaram a vender depois de dois
dias seguidos de tombo em soja e óleo, e é o teste mais direto do risco de
liquidação forçada levantado nesta leitura.

**O ratio Far/Soj precisa de 2-3 fechamentos consecutivos claramente de um
lado do piso de 80% para gerar qualquer confiança tática** — depois de duas
sessões seguidas com resultado revertido (79,96%→80,01% revisado→81,34%),
esta leitura recomenda tratar qualquer leitura pontual deste indicador com
ceticismo redobrado até um padrão mais persistente se formar.

**O nível de 1.180,00 na soja, recém-rompido, precisa de confirmação nas
próximas sessões** — um fechamento de volta acima dele desfaria a leitura
de ruptura tratada hoje como o desenvolvimento técnico mais importante do
dia.

**O heating oil (HO=F) está na terceira sessão seguida de volume anômalo**
(278 revisado para 23.447; depois 788; depois 70 hoje) — esta série de
leituras trata qualquer leitura de convicção baseada em volume recente de
heating oil com a máxima cautela até uma sessão de volume plausível
aparecer sem necessidade de revisão subsequente.

**NOPA — segue inacessível** (fila `release-nopa-2026-07-29` tratada aqui,
sem dado interpretável, apenas nova data de coleta), sem crush americano
confirmado por fonte primária, agora há quase sete semanas.

**MPOB — sem números de palma extraídos há 20 dias consecutivos**, mantendo
cego o efeito do El Niño e dos vetores regulatórios indonésios sobre o
prêmio de substituição do óleo de soja.

**O WASDE segue fora da janela de 14 dias deste briefing pelo segundo dia
seguido** (último dado 10/07/2026, agora 19 dias de atraso) — nenhuma
pergunta de tese que dependa do WASDE pode ser respondida a partir deste
briefing.

---

## Honestidade

O que não foi possível validar neste briefing de 29/07/2026, e uma correção
material em relação à leitura de ontem, onde a confiança é baixa ou há
lacunas relevantes:

**1. A leitura de 28/07/2026 declarou que o ratio Far/Soj havia fechado em
79,96%, confirmando o rompimento da zona comprimida (<80%) e a tese
estrutural bear-farelo de 11/06. O briefing de hoje, recalculando os
indicadores de 28/07 com preços de fechamento revisados (soja 1.204,75, não
1.204,00; farelo 321,30, não 320,90), chega a um ratio de 80,01% para
aquela mesma sessão — tecnicamente ACIMA de 80%, ou seja, na zona neutra,
não na comprimida.** Isto significa que a "confirmação tática" anunciada
ontem não sobrevive à revisão de dados disponível hoje — na melhor das
hipóteses, foi uma leitura de um valor preliminar que ficou por uma margem
mínima (0,04pp) do lado errado do piso, e essa margem já não existe nos
dados atuais. Esta leitura trata isso como o ponto de honestidade mais
importante do dia: **o gatilho estrutural da tese de 11/06 (ratio <80%
sustentado) segue formalmente não confirmado**, apesar de o indicador ter
oscilado repetidamente muito perto do piso ao longo de julho. Este é o
terceiro dia seguido (contando 27/07 e 28/07) em que uma revisão retroativa
de dados de sessão anterior é identificada — um padrão recorrente que exige
tratar qualquer leitura tática baseada no fechamento mais recente do
briefing com uma margem de segurança, não como definitiva, até que o
mesmo número apareça de forma estável em pelo menos um dump subsequente.

**2. O volume de heating oil (HO=F) trouxe hoje o terceiro print anômalo
seguido — 70 contratos, o menor valor de toda a janela observada.** Depois
da revisão de 278 para 23.447 contratos identificada para 27/07, e do print
de 788 contratos em 28/07 (também baixo, também não confirmado como
definitivo), o print de hoje é ainda mais extremo. Esta leitura não trata
o preço de fechamento de heating oil como suspeito (o preço não mostrou o
mesmo padrão de revisão que o volume até agora), mas recomenda cautela
máxima com qualquer leitura de convicção baseada em volume recente deste
instrumento.

**3. O veredito desta leitura sobre a soja — de que o rompimento de
1.180,00 é o desenvolvimento técnico mais importante do dia — é uma
interpretação própria desta análise, não um alerta gerado pelo sistema.**
A fila de julgamento de hoje sinalizou apenas o rompimento de suporte do
óleo (72,00) como alerta de nível técnico; não há nenhum item equivalente
para a soja apesar de um movimento de -2,49% através de um piso vigiado
havia mais de uma semana. Esta leitura optou por tratar o rompimento da
soja como material de qualquer forma, por julgamento analítico, mas
registra que ele não veio sinalizado pela camada de fatos do sistema — algo
a considerar na calibração de limiares de alerta.

**4. Os dados de OHLCV (abertura/máxima/mínima/fechamento/volume) de soja e
óleo para 28/07/2026 não estão disponíveis na tabela `cme_cbot` desta
janela de 14 dias** — apenas os valores de fechamento aparecem, indiretamente,
via a seção `indicators` (que usa esses fechamentos para calcular crush
margin, ratio etc.) e via a tabela de forecasts (que usa "spot ref"). Esta é
a mesma limitação identificada na leitura de ontem para os dados de 27/07 —
agora recorrente para uma data diferente, o que sugere um padrão estrutural
na forma como o dump de 14 dias trunca a tabela `cme_cbot`, não um evento
isolado. Como consequência, esta leitura não pode comparar volumes de soja e
óleo entre sessões recentes, apenas citar o nível absoluto do dia mais
atual.

**5. A manchete "Why we shouldn't rule out a record soybean crop" (Farm
Progress, 29/07/2026) foi citada apenas como registro de uma narrativa
qualitativa de oferta ampla** — não há projeção numérica específica
atribuível a esta safra citada no título capturado pelo RSS; esta leitura
não a usa como driver quantitativo de nenhuma tese, apenas como contexto
editorial.

**6. O USDA Crop Progress permanece no corte de 26/07/2026 (11%/52%/7%),
sem atualização nova nesta janela** — o próximo corte semanal é o dado a
acompanhar para ver se a condição da lavoura americana se move na direção
que sustentaria (ou contradiria) o tombo de hoje.

**7. O WASDE permanece completamente fora da janela de 14 dias deste
briefing pelo segundo dia seguido** — agora 19 dias de atraso desde o
último dado (10/07/2026). Nenhuma pergunta de tese que dependa do WASDE
pode ser respondida a partir deste briefing.

**8. NOPA (fila `release-nopa-2026-07-29`) segue com `monthly_status` em
0,0 bool** — mesma barreira de assinatura paga documentada desde meados de
junho, agora com quase sete semanas sem alternativa de dado primário sobre
o esmagamento americano.

**9. Palma malaia (MPOB) segue sem números extraídos, agora por 20 dias
consecutivos com o mesmo conteúdo exato (3.439 caracteres)** — a
persistência do byte count idêntico segue sugerindo, possivelmente, uma
página que não está mais sendo servida com conteúdo atualizado.

**10. O COT (CFTC) segue no corte de 21/07/2026, uma terça-feira — não
cobre nenhuma das três últimas sessões (27/07, 28/07 e 29/07)** — o próximo
corte (28/07, publicação normal ~31/07, agora a 2 dias) é o primeiro capaz
de capturar a reação dos fundos aos três últimos dias de mercado, incluindo
o tombo de hoje em soja e óleo.

**11. Percentis históricos de COT não calculados** — os números de
21/07/2026 seguem lidos apenas em nível absoluto e como fração do open
interest corrente, sem série histórica completa para calibrar se o
posicionamento estava objetivamente "esticado" no sentido histórico.

**12. Clima INMET (BR) não foi usado como driver de preço desta leitura.**
Julho/agosto é entressafra da soja brasileira (colheita concluída, plantio
só em outubro) — sem relevância direta para a tese de preço neste momento
do calendário agrícola, apesar de o dump trazer previsões detalhadas para
2026-07-30 (chuva isolada em PR/RS, calor seco em MT).

**13. BCBA Argentina — última leitura disponível é 22/07/2026, agora 7
dias sem atualização**, sem relatórios de esmagamento/exportação acessíveis
via scraper.

**14. RIN D4 como parâmetro fixo (2,11 USD/RIN) segue sendo uma fonte
relevante de incerteza do modelo de biodiesel** — a margem de 1,4385
USD/gal calculada hoje, assim como toda a série recente, depende desse
valor fixo, o que significa que a melhora expressiva de hoje reflete
inteiramente a combinação de óleo mais barato e heating oil mais caro, não
uma mudança no RIN em si.

**15. Os forecasts estatísticos internos (29/07/2026) mantiveram o rótulo
"altista" para as três commodities, no mesmo dia em que a soja teve o pior
fechamento relativo desta janela observada** — a defasagem deste modelo
(média móvel de 20 dias + volatilidade + inclinação de curto prazo) nunca
ficou tão evidente quanto hoje; esta leitura não usa esses forecasts como
argumento de tese, apenas como referência de banda estatística.

**16. O prêmio de exportação em Paranaguá (+10,68% sobre a paridade
teórica) é o maior desta janela observada, mas esta leitura não tem como
determinar se reflete demanda física genuinamente mais firme ou apenas um
atraso na atualização do preço CEPEA/ESALQ frente ao tombo do CBOT** — as
duas hipóteses têm implicações opostas para a tese de soja e só serão
distinguíveis com a atualização de amanhã.

*Nenhum número foi inventado ou estimado além do que consta no briefing de
29/07/2026 e nos insights anteriores referenciados. A contribuição central
desta leitura foi (1) identificar e corrigir, com transparência, que a
"confirmação tática" do rompimento do ratio Far/Soj anunciada na leitura de
ontem não sobrevive à revisão de dados disponível hoje, recalibrando a
tese estrutural de 11/06 como ainda não confirmada por gatilho de preço
robusto; (2) identificar e explicar o rompimento decisivo do nível técnico
de 1.180,00 na soja — um desenvolvimento que a fila de julgamento não
sinalizou, mas que esta análise tratou como material por julgamento
próprio; (3) decompor o mecanismo pelo qual um dia de queda generalizada
nas três pernas produziu, ao mesmo tempo, uma crush margin em recuperação
(soja caiu mais rápido que farelo+óleo) e um ratio Far/Soj subindo (farelo
caiu menos que soja) — mostrando que "tudo caindo junto" não implica leitura
uniforme entre os indicadores do complexo; (4) documentar a terceira sessão
seguida de anomalia no volume de heating oil, agora no menor nível da
janela (70 contratos), reforçando a recomendação de cautela já levantada
ontem; e (5) registrar a divergência crescente entre a margem de biodiesel
americana (no maior nível da janela) e o risco tributário doméstico da
isenção PIS/Cofins (a 2 dias do vencimento, sem sinalização), a tensão
fiscal mais aguda desta leitura para o óleo.*
