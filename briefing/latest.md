# Briefing consolidado — 2026-11-24

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

---

## anec

- 2026-11-24 | anec | links_relatorios: 0.0 count (Nenhum link de relatorio encontrado na pagina /estatisticas/. Estrutura pode ter mudado.)
- 2026-11-23 | anec | links_relatorios: 0.0 count (Nenhum link de relatorio encontrado na pagina /estatisticas/. Estrutura pode ter mudado.)
- 2026-11-22 | anec | links_relatorios: 0.0 count (Nenhum link de relatorio encontrado na pagina /estatisticas/. Estrutura pode ter mudado.)
- 2026-11-21 | anec | links_relatorios: 0.0 count (Nenhum link de relatorio encontrado na pagina /estatisticas/. Estrutura pode ter mudado.)
- 2026-11-20 | anec | links_relatorios: 0.0 count (Nenhum link de relatorio encontrado na pagina /estatisticas/. Estrutura pode ter mudado.)
- 2026-11-19 | anec | links_relatorios: 0.0 count (Nenhum link de relatorio encontrado na pagina /estatisticas/. Estrutura pode ter mudado.)
- 2026-11-18 | anec | links_relatorios: 0.0 count (Nenhum link de relatorio encontrado na pagina /estatisticas/. Estrutura pode ter mudado.)

---

## bcb

- 2026-11-23 | eur_brl_ptax | valor: 6.5076 BRL/EUR (sgs=21619)
- 2026-11-23 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-11-23 | usd_brl_ptax | valor: 5.9708 BRL/USD (sgs=1)
- 2026-11-19 | eur_brl_ptax | valor: 6.4672 BRL/EUR (sgs=21619)
- 2026-11-19 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-11-19 | usd_brl_ptax | valor: 5.8889 BRL/USD (sgs=1)
- 2026-11-18 | eur_brl_ptax | valor: 6.372 BRL/EUR (sgs=21619)
- 2026-11-18 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-11-18 | usd_brl_ptax | valor: 5.8102 BRL/USD (sgs=1)
- 2026-11-17 | eur_brl_ptax | valor: 6.3659 BRL/EUR (sgs=21619)
- 2026-11-17 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-11-17 | usd_brl_ptax | valor: 5.7851 BRL/USD (sgs=1)
- 2026-11-16 | eur_brl_ptax | valor: 6.3102 BRL/EUR (sgs=21619)
- 2026-11-16 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-11-16 | usd_brl_ptax | valor: 5.7324 BRL/USD (sgs=1)
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

---

## cftc_cot

- 2026-11-17 | farelo_cbot | managed_money_long: 121043.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-11-17 | farelo_cbot | managed_money_net: 80610.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE — long - short)
- 2026-11-17 | farelo_cbot | managed_money_short: 40433.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-11-17 | farelo_cbot | open_interest: 586450.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-11-17 | farelo_cbot | producer_long: 90581.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-11-17 | farelo_cbot | producer_short: 337150.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-11-17 | farelo_cbot | swap_long: 119778.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-11-17 | farelo_cbot | swap_short: 10762.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-11-17 | oleo_cbot | managed_money_long: 81049.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-11-17 | oleo_cbot | managed_money_net: 15134.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE — long - short)
- 2026-11-17 | oleo_cbot | managed_money_short: 65915.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-11-17 | oleo_cbot | open_interest: 612107.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-11-17 | oleo_cbot | producer_long: 179907.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-11-17 | oleo_cbot | producer_short: 300504.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-11-17 | oleo_cbot | swap_long: 98533.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-11-17 | oleo_cbot | swap_short: 5070.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-11-17 | soja_cbot | managed_money_long: 170322.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-11-17 | soja_cbot | managed_money_net: 113630.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE — long - short)
- 2026-11-17 | soja_cbot | managed_money_short: 56692.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-11-17 | soja_cbot | open_interest: 997948.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-11-17 | soja_cbot | producer_long: 335993.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-11-17 | soja_cbot | producer_short: 549418.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-11-17 | soja_cbot | swap_long: 129138.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-11-17 | soja_cbot | swap_short: 41860.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-11-10 | farelo_cbot | managed_money_long: 116511.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-11-10 | farelo_cbot | managed_money_net: 66653.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE — long - short)
- 2026-11-10 | farelo_cbot | managed_money_short: 49858.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-11-10 | farelo_cbot | open_interest: 576238.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-11-10 | farelo_cbot | producer_long: 88106.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-11-10 | farelo_cbot | producer_short: 328262.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-11-10 | farelo_cbot | swap_long: 120743.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-11-10 | farelo_cbot | swap_short: 9670.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-11-10 | oleo_cbot | managed_money_long: 82605.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-11-10 | oleo_cbot | managed_money_net: 19562.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE — long - short)
- 2026-11-10 | oleo_cbot | managed_money_short: 63043.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-11-10 | oleo_cbot | open_interest: 614995.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-11-10 | oleo_cbot | producer_long: 177452.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-11-10 | oleo_cbot | producer_short: 300803.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-11-10 | oleo_cbot | swap_long: 93320.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-11-10 | oleo_cbot | swap_short: 4815.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-11-10 | soja_cbot | managed_money_long: 181446.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-11-10 | soja_cbot | managed_money_net: 117586.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE — long - short)
- 2026-11-10 | soja_cbot | managed_money_short: 63860.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-11-10 | soja_cbot | open_interest: 973693.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-11-10 | soja_cbot | producer_long: 320416.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-11-10 | soja_cbot | producer_short: 526115.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-11-10 | soja_cbot | swap_long: 123025.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-11-10 | soja_cbot | swap_short: 42145.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)

---

## cme_cbot

- 2026-11-24 | farelo_cbot | abertura: 344.1000061035156 USD/short_ton (ticker=ZMF27.CBT)
- 2026-11-24 | farelo_cbot | fechamento: 346.0 USD/short_ton (ticker=ZMF27.CBT)
- 2026-11-24 | farelo_cbot | fechamento_F27: 346.0 USD/short_ton (ticker=ZMF27.CBT venc=jan/27)
- 2026-11-24 | farelo_cbot | fechamento_H27: 346.5 USD/short_ton (ticker=ZMH27.CBT venc=mar/27)
- 2026-11-24 | farelo_cbot | fechamento_K27: 347.8999938964844 USD/short_ton (ticker=ZMK27.CBT venc=mai/27)
- 2026-11-24 | farelo_cbot | fechamento_N27: 349.79998779296875 USD/short_ton (ticker=ZMN27.CBT venc=jul/27)
- 2026-11-24 | farelo_cbot | fechamento_Q27: 347.6000061035156 USD/short_ton (ticker=ZMQ27.CBT venc=ago/27)
- 2026-11-24 | farelo_cbot | fechamento_Z26: 347.29998779296875 USD/short_ton (ticker=ZMZ26.CBT venc=dez/26)
- 2026-11-24 | farelo_cbot | maxima: 346.20001220703125 USD/short_ton (ticker=ZMF27.CBT)
- 2026-11-24 | farelo_cbot | minima: 344.1000061035156 USD/short_ton (ticker=ZMF27.CBT)
- 2026-11-24 | farelo_cbot | volume: 3280.0 contratos (ticker=ZMF27.CBT)
- 2026-11-24 | heating_oil_cbot | abertura: 3.657900094985962 USD/galão (ticker=HO=F)
- 2026-11-24 | heating_oil_cbot | fechamento: 3.623800039291382 USD/galão (ticker=HO=F)
- 2026-11-24 | heating_oil_cbot | maxima: 3.657900094985962 USD/galão (ticker=HO=F)
- 2026-11-24 | heating_oil_cbot | minima: 3.6208999156951904 USD/galão (ticker=HO=F)
- 2026-11-24 | heating_oil_cbot | volume: 1210.0 contratos (ticker=HO=F)
- 2026-11-24 | oleo_cbot | abertura: 59.54999923706055 USD_cts/lb (ticker=ZLF27.CBT)
- 2026-11-24 | oleo_cbot | fechamento: 59.08000183105469 USD_cts/lb (ticker=ZLF27.CBT)
- 2026-11-24 | oleo_cbot | fechamento_F27: 59.08000183105469 USD_cts/lb (ticker=ZLF27.CBT venc=jan/27)
- 2026-11-24 | oleo_cbot | fechamento_H27: 59.560001373291016 USD_cts/lb (ticker=ZLH27.CBT venc=mar/27)
- 2026-11-24 | oleo_cbot | fechamento_K27: 60.060001373291016 USD_cts/lb (ticker=ZLK27.CBT venc=mai/27)
- 2026-11-24 | oleo_cbot | fechamento_N27: 60.369998931884766 USD_cts/lb (ticker=ZLN27.CBT venc=jul/27)
- 2026-11-24 | oleo_cbot | fechamento_Q27: 60.22999954223633 USD_cts/lb (ticker=ZLQ27.CBT venc=ago/27)
- 2026-11-24 | oleo_cbot | fechamento_Z26: 58.849998474121094 USD_cts/lb (ticker=ZLZ26.CBT venc=dez/26)
- 2026-11-24 | oleo_cbot | maxima: 59.599998474121094 USD_cts/lb (ticker=ZLF27.CBT)
- 2026-11-24 | oleo_cbot | minima: 59.040000915527344 USD_cts/lb (ticker=ZLF27.CBT)
- 2026-11-24 | oleo_cbot | volume: 3717.0 contratos (ticker=ZLF27.CBT)
- 2026-11-24 | soja_cbot | abertura: 1227.25 USD/bushel (ticker=ZSF27.CBT)
- 2026-11-24 | soja_cbot | fechamento: 1228.5 USD/bushel (ticker=ZSF27.CBT)
- 2026-11-24 | soja_cbot | fechamento_F27: 1228.5 USD/bushel (ticker=ZSF27.CBT venc=jan/27)
- 2026-11-24 | soja_cbot | fechamento_H27: 1232.75 USD/bushel (ticker=ZSH27.CBT venc=mar/27)
- 2026-11-24 | soja_cbot | fechamento_K27: 1238.75 USD/bushel (ticker=ZSK27.CBT venc=mai/27)
- 2026-11-24 | soja_cbot | fechamento_N27: 1243.0 USD/bushel (ticker=ZSN27.CBT venc=jul/27)
- 2026-11-24 | soja_cbot | fechamento_Q27: 1223.0 USD/bushel (ticker=ZSQ27.CBT venc=ago/27)
- 2026-11-24 | soja_cbot | maxima: 1232.0 USD/bushel (ticker=ZSF27.CBT)
- 2026-11-24 | soja_cbot | minima: 1226.75 USD/bushel (ticker=ZSF27.CBT)
- 2026-11-24 | soja_cbot | volume: 5758.0 contratos (ticker=ZSF27.CBT)
- 2026-11-23 | farelo_cbot | abertura: 340.1000061035156 USD/short_ton (ticker=ZMF27.CBT)
- 2026-11-23 | farelo_cbot | fechamento: 344.5 USD/short_ton (ticker=ZMF27.CBT)
- 2026-11-23 | farelo_cbot | fechamento_F27: 344.5 USD/short_ton (ticker=ZMF27.CBT venc=jan/27)
- 2026-11-23 | farelo_cbot | fechamento_H27: 345.20001220703125 USD/short_ton (ticker=ZMH27.CBT venc=mar/27)
- 2026-11-23 | farelo_cbot | fechamento_K27: 346.3999938964844 USD/short_ton (ticker=ZMK27.CBT venc=mai/27)
- 2026-11-23 | farelo_cbot | fechamento_N27: 348.6000061035156 USD/short_ton (ticker=ZMN27.CBT venc=jul/27)
- 2026-11-23 | farelo_cbot | fechamento_Q27: 346.3999938964844 USD/short_ton (ticker=ZMQ27.CBT venc=ago/27)
- 2026-11-23 | farelo_cbot | fechamento_Z26: 345.70001220703125 USD/short_ton (ticker=ZMZ26.CBT venc=dez/26)
- 2026-11-23 | farelo_cbot | maxima: 344.70001220703125 USD/short_ton (ticker=ZMF27.CBT)
- 2026-11-23 | farelo_cbot | minima: 338.79998779296875 USD/short_ton (ticker=ZMF27.CBT)
- 2026-11-23 | farelo_cbot | volume: 111563.0 contratos (ticker=ZMF27.CBT)
- 2026-11-23 | heating_oil_cbot | abertura: 3.9649999141693115 USD/galão (ticker=HO=F)
- 2026-11-23 | heating_oil_cbot | fechamento: 3.697499990463257 USD/galão (ticker=HO=F)

---

## indicators

- 2026-11-24 | biodiesel_us | custo_oleo_usd_galao: 4.431 USD/galão (7.5 lb × óleo 59.08 cts/lb)
- 2026-11-24 | biodiesel_us | margem_usd_galao: 1.5578 USD/galão (receita 6.79 (HO 3.62 + 1.5×RIN 2.11) − custo 5.23 (óleo 4.43 + ind 0.80))
- 2026-11-24 | biodiesel_us | receita_usd_galao: 6.7888 USD/galão (HO 3.62 + 1.5×RIN 2.11)
- 2026-11-24 | complexo_soja | crush_margin_usd_bu: 1.8258 USD/bushel (Board Crush: farelo 346.00 + oleo 59.08 − soja 1228.50)
- 2026-11-24 | complexo_soja | far_soj_ratio_pct: 84.49 % (farelo 346.00/sht ÷ (soja 1228.50cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-11-24 | complexo_soja | indice_sobra_farelo: 25.0 0-100 (sem sobra relevante (1/4 condições))
- 2026-11-24 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-11-24 | complexo_soja | oil_meal_spread_usd_bu: -1.1132 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-11-24 | complexo_soja | oil_share_pct: 46.06 % (valor oleo 6.50 / total 14.11)
- 2026-11-24 | soja_paridade_br | brl_saca_paridade: 161.71 BRL/saca60kg (CBOT 1228.50 cts × USD/BRL 5.9708 (sem basis))
- 2026-11-23 | biodiesel_us | custo_oleo_usd_galao: 4.4662 USD/galão (7.5 lb × óleo 59.55 cts/lb)
- 2026-11-23 | biodiesel_us | margem_usd_galao: 1.5963 USD/galão (receita 6.86 (HO 3.70 + 1.5×RIN 2.11) − custo 5.27 (óleo 4.47 + ind 0.80))
- 2026-11-23 | biodiesel_us | receita_usd_galao: 6.8625 USD/galão (HO 3.70 + 1.5×RIN 2.11)
- 2026-11-23 | complexo_soja | crush_margin_usd_bu: 1.842 USD/bushel (Board Crush: farelo 344.50 + oleo 59.55 − soja 1228.75)
- 2026-11-23 | complexo_soja | far_soj_ratio_pct: 84.11 % (farelo 344.50/sht ÷ (soja 1228.75cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-11-23 | complexo_soja | indice_sobra_farelo: 25.0 0-100 (sem sobra relevante (1/4 condições))
- 2026-11-23 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-11-23 | complexo_soja | oil_meal_spread_usd_bu: -1.0285 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-11-23 | complexo_soja | oil_share_pct: 46.36 % (valor oleo 6.55 / total 14.13)
- 2026-11-23 | soja_paridade_br | brl_saca_paridade: 161.74 BRL/saca60kg (CBOT 1228.75 cts × USD/BRL 5.9708 (sem basis))
- 2026-11-22 | complexo_soja | indice_sobra_farelo: 25.0 0-100 (sem sobra relevante (1/4 condições))
- 2026-11-22 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-11-21 | complexo_soja | indice_sobra_farelo: 25.0 0-100 (sem sobra relevante (1/4 condições))
- 2026-11-21 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-11-20 | biodiesel_us | custo_oleo_usd_galao: 4.5007 USD/galão (7.5 lb × óleo 60.01 cts/lb)
- 2026-11-20 | biodiesel_us | margem_usd_galao: 1.7859 USD/galão (receita 7.09 (HO 3.92 + 1.5×RIN 2.11) − custo 5.30 (óleo 4.50 + ind 0.80))
- 2026-11-20 | biodiesel_us | receita_usd_galao: 7.0866 USD/galão (HO 3.92 + 1.5×RIN 2.11)
- 2026-11-20 | complexo_soja | crush_margin_usd_bu: 1.8802 USD/bushel (Board Crush: farelo 340.30 + oleo 60.01 − soja 1220.75)
- 2026-11-20 | complexo_soja | far_soj_ratio_pct: 83.63 % (farelo 340.30/sht ÷ (soja 1220.75cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-11-20 | complexo_soja | indice_sobra_farelo: 25.0 0-100 (sem sobra relevante (1/4 condições))
- 2026-11-20 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-11-20 | complexo_soja | oil_meal_spread_usd_bu: -0.8855 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-11-20 | complexo_soja | oil_share_pct: 46.86 % (valor oleo 6.60 / total 14.09)
- 2026-11-20 | soja_paridade_br | brl_saca_paridade: 158.49 BRL/saca60kg (CBOT 1220.75 cts × USD/BRL 5.8889 (sem basis))
- 2026-11-19 | biodiesel_us | custo_oleo_usd_galao: 4.5225 USD/galão (7.5 lb × óleo 60.30 cts/lb)
- 2026-11-19 | biodiesel_us | margem_usd_galao: 1.7939 USD/galão (receita 7.12 (HO 3.95 + 1.5×RIN 2.11) − custo 5.32 (óleo 4.52 + ind 0.80))
- 2026-11-19 | biodiesel_us | receita_usd_galao: 7.1164 USD/galão (HO 3.95 + 1.5×RIN 2.11)
- 2026-11-19 | complexo_soja | crush_margin_usd_bu: 1.8378 USD/bushel (Board Crush: farelo 330.90 + oleo 60.30 − soja 1207.50)
- 2026-11-19 | complexo_soja | far_soj_ratio_pct: 82.21 % (farelo 330.90/sht ÷ (soja 1207.50cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-11-19 | complexo_soja | indice_sobra_farelo: 25.0 0-100 (sem sobra relevante (1/4 condições))
- 2026-11-19 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-11-19 | complexo_soja | oil_meal_spread_usd_bu: -0.6468 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-11-19 | complexo_soja | oil_share_pct: 47.68 % (valor oleo 6.63 / total 13.91)
- 2026-11-19 | soja_paridade_br | brl_saca_paridade: 156.77 BRL/saca60kg (CBOT 1207.50 cts × USD/BRL 5.8889 (sem basis))
- 2026-11-18 | biodiesel_us | custo_oleo_usd_galao: 4.5075 USD/galão (7.5 lb × óleo 60.10 cts/lb)
- 2026-11-18 | biodiesel_us | margem_usd_galao: 1.8298 USD/galão (receita 7.14 (HO 3.97 + 1.5×RIN 2.11) − custo 5.31 (óleo 4.51 + ind 0.80))
- 2026-11-18 | biodiesel_us | receita_usd_galao: 7.1373 USD/galão (HO 3.97 + 1.5×RIN 2.11)
- 2026-11-18 | complexo_soja | crush_margin_usd_bu: 1.7893 USD/bushel (Board Crush: farelo 333.90 + oleo 60.10 − soja 1216.75)
- 2026-11-18 | complexo_soja | far_soj_ratio_pct: 82.33 % (farelo 333.90/sht ÷ (soja 1216.75cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-11-18 | complexo_soja | indice_sobra_farelo: 25.0 0-100 (sem sobra relevante (1/4 condições))

---

## inmet

- 2026-11-25 | cascavel_pr | temp_max_manha: 25.0 C (Cascavel/PR — Encoberto com pancadas de chuva isoladas)
- 2026-11-25 | cascavel_pr | temp_max_noite: 25.0 C (Cascavel/PR — Encoberto)
- 2026-11-25 | cascavel_pr | temp_max_tarde: 25.0 C (Cascavel/PR — Encoberto)
- 2026-11-25 | cascavel_pr | temp_min_manha: 20.0 C (Cascavel/PR — Encoberto com pancadas de chuva isoladas)
- 2026-11-25 | cascavel_pr | temp_min_noite: 20.0 C (Cascavel/PR — Encoberto)
- 2026-11-25 | cascavel_pr | temp_min_tarde: 20.0 C (Cascavel/PR — Encoberto)
- 2026-11-25 | cuiaba_mt | temp_max_manha: 36.0 C (Cuiaba/MT — Nublado com chuvisco)
- 2026-11-25 | cuiaba_mt | temp_max_noite: 36.0 C (Cuiaba/MT — Nublado)
- 2026-11-25 | cuiaba_mt | temp_max_tarde: 36.0 C (Cuiaba/MT — Nublado)
- 2026-11-25 | cuiaba_mt | temp_min_manha: 27.0 C (Cuiaba/MT — Nublado com chuvisco)
- 2026-11-25 | cuiaba_mt | temp_min_noite: 27.0 C (Cuiaba/MT — Nublado)
- 2026-11-25 | cuiaba_mt | temp_min_tarde: 27.0 C (Cuiaba/MT — Nublado)
- 2026-11-25 | lucas_rio_verde_mt | temp_max_manha: 35.0 C (Lucas do Rio Verde/MT — Encoberto com chuvisco)
- 2026-11-25 | lucas_rio_verde_mt | temp_max_noite: 35.0 C (Lucas do Rio Verde/MT — Nublado)
- 2026-11-25 | lucas_rio_verde_mt | temp_max_tarde: 35.0 C (Lucas do Rio Verde/MT — Encoberto)
- 2026-11-25 | lucas_rio_verde_mt | temp_min_manha: 24.0 C (Lucas do Rio Verde/MT — Encoberto com chuvisco)
- 2026-11-25 | lucas_rio_verde_mt | temp_min_noite: 24.0 C (Lucas do Rio Verde/MT — Nublado)
- 2026-11-25 | lucas_rio_verde_mt | temp_min_tarde: 24.0 C (Lucas do Rio Verde/MT — Encoberto)
- 2026-11-25 | maringa_pr | temp_max_manha: 29.0 C (Maringa/PR — Encoberto com pancadas de chuva isoladas)
- 2026-11-25 | maringa_pr | temp_max_noite: 29.0 C (Maringa/PR — Encoberto)
- 2026-11-25 | maringa_pr | temp_max_tarde: 29.0 C (Maringa/PR — Encoberto)
- 2026-11-25 | maringa_pr | temp_min_manha: 23.0 C (Maringa/PR — Encoberto com pancadas de chuva isoladas)
- 2026-11-25 | maringa_pr | temp_min_noite: 23.0 C (Maringa/PR — Encoberto)
- 2026-11-25 | maringa_pr | temp_min_tarde: 23.0 C (Maringa/PR — Encoberto)
- 2026-11-25 | passo_fundo_rs | temp_max_manha: 23.0 C (Passo Fundo/RS — Encoberto)
- 2026-11-25 | passo_fundo_rs | temp_max_noite: 23.0 C (Passo Fundo/RS — Encoberto)
- 2026-11-25 | passo_fundo_rs | temp_max_tarde: 23.0 C (Passo Fundo/RS — Encoberto)
- 2026-11-25 | passo_fundo_rs | temp_min_manha: 13.0 C (Passo Fundo/RS — Encoberto)
- 2026-11-25 | passo_fundo_rs | temp_min_noite: 13.0 C (Passo Fundo/RS — Encoberto)
- 2026-11-25 | passo_fundo_rs | temp_min_tarde: 13.0 C (Passo Fundo/RS — Encoberto)
- 2026-11-25 | rio_verde_go | temp_max_manha: 30.0 C (Rio Verde/GO — Nublado com chuvisco)
- 2026-11-25 | rio_verde_go | temp_max_noite: 30.0 C (Rio Verde/GO — Nublado)
- 2026-11-25 | rio_verde_go | temp_max_tarde: 30.0 C (Rio Verde/GO — Encoberto)
- 2026-11-25 | rio_verde_go | temp_min_manha: 21.0 C (Rio Verde/GO — Nublado com chuvisco)
- 2026-11-25 | rio_verde_go | temp_min_noite: 21.0 C (Rio Verde/GO — Nublado)
- 2026-11-25 | rio_verde_go | temp_min_tarde: 21.0 C (Rio Verde/GO — Encoberto)
- 2026-11-25 | sinop_mt | temp_max_manha: 35.0 C (Sinop/MT — Encoberto com chuvisco)
- 2026-11-25 | sinop_mt | temp_max_noite: 35.0 C (Sinop/MT — Encoberto)
- 2026-11-25 | sinop_mt | temp_max_tarde: 35.0 C (Sinop/MT — Encoberto)
- 2026-11-25 | sinop_mt | temp_min_manha: 23.0 C (Sinop/MT — Encoberto com chuvisco)
- 2026-11-25 | sinop_mt | temp_min_noite: 23.0 C (Sinop/MT — Encoberto)
- 2026-11-25 | sinop_mt | temp_min_tarde: 23.0 C (Sinop/MT — Encoberto)
- 2026-11-25 | sorriso_mt | temp_max_manha: 33.0 C (Sorriso/MT — Encoberto com chuvisco)
- 2026-11-25 | sorriso_mt | temp_max_noite: 33.0 C (Sorriso/MT — Encoberto)
- 2026-11-25 | sorriso_mt | temp_max_tarde: 33.0 C (Sorriso/MT — Encoberto)
- 2026-11-25 | sorriso_mt | temp_min_manha: 23.0 C (Sorriso/MT — Encoberto com chuvisco)
- 2026-11-25 | sorriso_mt | temp_min_noite: 23.0 C (Sorriso/MT — Encoberto)
- 2026-11-25 | sorriso_mt | temp_min_tarde: 23.0 C (Sorriso/MT — Encoberto)
- 2026-11-24 | cascavel_pr | temp_max_manha: 29.0 C (Cascavel/PR — Muitas nuvens com chuva)
- 2026-11-24 | cascavel_pr | temp_max_noite: 29.0 C (Cascavel/PR — Muitas nuvens com pancadas de chuva e trovoadas isoladas)

---

## mpob

- 2026-11-24 | palma_malasia | page_fetched: 3209.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-23 | palma_malasia | page_fetched: 3209.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-22 | palma_malasia | page_fetched: 3209.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-21 | palma_malasia | page_fetched: 3209.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-20 | palma_malasia | page_fetched: 3209.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-19 | palma_malasia | page_fetched: 3209.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-18 | palma_malasia | page_fetched: 3209.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-17 | palma_malasia | page_fetched: 3209.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-16 | palma_malasia | page_fetched: 3209.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-15 | palma_malasia | page_fetched: 3209.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-14 | palma_malasia | page_fetched: 3209.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-13 | palma_malasia | page_fetched: 3209.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-12 | palma_malasia | page_fetched: 3209.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-11 | palma_malasia | page_fetched: 3209.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-10 | palma_malasia | page_fetched: 3208.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)

---

## noaa_cpc

- 2026-11-24 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-23 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-22 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-21 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-20 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-19 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-18 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-17 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-16 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-15 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-14 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-13 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-12 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-11 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-10 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)

---

## nopa

- 2026-11-24 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-23 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-22 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-21 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-20 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-19 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-18 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-17 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-16 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-15 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-14 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-13 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-12 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-11 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-10 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)

---

## noticias_rss

- 2026-11-24 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-23 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-22 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-21 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-20 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-19 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-18 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-17 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-16 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-15 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-14 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-13 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-12 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-11 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-10 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))

---

## usda_crop_progress

- 2026-11-15 | soybeans_eua | pct_harvested: 96.0 % (SOYBEANS - PROGRESS, MEASURED IN PCT HARVESTED)

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
| 2026-11-24 | 7d | 2026-12-01 | farelo_cbot | 346.00 | 333.19 | 349.76 | 366.34 | altista |
| 2026-11-24 | 7d | 2026-12-01 | oleo_cbot | 59.08 | 54.73 | 57.46 | 60.20 | baixista |
| 2026-11-24 | 7d | 2026-12-01 | soja_cbot | 1228.50 | 1184.93 | 1227.87 | 1270.82 | lateral |
| 2026-11-24 | 30d | 2026-12-24 | farelo_cbot | 346.00 | 332.19 | 366.50 | 400.81 | altista |
| 2026-11-24 | 30d | 2026-12-24 | oleo_cbot | 59.08 | 45.56 | 51.22 | 56.87 | baixista |
| 2026-11-24 | 30d | 2026-12-24 | soja_cbot | 1228.50 | 1139.33 | 1228.24 | 1317.15 | lateral |
| 2026-11-23 | 7d | 2026-11-30 | farelo_cbot | 344.50 | 326.55 | 342.80 | 359.05 | lateral |
| 2026-11-23 | 7d | 2026-11-30 | oleo_cbot | 59.55 | 55.76 | 58.60 | 61.44 | baixista |
| 2026-11-23 | 7d | 2026-11-30 | soja_cbot | 1228.75 | 1179.92 | 1223.32 | 1266.72 | lateral |
| 2026-11-23 | 30d | 2026-12-23 | farelo_cbot | 344.50 | 317.78 | 351.42 | 385.06 | altista |
| 2026-11-23 | 30d | 2026-12-23 | oleo_cbot | 59.55 | 46.55 | 52.43 | 58.32 | baixista |
| 2026-11-23 | 30d | 2026-12-23 | soja_cbot | 1228.75 | 1122.50 | 1212.34 | 1302.19 | baixista |
| 2026-11-22 | 7d | 2026-11-29 | farelo_cbot | 340.30 | 322.88 | 339.32 | 355.77 | lateral |
| 2026-11-22 | 7d | 2026-11-29 | oleo_cbot | 60.01 | 55.56 | 58.42 | 61.28 | baixista |
| 2026-11-22 | 7d | 2026-11-29 | soja_cbot | 1220.75 | 1170.61 | 1214.01 | 1257.41 | baixista |
| 2026-11-22 | 30d | 2026-12-22 | farelo_cbot | 340.30 | 305.22 | 339.26 | 373.30 | lateral |
| 2026-11-22 | 30d | 2026-12-22 | oleo_cbot | 60.01 | 46.39 | 52.30 | 58.22 | baixista |
| 2026-11-22 | 30d | 2026-12-22 | soja_cbot | 1220.75 | 1102.03 | 1191.88 | 1281.73 | baixista |
| 2026-11-21 | 7d | 2026-11-28 | farelo_cbot | 340.30 | 322.77 | 339.14 | 355.50 | lateral |
| 2026-11-21 | 7d | 2026-11-28 | oleo_cbot | 60.01 | 55.55 | 58.41 | 61.27 | baixista |
| 2026-11-21 | 7d | 2026-11-28 | soja_cbot | 1220.75 | 1170.43 | 1213.78 | 1257.12 | baixista |
| 2026-11-21 | 30d | 2026-12-21 | farelo_cbot | 340.30 | 305.18 | 339.07 | 372.95 | lateral |
| 2026-11-21 | 30d | 2026-12-21 | oleo_cbot | 60.01 | 46.38 | 52.29 | 58.21 | baixista |
| 2026-11-21 | 30d | 2026-12-21 | soja_cbot | 1220.75 | 1101.91 | 1191.64 | 1281.37 | baixista |

---


---

# Fila de julgamento — 2026-11-24

**8 item(ns).** Frase-gatilho: "lê a fila de julgamento e trata"

## 🔴 [nivel_tese] soja_cbot fechou em 1228.50 — acima da resistencia 1180.00
- id: `alerta-quebra_resistencia-soja_cbot-2026-11-24`
- fato: soja_cbot = 1228.50 vs nivel 1180.00 (2026-11-24)
- refs: soja_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] oleo_cbot fechou em 59.08 — abaixo do suporte 72.00
- id: `alerta-quebra_suporte-oleo_cbot-2026-11-24`
- fato: oleo_cbot = 59.08 vs nivel 72.00 (2026-11-24)
- refs: oleo_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] farelo_cbot fechou em 346.00 — acima da resistencia 325.00
- id: `alerta-quebra_resistencia-farelo_cbot-2026-11-24`
- fato: farelo_cbot = 346.00 vs nivel 325.00 (2026-11-24)
- refs: farelo_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] usd_brl_ptax fechou em 5.97 — acima da resistencia 5.30
- id: `alerta-quebra_resistencia-usd_brl_ptax-2026-11-23`
- fato: usd_brl_ptax = 5.97 vs nivel 5.30 (2026-11-23)
- refs: usd_brl_ptax
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] complexo_soja fechou em 1.83 — abaixo do suporte 2.50
- id: `alerta-quebra_suporte-complexo_soja-2026-11-24`
- fato: complexo_soja = 1.83 vs nivel 2.50 (2026-11-24)
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

## 🟡 [release] NOPA novo (2026-11-24)
- id: `release-nopa-2026-11-24`
- fato: fonte nopa com data 2026-11-24 — coletado, ainda nao interpretado
- refs: complexo_soja
- leitura: O numero muda o balanco/tese? Algo relevante pro farelo?

---
Trate só 🔴/🟡. Saída = `insights/*.md` (formato de generate_insights.txt, com `vies:`). Cite o `id` da fila no corpo do insight. Máx 1-3. Não duplicar insight recente.
