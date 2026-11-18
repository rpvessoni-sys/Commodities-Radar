# Briefing consolidado — 2026-11-18

_Base 100% publica (CBOT/BCB/CEPEA/NAG/USDA/COT/clima) + notas manuais do consultor._

## O que fazer com este briefing

- **Tratar a fila de julgamento** (camada de LEITURA): rode `python main.py queue`, siga `system/prompts/treat_queue.txt` e escreva so `insights/*.md` (com `vies:`).
- **Sintese narrativa do dia** (opcional): siga `system/prompts/synthesize_daily.txt`.
- Numeros SEMPRE com fonte + data. Aplicar a lente tributaria BR antes de concluir tese de preco.
- NUNCA escrever em numero/indicador/DB/alerts_config — opiniao so vai pra `insights/*.md`.

Notas manuais disponiveis: 0 do consultor · 0 de call.

---

# DADOS PUBLICOS (ultimos 14 dias)

## abiove

- 2026-12-01 | farelo_brasil | estoque_final: 1015.5196837897658 mil_t (ABIOVE projecoes_mensais | farelo | mes 12/2026)
- 2026-12-01 | farelo_brasil | estoque_inicial: 1101.4257219409003 mil_t (ABIOVE projecoes_mensais | farelo | mes 12/2026)
- 2026-12-01 | farelo_brasil | exportacao: 700.0 mil_t (ABIOVE projecoes_mensais | farelo | mes 12/2026)
- 2026-12-01 | farelo_brasil | producao: 1659.0394113036511 mil_t (ABIOVE projecoes_mensais | farelo | mes 12/2026)
- 2026-12-01 | oleo_brasil | estoque_final: 291.87935176989765 mil_t (ABIOVE projecoes_mensais | oleo | mes 12/2026)
- 2026-12-01 | oleo_brasil | estoque_inicial: 315.25442492998815 mil_t (ABIOVE projecoes_mensais | oleo | mes 12/2026)
- 2026-12-01 | oleo_brasil | producao: 415.1871689782802 mil_t (ABIOVE projecoes_mensais | oleo | mes 12/2026)
- 2026-12-01 | soja_brasil | esmagamento: 2203.5374323262477 mil_t (ABIOVE projecoes_mensais | soja | mes 12/2026)
- 2026-12-01 | soja_brasil | estoque_final: 1889.9122826199473 mil_t (ABIOVE projecoes_mensais | soja | mes 12/2026)
- 2026-12-01 | soja_brasil | estoque_inicial: 3658.9889445987023 mil_t (ABIOVE projecoes_mensais | soja | mes 12/2026)

---

## anec

- 2026-11-18 | anec | links_relatorios: 0.0 count (Nenhum link de relatorio encontrado na pagina /estatisticas/. Estrutura pode ter mudado.)

---

## bcb

- 2026-11-17 | eur_brl_ptax | valor: 6.3659 BRL/EUR (sgs=21619)
- 2026-11-17 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-11-17 | usd_brl_ptax | valor: 5.7851 BRL/USD (sgs=1)
- 2026-11-16 | eur_brl_ptax | valor: 6.3102 BRL/EUR (sgs=21619)
- 2026-11-16 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-11-16 | usd_brl_ptax | valor: 5.7324 BRL/USD (sgs=1)
- 2026-11-13 | eur_brl_ptax | valor: 6.2334 BRL/EUR (sgs=21619)
- 2026-11-13 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-11-13 | usd_brl_ptax | valor: 5.6518 BRL/USD (sgs=1)
- 2026-11-12 | eur_brl_ptax | valor: 6.2133 BRL/EUR (sgs=21619)
- 2026-11-12 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-11-12 | usd_brl_ptax | valor: 5.6143 BRL/USD (sgs=1)
- 2026-11-11 | eur_brl_ptax | valor: 6.1706 BRL/EUR (sgs=21619)
- 2026-11-11 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-11-11 | usd_brl_ptax | valor: 5.5606 BRL/USD (sgs=1)
- 2026-11-10 | eur_brl_ptax | valor: 6.2317 BRL/EUR (sgs=21619)
- 2026-11-10 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-11-10 | usd_brl_ptax | valor: 5.584 BRL/USD (sgs=1)
- 2026-11-09 | eur_brl_ptax | valor: 6.1741 BRL/EUR (sgs=21619)
- 2026-11-09 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-11-09 | usd_brl_ptax | valor: 5.5146 BRL/USD (sgs=1)
- 2026-11-06 | eur_brl_ptax | valor: 6.1317 BRL/EUR (sgs=21619)
- 2026-11-06 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-11-06 | usd_brl_ptax | valor: 5.5013 BRL/USD (sgs=1)
- 2026-11-05 | eur_brl_ptax | valor: 6.1323 BRL/EUR (sgs=21619)
- 2026-11-05 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-11-05 | usd_brl_ptax | valor: 5.4621 BRL/USD (sgs=1)
- 2026-11-04 | eur_brl_ptax | valor: 6.1549 BRL/EUR (sgs=21619)
- 2026-11-04 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-11-04 | usd_brl_ptax | valor: 5.4778 BRL/USD (sgs=1)

---

## cftc_cot

- 2026-11-10 | farelo_cbot | managed_money_long: 116511.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-11-10 | farelo_cbot | managed_money_net: 66653.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE — long - short)
- 2026-11-10 | farelo_cbot | managed_money_short: 49858.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-11-10 | farelo_cbot | open_interest: 576238.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-11-10 | farelo_cbot | producer_long: 88106.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-11-10 | farelo_cbot | producer_short: 328262.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-11-10 | farelo_cbot | swap_long: 120743.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-11-10 | farelo_cbot | swap_short: 9670.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-11-10 | oleo_cbot | managed_money_long: 82605.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-11-10 | oleo_cbot | managed_money_net: 19562.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE — long - short)
- 2026-11-10 | oleo_cbot | managed_money_short: 63043.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-11-10 | oleo_cbot | open_interest: 614995.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-11-10 | oleo_cbot | producer_long: 177452.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-11-10 | oleo_cbot | producer_short: 300803.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-11-10 | oleo_cbot | swap_long: 93320.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-11-10 | oleo_cbot | swap_short: 4815.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-11-10 | soja_cbot | managed_money_long: 181446.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-11-10 | soja_cbot | managed_money_net: 117586.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE — long - short)
- 2026-11-10 | soja_cbot | managed_money_short: 63860.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-11-10 | soja_cbot | open_interest: 973693.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-11-10 | soja_cbot | producer_long: 320416.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-11-10 | soja_cbot | producer_short: 526115.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-11-10 | soja_cbot | swap_long: 123025.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-11-10 | soja_cbot | swap_short: 42145.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)

---

## cme_cbot

- 2026-11-18 | farelo_cbot | abertura: 335.5 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-18 | farelo_cbot | fechamento: 337.8999938964844 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-18 | farelo_cbot | fechamento_F27: 335.6000061035156 USD/short_ton (ticker=ZMF27.CBT venc=jan/27)
- 2026-11-18 | farelo_cbot | fechamento_H27: 336.1000061035156 USD/short_ton (ticker=ZMH27.CBT venc=mar/27)
- 2026-11-18 | farelo_cbot | fechamento_K27: 337.6000061035156 USD/short_ton (ticker=ZMK27.CBT venc=mai/27)
- 2026-11-18 | farelo_cbot | fechamento_N27: 340.70001220703125 USD/short_ton (ticker=ZMN27.CBT venc=jul/27)
- 2026-11-18 | farelo_cbot | fechamento_Q27: 339.1000061035156 USD/short_ton (ticker=ZMQ27.CBT venc=ago/27)
- 2026-11-18 | farelo_cbot | fechamento_Z26: 337.8999938964844 USD/short_ton (ticker=ZMZ26.CBT venc=dez/26)
- 2026-11-18 | farelo_cbot | maxima: 338.5 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-18 | farelo_cbot | minima: 335.20001220703125 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-18 | farelo_cbot | volume: 3998.0 contratos (ticker=ZMZ26.CBT)
- 2026-11-18 | heating_oil_cbot | abertura: 3.990000009536743 USD/galão (ticker=HO=F)
- 2026-11-18 | heating_oil_cbot | fechamento: 3.958699941635132 USD/galão (ticker=HO=F)
- 2026-11-18 | heating_oil_cbot | maxima: 3.989799976348877 USD/galão (ticker=HO=F)
- 2026-11-18 | heating_oil_cbot | minima: 3.950000047683716 USD/galão (ticker=HO=F)
- 2026-11-18 | heating_oil_cbot | volume: 655.0 contratos (ticker=HO=F)
- 2026-11-18 | oleo_cbot | abertura: 62.13999938964844 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-11-18 | oleo_cbot | fechamento: 61.689998626708984 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-11-18 | oleo_cbot | fechamento_F27: 61.959999084472656 USD_cts/lb (ticker=ZLF27.CBT venc=jan/27)
- 2026-11-18 | oleo_cbot | fechamento_H27: 62.4900016784668 USD_cts/lb (ticker=ZLH27.CBT venc=mar/27)
- 2026-11-18 | oleo_cbot | fechamento_K27: 62.97999954223633 USD_cts/lb (ticker=ZLK27.CBT venc=mai/27)
- 2026-11-18 | oleo_cbot | fechamento_N27: 63.2599983215332 USD_cts/lb (ticker=ZLN27.CBT venc=jul/27)
- 2026-11-18 | oleo_cbot | fechamento_Q27: 63.189998626708984 USD_cts/lb (ticker=ZLQ27.CBT venc=ago/27)
- 2026-11-18 | oleo_cbot | fechamento_Z26: 61.689998626708984 USD_cts/lb (ticker=ZLZ26.CBT venc=dez/26)
- 2026-11-18 | oleo_cbot | maxima: 62.25 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-11-18 | oleo_cbot | minima: 61.689998626708984 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-11-18 | oleo_cbot | volume: 3903.0 contratos (ticker=ZLZ26.CBT)
- 2026-11-18 | soja_cbot | abertura: 1225.5 USD/bushel (ticker=ZSF27.CBT)
- 2026-11-18 | soja_cbot | fechamento: 1225.75 USD/bushel (ticker=ZSF27.CBT)
- 2026-11-18 | soja_cbot | fechamento_F27: 1225.75 USD/bushel (ticker=ZSF27.CBT venc=jan/27)
- 2026-11-18 | soja_cbot | fechamento_H27: 1231.25 USD/bushel (ticker=ZSH27.CBT venc=mar/27)
- 2026-11-18 | soja_cbot | fechamento_K27: 1238.5 USD/bushel (ticker=ZSK27.CBT venc=mai/27)
- 2026-11-18 | soja_cbot | fechamento_N27: 1243.75 USD/bushel (ticker=ZSN27.CBT venc=jul/27)
- 2026-11-18 | soja_cbot | fechamento_Q27: 1227.75 USD/bushel (ticker=ZSQ27.CBT venc=ago/27)
- 2026-11-18 | soja_cbot | maxima: 1229.75 USD/bushel (ticker=ZSF27.CBT)
- 2026-11-18 | soja_cbot | minima: 1225.5 USD/bushel (ticker=ZSF27.CBT)
- 2026-11-18 | soja_cbot | volume: 8031.0 contratos (ticker=ZSF27.CBT)
- 2026-11-17 | farelo_cbot | abertura: 334.6000061035156 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-17 | farelo_cbot | fechamento: 335.20001220703125 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-17 | farelo_cbot | fechamento_F27: 333.29998779296875 USD/short_ton (ticker=ZMF27.CBT venc=jan/27)
- 2026-11-17 | farelo_cbot | fechamento_H27: 334.3999938964844 USD/short_ton (ticker=ZMH27.CBT venc=mar/27)
- 2026-11-17 | farelo_cbot | fechamento_K27: 336.0 USD/short_ton (ticker=ZMK27.CBT venc=mai/27)
- 2026-11-17 | farelo_cbot | fechamento_N27: 339.20001220703125 USD/short_ton (ticker=ZMN27.CBT venc=jul/27)
- 2026-11-17 | farelo_cbot | fechamento_Q27: 337.70001220703125 USD/short_ton (ticker=ZMQ27.CBT venc=ago/27)
- 2026-11-17 | farelo_cbot | fechamento_Z26: 335.29998779296875 USD/short_ton (ticker=ZMZ26.CBT venc=dez/26)
- 2026-11-17 | farelo_cbot | maxima: 339.79998779296875 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-17 | farelo_cbot | minima: 333.70001220703125 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-17 | farelo_cbot | volume: 65744.0 contratos (ticker=ZMZ26.CBT)
- 2026-11-17 | heating_oil_cbot | abertura: 4.071199893951416 USD/galão (ticker=HO=F)
- 2026-11-17 | heating_oil_cbot | fechamento: 4.047500133514404 USD/galão (ticker=HO=F)

---

## indicators

- 2026-11-18 | biodiesel_us | custo_oleo_usd_galao: 4.6267 USD/galão (7.5 lb × óleo 61.69 cts/lb)
- 2026-11-18 | biodiesel_us | margem_usd_galao: 1.697 USD/galão (receita 7.12 (HO 3.96 + 1.5×RIN 2.11) − custo 5.43 (óleo 4.63 + ind 0.80))
- 2026-11-18 | biodiesel_us | receita_usd_galao: 7.1237 USD/galão (HO 3.96 + 1.5×RIN 2.11)
- 2026-11-18 | complexo_soja | crush_margin_usd_bu: 1.9622 USD/bushel (Board Crush: farelo 337.90 + oleo 61.69 − soja 1225.75)
- 2026-11-18 | complexo_soja | far_soj_ratio_pct: 82.7 % (farelo 337.90/sht ÷ (soja 1225.75cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-11-18 | complexo_soja | indice_sobra_farelo: 25.0 0-100 (sem sobra relevante (1/4 condições))
- 2026-11-18 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-11-18 | complexo_soja | oil_meal_spread_usd_bu: -0.6479 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-11-18 | complexo_soja | oil_share_pct: 47.72 % (valor oleo 6.79 / total 14.22)
- 2026-11-18 | soja_paridade_br | brl_saca_paridade: 156.33 BRL/saca60kg (CBOT 1225.75 cts × USD/BRL 5.7851 (sem basis))
- 2026-11-17 | biodiesel_us | custo_oleo_usd_galao: 4.6598 USD/galão (7.5 lb × óleo 62.13 cts/lb)
- 2026-11-17 | biodiesel_us | margem_usd_galao: 1.7528 USD/galão (receita 7.21 (HO 4.05 + 1.5×RIN 2.11) − custo 5.46 (óleo 4.66 + ind 0.80))
- 2026-11-17 | biodiesel_us | receita_usd_galao: 7.2125 USD/galão (HO 4.05 + 1.5×RIN 2.11)
- 2026-11-17 | complexo_soja | crush_margin_usd_bu: 1.9537 USD/bushel (Board Crush: farelo 335.20 + oleo 62.13 − soja 1225.50)
- 2026-11-17 | complexo_soja | far_soj_ratio_pct: 82.06 % (farelo 335.20/sht ÷ (soja 1225.50cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-11-17 | complexo_soja | indice_sobra_farelo: 25.0 0-100 (sem sobra relevante (1/4 condições))
- 2026-11-17 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-11-17 | complexo_soja | oil_meal_spread_usd_bu: -0.5401 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-11-17 | complexo_soja | oil_share_pct: 48.1 % (valor oleo 6.83 / total 14.21)
- 2026-11-17 | soja_paridade_br | brl_saca_paridade: 156.3 BRL/saca60kg (CBOT 1225.50 cts × USD/BRL 5.7851 (sem basis))
- 2026-11-16 | biodiesel_us | custo_oleo_usd_galao: 4.6642 USD/galão (7.5 lb × óleo 62.19 cts/lb)
- 2026-11-16 | biodiesel_us | margem_usd_galao: 1.7826 USD/galão (receita 7.25 (HO 4.08 + 1.5×RIN 2.11) − custo 5.46 (óleo 4.66 + ind 0.80))
- 2026-11-16 | biodiesel_us | receita_usd_galao: 7.2468 USD/galão (HO 4.08 + 1.5×RIN 2.11)
- 2026-11-16 | complexo_soja | crush_margin_usd_bu: 1.9121 USD/bushel (Board Crush: farelo 334.60 + oleo 62.19 − soja 1229.00)
- 2026-11-16 | complexo_soja | far_soj_ratio_pct: 81.68 % (farelo 334.60/sht ÷ (soja 1229.00cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-11-16 | complexo_soja | indice_sobra_farelo: 25.0 0-100 (sem sobra relevante (1/4 condições))
- 2026-11-16 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-11-16 | complexo_soja | oil_meal_spread_usd_bu: -0.5203 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-11-16 | complexo_soja | oil_share_pct: 48.17 % (valor oleo 6.84 / total 14.20)
- 2026-11-16 | soja_paridade_br | brl_saca_paridade: 155.32 BRL/saca60kg (CBOT 1229.00 cts × USD/BRL 5.7324 (sem basis))
- 2026-11-15 | complexo_soja | indice_sobra_farelo: 25.0 0-100 (sem sobra relevante (1/4 condições))
- 2026-11-15 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-11-14 | complexo_soja | indice_sobra_farelo: 25.0 0-100 (sem sobra relevante (1/4 condições))
- 2026-11-14 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-11-13 | biodiesel_us | custo_oleo_usd_galao: 4.7828 USD/galão (7.5 lb × óleo 63.77 cts/lb)
- 2026-11-13 | biodiesel_us | margem_usd_galao: 1.8408 USD/galão (receita 7.42 (HO 4.26 + 1.5×RIN 2.11) − custo 5.58 (óleo 4.78 + ind 0.80))
- 2026-11-13 | biodiesel_us | receita_usd_galao: 7.4235 USD/galão (HO 4.26 + 1.5×RIN 2.11)
- 2026-11-13 | complexo_soja | crush_margin_usd_bu: 1.9553 USD/bushel (Board Crush: farelo 329.80 + oleo 63.77 − soja 1231.50)
- 2026-11-13 | complexo_soja | far_soj_ratio_pct: 80.34 % (farelo 329.80/sht ÷ (soja 1231.50cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-11-13 | complexo_soja | indice_sobra_farelo: 25.0 0-100 (sem sobra relevante (1/4 condições))
- 2026-11-13 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-11-13 | complexo_soja | oil_meal_spread_usd_bu: -0.2409 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-11-13 | complexo_soja | oil_share_pct: 49.16 % (valor oleo 7.01 / total 14.27)
- 2026-11-13 | soja_paridade_br | brl_saca_paridade: 153.44 BRL/saca60kg (CBOT 1231.50 cts × USD/BRL 5.6518 (sem basis))
- 2026-11-12 | biodiesel_us | custo_oleo_usd_galao: 4.7565 USD/galão (7.5 lb × óleo 63.42 cts/lb)
- 2026-11-12 | biodiesel_us | margem_usd_galao: 1.895 USD/galão (receita 7.45 (HO 4.29 + 1.5×RIN 2.11) − custo 5.56 (óleo 4.76 + ind 0.80))
- 2026-11-12 | biodiesel_us | receita_usd_galao: 7.4515 USD/galão (HO 4.29 + 1.5×RIN 2.11)
- 2026-11-12 | complexo_soja | crush_margin_usd_bu: 1.945 USD/bushel (Board Crush: farelo 325.40 + oleo 63.42 − soja 1219.00)
- 2026-11-12 | complexo_soja | far_soj_ratio_pct: 80.08 % (farelo 325.40/sht ÷ (soja 1219.00cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-11-12 | complexo_soja | indice_sobra_farelo: 25.0 0-100 (sem sobra relevante (1/4 condições))

---

## inmet

- 2026-11-19 | cascavel_pr | temp_max_manha: 31.0 C (Cascavel/PR — Encoberto com chuvisco)
- 2026-11-19 | cascavel_pr | temp_max_noite: 31.0 C (Cascavel/PR — Encoberto)
- 2026-11-19 | cascavel_pr | temp_max_tarde: 31.0 C (Cascavel/PR — Encoberto)
- 2026-11-19 | cascavel_pr | temp_min_manha: 20.0 C (Cascavel/PR — Encoberto com chuvisco)
- 2026-11-19 | cascavel_pr | temp_min_noite: 20.0 C (Cascavel/PR — Encoberto)
- 2026-11-19 | cascavel_pr | temp_min_tarde: 20.0 C (Cascavel/PR — Encoberto)
- 2026-11-19 | cuiaba_mt | temp_max_manha: 33.0 C (Cuiaba/MT — Encoberto com chuvisco)
- 2026-11-19 | cuiaba_mt | temp_max_noite: 33.0 C (Cuiaba/MT — Encoberto)
- 2026-11-19 | cuiaba_mt | temp_max_tarde: 33.0 C (Cuiaba/MT — Encoberto)
- 2026-11-19 | cuiaba_mt | temp_min_manha: 25.0 C (Cuiaba/MT — Encoberto com chuvisco)
- 2026-11-19 | cuiaba_mt | temp_min_noite: 25.0 C (Cuiaba/MT — Encoberto)
- 2026-11-19 | cuiaba_mt | temp_min_tarde: 25.0 C (Cuiaba/MT — Encoberto)
- 2026-11-19 | lucas_rio_verde_mt | temp_max_manha: 34.0 C (Lucas do Rio Verde/MT — Encoberto com chuvisco)
- 2026-11-19 | lucas_rio_verde_mt | temp_max_noite: 34.0 C (Lucas do Rio Verde/MT — Encoberto)
- 2026-11-19 | lucas_rio_verde_mt | temp_max_tarde: 34.0 C (Lucas do Rio Verde/MT — Encoberto)
- 2026-11-19 | lucas_rio_verde_mt | temp_min_manha: 24.0 C (Lucas do Rio Verde/MT — Encoberto com chuvisco)
- 2026-11-19 | lucas_rio_verde_mt | temp_min_noite: 24.0 C (Lucas do Rio Verde/MT — Encoberto)
- 2026-11-19 | lucas_rio_verde_mt | temp_min_tarde: 24.0 C (Lucas do Rio Verde/MT — Encoberto)
- 2026-11-19 | maringa_pr | temp_max_manha: 29.0 C (Maringa/PR — Encoberto com chuva isolada)
- 2026-11-19 | maringa_pr | temp_max_noite: 29.0 C (Maringa/PR — Encoberto)
- 2026-11-19 | maringa_pr | temp_max_tarde: 29.0 C (Maringa/PR — Encoberto)
- 2026-11-19 | maringa_pr | temp_min_manha: 23.0 C (Maringa/PR — Encoberto com chuva isolada)
- 2026-11-19 | maringa_pr | temp_min_noite: 23.0 C (Maringa/PR — Encoberto)
- 2026-11-19 | maringa_pr | temp_min_tarde: 23.0 C (Maringa/PR — Encoberto)
- 2026-11-19 | passo_fundo_rs | temp_max_manha: 26.0 C (Passo Fundo/RS — Encoberto com chuvisco)
- 2026-11-19 | passo_fundo_rs | temp_max_noite: 26.0 C (Passo Fundo/RS — Encoberto)
- 2026-11-19 | passo_fundo_rs | temp_max_tarde: 26.0 C (Passo Fundo/RS — Encoberto)
- 2026-11-19 | passo_fundo_rs | temp_min_manha: 19.0 C (Passo Fundo/RS — Encoberto com chuvisco)
- 2026-11-19 | passo_fundo_rs | temp_min_noite: 19.0 C (Passo Fundo/RS — Encoberto)
- 2026-11-19 | passo_fundo_rs | temp_min_tarde: 19.0 C (Passo Fundo/RS — Encoberto)
- 2026-11-19 | rio_verde_go | temp_max_manha: 28.0 C (Rio Verde/GO — Encoberto com chuvisco)
- 2026-11-19 | rio_verde_go | temp_max_noite: 28.0 C (Rio Verde/GO — Encoberto)
- 2026-11-19 | rio_verde_go | temp_max_tarde: 28.0 C (Rio Verde/GO — Encoberto)
- 2026-11-19 | rio_verde_go | temp_min_manha: 21.0 C (Rio Verde/GO — Encoberto com chuvisco)
- 2026-11-19 | rio_verde_go | temp_min_noite: 21.0 C (Rio Verde/GO — Encoberto)
- 2026-11-19 | rio_verde_go | temp_min_tarde: 21.0 C (Rio Verde/GO — Encoberto)
- 2026-11-19 | sinop_mt | temp_max_manha: 33.0 C (Sinop/MT — Encoberto com chuvisco)
- 2026-11-19 | sinop_mt | temp_max_noite: 33.0 C (Sinop/MT — Encoberto)
- 2026-11-19 | sinop_mt | temp_max_tarde: 33.0 C (Sinop/MT — Encoberto)
- 2026-11-19 | sinop_mt | temp_min_manha: 24.0 C (Sinop/MT — Encoberto com chuvisco)
- 2026-11-19 | sinop_mt | temp_min_noite: 24.0 C (Sinop/MT — Encoberto)
- 2026-11-19 | sinop_mt | temp_min_tarde: 24.0 C (Sinop/MT — Encoberto)
- 2026-11-19 | sorriso_mt | temp_max_manha: 33.0 C (Sorriso/MT — Encoberto com chuva isolada)
- 2026-11-19 | sorriso_mt | temp_max_noite: 33.0 C (Sorriso/MT — Encoberto)
- 2026-11-19 | sorriso_mt | temp_max_tarde: 33.0 C (Sorriso/MT — Encoberto)
- 2026-11-19 | sorriso_mt | temp_min_manha: 24.0 C (Sorriso/MT — Encoberto com chuva isolada)
- 2026-11-19 | sorriso_mt | temp_min_noite: 24.0 C (Sorriso/MT — Encoberto)
- 2026-11-19 | sorriso_mt | temp_min_tarde: 24.0 C (Sorriso/MT — Encoberto)
- 2026-11-18 | cascavel_pr | temp_max_manha: 29.0 C (Cascavel/PR — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-18 | cascavel_pr | temp_max_noite: 29.0 C (Cascavel/PR — Muitas nuvens com pancadas de chuva e trovoadas isoladas)

---

## mpob

- 2026-11-18 | palma_malasia | page_fetched: 3209.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-17 | palma_malasia | page_fetched: 3209.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-16 | palma_malasia | page_fetched: 3209.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-15 | palma_malasia | page_fetched: 3209.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-14 | palma_malasia | page_fetched: 3209.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-13 | palma_malasia | page_fetched: 3209.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-12 | palma_malasia | page_fetched: 3209.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-11 | palma_malasia | page_fetched: 3209.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-10 | palma_malasia | page_fetched: 3208.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-09 | palma_malasia | page_fetched: 3201.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-08 | palma_malasia | page_fetched: 3201.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-07 | palma_malasia | page_fetched: 3201.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-06 | palma_malasia | page_fetched: 3201.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-05 | palma_malasia | page_fetched: 3201.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-04 | palma_malasia | page_fetched: 3201.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)

---

## noaa_cpc

- 2026-11-18 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-17 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-16 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-15 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-14 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-13 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-12 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-11 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-10 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-09 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-08 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-07 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-06 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-05 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-04 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)

---

## nopa

- 2026-11-18 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-17 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-16 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-15 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-14 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-13 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-12 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-11 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-10 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-09 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-08 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-07 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-06 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-05 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-04 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)

---

## noticias_rss

- 2026-11-18 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-17 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-16 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-15 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-14 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-13 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-12 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-11 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-10 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-09 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-08 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-07 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-06 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-05 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-04 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))

---

## usda_crop_progress

- 2026-11-15 | soybeans_eua | pct_harvested: 96.0 % (SOYBEANS - PROGRESS, MEASURED IN PCT HARVESTED)
- 2026-11-08 | soybeans_eua | pct_harvested: 92.0 % (SOYBEANS - PROGRESS, MEASURED IN PCT HARVESTED)

---

## usda_wasde

- 2026-11-10 | farelo_argentina | beginning_stocks_2024/2025: 2.26 mi_t (WASDE farelo | Argentina | 2024/2025)
- 2026-11-10 | farelo_argentina | beginning_stocks_2025/2026: 2.74 mi_t (WASDE farelo | Argentina | 2025/2026)
- 2026-11-10 | farelo_argentina | beginning_stocks_2026/2027_nov: 2.88 mi_t (WASDE farelo | Argentina | 2026/2027 [Nov])
- 2026-11-10 | farelo_argentina | beginning_stocks_2026/2027_oct: 2.83 mi_t (WASDE farelo | Argentina | 2026/2027 [Oct])
- 2026-11-10 | farelo_argentina | domestic_crush_2024/2025: 3.53 mi_t (WASDE farelo | Argentina | 2024/2025)
- 2026-11-10 | farelo_argentina | domestic_crush_2025/2026: 3.6 mi_t (WASDE farelo | Argentina | 2025/2026)
- 2026-11-10 | farelo_argentina | domestic_crush_2026/2027_nov: 3.65 mi_t (WASDE farelo | Argentina | 2026/2027 [Nov])
- 2026-11-10 | farelo_argentina | domestic_crush_2026/2027_oct: 3.65 mi_t (WASDE farelo | Argentina | 2026/2027 [Oct])
- 2026-11-10 | farelo_argentina | domestic_total_2024/2025: 29.78 mi_t (WASDE farelo | Argentina | 2024/2025)
- 2026-11-10 | farelo_argentina | domestic_total_2025/2026: 29.7 mi_t (WASDE farelo | Argentina | 2025/2026)
- 2026-11-10 | farelo_argentina | domestic_total_2026/2027_nov: 30.0 mi_t (WASDE farelo | Argentina | 2026/2027 [Nov])
- 2026-11-10 | farelo_argentina | domestic_total_2026/2027_oct: 30.0 mi_t (WASDE farelo | Argentina | 2026/2027 [Oct])
- 2026-11-10 | farelo_argentina | exports_2024/2025: 2.74 mi_t (WASDE farelo | Argentina | 2024/2025)
- 2026-11-10 | farelo_argentina | exports_2025/2026: 2.88 mi_t (WASDE farelo | Argentina | 2025/2026)
- 2026-11-10 | farelo_argentina | exports_2026/2027_nov: 3.07 mi_t (WASDE farelo | Argentina | 2026/2027 [Nov])
- 2026-11-10 | farelo_argentina | exports_2026/2027_oct: 3.02 mi_t (WASDE farelo | Argentina | 2026/2027 [Oct])
- 2026-11-10 | farelo_argentina | imports_2024/2025: 0.28 mi_t (WASDE farelo | Argentina | 2024/2025)
- 2026-11-10 | farelo_argentina | imports_2025/2026: 0.38 mi_t (WASDE farelo | Argentina | 2025/2026)
- 2026-11-10 | farelo_argentina | imports_2026/2027_nov: 0.35 mi_t (WASDE farelo | Argentina | 2026/2027 [Nov])
- 2026-11-10 | farelo_argentina | imports_2026/2027_oct: 0.35 mi_t (WASDE farelo | Argentina | 2026/2027 [Oct])
- 2026-11-10 | farelo_argentina | production_2024/2025: 33.51 mi_t (WASDE farelo | Argentina | 2024/2025)
- 2026-11-10 | farelo_argentina | production_2025/2026: 33.06 mi_t (WASDE farelo | Argentina | 2025/2026)
- 2026-11-10 | farelo_argentina | production_2026/2027_nov: 33.5 mi_t (WASDE farelo | Argentina | 2026/2027 [Nov])
- 2026-11-10 | farelo_argentina | production_2026/2027_oct: 33.5 mi_t (WASDE farelo | Argentina | 2026/2027 [Oct])
- 2026-11-10 | farelo_brazil | beginning_stocks_2024/2025: 0.22 mi_t (WASDE farelo | Brazil | 2024/2025)
- 2026-11-10 | farelo_brazil | beginning_stocks_2025/2026: 0.3 mi_t (WASDE farelo | Brazil | 2025/2026)
- 2026-11-10 | farelo_brazil | beginning_stocks_2026/2027_nov: 0.28 mi_t (WASDE farelo | Brazil | 2026/2027 [Nov])
- 2026-11-10 | farelo_brazil | beginning_stocks_2026/2027_oct: 0.2 mi_t (WASDE farelo | Brazil | 2026/2027 [Oct])
- 2026-11-10 | farelo_brazil | domestic_crush_2024/2025: 7.19 mi_t (WASDE farelo | Brazil | 2024/2025)
- 2026-11-10 | farelo_brazil | domestic_crush_2025/2026: 7.16 mi_t (WASDE farelo | Brazil | 2025/2026)
- 2026-11-10 | farelo_brazil | domestic_crush_2026/2027_nov: 7.18 mi_t (WASDE farelo | Brazil | 2026/2027 [Nov])
- 2026-11-10 | farelo_brazil | domestic_crush_2026/2027_oct: 7.1 mi_t (WASDE farelo | Brazil | 2026/2027 [Oct])
- 2026-11-10 | farelo_brazil | domestic_total_2024/2025: 1.78 mi_t (WASDE farelo | Brazil | 2024/2025)
- 2026-11-10 | farelo_brazil | domestic_total_2025/2026: 1.0 mi_t (WASDE farelo | Brazil | 2025/2026)
- 2026-11-10 | farelo_brazil | domestic_total_2026/2027_nov: 1.0 mi_t (WASDE farelo | Brazil | 2026/2027 [Nov])
- 2026-11-10 | farelo_brazil | domestic_total_2026/2027_oct: 1.0 mi_t (WASDE farelo | Brazil | 2026/2027 [Oct])
- 2026-11-10 | farelo_brazil | exports_2024/2025: 0.3 mi_t (WASDE farelo | Brazil | 2024/2025)
- 2026-11-10 | farelo_brazil | exports_2025/2026: 0.28 mi_t (WASDE farelo | Brazil | 2025/2026)
- 2026-11-10 | farelo_brazil | exports_2026/2027_nov: 0.28 mi_t (WASDE farelo | Brazil | 2026/2027 [Nov])
- 2026-11-10 | farelo_brazil | exports_2026/2027_oct: 0.2 mi_t (WASDE farelo | Brazil | 2026/2027 [Oct])
- 2026-11-10 | farelo_brazil | imports_2024/2025: 0.01 mi_t (WASDE farelo | Brazil | 2024/2025)
- 2026-11-10 | farelo_brazil | imports_2025/2026: 0.05 mi_t (WASDE farelo | Brazil | 2025/2026)
- 2026-11-10 | farelo_brazil | imports_2026/2027_nov: 0.1 mi_t (WASDE farelo | Brazil | 2026/2027 [Nov])
- 2026-11-10 | farelo_brazil | imports_2026/2027_oct: 0.1 mi_t (WASDE farelo | Brazil | 2026/2027 [Oct])
- 2026-11-10 | farelo_brazil | production_2024/2025: 9.04 mi_t (WASDE farelo | Brazil | 2024/2025)
- 2026-11-10 | farelo_brazil | production_2025/2026: 8.08 mi_t (WASDE farelo | Brazil | 2025/2026)
- 2026-11-10 | farelo_brazil | production_2026/2027_nov: 8.08 mi_t (WASDE farelo | Brazil | 2026/2027 [Nov])
- 2026-11-10 | farelo_brazil | production_2026/2027_oct: 8.0 mi_t (WASDE farelo | Brazil | 2026/2027 [Oct])
- 2026-11-10 | farelo_china | beginning_stocks_2024/2025: 0.79 mi_t (WASDE farelo | China | 2024/2025)
- 2026-11-10 | farelo_china | beginning_stocks_2025/2026: 0.94 mi_t (WASDE farelo | China | 2025/2026)

---

# FORECASTS ATIVOS (bandas estatisticas)

Bandas calculadas via MA20+volatilidade+slope curto. Claude Code DEVE refinar com drivers fundamentais.

| Geracao | Horizonte | Alvo | Commodity | Spot ref | Baixo | Central | Alto | Vies |
|---|---|---|---|---|---|---|---|---|
| 2026-11-18 | 7d | 2026-11-25 | farelo_cbot | 337.90 | 317.59 | 333.28 | 348.97 | baixista |
| 2026-11-18 | 7d | 2026-11-25 | oleo_cbot | 61.69 | 57.53 | 60.17 | 62.81 | baixista |
| 2026-11-18 | 7d | 2026-11-25 | soja_cbot | 1225.75 | 1169.82 | 1212.82 | 1255.81 | baixista |
| 2026-11-18 | 30d | 2026-12-18 | farelo_cbot | 337.90 | 287.71 | 320.19 | 352.68 | baixista |
| 2026-11-18 | 30d | 2026-12-18 | oleo_cbot | 61.69 | 49.08 | 54.54 | 60.01 | baixista |
| 2026-11-18 | 30d | 2026-12-18 | soja_cbot | 1225.75 | 1081.14 | 1170.15 | 1259.16 | baixista |
| 2026-11-17 | 7d | 2026-11-24 | farelo_cbot | 335.20 | 313.11 | 328.80 | 344.49 | baixista |
| 2026-11-17 | 7d | 2026-11-24 | oleo_cbot | 62.13 | 57.79 | 60.48 | 63.17 | baixista |
| 2026-11-17 | 7d | 2026-11-24 | soja_cbot | 1225.50 | 1167.41 | 1211.19 | 1254.96 | baixista |
| 2026-11-17 | 30d | 2026-12-17 | farelo_cbot | 335.20 | 275.07 | 307.55 | 340.03 | baixista |
| 2026-11-17 | 30d | 2026-12-17 | oleo_cbot | 62.13 | 49.56 | 55.13 | 60.70 | baixista |
| 2026-11-17 | 30d | 2026-12-17 | soja_cbot | 1225.50 | 1068.33 | 1158.95 | 1249.56 | baixista |
| 2026-11-16 | 7d | 2026-11-23 | farelo_cbot | 334.60 | 306.35 | 321.41 | 336.47 | baixista |
| 2026-11-16 | 7d | 2026-11-23 | oleo_cbot | 62.19 | 59.62 | 62.22 | 64.81 | baixista |
| 2026-11-16 | 7d | 2026-11-23 | soja_cbot | 1229.00 | 1168.12 | 1213.01 | 1257.90 | baixista |
| 2026-11-16 | 30d | 2026-12-16 | farelo_cbot | 334.60 | 261.29 | 292.47 | 323.64 | baixista |
| 2026-11-16 | 30d | 2026-12-16 | oleo_cbot | 62.19 | 51.67 | 57.04 | 62.42 | baixista |
| 2026-11-16 | 30d | 2026-12-16 | soja_cbot | 1229.00 | 1056.63 | 1149.57 | 1242.50 | baixista |
| 2026-11-15 | 7d | 2026-11-22 | farelo_cbot | 329.80 | 303.60 | 318.90 | 334.20 | baixista |
| 2026-11-15 | 7d | 2026-11-22 | oleo_cbot | 63.77 | 59.56 | 62.21 | 64.86 | baixista |
| 2026-11-15 | 7d | 2026-11-22 | soja_cbot | 1231.50 | 1162.73 | 1208.38 | 1254.03 | baixista |
| 2026-11-15 | 30d | 2026-12-15 | farelo_cbot | 329.80 | 250.93 | 282.60 | 314.27 | baixista |
| 2026-11-15 | 30d | 2026-12-15 | oleo_cbot | 63.77 | 51.33 | 56.81 | 62.30 | baixista |
| 2026-11-15 | 30d | 2026-12-15 | soja_cbot | 1231.50 | 1037.79 | 1132.30 | 1226.80 | baixista |

---


---

# Fila de julgamento — 2026-11-18

**8 item(ns).** Frase-gatilho: "lê a fila de julgamento e trata"

## 🔴 [nivel_tese] soja_cbot fechou em 1225.75 — acima da resistencia 1180.00
- id: `alerta-quebra_resistencia-soja_cbot-2026-11-18`
- fato: soja_cbot = 1225.75 vs nivel 1180.00 (2026-11-18)
- refs: soja_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] oleo_cbot fechou em 61.69 — abaixo do suporte 72.00
- id: `alerta-quebra_suporte-oleo_cbot-2026-11-18`
- fato: oleo_cbot = 61.69 vs nivel 72.00 (2026-11-18)
- refs: oleo_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] farelo_cbot fechou em 337.90 — acima da resistencia 325.00
- id: `alerta-quebra_resistencia-farelo_cbot-2026-11-18`
- fato: farelo_cbot = 337.90 vs nivel 325.00 (2026-11-18)
- refs: farelo_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] usd_brl_ptax fechou em 5.79 — acima da resistencia 5.30
- id: `alerta-quebra_resistencia-usd_brl_ptax-2026-11-17`
- fato: usd_brl_ptax = 5.79 vs nivel 5.30 (2026-11-17)
- refs: usd_brl_ptax
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] complexo_soja fechou em 1.96 — abaixo do suporte 2.50
- id: `alerta-quebra_suporte-complexo_soja-2026-11-18`
- fato: complexo_soja = 1.96 vs nivel 2.50 (2026-11-18)
- refs: complexo_soja
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [revisao] Revisao D+7 VENCIDA: Ratio Far/Soj 81,4% + FOB export zerado — spread far÷so
- id: `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
- fato: D+7 2026-06-18 — ratio fechou <80%? WASDE mudou o quadro? NOPA confirmou crush?
- refs: farelo,ratio-far-soj,spread
- leitura: A tese se confirmou? Atualizar status/insight.

## 🔴 [revisao] Revisao D+90 VENCIDA: Ratio Far/Soj 81,4% + FOB export zerado — spread far÷so
- id: `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`
- fato: D+90 2026-09-09 — o spread far÷soj reverteu ou seguiu comprimindo? O viés baixista no farelo se co
- refs: farelo,ratio-far-soj,spread
- leitura: A tese se confirmou? Atualizar status/insight.

## 🟡 [release] NOPA novo (2026-11-18)
- id: `release-nopa-2026-11-18`
- fato: fonte nopa com data 2026-11-18 — coletado, ainda nao interpretado
- refs: complexo_soja
- leitura: O numero muda o balanco/tese? Algo relevante pro farelo?

---
Trate só 🔴/🟡. Saída = `insights/*.md` (formato de generate_insights.txt, com `vies:`). Cite o `id` da fila no corpo do insight. Máx 1-3. Não duplicar insight recente.
