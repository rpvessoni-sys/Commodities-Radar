---
data: 2026-07-18
titulo: "Sábado sem sessão: a segunda geração dos dados de sexta (17/07) revisa fechamentos e margem de biodiesel, mas confirma os três vieses de ontem — soja acima da resistência com folga maior (2,08%), farelo com o ratio Far/Soj agora mais solidamente abaixo de 80% (79,75%, ante 79,98% na leitura de ontem), e óleo seguindo como a perna mais forte do complexo — mercado fechado até segunda (20/07), quando chegam a nova sessão e o Crop Progress semanal"
tags: [complexo, auto-claude]
fontes:
  - CBOT CME (ZSQ26/ZMQ26/ZLQ26 + curva forward completa + HO=F) — sessão de 2026-07-17 (última sessão disponível; mercado fechado 18-19/07, fim de semana), segunda geração de dados, com revisão de fechamento frente à leitura de ontem
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, ISF/ISO, paridade BR) — recalculados sobre os closes revisados de 2026-07-17, série de 13 a 18/07 (ISF/ISO também recalculados hoje, 18/07, sem variação)
  - BCB PTAX — 2026-07-17 (USD/BRL 5,1176), sem publicação nova hoje (sábado, sem pregão bancário)
  - CEPEA/ESALQ Paranaguá e Paraná interior via NAG — 2026-07-17 (suporte Paranaguá R$ 141,02/saca, Paraná interior R$ 134,11/saca), sem dado novo hoje
  - NAG Físico BR (farelo MT/IMEA, RS, Rondonópolis; prêmios export PGUA farelo/óleo) — último dado 2026-07-17
  - CFTC COT Managed Money — ainda referência 2026-07-14, sem atualização (próximo dado esperado ~21/07, publicação ~24/07)
  - USDA Crop Progress — ainda 2026-07-12 (65% bom-ou-melhor), sem atualização; próximo relatório normal ~2026-07-20 (segunda-feira, dado "as of" 19/07)
  - USDA WASDE — ainda 2026-07-10 (só farelo Argentina/Brasil/China parcial), sem publicação nova
  - NOPA — 2026-07-18, `monthly_status` continua inacessível (paywall), fila `release-nopa-2026-07-18`
  - ABIOVE projeções mensais — balanços ago-dez/2026 (farelo/óleo/soja), sem alteração
  - NOAA CPC ENSO — 2026-07-18 (El Niño Advisory, sem mudança)
  - MPOB — 2026-07-18 (parser sem números extraídos, 3.439 caracteres, mesmo texto de pelo menos 9 dias)
  - BCBA — 2026-07-18 (acessível, sem links de relatório detectados)
  - Notícias Agrícolas/Canal Rural RSS — 2026-07-18 (160 itens lidos, 6 mantidos; manchete "Você viu? Produtor gaúcho diz precisar de 54 sacas de soja por ano só para pagar dívidas", Canal Rural)
  - Forecasts estatísticos internos — 2026-07-18 (as seis bandas — 3 commodities × 2 horizontes — seguem simultaneamente em viés altista, terceira leitura seguida nessa condição, spot ref já refletindo os closes revisados de 17/07)
  - system/tributario_watch.toml — MP-1358-2026 (vigência formal encerrada há 7 dias, status ainda "tramitação"), PISCOFINS-BIODIESEL-ISENCAO (vence em 13 dias), MP-1363-2026, STJ-RESP-2165276, B16-CNPE-2026, EPA-RFS-2026-2027, 45Z-CLEAN-FUEL, DANANTARA-INDONESIA, INDONESIA-B50, INDONESIA-LEVY-PMK9 — todos `atualizado_em` 2026-06-05 (43 dias sem atualização do monitor)
  - Cruza com [[2026-07-17_leitura-complexo]], [[2026-07-16_leitura-complexo]], [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (checkpoint D+7, tratado abaixo — agora 30 dias vencido), [[2026-05-26_subvencao-fossil-aperta-biodiesel]]
status: ativa
vies: [bull-soja, bear-farelo, bull-oleo_soja]
---

> **Nota de proveniência:** hoje, sábado 18/07/2026, não há novo pregão na CBOT
> (mercado fecha sexta e reabre segunda). O dump de hoje não traz nenhum
> fechamento novo de soja/farelo/óleo — mas o pipeline reprocessou os dados de
> sexta-feira (17/07) e produziu uma **segunda revisão** de vários números que a
> leitura de ontem já havia tratado como "definitivos". A diferença desta vez é
> mais sutil que as anteriores (não inverte o sinal de nenhuma tese), mas dois
> pontos merecem atenção redobrada: (1) o ratio Far/Soj de 17/07 foi revisado de
> 79,98% para 79,75% — o cruzamento abaixo de 80% ficou **mais** confortável, não
> menos; e (2) a margem de biodiesel americana de 17/07 foi revisada de 0,7029
> para 0,8189 USD/galão — uma correção de +16,5% que muda a leitura de "pior
> valor da janela" para "terceiro pior", porque o heating oil de 17/07 (insumo de
> receita do biodiesel) foi revisado de queda (-2,0%) para alta (+0,84%) no dia.
> A seção Honestidade detalha as duas revisões número a número.

## Visão geral

O complexo soja é uma fábrica com uma única matéria-prima (a soja em grão) e
dois produtos de saída em proporção fixa por bushel esmagado: o **farelo**
(fração proteica, ~78% da massa, vira ração animal) e o **óleo degomado**
(fração de gordura, ~18-20% da massa, vira óleo de cozinha e biodiesel). Quem
decide o ritmo de esmagamento é a esmagadora, olhando a **crush margin** (valor
de farelo + óleo por bushel, menos o custo daquele bushel de soja, medido na
CBOT — Chicago Board of Trade, a bolsa de referência mundial para esses
contratos) e o **oil share** (fração desse valor capturada pelo óleo). Quando o
oil share sobe, o óleo passa a "pagar o crush" sozinho, e o farelo vira, cada
vez mais, um subproduto que a esmagadora aceita vender barato só para liberar o
óleo — é esse mecanismo que está por trás do **ratio Far/Soj** (preço do farelo
dividido pelo preço da soja, normalizado pela conversão bushel↔short ton):
quando cai abaixo de 80%, o farelo está historicamente "abundante" frente à
soja, e o spread tende a comprimir (é um spread de mean-reversion — comprimido
demais tende a esticar de volta, esticado demais tende a comprimir; hoje o sinal
aponta para o lado "comprimido").

**Hoje é sábado, e não há pregão novo para analisar** — a CBOT fecha na
sexta-feira à noite (horário de Chicago) e só reabre domingo à noite
(horário de Brasília já é segunda de manhã em Chicago). O que o dump de hoje
traz de genuinamente novo não é preço, é **reprocessamento**: pela quarta vez
nesta série de leituras, os números de uma sessão já "fechada" mudaram entre
uma geração do dump e a seguinte. Desta vez os closes de soja (1.204,50 cts/bu,
+0,50 frente ao 1.204,00 de ontem), farelo (320,20 USD/sht, -0,80 frente ao
321,00 de ontem) e óleo (74,81 cts/lb, praticamente idêntico ao 74,82 de ontem)
tiveram ajustes pequenos — mas o **ratio Far/Soj** e a **margem de biodiesel**,
que dependem de razões entre esses números, tiveram movimentos proporcionalmente
maiores. O ratio caiu de 79,98% (ontem) para 79,75% (hoje) — o cruzamento abaixo
do limiar de 80% que ontem foi tratado como "frágil, por margem de apenas 0,02
ponto" ficou hoje **mais robusto**, com 0,25 ponto de distância. Trata
`ratio-zona-2026-07-17`. Ao mesmo tempo, a soja segue folgadamente acima da
resistência de 1.180,00 (agora 2,08% de distância, ante 2,03% ontem — trata
`alerta-quebra_resistencia-soja_cbot-2026-07-17`), e o óleo segue como a perna
mais forte do dia (+3,29% no pregão de sexta, trata
`alerta-movimento_forte-oleo_cbot-2026-07-17`). A crush margin (3,2285
USD/bushel, farelo 320,20 + óleo 74,81 − soja 1.204,50) segue no maior valor da
janela de cinco dias, pela terceira sessão seguida em alta, mesmo com a
revisão. **Leitura de uma linha:** com o mercado fechado neste fim de semana, o
pivô de hoje não é um novo movimento de preço, é a confirmação de que os três
vieses da véspera (bull tático em soja, bull forte em óleo, bear estrutural com
tático agora mais sólido em farelo) sobrevivem — e até se fortalecem
marginalmente — a uma segunda rodada de revisão de dados; convicção
moderada-alta em soja e óleo, moderada-alta (upgrade de moderada) em farelo,
com a confirmação de segunda-feira (nova sessão + Crop Progress) como o próximo
teste real.

---

## Soja

**Viés: bull tático (convicção moderada-alta, mantido da leitura de ontem) —
fechou em 1.204,50 cts/bu na sessão de sexta-feira (17/07/2026, dado revisado
hoje, +0,50 frente ao valor tratado ontem como definitivo), 2,08% acima da
resistência 1.180,00. Trata `alerta-quebra_resistencia-soja_cbot-2026-07-17`.
Sem pregão novo hoje (sábado) para testar a tese em tempo real.**

### O que sustenta a tese

**A vela de sexta-feira, agora na sua segunda revisão, continua sendo a mais
forte da semana.** Fechamento revisado de 1.204,50 cts/bu (CBOT, sessão de
17/07/2026), com abertura em 1.195,00 (idêntica ao fechamento de 16/07, sem
gap), mínima de 1.186,75 e máxima de 1.205,25 — abertura, mínima e máxima não
mudaram frente à leitura de ontem, só o fechamento subiu 0,50 ponto (de
1.204,00 para 1.204,50). O fechamento fica a apenas 0,75 ponto da máxima do
dia, sobre um range de 18,50 pontos — 96% do movimento do dia terminou perto do
topo, uma fração ainda maior que os 93% calculados ontem sobre o valor não
revisado. A distância de segurança até o suporte estrutural de 1.180,00 subiu
de 2,03% (leitura de ontem) para 2,08% (hoje, com o fechamento revisado) — a
revisão, por menor que seja, empurra a tese na mesma direção, não na oposta,
o que é o padrão mais tranquilizador possível dado o histórico desta série de
inversões.

**A sequência dos últimos cinco fechamentos, incorporando a revisão de hoje —
1.196,75 (13/07) → 1.192,75 (14/07) → 1.202,25 (15/07) → 1.195,00 (16/07) →
1.204,50 (17/07, revisado)** — mantém o mesmo formato descrito ontem: uma
consolidação lateral com viés de alta, com o fechamento de sexta-feira sendo o
mais alto da janela de cinco dias (ligeiramente acima até do de 15/07). O
rompimento de alta de 06-07/07 (que levou o preço de ~1.180,00 para a faixa
de 1.190-1.205) segue integralmente válido.

**A manchete de demanda de exportação de sexta segue sendo, muito
provavelmente, o gatilho mais direto do movimento — sem notícia nova hoje que
a reforce ou contradiga.** Farm Progress noticiou em 17/07/2026: "USDA exports
– 3 large soybean sales announced" (farmprogress.com/marketing/flash-sales).
Esses "flash sales" são vendas de exportação privada dos EUA que, por
regulação do USDA, precisam ser declaradas em até 24 horas quando ultrapassam
100 mil toneladas para um único destino ou 200 mil toneladas para múltiplos
destinos — ou seja, são vendas já fechadas, não estimativa, o tipo de notícia
que historicamente move o mercado de forma direta. O dump de hoje (18/07) não
traz nenhuma manchete nova de soja — a única manchete capturada hoje é sobre
o produtor gaúcho endividado (ver adiante, fundamentos BR) — então a tese de
demanda de exportação como catalisador do rali de sexta segue sem confirmação
ou contradição adicional neste fim de semana.

**A curva forward, sem pregão novo, permanece exatamente a mesma descrita
ontem**: Agosto/26 (Q26, spot) 1.204,50 → Setembro/26 (U26) 1.193,50 (desconto
de −11,00, −0,91%) → Novembro/26 (X26) 1.203,00 (recupera +9,50 sobre setembro,
ficando praticamente colado ao spot) → Janeiro/27 (F27) 1.216,75 (+1,14% sobre
novembro) → Março/27 (H27) 1.220,00 (+0,27% sobre janeiro). O formato de
"sorriso" (desconto no meio, prêmio na ponta longa) segue intacto — o mercado
não está precificando um susto estrutural de oferta na curva.

**A paridade teórica em reais, recalculada com o fechamento revisado de hoje,
ficou em R$ 135,89/saca 60kg** (indicadores, sobre CBOT 1.204,50 cts × PTAX
5,1176 USD/BRL de 17/07 — sem PTAX novo hoje, sábado). Comparando com o físico
de Paranaguá de 17/07 (R$ 141,02/saca, CEPEA/ESALQ via NAG): um prêmio de
R$ 5,13/saca (+3,78%) do físico sobre a paridade teórica. A leitura de ontem
havia calculado esse prêmio em 3,81% sobre uma paridade ligeiramente menor
(R$ 135,84); com a revisão de hoje, o número muda muito pouco (3,78%),
confirmando a tendência de leve compressão do prêmio físico-sobre-papel
observada nas últimas duas leituras (4,68% em 16/07 → 3,81% em 17/07-ontem →
3,78% em 17/07-revisado-hoje) — a essa altura já são três pontos de dado
seguidos na mesma direção, o suficiente para começar a levar a sério a
possibilidade de uma tendência real, não apenas ruído (ver Honestidade). O
físico do Paraná interior fechou em R$ 134,11/saca (17/07, NAG, sem dado novo
hoje), um desconto de R$ 6,91/saca frente ao suporte de Paranaguá, dentro do
spread logístico normal já documentado.

**Uma manchete de hoje, embora não seja sobre preço, é relevante para o
fundamento físico brasileiro e merece registro cauteloso.** Canal Rural
publicou em 18/07/2026: "Você viu? Produtor gaúcho diz precisar de 54 sacas de
soja por ano só para pagar dívidas" — uma reportagem qualitativa (sem número de
área, safra ou valor de dívida citado no headline capturado pelo dump) sobre
estresse financeiro entre produtores do Rio Grande do Sul. O mecanismo, se a
tendência for disseminada: produtores endividados podem ser forçados a vender
grão mais cedo (pressão de oferta física de curto prazo, potencialmente
bearish para o basis local) ou, alternativamente, podem segurar estoque na
esperança de preços melhores para cobrir a dívida (o oposto). Como é uma única
manchete anedótica, sem dado quantitativo formal, ela **não** deve ser tratada
como driver de preço nesta leitura — está registrada aqui como um sinal de
fundo a monitorar, não como suporte ou risco para a tese de hoje (ver
Honestidade, item sobre uso de notícias qualitativas).

**O COT (CFTC) permanece com o mesmo dado de referência de ontem, 14/07/2026,
sem atualização.** Managed money net long em soja em +75.191 contratos (7,48%
do open interest de 1.004.746), ante +69.579 contratos (7,13% do OI de
975.954) em 07/07/2026 — um crescimento acompanhado de OI total subindo
+2,95% na semana, assinatura de dinheiro novo entrando comprado, não apenas
de posições vendidas fechando. O próximo COT (dado esperado ~21/07, publicação
~24/07) é que vai mostrar se essa compra continuou durante a semana do
rompimento de 17/07.

**O USDA Crop Progress permanece parado em 12/07/2026** (65% da lavoura
americana em condição boa-ou-excelente, 12% excelente + 53% boa, 6% em
condição ruim). O próximo relatório semanal normal deve sair na segunda-feira,
20/07/2026 ("as of" 19/07) — a apenas dois dias de distância.

**Os forecasts estatísticos internos (18/07/2026, calculados sobre o spot
revisado de 1.204,50)** seguem altistas: central 7d = 1.233,54 cts/bu (bandas
1.182,23-1.284,86); central 30d = 1.339,97 cts/bu (bandas 1.233,73-1.446,20).
É a terceira sessão seguida em que as seis bandas do sistema (soja, farelo e
óleo, 7d e 30d) fecham simultaneamente em viés altista — os valores de hoje são
praticamente idênticos aos de ontem, coerente com não haver pregão novo para o
modelo reagir.

### O que invalida / risco para a soja

- **Um fechamento de volta abaixo de 1.195,00 (fechamento de 16/07) ou de
  1.186,75 (mínima de sexta-feira) na reabertura de segunda-feira**
  questionaria a força da recuperação em V e reabriria o cenário de teste do
  suporte 1.180,00.
- **Uma terceira revisão dos números de 17/07 que reverta o sinal** — pouco
  provável dado que já são duas gerações apontando na mesma direção, mas o
  histórico desta série (quatro episódios de revisão material em cinco
  leituras) não permite descartar por completo.
- **O prêmio físico de Paranaguá sobre a paridade continuar comprimindo** — já
  são três leituras seguidas de compressão (4,68% → 3,81% → 3,78%); uma quarta
  reforçaria a hipótese de que o físico não está acompanhando a força do
  papel.
- **O COT de 21/07 (publicação ~24/07) mostrar que os fundos venderam durante
  o rompimento** — o dado disponível (14/07) ainda é de antes do movimento.
- **O USDA Crop Progress de segunda-feira (20/07) mostrar melhora
  continuada** da lavoura americana — reduziria o argumento de oferta apertada
  que sustenta parte do apetite comprador.

### Leitura operacional — soja

Sem pregão hoje, a leitura operacional de sábado é essencialmente uma
checagem de solidez da tese: a segunda revisão dos dados de sexta-feira
reforçou, em vez de enfraquecer, o rompimento de resistência (2,08% de folga,
ante 2,03% ontem), o que dá mais confiança para manter posição comprada
alinhada ao rompimento de 06-07/07, com 1.180,00 seguindo como referência de
stop lógica. Para quem está vendido contra esse rompimento, a tese de hoje não
oferece nenhum alívio adicional frente à leitura de ontem — a posição segue
questionada pelos mesmos fundamentos. O evento mais importante da próxima
semana é duplo: a reabertura de segunda-feira (20/07), que vai mostrar se o
mercado global (Ásia, Europa) reagiu a algo no fim de semana, e o Crop
Progress do mesmo dia, que atualiza pela primeira vez em 8 dias a condição da
lavoura americana.

---

## Farelo

**Viés: bear (estrutural mantido, tático agora mais sólido que ontem). O
ratio Far/Soj da sessão de 17/07/2026 foi revisado hoje para 79,75%
(indicadores: farelo 320,20 ÷ soja 1.204,50, base normalizada), ante 79,98% na
leitura de ontem — o cruzamento abaixo do limiar de 80% ganhou margem, não
perdeu. Trata `ratio-zona-2026-07-17` e
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` (revisão
programada, hoje 30 dias vencida — ver abaixo).**

### O que sustenta a tese

**O ratio Far/Soj, na sua segunda revisão para a sessão de 17/07, ficou mais
confortavelmente abaixo de 80%, não menos.** Refazendo a sequência com os
números que o sistema hoje trata como definitivos: 79,52% (13/07) → 79,83%
(14/07) → 79,58% (15/07) → 81,06% (16/07) → **79,75% (17/07, revisado de
79,98%)**. A distância abaixo do limiar de 80% passou de 0,02 ponto percentual
(leitura de ontem) para 0,25 ponto (hoje) — ainda pequena em termos absolutos,
mas 12,5 vezes maior que a margem que ontem foi tratada como "frágil demais
para confirmação robusta". A postura recomendada ontem — aguardar uma segunda
sessão consecutiva abaixo de 80% antes de tratar o gatilho como robusto —
segue válida, porque hoje não é uma segunda sessão nova (é a mesma sessão de
sexta revisada), mas a direção da revisão é um sinal favorável à tese: se o
número estivesse "no limite" por erro de captura, seria pelo menos igualmente
provável que a revisão o levasse de volta para cima de 80% quanto para baixo —
o fato de ter ido mais para baixo é um dado a favor da robustez do cruzamento,
não contra.

**Tratando `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`:**
a revisão programada da tese original (insight
[[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]) tinha data-alvo
18/06/2026 — hoje, 18/07/2026, ela está exatamente **30 dias vencida**. As três
perguntas da revisão D+7 eram: (1) o ratio fechou abaixo de 80%? (2) o WASDE
mudou o quadro? (3) o NOPA confirmou o ritmo de esmagamento? Respostas com os
dados de hoje: (1) **sim**, com margem agora mais confortável (79,75%, ante os
79,98% frágeis de ontem) — ainda assim sem uma segunda sessão de pregão
independente para confirmar (o mercado está fechado); (2) **não**, o WASDE
segue parado em 10/07/2026, sem cobertura de soja em grão ou óleo; (3) **não**,
o NOPA segue inacessível (trata `release-nopa-2026-07-18`, ver abaixo). Status
da tese original: mantida como "bear-farelo estrutural", com o gatilho tático
agora tecnicamente confirmado por duas gerações de dado (embora da mesma
sessão), mas ainda sem a confirmação de fundamentos (WASDE, NOPA) que a
revisão original pedia. Recomenda-se reabrir esta revisão formalmente assim
que o NOPA ou um novo WASDE de soja/óleo estiverem disponíveis, ou assim que a
sessão de segunda-feira (20/07) confirmar o ratio abaixo de 80% de forma
independente.

**A crush margin, mesmo revisada para baixo, segue no maior valor da janela de
cinco dias, e pela terceira sessão seguida em alta.** Fechou em 3,2285
USD/bushel (indicadores, sobre os closes revisados de 17/07: farelo 320,20 +
óleo 74,81 − soja 1.204,50) — abaixo do 3,2522 tratado ontem como definitivo,
mas ainda acima do 3,1211 de 16/07 (sequência completa: 3,0211 em 13/07 →
3,0193 em 14/07 → 3,0145 em 15/07 → 3,1211 em 16/07 → 3,2285 em 17/07,
revisado). O mecanismo estrutural segue intacto: quanto maior a crush margin,
maior o incentivo da esmagadora a processar soja a pleno vapor, e mais farelo
(subproduto obrigatório do esmagamento) entra no mercado.

**A trajetória projetada da ABIOVE (Associação Brasileira das Indústrias de
Óleos Vegetais, projeções mensais, sem alteração) segue sendo o pilar mais
sólido do argumento estrutural, porque não depende do preço do dia nem de
revisões de fechamento.** A exportação de farelo brasileiro projetada cai de
1.400 mil toneladas em agosto/2026 para 700 mil toneladas em dezembro/2026
(queda de 50% em 4 meses), enquanto a produção cai de forma bem mais suave
(2.285,06 → 1.659,04 mil toneladas no mesmo período, −27%) — menos farelo
saindo pelo porto, com produção caindo bem menos que a exportação, empurra o
volume excedente para o mercado interno de ração, pressionando o preço
doméstico.

**As praças físicas de farelo no Brasil (NAG, último dado 17/07/2026, sem
atualização hoje) seguem no mesmo patamar descrito ontem.** Mato Grosso/IMEA em
R$ 1.602,80/ton, Rondonópolis/MT estável em R$ 1.600,00/ton, Rio Grande do Sul
em R$ 1.640,00/ton. O prêmio de exportação em Paranaguá segue em +0,05
USD/short_ton (julho/26, NAG), agora **15 dias corridos sem qualquer
variação** desde 03/07/2026 — o intervalo cresce mais um dia, reforçando a
suspeita (já registrada em leituras anteriores) de que pode ser um dado de
fonte não atualizada, não um preço de mercado genuinamente parado (ver
Honestidade).

**O Índice de Sobra de Farelo (ISF) permanece em 80/100 (4 de 5 condições
estruturais)** (indicadores, recalculado hoje 18/07/2026, sem variação) —
inalterado desde pelo menos 01/07/2026, agora confirmado inclusive no fim de
semana sem pregão, reforçando que é um índice calculado sobre condições
estruturais (ABIOVE, crush, oferta), não sobre o fechamento do dia.

**Tratando `release-nopa-2026-07-18`:** o NOPA (National Oilseed Processors
Association, dado mensal de esmagamento americano) segue com `monthly_status`
em 0,0 bool — a mesma barreira de assinatura paga documentada desde meados de
junho, agora mais de um mês sem alternativa de dado primário sobre o
esmagamento americano. Sem nenhuma informação nova para interpretar hoje.

**O oil-meal spread (óleo menos farelo, por bushel), recalculado com os
números revisados, subiu ainda mais do que a leitura de ontem havia
registrado: 1,1847 USD/bu**, ante 0,8635 (16/07) — uma alta de +37,2% no dia
(maior que os +35,3% calculados ontem sobre o dado não revisado). Mede, de
outro ângulo, a mesma divergência farelo-fraco/óleo-forte que caracteriza a
sessão de sexta, e a revisão de hoje só acentua essa divergência.

**O COT de 14/07/2026, sem atualização, mantém o mesmo contraponto relevante
à tese bear já descrito ontem.** Managed money net long em farelo em +46.576
contratos (7,77% do open interest de 599.353), ante +18.722 contratos (3,14%
do OI de 595.447) em 07/07/2026 — mais que dobrou em uma semana. Como fração
do OI, ficou próximo do de soja (7,48%) e bem abaixo do de óleo (16,92%), e as
três pernas cresceram na mesma semana — leitura mais consistente com um fluxo
amplo de "comprar o complexo inteiro" do que com convicção específica dos
fundos contra a tese bear-farelo, mas ainda no campo do plausível, não do
confirmado (sem percentil histórico — ver Honestidade). Continua sendo o dado
mais direto disponível hoje contra uma posição vendida em farelo outright, sem
mudança frente a ontem.

**O forecast estatístico do farelo (18/07/2026)** segue com viés altista,
praticamente estável frente a ontem: central 7d = 327,18 USD/sht (bandas
314,36-340,01); central 30d = 352,56 USD/sht (bandas 326,01-379,12). O modelo
estatístico (que reage a momentum de preço recente, não a fundamentos) segue
na direção oposta à tese fundamentalista ABIOVE + ratio.

### O que invalida / risco para o farelo

- **A reabertura de segunda-feira trazer o ratio de volta acima de 80%** — a
  margem de hoje (0,25 ponto) é maior que a de ontem, mas ainda pequena o
  suficiente para uma sessão de fato nova reverter.
- **A tese estrutural ABIOVE não se confirmar no físico ao longo do 2S/26** —
  sem atualização de praças físicas desde 17/07, não há novo dado para testar
  isso hoje.
- **O COT de 21/07 (publicação ~24/07) mostrar os fundos continuando a
  aumentar o net long em farelo** — reforçaria o risco de squeeze numa posição
  vendida direcional.
- **NOPA seguir inacessível indefinidamente**, sem confirmação do esmagamento
  americano para os checkpoints D+90 (09/09/2026) e D+180 (08/12/2026).
- **O prêmio de exportação Paranaguá "congelado" há 15 dias ser, na verdade,
  um dado sem atualização de fonte** (ver Honestidade).

### Leitura operacional — farelo

A tese estrutural (ABIOVE, ISF 80/100, crush margin em novo topo pela terceira
sessão) segue sendo o pilar mais forte da leitura, e o gatilho tático (ratio
< 80%) saiu do fim de semana mais robusto, não mais frágil, depois da segunda
revisão dos dados de sexta. Ainda assim, sem uma sessão de pregão
genuinamente nova para confirmar de forma independente, e com o COT mostrando
fundos ampliando net long em farelo na mesma semana, a postura recomendada
segue sendo aguardar a confirmação de segunda-feira antes de tratar o
cruzamento como definitivamente robusto, dimensionando a posição
principalmente no pilar estrutural. Para quem prefere o veículo mais
defensável — o spread farelo/soja ou o crush completo, em vez de direcional
puro —, o argumento permanece o mais forte da leitura: a divergência relativa
entre as pernas (medida pelo oil-meal spread, +37,2% na revisão de hoje) não
depende de o ratio confirmar de forma limpa nos próximos pregões, e não fica
exposta ao risco de squeeze que o posicionamento crescente dos fundos em
farelo outright sugere.

---

## Óleo

**Viés: bull forte (mantido da leitura de ontem — a perna mais limpa do
complexo). Fechou em 74,81 cts/lb na sessão de 17/07/2026 (dado revisado hoje,
praticamente idêntico ao 74,82 tratado ontem como definitivo), subindo +3,29%
no dia (de 72,43 para 74,81, trata
`alerta-movimento_forte-oleo_cbot-2026-07-17`). O oil share subiu para 53,88%
(revisado para cima frente ao 53,82% de ontem — novo topo da janela ainda mais
alto) e o Índice de Suporte do Óleo (ISO) segue em 100/100.**

### O que sustenta a tese

**A vela de sexta-feira, a mais forte da série, praticamente não mudou na
revisão de hoje — ao contrário de farelo e do ratio.** Fechamento de 74,81
cts/lb (CBOT, sessão de 17/07/2026), abertura em 72,62 (praticamente na
mínima do dia, 72,43) e máxima de 75,44 — o preço subiu de forma consistente
ao longo da sessão, com o fechamento retendo 79% do movimento até a máxima
(idêntico ao calculado ontem). O volume de 32.629 contratos (dado que só
aparece na segunda geração do dump; a leitura de ontem citou 40.029 — mais
uma pequena divergência entre gerações, ver Honestidade) segue sendo uma
referência relevante de participação de mercado, mesmo que o valor exato
tenha oscilado entre as leituras.

**A curva forward, sem pregão novo, mantém exatamente a mesma backwardation
descrita ontem**: Agosto/26 (Q26, spot) 74,81 → Setembro/26 (U26) 73,93
(−0,88, −1,18%) → Outubro/26 (V26) 73,02 (−0,91, −1,23%) → Dezembro/26 (Z26)
72,43 (−0,59, −0,81%) → Janeiro/27 (F27) 72,07 (−0,36, −0,50%) — uma queda
total de −2,74 cts/lb (−3,66%) de agosto a janeiro/27. A assinatura de rali
concentrado no vencimento mais próximo (em vez de re-precificação estrutural
de toda a curva) segue intacta.

**A margem de biodiesel americano, na segunda revisão de hoje, corrigiu
substancialmente para cima — o dado mais relevante desta leitura para a tese
do óleo.** Fechou revisada em 0,8189 USD/galão (indicadores: receita 7,2296 =
heating oil 4,0646 + 1,5×RIN 2,11; custo 6,4107 = óleo 5,6107 + industrial
0,80), ante os 0,7029 tratados ontem como definitivos — uma correção de
+16,5%. A causa raiz: o heating oil de 17/07 (principal componente de receita
do biodiesel, junto com o RIN D4) foi revisado de 3,9494 (queda de −2,0% no
dia, como a leitura de ontem descreveu) para 4,0646 (**alta** de +0,84% no dia
frente ao close de 16/07) — uma reversão completa de sinal no insumo de
receita, não apenas de magnitude. Com a correção, a margem de sexta-feira
deixa de ser "a menor da janela de cinco dias" (como ontem foi descrito) e
passa a ser a terceira menor: 0,7271 (13/07) → 0,9493 (14/07) → 0,8443
(15/07) → 0,9635 (16/07) → 0,8189 (17/07, revisado) — ainda uma queda de
−15,0% frente a 16/07 (bem menor que os −27,0% calculados ontem), mas não mais
o piso da série. A tensão de mecanismo permanece válida e vale repetir: a
mesma alta do óleo que é bullish para o papel CBOT é, ao mesmo tempo, bearish
para a margem do biodiesel (o óleo é o principal insumo de custo do processo)
— só que a magnitude dessa tensão, com o dado corrigido, é menor do que se
pensava ontem.

**O Índice de Suporte do Óleo (ISO) permanece em 100/100 (5 de 5 condições)**
(indicadores, recalculado hoje 18/07/2026, sem variação) — inalterado desde
pelo menos 01/07/2026, confirmado inclusive no fim de semana sem pregão. Com a
correção da margem de biodiesel para um valor menos extremo, o argumento de
que o ISO poderia estar sob pressão de uma margem "no piso da janela" perde
força — o quadro é de suporte estrutural mais confortável do que a leitura de
ontem sugeria.

**O oil share, recalculado com os números revisados, subiu ainda mais do que
a leitura de ontem registrou: 53,88%** (indicadores, 17/07/2026, revisado),
ante os 53,82% tratados ontem como topo da janela — um novo recorde ainda mais
alto, confirmando que o óleo continua sendo o motor de valor do crush.
Coerente com o oil-meal spread (+37,2% na revisão de hoje, ver Spreads).

**O COT de 14/07/2026, sem atualização, mantém o óleo como a perna mais
"concorrida" das três em termos de posicionamento — sem mudança frente a
ontem.** Managed money net long em +107.945 contratos (16,92% do open
interest de 638.102), ante +84.919 contratos (13,22% do OI de 642.514) em
07/07/2026 — um aumento de +23.026 contratos (+27,1%) na semana, o maior em
termos absolutos das três pernas, com o OI total caindo ligeiramente (−0,69%)
na mesma semana, sugerindo parte do aumento vindo de short covering. Com o
net long em ~17% do OI (o mais alto das três pernas, sem histórico de
percentil para calibrar — ver Honestidade), a posição comprada no óleo segue
sendo a mais crowded do complexo.

**O forecast estatístico do óleo (18/07/2026)** mantém o viés altista, quase
idêntico ao de ontem: central 7d = 75,82 cts/lb (bandas 71,01-80,62); central
30d = 80,37 cts/lb (bandas 70,42-90,32). É a terceira leitura seguida em que
as seis bandas de forecast do sistema fecham simultaneamente em viés altista.

### O que invalida / risco para o óleo

- **Um fechamento abaixo de 73,02 (o vencimento de outubro na curva de hoje)
  na reabertura de segunda-feira** reabriria o cenário de correção.
- **A margem de biodiesel, mesmo corrigida para cima, seguir historicamente
  comprimida frente ao início do mês** — 0,8189 USD/gal ainda é a terceira
  menor da janela de cinco dias, não uma recuperação plena.
- **O posicionamento dos fundos (net long em 16,92% do OI, o mais concorrido
  das três pernas) sofrer uma reversão** quando o próximo COT chegar
  (~24/07).
- **MPOB seguir inacessível** — impossível avaliar o efeito do El Niño ou das
  restrições/levy indonésias (PMK 9/2026, Danantara — ver Lente fiscal) sobre
  o prêmio de substituição via palma. Hoje é o nono dia consecutivo (pelo
  menos) sem números extraídos.

### Leitura operacional — óleo

O óleo segue sendo a tese mais forte e mais bem sustentada do complexo, e a
segunda revisão dos dados de sexta-feira, ao corrigir a margem de biodiesel
para cima, **remove** uma das duas nuances de cautela que a leitura de ontem
havia sinalizado — o rali do óleo aperta a economia do biodiesel menos do que
se pensava ontem. A outra nuance (posicionamento dos fundos já concorrido,
16,92% do OI) permanece inalterada. Para quem opera exposição relativa dentro
do crush, o oil-meal spread (+37,2% na revisão de hoje) segue sendo o veículo
mais direto para capturar a divergência entre as duas pernas do complexo. Para
quem opera direcional puro em óleo, a ausência de pregão hoje é uma pausa
natural para reavaliar o dimensionamento antes da reabertura de segunda-feira,
que trará tanto o teste real da vela de sexta quanto, potencialmente, reação a
qualquer notícia de fim de semana sobre biodiesel, RFS ou palma.

---

## Spreads e crush — leitura de complexo

### Crush margin: 3,2285 USD/bu — maior valor da janela, pela terceira sessão seguida, mesmo após revisão para baixo

A crush segue em alta pela terceira sessão consecutiva, mesmo que a segunda
geração do dump tenha revisado o valor de sexta-feira levemente para baixo
(de 3,2522 para 3,2285). Sequência completa: 3,0211 (13/07) → 3,0193 (14/07)
→ 3,0145 (15/07) → 3,1211 (16/07) → 3,2285 (17/07, revisado). O incentivo de
esmagamento a pleno vapor segue se fortalecendo de forma consistente,
alimentando o mecanismo estrutural ABIOVE independentemente de qual perna do
complexo está subindo ou caindo no dia.

### Ratio Far/Soj: 79,75% — segunda revisão aprofunda o cruzamento abaixo de 80%

O achado tático central desta leitura de sábado: a segunda geração dos dados
de sexta-feira moveu o ratio de 79,98% (ontem) para 79,75% (hoje) — mais
distante do limiar de 80%, não menos. Sequência completa: 79,52% (13/07) →
79,83% (14/07) → 79,58% (15/07) → 81,06% (16/07) → **79,75% (17/07,
revisado)**. Trata `ratio-zona-2026-07-17` e a revisão programada
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` (agora 30
dias vencida, ver seção Farelo para o detalhamento completo das três
perguntas da revisão original). Ainda assim, sem uma sessão de pregão nova e
independente (mercado fechado no fim de semana), a recomendação de aguardar
confirmação de uma sessão genuinamente nova antes de tratar o cruzamento como
robusto permanece — a diferença é que a base de partida ficou mais sólida.

### Oil share: 53,88% — novo topo da janela, revisado ainda mais alto

Subiu de 52,86% (16/07) para 53,88% na revisão de hoje da sessão de 17/07
(ante 53,82% tratado ontem como definitivo) — o óleo capturando a maior
fatia do valor do crush em toda a janela visível, com a revisão reforçando,
não enfraquecendo, esse recorde.

### Oil-meal spread: 1,1847 USD/bu — maior alta de um dia da série, revisada ainda mais alta

Subiu de 0,8635 (16/07) para 1,1847 USD/bu na revisão de hoje (ante 1,1682
tratado ontem como definitivo) — uma alta de +37,2% no dia (maior que os
+35,3% calculados ontem). Mede a mesma divergência farelo-fraco/óleo-forte, e
a revisão de hoje só acentua essa divergência.

### Margem de biodiesel: 0,8189 USD/gal — revisão para cima muda a leitura de "piso da janela" para "terceiro pior valor"

O achado de segundo plano mais importante desta leitura: a margem de
biodiesel de sexta-feira, revisada hoje, subiu +16,5% frente ao valor tratado
ontem como definitivo (de 0,7029 para 0,8189), porque o heating oil de
sexta-feira foi revisado de queda para alta no dia. Isso não muda o viés bull
do óleo CBOT, mas reduz a magnitude da tensão entre "óleo subindo" e "margem
de biodiesel comprimindo" que a leitura de ontem havia destacado como ponto
de atenção.

### COT: sem atualização — óleo segue disparado o mais concorrido

O dado de 14/07/2026 (trata `release-cftc_cot-2026-07-14`, já tratado na
leitura de ontem) segue sem atualização. Como fração do open interest, o óleo
é disparado o mais concorrido (16,92% vs 7,77% do farelo e 7,48% da soja) —
o posicionamento confirma o bull-óleo desta leitura, mas também é o maior
fator de risco de reversão abrupta.

### ISF em 80/100, ISO em 100/100 — recalculados hoje, sem variação mesmo no fim de semana

O Índice de Sobra de Farelo (ISF, 4/5 condições) e o Índice de Suporte do
Óleo (ISO, 5/5 condições) foram recalculados hoje (18/07/2026, sábado, sem
pregão) e permanecem inalterados — a prova mais direta de que são índices
calculados sobre condições estruturais (ABIOVE, crush, oferta), não sobre o
fechamento pontual de uma sessão.

### O que os índices dizem juntos em 18/07/2026

ISF 80/100 + ISO 100/100 (ambos estáveis mesmo sem pregão) + ratio Far/Soj
mais solidamente abaixo de 80% após a segunda revisão + oil share em novo
topo (revisado ainda mais alto, 53,88%) + crush margin em novo topo pela
terceira sessão seguida (3,2285) + oil-meal spread com a maior alta de um dia
da série (revisada para +37,2%) + margem de biodiesel corrigida para cima
(reduzindo uma fonte de tensão na tese do óleo) + COT mostrando fundos
comprando as três pernas, com óleo disparado o mais concorrido — formam um
quadro ainda mais coerente do que ontem: complexo esmagando a pleno vapor,
com o mercado precificando farelo e óleo de forma cada vez mais divergente, e
a segunda rodada de revisão de dados reforçando, em vez de contradizer, essa
leitura em praticamente todos os pontos.

---

## Lente fiscal e regulatória BR

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L) — a
vigência formal (`vigencia_ate` 11/07/2026) venceu há 7 dias, e o monitor
tributário segue sem qualquer atualização de status** (system/tributario_watch.toml,
evento MP-1358-2026, `atualizado_em` 2026-06-05, status ainda "tramitacao").
Enquanto o combustível fóssil segue subsidiado, a competitividade relativa do
biodiesel dentro do mix B15 mandatório fica pressionada — e a correção de
hoje na margem de biodiesel americana (revisada de 0,7029 para 0,8189
USD/gal) não muda esse quadro regulatório BR, que é um vetor independente do
proxy americano.

**Isenção PIS/Cofins biodiesel — vencimento em 31/07/2026, agora a 13
dias.** Sem sinalização pública de renovação até hoje (evento
PISCOFINS-BIODIESEL-ISENCAO, `atualizado_em` 2026-06-05, sem mudança). Com a
margem de biodiesel americana corrigida para um valor menos extremo (0,8189,
não mais o piso da janela), o cenário de "duplo headwind" (custo tributário +
margem apertada) descrito ontem fica um pouco menos severo na perna
econômica — mas o vetor tributário BR, por si só, segue intacto e é o mais
urgente a monitorar nas próximas duas semanas.

**B16 — sem data, travado em B15.** Sem mudança de status (evento
B16-CNPE-2026, `atualizado_em` 2026-06-05, status "adiado"). Testes técnicos
do FNDCT com resultado esperado ~nov/2026 — realista só fim de 2026/início de
2027.

**MP 1.363/2026 (subsídio ao diesel fóssil, R$ 1,12/L) — em vigor até
31/12/2026.** Sem alteração. Bearish estrutural persistente para a demanda
incremental de óleo de soja no mercado doméstico brasileiro.

**STJ REsp 2.165.276/2026 — crédito PIS/Cofins para esmagadoras.** Sem
alteração. Bullish para soja/óleo (alívio de custo de entrada para
biodiesel) e, por extensão, incentivo a mais esmagamento — coerente com a
crush margin em novo topo pela terceira sessão seguida.

**Vetores dos EUA e Indonésia, revisitados (sem mudança de status,
`atualizado_em` 2026-06-05 em todos):** EPA-RFS-2026-2027 (volumes recordes
de biocombustível, BBD 8,86→9,07 bi RINs, sustentando estruturalmente o RIN
D4 e o óleo CBOT — vale notar que o RIN D4 usado no cálculo da margem de
biodiesel segue fixo em 2,11 USD/RIN, ver Honestidade); 45Z-CLEAN-FUEL (regra
proposta que tiraria insumo importado da elegibilidade ao crédito,
favorecendo óleo de soja doméstico americano); DANANTARA-INDONESIA
(centralização estatal da exportação de palma, assunção plena da cadeia alvo
em 01/09/2026 — risco de menor saldo exportável de palma, suporte ao óleo de
soja por substituição); INDONESIA-B50 (retórica agressiva mas quota flat —
provável B45 em 2026, B50 pleno só 2027-28); INDONESIA-LEVY-PMK9 (imposto de
exportação de CPO até 12,5% desde 01/03, encarecendo palma e favorecendo
substituição por óleo de soja). Todos esses vetores seguem, em conjunto, num
sentido estruturalmente bullish para o óleo de soja via substituição de
palma — mas seguem inverificáveis pelo lado dos dados de mercado (MPOB
inacessível há pelo menos 9 dias, ver Honestidade).

**O monitor tributário como um todo está há 43 dias sem qualquer
atualização** (`atualizado_em` 2026-06-05 em todos os dez eventos
rastreados) — o intervalo segue crescendo em um momento em que dois vetores
(MP 1.358 e a isenção PIS/Cofins) têm datas de vencimento formal já vencida
ou a apenas 13 dias. Vale sinalizar este ponto como prioridade de manutenção
do sistema, independentemente da leitura de preço.

---

## Riscos e eventos próximos

**A reabertura de segunda-feira (20/07) é o próximo teste real de todas as
teses desta leitura.** Sem pregão neste fim de semana, tudo o que esta
leitura pôde fazer foi confirmar a solidez dos números de sexta-feira através
de uma segunda rodada de revisão — o teste genuíno (nova oferta e demanda,
reação a notícias de fim de semana) só vem com a próxima sessão.

**O USDA Crop Progress de segunda-feira (20/07, dado "as of" 19/07) atualiza
pela primeira vez em 8 dias a condição da lavoura americana** (última leitura
12/07: 65% bom-ou-melhor). É o evento fundamentalista mais concreto e datado
da próxima semana.

**COT (CFTC) — dado de 14/07/2026 segue sendo o mais recente, ainda não
cobre a semana do rompimento.** O próximo dado (referência ~21/07,
publicação normal ~24/07) é o que vai mostrar se os fundos continuaram
comprando soja e óleo, e se começaram a reduzir farelo, durante a semana em
que o ratio cruzou abaixo de 80%.

**O padrão de revisão dump-a-dump se repetiu pela quarta vez nesta série de
leituras — desta vez sem inverter nenhum sinal tático, mas com magnitude
suficiente para mudar a leitura da margem de biodiesel (de "pior da janela"
para "terceira pior") e reforçar o cruzamento do ratio Far/Soj.** Recomenda-se,
mais uma vez, tratar qualquer número do dia da própria publicação — mesmo em
dias sem pregão novo, como hoje — como sujeito a nova revisão até uma sessão
genuinamente independente confirmar.

**Desfecho da MP 1.358/2026 — vigência formal encerrada há 7 dias, sem
confirmação.** Monitorar deliberação da comissão mista e qualquer decreto de
prorrogação.

**Isenção PIS/Cofins biodiesel — vencimento 31/07/2026 (13 dias).** Sem
sinalização de renovação até agora.

**NOPA — segue inacessível** (fila `release-nopa-2026-07-18` tratada aqui,
sem dado interpretável), sem crush americano confirmado por fonte primária.

**MPOB — sem números de palma extraídos há pelo menos 9 dias**, mantendo
cego o efeito do El Niño e dos vetores regulatórios indonésios (Danantara,
B50, levy PMK 9) sobre o prêmio de substituição do óleo de soja.

**Checkpoints futuros da tese estrutural do farelo (ABIOVE)** — D+90 em
09/09/2026 e D+180 em 08/12/2026 (insight
[[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]) — a revisão D+7,
tratada nesta leitura com 30 dias de atraso exato, aponta confirmação tática
mais sólida (ratio < 80% em duas gerações de dado da mesma sessão) mas ainda
sem confirmação de fundamentos (WASDE, NOPA); os checkpoints estruturais
seguem o critério de mais alta confiança para julgar a tese ao longo do
tempo.

---

## Honestidade

O que não foi possível validar neste briefing de 18/07/2026, onde a confiança
é baixa ou há lacunas materiais:

**1. Hoje é sábado, sem pregão novo — tudo o que esta leitura pôde fazer foi
reanalisar a sessão de sexta-feira (17/07) através de uma segunda geração de
dados revisados.** Isso significa que nenhuma das teses foi testada por uma
sessão de mercado genuinamente independente hoje. A confirmação real só vem
com a reabertura de segunda-feira (20/07).

**2. O ratio Far/Soj de 17/07 foi revisado de 79,98% (leitura de ontem) para
79,75% (hoje) — uma mudança de 0,23 ponto percentual entre duas gerações do
dump para a MESMA sessão.** Embora a direção da revisão favoreça a tese bear
tática do farelo (mais distante do limiar de 80%, não menos), o próprio fato
de haver uma segunda revisão material da mesma sessão, quatro dias depois de
o padrão já ter sido documentado três vezes nesta série, reforça que
qualquer número do dia da publicação — mesmo em dia sem pregão, como hoje —
não deve ser tratado como definitivo até uma sessão nova e independente
confirmar.

**3. A margem de biodiesel americano de 17/07 foi revisada de 0,7029 USD/gal
(leitura de ontem) para 0,8189 USD/gal (hoje) — uma correção de +16,5%, com a
causa raiz sendo uma reversão de sinal no heating oil do mesmo dia (de −2,0%
para +0,84% no dia).** Isso muda materialmente a leitura de "margem no piso
da janela de 5 dias" (descrição de ontem) para "terceira menor margem da
janela" (descrição de hoje) — um exemplo claro de como uma revisão em um
componente aparentemente secundário (heating oil) pode alterar a
interpretação de um indicador derivado (margem de biodiesel) de forma
proporcionalmente maior que a revisão do componente em si.

**4. O volume da sessão de óleo de 17/07 também mudou entre gerações do
dump — 40.029 contratos na leitura de ontem, 32.629 contratos na leitura de
hoje** — sem que o dump traga uma explicação para essa diferença. Como o
volume foi usado ontem como argumento de "maior confiança de que o movimento
é real", essa divergência reduz um pouco a força desse argumento específico,
ainda que não mude a leitura da vela em si (abertura, mínima, máxima e
fechamento do óleo permaneceram praticamente idênticos entre as duas
gerações).

**5. O COT (CFTC) segue com dado de referência 14/07/2026, sem atualização
frente à leitura de ontem.** A semana do rompimento da soja e do
salto do óleo ainda não está refletida no posicionamento dos fundos — o
próximo relatório (dado esperado ~21/07, publicação ~24/07) é que vai testar
se a compra de dinheiro novo em soja e óleo continuou durante essa semana.

**6. Percentis históricos de COT não calculados** — os números de 14/07/2026
são lidos apenas em nível absoluto e como fração do open interest corrente
(soja 7,48%, farelo 7,77%, óleo 16,92%), sem série histórica completa para
calibrar se algum desses níveis está objetivamente "esticado" no sentido
histórico.

**7. O prêmio de exportação de farelo em Paranaguá (+0,05 USD/sht) e o de
óleo (+0,08 cts/lb) estão no mesmo valor exato desde pelo menos 03/07/2026**
(NAG, agora 15 dias corridos sem variação de nenhum centavo) — não é
possível distinguir se isso reflete um mercado de exportação genuinamente
parado ou um valor que não está sendo atualizado de fato na fonte.

**8. O prêmio físico de Paranaguá sobre a paridade teórica comprimiu por três
leituras seguidas (4,68% → 3,81% → 3,78%)** — a sequência já é longa o
suficiente para começar a considerar uma tendência real, mas ainda sem um
mecanismo causal identificado no briefing (poderia ser atraso do físico em
acompanhar o papel, poderia ser ruído de PTAX, poderia ser outra coisa) — não
tratar como confirmado sem mais pontos de dado.

**9. A manchete sobre o produtor gaúcho endividado (Canal Rural, 18/07/2026)
é anedótica — uma única reportagem, sem dado quantitativo de área, safra ou
valor de dívida capturado no headline do dump, e sem contexto sobre se é
representativa de uma tendência mais ampla entre produtores do Rio Grande do
Sul ou do Brasil.** Foi registrada nesta leitura como sinal de fundo a
monitorar, explicitamente NÃO como driver de preço — tratar como tal seria
inventar peso quantitativo que a fonte não sustenta.

**10. O WASDE segue cobrindo apenas farelo (Argentina, Brasil, China
parcial), sem nenhum dado de soja em grão ou óleo de soja, em qualquer
geografia, e sem nenhum dado dos Estados Unidos** — sem atualização desde
10/07/2026. A pergunta central sobre "oferta grande de soja" segue sem canal
de resposta interno.

**11. NOPA (fila `release-nopa-2026-07-18`) segue com `monthly_status` em
0,0 bool** — mesma barreira de assinatura paga documentada desde meados de
junho, agora com mais de um mês sem alternativa de dado primário sobre o
esmagamento americano.

**12. Palma malaia (MPOB) segue sem números extraídos** (18/07/2026, mesmo
texto de HTML de 3.439 caracteres sem valores, streak de pelo menos 9 dias
consecutivos) — impossível avaliar o efeito do El Niño ou dos vetores
regulatórios indonésios (Danantara, B50, levy PMK 9 — ver Lente fiscal) sobre
o prêmio de substituição do óleo de soja.

**13. Clima INMET (BR) não foi usado como driver desta leitura.** Julho é
entressafra da soja brasileira (colheita concluída, plantio só em outubro) —
sem relevância direta para a tese de preço neste momento do calendário
agrícola, embora o El Niño Advisory (NOAA CPC, inalterado desde pelo menos
03/07/2026) permaneça relevante para a expectativa da safra de plantio de
outubro/26 e para o clima do Sudeste Asiático (palma).

**14. BCBA Argentina — sem relatórios de esmagamento/exportação acessíveis
via scraper** (page_fetched=1,0 mas sem links de relatório, 18/07/2026, sem
mudança).

**15. RIN D4 como parâmetro fixo (2,11 USD/RIN) segue sendo uma fonte
relevante de incerteza do modelo de biodiesel**, sem novo dado hoje — a
margem revisada de hoje (0,8189) foi recalculada com esse valor fixo; se o
RIN de mercado estiver, na realidade, diferente de 2,11, tanto a margem
quanto o ISO podem estar mal calibrados, independentemente da correção
documentada nesta leitura.

*Nenhum número foi inventado ou estimado além do que consta no briefing de
18/07/2026 e nos insights anteriores referenciados. A contribuição central
desta leitura foi identificar, através de uma segunda geração de dados para a
mesma sessão de sexta-feira (17/07), que o cruzamento do ratio Far/Soj abaixo
de 80% ficou mais sólido (não menos) e que a margem de biodiesel americana,
antes descrita como "no piso da janela de 5 dias", na verdade se recuperou
parcialmente por conta de uma reversão de sinal no heating oil — dois ajustes
que reforçam a leitura de ontem em vez de contradizê-la, mas que reafirmam,
pela quarta vez nesta série, que nenhum número do dia da publicação — mesmo
em um dia sem pregão, como hoje — deve ser tratado como definitivo até uma
sessão de mercado genuinamente nova confirmar.*
