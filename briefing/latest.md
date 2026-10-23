# Briefing consolidado — 2026-10-23

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
- 2026-10-09 | eur_brl_ptax | valor: 5.5844 BRL/EUR (sgs=21619)
- 2026-10-09 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-10-09 | usd_brl_ptax | valor: 4.9892 BRL/USD (sgs=1)

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

---

## cme_cbot

- 2026-10-23 | farelo_cbot | abertura: 347.29998779296875 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-23 | farelo_cbot | fechamento: 348.1000061035156 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-23 | farelo_cbot | fechamento_F27: 345.8999938964844 USD/short_ton (ticker=ZMF27.CBT venc=jan/27)
- 2026-10-23 | farelo_cbot | fechamento_H27: 344.70001220703125 USD/short_ton (ticker=ZMH27.CBT venc=mar/27)
- 2026-10-23 | farelo_cbot | fechamento_K27: 346.1000061035156 USD/short_ton (ticker=ZMK27.CBT venc=mai/27)
- 2026-10-23 | farelo_cbot | fechamento_N27: 349.3999938964844 USD/short_ton (ticker=ZMN27.CBT venc=jul/27)
- 2026-10-23 | farelo_cbot | fechamento_Z26: 348.1000061035156 USD/short_ton (ticker=ZMZ26.CBT venc=dez/26)
- 2026-10-23 | farelo_cbot | maxima: 348.1000061035156 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-23 | farelo_cbot | minima: 347.29998779296875 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-23 | farelo_cbot | volume: 411.0 contratos (ticker=ZMZ26.CBT)
- 2026-10-23 | heating_oil_cbot | abertura: 4.764599800109863 USD/galão (ticker=HO=F)
- 2026-10-23 | heating_oil_cbot | fechamento: 4.754700183868408 USD/galão (ticker=HO=F)
- 2026-10-23 | heating_oil_cbot | maxima: 4.764599800109863 USD/galão (ticker=HO=F)
- 2026-10-23 | heating_oil_cbot | minima: 4.740200042724609 USD/galão (ticker=HO=F)
- 2026-10-23 | heating_oil_cbot | volume: 219.0 contratos (ticker=HO=F)
- 2026-10-23 | oleo_cbot | abertura: 66.9000015258789 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-10-23 | oleo_cbot | fechamento: 66.76000213623047 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-10-23 | oleo_cbot | fechamento_F27: 66.94999694824219 USD_cts/lb (ticker=ZLF27.CBT venc=jan/27)
- 2026-10-23 | oleo_cbot | fechamento_H27: 67.20999908447266 USD_cts/lb (ticker=ZLH27.CBT venc=mar/27)
- 2026-10-23 | oleo_cbot | fechamento_K27: 67.44999694824219 USD_cts/lb (ticker=ZLK27.CBT venc=mai/27)
- 2026-10-23 | oleo_cbot | fechamento_N27: 67.44999694824219 USD_cts/lb (ticker=ZLN27.CBT venc=jul/27)
- 2026-10-23 | oleo_cbot | fechamento_Z26: 66.76000213623047 USD_cts/lb (ticker=ZLZ26.CBT venc=dez/26)
- 2026-10-23 | oleo_cbot | maxima: 66.9000015258789 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-10-23 | oleo_cbot | minima: 66.83999633789062 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-10-23 | oleo_cbot | volume: 299.0 contratos (ticker=ZLZ26.CBT)
- 2026-10-23 | soja_cbot | abertura: 1264.75 USD/bushel (ticker=ZSF27.CBT)
- 2026-10-23 | soja_cbot | fechamento: 1265.75 USD/bushel (ticker=ZSF27.CBT)
- 2026-10-23 | soja_cbot | fechamento_F27: 1265.75 USD/bushel (ticker=ZSF27.CBT venc=jan/27)
- 2026-10-23 | soja_cbot | fechamento_H27: 1272.25 USD/bushel (ticker=ZSH27.CBT venc=mar/27)
- 2026-10-23 | soja_cbot | fechamento_K27: 1279.25 USD/bushel (ticker=ZSK27.CBT venc=mai/27)
- 2026-10-23 | soja_cbot | fechamento_N27: 1284.0 USD/bushel (ticker=ZSN27.CBT venc=jul/27)
- 2026-10-23 | soja_cbot | fechamento_Q27: 1268.5 USD/bushel (ticker=ZSQ27.CBT venc=ago/27)
- 2026-10-23 | soja_cbot | fechamento_X26: 1254.0 USD/bushel (ticker=ZSX26.CBT venc=nov/26)
- 2026-10-23 | soja_cbot | maxima: 1266.0 USD/bushel (ticker=ZSF27.CBT)
- 2026-10-23 | soja_cbot | minima: 1263.75 USD/bushel (ticker=ZSF27.CBT)
- 2026-10-23 | soja_cbot | volume: 781.0 contratos (ticker=ZSF27.CBT)
- 2026-10-22 | farelo_cbot | abertura: 347.29998779296875 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-22 | farelo_cbot | fechamento: 347.3999938964844 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-22 | farelo_cbot | fechamento_F27: 345.3999938964844 USD/short_ton (ticker=ZMF27.CBT venc=jan/27)
- 2026-10-22 | farelo_cbot | fechamento_H27: 344.1000061035156 USD/short_ton (ticker=ZMH27.CBT venc=mar/27)
- 2026-10-22 | farelo_cbot | fechamento_K27: 345.70001220703125 USD/short_ton (ticker=ZMK27.CBT venc=mai/27)
- 2026-10-22 | farelo_cbot | fechamento_N27: 348.8999938964844 USD/short_ton (ticker=ZMN27.CBT venc=jul/27)
- 2026-10-22 | farelo_cbot | fechamento_Z26: 347.3999938964844 USD/short_ton (ticker=ZMZ26.CBT venc=dez/26)
- 2026-10-22 | farelo_cbot | maxima: 348.1000061035156 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-22 | farelo_cbot | minima: 347.29998779296875 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-22 | farelo_cbot | volume: 411.0 contratos (ticker=ZMZ26.CBT)
- 2026-10-22 | heating_oil_cbot | abertura: 4.764599800109863 USD/galão (ticker=HO=F)
- 2026-10-22 | heating_oil_cbot | fechamento: 4.761300086975098 USD/galão (ticker=HO=F)
- 2026-10-22 | heating_oil_cbot | maxima: 4.764599800109863 USD/galão (ticker=HO=F)
- 2026-10-22 | heating_oil_cbot | minima: 4.740200042724609 USD/galão (ticker=HO=F)

---

## indicators

- 2026-10-23 | biodiesel_us | custo_oleo_usd_galao: 5.007 USD/galão (7.5 lb × óleo 66.76 cts/lb)
- 2026-10-23 | biodiesel_us | margem_usd_galao: 2.1127 USD/galão (receita 7.92 (HO 4.75 + 1.5×RIN 2.11) − custo 5.81 (óleo 5.01 + ind 0.80))
- 2026-10-23 | biodiesel_us | receita_usd_galao: 7.9197 USD/galão (HO 4.75 + 1.5×RIN 2.11)
- 2026-10-23 | complexo_soja | crush_margin_usd_bu: 2.3443 USD/bushel (Board Crush: farelo 348.10 + oleo 66.76 − soja 1265.75)
- 2026-10-23 | complexo_soja | far_soj_ratio_pct: 82.5 % (farelo 348.10/sht ÷ (soja 1265.75cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-10-23 | complexo_soja | indice_sobra_farelo: 80.0 0-100 (forte pressão baixista no farelo (4/5 condições))
- 2026-10-23 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-10-23 | complexo_soja | oil_meal_spread_usd_bu: -0.3146 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-10-23 | complexo_soja | oil_share_pct: 48.95 % (valor oleo 7.34 / total 15.00)
- 2026-10-23 | soja_paridade_br | brl_saca_paridade: 140.59 BRL/saca60kg (CBOT 1265.75 cts × USD/BRL 5.0383 (sem basis))
- 2026-10-22 | biodiesel_us | custo_oleo_usd_galao: 5.0048 USD/galão (7.5 lb × óleo 66.73 cts/lb)
- 2026-10-22 | biodiesel_us | margem_usd_galao: 2.1215 USD/galão (receita 7.93 (HO 4.76 + 1.5×RIN 2.11) − custo 5.80 (óleo 5.00 + ind 0.80))
- 2026-10-22 | biodiesel_us | receita_usd_galao: 7.9263 USD/galão (HO 4.76 + 1.5×RIN 2.11)
- 2026-10-22 | complexo_soja | crush_margin_usd_bu: 2.3306 USD/bushel (Board Crush: farelo 347.40 + oleo 66.73 − soja 1265.25)
- 2026-10-22 | complexo_soja | far_soj_ratio_pct: 82.37 % (farelo 347.40/sht ÷ (soja 1265.25cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-10-22 | complexo_soja | indice_sobra_farelo: 80.0 0-100 (forte pressão baixista no farelo (4/5 condições))
- 2026-10-22 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-10-22 | complexo_soja | oil_meal_spread_usd_bu: -0.3025 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-10-22 | complexo_soja | oil_share_pct: 48.99 % (valor oleo 7.34 / total 14.98)
- 2026-10-22 | soja_paridade_br | brl_saca_paridade: 140.54 BRL/saca60kg (CBOT 1265.25 cts × USD/BRL 5.0383 (sem basis))
- 2026-10-21 | biodiesel_us | custo_oleo_usd_galao: 4.9478 USD/galão (7.5 lb × óleo 65.97 cts/lb)
- 2026-10-21 | biodiesel_us | margem_usd_galao: 2.1805 USD/galão (receita 7.93 (HO 4.76 + 1.5×RIN 2.11) − custo 5.75 (óleo 4.95 + ind 0.80))
- 2026-10-21 | biodiesel_us | receita_usd_galao: 7.9283 USD/galão (HO 4.76 + 1.5×RIN 2.11)
- 2026-10-21 | complexo_soja | crush_margin_usd_bu: 2.3368 USD/bushel (Board Crush: farelo 348.30 + oleo 65.97 − soja 1258.25)
- 2026-10-21 | complexo_soja | far_soj_ratio_pct: 83.04 % (farelo 348.30/sht ÷ (soja 1258.25cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-10-21 | complexo_soja | indice_sobra_farelo: 80.0 0-100 (forte pressão baixista no farelo (4/5 condições))
- 2026-10-21 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-10-21 | complexo_soja | oil_meal_spread_usd_bu: -0.4059 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-10-21 | complexo_soja | oil_share_pct: 48.64 % (valor oleo 7.26 / total 14.92)
- 2026-10-21 | soja_paridade_br | brl_saca_paridade: 139.47 BRL/saca60kg (CBOT 1258.25 cts × USD/BRL 5.0277 (sem basis))
- 2026-10-20 | biodiesel_us | custo_oleo_usd_galao: 5.0048 USD/galão (7.5 lb × óleo 66.73 cts/lb)
- 2026-10-20 | biodiesel_us | margem_usd_galao: 2.2852 USD/galão (receita 8.09 (HO 4.93 + 1.5×RIN 2.11) − custo 5.80 (óleo 5.00 + ind 0.80))
- 2026-10-20 | biodiesel_us | receita_usd_galao: 8.09 USD/galão (HO 4.93 + 1.5×RIN 2.11)
- 2026-10-20 | complexo_soja | crush_margin_usd_bu: 2.3767 USD/bushel (Board Crush: farelo 348.70 + oleo 66.73 − soja 1263.50)
- 2026-10-20 | complexo_soja | far_soj_ratio_pct: 82.79 % (farelo 348.70/sht ÷ (soja 1263.50cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-10-20 | complexo_soja | indice_sobra_farelo: 80.0 0-100 (forte pressão baixista no farelo (4/5 condições))
- 2026-10-20 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-10-20 | complexo_soja | oil_meal_spread_usd_bu: -0.3311 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-10-20 | complexo_soja | oil_share_pct: 48.9 % (valor oleo 7.34 / total 15.01)
- 2026-10-20 | soja_paridade_br | brl_saca_paridade: 139.67 BRL/saca60kg (CBOT 1263.50 cts × USD/BRL 5.0140 (sem basis))
- 2026-10-19 | biodiesel_us | custo_oleo_usd_galao: 5.0018 USD/galão (7.5 lb × óleo 66.69 cts/lb)
- 2026-10-19 | biodiesel_us | margem_usd_galao: 2.2834 USD/galão (receita 8.09 (HO 4.92 + 1.5×RIN 2.11) − custo 5.80 (óleo 5.00 + ind 0.80))
- 2026-10-19 | biodiesel_us | receita_usd_galao: 8.0851 USD/galão (HO 4.92 + 1.5×RIN 2.11)
- 2026-10-19 | complexo_soja | crush_margin_usd_bu: 2.454 USD/bushel (Board Crush: farelo 354.80 + oleo 66.69 − soja 1268.75)
- 2026-10-19 | complexo_soja | far_soj_ratio_pct: 83.89 % (farelo 354.80/sht ÷ (soja 1268.75cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-10-19 | complexo_soja | indice_sobra_farelo: 80.0 0-100 (forte pressão baixista no farelo (4/5 condições))
- 2026-10-19 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-10-19 | complexo_soja | oil_meal_spread_usd_bu: -0.4697 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-10-19 | complexo_soja | oil_share_pct: 48.45 % (valor oleo 7.34 / total 15.14)
- 2026-10-19 | soja_paridade_br | brl_saca_paridade: 141.43 BRL/saca60kg (CBOT 1268.75 cts × USD/BRL 5.0564 (sem basis))

---

## inmet

- 2026-10-23 | cascavel_pr | temp_max_manha: 26.0 C (Cascavel/PR — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-23 | cascavel_pr | temp_max_noite: 26.0 C (Cascavel/PR — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-23 | cascavel_pr | temp_max_tarde: 26.0 C (Cascavel/PR — Muitas nuvens pancadas de chuva e possível queda de granizo)
- 2026-10-23 | cascavel_pr | temp_min_manha: 17.0 C (Cascavel/PR — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-23 | cascavel_pr | temp_min_noite: 17.0 C (Cascavel/PR — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-23 | cascavel_pr | temp_min_tarde: 17.0 C (Cascavel/PR — Muitas nuvens pancadas de chuva e possível queda de granizo)
- 2026-10-23 | cuiaba_mt | temp_max_manha: 39.0 C (Cuiaba/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-23 | cuiaba_mt | temp_max_noite: 39.0 C (Cuiaba/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-23 | cuiaba_mt | temp_max_tarde: 39.0 C (Cuiaba/MT — Muitas nuvens com pancadas de chuva e trovoadas)
- 2026-10-23 | cuiaba_mt | temp_min_manha: 26.0 C (Cuiaba/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-23 | cuiaba_mt | temp_min_noite: 26.0 C (Cuiaba/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-23 | cuiaba_mt | temp_min_tarde: 26.0 C (Cuiaba/MT — Muitas nuvens com pancadas de chuva e trovoadas)
- 2026-10-23 | lucas_rio_verde_mt | temp_max_manha: 36.0 C (Lucas do Rio Verde/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-23 | lucas_rio_verde_mt | temp_max_noite: 36.0 C (Lucas do Rio Verde/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-23 | lucas_rio_verde_mt | temp_max_tarde: 36.0 C (Lucas do Rio Verde/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-23 | lucas_rio_verde_mt | temp_min_manha: 25.0 C (Lucas do Rio Verde/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-23 | lucas_rio_verde_mt | temp_min_noite: 25.0 C (Lucas do Rio Verde/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-23 | lucas_rio_verde_mt | temp_min_tarde: 25.0 C (Lucas do Rio Verde/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-23 | maringa_pr | temp_max_manha: 26.0 C (Maringa/PR — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-23 | maringa_pr | temp_max_noite: 26.0 C (Maringa/PR — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-23 | maringa_pr | temp_max_tarde: 26.0 C (Maringa/PR — Muitas nuvens pancadas de chuva e possível queda de granizo)
- 2026-10-23 | maringa_pr | temp_min_manha: 19.0 C (Maringa/PR — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-23 | maringa_pr | temp_min_noite: 19.0 C (Maringa/PR — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-23 | maringa_pr | temp_min_tarde: 19.0 C (Maringa/PR — Muitas nuvens pancadas de chuva e possível queda de granizo)
- 2026-10-23 | passo_fundo_rs | temp_max_manha: 21.0 C (Passo Fundo/RS — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-23 | passo_fundo_rs | temp_max_noite: 21.0 C (Passo Fundo/RS — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-23 | passo_fundo_rs | temp_max_tarde: 21.0 C (Passo Fundo/RS — Muitas nuvens com pancadas de chuva e trovoadas)
- 2026-10-23 | passo_fundo_rs | temp_min_manha: 16.0 C (Passo Fundo/RS — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-23 | passo_fundo_rs | temp_min_noite: 16.0 C (Passo Fundo/RS — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-23 | passo_fundo_rs | temp_min_tarde: 16.0 C (Passo Fundo/RS — Muitas nuvens com pancadas de chuva e trovoadas)
- 2026-10-23 | rio_verde_go | temp_max_manha: 35.0 C (Rio Verde/GO — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-23 | rio_verde_go | temp_max_noite: 35.0 C (Rio Verde/GO — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-23 | rio_verde_go | temp_max_tarde: 35.0 C (Rio Verde/GO — Muitas nuvens com pancadas de chuva e trovoadas)
- 2026-10-23 | rio_verde_go | temp_min_manha: 22.0 C (Rio Verde/GO — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-23 | rio_verde_go | temp_min_noite: 22.0 C (Rio Verde/GO — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-23 | rio_verde_go | temp_min_tarde: 22.0 C (Rio Verde/GO — Muitas nuvens com pancadas de chuva e trovoadas)
- 2026-10-23 | sinop_mt | temp_max_manha: 36.0 C (Sinop/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-23 | sinop_mt | temp_max_noite: 36.0 C (Sinop/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-23 | sinop_mt | temp_max_tarde: 36.0 C (Sinop/MT — Muitas nuvens com pancadas de chuva e trovoadas)
- 2026-10-23 | sinop_mt | temp_min_manha: 25.0 C (Sinop/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-23 | sinop_mt | temp_min_noite: 25.0 C (Sinop/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-23 | sinop_mt | temp_min_tarde: 25.0 C (Sinop/MT — Muitas nuvens com pancadas de chuva e trovoadas)
- 2026-10-23 | sorriso_mt | temp_max_manha: 37.0 C (Sorriso/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-23 | sorriso_mt | temp_max_noite: 37.0 C (Sorriso/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-23 | sorriso_mt | temp_max_tarde: 37.0 C (Sorriso/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-23 | sorriso_mt | temp_min_manha: 25.0 C (Sorriso/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-23 | sorriso_mt | temp_min_noite: 25.0 C (Sorriso/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-23 | sorriso_mt | temp_min_tarde: 25.0 C (Sorriso/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-22 | cascavel_pr | temp_max_manha: 22.0 C (Cascavel/PR — Nublado com pancadas de chuva e trovoadas)
- 2026-10-22 | cascavel_pr | temp_max_noite: 22.0 C (Cascavel/PR — Muitas nuvens com pancadas de chuva e trovoadas isoladas)

---

## mpob

- 2026-10-23 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-22 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-21 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
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

---

## noaa_cpc

- 2026-10-23 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-22 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-21 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
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

---

## nopa

- 2026-10-23 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-22 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-21 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
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

---

## noticias_rss

- 2026-10-23 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-10-22 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-10-21 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
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
| 2026-10-23 | 7d | 2026-10-30 | farelo_cbot | 348.10 | 325.31 | 347.54 | 369.76 | lateral |
| 2026-10-23 | 7d | 2026-10-30 | oleo_cbot | 66.76 | 62.48 | 66.13 | 69.78 | baixista |
| 2026-10-23 | 7d | 2026-10-30 | soja_cbot | 1265.75 | 1202.85 | 1256.53 | 1310.21 | baixista |
| 2026-10-23 | 30d | 2026-11-22 | farelo_cbot | 348.10 | 297.61 | 343.62 | 389.63 | baixista |
| 2026-10-23 | 30d | 2026-11-22 | oleo_cbot | 66.76 | 56.27 | 63.83 | 71.40 | baixista |
| 2026-10-23 | 30d | 2026-11-22 | soja_cbot | 1265.75 | 1109.57 | 1220.69 | 1331.82 | baixista |
| 2026-10-22 | 7d | 2026-10-29 | farelo_cbot | 347.40 | 324.15 | 346.59 | 369.04 | lateral |
| 2026-10-22 | 7d | 2026-10-29 | oleo_cbot | 66.73 | 61.85 | 65.47 | 69.09 | baixista |
| 2026-10-22 | 7d | 2026-10-29 | soja_cbot | 1265.25 | 1194.49 | 1248.30 | 1302.12 | baixista |
| 2026-10-22 | 30d | 2026-11-21 | farelo_cbot | 347.40 | 294.95 | 341.42 | 387.89 | baixista |
| 2026-10-22 | 30d | 2026-11-21 | oleo_cbot | 66.73 | 55.97 | 63.47 | 70.97 | baixista |
| 2026-10-22 | 30d | 2026-11-21 | soja_cbot | 1265.25 | 1100.03 | 1211.44 | 1322.85 | baixista |
| 2026-10-21 | 7d | 2026-10-28 | farelo_cbot | 348.30 | 323.92 | 346.70 | 369.48 | lateral |
| 2026-10-21 | 7d | 2026-10-28 | oleo_cbot | 65.97 | 62.79 | 66.48 | 70.16 | lateral |
| 2026-10-21 | 7d | 2026-10-28 | soja_cbot | 1258.25 | 1199.50 | 1254.12 | 1308.73 | baixista |
| 2026-10-21 | 30d | 2026-11-20 | farelo_cbot | 348.30 | 293.19 | 340.36 | 387.53 | baixista |
| 2026-10-21 | 30d | 2026-11-20 | oleo_cbot | 65.97 | 57.59 | 65.21 | 72.84 | baixista |
| 2026-10-21 | 30d | 2026-11-20 | soja_cbot | 1258.25 | 1107.32 | 1220.39 | 1333.46 | baixista |
| 2026-10-20 | 7d | 2026-10-27 | farelo_cbot | 348.70 | 329.37 | 352.15 | 374.93 | lateral |
| 2026-10-20 | 7d | 2026-10-27 | oleo_cbot | 66.73 | 62.57 | 66.48 | 70.39 | lateral |
| 2026-10-20 | 7d | 2026-10-27 | soja_cbot | 1263.50 | 1203.55 | 1259.20 | 1314.84 | baixista |
| 2026-10-20 | 30d | 2026-11-19 | farelo_cbot | 348.70 | 298.91 | 346.06 | 393.22 | baixista |
| 2026-10-20 | 30d | 2026-11-19 | oleo_cbot | 66.73 | 57.56 | 65.65 | 73.75 | baixista |
| 2026-10-20 | 30d | 2026-11-19 | soja_cbot | 1263.50 | 1114.09 | 1229.29 | 1344.48 | baixista |

---


---

# Fila de julgamento — 2026-10-23

**7 item(ns).** Frase-gatilho: "lê a fila de julgamento e trata"

## 🔴 [nivel_tese] soja_cbot fechou em 1265.75 — acima da resistencia 1180.00
- id: `alerta-quebra_resistencia-soja_cbot-2026-10-23`
- fato: soja_cbot = 1265.75 vs nivel 1180.00 (2026-10-23)
- refs: soja_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] oleo_cbot fechou em 66.76 — abaixo do suporte 72.00
- id: `alerta-quebra_suporte-oleo_cbot-2026-10-23`
- fato: oleo_cbot = 66.76 vs nivel 72.00 (2026-10-23)
- refs: oleo_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] farelo_cbot fechou em 348.10 — acima da resistencia 325.00
- id: `alerta-quebra_resistencia-farelo_cbot-2026-10-23`
- fato: farelo_cbot = 348.10 vs nivel 325.00 (2026-10-23)
- refs: farelo_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] complexo_soja fechou em 2.34 — abaixo do suporte 2.50
- id: `alerta-quebra_suporte-complexo_soja-2026-10-23`
- fato: complexo_soja = 2.34 vs nivel 2.50 (2026-10-23)
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

## 🟡 [release] NOPA novo (2026-10-23)
- id: `release-nopa-2026-10-23`
- fato: fonte nopa com data 2026-10-23 — coletado, ainda nao interpretado
- refs: complexo_soja
- leitura: O numero muda o balanco/tese? Algo relevante pro farelo?

---
Trate só 🔴/🟡. Saída = `insights/*.md` (formato de generate_insights.txt, com `vies:`). Cite o `id` da fila no corpo do insight. Máx 1-3. Não duplicar insight recente.
