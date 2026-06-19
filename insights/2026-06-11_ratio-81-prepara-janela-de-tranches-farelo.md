---
data: 2026-06-11
titulo: Ratio Far/Soj 81,4% + FOB export zerado — spread far÷soj comprimindo, viés baixista no farelo
tags: [farelo, ratio-far-soj, spread, fisico, paranagua, auto-claude]
fontes:
  - Sistema commodities-radar — CBOT/indicators 11/jun/2026
  - Notícias Agrícolas (NAG) — prêmio farelo Paranaguá +0,05 US$/sht e praças físicas, fechamento 10/jun/2026
  - Varredura completa 05/jun (baseline de comparação)
  - Sistema commodities-radar — CBOT/indicators/WASDE 18/jun/2026 (revisão D+7)
status: revisada
vies: [bear-farelo]
---

> **Atualização 2026-06-18 (revisão D+7 — trata fila `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`):**
> Ratio Far/Soj comprimiu mais 90bps (81,4% → 80,51%, indicadores 18/jun) mas **não rompeu o gatilho de <80% ainda** — tese mantida, vigilância redobrada.
> WASDE 11/jun: produção farelo Argentina 2026/27 cortada levemente (33,33 → 33,11 mi_t) — impacto marginal, não muda o quadro. NOPA mai/26 não acessível (membership pago, sem dado); `release-nopa-2026-06-19` também não entrou (monthly_status=0, sem número real).
> Crush margin recuou de 3,78 → 3,07 USD/bu (18/jun) — esmagadora ainda lucrativa, mas com menor folga, podendo desacelerar levemente oferta de farelo (risco de alívio de curto prazo). Índice sobra_farelo mantido em 100.0 (5/5 condições) — pressão baixista máxima.
> Prêmio export farelo Paranaguá inalterado (+0,05 USD/sht, NAG 18/jun). Física MT: R$ 1.545/t (IMEA) e R$ 1.560/t (Rondonópolis) — sem alteração nos últimos 7 dias.
> Análise da queda do óleo (−2,59%) e contexto cambial (USD/BRL +1,92%) em `[[2026-06-18_oleo-quebra-suporte-72]]` e `[[2026-06-19_usd-brl-alta-amortece-queda-cbot-soja-br]]`.
> **Próxima revisão**: D+7 = 2026-06-25 ou ao romper ratio <80%.

> **Atualização 11/jun (mesmo dia, pós-backfill de 5 anos do CBOT):** o argumento
> "preço absoluto perto da mínima de 52 semanas" estava calibrado errado. A mínima
> ~293 vale pro **contrato atual**; a **série front-month contínua** fez 260,70 em
> 2025, e os US$ 303,60 de hoje estão no **percentil 57** do ano — meio do range,
> não extremo. O pilar da tese segue sendo o **ratio comprimindo (81,4%)**, o
> **prêmio export zerado** e a **estrutura do crush** (oil share 55%, fundos
> managed money no percentil 94 de net long em farelo — posição não paga, risco
> de desmonte baixista). O "preço raro" sai da lista de argumentos.

## Resumo executivo

- **Ratio Far/Soj comprimiu de 83,3% → 81,4% em 4 pregões** (05→11/jun) — a velocidade de compressão indica que a zona comprimida (<80%) pode chegar em 1-2 semanas se o padrão se mantiver.
- **Farelo CBOT jul a US$ 303,60/sht, a 3,6% da mínima de 52 semanas (293)** e com momentum vendedor (−3,2% em 5 pregões) — o preço absoluto já é de oportunidade mesmo sem o ratio "perfeito".
- **Prêmio de exportação do farelo em Paranaguá está zerado (+0,05 US$/sht, NAG 10/jun)** — FOB implícito R$ 1.732/t fica ABAIXO do interno: exportar não compete, o farelo sobra no mercado doméstico. É pressão adicional de baixa que NÃO aparece no CBOT.
- **A estrutura que despeja farelo segue intacta**: crush US$ 3,78/bu (recorde) + oil share 55,4% — a esmagadora roda pra capturar óleo e aceita vender farelo barato.
- **Leitura operacional (trader)**: spread far÷soj comprimindo rumo a <80% + viés baixista no farelo absoluto. Pra quem opera o spread, o lado de convergência (long farelo / short soja, ou crush) ganha assimetria se o ratio fechar <80% ou o CBOT romper 293. Risco de cauda: China destravar compras de soja US levanta o complexo inteiro e estica o ratio sem aviso.

## Contexto / dados

| Métrica | 05/jun | 11/jun | Leitura |
|---|---|---|---|
| Ratio Far/Soj | 83,3% | 81,4% | compressão rápida rumo a <80% |
| Farelo CBOT jul | ~313 | 303,60 | −3% na semana, mínima 52sem 293 |
| Prêmio export PGUA (NAG) | n/d | +0,05 US$/sht | export não compete c/ interno |
| Crush margin | 3,78 | 3,78 | esmagadora a fundo, sem alívio |
| Oil share | 55,4% | 55,4% | óleo paga o crush, farelo é resto |

Cotações físicas públicas 10/jun (NAG): Média RS R$ 1.710/t · MT (IMEA) R$ 1.562/t · Rondonópolis R$ 1.580/t. Spread interno vs RS de ~R$ 150/t confirma o Sul mais caro — relevante pra quem opera o físico no PR.

Cruza com [[2026-06-05_varredura-completa-complexo-soja]] (tese do complexo partido) e atualiza a régua de decisão do card Ratio Far/Soj. O contraponto altista de [[2026-05-26_b16-bullish-farelo]] segue ADIADO (B16 sem data — ver Monitor Tributário).

## Pergunta-tese

O que precisa ser verdadeiro pra essa tese se confirmar:

- Esmagamento BR/US segue em ritmo recorde (NOPA ~15/jun confirma?)
- China continua fora das compras de soja US (sem destravamento)
- B16 continua adiado (sem data no CNPE)
- WASDE de HOJE (11/jun) não mostra corte de oferta de farelo/grão

## Gatilhos que invalidam

- China anuncia compras grandes de soja US → complexo inteiro sobe, ratio vira pra cima
- B16 ganha data de vigência → demanda de óleo interno sobe, esmagamento BR acelera ainda mais... mas farelo extra pode até REFORÇAR a baixa (avaliar sinal)
- Crush margin desabar pra <2,50 (alerta configurado) → esmagadora tira o pé, oferta de farelo seca
- WASDE 11/jun cortar estoque mundial de farelo de forma relevante

## Revisão programada

- **D+7**: 2026-06-18 — ratio fechou <80%? WASDE mudou o quadro? NOPA confirmou crush?
- **D+90**: 2026-09-09 — o spread far÷soj reverteu ou seguiu comprimindo? O viés baixista no farelo se confirmou?
- **D+180**: 2026-12-08 — fechar ciclo, marcar status
