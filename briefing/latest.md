# Briefing consolidado — 2026-11-14

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
- 2026-11-03 | eur_brl_ptax | valor: 6.15 BRL/EUR (sgs=21619)
- 2026-11-03 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-11-03 | usd_brl_ptax | valor: 5.4935 BRL/USD (sgs=1)

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

---

## cme_cbot

- 2026-11-13 | farelo_cbot | abertura: 325.3999938964844 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-13 | farelo_cbot | fechamento: 330.20001220703125 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-13 | farelo_cbot | fechamento_F27: 327.8999938964844 USD/short_ton (ticker=ZMF27.CBT venc=jan/27)
- 2026-11-13 | farelo_cbot | fechamento_H27: 328.79998779296875 USD/short_ton (ticker=ZMH27.CBT venc=mar/27)
- 2026-11-13 | farelo_cbot | fechamento_K27: 330.79998779296875 USD/short_ton (ticker=ZMK27.CBT venc=mai/27)
- 2026-11-13 | farelo_cbot | fechamento_N27: 334.5 USD/short_ton (ticker=ZMN27.CBT venc=jul/27)
- 2026-11-13 | farelo_cbot | fechamento_Q27: 333.1000061035156 USD/short_ton (ticker=ZMQ27.CBT venc=ago/27)
- 2026-11-13 | farelo_cbot | fechamento_Z26: 330.20001220703125 USD/short_ton (ticker=ZMZ26.CBT venc=dez/26)
- 2026-11-13 | farelo_cbot | maxima: 331.5 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-13 | farelo_cbot | minima: 324.70001220703125 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-13 | farelo_cbot | volume: 55461.0 contratos (ticker=ZMZ26.CBT)
- 2026-11-13 | heating_oil_cbot | abertura: 4.288000106811523 USD/galão (ticker=HO=F)
- 2026-11-13 | heating_oil_cbot | fechamento: 4.306700229644775 USD/galão (ticker=HO=F)
- 2026-11-13 | heating_oil_cbot | maxima: 4.345799922943115 USD/galão (ticker=HO=F)
- 2026-11-13 | heating_oil_cbot | minima: 4.242400169372559 USD/galão (ticker=HO=F)
- 2026-11-13 | heating_oil_cbot | volume: 38482.0 contratos (ticker=HO=F)
- 2026-11-13 | oleo_cbot | abertura: 63.41999816894531 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-11-13 | oleo_cbot | fechamento: 63.72999954223633 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-11-13 | oleo_cbot | fechamento_F27: 64.0199966430664 USD_cts/lb (ticker=ZLF27.CBT venc=jan/27)
- 2026-11-13 | oleo_cbot | fechamento_H27: 64.5199966430664 USD_cts/lb (ticker=ZLH27.CBT venc=mar/27)
- 2026-11-13 | oleo_cbot | fechamento_K27: 64.95999908447266 USD_cts/lb (ticker=ZLK27.CBT venc=mai/27)
- 2026-11-13 | oleo_cbot | fechamento_N27: 65.16000366210938 USD_cts/lb (ticker=ZLN27.CBT venc=jul/27)
- 2026-11-13 | oleo_cbot | fechamento_Q27: 64.95999908447266 USD_cts/lb (ticker=ZLQ27.CBT venc=ago/27)
- 2026-11-13 | oleo_cbot | fechamento_Z26: 63.72999954223633 USD_cts/lb (ticker=ZLZ26.CBT venc=dez/26)
- 2026-11-13 | oleo_cbot | maxima: 64.19999694824219 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-11-13 | oleo_cbot | minima: 63.33000183105469 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-11-13 | oleo_cbot | volume: 65775.0 contratos (ticker=ZLZ26.CBT)
- 2026-11-13 | soja_cbot | abertura: 1219.0 USD/bushel (ticker=ZSF27.CBT)
- 2026-11-13 | soja_cbot | fechamento: 1232.75 USD/bushel (ticker=ZSF27.CBT)
- 2026-11-13 | soja_cbot | fechamento_F27: 1232.75 USD/bushel (ticker=ZSF27.CBT venc=jan/27)
- 2026-11-13 | soja_cbot | fechamento_H27: 1238.5 USD/bushel (ticker=ZSH27.CBT venc=mar/27)
- 2026-11-13 | soja_cbot | fechamento_K27: 1245.5 USD/bushel (ticker=ZSK27.CBT venc=mai/27)
- 2026-11-13 | soja_cbot | fechamento_N27: 1250.25 USD/bushel (ticker=ZSN27.CBT venc=jul/27)
- 2026-11-13 | soja_cbot | fechamento_Q27: 1233.0 USD/bushel (ticker=ZSQ27.CBT venc=ago/27)
- 2026-11-13 | soja_cbot | fechamento_X26: 1243.0 USD/bushel (ticker=ZSX26.CBT venc=nov/26)
- 2026-11-13 | soja_cbot | maxima: 1240.75 USD/bushel (ticker=ZSF27.CBT)
- 2026-11-13 | soja_cbot | minima: 1218.75 USD/bushel (ticker=ZSF27.CBT)
- 2026-11-13 | soja_cbot | volume: 103557.0 contratos (ticker=ZSF27.CBT)
- 2026-11-12 | farelo_cbot | abertura: 329.3999938964844 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-12 | farelo_cbot | fechamento: 325.3999938964844 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-12 | farelo_cbot | fechamento_F27: 323.6000061035156 USD/short_ton (ticker=ZMF27.CBT venc=jan/27)
- 2026-11-12 | farelo_cbot | fechamento_H27: 324.79998779296875 USD/short_ton (ticker=ZMH27.CBT venc=mar/27)
- 2026-11-12 | farelo_cbot | fechamento_K27: 327.6000061035156 USD/short_ton (ticker=ZMK27.CBT venc=mai/27)
- 2026-11-12 | farelo_cbot | fechamento_N27: 331.3999938964844 USD/short_ton (ticker=ZMN27.CBT venc=jul/27)
- 2026-11-12 | farelo_cbot | fechamento_Q27: 330.20001220703125 USD/short_ton (ticker=ZMQ27.CBT venc=ago/27)
- 2026-11-12 | farelo_cbot | fechamento_Z26: 325.3999938964844 USD/short_ton (ticker=ZMZ26.CBT venc=dez/26)
- 2026-11-12 | farelo_cbot | maxima: 330.0 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-12 | farelo_cbot | minima: 325.1000061035156 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-12 | farelo_cbot | volume: 82193.0 contratos (ticker=ZMZ26.CBT)
- 2026-11-12 | heating_oil_cbot | abertura: 4.209000110626221 USD/galão (ticker=HO=F)

---

## indicators

- 2026-11-14 | complexo_soja | indice_sobra_farelo: 25.0 0-100 (sem sobra relevante (1/4 condições))
- 2026-11-14 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-11-13 | biodiesel_us | custo_oleo_usd_galao: 4.7797 USD/galão (7.5 lb × óleo 63.73 cts/lb)
- 2026-11-13 | biodiesel_us | margem_usd_galao: 1.892 USD/galão (receita 7.47 (HO 4.31 + 1.5×RIN 2.11) − custo 5.58 (óleo 4.78 + ind 0.80))
- 2026-11-13 | biodiesel_us | receita_usd_galao: 7.4717 USD/galão (HO 4.31 + 1.5×RIN 2.11)
- 2026-11-13 | complexo_soja | crush_margin_usd_bu: 1.9472 USD/bushel (Board Crush: farelo 330.20 + oleo 63.73 − soja 1232.75)
- 2026-11-13 | complexo_soja | far_soj_ratio_pct: 80.36 % (farelo 330.20/sht ÷ (soja 1232.75cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-11-13 | complexo_soja | indice_sobra_farelo: 25.0 0-100 (sem sobra relevante (1/4 condições))
- 2026-11-13 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-11-13 | complexo_soja | oil_meal_spread_usd_bu: -0.2541 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-11-13 | complexo_soja | oil_share_pct: 49.11 % (valor oleo 7.01 / total 14.27)
- 2026-11-13 | soja_paridade_br | brl_saca_paridade: 153.6 BRL/saca60kg (CBOT 1232.75 cts × USD/BRL 5.6518 (sem basis))
- 2026-11-12 | biodiesel_us | custo_oleo_usd_galao: 4.7565 USD/galão (7.5 lb × óleo 63.42 cts/lb)
- 2026-11-12 | biodiesel_us | margem_usd_galao: 1.895 USD/galão (receita 7.45 (HO 4.29 + 1.5×RIN 2.11) − custo 5.56 (óleo 4.76 + ind 0.80))
- 2026-11-12 | biodiesel_us | receita_usd_galao: 7.4515 USD/galão (HO 4.29 + 1.5×RIN 2.11)
- 2026-11-12 | complexo_soja | crush_margin_usd_bu: 1.945 USD/bushel (Board Crush: farelo 325.40 + oleo 63.42 − soja 1219.00)
- 2026-11-12 | complexo_soja | far_soj_ratio_pct: 80.08 % (farelo 325.40/sht ÷ (soja 1219.00cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-11-12 | complexo_soja | indice_sobra_farelo: 25.0 0-100 (sem sobra relevante (1/4 condições))
- 2026-11-12 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-11-12 | complexo_soja | oil_meal_spread_usd_bu: -0.1826 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-11-12 | complexo_soja | oil_share_pct: 49.35 % (valor oleo 6.98 / total 14.13)
- 2026-11-12 | soja_paridade_br | brl_saca_paridade: 150.88 BRL/saca60kg (CBOT 1219.00 cts × USD/BRL 5.6143 (sem basis))
- 2026-11-11 | biodiesel_us | custo_oleo_usd_galao: 4.791 USD/galão (7.5 lb × óleo 63.88 cts/lb)
- 2026-11-11 | biodiesel_us | margem_usd_galao: 1.7853 USD/galão (receita 7.38 (HO 4.21 + 1.5×RIN 2.11) − custo 5.59 (óleo 4.79 + ind 0.80))
- 2026-11-11 | biodiesel_us | receita_usd_galao: 7.3763 USD/galão (HO 4.21 + 1.5×RIN 2.11)
- 2026-11-11 | complexo_soja | crush_margin_usd_bu: 1.9727 USD/bushel (Board Crush: farelo 329.70 + oleo 63.88 − soja 1230.75)
- 2026-11-11 | complexo_soja | far_soj_ratio_pct: 80.37 % (farelo 329.70/sht ÷ (soja 1230.75cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-11-11 | complexo_soja | indice_sobra_farelo: 25.0 0-100 (sem sobra relevante (1/4 condições))
- 2026-11-11 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-11-11 | complexo_soja | oil_meal_spread_usd_bu: -0.2266 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-11-11 | complexo_soja | oil_share_pct: 49.21 % (valor oleo 7.03 / total 14.28)
- 2026-11-11 | soja_paridade_br | brl_saca_paridade: 150.88 BRL/saca60kg (CBOT 1230.75 cts × USD/BRL 5.5606 (sem basis))
- 2026-11-10 | biodiesel_us | custo_oleo_usd_galao: 4.7078 USD/galão (7.5 lb × óleo 62.77 cts/lb)
- 2026-11-10 | biodiesel_us | margem_usd_galao: 1.7881 USD/galão (receita 7.30 (HO 4.13 + 1.5×RIN 2.11) − custo 5.51 (óleo 4.71 + ind 0.80))
- 2026-11-10 | biodiesel_us | receita_usd_galao: 7.2959 USD/galão (HO 4.13 + 1.5×RIN 2.11)
- 2026-11-10 | complexo_soja | crush_margin_usd_bu: 1.8077 USD/bushel (Board Crush: farelo 326.50 + oleo 62.77 − soja 1228.00)
- 2026-11-10 | complexo_soja | far_soj_ratio_pct: 79.76 % (farelo 326.50/sht ÷ (soja 1228.00cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-11-10 | complexo_soja | indice_sobra_farelo: 25.0 0-100 (sem sobra relevante (1/4 condições))
- 2026-11-10 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-11-10 | complexo_soja | oil_meal_spread_usd_bu: -0.2783 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-11-10 | complexo_soja | oil_share_pct: 49.01 % (valor oleo 6.90 / total 14.09)
- 2026-11-10 | soja_paridade_br | brl_saca_paridade: 151.17 BRL/saca60kg (CBOT 1228.00 cts × USD/BRL 5.5840 (sem basis))
- 2026-11-09 | biodiesel_us | custo_oleo_usd_galao: 4.6522 USD/galão (7.5 lb × óleo 62.03 cts/lb)
- 2026-11-09 | biodiesel_us | margem_usd_galao: 1.9275 USD/galão (receita 7.38 (HO 4.21 + 1.5×RIN 2.11) − custo 5.45 (óleo 4.65 + ind 0.80))
- 2026-11-09 | biodiesel_us | receita_usd_galao: 7.3798 USD/galão (HO 4.21 + 1.5×RIN 2.11)
- 2026-11-09 | complexo_soja | crush_margin_usd_bu: 1.9962 USD/bushel (Board Crush: farelo 320.70 + oleo 62.03 − soja 1188.25)
- 2026-11-09 | complexo_soja | far_soj_ratio_pct: 80.97 % (farelo 320.70/sht ÷ (soja 1188.25cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-11-09 | complexo_soja | indice_sobra_farelo: 25.0 0-100 (sem sobra relevante (1/4 condições))
- 2026-11-09 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-11-09 | complexo_soja | oil_meal_spread_usd_bu: -0.2321 USD/bushel (Oleo - Farelo (positivo = oleo manda))

---

## inmet

- 2026-11-14 | cascavel_pr | temp_max_manha: 31.0 C (Cascavel/PR — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-14 | cascavel_pr | temp_max_noite: 31.0 C (Cascavel/PR — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-14 | cascavel_pr | temp_max_tarde: 31.0 C (Cascavel/PR — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-14 | cascavel_pr | temp_min_manha: 20.0 C (Cascavel/PR — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-14 | cascavel_pr | temp_min_noite: 20.0 C (Cascavel/PR — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-14 | cascavel_pr | temp_min_tarde: 20.0 C (Cascavel/PR — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-14 | cuiaba_mt | temp_max_manha: 36.0 C (Cuiaba/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-14 | cuiaba_mt | temp_max_noite: 36.0 C (Cuiaba/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-14 | cuiaba_mt | temp_max_tarde: 36.0 C (Cuiaba/MT — Muitas nuvens com chuva)
- 2026-11-14 | cuiaba_mt | temp_min_manha: 26.0 C (Cuiaba/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-14 | cuiaba_mt | temp_min_noite: 26.0 C (Cuiaba/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-14 | cuiaba_mt | temp_min_tarde: 26.0 C (Cuiaba/MT — Muitas nuvens com chuva)
- 2026-11-14 | lucas_rio_verde_mt | temp_max_manha: 34.0 C (Lucas do Rio Verde/MT — Muitas nuvens com chuva)
- 2026-11-14 | lucas_rio_verde_mt | temp_max_noite: 34.0 C (Lucas do Rio Verde/MT — Muitas nuvens com chuva)
- 2026-11-14 | lucas_rio_verde_mt | temp_max_tarde: 34.0 C (Lucas do Rio Verde/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-14 | lucas_rio_verde_mt | temp_min_manha: 24.0 C (Lucas do Rio Verde/MT — Muitas nuvens com chuva)
- 2026-11-14 | lucas_rio_verde_mt | temp_min_noite: 24.0 C (Lucas do Rio Verde/MT — Muitas nuvens com chuva)
- 2026-11-14 | lucas_rio_verde_mt | temp_min_tarde: 24.0 C (Lucas do Rio Verde/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-14 | maringa_pr | temp_max_manha: 31.0 C (Maringa/PR — Muitas nuvens)
- 2026-11-14 | maringa_pr | temp_max_noite: 31.0 C (Maringa/PR — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-14 | maringa_pr | temp_max_tarde: 31.0 C (Maringa/PR — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-14 | maringa_pr | temp_min_manha: 22.0 C (Maringa/PR — Muitas nuvens)
- 2026-11-14 | maringa_pr | temp_min_noite: 22.0 C (Maringa/PR — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-14 | maringa_pr | temp_min_tarde: 22.0 C (Maringa/PR — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-14 | passo_fundo_rs | temp_max_manha: 32.0 C (Passo Fundo/RS — Muitas nuvens)
- 2026-11-14 | passo_fundo_rs | temp_max_noite: 32.0 C (Passo Fundo/RS — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-14 | passo_fundo_rs | temp_max_tarde: 32.0 C (Passo Fundo/RS — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-14 | passo_fundo_rs | temp_min_manha: 17.0 C (Passo Fundo/RS — Muitas nuvens)
- 2026-11-14 | passo_fundo_rs | temp_min_noite: 17.0 C (Passo Fundo/RS — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-14 | passo_fundo_rs | temp_min_tarde: 17.0 C (Passo Fundo/RS — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-14 | rio_verde_go | temp_max_manha: 31.0 C (Rio Verde/GO — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-14 | rio_verde_go | temp_max_noite: 31.0 C (Rio Verde/GO — Muitas nuvens com chuva)
- 2026-11-14 | rio_verde_go | temp_max_tarde: 31.0 C (Rio Verde/GO — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-14 | rio_verde_go | temp_min_manha: 21.0 C (Rio Verde/GO — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-14 | rio_verde_go | temp_min_noite: 21.0 C (Rio Verde/GO — Muitas nuvens com chuva)
- 2026-11-14 | rio_verde_go | temp_min_tarde: 21.0 C (Rio Verde/GO — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-14 | sinop_mt | temp_max_manha: 34.0 C (Sinop/MT — Muitas nuvens com chuva)
- 2026-11-14 | sinop_mt | temp_max_noite: 34.0 C (Sinop/MT — Muitas nuvens com chuva)
- 2026-11-14 | sinop_mt | temp_max_tarde: 34.0 C (Sinop/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-14 | sinop_mt | temp_min_manha: 24.0 C (Sinop/MT — Muitas nuvens com chuva)
- 2026-11-14 | sinop_mt | temp_min_noite: 24.0 C (Sinop/MT — Muitas nuvens com chuva)
- 2026-11-14 | sinop_mt | temp_min_tarde: 24.0 C (Sinop/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-14 | sorriso_mt | temp_max_manha: 34.0 C (Sorriso/MT — Muitas nuvens com chuva)
- 2026-11-14 | sorriso_mt | temp_max_noite: 34.0 C (Sorriso/MT — Muitas nuvens com chuva)
- 2026-11-14 | sorriso_mt | temp_max_tarde: 34.0 C (Sorriso/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-14 | sorriso_mt | temp_min_manha: 23.0 C (Sorriso/MT — Muitas nuvens com chuva)
- 2026-11-14 | sorriso_mt | temp_min_noite: 23.0 C (Sorriso/MT — Muitas nuvens com chuva)
- 2026-11-14 | sorriso_mt | temp_min_tarde: 23.0 C (Sorriso/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-13 | cascavel_pr | temp_max_manha: 32.0 C (Cascavel/PR — Muitas nuvens)
- 2026-11-13 | cascavel_pr | temp_max_noite: 32.0 C (Cascavel/PR — Muitas nuvens)

---

## mpob

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
- 2026-11-03 | palma_malasia | page_fetched: 3201.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-02 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-01 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-31 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)

---

## noaa_cpc

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
- 2026-11-03 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-02 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-01 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-31 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)

---

## nopa

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
- 2026-11-03 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-02 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-01 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-31 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)

---

## noticias_rss

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
- 2026-11-03 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-02 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-01 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-10-31 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))

---

## usda_crop_progress

- 2026-11-08 | soybeans_eua | pct_harvested: 92.0 % (SOYBEANS - PROGRESS, MEASURED IN PCT HARVESTED)
- 2026-11-01 | soybeans_eua | pct_harvested: 88.0 % (SOYBEANS - PROGRESS, MEASURED IN PCT HARVESTED)

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
| 2026-11-14 | 7d | 2026-11-21 | farelo_cbot | 330.20 | 303.86 | 319.27 | 334.68 | baixista |
| 2026-11-14 | 7d | 2026-11-21 | oleo_cbot | 63.73 | 59.53 | 62.17 | 64.82 | baixista |
| 2026-11-14 | 7d | 2026-11-21 | soja_cbot | 1232.75 | 1163.57 | 1209.55 | 1255.52 | baixista |
| 2026-11-14 | 30d | 2026-12-14 | farelo_cbot | 330.20 | 251.08 | 282.98 | 314.88 | baixista |
| 2026-11-14 | 30d | 2026-12-14 | oleo_cbot | 63.73 | 51.30 | 56.77 | 62.25 | baixista |
| 2026-11-14 | 30d | 2026-12-14 | soja_cbot | 1232.75 | 1038.32 | 1133.49 | 1228.66 | baixista |
| 2026-11-13 | 7d | 2026-11-20 | farelo_cbot | 330.20 | 301.28 | 315.91 | 330.54 | baixista |
| 2026-11-13 | 7d | 2026-11-20 | oleo_cbot | 63.73 | 59.52 | 62.16 | 64.80 | baixista |
| 2026-11-13 | 7d | 2026-11-20 | soja_cbot | 1232.75 | 1159.14 | 1203.71 | 1248.28 | baixista |
| 2026-11-13 | 30d | 2026-12-13 | farelo_cbot | 330.20 | 249.26 | 279.55 | 309.83 | baixista |
| 2026-11-13 | 30d | 2026-12-13 | oleo_cbot | 63.73 | 51.29 | 56.75 | 62.22 | baixista |
| 2026-11-13 | 30d | 2026-12-13 | soja_cbot | 1232.75 | 1035.26 | 1127.53 | 1219.80 | baixista |
| 2026-11-12 | 7d | 2026-11-19 | farelo_cbot | 325.40 | 302.36 | 317.10 | 331.84 | baixista |
| 2026-11-12 | 7d | 2026-11-19 | oleo_cbot | 63.42 | 59.50 | 62.16 | 64.82 | baixista |
| 2026-11-12 | 7d | 2026-11-19 | soja_cbot | 1219.00 | 1159.68 | 1203.92 | 1248.17 | baixista |
| 2026-11-12 | 30d | 2026-12-12 | farelo_cbot | 325.40 | 244.59 | 275.11 | 305.63 | baixista |
| 2026-11-12 | 30d | 2026-12-12 | oleo_cbot | 63.42 | 51.11 | 56.62 | 62.12 | baixista |
| 2026-11-12 | 30d | 2026-12-12 | soja_cbot | 1219.00 | 1026.99 | 1118.60 | 1210.20 | baixista |
| 2026-11-11 | 7d | 2026-11-18 | farelo_cbot | 329.70 | 298.30 | 312.87 | 327.44 | baixista |
| 2026-11-11 | 7d | 2026-11-18 | oleo_cbot | 63.88 | 58.93 | 61.42 | 63.91 | baixista |
| 2026-11-11 | 7d | 2026-11-18 | soja_cbot | 1230.75 | 1155.60 | 1200.71 | 1245.82 | baixista |
| 2026-11-11 | 30d | 2026-12-11 | farelo_cbot | 329.70 | 233.76 | 263.92 | 294.08 | baixista |
| 2026-11-11 | 30d | 2026-12-11 | oleo_cbot | 63.88 | 50.52 | 55.68 | 60.83 | baixista |
| 2026-11-11 | 30d | 2026-12-11 | soja_cbot | 1230.75 | 1010.08 | 1103.46 | 1196.84 | baixista |

---


---

# Fila de julgamento — 2026-11-14

**8 item(ns).** Frase-gatilho: "lê a fila de julgamento e trata"

## 🔴 [nivel_tese] soja_cbot fechou em 1232.75 — acima da resistencia 1180.00
- id: `alerta-quebra_resistencia-soja_cbot-2026-11-13`
- fato: soja_cbot = 1232.75 vs nivel 1180.00 (2026-11-13)
- refs: soja_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] oleo_cbot fechou em 63.73 — abaixo do suporte 72.00
- id: `alerta-quebra_suporte-oleo_cbot-2026-11-13`
- fato: oleo_cbot = 63.73 vs nivel 72.00 (2026-11-13)
- refs: oleo_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] farelo_cbot fechou em 330.20 — acima da resistencia 325.00
- id: `alerta-quebra_resistencia-farelo_cbot-2026-11-13`
- fato: farelo_cbot = 330.20 vs nivel 325.00 (2026-11-13)
- refs: farelo_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] usd_brl_ptax fechou em 5.65 — acima da resistencia 5.30
- id: `alerta-quebra_resistencia-usd_brl_ptax-2026-11-13`
- fato: usd_brl_ptax = 5.65 vs nivel 5.30 (2026-11-13)
- refs: usd_brl_ptax
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] complexo_soja fechou em 1.95 — abaixo do suporte 2.50
- id: `alerta-quebra_suporte-complexo_soja-2026-11-13`
- fato: complexo_soja = 1.95 vs nivel 2.50 (2026-11-13)
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

## 🟡 [release] NOPA novo (2026-11-14)
- id: `release-nopa-2026-11-14`
- fato: fonte nopa com data 2026-11-14 — coletado, ainda nao interpretado
- refs: complexo_soja
- leitura: O numero muda o balanco/tese? Algo relevante pro farelo?

---
Trate só 🔴/🟡. Saída = `insights/*.md` (formato de generate_insights.txt, com `vies:`). Cite o `id` da fila no corpo do insight. Máx 1-3. Não duplicar insight recente.
