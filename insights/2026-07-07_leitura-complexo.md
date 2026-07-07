---
data: 2026-07-07
titulo: "Segundo pregão seguido confirma os dois gatilhos mais aguardados da série — soja fecha acima de 1.180,00 pela segunda vez consecutiva (1.186,25) e o ratio Far/Soj trava em 79,28% por dois fechamentos seguidos, a primeira validação plena da tese de 11/jun (farelo passa de 'quase' para 'confirmado'); óleo segue preso abaixo do suporte 72,00, mas o forecast de 30 dias do próprio farelo virou de lateral para altista, abrindo a primeira fissura estatística bem no momento em que a tese fundamentalista se confirma"
tags: [complexo, auto-claude]
fontes:
  - CBOT CME (ZSQ26/ZMQ26/ZLQ26 + curva forward completa + HO=F) — sessão de 2026-07-07
  - BCB PTAX — último dado disponível 2026-07-06 (USD/BRL 5,1670; EUR/BRL 5,9043; Selic 0,052531% a.a.), sem publicação de 07/jul no dump (defasagem normal de T+1, ver Honestidade)
  - CEPEA/ESALQ Paranaguá e Paraná interior via NAG — último dado disponível 2026-07-06
  - NAG Físico BR (farelo MT/IMEA, RS, Rondonópolis; prêmios export PGUA farelo/óleo) — 2026-07-06
  - CFTC COT Managed Money — 2026-06-30 (primeira atualização desde 23/06, tratada nesta leitura)
  - USDA Crop Progress — 2026-07-05 (atualizado desde 28/06)
  - NOAA CPC ENSO — 2026-07-07 (El Niño Advisory, sem mudança)
  - ABIOVE projeções mensais — balanços ago-dez/2026 (farelo/óleo/soja), sem alteração
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, margem biodiesel, ISF/ISO) — 2026-07-07
  - MPOB — 2026-07-07 (22º dia consecutivo sem números extraídos, desde 16/jun)
  - NOPA — 2026-07-07 (fila `release-nopa-2026-07-07`; monthly_status inacessível)
  - system/tributario_watch.toml — eventos MP-1358-2026, MP-1363-2026, PISCOFINS-BIODIESEL-ISENCAO, STJ-RESP-2165276, B16-CNPE-2026, EPA-RFS-2026-2027, 45Z-CLEAN-FUEL, DANANTARA-INDONESIA, INDONESIA-B50, INDONESIA-LEVY-PMK9 (todos `atualizado_em` 2026-06-05, sem mudança de status)
  - Notícias Agrícolas / Farm Progress — 2026-07-06 ("Soybeans rally on U.S. heat, China sales")
  - Forecasts estatísticos internos — 2026-07-07 (recalibrados com o spot de hoje)
  - Cruza com [[2026-07-06_leitura-complexo]], [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]], [[2026-05-26_subvencao-fossil-aperta-biodiesel]], [[2026-05-26_pis-cofins-biodiesel-explica-mercado-fisico-fraco]], [[2026-05-26_b16-bullish-farelo]], [[2026-05-26_curva-forward-cbot-oleo-desacopla]]
status: ativa
vies: [bull-soja, bear-farelo, bear-oleo]
---

## Visão geral

O complexo soja funciona como uma fábrica com uma única matéria-prima (a soja em grão) e
dois produtos de saída fabricados em proporção fixa a cada bushel esmagado: o **farelo** (a
fração proteica, ~78% da massa, vira ração animal) e o **óleo degomado** (a fração de
gordura, ~18-20% da massa, vira óleo de cozinha e biodiesel). Quem decide o ritmo de
esmagamento é a esmagadora, olhando a **crush margin** (o valor de mercado de farelo + óleo
produzidos por um bushel de soja, menos o custo daquele bushel) e o **oil share** (a fração
desse valor capturada pelo óleo). Quando o óleo "paga o crush" — como vem acontecendo desde
maio, com oil share girando em torno de 52% — a esmagadora tem incentivo a esmagar a pleno
vapor para capturar o valor do óleo, e "deixa sobrar" farelo como subproduto menos desejado.
O **ratio Far/Soj** (preço do farelo dividido pelo preço da soja, na mesma base) é o
termômetro dessa dinâmica: abaixo de 80% o farelo está "abundante" frente à soja (o cenário
que a tese de 11/06/2026 vinha antecipando), acima de 87% estaria "apertado".

**Hoje, 07/07/2026, é o dia da confirmação dupla.** Primeiro, a soja (ZSQ26.CBT) fechou em
**1.186,25 cts/bu**, subindo pelo segundo pregão seguido acima do nível técnico de 1.180,00
(fila `alerta-quebra_resistencia-soja_cbot-2026-07-07`) — o rompimento de ontem (1.184,00) não
foi um acidente de reabertura pós-feriado, teve continuidade. Segundo, e mais importante
estruturalmente: **o ratio Far/Soj fechou em 79,28% pelo SEGUNDO dia consecutivo** (indicadores,
07-06 e 07-07), a primeira vez que a métrica se sustenta abaixo do gatilho de 80% por mais de
uma sessão desde que a tese nasceu em 11/06/2026 (fila
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, D+26 e finalmente
resolvida). O protocolo original exigia "2-3 fechamentos consecutivos abaixo de 80%" para
confirmar — hoje esse critério é satisfeito pela primeira vez.

O terceiro fato relevante contradiz parcialmente o segundo: **o forecast estatístico de 30
dias do próprio farelo virou de "lateral" (ontem, central 312,43) para "altista" (hoje,
central 320,53)** — bem no momento em que a tese fundamentalista bearish finalmente se
confirma. Isso não invalida a tese (o modelo é puramente estatístico, baseado em média móvel
e volatilidade recentes, não em fundamento), mas é uma tensão real que merece monitoramento:
o mercado de futuros pode estar precificando continuação do rali generalizado do complexo,
não a compressão relativa que o ratio capturou.

O quarto fato é sobre qualidade de dado: pela primeira vez em várias leituras, o físico
brasileiro (CEPEA Paranaguá) e o câmbio (PTAX) estão defasados apenas **um dia** frente ao
CBOT — a normalidade de T+1, não mais os gaps de três dias vistos na reabertura pós-feriado.
E o COT da CFTC, que estava travado há 13 dias em 23/06, finalmente atualizou para **30/06**
— dado ainda anterior ao rali desta semana, mas mostra algo relevante: os fundos já vinham
reduzindo a posição comprada em óleo (-10,9%) e ampliando a posição vendida em farelo (short
+7,6%) antes mesmo da confirmação do ratio de hoje — ou seja, o "dinheiro grande" já estava
posicionado na direção que os fundamentos acabaram de confirmar.

**Leitura de uma linha:** o dia da confirmação — soja rompe 1.180 pela segunda vez seguida,
o ratio Far/Soj trava abaixo de 80% pela segunda vez seguida (tese de 25 dias finalmente
validada), e o óleo segue preso abaixo de 72,00 — mas o forecast de 30 dias do farelo
acabou de virar contra a própria tese que se confirmou hoje, e isso pede vigilância nas
próximas 2-3 sessões antes de tratar qualquer coisa como definitivo. Confiança alta no
bear-óleo tático; confiança agora alta (subindo de moderada-alta) no bear-farelo estrutural,
com a ressalva do forecast 30d; confiança moderada no bull-soja tático, pois o rompimento
veio em volume mais fraco que o pregão anterior.

---

## Soja

**Viés: bull tático — segundo fechamento consecutivo acima do nível técnico de 1.180,00,
mas em volume sensivelmente mais fraco que o pregão de ontem, e o próprio forecast de 7 dias
já trata o nível de hoje como o centro esperado da semana, não como ponto de partida**

### O que sustenta a tese

A soja de agosto (ZSQ26.CBT) abriu em 1.181,50, fez mínima em 1.180,00, máxima em 1.189,00 e
fechou em **1.186,25 cts/bu** (CBOT CME, 07/07/2026, volume 3.640 contratos), uma alta de
**+2,25 cts (+0,19%)** frente ao fechamento de ontem (1.184,00, via recálculo dos
indicadores de 06/07/2026) — tratando a fila `alerta-quebra_resistencia-soja_cbot-2026-07-07`.
É o segundo fechamento seguido acima do nível de 1.180,00 (o primeiro foi ontem, no
retorno do feriado), o que dá ao rompimento mais credibilidade técnica do que um único
pregão isolado teria. **Mas atenção ao volume:** o farelo negociou 23.412 contratos ontem
(dia de reabertura pós-feriado, com notícia acumulada de três dias) contra apenas 3.579 hoje
— uma queda de -84,7% na participação do complexo como um todo. A confirmação do rompimento
da soja veio, portanto, num dia de volume claramente mais fraco, um sinal técnico de cautela:
o mercado sustentou o nível, mas sem o mesmo fluxo que gerou o movimento inicial.

**A manchete do dia anterior (Farm Progress, 06/07/2026)** atribui o rali a "calor nos EUA e
vendas para a China" ("Soybeans rally on U.S. heat, China sales") — dois mecanismos
concretos e plausíveis: calor durante o florescimento/formação de vagens (julho é o mês
crítico para a lavoura americana) reduz expectativa de produtividade, e vendas à China
tensionam a disponibilidade de curto prazo. **O USDA Crop Progress, atualizado para
05/07/2026** (rompendo a estagnação de 28/06 que persistia há mais de uma semana), mostra
condição **11% excelente + 53% boa = 64% bom-ou-melhor**, ante 10%+55%=65% em 28/06 — uma
queda de -1 p.p. na condição combinada, com a fração "pobre" estável em 6%. É uma
deterioração pequena, mas na direção que a manchete de calor sugere, e é o primeiro dado
agronômico fresco da série em mais de uma semana.

**O câmbio (BCB PTAX) resolve uma divergência que a leitura de ontem havia sinalizado como
pendente de confirmação — e a resposta é o oposto do que a manchete de ontem sugeria.** A
manchete do Canal Rural de 06/07 falava em "dólar em alta", mas a série oficial de câmbio
mostra o real **se apreciando continuamente por quatro leituras seguidas**: USD/BRL 5,1950
(01/jul) → 5,1945 (02/jul) → 5,1717 (03/jul) → **5,1670 (06/jul, BCB PTAX, sgs=1)**. Ou
seja, o dólar não subiu — o real vem ficando mais forte desde o início de julho. Isso muda a
leitura do mecanismo: **o rali da soja não está sendo puxado por câmbio, está sendo puxado
integralmente pelo CBOT** (fundamento/fluxo americano), o que na verdade é um sinal mais
"limpo" para quem opera o papel, mas menos favorável para quem espera ganho adicional de
paridade em reais via depreciação cambial.

**A paridade em reais oficial (indicadores, 07/07/2026) subiu para R$ 135,13/saca60kg** (CBOT
1.186,25 cts × PTAX 5,1670 BRL/USD, sem básis), ante R$ 134,87 em 06/07 — um ganho de apenas
+R$ 0,26/saca (+0,19%), coerente com o CBOT ter avançado sozinho (mesma PTAX usada nos dois
cálculos, pois ainda não há PTAX de 07/07 no dump). **O dado mais interessante do dia está no
físico do porto:** a soja Paranaguá (CEPEA/ESALQ via NAG, 06/07/2026) fechou em **R$
139,01/saca**, subindo forte **+2,63%** frente aos R$ 135,45 de 03/07 — e esse valor está
**R$ 3,88/saca ACIMA da própria paridade teórica calculada (R$ 135,13)**. Isso é um sinal de
básis positivo genuíno no porto: o preço físico de Paranaguá está pagando um prêmio sobre o
valor "justo" de conversão do CBOT, coerente com a leitura de "exportações antecipadas" da
manchete de 06/07 — há demanda física real disputando o produto no porto, não apenas
valorização do papel. Já a soja Paraná interior (NAG, 06/07/2026) fechou em R$ 129,93/saca
(+1,18% frente a 03/07), ainda com desconto de -R$ 5,20/saca frente à paridade — o padrão
normal de porto mais caro que o interior, sem distorção.

**A colheita argentina segue encerrada em 98%**, produção mantida em 50,1 milhões de
toneladas (Canal Rural, 27/06/2026, sem atualização) — o competidor sul-americano já está
com oferta plena no mercado, um teto estrutural para o quanto a soja brasileira/americana
pode se valorizar por escassez regional.

**O posicionamento dos fundos (COT, CFTC) finalmente atualizou — de 23/06 para 30/06/2026,**
encerrando 13 dias de estagnação. A leitura, porém, não é de aposta direcional nova: managed
money net long em soja está em **+38.149 contratos** (long 133.396, short 95.247), ante
+36.986 em 23/06 — um ganho marginal de +1.163 contratos (+3,1%). O dado mais chamativo é
outro: o **open interest total caiu de 1.006.834 para 898.681 contratos (-10,7%)** — uma
redução generalizada de exposição bruta dos dois lados (long caiu -8.772, short caiu -9.935),
um "desalavancamento" coletivo, não uma aposta nova. Como fração do OI, o net long subiu
ligeiramente (4,25% ante 3,67%), mas seguindo em território modesto — nada perto de extremo
histórico (sem série de percentil disponível para calibrar, ver Honestidade).

**A curva forward (07/07/2026)** mantém contango moderado, sem sinal de estresse:

| Vencimento | Código | Preço (cts/bu) | Var. vs Ago |
|---|---|---|---|
| Julho/26 | N26 | 1.181,50 | −4,75 |
| Agosto/26 | Q26 | 1.186,25 | — (spot) |
| Setembro/26 | U26 | 1.182,50 | −3,75 |
| Novembro/26 | X26 | 1.193,50 | +7,25 |
| Janeiro/27 | F27 | 1.207,75 | +21,50 |
| Março/27 | H27 | 1.209,75 | +23,50 |

Contango de +23,50 cts (+2,0%) de agosto a março/27 — dentro do custo de carregamento
normal, a curva não "grita" escassez apesar dos dois dias seguidos de alta.

**Os forecasts estatísticos internos (07/07/2026, recalibrados)** mostram: central 7d =
**1.190,75 cts/bu** (bandas 1.130,79-1.250,71), viés **lateral** — praticamente igual ao
fechamento de hoje, ou seja, o modelo já trata o nível pós-rompimento como o centro esperado
da próxima semana, não como ponto de partida para mais alta imediata. Já o central 30d =
**1.218,97 cts/bu** (bandas 1.094,83-1.343,11), viés **altista** — a assimetria de alta
aparece apenas no horizonte de um mês.

### O que invalida / risco para a soja

- **Volume de confirmação fraco (3.640 contratos hoje vs 23.412 ontem no farelo):** se o
  próximo pregão reverter para baixo de 1.180,00 em volume também fraco, o rompimento de dois
  dias vira um "double top" técnico, não uma tendência.
- **O forecast de 7d (central 1.190,75, já "lateral") se confirmar:** quem compra agora está
  na mediana do próprio modelo, não abaixo dela — trade de convicção fundamentalista
  (calor + China), não de momentum estatístico.
- **WASDE de julho (~10/07/2026) reverter a leitura de "oferta grande":** cai na mesma semana
  do vencimento da MP 1.358 (ver Riscos).
- **A condição de lavoura (64% bom-ou-melhor, 05/07) piorar mais nas próximas semanas de
  calor:** o relatório semanal seguinte é o teste direto da manchete de "U.S. heat".
- **O básis físico positivo em Paranaguá (+R$ 3,88/sc sobre a paridade) se dissipar:**
  confirmaria que foi um efeito pontual de defasagem entre CBOT fresco e físico de um dia
  atrás, não demanda estrutural.

### Leitura operacional — soja

O rompimento de 1.180,00 tem agora dois fechamentos a favor, mas veio acompanhado de queda
sensível no volume do complexo — sinal técnico de que a continuidade ainda não tem
participação forte por trás. Para quem opera o papel, o forecast de 7 dias do próprio sistema
já embute o nível de hoje como "central": comprar agora é apostar contra a mediana de curto
prazo do modelo, um trade fundamentado em notícia (calor + China + básis físico positivo),
não em momentum estatístico. Para quem tem física para fixar, o básis de Paranaguá pagando
prêmio sobre a paridade teórica (R$ 139,01 vs R$ 135,13) é a melhor janela de venda à vista
documentada nesta série de leituras — vale considerar fixação parcial enquanto esse prêmio
persistir. O gatilho que decide os próximos dias é duplo: (1) se o volume voltar a crescer
sustentando o nível, e (2) o WASDE de julho (~10/07), que cai na mesma semana do vencimento
da MP 1.358.

---

## Farelo

**Viés: bear estrutural CONFIRMADO — ratio Far/Soj fechou em 79,28% pelo SEGUNDO pregão
consecutivo (06/07 e 07/07), satisfazendo pela primeira vez o protocolo de confirmação da
tese de 11/06/2026 (2-3 fechamentos consecutivos abaixo de 80%), tratando a fila
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, agora D+26; mas o
forecast de 30 dias do próprio farelo virou de lateral para altista no mesmo dia**

### Tratando a fila `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`

A pergunta que a fila cobra: "ratio fechou <80%? WASDE mudou o quadro? NOPA confirmou
crush?" **Resposta: sim ao primeiro, parcialmente aos outros dois.** A trajetória completa
do ratio, agora com o segundo fechamento confirmando a compressão:

| Data-base | Ratio Far/Soj | Evento |
|---|---|---|
| 11/jun | 81,4% | origem da tese |
| 01/jul | 80,82% | recuando, ainda acima de 80% |
| 02/jul | 80,66% | a 0,66 p.p. do gatilho |
| 03-05/jul | sem sessão | mercado fechado (feriado + fim de semana) |
| 06/jul | **79,28%** | primeiro fechamento abaixo de 80% |
| **07/jul** | **79,28%** | **segundo fechamento seguido abaixo de 80% — CONFIRMA** |

O protocolo original de 11/06/2026 (documentado em
[[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]) definia o gatilho como "ratio
sustentado abaixo de 80% por 2-3 pregões consecutivos". Hoje esse critério é satisfeito: dois
fechamentos seguidos em 79,28%. **O WASDE ainda não mudou o quadro** (o próximo é ~10/07,
ainda não saiu) e **a NOPA segue sem confirmar nada** (fila `release-nopa-2026-07-07`,
`monthly_status: 0,0 bool`, inacessível por exigir membership pago — mesma lacuna de mais de
um mês, ver Honestidade). Ou seja: a confirmação vem puramente do preço relativo (ratio),
ainda sem o respaldo direto de um dado de esmagamento americano fresco.

**Por que o ratio ficou parado exatamente em 79,28% hoje, em vez de comprimir mais:** o
mecanismo de ontem foi divergência (soja subiu proporcionalmente mais que o farelo durante o
gap do feriado: soja +4,2% de 1.136,25 para 1.184,00 contra farelo +2,4% de 305,50 para
312,90). **Hoje o mecanismo é outro: farelo e soja subiram no mesmo ritmo** (farelo 312,90 →
313,50, +0,19%; soja 1.184,00 → 1.186,25, +0,19%) — por isso o ratio não comprimiu mais, mas
também não reverteu. O fato relevante é que ele **sustentou** o nível comprimido de ontem em
vez de corrigir para cima, que é exatamente o comportamento que separa uma confirmação real
de um "quase rompe e volta" (como já ocorreu em 29/06, quando o ratio foi de 80,30% para
81,43% em três dias).

**A crush margin está em 2,509 USD/bu** (Board Crush: farelo 313,50 + óleo 67,95 − soja
1.186,25; indicadores, 07/07/2026), uma leve alta de +0,46% frente aos 2,4974 de ontem — mas
o quadro de cinco sessões é de compressão: 2,8056 (30/jun) → 2,72 (01/jul) → 2,7032 (02/jul)
→ 2,4974 (06/jul) → **2,509 (07/jul)**, uma queda acumulada de **-10,6%** em relação à ponta
de 30/06. A leve alta de hoje não reverte a tendência, apenas estabiliza perto da mínima do
ciclo — vale monitorar se a esmagadora começa a reduzir ritmo caso a compressão volte a
acelerar (o que tiraria oferta de farelo do mercado, contrapondo o próprio bear estrutural).

**As praças físicas de farelo no Brasil (NAG, 06/07/2026)** seguem em padrão morno: MT/IMEA
em R$ 1.554,53/ton (estável, var 0,0%), Rondonópolis em R$ 1.550,00/ton (+3,33% frente a
1.500,00), RS em R$ 1.640,00/ton (estável). O prêmio de exportação do farelo em Paranaguá
segue em **+0,05 USD/sht** (mês de referência julho/26) — praticamente nulo, confirmando que
o Brasil ainda não tem vantagem de preço para exportar farelo (Argentina com colheita 98%
concluída, oferecendo concorrência plena).

**Os dados projetados da ABIOVE (sem alteração desde a leitura anterior)** continuam
mostrando a exportação de farelo brasileiro recuando pela metade entre agosto e
dezembro/2026: 1.400 → 1.100 → 850 → 800 → **700 mil t**, sem queda proporcional no estoque
final projetado (1.224 → 1.016 → 1.100 → 1.101 → 1.015 mil t) — o mecanismo já detalhado na
leitura de ontem ([[2026-07-06_leitura-complexo]]) segue intacto: menos saída pelo porto
empurra o excedente de farelo para o mercado interno de ração, que não tem elasticidade
suficiente para absorver toda a queda de exportação, pressionando o preço doméstico — coerente
com a compressão do ratio confirmada hoje.

**A curva forward do farelo (07/07/2026)** mantém a mesma forma, com outubro seguindo o
vencimento mais fraco:

| Vencimento | Código | Preço (USD/sht) | Var. vs Ago |
|---|---|---|---|
| Julho/26 | N26 | 315,80 | +2,30 |
| Agosto/26 | Q26 | 313,50 | — (spot) |
| Setembro/26 | U26 | 311,80 | −1,70 |
| Outubro/26 | V26 | 310,70 | −2,80 |
| Dezembro/26 | Z26 | 313,70 | +0,20 |
| Janeiro/27 | F27 | 315,00 | +1,50 |

Outubro (V26, 310,70) permanece o vencimento mais descontado — coincide com o pico sazonal de
esmagamento simultâneo Brasil + Argentina (ABIOVE projeta 2.846 mil t de esmagamento BR em
outubro, o maior mês do ano).

**O posicionamento dos fundos (COT, atualizado de 23/06 para 30/06/2026) é o dado mais
relevante desta leitura para o farelo.** O managed money net long **colapsou de +12.359 para
apenas +4.740 contratos (-61,6%)** — praticamente neutro. O mecanismo por trás não foi
liquidação de posição comprada (long caiu de 110.276 para 110.069, praticamente estável,
-0,2%), mas sim **construção ativa de posição vendida**: short subiu de 97.917 para
**105.329 contratos (+7,6%)**, agora representando 17,9% do open interest de 588.519. Isso é
um dado estruturalmente importante: os fundos estavam **ampliando a aposta baixista em
farelo antes mesmo de o ratio confirmar a compressão hoje** — o "dinheiro grande" já vinha na
direção que os fundamentos acabaram de validar. Isso também reduz o risco de "short squeeze"
que leituras anteriores apontavam como risco de cauda: uma posição vendida que cresce junto
com a confirmação do fundamento é mais defensável do que uma posição vendida isolada torcendo
contra o mercado.

**O forecast estatístico de 30 dias do farelo, no entanto, virou de lateral para altista no
mesmo dia da confirmação do ratio** — central 320,53 USD/sht (07/07, bandas 290,89-350,17,
viés altista) ante central 312,43 (06/07, viés lateral). Como o modelo é construído a partir
de média móvel de 20 dias + volatilidade + inclinação recente (não de fundamento), essa
virada provavelmente reflete a extrapolação estatística do rali dos últimos dois pregões, não
uma reavaliação do balanço físico. Ainda assim, é uma tensão real: o mesmo dia em que a tese
fundamentalista bearish se confirma é o dia em que o modelo estatístico de médio prazo vira
contra ela — um sinal de alerta que merece acompanhamento nas próximas 2-3 sessões antes de
tratar a confirmação do ratio como definitiva para o horizonte de 30 dias.

### O que invalida / risco para o farelo

- **O forecast de 30d ter virado para altista (320,53) no mesmo dia da confirmação do ratio:**
  tensão direta com a tese estrutural, mesmo sem explicação fundamentalista — merece
  monitoramento nas próximas sessões.
- **Ratio reverter para cima de novo:** já ocorreu em 29/06 (de 80,30% para 81,43% em três
  dias); hoje precisaria de uma reversão maior (a partir de 79,28%) para repetir o padrão.
- **Crush margin continuar comprimindo abaixo de 2,40 USD/bu:** hoje em 2,509, ainda perto da
  mínima do ciclo — se cair mais, a esmagadora pode reduzir ritmo, tirando oferta de farelo.
- **WASDE de julho (~10/jul) reduzir a área de soja americana de forma expressiva:** menos
  esmagamento no 4T26 → menos farelo global, risco de aperto mesmo com os fundos agora mais
  vendidos (105.329 contratos).
- **Estoque doméstico de farelo projetado pela ABIOVE não desinchar como a queda de
  exportação sugere:** reforça pressão, não alivia.

### Leitura operacional — farelo

A tese nascida em 11/06/2026 está, pela primeira vez, formalmente confirmada nesta leitura:
dois fechamentos consecutivos do ratio Far/Soj abaixo de 80%, satisfazendo o protocolo
original — tratando o checkpoint D+7 vencido (fila `revisao-2026-06-11_ratio-81-prepara-
janela-de-tranches-farelo-D+7`) como encerrado com confirmação. Para quem opera o spread de
convergência (long farelo/short soja, ou o crush completo), a régua sobe de "aguardar
confirmação" para "tese validada, gerenciar continuidade" — os fundos já estão posicionados
na mesma direção (short crescente em farelo), o que reduz o risco de squeeze mas também
significa que parte do movimento já pode estar precificada. O contraponto que exige atenção
imediata é o forecast de 30d virando altista no mesmo dia: não é motivo para desmontar a
tese, mas é motivo para não aumentar posição de forma agressiva sem ver as próximas 2-3
sessões confirmarem que o ratio continua abaixo de 80% e que o forecast não segue subindo.
Para quem já está posicionado no short estrutural de farelo em preço absoluto, referência de
stop em 315-317 USD/sht (ajustada levemente para cima acompanhando o rali dos últimos dois
dias).

---

## Óleo

**Viés: bear tático confirmado — fechamento de 67,95 cts/lb segue abaixo do suporte-virou-
resistência 72,00 (fila `alerta-quebra_suporte-oleo_cbot-2026-07-07`), agora sem recuperar
por mais de duas semanas mesmo com dois pregões seguidos de rali no complexo; margem de
biodiesel comprimiu no dia mas mantém folga maior sobre o piso do que leituras anteriores
sugeriam**

### Tratando a fila `alerta-quebra_suporte-oleo_cbot-2026-07-07`

O óleo de agosto (ZLQ26.CBT) abriu em 67,70, fez máxima de 68,47, mínima de 67,64 e fechou em
**67,95 cts/lb** (CBOT CME, 07/07/2026, volume 3.434 contratos) — uma alta de **+0,19 cts
(+0,28%)** frente ao fechamento de ontem (67,76, via recálculo dos indicadores), participando
do rali do complexo pelo segundo dia seguido, mas **sem recuperar o suporte de 72,00**, que
segue funcionando como resistência. A pergunta operacional da fila — confirma ou muda a tese?
— **confirma**: o óleo está **5,63% abaixo** do nível de 72,00, e o segundo dia seguido de
alta do complexo não foi suficiente para sequer testar essa resistência — sinal de força
relativa negativa persistente.

**A margem de biodiesel americano comprimiu para 0,5612 USD/galão** (indicadores, 07/07/2026:
receita 6,4574 = HO 3,2924 + 1,5×RIN 2,11; custo 5,90 = óleo 5,0962 + industrial 0,80), uma
queda de -3,5% frente aos 0,5814 de ontem. O mecanismo: o custo do óleo subiu (+0,28%,
acompanhando o CBOT) enquanto o heating oil (a receita) recuou levemente, de 3,2984 para
**3,2924 USD/galão (-0,18%)** — como a margem é receita menos custo, e o custo subiu mais que
a receita, a margem aperta. **Olhando a janela de uma semana, porém, o quadro é de oscilação,
não de tendência limpa**: 0,6621 (30/jun) → 0,5811 (01/jul) → 0,5395 (02/jul) → 0,5814
(06/jul, recuperação) → **0,5612 (07/jul)** — a margem tem oscilado entre 0,54 e 0,66 na
última semana, dentro da faixa de conforto de 0,50-0,80 USD/gal já documentada em leituras
anteriores, sem romper o piso. **Nota de transparência:** a leitura de ontem
([[2026-07-06_leitura-complexo]]) havia registrado a margem de 06/07 em 0,5156 USD/gal (o
"nível mais baixo desde 29/06"); o dump de hoje, ao recalcular a mesma data de 06/07, mostra
0,5814 — um valor mais alto e menos alarmante. Não há como reconciliar essa diferença com os
dados disponíveis (ver Honestidade #1); esta leitura usa os números do dump de hoje como
referência, o que significa que a margem de biodiesel está com mais folga sobre o piso do que
a narrativa de ontem sugeria.

**A curva forward do óleo (07/07/2026)** mantém backwardation clara mesmo após dois dias de
alta:

| Vencimento | Código | Preço (cts/lb) | Var. vs Ago |
|---|---|---|---|
| Agosto/26 | Q26 | 67,95 | — (spot) |
| Setembro/26 | U26 | 67,57 | −0,38 |
| Outubro/26 | V26 | 67,05 | −0,90 |
| Dezembro/26 | Z26 | 66,74 | −1,21 |
| Janeiro/27 | F27 | 66,68 | −1,27 |

A curva caindo -1,27 cts/lb (-1,9%) de agosto a janeiro/27 segue sendo o argumento técnico
mais forte para manter posição vendida de médio prazo: quem rola a posição mês a mês colhe
esse carry independentemente da direção do preço à vista.

**O posicionamento dos fundos (COT, atualizado de 23/06 para 30/06/2026)** mostra
de-risking real da posição comprada, ainda que anterior ao rali desta semana: managed money
net long caiu de **+103.206 para +91.946 contratos (-10,9%)**, com long recuando -3,5% (de
132.666 para 128.014) e short subindo **+22,4%** (de 29.460 para 36.068). Como fração do open
interest (630.035, também em queda de -4,4% frente a 658.976), o net long caiu de 15,7% para
14,6%. Isso mostra que os fundos já vinham reduzindo a maior exposição relativa das três
pernas do complexo antes mesmo do rali dos últimos dois dias — o que **reduz, mas não
elimina**, o risco de liquidação forçada de posição comprada se o óleo voltar a cair. Sem COT
mais fresco (a atualização de 30/06 ainda não captura a reação dos fundos ao rali de 06-07/07),
não é possível confirmar se eles aproveitaram a alta recente para reduzir ainda mais a
posição ou se pausaram o movimento.

**O Índice de Suporte do Óleo (ISO) permanece em 100/100 (5/5 condições)**, o oitavo pregão
seguido nesse patamar desde a virada de 01/07 (indicadores, 07/07/2026) — reforçando a
hipótese, já tratada em leituras anteriores, de efeito calendário na virada de junho para
julho (ver Honestidade #4, e [[2026-07-06_leitura-complexo]] para a derivação completa).

**O pano de fundo regulatório global segue inalterado desde 05/06/2026**
(`system/tributario_watch.toml`, sem novos `atualizado_em`): o EPA Final RFS 2026/2027 (BBD
8,86→9,07 bi RINs, +61% a/a) sustenta o RIN D4 e o óleo doméstico americano; o crédito 45Z
(Clean Fuel Production), em tramitação, tende a excluir insumo importado da elegibilidade,
reforçando demanda por óleo doméstico americano; e a Indonésia mantém a exportação de palma
centralizada via Danantara (desde 01/06, assunção plena prevista para 01/09/2026) mais o levy
de exportação de CPO de até 12,5% (PMK 9/2026) — ambos encarecendo a palma e favorecendo o
óleo de soja por substituição, mas sem poder ser quantificado porque o MPOB segue inacessível
há 22 dias consecutivos (ver Honestidade #4).

### O que invalida / risco para o óleo

- **Margem de biodiesel cair abaixo de 0,50 USD/gal:** hoje em 0,5612, com folga de 0,06 sobre
  o piso — menos urgente que a leitura anterior sugeria, mas ainda o item de maior
  sensibilidade tática de curto prazo.
- **Heating oil não acompanhar uma eventual continuação de alta do óleo de soja:** se o óleo
  subir mais rápido que o HO de novo, a margem aperta mais.
- **RIN D4 real acima de 2,40 USD/RIN** (o modelo usa 2,11 fixo): incerteza estrutural
  bidirecional, sem novo dado hoje.
- **Dados de palma malaia (MPOB) inacessíveis há 22 dias consecutivos** — se a produção de
  palma estiver caindo por El Niño ou pelas restrições indonésias, o óleo de soja ganharia
  prêmio de substituição global, o que seria altista.
- **WASDE de julho reduzir a área de soja americana:** menos esmagamento futuro nos EUA →
  menos óleo produzido → altista para os contratos de novembro em diante.
- **Exportação de óleo brasileiro projetada pela ABIOVE em queda** (110 mil t setembro → 45
  outubro → 21 novembro) — mais óleo represado internamente (bearish doméstico) ou mais
  disponibilidade para o mandato B15 (efeito ambíguo).

### Leitura operacional — óleo

O viés segue bear tático, com a quebra do suporte 72,00 confirmada por mais um dia mesmo com
o complexo em alta pelo segundo pregão seguido — força relativa negativa que reforça, não
contesta, a tese. A margem de biodiesel comprimiu no dia (0,5612) mas está com mais folga
sobre o piso de 0,50 do que a narrativa de ontem sugeria — reduz a urgência tática desse
gatilho específico por ora, sem eliminá-lo do radar. O carry negativo da curva forward
(-1,27 cts/lb agosto→janeiro/27) segue favorecendo posição vendida de médio prazo, com
referência de stop em 69,50-70,50 cts/lb. As zonas-alvo dos forecasts seguem válidas: central
7d em 65,64 (bandas 61,79-69,48) e central 30d em 57,52 (bandas 49,56-65,48) — a assimetria
de baixa mais profunda aparece no horizonte de um mês. Para quem opera o oil share (hoje em
52,01%, estável), o viés estrutural segue favorecendo manter exposição ao óleo dentro do
crush frente ao farelo — a dominância relativa (ISO 100/100) é uma dimensão distinta do
nível de preço isolado ou da margem de biodiesel.

---

## Spreads e crush — leitura de complexo

### Crush margin: 2,509 USD/bu — estabiliza perto da mínima do ciclo, após -10,6% em cinco sessões

A crush está em **2,509 USD/bu** (Board Crush: farelo 313,50 + óleo 67,95 − soja 1.186,25;
indicadores, 07/07/2026), uma leve alta de +0,46% frente aos 2,4974 de ontem, mas ainda
próxima da mínima do ciclo recente: 2,8056 (30/jun) → 2,72 (01/jul) → 2,7032 (02/jul) →
2,4974 (06/jul) → 2,509 (07/jul), uma compressão acumulada de -10,6% em cinco sessões. Vale
monitorar se a estabilização de hoje é o início de um piso ou apenas uma pausa antes de nova
queda — se a compressão retomar, pode começar a desestimular o ritmo de esmagamento nas
próximas semanas, o que tiraria oferta física de farelo e óleo simultaneamente do mercado.

### Ratio Far/Soj: 79,28% — CONFIRMADO por dois fechamentos seguidos abaixo de 80%

Como detalhado na seção de Farelo, o ratio sustentou hoje o nível de compressão atingido
ontem, satisfazendo pela primeira vez o protocolo de confirmação da tese de 11/06 (2-3
fechamentos consecutivos abaixo de 80%). É o desenvolvimento estrutural mais importante da
série desde a origem da tese, tratando a fila
`revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`.

### Oil share: 52,01% — estável

O oil share está em 52,01%, praticamente igual aos 51,99% de ontem e à faixa de 52,0-52,2% da
última semana — o óleo segue dominando o crush (>50%), sem sinal de mudança estrutural.

### Oil-meal spread: 0,5775 USD/bu — leve alta

O oil-meal spread (contribuição do óleo menos a do farelo por bushel) subiu para 0,5775 ante
0,5698 de ontem — óleo ampliando ligeiramente sua vantagem relativa dentro do crush.

### ISF em 80/100, ISO em 100/100 — oitavo pregão seguido no mesmo patamar

O Índice de Sobra de Farelo (ISF) está em 80/100 (4/5 condições) e o Índice de Suporte do
Óleo (ISO) em 100/100 (5/5) — o mesmo patamar desde 01/07/2026, agora o oitavo pregão
consecutivo. A estabilidade reforça a hipótese de efeito calendário na virada de ISF/ISO
ocorrida na virada do mês de junho para julho (ver Honestidade #4).

### O que os índices dizem juntos em 07/07/2026

ISF 80/100 + ISO 100/100 (ambos estáveis, efeito calendário) + ratio Far/Soj confirmado abaixo
de 80% por dois fechamentos seguidos (tese de 25 dias validada) + oil share 52,01% (estável) +
oil-meal spread 0,5775 (leve alta) + crush estabilizando perto da mínima do ciclo (-10,6% em
cinco sessões) + margem de biodiesel oscilando dentro da faixa de conforto (0,5612, sem
romper piso) + COT de 30/06 mostrando fundos já reduzindo long em óleo (-10,9%) e ampliando
short em farelo (+7,6%) antes da confirmação do ratio + soja rompendo 1.180 pela segunda vez
seguida em volume mais fraco:

A leitura de hoje é de **confirmação estrutural do bear-farelo, mantendo o bear-óleo tático
intacto, com o bull-soja tático dependente de continuidade de volume.** O desenvolvimento
central da série (o ratio cruzando e sustentando abaixo de 80%) finalmente aconteceu, com o
respaldo adicional de que os fundos já vinham se posicionando na mesma direção antes da
confirmação — um alinhamento raro entre preço relativo, fundamento de balanço (ABIOVE) e
posicionamento especulativo. O contraponto que evita excesso de confiança é o forecast de 30d
do farelo virando altista no mesmo dia — um lembrete de que o modelo estatístico e a leitura
fundamentalista podem divergir, e de que a régua de gestão de risco não deve relaxar só
porque a tese "confirmou".

---

## Lente fiscal e regulatória BR

**MP 1.358/2026 — subvenção à gasolina (R$ 0,89/L) e diesel (R$ 0,35/L) — vence em 4 dias
(11/07/2026, fila `trib-MP-1358-2026-2026-07-11`).** A MP ressarce PIS/Cofins/Cide da
gasolina e do diesel, mantendo o combustível fóssil artificialmente mais barato — o mesmo
espírito da MP 1.363/2026 (subsídio de R$ 1,12/L ao diesel, vigente até 31/12/2026, já
tratada em [[2026-05-26_subvencao-fossil-aperta-biodiesel]]). O próximo marco é a
**deliberação da comissão mista**, travada em regime de urgência desde 27/06/2026
(`system/tributario_watch.toml`, evento MP-1358-2026, `atualizado_em` 05/06/2026, sem
mudança de status desde então) — ou o Congresso delibera e converte (ou rejeita) a MP até
11/07, ou ela caduca por decurso de prazo. O mecanismo de transmissão para o complexo soja é
indireto mas real: enquanto o combustível fóssil segue subsidiado, a competitividade
relativa do biodiesel dentro do mix B15 mandatório permanece pressionada — se o diesel
mineral fica mais barato via subvenção, o biodiesel não ganha proporcionalmente, e a
indústria de biodiesel (maior consumidora industrial de óleo de soja no Brasil) segue com
margem mais apertada do que teria sem a subvenção ao concorrente fóssil. **Este marco cai na
mesma semana do WASDE de julho (~10/07)** — dois catalisadores relevantes concentrados no
mesmo intervalo de dias. Se a MP 1.358 caducar sem conversão em lei, é um sinal (fraco, mas
real) de que o pacote pró-fóssil pode perder fôlego político — levemente positivo para a
competitividade do biodiesel e, por extensão, para a demanda industrial de óleo de soja; se
for convertida, reforça o quadro de pressão já documentado desde maio.

**Isenção PIS/Cofins biodiesel — vencimento em 31/07/2026, 24 dias.** Sem sinalização
pública do MAPA ou MINFRA sobre renovação até hoje (`system/tributario_watch.toml`, evento
PISCOFINS-BIODIESEL-ISENCAO, sem mudança). O checkpoint D+45 desse insight (10/07/2026,
[[2026-05-26_pis-cofins-biodiesel-explica-mercado-fisico-fraco]]) cai em 3 dias, coincidindo
com o WASDE e com o vencimento da MP 1.358 — a semana de 06-11/jul concentra três marcos
relevantes ao mesmo tempo.

**B16 — sem data, travado em B15.** Sem mudança de status desde a última leitura (evento
B16-CNPE-2026, status "adiado", sem `proximo_data`).

**MP 1.363/2026 (subsídio ao diesel fóssil) — em vigor até 31/12/2026.** Sem alteração.
Bearish estrutural persistente para a demanda incremental de óleo de soja no mercado
doméstico brasileiro.

**STJ REsp 2.165.276/2026 — crédito PIS/Cofins para esmagadoras.** Sem alteração. Bullish
para a soja/óleo (alívio de custo de entrada para biodiesel) e, por extensão, incentivo a mais
esmagamento — coerente com mais oferta de co-produtos, reforçando a leitura bearish do
farelo.

**Câmbio (PTAX) segue com defasagem normal de um dia** — o último dado oficial (06/07/2026,
5,1670 BRL/USD) mostra o real em quarta sessão seguida de apreciação, o que já foi tratado na
seção de Soja como resolução da divergência flagrada ontem entre a manchete de "dólar em
alta" e a série oficial (ver também Honestidade #2).

**Pano de fundo regulatório global (EUA e Indonésia) segue dando suporte estrutural ao óleo,
sem contradizer o viés bearish tático** — detalhado na seção Óleo.

---

## Riscos e eventos próximos

**WASDE de julho — ~10/07/2026 (3 dias).** Primeiro WASDE do mês, coincide com o vencimento
da MP 1.358 e o checkpoint D+45 da tese PIS/Cofins — rara concentração de catalisadores na
mesma semana.

**Vencimento da MP 1.358/2026 — 11/07/2026 (4 dias), fila `trib-MP-1358-2026-2026-07-11`.**
Deliberação da comissão mista é o marco a monitorar.

**Isenção PIS/Cofins biodiesel — vencimento 31/07/2026 (24 dias).** Sem sinalização de
renovação até agora.

**COT CFTC — dado de 30/06/2026 ainda não captura a reação dos fundos ao rali de 06-07/07.**
A próxima atualização é o teste real de como o "dinheiro grande" reagiu à confirmação do
ratio e ao rompimento da soja.

**Forecast de 30 dias do farelo virou de lateral para altista no mesmo dia da confirmação do
ratio — monitorar se essa virada se mantém ou reverte nas próximas 2-3 sessões** antes de
tratar a confirmação da tese bear-farelo como definitiva para o horizonte de um mês.

**USDA Crop Progress — próximo relatório semanal é o teste direto da narrativa de "calor nos
EUA" que sustentou parte do rali da soja.**

**NOPA — segue inacessível (fila `release-nopa-2026-07-07`), 22º dia sem crush americano
confirmado por fonte primária.**

**MPOB — 22 dias consecutivos sem números de palma extraídos**, mantendo cego o efeito da
Indonésia e do El Niño sobre o prêmio de substituição do óleo de soja.

**Margem de biodiesel em 0,5612 USD/gal — dentro da faixa de conforto, mas ainda o item de
maior sensibilidade tática de curto prazo do óleo.**

---

## Honestidade

O que não foi possível validar neste briefing de 07/07/2026, onde a confiança é baixa ou há
lacunas materiais:

**1. Discrepância entre os valores de 06/07/2026 reportados pela leitura de ontem e os
valores da mesma data recalculados no dump de hoje.** A leitura de 06/07
([[2026-07-06_leitura-complexo]]) registrou soja em 1.167,25 cts/bu, farelo em 311,40
USD/sht, óleo em 67,98 cts/lb e margem de biodiesel em 0,5156 USD/gal para aquele dia. O dump
de hoje, ao recalcular a mesma data (06/07/2026) via indicadores, mostra soja em 1.184,00,
farelo em 312,90, óleo em 67,76 e margem de biodiesel em 0,5814 — valores sensivelmente
diferentes. Esta leitura **não tem acesso ao banco de dados subjacente** para investigar a
causa (possivelmente correção de settle após publicação inicial, ou diferença entre preço
intradiário e fechamento oficial). Optou-se por usar os números do dump de hoje como
referência para todas as comparações dia-a-dia desta leitura, por serem internamente
consistentes entre si — mas isso significa que qualquer variação percentual "07/07 vs 06/07"
citada aqui carrega essa incerteza de base, e a magnitude exata dos movimentos recentes deve
ser tratada com cautela redobrada até o padrão ser entendido.

**2. Câmbio (PTAX) com defasagem normal de um dia (06/07 vs CBOT de 07/07).** Menor que os
gaps de três dias vistos na reabertura pós-feriado, mas ainda significa que a paridade em
reais de hoje (R$ 135,13/saca) combina CBOT fresco com câmbio de ontem — normal para o fluxo
T+1 do BCB, mas relevante para quem faz leitura fina de paridade no mesmo dia.

**3. COT com defasagem de uma semana em relação ao rali de 06-07/07/2026.** O dado mais
recente (30/06/2026) mostra os fundos reduzindo long em óleo e ampliando short em farelo,
mas não captura a reação a esta semana — a magnitude exata do "alinhamento" entre
posicionamento e fundamento discutido nesta leitura é inferida do dado mais recente
disponível, não confirmada para a semana corrente.

**4. Palma malaia (MPOB) — 22 dias consecutivos sem dados numéricos** (16/jun a 07/07/2026).
O parser continua retornando apenas ~3.430 chars de HTML sem valores extraídos. Sem os preços
de CPO na BMD, não é possível quantificar o efeito do El Niño nem das restrições
regulatórias indonésias sobre a produção e o prêmio de substituição para o óleo de soja
americano.

**5. NOPA — dado inacessível há mais de um mês** (fila `release-nopa-2026-07-07` tratada
aqui). `monthly_status = 0,0 bool` (indicadores, 07/07/2026). O esmagamento americano de
junho/2026 segue sem fonte primária acessível.

**6. A atribuição da virada do ISF/ISO ao efeito calendário ABIOVE não pôde ser confirmada por
consulta direta ao banco de dados.** O ambiente de execução deste insight não tem acesso ao
banco SQLite do sistema (apenas ao dump `briefing/latest.md`), então a conclusão de que a
rolagem do mês de referência (junho→julho) é a causa da inversão dos índices — reforçada hoje
pela estabilidade do novo patamar por oito pregões seguidos — é uma inferência lógica bem
fundamentada, mas não uma verificação direta do código.

**7. RIN D4 como parâmetro fixo (2,11 USD/RIN) segue sendo a maior fonte de incerteza do
modelo de biodiesel.** Não há dado de mercado secundário no briefing para confirmar se o
valor real mudou, apesar do EPA Final RFS ter elevado os volumes obrigatórios desde 15/06.

**8. Percentis históricos de COT não calculados** — os 91.946 net longs em óleo, 4.740 em
farelo (com 105.329 shorts) e 38.149 em soja são lidos apenas em nível absoluto e como fração
do open interest corrente, sem série histórica completa para calibrar se estão em zona
extrema.

**9. BCBA Argentina — sem relatórios de esmagamento/exportação acessíveis via scraper**
(page_fetched=1,0 mas sem links de relatório, 06/07/2026). O ritmo de processamento
argentino pós-colheita (50,1 mi t) é estimado por notícia, não medido por fonte primária.

**10. Dados de clima INMET (BR) não foram usados como driver desta leitura.** Julho é
entressafra da soja brasileira (colheita já concluída, plantio só em outubro) — as
temperaturas de Cascavel/PR, Cuiabá/MT, Sinop/MT etc. no dump são monitoramento de rotina,
sem relevância direta para a tese de preço da soja/farelo/óleo neste momento do calendário
agrícola; por isso não aparecem como driver nas seções acima.

*Nenhum número foi inventado ou estimado além do que consta no briefing de 07/07/2026 e nos
insights anteriores referenciados. A maior contribuição desta leitura foi identificar que o
ratio Far/Soj sustentou a compressão abaixo de 80% por um segundo fechamento consecutivo,
satisfazendo o protocolo de confirmação da tese de 11/06 pela primeira vez em 26 dias — e
documentar, com a mesma transparência, que o forecast estatístico de 30 dias do farelo virou
contra essa mesma tese no dia da confirmação, um contraponto que exige acompanhamento antes
de tratar o caso como encerrado.*
