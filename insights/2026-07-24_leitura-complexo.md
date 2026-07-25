---
data: 2026-07-24
titulo: "Soja rompe com força e fecha a 77,8% do range do dia, e o COT (CFTC) de 21/07 — finalmente publicado depois de 10 dias de atraso — confirma que os fundos compraram agressivamente as três pernas durante toda a semana do rompimento (net long +73,6% em soja, +57,8% em farelo, +11,4% em óleo); mas o óleo diverge sozinho, caindo -1,81% e fechando a 2,7% da mínima, comprimindo a margem de crush para o menor nível da janela (2,9616 USD/bu) e derrubando o oil share para fora da faixa recente de 53%"
tags: [complexo, auto-claude]
fontes:
  - CBOT CME (ZSU26 soja / ZMU26 farelo / ZLU26 óleo + curva forward completa Q26-H27/F27) — sessão de 2026-07-24
  - CME heating_oil_cbot (HO=F) — fechamento de 2026-07-24 (4,1311 USD/galão, volume 41.488 contratos)
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, paridade BR, ISF, ISO) — 2026-07-24, com comparação contra os mesmos indicadores recalculados para 2026-07-23 dentro do próprio dump de hoje
  - BCB PTAX — 2026-07-24 (USD/BRL 5,0666, EUR/BRL 5,7683)
  - CEPEA/ESALQ Paranaguá via NAG — última leitura disponível 2026-07-23 (suporte R$ 147,47/saca, var +1,39%; sem novo print para 24/07 neste dump)
  - CEPEA/ESALQ Paraná interior via NAG — última leitura disponível 2026-07-23 (R$ 139,28/saca, var +1,04%; sem novo print para 24/07 neste dump)
  - NAG Físico BR (farelo MT/IMEA, RS, Rondonópolis; prêmios export PGUA farelo/óleo) — 2026-07-24
  - CFTC COT Managed Money — corte de 2026-07-21, publicado hoje pela primeira vez (fila `release-cftc_cot-2026-07-21`), comparado contra o corte anterior de 2026-07-14
  - USDA Crop Progress — ainda 2026-07-19 (13% excelente + 53% boa + 6% ruim = 66% bom-ou-excelente), sem nova publicação
  - USDA WASDE — ainda 2026-07-10 (só farelo Argentina/Brasil/China parcial), sem publicação nova
  - NOPA — fila `release-nopa-2026-07-24`, `monthly_status` continua em 0,0 bool (paywall), sem dado interpretável novo
  - ABIOVE projeções mensais — balanços ago-dez/2026 (farelo/óleo/soja), sem alteração frente às leituras anteriores
  - NOAA CPC ENSO — 2026-07-24 (El Niño Advisory, sem mudança)
  - MPOB — 2026-07-24 (parser sem números extraídos, 3.439 caracteres, agora 15º dia consecutivo com o mesmo conteúdo, 10/07 a 24/07)
  - BCBA — 2026-07-22 (última leitura do scraper, acessível, sem links de relatório detectados, mesmo padrão)
  - Notícias Agrícolas/Canal Rural/Farm Progress RSS — 2026-07-24 (160 itens lidos, 6 mantidos; manchete "Frost-damaged soybeans see late-season gains", Farm Progress, sem número de preço ou área)
  - Forecasts estatísticos internos — 2026-07-24 (décima geração seguida com as seis bandas simultaneamente em viés altista)
  - system/tributario_watch.toml (lido apenas como referência, não editado) — MP-1358-2026 (`vigencia_ate` 11/07/2026, 13 dias vencida), PIS/COFINS-BIODIESEL-ISENCAO (`vigencia_ate` 31/07/2026, 7 dias restantes — trata `trib-PISCOFINS-BIODIESEL-ISENCAO-2026-07-31`), MP-1363-2026, STJ-RESP-2165276, B16-CNPE-2026, EPA-RFS-2026-2027, 45Z-CLEAN-FUEL, DANANTARA-INDONESIA, INDONESIA-B50, INDONESIA-LEVY-PMK9 — todos `atualizado_em` 2026-06-05 (49 dias sem atualização do monitor)
  - Cruza com [[2026-07-23_leitura-complexo]], [[2026-07-22_leitura-complexo]], [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (checkpoint D+7, tratado abaixo — hoje 36 dias vencido)
status: ativa
vies: [bull-soja, neutral-farelo, bear-oleo_soja]
---

> **Nota de proveniência (recorrente nesta série, hoje mais acentuada que o
> habitual):** dois recálculos do passado embutido no dump de hoje divergem
> das leituras anteriores por margem maior que o padrão documentado até
> agora. Primeiro, a soja: a leitura de ontem (23/07) registrou o fechamento
> daquele dia em 1.227,75 cts/bushel; o recálculo de hoje, embutido na
> fórmula de crush margin dos indicadores ("farelo 328,80 + óleo 74,69 −
> soja 1.231,00"), usa **1.231,00** — uma diferença de 3,25 pontos (0,26%),
> **a maior divergência de fechamento já registrada nesta série** (as
> anteriores giravam em torno de 0,01-0,25 pontos). Segundo, e mais grave: o
> heating oil (HO=F) de 23/07. A leitura de ontem, citando diretamente o
> dump daquele dia, registrou fechamento de 4,2531 USD/galão com **volume de
> apenas 29 contratos** — e usou esse volume baixíssimo como base para
> descartar, por baixa confiabilidade, a expansão de margem de biodiesel
> daquele dia. O dump de hoje traz a mesma sessão de 23/07 com fechamento de
> **4,3416 USD/galão e volume de 25.967 contratos** — quase 900 vezes mais
> volume do que o registrado ontem. Isso muda a leitura retrospectiva de
> forma material: **o alerta de baixa liquidez de ontem provavelmente
> refletia um artefato de pipeline (dado parcial no momento da coleta), não
> a liquidez real do mercado.** Não há como confirmar a causa raiz a partir
> deste briefing (ver Honestidade, item 1), mas o tamanho da revisão é
> grande o suficiente para tratar com ceticismo redobrado qualquer alerta
> futuro de "volume baixo" nesta série até o padrão se esclarecer. Por
> consistência interna, todos os deltas desta leitura contra "ontem" usam os
> valores de 23/07 **tal como recalculados dentro do próprio dump de hoje**
> (soja 1.231,00 / farelo 328,80 / óleo 74,69 / HO 4,3416).

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

**Hoje é o dia em que a pergunta mais importante das últimas duas semanas
finalmente ganhou resposta parcial: o rompimento de preço teve, de fato,
compra real de fundos por trás dele?** O CFTC (Commodity Futures Trading
Commission, o regulador americano de futuros) publica semanalmente o COT
(Commitments of Traders), um raio-x de quem está posicionado em cada
mercado — hoje, pela primeira vez em 10 dias, chegou o corte referente a
21/07/2026 (fila `release-cftc_cot-2026-07-21`), cobrindo exatamente a
semana em que soja e farelo romperam resistências (20-22/07). A resposta é
inequívoca: **o "managed money"** (fundos especulativos geridos
profissionalmente, a categoria da CFTC que mais se aproxima de dinheiro
direcional puro) **comprou pesado nas três pernas**, tanto adicionando
posições compradas quanto recomprando posições vendidas — net long em soja
subiu de 75.191 para 130.505 contratos (+73,6%), em farelo de 46.576 para
73.476 (+57,8%), em óleo de 107.945 para 120.246 (+11,4%). Isso resolve, ao
menos para a semana observada, a dúvida que dominou as duas últimas leituras
("o rompimento tem lastro em fluxo real ou é só técnico?") — a resposta é
que teve, sim, fluxo real de fundos por trás do movimento inicial. **O que
o COT não resolve é a sessão de ontem (23/07, um dia de exaustão nas três
pernas) nem a de hoje**, porque o corte semanal do CFTC fecha às
terças-feiras — a foto de 21/07 já está, portanto, uma sessão e meia
desatualizada frente ao pregão de hoje.

E o pregão de hoje trouxe uma divergência nova dentro do próprio complexo.
**A soja confirmou a força com um fechamento perto da máxima do dia**: abriu
em 1.229,50, foi a 1.243,00 na máxima, recuou a 1.225,00 na mínima, e fechou
em 1.239,00 — a 77,8% do próprio range diário, o oposto do padrão de
rejeição de ontem. **O farelo ficou no meio do caminho**: fechou em 331,10,
a exatos 50,0% do range do dia, nem confirmando força nem mostrando
fraqueza. **O óleo foi na direção contrária das outras duas pernas**: caiu
-1,81% frente a ontem, fechando em 73,34, a apenas 2,7% da mínima do dia
(73,30) — a vela mais fraca do complexo hoje, e a primeira queda absoluta
consecutiva desde a reversão tática do início da semana. Essa divergência
tem uma consequência mecânica direta: como a soja (o custo do crush) subiu
mais forte do que a soma de farelo+óleo (a receita), **a crush margin caiu
-5,67% hoje, de 3,1395 para 2,9616 USD/bushel — o primeiro valor abaixo de
3,00 em toda a janela recente**, e o oil share recuou de 53,18% para 52,55%,
saindo pela primeira vez da faixa de 53,0-53,5% em que vinha oscilando desde
20/07. **O que mudou hoje:** (1) o COT de 21/07, o dado mais aguardado das
últimas duas leituras, chegou e confirmou compra de fundos nas três pernas
durante a semana do rompimento (trata `alerta-quebra_resistencia-soja_cbot-2026-07-24`
e `alerta-quebra_resistencia-farelo_cbot-2026-07-24`); (2) a soja reverteu
com força o sinal de exaustão de ontem, fechando a 77,8% do range e ainda
mais distante (+5,0%) da resistência rompida de 1.180,00; (3) o óleo, ao
contrário, caiu de forma isolada e fechou perto da mínima, quebrando a
divergência favorável que vinha sustentando desde o início da semana; (4)
a crush margin comprimiu para o menor nível da janela e o oil share saiu
da faixa recente; e (5) o físico de farelo em Mato Grosso (IMEA) saltou
+4,18% depois de sete dias parado, um sinal doméstico novo que ainda não
tinha aparecido nesta série. **Leitura de uma linha:** o pivô do complexo
hoje é a soja — confirmação de força com lastro de fluxo real de fundos —
mas a maior convicção da leitura está no COT (evidência de compra
coordenada), não no preço de hoje isoladamente; a confiança geral é
moderada-alta para soja, baixa para farelo (ainda preso entre COT bullish
e ratio tecnicamente indefinido) e baixa para óleo, cuja divergência de
hoje é o primeiro dado tático a favor de reduzir exposição comprada na
perna mais concorrida (18,17% do open interest em managed money net long,
CFTC 21/07) das três.

---

## Soja

**Viés: bull tático — fechamento de 1.239,00 (CBOT, 24/07/2026), a 77,8% do
range do próprio dia, reverte com força o padrão de rejeição de ontem e
amplia a distância acima da resistência rompida de 1.180,00 para +5,0%. O
COT de 21/07, publicado hoje, confirma compra líquida de fundos de +73,6% na
semana do rompimento — o dado de maior peso desta leitura. Trata
`alerta-quebra_resistencia-soja_cbot-2026-07-24`.**

### O que sustenta a tese

**A vela de hoje é o espelho invertido da de ontem.** Abertura 1.229,50,
fechamento 1.239,00 (+9,50, +0,77% frente à própria abertura), mínima
1.225,00, máxima 1.243,00, volume 26.848 contratos (CBOT, ticker ZSU26.CBT,
24/07/2026). O fechamento ficou em 77,8% do range do dia
((1.239,00-1.225,00)÷(1.243,00-1.225,00)) — o oposto dos 32,7% de ontem, e a
vela mais decisiva desta janela desde o rompimento original. Frente ao
fechamento de ontem (1.231,00, ver nota de proveniência), o ganho foi de
+8,00 pontos (+0,65%). A resistência original de 1.180,00, rompida em
meados de julho, agora está **5,0% abaixo** do fechamento de hoje
((1.239,00-1.180,00)÷1.180,00) — a maior distância de toda a janela de
acompanhamento, um sinal de que o rompimento não só se sustentou como
ganhou nova perna de força hoje.

**O COT (CFTC, corte de 21/07/2026, publicado hoje) é o dado central desta
leitura para a soja.** Managed money (fundos especulativos, a categoria que
mais se aproxima de posicionamento direcional puro dentro do relatório)
elevou a posição comprada de 145.930 para 180.163 contratos (+23,5%) e
reduziu a posição vendida de 70.739 para 49.658 (-29,8%) — o resultado
combinado é um salto na posição líquida comprada (net long) de 75.191 para
**130.505 contratos, um ganho de +73,6% em uma única semana**. Como fração
do open interest total (1.045.077 contratos, +4,0% frente à semana
anterior, refletindo entrada de capital novo no mercado, não só rotação
entre participantes), o net long subiu de 7,48% para **12,49%** — ainda
distante de níveis historicamente extremos (que costumam superar 20-25% em
ciclos de alta pronunciada, embora este briefing não traga série histórica
de percentis para calibrar isso com precisão, ver Honestidade), mas um
salto expressivo em uma única semana. **O mecanismo importa: essa não é uma
semana qualquer — é exatamente a semana em que a soja rompeu 1.180,00
(20-22/07)**, então o COT está dizendo que o rompimento teve, de fato,
dinheiro novo de fundos entrando a favor do movimento, e não apenas
reposicionamento técnico de curto prazo dentro de quem já estava posicionado.
Isso é a resposta mais concreta, até agora, à pergunta que as duas últimas
leituras deixaram em aberto.

**A curva forward manteve a estrutura de prêmio crescente nos vencimentos
mais distantes.** Setembro/26 (U26, spot) 1.239,00 → Novembro/26 (X26)
1.252,50 (+13,50 sobre o spot, +1,09%) → Janeiro/27 (F27) 1.265,50 (+13,00
sobre novembro, +1,04%) → Março/27 (H27) 1.263,25 (-2,25, -0,18%,
praticamente estável) — o mesmo padrão de contango moderado e crescente
documentado nas leituras recentes, sem sinal de estresse ou inversão
mesmo com o salto de preço de hoje. Agosto/26 (Q26) fechou em 1.246,75,
um prêmio de +0,63% sobre o spot de setembro — igualmente estável.

**A paridade teórica em reais avançou para R$ 138,39/saca 60kg** (indicadores,
CBOT 1.239,00 cts × PTAX 5,0666 USD/BRL de 24/07/2026), um ganho de +0,51
(+0,37%) frente aos R$ 137,88/saca implícitos de ontem — um ganho menor,
proporcionalmente, do que o ganho em dólar (+0,65%), porque o câmbio
trabalhou contra a paridade desta vez: o real se valorizou (USD/BRL caiu de
5,0807 para 5,0666, -0,28%) no mesmo dia em que a soja em dólar subiu. **O
físico de Paranaguá ainda não tem print novo neste dump** — a última leitura
disponível (CEPEA/ESALQ via NAG) segue sendo a de ontem, R$ 147,47/saca
(var +1,39% naquele dia). Comparando esse físico desatualizado contra a
paridade fresca de hoje, o prêmio aparente cai para +6,56%
((147,47-138,39)÷138,39) — ante os +6,95% que o mesmo físico representava
contra a paridade de ontem (137,88) — mas essa leitura precisa ser tratada
com cautela: não é uma comparação de mesmo dia, e sim papel de hoje contra
físico de ontem; o print de físico de hoje só deve aparecer no dump de
amanhã. O mesmo vale para o Paraná interior, também parado no valor de
ontem (R$ 139,28/saca, var +1,04% naquele dia), cujo prêmio aparente sobre
a paridade de hoje cai para +0,64% (ante +1,02% contra a paridade de
ontem) — mais uma vez, sem confirmação de mesmo dia.

**O USDA Crop Progress segue parado em 19/07/2026** (13% excelente + 53% boa
+ 6% ruim = 66% bom-ou-excelente), sem atualização nova. A próxima
publicação semanal é esperada por volta de 26/07/2026.

**Os forecasts estatísticos internos (24/07/2026)** seguem altistas e
deslocaram para cima com o preço de hoje: central 7d = 1.267,89 cts/bu
(bandas 1.215,36-1.320,42); central 30d = 1.377,42 cts/bu (bandas
1.268,66-1.486,17) — ambos acima de ontem, mas vale lembrar, como em todas
as leituras anteriores desta série, que o modelo reage a médias móveis e
momentum de vários dias, e hoje esse momentum finalmente voltou a apontar
na mesma direção que o preço do dia (diferente de ontem, quando o modelo
seguia altista apesar da vela de rejeição).

### O que invalida / risco para a soja

- **Um fechamento amanhã abaixo de 1.225,00 (mínima de hoje)** devolveria
  parte da força mostrada hoje e reabriria a dúvida tática que a sessão de
  ontem havia introduzido.
- **Um fechamento abaixo de 1.180,00** (agora 5,0% de distância, a maior
  margem de segurança desta janela) encerraria por completo a leitura
  tática de continuidade — mas exigiria uma reversão muito mais expressiva
  do que qualquer coisa vista até agora.
- **O próximo corte do COT (28/07, publicação normal ~31/07) mostrar
  realização de lucro** depois do salto de +73,6% desta semana — um recuo
  do net long, mesmo que o preço continue subindo, seria o primeiro sinal
  de que a compra de fundos já capturou a maior parte do movimento.
- **O prêmio físico de Paranaguá (última leitura +6,56% sobre a paridade de
  hoje, mas com defasagem de um dia) continuar esticando** quando o print
  de físico de hoje for publicado amanhã — confirmaria um mercado
  exportador fisicamente mais apertado do que o papel sozinho sugere.

### Leitura operacional — soja

A sessão de hoje resolve, ao menos taticamente, a dúvida que a rejeição de
ontem havia introduzido: o preço não só recuperou o terreno perdido como
fechou perto da máxima do dia, e o COT confirma que há fluxo real de fundos
por trás do movimento da semana. Para quem está comprado alinhado ao
rompimento, a leitura de hoje é a mais favorável desde o início do
movimento — não há motivo para reduzir posição, e a distância maior até o
nível estrutural (1.180,00, agora a 5,0%) dá mais espaço para operar com um
stop tático na mínima de hoje (1.225,00) em vez de um stop mais apertado.
Para quem está vendido contra o rompimento, o dado de hoje — sobretudo o
COT — é o primeiro sinal genuinamente desfavorável à posição desde que a
rejeição de ontem havia dado alguma esperança tática: operar vendido soja
agora significa apostar contra um movimento que tem, comprovadamente,
compra de fundos por trás. Isso não invalida uma posição vendida estrutural
baseada em outra tese (por exemplo, oferta futura), mas eleva o risco de
uma posição vendida puramente tática neste momento.

---

## Farelo

**Viés: neutro — tensão real entre um COT fortemente bullish (net long
+57,8% na semana) e um preço/ratio que não confirmaram força de forma
decisiva hoje. Fechou em 331,10, exatamente no meio do range do dia (50,0%),
ainda acima da resistência rompida de 325,00 (+1,88%). O ratio Far/Soj mal
se moveu (80,13%→80,17%), permanecendo na zona neutra, longe de confirmar
tanto a reversão bull quanto a tese estrutural bear. Trata
`alerta-quebra_resistencia-farelo_cbot-2026-07-24` e a revisão
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`.**

### O que sustenta a tese

**A vela de hoje é ambígua por construção — nem forte, nem fraca.**
Fechamento 331,10 USD/short ton (CBOT, ticker ZMU26.CBT, 24/07/2026),
abertura 329,40, mínima 327,90, máxima 334,30, volume 35.887 contratos — um
ganho de +1,70 (+0,52%) frente à própria abertura e de +2,30 (+0,70%)
frente ao fechamento de ontem (328,80, ver nota de proveniência). O
fechamento ficou em exatos 50,0% do range do dia
((331,10-327,90)÷(334,30-327,90)) — nem o padrão de força de 22/07, nem o
de rejeição de 23/07. A resistência de 325,00, rompida em 22/07, segue
respeitada como suporte, com a mínima de hoje (327,90) 2,90 pontos acima
dela — uma margem de segurança semelhante à de ontem (2,70 pontos).

**O COT (CFTC, corte de 21/07/2026) é fortemente bullish para o farelo, e
está em tensão direta com a tese estrutural bear (ABIOVE).** Managed money
elevou a posição comprada de 119.347 para 130.152 contratos (+9,1%) e
reduziu a posição vendida de 72.771 para 56.676 (-22,1%) — o net long saltou
de 46.576 para **73.476 contratos, +57,8% na semana**, e como fração do
open interest (618.289 contratos, +3,2%) subiu de 7,77% para **11,89%**.
Esse é o mesmo mecanismo da soja: fundos compraram farelo de forma
coordenada durante a semana do rompimento de 325,00 (22/07). **A tensão
central da leitura de hoje é que esse posicionamento crescente de fundos
compradores está de frente com a tese estrutural bear (ABIOVE, ISF em
80/100), que não mudou.** Um mercado em que os fundos estão cada vez mais
comprados contra um pano de fundo estrutural de excedente é, classicamente,
a configuração que precede tanto um "short squeeze" (se o dado estrutural
vier fraco e forçar cobertura de posições vendidas remanescentes) quanto uma
reversão brusca (se os fundos decidirem que a tese estrutural prevalece e
começarem a vender a posição comprada recém-construída). Nenhum dos dois
cenários pode ser descartado com o dado de hoje.

**O ratio Far/Soj mal se moveu: 80,13% (ontem, recalculado hoje) →
80,17% hoje, um ganho de apenas +0,04 ponto percentual.** A revisão
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, com
data-alvo original 18/06/2026, está hoje **36 dias vencida**. A tese
original apostava em ratio comprimindo para <80% (gatilho tático), prêmio
de exportação zerado (ainda verdadeiro, ver abaixo) e estrutura de crush
favorecendo o óleo (também ainda verdadeiro, embora tenha perdido força
hoje — ver seção Óleo). **O pilar tático segue, pelo sexto pregão seguido,
tecnicamente indefinido**: o ratio não fechou abaixo de 80% desde 20/07
(mínimo 79,28% naquele dia), mas também não rompeu de forma decisiva a
máxima recente de 80,65% (22/07) — hoje ficou praticamente parado dentro
dessa faixa estreita, mesmo com o COT trazendo o dado mais bullish da
semana para o farelo. Isso é, em si, uma informação: se o posicionamento de
fundos subiu tanto e o preço/ratio mal reagiu, o mercado pode já estar
"pagando" boa parte dessa notícia, ou a compra de fundos pode estar mais
concentrada em soja/óleo (via arbitragem de crush) do que em farelo
isoladamente.

**A crush margin caiu -5,67% hoje, de 3,1395 para 2,9616 USD/bushel** (Board
Crush: farelo 331,10 + óleo 73,34 − soja 1.239,00) — o primeiro valor abaixo
de 3,00 em toda a janela recente (07-20: 3,0316; 07-21: 3,1047; 07-22:
3,1895; 07-23 recalc: 3,1395; 07-24: **2,9616**). O mecanismo: a soja (o
insumo/custo) subiu +0,65% enquanto farelo (+0,70%) e principalmente óleo
(-1,81%) não acompanharam no lado da receita — o custo subiu mais rápido
que a soma dos produtos. Isso é um sinal, ainda que de um único dia, de que
o incentivo econômico ao esmagamento ficou marginalmente menos atraente
hoje, mesmo com o preço do farelo em alta absoluta — uma distinção
importante entre "farelo mais caro" e "crush mais lucrativo", que nem
sempre andam juntos.

**O oil-meal spread comprimiu -20,3% para 0,7832 USD/bushel** (ante 0,9823
ontem) — o mecanismo é simétrico ao da crush margin: o farelo subiu
enquanto o óleo caiu, então o farelo ganhou terreno relativo sobre o óleo
dentro do valor do crush. Isso é, na prática, o farelo "vencendo" o óleo
hoje dentro da disputa por participação no valor total esmagado — um sinal
tático a favor de operações relativas que comprem farelo contra óleo (ver
Spreads e crush).

**A trajetória projetada da ABIOVE (sem alteração) segue sendo o pilar mais
sólido do argumento estrutural, porque não depende do preço do dia.** A
exportação de farelo brasileiro projetada cai de 1.400 mil toneladas em
agosto/2026 para 700 mil toneladas em dezembro/2026 (-50% em quatro meses),
enquanto a produção cai de forma bem mais suave (2.285,06 → 1.659,04 mil
toneladas no mesmo período, -27,4%) — menos farelo saindo pelo porto, com
produção caindo bem menos que a exportação, empurra o volume excedente para
o mercado interno de ração. Esse mecanismo estrutural não é afetado nem
pelo COT bullish de hoje nem pela ambiguidade tática do ratio.

**As praças físicas de farelo no Brasil (NAG, 24/07/2026) trouxeram o
primeiro movimento doméstico relevante desta janela.** Mato Grosso/IMEA
saltou **+4,18% para R$ 1.669,72/ton**, encerrando sete dias parado em R$
1.602,80 (desde 17/07). É o maior salto físico desta série recente e o
primeiro sinal de que o mercado interno de ração pode estar reagindo a algo
— possivelmente a própria força de preço-papel da semana, possivelmente
demanda genuína de ração. Rondonópolis/MT segue em R$ 1.650,00/ton, estável
pelo 5º dia seguido (desde o salto de +3,13% em 20/07); Rio Grande do Sul
segue em R$ 1.640,00/ton, parado desde pelo menos 14/07. O prêmio de
exportação em Paranaguá permanece em +0,05 USD/short ton (julho/26, NAG),
agora **21 dias corridos sem qualquer variação** desde 03/07/2026 — o
físico exportador segue tão parado quanto na tese original de 11/06/2026
("prêmio de exportação zerado"), mesmo com o salto do IMEA no mercado
doméstico — uma dissociação entre o canal doméstico (que hoje mostrou
sinal de vida) e o canal de exportação (que segue congelado), coerente com
a tese ABIOVE de que o excedente de farelo está sendo absorvido
internamente, não exportado.

**O Índice de Sobra de Farelo (ISF) permanece em 80/100 (4 de 5 condições
estruturais)**, inalterado desde pelo menos 01/07/2026 — mais uma
confirmação de que o índice captura condições estruturais (ABIOVE, crush,
oferta), não a mecânica tática de preço de curto prazo ou o COT recém-
publicado.

**O forecast estatístico do farelo (24/07/2026)** segue com viés altista:
central 7d = 338,23 USD/sht (bandas 324,74-351,71); central 30d = 365,55
USD/sht (bandas 337,63-393,48) — ambos acima de ontem, refletindo o ganho
de preço de hoje, mas sem captar a ambiguidade do fechamento no meio do
range.

### O que invalida / risco para o farelo

- **Um fechamento amanhã abaixo de 325,00** desfaria o sinal tático do
  rompimento, mesmo com o COT bullish — o mercado de futuro tende a
  respeitar preço acima de posicionamento de fundos no curtíssimo prazo.
- **O ratio fechar abaixo de 80%** devolveria o quadro tático integralmente
  a favor da tese estrutural bear original, apesar do COT — o pilar mais
  citado desta série de leituras para arbitrar a revisão vencida.
- **O próximo corte do COT (28/07, publicação ~31/07) mostrar reversão do
  net long** — se os fundos que compraram nesta semana começarem a vender,
  a configuração de tensão entre COT e ABIOVE se resolveria a favor da
  tese estrutural bear.
- **O salto do físico em MT/IMEA (+4,18% hoje) não se confirmar amanhã** —
  se for revertido ou não repetido, seria mais consistente com ruído de um
  dia do que com uma mudança genuína de demanda doméstica.
- **NOPA seguir inacessível**, sem confirmação do esmagamento americano
  para os checkpoints D+90 (09/09/2026) e D+180 (08/12/2026).

### Leitura operacional — farelo

O dado mais importante de hoje para quem opera farelo não é o preço — é o
COT. Fundos compraram pesado durante a semana do rompimento (net long
+57,8%), o que é um contraponto real e cada vez mais difícil de ignorar à
tese estrutural bear (ABIOVE/ISF). Para quem mantém posição vendida
estrutural, a recomendação desta leitura é a mesma das últimas sessões:
manter a tese via spread (farelo/soja ou crush completo) em vez de posição
vendida outright, porque o risco de um "short squeeze" alimentado por fluxo
de fundos comprado é real e crescente — hoje mais do que ontem. Para quem
está comprado tático desde o rompimento de 325,00, o fechamento no meio do
range não é um sinal forte o suficiente para aumentar posição, mas o COT dá
suporte para manter a posição com o stop na mínima de hoje (327,90) ou no
nível estrutural (325,00). O salto do físico em Mato Grosso é um dado novo
a acompanhar de perto amanhã — se confirmado, reforça o lado comprado
tático; se revertido, é apenas ruído. A operação relativa mais atraente
hoje, dado o oil-meal spread comprimindo -20,3%, é comprar farelo contra
óleo dentro do crush — capturando exatamente a divergência que apareceu
hoje entre as duas pernas.

---

## Óleo

**Viés: bear tático — primeira queda absoluta isolada da semana (-1,81%),
fechando a apenas 2,7% da mínima do dia, a vela mais fraca do complexo
hoje. O oil share caiu para 52,55% (ante 53,18% ontem), saindo da faixa de
53,0-53,5% em que vinha oscilando desde 20/07. Estrutural, ainda bull via
ISO 100/100 e COT mais concorrido das três pernas — mas hoje é o primeiro
dado tático a favor de reduzir exposição.**

### O que sustenta a tese

**O óleo foi a única perna do complexo a cair de forma isolada hoje, e com
um fechamento particularmente fraco.** Fechamento 73,34 cts/lb (CBOT,
ticker ZLU26.CBT, 24/07/2026), abertura 74,53, mínima 73,30, máxima 74,77 —
uma queda de -1,19 (-1,60%) frente à própria abertura e de -1,35 (-1,81%)
frente ao fechamento de ontem (74,69, ver nota de proveniência). O
fechamento ficou em apenas 2,7% do range do dia
((73,34-73,30)÷(74,77-73,30)) — o pior fechamento relativo das três
commodities hoje, e um contraste direto com a soja (77,8%) e o farelo
(50,0%). Diferente de farelo e soja, que romperam e sustentaram níveis
técnicos nas últimas duas semanas, o óleo não tinha um nível de resistência
citado na fila de julgamento — mas o padrão de hoje (máxima testada e
rejeitada, fechamento na mínima) é tecnicamente idêntico ao padrão de
exaustão que soja e farelo mostraram ontem, só que um dia depois e sem a
reversão que a soja teve hoje.

**A curva forward aprofundou ainda mais a backwardation (desconto crescente
nos vencimentos mais distantes), mantendo o padrão já documentado em
leituras anteriores — mesmo com a queda de hoje.** Agosto/26 (Q26) 74,14 →
Setembro/26 (U26, spot) 73,34 (-0,80, -1,08%) → Outubro/26 (V26) 72,55
(-0,79, -1,08%) → Dezembro/26 (Z26) 71,87 (-0,68, -0,94%) → Janeiro/27 (F27)
71,46 (-0,41, -0,57%) — uma queda total de -2,68 cts/lb (-3,61%) de agosto a
janeiro/27, uma compressão ligeiramente menor que a de dias anteriores. A
força relativa segue concentrada no vencimento mais próximo — a mesma
assinatura de aperto físico de curto prazo mais do que reprecificação
estrutural de toda a curva —, mas o fato de o spot ter caído mais em termos
absolutos do que os vencimentos distantes hoje é consistente com a queda
de hoje sendo, ao menos em parte, um ajuste de curto prazo, não uma
reavaliação da tese de médio prazo.

**A margem de biodiesel americano caiu -9,88% no dia, para 0,9956 USD/galão**
(receita 7,2961 = heating oil 4,1311 + 1,5×RIN 2,11; custo 6,3005 = óleo
5,5005 + industrial 0,80), ante 1,1048 ontem (recalculado, ver nota de
proveniência). **O mecanismo aqui é o oposto do que se poderia esperar à
primeira vista.** O custo do óleo efetivamente caiu (-1,81% em dólar,
refletindo a queda do CBOT), o que isoladamente favoreceria a margem — mas
a receita caiu ainda mais (-2,80% em termos absolutos, -3,74% relativo a
ontem), puxada pelo heating oil, que recuou -4,85% (de 4,3416 para 4,3311…
na verdade 4,1311 USD/galão, ver nota de proveniência sobre a revisão do
dado de ontem). **Isso significa que a queda de margem de hoje não é
originada no complexo soja — é originada no mercado de energia (diesel/
heating oil), que hoje operou mais fraco de forma independente.** Com o
volume do heating oil hoje em 41.488 contratos — o maior desta janela
recente, e 59,8% acima dos 25.967 contratos que o dump de hoje atribui a
ontem — esse é um dado de alta confiabilidade, ao contrário da fragilidade
de liquidez que marcou leituras anteriores (ver nota de proveniência no
topo). Ou seja: a margem caiu por um motivo real e líquido — o mercado de
energia enfraqueceu — não por um artefato de baixo volume.

**O Índice de Suporte do Óleo (ISO) permanece em 100/100 (5 de 5 condições)**,
inalterado desde pelo menos 01/07/2026 — a tese estrutural (óleo dominando
o valor do crush) segue formalmente intacta, mas vale registrar que é um
índice de condições estruturais, não reativo à queda tática de hoje; o
oil share (a métrica de captura de valor mais sensível a preço do dia)
já mostrou o primeiro sinal de reversão (ver Spreads e crush).

**O oil share caiu para 52,55%** (indicadores, 24/07/2026), ante 53,18%
ontem — uma queda de -0,63 ponto percentual, a maior queda em uma única
sessão desde pelo menos 20/07, e o primeiro valor fora da faixa de
53,0-53,5% em que o indicador vinha oscilando nos últimos cinco pregões
(53,47%→53,09%→53,07%→53,18%→**52,55%**). Isoladamente, um dia não desfaz a
tese estrutural de que o óleo "manda" no crush (ainda está acima de 50%),
mas é o primeiro dado tático que aponta na direção contrária à narrativa
dominante das últimas semanas.

**O COT (CFTC, corte de 21/07/2026) confirma que o óleo é, de longe, a
perna mais concorrida das três — e isso é tanto suporte estrutural quanto
risco.** Managed money elevou a posição comprada de 133.321 para 143.159
contratos (+7,4%) e reduziu a posição vendida de 25.376 para 22.913
(-9,7%) — o net long subiu de 107.945 para **120.246 contratos, +11,4% na
semana**, a menor variação percentual das três pernas, mas o nível
absoluto mais alto: como fração do open interest (661.652 contratos, +3,7%),
o net long está em **18,17%** — o mais alto entre soja (12,49%) e farelo
(11,89%), e também o mais alto desta janela recente para o próprio óleo
(ante 16,92% na semana anterior). Um posicionamento tão assimétrico é, ao
mesmo tempo, evidência de convicção de fundos na tese estrutural (óleo
dominando o crush, apoio de biodiesel/RIN D4) e o maior fator de risco de
uma correção mais aguda se o sentimento virar — a queda isolada de hoje é o
primeiro dado tático a apontar nessa direção.

**O forecast estatístico do óleo (24/07/2026)** mantém o viés altista:
central 7d = 75,77 cts/lb (bandas 71,11-80,42); central 30d = 84,39 cts/lb
(bandas 74,75-94,03) — mas como o modelo reage a médias de vários dias e
momentum recente (que ainda é positivo olhando a janela mais ampla), ele
não captura a queda isolada de hoje.

### O que invalida / risco para o óleo

- **Um fechamento amanhã abaixo de 73,30 (mínima de hoje)** confirmaria a
  primeira sequência de dois dias de fraqueza desde o início do rali,
  reforçando o sinal tático de hoje.
- **O oil share continuar caindo abaixo de 52,55%** — se a tendência de
  hoje persistir por mais uma ou duas sessões, a narrativa estrutural de
  "óleo domina o crush" começaria a perder sustentação também no dado
  tático, não só no ISO (que é mais lento a reagir).
- **O próximo corte do COT (28/07, publicação ~31/07) mostrar realização de
  lucro no net long mais concorrido das três pernas (18,17% do OI)** — o
  risco estrutural de médio prazo mais relevante, agora com o primeiro
  dado de preço a apontar na mesma direção.
- **O mercado de energia (heating oil, diesel) continuar enfraquecendo** —
  hoje a queda de margem de biodiesel veio de fora do complexo soja; se
  persistir, reduz o apoio de demanda de biodiesel ao óleo de forma
  independente dos fundamentos agrícolas.
- **MPOB seguir inacessível** — impossível avaliar o efeito do El Niño ou
  das restrições/levy indonésias sobre o prêmio de substituição via palma.
  Hoje é o 15º dia consecutivo com o mesmo conteúdo sem números extraídos.

### Leitura operacional — óleo

Hoje é o primeiro dado tático genuinamente desfavorável ao lado comprado em
óleo desde o início do rali recente. Para quem está comprado direcional, a
recomendação é reavaliar o tamanho da posição — não necessariamente zerar,
porque a tese estrutural (ISO 100/100, backwardation na curva, RIN D4/
biodiesel) segue de pé, mas o posicionamento de fundos já é o mais
concorrido das três pernas (18,17% do OI) e hoje o preço confirmou a
primeira fraqueza isolada; um stop na mínima de hoje (73,30) é a referência
tática mais próxima. Para quem opera vendido ou via spread, hoje é o
primeiro dia em que a aposta relativa "farelo forte / óleo fraco" (capturada
pelo oil-meal spread, que comprimiu -20,3% hoje) teve confirmação de preço
nas duas pernas simultaneamente — essa é a operação mais atraente que a
leitura de hoje sugere dentro do complexo, mais do que uma posição outright
vendida em óleo, que ainda enfrentaria a tese estrutural (ISO, RIN D4)
como vento contrário.

---

## Spreads e crush — leitura de complexo

### Crush margin: 2,9616 USD/bu — primeiro valor abaixo de 3,00 na janela recente

A crush margin caiu -5,67% no dia (de 3,1395 para 2,9616 USD/bu), o menor
valor de toda a janela observada (07-20: 3,0316; 07-21: 3,1047; 07-22:
3,1895; 07-23 recalc: 3,1395; 07-24: 2,9616). O mecanismo: a soja (o custo)
subiu +0,65% enquanto a soma de farelo (+0,70%) e óleo (-1,81%) não
acompanhou — o óleo, que vinha sendo o motor da margem elevada nas últimas
semanas, foi hoje o fator que puxou a margem para baixo. Um único dia de
compressão, partindo de um nível historicamente elevado, não desfaz o
argumento estrutural de que a margem segue favorável ao processamento —
mas é o primeiro dado que sugere que o incentivo ao esmagamento pode estar
perdendo força na margem (trocadilho literal), não só figurativamente.

### Ratio Far/Soj: 80,17% — praticamente parado, ainda tecnicamente indefinido

Ganho de apenas +0,04 ponto percentual (80,13%→80,17%), o menor movimento
diário desta janela. O ratio segue preso na zona "neutra" (entre 80% e
87%), sem confirmar nem a reversão da tese estrutural bear (que exigiria
romper de forma sustentada acima de 80,65%, a máxima de 22/07) nem o
retorno à tese original (que exigiria fechar abaixo de 80%, algo que não
acontece desde 20/07). Trata `alerta-quebra_resistencia-farelo_cbot-2026-07-24`
e a revisão `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
(agora 36 dias vencida — ver seção Farelo).

### Oil share: 52,55% — primeira queda fora da faixa recente de 53,0-53,5%

Queda de -0,63 ponto percentual frente a ontem (53,18%→52,55%), a maior
variação diária desde pelo menos 20/07 e o primeiro valor fora da banda
estreita em que o indicador vinha oscilando nos últimos cinco pregões. O
óleo perdeu participação relativa no valor do crush hoje — coerente com a
queda isolada do óleo e a alta do farelo na mesma sessão.

### Oil-meal spread: 0,7832 USD/bu — compressão de -20,3%, a maior desta janela

Queda de -20,3% no dia (0,9823→0,7832 USD/bu), de longe a maior variação
diária deste indicador na janela observada. O farelo ganhou terreno
relativo sobre o óleo de forma expressiva — a operação relativa mais clara
que o dado de hoje sugere dentro do complexo (ver seções Farelo e Óleo).

### Margem de biodiesel: 0,9956 USD/gal — queda de -9,88%, mas com volume de heating oil finalmente confiável

A margem caiu -9,88% no dia, revertendo boa parte da alta (revisada) de
ontem. Diferente de leituras anteriores desta série, o dado de hoje vem com
volume de heating oil robusto (41.488 contratos, o maior da janela) — a
queda de margem, portanto, deve ser tratada como um sinal real de mercado
de energia mais fraco, não como artefato de baixa liquidez (ver nota de
proveniência).

### COT: primeira atualização em 10 dias (corte 21/07), o dado mais importante desta leitura

O corte de 21/07/2026, publicado hoje pela primeira vez (fila
`release-cftc_cot-2026-07-21`), mostra managed money comprando
agressivamente as três pernas durante a semana do rompimento: net long
+73,6% em soja, +57,8% em farelo, +11,4% em óleo. Em fração do open
interest, óleo segue sendo a perna mais concorrida (18,17%), seguida por
soja (12,49%) e farelo (11,89%). Esse dado resolve, para a semana
observada, a dúvida sobre lastro de fluxo real por trás do rompimento —
mas ainda não cobre a sessão de exaustão de ontem nem a divergência de
hoje entre soja (forte) e óleo (fraco), porque o corte fecha às
terças-feiras. O próximo corte (28/07, publicação normal ~31/07) é o
próximo dado capaz de dizer se essa compra se sustentou ou começou a
reverter.

### ISF em 80/100, ISO em 100/100 — inalterados, mas a tensão com o tático cresce

O Índice de Sobra de Farelo (4/5 condições) e o Índice de Suporte do Óleo
(5/5 condições) permanecem exatamente nos mesmos níveis de semanas
anteriores. Para o farelo, a tensão entre o índice estrutural (ainda bear)
e o COT (fortemente bullish, +57,8% na semana) é o ponto mais importante
em aberto do complexo — nenhum dos dois invalida o outro isoladamente, mas
juntos formam uma configuração clássica de mercado dividido entre fluxo
de curto prazo e fundamento de médio prazo. Para o óleo, a rejeição tática
de hoje (primeira queda isolada, oil share fora da faixa recente) é o
primeiro dado a contrastar, ainda que levemente, com o índice que segue no
teto.

### O que os índices dizem juntos em 24/07/2026

ISF 80/100 + ISO 100/100 (ambos inalterados) + ratio Far/Soj praticamente
parado (80,17%, ainda indefinido) + crush margin no menor nível da janela
(2,9616 USD/bu, primeira vez abaixo de 3,00) + oil share saindo da faixa
recente pela primeira vez (52,55%) + oil-meal spread na maior compressão da
janela (-20,3%, farelo ganhando terreno sobre óleo) + COT confirmando
compra maciça de fundos nas três pernas durante a semana do rompimento,
mais concentrada proporcionalmente em soja (+73,6%) mas em nível absoluto
mais concentrada em óleo (18,17% do OI) + margem de biodiesel caindo por um
motivo real (mercado de energia, não liquidez artificial) — formam um
quadro em que a semana do rompimento teve, comprovadamente, lastro de
fluxo real de fundos, mas a sessão de hoje já mostra a primeira divergência
interna desde então: soja e farelo (via COT) seguem fortes, enquanto óleo
mostrou a primeira fraqueza tática isolada, com a métrica mais sensível a
preço (oil share) já reagindo antes do índice estrutural (ISO). A lição
mais importante para quem opera o complexo hoje: o dado mais valioso da
leitura (o COT) é uma foto de uma semana que já passou — a leitura do
preço de hoje sugere que a força pode estar migrando de óleo para farelo/
soja dentro do próprio complexo, algo que só o COT de 28/07 vai confirmar
ou desmentir com dados de posicionamento.

---

## Lente fiscal e regulatória BR

**Isenção PIS/Cofins biodiesel — vencimento em 31/07/2026, agora a apenas 7
dias, e ainda sem sinalização pública de renovação** (evento
PISCOFINS-BIODIESEL-ISENCAO, `atualizado_em` 2026-06-05, sem mudança desde
então). Trata `trib-PISCOFINS-BIODIESEL-ISENCAO-2026-07-31`. **O mecanismo:**
a isenção incide na saída do biodiesel; se expirar sem renovação em
31/07, o custo tributário efetivo da produção de biodiesel sobe, o que
tende a reduzir a margem de biodiesel doméstica (distinta da margem
americana calculada nesta leitura, que usa RIN D4 e heating oil dos EUA) e,
por extensão, pressionar a demanda por óleo de soja como insumo dentro do
mix B15 mandatório — um vetor bearish direto para óleo, independente do
que acontecer no CBOT. **A proximidade da data (7 dias) contrasta com os 49
dias sem qualquer atualização do monitor tributário** (`atualizado_em`
2026-06-05 em todos os dez eventos rastreados) — um descompasso que, com o
vencimento agora dentro da janela de uma semana, se torna um risco de
execução concreto: se a decisão de renovar (ou não) sair de última hora,
como ocorreu com a prorrogação anterior (decreto de 29/mai, citado no
mecanismo do próprio evento), o sistema pode não capturá-la a tempo de
refletir na leitura do dia seguinte. Esta é, agora, a leitura de maior
prioridade de monitoramento tributário desta série.

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L) — a
vigência formal (`vigencia_ate` 11/07/2026) venceu há 13 dias, e o monitor
tributário segue sem qualquer atualização de status** (evento MP-1358-2026,
`atualizado_em` 2026-06-05, status ainda "tramitacao"). Enquanto o
combustível fóssil segue subsidiado, a competitividade relativa do
biodiesel dentro do mix B15 mandatório fica pressionada — um vetor
regulatório independente da margem de biodiesel americana (que hoje caiu
-9,88%, mas por um motivo genuíno de mercado de energia, ver Spreads e
crush), somando incerteza sobre a economia de processamento em duas
geografias distintas.

**B16 — sem data, travado em B15.** Sem mudança de status (evento
B16-CNPE-2026, `atualizado_em` 2026-06-05, status "adiado"). Testes técnicos
do FNDCT com resultado esperado ~nov/2026 — realista só fim de 2026/início
de 2027.

**MP 1.363/2026 (subsídio ao diesel fóssil, R$ 1,12/L) — em vigor até
31/12/2026.** Sem alteração. Bearish estrutural persistente para a demanda
incremental de óleo de soja no mercado doméstico brasileiro.

**STJ REsp 2.165.276/2026 — crédito PIS/Cofins para esmagadoras.** Sem
alteração. Bullish para soja/óleo (alívio de custo de entrada para
biodiesel) e, por extensão, incentivo a mais esmagamento — em tensão com a
contração da crush margin registrada hoje, que reduz o incentivo tático de
curto prazo mesmo com o alívio tributário estrutural intacto.

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
inverificáveis pelo lado dos dados de mercado (MPOB inacessível há 15 dias
consecutivos, ver Honestidade), e vale notar que esses vetores estruturais
não conseguiram evitar a queda tática do óleo hoje, sinal de que fatores
de curto prazo (mercado de energia, oil share) dominaram a sessão.

**O monitor tributário como um todo está há 49 dias sem qualquer
atualização** (`atualizado_em` 2026-06-05 em todos os dez eventos
rastreados) — o intervalo segue crescendo em um momento em que dois vetores
têm datas formais já vencidas ou criticamente próximas (MP 1.358, vencida
há 13 dias; isenção PIS/Cofins, a apenas 7 dias do vencimento). Vale
sinalizar este ponto, mais uma vez e com urgência crescente, como
prioridade de manutenção do sistema, independentemente da leitura de
preço.

---

## Riscos e eventos próximos

**A isenção PIS/Cofins do biodiesel vence em 31/07/2026, agora a apenas 7
dias**, sem sinalização de renovação — o vetor tributário mais próximo de
um desfecho concreto nesta leitura, e o de maior prioridade de
monitoramento até a resolução.

**O próximo corte do COT (referente a 28/07/2026, publicação normal
~31/07/2026)** é o dado mais aguardado agora — vai mostrar se a compra
maciça de fundos documentada hoje (semana de 21/07) se sustentou durante a
sessão de exaustão de 23/07 e a divergência de hoje (soja forte, óleo
fraco), ou se já começou a reverter.

**O ratio Far/Soj segue tecnicamente indefinido, agora há seis pregões
seguidos dentro da mesma faixa estreita (79,28%-80,65%)** — a revisão D+7
(`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`), hoje
36 dias vencida, segue sem resolução tática, mesmo com o COT trazendo o
dado fundamental mais relevante das últimas duas semanas.

**A divergência de hoje entre farelo (COT bullish, preço no meio do range) e
óleo (queda isolada, oil share fora da faixa recente) precisa de
confirmação nas próximas sessões** — se o óleo confirmar fraqueza por mais
um ou dois dias, a leitura de "óleo domina o crush" (ISO 100/100) começaria
a ganhar o primeiro contraponto tático desde que essa tese foi estabelecida.

**NOPA — segue inacessível** (fila `release-nopa-2026-07-24` tratada aqui,
sem dado interpretável, apenas nova data de coleta), sem crush americano
confirmado por fonte primária.

**MPOB — sem números de palma extraídos há 15 dias consecutivos**, mantendo
cego o efeito do El Niño e dos vetores regulatórios indonésios sobre o
prêmio de substituição do óleo de soja.

**Os prints físicos de soja em Paranaguá e Paraná interior (CEPEA/ESALQ via
NAG) ainda não atualizaram para 24/07** neste dump — a comparação de
prêmio sobre a paridade teórica feita nesta leitura usa o último print
disponível (23/07) contra a paridade fresca de hoje, uma comparação
imperfeita que deve se resolver com o dump de amanhã.

**Checkpoints futuros da tese estrutural do farelo (ABIOVE)** — D+90 em
09/09/2026 e D+180 em 08/12/2026 (insight
[[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]) — a revisão D+7,
agora 36 dias vencida, permanece sem resolução tática (ver seção Farelo) e
segue sem confirmação de fundamentos (WASDE, parado desde 10/07; NOPA,
inacessível); os checkpoints estruturais seguem o critério de mais alta
confiança para julgar a tese ao longo do tempo.

---

## Honestidade

O que não foi possível validar neste briefing de 24/07/2026, onde a
confiança é baixa ou há lacunas materiais:

**1. O fechamento de soja de 23/07/2026 usado como base de comparação para
os números de hoje diverge da leitura de ontem pela maior margem já
registrada nesta série.** A leitura de 23/07 registrou o fechamento daquele
dia em 1.227,75 cts/bushel; o recálculo de hoje, embutido na fórmula de
crush margin dos indicadores, usa 1.231,00 — uma diferença de 3,25 pontos
(0,26%). As divergências anteriores nesta série giravam em torno de
0,01-0,25 pontos, então esta é proporcionalmente a maior já vista. Não é
possível, a partir deste briefing, determinar a causa exata (possível
ajuste de fonte, arredondamento acumulado, ou reprocessamento do
pipeline), mas o tamanho justifica um alerta redobrado. Ainda mais
relevante: o heating oil de 23/07/2026 também divergiu de forma muito
maior que o padrão — a leitura de ontem citou fechamento de 4,2531 USD/
galão com volume de apenas 29 contratos (base para descartar a expansão de
margem daquela sessão por baixa liquidez); o dump de hoje traz a mesma
sessão com fechamento de 4,3416 e volume de 25.967 contratos — quase 900
vezes mais volume. **Isso sugere fortemente que os alertas de "volume
baixo" documentados em leituras anteriores desta série podem ter refletido
artefatos de coleta parcial no momento da publicação, não a liquidez real
do mercado.** Recomenda-se tratar com ceticismo redobrado qualquer futuro
alerta de volume baixo até que esse padrão de revisão se esclareça ou
pare de se repetir. Todos os cálculos de variação desta leitura usam
consistentemente os valores recalculados dentro do próprio dump de hoje
(soja 1.231,00 / farelo 328,80 / óleo 74,69 / HO 4,3416), por consistência
interna.

**2. A seção bruta `cme_cbot` do dump de hoje não traz os preços OHLC de
soja e óleo para a sessão de 23/07/2026** — apenas farelo e heating oil
aparecem com dado bruto completo daquele dia, a mesma lacuna documentada
nas leituras anteriores. A comparação de hoje contra ontem para soja e óleo
depende inteiramente do fechamento implícito na fórmula de crush margin dos
indicadores, não de uma confirmação direta da fonte primária CME para
aquele dia específico — o que também explica, em parte, a divergência do
item 1 acima.

**3. Os prints físicos de soja (Paranaguá e Paraná interior, CEPEA/ESALQ
via NAG) não atualizaram para 24/07/2026 neste dump** — a comparação de
prêmio sobre a paridade teórica feita na seção Soja usa o último print
disponível (23/07) contra a paridade fresca de hoje, uma comparação que
mistura dias diferentes e deve ser tratada como aproximação, não como fato
de mesmo dia.

**4. O prêmio de exportação de farelo em Paranaguá (+0,05 USD/sht) e o de
óleo (+0,08 cts/lb) estão no mesmo valor exato desde pelo menos 03/07/2026**
(NAG, agora 21 dias corridos sem variação de nenhum centavo) — não é
possível distinguir se isso reflete um mercado de exportação genuinamente
parado ou um valor que não está sendo atualizado de fato na fonte.

**5. Os níveis de resistência/suporte de 1.180,00 (soja) e 325,00 (farelo)
são alertas gerados pelo sistema de calibração interna, cuja metodologia de
definição de nível não é visível a partir deste briefing** — esta leitura
trata os níveis como dado (o sistema já os fiscaliza automaticamente), sem
poder validar de forma independente os critérios técnicos usados para
calibrá-los.

**6. O COT (CFTC) foi publicado hoje pela primeira vez em 10 dias, mas o
corte é de 21/07/2026 — uma terça-feira** — não cobre nem a sessão de
exaustão de 23/07 (quarta), nem a sessão de hoje (24/07, sexta), incluindo
a divergência entre soja forte e óleo fraco observada hoje. O próximo corte
(28/07, publicação normal ~31/07) é o primeiro capaz de capturar esse
período.

**7. Percentis históricos de COT não calculados** — os números de
21/07/2026 são lidos apenas em nível absoluto e como fração do open
interest corrente (soja 12,49%, farelo 11,89%, óleo 18,17%), sem série
histórica completa para calibrar se algum desses níveis está objetivamente
"esticado" no sentido histórico, apesar do salto expressivo na semana.

**8. O WASDE segue cobrindo apenas farelo (Argentina, Brasil, China
parcial), sem nenhum dado de soja em grão ou óleo de soja, em qualquer
geografia, e sem nenhum dado dos Estados Unidos** — sem atualização desde
10/07/2026. A pergunta central da revisão D+7 vencida ("o WASDE mudou o
quadro?") segue sem canal de resposta interno.

**9. NOPA (fila `release-nopa-2026-07-24`) segue com `monthly_status` em
0,0 bool** — mesma barreira de assinatura paga documentada desde meados de
junho, agora com quase um mês e meio sem alternativa de dado primário sobre
o esmagamento americano. A "novidade" sinalizada pela fila é apenas a data
de coleta, não um dado genuinamente interpretável — o mesmo padrão das
leituras anteriores.

**10. Palma malaia (MPOB) segue sem números extraídos, agora por 15 dias
consecutivos com o mesmo conteúdo exato (3.439 caracteres, de 10/07 a
24/07/2026)** — a persistência do byte count idêntico sugere, possivelmente,
uma página que não está mais sendo servida com conteúdo atualizado. Continua
impossível avaliar o efeito do El Niño ou dos vetores regulatórios
indonésios sobre o prêmio de substituição do óleo de soja.

**11. Clima INMET (BR) não foi usado como driver de preço desta leitura.**
Julho é entressafra da soja brasileira (colheita concluída, plantio só em
outubro) — sem relevância direta para a tese de preço neste momento do
calendário agrícola, apesar da previsão de chuva isolada em praças do
Paraná (Cascavel, Maringá) para 25/07 constar no dump. O El Niño Advisory
(NOAA CPC, inalterado desde pelo menos 03/07/2026) permanece relevante
apenas para a expectativa da safra de plantio de outubro/26 e para o clima
do Sudeste Asiático (palma).

**12. A manchete de notícia do dia ("Frost-damaged soybeans see late-season
gains", Farm Progress, 24/07/2026) não traz número de preço ou de área** e
por isso não foi tratada como driver — segue a regra de nunca inventar ou
inferir magnitude além do que consta no briefing.

**13. BCBA Argentina — última leitura disponível é 22/07/2026** (o dump de
hoje não traz uma linha nova para 24/07 na seção `bcba`), sem relatórios de
esmagamento/exportação acessíveis via scraper, sem mudança de padrão.

**14. RIN D4 como parâmetro fixo (2,11 USD/RIN) segue sendo uma fonte
relevante de incerteza do modelo de biodiesel**, sem novo dado hoje — a
margem calculada em 0,9956 USD/gal usa esse valor fixo. Diferente de
leituras anteriores, porém, o dado de hoje tem volume de heating oil
robusto (41.488 contratos), então a incerteza remanescente está
concentrada no RIN D4 fixo, não mais na liquidez do heating oil.

**15. A divergência de hoje entre a força de soja/farelo (via COT) e a
fraqueza isolada do óleo é o achado central desta leitura, e permanece sem
confirmação de mais de uma sessão** — esta leitura recomenda não tratar a
queda de hoje no óleo como início de reversão de tendência nem como ruído
de um dia isoladamente, até que o preço confirme por pelo menos mais uma
sessão. Aplicar esse padrão de forma consistente, inclusive quando o dado
do dia complica em vez de simplificar a leitura anterior, é o que preserva
a credibilidade metodológica desta série.

*Nenhum número foi inventado ou estimado além do que consta no briefing de
24/07/2026 e nos insights anteriores referenciados. A contribuição central
desta leitura foi interpretar o primeiro COT (CFTC) publicado em 10 dias —
confirmando compra maciça e coordenada de fundos nas três pernas do
complexo durante a semana do rompimento (net long soja +73,6%, farelo
+57,8%, óleo +11,4%) — e identificar que a sessão de hoje já mostra a
primeira divergência interna desde então: soja reverteu com força o sinal
de exaustão de ontem e fechou a 77,8% do range, farelo ficou ambíguo no
meio do range, e o óleo caiu isoladamente, fechando a apenas 2,7% da
mínima, derrubando o oil share para fora da faixa recente e comprimindo a
crush margin para o menor nível da janela observada. Também foi
identificada uma revisão de dados anômala e potencialmente relevante para
a credibilidade metodológica da série: o volume de heating oil de
23/07/2026, citado como 29 contratos na leitura de ontem, aparece hoje
como 25.967 contratos no mesmo dump — uma discrepância de quase 900 vezes
que sugere que alertas anteriores de "baixa liquidez" nesta série podem
ter sido artefatos de coleta parcial.*
