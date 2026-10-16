# Briefing consolidado — 2026-10-16

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
- 2026-10-05 | eur_brl_ptax | valor: 5.5897 BRL/EUR (sgs=21619)
- 2026-10-05 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-10-05 | usd_brl_ptax | valor: 4.9859 BRL/USD (sgs=1)
- 2026-10-02 | eur_brl_ptax | valor: 5.8815 BRL/EUR (sgs=21619)
- 2026-10-02 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-10-02 | usd_brl_ptax | valor: 5.2238 BRL/USD (sgs=1)

---

## bcba

- 2026-10-02 | argentina | page_fetched: 1.0 bool (BCBA acessivel via scraper mas sem links de relatorio detectados.)

---

## cepea_rss

- 2026-10-02 | cepea | release_items: 104.0 items (CEPEA RSS feed — 104 itens parseados)

---

## cftc_cot

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

- 2026-10-16 | farelo_cbot | abertura: 359.79998779296875 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-16 | farelo_cbot | fechamento: 358.8999938964844 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-16 | farelo_cbot | fechamento_F27: 357.20001220703125 USD/short_ton (ticker=ZMF27.CBT venc=jan/27)
- 2026-10-16 | farelo_cbot | fechamento_H27: 355.5 USD/short_ton (ticker=ZMH27.CBT venc=mar/27)
- 2026-10-16 | farelo_cbot | fechamento_K27: 355.79998779296875 USD/short_ton (ticker=ZMK27.CBT venc=mai/27)
- 2026-10-16 | farelo_cbot | fechamento_N27: 358.3999938964844 USD/short_ton (ticker=ZMN27.CBT venc=jul/27)
- 2026-10-16 | farelo_cbot | fechamento_Z26: 358.8999938964844 USD/short_ton (ticker=ZMZ26.CBT venc=dez/26)
- 2026-10-16 | farelo_cbot | maxima: 359.79998779296875 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-16 | farelo_cbot | minima: 358.5 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-16 | farelo_cbot | volume: 1757.0 contratos (ticker=ZMZ26.CBT)
- 2026-10-16 | heating_oil_cbot | abertura: 4.633800029754639 USD/galão (ticker=HO=F)
- 2026-10-16 | heating_oil_cbot | fechamento: 4.605100154876709 USD/galão (ticker=HO=F)
- 2026-10-16 | heating_oil_cbot | maxima: 4.633800029754639 USD/galão (ticker=HO=F)
- 2026-10-16 | heating_oil_cbot | minima: 4.575099945068359 USD/galão (ticker=HO=F)
- 2026-10-16 | heating_oil_cbot | volume: 686.0 contratos (ticker=HO=F)
- 2026-10-16 | oleo_cbot | abertura: 67.22000122070312 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-10-16 | oleo_cbot | fechamento: 67.04000091552734 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-10-16 | oleo_cbot | fechamento_F27: 67.22000122070312 USD_cts/lb (ticker=ZLF27.CBT venc=jan/27)
- 2026-10-16 | oleo_cbot | fechamento_H27: 67.43000030517578 USD_cts/lb (ticker=ZLH27.CBT venc=mar/27)
- 2026-10-16 | oleo_cbot | fechamento_K27: 67.62000274658203 USD_cts/lb (ticker=ZLK27.CBT venc=mai/27)
- 2026-10-16 | oleo_cbot | fechamento_N27: 67.63999938964844 USD_cts/lb (ticker=ZLN27.CBT venc=jul/27)
- 2026-10-16 | oleo_cbot | fechamento_Z26: 67.04000091552734 USD_cts/lb (ticker=ZLZ26.CBT venc=dez/26)
- 2026-10-16 | oleo_cbot | maxima: 67.3499984741211 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-10-16 | oleo_cbot | minima: 67.0199966430664 USD_cts/lb (ticker=ZLZ26.CBT)
- 2026-10-16 | oleo_cbot | volume: 1703.0 contratos (ticker=ZLZ26.CBT)
- 2026-10-16 | soja_cbot | abertura: 1263.0 USD/bushel (ticker=ZSX26.CBT)
- 2026-10-16 | soja_cbot | fechamento: 1263.0 USD/bushel (ticker=ZSX26.CBT)
- 2026-10-16 | soja_cbot | fechamento_F27: 1278.5 USD/bushel (ticker=ZSF27.CBT venc=jan/27)
- 2026-10-16 | soja_cbot | fechamento_H27: 1287.25 USD/bushel (ticker=ZSH27.CBT venc=mar/27)
- 2026-10-16 | soja_cbot | fechamento_K27: 1295.5 USD/bushel (ticker=ZSK27.CBT venc=mai/27)
- 2026-10-16 | soja_cbot | fechamento_N27: 1301.75 USD/bushel (ticker=ZSN27.CBT venc=jul/27)
- 2026-10-16 | soja_cbot | fechamento_Q27: 1285.0 USD/bushel (ticker=ZSQ27.CBT venc=ago/27)
- 2026-10-16 | soja_cbot | fechamento_X26: 1263.0 USD/bushel (ticker=ZSX26.CBT venc=nov/26)
- 2026-10-16 | soja_cbot | maxima: 1264.75 USD/bushel (ticker=ZSX26.CBT)
- 2026-10-16 | soja_cbot | minima: 1262.5 USD/bushel (ticker=ZSX26.CBT)
- 2026-10-16 | soja_cbot | volume: 6389.0 contratos (ticker=ZSX26.CBT)
- 2026-10-15 | farelo_cbot | abertura: 359.79998779296875 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-15 | farelo_cbot | fechamento: 359.79998779296875 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-15 | farelo_cbot | fechamento_F27: 357.6000061035156 USD/short_ton (ticker=ZMF27.CBT venc=jan/27)
- 2026-10-15 | farelo_cbot | fechamento_H27: 355.70001220703125 USD/short_ton (ticker=ZMH27.CBT venc=mar/27)
- 2026-10-15 | farelo_cbot | fechamento_K27: 355.79998779296875 USD/short_ton (ticker=ZMK27.CBT venc=mai/27)
- 2026-10-15 | farelo_cbot | fechamento_N27: 358.20001220703125 USD/short_ton (ticker=ZMN27.CBT venc=jul/27)
- 2026-10-15 | farelo_cbot | fechamento_Z26: 359.79998779296875 USD/short_ton (ticker=ZMZ26.CBT venc=dez/26)
- 2026-10-15 | farelo_cbot | maxima: 359.79998779296875 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-15 | farelo_cbot | minima: 358.5 USD/short_ton (ticker=ZMZ26.CBT)
- 2026-10-15 | farelo_cbot | volume: 1757.0 contratos (ticker=ZMZ26.CBT)
- 2026-10-15 | heating_oil_cbot | abertura: 4.633800029754639 USD/galão (ticker=HO=F)
- 2026-10-15 | heating_oil_cbot | fechamento: 4.600800037384033 USD/galão (ticker=HO=F)
- 2026-10-15 | heating_oil_cbot | maxima: 4.633800029754639 USD/galão (ticker=HO=F)
- 2026-10-15 | heating_oil_cbot | minima: 4.575099945068359 USD/galão (ticker=HO=F)

---

## indicators

- 2026-10-16 | biodiesel_us | custo_oleo_usd_galao: 5.028 USD/galão (7.5 lb × óleo 67.04 cts/lb)
- 2026-10-16 | biodiesel_us | margem_usd_galao: 1.9421 USD/galão (receita 7.77 (HO 4.61 + 1.5×RIN 2.11) − custo 5.83 (óleo 5.03 + ind 0.80))
- 2026-10-16 | biodiesel_us | receita_usd_galao: 7.7701 USD/galão (HO 4.61 + 1.5×RIN 2.11)
- 2026-10-16 | complexo_soja | crush_margin_usd_bu: 2.6402 USD/bushel (Board Crush: farelo 358.90 + oleo 67.04 − soja 1263.00)
- 2026-10-16 | complexo_soja | far_soj_ratio_pct: 85.25 % (farelo 358.90/sht ÷ (soja 1263.00cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-10-16 | complexo_soja | indice_sobra_farelo: 80.0 0-100 (forte pressão baixista no farelo (4/5 condições))
- 2026-10-16 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-10-16 | complexo_soja | oil_meal_spread_usd_bu: -0.5214 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-10-16 | complexo_soja | oil_share_pct: 48.29 % (valor oleo 7.37 / total 15.27)
- 2026-10-16 | soja_paridade_br | brl_saca_paridade: 140.67 BRL/saca60kg (CBOT 1263.00 cts × USD/BRL 5.0521 (sem basis))
- 2026-10-15 | biodiesel_us | custo_oleo_usd_galao: 5.0385 USD/galão (7.5 lb × óleo 67.18 cts/lb)
- 2026-10-15 | biodiesel_us | margem_usd_galao: 1.9273 USD/galão (receita 7.77 (HO 4.60 + 1.5×RIN 2.11) − custo 5.84 (óleo 5.04 + ind 0.80))
- 2026-10-15 | biodiesel_us | receita_usd_galao: 7.7658 USD/galão (HO 4.60 + 1.5×RIN 2.11)
- 2026-10-15 | complexo_soja | crush_margin_usd_bu: 2.6629 USD/bushel (Board Crush: farelo 359.80 + oleo 67.18 − soja 1264.25)
- 2026-10-15 | complexo_soja | far_soj_ratio_pct: 85.38 % (farelo 359.80/sht ÷ (soja 1264.25cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-10-15 | complexo_soja | indice_sobra_farelo: 80.0 0-100 (forte pressão baixista no farelo (4/5 condições))
- 2026-10-15 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-10-15 | complexo_soja | oil_meal_spread_usd_bu: -0.5258 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-10-15 | complexo_soja | oil_share_pct: 48.28 % (valor oleo 7.39 / total 15.31)
- 2026-10-15 | soja_paridade_br | brl_saca_paridade: 140.81 BRL/saca60kg (CBOT 1264.25 cts × USD/BRL 5.0521 (sem basis))
- 2026-10-14 | biodiesel_us | custo_oleo_usd_galao: 5.0295 USD/galão (7.5 lb × óleo 67.06 cts/lb)
- 2026-10-14 | biodiesel_us | margem_usd_galao: 2.2629 USD/galão (receita 8.09 (HO 4.93 + 1.5×RIN 2.11) − custo 5.83 (óleo 5.03 + ind 0.80))
- 2026-10-14 | biodiesel_us | receita_usd_galao: 8.0924 USD/galão (HO 4.93 + 1.5×RIN 2.11)
- 2026-10-14 | complexo_soja | crush_margin_usd_bu: 2.6231 USD/bushel (Board Crush: farelo 364.50 + oleo 67.06 − soja 1277.25)
- 2026-10-14 | complexo_soja | far_soj_ratio_pct: 85.61 % (farelo 364.50/sht ÷ (soja 1277.25cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-10-14 | complexo_soja | indice_sobra_farelo: 80.0 0-100 (forte pressão baixista no farelo (4/5 condições))
- 2026-10-14 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-10-14 | complexo_soja | oil_meal_spread_usd_bu: -0.6424 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-10-14 | complexo_soja | oil_share_pct: 47.91 % (valor oleo 7.38 / total 15.40)
- 2026-10-14 | soja_paridade_br | brl_saca_paridade: 142.03 BRL/saca60kg (CBOT 1277.25 cts × USD/BRL 5.0441 (sem basis))
- 2026-10-13 | biodiesel_us | custo_oleo_usd_galao: 5.1015 USD/galão (7.5 lb × óleo 68.02 cts/lb)
- 2026-10-13 | biodiesel_us | margem_usd_galao: 2.1979 USD/galão (receita 8.10 (HO 4.93 + 1.5×RIN 2.11) − custo 5.90 (óleo 5.10 + ind 0.80))
- 2026-10-13 | biodiesel_us | receita_usd_galao: 8.0994 USD/galão (HO 4.93 + 1.5×RIN 2.11)
- 2026-10-13 | complexo_soja | crush_margin_usd_bu: 2.6351 USD/bushel (Board Crush: farelo 363.20 + oleo 68.02 − soja 1283.75)
- 2026-10-13 | complexo_soja | far_soj_ratio_pct: 84.88 % (farelo 363.20/sht ÷ (soja 1283.75cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-10-13 | complexo_soja | indice_sobra_farelo: 80.0 0-100 (forte pressão baixista no farelo (4/5 condições))
- 2026-10-13 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-10-13 | complexo_soja | oil_meal_spread_usd_bu: -0.5082 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-10-13 | complexo_soja | oil_share_pct: 48.36 % (valor oleo 7.48 / total 15.47)
- 2026-10-13 | soja_paridade_br | brl_saca_paridade: 141.78 BRL/saca60kg (CBOT 1283.75 cts × USD/BRL 5.0096 (sem basis))
- 2026-10-12 | biodiesel_us | custo_oleo_usd_galao: 5.1472 USD/galão (7.5 lb × óleo 68.63 cts/lb)
- 2026-10-12 | biodiesel_us | margem_usd_galao: 1.941 USD/galão (receita 7.89 (HO 4.72 + 1.5×RIN 2.11) − custo 5.95 (óleo 5.15 + ind 0.80))
- 2026-10-12 | biodiesel_us | receita_usd_galao: 7.8882 USD/galão (HO 4.72 + 1.5×RIN 2.11)
- 2026-10-12 | complexo_soja | crush_margin_usd_bu: 2.7832 USD/bushel (Board Crush: farelo 368.70 + oleo 68.63 − soja 1287.75)
- 2026-10-12 | complexo_soja | far_soj_ratio_pct: 85.89 % (farelo 368.70/sht ÷ (soja 1287.75cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-10-12 | complexo_soja | indice_sobra_farelo: 80.0 0-100 (forte pressão baixista no farelo (4/5 condições))
- 2026-10-12 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-10-12 | complexo_soja | oil_meal_spread_usd_bu: -0.5621 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-10-12 | complexo_soja | oil_share_pct: 48.21 % (valor oleo 7.55 / total 15.66)
- 2026-10-12 | soja_paridade_br | brl_saca_paridade: 141.64 BRL/saca60kg (CBOT 1287.75 cts × USD/BRL 4.9892 (sem basis))

---

## inmet

- 2026-10-16 | cascavel_pr | temp_max_manha: 21.0 C (Cascavel/PR — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-16 | cascavel_pr | temp_max_noite: 21.0 C (Cascavel/PR — Muitas nuvens)
- 2026-10-16 | cascavel_pr | temp_max_tarde: 21.0 C (Cascavel/PR — Muitas nuvens)
- 2026-10-16 | cascavel_pr | temp_min_manha: 11.0 C (Cascavel/PR — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-16 | cascavel_pr | temp_min_noite: 11.0 C (Cascavel/PR — Muitas nuvens)
- 2026-10-16 | cascavel_pr | temp_min_tarde: 11.0 C (Cascavel/PR — Muitas nuvens)
- 2026-10-16 | cuiaba_mt | temp_max_manha: 29.0 C (Cuiaba/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-16 | cuiaba_mt | temp_max_noite: 29.0 C (Cuiaba/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-16 | cuiaba_mt | temp_max_tarde: 29.0 C (Cuiaba/MT — Muitas nuvens com pancadas de chuva e trovoadas)
- 2026-10-16 | cuiaba_mt | temp_min_manha: 20.0 C (Cuiaba/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-16 | cuiaba_mt | temp_min_noite: 20.0 C (Cuiaba/MT — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-16 | cuiaba_mt | temp_min_tarde: 20.0 C (Cuiaba/MT — Muitas nuvens com pancadas de chuva e trovoadas)
- 2026-10-16 | lucas_rio_verde_mt | temp_max_manha: 32.0 C (Lucas do Rio Verde/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-16 | lucas_rio_verde_mt | temp_max_noite: 32.0 C (Lucas do Rio Verde/MT — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-16 | lucas_rio_verde_mt | temp_max_tarde: 32.0 C (Lucas do Rio Verde/MT — Muitas nuvens com pancadas de chuva e trovoadas)
- 2026-10-16 | lucas_rio_verde_mt | temp_min_manha: 21.0 C (Lucas do Rio Verde/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-16 | lucas_rio_verde_mt | temp_min_noite: 21.0 C (Lucas do Rio Verde/MT — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-16 | lucas_rio_verde_mt | temp_min_tarde: 21.0 C (Lucas do Rio Verde/MT — Muitas nuvens com pancadas de chuva e trovoadas)
- 2026-10-16 | maringa_pr | temp_max_manha: 25.0 C (Maringa/PR — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-16 | maringa_pr | temp_max_noite: 25.0 C (Maringa/PR — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-16 | maringa_pr | temp_max_tarde: 25.0 C (Maringa/PR — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-16 | maringa_pr | temp_min_manha: 13.0 C (Maringa/PR — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-16 | maringa_pr | temp_min_noite: 13.0 C (Maringa/PR — Muitas nuvens com possibilidade de chuva isolada)
- 2026-10-16 | maringa_pr | temp_min_tarde: 13.0 C (Maringa/PR — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-16 | passo_fundo_rs | temp_max_manha: 19.0 C (Passo Fundo/RS — Muitas nuvens)
- 2026-10-16 | passo_fundo_rs | temp_max_noite: 19.0 C (Passo Fundo/RS — Muitas nuvens)
- 2026-10-16 | passo_fundo_rs | temp_max_tarde: 19.0 C (Passo Fundo/RS — Muitas nuvens)
- 2026-10-16 | passo_fundo_rs | temp_min_manha: 11.0 C (Passo Fundo/RS — Muitas nuvens)
- 2026-10-16 | passo_fundo_rs | temp_min_noite: 11.0 C (Passo Fundo/RS — Muitas nuvens)
- 2026-10-16 | passo_fundo_rs | temp_min_tarde: 11.0 C (Passo Fundo/RS — Muitas nuvens)
- 2026-10-16 | rio_verde_go | temp_max_manha: 29.0 C (Rio Verde/GO — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-16 | rio_verde_go | temp_max_noite: 29.0 C (Rio Verde/GO — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-16 | rio_verde_go | temp_max_tarde: 29.0 C (Rio Verde/GO — Muitas nuvens com pancadas de chuva e trovoadas)
- 2026-10-16 | rio_verde_go | temp_min_manha: 20.0 C (Rio Verde/GO — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-16 | rio_verde_go | temp_min_noite: 20.0 C (Rio Verde/GO — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-16 | rio_verde_go | temp_min_tarde: 20.0 C (Rio Verde/GO — Muitas nuvens com pancadas de chuva e trovoadas)
- 2026-10-16 | sinop_mt | temp_max_manha: 34.0 C (Sinop/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-16 | sinop_mt | temp_max_noite: 34.0 C (Sinop/MT — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-16 | sinop_mt | temp_max_tarde: 34.0 C (Sinop/MT — Muitas nuvens com pancadas de chuva e trovoadas)
- 2026-10-16 | sinop_mt | temp_min_manha: 22.0 C (Sinop/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-16 | sinop_mt | temp_min_noite: 22.0 C (Sinop/MT — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-16 | sinop_mt | temp_min_tarde: 22.0 C (Sinop/MT — Muitas nuvens com pancadas de chuva e trovoadas)
- 2026-10-16 | sorriso_mt | temp_max_manha: 34.0 C (Sorriso/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-16 | sorriso_mt | temp_max_noite: 34.0 C (Sorriso/MT — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-16 | sorriso_mt | temp_max_tarde: 34.0 C (Sorriso/MT — Muitas nuvens com pancadas de chuva e trovoadas)
- 2026-10-16 | sorriso_mt | temp_min_manha: 23.0 C (Sorriso/MT — Muitas nuvens com pancadas de chuva e trovoadas isoladas)
- 2026-10-16 | sorriso_mt | temp_min_noite: 23.0 C (Sorriso/MT — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-16 | sorriso_mt | temp_min_tarde: 23.0 C (Sorriso/MT — Muitas nuvens com pancadas de chuva e trovoadas)
- 2026-10-15 | cascavel_pr | temp_max_manha: 24.0 C (Cascavel/PR — Muitas nuvens com pancadas de chuva isoladas)
- 2026-10-15 | cascavel_pr | temp_max_noite: 24.0 C (Cascavel/PR — Muitas nuvens com pancadas de chuva isoladas)

---

## mpob

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
- 2026-10-05 | palma_malasia | page_fetched: 3181.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-04 | palma_malasia | page_fetched: 3181.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-03 | palma_malasia | page_fetched: 3181.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-10-02 | palma_malasia | page_fetched: 3181.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)

---

## noaa_cpc

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
- 2026-10-05 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-04 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-03 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-10-02 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)

---

## nopa

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
- 2026-10-05 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-04 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-03 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-10-02 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)

---

## noticias_rss

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
- 2026-10-05 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-10-04 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-10-03 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-10-02 | noticias | items_fetched: 160.0 items (160 items lidos, 6 mantidos (soja/farelo/oleo))

---

## usda_crop_progress

- 2026-10-11 | soybeans_eua | cond_pct_excellent: 11.0 % (SOYBEANS - CONDITION, MEASURED IN PCT EXCELLENT)
- 2026-10-11 | soybeans_eua | cond_pct_good: 46.0 % (SOYBEANS - CONDITION, MEASURED IN PCT GOOD)
- 2026-10-11 | soybeans_eua | cond_pct_poor: 10.0 % (SOYBEANS - CONDITION, MEASURED IN PCT POOR)
- 2026-10-11 | soybeans_eua | pct_harvested: 46.0 % (SOYBEANS - PROGRESS, MEASURED IN PCT HARVESTED)
- 2026-10-04 | soybeans_eua | cond_pct_excellent: 11.0 % (SOYBEANS - CONDITION, MEASURED IN PCT EXCELLENT)
- 2026-10-04 | soybeans_eua | cond_pct_good: 46.0 % (SOYBEANS - CONDITION, MEASURED IN PCT GOOD)
- 2026-10-04 | soybeans_eua | cond_pct_poor: 10.0 % (SOYBEANS - CONDITION, MEASURED IN PCT POOR)
- 2026-10-04 | soybeans_eua | pct_harvested: 25.0 % (SOYBEANS - PROGRESS, MEASURED IN PCT HARVESTED)

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
| 2026-10-16 | 7d | 2026-10-23 | farelo_cbot | 358.90 | 333.94 | 356.73 | 379.52 | baixista |
| 2026-10-16 | 7d | 2026-10-23 | oleo_cbot | 67.04 | 62.87 | 67.02 | 71.17 | lateral |
| 2026-10-16 | 7d | 2026-10-23 | soja_cbot | 1263.00 | 1195.24 | 1249.39 | 1303.54 | baixista |
| 2026-10-16 | 30d | 2026-11-15 | farelo_cbot | 358.90 | 301.71 | 348.88 | 396.05 | baixista |
| 2026-10-16 | 30d | 2026-11-15 | oleo_cbot | 67.04 | 58.10 | 66.69 | 75.28 | baixista |
| 2026-10-16 | 30d | 2026-11-15 | soja_cbot | 1263.00 | 1084.76 | 1196.86 | 1308.96 | baixista |
| 2026-10-15 | 7d | 2026-10-22 | farelo_cbot | 359.80 | 339.57 | 362.69 | 385.80 | baixista |
| 2026-10-15 | 7d | 2026-10-22 | oleo_cbot | 67.18 | 62.80 | 67.00 | 71.20 | lateral |
| 2026-10-15 | 7d | 2026-10-22 | soja_cbot | 1264.25 | 1208.07 | 1262.68 | 1317.30 | baixista |
| 2026-10-15 | 30d | 2026-11-14 | farelo_cbot | 359.80 | 308.89 | 356.75 | 404.60 | baixista |
| 2026-10-15 | 30d | 2026-11-14 | oleo_cbot | 67.18 | 58.26 | 66.94 | 75.63 | lateral |
| 2026-10-15 | 30d | 2026-11-14 | soja_cbot | 1264.25 | 1105.96 | 1219.02 | 1332.08 | baixista |
| 2026-10-14 | 7d | 2026-10-21 | farelo_cbot | 364.50 | 336.67 | 360.00 | 383.34 | baixista |
| 2026-10-14 | 7d | 2026-10-21 | oleo_cbot | 67.06 | 63.79 | 68.08 | 72.36 | lateral |
| 2026-10-14 | 7d | 2026-10-21 | soja_cbot | 1277.25 | 1217.37 | 1272.87 | 1328.37 | baixista |
| 2026-10-14 | 30d | 2026-11-13 | farelo_cbot | 364.50 | 301.73 | 350.04 | 398.34 | baixista |
| 2026-10-14 | 30d | 2026-11-13 | oleo_cbot | 67.06 | 59.25 | 68.11 | 76.98 | lateral |
| 2026-10-14 | 30d | 2026-11-13 | soja_cbot | 1277.25 | 1114.50 | 1229.40 | 1344.31 | baixista |
| 2026-10-13 | 7d | 2026-10-20 | farelo_cbot | 363.20 | 337.08 | 360.36 | 383.64 | baixista |
| 2026-10-13 | 7d | 2026-10-20 | oleo_cbot | 68.02 | 63.73 | 68.20 | 72.66 | lateral |
| 2026-10-13 | 7d | 2026-10-20 | soja_cbot | 1283.75 | 1208.05 | 1265.44 | 1322.84 | baixista |
| 2026-10-13 | 30d | 2026-11-12 | farelo_cbot | 363.20 | 300.92 | 349.10 | 397.29 | baixista |
| 2026-10-13 | 30d | 2026-11-12 | oleo_cbot | 68.02 | 58.65 | 67.90 | 77.15 | baixista |
| 2026-10-13 | 30d | 2026-11-12 | soja_cbot | 1283.75 | 1102.67 | 1221.50 | 1340.32 | baixista |

---


---

# Fila de julgamento — 2026-10-16

**6 item(ns).** Frase-gatilho: "lê a fila de julgamento e trata"

## 🔴 [nivel_tese] soja_cbot fechou em 1263.00 — acima da resistencia 1180.00
- id: `alerta-quebra_resistencia-soja_cbot-2026-10-16`
- fato: soja_cbot = 1263.00 vs nivel 1180.00 (2026-10-16)
- refs: soja_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] oleo_cbot fechou em 67.04 — abaixo do suporte 72.00
- id: `alerta-quebra_suporte-oleo_cbot-2026-10-16`
- fato: oleo_cbot = 67.04 vs nivel 72.00 (2026-10-16)
- refs: oleo_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] farelo_cbot fechou em 358.90 — acima da resistencia 325.00
- id: `alerta-quebra_resistencia-farelo_cbot-2026-10-16`
- fato: farelo_cbot = 358.90 vs nivel 325.00 (2026-10-16)
- refs: farelo_cbot
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

## 🟡 [release] NOPA novo (2026-10-16)
- id: `release-nopa-2026-10-16`
- fato: fonte nopa com data 2026-10-16 — coletado, ainda nao interpretado
- refs: complexo_soja
- leitura: O numero muda o balanco/tese? Algo relevante pro farelo?

---
Trate só 🔴/🟡. Saída = `insights/*.md` (formato de generate_insights.txt, com `vies:`). Cite o `id` da fila no corpo do insight. Máx 1-3. Não duplicar insight recente.
