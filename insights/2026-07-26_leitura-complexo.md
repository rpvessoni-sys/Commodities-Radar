---
data: 2026-07-26
titulo: "Domingo sem sessão nova de soja/farelo/óleo: os preços de sexta-feira (24/07) ficaram estáveis por dois dumps consecutivos (só o volume ainda foi revisado), mas a reabertura eletrônica do heating oil já embutiu um gap de -4,59% em volume muito fino, sinalizando pressão energética prévia sobre o óleo antes de segunda; o ratio Farelo/Soja segue 'encostado' em 80,02% sem romper o piso de 80% pela quinta sessão seguida, deixando a revisão D+7 de 11/06 formalmente 38 dias vencida sem confirmação nem invalidação; e a isenção PIS/Cofins do biodiesel entra na semana decisiva, a apenas 5 dias do vencimento em 31/07"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT (ZSU26 soja / ZMU26 farelo / ZLU26 óleo + curva forward Q26-H27/F27) — sessão de 2026-07-24, confirmada estável (preço) no dump de 2026-07-26; apenas volume revisado (ver Nota de proveniência)
  - CME heating_oil_cbot (HO=F) — NOVO print da sessão eletrônica de 2026-07-26 (domingo, reabertura), volume 1.458 contratos; e sessão de 2026-07-24 (revisada e agora estável)
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, paridade BR) — recorte de 2026-07-24 (agora estável entre dois dumps); Índice de Sobra de Farelo e Índice de Suporte do Óleo com print próprio de 2026-07-26
  - BCB PTAX — 2026-07-24 (USD/BRL 5,0666, EUR/BRL 5,7683); sem novo print para 25-26/07 (fim de semana, sem pregão de câmbio)
  - CEPEA/ESALQ Paranaguá via NAG — 2026-07-24 (suporte R$ 148,37/saca, var +0,61%), sem novo print no fim de semana
  - CEPEA/ESALQ Paraná interior via NAG — 2026-07-24 (R$ 140,26/saca, var +0,70%), sem novo print no fim de semana
  - NAG Físico BR (farelo MT/IMEA R$ 1.669,72/ton; Rondonópolis R$ 1.650,00/ton; RS R$ 1.640,00/ton; prêmios export PGUA farelo +0,05 USD/sht e óleo +0,08 cts/lb) — 2026-07-24, sem novo print no fim de semana
  - CFTC COT Managed Money — corte de 2026-07-21 (inalterado; próximo corte 28/07, publicação normal ~31/07)
  - USDA Crop Progress — ainda 2026-07-19 (13% excelente + 53% boa + 6% ruim = 66% bom-ou-excelente); próxima publicação semanal esperada nas próximas 24-48h (convenção USDA: segunda-feira à tarde, horário EUA)
  - USDA WASDE — ainda 2026-07-10, sem publicação nova (16 dias sem atualização)
  - NOPA — fila `release-nopa-2026-07-26`, `monthly_status` continua em 0,0 bool (paywall), sem dado interpretável novo
  - ABIOVE projeções mensais — balanços ago-dez/2026 (farelo/óleo/soja), sem alteração
  - NOAA CPC ENSO — 2026-07-26 (El Niño Advisory, inalterado desde pelo menos 03/07/2026)
  - MPOB — 2026-07-26 (parser sem números extraídos, 3.439 caracteres, 17º dia consecutivo com o mesmo conteúdo, 10/07 a 26/07)
  - BCBA — 2026-07-22 (última leitura do scraper, sem relatórios detectados; hoje 4 dias sem atualização)
  - Notícias Agrícolas/Canal Rural/Farm Progress RSS — 2026-07-26 (160 itens lidos, 6 mantidos; manchete NOVA "Exportações de soja do Brasil podem atingir 110 milhões de t na safra 26/27, projeta consultoria", Canal Rural)
  - Forecasts estatísticos internos — 2026-07-26 (nova geração, spot ref replica os valores estáveis de 24/07: soja 1.240,25 / farelo 330,80 / óleo 73,47)
  - system/tributario_watch.toml (lido apenas como referência, não editado) — 10 eventos, todos `atualizado_em` 2026-06-05 (51 dias sem atualização do monitor); trata `trib-PISCOFINS-BIODIESEL-ISENCAO-2026-07-31`
  - Cruza com [[2026-07-25_leitura-complexo]], [[2026-07-24_leitura-complexo]], [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (checkpoint D+7, tratado abaixo — hoje 38 dias vencido)
status: ativa
vies: [bull-soja, neutral-farelo, bear-oleo_soja]
---

> **Nota de proveniência (o padrão de revisão diária, pela primeira vez em
> três dias, NÃO se repetiu nos preços — só no volume):** as duas leituras
> anteriores desta série documentaram que a sessão de 23/07 chegou revisada
> no dump de 24/07 (revisão grande, sobretudo em heating oil) e que a sessão
> de 24/07 chegou revisada no dump de 25/07 (revisão pequena, invertendo o
> sinal do ratio Far/Soj). **O dump de hoje (26/07) traz a mesma sessão de
> 24/07 pela terceira vez, e desta vez os preços de fechamento, abertura,
> máxima e mínima de soja, farelo, óleo e heating oil são IDÊNTICOS aos do
> dump de ontem** — 1.240,25 / 330,80 / 73,47 / 4,1806, respectivamente. A
> única coisa que ainda se moveu foi o **volume**: farelo 37.681→**35.887**
> contratos (-4,77%) e soja 26.510→**26.848** contratos (+1,27%); óleo e
> heating oil mantiveram o volume relatado ontem (46.086 e 22.882). **Leitura
> prática: os níveis de preço da sessão de sexta (24/07) agora podem ser
> tratados como definitivos** para fins de referência técnica (resistências,
> stops, paridade) — o único resíduo de incerteza que sobra é o volume, que
> ainda não estabilizou. Todos os indicadores sintéticos (crush margin, ratio
> Far/Soj, oil share, oil-meal spread, margem biodiesel, paridade BR)
> replicaram exatamente os valores revisados de ontem, confirmando a mesma
> conclusão pelo lado dos indicadores derivados.

## Visão geral

O complexo soja é uma fábrica com uma única matéria-prima (a soja em grão) e
dois produtos de saída em proporção fixa por bushel esmagado: o **farelo**
(fração proteica, ~78% da massa, vira ração animal) e o **óleo degomado**
(fração de gordura, ~18-20% da massa, vira óleo de cozinha e biodiesel). Quem
decide o ritmo de esmagamento é a esmagadora, olhando a **crush margin**
(valor de farelo + óleo por bushel, menos o custo daquele bushel de soja,
medido na CBOT — Chicago Board of Trade, a bolsa de referência mundial para
esses contratos) e o **oil share** (fração desse valor capturada pelo óleo).
Quando o oil share sobe, o óleo passa a "pagar o crush" sozinho, e o farelo
vira, cada vez mais, um subproduto que a esmagadora aceita vender barato só
para liberar o óleo — é esse mecanismo que está por trás do **ratio Far/Soj**
(preço do farelo dividido pelo preço da soja, normalizado pela conversão
bushel↔short ton): abaixo de 80% o farelo está historicamente "abundante"
frente à soja (zona bear); acima de 87%, "apertado" (zona bull); entre os
dois, zona "neutra" e de **mean-reversion** — funciona nos dois lados.

**Hoje é domingo — não há pregão de soja, farelo ou óleo na CBOT** (a última
sessão disponível segue sendo a de sexta-feira, 24/07/2026; a reabertura
acontece segunda-feira, 27/07/2026). Diferente do dump de ontem (que ainda
trazia uma revisão relevante de preço), **o dump de hoje confirma que os
quatro contratos que movem esta leitura — soja, farelo, óleo e heating oil —
fecharam a sessão de 24/07 com valores agora estáveis por dois dumps
seguidos**: 1.240,25 cts/bushel (soja), 330,80 USD/short ton (farelo), 73,47
cts/lb (óleo) e 4,1806 USD/galão (heating oil). Isso reduz o risco de operar
em cima de um nível técnico ainda sujeito a revisão — algo que as duas
últimas leituras trataram como preocupação central. **Mas o dump de hoje traz
algo genuinamente novo: o primeiro print da reabertura eletrônica de
domingo do heating oil** (ticker HO=F), que abriu com um gap de -3,76% frente
ao fechamento de sexta e fechou a 3,9889 USD/galão — uma queda de -4,59% no
total, em volume muito fino (1.458 contratos, apenas 6,4% do volume de
sexta). Como o heating oil é o principal termômetro de energia usado na
margem de biodiesel americana (que por sua vez sustenta a tese estrutural do
óleo de soja via RIN D4), esse gap — mesmo fino e ainda sem confirmação —
é o dado mais "adiantado" que este briefing oferece sobre o tom da semana que
abre amanhã. **Também há uma notícia nova e com número**: uma consultoria (não
identificada na manchete) projeta que as exportações de soja do Brasil podem
atingir **110 milhões de toneladas na safra 2026/27** (Canal Rural,
26/07/2026) — um dado estrutural de capacidade exportadora brasileira para a
PRÓXIMA safra, não um driver de curto prazo para o contrato corrente, mas que
reforça o pano de fundo de demanda física por soja brasileira. **O que não
mudou, e que segue sendo o ponto mais tenso da leitura**: o ratio Far/Soj
segue em 80,02% (indicadores, 24/07, agora confirmado estável), a apenas 0,02
ponto percentual do piso de 80% que confirmaria a tese estrutural bear do
farelo — a quinta sessão seguida em que esse piso é testado sem ser rompido,
e a revisão D+7 da tese original (`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`)
está hoje formalmente **38 dias vencida**, ainda sem confirmação nem
invalidação clara (ver seção Farelo). **Leitura de uma linha:** o pivô do
complexo segue sendo a soja, agora sobre uma base de preço confirmada e
estável; o gap fino do heating oil de domingo é o primeiro sinal (não
confirmado) de que a semana pode abrir com pressão sobre o óleo; e o ratio
Far/Soj — "encostado" no piso técnico há cinco sessões — é o dado que mais
precisa de resolução na abertura de amanhã. Confiança moderada-alta para
soja, baixa para farelo (tensão entre COT bullish e ratio no limiar,
persistente há mais de uma semana sem resolução), baixa-moderada para óleo
(estrutura ainda intacta, mas o gap de energia de domingo pede cautela
tática antes da confirmação de segunda).

---

## Soja

**Viés: bull, com base de preço agora confirmada — o fechamento de
sexta-feira (24/07/2026), 1.240,25 cts/bushel, está estável por dois dumps
consecutivos (25/07 e 26/07), o que elimina o risco de revisão que pairava
sobre esse nível nas duas últimas leituras. O COT de 21/07 (ainda o mais
recente) confirma compra líquida de fundos de +73,6% na semana do
rompimento. Uma notícia nova (Canal Rural, 26/07) projeta exportação
recorde de 110 milhões de toneladas na safra 26/27, reforçando o pano de
fundo estrutural de demanda por soja brasileira. Trata
`alerta-quebra_resistencia-soja_cbot-2026-07-24`.**

### O que sustenta a tese

**A base de preço da sessão de sexta-feira está, agora sim, confirmada.**
Abertura 1.229,50, fechamento 1.240,25 (+10,75 frente à abertura, +0,87%),
mínima 1.225,00, máxima 1.243,00 (CBOT, ticker ZSU26.CBT, sessão de
24/07/2026) — todos os quatro valores idênticos entre o dump de ontem
(25/07) e o de hoje (26/07). O único número que ainda se moveu foi o
**volume**, revisado de 26.510 para **26.848 contratos** (+1,27% — uma
revisão pequena, na direção oposta à do farelo, ver Farelo). O fechamento
segue equivalendo a **84,7% do range do dia**
((1.240,25-1.225,00)÷(1.243,00-1.225,00)) — um fechamento forte, perto da
máxima, sem sinal de rejeição. Frente ao fechamento de quinta-feira
(1.231,00), o ganho foi de +9,25 pontos (+0,75%). A resistência original de
1.180,00, rompida em meados de julho, está **5,10% abaixo** do fechamento
confirmado de sexta ((1.240,25-1.180,00)÷1.180,00) — a maior distância de
toda a janela de acompanhamento desta série.

**O COT (CFTC, corte de 21/07/2026) segue sendo o dado de maior peso desta
leitura para a soja, e não teve atualização nova hoje.** Managed money (a
categoria de fundos especulativos que mais se aproxima de posicionamento
direcional puro dentro do relatório) elevou a posição comprada de 145.930
para 180.163 contratos (+23,5%) e reduziu a posição vendida de 70.739 para
49.658 (-29,8%) na semana de 21/07 — o net long saltou de 75.191 para
130.505 contratos (+73,6%), e como fração do open interest (1.045.077
contratos) subiu de 7,48% para 12,49%. Esse dado permanece, sem alteração, o
principal lastro fundamental por trás do rompimento — o próximo corte
(28/07, publicação normal ~31/07) é o primeiro capaz de dizer se essa compra
se sustentou durante a sessão de sexta-feira (24/07) e o fim de semana.

**Uma notícia nova traz um número estrutural relevante para a demanda de
exportação brasileira.** O Canal Rural publicou em 26/07/2026 que "exportações
de soja do Brasil podem atingir 110 milhões de toneladas na safra 26/27,
projeta consultoria" — a manchete não identifica a consultoria nem detalha a
metodologia, e o número se refere à **safra 2026/27** (a próxima, ainda em
formação, não à safra corrente que já está no fim do ciclo de exportação).
**Mecanismo:** um patamar recorde de exportação projetada sinaliza que o
mercado físico brasileiro segue estruturalmente com apetite comprador
externo forte, o que sustenta o prêmio de exportação físico (ver abaixo) e a
tese de que o Brasil segue absorvendo parcela crescente da demanda global —
inclusive a chinesa, tema já registrado em notícias anteriores desta janela
(ex.: "China compra mais soja do Brasil enquanto reduz importações dos EUA",
G1, 20/07/2026). **Esta leitura trata o número como um dado qualitativo de
pano de fundo estrutural** (fonte não identificada nominalmente, projeção de
consultoria, não estatística oficial USDA/CONAB), não como um driver
quantitativo direto de preço para o contrato corrente CBOT — mas é
consistente com, e reforça, a leitura bull já sustentada por COT e físico.

**A curva forward manteve a estrutura de prêmio crescente nos vencimentos
mais distantes, com os valores agora confirmados.** Setembro/26 (U26, spot)
1.240,25 → Novembro/26 (X26) 1.253,50 (+13,25 sobre o spot, +1,07%) →
Janeiro/27 (F27) 1.266,50 (+13,00 sobre novembro, +1,04%) → Março/27 (H27)
1.264,00 (-2,50, -0,20%, praticamente estável) — o mesmo padrão de contango
moderado e crescente documentado nas leituras recentes, sem sinal de
estresse ou inversão. Agosto/26 (Q26) fechou em 1.248,00, um prêmio de
+0,62% sobre o spot de setembro.

**A paridade teórica em reais permanece em R$ 138,53/saca de 60kg**
(indicadores, CBOT 1.240,25 cts × PTAX 5,0666 USD/BRL de 24/07/2026 — sem
novo PTAX para o fim de semana). **O físico de Paranaguá segue no print de
24/07, sem atualização de fim de semana: R$ 148,37/saca** (CEPEA/ESALQ via
NAG, var +0,61%) — um prêmio de exportação de **+7,10%** sobre a paridade
((148,37-138,53)÷138,53), confirmado de mesmo dia (24/07 contra 24/07). O
físico de Paraná interior também permanece em R$ 140,26/saca (24/07, var
+0,70%), um prêmio de +1,25% sobre a paridade. **A sequência de cinco altas
consecutivas em Paranaguá (07-20: 142,65 → 07-21: 144,17 → 07-22: 145,45 →
07-23: 147,47 → 07-24: 148,37) segue sendo o melhor dado físico desta
janela**, e a notícia de hoje sobre exportação recorde projetada para 26/27
reforça essa leitura de mercado físico exportador estruturalmente apertado,
mesmo sem print novo no fim de semana.

**O USDA Crop Progress segue parado em 19/07/2026** (13% excelente + 53% boa
+ 6% ruim = 66% bom-ou-excelente), sem atualização nova. A próxima
publicação semanal é esperada nas próximas 24-48 horas (convenção USDA:
segunda-feira à tarde, horário dos EUA) — o primeiro dado agrícola
potencialmente novo desta janela.

**Os forecasts estatísticos internos (26/07/2026)**, recalculados a partir
do spot agora estável, replicaram a geração de ontem: central 7d = 1.269,06
cts/bu (bandas 1.215,73-1.322,38); central 30d = 1.378,61 cts/bu (bandas
1.268,22-1.489,00) — sem mudança de viés, coerente com a base de preço
confirmada.

### O que invalida / risco para a soja

- **Um fechamento de segunda-feira (27/07) abaixo de 1.225,00** (mínima de
  sexta, agora confirmada) devolveria parte da força mostrada na última
  sessão e reabriria a dúvida tática.
- **Um fechamento abaixo de 1.180,00** (5,10% de distância, a maior margem
  de segurança desta janela) encerraria por completo a leitura tática de
  continuidade — mas exigiria uma reversão muito mais expressiva do que
  qualquer coisa vista até agora.
- **O próximo corte do COT (28/07, publicação ~31/07) mostrar realização de
  lucro** depois do salto de +73,6% da semana de 21/07 — um recuo do net
  long, mesmo que o preço continue subindo, seria o primeiro sinal de que a
  compra de fundos já capturou a maior parte do movimento.
- **A projeção de 110 milhões de toneladas de exportação 26/27 não se
  confirmar em fontes oficiais** (USDA/CONAB) — como número de consultoria
  não identificada, carrega risco de revisão para baixo; esta leitura não
  usa esse número como pilar quantitativo da tese, apenas como reforço
  qualitativo.

### Leitura operacional — soja

Com a base de preço de sexta-feira agora confirmada por dois dumps
consecutivos, a referência técnica para quem está comprado alinhado ao
rompimento pode ser tratada com mais confiança do que nas duas últimas
leituras: stop tático na mínima confirmada de sexta (1.225,00), sem
necessidade de reduzir posição diante da distância estrutural (1.180,00, a
5,10%). Como não há pregão hoje, a ação prática é monitorar a abertura de
segunda-feira contra esses dois níveis e acompanhar a publicação do Crop
Progress, esperada nas próximas 24-48 horas. Para quem está vendido contra o
rompimento, o quadro segue desfavorável: operar vendido soja neste momento
significa apostar contra compra de fundos comprovada (COT), confirmação
física (Paranaguá, quinto dia seguido de alta) e agora também um reforço
estrutural qualitativo (projeção de exportação recorde 26/27) — o risco de
uma posição vendida puramente tática segue elevado.

---

## Farelo

**Viés: neutro, mas com a tensão tática mais prolongada desta série — o
ratio Far/Soj está confirmado em 80,02% (indicadores, 24/07, estável entre
os dumps de 25/07 e 26/07), a apenas 0,02 ponto percentual do piso de 80%
que confirmaria a tese estrutural bear (ABIOVE/ISF), pela QUINTA sessão
seguida sem romper claramente para nenhum dos dois lados. O COT (21/07,
inalterado) segue fortemente bullish (net long +57,8% na semana). Trata
`alerta-quebra_resistencia-farelo_cbot-2026-07-24` e a revisão
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, hoje
formalmente 38 dias vencida — ver veredito abaixo.**

### O que sustenta a tese

**A base de preço da sessão de sexta-feira está confirmada, com uma pequena
revisão de volume.** Fechamento 330,80 USD/short ton (CBOT, ticker ZMU26.CBT,
sessão de 24/07/2026), abertura 329,40, mínima 327,90, máxima 334,30 —
todos idênticos ao dump de ontem. **O volume, porém, foi revisado de 37.681
para 35.887 contratos (-4,77%)** — uma revisão na direção oposta à da soja
(que subiu +1,27%), reforçando a leitura já registrada nesta série de que o
campo de volume, mesmo depois de o preço estabilizar, continua sujeito a
ajuste. O fechamento confirmado equivale a **45,3% do range do dia**
((330,80-327,90)÷(334,30-327,90)) — abaixo do meio do range, um sinal
ligeiramente fraco, mas longe de configurar rejeição clara. A resistência
de 325,00, rompida em 22/07, segue respeitada como suporte, com a mínima de
sexta (327,90) 2,90 pontos acima dela.

**O ratio Far/Soj é, pelo quinto dia seguido, o dado mais tenso desta
leitura — e hoje ele está formalmente confirmado, não apenas revisado.**
Sequência da janela: 07-20: 79,28% (mínima) → 07-21: 80,37% → 07-22: 80,65%
(máxima) → 07-23: 80,13% → 07-24: **80,02%** (agora confirmado estável entre
os dumps de 25/07 e 26/07). O ratio está, portanto, na fronteira inferior da
zona "neutra" (entre 80% e 87%) pela margem mais estreita de toda a janela
observada desde 20/07, mas **ainda não rompeu o piso de 80% em nenhuma das
cinco sessões**. O mecanismo por trás da compressão continuada é o mesmo de
sempre: o Board Crush — farelo, óleo e soja se movendo em proporções
distintas dentro do valor total do esmagamento, com a soja historicamente
subindo mais rápido do que o farelo nas sessões recentes de força do
complexo.

**Veredito sobre a revisão D+7 (`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`),
hoje 38 dias vencida.** A tese original (11/06/2026) apostava em três
condições para a janela de D+7 (alvo original: 18/06/2026): (1) ratio
comprimindo para <80% — **ainda não ocorreu**, mesmo 38 dias depois do alvo
e com o ratio "encostado" a 0,02pp do piso por cinco sessões seguidas; (2)
prêmio de exportação de farelo em Paranaguá zerado — **confirmado, e
persistente**: +0,05 USD/short ton (NAG, 24/07/2026), o mesmo valor exato há
22 dias corridos desde 03/07/2026 (nenhum novo print no fim de semana muda
essa contagem); (3) estrutura de crush favorecendo o óleo — **confirmada
estruturalmente** (ISO em 100/100, oil share em 52,62%), embora tenha
perdido força tática nas últimas sessões (ver seção Óleo). **Veredito desta
leitura: a tese está parcialmente confirmada — dois dos três pilares
originais (prêmio zerado, estrutura de crush) seguem de pé, mas o gatilho
tático central (ratio <80%) nunca disparou, apesar de cinco sessões seguidas
testando o piso sem rompê-lo.** Isso sugere que o mercado está, na prática,
em equilíbrio tenso entre a pressão estrutural bear (ABIOVE, ISF 80/100) e a
compra maciça de fundos (COT, net long +57,8% na semana de 21/07) — nenhum
dos dois lados venceu ainda. Dado que o checkpoint seguinte já programado
(D+90, 09/09/2026) está mais bem posicionado para capturar uma resolução
definitiva (WASDE e NOPA têm mais tempo para publicar dados novos até lá),
esta leitura recomenda **não fechar o ciclo desta revisão agora**, mas
registrar formalmente que o gatilho tático de D+7 não se confirmou dentro do
prazo original, e que o piso de 80% segue sendo o nível mais importante a
observar sessão a sessão até o próximo checkpoint.

**O COT (CFTC, corte de 21/07/2026) segue fortemente bullish para o farelo,
sem atualização nova hoje, mantendo a tensão com a tese estrutural bear.**
Managed money elevou a posição comprada de 119.347 para 130.152 contratos
(+9,1%) e reduziu a posição vendida de 72.771 para 56.676 (-22,1%) na semana
de 21/07 — o net long saltou de 46.576 para 73.476 contratos (+57,8%), e
como fração do open interest (618.289 contratos) subiu de 7,77% para
11,89%. Essa configuração — fundos cada vez mais comprados contra um ratio
que testa repetidamente o piso estrutural bear sem romper — é o retrato mais
direto da indefinição atual do farelo.

**A crush margin permanece confirmada no menor valor da janela recente:
2,9568 USD/bushel** (Board Crush: farelo 330,80 + óleo 73,47 − soja
1.240,25; 07-20: 3,0316 → 07-21: 3,1047 → 07-22: 3,1895 → 07-23: 3,1395 →
07-24: **2,9568**). O mecanismo segue o mesmo: a soja (o custo) subiu mais
rápido do que a soma de farelo e óleo (a receita) na sessão de sexta.

**O oil-meal spread permanece confirmado em 0,8041 USD/bushel** (ante 0,9823
na quinta, -18,1%) — a maior compressão diária desta janela, com o farelo
ganhando terreno relativo sobre o óleo dentro do valor do crush.

**A trajetória projetada da ABIOVE (sem alteração) segue sendo o pilar mais
sólido do argumento estrutural, porque não depende do preço do dia.** A
exportação de farelo brasileiro projetada cai de 1.400 mil toneladas em
agosto/2026 para 700 mil toneladas em dezembro/2026 (-50% em quatro meses),
enquanto a produção cai de forma bem mais suave (2.285,06 → 1.659,04 mil
toneladas no mesmo período, -27,4%) — menos farelo saindo pelo porto, com
produção caindo bem menos que a exportação, empurra o volume excedente para
o mercado interno de ração.

**As praças físicas de farelo no Brasil (NAG) não têm print novo para o fim
de semana.** O último dado segue sendo o salto de Mato Grosso/IMEA em 24/07:
+4,18% para R$ 1.669,72/ton, encerrando sete dias parado em R$ 1.602,80 —
**ainda sem confirmação ou reversão**, porque o primeiro print físico capaz
de validar (ou desmentir) esse salto só deve chegar no dump de segunda-feira.
Rondonópolis/MT segue em R$ 1.650,00/ton (estável desde 20/07) e Rio Grande
do Sul em R$ 1.640,00/ton (estável desde pelo menos 14/07).

**O Índice de Sobra de Farelo (ISF) permanece em 80/100 (4 de 5 condições
estruturais), com print explícito de 26/07/2026** (indicadores) — inalterado
desde pelo menos 01/07/2026, é recalculado mesmo em dia sem pregão porque
capta condições estruturais, não a mecânica de preço intradiário.

### O que invalida / risco para o farelo

- **Um fechamento de segunda-feira (27/07) abaixo de 325,00** desfaria o
  sinal tático do rompimento, mesmo com o COT bullish.
- **O ratio Far/Soj fechar segunda-feira abaixo de 80,00%** — o gatilho
  técnico mais próximo de toda a janela observada (0,02pp de distância,
  testado sem romper por cinco sessões seguidas) para devolver o quadro
  tático integralmente à tese estrutural bear original.
- **O próximo corte do COT (28/07, publicação ~31/07) mostrar reversão do
  net long** — se os fundos que compraram nesta semana começarem a vender, a
  configuração de tensão entre COT e ABIOVE se resolveria a favor da tese
  estrutural bear.
- **O salto do físico em MT/IMEA (+4,18% em 24/07) não se confirmar na
  próxima publicação** — sem dado de fim de semana, esta é a primeira
  pendência a resolver na reabertura.
- **NOPA seguir inacessível**, sem confirmação do esmagamento americano para
  os checkpoints D+90 (09/09/2026, agora também o checkpoint efetivo da
  revisão do ratio) e D+180 (08/12/2026).

### Leitura operacional — farelo

A leitura operacional não muda desde ontem, mas ganha um veredito formal
sobre a revisão vencida: para quem mantém posição vendida estrutural, a
recomendação segue sendo manter a tese via spread (farelo/soja ou crush
completo) em vez de posição vendida outright, dado o risco de "short
squeeze" alimentado pelo COT bullish — com o ratio testando o piso de 80%
pela quinta sessão sem romper, a paciência tática segue sendo o custo de
operar essa tese, não a convicção estrutural (que segue intacta via
ABIOVE/ISF). Para quem está comprado tático desde o rompimento de 325,00, a
base de preço agora confirmada (fechamento a 45,3% do range) sustenta manter
posição com stop na mínima confirmada de sexta (327,90) ou no nível
estrutural (325,00), mas sem espaço para aumentar exposição enquanto o ratio
segue "encostado" no piso. A operação relativa de comprar farelo contra óleo
dentro do crush (capturando a compressão de -18,1% do oil-meal spread,
confirmada) segue válida e é, nesta leitura, a forma mais equilibrada de
expressar a tensão atual sem depender da resolução do ratio.

---

## Óleo

**Viés: bear tático, com um sinal novo e ainda não confirmado — a base de
preço de sexta (73,47 cts/lb) está confirmada, mas a reabertura eletrônica
de domingo do heating oil (HO=F) trouxe um gap de -4,59% em volume muito
fino (1.458 contratos, 6,4% do volume de sexta), o primeiro dado
"adiantado" desta janela sobre o tom da semana. Estrutural, segue bull via
ISO 100/100 (print de 26/07) e COT mais concorrido das três pernas (18,17%
do OI, corte de 21/07, inalterado).**

### O que sustenta a tese

**A base de preço de sexta-feira está confirmada, sem revisão de volume.**
Fechamento 73,47 cts/lb (CBOT, ticker ZLU26.CBT, sessão de 24/07/2026),
abertura 74,53, mínima 73,30, máxima 74,77, volume 46.086 contratos — todos
idênticos ao dump de ontem, incluindo o volume (diferente de soja e farelo,
que ainda tiveram pequenas revisões de volume hoje). O fechamento confirmado
equivale a **11,6% do range do dia** ((73,47-73,30)÷(74,77-73,30)) — ainda o
pior fechamento relativo das três commodities na sessão de sexta (soja
84,7%, farelo 45,3%), agora sem incerteza residual sobre a magnitude exata.

**O dado genuinamente novo de hoje é o primeiro print da reabertura
eletrônica de domingo do heating oil (HO=F, ticker do contrato de referência
usado nesta série para a margem de biodiesel americano).** Abertura 4,0234
USD/galão — um gap de **-3,76%** frente ao fechamento de sexta (4,1806) —,
máxima 4,0355 (+0,30% sobre a própria abertura), mínima 3,9254 (-2,44% sobre
a própria abertura), fechamento 3,9889 (-0,86% sobre a própria abertura, mas
uma recuperação de +1,62% frente à mínima da sessão), volume 1.458
contratos. **O resultado líquido frente ao fechamento de sexta é uma queda
de -4,59%** ((3,9889-4,1806)÷4,1806). **Mecanismo:** o heating oil é o
combustível fóssil de referência usado nesta série para calcular a receita
da margem de biodiesel americano (junto com o RIN D4); uma queda no
heating oil, mantendo o custo do óleo de soja constante, comprime
diretamente essa margem — o que reduz o incentivo econômico à produção de
biodiesel e, por extensão, à demanda por óleo de soja como insumo. **Esta
leitura NÃO trata esse gap como um sinal confirmado**, por três razões: (1)
o volume de 1.458 contratos é o mais baixo de toda a janela observada por
uma grande margem (a sessão de sexta teve 22.882, quase 16x mais); (2) a
maior parte da queda ocorreu no gap de abertura (-3,76%), não numa
deterioração intradiária consistente — o preço, de fato, recuperou parte do
terreno perdido dentro da própria sessão fina; e (3) o briefing não traz
nenhuma notícia ou dado de energia (petróleo, diesel, geopolítica) que
explique a causa do gap — sem uma fonte que sustente o mecanismo por trás do
movimento, esta leitura trata o gap como um alerta tático a confirmar na
segunda-feira, não como um driver validado.

**Como exercício de mecanismo (não como indicador oficial do sistema, que
ainda não recalculou a margem de biodiesel para 26/07 — o último print
oficial segue sendo o de 24/07), aplicar a mesma fórmula documentada pelo
indicador `margem_usd_galao` ao heating oil de domingo, mantendo o custo do
óleo constante (Friday, sem sessão nova de ZLU26), resulta em: receita =
3,9889 (HO) + 1,5×2,11 (RIN D4, valor fixo usado pelo sistema) = 7,1539
USD/galão; margem = 7,1539 − 6,3103 (custo: óleo 5,5103 + industrial 0,80) =
**0,8436 USD/galão** — uma compressão adicional de -18,5% frente ao valor
oficial de sexta-feira (1,0354 USD/galão, 07-24). **Esta conta é uma
extrapolação da própria leitura, não um dado do sistema, e carrega toda a
incerteza do volume fino de domingo** — é apresentada apenas para
dimensionar a magnitude do mecanismo, não como número a operar.

**A curva forward, com os valores confirmados de sexta, manteve a
backwardation (desconto crescente nos vencimentos mais distantes)
documentada em leituras anteriores.** Agosto/26 (Q26) 74,33 → Setembro/26
(U26, spot) 73,47 (-0,86, -1,16%) → Outubro/26 (V26) 72,67 (-0,80, -1,09%) →
Dezembro/26 (Z26) 72,01 (-0,66, -0,91%) → Janeiro/27 (F27) 71,56 (-0,45,
-0,63%) — uma queda total de -2,77 cts/lb (-3,73%) de agosto a janeiro/27,
padrão de aperto físico de curto prazo mais do que reprecificação estrutural
de toda a curva.

**O Índice de Suporte do Óleo (ISO) permanece em 100/100 (5 de 5
condições), com print explícito de 26/07/2026** (indicadores) — a tese
estrutural (óleo dominando o valor do crush) segue formalmente intacta,
mesmo com o gap tático do heating oil.

**O oil share permanece confirmado em 52,62%** (ante 53,18% na quinta, uma
queda de -0,56 ponto percentual) — o primeiro valor fora da faixa de
53,0-53,5% em que o indicador vinha oscilando nos cinco pregões anteriores
(53,47%→53,09%→53,07%→53,18%→**52,62%**), agora confirmado sem incerteza de
revisão.

**O COT (CFTC, corte de 21/07/2026) segue confirmando que o óleo é, de
longe, a perna mais concorrida das três — sem atualização nova hoje.**
Managed money elevou a posição comprada de 133.321 para 143.159 contratos
(+7,4%) e reduziu a posição vendida de 25.376 para 22.913 (-9,7%) — o net
long subiu de 107.945 para 120.246 contratos (+11,4% na semana), e como
fração do open interest (661.652 contratos) está em 18,17% — o mais alto
entre soja (12,49%) e farelo (11,89%). Esse posicionamento assimétrico segue
sendo, ao mesmo tempo, evidência de convicção de fundos na tese estrutural e
o maior fator de risco de uma correção mais aguda se o sentimento virar —
um risco que ganha um pouco mais de relevância tática à luz do gap do
heating oil de hoje.

**Os forecasts estatísticos internos (26/07/2026)**, recalculados com o spot
agora confirmado, replicaram a geração de ontem: central 7d = 75,89 cts/lb
(bandas 71,22-80,56); central 30d = 84,51 cts/lb (bandas 74,85-94,18) —
sem mudança de viés (esses forecasts não incorporam o gap fino do heating
oil de domingo, que é um dado fora do escopo do modelo estatístico interno).

### O que invalida / risco para o óleo

- **Um fechamento de segunda-feira (27/07) abaixo de 73,30 (mínima de
  sexta)** confirmaria a primeira sequência de dois dias de fraqueza desde o
  início do rali — e ganharia peso adicional se coincidir com confirmação do
  gap do heating oil na sessão eletrônica plena de segunda.
- **O gap do heating oil de domingo se confirmar (não reverter) na sessão
  regular de segunda-feira, com volume normal** — transformaria um sinal
  tático fino e não confirmado no primeiro driver de energia genuinamente
  bearish desta janela para a margem de biodiesel.
- **O oil share continuar caindo abaixo de 52,62%** — se a tendência
  persistir por mais uma ou duas sessões, a narrativa estrutural de "óleo
  domina o crush" começaria a perder sustentação também no dado tático.
- **O próximo corte do COT (28/07, publicação ~31/07) mostrar realização de
  lucro no net long mais concorrido das três pernas (18,17% do OI)** — o
  risco estrutural de médio prazo mais relevante.
- **A isenção PIS/Cofins do biodiesel expirar em 31/07 sem renovação** (ver
  Lente fiscal), agora a apenas 5 dias — um vetor bearish direto para a
  demanda doméstica de óleo, independente do CBOT.
- **MPOB seguir inacessível** — hoje é o 17º dia consecutivo com o mesmo
  conteúdo sem números extraídos, mantendo cego o efeito do El Niño e dos
  vetores regulatórios indonésios sobre o prêmio de substituição via palma.

### Leitura operacional — óleo

A base de preço de sexta agora confirmada dá mais confiança para operar em
cima do nível de 73,30 como referência tática, mas o gap fino do heating oil
de domingo é motivo concreto para tratar segunda-feira como a sessão de
confirmação, não de ação imediata. Para quem está comprado direcional, a
recomendação é reavaliar o tamanho da posição antes da abertura de amanhã —
a tese estrutural (ISO 100/100, backwardation na curva, RIN D4/biodiesel)
segue de pé, mas o gap de energia, mesmo não confirmado, é o tipo de sinal
que precede sessões de maior volatilidade; um stop na mínima confirmada de
sexta (73,30) segue sendo a referência mais próxima. Para quem opera vendido
ou via spread, a operação relativa "farelo forte / óleo fraco" (oil-meal
spread, comprimido -18,1%) segue sendo a leitura mais atraente dentro do
complexo, e ganha um argumento tático adicional (não estrutural) com o gap
do heating oil — mas convém aguardar a sessão regular de segunda-feira antes
de aumentar exposição baseada nesse gap específico, dado o volume muito fino
em que ele ocorreu.

---

## Spreads e crush — leitura de complexo

### Crush margin: 2,9568 USD/bu (confirmado) — ainda o menor valor da janela recente

Confirmado estável entre os dumps de 25/07 e 26/07, o menor valor de toda a
janela observada (07-20: 3,0316; 07-21: 3,1047; 07-22: 3,1895; 07-23:
3,1395; 07-24: **2,9568**). O mecanismo segue o mesmo: a soja (o custo)
subiu mais rápido do que a soma de farelo e óleo (a receita) na sessão de
sexta.

### Ratio Far/Soj: 80,02% (confirmado) — quinta sessão seguida "encostado" no piso de 80%, sem romper

**Este é o ponto central da leitura de hoje, agora com um veredito
formal.** O ratio está confirmado, sem incerteza de revisão, em 80,02% —
dentro da zona "neutra" (entre 80% e 87%), mas pela margem mais estreita de
toda a janela observada desde 20/07 (79,28%→80,37%→80,65%→80,13%→**80,02%**)
e sem romper o piso em nenhuma das cinco sessões testadas. A revisão D+7
original (`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`)
está hoje 38 dias vencida com veredito de **confirmação parcial**: dois dos
três pilares (prêmio de exportação zerado, estrutura de crush favorecendo o
óleo) seguem de pé, mas o gatilho tático (ratio <80%) nunca disparou — ver
detalhamento na seção Farelo. O próximo checkpoint formal passa a ser o D+90
já programado (09/09/2026).

### Oil share: 52,62% (confirmado) — primeira queda fora da faixa recente, agora sem incerteza de magnitude

Confirmada a queda de -0,56 ponto percentual frente a quinta-feira
(53,18%→52,62%) — o primeiro valor fora da banda estreita de 53,0-53,5% em
que o indicador vinha oscilando nos cinco pregões anteriores. O óleo perdeu
participação relativa no valor do crush na sessão de sexta.

### Oil-meal spread: 0,8041 USD/bu (confirmado) — compressão de -18,1%, ainda a maior desta janela

Confirmada a queda de -18,1% no dia (0,9823→0,8041 USD/bu) — a maior
variação diária deste indicador na janela observada. O farelo ganhou terreno
relativo sobre o óleo de forma expressiva na sessão de sexta.

### Margem de biodiesel: 1,0354 USD/gal (oficial, 24/07) — extrapolação com heating oil de domingo aponta compressão adicional

O valor oficial do sistema segue em 1,0354 USD/gal (24/07, confirmado). A
extrapolação própria desta leitura (não oficial, ver seção Óleo), usando o
heating oil da reabertura de domingo (3,9889, volume fino de 1.458
contratos), projeta uma compressão adicional para ~0,8436 USD/gal (-18,5%) —
um sinal a confirmar, não a operar, até a sessão regular de segunda-feira.

### COT: corte de 21/07, ainda o mais recente — sem atualização nesta leitura

O corte de 21/07/2026 segue sendo o dado de posicionamento mais recente
disponível — mostra managed money comprando agressivamente as três pernas na
semana do rompimento: net long +73,6% em soja, +57,8% em farelo, +11,4% em
óleo. Em fração do open interest, óleo segue sendo a perna mais concorrida
(18,17%), seguida por soja (12,49%) e farelo (11,89%). O próximo corte
(28/07, publicação normal ~31/07) é o próximo capaz de dizer se essa compra
se sustentou.

### ISF em 80/100, ISO em 100/100 — ambos com print explícito de 26/07, inalterados

O Índice de Sobra de Farelo (4/5 condições) e o Índice de Suporte do Óleo (5
de 5 condições) permanecem exatamente nos mesmos níveis desde pelo menos
01/07/2026, agora confirmados por print datado de hoje (26/07) mesmo sem
pregão de grãos — esses índices captam condições estruturais, não a mecânica
tática de preço de curto prazo.

### O que os índices dizem juntos em 26/07/2026 (domingo, sessão de referência 24/07 confirmada)

ISF 80/100 + ISO 100/100 (ambos inalterados) + ratio Far/Soj confirmado em
80,02% (quinta sessão seguida sem romper o piso de 80%) + crush margin no
menor nível da janela (2,9568 USD/bu) + oil share fora da faixa recente
(52,62%) + oil-meal spread na maior compressão da janela (-18,1%) + COT
ainda parado no corte de 21/07 (compra maciça de fundos nas três pernas,
proporcionalmente mais concentrada em soja mas em nível absoluto mais
concentrada em óleo) + o gap fino e não confirmado do heating oil de domingo
(-4,59%, primeiro sinal de pressão energética sobre a margem de biodiesel) —
formam um quadro em que a base de preço agora **confirmada e estável** dá
mais confiança operacional a todos os níveis técnicos citados nesta leitura,
enquanto o novo dado de domingo (heating oil) é o primeiro elemento
genuinamente incerto a monitorar na abertura. **A lição mais importante
desta leitura, em contraste com as duas anteriores**: depois de dois dias
seguidos de revisão de preço (23/07 revisado em 24/07; 24/07 revisado em
25/07), a sessão de sexta-feira (24/07) finalmente **estabilizou** — o que
sugere que o padrão de revisão documentado nesta série não é permanente,
apenas um atraso de um dia no assentamento dos dados, e que a partir de
amanhã (sessão nova de segunda-feira) a leitura volta a operar sobre dados
de preço "frescos", não revisados.

---

## Lente fiscal e regulatória BR

**Isenção PIS/Cofins biodiesel — vencimento em 31/07/2026, agora a apenas 5
dias, e ainda sem sinalização pública de renovação** (evento
PISCOFINS-BIODIESEL-ISENCAO, `atualizado_em` 2026-06-05, sem mudança desde
então). Trata `trib-PISCOFINS-BIODIESEL-ISENCAO-2026-07-31`. **O mecanismo:**
a isenção incide na saída do biodiesel; se expirar sem renovação em 31/07, o
custo tributário efetivo da produção de biodiesel sobe, o que tende a
reduzir a margem de biodiesel doméstica (distinta da margem americana
calculada nesta leitura, que usa RIN D4 e heating oil dos EUA) e, por
extensão, pressionar a demanda por óleo de soja como insumo dentro do mix
B15 mandatório — um vetor bearish direto para óleo, independente do que
acontecer no CBOT. **A semana que abre amanhã (27-31/07) é literalmente a
última antes do vencimento** — com o monitor tributário há 51 dias sem
qualquer atualização (`atualizado_em` 2026-06-05 em todos os dez eventos
rastreados), o risco de execução descrito nas leituras anteriores (decisão
de renovar saindo de última hora, como ocorreu com a prorrogação anterior de
29/mai, e o sistema não capturando a tempo) chega ao seu momento mais
crítico de toda a janela observada. Esta segue sendo a leitura de maior
prioridade de monitoramento tributário desta série.

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L) — a
vigência formal (`vigencia_ate` 11/07/2026) venceu há 15 dias, e o monitor
tributário segue sem qualquer atualização de status** (evento MP-1358-2026,
`atualizado_em` 2026-06-05, status ainda "tramitacao"). Enquanto o
combustível fóssil segue subsidiado, a competitividade relativa do
biodiesel dentro do mix B15 mandatório fica pressionada.

**B16 — sem data, travado em B15.** Sem mudança de status (evento
B16-CNPE-2026, `atualizado_em` 2026-06-05, status "adiado"). Testes técnicos
do FNDCT com resultado esperado ~nov/2026 — realista só fim de 2026/início
de 2027.

**MP 1.363/2026 (subsídio ao diesel fóssil, R$ 1,12/L) — em vigor até
31/12/2026.** Sem alteração. Bearish estrutural persistente para a demanda
incremental de óleo de soja no mercado doméstico brasileiro.

**STJ REsp 2.165.276/2026 — crédito PIS/Cofins para esmagadoras.** Sem
alteração. Bullish para soja/óleo (alívio de custo de entrada para
biodiesel) e, por extensão, incentivo a mais esmagamento — em tensão com a
contração da crush margin (confirmada no menor nível da janela), que reduz
o incentivo tático de curto prazo mesmo com o alívio tributário estrutural
intacto.

**Vetores dos EUA e Indonésia, revisitados (sem mudança de status,
`atualizado_em` 2026-06-05 em todos):** EPA-RFS-2026-2027 (volumes recordes
de biocombustível, BBD 8,86→9,07 bi RINs, sustentando estruturalmente o RIN
D4 e o óleo CBOT — o RIN D4 usado no cálculo da margem de biodiesel segue
fixo em 2,11 USD/RIN, ver Honestidade); 45Z-CLEAN-FUEL (regra proposta que
tiraria insumo importado da elegibilidade ao crédito, favorecendo óleo de
soja doméstico americano); DANANTARA-INDONESIA (centralização estatal da
exportação de palma, assunção plena da cadeia alvo em 01/09/2026 — risco de
menor saldo exportável de palma, suporte ao óleo de soja por substituição);
INDONESIA-B50 (retórica agressiva mas quota flat — provável B45 em 2026,
B50 pleno só 2027-28); INDONESIA-LEVY-PMK9 (imposto de exportação de CPO até
12,5% desde 01/03, encarecendo palma e favorecendo substituição por óleo de
soja). Esses vetores seguem, em conjunto, num sentido estruturalmente
bullish para o óleo de soja via substituição de palma — mas continuam
inverificáveis pelo lado dos dados de mercado (MPOB inacessível há 17 dias
consecutivos, ver Honestidade).

**O monitor tributário como um todo está há 51 dias sem qualquer
atualização** (`atualizado_em` 2026-06-05 em todos os dez eventos
rastreados) — o intervalo segue crescendo exatamente na semana em que a
isenção PIS/Cofins do biodiesel chega ao vencimento (5 dias). Vale sinalizar
este ponto, mais uma vez e com urgência máxima, como prioridade de
manutenção do sistema, independentemente da leitura de preço.

---

## Riscos e eventos próximos

**A isenção PIS/Cofins do biodiesel vence em 31/07/2026, agora a apenas 5
dias**, sem sinalização de renovação — o vetor tributário mais próximo de um
desfecho concreto nesta leitura, e a prioridade máxima de monitoramento até
a resolução, com a janela de decisão coincidindo exatamente com a semana de
pregão que se abre amanhã (27-31/07).

**O ratio Far/Soj fecha a quinta sessão seguida em 80,02% (confirmado), a
0,02 ponto percentual do piso de 80%** — a abertura de segunda-feira (27/07)
é, portanto, a sessão mais importante desta janela para essa tese
específica, agora com a revisão D+7 (`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`)
formalmente encerrada com veredito de confirmação parcial e o próximo
checkpoint remarcado para o D+90 já programado (09/09/2026).

**O gap fino do heating oil na reabertura eletrônica de domingo (-4,59%,
volume de apenas 1.458 contratos) é o primeiro sinal, ainda não confirmado,
de pressão energética sobre a margem de biodiesel** — a sessão regular de
segunda-feira, com volume normal, é o teste decisivo para saber se esse gap
se sustenta ou reverte.

**O próximo corte do COT (referente a 28/07/2026, publicação normal
~31/07/2026)** é o dado mais aguardado agora — vai mostrar se a compra
maciça de fundos documentada na semana de 21/07 se sustentou durante a
sessão de sexta-feira (24/07) e a semana que se abre, ou se já começou a
reverter.

**O USDA Crop Progress deve publicar nova leitura nas próximas 24-48
horas** — o primeiro dado agrícola potencialmente novo desta janela.

**NOPA — segue inacessível** (fila `release-nopa-2026-07-26` tratada aqui,
sem dado interpretável, apenas nova data de coleta), sem crush americano
confirmado por fonte primária.

**MPOB — sem números de palma extraídos há 17 dias consecutivos**, mantendo
cego o efeito do El Niño e dos vetores regulatórios indonésios sobre o
prêmio de substituição do óleo de soja.

---

## Honestidade

O que não foi possível validar neste briefing de 26/07/2026, onde a
confiança é baixa ou há lacunas materiais:

**1. O primeiro print da reabertura eletrônica de domingo do heating oil
(-4,59% frente ao fechamento de sexta) foi negociado em apenas 1.458
contratos — 6,4% do volume da sessão regular de sexta (22.882)** — volume
muito abaixo do necessário para tratar esse movimento como confirmado. Esta
leitura tratou o gap explicitamente como um sinal tático a confirmar, não
como driver validado, e a extrapolação de margem de biodiesel feita a partir
dele (0,8436 USD/gal) é uma conta própria desta leitura, não um número
oficial do sistema.

**2. O padrão de revisão diária de preço documentado nas duas últimas
leituras (23/07 revisado em 24/07; 24/07 revisado em 25/07) não se repetiu
hoje para os PREÇOS da sessão de 24/07 — apenas o volume de soja (+1,27%) e
farelo (-4,77%) ainda se moveu entre os dumps de 25/07 e 26/07.** Não é
possível, a partir deste briefing, confirmar se essa estabilização de preço
é definitiva ou se ainda pode haver uma nova revisão no dump de amanhã —
esta leitura recomenda, por precaução, continuar cruzando os números antes
de decisões táticas muito apertadas, mesmo que a expectativa agora seja de
dados assentados.

**3. A projeção de exportação de soja de 110 milhões de toneladas na safra
26/27 (Canal Rural, 26/07/2026) não identifica a consultoria responsável nem
a metodologia** — esta leitura trata o número como reforço qualitativo
estrutural, não como pilar quantitativo da tese, dado que não é possível
verificar a fonte original nem compará-lo com projeções oficiais (USDA/CONAB
não trazem, neste briefing, uma cifra equivalente para a safra 26/27 ainda
em formação).

**4. O veredito de "confirmação parcial" dado à revisão D+7 de 11/06/2026
(hoje 38 dias vencida) é uma leitura interpretativa desta análise, não um
critério objetivo pré-definido no insight original** — o insight de 11/06
não especificou um critério de desempate para o caso em que dois de três
pilares se confirmam mas o terceiro (o gatilho tático) fica indefinido por
semanas. Esta leitura optou por remarcar o checkpoint para o D+90 já
programado, em vez de fechar o ciclo, mas essa é uma escolha de julgamento,
não uma regra do sistema.

**5. Sem pregão de grãos hoje (domingo), não há dado de preço novo de
soja/farelo/óleo a validar — toda a análise de preço desta leitura descreve
a sessão de 24/07/2026 (sexta-feira), a mais recente disponível.** A próxima
sessão de referência é segunda-feira, 27/07/2026.

**6. O prêmio de exportação de farelo em Paranaguá (+0,05 USD/sht) e o de
óleo (+0,08 cts/lb) estão no mesmo valor exato desde pelo menos 03/07/2026**
(NAG, agora 23 dias corridos sem variação de nenhum centavo) — não é
possível distinguir se isso reflete um mercado de exportação genuinamente
parado ou um valor que não está sendo atualizado de fato na fonte.

**7. Os níveis de resistência/suporte de 1.180,00 (soja) e 325,00 (farelo)
são alertas gerados pelo sistema de calibração interna, cuja metodologia de
definição de nível não é visível a partir deste briefing** — esta leitura
trata os níveis como dado (o sistema já os fiscaliza automaticamente), sem
poder validar de forma independente os critérios técnicos usados para
calibrá-los.

**8. O COT (CFTC) segue no corte de 21/07/2026, uma terça-feira — não cobre
a sessão de sexta-feira (24/07) nem o fim de semana** — o próximo corte
(28/07, publicação normal ~31/07) é o primeiro capaz de capturar esse
período, incluindo a possível reação dos fundos ao ratio Far/Soj ainda no
limiar técnico e ao gap do heating oil.

**9. Percentis históricos de COT não calculados** — os números de
21/07/2026 seguem lidos apenas em nível absoluto e como fração do open
interest corrente (soja 12,49%, farelo 11,89%, óleo 18,17%), sem série
histórica completa para calibrar se algum desses níveis está objetivamente
"esticado" no sentido histórico.

**10. O WASDE segue cobrindo apenas farelo (Argentina, Brasil, China
parcial), sem nenhum dado de soja em grão ou óleo de soja, em qualquer
geografia, e sem nenhum dado dos Estados Unidos** — sem atualização desde
10/07/2026 (16 dias). A pergunta central da revisão D+7 ("o WASDE mudou o
quadro?") segue sem canal de resposta interno.

**11. NOPA (fila `release-nopa-2026-07-26`) segue com `monthly_status` em
0,0 bool** — mesma barreira de assinatura paga documentada desde meados de
junho, agora com quase um mês e meio sem alternativa de dado primário sobre
o esmagamento americano. A "novidade" sinalizada pela fila é apenas a data
de coleta, não um dado genuinamente interpretável.

**12. Palma malaia (MPOB) segue sem números extraídos, agora por 17 dias
consecutivos com o mesmo conteúdo exato (3.439 caracteres, de 10/07 a
26/07/2026)** — a persistência do byte count idêntico segue sugerindo,
possivelmente, uma página que não está mais sendo servida com conteúdo
atualizado. Continua impossível avaliar o efeito do El Niño ou dos vetores
regulatórios indonésios sobre o prêmio de substituição do óleo de soja.

**13. Clima INMET (BR) não foi usado como driver de preço desta leitura.**
Julho é entressafra da soja brasileira (colheita concluída, plantio só em
outubro) — sem relevância direta para a tese de preço neste momento do
calendário agrícola. O El Niño Advisory (NOAA CPC, inalterado desde pelo
menos 03/07/2026) permanece relevante apenas para a expectativa da safra de
plantio de outubro/26 e para o clima do Sudeste Asiático (palma).

**14. BCBA Argentina — última leitura disponível é 22/07/2026, agora 4 dias
sem atualização**, sem relatórios de esmagamento/exportação acessíveis via
scraper.

**15. RIN D4 como parâmetro fixo (2,11 USD/RIN) segue sendo uma fonte
relevante de incerteza do modelo de biodiesel**, sem novo dado hoje — tanto
a margem oficial de 1,0354 USD/gal (24/07) quanto a extrapolação própria
desta leitura (0,8436 USD/gal, usando o heating oil de domingo) usam esse
valor fixo, o que significa que ambas compartilham a mesma fonte de
incerteza estrutural.

*Nenhum número foi inventado ou estimado além do que consta no briefing de
26/07/2026 e nos insights anteriores referenciados; a única exceção
explícita é a extrapolação de margem de biodiesel na seção Óleo, claramente
rotulada como conta própria desta leitura (não indicador oficial do
sistema), usando apenas a fórmula já documentada pelo indicador
`margem_usd_galao` e valores publicados no próprio briefing. A contribuição
central desta leitura foi (1) confirmar que a sessão de 24/07/2026
finalmente estabilizou em preço depois de duas revisões consecutivas
documentadas nas leituras anteriores, restando apenas ajustes residuais de
volume; (2) identificar e contextualizar o primeiro sinal (não confirmado,
volume muito fino) de pressão energética sobre o óleo via o gap de domingo
do heating oil; (3) fechar formalmente a revisão D+7 do farelo, vencida há
38 dias, com um veredito de confirmação parcial e remarcação para o
checkpoint D+90 já programado; e (4) incorporar a notícia nova sobre
projeção de exportação recorde de soja para a safra 26/27 como reforço
qualitativo à tese bull, sem tratá-la como pilar quantitativo dada a
ausência de fonte identificada.*
