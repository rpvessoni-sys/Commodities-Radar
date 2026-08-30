---
data: 2026-08-30
titulo: "Fim de semana sem pregão novo: a tese de sexta (soja rompida em 1.288,00, farelo em 342,50, óleo ainda preso abaixo de 72,00) segue intacta porque nada a invalidou — mas o dado do próprio fechamento de 28/08 mudou pela TERCEIRA noite seguida, e o catalisador Danantara da Indonésia chega em menos de 48h, ainda sem confirmação de execução"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT (ZSX26 soja / ZMV26 farelo / ZLV26 óleo) — última sessão disponível, 2026-08-28 (sexta-feira; sábado e domingo não têm pregão): soja abertura 1.270,00, máxima 1.290,00, mínima 1.269,25, fechamento 1.288,00 USD cts/bushel, volume 162.537 contratos; farelo abertura 333,10, máxima 345,70, mínima 331,40, fechamento 342,50 USD/short ton, volume 43.217 contratos; óleo abertura 69,12, máxima 71,08, mínima 68,93, fechamento 70,82 USD cts/lb, volume 64.978 contratos
  - CME CBOT — sessão de 2026-08-27, presente no dump só para farelo (fechamento 334,40 USD/sht, volume 59.717 — nesta base 43.217, ver nota) e heating oil (fechamento 4,2787 USD/galão); os fechamentos de soja (1.268,00) e óleo (68,23) de 27/08 usados nesta leitura vêm reconstruídos via `indicators` (crush margin), não de uma linha própria de CBOT
  - CME NYMEX heating oil (HO=F) — 2026-08-28 fechamento 4,3567 USD/galão
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, paridade BR, ISF, ISO) — série 2026-08-21 a 2026-08-29 (indicadores estruturais ISF/ISO têm um carimbo de 29/08 repetindo o valor de 28/08, sem pregão novo para recalcular)
  - BCB PTAX — série 2026-08-17 a 2026-08-28, USD/BRL fechou em 5,2005 (28/08, última cotação disponível; PTAX não publica fim de semana)
  - CEPEA/ESALQ Soja Paranaguá via NAG — série 2026-08-20 a 2026-08-28, fechou em R$ 159,76/saca (28/08, var. +3,04%)
  - CEPEA/ESALQ Soja Paraná interior via NAG — série 2026-08-24 a 2026-08-28, fechou em R$ 151,32/saca (28/08, var. +1,41%)
  - NAG Físico BR — série 2026-08-24 a 2026-08-28: farelo MT/IMEA R$ 1.795,68/ton (28/08, +4,03% no dia), Rondonópolis/MT R$ 1.870,00/ton (estável desde 26/08), RS média R$ 1.860,00/ton (estável); prêmios export PGUA farelo +0,12 USD/short ton e óleo +0,10 cts/lb, ambos congelados nos mesmos valores desde 24/08 (5 sessões seguidas sem mover, mesmo com o board em alta forte — ver Honestidade)
  - CFTC COT Managed Money, Swap Dealers e Producer/Merchant — corte de 2026-08-25, ainda o mais recente disponível (nenhum corte novo no fim de semana; o próximo, refletindo posições de terça 01/09, só deve sair por volta de sexta 04/09 pelo calendário semanal do CFTC — inferência, não confirmada no briefing)
  - USDA Crop Progress — corte de 2026-08-23 (12% excelente / 48% boa / 9% ruim), sem corte novo
  - USDA WASDE — segue ausente da janela deste briefing
  - NOPA — fila `release-nopa-2026-08-29`, `monthly_status` continua em 0,0 bool (paywall, sem mudança)
  - ABIOVE projeções mensais — balanços set-dez/2026, mesmos valores da leitura anterior
  - NOAA CPC ENSO — carimbo 2026-08-29 (El Niño Advisory, inalterado)
  - MPOB — carimbo 2026-08-29 (3.456 caracteres, parser sem números extraídos, mesma barreira)
  - INMET — previsão para 2026-08-30 (hoje): calor extremo e tempo seco no núcleo produtor de Mato Grosso (43°C em Cuiabá, 40°C em Sinop/Sorriso/Lucas do Rio Verde, poucas nuvens), 38°C em Rio Verde/GO; já no Sul, céu mais fechado e chuva — Passo Fundo/RS com máxima de só 19°C e mínima de 15°C sob pancadas e trovoadas, Cascavel/PR 32°C com pancadas e trovoadas, Maringá/PR 36°C com nuvens e pancadas isoladas
  - Notícias Agrícolas/Canal Rural RSS — "Soja sobe no Brasil e em Chicago; mercado apresenta ritmo na semana" (29/08, item novo neste dump, resumo semanal que confirma o rali sem acrescentar fato novo); "Novo episódio do Soja Brasil aborda decisão do STF, clima e desafios para a nova safra" (28/08, sem detalhe do teor da decisão — ver Honestidade)
  - Forecasts estatísticos internos (bandas 7d/30d, MA20+volatilidade+slope) — geração de 2026-08-29, alvos 05/09 (7d) e 28/09 (30d); viés "altista" em soja e farelo nos dois horizontes, óleo "lateral" no 7d e "altista" no 30d
  - system/tributario_watch.toml (lido como referência, não editado) — `atualizado_em` 2026-06-05 em todos os eventos, 86 dias sem revisão — ver Lente fiscal e Honestidade
  - Fila de julgamento — carimbada 2026-08-29 no briefing, 8 itens, TODOS já citados e substancialmente tratados na leitura anterior [[2026-08-29_leitura-complexo]]: `alerta-quebra_resistencia-soja_cbot-2026-08-28`, `alerta-quebra_suporte-oleo_cbot-2026-08-28`, `alerta-movimento_forte-oleo_cbot-2026-08-28`, `alerta-quebra_resistencia-farelo_cbot-2026-08-28`, `alerta-quebra_suporte-complexo_soja-2026-08-28`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, `trib-DANANTARA-INDONESIA-2026-09-01`, `release-nopa-2026-08-29` — nenhum item novo surgiu porque não houve pregão entre a leitura de ontem e esta (sábado/domingo)
  - Cruza com [[2026-08-29_leitura-complexo]] (leitura de sexta, cujos números de fechamento de 28/08 este briefing revisa outra vez — ver Honestidade) e com [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (tese original do ratio, já revisada ontem)
status: ativa
vies: [bull-soja, bull-farelo, neutral-oleo_soja]
---

## Visão geral

Hoje é domingo (30/08/2026) e não houve pregão desde a sexta-feira — CBOT não opera
sábado nem domingo, e por isso este briefing carrega os MESMOS fechamentos de 28/08 que
alimentaram a leitura de ontem, apenas revisados de novo (ver Honestidade). Isso muda o
tipo de análise que cabe fazer hoje: não é dia de procurar um fato novo de preço, é dia de
testar se a tese de sexta-feira ainda se sustenta sem contradição, e de olhar pra frente —
o que pode acontecer entre agora e a reabertura de segunda-feira (31/08).

Recapitulando o mecanismo pra quem não acompanha o dia a dia: o complexo soja é uma
cadeia de transformação. Compra-se soja em grão, "esmaga-se" (crush) numa esmagadora, e
saem dois produtos com destinos e dinâmicas de preço diferentes — farelo (proteína, vai
pra ração animal) e óleo (vai pra alimentação humana e, cada vez mais, pra biodiesel). O
crush margin é o que sobra pra esmagadora depois de vender farelo + óleo e pagar a soja;
ele fechou a sexta em **US$ 2,45/bushel** (indicators, 28/08, "Board Crush": farelo 342,50
+ óleo 70,82 − soja 1.288,00), ainda abaixo do referencial de US$ 2,50 que a fila monitora
(`alerta-quebra_suporte-complexo_soja-2026-08-28`), mas em recuperação clara nos últimos
três pregões (US$ 2,09 em 26/08 → US$ 2,18 em 27/08 → US$ 2,45 em 28/08, +17% em três
dias). Quem "manda" dentro desse crush — farelo ou óleo — está num empate técnico: o
**oil share** (fatia do óleo no valor total do crush) fechou em **50,83%** (indicators,
28/08), só ligeiramente acima da metade, mas também em leve tendência de alta (50,3% →
50,5% → 50,83% nos últimos três pregões). Os dois índices estruturais sintéticos internos
seguem nos extremos da régua: o **Índice de Suporte do Óleo (ISO)** trava em **100/100**
(5 de 5 condições favoráveis) e o **Índice de Sobra de Farelo (ISF)** trava em **80/100**
(4 de 5 condições apontando pressão baixista) — ambos sem mudar nem no carimbo de 29/08
do próprio indicador, porque não houve pregão novo pra recalcular nada.

O termômetro mais importante do complexo continua sendo o **ratio Far/Soj** — preço do
farelo relativo à soja, não em valor absoluto. Fechou em **79,77%** (indicators, 28/08),
ainda dentro da zona que o próprio sistema rotula "abundante" (<80%), mas subindo devagar
há quatro pregões seguidos (78,46% em 25/08 → 78,93% → 79,12% → 79,77% em 28/08). A leitura
que isso ensina não muda de sexta pra hoje: farelo está caro em valor absoluto (342,50
USD/sht) porque a soja está subindo mais rápido, não porque o farelo esteja isoladamente
escasso. É a soja que segue no comando do complexo.

O que muda hoje, numa frase, é justamente a AUSÊNCIA de mudança: nenhum dos gatilhos da
fila foi invalidado, nenhum nível técnico foi revisitado, e o único "evento" real do fim
de semana foi editorial — a StoneX/Canal Rural publicou um resumo semanal ("Soja sobe no
Brasil e em Chicago; mercado ganha ritmo na semana", 29/08) que só reafirma, sem
acrescentar fato novo, o que os números de sexta já mostravam. **Leitura de uma linha**:
o pivô do complexo continua sendo a soja, a maior convicção segue a mesma de ontem — o
rali tem fundo comprado novo entrando via CFTC —, e o nível de confiança cai de "médio"
para **médio-baixo** justamente por causa do gap temporal: são dois dias corridos a mais
sem confirmação de mercado (COT ainda de 25/08, agora cinco dias atrás; fechamento de
28/08 revisado pela terceira noite seguida), e o catalisador Danantara na Indonésia vence
em menos de 48 horas sem qualquer atualização do monitor tributário desde junho.

## Soja

**Viés: bull, moderadamente forte — tese herdada de sexta-feira, sem novo teste nem nova
confirmação porque não houve pregão.**

O que sustenta a tese:

- **Rompimento técnico que já teve três sessões pra consolidar.** Soja CBOT fechou em
  1.288,00 USD cts/bushel em 28/08/2026 (CME CBOT), 9,2% acima da resistência de 1.180,00
  que a fila de julgamento monitora (`alerta-quebra_resistencia-soja_cbot-2026-08-28`).
  Essa é a mesma leitura de ontem — o fato não mudou porque não há pregão novo — mas o
  peso dela aumenta com o tempo: quanto mais sessões o mercado passa sem devolver o
  rompimento, menor a chance de ele ter sido um "fakeout" técnico. A pergunta em aberto
  pra segunda-feira é se a abertura de 31/08 confirma o nível ou se o fim de semana trouxe
  alguma notícia (clima, China, política comercial) que ainda não está neste briefing.
- **Fundos com dinheiro novo, não só cobertura — mas essa foto está ficando velha.** O
  corte CFTC COT de 25/08/2026 (ainda o mais recente do briefing, agora 5 dias corridos
  atrás) mostrava managed money em soja com long de 239.335 contratos (vs 197.446 em
  18/08, +21,2%) e short de 38.656 (vs 45.664, -15,3%) — net long saltando 32,2% em uma
  semana, com o open interest total praticamente estável (972.531 vs 989.729, -1,7%). O
  mecanismo que sustenta a tese continua válido em teoria, mas o corte não enxerga NENHUMA
  das sessões do rali de 27-28/08 — a defasagem que já preocupava ontem só cresceu.
- **Câmbio ainda alinhado com o movimento, sem informação nova de fim de semana.** USD/BRL
  fechou 28/08 em 5,2005 (BCB PTAX), +0,70% frente a 27/08 (5,1642) — sem PTAX de sábado
  ou domingo pra atualizar. A paridade CBOT-implícita em saca (sem basis) está em R$
  147,67/saca (indicators, 28/08, usando CBOT 1.288,00 × USD/BRL 5,2005) — o câmbio segue
  reforçando o rali de dólar, não competindo com ele, mas essa leitura só será testada de
  novo na abertura de segunda.
- **Físico brasileiro pagando prêmio sobre a paridade — última leitura, ainda válida.** O
  preço à vista em Paranaguá (CEPEA/ESALQ via NAG) fechou 28/08 em R$ 159,76/saca, R$
  12,09/saca (~8,2%) acima da paridade CBOT-implícita (R$ 147,67) — basis físico positivo,
  sinal de mercado apertado no porto. O prêmio do porto sobre o interior (Paraná interior
  a R$ 151,32) está em R$ 8,44/saca (5,6%), o mesmo dado de ontem: sem pregão físico novo
  no fim de semana, não há como confirmar se esse aperto persiste na segunda.
- **Estoques brasileiros de soja seguem apertando estruturalmente rumo ao fim de 2026**
  nas projeções ABIOVE (sem atualização nesta janela): estoque final recuando de 5.720,8
  mil t (out/26) para 3.658,9 mil t (nov/26) e 1.889,9 mil t (dez/26) — calendário sazonal
  natural, mas alimenta o pano de fundo de oferta mais curta no fim de ano.
- **USDA Crop Progress ainda em 23/08** (12% excelente / 49% boa / 8% ruim na leitura mais
  recente, 16/08, comparado a 12%/48%/9% em 23/08): leve deterioração, sem corte novo no
  fim de semana pra confirmar se a tendência de piora continuou.

**O que invalida / risco:**

- O maior risco específico de HOJE é justamente o gap de fim de semana: qualquer notícia
  de sábado ou domingo sobre China, clima na Argentina/EUA ou política comercial que não
  esteja neste briefing pode gerar um gap de abertura na segunda que nenhum dos números
  acima captura. Trate a tese como "válida até prova em contrário na abertura de 31/08",
  não como testada hoje.
- O COT de 25/08 segue sem enxergar as sessões de 27-28/08; o próximo corte (posições de
  terça 01/09, esperado por volta de sexta 04/09 pelo calendário semanal do CFTC) é o
  primeiro que vai realmente mostrar se os fundos entraram comprados NO rali ou se
  ficaram de fora — cinco dias corridos de exposição a essa incerteza, não mais dois.
- Nível técnico a vigiar: qualquer fechamento de volta abaixo de 1.180 desfaz o
  rompimento.
- A decisão do STF mencionada na notícia de 28/08 ("Novo episódio do Soja Brasil aborda
  decisão do STF...") segue sem teor detalhado no briefing — é um risco de cauda não
  quantificável enquanto durar essa lacuna de informação.

**Leitura operacional:** sem pregão novo, não há ação a tomar hoje além de planejar a
reação à abertura de segunda. O rompimento tem 3+ sessões de consolidação e dois motores
(CBOT + câmbio) alinhados — não é dia de vender força preventivamente. Mas o hiato do COT
já passa de 5 dias corridos sem ver o rali: quem está comprado sem proteção deveria usar
o fim de semana pra decidir o nível de stop (por exemplo, 1.180) e o tamanho de posição
ANTES da abertura de segunda, não depois. Quem quer jogar contra o movimento segue sem
sinal técnico pra isso — nada nos dados aponta exaustão, só uma lacuna de confirmação.

## Farelo

**Viés: bull na fita, mas com estrutura contraditória por baixo — leitura herdada de
sexta, ainda não retestada.**

O que sustenta a tese (na fita):

- **Rompimento de resistência com volume.** Farelo CBOT fechou em 342,50 USD/short ton em
  28/08/2026, 5,4% acima da resistência de 325,00 (`alerta-quebra_resistencia-farelo_cbot-
  2026-08-28`), com alta de +2,42% no dia (vs 334,40 em 27/08) e volume de 43.217
  contratos.
- **Cobertura de posição vendida agressiva no CFTC (foto de 25/08, ainda a mais recente).**
  Managed money com short caindo de 46.003 para 33.662 contratos (-26,8% em uma semana)
  enquanto o long ficou praticamente parado (129.318 → 129.615, +0,2%) — assinatura de
  short covering, não de convicção compradora nova. Sem corte novo no fim de semana pra
  saber se essa cobertura já se esgotou ou se ainda tem munição.
- **Físico brasileiro reagindo, ainda que atrasado.** O farelo MT/IMEA (NAG) saltou de R$
  1.726,20/ton (congelado por 5 sessões) para R$ 1.795,68/ton em 28/08 (+4,03%), fechando
  parte do gap para Rondonópolis/MT (R$ 1.870,00) e RS média (R$ 1.860,00). Sem dado novo
  de fim de semana pra confirmar se o repasse continuou.

O que tensiona a tese (a estrutura por baixo, inalterada desde sexta):

- **O ratio Far/Soj segue na zona "abundante" (<80%).** Fechou em 79,77% em 28/08
  (indicators) — quarta sessão seguida de alta gradual (78,46% → 78,93% → 79,12% →
  79,77%), mas ainda abaixo do limiar de 80%. O farelo continua relativamente barato
  frente à soja, mesmo depois do rompimento técnico.
- **O ISF segue travado em 80/100**, inclusive no carimbo repetido de 29/08 (sem pregão
  novo pra recalcular) — o sistema não vê o quadro estrutural de oferta de farelo mudando.
- **Prêmio de exportação em Paranaguá congelado em +0,12 USD/short ton desde 24/08** — já
  são 5 sessões sem se mexer mesmo com o board em alta forte (mesmo padrão flagrado
  ontem, sem dado novo pra reavaliar).

**Revisão da fila `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`:**
esse item já foi tratado em profundidade na leitura de ontem
[[2026-08-29_leitura-complexo]] — conclusão que permanece válida hoje sem fato novo pra
mudá-la: a compressão do ratio Far/Soj (que a tese original de 11/06 previa em "1-2
semanas" e levou ~11 semanas) **se confirmou**, mas o mecanismo foi diferente do previsto
(farelo subiu em valor absoluto em vez de cair — CBOT saiu de ~303,60 USD/sht em 10/06
para 342,50 hoje, +12,8%). Status: revisada, sem encerrar — cita-se aqui de novo só para
manter o rastro do `id` na leitura do dia, não para reabrir a análise.

**O que invalida / risco:** o short de managed money já caiu 27% numa semana (foto de
25/08) — tem menos munição de cobertura sobrando, e o próximo corte (posições de 01/09)
é quem vai dizer se esse motor está se esgotando. Se o ratio Far/Soj voltar a CAIR (não
subir) na reabertura de segunda enquanto o preço absoluto segue alto, é sinal de que o
farelo está sendo carregado pela soja sem força própria — e qualquer correção na soja bate
desproporcionalmente nele.

**Leitura operacional:** nada muda em relação a ontem por falta de pregão novo. Para quem
opera o spread Far/Soj, a zona de acumulação (ratio comprimido, <80% há 5+ sessões) segue
válida para quem monta tese de reversão (long farelo / short soja), mas o precedente de
"1-2 semanas virou 72 dias" continua valendo como aviso contra apressar o timing.

## Óleo

**Viés: neutro — a divergência mais interessante do complexo hoje: ISO travado em 100 mas
a margem de biodiesel comprimindo pregão após pregão, sem mudança de fita porque não houve
pregão novo.**

O que sustenta o lado comprado:

- **Salto do dia (sexta) segue sendo o maior das três pernas.** Óleo CBOT fechou em 70,82
  USD cts/lb em 28/08/2026, alta de +3,79% frente aos 68,23 de 27/08
  (`alerta-movimento_forte-oleo_cbot-2026-08-28`) — mais que o dobro da alta percentual da
  soja (+1,58%).
- **ISO travado em 100/100**, sem uma única sessão de enfraquecimento na janela disponível
  — mas repare: o ISO é um índice de CONDIÇÕES estruturais (biodiesel positivo, RIN D4
  sustentado, heating oil firme, oil share saudável, momentum técnico), não do TAMANHO da
  margem. Ele pode continuar em 100 mesmo com a margem encolhendo, desde que ela continue
  positiva — que é exatamente o que está acontecendo (ver abaixo).
- **Catalisador regulatório agora a menos de 48 horas de distância.** A fila traz
  `trib-DANANTARA-INDONESIA-2026-09-01`: em 01/09/2026 (terça-feira, depois de amanhã), a
  Indonésia projeta completar a centralização da exportação de óleo de palma sob o fundo
  soberano Danantara (tributario_watch.toml, id `DANANTARA-INDONESIA`, atualizado
  05/06/2026, direção "alta" para óleo de soja). Mecanismo: menos ou mais burocrática a
  exportação do maior óleo vegetal do mundo em volume, mais espaço pro óleo de soja como
  substituto na demanda global. O evento está pertíssimo agora, mas o monitor segue com
  dado de 86 dias sem atualização — tratar como catalisador binário a confirmar, não como
  fato já precificado.
- **Levy de exportação da palma indonésia (até 12,5%, PMK 9/2026, id `INDONESIA-LEVY-
  PMK9`) segue vigente**, sustentando o óleo de soja por substituição de forma permanente,
  independente do desfecho da Danantara.

O que sustenta o lado vendido / cético:

- **Ainda abaixo do pivô técnico de 72,00.** O fechamento de 70,82 segue 1,6% abaixo do
  nível monitorado como suporte perdido (`alerta-quebra_suporte-oleo_cbot-2026-08-28`) —
  tecnicamente um repique dentro de uma estrutura ainda quebrada. A pergunta que só a
  reabertura de segunda responde: consolida acima de 72,00 (reversão real) ou devolve o
  ganho?
- **A margem de biodiesel americana está comprimindo há uma semana, mesmo com o ISO em
  100.** Série completa disponível no briefing: 1,6481 USD/galão (21/08) → 1,5882 (24/08)
  → 1,5313 (25/08) → 1,5678 (26/08) → 1,5264 (27/08) → **1,4102 (28/08)** — uma queda de
  14,4% em uma semana, com o maior tombo justamente no último pregão (-7,6% de 27 para
  28/08). O mecanismo: o CUSTO do óleo (insumo do biodiesel) sobe junto com o próprio
  rali do CBOT (+3,79% no dia), mais rápido do que a receita (heating oil + RIN),
  espremendo quem produz biodiesel. Essa é uma tensão real que o ISO — por ser binário
  ("a margem está positiva?", não "quanto ela vale?") — não capta: o óleo pode estar
  ficando estruturalmente mais caro pro biodiesel absorver, mesmo com todas as 5
  condições do ISO ainda tecnicamente "verdes". Vale vigiar se a compressão continua na
  próxima semana — margem ainda positiva (>US$ 1,40/galão) não é o mesmo que margem
  confortável.
- **COT de 25/08 (ainda sem atualização) mostrava fundos DIMINUINDO net long antes do
  próprio rali** — managed money com long caindo de 116.669 para 114.248 (-2,1%) e short
  subindo de 25.436 para 29.132 (+14,5%) entre 18/08 e 25/08, net long recuando 6,7%. É o
  oposto do padrão em soja. Cinco dias corridos sem atualização agora, a maior lacuna
  relativa das três pernas porque é justamente aqui que a foto pré-rali contradizia o
  movimento.
- **Prêmio de exportação em Paranaguá congelado em +0,10 cts/lb desde 24/08** — mesmo
  padrão de estagnação do farelo, sem dado novo no fim de semana.

**O que invalida / risco:** para o lado comprado, um fechamento de segunda de volta abaixo
de ~69 devolveria o repique. Para o lado vendido, se a compressão da margem de biodiesel
continuar no ritmo do último pregão (-7,6% em um dia), ela pode cruzar pra terreno mais
apertado nas próximas semanas e finalmente puxar o ISO pra baixo de 100 — o gatilho a
vigiar não é mais só heating oil ou RIN isoladamente, é a combinação custo-óleo × receita.
O evento Danantara em 01/09 é binário: qualquer sinal de atraso (o precedente do B50
indonésio, monitorado desde junho sem confirmação de execução plena — id
`INDONESIA-B50` — mostra que anúncios ambiciosos nem sempre viram fato no prazo) esfria o
efeito bullish esperado.

**Leitura operacional:** segue sendo a perna mais indefinida das três — e o fim de semana
não resolveu isso, só aproximou o catalisador Danantara. Quem está comprado tem a favor o
ISO no teto e o evento de terça; quem está vendido tem a favor o nível técnico não
reconquistado, o COT desatualizado mostrando fundos céticos, e agora também a margem de
biodiesel em compressão de uma semana inteira — um contraponto novo que a leitura de
ontem não tinha destrinchado com esse nível de detalhe. Ainda faz mais sentido tratar
óleo como parte do spread/crush do que como aposta direcional pura antes da reabertura.

## Spreads e crush (leitura de complexo)

Juntando as três leituras: o ratio Far/Soj em 79,77% (zona "abundante", <80%) e o oil
share em 50,83% dizem que, em termos relativos, a soja segue cara frente ao farelo, e o
crush está quase empatado entre farelo e óleo como fonte de receita — nenhum dos dois
domina folgadamente. Os dois índices sintéticos, porém, desenham um retrato mais
assimétrico: ISF em 80 (sobra estrutural de farelo) e ISO em 100 (domínio estrutural do
óleo) — o sistema "acredita" mais na tese de suporte ao óleo do que na tese de sobra do
farelo, mesmo que o oil share bruto não mostre essa assimetria com tanta clareza. A leitura
mais honesta de complexo hoje é a mesma de sexta, só que com um detalhe novo vindo da
seção Óleo: o crush margin em US$ 2,45/bushel está subindo (2,09 → 2,18 → 2,45 em três
pregões) porque farelo (+2,42%) e óleo (+3,79%) subiram mais, juntos, do que a soja
(+1,58%) — mas dentro desse óleo que "ajudou" o crush a subir, a margem de biodiesel
específica (que mede quanto sobra pro USINEIRO de biodiesel, não pro crushor de soja) está
comprimindo há uma semana. São duas margens diferentes reagindo de formas opostas ao
mesmo movimento de preço: o crush da esmagadora de soja melhora, a margem do produtor de
biodiesel piora — o mesmo rali de óleo que é bom pra quem vende a matéria-prima é custo
mais alto pra quem a transforma em combustível.

Para quem opera o spread Far/Soj: a compressão abaixo de 80% já dura pelo menos 6 sessões
(desde 24/08) sem reverter de forma consistente — o avanço de 78,46% para 79,77% nos
últimos 4 pregões é gradual, não um estouro, e o fim de semana não muda essa contagem
porque não há pregão pra somar dias. Trate como zona de acumulação para quem monta a tese
de reversão (farelo relativamente barato tende a se recuperar frente à soja), mas sem
timing definido — a experiência de junho (ver seção Farelo) prova que "esticado" pode
continuar esticado por meses. Para quem opera o crush diretamente: 2,45 está abaixo do
referencial histórico de 2,50 mas em recuperação de 3 dias — segue sendo zona neutra até
o próximo movimento direcional confirmar, e esse próximo movimento só pode vir na
reabertura de segunda.

## Lente fiscal/regulatoria BR

Antes de fechar qualquer tese de preço BR, os vetores tributários/regulatórios vivos que
pesam no complexo — todos do `system/tributario_watch.toml`, cujo carimbo mais recente
(`atualizado_em`) em TODOS os eventos é 2026-06-05, ou seja, **86 dias sem revisão** (mais
um dia desde a leitura de ontem, o hiato só cresce):

- **MP 1.363/2026** (id `MP-1363-2026`, subvenção diesel fóssil R$ 1,12/L, vigente até
  31/12/2026): barateia o diesel fóssil no mix B15, reduzindo a competitividade relativa
  do biodiesel e a demanda doméstica por óleo de soja — vetor de baixa para óleo, sem
  mudança de status.
- **B16 (id `B16-CNPE-2026`, elevação da mistura de biodiesel para 16%)** segue "adiado" —
  CNPE cancelado em maio, testes técnicos com resultado esperado só por volta de
  novembro/2026. Upside represado (~436 mil toneladas de óleo adicional), não corrente.
- **Isenção de PIS/Cofins do biodiesel na mistura** (id `PISCOFINS-BIODIESEL-ISENCAO`): o
  TOML registra vigência ATÉ 31/07/2026 — já **30 dias corridos vencida** frente aos
  30/08/2026 de hoje, sem qualquer registro de prorrogação ou expiração no arquivo. Segue
  sendo uma lacuna real de informação (ver Honestidade), não uma leitura de preço.
- **STJ REsp 2.165.276** (id `STJ-RESP-2165276`, crédito de PIS/Cofins sobre soja em
  biodiesel, vigente, direção "alta" para soja/óleo): alívio de custo pontual, não
  vinculante (não é repetitivo).
- **EPA RFS 2026/2027** (id `EPA-RFS-2026-2027`, mandato de biocombustível americano,
  vigente desde 15/06/2026, direção "alta" para óleo): volumes recordes de RINs sustentam
  a margem de biodiesel americana — mesmo que essa margem esteja comprimindo pregão a
  pregão nesta semana (ver seção Óleo), o mandato em si não mudou de status.
- **Crédito 45Z** (id `45Z-CLEAN-FUEL`, Clean Fuel Production, em tramitação, direção
  "mista"): se a regra final excluir insumo importado da elegibilidade, o óleo de soja
  DOMÉSTICO americano ganha, mas o sebo bovino brasileiro hoje exportado como insumo
  perderia esse mercado e voltaria pro blend doméstico — o que tira, na margem, demanda
  do óleo de soja DENTRO do Brasil. Vetor que pode virar contra o óleo de soja BR mesmo
  sendo favorável ao óleo de soja americano.
- **Indonésia — Danantara** (id `DANANTARA-INDONESIA`) e **levy de exportação PMK 9/2026**
  (id `INDONESIA-LEVY-PMK9`): já tratados na seção Óleo, ambos direção "alta" para óleo de
  soja via substituição de palma. Danantara agora a menos de 48h do marco-alvo.
- **Notícia de 28/08/2026** sobre uma decisão do STF segue sem teor detalhado no
  briefing, e não há nenhum evento STF cadastrado no `tributario_watch.toml` (só STJ) —
  não é possível avaliar o impacto com os dados disponíveis; fica como item para
  acompanhar, não para precificar.

## Riscos e eventos próximos

- **01/09/2026 (terça, depois de amanhã)** — marco-alvo da centralização plena da
  exportação de palma pela Danantara (Indonésia), `trib-DANANTARA-INDONESIA-2026-09-01`;
  vigiar se a assunção da cadeia se confirma no prazo ou escorrega, como já aconteceu com
  o B50 indonésio (`INDONESIA-B50`).
- **31/08/2026 (segunda)** — reabertura do CBOT depois do fim de semana; primeiro teste
  real da tese herdada de sexta-feira. Vigiar especialmente se soja segura 1.180, farelo
  segura 325 e se óleo consegue finalmente fechar acima de 72,00.
- **Próximo corte CFTC COT** — posições de terça 01/09, com publicação estimada por volta
  de sexta 04/09 pelo calendário semanal do CFTC (inferência, não confirmada no
  briefing): é o dado que revela se os fundos entraram comprados NAS sessões de rali
  (27-28/08) ou ficaram de fora.
- **NOPA mensal** (`release-nopa-2026-08-29`): segue atrás de paywall, sem confirmação do
  ritmo de esmagamento americano.
- **USDA WASDE**: ausente da janela há bastante tempo; qualquer publicação nova é
  catalisador potencial de revisão de balanço mundial.
- **Vigência da isenção PIS/Cofins do biodiesel** (TOML aponta 31/07/2026, agora 30 dias
  vencida sem confirmação de prorrogação) — checar notícia de renovação/expiração antes
  de assumir qualquer tese de custo do biodiesel BR.
- **Clima**: calor extremo e tempo seco em Mato Grosso (43°C em Cuiabá, INMET, previsão
  para hoje 30/08) contrasta com chuva no Sul (Passo Fundo/RS, Cascavel/PR) — relevante
  para a JANELA DE PLANTIO da safra 2026/27 que se aproxima (set/out); solo seco no
  núcleo produtor às vésperas do plantio é vetor a monitorar, ainda não problema
  confirmado de safra.
- **Margem de biodiesel americana em compressão de uma semana** (1,65 → 1,41 USD/galão,
  21/08 a 28/08) — se continuar no ritmo do último pregão, é o vetor mais próximo de
  derrubar o ISO de 100, o índice mais "unânime" do briefing até aqui.

## Honestidade

- **Terceira revisão retroativa consecutiva do fechamento de 28/08.** A leitura de ontem
  ([[2026-08-29_leitura-complexo]]) registrou soja 1.287,75 (vol. 153.472), farelo 342,70
  (vol. 46.745) e óleo 70,71 (vol. 57.670) para a sessão de 28/08. Este briefing, lido
  hoje, traz para a MESMA sessão soja 1.288,00 (vol. 162.537), farelo 342,50 (vol.
  43.217) e óleo 70,82 (vol. 64.978) — abertura, máxima e mínima idênticas, mas
  fechamento e volume revisados de novo, inclusive o volume mudando double-digit percent
  (46.745 → 43.217 no farelo, -7,5%; 57.670 → 64.978 no óleo, +12,7%). O padrão já
  apontado nas duas últimas leituras se repete pela terceira noite: os "fechamentos" mais
  recentes deste pipeline continuam sendo ajustados depois de já terem sido publicados
  como definitivos. As diferenças de preço são pequenas (<0,2%), mas o padrão em si — e
  principalmente a variação de volume, que é mais volátil — é um sinal de que a fonte de
  dados ainda está estabilizando o dado do dia mais recente por várias janelas de coleta
  seguidas. Trate os números de 28/08 usados aqui como o melhor dado disponível hoje, não
  como definitivo.
- **Nenhum pregão novo desde sexta-feira.** Esta leitura não testa nem invalida nada da
  tese de ontem — ela só recontextualiza os mesmos fatos com mais dois dias de defasagem
  em cima do COT, do câmbio e do físico BR. Onde esta leitura foi além da de ontem foi na
  série completa da margem de biodiesel (compressão de uma semana) e na proximidade do
  evento Danantara (agora <48h) — o resto é, deliberadamente, a mesma tese revisitada.
- **COT desatualizado, agora com 5 dias corridos de defasagem** (corte de 25/08 frente ao
  fechamento de 28/08, mais o fim de semana em cima) — a maior lacuna desta leitura,
  igual à de ontem mas mais grave em termos de tempo decorrido.
- **Prêmios de exportação (Paranaguá, farelo e óleo) seguem congelados**, agora 5-6
  sessões seguidas idênticas — não dá para saber se reflete mercado físico realmente
  parado ou limitação de atualização da fonte (NAG).
- **Decisão do STF mencionada na notícia de 28/08 segue sem teor detalhado** no briefing —
  não há vínculo a nenhum evento do `tributario_watch.toml`. Nenhum conteúdo foi inventado
  para essa decisão.
- **`tributario_watch.toml` sem atualização há 86 dias** — pelo menos dois vetores
  (isenção PIS/Cofins do biodiesel, vigência até 31/07; MP 1.358/2026, vigência até
  11/07) já passaram da data de vigência registrada sem nota de renovação ou expiração.
  Tratados como "status desconhecido pós-vigência".
- **NOPA segue inacessível** (paywall) — nenhum número de esmagamento americano mensal
  confirmado.
- **USDA WASDE ausente** da janela — nenhuma leitura de balanço mundial oficial
  atualizado disponível.
- **Percentil histórico de posicionamento COT não está disponível no briefing** — toda
  leitura de "fundos comprando/vendendo" nesta análise usa variação semana a semana de
  contratos absolutos, não percentil histórico. Nenhum percentil foi inventado.
- **MPOB (palma Malásia) segue com parser quebrado** (3.456 caracteres, sem números
  extraídos) desde pelo menos 27/08 — nenhum dado de produção/estoque de palma malaia
  disponível para cruzar com a tese de substituição via Indonésia.
