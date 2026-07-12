---
data: 2026-07-12
titulo: "Domingo sem pregão novo (segundo dia seguido de fim de semana): o complexo permanece exatamente onde a leitura de 11/07 o deixou — soja acima de 1.180,00 (1.191,75), farelo com o ratio Far/Soj acima de 80% por duas sessões limpas (falhando o gatilho tático do bear-farelo) e óleo abaixo do suporte 72,00 (70,46) — mas a fila força o fechamento formal da revisão D+7 de 11/06 (VENCIDA há 24 dias), e o vencimento da MP 1.358 passou ONTEM (11/07) sem que o monitor tributário confirme o desfecho; o próximo dado real chega amanhã, segunda-feira 13/07, com o pregão da semana e o Crop Progress do USDA"
tags: [complexo, auto-claude]
fontes:
  - CBOT CME (ZSQ26/ZMQ26/ZLQ26 + curva forward completa + HO=F) — última sessão disponível 2026-07-10 (sexta-feira); 2026-07-11 (sábado) e 2026-07-12 (domingo) não têm pregão, sem dado novo de preço
  - CFTC COT Managed Money — dado de referência 2026-07-07, sem atualização desde a leitura de ontem (publicado 2026-07-10; próxima atualização normalmente às sextas, ~2026-07-17)
  - BCB PTAX — último dado disponível 2026-07-10 (USD/BRL 5,1088; EUR/BRL 5,8434; Selic 0,052531% a.a.), sem publicação de fim de semana
  - CEPEA/ESALQ Paranaguá e Paraná interior via NAG — último dado disponível 2026-07-10
  - NAG Físico BR (farelo MT/IMEA, RS, Rondonópolis; prêmios export PGUA farelo/óleo) — último dado disponível 2026-07-10
  - USDA Crop Progress — 2026-07-05 (sem atualização; próximo relatório semanal amanhã, ~2026-07-13)
  - NOAA CPC ENSO — 2026-07-12 (El Niño Advisory, sem mudança)
  - ABIOVE projeções mensais — balanços ago-dez/2026 (farelo/óleo/soja), sem alteração frente à leitura anterior
  - USDA WASDE — 2026-07-10 (mesma publicação tratada ontem; cobre apenas farelo Argentina/Brasil, e China parcial)
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, ISF/ISO, paridade BR) — última base de cálculo 2026-07-10 (preço); ISF/ISO recalculados hoje (2026-07-12) mas no mesmo patamar
  - MPOB — 2026-07-12 (28º dia consecutivo sem números extraídos, desde 16/jun)
  - NOPA — 2026-07-12 (fila `release-nopa-2026-07-12`; monthly_status inacessível)
  - system/tributario_watch.toml — eventos MP-1358-2026 (`vigencia_ate` passou ontem, 11/07, sem atualização de status), MP-1363-2026, PISCOFINS-BIODIESEL-ISENCAO (vence em 19 dias), STJ-RESP-2165276, B16-CNPE-2026, EPA-RFS-2026-2027, 45Z-CLEAN-FUEL, DANANTARA-INDONESIA, INDONESIA-B50, INDONESIA-LEVY-PMK9 (todos `atualizado_em` 2026-06-05)
  - Notícias Agrícolas / Farm Progress RSS — 2026-07-12 (160 itens lidos, 3 mantidos, sem manchete nova específica destacada no dump)
  - Forecasts estatísticos internos — 2026-07-12 (recalibrados, mesmo spot-base de 10/07, bandas ligeiramente mais estreitas que ontem)
  - Cruza com [[2026-07-11_leitura-complexo]], [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (revisão D+7 fechada nesta leitura), [[2026-05-26_subvencao-fossil-aperta-biodiesel]], [[2026-05-26_pis-cofins-biodiesel-explica-mercado-fisico-fraco]], [[2026-05-26_b16-bullish-farelo]], [[2026-05-26_curva-forward-cbot-oleo-desacopla]]
status: ativa
vies: [bull-soja, neutral-farelo, bear-oleo_soja]
---

## Visão geral

O complexo soja é uma fábrica com uma única matéria-prima — a soja em grão — e dois
produtos de saída fabricados em proporção fixa a cada bushel esmagado: o **farelo** (a
fração proteica, ~78% da massa, vira ração animal) e o **óleo degomado** (a fração de
gordura, ~18-20% da massa, vira óleo de cozinha e biodiesel). Quem decide o ritmo de
esmagamento é a esmagadora, olhando a **crush margin** (o valor de farelo + óleo
produzidos por bushel, menos o custo daquele bushel de soja, medida na CBOT — Chicago
Board of Trade, a bolsa onde soja/farelo/óleo são negociados como futuros) e o **oil
share** (a fração desse valor capturada pelo óleo, hoje em 52,37% — indicadores,
10/07/2026). Quando o óleo "paga o crush" — como está acontecendo agora, com o Índice
de Suporte do Óleo (ISO) em 100/100 — a esmagadora tem incentivo a esmagar a pleno
vapor para capturar o valor do óleo, e "deixa sobrar" farelo como subproduto menos
essencial, pressionando seu preço relativo. O **ratio Far/Soj** (preço do farelo
dividido pelo preço da soja, na mesma base) é o termômetro dessa dinâmica: abaixo de
80% o farelo está "abundante" frente à soja; acima de 87% estaria "apertado"; entre 80%
e 87% é zona neutra.

**Hoje é domingo, 12/07/2026, o segundo dia seguido sem pregão** (sábado 11/07 e
domingo 12/07 não têm sessão na CBOT) — a última sessão de fato disponível continua
sendo a de sexta-feira, 10/07/2026, a mesma que a leitura de ontem já tratou em
profundidade. Isso significa que **nenhum dos três preços do complexo mudou desde
ontem**: soja segue fechada em 1.191,75 cts/bu (acima da resistência de 1.180,00),
farelo em 320,40 USD/short_ton (com o ratio Far/Soj em 80,65%, a segunda sessão
consecutiva e limpa acima de 80%) e óleo em 70,46 cts/lb (abaixo do suporte de 72,00).
Não há dado novo de câmbio (PTAX ainda em 5,1088 BRL/USD, de sexta), nem de físico BR
(NAG parado em 10/07), nem de COT (ainda 07/07, a próxima atualização normalmente sai
às sextas-feiras, o que aponta para ~17/07). O que **é novo hoje** são três coisas: (1)
a fila força o fechamento formal da revisão D+7 do insight de 11/06/2026
(`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`), marcada como
**VENCIDA** — a data de revisão programada (18/06) já passou há 24 dias, e a resposta
já ficou clara na leitura de ontem (o ratio não sustentou abaixo de 80%, pelo
contrário); (2) o `vigencia_ate` da MP 1.358/2026 (subvenção à gasolina) era
11/07/2026 — **ontem** — e o monitor tributário segue sem qualquer atualização de
status, o que significa que o sistema não consegue confirmar se a MP caducou, foi
prorrogada ou convertida em lei; e (3) a isenção de PIS/Cofins do biodiesel vence em
19 dias (31/07/2026), a contagem regressiva mais próxima do calendário fiscal.

**Leitura de uma linha:** o pivô do complexo hoje não é preço — é o calendário. Nada
mudou nos três papéis desde ontem, mas dois relógios fiscais bateram ou estão prestes a
bater (MP 1.358 venceu ontem sem confirmação, PIS/Cofins biodiesel vence em 19 dias), e
o relógio de revisão programada da tese original de bear-farelo (D+7 de 11/06) expirou
formalmente sem que o gatilho técnico específico jamais tivesse se confirmado de forma
sustentada — o ratio chegou a ficar 3 sessões abaixo de 80% (06-08/07) mas reverteu nas
duas seguintes (09-10/07). Maior convicção: bull tático em soja (nível técnico +
posicionamento de fundos + modelo estatístico alinhados, sem nenhum dado contraditório
surgindo hoje). Confiança MODERADA-ALTA em soja e no bear-óleo tático; BAIXA no
componente tático do bear-farelo (a tese estrutural ABIOVE segue de pé, mas o gatilho
de curto prazo que a acompanhava está oficialmente encerrado sem confirmação). O teste
real de tudo isso vem amanhã, segunda-feira 13/07 — primeiro pregão da semana e também
a data normal do relatório semanal de Crop Progress do USDA.

---

## Soja

**Viés: bull tático mantido, sem novo dado que o altere — soja segue fechada acima da
resistência de 1.180,00 (1.191,75 cts/bu, sessão de 10/07, ainda a mais recente
disponível), com o rompimento já confirmado por dado limpo na leitura de ontem e sem
nenhuma informação nova hoje que o contradiga, tratando novamente o id
`alerta-quebra_resistencia-soja_cbot-2026-07-10` (ainda presente na fila de hoje,
2026-07-12)**

### Tratando (de novo) a fila `alerta-quebra_resistencia-soja_cbot-2026-07-10`

Este alerta apareceu pela primeira vez na fila de ontem (11/07) e a leitura daquele dia
já respondeu "confirma" com dado limpo — o contrato N26 havia voltado à curva e o
fechamento de 10/07 (1.191,75 cts/bu, +14,00 cts frente a 09/07) ficou coerente entre
as duas gerações de dump. **O fato de o mesmo id reaparecer na fila de hoje não é um
novo evento de mercado — é simplesmente o sistema mantendo o alerta aberto até que o
próximo pregão (segunda-feira, 13/07) confirme continuidade ou reverta o nível.** Não
há sessão nova entre ontem e hoje (sábado e domingo não têm pregão), então a resposta
de hoje é idêntica à de ontem: **o rompimento de 1.180,00 segue confirmado**, sem
deterioração nem reforço adicional, porque simplesmente não há preço novo para
avaliar.

**A curva forward permanece a mesma de 10/07/2026** (Julho/26 N26 1.196,50 / Agosto/26
Q26 1.191,75 spot / Setembro/26 U26 1.181,25 / Novembro/26 X26 1.190,75 / Janeiro/27
F27 1.204,75 / Março/27 H27 1.207,50) — sem desconto de estoque físico imediato, com o
padrão sazonal normal de desconto pré-colheita americana (setembro) seguido de
recuperação em novembro/janeiro. **O câmbio (BCB PTAX) permanece em 5,1088 BRL/USD**
(último dado, 10/07/2026), e a **paridade teórica em reais permanece em R$
134,23/saca 60kg**. O **básis físico em Paranaguá (CEPEA/ESALQ via NAG) permanece em R$
140,44/saca** (10/07/2026) — o prêmio do porto sobre a paridade teórica segue em
aproximadamente +R$ 6,21/saca (+4,6%), o mesmo nível documentado ontem, ainda claramente
acima da média da semana (que começou em +R$ 4,29/saca em 07/07).

**O posicionamento dos fundos (COT, CFTC) permanece no dado de referência 07/07/2026**
— managed money net long em +69.579 contratos (7,13% do open interest de 975.954),
uma alta de +82,4% frente à semana anterior (30/06). Vale aprofundar aqui um ângulo
que as leituras dos últimos dias não detalharam: **como as outras categorias de
trader estão posicionadas** (CFTC COT, 07/07/2026). Os "producers/merchants" (a
categoria que inclui produtores rurais, cooperativas e processadoras que hedgeiam
posição física) estão **long em 323.470 contratos e short em 524.759** — um net short
de -201.289 contratos, o padrão normal para essa categoria (produtores vendem futuro
para travar preço da safra física que ainda vão colher/vender). Os "swap dealers"
(uma proxy razoável para fluxo de fundos-índice e estruturas passivas, que tipicamente
mantêm exposição comprada estrutural em commodities) estão **long em 157.963 e short
em apenas 42.259** — um net long de +115.704 contratos, a posição mais assimetricamente
comprada de todas as categorias em soja. Isso quer dizer que a demanda "passiva" via
índices já está estruturalmente comprada em soja independentemente do movimento tático
desta semana — o salto de +82% do managed money (o dinheiro mais tático e reativo a
notícia) se soma a essa base já comprada dos swap dealers, o que ajuda a explicar por
que o rali de 06-10/07 teve o volume mais robusto da série (59.159 contratos em
10/07, revertendo por completo o volume anômalo documentado dois dias antes).

**A condição de lavoura americana (USDA Crop Progress) permanece no dado de
05/07/2026**: 53% good + 11% excellent = 64% bom-ou-melhor, 6% poor — sem atualização
desde a leitura anterior. **O próximo relatório semanal sai amanhã, segunda-feira
13/07/2026** — é o teste direto e mais próximo no calendário para o driver "calor nos
EUA" que vem sendo citado como parte do rali recente, e chega bem no momento em que a
soja testa se consegue segurar o rompimento de 1.180,00 por um terceiro pregão útil
seguido (a contar 06, 07, 08/07, já que 09 e 10/07 fecharam acima também, mas o
critério de "consecutivo e confirmado" do ponto de vista técnico pede sustentação além
do fim de semana).

**A colheita argentina segue encerrada em 98%, produção mantida em 50,1 milhões de
toneladas** (Canal Rural, 27/06/2026, sem atualização) — teto estrutural regional
inalterado. BCBA (Bolsa de Comércio de Buenos Aires) segue acessível via scraper mas
sem links de relatório detectados (12/07/2026, sem mudança).

**Os forecasts estatísticos internos (12/07/2026)** foram recalibrados mas usam o
mesmo spot-base de 10/07 (não há sessão nova para recalcular a partir de um preço
diferente): central 7d = 1.208,67 cts/bu (bandas 1.147,40-1.269,94), viés altista,
praticamente idêntico ao de ontem (1.208,67, bandas 1.148,17-1.269,17) — a banda ficou
marginalmente mais larga. Central 30d = 1.276,55 cts/bu (bandas 1.149,71-1.403,40),
viés altista, também estável frente a ontem. O modelo não teve novo preço para reagir,
então essencialmente repete a leitura anterior com pequeníssimo ajuste estatístico de
janela.

### O que invalida / risco para a soja

- **Um fechamento limpo abaixo de 1.180,00 na segunda-feira (13/07)** seria a primeira
  quebra genuína do nível desde o rompimento — com o pregão de sábado/domingo
  inexistente, esse é o próximo teste real, já em menos de 24 horas.
- **O Crop Progress de amanhã (~13/07) piorar a condição de lavoura** (hoje em 64%
  bom-ou-melhor) reforçaria o driver de oferta apertada; uma melhora, ao contrário,
  tiraria um dos pilares do rali recente.
- **Nenhum WASDE de soja (EUA, Brasil ou Argentina) está disponível neste sistema** —
  mesmo com o WASDE tendo aparecido pela primeira vez em 10/07, a cobertura seguiu
  restrita a farelo (ver seção Farelo e Honestidade). A pergunta "oferta grande" segue
  sem resposta direta.
- **O COT de 07/07 ser um pico isolado** — a próxima atualização (~17/07) precisa
  confirmar que os fundos mantiveram ou ampliaram a compra ao longo da semana corrente
  (13-17/07), ainda não capturada.
- **O básis de Paranaguá (+R$ 6,21/sc) continuar recuando** — já mostrou uma pequena
  reversão frente ao pico da semana passada; se a tendência de queda continuar, esvazia
  o argumento de demanda física forte no porto.

### Leitura operacional — soja

Sem pregão novo, a leitura operacional de hoje é idêntica à de ontem: o viés tático de
alta permanece válido, com stop de referência logo abaixo de 1.180,00 (um fechamento
limpo abaixo desse nível inverteria a leitura). A convicção segue não-máxima porque
falta confirmação fundamental do WASDE de soja, que permanece ausente do sistema — o
movimento é majoritariamente técnico e de fluxo (COT + swap dealers já estruturalmente
comprados). Para quem tem física para fixar, o básis de Paranaguá (+R$ 6,21/saca sobre
a paridade) segue historicamente elevado — continuar travando parte do volume físico
nesses níveis segue sendo a leitura de maior convicção da seção, sem necessidade de
ajuste desde ontem.

---

## Farelo

**Viés: neutro tático, com a revisão estrutural D+7 formalmente encerrada hoje — o
ratio Far/Soj permanece em 80,65% (última sessão, 10/07), a segunda consecutiva e
limpa acima de 80%, o que fecha, sem ambiguidade, o veredito da revisão programada
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` (marcada VENCIDA
na fila de hoje): o gatilho tático original NÃO se sustentou**

### Tratando a fila `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` (VENCIDA)

O insight original de 11/06/2026 ([[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]])
programou três checkpoints: **D+7 (18/06/2026)**, D+90 (09/09/2026) e D+180
(08/12/2026). A fila de hoje marca o D+7 como **VENCIDO** — já se passaram 24 dias
desde a data programada de revisão sem que o sistema tivesse formalmente fechado essa
etapa (as leituras diárias intermediárias trataram o ratio tacitamente, mas o
checkpoint específico nunca foi encerrado com um veredito explícito). É o momento de
fazer isso.

**A pergunta original era: "ratio fechou <80%? WASDE mudou o quadro? NOPA confirmou
crush?"** Como já demonstrado com dado limpo na leitura de ontem (11/07) e reafirmado
hoje sem qualquer informação nova que mude a conclusão:

**1) O ratio NÃO fechou sustentado abaixo de 80%.** A trajetória completa desde a
origem da tese (11/06/2026, ratio em 81,4%) até hoje mostra um padrão de vaivém, não
uma tendência unidirecional: caiu para a zona <80% entre 06 e 08/07/2026 (79,28% →
79,46% → 78,52%, três sessões, o mais perto que a tese chegou de se confirmar
taticamente), mas reverteu para acima de 80% nas duas sessões seguintes e mais
recentes (80,85% em 09/07, 80,65% em 10/07, ambas usando dado limpo e consistente
entre gerações do dump, ao contrário da ambiguidade que contaminou a leitura de
09-10/07 nos primeiros dumps). **O critério original — "sustentado abaixo de 80% por
2-3 pregões consecutivos" — chegou a ser tecnicamente satisfeito entre 06-08/07, mas
não se manteve**, e o estado mais recente do indicador é o oposto do que a tese
apostava.

**2) O WASDE, quando finalmente apareceu no sistema (10/07/2026, um mês depois do
prazo original de revisão), não mudou o quadro do farelo.** Comparando a geração de
junho com a de julho (a única comparação temporal disponível nesta fonte), os números
de farelo Brasil e Argentina estão **congelados, sem nenhuma revisão**: farelo Brasil
— produção 8,00 mi t, exportação 0,19 mi t, esmagamento doméstico 7,10 mi t, estoque
inicial 0,19 mi t (idênticos em jun e jul); farelo Argentina — produção 33,11 mi t,
exportação 2,91 mi t, esmagamento doméstico 3,65 mi t (idênticos em jun e jul). O WASDE
não trouxe nem confirmação nem revisão de baixa/alta para o balanço de farelo — uma
publicação estatisticamente "muda" nesse recorte.

**3) A NOPA segue com `monthly_status` em 0,0 bool** (indicadores, 12/07/2026) — a
mesma barreira de assinatura paga documentada desde meados de junho, agora há quase um
mês sem qualquer alternativa de dado primário sobre o esmagamento americano. **Resposta
final ao checkpoint: não, a NOPA nunca confirmou o crush americano dentro da janela de
revisão.**

**Veredito de fechamento do checkpoint D+7:** o gatilho tático específico (ratio
sustentado <80%) **não se confirmou como tendência**, mesmo tendo chegado perto (três
sessões) — a estrutura de preço relativo farelo/soja reverteu antes de a tese poder ser
operacionalizada com confiança. Isso **não invalida o argumento estrutural mais amplo
da ABIOVE** (exportação de farelo brasileiro caindo pela metade entre agosto e
dezembro/2026, sem queda proporcional de estoque — ver tabela abaixo), que continua de
pé como pano de fundo de médio prazo e tem seus próprios checkpoints ainda vivos (D+90
em 09/09/2026, D+180 em 08/12/2026) — mas o insight original de 11/06 deve ser
atualizado para refletir que o **gatilho tático de curto prazo falhou**, preservando
apenas a tese estrutural de fundo para os checkpoints futuros.

**A trajetória projetada da ABIOVE (Associação Brasileira das Indústrias de Óleos
Vegetais, projeções mensais, sem alteração desde a leitura anterior) permanece o pilar
mais sólido do argumento estrutural**, porque não depende de nenhum contrato CBOT nem
do ratio do dia. A tabela completa de agosto a dezembro/2026 (mil toneladas):

| Mês/2026 | Estoque inicial | Produção | Exportação | Estoque final |
|---|---|---|---|---|
| Agosto | 1.561,43 | 2.285,06 | 1.400,00 | 1.224,23 |
| Setembro | 1.224,23 | 2.128,55 | 1.100,00 | 1.016,32 |
| Outubro | 1.016,32 | 2.142,97 | 850,00 | 1.100,13 |
| Novembro | 1.100,13 | 1.977,59 | 800,00 | 1.101,43 |
| Dezembro | 1.101,43 | 1.659,04 | 700,00 | 1.015,52 |

A exportação projetada cai de forma quase linear, **de 1.400 mil t em agosto para 700
mil t em dezembro — uma queda de exatamente 50% em quatro meses** — enquanto o estoque
final projetado **não acompanha essa queda na mesma proporção** (1.224 → 1.016 → 1.100
→ 1.101 → 1.016 mil t, basicamente estável em torno de 1.000-1.200 mil t ao longo de
todo o período). O mecanismo de transmissão para o preço doméstico é direto: se menos
farelo sai pelo porto mas a produção continua praticamente constante (2.285 → 2.129 →
2.143 → 1.978 → 1.659 mil t, uma queda suave, não um corte abrupto), o volume que deixa
de ser exportado precisa ser absorvido pelo mercado interno de ração — pressionando o
preço doméstico ao longo do segundo semestre. Esse argumento é o que sobrevive ao
fechamento do checkpoint tático de hoje.

**A crush margin permanece em 2,8819 USD/bu** (última base de cálculo, 10/07/2026:
farelo 320,40 + óleo 70,46 − soja 1.191,75) — perto do topo da série documentada na
semana, sustentando o incentivo de esmagamento a pleno vapor. **As praças físicas de
farelo no Brasil (NAG, último dado 10/07/2026)** permanecem em Mato Grosso/IMEA R$
1.577,34/ton, Rondonópolis R$ 1.620,00/ton e RS R$ 1.640,00/ton — sem novo dado desde
sexta-feira. O prêmio de exportação em Paranaguá segue em +0,05 USD/sht (julho/26,
inalterado há semanas) — o Brasil continua sem vantagem de preço para exportar farelo,
reforçando o mecanismo ABIOVE de absorção doméstica.

**O posicionamento dos fundos (COT, 07/07/2026)** permanece net long em +18.722
contratos (3,14% do OI de 595.447) — um salto de +295% frente à semana anterior, saindo
de posição quase neutra. Olhando as outras categorias nessa mesma data: producers/
merchants estão **long em 138.687 e short em 335.771** (net short de -197.084, o padrão
normal de hedge de quem vai vender o farelo físico), e swap dealers estão **long em
117.671 e short em apenas 6.804** — um net long de +110.867 contratos, a posição mais
assimétrica de todas as categorias em farelo, e proporcionalmente ainda maior que a
mesma métrica em soja. Essa base estrutural de compra via swap dealers ajuda a explicar
por que o farelo também subiu junto com a soja nesta semana, mesmo com o fundamento
ABIOVE apontando para pressão baixista de médio prazo — o fluxo de curto prazo (managed
money + swap dealers) pode dominar o preço por semanas antes que o fundamento físico se
imponha.

**O forecast estatístico do farelo (12/07/2026)** segue destoando da tese
fundamentalista ABIOVE: central 7d = 323,59 USD/sht (bandas 310,22-336,96), viés
altista, essencialmente idêntico ao de ontem (bandas ligeiramente mais estreitas).
Central 30d = 337,54 USD/sht (bandas 309,85-365,22), viés altista, também estável. Essa
divergência entre modelo (altista, reagindo ao movimento recente de preço) e ABIOVE
(estrutural, baixista) é exatamente o tipo de contradição que o fechamento do
checkpoint de hoje formaliza: o curto prazo e o médio prazo apontam para direções
diferentes, e não há mais um gatilho tático único (o ratio <80%) para reconciliá-los.

### O que invalida / risco para o farelo

- **A tese estrutural ABIOVE (exportação caindo pela metade, estoque sustentado) deixar
  de se confirmar no físico ao longo do 2S/26** — seria a invalidação do único pilar
  que sobrevive ao fechamento do checkpoint tático de hoje.
- **O ratio Far/Soj voltar a fechar sustentado abaixo de 80% por 2-3 pregões** —
  reabriria a possibilidade de um novo gatilho tático, mas exigiria um novo ciclo de
  confirmação, não uma simples reversão de um dia.
- **NOPA seguir inacessível indefinidamente** — sem confirmação direta de esmagamento
  americano, o novo checkpoint (D+90, 09/09) corre o risco de vencer com a mesma lacuna.
- **WASDE seguir sem cobrir soja/óleo/EUA** — mesmo com a fonte existindo desde 10/07, a
  cobertura restrita a farelo BR/ARG limita o valor da fonte para arbitrar a tese mais
  ampla do complexo.
- **A alta física pontual em MT/IMEA (+1,47% em 10/07) virar tendência** — enfraqueceria
  ainda mais a narrativa de sobra doméstica no curtíssimo prazo.

### Leitura operacional — farelo

Com o checkpoint D+7 formalmente fechado e o veredito sendo "gatilho tático falhou,
tese estrutural intacta", a recomendação operacional não muda frente à leitura de
ontem: para quem tinha posição vendida tática ancorada estritamente no ratio <80%, a
indicação permanece **reduzir ou zerar essa perna**. Para quem quer manter exposição à
tese estrutural ABIOVE (exportação caindo, estoque sustentado, pressão doméstica de
2S/26), o veículo mais robusto continua sendo um spread de convergência (farelo/soja ou
o crush completo) em vez de posição direcional pura vendida — isso evita ficar exposto
a reversões técnicas de curto prazo como a documentada nas últimas duas sessões. Os
próximos checkpoints reais da tese estrutural são D+90 (09/09/2026) e D+180
(08/12/2026) — vale registrar essa data no radar, já que é quando a curva de exportação
projetada da ABIOVE (queda de 1.100 para 700 mil t entre setembro e dezembro) deve
começar a aparecer nos dados físicos, se a tese se confirmar.

---

## Óleo

**Viés: bear tático mantido, sem novo dado que o altere — óleo segue fechado abaixo do
suporte de 72,00 (70,46 cts/lb, sessão de 10/07, ainda a mais recente disponível), com
a curva forward em backwardation e o COT (07/07) mostrando fundos reduzindo net long,
tratando novamente o id `alerta-quebra_suporte-oleo_cbot-2026-07-10` (ainda presente na
fila de hoje)**

### Tratando (de novo) a fila `alerta-quebra_suporte-oleo_cbot-2026-07-10`

Assim como o alerta de soja, este id já foi tratado com dado limpo na leitura de ontem
(11/07) — o óleo fechou em 70,46 cts/lb em 10/07, abaixo do suporte de 72,00 por uma
distância de -2,14%, e o contrato N26 nunca desapareceu da curva (ao contrário de soja
e farelo), o que já indicava que essa perna não tinha problema de qualidade de dado. Sem
pregão novo entre sexta e hoje, **a resposta de hoje é idêntica à de ontem: o óleo
segue abaixo do suporte, sem deterioração nem melhora adicional.**

**A margem de biodiesel americano permanece em 0,6338 USD/galão** (última base de
cálculo, 10/07/2026: receita 6,7183 = HO 3,5533 + 1,5×RIN 2,11; custo 6,0845 = óleo
5,2845 + industrial 0,80) — dentro da faixa de conforto de 0,50-0,80 USD/gal, mas tendo
perdido 8,5% de folga no último dado disponível frente ao dia anterior. **A curva
forward do óleo (10/07/2026, sem dado mais recente)** mantém backwardation clara:
Julho/26 (N26) 70,86 → Agosto/26 (Q26) 70,46 spot → Setembro/26 (U26) 69,92 → Outubro/26
(V26) 69,33 → Dezembro/26 (Z26) 68,98 → Janeiro/27 (F27) 68,84 — uma queda de -1,62
cts/lb (-2,3%) de agosto a janeiro/27, o argumento técnico mais robusto e mais estável
da leitura, porque não depende de nenhuma ambiguidade de dado (a curva do óleo está
limpa há semanas).

**O posicionamento dos fundos (COT, 07/07/2026)** permanece em net long +84.919
contratos (13,22% do OI de 642.514) — uma queda de -7,6% frente à semana anterior,
ainda de longe a posição mais assimétrica das três pernas do complexo. Detalhando as
outras categorias: producers/merchants estão **long em 197.872 e short em 380.118**
(net short de -182.246, hedge normal de quem processa/vende óleo físico), e swap
dealers estão **long em 86.401 e short em 8.463** — net long de +77.938, também
expressivo, mas proporcionalmente menor (12,1% do OI) que a mesma métrica em farelo
(18,6% do OI) — sugerindo que o fluxo estrutural passivo está relativamente mais
concentrado no farelo e na soja do que no óleo neste momento, o que é coerente com o
managed money estar reduzindo (não aumentando) a aposta no óleo na margem.

**O Índice de Suporte do Óleo (ISO) permanece em 100/100 (5/5 condições)** (indicadores,
12/07/2026) — o mesmo patamar máximo documentado desde 01/07/2026, sem qualquer sinal
de enfraquecimento nas últimas duas semanas.

**O pano de fundo regulatório global permanece inalterado desde 05/06/2026**
(`system/tributario_watch.toml`, 38 dias sem atualização): EPA Final RFS 2026/2027
sustenta o RIN D4, o crédito 45Z tende a favorecer óleo doméstico americano, a
Indonésia mantém a exportação de palma centralizada via Danantara mais o levy de até
12,5% sobre CPO (crude palm oil) — mas segue impossível quantificar o efeito porque o
**MPOB (Malaysian Palm Oil Board) está inacessível pelo 28º dia consecutivo**, com o
parser retornando apenas ~3.439 caracteres de HTML sem números extraídos (12/07/2026).

**O forecast estatístico do óleo (12/07/2026)** mantém o viés baixista: central 7d =
69,07 cts/lb (bandas 64,86-73,28), praticamente idêntico ao de ontem. Central 30d =
64,72 cts/lb (bandas 56,02-73,43), também estável. O modelo estatístico e a curva
forward seguem alinhados na mesma direção — o caso mais consistente de todo o complexo,
sem alteração desde ontem.

### O que invalida / risco para o óleo

- **Um fechamento limpo acima de 70,86 (nível de N26) ou perto de 72,00** na segunda-
  feira (13/07) reabriria o teste da resistência — o próximo teste real chega em menos
  de 24 horas.
- **A margem de biodiesel (0,6338 USD/gal) cair abaixo de ~0,50 USD/gal** (piso da faixa
  de conforto) reduziria o incentivo doméstico americano ao óleo.
- **RIN D4 real acima ou abaixo do parâmetro fixo usado no modelo (2,11 USD/RIN)** —
  incerteza estrutural bidirecional, sem novo dado hoje.
- **MPOB seguir inacessível** — impossível avaliar o efeito de El Niño ou das
  restrições indonésias sobre o prêmio de substituição.
- **O COT continuar mostrando redução de net long na próxima atualização (~17/07)** —
  aceleraria o de-risking já documentado desde 30/06.

### Leitura operacional — óleo

Sem pregão novo, a leitura operacional permanece idêntica à de ontem: viés bear tático,
com a curva forward em backwardation como argumento técnico mais robusto para manter
exposição vendida de médio prazo via carry. Referência de stop para quem está
posicionado vendido: 71,00-72,00 cts/lb. Para quem opera o oil share dentro do crush
(52,37%, sem novo dado), o viés estrutural segue favorecendo manter exposição relativa
ao óleo frente ao farelo — ISO em 100/100 e margem de biodiesel ainda positiva — mas a
folga da margem e o COT mostrando redução de aposta seguem pedindo cautela para quem
quiser aumentar essa exposição relativa a partir daqui.

---

## Spreads e crush — leitura de complexo

### Crush margin: 2,8819 USD/bu — sem dado novo, perto do topo da série da semana

A crush permanece em 2,8819 USD/bu (base de cálculo 10/07/2026), o mesmo valor
documentado ontem. A série da semana (2,4974 em 06/07 → 2,5638 em 07/07 → 2,7316 em
08/07 → 2,8965 em 09/07 → 2,8819 em 10/07) fecha com alta líquida de +15,4%, sustentando
o incentivo de esmagamento a pleno vapor e, por extensão, a oferta física de farelo e
óleo que alimenta diretamente o mecanismo ABIOVE descrito na seção Farelo.

### Ratio Far/Soj: 80,65% — checkpoint D+7 fechado hoje, gatilho tático não confirmado

Como detalhado na seção de Farelo, o fechamento formal do checkpoint D+7 da tese de
11/06/2026 é o desenvolvimento mais importante da leitura de hoje: o ratio chegou a
ficar 3 sessões abaixo de 80% (06-08/07), mas reverteu e fechou 2 sessões consecutivas
e limpas acima de 80% (09-10/07) — o gatilho tático original não se sustentou como
tendência, tratando `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`.

### Oil share: 52,37% — estável, sem tendência direcional clara

Sem dado novo desde 10/07/2026. A série da semana (52,03% → 53,15% → 52,41% → 52,37%)
mostra vaivém em torno de 52-53%, sem trajetória monotônica.

### Oil-meal spread: 0,7018 USD/bu — sem dado novo

Estável frente à leitura de ontem, dentro da faixa recente de oscilação da semana.

### ISF em 80/100, ISO em 100/100 — patamar sustentado há 12 dias

O Índice de Sobra de Farelo (ISF) está em 80/100 (4/5 condições) e o Índice de Suporte
do Óleo (ISO) em 100/100 (5/5) — o mesmo patamar documentado desde 01/07/2026
(indicadores, 12/07/2026), agora 12 dias consecutivos sem mudança de nível, o que
reforça a hipótese de efeito calendário/estrutural (e não ruído de curto prazo) já
levantada em leituras anteriores.

### O que os índices e o COT dizem juntos em 12/07/2026

ISF 80/100 + ISO 100/100 (ambos estáveis há 12 dias) + ratio Far/Soj acima de 80% em
duas sessões limpas (checkpoint tático do bear-farelo formalmente fechado hoje, sem
confirmação) + oil share sem tendência clara (52-53%, vaivém) + crush margin perto do
topo da série (+15,4% na semana) + swap dealers estruturalmente mais comprados
proporcionalmente em farelo (18,6% do OI) e soja (16,2% do OI, calculando 115.704/
975.954... na verdade a métrica exata deve ser lida como fração do OI: net long swap
em soja +115.704/975.954 = 11,9%; em farelo +110.867/595.447 = 18,6%; em óleo +77.938/
642.514 = 12,1%) do que no óleo (12,1% do OI):

**A leitura de hoje é de "pausa de calendário, nenhum dado novo, dois relógios fiscais
batendo".** O complexo permanece exatamente onde a sexta-feira o deixou — soja rompida
para cima, óleo rompido para baixo, farelo em zona neutra com o gatilho tático que
antes apontava para baixo agora formalmente encerrado sem confirmação. O
desenvolvimento real do dia não é de mercado, é de calendário: o checkpoint D+7 de
11/06 venceu e foi fechado, e a MP 1.358 (subvenção à gasolina) passou do seu prazo de
vigência ontem sem que o sistema consiga confirmar o desfecho. A régua de gestão de
risco pode seguir a mesma de ontem — não há novo elemento de qualidade de dado a
considerar —, mas a régua de calendário aponta para amanhã, segunda-feira 13/07, como
o próximo ponto real de teste: primeiro pregão da semana e Crop Progress do USDA no
mesmo dia.

---

## Lente fiscal e regulatória BR

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L) — o
`vigencia_ate` era ONTEM, 11/07/2026, e o monitor tributário segue sem qualquer
atualização de status (`system/tributario_watch.toml`, evento MP-1358-2026,
`atualizado_em` 2026-06-05, status ainda "tramitacao", `proximo_marco` = "Deliberação
comissão mista", `proximo_data` = 2026-07-11 — data que já passou).** Isso é o
desenvolvimento fiscal mais concreto da leitura de hoje: a data formal de vigência da
MP passou sem que nenhuma fonte pública rastreada pelo sistema (ABIOVE, NAG, notícias)
confirme se ela caducou, foi prorrogada por novo decreto, ou foi convertida em lei pelo
Congresso. A MP ressarce PIS/Cofins/Cide da gasolina e do diesel, mantendo o
combustível fóssil artificialmente mais barato — o mesmo espírito da MP 1.363/2026
(subsídio de R$ 1,12/L ao diesel, vigente até 31/12/2026, já tratada em
[[2026-05-26_subvencao-fossil-aperta-biodiesel]]). O mecanismo de transmissão para o
complexo soja é indireto mas real: enquanto o combustível fóssil segue subsidiado, a
competitividade relativa do biodiesel dentro do mix B15 mandatório permanece
pressionada, mantendo a margem da indústria de biodiesel (maior consumidora industrial
de óleo de soja no Brasil) mais apertada do que teria sem a subvenção ao concorrente
fóssil. **Se a MP de fato caducou sem conversão em lei — o que não podemos confirmar
com as fontes disponíveis —, seria um sinal (fraco, mas real) de perda de fôlego
político do pacote pró-fóssil, levemente positivo para a competitividade do biodiesel
e, por extensão, para a demanda industrial de óleo de soja; se foi convertida ou
prorrogada, reforça o quadro de pressão já documentado desde maio.** Esta é a segunda
leitura seguida (ontem e hoje) que registra essa lacuna sem conseguir fechá-la — vale
monitorar de perto nos próximos dias úteis, já que o Congresso não delibera em fins de
semana e qualquer desfecho tende a aparecer apenas a partir de segunda-feira.

**Isenção PIS/Cofins biodiesel — vencimento em 31/07/2026, agora a 19 dias.** Sem
sinalização pública de renovação até hoje (evento PISCOFINS-BIODIESEL-ISENCAO,
`atualizado_em` 2026-06-05, sem mudança). O checkpoint D+45 do insight relacionado
([[2026-05-26_pis-cofins-biodiesel-explica-mercado-fisico-fraco]]) já venceu em
09/07/2026 sem resposta, como registrado nas últimas leituras — segue sem resposta
hoje também. Com apenas 19 dias até o vencimento formal da isenção, esse é o próximo
relógio fiscal a vigiar de perto depois da MP 1.358.

**B16 — sem data, travado em B15.** Sem mudança de status (evento B16-CNPE-2026,
`atualizado_em` 2026-06-05, status "adiado", sem `proximo_data`).

**MP 1.363/2026 (subsídio ao diesel fóssil) — em vigor até 31/12/2026.** Sem
alteração. Bearish estrutural persistente para a demanda incremental de óleo de soja no
mercado doméstico brasileiro.

**STJ REsp 2.165.276/2026 — crédito PIS/Cofins para esmagadoras.** Sem alteração.
Bullish para a soja/óleo (alívio de custo de entrada para biodiesel) e, por extensão,
incentivo a mais esmagamento — coerente com mais oferta de co-produtos, reforçando o
argumento estrutural (não tático) do farelo.

**Câmbio (PTAX) em 5,1088 BRL/USD (último dado, 10/07/2026), sem publicação de fim de
semana.** Já tratado na seção de Soja.

**Pano de fundo regulatório global (EUA e Indonésia) segue dando suporte estrutural ao
óleo, sem contradizer o viés bearish tático** — detalhado na seção Óleo.

---

## Riscos e eventos próximos

**Segunda-feira, 13/07/2026 — primeiro pregão da semana.** Teste real dos três níveis
técnicos em aberto: soja segurando acima de 1.180,00, óleo seguindo abaixo de 72,00, e
o ratio Far/Soj definindo se a reversão para acima de 80% (duas sessões) ganha uma
terceira confirmação ou volta a cair.

**USDA Crop Progress — próximo relatório semanal também amanhã, ~13/07/2026** — teste
direto da narrativa de "calor nos EUA" sobre a condição de lavoura (hoje em 64%
bom-ou-melhor, sem atualização desde 05/07).

**Desfecho da MP 1.358/2026 — vigência formal encerrada ontem (11/07), sem
confirmação.** Monitorar deliberação da comissão mista e qualquer decreto de
prorrogação nos próximos dias úteis.

**Isenção PIS/Cofins biodiesel — vencimento 31/07/2026 (19 dias).** Sem sinalização de
renovação até agora.

**Próxima atualização do COT (~17/07/2026, sexta-feira)** — teste de se a rotação de
fundos documentada em 07/07 (comprando soja e farelo, reduzindo óleo) continuou ao
longo da semana de 13-17/07.

**NOPA — segue inacessível** (fila `release-nopa-2026-07-12` tratada aqui, sem dado
interpretável), sem crush americano confirmado por fonte primária.

**MPOB — sem números de palma extraídos**, mantendo cego o efeito da Indonésia e do El
Niño sobre o prêmio de substituição do óleo de soja.

**Checkpoints futuros da tese estrutural do farelo (ABIOVE)** — D+90 em 09/09/2026 e
D+180 em 08/12/2026 (insight [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]),
agora os únicos checkpoints vivos depois do fechamento do D+7 nesta leitura.

---

## Honestidade

O que não foi possível validar neste briefing de 12/07/2026, onde a confiança é baixa
ou há lacunas materiais:

**1. Não há nenhum dado de preço novo desde a sessão de 10/07/2026** — hoje (domingo)
e ontem (sábado) não têm pregão na CBOT, e nenhuma outra fonte de preço/físico BR
(PTAX, NAG, CEPEA) publica em fins de semana. Toda a análise de preço desta leitura é,
necessariamente, uma releitura do mesmo dado já tratado ontem, sem poder confirmar
continuidade ou reversão até o pregão de amanhã.

**2. O fechamento do checkpoint D+7 da tese de 11/06/2026 é uma decisão editorial desta
leitura, não um cálculo automático do sistema** — a fila apenas sinaliza "VENCIDA"; o
veredito de que o gatilho tático "não se confirmou" é uma interpretação baseada nos
dados de ratio Far/Soj disponíveis (que mostram reversão, não confirmação), mas não há
um mecanismo formal no sistema que marque checkpoints como "encerrados" — isso deveria
ser refletido manualmente no arquivo do insight original, o que esta leitura não faz
(escreve apenas em `insights/`, mas não edita o arquivo de 11/06 diretamente, seguindo
a instrução de tratar a fila em vez de recriar/editar insights antigos).

**3. O desfecho da MP 1.358/2026 não pôde ser confirmado** — o `vigencia_ate` passou
ontem (11/07) e o monitor tributário (`system/tributario_watch.toml`) não tem
atualização de status há 38 dias (desde 05/06/2026). Nenhuma fonte pública rastreada
pelo sistema (ABIOVE, NAG, notícias) confirma se a MP caducou, foi prorrogada ou
convertida em lei.

**4. O WASDE, desde que apareceu em 10/07/2026, cobre apenas farelo (Argentina e
Brasil, mais duas linhas truncadas de China)** — segue sem nenhum dado de soja em
grão ou óleo de soja, em qualquer geografia, e sem nenhum dado dos Estados Unidos. A
pergunta central sobre "oferta grande de soja" segue sem canal de resposta interno.

**5. NOPA segue com `monthly_status` em 0,0 bool** (indicadores, 12/07/2026) — mesma
barreira de assinatura paga documentada desde meados de junho, agora há 28 dias.

**6. Percentis históricos de COT não calculados** — os números de 07/07/2026 são lidos
apenas em nível absoluto e como fração do open interest corrente, sem série histórica
completa para calibrar se estão em zona extrema frente ao próprio histórico de cada
contrato. A quebra por categoria (managed money, producer/merchant, swap dealer) usada
nesta leitura para aprofundar a análise de fluxo também não tem série histórica de
comparação — os números absolutos de 07/07 são o único ponto de referência disponível.

**7. Palma malaia (MPOB) segue sem números extraídos** (12/07/2026, mesmo texto de
HTML ~3.439 caracteres sem valores, 28º dia consecutivo) — impossível avaliar o efeito
de El Niño ou das restrições indonésias sobre o prêmio de substituição do óleo de soja.

**8. O checkpoint D+45 de [[2026-05-26_subvencao-fossil-aperta-biodiesel]] venceu em
10/07/2026 sem resposta** (já registrado nas duas últimas leituras) — segue sem
resposta hoje, sem fonte nova disponível para as quatro perguntas de revisão programada
daquele insight.

**9. Dados de clima INMET (BR) não foram usados como driver desta leitura.** Julho é
entressafra da soja brasileira (colheita já concluída, plantio só em outubro) —
monitoramento de rotina, sem relevância direta para a tese de preço neste momento do
calendário agrícola.

**10. RIN D4 como parâmetro fixo (2,11 USD/RIN) segue sendo uma fonte relevante de
incerteza do modelo de biodiesel**, sem novo dado hoje.

**11. BCBA Argentina — sem relatórios de esmagamento/exportação acessíveis via
scraper** (page_fetched=1,0 mas sem links de relatório, 12/07/2026, sem atualização).

**12. Notícias Agrícolas/Farm Progress RSS (12/07/2026, 160 itens lidos, 3 mantidos)
não trouxe nenhuma manchete específica destacada no dump para hoje** — diferente de
dias anteriores da semana, que citavam manchetes pontuais (compras chinesas, clima
americano). A ausência pode simplesmente refletir menor volume de notícia de fim de
semana, não uma mudança de fundamento.

*Nenhum número foi inventado ou estimado além do que consta no briefing de 12/07/2026 e
nos insights anteriores referenciados. A contribuição central desta leitura foi
reconhecer que não há dado de mercado novo (fim de semana) e usar essa pausa para
fechar formalmente o checkpoint D+7 da tese de 11/06 (gatilho tático do bear-farelo não
confirmado, tese estrutural ABIOVE preservada para os checkpoints de setembro e
dezembro), aprofundar a leitura do COT por categoria de trader (producer/merchant vs.
swap dealer, não detalhado em profundidade nas leituras anteriores) e registrar que a
MP 1.358 passou do seu prazo de vigência sem confirmação de desfecho — um vetor fiscal
que segue em aberto e deve ser a primeira coisa a verificar na leitura de amanhã.*
