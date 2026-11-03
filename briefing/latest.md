# Briefing consolidado — 2026-11-03

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
- 2026-10-21 | eur_brl_ptax | valor: 5.6411 BRL/EUR (sgs=21619)
- 2026-10-21 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-10-21 | usd_brl_ptax | valor: 5.0277 BRL/USD (sgs=1)
- 2026-10-20 | eur_brl_ptax | valor: 5.6317 BRL/EUR (sgs=21619)
- 2026-10-20 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-10-20 | usd_brl_ptax | valor: 5.014 BRL/USD (sgs=1)

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

- 2026-11-03 | farelo_cbot | abertura: 320.29998779296875 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-03 | farelo_cbot | fechamento: 319.5 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-03 | farelo_cbot | fechamento_F27: 319.8999938964844 USD/short_ton (ticker=ZMF27.CBT venc=jan/27)
- 2026-11-03 | farelo_cbot | fechamento_H27: 321.20001220703125 USD/short_ton (ticker=ZMH27.CBT venc=mar/27)
- 2026-11-03 | farelo_cbot | fechamento_K27: 325.5 USD/short_ton (ticker=ZMK27.CBT venc=mai/27)
- 2026-11-03 | farelo_cbot | fechamento_N27: 330.70001220703125 USD/short_ton (ticker=ZMN27.CBT venc=jul/27)
- 2026-11-03 | farelo_cbot | fechamento_Q27: 330.8999938964844 USD/short_ton (ticker=ZMQ27.CBT venc=ago/27)
- 2026-11-03 | farelo_cbot | fechamento_Z26: 319.6000061035156 USD/short_ton (ticker=ZMZ26.CBT venc=dez/26)
- 2026-11-03 | farelo_cbot | maxima: 320.5 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-03 | farelo_cbot | minima: 319.0 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-03 | farelo_cbot | volume: 1503.0 contratos (ticker=ZMZ26.CBT)
- 2026-11-03 | heating_oil_cbot | abertura: 4.674600124359131 USD/galão (ticker=HO=F)
- 2026-11-03 | heating_oil_cbot | fechamento: 4.421800136566162 USD/galão (ticker=HO=F)
- 2026-11-03 | heating_oil_cbot | maxima: 4.448800086975098 USD/galão (ticker=HO=F)
- 2026-11-03 | heating_oil_cbot | minima: 4.405200004577637 USD/galão (ticker=HO=F)
- 2026-11-03 | heating_oil_cbot | volume: 700.0 contratos (ticker=HO=F)
- 2026-11-03 | oleo_cbot | abertura: 65.12000274658203 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-11-03 | oleo_cbot | fechamento: 65.13999938964844 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-11-03 | oleo_cbot | fechamento_F27: 65.3499984741211 USD_cts/lb (ticker=ZLF27.CBT venc=jan/27)
- 2026-11-03 | oleo_cbot | fechamento_H27: 65.81999969482422 USD_cts/lb (ticker=ZLH27.CBT venc=mar/27)
- 2026-11-03 | oleo_cbot | fechamento_K27: 66.20999908447266 USD_cts/lb (ticker=ZLK27.CBT venc=mai/27)
- 2026-11-03 | oleo_cbot | fechamento_N27: 66.33999633789062 USD_cts/lb (ticker=ZLN27.CBT venc=jul/27)
- 2026-11-03 | oleo_cbot | fechamento_Q27: 65.95999908447266 USD_cts/lb (ticker=ZLQ27.CBT venc=ago/27)
- 2026-11-03 | oleo_cbot | fechamento_Z26: 65.13999938964844 USD_cts/lb (ticker=ZLZ26.CBT venc=dez/26)
- 2026-11-03 | oleo_cbot | maxima: 65.25 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-11-03 | oleo_cbot | minima: 64.95999908447266 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-11-03 | oleo_cbot | volume: 2357.0 contratos (ticker=ZLZ26.CBT)
- 2026-11-03 | soja_cbot | abertura: 1217.0 USD/bushel (ticker=ZSF27.CBT)
- 2026-11-03 | soja_cbot | fechamento: 1219.5 USD/bushel (ticker=ZSF27.CBT)
- 2026-11-03 | soja_cbot | fechamento_F27: 1219.5 USD/bushel (ticker=ZSF27.CBT venc=jan/27)
- 2026-11-03 | soja_cbot | fechamento_H27: 1228.5 USD/bushel (ticker=ZSH27.CBT venc=mar/27)
- 2026-11-03 | soja_cbot | fechamento_K27: 1238.75 USD/bushel (ticker=ZSK27.CBT venc=mai/27)
- 2026-11-03 | soja_cbot | fechamento_N27: 1247.0 USD/bushel (ticker=ZSN27.CBT venc=jul/27)
- 2026-11-03 | soja_cbot | fechamento_Q27: 1233.25 USD/bushel (ticker=ZSQ27.CBT venc=ago/27)
- 2026-11-03 | soja_cbot | fechamento_X26: 1205.5 USD/bushel (ticker=ZSX26.CBT venc=nov/26)
- 2026-11-03 | soja_cbot | maxima: 1219.5 USD/bushel (ticker=ZSF27.CBT)
- 2026-11-03 | soja_cbot | minima: 1216.0 USD/bushel (ticker=ZSF27.CBT)
- 2026-11-03 | soja_cbot | volume: 12351.0 contratos (ticker=ZSF27.CBT)
- 2026-11-02 | farelo_cbot | abertura: 324.6000061035156 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-02 | farelo_cbot | fechamento: 319.6000061035156 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-02 | farelo_cbot | fechamento_F27: 319.70001220703125 USD/short_ton (ticker=ZMF27.CBT venc=jan/27)
- 2026-11-02 | farelo_cbot | fechamento_H27: 321.29998779296875 USD/short_ton (ticker=ZMH27.CBT venc=mar/27)
- 2026-11-02 | farelo_cbot | fechamento_K27: 325.5 USD/short_ton (ticker=ZMK27.CBT venc=mai/27)
- 2026-11-02 | farelo_cbot | fechamento_N27: 330.79998779296875 USD/short_ton (ticker=ZMN27.CBT venc=jul/27)
- 2026-11-02 | farelo_cbot | fechamento_Q27: 331.0 USD/short_ton (ticker=ZMQ27.CBT venc=ago/27)
- 2026-11-02 | farelo_cbot | fechamento_Z26: 319.3999938964844 USD/short_ton (ticker=ZMZ26.CBT venc=dez/26)
- 2026-11-02 | farelo_cbot | maxima: 326.0 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-02 | farelo_cbot | minima: 318.79998779296875 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-11-02 | farelo_cbot | volume: 74254.0 contratos (ticker=ZMZ26.CBT)
- 2026-11-02 | heating_oil_cbot | abertura: 4.674600124359131 USD/galão (ticker=HO=F)

---

## indicators

- 2026-11-03 | biodiesel_us | custo_oleo_usd_galao: 4.8855 USD/galão (7.5 lb × óleo 65.14 cts/lb)
- 2026-11-03 | biodiesel_us | margem_usd_galao: 1.9013 USD/galão (receita 7.59 (HO 4.42 + 1.5×RIN 2.11) − custo 5.69 (óleo 4.89 + ind 0.80))
- 2026-11-03 | biodiesel_us | receita_usd_galao: 7.5868 USD/galão (HO 4.42 + 1.5×RIN 2.11)
- 2026-11-03 | complexo_soja | crush_margin_usd_bu: 1.9994 USD/bushel (Board Crush: farelo 319.50 + oleo 65.14 − soja 1219.50)
- 2026-11-03 | complexo_soja | far_soj_ratio_pct: 78.6 % (farelo 319.50/sht ÷ (soja 1219.50cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-11-03 | complexo_soja | indice_sobra_farelo: 50.0 0-100 (pressão moderada (2/4 condições))
- 2026-11-03 | complexo_soja | indice_suporte_oleo: 80.0 0-100 (óleo domina o crush (4/5 condições))
- 2026-11-03 | complexo_soja | oil_meal_spread_usd_bu: 0.1364 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-11-03 | complexo_soja | oil_share_pct: 50.48 % (valor oleo 7.17 / total 14.19)
- 2026-11-03 | soja_paridade_br | brl_saca_paridade: 145.75 BRL/saca60kg (CBOT 1219.50 cts × USD/BRL 5.4212 (sem basis))
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
- 2026-10-30 | complexo_soja | indice_suporte_oleo: 80.0 0-100 (óleo domina o crush (4/5 condições))
- 2026-10-30 | complexo_soja | oil_meal_spread_usd_bu: 0.1078 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-10-30 | complexo_soja | oil_share_pct: 50.37 % (valor oleo 7.25 / total 14.39)
- 2026-10-30 | soja_paridade_br | brl_saca_paridade: 147.51 BRL/saca60kg (CBOT 1234.25 cts × USD/BRL 5.4212 (sem basis))
- 2026-10-29 | biodiesel_us | custo_oleo_usd_galao: 4.923 USD/galão (7.5 lb × óleo 65.64 cts/lb)
- 2026-10-29 | biodiesel_us | margem_usd_galao: 2.178 USD/galão (receita 7.90 (HO 4.74 + 1.5×RIN 2.11) − custo 5.72 (óleo 4.92 + ind 0.80))
- 2026-10-29 | biodiesel_us | receita_usd_galao: 7.901 USD/galão (HO 4.74 + 1.5×RIN 2.11)
- 2026-10-29 | complexo_soja | crush_margin_usd_bu: 2.1175 USD/bushel (Board Crush: farelo 329.30 + oleo 65.64 − soja 1234.75)
- 2026-10-29 | complexo_soja | far_soj_ratio_pct: 80.01 % (farelo 329.30/sht ÷ (soja 1234.75cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-10-29 | complexo_soja | indice_sobra_farelo: 75.0 0-100 (sobra relevante (3/4 condições))
- 2026-10-29 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-10-29 | complexo_soja | oil_meal_spread_usd_bu: -0.0242 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-10-29 | complexo_soja | oil_share_pct: 49.92 % (valor oleo 7.22 / total 14.46)
- 2026-10-29 | soja_paridade_br | brl_saca_paridade: 146.3 BRL/saca60kg (CBOT 1234.75 cts × USD/BRL 5.3744 (sem basis))
- 2026-10-28 | biodiesel_us | custo_oleo_usd_galao: 4.917 USD/galão (7.5 lb × óleo 65.56 cts/lb)
- 2026-10-28 | biodiesel_us | margem_usd_galao: 2.2632 USD/galão (receita 7.98 (HO 4.82 + 1.5×RIN 2.11) − custo 5.72 (óleo 4.92 + ind 0.80))
- 2026-10-28 | biodiesel_us | receita_usd_galao: 7.9802 USD/galão (HO 4.82 + 1.5×RIN 2.11)
- 2026-10-28 | complexo_soja | crush_margin_usd_bu: 2.217 USD/bushel (Board Crush: farelo 335.70 + oleo 65.56 − soja 1238.00)
- 2026-10-28 | complexo_soja | far_soj_ratio_pct: 81.35 % (farelo 335.70/sht ÷ (soja 1238.00cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-10-28 | complexo_soja | indice_sobra_farelo: 75.0 0-100 (sobra relevante (3/4 condições))

---

## inmet

- 2026-11-04 | cascavel_pr | temp_max_manha: 30.0 C (Cascavel/PR — Encoberto com chuva isolada)
- 2026-11-04 | cascavel_pr | temp_max_noite: 30.0 C (Cascavel/PR — Encoberto com pancadas de chuva e trovoadas isoladas)
- 2026-11-04 | cascavel_pr | temp_max_tarde: 30.0 C (Cascavel/PR — Encoberto com chuvisco)
- 2026-11-04 | cascavel_pr | temp_min_manha: 19.0 C (Cascavel/PR — Encoberto com chuva isolada)
- 2026-11-04 | cascavel_pr | temp_min_noite: 19.0 C (Cascavel/PR — Encoberto com pancadas de chuva e trovoadas isoladas)
- 2026-11-04 | cascavel_pr | temp_min_tarde: 19.0 C (Cascavel/PR — Encoberto com chuvisco)
- 2026-11-04 | cuiaba_mt | temp_max_manha: 38.0 C (Cuiaba/MT — Encoberto com chuvisco)
- 2026-11-04 | cuiaba_mt | temp_max_noite: 38.0 C (Cuiaba/MT — Nublado)
- 2026-11-04 | cuiaba_mt | temp_max_tarde: 38.0 C (Cuiaba/MT — Encoberto)
- 2026-11-04 | cuiaba_mt | temp_min_manha: 25.0 C (Cuiaba/MT — Encoberto com chuvisco)
- 2026-11-04 | cuiaba_mt | temp_min_noite: 25.0 C (Cuiaba/MT — Nublado)
- 2026-11-04 | cuiaba_mt | temp_min_tarde: 25.0 C (Cuiaba/MT — Encoberto)
- 2026-11-04 | lucas_rio_verde_mt | temp_max_manha: 37.0 C (Lucas do Rio Verde/MT — Encoberto com chuvisco)
- 2026-11-04 | lucas_rio_verde_mt | temp_max_noite: 37.0 C (Lucas do Rio Verde/MT — Encoberto)
- 2026-11-04 | lucas_rio_verde_mt | temp_max_tarde: 37.0 C (Lucas do Rio Verde/MT — Encoberto)
- 2026-11-04 | lucas_rio_verde_mt | temp_min_manha: 26.0 C (Lucas do Rio Verde/MT — Encoberto com chuvisco)
- 2026-11-04 | lucas_rio_verde_mt | temp_min_noite: 26.0 C (Lucas do Rio Verde/MT — Encoberto)
- 2026-11-04 | lucas_rio_verde_mt | temp_min_tarde: 26.0 C (Lucas do Rio Verde/MT — Encoberto)
- 2026-11-04 | maringa_pr | temp_max_manha: 30.0 C (Maringa/PR — Encoberto com chuvisco)
- 2026-11-04 | maringa_pr | temp_max_noite: 30.0 C (Maringa/PR — Encoberto)
- 2026-11-04 | maringa_pr | temp_max_tarde: 30.0 C (Maringa/PR — Encoberto)
- 2026-11-04 | maringa_pr | temp_min_manha: 23.0 C (Maringa/PR — Encoberto com chuvisco)
- 2026-11-04 | maringa_pr | temp_min_noite: 23.0 C (Maringa/PR — Encoberto)
- 2026-11-04 | maringa_pr | temp_min_tarde: 23.0 C (Maringa/PR — Encoberto)
- 2026-11-04 | passo_fundo_rs | temp_max_manha: 23.0 C (Passo Fundo/RS — Encoberto com pancadas de chuva e trovoadas isoladas)
- 2026-11-04 | passo_fundo_rs | temp_max_noite: 23.0 C (Passo Fundo/RS — Encoberto)
- 2026-11-04 | passo_fundo_rs | temp_max_tarde: 23.0 C (Passo Fundo/RS — Encoberto)
- 2026-11-04 | passo_fundo_rs | temp_min_manha: 15.0 C (Passo Fundo/RS — Encoberto com pancadas de chuva e trovoadas isoladas)
- 2026-11-04 | passo_fundo_rs | temp_min_noite: 15.0 C (Passo Fundo/RS — Encoberto)
- 2026-11-04 | passo_fundo_rs | temp_min_tarde: 15.0 C (Passo Fundo/RS — Encoberto)
- 2026-11-04 | rio_verde_go | temp_max_manha: 33.0 C (Rio Verde/GO — Encoberto com chuvisco)
- 2026-11-04 | rio_verde_go | temp_max_noite: 33.0 C (Rio Verde/GO — Encoberto)
- 2026-11-04 | rio_verde_go | temp_max_tarde: 33.0 C (Rio Verde/GO — Encoberto)
- 2026-11-04 | rio_verde_go | temp_min_manha: 23.0 C (Rio Verde/GO — Encoberto com chuvisco)
- 2026-11-04 | rio_verde_go | temp_min_noite: 23.0 C (Rio Verde/GO — Encoberto)
- 2026-11-04 | rio_verde_go | temp_min_tarde: 23.0 C (Rio Verde/GO — Encoberto)
- 2026-11-04 | sinop_mt | temp_max_manha: 37.0 C (Sinop/MT — Encoberto com chuvisco)
- 2026-11-04 | sinop_mt | temp_max_noite: 37.0 C (Sinop/MT — Encoberto)
- 2026-11-04 | sinop_mt | temp_max_tarde: 37.0 C (Sinop/MT — Encoberto)
- 2026-11-04 | sinop_mt | temp_min_manha: 25.0 C (Sinop/MT — Encoberto com chuvisco)
- 2026-11-04 | sinop_mt | temp_min_noite: 25.0 C (Sinop/MT — Encoberto)
- 2026-11-04 | sinop_mt | temp_min_tarde: 25.0 C (Sinop/MT — Encoberto)
- 2026-11-04 | sorriso_mt | temp_max_manha: 38.0 C (Sorriso/MT — Encoberto com chuvisco)
- 2026-11-04 | sorriso_mt | temp_max_noite: 38.0 C (Sorriso/MT — Encoberto)
- 2026-11-04 | sorriso_mt | temp_max_tarde: 38.0 C (Sorriso/MT — Encoberto)
- 2026-11-04 | sorriso_mt | temp_min_manha: 25.0 C (Sorriso/MT — Encoberto com chuvisco)
- 2026-11-04 | sorriso_mt | temp_min_noite: 25.0 C (Sorriso/MT — Encoberto)
- 2026-11-04 | sorriso_mt | temp_min_tarde: 25.0 C (Sorriso/MT — Encoberto)
- 2026-11-03 | cascavel_pr | temp_max_manha: 28.0 C (Cascavel/PR — Muitas nuvens com pancadas de chuva e trovoadas)
- 2026-11-03 | cascavel_pr | temp_max_noite: 28.0 C (Cascavel/PR — Muitas nuvens)

---

## mpob

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
| 2026-11-03 | 7d | 2026-11-10 | farelo_cbot | 319.50 | 291.32 | 305.36 | 319.40 | baixista |
| 2026-11-03 | 7d | 2026-11-10 | oleo_cbot | 65.14 | 62.23 | 64.30 | 66.36 | baixista |
| 2026-11-03 | 7d | 2026-11-10 | soja_cbot | 1219.50 | 1166.02 | 1192.23 | 1218.45 | baixista |
| 2026-11-03 | 30d | 2026-12-03 | farelo_cbot | 319.50 | 223.07 | 252.13 | 281.20 | baixista |
| 2026-11-03 | 30d | 2026-12-03 | oleo_cbot | 65.14 | 56.86 | 61.13 | 65.41 | baixista |
| 2026-11-03 | 30d | 2026-12-03 | soja_cbot | 1219.50 | 1037.11 | 1091.39 | 1145.66 | baixista |
| 2026-11-02 | 7d | 2026-11-09 | farelo_cbot | 319.60 | 296.71 | 311.44 | 326.18 | baixista |
| 2026-11-02 | 7d | 2026-11-09 | oleo_cbot | 65.08 | 62.94 | 65.04 | 67.14 | baixista |
| 2026-11-02 | 7d | 2026-11-09 | soja_cbot | 1216.75 | 1182.82 | 1206.50 | 1230.18 | baixista |
| 2026-11-02 | 30d | 2026-12-02 | farelo_cbot | 319.60 | 231.43 | 261.93 | 292.43 | baixista |
| 2026-11-02 | 30d | 2026-12-02 | oleo_cbot | 65.08 | 57.62 | 61.97 | 66.31 | baixista |
| 2026-11-02 | 30d | 2026-12-02 | soja_cbot | 1216.75 | 1057.38 | 1106.39 | 1155.41 | baixista |
| 2026-11-01 | 7d | 2026-11-08 | farelo_cbot | 324.60 | 296.71 | 311.44 | 326.18 | baixista |
| 2026-11-01 | 7d | 2026-11-08 | oleo_cbot | 65.90 | 62.94 | 65.04 | 67.14 | baixista |
| 2026-11-01 | 7d | 2026-11-08 | soja_cbot | 1234.25 | 1182.82 | 1206.50 | 1230.18 | baixista |
| 2026-11-01 | 30d | 2026-12-01 | farelo_cbot | 324.60 | 231.43 | 261.93 | 292.43 | baixista |
| 2026-11-01 | 30d | 2026-12-01 | oleo_cbot | 65.90 | 57.62 | 61.97 | 66.31 | baixista |
| 2026-11-01 | 30d | 2026-12-01 | soja_cbot | 1234.25 | 1057.38 | 1106.39 | 1155.41 | baixista |
| 2026-10-31 | 7d | 2026-11-07 | farelo_cbot | 324.60 | 296.82 | 311.54 | 326.26 | baixista |
| 2026-10-31 | 7d | 2026-11-07 | oleo_cbot | 65.90 | 62.87 | 64.95 | 67.04 | baixista |
| 2026-10-31 | 7d | 2026-11-07 | soja_cbot | 1234.25 | 1182.63 | 1206.26 | 1229.89 | baixista |
| 2026-10-31 | 30d | 2026-11-30 | farelo_cbot | 324.60 | 231.57 | 262.04 | 292.51 | baixista |
| 2026-10-31 | 30d | 2026-11-30 | oleo_cbot | 65.90 | 57.56 | 61.87 | 66.18 | baixista |
| 2026-10-31 | 30d | 2026-11-30 | soja_cbot | 1234.25 | 1057.19 | 1106.11 | 1155.03 | baixista |

---


---

# Fila de julgamento — 2026-11-03

**7 item(ns).** Frase-gatilho: "lê a fila de julgamento e trata"

## 🔴 [nivel_tese] soja_cbot fechou em 1219.50 — acima da resistencia 1180.00
- id: `alerta-quebra_resistencia-soja_cbot-2026-11-03`
- fato: soja_cbot = 1219.50 vs nivel 1180.00 (2026-11-03)
- refs: soja_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] oleo_cbot fechou em 65.14 — abaixo do suporte 72.00
- id: `alerta-quebra_suporte-oleo_cbot-2026-11-03`
- fato: oleo_cbot = 65.14 vs nivel 72.00 (2026-11-03)
- refs: oleo_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] usd_brl_ptax fechou em 5.42 — acima da resistencia 5.30
- id: `alerta-quebra_resistencia-usd_brl_ptax-2026-10-30`
- fato: usd_brl_ptax = 5.42 vs nivel 5.30 (2026-10-30)
- refs: usd_brl_ptax
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] complexo_soja fechou em 2.00 — abaixo do suporte 2.50
- id: `alerta-quebra_suporte-complexo_soja-2026-11-03`
- fato: complexo_soja = 2.00 vs nivel 2.50 (2026-11-03)
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

## 🟡 [release] NOPA novo (2026-11-03)
- id: `release-nopa-2026-11-03`
- fato: fonte nopa com data 2026-11-03 — coletado, ainda nao interpretado
- refs: complexo_soja
- leitura: O numero muda o balanco/tese? Algo relevante pro farelo?

---
Trate só 🔴/🟡. Saída = `insights/*.md` (formato de generate_insights.txt, com `vies:`). Cite o `id` da fila no corpo do insight. Máx 1-3. Não duplicar insight recente.
