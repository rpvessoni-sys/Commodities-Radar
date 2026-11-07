# Briefing consolidado — 2026-11-07

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

- 2026-11-06 | eur_brl_ptax | valor: 6.1317 BRL/EUR (sgs=21619)
- 2026-11-06 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-11-06 | usd_brl_ptax | valor: 5.5013 BRL/USD (sgs=1)
- 2026-11-05 | eur_brl_ptax | valor: 6.1323 BRL/EUR (sgs=21619)
- 2026-11-05 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-11-05 | usd_brl_ptax | valor: 5.4621 BRL/USD (sgs=1)
- 2026-11-04 | eur_brl_ptax | valor: 6.1549 BRL/EUR (sgs=21619)
- 2026-11-04 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-11-04 | usd_brl_ptax | valor: 5.4778 BRL/USD (sgs=1)
- 2026-11-03 | eur_brl_ptax | valor: 6.15 BRL/EUR (sgs=21619)
- 2026-11-03 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-11-03 | usd_brl_ptax | valor: 5.4935 BRL/USD (sgs=1)
- 2026-10-30 | eur_brl_ptax | valor: 6.0522 BRL/EUR (sgs=21619)
- 2026-10-30 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-10-30 | usd_brl_ptax | valor: 5.4212 BRL/USD (sgs=1)
- 2026-10-29 | eur_brl_ptax | valor: 6.0 BRL/EUR (sgs=21619)
- 2026-10-29 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-10-29 | usd_brl_ptax | valor: 5.3744 BRL/USD (sgs=1)
- 2026-10-28 | eur_brl_ptax | valor: 5.9515 BRL/EUR (sgs=21619)
- 2026-10-28 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-10-28 | usd_brl_ptax | valor: 5.342 BRL/USD (sgs=1)
- 2026-10-27 | eur_brl_ptax | valor: 5.9449 BRL/EUR (sgs=21619)
- 2026-10-27 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-10-27 | usd_brl_ptax | valor: 5.3346 BRL/USD (sgs=1)
- 2026-10-26 | eur_brl_ptax | valor: 6.1487 BRL/EUR (sgs=21619)
- 2026-10-26 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-10-26 | usd_brl_ptax | valor: 5.5007 BRL/USD (sgs=1)

---

## cftc_cot

- 2026-11-03 | farelo_cbot | managed_money_long: 132789.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-11-03 | farelo_cbot | managed_money_net: 108367.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE — long - short)
- 2026-11-03 | farelo_cbot | managed_money_short: 24422.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-11-03 | farelo_cbot | open_interest: 577046.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-11-03 | farelo_cbot | producer_long: 81747.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-11-03 | farelo_cbot | producer_short: 346827.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-11-03 | farelo_cbot | swap_long: 123313.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-11-03 | farelo_cbot | swap_short: 10086.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-11-03 | oleo_cbot | managed_money_long: 91647.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-11-03 | oleo_cbot | managed_money_net: 47413.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE — long - short)
- 2026-11-03 | oleo_cbot | managed_money_short: 44234.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-11-03 | oleo_cbot | open_interest: 602052.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-11-03 | oleo_cbot | producer_long: 151320.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-11-03 | oleo_cbot | producer_short: 301185.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-11-03 | oleo_cbot | swap_long: 96011.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-11-03 | oleo_cbot | swap_short: 4691.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-11-03 | soja_cbot | managed_money_long: 187713.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-11-03 | soja_cbot | managed_money_net: 142727.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE — long - short)
- 2026-11-03 | soja_cbot | managed_money_short: 44986.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-11-03 | soja_cbot | open_interest: 959576.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-11-03 | soja_cbot | producer_long: 303815.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-11-03 | soja_cbot | producer_short: 525261.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-11-03 | soja_cbot | swap_long: 125959.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-11-03 | soja_cbot | swap_short: 47991.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-10-27 | farelo_cbot | managed_money_long: 184371.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-10-27 | farelo_cbot | managed_money_net: 168714.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE — long - short)
- 2026-10-27 | farelo_cbot | managed_money_short: 15657.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-10-27 | farelo_cbot | open_interest: 609960.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-10-27 | farelo_cbot | producer_long: 69776.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-10-27 | farelo_cbot | producer_short: 387753.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-10-27 | farelo_cbot | swap_long: 133898.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-10-27 | farelo_cbot | swap_short: 13251.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-10-27 | oleo_cbot | managed_money_long: 97309.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-10-27 | oleo_cbot | managed_money_net: 60331.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE — long - short)
- 2026-10-27 | oleo_cbot | managed_money_short: 36978.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-10-27 | oleo_cbot | open_interest: 573736.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-10-27 | oleo_cbot | producer_long: 137797.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-10-27 | oleo_cbot | producer_short: 304862.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-10-27 | oleo_cbot | swap_long: 98096.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-10-27 | oleo_cbot | swap_short: 5266.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-10-27 | soja_cbot | managed_money_long: 226215.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-10-27 | soja_cbot | managed_money_net: 193781.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE — long - short)
- 2026-10-27 | soja_cbot | managed_money_short: 32434.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-10-27 | soja_cbot | open_interest: 979414.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-10-27 | soja_cbot | producer_long: 307664.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-10-27 | soja_cbot | producer_short: 563057.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-10-27 | soja_cbot | swap_long: 128563.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-10-27 | soja_cbot | swap_short: 54223.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)

---

## cme_cbot

- 2026-11-06 | farelo_cbot | abertura: 317.5 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-06 | farelo_cbot | fechamento: 318.79998779296875 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-06 | farelo_cbot | fechamento_F27: 319.6000061035156 USD/short_ton (ticker=ZMF27.CBT venc=jan/27)
- 2026-11-06 | farelo_cbot | fechamento_H27: 321.29998779296875 USD/short_ton (ticker=ZMH27.CBT venc=mar/27)
- 2026-11-06 | farelo_cbot | fechamento_K27: 324.6000061035156 USD/short_ton (ticker=ZMK27.CBT venc=mai/27)
- 2026-11-06 | farelo_cbot | fechamento_N27: 328.70001220703125 USD/short_ton (ticker=ZMN27.CBT venc=jul/27)
- 2026-11-06 | farelo_cbot | fechamento_Q27: 329.1000061035156 USD/short_ton (ticker=ZMQ27.CBT venc=ago/27)
- 2026-11-06 | farelo_cbot | fechamento_Z26: 318.79998779296875 USD/short_ton (ticker=ZMZ26.CBT venc=dez/26)
- 2026-11-06 | farelo_cbot | maxima: 320.70001220703125 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-06 | farelo_cbot | minima: 316.5 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-06 | farelo_cbot | volume: 73633.0 contratos (ticker=ZMZ26.CBT)
- 2026-11-06 | heating_oil_cbot | abertura: 4.368000030517578 USD/galão (ticker=HO=F)
- 2026-11-06 | heating_oil_cbot | fechamento: 4.3429999351501465 USD/galão (ticker=HO=F)
- 2026-11-06 | heating_oil_cbot | maxima: 4.407800197601318 USD/galão (ticker=HO=F)
- 2026-11-06 | heating_oil_cbot | minima: 4.2667999267578125 USD/galão (ticker=HO=F)
- 2026-11-06 | heating_oil_cbot | volume: 39289.0 contratos (ticker=HO=F)
- 2026-11-06 | oleo_cbot | abertura: 62.54999923706055 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-11-06 | oleo_cbot | fechamento: 62.310001373291016 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-11-06 | oleo_cbot | fechamento_F27: 62.470001220703125 USD_cts/lb (ticker=ZLF27.CBT venc=jan/27)
- 2026-11-06 | oleo_cbot | fechamento_H27: 62.959999084472656 USD_cts/lb (ticker=ZLH27.CBT venc=mar/27)
- 2026-11-06 | oleo_cbot | fechamento_K27: 63.4900016784668 USD_cts/lb (ticker=ZLK27.CBT venc=mai/27)
- 2026-11-06 | oleo_cbot | fechamento_N27: 63.709999084472656 USD_cts/lb (ticker=ZLN27.CBT venc=jul/27)
- 2026-11-06 | oleo_cbot | fechamento_Q27: 63.56999969482422 USD_cts/lb (ticker=ZLQ27.CBT venc=ago/27)
- 2026-11-06 | oleo_cbot | fechamento_Z26: 62.310001373291016 USD_cts/lb (ticker=ZLZ26.CBT venc=dez/26)
- 2026-11-06 | oleo_cbot | maxima: 62.560001373291016 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-11-06 | oleo_cbot | minima: 61.34000015258789 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-11-06 | oleo_cbot | volume: 85248.0 contratos (ticker=ZLZ26.CBT)
- 2026-11-06 | soja_cbot | abertura: 1189.0 USD/bushel (ticker=ZSF27.CBT)
- 2026-11-06 | soja_cbot | fechamento: 1194.5 USD/bushel (ticker=ZSF27.CBT)
- 2026-11-06 | soja_cbot | fechamento_F27: 1194.5 USD/bushel (ticker=ZSF27.CBT venc=jan/27)
- 2026-11-06 | soja_cbot | fechamento_H27: 1200.0 USD/bushel (ticker=ZSH27.CBT venc=mar/27)
- 2026-11-06 | soja_cbot | fechamento_K27: 1209.0 USD/bushel (ticker=ZSK27.CBT venc=mai/27)
- 2026-11-06 | soja_cbot | fechamento_N27: 1216.25 USD/bushel (ticker=ZSN27.CBT venc=jul/27)
- 2026-11-06 | soja_cbot | fechamento_Q27: 1205.5 USD/bushel (ticker=ZSQ27.CBT venc=ago/27)
- 2026-11-06 | soja_cbot | fechamento_X26: 1190.25 USD/bushel (ticker=ZSX26.CBT venc=nov/26)
- 2026-11-06 | soja_cbot | maxima: 1195.5 USD/bushel (ticker=ZSF27.CBT)
- 2026-11-06 | soja_cbot | minima: 1184.0 USD/bushel (ticker=ZSF27.CBT)
- 2026-11-06 | soja_cbot | volume: 121591.0 contratos (ticker=ZSF27.CBT)
- 2026-11-05 | farelo_cbot | abertura: 318.6000061035156 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-05 | farelo_cbot | fechamento: 317.20001220703125 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-05 | farelo_cbot | fechamento_F27: 317.70001220703125 USD/short_ton (ticker=ZMF27.CBT venc=jan/27)
- 2026-11-05 | farelo_cbot | fechamento_H27: 319.5 USD/short_ton (ticker=ZMH27.CBT venc=mar/27)
- 2026-11-05 | farelo_cbot | fechamento_K27: 323.0 USD/short_ton (ticker=ZMK27.CBT venc=mai/27)
- 2026-11-05 | farelo_cbot | fechamento_N27: 327.6000061035156 USD/short_ton (ticker=ZMN27.CBT venc=jul/27)
- 2026-11-05 | farelo_cbot | fechamento_Q27: 328.0 USD/short_ton (ticker=ZMQ27.CBT venc=ago/27)
- 2026-11-05 | farelo_cbot | fechamento_Z26: 317.20001220703125 USD/short_ton (ticker=ZMZ26.CBT venc=dez/26)
- 2026-11-05 | farelo_cbot | maxima: 321.8999938964844 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-05 | farelo_cbot | minima: 316.79998779296875 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-05 | farelo_cbot | volume: 95164.0 contratos (ticker=ZMZ26.CBT)
- 2026-11-05 | heating_oil_cbot | abertura: 4.20550012588501 USD/galão (ticker=HO=F)

---

## indicators

- 2026-11-07 | complexo_soja | indice_sobra_farelo: 25.0 0-100 (sem sobra relevante (1/4 condições))
- 2026-11-07 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-11-06 | biodiesel_us | custo_oleo_usd_galao: 4.6733 USD/galão (7.5 lb × óleo 62.31 cts/lb)
- 2026-11-06 | biodiesel_us | margem_usd_galao: 2.0347 USD/galão (receita 7.51 (HO 4.34 + 1.5×RIN 2.11) − custo 5.47 (óleo 4.67 + ind 0.80))
- 2026-11-06 | biodiesel_us | receita_usd_galao: 7.508 USD/galão (HO 4.34 + 1.5×RIN 2.11)
- 2026-11-06 | complexo_soja | crush_margin_usd_bu: 1.9227 USD/bushel (Board Crush: farelo 318.80 + oleo 62.31 − soja 1194.50)
- 2026-11-06 | complexo_soja | far_soj_ratio_pct: 80.07 % (farelo 318.80/sht ÷ (soja 1194.50cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-11-06 | complexo_soja | indice_sobra_farelo: 25.0 0-100 (sem sobra relevante (1/4 condições))
- 2026-11-06 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-11-06 | complexo_soja | oil_meal_spread_usd_bu: -0.1595 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-11-06 | complexo_soja | oil_share_pct: 49.42 % (valor oleo 6.85 / total 13.87)
- 2026-11-06 | soja_paridade_br | brl_saca_paridade: 144.87 BRL/saca60kg (CBOT 1194.50 cts × USD/BRL 5.5013 (sem basis))
- 2026-11-05 | biodiesel_us | custo_oleo_usd_galao: 4.668 USD/galão (7.5 lb × óleo 62.24 cts/lb)
- 2026-11-05 | biodiesel_us | margem_usd_galao: 2.0489 USD/galão (receita 7.52 (HO 4.35 + 1.5×RIN 2.11) − custo 5.47 (óleo 4.67 + ind 0.80))
- 2026-11-05 | biodiesel_us | receita_usd_galao: 7.5169 USD/galão (HO 4.35 + 1.5×RIN 2.11)
- 2026-11-05 | complexo_soja | crush_margin_usd_bu: 1.9423 USD/bushel (Board Crush: farelo 317.20 + oleo 62.24 − soja 1188.25)
- 2026-11-05 | complexo_soja | far_soj_ratio_pct: 80.08 % (farelo 317.20/sht ÷ (soja 1188.25cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-11-05 | complexo_soja | indice_sobra_farelo: 25.0 0-100 (sem sobra relevante (1/4 condições))
- 2026-11-05 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-11-05 | complexo_soja | oil_meal_spread_usd_bu: -0.132 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-11-05 | complexo_soja | oil_share_pct: 49.52 % (valor oleo 6.85 / total 13.82)
- 2026-11-05 | soja_paridade_br | brl_saca_paridade: 143.09 BRL/saca60kg (CBOT 1188.25 cts × USD/BRL 5.4621 (sem basis))
- 2026-11-04 | biodiesel_us | custo_oleo_usd_galao: 4.7647 USD/galão (7.5 lb × óleo 63.53 cts/lb)
- 2026-11-04 | biodiesel_us | margem_usd_galao: 1.8058 USD/galão (receita 7.37 (HO 4.21 + 1.5×RIN 2.11) − custo 5.56 (óleo 4.76 + ind 0.80))
- 2026-11-04 | biodiesel_us | receita_usd_galao: 7.3705 USD/galão (HO 4.21 + 1.5×RIN 2.11)
- 2026-11-04 | complexo_soja | crush_margin_usd_bu: 1.975 USD/bushel (Board Crush: farelo 318.60 + oleo 63.53 − soja 1202.25)
- 2026-11-04 | complexo_soja | far_soj_ratio_pct: 79.5 % (farelo 318.60/sht ÷ (soja 1202.25cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-11-04 | complexo_soja | indice_sobra_farelo: 25.0 0-100 (sem sobra relevante (1/4 condições))
- 2026-11-04 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-11-04 | complexo_soja | oil_meal_spread_usd_bu: -0.0209 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-11-04 | complexo_soja | oil_share_pct: 49.93 % (valor oleo 6.99 / total 14.00)
- 2026-11-04 | soja_paridade_br | brl_saca_paridade: 145.19 BRL/saca60kg (CBOT 1202.25 cts × USD/BRL 5.4778 (sem basis))
- 2026-11-03 | biodiesel_us | custo_oleo_usd_galao: 4.896 USD/galão (7.5 lb × óleo 65.28 cts/lb)
- 2026-11-03 | biodiesel_us | margem_usd_galao: 1.9996 USD/galão (receita 7.70 (HO 4.53 + 1.5×RIN 2.11) − custo 5.70 (óleo 4.90 + ind 0.80))
- 2026-11-03 | biodiesel_us | receita_usd_galao: 7.6956 USD/galão (HO 4.53 + 1.5×RIN 2.11)
- 2026-11-03 | complexo_soja | crush_margin_usd_bu: 2.0368 USD/bushel (Board Crush: farelo 318.00 + oleo 65.28 − soja 1214.00)
- 2026-11-03 | complexo_soja | far_soj_ratio_pct: 78.58 % (farelo 318.00/sht ÷ (soja 1214.00cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-11-03 | complexo_soja | indice_sobra_farelo: 75.0 0-100 (sobra relevante (3/4 condições))
- 2026-11-03 | complexo_soja | indice_suporte_oleo: 80.0 0-100 (óleo domina o crush (4/5 condições))
- 2026-11-03 | complexo_soja | oil_meal_spread_usd_bu: 0.1848 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-11-03 | complexo_soja | oil_share_pct: 50.65 % (valor oleo 7.18 / total 14.18)
- 2026-11-03 | soja_paridade_br | brl_saca_paridade: 147.03 BRL/saca60kg (CBOT 1214.00 cts × USD/BRL 5.4935 (sem basis))
- 2026-11-02 | biodiesel_us | custo_oleo_usd_galao: 4.881 USD/galão (7.5 lb × óleo 65.08 cts/lb)
- 2026-11-02 | biodiesel_us | margem_usd_galao: 1.9056 USD/galão (receita 7.59 (HO 4.42 + 1.5×RIN 2.11) − custo 5.68 (óleo 4.88 + ind 0.80))
- 2026-11-02 | biodiesel_us | receita_usd_galao: 7.5866 USD/galão (HO 4.42 + 1.5×RIN 2.11)
- 2026-11-02 | complexo_soja | crush_margin_usd_bu: 2.0225 USD/bushel (Board Crush: farelo 319.60 + oleo 65.08 − soja 1216.75)
- 2026-11-02 | complexo_soja | far_soj_ratio_pct: 78.8 % (farelo 319.60/sht ÷ (soja 1216.75cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-11-02 | complexo_soja | indice_sobra_farelo: 75.0 0-100 (sobra relevante (3/4 condições))
- 2026-11-02 | complexo_soja | indice_suporte_oleo: 80.0 0-100 (óleo domina o crush (4/5 condições))
- 2026-11-02 | complexo_soja | oil_meal_spread_usd_bu: 0.1276 USD/bushel (Oleo - Farelo (positivo = oleo manda))

---

## inmet

- 2026-11-07 | cascavel_pr | temp_max_manha: 29.0 C (Cascavel/PR — Nublado com pancadas de chuva e trovoadas)
- 2026-11-07 | cascavel_pr | temp_max_noite: 29.0 C (Cascavel/PR — Muitas nuvens com pancadas de chuva e trovoadas)
- 2026-11-07 | cascavel_pr | temp_max_tarde: 29.0 C (Cascavel/PR — Nublado com pancadas de chuva e trovoadas)
- 2026-11-07 | cascavel_pr | temp_min_manha: 14.0 C (Cascavel/PR — Nublado com pancadas de chuva e trovoadas)
- 2026-11-07 | cascavel_pr | temp_min_noite: 14.0 C (Cascavel/PR — Muitas nuvens com pancadas de chuva e trovoadas)
- 2026-11-07 | cascavel_pr | temp_min_tarde: 14.0 C (Cascavel/PR — Nublado com pancadas de chuva e trovoadas)
- 2026-11-07 | cuiaba_mt | temp_max_manha: 38.0 C (Cuiaba/MT — Muitas nuvens)
- 2026-11-07 | cuiaba_mt | temp_max_noite: 38.0 C (Cuiaba/MT — Muitas nuvens com pancadas de chuva e trovoadas)
- 2026-11-07 | cuiaba_mt | temp_max_tarde: 38.0 C (Cuiaba/MT — Muitas nuvens com chuva isolada)
- 2026-11-07 | cuiaba_mt | temp_min_manha: 27.0 C (Cuiaba/MT — Muitas nuvens)
- 2026-11-07 | cuiaba_mt | temp_min_noite: 27.0 C (Cuiaba/MT — Muitas nuvens com pancadas de chuva e trovoadas)
- 2026-11-07 | cuiaba_mt | temp_min_tarde: 27.0 C (Cuiaba/MT — Muitas nuvens com chuva isolada)
- 2026-11-07 | lucas_rio_verde_mt | temp_max_manha: 37.0 C (Lucas do Rio Verde/MT — Muitas nuvens)
- 2026-11-07 | lucas_rio_verde_mt | temp_max_noite: 37.0 C (Lucas do Rio Verde/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-07 | lucas_rio_verde_mt | temp_max_tarde: 37.0 C (Lucas do Rio Verde/MT — Muitas nuvens com chuva isolada)
- 2026-11-07 | lucas_rio_verde_mt | temp_min_manha: 24.0 C (Lucas do Rio Verde/MT — Muitas nuvens)
- 2026-11-07 | lucas_rio_verde_mt | temp_min_noite: 24.0 C (Lucas do Rio Verde/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-07 | lucas_rio_verde_mt | temp_min_tarde: 24.0 C (Lucas do Rio Verde/MT — Muitas nuvens com chuva isolada)
- 2026-11-07 | maringa_pr | temp_max_manha: 31.0 C (Maringa/PR — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-07 | maringa_pr | temp_max_noite: 31.0 C (Maringa/PR — Nublado com pancadas de chuva e trovoadas)
- 2026-11-07 | maringa_pr | temp_max_tarde: 31.0 C (Maringa/PR — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-07 | maringa_pr | temp_min_manha: 21.0 C (Maringa/PR — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-07 | maringa_pr | temp_min_noite: 21.0 C (Maringa/PR — Nublado com pancadas de chuva e trovoadas)
- 2026-11-07 | maringa_pr | temp_min_tarde: 21.0 C (Maringa/PR — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-07 | passo_fundo_rs | temp_max_manha: 23.0 C (Passo Fundo/RS — Nublado com pancadas de chuva e trovoadas)
- 2026-11-07 | passo_fundo_rs | temp_max_noite: 23.0 C (Passo Fundo/RS — Muitas nuvens com pancadas de chuva isoladas)
- 2026-11-07 | passo_fundo_rs | temp_max_tarde: 23.0 C (Passo Fundo/RS — Nublado com pancadas de chuva e trovoadas)
- 2026-11-07 | passo_fundo_rs | temp_min_manha: 13.0 C (Passo Fundo/RS — Nublado com pancadas de chuva e trovoadas)
- 2026-11-07 | passo_fundo_rs | temp_min_noite: 13.0 C (Passo Fundo/RS — Muitas nuvens com pancadas de chuva isoladas)
- 2026-11-07 | passo_fundo_rs | temp_min_tarde: 13.0 C (Passo Fundo/RS — Nublado com pancadas de chuva e trovoadas)
- 2026-11-07 | rio_verde_go | temp_max_manha: 34.0 C (Rio Verde/GO — Muitas nuvens)
- 2026-11-07 | rio_verde_go | temp_max_noite: 34.0 C (Rio Verde/GO — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-07 | rio_verde_go | temp_max_tarde: 34.0 C (Rio Verde/GO — Muitas nuvens com chuva isolada)
- 2026-11-07 | rio_verde_go | temp_min_manha: 21.0 C (Rio Verde/GO — Muitas nuvens)
- 2026-11-07 | rio_verde_go | temp_min_noite: 21.0 C (Rio Verde/GO — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-07 | rio_verde_go | temp_min_tarde: 21.0 C (Rio Verde/GO — Muitas nuvens com chuva isolada)
- 2026-11-07 | sinop_mt | temp_max_manha: 38.0 C (Sinop/MT — Muitas nuvens)
- 2026-11-07 | sinop_mt | temp_max_noite: 38.0 C (Sinop/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-07 | sinop_mt | temp_max_tarde: 38.0 C (Sinop/MT — Muitas nuvens com chuva isolada)
- 2026-11-07 | sinop_mt | temp_min_manha: 24.0 C (Sinop/MT — Muitas nuvens)
- 2026-11-07 | sinop_mt | temp_min_noite: 24.0 C (Sinop/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-07 | sinop_mt | temp_min_tarde: 24.0 C (Sinop/MT — Muitas nuvens com chuva isolada)
- 2026-11-07 | sorriso_mt | temp_max_manha: 38.0 C (Sorriso/MT — Muitas nuvens)
- 2026-11-07 | sorriso_mt | temp_max_noite: 38.0 C (Sorriso/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-07 | sorriso_mt | temp_max_tarde: 38.0 C (Sorriso/MT — Muitas nuvens com chuva isolada)
- 2026-11-07 | sorriso_mt | temp_min_manha: 24.0 C (Sorriso/MT — Muitas nuvens)
- 2026-11-07 | sorriso_mt | temp_min_noite: 24.0 C (Sorriso/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-07 | sorriso_mt | temp_min_tarde: 24.0 C (Sorriso/MT — Muitas nuvens com chuva isolada)
- 2026-11-06 | cascavel_pr | temp_max_manha: 28.0 C (Cascavel/PR — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-06 | cascavel_pr | temp_max_noite: 28.0 C (Cascavel/PR — Nublado com pancadas de chuva e trovoadas)

---

## mpob

- 2026-11-07 | palma_malasia | page_fetched: 3201.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-06 | palma_malasia | page_fetched: 3201.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-05 | palma_malasia | page_fetched: 3201.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-04 | palma_malasia | page_fetched: 3201.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-03 | palma_malasia | page_fetched: 3201.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-02 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-01 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-31 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-30 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-29 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-28 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-27 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-26 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-25 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-24 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)

---

## noaa_cpc

- 2026-11-07 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-06 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-05 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-04 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-03 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-02 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-01 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-31 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-30 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-29 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-28 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-27 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-26 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-25 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-24 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)

---

## nopa

- 2026-11-07 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-06 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-05 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-04 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-03 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-02 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-01 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-31 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-30 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-29 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-28 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-27 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-26 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-25 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-24 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)

---

## noticias_rss

- 2026-11-07 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-06 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-05 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-04 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-03 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-02 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-01 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-10-31 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-10-30 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-10-29 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-10-28 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-10-27 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-10-26 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-10-25 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-10-24 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))

---

## usda_crop_progress

- 2026-11-01 | soybeans_eua | pct_harvested: 88.0 % (SOYBEANS - PROGRESS, MEASURED IN PCT HARVESTED)
- 2026-10-25 | soybeans_eua | pct_harvested: 79.0 % (SOYBEANS - PROGRESS, MEASURED IN PCT HARVESTED)

---

# FORECASTS ATIVOS (bandas estatisticas)

Bandas calculadas via MA20+volatilidade+slope curto. Claude Code DEVE refinar com drivers fundamentais.

| Geracao | Horizonte | Alvo | Commodity | Spot ref | Baixo | Central | Alto | Vies |
|---|---|---|---|---|---|---|---|---|
| 2026-11-07 | 7d | 2026-11-14 | farelo_cbot | 318.80 | 288.80 | 302.17 | 315.55 | baixista |
| 2026-11-07 | 7d | 2026-11-14 | oleo_cbot | 62.31 | 58.72 | 61.20 | 63.67 | baixista |
| 2026-11-07 | 7d | 2026-11-14 | soja_cbot | 1194.50 | 1137.77 | 1164.60 | 1191.44 | baixista |
| 2026-11-07 | 30d | 2026-12-07 | farelo_cbot | 318.80 | 214.37 | 242.05 | 269.74 | baixista |
| 2026-11-07 | 30d | 2026-12-07 | oleo_cbot | 62.31 | 51.49 | 56.61 | 61.72 | baixista |
| 2026-11-07 | 30d | 2026-12-07 | soja_cbot | 1194.50 | 997.03 | 1052.60 | 1108.16 | baixista |
| 2026-11-06 | 7d | 2026-11-13 | farelo_cbot | 318.80 | 288.87 | 302.27 | 315.66 | baixista |
| 2026-11-06 | 7d | 2026-11-13 | oleo_cbot | 62.31 | 58.53 | 60.97 | 63.42 | baixista |
| 2026-11-06 | 7d | 2026-11-13 | soja_cbot | 1194.50 | 1135.91 | 1161.80 | 1187.69 | baixista |
| 2026-11-06 | 30d | 2026-12-06 | farelo_cbot | 318.80 | 214.42 | 242.15 | 269.88 | baixista |
| 2026-11-06 | 30d | 2026-12-06 | oleo_cbot | 62.31 | 51.32 | 56.38 | 61.44 | baixista |
| 2026-11-06 | 30d | 2026-12-06 | soja_cbot | 1194.50 | 996.13 | 1049.73 | 1103.34 | baixista |
| 2026-11-05 | 7d | 2026-11-12 | farelo_cbot | 317.20 | 289.88 | 303.54 | 317.20 | baixista |
| 2026-11-05 | 7d | 2026-11-12 | oleo_cbot | 62.24 | 59.88 | 62.25 | 64.62 | baixista |
| 2026-11-05 | 7d | 2026-11-12 | soja_cbot | 1188.25 | 1149.47 | 1174.40 | 1199.33 | baixista |
| 2026-11-05 | 30d | 2026-12-05 | farelo_cbot | 317.20 | 216.28 | 244.56 | 272.83 | baixista |
| 2026-11-05 | 30d | 2026-12-05 | oleo_cbot | 62.24 | 53.58 | 58.48 | 63.39 | baixista |
| 2026-11-05 | 30d | 2026-12-05 | soja_cbot | 1188.25 | 1015.54 | 1067.15 | 1118.77 | baixista |
| 2026-11-04 | 7d | 2026-11-11 | farelo_cbot | 318.60 | 288.62 | 302.03 | 315.44 | baixista |
| 2026-11-04 | 7d | 2026-11-11 | oleo_cbot | 63.53 | 62.02 | 64.04 | 66.07 | baixista |
| 2026-11-04 | 7d | 2026-11-11 | soja_cbot | 1202.25 | 1155.76 | 1180.10 | 1204.43 | baixista |
| 2026-11-04 | 30d | 2026-12-04 | farelo_cbot | 318.60 | 219.91 | 247.67 | 275.44 | baixista |
| 2026-11-04 | 30d | 2026-12-04 | oleo_cbot | 63.53 | 56.70 | 60.89 | 65.08 | baixista |
| 2026-11-04 | 30d | 2026-12-04 | soja_cbot | 1202.25 | 1027.74 | 1078.12 | 1128.49 | baixista |

---


---

# Fila de julgamento — 2026-11-07

**7 item(ns).** Frase-gatilho: "lê a fila de julgamento e trata"

## 🔴 [nivel_tese] soja_cbot fechou em 1194.50 — acima da resistencia 1180.00
- id: `alerta-quebra_resistencia-soja_cbot-2026-11-06`
- fato: soja_cbot = 1194.50 vs nivel 1180.00 (2026-11-06)
- refs: soja_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] oleo_cbot fechou em 62.31 — abaixo do suporte 72.00
- id: `alerta-quebra_suporte-oleo_cbot-2026-11-06`
- fato: oleo_cbot = 62.31 vs nivel 72.00 (2026-11-06)
- refs: oleo_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] usd_brl_ptax fechou em 5.50 — acima da resistencia 5.30
- id: `alerta-quebra_resistencia-usd_brl_ptax-2026-11-06`
- fato: usd_brl_ptax = 5.50 vs nivel 5.30 (2026-11-06)
- refs: usd_brl_ptax
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] complexo_soja fechou em 1.92 — abaixo do suporte 2.50
- id: `alerta-quebra_suporte-complexo_soja-2026-11-06`
- fato: complexo_soja = 1.92 vs nivel 2.50 (2026-11-06)
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

## 🟡 [release] NOPA novo (2026-11-07)
- id: `release-nopa-2026-11-07`
- fato: fonte nopa com data 2026-11-07 — coletado, ainda nao interpretado
- refs: complexo_soja
- leitura: O numero muda o balanco/tese? Algo relevante pro farelo?

---
Trate só 🔴/🟡. Saída = `insights/*.md` (formato de generate_insights.txt, com `vies:`). Cite o `id` da fila no corpo do insight. Máx 1-3. Não duplicar insight recente.
