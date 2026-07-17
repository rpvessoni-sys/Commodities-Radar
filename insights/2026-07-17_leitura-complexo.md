---
data: 2026-07-17
titulo: "O fechamento definitivo de hoje (volumes reais de 27-40 mil contratos, contra os 1-3 mil da leitura intraday) inverte por completo o quadro: a soja não rompeu suporte, subiu 0,75% e fechou em 1.204,00 — 2,03% ACIMA da resistência 1.180,00 (trata `alerta-quebra_resistencia-soja_cbot-2026-07-17`), no mesmo dia em que a USDA anunciou 3 grandes vendas de exportação de soja; o óleo disparou +3,30% para 74,82 cts/lb (trata `alerta-movimento_forte-oleo_cbot-2026-07-17`); o farelo ficou para trás e o ratio Far/Soj fechou, pela primeira vez com dado definitivo, abaixo de 80% (79,98%, trata `ratio-zona-2026-07-17`) — mas por uma margem de apenas 0,02 ponto percentual, distância bem menor que as revisões já vistas nesta série; e o COT que faltava ontem finalmente chegou (dado de 14/07, trata `release-cftc_cot-2026-07-14`), mostrando os fundos ampliando net long em soja, farelo E óleo simultaneamente na mesma semana"
tags: [complexo, auto-claude]
fontes:
  - CBOT CME (ZSQ26/ZMQ26/ZLQ26 + curva forward completa + HO=F) — sessão de 2026-07-17, fechamento definitivo (volumes 27.197-40.029 contratos, padrão próximo do normal — ver Honestidade sobre a diferença frente à leitura intraday do mesmo dia)
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, ISF/ISO, paridade BR) — 2026-07-17, série de 13 a 17/07
  - BCB PTAX — 2026-07-17 (USD/BRL 5,1176), dado do PRÓPRIO dia, sem a defasagem de 1 dia que caracterizou leituras anteriores
  - CEPEA/ESALQ Paranaguá e Paraná interior via NAG — 2026-07-17 (suporte Paranaguá R$ 141,02/saca, Paraná interior R$ 134,11/saca), também dado do próprio dia
  - NAG Físico BR (farelo MT/IMEA, RS, Rondonópolis; prêmios export PGUA farelo/óleo) — último dado 2026-07-17
  - CFTC COT Managed Money — NOVO dado, referência 2026-07-14 (primeira atualização em 10 dias; trata `release-cftc_cot-2026-07-14`)
  - USDA Crop Progress — ainda 2026-07-12 (65% bom-ou-melhor), sem atualização; próximo relatório normal ~2026-07-20 (segunda-feira)
  - USDA WASDE — ainda 2026-07-10 (só farelo Argentina/Brasil/China parcial), sem publicação nova
  - NOPA — 2026-07-17, `monthly_status` continua inacessível (paywall), fila `release-nopa-2026-07-17`
  - ABIOVE projeções mensais — balanços ago-dez/2026 (farelo/óleo/soja), sem alteração frente às leituras anteriores
  - NOAA CPC ENSO — 2026-07-17 (El Niño Advisory, sem mudança)
  - MPOB — 2026-07-17 (parser sem números extraídos, streak de ~2 semanas)
  - BCBA — 2026-07-17 (acessível, sem links de relatório detectados)
  - Farm Progress / Notícias Agrícolas RSS — 2026-07-17 (160 itens lidos, 6 mantidos; manchete "USDA exports – 3 large soybean sales announced, July 17, 2026", Farm Progress)
  - Forecasts estatísticos internos — 2026-07-17 (as seis bandas — 3 commodities × 2 horizontes — seguem simultaneamente em viés altista, segunda leitura seguida nessa condição, com spot já refletindo o fechamento definitivo)
  - system/tributario_watch.toml — MP-1358-2026 (vigência formal encerrada há 6 dias, status ainda "tramitação"), PISCOFINS-BIODIESEL-ISENCAO (vence em 14 dias), MP-1363-2026, STJ-RESP-2165276, B16-CNPE-2026, EPA-RFS-2026-2027, 45Z-CLEAN-FUEL, DANANTARA-INDONESIA, INDONESIA-B50, INDONESIA-LEVY-PMK9 — todos `atualizado_em` 2026-06-05 (42 dias sem atualização do monitor)
  - Cruza com [[2026-07-16_leitura-complexo]], [[2026-07-15_leitura-complexo]], [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (checkpoint D+7, tratado abaixo — agora 29 dias vencido), [[2026-05-26_subvencao-fossil-aperta-biodiesel]], [[2026-05-26_pis-cofins-biodiesel-explica-mercado-fisico-fraco]]
status: ativa
vies: [bull-soja, bear-farelo, bull-oleo_soja]
---

> **Nota de proveniência:** esta leitura substitui uma versão anterior de 17/07/2026
> publicada mais cedo no dia, construída sobre dados intraday de volume muito baixo
> (soja 2.182, farelo 1.087, óleo 3.244 contratos) que geraram uma leitura tática
> **oposta** à que os dados definitivos de hoje sustentam — naquela versão a soja
> aparecia rompendo suporte para baixo; nos dados que fecharam o dia, a soja subiu e
> fechou acima da resistência. O item 1 da seção Honestidade detalha exatamente o
> que mudou e por quê isso deve pesar em qualquer leitura de vela do dia da
> publicação daqui em diante.

## Visão geral

O complexo soja é uma fábrica com uma única matéria-prima (a soja em grão) e dois
produtos de saída em proporção fixa por bushel esmagado: o **farelo** (fração
proteica, ~78% da massa, vira ração animal) e o **óleo degomado** (fração de
gordura, ~18-20% da massa, vira óleo de cozinha e biodiesel). Quem decide o ritmo
de esmagamento é a esmagadora, olhando a **crush margin** (valor de farelo + óleo
por bushel, menos o custo daquele bushel de soja, medido na CBOT — Chicago Board
of Trade) e o **oil share** (fração desse valor capturada pelo óleo). Quando o
oil share sobe, o óleo "paga o crush" e o farelo vira, cada vez mais, um
subproduto que a esmagadora aceita vender barato só para liberar o óleo — é
exatamente esse mecanismo que está por trás do **ratio Far/Soj** (preço do
farelo dividido pelo preço da soja, normalizado): quando ele cai abaixo de 80%,
o farelo está historicamente "abundante" frente à soja: sobra farelo, o spread
tende a comprimir. Hoje, sexta-feira 17/07/2026, a crush margin fechou em 3,2522
USD/bushel (indicadores, farelo 321,00 + óleo 74,82 − soja 1.204,00) — o **maior
valor de toda a janela de 5 dias visível neste dump** (3,0211 em 13/07 → 3,0193
em 14/07 → 3,0145 em 15/07 → 3,1211 em 16/07 → 3,2522 hoje) — a esmagadora segue
com forte e crescente incentivo a rodar a pleno vapor.

**O que mudou hoje, antes de qualquer tese de preço, foi a confirmação — pela
terceira vez em três dias — de que os números capturados no MOMENTO da
publicação do dump não são os números finais da sessão, e desta vez a diferença
inverteu o sinal da tese, não só a magnitude.** Uma primeira geração da leitura
de hoje, feita sobre volumes de 1.087 a 3.244 contratos (uma fração óbvia do
normal), descreveu a soja rompendo a mínima de uma consolidação de quatro dias,
fechando em 1.187,75 com uma vela sem qualquer recuperação. Os dados que
efetivamente fecharam o pregão (volumes de 27.197 a 40.029 contratos, a ordem
de grandeza normal) contam uma história diferente: a soja abriu em 1.195,00
(exatamente no fechamento revisado de ontem, sem gap), caiu até uma mínima de
1.186,75 — quase idêntica à "mínima" que a leitura preliminar já havia
capturado, sugerindo que aquela leitura pegou o fundo do movimento, não o
fechamento — e a partir daí subiu com força até uma máxima de 1.205,25,
fechando em 1.204,00, a 93% do topo do range do dia. Ou seja: o dia teve, sim,
um movimento de queda pela manhã (que a leitura intraday capturou), mas a
sessão inteira foi de recuperação em V, fechando a soja **acima** da resistência
de 1.180,00 (trata `alerta-quebra_resistencia-soja_cbot-2026-07-17`), com uma
folga de 2,03% — não a 0,66% "quase rompendo" que a leitura intraday registrou.

**O óleo teve o dia mais forte do complexo, com dado que já era robusto mesmo na
leitura intraday e ficou ainda mais forte no fechamento**: subiu +3,30% (de
72,43 para 74,82 cts/lb, trata `alerta-movimento_forte-oleo_cbot-2026-07-17`),
fechando a 79% do topo do range, com volume de 40.029 contratos — o mais
próximo do "normal" das três pernas hoje, o que dá a maior confiança de que
esse movimento é real, não um artefato de captura parcial. O **farelo**, ao
contrário, ficou para trás: fechou em 321,00, caindo 0,59% no dia, e mesmo
recuperando 57% do range desde a mínima (318,50), foi a perna mais fraca da
sessão. Essa divergência empurrou o ratio Far/Soj para 79,98% (farelo 321,00 ÷
soja 1.204,00, base normalizada) — **abaixo de 80% pela primeira vez com dado
que o próprio sistema está tratando como definitivo**, cruzando o limiar que
sustenta a tese estrutural de compressão do spread desde 11/06/2026. Mas a
margem é mínima: 0,02 ponto percentual, uma distância menor do que qualquer uma
das revisões dump-a-dump já documentadas nesta série (a de ontem, sozinha, foi
de 1,28 ponto). Trata `ratio-zona-2026-07-17`. Some a isso a chegada do COT
(Commitments of Traders, o raio-x semanal de posicionamento dos fundos
publicado pela CFTC) referente a 14/07/2026 — que estava faltando na leitura de
ontem — mostrando os fundos ("managed money") ampliando a posição comprada
líquida em soja, farelo E óleo na mesma semana (trata
`release-cftc_cot-2026-07-14`). **Leitura de uma linha:** o pivô do complexo
hoje é a confirmação de que o fechamento oficial da sessão pode ser
radicalmente diferente da leitura feita no momento da publicação — com essa
ressalva no centro, a tese de hoje é bull tático em soja (rompimento de
resistência com volume e notícia de demanda no mesmo dia), bull reforçado em
óleo (a perna mais limpa e com o volume mais normal das três), e bear
estrutural com tático apenas marginalmente confirmado em farelo — convicção
moderada-alta em soja e óleo, moderada em farelo (pela fragilidade da margem do
cruzamento), com a confirmação de amanhã sobre se os números de hoje se mantêm
como o próximo teste real de tudo isso.

---

## Soja

**Viés: bull tático (convicção moderada-alta, upgrade de bear tático na leitura
intraday de hoje) — fechou em 1.204,00 cts/bu (17/07/2026), 2,03% acima da
resistência 1.180,00, com uma vela de recuperação em V: abriu em 1.195,00, caiu
até 1.186,75 (mínima do dia), e subiu até 1.205,25 (máxima), fechando a 93% do
topo do range de 18,50 pontos. Trata `alerta-quebra_resistencia-soja_cbot-2026-07-17`.**

### O que sustenta a tese

**A vela de hoje é, na verdade, a mais forte da semana — o oposto exato do que
a leitura intraday sugeriu.** Fechamento de 1.204,00 cts/bu (CBOT, 17/07/2026),
abertura em 1.195,00 (idêntica ao fechamento revisado de ontem, sem gap),
mínima de 1.186,75 e máxima de 1.205,25. A distância entre o fechamento e a
máxima é de apenas 1,25 ponto sobre um range de 18,50 — ou seja, 93% do
movimento do dia terminou perto do topo, o inverso do padrão "vela sem pavio
que fecha embaixo" registrado tanto ontem quanto na leitura intraday de hoje.
Isso muda a leitura técnica por completo: em vez de romper a mínima da
consolidação de quatro dias (1.192,75-1.205,50 desde 13/07), a soja **testou a
região baixa dessa consolidação pela manhã e reverteu com força**, fechando
dentro da parte alta da própria banda — a máxima de hoje (1.205,25) praticamente
retesta o teto do range dos últimos cinco pregões (1.205,50, de 15/07).

**Olhando os cinco últimos fechamentos em sequência — 1.196,75 (13/07) →
1.192,75 (14/07) → 1.202,25 (15/07) → 1.195,00 (16/07, revisado) → 1.204,00
(hoje)** — o padrão volta a ser de consolidação lateral com viés de alta, não
de rompimento de baixa: o fechamento de hoje é o segundo mais alto da janela,
atrás apenas do de 15/07. O rompimento de alta de 06-07/07 (que levou o preço
de ~1.180,00 para a faixa de 1.190-1.205) permanece integralmente válido, e a
distância de segurança até o suporte estrutural de 1.180,00 **subiu** de 1,65%
(fechamento de 16/07) para 2,03% hoje — o oposto da compressão que a leitura
intraday havia descrito.

**A manchete de notícias de hoje é, muito provavelmente, o gatilho mais direto
do movimento.** Farm Progress noticiou em 17/07/2026: "USDA exports – 3 large
soybean sales announced" (farmprogress.com/marketing/flash-sales). O mecanismo:
o USDA exige que exportadores privados americanos declarem, dentro de 24 horas,
qualquer venda confirmada de ≥100 mil toneladas para um único destino ou ≥200
mil toneladas para múltiplos destinos — os chamados "flash sales". Três anúncios
desse tipo no mesmo dia é um sinal de demanda de exportação concreta (vendas já
fechadas, não estimativa), o tipo de notícia que historicamente move o mercado
de forma rápida e direta. O dump não traz o timestamp exato do anúncio frente
ao movimento intradiário, então a relação causal não pode ser cravada com
certeza — mas o formato do dia (queda pela manhã, recuperação forte depois) é
consistente com essa notícia tendo revertido o humor do mercado durante a
sessão.

**A curva forward mantém o formato de "sorriso" já documentado, com magnitude
muito próxima à de leituras anteriores**: Agosto/26 (Q26, spot) 1.204,00 →
Setembro/26 (U26) 1.193,00 (desconto de −11,00, −0,91%) → Novembro/26 (X26)
1.202,50 (recupera +9,50 sobre setembro, ficando praticamente colado ao spot,
apenas −0,12% abaixo) → Janeiro/27 (F27) 1.216,50 (+1,16% sobre novembro) →
Março/27 (H27) 1.219,50 (+0,25% sobre janeiro). O desconto no meio da curva e o
prêmio na ponta longa seguem intactos — a curva não está descontando um susto
estrutural de oferta, só acompanhando o spot num movimento que, hoje, foi de
alta.

**A paridade teórica em reais subiu para R$ 135,84/saca 60kg** (indicadores,
17/07/2026: CBOT 1.204,00 cts × PTAX 5,1176 USD/BRL) — e, pela primeira vez em
várias leituras, o câmbio usado é o do PRÓPRIO dia (o BCB publicou o PTAX de
17/07 a tempo da coleta), eliminando a defasagem de um dia que exigia
comparações pareadas em leituras anteriores. Comparando com o físico de
Paranaguá do mesmo dia (R$ 141,02/saca, CEPEA/ESALQ via NAG, 17/07/2026): um
prêmio de R$ 5,18/saca (+3,81%) do físico sobre a paridade teórica — que
**comprimiu** frente ao prêmio pareado de 16/07 (R$ 6,29/saca, +4,68%). A
compressão de hoje não veio de o físico ter caído (Paranaguá subiu +0,31% no
dia), mas de a paridade teórica ter subido mais rápido (CBOT +0,75% mais PTAX
+0,39% [de 5,0975 para 5,1176] combinados) — um sinal de que o físico, por
ora, não está perseguindo a força do papel com a mesma velocidade, o que vale
monitorar (ver Honestidade). O físico do Paraná interior fechou em R$
134,11/saca (17/07, NAG), um desconto de R$ 6,91/saca frente ao suporte de
Paranaguá, dentro do spread logístico normal já documentado (R$ 6,64-6,91 nas
últimas leituras).

**O COT (CFTC), que faltava na leitura de ontem, chegou hoje com dado de
referência 14/07/2026 — trata `release-cftc_cot-2026-07-14`.** Managed money
net long em soja subiu para +75.191 contratos (7,48% do open interest de
1.004.746), de +69.579 contratos (7,13% do OI de 975.954) em 07/07/2026. O
open interest também cresceu +2,95% na semana — ou seja, o aumento do net long
veio acompanhado de crescimento do interesse aberto total, uma assinatura
típica de **dinheiro novo entrando comprado**, não apenas de posições vendidas
sendo fechadas. Isso é uma confirmação de positioning para o viés de alta,
ainda que o dado seja de 14/07 (três dias antes do rompimento de hoje) — o
próximo COT (dado esperado ~21/07, publicação ~24/07) é que vai mostrar se essa
compra continuou durante a semana do rompimento.

**O USDA Crop Progress permanece sem atualização desde 12/07/2026** (65% da
lavoura americana em condição boa-ou-excelente, 12% excelente + 53% boa, 6% em
condição ruim) — o próximo relatório semanal normal deve sair na segunda-feira,
20/07/2026. Sem dado novo, esse argumento segue congelado.

**Os forecasts estatísticos internos (17/07/2026, já calculados sobre o spot
definitivo de 1.204,00)** seguem altistas e aceleraram frente a ontem: central
7d = 1.233,07 cts/bu (bandas 1.182,42-1.283,73, acima do central de ontem,
1.226,82); central 30d = 1.339,49 cts/bu (bandas 1.234,63-1.444,35, acima de
1.327,14 ontem). É a segunda sessão seguida em que as seis bandas do sistema
(soja, farelo e óleo, 7d e 30d) fecham simultaneamente em viés altista — e,
diferente de ontem, hoje o preço também subiu no dia, então modelo estatístico
e movimento de preço apontam na mesma direção.

### O que invalida / risco para a soja

- **Um fechamento de volta abaixo de 1.195,00 (abertura/fechamento revisado de
  ontem) ou de 1.186,75 (mínima de hoje)** questionaria a força da recuperação
  em V e reabriria o cenário de teste do suporte 1.180,00.
- **Os números de hoje serem revisados amanhã na mesma linha do que já ocorreu
  duas vezes nesta série** — mesmo com volume de 27.197 contratos (ordem de
  grandeza normal, bem mais robusto que os 2.182 da leitura intraday), o
  precedente de farelo (+1,22%) e heating oil (+4,90%) revisados de uma geração
  do dump para a seguinte não permite tratar 1.204,00 como blindado a revisão.
- **O prêmio físico de Paranaguá sobre a paridade continuar comprimindo** —
  caiu de 4,68% (16/07) para 3,81% (17/07); uma sequência de compressão
  sinalizaria que o físico não está validando a força do papel.
- **O COT de 21/07 (publicação ~24/07) mostrar que os fundos venderam durante o
  rompimento de hoje** — o dado disponível (14/07) é de antes do movimento de
  hoje, então ainda não testa a tese com a informação mais recente.
- **Novas leituras de Crop Progress (esperadas ~20/07) mostrarem melhora
  continuada** — reduziria progressivamente o argumento de oferta apertada que
  sustenta parte do apetite comprador.

### Leitura operacional — soja

O viés foi corrigido de bear tático (na leitura intraday de hoje) para bull
tático, com convicção moderada-alta: o fechamento definitivo mostra uma
recuperação em V que reconquistou e ultrapassou a resistência de 1.180,00 com
folga confortável (2,03%), num dia com volume próximo do normal (27.197
contratos) e uma notícia de demanda concreta (flash sales da USDA) no mesmo
pregão. Para quem está comprado, 1.180,00 volta a ser a referência de stop
lógica, agora com mais espaço do que ontem. Para quem está vendido contra o
rompimento de 06-07/07, a tese de hoje enfraquece esse posicionamento — um
short aberto na leitura intraday (que apontava rompimento de baixa) provavelmente
está no vermelho com o fechamento real. O evento mais importante para testar se
esse novo posicionamento é sólido é dobrado: (1) a confirmação de amanhã de que
os números de hoje não sofrem nova revisão material, e (2) o próximo COT
(~24/07), que vai mostrar se o dinheiro novo que entrou comprado até 14/07
continuou entrando durante o rompimento desta semana.

---

## Farelo

**Viés: bear (estrutural mais forte do que nunca, tático cruzado pela primeira
vez com dado definitivo — mas por margem mínima). O ratio Far/Soj fechou em
79,98% (indicadores, 17/07/2026: farelo 321,00 ÷ soja 1.204,00, base
normalizada) — abaixo do limiar de 80% pela primeira vez desde que a revisão de
dados resetou a contagem ontem, cruzando por apenas 0,02 ponto percentual.
Trata `ratio-zona-2026-07-17` e `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
(revisão programada, agora 29 dias vencida — ver abaixo).**

### O que sustenta a tese

**O ratio Far/Soj voltou a fechar abaixo de 80% — mas por uma margem que
precisa ser tratada com cautela, dado o histórico recente da série.** Refazendo
a sequência com os números que o sistema hoje trata como definitivos: 79,52%
(13/07) → 79,83% (14/07) → 79,58% (15/07) → 81,06% (16/07, revisado) → **79,98%
(hoje)**. É a primeira vez, desde que a revisão de ontem resetou a contagem, que
o ratio fecha de volta abaixo do limiar — mas a distância (0,02 ponto) é
minúscula frente à revisão de 1,28 ponto que moveu o fechamento de 16/07 de
79,78% para 81,06% entre uma geração do dump e a seguinte. Tratar o
cruzamento de hoje como "confirmação limpa" seria repetir o mesmo erro
metodológico que a leitura de ontem cometeu ao celebrar prematuramente a
"quarta confirmação orgânica" — a postura correta é tratar 79,98% como um
cruzamento tecnicamente válido, mas frágil, que precisa de uma segunda sessão
consecutiva abaixo de 80% para ganhar robustez.

**A vela de hoje do farelo, ao contrário do que a leitura intraday sugeriu, não
foi uma queda monotônica sem recuperação.** Fechamento em 321,00, abertura em
322,90 (idêntica ao fechamento revisado de ontem, sem gap — o mesmo padrão
observado na soja), mínima de 318,50 e máxima de 322,90 (a própria abertura).
O fechamento está a 2,50 pontos acima da mínima, sobre um range de 4,40 pontos
— ou seja, o farelo recuperou 57% do movimento de baixa intradiário, uma vela
bem menos fraca do que a "abriu na máxima, fechou na mínima" registrada na
leitura intraday (que capturou apenas a primeira metade do movimento). Ainda
assim, uma queda de −0,59% no dia, e a perna claramente mais fraca do complexo
frente à soja (+0,75%) e ao óleo (+3,30%) — essa **divergência relativa**, não
o formato da vela isolada, é o que de fato sustenta a leitura bear do farelo
hoje.

**Tratando `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`:**
a revisão programada da tese original (insight
[[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]) tinha data-alvo
18/06/2026 — hoje, 17/07/2026, ela está 29 dias vencida. As três perguntas da
revisão D+7 eram: (1) o ratio fechou abaixo de 80%? (2) o WASDE mudou o quadro?
(3) o NOPA confirmou o ritmo de esmagamento? Respostas com os dados de hoje:
(1) **sim, tecnicamente**, mas por margem mínima (79,98%, cruzamento de apenas
0,02 ponto, sem confirmação de uma segunda sessão) — tratar como confirmação
PROVISÓRIA; (2) **não**, o WASDE segue parado em 10/07/2026, sem cobertura de
soja em grão ou óleo, e sem atualização para farelo desde então; (3) **não**, o
NOPA segue inacessível (ver abaixo). Status da tese original: mantida como
"bear-farelo estrutural", com o gatilho tático agora tecnicamente disparado
pela primeira vez, mas ainda sem a confirmação de fundamentos (WASDE, NOPA) que
a revisão original pedia. Recomenda-se reabrir esta revisão formalmente assim
que o NOPA ou um novo WASDE de soja/óleo estiverem disponíveis.

**A crush margin fechou em 3,2522 USD/bushel** (indicadores, 17/07/2026: farelo
321,00 + óleo 74,82 − soja 1.204,00) — o **maior valor de toda a janela visível
neste dump**, superando o 3,1211 revisado de 16/07 e o 3,1804 da leitura
intraday de hoje. Esse é o pilar estrutural mais robusto do farelo, porque não
depende de qual perna caiu ou subiu mais rápido no dia: quanto maior a crush
margin, maior o incentivo da esmagadora a processar soja a pleno vapor, e mais
farelo (subproduto obrigatório do esmagamento) entra no mercado — o mecanismo
estrutural que sustenta a tese de excesso de oferta.

**A trajetória projetada da ABIOVE (Associação Brasileira das Indústrias de
Óleos Vegetais, projeções mensais, sem alteração) segue sendo o pilar mais
sólido do argumento estrutural, porque não depende do preço do dia.** A
exportação de farelo brasileiro projetada cai de 1.400 mil toneladas em
agosto/2026 para 700 mil toneladas em dezembro/2026 (queda de 50% em 4 meses),
enquanto a produção cai de forma bem mais suave (2.285,06 → 1.659,04 mil
toneladas no mesmo período, −27%) — o mecanismo é direto: menos farelo saindo
pelo porto, com produção caindo bem menos que a exportação, empurra o volume
excedente para o mercado interno de ração, pressionando o preço doméstico.

**As praças físicas de farelo no Brasil (NAG, 17/07/2026) mostram sinais
mistos.** Mato Grosso/IMEA subiu para R$ 1.602,80/ton (+1,61%, recuperando após
ficar parado em R$ 1.577,34 desde 09/07), Rondonópolis/MT ficou estável em R$
1.600,00/ton (0,0%, estabilizando depois da queda de −4,19% documentada ontem),
e Rio Grande do Sul seguiu em R$ 1.640,00/ton (inalterado). A estabilização em
Rondonópolis (nem mais queda, nem recuperação) é consistente com um mercado que
absorveu o choque de ontem sem reverter — nem confirma nem invalida o mecanismo
estrutural ABIOVE de forma definitiva. O prêmio de exportação em Paranaguá
segue em +0,05 USD/short_ton (julho/26, NAG), agora **14 dias corridos sem
qualquer variação** desde 03/07/2026 — como já registrado em leituras
anteriores, essa constância pode refletir um mercado de exportação genuinamente
parado ou uma fonte não atualizada (ver Honestidade).

**O Índice de Sobra de Farelo (ISF) permanece em 80/100 (4 de 5 condições
estruturais)** (indicadores, 17/07/2026) — inalterado nas cinco sessões
visíveis neste dump (13 a 17/07) e, segundo leituras anteriores, desde pelo
menos 01/07/2026. Segue sendo o índice mais estável de toda a leitura,
calculado sobre condições estruturais (ABIOVE, crush, oferta), não sobre o
fechamento do dia.

**Tratando `release-nopa-2026-07-17`:** o NOPA (National Oilseed Processors
Association, dado mensal de esmagamento americano) segue com `monthly_status`
em 0,0 bool — a mesma barreira de assinatura paga documentada desde meados de
junho. Sem nenhuma informação nova para interpretar.

**O oil-meal spread (óleo menos farelo, por bushel) deu o maior salto de um dia
de toda a série: subiu para 1,1682 USD/bu**, de 0,8635 (16/07, revisado) —
uma alta de +35,3% no dia. Mede, de outro ângulo, a mesma divergência
farelo-fraco/óleo-forte que caracteriza o dia de hoje, e reforça a leitura de
que o mercado está precificando as duas pernas do crush de forma cada vez mais
diferente.

**O COT de 14/07/2026 traz um contraponto relevante à tese bear.** Managed
money net long em farelo saltou para +46.576 contratos (7,77% do open interest
de 599.353), de +18.722 contratos (3,14% do OI de 595.447) em 07/07/2026 — mais
que dobrou em uma semana, o maior salto percentual de posicionamento entre as
três pernas. À primeira vista, isso parece um sinal de que os fundos não
compram a tese bear-farelo e estão posicionados contra ela — risco real de que
uma posição vendida em farelo direcional puro sofra um "short squeeze" se essa
compra continuar. Olhando com mais cuidado, porém: o net long de farelo como
fração do OI (7,77%) ficou muito próximo do de soja (7,48%), e bem abaixo do de
óleo (16,92%, ver seção Óleo) — e as três pernas tiveram o net long crescendo
na mesma semana (soja +8%, farelo +149%, óleo +27%). Isso é mais consistente
com um fluxo amplo de "comprar o complexo inteiro" (possivelmente ligado a
rebalanceamento de índice ou apetite macro por commodities agrícolas) do que
com uma convicção específica dos fundos contra a tese bear-farelo — mas, sem
dado de percentil histórico (ver Honestidade), essa leitura fica no campo do
plausível, não do confirmado. De qualquer forma, é o dado mais direto disponível
hoje que argumenta contra uma posição vendida em farelo outright.

**O forecast estatístico do farelo (17/07/2026)** segue com viés altista e
subiu frente a ontem: central 7d = 327,93 USD/sht (bandas 315,23-340,63,
acima do central de ontem, 325,11); central 30d = 353,33 USD/sht (bandas
327,04-379,62, acima de 347,56). O modelo estatístico (que reage a momentum de
preço recente, não a fundamentos) segue na direção oposta à tese fundamentalista
ABIOVE + ratio, ainda ancorado na recuperação de preço desde a mínima de 293
documentada em junho.

### O que invalida / risco para o farelo

- **O ratio não fechar novamente abaixo de 80% na próxima sessão** — a margem
  de hoje (0,02 ponto) é pequena demais para ser tratada como confirmação
  robusta; um retorno acima de 80% (mesmo que por revisão) reabriria a mesma
  discussão de ontem.
- **A tese estrutural ABIOVE não se confirmar no físico ao longo do 2S/26** —
  a estabilização (não reversão) de Rondonópolis hoje é um sinal neutro, não
  uma confirmação.
- **O COT de 21/07 (publicação ~24/07) mostrar os fundos continuando a
  aumentar o net long em farelo** — reforçaria o risco de squeeze numa posição
  vendida direcional.
- **NOPA seguir inacessível indefinidamente**, sem confirmação do esmagamento
  americano para os checkpoints D+90 (09/09/2026) e D+180 (08/12/2026).
- **O prêmio de exportação Paranaguá "congelado" em 0,05 USD/sht ser, na
  verdade, um dado sem atualização de fonte, não um preço de mercado real**
  (ver Honestidade).
- **O padrão de revisão dump-a-dump se repetir com os números de hoje** — dado
  o precedente de duas revisões materiais consecutivas, o fechamento de hoje
  (321,00) e o ratio de hoje (79,98%) devem ser tratados como sujeitos a
  revisão até a próxima geração confirmar.

### Leitura operacional — farelo

A tese estrutural (ABIOVE, ISF 80/100, crush margin em novo topo) segue sendo o
pilar mais forte de toda a leitura de hoje. O gatilho tático (ratio < 80%)
tecnicamente disparou pela primeira vez com dado definitivo, mas a margem de
0,02 ponto é frágil demais, e o COT de hoje mostra fundos ampliando net long em
farelo na mesma semana — dois motivos para não tratar isso como luz verde para
uma posição vendida direcional pura. A postura recomendada é aguardar uma
segunda sessão consecutiva abaixo de 80% antes de tratar o gatilho tático como
robusto, dimensionando a posição principalmente no pilar estrutural. Para quem
prefere o veículo mais defensável — o spread farelo/soja ou o crush completo,
em vez de direcional puro —, o argumento para esse veículo permanece o mais
forte da leitura: ele captura a divergência relativa (farelo -0,59% vs soja
+0,75% vs óleo +3,30% hoje) sem depender de o ratio confirmar de forma limpa
nos próximos pregões, e sem ficar exposto ao risco de squeeze que o
posicionamento crescente dos fundos em farelo outright sugere.

---

## Óleo

**Viés: bull forte (upgrade de bull moderado — a perna mais limpa e com o
volume mais próximo do normal do complexo hoje) — fechou em 74,82 cts/lb
(17/07/2026), subindo +3,30% no dia (de 72,43 para 74,82, trata
`alerta-movimento_forte-oleo_cbot-2026-07-17`), fechando a 79% do topo do range
(mínima 72,43, máxima 75,44). O oil share subiu para 53,82% (novo topo da
janela) e o Índice de Suporte do Óleo (ISO) segue em 100/100.**

### O que sustenta a tese

**O óleo fechou hoje em 74,82 cts/lb** (CBOT, 17/07/2026), com abertura em
72,62 (praticamente na mínima do dia, 72,43) e máxima de 75,44 — o preço subiu
de forma consistente ao longo da sessão, e o fechamento retém 79% do movimento
até a máxima. É a vela mais forte de toda esta série de leituras (13-17/07), e
o volume de 40.029 contratos é o mais próximo de "típico" das três pernas hoje
— o que dá à alta de hoje um grau de confiança bem maior do que o normal para
uma leitura do dia da publicação.

**A curva forward manteve backwardation, e ela se aprofundou um pouco frente a
leituras anteriores**: Agosto/26 (Q26, spot) 74,82 → Setembro/26 (U26) 73,94
(−0,88, −1,18%) → Outubro/26 (V26) 73,03 (−0,91, −1,23%) → Dezembro/26 (Z26)
72,44 (−0,59, −0,81%) → Janeiro/27 (F27) 72,05 (−0,39, −0,54%) — uma queda
total de −2,77 cts/lb (−3,70%) de agosto a janeiro/27. O aprofundamento (frente
a magnitudes de −2,98% a −3,0% documentadas em leituras recentes) é coerente
com um rali concentrado no vencimento mais próximo — a assinatura típica de um
catalisador de curto prazo (como a força do crush margin e/ou a notícia de
exportação de soja puxando o complexo) em vez de uma re-precificação
estrutural de toda a curva.

**A margem de biodiesel americano fechou em 0,7029 USD/galão** (indicadores,
17/07/2026: receita 7,1144 = HO/heating oil 3,9494 + 1,5×RIN 2,11; custo 6,4115
= óleo 5,6115 + industrial 0,80) — uma queda de −27,0% frente ao valor
revisado de 16/07 (0,9635), e o **menor valor de toda a janela de 5 dias**
(0,7271 em 13/07 → 0,9493 em 14/07 → 0,8443 em 15/07 → 0,9635 em 16/07,
revisado → 0,7029 hoje). O mecanismo por trás dessa queda é importante e é uma
tensão real dentro da própria tese bull do óleo: a mesma alta de +3,30% no
preço do óleo que é bullish para o papel CBOT é, ao mesmo tempo, bearish para a
margem do produtor de biodiesel, porque o óleo é o principal insumo de custo
(custo do óleo subiu para US$ 5,6115/galão, +3,3%, enquanto a receita — heating
oil + RIN — cresceu só marginalmente, com o heating oil caindo −2,0% no dia,
3,9494 vs 4,0307 revisado de ontem). Se essa margem seguir comprimindo, o
incentivo ao blending voluntário de biodiesel acima do mandato B15 enfraquece,
mesmo que o preço do óleo continue subindo — uma dinâmica que vale a pena
monitorar de perto nos próximos dias.

**O Índice de Suporte do Óleo (ISO) permanece em 100/100 (5 de 5 condições)**
(indicadores, 17/07/2026) — inalterado nas cinco sessões visíveis neste dump
(13 a 17/07). O índice não reagiu à queda de margem de hoje porque é calculado
sobre um conjunto mais amplo de condições (não só o nível pontual da margem) —
mas se a compressão da margem persistir nos próximos dias, é o indicador a
observar para uma eventual mudança.

**O oil share (fração do valor do crush capturada pelo óleo) subiu para
53,82%** (indicadores, 17/07/2026) — o **maior valor da janela visível** (contra
53,44% em 13/07, o pico anterior), confirmando que o óleo continua sendo o
motor de valor do crush, agora com ainda mais força do que em qualquer dia
recente. Coerente com o oil-meal spread (+35,3% no dia, ver Spreads): o óleo
capturou proporcionalmente mais valor do crush hoje do que em qualquer outro
dia da janela.

**O COT de 14/07/2026 mostra o óleo como a perna mais "concorrida" das três em
termos de posicionamento.** Managed money net long subiu para +107.945
contratos (16,92% do open interest de 638.102), de +84.919 contratos (13,22% do
OI de 642.514) em 07/07/2026 — um aumento de +23.026 contratos (+27,1%) na
semana, o maior em termos absolutos das três pernas. Diferente da soja (onde o
OI total também cresceu, sinal de dinheiro novo), o OI do óleo **caiu**
ligeiramente (−0,69%) na mesma semana — o que sugere que parte do aumento do
net long veio de posições vendidas sendo fechadas (short covering), não só de
compra nova. Com o net long em ~17% do OI (o mais alto das três pernas, e sem
histórico de percentil para calibrar o quão "esticado" isso está — ver
Honestidade), a posição comprada no óleo é a mais crowded do complexo, o que é
ao mesmo tempo uma confirmação do momentum bull e um fator de risco: uma
posição concentrada tende a reagir de forma mais abrupta a qualquer notícia que
contrarie a tese.

**O forecast estatístico do óleo (17/07/2026) reforça o viés altista e
acelerou**: central 7d = 75,83 cts/lb (bandas 71,08-80,58, acima do central de
ontem, 73,43); central 30d = 80,38 cts/lb (bandas 70,55-90,21, acima de 76,79).
É a segunda leitura seguida em que as seis bandas de forecast do sistema
fecham simultaneamente em viés altista, e hoje, diferente de ontem, o preço
também subiu no dia — modelo estatístico e movimento de preço, mais uma vez,
apontando na mesma direção dentro dessa perna.

### O que invalida / risco para o óleo

- **Um fechamento abaixo de 73,03 (o vencimento de outubro na curva de hoje)**
  reabriria o cenário de correção — não ocorreu hoje, mas o padrão de reversão
  rápida já visto em outras pernas do complexo nesta semana não pode ser
  descartado.
- **A margem de biodiesel (0,7029 USD/gal, a menor da janela) seguir
  comprimindo** — se o óleo continuar subindo mais rápido que a receita
  (heating oil + RIN), o incentivo de blending voluntário acima do mandato B15
  enfraquece, testando eventualmente o ISO.
- **O posicionamento dos fundos (net long em 16,92% do OI, o mais concorrido
  das três pernas) sofrer uma reversão** — sem histórico de percentil para
  calibrar, não é possível dizer se isso já está "esticado" no sentido
  histórico, mas é a posição mais concentrada do complexo, logo a mais sensível
  a um catalisador negativo.
- **O heating oil (proxy de receita do biodiesel) seguir caindo** — recuou
  −2,0% hoje frente ao pico revisado de 16/07 (4,0307); uma sequência de
  quedas pressionaria ainda mais a margem.
- **MPOB seguir inacessível** — impossível avaliar o efeito do El Niño ou das
  restrições/levy indonésias (PMK 9/2026, Danantara — ver Lente fiscal) sobre o
  prêmio de substituição via palma.

### Leitura operacional — óleo

O óleo é hoje a tese mais forte e mais bem sustentada por volume do complexo:
vela de alta consistente, backwardation, oil share em novo topo, ISO no
máximo, e forecast estatístico e preço andando na mesma direção. Duas nuances
pedem cautela na hora de dimensionar: a margem de biodiesel comprimiu para o
menor valor da janela (o próprio rali do óleo está apertando a economia de
quem faz biodiesel), e o posicionamento dos fundos já é o mais concorrido das
três pernas (16,92% do OI), o que aumenta o risco de um movimento de dois lados
mais abrupto do que em soja ou farelo. Para quem opera exposição relativa
dentro do crush, os pilares estruturais seguem intactos e reforçados — o
oil-meal spread (óleo menos farelo) deu hoje o maior salto de um dia de toda a
série (+35,3%), sendo o veículo mais direto para capturar a divergência entre
as duas pernas. Para quem opera direcional puro em óleo, a vela de hoje é a
mais limpa da semana, mas o tamanho da posição deveria refletir tanto o
posicionamento já concorrido quanto a possibilidade (recorrente nesta série) de
revisão do fechamento amanhã.

---

## Spreads e crush — leitura de complexo

### Crush margin: 3,2522 USD/bu — novo topo da janela, pela terceira sessão seguida em alta

A crush subiu pela terceira sessão seguida e atingiu o maior valor visível
nesta série (3,0211 em 13/07 → 3,0193 em 14/07 → 3,0145 em 15/07 → 3,1211 em
16/07 → 3,2522 hoje). O incentivo de esmagamento a pleno vapor está se
fortalecendo de forma consistente, alimentando o mecanismo estrutural ABIOVE
independentemente de qual perna do complexo está subindo ou caindo no dia.

### Ratio Far/Soj: 79,98% — cruzou abaixo de 80% pela primeira vez com dado definitivo, mas por margem mínima

O achado tático central desta leitura: depois do reset causado pela revisão de
16/07 (79,78%→81,06%), o ratio voltou a fechar abaixo de 80% hoje — mas por
apenas 0,02 ponto percentual, uma margem menor que qualquer revisão já
documentada nesta série. Sequência completa: 79,52% (13/07) → 79,83% (14/07) →
79,58% (15/07) → 81,06% (16/07, revisado) → **79,98% (hoje)**. Trata
`ratio-zona-2026-07-17` e a revisão programada
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` (agora 29
dias vencida, ver seção Farelo para o detalhamento completo das três perguntas
da revisão original). Recomenda-se tratar este cruzamento como PROVISÓRIO até
uma segunda sessão consecutiva confirmar abaixo de 80%.

### Oil share: 53,82% — novo topo da janela

Subiu de 52,86% (16/07, revisado) para 53,82% hoje, superando o pico anterior
de 53,44% (13/07) — o óleo capturando a maior fatia do valor do crush em toda a
janela visível, coerente com sua vela mais forte do dia.

### Oil-meal spread: 1,1682 USD/bu — maior alta de um dia da série (+35,3%)

Subiu de 0,8635 (16/07, revisado) para 1,1682 USD/bu hoje — mede o valor do
óleo menos o valor do farelo por bushel; a alta de hoje é o maior movimento de
um dia documentado nesta série, capturando de forma direta a divergência entre
o óleo (vela mais forte da semana) e o farelo (a perna mais fraca hoje) na
mesma sessão.

### COT: os fundos compraram as três pernas na semana até 14/07 — óleo é a mais concorrida

O dado que faltava ontem (trata `release-cftc_cot-2026-07-14`) mostra o
managed money ampliando net long em soja (+8% na semana, com OI também
subindo — dinheiro novo), farelo (+149%, o maior salto percentual, mas partindo
de uma base pequena e ainda com net long/OI comparável ao da soja) e óleo
(+27%, com OI caindo — parte via short covering). Como fração do open
interest, o óleo é disparado o mais concorrido (16,92% vs 7,77% do farelo e
7,48% da soja) — o posicionamento confirma o bull-oleo desta leitura, mas
também é o maior fator de risco de reversão abrupta caso o fundamento (margem
de biodiesel, que já comprimiu hoje) vire.

### ISF em 80/100, ISO em 100/100 — os dois índices que nenhuma revisão tocou

O Índice de Sobra de Farelo (ISF, 4/5 condições) e o Índice de Suporte do Óleo
(ISO, 5/5 condições) permanecem inalterados em todas as cinco sessões visíveis
neste dump (13 a 17/07) e, segundo leituras anteriores, desde pelo menos
01/07/2026. Continuam sendo o contraponto mais estável de toda a leitura,
porque são calculados sobre condições estruturais (ABIOVE, crush, oferta), não
sobre o fechamento pontual do dia.

### O que os índices dizem juntos em 17/07/2026

ISF 80/100 + ISO 100/100 (ambos estáveis) + ratio Far/Soj cruzando abaixo de
80% pela primeira vez com dado definitivo (mas por margem frágil) + oil share
em novo topo (53,82%) + crush margin em novo topo pela terceira sessão seguida
(3,2522) + oil-meal spread com a maior alta de um dia da série (+35,3%) + COT
mostrando fundos comprando as três pernas, com óleo disparado o mais
concorrido — formam um quadro coerente de complexo esmagando a pleno vapor
(garantindo fluxo constante de farelo e óleo simultaneamente), mas com o
mercado precificando essas duas saídas de forma cada vez mais diferente: o
óleo captura valor, volume e posicionamento de fundo de forma inequívoca; o
farelo tem a estrutura ABIOVE a seu favor mas o gatilho tático ainda frágil e
posicionamento de fundos crescendo contra a tese bear.

---

## Lente fiscal e regulatória BR

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L) — a
vigência formal (`vigencia_ate` 11/07/2026) venceu há 6 dias, e o monitor
tributário segue sem qualquer atualização de status** (system/tributario_watch.toml,
evento MP-1358-2026, `atualizado_em` 2026-06-05, status ainda "tramitacao").
Enquanto o combustível fóssil segue subsidiado, a competitividade relativa do
biodiesel dentro do mix B15 mandatório fica pressionada — um mecanismo que hoje
ganha um segundo motivo de atenção: a margem de biodiesel americana (proxy
paralelo, calculada sobre RIN D4 + heating oil) comprimiu para o menor valor da
janela (0,7029 USD/gal), então dois sinais independentes (regulatório BR +
margem econômica US) apontam, no mesmo dia, para um ambiente mais apertado
para o blending de biodiesel.

**Isenção PIS/Cofins biodiesel — vencimento em 31/07/2026, agora a 14 dias.**
Sem sinalização pública de renovação até hoje (evento
PISCOFINS-BIODIESEL-ISENCAO, `atualizado_em` 2026-06-05, sem mudança). Se essa
isenção expirar bem no momento em que a margem de biodiesel já está no piso da
janela recente, o efeito combinado (custo tributário + margem apertada) seria
um duplo headwind para o blending doméstico em agosto — vale ser o relógio
fiscal mais monitorado nas próximas duas semanas.

**B16 — sem data, travado em B15.** Sem mudança de status (evento
B16-CNPE-2026, `atualizado_em` 2026-06-05, status "adiado"). Testes técnicos do
FNDCT com resultado esperado ~nov/2026 — realista só fim de 2026/início de
2027.

**MP 1.363/2026 (subsídio ao diesel fóssil, R$ 1,12/L) — em vigor até
31/12/2026.** Sem alteração. Bearish estrutural persistente para a demanda
incremental de óleo de soja no mercado doméstico brasileiro.

**STJ REsp 2.165.276/2026 — crédito PIS/Cofins para esmagadoras.** Sem
alteração. Bullish para soja/óleo (alívio de custo de entrada para biodiesel) e,
por extensão, incentivo a mais esmagamento — coerente com a crush margin em
novo topo documentada hoje pela terceira sessão seguida.

**Vetores dos EUA e Indonésia, revisitados (sem mudança de status,
`atualizado_em` 2026-06-05 em todos):** EPA-RFS-2026-2027 (volumes recordes de
biocombustível, BBD 8,86→9,07 bi RINs, sustentando estruturalmente o RIN D4 e o
óleo CBOT); 45Z-CLEAN-FUEL (regra proposta que tiraria insumo importado da
elegibilidade ao crédito, favorecendo óleo de soja doméstico americano);
DANANTARA-INDONESIA (centralização estatal da exportação de palma, assunção
plena da cadeia alvo em 01/09/2026 — risco de menor saldo exportável de palma,
suporte ao óleo de soja por substituição); INDONESIA-B50 (retórica agressiva
mas quota flat — provável B45 em 2026, B50 pleno só 2027-28); INDONESIA-LEVY-PMK9
(imposto de exportação de CPO até 12,5% desde 01/03, encarecendo palma e
favorecendo substituição por óleo de soja). Todos esses vetores seguem, em
conjunto, num sentido estruturalmente bullish para o óleo de soja via
substituição de palma — coerente com o viés bull forte de hoje na seção Óleo.

**O monitor tributário como um todo está há 42 dias sem qualquer atualização**
(`atualizado_em` 2026-06-05 em todos os dez eventos rastreados) — o intervalo
segue crescendo em um momento em que dois vetores (MP 1.358 e a isenção
PIS/Cofins) têm datas de vencimento formal já vencida ou a apenas 14 dias. Vale
sinalizar este ponto como prioridade de manutenção do sistema, independentemente
da leitura de preço.

---

## Riscos e eventos próximos

**Confirmar se os preços de hoje (soja 1.204,00, farelo 321,00, óleo 74,82,
ratio 79,98%) sofrem revisão amanhã.** É o item de maior prioridade: esta é a
terceira sessão seguida em que a comparação entre a geração intraday e a
geração de fechamento do dump revela diferenças materiais — e desta vez, pela
primeira vez, uma reviravolta completa de sinal tático (soja de bear pra bull).
Tratar o fechamento de hoje como preliminar até a confirmação de amanhã.

**COT (CFTC) — dado de 14/07/2026 chegou hoje, mas ainda não cobre a semana do
rompimento.** O próximo dado (referência ~21/07, publicação normal ~24/07) é o
que vai mostrar se os fundos continuaram comprando soja e óleo, e se
começaram a reduzir farelo, durante a semana em que o ratio finalmente cruzou
abaixo de 80%.

**O cruzamento do ratio Far/Soj abaixo de 80% precisa de uma segunda sessão de
confirmação** — a margem de hoje (0,02 ponto) é a menor de toda a série de
cruzamentos documentados, e o histórico recente mostra revisões maiores que
essa margem de uma geração do dump para a outra.

**A margem de biodiesel americana caiu para o piso da janela de 5 dias
(0,7029 USD/gal)** — monitorar se a compressão continua; é o dado mais direto
disponível sobre o incentivo de blending voluntário além do mandato B15, e
interage diretamente com o vencimento da isenção PIS/Cofins BR em 14 dias.

**Desfecho da MP 1.358/2026 — vigência formal encerrada há 6 dias, sem
confirmação.** Monitorar deliberação da comissão mista e qualquer decreto de
prorrogação.

**Isenção PIS/Cofins biodiesel — vencimento 31/07/2026 (14 dias).** Sem
sinalização de renovação até agora.

**Próxima leitura de USDA Crop Progress — esperada ~20/07/2026 (segunda-feira),
dados "as of" 19/07.** Sem atualização desde 12/07.

**NOPA — segue inacessível** (fila `release-nopa-2026-07-17` tratada aqui, sem
dado interpretável), sem crush americano confirmado por fonte primária.

**MPOB — sem números de palma extraídos**, mantendo cego o efeito do El Niño e
dos vetores regulatórios indonésios (Danantara, B50, levy PMK 9) sobre o prêmio
de substituição do óleo de soja.

**Checkpoints futuros da tese estrutural do farelo (ABIOVE)** — D+90 em
09/09/2026 e D+180 em 08/12/2026 (insight
[[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]) — a revisão D+7,
tratada nesta leitura com 29 dias de atraso, aponta confirmação tática
provisória (ratio < 80%) mas sem confirmação de fundamentos (WASDE, NOPA);
os checkpoints estruturais seguem o critério de mais alta confiança para julgar
a tese ao longo do tempo.

**Padrão sistêmico de revisão de dados dump-a-dump** — esta é agora a terceira
leitura seguida em que uma diferença material entre gerações do dump altera a
interpretação, e a primeira em que a diferença inverte o sinal tático de uma
das três pernas por completo. Recomenda-se, mais uma vez e com ainda mais
ênfase, tratar o fechamento e os índices do próprio dia de publicação como
preliminares por padrão.

---

## Honestidade

O que não foi possível validar neste briefing de 17/07/2026, onde a confiança é
baixa ou há lacunas materiais:

**1. A descoberta mais importante desta leitura: uma versão anterior desta
mesma data (17/07/2026), publicada mais cedo com dados intraday, chegou a uma
conclusão tática oposta à que os dados definitivos sustentam.** A versão
intraday (volumes de 1.087 a 3.244 contratos) descreveu a soja rompendo a
mínima de uma consolidação de quatro dias e fechando em 1.187,75, quase
testando o suporte estrutural de 1.180,00. Os dados que efetivamente fecharam
o pregão (volumes de 27.197 a 40.029 contratos, ordem de grandeza normal)
mostram a soja em 1.204,00 — uma recuperação em V que fecha **acima** da
resistência de 1.180,00 com folga de 2,03%. A mínima intraday (1.187,75) e a
mínima real do dia (1.186,75) são quase idênticas — o que sugere que a versão
intraday capturou fielmente o ponto mais baixo da manhã, mas não teve como
saber que a tarde traria uma reversão forte, possivelmente ligada ao anúncio de
flash sales da USDA no mesmo dia. Diferente das duas revisões anteriores desta
série (que alteravam preços de FECHAMENTO já publicados um dia depois), este
caso é sobre a diferença entre um dado ainda em formação (sessão em
andamento) e o dado após o fechamento — reforça, com um exemplo ainda mais
direto, a recomendação já feita nas duas últimas leituras: tratar qualquer
número do dia da própria publicação como preliminar.

**2. O cruzamento do ratio Far/Soj abaixo de 80% (79,98%) tem margem de apenas
0,02 ponto percentual** — menor que qualquer uma das revisões dump-a-dump já
documentadas nesta série (a maior foi de 1,28 ponto, entre as gerações de
16/07 e 17/07). Não há garantia de que esse cruzamento sobreviva à próxima
atualização dos dados de hoje.

**3. O COT (CFTC) chegou com dado de referência 14/07/2026, três dias antes do
fechamento de hoje.** A semana do rompimento da soja e do salto do óleo (a
semana de 14 a 17/07) ainda não está refletida no posicionamento dos fundos —
o próximo relatório (dado esperado ~21/07, publicação ~24/07) é que vai testar
se a compra de dinheiro novo em soja e óleo continuou durante essa semana.

**4. Percentis históricos de COT não calculados** — os números de 14/07/2026
são lidos apenas em nível absoluto e como fração do open interest corrente
(soja 7,48%, farelo 7,77%, óleo 16,92%), sem série histórica completa para
calibrar se algum desses níveis está objetivamente "esticado" no sentido
histórico. A leitura de que o óleo é "o mais concorrido" é uma comparação
relativa entre as três pernas nesta mesma semana, não uma leitura de percentil.

**5. O prêmio de exportação de farelo em Paranaguá (+0,05 USD/sht) e o de óleo
(+0,08 cts/lb) estão no mesmo valor exato desde pelo menos 03/07/2026** (NAG,
agora 14 dias corridos sem variação de nenhum centavo) — não é possível
distinguir, só com os dados disponíveis, se isso reflete um mercado de
exportação genuinamente parado ou um valor que não está sendo atualizado de
fato na fonte.

**6. O prêmio físico de Paranaguá sobre a paridade teórica comprimiu hoje
(4,68%→3,81%), mas é apenas um ponto de dado** — não é possível ainda
distinguir se é o início de uma tendência de o físico não acompanhar a força do
papel, ou apenas ruído de um dia.

**7. O WASDE segue cobrindo apenas farelo (Argentina, Brasil, China parcial),
sem nenhum dado de soja em grão ou óleo de soja, em qualquer geografia, e sem
nenhum dado dos Estados Unidos** — sem atualização desde 10/07/2026. A pergunta
central sobre "oferta grande de soja" segue sem canal de resposta interno, e é
uma das três perguntas não respondidas da revisão D+7 do farelo (ver seção
Farelo).

**8. NOPA (fila `release-nopa-2026-07-17`) segue com `monthly_status` em 0,0
bool** — mesma barreira de assinatura paga documentada desde meados de junho,
agora com mais de um mês sem alternativa de dado primário sobre o esmagamento
americano. É a segunda das três perguntas não respondidas da revisão D+7 do
farelo.

**9. Palma malaia (MPOB) segue sem números extraídos** (17/07/2026, mesmo
texto de HTML sem valores) — impossível avaliar o efeito do El Niño ou dos
vetores regulatórios indonésios (Danantara, B50, levy PMK 9 — ver Lente fiscal)
sobre o prêmio de substituição do óleo de soja.

**10. Clima INMET (BR) não foi usado como driver desta leitura.** Julho é
entressafra da soja brasileira (colheita concluída, plantio só em outubro) —
sem relevância direta para a tese de preço neste momento do calendário
agrícola, embora o El Niño Advisory (NOAA CPC, inalterado desde pelo menos
03/07/2026) permaneça relevante para a expectativa da safra de plantio de
outubro/26 e para o clima do Sudeste Asiático (palma).

**11. BCBA Argentina — sem relatórios de esmagamento/exportação acessíveis via
scraper** (page_fetched=1,0 mas sem links de relatório, 17/07/2026, sem
mudança).

**12. RIN D4 como parâmetro fixo (2,11 USD/RIN) segue sendo uma fonte relevante
de incerteza do modelo de biodiesel**, sem novo dado hoje — a margem de hoje
(0,7029, a menor da janela) foi calculada com esse valor fixo; se o RIN de
mercado estiver, na realidade, diferente de 2,11, tanto a margem quanto o ISO
podem estar mal calibrados, independentemente da compressão documentada nesta
leitura.

**13. A manchete de notícias de hoje (flash sales da USDA, Farm Progress) é a
única manchete específica de soja capturada no dump de 17/07** — o contador
mostra "160 itens lidos, 6 mantidos", mas sem visibilidade sobre os outros 5
itens mantidos além da manchete listada, nem sobre farelo ou óleo
especificamente. A relação causal entre o anúncio de flash sales e a
recuperação em V da soja é plausível e cronologicamente coerente, mas não pode
ser cravada sem o timestamp exato do anúncio frente ao movimento intradiário.

*Nenhum número foi inventado ou estimado além do que consta no briefing de
17/07/2026 e nos insights anteriores referenciados. A contribuição central
desta leitura foi identificar, com o fechamento definitivo da sessão, que a
soja não rompeu suporte como uma leitura intraday anterior do mesmo dia havia
descrito — na verdade fechou com folga acima da resistência —, ao mesmo tempo
em que o ratio Far/Soj cruzou abaixo de 80% pela primeira vez com dado
definitivo (por margem mínima) e o COT, ausente há dez dias, finalmente
confirmou os fundos comprando as três pernas do complexo na semana até 14/07.
A recomendação prática permanece a mesma das duas últimas leituras, agora
reforçada por um terceiro exemplo consecutivo: tratar qualquer leitura de vela,
volume ou índice do próprio dia de publicação como preliminar por padrão, e
revisitá-la explicitamente no dia seguinte antes de tratá-la como definitiva.*
