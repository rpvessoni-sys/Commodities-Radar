# Briefing consolidado — 2026-10-28

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
- 2026-10-15 | eur_brl_ptax | valor: 5.6609 BRL/EUR (sgs=21619)
- 2026-10-15 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-10-15 | usd_brl_ptax | valor: 5.0521 BRL/USD (sgs=1)
- 2026-10-14 | eur_brl_ptax | valor: 5.6111 BRL/EUR (sgs=21619)
- 2026-10-14 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-10-14 | usd_brl_ptax | valor: 5.0441 BRL/USD (sgs=1)

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

- 2026-10-28 | farelo_cbot | abertura: 334.8999938964844 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-28 | farelo_cbot | fechamento: 335.3999938964844 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-28 | farelo_cbot | fechamento_F27: 334.6000061035156 USD/short_ton (ticker=ZMF27.CBT venc=jan/27)
- 2026-10-28 | farelo_cbot | fechamento_H27: 334.8999938964844 USD/short_ton (ticker=ZMH27.CBT venc=mar/27)
- 2026-10-28 | farelo_cbot | fechamento_K27: 337.8999938964844 USD/short_ton (ticker=ZMK27.CBT venc=mai/27)
- 2026-10-28 | farelo_cbot | fechamento_N27: 341.79998779296875 USD/short_ton (ticker=ZMN27.CBT venc=jul/27)
- 2026-10-28 | farelo_cbot | fechamento_Z26: 335.3999938964844 USD/short_ton (ticker=ZMZ26.CBT venc=dez/26)
- 2026-10-28 | farelo_cbot | maxima: 335.3999938964844 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-28 | farelo_cbot | minima: 334.5 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-28 | farelo_cbot | volume: 1298.0 contratos (ticker=ZMZ26.CBT)
- 2026-10-28 | heating_oil_cbot | abertura: 4.590700149536133 USD/galão (ticker=HO=F)
- 2026-10-28 | heating_oil_cbot | fechamento: 4.591300010681152 USD/galão (ticker=HO=F)
- 2026-10-28 | heating_oil_cbot | maxima: 4.598100185394287 USD/galão (ticker=HO=F)
- 2026-10-28 | heating_oil_cbot | minima: 4.57859992980957 USD/galão (ticker=HO=F)
- 2026-10-28 | heating_oil_cbot | volume: 403.0 contratos (ticker=HO=F)
- 2026-10-28 | oleo_cbot | abertura: 66.70999908447266 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-10-28 | oleo_cbot | fechamento: 66.55000305175781 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-10-28 | oleo_cbot | fechamento_F27: 66.77999877929688 USD_cts/lb (ticker=ZLF27.CBT venc=jan/27)
- 2026-10-28 | oleo_cbot | fechamento_H27: 67.0999984741211 USD_cts/lb (ticker=ZLH27.CBT venc=mar/27)
- 2026-10-28 | oleo_cbot | fechamento_K27: 67.43000030517578 USD_cts/lb (ticker=ZLK27.CBT venc=mai/27)
- 2026-10-28 | oleo_cbot | fechamento_N27: 67.4800033569336 USD_cts/lb (ticker=ZLN27.CBT venc=jul/27)
- 2026-10-28 | oleo_cbot | fechamento_Z26: 66.55000305175781 USD_cts/lb (ticker=ZLZ26.CBT venc=dez/26)
- 2026-10-28 | oleo_cbot | maxima: 66.73999786376953 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-10-28 | oleo_cbot | minima: 66.52999877929688 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-10-28 | oleo_cbot | volume: 775.0 contratos (ticker=ZLZ26.CBT)
- 2026-10-28 | soja_cbot | abertura: 1243.25 USD/bushel (ticker=ZSF27.CBT)
- 2026-10-28 | soja_cbot | fechamento: 1244.0 USD/bushel (ticker=ZSF27.CBT)
- 2026-10-28 | soja_cbot | fechamento_F27: 1244.0 USD/bushel (ticker=ZSF27.CBT venc=jan/27)
- 2026-10-28 | soja_cbot | fechamento_H27: 1252.75 USD/bushel (ticker=ZSH27.CBT venc=mar/27)
- 2026-10-28 | soja_cbot | fechamento_K27: 1261.25 USD/bushel (ticker=ZSK27.CBT venc=mai/27)
- 2026-10-28 | soja_cbot | fechamento_N27: 1267.75 USD/bushel (ticker=ZSN27.CBT venc=jul/27)
- 2026-10-28 | soja_cbot | fechamento_Q27: 1253.0 USD/bushel (ticker=ZSQ27.CBT venc=ago/27)
- 2026-10-28 | soja_cbot | fechamento_X26: 1231.25 USD/bushel (ticker=ZSX26.CBT venc=nov/26)
- 2026-10-28 | soja_cbot | maxima: 1245.75 USD/bushel (ticker=ZSF27.CBT)
- 2026-10-28 | soja_cbot | minima: 1242.25 USD/bushel (ticker=ZSF27.CBT)
- 2026-10-28 | soja_cbot | volume: 5318.0 contratos (ticker=ZSF27.CBT)
- 2026-10-27 | farelo_cbot | abertura: 334.8999938964844 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-27 | farelo_cbot | fechamento: 334.6000061035156 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-27 | farelo_cbot | fechamento_F27: 334.0 USD/short_ton (ticker=ZMF27.CBT venc=jan/27)
- 2026-10-27 | farelo_cbot | fechamento_H27: 334.6000061035156 USD/short_ton (ticker=ZMH27.CBT venc=mar/27)
- 2026-10-27 | farelo_cbot | fechamento_K27: 337.6000061035156 USD/short_ton (ticker=ZMK27.CBT venc=mai/27)
- 2026-10-27 | farelo_cbot | fechamento_N27: 341.5 USD/short_ton (ticker=ZMN27.CBT venc=jul/27)
- 2026-10-27 | farelo_cbot | fechamento_Z26: 334.6000061035156 USD/short_ton (ticker=ZMZ26.CBT venc=dez/26)
- 2026-10-27 | farelo_cbot | maxima: 335.3999938964844 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-27 | farelo_cbot | minima: 334.5 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-27 | farelo_cbot | volume: 1298.0 contratos (ticker=ZMZ26.CBT)
- 2026-10-27 | heating_oil_cbot | abertura: 4.590700149536133 USD/galão (ticker=HO=F)
- 2026-10-27 | heating_oil_cbot | fechamento: 4.587800025939941 USD/galão (ticker=HO=F)
- 2026-10-27 | heating_oil_cbot | maxima: 4.598100185394287 USD/galão (ticker=HO=F)
- 2026-10-27 | heating_oil_cbot | minima: 4.57859992980957 USD/galão (ticker=HO=F)

---

## indicators

- 2026-10-28 | biodiesel_us | custo_oleo_usd_galao: 4.9913 USD/galão (7.5 lb × óleo 66.55 cts/lb)
- 2026-10-28 | biodiesel_us | margem_usd_galao: 1.965 USD/galão (receita 7.76 (HO 4.59 + 1.5×RIN 2.11) − custo 5.79 (óleo 4.99 + ind 0.80))
- 2026-10-28 | biodiesel_us | receita_usd_galao: 7.7563 USD/galão (HO 4.59 + 1.5×RIN 2.11)
- 2026-10-28 | complexo_soja | crush_margin_usd_bu: 2.2593 USD/bushel (Board Crush: farelo 335.40 + oleo 66.55 − soja 1244.00)
- 2026-10-28 | complexo_soja | far_soj_ratio_pct: 80.88 % (farelo 335.40/sht ÷ (soja 1244.00cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-10-28 | complexo_soja | indice_sobra_farelo: 75.0 0-100 (sobra relevante (3/4 condições))
- 2026-10-28 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-10-28 | complexo_soja | oil_meal_spread_usd_bu: -0.0583 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-10-28 | complexo_soja | oil_share_pct: 49.8 % (valor oleo 7.32 / total 14.70)
- 2026-10-28 | soja_paridade_br | brl_saca_paridade: 146.3 BRL/saca60kg (CBOT 1244.00 cts × USD/BRL 5.3346 (sem basis))
- 2026-10-27 | biodiesel_us | custo_oleo_usd_galao: 4.9958 USD/galão (7.5 lb × óleo 66.61 cts/lb)
- 2026-10-27 | biodiesel_us | margem_usd_galao: 1.957 USD/galão (receita 7.75 (HO 4.59 + 1.5×RIN 2.11) − custo 5.80 (óleo 5.00 + ind 0.80))
- 2026-10-27 | biodiesel_us | receita_usd_galao: 7.7528 USD/galão (HO 4.59 + 1.5×RIN 2.11)
- 2026-10-27 | complexo_soja | crush_margin_usd_bu: 2.2558 USD/bushel (Board Crush: farelo 334.60 + oleo 66.61 − soja 1243.25)
- 2026-10-27 | complexo_soja | far_soj_ratio_pct: 80.74 % (farelo 334.60/sht ÷ (soja 1243.25cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-10-27 | complexo_soja | indice_sobra_farelo: 75.0 0-100 (sobra relevante (3/4 condições))
- 2026-10-27 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-10-27 | complexo_soja | oil_meal_spread_usd_bu: -0.0341 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-10-27 | complexo_soja | oil_share_pct: 49.88 % (valor oleo 7.33 / total 14.69)
- 2026-10-27 | soja_paridade_br | brl_saca_paridade: 146.21 BRL/saca60kg (CBOT 1243.25 cts × USD/BRL 5.3346 (sem basis))
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
- 2026-10-25 | complexo_soja | indice_sobra_farelo: 75.0 0-100 (sobra relevante (3/4 condições))
- 2026-10-25 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-10-24 | complexo_soja | indice_sobra_farelo: 75.0 0-100 (sobra relevante (3/4 condições))
- 2026-10-24 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-10-23 | biodiesel_us | custo_oleo_usd_galao: 5.0123 USD/galão (7.5 lb × óleo 66.83 cts/lb)
- 2026-10-23 | biodiesel_us | margem_usd_galao: 2.3369 USD/galão (receita 8.15 (HO 4.98 + 1.5×RIN 2.11) − custo 5.81 (óleo 5.01 + ind 0.80))
- 2026-10-23 | biodiesel_us | receita_usd_galao: 8.1492 USD/galão (HO 4.98 + 1.5×RIN 2.11)
- 2026-10-23 | complexo_soja | crush_margin_usd_bu: 2.2805 USD/bushel (Board Crush: farelo 346.10 + oleo 66.83 − soja 1268.50)
- 2026-10-23 | complexo_soja | far_soj_ratio_pct: 81.85 % (farelo 346.10/sht ÷ (soja 1268.50cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-10-23 | complexo_soja | indice_sobra_farelo: 50.0 0-100 (pressão moderada (1/2 condições))
- 2026-10-23 | complexo_soja | indice_suporte_oleo: 75.0 0-100 (suporte relevante (3/4 condições))
- 2026-10-23 | complexo_soja | oil_meal_spread_usd_bu: -0.2629 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-10-23 | complexo_soja | oil_share_pct: 49.12 % (valor oleo 7.35 / total 14.97)
- 2026-10-23 | soja_paridade_br | brl_saca_paridade: 140.88 BRL/saca60kg (CBOT 1268.50 cts × USD/BRL 5.0377 (sem basis))
- 2026-10-22 | biodiesel_us | custo_oleo_usd_galao: 5.0055 USD/galão (7.5 lb × óleo 66.74 cts/lb)
- 2026-10-22 | biodiesel_us | margem_usd_galao: 2.2916 USD/galão (receita 8.10 (HO 4.93 + 1.5×RIN 2.11) − custo 5.81 (óleo 5.01 + ind 0.80))
- 2026-10-22 | biodiesel_us | receita_usd_galao: 8.0971 USD/galão (HO 4.93 + 1.5×RIN 2.11)
- 2026-10-22 | complexo_soja | crush_margin_usd_bu: 2.3345 USD/bushel (Board Crush: farelo 347.30 + oleo 66.74 − soja 1264.75)
- 2026-10-22 | complexo_soja | far_soj_ratio_pct: 82.38 % (farelo 347.30/sht ÷ (soja 1264.75cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-10-22 | complexo_soja | oil_meal_spread_usd_bu: -0.2992 USD/bushel (Oleo - Farelo (positivo = oleo manda))

---

## inmet

- 2026-10-28 | cascavel_pr | temp_max_manha: 27.0 C (Cascavel/PR — Muitas nuvens)
- 2026-10-28 | cascavel_pr | temp_max_noite: 27.0 C (Cascavel/PR — Muitas nuvens)
- 2026-10-28 | cascavel_pr | temp_max_tarde: 27.0 C (Cascavel/PR — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-28 | cascavel_pr | temp_min_manha: 16.0 C (Cascavel/PR — Muitas nuvens)
- 2026-10-28 | cascavel_pr | temp_min_noite: 16.0 C (Cascavel/PR — Muitas nuvens)
- 2026-10-28 | cascavel_pr | temp_min_tarde: 16.0 C (Cascavel/PR — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-28 | cuiaba_mt | temp_max_manha: 34.0 C (Cuiaba/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-28 | cuiaba_mt | temp_max_noite: 34.0 C (Cuiaba/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-28 | cuiaba_mt | temp_max_tarde: 34.0 C (Cuiaba/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-28 | cuiaba_mt | temp_min_manha: 25.0 C (Cuiaba/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-28 | cuiaba_mt | temp_min_noite: 25.0 C (Cuiaba/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-28 | cuiaba_mt | temp_min_tarde: 25.0 C (Cuiaba/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-28 | lucas_rio_verde_mt | temp_max_manha: 34.0 C (Lucas do Rio Verde/MT — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-28 | lucas_rio_verde_mt | temp_max_noite: 34.0 C (Lucas do Rio Verde/MT — Muitas nuvens com pancadas de chuva)
- 2026-10-28 | lucas_rio_verde_mt | temp_max_tarde: 34.0 C (Lucas do Rio Verde/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-28 | lucas_rio_verde_mt | temp_min_manha: 23.0 C (Lucas do Rio Verde/MT — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-28 | lucas_rio_verde_mt | temp_min_noite: 23.0 C (Lucas do Rio Verde/MT — Muitas nuvens com pancadas de chuva)
- 2026-10-28 | lucas_rio_verde_mt | temp_min_tarde: 23.0 C (Lucas do Rio Verde/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-28 | maringa_pr | temp_max_manha: 28.0 C (Maringa/PR — Muitas nuvens)
- 2026-10-28 | maringa_pr | temp_max_noite: 28.0 C (Maringa/PR — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-28 | maringa_pr | temp_max_tarde: 28.0 C (Maringa/PR — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-28 | maringa_pr | temp_min_manha: 17.0 C (Maringa/PR — Muitas nuvens)
- 2026-10-28 | maringa_pr | temp_min_noite: 17.0 C (Maringa/PR — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-28 | maringa_pr | temp_min_tarde: 17.0 C (Maringa/PR — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-28 | passo_fundo_rs | temp_max_manha: 26.0 C (Passo Fundo/RS — Muitas nuvens)
- 2026-10-28 | passo_fundo_rs | temp_max_noite: 26.0 C (Passo Fundo/RS — Muitas nuvens)
- 2026-10-28 | passo_fundo_rs | temp_max_tarde: 26.0 C (Passo Fundo/RS — Muitas nuvens)
- 2026-10-28 | passo_fundo_rs | temp_min_manha: 13.0 C (Passo Fundo/RS — Muitas nuvens)
- 2026-10-28 | passo_fundo_rs | temp_min_noite: 13.0 C (Passo Fundo/RS — Muitas nuvens)
- 2026-10-28 | passo_fundo_rs | temp_min_tarde: 13.0 C (Passo Fundo/RS — Muitas nuvens)
- 2026-10-28 | rio_verde_go | temp_max_manha: 28.0 C (Rio Verde/GO — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-28 | rio_verde_go | temp_max_noite: 28.0 C (Rio Verde/GO — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-28 | rio_verde_go | temp_max_tarde: 28.0 C (Rio Verde/GO — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-28 | rio_verde_go | temp_min_manha: 21.0 C (Rio Verde/GO — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-28 | rio_verde_go | temp_min_noite: 21.0 C (Rio Verde/GO — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-28 | rio_verde_go | temp_min_tarde: 21.0 C (Rio Verde/GO — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-28 | sinop_mt | temp_max_manha: 34.0 C (Sinop/MT — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-28 | sinop_mt | temp_max_noite: 34.0 C (Sinop/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-28 | sinop_mt | temp_max_tarde: 34.0 C (Sinop/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-28 | sinop_mt | temp_min_manha: 24.0 C (Sinop/MT — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-28 | sinop_mt | temp_min_noite: 24.0 C (Sinop/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-28 | sinop_mt | temp_min_tarde: 24.0 C (Sinop/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-28 | sorriso_mt | temp_max_manha: 34.0 C (Sorriso/MT — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-28 | sorriso_mt | temp_max_noite: 34.0 C (Sorriso/MT — Muitas nuvens com pancadas de chuva)
- 2026-10-28 | sorriso_mt | temp_max_tarde: 34.0 C (Sorriso/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-28 | sorriso_mt | temp_min_manha: 24.0 C (Sorriso/MT — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-28 | sorriso_mt | temp_min_noite: 24.0 C (Sorriso/MT — Muitas nuvens com pancadas de chuva)
- 2026-10-28 | sorriso_mt | temp_min_tarde: 24.0 C (Sorriso/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-27 | cascavel_pr | temp_max_manha: 25.0 C (Cascavel/PR — Poucas nuvens)
- 2026-10-27 | cascavel_pr | temp_max_noite: 25.0 C (Cascavel/PR — Muitas nuvens)

---

## mpob

- 2026-10-28 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-27 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-26 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-25 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-24 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)

---

## noaa_cpc

- 2026-10-28 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-27 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-26 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-25 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-24 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)

---

## nopa

- 2026-10-28 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-27 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-26 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-25 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-24 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)

---

## noticias_rss

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
| 2026-10-28 | 7d | 2026-11-04 | farelo_cbot | 335.40 | 307.47 | 322.56 | 337.66 | baixista |
| 2026-10-28 | 7d | 2026-11-04 | oleo_cbot | 66.55 | 63.86 | 65.79 | 67.71 | baixista |
| 2026-10-28 | 7d | 2026-11-04 | soja_cbot | 1244.00 | 1190.28 | 1216.07 | 1241.86 | baixista |
| 2026-10-28 | 30d | 2026-11-27 | farelo_cbot | 335.40 | 244.78 | 276.03 | 307.28 | baixista |
| 2026-10-28 | 30d | 2026-11-27 | oleo_cbot | 66.55 | 59.15 | 63.13 | 67.12 | baixista |
| 2026-10-28 | 30d | 2026-11-27 | soja_cbot | 1244.00 | 1063.12 | 1116.52 | 1169.92 | baixista |
| 2026-10-27 | 7d | 2026-11-03 | farelo_cbot | 334.60 | 312.51 | 327.77 | 343.03 | baixista |
| 2026-10-27 | 7d | 2026-11-03 | oleo_cbot | 66.61 | 64.24 | 66.22 | 68.21 | baixista |
| 2026-10-27 | 7d | 2026-11-03 | soja_cbot | 1243.25 | 1200.30 | 1225.88 | 1251.45 | baixista |
| 2026-10-27 | 30d | 2026-11-26 | farelo_cbot | 334.60 | 253.02 | 284.61 | 316.20 | baixista |
| 2026-10-27 | 30d | 2026-11-26 | oleo_cbot | 66.61 | 59.38 | 63.50 | 67.62 | baixista |
| 2026-10-27 | 30d | 2026-11-26 | soja_cbot | 1243.25 | 1076.76 | 1129.71 | 1182.67 | baixista |
| 2026-10-26 | 7d | 2026-11-02 | farelo_cbot | 340.20 | 312.04 | 327.95 | 343.86 | baixista |
| 2026-10-26 | 7d | 2026-11-02 | oleo_cbot | 67.01 | 63.24 | 65.32 | 67.40 | baixista |
| 2026-10-26 | 7d | 2026-11-02 | soja_cbot | 1252.50 | 1195.08 | 1222.78 | 1250.48 | baixista |
| 2026-10-26 | 30d | 2026-11-25 | farelo_cbot | 340.20 | 253.06 | 286.00 | 318.95 | baixista |
| 2026-10-26 | 30d | 2026-11-25 | oleo_cbot | 67.01 | 57.47 | 61.77 | 66.07 | baixista |
| 2026-10-26 | 30d | 2026-11-25 | soja_cbot | 1252.50 | 1064.73 | 1122.07 | 1179.41 | baixista |
| 2026-10-25 | 7d | 2026-11-01 | farelo_cbot | 346.10 | 319.19 | 334.80 | 350.41 | baixista |
| 2026-10-25 | 7d | 2026-11-01 | oleo_cbot | 66.83 | 63.54 | 65.69 | 67.83 | baixista |
| 2026-10-25 | 7d | 2026-11-01 | soja_cbot | 1268.50 | 1213.36 | 1237.40 | 1261.44 | baixista |
| 2026-10-25 | 30d | 2026-11-24 | farelo_cbot | 346.10 | 262.67 | 294.99 | 327.30 | baixista |
| 2026-10-25 | 30d | 2026-11-24 | oleo_cbot | 66.83 | 57.38 | 61.82 | 66.26 | baixista |
| 2026-10-25 | 30d | 2026-11-24 | soja_cbot | 1268.50 | 1082.01 | 1131.77 | 1181.54 | baixista |

---


---

# Fila de julgamento — 2026-10-28

**10 item(ns).** Frase-gatilho: "lê a fila de julgamento e trata"

## 🔴 [nivel_tese] soja_cbot fechou em 1244.00 — acima da resistencia 1180.00
- id: `alerta-quebra_resistencia-soja_cbot-2026-10-28`
- fato: soja_cbot = 1244.00 vs nivel 1180.00 (2026-10-28)
- refs: soja_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] oleo_cbot fechou em 66.55 — abaixo do suporte 72.00
- id: `alerta-quebra_suporte-oleo_cbot-2026-10-28`
- fato: oleo_cbot = 66.55 vs nivel 72.00 (2026-10-28)
- refs: oleo_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] farelo_cbot fechou em 335.40 — acima da resistencia 325.00
- id: `alerta-quebra_resistencia-farelo_cbot-2026-10-28`
- fato: farelo_cbot = 335.40 vs nivel 325.00 (2026-10-28)
- refs: farelo_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] usd_brl_ptax fechou em 5.33 — acima da resistencia 5.30
- id: `alerta-quebra_resistencia-usd_brl_ptax-2026-10-27`
- fato: usd_brl_ptax = 5.33 vs nivel 5.30 (2026-10-27)
- refs: usd_brl_ptax
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] usd_brl_ptax variou -3.02% no dia (de 5.50 para 5.33)
- id: `alerta-movimento_forte-usd_brl_ptax-2026-10-27`
- fato: usd_brl_ptax = 5.33 vs nivel 5.50 (2026-10-27)
- refs: usd_brl_ptax
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] complexo_soja fechou em 2.26 — abaixo do suporte 2.50
- id: `alerta-quebra_suporte-complexo_soja-2026-10-28`
- fato: complexo_soja = 2.26 vs nivel 2.50 (2026-10-28)
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

## 🟡 [release] WASDE novo (2026-10-28)
- id: `release-usda_wasde-2026-10-28`
- fato: fonte usda_wasde com data 2026-10-28 — coletado, ainda nao interpretado
- refs: complexo_soja
- leitura: O numero muda o balanco/tese? Algo relevante pro farelo?

## 🟡 [release] NOPA novo (2026-10-28)
- id: `release-nopa-2026-10-28`
- fato: fonte nopa com data 2026-10-28 — coletado, ainda nao interpretado
- refs: complexo_soja
- leitura: O numero muda o balanco/tese? Algo relevante pro farelo?

---
Trate só 🔴/🟡. Saída = `insights/*.md` (formato de generate_insights.txt, com `vies:`). Cite o `id` da fila no corpo do insight. Máx 1-3. Não duplicar insight recente.
