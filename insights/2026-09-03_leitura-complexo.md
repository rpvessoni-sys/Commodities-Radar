---
data: 2026-09-03
titulo: "Quarta-feira (02/09) devolve o rali: o óleo quebra o suporte de 72,00 e lidera a queda do complexo (-2,64%) enquanto soja e farelo seguram o rompimento técnico, mas o crush aprofunda a compressão para US$ 2,22/bushel — o menor nível da janela, mesmo com a soja mais barata"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT (ZSX26 soja / ZMV26 farelo / ZLV26 óleo) — sessão de 2026-09-02 (quarta-feira), a mais recente do pipeline: soja abertura 1.317,00, máxima 1.324,00, mínima 1.300,00, fechamento 1.308,75 USD cts/bushel, volume 161.746 contratos; farelo abertura 345,00, máxima 347,60, mínima 338,50, fechamento 343,00 USD/short ton, volume 21.369 contratos; óleo abertura 72,31, máxima 72,80, mínima 70,45, fechamento 70,54 USD cts/lb, volume 33.378 contratos. Curva futura em 02/09: soja set/26 (U26) 1.295,50, nov/26 (X26, contrato-base) 1.308,75, jan/27 (F27) 1.323,50, mar/27 (H27) 1.329,00, mai/27 (K27) 1.333,50; farelo set/26 (U26) 339,40, out/26 (V26, contrato-base) 343,00, dez/26 (Z26) 349,90, jan/27 (F27) 352,50, mar/27 (H27) 353,90, mai/27 (K27) 355,10; óleo set/26 (U26) 71,05, out/26 (V26, contrato-base) 70,54, dez/26 (Z26) 70,94, jan/27 (F27) 70,96, mar/27 (H27) 70,96, mai/27 (K27) 70,90
  - CME CBOT — sessão de 2026-09-01 (terça-feira), usada como base de comparação (valores de fechamento hoje reconciliados no dump atual, levemente diferentes dos citados na leitura de ontem por revisão pós-pregão da fonte): soja fechamento 1.317,75, farelo fechamento 345,70, óleo fechamento 72,45 (indicators, 2026-09-01) — a variação de -2,64% do óleo registrada pela fila de julgamento hoje bate exatamente com esses números (70,54 vs 72,45), confirmando que são os corretos para esta leitura
  - CME NYMEX heating oil (HO=F) — 2026-09-02: abertura 4,6572, fechamento 4,6593, máxima 4,6666, mínima 4,6545 USD/galão, volume 309 contratos (baixo, ver Honestidade); referência implícita de 09-01 via indicators: ~4,68 USD/galão (receita biodiesel 7,84 = HO + 1,5×RIN 2,11)
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, paridade BR, ISF, ISO) — 2026-09-02 e 2026-09-01, usados para reconstruir a trajetória do dia
  - BCB PTAX — 2026-09-02: USD/BRL 5,1273, EUR/BRL 5,9436, Selic diária 0,05166% a.a.; 2026-09-01: USD/BRL 5,1570 — quarta sessão seguida de valorização do real (5,2005 em 28/08 → 5,1816 em 31/08 → 5,1570 em 01/09 → 5,1273 em 02/09)
  - CEPEA/ESALQ Soja Paranaguá via NAG — 2026-09-02: R$ 160,99/saca (var -0,09%); 2026-09-01: R$ 161,14 (var +1,07%)
  - CEPEA/ESALQ Soja Paraná interior via NAG — 2026-09-02: R$ 152,61/saca (var -0,29%); 2026-09-01: R$ 153,06 (var +1,16%)
  - NAG Físico BR — 2026-09-02: farelo MT/IMEA R$ 1.795,68/ton (var 0,0%, congelado desde 31/08), Rondonópolis/MT R$ 1.900,00/ton (var 0,0%, congelado desde 31/08), RS média R$ 1.860,00/ton (congelada há várias sessões); prêmios export PGUA farelo +0,12 USD/short ton e óleo +0,10 cts/lb, ambos sob rótulo "Setembro/26", mesmo valor idêntico desde 24/08/2026 — agora 9 dias corridos sem se mexer, ver Honestidade
  - CFTC COT Managed Money, Swap Dealers e Producer/Merchant — corte de 2026-08-25, AINDA o mais recente disponível (nenhum corte novo neste dump); 8 dias corridos de defasagem frente ao fechamento de 02/09
  - USDA Crop Progress — corte de 2026-08-30 (12% excelente / 46% boa / 9% ruim), sem atualização nova nesta janela frente à leitura anterior
  - USDA WASDE — segue ausente da janela deste briefing
  - NOPA — fila `release-nopa-2026-09-02` marca novo "release", mas `monthly_status` segue em 0,0 bool (paywall), sem número de esmagamento americano mensal — segundo falso positivo seguido, ver Honestidade
  - ABIOVE projeções mensais — balanços set-dez/2026, mesmos valores da leitura anterior
  - NOAA CPC ENSO — carimbo 2026-09-02 (El Niño Advisory, inalterado)
  - MPOB — carimbo 2026-09-02 (3.456 caracteres, parser sem números extraídos, mesma barreira)
  - BCBA (Argentina) — carimbo 2026-09-02, scraper acessa a página mas não encontra links de relatório detectados
  - INMET — previsão para 2026-09-02: núcleo produtor de Mato Grosso segue quente (35°C em Cuiabá, 39°C em Sinop/Lucas do Rio Verde, 38°C em Sorriso, 34°C em Rio Verde/GO) com "pancadas de chuva isoladas" — mesmo padrão já descrito na leitura anterior; Sul com céu aberto (Cascavel/PR 24°C/11°C, Maringá/PR 26°C/12°C, Passo Fundo/RS 20°C/7°C, todos "poucas nuvens") — sem previsão mais recente (03/09) disponível neste dump
  - Notícias Agrícolas/Canal Rural + FarmProgress RSS — 2026-09-02: "160 items lidos, 8 mantidos (soja/farelo/oleo)", único headline com texto legível: soja — "Nebraska FFA vice president gives soybean update" (FarmProgress), sem conteúdo de mercado relevante — ver Honestidade sobre os outros 7 itens "mantidos" sem headline exposto
  - Forecasts estatísticos internos (bandas 7d/30d, MA20+volatilidade+slope) — geração de 2026-09-02, alvos 09/09 (7d) e 02/10 (30d); viés "altista" em soja, farelo e óleo nos dois horizontes — ver Honestidade sobre a defasagem entre este forecast (calculado ANTES do fechamento de hoje) e o próprio fechamento de queda de 02/09
  - system/tributario_watch.toml (lido como referência, não editado) — `atualizado_em` 2026-06-05 em todos os eventos, agora **90 dias sem revisão**
  - Fila de julgamento — carimbada 2026-09-02 no briefing, 8 itens; tratados nesta leitura: `alerta-quebra_resistencia-soja_cbot-2026-09-02`, `alerta-quebra_suporte-oleo_cbot-2026-09-02`, `alerta-movimento_forte-oleo_cbot-2026-09-02`, `alerta-quebra_resistencia-farelo_cbot-2026-09-02`, `alerta-quebra_suporte-complexo_soja-2026-09-02`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, `release-nopa-2026-09-02`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`
  - Cruza com [[2026-09-02_leitura-complexo]] (leitura de ontem, que classificava o rompimento das três pernas como "confirmado" e o óleo como tendo finalmente resolvido sua divergência a favor do lado comprado — teste que a sessão de hoje reabre parcialmente)
status: ativa
vies: [bull-soja, bull-farelo, bear-oleo_soja]
---

## Visão geral

Hoje é quinta-feira, 03/09/2026, e o briefing mais recente traz o fechamento de
quarta-feira (02/09) — e essa sessão faz exatamente o oposto do que a leitura de ontem
descrevia como "rompimento confirmado". Depois de duas sessões seguidas de alta sincronizada
(28/08 e 01/09), o complexo inteiro devolveu parte do ganho: soja caiu **-0,68%** (de
1.317,75 para 1.308,75 USD cts/bushel), farelo caiu **-0,78%** (de 345,70 para 343,00 USD/
short ton) e o óleo caiu **-2,64%** (de 72,45 para 70,54 USD cts/lb) — a queda mais forte do
dia em qualquer perna do complexo nesta janela de 14 dias, e grande o suficiente para a fila
de julgamento disparar um alerta específico de "movimento forte"
(`alerta-movimento_forte-oleo_cbot-2026-09-02`).

Para quem não acompanha o complexo diariamente: a soja em grão vira, na esmagadora
(crush), dois produtos com demandas diferentes — farelo (proteína para ração animal) e óleo
(alimentação humana e biodiesel). O **crush margin** mede, em dólares por bushel (~27,2 kg de
soja), quanto sobra para quem esmaga depois de vender farelo + óleo e pagar a soja. Dentro
desse crush, o **oil share** (fatia do valor total que vem do óleo) diz qual dos dois produtos
está "mandando" no resultado econômico da esmagadora; o **ratio Far/Soj** mede se o farelo
está caro ou barato EM RELAÇÃO à soja, não em valor absoluto. A mecânica de hoje é didática
porque ilustra bem essa relação: a soja (matéria-prima) ficou mais barata, o que DEVERIA
melhorar o crush isoladamente — mas farelo e óleo (os produtos) caíram proporcionalmente
mais, sobretudo o óleo, então o crush pagou o preço do lado errado. O crush margin fechou em
**US$ 2,2179/bushel** (indicators, 02/09: Board Crush farelo 343,00 + óleo 70,54 − soja
1.308,75), o menor nível de toda a janela de 14 dias do briefing e uma queda de -7,5% frente
aos US$ 2,3974/bushel de ontem — a terceira sessão seguida abaixo do referencial de US$ 2,50
monitorado pela fila (`alerta-quebra_suporte-complexo_soja-2026-09-02`), e desta vez a
compressão não é mais compatível com a leitura de ontem ("a soja sobe mais rápido que os
produtos"): hoje a soja caiu, e o crush comprimiu mesmo assim, porque o óleo caiu ainda mais
rápido. Isso muda o diagnóstico: o crush não está simplesmente "perseguindo" a soja, ele tem
uma fragilidade estrutural própria, hoje evidenciada pelo colapso do óleo.

Tecnicamente, o quadro é misto e vale a pena separar por perna. Soja e farelo caíram no dia,
mas SEGUEM acima dos níveis de resistência que romperam na semana passada (1.180,00 e 325,00
respectivamente) — a fila voltou a disparar os dois alertas de rompimento hoje
(`alerta-quebra_resistencia-soja_cbot-2026-09-02` e
`alerta-quebra_resistencia-farelo_cbot-2026-09-02`) simplesmente porque o preço continua
estruturalmente acima desses patamares, não porque houve um novo rompimento — é a estrutura
de alta se mantendo, apenas com a primeira sessão de recuo depois do rali. O óleo é outra
história: fechou em 70,54, ABAIXO do suporte técnico de 72,00
(`alerta-quebra_suporte-oleo_cbot-2026-09-02`), devolvendo integralmente a reconquista que a
leitura de ontem tratou como o principal fato novo e positivo da semana. **Leitura de uma
linha**: o pivô do complexo continua sendo a soja em termos de tendência geral (ela ainda
segura o rompimento), mas o evento mais importante de hoje é o colapso do óleo — ele reabre a
divergência antiga (estrutura técnica quebrada vs. margem de biodiesel sustentada) que
parecia resolvida ontem — e o nível de confiança recua de médio-alto para **médio**, porque o
complexo mostrou pela primeira vez nesta janela que a alta das três pernas junta pode reverter
com a mesma rapidez com que apareceu.

## Soja

**Viés: bull, moderado — primeira sessão de recuo depois do rali, mas o rompimento técnico
segue de pé com folga, câmbio e crush são os dois pontos de atenção novos.**

O que sustenta a tese:

- **O rompimento técnico de 1.180,00 segue confirmado, mesmo com o recuo do dia.** Soja CBOT
  fechou em 1.308,75 USD cts/bushel em 02/09/2026 (CME CBOT), 10,9% acima da resistência de
  1.180,00 monitorada pela fila (`alerta-quebra_resistencia-soja_cbot-2026-09-02`) — uma folga
  ligeiramente menor que os 11,7% de ontem, mas ainda uma distância grande de segurança. O
  mecanismo: uma queda de -0,68% depois de um rali de +2,37% no dia anterior é, em termos
  proporcionais, um recuo pequeno — do tipo que se espera ver dentro de uma tendência de alta
  saudável (realização de lucro parcial), não o tipo de reversão de -3% ou mais que costuma
  preceder uma virada de tendência.
- **Volume da sessão de queda foi robusto, mas menor que o da sessão de rali.** 161.746
  contratos em 02/09, ante 175.695 em 01/09 (CME CBOT) — o mercado negociou volume relevante na
  queda, mas não superou o volume do dia de alta que confirmou o rompimento; um sinal
  neutro-a-levemente-positivo para quem está comprado, porque a "prova de força" da venda de
  hoje foi mais fraca que a prova de força da compra de ontem.
- **Curva futura segue em contango crescente**, agora nov/26 (X26, contrato-base) 1.308,75 →
  jan/27 (F27) 1.323,50 → mar/27 (H27) 1.329,00 → mai/27 (K27) 1.333,50 (CME CBOT, 02/09) — a
  estrutura de prêmio crescente ao longo da curva não se desfez com o recuo do dia, reforçando
  que o mercado trata a queda como ajuste pontual, não como mudança de regime.
- **Físico brasileiro no porto resistiu MUITO melhor do que o papel.** CEPEA/ESALQ Soja
  Paranaguá (via NAG) fechou 02/09 em R$ 160,99/saca, praticamente estável (-0,09% sobre
  01/09), enquanto a paridade CBOT-implícita em reais recuou -1,25% (de R$ 149,82 para R$
  147,94/saca, indicators — CBOT 1.308,75 × USD/BRL 5,1273). O mecanismo: quando o físico no
  porto não acompanha a queda do papel na mesma proporção, o basis (diferença entre preço físico
  e paridade) se ALARGA — foi de R$ 11,32/saca (7,55%) em 01/09 para **R$ 13,05/saca (8,82%)**
  em 02/09, o maior nível desta janela. Isso é evidência de que o mercado físico exportador
  segue mais apertado do que o CBOT sozinho sugere, e que o recuo de hoje é, em boa parte, um
  fenômeno de papel (futuros), não necessariamente de oferta física real no porto.

**O que invalida / risco:**

- **Câmbio: quarta sessão seguida de valorização do real, agora comendo mais do ganho do que
  antes.** USD/BRL fechou 02/09 em 5,1273 (BCB PTAX), -0,58% sobre 01/09 (5,1570) — a quarta
  queda seguida (5,2005 em 28/08 → 5,1816 em 31/08 → 5,1570 em 01/09 → 5,1273 em 02/09, -1,41%
  acumulado). O mecanismo, reforçado hoje: quando o CBOT cai E o real se valoriza ao mesmo
  tempo, os dois efeitos se somam contra o produtor brasileiro em vez de se compensarem — é
  exatamente o oposto do padrão observado durante o rali (quando o real valorizando "roubava"
  só uma fração do ganho em dólar). Hoje a paridade em reais caiu quase o dobro, em termos
  proporcionais, da queda do CBOT em dólar (-1,25% vs -0,68%).
- **O COT segue cego para toda a semana do rali E agora também para a reversão de hoje.** O
  corte de 25/08/2026 (Commodity Futures Trading Commission) — ainda o mais recente — mostrava
  managed money com net long de 200.679 contratos, mas não enxerga nenhuma das seis sessões
  entre 27/08 e 02/09 (rali + reversão). O hiato chegou a 8 dias corridos. O próximo corte
  (posições de terça 01/09, publicação estimada por volta de sexta 04/09 pelo calendário
  semanal do CFTC — inferência, não confirmada no briefing) só vai revelar o posicionamento até
  a véspera da queda de hoje, não a reação dos fundos a ela.
- **O crush margin caiu para o menor nível da janela (US$ 2,2179/bushel) mesmo com a soja mais
  barata** — isso é, por definição, o mercado dizendo que o valor agregado de farelo + óleo
  caiu proporcionalmente mais que a soja. Se essa dinâmica persistir, esmagadoras enfrentam
  margem cada vez mais apertada e podem reduzir ritmo de moagem, o que eventualmente reduz a
  demanda física por soja — um freio de médio prazo à própria tese de alta da soja, ainda que
  não seja um sinal de curto prazo.
- **Nível técnico a vigiar:** um fechamento de volta abaixo de 1.180 desfaria o rompimento; a
  distância de segurança (10,9%) ainda é grande, mas encolheu levemente frente aos 11,7% de
  ontem.

**Leitura operacional:** a estrutura de alta segue intacta — o recuo de hoje, isolado, não é
suficiente para abandonar a tese compradora no rompimento, e o basis físico alargando é um
argumento adicional de que a queda é mais de papel do que de oferta real. Ainda assim, é a
primeira vez nesta sequência de leituras que soja, farelo E óleo caem juntos no mesmo pregão —
quem está comprado deve tratar hoje como o primeiro teste real de quão sólido é o rompimento
(o stop técnico em 1.180, ou um nível intermediário como 1.288 — mínima do pregão de pausa de
segunda — continua sendo a referência de proteção). Quem quer montar posição vendida contra o
movimento ainda não tem confirmação técnica de reversão em soja isoladamente (isso exigiria
pelo menos uma sessão de queda mais forte, com volume maior que o de alta), mas ganhou hoje um
argumento novo e concreto: o crush no menor nível da janela é o primeiro sinal de que o
mercado físico de esmagamento pode começar a resistir ao nível de preço da soja relativamente
a seus produtos.

## Farelo

**Viés: bull, moderado — segue acima do rompimento técnico, mas a revisão D+7 da tese de
ratio venceu sem convergência, e a D+90 chega em uma semana.**

O que sustenta a tese (na fita):

- **Rompimento de resistência ainda de pé.** Farelo CBOT fechou em 343,00 USD/short ton em
  02/09/2026, 5,5% acima da resistência de 325,00 (`alerta-quebra_resistencia-farelo_cbot-2026-09-02`)
  — a folga encolheu de 6,2% (ontem) para 5,5% hoje, a queda de -0,78% (de 345,70 para 343,00)
  corroeu parte, mas não todo, o colchão de segurança.
- **Curva futura segue em contango crescente**, de 339,40 (set/26) a 355,10 (mai/27, +4,6%
  entre pontas) — estrutura de firmeza sustentada intacta apesar do recuo do dia.
- **Físico brasileiro permanece congelado no patamar mais alto**, sem repasse de queda:
  farelo MT/IMEA (NAG) em R$ 1.795,68/ton e Rondonópolis/MT em R$ 1.900,00/ton, ambos
  congelados desde 31/08 — o físico local não reagiu à queda do CBOT de hoje, o que é
  compatível com o mesmo padrão observado em soja (o recuo é mais um fenômeno de papel do que
  de oferta física local).

O que tensiona a tese (a estrutura relativa segue não convergindo):

- **O ratio Far/Soj caiu novamente, quarta sessão seguida de recuo.** Fechou em 78,62% em
  02/09 (indicators), abaixo dos 78,70% de ontem, que por sua vez já era abaixo dos 78,87% de
  31/08 e dos 79,77% de 28/08 — uma sequência ininterrupta de queda desde o fim de agosto. O
  mecanismo, hoje na direção oposta de ontem: farelo caiu -0,78% no dia, soja caiu -0,68% — como
  o ratio mede farelo relativo à soja, o farelo caindo PROPORCIONALMENTE MAIS que a soja também
  empurra o ratio para baixo, mesmo em dia de queda geral. Ou seja: seja em dia de alta (ontem,
  soja subindo mais rápido) ou em dia de queda (hoje, farelo caindo mais rápido), o resultado
  líquido tem sido o mesmo nas últimas quatro sessões — o ratio segue caindo, o que é a marca de
  um farelo estruturalmente mais fraco que a soja em qualquer direção de mercado.
- **O ISF (Índice de Sobra de Farelo) segue travado em 80/100** (4 de 5 condições estruturais
  apontando pressão baixista), sem nenhuma sessão de melhora em toda a janela do briefing.
- **Prêmio de exportação em Paranaguá congelado em +0,12 USD/short ton desde 24/08/2026** —
  agora 9 dias corridos sem se mexer, mesmo com o board tendo subido e caído com força nesse
  intervalo.

**Trata a fila `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
(marcada 🔴 VENCIDA no briefing de hoje):** a tese original de 11/06/2026 previa convergência
do ratio Far/Soj para a zona 80-87% ("apertado") num horizonte de dias (D+7). Essa janela de
revisão venceu sem que a convergência tenha ocorrido — pelo contrário, o ratio está mais longe
da zona-alvo hoje (78,62%) do que estava há uma semana. São **84 dias corridos** desde o
alerta original (11/06 a 02/09), contra os "dias" que a tese original supunha. Mantendo o
registro já feito em [[2026-09-02_leitura-complexo]] e [[2026-08-31_leitura-complexo]]: a tese
segue "revisada, não encerrada" — o preço absoluto do farelo subiu bastante desde junho
(~303,60 USD/sht em 10/06 para 343,00 hoje, +13,0%), mas o ratio relativo nunca convergiu, e
hoje se afasta ainda mais. **A fila também traz a revisão D+90 da mesma tese
(`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`), vencendo em
2026-09-09 — daqui a 7 dias.** Esse é o próximo marco formal para decidir se a tese de
convergência do ratio deve ser encerrada de vez ou se ainda há espaço para revisão; com a
tendência atual (quarta sessão seguida de queda do ratio, agora se afastando e não convergindo),
a leitura de hoje é cética quanto a uma virada a tempo do D+90.

**O que invalida / risco:** o padrão "ratio cai independentemente da direção do board" é, na
prática, o mercado dizendo que o farelo é sistematicamente o lado mais fraco do par farelo/soja
— tanto para cima (farelo sobe menos que a soja) quanto para baixo (farelo cai mais que a
soja). Isso é uma leitura estrutural mais forte contra a tese de reversão do ratio do que
qualquer sessão isolada.

**Leitura operacional:** o rompimento técnico direcional em farelo segue válido e sustenta
posições compradas simples, mas para quem opera o spread Far/Soj (long farelo / short soja
apostando em reversão do ratio) a sessão de hoje reforça, pela quinta vez consecutiva contando
desde 28/08, que o timing de entrada não chegou — o ratio não dá sinal de fundo, e o
vencimento da revisão D+7 sem convergência, com a D+90 batendo à porta em uma semana, é motivo
concreto para não montar essa posição de forma agressiva antes de 09/09.

## Óleo

**Viés: bear, moderado — o suporte técnico de 72,00 quebrou de volta, com a maior queda
percentual do complexo no dia, mesmo com a margem de biodiesel melhorando por conta do custo
mais barato da matéria-prima.**

O que sustenta o lado vendido / cético:

- **Quebra de suporte confirmada, com o maior movimento do dia em qualquer perna do
  complexo.** Óleo CBOT fechou em 70,54 USD cts/lb em 02/09/2026, -2,64% sobre 01/09 (72,45) —
  variação grande o suficiente para acionar o alerta específico de "movimento forte" da fila
  (`alerta-movimento_forte-oleo_cbot-2026-09-02`), e o fechamento ficou abaixo do pivô técnico
  de 72,00 (`alerta-quebra_suporte-oleo_cbot-2026-09-02`) que a leitura de ontem tratava como
  reconquistado. A mínima do dia, 70,45, ficou bem abaixo até do fechamento de ontem — a queda
  não foi um gap pontual na abertura, ela se aprofundou ao longo do pregão (abertura 72,31 →
  mínima 70,45).
- **Volume elevado na queda** — 33.378 contratos, o segundo maior volume de óleo desta janela
  (atrás apenas do próprio dia de rompimento) — o que dá mais credibilidade técnica à quebra do
  que se tivesse ocorrido em volume fino.
- **O oil-meal spread (valor do óleo menos valor do farelo dentro do crush, em USD/bushel)
  despencou, revertendo quatro sessões seguidas de alta.** Caiu de 0,3641 (01/09) para
  **0,2134 (02/09)**, -41,4% em uma sessão — depois de subir de 0,1485 (27/08) para 0,3696
  (01/09, pico da janela). O mecanismo: o óleo estava "vencendo" o farelo dentro do crush a
  cada sessão desde 27/08; hoje essa dinâmica inverteu com força, e é o próprio recuo do oil
  share (ver seção de Spreads) que confirma a perda de espaço relativo do óleo.
- **Curva futura segue praticamente achatada, e agora com backwardation no front.** Set/26
  (U26) 71,05 > out/26 (V26, contrato-base) 70,54 — o vencimento mais próximo do vencimento-base
  está mais caro que o próprio contrato-base, um sinal técnico de fraqueza de curto prazo (o
  mercado não está descontando o preço à vista tanto quanto descontou o contrato corrente na
  queda de hoje). Os vencimentos mais distantes seguem estáveis (dez/26 70,94 → jan/27 70,96 →
  mar/27 70,96 → mai/27 70,90) — o mercado trata a fraqueza como concentrada no curto prazo, não
  como reprecificação estrutural de longo prazo.

O que ainda sustenta o lado comprado / a cautela contra vender:

- **A margem de biodiesel americana MELHOROU, não piorou, apesar da queda do preço do óleo —
  e o mecanismo importa.** Margem de 1,7338 USD/galão em 02/09, ante 1,6086 em 01/09
  (indicators), alta de +7,8%. A receita (heating oil + 1,5× valor do crédito RIN D4) caiu
  ligeiramente: de ~7,84 USD/galão (01/09, HO ~4,68) para 7,8243 (02/09, HO 4,66 cts implícito
  no cálculo — CME NYMEX HO=F fechou 02/09 em 4,6593 USD/galão, -0,4% sobre a referência de
  ontem). O custo, porém, caiu MUITO mais: de 6,23 USD/galão (01/09, óleo a 5,43 USD/galão
  equivalente) para 6,09 (02/09, óleo a 5,29) — uma queda de -2,2% no custo, quase seis vezes
  maior, em pontos percentuais, que a queda da receita. Ou seja: o RIN D4 ficou estável (1,5×RIN
  = 2,11 USD/galão em ambos os dias) e o heating oil quase não se mexeu — foi o próprio colapso
  do preço do óleo que abaratou o custo do biodiesel e, paradoxalmente, melhorou a margem do
  produtor. Isso é economicamente relevante: margem mais larga é incentivo a mais blending, o
  que sustenta demanda física por óleo de soja mesmo com o preço em queda — um amortecedor de
  médio prazo, não um sinal contra a queda de curto prazo.
- **ISO (Índice de Suporte do Óleo) segue travado em 100/100**, sem nenhuma sessão de
  enfraquecimento — o índice não reagiu à queda de hoje porque suas condições estruturais (entre
  elas, oil share ainda acima de 50%) continuam intactas; é um lembrete de que esse índice mede
  condições de fundo, não timing de preço (ver Honestidade).
- **Catalisador regulatório (Danantara) segue pendente de confirmação, não invalidado.** O
  marco-alvo de assunção plena da centralização da exportação de palma pela Indonésia
  (`DANANTARA-INDONESIA`, tributario_watch.toml) era 01/09/2026 — já passou há dois dias — mas
  nenhuma notícia neste dump confirma execução real. Segue como catalisador de alta represado,
  sem relação direta com a queda técnica de hoje.

**O que invalida / risco:** para o lado vendido, a melhora da margem de biodiesel é o principal
contra-argumento — se ela continuar se ampliando, a demanda física por óleo tende a aumentar e
pode conter a queda antes que ela se estenda. Para o lado comprado (quem ainda segura a tese de
ontem), o nível a vigiar agora é se o óleo consegue reconquistar 72,00 rapidamente (como fez
entre 28/08 e 01/09) ou se a quebra de hoje vira um padrão — um fechamento adicional abaixo de
70,45 (mínima de hoje) sem reação técnica reforçaria a leitura bear.

**Leitura operacional:** a sessão de hoje devolve o óleo à situação de divergência que marcava
as leituras anteriores a 01/09 — preço tecnicamente fraco, mas fundamento de margem
relativamente favorável — só que agora com o sinal invertido em relação a antes (antes era ISO
alto + margem comprimindo; hoje é ISO alto + margem melhorando + preço quebrando suporte). Para
quem opera direcional, o rompimento de suporte com volume alto é um argumento técnico real a
favor do lado vendido no curtíssimo prazo, mas o tamanho de posição deveria ser moderado dado
que o motor de fundo (margem de biodiesel, RIN D4 estável) não está deteriorando — é mais
compatível com um repique técnico dentro de um viés de fundo ainda não claramente bear do que
com o início de uma tendência de baixa estrutural. Para quem opera o crush/oil share, a queda
do oil-meal spread hoje (-41,4%) é um sinal de que a "aposta no óleo dentro do complexo" perdeu
força relativa nesta sessão especificamente, depois de quatro sessões ganhando espaço.

## Spreads e crush (leitura de complexo)

A leitura de hoje inverte, ao menos parcialmente, o padrão que vinha se consolidando desde
27/08. O oil share (fatia do valor do crush que vem do óleo) recuou de 51,17% (01/09) para
**50,70% (02/09)** — ainda acima de 50%, ou seja, o óleo continua "mandando" no crush por essa
métrica, mas perdendo terreno pela primeira vez desde 27/08. O oil-meal spread confirma com
mais força: caiu -41,4% no dia (0,3641 → 0,2134 USD/bushel), revertendo quatro sessões seguidas
de alta. Ao mesmo tempo, o ratio Far/Soj também caiu (78,70% → 78,62%) — ou seja, farelo e óleo
perderam valor relativo ao mesmo tempo hoje, o que só é aritmeticamente possível porque a soja
(o denominador comum dos dois indicadores) caiu MENOS, proporcionalmente, do que qualquer um
dos dois produtos. Essa é a peça central da leitura de hoje: numa sessão de queda generalizada,
a soja foi relativamente a mais "resiliente" das três pernas (-0,68%), o farelo ficou no meio
(-0,78%) e o óleo foi de longe o mais fraco (-2,64%) — o inverso exato da hierarquia observada
no rali de 01/09, quando a soja liderava a alta.

O crush margin sintetiza esse desequilíbrio: US$ 2,2179/bushel (02/09), -7,5% sobre os US$
2,3974 de ontem e o menor valor de toda a janela de 14 dias — a TERCEIRA sessão seguida abaixo
do referencial de US$ 2,50 (`alerta-quebra_suporte-complexo_soja-2026-09-02`), mas a primeira
em que a compressão não pode ser explicada pela soja subindo mais rápido que os produtos (ontem
e anteontem, sim; hoje, não — a soja caiu). A única explicação consistente com os números é que
farelo e óleo, juntos, perderam mais valor absoluto do que a soja perdeu — puxados
principalmente pelo colapso do óleo. Os índices sintéticos (ISF 80, ISO 100) permanecem
travados nos mesmos valores de toda a janela — nem a alta de 01/09 nem a queda de 02/09
moveram esses índices um único ponto, reforçando que eles captam condições estruturais de baixa
frequência (thresholds binários), não a dinâmica intradiária de preço — uma limitação a ter em
mente sempre que se usa ISF/ISO como sinal de timing, e especialmente relevante hoje, quando o
preço do óleo se moveu -2,64% sem qualquer reação do ISO.

Para quem opera o crush diretamente: a tese de "crush melhora com o rali" já havia falhado
ontem (crush comprimiu com o board em alta); hoje ela falha de novo, mas por um motivo
diferente e mais preocupante — o crush comprime mesmo com o board em queda, o que descarta a
hipótese simples de "a soja está descolada dos produtos" e aponta para uma fraqueza mais ampla
no valor agregado de farelo + óleo frente à soja, independente da direção do dia. Para quem
opera o spread Far/Soj, a compressão do ratio abaixo de 80% já dura pelo menos 10 sessões (desde
24/08) e hoje voltou a se aprofundar (78,62%, o menor nível da janela) — reforça a leitura de
zona de acumulação sem sinal de reversão, agora com a revisão D+7 da tese original vencida sem
convergência (ver seção Farelo) e a D+90 batendo em uma semana (09/09).

## Lente fiscal/regulatoria BR

Antes de fechar qualquer tese de preço BR, os vetores tributários/regulatórios vivos que pesam
no complexo — todos do `system/tributario_watch.toml`, cujo carimbo mais recente
(`atualizado_em`) em TODOS os eventos é 2026-06-05, ou seja, **90 dias sem revisão** (mais um
dia de defasagem acumulada desde a leitura de ontem):

- **MP 1.363/2026** (id `MP-1363-2026`, subvenção diesel fóssil R$ 1,12/L, vigente até
  31/12/2026): barateia o diesel fóssil no mix B15, reduzindo a competitividade relativa do
  biodiesel e a demanda doméstica por óleo de soja — vetor de baixa para óleo, sem mudança de
  status. Vale notar que esse vetor de baixa estrutural convive, na prática, com a margem de
  biodiesel AMERICANA subindo hoje — são mercados diferentes (subsídio fóssil é BR, margem de
  biodiesel calculada aqui é referência EUA), e não devem ser confundidos ao ler a tese de óleo.
- **B16 (id `B16-CNPE-2026`, elevação da mistura de biodiesel para 16%)** segue "adiado" —
  resultado dos testes técnicos esperado por volta de novembro/2026. Upside represado (~436 mil
  toneladas de demanda potencial adicional de óleo), não corrente.
- **Isenção de PIS/Cofins do biodiesel na mistura** (id `PISCOFINS-BIODIESEL-ISENCAO`): o TOML
  registra vigência ATÉ 31/07/2026 — já **34 dias corridos vencida** frente a 02/09/2026, sem
  qualquer registro de prorrogação ou expiração no arquivo.
- **MP 1.358/2026** (subvenção gasolina R$ 0,89/L): vigência registrada até 11/07/2026, agora
  **54 dias corridos vencida**, mesma lacuna de informação sobre renovação.
- **STJ REsp 2.165.276** (id `STJ-RESP-2165276`, crédito de PIS/Cofins sobre soja em biodiesel,
  vigente, direção "alta" para soja/óleo): alívio de custo pontual, não vinculante.
- **EPA RFS 2026/2027** (id `EPA-RFS-2026-2027`, mandato de biocombustível americano, vigente
  desde 15/06/2026, direção "alta" para óleo): sustenta o RIN D4, que hoje ficou estável em
  1,5×RIN = 2,11 USD/galão — o arcabouço regulatório continua intacto e é parte do motivo pelo
  qual a receita do biodiesel não caiu junto com o preço do óleo.
- **Crédito 45Z** (id `45Z-CLEAN-FUEL`, em tramitação, direção "mista"): sem novidade nesta
  janela.
- **Indonésia — Danantara** (id `DANANTARA-INDONESIA`) e **levy de exportação PMK 9/2026** (id
  `INDONESIA-LEVY-PMK9`): já tratados na seção Óleo. O marco-alvo da Danantara (01/09) já passou
  há dois dias sem confirmação de execução no briefing — segue pendente, não invalidado.

## Riscos e eventos próximos

- **Próximo corte CFTC COT** — posições de terça 01/09, publicação estimada por volta de sexta
  04/09 pelo calendário semanal do CFTC (inferência, não confirmada no briefing): revela o
  posicionamento até a véspera da reversão de hoje, mas ainda não a reação dos fundos à própria
  queda de 02/09 — essa só aparecerá no corte seguinte.
- **Revisão D+90 da tese do ratio Far/Soj** (`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`),
  vencendo em **2026-09-09**, daqui a 7 dias — marco formal para decidir se a tese de
  convergência do ratio para a zona 80-87% deve ser encerrada.
- **Confirmação (ou não) da centralização plena da exportação de palma pela Danantara** —
  marco-alvo era 01/09, já passou há dois dias; vigiar notícia confirmando execução ou, como no
  precedente do B50 indonésio (`INDONESIA-B50`), sinal de atraso.
- **NOPA mensal** (`release-nopa-2026-09-02`): segundo dia seguido em que a fila sinaliza
  "release novo" sem que o conteúdo (`monthly_status` 0,0 bool, paywall) traga qualquer número
  real de esmagamento americano.
- **USDA WASDE**: ausente da janela há bastante tempo; catalisador potencial de revisão de
  balanço mundial.
- **USDA Crop Progress semanal**: próximo corte normalmente segunda-feira à tarde (horário EUA)
  — atualizaria o dado de 30/08 (12%/46%/9%), primeiro sinal de deterioração da safra "boa" em
  semanas.
- **Vigência da isenção PIS/Cofins do biodiesel** (34 dias vencida) e **MP 1.358/2026 da
  gasolina** (54 dias vencida) — checar notícia de renovação/expiração antes de assumir qualquer
  tese de custo de combustível BR.
- **Reação do óleo ao nível de 72,00**: se reconquistar rapidamente (como fez entre 28/08 e
  01/09), a leitura bear de hoje perde força; se romper mais fundo (abaixo de 70,45, mínima de
  hoje), reforça um padrão de fraqueza técnica persistente.
- **Confirmação (ou reversão) da leve queda do heating oil de hoje** — sessão de volume ainda
  baixo (309 contratos); junto com o RIN D4 estável, é a peça que sustenta a melhora da margem
  de biodiesel apesar da queda do óleo.
- **Clima**: previsão de 02/09 (mais recente disponível) mostra o núcleo produtor de Mato Grosso
  ainda recebendo "pancadas de chuva isoladas" e calor extremo (35-39°C); sem previsão mais
  recente (03/09) neste dump para confirmar continuidade do padrão às vésperas da janela de
  plantio da safra 2026/27.

## Honestidade

- **A leitura de ontem classificava o rompimento como "confirmado" com confiança médio-alta; a
  sessão de hoje mostra que essa confirmação não elimina o risco de reversão rápida — o
  complexo caiu como um todo pela primeira vez desde 27/08.** Isso não invalida a tese de
  rompimento em soja e farelo (ambos seguem acima dos níveis técnicos), mas é um lembrete
  explícito de que "teste bem-sucedido" (linguagem usada ontem) não é sinônimo de "sem risco de
  recuo" — e o óleo, especificamente, devolveu o "fato novo e positivo" que ontem foi tratado
  como o principal ponto de virada da semana.
- **Os valores de fechamento de 01/09 citados nesta leitura (soja 1.317,75 / farelo 345,70 /
  óleo 72,45) diferem ligeiramente dos citados na leitura de ontem (1.318,50 / 345,10 / 72,38).**
  A fila de julgamento de hoje calcula a variação do óleo em -2,64%, o que só bate exatamente
  com a base 72,45 (não 72,38) — sinal de que a fonte revisou os números de fechamento de 01/09
  após o pregão (comum em dados de mercado que se firmam horas depois do fechamento nominal).
  Esta leitura usa os valores atuais do dump (mais recentes e reconciliados com a fila), não os
  citados ontem — nenhum número foi inventado, apenas reconciliado com a fonte mais atual.
- **Heating oil com volume ainda baixo (309 contratos) na sessão que sustenta parte da tese de
  margem de biodiesel de hoje** — mesma ressalva já feita ontem (466 contratos); o número
  merece confirmação em mais sessões antes de ser tratado como sinal robusto, especialmente
  porque hoje ele mal se moveu (-0,4%), o que é consistente com baixa liquidez ou com
  estabilidade real — não dá para distinguir as duas coisas só com este dado.
- **`noticias_rss` registra "8 mantidos" em 02/09, mas apenas 1 headline aparece com texto
  legível no dump** (soja: FarmProgress, sem conteúdo de mercado relevante) — os outros 7 itens
  "mantidos" não têm headline nem link visíveis nesta leitura. Nenhum conteúdo foi inventado
  para preencher essa lacuna.
- **COT desatualizado, agora com 8 dias corridos de defasagem** (corte de 25/08 frente ao
  fechamento de 02/09) — segue sendo a maior lacuna desta leitura, e agora pesa dos dois lados:
  não sabemos se os fundos entraram no rali NEM se já reagiram à reversão de hoje.
- **Prêmios de exportação (Paranaguá, farelo e óleo) seguem congelados**, agora 9 dias corridos
  idênticos (desde 24/08) — atravessando tanto o rali quanto a reversão de hoje sem se mexer;
  não dá para saber se reflete mercado físico export realmente parado ou limitação de
  atualização da fonte (NAG).
- **Danantara: marco-alvo atingido no calendário (01/09), agora dois dias sem qualquer notícia
  ou dado no briefing confirmando execução real.** Tratado como catalisador pendente de
  confirmação, não como fato consumado.
- **`tributario_watch.toml` sem atualização há 90 dias** — pelo menos dois vetores (isenção
  PIS/Cofins do biodiesel, MP 1.358/2026) já passaram da data de vigência registrada sem nota
  de renovação ou expiração. Tratados como "status desconhecido pós-vigência".
- **NOPA segue inacessível** (paywall) — segunda sessão seguida em que a fila sinaliza "release
  novo" sem que isso traga qualquer número real; tratado explicitamente como falso positivo de
  novidade, não como dado novo.
- **USDA WASDE ausente** da janela — nenhuma leitura de balanço mundial oficial atualizado
  disponível.
- **Forecasts estatísticos internos (bandas 7d/30d) geradas em 02/09 já embutem viés "altista"
  nas três pernas para os horizontes de 09/09 e 02/10** — mas esses forecasts são calculados com
  base no fechamento de 02/09 (spot ref já reflete a queda de hoje) e usam MA20+volatilidade+
  slope; não incorporam qualitativamente o evento específico de hoje (quebra do suporte do
  óleo), apenas o nível de preço resultante. Tratar como referência estatística de banda, não
  como leitura fundamentalista independente desta análise.
- **Percentil histórico de posicionamento COT não está disponível no briefing** — toda leitura
  de "fundos comprando/vendendo" nesta análise usa variação semana a semana de contratos
  absolutos, não percentil histórico.
- **MPOB (palma Malásia) segue com parser quebrado** — nenhum dado de produção/estoque de palma
  malaia disponível para cruzar com a tese de substituição via Indonésia.
- **BCBA (Argentina) segue sem links de relatório detectados pelo scraper** — nenhum dado de
  safra ou exportação argentina disponível nesta janela.
- **Sem previsão INMET para 03/09 (hoje) neste dump** — a leitura climática usa a previsão mais
  recente disponível (02/09), que já havia sido citada ontem; não há confirmação de precipitação
  real (medição), apenas previsão meteorológica.
