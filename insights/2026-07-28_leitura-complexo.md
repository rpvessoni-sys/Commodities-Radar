---
data: 2026-07-28
titulo: "Terça-feira de resolução parcial: o ratio Farelo/Soja finalmente rompe para baixo de 80% (79,96%, CBOT 2026-07-28) e entra oficialmente na zona 'comprimida' — resolvendo, com 47 dias de atraso, o gatilho estrutural bear-farelo aberto em 11/jun — enquanto a soja fecha pelo 2º dia acima da resistência de 1.180,00 (1.204,00, +0,35%) com a base física em Paranaguá ainda alargada (+8,87% sobre a paridade) e o óleo estende a quebra do suporte de 72,00 por mais uma sessão (70,36, -0,69%) mesmo com a margem de biodiesel americana melhorando pelo 2º dia seguido (1,1894 USD/gal, +2,28%) — um complexo que se divide de forma cada vez mais nítida entre um farelo estruturalmente pressionado, uma soja tecnicamente firme e um óleo tecnicamente fraco mas fundamentalmente sustentado"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT (ZSU26 soja / ZMU26 farelo / ZLU26 óleo) — sessão de 2026-07-28
  - CME heating_oil_cbot (HO=F) — sessão de 2026-07-28 (788 contratos) e revisão de 2026-07-27 (23.447 contratos, corrigindo o print anômalo de 278 contratos citado na leitura anterior)
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, paridade BR, Índice de Sobra de Farelo, Índice de Suporte do Óleo) — 2026-07-28, com a série 2026-07-27 revisada (ver Honestidade)
  - BCB PTAX — 2026-07-28 (USD/BRL 5,1177, EUR/BRL 5,8347, Selic diária 0,052531% a.a.)
  - CEPEA/ESALQ Paranaguá via NAG — 2026-07-28 (suporte R$ 147,89/saca, var +0,09%)
  - CEPEA/ESALQ Paraná interior via NAG — 2026-07-28 (R$ 140,02/saca, var -0,40%)
  - NAG Físico BR (farelo MT/IMEA R$ 1.669,72/ton estável; Rondonópolis R$ 1.650,00/ton estável; RS R$ 1.640,00/ton estável; prêmios export PGUA farelo +0,05 USD/sht e óleo +0,08 cts/lb, ambos inalterados) — 2026-07-28
  - CFTC COT Managed Money — corte de 2026-07-21 (ainda o mais recente; próximo corte referente a 28/07, publicação normal ~31/07)
  - USDA Crop Progress — ainda 2026-07-26 (11% excelente + 52% boa + 7% ruim), sem corte novo esta semana
  - USDA WASDE — ausente da janela de 14 dias deste briefing (último dado 2026-07-10, agora 18 dias, saiu da janela rolante — ver Honestidade)
  - NOPA — fila `release-nopa-2026-07-28`, `monthly_status` continua em 0,0 bool (paywall)
  - ABIOVE projeções mensais — balanços ago-dez/2026 (farelo/óleo/soja), sem alteração
  - NOAA CPC ENSO — 2026-07-28 (El Niño Advisory, inalterado desde pelo menos 03/07/2026)
  - MPOB — 2026-07-28 (19º dia consecutivo com o mesmo conteúdo exato de 3.439 caracteres, parser sem números extraídos)
  - BCBA Argentina — 2026-07-22 (6 dias sem atualização)
  - Notícias Agrícolas/Farm Progress RSS — 2026-07-28 (160 itens lidos, 9 mantidos; manchete nova "North Dakota names new soybean group leaders", farmprogress.com, sem conteúdo quantitativo)
  - Forecasts estatísticos internos — 2026-07-28 (spot ref já reflete o fechamento de hoje: soja 1.204,00 / farelo 320,90 / óleo 70,36; viés "altista" nas três, ver Honestidade sobre defasagem do modelo)
  - system/tributario_watch.toml (lido apenas como referência, não editado) — 10 eventos, `atualizado_em` 2026-06-05 (54 dias sem atualização); trata `trib-PISCOFINS-BIODIESEL-ISENCAO-2026-07-31`
  - Cruza com [[2026-07-27_leitura-complexo]], [[2026-07-26_leitura-complexo]], [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (D+7 vencido, checkpoint D+90 em 2026-09-09)
status: ativa
vies: [bear-farelo, bear-oleo_soja, neutral-soja]
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
Quando o oil share sobe, o óleo passa a "pagar o crush" sozinho, e o farelo
vira, cada vez mais, um subproduto que a esmagadora aceita vender barato só
para liberar o óleo — é esse mecanismo que está por trás do **ratio Far/Soj**
(preço do farelo dividido pelo preço da soja, normalizado pela conversão
bushel↔short ton): abaixo de 80% o farelo está historicamente "abundante"
frente à soja (zona bear, chamada aqui de "comprimida"); acima de 87%,
"apertado" (zona bull); entre os dois, zona neutra e de **mean-reversion**
(funciona nos dois lados do book, tanto para quem compra quanto para quem
vende o spread).

**O evento mais importante desta sessão não foi um choque de preço — foi um
número cruzando uma linha que já vinha sendo vigiada há sete semanas.** O
ratio Far/Soj fechou hoje em **79,96%** (indicators, 2026-07-28: farelo
320,90 USD/short ton ÷ (soja 1.204,00 cts/bushel × 33,33)), abaixo de 80,09%
em 27/07 (indicators, revisado — ver Honestidade) e, pela primeira vez desde
que esta série de leituras diárias começou a rastrear o indicador,
**oficialmente dentro da zona "comprimida"** (<80%, farelo estruturalmente
abundante frente à soja). O próprio sistema sinalizou isso como o item de
maior prioridade da fila de julgamento de hoje (🔴 `ratio-zona-2026-07-28`,
"Ratio Far/Soj entrou na zona 'comprimido' (80,0%, era 'neutro' 80,1%)"). O
significado prático: o mecanismo de mean-reversion do spread muda de regime
— dentro da zona neutra (80-87%), o spread historicamente oscila nos dois
sentidos sem viés direcional forte; abaixo de 80%, a probabilidade histórica
favorece a continuação da compressão (farelo caro demais frente à soja,
tendendo a corrigir para baixo) até a zona reverter. **Este é, também, o
desfecho — com 47 dias de atraso — do gatilho central da tese bear-farelo
aberta em [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]:**
naquela leitura, o ratio havia comprimido de 83,3% para 81,4% em quatro
pregões e a revisão D+7 (marcada para 2026-06-18, vencida e reaberta pela
fila de hoje como `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`)
perguntava explicitamente "o ratio fechou <80%?". A resposta, sete semanas
depois do prazo original, é **sim, hoje** — o que não invalida o atraso (o
ratio passou boa parte de julho oscilando entre 79,3% e 80,7%, testando o
piso sem romper, como as leituras dos últimos dez dias documentaram
exaustivamente), mas dá à tese estrutural bear-farelo (sustentada por
ABIOVE, pelo Índice de Sobra de Farelo em 80/100, e pelo prêmio de
exportação zerado em Paranaguá há 25 dias) a primeira confirmação tática
concreta do próprio indicador que a originou. **Ao mesmo tempo, e é
importante não deixar isso em segundo plano, a soja fechou pelo segundo dia
seguido acima do nível técnico de 1.180,00** (1.204,00 hoje, 2,03% acima,
ante 1,48% ontem — a distância aumentou, não diminuiu, porque a soja subiu
+0,35% no dia enquanto o farelo subiu só +0,19%: é exatamente essa diferença
de ritmo, soja mais forte que farelo em termos absolutos, que empurrou o
ratio para baixo de 80%, mesmo com o farelo tecnicamente positivo no dia).
**E o óleo estendeu a quebra do suporte de 72,00 por mais uma sessão**
(fechamento 70,36 cts/lb, -0,69% no dia, quinta ou sexta sessão nesta faixa
de fraqueza técnica), mas a margem de biodiesel americana **melhorou pelo
segundo dia seguido** (1,1894 USD/galão, +2,28%, porque o custo do óleo caiu
mais rápido do que a receita) — a mesma tensão entre "preço fraco" e
"fundamento de demanda forte" que já vinha sendo documentada. **Leitura de
uma linha:** o pivô do complexo hoje é o ratio Far/Soj, que finalmente
resolveu (bear) o impasse de sete semanas; a maior convicção desta leitura é
que o farelo entrou em regime tático bear confirmado pelo próprio gatilho
que a tese estrutural sempre apontou; confiança moderada-alta para farelo,
moderada para óleo (tecnicamente fraco, fundamentalmente sustentado — a
tensão não se resolveu, só se prolongou), e neutra-com-tilt-de-alta para
soja (acima da resistência por dois dias, mas o COT mais recente ainda é de
21/07 e não confirma se os fundos mantiveram a posição extremamente comprada
que se formou naquela semana).

---

## Soja

**Viés: neutro, com viés tático de alta — a soja fechou 1.204,00 cts/bushel
(CBOT, ticker ZSU26.CBT, +0,35% sobre o fechamento revisado de 27/07 de
1.199,75), o segundo fechamento seguido acima do nível técnico de 1.180,00,
com a distância aumentando (2,03% hoje ante 1,48% ontem).** Trata
`alerta-quebra_resistencia-soja_cbot-2026-07-28` (o alerta confirma que o
fechamento de hoje segue acima do nível 1.180,00 pelo segundo dia, com a
estrutura de rompimento de meados de julho ganhando fôlego em vez de perder,
ao contrário do que o tombo de 27/07 sugeria como risco iminente).

### O que sustenta a tese

**A sessão de hoje foi de recuperação técnica dentro de um range moderado.**
Abertura 1.202,75 (já 0,25% acima do fechamento revisado de ontem — um gap
de abertura positivo, o oposto do gap negativo de 27/07), máxima 1.209,50
(tocada sem se sustentar), mínima 1.193,00 (abaixo da abertura, indicando
que houve pressão vendedora real durante o pregão) e fechamento em 1.204,00
— uma recuperação de +0,92% desde a mínima até o fechamento
((1.204,00-1.193,00)÷1.193,00), ou 66,7% do range do dia
((1.204,00-1.193,00)÷(1.209,50-1.193,00)). **Mecanismo e leitura:** o
contrato testou território abaixo da abertura durante a sessão (mínima
1.193,00, ainda 1,10% acima do nível técnico de 1.180,00) mas foi comprado
de volta para fechar no terço superior do range — um padrão de "compra na
fraqueza" mais construtivo do que o fechamento na mínima observado em 27/07,
e consistente com um mercado que, depois do desmonte técnico da véspera,
encontrou comprador real na região perto de 1.193-1.195. O volume de hoje
foi de 28.794 contratos — este briefing não traz, na janela de 14 dias
consultada, o volume de 27/07 para soja especificamente (a tabela `cme_cbot`
truncou antes de chegar à linha de soja daquela data — ver Honestidade),
então esta leitura **não afirma** se o volume de hoje veio acima ou abaixo
do de ontem; o dado disponível e citável é apenas o nível absoluto de hoje.

**O nível de 1.180,00 segue sendo o pivô técnico mais vigiado, mas a folga
aumentou hoje, não diminuiu.** Ontem, a distância até esse nível havia caído
para 1,48% (a menor da janela até então, depois do tombo de -3,45%); hoje,
com a alta de +0,35%, a distância voltou a 2,03%
((1.204,00-1.180,00)÷1.180,00). **Isso não elimina o risco** — a mínima de
hoje (1.193,00) chegou a ficar a apenas 1,10% do nível, o mais próximo que o
intradia chegou de tocar 1.180,00 em toda a janela recente — mas o
fechamento reforça, por ora, a leitura de que o piso estrutural aguentou o
teste da véspera sem ceder.

**O câmbio trabalhou a favor da soja em reais hoje.** USD/BRL PTAX fechou em
5,1177 (BCB, 2026-07-28), alta de +0,34% sobre 5,1005 de ontem — a quarta
alta seguida do dólar frente ao real desde a mínima local de 5,0638 em
22/07. **Mecanismo:** a paridade teórica em reais (CBOT convertido pelo
câmbio, sem considerar basis/frete/ágio local) é
`preço CBOT em cts × PTAX`; com o CBOT subindo +0,35% e o câmbio subindo
+0,34% na mesma sessão, os dois efeitos se somam em vez de se cancelarem —
a paridade calculada saltou para **R$ 135,84/saca** (indicators,
2026-07-28: CBOT 1.204,00 cts × USD/BRL 5,1177), ante R$ 134,91 em 27/07
(indicators revisado), alta de +0,69% — quase o dobro do movimento do CBOT
isolado, porque câmbio e papel jogaram na mesma direção pela primeira vez em
várias sessões.

**A base física em Paranaguá segue larga, embora tenha estreitado
ligeiramente frente ao pico de ontem.** CEPEA/ESALQ Soja Paranaguá (via NAG)
fechou em R$ 147,89/saca hoje, alta de +0,09% sobre R$ 147,75 de ontem — a
segunda alta seguida depois da única queda da semana (27/07, -0,42%). Com a
paridade teórica em R$ 135,84, o **prêmio de exportação sobre a paridade
ficou em +8,87%** ((147,89-135,84)÷135,84), ante aproximadamente +9,52%
calculado sobre os números revisados de ontem (147,75 vs paridade 134,91) —
uma leve compressão do prêmio, mas ainda um dos níveis mais largos desta
janela observada (a série recente oscilou entre +7% e +9,7%). **Mecanismo e
leitura:** o prêmio comprimiu hoje porque a paridade teórica subiu mais
rápido (+0,69%) do que o preço físico em Paranaguá (+0,09%) — ou seja, o
papel (CBOT + câmbio) "alcançou" um pouco do físico, e não o contrário. Isso
é consistente com a leitura de que grande parte do alargamento de +9,73%
observado ontem era mesmo um artefato temporário do desmonte técnico do
papel, e não uma mudança permanente na demanda física de exportação — a
base ainda está historicamente larga, mas normalizando gradualmente. O
físico do Paraná interior, em contraste, **caiu** hoje (R$ 140,02/saca, var
-0,40%, NAG) — depois de ter subido ontem (+0,23%) — uma reversão que não
tem, neste briefing, uma explicação fundamental clara distinta de ruído de
praça normal.

**A curva forward preservou a forma de contango crescente, com um detalhe
de calendário que vale registrar.** Agosto/26 (Q26) 1.211,25 → Setembro/26
(U26, spot) 1.204,00 → Novembro/26 (X26) 1.219,75 (+15,75, +1,31% sobre o
spot) → Janeiro/27 (F27) 1.233,25 (+13,50, +1,11% sobre X26) → Março/27
(H27) 1.235,25 (+2,00, +0,16% sobre F27). **Note-se que Agosto/26 (o
vencimento mais próximo) está precificado ACIMA do spot de Setembro** — uma
pequena inversão de calendário (1.211,25 vs 1.204,00, +0,60%) que já
aparecia nas leituras anteriores e reflete tipicamente um prêmio de
convivência/entrega no vencimento mais próximo do fim da entressafra
brasileira, não uma mudança de tese. Da parte de trás da curva em diante
(U26→X26→F27→H27), a forma de contango crescente e suave segue idêntica à
documentada nos últimos dias — nenhum sinal de estresse físico de curto
prazo embutido na curva.

**Os forecasts estatísticos internos (2026-07-28)**, recalculados com o
fechamento de hoje (1.204,00), seguem etiquetados como "altista": central 7d
= 1.232,36 cts/bu (bandas 1.174,52-1.290,19); central 30d = 1.329,53 cts/bu
(bandas 1.209,79-1.449,26). Como já registrado em leituras anteriores, este
modelo (média móvel de 20 dias + volatilidade + inclinação de curto prazo)
carrega inércia da tendência ascendente das últimas semanas e tende a reagir
com atraso a reversões — esta leitura o trata como referência de banda
estatística, não como argumento de tese (ver Honestidade).

**A manchete do dia (Farm Progress, 28/07/2026, "North Dakota names new
soybean group leaders") não carrega nenhum conteúdo quantitativo** — é uma
notícia institucional/administrativa, sem relevância para a tese de preço.
Diferente da manchete de ontem ("Is a record soybean crop in the works?"),
que ao menos levantava uma narrativa de oferta, a manchete de hoje não
adiciona nem tira nada da leitura fundamental.

### O que invalida / risco para a soja

- **Um fechamento abaixo de 1.180,00** ainda encerraria a leitura de "piso
  estrutural de pé" — a mínima de hoje (1.193,00) chegou a 1,10% de
  distância, a mais próxima já registrada nesta janela, então o risco
  intradiário de teste segue vivo mesmo com o fechamento acima do nível.
- **O próximo corte do COT (28/07, publicação ~31/07) mostrar reversão do
  net long** de 21/07 (+73,6% na semana, 12,49% do open interest) —
  continua sendo o dado mais aguardado para validar se a posição
  especulativa esticada já foi parcialmente desmontada ou se ainda está
  intacta.
- **A base física em Paranaguá continuar comprimindo** — hoje o prêmio
  caiu de ~9,52% para 8,87%; uma sequência de compressões devolveria a
  leitura de "demanda de exportação excepcionalmente firme" para um
  patamar mais ordinário.
- **O câmbio reverter a sequência de altas** (quatro dias seguidos desde
  22/07) — se o USD/BRL cair enquanto o CBOT segue lateral, a paridade em
  reais perde o suporte que teve hoje.

### Leitura operacional — soja

O quadro de hoje é de **consolidação tática de alta** dentro de uma leitura
ainda oficialmente neutra: o fechamento no terço superior do range, acima
da resistência pelo segundo dia, com câmbio e papel reforçando juntos a
paridade em reais, dá alguma munição para quem está comprado desde o
rompimento de julho manter a posição com stop reavaliado logo abaixo de
1.193,00 (a mínima de hoje) ou, mais conservador, abaixo de 1.180,00. Para
quem opera vendido tático, a mínima intradiária de 1.193,00 — a mais
próxima que o preço chegou de tocar o piso estrutural nesta janela — é a
referência de entrada mais recente, com stop acima da máxima de hoje
(1.209,50); mas o argumento contra essa posição é que o fechamento no
terço superior do range sugere que o vendedor perdeu o pregão de hoje. Para
quem opera o book relativo, a compressão do prêmio de Paranaguá (de ~9,5%
para 8,9%) é, em si, uma operação de convergência de basis que capturou
valor hoje na direção oposta à de ontem — e o cruzamento com o farelo (ver
abaixo) torna o spread soja-forte/farelo-fraco (equivalente a short no
ratio Far/Soj, ou long soja/short farelo) a expressão mais direta da leitura
central desta edição.

---

## Farelo

**Viés: bear tático confirmado — o ratio Far/Soj cruzou hoje para dentro da
zona "comprimida" (<80%), fechando em 79,96% (indicators, 2026-07-28), o
primeiro fechamento abaixo de 80% documentado nesta série de leituras
diárias, resolvendo (com atraso, mas na direção prevista) o gatilho central
da tese estrutural aberta em [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]].**
Trata `ratio-zona-2026-07-28` (o item de maior prioridade da fila de hoje) e
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` (a
revisão D+7, vencida desde 2026-06-18, ganha hoje sua primeira confirmação
tática concreta — ver detalhamento abaixo).

### O que sustenta a tese

**O preço absoluto do farelo, isoladamente, teve um dia positivo e sem
direção clara — o que torna o movimento do ratio ainda mais relevante,
porque ele não veio de uma queda do farelo, e sim de a soja subir mais
rápido.** Farelo CBOT (ZMU26.CBT) abriu em 320,30 (exatamente no fechamento
revisado de ontem, um gap zero — o menor gap de abertura das três
commodities hoje), fez máxima de 323,30 e mínima de 318,60, fechando em
320,90 — alta de +0,19% no dia. O fechamento equivale a 48,9% do range
((320,90-318,60)÷(323,30-318,60)) — bem no meio, sem viés técnico forte de
força ou fraqueza. O volume, porém, saltou para **54.336 contratos**, alta
de +45,3% sobre os 37.404 de ontem (cme_cbot, 2026-07-27, dado citável
diretamente desta janela) — o maior salto de volume das três pernas hoje, e
justamente na sessão em que o ratio rompeu a zona comprimida. **Mecanismo e
leitura:** ratio Far/Soj = preço do farelo ÷ (preço da soja × fator de
conversão bushel↔short ton). Como a soja subiu +0,35% e o farelo subiu
apenas +0,19%, o numerador cresceu menos que o denominador, e o ratio caiu
— mesmo com o farelo positivo em termos absolutos. Esse é o ponto mais
importante para um trader que só olhasse o preço do farelo isoladamente
teria a impressão de um dia neutro-a-levemente-positivo; só o ratio revela
a fraqueza relativa real.

**A sequência recente do ratio mostra a compressão final até o rompimento.**
07-22: 80,65% → 07-23: 80,13% → 07-24: 80,02% → 07-27: 80,09% (indicators
revisado) → **07-28: 79,96%**. Note que 27/07 havia mostrado um respiro
(80,02%→80,09%, uma leve alta, dado revisado — ver Honestidade sobre a
diferença frente ao que a leitura de ontem registrou usando dados
pré-revisão), mas essa pausa não se sustentou: hoje o ratio voltou a cair e,
desta vez, atravessou o piso de 80% pela primeira vez de forma confirmada
no fechamento. **Isso é exatamente o padrão que a tese de 11/06 descrevia**
("Ratio Far/Soj comprimiu de 83,3% → 81,4% em 4 pregões... a zona comprimida
(<80%) pode chegar em 1-2 semanas se o padrão se mantiver") — o padrão
demorou muito mais que 1-2 semanas para se completar (47 dias, não 7-14),
com o ratio passando boa parte de julho testando e recuando do piso, mas o
desfecho direcional (compressão até <80%) é exatamente o que a tese
previu. **Veredito atualizado sobre a revisão D+7:** confirmado hoje, com
a ressalva de que o tempo de maturação foi muito mais longo do que a janela
original de revisão previa — um dado relevante para calibrar expectativas de
velocidade em teses futuras baseadas neste mesmo indicador.

**O COT de 21/07/2026 (CFTC, ainda o mais recente) mostrava managed money
extremamente comprado em farelo antes deste rompimento** — net long de
73.476 contratos (11,89% do open interest de 618.289 contratos), alta de
+57,8% na semana. **Mecanismo e tensão:** um ratio caindo para a zona
estruturalmente bear, combinado com fundos ainda posicionados comprados (na
foto de 21/07), monta a configuração clássica de "posição não paga" —
especuladores comprados justamente quando o indicador estrutural que
sustenta a tese contrária (farelo abundante) está se confirmando. Se o
corte de 28/07 (publicação ~31/07) mostrar esses fundos começando a vender,
a resolução do ratio para baixo de 80% ganharia reforço de fluxo adicional
(venda de posição comprada mal calibrada, empurrando o farelo ainda mais
para baixo relativo à soja).

**A crush margin caiu para 2,7594 USD/bushel hoje, o menor valor de toda a
janela observada com dados nesta série** (Board Crush: farelo 320,90 +
óleo 70,36 − soja 1.204,00; sequência 07-23: 3,1395 → 07-24: 2,9568 → 07-27:
2,8426 (revisado) → **07-28: 2,7594**, -2,93% no dia). **Mecanismo:** a soja
(o custo) subiu +0,35% enquanto a soma farelo+óleo (a receita, em termos
absolutos de pontos) mal se moveu (farelo +0,19%, óleo em queda -0,69%) — a
crush comprime porque o custo sobe mais rápido que a receita combinada. A
crush segue positiva e ainda distante do nível de alerta histórico citado em
leituras passadas (<2,50 USD/bu), mas a tendência de seis sessões
consecutivas de compressão é a mais persistente desta janela — um sinal, se
continuar, de que a esmagadora pode começar a moderar o ritmo de
esmagamento, o que reduziria a oferta física de farelo (um contraponto
estrutural, ainda incipiente, à tese bear).

**O oil-meal spread caiu para 0,6798 USD/bushel** (ante 0,7469 em 27/07,
-8,99%) — a quinta sessão seguida de compressão nesta métrica, com o
farelo ganhando terreno relativo sobre o óleo dentro do valor do crush
(mecanismo distinto do ratio Far/Soj: aqui a comparação é farelo vs. óleo,
não farelo vs. soja — e nessa comparação específica o farelo está
relativamente FORTE, não fraco, porque o óleo caiu -0,69% no dia enquanto o
farelo subiu +0,19%). Isso ilustra a diferença central desta leitura: o
farelo está fraco frente à SOJA (ratio caindo) mas forte frente ao ÓLEO
(oil-meal spread caindo) — duas comparações diferentes, ambas verdadeiras
simultaneamente, e ambas relevantes para quem opera spreads dentro do
crush.

**As praças físicas de farelo no Brasil (NAG) seguem totalmente estáveis
hoje.** Mato Grosso/IMEA R$ 1.669,72/ton (var 0,0%, quinto dia sem variação
desde o salto de +4,18% em 24/07), Rondonópolis R$ 1.650,00/ton (estável
desde 20/07) e RS R$ 1.640,00/ton (estável desde pelo menos 14/07). O
prêmio de exportação em Paranaguá segue zerado em +0,05 USD/short ton — o
mesmo valor exato desde 03/07/2026, agora **25 dias corridos sem variação**
— o pilar mais persistente da tese estrutural bear (exportar farelo não
compete com o mercado interno, o excedente fica represado internamente).

**O Índice de Sobra de Farelo (ISF) permanece em 80/100 (4 de 5 condições
estruturais), com print de 28/07/2026** — inalterado desde pelo menos
01/07/2026. **A trajetória ABIOVE (sem alteração)** segue mostrando a
exportação de farelo brasileiro projetada caindo de 1.400 mil toneladas em
agosto/2026 para 700 mil toneladas em dezembro/2026 (-50% em quatro meses),
com produção caindo bem menos (2.285,06 → 1.659,04 mil toneladas, -27,4%) —
o excedente segue sendo empurrado para o mercado interno de ração,
sustentando o pilar estrutural bear independentemente do preço diário. **É
importante notar que o ISF e a trajetória ABIOVE não se moveram hoje** — o
rompimento do ratio para baixo de 80% é um evento TÁTICO (o preço relativo
finalmente reconheceu uma condição estrutural que já estava posta há
semanas), não uma mudança nos fundamentos em si.

### O que invalida / risco para o farelo

- **O ratio Far/Soj devolver o rompimento e fechar de volta acima de 80,00%**
  nas próximas sessões — dado que o próprio ratio passou boa parte de julho
  testando e recuando desse nível, um único fechamento abaixo de 80% ainda
  não é, por si só, uma confirmação definitiva de tendência; 2-3 fechamentos
  consecutivos abaixo do nível dariam mais robustez à leitura de regime
  mudado.
- **O próximo corte do COT (28/07, publicação ~31/07) mostrar os fundos
  ainda comprados** (não vendendo) apesar do ratio comprimindo — sustentaria
  a configuração de "posição não paga" sem gatilho de fluxo adicional,
  atrasando a resolução baixista via venda especulativa.
- **A crush margin estabilizar ou reverter a compressão** — se a esmagadora
  reduzir o ritmo de esmagamento (resposta a seis sessões de crush em
  queda), a oferta física de farelo poderia encolher o suficiente para
  sustentar o preço relativo, contrariando a tese ABIOVE/ISF no curto prazo.
- **O prêmio de exportação em Paranaguá sair de zero** — 25 dias sem
  variação é um pilar estrutural forte, mas uma mudança abrupta (ex.:
  demanda chinesa por farelo, não usual, ou reversão cambial abrupta)
  reabriria o canal de exportação e absorveria parte do excedente interno.
- **NOPA seguir inacessível** para os checkpoints D+90 (2026-09-09) e D+180
  (2026-12-08) da revisão de 11/06 — trata `release-nopa-2026-07-28`, ainda
  sem dado interpretável (`monthly_status` 0,0 bool, mesma barreira de
  assinatura paga).

### Leitura operacional — farelo

O rompimento do ratio Far/Soj para dentro da zona comprimida é, nesta
leitura, o gatilho tático mais acionável do dia — mas a forma recomendada de
expressá-lo continua sendo via spread, não posição vendida outright em
farelo isolado: o próprio preço absoluto do farelo subiu hoje (+0,19%), e o
volume elevado (+45,3%) sustenta convicção por trás do movimento do ratio,
mas não por trás de uma queda de preço absoluto — o risco de "short squeeze"
em farelo isolado, documentado em leituras anteriores, permanece real
enquanto o COT (ainda de 21/07) mostra fundos comprados. Para quem opera o
spread Far/Soj diretamente, hoje foi um dia claramente favorável ao lado
"soja forte / farelo fraco" (short farelo / long soja no ratio, ou
equivalente) — a operação relativa mais direta desta leitura. Para quem
opera o crush completo, a compressão simultânea do ratio Far/Soj (farelo
fraco vs. soja) e do oil-meal spread (farelo forte vs. óleo) sugere que a
perna mais fraca do complexo hoje, relativamente, não é bem descrita como
"farelo" isolado, mas como "farelo vs. soja" especificamente — comprar
farelo contra óleo (capturando a compressão do oil-meal spread) e vender
farelo contra soja (capturando a compressão do ratio) são, na prática, apostas
direcionalmente opostas dentro do mesmo produto, o que reforça a
recomendação de operar via spreads calibrados à tese específica, não via
uma leitura única de "farelo bear" aplicada indiscriminadamente a todos os
pares.

---

## Óleo

**Viés: bear tático, com tensão estrutural crescente — o óleo estendeu a
quebra do suporte técnico de 72,00 cts/lb por mais uma sessão, fechando em
70,36 cts/lb (-0,69% sobre o fechamento revisado de ontem de 70,85), mas a
margem de biodiesel americana melhorou pelo segundo dia seguido (+2,28%
hoje, após +0,78% ontem), e o Índice de Suporte do Óleo segue em 100/100.**
Trata `alerta-quebra_suporte-oleo_cbot-2026-07-28` (segunda confirmação
consecutiva do rompimento, depois da quebra inicial de 27/07).

### O que sustenta a tese

**A sessão de hoje foi de recuperação parcial dentro de uma tendência ainda
de fraqueza.** Abertura 70,90 (praticamente no fechamento de ontem, +0,07%,
o menor gap das três commodities hoje), máxima 71,10 (uma máxima marginal
acima da abertura, tocada e não sustentada), mínima 69,59 (um novo patamar
de fraqueza, bem abaixo do suporte de 72,00) e fechamento em 70,36 — uma
recuperação desde a mínima até o fechamento de +1,11%
((70,36-69,59)÷69,59), equivalente a 51,0% do range do dia
((70,36-69,59)÷(71,10-69,59)). **Mecanismo e leitura:** diferente do
fechamento no fundo do range observado em 27/07 (3,7% do range, o pior das
três pernas naquele dia), hoje o óleo fechou no meio do range — um sinal de
que, mesmo em queda no dia e mesmo abaixo do suporte técnico, houve alguma
recompra ao longo da sessão. Isso não desfaz a quebra de 72,00 (o
fechamento segue -2,28% abaixo desse nível), mas modera a leitura de
"capitulação" que o fechamento de ontem sugeria. O volume de hoje foi de
50.475 contratos; este briefing não traz, na janela consultada, o volume de
27/07 para óleo (mesma limitação de truncamento da tabela `cme_cbot`
observada para a soja — ver Honestidade), então esta leitura não compara
volumes dia a dia para o óleo.

**A margem de biodiesel americana é o dado mais importante e menos óbvio
desta sessão para o óleo, pelo segundo dia seguido.** Custo do óleo: 5,277
USD/galão (7,5 lb × 70,36 cts/lb), ante 5,3137 ontem (-0,69%, seguindo
exatamente a queda do preço do óleo). Receita: 7,2664 USD/galão (heating
oil 4,1014 + 1,5×RIN D4 2,11), ante 7,2766 ontem (-0,14% — o heating oil
caiu de 4,1116 para 4,1014, -0,25%, um movimento pequeno). Margem:
**1,1894 USD/galão**, ante 1,1629 (+2,28%). **Mecanismo:** como o custo do
óleo caiu mais rápido (-0,69%) do que a receita (-0,14%, quase estável, com
o RIN D4 fixo em 2,11 USD/RIN e o heating oil quase parado), a margem —
que mede o incentivo econômico da indústria de biodiesel americana a usar
óleo de soja como insumo — melhorou de forma consistente pelo segundo dia
seguido (07-27: +0,78%, 07-28: +2,28%, um ganho acumulado de ~3,1% em duas
sessões). **Esta é a tensão central e recorrente da tese do óleo**: o
preço cai, mas o incentivo a comprá-lo como insumo de biodiesel aumenta —
um padrão que, se persistir, sugere que a fraqueza técnica do papel pode
estar criando uma janela de entrada para quem acompanha a tese estrutural
de demanda de biodiesel, mais do que sinalizando uma deterioração genuína
de fundamento.

**O heating oil (HO=F), o termômetro de energia usado nesta série para
calcular a margem de biodiesel, teve um volume anormalmente baixo hoje —
mas o dado de ontem, antes tratado como suspeito, foi revisado para um
volume normal.** O print de hoje veio com apenas **788 contratos** — baixo,
embora não tão extremo quanto o de 27/07. E é aqui que está o detalhe mais
relevante: a leitura de ontem havia registrado, como ponto de Honestidade,
que o print de 27/07 veio com apenas 278 contratos (o mais baixo da janela
até então) e por isso não tratava o heating oil daquele dia como
confirmado. **Este briefing de hoje traz o mesmo dado de 27/07 já
REVISADO para 23.447 contratos** (cme_cbot, linha de 2026-07-27) — uma
correção de mais de 80x o valor original, confirmando que o print de 278
contratos era de fato incompleto/preliminar, exatamente como a leitura
anterior havia suspeitado. **Isso valida retroativamente a cautela da
leitura de 27/07**, mas também levanta uma bandeira nova: se o padrão se
repetir, o print de hoje (788 contratos) também pode estar incompleto e
sujeito a revisão para cima no próximo dump — esta leitura trata o dado de
hoje com a mesma cautela, sem descartá-lo nem tratá-lo como definitivo (ver
Honestidade).

**O Índice de Suporte do Óleo (ISO) permanece em 100/100 (5 de 5
condições), com print de 28/07/2026** — a tese estrutural (óleo dominando
o valor do crush) segue formalmente intacta, sem nenhuma alteração apesar
da quebra técnica persistente do preço.

**O oil share caiu para 52,3%** (ante 52,52% em 27/07, -0,22 ponto
percentual) — a continuação da tendência de queda já documentada nas
últimas leituras (52,62% em 24/07 → 52,52% em 27/07 → **52,3%** hoje),
agora bem abaixo da faixa de 53,0-53,5% em que o indicador oscilou até
22/07. **Mecanismo:** o oil share mede a fração do valor total do crush
capturada pelo óleo; como o óleo caiu -0,69% no dia enquanto o farelo subiu
+0,19%, a fração de valor do óleo dentro do total encolheu. A persistência
dessa queda (agora três leituras seguidas) é o dado tático que mais tensiona
a narrativa estrutural do ISO 100/100 — ainda não a contradiz (o índice usa
critérios estruturais, não o valor tático do dia), mas é o indicador mais
provável de ser o primeiro a capturar uma eventual mudança de regime se a
fraqueza do óleo persistir.

**O COT de 21/07/2026 (CFTC, ainda o mais recente) seguia mostrando o óleo
como a perna mais concorrida das três** — managed money com 143.159
contratos comprados, 18,17% do open interest de 661.652 contratos (ante
12,49% em soja e 11,89% em farelo). Esse posicionamento concentrado, ainda
não confirmado ou desmentido pelo corte de 28/07 (publicação ~31/07), segue
sendo o maior risco de uma correção mais aguda se o sentimento virar de vez
— e a quebra técnica persistente de 72,00 é, no mínimo, um sinal de alerta
tático nessa direção.

**A curva forward manteve a backwardation (desconto crescente nos
vencimentos mais distantes) com a forma preservada.** Agosto/26 (Q26) 70,83
→ Setembro/26 (U26, spot) 70,36 (-0,47, -0,66%) → Outubro/26 (V26) 69,59
(-0,77, -1,09%) → Dezembro/26 (Z26) 69,07 (-0,52, -0,75%) → Janeiro/27
(F27) 68,83 (-0,24, -0,35%) — uma queda total de -2,00 cts/lb (-2,82%) de
agosto a janeiro/27, em linha com a estrutura documentada nas últimas
leituras (backwardation moderada, sinalizando aperto físico relativo de
curto prazo frente aos vencimentos futuros, sem sinal de estresse agudo).

### O que invalida / risco para o óleo

- **Um fechamento abaixo de 69,59** (mínima de hoje) confirmaria uma
  terceira sessão seguida de fraqueza (contando 27/07 e 28/07) e reforçaria
  a leitura de mudança de regime técnico persistente, não apenas um evento
  de dois dias.
- **O heating oil (HO=F) mostrar, na próxima sessão, um volume consistente
  e não sujeito a revisão material** — depois da correção de 278 para
  23.447 contratos em 27/07, e do novo print baixo de 788 contratos hoje,
  esta leitura não trata nenhum dos dois últimos prints de heating oil como
  plenamente confiáveis até uma sessão de volume estável confirmar o nível.
- **O oil share continuar caindo abaixo de 52,3%** por mais sessões —
  reforçaria a leitura de perda estrutural de participação do óleo no valor
  do crush, o primeiro indicador tático a se mover na direção de contradizer
  o ISO 100/100.
- **O próximo corte do COT (28/07, publicação ~31/07) confirmar liquidação
  no net long mais concorrido das três pernas (18,17% do OI)** — o teste
  mais direto da hipótese de que o posicionamento excessivamente comprado
  está começando a ser desmontado.
- **A isenção PIS/Cofins do biodiesel expirar em 31/07 sem renovação** (ver
  Lente fiscal), agora a apenas **3 dias** — um vetor bearish direto para a
  demanda doméstica de óleo, independente do CBOT e da margem americana.
- **MPOB seguir inacessível** (19º dia consecutivo) — mantém cego o efeito
  de eventuais movimentos no prêmio de substituição via palma.

### Leitura operacional — óleo

O óleo segue sendo, nesta leitura, a perna com a tensão mais explícita entre
técnico e fundamento: dois fechamentos seguidos abaixo do suporte de 72,00
(27/07 e 28/07), mas com o segundo fechando no meio do range (não no fundo,
como ontem) e com a margem de biodiesel melhorando por dois dias seguidos.
Para quem está comprado direcional, a quebra persistente é motivo concreto
para manter cautela e considerar redução de exposição ou stop na mínima de
hoje (69,59), mas a recuperação intradiária (do fundo do range para o meio)
e a margem de biodiesel mais favorável são argumentos reais para não tratar
a posição como definitivamente invalidada — mais como uma tese estrutural
que está sendo testada tecnicamente, sem confirmação de que perdeu
sustentação fundamental. Para quem opera vendido ou tático short, a mínima
de hoje (69,59) é a referência de entrada mais recente, com stop acima da
máxima de hoje (71,10); mas a melhora de dois dias seguidos na margem de
biodiesel, somada ao ISO ainda em 100/100, significa que essa é uma aposta
em continuidade técnica de curto prazo, não em mudança de tese estrutural —
e o prazo de 3 dias até o vencimento da isenção PIS/Cofins (31/07) é um
catalisador concreto a observar antes de estender esse tipo de posição além
da próxima semana. Para quem opera o crush ou o oil-meal spread, a
compressão do spread (-8,99% hoje, quinta queda seguida, ver Farelo) segue
sendo a expressão mais equilibrada da tensão atual entre as duas pernas de
saída do esmagamento — hoje especificamente favorável ao lado "farelo forte
/ óleo fraco" dentro do crush.

---

## Spreads e crush — leitura de complexo

### Ratio Far/Soj: 79,96% — rompimento confirmado da zona comprimida, o evento do dia

Depois de sete semanas testando o piso de 80% (desde a compressão inicial
de 83,3%→81,4% documentada em 11/06), o ratio fechou hoje **abaixo de 80%
pela primeira vez de forma sinalizada pelo próprio sistema** (fila
`ratio-zona-2026-07-28`). A sequência recente: 07-22: 80,65% → 07-23:
80,13% → 07-24: 80,02% → 07-27: 80,09% (revisado) → **07-28: 79,96%**. O
mecanismo do dia foi soja subindo mais rápido (+0,35%) que farelo (+0,19%)
— não uma queda absoluta do farelo. A revisão D+7 de 11/06
(`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, vencida
desde 2026-06-18) ganha hoje sua primeira confirmação tática concreta, com
a ressalva de que o tempo de maturação (47 dias) foi muito mais longo do
que a janela original de revisão previa. O checkpoint D+90 (2026-09-09)
permanece como o próximo marco formal de revisão da tese completa.

### Crush margin: 2,7594 USD/bu — novo menor valor da janela, sexta sessão seguida de compressão

Caiu -2,93% no dia (2,8426 → 2,7594, ambos valores revisados/atuais), o
menor valor de toda a série recente (07-23: 3,1395 → 07-24: 2,9568 → 07-27:
2,8426 → **07-28: 2,7594**). O mecanismo é sempre o mesmo: a soja subiu
proporcionalmente mais rápido do que a soma de farelo e óleo na sessão de
hoje. A crush segue folgada em termos absolutos (bem acima de zero, e
distante do nível de alerta de <2,50 USD/bu citado em leituras passadas),
mas a persistência de seis sessões seguidas de compressão é o dado a
monitorar para avaliar se a esmagadora começa a moderar o ritmo — o que, se
ocorrer, reduziria a oferta física de farelo e seria um contraponto,
ainda que incipiente, à tese bear estrutural.

### Oil share: 52,3% — quarta sessão seguida de queda, abaixo da faixa recente

Caiu -0,22 ponto percentual (52,52% → 52,3%), a continuação da sequência
de quedas desde que o indicador saiu da faixa estreita de 53,0-53,5% em
que oscilou até 22/07 (52,62% em 24/07 → 52,52% em 27/07 → **52,3%** hoje).
Ainda não é uma ruptura estrutural (o ISO permanece 100/100), mas a
persistência da queda é o indicador tático mais provável de antecipar uma
eventual revisão do índice estrutural, se continuar.

### Oil-meal spread: 0,6798 USD/bu — compressão de -8,99%, quinta queda seguida

Caiu -8,99% no dia (0,7469 → 0,6798) — o farelo segue ganhando terreno
relativo sobre o óleo dentro do valor do crush, quinta sessão seguida nessa
direção. **Importante**: esse movimento é o oposto do ratio Far/Soj (que
mostra o farelo perdendo terreno relativo à SOJA) — as duas métricas
capturam comparações diferentes (farelo vs. óleo, e farelo vs. soja) e hoje
apontam em direções opostas, o que é a evidência mais direta de que a soja,
especificamente, foi a perna mais forte do complexo hoje, não o farelo mais
fraco em termos absolutos.

### Margem de biodiesel: 1,1894 USD/gal — segunda melhora seguida, +2,28% hoje (+3,1% acumulado em 2 dias)

O único indicador desta leitura que se move de forma consistentemente
OPOSTA à direção do preço do óleo: melhorou pelo segundo dia seguido
(07-27: +0,78%, 07-28: +2,28%) porque o custo do óleo caiu mais rápido do
que a receita (heating oil praticamente estável, RIN D4 fixo). É o dado
mais importante para entender que a queda do óleo nestes dois últimos dias
não reflete, ao menos pelo canal do biodiesel americano, uma deterioração
fundamental — pelo contrário, o incentivo econômico ao uso de óleo de soja
como insumo aumentou.

### COT: corte de 21/07, ainda o mais recente — o dado mais aguardado desta janela

O corte de 21/07/2026 mostrava fundos extremamente comprados nas três
pernas (net long +73,6% soja/12,49% OI, +57,8% farelo/11,89% OI, +11,4%
óleo/18,17% OI na semana). Nenhum dado novo chegou hoje. O próximo corte
(28/07, publicação normal ~31/07) é, para as três pernas, o teste mais
direto de se a posição especulativa esticada já começou a ser desmontada —
e ganha ainda mais relevância para o farelo especificamente, dado o
rompimento do ratio hoje: se os fundos comprados em farelo começarem a
vender, a resolução baixista do ratio ganharia reforço de fluxo adicional.

### ISF em 80/100, ISO em 100/100 — ambos inalterados, prints de 28/07

Os dois índices sintéticos, que captam condições estruturais (não a
mecânica tática de preço intradiário), permanecem exatamente nos mesmos
níveis desde pelo menos 01/07/2026. Eles não se moveram apesar do
rompimento do ratio hoje — o que é coerente: o ISF já apontava farelo
estruturalmente pressionado há semanas; o ratio cruzando 80% é o preço
finalmente reconhecendo tacitamente essa condição estrutural, não uma
mudança nela.

### O que os índices dizem juntos em 28/07/2026

ISF 80/100 + ISO 100/100 (ambos inalterados) + ratio Far/Soj rompendo para
dentro da zona comprimida pela primeira vez (79,96%) + crush margin no
menor nível da janela, sexta queda seguida (2,7594) + oil share na quarta
queda seguida (52,3%) + oil-meal spread na maior compressão acumulada
(-8,99% hoje, quinta queda seguida) + margem de biodiesel melhorando pelo
segundo dia seguido (+2,28%, divergindo da queda do óleo) + COT parado no
corte de 21/07 (fundos extremamente comprados nas três pernas, posição
ainda não confirmada como desmontada) formam um quadro que **finalmente
converge, pelo menos para o farelo**: a tese estrutural bear (ABIOVE, ISF)
e o gatilho tático (ratio <80%) estão, hoje, alinhados na mesma direção pela
primeira vez desde 11/06. Para soja e óleo, a divergência entre técnico e
fundamento persiste — a soja tecnicamente firme (acima da resistência,
câmbio e papel reforçando juntos) e o óleo tecnicamente fraco mas com
margem de biodiesel em melhora seguem sendo, cada um a seu modo, situações
não resolvidas que dependem do próximo corte do COT (28/07, publicação
~31/07) para ganhar clareza adicional.

---

## Lente fiscal e regulatória BR

**Isenção PIS/Cofins biodiesel — vencimento em 31/07/2026, agora a apenas 3
dias, ainda sem sinalização pública de renovação** (evento
PISCOFINS-BIODIESEL-ISENCAO, `atualizado_em` 2026-06-05, sem mudança desde
então — agora 54 dias sem atualização do monitor). Trata
`trib-PISCOFINS-BIODIESEL-ISENCAO-2026-07-31`, sinalizado pela fila de hoje
com a tag `[3d]`, o vetor tributário de maior prioridade de monitoramento
no momento. **O mecanismo:** a isenção incide na saída do biodiesel; se
expirar sem renovação, o custo tributário efetivo da produção sobe, o que
tende a reduzir a margem de biodiesel doméstica (distinta da margem
americana calculada nesta leitura, que hoje melhorou pelo segundo dia
seguido, mas usa RIN D4 e heating oil dos EUA, não o regime tributário
brasileiro) e, por extensão, pressionar a demanda por óleo de soja como
insumo dentro do mix B15 mandatório — um vetor bearish direto para o óleo
doméstico, independentemente do que acontecer no CBOT ou na margem
americana. Com a decisão devendo sair nos próximos três dias corridos e o
monitor tributário sem qualquer atualização há quase oito semanas, este
segue sendo o vetor de maior prioridade — a divergência entre uma margem
americana em melhora e um risco tributário doméstico crescente é a tensão
fiscal central desta leitura para o óleo.

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L) —
vigência formal venceu há 17 dias (`vigencia_ate` 11/07/2026), sem qualquer
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
biodiesel), em tensão com a crush margin no menor nível da janela — o
alívio tributário é estrutural, o aperto de crush é tático.

**Vetores dos EUA e Indonésia, sem mudança de status desde 2026-06-05:**
EPA-RFS-2026-2027 (volumes recordes de biocombustível, sustentando o RIN
D4 usado na margem de biodiesel, fixo em 2,11 USD/RIN); 45Z-CLEAN-FUEL
(regra que favoreceria óleo de soja doméstico americano); DANANTARA-INDONESIA
(centralização estatal da exportação de palma, plena em 01/09/2026);
INDONESIA-B50 (provável B45 em 2026, B50 pleno só 2027-28);
INDONESIA-LEVY-PMK9 (imposto de exportação de CPO até 12,5%, encarecendo
palma). Conjunto estruturalmente bullish para óleo de soja via substituição
de palma, mas inverificável pelo lado de mercado (MPOB inacessível há 19
dias, ver Honestidade).

**O monitor tributário como um todo está há 54 dias sem qualquer
atualização** — o intervalo cresce exatamente na semana do vencimento da
isenção PIS/Cofins (3 dias). Prioridade máxima de manutenção do sistema,
independentemente da leitura de preço de hoje.

---

## Riscos e eventos próximos

**A isenção PIS/Cofins do biodiesel vence em 31/07/2026, agora a apenas 3
dias**, sem sinalização de renovação — prioridade máxima de monitoramento
até a resolução (fila `trib-PISCOFINS-BIODIESEL-ISENCAO-2026-07-31`).

**O próximo corte do COT (referente a 28/07/2026, publicação normal
~31/07/2026)** é o dado mais aguardado de toda esta janela para as três
pernas — vai mostrar se os fundos que compraram agressivamente na semana de
21/07 (net long +73,6% soja, +57,8% farelo, +11,4% óleo) começaram a
vender, e ganha relevância adicional para o farelo especificamente após o
rompimento do ratio Far/Soj hoje.

**O ratio Far/Soj precisa de mais 2-3 fechamentos abaixo de 80% para
confirmar robustamente o rompimento de hoje** — depois de sete semanas
testando e recuando do piso, um único fechamento em 79,96% ainda pode ser
revertido nas próximas sessões; a sequência dos próximos dias é o teste
mais direto desta leitura.

**O nível de 1.180,00 na soja segue sendo o pivô técnico mais vigiado** —
a mínima de hoje (1.193,00) chegou à distância mais curta já registrada
nesta janela (1,10%), mesmo com o fechamento se afastando do nível.

**O heating oil (HO=F) precisa de uma sessão de volume normal e estável
para ganhar confiança** — depois da revisão de 278 para 23.447 contratos
em 27/07, e do novo print baixo de 788 contratos hoje, esta série de
leituras trata os últimos dois prints com cautela redobrada.

**NOPA — segue inacessível** (fila `release-nopa-2026-07-28` tratada aqui,
sem dado interpretável, apenas nova data de coleta), sem crush americano
confirmado por fonte primária.

**MPOB — sem números de palma extraídos há 19 dias consecutivos**, mantendo
cego o efeito do El Niño e dos vetores regulatórios indonésios sobre o
prêmio de substituição do óleo de soja.

**O WASDE saiu completamente da janela de 14 dias deste briefing** (último
dado 10/07/2026, agora 18 dias) — sem nenhuma linha de WASDE visível nesta
consulta, diferente de leituras anteriores que ainda viam o dado (stale,
mas presente). Monitorar se a próxima atualização do WASDE volta a aparecer
ou se o canal de coleta precisa de atenção.

---

## Honestidade

O que não foi possível validar neste briefing de 28/07/2026, onde a
confiança é baixa ou há lacunas materiais:

**1. Os dados de fechamento de 27/07/2026 foram revisados entre o dump de
ontem e o dump de hoje, e de forma não trivial.** A leitura de 27/07
registrou soja fechando em 1.197,50, farelo em 320,50 e óleo em 70,77
(cts/lb ou USD/sht conforme o caso). O briefing de hoje, ao recalcular os
indicadores para a data de 27/07 (seção `indicators`), cita explicitamente
soja 1.199,75, farelo 320,30 e óleo 70,85 para a mesma sessão — diferenças
de +0,19%, -0,06% e +0,11% respectivamente. Esta leitura optou por usar os
valores REVISADOS (os que aparecem no briefing de hoje) como base de
comparação para todos os deltas de 28/07 calculados acima, por serem a
versão mais atual disponível — mas isso significa que qualquer leitor que
compare esta análise com a de ontem verá pequenas divergências nos "valores
de ontem" citados, que refletem a revisão da fonte, não um erro de cálculo.
Este é o segundo dia seguido em que uma revisão de dados de sessão anterior
é identificada (ver também item 2) — um padrão a monitorar na qualidade da
fonte.

**2. O volume de heating oil de 27/07/2026 foi revisado de 278 para 23.447
contratos** — uma correção de mais de 80 vezes o valor original. A leitura
de ontem havia tratado o print de 278 contratos com ceticismo explícito
("sugere fortemente que o dado... é parcial/incompleto"), e a revisão de
hoje confirma essa suspeita. O print de heating oil de HOJE (788 contratos)
é, por si só, também baixo o suficiente para levantar a mesma dúvida — esta
leitura o trata com a mesma cautela, sem tratá-lo como definitivo até uma
sessão de volume estável confirmar.

**3. O veredito desta leitura — de que o rompimento do ratio Far/Soj para
baixo de 80% confirma taticamente a tese estrutural bear-farelo — é uma
interpretação, não um fato objetivo isolado do briefing.** O dado bruto
(ratio 79,96%, abaixo de 80%) é real e citado com fonte; a conexão entre
esse dado e "confirmação da tese de 11/06" é um julgamento desta análise,
reforçado pelo fato de o próprio sistema ter sinalizado essa transição de
zona na fila de julgamento como o item de maior prioridade do dia. Ainda
assim, um único fechamento abaixo de 80%, depois de sete semanas de testes
sem rompimento, pode ser revertido — a confirmação robusta depende de mais
sessões.

**4. Os volumes de soja e óleo em 27/07/2026 não estão disponíveis nesta
janela de 14 dias do briefing** — a tabela `cme_cbot` desta consulta traz,
para a data de 27/07, apenas as linhas de farelo e heating oil, sem chegar
às linhas de óleo e soja daquele dia (a seção termina antes). Esta leitura
evitou citar os volumes de 27/07 para soja e óleo que apareceram na leitura
anterior, porque, dado o padrão de revisão identificado nos itens 1 e 2
acima, não há garantia de que aqueles valores permaneçam válidos — e não há
como confirmá-los ou desmenti-los a partir deste briefing.

**5. A manchete "North Dakota names new soybean group leaders" (Farm
Progress, 28/07/2026) foi citada apenas como registro de ausência de
conteúdo quantitativo** — não há projeção numérica nem fato de mercado
associado; esta leitura não a usa como driver de nenhuma tese.

**6. O USDA Crop Progress permanece no corte de 26/07/2026 (11%/52%/7%),
sem atualização nova nesta janela** — o próximo corte semanal (esperado por
volta de 02/08) é o dado a acompanhar para ver se a piora marginal
documentada na leitura anterior continua.

**7. O WASDE desapareceu completamente da janela de 14 dias deste
briefing** — a leitura anterior ainda via a linha stale de 10/07/2026 (17
dias de atraso); hoje, com 18 dias de atraso, o dado saiu da janela
rolante de 14 dias e não aparece mais nesta consulta. Isso é esperado
matematicamente (14 dias de janela, 18 dias de atraso), mas remove
completamente a visibilidade sobre farelo (Argentina, Brasil, China
parcial) que ainda existia ontem — nenhuma pergunta de tese que dependa do
WASDE pode ser respondida a partir deste briefing.

**8. NOPA (fila `release-nopa-2026-07-28`) segue com `monthly_status` em
0,0 bool** — mesma barreira de assinatura paga documentada desde meados de
junho, agora com quase oito semanas sem alternativa de dado primário sobre
o esmagamento americano.

**9. Palma malaia (MPOB) segue sem números extraídos, agora por 19 dias
consecutivos com o mesmo conteúdo exato (3.439 caracteres)** — a
persistência do byte count idêntico segue sugerindo, possivelmente, uma
página que não está mais sendo servida com conteúdo atualizado.

**10. O COT (CFTC) segue no corte de 21/07/2026, uma terça-feira — não
cobre nenhuma das duas últimas sessões (27/07 e 28/07)** — o próximo corte
(28/07, publicação normal ~31/07) é o primeiro capaz de capturar a reação
dos fundos aos dois últimos dias de mercado, incluindo o rompimento do
ratio Far/Soj de hoje.

**11. Percentis históricos de COT não calculados** — os números de
21/07/2026 seguem lidos apenas em nível absoluto e como fração do open
interest corrente, sem série histórica completa para calibrar se o
posicionamento estava objetivamente "esticado" no sentido histórico.

**12. Clima INMET (BR) não foi usado como driver de preço desta leitura.**
Julho/agosto é entressafra da soja brasileira (colheita concluída, plantio
só em outubro) — sem relevância direta para a tese de preço neste momento
do calendário agrícola, apesar de o dump trazer previsões detalhadas para
2026-07-29 (chuva isolada em PR/RS, calor seco em MT).

**13. BCBA Argentina — última leitura disponível é 22/07/2026, agora 6
dias sem atualização**, sem relatórios de esmagamento/exportação acessíveis
via scraper.

**14. RIN D4 como parâmetro fixo (2,11 USD/RIN) segue sendo uma fonte
relevante de incerteza do modelo de biodiesel** — a margem de 1,1894
USD/gal calculada hoje, assim como toda a série recente, depende desse
valor fixo, o que significa que os dois dias seguidos de "melhora da
margem" refletem inteiramente a queda do custo do óleo e a estabilidade do
heating oil, não uma mudança no RIN em si.

**15. Os forecasts estatísticos internos (28/07/2026) mantiveram o rótulo
"altista" para as três commodities** — como o modelo usa média móvel de 20
dias + volatilidade + inclinação de curto prazo, ele tende a carregar
inércia da tendência recente e reagir com atraso a mudanças de regime como
o rompimento do ratio Far/Soj de hoje; esta leitura não usa esses
forecasts como argumento de tese, apenas como referência de banda
estatística.

*Nenhum número foi inventado ou estimado além do que consta no briefing de
28/07/2026 e nos insights anteriores referenciados. A contribuição central
desta leitura foi (1) identificar e explicar o rompimento do ratio Far/Soj
para dentro da zona "comprimida" (<80%), conectando-o explicitamente ao
gatilho da tese estrutural bear-farelo aberta em 11/06/2026 e à revisão D+7
vencida; (2) decompor o mecanismo exato desse rompimento — soja subindo
mais rápido que farelo, não o farelo caindo em termos absolutos — algo que
uma leitura só do preço do farelo isoladamente não revelaria; (3)
documentar a divergência entre o ratio Far/Soj (farelo fraco vs. soja) e o
oil-meal spread (farelo forte vs. óleo) na mesma sessão, mostrando que
"farelo bear" não é uma leitura uniforme aplicável a todos os pares; (4)
identificar a revisão retroativa dos dados de 27/07 (preços e,
principalmente, o volume de heating oil de 278 para 23.447 contratos), que
confirma a cautela da leitura anterior e justifica cautela redobrada com o
novo print baixo de hoje (788 contratos); e (5) registrar que o WASDE saiu
completamente da janela de 14 dias do briefing, uma perda de visibilidade
que não existia na leitura de ontem.*
