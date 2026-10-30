# Briefing consolidado — 2026-10-30

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

---

## cme_cbot

- 2026-10-30 | farelo_cbot | abertura: 329.29998779296875 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-30 | farelo_cbot | fechamento: 329.20001220703125 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-30 | farelo_cbot | fechamento_F27: 329.5 USD/short_ton (ticker=ZMF27.CBT venc=jan/27)
- 2026-10-30 | farelo_cbot | fechamento_H27: 330.70001220703125 USD/short_ton (ticker=ZMH27.CBT venc=mar/27)
- 2026-10-30 | farelo_cbot | fechamento_K27: 334.0 USD/short_ton (ticker=ZMK27.CBT venc=mai/27)
- 2026-10-30 | farelo_cbot | fechamento_N27: 338.20001220703125 USD/short_ton (ticker=ZMN27.CBT venc=jul/27)
- 2026-10-30 | farelo_cbot | fechamento_Z26: 329.20001220703125 USD/short_ton (ticker=ZMZ26.CBT venc=dez/26)
- 2026-10-30 | farelo_cbot | maxima: 330.1000061035156 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-30 | farelo_cbot | minima: 328.29998779296875 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-30 | farelo_cbot | volume: 1528.0 contratos (ticker=ZMZ26.CBT)
- 2026-10-30 | heating_oil_cbot | abertura: 4.579999923706055 USD/galão (ticker=HO=F)
- 2026-10-30 | heating_oil_cbot | fechamento: 4.573800086975098 USD/galão (ticker=HO=F)
- 2026-10-30 | heating_oil_cbot | maxima: 4.591899871826172 USD/galão (ticker=HO=F)
- 2026-10-30 | heating_oil_cbot | minima: 4.570000171661377 USD/galão (ticker=HO=F)
- 2026-10-30 | heating_oil_cbot | volume: 491.0 contratos (ticker=HO=F)
- 2026-10-30 | oleo_cbot | abertura: 65.66000366210938 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-10-30 | oleo_cbot | fechamento: 65.80999755859375 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-10-30 | oleo_cbot | fechamento_F27: 66.04000091552734 USD_cts/lb (ticker=ZLF27.CBT venc=jan/27)
- 2026-10-30 | oleo_cbot | fechamento_H27: 66.47000122070312 USD_cts/lb (ticker=ZLH27.CBT venc=mar/27)
- 2026-10-30 | oleo_cbot | fechamento_K27: 66.7699966430664 USD_cts/lb (ticker=ZLK27.CBT venc=mai/27)
- 2026-10-30 | oleo_cbot | fechamento_N27: 66.83999633789062 USD_cts/lb (ticker=ZLN27.CBT venc=jul/27)
- 2026-10-30 | oleo_cbot | fechamento_Z26: 65.80999755859375 USD_cts/lb (ticker=ZLZ26.CBT venc=dez/26)
- 2026-10-30 | oleo_cbot | maxima: 65.9000015258789 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-10-30 | oleo_cbot | minima: 65.63999938964844 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-10-30 | oleo_cbot | volume: 1709.0 contratos (ticker=ZLZ26.CBT)
- 2026-10-30 | soja_cbot | abertura: 1234.5 USD/bushel (ticker=ZSF27.CBT)
- 2026-10-30 | soja_cbot | fechamento: 1234.0 USD/bushel (ticker=ZSF27.CBT)
- 2026-10-30 | soja_cbot | fechamento_F27: 1234.0 USD/bushel (ticker=ZSF27.CBT venc=jan/27)
- 2026-10-30 | soja_cbot | fechamento_H27: 1242.5 USD/bushel (ticker=ZSH27.CBT venc=mar/27)
- 2026-10-30 | soja_cbot | fechamento_K27: 1252.25 USD/bushel (ticker=ZSK27.CBT venc=mai/27)
- 2026-10-30 | soja_cbot | fechamento_N27: 1259.5 USD/bushel (ticker=ZSN27.CBT venc=jul/27)
- 2026-10-30 | soja_cbot | fechamento_Q27: 1245.25 USD/bushel (ticker=ZSQ27.CBT venc=ago/27)
- 2026-10-30 | soja_cbot | fechamento_X26: 1222.0 USD/bushel (ticker=ZSX26.CBT venc=nov/26)
- 2026-10-30 | soja_cbot | maxima: 1236.75 USD/bushel (ticker=ZSF27.CBT)
- 2026-10-30 | soja_cbot | minima: 1230.75 USD/bushel (ticker=ZSF27.CBT)
- 2026-10-30 | soja_cbot | volume: 3667.0 contratos (ticker=ZSF27.CBT)
- 2026-10-29 | farelo_cbot | abertura: 329.29998779296875 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-29 | farelo_cbot | fechamento: 329.20001220703125 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-29 | farelo_cbot | fechamento_F27: 329.70001220703125 USD/short_ton (ticker=ZMF27.CBT venc=jan/27)
- 2026-10-29 | farelo_cbot | fechamento_H27: 330.79998779296875 USD/short_ton (ticker=ZMH27.CBT venc=mar/27)
- 2026-10-29 | farelo_cbot | fechamento_K27: 334.0 USD/short_ton (ticker=ZMK27.CBT venc=mai/27)
- 2026-10-29 | farelo_cbot | fechamento_N27: 338.1000061035156 USD/short_ton (ticker=ZMN27.CBT venc=jul/27)
- 2026-10-29 | farelo_cbot | fechamento_Z26: 329.20001220703125 USD/short_ton (ticker=ZMZ26.CBT venc=dez/26)
- 2026-10-29 | farelo_cbot | maxima: 330.1000061035156 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-29 | farelo_cbot | minima: 328.29998779296875 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-29 | farelo_cbot | volume: 1528.0 contratos (ticker=ZMZ26.CBT)
- 2026-10-29 | heating_oil_cbot | abertura: 4.579999923706055 USD/galão (ticker=HO=F)
- 2026-10-29 | heating_oil_cbot | fechamento: 4.58050012588501 USD/galão (ticker=HO=F)
- 2026-10-29 | heating_oil_cbot | maxima: 4.591899871826172 USD/galão (ticker=HO=F)
- 2026-10-29 | heating_oil_cbot | minima: 4.570000171661377 USD/galão (ticker=HO=F)

---

## indicators

- 2026-10-30 | biodiesel_us | custo_oleo_usd_galao: 4.9357 USD/galão (7.5 lb × óleo 65.81 cts/lb)
- 2026-10-30 | biodiesel_us | margem_usd_galao: 2.0031 USD/galão (receita 7.74 (HO 4.57 + 1.5×RIN 2.11) − custo 5.74 (óleo 4.94 + ind 0.80))
- 2026-10-30 | biodiesel_us | receita_usd_galao: 7.7388 USD/galão (HO 4.57 + 1.5×RIN 2.11)
- 2026-10-30 | complexo_soja | crush_margin_usd_bu: 2.1415 USD/bushel (Board Crush: farelo 329.20 + oleo 65.81 − soja 1234.00)
- 2026-10-30 | complexo_soja | far_soj_ratio_pct: 80.03 % (farelo 329.20/sht ÷ (soja 1234.00cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-10-30 | complexo_soja | indice_sobra_farelo: 75.0 0-100 (sobra relevante (3/4 condições))
- 2026-10-30 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-10-30 | complexo_soja | oil_meal_spread_usd_bu: -0.0033 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-10-30 | complexo_soja | oil_share_pct: 49.99 % (valor oleo 7.24 / total 14.48)
- 2026-10-30 | soja_paridade_br | brl_saca_paridade: 146.21 BRL/saca60kg (CBOT 1234.00 cts × USD/BRL 5.3744 (sem basis))
- 2026-10-29 | biodiesel_us | custo_oleo_usd_galao: 4.9268 USD/galão (7.5 lb × óleo 65.69 cts/lb)
- 2026-10-29 | biodiesel_us | margem_usd_galao: 2.0187 USD/galão (receita 7.75 (HO 4.58 + 1.5×RIN 2.11) − custo 5.73 (óleo 4.93 + ind 0.80))
- 2026-10-29 | biodiesel_us | receita_usd_galao: 7.7455 USD/galão (HO 4.58 + 1.5×RIN 2.11)
- 2026-10-29 | complexo_soja | crush_margin_usd_bu: 2.1233 USD/bushel (Board Crush: farelo 329.20 + oleo 65.69 − soja 1234.50)
- 2026-10-29 | complexo_soja | far_soj_ratio_pct: 80.0 % (farelo 329.20/sht ÷ (soja 1234.50cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-10-29 | complexo_soja | indice_sobra_farelo: 75.0 0-100 (sobra relevante (3/4 condições))
- 2026-10-29 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-10-29 | complexo_soja | oil_meal_spread_usd_bu: -0.0165 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-10-29 | complexo_soja | oil_share_pct: 49.94 % (valor oleo 7.23 / total 14.47)
- 2026-10-29 | soja_paridade_br | brl_saca_paridade: 146.27 BRL/saca60kg (CBOT 1234.50 cts × USD/BRL 5.3744 (sem basis))
- 2026-10-28 | biodiesel_us | custo_oleo_usd_galao: 4.917 USD/galão (7.5 lb × óleo 65.56 cts/lb)
- 2026-10-28 | biodiesel_us | margem_usd_galao: 2.2632 USD/galão (receita 7.98 (HO 4.82 + 1.5×RIN 2.11) − custo 5.72 (óleo 4.92 + ind 0.80))
- 2026-10-28 | biodiesel_us | receita_usd_galao: 7.9802 USD/galão (HO 4.82 + 1.5×RIN 2.11)
- 2026-10-28 | complexo_soja | crush_margin_usd_bu: 2.217 USD/bushel (Board Crush: farelo 335.70 + oleo 65.56 − soja 1238.00)
- 2026-10-28 | complexo_soja | far_soj_ratio_pct: 81.35 % (farelo 335.70/sht ÷ (soja 1238.00cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-10-28 | complexo_soja | indice_sobra_farelo: 75.0 0-100 (sobra relevante (3/4 condições))
- 2026-10-28 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-10-28 | complexo_soja | oil_meal_spread_usd_bu: -0.1738 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-10-28 | complexo_soja | oil_share_pct: 49.4 % (valor oleo 7.21 / total 14.60)
- 2026-10-28 | soja_paridade_br | brl_saca_paridade: 145.8 BRL/saca60kg (CBOT 1238.00 cts × USD/BRL 5.3420 (sem basis))
- 2026-10-27 | biodiesel_us | custo_oleo_usd_galao: 5.0032 USD/galão (7.5 lb × óleo 66.71 cts/lb)
- 2026-10-27 | biodiesel_us | margem_usd_galao: 2.1369 USD/galão (receita 7.94 (HO 4.78 + 1.5×RIN 2.11) − custo 5.80 (óleo 5.00 + ind 0.80))
- 2026-10-27 | biodiesel_us | receita_usd_galao: 7.9402 USD/galão (HO 4.78 + 1.5×RIN 2.11)
- 2026-10-27 | complexo_soja | crush_margin_usd_bu: 2.2693 USD/bushel (Board Crush: farelo 334.60 + oleo 66.71 − soja 1243.00)
- 2026-10-27 | complexo_soja | far_soj_ratio_pct: 80.76 % (farelo 334.60/sht ÷ (soja 1243.00cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-10-27 | complexo_soja | indice_sobra_farelo: 75.0 0-100 (sobra relevante (3/4 condições))
- 2026-10-27 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-10-27 | complexo_soja | oil_meal_spread_usd_bu: -0.0231 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-10-27 | complexo_soja | oil_share_pct: 49.92 % (valor oleo 7.34 / total 14.70)
- 2026-10-27 | soja_paridade_br | brl_saca_paridade: 146.18 BRL/saca60kg (CBOT 1243.00 cts × USD/BRL 5.3346 (sem basis))
- 2026-10-26 | biodiesel_us | custo_oleo_usd_galao: 5.0258 USD/galão (7.5 lb × óleo 67.01 cts/lb)
- 2026-10-26 | biodiesel_us | margem_usd_galao: 2.2513 USD/galão (receita 8.08 (HO 4.91 + 1.5×RIN 2.11) − custo 5.83 (óleo 5.03 + ind 0.80))
- 2026-10-26 | biodiesel_us | receita_usd_galao: 8.077 USD/galão (HO 4.91 + 1.5×RIN 2.11)
- 2026-10-26 | complexo_soja | crush_margin_usd_bu: 2.3305 USD/bushel (Board Crush: farelo 340.20 + oleo 67.01 − soja 1252.50)
- 2026-10-26 | complexo_soja | far_soj_ratio_pct: 81.49 % (farelo 340.20/sht ÷ (soja 1252.50cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-10-26 | complexo_soja | indice_sobra_farelo: 75.0 0-100 (sobra relevante (3/4 condições))
- 2026-10-26 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-10-26 | complexo_soja | oil_meal_spread_usd_bu: -0.1133 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-10-26 | complexo_soja | oil_share_pct: 49.62 % (valor oleo 7.37 / total 14.86)
- 2026-10-26 | soja_paridade_br | brl_saca_paridade: 151.89 BRL/saca60kg (CBOT 1252.50 cts × USD/BRL 5.5007 (sem basis))

---

## inmet

- 2026-10-30 | cascavel_pr | temp_max_manha: 24.0 C (Cascavel/PR — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-30 | cascavel_pr | temp_max_noite: 24.0 C (Cascavel/PR — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-30 | cascavel_pr | temp_max_tarde: 24.0 C (Cascavel/PR — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-30 | cascavel_pr | temp_min_manha: 17.0 C (Cascavel/PR — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-30 | cascavel_pr | temp_min_noite: 17.0 C (Cascavel/PR — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-30 | cascavel_pr | temp_min_tarde: 17.0 C (Cascavel/PR — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-30 | cuiaba_mt | temp_max_manha: 33.0 C (Cuiaba/MT — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-30 | cuiaba_mt | temp_max_noite: 33.0 C (Cuiaba/MT — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-30 | cuiaba_mt | temp_max_tarde: 33.0 C (Cuiaba/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-30 | cuiaba_mt | temp_min_manha: 24.0 C (Cuiaba/MT — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-30 | cuiaba_mt | temp_min_noite: 24.0 C (Cuiaba/MT — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-30 | cuiaba_mt | temp_min_tarde: 24.0 C (Cuiaba/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-30 | lucas_rio_verde_mt | temp_max_manha: 33.0 C (Lucas do Rio Verde/MT — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-30 | lucas_rio_verde_mt | temp_max_noite: 33.0 C (Lucas do Rio Verde/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-30 | lucas_rio_verde_mt | temp_max_tarde: 33.0 C (Lucas do Rio Verde/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-30 | lucas_rio_verde_mt | temp_min_manha: 23.0 C (Lucas do Rio Verde/MT — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-30 | lucas_rio_verde_mt | temp_min_noite: 23.0 C (Lucas do Rio Verde/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-30 | lucas_rio_verde_mt | temp_min_tarde: 23.0 C (Lucas do Rio Verde/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-30 | maringa_pr | temp_max_manha: 27.0 C (Maringa/PR — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-30 | maringa_pr | temp_max_noite: 27.0 C (Maringa/PR — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-30 | maringa_pr | temp_max_tarde: 27.0 C (Maringa/PR — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-30 | maringa_pr | temp_min_manha: 19.0 C (Maringa/PR — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-30 | maringa_pr | temp_min_noite: 19.0 C (Maringa/PR — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-30 | maringa_pr | temp_min_tarde: 19.0 C (Maringa/PR — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-30 | passo_fundo_rs | temp_max_manha: 24.0 C (Passo Fundo/RS — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-30 | passo_fundo_rs | temp_max_noite: 24.0 C (Passo Fundo/RS — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-30 | passo_fundo_rs | temp_max_tarde: 24.0 C (Passo Fundo/RS — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-30 | passo_fundo_rs | temp_min_manha: 13.0 C (Passo Fundo/RS — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-30 | passo_fundo_rs | temp_min_noite: 13.0 C (Passo Fundo/RS — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-30 | passo_fundo_rs | temp_min_tarde: 13.0 C (Passo Fundo/RS — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-30 | rio_verde_go | temp_max_manha: 30.0 C (Rio Verde/GO — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-30 | rio_verde_go | temp_max_noite: 30.0 C (Rio Verde/GO — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-30 | rio_verde_go | temp_max_tarde: 30.0 C (Rio Verde/GO — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-30 | rio_verde_go | temp_min_manha: 21.0 C (Rio Verde/GO — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-30 | rio_verde_go | temp_min_noite: 21.0 C (Rio Verde/GO — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-30 | rio_verde_go | temp_min_tarde: 21.0 C (Rio Verde/GO — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-30 | sinop_mt | temp_max_manha: 34.0 C (Sinop/MT — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-30 | sinop_mt | temp_max_noite: 34.0 C (Sinop/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-30 | sinop_mt | temp_max_tarde: 34.0 C (Sinop/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-30 | sinop_mt | temp_min_manha: 23.0 C (Sinop/MT — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-30 | sinop_mt | temp_min_noite: 23.0 C (Sinop/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-30 | sinop_mt | temp_min_tarde: 23.0 C (Sinop/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-30 | sorriso_mt | temp_max_manha: 35.0 C (Sorriso/MT — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-30 | sorriso_mt | temp_max_noite: 35.0 C (Sorriso/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-30 | sorriso_mt | temp_max_tarde: 35.0 C (Sorriso/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-30 | sorriso_mt | temp_min_manha: 24.0 C (Sorriso/MT — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-30 | sorriso_mt | temp_min_noite: 24.0 C (Sorriso/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-30 | sorriso_mt | temp_min_tarde: 24.0 C (Sorriso/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-29 | cascavel_pr | temp_max_manha: 22.0 C (Cascavel/PR — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-29 | cascavel_pr | temp_max_noite: 22.0 C (Cascavel/PR — Muitas nuvens com pancadas de chuva e trovoadas isoladas)

---

## mpob

- 2026-10-30 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-29 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-28 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-27 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-26 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-25 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-24 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)

---

## noaa_cpc

- 2026-10-30 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-29 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-28 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-27 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-26 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-25 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-24 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)

---

## nopa

- 2026-10-30 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-29 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-28 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-27 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-26 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-25 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-24 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)

---

## noticias_rss

- 2026-10-30 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-10-29 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-10-28 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-10-27 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-10-26 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-10-25 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-10-24 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))

---

## usda_crop_progress

- 2026-10-25 | soybeans_eua | pct_harvested: 79.0 % (SOYBEANS - PROGRESS, MEASURED IN PCT HARVESTED)
- 2026-10-18 | soybeans_eua | pct_harvested: 64.0 % (SOYBEANS - PROGRESS, MEASURED IN PCT HARVESTED)

---

# FORECASTS ATIVOS (bandas estatisticas)

Bandas calculadas via MA20+volatilidade+slope curto. Claude Code DEVE refinar com drivers fundamentais.

| Geracao | Horizonte | Alvo | Commodity | Spot ref | Baixo | Central | Alto | Vies |
|---|---|---|---|---|---|---|---|---|
| 2026-10-30 | 7d | 2026-11-06 | farelo_cbot | 329.20 | 301.11 | 315.91 | 330.71 | baixista |
| 2026-10-30 | 7d | 2026-11-06 | oleo_cbot | 65.81 | 62.88 | 64.96 | 67.04 | baixista |
| 2026-10-30 | 7d | 2026-11-06 | soja_cbot | 1234.00 | 1182.56 | 1206.22 | 1229.89 | baixista |
| 2026-10-30 | 30d | 2026-11-29 | farelo_cbot | 329.20 | 236.38 | 267.01 | 297.65 | baixista |
| 2026-10-30 | 30d | 2026-11-29 | oleo_cbot | 65.81 | 57.59 | 61.89 | 66.20 | baixista |
| 2026-10-30 | 30d | 2026-11-29 | soja_cbot | 1234.00 | 1057.00 | 1105.98 | 1154.96 | baixista |
| 2026-10-29 | 7d | 2026-11-05 | farelo_cbot | 329.20 | 307.87 | 322.53 | 337.19 | baixista |
| 2026-10-29 | 7d | 2026-11-05 | oleo_cbot | 65.69 | 62.24 | 64.35 | 66.45 | baixista |
| 2026-10-29 | 7d | 2026-11-05 | soja_cbot | 1234.50 | 1181.89 | 1206.01 | 1230.13 | baixista |
| 2026-10-29 | 30d | 2026-11-28 | farelo_cbot | 329.20 | 245.83 | 276.17 | 306.51 | baixista |
| 2026-10-29 | 30d | 2026-11-28 | oleo_cbot | 65.69 | 56.83 | 61.19 | 65.55 | baixista |
| 2026-10-29 | 30d | 2026-11-28 | soja_cbot | 1234.50 | 1054.57 | 1104.51 | 1154.45 | baixista |
| 2026-10-28 | 7d | 2026-11-04 | farelo_cbot | 335.70 | 307.31 | 322.36 | 337.41 | baixista |
| 2026-10-28 | 7d | 2026-11-04 | oleo_cbot | 65.56 | 63.90 | 65.83 | 67.76 | baixista |
| 2026-10-28 | 7d | 2026-11-04 | soja_cbot | 1238.00 | 1189.70 | 1215.31 | 1240.93 | baixista |
| 2026-10-28 | 30d | 2026-11-27 | farelo_cbot | 335.70 | 244.61 | 275.77 | 306.93 | baixista |
| 2026-10-28 | 30d | 2026-11-27 | oleo_cbot | 65.56 | 59.19 | 63.18 | 67.18 | baixista |
| 2026-10-28 | 30d | 2026-11-27 | soja_cbot | 1238.00 | 1062.53 | 1115.56 | 1168.59 | baixista |
| 2026-10-27 | 7d | 2026-11-03 | farelo_cbot | 334.60 | 312.51 | 327.77 | 343.03 | baixista |
| 2026-10-27 | 7d | 2026-11-03 | oleo_cbot | 66.71 | 64.24 | 66.22 | 68.21 | baixista |
| 2026-10-27 | 7d | 2026-11-03 | soja_cbot | 1243.00 | 1200.30 | 1225.88 | 1251.45 | baixista |
| 2026-10-27 | 30d | 2026-11-26 | farelo_cbot | 334.60 | 253.02 | 284.61 | 316.20 | baixista |
| 2026-10-27 | 30d | 2026-11-26 | oleo_cbot | 66.71 | 59.38 | 63.50 | 67.62 | baixista |
| 2026-10-27 | 30d | 2026-11-26 | soja_cbot | 1243.00 | 1076.76 | 1129.71 | 1182.67 | baixista |

---


---

# Fila de julgamento — 2026-10-30

**7 item(ns).** Frase-gatilho: "lê a fila de julgamento e trata"

## 🔴 [nivel_tese] soja_cbot fechou em 1234.00 — acima da resistencia 1180.00
- id: `alerta-quebra_resistencia-soja_cbot-2026-10-30`
- fato: soja_cbot = 1234.00 vs nivel 1180.00 (2026-10-30)
- refs: soja_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] oleo_cbot fechou em 65.81 — abaixo do suporte 72.00
- id: `alerta-quebra_suporte-oleo_cbot-2026-10-30`
- fato: oleo_cbot = 65.81 vs nivel 72.00 (2026-10-30)
- refs: oleo_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] usd_brl_ptax fechou em 5.37 — acima da resistencia 5.30
- id: `alerta-quebra_resistencia-usd_brl_ptax-2026-10-29`
- fato: usd_brl_ptax = 5.37 vs nivel 5.30 (2026-10-29)
- refs: usd_brl_ptax
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

## 🟡 [release] WASDE novo (2026-10-28)
- id: `release-usda_wasde-2026-10-28`
- fato: fonte usda_wasde com data 2026-10-28 — coletado, ainda nao interpretado
- refs: complexo_soja
- leitura: O numero muda o balanco/tese? Algo relevante pro farelo?

## 🟡 [release] NOPA novo (2026-10-30)
- id: `release-nopa-2026-10-30`
- fato: fonte nopa com data 2026-10-30 — coletado, ainda nao interpretado
- refs: complexo_soja
- leitura: O numero muda o balanco/tese? Algo relevante pro farelo?

---
Trate só 🔴/🟡. Saída = `insights/*.md` (formato de generate_insights.txt, com `vies:`). Cite o `id` da fila no corpo do insight. Máx 1-3. Não duplicar insight recente.
