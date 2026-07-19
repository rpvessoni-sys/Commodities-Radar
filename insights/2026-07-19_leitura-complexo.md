---
data: 2026-07-19
titulo: "Domingo sem pregão: pela primeira vez nesta série, a terceira geração dos dados de sexta (17/07) não muda nada — ratio Far/Soj, crush, oil share e curvas completas ficam idênticos à segunda geração, só o volume do óleo volta ao valor original e o heating oil eletrônico de domingo abre com um gap leve para baixo; notícia sobre expansão de área de soja 2026/27 e MPOB parado há 10 dias completam o quadro do fim de semana"
tags: [complexo, auto-claude]
fontes:
  - CBOT CME (ZSQ26/ZMQ26/ZLQ26 + curva forward completa) — sessão de 2026-07-17 (última sessão disponível para o complexo agrícola; mercado fechado 18-19/07, fim de semana), terceira geração de dados, sem revisão frente à leitura de ontem (18/07)
  - CME heating_oil_cbot (HO=F) — nova vela de 2026-07-19 (domingo), sessão eletrônica em andamento, volume baixo (859 contratos)
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, paridade BR) — datados de 2026-07-17, idênticos à segunda geração de ontem; ISF/ISO recalculados hoje (2026-07-19), sem variação
  - BCB PTAX — ainda 2026-07-17 (USD/BRL 5,1176), sem publicação nova (fim de semana, sem pregão bancário)
  - CEPEA/ESALQ Paranaguá e Paraná interior via NAG — ainda 2026-07-17 (suporte Paranaguá R$ 141,02/saca, Paraná interior R$ 134,11/saca), sem dado novo
  - NAG Físico BR (farelo MT/IMEA, RS, Rondonópolis; prêmios export PGUA farelo/óleo) — ainda 2026-07-17, sem atualização
  - CFTC COT Managed Money — ainda referência 2026-07-14, sem atualização (próximo dado esperado ~21/07, publicação ~24/07)
  - USDA Crop Progress — ainda 2026-07-12 (65% bom-ou-melhor), sem atualização; próximo relatório "as of" hoje (19/07), publicação normal amanhã (20/07)
  - USDA WASDE — ainda 2026-07-10 (só farelo Argentina/Brasil/China parcial), sem publicação nova
  - NOPA — 2026-07-19, `monthly_status` continua inacessível (paywall), fila `release-nopa-2026-07-19`
  - ABIOVE projeções mensais — balanços ago-dez/2026 (farelo/óleo/soja), sem alteração
  - NOAA CPC ENSO — 2026-07-19 (El Niño Advisory, sem mudança)
  - MPOB — 2026-07-19 (parser sem números extraídos, 3.439 caracteres, 10º dia consecutivo com o mesmo conteúdo, contando de 10/07 a 19/07)
  - BCBA — 2026-07-19 (acessível, sem links de relatório detectados, mesmo padrão)
  - Notícias Agrícolas/Canal Rural RSS — 2026-07-19 (160 itens lidos, 7 mantidos; manchete "Consultor aponta avanço da área de soja, algodão e feijão, enquanto trigo, arroz e milho de verão devem perder espaço", Canal Rural)
  - Forecasts estatísticos internos — 2026-07-19 (as seis bandas seguem simultaneamente em viés altista, quarta leitura seguida nessa condição, spot ref idêntico ao de ontem)
  - system/tributario_watch.toml — MP-1358-2026 (vigência formal encerrada há 8 dias, status ainda "tramitação"), PIS/COFINS-BIODIESEL-ISENCAO (vence em 12 dias), MP-1363-2026, STJ-RESP-2165276, B16-CNPE-2026, EPA-RFS-2026-2027, 45Z-CLEAN-FUEL, DANANTARA-INDONESIA, INDONESIA-B50, INDONESIA-LEVY-PMK9 — todos `atualizado_em` 2026-06-05 (44 dias sem atualização do monitor)
  - Cruza com [[2026-07-18_leitura-complexo]], [[2026-07-17_leitura-complexo]], [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (checkpoint D+7, tratado abaixo — agora 31 dias vencido), [[2026-05-26_subvencao-fossil-aperta-biodiesel]]
status: ativa
vies: [bull-soja, bear-farelo, bull-oleo_soja]
---

> **Nota de proveniência:** hoje é domingo, 19/07/2026 — a CBOT reabre a sessão
> eletrônica do complexo agrícola só à noite, horário de Chicago (já madrugada
> de segunda-feira em Brasília), então o dump de hoje ainda não traz nenhum
> fechamento novo de soja/farelo/óleo. O que muda de fato hoje, pela primeira
> vez em quatro gerações de dado sobre a mesma sessão de sexta-feira (17/07):
> **nada mudou nos indicadores de complexo** (ratio Far/Soj, crush margin, oil
> share, oil-meal spread, margem de biodiesel, paridade BR e a curva forward
> completa das três pernas ficaram byte-a-byte idênticos à leitura de ontem).
> A única oscilação renovada foi o **volume do óleo de 17/07**, que voltou a
> 40.029 contratos (o valor original da primeira geração, não os 32.629 que a
> leitura de ontem tratou como "revisão"). E há uma vela genuinamente nova,
> mas de outro mercado: o **heating oil eletrônico (HO=F) de domingo** já abriu
> a sessão (4,00 USD/galão, -1,59% frente ao fechamento de sexta) com volume
> muito baixo (859 contratos, sessão em formação). A seção Honestidade
> detalha o que essa estabilização (e essa reversão pontual) significam para a
> confiança nos números.

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
bushel↔short ton): quando cai abaixo de 80%, o farelo está historicamente
"abundante" frente à soja, e o spread tende a comprimir (é um spread de
mean-reversion — comprimido demais tende a esticar de volta, esticado demais
tende a comprimir; hoje o sinal segue apontando para o lado "comprimido").

**Hoje é domingo, e ainda não há pregão novo do complexo agrícola para
analisar.** O que o dump de hoje traz de genuinamente relevante não é um novo
sinal de preço — é o **fim de uma sequência de revisões**. Pela primeira vez
desde que esta série de leituras começou a documentar o fenômeno (quatro
gerações de dado sobre a mesma sessão de sexta-feira: a original de 17/07, a
revisão de 18/07, e agora a terceira geração de 19/07), os indicadores de
complexo — ratio Far/Soj (79,75%), crush margin (3,2285 USD/bu), oil share
(53,88%), oil-meal spread (1,1847 USD/bu), margem de biodiesel (0,8189
USD/gal) e a paridade teórica em reais (R$ 135,89/saca) — **não mudaram nem
um dígito** frente à leitura de ontem. O mesmo vale para a curva forward
completa das três pernas (soja, farelo, óleo), citada abaixo seção por seção.
A única peça que voltou a se mexer foi o **volume da sessão de óleo de
17/07**, que hoje aparece em 40.029 contratos — o valor da primeira geração
(17/07), não os 32.629 que a segunda geração (18/07) havia tratado como
"revisão". Isso é tratado com cautela na seção Honestidade: não dá para saber
se o valor de hoje é o definitivo ou se o campo simplesmente continua
instável. Separadamente, há uma vela genuinamente nova de um mercado
correlato: o **heating oil (HO=F, o diesel de aquecimento americano, insumo
de receita do biodiesel)** já abriu a sessão eletrônica de domingo em 4,00
USD/galão — um gap de -1,59% frente ao fechamento de sexta (4,0646) — e
opera agora em 4,0483 (-0,40% frente à sexta), com volume muito baixo (859
contratos, uma fração dos ~32.681 contratos negociados na sexta), sinal de
que a sessão ainda está se formando e não deve ser tratada como direcional.
Trata `ratio-zona-2026-07-17`, `alerta-quebra_resistencia-soja_cbot-2026-07-17`
e `alerta-movimento_forte-oleo_cbot-2026-07-17` — os três gatilhos táticos da
sexta-feira seguem sem teste por uma sessão nova e independente. Fora do
mercado, duas peças novas de contexto: uma manchete do Canal Rural
(19/07/2026) sobre expansão da área de soja brasileira para a safra 2026/27
(tratada na seção Soja) e o décimo dia consecutivo de MPOB travado no mesmo
conteúdo (tratado na Honestidade). **Leitura de uma linha:** com o mercado
ainda fechado, o pivô de hoje é a estabilização dos números pela primeira vez
nesta série — o que aumenta, não diminui, a confiança de que os três vieses
(bull tático em soja, bear estrutural com tático confirmado em farelo, bull
forte em óleo) refletem a sessão real de sexta-feira, e não um artefato de
pipeline; convicção moderada-alta em soja e óleo, moderada-alta em farelo,
com a reabertura de amanhã (segunda-feira, 20/07) — trazendo também o Crop
Progress semanal — como o próximo teste genuíno.

---

## Soja

**Viés: bull tático (convicção moderada-alta, mantido pela terceira leitura
seguida) — fechou em 1.204,50 cts/bu na sessão de sexta-feira (17/07/2026,
terceira geração de dado, sem qualquer revisão frente a ontem), 2,08% acima
da resistência 1.180,00. Trata `alerta-quebra_resistencia-soja_cbot-2026-07-17`.
Sem pregão novo hoje (domingo) para testar a tese em tempo real.**

### O que sustenta a tese

**A vela de sexta-feira, agora na sua terceira geração, permanece
exatamente igual à segunda.** Fechamento 1.204,50 cts/bu (CBOT, sessão de
17/07/2026), abertura 1.195,00 (idêntica ao fechamento de 16/07, sem gap),
mínima 1.186,75, máxima 1.205,25, volume 27.197 contratos — todos os cinco
valores idênticos aos citados na leitura de ontem. O fechamento fica a
apenas 0,75 ponto da máxima do dia, sobre um range de 18,50 pontos — 96% do
movimento do dia terminou perto do topo, e essa leitura de força não sofreu
nenhum desgaste com mais uma rodada de reprocessamento. A distância de
segurança até o suporte estrutural de 1.180,00 permanece em 2,08% (mesma da
leitura de ontem) — pela primeira vez nesta série, um número tático não
mudou de uma geração para a outra.

**A sequência dos últimos cinco fechamentos permanece a mesma de ontem —
1.196,75 (13/07) → 1.192,75 (14/07) → 1.202,25 (15/07) → 1.195,00 (16/07) →
1.204,50 (17/07)** — uma consolidação lateral com viés de alta, com o
fechamento de sexta-feira sendo o mais alto da janela de cinco dias. O
rompimento de alta de 06-07/07 (que levou o preço de ~1.180,00 para a faixa
de 1.190-1.205) segue integralmente válido, agora com três leituras
consecutivas confirmando os mesmos números.

**A curva forward, sem pregão novo, permanece exatamente a mesma descrita
ontem**: Agosto/26 (Q26, spot) 1.204,50 → Setembro/26 (U26) 1.193,50
(desconto de −11,00, −0,91%) → Novembro/26 (X26) 1.203,00 (recupera +9,50
sobre setembro, ficando praticamente colado ao spot) → Janeiro/27 (F27)
1.216,75 (+1,14% sobre novembro) → Março/27 (H27) 1.220,00 (+0,27% sobre
janeiro). O formato de "sorriso" (desconto no meio, prêmio na ponta longa)
segue intacto — o mercado não está precificando um susto estrutural de
oferta na curva.

**A paridade teórica em reais permanece em R$ 135,89/saca 60kg**
(indicadores, sobre CBOT 1.204,50 cts × PTAX 5,1176 USD/BRL de 17/07 — sem
PTAX novo hoje, fim de semana). Comparando com o físico de Paranaguá de
17/07 (R$ 141,02/saca, CEPEA/ESALQ via NAG, também sem dado novo hoje): um
prêmio de R$ 5,13/saca (+3,78%) do físico sobre a paridade teórica —
idêntico ao calculado ontem. A tendência de compressão do prêmio observada
nas três leituras anteriores (4,68% em 16/07 → 3,81% em 17/07-primeira
geração → 3,78% em 17/07-segunda e agora terceira geração) fica congelada
sem dado físico novo para testar se a compressão continua.

**A notícia de hoje sobre a área de soja para a safra 2026/27 é o dado mais
relevante deste domingo, e merece leitura cuidadosa sobre horizonte.** O
Canal Rural publicou em 19/07/2026: "Consultor aponta avanço da área de soja,
algodão e feijão, enquanto trigo, arroz e milho de verão devem perder
espaço" (canalrural.com.br). O headline, sem números de área capturados pelo
dump, aponta um consultor de mercado projetando que a área plantada de soja
no Brasil deve crescer na safra 2026/27 (que começa a ser plantada em
outubro/26) às custas de área de trigo, arroz e milho de verão — ou seja, um
sinal de **expansão de oferta futura**, não de preço presente. O mecanismo
é o inverso do que sustenta o bull tático de hoje: mais área plantada em
outubro/26 é, historicamente, um driver bearish de médio prazo (mais uma
safra grande no radar, pressionando os contratos de vencimento 2027), mas
não tem nenhuma relação causal direta com o rompimento de resistência de
sexta-feira, que foi motivado por vendas de exportação americanas (ver
leituras anteriores). É importante não confundir os dois horizontes: a tese
tática de hoje (bull, suporte em 1.180,00, horizonte de dias/semanas) e essa
notícia (um sinal estrutural de oferta 2026/27, horizonte de meses) apontam
em direções diferentes — o que é normal e não invalida nenhuma das duas
leituras, mas deve ser registrado como o primeiro fio de um contraponto
estrutural de médio prazo à tese tática atual. Sem número de área
quantificado no headline, esta notícia entra como contexto, não como driver
calibrado (ver Honestidade).

**O COT (CFTC) permanece com o mesmo dado de referência, 14/07/2026, sem
atualização.** Managed money net long em soja em +75.191 contratos (7,48% do
open interest de 1.004.746), ante +69.579 contratos (7,13% do OI de 975.954)
em 07/07/2026 — um crescimento acompanhado de OI total subindo +2,95% na
semana, assinatura de dinheiro novo entrando comprado, não apenas de
posições vendidas fechando. O próximo COT (dado esperado ~21/07, publicação
~24/07) é que vai mostrar se essa compra continuou durante a semana do
rompimento de 17/07 — agora a apenas dois dias de distância do corte de
dados.

**O USDA Crop Progress permanece parado em 12/07/2026** (65% da lavoura
americana em condição boa-ou-excelente, 12% excelente + 53% boa, 6% em
condição ruim). O próximo relatório semanal normal tem "as of" hoje
(19/07/2026) e deve ser publicado amanhã, segunda-feira 20/07 — a
proximidade máxima desta série de leituras.

**Os forecasts estatísticos internos (19/07/2026, calculados sobre o mesmo
spot de 1.204,50)** seguem altistas: central 7d = 1.233,54 cts/bu (bandas
1.181,94-1.285,15); central 30d = 1.339,97 cts/bu (bandas 1.233,13-1.446,80).
É a quarta sessão seguida em que as seis bandas do sistema (soja, farelo e
óleo, 7d e 30d) fecham simultaneamente em viés altista.

### O que invalida / risco para a soja

- **Um fechamento de volta abaixo de 1.195,00 (fechamento de 16/07) ou de
  1.186,75 (mínima de sexta-feira) na reabertura de amanhã** questionaria a
  força da recuperação em V e reabriria o cenário de teste do suporte
  1.180,00.
- **O prêmio físico de Paranaguá sobre a paridade continuar comprimindo**
  quando houver dado físico novo — já são três leituras seguidas de
  compressão (4,68% → 3,81% → 3,78%), congeladas hoje por falta de dado.
- **O COT de 21/07 (publicação ~24/07) mostrar que os fundos venderam
  durante o rompimento** — o dado disponível (14/07) ainda é de antes do
  movimento.
- **O USDA Crop Progress de amanhã (20/07) mostrar melhora continuada** da
  lavoura americana — reduziria o argumento de oferta apertada que sustenta
  parte do apetite comprador.
- **A notícia de expansão de área para 2026/27 se confirmar em números
  concretos** (relatório formal de intenção de plantio, Conab ou USDA) — um
  contraponto estrutural de médio prazo que, se quantificado, merece
  incorporação numa leitura futura, sem confundir com a tese tática de hoje.

### Leitura operacional — soja

Sem pregão hoje, a leitura operacional de domingo é essencialmente uma
checagem de solidez: pela primeira vez nesta série, uma terceira rodada de
reprocessamento não alterou nenhum número da tese, o que dá o maior grau de
confiança já registrado nesta janela de que o rompimento de 2,08% acima de
1.180,00 é real, e não um artefato de revisão de dados. Isso favorece manter
posição comprada alinhada ao rompimento de 06-07/07, com 1.180,00 seguindo
como referência de stop lógica. Para quem está vendido contra esse
rompimento, a tese de hoje não oferece nenhum alívio adicional. O evento
mais importante da próxima sessão é duplo: a reabertura de amanhã
(20/07), que vai mostrar se o mercado global reagiu a algo no fim de
semana (inclusive à notícia de expansão de área), e o Crop Progress do
mesmo dia, que atualiza pela primeira vez em 8 dias a condição da lavoura
americana.

---

## Farelo

**Viés: bear (estrutural mantido, tático confirmado por três gerações de
dado da mesma sessão). O ratio Far/Soj de 17/07/2026 permanece em 79,75%
(indicadores: farelo 320,20 ÷ soja 1.204,50, base normalizada), idêntico à
leitura de ontem — nenhuma revisão nova. Trata `ratio-zona-2026-07-17` e
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` (revisão
programada, hoje 31 dias vencida — ver abaixo).**

### O que sustenta a tese

**O ratio Far/Soj, pela primeira vez em três gerações de dado sobre a
sessão de 17/07, não mudou.** Sequência completa, agora estável: 79,52%
(13/07) → 79,83% (14/07) → 79,58% (15/07) → 81,06% (16/07) → **79,75%
(17/07, idêntico à leitura de ontem)**. A distância abaixo do limiar de 80%
permanece em 0,25 ponto percentual. A postura recomendada nas duas últimas
leituras — aguardar uma sessão de pregão genuinamente nova antes de tratar
o cruzamento como robusto — segue tecnicamente válida (ainda não houve
sessão nova), mas a estabilização do número em si, depois de duas rodadas
de revisão que já haviam movido a mesma sessão em direções distintas,
reduz o risco de que o valor de 79,75% seja, ele mesmo, um artefato de
pipeline ainda em fluxo.

**Tratando `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`:**
a revisão programada da tese original (insight
[[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]) tinha data-alvo
18/06/2026 — hoje, 19/07/2026, ela está **31 dias vencida** (mais um dia
frente aos 30 de ontem). As três perguntas seguem com as mesmas respostas
de ontem, sem novo dado para atualizá-las: (1) o ratio fechou abaixo de
80%? **Sim**, com margem estável de 0,25 ponto, mas ainda sem uma segunda
sessão de pregão independente para confirmar (mercado fechado); (2) o
WASDE mudou o quadro? **Não**, segue parado em 10/07/2026, sem cobertura de
soja em grão ou óleo; (3) o NOPA confirmou o esmagamento? **Não**, segue
inacessível (trata `release-nopa-2026-07-19`, ver abaixo). Recomenda-se,
mais uma vez, reabrir esta revisão formalmente assim que o NOPA ou um novo
WASDE de soja/óleo estiverem disponíveis, ou assim que a sessão de amanhã
(20/07) confirmar o ratio abaixo de 80% de forma independente.

**A crush margin permanece em 3,2285 USD/bushel, o maior valor da janela de
cinco dias, agora sem nenhuma revisão adicional.** Sequência completa:
3,0211 (13/07) → 3,0193 (14/07) → 3,0145 (15/07) → 3,1211 (16/07) → 3,2285
(17/07, estável). O mecanismo estrutural segue intacto: quanto maior a
crush margin, maior o incentivo da esmagadora a processar soja a pleno
vapor, e mais farelo (subproduto obrigatório do esmagamento) entra no
mercado.

**A trajetória projetada da ABIOVE (Associação Brasileira das Indústrias de
Óleos Vegetais, projeções mensais, sem alteração) segue sendo o pilar mais
sólido do argumento estrutural, porque não depende do preço do dia nem de
revisões de fechamento.** A exportação de farelo brasileiro projetada cai
de 1.400 mil toneladas em agosto/2026 para 700 mil toneladas em
dezembro/2026 (queda de 50% em 4 meses), enquanto a produção cai de forma
bem mais suave (2.285,06 → 1.659,04 mil toneladas no mesmo período, −27%) —
menos farelo saindo pelo porto, com produção caindo bem menos que a
exportação, empurra o volume excedente para o mercado interno de ração,
pressionando o preço doméstico.

**As praças físicas de farelo no Brasil (NAG, último dado 17/07/2026, sem
atualização hoje) seguem no mesmo patamar descrito ontem.** Mato
Grosso/IMEA em R$ 1.602,80/ton, Rondonópolis/MT estável em R$ 1.600,00/ton,
Rio Grande do Sul em R$ 1.640,00/ton. O prêmio de exportação em Paranaguá
segue em +0,05 USD/short_ton (julho/26, NAG), agora **16 dias corridos sem
qualquer variação** desde 03/07/2026 — o intervalo cresce mais um dia,
reforçando a suspeita (já registrada em leituras anteriores) de que pode
ser um dado de fonte não atualizada, não um preço de mercado genuinamente
parado (ver Honestidade).

**O Índice de Sobra de Farelo (ISF) permanece em 80/100 (4 de 5 condições
estruturais)** (indicadores, recalculado hoje 19/07/2026, sem variação) —
inalterado desde pelo menos 01/07/2026, agora confirmado por um segundo
fim de semana seguido sem pregão, reforçando que é um índice calculado
sobre condições estruturais (ABIOVE, crush, oferta), não sobre o
fechamento do dia.

**Tratando `release-nopa-2026-07-19`:** o NOPA (National Oilseed Processors
Association, dado mensal de esmagamento americano) segue com
`monthly_status` em 0,0 bool — a mesma barreira de assinatura paga
documentada desde meados de junho, agora mais de um mês sem alternativa de
dado primário sobre o esmagamento americano. Sem nenhuma informação nova
para interpretar hoje.

**O oil-meal spread (óleo menos farelo, por bushel) permanece em 1,1847
USD/bu**, ante 0,8635 (16/07) — a mesma alta de +37,2% no dia calculada
ontem, sem nenhuma revisão adicional. Mede, de outro ângulo, a mesma
divergência farelo-fraco/óleo-forte que caracteriza a sessão de sexta.

**O COT de 14/07/2026, sem atualização, mantém o mesmo contraponto
relevante à tese bear já descrito nas últimas duas leituras.** Managed
money net long em farelo em +46.576 contratos (7,77% do open interest de
599.353), ante +18.722 contratos (3,14% do OI de 595.447) em 07/07/2026 —
mais que dobrou em uma semana. Como fração do OI, ficou próximo do de soja
(7,48%) e bem abaixo do de óleo (16,92%). Continua sendo o dado mais
direto disponível hoje contra uma posição vendida em farelo outright, sem
mudança frente às leituras anteriores.

**O forecast estatístico do farelo (19/07/2026)** segue com viés altista,
praticamente estável: central 7d = 327,18 USD/sht (bandas 314,21-340,16);
central 30d = 352,56 USD/sht (bandas 325,70-379,43). O modelo estatístico
(que reage a momentum de preço recente, não a fundamentos) segue na
direção oposta à tese fundamentalista ABIOVE + ratio.

### O que invalida / risco para o farelo

- **A reabertura de amanhã trazer o ratio de volta acima de 80%** — a
  margem atual (0,25 ponto) ainda é pequena o suficiente para uma sessão de
  fato nova reverter.
- **A tese estrutural ABIOVE não se confirmar no físico ao longo do
  2S/26** — sem atualização de praças físicas desde 17/07, não há novo
  dado para testar isso hoje.
- **O COT de 21/07 (publicação ~24/07) mostrar os fundos continuando a
  aumentar o net long em farelo** — reforçaria o risco de squeeze numa
  posição vendida direcional.
- **NOPA seguir inacessível indefinidamente**, sem confirmação do
  esmagamento americano para os checkpoints D+90 (09/09/2026) e D+180
  (08/12/2026).
- **O prêmio de exportação Paranaguá "congelado" há 16 dias ser, na
  verdade, um dado sem atualização de fonte** (ver Honestidade).

### Leitura operacional — farelo

A tese estrutural (ABIOVE, ISF 80/100, crush margin em novo topo pela
quarta sessão consecutiva de dado) segue sendo o pilar mais forte da
leitura, e o gatilho tático (ratio < 80%) ganhou, hoje, o primeiro sinal de
estabilidade genuína desde que a série de revisões começou — três gerações
seguidas do mesmo número (79,75%). Ainda assim, sem uma sessão de pregão
nova para confirmar de forma independente, e com o COT mostrando fundos
ampliando net long em farelo na mesma semana do cruzamento, a postura
recomendada segue sendo aguardar a confirmação de amanhã antes de tratar o
cruzamento como definitivamente robusto, dimensionando a posição
principalmente no pilar estrutural. Para quem prefere o veículo mais
defensável — o spread farelo/soja ou o crush completo, em vez de
direcional puro —, o argumento permanece o mais forte da leitura: a
divergência relativa entre as pernas (medida pelo oil-meal spread, estável
em +37,2% frente a 16/07) não depende de o ratio confirmar de forma limpa
nos próximos pregões, e não fica exposta ao risco de squeeze que o
posicionamento crescente dos fundos em farelo outright sugere.

---

## Óleo

**Viés: bull forte (mantido — a perna mais limpa do complexo, agora com
três leituras seguidas confirmando os mesmos números de preço). Fechou em
74,81 cts/lb na sessão de 17/07/2026, subindo +3,29% no dia (de 72,43 para
74,81, trata `alerta-movimento_forte-oleo_cbot-2026-07-17`). O oil share
permanece em 53,88% e o Índice de Suporte do Óleo (ISO) segue em 100/100.**

### O que sustenta a tese

**A vela de sexta-feira permanece idêntica pela segunda vez consecutiva.**
Fechamento 74,81 cts/lb (CBOT, sessão de 17/07/2026), abertura 72,62
(praticamente na mínima do dia, 72,43) e máxima 75,44 — o preço subiu de
forma consistente ao longo da sessão, com o fechamento retendo 79% do
movimento até a máxima. **O volume, porém, voltou a se mexer**: hoje
aparece em 40.029 contratos, o mesmo valor da primeira geração (17/07,
gerada no próprio dia da sessão), não os 32.629 que a leitura de ontem
tratou como uma revisão legítima. É a terceira leitura seguida em que este
campo específico oscila entre gerações do dump, sem explicação visível na
fonte — tratado com cautela na Honestidade, e **não** usado aqui como
argumento de convicção adicional para a tese (nem a favor, nem contra).

**A curva forward, sem pregão novo, mantém exatamente a mesma
backwardation descrita nas duas últimas leituras**: Agosto/26 (Q26, spot)
74,81 → Setembro/26 (U26) 73,93 (−0,88, −1,18%) → Outubro/26 (V26) 73,02
(−0,91, −1,23%) → Dezembro/26 (Z26) 72,43 (−0,59, −0,81%) → Janeiro/27
(F27) 72,07 (−0,36, −0,50%) — uma queda total de −2,74 cts/lb (−3,66%) de
agosto a janeiro/27. A assinatura de rali concentrado no vencimento mais
próximo (em vez de re-precificação estrutural de toda a curva) segue
intacta.

**A margem de biodiesel americano permanece em 0,8189 USD/galão, sem
nenhuma revisão adicional.** Receita 7,2296 (heating oil 4,0646 + 1,5×RIN
2,11) menos custo 6,4107 (óleo 5,6107 + industrial 0,80). Sequência
completa, agora estável na ponta: 0,7271 (13/07) → 0,9493 (14/07) → 0,8443
(15/07) → 0,9635 (16/07) → 0,8189 (17/07, estável) — a terceira menor
margem da janela de cinco dias, não mais o piso, como as duas últimas
leituras já haviam corrigido. A tensão de mecanismo permanece válida: a
mesma alta do óleo que é bullish para o papel CBOT é, ao mesmo tempo,
bearish para a margem do biodiesel (o óleo é o principal insumo de custo
do processo).

**Um dado genuinamente novo, embora de baixa confiabilidade por ora: o
heating oil eletrônico de domingo (19/07/2026) abriu com um gap para
baixo.** Abertura 4,00 USD/galão (HO=F, -1,59% frente ao fechamento de
sexta, 4,0646), mínima também em 4,00, máxima 4,0626, cotação corrente
4,0483 (-0,40% frente à sexta), volume de apenas 859 contratos — uma
fração dos 32.681 negociados na sexta-feira. O heating oil é o principal
componente de receita do biodiesel americano (junto com o RIN D4) no
cálculo da margem usada nesta leitura; um gap de abertura para baixo, se
confirmado ao longo da semana, tende a comprimir ainda mais a margem de
biodiesel (que já é a terceira menor da janela). Mas com volume tão baixo
e a sessão ainda em formação (é comum a Globex de energia abrir com gaps
que se fecham nas primeiras horas), este dado **não** deve ser tratado como
um sinal direcional confiável — é o primeiro pingo de informação da
próxima semana, não uma confirmação.

**O Índice de Suporte do Óleo (ISO) permanece em 100/100 (5 de 5
condições)** (indicadores, recalculado hoje 19/07/2026, sem variação) —
inalterado desde pelo menos 01/07/2026, confirmado por um segundo fim de
semana seguido sem pregão.

**O oil share permanece em 53,88%** (indicadores, 17/07/2026, sem revisão
adicional), o mesmo novo recorde da janela citado ontem, confirmando que o
óleo continua sendo o motor de valor do crush.

**O COT de 14/07/2026, sem atualização, mantém o óleo como a perna mais
"concorrida" das três em termos de posicionamento — sem mudança frente às
leituras anteriores.** Managed money net long em +107.945 contratos
(16,92% do open interest de 638.102), ante +84.919 contratos (13,22% do OI
de 642.514) em 07/07/2026 — um aumento de +23.026 contratos (+27,1%) na
semana, o maior em termos absolutos das três pernas. Com o net long em
~17% do OI (o mais alto das três pernas, sem histórico de percentil para
calibrar — ver Honestidade), a posição comprada no óleo segue sendo a mais
crowded do complexo.

**O forecast estatístico do óleo (19/07/2026)** mantém o viés altista,
quase idêntico às leituras anteriores: central 7d = 75,82 cts/lb (bandas
70,97-80,66); central 30d = 80,37 cts/lb (bandas 70,34-90,40). É a quarta
leitura seguida em que as seis bandas de forecast do sistema fecham
simultaneamente em viés altista.

### O que invalida / risco para o óleo

- **Um fechamento abaixo de 73,02 (o vencimento de outubro na curva de
  hoje) na reabertura de amanhã** reabriria o cenário de correção.
- **O gap de abertura do heating oil de domingo se confirmar e se
  aprofundar ao longo da semana** — comprimiria ainda mais a margem de
  biodiesel, já a terceira menor da janela, e reduziria o incentivo
  econômico a produzir biodiesel a partir do óleo de soja.
- **O posicionamento dos fundos (net long em 16,92% do OI, o mais
  concorrido das três pernas) sofrer uma reversão** quando o próximo COT
  chegar (~24/07).
- **MPOB seguir inacessível** — impossível avaliar o efeito do El Niño ou
  das restrições/levy indonésias (PMK 9/2026, Danantara — ver Lente
  fiscal) sobre o prêmio de substituição via palma. Hoje é o décimo dia
  consecutivo com o mesmo conteúdo sem números extraídos.

### Leitura operacional — óleo

O óleo segue sendo a tese mais forte e mais bem sustentada do complexo. A
estabilização dos números de preço (terceira geração idêntica) reforça a
confiança na vela de sexta-feira como um movimento real, mas o gap de
abertura do heating oil eletrônico de domingo — ainda que de baixo volume
e baixa confiabilidade — é o primeiro sinal, por menor que seja, de que a
margem de biodiesel pode voltar a comprimir na semana que vem. Para quem
opera exposição relativa dentro do crush, o oil-meal spread (estável em
+37,2%) segue sendo o veículo mais direto para capturar a divergência entre
as duas pernas do complexo. Para quem opera direcional puro em óleo, a
ausência de pregão hoje é uma pausa natural para reavaliar o dimensionamento
antes da reabertura de amanhã, que trará tanto o teste real da vela de
sexta quanto a primeira confirmação (ou não) do gap do heating oil.

---

## Spreads e crush — leitura de complexo

### Crush margin: 3,2285 USD/bu — estável no maior valor da janela, sem nova revisão

A crush segue no maior valor da janela de cinco dias, agora sem nenhuma
revisão adicional frente à leitura de ontem. Sequência completa: 3,0211
(13/07) → 3,0193 (14/07) → 3,0145 (15/07) → 3,1211 (16/07) → 3,2285 (17/07,
estável). O incentivo de esmagamento a pleno vapor segue se fortalecendo de
forma consistente, alimentando o mecanismo estrutural ABIOVE independentemente
de qual perna do complexo está subindo ou caindo no dia.

### Ratio Far/Soj: 79,75% — primeira estabilização da série, ainda na zona comprimida

O achado tático central desta leitura de domingo: pela primeira vez em três
gerações de dado sobre a mesma sessão, o ratio não se moveu (79,75% ontem,
79,75% hoje). Sequência completa: 79,52% (13/07) → 79,83% (14/07) → 79,58%
(15/07) → 81,06% (16/07) → **79,75% (17/07, estável)**. Trata
`ratio-zona-2026-07-17` e a revisão programada
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` (agora
31 dias vencida, ver seção Farelo). Ainda assim, sem uma sessão de pregão
nova e independente (mercado fechado no fim de semana), a recomendação de
aguardar confirmação de uma sessão genuinamente nova antes de tratar o
cruzamento como robusto permanece — a diferença é que a base de partida,
agora estável por duas gerações seguidas, é a mais confiável desta série
até aqui.

### Oil share: 53,88% — estável no novo topo da janela

Sem mudança frente a ontem — o óleo segue capturando a maior fatia do valor
do crush em toda a janela visível, com a estabilidade do número (em vez de
mais uma revisão) reforçando a confiança no recorde.

### Oil-meal spread: 1,1847 USD/bu — estável na maior alta de um dia da série

Sem mudança frente a ontem (+37,2% no dia, de 0,8635 em 16/07 para 1,1847
em 17/07). Mede a mesma divergência farelo-fraco/óleo-forte, agora
confirmada por uma segunda geração idêntica de dado.

### Margem de biodiesel: 0,8189 USD/gal — estável, mas heating oil de domingo abre com gap para baixo

A margem de sexta-feira, revisada na leitura de ontem, permanece em 0,8189
USD/gal sem nova mudança. O dado novo do dia não é sobre a margem em si
(que segue calculada sobre 17/07), mas sobre o insumo de receita: o heating
oil eletrônico de domingo abriu em 4,00 (-1,59% frente à sexta), um sinal
preliminar (baixo volume) de possível compressão adicional na margem
quando a sessão de amanhã atualizar o indicador com um fechamento
genuinamente novo.

### COT: sem atualização — óleo segue disparado o mais concorrido

O dado de 14/07/2026 segue sem atualização, agora a apenas dois dias do
próximo corte (~21/07, publicação ~24/07). Como fração do open interest, o
óleo é disparado o mais concorrido (16,92% vs 7,77% do farelo e 7,48% da
soja) — o posicionamento confirma o bull-óleo desta leitura, mas também é
o maior fator de risco de reversão abrupta.

### ISF em 80/100, ISO em 100/100 — recalculados hoje, sem variação pelo segundo fim de semana seguido

O Índice de Sobra de Farelo (ISF, 4/5 condições) e o Índice de Suporte do
Óleo (ISO, 5/5 condições) foram recalculados hoje (19/07/2026, domingo, sem
pregão) e permanecem inalterados — a segunda confirmação seguida, num fim
de semana sem pregão, de que são índices calculados sobre condições
estruturais (ABIOVE, crush, oferta), não sobre o fechamento pontual de uma
sessão.

### O que os índices dizem juntos em 19/07/2026

ISF 80/100 + ISO 100/100 (ambos estáveis por dois dias seguidos sem
pregão) + ratio Far/Soj estável abaixo de 80% pela primeira vez nesta série
+ oil share estável no topo da janela (53,88%) + crush margin estável no
topo pela quarta sessão de dado (3,2285) + oil-meal spread estável na maior
alta de um dia da série (+37,2%) + margem de biodiesel estável, mas com o
primeiro sinal preliminar (heating oil de domingo) de possível compressão
adicional + COT ainda mostrando fundos comprando as três pernas, com óleo
disparado o mais concorrido — formam o quadro mais estável e coerente
desta série de leituras: complexo esmagando a pleno vapor, com o mercado
precificando farelo e óleo de forma cada vez mais divergente, e pela
primeira vez sem uma nova rodada de revisão de dados para complicar a
leitura.

---

## Lente fiscal e regulatória BR

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L) — a
vigência formal (`vigencia_ate` 11/07/2026) venceu há 8 dias, e o monitor
tributário segue sem qualquer atualização de status** (system/tributario_watch.toml,
evento MP-1358-2026, `atualizado_em` 2026-06-05, status ainda "tramitacao").
Enquanto o combustível fóssil segue subsidiado, a competitividade relativa
do biodiesel dentro do mix B15 mandatório fica pressionada — um vetor
regulatório independente do proxy americano de margem de biodiesel, que
segue vigente sem qualquer sinal de resolução.

**Isenção PIS/Cofins biodiesel — vencimento em 31/07/2026, agora a 12
dias.** Sem sinalização pública de renovação até hoje (evento
PISCOFINS-BIODIESEL-ISENCAO, `atualizado_em` 2026-06-05, sem mudança). Com
a margem de biodiesel americana estável em 0,8189 (terceira menor da
janela, não mais o piso) e um sinal preliminar de possível compressão
adicional via heating oil de domingo, o cenário de "duplo headwind" (custo
tributário potencial + margem apertada) segue relevante e sem novidade
concreta nesta leitura — o vetor tributário BR, por si só, é o mais urgente
a monitorar nos próximos 12 dias.

**B16 — sem data, travado em B15.** Sem mudança de status (evento
B16-CNPE-2026, `atualizado_em` 2026-06-05, status "adiado"). Testes
técnicos do FNDCT com resultado esperado ~nov/2026 — realista só fim de
2026/início de 2027.

**MP 1.363/2026 (subsídio ao diesel fóssil, R$ 1,12/L) — em vigor até
31/12/2026.** Sem alteração. Bearish estrutural persistente para a demanda
incremental de óleo de soja no mercado doméstico brasileiro.

**STJ REsp 2.165.276/2026 — crédito PIS/Cofins para esmagadoras.** Sem
alteração. Bullish para soja/óleo (alívio de custo de entrada para
biodiesel) e, por extensão, incentivo a mais esmagamento — coerente com a
crush margin no topo da janela.

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
B50 pleno só 2027-28); INDONESIA-LEVY-PMK9 (imposto de exportação de CPO
até 12,5% desde 01/03, encarecendo palma e favorecendo substituição por
óleo de soja). Todos esses vetores seguem, em conjunto, num sentido
estruturalmente bullish para o óleo de soja via substituição de palma —
mas seguem inverificáveis pelo lado dos dados de mercado (MPOB inacessível
há 10 dias consecutivos, ver Honestidade).

**O monitor tributário como um todo está há 44 dias sem qualquer
atualização** (`atualizado_em` 2026-06-05 em todos os dez eventos
rastreados) — o intervalo segue crescendo em um momento em que dois
vetores (MP 1.358 e a isenção PIS/Cofins) têm datas de vencimento formal já
vencida ou a apenas 12 dias. Vale sinalizar este ponto, mais uma vez, como
prioridade de manutenção do sistema, independentemente da leitura de
preço.

---

## Riscos e eventos próximos

**A reabertura de amanhã (segunda-feira, 20/07) é o próximo teste real de
todas as teses desta leitura.** Sem pregão neste fim de semana, tudo o que
esta leitura pôde fazer foi confirmar a solidez dos números de
sexta-feira através de uma terceira rodada de reprocessamento (a primeira
sem qualquer mudança) — o teste genuíno (nova oferta e demanda, reação ao
gap do heating oil, reação à notícia de área de soja 2026/27) só vem com a
próxima sessão.

**O USDA Crop Progress de amanhã (20/07, dado "as of" hoje, 19/07) atualiza
pela primeira vez em 8 dias a condição da lavoura americana** (última
leitura 12/07: 65% bom-ou-melhor). É o evento fundamentalista mais
concreto e datado da próxima sessão.

**COT (CFTC) — dado de 14/07/2026 segue sendo o mais recente, a dois dias
do próximo corte.** O próximo dado (referência ~21/07, publicação normal
~24/07) é o que vai mostrar se os fundos continuaram comprando soja e
óleo, e se começaram a reduzir farelo, durante a semana em que o ratio
cruzou abaixo de 80%.

**Pela primeira vez nesta série de revisões dump-a-dump, uma terceira
geração de dado sobre a mesma sessão não mudou nada nos indicadores de
complexo — só o volume do óleo voltou a oscilar.** Isso é, em si, uma
informação: depois de quatro episódios de revisão material em cinco
leituras anteriores, a estabilização de hoje é o primeiro sinal de que os
números de 17/07 podem estar, finalmente, convergindo para um valor
definitivo. Ainda assim, recomenda-se manter a prática de tratar qualquer
número do dia da própria publicação como sujeito a revisão até uma sessão
genuinamente independente confirmar — a oscilação do volume do óleo (que
voltou ao valor original depois de uma "revisão" de ontem) mostra que nem
todos os campos estabilizaram.

**Desfecho da MP 1.358/2026 — vigência formal encerrada há 8 dias, sem
confirmação.** Monitorar deliberação da comissão mista e qualquer decreto
de prorrogação.

**Isenção PIS/Cofins biodiesel — vencimento 31/07/2026 (12 dias).** Sem
sinalização de renovação até agora.

**NOPA — segue inacessível** (fila `release-nopa-2026-07-19` tratada
aqui, sem dado interpretável), sem crush americano confirmado por fonte
primária.

**MPOB — sem números de palma extraídos há 10 dias consecutivos**,
mantendo cego o efeito do El Niño e dos vetores regulatórios indonésios
(Danantara, B50, levy PMK 9) sobre o prêmio de substituição do óleo de
soja.

**A notícia sobre expansão de área de soja BR para 2026/27 (Canal Rural,
19/07)** merece acompanhamento nas próximas semanas — se um relatório
formal de intenção de plantio (Conab, USDA) quantificar essa expansão, ela
passa a ser um driver estrutural relevante de médio prazo, em direção
contrária à tese tática atual.

**Checkpoints futuros da tese estrutural do farelo (ABIOVE)** — D+90 em
09/09/2026 e D+180 em 08/12/2026 (insight
[[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]) — a revisão
D+7, agora 31 dias vencida, aponta confirmação tática mais sólida (ratio <
80% estável por duas gerações seguidas) mas ainda sem confirmação de
fundamentos (WASDE, NOPA); os checkpoints estruturais seguem o critério de
mais alta confiança para julgar a tese ao longo do tempo.

---

## Honestidade

O que não foi possível validar neste briefing de 19/07/2026, onde a
confiança é baixa ou há lacunas materiais:

**1. Hoje é domingo, sem pregão novo do complexo agrícola — tudo o que
esta leitura pôde fazer foi reanalisar a sessão de sexta-feira (17/07)
através de uma terceira geração de dados.** Pela primeira vez, essa
terceira geração não mudou nenhum indicador de complexo frente à segunda —
um sinal positivo de convergência, mas ainda não substitui uma sessão de
mercado genuinamente nova. A confirmação real só vem com a reabertura de
amanhã (20/07).

**2. O volume da sessão de óleo de 17/07 voltou a oscilar: 40.029
contratos hoje, ante os 32.629 que a leitura de ontem tratou como
"revisão", que por sua vez vieram dos 40.029 da primeira geração.** Ou
seja, o campo fez um ciclo completo (40.029 → 32.629 → 40.029) sem que o
dump traga qualquer explicação. Isso não muda a leitura da vela em si
(abertura, mínima, máxima e fechamento do óleo permaneceram idênticos nas
três gerações), mas é evidência direta de que nem todo campo do dump
estabilizou — o volume, especificamente, não deve ser tratado como um
número confiável até uma fonte independente confirmar.

**3. O heating oil eletrônico de domingo (19/07) tem volume muito baixo
(859 contratos, ante ~32.681 na sexta) e a sessão ainda está em
formação.** O gap de abertura para baixo (-1,59% frente à sexta) é o
primeiro dado de mercado genuinamente novo desta leitura, mas com essa
liquidez não deve ser extrapolado como sinal direcional confiável para a
margem de biodiesel da semana que vem — é um pingo de informação, não uma
confirmação.

**4. O COT (CFTC) segue com dado de referência 14/07/2026, sem
atualização.** A semana do rompimento da soja e do salto do óleo ainda não
está refletida no posicionamento dos fundos — o próximo relatório (dado
esperado ~21/07, publicação ~24/07) é que vai testar se a compra de
dinheiro novo em soja e óleo continuou durante essa semana.

**5. Percentis históricos de COT não calculados** — os números de
14/07/2026 são lidos apenas em nível absoluto e como fração do open
interest corrente (soja 7,48%, farelo 7,77%, óleo 16,92%), sem série
histórica completa para calibrar se algum desses níveis está
objetivamente "esticado" no sentido histórico.

**6. O prêmio de exportação de farelo em Paranaguá (+0,05 USD/sht) e o de
óleo (+0,08 cts/lb) estão no mesmo valor exato desde pelo menos
03/07/2026** (NAG, agora 16 dias corridos sem variação de nenhum
centavo) — não é possível distinguir se isso reflete um mercado de
exportação genuinamente parado ou um valor que não está sendo atualizado
de fato na fonte.

**7. O prêmio físico de Paranaguá sobre a paridade teórica está congelado
em 3,78% desde a leitura de ontem**, sem dado físico novo para testar se a
sequência de compressão (4,68% → 3,81% → 3,78%) continua ou estabilizou
junto com o resto dos indicadores.

**8. A notícia sobre expansão de área de soja 2026/27 (Canal Rural,
19/07/2026) não traz nenhum número de área, safra ou fonte primária
(Conab/USDA) no headline capturado pelo dump — é a visão de "um
consultor" não identificado.** Foi registrada nesta leitura como contexto
estrutural de médio prazo a monitorar, explicitamente **não** como driver
calibrado da tese tática de hoje — tratar como tal seria inventar peso
quantitativo que a fonte não sustenta.

**9. O WASDE segue cobrindo apenas farelo (Argentina, Brasil, China
parcial), sem nenhum dado de soja em grão ou óleo de soja, em qualquer
geografia, e sem nenhum dado dos Estados Unidos** — sem atualização desde
10/07/2026. A pergunta central sobre "oferta grande de soja" segue sem
canal de resposta interno.

**10. NOPA (fila `release-nopa-2026-07-19`) segue com `monthly_status` em
0,0 bool** — mesma barreira de assinatura paga documentada desde meados de
junho, agora com mais de um mês sem alternativa de dado primário sobre o
esmagamento americano.

**11. Palma malaia (MPOB) segue sem números extraídos, agora por 10 dias
consecutivos com o mesmo conteúdo exato (3.439 caracteres, de 10/07 a
19/07/2026)** — a persistência do byte count idêntico já sugere,
possivelmente, uma página que não está mais sendo servida com conteúdo
atualizado (e não apenas um parser incompatível com a estrutura). Continua
impossível avaliar o efeito do El Niño ou dos vetores regulatórios
indonésios (Danantara, B50, levy PMK 9 — ver Lente fiscal) sobre o prêmio
de substituição do óleo de soja.

**12. Clima INMET (BR) não foi usado como driver desta leitura.** Julho é
entressafra da soja brasileira (colheita concluída, plantio só em
outubro) — sem relevância direta para a tese de preço neste momento do
calendário agrícola, embora o El Niño Advisory (NOAA CPC, inalterado
desde pelo menos 03/07/2026) permaneça relevante para a expectativa da
safra de plantio de outubro/26 (inclusive para a notícia de expansão de
área tratada acima) e para o clima do Sudeste Asiático (palma).

**13. BCBA Argentina — sem relatórios de esmagamento/exportação
acessíveis via scraper** (page_fetched=1,0 mas sem links de relatório,
19/07/2026, sem mudança).

**14. RIN D4 como parâmetro fixo (2,11 USD/RIN) segue sendo uma fonte
relevante de incerteza do modelo de biodiesel**, sem novo dado hoje — a
margem estável de 0,8189 foi calculada com esse valor fixo; se o RIN de
mercado estiver, na realidade, diferente de 2,11, tanto a margem quanto o
ISO podem estar mal calibrados, independentemente da estabilização
documentada nesta leitura.

*Nenhum número foi inventado ou estimado além do que consta no briefing de
19/07/2026 e nos insights anteriores referenciados. A contribuição central
desta leitura foi identificar que, pela primeira vez em quatro gerações de
dado sobre a mesma sessão de sexta-feira (17/07), os indicadores de
complexo pararam de mudar — com a exceção pontual do volume do óleo, que
completou um ciclo (40.029 → 32.629 → 40.029) sem explicação visível na
fonte, e com a chegada de uma vela genuinamente nova, mas de baixa
liquidez e baixa confiabilidade, no heating oil eletrônico de domingo.
Nenhum desses dois achados inverte qualquer um dos três vieses desta
leitura, mas reforçam, juntos, a recomendação de sempre tratar números de
sessões sem pregão como preliminares até uma sessão de mercado
genuinamente nova confirmar.*
