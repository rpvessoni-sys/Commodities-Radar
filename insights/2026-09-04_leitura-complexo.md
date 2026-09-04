---
data: 2026-09-04
titulo: "Quinta-feira (03/09) inverte a hierarquia de ontem — farelo lidera a alta (+1,55%) enquanto o óleo aprofunda a queda (-1,57%) abaixo do suporte — e pela primeira vez em 14 dias os índices estruturais ISF e ISO se movem juntos, com o oil share cruzando abaixo de 50% e o oil-meal spread virando negativo, confirmando uma realocação real de valor dentro do crush, não apenas ruído técnico"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT (ZSX26 soja / ZMV26 farelo / ZLV26 óleo) — sessão de 2026-09-03 (quinta-feira), a mais recente do pipeline: soja abertura 1.308,50, máxima 1.319,00, mínima 1.290,25, fechamento 1.314,50 USD cts/bushel, volume 158.286 contratos; farelo abertura 343,10, máxima 349,50, mínima 338,10, fechamento 348,20 USD/short ton, volume 22.991 contratos; óleo abertura 70,63, máxima 70,63, mínima 68,84, fechamento 69,53 USD cts/lb, volume 28.714 contratos. Curva futura em 03/09: soja set/26 (U26) 1.300,25, nov/26 (X26, contrato-base) 1.314,50, jan/27 (F27) 1.330,00, mar/27 (H27) 1.335,25, mai/27 (K27) 1.340,25, jul/27 (N27) 1.341,75; farelo set/26 (U26) 345,10, out/26 (V26, contrato-base) 348,20, dez/26 (Z26) 355,20, jan/27 (F27) 357,80, mar/27 (H27) 358,90, mai/27 (K27) 359,60; óleo out/26 (V26, contrato-base) 69,53, dez/26 (Z26) 70,00, jan/27 (F27) 70,16, mar/27 (H27) 70,29, mai/27 (K27) 70,34 (sem cotação de set/26 (U26) para óleo neste dump)
  - CME CBOT — sessão de 2026-09-02 (quarta-feira), usada como base de comparação: farelo fechamento 342,90, heating oil fechamento 4,6822 USD/galão (dados diretos do dump); soja fechamento 1.310,25 e óleo fechamento 70,64 reconstituídos via indicators (Board Crush 02/09: farelo 342,90 + óleo 70,64 − soja 1.310,25) — ver Honestidade sobre divergência frente aos valores usados na leitura de ontem (1.308,75/70,54)
  - CME NYMEX heating oil (HO=F) — 2026-09-03: abertura 4,5976, fechamento 4,6006, máxima 4,6026, mínima 4,5898 USD/galão, volume 118 contratos (volume muito baixo, ver Honestidade); 2026-09-02: fechamento 4,6822, volume não destacado nesta leitura
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, ISF, ISO, margem biodiesel, paridade BR) — 2026-09-03 e 2026-09-02, usados para reconstruir a trajetória do dia
  - BCB PTAX — 2026-09-03: USD/BRL 5,0962, EUR/BRL 5,9233, Selic diária 0,05166% a.a.; série de comparação 28/08→03/09: 5,2005 → 5,1816 → 5,1570 → 5,1273 → 5,0962 (BCB, séries SGS 1, 21619 e 11)
  - CEPEA/ESALQ Soja Paranaguá via NAG — 2026-09-03: R$ 160,14/saca (var -0,53%); 2026-09-02: R$ 160,99 (var -0,09%)
  - CEPEA/ESALQ Soja Paraná interior via NAG — 2026-09-03: R$ 151,68/saca (var -0,61%); 2026-09-02: R$ 152,61 (var -0,29%)
  - NAG Físico BR — 2026-09-03: farelo MT/IMEA R$ 1.795,68/ton (var 0,0%, congelado desde 31/08), Rondonópolis/MT R$ 1.900,00/ton (var 0,0%, congelado desde 31/08), RS média R$ 1.860,00/ton (congelada há várias sessões); prêmios export PGUA farelo +0,12 USD/short ton e óleo +0,10 cts/lb, ambos sob rótulo "Setembro/26", mesmo valor idêntico desde 24/08/2026 — agora 10 dias corridos sem se mexer neste dump (11 dias corridos até hoje, 04/09), ver Honestidade
  - CFTC COT Managed Money, Swap Dealers e Producer/Merchant — corte de 2026-08-25, AINDA o mais recente disponível (nenhum corte novo neste dump); 9 dias corridos de defasagem frente ao fechamento de 03/09 (10 dias frente a hoje, 04/09)
  - USDA Crop Progress — corte de 2026-08-30 (12% excelente / 46% boa / 9% ruim), sem atualização nova nesta janela
  - USDA WASDE — segue ausente da janela deste briefing
  - NOPA — fila `release-nopa-2026-09-03` marca novo "release" pelo terceiro dia seguido, mas `monthly_status` segue em 0,0 bool (paywall), sem número de esmagamento americano mensal
  - ABIOVE projeções mensais — balanços set-dez/2026, mesmos valores da leitura anterior, sem revisão nesta janela
  - NOAA CPC ENSO — carimbo 2026-09-03 (El Niño Advisory, inalterado)
  - MPOB — carimbo 2026-09-03 (3.456 caracteres, parser sem números extraídos, mesma barreira)
  - BCBA (Argentina) — carimbo 2026-09-03, scraper acessa a página mas não encontra links de relatório detectados
  - INMET — previsão para 2026-09-04 (hoje, primeira vez nesta sequência de leituras com previsão same-day disponível no dump): núcleo produtor de Mato Grosso segue muito quente e SEM menção de chuva no boletim — Cuiabá 37°C/26°C "muitas nuvens", Sinop 39°C/24°C "muitas nuvens", Lucas do Rio Verde 38°C/24°C "muitas nuvens", Sorriso 37°C/24°C "muitas nuvens", Rio Verde/GO 34°C/21°C "muitas nuvens" — nenhuma dessas cinco estações menciona precipitação no boletim de hoje; já o Sul aparece com chuva: Cascavel/PR 28°C/18°C "pancadas de chuva e trovoadas isoladas", Maringá/PR 31°C/18°C "pancadas de chuva e trovoadas isoladas", Passo Fundo/RS 17°C/11°C "pancadas de chuva isoladas" — contraste com a condição de 03/09 em Cascavel/PR, que era "poucas nuvens" (seca)
  - Notícias Agrícolas/Canal Rural + FarmProgress RSS — 2026-09-03: "160 items lidos, 9 mantidos (soja/farelo/oleo)", único headline com texto legível: soja — "The soybean sales pitch you can't make over Zoom" (FarmProgress), sem conteúdo de mercado relevante — ver Honestidade sobre os outros 8 itens "mantidos" sem headline exposto
  - Forecasts estatísticos internos (bandas 7d/30d, MA20+volatilidade+slope) — geração de 2026-09-03, alvos 10/09 (7d) e 03/10 (30d); viés "altista" em soja, farelo e óleo nos dois horizontes — ver Honestidade sobre a defasagem entre esse forecast (calculado com o fechamento de 03/09, que já reflete a queda do óleo) e a leitura qualitativa desta análise
  - system/tributario_watch.toml (lido como referência, não editado) — `atualizado_em` 2026-06-05 em todos os eventos, agora **91 dias sem revisão**
  - Fila de julgamento — carimbada 2026-09-03 no briefing, 7 itens; tratados nesta leitura: `alerta-quebra_resistencia-soja_cbot-2026-09-03`, `alerta-quebra_suporte-oleo_cbot-2026-09-03`, `alerta-quebra_resistencia-farelo_cbot-2026-09-03`, `alerta-quebra_suporte-complexo_soja-2026-09-03`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, `release-nopa-2026-09-03`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`
  - Cruza com [[2026-09-03_leitura-complexo]] (leitura de ontem, que descrevia a primeira sessão de queda sincronizada das três pernas desde 27/08, liderada pelo colapso do óleo, e classificava o crush no menor nível da janela como sinal de fraqueza estrutural ampla — teste que a sessão de hoje confirma parcialmente, mas com uma reviravolta importante: farelo e soja se recuperam, só o óleo continua caindo)
status: ativa
vies: [bull-soja, bull-farelo, bear-oleo_soja]
---

## Visão geral

Hoje é sexta-feira, 04/09/2026, e o briefing mais recente traz o fechamento de quinta-feira
(03/09) — uma sessão que devolve parte do enredo de ontem, mas não todo. Ontem (02/09) as três
pernas do complexo caíram juntas pela primeira vez em duas semanas, lideradas pelo colapso do
óleo (-2,64%). Hoje a soja recuperou **+0,32%** (de 1.310,25 para 1.314,50 USD cts/bushel) e o
farelo recuperou **+1,55%** (de 342,90 para 348,20 USD/short ton) — mas o óleo NÃO acompanhou:
caiu mais **-1,57%** (de 70,64 para 69,53 USD cts/lb), aprofundando a quebra do suporte técnico
de 72,00 identificada ontem. Pela primeira vez nesta sequência de leituras, o complexo não se
move junto nem para cima nem para baixo — ele se divide, com farelo e soja de um lado e óleo do
outro.

Para quem não acompanha o complexo diariamente: a soja em grão vira, na esmagadora (crush),
dois produtos com demandas diferentes — farelo (proteína para ração animal) e óleo (alimentação
humana e biodiesel). O crush margin mede, em dólares por bushel (~27,2 kg de soja), quanto
sobra para quem esmaga depois de vender farelo + óleo e pagar a soja. Dentro desse crush, o
oil share (fatia do valor total que vem do óleo) diz qual dos dois produtos está "mandando" no
resultado econômico da esmagadora — e é justamente aqui que está o fato mais importante do dia:
o oil share **caiu de 50,74% para 49,96%** (indicators, 03/09) — a PRIMEIRA vez em toda a janela
de 14 dias do briefing em que o óleo perde a maioria simples dentro do valor do crush. Na
prática, o mercado está dizendo, pela primeira vez nesta janela, que o farelo (a "sobra" do
esmagamento, tradicionalmente o subproduto menos valorizado) passou a valer, marginalmente, mais
do que o óleo dentro de cada bushel esmagado. O oil-meal spread (valor do óleo menos valor do
farelo, em USD/bushel) confirma com força: virou **negativo pela primeira vez na janela**, em
-0,0121 USD/bushel (03/09), ante +0,2266 (02/09) — uma queda de -0,2387 em um único pregão.

O outro fato estrutural do dia, e talvez o mais relevante para quem opera o spread Far/Soj, é
que os dois índices sintéticos que ficaram TRAVADOS durante toda a janela de 14 dias — o ISF
(Índice de Sobra de Farelo, travado em 80/100 desde o início da janela) e o ISO (Índice de
Suporte do Óleo, travado em 100/100) — finalmente se moveram, e se moveram JUNTOS, na mesma
direção qualitativa. O ISF caiu de 80 para **60/100** (indicators, 03/09: "sobra relevante,
3 de 5 condições" — antes era "forte pressão baixista, 4 de 5 condições") e o ISO caiu de 100
para **80/100** ("óleo domina o crush, 4 de 5 condições" — antes 5 de 5). Mecanicamente, isso
significa que uma das condições estruturais que mediam pressão baixista no farelo deixou de se
verificar, e uma das condições que sustentavam o domínio do óleo também deixou de se verificar —
o candidato mais óbvio para as duas mudanças é justamente o cruzamento do oil share abaixo de
50%, que é tipicamente uma das variáveis que compõe os dois índices. O ratio Far/Soj (farelo
relativo à soja) também colaborou: subiu de 78,51% para **79,47%** (indicators, 03/09), a
primeira alta depois de quatro sessões seguidas de queda — ainda abaixo do patamar de 80% que
separa a zona "abundante" da zona intermediária, mas a mais próxima do cruzamento em toda a
janela.

Em resumo: ontem o mercado vendeu o complexo inteiro; hoje ele COMPROU farelo e soja de volta,
mas continuou vendendo óleo — e fez isso com força suficiente para finalmente mexer os
indicadores estruturais que vinham congelados havia duas semanas. **Leitura de uma linha**: o
pivô do complexo deixou de ser "soja puxando tudo junto" e passou a ser a divergência
farelo-vs-óleo dentro do próprio crush — o farelo (maior conviccao do dia) está sendo
repriced para cima em relação ao óleo, tanto em preço absoluto quanto nos índices estruturais, e
o nível de confiança sobe de médio para **médio-alto** no farelo especificamente, mas o óleo
entra em uma zona de maior incerteza técnica (suporte quebrado há dois dias, sem reação) que
pede cautela em qualquer leitura direcional isolada nele.

## Soja

**Viés: bull, moderado — retoma a alta depois do único dia de recuo da janela, folga sobre o
rompimento técnico volta a crescer, mas o câmbio segue corroendo o ganho em reais.**

O que sustenta a tese:

- **Recuperação confirma o rompimento como estrutural, não como evento isolado.** Soja CBOT
  fechou em 1.314,50 USD cts/bushel em 03/09/2026 (CME CBOT), 11,4% acima da resistência de
  1.180,00 monitorada pela fila (`alerta-quebra_resistencia-soja_cbot-2026-09-03`) — folga maior
  que os 10,9% de ontem, recuperando o espaço perdido no único pregão de queda desta janela. O
  mecanismo: depois de uma queda de -0,68% (02/09), uma alta de +0,32% no dia seguinte, mesmo
  que modesta, é o tipo de comportamento que confirma que o recuo de ontem foi realização de
  lucro pontual e não o início de uma reversão de tendência — o preço não "seguiu caindo" depois
  do primeiro sinal de fraqueza.
- **Volume da sessão de hoje segue relevante, embora um pouco menor.** 158.286 contratos em
  03/09, ante 161.746 em 02/09 (CME CBOT) — volume elevado tanto na queda de ontem quanto na
  recuperação de hoje é consistente com um mercado ainda ativamente repreciando a tese, não com
  um ativo entediado lateralizando.
- **Curva futura segue em contango crescente e ligeiramente mais esticada.** Nov/26 (X26,
  contrato-base) 1.314,50 → jan/27 (F27) 1.330,00 → mar/27 (H27) 1.335,25 → mai/27 (K27)
  1.340,25 → jul/27 (N27) 1.341,75 (CME CBOT, 03/09) — a distância entre o contrato-base e o
  mais distante (N27) é de +2,08%, levemente acima do +1,89% implícito na curva de ontem (K27
  1.333,50 sobre X26 1.308,75) — o mercado segue precificando prêmio para entregas futuras, sem
  sinal de desmonte da estrutura de alta.
- **Físico brasileiro caiu, mas menos que o papel em termos absolutos — o basis segue alargado
  frente ao início da janela.** CEPEA/ESALQ Soja Paranaguá (via NAG) fechou 03/09 em R$
  160,14/saca, -0,53% sobre 02/09 (160,99), enquanto a paridade CBOT-implícita em reais também
  recuou, -0,28% (de R$ 148,11 para R$ 147,69/saca, indicators — CBOT 1.314,50 × USD/BRL
  5,0962). O basis (físico menos paridade) ficou em **R$ 12,45/saca (8,43%)**, ligeiramente
  menor que os R$ 12,88/saca (8,70%) de ontem, mas ainda um nível elevado frente ao início da
  janela — o mercado físico exportador segue precificando um prêmio relevante sobre o CBOT puro.

**O que invalida / risco:**

- **Câmbio: quinta sessão seguida de valorização do real, agora o fator que mais corrói o ganho
  em reais.** USD/BRL fechou 03/09 em 5,0962 (BCB PTAX), -0,61% sobre 02/09 (5,1273) — a quinta
  queda seguida (5,2005 em 28/08 → 5,1816 em 31/08 → 5,1570 em 01/09 → 5,1273 em 02/09 → 5,0962
  em 03/09), acumulando **-2,01%** em cinco pregões. O mecanismo: hoje a soja em dólar subiu
  +0,32%, mas a paridade em reais caiu -0,28% — ou seja, a valorização cambial mais do que
  neutralizou o ganho em dólar. Para o produtor brasileiro vendendo em reais, a alta em Chicago
  desta sessão simplesmente não existiu; o que existiu foi uma perda cambial de -0,61% que
  superou o ganho em CBOT. Esse é o quarto pregão consecutivo (contando desde 01/09) em que o
  câmbio trabalha contra o ganho em dólar, e a magnitude está aumentando.
- **O COT segue cego para toda a janela de alta-queda-alta das últimas seis sessões.** O corte
  de 25/08/2026 (Commodity Futures Trading Commission) — ainda o mais recente — mostrava managed
  money com net long de 200.679 contratos, mas não enxerga nada entre 27/08 e 03/09. O hiato
  chegou a 9 dias corridos frente ao fechamento de hoje (10 dias frente à data de calendário de
  04/09). O próximo corte (posições de terça 01/09, publicação estimada por volta de sexta 04/09
  pelo calendário semanal do CFTC — inferência, não confirmada no briefing) ainda vai revelar
  apenas o posicionamento até a véspera da sequência recente, não a reação dos fundos a ela.
- **O crush margin segue comprimido, embora tenha se estabilizado perto do piso.** Fechou em
  US$ 2,1637/bushel (03/09), -2,17% sobre os US$ 2,2117 de ontem — a QUARTA sessão seguida
  abaixo do referencial de US$ 2,50 monitorado pela fila
  (`alerta-quebra_suporte-complexo_soja-2026-09-03`) e um novo mínimo da janela. Isso continua
  sendo um freio de médio prazo: se esmagadoras enfrentam margem cada vez mais apertada, podem
  reduzir ritmo de moagem, reduzindo a demanda física por soja — mas note que a compressão de
  hoje tem uma causa mais específica (queda do óleo, ver seção Óleo) do que um sinal amplo contra
  a soja.
- **Nível técnico a vigiar:** um fechamento de volta abaixo de 1.180 desfaria o rompimento; a
  distância de segurança (11,4%) voltou a crescer e segue confortável.

**Leitura operacional:** a recuperação de hoje é um argumento a favor de quem está comprado no
rompimento — o teste da sessão de ontem foi superado sem desdobramento técnico negativo, e o
volume elevado em ambas as direções (queda e alta) sugere que o mercado está ativamente validando
o novo patamar, não apenas deixando o preço "flutuar" sem convicção. Para quem pensa no lado
vendido, a soja isoladamente não oferece hoje nenhum gatilho técnico novo — a tese de reversão
segue sem confirmação. O ponto mais acionável do dia, no entanto, está no câmbio: para quem opera
com referência em reais (venda física, hedge cambial), a dissociação entre CBOT em alta e
paridade em reais em queda é o quarto evento consecutivo do tipo, e já não pode ser tratada como
ruído pontual — vale considerar proteção cambial separada da proteção de preço em dólar,
especialmente se a Selic (0,05166% a.a., estável, BCB PTAX) continuar sustentando o carry que
atrai fluxo para o real.

## Farelo

**Viés: bull, forte — maior alta absoluta do complexo hoje, ratio Far/Soj rompe a sequência de
queda, e o ISF (índice estrutural) se move pela primeira vez em 14 dias na direção de menos
pressão baixista.**

O que sustenta a tese (na fita):

- **Maior variação positiva do complexo hoje, e com folga técnica em expansão.** Farelo CBOT
  fechou em 348,20 USD/short ton em 03/09/2026, +1,55% sobre 02/09 (342,90) — a maior alta
  percentual entre as três pernas nesta sessão (soja +0,32%, óleo -1,57%). A folga sobre a
  resistência de 325,00 (`alerta-quebra_resistencia-farelo_cbot-2026-09-03`) subiu de 5,5% ontem
  para **7,14%** hoje — a maior distância de segurança desde o dia do rompimento inicial.
- **Curva futura segue em contango crescente e mais esticada.** Set/26 (U26) 345,10 → out/26
  (V26, contrato-base) 348,20 → dez/26 (Z26) 355,20 → jan/27 (F27) 357,80 → mar/27 (H27) 358,90
  → mai/27 (K27) 359,60 — prêmio de +3,28% entre o contrato-base e o mais distante (K27), maior
  que o +2,66% implícito na curva de ontem — a estrutura de firmeza se fortaleceu junto com o
  preço à vista.
- **Físico brasileiro permanece congelado no patamar mais alto, sem repasse de queda nem de
  alta.** Farelo MT/IMEA (NAG) em R$ 1.795,68/ton e Rondonópolis/MT em R$ 1.900,00/ton, ambos
  congelados desde 31/08 — o físico local simplesmente não reagiu a nenhuma das últimas três
  sessões do CBOT (queda de ontem, alta de hoje), reforçando que o dado físico brasileiro está,
  no momento, mais atrelado à atualização da fonte do que ao movimento diário do papel.

O que finalmente começa a convergir (o desenvolvimento mais importante do dia para esta perna):

- **O ratio Far/Soj subiu pela primeira vez depois de quatro sessões seguidas de queda.** Fechou
  em 79,47% em 03/09 (indicators), acima dos 78,51% de ontem — a primeira alta desde 27/08. O
  mecanismo: farelo subiu +1,55% no dia, soja subiu apenas +0,32% — como o ratio mede farelo
  relativo à soja, o farelo subindo PROPORCIONALMENTE MAIS que a soja empurra o ratio para cima.
  Ainda está abaixo do patamar de 80% que separa a zona "abundante" (formula do indicador:
  <80% abundante, >=87% apertado) da zona intermediária, mas é o valor mais próximo do
  cruzamento em toda a janela de 14 dias — e quebra, pela primeira vez, o padrão descrito na
  leitura de ontem de que "o ratio cai independentemente da direção do board".
- **O ISF (Índice de Sobra de Farelo) caiu de 80 para 60/100 — a primeira mudança em toda a
  janela.** A descrição do próprio indicador passou de "forte pressão baixista no farelo (4 de 5
  condições)" para "sobra relevante (3 de 5 condições)" (indicators, 03/09) — uma das quatro
  condições estruturais que apontavam excesso de oferta de farelo deixou de se verificar. Isso
  não inverte a tese de fundo (o índice ainda aponta sobra, só que menos severa), mas é a
  primeira evidência mensurável, fora do preço bruto, de que a pressão baixista estrutural sobre
  o farelo está perdendo uma de suas pernas de sustentação.
- **Prêmio de exportação em Paranaguá segue congelado em +0,12 USD/short ton desde 24/08/2026**
  — agora 10 dias corridos sem se mexer neste dump (11 até hoje, 04/09), atravessando quedas e
  altas do board sem reação — mesma ressalva de sempre sobre limitação da fonte NAG.

**Trata a fila `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
(novamente marcada 🔴 VENCIDA no briefing de hoje):** a tese original de 11/06/2026 previa
convergência do ratio Far/Soj para a zona 80-87% ("apertado") num horizonte de dias (D+7). Essa
janela venceu há semanas sem convergência — mas a sessão de hoje é a primeira, desde então, em
que o ratio efetivamente se move NA DIREÇÃO da tese original (para cima), ainda que sem cruzar o
patamar. São **85 dias corridos** desde o alerta original (11/06 a 04/09). Mantendo o registro já
feito em [[2026-09-03_leitura-complexo]] e leituras anteriores: a tese segue "revisada, não
encerrada" — o preço absoluto do farelo subiu bastante desde junho (~303,60 USD/sht em 10/06
para 348,20 hoje, +14,7%), e agora, pela primeira vez, o ratio relativo também dá um passo na
direção certa, mesmo que pequeno. **A fila também traz a revisão D+90 da mesma tese
(`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`), descrita no briefing como
vencendo "em 6d" (a partir de 03/09) — a partir de hoje (04/09), faltam 5 dias corridos, com
vencimento em 2026-09-09.** Com o movimento de hoje (ratio subindo, ISF aliviando), a leitura
de hoje é menos cética do que a de ontem quanto à chance de uma virada relevante a tempo do D+90,
mas ainda é cedo para chamar de convergência — uma sessão não desfaz quatro de queda.

**O que invalida / risco:** o movimento de hoje é o primeiro na direção da convergência, mas uma
única sessão de alta do ratio, depois de quatro seguidas de queda, ainda não permite declarar
reversão de tendência — o padrão "farelo sistematicamente mais fraco que a soja" só será
efetivamente desmentido se a alta do ratio se repetir por mais sessões. Se o ratio voltar a cair
amanhã, hoje deve ser tratado como um dia de reversão técnica pontual dentro de uma tendência de
compressão ainda maior, não como o início de uma nova tendência.

**Leitura operacional:** o rompimento técnico direcional em farelo se fortalece e sustenta
posições compradas simples com folga técnica crescente (7,14% sobre a resistência). Para quem
opera o spread Far/Soj (long farelo / short soja apostando em reversão do ratio), a sessão de
hoje é o primeiro sinal concreto, em duas semanas, de que a entrada pode estar se aproximando —
mas ainda não é confirmação: o ideal é aguardar pelo menos mais uma ou duas sessões de ratio em
alta, ou um cruzamento efetivo acima de 80%, antes de montar posição de tamanho relevante, dado
que a revisão D+7 já venceu sem sucesso uma vez e a D+90 está a apenas 5 dias.

## Óleo

**Viés: bear, moderado a forte — segunda sessão seguida de queda abaixo do suporte de 72,00, e
agora com confirmação estrutural: oil share cruza abaixo de 50%, oil-meal spread vira negativo e
o ISO (índice de suporte) recua pela primeira vez na janela.**

O que sustenta o lado vendido / cético:

- **Segunda queda consecutiva, ainda sem reação técnica.** Óleo CBOT fechou em 69,53 USD cts/lb
  em 03/09/2026, -1,57% sobre 02/09 (70,64) — a queda de ontem (-2,64%) já havia quebrado o
  suporte de 72,00; hoje o preço não tentou reconquistá-lo, e a mínima do dia (68,84) ficou ainda
  mais baixa que a mínima de ontem (70,45), aprofundando o novo patamar. Diferente de ontem, a
  fila NÃO disparou um alerta específico de "movimento forte" hoje — a queda de -1,57% é
  relevante, mas não do tamanho da de ontem — o que é consistente com uma perna que já quebrou o
  suporte e agora consolida abaixo dele, em vez de continuar em colapso acelerado.
- **Oil share cruzou abaixo de 50% pela primeira vez em toda a janela de 14 dias.** Fechou em
  49,96% em 03/09 (indicators: valor óleo 7,65 / total 15,31), ante 50,74% ontem — em toda a
  janela anterior (desde pelo menos 27/08) o oil share sempre ficou acima de 50%, ou seja, o óleo
  sempre foi a fatia majoritária do valor do crush. Hoje, pela primeira vez, essa maioria se
  perdeu — um sinal estrutural de que o mercado está reprecificando o valor relativo dos dois
  produtos dentro do crush, não apenas o preço absoluto do óleo isoladamente.
- **O oil-meal spread (valor do óleo menos valor do farelo dentro do crush) virou negativo pela
  primeira vez na janela.** Caiu de +0,2266 (02/09) para **-0,0121 USD/bushel (03/09)** — uma
  queda de -0,2387 em uma única sessão, cruzando de território positivo (óleo "vencendo" o
  farelo) para território negativo (farelo levemente à frente). O mecanismo: como o spread é a
  diferença de valor entre os dois produtos dentro do mesmo bushel esmagado, e o farelo subiu
  enquanto o óleo caiu, o spread não apenas comprimiu — inverteu de sinal. É a mesma dinâmica que
  derruba o oil share, vista por outro ângulo.
- **O ISO (Índice de Suporte do Óleo) caiu de 100 para 80/100 — primeira mudança em toda a
  janela.** A descrição passou de "óleo domina o crush (5 de 5 condições)" para "óleo domina o
  crush (4 de 5 condições)" (indicators, 03/09) — uma das cinco condições estruturais que
  sustentavam o predomínio do óleo deixou de se verificar, com grande probabilidade o próprio
  cruzamento do oil share abaixo de 50%. O índice ainda aponta domínio do óleo (4 de 5 ainda é
  maioria), mas a mudança quebra duas semanas de estabilidade total.

O que ainda sustenta o lado comprado / a cautela contra vender:

- **A margem de biodiesel americana ficou praticamente estável, não deteriorou.** Margem de
  1,7508 USD/galão em 03/09, ante 1,7492 em 02/09 (indicators) — variação de apenas +0,09%, bem
  mais modesta que o salto de +7,8% de ontem. A receita caiu -1,04% (de 7,8472 para 7,7656
  USD/galão, puxada pela queda do heating oil: HO fechou 03/09 em 4,6006 USD/galão via CME NYMEX
  HO=F, -1,74% sobre 4,6822 ontem) e o custo do óleo caiu -1,57% (de 5,298 para 5,2147
  USD/galão) — desta vez as duas pontas se moveram de forma mais proporcional do que ontem, sem
  o descolamento que then favoreceu tanto a margem. Ainda assim, a margem não piorou, o que
  segue sendo um amortecedor: não há sinal, pelo lado da demanda de biodiesel americana, de que a
  queda do óleo esteja sendo puxada por deterioração de margem do blender.
- **O RIN D4 (crédito de biocombustível, EPA) segue estável.** 1,5×RIN = 2,11 USD/galão
  implícito no cálculo de receita tanto em 02/09 quanto em 03/09 (indicators) — o arcabouço
  regulatório (EPA RFS 2026/2027, vigente desde 15/06/2026) segue intacto e não contribui para a
  queda de hoje.
- **Curva futura recupera o contango pleno, desfazendo a backwardation observada ontem.** Out/26
  (V26, contrato-base) 69,53 → dez/26 (Z26) 70,00 → jan/27 (F27) 70,16 → mar/27 (H27) 70,29 →
  mai/27 (K27) 70,34 (CME CBOT, 03/09) — sequência estritamente crescente, sem nenhum vencimento
  próximo mais caro que o contrato-base (o dump de hoje não traz cotação separada de set/26 para
  óleo, então a comparação direta com o U26 71,05 de ontem não é possível, mas a curva a partir
  do contrato-base está de volta ao formato normal de contango). Isso é um sinal técnico
  levemente positivo: o mercado não está descontando o vencimento mais próximo com mais força que
  os distantes, o que seria o padrão típico de um colapso mais estrutural.
- **Catalisador regulatório (Danantara) segue pendente de confirmação, não invalidado.** O
  marco-alvo de assunção plena da centralização da exportação de palma pela Indonésia
  (`DANANTARA-INDONESIA`, tributario_watch.toml) era 01/09/2026 — já passou há três dias — mas
  nenhuma notícia neste dump confirma execução real. Segue como catalisador de alta represado.

**O que invalida / risco:** para o lado vendido, a estabilidade da margem de biodiesel e o RIN D4
inalterado são os principais contra-argumentos — nada na cadeia regulatória americana está
piorando a demanda por óleo; a queda de hoje parece mais uma reprecificação relativa dentro do
complexo (farelo ganhando espaço) do que uma deterioração fundamentalista específica do óleo. Se
o oil share voltar a subir acima de 50% e o oil-meal spread voltar a território positivo nas
próximas sessões, a leitura bear de hoje perde a maior parte de sua sustentação estrutural. Para
o lado comprado (quem ainda vê o óleo como o pivô de alta do complexo, como em leituras de semanas
anteriores), o nível a vigiar é se o preço consegue estabilizar acima de 68,84 (mínima de hoje) —
um novo fechamento abaixo desse nível, sem reação, reforçaria um padrão de fraqueza técnica mais
persistente.

**Leitura operacional:** a sessão de hoje consolida, em vez de reverter, a quebra técnica de
ontem — mas agora com um lastro estrutural mais sólido (oil share <50%, oil-meal spread negativo,
ISO caindo), o que muda a qualidade do sinal: já não é apenas uma quebra de suporte técnico
isolada, é uma quebra acompanhada de evidência de realocação real de valor dentro do crush. Para
quem opera direcional, isso é um argumento mais forte a favor do lado vendido do que a quebra de
ontem sozinha — ainda assim, o tamanho de posição deveria respeitar o fato de que a margem de
biodiesel não está deteriorando e o RIN segue firme, então o cenário mais provável continua sendo
uma correção relativa dentro do complexo, não uma tendência de baixa estrutural isolada de longo
prazo no óleo. Para quem opera o crush/oil share diretamente, hoje é o primeiro dia em que vale a
pena considerar montar ou reforçar uma posição que se beneficie do farelo ganhando espaço sobre
o óleo dentro do crush (long farelo / short óleo em termos de valor relativo), já que os dois
indicadores estruturais (ISF e ISO) confirmam, pela primeira vez juntos, essa direção.

## Spreads e crush (leitura de complexo)

A leitura de hoje é a mais rica da janela em termos de mudança estrutural, mesmo com movimentos
de preço absoluto mais moderados que os de dias anteriores. O oil share caiu de 50,74% (02/09)
para **49,96% (03/09)**, cruzando abaixo de 50% pela primeira vez desde o início da janela de 14
dias — ou seja, o óleo perdeu a maioria simples do valor do crush pela primeira vez. O oil-meal
spread confirma com mais força ainda: virou negativo (-0,0121 USD/bushel), revertendo de +0,2266
em apenas uma sessão. Ao mesmo tempo, o ratio Far/Soj SUBIU (78,51% → 79,47%) — o oposto exato do
padrão de ontem, quando farelo e óleo perderam valor relativo juntos porque a soja caiu menos que
os dois. Hoje farelo ganhou valor relativo (ratio sobe) enquanto óleo perdeu (oil share cai) — os
dois produtos estão, pela primeira vez nesta janela, se movendo em direções relativas opostas ao
mesmo tempo, o que só é aritmeticamente possível porque o farelo subiu proporcionalmente mais que
a soja (+1,55% vs +0,32%) enquanto o óleo caiu em termos absolutos (-1,57%). Essa é a peça central
da leitura de hoje: não é mais "o complexo sobe" ou "o complexo cai" junto — é uma realocação de
valor DE DENTRO do crush, do óleo para o farelo.

O crush margin sintetiza parcialmente esse desequilíbrio, mas de forma enganosa se lida
isoladamente: US$ 2,1637/bushel (03/09), -2,17% sobre os US$ 2,2117 de ontem, um novo mínimo da
janela e a quarta sessão seguida abaixo do referencial de US$ 2,50
(`alerta-quebra_suporte-complexo_soja-2026-09-03`). À primeira vista isso parece confirmar a
narrativa de "crush cada vez mais fraco", mas a composição interna conta uma história mais
específica: o farelo SUBIU (contribuindo positivamente para o crush) enquanto o óleo CAIU MAIS
que o suficiente para compensar esse ganho e ainda puxar o total para baixo. Ou seja, o crush
margin comprimido de hoje não é sintoma de fraqueza ampla e simultânea de farelo e óleo (como
parecia ser o caso ontem) — é o resultado líquido de uma perna forte (farelo) sendo mais do que
neutralizada por uma perna fraca (óleo). Essa distinção importa para quem monitora o crush como
sinal de saúde do esmagamento: o esmagador ainda está espremido, mas a origem do aperto mudou de
"soja cara demais" (leitura de semanas atrás) para "óleo fraco demais" (leitura de hoje e de
ontem).

Os índices sintéticos, que passaram toda a janela travados (ISF em 80, ISO em 100), finalmente se
moveram — e se moveram JUNTOS, na mesma direção qualitativa (menos pressão baixista no farelo,
menos domínio do óleo). ISF caiu para 60/100 (3 de 5 condições, ante 4 de 5) e ISO caiu para
80/100 (4 de 5 condições, ante 5 de 5). Essa sincronia reforça a leitura de que existe uma causa
comum por trás das duas mudanças — mais provavelmente o cruzamento do oil share abaixo de 50%,
que plausivelmente é uma das condições compartilhadas pelos dois índices (o briefing não detalha
as fórmulas exatas de cada condição, então esta é uma inferência razoável, não um fato
confirmado — ver Honestidade).

Para quem opera o crush diretamente: a compressão de hoje tem uma leitura mais construtiva do que
a de ontem, porque a origem é identificável e específica (óleo), não uma fraqueza difusa em toda
a cadeia. Para quem opera o spread Far/Soj, a sessão de hoje é o desenvolvimento mais relevante
desde o início do monitoramento da tese de convergência (11/06/2026) — o ratio subiu pela
primeira vez em quatro sessões, e o índice estrutural (ISF) confirma que uma das pernas da tese de
"farelo abundante" está perdendo força. Ainda não é motivo para declarar a tese de convergência
vencida a favor do reversal, mas é a primeira evidência concreta, em quase três meses, de que a
direção pode estar começando a virar — com a revisão D+90 vencendo em apenas 5 dias (09/09), o
timing não poderia ser mais oportuno para acompanhar de perto as próximas sessões.

## Lente fiscal/regulatoria BR

Antes de fechar qualquer tese de preço BR, os vetores tributários/regulatórios vivos que pesam
no complexo — todos do `system/tributario_watch.toml`, cujo carimbo mais recente
(`atualizado_em`) em TODOS os eventos é 2026-06-05, ou seja, **91 dias sem revisão** (mais um dia
de defasagem acumulada desde a leitura de ontem):

- **MP 1.363/2026** (id `MP-1363-2026`, subvenção diesel fóssil R$ 1,12/L, vigente até
  31/12/2026): barateia o diesel fóssil no mix B15, reduzindo a competitividade relativa do
  biodiesel e a demanda doméstica por óleo de soja — vetor de baixa estrutural para óleo, sem
  mudança de status. Esse vetor (BR, estrutural) não deve ser confundido com a margem de
  biodiesel AMERICANA (referência EUA) que hoje ficou praticamente estável — são mercados e
  mecanismos diferentes.
- **B16 (id `B16-CNPE-2026`, elevação da mistura de biodiesel para 16%)** segue "adiado" —
  resultado dos testes técnicos esperado por volta de novembro/2026. Upside represado (~436 mil
  toneladas de demanda potencial adicional de óleo), não corrente — mas relevante lembrar que,
  se o farelo continuar ganhando espaço relativo dentro do crush (como hoje), qualquer estímulo
  futuro de demanda por óleo (via B16) teria efeito ainda mais visível sobre o oil share, hoje na
  fronteira dos 50%.
- **Isenção de PIS/Cofins do biodiesel na mistura** (id `PISCOFINS-BIODIESEL-ISENCAO`): o TOML
  registra vigência ATÉ 31/07/2026 — já **35 dias corridos vencida** frente a 04/09/2026, sem
  qualquer registro de prorrogação ou expiração no arquivo.
- **MP 1.358/2026** (subvenção gasolina R$ 0,89/L): vigência registrada até 11/07/2026, agora
  **55 dias corridos vencida**, mesma lacuna de informação sobre renovação.
- **STJ REsp 2.165.276** (id `STJ-RESP-2165276`, crédito de PIS/Cofins sobre soja em biodiesel,
  vigente, direção "alta" para soja/óleo): alívio de custo pontual, não vinculante, sem novidade.
- **EPA RFS 2026/2027** (id `EPA-RFS-2026-2027`, mandato de biocombustível americano, vigente
  desde 15/06/2026, direção "alta" para óleo): sustenta o RIN D4, que hoje ficou estável em
  1,5×RIN = 2,11 USD/galão pelo segundo dia seguido — o arcabouço regulatório continua intacto e
  é parte do motivo pelo qual a margem de biodiesel não deteriorou apesar da queda do óleo.
- **Crédito 45Z** (id `45Z-CLEAN-FUEL`, em tramitação, direção "mista"): sem novidade nesta
  janela.
- **Indonésia — Danantara** (id `DANANTARA-INDONESIA`) e **levy de exportação PMK 9/2026** (id
  `INDONESIA-LEVY-PMK9`): já tratados na seção Óleo. O marco-alvo da Danantara (01/09) já passou
  há três dias sem confirmação de execução no briefing — segue pendente, não invalidado.

## Riscos e eventos próximos

- **Próximo corte CFTC COT** — posições de terça 01/09, publicação estimada por volta de sexta
  04/09 (hoje) pelo calendário semanal do CFTC (inferência, não confirmada no briefing, que ainda
  não trazia o corte na hora do fechamento dos dados usados nesta leitura): se sair hoje, revela
  o posicionamento até a véspera da sequência recente de alta-queda-alta, mas ainda não a reação
  dos fundos à divergência farelo-vs-óleo desta semana — isso só aparecerá no corte seguinte.
- **Revisão D+90 da tese do ratio Far/Soj** (`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`),
  vencendo em **2026-09-09**, daqui a 5 dias — o marco mais importante da próxima semana para
  decidir se a tese de convergência do ratio para a zona 80-87% deve ser encerrada ou mantida, e
  a sessão de hoje (primeira alta do ratio em quatro dias) chega bem a tempo de ser um dado
  relevante para essa decisão.
- **Confirmação (ou não) da centralização plena da exportação de palma pela Danantara** —
  marco-alvo era 01/09, já passou há três dias; vigiar notícia confirmando execução ou, como no
  precedente do B50 indonésio (`INDONESIA-B50`), sinal de atraso.
- **NOPA mensal** (`release-nopa-2026-09-03`): terceiro dia seguido em que a fila sinaliza
  "release novo" sem que o conteúdo (`monthly_status` 0,0 bool, paywall) traga qualquer número
  real de esmagamento americano — o gap de dado de crush americano segue sem solução.
- **USDA WASDE**: ausente da janela há bastante tempo; catalisador potencial de revisão de
  balanço mundial.
- **USDA Crop Progress semanal**: próximo corte normalmente segunda-feira à tarde (horário EUA)
  — atualizaria o dado de 30/08 (12%/46%/9%).
- **Vigência da isenção PIS/Cofins do biodiesel** (35 dias vencida) e **MP 1.358/2026 da
  gasolina** (55 dias vencida) — checar notícia de renovação/expiração antes de assumir qualquer
  tese de custo de combustível BR.
- **Reação do óleo ao nível de 68,84** (mínima de hoje): um fechamento adicional abaixo desse
  nível sem reação técnica reforçaria o padrão de fraqueza persistente; uma reconquista rápida de
  70,00-72,00 esvaziaria parte da leitura bear de hoje e de ontem.
- **Persistência (ou reversão) do cruzamento do oil share abaixo de 50% e do oil-meal spread
  negativo** — se esses dois indicadores voltarem para o território anterior (oil share >50%,
  spread positivo) já na próxima sessão, o movimento de hoje deve ser tratado como um evento
  isolado de um dia; se persistirem por mais sessões, reforça a leitura de realocação estrutural
  de valor dentro do crush.
- **Clima**: previsão de 04/09 (hoje) mostra o núcleo produtor de Mato Grosso seguindo muito
  quente (34-39°C) e sem menção de chuva no boletim (Cuiabá, Sinop, Lucas do Rio Verde, Sorriso,
  Rio Verde/GO), às vésperas da janela de plantio da safra 2026/27, enquanto o Sul (Cascavel/PR,
  Maringá/PR, Passo Fundo/RS) recebe chuva e trovoadas isoladas hoje, contrastando com a condição
  seca de ontem (03/09) nas mesmas estações do Paraná — vigiar se a ausência de chuva prevista no
  núcleo de MT persiste, dado que setembro é o início típico da janela de plantio nessa região.

## Honestidade

- **O oil share cruzando abaixo de 50% e o oil-meal spread virando negativo são leituras
  aritméticas diretas dos números do dump (indicators, 03/09), mas a interpretação de que essas
  mudanças "causaram" a queda simultânea do ISF e do ISO é uma inferência razoável, não um fato
  confirmado no briefing.** O dump não detalha quais são as 5 condições exatas que compõem cada
  índice sintético — apenas o resultado agregado (3/5, 4/5 etc.) e um rótulo qualitativo. Esta
  leitura tratou a coincidência temporal como evidência de causa comum, mas não há confirmação
  explícita da fonte de que o oil share seja, de fato, uma das condições compartilhadas.
- **Os valores de fechamento de 02/09 citados nesta leitura (soja 1.310,25 / óleo 70,64) foram
  reconstituídos a partir do cálculo de indicators (Board Crush), porque o dump de hoje não traz
  as linhas diretas de `cme_cbot` para soja_cbot e oleo_cbot em 02/09 (apenas farelo_cbot e
  heating_oil_cbot aparecem diretamente).** Esses valores diferem dos citados na leitura de ontem
  (1.308,75 / 70,54) — mesmo padrão de revisão pós-pregão já registrado nas honestidades
  anteriores. Nenhum número foi inventado; os valores usados aqui são os que constam do dump mais
  recente disponível nesta leitura, reconciliados via indicators.
- **Heating oil com volume muito baixo hoje (118 contratos), o menor de toda a janela citada
  nas últimas leituras** — mesma ressalva já feita nos dias anteriores (309 e 466 contratos); o
  número merece confirmação em mais sessões antes de ser tratado como sinal robusto,
  especialmente porque a margem de biodiesel depende diretamente desse preço.
- **`noticias_rss` registra "9 mantidos" em 03/09, mas apenas 1 headline aparece com texto
  legível no dump** (soja: FarmProgress, sem conteúdo de mercado relevante) — os outros 8 itens
  "mantidos" não têm headline nem link visíveis nesta leitura. Nenhum conteúdo foi inventado para
  preencher essa lacuna.
- **COT desatualizado, agora com 9 dias corridos de defasagem frente ao fechamento de 03/09 (10
  frente a hoje)** — segue sendo a maior lacuna desta leitura: não sabemos se os fundos já
  reagiram à divergência farelo-vs-óleo desta semana, nem se a alta do ratio de hoje tem qualquer
  eco no posicionamento especulativo.
- **Prêmios de exportação (Paranaguá, farelo e óleo) seguem congelados**, agora 10 dias corridos
  idênticos no dump (24/08 a 03/09, 11 dias até hoje) — atravessando toda a sequência de alta,
  queda e nova divisão do complexo sem se mexer; não dá para saber se reflete mercado físico
  export realmente parado ou limitação de atualização da fonte (NAG).
- **Danantara: marco-alvo atingido no calendário (01/09), agora três dias sem qualquer notícia ou
  dado no briefing confirmando execução real.** Tratado como catalisador pendente de confirmação,
  não como fato consumado.
- **`tributario_watch.toml` sem atualização há 91 dias** — pelo menos dois vetores (isenção
  PIS/Cofins do biodiesel, MP 1.358/2026) já passaram da data de vigência registrada sem nota de
  renovação ou expiração. Tratados como "status desconhecido pós-vigência".
- **NOPA segue inacessível** (paywall) — terceira sessão seguida em que a fila sinaliza "release
  novo" sem que isso traga qualquer número real; tratado explicitamente como falso positivo
  repetido, não como dado novo.
- **USDA WASDE ausente** da janela — nenhuma leitura de balanço mundial oficial atualizado
  disponível.
- **Forecasts estatísticos internos (bandas 7d/30d) geradas em 03/09 já embutem viés "altista"
  nas três pernas, inclusive no óleo** — mas esses forecasts usam MA20+volatilidade+slope sobre o
  fechamento de 03/09 (que já reflete dois dias de queda do óleo) e não incorporam
  qualitativamente a divergência farelo-vs-óleo desta leitura, apenas o nível de preço resultante.
  Tratar como referência estatística de banda, não como leitura fundamentalista independente
  desta análise — em particular, o viés "altista" do forecast de óleo não deve ser lido como
  contradição desta leitura bear de curto prazo; são horizontes e métodos diferentes.
- **Percentil histórico de posicionamento COT não está disponível no briefing** — toda leitura de
  "fundos comprando/vendendo" nesta análise usa variação semana a semana de contratos absolutos,
  não percentil histórico.
- **MPOB (palma Malásia) segue com parser quebrado** — nenhum dado de produção/estoque de palma
  malaia disponível para cruzar com a tese de substituição via Indonésia.
- **BCBA (Argentina) segue sem links de relatório detectados pelo scraper** — nenhum dado de
  safra ou exportação argentina disponível nesta janela.
- **A previsão INMET para 04/09 (hoje) é a primeira desta sequência de leituras disponível
  same-day, mas ainda é previsão meteorológica, não medição de precipitação real** — a leitura
  desta seção trata a ausência de menção a chuva nos boletins de Cuiabá/Sinop/Lucas do Rio
  Verde/Sorriso/Rio Verde-GO como ausência de chuva PREVISTA no boletim, não necessariamente como
  confirmação de que não choveu ou não vai chover — o boletim do INMET usado aqui é qualitativo
  (descrição textual), não uma série numérica de milímetros de precipitação.
- **A inferência de que o oil share e o oil-meal spread negativo compartilham causa com a queda
  do ISF/ISO (ver primeiro item desta seção) é o ponto de maior incerteza qualitativa desta
  leitura** — trata-se da interpretação central do "Visão geral" e da seção "Spreads e crush", e
  vale registrar explicitamente que é uma inferência analítica, não um fato extraído literalmente
  do briefing.
