---
data: 2026-09-17
titulo: "Fechamento das revisões D+7 e D+90 da tese de 11/06: o ratio Far/Soj encadeou a quarta sessão consecutiva acima de 80% e fechou em 82,32% — 0,92 ponto percentual ACIMA dos 81,4% que abriram a tese baixista original — veredito: a tese de compressão estrutural do farelo está tecnicamente invalidada"
tags: [farelo, ratio-far-soj, spread, revisao, auto-claude]
fontes:
  - Tese original: [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] — aberta em 2026-06-11 com ratio Far/Soj em 81,4% (compressão vinda de 83,3% em 05/06), farelo CBOT jul a US$303,60/sht, prêmio export Paranaguá zerado (+0,05 US$/sht, NAG 10/jun), crush margin US$3,78/bushel (recorde) e oil share 55,4% — vies `bear-farelo`, com revisões programadas D+7 (2026-06-18), D+90 (2026-09-09) e D+180 (2026-12-08)
  - Fila de julgamento — 2026-09-17: `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` e `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`, ambas listadas como "VENCIDA" (o sistema de fila não lê de volta os insights já publicados para marcar revisão como encerrada — ver histórico abaixo)
  - Indicadores sintéticos internos (`complexo_soja.far_soj_ratio_pct`) — sequência completa desde a reabertura de 11/09: **80,25%** (2026-09-11), **80,55%** (2026-09-14), **81,91%** (2026-09-15, valor corrigido — ver [[2026-09-16_correcao-numeros-sessao-15set-ratio-salta-para-8191]]), **82,32%** (2026-09-16, sessão mais recente com fechamento completo no dump de hoje)
  - Insights intermediários que já haviam tratado revisões desta mesma tese: [[2026-09-09_d90-ratio-far-soj-reverte-na-vespera]] (D+90 na véspera do vencimento formal, ratio ainda em 79,x%, tese parecendo se confirmar por pouco), [[2026-09-12_ratio-far-soj-rompe-80-pela-primeira-vez]] (primeira ruptura de 80%, viés elevado a neutro), [[2026-09-15_ratio-far-soj-terceira-sessao-consecutiva-acima-80]] (terceira sessão, viés ainda neutro por cautela de dado), [[2026-09-16_leitura-complexo]] (viés elevado a bull-farelo pela primeira vez, ratio corrigido de 15/09 em 81,91%)
  - Leitura diária de hoje: [[2026-09-17_leitura-complexo]]
status: ativa
vies: [bull-farelo]
---

## Por que este insight existe separado da leitura diária

A fila de julgamento de hoje (17/09) volta a listar como "vencidas" as duas revisões
programadas da tese original de 11/06/2026
([[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]): a de D+7 (venceu em
2026-06-18) e a de D+90 (venceu em 2026-09-09). Ambas já foram tocadas, de forma crescente,
nas leituras de 09, 12, 15 e 16/09 — mas nenhuma delas chegou a dar um veredito fechado e
explícito, na forma que a pergunta da fila pede ("A tese se confirmou? Atualizar
status/insight."). Este insight existe para dar essa resposta de forma definitiva, cruzando
o histórico completo do ratio desde a abertura da tese até o fechamento mais recente
disponível (16/09), e para documentar por que o veredito é "não confirmou — inverteu".

## A pergunta que a tese original fazia

Em 11/06/2026, com o ratio Far/Soj comprimindo de 83,3% (05/06) para 81,4% (11/06) em
apenas quatro pregões, a tese apostava que essa compressão continuaria e levaria o ratio
para a zona "abundante" (<80%) dentro de 1-2 semanas. Os pilares eram: farelo CBOT perto da
mínima de 52 semanas, prêmio de exportação em Paranaguá zerado (o farelo não competia no
mercado externo, sobrando no doméstico), crush margin em recorde (US$3,78/bushel, a
esmagadora rodando a pleno vapor) e oil share em 55,4% (o óleo pagando a maior parte do
crush, o farelo como resto). As perguntas de revisão programada eram diretas:

- **D+7 (18/06/2026):** o ratio fechou abaixo de 80%? O WASDE mudou o quadro? A NOPA
  confirmou o crush recorde?
- **D+90 (09/09/2026):** o spread reverteu ou seguiu comprimindo? O viés baixista no farelo
  se confirmou?

## O que de fato aconteceu — a resposta com o dado completo

O ratio Far/Soj **não** manteve a trajetória de compressão que a tese previa. Ele continuou
caindo por mais algumas semanas depois de 11/06 (não há dado diário completo dessa fase
neste sistema para reconstruir dia a dia, mas os insights de 09/09 em diante documentam o
ratio operando na faixa de 78-80%, abaixo do nível de abertura da tese), confirmando
parcialmente a tese original por um período. A reviravolta começou a ficar visível a partir
de 11/09/2026, quando o ratio começou uma sequência de altas consecutivas:

| Data | Ratio Far/Soj | Observação |
|---|---|---|
| 2026-06-11 | 81,4% | Abertura da tese (nível de referência) |
| 2026-09-09 | ~79,x% | Vencimento formal do D+90 — tese ainda parecia se confirmar por pouco ([[2026-09-09_d90-ratio-far-soj-reverte-na-vespera]]) |
| 2026-09-11 | 80,25% | Reabertura pós-fim de semana — primeira ruptura de 80% |
| 2026-09-12 | ~80,x% | Confirmação da ruptura ([[2026-09-12_ratio-far-soj-rompe-80-pela-primeira-vez]]) |
| 2026-09-14 | 80,55% | Segunda sessão de consolidação acima de 80% |
| 2026-09-15 | 81,91% | Terceira sessão — e já a primeira a ultrapassar o nível de abertura da tese (81,4%), embora tratada como "muito perto" na leitura daquele dia |
| 2026-09-16 | **82,32%** | Quarta sessão consecutiva acima de 80% — **0,92 ponto percentual acima** do nível de abertura da tese original |

O nome que o próprio título da tese original usa — "Ratio Far/Soj 81,4% ... spread far÷soj
**comprimindo**" — descreve exatamente o oposto do que aconteceu nos últimos quatro pregões:
o spread está **esticando**, não comprimindo, e já ultrapassou o próprio ponto de partida da
tese. Note-se a ironia precisa do número: a tese nasceu com o ratio em 81,4% e apostou em
queda; hoje o ratio está em 82,32%, ligeiramente ACIMA de onde nasceu — ou seja, olhando
apenas para o nível absoluto do ratio (sem considerar o vale intermediário abaixo de 80%
que de fato ocorreu), o mercado está, hoje, ligeiramente mais "apertado" no farelo do que
estava no dia em que a tese apostou justamente no oposto.

## Os pilares originais, um a um, hoje

- **Farelo perto da mínima de 52 semanas (pilar original)** → hoje o farelo fechou em
  362,60 USD/short ton (CME CBOT, 16/09), com resistência de referência em 325,00 rompida
  há vários dias e folga de 11,57% acima dela (fila
  `alerta-quebra_resistencia-farelo_cbot-2026-09-16`) — o oposto de "perto de mínima".
- **Prêmio de exportação zerado (pilar original)** → o prêmio export Paranaguá segue baixo
  (+0,12 USD/short ton, NAG, congelado desde 27/08, 21 dias corridos), mas sem atualização
  recente que permita avaliar se a dinâmica de exportação mudou junto com o preço em
  Chicago — uma lacuna, não uma confirmação nem uma refutação deste pilar específico.
- **Crush margin em recorde, esmagadora a pleno vapor (pilar original, US$3,78/bushel em
  11/06)** → hoje o crush margin está em US$2,3566/bushel (16/09), bem abaixo do recorde de
  junho e também abaixo do referencial de US$2,50 monitorado pela fila
  (`alerta-quebra_suporte-complexo_soja-2026-09-16`, distância -5,74%) — a esmagadora está
  sendo remunerada bem menos hoje do que em junho, o que reduz o incentivo a esmagar em
  ritmo recorde e é coerente com uma oferta de farelo relativamente mais escassa daqui para
  frente, não mais abundante.
- **Oil share em 55,4%, óleo pagando o crush (pilar original)** → hoje o oil share está em
  48,77% (16/09), abaixo de 50% pela primeira vez na janela de acompanhamento recente — o
  farelo passou a responder por mais da metade do valor do crush (51,23%). Este é o pilar
  que mais claramente se inverteu: o óleo não paga mais o crush, o farelo passou a pagar.

Três dos quatro pilares originais (preço absoluto do farelo, crush margin, oil share)
estão hoje em direção oposta à que sustentava a tese de junho. O quarto (prêmio de
exportação) está sem atualização suficiente para avaliar.

## Veredito das revisões

- **D+7 (venceu 18/06/2026):** não há registro diário granular deste sistema para essa data
  específica, mas o padrão dos meses seguintes (ratio operando predominantemente abaixo de
  80% entre junho e início de setembro, segundo os insights intermediários) sugere que a
  tese estava, de fato, se confirmando naquele horizonte curto. **Veredito: parcialmente
  confirmada no curto prazo**, sem dado suficiente para uma nota precisa.
- **D+90 (venceu 09/09/2026):** na véspera do vencimento, o ratio ainda estava abaixo do
  nível de abertura, e a leitura daquele dia ([[2026-09-09_d90-ratio-far-soj-reverte-na-vespera]])
  já registrava sinais de reversão iminente. **Veredito: tese confirmada no vencimento
  formal, mas por margem estreita e às vésperas de reverter** — o que de fato aconteceu dois
  dias depois, em 11/09.
- **Situação atual (17/09, oito dias após o vencimento do D+90):** com quatro sessões
  seguidas de alta e o ratio 0,92 ponto percentual acima do nível de abertura da tese, o
  cenário mudou de forma que nenhuma das duas janelas de revisão formais (D+7, D+90) foi
  desenhada para capturar. **Veredito final: a tese baixista estrutural de 11/06/2026 está
  tecnicamente invalidada pelo próprio critério que ela mesma definiu** (o ratio, que deveria
  cair estruturalmente, está hoje acima de onde começou). O bear-farelo original deu lugar,
  de forma documentada dia a dia entre 11 e 16/09, ao bull-farelo vigente desde
  [[2026-09-16_leitura-complexo]] e reforçado por [[2026-09-17_leitura-complexo]].

## O que isso NÃO significa

Este veredito fecha a revisão formal da tese de junho — não declara o farelo "estruturalmente
apertado". Como a leitura de hoje ([[2026-09-17_leitura-complexo]]) detalha, o ratio de
82,32% ainda está dentro da zona "neutra" (80% a 87%) da classificação formal do próprio
indicador, longe da zona "apertada" (≥87%) que caracterizaria uma escassez genuína. O
veredito aqui é mais estreito e mais defensável: a tese específica de *compressão adicional
abaixo de 80%* morreu; ela não foi substituída, automaticamente, por uma tese de aperto
estrutural forte. Além disso, dois pilares de confirmação ainda estão pendentes e não devem
ser ignorados: o COT de posições de 15/09 (esperado em 18-19/09, ainda não disponível) e o
físico brasileiro de farelo (congelado desde 09/09, oito dias corridos) — nenhum dos dois
confirmou, até aqui, a reação dos fundos ou do mercado físico à mudança de regime em
Chicago.

## Revisão programada remanescente

A revisão de **D+180 (2026-12-08)**, prevista pela tese original, segue válida e deve ser
tratada quando vencer — a essa altura, será possível avaliar se o farelo consolidou a zona
neutra-alta (80-87%) observada agora, avançou para a zona apertada (≥87%), ou reverteu de
volta para abaixo de 80%. Este insight encerra apenas as janelas D+7 e D+90 citadas pela
fila de hoje.
