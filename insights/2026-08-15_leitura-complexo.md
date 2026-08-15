---
data: 2026-08-15
titulo: "Sábado 15/08 — o pregão não existe hoje por calendário, não por falha, mas o pipeline segue travado em 06/08 há 9 dias corridos e 6 sessões reais represadas; nesse intervalo o oil-meal spread caiu -5,4% (farelo ganhando força relativa) e o óleo aprofundou quebra técnica (-1,73%, sob o suporte 72,00) — o teste real agora é a abertura de segunda-feira 17/08"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT (ZSU26 soja / ZMU26 farelo / ZLU26 óleo) — sessão de 2026-08-06 (quinta-feira), a MESMA sessão já usada em todas as leituras de 2026-08-07 a 2026-08-14; hoje é sábado 2026-08-15, dia sem pregão por calendário (mercado americano não abre aos sábados) — ver Honestidade para a distinção entre "dia sem pregão por calendário" e "sessão represada por falha de pipeline"
  - CME CBOT — série completa dos últimos 4 pregões genuinamente conhecidos (2026-08-03, 08-04, 08-05, 08-06), única janela de tendência de mercado disponível, sem nenhum ponto adicional desde a leitura de ontem
  - CME NYMEX heating oil (HO=F) — 2026-08-06, fechamento 3,7691 USD/galão (mesmo dado repetido desde 08-05, suspeita de pipeline mantida)
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, paridade BR, Índice de Sobra de Farelo, Índice de Suporte do Óleo) — todos calculados sobre o fechamento de 2026-08-06, sem recálculo novo
  - BCB PTAX — carimbo mais recente 2026-08-05 (USD/BRL 5,1154); agora 10 dias corridos sem atualização
  - CEPEA/ESALQ Soja Paranaguá via NAG — carimbo mais recente 2026-08-05, R$ 144,91/saca; 10 dias sem atualização
  - CEPEA/ESALQ Soja Paraná interior via NAG — carimbo mais recente 2026-08-05, R$ 136,73/saca
  - NAG Físico BR — carimbo mais recente 2026-08-05 (farelo MT/IMEA R$ 1.675,10/ton, congelado desde 31/07; Rondonópolis/MT R$ 1.700,00/ton, mesmo congelamento; RS R$ 1.800,00/ton, agora 10 dias sem segunda leitura de confirmação); prêmios export PGUA farelo (+0,05 USD/sht) e óleo (+0,08 cts/lb), carimbo 2026-08-05, "mês Agosto/26"
  - CFTC COT Managed Money, Swap Dealers e Producer/Merchant — corte de 2026-07-28, agora 18 dias sem atualização
  - USDA Crop Progress — corte rotulado 2026-08-02, mesmos valores do corte de 2026-07-26 (11% excelente / 52% boa / 7% ruim)
  - USDA WASDE — ausente da janela, agora 36 dias de atraso desde o último dado (2026-07-10)
  - NOPA — fila `release-nopa-2026-08-06`, `monthly_status` continua em 0,0 bool (paywall)
  - ABIOVE projeções mensais — balanços ago-dez/2026, sem alteração frente ao dump anterior
  - NOAA CPC ENSO — carimbo mais recente 2026-08-06 (El Niño Advisory, inalterado)
  - MPOB — carimbo mais recente 2026-08-06 (mesmo conteúdo de 3.439 caracteres, parser sem números extraídos)
  - BCBA Argentina — carimbo mais recente 2026-08-06 (acessível, sem links de relatório detectados)
  - INMET — última previsão capturada é para 2026-08-06
  - Notícias Agrícolas/Canal Rural RSS — última manchete relevante capturada em 2026-08-06 ("Soja em Mato Grosso atinge maior preço do ano, mas indústria enfrenta desafios"), sem item novo desde então
  - Forecasts estatísticos internos (bandas 7d/30d, MA20+volatilidade+slope) — geração mais recente 2026-08-06; as QUATRO bandas de 7 dias geradas em 03, 04, 05 e 06/08 (alvos 10, 11, 12 e 13/08) já venceram sem nunca terem sido testadas — ver Visão geral e Honestidade
  - system/tributario_watch.toml (lido como referência, não editado) — `atualizado_em` 2026-06-05, agora 71 dias sem atualização
  - Notas manuais do consultor/call: 0 disponíveis nesta janela (campo do briefing)
  - Fila de julgamento — 2026-08-06 (mesmos 3 itens de sempre, ainda sem carimbo novo): `alerta-quebra_suporte-oleo_cbot-2026-08-06`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, `release-nopa-2026-08-06`
  - Calendário (cálculo próprio, sem fonte externa): 2026-08-15 cai num sábado — confirmado por conversão de calendário gregoriano, não por dado do briefing
  - Cruza com [[2026-08-14_leitura-complexo]], [[2026-08-13_leitura-complexo]], [[2026-08-12_leitura-complexo]], [[2026-08-11_leitura-complexo]] e [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (tese original do D+7, checkpoint segue vencido)
status: ativa
vies: [neutral-soja, bear-farelo, bear-oleo_soja]
---

## Visão geral

O complexo soja é, mecanicamente, uma fábrica com uma única matéria-prima (a
soja em grão) e dois produtos de saída em proporção fixa por bushel esmagado:
o **farelo** (a fração proteica, ~78% da massa do grão, vira ração animal) e
o **óleo degomado** (a fração de gordura, ~18-20% da massa, vira óleo de
cozinha e biodiesel). Quem decide o ritmo de esmagamento é a esmagadora,
olhando dois números sempre calculados em dólares na CBOT (Chicago Board of
Trade, a bolsa de referência mundial para esses três contratos): a **crush
margin** (farelo + óleo, por bushel, menos o custo daquele bushel de soja) e
o **oil share** (a fatia dessa margem capturada especificamente pelo óleo).
Quando o oil share sobe, o óleo "manda" no crush — a esmagadora tolera vender
o farelo mais barato porque a decisão de esmagar já se sustenta pela margem
do óleo, e o farelo vira, na prática, o subproduto que sobra. O **ratio
Far/Soj** (preço do farelo dividido pelo preço da soja, normalizado pela
conversão bushel↔short ton, onde 1 bushel de soja = 60 lb = 33,33 short tons
equivalentes de farelo por essa métrica) mede a mesma dinâmica por outro
ângulo: abaixo de 80% o farelo está historicamente "abundante" frente à soja
— zona baixista para o farelo —, acima de 87% está "apertado" — zona altista
—, e entre os dois fica a faixa neutra de mean-reversion.

**Hoje é sábado, 2026-08-15, e pela primeira vez nesta série vale abrir com
uma distinção importante: hoje NÃO É um dia de pregão perdido por falha —
mercados americanos (CBOT/CME) não operam aos sábados, então não existe
sessão real "faltando" especificamente na data de hoje.** O que persiste,
sem qualquer relação com o calendário de fim de semana, é o problema
estrutural já registrado nas oito leituras anteriores: o job que gera
`briefing/latest.md` parou de trazer dado novo depois do fechamento de
quinta-feira, 2026-08-06, e essa estagnação **já soma 9 dias corridos** e
**6 sessões reais de pregão genuinamente represadas** — sexta 07/08, segunda
10/08, terça 11/08, quarta 12/08, quinta 13/08 e sexta 14/08. O marco que
esta leitura registra hoje não é "mais um dia perdido" (hoje não seria dia
de pregão de qualquer forma), mas sim que **o hiato atravessou um fim de
semana inteiro sem nunca ter sido resolvido durante a semana que o
antecedeu** — a primeira vez nesta série em que o problema de pipeline
sobrevive a um ciclo semanal completo sem qualquer sinal de recuperação. Em
termos práticos para quem lê este documento amanhã ou depois: o próximo
teste real não é hoje, é a abertura de **segunda-feira, 2026-08-17** — se o
pipeline normalizar até lá, essa sessão terá que digerir de uma só vez até 7
pregões de notícia, câmbio, COT e fluxo represados (os 6 já listados mais a
própria segunda). Um segundo marco reforça a gravidade: as **quatro** bandas
estatísticas de 7 dias geradas nos dias que antecederam o hiato (03, 04, 05 e
06/08, com alvos em 10, 11, 12 e 13/08) já venceram, uma atrás da outra, sem
nunca terem sido confrontadas com um único fechamento real — situação
inalterada desde ontem, porque não há sessão nova para testá-las hoje nem
haveria mesmo sem o problema de pipeline. Esta leitura mantém o tratamento
desse achado estrutural como o mais acionável do conjunto, à frente de
qualquer conclusão sobre preço — ver Honestidade para o detalhamento
completo.

Dito isso, os dados que o briefing efetivamente carrega — os 4 pregões
2026-08-03 a 2026-08-06 — continuam contando a mesma história consistente já
identificada nas oito leituras anteriores, e que esta análise aprofunda mais
uma vez porque é, literalmente, o único material de mercado disponível para
interpretar: o oil-meal spread (quanto o óleo vale a mais que o farelo dentro
da margem de crush, em USD/bushel) caiu em todas as 4 sessões seguidas (0,628
→ 0,594 USD/bu, -5,4% acumulado), um sinal tático de farelo recuperando força
relativa dentro do crush; ao mesmo tempo, o preço do óleo em nível absoluto
caiu mais que soja e farelo na mesma janela (-1,73% vs. -1,39% e -1,40%) e
segue abaixo do suporte técnico de 72,00 (fechamento 67,60, -6,11% abaixo do
nível), com a curva futura em backwardation. Os índices estruturais — Índice
de Sobra de Farelo (ISF) em 80/100 e Índice de Suporte do Óleo (ISO) em
100/100 — não mudam desde pelo menos 31/07, porque medem condições de
oferta/demanda de mais longo prazo que não "pausam" quando o pregão não
abre. **Leitura de uma linha:** o pivô do complexo hoje segue sendo duplo —
de um lado, o pipeline está parado há 9 dias corridos e 6 sessões reais, um
hiato que agora atravessou um fim de semana inteiro sem resolução e que terá
seu primeiro teste possível apenas na segunda-feira 17/08; do outro, a única
informação de mercado disponível, lida em janela de 4 sessões em vez de 1
dia, continua mostrando farelo ganhando força tática dentro do crush enquanto
o óleo aprofunda uma quebra técnica estrutural — maior convicção nos
mecanismos estruturais (ISF, ISO, ABIOVE) que independem do calendário,
confiança moderada na tendência tática de 4 sessões (o mesmo conjunto de
pontos de dado das últimas oito leituras, sem nenhum ponto novo para
reforçá-la ou refutá-la), e confiança mínima sobre o que efetivamente
aconteceu com o preço entre a tarde de 06/08 e agora — um hiato que já soma 9
dias corridos e 6 sessões reais de mercado, com o teste seguinte marcado para
depois de amanhã.

---

## Soja

**Viés: neutro no curtíssimo prazo (últimos pregões conhecidos, 04→05→06/08,
mostram consolidação extrema), mas modestamente baixista na janela de 4
sessões (03→06/08, -1,39% acumulado) — a mesma leitura híbrida das oito
análises anteriores, agora sem nenhum dado adicional para confirmar ou
descartar qualquer das duas hipóteses, e sem expectativa de dado novo até a
próxima segunda-feira.** Último fechamento disponível: 1.157,50 cts/bushel
(CBOT, ticker ZSU26.CBT, 2026-08-06).

### O que sustenta a tese

**A última sessão registrada (06/08) segue sendo a mais estreita da série, e
é também o único dado que existe para julgar se a compressão técnica se
resolveu — e já deveriam ter existido pelo menos SEIS novas sessões (sexta
07, segunda 10, terça 11, quarta 12, quinta 13 e sexta 14) para testar isso,
e não existe nenhuma; hoje, sábado, não seria dia de teste de qualquer
forma.** Abertura 1.157,25, máxima 1.158,50, mínima 1.155,75, fechamento
1.157,50 — amplitude de apenas 2,75 pontos, um quarto dos 13,00 pontos do
pregão anterior (05/08). **Mecanismo:** compressão de amplitude tende, em
teoria técnica de mercado, a preceder um movimento mais amplo quando aparece
o catalisador — e agora há seis sessões represadas mais dois cortes de COT
que já deveriam ter saído (semanas de 04/08 e 11/08), o que reforça ainda
mais a hipótese de represamento técnico sem, no entanto, confirmá-la — a
confirmação só existe quando o pregão real voltar a aparecer no briefing,
sendo segunda-feira 17/08 a primeira oportunidade de calendário para isso
acontecer.

**Olhando os 4 últimos pregões completos (03→06/08), a soja caiu de forma
mais consistente do que a leitura de "consolidação" isolada sugere:
1.173,75 → 1.158,75 → 1.158,25 → 1.157,50, uma queda acumulada de -1,39% em
3 sessões de queda seguidas antes de estabilizar.** **Mecanismo:** a "pausa"
de 06/08 veio depois de um movimento de baixa já em curso, não do nada — o
mercado perdeu força vendedora, mas não reverteu para alta em nenhuma das 4
sessões conhecidas. É uma leitura mais consistente com "baixa perdendo
momentum" do que com "topo lateral neutro", ainda que a magnitude (-1,39% em
quase 3 semanas corridas) seja pequena para qualificar como tendência forte.
Com o hiato tendo atravessado um fim de semana inteiro sem resolução, essa
magnitude relativamente pequena carrega um risco extra que só cresce: se o
mercado tiver, de fato, continuado a ceder nos seis pregões represados na
mesma velocidade média observada nos últimos três pregões de queda (cerca de
-0,5% por sessão), a soja poderia, hipoteticamente, já estar bem abaixo de
1.130 no momento em que o pregão real reaparecer — um exercício puramente
ilustrativo, não uma previsão, que serve apenas para mostrar por que o
tamanho do hiato já importa para o dimensionamento de risco de quem
eventualmente reabrir posição na segunda-feira.

**A curva futura, na última leitura disponível, seguia em contango regular,
sem sinal de aperto de oferta prompt.** Q26 (ago/26) 1.151,75, U26 (set/26)
1.157,50, X26 (nov/26) 1.175,75, F27 (jan/27) 1.191,00, H27 (mar/27) 1.197,00,
K27 (mai/27) 1.205,25 — cada vencimento mais distante vale mais que o
anterior, o formato normal quando não há escassez imediata percebida. O
spread K27-Q26 (53,50 pontos) tinha se mantido estável frente ao pregão
anterior (54,50 em 05/08). Sem sessão desde então, esta leitura não tem como
saber se esse formato persistiu — e, relevante para quem monitora spreads de
calendário, seis pregões represados significam que qualquer ajuste de curva
que tenha ocorrido no intervalo pode aparecer de uma vez, como um salto maior
do que o normal, na próxima sessão real, em vez de gradualmente distribuído
ao longo de duas semanas e um fim de semana.

**O câmbio permanece com o mesmo carimbo de quarta-feira (05/08), agora há
10 dias sem atualização — mas a série das duas semanas anteriores ao hiato
mostra uma depreciação leve e consistente do real.** USD/BRL PTAX foi de
5,0666 (24/07) a 5,1154 (05/08, BCB) — alta de +0,96% em 8 pregões, com
oscilação no meio do caminho (chegou a 5,1217 em 29/07, recuou a 5,0723 em
03/08). A paridade teórica em reais (sem prêmio de basis) está em **R$
130,54/saca** (indicators, CBOT 1.157,50 cts × USD/BRL 5,1154, 06/08).
**Mecanismo e leitura:** um real mais fraco eleva a paridade em reais mesmo
com a CBOT parada ou em leve queda — vetor estrutural moderadamente
favorável para quem vende soja fisicamente no Brasil, parcialmente
compensando a queda de -1,39% do CBOT na mesma janela. Qualquer movimento de
câmbio dos últimos dias não está capturado neste número — e, como o USD/BRL
é o canal mais direto entre o CBOT em dólares e o preço físico em reais,
essa é, junto com o próprio CBOT, a lacuna mais relevante para quem decide
originação ou hedge cambial hoje.

**Divergência que persiste sem solução: a manchete de "máxima do ano" em
Mato Grosso contrasta com o prêmio de exportação em Paranaguá, que vem
caindo, não subindo, nas últimas 2 semanas conhecidas.** A manchete "Soja em
Mato Grosso atinge maior preço do ano, mas indústria enfrenta desafios"
(Canal Rural, 06/08/2026) segue sem corpo de texto nem número (`headline:
None`). O preço de suporte CEPEA/ESALQ em Paranaguá (via NAG) mostra queda
ao longo das últimas 2 semanas: de R$ 148,37/saca (24/07) para R$ 144,04/saca
(03/08) — -2,92% em 8 pregões — antes de recuperar levemente para R$
144,91/saca (05/08, carimbo mais recente, agora 10 dias parado).
**Mecanismo:** compatível com dois cenários que esta leitura não consegue
distinguir sem mais dado: (1) a manchete se refere ao mercado *interior* de
Mato Grosso, onde custo/frete e demanda da própria indústria local podem
estar dissociados do preço de exportação — coerente com "indústria enfrenta
desafios" (margem de esmagamento local apertando mesmo com FOB porto estável
ou em leve queda); ou (2) a manchete usa métrica ou data-base diferente da
série CEPEA/NAG. No último dia comparável (05/08), a soja em Paranaguá (R$
144,91/saca) pagava um prêmio de **+10,94%** sobre a paridade teórica (R$
130,62/saca, indicators). Recomendação mantida: não tratar a manchete como
driver quantitativo sem número verificável em fonte primária.

**O posicionamento do COT (CFTC) segue no corte de 28/07/2026, agora 18
dias sem atualização — mais que o dobro do ciclo semanal normal — e a
leitura das três categorias juntas continua mostrando concentração
especulativa comprada relevante.** O managed money (fundos sistemáticos e
CTAs) net long em soja estava em 160.479 contratos (15,73% do open interest
de 1.020.108). Os swap dealers (posições de índice/passivos repassadas via
swap) também estavam líquidos comprados: swap long 148.653 menos swap short
42.713 = net long de **105.940 contratos** — quase dois terços do tamanho da
posição do managed money. Somando as duas categorias não-comerciais, o net
long combinado chega a **~266.419 contratos**, compensado quase inteiramente
pelos produtores/comerciais (producer long 283.941, producer short 582.088,
net **-298.147**, líquido vendido, como esperado de hedge de produção
física). **Mecanismo e leitura:** essa concentração — duas categorias
especulativas grandes do lado comprado contra uma única categoria de hedge
do lado vendido — é a estrutura clássica que precede liquidações mais
bruscas quando aparece um catalisador baixista: se o preço cair o suficiente
para acionar stops ou margem nos fundos, tanto o managed money quanto os
swap dealers têm posição a reduzir na mesma direção, o que amplificaria
qualquer queda. O corte tem agora 18 dias — mais de dois ciclos semanais
completos sem renovação. Já deveriam ter saído, no mínimo, dois cortes novos
(nominalmente 07/08 e 14/08), o dado mais urgente desta janela para
reavaliar se essa concentração ainda existe.

### O que invalida / risco para a soja

- **As sessões represadas (07, 10, 11, 12, 13 e 14/08) aparecerem
  retroativamente num briefing futuro** fora do range de 1.155,75-1.158,50 —
  romperia a consolidação e definiria a primeira direção nova desde 04/08.
- **A queda acumulada de 4 sessões (-1,39%) se estender por mais 2-3 pregões
  quando o pregão real voltar** — mudaria a leitura de "baixa perdendo
  momentum" para "tendência de baixa em curso".
- **A manchete de máxima do ano em Mato Grosso ganhar número verificável e
  se confirmar como contradição real (não aparente) ao prêmio de Paranaguá
  em queda.**
- **O COT (referente a 04/08, e possivelmente já a 11/08) finalmente ser
  publicado** — mostraria se a concentração comprada (managed money + swap
  dealers) já reduzia antes da consolidação técnica, ou se seguiu crescendo.
- **O WASDE finalmente voltar a ser publicado** (36 dias de atraso).

### Leitura operacional — soja

Para quem opera os dois lados, a lacuna de dado hoje é, mais uma vez, a
informação operacional mais relevante, ainda que hoje em si não seja dia de
pregão: seis pregões reais represados (sexta, segunda, terça, quarta, quinta
e sexta) aumentam a probabilidade de um movimento de abertura amplo quando o
pregão realmente voltar a ser refletido no briefing — mais tempo, mais
notícia potencialmente acumulada (COT, RSS, câmbio) para o mercado digerir
de uma só vez, e a primeira oportunidade real de calendário para isso é
segunda-feira 17/08. A leitura de tendência de 4 sessões (-1,39%) sugere
viés ligeiramente baixista de curtíssimo prazo, mas com convicção baixa — a
magnitude é pequena e o hiato de dados pede cautela extra antes de
dimensionar posição nova assim que o pregão voltar. A concentração de
posição comprada em managed money + swap dealers é um argumento de contexto
para quem avalia o lado short: um catalisador baixista genuíno (WASDE, COT
confirmando redução de posição, ou ruptura técnica abaixo de 1.155,75) tem
potencial de acelerar mais do que o normal dado esse desenho de
posicionamento — e, com seis pregões represados, a abertura de segunda-feira
é a candidata mais provável para esse tipo de movimento amplo. Para quem
opera o físico brasileiro, a recomendação permanece: buscar confirmação
direta na praça da manchete de máxima do ano antes de qualquer decisão de
originação, usando o basis prático do dono, não a manchete, como referência.

---

## Farelo

**Viés: bear estrutural, com o sinal tático de força relativa (oil-meal
spread caindo 4 sessões seguidas) ainda sem uma quinta sessão real para
confirmar ou reverter — e a lacuna, embora hoje não conte como dia útil
perdido, já soma seis sessões reais represadas em que essa quinta
confirmação deveria ter chegado e não chegou, o que torna esse o sinal mais
"represado" de toda a leitura.** Trata
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` (fila,
ainda com carimbo 2026-08-06) e `release-nopa-2026-08-06` (fila, mesma
barreira de sempre, ver abaixo). Último fechamento disponível: 311,00
USD/short ton (CBOT, ticker ZMU26.CBT, 2026-08-06).

### O D+7 chega a 58 dias vencido — e o ratio nunca fechou abaixo de 80% no período recente

A tese original ([[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]])
apostava que a compressão rápida do ratio em junho (83,3%→81,4% em 4
pregões) levaria à zona comprimida (<80%) "em 1-2 semanas". O checkpoint
formal (D+7) caiu em 18/06/2026; hoje, 15/08/2026, são **58 dias corridos**
sem confirmação do fechamento abaixo de 80%. Olhando os 4 últimos pregões
conhecidos, o ratio oscilou entre 80,47% (mínimo, 05/08) e 80,96% (máximo,
04/08) — **nunca chegou a tocar a zona de "abundante" (<80%)** que a própria
tese original previa, mesmo com o farelo estruturalmente pressionado por
todos os outros indicadores (ISF, ABIOVE). **Mecanismo:** o ratio, como
sinal tático de curtíssimo prazo, está preso numa faixa estreita logo acima
do gatilho (80,0%) há semanas — um "quase lá" persistente que esta leitura
continua registrando como tal, não arredondando para "dentro" ou "fora" da
zona. O próximo marco formal é o D+90 (2026-09-09), agora a **25 dias**.

### O que sustenta a leitura de hoje

**O oil-meal spread caiu em todas as 4 últimas sessões conhecidas — o sinal
mais forte desta leitura, e o que mais precisa de confirmação com dado novo,
agora represado por seis sessões reais inteiras.** 0,6281 USD/bu (03/08) →
0,6226 (04/08) → 0,6160 (05/08) → 0,5940 (06/08, indicators) — queda
acumulada de **-5,43% em 4 sessões seguidas**, sem uma única reversão no
meio do caminho. **Mecanismo:** o oil-meal spread mede quanto o óleo vale a
mais que o farelo dentro da margem de crush, em USD por bushel; uma queda
consistente e multi-sessão significa que o farelo está, sessão após sessão,
recuperando participação relativa dentro do valor total do crush — o oposto
tático do que sustenta a tese estrutural "óleo manda, farelo sobra". Com 4
pontos de dados na mesma direção, esta leitura mantém a classificação das
análises anteriores: tendência tática em desenvolvimento, ainda não
confirmada por dado que dependa de uma quinta sessão real — que já deveria
ter existido seis vezes e ainda não existe, com a primeira chance real de
calendário para isso mudar sendo segunda-feira 17/08.

**A crush margin, na última leitura disponível, também cedeu nas 4 sessões,
embora de forma menos linear.** 2,7682 USD/bushel (03/08) → 2,7939 (04/08,
único dia de alta) → 2,7043 (05/08) → 2,7030 (06/08) — queda acumulada de
**-2,36% em 4 sessões**, ainda folgada frente ao nível de alerta histórico
(<2,50 USD/bu), com margem de segurança de ~8% acima do gatilho.
**Mecanismo:** enquanto a margem de papel (CBOT) segue folgada, a
esmagadora não tem, por esse indicador, sinal de que precise reduzir ritmo
de esmagamento — mas a direção (queda em 3 das 4 últimas sessões) é o
primeiro sinal, ainda pequeno, de que essa folga vem diminuindo.

**O oil share, por outro lado, mostrou queda pequena e quase plana nas
mesmas 4 sessões — sinal mais fraco que o oil-meal spread.** 52,17% (03/08)
→ 52,16% (04/08) → 52,16% (05/08) → 52,08% (06/08) — variação de apenas
-0,09 ponto percentual em 4 sessões. **Mecanismo e leitura:** o oil share
(medido em % da margem total) caiu muito menos que o oil-meal spread
(medido em USD/bushel absolutos), o que sugere que boa parte da queda do
spread veio da queda geral de preços do complexo (o óleo caiu mais em
termos absolutos, mas a proporção dentro da margem mudou pouco) — leitura
mais moderada do que "farelo ganhando terreno" sozinho sugeriria. Os dois
indicadores apontam na mesma direção, mas com intensidades diferentes, o
que reforça tratar isso como sinal tático emergente, não como mudança de
regime confirmada.

**O Índice de Sobra de Farelo (ISF) permanece em 80/100 (4 de 5 condições
estruturais) — o mesmo valor em todos os carimbos disponíveis na janela
deste briefing (pelo menos 31/07 a 06/08), sem novo carimbo hoje porque não
há sessão nova nem seria esperada num sábado.** As projeções ABIOVE seguem,
sem alteração, mostrando a exportação de farelo brasileiro caindo de 1.400
mil toneladas em agosto/2026 para 700 mil toneladas em dezembro/2026 (-50%
em quatro meses, ABIOVE projeções mensais) e o esmagamento mensal projetado
caindo de 2.827 mil t em setembro para 2.204 mil t em dezembro (-22%) —
drivers estruturais de mais longo prazo que independem completamente do
calendário de pregões, e por isso continuam sendo a parte mais sólida desta
leitura de farelo.

**Prêmio de exportação em Paranaguá permanece perto de zero, carimbo de
2026-08-05, agora 10 dias sem atualização.** +0,05 USD/short ton, "mês
Agosto/26" (NAG). **Mecanismo, sem mudança:** um prêmio de exportação perto
de zero por semanas seguidas significa que o mercado externo não paga o
suficiente acima do preço doméstico para justificar direcionar farelo
brasileiro para o porto — o farelo fica represado internamente, pressão
estrutural de baixa que reforça o mecanismo por trás do ISF.

**As praças físicas de farelo no Brasil (NAG) seguem sem carimbo novo desde
05/08.** Mato Grosso/IMEA congelado em R$ 1.675,10/ton **há 15 dias**
(desde 31/07), Rondonópolis/MT congelado em R$ 1.700,00/ton no mesmo
período, e o salto do Rio Grande do Sul (R$ 1.640,00→1.800,00/ton,
registrado em 05/08) **segue sem uma segunda leitura de confirmação, agora
há 10 dias**. Quanto mais tempo passa sem segunda leitura, maior o peso da
ressalva de que pode ser anomalia de coleta, não um novo nível de preço
confirmado — 10 dias sem confirmação já justifica, na visão desta leitura,
contato direto com a praça em vez de aguardar mais um dump.

**`release-nopa-2026-08-06` (fila) sinaliza novo carimbo, mas o
`monthly_status` permanece em 0,0 bool** — mesma barreira de assinatura paga
documentada desde meados de junho, sem alternativa de dado primário sobre o
crush americano. Tratado como item da fila resolvido (sem conteúdo novo
para incorporar), não como pendência de leitura.

### O que invalida / risco para o farelo

- **O oil-meal spread interromper a queda de 4 sessões na próxima sessão
  real** — se reverter para alta, reforça a leitura de "farelo relativamente
  mais forte" como episódio encerrado; se continuar caindo, o sinal tático
  ganha mais peso e a leitura precisaria reconsiderar a força do viés
  bear-farelo de curto prazo, mesmo mantendo o pano de fundo estrutural
  (ISF, ABIOVE) inalterado.
- **O ratio Far/Soj finalmente fechar abaixo de 80%** após 58 dias sem
  fazê-lo, mesmo oscilando perto do gatilho — confirmaria, com atraso, a
  tese original do D+7.
- **O salto do físico no RS (R$ 1.640→1.800/ton) se confirmar com um
  segundo carimbo** — validaria uma correção real de represamento, não uma
  anomalia de coleta.
- **O prêmio de exportação em Paranaguá sair de zero** depois de mais de um
  mês parado.
- **A crush margin cair de forma mais persistente** rumo ao nível de alerta
  (<2,50 USD/bu) — a série de 4 sessões já mostra queda de -2,36%; mais 2-3
  sessões na mesma velocidade aproximariam o nível de alerta.

### Leitura operacional — farelo

Para quem monitora o ratio Far/Soj como gatilho tático, a novidade real
desta leitura é que o farelo vem ganhando força relativa dentro do crush há
4 sessões seguidas (oil-meal spread), mas a quinta confirmação — que já
deveria ter chegado seis vezes — continua ausente, e hoje, sábado, não é dia
em que ela poderia chegar de qualquer forma. A recomendação operacional
segue a mesma das leituras anteriores, com o foco agora deslocado
explicitamente para a abertura de segunda-feira: aguardar essa próxima
sessão real antes de ajustar tamanho de posição no spread Far/Soj, e
considerar que ela carrega potencialmente seis pregões de mercado
represado, o que pode produzir um movimento de abertura maior do que o
normal em qualquer direção logo no início da semana. Para quem opera o
físico de farelo no RS, a recomendação permanece: não tratar R$ 1.800,00/ton
como preço de mercado confirmado sem uma segunda leitura, e considerar
contato direto com a praça dado que já são 10 dias sem confirmação via o
dado público.

---

## Óleo

**Viés: bear estrutural com a quebra técnica confirmada e reforçada pela
leitura de 4 sessões — o óleo caiu mais, em termos percentuais, do que soja
ou farelo nas últimas 2 semanas conhecidas (-1,73% vs. -1,39% e -1,40%),
consistente com a curva em backwardation e a quebra do suporte técnico —
sem nenhum dado novo desde então para testar se o movimento continuou,
estabilizou ou reverteu, e sem expectativa de teste possível antes de
segunda-feira.** Trata `alerta-quebra_suporte-oleo_cbot-2026-08-06` (fato:
67,60 vs nível 72,00, ainda o carimbo mais recente). Último fechamento
disponível: 67,60 cts/lb (CBOT, ticker ZLU26.CBT, 2026-08-06).

### O que sustenta a tese

**Olhando os 4 últimos pregões conhecidos, o óleo caiu em todas as sessões,
sem uma única alta no meio do caminho: 68,79 (03/08) → 68,20 (04/08) → 67,74
(05/08) → 67,60 (06/08), uma queda acumulada de -1,73% — maior, em termos
percentuais, do que a queda da soja (-1,39%) ou do farelo (-1,40%) na mesma
janela.** **Mecanismo:** confirmação, com dados de múltiplas sessões e não
de um único candle, de que o mercado vendeu óleo mais agressivamente do que
os outros dois pernas do complexo — coerente com a curva em backwardation e
com o rompimento do suporte técnico de 72,00. Em nível, 67,60 está -6,11%
abaixo desse suporte — a distância mais recente conhecida, sem confirmação
de sessão nova por já seis pregões reais represados.

**A última sessão registrada (06/08) fechou perto da mínima do dia.**
Abertura 67,75, máxima 67,89, mínima 67,57, fechamento 67,60 — fechamento a
apenas 9,4% do range, um candle de viés vendedor claro, o mais fraco desta
série de leituras.

**A curva futura, na última leitura, estava em backwardation havia dois
pregões seguidos, com o spread entre a ponta curta (Q26) e a ponta longa
(H27) em 0,97 cts/lb** — Q26 67,85, U26 67,60, V26 67,30, Z26 67,06, F27
67,00, H27 66,88. O aprofundamento da inversão entre 05/08 e 06/08 veio mais
da ponta longa cedendo (H27 caiu 0,16) do que da ponta curta subindo (Q26
praticamente parado, -0,01) — leitura mais consistente com o mercado
descontando mais oferta ou mais pressão regulatória nos meses seguintes do
que com aperto de disponibilidade imediata. Sem sessão nova, esta leitura
mantém essa interpretação como hipótese de trabalho, agora sem teste
possível por seis pregões e um fim de semana.

**A margem de biodiesel americana oscilou sem tendência clara nas últimas 4
sessões: 1,0829 USD/galão (03/08) → 1,0205 (04/08) → 1,0594 (05/08) →
1,0641 (06/08, indicators).** Ao contrário do preço do óleo (queda
consistente), essa margem não mostra direção — coerente com o fato de que
depende de dois insumos que se movem de forma parcialmente independente
(RIN D4 fixo em 2,11 USD/RIN e heating oil, cujo dado de 06/08 segue sob
suspeita de repetição de pipeline, ver Honestidade). **Mecanismo e
leitura:** com o custo do óleo caindo (68,79→67,60, -1,73%) e a margem de
biodiesel não caindo na mesma proporção, o biodiesel americano não está
perdendo competitividade apesar da queda de preço do insumo — isso reduz
(não elimina) a hipótese de que a fraqueza do óleo venha de um choque de
demanda de biodiesel nos EUA, e mantém em aberto a hipótese alternativa
(oferta de palma via Danantara, ou incerteza regulatória BR, ver Lente
fiscal) como explicação mais provável para a backwardation.

**O Índice de Suporte do Óleo (ISO) permanece em 100/100 (5 de 5 condições)
— mesmo valor em todos os carimbos disponíveis na janela deste briefing
(pelo menos 31/07 a 06/08).** A tese estrutural (óleo dominando o valor do
crush) segue formalmente intacta como último retrato conhecido, coexistindo
sem contradição técnica com o preço em tendência de baixa e a curva cada
vez mais invertida — o ISO mede quem captura valor dentro do crush, não se
o preço está caro ou barato frente a um nível técnico.

**As projeções ABIOVE de exportação de óleo brasileiro, sem alteração desde
o dump anterior, seguem reforçando a leitura de oferta represada no mercado
interno.** Exportação de óleo caindo de 110 mil toneladas em setembro/2026
para 45 mil em outubro e 21 mil em novembro/2026 (-80% em dois meses) — um
driver estrutural que, assim como o ISF do farelo, não depende de pregão
novo para permanecer válido.

**Sem COT novo — o corte de 28/07/2026 segue sendo a fotografia mais
recente, agora 18 dias velha, e olhando as 3 categorias juntas, o óleo é a
única das três pernas em que o managed money já reduzia exposição comprada
antes da queda de preço das sessões seguintes.** Managed money net long em
óleo: 107.898 contratos (16,60% do open interest de 650.041), após redução
de -10,27% na semana anterior ao corte. Os swap dealers, no entanto,
seguiam fortemente líquidos comprados: swap long 97.067 menos swap short
8.660 = net long de **88.407 contratos** — quase do mesmo tamanho da
posição do managed money, sem sinal (no dado disponível) de redução
equivalente. **Mecanismo:** leitura mista — o managed money (mais sensível
a sinais técnicos de curto prazo) já vinha reduzindo antes da queda recente
confirmar a tese bearish, mas os swap dealers (posição mais estrutural,
ligada a fluxo de índice) não mostram o mesmo movimento no último corte —
o que sugere que a posição comprada agregada no óleo ainda tem gordura para
reduzir se a queda de preço continuar e afetar também essa segunda
categoria. Com 18 dias de idade, esse corte é o dado de posicionamento mais
velho usado nesta leitura desde o início da série.

### O que invalida / risco para o óleo

- **A queda de 4 sessões (-1,73%) se interromper e reverter para alta na
  próxima sessão real** — mudaria a leitura de "óleo underperforming o
  complexo" para "movimento pontual já precificado".
- **A curva futura voltar a contango** — se os vencimentos distantes (Z26,
  F27, H27) voltarem a valer mais que os próximos, tanto a leitura de
  aperto de curto prazo quanto a de desconto de longo prazo perderiam
  sustentação.
- **A ponta longa da curva (H27) parar de ceder e estabilizar.**
- **O heating oil confirmar volume e extremos genuinamente novos** (não
  repetidos de um carimbo anterior) — validaria ou descartaria a suspeita
  de pipeline identificada nas leituras anteriores.
- **Um fechamento consistente de volta acima de 68,55** (máxima da sessão
  de 05/08) — romperia a sequência de fechamentos fracos.
- **A isenção PIS/Cofins do biodiesel seguir sem renovação** — ver Lente
  fiscal.

### Leitura operacional — óleo

Para quem está vendido desde a quebra do suporte 72,00, a leitura de 4
sessões reforça a recomendação de manter a posição vendida com stop lógico
acima de 68,55 — mas com uma ressalva que se acentua nesta leitura: com
seis pregões reais represados e a abertura de segunda-feira 17/08 como
primeiro teste real de calendário, essa próxima sessão carrega risco
elevado de gap de abertura em qualquer direção, o que muda a mecânica
prática de onde e como esse stop deveria estar posicionado (um stop lógico
numa cotação intradiária pode não capturar um gap que abre diretamente
acima ou abaixo do nível). A leitura de que o aprofundamento da
backwardation vinha do fim da curva, não do início, continua relevante para
quem opera spreads de calendário — estruturas que vendem os vencimentos
mais distantes contra os próximos (vende F27/H27, compra Q26/U26) seguem
coerentes com o último dado disponível, mas carregam agora nove dias
corridos de risco de gap (sexta que faltou + fim de semana + segunda + terça
+ quarta + quinta + sexta + o próprio fim de semana de hoje) sem
atualização de preço para reavaliar. Para quem considera nova posição
comprada, a posição residual dos swap dealers (net long ~88.407 contratos,
sem sinal de redução no último corte) é argumento de cautela adicional:
ainda há posição especulativa "gorda" que pode ser liquidada se a queda
técnica continuar, o que favorece mais o lado vendido no curto prazo do que
uma aposta contrária.

---

## Spreads e crush (leitura de complexo)

**Ratio Far/Soj: 80,60% no último carimbo disponível (06/08); olhando os 4
últimos pregões, o ratio oscilou entre 80,47% e 80,96%, sem nunca tocar a
zona de "abundante" (<80%) que a tese do D+7 precisa para se confirmar,
agora 58 dias vencida.** A recomendação operacional permanece: exigir
confirmação por mais de uma sessão seguida na mesma direção antes de tratar
qualquer nível como sinal robusto — e hoje, com a quinta sessão ainda
ausente e sem expectativa de sessão num sábado, essa confirmação segue
impossível de obter antes de segunda-feira.

**Crush margin: 2,7030 USD/bu no último carimbo, com queda acumulada de
-2,36% nas últimas 4 sessões — ainda folgada (~8% acima) frente ao nível de
alerta (<2,50 USD/bu), mas a direção deixou de ser plana.**

**Oil share: 52,08% no último carimbo, com queda pequena e quase linear de
apenas -0,09pp em 4 sessões — o sinal mais fraco dos indicadores táticos,
sugerindo que a mudança no crush é mais sobre nível de preço absoluto do
óleo caindo do que sobre a proporção capturada por ele dentro da margem.**

**Oil-meal spread: 0,594 USD/bu no último carimbo, com queda acumulada de
-5,43% em 4 sessões seguidas — o sinal tático mais forte e mais consistente
desta série, e o que mais precisa de uma quinta sessão real para deixar de
ser "tendência a confirmar" e virar "tendência confirmada" ou "episódio
encerrado".**

**ISF em 80/100, ISO em 100/100 — ambos inalterados desde pelo menos 15
dias antes do último carimbo (31/07), e ambos continuam sendo a parte mais
sólida desta leitura: são índices estruturais que não "pausam" quando o
mercado não abre.** As projeções ABIOVE de esmagamento mensal (2.827 mil t
em setembro caindo para 2.204 mil t em dezembro, -22%) seguem reforçando o
pano de fundo de menor oferta futura de farelo e óleo no Brasil.

**A curva futura do óleo, no último retrato disponível, seguia em
backwardation pelo segundo pregão seguido, enquanto soja e farelo seguiam
em contango regular — a divergência estrutural mais persistente da série.**

**O que os índices dizem juntos hoje:** o quadro estrutural (ISF, ISO,
ABIOVE) continua apontando para um farelo pressionado por baixo e um óleo
estruturalmente favorecido na captura de valor do crush, mas os componentes
táticos, quando lidos em janela de 4 sessões em vez de 1 dia, mostram um
movimento consistente na direção oposta à tese estrutural: farelo ganhando
força relativa (oil-meal spread -5,43% em 4 sessões) enquanto o preço do
óleo cai mais rápido que os demais (-1,73% em 4 sessões). Isso não é uma
contradição — mede-se aqui duas coisas diferentes (quem "domina" o valor do
crush no longo prazo vs. quem está sendo mais vendido no curto prazo) — mas
é a tensão mais relevante do complexo nesta leitura. Com seis pregões reais
represados e o hiato agora atravessando um fim de semana inteiro sem
resolução, essa tensão segue sem teste novo até segunda-feira: a próxima
sessão real decide se o sinal tático do farelo se firma ou se dissolve, e
chega carregando o peso extra de mais de uma semana e meia de mercado
potencialmente represado.

---

## Lente fiscal e regulatória BR

**Isenção PIS/Cofins do biodiesel (`PISCOFINS-BIODIESEL-ISENCAO`,
`vigencia_ate` 2026-07-31) — hoje, sábado 2026-08-15, não é dia útil, então
o contador de dias úteis desde o vencimento permanece no mesmo patamar
registrado ontem (10º dia útil, 03, 04, 05, 06, 07, 10, 11, 12, 13, 14/08) e
só avançará na próxima segunda-feira, 17/08, quando se tornaria o 11º dia
útil sem confirmação de status.** Nenhum item do RSS desde 06/08 trouxe
informação sobre este tema, e o monitor tributário
(`system/tributario_watch.toml`) segue parado desde 2026-06-05 — **71 dias
sem atualização**. **Mecanismo e leitura, sem mudança:** se a isenção
caducou sem renovação, o custo de produção do biodiesel brasileiro sobe,
reduzindo a competitividade do biodiesel dentro do mix mandatório e
pressionando a demanda de óleo de soja como insumo doméstico — vetor
bearish direto para o óleo, e um candidato a explicar (parcialmente) por
que a ponta longa da curva do óleo estava cedendo mais que a curta na
última leitura disponível. Com duas semanas inteiras de pregões (03 a
07/08, mais 10, 11, 12, 13 e 14/08) transcorridas sem confirmação, este
item permanece, nesta leitura, a verificação manual mais urgente do
conjunto fiscal — o tempo decorrido só cresce a cada dia útil sem checagem
direta, e o próximo incremento desse contador cai justamente na
segunda-feira em que o pregão também pode voltar.

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L) —
vigência formal venceu há 35 dias** (`vigencia_ate` 11/07/2026), sem
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
fixo em 2,11 USD/RIN usado na margem de biodiesel — coerente com a margem
não ter caído na mesma proporção que o preço do óleo, ver seção Óleo);
45Z-CLEAN-FUEL (regra que favoreceria óleo de soja doméstico americano
frente a insumo importado, pendente de regra final do Treasury/IRS);
DANANTARA-INDONÉSIA (centralização estatal da exportação de palma, assunção
plena prevista para 01/09/2026, agora a **17 dias**); INDONESIA-B50
(provável B45 em 2026, B50 pleno só 2027-28); INDONESIA-LEVY-PMK9 (imposto
de exportação de CPO até 12,5%, encarecendo palma). Conjunto
estruturalmente bullish para óleo de soja via substituição de palma, mas
inverificável pelo lado de mercado (MPOB inacessível, ver Honestidade) — e
em tensão direta com a backwardation observada na curva do óleo, cuja ponta
longa (justamente os vencimentos que incluiriam o período pós-assunção
plena da Danantara) estava cedendo, não subindo — o mercado, pelos dados
disponíveis até quinta-feira 06/08, ainda não estava precificando esse
suporte estrutural.

**O monitor tributário como um todo está há 71 dias sem qualquer
atualização** — prioridade de manutenção do sistema, especialmente relevante
agora que a isenção PIS/Cofins se aproxima do 11º dia útil sem confirmação
de status.

---

## Riscos e eventos próximos

**O gap de dado do pipeline é, hoje, o risco mais imediato do sistema, não
do mercado — e o marco relevante de hoje é distinto dos anteriores: o
hiato atravessou um fim de semana inteiro sem qualquer sinal de
recuperação durante a semana que o antecedeu.** Sexta 07/08, segunda 10/08,
terça 11/08, quarta 12/08, quinta 13/08 e sexta 14/08 estão ausentes do
briefing, e o job que gera `briefing/latest.md` parece não ter rodado desde
05→06/08, agora **9 dias corridos** exatos — recomendação de verificação
técnica direta, com prioridade máxima, antes de tratar qualquer gap de
preço na próxima abertura refletida como movimento de mercado genuíno, e
não como acúmulo de mais de uma semana e meia de notícia processada de uma
vez. **A segunda-feira 17/08 é o primeiro teste de calendário real: se o
briefing continuar parado nessa data, o hiato terá sobrevivido a um ciclo
semanal inteiro sem qualquer intervenção aparente.**

**Quatro forecasts estatísticos internos de 7 dias consecutivos — gerados
em 03, 04, 05 e 06/08, com alvos em 10, 11, 12 e 13/08 — já venceram, um
atrás do outro, sem nunca terem sido confrontados com um único fechamento
real.** Situação inalterada desde ontem, porque não há sessão nova para
testá-las e não haveria mesmo num sábado. O forecast de 30 dias gerado em
06/08 (alvo 05/09) segue formalmente ativo, mas já perdeu, sem
possibilidade de recuperação, 9 dos seus 30 dias de janela sem qualquer
verificação.

**O COT (CFTC) referente a 04/08/2026 segue ausente, agora 18 dias desde o
último corte (28/07) — mais que o dobro do intervalo semanal normal —, e o
corte seguinte (nominalmente de 11/08) já deveria estar publicado, com o
corte de 18/08 a apenas 3 dias.** Quando o dado chegar, o ponto mais
relevante a checar é se o managed money e os swap dealers em óleo (que, no
último corte, tinham comportamento divergente — managed money já reduzindo,
swap dealers ainda "gordos") convergiram na mesma direção.

**O oil-meal spread caiu por 4 sessões seguidas (03→06/08, -5,43%
acumulado) — a próxima sessão real, sempre que o pipeline voltar a rodar, é
a primeira oportunidade de saber se essa tendência tática continua,
estabiliza ou reverte**, o que determinaria se o farelo mantém o ganho de
força relativa dentro do crush ou se o episódio se encerra.

**O ratio Far/Soj fechou a última sessão conhecida em 80,60%, dentro da
faixa 80,47%-80,96% das últimas 4 sessões, sem nunca tocar a zona de
"abundante" (<80%)** — a próxima sessão real é a primeira chance de testar
se o ratio finalmente rompe essa faixa, o que enfraqueceria ainda mais a
tese do D+7 (agora 58 dias vencida), ou se rompe para baixo, confirmando-a
com atraso.

**A backwardation da curva do óleo, no último retrato disponível,
aprofundava pelo segundo pregão seguido, com a ponta longa cedendo mais que
a curta** — a próxima sessão real é a primeira chance de saber se esse
padrão continua.

**O suporte técnico do óleo (72,00) seguia rompido, a -6,11%, no último
fechamento conhecido, com queda acumulada de -1,73% nas últimas 4
sessões.**

**A isenção PIS/Cofins do biodiesel está a um dia útil (segunda-feira
17/08) de completar o 11º dia útil sem confirmação de status** — item de
verificação manual mais urgente desta janela.

**O salto do físico de farelo no RS (R$ 1.640→1.800/ton) segue sem segunda
leitura de confirmação, agora há 10 dias** — recomendação de contato direto
com a praça.

**O USDA Crop Progress rotulado 2026-08-02 segue com os MESMOS valores do
corte de 26/07**; o próximo corte, referente à semana de 09/08, já deveria
ter saído.

**NOPA — fila `release-nopa-2026-08-06` sinaliza novo "release", mas o
dado segue inacessível**, sem alternativa de dado primário sobre o crush
americano.

**MPOB — sem números de palma extraídos, mesma barreira de longa data.**

**O WASDE segue fora da janela deste briefing, agora 36 dias de atraso**
desde o último dado (10/07/2026).

**Danantara (Indonésia) assume plenamente a cadeia de exportação de palma
em 01/09/2026, a 17 dias de hoje** — monitorar se a curva do óleo CBOT
começa a precificar esse suporte estrutural, especialmente na ponta longa,
que na última leitura disponível estava se movendo na direção oposta.

---

## Honestidade

O que não foi possível validar neste briefing, cujo dado de mercado mais
recente é de 2026-08-06 (lido em 2026-08-15), e os pontos onde a confiança
é baixa:

**1. O achado central desta leitura, agora pela nona vez seguida, ganha
hoje uma distinção qualitativa que vale registrar com precisão: hoje,
sábado 15/08, NÃO é, por si só, um dia de pregão perdido — o CBOT/CME não
opera aos sábados, então não existe uma sétima sessão real "faltando"
especificamente na data de hoje.** O que persiste, sem qualquer relação com
o fim de semana, é que nenhuma fonte do briefing trouxe dado novo desde a
sessão de 2026-08-06 — nem CBOT, nem PTAX, nem NAG físico, nem COT, nem
RSS, nem INMET, nem ENSO, nem MPOB, nem BCBA — e essa estagnação já soma
**9 dias corridos** e **6 sessões reais de pregão genuinamente
represadas** (sexta 07/08, segunda 10/08, terça 11/08, quarta 12/08, quinta
13/08 e sexta 14/08). O marco novo desta leitura é que esse hiato
atravessou um fim de semana inteiro (o de 08-09/08 já estava coberto pela
leitura anterior; o novo é o de 15-16/08 que se abre agora) sem que a
semana útil que o precedeu (10 a 14/08, cinco dias úteis completos) trouxesse
qualquer sinal de recuperação do pipeline. O padrão — ausência total e
uniforme em todas as fontes, não apenas na CBOT, e agora persistente por
seis dias úteis consecutivos mais um fim de semana — é incompatível com
qualquer hipótese de atraso pontual de uma única fonte, e aponta com
convicção alta para o job que gera `briefing/latest.md` não ter rodado
desde a noite de 05→06/08. Esta leitura recomenda, pela nona vez,
verificação técnica direta do pipeline de coleta (`main.py` / scraper CME /
agendador do job) antes de mais um ciclo de leitura ser gerado sobre o
mesmo dado de 06/08 — o custo de continuar reprocessando a mesma sessão
cresce a cada dia que passa sem essa verificação, e o teste mais imediato
de se o problema persiste chega já na segunda-feira 17/08: se o briefing
continuar sem dado novo nessa data, ficará confirmado que o hiato sobrevive
a um ciclo de calendário semanal inteiro sem qualquer intervenção visível.

**2. A leitura de tendência de 4 sessões (03→06/08) usada extensivamente
nesta análise é matematicamente válida (os números vêm diretamente do
briefing), mas continua sendo uma janela curta — 4 pontos de dados não são
suficientes para separar tendência genuína de ruído estatístico normal,
especialmente no oil-meal spread e na queda percentual do óleo.** Esta
leitura trata essas tendências como "sinais emergentes a confirmar", não
como fatos estabelecidos — e, sem uma quinta sessão até agora, essa
classificação não pôde avançar desde a leitura de 14/08.

**3. O problema de qualidade de dado identificado nas leituras anteriores
(campos de máxima, mínima e volume do farelo CBOT e de abertura do heating
oil idênticos entre carimbos de datas diferentes no mesmo dump) não pôde
ser testado novamente hoje**, porque não há sessão nova para comparar. Os
fechamentos de farelo, óleo e soja seguem tratados como confiáveis (batem
com o cálculo independente da seção `indicators`), mas os extremos e
volumes de farelo e heating oil do último dump, não.

**4. O COT (CFTC) de 28/07/2026 segue sendo o dado de posicionamento mais
recente, agora 18 dias sem atualização — mais que o dobro do intervalo
semanal normal, e o intervalo mais longo desta série de leituras.** A
leitura de swap dealers "gordos" em óleo e da concentração comprada em soja
(managed money + swap dealers) usa dado de mais de duas semanas e meia de
idade — pode já estar desatualizada, especialmente se um catalisador de
mercado tiver ocorrido nos seis pregões represados.

**5. O prêmio de exportação de Paranaguá (soja) e o CEPEA Paraná interior
não trouxeram carimbo novo desde 2026-08-05** — agora 10 dias sem
atualização.

**6. O salto do físico de farelo no Rio Grande do Sul (R$ 1.640,00/ton →
R$ 1.800,00/ton, registrado em 05/08) segue sem uma segunda leitura de
confirmação, agora há 10 dias.**

**7. A manchete "Soja em Mato Grosso atinge maior preço do ano, mas
indústria enfrenta desafios" (Canal Rural, 06/08/2026) segue sem corpo de
texto, número ou metodologia neste briefing** (campo `headline: None`).
Esta leitura mantém a hipótese de que ela se refere ao mercado interior, não
ao portuário, para explicar a divergência com o prêmio de Paranaguá em
queda — mas essa é uma hipótese não confirmada por nenhum dado do
briefing.

**8. O PTAX (BCB) não trouxe carimbo novo desde 2026-08-05** — a paridade
em reais calculada nesta leitura usa o câmbio de quarta-feira; a leitura de
tendência cambial de 2 semanas (+0,96%, 24/07 a 05/08) é a mais recente
disponível, mas não captura nenhum movimento posterior a essa data,
incluindo qualquer variação dos últimos seis pregões represados.

**9. A interpretação causal da backwardation do óleo (ligação com
incerteza regulatória de biodiesel BR ou expectativa de mais oferta de
palma via Danantara) permanece uma hipótese desta série de leituras, não um
fato confirmado por nenhuma fonte do briefing.** Nenhum dado de palma
(MPOB bloqueado) ou de biodiesel BR (monitor tributário parado) permite
confirmar essa hipótese diretamente.

**10. O ratio Far/Soj (80,60%) segue sem fechar abaixo de 80%, agora 58
dias depois do checkpoint formal do D+7 (18/06/2026).** Esta leitura não
conclui que a tese original foi invalidada — apenas que, na janela de 4
sessões disponível, o ratio nunca tocou a zona de confirmação, e mantém o
D+90 (2026-09-09, a 25 dias) como próximo marco formal.

**11. O USDA Crop Progress rotulado 2026-08-02 continua trazendo, no dump
atual, valores idênticos ao corte de 26/07/2026 (11%/52%/7%), sem nenhum
carimbo mais novo aparecer nesta janela.** Esta leitura não trata isso como
semanas genuinamente estáveis de condição de lavoura, e reforça a
recomendação de reconferir no próximo corte esperado (semana de 09/08, que
já deveria ter sido publicado).

**12. A isenção PIS/Cofins do biodiesel — sem confirmação de renovação ou
caducidade neste briefing, a um dia útil (segunda-feira 17/08) de completar
o 11º dia útil sem status.** O monitor tributário está 71 dias sem
atualização; esta leitura não presume nenhum dos dois cenários.

**13. O WASDE permanece completamente fora da janela deste briefing** —
agora 36 dias de atraso desde o último dado (10/07/2026).

**14. NOPA (`release-nopa-2026-08-06`) segue com `monthly_status` em 0,0
bool** — mesma barreira de assinatura paga.

**15. Palma malaia (MPOB) segue sem números extraídos**, mesmo conteúdo de
3.439 caracteres desde 30/07.

**16. Nenhuma nota manual de consultor ou de call está disponível nesta
janela** (0 e 0, conforme o próprio briefing) — toda a leitura depende
exclusivamente de dado público.

**17. Clima INMET (BR) não foi usado como driver de preço** — agosto é
entressafra da soja brasileira, sem relevância direta neste momento do
calendário agrícola; a última previsão capturada é para 06/08.

**18. Os forecasts estatísticos internos de 7 dias gerados em 03, 04, 05 e
06/08 — com alvos em 10, 11, 12 e 13/08, respectivamente — venceram todos
sem nunca terem sido testados contra um fechamento real, porque o hiato do
pipeline cobriu inteiramente as quatro janelas de vigência.** O forecast de
30 dias gerado em 06/08 (alvo 2026-09-05) segue formalmente ativo, mas já
perdeu, sem possibilidade de recuperação, os primeiros 9 dos seus 30 dias
de janela sem qualquer verificação — quando (e se) o pipeline normalizar,
esse forecast deveria ser o primeiro a ser reavaliado, já que sua banda foi
calculada sobre uma base de preço (06/08) que pode estar significativamente
desatualizada frente ao nível real de mercado.

**19. Distinção de calendário registrada nesta leitura pela primeira vez de
forma explícita: nem todo dia sem dado novo é um dia de pregão perdido.**
Hoje, sábado 15/08, é dia sem pregão por definição de calendário do mercado
americano, não um dia adicional de falha de pipeline. Esta leitura optou
por manter os contadores de "sessões reais represadas" fixos em 6 (as
sessões de segunda a sexta que efetivamente deveriam ter trazido dado e não
trouxeram) e avançar apenas os contadores de "dias corridos" (9, desde
06/08) e de dias úteis fiscais (que só voltam a avançar na segunda-feira) —
uma escolha metodológica desta leitura, não um dado do briefing, feita para
não inflar artificialmente a gravidade do hiato com um dia que não seria de
pregão de qualquer forma.

*Nenhum número foi inventado ou estimado além do que consta no briefing
lido em 2026-08-15 e nos insights anteriores referenciados. A contribuição
central desta leitura foi (1) introduzir, pela primeira vez na série, a
distinção explícita entre "dia sem pregão por calendário" (hoje, sábado) e
"sessão represada por falha de pipeline" (as 6 sessões de segunda a sexta
entre 07 e 14/08), evitando inflar o contador de gravidade com um dia que
não seria de mercado de qualquer forma; (2) registrar que o hiato de
pipeline atravessou um fim de semana inteiro sem qualquer sinal de
recuperação durante a semana útil que o precedeu, com o próximo teste real
marcado para a abertura de segunda-feira 17/08; (3) recalcular com precisão
todos os contadores de dias da fila de julgamento e da lente fiscal (D+7
agora a 58 dias, D+90 a 25 dias, PIS/Cofins a um dia útil do 11º dia sem
status, MP 1.358 a 35 dias, WASDE a 36 dias de atraso, monitor tributário a
71 dias, RS sem segunda leitura há 10 dias, COT a 18 dias, Danantara a 17
dias); e (4) manter a leitura de tendência de 4 sessões (03→06/08) como o
melhor sinal tático disponível — farelo ganhando força relativa (oil-meal
spread -5,4%) e óleo em quebra técnica (-1,73%, abaixo do suporte 72,00) —,
tratando os três itens da fila de julgamento —
`alerta-quebra_suporte-oleo_cbot-2026-08-06`,
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` e
`release-nopa-2026-08-06` — no contexto específico de um hiato de pipeline
que agora atravessa um fim de semana inteiro sem resolução, sem inventar
confirmação, tonelagem ou percentil que o briefing não trouxe.*
