# Briefing consolidado — 2026-11-11

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
- 2026-10-30 | eur_brl_ptax | valor: 6.0522 BRL/EUR (sgs=21619)
- 2026-10-30 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-10-30 | usd_brl_ptax | valor: 5.4212 BRL/USD (sgs=1)
- 2026-10-29 | eur_brl_ptax | valor: 6.0 BRL/EUR (sgs=21619)
- 2026-10-29 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-10-29 | usd_brl_ptax | valor: 5.3744 BRL/USD (sgs=1)
- 2026-10-28 | eur_brl_ptax | valor: 5.9515 BRL/EUR (sgs=21619)
- 2026-10-28 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-10-28 | usd_brl_ptax | valor: 5.342 BRL/USD (sgs=1)

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

- 2026-11-11 | heating_oil_cbot | abertura: 4.184000015258789 USD/galão (ticker=HO=F)
- 2026-11-11 | heating_oil_cbot | fechamento: 4.148600101470947 USD/galão (ticker=HO=F)
- 2026-11-11 | heating_oil_cbot | maxima: 4.148600101470947 USD/galão (ticker=HO=F)
- 2026-11-11 | heating_oil_cbot | minima: 4.133699893951416 USD/galão (ticker=HO=F)
- 2026-11-11 | heating_oil_cbot | volume: 142.0 contratos (ticker=HO=F)
- 2026-11-10 | farelo_cbot | abertura: 321.0 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-10 | farelo_cbot | fechamento: 326.5 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-10 | farelo_cbot | fechamento_F27: 326.29998779296875 USD/short_ton (ticker=ZMF27.CBT venc=jan/27)
- 2026-11-10 | farelo_cbot | fechamento_H27: 328.1000061035156 USD/short_ton (ticker=ZMH27.CBT venc=mar/27)
- 2026-11-10 | farelo_cbot | fechamento_K27: 331.29998779296875 USD/short_ton (ticker=ZMK27.CBT venc=mai/27)
- 2026-11-10 | farelo_cbot | fechamento_N27: 335.20001220703125 USD/short_ton (ticker=ZMN27.CBT venc=jul/27)
- 2026-11-10 | farelo_cbot | fechamento_Q27: 334.20001220703125 USD/short_ton (ticker=ZMQ27.CBT venc=ago/27)
- 2026-11-10 | farelo_cbot | fechamento_Z26: 326.5 USD/short_ton (ticker=ZMZ26.CBT venc=dez/26)
- 2026-11-10 | farelo_cbot | maxima: 328.29998779296875 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-10 | farelo_cbot | minima: 319.1000061035156 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-10 | farelo_cbot | volume: 104569.0 contratos (ticker=ZMZ26.CBT)
- 2026-11-10 | heating_oil_cbot | abertura: 4.184000015258789 USD/galão (ticker=HO=F)
- 2026-11-10 | heating_oil_cbot | fechamento: 4.142899990081787 USD/galão (ticker=HO=F)
- 2026-11-10 | heating_oil_cbot | maxima: 4.148600101470947 USD/galão (ticker=HO=F)
- 2026-11-10 | heating_oil_cbot | minima: 4.133699893951416 USD/galão (ticker=HO=F)
- 2026-11-10 | heating_oil_cbot | volume: 142.0 contratos (ticker=HO=F)
- 2026-11-10 | oleo_cbot | abertura: 61.9900016784668 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-11-10 | oleo_cbot | fechamento: 62.709999084472656 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-11-10 | oleo_cbot | fechamento_F27: 62.900001525878906 USD_cts/lb (ticker=ZLF27.CBT venc=jan/27)
- 2026-11-10 | oleo_cbot | fechamento_H27: 63.380001068115234 USD_cts/lb (ticker=ZLH27.CBT venc=mar/27)
- 2026-11-10 | oleo_cbot | fechamento_K27: 63.88999938964844 USD_cts/lb (ticker=ZLK27.CBT venc=mai/27)
- 2026-11-10 | oleo_cbot | fechamento_N27: 64.16000366210938 USD_cts/lb (ticker=ZLN27.CBT venc=jul/27)
- 2026-11-10 | oleo_cbot | fechamento_Q27: 64.01000213623047 USD_cts/lb (ticker=ZLQ27.CBT venc=ago/27)
- 2026-11-10 | oleo_cbot | fechamento_Z26: 62.709999084472656 USD_cts/lb (ticker=ZLZ26.CBT venc=dez/26)
- 2026-11-10 | oleo_cbot | maxima: 62.95000076293945 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-11-10 | oleo_cbot | minima: 61.5 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-11-10 | oleo_cbot | volume: 77403.0 contratos (ticker=ZLZ26.CBT)
- 2026-11-10 | soja_cbot | abertura: 1188.0 USD/bushel (ticker=ZSF27.CBT)
- 2026-11-10 | soja_cbot | fechamento: 1226.75 USD/bushel (ticker=ZSF27.CBT)
- 2026-11-10 | soja_cbot | fechamento_F27: 1226.75 USD/bushel (ticker=ZSF27.CBT venc=jan/27)
- 2026-11-10 | soja_cbot | fechamento_H27: 1233.0 USD/bushel (ticker=ZSH27.CBT venc=mar/27)
- 2026-11-10 | soja_cbot | fechamento_K27: 1241.75 USD/bushel (ticker=ZSK27.CBT venc=mai/27)
- 2026-11-10 | soja_cbot | fechamento_N27: 1246.5 USD/bushel (ticker=ZSN27.CBT venc=jul/27)
- 2026-11-10 | soja_cbot | fechamento_Q27: 1230.75 USD/bushel (ticker=ZSQ27.CBT venc=ago/27)
- 2026-11-10 | soja_cbot | fechamento_X26: 1225.75 USD/bushel (ticker=ZSX26.CBT venc=nov/26)
- 2026-11-10 | soja_cbot | maxima: 1230.75 USD/bushel (ticker=ZSF27.CBT)
- 2026-11-10 | soja_cbot | minima: 1185.0 USD/bushel (ticker=ZSF27.CBT)
- 2026-11-10 | soja_cbot | volume: 223706.0 contratos (ticker=ZSF27.CBT)
- 2026-11-09 | farelo_cbot | abertura: 319.29998779296875 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-09 | farelo_cbot | fechamento: 320.70001220703125 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-09 | farelo_cbot | fechamento_F27: 320.8999938964844 USD/short_ton (ticker=ZMF27.CBT venc=jan/27)
- 2026-11-09 | farelo_cbot | fechamento_H27: 321.79998779296875 USD/short_ton (ticker=ZMH27.CBT venc=mar/27)
- 2026-11-09 | farelo_cbot | fechamento_K27: 324.6000061035156 USD/short_ton (ticker=ZMK27.CBT venc=mai/27)
- 2026-11-09 | farelo_cbot | fechamento_N27: 328.29998779296875 USD/short_ton (ticker=ZMN27.CBT venc=jul/27)
- 2026-11-09 | farelo_cbot | fechamento_Q27: 328.1000061035156 USD/short_ton (ticker=ZMQ27.CBT venc=ago/27)

---

## indicators

- 2026-11-11 | complexo_soja | indice_sobra_farelo: 25.0 0-100 (sem sobra relevante (1/4 condições))
- 2026-11-11 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-11-10 | biodiesel_us | custo_oleo_usd_galao: 4.7032 USD/galão (7.5 lb × óleo 62.71 cts/lb)
- 2026-11-10 | biodiesel_us | margem_usd_galao: 1.8047 USD/galão (receita 7.31 (HO 4.14 + 1.5×RIN 2.11) − custo 5.50 (óleo 4.70 + ind 0.80))
- 2026-11-10 | biodiesel_us | receita_usd_galao: 7.3079 USD/galão (HO 4.14 + 1.5×RIN 2.11)
- 2026-11-10 | complexo_soja | crush_margin_usd_bu: 1.8136 USD/bushel (Board Crush: farelo 326.50 + oleo 62.71 − soja 1226.75)
- 2026-11-10 | complexo_soja | far_soj_ratio_pct: 79.85 % (farelo 326.50/sht ÷ (soja 1226.75cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-11-10 | complexo_soja | indice_sobra_farelo: 25.0 0-100 (sem sobra relevante (1/4 condições))
- 2026-11-10 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-11-10 | complexo_soja | oil_meal_spread_usd_bu: -0.2849 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-11-10 | complexo_soja | oil_share_pct: 48.99 % (valor oleo 6.90 / total 14.08)
- 2026-11-10 | soja_paridade_br | brl_saca_paridade: 151.02 BRL/saca60kg (CBOT 1226.75 cts × USD/BRL 5.5840 (sem basis))
- 2026-11-09 | biodiesel_us | custo_oleo_usd_galao: 4.6522 USD/galão (7.5 lb × óleo 62.03 cts/lb)
- 2026-11-09 | biodiesel_us | margem_usd_galao: 1.9275 USD/galão (receita 7.38 (HO 4.21 + 1.5×RIN 2.11) − custo 5.45 (óleo 4.65 + ind 0.80))
- 2026-11-09 | biodiesel_us | receita_usd_galao: 7.3798 USD/galão (HO 4.21 + 1.5×RIN 2.11)
- 2026-11-09 | complexo_soja | crush_margin_usd_bu: 1.9962 USD/bushel (Board Crush: farelo 320.70 + oleo 62.03 − soja 1188.25)
- 2026-11-09 | complexo_soja | far_soj_ratio_pct: 80.97 % (farelo 320.70/sht ÷ (soja 1188.25cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-11-09 | complexo_soja | indice_sobra_farelo: 25.0 0-100 (sem sobra relevante (1/4 condições))
- 2026-11-09 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-11-09 | complexo_soja | oil_meal_spread_usd_bu: -0.2321 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-11-09 | complexo_soja | oil_share_pct: 49.16 % (valor oleo 6.82 / total 13.88)
- 2026-11-09 | soja_paridade_br | brl_saca_paridade: 144.46 BRL/saca60kg (CBOT 1188.25 cts × USD/BRL 5.5146 (sem basis))
- 2026-11-08 | complexo_soja | indice_sobra_farelo: 25.0 0-100 (sem sobra relevante (1/4 condições))
- 2026-11-08 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-11-07 | complexo_soja | indice_sobra_farelo: 25.0 0-100 (sem sobra relevante (1/4 condições))
- 2026-11-07 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-11-06 | biodiesel_us | custo_oleo_usd_galao: 4.6695 USD/galão (7.5 lb × óleo 62.26 cts/lb)
- 2026-11-06 | biodiesel_us | margem_usd_galao: 2.0272 USD/galão (receita 7.50 (HO 4.33 + 1.5×RIN 2.11) − custo 5.47 (óleo 4.67 + ind 0.80))
- 2026-11-06 | biodiesel_us | receita_usd_galao: 7.4967 USD/galão (HO 4.33 + 1.5×RIN 2.11)
- 2026-11-06 | complexo_soja | crush_margin_usd_bu: 1.9335 USD/bushel (Board Crush: farelo 319.20 + oleo 62.26 − soja 1193.75)
- 2026-11-06 | complexo_soja | far_soj_ratio_pct: 80.22 % (farelo 319.20/sht ÷ (soja 1193.75cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-11-06 | complexo_soja | indice_sobra_farelo: 25.0 0-100 (sem sobra relevante (1/4 condições))
- 2026-11-06 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-11-06 | complexo_soja | oil_meal_spread_usd_bu: -0.1738 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-11-06 | complexo_soja | oil_share_pct: 49.37 % (valor oleo 6.85 / total 13.87)
- 2026-11-06 | soja_paridade_br | brl_saca_paridade: 144.78 BRL/saca60kg (CBOT 1193.75 cts × USD/BRL 5.5013 (sem basis))
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

---

## inmet

- 2026-11-11 | cascavel_pr | temp_max_manha: 28.0 C (Cascavel/PR — Poucas nuvens)
- 2026-11-11 | cascavel_pr | temp_max_noite: 28.0 C (Cascavel/PR — Muitas nuvens)
- 2026-11-11 | cascavel_pr | temp_max_tarde: 28.0 C (Cascavel/PR — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-11 | cascavel_pr | temp_min_manha: 13.0 C (Cascavel/PR — Poucas nuvens)
- 2026-11-11 | cascavel_pr | temp_min_noite: 13.0 C (Cascavel/PR — Muitas nuvens)
- 2026-11-11 | cascavel_pr | temp_min_tarde: 13.0 C (Cascavel/PR — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-11 | cuiaba_mt | temp_max_manha: 36.0 C (Cuiaba/MT — Muitas nuvens)
- 2026-11-11 | cuiaba_mt | temp_max_noite: 36.0 C (Cuiaba/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-11 | cuiaba_mt | temp_max_tarde: 36.0 C (Cuiaba/MT — Nublado com pancadas de chuva e trovoadas)
- 2026-11-11 | cuiaba_mt | temp_min_manha: 25.0 C (Cuiaba/MT — Muitas nuvens)
- 2026-11-11 | cuiaba_mt | temp_min_noite: 25.0 C (Cuiaba/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-11 | cuiaba_mt | temp_min_tarde: 25.0 C (Cuiaba/MT — Nublado com pancadas de chuva e trovoadas)
- 2026-11-11 | lucas_rio_verde_mt | temp_max_manha: 36.0 C (Lucas do Rio Verde/MT — Muitas nuvens)
- 2026-11-11 | lucas_rio_verde_mt | temp_max_noite: 36.0 C (Lucas do Rio Verde/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-11 | lucas_rio_verde_mt | temp_max_tarde: 36.0 C (Lucas do Rio Verde/MT — Muitas nuvens com pancadas de chuva e trovoadas)
- 2026-11-11 | lucas_rio_verde_mt | temp_min_manha: 24.0 C (Lucas do Rio Verde/MT — Muitas nuvens)
- 2026-11-11 | lucas_rio_verde_mt | temp_min_noite: 24.0 C (Lucas do Rio Verde/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-11 | lucas_rio_verde_mt | temp_min_tarde: 24.0 C (Lucas do Rio Verde/MT — Muitas nuvens com pancadas de chuva e trovoadas)
- 2026-11-11 | maringa_pr | temp_max_manha: 28.0 C (Maringa/PR — Muitas nuvens)
- 2026-11-11 | maringa_pr | temp_max_noite: 28.0 C (Maringa/PR — Muitas nuvens)
- 2026-11-11 | maringa_pr | temp_max_tarde: 28.0 C (Maringa/PR — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-11 | maringa_pr | temp_min_manha: 16.0 C (Maringa/PR — Muitas nuvens)
- 2026-11-11 | maringa_pr | temp_min_noite: 16.0 C (Maringa/PR — Muitas nuvens)
- 2026-11-11 | maringa_pr | temp_min_tarde: 16.0 C (Maringa/PR — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-11 | passo_fundo_rs | temp_max_manha: 24.0 C (Passo Fundo/RS — Poucas nuvens)
- 2026-11-11 | passo_fundo_rs | temp_max_noite: 24.0 C (Passo Fundo/RS — Muitas nuvens)
- 2026-11-11 | passo_fundo_rs | temp_max_tarde: 24.0 C (Passo Fundo/RS — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-11 | passo_fundo_rs | temp_min_manha: 12.0 C (Passo Fundo/RS — Poucas nuvens)
- 2026-11-11 | passo_fundo_rs | temp_min_noite: 12.0 C (Passo Fundo/RS — Muitas nuvens)
- 2026-11-11 | passo_fundo_rs | temp_min_tarde: 12.0 C (Passo Fundo/RS — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-11 | rio_verde_go | temp_max_manha: 27.0 C (Rio Verde/GO — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-11 | rio_verde_go | temp_max_noite: 27.0 C (Rio Verde/GO — Muitas nuvens com pancadas de chuva e trovoadas)
- 2026-11-11 | rio_verde_go | temp_max_tarde: 27.0 C (Rio Verde/GO — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-11 | rio_verde_go | temp_min_manha: 20.0 C (Rio Verde/GO — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-11 | rio_verde_go | temp_min_noite: 20.0 C (Rio Verde/GO — Muitas nuvens com pancadas de chuva e trovoadas)
- 2026-11-11 | rio_verde_go | temp_min_tarde: 20.0 C (Rio Verde/GO — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-11 | sinop_mt | temp_max_manha: 36.0 C (Sinop/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-11 | sinop_mt | temp_max_noite: 36.0 C (Sinop/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-11 | sinop_mt | temp_max_tarde: 36.0 C (Sinop/MT — Muitas nuvens com pancadas de chuva e trovoadas)
- 2026-11-11 | sinop_mt | temp_min_manha: 23.0 C (Sinop/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-11 | sinop_mt | temp_min_noite: 23.0 C (Sinop/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-11 | sinop_mt | temp_min_tarde: 23.0 C (Sinop/MT — Muitas nuvens com pancadas de chuva e trovoadas)
- 2026-11-11 | sorriso_mt | temp_max_manha: 36.0 C (Sorriso/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-11 | sorriso_mt | temp_max_noite: 36.0 C (Sorriso/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-11 | sorriso_mt | temp_max_tarde: 36.0 C (Sorriso/MT — Muitas nuvens com pancadas de chuva e trovoadas)
- 2026-11-11 | sorriso_mt | temp_min_manha: 23.0 C (Sorriso/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-11 | sorriso_mt | temp_min_noite: 23.0 C (Sorriso/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-11 | sorriso_mt | temp_min_tarde: 23.0 C (Sorriso/MT — Muitas nuvens com pancadas de chuva e trovoadas)
- 2026-11-10 | cascavel_pr | temp_max_manha: 27.0 C (Cascavel/PR — Poucas nuvens)
- 2026-11-10 | cascavel_pr | temp_max_noite: 27.0 C (Cascavel/PR — Poucas nuvens)

---

## mpob

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
- 2026-10-30 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-29 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-28 | palma_malasia | page_fetched: 3202.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)

---

## noaa_cpc

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
- 2026-10-30 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-29 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-28 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)

---

## nopa

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
- 2026-10-30 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-29 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-28 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)

---

## noticias_rss

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
- 2026-10-30 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-10-29 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-10-28 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))

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
| 2026-11-11 | 7d | 2026-11-18 | farelo_cbot | 326.50 | 295.69 | 310.46 | 325.24 | baixista |
| 2026-11-11 | 7d | 2026-11-18 | oleo_cbot | 62.71 | 58.78 | 61.27 | 63.76 | baixista |
| 2026-11-11 | 7d | 2026-11-18 | soja_cbot | 1226.75 | 1148.97 | 1193.95 | 1238.93 | baixista |
| 2026-11-11 | 30d | 2026-12-11 | farelo_cbot | 326.50 | 224.68 | 255.26 | 285.84 | baixista |
| 2026-11-11 | 30d | 2026-12-11 | oleo_cbot | 62.71 | 50.70 | 55.86 | 61.02 | baixista |
| 2026-11-11 | 30d | 2026-12-11 | soja_cbot | 1226.75 | 989.74 | 1082.85 | 1175.96 | baixista |
| 2026-11-10 | 7d | 2026-11-17 | farelo_cbot | 326.50 | 293.60 | 307.29 | 320.98 | baixista |
| 2026-11-10 | 7d | 2026-11-17 | oleo_cbot | 62.71 | 57.97 | 60.30 | 62.63 | baixista |
| 2026-11-10 | 7d | 2026-11-17 | soja_cbot | 1226.75 | 1133.20 | 1158.94 | 1184.68 | baixista |
| 2026-11-10 | 30d | 2026-12-10 | farelo_cbot | 326.50 | 223.69 | 252.02 | 280.35 | baixista |
| 2026-11-10 | 30d | 2026-12-10 | oleo_cbot | 62.71 | 50.05 | 54.87 | 59.69 | baixista |
| 2026-11-10 | 30d | 2026-12-10 | soja_cbot | 1226.75 | 993.80 | 1047.09 | 1100.38 | baixista |
| 2026-11-09 | 7d | 2026-11-16 | farelo_cbot | 320.70 | 291.31 | 304.91 | 318.51 | baixista |
| 2026-11-09 | 7d | 2026-11-16 | oleo_cbot | 62.03 | 58.74 | 61.19 | 63.63 | baixista |
| 2026-11-09 | 7d | 2026-11-16 | soja_cbot | 1188.25 | 1140.55 | 1167.88 | 1195.22 | baixista |
| 2026-11-09 | 30d | 2026-12-09 | farelo_cbot | 320.70 | 218.92 | 247.09 | 275.25 | baixista |
| 2026-11-09 | 30d | 2026-12-09 | oleo_cbot | 62.03 | 51.16 | 56.22 | 61.27 | baixista |
| 2026-11-09 | 30d | 2026-12-09 | soja_cbot | 1188.25 | 999.26 | 1055.85 | 1112.43 | baixista |
| 2026-11-08 | 7d | 2026-11-15 | farelo_cbot | 319.20 | 289.07 | 302.55 | 316.02 | baixista |
| 2026-11-08 | 7d | 2026-11-15 | oleo_cbot | 62.26 | 58.68 | 61.15 | 63.61 | baixista |
| 2026-11-08 | 7d | 2026-11-15 | soja_cbot | 1193.75 | 1137.32 | 1163.90 | 1190.48 | baixista |
| 2026-11-08 | 30d | 2026-12-08 | farelo_cbot | 319.20 | 214.55 | 242.43 | 270.32 | baixista |
| 2026-11-08 | 30d | 2026-12-08 | oleo_cbot | 62.26 | 51.46 | 56.56 | 61.66 | baixista |
| 2026-11-08 | 30d | 2026-12-08 | soja_cbot | 1193.75 | 996.85 | 1051.88 | 1106.91 | baixista |

---


---

# Fila de julgamento — 2026-11-11

**11 item(ns).** Frase-gatilho: "lê a fila de julgamento e trata"

## 🔴 [ratio_zona] Ratio Far/Soj entrou na zona 'comprimido' (79.8%, era 'neutro' 81.0%)
- id: `ratio-zona-2026-11-10`
- fato: far_soj_ratio_pct 81.0% -> 79.8% em 2026-11-10 (indicators/DB)
- refs: farelo
- leitura: Muda a leitura do spread Far/Soj (mean-reversion, os dois lados)?

## 🔴 [nivel_tese] soja_cbot fechou em 1226.75 — acima da resistencia 1180.00
- id: `alerta-quebra_resistencia-soja_cbot-2026-11-10`
- fato: soja_cbot = 1226.75 vs nivel 1180.00 (2026-11-10)
- refs: soja_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] soja_cbot variou +3.24% no dia (de 1188.25 para 1226.75)
- id: `alerta-movimento_forte-soja_cbot-2026-11-10`
- fato: soja_cbot = 1226.75 vs nivel 1188.25 (2026-11-10)
- refs: soja_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] oleo_cbot fechou em 62.71 — abaixo do suporte 72.00
- id: `alerta-quebra_suporte-oleo_cbot-2026-11-10`
- fato: oleo_cbot = 62.71 vs nivel 72.00 (2026-11-10)
- refs: oleo_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] farelo_cbot fechou em 326.50 — acima da resistencia 325.00
- id: `alerta-quebra_resistencia-farelo_cbot-2026-11-10`
- fato: farelo_cbot = 326.50 vs nivel 325.00 (2026-11-10)
- refs: farelo_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] usd_brl_ptax fechou em 5.58 — acima da resistencia 5.30
- id: `alerta-quebra_resistencia-usd_brl_ptax-2026-11-10`
- fato: usd_brl_ptax = 5.58 vs nivel 5.30 (2026-11-10)
- refs: usd_brl_ptax
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] complexo_soja fechou em 1.81 — abaixo do suporte 2.50
- id: `alerta-quebra_suporte-complexo_soja-2026-11-10`
- fato: complexo_soja = 1.81 vs nivel 2.50 (2026-11-10)
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

## 🟡 [release] WASDE novo (2026-11-10)
- id: `release-usda_wasde-2026-11-10`
- fato: fonte usda_wasde com data 2026-11-10 — coletado, ainda nao interpretado
- refs: complexo_soja
- leitura: O numero muda o balanco/tese? Algo relevante pro farelo?

## 🟡 [release] NOPA novo (2026-11-11)
- id: `release-nopa-2026-11-11`
- fato: fonte nopa com data 2026-11-11 — coletado, ainda nao interpretado
- refs: complexo_soja
- leitura: O numero muda o balanco/tese? Algo relevante pro farelo?

---
Trate só 🔴/🟡. Saída = `insights/*.md` (formato de generate_insights.txt, com `vies:`). Cite o `id` da fila no corpo do insight. Máx 1-3. Não duplicar insight recente.
