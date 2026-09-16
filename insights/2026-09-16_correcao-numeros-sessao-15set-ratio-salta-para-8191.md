---
data: 2026-09-16
titulo: "Auditoria dos números da sessão de 15/09: a leitura de ontem usou fechamentos e volumes parciais para soja, farelo e óleo — o dump de hoje traz, para a mesma data, fechamentos mais altos nos três produtos e volumes 25 a 83 vezes maiores, e o achado mais importante é que o ratio Far/Soj real da sessão é 81,91% (não 80,46%), a maior leitura da janela e o maior salto diário desde a abertura da tese"
tags: [farelo, oleo_soja, soja, ratio-far-soj, dados, auto-claude]
fontes:
  - CME CBOT — linhas brutas da sessão de 2026-09-15 presentes no dump de hoje (`briefing/latest.md`, seção `cme_cbot`): soja (ZSX26) abertura 1.303,25, máxima 1.319,50, mínima 1.294,25, **fechamento 1.319,25**, volume **121.947** contratos; farelo (ZMV26) abertura 350,30, máxima 360,70, mínima 347,30, **fechamento 360,20**, volume **39.805** contratos; óleo (ZLV26) abertura 69,62, máxima 70,15, mínima 69,11, **fechamento 69,79**, volume **22.257** contratos; heating oil (HO=F) abertura 4,9924, máxima 5,0118, mínima 4,9923, **fechamento 5,0077**, volume 203 contratos (ainda anormalmente baixo — ver seção final)
  - Indicadores sintéticos internos, 2026-09-15 (seção `indicators` do dump de hoje): crush margin **2,4088** USD/bushel ("farelo 360,20 + óleo 69,79 − soja 1319,25"), far_soj_ratio_pct **81,91%** ("farelo 360,20/sht ÷ (soja 1319,25cts × 33,33)"), oil_share_pct **49,21%** ("valor óleo 7,68/total 15,60"), oil_meal_spread_usd_bu **-0,2475**, paridade BR soja **R$149,75/saca** ("CBOT 1319,25 × USD/BRL 5,1490"); biodiesel_us: custo_óleo **5,2343** USD/galão, receita **8,1727** USD/galão, margem **2,1384** USD/galão
  - Fila de julgamento — 2026-09-15 (a mesma que acompanha o dump de hoje), item `alerta-quebra_resistencia-soja_cbot-2026-09-15`: "soja_cbot fechou em **1319.25** — acima da resistencia 1180.00" — gerado automaticamente pelo sistema a partir do banco de indicadores, não por este analista
  - Fila de julgamento — mesma data, itens `alerta-quebra_resistencia-farelo_cbot-2026-09-15` ("farelo_cbot fechou em **360.20**") e `alerta-quebra_suporte-oleo_cbot-2026-09-15` ("oleo_cbot fechou em **69.79**") — confirmam independentemente os três fechamentos corrigidos
  - Fila de julgamento — mesma data, item `alerta-quebra_suporte-complexo_soja-2026-09-15`: "complexo_soja fechou em **2.41**" (arredondamento de 2,4088) — confirma independentemente o crush margin correto
  - Comparação: [[2026-09-15_leitura-complexo]] e [[2026-09-15_ratio-far-soj-terceira-sessao-consecutiva-acima-80]], que usaram fechamento soja 1.298,25 (volume 2.379), farelo 348,20 (volume 479), óleo 69,50 (volume 1.045), heating oil 4,8126 (volume 510), ratio 80,46%, oil share 49,95%, oil-meal spread -0,0154, crush margin 2,3229, paridade BR R$147,96, margem de biodiesel US$1,9651
  - Precedente direto: [[2026-09-13_correcao-numeros-sessao-11set-farelo-oleo]] — mesma classe de problema (fechamentos/volumes de uma sessão revisados na geração seguinte do briefing), mesma sessão-fonte CME CBOT, mesma metodologia de verificação cruzada via fila autogerada
status: ativa
vies: [bull-soja, bull-farelo, bear-oleo_soja]
---

## Por que este insight existe separado da leitura diária

Ao preparar a leitura de hoje (16/09), cruzei os números usados pela leitura de ontem
([[2026-09-15_leitura-complexo]]) e pelo insight dedicado de ontem
([[2026-09-15_ratio-far-soj-terceira-sessao-consecutiva-acima-80]]) contra as linhas brutas
que o dump de hoje efetivamente traz para a mesma sessão de 15/09. Os números não batem em
nenhum dos três produtos, e a divergência muda uma conclusão central da leitura de ontem: a
ideia de que o complexo "deu uma pequena respirada" depois do salto de segunda-feira não é
sustentada pelos dados agora disponíveis — o oposto é o que se vê. Este é o segundo episódio
do gênero em uma semana (o primeiro foi a auditoria de 13/09, sobre a sessão de 11/09), e a
recorrência por si só é um achado que merece registro formal, para não deixar que o padrão
se torne invisível por ser tratado como acidente isolado a cada vez.

## O que diverge, produto por produto

| Métrica (15/09) | Usado em 15/09 | No dump de hoje (16/09) | Fonte que corrobora o valor correto |
|---|---|---|---|
| Soja CBOT fechamento | 1.298,25 | **1.319,25** | `alerta-quebra_resistencia-soja_cbot-2026-09-15` (fila, autogerado) e `soja_paridade_br` (indicators) |
| Soja CBOT volume | 2.379 | **121.947** | linha bruta `cme_cbot` |
| Soja variação vs 14/09 | -0,52% | **+1,15%** | recalculado de 1.304,25→1.319,25 |
| Farelo CBOT fechamento | 348,20 | **360,20** | `alerta-quebra_resistencia-farelo_cbot-2026-09-15` (fila, autogerado) e `complexo_soja.crush_margin_usd_bu` (indicators) |
| Farelo CBOT volume | 479 | **39.805** | linha bruta `cme_cbot` |
| Farelo variação vs 14/09 | -0,63% | **+2,86%** | recalculado de 350,20→360,20 |
| Óleo CBOT fechamento | 69,50 | **69,79** | `alerta-quebra_suporte-oleo_cbot-2026-09-15` (fila, autogerado) e `biodiesel_us.custo_oleo_usd_galao` (indicators) |
| Óleo CBOT volume | 1.045 | **22.257** | linha bruta `cme_cbot` |
| Óleo variação vs 14/09 | -0,17% | **+0,20%** | recalculado de 69,65→69,79 |
| Heating oil (HO=F) fechamento | 4,8126 | **5,0077** | linha bruta `cme_cbot` (heating_oil_cbot) |
| Heating oil volume | 510 | 203 | linha bruta — ainda baixo, ver seção final |
| Ratio Far/Soj | 80,46% | **81,91%** | `complexo_soja.far_soj_ratio_pct` (indicators) |
| Oil share | 49,95% | **49,21%** | `complexo_soja.oil_share_pct` (indicators) |
| Oil-meal spread | -0,0154 | **-0,2475** | `complexo_soja.oil_meal_spread_usd_bu` (indicators) |
| Crush margin | 2,3229 (dist. -7,08%) | **2,4088** (dist. -3,65%) | `alerta-quebra_suporte-complexo_soja-2026-09-15` (fila arredonda p/ "2.41") |
| Paridade BR soja | R$147,96 | **R$149,75** | `soja_paridade_br.brl_saca_paridade` (indicators) |
| Margem biodiesel US | US$1,9651 | **US$2,1384 (recorde da janela)** | `biodiesel_us.margem_usd_galao` (indicators) |

O ISF (60/100) e o ISO (80/100) são, de novo, as duas únicas métricas que batem exatamente
entre as duas leituras — a mesma constatação já feita na auditoria de 13/09.

## Por que confio nos números do dump de hoje, e não nos de ontem

A mesma lógica de verificação cruzada usada na auditoria de 13/09 se aplica aqui, com uma
camada adicional de evidência:

1. **A fila de julgamento é gerada automaticamente pelo robô a partir do banco de
   indicadores**, não por este analista. Os itens `alerta-quebra_resistencia-soja_cbot-2026-09-15`,
   `alerta-quebra_resistencia-farelo_cbot-2026-09-15` e `alerta-quebra_suporte-oleo_cbot-2026-09-15`
   citam literalmente 1.319,25 / 360,20 / 69,79 — se a leitura de ontem estivesse certa
   (1.298,25 / 348,20 / 69,50), a fila teria gerado números diferentes. Ela não gerou.
2. **Os volumes corrigidos caem dentro (ou acima) da faixa histórica recente desta mesma
   janela do dump** (soja 100-160 mil, farelo 20-30 mil, óleo 17-32 mil, todos citados em
   leituras anteriores) — os volumes de ontem (2.379/479/1.045) eram órfãos desse padrão,
   um sinal de alerta que a própria leitura de ontem já havia registrado na seção
   Honestidade sem conseguir confirmá-lo.
3. **As três fórmulas internas (crush margin, ratio, paridade BR) fecham de forma
   consistente com os novos fechamentos**, e não fechariam com os antigos — por exemplo, o
   crush margin de 2,4088 só bate com "farelo 360,20 + óleo 69,79 − soja 1.319,25" descrito
   literalmente na nota de fonte do próprio indicador.
4. **A curva futura "de 14/09" também veio corrigida no mesmo dump**: máxima, mínima e
   volume de farelo para 14/09, que ontem apareciam idênticos aos de 15/09 (contaminação
   cruzada, documentada na seção Honestidade da leitura de ontem), hoje aparecem com valores
   próprios e plausíveis (máxima 352,80, mínima 344,60, volume 34.001) — coerentes com um
   pregão normal de segunda-feira, reforçando que o problema de ontem era um artefato de
   captura parcial, não uma mudança real na estrutura do mercado.

## O que muda na leitura do complexo

A mudança mais importante não é de sinal (o complexo já estava subindo desde a leitura de
14/09), é de **magnitude e de aceleração**:

- O ratio Far/Soj não estava "estabilizando perto de zero" no oil-meal spread, como a
  leitura de ontem descrevia (-0,0154, "o mais próximo de zero dos três") — estava
  **acelerando** (-0,2475, mais de 8 vezes maior em módulo). A diferença entre "equilíbrio se
  formando" e "farelo disparando" é grande o suficiente para justificar, na leitura
  principal de hoje ([[2026-09-16_leitura-complexo]]), a primeira elevação de viés do
  farelo de "neutro" para "bull" desde a abertura da tese em 11/06/2026
  ([[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]).
- O ratio corrigido de 81,91% está a apenas 0,51 ponto percentual do nível de abertura da
  tese original (81,4%, em 11/06/2026) — um dado simbólico relevante: o ratio completou uma
  volta quase completa desde o início da tese de "abundância de farelo", mas chegando lá por
  cima (subindo de volta através da zona 80-82%), não confirmando a compressão adicional que
  a tese original apostava.
- A soja não deu uma pausa técnica — estendeu o rompimento da resistência de 1.180,00 para
  uma folga de 11,80% (ante os 10,02% calculados ontem), com volume que remove qualquer
  dúvida sobre a genuinidade do movimento.
- A margem de biodiesel americana não recuou para US$1,9651 — bateu um novo recorde da
  janela em US$2,1384, ampliando a divergência entre o preço do óleo em Chicago (ainda
  abaixo do suporte de 72,00) e o fundamento de demanda real por óleo como insumo de
  biocombustível.

## O que ainda não está resolvido

- **O volume do heating oil (HO=F) em 15/09 continua anormalmente baixo mesmo após a
  correção geral dos outros quatro instrumentos — apenas 203 contratos**, ainda muito
  distante dos 62.190 vistos em 11/09. Isso significa que o fechamento de 5,0077 usado no
  cálculo da margem recorde de biodiesel desta leitura carrega o mesmo tipo de incerteza que
  os outros quatro instrumentos carregavam ontem, e ainda não foi resolvido por nenhuma das
  duas gerações do briefing observadas até agora.
- **A janela de 14 dias do dump ainda não traz nenhuma linha bruta de CME CBOT para soja e
  óleo na data de 14/09** — apenas farelo e heating oil. Essa lacuna específica persiste
  desde a leitura de ontem.
- **Este é o segundo episódio do gênero em uma semana**, ambos na mesma fonte (CME CBOT) e
  ambos na mesma direção (dado inicial mais fraco/parcial, correção posterior mais forte,
  nunca o oposto até agora). Duas ocorrências não provam um padrão estrutural, mas já são
  o suficiente para recomendar, de forma prática, que qualquer fechamento do dia mais
  recente do dump seja tratado com desconto de confiança até a geração seguinte confirmar —
  uma regra de bolso que passa a valer a partir de hoje para as próximas leituras desta
  série, não apenas para este episódio.

Cruza com [[2026-09-16_leitura-complexo]] (leitura diária de hoje, que incorpora esta
correção em todas as seções e trata os itens de fila
`alerta-quebra_resistencia-soja_cbot-2026-09-15`,
`alerta-quebra_resistencia-farelo_cbot-2026-09-15`,
`alerta-quebra_suporte-oleo_cbot-2026-09-15` e
`alerta-quebra_suporte-complexo_soja-2026-09-15`).
