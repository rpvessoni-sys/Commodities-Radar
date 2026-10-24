# Briefing consolidado — 2026-10-24

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

- 2026-10-23 | eur_brl_ptax | valor: 5.6422 BRL/EUR (sgs=21619)
- 2026-10-23 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-10-23 | usd_brl_ptax | valor: 5.0377 BRL/USD (sgs=1)
- 2026-10-22 | eur_brl_ptax | valor: 5.6494 BRL/EUR (sgs=21619)
- 2026-10-22 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-10-22 | usd_brl_ptax | valor: 5.0383 BRL/USD (sgs=1)
- 2026-10-21 | eur_brl_ptax | valor: 5.6411 BRL/EUR (sgs=21619)
- 2026-10-21 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-10-21 | usd_brl_ptax | valor: 5.0277 BRL/USD (sgs=1)
- 2026-10-20 | eur_brl_ptax | valor: 5.6317 BRL/EUR (sgs=21619)
- 2026-10-20 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-10-20 | usd_brl_ptax | valor: 5.014 BRL/USD (sgs=1)
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

---

## cftc_cot

- 2026-10-20 | farelo_cbot | managed_money_long: 213717.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-10-20 | farelo_cbot | managed_money_net: 200878.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE — long - short)
- 2026-10-20 | farelo_cbot | managed_money_short: 12839.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-10-20 | farelo_cbot | open_interest: 635401.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-10-20 | farelo_cbot | producer_long: 66804.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-10-20 | farelo_cbot | producer_short: 414822.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-10-20 | farelo_cbot | swap_long: 134316.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-10-20 | farelo_cbot | swap_short: 15508.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-10-20 | oleo_cbot | managed_money_long: 104484.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-10-20 | oleo_cbot | managed_money_net: 71518.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE — long - short)
- 2026-10-20 | oleo_cbot | managed_money_short: 32966.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-10-20 | oleo_cbot | open_interest: 570462.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-10-20 | oleo_cbot | producer_long: 131862.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-10-20 | oleo_cbot | producer_short: 317608.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-10-20 | oleo_cbot | swap_long: 97172.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-10-20 | oleo_cbot | swap_short: 4819.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-10-20 | soja_cbot | managed_money_long: 259970.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-10-20 | soja_cbot | managed_money_net: 221325.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE — long - short)
- 2026-10-20 | soja_cbot | managed_money_short: 38645.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-10-20 | soja_cbot | open_interest: 1093612.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-10-20 | soja_cbot | producer_long: 329927.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-10-20 | soja_cbot | producer_short: 617362.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-10-20 | soja_cbot | swap_long: 124730.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-10-20 | soja_cbot | swap_short: 58933.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
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

---

## cme_cbot

- 2026-10-23 | farelo_cbot | abertura: 347.29998779296875 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-23 | farelo_cbot | fechamento: 346.5 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-23 | farelo_cbot | fechamento_F27: 345.1000061035156 USD/short_ton (ticker=ZMF27.CBT venc=jan/27)
- 2026-10-23 | farelo_cbot | fechamento_H27: 344.8999938964844 USD/short_ton (ticker=ZMH27.CBT venc=mar/27)
- 2026-10-23 | farelo_cbot | fechamento_K27: 346.70001220703125 USD/short_ton (ticker=ZMK27.CBT venc=mai/27)
- 2026-10-23 | farelo_cbot | fechamento_N27: 350.29998779296875 USD/short_ton (ticker=ZMN27.CBT venc=jul/27)
- 2026-10-23 | farelo_cbot | fechamento_Z26: 346.5 USD/short_ton (ticker=ZMZ26.CBT venc=dez/26)
- 2026-10-23 | farelo_cbot | maxima: 350.70001220703125 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-23 | farelo_cbot | minima: 345.6000061035156 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-23 | farelo_cbot | volume: 56735.0 contratos (ticker=ZMZ26.CBT)
- 2026-10-23 | heating_oil_cbot | abertura: 4.764599800109863 USD/galão (ticker=HO=F)
- 2026-10-23 | heating_oil_cbot | fechamento: 4.803899765014648 USD/galão (ticker=HO=F)
- 2026-10-23 | heating_oil_cbot | maxima: 4.832600116729736 USD/galão (ticker=HO=F)
- 2026-10-23 | heating_oil_cbot | minima: 4.695700168609619 USD/galão (ticker=HO=F)
- 2026-10-23 | heating_oil_cbot | volume: 39045.0 contratos (ticker=HO=F)
- 2026-10-23 | oleo_cbot | abertura: 66.9000015258789 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-10-23 | oleo_cbot | fechamento: 66.79000091552734 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-10-23 | oleo_cbot | fechamento_F27: 67.0 USD_cts/lb (ticker=ZLF27.CBT venc=jan/27)
- 2026-10-23 | oleo_cbot | fechamento_H27: 67.29000091552734 USD_cts/lb (ticker=ZLH27.CBT venc=mar/27)
- 2026-10-23 | oleo_cbot | fechamento_K27: 67.55000305175781 USD_cts/lb (ticker=ZLK27.CBT venc=mai/27)
- 2026-10-23 | oleo_cbot | fechamento_N27: 67.58999633789062 USD_cts/lb (ticker=ZLN27.CBT venc=jul/27)
- 2026-10-23 | oleo_cbot | fechamento_Z26: 66.79000091552734 USD_cts/lb (ticker=ZLZ26.CBT venc=dez/26)
- 2026-10-23 | oleo_cbot | maxima: 67.29000091552734 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-10-23 | oleo_cbot | minima: 66.36000061035156 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-10-23 | oleo_cbot | volume: 56941.0 contratos (ticker=ZLZ26.CBT)
- 2026-10-23 | soja_cbot | abertura: 1264.75 USD/bushel (ticker=ZSF27.CBT)
- 2026-10-23 | soja_cbot | fechamento: 1269.5 USD/bushel (ticker=ZSF27.CBT)
- 2026-10-23 | soja_cbot | fechamento_F27: 1269.5 USD/bushel (ticker=ZSF27.CBT venc=jan/27)
- 2026-10-23 | soja_cbot | fechamento_H27: 1276.5 USD/bushel (ticker=ZSH27.CBT venc=mar/27)
- 2026-10-23 | soja_cbot | fechamento_K27: 1284.25 USD/bushel (ticker=ZSK27.CBT venc=mai/27)
- 2026-10-23 | soja_cbot | fechamento_N27: 1289.25 USD/bushel (ticker=ZSN27.CBT venc=jul/27)
- 2026-10-23 | soja_cbot | fechamento_Q27: 1273.25 USD/bushel (ticker=ZSQ27.CBT venc=ago/27)
- 2026-10-23 | soja_cbot | fechamento_X26: 1257.5 USD/bushel (ticker=ZSX26.CBT venc=nov/26)
- 2026-10-23 | soja_cbot | maxima: 1275.5 USD/bushel (ticker=ZSF27.CBT)
- 2026-10-23 | soja_cbot | minima: 1263.5 USD/bushel (ticker=ZSF27.CBT)
- 2026-10-23 | soja_cbot | volume: 134494.0 contratos (ticker=ZSF27.CBT)
- 2026-10-22 | farelo_cbot | abertura: 348.29998779296875 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-22 | farelo_cbot | fechamento: 347.29998779296875 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-22 | farelo_cbot | maxima: 351.29998779296875 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-22 | farelo_cbot | minima: 346.1000061035156 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-22 | farelo_cbot | volume: 110471.0 contratos (ticker=ZMZ26.CBT)
- 2026-10-22 | heating_oil_cbot | abertura: 4.7967000007629395 USD/galão (ticker=HO=F)
- 2026-10-22 | heating_oil_cbot | fechamento: 4.93209981918335 USD/galão (ticker=HO=F)
- 2026-10-22 | heating_oil_cbot | maxima: 4.9618000984191895 USD/galão (ticker=HO=F)
- 2026-10-22 | heating_oil_cbot | minima: 4.7855000495910645 USD/galão (ticker=HO=F)
- 2026-10-22 | heating_oil_cbot | volume: 29753.0 contratos (ticker=HO=F)
- 2026-10-22 | oleo_cbot | abertura: 66.0 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-10-22 | oleo_cbot | fechamento: 66.73999786376953 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-10-22 | oleo_cbot | maxima: 67.1500015258789 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-10-22 | oleo_cbot | minima: 65.80000305175781 USD_cts/lb (ticker=ZLZ26.CBT)

---

## indicators

- 2026-10-24 | complexo_soja | indice_sobra_farelo: 75.0 0-100 (sobra relevante (3/4 condições))
- 2026-10-24 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-10-23 | biodiesel_us | custo_oleo_usd_galao: 5.0093 USD/galão (7.5 lb × óleo 66.79 cts/lb)
- 2026-10-23 | biodiesel_us | margem_usd_galao: 2.1596 USD/galão (receita 7.97 (HO 4.80 + 1.5×RIN 2.11) − custo 5.81 (óleo 5.01 + ind 0.80))
- 2026-10-23 | biodiesel_us | receita_usd_galao: 7.9689 USD/galão (HO 4.80 + 1.5×RIN 2.11)
- 2026-10-23 | complexo_soja | crush_margin_usd_bu: 2.2749 USD/bushel (Board Crush: farelo 346.50 + oleo 66.79 − soja 1269.50)
- 2026-10-23 | complexo_soja | far_soj_ratio_pct: 81.88 % (farelo 346.50/sht ÷ (soja 1269.50cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-10-23 | complexo_soja | indice_sobra_farelo: 50.0 0-100 (pressão moderada (1/2 condições))
- 2026-10-23 | complexo_soja | indice_suporte_oleo: 75.0 0-100 (suporte relevante (3/4 condições))
- 2026-10-23 | complexo_soja | oil_meal_spread_usd_bu: -0.2761 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-10-23 | complexo_soja | oil_share_pct: 49.08 % (valor oleo 7.35 / total 14.97)
- 2026-10-23 | soja_paridade_br | brl_saca_paridade: 140.99 BRL/saca60kg (CBOT 1269.50 cts × USD/BRL 5.0377 (sem basis))
- 2026-10-22 | biodiesel_us | custo_oleo_usd_galao: 5.0055 USD/galão (7.5 lb × óleo 66.74 cts/lb)
- 2026-10-22 | biodiesel_us | margem_usd_galao: 2.2916 USD/galão (receita 8.10 (HO 4.93 + 1.5×RIN 2.11) − custo 5.81 (óleo 5.01 + ind 0.80))
- 2026-10-22 | biodiesel_us | receita_usd_galao: 8.0971 USD/galão (HO 4.93 + 1.5×RIN 2.11)
- 2026-10-22 | complexo_soja | crush_margin_usd_bu: 2.3345 USD/bushel (Board Crush: farelo 347.30 + oleo 66.74 − soja 1264.75)
- 2026-10-22 | complexo_soja | far_soj_ratio_pct: 82.38 % (farelo 347.30/sht ÷ (soja 1264.75cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-10-22 | complexo_soja | oil_meal_spread_usd_bu: -0.2992 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-10-22 | complexo_soja | oil_share_pct: 49.0 % (valor oleo 7.34 / total 14.98)
- 2026-10-22 | soja_paridade_br | brl_saca_paridade: 140.48 BRL/saca60kg (CBOT 1264.75 cts × USD/BRL 5.0383 (sem basis))
- 2026-10-21 | biodiesel_us | custo_oleo_usd_galao: 4.9478 USD/galão (7.5 lb × óleo 65.97 cts/lb)
- 2026-10-21 | biodiesel_us | margem_usd_galao: 2.1805 USD/galão (receita 7.93 (HO 4.76 + 1.5×RIN 2.11) − custo 5.75 (óleo 4.95 + ind 0.80))
- 2026-10-21 | biodiesel_us | receita_usd_galao: 7.9283 USD/galão (HO 4.76 + 1.5×RIN 2.11)
- 2026-10-21 | complexo_soja | crush_margin_usd_bu: 2.3368 USD/bushel (Board Crush: farelo 348.30 + oleo 65.97 − soja 1258.25)
- 2026-10-21 | complexo_soja | far_soj_ratio_pct: 83.04 % (farelo 348.30/sht ÷ (soja 1258.25cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-10-21 | complexo_soja | oil_meal_spread_usd_bu: -0.4059 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-10-21 | complexo_soja | oil_share_pct: 48.64 % (valor oleo 7.26 / total 14.92)
- 2026-10-21 | soja_paridade_br | brl_saca_paridade: 139.47 BRL/saca60kg (CBOT 1258.25 cts × USD/BRL 5.0277 (sem basis))
- 2026-10-20 | biodiesel_us | custo_oleo_usd_galao: 5.0048 USD/galão (7.5 lb × óleo 66.73 cts/lb)
- 2026-10-20 | biodiesel_us | margem_usd_galao: 2.2852 USD/galão (receita 8.09 (HO 4.93 + 1.5×RIN 2.11) − custo 5.80 (óleo 5.00 + ind 0.80))
- 2026-10-20 | biodiesel_us | receita_usd_galao: 8.09 USD/galão (HO 4.93 + 1.5×RIN 2.11)
- 2026-10-20 | complexo_soja | crush_margin_usd_bu: 2.3767 USD/bushel (Board Crush: farelo 348.70 + oleo 66.73 − soja 1263.50)
- 2026-10-20 | complexo_soja | far_soj_ratio_pct: 82.79 % (farelo 348.70/sht ÷ (soja 1263.50cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-10-20 | complexo_soja | oil_meal_spread_usd_bu: -0.3311 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-10-20 | complexo_soja | oil_share_pct: 48.9 % (valor oleo 7.34 / total 15.01)
- 2026-10-20 | soja_paridade_br | brl_saca_paridade: 139.67 BRL/saca60kg (CBOT 1263.50 cts × USD/BRL 5.0140 (sem basis))
- 2026-10-19 | biodiesel_us | custo_oleo_usd_galao: 5.0018 USD/galão (7.5 lb × óleo 66.69 cts/lb)
- 2026-10-19 | biodiesel_us | margem_usd_galao: 2.2834 USD/galão (receita 8.09 (HO 4.92 + 1.5×RIN 2.11) − custo 5.80 (óleo 5.00 + ind 0.80))
- 2026-10-19 | biodiesel_us | receita_usd_galao: 8.0851 USD/galão (HO 4.92 + 1.5×RIN 2.11)
- 2026-10-19 | complexo_soja | crush_margin_usd_bu: 2.454 USD/bushel (Board Crush: farelo 354.80 + oleo 66.69 − soja 1268.75)
- 2026-10-19 | complexo_soja | far_soj_ratio_pct: 83.89 % (farelo 354.80/sht ÷ (soja 1268.75cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-10-19 | complexo_soja | oil_meal_spread_usd_bu: -0.4697 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-10-19 | complexo_soja | oil_share_pct: 48.45 % (valor oleo 7.34 / total 15.14)
- 2026-10-19 | soja_paridade_br | brl_saca_paridade: 141.43 BRL/saca60kg (CBOT 1268.75 cts × USD/BRL 5.0564 (sem basis))
- 2026-10-16 | biodiesel_us | custo_oleo_usd_galao: 5.0347 USD/galão (7.5 lb × óleo 67.13 cts/lb)
- 2026-10-16 | biodiesel_us | margem_usd_galao: 2.2294 USD/galão (receita 8.06 (HO 4.90 + 1.5×RIN 2.11) − custo 5.83 (óleo 5.03 + ind 0.80))
- 2026-10-16 | biodiesel_us | receita_usd_galao: 8.0641 USD/galão (HO 4.90 + 1.5×RIN 2.11)
- 2026-10-16 | complexo_soja | crush_margin_usd_bu: 2.483 USD/bushel (Board Crush: farelo 357.10 + oleo 67.13 − soja 1275.75)
- 2026-10-16 | complexo_soja | far_soj_ratio_pct: 83.97 % (farelo 357.10/sht ÷ (soja 1275.75cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-10-16 | complexo_soja | oil_meal_spread_usd_bu: -0.4719 USD/bushel (Oleo - Farelo (positivo = oleo manda))

---

## inmet

- 2026-10-24 | cascavel_pr | temp_max_manha: 27.0 C (Cascavel/PR — Nublado com pancadas de chuva e trovoadas)
- 2026-10-24 | cascavel_pr | temp_max_noite: 27.0 C (Cascavel/PR — Nublado com pancadas de chuva e trovoadas)
- 2026-10-24 | cascavel_pr | temp_max_tarde: 27.0 C (Cascavel/PR — Nublado com pancadas de chuva e trovoadas)
- 2026-10-24 | cascavel_pr | temp_min_manha: 18.0 C (Cascavel/PR — Nublado com pancadas de chuva e trovoadas)
- 2026-10-24 | cascavel_pr | temp_min_noite: 18.0 C (Cascavel/PR — Nublado com pancadas de chuva e trovoadas)
- 2026-10-24 | cascavel_pr | temp_min_tarde: 18.0 C (Cascavel/PR — Nublado com pancadas de chuva e trovoadas)
- 2026-10-24 | cuiaba_mt | temp_max_manha: 38.0 C (Cuiaba/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-24 | cuiaba_mt | temp_max_noite: 38.0 C (Cuiaba/MT — Muitas nuvens)
- 2026-10-24 | cuiaba_mt | temp_max_tarde: 38.0 C (Cuiaba/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-24 | cuiaba_mt | temp_min_manha: 29.0 C (Cuiaba/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-24 | cuiaba_mt | temp_min_noite: 29.0 C (Cuiaba/MT — Muitas nuvens)
- 2026-10-24 | cuiaba_mt | temp_min_tarde: 29.0 C (Cuiaba/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-24 | lucas_rio_verde_mt | temp_max_manha: 39.0 C (Lucas do Rio Verde/MT — Muitas nuvens)
- 2026-10-24 | lucas_rio_verde_mt | temp_max_noite: 39.0 C (Lucas do Rio Verde/MT — Muitas nuvens)
- 2026-10-24 | lucas_rio_verde_mt | temp_max_tarde: 39.0 C (Lucas do Rio Verde/MT — Muitas nuvens)
- 2026-10-24 | lucas_rio_verde_mt | temp_min_manha: 24.0 C (Lucas do Rio Verde/MT — Muitas nuvens)
- 2026-10-24 | lucas_rio_verde_mt | temp_min_noite: 24.0 C (Lucas do Rio Verde/MT — Muitas nuvens)
- 2026-10-24 | lucas_rio_verde_mt | temp_min_tarde: 24.0 C (Lucas do Rio Verde/MT — Muitas nuvens)
- 2026-10-24 | maringa_pr | temp_max_manha: 34.0 C (Maringa/PR — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-24 | maringa_pr | temp_max_noite: 34.0 C (Maringa/PR — Nublado com pancadas de chuva e trovoadas)
- 2026-10-24 | maringa_pr | temp_max_tarde: 34.0 C (Maringa/PR — Nublado com pancadas de chuva e trovoadas)
- 2026-10-24 | maringa_pr | temp_min_manha: 22.0 C (Maringa/PR — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-24 | maringa_pr | temp_min_noite: 22.0 C (Maringa/PR — Nublado com pancadas de chuva e trovoadas)
- 2026-10-24 | maringa_pr | temp_min_tarde: 22.0 C (Maringa/PR — Nublado com pancadas de chuva e trovoadas)
- 2026-10-24 | passo_fundo_rs | temp_max_manha: 20.0 C (Passo Fundo/RS — Nublado com pancadas de chuva e trovoadas)
- 2026-10-24 | passo_fundo_rs | temp_max_noite: 20.0 C (Passo Fundo/RS — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-24 | passo_fundo_rs | temp_max_tarde: 20.0 C (Passo Fundo/RS — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-24 | passo_fundo_rs | temp_min_manha: 13.0 C (Passo Fundo/RS — Nublado com pancadas de chuva e trovoadas)
- 2026-10-24 | passo_fundo_rs | temp_min_noite: 13.0 C (Passo Fundo/RS — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-24 | passo_fundo_rs | temp_min_tarde: 13.0 C (Passo Fundo/RS — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-24 | rio_verde_go | temp_max_manha: 34.0 C (Rio Verde/GO — Muitas nuvens)
- 2026-10-24 | rio_verde_go | temp_max_noite: 34.0 C (Rio Verde/GO — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-24 | rio_verde_go | temp_max_tarde: 34.0 C (Rio Verde/GO — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-24 | rio_verde_go | temp_min_manha: 21.0 C (Rio Verde/GO — Muitas nuvens)
- 2026-10-24 | rio_verde_go | temp_min_noite: 21.0 C (Rio Verde/GO — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-24 | rio_verde_go | temp_min_tarde: 21.0 C (Rio Verde/GO — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-24 | sinop_mt | temp_max_manha: 39.0 C (Sinop/MT — Muitas nuvens)
- 2026-10-24 | sinop_mt | temp_max_noite: 39.0 C (Sinop/MT — Muitas nuvens)
- 2026-10-24 | sinop_mt | temp_max_tarde: 39.0 C (Sinop/MT — Muitas nuvens)
- 2026-10-24 | sinop_mt | temp_min_manha: 25.0 C (Sinop/MT — Muitas nuvens)
- 2026-10-24 | sinop_mt | temp_min_noite: 25.0 C (Sinop/MT — Muitas nuvens)
- 2026-10-24 | sinop_mt | temp_min_tarde: 25.0 C (Sinop/MT — Muitas nuvens)
- 2026-10-24 | sorriso_mt | temp_max_manha: 38.0 C (Sorriso/MT — Muitas nuvens)
- 2026-10-24 | sorriso_mt | temp_max_noite: 38.0 C (Sorriso/MT — Muitas nuvens)
- 2026-10-24 | sorriso_mt | temp_max_tarde: 38.0 C (Sorriso/MT — Muitas nuvens)
- 2026-10-24 | sorriso_mt | temp_min_manha: 24.0 C (Sorriso/MT — Muitas nuvens)
- 2026-10-24 | sorriso_mt | temp_min_noite: 24.0 C (Sorriso/MT — Muitas nuvens)
- 2026-10-24 | sorriso_mt | temp_min_tarde: 24.0 C (Sorriso/MT — Muitas nuvens)
- 2026-10-23 | cascavel_pr | temp_max_manha: 25.0 C (Cascavel/PR — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-23 | cascavel_pr | temp_max_noite: 25.0 C (Cascavel/PR — Muitas nuvens com pancadas de chuva e trovoadas isoladas)

---

## mpob

- 2026-10-24 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)

---

## noaa_cpc

- 2026-10-24 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)

---

## nopa

- 2026-10-24 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)

---

## noticias_rss

- 2026-10-24 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))

---

## usda_crop_progress

- 2026-10-18 | soybeans_eua | pct_harvested: 64.0 % (SOYBEANS - PROGRESS, MEASURED IN PCT HARVESTED)
- 2026-10-11 | soybeans_eua | cond_pct_excellent: 11.0 % (SOYBEANS - CONDITION, MEASURED IN PCT EXCELLENT)
- 2026-10-11 | soybeans_eua | cond_pct_good: 46.0 % (SOYBEANS - CONDITION, MEASURED IN PCT GOOD)
- 2026-10-11 | soybeans_eua | cond_pct_poor: 10.0 % (SOYBEANS - CONDITION, MEASURED IN PCT POOR)
- 2026-10-11 | soybeans_eua | pct_harvested: 46.0 % (SOYBEANS - PROGRESS, MEASURED IN PCT HARVESTED)

---

# FORECASTS ATIVOS (bandas estatisticas)

Bandas calculadas via MA20+volatilidade+slope curto. Claude Code DEVE refinar com drivers fundamentais.

| Geracao | Horizonte | Alvo | Commodity | Spot ref | Baixo | Central | Alto | Vies |
|---|---|---|---|---|---|---|---|---|
| 2026-10-24 | 7d | 2026-10-31 | farelo_cbot | 346.50 | 319.61 | 335.24 | 350.87 | baixista |
| 2026-10-24 | 7d | 2026-10-31 | oleo_cbot | 66.79 | 63.50 | 65.64 | 67.78 | baixista |
| 2026-10-24 | 7d | 2026-10-31 | soja_cbot | 1269.50 | 1213.97 | 1238.51 | 1263.05 | baixista |
| 2026-10-24 | 30d | 2026-11-23 | farelo_cbot | 346.50 | 263.31 | 295.67 | 328.02 | baixista |
| 2026-10-24 | 30d | 2026-11-23 | oleo_cbot | 66.79 | 57.33 | 61.75 | 66.18 | baixista |
| 2026-10-24 | 30d | 2026-11-23 | soja_cbot | 1269.50 | 1082.67 | 1133.47 | 1184.27 | baixista |

---


---

# Fila de julgamento — 2026-10-24

**7 item(ns).** Frase-gatilho: "lê a fila de julgamento e trata"

## 🔴 [nivel_tese] soja_cbot fechou em 1269.50 — acima da resistencia 1180.00
- id: `alerta-quebra_resistencia-soja_cbot-2026-10-23`
- fato: soja_cbot = 1269.50 vs nivel 1180.00 (2026-10-23)
- refs: soja_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] oleo_cbot fechou em 66.79 — abaixo do suporte 72.00
- id: `alerta-quebra_suporte-oleo_cbot-2026-10-23`
- fato: oleo_cbot = 66.79 vs nivel 72.00 (2026-10-23)
- refs: oleo_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] farelo_cbot fechou em 346.50 — acima da resistencia 325.00
- id: `alerta-quebra_resistencia-farelo_cbot-2026-10-23`
- fato: farelo_cbot = 346.50 vs nivel 325.00 (2026-10-23)
- refs: farelo_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] complexo_soja fechou em 2.27 — abaixo do suporte 2.50
- id: `alerta-quebra_suporte-complexo_soja-2026-10-23`
- fato: complexo_soja = 2.27 vs nivel 2.50 (2026-10-23)
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

## 🟡 [release] NOPA novo (2026-10-24)
- id: `release-nopa-2026-10-24`
- fato: fonte nopa com data 2026-10-24 — coletado, ainda nao interpretado
- refs: complexo_soja
- leitura: O numero muda o balanco/tese? Algo relevante pro farelo?

---
Trate só 🔴/🟡. Saída = `insights/*.md` (formato de generate_insights.txt, com `vies:`). Cite o `id` da fila no corpo do insight. Máx 1-3. Não duplicar insight recente.
