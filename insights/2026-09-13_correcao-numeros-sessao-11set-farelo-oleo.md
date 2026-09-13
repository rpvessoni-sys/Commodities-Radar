---
data: 2026-09-13
titulo: "Auditoria dos números da sessão de 11/09: a leitura de 12/09 usou fechamentos, volume e heating oil incorretos para farelo, soja e óleo — o dump e a própria fila de julgamento de hoje confirmam valores diferentes, e o achado mais importante é que a margem de biodiesel americana NÃO recuou como descrito; na verdade bateu novo recorde da janela"
tags: [farelo, oleo_soja, soja, ratio-far-soj, dados, auto-claude]
fontes:
  - CME CBOT — linhas brutas da sessão de 2026-09-11 presentes no dump de hoje (`briefing/latest.md`, seção `cme_cbot`): soja (ZSX26) abertura 1.330,00, máxima 1.335,25, mínima 1.293,00, **fechamento 1.296,50**, volume **162.475** contratos; farelo (ZMV26) abertura 349,30, máxima 350,60, mínima 344,70, **fechamento 346,80**, volume 30.816 contratos; óleo (ZLV26) abertura 71,57, máxima 71,72, mínima 69,05, **fechamento 69,19**, volume 32.345 contratos; heating oil (HO=F, CME NYMEX) abertura 5,1481, máxima 5,1664, mínima 4,9380, **fechamento 4,9593**, volume 62.190 contratos
  - Indicadores sintéticos internos, 2026-09-11 (seção `indicators` do dump): crush margin **2,2755** USD/bushel ("farelo 346,80 + óleo 69,19 − soja 1296,50"), far_soj_ratio_pct **80,25%** ("farelo 346,80/sht ÷ (soja 1296,50cts × 33,33)"), oil_share_pct **49,94%** ("valor óleo 7,61/total 15,24"), oil_meal_spread_usd_bu **-0,0187**, paridade BR soja **R$145,54/saca** ("CBOT 1296,50 × USD/BRL 5,0918"); biodiesel_us: custo_oleo **5,1893** USD/galão, receita **8,1243** USD/galão, margem **2,135** USD/galão
  - Fila de julgamento — 2026-09-12 (a mesma que acompanha o dump de hoje), item `alerta-movimento_forte-soja_cbot-2026-09-11`: "soja_cbot variou **-2.68%** no dia (de 1332.25 para **1296.50**)" — gerado automaticamente pelo sistema a partir do banco de indicadores, não por este analista
  - Fila de julgamento — mesma data, item `alerta-quebra_suporte-complexo_soja-2026-09-11`: "complexo_soja fechou em **2.28**" (arredondamento de 2,2755) — confirma independentemente o crush margin correto
  - Comparação: [[2026-09-12_leitura-complexo]] e [[2026-09-12_ratio-far-soj-rompe-80-pela-primeira-vez]], que usaram fechamento soja 1.299,00 (volume 245.874), farelo 347,80, óleo 69,11, heating oil 4,7792 (com uma "inconsistência" abertura>máxima que não existe nos dados hoje disponíveis), ratio 80,32%, oil share 49,84%, oil-meal spread -0,0495, crush margin 2,2637, paridade BR R$145,82, margem de biodiesel US$1,961 (-5,11%)
status: ativa
vies: [neutral-farelo]
---

## Por que este insight existe separado da leitura diária

Ao preparar a leitura de hoje (13/09, domingo — sem pregão novo desde a sessão de
sexta-feira 11/09), cruzei os números usados pela leitura de ontem
([[2026-09-12_leitura-complexo]]) e pelo insight dedicado
([[2026-09-12_ratio-far-soj-rompe-80-pela-primeira-vez]]) contra as linhas brutas que o
dump de hoje efetivamente traz para a mesma sessão de 11/09. Os números não batem em
praticamente nenhum dos três produtos, e a divergência muda uma conclusão central: a
narrativa de que "o motor de alta do óleo (heating oil) se desfez e derrubou a margem de
biodiesel" não é sustentada pelos dados atualmente disponíveis — o oposto é o que se vê.
Como a rotina exige nunca inventar número e sempre citar fonte+data, um documento próprio
para esta auditoria evita que o erro se propague silenciosamente para as próximas revisões
da tese do ratio Far/Soj (D+7, D+90, D+180), que dependem exatamente desses valores.

## O que diverge, produto por produto

| Métrica (11/09) | Usado em 12/09 | No dump de hoje | Fonte que corrobora o valor correto |
|---|---|---|---|
| Soja CBOT fechamento | 1.299,00 | **1.296,50** | `alerta-movimento_forte-soja_cbot-2026-09-11` (fila, autogerado) e `soja_paridade_br` (indicators) |
| Soja CBOT volume | 245.874 | **162.475** | linha bruta `cme_cbot` |
| Soja variação vs 10/09 | -2,50% | **-2,68%** | mesmo item de fila, texto literal "-2.68%" |
| Farelo CBOT fechamento | 347,80 | **346,80** | linha bruta `cme_cbot` e `complexo_soja.crush_margin_usd_bu` (indicators) |
| Farelo variação vs 10/09 | -0,80% | **-1,08%** | recalculado de 350,60→346,80 |
| Óleo CBOT fechamento | 69,11 | **69,19** | linha bruta `cme_cbot` e `biodiesel_us.custo_oleo_usd_galao` (indicators) |
| Óleo variação vs 10/09 | -3,22% | **-3,11%** | `alerta-movimento_forte-oleo_cbot-2026-09-11` (fila, texto literal "-3.11%") |
| Ratio Far/Soj | 80,32% | **80,25%** | `complexo_soja.far_soj_ratio_pct` (indicators) |
| Oil share | 49,84% | **49,94%** | `complexo_soja.oil_share_pct` (indicators) |
| Oil-meal spread | -0,0495 | **-0,0187** | `complexo_soja.oil_meal_spread_usd_bu` (indicators) |
| Crush margin | 2,2637 (dist. -9,45%) | **2,2755** (dist. -8,98%) | `alerta-quebra_suporte-complexo_soja-2026-09-11` (fila arredonda p/ "2.28") |
| Paridade BR soja | R$145,82 (-2,94%) | **R$145,54** (-3,12%) | `soja_paridade_br.brl_saca_paridade` (indicators) |
| Heating oil (HO=F) fechamento | 4,7792 | **4,9593** | linha bruta `cme_cbot` (heating_oil_cbot) |
| Margem biodiesel US | US$1,961 (**-5,11%**) | **US$2,135 (+3,30%)** | `biodiesel_us.margem_usd_galao` (indicators), consistente internamente: receita 8,1243 − custo_oleo 5,1893 − custo industrial 0,80 = 2,135 |

O ISF (60/100) e o ISO (80/100) são as duas únicas métricas que batem exatamente entre as
duas leituras — não houve erro nelas.

## Por que confio nos números do dump de hoje, e não nos de ontem

Três fontes independentes dentro do próprio sistema — que eu não escrevi e não controlo —
corroboram os valores da coluna "dump de hoje":

1. **A fila de julgamento é gerada automaticamente pelo robô a partir do banco de
   indicadores**, não por este analista. O item `alerta-movimento_forte-soja_cbot-2026-09-11`
   cita literalmente "-2.68% ... de 1332.25 para 1296.50" e o item
   `alerta-movimento_forte-oleo_cbot-2026-09-11` cita literalmente "-3.11% ... de 71.41
   para 69.19". Se a leitura de ontem estivesse certa (1.299,00 e 69,11), a fila teria
   gerado números de variação diferentes dos que ela de fato gerou.
2. **Os valores dos indicadores sintéticos são internamente consistentes entre si.** O
   crush margin (2,2755) usa explicitamente "farelo 346,80 + óleo 69,19 − soja 1296,50"
   na própria descrição do dado — os três valores corretos aparecem juntos, gerados pela
   mesma fórmula. A margem de biodiesel (2,135) reconcilia exatamente com
   receita (8,1243) − custo_oleo (5,1893) − custo industrial fixo (0,80) = 2,135 — uma
   verificação aritmética direta que fecha sem resíduo.
3. **A queda percentual do custo do óleo no biodiesel (-3,11%) bate exatamente com a queda
   do preço do óleo em Chicago (71,41→69,19 = -3,11%)**, como deveria ser, já que
   custo_oleo é uma função linear do preço do óleo (7,5 lb × preço em cts/lb). Essa
   consistência cruzada não existiria se um dos dois números fosse produto de invenção.

Não é possível, com os dados disponíveis, determinar a causa raiz da divergência (revisão
upstream dos dados entre a geração do dump de 12/09 e o de hoje, ou erro de leitura da
sessão anterior) — e este documento não afirma qual das duas hipóteses é verdadeira.
Registra apenas que, hoje, o conjunto de números internamente consistente e corroborado
por três fontes independentes é o do dump atual, e é esse conjunto que esta leitura e as
próximas devem usar como referência para a sessão de 11/09.

## A consequência que mais importa: a tese do óleo precisa de nuance

A leitura de ontem descreveu um mecanismo causal claro: "o heating oil saltou +7% na
quinta e devolveu quase tudo na sexta, arrastando a margem de biodiesel para baixo em
-5,11%, o que ajuda a explicar a queda do óleo". Com os números corretos, essa cadeia
causal não se sustenta: a margem de biodiesel **subiu** para US$2,135/galão, o valor mais
alto de toda a janela visível do dump (superando os US$1,7385/galão de 04/09, os
US$1,6663 de 08/09, US$1,91 de 09/09 e US$2,0667 de 10/09) — a terceira alta diária
consecutiva. O mecanismo real, olhando os componentes: o custo do óleo como insumo caiu
-3,11% junto com o próprio preço do óleo em Chicago (o que **melhora** a margem do
produtor de biodiesel, pois óleo é custo, não receita, nessa conta), enquanto a receita
modelada caiu bem menos (-1,19%). O resultado líquido foi margem melhor, não pior.

Isso não significa que o óleo tenha razão fundamental para subir — significa que a queda
de preço do óleo em Chicago no dia 11/09 aconteceu **apesar de**, não **por causa de**, uma
deterioração da economia do biodiesel americano. É uma divergência entre o preço
(caindo, bearish) e um dos seus principais fundamentos de demanda (biodiesel, melhorando)
que merece ser tratada como tal na leitura do dia — ver seção Óleo de
[[2026-09-13_leitura-complexo]], que desenvolve esse ponto com a devida profundidade e
rebaixa a convicção do viés bear-óleo de "moderado a forte" para "moderado" por causa
justamente dessa divergência.

## O que isto muda (e o que não muda) na tese do ratio Far/Soj

O ratio Far/Soj corrigido (80,25%, não 80,32%) **ainda fecha acima de 80%** — o gatilho de
invalidação definido em 11/06/2026
([[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]) e reafirmado no veredito D+90
([[2026-09-09_d90-ratio-far-soj-reverte-na-vespera]]) continua tecnicamente disparado, e a
classificação `neutral-farelo` adotada em
[[2026-09-12_ratio-far-soj-rompe-80-pela-primeira-vez]] permanece válida. O que muda é a
margem de segurança do argumento: o salto do ratio foi de +1,30 ponto percentual (não
+1,37), o oil share ficou a apenas 0,06 ponto abaixo de 50% (49,94%, não 49,84% — uma
margem quase invisível), e o oil-meal spread virou negativo por uma margem muito mais
estreita (-0,0187, não -0,0495 — praticamente um empate técnico entre óleo e farelo dentro
do crush, não uma vitória clara do farelo). A leitura de ontem descreveu "cinco
indicadores se movendo juntos com folga" — o correto é "cinco indicadores se movendo
juntos, mas por margens pequenas, quase no limite de arredondamento". Isso não desfaz o
evento (o fechamento acima de 80% é real e a fila o confirma de forma independente), mas
reduz um pouco a força da evidência de suporte, e é essa versão mais conservadora que deve
ser usada nas próximas revisões (D+7 vencida, D+90 já tratada, D+180 em 08/12/2026).

## Encaminhamento

Nenhuma tese de viés muda de direção por causa desta auditoria — farelo segue
`neutral-farelo`, e óleo segue com viés baixista de preço, agora com convicção reduzida
para "moderado" em vez de "moderado a forte". O que muda é a precisão dos números que
sustentam essas teses, e a identificação de uma divergência genuína (preço do óleo caindo,
margem de biodiesel subindo) que a leitura de ontem não capturou porque partiu de um dado
de heating oil que não confere com o dump atual. Recomenda-se, para as próximas leituras,
conferir cruzadamente os valores de `cme_cbot` e `indicators` do dump antes de citar
variações percentuais — a fila de julgamento, por ser autogerada a partir do banco, é um
bom ponto de verificação independente quando ela cobre o mesmo fato.
