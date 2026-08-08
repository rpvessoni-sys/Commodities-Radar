---
data: 2026-08-08
titulo: "Sábado sem sessão nova: o briefing segue travado no fechamento de quinta-feira (06/08) — nenhuma fonte, nem CBOT, nem PTAX, nem físico, nem COT, avançou desde a leitura de ontem, e o gap mais relevante é a ausência total da sessão de sexta-feira (07/08) da CBOT, que deveria existir e não está aqui; o complexo permanece com farelo estruturalmente pressionado (ISF 80/100), óleo tecnicamente rompido (67,60 vs. suporte 72,00, curva em backwardation) e soja tecnicamente neutra, mas todos os relógios da fila (D+7 do ratio, PIS/Cofins, Danantara) avançaram dois dias sem mudança de estado"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT (ZSU26 soja / ZMU26 farelo / ZLU26 óleo) — sessão de 2026-08-06 (quinta-feira), a MESMA sessão já usada na leitura de 2026-08-07; nenhuma sessão de 2026-08-07 (sexta-feira) está neste briefing, ver Honestidade
  - CME NYMEX heating oil (HO=F) — 2026-08-06, fechamento 3,7691 USD/galão (mesmo dado de ontem)
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, paridade BR, Índice de Sobra de Farelo, Índice de Suporte do Óleo) — todos calculados sobre o fechamento de 2026-08-06, sem recálculo novo
  - BCB PTAX — carimbo mais recente permanece 2026-08-05 (USD/BRL 5,1154); agora 3 dias corridos sem atualização (nenhum PTAX é publicado em fins de semana, mas também falta o de sexta-feira 07/08)
  - CEPEA/ESALQ Soja Paranaguá via NAG — carimbo mais recente 2026-08-05, R$ 144,91/saca; sem novo carimbo há 3 dias
  - CEPEA/ESALQ Soja Paraná interior via NAG — carimbo mais recente 2026-08-05, R$ 136,73/saca
  - NAG Físico BR — carimbo mais recente 2026-08-05 (farelo MT/IMEA R$ 1.675,10/ton, congelado há 8 dias desde 31/07; Rondonópolis/MT R$ 1.700,00/ton, mesmo congelamento; RS R$ 1.800,00/ton, ainda uma única leitura, sem segunda confirmação há 3 dias); prêmios export PGUA farelo (+0,05 USD/sht) e óleo (+0,08 cts/lb) também carimbados em 2026-08-05, "mês Agosto/26"
  - CFTC COT Managed Money — corte de 2026-07-28, ainda o mais recente; o corte referente a 2026-08-04, que a leitura de ontem esperava "por volta de sexta-feira 07/08", não chegou nem ontem nem hoje — agora 11 dias sem atualização de posicionamento
  - USDA Crop Progress — corte rotulado 2026-08-02, mesmos valores do corte de 2026-07-26 (11% excelente / 52% boa / 7% ruim), quinta leitura seguida sem mudança
  - USDA WASDE — ausente da janela, agora 29 dias de atraso desde o último dado (2026-07-10)
  - NOPA — fila `release-nopa-2026-08-06`, `monthly_status` continua em 0,0 bool (paywall), mais de 8 semanas sem alternativa de dado primário
  - ABIOVE projeções mensais — balanços ago-dez/2026, sem alteração frente ao dump anterior
  - NOAA CPC ENSO — carimbo mais recente 2026-08-06 (El Niño Advisory, inalterado)
  - MPOB — carimbo mais recente 2026-08-06 (mesmo conteúdo de 3.439 caracteres, parser sem números extraídos)
  - BCBA Argentina — carimbo mais recente 2026-08-06 (acessível, sem links de relatório detectados)
  - INMET — última previsão capturada é para 2026-08-06 (chuva/trovoada em Cascavel e Maringá/PR e Passo Fundo/RS; calor seco em Cuiabá, Lucas do Rio Verde, Rio Verde/GO, Sinop e Sorriso/MT)
  - Notícias Agrícolas/Canal Rural RSS — última manchete relevante capturada em 2026-08-06 ("Soja em Mato Grosso atinge maior preço do ano, mas indústria enfrenta desafios", canalrural.com.br), sem item novo de soja/farelo/óleo desde então
  - system/tributario_watch.toml (lido como referência, não editado) — `atualizado_em` 2026-06-05, agora 64 dias sem atualização
  - Cruza com [[2026-08-07_leitura-complexo]], [[2026-08-05_leitura-complexo]] e [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (tese original do D+7, cujo checkpoint segue vencido)
status: ativa
vies: [neutral-soja, bear-farelo, bear-oleo_soja]
---

## Visão geral

O complexo soja é, mecanicamente, uma fábrica com uma única matéria-prima (a
soja em grão) e dois produtos de saída em proporção fixa por bushel esmagado:
o **farelo** (a fração proteica, ~78% da massa, vira ração animal) e o **óleo
degomado** (a fração de gordura, ~18-20% da massa, vira óleo de cozinha e
biodiesel). Quem decide o ritmo de esmagamento é a esmagadora, olhando dois
números calculados sempre em dólares na CBOT (Chicago Board of Trade, a bolsa
de referência mundial para esses três contratos): a **crush margin** (farelo
+ óleo, por bushel, menos o custo daquele bushel de soja) e o **oil share** (a
fatia dessa margem capturada especificamente pelo óleo). Quando o oil share
sobe, o óleo "manda" no crush — a esmagadora tolera vender o farelo mais
barato porque a decisão de esmagar é sustentada pela margem do óleo, e o
farelo vira, na prática, o subproduto que sobra. O **ratio Far/Soj** (preço do
farelo dividido pelo preço da soja, normalizado pela conversão bushel↔short
ton) mede a mesma dinâmica por outro ângulo: abaixo de 80% o farelo está
historicamente "abundante" frente à soja (zona baixista para o farelo), acima
de 87% está "apertado" (zona altista), e entre os dois fica uma faixa neutra
de mean-reversion.

**Hoje é sábado, 2026-08-08, e este é o ponto central desta leitura: o
briefing não trouxe absolutamente nenhum dado novo em nenhuma das suas
fontes desde a sessão de quinta-feira, 2026-08-06 — a mesma sessão que já
sustentou integralmente a leitura de ontem, 2026-08-07.** Isso é esperado até
certo ponto (a CBOT não opera aos sábados, e o BCB não publica PTAX aos fins
de semana), mas há uma lacuna que não é meramente de calendário: a sessão de
**sexta-feira, 2026-08-07**, que deveria existir (a CBOT opera normalmente às
sextas), **não está neste briefing** — nem soja, nem farelo, nem óleo, nem
heating oil trazem um carimbo de 07/08. O mesmo vale para o COT (CFTC), cujo
corte referente a 04/08 a leitura de ontem esperava "por volta de sexta-feira"
e que segue ausente hoje. Por isso, esta leitura trata o conteúdo de mercado
como **idêntico** ao de ontem — nenhum preço, nenhuma margem, nenhum índice
sintético mudou — e desloca o foco para três frentes que *de fato* avançam
independente de haver pregão novo: (1) os contadores de dias da fila de
julgamento, que continuam correndo mesmo sem dado novo; (2) uma checagem mais
funda dos mecanismos que já estavam em jogo, útil justamente porque não há
ruído de um novo candle para disputar espaço com a explicação; e (3) o
registro explícito, para o dono, de que a ausência da sessão de sexta-feira é
uma lacuna de dado real, não uma leitura de mercado — ver Honestidade. Com
isso: o farelo segue estruturalmente pressionado por baixo (Índice de Sobra
de Farelo em 80/100 pelo nono carimbo seguido com o mesmo valor, embora sem
sessão nova desde quinta), o óleo segue tecnicamente rompido (67,60 cts/lb
ante o suporte de 72,00, -6,11%, com a curva futura em backwardation) e a
soja segue tecnicamente neutra (consolidação extrema nos dois últimos
pregões conhecidos, sem confirmação de direção). **Leitura de uma linha:** o
pivô do complexo hoje não é um número — é a ausência de números; a maior
convicção desta leitura está nos mecanismos estruturais que independem do
calendário (ISF, ISO, ABIOVE), a confiança é moderada para as leituras
técnicas de curto prazo (óleo rompido, ratio em disputa) porque ficam
"congeladas" há dois dias sem teste novo, e a confiança é baixa para
qualquer afirmação sobre o que aconteceu de fato na sexta-feira 07/08, que
esta leitura não pode nem confirmar nem descartar.

---

## Soja

**Viés: neutro — dois pregões seguidos (04→05, 05→06/08) de consolidação
extrema no papel (CBOT), sem um terceiro pregão disponível para testar se o
padrão se rompe, porque a sessão de sexta-feira não está neste briefing.**
Último fechamento disponível: 1.157,50 cts/bushel (CBOT, ticker ZSU26.CBT,
2026-08-06).

### O que sustenta a tese

**A última sessão registrada (06/08) foi a mais estreita da série de
leituras recentes, e essa é a informação mais recente que existe — não há
como saber se a compressão se rompeu na sexta.** Abertura 1.157,25, máxima
1.158,50, mínima 1.155,75, fechamento 1.157,50 — amplitude de apenas 2,75
pontos, um quarto dos 13,00 pontos do pregão anterior. **Mecanismo:**
compressão de amplitude, em teoria técnica de mercado, tende a preceder um
movimento mais amplo quando aparece o catalisador — mas o catalisador mais
óbvio que faltava (o COT da semana, esperado para sexta) também não chegou,
o que é coerente com a hipótese de que o "represamento" técnico persiste,
mas não é uma confirmação, porque simplesmente não há dado de sexta-feira
disponível para testar essa hipótese.

**A curva futura, na última leitura disponível, seguia em contango regular,
sem sinal de aperto de oferta prompt.** Q26 (ago/26) 1.151,75, U26 (set/26)
1.157,50, X26 (nov/26) 1.175,75, F27 (jan/27) 1.191,00, H27 (mar/27) 1.197,00,
K27 (mai/27) 1.205,25 — cada vencimento mais distante vale mais que o
anterior. O spread K27-Q26 (53,50 pontos) tinha se mantido estável frente ao
pregão anterior (54,50), sem sinal de esticamento ou compressão. **Sem
sessão de sexta-feira, esta leitura não tem como saber se esse formato de
curva persistiu** — é o desenho mais recente confirmado, tratado como ponto
de partida, não como fato de hoje.

**O câmbio permanece com o mesmo carimbo de quarta-feira (05/08), agora há
3 dias sem atualização.** USD/BRL PTAX em **5,1154** (BCB, 2026-08-05) — a
paridade teórica em reais (sem prêmio de basis) segue em **R$ 130,54/saca**
(indicators, CBOT 1.157,50 cts × USD/BRL 5,1154, ambos os insumos do mesmo
carimbo de 06/08 no lado CBOT, mas de 05/08 no lado câmbio). **Mecanismo e
leitura:** qualquer movimento genuíno de câmbio de quinta (06/08) ou sexta
(07/08) — inclusive o efeito de eventos macro de fim de semana, que também
não estão capturados — não aparece neste número. Para quem usa a paridade
como referência de originação, o número de hoje deve ser tratado como uma
foto de quarta-feira, não de sábado.

**A manchete "Soja em Mato Grosso atinge maior preço do ano, mas indústria
enfrenta desafios" (Canal Rural, 06/08/2026) segue sendo a última notícia
relevante do complexo capturada pelo RSS — nenhum item novo de soja, farelo
ou óleo apareceu nas leituras de 07/08 ou 08/08.** Ela veio como headline
puro, sem corpo de texto nem número (`headline: None`). **Mecanismo e
leitura, sem progresso desde ontem:** se o preço físico da soja em Mato
Grosso está de fato fazendo máxima do ano, isso é coerente com o prêmio de
exportação de Paranaguá — na última leitura em que é possível comparar
CBOT e físico no mesmo dia (05/08), a soja em Paranaguá (R$ 144,91/saca)
pagava um prêmio de **+10,94%** sobre a paridade teórica daquele dia (R$
130,62/saca, indicators). Esse número não mudou porque não há dado novo de
nenhum dos dois lados — mas o fato de a manchete continuar sem confirmação
numérica, agora há dois dias, reforça a recomendação já feita ontem: **não
tratar essa manchete como driver quantitativo até aparecer um número
verificável em fonte primária.**

**O posicionamento do COT (CFTC) segue no corte de 28/07/2026 — o corte
referente a 04/08, que a leitura de ontem esperava "por volta de sexta-feira,
07/08", não chegou nem ontem nem hoje.** O managed money net long em soja
estava em 160.479 contratos (15,73% do open interest de 1.020.108) no
último corte conhecido, após uma alta de +22,97% na semana anterior, com o
preço na época rondando o topo recente (fechamento de 28/07: 1.204,75). A
soja de hoje (1.157,50, mesmo valor de quinta) está -3,93% abaixo desse
nível — distância que não mudou desde ontem, porque nenhum dos dois lados
(preço ou posicionamento) tem dado novo. **Mecanismo:** o atraso do COT
começa a ficar relevante por si só — o intervalo normal entre publicações é
semanal (toda sexta, referente à terça anterior); já se passaram 11 dias
desde o corte de 28/07 sem um novo, o dobro do intervalo padrão, o que
sugere possível atraso na publicação da própria CFTC (não necessariamente
um problema do pipeline do robô) — vale a pena o dono checar diretamente a
CFTC antes de segunda-feira, caso o dado siga ausente no próximo briefing.

### O que invalida / risco para a soja

- **A sessão de sexta-feira (07/08) aparecer retroativamente num briefing
  futuro** — se vier fora do range de 1.155,75-1.158,50, romperia a
  consolidação e definiria a primeira direção nova desde 04/08.
- **A manchete de máxima do ano em Mato Grosso ganhar um número
  verificável** — muda a magnitude da leitura sobre o basis físico
  brasileiro.
- **O COT (referente a 04/08) finalmente ser publicado** — mostraria se os
  fundos já vinham reduzindo o net long antes da consolidação técnica, ou
  se mantiveram a posição.
- **O câmbio (PTAX) trazer carimbos de 06/08 e 07/08 simultaneamente** — um
  salto acumulado de dois dias mudaria a leitura de paridade de forma mais
  visível do que updates diários incrementais.
- **O WASDE finalmente voltar a ser publicado** (29 dias de atraso).

### Leitura operacional — soja

Para quem opera os dois lados, a ausência de sessão de sexta-feira é, em si,
uma informação operacional: não há como saber se a compressão de volatilidade
dos últimos dois pregões conhecidos (13,00 pontos em 05/08, 2,75 pontos em
06/08) persistiu, reverteu ou rompeu na sexta. A recomendação é tratar
segunda-feira (10/08) como a primeira leitura realmente nova desde
quinta-feira — dois pregões acumulados (sexta que faltou e segunda) podem
trazer um movimento maior que o normal, simplesmente por acúmulo de tempo
sem descoberta de preço neste briefing. O range de quinta (1.155,75-1.158,50)
segue como a referência técnica mais próxima; o range de quarta
(1.148,75-1.161,75) como referência secundária mais ampla. Para quem opera o
físico brasileiro, a recomendação de ontem permanece idêntica: buscar
confirmação direta na praça da manchete de máxima do ano antes de qualquer
decisão de originação, usando o basis prático do dono em vez da paridade
CBOT×PTAX pura — hoje isso é ainda mais importante, porque a paridade
calculada usa um câmbio de quarta-feira.

---

## Farelo

**Viés: bear estrutural — sem sessão nova para testar a reversão tática de
ontem (ratio subindo de 80,47% para 80,60%), a leitura de hoje mantém a
tese de fundo (ISF em 80/100) e trata o sinal tático de quinta como ainda
não confirmado nem invalidado, apenas suspenso pela falta de dado.** Trata
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` (fila,
ainda listada com carimbo 2026-08-06) e `release-nopa-2026-08-06` (fila,
mesma barreira de sempre, ver abaixo). Último fechamento disponível: 311,00
USD/short ton (CBOT, ticker ZMU26.CBT, 2026-08-06).

### O D+7 chega a 51 dias vencido — e agora soma um fim de semana sem teste

A tese original ([[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]])
apostava que a compressão rápida do ratio em junho (83,3%→81,4% em 4
pregões) levaria à zona comprimida (<80%) "em 1-2 semanas". O checkpoint
formal (D+7) caiu em 18/06/2026; hoje, 08/08/2026, são **51 dias corridos**
sem confirmação do fechamento abaixo de 80% — um dia a mais que os 50
registrados ontem, mas sem nenhum pregão novo para testar se o sinal de
ontem (ratio subindo, contra a tese) se repete ou se inverte de volta.
**O item mais importante para o dono aqui é que a fila continua listando
este gatilho com o carimbo de 2026-08-06** — ou seja, o próprio robô ainda
não teve uma sessão nova para reavaliar o item; esta leitura o trata como
"sem novidade desde ontem", não como pendência nova. O ratio mais recente
conhecido segue em **80,60%** (indicators, 2026-08-06), ainda dentro da
faixa neutra (80-87%), ainda sem confirmar nem a compressão de julho, nem a
reversão de quinta-feira por mais de uma sessão. O próximo marco formal
continua sendo o D+90 (2026-09-09, agora a **32 dias** de hoje).

### O que sustenta a leitura de hoje

**A crush margin, na última leitura disponível, estava estabilizada em
2,703 USD/bushel** (farelo 311,00 + óleo 67,60 − soja 1.157,50) — folgada
frente ao nível de alerta histórico (<2,50 USD/bu). **Mecanismo, sem
mudança:** enquanto a margem de papel (CBOT) segue folgada, a esmagadora não
tem, por esse indicador, sinal de que precise reduzir ritmo de esmagamento
— mas, como já registrado ontem, esse número não captura a margem
*doméstica* real, que depende do custo local da soja e que a manchete de
Mato Grosso sugere estar sob pressão (ver seção Soja).

**O oil-meal spread e o oil share, na última leitura, favoreciam o farelo
relativamente ao óleo dentro do crush — mas esse sinal, por ser de um único
pregão, segue sem confirmação de uma segunda sessão.** Oil-meal spread em
0,594 USD/bushel (queda de -3,57% frente ao pregão anterior) e oil share em
52,08% (queda de -0,08 ponto percentual). **Mecanismo, sem dado novo para
testar:** essa combinação — farelo relativamente mais forte, óleo
relativamente mais fraco no mesmo pregão — é exatamente o oposto do padrão
que sustentaria "óleo manda, farelo sobra" no curto prazo. A recomendação
desta leitura é a mesma de ontem, reforçada pela ausência de teste novo:
tratar isso como um dia isolado até haver confirmação, não como mudança de
regime.

**O Índice de Sobra de Farelo (ISF) permanece em 80/100 (4 de 5 condições
estruturais) — agora pelo nono carimbo consecutivo com o mesmo valor**
(30/07 a 06/08, todos idênticos; sem carimbo novo hoje porque não há sessão
nova). As projeções ABIOVE seguem, sem alteração, mostrando a exportação de
farelo brasileiro caindo de 1.400 mil toneladas em agosto/2026 para 700 mil
toneladas em dezembro/2026 (-50% em quatro meses) e o esmagamento mensal
projetado caindo de 2.827 mil t em setembro para 2.204 mil t em dezembro
(-22%) — drivers estruturais de mais longo prazo que independem
completamente do calendário de pregões, e por isso são a parte mais sólida
desta leitura de farelo hoje: **eles não "pararam" só porque o mercado não
abriu.**

**Prêmio de exportação em Paranaguá permanece perto de zero, carimbo de
2026-08-05, agora 3 dias sem atualização.** +0,05 USD/short ton, "mês
Agosto/26" (NAG). **Mecanismo, sem mudança:** um prêmio de exportação perto
de zero por semanas seguidas significa que o mercado externo não paga o
suficiente acima do preço doméstico para justificar direcionar farelo
brasileiro para o porto — o farelo fica represado internamente, pressão
estrutural de baixa que reforça o mecanismo por trás do ISF, e que — ao
contrário do ratio tático — não depende de um pregão CBOT para se manter
válida.

**As praças físicas de farelo no Brasil (NAG) seguem sem carimbo novo desde
05/08.** Mato Grosso/IMEA congelado em R$ 1.675,10/ton **há 8 dias**
(desde 31/07), Rondonópolis/MT congelado em R$ 1.700,00/ton no mesmo
período, e o salto do Rio Grande do Sul (R$ 1.640,00→1.800,00/ton,
registrado em 05/08) **segue sem uma segunda leitura de confirmação há 3
dias**. Como as leituras anteriores já vinham recomendando, um único pregão
pós-congelamento de mais de uma semana não é suficiente para tratar R$
1.800,00/ton como o novo preço de referência — quanto mais tempo passa sem
segunda leitura, maior o peso dessa ressalva.

**`release-nopa-2026-08-06` (fila) sinaliza novo carimbo, mas o
`monthly_status` permanece em 0,0 bool** — mesma barreira de assinatura
paga documentada desde meados de junho, agora mais de 8 semanas sem
alternativa de dado primário sobre o crush americano. Tratado como item da
fila resolvido (sem conteúdo novo para incorporar), não como pendência de
leitura.

### O que invalida / risco para o farelo

- **A primeira sessão nova (provavelmente segunda-feira, 10/08) confirmar
  a alta do ratio de quinta-feira** — se o farelo seguir subindo relativo à
  soja por mais de uma sessão, a leitura precisaria reconsiderar a força
  tática do viés bear-farelo, mesmo com o pano de fundo estrutural (ISF,
  ABIOVE) inalterado.
- **O salto do físico no RS (R$ 1.640→1.800/ton) se confirmar com um
  segundo carimbo** — validaria uma correção real de represamento, não uma
  anomalia de coleta; quanto mais dias sem segunda leitura, mais essa
  ausência em si vira um sinal de possível erro de coleta a ser verificado
  manualmente.
- **O prêmio de exportação em Paranaguá sair de zero** depois de mais de um
  mês parado.
- **A manchete de "indústria enfrenta desafios" em Mato Grosso se traduzir
  em redução de ritmo de esmagamento local**, com número verificável.
- **A crush margin cair de forma mais persistente** rumo ao nível de alerta
  (<2,50 USD/bu).

### Leitura operacional — farelo

Para quem monitora o ratio Far/Soj como gatilho tático, a recomendação
operacional não muda, mas ganha um motivo adicional para paciência: sem
sessão de sexta-feira, o "terceiro pregão" que decidiria se a reversão de
quinta é ruído ou início de tendência simplesmente não existe ainda —
segunda-feira concentra a informação de dois dias de mercado potencialmente
represados (a própria sexta que não abriu neste briefing, mais o fim de
semana). A recomendação é aguardar essa sessão antes de tratar qualquer
nível do ratio como sinal robusto para posições de convergência. Para quem
opera o físico de farelo no RS, a ausência de dado novo mantém a mesma
recomendação: não tratar R$ 1.800,00/ton como preço de mercado confirmado
sem uma segunda leitura, e considerar contato direto com a praça dado que
já são 3 dias sem confirmação via o dado público.

---

## Óleo

**Viés: bear estrutural com a quebra técnica confirmada e sem teste novo —
a curva futura, na última leitura, estava em backwardation por dois pregões
seguidos, com o spread entre pontas alargando; sem sessão de sexta-feira,
esta leitura não pode dizer se a inversão avançou, estabilizou ou reverteu.**
Trata `alerta-quebra_suporte-oleo_cbot-2026-08-06` (fato: 67,60 vs nível
72,00, ainda o carimbo mais recente). Último fechamento disponível: 67,60
cts/lb (CBOT, ticker ZLU26.CBT, 2026-08-06).

### O que sustenta a tese

**A última sessão registrada fechou perto da mínima do dia, um candle de
viés vendedor claro.** Abertura 67,75, máxima 67,89, mínima 67,57,
fechamento 67,60 — fechamento a apenas 9,4% do range, o mais fraco desta
série de leituras recentes. Em nível, **67,60 está -6,11% abaixo do suporte
técnico de 72,00** monitorado pela fila desde 31/07. Essa é a distância mais
recente conhecida — sem sessão de sexta-feira, não há como saber se o óleo
testou o suporte de volta, aprofundou a queda, ou reverteu; esta leitura
trata -6,11% como o dado mais atual disponível, não como o dado de hoje.

**A curva futura, na última leitura, estava em backwardation havia dois
pregões seguidos, com o spread entre a ponta curta (Q26) e a ponta longa
(H27) em 0,97 cts/lb** — Q26 67,85, U26 67,60, V26 67,30, Z26 67,06, F27
67,00, H27 66,88. O mecanismo identificado ontem segue válido como último
retrato conhecido: o aprofundamento da inversão entre 05/08 e 06/08 veio
mais da ponta longa cedendo (H27 caiu 0,16) do que da ponta curta subindo
(Q26 praticamente parado, -0,01) — uma leitura mais consistente com o
mercado descontando mais oferta ou mais pressão regulatória nos meses
seguintes do que com um aperto de disponibilidade imediata. **Sem sessão
nova, esta leitura mantém essa interpretação como hipótese de trabalho, não
como fato reforçado por dado adicional.**

**A margem de biodiesel americana, no último cálculo disponível, estava em
1,0641 USD/galão — mas esse número já vinha sob suspeita de qualidade de
dado, e essa suspeita não teve como ser resolvida hoje por falta de dado
novo.** Como identificado na leitura de ontem, os campos de abertura do
heating oil de quinta-feira eram idênticos, casa decimal por casa decimal,
aos mesmos campos registrados sob o carimbo de quarta-feira neste mesmo
dump — evidência concreta de um provável problema de pipeline. Sem uma
sessão nova para comparar, esta leitura não pode confirmar se o problema
persiste, foi corrigido, ou era um evento isolado — mantém a mesma reserva
de confiança sobre volumes e extremos (máxima/mínima) do heating oil e do
farelo já registrada ontem.

**O Índice de Suporte do Óleo (ISO) permanece em 100/100 (5 de 5 condições)
— agora pelo nono carimbo consecutivo com o mesmo valor** (30/07 a 06/08).
A tese estrutural (óleo dominando o valor do crush) segue formalmente
intacta como último retrato conhecido, coexistindo sem contradição técnica
com o preço em tendência de baixa e a curva cada vez mais invertida — o ISO
mede quem captura valor dentro do crush, não se o preço está caro ou barato
frente a um nível técnico.

**As projeções ABIOVE de exportação de óleo brasileiro, sem alteração desde
o dump anterior, seguem reforçando a leitura de oferta represada no mercado
interno.** Exportação de óleo caindo de 110 mil toneladas em setembro/2026
para 45 mil em outubro e 21 mil em novembro/2026 (-80% em dois meses) — um
driver estrutural que, assim como o ISF do farelo, não depende de pregão
novo para permanecer válido.

**Sem COT novo — o corte de 28/07/2026 segue sendo a fotografia mais
recente**, mostrando os fundos com net long em óleo de 107.898 contratos
(16,60% do open interest de 650.041), após uma redução de -10,27% na semana
anterior ao corte — a única das três pernas em que o book especulativo já
reduzia exposição comprada antes da queda de preço das sessões seguintes. O
corte referente a 04/08, esperado "por volta de sexta-feira" segundo a
leitura de ontem, segue ausente também hoje.

### O que invalida / risco para o óleo

- **A curva futura, na primeira sessão nova, voltar a contango** — se os
  vencimentos distantes (Z26, F27, H27) voltarem a valer mais que os
  próximos, tanto a leitura de aperto de curto prazo quanto a de desconto
  de longo prazo perderiam sustentação.
- **A ponta longa da curva (H27) parar de ceder e estabilizar** na próxima
  leitura disponível.
- **O heating oil confirmar volume e extremos genuinamente novos** (não
  repetidos de um carimbo anterior) na próxima sessão — validaria ou
  descartaria a suspeita de pipeline identificada ontem.
- **Um fechamento consistente de volta acima de 68,55** (máxima da sessão
  de 05/08) — romperia a sequência de fechamentos fracos.
- **A isenção PIS/Cofins do biodiesel seguir sem renovação** — hoje é o 5º
  dia útil desde o vencimento (31/07), sábado não conta como dia útil (ver
  Lente fiscal).

### Leitura operacional — óleo

Para quem está vendido desde a quebra do suporte 72,00, a ausência de
sessão nova não muda a recomendação: manter a leitura tática de posição
vendida com stop lógico acima de 68,55, já que nada surgiu para invalidar o
desenho técnico do último pregão conhecido. A leitura de que o
aprofundamento da backwardation vinha do fim da curva, não do início,
continua relevante para quem opera spreads de calendário — estruturas que
vendem os vencimentos mais distantes contra os próximos (vende F27/H27,
compra Q26/U26) seguem sendo a leitura coerente com o último dado
disponível, mas a ausência de sessão de sexta-feira significa que essa
posição carrega dois dias de risco de gap (sexta que faltou + fim de
semana) sem atualização de preço para reavaliar. Para quem considera nova
posição comprada, a recomendação de ontem permanece reforçada: não tratar
a margem de biodiesel do último carimbo disponível como número confiável,
dado o problema de qualidade de dado identificado e ainda não resolvido.

---

## Spreads e crush (leitura de complexo)

**Ratio Far/Soj: 80,60% no último carimbo disponível (06/08), sem sessão
nova para testar se a alta de quinta-feira (que revertia a compressão de
quarta) se confirma ou reverte de novo.** A recomendação operacional
permanece: exigir confirmação por mais de uma sessão seguida na mesma
direção antes de tratar qualquer nível como sinal robusto — e a ausência de
pregão hoje só reforça essa cautela, porque o "próximo pregão" que
determinaria essa confirmação ainda não aconteceu neste briefing.

**Crush margin: 2,703 USD/bu no último carimbo, folgada acima do nível de
alerta (<2,50 USD/bu).** Sem dado novo para reavaliar.

**Oil share: 52,08% no último carimbo — a leitura de farelo relativamente
mais forte e óleo relativamente mais fraco dentro do crush, registrada em
06/08, segue sem teste de continuidade.**

**Oil-meal spread: 0,594 USD/bu no último carimbo, -3,57% frente ao pregão
anterior — mesma leitura de "dia isolado" sem confirmação, já discutida na
seção Farelo.**

**ISF em 80/100, ISO em 100/100 — ambos inalterados agora pelo nono
carimbo seguido, e ambos são, tecnicamente, a parte mais sólida desta
leitura de hoje: são índices estruturais (calculados sobre condições de
mais longo prazo — exportação, esmagamento, participação relativa no
crush) que não "pausam" quando o mercado não abre.** As projeções ABIOVE de
esmagamento mensal (2.827 mil t em setembro caindo para 2.204 mil t em
dezembro, -22%) seguem reforçando o pano de fundo de menor oferta futura de
farelo e óleo no Brasil.

**A curva futura do óleo, no último retrato disponível, seguia em
backwardation pelo segundo pregão seguido, enquanto soja e farelo seguiam
em contango regular.** Esta continua sendo a divergência estrutural mais
persistente da série — mas hoje, sem pregão novo, ela é tratada como
"último estado conhecido", não como fato reconfirmado.

**O que os índices dizem juntos hoje:** nada mudou nos números, e essa
ausência de mudança é o próprio dado relevante — os componentes estruturais
do complexo (ISF, ISO, ABIOVE) continuam apontando para um farelo pressionado
por baixo e um óleo estruturalmente favorecido na captura de valor do crush
(mesmo com o preço do óleo em tendência de queda técnica), enquanto os
componentes táticos (ratio, oil-meal spread, curva do óleo) ficam
"suspensos" no último estado conhecido de quinta-feira, aguardando a
próxima sessão real para confirmar ou reverter.

---

## Lente fiscal e regulatória BR

**Isenção PIS/Cofins do biodiesel (`PISCOFINS-BIODIESEL-ISENCAO`,
`vigencia_ate` 2026-07-31) — hoje, 2026-08-08 (sábado), permanece no 5º dia
útil desde o vencimento, porque sábado e domingo não contam como dias
úteis.** Os dias úteis decorridos seguem sendo 03/08 (seg), 04/08 (ter),
05/08 (qua), 06/08 (qui) e 07/08 (sex) — o contador só volta a andar na
segunda-feira, 10/08, que será o 6º dia útil. Nenhum item do RSS desde
06/08 trouxe informação sobre este tema. **Mecanismo e leitura, sem
mudança:** se a isenção caducou sem renovação, o custo de produção do
biodiesel brasileiro sobe, reduzindo a competitividade do biodiesel dentro
do mix mandatório e pressionando a demanda de óleo de soja como insumo
doméstico — vetor bearish direto para o óleo, e um candidato a explicar
(parcialmente) por que a ponta longa da curva do óleo estava cedendo mais
que a curta na última leitura disponível. Com o monitor tributário
(`system/tributario_watch.toml`) parado desde 2026-06-05 (**64 dias sem
atualização**), esta leitura segue sem poder confirmar nem descartar a
caducidade — mantém-se como o item de verificação manual mais urgente desta
janela.

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L) —
vigência formal venceu há 28 dias** (`vigencia_ate` 11/07/2026), sem
qualquer atualização de status no monitor.

**MP 1.363/2026 — subsídio ao diesel fóssil (R$ 1,12/L), em vigor até
31/12/2026, sem alteração.** Bearish estrutural persistente: enquanto o
diesel fóssil segue subsidiado no mix B15, o biodiesel via óleo de soja
compete em desvantagem — reforçado se a isenção PIS/Cofins também tiver
caducado.

**B16 — sem data, travado em B15, sem mudança de status.** Cada +1pp de
mistura obrigatória de biodiesel puxaria demanda adicional de óleo de soja
para o mercado interno (~+436 mil toneladas no B16 pleno), mas o CNPE segue
sem nova convocação.

**STJ REsp 2.165.276/2026 — crédito PIS/Cofins para esmagadoras sobre soja
usada em biodiesel, sem alteração.** Bullish para soja/óleo (alívio de
custo de entrada), mas ainda não vinculante (não é decisão repetitiva).

**Vetores dos EUA e Indonésia, sem mudança de status desde 2026-06-05:**
EPA-RFS-2026-2027 (volumes recordes de biocombustível, sustentando o RIN D4
fixo em 2,11 USD/RIN usado na margem de biodiesel); 45Z-CLEAN-FUEL (regra
que favoreceria óleo de soja doméstico americano frente a insumo importado,
pendente de regra final do Treasury/IRS); DANANTARA-INDONÉSIA
(centralização estatal da exportação de palma, assunção plena prevista para
01/09/2026, agora a **24 dias**); INDONESIA-B50 (provável B45 em 2026, B50
pleno só 2027-28); INDONESIA-LEVY-PMK9 (imposto de exportação de CPO até
12,5%, encarecendo palma). Conjunto estruturalmente bullish para óleo de
soja via substituição de palma, mas inverificável pelo lado de mercado
(MPOB inacessível, ver Honestidade) — e em tensão direta com a
backwardation observada na curva do óleo na última leitura, cuja ponta
longa (justamente os vencimentos que incluiriam o período pós-assunção
plena da Danantara) estava cedendo, não subindo — o mercado, pelos dados
disponíveis até quinta-feira, ainda não estava precificando esse suporte
estrutural.

**O monitor tributário como um todo está há 64 dias sem qualquer
atualização** — prioridade de manutenção do sistema, especialmente
relevante agora que a isenção PIS/Cofins se aproxima de uma semana útil
inteira vencida sem confirmação de status.

---

## Riscos e eventos próximos

**O COT (CFTC) referente a 04/08/2026 segue ausente, agora 11 dias desde o
último corte (28/07) — o dobro do intervalo semanal normal.** Vale
verificação direta com a CFTC se o próximo briefing (segunda-feira, 10/08)
também não trouxer o dado.

**A sessão de sexta-feira (07/08) da CBOT está ausente deste briefing** —
prioridade técnica: confirmar se o pipeline de coleta rodou normalmente na
sexta, antes de tratar qualquer gap de preço na abertura de segunda-feira
como movimento de mercado genuíno.

**O ratio Far/Soj fechou a última sessão conhecida em 80,60%, revertendo a
compressão do dia anterior — segunda-feira (10/08) é a primeira
oportunidade real de testar se essa reversão persiste**, o que enfraqueceria
ainda mais a tese do D+7 (agora 51 dias vencida), ou se reverte de volta
para a compressão.

**A backwardation da curva do óleo, no último retrato disponível,
aprofundava pelo segundo pregão seguido, com a ponta longa cedendo mais que
a curta** — segunda-feira é a primeira chance de saber se esse padrão
continua.

**O suporte técnico do óleo (72,00) seguia rompido, a -6,11%, no último
fechamento conhecido** — a reabertura de segunda-feira é o próximo teste
real.

**A isenção PIS/Cofins do biodiesel completa o 5º dia útil sem confirmação
de status, e só volta a avançar na segunda-feira** — item de verificação
manual mais urgente desta janela.

**O salto do físico de farelo no RS (R$ 1.640→1.800/ton) segue sem segunda
leitura de confirmação, agora há 3 dias.**

**O USDA Crop Progress rotulado 2026-08-02 segue com os MESMOS valores do
corte de 26/07**, agora pela quinta leitura seguida; o próximo corte,
referente à semana de 09/08, deve sair na segunda-feira seguinte (10/08).

**NOPA — fila `release-nopa-2026-08-06` sinaliza novo "release", mas o
dado segue inacessível**, agora mais de 8 semanas sem alternativa de dado
primário sobre o crush americano.

**MPOB — sem números de palma extraídos, mesma barreira de longa data.**

**O WASDE segue fora da janela deste briefing, agora 29 dias de atraso**
desde o último dado (10/07/2026).

**Danantara (Indonésia) assume plenamente a cadeia de exportação de palma
em 01/09/2026, a 24 dias de hoje** — monitorar se a curva do óleo CBOT
começa a precificar esse suporte estrutural, especialmente na ponta longa,
que na última leitura disponível estava se movendo na direção oposta.

---

## Honestidade

O que não foi possível validar neste briefing, cujo dado de mercado mais
recente é de 2026-08-06 (lido em 2026-08-08), e os pontos onde a confiança
é baixa:

**1. O achado central desta leitura: nenhuma fonte do briefing trouxe dado
novo desde a sessão de 2026-08-06 — nem CBOT, nem PTAX, nem NAG físico, nem
COT, nem RSS, nem INMET, nem ENSO, nem MPOB, nem BCBA.** Parte disso é
esperado por calendário (BCB não publica PTAX aos fins de semana; a CBOT não
opera aos sábados), mas a peça que **não** é explicada só pelo calendário é
a ausência completa da sessão de **sexta-feira, 2026-08-07** — um dia útil
normal de pregão na CBOT, que deveria ter gerado um carimbo de fechamento
para soja, farelo e óleo e não gerou. Esta leitura recomenda verificação
técnica direta do pipeline de coleta (`main.py` / scraper CME) antes de
segunda-feira, para garantir que o gap não se repita e para entender se
sexta-feira simplesmente não rodou ou se rodou e o resultado não chegou a
este briefing.

**2. O problema de qualidade de dado identificado na leitura de ontem
(campos de máxima, mínima e volume do farelo CBOT e de abertura do heating
oil idênticos entre carimbos de datas diferentes no mesmo dump) não pôde
ser testado novamente hoje**, porque não há sessão nova para comparar. Esta
leitura mantém a mesma reserva: os fechamentos de farelo, óleo e soja
seguem tratados como confiáveis (batem com o cálculo independente da seção
`indicators`), mas os extremos e volumes de farelo e heating oil do último
dump, não.

**3. O COT (CFTC) de 28/07/2026 segue sendo o dado de posicionamento mais
recente, agora 11 dias sem atualização — o dobro do intervalo semanal
padrão.** Esta leitura não tem como determinar se o atraso é da CFTC (fonte
primária) ou do pipeline de coleta do robô; recomenda-se checagem direta
antes de tratar a ausência continuada como normal.

**4. O prêmio de exportação de Paranaguá (soja) e o CEPEA Paraná interior
não trouxeram carimbo novo desde 2026-08-05** — agora 3 dias sem
atualização; qualquer menção ao prêmio físico nesta leitura parte desse
último carimbo, não de um dado mais recente.

**5. O salto do físico de farelo no Rio Grande do Sul (R$ 1.640,00/ton →
R$ 1.800,00/ton, registrado em 05/08) segue sem uma segunda leitura de
confirmação, agora há 3 dias** — esta leitura não pode nem confirmar nem
descartar o nível como represamento resolvido ou anomalia de coleta.

**6. A manchete "Soja em Mato Grosso atinge maior preço do ano, mas
indústria enfrenta desafios" (Canal Rural, 06/08/2026) segue sem corpo de
texto, número ou metodologia neste briefing** (campo `headline: None`), e
nenhum item novo de soja/farelo/óleo apareceu no RSS desde então. Esta
leitura trata a manchete como um dado qualitativo, com fonte e data, mas
sem poder verificar o nível de preço citado.

**7. O PTAX (BCB) não trouxe carimbo novo desde 2026-08-05** — a paridade
em reais calculada nesta leitura usa o câmbio de quarta-feira; qualquer
movimento cambial genuíno de quinta, sexta ou do próprio fim de semana não
está capturado.

**8. A interpretação causal da backwardation do óleo (ligação com
incerteza regulatória de biodiesel BR ou expectativa de mais oferta de
palma via Danantara) permanece uma hipótese desta série de leituras, não um
fato confirmado por nenhuma fonte do briefing** — e não pôde ser testada
novamente hoje por falta de dado novo. Nenhum dado de palma (MPOB bloqueado)
ou de biodiesel BR (monitor tributário parado) permite confirmar essa
hipótese diretamente.

**9. O ratio Far/Soj (80,60%) segue sem fechar abaixo de 80%, agora 51 dias
depois do checkpoint formal do D+7 (18/06/2026).** Esta leitura não conclui
que a tese original foi invalidada — apenas que não há dado novo desde
ontem para reavaliar, e mantém o D+90 (2026-09-09, a 32 dias) como próximo
marco formal.

**10. O USDA Crop Progress rotulado 2026-08-02 trouxe, pelo quinto dump
seguido, valores idênticos ao corte de 26/07/2026 (11%/52%/7%).** Esta
leitura não trata isso como semanas genuinamente estáveis de condição de
lavoura, e reforça a recomendação de reconferir no próximo corte esperado
(semana de 09/08, publicação em torno de segunda-feira, 10/08).

**11. A isenção PIS/Cofins do biodiesel — sem confirmação de renovação ou
caducidade neste briefing, agora no 5º dia útil desde o vencimento (o
contador só volta a andar na segunda-feira).** O monitor tributário está 64
dias sem atualização; esta leitura não presume nenhum dos dois cenários.

**12. O WASDE permanece completamente fora da janela deste briefing** —
agora 29 dias de atraso desde o último dado (10/07/2026).

**13. NOPA (`release-nopa-2026-08-06`) segue com `monthly_status` em 0,0
bool** — mesma barreira de assinatura paga, mais de 8 semanas sem
alternativa de dado primário.

**14. Palma malaia (MPOB) segue sem números extraídos**, mesmo conteúdo de
3.439 caracteres desde 30/07.

**15. Clima INMET (BR) não foi usado como driver de preço** — agosto é
entressafra da soja brasileira, sem relevância direta neste momento do
calendário agrícola; a última previsão capturada é para 06/08.

**16. Os forecasts estatísticos internos (bandas 7d/30d, geradas em
2026-08-06, a geração mais recente do briefing) não foram usados como
driver desta leitura** — são bandas MA20+volatilidade+slope, mecânicas
(soja 7d "baixista"/30d "baixista", farelo 7d "lateral"/30d "baixista",
óleo 7d "baixista"/30d "baixista"), sem incorporar a leitura qualitativa de
hoje; ficam registradas no briefing, mas esta leitura não as toma como
fonte de tese.

*Nenhum número foi inventado ou estimado além do que consta no briefing
lido em 2026-08-08 e nos insights anteriores referenciados. A contribuição
central desta leitura foi (1) identificar e documentar explicitamente que o
briefing de hoje não trouxe nenhum dado novo em nenhuma fonte desde a
sessão de 2026-08-06, com destaque para a ausência anômala da sessão de
sexta-feira 07/08 (que deveria existir por calendário e não existe),
recomendando verificação técnica do pipeline antes de segunda-feira; (2)
recalcular com precisão todos os contadores de dias da fila de julgamento e
da lente fiscal que avançam independente de haver pregão novo (D+7 do
ratio agora a 51 dias, D+90 a 32 dias, PIS/Cofins no 5º dia útil, MP 1.358
a 28 dias, WASDE a 29 dias de atraso, monitor tributário a 64 dias, RS sem
segunda leitura há 3 dias, Danantara a 24 dias); (3) separar explicitamente,
em cada seção, o que é estrutural e independe do calendário de pregões (ISF,
ISO, ABIOVE — a parte mais sólida desta leitura) do que é tático e depende
de confirmação por sessão nova (ratio, curva do óleo, oil-meal spread — hoje
"suspensos" no último estado conhecido); e (4) tratar os três itens da fila
de julgamento — `alerta-quebra_suporte-oleo_cbot-2026-08-06`,
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` e
`release-nopa-2026-08-06` — no contexto específico de um sábado sem sessão
nova, sem inventar confirmação, tonelagem ou percentil que o briefing não
trouxe.*
