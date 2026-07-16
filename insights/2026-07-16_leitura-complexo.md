---
data: 2026-07-16
titulo: "Farelo fecha a quarta sessão seguida com o ratio Far/Soj abaixo de 80% (79,78%), confirmando de forma persistente o gatilho estrutural de 11/06; a soja esfria com uma vela fraca (abriu perto da máxima, fechou perto da mínima) dentro do range de consolidação acima de 1.180, na véspera do COT de sexta-feira; e o óleo perde tração no dia — a margem de biodiesel americano caiu -10,0%, a segunda queda de dois dígitos em dois pregões seguidos — mesmo com o Índice de Suporte do Óleo intacto em 100/100 e a curva forward em backwardation ligeiramente mais acentuada"
tags: [complexo, auto-claude]
fontes:
  - CBOT CME (ZSQ26/ZMQ26/ZLQ26 + curva forward completa + HO=F) — sessão de 2026-07-16 (volumes muito baixos hoje — ver Honestidade)
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, ISF/ISO, paridade BR) — 2026-07-16
  - BCB PTAX — último dado 2026-07-15 (USD/BRL 5,0727), usado também no cálculo de paridade de hoje (defasagem de 1 dia)
  - CEPEA/ESALQ Paranaguá e Paraná interior via NAG — último dado 2026-07-15 (suporte Paranaguá R$ 139,99/saca, Paraná interior R$ 133,14/saca)
  - NAG Físico BR (farelo MT/IMEA, RS, Rondonópolis; prêmios export PGUA farelo/óleo) — último dado 2026-07-15
  - CFTC COT Managed Money — dado de referência 2026-07-07, sem atualização; próxima publicação normal amanhã, 2026-07-17 (sexta-feira)
  - USDA Crop Progress — último dado 2026-07-12 (65% bom-ou-melhor), sem atualização; próximo relatório normal ~2026-07-20 (segunda-feira)
  - USDA WASDE — ainda 2026-07-10 (só farelo Argentina/Brasil/China parcial), sem publicação nova
  - NOPA — 2026-07-16, `monthly_status` continua inacessível (paywall), fila `release-nopa-2026-07-16`
  - ABIOVE projeções mensais — balanços ago-dez/2026 (farelo/óleo/soja), sem alteração
  - NOAA CPC ENSO — 2026-07-16 (El Niño Advisory, sem mudança)
  - MPOB — 2026-07-16 (parser sem números extraídos, streak de ~2 semanas nesta janela de dados)
  - BCBA — 2026-07-16 (acessível, sem links de relatório detectados)
  - Notícias Agrícolas / Farm Progress RSS — 2026-07-16 (160 itens lidos, 8 mantidos, sem manchete específica listada no dump de hoje — ver Honestidade)
  - Forecasts estatísticos internos — 2026-07-16 (recalibrados; pela primeira vez em várias leituras, as seis bandas — 3 commodities × 2 horizontes — fecham simultaneamente em viés altista)
  - system/tributario_watch.toml — MP-1358-2026 (vigência formal encerrada há 5 dias, status ainda "tramitação"), PISCOFINS-BIODIESEL-ISENCAO (vence em 15 dias), MP-1363-2026, STJ-RESP-2165276, B16-CNPE-2026 — todos `atualizado_em` 2026-06-05 (41 dias sem atualização do monitor)
  - Cruza com [[2026-07-15_leitura-complexo]], [[2026-07-13_leitura-complexo]], [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (checkpoint D+7, agora com 4ª confirmação consecutiva), [[2026-05-26_subvencao-fossil-aperta-biodiesel]], [[2026-05-26_pis-cofins-biodiesel-explica-mercado-fisico-fraco]]
status: ativa
vies: [neutral-soja, bear-farelo, neutral-oleo_soja]
---

## Visão geral

O complexo soja é uma fábrica com uma única matéria-prima (a soja em grão) e dois
produtos de saída em proporção fixa por bushel esmagado: o **farelo** (fração
proteica, ~78% da massa, vira ração animal) e o **óleo degomado** (fração de gordura,
~18-20% da massa, vira óleo de cozinha e biodiesel). Quem decide o ritmo de
esmagamento é a esmagadora, olhando a **crush margin** (valor de farelo + óleo por
bushel, menos o custo daquele bushel de soja, medido na CBOT — Chicago Board of
Trade, a bolsa onde soja/farelo/óleo são negociados como futuros) e o **oil share**
(fração desse valor capturada pelo óleo). Hoje, quinta-feira 16/07/2026, a crush
margin fechou em 3,0134 USD/bushel (indicadores, farelo 319,00 + óleo 72,64 − soja
1.199,50), essencialmente estável frente aos últimos pregões (3,0145 em 15/07, 3,0193
em 14/07) — a esmagadora segue com forte incentivo econômico a rodar a pleno vapor,
sem sinal de arrefecimento.

**O que mudou hoje foi a persistência de dois sinais divergentes dentro do mesmo
complexo, mais uma confirmação importante sobre a qualidade dos próprios dados que
alimentam esta leitura.** No **farelo**, o ratio Far/Soj (preço do farelo dividido
pelo da soja, na mesma base — abaixo de 80% indica farelo "abundante" frente à soja)
fechou em 79,78% hoje, a **quarta sessão consecutiva** abaixo do limiar de 80%
(79,52% em 13/07, 79,83% em 14/07, 79,58% em 15/07, 79,78% hoje) — o gatilho tático
da tese de 11/06/2026 (`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`),
que a leitura de ontem já havia dado como confirmado com ressalva (a confirmação
tinha vindo de uma revisão de dado, não de um evento novo), hoje se confirma de novo
com um número gerado organicamente na sessão do dia, sem qualquer revisão retroativa
envolvida. Isso eleva a convicção da tese estrutural do farelo de moderada para
moderada-alta. Na **soja**, o fechamento de hoje (1.199,50 cts/bu) segue 1,65% acima
da resistência-agora-suporte de 1.180,00, mas a vela do dia é o oposto da vela
construtiva de ontem: abriu perto da máxima (1.202,00, muito perto do topo do dia de
1.205,50) e fechou perto da mínima (1.199,50, contra mínima de 1.197,75) — um padrão
de rejeição no topo, não de recuperação, o quarto pregão seguido sem uma nova máxima
desde os 1.208,75 intradiários de 13/07. No **óleo**, o fechamento de 72,64 cts/lb
também fecha fraco dentro do range do dia (perto da mínima de 72,42, longe da máxima
de 73,18, -0,52% na sessão), e a margem de biodiesel americano (receita do heating
oil + crédito RIN D4, menos o custo do óleo) caiu -10,0% no dia, a segunda queda de
dois dígitos percentuais em dois pregões consecutivos (-14,4% ontem, -10,0% hoje,
queda acumulada de -20,0% desde o pico de 14/07) — mas o Índice de Suporte do Óleo
(ISO) permanece intacto em 100/100 e a curva forward está em backwardation
ligeiramente mais acentuada que ontem. **A peça mais importante para a integridade
desta leitura, porém, veio de conferir os próprios números:** o volume de farelo que
a leitura de ontem registrou para a sessão de 15/07 (932 contratos, capturado no
mesmo dia) aparece no dump de hoje, já fechado e definitivo, como 25.461 contratos —
27 vezes mais. Isso confirma, com prova concreta, a suspeita registrada na seção de
Honestidade de ontem: os volumes capturados no mesmo dia da sessão são fortemente
subestimados, e os volumes de hoje (soja 2.242, farelo 1.304, óleo 1.573) quase
certamente também são captura parcial, não a sessão fechada — não devem ser lidos
como "dia de baixa convicção" até serem confirmados amanhã. **Leitura de uma linha:**
o pivô do complexo continua sendo a soja (ainda seguindo acima de 1.180, mas com o
quarto fechamento fraco seguido, aumentando o risco de reversão do range antes do
COT de amanhã), o farelo aprofunda a convicção bear com uma quarta confirmação
orgânica do ratio, e o óleo mostra a primeira divergência clara entre estrutura (ISO,
backwardation, forecast) e momentum de curto prazo (margem em queda, vela fraca) —
convicção moderada em todas as três pernas, com o evento de amanhã (COT, sexta-feira)
como o próximo teste real de quem estava certo.

---

## Soja

**Viés: neutro tático (rebaixado de bull tático em 15/07) — fechou em 1.199,50
cts/bu (16/07/2026), 1,65% acima da resistência-agora-suporte de 1.180,00, mas com
uma vela de rejeição no topo (abriu em 1.202,00, perto da máxima de 1.205,50, e
fechou em 1.199,50, perto da mínima de 1.197,75) — o oposto da vela de recuperação de
ontem, e o quarto pregão seguido sem uma nova máxima desde 13/07. Trata
`alerta-quebra_resistencia-soja_cbot-2026-07-16`.**

### O que sustenta a tese

**O nível técnico de 1.180,00 segue tecnicamente de pé, mas a qualidade da sessão de
hoje piorou frente a ontem.** Fechamento de 1.199,50 cts/bu (CBOT, 16/07/2026), com
abertura em 1.202,00 (perto da máxima do dia, 1.205,50) e mínima de 1.197,75 — ou
seja, o preço abriu perto do teto do dia e fechou perto do piso, a apenas 22,6% do
range total acima da mínima (1.199,50-1.197,75 = 1,75, sobre um range total de 7,75
pontos). Isso é um padrão de rejeição intradiário: o mercado tentou avançar cedo no
dia, esbarrou em vendedores, e devolveu praticamente todo o ganho até o fechamento.
Contrasta diretamente com a vela de 15/07 (abriu na mínima, fechou perto da máxima,
recuperação clássica) e reforça a leitura de que o rali de 06-07/07 perdeu força:
nenhum fechamento desde 13/07 superou os 1.202,25 (fechamento revisado de 15/07 — ver
Honestidade), e o intervalo de 4 pregões (1.192,75 a 1.205,50 em máximas intradiárias)
segue sendo uma consolidação lateral apertada, não uma tendência.

**Olhando os quatro últimos fechamentos em sequência — 1.196,75 (13/07) → 1.192,75
(14/07) → 1.202,25 (15/07, valor final revisado — ver Honestidade) → 1.199,50 (hoje)
— o padrão é de um mercado que testa os dois extremos do range sem conseguir romper
para nenhum dos lados.** O rompimento de 06-07/07 segue tecnicamente de pé (nenhum
fechamento voltou a testar 1.180,00), mas quatro sessões seguidas de range estreito
sem direção definida, somadas à vela de rejeição de hoje, tornam o cenário de
correção mais profunda (teste de 1.180,00) tão plausível quanto o de continuação —
o que justifica rebaixar o viés de bull tático para neutro até o próximo evento de
catalisação (o COT de amanhã).

**O USDA Crop Progress permanece sem atualização desde 12/07/2026** (65% da lavoura
americana em condição boa-ou-excelente, 12% excelente + 53% boa, 6% em condição
ruim/poor) — o próximo relatório semanal normal deve sair na segunda-feira,
20/07/2026 (dados "as of" domingo 19/07). Sem dado novo, o argumento de melhora
marginal de oferta americana (a leitura de 15/07 já registrava isso como
estruturalmente bearish, mesmo que pequeno) permanece congelado, nem reforçando nem
enfraquecendo a tese.

**A curva forward mantém o formato de "sorriso" já documentado**: Agosto/26 (Q26,
spot) 1.199,50 → Setembro/26 (U26) 1.189,00 (desconto de -10,50, o padrão sazonal de
pressão pré-colheita americana, quase idêntico ao desconto de -10,50 de ontem) →
Novembro/26 (X26) 1.198,75 (recupera +9,75 sobre setembro) → Janeiro/27 (F27)
1.212,75 (+14,00) → Março/27 (H27) 1.216,75 (+4,00) — desconto no meio da curva
(pressão de colheita/safra nova) e prêmio na ponta longa (custo de carregamento ou
expectativa de aperto pós-colheita), formato estável dia a dia, sem sinal de estresse
de estoque imediato nem de relaxamento.

**A paridade teórica em reais caiu para R$ 134,14/saca 60kg** (indicadores,
16/07/2026: CBOT 1.199,50 cts × PTAX 5,0727 USD/BRL, sem basis) — o câmbio usado
ainda é o de 15/07/2026 (o BCB — Banco Central do Brasil — ainda não havia publicado
o PTAX de hoje no momento da coleta), então a paridade de hoje soma o recuo de preço
em Chicago à mesma taxa de câmbio de ontem. Comparando de forma pareada por data (as
duas leituras usando 15/07/2026 como referência): paridade teórica de 15/07 em
R$ 134,45/saca (CBOT 1.202,25 × PTAX 5,0727) versus o preço físico de Paranaguá do
mesmo dia (R$ 139,99/saca, CEPEA/ESALQ via NAG, 15/07/2026) — um prêmio de
R$ 5,54/saca (+4,1%) do físico sobre a paridade teórica. Esse prêmio é positivo (sinal
de demanda de exportação real no porto), mas **comprimiu** frente ao prêmio pareado de
14/07 documentado ontem (R$ 7,20/saca, +5,4%) — uma leitura ligeiramente menos
bullish para a demanda física de exportação do que a de ontem, ainda que o sinal
direcional (prêmio positivo) se mantenha. O preço físico do Paraná interior (via NAG)
fechou em R$ 133,14/saca (15/07/2026), um desconto de R$ 6,85/saca frente ao suporte
de Paranaguá — o spread logístico normal de frete até o porto.

**O posicionamento dos fundos (COT, CFTC) permanece no dado de referência de
07/07/2026** — managed money net long em +69.579 contratos (7,13% do open interest de
975.954), sem atualização nova. **A próxima publicação normal sai amanhã,
17/07/2026 (sexta-feira)** — o evento mais importante e mais próximo desta leitura:
será o primeiro teste real de se a compra dos fundos sobreviveu à semana de
consolidação de 13-16/07, incluindo a vela de rejeição de hoje.

**Os forecasts estatísticos internos (16/07/2026)** seguem com viés altista: central
7d = 1.226,82 cts/bu (bandas 1.176,23-1.277,42); central 30d = 1.327,14 cts/bu
(bandas 1.222,39-1.431,88) — ambos acima dos centrais de ontem (1.219,37 e 1.309,78).
É importante registrar que esses forecasts são um modelo estatístico puro (média
móvel de 20 dias + volatilidade + inclinação recente), que reage a momentum de preço
passado — ele ainda não "viu" a vela de rejeição de hoje refletida em um novo
fechamento mais baixo, então seu viés altista deve ser lido como um eco do rali
anterior, não como uma previsão independente da vela fraca de hoje.

### O que invalida / risco para a soja

- **Um fechamento abaixo de 1.197,75 (mínima de hoje) ou de 1.180,00** reabriria o
  teste do nível-chave e daria força ao cenário de reversão do rompimento — a vela de
  rejeição de hoje é o primeiro sinal técnico nessa direção desde o rompimento de
  06-07/07.
- **O COT de amanhã (17/07) mostrar que o managed money vendeu durante a
  consolidação** — quatro sessões de range apertado com uma vela de rejeição no fim
  é exatamente o tipo de padrão que precede realização de lucro de fundos táticos.
- **Novas leituras de Crop Progress (esperadas ~20/07) mostrarem melhora
  continuada** — a leitura de 12/07 já mostrou +1pp; uma sequência de melhoras
  reduziria progressivamente o argumento de "oferta apertada".
- **O prêmio físico de Paranaguá continuar comprimindo** — caiu de +5,4% (14/07) para
  +4,1% (15/07, pareado); uma nova compressão sinalizaria enfraquecimento da demanda
  de exportação que vinha sustentando o viés de alta.

### Leitura operacional — soja

O viés tático foi rebaixado de bull para neutro: o range de 4 sessões não resolveu na
direção de uma nova máxima, e a vela de hoje, ao contrário da de ontem, é de rejeição
no topo, não de recuperação. Para quem está comprado taticamente, a referência de
stop desce para perto de 1.197,75 (mínima de hoje) — um fechamento abaixo desse nível,
e principalmente abaixo de 1.180,00, seria confirmação de reversão do range para
baixo. Para quem está vendido contra o rompimento, a vela de hoje é o primeiro
argumento técnico a favor da posição desde 13/07, mas o nível de 1.180,00 continua
sendo o teste decisivo, não ainda rompido. O COT de amanhã (17/07) é o evento que
deve dar a direção mais clara para os próximos dias, para qualquer um dos dois lados.

---

## Farelo

**Viés: bear (tático + estrutural), convicção elevada de moderada para
moderada-alta — o ratio Far/Soj fechou em 79,78% hoje, a QUARTA sessão consecutiva
abaixo de 80% (79,52% em 13/07, 79,83% em 14/07, 79,58% em 15/07, 79,78% hoje), e
pela primeira vez desde a revisão de dado documentada ontem, a confirmação de hoje
veio de um número gerado organicamente no dia, sem qualquer revisão retroativa
envolvida. Trata `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
(agora com quatro confirmações consecutivas) e `release-nopa-2026-07-16`.**

### O que sustenta a tese

**O ratio Far/Soj de hoje fechou em 79,78%** (indicadores, 16/07/2026: farelo 319,00
USD/short_ton ÷ soja 1.199,50 cts/bu, na mesma base), a quarta sessão seguida abaixo
do limiar de 80% que a tese original de 11/06/2026 usava como gatilho tático para
"farelo abundante frente à soja". Diferente da confirmação de ontem — que veio de uma
revisão retroativa dos dados de 13-14/07 —, a confirmação de hoje é direta: o número
de hoje foi calculado com o fechamento de hoje, sem qualquer correção de série
envolvida. Isso é relevante porque eleva a convicção da tese de moderada (como
registrado ontem, por causa da origem via revisão) para moderada-alta: agora há
quatro sessões seguidas, sendo a mais recente uma confirmação "limpa".

**A crush margin fechou em 3,0134 USD/bushel** (indicadores, 16/07/2026: farelo
319,00 + óleo 72,64 − soja 1.199,50), praticamente estável frente a 15/07 (3,0145) e
14/07 (3,0193) — seguindo em patamar historicamente elevado, sem sinal de
arrefecimento do incentivo de esmagamento. O mecanismo continua o mesmo: quanto maior
a crush margin, maior o incentivo da esmagadora a processar soja a pleno vapor, e
mais farelo (subproduto obrigatório do esmagamento) entra no mercado — a base
estrutural da tese ABIOVE de excesso doméstico de farelo no 2º semestre.

**A trajetória projetada da ABIOVE (Associação Brasileira das Indústrias de Óleos
Vegetais, projeções mensais, sem alteração) segue sendo o pilar mais sólido do
argumento estrutural, porque não depende do preço do dia.** A exportação de farelo
brasileiro projetada cai de 1.400 mil toneladas em agosto/2026 para 700 mil toneladas
em dezembro/2026 (queda de 50% em 4 meses), enquanto a produção cai de forma bem mais
suave (2.285,06 → 1.659,04 mil toneladas no mesmo período, -27%) e o estoque final
oscila sem tendência clara entre 1.000 e 1.224 mil toneladas ao longo de todo o
semestre. O mecanismo de transmissão é direto: menos farelo saindo pelo porto, com
produção caindo bem menos que a exportação, empurra o volume excedente para o mercado
interno de ração, pressionando o preço doméstico.

**As praças físicas de farelo no Brasil (NAG) permanecem no último dado de
15/07/2026** — Mato Grosso/IMEA R$ 1.577,34/ton, Rondonópolis R$ 1.670,00/ton, RS
R$ 1.640,00/ton — sem variação frente a 14/07 (mesmos valores, "var 0,0%" reportado
em todas as três praças). O prêmio de exportação em Paranaguá segue em +0,05
USD/short_ton (julho/26, NAG, inalterado desde pelo menos 03/07/2026, agora quase
duas semanas exatas no mesmo valor) — como já registrado ontem, essa constância pode
refletir um mercado de exportação genuinamente parado (reforçando a absorção
doméstica, coerente com a tese bear) ou uma fonte que não está sendo atualizada de
fato (ver Honestidade). De qualquer forma, um prêmio de exportação perto de zero
sustenta o mecanismo de que o farelo brasileiro não tem para onde escoar
externamente.

**O Índice de Sobra de Farelo (ISF) permanece em 80/100 (4 de 5 condições
estruturais)** (indicadores, 16/07/2026) — o mesmo nível desde pelo menos 01/07/2026,
agora pelo menos 16 dias consecutivos sem mudança, o índice estrutural mais estável e
persistente de toda a leitura, e que segue convergindo com o sinal tático do ratio.

**Tratando `release-nopa-2026-07-16`:** o NOPA (National Oilseed Processors
Association, dado mensal de esmagamento americano) segue com `monthly_status` em 0,0
bool — a mesma barreira de assinatura paga documentada desde meados de junho. O item
aparece de novo na fila como "release" do dia, mas não há nenhuma informação nova
para interpretar; não há confirmação direta do ritmo de esmagamento americano por
fonte primária.

**O oil-meal spread (óleo menos farelo, por bushel) caiu para 0,9724 USD/bu**
(indicadores, 16/07/2026), de 1,0054 (15/07) — uma queda de -3,3% no dia, coerente
com o farelo ganhando terreno relativo frente ao óleo hoje (o ratio Far/Soj subiu de
79,58% para 79,78%), mesmo que ambos os patamares sigam abaixo do limiar de 80% que
define a tese bear estrutural do farelo.

**O forecast estatístico do farelo (16/07/2026)** segue com viés altista: central 7d
= 325,11 USD/sht (bandas 312,67-337,56); central 30d = 347,56 USD/sht (bandas
321,80-373,33) — o modelo estatístico (que reage a momentum de preço recente, não a
fundamentos) segue na direção oposta à tese fundamentalista ABIOVE + ratio, a mesma
contradição entre curto prazo (modelo, movido pelo próprio preço em USD/sht que vem
subindo desde a mínima de 293 documentada em junho) e médio prazo (estrutura) já
documentada nas leituras anteriores.

### O que invalida / risco para o farelo

- **A tese estrutural ABIOVE não se confirmar no físico ao longo do 2S/26.**
- **O ratio reverter para cima de 80% nos próximos pregões** — mesmo com quatro
  sessões seguidas abaixo do limiar, o ratio de hoje (79,78%) está a apenas 0,22
  ponto percentual da fronteira; uma alta modesta do farelo ou queda adicional da
  soja já reverteria o sinal.
- **NOPA seguir inacessível indefinidamente**, sem confirmação do esmagamento
  americano para os checkpoints D+90 (09/09/2026) e D+180 (08/12/2026).
- **O prêmio de exportação Paranaguá "congelado" em 0,05 USD/sht ser, na verdade, um
  dado sem atualização de fonte, não um preço de mercado real** — reduziria a
  confiança no argumento de ausência de competitividade exportadora (ver
  Honestidade).
- **O volume de hoje (1.304 contratos no farelo Q26) ser uma captura parcial da
  sessão** — como documentado na Visão geral, o volume de ontem (932, capturado no
  mesmo dia) foi revisado hoje para 25.461 (27x maior); se o mesmo ocorrer com o
  fechamento de hoje amanhã, o preço de fechamento de 319,00 também pode ser
  revisado.

### Leitura operacional — farelo

Com o gatilho tático agora confirmado de forma orgânica pela quarta sessão seguida
(não mais dependente da revisão de dado que sustentou a confirmação de ontem), a
convicção sobe de moderada para moderada-alta: o cenário original da tese de 11/06
(spread de convergência farelo/soja, ou posição vendida tática em farelo isolado)
tem hoje o suporte de dado mais limpo desde que a tese foi aberta, partindo de um
ratio (79,78%) ainda perto da fronteira de 80%, mas consistentemente abaixo dela há
quatro pregões. Para quem prefere a tese estrutural pura (ABIOVE), o veículo mais
robusto continua sendo o spread farelo/soja ou o crush completo, em vez de
direcional puro — especialmente dado que o ratio, mesmo confirmado, segue
tecnicamente próximo o suficiente da fronteira de 80% para reverter com um movimento
modesto de qualquer uma das duas pernas.

---

## Óleo

**Viés: neutro, com o primeiro sinal claro de divergência entre estrutura e
momentum de curto prazo — o fechamento de hoje (72,64 cts/lb) é fraco dentro do
range do dia e a margem de biodiesel caiu -10,0% (segunda queda de dois dígitos
percentuais seguida), mas o Índice de Suporte do Óleo (ISO) segue em 100/100, o oil
share segue acima de 53%, e a curva forward está em backwardation ligeiramente mais
acentuada que ontem.**

### O que sustenta a tese

**O óleo fechou hoje em 72,64 cts/lb** (CBOT, 16/07/2026), com abertura em 73,02
(perto da máxima do dia, 73,18) e mínima de 72,42 — fechando a apenas 28,9% do range
total acima da mínima (72,64-72,42 = 0,22, sobre um range total de 0,76 pontos), uma
sessão que abriu perto do teto e devolveu a maior parte do ganho, -0,52% no dia frente
ao fechamento de 72,92 de 15/07/2026 (valor final revisado — ver Honestidade). É a
mesma assinatura técnica da vela fraca da soja hoje (abertura perto da máxima,
fechamento perto da mínima), sugerindo que o recuo de hoje tem um componente de
complexo (movimento conjunto soja-óleo), não é isolado ao óleo.

**A curva forward mantém backwardation limpa, e ligeiramente mais acentuada que
ontem**: Agosto/26 (Q26, spot) 72,64 → Setembro/26 (U26) 71,91 (-0,73) → Outubro/26
(V26) 71,12 (-0,79) → Dezembro/26 (Z26) 70,68 (-0,44) → Janeiro/27 (F27) 70,47
(-0,21) — uma queda de -2,17 cts/lb (-3,0%) de agosto a janeiro/27, ante -1,95 cts/lb
(-2,7%) na curva de ontem. Esse formato (prêmio no vencimento mais próximo, desconto
nos mais distantes) reflete demanda física presente forte (biodiesel americano +
exportação brasileira) frente a uma expectativa de oferta mais confortável adiante —
o fato de a backwardation ter se acentuado no mesmo dia em que o spot caiu é
tecnicamente positivo: o mercado não está descontando o recuo de hoje para os
vencimentos futuros, ao contrário, está pagando ainda mais pela entrega mais próxima
em termos relativos.

**A margem de biodiesel americano caiu para 0,7595 USD/galão** (indicadores,
16/07/2026: receita 7,0075 = HO/heating oil 3,8425 + 1,5×RIN 2,11; custo 6,2480 =
óleo 5,4480 + industrial 0,80), uma queda de -10,0% frente a 15/07 (0,8443) — a
segunda queda de dois dígitos percentuais em dois pregões seguidos, depois da queda
de -14,4% registrada ontem. Acumulada desde o pico de 14/07 (0,9493), a margem caiu
-20,0% em dois dias. O mecanismo, como ontem, vem majoritariamente do lado da
receita: o heating oil (proxy de receita do biodiesel) recuou pela terceira sessão
seguida — 4,0143 (14/07) → 3,9483 (15/07, -1,6%) → 3,8425 (16/07, -2,7%) —, uma
queda acumulada de -4,3% em dois dias, enquanto o custo do óleo (insumo) se moveu
pouco (5,47 → 5,45 cts/lb). Ainda dentro da faixa histórica de conforto de 0,50-0,80
USD/galão (documentada em leituras anteriores como a zona onde compradores
voluntários de blending, acima do mandato B15, costumam atuar), mas a margem de hoje
(0,7595) já está bem mais perto do piso dessa faixa do que do teto — se o heating oil
continuar a sequência de três quedas seguidas, a margem pode sair da zona de conforto
nos próximos pregões, reduzindo o incentivo doméstico americano ao óleo.

**O Índice de Suporte do Óleo (ISO) permanece em 100/100 (5 de 5 condições)**
(indicadores, 16/07/2026) — o mesmo patamar máximo desde 01/07/2026, agora pelo menos
16 dias consecutivos sem qualquer sinal de enfraquecimento, mesmo com a compressão
acumulada de -20,0% na margem de biodiesel nos últimos dois dias. Essa persistência é
justamente o ponto central da divergência desta leitura: o índice estrutural (que
soma condições de crush margin, oil share, backwardation, COT e margem de biodiesel
dentro da faixa de conforto) segue no máximo, mesmo com um dos seus componentes
(a margem) em trajetória de queda acentuada.

**O oil share (fração do valor do crush capturada pelo óleo) está em 53,24%**
(indicadores, 16/07/2026), levemente abaixo dos 53,34% de 15/07 (revisado) e dos
53,28% de 14/07 — seguindo folgadamente acima de 50%, confirmando que o óleo
continua sendo o motor de valor do crush, mesmo com a leve cessão de terreno para o
farelo documentada no oil-meal spread.

**O forecast estatístico do óleo (16/07/2026) reforça o viés altista**: central 7d =
73,43 cts/lb (bandas 69,03-77,84); central 30d = 76,79 cts/lb (bandas 67,67-85,91) —
ambos em viés "altista", consolidando a mudança que começou ontem (quando o modelo
de 30d assumiu alta pela primeira vez em semanas). É a primeira leitura em que as
seis bandas de forecast do sistema (soja, farelo e óleo, 7d e 30d) fecham
simultaneamente em viés altista — um sinal puramente técnico/estatístico (o modelo
não conhece fundamentos), mas que contrasta com a vela fraca e a margem em queda
documentadas hoje, reforçando a leitura de que o curto prazo (preço/momentum) e o
médio prazo (estrutura + modelo estatístico) estão, pela primeira vez em dias,
puxando em direções diferentes dentro do próprio óleo.

### O que invalida / risco para o óleo

- **Um fechamento abaixo de 71,12 (o vencimento de outubro na curva de hoje) ou
  repetição de um fechamento como o antigo 71,02 citado em leituras anteriores**
  reabriria o cenário bear tático — ainda não ocorreu nas últimas 4 sessões, mas a
  vela de rejeição de hoje é o primeiro sinal de enfraquecimento desde a reversão
  registrada em 15/07.
- **A margem de biodiesel (0,7595 USD/gal) continuar caindo** — a queda acumulada de
  -20,0% em dois dias é o maior movimento de dois pregões documentado recentemente;
  se o heating oil mantiver a sequência de três quedas seguidas, a margem sai da
  faixa de conforto histórica (0,50-0,80) pelo lado de baixo.
- **O heating oil (proxy de receita do biodiesel) seguir em queda** — recuou -1,6% e
  depois -2,7% em dois pregões seguidos; essa tendência (diferente da reversão
  pontual documentada ontem) é um fator externo ao complexo soja (mercado de
  energia) que pode continuar ditando o ritmo da margem de biodiesel.
- **A divergência entre ISO (100/100, estrutural) e a margem em queda (tático) não
  se resolver a favor do índice estrutural** — se a margem continuar caindo, alguma
  das cinco condições que compõem o ISO deve, eventualmente, deixar de ser
  satisfeita.
- **MPOB seguir inacessível** — impossível avaliar o efeito do El Niño ou das
  restrições indonésias sobre o prêmio de substituição via palma.

### Leitura operacional — óleo

O viés permanece neutro, mas a natureza da neutralidade mudou frente a ontem: ontem
era uma neutralidade de "sem direção clara nos últimos 3 fechamentos"; hoje é uma
neutralidade de "estrutura (ISO 100/100, backwardation, oil share, forecast) contra
momentum de curto prazo (vela fraca, margem de biodiesel em queda acentuada)". Para
quem mantém exposição relativa ao óleo dentro do crush, os pilares estruturais
seguem intactos e até um pouco mais fortes (backwardation mais acentuada). Para quem
opera direcional puro em óleo, a vela de hoje e a queda de dois dias na margem de
biodiesel são o primeiro argumento tático a favor de reduzir exposição comprada até o
COT de amanhã esclarecer se o movimento de fundos acompanha o enfraquecimento de
momentum. O spread oil-meal (óleo menos farelo) segue sendo o veículo mais direto
para capturar a divergência estrutural entre as duas pernas sem depender da direção
absoluta do óleo, ainda que tenha comprimido -3,3% hoje (farelo ganhando terreno
relativo).

---

## Spreads e crush — leitura de complexo

### Crush margin: 3,0134 USD/bu — estável em patamar elevado

A crush ficou praticamente estável nos últimos 3 pregões (3,0211 em 13/07 → 3,0193
em 14/07 → 3,0145 em 15/07 → 3,0134 hoje), sem sobressaltos, seguindo em nível
historicamente alto. O incentivo de esmagamento a pleno vapor permanece intacto,
alimentando o mecanismo estrutural ABIOVE mesmo com o preço relativo de cada perna se
movendo em direções distintas dentro do complexo.

### Ratio Far/Soj: 79,78% — quarta sessão abaixo de 80%, gatilho confirmado organicamente

O achado central desta leitura: quatro sessões seguidas abaixo de 80% (79,52 → 79,83
→ 79,58 → 79,78), sendo a de hoje a primeira confirmação que não depende de uma
revisão retroativa de série. Trata
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` — o gatilho
tático está confirmado com convicção moderada-alta, a mais alta desde a abertura da
tese em 11/06/2026.

### Oil share: 53,24% — leve recuo, mas óleo segue dominando o crush

Recuou ligeiramente frente aos últimos dias (53,44% em 13/07, 53,28% em 14/07,
53,34% em 15/07 revisado, 53,24% hoje) — folgadamente acima de 50%, o óleo seguindo
como o principal captador do valor do crush, mas cedendo terreno marginal ao farelo
nesta sessão.

### Oil-meal spread: 0,9724 USD/bu — queda de -3,3% no dia

Recuou de 1,0054 (15/07, revisado) para 0,9724 USD/bu (16/07/2026) — mede o valor do
óleo menos o valor do farelo por bushel; a queda de hoje é coerente com o farelo
ganhando terreno relativo (ratio Far/Soj subindo de 79,58% para 79,78%) mesmo dentro
da mesma tese bear estrutural do farelo.

### ISF em 80/100, ISO em 100/100 — patamar sustentado, agora pelo menos 16 dias

O Índice de Sobra de Farelo (ISF, 4/5 condições) e o Índice de Suporte do Óleo (ISO,
5/5 condições) permanecem nos mesmos níveis desde pelo menos 01/07/2026 (indicadores,
16/07/2026) — a persistência do ISO em 100/100 mesmo com a margem de biodiesel caindo
-20,0% em dois dias é o ponto mais relevante para monitorar nos próximos pregões: ou
a margem se recupera, ou o índice deve eventualmente refletir a deterioração.

### O que os índices dizem juntos em 16/07/2026

ISF 80/100 + ISO 100/100 (ambos estáveis há ~16 dias) + ratio Far/Soj em 79,78% (4ª
sessão abaixo de 80%, gatilho confirmado organicamente pela primeira vez) + oil share
em leve recuo (53,24%) + crush margin estável em patamar elevado (3,0134) + oil-meal
spread em queda (-3,3%) formam um quadro onde a divergência entre farelo e óleo,
identificada pela primeira vez de forma coesa na leitura de ontem, se aprofunda: o
farelo acumula convicção bear (agora moderada-alta) enquanto o óleo mostra sinais
mistos — estrutura ainda favorável (ISO no máximo, backwardation mais acentuada), mas
momentum de curto prazo enfraquecendo (vela fraca, margem em queda). O complexo
segue esmagando a pleno vapor (crush estável e elevada), o que garante fluxo
constante de farelo (reforçando a tese bear) e de óleo (sem sinal de escassez física)
simultaneamente.

---

## Lente fiscal e regulatória BR

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L) — a vigência
formal (`vigencia_ate` 11/07/2026) venceu há 5 dias, e o monitor tributário segue sem
qualquer atualização de status** (`system/tributario_watch.toml`, evento
MP-1358-2026, `atualizado_em` 2026-06-05, status ainda "tramitacao", `proximo_marco` =
"Deliberação comissão mista", `proximo_data` = 2026-07-11, já vencida há 5 dias). São
agora cinco dias úteis (13, 14, 15 e 16/07, mais o fim de semana anterior) desde o
vencimento formal sem nenhuma fonte pública rastreada pelo sistema (ABIOVE, NAG,
notícias) confirmar se a MP caducou, foi prorrogada por novo decreto, ou foi
convertida em lei. O mecanismo de transmissão para o complexo permanece o mesmo já
documentado: enquanto o combustível fóssil segue subsidiado, a competitividade
relativa do biodiesel dentro do mix B15 mandatório fica pressionada, mantendo a
margem da indústria de biodiesel mais apertada do que sem a subvenção ao concorrente
fóssil — um pano de fundo estrutural que ecoa (por um canal distinto, mais lento) a
mesma direção da compressão de margem de curto prazo documentada hoje na seção Óleo
(que veio do heating oil americano, não desta MP brasileira).

**Isenção PIS/Cofins biodiesel — vencimento em 31/07/2026, agora a 15 dias.** Sem
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

**O monitor tributário como um todo está há 41 dias sem qualquer atualização**
(`atualizado_em` 2026-06-05 em todos os eventos rastreados) — um dia a mais que
ontem, e o intervalo cresce em um momento em que dois vetores (MP 1.358 e a isenção
PIS/Cofins) têm datas de vencimento formal já vencida ou a apenas 15 dias. Vale
sinalizar este ponto como prioridade de manutenção do sistema, independentemente da
leitura de preço.

---

## Riscos e eventos próximos

**COT (CFTC) de amanhã, 17/07/2026 (sexta-feira) — o evento mais próximo e mais
importante desta leitura.** Testará se o managed money manteve a compra em
soja/farelo/óleo ou começou a reduzir posições durante a semana de consolidação
apertada de 13-16/07, que terminou hoje com velas de rejeição tanto na soja quanto
no óleo.

**Confirmar se os volumes e preços de hoje (16/07) sofrem a mesma revisão
identificada no farelo de ontem (932 → 25.461 contratos).** É o segundo item mais
urgente: se o padrão se repetir, o fechamento de hoje (soja 1.199,50, farelo 319,00,
óleo 72,64) pode não representar a sessão completa, e a leitura de "vela de rejeição"
desta análise precisaria ser reavaliada com os números finais.

**Desfecho da MP 1.358/2026 — vigência formal encerrada há 5 dias, sem confirmação.**
Monitorar deliberação da comissão mista e qualquer decreto de prorrogação.

**Isenção PIS/Cofins biodiesel — vencimento 31/07/2026 (15 dias).** Sem sinalização de
renovação até agora.

**Próxima leitura de USDA Crop Progress — esperada ~20/07/2026 (segunda-feira),
dados "as of" 19/07.** Sem atualização desde 12/07.

**NOPA — segue inacessível** (fila `release-nopa-2026-07-16` tratada aqui, sem dado
interpretável), sem crush americano confirmado por fonte primária.

**MPOB — sem números de palma extraídos**, mantendo cego o efeito da Indonésia e do
El Niño sobre o prêmio de substituição do óleo de soja.

**A margem de biodiesel americano em trajetória de queda acentuada (-20,0% em dois
dias)** — se o heating oil continuar a sequência de três quedas seguidas, a margem
sai da faixa histórica de conforto (0,50-0,80 USD/gal), o que testaria diretamente a
persistência do ISO em 100/100.

**Checkpoints futuros da tese estrutural do farelo (ABIOVE)** — D+90 em 09/09/2026 e
D+180 em 08/12/2026 (insight [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]),
agora reforçados por quatro sessões consecutivas do ratio tático abaixo de 80%, a
mais recente confirmada organicamente.

**Definição do range da soja e do óleo** — quatro sessões de consolidação apertada
na soja, ambas encerrando hoje com velas de rejeição em soja e óleo, pedem um
rompimento de qualquer um dos lados para redefinir a tendência de curto prazo, com o
COT de amanhã como catalisador mais provável.

---

## Honestidade

O que não foi possível validar neste briefing de 16/07/2026, onde a confiança é baixa
ou há lacunas materiais:

**1. A descoberta mais importante desta leitura: o volume de farelo de ontem (15/07)
foi revisado de 932 para 25.461 contratos — 27 vezes mais.** A leitura publicada em
15/07/2026 registrou, com os dados então disponíveis (capturados no mesmo dia da
sessão), um volume de 932 contratos para o farelo Q26 e usou esse número para
questionar se a sessão estava sendo capturada de forma parcial. O dump de hoje, já
com a sessão de 15/07 fechada e definitiva, mostra 25.461 contratos para o mesmo
contrato na mesma data — confirmando, com prova concreta e não apenas suspeita, que
os volumes (e possivelmente os próprios preços de fechamento) capturados no mesmo dia
da sessão são sistematicamente subestimados. Isso significa que os volumes de hoje
usados nesta leitura (soja 2.242, farelo 1.304, óleo 1.573, heating oil 913) quase
certamente também são captura parcial e não devem ser lidos como sinal de "sessão de
baixa convicção" até serem confirmados (ou revisados) na próxima geração do dump.
Da mesma forma, os preços de fechamento de hoje (soja 1.199,50, farelo 319,00, óleo
72,64) foram tratados nesta leitura como definitivos, seguindo a mesma convenção da
leitura de ontem ("números do dump como fonte da verdade"), mas a experiência de
ontem-para-hoje mostra que isso é uma aproximação sujeita a revisão — a vela de
rejeição descrita na soja e no óleo hoje precisa ser reconfirmada amanhã.

**2. Continuidade da revisão de preços entre gerações do dump — desta vez modesta.**
O dump de hoje atribui à data de 15/07/2026 valores de farelo (318,90 USD/sht),
óleo (72,92 cts/lb) e soja (1.202,25 cts/bu) fechamento ligeiramente diferentes dos
usados na leitura publicada nesse mesmo dia (318,20, 72,58 e 1.195,00,
respectivamente) — uma revisão de +0,2% a +0,6% em cada perna, bem mais modesta do
que a revisão documentada entre as leituras de 13-14/07 (que chegou a inverter o
sinal do ratio Far/Soj e do nível técnico do óleo). Isso é consistente com uma
correção normal de settlement (fechamento oficial vs. captura intradiária), não com
uma anomalia de fonte — mas reforça que qualquer número do "dia corrente" citado
nesta série de leituras deve ser lido como preliminar até a geração seguinte do
dump confirmá-lo.

**3. O prêmio de exportação de farelo em Paranaguá (+0,05 USD/sht) e o de óleo
(+0,08 cts/lb) estão no mesmo valor exato desde pelo menos 03/07/2026** (NAG, agora
duas semanas sem variação de nenhum centavo) — não é possível distinguir, só com os
dados disponíveis, se isso reflete um mercado de exportação genuinamente parado ou um
valor que não está sendo atualizado de fato na fonte.

**4. A manchete específica de notícias para 16/07/2026 não aparece no dump** — o
contador mostra "160 itens lidos, 8 mantidos (soja/farelo/oleo)", o maior número de
itens mantidos em várias leituras recentes, mas nenhuma linha de headline para a data
de hoje foi capturada nesta geração, o mesmo padrão de lacuna já registrado na
leitura de ontem (que também não tinha manchete de 15/07, mas hoje o dump já mostra a
manchete retroativa de 15/07 — sugerindo que a manchete específica aparece com um dia
de atraso na captura). Não há como confirmar qual foi a notícia mais relevante de
hoje segundo o próprio sistema.

**5. O WASDE segue cobrindo apenas farelo (Argentina, Brasil, China parcial), sem
nenhum dado de soja em grão ou óleo de soja, em qualquer geografia, e sem nenhum dado
dos Estados Unidos** — sem atualização desde 10/07/2026. A pergunta central sobre
"oferta grande de soja" segue sem canal de resposta interno.

**6. NOPA (fila `release-nopa-2026-07-16`) segue com `monthly_status` em 0,0 bool** —
mesma barreira de assinatura paga documentada desde meados de junho, agora com mais de
um mês sem alternativa de dado primário sobre o esmagamento americano.

**7. Percentis históricos de COT não calculados** — os números de 07/07/2026 (sem
atualização há 9 dias, atualização esperada amanhã) são lidos apenas em nível
absoluto e como fração do open interest corrente, sem série histórica completa para
calibrar zona extrema.

**8. Palma malaia (MPOB) segue sem números extraídos** (16/07/2026, mesmo texto de
HTML sem valores) — impossível avaliar o efeito do El Niño ou das restrições
indonésias sobre o prêmio de substituição do óleo de soja.

**9. O câmbio (PTAX) usado no cálculo de paridade de hoje ainda é o de 15/07/2026**
(5,0727 BRL/USD) — o BCB não havia publicado o PTAX de 16/07 no momento da coleta
deste briefing, então a paridade teórica de hoje mistura o preço CBOT de hoje com o
câmbio de ontem; a comparação pareada com o físico (item central da seção Soja) usou
datas idênticas (15/07 nos dois lados) para evitar esse viés.

**10. Clima INMET (BR) não foi usado como driver desta leitura.** Julho é entressafra
da soja brasileira (colheita concluída, plantio só em outubro) — sem relevância
direta para a tese de preço neste momento do calendário agrícola, embora o El Niño
Advisory (NOAA CPC, inalterado) permaneça relevante para a expectativa da safra de
plantio de outubro/26 e para o clima do Sudeste Asiático (palma).

**11. BCBA Argentina — sem relatórios de esmagamento/exportação acessíveis via
scraper** (page_fetched=1,0 mas sem links de relatório, 16/07/2026, sem mudança).

**12. RIN D4 como parâmetro fixo (2,11 USD/RIN) segue sendo uma fonte relevante de
incerteza do modelo de biodiesel**, sem novo dado hoje — a queda de -10,0% na margem
foi atribuída ao heating oil, mas o RIN fixo nunca é testado contra um valor real de
mercado neste sistema; se o RIN de mercado estiver, na realidade, diferente de 2,11,
tanto a margem quanto o ISO podem estar mal calibrados.

*Nenhum número foi inventado ou estimado além do que consta no briefing de 16/07/2026
e nos insights anteriores referenciados. A contribuição central desta leitura foi
confirmar, com um exemplo concreto e quantificado (volume de farelo revisado de 932
para 25.461 contratos, 27x), que os dados do "dia corrente" neste sistema são
sistematicamente preliminares e sujeitos a revisão material no dia seguinte — o que
recomenda tratar qualquer leitura de vela/volume do próprio dia de publicação com
cautela redobrada, e revisitá-la explicitamente no dia seguinte antes de tratá-la
como definitiva.*
