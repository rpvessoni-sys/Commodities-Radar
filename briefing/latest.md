# Briefing consolidado — 2026-10-20

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
- 2026-11-01 | farelo_brasil | estoque_final: 1101.4257219409003 mil_t (ABIOVE projecoes_mensais | farelo | mes 11/2026)
- 2026-11-01 | farelo_brasil | estoque_inicial: 1100.1295542061137 mil_t (ABIOVE projecoes_mensais | farelo | mes 11/2026)
- 2026-11-01 | farelo_brasil | exportacao: 800.0 mil_t (ABIOVE projecoes_mensais | farelo | mes 11/2026)
- 2026-11-01 | farelo_brasil | producao: 1977.5922854379314 mil_t (ABIOVE projecoes_mensais | farelo | mes 11/2026)
- 2026-11-01 | oleo_brasil | estoque_final: 315.25442492998815 mil_t (ABIOVE projecoes_mensais | oleo | mes 11/2026)
- 2026-11-01 | oleo_brasil | estoque_inicial: 306.38063039798806 mil_t (ABIOVE projecoes_mensais | oleo | mes 11/2026)
- 2026-11-01 | oleo_brasil | exportacao: 21.0 mil_t (ABIOVE projecoes_mensais | oleo | mes 11/2026)
- 2026-11-01 | oleo_brasil | producao: 494.90743667088356 mil_t (ABIOVE projecoes_mensais | oleo | mes 11/2026)
- 2026-11-01 | soja_brasil | esmagamento: 2626.6396067215023 mil_t (ABIOVE projecoes_mensais | soja | mes 11/2026)
- 2026-11-01 | soja_brasil | estoque_final: 3658.9889445987023 mil_t (ABIOVE projecoes_mensais | soja | mes 11/2026)
- 2026-11-01 | soja_brasil | estoque_inicial: 5720.771106475192 mil_t (ABIOVE projecoes_mensais | soja | mes 11/2026)
- 2026-11-01 | soja_brasil | exportacao: 108.0 mil_t (ABIOVE projecoes_mensais | soja | mes 11/2026)

---

## bcb

- 2026-10-19 | eur_brl_ptax | valor: 5.6682 BRL/EUR (sgs=21619)
- 2026-10-19 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-10-19 | usd_brl_ptax | valor: 5.0564 BRL/USD (sgs=1)
- 2026-10-16 | eur_brl_ptax | valor: 5.7088 BRL/EUR (sgs=21619)
- 2026-10-16 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-10-16 | usd_brl_ptax | valor: 5.0826 BRL/USD (sgs=1)
- 2026-10-15 | eur_brl_ptax | valor: 5.6609 BRL/EUR (sgs=21619)
- 2026-10-15 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-10-15 | usd_brl_ptax | valor: 5.0521 BRL/USD (sgs=1)
- 2026-10-14 | eur_brl_ptax | valor: 5.6111 BRL/EUR (sgs=21619)
- 2026-10-14 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-10-14 | usd_brl_ptax | valor: 5.0441 BRL/USD (sgs=1)
- 2026-10-13 | eur_brl_ptax | valor: 5.6092 BRL/EUR (sgs=21619)
- 2026-10-13 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-10-13 | usd_brl_ptax | valor: 5.0096 BRL/USD (sgs=1)
- 2026-10-09 | eur_brl_ptax | valor: 5.5844 BRL/EUR (sgs=21619)
- 2026-10-09 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-10-09 | usd_brl_ptax | valor: 4.9892 BRL/USD (sgs=1)
- 2026-10-08 | eur_brl_ptax | valor: 5.6093 BRL/EUR (sgs=21619)
- 2026-10-08 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-10-08 | usd_brl_ptax | valor: 5.0119 BRL/USD (sgs=1)
- 2026-10-07 | eur_brl_ptax | valor: 5.5867 BRL/EUR (sgs=21619)
- 2026-10-07 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-10-07 | usd_brl_ptax | valor: 4.9935 BRL/USD (sgs=1)
- 2026-10-06 | eur_brl_ptax | valor: 5.5975 BRL/EUR (sgs=21619)
- 2026-10-06 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-10-06 | usd_brl_ptax | valor: 4.9698 BRL/USD (sgs=1)

---

## cftc_cot

- 2026-10-13 | farelo_cbot | managed_money_long: 213072.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-10-13 | farelo_cbot | managed_money_net: 204643.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE — long - short)
- 2026-10-13 | farelo_cbot | managed_money_short: 8429.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-10-13 | farelo_cbot | open_interest: 644308.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-10-13 | farelo_cbot | producer_long: 72902.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-10-13 | farelo_cbot | producer_short: 427645.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-10-13 | farelo_cbot | swap_long: 132419.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-10-13 | farelo_cbot | swap_short: 17266.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-10-13 | oleo_cbot | managed_money_long: 114489.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-10-13 | oleo_cbot | managed_money_net: 87972.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE — long - short)
- 2026-10-13 | oleo_cbot | managed_money_short: 26517.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-10-13 | oleo_cbot | open_interest: 565878.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-10-13 | oleo_cbot | producer_long: 125077.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-10-13 | oleo_cbot | producer_short: 337642.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-10-13 | oleo_cbot | swap_long: 93238.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-10-13 | oleo_cbot | swap_short: 4840.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-10-13 | soja_cbot | managed_money_long: 285231.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-10-13 | soja_cbot | managed_money_net: 249807.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE — long - short)
- 2026-10-13 | soja_cbot | managed_money_short: 35424.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-10-13 | soja_cbot | open_interest: 1072235.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-10-13 | soja_cbot | producer_long: 310287.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-10-13 | soja_cbot | producer_short: 613265.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-10-13 | soja_cbot | swap_long: 122049.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-10-13 | soja_cbot | swap_short: 64810.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-10-06 | farelo_cbot | managed_money_long: 213268.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-10-06 | farelo_cbot | managed_money_net: 205301.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE — long - short)
- 2026-10-06 | farelo_cbot | managed_money_short: 7967.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-10-06 | farelo_cbot | open_interest: 632133.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-10-06 | farelo_cbot | producer_long: 68237.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-10-06 | farelo_cbot | producer_short: 429572.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-10-06 | farelo_cbot | swap_long: 129964.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-10-06 | farelo_cbot | swap_short: 13235.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-10-06 | oleo_cbot | managed_money_long: 116042.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-10-06 | oleo_cbot | managed_money_net: 93518.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE — long - short)
- 2026-10-06 | oleo_cbot | managed_money_short: 22524.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-10-06 | oleo_cbot | open_interest: 549657.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-10-06 | oleo_cbot | producer_long: 121463.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-10-06 | oleo_cbot | producer_short: 335277.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-10-06 | oleo_cbot | swap_long: 94568.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-10-06 | oleo_cbot | swap_short: 5942.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-10-06 | soja_cbot | managed_money_long: 289942.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-10-06 | soja_cbot | managed_money_net: 258066.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE — long - short)
- 2026-10-06 | soja_cbot | managed_money_short: 31876.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-10-06 | soja_cbot | open_interest: 1121298.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-10-06 | soja_cbot | producer_long: 338185.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-10-06 | soja_cbot | producer_short: 649952.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-10-06 | soja_cbot | swap_long: 126785.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-10-06 | soja_cbot | swap_short: 65015.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)

---

## cme_cbot

- 2026-10-20 | farelo_cbot | abertura: 354.79998779296875 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-20 | farelo_cbot | fechamento: 354.20001220703125 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-20 | farelo_cbot | fechamento_F27: 352.1000061035156 USD/short_ton (ticker=ZMF27.CBT venc=jan/27)
- 2026-10-20 | farelo_cbot | fechamento_H27: 350.0 USD/short_ton (ticker=ZMH27.CBT venc=mar/27)
- 2026-10-20 | farelo_cbot | fechamento_K27: 350.6000061035156 USD/short_ton (ticker=ZMK27.CBT venc=mai/27)
- 2026-10-20 | farelo_cbot | fechamento_N27: 353.29998779296875 USD/short_ton (ticker=ZMN27.CBT venc=jul/27)
- 2026-10-20 | farelo_cbot | fechamento_Z26: 354.20001220703125 USD/short_ton (ticker=ZMZ26.CBT venc=dez/26)
- 2026-10-20 | farelo_cbot | maxima: 354.79998779296875 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-20 | farelo_cbot | minima: 352.79998779296875 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-20 | farelo_cbot | volume: 1407.0 contratos (ticker=ZMZ26.CBT)
- 2026-10-20 | heating_oil_cbot | abertura: 4.7179999351501465 USD/galão (ticker=HO=F)
- 2026-10-20 | heating_oil_cbot | fechamento: 4.729800224304199 USD/galão (ticker=HO=F)
- 2026-10-20 | heating_oil_cbot | maxima: 4.736100196838379 USD/galão (ticker=HO=F)
- 2026-10-20 | heating_oil_cbot | minima: 4.716700077056885 USD/galão (ticker=HO=F)
- 2026-10-20 | heating_oil_cbot | volume: 348.0 contratos (ticker=HO=F)
- 2026-10-20 | oleo_cbot | abertura: 66.69999694824219 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-10-20 | oleo_cbot | fechamento: 66.66000366210938 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-10-20 | oleo_cbot | fechamento_F27: 66.81999969482422 USD_cts/lb (ticker=ZLF27.CBT venc=jan/27)
- 2026-10-20 | oleo_cbot | fechamento_H27: 67.05999755859375 USD_cts/lb (ticker=ZLH27.CBT venc=mar/27)
- 2026-10-20 | oleo_cbot | fechamento_K27: 67.31999969482422 USD_cts/lb (ticker=ZLK27.CBT venc=mai/27)
- 2026-10-20 | oleo_cbot | fechamento_N27: 67.37000274658203 USD_cts/lb (ticker=ZLN27.CBT venc=jul/27)
- 2026-10-20 | oleo_cbot | fechamento_Z26: 66.66000366210938 USD_cts/lb (ticker=ZLZ26.CBT venc=dez/26)
- 2026-10-20 | oleo_cbot | maxima: 66.75 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-10-20 | oleo_cbot | minima: 66.5999984741211 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-10-20 | oleo_cbot | volume: 1902.0 contratos (ticker=ZLZ26.CBT)
- 2026-10-20 | soja_cbot | abertura: 1267.25 USD/bushel (ticker=ZSF27.CBT)
- 2026-10-20 | soja_cbot | fechamento: 1266.5 USD/bushel (ticker=ZSF27.CBT)
- 2026-10-20 | soja_cbot | fechamento_F27: 1266.5 USD/bushel (ticker=ZSF27.CBT venc=jan/27)
- 2026-10-20 | soja_cbot | fechamento_H27: 1275.5 USD/bushel (ticker=ZSH27.CBT venc=mar/27)
- 2026-10-20 | soja_cbot | fechamento_K27: 1284.5 USD/bushel (ticker=ZSK27.CBT venc=mai/27)
- 2026-10-20 | soja_cbot | fechamento_N27: 1290.75 USD/bushel (ticker=ZSN27.CBT venc=jul/27)
- 2026-10-20 | soja_cbot | fechamento_Q27: 1277.0 USD/bushel (ticker=ZSQ27.CBT venc=ago/27)
- 2026-10-20 | soja_cbot | fechamento_X26: 1251.25 USD/bushel (ticker=ZSX26.CBT venc=nov/26)
- 2026-10-20 | soja_cbot | maxima: 1267.75 USD/bushel (ticker=ZSF27.CBT)
- 2026-10-20 | soja_cbot | minima: 1264.25 USD/bushel (ticker=ZSF27.CBT)
- 2026-10-20 | soja_cbot | volume: 981.0 contratos (ticker=ZSF27.CBT)
- 2026-10-19 | farelo_cbot | abertura: 354.79998779296875 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-19 | farelo_cbot | fechamento: 354.3999938964844 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-19 | farelo_cbot | fechamento_F27: 352.3999938964844 USD/short_ton (ticker=ZMF27.CBT venc=jan/27)
- 2026-10-19 | farelo_cbot | fechamento_H27: 350.20001220703125 USD/short_ton (ticker=ZMH27.CBT venc=mar/27)
- 2026-10-19 | farelo_cbot | fechamento_K27: 350.79998779296875 USD/short_ton (ticker=ZMK27.CBT venc=mai/27)
- 2026-10-19 | farelo_cbot | fechamento_N27: 353.5 USD/short_ton (ticker=ZMN27.CBT venc=jul/27)
- 2026-10-19 | farelo_cbot | fechamento_Z26: 354.3999938964844 USD/short_ton (ticker=ZMZ26.CBT venc=dez/26)
- 2026-10-19 | farelo_cbot | maxima: 354.79998779296875 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-19 | farelo_cbot | minima: 352.79998779296875 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-19 | farelo_cbot | volume: 1407.0 contratos (ticker=ZMZ26.CBT)
- 2026-10-19 | heating_oil_cbot | abertura: 4.7179999351501465 USD/galão (ticker=HO=F)
- 2026-10-19 | heating_oil_cbot | fechamento: 4.727200031280518 USD/galão (ticker=HO=F)
- 2026-10-19 | heating_oil_cbot | maxima: 4.736100196838379 USD/galão (ticker=HO=F)
- 2026-10-19 | heating_oil_cbot | minima: 4.716700077056885 USD/galão (ticker=HO=F)

---

## indicators

- 2026-10-20 | biodiesel_us | custo_oleo_usd_galao: 4.9995 USD/galão (7.5 lb × óleo 66.66 cts/lb)
- 2026-10-20 | biodiesel_us | margem_usd_galao: 2.0953 USD/galão (receita 7.89 (HO 4.73 + 1.5×RIN 2.11) − custo 5.80 (óleo 5.00 + ind 0.80))
- 2026-10-20 | biodiesel_us | receita_usd_galao: 7.8948 USD/galão (HO 4.73 + 1.5×RIN 2.11)
- 2026-10-20 | complexo_soja | crush_margin_usd_bu: 2.46 USD/bushel (Board Crush: farelo 354.20 + oleo 66.66 − soja 1266.50)
- 2026-10-20 | complexo_soja | far_soj_ratio_pct: 83.9 % (farelo 354.20/sht ÷ (soja 1266.50cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-10-20 | complexo_soja | indice_sobra_farelo: 80.0 0-100 (forte pressão baixista no farelo (4/5 condições))
- 2026-10-20 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-10-20 | complexo_soja | oil_meal_spread_usd_bu: -0.4598 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-10-20 | complexo_soja | oil_share_pct: 48.48 % (valor oleo 7.33 / total 15.13)
- 2026-10-20 | soja_paridade_br | brl_saca_paridade: 141.18 BRL/saca60kg (CBOT 1266.50 cts × USD/BRL 5.0564 (sem basis))
- 2026-10-19 | biodiesel_us | custo_oleo_usd_galao: 5.0025 USD/galão (7.5 lb × óleo 66.70 cts/lb)
- 2026-10-19 | biodiesel_us | margem_usd_galao: 2.0897 USD/galão (receita 7.89 (HO 4.73 + 1.5×RIN 2.11) − custo 5.80 (óleo 5.00 + ind 0.80))
- 2026-10-19 | biodiesel_us | receita_usd_galao: 7.8922 USD/galão (HO 4.73 + 1.5×RIN 2.11)
- 2026-10-19 | complexo_soja | crush_margin_usd_bu: 2.4513 USD/bushel (Board Crush: farelo 354.40 + oleo 66.70 − soja 1268.25)
- 2026-10-19 | complexo_soja | far_soj_ratio_pct: 83.83 % (farelo 354.40/sht ÷ (soja 1268.25cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-10-19 | complexo_soja | indice_sobra_farelo: 80.0 0-100 (forte pressão baixista no farelo (4/5 condições))
- 2026-10-19 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-10-19 | complexo_soja | oil_meal_spread_usd_bu: -0.4598 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-10-19 | complexo_soja | oil_share_pct: 48.48 % (valor oleo 7.34 / total 15.13)
- 2026-10-19 | soja_paridade_br | brl_saca_paridade: 141.38 BRL/saca60kg (CBOT 1268.25 cts × USD/BRL 5.0564 (sem basis))
- 2026-10-18 | complexo_soja | indice_sobra_farelo: 80.0 0-100 (forte pressão baixista no farelo (4/5 condições))
- 2026-10-18 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-10-17 | complexo_soja | indice_sobra_farelo: 80.0 0-100 (forte pressão baixista no farelo (4/5 condições))
- 2026-10-17 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-10-16 | biodiesel_us | custo_oleo_usd_galao: 5.0347 USD/galão (7.5 lb × óleo 67.13 cts/lb)
- 2026-10-16 | biodiesel_us | margem_usd_galao: 2.2294 USD/galão (receita 8.06 (HO 4.90 + 1.5×RIN 2.11) − custo 5.83 (óleo 5.03 + ind 0.80))
- 2026-10-16 | biodiesel_us | receita_usd_galao: 8.0641 USD/galão (HO 4.90 + 1.5×RIN 2.11)
- 2026-10-16 | complexo_soja | crush_margin_usd_bu: 2.483 USD/bushel (Board Crush: farelo 357.10 + oleo 67.13 − soja 1275.75)
- 2026-10-16 | complexo_soja | far_soj_ratio_pct: 83.97 % (farelo 357.10/sht ÷ (soja 1275.75cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-10-16 | complexo_soja | indice_sobra_farelo: 80.0 0-100 (forte pressão baixista no farelo (4/5 condições))
- 2026-10-16 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-10-16 | complexo_soja | oil_meal_spread_usd_bu: -0.4719 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-10-16 | complexo_soja | oil_share_pct: 48.45 % (valor oleo 7.38 / total 15.24)
- 2026-10-16 | soja_paridade_br | brl_saca_paridade: 142.95 BRL/saca60kg (CBOT 1275.75 cts × USD/BRL 5.0826 (sem basis))
- 2026-10-15 | biodiesel_us | custo_oleo_usd_galao: 5.0363 USD/galão (7.5 lb × óleo 67.15 cts/lb)
- 2026-10-15 | biodiesel_us | margem_usd_galao: 2.1744 USD/galão (receita 8.01 (HO 4.85 + 1.5×RIN 2.11) − custo 5.84 (óleo 5.04 + ind 0.80))
- 2026-10-15 | biodiesel_us | receita_usd_galao: 8.0106 USD/galão (HO 4.85 + 1.5×RIN 2.11)
- 2026-10-15 | complexo_soja | crush_margin_usd_bu: 2.5246 USD/bushel (Board Crush: farelo 359.80 + oleo 67.15 − soja 1277.75)
- 2026-10-15 | complexo_soja | far_soj_ratio_pct: 84.48 % (farelo 359.80/sht ÷ (soja 1277.75cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-10-15 | complexo_soja | indice_sobra_farelo: 80.0 0-100 (forte pressão baixista no farelo (4/5 condições))
- 2026-10-15 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-10-15 | complexo_soja | oil_meal_spread_usd_bu: -0.5291 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-10-15 | complexo_soja | oil_share_pct: 48.27 % (valor oleo 7.39 / total 15.30)
- 2026-10-15 | soja_paridade_br | brl_saca_paridade: 142.31 BRL/saca60kg (CBOT 1277.75 cts × USD/BRL 5.0521 (sem basis))
- 2026-10-14 | biodiesel_us | custo_oleo_usd_galao: 5.0295 USD/galão (7.5 lb × óleo 67.06 cts/lb)
- 2026-10-14 | biodiesel_us | margem_usd_galao: 2.2629 USD/galão (receita 8.09 (HO 4.93 + 1.5×RIN 2.11) − custo 5.83 (óleo 5.03 + ind 0.80))
- 2026-10-14 | biodiesel_us | receita_usd_galao: 8.0924 USD/galão (HO 4.93 + 1.5×RIN 2.11)
- 2026-10-14 | complexo_soja | crush_margin_usd_bu: 2.4756 USD/bushel (Board Crush: farelo 364.50 + oleo 67.06 − soja 1292.00)
- 2026-10-14 | complexo_soja | far_soj_ratio_pct: 84.64 % (farelo 364.50/sht ÷ (soja 1292.00cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-10-14 | complexo_soja | indice_sobra_farelo: 80.0 0-100 (forte pressão baixista no farelo (4/5 condições))

---

## inmet

- 2026-10-20 | cascavel_pr | temp_max_manha: 28.0 C (Cascavel/PR — Muitas nuvens)
- 2026-10-20 | cascavel_pr | temp_max_noite: 28.0 C (Cascavel/PR — Muitas nuvens)
- 2026-10-20 | cascavel_pr | temp_max_tarde: 28.0 C (Cascavel/PR — Muitas nuvens)
- 2026-10-20 | cascavel_pr | temp_min_manha: 12.0 C (Cascavel/PR — Muitas nuvens)
- 2026-10-20 | cascavel_pr | temp_min_noite: 12.0 C (Cascavel/PR — Muitas nuvens)
- 2026-10-20 | cascavel_pr | temp_min_tarde: 12.0 C (Cascavel/PR — Muitas nuvens)
- 2026-10-20 | cuiaba_mt | temp_max_manha: 36.0 C (Cuiaba/MT — Muitas nuvens)
- 2026-10-20 | cuiaba_mt | temp_max_noite: 36.0 C (Cuiaba/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-20 | cuiaba_mt | temp_max_tarde: 36.0 C (Cuiaba/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-20 | cuiaba_mt | temp_min_manha: 23.0 C (Cuiaba/MT — Muitas nuvens)
- 2026-10-20 | cuiaba_mt | temp_min_noite: 23.0 C (Cuiaba/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-20 | cuiaba_mt | temp_min_tarde: 23.0 C (Cuiaba/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-20 | lucas_rio_verde_mt | temp_max_manha: 37.0 C (Lucas do Rio Verde/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-20 | lucas_rio_verde_mt | temp_max_noite: 37.0 C (Lucas do Rio Verde/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-20 | lucas_rio_verde_mt | temp_max_tarde: 37.0 C (Lucas do Rio Verde/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-20 | lucas_rio_verde_mt | temp_min_manha: 25.0 C (Lucas do Rio Verde/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-20 | lucas_rio_verde_mt | temp_min_noite: 25.0 C (Lucas do Rio Verde/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-20 | lucas_rio_verde_mt | temp_min_tarde: 25.0 C (Lucas do Rio Verde/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-20 | maringa_pr | temp_max_manha: 29.0 C (Maringa/PR — Muitas nuvens)
- 2026-10-20 | maringa_pr | temp_max_noite: 29.0 C (Maringa/PR — Muitas nuvens)
- 2026-10-20 | maringa_pr | temp_max_tarde: 29.0 C (Maringa/PR — Poucas nuvens)
- 2026-10-20 | maringa_pr | temp_min_manha: 15.0 C (Maringa/PR — Muitas nuvens)
- 2026-10-20 | maringa_pr | temp_min_noite: 15.0 C (Maringa/PR — Muitas nuvens)
- 2026-10-20 | maringa_pr | temp_min_tarde: 15.0 C (Maringa/PR — Poucas nuvens)
- 2026-10-20 | passo_fundo_rs | temp_max_manha: 23.0 C (Passo Fundo/RS — Poucas nuvens com possibilidade de geada)
- 2026-10-20 | passo_fundo_rs | temp_max_noite: 23.0 C (Passo Fundo/RS — Muitas nuvens)
- 2026-10-20 | passo_fundo_rs | temp_max_tarde: 23.0 C (Passo Fundo/RS — Poucas nuvens)
- 2026-10-20 | passo_fundo_rs | temp_min_manha: 8.0 C (Passo Fundo/RS — Poucas nuvens com possibilidade de geada)
- 2026-10-20 | passo_fundo_rs | temp_min_noite: 8.0 C (Passo Fundo/RS — Muitas nuvens)
- 2026-10-20 | passo_fundo_rs | temp_min_tarde: 8.0 C (Passo Fundo/RS — Poucas nuvens)
- 2026-10-20 | rio_verde_go | temp_max_manha: 34.0 C (Rio Verde/GO — Poucas nuvens)
- 2026-10-20 | rio_verde_go | temp_max_noite: 34.0 C (Rio Verde/GO — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-20 | rio_verde_go | temp_max_tarde: 34.0 C (Rio Verde/GO — Muitas nuvens)
- 2026-10-20 | rio_verde_go | temp_min_manha: 19.0 C (Rio Verde/GO — Poucas nuvens)
- 2026-10-20 | rio_verde_go | temp_min_noite: 19.0 C (Rio Verde/GO — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-20 | rio_verde_go | temp_min_tarde: 19.0 C (Rio Verde/GO — Muitas nuvens)
- 2026-10-20 | sinop_mt | temp_max_manha: 39.0 C (Sinop/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-20 | sinop_mt | temp_max_noite: 39.0 C (Sinop/MT — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-20 | sinop_mt | temp_max_tarde: 39.0 C (Sinop/MT — Muitas nuvens com pancadas de chuva)
- 2026-10-20 | sinop_mt | temp_min_manha: 24.0 C (Sinop/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-20 | sinop_mt | temp_min_noite: 24.0 C (Sinop/MT — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-20 | sinop_mt | temp_min_tarde: 24.0 C (Sinop/MT — Muitas nuvens com pancadas de chuva)
- 2026-10-20 | sorriso_mt | temp_max_manha: 36.0 C (Sorriso/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-20 | sorriso_mt | temp_max_noite: 36.0 C (Sorriso/MT — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-20 | sorriso_mt | temp_max_tarde: 36.0 C (Sorriso/MT — Muitas nuvens com pancadas de chuva)
- 2026-10-20 | sorriso_mt | temp_min_manha: 25.0 C (Sorriso/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-20 | sorriso_mt | temp_min_noite: 25.0 C (Sorriso/MT — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-20 | sorriso_mt | temp_min_tarde: 25.0 C (Sorriso/MT — Muitas nuvens com pancadas de chuva)
- 2026-10-19 | cascavel_pr | temp_max_manha: 23.0 C (Cascavel/PR — Poucas nuvens)
- 2026-10-19 | cascavel_pr | temp_max_noite: 23.0 C (Cascavel/PR — Muitas nuvens)

---

## mpob

- 2026-10-20 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-19 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-18 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-17 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-16 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-15 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-14 | palma_malasia | page_fetched: 3200.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-13 | palma_malasia | page_fetched: 3200.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-12 | palma_malasia | page_fetched: 3200.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-11 | palma_malasia | page_fetched: 3200.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-10 | palma_malasia | page_fetched: 3200.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-09 | palma_malasia | page_fetched: 3200.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-08 | palma_malasia | page_fetched: 3200.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-07 | palma_malasia | page_fetched: 3200.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-06 | palma_malasia | page_fetched: 3200.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)

---

## noaa_cpc

- 2026-10-20 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-19 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-18 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-17 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-16 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-15 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-14 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-13 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-12 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-11 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-10 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-09 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-08 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-07 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-06 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)

---

## nopa

- 2026-10-20 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-19 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-18 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-17 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-16 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-15 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-14 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-13 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-12 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-11 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-10 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-09 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-08 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-07 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-06 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)

---

## noticias_rss

- 2026-10-20 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-10-19 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-10-18 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-10-17 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-10-16 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-10-15 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-10-14 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-10-13 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-10-12 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-10-11 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-10-10 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-10-09 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-10-08 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-10-07 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-10-06 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))

---

## usda_crop_progress

- 2026-10-18 | soybeans_eua | pct_harvested: 64.0 % (SOYBEANS - PROGRESS, MEASURED IN PCT HARVESTED)
- 2026-10-11 | soybeans_eua | cond_pct_excellent: 11.0 % (SOYBEANS - CONDITION, MEASURED IN PCT EXCELLENT)
- 2026-10-11 | soybeans_eua | cond_pct_good: 46.0 % (SOYBEANS - CONDITION, MEASURED IN PCT GOOD)
- 2026-10-11 | soybeans_eua | cond_pct_poor: 10.0 % (SOYBEANS - CONDITION, MEASURED IN PCT POOR)
- 2026-10-11 | soybeans_eua | pct_harvested: 46.0 % (SOYBEANS - PROGRESS, MEASURED IN PCT HARVESTED)

---

## usda_wasde

- 2026-10-09 | farelo_argentina | beginning_stocks_2024/2025: 2.26 mi_t (WASDE farelo | Argentina | 2024/2025)
- 2026-10-09 | farelo_argentina | beginning_stocks_2025/2026: 2.74 mi_t (WASDE farelo | Argentina | 2025/2026)
- 2026-10-09 | farelo_argentina | beginning_stocks_2026/2027_oct: 2.83 mi_t (WASDE farelo | Argentina | 2026/2027 [Oct])
- 2026-10-09 | farelo_argentina | beginning_stocks_2026/2027_sep: 2.83 mi_t (WASDE farelo | Argentina | 2026/2027 [Sep])
- 2026-10-09 | farelo_argentina | domestic_crush_2024/2025: 3.53 mi_t (WASDE farelo | Argentina | 2024/2025)
- 2026-10-09 | farelo_argentina | domestic_crush_2025/2026: 3.6 mi_t (WASDE farelo | Argentina | 2025/2026)
- 2026-10-09 | farelo_argentina | domestic_crush_2026/2027_oct: 3.65 mi_t (WASDE farelo | Argentina | 2026/2027 [Oct])
- 2026-10-09 | farelo_argentina | domestic_crush_2026/2027_sep: 3.65 mi_t (WASDE farelo | Argentina | 2026/2027 [Sep])
- 2026-10-09 | farelo_argentina | domestic_total_2024/2025: 29.78 mi_t (WASDE farelo | Argentina | 2024/2025)
- 2026-10-09 | farelo_argentina | domestic_total_2025/2026: 29.8 mi_t (WASDE farelo | Argentina | 2025/2026)
- 2026-10-09 | farelo_argentina | domestic_total_2026/2027_oct: 30.0 mi_t (WASDE farelo | Argentina | 2026/2027 [Oct])
- 2026-10-09 | farelo_argentina | domestic_total_2026/2027_sep: 29.6 mi_t (WASDE farelo | Argentina | 2026/2027 [Sep])
- 2026-10-09 | farelo_argentina | exports_2024/2025: 2.74 mi_t (WASDE farelo | Argentina | 2024/2025)
- 2026-10-09 | farelo_argentina | exports_2025/2026: 2.83 mi_t (WASDE farelo | Argentina | 2025/2026)
- 2026-10-09 | farelo_argentina | exports_2026/2027_oct: 3.02 mi_t (WASDE farelo | Argentina | 2026/2027 [Oct])
- 2026-10-09 | farelo_argentina | exports_2026/2027_sep: 2.99 mi_t (WASDE farelo | Argentina | 2026/2027 [Sep])
- 2026-10-09 | farelo_argentina | imports_2024/2025: 0.28 mi_t (WASDE farelo | Argentina | 2024/2025)
- 2026-10-09 | farelo_argentina | imports_2025/2026: 0.38 mi_t (WASDE farelo | Argentina | 2025/2026)
- 2026-10-09 | farelo_argentina | imports_2026/2027_oct: 0.35 mi_t (WASDE farelo | Argentina | 2026/2027 [Oct])
- 2026-10-09 | farelo_argentina | imports_2026/2027_sep: 0.3 mi_t (WASDE farelo | Argentina | 2026/2027 [Sep])
- 2026-10-09 | farelo_argentina | production_2024/2025: 33.51 mi_t (WASDE farelo | Argentina | 2024/2025)
- 2026-10-09 | farelo_argentina | production_2025/2026: 33.11 mi_t (WASDE farelo | Argentina | 2025/2026)
- 2026-10-09 | farelo_argentina | production_2026/2027_oct: 33.5 mi_t (WASDE farelo | Argentina | 2026/2027 [Oct])
- 2026-10-09 | farelo_argentina | production_2026/2027_sep: 33.11 mi_t (WASDE farelo | Argentina | 2026/2027 [Sep])
- 2026-10-09 | farelo_brazil | beginning_stocks_2024/2025: 0.22 mi_t (WASDE farelo | Brazil | 2024/2025)
- 2026-10-09 | farelo_brazil | beginning_stocks_2025/2026: 0.3 mi_t (WASDE farelo | Brazil | 2025/2026)
- 2026-10-09 | farelo_brazil | beginning_stocks_2026/2027_oct: 0.2 mi_t (WASDE farelo | Brazil | 2026/2027 [Oct])
- 2026-10-09 | farelo_brazil | beginning_stocks_2026/2027_sep: 0.2 mi_t (WASDE farelo | Brazil | 2026/2027 [Sep])
- 2026-10-09 | farelo_brazil | domestic_crush_2024/2025: 7.19 mi_t (WASDE farelo | Brazil | 2024/2025)
- 2026-10-09 | farelo_brazil | domestic_crush_2025/2026: 7.13 mi_t (WASDE farelo | Brazil | 2025/2026)
- 2026-10-09 | farelo_brazil | domestic_crush_2026/2027_oct: 7.1 mi_t (WASDE farelo | Brazil | 2026/2027 [Oct])
- 2026-10-09 | farelo_brazil | domestic_crush_2026/2027_sep: 7.1 mi_t (WASDE farelo | Brazil | 2026/2027 [Sep])
- 2026-10-09 | farelo_brazil | domestic_total_2024/2025: 1.78 mi_t (WASDE farelo | Brazil | 2024/2025)
- 2026-10-09 | farelo_brazil | domestic_total_2025/2026: 1.0 mi_t (WASDE farelo | Brazil | 2025/2026)
- 2026-10-09 | farelo_brazil | domestic_total_2026/2027_oct: 1.0 mi_t (WASDE farelo | Brazil | 2026/2027 [Oct])
- 2026-10-09 | farelo_brazil | domestic_total_2026/2027_sep: 1.0 mi_t (WASDE farelo | Brazil | 2026/2027 [Sep])
- 2026-10-09 | farelo_brazil | exports_2024/2025: 0.3 mi_t (WASDE farelo | Brazil | 2024/2025)
- 2026-10-09 | farelo_brazil | exports_2025/2026: 0.2 mi_t (WASDE farelo | Brazil | 2025/2026)
- 2026-10-09 | farelo_brazil | exports_2026/2027_oct: 0.2 mi_t (WASDE farelo | Brazil | 2026/2027 [Oct])
- 2026-10-09 | farelo_brazil | exports_2026/2027_sep: 0.2 mi_t (WASDE farelo | Brazil | 2026/2027 [Sep])
- 2026-10-09 | farelo_brazil | imports_2024/2025: 0.01 mi_t (WASDE farelo | Brazil | 2024/2025)
- 2026-10-09 | farelo_brazil | imports_2025/2026: 0.05 mi_t (WASDE farelo | Brazil | 2025/2026)
- 2026-10-09 | farelo_brazil | imports_2026/2027_oct: 0.1 mi_t (WASDE farelo | Brazil | 2026/2027 [Oct])
- 2026-10-09 | farelo_brazil | imports_2026/2027_sep: 0.1 mi_t (WASDE farelo | Brazil | 2026/2027 [Sep])
- 2026-10-09 | farelo_brazil | production_2024/2025: 9.04 mi_t (WASDE farelo | Brazil | 2024/2025)
- 2026-10-09 | farelo_brazil | production_2025/2026: 7.98 mi_t (WASDE farelo | Brazil | 2025/2026)
- 2026-10-09 | farelo_brazil | production_2026/2027_oct: 8.0 mi_t (WASDE farelo | Brazil | 2026/2027 [Oct])
- 2026-10-09 | farelo_brazil | production_2026/2027_sep: 8.0 mi_t (WASDE farelo | Brazil | 2026/2027 [Sep])
- 2026-10-09 | farelo_china | beginning_stocks_2024/2025: 0.79 mi_t (WASDE farelo | China | 2024/2025)
- 2026-10-09 | farelo_china | beginning_stocks_2025/2026: 0.94 mi_t (WASDE farelo | China | 2025/2026)

---

# FORECASTS ATIVOS (bandas estatisticas)

Bandas calculadas via MA20+volatilidade+slope curto. Claude Code DEVE refinar com drivers fundamentais.

| Geracao | Horizonte | Alvo | Commodity | Spot ref | Baixo | Central | Alto | Vies |
|---|---|---|---|---|---|---|---|---|
| 2026-10-20 | 7d | 2026-10-27 | farelo_cbot | 354.20 | 330.00 | 352.80 | 375.61 | lateral |
| 2026-10-20 | 7d | 2026-10-27 | oleo_cbot | 66.66 | 62.59 | 66.50 | 70.41 | lateral |
| 2026-10-20 | 7d | 2026-10-27 | soja_cbot | 1266.50 | 1204.01 | 1259.66 | 1315.32 | baixista |
| 2026-10-20 | 30d | 2026-11-19 | farelo_cbot | 354.20 | 299.52 | 346.73 | 393.94 | baixista |
| 2026-10-20 | 30d | 2026-11-19 | oleo_cbot | 66.66 | 57.58 | 65.67 | 73.77 | baixista |
| 2026-10-20 | 30d | 2026-11-19 | soja_cbot | 1266.50 | 1114.54 | 1229.77 | 1344.99 | baixista |
| 2026-10-19 | 7d | 2026-10-26 | farelo_cbot | 354.40 | 332.61 | 355.52 | 378.42 | baixista |
| 2026-10-19 | 7d | 2026-10-26 | oleo_cbot | 66.70 | 62.82 | 66.87 | 70.93 | lateral |
| 2026-10-19 | 7d | 2026-10-26 | soja_cbot | 1268.25 | 1192.08 | 1246.10 | 1300.13 | baixista |
| 2026-10-19 | 30d | 2026-11-18 | farelo_cbot | 354.40 | 300.99 | 348.40 | 395.81 | baixista |
| 2026-10-19 | 30d | 2026-11-18 | oleo_cbot | 66.70 | 58.09 | 66.49 | 74.89 | baixista |
| 2026-10-19 | 30d | 2026-11-18 | soja_cbot | 1268.25 | 1081.68 | 1193.52 | 1305.35 | baixista |
| 2026-10-18 | 7d | 2026-10-25 | farelo_cbot | 357.10 | 332.06 | 355.05 | 378.04 | baixista |
| 2026-10-18 | 7d | 2026-10-25 | oleo_cbot | 67.13 | 62.93 | 67.10 | 71.27 | lateral |
| 2026-10-18 | 7d | 2026-10-25 | soja_cbot | 1275.75 | 1193.56 | 1247.64 | 1301.71 | baixista |
| 2026-10-18 | 30d | 2026-11-17 | farelo_cbot | 357.10 | 299.56 | 347.16 | 394.76 | baixista |
| 2026-10-18 | 30d | 2026-11-17 | oleo_cbot | 67.13 | 58.14 | 66.76 | 75.39 | baixista |
| 2026-10-18 | 30d | 2026-11-17 | soja_cbot | 1275.75 | 1082.73 | 1194.68 | 1306.63 | baixista |
| 2026-10-17 | 7d | 2026-10-24 | farelo_cbot | 357.10 | 332.02 | 355.05 | 378.08 | baixista |
| 2026-10-17 | 7d | 2026-10-24 | oleo_cbot | 67.13 | 62.98 | 67.10 | 71.22 | lateral |
| 2026-10-17 | 7d | 2026-10-24 | soja_cbot | 1275.75 | 1192.77 | 1247.64 | 1302.50 | baixista |
| 2026-10-17 | 30d | 2026-11-16 | farelo_cbot | 357.10 | 299.48 | 347.16 | 394.85 | baixista |
| 2026-10-17 | 30d | 2026-11-16 | oleo_cbot | 67.13 | 58.24 | 66.76 | 75.29 | baixista |
| 2026-10-17 | 30d | 2026-11-16 | soja_cbot | 1275.75 | 1081.10 | 1194.68 | 1308.27 | baixista |

---


---

# Fila de julgamento — 2026-10-20

**7 item(ns).** Frase-gatilho: "lê a fila de julgamento e trata"

## 🔴 [nivel_tese] soja_cbot fechou em 1266.50 — acima da resistencia 1180.00
- id: `alerta-quebra_resistencia-soja_cbot-2026-10-20`
- fato: soja_cbot = 1266.50 vs nivel 1180.00 (2026-10-20)
- refs: soja_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] oleo_cbot fechou em 66.66 — abaixo do suporte 72.00
- id: `alerta-quebra_suporte-oleo_cbot-2026-10-20`
- fato: oleo_cbot = 66.66 vs nivel 72.00 (2026-10-20)
- refs: oleo_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] farelo_cbot fechou em 354.20 — acima da resistencia 325.00
- id: `alerta-quebra_resistencia-farelo_cbot-2026-10-20`
- fato: farelo_cbot = 354.20 vs nivel 325.00 (2026-10-20)
- refs: farelo_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] complexo_soja fechou em 2.46 — abaixo do suporte 2.50
- id: `alerta-quebra_suporte-complexo_soja-2026-10-20`
- fato: complexo_soja = 2.46 vs nivel 2.50 (2026-10-20)
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

## 🟡 [release] NOPA novo (2026-10-20)
- id: `release-nopa-2026-10-20`
- fato: fonte nopa com data 2026-10-20 — coletado, ainda nao interpretado
- refs: complexo_soja
- leitura: O numero muda o balanco/tese? Algo relevante pro farelo?

---
Trate só 🔴/🟡. Saída = `insights/*.md` (formato de generate_insights.txt, com `vies:`). Cite o `id` da fila no corpo do insight. Máx 1-3. Não duplicar insight recente.
