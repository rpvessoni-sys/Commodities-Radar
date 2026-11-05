# Briefing consolidado — 2026-11-05

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
- 2026-10-23 | eur_brl_ptax | valor: 5.6422 BRL/EUR (sgs=21619)
- 2026-10-23 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-10-23 | usd_brl_ptax | valor: 5.0377 BRL/USD (sgs=1)
- 2026-10-22 | eur_brl_ptax | valor: 5.6494 BRL/EUR (sgs=21619)
- 2026-10-22 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-10-22 | usd_brl_ptax | valor: 5.0383 BRL/USD (sgs=1)

---

## cftc_cot

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

- 2026-11-05 | farelo_cbot | abertura: 318.6000061035156 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-05 | farelo_cbot | fechamento: 319.70001220703125 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-05 | farelo_cbot | fechamento_F27: 319.6000061035156 USD/short_ton (ticker=ZMF27.CBT venc=jan/27)
- 2026-11-05 | farelo_cbot | fechamento_H27: 320.20001220703125 USD/short_ton (ticker=ZMH27.CBT venc=mar/27)
- 2026-11-05 | farelo_cbot | fechamento_K27: 322.8999938964844 USD/short_ton (ticker=ZMK27.CBT venc=mai/27)
- 2026-11-05 | farelo_cbot | fechamento_N27: 327.1000061035156 USD/short_ton (ticker=ZMN27.CBT venc=jul/27)
- 2026-11-05 | farelo_cbot | fechamento_Q27: 327.0 USD/short_ton (ticker=ZMQ27.CBT venc=ago/27)
- 2026-11-05 | farelo_cbot | fechamento_Z26: 319.70001220703125 USD/short_ton (ticker=ZMZ26.CBT venc=dez/26)
- 2026-11-05 | farelo_cbot | maxima: 320.3999938964844 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-05 | farelo_cbot | minima: 318.5 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-05 | farelo_cbot | volume: 1581.0 contratos (ticker=ZMZ26.CBT)
- 2026-11-05 | heating_oil_cbot | abertura: 4.20550012588501 USD/galão (ticker=HO=F)
- 2026-11-05 | heating_oil_cbot | fechamento: 4.173099994659424 USD/galão (ticker=HO=F)
- 2026-11-05 | heating_oil_cbot | maxima: 4.212100028991699 USD/galão (ticker=HO=F)
- 2026-11-05 | heating_oil_cbot | minima: 4.17140007019043 USD/galão (ticker=HO=F)
- 2026-11-05 | heating_oil_cbot | volume: 776.0 contratos (ticker=HO=F)
- 2026-11-05 | oleo_cbot | abertura: 63.599998474121094 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-11-05 | oleo_cbot | fechamento: 63.15999984741211 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-11-05 | oleo_cbot | fechamento_F27: 63.38999938964844 USD_cts/lb (ticker=ZLF27.CBT venc=jan/27)
- 2026-11-05 | oleo_cbot | fechamento_H27: 63.900001525878906 USD_cts/lb (ticker=ZLH27.CBT venc=mar/27)
- 2026-11-05 | oleo_cbot | fechamento_K27: 64.30000305175781 USD_cts/lb (ticker=ZLK27.CBT venc=mai/27)
- 2026-11-05 | oleo_cbot | fechamento_N27: 64.51000213623047 USD_cts/lb (ticker=ZLN27.CBT venc=jul/27)
- 2026-11-05 | oleo_cbot | fechamento_Q27: 64.31999969482422 USD_cts/lb (ticker=ZLQ27.CBT venc=ago/27)
- 2026-11-05 | oleo_cbot | fechamento_Z26: 63.150001525878906 USD_cts/lb (ticker=ZLZ26.CBT venc=dez/26)
- 2026-11-05 | oleo_cbot | maxima: 63.709999084472656 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-11-05 | oleo_cbot | minima: 63.08000183105469 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-11-05 | oleo_cbot | volume: 3547.0 contratos (ticker=ZLZ26.CBT)
- 2026-11-05 | soja_cbot | abertura: 1202.25 USD/bushel (ticker=ZSF27.CBT)
- 2026-11-05 | soja_cbot | fechamento: 1203.0 USD/bushel (ticker=ZSF27.CBT)
- 2026-11-05 | soja_cbot | fechamento_F27: 1202.75 USD/bushel (ticker=ZSF27.CBT venc=jan/27)
- 2026-11-05 | soja_cbot | fechamento_H27: 1210.75 USD/bushel (ticker=ZSH27.CBT venc=mar/27)
- 2026-11-05 | soja_cbot | fechamento_K27: 1220.0 USD/bushel (ticker=ZSK27.CBT venc=mai/27)
- 2026-11-05 | soja_cbot | fechamento_N27: 1227.0 USD/bushel (ticker=ZSN27.CBT venc=jul/27)
- 2026-11-05 | soja_cbot | fechamento_Q27: 1214.5 USD/bushel (ticker=ZSQ27.CBT venc=ago/27)
- 2026-11-05 | soja_cbot | fechamento_X26: 1198.0 USD/bushel (ticker=ZSX26.CBT venc=nov/26)
- 2026-11-05 | soja_cbot | maxima: 1206.75 USD/bushel (ticker=ZSF27.CBT)
- 2026-11-05 | soja_cbot | minima: 1202.25 USD/bushel (ticker=ZSF27.CBT)
- 2026-11-05 | soja_cbot | volume: 3686.0 contratos (ticker=ZSF27.CBT)
- 2026-11-04 | farelo_cbot | abertura: 317.5 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-04 | farelo_cbot | fechamento: 318.6000061035156 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-04 | farelo_cbot | fechamento_F27: 319.6000061035156 USD/short_ton (ticker=ZMF27.CBT venc=jan/27)
- 2026-11-04 | farelo_cbot | fechamento_H27: 320.29998779296875 USD/short_ton (ticker=ZMH27.CBT venc=mar/27)
- 2026-11-04 | farelo_cbot | fechamento_K27: 322.8999938964844 USD/short_ton (ticker=ZMK27.CBT venc=mai/27)
- 2026-11-04 | farelo_cbot | fechamento_N27: 327.20001220703125 USD/short_ton (ticker=ZMN27.CBT venc=jul/27)
- 2026-11-04 | farelo_cbot | fechamento_Q27: 327.3999938964844 USD/short_ton (ticker=ZMQ27.CBT venc=ago/27)
- 2026-11-04 | farelo_cbot | fechamento_Z26: 319.8999938964844 USD/short_ton (ticker=ZMZ26.CBT venc=dez/26)
- 2026-11-04 | farelo_cbot | maxima: 320.6000061035156 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-04 | farelo_cbot | minima: 315.20001220703125 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-04 | farelo_cbot | volume: 93494.0 contratos (ticker=ZMZ26.CBT)
- 2026-11-04 | heating_oil_cbot | abertura: 4.570000171661377 USD/galão (ticker=HO=F)

---

## indicators

- 2026-11-05 | biodiesel_us | custo_oleo_usd_galao: 4.737 USD/galão (7.5 lb × óleo 63.16 cts/lb)
- 2026-11-05 | biodiesel_us | margem_usd_galao: 1.8011 USD/galão (receita 7.34 (HO 4.17 + 1.5×RIN 2.11) − custo 5.54 (óleo 4.74 + ind 0.80))
- 2026-11-05 | biodiesel_us | receita_usd_galao: 7.3381 USD/galão (HO 4.17 + 1.5×RIN 2.11)
- 2026-11-05 | complexo_soja | crush_margin_usd_bu: 1.951 USD/bushel (Board Crush: farelo 319.70 + oleo 63.16 − soja 1203.00)
- 2026-11-05 | complexo_soja | far_soj_ratio_pct: 79.73 % (farelo 319.70/sht ÷ (soja 1203.00cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-11-05 | complexo_soja | indice_sobra_farelo: 25.0 0-100 (sem sobra relevante (1/4 condições))
- 2026-11-05 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-11-05 | complexo_soja | oil_meal_spread_usd_bu: -0.0858 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-11-05 | complexo_soja | oil_share_pct: 49.69 % (valor oleo 6.95 / total 13.98)
- 2026-11-05 | soja_paridade_br | brl_saca_paridade: 145.28 BRL/saca60kg (CBOT 1203.00 cts × USD/BRL 5.4778 (sem basis))
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
- 2026-11-02 | complexo_soja | oil_share_pct: 50.45 % (valor oleo 7.16 / total 14.19)
- 2026-11-02 | soja_paridade_br | brl_saca_paridade: 145.42 BRL/saca60kg (CBOT 1216.75 cts × USD/BRL 5.4212 (sem basis))
- 2026-11-01 | complexo_soja | indice_sobra_farelo: 75.0 0-100 (sobra relevante (3/4 condições))
- 2026-11-01 | complexo_soja | indice_suporte_oleo: 80.0 0-100 (óleo domina o crush (4/5 condições))
- 2026-10-31 | complexo_soja | indice_sobra_farelo: 100.0 0-100 (forte pressão baixista no farelo (4/4 condições))
- 2026-10-31 | complexo_soja | indice_suporte_oleo: 80.0 0-100 (óleo domina o crush (4/5 condições))
- 2026-10-30 | biodiesel_us | custo_oleo_usd_galao: 4.9425 USD/galão (7.5 lb × óleo 65.90 cts/lb)
- 2026-10-30 | biodiesel_us | margem_usd_galao: 2.213 USD/galão (receita 7.96 (HO 4.79 + 1.5×RIN 2.11) − custo 5.74 (óleo 4.94 + ind 0.80))
- 2026-10-30 | biodiesel_us | receita_usd_galao: 7.9555 USD/galão (HO 4.79 + 1.5×RIN 2.11)
- 2026-10-30 | complexo_soja | crush_margin_usd_bu: 2.0477 USD/bushel (Board Crush: farelo 324.60 + oleo 65.90 − soja 1234.25)
- 2026-10-30 | complexo_soja | far_soj_ratio_pct: 78.9 % (farelo 324.60/sht ÷ (soja 1234.25cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-10-30 | complexo_soja | indice_sobra_farelo: 100.0 0-100 (forte pressão baixista no farelo (4/4 condições))

---

## inmet

- 2026-11-05 | cascavel_pr | temp_max_manha: 28.0 C (Cascavel/PR — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-05 | cascavel_pr | temp_max_noite: 28.0 C (Cascavel/PR — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-05 | cascavel_pr | temp_max_tarde: 28.0 C (Cascavel/PR — Muitas nuvens com chuva isolada)
- 2026-11-05 | cascavel_pr | temp_min_manha: 17.0 C (Cascavel/PR — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-05 | cascavel_pr | temp_min_noite: 17.0 C (Cascavel/PR — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-05 | cascavel_pr | temp_min_tarde: 17.0 C (Cascavel/PR — Muitas nuvens com chuva isolada)
- 2026-11-05 | cuiaba_mt | temp_max_manha: 35.0 C (Cuiaba/MT — Muitas nuvens com chuva isolada)
- 2026-11-05 | cuiaba_mt | temp_max_noite: 35.0 C (Cuiaba/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-05 | cuiaba_mt | temp_max_tarde: 35.0 C (Cuiaba/MT — Muitas nuvens com chuva isolada)
- 2026-11-05 | cuiaba_mt | temp_min_manha: 27.0 C (Cuiaba/MT — Muitas nuvens com chuva isolada)
- 2026-11-05 | cuiaba_mt | temp_min_noite: 27.0 C (Cuiaba/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-05 | cuiaba_mt | temp_min_tarde: 27.0 C (Cuiaba/MT — Muitas nuvens com chuva isolada)
- 2026-11-05 | lucas_rio_verde_mt | temp_max_manha: 38.0 C (Lucas do Rio Verde/MT — Muitas nuvens com chuva isolada)
- 2026-11-05 | lucas_rio_verde_mt | temp_max_noite: 38.0 C (Lucas do Rio Verde/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-05 | lucas_rio_verde_mt | temp_max_tarde: 38.0 C (Lucas do Rio Verde/MT — Muitas nuvens com chuva isolada)
- 2026-11-05 | lucas_rio_verde_mt | temp_min_manha: 25.0 C (Lucas do Rio Verde/MT — Muitas nuvens com chuva isolada)
- 2026-11-05 | lucas_rio_verde_mt | temp_min_noite: 25.0 C (Lucas do Rio Verde/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-05 | lucas_rio_verde_mt | temp_min_tarde: 25.0 C (Lucas do Rio Verde/MT — Muitas nuvens com chuva isolada)
- 2026-11-05 | maringa_pr | temp_max_manha: 27.0 C (Maringa/PR — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-05 | maringa_pr | temp_max_noite: 27.0 C (Maringa/PR — Muitas nuvens com pancadas de chuva isoladas)
- 2026-11-05 | maringa_pr | temp_max_tarde: 27.0 C (Maringa/PR — Muitas nuvens com pancadas de chuva isoladas)
- 2026-11-05 | maringa_pr | temp_min_manha: 22.0 C (Maringa/PR — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-05 | maringa_pr | temp_min_noite: 22.0 C (Maringa/PR — Muitas nuvens com pancadas de chuva isoladas)
- 2026-11-05 | maringa_pr | temp_min_tarde: 22.0 C (Maringa/PR — Muitas nuvens com pancadas de chuva isoladas)
- 2026-11-05 | passo_fundo_rs | temp_max_manha: 24.0 C (Passo Fundo/RS — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-05 | passo_fundo_rs | temp_max_noite: 24.0 C (Passo Fundo/RS — Poucas nuvens)
- 2026-11-05 | passo_fundo_rs | temp_max_tarde: 24.0 C (Passo Fundo/RS — Muitas nuvens)
- 2026-11-05 | passo_fundo_rs | temp_min_manha: 13.0 C (Passo Fundo/RS — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-05 | passo_fundo_rs | temp_min_noite: 13.0 C (Passo Fundo/RS — Poucas nuvens)
- 2026-11-05 | passo_fundo_rs | temp_min_tarde: 13.0 C (Passo Fundo/RS — Muitas nuvens)
- 2026-11-05 | rio_verde_go | temp_max_manha: 35.0 C (Rio Verde/GO — Muitas nuvens com chuva isolada)
- 2026-11-05 | rio_verde_go | temp_max_noite: 35.0 C (Rio Verde/GO — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-05 | rio_verde_go | temp_max_tarde: 35.0 C (Rio Verde/GO — Muitas nuvens com pancadas de chuva isoladas)
- 2026-11-05 | rio_verde_go | temp_min_manha: 21.0 C (Rio Verde/GO — Muitas nuvens com chuva isolada)
- 2026-11-05 | rio_verde_go | temp_min_noite: 21.0 C (Rio Verde/GO — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-11-05 | rio_verde_go | temp_min_tarde: 21.0 C (Rio Verde/GO — Muitas nuvens com pancadas de chuva isoladas)
- 2026-11-05 | sinop_mt | temp_max_manha: 38.0 C (Sinop/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-05 | sinop_mt | temp_max_noite: 38.0 C (Sinop/MT — Muitas nuvens com pancadas de chuva isoladas)
- 2026-11-05 | sinop_mt | temp_max_tarde: 38.0 C (Sinop/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-05 | sinop_mt | temp_min_manha: 24.0 C (Sinop/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-05 | sinop_mt | temp_min_noite: 24.0 C (Sinop/MT — Muitas nuvens com pancadas de chuva isoladas)
- 2026-11-05 | sinop_mt | temp_min_tarde: 24.0 C (Sinop/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-05 | sorriso_mt | temp_max_manha: 37.0 C (Sorriso/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-05 | sorriso_mt | temp_max_noite: 37.0 C (Sorriso/MT — Muitas nuvens com pancadas de chuva isoladas)
- 2026-11-05 | sorriso_mt | temp_max_tarde: 37.0 C (Sorriso/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-05 | sorriso_mt | temp_min_manha: 24.0 C (Sorriso/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-05 | sorriso_mt | temp_min_noite: 24.0 C (Sorriso/MT — Muitas nuvens com pancadas de chuva isoladas)
- 2026-11-05 | sorriso_mt | temp_min_tarde: 24.0 C (Sorriso/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-04 | cascavel_pr | temp_max_manha: 32.0 C (Cascavel/PR — Nublado com pancadas de chuva e trovoadas)
- 2026-11-04 | cascavel_pr | temp_max_noite: 32.0 C (Cascavel/PR — Nublado com pancadas de chuva e trovoadas)

---

## mpob

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
| 2026-11-05 | 7d | 2026-11-12 | farelo_cbot | 319.70 | 289.88 | 303.54 | 317.20 | baixista |
| 2026-11-05 | 7d | 2026-11-12 | oleo_cbot | 63.16 | 59.88 | 62.25 | 64.62 | baixista |
| 2026-11-05 | 7d | 2026-11-12 | soja_cbot | 1203.00 | 1149.47 | 1174.40 | 1199.33 | baixista |
| 2026-11-05 | 30d | 2026-12-05 | farelo_cbot | 319.70 | 216.28 | 244.56 | 272.83 | baixista |
| 2026-11-05 | 30d | 2026-12-05 | oleo_cbot | 63.16 | 53.58 | 58.48 | 63.39 | baixista |
| 2026-11-05 | 30d | 2026-12-05 | soja_cbot | 1203.00 | 1015.54 | 1067.15 | 1118.77 | baixista |
| 2026-11-04 | 7d | 2026-11-11 | farelo_cbot | 318.60 | 288.62 | 302.03 | 315.44 | baixista |
| 2026-11-04 | 7d | 2026-11-11 | oleo_cbot | 63.53 | 62.02 | 64.04 | 66.07 | baixista |
| 2026-11-04 | 7d | 2026-11-11 | soja_cbot | 1202.25 | 1155.76 | 1180.10 | 1204.43 | baixista |
| 2026-11-04 | 30d | 2026-12-04 | farelo_cbot | 318.60 | 219.91 | 247.67 | 275.44 | baixista |
| 2026-11-04 | 30d | 2026-12-04 | oleo_cbot | 63.53 | 56.70 | 60.89 | 65.08 | baixista |
| 2026-11-04 | 30d | 2026-12-04 | soja_cbot | 1202.25 | 1027.74 | 1078.12 | 1128.49 | baixista |
| 2026-11-03 | 7d | 2026-11-10 | farelo_cbot | 318.00 | 291.32 | 305.36 | 319.40 | baixista |
| 2026-11-03 | 7d | 2026-11-10 | oleo_cbot | 65.28 | 62.23 | 64.30 | 66.36 | baixista |
| 2026-11-03 | 7d | 2026-11-10 | soja_cbot | 1214.00 | 1166.02 | 1192.23 | 1218.45 | baixista |
| 2026-11-03 | 30d | 2026-12-03 | farelo_cbot | 318.00 | 223.07 | 252.13 | 281.20 | baixista |
| 2026-11-03 | 30d | 2026-12-03 | oleo_cbot | 65.28 | 56.86 | 61.13 | 65.41 | baixista |
| 2026-11-03 | 30d | 2026-12-03 | soja_cbot | 1214.00 | 1037.11 | 1091.39 | 1145.66 | baixista |
| 2026-11-02 | 7d | 2026-11-09 | farelo_cbot | 319.60 | 296.71 | 311.44 | 326.18 | baixista |
| 2026-11-02 | 7d | 2026-11-09 | oleo_cbot | 65.08 | 62.94 | 65.04 | 67.14 | baixista |
| 2026-11-02 | 7d | 2026-11-09 | soja_cbot | 1216.75 | 1182.82 | 1206.50 | 1230.18 | baixista |
| 2026-11-02 | 30d | 2026-12-02 | farelo_cbot | 319.60 | 231.43 | 261.93 | 292.43 | baixista |
| 2026-11-02 | 30d | 2026-12-02 | oleo_cbot | 65.08 | 57.62 | 61.97 | 66.31 | baixista |
| 2026-11-02 | 30d | 2026-12-02 | soja_cbot | 1216.75 | 1057.38 | 1106.39 | 1155.41 | baixista |

---


---

# Fila de julgamento — 2026-11-05

**7 item(ns).** Frase-gatilho: "lê a fila de julgamento e trata"

## 🔴 [nivel_tese] soja_cbot fechou em 1203.00 — acima da resistencia 1180.00
- id: `alerta-quebra_resistencia-soja_cbot-2026-11-05`
- fato: soja_cbot = 1203.00 vs nivel 1180.00 (2026-11-05)
- refs: soja_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] oleo_cbot fechou em 63.16 — abaixo do suporte 72.00
- id: `alerta-quebra_suporte-oleo_cbot-2026-11-05`
- fato: oleo_cbot = 63.16 vs nivel 72.00 (2026-11-05)
- refs: oleo_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] usd_brl_ptax fechou em 5.48 — acima da resistencia 5.30
- id: `alerta-quebra_resistencia-usd_brl_ptax-2026-11-04`
- fato: usd_brl_ptax = 5.48 vs nivel 5.30 (2026-11-04)
- refs: usd_brl_ptax
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] complexo_soja fechou em 1.95 — abaixo do suporte 2.50
- id: `alerta-quebra_suporte-complexo_soja-2026-11-05`
- fato: complexo_soja = 1.95 vs nivel 2.50 (2026-11-05)
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

## 🟡 [release] NOPA novo (2026-11-05)
- id: `release-nopa-2026-11-05`
- fato: fonte nopa com data 2026-11-05 — coletado, ainda nao interpretado
- refs: complexo_soja
- leitura: O numero muda o balanco/tese? Algo relevante pro farelo?

---
Trate só 🔴/🟡. Saída = `insights/*.md` (formato de generate_insights.txt, com `vies:`). Cite o `id` da fila no corpo do insight. Máx 1-3. Não duplicar insight recente.
