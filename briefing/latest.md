# Briefing consolidado — 2026-11-26

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

- 2026-11-26 | anec | links_relatorios: 0.0 count (Nenhum link de relatorio encontrado na pagina /estatisticas/. Estrutura pode ter mudado.)
- 2026-11-25 | anec | links_relatorios: 0.0 count (Nenhum link de relatorio encontrado na pagina /estatisticas/. Estrutura pode ter mudado.)
- 2026-11-24 | anec | links_relatorios: 0.0 count (Nenhum link de relatorio encontrado na pagina /estatisticas/. Estrutura pode ter mudado.)
- 2026-11-23 | anec | links_relatorios: 0.0 count (Nenhum link de relatorio encontrado na pagina /estatisticas/. Estrutura pode ter mudado.)
- 2026-11-22 | anec | links_relatorios: 0.0 count (Nenhum link de relatorio encontrado na pagina /estatisticas/. Estrutura pode ter mudado.)
- 2026-11-21 | anec | links_relatorios: 0.0 count (Nenhum link de relatorio encontrado na pagina /estatisticas/. Estrutura pode ter mudado.)
- 2026-11-20 | anec | links_relatorios: 0.0 count (Nenhum link de relatorio encontrado na pagina /estatisticas/. Estrutura pode ter mudado.)
- 2026-11-19 | anec | links_relatorios: 0.0 count (Nenhum link de relatorio encontrado na pagina /estatisticas/. Estrutura pode ter mudado.)
- 2026-11-18 | anec | links_relatorios: 0.0 count (Nenhum link de relatorio encontrado na pagina /estatisticas/. Estrutura pode ter mudado.)

---

## bcb

- 2026-11-25 | eur_brl_ptax | valor: 6.4413 BRL/EUR (sgs=21619)
- 2026-11-25 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-11-25 | usd_brl_ptax | valor: 5.8825 BRL/USD (sgs=1)
- 2026-11-24 | eur_brl_ptax | valor: 6.426 BRL/EUR (sgs=21619)
- 2026-11-24 | selic_diaria | valor: 0.050788 % a.a. (sgs=11)
- 2026-11-24 | usd_brl_ptax | valor: 5.8573 BRL/USD (sgs=1)
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

---

## cme_cbot

- 2026-11-26 | heating_oil_cbot | abertura: 3.65310001373291 USD/galão (ticker=HO=F)
- 2026-11-26 | heating_oil_cbot | fechamento: 3.669800043106079 USD/galão (ticker=HO=F)
- 2026-11-26 | heating_oil_cbot | maxima: 3.6733999252319336 USD/galão (ticker=HO=F)
- 2026-11-26 | heating_oil_cbot | minima: 3.643399953842163 USD/galão (ticker=HO=F)
- 2026-11-26 | heating_oil_cbot | volume: 534.0 contratos (ticker=HO=F)
- 2026-11-25 | farelo_cbot | abertura: 351.0 USD/short_ton (ticker=ZMF27.CBT)
- 2026-11-25 | farelo_cbot | fechamento: 358.1000061035156 USD/short_ton (ticker=ZMF27.CBT)
- 2026-11-25 | farelo_cbot | fechamento_F27: 358.1000061035156 USD/short_ton (ticker=ZMF27.CBT venc=jan/27)
- 2026-11-25 | farelo_cbot | fechamento_H27: 356.79998779296875 USD/short_ton (ticker=ZMH27.CBT venc=mar/27)
- 2026-11-25 | farelo_cbot | fechamento_K27: 356.6000061035156 USD/short_ton (ticker=ZMK27.CBT venc=mai/27)
- 2026-11-25 | farelo_cbot | fechamento_N27: 357.8999938964844 USD/short_ton (ticker=ZMN27.CBT venc=jul/27)
- 2026-11-25 | farelo_cbot | fechamento_Q27: 354.29998779296875 USD/short_ton (ticker=ZMQ27.CBT venc=ago/27)
- 2026-11-25 | farelo_cbot | fechamento_Z26: 361.70001220703125 USD/short_ton (ticker=ZMZ26.CBT venc=dez/26)
- 2026-11-25 | farelo_cbot | maxima: 358.5 USD/short_ton (ticker=ZMF27.CBT)
- 2026-11-25 | farelo_cbot | minima: 347.79998779296875 USD/short_ton (ticker=ZMF27.CBT)
- 2026-11-25 | farelo_cbot | volume: 114045.0 contratos (ticker=ZMF27.CBT)
- 2026-11-25 | heating_oil_cbot | abertura: 3.7032999992370605 USD/galão (ticker=HO=F)
- 2026-11-25 | heating_oil_cbot | fechamento: 3.702500104904175 USD/galão (ticker=HO=F)
- 2026-11-25 | heating_oil_cbot | maxima: 3.744499921798706 USD/galão (ticker=HO=F)
- 2026-11-25 | heating_oil_cbot | minima: 3.616300106048584 USD/galão (ticker=HO=F)
- 2026-11-25 | heating_oil_cbot | volume: 21070.0 contratos (ticker=HO=F)
- 2026-11-25 | oleo_cbot | abertura: 58.150001525878906 USD_cts/lb (ticker=ZLF27.CBT)
- 2026-11-25 | oleo_cbot | fechamento: 58.2599983215332 USD_cts/lb (ticker=ZLF27.CBT)
- 2026-11-25 | oleo_cbot | fechamento_F27: 58.2599983215332 USD_cts/lb (ticker=ZLF27.CBT venc=jan/27)
- 2026-11-25 | oleo_cbot | fechamento_H27: 58.75 USD_cts/lb (ticker=ZLH27.CBT venc=mar/27)
- 2026-11-25 | oleo_cbot | fechamento_K27: 59.2599983215332 USD_cts/lb (ticker=ZLK27.CBT venc=mai/27)
- 2026-11-25 | oleo_cbot | fechamento_N27: 59.59000015258789 USD_cts/lb (ticker=ZLN27.CBT venc=jul/27)
- 2026-11-25 | oleo_cbot | fechamento_Q27: 59.47999954223633 USD_cts/lb (ticker=ZLQ27.CBT venc=ago/27)
- 2026-11-25 | oleo_cbot | fechamento_Z26: 58.0099983215332 USD_cts/lb (ticker=ZLZ26.CBT venc=dez/26)
- 2026-11-25 | oleo_cbot | maxima: 58.7400016784668 USD_cts/lb (ticker=ZLF27.CBT)
- 2026-11-25 | oleo_cbot | minima: 57.560001373291016 USD_cts/lb (ticker=ZLF27.CBT)
- 2026-11-25 | oleo_cbot | volume: 94669.0 contratos (ticker=ZLF27.CBT)
- 2026-11-25 | soja_cbot | abertura: 1233.75 USD/bushel (ticker=ZSF27.CBT)
- 2026-11-25 | soja_cbot | fechamento: 1243.25 USD/bushel (ticker=ZSF27.CBT)
- 2026-11-25 | soja_cbot | fechamento_F27: 1243.25 USD/bushel (ticker=ZSF27.CBT venc=jan/27)
- 2026-11-25 | soja_cbot | fechamento_H27: 1244.25 USD/bushel (ticker=ZSH27.CBT venc=mar/27)
- 2026-11-25 | soja_cbot | fechamento_K27: 1248.5 USD/bushel (ticker=ZSK27.CBT venc=mai/27)
- 2026-11-25 | soja_cbot | fechamento_N27: 1251.5 USD/bushel (ticker=ZSN27.CBT venc=jul/27)
- 2026-11-25 | soja_cbot | fechamento_Q27: 1231.75 USD/bushel (ticker=ZSQ27.CBT venc=ago/27)
- 2026-11-25 | soja_cbot | maxima: 1247.25 USD/bushel (ticker=ZSF27.CBT)
- 2026-11-25 | soja_cbot | minima: 1220.5 USD/bushel (ticker=ZSF27.CBT)
- 2026-11-25 | soja_cbot | volume: 122801.0 contratos (ticker=ZSF27.CBT)
- 2026-11-24 | farelo_cbot | abertura: 344.1000061035156 USD/short_ton (ticker=ZMF27.CBT)
- 2026-11-24 | farelo_cbot | fechamento: 351.1000061035156 USD/short_ton (ticker=ZMF27.CBT)
- 2026-11-24 | farelo_cbot | fechamento_F27: 351.1000061035156 USD/short_ton (ticker=ZMF27.CBT venc=jan/27)
- 2026-11-24 | farelo_cbot | fechamento_H27: 351.3999938964844 USD/short_ton (ticker=ZMH27.CBT venc=mar/27)
- 2026-11-24 | farelo_cbot | fechamento_K27: 352.29998779296875 USD/short_ton (ticker=ZMK27.CBT venc=mai/27)
- 2026-11-24 | farelo_cbot | fechamento_N27: 354.20001220703125 USD/short_ton (ticker=ZMN27.CBT venc=jul/27)
- 2026-11-24 | farelo_cbot | fechamento_Q27: 351.8999938964844 USD/short_ton (ticker=ZMQ27.CBT venc=ago/27)
- 2026-11-24 | farelo_cbot | fechamento_Z26: 353.0 USD/short_ton (ticker=ZMZ26.CBT venc=dez/26)

---

## indicators

- 2026-11-26 | complexo_soja | indice_sobra_farelo: 25.0 0-100 (sem sobra relevante (1/4 condições))
- 2026-11-26 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-11-25 | biodiesel_us | custo_oleo_usd_galao: 4.3695 USD/galão (7.5 lb × óleo 58.26 cts/lb)
- 2026-11-25 | biodiesel_us | margem_usd_galao: 1.698 USD/galão (receita 6.87 (HO 3.70 + 1.5×RIN 2.11) − custo 5.17 (óleo 4.37 + ind 0.80))
- 2026-11-25 | biodiesel_us | receita_usd_galao: 6.8675 USD/galão (HO 3.70 + 1.5×RIN 2.11)
- 2026-11-25 | complexo_soja | crush_margin_usd_bu: 1.8543 USD/bushel (Board Crush: farelo 358.10 + oleo 58.26 − soja 1243.25)
- 2026-11-25 | complexo_soja | far_soj_ratio_pct: 86.41 % (farelo 358.10/sht ÷ (soja 1243.25cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-11-25 | complexo_soja | indice_sobra_farelo: 25.0 0-100 (sem sobra relevante (1/4 condições))
- 2026-11-25 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-11-25 | complexo_soja | oil_meal_spread_usd_bu: -1.4696 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-11-25 | complexo_soja | oil_share_pct: 44.86 % (valor oleo 6.41 / total 14.29)
- 2026-11-25 | soja_paridade_br | brl_saca_paridade: 161.23 BRL/saca60kg (CBOT 1243.25 cts × USD/BRL 5.8825 (sem basis))
- 2026-11-24 | biodiesel_us | custo_oleo_usd_galao: 4.374 USD/galão (7.5 lb × óleo 58.32 cts/lb)
- 2026-11-24 | biodiesel_us | margem_usd_galao: 1.694 USD/galão (receita 6.87 (HO 3.70 + 1.5×RIN 2.11) − custo 5.17 (óleo 4.37 + ind 0.80))
- 2026-11-24 | biodiesel_us | receita_usd_galao: 6.868 USD/galão (HO 3.70 + 1.5×RIN 2.11)
- 2026-11-24 | complexo_soja | crush_margin_usd_bu: 1.7994 USD/bushel (Board Crush: farelo 351.10 + oleo 58.32 − soja 1234.00)
- 2026-11-24 | complexo_soja | far_soj_ratio_pct: 85.36 % (farelo 351.10/sht ÷ (soja 1234.00cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-11-24 | complexo_soja | indice_sobra_farelo: 25.0 0-100 (sem sobra relevante (1/4 condições))
- 2026-11-24 | complexo_soja | indice_suporte_oleo: 60.0 0-100 (suporte relevante (3/5 condições))
- 2026-11-24 | complexo_soja | oil_meal_spread_usd_bu: -1.309 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-11-24 | complexo_soja | oil_share_pct: 45.37 % (valor oleo 6.42 / total 14.14)
- 2026-11-24 | soja_paridade_br | brl_saca_paridade: 159.35 BRL/saca60kg (CBOT 1234.00 cts × USD/BRL 5.8573 (sem basis))
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

---

## inmet

- 2026-11-27 | cascavel_pr | temp_max_manha: 20.0 C (Cascavel/PR — Encoberto com pancadas de chuva isoladas)
- 2026-11-27 | cascavel_pr | temp_max_noite: 20.0 C (Cascavel/PR — Encoberto com chuvisco)
- 2026-11-27 | cascavel_pr | temp_max_tarde: 20.0 C (Cascavel/PR — Encoberto com chuvisco)
- 2026-11-27 | cascavel_pr | temp_min_manha: 17.0 C (Cascavel/PR — Encoberto com pancadas de chuva isoladas)
- 2026-11-27 | cascavel_pr | temp_min_noite: 17.0 C (Cascavel/PR — Encoberto com chuvisco)
- 2026-11-27 | cascavel_pr | temp_min_tarde: 17.0 C (Cascavel/PR — Encoberto com chuvisco)
- 2026-11-27 | cuiaba_mt | temp_max_manha: 31.0 C (Cuiaba/MT — Encoberto com pancadas de chuva isoladas)
- 2026-11-27 | cuiaba_mt | temp_max_noite: 31.0 C (Cuiaba/MT — Encoberto com chuvisco)
- 2026-11-27 | cuiaba_mt | temp_max_tarde: 31.0 C (Cuiaba/MT — Encoberto)
- 2026-11-27 | cuiaba_mt | temp_min_manha: 26.0 C (Cuiaba/MT — Encoberto com pancadas de chuva isoladas)
- 2026-11-27 | cuiaba_mt | temp_min_noite: 26.0 C (Cuiaba/MT — Encoberto com chuvisco)
- 2026-11-27 | cuiaba_mt | temp_min_tarde: 26.0 C (Cuiaba/MT — Encoberto)
- 2026-11-27 | lucas_rio_verde_mt | temp_max_manha: 33.0 C (Lucas do Rio Verde/MT — Encoberto com chuvisco)
- 2026-11-27 | lucas_rio_verde_mt | temp_max_noite: 33.0 C (Lucas do Rio Verde/MT — Encoberto)
- 2026-11-27 | lucas_rio_verde_mt | temp_max_tarde: 33.0 C (Lucas do Rio Verde/MT — Encoberto)
- 2026-11-27 | lucas_rio_verde_mt | temp_min_manha: 24.0 C (Lucas do Rio Verde/MT — Encoberto com chuvisco)
- 2026-11-27 | lucas_rio_verde_mt | temp_min_noite: 24.0 C (Lucas do Rio Verde/MT — Encoberto)
- 2026-11-27 | lucas_rio_verde_mt | temp_min_tarde: 24.0 C (Lucas do Rio Verde/MT — Encoberto)
- 2026-11-27 | maringa_pr | temp_max_manha: 24.0 C (Maringa/PR — Encoberto com chuvisco)
- 2026-11-27 | maringa_pr | temp_max_noite: 24.0 C (Maringa/PR — Encoberto com chuvisco)
- 2026-11-27 | maringa_pr | temp_max_tarde: 24.0 C (Maringa/PR — Encoberto)
- 2026-11-27 | maringa_pr | temp_min_manha: 19.0 C (Maringa/PR — Encoberto com chuvisco)
- 2026-11-27 | maringa_pr | temp_min_noite: 19.0 C (Maringa/PR — Encoberto com chuvisco)
- 2026-11-27 | maringa_pr | temp_min_tarde: 19.0 C (Maringa/PR — Encoberto)
- 2026-11-27 | passo_fundo_rs | temp_max_manha: 23.0 C (Passo Fundo/RS — Encoberto com chuvisco)
- 2026-11-27 | passo_fundo_rs | temp_max_noite: 23.0 C (Passo Fundo/RS — Encoberto)
- 2026-11-27 | passo_fundo_rs | temp_max_tarde: 23.0 C (Passo Fundo/RS — Encoberto com chuvisco)
- 2026-11-27 | passo_fundo_rs | temp_min_manha: 14.0 C (Passo Fundo/RS — Encoberto com chuvisco)
- 2026-11-27 | passo_fundo_rs | temp_min_noite: 14.0 C (Passo Fundo/RS — Encoberto)
- 2026-11-27 | passo_fundo_rs | temp_min_tarde: 14.0 C (Passo Fundo/RS — Encoberto com chuvisco)
- 2026-11-27 | rio_verde_go | temp_max_manha: 28.0 C (Rio Verde/GO — Encoberto com pancadas de chuva isoladas)
- 2026-11-27 | rio_verde_go | temp_max_noite: 28.0 C (Rio Verde/GO — Encoberto com pancadas de chuva isoladas)
- 2026-11-27 | rio_verde_go | temp_max_tarde: 28.0 C (Rio Verde/GO — Encoberto com pancadas de chuva e trovoadas isoladas)
- 2026-11-27 | rio_verde_go | temp_min_manha: 23.0 C (Rio Verde/GO — Encoberto com pancadas de chuva isoladas)
- 2026-11-27 | rio_verde_go | temp_min_noite: 23.0 C (Rio Verde/GO — Encoberto com pancadas de chuva isoladas)
- 2026-11-27 | rio_verde_go | temp_min_tarde: 23.0 C (Rio Verde/GO — Encoberto com pancadas de chuva e trovoadas isoladas)
- 2026-11-27 | sinop_mt | temp_max_manha: 34.0 C (Sinop/MT — Encoberto com chuvisco)
- 2026-11-27 | sinop_mt | temp_max_noite: 34.0 C (Sinop/MT — Encoberto)
- 2026-11-27 | sinop_mt | temp_max_tarde: 34.0 C (Sinop/MT — Encoberto)
- 2026-11-27 | sinop_mt | temp_min_manha: 24.0 C (Sinop/MT — Encoberto com chuvisco)
- 2026-11-27 | sinop_mt | temp_min_noite: 24.0 C (Sinop/MT — Encoberto)
- 2026-11-27 | sinop_mt | temp_min_tarde: 24.0 C (Sinop/MT — Encoberto)
- 2026-11-27 | sorriso_mt | temp_max_manha: 33.0 C (Sorriso/MT — Encoberto com chuvisco)
- 2026-11-27 | sorriso_mt | temp_max_noite: 33.0 C (Sorriso/MT — Encoberto)
- 2026-11-27 | sorriso_mt | temp_max_tarde: 33.0 C (Sorriso/MT — Encoberto)
- 2026-11-27 | sorriso_mt | temp_min_manha: 24.0 C (Sorriso/MT — Encoberto com chuvisco)
- 2026-11-27 | sorriso_mt | temp_min_noite: 24.0 C (Sorriso/MT — Encoberto)
- 2026-11-27 | sorriso_mt | temp_min_tarde: 24.0 C (Sorriso/MT — Encoberto)
- 2026-11-26 | cascavel_pr | temp_max_manha: 26.0 C (Cascavel/PR — Muitas nuvens com possibilidade de chuva isolada)
- 2026-11-26 | cascavel_pr | temp_max_noite: 26.0 C (Cascavel/PR — Muitas nuvens com pancadas de chuva isoladas)

---

## mpob

- 2026-11-26 | palma_malasia | page_fetched: 3209.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-11-25 | palma_malasia | page_fetched: 3209.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
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

---

## noaa_cpc

- 2026-11-26 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-11-25 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
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

---

## nopa

- 2026-11-26 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-11-25 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
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

---

## noticias_rss

- 2026-11-26 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
- 2026-11-25 | noticias | items_fetched: 0.0 items (0 items lidos, 0 mantidos (soja/farelo/oleo))
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

---

## usda_crop_progress

- 2026-11-15 | soybeans_eua | pct_harvested: 96.0 % (SOYBEANS - PROGRESS, MEASURED IN PCT HARVESTED)

---

# FORECASTS ATIVOS (bandas estatisticas)

Bandas calculadas via MA20+volatilidade+slope curto. Claude Code DEVE refinar com drivers fundamentais.

| Geracao | Horizonte | Alvo | Commodity | Spot ref | Baixo | Central | Alto | Vies |
|---|---|---|---|---|---|---|---|---|
| 2026-11-26 | 7d | 2026-12-03 | farelo_cbot | 358.10 | 345.97 | 364.20 | 382.42 | altista |
| 2026-11-26 | 7d | 2026-12-03 | oleo_cbot | 58.26 | 53.76 | 56.49 | 59.23 | baixista |
| 2026-11-26 | 7d | 2026-12-03 | soja_cbot | 1243.25 | 1201.41 | 1245.19 | 1288.97 | lateral |
| 2026-11-26 | 30d | 2026-12-26 | farelo_cbot | 358.10 | 353.56 | 391.29 | 429.01 | altista |
| 2026-11-26 | 30d | 2026-12-26 | oleo_cbot | 58.26 | 43.97 | 49.63 | 55.30 | baixista |
| 2026-11-26 | 30d | 2026-12-26 | soja_cbot | 1243.25 | 1166.92 | 1257.56 | 1348.19 | altista |
| 2026-11-25 | 7d | 2026-12-02 | farelo_cbot | 358.10 | 339.66 | 356.82 | 373.98 | altista |
| 2026-11-25 | 7d | 2026-12-02 | oleo_cbot | 58.26 | 53.33 | 56.04 | 58.76 | baixista |
| 2026-11-25 | 7d | 2026-12-02 | soja_cbot | 1243.25 | 1185.68 | 1228.39 | 1271.09 | lateral |
| 2026-11-25 | 30d | 2026-12-25 | farelo_cbot | 358.10 | 348.23 | 383.75 | 419.28 | altista |
| 2026-11-25 | 30d | 2026-12-25 | oleo_cbot | 58.26 | 43.56 | 49.18 | 54.80 | baixista |
| 2026-11-25 | 30d | 2026-12-25 | soja_cbot | 1243.25 | 1151.98 | 1240.39 | 1328.80 | altista |
| 2026-11-24 | 7d | 2026-12-01 | farelo_cbot | 351.10 | 333.19 | 349.76 | 366.34 | altista |
| 2026-11-24 | 7d | 2026-12-01 | oleo_cbot | 58.32 | 54.73 | 57.46 | 60.20 | baixista |
| 2026-11-24 | 7d | 2026-12-01 | soja_cbot | 1234.00 | 1184.93 | 1227.87 | 1270.82 | lateral |
| 2026-11-24 | 30d | 2026-12-24 | farelo_cbot | 351.10 | 332.19 | 366.50 | 400.81 | altista |
| 2026-11-24 | 30d | 2026-12-24 | oleo_cbot | 58.32 | 45.56 | 51.22 | 56.87 | baixista |
| 2026-11-24 | 30d | 2026-12-24 | soja_cbot | 1234.00 | 1139.33 | 1228.24 | 1317.15 | lateral |
| 2026-11-23 | 7d | 2026-11-30 | farelo_cbot | 344.50 | 326.55 | 342.80 | 359.05 | lateral |
| 2026-11-23 | 7d | 2026-11-30 | oleo_cbot | 59.55 | 55.76 | 58.60 | 61.44 | baixista |
| 2026-11-23 | 7d | 2026-11-30 | soja_cbot | 1228.75 | 1179.92 | 1223.32 | 1266.72 | lateral |
| 2026-11-23 | 30d | 2026-12-23 | farelo_cbot | 344.50 | 317.78 | 351.42 | 385.06 | altista |
| 2026-11-23 | 30d | 2026-12-23 | oleo_cbot | 59.55 | 46.55 | 52.43 | 58.32 | baixista |
| 2026-11-23 | 30d | 2026-12-23 | soja_cbot | 1228.75 | 1122.50 | 1212.34 | 1302.19 | baixista |

---


---

# Fila de julgamento — 2026-11-26

**8 item(ns).** Frase-gatilho: "lê a fila de julgamento e trata"

## 🔴 [nivel_tese] soja_cbot fechou em 1243.25 — acima da resistencia 1180.00
- id: `alerta-quebra_resistencia-soja_cbot-2026-11-25`
- fato: soja_cbot = 1243.25 vs nivel 1180.00 (2026-11-25)
- refs: soja_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] oleo_cbot fechou em 58.26 — abaixo do suporte 72.00
- id: `alerta-quebra_suporte-oleo_cbot-2026-11-25`
- fato: oleo_cbot = 58.26 vs nivel 72.00 (2026-11-25)
- refs: oleo_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] farelo_cbot fechou em 358.10 — acima da resistencia 325.00
- id: `alerta-quebra_resistencia-farelo_cbot-2026-11-25`
- fato: farelo_cbot = 358.10 vs nivel 325.00 (2026-11-25)
- refs: farelo_cbot
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] usd_brl_ptax fechou em 5.88 — acima da resistencia 5.30
- id: `alerta-quebra_resistencia-usd_brl_ptax-2026-11-25`
- fato: usd_brl_ptax = 5.88 vs nivel 5.30 (2026-11-25)
- refs: usd_brl_ptax
- leitura: Confirma ou muda a tese? O que voce faria diferente sabendo disso?

## 🔴 [nivel_tese] complexo_soja fechou em 1.85 — abaixo do suporte 2.50
- id: `alerta-quebra_suporte-complexo_soja-2026-11-25`
- fato: complexo_soja = 1.85 vs nivel 2.50 (2026-11-25)
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

## 🟡 [release] NOPA novo (2026-11-26)
- id: `release-nopa-2026-11-26`
- fato: fonte nopa com data 2026-11-26 — coletado, ainda nao interpretado
- refs: complexo_soja
- leitura: O numero muda o balanco/tese? Algo relevante pro farelo?

---
Trate só 🔴/🟡. Saída = `insights/*.md` (formato de generate_insights.txt, com `vies:`). Cite o `id` da fila no corpo do insight. Máx 1-3. Não duplicar insight recente.
