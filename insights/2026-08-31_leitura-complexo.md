---
data: 2026-08-31
titulo: "Segunda-feira real (não fim de semana) mas ainda sem um fechamento novo do CBOT no pipeline — a tese de sexta (soja rompida em 1.288,00, farelo em 342,50, óleo preso abaixo de 72,00) chega à véspera do gatilho Danantara (amanhã, 01/09) ainda sem o primeiro teste de mercado, enquanto os dados retroativos de 28/08 mostram um padrão de revisão que agora parece cíclico, não apenas ruidoso"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT (ZSX26 soja / ZMV26 farelo / ZLV26 óleo) — última sessão disponível no pipeline, 2026-08-28 (sexta-feira): soja abertura 1.270,00, máxima 1.290,00, mínima 1.269,25, fechamento 1.288,00 USD cts/bushel, volume 153.472 contratos; farelo abertura 333,10, máxima 345,70, mínima 331,40, fechamento 342,50 USD/short ton, volume 46.745 contratos; óleo abertura 69,12, máxima 71,08, mínima 68,93, fechamento 70,82 USD cts/lb, volume 57.670 contratos. Curva futura em 28/08: soja set/26 (U26) 1.276,25, jan/27 (F27) 1.302,75, mar/27 (H27) 1.306,50, mai/27 (K27) 1.310,50; farelo set/26 (U26) 338,20, dez/26 (Z26) 348,90, jan/27 (F27) 350,50, mar/27 (H27) 350,90; óleo set/26 (U26) 70,59, dez/26 (Z26) 71,06, jan/27 (F27) 70,99, mar/27 (H27) 70,92
  - CME CBOT — sessão de 2026-08-27, presente no dump só para farelo (fechamento 334,40 USD/sht) e para reconstrução de soja (1.268,00) e óleo (68,23) via `indicators`
  - CME NYMEX heating oil (HO=F) — DOIS carimbos novos nesta janela: 2026-08-28 fechamento 4,3567 USD/galão (volume 19.477) e 2026-08-30 (domingo) abertura 4,3000, máxima 4,3230, mínima 4,2861, fechamento 4,2962 USD/galão, volume 901 contratos — ver Honestidade sobre o que esse print de domingo revela (e não revela) sobre a segunda-feira
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, paridade BR, ISF, ISO) — última atualização com pregão real 2026-08-28; ISF e ISO carimbados também em 29/08, 30/08 e 31/08 repetindo os mesmos valores de 28/08 por falta de fechamento novo pra recalcular
  - BCB PTAX — série 2026-08-17 a 2026-08-28, USD/BRL fechou em 5,2005 (28/08, última cotação disponível; sem PTAX de fim de semana nem, ainda, de segunda-feira 31/08 neste dump)
  - CEPEA/ESALQ Soja Paranaguá via NAG — série 2026-08-20 a 2026-08-28, fechou em R$ 159,76/saca (28/08, var. +3,04%)
  - CEPEA/ESALQ Soja Paraná interior via NAG — série 2026-08-24 a 2026-08-28, fechou em R$ 151,32/saca (28/08, var. +1,41%)
  - NAG Físico BR — série 2026-08-24 a 2026-08-28: farelo MT/IMEA R$ 1.795,68/ton (28/08, +4,03%), Rondonópolis/MT R$ 1.870,00/ton (estável desde 26/08), RS média R$ 1.860,00/ton (estável); prêmios export PGUA farelo +0,12 USD/short ton e óleo +0,10 cts/lb, ambos congelados desde 24/08 (6 sessões seguidas)
  - CFTC COT Managed Money, Swap Dealers e Producer/Merchant — corte de 2026-08-25, ainda o mais recente disponível, agora 6 dias corridos de defasagem frente ao fechamento de 28/08 mais 3 dias corridos adicionais até hoje
  - USDA Crop Progress — corte de 2026-08-23 (12% excelente / 48% boa / 9% ruim), sem corte novo
  - USDA WASDE — segue ausente da janela deste briefing
  - NOPA — fila `release-nopa-2026-08-31` marca um release "novo", mas `monthly_status` segue em 0,0 bool (paywall) sem qualquer número novo — ver Honestidade
  - ABIOVE projeções mensais — balanços set-dez/2026, mesmos valores da leitura anterior
  - NOAA CPC ENSO — carimbo 2026-08-31 (El Niño Advisory, inalterado desde 27/08)
  - MPOB — carimbo 2026-08-31 (3.456 caracteres, parser sem números extraídos, mesma barreira desde pelo menos 27/08)
  - INMET — previsão para 2026-08-31 (hoje): calor extremo e céu limpo no núcleo produtor de Mato Grosso (41°C em Cuiabá/Sinop/Lucas do Rio Verde, 40°C em Sorriso, "poucas nuvens" — sinal de seca), contra chuva e trovoadas no Sul (Passo Fundo/RS 19°C/13°C, Cascavel/PR 33°C/14°C, Maringá/PR 37°C/19°C, todas com pancadas e trovoadas)
  - Notícias Agrícolas/Canal Rural RSS — 2026-08-31 registra "160 items lidos, 3 mantidos (soja/farelo/oleo)" mas SEM headline de nenhum dos 3 itens exposta no dump (ver Honestidade); o headline mais recente com texto visível é de 29/08, "Soja sobe no Brasil e em Chicago; mercado apresenta ritmo na semana", e de 30/08, "Falta pouco! Saiba como se inscrever para a Abertura Nacional do Plantio da Soja 2026/27" (institucional/calendário, não fato de preço)
  - Forecasts estatísticos internos (bandas 7d/30d, MA20+volatilidade+slope) — geração de 2026-08-31, alvos 07/09 (7d) e 30/09 (30d); viés "altista" em soja e farelo nos dois horizontes, óleo "lateral" no 7d e "altista" no 30d
  - system/tributario_watch.toml (lido como referência, não editado) — `atualizado_em` 2026-06-05 em todos os eventos, agora **87 dias sem revisão** — ver Lente fiscal e Honestidade
  - Fila de julgamento — carimbada 2026-08-31 no briefing, 8 itens; 7 idênticos aos de ontem (mesmos `id`, mesmo fato de 28/08) e 1 com `id` atualizado (`release-nopa-2026-08-31`, substituindo `release-nopa-2026-08-29`) mas sem conteúdo novo real
  - Cruza com [[2026-08-30_leitura-complexo]] (leitura de ontem, domingo, cujos números de 28/08 este briefing revisa outra vez) e com [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (tese original do ratio, revisada em 29/08 e 30/08)
status: ativa
vies: [bull-soja, bull-farelo, neutral-oleo_soja]
---

## Visão geral

Hoje é segunda-feira, 31/08/2026 — e isso muda a natureza do dia em relação às duas
leituras anteriores, mesmo que o resultado pareça idêntico à primeira vista. Sábado e
domingo não têm pregão porque a CBOT (Chicago Board of Trade, a bolsa onde se negociam os
contratos futuros de soja, farelo e óleo) simplesmente não opera nesses dias; por isso as
leituras de 29 e 30/08 recontextualizavam o MESMO fechamento de sexta-feira sem nenhuma
chance de ele ser testado. Hoje é diferente: a segunda-feira É um dia de pregão normal, o
mercado de Chicago abriu e fechou hoje — só que o briefing usado para esta leitura foi
compilado ANTES desse fechamento chegar ao pipeline de dados. Ou seja, o "nada mudou" de
hoje não é porque o mercado ficou parado (como no fim de semana), é porque ainda não
temos visibilidade sobre o que ele fez. Essa é uma diferença importante de tratar: a tese
de sexta-feira está prestes a receber seu primeiro teste real, só que o resultado desse
teste só vai aparecer na leitura de amanhã (01/09) — que, por coincidência de calendário,
é exatamente o dia do marco-alvo do evento Danantara na Indonésia (ver Riscos e Lente
fiscal). Amanhã, portanto, dois relógios batem ao mesmo tempo: o relógio do teste técnico
do rompimento de sexta e o relógio do catalisador regulatório do óleo.

Para quem não acompanha o complexo diariamente, vale reforçar o mecanismo de novo, porque
é ele que dá sentido a todos os números abaixo. A soja em grão é a matéria-prima; ela entra
numa esmagadora (crush) e sai como dois produtos com destinos de demanda completamente
diferentes — farelo, que é proteína e vai para ração animal, e óleo, que vai para consumo
humano e, cada vez mais, para biodiesel. O crush margin é a diferença entre o valor de
venda de farelo + óleo e o custo de compra da soja; ele mede, em dólares por bushel
(unidade de volume da soja, ~27,2 kg), quanto sobra para quem opera a esmagadora. Esse
indicador fechou a sexta-feira em **US$ 2,45/bushel** (indicators, 28/08, "Board Crush":
farelo 342,50 + óleo 70,82 − soja 1.288,00) — ainda abaixo do nível de referência de US$
2,50 que a fila monitora (`alerta-quebra_suporte-complexo_soja-2026-08-28`), mas em
recuperação de três pregões seguidos (US$ 2,09 em 26/08 → 2,18 em 27/08 → 2,45 em 28/08,
+17% em três dias). Dentro desse crush, quem "manda" — farelo ou óleo — é medido pelo
**oil share** (fatia do valor total do crush que vem do óleo): fechou em **50,83%**
(indicators, 28/08), pouco acima da metade, também em leve alta nos últimos três pregões
(50,3% → 50,5% → 50,83%). Os dois índices sintéticos internos seguem travados nos extremos
desde a semana passada: **Índice de Suporte do Óleo (ISO)** em **100/100** (5 de 5
condições estruturais favoráveis ao óleo) e **Índice de Sobra de Farelo (ISF)** em
**80/100** (4 de 5 condições apontando pressão baixista no farelo) — ambos repetidos nos
carimbos de 29, 30 e 31/08 porque não há pregão novo para recalculá-los.

O termômetro mais informativo do complexo continua sendo o **ratio Far/Soj** — o preço do
farelo dividido pelo valor equivalente em soja, que mede se o farelo está caro ou barato
EM RELAÇÃO à soja (não em valor absoluto). Fechou em **79,77%** em 28/08 (indicators),
ainda dentro da zona "abundante" (<80%) que o próprio sistema usa como limiar, mas subindo
de forma consistente há quatro pregões (78,46% em 25/08 → 78,93% → 79,12% → 79,77%). A
leitura que isso ensina é a mesma de domingo: o farelo está caro em valor absoluto (342,50
USD/sht) porque a SOJA está subindo mais depressa, não porque o farelo esteja isoladamente
escasso — é a soja que segue no comando do complexo, e é por isso que a pergunta mais
importante de amanhã não é "o farelo confirma o rompimento de 325?" mas sim "a soja segura
1.180?", porque se a soja cair o farelo cai proporcionalmente mais rápido enquanto o ratio
segue comprimido.

O que muda hoje, numa frase, é a NATUREZA da espera: deixamos de esperar o fim de semana
passar e passamos a esperar um dado que já existe (o fechamento de hoje já aconteceu em
Chicago) mas que ainda não chegou até nós. **Leitura de uma linha**: o pivô do complexo
continua sendo a soja, a maior convicção segue sendo a de que o rali tem fundo comprado
novo entrando via CFTC (ainda sem confirmação pós-rali), e o nível de confiança permanece
**médio-baixo** — não porque a tese tenha enfraquecido, mas porque o teste real dela
(tanto técnico quanto do catalisador Danantara) está literalmente a um dia de distância,
e a leitura de hoje ainda opera com os mesmos fatos de sexta-feira.

## Soja

**Viés: bull, moderadamente forte — tese de sexta ainda não retestada, mas com um pregão
real (hoje) já ocorrido e pendente de confirmação amanhã.**

O que sustenta a tese:

- **Rompimento técnico com quatro sessões corridas de calendário para consolidar (três de
  pregão real).** Soja CBOT fechou em 1.288,00 USD cts/bushel em 28/08/2026 (CME CBOT),
  9,2% acima da resistência de 1.180,00 monitorada pela fila
  (`alerta-quebra_resistencia-soja_cbot-2026-08-28`). O mecanismo por trás da força desse
  argumento é estatístico: quanto mais tempo um mercado passa sem devolver um rompimento,
  menor a probabilidade condicional de que ele tenha sido um "fakeout" (rompimento falso
  que reverte rápido) — mas hoje é o primeiro dia em que essa consolidação está sendo
  testada por um pregão de verdade, não por ausência de pregão. Sem o dado do fechamento
  de hoje, não dá para dizer se o quarto dia consolidou ou testou o nível.
- **Fundos com dinheiro novo entrando, não só cobertura — mas a foto está ficando velha
  rápido.** O corte CFTC COT de 25/08/2026 (Commodity Futures Trading Commission,
  regulador americano que publica toda sexta-feira a posição líquida dos grandes fundos)
  mostrava managed money em soja com long de 239.335 contratos (vs 197.446 em 18/08,
  +21,2%) e short de 38.656 contratos (vs 45.664, -15,3%) — o net long saltou 32,2% numa
  semana, com o open interest total (total de contratos em aberto) praticamente estável
  (972.531 vs 989.729, -1,7%). O mecanismo aqui é: quando o net long sobe muito mais rápido
  que o open interest total, é sinal de que dinheiro NOVO está entrando comprado, não
  apenas de que posições vendidas antigas estão sendo fechadas (que também empurraria o
  net long para cima, mas via cobertura, não convicção). O problema é que esse corte não
  enxerga NENHUMA das sessões do próprio rali (27-28/08) nem, agora, o pregão de hoje —
  são 6 dias corridos de defasagem, a maior desde que essa tese começou a ser acompanhada.
- **Câmbio ainda alinhado com o movimento, sem dado de hoje ainda.** USD/BRL fechou 28/08
  em 5,2005 (BCB PTAX, Banco Central do Brasil), +0,70% frente a 27/08 (5,1642) — a PTAX
  de hoje (segunda-feira) normalmente sai por volta do fim da tarde e ainda não está neste
  dump. A paridade CBOT-implícita em saca de 60kg (sem considerar basis/frete/prêmio
  portuário) está em R$ 147,67/saca (indicators, 28/08, CBOT 1.288,00 × USD/BRL 5,2005) —
  o câmbio até aqui reforça o rali de dólar em vez de competir com ele, mas essa conta só
  será atualizada quando a PTAX de hoje sair.
- **Físico brasileiro pagando prêmio sobre a paridade — última leitura, ainda válida.** O
  preço à vista em Paranaguá (CEPEA/ESALQ via NAG, o principal porto exportador de grãos
  do Sul do Brasil) fechou 28/08 em R$ 159,76/saca, R$ 12,09/saca (~8,2%) acima da
  paridade CBOT-implícita — basis físico positivo, sinal de mercado apertado no porto (ou
  seja, quem quer comprar soja física ali paga um prêmio sobre o que a bolsa de Chicago
  "deveria" indicar). O prêmio do porto sobre o interior do Paraná (R$ 151,32/saca) está em
  R$ 8,44/saca (5,6%), mesmo dado de domingo, sem atualização de segunda ainda.
- **Estoques brasileiros de soja seguem apertando estruturalmente rumo ao fim de 2026**
  nas projeções ABIOVE (Associação Brasileira das Indústrias de Óleos Vegetais, sem
  atualização nesta janela): estoque final recuando de 5.720,8 mil toneladas (out/26) para
  3.658,9 mil t (nov/26) e 1.889,9 mil t (dez/26) — parte é sazonalidade normal (fim de
  safra), mas alimenta o pano de fundo de oferta mais curta no encerramento do ano-safra.
- **USDA Crop Progress ainda em 23/08** (12% excelente / 48% boa / 9% ruim, comparado a
  12%/49%/8% em 16/08): leve deterioração na semana anterior, sem corte novo nesta janela
  para confirmar se a tendência de piora continuou — o próximo corte semanal do USDA
  (United States Department of Agriculture) normalmente sai às segundas à tarde, então
  pode chegar ainda hoje ou amanhã.

**O que invalida / risco:**

- O risco mais concreto de HOJE é justamente o pregão que já aconteceu e que ainda não
  vemos: qualquer notícia relevante do fim de semana ou da manhã de segunda (China, clima
  na Argentina/EUA, política comercial) pode ter gerado um movimento em Chicago hoje que
  nenhum número deste briefing captura. Trate a tese como "válida até prova em contrário
  no fechamento de hoje", que só vamos ver amanhã.
- O COT de 25/08 segue sem enxergar as sessões de 27-28/08 nem a sessão de hoje; o próximo
  corte (posições de terça 01/09, esperado por volta de sexta 04/09 pelo calendário
  semanal do CFTC — inferência, não confirmada no briefing) é o primeiro que vai mostrar
  se os fundos entraram comprados NO rali ou ficaram de fora. Já são 6 dias corridos de
  exposição a essa incerteza.
- Nível técnico a vigiar: qualquer fechamento de volta abaixo de 1.180 desfaz o
  rompimento.
- A notícia de 28/08 sobre uma decisão do STF (Supremo Tribunal Federal) mencionada no
  RSS segue sem teor detalhado no briefing — risco de cauda não quantificável enquanto
  durar essa lacuna de informação.

**Leitura operacional:** o trader que já está posicionado comprado no rompimento não tem
motivo, com os dados de hoje, para reduzir posição preventivamente — a estrutura segue
intacta e os motores (CBOT + câmbio) seguem alinhados. Mas o hiato do COT chegou a 6 dias
corridos sem ver o rali, e o fechamento de hoje (que só vamos conhecer amanhã) é o
primeiro teste real do nível de 1.180 como suporte. Quem está comprado sem proteção deveria
ter decidido o stop (por exemplo, 1.180) e o tamanho de posição ANTES da abertura de hoje —
se ainda não decidiu, o ideal é fazer isso agora, antes de ver o resultado do pregão, para
não deixar o próprio resultado influenciar a decisão de risco. Quem quer montar posição
vendida contra o movimento segue sem sinal técnico para isso — nada nos dados aponta
exaustão do rali, só uma lacuna de confirmação que se estreita a cada dia.

## Farelo

**Viés: bull na fita, mas com estrutura contraditória por baixo — leitura herdada de
sexta, também pendente do primeiro teste real hoje.**

O que sustenta a tese (na fita):

- **Rompimento de resistência com volume relevante.** Farelo CBOT fechou em 342,50 USD/
  short ton em 28/08/2026, 5,4% acima da resistência de 325,00
  (`alerta-quebra_resistencia-farelo_cbot-2026-08-28`), com alta de +2,42% no dia (vs
  334,40 em 27/08).
- **Cobertura de posição vendida agressiva no CFTC (foto de 25/08, ainda a mais recente).**
  Managed money com short caindo de 46.003 para 33.662 contratos (-26,8% em uma semana)
  enquanto o long ficou praticamente parado (129.318 → 129.615, +0,2%) — assinatura de
  "short covering" (fundos que estavam vendidos recomprando para fechar posição, o que
  empurra o preço para cima sem representar convicção compradora nova). Ainda sem corte
  novo para saber se essa cobertura já se esgotou ou ainda tem munição — 6 dias de
  defasagem, como em soja.
- **Físico brasileiro reagindo, ainda que atrasado.** O farelo MT/IMEA (NAG, Instituto Mato
  Grossense de Economia Agropecuária) saltou de R$ 1.726,20/ton (congelado por 5 sessões)
  para R$ 1.795,68/ton em 28/08 (+4,03%), fechando parte do gap para Rondonópolis/MT (R$
  1.870,00) e RS média (R$ 1.860,00). Sem dado novo de segunda ainda para confirmar se o
  repasse continuou.

O que tensiona a tese (a estrutura por baixo, inalterada desde sexta):

- **O ratio Far/Soj segue na zona "abundante" (<80%).** Fechou em 79,77% em 28/08
  (indicators) — quarta sessão seguida de alta gradual, mas ainda abaixo do limiar de 80%.
  O farelo continua relativamente barato frente à soja, mesmo depois do rompimento
  técnico — o que reforça a leitura de que é a soja, não o farelo, quem está no comando do
  movimento.
- **O ISF segue travado em 80/100**, inclusive no carimbo repetido de 31/08 (sem pregão
  novo para recalcular) — o sistema não vê o quadro estrutural de oferta de farelo mudando.
- **Prêmio de exportação em Paranaguá congelado em +0,12 USD/short ton desde 24/08** — já
  são 6 sessões sem se mexer mesmo com o board em alta forte, um padrão que já dura mais
  de uma semana.

**Trata a fila `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`:** esse
item já foi tratado em profundidade nas leituras de 29 e 30/08
([[2026-08-30_leitura-complexo]]) — a conclusão permanece válida hoje sem fato novo para
mudá-la: a compressão do ratio Far/Soj (que a tese original de 11/06 previa se resolver em
"1-2 semanas" e levou ~11 semanas para se confirmar) se confirmou, mas por um mecanismo
diferente do previsto — o farelo subiu em valor absoluto (CBOT de ~303,60 USD/sht em
10/06 para 342,50 hoje, +12,8%) em vez de cair a soja. Status: revisada, sem encerrar;
cita-se aqui de novo apenas para manter o rastro do `id`, não para reabrir a análise.

**O que invalida / risco:** o short de managed money já caiu 27% numa semana (foto de
25/08) — sobra menos munição de cobertura. Se o ratio Far/Soj voltar a CAIR (não subir) no
fechamento de hoje enquanto o preço absoluto segue alto, é sinal de que o farelo está
sendo carregado pela soja sem força própria — e qualquer correção na soja bateria
desproporcionalmente nele.

**Leitura operacional:** nada muda em relação a domingo por falta de pregão confirmado.
Para quem opera o spread Far/Soj, a zona de acumulação (ratio comprimido, <80% há 6+
sessões) segue válida para quem monta tese de reversão (long farelo / short soja), mas o
precedente de "1-2 semanas virou 72 dias" continua valendo como aviso contra apressar o
timing — especialmente com o fechamento de hoje ainda desconhecido.

## Óleo

**Viés: neutro — a divergência mais interessante do complexo permanece: ISO travado em
100 mas a margem de biodiesel comprimindo pregão após pregão, e agora um primeiro indício
(de baixa confiabilidade) de que essa compressão pode ter continuado no fim de semana.**

O que sustenta o lado comprado:

- **Salto do dia (sexta) segue sendo o maior das três pernas.** Óleo CBOT fechou em 70,82
  USD cts/lb em 28/08/2026, alta de +3,79% frente aos 68,23 de 27/08
  (`alerta-movimento_forte-oleo_cbot-2026-08-28`) — mais que o dobro da alta percentual da
  soja (+1,58%).
- **ISO travado em 100/100**, sem uma única sessão de enfraquecimento na janela disponível
  — mas vale repetir a ressalva de domingo: o ISO mede CONDIÇÕES estruturais (biodiesel
  positivo, RIN D4 sustentado, heating oil firme, oil share saudável, momentum técnico),
  não o TAMANHO da margem. Ele pode ficar em 100 mesmo com a margem encolhendo, desde que
  continue positiva.
- **Catalisador regulatório agora a menos de 24 horas de distância.** A fila traz
  `trib-DANANTARA-INDONESIA-2026-09-01`: amanhã, 01/09/2026 (terça-feira), a Indonésia
  projeta completar a centralização da exportação de óleo de palma sob o fundo soberano
  Danantara (tributario_watch.toml, id `DANANTARA-INDONESIA`, atualizado 05/06/2026,
  direção "alta" para óleo de soja). O mecanismo: quanto mais centralizada/burocratizada
  fica a exportação do maior óleo vegetal do mundo em volume, mais espaço abre para o óleo
  de soja como substituto na demanda global (biodiesel e alimentação). O evento está
  amanhã, mas o monitor tributário segue com 87 dias sem atualização — tratar como
  catalisador binário a confirmar, não como fato já precificado.
- **Levy de exportação da palma indonésia (até 12,5%, PMK 9/2026, id
  `INDONESIA-LEVY-PMK9`) segue vigente**, sustentando o óleo de soja por substituição de
  forma permanente, independentemente do desfecho da Danantara.

O que sustenta o lado vendido / cético:

- **Ainda abaixo do pivô técnico de 72,00.** O fechamento de 70,82 segue 1,6% abaixo do
  nível monitorado como suporte perdido (`alerta-quebra_suporte-oleo_cbot-2026-08-28`) —
  tecnicamente um repique dentro de uma estrutura ainda quebrada.
- **A margem de biodiesel americana está comprimindo há mais de uma semana, mesmo com o
  ISO em 100.** Série completa no briefing: 1,6481 USD/galão (21/08) → 1,5882 (24/08) →
  1,5313 (25/08) → 1,5678 (26/08) → 1,5264 (27/08) → 1,4102 (28/08) — queda de 14,4% em uma
  semana, com o maior tombo justamente no último pregão disponível (-7,6% de 27 para
  28/08). O mecanismo: o CUSTO do óleo (insumo do biodiesel) sobe junto com o rali do CBOT
  (+3,79% no dia), mais rápido do que a receita (heating oil + valor do crédito RIN D4,
  Renewable Identification Number, o certificado que comprova mistura de biocombustível
  nos EUA), espremendo quem produz biodiesel.
- **Primeiro indício (fraco) de que a pressão sobre a margem pode ter continuado.** O
  heating oil (HO=F, óleo combustível usado para aquecimento e como proxy de diesel nos
  EUA — compõe a RECEITA do biodiesel) tem um print de domingo, 30/08: fechamento 4,2962
  USD/galão, -1,4% frente ao fechamento de sexta (4,3567). Se esse número se confirmar
  como representativo da abertura de segunda (o que este briefing não permite afirmar —
  ver Honestidade sobre a natureza desse dado), a RECEITA do biodiesel caiu enquanto o
  CUSTO do óleo (que segue em 70,82, sem dado de hoje ainda) ficou parado — o que
  apertaria ainda mais a margem, não aliviaria. É um sinal de baixíssima confiabilidade
  (volume de apenas 901 contratos, ante os 19.477 de sexta-feira), mas é o único fio de
  informação sobre "o que pode ter acontecido" no intervalo entre sexta e hoje.
- **COT de 25/08 (ainda sem atualização) mostrava fundos DIMINUINDO net long antes do
  próprio rali** — managed money com long caindo de 116.669 para 114.248 (-2,1%) e short
  subindo de 25.436 para 29.132 (+14,5%) entre 18/08 e 25/08, net long recuando 6,7%. É o
  oposto do padrão em soja, e já são 6 dias corridos sem atualização — a maior lacuna
  relativa das três pernas porque é justamente aqui que a foto pré-rali contradizia o
  movimento.
- **Prêmio de exportação em Paranaguá congelado em +0,10 cts/lb desde 24/08** — mesmo
  padrão de estagnação do farelo.

**O que invalida / risco:** para o lado comprado, um fechamento de hoje de volta abaixo de
~69 devolveria o repique. Para o lado vendido, se a compressão da margem de biodiesel tiver
continuado no fim de semana (como o print de heating oil de domingo sugere, com toda a
cautela sobre confiabilidade já registrada acima), ela pode cruzar para terreno mais
apertado e finalmente puxar o ISO para baixo de 100 — o gatilho a vigiar não é mais só
heating oil ou RIN isoladamente, é a combinação custo-óleo × receita. O evento Danantara de
amanhã é binário: qualquer sinal de atraso (o precedente do B50 indonésio, monitorado desde
junho sem confirmação de execução plena — id `INDONESIA-B50` — mostra que anúncios
ambiciosos nem sempre viram fato no prazo) esfria o efeito bullish esperado.

**Leitura operacional:** segue sendo a perna mais indefinida das três, e amanhã concentra
dois testes ao mesmo tempo — o nível técnico de 72,00 e o marco Danantara. Quem está
comprado tem a favor o ISO no teto e o evento regulatório; quem está vendido tem a favor o
nível técnico não reconquistado, o COT desatualizado mostrando fundos céticos, e agora
também um indício (fraco, mas direcionalmente consistente) de que a margem de biodiesel
pode ter seguido comprimindo no fim de semana. Ainda faz mais sentido tratar óleo como
parte do spread/crush do que como aposta direcional pura antes de amanhã.

## Spreads e crush (leitura de complexo)

Juntando as três leituras: o ratio Far/Soj em 79,77% (zona "abundante", <80%) e o oil
share em 50,83% dizem que, em termos relativos, a soja segue cara frente ao farelo, e o
crush está quase empatado entre farelo e óleo como fonte de receita — nenhum dos dois
domina folgadamente em termos de valor bruto. Os dois índices sintéticos, porém, desenham
um retrato mais assimétrico: ISF em 80 (sobra estrutural de farelo) e ISO em 100 (domínio
estrutural do óleo) — o sistema "acredita" mais na tese de suporte ao óleo do que na tese
de sobra do farelo, mesmo que o oil share bruto não mostre essa assimetria com tanta
clareza. O crush margin em US$ 2,45/bushel está subindo (2,09 → 2,18 → 2,45 em três
pregões) porque farelo (+2,42%) e óleo (+3,79%) subiram mais, juntos, do que a soja
(+1,58%) — mas dentro desse óleo que "ajudou" o crush a subir, a margem de biodiesel
específica (que mede quanto sobra para o USINEIRO de biodiesel, não para o crushor de
soja) está comprimindo há mais de uma semana. São duas margens diferentes reagindo de
formas opostas ao mesmo movimento de preço: o crush da esmagadora de soja melhora, a
margem do produtor de biodiesel piora — o mesmo rali de óleo que é bom para quem vende a
matéria-prima é custo mais alto para quem a transforma em combustível.

Para quem opera o spread Far/Soj: a compressão abaixo de 80% já dura pelo menos 7 sessões
(desde 24/08) sem reverter de forma consistente — o avanço de 78,46% para 79,77% nos
últimos 4 pregões é gradual, não um estouro. Trate como zona de acumulação para quem monta
a tese de reversão (farelo relativamente barato tende a se recuperar frente à soja), mas
sem timing definido — a experiência de junho (ver seção Farelo) prova que "esticado" pode
continuar esticado por meses. Para quem opera o crush diretamente: 2,45 está abaixo do
referencial histórico de 2,50 mas em recuperação de 3 dias — segue sendo zona neutra até o
fechamento de hoje (ainda desconhecido) confirmar ou reverter essa recuperação.

## Lente fiscal/regulatoria BR

Antes de fechar qualquer tese de preço BR, os vetores tributários/regulatórios vivos que
pesam no complexo — todos do `system/tributario_watch.toml`, cujo carimbo mais recente
(`atualizado_em`) em TODOS os eventos é 2026-06-05, ou seja, **87 dias sem revisão**:

- **MP 1.363/2026** (id `MP-1363-2026`, subvenção diesel fóssil R$ 1,12/L, vigente até
  31/12/2026): barateia o diesel fóssil no mix B15 (mistura de 15% de biodiesel ao diesel
  fóssil, obrigatória no Brasil), reduzindo a competitividade relativa do biodiesel e a
  demanda doméstica por óleo de soja — vetor de baixa para óleo, sem mudança de status.
- **B16 (id `B16-CNPE-2026`, elevação da mistura de biodiesel para 16%)** segue "adiado" —
  CNPE (Conselho Nacional de Política Energética) cancelou em maio, testes técnicos com
  resultado esperado só por volta de novembro/2026. Upside represado (~436 mil toneladas
  de óleo adicional de demanda potencial), não corrente.
- **Isenção de PIS/Cofins do biodiesel na mistura** (id `PISCOFINS-BIODIESEL-ISENCAO`): o
  TOML registra vigência ATÉ 31/07/2026 — já **31 dias corridos vencida** frente aos
  31/08/2026 de hoje, sem qualquer registro de prorrogação ou expiração no arquivo. Segue
  sendo uma lacuna real de informação (ver Honestidade), não uma leitura de preço.
- **MP 1.358/2026** (subvenção gasolina R$ 0,89/L, mencionada com vigência até 11/07/2026
  na leitura de domingo): também já **51 dias corridos vencida**, mesma lacuna de
  informação sobre renovação.
- **STJ REsp 2.165.276** (id `STJ-RESP-2165276`, crédito de PIS/Cofins sobre soja em
  biodiesel, vigente, direção "alta" para soja/óleo): alívio de custo pontual, não
  vinculante (não é decisão repetitiva, ou seja, não obriga automaticamente outros casos
  semelhantes).
- **EPA RFS 2026/2027** (id `EPA-RFS-2026-2027`, mandato de biocombustível americano da
  Environmental Protection Agency, vigente desde 15/06/2026, direção "alta" para óleo):
  volumes recordes de RINs sustentam a margem de biodiesel americana — mesmo que essa
  margem esteja comprimindo pregão a pregão (ver seção Óleo), o mandato em si não mudou de
  status.
- **Crédito 45Z** (id `45Z-CLEAN-FUEL`, Clean Fuel Production Credit americano, em
  tramitação, direção "mista"): se a regra final excluir insumo importado da
  elegibilidade, o óleo de soja DOMÉSTICO americano ganha, mas o sebo bovino brasileiro
  hoje exportado como insumo perderia esse mercado e voltaria para o blend doméstico
  americano — o que tira, na margem, demanda do óleo de soja DENTRO do Brasil. Vetor que
  pode virar contra o óleo de soja BR mesmo sendo favorável ao óleo de soja americano.
- **Indonésia — Danantara** (id `DANANTARA-INDONESIA`) e **levy de exportação PMK
  9/2026** (id `INDONESIA-LEVY-PMK9`): já tratados na seção Óleo, ambos direção "alta"
  para óleo de soja via substituição de palma. Danantara agora a menos de 24h do
  marco-alvo (amanhã, 01/09).
- **Notícia de 28/08/2026** sobre uma decisão do STF segue sem teor detalhado no
  briefing, e não há nenhum evento STF cadastrado no `tributario_watch.toml` (só STJ) —
  não é possível avaliar o impacto com os dados disponíveis; fica como item para
  acompanhar, não para precificar.

## Riscos e eventos próximos

- **01/09/2026 (amanhã, terça)** — marco-alvo da centralização plena da exportação de
  palma pela Danantara (Indonésia), `trib-DANANTARA-INDONESIA-2026-09-01`; vigiar se a
  assunção da cadeia se confirma no prazo ou escorrega, como já aconteceu com o B50
  indonésio (`INDONESIA-B50`). Coincide com o dia em que o fechamento de hoje (31/08)
  finalmente deve aparecer no pipeline — dois testes simultâneos.
- **Fechamento de hoje, 31/08/2026** — já ocorreu em Chicago no momento em que este
  briefing foi compilado, mas ainda não está neste dump. É o primeiro teste real da tese
  herdada de sexta-feira. Vigiar especialmente se soja segura 1.180, farelo segura 325 e
  se óleo consegue finalmente fechar acima de 72,00.
- **Próximo corte CFTC COT** — posições de terça 01/09, com publicação estimada por volta
  de sexta 04/09 pelo calendário semanal do CFTC (inferência, não confirmada no
  briefing): é o dado que revela se os fundos entraram comprados NAS sessões de rali
  (27-28/08) ou ficaram de fora, agora com 6+ dias de defasagem acumulada.
- **NOPA mensal** (`release-nopa-2026-08-31`): a fila sinaliza um "release novo", mas o
  conteúdo (`monthly_status` 0,0 bool, paywall) é idêntico ao dos dias anteriores — não há
  confirmação real do ritmo de esmagamento americano ainda.
- **USDA WASDE**: ausente da janela há bastante tempo; qualquer publicação nova é
  catalisador potencial de revisão de balanço mundial.
- **USDA Crop Progress semanal**: normalmente publicado às segundas à tarde (horário dos
  EUA) — pode chegar ainda hoje ou amanhã, atualizando o corte de 23/08.
- **Vigência da isenção PIS/Cofins do biodiesel** (TOML aponta 31/07/2026, agora 31 dias
  vencida sem confirmação de prorrogação) e **MP 1.358/2026 da gasolina** (51 dias
  vencida) — checar notícia de renovação/expiração antes de assumir qualquer tese de
  custo de combustível BR.
- **Clima**: calor extremo e céu limpo no núcleo produtor de Mato Grosso (41°C em Cuiabá/
  Sinop/Lucas do Rio Verde, INMET, previsão para hoje 31/08) contrasta com chuva e
  trovoadas no Sul (Passo Fundo/RS, Cascavel/PR, Maringá/PR) — relevante para a JANELA DE
  PLANTIO da safra 2026/27 que se aproxima (set/out); solo seco no núcleo produtor às
  vésperas do plantio é vetor a monitorar, ainda não problema confirmado de safra.
- **Margem de biodiesel americana em compressão de mais de uma semana** (1,65 → 1,41
  USD/galão, 21/08 a 28/08), com um indício fraco (heating oil de domingo, -1,4%) de que a
  pressão pode ter continuado — se confirmado no fechamento de hoje, é o vetor mais
  próximo de derrubar o ISO de 100, o índice mais "unânime" do briefing até aqui.

## Honestidade

- **O padrão de revisão retroativa do fechamento de 28/08 agora parece cíclico, não só
  ruidoso — e essa é a descoberta mais concreta desta leitura.** Comparando as três
  últimas leituras para a MESMA sessão de 28/08:
  - Leitura de 29/08 ([[2026-08-30_leitura-complexo]], citando [[2026-08-29_leitura-complexo]]):
    soja 1.287,75 (vol. 153.472), farelo 342,70 (vol. 46.745), óleo 70,71 (vol. 57.670).
  - Leitura de 30/08: soja 1.288,00 (vol. 162.537), farelo 342,50 (vol. 43.217), óleo
    70,82 (vol. 64.978).
  - Este briefing (31/08, hoje): soja 1.288,00 (vol. 153.472), farelo 342,50 (vol. 46.745),
    óleo 70,82 (vol. 57.670).
  Ou seja: os PREÇOS de fechamento estabilizaram entre a leitura de ontem e a de hoje
  (1.288,00 / 342,50 / 70,82 nas duas últimas leituras, sem mudança) — mas os VOLUMES
  voltaram EXATAMENTE aos valores que apareciam na leitura de 29/08, abandonando os
  valores intermediários de 30/08. Isso não parece um simples "ainda ajustando o dado mais
  recente" (que seria uma progressão numa direção); parece mais um pipeline que está
  alternando entre (pelo menos) duas versões cacheadas ou duas fontes diferentes do mesmo
  dado histórico. Tratar qualquer leitura de volume desta sessão como não confiável até o
  dado se manter estável por 3+ dumps seguidos — o que ainda não aconteceu.
- **Nenhum fechamento novo de soja/farelo/óleo desde sexta-feira, apesar de hoje ser dia
  de pregão real.** Diferente do fim de semana (onde a ausência de dado novo é esperada
  porque não há sessão), hoje HOUVE sessão e o dado ainda não chegou — uma lacuna
  temporal genuína, não apenas a repetição de um fato já conhecido.
- **Assimetria na cobertura de dados overnight/Globex.** O heating oil (HO=F) tem um print
  para domingo, 30/08 (fechamento 4,2962, volume 901 contratos), presumivelmente captando
  a abertura eletrônica noturna do contrato — mas os três tickers agrícolas centrais do
  complexo (ZSX26, ZMV26, ZLV26, que também operam em horário quase contínuo via CME
  Globex) não têm NENHUM print entre 28/08 e hoje. Isso sugere uma assimetria na coleta de
  dados entre famílias de contrato (energia vs. agrícolas) na mesma fonte, não uma
  diferença real de horário de mercado — e significa que, mesmo que os contratos
  agrícolas tenham negociado durante o fim de semana/noite de domingo, não temos
  visibilidade sobre esse movimento.
- **`noticias_rss` registra "3 mantidos" em 31/08 mas nenhum headline específico de hoje
  aparece no dump** — não há como saber se são notícias de preço, clima, ou institucionais
  como a de plantio de 30/08. Nenhum conteúdo foi inventado para preencher essa lacuna.
- **COT desatualizado, agora com 6 dias corridos de defasagem** (corte de 25/08 frente ao
  fechamento de 28/08, mais o fim de semana e hoje em cima) — a maior lacuna desta leitura.
- **Prêmios de exportação (Paranaguá, farelo e óleo) seguem congelados**, agora 6 sessões
  seguidas idênticas — não dá para saber se reflete mercado físico realmente parado ou
  limitação de atualização da fonte (NAG).
- **Decisão do STF mencionada na notícia de 28/08 segue sem teor detalhado** no briefing —
  não há vínculo a nenhum evento do `tributario_watch.toml`. Nenhum conteúdo foi inventado
  para essa decisão.
- **`tributario_watch.toml` sem atualização há 87 dias** — pelo menos dois vetores
  (isenção PIS/Cofins do biodiesel, vigência até 31/07; MP 1.358/2026, vigência até 11/07)
  já passaram da data de vigência registrada sem nota de renovação ou expiração. Tratados
  como "status desconhecido pós-vigência".
- **NOPA segue inacessível** (paywall) — o "release novo" sinalizado pela fila
  (`release-nopa-2026-08-31`) não trouxe nenhum número de esmagamento americano mensal
  confirmado; é um falso positivo de novidade, não um dado novo.
- **USDA WASDE ausente** da janela — nenhuma leitura de balanço mundial oficial
  atualizado disponível.
- **Percentil histórico de posicionamento COT não está disponível no briefing** — toda
  leitura de "fundos comprando/vendendo" nesta análise usa variação semana a semana de
  contratos absolutos, não percentil histórico. Nenhum percentil foi inventado.
- **MPOB (palma Malásia) segue com parser quebrado** (3.456 caracteres, sem números
  extraídos) desde pelo menos 27/08 — nenhum dado de produção/estoque de palma malaia
  disponível para cruzar com a tese de substituição via Indonésia.
