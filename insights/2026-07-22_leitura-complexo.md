---
data: 2026-07-22
titulo: "Soja estende o rompimento para +3,87% sobre 1.180,00 com fechamento a 90,7% da máxima do dia; farelo rompe a resistência de 325,00 e o ratio Far/Soj sobe pelo 2º pregão seguido para 80,67%, tensionando a tese estrutural bear (ABIOVE) contra o preço; óleo encerra dois dias de fraqueza com o fechamento mais forte da semana, mas a margem de biodiesel comprime -12,1% porque o próprio custo do óleo sobe"
tags: [complexo, auto-claude]
fontes:
  - CBOT CME (ZSU26 soja / ZMU26 farelo / ZLU26 óleo + curva forward completa Q26-H27) — sessão de 2026-07-22
  - CME heating_oil_cbot (HO=F) — fechamento de 2026-07-22 (4,0806 USD/galão, volume de 451 contratos — normalização relevante frente aos 26 contratos de 21/07)
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, paridade BR, ISF, ISO) — 2026-07-22, com comparação contra os mesmos indicadores recalculados para 2026-07-21 dentro do próprio dump de hoje
  - BCB PTAX — 2026-07-22 (USD/BRL 5,0638, EUR/BRL 5,7803)
  - CEPEA/ESALQ Paranaguá e Paraná interior via NAG — 2026-07-22 (suporte Paranaguá R$ 145,45/saca, var +0,89%; Paraná interior R$ 137,84/saca, var +0,78%)
  - NAG Físico BR (farelo MT/IMEA, RS, Rondonópolis; prêmios export PGUA farelo/óleo) — 2026-07-22
  - CFTC COT Managed Money — ainda referência 2026-07-14, sem atualização (próximo corte foi 21/07, publicação normal ~24/07)
  - USDA Crop Progress — ainda 2026-07-19 (13% excelente + 53% boa + 6% ruim = 66% bom-ou-excelente), sem nova publicação
  - USDA WASDE — ainda 2026-07-10 (só farelo Argentina/Brasil/China parcial), sem publicação nova
  - NOPA — 2026-07-22, `monthly_status` continua em 0,0 bool (paywall), fila `release-nopa-2026-07-22` — a "novidade" é apenas a data de coleta
  - ABIOVE projeções mensais — balanços ago-dez/2026 (farelo/óleo/soja), sem alteração frente às leituras anteriores
  - NOAA CPC ENSO — 2026-07-22 (El Niño Advisory, sem mudança)
  - MPOB — 2026-07-22 (parser sem números extraídos, 3.439 caracteres, 13º dia consecutivo com o mesmo conteúdo, 10/07 a 22/07)
  - BCBA — 2026-07-22 (acessível, sem links de relatório detectados, mesmo padrão)
  - Notícias Agrícolas/Canal Rural/Farm Progress RSS — 2026-07-22 (160 itens lidos, 6 mantidos; manchete "Vazio sanitário da soja já começou em parte do Brasil; entenda por que ele é decisivo para proteger a próxima safra", Canal Rural)
  - Forecasts estatísticos internos — 2026-07-22 (oitava geração seguida com as seis bandas simultaneamente em viés altista)
  - system/tributario_watch.toml (lido apenas como referência, não editado) — MP-1358-2026, PIS/COFINS-BIODIESEL-ISENCAO, MP-1363-2026, STJ-RESP-2165276, B16-CNPE-2026, EPA-RFS-2026-2027, 45Z-CLEAN-FUEL, DANANTARA-INDONESIA, INDONESIA-B50, INDONESIA-LEVY-PMK9 — todos `atualizado_em` 2026-06-05 (47 dias sem atualização do monitor)
  - Cruza com [[2026-07-21_leitura-complexo]], [[2026-07-20_leitura-complexo]], [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (checkpoint D+7, tratado abaixo — hoje 34 dias vencido)
status: ativa
vies: [bull-soja, neutral-farelo, bull-oleo_soja]
---

> **Nota de proveniência:** a lacuna estrutural do dump persiste — a seção
> bruta `cme_cbot` de hoje traz o OHLC completo de soja, farelo, óleo e
> heating oil para 22/07/2026, mas, para 21/07/2026, só repete farelo e
> heating oil; soja e óleo daquele dia seguem disponíveis apenas de forma
> **implícita**, via a fórmula de crush margin que os próprios indicadores
> recalculam dentro do dump de hoje ("farelo 324,30 + óleo 73,41 − soja
> 1.210,50"). Isso já é a mesma falha documentada nas duas leituras
> anteriores — e note-se uma pequena divergência adicional: a leitura de
> ontem (21/07) registrou o fechamento da soja daquele dia em 1.210,25 e o
> ratio Far/Soj em 80,31%; o recálculo de hoje, para o mesmo dia, usa 1.210,50
> e chega a 80,37% — uma diferença de 0,25 ponto na soja e 0,06pp no ratio,
> pequena o bastante para não mudar nenhuma conclusão, mas grande o bastante
> para merecer registro (mais uma vez) como sintoma do mesmo problema de
> gerações sucessivas do pipeline recalculando o passado com valores
> ligeiramente distintos (ver Honestidade, item 1). Todos os deltas desta
> leitura usam o valor de 21/07 tal como recalculado **dentro do próprio dump
> de hoje**, por consistência interna. Feita a ressalva, os fatos: a soja
> fechou em 1.225,75 cts/bushel, um ganho de +1,26% sobre o fechamento
> implícito de ontem e o segundo dia forte seguido, fechando a 90,7% do range
> do dia — a vela mais decidida da semana (trata
> `alerta-quebra_resistencia-soja_cbot-2026-07-22`). O farelo subiu ainda
> mais em termos relativos (+1,63%) e **rompeu a resistência de 325,00**,
> fechando em 329,60 (trata `alerta-quebra_resistencia-farelo_cbot-2026-07-22`)
> — e é esse ganho relativo do farelo sobre a soja que empurrou o ratio
> Far/Soj para 80,67%, o segundo pregão seguido acima do limiar de 80% e,
> desta vez, **subindo**, não apenas cruzando (trata a revisão vencida
> `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, hoje
> 34 dias vencida). O óleo fechou em 74,39 cts/lb, o fechamento mais forte da
> semana (89,5% do range), encerrando a sequência de dois dias de fricção
> tática — mas a margem de biodiesel americana comprimiu -12,1% no dia, não
> por queda do heating oil, e sim porque o próprio custo do óleo (insumo do
> biodiesel) subiu junto com o rali do contrato CBOT.

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
bushel↔short ton, "sht"): abaixo de 80% o farelo está historicamente
"abundante" frente à soja (zona bear); acima de 87%, "apertado" (zona bull);
entre os dois, zona "neutra". É um spread de **mean-reversion** — funciona
nos dois lados.

**Hoje é o dia em que o mecanismo do complexo produziu o resultado mais raro
das últimas semanas: as três pernas subiram juntas, e por magnitudes
crescentes na ordem farelo > soja > óleo.** A soja fechou em 1.225,75
cts/bushel (CBOT, 22/07/2026), +1,26% sobre o fechamento implícito de ontem;
o farelo fechou em 329,60 USD/short ton, +1,63%; o óleo fechou em 74,39
cts/lb, +1,33%. Como o ratio Far/Soj mede farelo *relativo* à soja, e hoje o
farelo subiu mais (proporcionalmente) que a soja, o ratio subiu de 80,37%
para 80,67% (+0,30 ponto percentual) — o **segundo pregão seguido** acima do
limiar de 80%, e desta vez em trajetória de alta, não apenas de cruzamento
pontual como na sessão de 21/07. A crush margin, pela mesma lógica (produtos
subindo mais que o custo do insumo), se expandiu +2,32% (de 3,1047 para
3,1766 USD/bushel). **É este o fato mais importante da leitura de hoje**: o
farelo, que a tese estrutural da ABIOVE classifica como estruturalmente
"sobrando" (Índice de Sobra de Farelo em 80/100, inalterado há semanas),
acabou de romper uma resistência técnica (325,00) e de acumular dois pregões
seguidos empurrando o ratio para cima — uma divergência crescente entre o
que o preço está fazendo agora e o que a tese estrutural, calibrada em
11/06/2026, previu que aconteceria. **O que mudou hoje:** (1) a soja estendeu
o rompimento de 1.180,00 para +3,87%, com o fechamento mais decidido da
semana (trata `alerta-quebra_resistencia-soja_cbot-2026-07-22`); (2) o
farelo rompeu pela primeira vez nesta janela a resistência de 325,00 (trata
`alerta-quebra_resistencia-farelo_cbot-2026-07-22`); (3) a revisão D+7 da
tese bear do farelo, 34 dias vencida, ganha um segundo dado tático contra o
critério original — o ratio não só deixou de fechar <80%, como agora sobe
por dois pregões seguidos (trata
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`); e (4)
o óleo encerrou a sequência de dois dias fracos com o fechamento mais forte
da semana, mesmo com a margem de biodiesel comprimindo por um motivo
diferente do heating oil desta vez. **Leitura de uma linha:** o pivô do
complexo hoje é o farelo — convicção moderada-alta em soja (tendência tática
intacta e reforçada, segundo dia de vela forte), **neutra, mas com viés
altista crescente** em farelo (o preço está, pela segunda sessão seguida,
contradizendo a tese estrutural bear, e uma resistência técnica caiu — mas a
disciplina que a própria leitura de ontem recomendou, de exigir 2-3 sessões
antes de tratar um cruzamento como sinal de regime, ainda pede mais uma
confirmação antes de virar a tese) e moderada-alta em óleo (a fricção tática
de dois dias terminou com um fechamento forte, a tese estrutural nunca
saiu do lugar, mas a margem de biodiesel comprimindo por conta do próprio
rali do óleo é um lembrete de que o "óleo caro" tem um lado ruim para quem
processa biodiesel).

---

## Soja

**Viés: bull tático reforçado. Fechou em 1.225,75 cts/bushel na sessão de
22/07/2026 (CBOT, ticker ZSU26.CBT, vencimento set/26), 3,87% acima da
resistência de 1.180,00 — a maior distância desde o rompimento. Trata
`alerta-quebra_resistencia-soja_cbot-2026-07-22`.**

### O que sustenta a tese

**A vela de hoje é a mais decidida da semana, e reverte por completo o sinal
de fadiga do dia anterior.** Abertura 1.209,75, fechamento 1.225,75 (+16,00,
+1,32% frente à própria abertura), mínima 1.206,25, máxima 1.227,75, volume
29.488 contratos (CBOT, 22/07/2026). O fechamento ficou em 90,7% do range do
dia ((1.225,75-1.206,25) ÷ (1.227,75-1.206,25)) — a sessão abriu perto da
mínima, testou o fundo cedo e subiu de forma quase ininterrupta até fechar
colada na máxima. Frente ao fechamento implícito de ontem (1.210,50 cts/bu,
ver nota de proveniência), o ganho foi de +15,25 pontos (+1,26%) — o
contrário exato do que a leitura de ontem descreveu como "primeiro dia de
devolução desde o rompimento": hoje não só a devolução não se repetiu, como
foi mais que compensada em uma única sessão. **Isso resolve, na prática, a
dúvida que a própria leitura de ontem havia levantado** ("a diferença entre
pausa saudável e início de reversão só fica clara com mais uma sessão") — a
resposta de hoje é pausa saudável, não reversão.

**A curva forward mantém o formato de "sorriso" já documentado, com a ponta
curta ligeiramente mais descontada e a ponta longa estável.** Agosto/26
(Q26) 1.232,75 → Setembro/26 (U26, contrato de referência/spot) 1.225,75
(desconto de -7,00, -0,57%) → Novembro/26 (X26) 1.238,25 (recupera +12,50
sobre setembro, +1,02%) → Janeiro/27 (F27) 1.252,00 (+13,75 sobre novembro,
+1,11%) → Março/27 (H27) 1.252,75 (+0,75, +0,06%, praticamente estável). O
desconto do spot frente ao mês anterior encolheu ligeiramente (-0,57% hoje
ante -0,68% ontem) e o prêmio da ponta longa (janeiro sobre novembro) se
manteve praticamente igual (+1,11% hoje vs +1,13% ontem) — a curva absorveu
o rali do spot sem mudar de formato, o que é consistente com um movimento de
preço à vista, não uma reprecificação de expectativa de oferta futura.

**A paridade teórica em reais subiu para R$ 136,84/saca 60kg** (indicadores,
CBOT 1.225,75 cts × PTAX 5,0638 USD/BRL de 22/07/2026), um ganho de +1,33
(+0,98%) frente aos R$ 135,51/saca implícitos de ontem. O câmbio reforçou
ligeiramente a alta em dólar: o real se apreciou (USD/BRL caiu de 5,0780
para 5,0638, -0,28%) no mesmo dia em que a soja em dólar subiu +1,26% — os
dois efeitos vão em direções opostas desta vez (mais dólares por bushel, mas
cada dólar valendo um pouco menos em reais), o que suavizou ligeiramente o
ganho líquido em reais (+0,98%) frente ao ganho isolado em dólar (+1,26%).
**O físico de Paranaguá segue na mesma direção do papel, mantendo o prêmio
estável**: fechou em R$ 145,45/saca (CEPEA/ESALQ via NAG, var +0,89% no
dia), um prêmio de R$ 8,61/saca (+6,29%) sobre a paridade teórica — bem
próximo do prêmio de +6,39% de ontem, sugerindo que o mercado físico não
está mais se descolando do papel como havia feito na sessão anterior (quando
o papel caiu e o físico subiu). Isso é coerente com a notícia do dia (Canal
Rural, 22/07/2026: "Vazio sanitário da soja já começou em parte do Brasil;
entenda por que ele é decisivo para proteger a próxima safra") — uma
manchete sobre o período de vazio sanitário (janela obrigatória sem soja
"tiguera"/voluntária no campo, usada para quebrar o ciclo de pragas e
doenças como a ferrugem asiática antes do plantio de outubro/26) que **não
traz número de preço ou de área e por isso não é tratada como driver desta
leitura** — é contexto de calendário agrícola para a próxima safra, sem
impacto direto na tese de preço de hoje.

**A soja no Paraná interior (CEPEA/ESALQ via NAG) fechou em R$ 137,84/saca**
(var +0,78% no dia), um prêmio de +R$ 1,00 (+0,73%) sobre a paridade teórica
de R$ 136,84/saca — dentro da faixa normal de custo logístico, sem sinal de
estresse na base doméstica.

**O USDA Crop Progress segue parado em 19/07/2026** (13% excelente + 53% boa
+ 6% ruim = 66% bom-ou-excelente), sem atualização nova. A próxima
publicação semanal é esperada por volta de 26/07/2026.

**O COT (CFTC) permanece com o mesmo dado de referência, 14/07/2026.**
Managed money net long em soja em +75.191 contratos (7,48% do open interest
de 1.004.746). O corte semanal que vai capturar o rompimento de 1.180,00, a
confirmação de 20/07, a devolução parcial de 21/07 e o rali de hoje ocorreu
ontem (21/07); a publicação normal (~24/07) é o primeiro dado de
posicionamento capaz de dizer se os fundos compraram durante essa janela
inteira de volatilidade, ou se ficaram de lado.

**Os forecasts estatísticos internos (22/07/2026)** seguem altistas: central
7d = 1.252,68 cts/bu (bandas 1.199,62-1.305,74); central 30d = 1.355,16
cts/bu (bandas 1.245,32-1.465,00) — ambos deslocados para cima frente a
ontem, absorvendo o rali de hoje, mas o modelo reage a momentum recente, não
a fundamentos.

### O que invalida / risco para a soja

- **Um fechamento amanhã abaixo de 1.206,25 (mínima de hoje) ou de 1.180,00
  (resistência/suporte original)** encerraria a leitura tática de
  continuidade.
- **O COT de 21/07 (publicação ~24/07) mostrar que os fundos venderam** ou
  ficaram de lado durante a semana do rompimento — reduziria a confiança de
  que o movimento tem lastro em fluxo real, não apenas em preço.
- **O Crop Progress, quando atualizado (~26/07), mostrar nova melhora** na
  condição da lavoura americana — reforçaria o argumento de oferta potencial
  maior, contrário à tese tática de alta.
- **O prêmio físico de Paranaguá (hoje 6,29% sobre a paridade) voltar a
  esticar sem correspondência no papel** — repetiria o padrão de descolamento
  visto em 21/07 e sinalizaria um mercado físico mais tensionado do que o
  CBOT sozinho sugere.

### Leitura operacional — soja

O rali de hoje resolve, a favor da continuidade, a dúvida tática que a
leitura de ontem havia deixado em aberto: a devolução de -0,43% não se
repetiu, foi mais que revertida, e o fechamento a 90,7% do range é o mais
forte da semana. Para quem está comprado alinhado ao rompimento, não há
qualquer motivo para reduzir posição — pelo contrário, a distância sobre
1.180,00 (+3,87%) dá mais espaço de manobra antes do stop lógico de fundo.
1.206,25 (mínima de hoje) é a referência tática mais próxima; 1.180,00
continua sendo o nível estrutural. Para quem está vendido contra o
rompimento, o dia de hoje invalida o único argumento tático que a sessão
anterior havia oferecido — a posição vendida direcional em soja outright
está, neste momento, sem qualquer sustentação de preço, restando apenas a
expectativa de que o COT de sexta (~24/07) revele um posicionamento de
fundos mais fraco do que o preço sugere.

---

## Farelo

**Viés: neutro tático com viés altista crescente — o segundo pregão seguido
em que o preço contradiz a tese estrutural bear, mas ainda sem as 2-3
sessões de confirmação que a própria leitura de ontem recomendou exigir.
Estrutural, ainda bear via ABIOVE/ISF. O ratio Far/Soj fechou em 80,67%
(indicadores, farelo 329,60 ÷ soja 1.225,75, base normalizada), subindo
+0,30 ponto percentual frente aos 80,37% de ontem (valor recalculado dentro
do dump de hoje) e permanecendo, pela segunda sessão seguida, acima do
limiar de 80% — desta vez em alta, não apenas cruzando. Trata
`alerta-quebra_resistencia-farelo_cbot-2026-07-22` e a revisão vencida
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`.**

### O que sustenta a tese

**O farelo rompeu hoje a resistência técnica de 325,00 — um evento distinto
e independente do whipsaw do ratio, e por isso um dado com peso próprio.**
Fechamento 329,60 USD/short ton (CBOT, ticker ZMU26.CBT, sessão de
22/07/2026), abertura 323,50, mínima 323,50 (a própria abertura foi a
mínima do dia — sessão sem teste de baixa), máxima 332,60, volume 35.027
contratos — um ganho de +6,10 (+1,89%) frente à própria abertura e de +5,30
(+1,63%) frente ao fechamento de ontem (324,30, valor real, não implícito).
O fechamento ficou em 67,0% do range do dia ((329,60-323,50)÷(332,60-323,50))
— um candle sólido, ainda que menos extremo que o da soja hoje. Trata
`alerta-quebra_resistencia-farelo_cbot-2026-07-22`: o nível de 325,00 não
havia sido testado com sucesso nas sessões recentes desta janela (farelo
fechou a 324,30 ontem, 321,20 anteontem), e o rompimento de hoje, por vir
acompanhado de volume normal (35.027 contratos, dentro da faixa recente) e
de uma vela sem sombra inferior relevante, tem mais credibilidade tática do
que um simples cruzamento de ratio perto de um número redondo.

**O ratio Far/Soj subiu pela segunda sessão seguida, e desta vez em
trajetória, não apenas em cruzamento pontual.** A sequência completa nesta
janela: 79,71% (17/07) → 79,28% (20/07) → 80,37% (21/07, recalculado hoje) →
**80,67% (22/07)**. Isso muda o caráter da observação: na leitura de ontem, o
cruzamento de volta acima de 80% foi tratado como possível ruído (o mesmo
nível havia sido cruzado para baixo e para cima em sessões consecutivas). Hoje,
o ratio não voltou a cruzar — ele **subiu depois de já estar acima do
limiar**, o segundo dado consecutivo na mesma direção. Isso ainda não são as
"2-3 sessões consecutivas do mesmo lado" que a própria leitura de ontem
definiu como critério para tratar o sinal como confiável — mas é a primeira
vez, desde o início desta janela de observação, que esse critério está a
apenas uma sessão de distância de ser satisfeito.

**Tratando `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`:**
a revisão programada da tese original (insight
[[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]), com data-alvo
18/06/2026, está hoje **34 dias vencida**. A tese original apostava em três
pilares: ratio comprimindo para <80% (o "gatilho" tático), prêmio de
exportação zerado (ainda verdadeiro — ver abaixo) e estrutura de crush
favorecendo o óleo (também ainda verdadeiro). **O pilar tático — o único dos
três com um número de preço explícito e verificável dia a dia — acumula
agora dois pregões seguidos na direção CONTRÁRIA à tese**, somados a um
rompimento de resistência técnica independente. A avaliação honesta desta
revisão, depois de 34 dias e mais um dia de dado novo, é que **o critério
tático da tese de 11/06 está mais perto de ser invalidado do que confirmado**
— mas a recomendação desta leitura, seguindo a mesma disciplina que a
própria leitura de ontem estabeleceu diante do whipsaw anterior, é não
fechar o veredito ainda: falta uma terceira sessão de confirmação do lado de
cima antes de tratar a reversão como definitiva, e os critérios
fundamentalistas (WASDE, parado desde 10/07 e sem nenhum dado de soja/óleo
americano; NOPA, ainda com `monthly_status` em 0,0 bool) continuam sem
resposta. Os checkpoints estruturais D+90 (09/09/2026) e D+180
(08/12/2026) seguem sendo o critério de mais alta confiança para julgar a
tese ABIOVE ao longo do tempo — o que está em xeque agora é apenas o
critério tático de curtíssimo prazo, não a tese estrutural inteira.

**A crush margin se expandiu +2,32% no dia, de 3,1047 para 3,1766 USD/bushel**
(Board Crush: farelo 329,60 + óleo 74,39 − soja 1.225,75) — a segunda
expansão seguida depois da forte recuperação de ontem (+2,09%). O mecanismo:
farelo e óleo, juntos, subiram mais em termos absolutos do que a soja (o
insumo), o que mecanicamente amplia a margem do board crush — um sinal, em
tese, de que a esmagadora tem incentivo crescente para acelerar o ritmo de
processamento, o que por sua vez tende a aumentar a oferta de farelo no
mercado interno (reforçando, e não contradizendo, o argumento estrutural da
ABIOVE sobre excedente).

**O oil-meal spread (óleo menos farelo, por bushel) comprimiu apenas
marginalmente, para 0,9317 USD/bu**, ante 0,9405 ontem — uma queda de
-0,94%, uma fração das compressões de -8,47% e -10,65% registradas nas duas
sessões anteriores. **A desaceleração da compressão é, em si, informativa**:
sugere que o movimento de "farelo recuperando terreno relativo ao óleo" está
estabilizando, não mais acelerando — consistente com o oil share do óleo
também mostrando sinais de estabilização (ver seção Óleo).

**A trajetória projetada da ABIOVE (sem alteração) segue sendo o pilar mais
sólido do argumento estrutural, porque não depende do preço do dia.** A
exportação de farelo brasileiro projetada cai de 1.400 mil toneladas em
agosto/2026 para 700 mil toneladas em dezembro/2026 (-50% em quatro meses),
enquanto a produção cai de forma bem mais suave (2.285,06 → 1.659,04 mil
toneladas no mesmo período, -27,4%) — menos farelo saindo pelo porto, com
produção caindo bem menos que a exportação, empurra o volume excedente para
o mercado interno de ração. Esse mecanismo estrutural não é afetado pelo
rompimento tático de hoje — mas também não impede que o preço, no curto
prazo, suba por outras razões (posicionamento de fundos, força relativa da
soja puxando o complexo inteiro).

**As praças físicas de farelo no Brasil (NAG, 22/07/2026) seguem
completamente estáveis**, sem variação em nenhuma das três: Mato Grosso/IMEA
R$ 1.602,80/ton (var 0,0%), Rio Grande do Sul R$ 1.640,00/ton (var 0,0%), e
Rondonópolis/MT R$ 1.650,00/ton (var 0,0%) — a praça de Rondonópolis
completa o terceiro dia seguido no patamar elevado de R$ 1.650,00/ton
(desde o salto de +3,13% em 20/07), sem propagar para as outras duas praças
e sem reverter. O prêmio de exportação em Paranaguá segue em +0,05 USD/short
ton (julho/26, NAG), agora **19 dias corridos sem qualquer variação** desde
03/07/2026 — o físico exportador segue tão parado quanto na tese original de
11/06/2026 ("prêmio de exportação zerado"), o pilar que mais resiste ao
whipsaw do preço-papel.

**O Índice de Sobra de Farelo (ISF) permanece em 80/100 (4 de 5 condições
estruturais)**, inalterado desde pelo menos 01/07/2026 — mais uma
confirmação de que o índice captura condições estruturais (ABIOVE, crush,
oferta), não a mecânica tática de preço de curto prazo.

**O COT de 14/07/2026, sem atualização, mantém o mesmo contraponto relevante
à tese bear.** Managed money net long em farelo em +46.576 contratos (7,77%
do open interest de 599.353) — mais que dobrado frente à semana anterior
(+18.722 em 07/07). Com o preço rompendo resistência hoje e o ratio subindo
pela segunda sessão, esse posicionamento comprado dos fundos ganha ainda
mais relevância: se o COT de sexta (~24/07) confirmar que os fundos
continuaram a comprar farelo durante a semana do rompimento, a tese bear
estrutural pode enfrentar squeeze — posição vendida direcional contra um
mercado que rompe resistência E tem fundos comprados é a pior combinação de
risco para quem está short outright.

**O forecast estatístico do farelo (22/07/2026)** segue com viés altista:
central 7d = 335,35 USD/sht (bandas 321,66-349,04); central 30d = 358,44
USD/sht (bandas 330,10-386,78) — ambos deslocados para cima frente a ontem,
absorvendo o rompimento de hoje, e cada vez mais alinhados (não mais em
divergência) com o sinal tático de preço, ainda que continuem desalinhados
com a tese fundamentalista ABIOVE.

### O que invalida / risco para o farelo

- **Um fechamento amanhã de volta abaixo de 325,00 (a resistência rompida
  hoje) ou abaixo de 80% no ratio** desfaria o sinal tático em uma única
  sessão — exatamente o padrão de whipsaw que a leitura de ontem já
  documentou uma vez nesta mesma janela.
- **O ratio precisa de uma terceira sessão consecutiva acima de 80% e em
  alta** para que o critério tático da revisão D+7 seja tratado como
  efetivamente revertido, não apenas em tendência.
- **O COT de 21/07 (publicação ~24/07) mostrar os fundos continuando a
  aumentar o net long em farelo** — com o preço já rompendo resistência, o
  risco de squeeze numa posição vendida direcional aumenta a cada dado
  novo.
- **A crush margin continuar se expandindo** — se a esmagadora acelerar o
  ritmo de processamento em resposta a uma margem maior, o excedente de
  farelo projetado pela ABIOVE pode chegar mais rápido do que o calendário
  sugere, o que paradoxalmente reforçaria a tese estrutural bear no médio
  prazo mesmo com o preço tático em alta agora.
- **NOPA seguir inacessível indefinidamente**, sem confirmação do
  esmagamento americano para os checkpoints D+90 (09/09/2026) e D+180
  (08/12/2026).

### Leitura operacional — farelo

Hoje é o dia em que a recomendação prática muda de tom, sem ainda virar de
lado por completo: o rompimento de 325,00, somado ao segundo dia seguido de
ratio em alta acima de 80%, é evidência mais forte do que o simples
cruzamento de ontem — mas ainda não são as 2-3 sessões de confirmação que a
disciplina desta própria série de leituras exige antes de tratar um sinal
como definitivo. Para quem está vendido direcional em farelo outright
alinhado à tese estrutural da ABIOVE, a assimetria de risco continua
piorando: dois dados táticos consecutivos contra a posição (ratio subindo,
resistência rompida), fundos net long mais que dobrados nas últimas semanas,
e nenhuma confirmação fundamentalista nova (WASDE/NOPA) para compensar. A
recomendação é reduzir o tamanho da posição vendida direcional, ou migrá-la
para o veículo mais defensável — o spread farelo/soja ou o crush completo —
até a terceira sessão de confirmação aparecer em qualquer direção. Para quem
está comprado tático em farelo desde o rompimento de hoje, 325,00 (agora
suporte) e o fechamento de hoje (329,60) são as referências mais próximas
para stop; o gatilho de invalidação mais claro é um fechamento de volta
abaixo de 325,00.

---

## Óleo

**Viés: bull estrutural mantido (oil share ainda acima de 50%, ISO no teto de
100/100) e a fricção tática de dois dias terminou hoje com o fechamento mais
forte da semana. Fechou em 74,39 cts/lb na sessão de 22/07/2026, um ganho de
+1,33% frente ao fechamento de ontem (73,41, recalculado hoje). O oil share
recuou apenas marginalmente para 53,0%.**

### O que sustenta a tese

**A vela de hoje reverteu, com folga, os dois dias de fechamento fraco
documentados nas leituras anteriores.** Fechamento 74,39 cts/lb (CBOT,
ticker ZLU26.CBT, 22/07/2026), abertura 73,48, mínima 72,68, máxima 74,59 —
um ganho de +0,91 (+1,24%) frente à própria abertura e de +0,98 (+1,33%)
frente ao fechamento implícito de ontem. O fechamento ficou em 89,5% do
range do dia ((74,39-72,68)÷(74,59-72,68)) — o oposto exato do padrão dos
dois dias anteriores (40,7% e 53,3% do range, fechamentos na metade inferior)
e o fechamento relativo mais forte de toda a semana, incluindo o rali
original que motivou a tese estrutural. **Isso resolve a dúvida tática que
as duas leituras anteriores levantaram** — a sequência de dois fechamentos
fracos não evoluiu para uma reversão de tendência, e sim para uma pausa que
hoje se encerrou com uma retomada decidida.

**A curva forward aprofundou ainda mais a backwardation (desconto crescente
nos vencimentos mais distantes), mantendo o padrão já documentado.** Agosto/26
(Q26) 75,36 → Setembro/26 (U26, spot) 74,39 (-0,97, -1,29%) → Outubro/26
(V26) 73,46 (-0,93, -1,25%) → Dezembro/26 (Z26) 72,73 (-0,73, -0,99%) →
Janeiro/27 (F27) 72,24 (-0,49, -0,67%) — uma queda total de -3,12 cts/lb
(-4,14%) de agosto a janeiro/27, ligeiramente mais acentuada que os -4,11% de
ontem. A força segue concentrada no vencimento mais próximo — a assinatura
característica de um mercado com aperto físico de curto prazo mais do que
uma reprecificação estrutural de toda a curva, o mesmo padrão de semanas
anteriores.

**A margem de biodiesel americano comprimiu -12,1% no dia, para 0,8663
USD/galão** (receita 7,2456 = heating oil 4,0806 + 1,5×RIN 2,11; custo
6,3792 = óleo 5,5792 + industrial 0,80), ante 0,9858 ontem. **O mecanismo
por trás desta queda é diferente do das duas sessões anteriores, e vale
destrinchar**: nos dois dias passados, a compressão veio principalmente do
heating oil caindo (a receita do biodiesel). Hoje, o heating oil de fato
caiu um pouco (-1,11%, de 4,1266 para 4,0806 USD/galão), mas o fator
dominante foi outro: **o custo do óleo (insumo do biodiesel) subiu +1,33%**,
acompanhando o próprio rali do contrato CBOT que, para o operador de ZL, é
bullish. Esse é o lado B do rali do óleo: o mesmo movimento que é positivo
para quem está comprado no contrato futuro de óleo de soja é negativo para
quem processa esse óleo em biodiesel e vende o produto final a um preço que
não sobe na mesma proporção — a margem do refinador aperta exatamente quando
o insumo que ele compra fica mais caro mais rápido do que o produto que ele
vende. **A boa notícia para a confiabilidade deste dado**: o volume do
heating oil normalizou para 451 contratos hoje, ante apenas 26 ontem e 109
anteontem — a maior liquidez de toda a janela recente, o que dá muito mais
credibilidade ao nível de 4,0806 do que aos dois dias anteriores (ver
Honestidade).

**O Índice de Suporte do Óleo (ISO) permanece em 100/100 (5 de 5 condições)**,
inalterado desde pelo menos 01/07/2026 — a tese estrutural (óleo dominando o
valor do crush) segue intacta e não foi abalada pela fricção tática dos
últimos dois dias, nem alterada pelo rali de hoje.

**O oil share recuou apenas marginalmente para 53,0%** (indicadores,
22/07/2026), ante 53,09% ontem — uma queda de -0,07 ponto percentual, a
quarta queda seguida (53,83%→53,47%→53,09%→53,02%), mas a menor magnitude da
sequência, coerente com a desaceleração do oil-meal spread descrita na seção
Farelo. O óleo segue, ainda assim, capturando a maior fatia do valor do
crush, com a tendência de recuo claramente perdendo força.

**O COT de 14/07/2026, sem atualização, mantém o óleo como a perna mais
"concorrida" das três.** Managed money net long em +107.945 contratos
(16,92% do open interest de 638.102) — o mais alto das três pernas por larga
margem. Com o fechamento forte de hoje encerrando dois dias de fraqueza, o
risco de que esse posicionamento concentrado amplifique uma eventual
correção futura segue sendo o maior fator de risco estrutural de médio
prazo, mas o dado de preço de hoje não aponta, por ora, para essa correção.

**O forecast estatístico do óleo (22/07/2026)** mantém o viés altista:
central 7d = 76,16 cts/lb (bandas 71,41-80,91); central 30d = 82,99 cts/lb
(bandas 73,16-92,83) — deslocado para cima frente a ontem, absorvendo o
rali de hoje.

### O que invalida / risco para o óleo

- **Um fechamento abaixo de 72,68 (mínima de hoje)** reabriria o cenário de
  correção depois do rali, embora hoje esse nível esteja mais distante do
  que estava a mínima da sessão anterior.
- **O posicionamento dos fundos (net long em 16,92% do OI, o mais concorrido
  das três pernas) sofrer uma reversão** quando o próximo COT chegar
  (~24/07) — o risco estrutural de médio prazo mais relevante, independente
  do preço de hoje.
- **A margem de biodiesel continuar comprimindo por conta do custo do óleo
  subindo** — se sustentado, é um headwind de demanda para o próprio óleo
  via canal biodiesel (menor margem do refinador reduz incentivo a comprar
  óleo para processar), uma tensão interna que vale monitorar mesmo com o
  ISO em 100/100.
- **MPOB seguir inacessível** — impossível avaliar o efeito do El Niño ou
  das restrições/levy indonésias sobre o prêmio de substituição via palma.
  Hoje é o 13º dia consecutivo com o mesmo conteúdo sem números extraídos.

### Leitura operacional — óleo

O fechamento de hoje encerra, com um sinal forte, a dúvida tática que as
duas sessões anteriores haviam levantado — a fricção não evoluiu para
reversão. Para quem está comprado direcional em óleo desde o rompimento
original, a recomendação de apertar o stop perto da mínima recente pode ser
relaxada um pouco: a mínima de hoje (72,68) já está mais distante do
fechamento do que estava a de ontem, dando mais espaço de manobra. Para quem
opera exposição relativa dentro do crush, a desaceleração da compressão do
oil-meal spread (-0,94% hoje, ante -8,47% e -10,65% nas duas sessões
anteriores) sugere que a divergência farelo-forte/óleo-fraco pode estar
perto de se estabilizar — momento de reavaliar, não necessariamente reduzir
mais, a exposição relativa a favor do óleo. O ponto mais sutil da leitura de
hoje para quem acompanha o canal de demanda: a compressão da margem de
biodiesel via custo do óleo (não via heating oil) é um lembrete de que o
próprio sucesso do rali do óleo, se sustentado, pode começar a esfriar a
demanda marginal do biodiesel doméstico americano — um mecanismo de
autolimitação que vale observar nas próximas semanas, especialmente
combinado com o vencimento em 9 dias da isenção PIS/Cofins do biodiesel
brasileiro (ver Lente fiscal).

---

## Spreads e crush — leitura de complexo

### Crush margin: 3,1766 USD/bu — segunda expansão seguida, farelo e óleo lideram sobre a soja

A crush margin subiu +2,32% no dia (de 3,1047 para 3,1766 USD/bu), a segunda
expansão seguida depois da recuperação de +2,09% de ontem. O mecanismo:
farelo (+1,63%) e óleo (+1,33%) subiram mais, em conjunto, do que a soja
(+1,26%, o insumo) — um sinal de que a esmagadora tem incentivo econômico
crescente para processar mais soja, o que tende a aumentar a oferta futura
de farelo (reforçando o argumento estrutural ABIOVE) mesmo com o preço
tático do farelo em alta agora.

### Ratio Far/Soj: 80,67% — segundo pregão seguido acima de 80% e em alta, não apenas cruzando

O achado tático central desta leitura: depois do whipsaw de 79,28%→80,37%
documentado ontem, o ratio de hoje não cruzou o limiar — ele **subiu depois
de já estar acima dele** (80,37%→80,67%), o primeiro par de sessões
consecutivas na mesma direção desde que esta janela de observação começou a
acompanhar o nível de 80%. Trata `alerta-quebra_resistencia-farelo_cbot-2026-07-22`
e a revisão `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
(agora 34 dias vencida, critério tático mais perto de invalidado do que
confirmado — ver seção Farelo). Falta uma terceira sessão de confirmação
para tratar o sinal como estabelecido, seguindo a mesma disciplina que a
leitura de ontem definiu diante do whipsaw anterior.

### Oil share: 53,0% — quarta queda seguida, mas desacelerando com força

Recuo de apenas -0,07 ponto percentual frente a ontem (53,09%→53,02%), a
quarta queda seguida (53,83%→53,47%→53,09%→53,02%) desde 17/07, mas a menor
magnitude da sequência por larga margem — sugere que o recuo do oil share
está perdendo força, coerente com a desaceleração do oil-meal spread.

### Oil-meal spread: 0,9317 USD/bu — compressão marginal, ritmo de duas sessões anteriores não se repetiu

Queda de apenas -0,94% no dia (0,9405→0,9317 USD/bu), uma fração das
compressões de -8,47% (21/07) e -10,65% (22/07 na leitura anterior, referente
à sessão de 21/07) registradas nas duas sessões anteriores. A desaceleração
acompanha a do oil share — o farelo parece estar consolidando o ganho
relativo recente sobre o óleo, não mais acelerando a recuperação.

### Margem de biodiesel: 0,8663 USD/gal — maior compressão da janela, mas agora com liquidez normal

A margem caiu -12,12% no dia, a maior queda de uma sessão nesta janela —
mas, ao contrário das duas quedas anteriores (lideradas pelo heating oil em
baixíssimo volume), esta foi liderada pelo custo do próprio óleo subindo
(+1,33%, acompanhando o rali do CBOT), com o heating oil normalizando para
451 contratos de volume (ante 26 ontem). Isso torna o dado de hoje mais
confiável do que os dois anteriores, ainda que por um mecanismo diferente —
ver seção Óleo para a explicação completa do "lado B" do rali.

### COT: sem atualização, publicação normal ~24/07 — o evento mais aguardado da semana

O dado de 14/07/2026 segue sendo o mais recente. A publicação normal
(~24/07, sexta-feira) vai mostrar, pela primeira vez, o posicionamento dos
fundos durante toda a janela de volatilidade desta semana — rompimento da
soja, rompimento do farelo, e o fim da fricção tática do óleo. É o dado mais
importante em aberto para as três pernas.

### ISF em 80/100, ISO em 100/100 — inalterados, mas a divergência com o preço tático do farelo cresce

O Índice de Sobra de Farelo (4/5 condições) e o Índice de Suporte do Óleo
(5/5 condições) permanecem exatamente nos mesmos níveis de semanas
anteriores. Para o óleo, isso é simplesmente consistência — o rali de hoje
confirma, não contradiz, o índice. **Para o farelo, a divergência entre o
índice estrutural (ainda bear) e o preço tático (rompendo resistência, ratio
subindo por dois dias) é o ponto mais importante para monitorar nos
próximos dias** — os índices capturam condições estruturais que não mudam
de um dia para o outro, mas dois dias seguidos de preço na direção oposta
começam a testar a paciência de quem opera a tese estrutural sem hedge
tático.

### O que os índices dizem juntos em 22/07/2026

ISF 80/100 + ISO 100/100 (ambos inalterados) + ratio Far/Soj subindo pelo
segundo dia seguido para 80,67% (a primeira confirmação de dois dias na
mesma direção desta janela) + crush margin em segunda expansão seguida +
oil-meal spread e oil share desacelerando sua compressão/queda + margem de
biodiesel na maior compressão da janela, mas agora por um mecanismo
credível (custo do óleo, não liquidez de heating oil) + COT ainda parado,
aguardando a publicação de sexta — formam um quadro em que a tese estrutural
do complexo (esmagamento incentivado, óleo dominando o valor, farelo
abundante no médio prazo) segue de pé, mas a mecânica tática de curtíssimo
prazo está, pela primeira vez em semanas, alinhada e não mais em conflito
entre as três pernas: todas subiram hoje, com o farelo subindo relativamente
mais. A lição mais importante para quem opera o complexo esta semana: o
farelo está a uma sessão de confirmação de virar de "sinal tático
inconclusivo" para "sinal tático confirmado contra a tese estrutural" — o
COT de sexta e o fechamento de amanhã, juntos, devem resolver essa
ambiguidade.

---

## Lente fiscal e regulatória BR

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L) — a
vigência formal (`vigencia_ate` 11/07/2026) venceu há 11 dias, e o monitor
tributário segue sem qualquer atualização de status** (system/tributario_watch.toml,
evento MP-1358-2026, `atualizado_em` 2026-06-05, status ainda "tramitacao").
Enquanto o combustível fóssil segue subsidiado, a competitividade relativa do
biodiesel dentro do mix B15 mandatório fica pressionada — um vetor
regulatório independente da margem de biodiesel americana (que hoje
comprimiu -12,1% por conta própria, via custo do óleo), somando dois
headwinds distintos sobre a mesma economia de processamento.

**Isenção PIS/Cofins biodiesel — vencimento em 31/07/2026, agora a apenas 9
dias.** Sem sinalização pública de renovação até hoje (evento
PISCOFINS-BIODIESEL-ISENCAO, `atualizado_em` 2026-06-05, sem mudança). O
cenário de "duplo headwind" ganha urgência crescente com a margem de
biodiesel americana na maior compressão da janela (-12,1% hoje) — se o custo
do óleo continuar subindo junto com o rali do complexo, e a isenção
brasileira não for renovada, as duas pernas do biodiesel (margem americana e
carga tributária brasileira) pioram ao mesmo tempo, nos próximos 9 dias. É o
vetor tributário mais próximo de um desfecho concreto nesta leitura.

**B16 — sem data, travado em B15.** Sem mudança de status (evento
B16-CNPE-2026, `atualizado_em` 2026-06-05, status "adiado"). Testes técnicos
do FNDCT com resultado esperado ~nov/2026 — realista só fim de 2026/início
de 2027.

**MP 1.363/2026 (subsídio ao diesel fóssil, R$ 1,12/L) — em vigor até
31/12/2026.** Sem alteração. Bearish estrutural persistente para a demanda
incremental de óleo de soja no mercado doméstico brasileiro.

**STJ REsp 2.165.276/2026 — crédito PIS/Cofins para esmagadoras.** Sem
alteração. Bullish para soja/óleo (alívio de custo de entrada para
biodiesel) e, por extensão, incentivo a mais esmagamento — coerente com a
expansão da crush margin registrada hoje, que já sinaliza incentivo de
curto prazo crescente independentemente do alívio tributário estrutural.

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
soja). Todos esses vetores seguem, em conjunto, num sentido estruturalmente
bullish para o óleo de soja via substituição de palma — mas seguem
inverificáveis pelo lado dos dados de mercado (MPOB inacessível há 13 dias
consecutivos, ver Honestidade).

**O monitor tributário como um todo está há 47 dias sem qualquer
atualização** (`atualizado_em` 2026-06-05 em todos os dez eventos
rastreados) — o intervalo segue crescendo em um momento em que dois vetores
têm datas formais já vencidas ou criticamente próximas (MP 1.358, vencida há
11 dias; isenção PIS/Cofins, a 9 dias do vencimento). Vale sinalizar este
ponto, mais uma vez, como prioridade de manutenção do sistema,
independentemente da leitura de preço.

---

## Riscos e eventos próximos

**O COT (CFTC) — publicação normal esperada ~24/07/2026 (sexta-feira),
referente ao corte de 21/07.** É o evento mais importante dos próximos dias:
vai mostrar se os fundos compraram ou venderam soja, farelo e óleo durante a
semana inteira de rompimentos (soja em 20-22/07, farelo em 22/07) — o
primeiro dado de posicionamento capaz de arbitrar se o rali desta semana tem
correspondência em fluxo real de fundos ou é, em parte, um movimento de
cobertura de posição vendida.

**A isenção PIS/Cofins do biodiesel vence em 31/07/2026, agora a 9 dias**,
sem sinalização de renovação — coincidindo com a maior compressão da margem
de biodiesel americana da janela (-12,1% hoje). O vetor tributário mais
próximo de um desfecho concreto nesta leitura.

**O ratio Far/Soj precisa de mais uma sessão de confirmação** — se fechar
amanhã novamente acima de 80% e em alta, a revisão D+7 vencida (34 dias)
pode ser tratada como tacticamente invalidada de fato; se recuar, o whipsaw
se repete pela segunda vez nesta janela.

**A resistência de 325,00 no farelo, rompida hoje, precisa se sustentar
como suporte** — um fechamento de volta abaixo dela na próxima sessão
desfaria o sinal tático mais concreto desta leitura.

**NOPA — segue inacessível** (fila `release-nopa-2026-07-22` tratada aqui,
sem dado interpretável, apenas nova data de coleta), sem crush americano
confirmado por fonte primária.

**MPOB — sem números de palma extraídos há 13 dias consecutivos**, mantendo
cego o efeito do El Niño e dos vetores regulatórios indonésios sobre o
prêmio de substituição do óleo de soja.

**Checkpoints futuros da tese estrutural do farelo (ABIOVE)** — D+90 em
09/09/2026 e D+180 em 08/12/2026 (insight
[[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]) — a revisão D+7,
agora 34 dias vencida, acumula um segundo dia de reversão tática (ver seção
Farelo) e segue sem confirmação de fundamentos (WASDE, NOPA); os checkpoints
estruturais seguem o critério de mais alta confiança para julgar a tese ao
longo do tempo.

---

## Honestidade

O que não foi possível validar neste briefing de 22/07/2026, onde a
confiança é baixa ou há lacunas materiais:

**1. O fechamento de soja de 21/07/2026 usado como base de comparação para
os números de hoje é, mais uma vez, ligeiramente distinto do valor que a
própria leitura de ontem registrou.** A leitura de 21/07 registrou o
fechamento daquele dia em 1.210,25 cts/bu e o ratio Far/Soj em 80,31%; o
recálculo de hoje, para o mesmo dia, usa 1.210,50 (crush margin) e chega a
80,37% no ratio — uma diferença de 0,25 ponto na soja e 0,06 ponto
percentual no ratio. É uma divergência pequena, mas é a continuação do
mesmo padrão documentado nas últimas leituras (gerações sucessivas do
pipeline recalculando o passado com valores ligeiramente distintos). Todos
os cálculos de variação desta leitura usam consistentemente o valor
recalculado dentro do próprio dump de hoje (1.210,50 / 80,37%), por
consistência interna.

**2. A seção bruta `cme_cbot` do dump de hoje não traz os preços OHLC de
soja e óleo para a sessão de 21/07/2026** — apenas farelo e heating oil
aparecem com dado bruto completo daquele dia, a mesma lacuna documentada nas
duas leituras anteriores. A comparação de hoje contra ontem para soja e óleo
depende inteiramente do fechamento implícito na fórmula de crush margin dos
indicadores, não de uma confirmação direta da fonte primária CME para
aquele dia específico.

**3. O volume do heating oil normalizou para 451 contratos hoje**, ante 26
ontem e 109 anteontem — uma melhora relevante de confiabilidade que resolve,
ao menos parcialmente, a preocupação levantada nas duas leituras anteriores.
A queda de -1,11% no heating oil de hoje tem, por isso, mais credibilidade
do que os movimentos das duas sessões anteriores. Ainda assim, uma única
sessão de volume normal não estabelece uma nova baseline — vale continuar
observando o volume nas próximas sessões.

**4. O prêmio de exportação de farelo em Paranaguá (+0,05 USD/sht) e o de
óleo (+0,08 cts/lb) estão no mesmo valor exato desde pelo menos 03/07/2026**
(NAG, agora 19 dias corridos sem variação de nenhum centavo) — não é
possível distinguir se isso reflete um mercado de exportação genuinamente
parado ou um valor que não está sendo atualizado de fato na fonte.

**5. O nível de resistência de 325,00 no farelo (rompido hoje) é um alerta
gerado pelo sistema de calibração interna, cuja metodologia de definição de
nível não é visível a partir deste briefing** — da mesma forma que já se
aplica ao nível de 1.180,00 na soja, esta leitura trata o nível como dado
(o sistema já o fiscaliza automaticamente), sem poder validar de forma
independente os critérios técnicos usados para calibrá-lo.

**6. O COT (CFTC) segue com dado de referência 14/07/2026.** O corte
seguinte (21/07) já ocorreu, mas a publicação (~24/07) ainda não está
disponível — é o teste genuíno mais importante em aberto para resolver se o
rali desta semana (soja, farelo e óleo subindo juntos) tem correspondência
em posicionamento real de fundos.

**7. Percentis históricos de COT não calculados** — os números de
14/07/2026 são lidos apenas em nível absoluto e como fração do open interest
corrente (soja 7,48%, farelo 7,77%, óleo 16,92%), sem série histórica
completa para calibrar se algum desses níveis está objetivamente "esticado"
no sentido histórico.

**8. O WASDE segue cobrindo apenas farelo (Argentina, Brasil, China
parcial), sem nenhum dado de soja em grão ou óleo de soja, em qualquer
geografia, e sem nenhum dado dos Estados Unidos** — sem atualização desde
10/07/2026. A pergunta central da revisão D+7 vencida ("o WASDE mudou o
quadro?") segue sem canal de resposta interno.

**9. NOPA (fila `release-nopa-2026-07-22`) segue com `monthly_status` em 0,0
bool** — mesma barreira de assinatura paga documentada desde meados de
junho, agora com mais de um mês sem alternativa de dado primário sobre o
esmagamento americano. A "novidade" sinalizada pela fila é apenas a data de
coleta, não um dado genuinamente interpretável — o mesmo padrão das
leituras anteriores.

**10. Palma malaia (MPOB) segue sem números extraídos, agora por 13 dias
consecutivos com o mesmo conteúdo exato (3.439 caracteres, de 10/07 a
22/07/2026)** — a persistência do byte count idêntico sugere, possivelmente,
uma página que não está mais sendo servida com conteúdo atualizado. Continua
impossível avaliar o efeito do El Niño ou dos vetores regulatórios
indonésios sobre o prêmio de substituição do óleo de soja.

**11. Clima INMET (BR) não foi usado como driver de preço desta leitura.**
Julho é entressafra da soja brasileira (colheita concluída, plantio só em
outubro) — sem relevância direta para a tese de preço neste momento do
calendário agrícola. A manchete do dia sobre o início do vazio sanitário
(Canal Rural, 22/07/2026) foi citada na seção Soja apenas como contexto de
calendário para a safra 26/27, sem número associado — não foi tratada como
driver de preço, seguindo a regra de nunca inventar ou inferir magnitude
além do que consta no briefing. O El Niño Advisory (NOAA CPC, inalterado
desde pelo menos 03/07/2026) permanece relevante para a expectativa da
safra de plantio de outubro/26 e para o clima do Sudeste Asiático (palma).

**12. BCBA Argentina — sem relatórios de esmagamento/exportação acessíveis
via scraper** (page_fetched=1,0 mas sem links de relatório, 22/07/2026, sem
mudança).

**13. RIN D4 como parâmetro fixo (2,11 USD/RIN) segue sendo uma fonte
relevante de incerteza do modelo de biodiesel**, sem novo dado hoje — a
margem calculada em 0,8663 USD/gal usa esse valor fixo; se o RIN de mercado
estiver, na realidade, diferente de 2,11, tanto a margem quanto o ISO podem
estar mal calibrados, independentemente da compressão real documentada hoje
via custo do óleo.

**14. O ratio Far/Soj em dois pregões seguidos acima de 80% e em alta é o
dado mais importante desta leitura, mas ainda não é conclusivo por si só** —
esta leitura recomenda tratar a reversão como "em progresso, não confirmada"
até uma terceira sessão na mesma direção, a mesma disciplina que a leitura
de ontem definiu diante do whipsaw anterior. Aplicar esse padrão de forma
consistente, mesmo quando os dois últimos dias favorecem uma conclusão mais
rápida, é o que preserva a credibilidade metodológica desta série de
leituras.

*Nenhum número foi inventado ou estimado além do que consta no briefing de
22/07/2026 e nos insights anteriores referenciados. A contribuição central
desta leitura foi identificar que o farelo rompeu uma resistência técnica
(325,00) e acumulou dois pregões seguidos de ratio Far/Soj em alta acima de
80% — o primeiro par de sessões consecutivas na mesma direção nesta janela
de observação, e portanto o dado mais próximo, até agora, de efetivamente
invalidar o critério tático da revisão D+7 vencida (34 dias) da tese bear do
farelo — ao mesmo tempo em que a soja estendeu o rompimento com o fechamento
mais forte da semana e o óleo encerrou dois dias de fricção tática com o
fechamento mais forte da semana, ainda que a margem de biodiesel americana
tenha comprimido -12,1% por um mecanismo distinto (custo do óleo, não
liquidez do heating oil) dos dois dias anteriores.*
