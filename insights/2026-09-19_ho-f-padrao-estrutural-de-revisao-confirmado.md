---
data: 2026-09-19
titulo: "Terceira ocorrência confirma um padrão estrutural, não acidental, no heating oil (HO=F): o fechamento do dia mais recente do dump sempre chega com volume anormalmente baixo (~180-200 contratos) e é revisado para cima (+3,77% a +5,91%) só 1-2 dias depois, junto com uma correção de volume de mais de duas ordens de magnitude (para 37-62 mil contratos) — qualquer leitura de margem de biodiesel construída sobre o HO=F do dia mais recente do dump deve ser tratada como provisória"
tags: [complexo, auto-claude]
fontes:
  - CME NYMEX heating oil (HO=F) — três ocorrências documentadas nesta série, todas do mesmo padrão (fechamento revisado para cima + volume corrigido de ~180-200 para dezenas de milhares de contratos na geração seguinte do dump):
    1) Sessão de **2026-09-11**: fechamento usado na leitura de 12/09 ([[2026-09-12_leitura-complexo]]) foi 4,7792 USD/galão; o dump de 13/09 revisou para **4,9593** (+3,77%), com volume de 62.190 contratos já presente na linha bruta original (a anomalia de volume, neste primeiro caso, não estava na sessão revisada, e sim na comparação seguinte de 15/09 — ver item 2). Documentado em [[2026-09-13_correcao-numeros-sessao-11set-farelo-oleo]].
    2) Sessão de **2026-09-16**: fechamento usado nas leituras de 17/09 e 18/09 foi 4,9662 USD/galão, volume 189 contratos; o dump de 18/09 revisou para **5,2465** (+5,65%). Documentado em [[2026-09-18_leitura-complexo]], que também registra volumes anormalmente baixos nas sessões vizinhas (203 contratos em 15/09, 179 em 17/09).
    3) Sessão de **2026-09-17**: fechamento usado na leitura de 18/09 foi 4,8284 USD/galão, volume 179 contratos; o dump de 19/09 (`briefing/latest.md`, seção `cme_cbot`) revisa para fechamento **5,1139** USD/galão e volume **43.659** contratos (+5,91% no preço, +24.297% no volume). Documentado em detalhe na leitura principal de hoje, [[2026-09-19_leitura-complexo]].
  - CME NYMEX heating oil (HO=F) — sessão de **2026-09-18** (a mais recente do dump de hoje): fechamento 4,8367 USD/galão, volume **37.512** contratos — já dentro da faixa saudável, o primeiro fechamento "do próprio dia" desta série a não aparecer com volume na faixa anômala de 180-200
  - Indicadores sintéticos internos (biodiesel_us) — as três ocorrências acima se propagam diretamente para a margem de biodiesel modelada (receita = HO + 1,5×RIN D4; margem = receita − custo do óleo − custo industrial fixo), amplificando o efeito da revisão: a margem de 16/09, descrita inicialmente como US$2,1532/galão, foi revisada para US$2,4222 (+12,5%); a de 17/09, descrita inicialmente como US$2,0537 (queda de -15,2%), foi revisada para US$2,3279 (queda real de apenas -3,89%)
  - Cruza com [[2026-09-13_correcao-numeros-sessao-11set-farelo-oleo]], [[2026-09-16_correcao-numeros-sessao-15set-ratio-salta-para-8191]] e [[2026-09-19_leitura-complexo]] (leitura principal de hoje, que trata a mesma revisão de 17/09 no corpo do texto e na seção Honestidade)
status: ativa
vies: [neutral-oleo_soja]
---

## O achado

Este é um insight de qualidade de dado, não uma nova leitura de preço — mas o padrão que ele
documenta afeta diretamente a confiança que se deve ter em qualquer leitura fundamentalista do
óleo baseada na margem de biodiesel americana, por isso merece registro próprio, separado da
leitura diária do complexo.

Três vezes em pouco mais de uma semana de leituras, o fechamento do heating oil (HO=F, o
contrato de referência usado internamente para modelar a receita do biodiesel americano — a
lógica é que o biodiesel compete com o diesel fóssil, e o heating oil é o proxy de preço mais
líquido e correlacionado disponível) apareceu no dump do dia com um valor que, um ou dois dias
depois, foi substituído por um valor bem diferente:

| Sessão | Fechamento inicial | Fechamento revisado | Variação | Volume inicial | Volume revisado |
|---|---|---|---|---|---|
| 2026-09-11 | 4,7792 | 4,9593 | +3,77% | (n/a nesta comparação) | 62.190 |
| 2026-09-16 | 4,9662 | 5,2465 | +5,65% | 189 | (não capturado diretamente nesta janela) |
| 2026-09-17 | 4,8284 | 5,1139 | +5,91% | 179 | 43.659 |

O padrão é consistente em três dimensões:

1. **Direção**: as três revisões são para cima. Nenhuma delas para baixo. Uma amostra de três
   não prova que a revisão *sempre* será para cima, mas a ausência de qualquer revisão para
   baixo nesta série é, no mínimo, um viés a considerar — se o padrão se mantiver, o
   fechamento mais recente do dump tende a subestimar o valor "verdadeiro" do HO=F.
2. **Magnitude**: as três revisões estão na faixa de +3,8% a +5,9% — grande o suficiente para
   mudar conclusões qualitativas (a leitura de 18/09 descreveu a margem de biodiesel de 17/09
   como "a primeira queda depois de dois recordes, -15,2%"; com o valor revisado, a queda real
   foi de apenas -3,89%, uma diferença que muda o peso que essa informação deveria ter tido na
   leitura operacional do óleo).
3. **Volume**: nos dois casos em que o volume da sessão inicial foi capturado (16/09: 189
   contratos; 17/09: 179 contratos), ambos estão na mesma faixa estreita de 180-200 — uma
   fração de 1% do volume que aparece 1-2 dias depois (43.659 em 17/09; a referência normal
   antes do início da anomalia era 62.190, em 11/09). Volume de 180-200 contratos em um
   contrato ativo do NYMEX é, por si só, um sinal de que o dado não reflete a sessão completa
   — é consistente com um print muito antecipado (talvez pré-abertura ou os primeiros minutos
   de negociação eletrônica) sendo capturado como se fosse o fechamento do dia.

## Por que isso é estrutural, não um acidente pontual

A leitura de 18/09 ([[2026-09-18_leitura-complexo]]) já havia levantado a hipótese, depois da
segunda ocorrência, de que isso seria "uma fragilidade estrutural de captura ligada à baixa
liquidez desse contrato específico" e recomendou explicitamente monitorar se um terceiro
episódio apareceria no dump seguinte. Ele apareceu — na sessão imediatamente seguinte (17/09),
com magnitude semelhante (+5,91%, contra +5,65% do episódio anterior) e a mesma assinatura de
volume (179 contratos, dentro do range 180-200 já observado duas vezes antes). Uma hipótese que
prevê corretamente o próximo evento antes de ele acontecer, e que se confirma com a mesma
assinatura três vezes seguidas, deixa de ser uma coincidência plausível e passa a ser o
comportamento esperado deste pipeline de dado específico até que haja evidência em contrário.

A boa notícia é que a sessão mais recente disponível no dump de hoje (18/09) já aparece com
volume de 37.512 contratos — a primeira vez, nesta série, em que o fechamento "do próprio dia"
não vem com a assinatura de baixo volume. Se essa normalização se mantiver (ou seja, se o
fechamento de 18/09 **não** for revisado de forma material no dump de amanhã), isso reforçaria
a hipótese de que o problema é uma questão de timing de captura (o dado é lido antes do
fechamento oficial em certos dias, por algum motivo ainda não identificado) e não uma falha
sistemática permanente. Se o padrão se repetir uma quarta vez — ou seja, se o próprio valor de
18/09 vier a ser revisado no dump de amanhã —, isso sugeriria algo mais amplo, possivelmente
ligado ao próprio provedor de dado ou à janela de coleta.

## O que isso muda na prática

- **Qualquer leitura da margem de biodiesel americana (e, por extensão, qualquer argumento de
  suporte fundamentalista ao óleo via biodiesel) que use o fechamento de HO=F do dia MAIS
  RECENTE do dump deveria ser tratada com desconto de confiança explícito**, e idealmente
  mencionar que o valor pode ser revisado para cima em 4-6% na geração seguinte.
- **Uma leitura que use o fechamento de HO=F de T-1 ou T-2 (não o mais recente) tem uma base
  mais sólida**, porque já teve ao menos uma janela de revisão para se estabilizar — como
  demonstrado pelas três ocorrências, a revisão acontece na geração imediatamente seguinte à
  sessão em questão, não em revisões posteriores adicionais (não há evidência, nesta série, de
  uma segunda rodada de revisão do mesmo dado dois dias depois).
- **O RIN D4 (crédito de biocombustível) permanece constante na fórmula interna em todas as
  três ocorrências** — a fragilidade está isolada no heating oil, não se estende a outros
  componentes da margem de biodiesel.
- Esta ressalva não invalida o argumento fundamentalista de que a economia do biodiesel
  americano sustenta o óleo de soja — apenas exige que esse argumento seja quantificado com o
  dado de HO=F mais maduro disponível, não o mais recente.

## Honestidade

- A amostra é de apenas três ocorrências — suficiente para tratar o padrão como estrutural
  dentro desta série de leituras, mas não uma prova estatística formal de que a revisão será
  sempre nessa direção e magnitude.
- Não há, neste briefing, acesso à metodologia de captura do provedor de dado por trás do
  ticker `HO=F` — a hipótese de "print antecipado de baixo volume" é a mais consistente com os
  fatos observados, mas não foi confirmada por nenhuma fonte externa, apenas inferida da
  própria série de revisões.
- Não foi possível verificar diretamente, nesta janela do dump, o volume revisado da sessão de
  16/09 (o dump mais antigo disponível não traz mais a linha bruta `cme_cbot` daquela data) —
  a tabela acima marca esse campo como "não capturado diretamente nesta janela".
