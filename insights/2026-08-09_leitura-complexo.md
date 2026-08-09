---
data: 2026-08-09
titulo: "Terceiro dia seguido sem sessão nova — a lacuna da sexta-feira 07/08 persiste e agora soma um fim de semana inteiro —, mas os quatro últimos pregões realmente conhecidos (03→06/08) mostram queda mais acentuada no óleo (-1,73%) do que na soja e no farelo (-1,39% ambos) e um oil-meal spread em declínio constante nas quatro sessões seguidas, um sinal tático de farelo ganhando força relativa dentro do crush que ainda não reverte, mas já não é mais 'um dia isolado', a tese estrutural de sobra do farelo (ISF 80/100) e de domínio do óleo (ISO 100/100)"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT (ZSU26 soja / ZMU26 farelo / ZLU26 óleo) — sessão de 2026-08-06 (quinta-feira), a MESMA sessão já usada nas leituras de 2026-08-07 e 2026-08-08; nenhuma sessão de 2026-08-07 (sexta-feira) está neste briefing, ver Honestidade
  - CME CBOT — série completa dos últimos 4 pregões conhecidos (2026-08-03, 08-04, 08-05, 08-06), usada nesta leitura para calcular tendência de 4 sessões (não apenas variação diária)
  - CME NYMEX heating oil (HO=F) — 2026-08-06, fechamento 3,7691 USD/galão (mesmo dado repetido desde 08-05, ver Honestidade sobre suspeita de pipeline)
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, paridade BR, Índice de Sobra de Farelo, Índice de Suporte do Óleo) — todos calculados sobre o fechamento de 2026-08-06, sem recálculo novo; série de 4 dias (03→06/08) usada para leitura de tendência
  - BCB PTAX — carimbo mais recente 2026-08-05 (USD/BRL 5,1154); 4 dias corridos sem atualização; série de 07-23 a 08-05 usada para leitura de tendência cambial de 2 semanas
  - CEPEA/ESALQ Soja Paranaguá via NAG — carimbo mais recente 2026-08-05, R$ 144,91/saca; série de 07-23 a 08-05 usada para leitura de tendência do prêmio físico portuário
  - CEPEA/ESALQ Soja Paraná interior via NAG — carimbo mais recente 2026-08-05, R$ 136,73/saca
  - NAG Físico BR — carimbo mais recente 2026-08-05 (farelo MT/IMEA R$ 1.675,10/ton, congelado há 9 dias desde 31/07; Rondonópolis/MT R$ 1.700,00/ton, mesmo congelamento; RS R$ 1.800,00/ton, agora 4 dias sem segunda leitura de confirmação); prêmios export PGUA farelo (+0,05 USD/sht) e óleo (+0,08 cts/lb), carimbo 2026-08-05, "mês Agosto/26"
  - CFTC COT Managed Money, Swap Dealers e Producer/Merchant — corte de 2026-07-28, ainda o mais recente; agora 12 dias sem atualização de posicionamento (o dobro do intervalo semanal normal); nesta leitura, além do managed money, também as categorias swap dealer e producer/merchant são lidas em conjunto para avaliar concentração de posicionamento
  - USDA Crop Progress — corte rotulado 2026-08-02, mesmos valores do corte de 2026-07-26 (11% excelente / 52% boa / 7% ruim), sexta leitura seguida sem mudança
  - USDA WASDE — ausente da janela, agora 30 dias de atraso desde o último dado (2026-07-10)
  - NOPA — fila `release-nopa-2026-08-06`, `monthly_status` continua em 0,0 bool (paywall)
  - ABIOVE projeções mensais — balanços ago-dez/2026, sem alteração frente ao dump anterior
  - NOAA CPC ENSO — carimbo mais recente 2026-08-06 (El Niño Advisory, inalterado)
  - MPOB — carimbo mais recente 2026-08-06 (mesmo conteúdo de 3.439 caracteres, parser sem números extraídos)
  - BCBA Argentina — carimbo mais recente 2026-08-06 (acessível, sem links de relatório detectados)
  - INMET — última previsão capturada é para 2026-08-06
  - Notícias Agrícolas/Canal Rural RSS — última manchete relevante capturada em 2026-08-06 ("Soja em Mato Grosso atinge maior preço do ano, mas indústria enfrenta desafios", canalrural.com.br), sem item novo de soja/farelo/óleo desde então
  - system/tributario_watch.toml (lido como referência, não editado) — `atualizado_em` 2026-06-05, agora 65 dias sem atualização
  - Notas manuais do consultor/call: 0 disponíveis nesta janela (campo do briefing)
  - Cruza com [[2026-08-08_leitura-complexo]], [[2026-08-07_leitura-complexo]] e [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (tese original do D+7, cujo checkpoint segue vencido)
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
o farelo mais barato porque a decisão de esmagar é sustentada pela margem do
óleo, e o farelo vira, na prática, o subproduto que sobra. O **ratio Far/Soj**
(preço do farelo dividido pelo preço da soja, normalizado pela conversão
bushel↔short ton) mede a mesma dinâmica por outro ângulo: abaixo de 80% o
farelo está historicamente "abundante" frente à soja — zona baixista para o
farelo —, acima de 87% está "apertado" — zona altista —, e entre os dois fica
a faixa neutra de mean-reversion, em que o mercado tende a puxar o preço de
volta pro meio quando ele se afasta demais de um extremo.

**Hoje é domingo, 2026-08-09, e o fato mais importante desta leitura é
estrutural, não de mercado: este é o terceiro dia seguido em que o briefing
não traz nenhum dado novo em nenhuma fonte — CBOT, PTAX, físico NAG, COT,
RSS — desde a sessão de quinta-feira, 2026-08-06.** Sábado e domingo não têm
pregão nem PTAX por calendário, então parte disso é esperado; mas a peça que
não é explicada só pelo calendário continua sendo a ausência completa da
sessão de **sexta-feira, 2026-08-07** — um dia útil normal de pregão na CBOT
que deveria ter gerado fechamento para soja, farelo e óleo, e que, três dias
depois, ainda não apareceu em nenhum briefing lido (nem no de 07/08, nem no
de 08/08, nem neste). Diante disso, esta leitura toma uma decisão diferente
das duas anteriores: em vez de apenas registrar o congelamento e aguardar,
ela usa a janela de 14 dias que o briefing efetivamente carrega para
calcular, pela primeira vez nesta série, uma **leitura de tendência de
múltiplas sessões** (03→06/08, os quatro últimos pregões genuinamente
conhecidos) em vez de olhar só a variação de um dia para o outro. O resultado
muda uma conclusão importante: o oil-meal spread (o quanto o óleo vale a mais
que o farelo dentro da margem, em USD/bushel) não caiu só na última sessão
conhecida — ele caiu em **todas as quatro sessões seguidas** (0,628→0,623→
0,616→0,594 USD/bu, uma queda acumulada de -5,4%), o que reclassifica o que
as leituras de 07/08 e 08/08 chamaram de "sinal isolado, sem confirmação" em
algo mais parecido com uma tendência tática de curto prazo — ainda pequena
demais para inverter a tese estrutural (o Índice de Sobra de Farelo segue em
80/100 e o Índice de Suporte do Óleo em 100/100, ambos sem um único carimbo
diferente desde pelo menos 30/07), mas grande o suficiente para merecer
monitoramento explícito, não descarte. Ao mesmo tempo, olhando os mesmos
quatro pregões em nível de preço, o óleo caiu mais (-1,73%, de 68,79 para
67,60 cts/lb) do que a soja (-1,39%, de 1.173,75 para 1.157,50 cts/bushel) ou
o farelo (-1,40%, de 315,40 para 311,00 USD/short ton) — ou seja, o mercado
vendeu proporcionalmente mais óleo do que farelo ou soja nessas quatro
sessões, o que é coerente com (embora não prove) a leitura de curva em
backwardation e quebra de suporte técnico já registrada nas leituras
anteriores. **Leitura de uma linha:** o pivô do complexo hoje não é mais
apenas "a ausência de dado" (esse still é o fato mais urgente para o
pipeline, ver Honestidade) — é a confirmação, pela primeira vez com dados de
múltiplas sessões e não de um único pregão, de que o óleo está perdendo valor
relativo mais rápido que farelo e soja, e de que o farelo vem ganhando força
tática dentro do crush por quatro sessões seguidas; a maior convicção
continua nos mecanismos estruturais que independem do calendário (ISF, ISO,
ABIOVE), a confiança é moderada-para-alta na tendência de 4 sessões porque
agora tem múltiplos pontos confirmando a mesma direção (não mais um pregão
isolado), e a confiança é baixa para qualquer afirmação sobre o que
aconteceu de fato entre sexta-feira 07/08 e hoje.

---

## Soja

**Viés: neutro — a série de preço mostra consolidação extrema nos dois
últimos pregões conhecidos (04→05, 05→06/08), mas a série de 4 sessões
(03→06/08) mostra uma queda acumulada de -1,39%, então "neutro" aqui
descreve o curtíssimo prazo (últimas 48h de pregão), não a janela de 2
semanas, que é modestamente baixista.** Último fechamento disponível:
1.157,50 cts/bushel (CBOT, ticker ZSU26.CBT, 2026-08-06).

### O que sustenta a tese

**A última sessão registrada (06/08) foi a mais estreita da série de
leituras recentes, e essa continua sendo a informação mais recente que
existe — não há como saber se a compressão se rompeu na sexta.** Abertura
1.157,25, máxima 1.158,50, mínima 1.155,75, fechamento 1.157,50 — amplitude
de apenas 2,75 pontos, um quarto dos 13,00 pontos do pregão anterior
(05/08). **Mecanismo:** compressão de amplitude tende, em teoria técnica de
mercado, a preceder um movimento mais amplo quando aparece o catalisador —
mas o catalisador mais óbvio que faltava (o COT da semana, esperado
originalmente para sexta) também não chegou, o que é coerente com a
hipótese de represamento técnico, mas segue sem confirmação, porque
simplesmente não há pregão de sexta-feira disponível para testá-la.

**Olhando os 4 últimos pregões completos (03→06/08) em vez de só o último,
a soja caiu de forma mais consistente do que a leitura de "consolidação"
sozinha sugere: 1.173,75 → 1.158,75 → 1.158,25 → 1.157,50, uma queda
acumulada de -1,39% em 3 sessões de queda seguidas antes de estabilizar.**
**Mecanismo:** isso significa que a "pausa" do dia 06/08 veio depois de um
movimento de baixa já em curso, não do nada — o mercado perdeu força de
queda, mas não reverteu para alta em nenhuma das 4 sessões. É uma leitura
mais consistente com "baixa que perde momentum" do que com "topo lateral
neutro", ainda que a magnitude (-1,39% em 2 semanas) seja pequena demais
para qualificar como tendência forte.

**A curva futura, na última leitura disponível, seguia em contango regular,
sem sinal de aperto de oferta prompt.** Q26 (ago/26) 1.151,75, U26 (set/26)
1.157,50, X26 (nov/26) 1.175,75, F27 (jan/27) 1.191,00, H27 (mar/27) 1.197,00,
K27 (mai/27) 1.205,25 — cada vencimento mais distante vale mais que o
anterior, o formato normal quando não há escassez imediata percebida pelo
mercado. O spread K27-Q26 (53,50 pontos) tinha se mantido estável frente ao
pregão anterior (54,50 em 05/08), sem sinal de esticamento ou compressão
relevante. Sem sessão de sexta-feira, esta leitura não tem como saber se
esse formato persistiu.

**O câmbio permanece com o mesmo carimbo de quarta-feira (05/08), agora há
4 dias sem atualização — mas a série das últimas 2 semanas mostra uma
depreciação leve e consistente do real.** USD/BRL PTAX foi de 5,0666
(07-24) a 5,1154 (05/08, BCB) — alta de +0,96% em 8 pregões, com oscilação
no meio do caminho (chegou a 5,1217 em 29/07, recuou a 5,0723 em 03/08, e
voltou a subir). A paridade teórica em reais (sem prêmio de basis) está em
**R$ 130,54/saca** (indicators, CBOT 1.157,50 cts × USD/BRL 5,1154, 06/08 e
05/08 respectivamente). **Mecanismo e leitura:** um real mais fraco eleva a
paridade em reais mesmo com a CBOT parada ou em leve queda — é um vetor
estrutural moderadamente favorável para quem vende soja fisicamente no
Brasil, e parcialmente compensa a queda de -1,39% do CBOT em dólares na
mesma janela. Qualquer movimento de câmbio genuíno de quinta, sexta ou do
fim de semana não está capturado neste número.

**Divergência a registrar: a manchete de "máxima do ano" em Mato Grosso
contrasta com o prêmio de exportação em Paranaguá, que vem caindo, não
subindo, nas últimas 2 semanas.** A manchete "Soja em Mato Grosso atinge
maior preço do ano, mas indústria enfrenta desafios" (Canal Rural,
06/08/2026) segue sem corpo de texto nem número (`headline: None`). Mas o
preço de suporte CEPEA/ESALQ em Paranaguá (via NAG) mostra uma trajetória de
queda ao longo das últimas 2 semanas: de R$ 148,37/saca (24/07) para R$
144,04/saca (03/08) — uma queda de -2,92% em 8 pregões — antes de recuperar
levemente para R$ 144,91/saca (05/08, o carimbo mais recente). **Mecanismo:**
isso é compatível com dois cenários distintos que esta leitura não consegue
distinguir sem mais dado: (1) a manchete se refere ao mercado *interior* de
Mato Grosso (onde o custo/frete até o porto e a demanda da própria indústria
local podem estar dissociados do preço de exportação em Paranaguá), o que
seria coerente com "indústria enfrenta desafios" — margem de esmagamento
local apertando mesmo com preço FOB porto estável ou em leve queda; ou (2) a
manchete usa uma métrica ou data-base diferente da série CEPEA/NAG deste
briefing. Na última leitura em que é possível comparar CBOT e físico no
mesmo dia (05/08), a soja em Paranaguá (R$ 144,91/saca) pagava um prêmio de
**+10,94%** sobre a paridade teórica daquele dia (R$ 130,62/saca,
indicators). A recomendação desta e das leituras anteriores permanece: não
tratar a manchete como driver quantitativo até aparecer um número
verificável em fonte primária — e agora, adicionalmente, checar se ela se
refere ao mercado interior (que não está nesta série de dados) antes de
assumir contradição com o prêmio portuário.

**O posicionamento do COT (CFTC) segue no corte de 28/07/2026, agora 12
dias sem atualização — e olhando as três categorias de posição juntas
(não só o managed money), o desenho mostra concentração especulativa
relevante do lado comprado.** O managed money (fundos sistemáticos e CTAs)
net long em soja estava em 160.479 contratos (15,73% do open interest de
1.020.108) no último corte. Mas os swap dealers (categoria que tipicamente
carrega posições de índices e fundos passivos repassadas via swap) também
estavam líquidos compradores: swap long 148.653 menos swap short 42.713 =
net long de **105.940 contratos** — quase dois terços do tamanho da posição
do managed money. Somando as duas categorias não-comerciais, o net long
combinado chega a **~266.419 contratos**, compensado do outro lado quase
inteiramente pelos produtores/comerciais (producer long 283.941, producer
short 582.088, net **-298.147**, ou seja, líquido vendido, como esperado de
quem faz hedge de produção física). **Mecanismo e leitura:** essa
concentração — duas categorias especulativas grandes do lado comprado contra
uma única categoria de hedge do lado vendido — é a estrutura clássica que
precede movimentos de liquidação mais bruscos quando aparece um catalisador
baixista: se o preço cair o suficiente para acionar stops ou margem nos
fundos, tanto o managed money quanto os swap dealers têm posição a reduzir
na mesma direção, o que amplificaria qualquer queda. Isso não é um sinal de
timing (o corte é de 28/07, quase 2 semanas velho), mas é um contexto de
risco relevante para quem avalia o tamanho de uma posição comprada nova.

### O que invalida / risco para a soja

- **A sessão de sexta-feira (07/08) aparecer retroativamente num briefing
  futuro** fora do range de 1.155,75-1.158,50 — romperia a consolidação e
  definiria a primeira direção nova desde 04/08.
- **A queda acumulada de 4 sessões (-1,39%) se estender por mais 2-3
  pregões** — mudaria a leitura de "baixa perdendo momentum" para "tendência
  de baixa em curso", exigindo revisão do viés neutro.
- **A manchete de máxima do ano em Mato Grosso ganhar um número verificável
  e se confirmar como contradição real (não aparente) ao prêmio de
  Paranaguá em queda** — mudaria a leitura sobre o basis físico brasileiro.
- **O COT (referente a 04/08) finalmente ser publicado** — mostraria se a
  concentração comprada (managed money + swap dealers) já reduzia antes da
  consolidação técnica, ou se seguiu crescendo.
- **O WASDE finalmente voltar a ser publicado** (30 dias de atraso).

### Leitura operacional — soja

Para quem opera os dois lados, a ausência de sessão de sexta-feira continua
sendo, em si, uma informação operacional: não há como saber se a compressão
de volatilidade dos últimos dois pregões conhecidos persistiu, reverteu ou
rompeu na sexta. A leitura de tendência de 4 sessões (-1,39%) sugere que,
quando o próximo pregão real chegar (o mais provável é segunda-feira,
10/08), o viés de curtíssimo prazo pende ligeiramente para baixo, mas com
convicção baixa — a magnitude é pequena e o hiato de dados é grande demais
para apostar tamanho nisso. A concentração de posição comprada em managed
money + swap dealers (contexto acima) é um argumento para quem está
avaliando o lado short: um catalisador baixista genuíno (WASDE, COT
confirmando redução de posição, ou ruptura técnica abaixo de 1.155,75) tem
potencial de acelerar mais do que o normal, dado o desenho de posicionamento.
Para quem opera o físico brasileiro, a recomendação permanece: buscar
confirmação direta na praça da manchete de máxima do ano antes de qualquer
decisão de originação, e notar que o prêmio de Paranaguá caiu, não subiu,
nas últimas 2 semanas — usar o basis prático do dono, não a manchete, como
referência.

---

## Farelo

**Viés: bear estrutural, mas com um sinal tático que já não pode mais ser
descartado como ruído de um dia — o oil-meal spread caiu em 4 sessões
seguidas (03→06/08), o que é uma tendência de curto prazo genuína, mesmo
que pequena demais para inverter o pano de fundo estrutural (ISF 80/100).**
Trata `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
(fila, ainda listada com carimbo 2026-08-06) e `release-nopa-2026-08-06`
(fila, mesma barreira de sempre, ver abaixo). Último fechamento disponível:
311,00 USD/short ton (CBOT, ticker ZMU26.CBT, 2026-08-06).

### O D+7 chega a 52 dias vencido — e o ratio nunca fechou abaixo de 80% no período recente

A tese original ([[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]])
apostava que a compressão rápida do ratio em junho (83,3%→81,4% em 4
pregões) levaria à zona comprimida (<80%) "em 1-2 semanas". O checkpoint
formal (D+7) caiu em 18/06/2026; hoje, 09/08/2026, são **52 dias corridos**
sem confirmação do fechamento abaixo de 80%. Vale registrar um detalhe que
as leituras anteriores não haviam explicitado: olhando os 4 últimos pregões
conhecidos, o ratio oscilou entre 80,47% (mínimo, 05/08) e 80,96% (máximo,
04/08) — **nunca chegou a tocar a zona de "abundante" (<80%) que a própria
tese original previa**, mesmo com o farelo estruturalmente pressionado por
todos os outros indicadores (ISF, ABIOVE). **Mecanismo:** isso sugere que o
ratio, como sinal tático de curtíssimo prazo, está preso numa faixa estreita
logo acima do gatilho (80,0%) há semanas, nem confirmando a tese de
compressão nem a invalidando de forma definitiva — um "quase lá" persistente
que qualquer leitura honesta precisa registrar como tal, não arredondar para
"dentro" ou "fora" da zona. O próximo marco formal continua sendo o D+90
(2026-09-09, agora a **31 dias** de hoje).

### O que sustenta a leitura de hoje

**O oil-meal spread caiu em todas as 4 últimas sessões conhecidas — a
mudança mais importante que esta leitura identifica hoje.** 0,6281 USD/bu
(03/08) → 0,6226 (04/08) → 0,6160 (05/08) → 0,5940 (06/08, indicators) — uma
queda acumulada de **-5,43% em 4 sessões seguidas**, sem uma única reversão
no meio do caminho. **Mecanismo:** o oil-meal spread mede quanto o óleo vale
a mais que o farelo dentro da margem de crush, em USD por bushel; uma queda
consistente e multi-sessão significa que o farelo está, sessão após sessão,
recuperando participação relativa dentro do valor total do crush — o oposto
tático do que sustenta a tese estrutural "óleo manda, farelo sobra". Isso
não inverte o ISF (que mede condições estruturais de oferta/demanda de mais
longo prazo, não o preço relativo dentro do crush), mas é um contraponto
tático que vinha sendo descartado como "ruído de um dia" nas duas leituras
anteriores — com 4 pontos de dados na mesma direção, essa descrição deixa de
ser precisa. Recomendação: tratar como tendência tática em desenvolvimento,
a confirmar (ou não) na próxima sessão real.

**A crush margin, na última leitura disponível, também cedeu nas 4 sessões,
embora de forma menos linear.** 2,7682 USD/bushel (03/08) → 2,7939 (04/08,
único dia de alta) → 2,7043 (05/08) → 2,7030 (06/08) — queda acumulada de
**-2,36% em 4 sessões**, ainda folgada frente ao nível de alerta histórico
(<2,50 USD/bu), com uma margem de segurança de cerca de 8% acima do gatilho.
**Mecanismo:** enquanto a margem de papel (CBOT) segue folgada, a esmagadora
não tem, por esse indicador, sinal de que precise reduzir ritmo de
esmagamento — mas a direção (queda em 3 das 4 últimas sessões) é o primeiro
sinal, ainda pequeno, de que essa folga vem diminuindo, não aumentando.

**O oil share, por outro lado, mostrou uma queda pequena e quase plana nas
mesmas 4 sessões — um sinal mais fraco que o oil-meal spread.** 52,17%
(03/08) → 52,16% (04/08) → 52,16% (05/08) → 52,08% (06/08) — variação de
apenas -0,09 ponto percentual em 4 sessões. **Mecanismo e leitura:** o fato
de o oil share (medido em % da margem total) ter caído muito menos que o
oil-meal spread (medido em USD/bushel absolutos) sugere que boa parte da
queda do spread veio da queda geral de preços do complexo (o óleo caiu mais
em termos absolutos, mas a proporção dentro da margem mudou pouco) — uma
leitura mais moderada do que "farelo ganhando terreno" sozinho sugeriria.
Os dois indicadores juntos apontam na mesma direção, mas com intensidades
diferentes, o que reforça tratar isso como sinal tático emergente, não como
mudança de regime confirmada.

**O Índice de Sobra de Farelo (ISF) permanece em 80/100 (4 de 5 condições
estruturais) — o mesmo valor em todos os carimbos disponíveis na janela de
14 dias deste briefing (pelo menos 30/07 a 06/08), sem novo carimbo hoje
porque não há sessão nova.** As projeções ABIOVE seguem, sem alteração,
mostrando a exportação de farelo brasileiro caindo de 1.400 mil toneladas em
agosto/2026 para 700 mil toneladas em dezembro/2026 (-50% em quatro meses,
ABIOVE projeções mensais) e o esmagamento mensal projetado caindo de 2.827
mil t em setembro para 2.204 mil t em dezembro (-22%) — drivers estruturais
de mais longo prazo que independem completamente do calendário de pregões,
e por isso continuam sendo a parte mais sólida desta leitura de farelo hoje.

**Prêmio de exportação em Paranaguá permanece perto de zero, carimbo de
2026-08-05, agora 4 dias sem atualização.** +0,05 USD/short ton, "mês
Agosto/26" (NAG). **Mecanismo, sem mudança:** um prêmio de exportação perto
de zero por semanas seguidas significa que o mercado externo não paga o
suficiente acima do preço doméstico para justificar direcionar farelo
brasileiro para o porto — o farelo fica represado internamente, pressão
estrutural de baixa que reforça o mecanismo por trás do ISF.

**As praças físicas de farelo no Brasil (NAG) seguem sem carimbo novo desde
05/08.** Mato Grosso/IMEA congelado em R$ 1.675,10/ton **há 9 dias** (desde
31/07), Rondonópolis/MT congelado em R$ 1.700,00/ton no mesmo período, e o
salto do Rio Grande do Sul (R$ 1.640,00→1.800,00/ton, registrado em 05/08)
**segue sem uma segunda leitura de confirmação, agora há 4 dias**. Quanto
mais tempo passa sem segunda leitura, maior o peso da ressalva de que pode
ser uma anomalia de coleta, não um novo nível de preço confirmado.

**`release-nopa-2026-08-06` (fila) sinaliza novo carimbo, mas o
`monthly_status` permanece em 0,0 bool** — mesma barreira de assinatura paga
documentada desde meados de junho, sem alternativa de dado primário sobre o
crush americano. Tratado como item da fila resolvido (sem conteúdo novo para
incorporar), não como pendência de leitura.

### O que invalida / risco para o farelo

- **O oil-meal spread interromper a queda de 4 sessões na próxima sessão
  real** (provavelmente segunda-feira, 10/08) — se reverter para alta,
  reforça a leitura de "farelo relativamente mais forte" como episódio
  encerrado; se continuar caindo, o sinal tático ganha mais peso e a
  leitura precisaria reconsiderar a força do viés bear-farelo de curto
  prazo, mesmo mantendo o pano de fundo estrutural (ISF, ABIOVE) inalterado.
- **O ratio Far/Soj finalmente fechar abaixo de 80%** após 52 dias sem
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
4 sessões seguidas (oil-meal spread), não apenas 1 — o que aumenta
ligeiramente a probabilidade de que a próxima sessão real confirme essa
direção em vez de reverter, mas ainda não é evidência suficiente para tratar
qualquer nível do ratio como sinal robusto para posições de convergência. A
recomendação operacional é a mesma das leituras anteriores, com peso um
pouco maior: aguardar a sessão de segunda-feira (10/08) — que carrega dois
dias de mercado potencialmente represados (a sexta que não abriu neste
briefing, mais o fim de semana) — antes de ajustar tamanho de posição no
spread Far/Soj. Para quem opera o físico de farelo no RS, a recomendação
permanece: não tratar R$ 1.800,00/ton como preço de mercado confirmado sem
uma segunda leitura, e considerar contato direto com a praça dado que já são
4 dias sem confirmação via o dado público.

---

## Óleo

**Viés: bear estrutural com a quebra técnica confirmada e reforçada pela
leitura de 4 sessões — o óleo caiu mais, em termos percentuais, do que soja
ou farelo nas últimas 2 semanas conhecidas (-1,73% vs. -1,39% e -1,40%),
consistente com a curva em backwardation e a quebra do suporte técnico.**
Trata `alerta-quebra_suporte-oleo_cbot-2026-08-06` (fato: 67,60 vs nível
72,00, ainda o carimbo mais recente). Último fechamento disponível: 67,60
cts/lb (CBOT, ticker ZLU26.CBT, 2026-08-06).

### O que sustenta a tese

**Olhando os 4 últimos pregões conhecidos, o óleo caiu em todas as
sessões, sem uma única alta no meio do caminho: 68,79 (03/08) → 68,20
(04/08) → 67,74 (05/08) → 67,60 (06/08), uma queda acumulada de -1,73% —
maior, em termos percentuais, do que a queda da soja (-1,39%) ou do farelo
(-1,40%) na mesma janela.** **Mecanismo:** essa é a confirmação, com dados
de múltiplas sessões e não de um único candle, de que o mercado está
vendendo óleo mais agressivamente do que os outros dois pernas do complexo
— coerente com a curva em backwardation (ver abaixo) e com o rompimento do
suporte técnico de 72,00, que já estava sendo monitorado pela fila desde
31/07. Em nível, 67,60 está -6,11% abaixo desse suporte — a distância mais
recente conhecida, sem confirmação de sessão nova.

**A última sessão registrada (06/08) fechou perto da mínima do dia.**
Abertura 67,75, máxima 67,89, mínima 67,57, fechamento 67,60 — fechamento a
apenas 9,4% do range, um candle de viés vendedor claro e o mais fraco desta
série de leituras recentes.

**A curva futura, na última leitura, estava em backwardation havia dois
pregões seguidos, com o spread entre a ponta curta (Q26) e a ponta longa
(H27) em 0,97 cts/lb** — Q26 67,85, U26 67,60, V26 67,30, Z26 67,06, F27
67,00, H27 66,88. O aprofundamento da inversão entre 05/08 e 06/08 veio mais
da ponta longa cedendo (H27 caiu 0,16) do que da ponta curta subindo (Q26
praticamente parado, -0,01) — uma leitura mais consistente com o mercado
descontando mais oferta ou mais pressão regulatória nos meses seguintes do
que com um aperto de disponibilidade imediata. Sem sessão nova, esta leitura
mantém essa interpretação como hipótese de trabalho.

**A margem de biodiesel americana oscilou sem tendência clara nas últimas 4
sessões: 1,0829 USD/galão (03/08) → 1,0205 (04/08) → 1,0594 (05/08) → 1,0641
(06/08, indicators).** Ao contrário do preço do óleo (queda consistente),
essa margem não mostra direção — o que é coerente com o fato de que ela
depende de dois insumos que se movem de forma parcialmente independente
(RIN D4 fixo em 2,11 USD/RIN e heating oil, cujo dado de 06/08 segue sob
suspeita de repetição de pipeline, ver Honestidade). **Mecanismo e leitura:**
com o custo do óleo caindo (68,79→67,60, -1,73%) e a margem de biodiesel
não caindo na mesma proporção, o biodiesel americano não está perdendo
competitividade apesar da queda de preço do insumo — isso é um dado
qualitativamente relevante que esta leitura não havia isolado explicitamente
antes: a queda do óleo, sozinha, não está sendo repassada como perda de
margem para o produtor de biodiesel, o que reduz (não elimina) a hipótese de
que a fraqueza do óleo venha de um choque de demanda de biodiesel nos EUA.

**O Índice de Suporte do Óleo (ISO) permanece em 100/100 (5 de 5
condições) — mesmo valor em todos os carimbos disponíveis na janela de 14
dias (pelo menos 30/07 a 06/08).** A tese estrutural (óleo dominando o valor
do crush) segue formalmente intacta como último retrato conhecido,
coexistindo sem contradição técnica com o preço em tendência de baixa e a
curva cada vez mais invertida — o ISO mede quem captura valor dentro do
crush, não se o preço está caro ou barato frente a um nível técnico.

**As projeções ABIOVE de exportação de óleo brasileiro, sem alteração desde
o dump anterior, seguem reforçando a leitura de oferta represada no mercado
interno.** Exportação de óleo caindo de 110 mil toneladas em setembro/2026
para 45 mil em outubro e 21 mil em novembro/2026 (-80% em dois meses) — um
driver estrutural que, assim como o ISF do farelo, não depende de pregão
novo para permanecer válido.

**Sem COT novo — o corte de 28/07/2026 segue sendo a fotografia mais
recente, e olhando as 3 categorias juntas, o óleo é a única das três pernas
em que o managed money já reduzia exposição comprada antes da queda de
preço das sessões seguintes.** Managed money net long em óleo: 107.898
contratos (16,60% do open interest de 650.041), após uma redução de -10,27%
na semana anterior ao corte. Os swap dealers, no entanto, seguiam
fortemente líquidos comprados: swap long 97.067 menos swap short 8.660 =
net long de **88.407 contratos** — quase do mesmo tamanho da posição do
managed money, e sem sinal (no dado disponível) de redução equivalente.
**Mecanismo:** isso é uma leitura mista — o managed money (mais sensível a
sinais técnicos de curto prazo) já vinha reduzindo antes da queda recente
confirmar a tese bearish, mas os swap dealers (posição mais estrutural,
ligada a fluxo de índice) não mostram o mesmo movimento no último corte
disponível — o que sugere que a posição comprada agregada no óleo ainda tem
gordura para reduzir se a queda de preço continuar e afetar também essa
segunda categoria.

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
sessões reforça a recomendação: manter a posição vendida com stop lógico
acima de 68,55, agora com o argumento adicional de que a queda não foi um
evento de um único pregão, mas uma sequência de 4 sessões seguidas de
fraqueza relativa frente a soja e farelo. A leitura de que o aprofundamento
da backwardation vinha do fim da curva, não do início, continua relevante
para quem opera spreads de calendário — estruturas que vendem os
vencimentos mais distantes contra os próximos (vende F27/H27, compra
Q26/U26) seguem coerentes com o último dado disponível, mas carregam dois
dias de risco de gap (sexta que faltou + fim de semana) sem atualização de
preço para reavaliar. Para quem considera nova posição comprada, a posição
residual dos swap dealers (net long ~88.407 contratos, sem sinal de redução
no último corte) é um argumento de cautela adicional: ainda há posição
especulativa "gorda" que pode ser liquidada se a queda técnica continuar,
o que favoreceria mais o lado vendido no curto prazo do que uma aposta
contrária.

---

## Spreads e crush (leitura de complexo)

**Ratio Far/Soj: 80,60% no último carimbo disponível (06/08); olhando os 4
últimos pregões, o ratio oscilou entre 80,47% e 80,96%, sem nunca tocar a
zona de "abundante" (<80%) que a tese do D+7 precisa para se confirmar.** A
recomendação operacional permanece: exigir confirmação por mais de uma
sessão seguida na mesma direção antes de tratar qualquer nível como sinal
robusto.

**Crush margin: 2,7030 USD/bu no último carimbo, com queda acumulada de
-2,36% nas últimas 4 sessões — ainda folgada (~8% acima) frente ao nível de
alerta (<2,50 USD/bu), mas a direção da margem deixou de ser plana.**

**Oil share: 52,08% no último carimbo, com queda pequena e quase linear de
apenas -0,09pp em 4 sessões — o sinal mais fraco dos indicadores táticos,
sugerindo que a mudança no crush é mais sobre nível de preço absoluto do
óleo caindo do que sobre a proporção capturada por ele dentro da margem.**

**Oil-meal spread: 0,594 USD/bu no último carimbo, com queda acumulada de
-5,43% em 4 sessões seguidas — o sinal tático mais forte e mais consistente
desta leitura, e a principal contribuição nova desta análise frente às
leituras de 07/08 e 08/08, que haviam tratado o mesmo movimento como "dia
isolado".**

**ISF em 80/100, ISO em 100/100 — ambos inalterados em toda a janela
disponível, e ambos continuam sendo a parte mais sólida desta leitura: são
índices estruturais (calculados sobre condições de mais longo prazo —
exportação, esmagamento, participação relativa no crush) que não "pausam"
quando o mercado não abre.** As projeções ABIOVE de esmagamento mensal
(2.827 mil t em setembro caindo para 2.204 mil t em dezembro, -22%) seguem
reforçando o pano de fundo de menor oferta futura de farelo e óleo no
Brasil.

**A curva futura do óleo, no último retrato disponível, seguia em
backwardation pelo segundo pregão seguido, enquanto soja e farelo seguiam em
contango regular — a divergência estrutural mais persistente da série.**

**O que os índices dizem juntos hoje:** o quadro estrutural (ISF, ISO,
ABIOVE) continua apontando para um farelo pressionado por baixo e um óleo
estruturalmente favorecido na captura de valor do crush, mas os componentes
táticos, quando lidos em janela de 4 sessões em vez de 1 dia, mostram um
movimento consistente na direção oposta à tese estrutural: farelo ganhando
força relativa (oil-meal spread -5,43% em 4 sessões) enquanto o preço do
óleo cai mais rápido que os demais (-1,73% em 4 sessões). Isso não é uma
contradição — mede-se aqui duas coisas diferentes (quem "domina" o valor do
crush no longo prazo vs. quem está sendo mais vendido no curto prazo) — mas
é a tensão mais relevante do complexo nesta leitura, e o motivo pelo qual a
próxima sessão real (10/08) é o teste mais importante da semana.

---

## Lente fiscal e regulatória BR

**Isenção PIS/Cofins do biodiesel (`PISCOFINS-BIODIESEL-ISENCAO`,
`vigencia_ate` 2026-07-31) — hoje, 2026-08-09 (domingo), permanece no 5º
dia útil desde o vencimento, porque sábado e domingo não contam como dias
úteis.** Os dias úteis decorridos seguem sendo 03/08 (seg), 04/08 (ter),
05/08 (qua), 06/08 (qui) e 07/08 (sex) — o contador só volta a andar na
segunda-feira, 10/08, que será o 6º dia útil. Nenhum item do RSS desde 06/08
trouxe informação sobre este tema. **Mecanismo e leitura, sem mudança:** se
a isenção caducou sem renovação, o custo de produção do biodiesel brasileiro
sobe, reduzindo a competitividade do biodiesel dentro do mix mandatório e
pressionando a demanda de óleo de soja como insumo doméstico — vetor
bearish direto para o óleo, e um candidato a explicar (parcialmente) por que
a ponta longa da curva do óleo estava cedendo mais que a curta na última
leitura disponível. Com o monitor tributário (`system/tributario_watch.toml`)
parado desde 2026-06-05 (**65 dias sem atualização**), esta leitura segue
sem poder confirmar nem descartar a caducidade — mantém-se como o item de
verificação manual mais urgente desta janela, agora há uma semana inteira de
pregões (03 a 07/08) transcorrida sem confirmação.

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L) —
vigência formal venceu há 29 dias** (`vigencia_ate` 11/07/2026), sem
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
usada em biodiesel, sem alteração.** Bullish para soja/óleo (alívio de custo
de entrada), mas ainda não vinculante (não é decisão repetitiva).

**Vetores dos EUA e Indonésia, sem mudança de status desde 2026-06-05:**
EPA-RFS-2026-2027 (volumes recordes de biocombustível, sustentando o RIN D4
fixo em 2,11 USD/RIN usado na margem de biodiesel — coerente com a margem
não ter caído na mesma proporção que o preço do óleo, ver seção Óleo);
45Z-CLEAN-FUEL (regra que favoreceria óleo de soja doméstico americano
frente a insumo importado, pendente de regra final do Treasury/IRS);
DANANTARA-INDONÉSIA (centralização estatal da exportação de palma, assunção
plena prevista para 01/09/2026, agora a **23 dias**); INDONESIA-B50
(provável B45 em 2026, B50 pleno só 2027-28); INDONESIA-LEVY-PMK9 (imposto
de exportação de CPO até 12,5%, encarecendo palma). Conjunto estruturalmente
bullish para óleo de soja via substituição de palma, mas inverificável pelo
lado de mercado (MPOB inacessível, ver Honestidade) — e em tensão direta com
a backwardation observada na curva do óleo, cuja ponta longa (justamente os
vencimentos que incluiriam o período pós-assunção plena da Danantara)
estava cedendo, não subindo — o mercado, pelos dados disponíveis até
quinta-feira, ainda não estava precificando esse suporte estrutural.

**O monitor tributário como um todo está há 65 dias sem qualquer
atualização** — prioridade de manutenção do sistema, especialmente relevante
agora que a isenção PIS/Cofins acumula uma semana inteira de pregões (03 a
07/08) sem confirmação de status.

---

## Riscos e eventos próximos

**O COT (CFTC) referente a 04/08/2026 segue ausente, agora 12 dias desde o
último corte (28/07) — mais que o dobro do intervalo semanal normal.** Vale
verificação direta com a CFTC se o próximo briefing (segunda-feira, 10/08)
também não trouxer o dado. Quando chegar, o dado mais relevante a checar é
se o managed money e os swap dealers em óleo (que, no último corte, tinham
comportamento divergente — managed money já reduzindo, swap dealers ainda
"gordos") convergiram na mesma direção.

**A sessão de sexta-feira (07/08) da CBOT está ausente deste briefing pela
terceira leitura seguida** — prioridade técnica: confirmar se o pipeline de
coleta rodou normalmente na sexta, antes de tratar qualquer gap de preço na
abertura de segunda-feira como movimento de mercado genuíno.

**O oil-meal spread caiu por 4 sessões seguidas (03→06/08, -5,43%
acumulado) — segunda-feira (10/08) é a primeira oportunidade real de saber
se essa tendência tática continua, estabiliza ou reverte**, o que
determinaria se o farelo mantém o ganho de força relativa dentro do crush
ou se o episódio se encerra.

**O ratio Far/Soj fechou a última sessão conhecida em 80,60%, dentro da
faixa 80,47%-80,96% das últimas 4 sessões, sem nunca tocar a zona de
"abundante" (<80%)** — segunda-feira é a primeira chance de testar se o
ratio finalmente rompe essa faixa, o que enfraqueceria ainda mais a tese do
D+7 (agora 52 dias vencida), ou se rompe para baixo, confirmando-a com
atraso.

**A backwardation da curva do óleo, no último retrato disponível,
aprofundava pelo segundo pregão seguido, com a ponta longa cedendo mais que
a curta** — segunda-feira é a primeira chance de saber se esse padrão
continua.

**O suporte técnico do óleo (72,00) seguia rompido, a -6,11%, no último
fechamento conhecido, com queda acumulada de -1,73% nas últimas 4
sessões** — a reabertura de segunda-feira é o próximo teste real.

**A isenção PIS/Cofins do biodiesel completa uma semana inteira de pregões
(03-07/08) sem confirmação de status, e só volta a avançar na
segunda-feira** — item de verificação manual mais urgente desta janela.

**O salto do físico de farelo no RS (R$ 1.640→1.800/ton) segue sem segunda
leitura de confirmação, agora há 4 dias.**

**O USDA Crop Progress rotulado 2026-08-02 segue com os MESMOS valores do
corte de 26/07**, agora pela sexta leitura seguida; o próximo corte,
referente à semana de 09/08, deve sair na segunda-feira seguinte (10/08).

**NOPA — fila `release-nopa-2026-08-06` sinaliza novo "release", mas o dado
segue inacessível**, sem alternativa de dado primário sobre o crush
americano.

**MPOB — sem números de palma extraídos, mesma barreira de longa data.**

**O WASDE segue fora da janela deste briefing, agora 30 dias de atraso**
desde o último dado (10/07/2026).

**Danantara (Indonésia) assume plenamente a cadeia de exportação de palma
em 01/09/2026, a 23 dias de hoje** — monitorar se a curva do óleo CBOT
começa a precificar esse suporte estrutural, especialmente na ponta longa,
que na última leitura disponível estava se movendo na direção oposta.

---

## Honestidade

O que não foi possível validar neste briefing, cujo dado de mercado mais
recente é de 2026-08-06 (lido em 2026-08-09), e os pontos onde a confiança é
baixa:

**1. O achado estrutural central desta leitura, agora pela terceira vez:
nenhuma fonte do briefing trouxe dado novo desde a sessão de 2026-08-06 —
nem CBOT, nem PTAX, nem NAG físico, nem COT, nem RSS, nem INMET, nem ENSO,
nem MPOB, nem BCBA.** Parte disso é esperado por calendário (fim de semana),
mas a peça que **não** é explicada só pelo calendário continua sendo a
ausência completa da sessão de **sexta-feira, 2026-08-07** — um dia útil
normal de pregão na CBOT, que deveria ter gerado um carimbo de fechamento
para soja, farelo e óleo e não gerou, em nenhum dos três briefings lidos
desde então. Esta leitura recomenda, pela terceira vez, verificação técnica
direta do pipeline de coleta (`main.py` / scraper CME) antes de
segunda-feira.

**2. A leitura de tendência de 4 sessões (03→06/08) usada extensivamente
nesta análise é matematicamente válida (os números vêm diretamente do
briefing), mas continua sendo uma janela curta — 4 pontos de dados não são
suficientes para separar tendência genuína de ruído estatístico normal,
especialmente no oil-meal spread e na queda percentual do óleo.** Esta
leitura trata essas tendências como "sinais emergentes a confirmar", não
como fatos estabelecidos.

**3. O problema de qualidade de dado identificado nas leituras anteriores
(campos de máxima, mínima e volume do farelo CBOT e de abertura do heating
oil idênticos entre carimbos de datas diferentes no mesmo dump) não pôde ser
testado novamente hoje**, porque não há sessão nova para comparar. Os
fechamentos de farelo, óleo e soja seguem tratados como confiáveis (batem
com o cálculo independente da seção `indicators`), mas os extremos e volumes
de farelo e heating oil do último dump, não.

**4. O COT (CFTC) de 28/07/2026 segue sendo o dado de posicionamento mais
recente, agora 12 dias sem atualização.** A leitura de swap dealers "gordos"
em óleo e da concentração comprada em soja (managed money + swap dealers)
usa dado de quase 2 semanas de idade — pode já estar desatualizada.

**5. O prêmio de exportação de Paranaguá (soja) e o CEPEA Paraná interior
não trouxeram carimbo novo desde 2026-08-05** — agora 4 dias sem
atualização.

**6. O salto do físico de farelo no Rio Grande do Sul (R$ 1.640,00/ton →
R$ 1.800,00/ton, registrado em 05/08) segue sem uma segunda leitura de
confirmação, agora há 4 dias.**

**7. A manchete "Soja em Mato Grosso atinge maior preço do ano, mas
indústria enfrenta desafios" (Canal Rural, 06/08/2026) segue sem corpo de
texto, número ou metodologia neste briefing** (campo `headline: None`).
Esta leitura levantou a hipótese de que ela se refere ao mercado interior,
não ao portuário, para explicar a divergência com o prêmio de Paranaguá em
queda — mas essa é uma hipótese não confirmada por nenhum dado do briefing.

**8. O PTAX (BCB) não trouxe carimbo novo desde 2026-08-05** — a paridade em
reais calculada nesta leitura usa o câmbio de quarta-feira; a leitura de
tendência cambial de 2 semanas (+0,96%, 07-24 a 08-05) é a mais recente
disponível, mas não captura nenhum movimento posterior a essa data.

**9. A interpretação causal da backwardation do óleo (ligação com
incerteza regulatória de biodiesel BR ou expectativa de mais oferta de
palma via Danantara) permanece uma hipótese desta série de leituras, não um
fato confirmado por nenhuma fonte do briefing.** Nenhum dado de palma (MPOB
bloqueado) ou de biodiesel BR (monitor tributário parado) permite confirmar
essa hipótese diretamente.

**10. O ratio Far/Soj (80,60%) segue sem fechar abaixo de 80%, agora 52
dias depois do checkpoint formal do D+7 (18/06/2026).** Esta leitura não
conclui que a tese original foi invalidada — apenas que, na janela de 4
sessões disponível, o ratio nunca tocou a zona de confirmação, e mantém o
D+90 (2026-09-09, a 31 dias) como próximo marco formal.

**11. O USDA Crop Progress rotulado 2026-08-02 trouxe, pelo sexto dump
seguido, valores idênticos ao corte de 26/07/2026 (11%/52%/7%).** Esta
leitura não trata isso como semanas genuinamente estáveis de condição de
lavoura, e reforça a recomendação de reconferir no próximo corte esperado
(semana de 09/08, publicação em torno de segunda-feira, 10/08).

**12. A isenção PIS/Cofins do biodiesel — sem confirmação de renovação ou
caducidade neste briefing, agora completando uma semana inteira de pregões
sem status.** O monitor tributário está 65 dias sem atualização; esta
leitura não presume nenhum dos dois cenários.

**13. O WASDE permanece completamente fora da janela deste briefing** —
agora 30 dias de atraso desde o último dado (10/07/2026).

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

**18. Os forecasts estatísticos internos (bandas 7d/30d, geradas em
2026-08-06) não foram usados como driver desta leitura** — são bandas
MA20+volatilidade+slope, mecânicas (soja 7d/30d "baixista", farelo 7d
"lateral"/30d "baixista", óleo 7d/30d "baixista"), sem incorporar a leitura
qualitativa de hoje; ficam registradas no briefing, mas esta leitura não as
toma como fonte de tese — embora seja notável que a direção "baixista" das
bandas estatísticas para o óleo seja consistente, por coincidência
metodológica e não por causalidade, com a queda de 4 sessões calculada
independentemente nesta leitura.

*Nenhum número foi inventado ou estimado além do que consta no briefing lido
em 2026-08-09 e nos insights anteriores referenciados. A contribuição
central desta leitura foi (1) registrar, pela terceira vez, a ausência
completa de dado novo desde a sessão de 2026-08-06, com destaque contínuo
para a lacuna anômala da sessão de sexta-feira 07/08; (2) usar a janela de 4
sessões efetivamente disponível (03→06/08) para calcular tendências
multi-sessão em vez de apenas variações diárias, o que reclassificou o
movimento do oil-meal spread de "ruído de um dia" (leituras de 07/08 e
08/08) para "tendência tática de 4 sessões a confirmar"; (3) ler as
categorias swap dealer e producer/merchant do COT junto com o managed money,
identificando concentração de posição comprada em soja e posição "gorda" de
swap dealers em óleo que as leituras anteriores não haviam detalhado; e (4)
recalcular com precisão todos os contadores de dias da fila de julgamento e
da lente fiscal (D+7 agora a 52 dias, D+90 a 31 dias, PIS/Cofins completando
uma semana de pregões sem status, MP 1.358 a 29 dias, WASDE a 30 dias de
atraso, monitor tributário a 65 dias, RS sem segunda leitura há 4 dias,
Danantara a 23 dias), tratando os três itens da fila de julgamento —
`alerta-quebra_suporte-oleo_cbot-2026-08-06`,
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` e
`release-nopa-2026-08-06` — no contexto específico de um domingo sem sessão
nova, sem inventar confirmação, tonelagem ou percentil que o briefing não
trouxe.*
