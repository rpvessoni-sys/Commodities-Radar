---
data: 2026-07-17
titulo: "O dump de hoje revisa o fechamento de farelo e heating oil de ontem (319,00→322,90 e 3,8425→4,0307) e isso reverte o ratio Far/Soj de 79,78% (abaixo de 80%, gatilho bear confirmado) para 81,06% (acima de 80%, gatilho invalidado) — o gatilho tático do farelo perde a 'quarta confirmação orgânica' anunciada ontem e reseta a zero, mesmo com o pilar estrutural (crush margin em novo topo de 3,18 USD/bu, ISF 80/100 intacto) mais forte que nunca; a soja rompe a mínima da consolidação de 4 dias com uma vela sem pavio (abriu na máxima, fechou na mínima, 1.187,75) mas ainda acima do suporte-chave 1.180,00; e o óleo é a perna mais forte do dia, subindo com oil share e crush share em alta — só que os volumes de hoje (1.087 a 3.244 contratos, ante ~40 mil típicos) são de novo uma fração do normal, então toda leitura de vela de hoje precisa ser tratada como preliminar"
tags: [complexo, auto-claude]
fontes:
  - CBOT CME (ZSQ26/ZMQ26/ZLQ26 + curva forward completa + HO=F) — sessão de 2026-07-17 (volumes baixos — ver Honestidade)
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, ISF/ISO, paridade BR) — 2026-07-17, com série revisada de 2026-07-13 a 2026-07-17
  - BCB PTAX — último dado 2026-07-16 (USD/BRL 5,0975), reutilizado no cálculo de paridade de hoje (defasagem de 1 dia, mesmo padrão de dias anteriores)
  - CEPEA/ESALQ Paranaguá e Paraná interior via NAG — último dado 2026-07-16 (suporte Paranaguá R$ 140,58/saca, Paraná interior R$ 133,94/saca)
  - NAG Físico BR (farelo MT/IMEA, RS, Rondonópolis; prêmios export PGUA farelo/óleo) — último dado 2026-07-16
  - CFTC COT Managed Money — dado de referência ainda 2026-07-07, SEM atualização apesar de hoje (sexta-feira, 17/07) ser o dia normal de publicação — ver Honestidade e Riscos
  - USDA Crop Progress — último dado 2026-07-12 (65% bom-ou-melhor), sem atualização; próximo relatório normal ~2026-07-20 (segunda-feira)
  - USDA WASDE — ainda 2026-07-10 (só farelo Argentina/Brasil/China parcial), sem publicação nova
  - NOPA — 2026-07-17, `monthly_status` continua inacessível (paywall), fila `release-nopa-2026-07-17`
  - ABIOVE projeções mensais — balanços ago-dez/2026 (farelo/óleo/soja), sem alteração frente às leituras anteriores
  - NOAA CPC ENSO — 2026-07-17 (El Niño Advisory, sem mudança)
  - MPOB — 2026-07-17 (parser sem números extraídos, streak de ~2 semanas nesta janela de dados)
  - BCBA — 2026-07-17 (acessível, sem links de relatório detectados)
  - Notícias Agrícolas / Canal Rural RSS — 2026-07-17 (160 itens lidos, 7 mantidos; manchete "Estudo projeta mais 1,4 milhão de hectares desmatados sem Moratória da Soja", Canal Rural)
  - Forecasts estatísticos internos — 2026-07-17 (recalibrados; as seis bandas — 3 commodities × 2 horizontes — seguem em viés altista pela segunda leitura seguida)
  - system/tributario_watch.toml — MP-1358-2026 (vigência formal encerrada há 6 dias, status ainda "tramitação"), PISCOFINS-BIODIESEL-ISENCAO (vence em 14 dias), MP-1363-2026, STJ-RESP-2165276, B16-CNPE-2026, EPA-RFS-2026-2027, 45Z-CLEAN-FUEL, DANANTARA-INDONESIA, INDONESIA-B50, INDONESIA-LEVY-PMK9 — todos `atualizado_em` 2026-06-05 (42 dias sem atualização do monitor)
  - Cruza com [[2026-07-16_leitura-complexo]], [[2026-07-15_leitura-complexo]], [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (checkpoint D+7, hoje resetado — ver Farelo), [[2026-05-26_subvencao-fossil-aperta-biodiesel]], [[2026-05-26_pis-cofins-biodiesel-explica-mercado-fisico-fraco]]
status: ativa
vies: [bear-soja, bear-farelo, bull-oleo_soja]
---

## Visão geral

O complexo soja é uma fábrica com uma única matéria-prima (a soja em grão) e dois
produtos de saída em proporção fixa por bushel esmagado: o **farelo** (fração
proteica, ~78% da massa, vira ração animal) e o **óleo degomado** (fração de
gordura, ~18-20% da massa, vira óleo de cozinha e biodiesel). Quem decide o ritmo
de esmagamento é a esmagadora, olhando a **crush margin** (valor de farelo + óleo
por bushel, menos o custo daquele bushel de soja, medido na CBOT — Chicago Board
of Trade) e o **oil share** (fração desse valor capturada pelo óleo). Hoje, sexta-
feira 17/07/2026, a crush margin fechou em 3,1804 USD/bushel (indicadores, farelo
319,20 + óleo 73,05 − soja 1.187,75), o **maior valor de toda a janela de 5 dias
visível neste dump** (3,0211 em 13/07 → 3,0193 em 14/07 → 3,0145 em 15/07 → 3,1211
em 16/07, revisado → 3,1804 hoje) — a esmagadora segue com forte incentivo
econômico a rodar a pleno vapor, e esse incentivo está, na verdade, **crescendo**,
não estabilizado como pareceu nas últimas leituras.

**O que mudou hoje foi, antes de qualquer preço, a descoberta de que os próprios
números de ontem (16/07) usados na leitura publicada naquele dia estavam errados —
e não por uma margem pequena.** O dump de hoje traz o fechamento de 16/07 já
"assentado" (definitivo, com volume de 43.934 contratos no farelo, coerente com um
pregão normal) e ele é MATERIALMENTE diferente do que a leitura de 16/07 registrou
com os dados então disponíveis (capturados no mesmo dia, com volume de apenas
1.304 contratos, uma fração óbvia do normal). O farelo de 16/07 sai de US$
319,00/sht (usado ontem) para US$ 322,90/sht (revisado hoje, +1,22%); a soja sai
de 1.199,50 cts/bu para 1.195,00 cts/bu (−0,375%); e o heating oil (proxy de
receita do biodiesel) sai de US$ 3,8425/galão para US$ 4,0307/galão — uma revisão
de **+4,90%**, a maior já documentada nesta série de leituras. **A consequência
direta: o ratio Far/Soj de 16/07, que a leitura de ontem fechou em 79,78% (a
"quarta sessão consecutiva abaixo de 80%", tratada como confirmação orgânica e
limpa do gatilho tático da tese de 11/06/2026), na verdade fechou em 81,06% —
ACIMA do limiar de 80%, invalidando a confirmação anunciada ontem.** E a margem de
biodiesel americano de 16/07, que ontem foi lida como uma queda de −10,0% (a
segunda queda de dois dígitos em dois pregões seguidos, acumulando −20,0% em dois
dias e soando um alarme sobre o Índice de Suporte do Óleo), na verdade **subiu**
para US$ 0,9635/galão (revisado) — o maior valor da janela de 5 dias, não o menor.
Toda a narrativa de "óleo perdendo tração" e "farelo confirmado bear pela quarta
vez" construída na leitura de ontem foi montada sobre números que a própria
geração seguinte do sistema revisou de forma direcionalmente relevante. Isso é
tratado em profundidade na seção Farelo e na Honestidade, mas precisa estar no
topo desta leitura porque muda o que "confiar em uma vela do dia da publicação"
significa para todo o sistema.

**Com essa ressalva pesando sobre qualquer leitura de curtíssimo prazo, os preços
de hoje (17/07/2026, ainda preliminares — volumes de apenas 1.087 a 3.244
contratos, quando o padrão final costuma rodar acima de 40 mil) mostram um
complexo em clara divergência interna.** A **soja** fechou em 1.187,75 cts/bu, com
uma vela sem pavio em nenhuma ponta (abriu em 1.195,00, foi exatamente até 1.199,50
— a máxima do dia, e coincidentemente quase idêntica ao fechamento revisado de
ontem —, caiu até 1.187,00, e fechou em 1.187,75, a 6% do fundo do range): um
rompimento claro para baixo da consolidação de quatro dias (1.192,75-1.205,50),
ainda que 0,66% acima do suporte estrutural de 1.180,00. Trata
`alerta-quebra_resistencia-soja_cbot-2026-07-17`. O **farelo** teve a vela mais
limpa (e mais fraca) da semana: abriu exatamente na máxima (322,90) e fechou
exatamente na mínima (319,20), uma queda monotônica sem qualquer tentativa de
recuperação intradiária, −1,15% no dia. O **óleo**, ao contrário dos outros dois,
subiu: fechou em 73,05 cts/lb, acima da abertura (72,62) e bem longe da mínima
(72,43), fechando a 59% do topo do range — o dia mais forte das três pernas,
puxando o oil share de volta para 53,36% (de 52,86% revisado ontem) e reforçando o
Índice de Suporte do Óleo (ISO), que segue intacto em 100/100. **Leitura de uma
linha:** o pivô do complexo hoje não é mais "qual nível técnico vai romper", é "quão
preliminares são estes números" — a soja rompeu a consolidação para baixo mas ainda
não tocou o suporte-chave, o farelo perdeu o gatilho tático que sustentava a
convicção moderada-alta de ontem (volta à estaca zero, precisando reconstruir a
sequência abaixo de 80%) mas ganhou o pilar estrutural mais forte já visto (crush
margin em novo topo), e o óleo é hoje a tese mais limpa e menos contestada do
complexo — convicção moderada em todas as três pernas, com a confirmação do COT
(que deveria ter saído hoje e não saiu) como o próximo evento a realmente testar
quem está certo.

---

## Soja

**Viés: bear tático (baixa-moderada convicção, rebaixado de neutro em 16/07) —
fechou em 1.187,75 cts/bu (17/07/2026), rompendo para baixo a consolidação de
quatro dias (mínimas entre 1.192,75 e 1.205,50 desde 13/07), com uma vela sem
pavio em nenhuma ponta (abriu na máxima do dia, 1.195,00→1.199,50, fechou na
mínima, 1.187,00→1.187,75). Ainda 0,66% acima do suporte estrutural de 1.180,00.
Trata `alerta-quebra_resistencia-soja_cbot-2026-07-17`.**

### O que sustenta a tese

**A vela de hoje é a mais fraca da semana, tecnicamente falando.** Fechamento de
1.187,75 cts/bu (CBOT, 17/07/2026), abertura em 1.195,00, máxima de exatamente
1.199,50 (que é, por coincidência ou não, quase idêntica ao fechamento revisado de
16/07, 1.195,00 — uma leitura possível é que o mercado testou a região do
fechamento anterior e foi vendido ali) e mínima de 1.187,00. O fechamento (1.187,75)
está a apenas 0,75 ponto acima da mínima do dia, sobre um range total de 12,50
pontos — ou seja, 94% do movimento do dia terminou perto do fundo. Isso é
tecnicamente mais fraco do que a "vela de rejeição" já documentada em 16/07
(abriu perto da máxima, fechou perto da mínima, mas ainda dentro do range dos
dias anteriores): hoje o preço efetivamente **rompeu** a mínima de todo o range de
consolidação dos últimos quatro pregões (a mínima mais baixa do período, 1.192,75
em 14/07, foi rompida com folga).

**Olhando os cinco últimos fechamentos em sequência — 1.196,75 (13/07) → 1.192,75
(14/07) → 1.202,25 (15/07, revisado) → 1.195,00 (16/07, revisado — não mais
1.199,50 como registrado ontem) → 1.187,75 (hoje)** — o padrão que era de
consolidação lateral (teste dos dois extremos sem direção) agora tem uma
resolução: dois fechamentos seguidos em queda (1.202,25 → 1.195,00 → 1.187,75),
com o de hoje rompendo abaixo de toda a banda anterior. O rompimento de alta de
06-07/07 (que levou o preço de ~1.180,00 para a faixa de 1.190-1.205) não está
formalmente invalidado — nenhum fechamento voltou a testar 1.180,00 — mas a
distância de segurança encolheu de 1,65% (fechamento de 16/07 sobre 1.180,00) para
apenas 0,66% hoje. Um novo fechamento no mesmo ritmo da queda de hoje (−0,65%)
testaria diretamente o suporte.

**O USDA Crop Progress permanece sem atualização desde 12/07/2026** (65% da
lavoura americana em condição boa-ou-excelente, 12% excelente + 53% boa, 6% em
condição ruim; USDA Crop Progress via briefing) — o próximo relatório semanal
normal deve sair na segunda-feira, 20/07/2026 (dados "as of" domingo 19/07). Sem
dado novo, o argumento de oferta americana confortável permanece congelado, nem
reforçando nem enfraquecendo a tese de hoje.

**A curva forward mudou de formato frente a ontem, mas de forma sutil.** Agosto/26
(Q26, spot) 1.187,75 → Setembro/26 (U26) 1.178,25 (desconto de −9,50, ligeiramente
menor que o desconto de −10,50 documentado ontem e anteontem — a pressão sazonal
de pré-colheita segue presente, mas um pouco menos acentuada) → Novembro/26 (X26)
1.187,75 (recupera +9,50 sobre setembro, e — coincidência notável — fecha
EXATAMENTE no mesmo valor do spot de hoje) → Janeiro/27 (F27) 1.202,25 (+14,50) →
Março/27 (H27) 1.206,25 (+4,00). O formato de "sorriso" (desconto no meio,
prêmio na ponta longa) permanece intacto e a magnitude é quase idêntica à de
ontem — a curva não está descontando uma queda estrutural maior, só acompanhando
o spot para baixo em paralelo.

**A paridade teórica em reais caiu para R$ 133,48/saca 60kg** (indicadores,
17/07/2026: CBOT 1.187,75 cts × PTAX 5,0975 USD/BRL, sem basis) — o câmbio usado
ainda é o de 16/07/2026 (o BCB ainda não havia publicado o PTAX de hoje no momento
da coleta, o mesmo padrão de defasagem de um dia já documentado em leituras
anteriores). Fazendo a comparação pareada por data (16/07/2026 dos dois lados, a
única data com dado físico e paridade teórica disponíveis simultaneamente):
paridade teórica de 16/07 em R$ 134,29/saca (CBOT 1.195,00 revisado × PTAX 5,0975)
versus o físico de Paranaguá do mesmo dia (R$ 140,58/saca, CEPEA/ESALQ via NAG,
16/07/2026) — um prêmio de R$ 6,29/saca (+4,68%) do físico sobre a paridade
teórica. Esse prêmio **subiu** frente ao prêmio pareado de 15/07 documentado
ontem (R$ 5,54/saca, +4,1%) — uma leitura ligeiramente mais bullish para a demanda
física de exportação no porto do que a de ontem, e o terceiro valor de uma série
que vai de +5,4% (14/07) → +4,1% (15/07) → +4,68% (16/07, revisado): oscila, mas
sem uma tendência de compressão limpa. O preço físico do Paraná interior (via NAG)
fechou em R$ 133,94/saca (16/07/2026), um desconto de R$ 6,64/saca frente ao
suporte de Paranaguá — o spread logístico normal de frete até o porto, estável
frente aos R$ 6,85/saca de 15/07.

**O posicionamento dos fundos (COT, CFTC) permanece no dado de referência de
07/07/2026 — e, de forma relevante, NÃO foi atualizado hoje, apesar de
17/07/2026 (sexta-feira) ser o dia normal de publicação semanal.** Managed money
net long em +69.579 contratos (7,13% do open interest de 975.954), sem mudança.
Isso significa que o teste mais esperado desta semana — se a compra dos fundos
sobreviveu à consolidação de 13-16/07 e à quebra de hoje — segue pendente; ver
Honestidade e Riscos para o detalhamento de por que essa ausência importa mais do
que uma simples "sem atualização".

**Os forecasts estatísticos internos (17/07/2026)** seguem com viés altista: central
7d = 1.217,90 cts/bu (bandas 1.168,09-1.267,71); central 30d = 1.323,99 cts/bu
(bandas 1.220,88-1.427,11) — ambos ligeiramente abaixo dos centrais de ontem
(1.226,82 e 1.327,14), a primeira desaceleração do viés altista do modelo desde
que ele virou simultaneamente altista nas seis bandas do sistema em 16/07. Como já
registrado em leituras anteriores, esse modelo é puramente estatístico (média
móvel de 20 dias + volatilidade + inclinação recente) e reage a momentum de preço
passado — ainda não incorporou plenamente a vela de rompimento de hoje, então a
desaceleração de hoje deve ser lida como um primeiro eco fraco da fraqueza de
preço recente, não como uma mudança de regime do modelo.

**A notícia de hoje (Canal Rural, 17/07/2026) — "Estudo projeta mais 1,4 milhão de
hectares desmatados sem Moratória da Soja"** — não é um driver de preço de curto
prazo, mas é relevante para o risco regulatório de médio prazo: a Moratória da
Soja é o acordo setorial que sustenta o acesso da soja brasileira a mercados com
exigência de rastreabilidade ambiental (como a UE, via EUDR — regulação europeia
de desmatamento). Um estudo que quantifica o custo de abandonar a moratória
reforça a pressão para mantê-la, o que é neutro a levemente construtivo para o
acesso de exportação de longo prazo, mas não muda a leitura de preço de hoje.

### O que invalida / risco para a soja

- **Um fechamento abaixo de 1.187,00 (mínima de hoje) ou de 1.180,00** confirmaria
  a reversão do rompimento de 06-07/07 — a distância até o suporte estrutural
  encolheu para 0,66%, a menor desde que o nível foi rompido.
- **O COT (que deveria ter saído hoje) mostrar, quando finalmente publicado, que o
  managed money vendeu durante a consolidação e a quebra de hoje** — a ausência do
  dado é, ela mesma, um risco de cauda: o mercado pode reagir com atraso quando o
  número sair, concentrando movimento num único pregão.
- **Novas leituras de Crop Progress (esperadas ~20/07) mostrarem melhora
  continuada** — a leitura de 12/07 já mostrou +1pp; uma sequência de melhoras
  reduziria progressivamente o argumento de "oferta apertada".
- **O prêmio físico de Paranaguá reverter a subida recente** — passou de +4,1%
  (15/07) para +4,68% (16/07, pareado); uma reversão sinalizaria enfraquecimento da
  demanda de exportação que, por ora, ainda sustenta algum piso para o físico
  mesmo com o papel em queda.
- **Os números de hoje serem revisados amanhã na mesma magnitude do que ocorreu
  entre 16/07 e hoje** — dado o precedente de farelo (+1,22%) e heating oil
  (+4,90%) revisados de um dia para o outro, não há garantia de que o fechamento
  de 1.187,75 da soja hoje seja o valor final.

### Leitura operacional — soja

O viés foi rebaixado de neutro para bear tático: o rompimento de hoje é o
primeiro fechamento fora da banda de consolidação de quatro dias, com uma vela
sem qualquer tentativa de recuperação intradiária. Para quem está comprado
taticamente (inclusive contra o rompimento de 06-07/07), a referência de stop
lógica é 1.180,00 — um fechamento abaixo desse nível confirmaria reversão
completa do movimento de alta de início de julho. Para quem está vendido, o
suporte de 1.180,00 é o alvo natural de curto prazo, mas vale lembrar que o
volume de hoje (2.182 contratos) é uma fração do volume final típico (documentado
em dias anteriores na casa de 40 mil+), então perseguir o rompimento de hoje com
tamanho de posição pleno é mais arriscado do que o padrão técnico sugere à
primeira vista — o precedente de revisão de farelo e heating oil de ontem-para-
hoje é um alerta direto sobre confiar demais numa vela do dia da publicação. O
evento mais importante para resolver essa incerteza é a publicação (ainda
pendente) do COT.

---

## Farelo

**Viés: bear (estrutural intacto, tático RESETADO — não mais "confirmado pela
quarta vez", mas de volta à espera de um novo fechamento abaixo de 80%). O ratio
Far/Soj de hoje fechou em 80,62% (indicadores, 17/07/2026: farelo 319,20 ÷ soja
1.187,75, mesma base) — ainda ACIMA do limiar de 80%, a segunda sessão seguida
nessa condição depois que a revisão do fechamento de 16/07 (79,78%→81,06%)
invalidou a "quarta confirmação orgânica" anunciada na leitura de ontem. Trata
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` (RESET, ver
abaixo) e `release-nopa-2026-07-17` (sem dado novo).**

### O que sustenta a tese

**O achado mais importante desta leitura para o farelo é o que a revisão de dados
mudou na contagem do gatilho tático.** A leitura de ontem (16/07) fechou o dia
celebrando a "quarta sessão consecutiva abaixo de 80%" no ratio Far/Soj, com a
confirmação de 16/07 (79,78%) descrita como a primeira "limpa" da sequência —
gerada organicamente no dia, sem depender de revisão retroativa como a
confirmação anterior. O dump de hoje mostra que essa leitura estava apoiada em
dados que a própria geração seguinte do sistema revisou: o fechamento de farelo
de 16/07 passou de US$ 319,00/sht para US$ 322,90/sht (+1,22%) e o de soja passou
de 1.199,50 para 1.195,00 cts/bu (−0,375%) — juntos, isso move o ratio de 79,78%
para **81,06%**, cruzando de volta para cima do limiar de 80%. Refazendo a
contagem com os números que o sistema hoje trata como definitivos: **79,52%
(13/07) → 79,83% (14/07) → 79,58% (15/07) → 81,06% (16/07, revisado) → 80,62%
(hoje)** — três sessões abaixo de 80%, seguidas por DUAS sessões acima. O gatilho
tático da tese de 11/06/2026 não está confirmado; está, na melhor leitura,
pausado a 0,62 ponto percentual acima do limiar, e precisa de um novo fechamento
abaixo de 80% para reabrir a contagem.

**Ainda assim, a trajetória dentro dessas duas sessões acima de 80% é de
compressão, não de fuga do gatilho:** o ratio caiu de 81,06% (16/07) para 80,62%
(hoje), uma queda de 0,44 ponto em um dia. Se esse ritmo se mantiver, o ratio
cruzaria de volta para baixo de 80% já na próxima ou na segunda sessão seguinte —
o que sustenta a leitura de que a tese de compressão do spread farelo/soja
continua estruturalmente viva, só que partindo de uma base mais alta do que se
pensava ontem, e com a contagem do gatilho tático reiniciada, não avançada.

**A crush margin fechou em 3,1804 USD/bushel** (indicadores, 17/07/2026: farelo
319,20 + óleo 73,05 − soja 1.187,75) — o **maior valor de toda a janela visível
neste dump**, superando inclusive o 3,1211 revisado de 16/07. Esse é o dado mais
robusto para a tese estrutural do farelo, porque não depende de revisão de série
nem de qual perna do complexo caiu mais rápido: quanto maior a crush margin, maior
o incentivo da esmagadora a processar soja a pleno vapor, e mais farelo
(subproduto obrigatório do esmagamento) entra no mercado. Com a crush margin
subindo justamente nos dois dias em que o ratio tático saiu da zona "abundante", o
pilar estrutural do farelo está, na verdade, mais forte hoje do que estava na
leitura de ontem — mesmo com o gatilho tático resetado.

**A trajetória projetada da ABIOVE (Associação Brasileira das Indústrias de Óleos
Vegetais, projeções mensais, sem alteração) segue sendo o pilar mais sólido do
argumento estrutural, porque não depende do preço do dia.** A exportação de
farelo brasileiro projetada cai de 1.400 mil toneladas em agosto/2026 para 700 mil
toneladas em dezembro/2026 (queda de 50% em 4 meses), enquanto a produção cai de
forma bem mais suave (2.285,06 → 1.659,04 mil toneladas no mesmo período, −27%) e
o estoque final oscila sem tendência clara entre 1.000 e 1.224 mil toneladas ao
longo de todo o semestre (ABIOVE projeções mensais, sem atualização desde as
últimas leituras). O mecanismo de transmissão é direto: menos farelo saindo pelo
porto, com produção caindo bem menos que a exportação, empurra o volume excedente
para o mercado interno de ração, pressionando o preço doméstico.

**As praças físicas de farelo no Brasil (NAG) mostram um sinal de enfraquecimento
concreto em Rondonópolis/MT.** No último dado, 16/07/2026: Mato Grosso/IMEA R$
1.577,34/ton (inalterado), Rondonópolis/MT R$ 1.600,00/ton (queda de −4,19% frente
a R$ 1.670,00 em 15/07 — o maior movimento de um dia em qualquer praça física
documentado nas últimas leituras), Rio Grande do Sul R$ 1.640,00/ton (inalterado).
A queda em Rondonópolis, um polo de esmagamento relevante em Mato Grosso, é
coerente com o mecanismo estrutural ABIOVE: mais farelo sendo produzido
localmente do que o mercado de exportação consegue absorver, pressionando o preço
onde o produto está mais concentrado. O prêmio de exportação em Paranaguá segue em
+0,05 USD/short_ton (julho/26, NAG, inalterado desde pelo menos 03/07/2026, agora
13 dias sem variação) — como já registrado em leituras anteriores, essa constância
pode refletir um mercado de exportação genuinamente parado (reforçando a absorção
doméstica) ou uma fonte que não está sendo atualizada de fato (ver Honestidade).

**O Índice de Sobra de Farelo (ISF) permanece em 80/100 (4 de 5 condições
estruturais)** (indicadores, 17/07/2026) — inalterado nas cinco sessões visíveis
neste dump (13 a 17/07) e, segundo leituras anteriores, desde pelo menos
01/07/2026. É o índice mais estável de toda a leitura e o único que não foi
tocado pela revisão de dados que abalou o ratio tático e a margem de biodiesel —
porque o ISF é calculado sobre condições estruturais (ABIOVE, crush, oferta), não
sobre a vela do dia.

**Tratando `release-nopa-2026-07-17`:** o NOPA (National Oilseed Processors
Association, dado mensal de esmagamento americano) segue com `monthly_status` em
0,0 bool — a mesma barreira de assinatura paga documentada desde meados de junho.
O item aparece de novo na fila como "release" do dia, mas não há nenhuma
informação nova para interpretar; não há confirmação direta do ritmo de
esmagamento americano por fonte primária.

**O oil-meal spread (óleo menos farelo, por bushel) subiu para 1,0131 USD/bu**
(indicadores, 17/07/2026), de 0,8635 (16/07, revisado) — uma alta de +17,3% no
dia, o maior movimento de um dia documentado nesta série, coerente com o óleo
tendo a vela mais forte das três pernas hoje enquanto o farelo teve a mais fraca
(abriu na máxima, fechou na mínima). Isso reforça, por um ângulo diferente do
ratio, a mesma divergência farelo-fraco/óleo-forte que caracteriza o dia de hoje.

**O forecast estatístico do farelo (17/07/2026)** segue com viés altista: central
7d = 326,25 USD/sht (bandas 313,49-339,01); central 30d = 351,61 USD/sht (bandas
325,19-378,03) — o modelo estatístico (que reage a momentum de preço recente, não
a fundamentos) segue na direção oposta à tese fundamentalista ABIOVE + ratio,
mesmo com o preço de hoje em queda — porque o modelo ainda está ancorado na
recuperação de preço em USD/sht desde a mínima de 293 documentada em junho, e
reage com atraso a uma única sessão de queda.

### O que invalida / risco para o farelo

- **A tese estrutural ABIOVE não se confirmar no físico ao longo do 2S/26** —
  ainda que a queda de Rondonópolis hoje seja um primeiro sinal físico a favor.
- **O ratio não voltar a fechar abaixo de 80% nos próximos pregões** — a contagem
  foi resetada por causa da revisão, e o ratio de hoje (80,62%) precisa de apenas
  0,62 ponto de queda adicional para reabrir o gatilho, mas até lá a tese tática
  permanece tecnicamente neutra.
- **NOPA seguir inacessível indefinidamente**, sem confirmação do esmagamento
  americano para os checkpoints D+90 (09/09/2026) e D+180 (08/12/2026).
- **O prêmio de exportação Paranaguá "congelado" em 0,05 USD/sht ser, na verdade,
  um dado sem atualização de fonte, não um preço de mercado real** (ver
  Honestidade).
- **O padrão de revisão material dump-a-dump se repetir com os números de hoje** —
  dado que o fechamento de farelo de 16/07 foi revisado em +1,22% e o de heating
  oil em +4,90% de uma geração do dump para a seguinte, o fechamento de hoje
  (319,20) e o próprio ratio de hoje (80,62%) devem ser tratados como sujeitos a
  revisão até a próxima geração confirmar.

### Leitura operacional — farelo

A tese estrutural (ABIOVE, ISF 80/100, crush margin em novo topo) está, se
qualquer coisa, mais forte hoje do que ontem. Mas o gatilho TÁTICO — o ratio
fechando abaixo de 80% — perdeu a confirmação que sustentava a convicção
moderada-alta anunciada ontem, e voltou à condição de "aproximando-se por cima",
não "confirmado". Para quem opera o spread de convergência (long farelo tático
não recomendado; a tese é vendida em farelo relativo à soja, ou o crush completo),
a postura recomendada hoje é a mesma de antes da "confirmação" de ontem: aguardar
um novo fechamento limpo abaixo de 80% antes de tratar o gatilho tático como
disparado, apoiando o dimensionamento da posição no pilar estrutural (ABIOVE, ISF)
mais do que na leitura de curto prazo do ratio. Para quem prefere o veículo mais
robusto — o spread farelo/soja ou o crush completo, em vez de direcional puro — o
argumento para esse veículo ficou mais forte hoje, não mais fraco: exatamente
porque a leitura tática provou ser instável entre gerações do dump, apostar no
mecanismo estrutural (que não depende do fechamento do dia) é a forma mais
defensável de expressar a tese.

---

## Óleo

**Viés: bull moderado (a perna mais limpa do complexo hoje) — fechou em 73,05
cts/lb (17/07/2026), subindo da abertura (72,62) e fechando a 59% do topo do
range do dia (mínima 72,43, máxima 73,45), a vela mais construtiva das três
pernas. O oil share voltou a 53,36% (de 52,86% revisado ontem) e o Índice de
Suporte do Óleo (ISO) segue em 100/100.**

### O que sustenta a tese

**O óleo fechou hoje em 73,05 cts/lb** (CBOT, 17/07/2026), com abertura em 72,62
(perto da mínima do dia, 72,43) e máxima de 73,45 — o preço subiu praticamente a
sessão inteira, devolvendo só uma fração do ganho até o fechamento (73,05 contra
máxima de 73,45, retração de apenas 39% do movimento de alta). Comparado ao
fechamento revisado de 16/07 (72,43, não mais 72,64 como registrado ontem — ver
Honestidade), a alta de hoje é de +0,86%. É o oposto da assinatura técnica da
soja e do farelo hoje (que abriram perto da máxima e fecharam perto da mínima):
o óleo é a única das três pernas com uma vela genuinamente construtiva na sessão
de hoje.

**A curva forward mantém backwardation limpa, de magnitude muito próxima à de
ontem**: Agosto/26 (Q26, spot) 73,05 → Setembro/26 (U26) 72,37 (−0,68) →
Outubro/26 (V26) 71,62 (−0,75) → Dezembro/26 (Z26) 71,15 (−0,47) → Janeiro/27
(F27) 70,87 (−0,28) — uma queda de −2,18 cts/lb (−2,98%) de agosto a janeiro/27,
praticamente idêntica à queda de −2,17 cts/lb (−3,0%) documentada ontem (com os
valores de ontem antes da revisão). Esse formato (prêmio no vencimento mais
próximo, desconto nos mais distantes) reflete demanda física presente forte
(biodiesel americano + exportação brasileira) frente a uma expectativa de oferta
mais confortável adiante — a estabilidade da magnitude da backwardation, mesmo
com o spot subindo hoje, é um sinal de que o mercado não está simplesmente
extrapolando o movimento de um dia para a curva inteira.

**A margem de biodiesel americano fechou em 0,8186 USD/galão** (indicadores,
17/07/2026: receita 7,0974 = HO/heating oil 3,9324 + 1,5×RIN 2,11; custo 6,2788 =
óleo 5,4788 + industrial 0,80), uma queda de −15,0% frente ao valor revisado de
16/07 (0,9635) — mas essa comparação precisa ser lida com cuidado: o valor de
16/07 usado ontem na leitura (0,7595) já estava errado por causa da captura
parcial do heating oil (3,8425 contra o valor final de 4,0307). Olhando a série
corrigida — 0,7271 (13/07) → 0,9493 (14/07) → 0,8443 (15/07) → 0,9635 (16/07,
revisado) → 0,8186 (hoje) — a margem de hoje está no meio da faixa observada nos
últimos cinco pregões, não em trajetória de colapso como a leitura de ontem
sugeriu. Ainda dentro (ou muito perto do teto) da faixa histórica de conforto de
0,50-0,80 USD/galão documentada em leituras anteriores como a zona onde
compradores voluntários de blending, acima do mandato B15, costumam atuar — hoje
a margem está ligeiramente acima desse teto, o que é, se algo, um sinal levemente
positivo para o incentivo de blending, não negativo.

**O Índice de Suporte do Óleo (ISO) permanece em 100/100 (5 de 5 condições)**
(indicadores, 17/07/2026) — o mesmo patamar máximo em todas as cinco sessões
visíveis neste dump (13 a 17/07) e, segundo leituras anteriores, desde pelo menos
01/07/2026. Diferente do que a leitura de ontem temia (que a margem em suposta
queda acentuada pudesse eventualmente derrubar uma das cinco condições do ISO), a
correção dos dados mostra que a margem nunca esteve de fato em colapso — o índice
permanece robusto porque o fundamento que ele mede também é robusto.

**O oil share (fração do valor do crush capturada pelo óleo) está em 53,36%**
(indicadores, 17/07/2026), subindo dos 52,86% revisados de 16/07 e recuperando o
patamar de 53,24-53,44% observado em 13-15/07 — seguindo folgadamente acima de
50%, confirmando que o óleo continua sendo o motor de valor do crush. A subida de
hoje é coerente com a alta do oil-meal spread (+17,3% no dia, ver seção Spreads):
o óleo capturou proporcionalmente mais valor do crush hoje do que em qualquer dia
da janela recente.

**O forecast estatístico do óleo (17/07/2026) reforça o viés altista**: central 7d
= 74,17 cts/lb (bandas 69,77-78,58); central 30d = 78,69 cts/lb (bandas
69,58-87,81) — ambos acima dos centrais de ontem (73,43 e 76,79), a segunda
leitura seguida em que as seis bandas de forecast do sistema (soja, farelo e
óleo, 7d e 30d) fecham simultaneamente em viés altista. Diferente da soja e do
farelo, onde o preço de hoje caiu enquanto o modelo estatístico ainda reflete o
momentum recente de alta (uma divergência), no óleo o preço subiu hoje e o modelo
também subiu — os dois sinais, pela primeira vez em vários dias, apontam na mesma
direção dentro dessa perna específica.

### O que invalida / risco para o óleo

- **Um fechamento abaixo de 71,62 (o vencimento de outubro na curva de hoje)**
  reabriria o cenário bear tático — não ocorreu hoje, e a vela de hoje é
  claramente construtiva, mas o padrão de reversão rápida já visto em outras
  pernas do complexo nesta semana não pode ser descartado.
- **A margem de biodiesel (0,8186 USD/gal) reverter para baixo de forma
  consistente** — mesmo com a correção mostrando que a série não estava em
  colapso, uma queda real e sustentada (não apenas um artefato de captura
  parcial) ainda testaria o ISO.
- **O heating oil (proxy de receita do biodiesel) reverter a recuperação de
  16/07** — o valor revisado de 16/07 (4,0307) foi o pico da janela; o fechamento
  de hoje (3,9324) já é uma retração de −2,4% frente a esse pico, e uma sequência
  de quedas voltaria a pressionar a margem.
- **A divergência entre a força de hoje no óleo e a fraqueza na soja e no farelo
  não se sustentar** — se amanhã o óleo seguir o resto do complexo para baixo, a
  leitura bull de hoje perde força rapidamente.
- **MPOB seguir inacessível** — impossível avaliar o efeito do El Niño ou das
  restrições/levy indonésias (PMK 9/2026, Danantara — ver Lente fiscal) sobre o
  prêmio de substituição via palma.

### Leitura operacional — óleo

O óleo é hoje a tese mais limpa do complexo: vela construtiva, backwardation
estável, oil share em alta, ISO no máximo, e forecast estatístico e preço andando
na mesma direção pela primeira vez em dias. Para quem opera exposição relativa ao
óleo dentro do crush, os pilares estruturais seguem intactos e reforçados pela
divergência de hoje frente a farelo e soja. Para quem opera direcional puro em
óleo, a vela de hoje é o primeiro argumento tático limpo (sem a contradição
estrutura-vs-momentum que caracterizou a leitura de ontem) desde a reversão de
15/07 — mas, como em toda leitura desta série, o volume de hoje (3.244 contratos)
é uma fração do volume final típico, então o tamanho da posição deve refletir essa
incerteza. O oil-meal spread (óleo menos farelo) segue sendo o veículo mais direto
para capturar a divergência entre as duas pernas, e hoje esse spread deu o maior
salto de um dia (+17,3%) de toda a série — o veículo que mais limpo capturou o
dia de hoje.

---

## Spreads e crush — leitura de complexo

### Crush margin: 3,1804 USD/bu — novo topo da janela, sem sinal de arrefecimento

A crush subiu pelo segundo dia seguido e atingiu o maior valor visível nesta série
(3,0211 em 13/07 → 3,0193 em 14/07 → 3,0145 em 15/07 → 3,1211 em 16/07, revisado →
3,1804 hoje). O incentivo de esmagamento a pleno vapor não só permanece intacto
como está se fortalecendo, alimentando o mecanismo estrutural ABIOVE
independentemente de qual perna do complexo está subindo ou caindo no dia.

### Ratio Far/Soj: 80,62% — RESETADO pela revisão, segunda sessão acima de 80% mas em queda

O achado central desta leitura: a revisão do fechamento de 16/07 (farelo
319,00→322,90, soja 1.199,50→1.195,00) moveu o ratio daquele dia de 79,78% (abaixo
do limiar, tratado ontem como "quarta confirmação orgânica") para 81,06% (acima do
limiar). A sequência corrigida é 79,52% (13/07) → 79,83% (14/07) → 79,58% (15/07)
→ 81,06% (16/07, revisado) → 80,62% (hoje) — três sessões abaixo de 80%, seguidas
por duas acima, com o ratio de hoje ainda caindo (−0,44 ponto frente a ontem).
Trata `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`: o
gatilho tático está TECNICAMENTE RESETADO, não confirmado — precisa de um novo
fechamento abaixo de 80% para reabrir a contagem, embora a trajetória de queda
dentro dos últimos dois dias sustente que isso pode ocorrer em breve.

### Oil share: 53,36% — recuperou o patamar de 13-15/07

Subiu de 52,86% (16/07, revisado) para 53,36% hoje, voltando à faixa de 53,24-
53,44% observada em 13-15/07 — o óleo capturando de volta uma fatia maior do valor
do crush, coerente com sua vela mais forte do dia.

### Oil-meal spread: 1,0131 USD/bu — maior alta de um dia da série (+17,3%)

Subiu de 0,8635 (16/07, revisado) para 1,0131 USD/bu hoje — mede o valor do óleo
menos o valor do farelo por bushel; a alta de hoje é o maior movimento de um dia
documentado nesta série, capturando de forma direta a divergência entre o óleo
(vela forte) e o farelo (vela fraca, abriu na máxima e fechou na mínima) na mesma
sessão.

### ISF em 80/100, ISO em 100/100 — os dois índices que a revisão NÃO tocou

O Índice de Sobra de Farelo (ISF, 4/5 condições) e o Índice de Suporte do Óleo
(ISO, 5/5 condições) permanecem inalterados em todas as cinco sessões visíveis
neste dump (13 a 17/07) e, segundo leituras anteriores, desde pelo menos
01/07/2026 (indicadores, 17/07/2026). É um contraste relevante: enquanto o ratio
tático e a margem de biodiesel se mostraram sujeitos a revisões materiais entre
gerações do dump, os dois índices estruturais — calculados sobre condições mais
amplas (ABIOVE, crush, oferta), não sobre o fechamento pontual do dia — não
oscilaram nem uma vez.

### O que os índices dizem juntos em 17/07/2026

ISF 80/100 + ISO 100/100 (ambos estáveis, imunes à revisão de preço) + ratio
Far/Soj resetado para 80,62% (acima do limiar, mas caindo) + oil share em alta
(53,36%) + crush margin em novo topo da janela (3,1804) + oil-meal spread com a
maior alta de um dia da série (+17,3%) formam um quadro em que a divergência
farelo-fraco/óleo-forte, que já vinha sendo documentada, se aprofunda — mas agora
com uma camada extra de cautela: o episódio de revisão de dados de hoje mostra que
qualquer leitura tática construída sobre o fechamento do dia de publicação precisa
ser tratada como provisória até a geração seguinte do dump confirmar. O complexo
segue esmagando a pleno vapor (crush em novo topo), o que garante fluxo constante
de farelo (reforçando a tese estrutural bear) e de óleo (sem sinal de escassez
física) simultaneamente — só que hoje o mercado está precificando essas duas
saídas de forma visivelmente diferente.

---

## Lente fiscal e regulatória BR

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L) — a
vigência formal (`vigencia_ate` 11/07/2026) venceu há 6 dias, e o monitor
tributário segue sem qualquer atualização de status** (system/tributario_watch.toml,
evento MP-1358-2026, `atualizado_em` 2026-06-05, status ainda "tramitacao",
`proximo_marco` = "Deliberação comissão mista", `proximo_data` = 2026-07-11, já
vencida há 6 dias). São agora seis dias úteis (13, 14, 15, 16 e 17/07, mais o fim
de semana anterior) desde o vencimento formal sem nenhuma fonte pública rastreada
pelo sistema (ABIOVE, NAG, notícias) confirmar se a MP caducou, foi prorrogada por
novo decreto, ou foi convertida em lei. O mecanismo de transmissão para o complexo
permanece o mesmo já documentado: enquanto o combustível fóssil segue subsidiado,
a competitividade relativa do biodiesel dentro do mix B15 mandatório fica
pressionada, mantendo a margem da indústria de biodiesel mais apertada do que sem
a subvenção ao concorrente fóssil.

**Isenção PIS/Cofins biodiesel — vencimento em 31/07/2026, agora a 14 dias.** Sem
sinalização pública de renovação até hoje (evento PISCOFINS-BIODIESEL-ISENCAO,
`atualizado_em` 2026-06-05, sem mudança). Continua sendo o próximo relógio fiscal
mais próximo a vigiar, à frente da própria definição da MP 1.358.

**B16 — sem data, travado em B15.** Sem mudança de status (evento B16-CNPE-2026,
`atualizado_em` 2026-06-05, status "adiado", sem `proximo_data`). Testes técnicos
do FNDCT com resultado esperado ~nov/2026 — realista só fim de 2026/início de
2027, segundo mecanismo já documentado.

**MP 1.363/2026 (subsídio ao diesel fóssil, R$ 1,12/L) — em vigor até
31/12/2026.** Sem alteração. Bearish estrutural persistente para a demanda
incremental de óleo de soja no mercado doméstico brasileiro.

**STJ REsp 2.165.276/2026 — crédito PIS/Cofins para esmagadoras.** Sem alteração.
Bullish para soja/óleo (alívio de custo de entrada para biodiesel) e, por
extensão, incentivo a mais esmagamento — coerente com a crush margin em novo topo
documentada hoje.

**Vetores dos EUA e Indonésia, revisitados (sem mudança de status, `atualizado_em`
2026-06-05 em todos):** EPA-RFS-2026-2027 (volumes recordes de biocombustível,
BBD 8,86→9,07 bi RINs, sustentando estruturalmente o RIN D4 e o óleo CBOT); 45Z-
CLEAN-FUEL (regra proposta que tiraria insumo importado da elegibilidade ao
crédito, favorecendo óleo de soja doméstico americano e empurrando sebo
brasileiro de volta ao mercado interno, aliviando insumo do biodiesel BR);
DANANTARA-INDONESIA (centralização estatal da exportação de palma desde 01/06,
assunção plena da cadeia alvo em 01/09/2026 — risco de menor saldo exportável de
palma, suporte ao óleo de soja por substituição); INDONESIA-B50 (retórica
agressiva mas quota flat, capacidade insuficiente — provável B45 em 2026, B50
pleno só 2027-28); INDONESIA-LEVY-PMK9 (imposto de exportação de CPO até 12,5%
desde 01/03, encarecendo palma e favorecendo substituição por óleo de soja). Todos
esses vetores seguem, em conjunto, num sentido estruturalmente bullish para o
óleo de soja via substituição de palma — coerente com o viés bull de hoje na
seção Óleo, ainda que nenhum tenha gerado um evento novo nesta data específica.

**O monitor tributário como um todo está há 42 dias sem qualquer atualização**
(`atualizado_em` 2026-06-05 em todos os dez eventos rastreados) — um dia a mais
que ontem, e o intervalo cresce em um momento em que dois vetores (MP 1.358 e a
isenção PIS/Cofins) têm datas de vencimento formal já vencida ou a apenas 14 dias.
Vale sinalizar este ponto como prioridade de manutenção do sistema,
independentemente da leitura de preço.

---

## Riscos e eventos próximos

**COT (CFTC) — deveria ter sido publicado hoje, 17/07/2026 (sexta-feira), e NÃO
apareceu no dump.** Este é o item de maior prioridade para a próxima leitura: ou o
dado ainda vai sair mais tarde no dia (atraso de coleta) ou algo interrompeu a
publicação regular da CFTC. Até ser confirmado, o teste mais esperado desta semana
— se o managed money manteve a compra em soja/farelo/óleo durante a consolidação
de 13-16/07 e a quebra de hoje na soja — segue pendente.

**Confirmar se os preços e volumes de hoje (17/07) sofrem revisão na mesma
magnitude identificada entre as gerações de 16/07 e 17/07 do dump.** É o segundo
item mais urgente: farelo (+1,22%) e heating oil (+4,90%) foram revisados de
16/07 para hoje, e essa não é a primeira vez (o farelo de 15/07 já havia sido
revisado em volume 27x na leitura de ontem). Se o padrão se repetir, o fechamento
de hoje (soja 1.187,75, farelo 319,20, óleo 73,05) e o ratio Far/Soj de hoje
(80,62%) podem não ser os números finais — inclusive podendo reverter de novo o
sinal do gatilho tático do farelo.

**Desfecho da MP 1.358/2026 — vigência formal encerrada há 6 dias, sem
confirmação.** Monitorar deliberação da comissão mista e qualquer decreto de
prorrogação.

**Isenção PIS/Cofins biodiesel — vencimento 31/07/2026 (14 dias).** Sem
sinalização de renovação até agora.

**Próxima leitura de USDA Crop Progress — esperada ~20/07/2026 (segunda-feira),
dados "as of" 19/07.** Sem atualização desde 12/07.

**NOPA — segue inacessível** (fila `release-nopa-2026-07-17` tratada aqui, sem
dado interpretável), sem crush americano confirmado por fonte primária.

**MPOB — sem números de palma extraídos**, mantendo cego o efeito do El Niño e dos
vetores regulatórios indonésios (Danantara, B50, levy PMK 9) sobre o prêmio de
substituição do óleo de soja.

**O suporte de 1.180,00 na soja está a apenas 0,66% do fechamento de hoje** — a
menor distância desde que o nível foi rompido em 06-07/07. Um novo fechamento no
mesmo ritmo da queda de hoje testaria diretamente esse nível.

**Checkpoints futuros da tese estrutural do farelo (ABIOVE)** — D+90 em
09/09/2026 e D+180 em 08/12/2026 (insight
[[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]) — o gatilho tático
segue vivo, mas hoje precisou ser formalmente resetado por causa da revisão de
dados; os checkpoints estruturais (ABIOVE) permanecem o critério de mais alta
confiança para julgar a tese ao longo do tempo.

**Padrão sistêmico de revisão de dados dump-a-dump** — esta é agora a segunda
leitura seguida (16/07 e 17/07) em que uma descoberta de revisão material altera
a interpretação do dia anterior. Recomenda-se que qualquer leitura futura desta
série trate o fechamento e os índices do próprio dia de publicação como
preliminares por padrão, não como exceção.

---

## Honestidade

O que não foi possível validar neste briefing de 17/07/2026, onde a confiança é
baixa ou há lacunas materiais:

**1. A descoberta mais importante desta leitura: o fechamento de farelo, soja e
heating oil de 16/07 foram revisados entre a geração de ontem do dump e a de
hoje, e a revisão foi direcionalmente relevante, não apenas de magnitude.** O
farelo de 16/07 saiu de US$ 319,00/sht (usado na leitura de ontem) para US$
322,90/sht (+1,22%); a soja saiu de 1.199,50 para 1.195,00 cts/bu (−0,375%); e o
heating oil saiu de US$ 3,8425/galão para US$ 4,0307/galão (+4,90%, a maior
revisão percentual já documentada nesta série). Isso não é apenas uma correção de
volume (como o caso de farelo 932→25.461 contratos documentado em 16/07) — desta
vez são os PREÇOS DE FECHAMENTO que mudaram o suficiente para inverter dois sinais
interpretativos inteiros: o ratio Far/Soj de 16/07 vai de 79,78% (abaixo de 80%,
gatilho bear confirmado) para 81,06% (acima de 80%, gatilho invalidado), e a
margem de biodiesel de 16/07 vai de 0,7595 USD/gal (leitura de "segunda queda de
dois dígitos seguida, −20% em dois dias") para 0,9635 USD/gal (na verdade o maior
valor da janela). A leitura de ontem não estava errada por falta de cuidado — ela
seguiu a convenção estabelecida de tratar os números do dump como fonte da
verdade — mas o episódio confirma, pela segunda vez em dois dias, que essa
convenção tem um custo real de interpretação. Os números de HOJE (soja 1.187,75,
farelo 319,20, óleo 73,05, heating oil 3,9324, ratio 80,62%) foram tratados nesta
leitura com a mesma convenção, mas devem ser lidos com a mesma reserva.

**2. Os volumes de hoje continuam sendo uma fração óbvia do padrão final.** Soja
2.182 contratos, farelo 1.087, óleo 3.244, heating oil 1.618 — todos
substancialmente abaixo do padrão final observado quando uma sessão já está
assentada (por exemplo, farelo em 16/07, revisado, fechou com 43.934 contratos, e
heating oil no mesmo dia com 43.513). Isso reforça a leitura do item 1: as velas
"sem pavio" da soja e do farelo hoje, embora tecnicamente limpas, foram
construídas sobre uma fração do volume que normalmente define o fechamento oficial
do dia.

**3. O COT (CFTC), esperado hoje, não apareceu no dump.** A seção `cftc_cot`
segue com o mesmo dado de referência de 07/07/2026, sem nenhuma linha nova
datada de hoje. Não é possível determinar, só com os dados disponíveis, se isso é
um atraso de coleta (o dado pode sair mais tarde no dia) ou uma falha na fonte —
mas é a ausência de dado mais impactante desta leitura, porque o COT era o evento
mais citado nas últimas três leituras como o próximo teste real da tese.

**4. O prêmio de exportação de farelo em Paranaguá (+0,05 USD/sht) e o de óleo
(+0,08 cts/lb) estão no mesmo valor exato desde pelo menos 03/07/2026** (NAG,
agora 13 dias sem variação de nenhum centavo) — não é possível distinguir, só com
os dados disponíveis, se isso reflete um mercado de exportação genuinamente
parado ou um valor que não está sendo atualizado de fato na fonte.

**5. O WASDE segue cobrindo apenas farelo (Argentina, Brasil, China parcial), sem
nenhum dado de soja em grão ou óleo de soja, em qualquer geografia, e sem nenhum
dado dos Estados Unidos** — sem atualização desde 10/07/2026. A pergunta central
sobre "oferta grande de soja" segue sem canal de resposta interno.

**6. NOPA (fila `release-nopa-2026-07-17`) segue com `monthly_status` em 0,0
bool** — mesma barreira de assinatura paga documentada desde meados de junho,
agora com mais de um mês sem alternativa de dado primário sobre o esmagamento
americano.

**7. Percentis históricos de COT não calculados** — os números de 07/07/2026 (sem
atualização há 10 dias, e sem a atualização esperada de hoje, ver item 3) são
lidos apenas em nível absoluto e como fração do open interest corrente, sem série
histórica completa para calibrar zona extrema.

**8. Palma malaia (MPOB) segue sem números extraídos** (17/07/2026, mesmo texto de
HTML sem valores) — impossível avaliar o efeito do El Niño ou dos vetores
regulatórios indonésios (Danantara, B50, levy PMK 9 — ver Lente fiscal) sobre o
prêmio de substituição do óleo de soja.

**9. O câmbio (PTAX) usado no cálculo de paridade de hoje ainda é o de
16/07/2026** (5,0975 BRL/USD) — o BCB não havia publicado o PTAX de 17/07 no
momento da coleta deste briefing, então a paridade teórica de hoje mistura o preço
CBOT de hoje com o câmbio de ontem; a comparação pareada com o físico (item
central da seção Soja) usou datas idênticas (16/07 nos dois lados) para evitar
esse viés.

**10. Clima INMET (BR) não foi usado como driver desta leitura.** Julho é
entressafra da soja brasileira (colheita concluída, plantio só em outubro) — sem
relevância direta para a tese de preço neste momento do calendário agrícola,
embora o El Niño Advisory (NOAA CPC, inalterado desde pelo menos 03/07/2026)
permaneça relevante para a expectativa da safra de plantio de outubro/26 e para o
clima do Sudeste Asiático (palma).

**11. BCBA Argentina — sem relatórios de esmagamento/exportação acessíveis via
scraper** (page_fetched=1,0 mas sem links de relatório, 17/07/2026, sem mudança).

**12. RIN D4 como parâmetro fixo (2,11 USD/RIN) segue sendo uma fonte relevante de
incerteza do modelo de biodiesel**, sem novo dado hoje — a margem de hoje (0,8186)
e a de 16/07 (revisada, 0,9635) foram ambas calculadas com esse valor fixo; se o
RIN de mercado estiver, na realidade, diferente de 2,11, tanto a margem quanto o
ISO podem estar mal calibrados, independentemente do episódio de revisão de preço
documentado nesta leitura.

**13. A manchete de notícias de hoje (desmatamento/Moratória da Soja, Canal
Rural) é a única manchete específica de soja capturada no dump de 17/07** — o
contador mostra "160 itens lidos, 7 mantidos", mas sem visibilidade sobre o que
foram os outros 6 itens mantidos além da manchete listada, nem sobre farelo ou
óleo especificamente.

*Nenhum número foi inventado ou estimado além do que consta no briefing de
17/07/2026 e nos insights anteriores referenciados. A contribuição central desta
leitura foi identificar, pela segunda vez em dois dias, uma revisão material de
dados entre gerações do dump — desta vez atingindo diretamente os preços de
fechamento (farelo e heating oil), não apenas o volume — e mostrar, com números
concretos, como essa revisão inverteu dois sinais interpretativos inteiros
(o gatilho tático do ratio Far/Soj e a leitura de tendência da margem de
biodiesel). A recomendação prática permanece a mesma de ontem, agora reforçada:
tratar qualquer leitura de vela, volume ou índice do próprio dia de publicação
como preliminar por padrão, e revisitá-la explicitamente no dia seguinte antes de
tratá-la como definitiva.*
