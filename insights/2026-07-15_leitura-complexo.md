---
data: 2026-07-15
titulo: "Revisão de dado muda o sinal do farelo: com o preço recalculado no dump de hoje, o ratio Far/Soj já está abaixo de 80% há três sessões (79,52% em 13/07, 79,83% em 14/07, 79,88% em 15/07) — o oposto do que a leitura de 13/07 havia lido (>80%) com o dado então disponível —, confirmando (com atraso e via revisão, não via evento novo) o gatilho tático bear da tese de 11/06; a soja consolida em range apertado acima da resistência de 1.180 com uma vela de recuperação hoje (fechou em 1.195,00, perto da máxima de 1.198,25, depois de abrir na mínima de 1.191,00); e o óleo, também com preço recalculado, aparece negociando OTIMISTAMENTE acima (não abaixo) de 72,00 nas últimas três sessões, invertendo a moldura bear tático das leituras recentes"
tags: [complexo, auto-claude]
fontes:
  - CBOT CME (ZSQ26/ZMQ26/ZLQ26 + curva forward completa + HO=F) — sessão de 2026-07-15
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, ISF/ISO, paridade BR) — recalculados com preço de 2026-07-15 e, para as séries históricas de 13-14/07, com valores DIFERENTES dos citados nas leituras publicadas nesses dias (ver Honestidade)
  - BCB PTAX — último dado 2026-07-14 (USD/BRL 5,0742), defasagem de apenas 1 dia (melhor que os 3 dias da leitura de 13/07)
  - CEPEA/ESALQ Paranaguá e Paraná interior via NAG — último dado 2026-07-14 (suporte Paranaguá R$ 140,63/saca, Paraná interior R$ 132,94/saca)
  - NAG Físico BR (farelo MT/IMEA, RS, Rondonópolis; prêmios export PGUA farelo/óleo) — último dado 2026-07-14
  - CFTC COT Managed Money — dado de referência 2026-07-07, sem atualização (próxima publicação normal ~2026-07-17, sexta-feira, em 2 dias)
  - USDA Crop Progress — ATUALIZOU: 2026-07-12 (65% bom-ou-melhor, +1pp sobre 05/07), preenchendo a lacuna que a leitura de 13/07 apontava como pendente
  - USDA WASDE — ainda 2026-07-10 (só farelo Argentina/Brasil/China parcial), sem publicação nova
  - NOPA — 2026-07-15, `monthly_status` continua inacessível (paywall), fila `release-nopa-2026-07-15`
  - ABIOVE projeções mensais — balanços ago-dez/2026 (farelo/óleo/soja), sem alteração
  - NOAA CPC ENSO — 2026-07-15 (El Niño Advisory, sem mudança)
  - MPOB — 2026-07-15 (parser sem números extraídos, streak de ~31 dias)
  - BCBA — 2026-07-15 (acessível, sem links de relatório detectados)
  - Notícias Agrícolas / Farm Progress RSS — 2026-07-15 (160 itens lidos, 5 mantidos, mas sem manchete específica listada no dump de hoje — ver Honestidade)
  - Forecasts estatísticos internos — 2026-07-15 (recalibrados com o novo spot)
  - system/tributario_watch.toml — MP-1358-2026 (vigência formal encerrada há 4 dias, status ainda "tramitação"), PISCOFINS-BIODIESEL-ISENCAO (vence em 16 dias), MP-1363-2026, STJ-RESP-2165276, B16-CNPE-2026 — todos `atualizado_em` 2026-06-05 (40 dias sem atualização do monitor)
  - Cruza com [[2026-07-13_leitura-complexo]], [[2026-07-12_leitura-complexo]], [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (checkpoint D+7, revisitado hoje com dado revisado), [[2026-05-26_subvencao-fossil-aperta-biodiesel]], [[2026-05-26_pis-cofins-biodiesel-explica-mercado-fisico-fraco]]
status: ativa
vies: [bull-soja, bear-farelo, neutral-oleo_soja]
---

## Visão geral

O complexo soja é uma fábrica com uma única matéria-prima (a soja em grão) e dois
produtos de saída em proporção fixa por bushel esmagado: o **farelo** (fração
proteica, ~78% da massa, vira ração animal) e o **óleo degomado** (fração de gordura,
~18-20% da massa, vira óleo de cozinha e biodiesel). Quem decide o ritmo de
esmagamento é a esmagadora, olhando a **crush margin** (valor de farelo + óleo por
bushel, menos o custo daquele bushel de soja, na CBOT — Chicago Board of Trade, a
bolsa onde soja/farelo/óleo são negociados como futuros) e o **oil share** (fração
desse valor capturada pelo óleo). Hoje, quarta-feira 15/07/2026, a crush margin fechou
em 3,0342 USD/bushel (indicadores, farelo 318,20 + óleo 72,58 − soja 1.195,00),
essencialmente estável frente aos últimos dois pregões (3,0211 em 13/07, 3,0193 em
14/07) — a esmagadora segue com forte incentivo econômico a rodar a pleno vapor, sem
sinal de arrefecimento nem de novo salto.

**O que realmente mudou hoje não foi um evento de mercado, foi a base de dados.** O
dump de hoje recalculou os indicadores das últimas sessões com preços de farelo e
óleo diferentes dos que as leituras publicadas em 13/07 e 14/07 usaram — e essa
revisão inverte a leitura tática de duas das três pernas do complexo. No **farelo**, o
ratio Far/Soj (preço do farelo dividido pelo da soja, na mesma base — abaixo de 80%
indica farelo "abundante" frente à soja) aparece agora em 79,52% (13/07), 79,83%
(14/07) e 79,88% (15/07) — três sessões consecutivas **abaixo** de 80%, o oposto do
que a leitura de 13/07 registrou em tempo real (80,46%, acima de 80%, "checkpoint D+7
não confirmado"). Com o dado de hoje como fonte da verdade, o gatilho tático da tese
de 11/06/2026 (`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`)
está, sim, confirmado — mas de forma que nenhum trader poderia ter agido em tempo
real, porque a confirmação só aparece agora, retroativamente, via correção de série.
No **óleo**, o mesmo fenômeno: o preço de 13/07 aparece hoje em 72,82 cts/lb e o de
14/07 em 72,40, ambos **acima** do nível de 72,00 que as leituras dos últimos dias
vinham descrevendo como resistência/suporte técnico rompido para baixo (a leitura de
13/07 citava 71,02). Juntando os três pregões mais recentes com o dado de hoje
(72,82 → 72,40 → 72,58), o óleo está de fato oscilando **em cima**, não abaixo, do
nível de 72,00 — o que muda o viés tático de bear para neutro. Na **soja**, não há
discrepância de série: o fechamento de hoje (1.195,00 cts/bu) segue 1,27% acima da
resistência de 1.180,00, mas é o terceiro pregão seguido de consolidação apertada
(1.197,25 em 13/07 → 1.192,75 em 14/07 → 1.195,00 hoje, um range de apenas 4,50 pontos
entre o mais alto e o mais baixo fechamento dos três dias) — a vela de hoje (abriu na
mínima de 1.191,00, subiu até 1.198,25 e fechou perto do topo, em 1.195,00) é uma
recuperação técnica depois do pregão de baixa de ontem, mas ainda dentro do mesmo
range lateral, não uma extensão nova do rompimento. **Leitura de uma linha:** o pivô
do complexo continua sendo a soja (consolidando, não revertendo, acima de 1.180), mas
a peça nova do dia é editorial, não de mercado — a revisão de série muda o farelo de
"neutro" para "bear" (tático + estrutural reforçando-se) e o óleo de "bear" para
"neutro", com convicção baixa em ambos até a próxima atualização confirmar se a
correção se sustenta.

---

## Soja

**Viés: bull tático mantido, convicção moderada — fechou em 1.195,00 cts/bu
(15/07/2026), 1,27% acima da resistência de 1.180,00, terceiro pregão seguido dentro
de um range de consolidação de apenas 4,50 pontos (1.192,75-1.197,25); a vela de hoje
é de recuperação (abriu na mínima do dia, fechou perto da máxima), não de extensão do
rompimento. Trata `alerta-quebra_resistencia-soja_cbot-2026-07-15`.**

### O que sustenta a tese

**O nível técnico permanece confirmado, e a vela de hoje é mais construtiva do que a
de ontem.** Fechamento de 1.195,00 cts/bu (CBOT, 15/07/2026), com abertura em
1.191,00 (que também foi a mínima da sessão), máxima de 1.198,25 e fechamento
1.195,00 — ou seja, o preço abriu no piso do dia e fechou a 57% do range total acima
da mínima, um padrão de recuperação intradiária, não de rejeição. Isso contrasta com
a sessão de 14/07 (fechamento em 1.192,75, abaixo do fechamento anterior de 1.197,25,
uma queda de -0,38% que parcialmente confirmava a exaustão técnica identificada na
vela de rejeição de 13/07) e sugere que o pregão de baixa de ontem não teve
continuidade — o mercado testou o piso do range (perto de 1.191) e foi comprado de
volta, não vendido mais.

**Olhando os três últimos fechamentos em conjunto — 1.197,25 (13/07) → 1.192,75
(14/07) → 1.195,00 (15/07) — o quadro é de consolidação lateral apertada acima de
1.180,00, não de tendência definida em nenhuma direção.** O rompimento de 06-07/07
segue tecnicamente de pé (nenhum fechamento voltou a testar 1.180), mas o mercado não
está fazendo novas máximas desde os 1.208,75 intradiários de 13/07 — três sessões
seguidas de range estreito depois de um movimento de alta forte costumam preceder ou
uma continuação (se o range resolver para cima) ou uma correção mais profunda (se
resolver para baixo); hoje, isoladamente, resolveu ligeiramente para cima dentro do
range, sem definir qual dos dois cenários prevalece.

**O USDA Crop Progress finalmente atualizou, preenchendo a lacuna que a leitura de
13/07 apontava como pendente.** O relatório de 12/07/2026 mostra 65% da lavoura
americana em condição boa-ou-excelente (12% excelente + 53% boa), ante 64% em
05/07/2026 (11% + 53%) — uma melhora marginal de +1 ponto percentual, com o
percentual em condição ruim (poor) estável em 6% nas duas semanas. O mecanismo é
direto: quanto melhor a condição da lavoura, maior a expectativa de produtividade e,
portanto, de oferta — um dado de melhora, mesmo que pequeno, é estruturalmente
bearish para o preço, na contramão da manchete "Soybean prices need poor weather,
exports to China" (Farm Progress, citada na leitura de 13/07) que fundamentava parte
do rali. Mas a magnitude é pequena (+1pp, poor estável) — não é evidência de uma
safra excelente se formando, apenas de estabilidade/leve melhora, insuficiente para
mudar o viés por si só.

**A curva forward mantém o formato de "sorriso" já documentado**: Agosto/26 (Q26,
spot) 1.195,00 → Setembro/26 (U26) 1.184,50 (desconto de -10,50, o padrão sazonal de
pressão pré-colheita americana) → Novembro/26 (X26) 1.194,25 (recupera +9,75 sobre
setembro) → Janeiro/27 (F27) 1.208,00 (+13,75) → Março/27 (H27) 1.211,50 (+3,50) —
desconto no meio da curva (safra nova entrando) e prêmio na ponta longa (expectativa
de aperto pós-colheita ou custo de carregamento), sem sinal de estresse de estoque
imediato.

**O câmbio (PTAX) melhorou de defasagem** — o BCB publicou PTAX para 14/07/2026
(5,0742 BRL/USD), então a paridade calculada hoje (R$ 133,68/saca 60kg, indicadores,
15/07/2026, usando CBOT de hoje × câmbio de ontem) tem apenas 1 dia de defasagem
cambial, ante 3 dias na leitura de 13/07. Comparando a paridade teórica de 14/07 (R$
133,43/saca, CBOT 1.192,75 × PTAX 5,0742, mesmo câmbio) com o preço físico de
Paranaguá do mesmo dia (R$ 140,63/saca, CEPEA/ESALQ via NAG, 14/07/2026), o porto
negocia com um prêmio de R$ 7,20/saca (+5,4%) sobre a paridade teórica — uma
comparação de data casada (ambos 14/07), mais limpa do que misturar spot de hoje com
câmbio de ontem. Esse prêmio físico consistente é um sinal de demanda de exportação
firme no porto, coerente com o viés de alta.

**O posicionamento dos fundos (COT, CFTC) permanece no dado de referência de
07/07/2026** — managed money net long em +69.579 contratos (7,13% do open interest de
975.954), sem atualização nova. A próxima publicação normal sai sexta-feira,
~17/07/2026, em apenas 2 dias — será o primeiro teste real de se a compra dos fundos
sobreviveu à semana de consolidação de 13-15/07.

**Os forecasts estatísticos internos (15/07/2026)** seguem com viés altista: central
7d = 1.219,37 cts/bu (bandas 1.168,70-1.270,05); central 30d = 1.309,78 cts/bu
(bandas 1.204,87-1.414,69) — ambos ligeiramente acima dos centrais de ontem
(1.216,05 e 1.300,97). Mesmo com viés de alta, a banda baixa de 7 dias (1.168,70)
segue abaixo da resistência de 1.180,00, reconhecendo um cenário de reversão dentro
do horizonte de uma semana como plausível, ainda que não central.

### O que invalida / risco para a soja

- **Um fechamento abaixo de 1.191,00 (mínima de hoje) ou de 1.180,00** reabriria o
  teste do nível-chave e daria força ao cenário de reversão do rompimento.
- **O COT de sexta (~17/07) mostrar que o managed money vendeu durante a
  consolidação** — o range apertado dos últimos 3 dias é o tipo de padrão que precede
  realização de lucro de fundos táticos.
- **Novas leituras de Crop Progress mostrarem melhora continuada** — hoje foi apenas
  +1pp; uma sequência de melhoras reduziria progressivamente o argumento de "oferta
  apertada" nas manchetes recentes.
- **A revisão de dado documentada nesta leitura (ver Honestidade) se repetir para a
  soja** — hoje não houve discrepância na série de soja, mas farelo e óleo tiveram, o
  que exige checar se o preço de soja de hoje também será revisado amanhã.

### Leitura operacional — soja

Viés tático de alta mantido, mas a convicção segue moderada (não moderada-alta): o
range apertado de 3 sessões não resolveu na direção de uma nova máxima, e a vela de
hoje, apesar de construtiva, ainda está contida dentro desse range. Para quem está
comprado taticamente, a referência de stop desce ligeiramente para perto de 1.191,00
(mínima de hoje, que também foi o piso das últimas duas sessões) — um fechamento
abaixo desse nível seria o primeiro sinal de ruptura do range lateral para baixo. Para
quem está vendido contra o rompimento, a consolidação atual é o ambiente onde essa
aposta tem menos custo de carrego contra si, mas o COT de sexta-feira é o próximo
evento que pode validar ou invalidar a tese de qualquer um dos dois lados.

---

## Farelo

**Viés: bear (tático + estrutural) — o ratio Far/Soj recalculado hoje mostra três
sessões consecutivas abaixo de 80% (79,52% em 13/07, 79,83% em 14/07, 79,88% em
15/07), invertendo a leitura em tempo real de 13/07 (que registrava >80%) e
confirmando, via revisão de dado, o gatilho tático da tese de 11/06/2026. Trata
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`.**

### O que sustenta a tese

**O ratio Far/Soj de hoje fechou em 79,88%** (indicadores, 15/07/2026: farelo 318,20
USD/short_ton ÷ soja 1.195,00 cts/bu, na mesma base), a terceira sessão consecutiva
abaixo do limiar de 80% que a tese original de 11/06/2026 usava como gatilho tático
para "farelo abundante frente à soja". O detalhe crítico é que essa mesma métrica,
recalculada hoje para as datas de 13/07 e 14/07, mostra 79,52% e 79,83% — valores que
a leitura publicada em 13/07/2026 registrou de forma diferente (80,46%, acima de 80%,
usando um preço de farelo de 321,10 USD/sht contra o farelo de 317,20 que o dump de
hoje atribui à mesma data). Não há como saber, só com os dados públicos deste
sistema, se a correção veio de um ajuste de fechamento (settlement final vs.
intradiário), uma correção de fonte upstream, ou outro motivo — mas o efeito prático é
que o gatilho tático da tese de 11/06 (ratio sustentado <80%) está, sim, confirmado
com os números de hoje, ainda que de forma que não podia ter sido operada em tempo
real durante as sessões em que efetivamente ocorreu.

**A crush margin (valor de farelo + óleo por bushel, menos o custo da soja, medido
pela CBOT) fechou em 3,0342 USD/bushel** (indicadores, 15/07/2026: farelo 318,20 +
óleo 72,58 − soja 1.195,00), estável frente a 13/07 (3,0211) e 14/07 (3,0193) — sem
o salto de "novo máximo da série" que caracterizou o pregão de 13/07, mas ainda em
patamar historicamente elevado. O mecanismo continua o mesmo: quanto maior a crush
margin, maior o incentivo da esmagadora a processar soja a pleno vapor, e mais farelo
(subproduto obrigatório do esmagamento) entra no mercado — a base estrutural da tese
ABIOVE de excesso doméstico de farelo no 2º semestre.

**A trajetória projetada da ABIOVE (Associação Brasileira das Indústrias de Óleos
Vegetais, projeções mensais, sem alteração) segue sendo o pilar mais sólido do
argumento estrutural, porque não depende do preço do dia.** A exportação de farelo
brasileiro projetada cai de 1.400 mil toneladas em agosto/2026 para 700 mil toneladas
em dezembro/2026 (queda de 50% em 4 meses), enquanto a produção cai de forma bem mais
suave (2.285,06 → 1.659,04 mil toneladas no mesmo período, -27%) e o estoque final
oscila sem tendência clara entre 1.000 e 1.224 mil toneladas ao longo de todo o
semestre. O mecanismo de transmissão é direto: menos farelo saindo pelo porto, com
produção caindo bem menos que a exportação, empurra o volume excedente para o mercado
interno de ração, pressionando o preço doméstico — esse mecanismo estrutural agora
está alinhado com o sinal tático do ratio, em vez de contradizê-lo como na leitura de
13/07.

**As praças físicas de farelo no Brasil (NAG) permanecem no último dado de 14/07/2026**
— Mato Grosso/IMEA R$ 1.577,34/ton, Rondonópolis R$ 1.670,00/ton, RS R$ 1.640,00/ton
— sem variação frente a 13/07 (mesmos valores). O prêmio de exportação em Paranaguá
segue em +0,05 USD/short_ton (julho/26, NAG, inalterado desde pelo menos 03/07/2026,
agora quase duas semanas no mesmo valor exato) — essa constância exata por tantos
dias seguidos é, em si, um ponto de atenção: pode refletir um mercado de exportação
genuinamente parado (Brasil sem vantagem de preço para exportar, reforçando a
absorção doméstica) ou um valor que não está sendo atualizado de fato na fonte (ver
Honestidade). De qualquer forma, um prêmio de exportação perto de zero sustenta o
mecanismo de que o farelo brasileiro não tem para onde escoar externamente, reforçando
a pressão doméstica.

**O Índice de Sobra de Farelo (ISF) permanece em 80/100 (4 de 5 condições
estruturais)** (indicadores, 15/07/2026), o mesmo nível desde pelo menos 01/07/2026 —
agora ao menos 15 dias consecutivos sem mudança, o índice estrutural mais estável e
persistente de toda a leitura, e que hoje finalmente converge com o sinal tático do
ratio, em vez de divergir dele.

**Tratando `release-nopa-2026-07-15`:** o NOPA (National Oilseed Processors
Association, dado mensal de esmagamento americano) segue com `monthly_status` em 0,0
bool — a mesma barreira de assinatura paga documentada desde meados de junho, sem
nenhuma informação nova para interpretar apesar do item aparecer na fila como
"release" do dia. Não há confirmação direta do ritmo de esmagamento americano por
fonte primária.

**O forecast estatístico do farelo (15/07/2026)** segue com viés altista: central 7d =
323,64 USD/sht (bandas 311,10-336,18); central 30d = 343,87 USD/sht (bandas
317,91-369,83) — o modelo estatístico (que reage a momentum de preço recente, não a
fundamentos) segue na direção oposta à tese fundamentalista ABIOVE + ratio, a mesma
contradição entre curto prazo (modelo) e médio prazo (estrutura) já documentada nas
leituras anteriores.

### O que invalida / risco para o farelo

- **A revisão de dado documentada hoje não se sustentar** — se uma futura geração do
  dump voltar a mostrar o ratio de 13-15/07 acima de 80%, a confirmação do gatilho
  tático seria desfeita tão silenciosamente quanto apareceu; vale conferir a
  consistência da série nas próximas leituras antes de tratar isso como definitivo.
- **A tese estrutural ABIOVE não se confirmar no físico ao longo do 2S/26.**
- **O ratio reverter para cima de 80% nos próximos pregões** — com o ratio agora perto
  da fronteira (79,88%), uma alta modesta do farelo ou queda da soja já reverteria o
  sinal.
- **NOPA seguir inacessível indefinidamente**, sem confirmação do esmagamento
  americano para os checkpoints D+90 (09/09/2026) e D+180 (08/12/2026).
- **O prêmio de exportação Paranaguá "congelado" em 0,05 USD/sht ser, na verdade, um
  dado sem atualização de fonte, não um preço de mercado real** — reduziria a
  confiança no argumento de ausência de competitividade exportadora.

### Leitura operacional — farelo

Com o gatilho tático agora tecnicamente confirmado pelos dados de hoje (ainda que via
revisão, não via evento novo), a leitura muda de "reduzir a posição vendida" (13/07)
para "o cenário original da tese de 11/06 (spread de convergência farelo/soja, ou
posição vendida tática em farelo isolado) volta a ter suporte de dado, partindo de um
ratio (79,88%) já mais próximo da fronteira de 80% do que do nível de origem da tese
(81,4% em 11/06)." Dado que a confirmação vem de uma correção de série, a recomendação
é tratar isso como reforço de convicção moderado, não alto, até uma nova geração do
dump confirmar a estabilidade dos números — e monitorar de perto se o ratio segue
descendo ou estabiliza perto de 80%. Para quem prefere a tese estrutural pura (ABIOVE),
o veículo mais robusto continua sendo o spread farelo/soja ou o crush completo, em vez
de direcional puro.

---

## Óleo

**Viés: neutro — com o preço recalculado hoje, o óleo aparece negociando ACIMA (não
abaixo) de 72,00 nas últimas três sessões (72,82 em 13/07, 72,40 em 14/07, 72,58 em
15/07), invertendo a moldura de bear tático das leituras recentes; ISO em 100/100 e
curva em backwardation seguem dando suporte técnico, mas a margem de biodiesel
comprimiu -14,4% no dia por causa do heating oil.**

### O que sustenta a tese

**O óleo fechou hoje em 72,58 cts/lb** (CBOT, 15/07/2026), com abertura em 72,53,
máxima de 72,97 e mínima de 72,43 — um range estreito (0,54 cts) e uma sessão sem
grande direção definida. O ponto que muda a leitura é olhar os últimos três
fechamentos em conjunto, com os valores que o dump de hoje atribui a cada data:
72,82 (13/07) → 72,40 (14/07) → 72,58 (15/07) — todos acima do nível de 72,00 que as
leituras recentes vinham tratando como resistência rompida para baixo. Isso é uma
mudança de leitura relevante: com a série de hoje como fonte da verdade, não há
evidência de que o óleo esteja abaixo de um suporte técnico relevante; ele está, na
verdade, oscilando logo acima de um número redondo, sem tendência direcional clara
nos últimos 3 pregões.

**A curva forward mantém backwardation limpa e consistente**: Agosto/26 (Q26, spot)
72,58 → Setembro/26 (U26) 71,84 (-0,74) → Outubro/26 (V26) 71,19 (-0,65) → Dezembro/26
(Z26) 70,81 (-0,38) → Janeiro/27 (F27) 70,63 (-0,18) — uma queda de -1,95 cts/lb
(-2,7%) de agosto a janeiro/27. Esse formato (prêmio no vencimento mais próximo,
desconto nos mais distantes) reflete demanda física presente forte (biodiesel
americano + exportação brasileira) frente a uma expectativa de oferta mais confortável
adiante, e é o argumento técnico mais estável de toda a leitura — não muda com a
revisão de série discutida acima, porque a curva de hoje é medida inteiramente com
dados de hoje.

**A margem de biodiesel americano caiu para 0,8127 USD/galão** (indicadores,
15/07/2026: receita 7,0562 = HO/heating oil 3,8912 + 1,5×RIN 2,11; custo 6,2435 = óleo
5,4435 + industrial 0,80), uma queda de -14,4% frente a 14/07 (0,9493). O mecanismo:
o heating oil (proxy de receita do biodiesel) recuou de 4,0143 (14/07) para 3,8912
(15/07, -3,1%) depois de ter saltado de 3,82 (13/07) para 4,01 (14/07, +5,0%) — uma
reversão quase total do salto de ontem —, enquanto o custo do óleo (insumo) subiu
ligeiramente (5,43 → 5,44). A compressão de hoje veio inteiramente do lado da receita
(heating oil recuando), não do custo — o oposto do padrão descrito na leitura de
13/07. Isso evidencia que a margem de biodiesel está sendo movida principalmente pela
volatilidade do complexo de energia (heating oil oscilou 3,82 → 4,01 → 3,89 em três
dias), um fator externo ao complexo soja em si.

**O Índice de Suporte do Óleo (ISO) permanece em 100/100 (5 de 5 condições)**
(indicadores, 15/07/2026) — o mesmo patamar máximo desde 01/07/2026, agora superando
duas semanas consecutivas sem qualquer sinal de enfraquecimento, mesmo com a
compressão pontual da margem de biodiesel hoje.

**O oil share (fração do valor do crush capturada pelo óleo) está em 53,28%**
(indicadores, 15/07/2026), estável frente aos 53,28% de 14/07 e levemente abaixo dos
53,44% de 13/07 — seguindo folgadamente acima de 50%, confirmando que o óleo continua
sendo o motor de valor do crush, não o farelo.

**O forecast estatístico do óleo (15/07/2026) mudou de viés**: central 7d = 72,83
cts/lb (bandas 68,39-77,28), viés "lateral" (não mais baixista como em leituras
anteriores); central 30d = 74,43 cts/lb (bandas 65,23-83,63), viés **altista** — a
primeira vez em várias leituras que o modelo estatístico de 30 dias assume viés de
alta para o óleo, corroborando (a partir de um modelo puramente técnico, sem
fundamento embutido) a leitura de que o preço genuinamente recuperou terreno frente
ao nível de 72,00.

### O que invalida / risco para o óleo

- **Um fechamento abaixo de 71,19 (mínima da curva forward de setembro) ou repetição
  de um fechamento como o antigo 71,02 citado em leituras anteriores** reabriria o
  cenário bear tático — mas com os dados de hoje isso ainda não aconteceu nas últimas
  3 sessões.
- **A margem de biodiesel (0,8127 USD/gal) continuar caindo** — ainda dentro da faixa
  de conforto de 0,50-0,80, mas a queda de -14,4% em um dia é o maior movimento diário
  documentado recentemente; se persistir, reduz o incentivo doméstico americano ao
  óleo.
- **O heating oil (proxy de receita do biodiesel) seguir volátil** — osciloue 3,82 →
  4,01 → 3,89 USD/galão em 3 dias; essa instabilidade externa (complexo de energia)
  pode continuar ditando o ritmo da margem de biodiesel independentemente do que
  acontece no óleo de soja.
- **A revisão de série documentada hoje não se sustentar** — mesma ressalva do
  farelo: se uma futura geração do dump reverter os valores de 13-14/07 para os
  patamares antigos (abaixo de 72,00), a leitura de "óleo acima de 72" cairia junto.
- **MPOB seguir inacessível** — impossível avaliar o efeito do El Niño ou das
  restrições indonésias sobre o prêmio de substituição via palma.

### Leitura operacional — óleo

O viés muda de bear tático para neutro: a curva em backwardation e o ISO em 100/100
seguem dando suporte estrutural para quem quer manter exposição relativa ao óleo
dentro do crush, mas a ausência de uma direção clara nos últimos 3 fechamentos (72,82
→ 72,40 → 72,58) não justifica nem uma posição direcional vendida nem comprada com
convicção alta neste momento — a referência de range para operar (72,40-72,97,
aproximadamente a extensão dos últimos 3 pregões) é mais útil agora do que um nível
de rompimento. Para quem opera o oil share dentro do crush, o viés estrutural segue
levemente favorável ao óleo frente ao farelo, reforçado pelo próprio sinal bear que
emergiu hoje no farelo — o spread oil-meal (óleo menos farelo, ver seção seguinte)
é o veículo mais direto para capturar essa divergência sem depender da direção
absoluta do óleo.

---

## Spreads e crush — leitura de complexo

### Crush margin: 3,0342 USD/bu — estável em patamar elevado

A crush ficou praticamente estável nos últimos 3 pregões (3,0211 → 3,0193 → 3,0342,
15/07/2026), sem o salto de "novo máximo" de 13/07, mas seguindo em nível
historicamente alto. O incentivo de esmagamento a pleno vapor permanece intacto,
alimentando o mecanismo estrutural ABIOVE (mais farelo entra no mercado como
subproduto) mesmo com o preço relativo de cada perna se movendo em direções distintas.

### Ratio Far/Soj: 79,88% — terceira sessão abaixo de 80%, gatilho tático confirmado (com ressalva de revisão)

O achado central desta leitura: com os números de hoje, o ratio está abaixo de 80%
há três sessões (79,52 → 79,83 → 79,88), o oposto do que a leitura de 13/07 registrou
em tempo real. Trata `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
— o gatilho tático está tecnicamente confirmado pelos dados atuais, mas a confirmação
veio de uma correção de série, não de um movimento de mercado novo (ver Honestidade).

### Oil share: 53,28% — estável, óleo segue dominando o crush

Sem variação relevante frente aos últimos dias (53,44% em 13/07, 53,28% em 14/07 e
hoje) — folgadamente acima de 50%, o óleo capturando a maior fatia do valor do crush.

### Oil-meal spread: 0,9834 USD/bu — leve alta no dia

Subiu de 0,9812 (14/07) para 0,9834 USD/bu (15/07,2026) — mede o valor do óleo menos
o valor do farelo por bushel; a leve alta de hoje, combinada com o farelo agora em
viés bear e o óleo em viés neutro-a-levemente-firme, é coerente com a divergência das
duas pernas identificada nesta leitura.

### ISF em 80/100, ISO em 100/100 — patamar sustentado, agora ao menos 15 dias

O Índice de Sobra de Farelo (ISF, 4/5 condições) e o Índice de Suporte do Óleo (ISO,
5/5 condições) permanecem nos mesmos níveis desde pelo menos 01/07/2026 (indicadores,
15/07/2026) — o ISF hoje finalmente converge com o sinal tático do ratio (ambos
apontando pressão baixista no farelo), depois de dias em que divergiam.

### O que os índices dizem juntos em 15/07/2026

ISF 80/100 + ISO 100/100 (ambos estáveis há ~15 dias) + ratio Far/Soj em 79,88% (3ª
sessão abaixo de 80%, gatilho tático confirmado) + oil share estável em 53,28% + crush
margin estável em patamar elevado (3,0342) + oil-meal spread em leve alta (0,9834)
formam, pela primeira vez em várias leituras, um quadro **coeso**: o complexo segue
esmagando a pleno vapor, e agora tanto o índice estrutural (ISF) quanto o sinal
tático (ratio) apontam na mesma direção para o farelo — pressão baixista —, enquanto
o óleo mantém sustentação técnica (ISO, backwardation) sem, no entanto, mostrar
tendência de alta forte no preço absoluto. A ressalva necessária é que essa
convergência farelo se apoia em uma revisão de dado, não em um evento de mercado novo
— vale confirmar sua persistência na próxima geração do dump antes de tratá-la como
definitiva.

---

## Lente fiscal e regulatória BR

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L) — a vigência
formal (`vigencia_ate` 11/07/2026) já venceu há 4 dias, e o monitor tributário segue
sem qualquer atualização de status** (`system/tributario_watch.toml`, evento
MP-1358-2026, `atualizado_em` 2026-06-05, status ainda "tramitacao", `proximo_marco` =
"Deliberação comissão mista", `proximo_data` = 2026-07-11, já vencida). Já são quatro
dias úteis (13, 14 e 15/07, mais o fim de semana) desde o vencimento formal sem
nenhuma fonte pública rastreada pelo sistema (ABIOVE, NAG, notícias) confirmar se a MP
caducou, foi prorrogada por novo decreto, ou foi convertida em lei. O mecanismo de
transmissão para o complexo permanece o mesmo já documentado: enquanto o combustível
fóssil segue subsidiado, a competitividade relativa do biodiesel dentro do mix B15
mandatório fica pressionada, mantendo a margem da indústria de biodiesel mais
apertada do que sem a subvenção ao concorrente fóssil — um pano de fundo que ecoa a
compressão pontual de margem documentada hoje na seção Óleo, ainda que por um canal
distinto (hoje foi o heating oil externo, não a MP, que comprimiu a margem).

**Isenção PIS/Cofins biodiesel — vencimento em 31/07/2026, agora a 16 dias.** Sem
sinalização pública de renovação até hoje (evento PISCOFINS-BIODIESEL-ISENCAO,
`atualizado_em` 2026-06-05, sem mudança). Continua sendo o próximo relógio fiscal mais
próximo a vigiar, à frente da própria definição da MP 1.358.

**B16 — sem data, travado em B15.** Sem mudança de status (evento B16-CNPE-2026,
`atualizado_em` 2026-06-05, status "adiado", sem `proximo_data`).

**MP 1.363/2026 (subsídio ao diesel fóssil) — em vigor até 31/12/2026.** Sem
alteração. Bearish estrutural persistente para a demanda incremental de óleo de soja
no mercado doméstico brasileiro.

**STJ REsp 2.165.276/2026 — crédito PIS/Cofins para esmagadoras.** Sem alteração.
Bullish para soja/óleo (alívio de custo de entrada para biodiesel) e, por extensão,
incentivo a mais esmagamento — coerente com a crush margin em patamar elevado
documentada hoje.

**O monitor tributário como um todo está há 40 dias sem qualquer atualização**
(`atualizado_em` 2026-06-05 em todos os eventos rastreados) — um intervalo cada vez
mais longo considerando que dois vetores (MP 1.358 e a isenção PIS/Cofins) têm datas
de vencimento formal já vencida ou muito próxima (31/07). Vale sinalizar este ponto
como prioridade de manutenção do sistema, independentemente da leitura de preço.

---

## Riscos e eventos próximos

**Confirmar se a revisão de série de farelo e óleo documentada hoje se sustenta na
próxima geração do dump.** É o item mais urgente desta leitura: se os valores de
13-15/07 voltarem a mudar, tanto o gatilho tático do farelo quanto a leitura de "óleo
acima de 72" precisam ser reavaliados.

**Próxima atualização do COT (~17/07/2026, sexta-feira, em 2 dias)** — teste de se o
managed money manteve a compra em soja/farelo e a redução em óleo durante a semana de
consolidação de 13-15/07.

**Desfecho da MP 1.358/2026 — vigência formal encerrada há 4 dias, sem confirmação.**
Monitorar deliberação da comissão mista e qualquer decreto de prorrogação.

**Isenção PIS/Cofins biodiesel — vencimento 31/07/2026 (16 dias).** Sem sinalização de
renovação até agora.

**NOPA — segue inacessível** (fila `release-nopa-2026-07-15` tratada aqui, sem dado
interpretável), sem crush americano confirmado por fonte primária.

**MPOB — sem números de palma extraídos**, mantendo cego o efeito da Indonésia e do
El Niño sobre o prêmio de substituição do óleo de soja.

**Checkpoints futuros da tese estrutural do farelo (ABIOVE)** — D+90 em 09/09/2026 e
D+180 em 08/12/2026 (insight [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]),
agora reforçados por um ratio tático que converge com o índice estrutural (ISF) pela
primeira vez em dias.

**Definição do range da soja** — três sessões de consolidação apertada (1.192,75 a
1.197,25) pedem um rompimento de qualquer um dos lados para redefinir a tendência de
curto prazo.

---

## Honestidade

O que não foi possível validar neste briefing de 15/07/2026, onde a confiança é baixa
ou há lacunas materiais:

**1. A revisão de série de farelo e óleo é o item mais importante desta seção.** O
dump de hoje atribui às datas de 13/07 e 14/07 valores de preço diferentes dos que as
leituras publicadas nesses mesmos dias registraram: farelo de 13/07 aparece hoje como
317,20 USD/sht (a leitura de 13/07 citava 321,10); óleo de 13/07 aparece hoje como
72,82 cts/lb (a leitura de 13/07 citava 71,02). Essas diferenças não são triviais —
mudam a conclusão do ratio Far/Soj de ">80%" para "<80%" e a leitura do óleo de
"abaixo de 72,00" para "acima de 72,00". Esta leitura tratou os números do dump de
hoje como fonte da verdade, por instrução explícita da rotina ("numeros SEMPRE com
fonte + data" do briefing corrente), mas não há como este sistema confirmar
independentemente qual das duas versões é a correta, nem por que a mudança ocorreu
(correção de settlement, ajuste de fonte upstream, ou outro motivo). Recomenda-se
tratar as conclusões táticas do farelo e do óleo nesta leitura com convicção moderada,
não alta, até a persistência da série ser confirmada em pelo menos mais uma geração
do dump.

**2. O prêmio de exportação de farelo em Paranaguá (+0,05 USD/sht) e o de óleo
(+0,08 cts/lb) estão no mesmo valor exato desde pelo menos 03/07/2026** (NAG, quase
duas semanas sem variação de nenhum centavo) — não é possível distinguir, só com os
dados disponíveis, se isso reflete um mercado de exportação genuinamente parado ou um
valor que não está sendo atualizado de fato na fonte.

**3. A manchete específica de notícias para 15/07/2026 não aparece no dump** — o
contador mostra "160 itens lidos, 5 mantidos (soja/farelo/oleo)", mas nenhuma linha
de headline para a data de hoje foi capturada nesta geração, ao contrário dos dias
anteriores (13/07, 14/07 etc., que trazem a manchete específica). Não há como
confirmar qual foi a notícia mais relevante do dia segundo o próprio sistema.

**4. O WASDE segue cobrindo apenas farelo (Argentina, Brasil, China parcial), sem
nenhum dado de soja em grão ou óleo de soja, em qualquer geografia, e sem nenhum dado
dos Estados Unidos** — sem atualização desde 10/07/2026. A pergunta central sobre
"oferta grande de soja" segue sem canal de resposta interno.

**5. NOPA (fila `release-nopa-2026-07-15`) segue com `monthly_status` em 0,0 bool** —
mesma barreira de assinatura paga documentada desde meados de junho, agora com mais de
um mês sem alternativa de dado primário sobre o esmagamento americano.

**6. Percentis históricos de COT não calculados** — os números de 07/07/2026 (sem
atualização há 8 dias) são lidos apenas em nível absoluto e como fração do open
interest corrente, sem série histórica completa para calibrar zona extrema.

**7. Palma malaia (MPOB) segue sem números extraídos** (15/07/2026, mesmo texto de
HTML sem valores, aproximando-se de um mês e meio consecutivo) — impossível avaliar o
efeito do El Niño ou das restrições indonésias sobre o prêmio de substituição do óleo
de soja.

**8. Os volumes de negociação de hoje chamam atenção pela magnitude baixa** — soja
Q26 com 2.703 contratos, farelo Q26 com apenas 932 (ante 31.109 em 14/07, dia de
expiração/rolagem do contrato N26/julho, o que explica parcialmente o pico de ontem),
óleo Q26 com 1.497. Não há como confirmar, com os dados disponíveis, se estes números
refletem a sessão completa fechada ou uma captura parcial no momento da geração do
dump — vale considerar essa possibilidade antes de usar o volume de hoje como sinal de
convicção (alta ou baixa) do movimento de preço.

**9. Basis físico de Paranaguá x paridade teórica foi calculado cruzando duas fontes
na mesma data (14/07) para evitar misturar câmbio defasado** — o cálculo (R$
140,63 − R$ 133,43 = R$ 7,20/saca) é aritmética direta sobre dois números do próprio
briefing, não um indicador computado internamente pelo sistema.

**10. Clima INMET (BR) não foi usado como driver desta leitura.** Julho é entressafra
da soja brasileira (colheita concluída, plantio só em outubro) — sem relevância
direta para a tese de preço neste momento do calendário agrícola, embora o El Niño
Advisory (NOAA CPC, inalterado) permaneça relevante para a expectativa da safra de
plantio de outubro/26 e para o clima do Sudeste Asiático (palma).

**11. BCBA Argentina — sem relatórios de esmagamento/exportação acessíveis via
scraper** (page_fetched=1,0 mas sem links de relatório, 15/07/2026, sem mudança).

**12. RIN D4 como parâmetro fixo (2,11 USD/RIN) segue sendo uma fonte relevante de
incerteza do modelo de biodiesel**, sem novo dado hoje — a queda de -14,4% na margem
foi atribuída ao heating oil, mas o RIN fixo nunca é testado contra um valor real de
mercado neste sistema.

*Nenhum número foi inventado ou estimado além do que consta no briefing de 15/07/2026
e nos insights anteriores referenciados. A contribuição central desta leitura foi
identificar que o dado histórico de farelo e óleo para 13-14/07 foi revisado entre
gerações do dump, o que inverte a leitura tática de ambas as pernas (farelo de neutro
para bear, óleo de bear para neutro) sem que tenha havido, isoladamente, um evento de
mercado novo — e registrar essa revisão com transparência em vez de simplesmente
adotar a nova conclusão sem explicar de onde ela vem.*
