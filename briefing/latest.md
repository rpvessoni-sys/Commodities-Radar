# Briefing consolidado — 2026-06-17

_Base 100% publica (CBOT/BCB/CEPEA/NAG/USDA/COT/clima) + notas manuais do consultor._

## O que fazer com este briefing

- **Tratar a fila de julgamento** (camada de LEITURA): rode `python main.py queue`, siga `system/prompts/treat_queue.txt` e escreva so `insights/*.md` (com `vies:`).
- **Sintese narrativa do dia** (opcional): siga `system/prompts/synthesize_daily.txt`.
- Numeros SEMPRE com fonte + data. Aplicar a lente tributaria BR antes de concluir tese de preco.
- NUNCA escrever em numero/indicador/DB/alerts_config — opiniao so vai pra `insights/*.md`.

Notas manuais disponiveis: 0 do consultor · 1 de call.

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
- 2026-10-01 | farelo_brasil | estoque_final: 1100.1295542061137 mil_t (ABIOVE projecoes_mensais | farelo | mes 10/2026)
- 2026-10-01 | farelo_brasil | estoque_inicial: 1016.3182259520293 mil_t (ABIOVE projecoes_mensais | farelo | mes 10/2026)
- 2026-10-01 | farelo_brasil | exportacao: 850.0 mil_t (ABIOVE projecoes_mensais | farelo | mes 10/2026)
- 2026-10-01 | farelo_brasil | producao: 2142.967360155052 mil_t (ABIOVE projecoes_mensais | farelo | mes 10/2026)
- 2026-10-01 | oleo_brasil | estoque_final: 306.38063039798806 mil_t (ABIOVE projecoes_mensais | oleo | mes 10/2026)
- 2026-10-01 | oleo_brasil | estoque_inicial: 286.9442352727726 mil_t (ABIOVE projecoes_mensais | oleo | mes 10/2026)
- 2026-10-01 | oleo_brasil | exportacao: 45.0 mil_t (ABIOVE projecoes_mensais | oleo | mes 10/2026)
- 2026-10-01 | oleo_brasil | producao: 536.2938007461164 mil_t (ABIOVE projecoes_mensais | oleo | mes 10/2026)
- 2026-10-01 | soja_brasil | esmagamento: 2846.290909174032 mil_t (ABIOVE projecoes_mensais | soja | mes 10/2026)
- 2026-10-01 | soja_brasil | estoque_final: 5720.771106475192 mil_t (ABIOVE projecoes_mensais | soja | mes 10/2026)
- 2026-10-01 | soja_brasil | estoque_inicial: 7912.141317419317 mil_t (ABIOVE projecoes_mensais | soja | mes 10/2026)
- 2026-10-01 | soja_brasil | exportacao: 300.0 mil_t (ABIOVE projecoes_mensais | soja | mes 10/2026)
- 2026-09-01 | farelo_brasil | estoque_final: 1016.3182259520293 mil_t (ABIOVE projecoes_mensais | farelo | mes 09/2026)
- 2026-09-01 | farelo_brasil | estoque_inicial: 1224.2300783008761 mil_t (ABIOVE projecoes_mensais | farelo | mes 09/2026)
- 2026-09-01 | farelo_brasil | exportacao: 1100.0 mil_t (ABIOVE projecoes_mensais | farelo | mes 09/2026)
- 2026-09-01 | farelo_brasil | producao: 2128.553432567879 mil_t (ABIOVE projecoes_mensais | farelo | mes 09/2026)
- 2026-09-01 | oleo_brasil | estoque_final: 286.9442352727726 mil_t (ABIOVE projecoes_mensais | oleo | mes 09/2026)
- 2026-09-01 | oleo_brasil | estoque_inicial: 348.9936958384728 mil_t (ABIOVE projecoes_mensais | oleo | mes 09/2026)
- 2026-09-01 | oleo_brasil | exportacao: 110.0 mil_t (ABIOVE projecoes_mensais | oleo | mes 09/2026)
- 2026-09-01 | oleo_brasil | producao: 532.6866062768339 mil_t (ABIOVE projecoes_mensais | oleo | mes 09/2026)
- 2026-09-01 | soja_brasil | esmagamento: 2827.146319377809 mil_t (ABIOVE projecoes_mensais | soja | mes 09/2026)
- 2026-09-01 | soja_brasil | estoque_final: 7912.141317419317 mil_t (ABIOVE projecoes_mensais | soja | mes 09/2026)
- 2026-09-01 | soja_brasil | estoque_inicial: 10169.243986312133 mil_t (ABIOVE projecoes_mensais | soja | mes 09/2026)
- 2026-09-01 | soja_brasil | exportacao: 600.0 mil_t (ABIOVE projecoes_mensais | soja | mes 09/2026)
- 2026-08-01 | farelo_brasil | estoque_final: 1224.2300783008761 mil_t (ABIOVE projecoes_mensais | farelo | mes 08/2026)
- 2026-08-01 | farelo_brasil | estoque_inicial: 1561.4277122641513 mil_t (ABIOVE projecoes_mensais | farelo | mes 08/2026)
- 2026-08-01 | farelo_brasil | exportacao: 1400.0 mil_t (ABIOVE projecoes_mensais | farelo | mes 08/2026)
- 2026-08-01 | farelo_brasil | producao: 2285.0579583273648 mil_t (ABIOVE projecoes_mensais | farelo | mes 08/2026)

---

## bcb

- 2026-06-16 | eur_brl_ptax | valor: 5.8981 BRL/EUR (sgs=21619)
- 2026-06-16 | selic_diaria | valor: 0.0534 % a.a. (sgs=11)
- 2026-06-16 | usd_brl_ptax | valor: 5.078 BRL/USD (sgs=1)
- 2026-06-15 | eur_brl_ptax | valor: 5.8494 BRL/EUR (sgs=21619)
- 2026-06-15 | selic_diaria | valor: 0.0534 % a.a. (sgs=11)
- 2026-06-15 | usd_brl_ptax | valor: 5.043 BRL/USD (sgs=1)
- 2026-06-12 | eur_brl_ptax | valor: 5.8827 BRL/EUR (sgs=21619)
- 2026-06-12 | selic_diaria | valor: 0.0534 % a.a. (sgs=11)
- 2026-06-12 | usd_brl_ptax | valor: 5.0827 BRL/USD (sgs=1)
- 2026-06-11 | eur_brl_ptax | valor: 5.9277 BRL/EUR (sgs=21619)
- 2026-06-11 | selic_diaria | valor: 0.0534 % a.a. (sgs=11)
- 2026-06-11 | usd_brl_ptax | valor: 5.1478 BRL/USD (sgs=1)
- 2026-06-10 | eur_brl_ptax | valor: 5.9791 BRL/EUR (sgs=21619)
- 2026-06-10 | selic_diaria | valor: 0.0534 % a.a. (sgs=11)
- 2026-06-10 | usd_brl_ptax | valor: 5.1763 BRL/USD (sgs=1)
- 2026-06-09 | eur_brl_ptax | valor: 5.9742 BRL/EUR (sgs=21619)
- 2026-06-09 | selic_diaria | valor: 0.0534 % a.a. (sgs=11)
- 2026-06-09 | usd_brl_ptax | valor: 5.1693 BRL/USD (sgs=1)
- 2026-06-08 | eur_brl_ptax | valor: 5.9682 BRL/EUR (sgs=21619)
- 2026-06-08 | selic_diaria | valor: 0.0534 % a.a. (sgs=11)
- 2026-06-08 | usd_brl_ptax | valor: 5.1695 BRL/USD (sgs=1)
- 2026-06-05 | eur_brl_ptax | valor: 5.91 BRL/EUR (sgs=21619)
- 2026-06-05 | selic_diaria | valor: 0.0534 % a.a. (sgs=11)
- 2026-06-05 | usd_brl_ptax | valor: 5.1244 BRL/USD (sgs=1)
- 2026-06-03 | eur_brl_ptax | valor: 5.8512 BRL/EUR (sgs=21619)
- 2026-06-03 | selic_diaria | valor: 0.0534 % a.a. (sgs=11)
- 2026-06-03 | usd_brl_ptax | valor: 5.0415 BRL/USD (sgs=1)

---

## bcba

- 2026-06-11 | argentina | page_fetched: 1.0 bool (BCBA acessivel via scraper mas sem links de relatorio detectados.)
- 2026-06-05 | argentina | page_fetched: 1.0 bool (BCBA acessivel via scraper mas sem links de relatorio detectados.)
- 2026-06-03 | argentina | page_fetched: 1.0 bool (BCBA acessivel via scraper mas sem links de relatorio detectados.)

---

## cepea_paranagua

- 2026-06-15 | soja_paranagua | preco_suporte_brl_sc: 129.24 BRL/saca (CEPEA/ESALQ Soja Paranagua via NAG (var -0.47%))
- 2026-06-12 | soja_paranagua | preco_suporte_brl_sc: 129.85 BRL/saca (CEPEA/ESALQ Soja Paranagua via NAG (var -1.46%))
- 2026-06-11 | soja_paranagua | preco_suporte_brl_sc: 131.78 BRL/saca (CEPEA/ESALQ Soja Paranagua via NAG (var -0.34%))
- 2026-06-10 | soja_paranagua | preco_suporte_brl_sc: 132.23 BRL/saca (CEPEA/ESALQ Soja Paranagua via NAG (var 1.05%))
- 2026-06-09 | soja_paranagua | preco_suporte_brl_sc: 130.85 BRL/saca (CEPEA/ESALQ Soja Paranagua via NAG (var 0.59%))
- 2026-06-08 | soja_paranagua | preco_suporte_brl_sc: 130.08 BRL/saca (CEPEA/ESALQ Soja Paranagua via NAG (var 0.71%))
- 2026-06-05 | soja_paranagua | preco_suporte_brl_sc: 129.16 BRL/saca (CEPEA/ESALQ Soja Paranagua via NAG (var -0.66%))
- 2026-06-03 | soja_paranagua | preco_suporte_brl_sc: 130.02 BRL/saca (CEPEA/ESALQ Soja Paranagua via NAG (var 0.99%))

---

## cepea_rss

- 2026-06-16 | cepea | release_items: 112.0 items (CEPEA RSS feed — 112 itens parseados)
- 2026-06-12 | soja | headline: None  (SOJA/CEPEA: Ritmo intenso dos negócios eleva cotações no BR; maior oferta limita altas | https://www.cepea.org.br/br/diarias-de-mercado/soja-cepea-ritmo-intenso-dos-negocios-eleva-cotacoes-no-br-maior-oferta-limita-altas.aspx)
- 2026-06-05 | soja | headline: None  (SOJA/CEPEA: Liquidez se aquece neste começo de junho | https://www.cepea.org.br/br/diarias-de-mercado/soja-cepea-liquidez-se-aquece-neste-comeco-de-junho.aspx)

---

## cftc_cot

- 2026-06-09 | farelo_cbot | managed_money_long: 114445.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-06-09 | farelo_cbot | managed_money_net: 55447.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE — long - short)
- 2026-06-09 | farelo_cbot | managed_money_short: 58998.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-06-09 | farelo_cbot | open_interest: 610926.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-06-09 | farelo_cbot | producer_long: 160819.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-06-09 | farelo_cbot | producer_short: 378788.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-06-09 | farelo_cbot | swap_long: 122113.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-06-09 | farelo_cbot | swap_short: 13914.0 contratos (SOYBEAN MEAL - CHICAGO BOARD OF TRADE)
- 2026-06-09 | oleo_cbot | managed_money_long: 157169.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-06-09 | oleo_cbot | managed_money_net: 128746.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE — long - short)
- 2026-06-09 | oleo_cbot | managed_money_short: 28423.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-06-09 | oleo_cbot | open_interest: 690051.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-06-09 | oleo_cbot | producer_long: 199144.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-06-09 | oleo_cbot | producer_short: 413144.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-06-09 | oleo_cbot | swap_long: 86126.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-06-09 | oleo_cbot | swap_short: 7228.0 contratos (SOYBEAN OIL - CHICAGO BOARD OF TRADE)
- 2026-06-09 | soja_cbot | managed_money_long: 179591.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-06-09 | soja_cbot | managed_money_net: 97859.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE — long - short)
- 2026-06-09 | soja_cbot | managed_money_short: 81732.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-06-09 | soja_cbot | open_interest: 1016125.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-06-09 | soja_cbot | producer_long: 308816.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-06-09 | soja_cbot | producer_short: 561486.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-06-09 | soja_cbot | swap_long: 172749.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)
- 2026-06-09 | soja_cbot | swap_short: 42199.0 contratos (SOYBEANS - CHICAGO BOARD OF TRADE)

---

## cme_cbot

- 2026-06-17 | farelo_cbot | abertura: 304.79998779296875 USD/short_ton (ticker=ZM=F)
- 2026-06-17 | farelo_cbot | fechamento: 307.8999938964844 USD/short_ton (ticker=ZM=F)
- 2026-06-17 | farelo_cbot | fechamento_F27: 310.3999938964844 USD/short_ton (ticker=ZMF27.CBT venc=jan/27)
- 2026-06-17 | farelo_cbot | fechamento_N26: 307.79998779296875 USD/short_ton (ticker=ZMN26.CBT venc=jul/26)
- 2026-06-17 | farelo_cbot | fechamento_Q26: 307.70001220703125 USD/short_ton (ticker=ZMQ26.CBT venc=ago/26)
- 2026-06-17 | farelo_cbot | fechamento_U26: 306.70001220703125 USD/short_ton (ticker=ZMU26.CBT venc=set/26)
- 2026-06-17 | farelo_cbot | fechamento_V26: 305.5 USD/short_ton (ticker=ZMV26.CBT venc=out/26)
- 2026-06-17 | farelo_cbot | fechamento_Z26: 308.5 USD/short_ton (ticker=ZMZ26.CBT venc=dez/26)
- 2026-06-17 | farelo_cbot | maxima: 308.8999938964844 USD/short_ton (ticker=ZM=F)
- 2026-06-17 | farelo_cbot | minima: 304.6000061035156 USD/short_ton (ticker=ZM=F)
- 2026-06-17 | farelo_cbot | volume: 12798.0 contratos (ticker=ZM=F)
- 2026-06-17 | heating_oil_cbot | abertura: 3.1535000801086426 USD/galão (ticker=HO=F)
- 2026-06-17 | heating_oil_cbot | fechamento: 3.1554999351501465 USD/galão (ticker=HO=F)
- 2026-06-17 | heating_oil_cbot | maxima: 3.161799907684326 USD/galão (ticker=HO=F)
- 2026-06-17 | heating_oil_cbot | minima: 3.1003000736236572 USD/galão (ticker=HO=F)
- 2026-06-17 | heating_oil_cbot | volume: 4581.0 contratos (ticker=HO=F)
- 2026-06-17 | oleo_cbot | abertura: 73.0999984741211 USD_cts/lb (ticker=ZL=F)
- 2026-06-17 | oleo_cbot | fechamento: 73.0999984741211 USD_cts/lb (ticker=ZL=F)
- 2026-06-17 | oleo_cbot | fechamento_F27: 68.05000305175781 USD_cts/lb (ticker=ZLF27.CBT venc=jan/27)
- 2026-06-17 | oleo_cbot | fechamento_N26: 73.0999984741211 USD_cts/lb (ticker=ZLN26.CBT venc=jul/26)
- 2026-06-17 | oleo_cbot | fechamento_Q26: 71.51000213623047 USD_cts/lb (ticker=ZLQ26.CBT venc=ago/26)
- 2026-06-17 | oleo_cbot | fechamento_U26: 70.12000274658203 USD_cts/lb (ticker=ZLU26.CBT venc=set/26)
- 2026-06-17 | oleo_cbot | fechamento_V26: 69.0 USD_cts/lb (ticker=ZLV26.CBT venc=out/26)
- 2026-06-17 | oleo_cbot | fechamento_Z26: 68.27999877929688 USD_cts/lb (ticker=ZLZ26.CBT venc=dez/26)
- 2026-06-17 | oleo_cbot | maxima: 73.30000305175781 USD_cts/lb (ticker=ZL=F)
- 2026-06-17 | oleo_cbot | minima: 72.2300033569336 USD_cts/lb (ticker=ZL=F)
- 2026-06-17 | oleo_cbot | volume: 11994.0 contratos (ticker=ZL=F)
- 2026-06-17 | soja_cbot | abertura: 1146.0 USD/bushel (ticker=ZS=F)
- 2026-06-17 | soja_cbot | fechamento: 1155.25 USD/bushel (ticker=ZS=F)
- 2026-06-17 | soja_cbot | fechamento_F27: 1169.0 USD/bushel (ticker=ZSF27.CBT venc=jan/27)
- 2026-06-17 | soja_cbot | fechamento_H27: 1175.0 USD/bushel (ticker=ZSH27.CBT venc=mar/27)
- 2026-06-17 | soja_cbot | fechamento_N26: 1138.0 USD/bushel (ticker=ZSN26.CBT venc=jul/26)
- 2026-06-17 | soja_cbot | fechamento_Q26: 1142.25 USD/bushel (ticker=ZSQ26.CBT venc=ago/26)
- 2026-06-17 | soja_cbot | fechamento_U26: 1142.0 USD/bushel (ticker=ZSU26.CBT venc=set/26)
- 2026-06-17 | soja_cbot | fechamento_X26: 1155.25 USD/bushel (ticker=ZSX26.CBT venc=nov/26)
- 2026-06-17 | soja_cbot | maxima: 1158.25 USD/bushel (ticker=ZS=F)
- 2026-06-17 | soja_cbot | minima: 1144.5 USD/bushel (ticker=ZS=F)
- 2026-06-17 | soja_cbot | volume: 25256.0 contratos (ticker=ZS=F)
- 2026-06-16 | farelo_cbot | abertura: 303.20001220703125 USD/short_ton (ticker=ZM=F)
- 2026-06-16 | farelo_cbot | fechamento: 304.8999938964844 USD/short_ton (ticker=ZM=F)
- 2026-06-16 | farelo_cbot | fechamento_F27: 309.20001220703125 USD/short_ton (ticker=ZMF27.CBT venc=jan/27)
- 2026-06-16 | farelo_cbot | fechamento_N26: 304.8999938964844 USD/short_ton (ticker=ZMN26.CBT venc=jul/26)
- 2026-06-16 | farelo_cbot | fechamento_Q26: 305.1000061035156 USD/short_ton (ticker=ZMQ26.CBT venc=ago/26)
- 2026-06-16 | farelo_cbot | fechamento_U26: 304.70001220703125 USD/short_ton (ticker=ZMU26.CBT venc=set/26)
- 2026-06-16 | farelo_cbot | fechamento_V26: 303.8999938964844 USD/short_ton (ticker=ZMV26.CBT venc=out/26)
- 2026-06-16 | farelo_cbot | fechamento_Z26: 307.1000061035156 USD/short_ton (ticker=ZMZ26.CBT venc=dez/26)
- 2026-06-16 | farelo_cbot | maxima: 305.20001220703125 USD/short_ton (ticker=ZM=F)
- 2026-06-16 | farelo_cbot | minima: 300.29998779296875 USD/short_ton (ticker=ZM=F)
- 2026-06-16 | farelo_cbot | volume: 64825.0 contratos (ticker=ZM=F)
- 2026-06-16 | heating_oil_cbot | abertura: 3.215100049972534 USD/galão (ticker=HO=F)

---

## indicators

- 2026-06-17 | biodiesel_us | custo_oleo_usd_galao: 5.4825 USD/galão (7.5 lb × óleo 73.10 cts/lb)
- 2026-06-17 | biodiesel_us | margem_usd_galao: 0.038 USD/galão (receita 6.32 (HO 3.16 + 1.5×RIN 2.11) − custo 6.28 (óleo 5.48 + ind 0.80))
- 2026-06-17 | biodiesel_us | receita_usd_galao: 6.3205 USD/galão (HO 3.16 + 1.5×RIN 2.11)
- 2026-06-17 | complexo_soja | crush_margin_usd_bu: 3.2623 USD/bushel (Board Crush: farelo 307.90 + oleo 73.10 − soja 1155.25)
- 2026-06-17 | complexo_soja | far_soj_ratio_pct: 79.96 % (farelo 307.90/sht ÷ (soja 1155.25cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-06-17 | complexo_soja | indice_sobra_farelo: 100.0 0-100 (forte pressão baixista no farelo (5/5 condições))
- 2026-06-17 | complexo_soja | indice_suporte_oleo: 80.0 0-100 (óleo domina o crush (4/5 condições))
- 2026-06-17 | complexo_soja | oil_meal_spread_usd_bu: 1.2672 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-06-17 | complexo_soja | oil_share_pct: 54.28 % (valor oleo 8.04 / total 14.81)
- 2026-06-17 | soja_paridade_br | brl_saca_paridade: 129.33 BRL/saca60kg (CBOT 1155.25 cts × USD/BRL 5.0780 (sem basis))
- 2026-06-16 | biodiesel_us | custo_oleo_usd_galao: 5.4675 USD/galão (7.5 lb × óleo 72.90 cts/lb)
- 2026-06-16 | biodiesel_us | margem_usd_galao: 0.0582 USD/galão (receita 6.33 (HO 3.16 + 1.5×RIN 2.11) − custo 6.27 (óleo 5.47 + ind 0.80))
- 2026-06-16 | biodiesel_us | receita_usd_galao: 6.3257 USD/galão (HO 3.16 + 1.5×RIN 2.11)
- 2026-06-16 | complexo_soja | crush_margin_usd_bu: 3.2718 USD/bushel (Board Crush: farelo 304.90 + oleo 72.90 − soja 1145.50)
- 2026-06-16 | complexo_soja | far_soj_ratio_pct: 79.85 % (farelo 304.90/sht ÷ (soja 1145.50cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-06-16 | complexo_soja | oil_meal_spread_usd_bu: 1.3112 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-06-16 | complexo_soja | oil_share_pct: 54.45 % (valor oleo 8.02 / total 14.73)
- 2026-06-16 | soja_paridade_br | brl_saca_paridade: 128.24 BRL/saca60kg (CBOT 1145.50 cts × USD/BRL 5.0780 (sem basis))
- 2026-06-15 | biodiesel_us | custo_oleo_usd_galao: 5.49 USD/galão (7.5 lb × óleo 73.20 cts/lb)
- 2026-06-15 | biodiesel_us | margem_usd_galao: 0.1101 USD/galão (receita 6.40 (HO 3.24 + 1.5×RIN 2.11) − custo 6.29 (óleo 5.49 + ind 0.80))
- 2026-06-15 | biodiesel_us | receita_usd_galao: 6.4001 USD/galão (HO 3.24 + 1.5×RIN 2.11)
- 2026-06-15 | complexo_soja | crush_margin_usd_bu: 3.5569 USD/bushel (Board Crush: farelo 301.70 + oleo 73.20 − soja 1113.25)
- 2026-06-15 | complexo_soja | far_soj_ratio_pct: 81.3 % (farelo 301.70/sht ÷ (soja 1113.25cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-06-15 | complexo_soja | oil_meal_spread_usd_bu: 1.4146 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-06-15 | complexo_soja | oil_share_pct: 54.82 % (valor oleo 8.05 / total 14.69)
- 2026-06-15 | soja_paridade_br | brl_saca_paridade: 123.77 BRL/saca60kg (CBOT 1113.25 cts × USD/BRL 5.0430 (sem basis))
- 2026-06-12 | biodiesel_us | custo_oleo_usd_galao: 5.571 USD/galão (7.5 lb × óleo 74.28 cts/lb)
- 2026-06-12 | biodiesel_us | margem_usd_galao: 0.1984 USD/galão (receita 6.57 (HO 3.40 + 1.5×RIN 2.11) − custo 6.37 (óleo 5.57 + ind 0.80))
- 2026-06-12 | biodiesel_us | receita_usd_galao: 6.5694 USD/galão (HO 3.40 + 1.5×RIN 2.11)
- 2026-06-12 | complexo_soja | crush_margin_usd_bu: 3.6644 USD/bushel (Board Crush: farelo 301.30 + oleo 74.28 − soja 1113.50)
- 2026-06-12 | complexo_soja | far_soj_ratio_pct: 81.18 % (farelo 301.30/sht ÷ (soja 1113.50cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-06-12 | complexo_soja | oil_meal_spread_usd_bu: 1.5422 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-06-12 | complexo_soja | oil_share_pct: 55.21 % (valor oleo 8.17 / total 14.80)
- 2026-06-12 | soja_paridade_br | brl_saca_paridade: 124.77 BRL/saca60kg (CBOT 1113.50 cts × USD/BRL 5.0827 (sem basis))
- 2026-06-11 | biodiesel_us | custo_oleo_usd_galao: 5.6505 USD/galão (7.5 lb × óleo 75.34 cts/lb)
- 2026-06-11 | biodiesel_us | margem_usd_galao: 0.3112 USD/galão (receita 6.76 (HO 3.60 + 1.5×RIN 2.11) − custo 6.45 (óleo 5.65 + ind 0.80))
- 2026-06-11 | biodiesel_us | receita_usd_galao: 6.7617 USD/galão (HO 3.60 + 1.5×RIN 2.11)
- 2026-06-11 | complexo_soja | crush_margin_usd_bu: 3.7766 USD/bushel (Board Crush: farelo 303.60 + oleo 75.34 − soja 1119.00)
- 2026-06-11 | complexo_soja | far_soj_ratio_pct: 81.39 % (farelo 303.60/sht ÷ (soja 1119.00cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-06-11 | complexo_soja | oil_meal_spread_usd_bu: 1.6082 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-06-11 | complexo_soja | oil_share_pct: 55.37 % (valor oleo 8.29 / total 14.97)
- 2026-06-11 | soja_paridade_br | brl_saca_paridade: 126.99 BRL/saca60kg (CBOT 1119.00 cts × USD/BRL 5.1478 (sem basis))
- 2026-06-10 | biodiesel_us | custo_oleo_usd_galao: 5.6385 USD/galão (7.5 lb × óleo 75.18 cts/lb)
- 2026-06-10 | biodiesel_us | margem_usd_galao: 0.3153 USD/galão (receita 6.75 (HO 3.59 + 1.5×RIN 2.11) − custo 6.44 (óleo 5.64 + ind 0.80))
- 2026-06-10 | biodiesel_us | receita_usd_galao: 6.7538 USD/galão (HO 3.59 + 1.5×RIN 2.11)
- 2026-06-10 | complexo_soja | crush_margin_usd_bu: 3.7299 USD/bushel (Board Crush: farelo 303.30 + oleo 75.18 − soja 1121.25)
- 2026-06-10 | complexo_soja | far_soj_ratio_pct: 81.15 % (farelo 303.30/sht ÷ (soja 1121.25cts × 33.33) — <80 abundante, >=87 apertado)
- 2026-06-10 | complexo_soja | oil_meal_spread_usd_bu: 1.5972 USD/bushel (Oleo - Farelo (positivo = oleo manda))
- 2026-06-10 | complexo_soja | oil_share_pct: 55.34 % (valor oleo 8.27 / total 14.94)
- 2026-06-10 | soja_paridade_br | brl_saca_paridade: 127.95 BRL/saca60kg (CBOT 1121.25 cts × USD/BRL 5.1763 (sem basis))

---

## inmet

- 2026-06-17 | cascavel_pr | temp_max_manha: 22.0 C (Cascavel/PR — Poucas nuvens)
- 2026-06-17 | cascavel_pr | temp_max_noite: 22.0 C (Cascavel/PR — Muitas nuvens)
- 2026-06-17 | cascavel_pr | temp_max_tarde: 22.0 C (Cascavel/PR — Muitas nuvens)
- 2026-06-17 | cascavel_pr | temp_min_manha: 10.0 C (Cascavel/PR — Poucas nuvens)
- 2026-06-17 | cascavel_pr | temp_min_noite: 10.0 C (Cascavel/PR — Muitas nuvens)
- 2026-06-17 | cascavel_pr | temp_min_tarde: 10.0 C (Cascavel/PR — Muitas nuvens)
- 2026-06-17 | cuiaba_mt | temp_max_manha: 34.0 C (Cuiaba/MT — Poucas nuvens)
- 2026-06-17 | cuiaba_mt | temp_max_noite: 34.0 C (Cuiaba/MT — Muitas nuvens)
- 2026-06-17 | cuiaba_mt | temp_max_tarde: 34.0 C (Cuiaba/MT — Poucas nuvens)
- 2026-06-17 | cuiaba_mt | temp_min_manha: 21.0 C (Cuiaba/MT — Poucas nuvens)
- 2026-06-17 | cuiaba_mt | temp_min_noite: 21.0 C (Cuiaba/MT — Muitas nuvens)
- 2026-06-17 | cuiaba_mt | temp_min_tarde: 21.0 C (Cuiaba/MT — Poucas nuvens)
- 2026-06-17 | lucas_rio_verde_mt | temp_max_manha: 36.0 C (Lucas do Rio Verde/MT — Poucas nuvens)
- 2026-06-17 | lucas_rio_verde_mt | temp_max_noite: 36.0 C (Lucas do Rio Verde/MT — Muitas nuvens)
- 2026-06-17 | lucas_rio_verde_mt | temp_max_tarde: 36.0 C (Lucas do Rio Verde/MT — Muitas nuvens)
- 2026-06-17 | lucas_rio_verde_mt | temp_min_manha: 18.0 C (Lucas do Rio Verde/MT — Poucas nuvens)
- 2026-06-17 | lucas_rio_verde_mt | temp_min_noite: 18.0 C (Lucas do Rio Verde/MT — Muitas nuvens)
- 2026-06-17 | lucas_rio_verde_mt | temp_min_tarde: 18.0 C (Lucas do Rio Verde/MT — Muitas nuvens)
- 2026-06-17 | maringa_pr | temp_max_manha: 22.0 C (Maringa/PR — Poucas nuvens)
- 2026-06-17 | maringa_pr | temp_max_noite: 22.0 C (Maringa/PR — Poucas nuvens)
- 2026-06-17 | maringa_pr | temp_max_tarde: 22.0 C (Maringa/PR — Poucas nuvens)
- 2026-06-17 | maringa_pr | temp_min_manha: 11.0 C (Maringa/PR — Poucas nuvens)
- 2026-06-17 | maringa_pr | temp_min_noite: 11.0 C (Maringa/PR — Poucas nuvens)
- 2026-06-17 | maringa_pr | temp_min_tarde: 11.0 C (Maringa/PR — Poucas nuvens)
- 2026-06-17 | passo_fundo_rs | temp_max_manha: 16.0 C (Passo Fundo/RS — Claro com geada)
- 2026-06-17 | passo_fundo_rs | temp_max_noite: 16.0 C (Passo Fundo/RS — Poucas nuvens)
- 2026-06-17 | passo_fundo_rs | temp_max_tarde: 16.0 C (Passo Fundo/RS — Poucas nuvens)
- 2026-06-17 | passo_fundo_rs | temp_min_manha: 6.0 C (Passo Fundo/RS — Claro com geada)
- 2026-06-17 | passo_fundo_rs | temp_min_noite: 6.0 C (Passo Fundo/RS — Poucas nuvens)
- 2026-06-17 | passo_fundo_rs | temp_min_tarde: 6.0 C (Passo Fundo/RS — Poucas nuvens)
- 2026-06-17 | rio_verde_go | temp_max_manha: 28.0 C (Rio Verde/GO — Poucas nuvens)
- 2026-06-17 | rio_verde_go | temp_max_noite: 28.0 C (Rio Verde/GO — Poucas nuvens)
- 2026-06-17 | rio_verde_go | temp_max_tarde: 28.0 C (Rio Verde/GO — Poucas nuvens)
- 2026-06-17 | rio_verde_go | temp_min_manha: 17.0 C (Rio Verde/GO — Poucas nuvens)
- 2026-06-17 | rio_verde_go | temp_min_noite: 17.0 C (Rio Verde/GO — Poucas nuvens)
- 2026-06-17 | rio_verde_go | temp_min_tarde: 17.0 C (Rio Verde/GO — Poucas nuvens)
- 2026-06-17 | sinop_mt | temp_max_manha: 36.0 C (Sinop/MT — Poucas nuvens)
- 2026-06-17 | sinop_mt | temp_max_noite: 36.0 C (Sinop/MT — Muitas nuvens)
- 2026-06-17 | sinop_mt | temp_max_tarde: 36.0 C (Sinop/MT — Poucas nuvens)
- 2026-06-17 | sinop_mt | temp_min_manha: 20.0 C (Sinop/MT — Poucas nuvens)
- 2026-06-17 | sinop_mt | temp_min_noite: 20.0 C (Sinop/MT — Muitas nuvens)
- 2026-06-17 | sinop_mt | temp_min_tarde: 20.0 C (Sinop/MT — Poucas nuvens)
- 2026-06-17 | sorriso_mt | temp_max_manha: 36.0 C (Sorriso/MT — Muitas nuvens)
- 2026-06-17 | sorriso_mt | temp_max_noite: 36.0 C (Sorriso/MT — Muitas nuvens)
- 2026-06-17 | sorriso_mt | temp_max_tarde: 36.0 C (Sorriso/MT — Muitas nuvens)
- 2026-06-17 | sorriso_mt | temp_min_manha: 22.0 C (Sorriso/MT — Muitas nuvens)
- 2026-06-17 | sorriso_mt | temp_min_noite: 22.0 C (Sorriso/MT — Muitas nuvens)
- 2026-06-17 | sorriso_mt | temp_min_tarde: 22.0 C (Sorriso/MT — Muitas nuvens)
- 2026-06-16 | cascavel_pr | temp_max_manha: 20.0 C (Cascavel/PR — Poucas nuvens)
- 2026-06-16 | cascavel_pr | temp_max_noite: 20.0 C (Cascavel/PR — Poucas nuvens)

---

## mpob

- 2026-06-16 | palma_malasia | page_fetched: 3428.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-06-15 | palma_malasia | page_fetched: 3428.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-06-11 | palma_malasia | page_fetched: 3428.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-06-05 | palma_malasia | page_fetched: 3427.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)
- 2026-06-03 | palma_malasia | page_fetched: 3427.0 chars (MPOB acessivel mas parser nao extraiu numeros — verificar estrutura.)

---

## nag_fisico

- 2026-06-16 | farelo_fisico_br | preco_brl_ton_mt_imea: 1545.75 BRL/ton (Mato Grosso (IMEA) via NAG (var 0.0%))
- 2026-06-16 | farelo_fisico_br | preco_brl_ton_rondonopolis_mt: 1560.0 BRL/ton (Rondonópolis/MT (BCSP) via NAG (var 0.65%))
- 2026-06-16 | farelo_fisico_br | preco_brl_ton_rs_media: 1710.0 BRL/ton (Média Rio Grande do Sul (Clicmercado) via NAG (var 0.0%))
- 2026-06-16 | farelo_paranagua | premio_usd_sht: 0.05 USD/short_ton (Premio farelo Paranagua (NAG) — mes Junho/26)
- 2026-06-16 | oleo_paranagua | premio_cts_lb: 0.08 cts/lb (Premio oleo Paranagua (NAG) — mes Junho/26)
- 2026-06-15 | farelo_fisico_br | preco_brl_ton_mt_imea: 1545.75 BRL/ton (Mato Grosso (IMEA) via NAG (var 0.0%))
- 2026-06-15 | farelo_fisico_br | preco_brl_ton_rondonopolis_mt: 1550.0 BRL/ton (Rondonópolis/MT (BCSP) via NAG (var 0.0%))
- 2026-06-15 | farelo_fisico_br | preco_brl_ton_rs_media: 1710.0 BRL/ton (Média Rio Grande do Sul (Clicmercado) via NAG (var 0.0%))
- 2026-06-15 | farelo_paranagua | premio_usd_sht: 0.05 USD/short_ton (Premio farelo Paranagua (NAG) — mes Junho/26)
- 2026-06-15 | oleo_paranagua | premio_cts_lb: 0.08 cts/lb (Premio oleo Paranagua (NAG) — mes Junho/26)
- 2026-06-15 | soja_parana_interior | preco_brl_sc: 122.68 BRL/saca (CEPEA/ESALQ Soja Parana interior via NAG (var -1.61%))
- 2026-06-12 | farelo_fisico_br | preco_brl_ton_mt_imea: 1545.75 BRL/ton (Mato Grosso (IMEA) via NAG (var -1.08%))
- 2026-06-12 | farelo_fisico_br | preco_brl_ton_rondonopolis_mt: 1550.0 BRL/ton (Rondonópolis/MT (BCSP) via NAG (var -0.64%))
- 2026-06-12 | farelo_fisico_br | preco_brl_ton_rs_media: 1710.0 BRL/ton (Média Rio Grande do Sul (Clicmercado) via NAG (var 0.0%))
- 2026-06-12 | farelo_paranagua | premio_usd_sht: 0.05 USD/short_ton (Premio farelo Paranagua (NAG) — mes Junho/26)
- 2026-06-12 | oleo_paranagua | premio_cts_lb: 0.08 cts/lb (Premio oleo Paranagua (NAG) — mes Junho/26)
- 2026-06-12 | soja_parana_interior | preco_brl_sc: 124.69 BRL/saca (CEPEA/ESALQ Soja Parana interior via NAG (var -0.83%))
- 2026-06-11 | farelo_fisico_br | preco_brl_ton_mt_imea: 1562.59 BRL/ton (Mato Grosso (IMEA) via NAG (var 0.0%))
- 2026-06-11 | farelo_fisico_br | preco_brl_ton_rondonopolis_mt: 1560.0 BRL/ton (Rondonópolis/MT (BCSP) via NAG (var -1.27%))
- 2026-06-11 | farelo_fisico_br | preco_brl_ton_rs_media: 1710.0 BRL/ton (Média Rio Grande do Sul (Clicmercado) via NAG (var 0.0%))
- 2026-06-11 | farelo_paranagua | premio_usd_sht: 0.05 USD/short_ton (Premio farelo Paranagua (NAG) — mes Junho/26)
- 2026-06-11 | oleo_paranagua | premio_cts_lb: 0.08 cts/lb (Premio oleo Paranagua (NAG) — mes Junho/26)
- 2026-06-11 | soja_parana_interior | preco_brl_sc: 125.73 BRL/saca (CEPEA/ESALQ Soja Parana interior via NAG (var 0.18%))
- 2026-06-10 | farelo_fisico_br | preco_brl_ton_mt_imea: 1562.59 BRL/ton (Mato Grosso (IMEA) via NAG (var 0.0%))
- 2026-06-10 | farelo_fisico_br | preco_brl_ton_rondonopolis_mt: 1580.0 BRL/ton (Rondonópolis/MT (BCSP) via NAG (var 0.0%))
- 2026-06-10 | farelo_fisico_br | preco_brl_ton_rs_media: 1710.0 BRL/ton (Média Rio Grande do Sul (Clicmercado) via NAG (var 0.0%))
- 2026-06-10 | farelo_paranagua | premio_usd_sht: 0.05 USD/short_ton (Premio farelo Paranagua (NAG) — mes Junho/26)
- 2026-06-10 | oleo_paranagua | premio_cts_lb: 0.08 cts/lb (Premio oleo Paranagua (NAG) — mes Junho/26)
- 2026-06-10 | soja_parana_interior | preco_brl_sc: 125.51 BRL/saca (CEPEA/ESALQ Soja Parana interior via NAG (var 0.66%))
- 2026-06-09 | farelo_fisico_br | preco_brl_ton_mt_imea: 1562.59 BRL/ton (Mato Grosso (IMEA) via NAG (var 0.0%))
- 2026-06-09 | farelo_fisico_br | preco_brl_ton_rondonopolis_mt: 1580.0 BRL/ton (Rondonópolis/MT (BCSP) via NAG (var 0.0%))
- 2026-06-09 | farelo_fisico_br | preco_brl_ton_rs_media: 1710.0 BRL/ton (Média Rio Grande do Sul (Clicmercado) via NAG (var 0.0%))
- 2026-06-09 | farelo_paranagua | premio_usd_sht: 0.05 USD/short_ton (Premio farelo Paranagua (NAG) — mes Junho/26)
- 2026-06-09 | oleo_paranagua | premio_cts_lb: 0.08 cts/lb (Premio oleo Paranagua (NAG) — mes Junho/26)
- 2026-06-09 | soja_parana_interior | preco_brl_sc: 124.69 BRL/saca (CEPEA/ESALQ Soja Parana interior via NAG (var 0.46%))
- 2026-06-08 | farelo_fisico_br | preco_brl_ton_mt_imea: 1562.59 BRL/ton (Mato Grosso (IMEA) via NAG (var -1.64%))
- 2026-06-08 | farelo_fisico_br | preco_brl_ton_rondonopolis_mt: 1580.0 BRL/ton (Rondonópolis/MT (BCSP) via NAG (var -4.24%))
- 2026-06-08 | farelo_fisico_br | preco_brl_ton_rs_media: 1710.0 BRL/ton (Média Rio Grande do Sul (Clicmercado) via NAG (var 0.0%))
- 2026-06-08 | farelo_paranagua | premio_usd_sht: 0.05 USD/short_ton (Premio farelo Paranagua (NAG) — mes Junho/26)
- 2026-06-08 | oleo_paranagua | premio_cts_lb: 0.08 cts/lb (Premio oleo Paranagua (NAG) — mes Junho/26)
- 2026-06-08 | soja_parana_interior | preco_brl_sc: 124.12 BRL/saca (CEPEA/ESALQ Soja Parana interior via NAG (var -0.19%))

---

## noaa_cpc

- 2026-06-16 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-06-15 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-06-11 | enso | status: 0.0 categorico (ENSO Alert: El Niño Advisory)
- 2026-06-05 | enso | status: 0.0 categorico (ENSO Alert: El Niño Watch)
- 2026-06-03 | enso | status: 0.0 categorico (ENSO Alert: El Niño Watch)

---

## nopa

- 2026-06-16 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-06-15 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-06-11 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-06-05 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)
- 2026-06-03 | nopa | monthly_status: 0.0 bool (NOPA Monthly Crush Reports requerem membership pagante. Dado mensal disponivel via StoneX 'Semanal de Oleos Vegetais' (que cita NOPA mensal nas analises).)

---

## noticias_rss

- 2026-06-16 | noticias | items_fetched: 160.0 items (160 items lidos, 3 mantidos (soja/farelo/oleo))
- 2026-06-16 | soja | headline: None  (Soybeans found plenty of upside on Tuesday | https://www.farmprogress.com/markets-and-quotes/afternoon-market-recap)
- 2026-06-15 | noticias | items_fetched: 160.0 items (160 items lidos, 5 mantidos (soja/farelo/oleo))
- 2026-06-15 | soja | headline: None  (Mercado de soja segue aquecido com demanda forte e dólar favorável | https://www.canalrural.com.br/agricultura/soja/mercado-de-soja-segue-aquecido-com-demanda-forte-e-dolar-favoravel/)
- 2026-06-14 | soja | headline: None  (Compactação do solo reduz produtividade da soja e desafia lavouras em períodos de seca, diz estudo | https://www.canalrural.com.br/agricultura/soja/compactacao-do-solo-reduz-produtividade-da-soja-e-desafia-lavouras-em-periodos-de-seca-diz-estudo/)
- 2026-06-12 | soja | headline: None  (Soybean planting depth affects late-season success | https://www.farmprogress.com/soybean/soybean-planting-depth-affects-late-season-success)
- 2026-06-11 | noticias | items_fetched: 160.0 items (160 items lidos, 2 mantidos (soja/farelo/oleo))
- 2026-06-11 | soja | headline: None  (Seed costs eat 25% of corn and soybean budgets, five times industry claims | https://www.farmprogress.com/crops/seed-costs-eat-25-of-corn-and-soybean-budgets-five-times-industry-claims)
- 2026-06-09 | soja | headline: None  (Ohio Soybean Council has 4 open board positions | https://www.farmprogress.com/soybean/ohio-soybean-council-has-4-open-board-positions)
- 2026-06-05 | noticias | items_fetched: 160.0 items (160 items lidos, 2 mantidos (soja/farelo/oleo))
- 2026-06-04 | soja | headline: None  (Reality check for soybean bulls: Record crop may be in works | https://www.farmprogress.com/marketing/reality-check-for-soybean-bulls-record-crop-may-be-in-works)
- 2026-06-03 | noticias | items_fetched: 160.0 items (160 items lidos, 2 mantidos (soja/farelo/oleo))
- 2026-06-03 | soja | headline: None  (Soybean crop looks promising after frost damage concerns | https://www.farmprogress.com/planting/soybean-crop-looks-promising-after-frost-damage-concerns)

---

## usda_crop_progress

- 2026-06-14 | soybeans_eua | cond_pct_excellent: 9.0 % (SOYBEANS - CONDITION, MEASURED IN PCT EXCELLENT)
- 2026-06-14 | soybeans_eua | cond_pct_good: 57.0 % (SOYBEANS - CONDITION, MEASURED IN PCT GOOD)
- 2026-06-14 | soybeans_eua | cond_pct_poor: 5.0 % (SOYBEANS - CONDITION, MEASURED IN PCT POOR)
- 2026-06-14 | soybeans_eua | pct_emerged: 88.0 % (SOYBEANS - PROGRESS, MEASURED IN PCT EMERGED)
- 2026-06-14 | soybeans_eua | pct_planted: 95.0 % (SOYBEANS - PROGRESS, MEASURED IN PCT PLANTED)
- 2026-06-07 | soybeans_eua | cond_pct_excellent: 9.0 % (SOYBEANS - CONDITION, MEASURED IN PCT EXCELLENT)
- 2026-06-07 | soybeans_eua | cond_pct_good: 56.0 % (SOYBEANS - CONDITION, MEASURED IN PCT GOOD)
- 2026-06-07 | soybeans_eua | cond_pct_poor: 5.0 % (SOYBEANS - CONDITION, MEASURED IN PCT POOR)
- 2026-06-07 | soybeans_eua | pct_emerged: 79.0 % (SOYBEANS - PROGRESS, MEASURED IN PCT EMERGED)
- 2026-06-07 | soybeans_eua | pct_planted: 92.0 % (SOYBEANS - PROGRESS, MEASURED IN PCT PLANTED)

---

## usda_wasde

- 2026-06-11 | farelo_argentina | beginning_stocks_2024/2025: 2.26 mi_t (WASDE farelo | Argentina | 2024/2025)
- 2026-06-11 | farelo_argentina | beginning_stocks_2025/2026: 2.74 mi_t (WASDE farelo | Argentina | 2025/2026)
- 2026-06-11 | farelo_argentina | beginning_stocks_2026/2027_jun: 2.73 mi_t (WASDE farelo | Argentina | 2026/2027 [Jun])
- 2026-06-11 | farelo_argentina | beginning_stocks_2026/2027_may: 2.47 mi_t (WASDE farelo | Argentina | 2026/2027 [May])
- 2026-06-11 | farelo_argentina | domestic_crush_2024/2025: 3.53 mi_t (WASDE farelo | Argentina | 2024/2025)
- 2026-06-11 | farelo_argentina | domestic_crush_2025/2026: 3.6 mi_t (WASDE farelo | Argentina | 2025/2026)
- 2026-06-11 | farelo_argentina | domestic_crush_2026/2027_jun: 3.65 mi_t (WASDE farelo | Argentina | 2026/2027 [Jun])
- 2026-06-11 | farelo_argentina | domestic_crush_2026/2027_may: 3.65 mi_t (WASDE farelo | Argentina | 2026/2027 [May])
- 2026-06-11 | farelo_argentina | domestic_total_2024/2025: 29.78 mi_t (WASDE farelo | Argentina | 2024/2025)
- 2026-06-11 | farelo_argentina | domestic_total_2025/2026: 29.0 mi_t (WASDE farelo | Argentina | 2025/2026)
- 2026-06-11 | farelo_argentina | domestic_total_2026/2027_jun: 29.4 mi_t (WASDE farelo | Argentina | 2026/2027 [Jun])
- 2026-06-11 | farelo_argentina | domestic_total_2026/2027_may: 29.4 mi_t (WASDE farelo | Argentina | 2026/2027 [May])
- 2026-06-11 | farelo_argentina | exports_2024/2025: 2.74 mi_t (WASDE farelo | Argentina | 2024/2025)
- 2026-06-11 | farelo_argentina | exports_2025/2026: 2.73 mi_t (WASDE farelo | Argentina | 2025/2026)
- 2026-06-11 | farelo_argentina | exports_2026/2027_jun: 2.91 mi_t (WASDE farelo | Argentina | 2026/2027 [Jun])
- 2026-06-11 | farelo_argentina | exports_2026/2027_may: 2.75 mi_t (WASDE farelo | Argentina | 2026/2027 [May])
- 2026-06-11 | farelo_argentina | imports_2024/2025: 0.28 mi_t (WASDE farelo | Argentina | 2024/2025)
- 2026-06-11 | farelo_argentina | imports_2025/2026: 0.25 mi_t (WASDE farelo | Argentina | 2025/2026)
- 2026-06-11 | farelo_argentina | imports_2026/2027_jun: 0.12 mi_t (WASDE farelo | Argentina | 2026/2027 [Jun])
- 2026-06-11 | farelo_argentina | production_2024/2025: 33.51 mi_t (WASDE farelo | Argentina | 2024/2025)
- 2026-06-11 | farelo_argentina | production_2025/2026: 32.34 mi_t (WASDE farelo | Argentina | 2025/2026)
- 2026-06-11 | farelo_argentina | production_2026/2027_jun: 33.11 mi_t (WASDE farelo | Argentina | 2026/2027 [Jun])
- 2026-06-11 | farelo_argentina | production_2026/2027_may: 33.33 mi_t (WASDE farelo | Argentina | 2026/2027 [May])
- 2026-06-11 | farelo_brazil | beginning_stocks_2024/2025: 2.97 mi_t (WASDE farelo | Brazil | 2024/2025)
- 2026-06-11 | farelo_brazil | beginning_stocks_2025/2026: 3.47 mi_t (WASDE farelo | Brazil | 2025/2026)
- 2026-06-11 | farelo_brazil | beginning_stocks_2026/2027_jun: 4.16 mi_t (WASDE farelo | Brazil | 2026/2027 [Jun])
- 2026-06-11 | farelo_brazil | beginning_stocks_2026/2027_may: 4.16 mi_t (WASDE farelo | Brazil | 2026/2027 [May])
- 2026-06-11 | farelo_brazil | domestic_crush_2024/2025: 20.5 mi_t (WASDE farelo | Brazil | 2024/2025)
- 2026-06-11 | farelo_brazil | domestic_crush_2025/2026: 21.8 mi_t (WASDE farelo | Brazil | 2025/2026)
- 2026-06-11 | farelo_brazil | domestic_crush_2026/2027_jun: 23.0 mi_t (WASDE farelo | Brazil | 2026/2027 [Jun])
- 2026-06-11 | farelo_brazil | domestic_crush_2026/2027_may: 23.0 mi_t (WASDE farelo | Brazil | 2026/2027 [May])
- 2026-06-11 | farelo_brazil | domestic_total_2024/2025: 23.39 mi_t (WASDE farelo | Brazil | 2024/2025)
- 2026-06-11 | farelo_brazil | domestic_total_2025/2026: 25.0 mi_t (WASDE farelo | Brazil | 2025/2026)
- 2026-06-11 | farelo_brazil | domestic_total_2026/2027_jun: 26.9 mi_t (WASDE farelo | Brazil | 2026/2027 [Jun])
- 2026-06-11 | farelo_brazil | domestic_total_2026/2027_may: 26.9 mi_t (WASDE farelo | Brazil | 2026/2027 [May])
- 2026-06-11 | farelo_brazil | exports_2024/2025: 3.47 mi_t (WASDE farelo | Brazil | 2024/2025)
- 2026-06-11 | farelo_brazil | exports_2025/2026: 4.16 mi_t (WASDE farelo | Brazil | 2025/2026)
- 2026-06-11 | farelo_brazil | exports_2026/2027_jun: 4.28 mi_t (WASDE farelo | Brazil | 2026/2027 [Jun])
- 2026-06-11 | farelo_brazil | exports_2026/2027_may: 4.28 mi_t (WASDE farelo | Brazil | 2026/2027 [May])
- 2026-06-11 | farelo_brazil | imports_2024/2025: 0.01 mi_t (WASDE farelo | Brazil | 2024/2025)
- 2026-06-11 | farelo_brazil | imports_2025/2026: 0.01 mi_t (WASDE farelo | Brazil | 2025/2026)
- 2026-06-11 | farelo_brazil | imports_2026/2027_jun: 0.01 mi_t (WASDE farelo | Brazil | 2026/2027 [Jun])
- 2026-06-11 | farelo_brazil | imports_2026/2027_may: 0.01 mi_t (WASDE farelo | Brazil | 2026/2027 [May])
- 2026-06-11 | farelo_brazil | production_2024/2025: 44.38 mi_t (WASDE farelo | Brazil | 2024/2025)
- 2026-06-11 | farelo_brazil | production_2025/2026: 47.48 mi_t (WASDE farelo | Brazil | 2025/2026)
- 2026-06-11 | farelo_brazil | production_2026/2027_jun: 50.01 mi_t (WASDE farelo | Brazil | 2026/2027 [Jun])
- 2026-06-11 | farelo_brazil | production_2026/2027_may: 50.01 mi_t (WASDE farelo | Brazil | 2026/2027 [May])
- 2026-06-11 | farelo_china | beginning_stocks_2024/2025: 0.79 mi_t (WASDE farelo | China | 2024/2025)
- 2026-06-11 | farelo_china | beginning_stocks_2025/2026: 0.94 mi_t (WASDE farelo | China | 2025/2026)
- 2026-06-11 | farelo_china | beginning_stocks_2026/2027_jun: 1.28 mi_t (WASDE farelo | China | 2026/2027 [Jun])

---

# FORECASTS ATIVOS (bandas estatisticas)

Bandas calculadas via MA20+volatilidade+slope curto. Claude Code DEVE refinar com drivers fundamentais.

| Geracao | Horizonte | Alvo | Commodity | Spot ref | Baixo | Central | Alto | Vies |
|---|---|---|---|---|---|---|---|---|
| 2026-06-16 | 7d | 2026-06-23 | farelo_cbot | 304.90 | 276.64 | 293.18 | 309.72 | baixista |
| 2026-06-16 | 7d | 2026-06-23 | oleo_cbot | 72.90 | 68.60 | 73.06 | 77.52 | lateral |
| 2026-06-16 | 7d | 2026-06-23 | soja_cbot | 1145.50 | 1053.42 | 1109.07 | 1164.73 | baixista |
| 2026-06-16 | 30d | 2026-07-16 | farelo_cbot | 304.90 | 216.96 | 251.21 | 285.45 | baixista |
| 2026-06-16 | 30d | 2026-07-16 | oleo_cbot | 72.90 | 63.73 | 72.95 | 82.18 | lateral |
| 2026-06-16 | 30d | 2026-07-16 | soja_cbot | 1145.50 | 870.49 | 985.71 | 1100.93 | baixista |
| 2026-06-15 | 7d | 2026-06-22 | farelo_cbot | 301.70 | 274.56 | 290.75 | 306.94 | baixista |
| 2026-06-15 | 7d | 2026-06-22 | oleo_cbot | 73.20 | 69.04 | 73.59 | 78.14 | altista |
| 2026-06-15 | 7d | 2026-06-22 | soja_cbot | 1113.25 | 1029.27 | 1079.40 | 1129.53 | baixista |
| 2026-06-15 | 30d | 2026-07-15 | farelo_cbot | 301.70 | 216.63 | 250.14 | 283.66 | baixista |
| 2026-06-15 | 30d | 2026-07-15 | oleo_cbot | 73.20 | 64.86 | 74.28 | 83.69 | altista |
| 2026-06-15 | 30d | 2026-07-15 | soja_cbot | 1113.25 | 851.83 | 955.60 | 1059.38 | baixista |

---

# NOTAS DE CALL

## meeting_2026-05-25_fabio-cruz_oleo-biodiesel.md

# Reunião StoneX — Fabio Cruz — Óleo soja × biodiesel americano

> **Data:** 2026-05-25, 13h31 BRT
> **Duração:** 60 min
> **Participantes:** usuário + Fabio Cruz (consultor StoneX)
> **Tema central:** o que faz o óleo soja subir/cair no CBOT atualmente; matriz de cenários soja × farelo × óleo
> **Transcrição original:** local em `D:\Downloads\Meeting Transcription.txt` (Tactiq AI)

---

## Resumo executivo — 10 pontos-chave

1. **Óleo soja CBOT perdeu correlação com o mercado mundial.** EUA exportam quase nada de óleo de soja (são até importadores líquidos). Hoje quem manda no preço é o mercado interno americano via política de biodiesel.

2. **Mecânica do limite (RFS/RIN):** refinaria diesel é obrigada a misturar biodiesel OU comprar crédito RIN. Pequenas refinarias tinham isenção; agora isenções retroativas estão sendo aplicadas → demanda RIN explodiu → preço RIN sustenta margem biodiesel → preço óleo soja sobe.

3. **Conta da margem biodiesel americano (USD/galão):**
   ```
   receita = HO Chicago + 1,5 × RIN D4
   custo   = 7,5 × (óleo soja cents/lb) + custo industrial (~$0,6-1)
   margem  = receita − custo
   ```
   Atualmente RIN D4 ~$2,11/gal, óleo ~74 cts/lb, HO recente ~$3,77/gal.

4. **Teto natural do óleo:** se óleo subir pra ~80 cts/lb com HO/RIN atuais, margem biodiesel zera → produção reduz → óleo cai. É o "circuit breaker" que segura o bull run.

5. **Soja CBOT × estoque/uso americano** (base histórica USDA):
   - S/U 8% → ~$11,00/bu
   - S/U 6% → ~$11,45/bu
   - S/U 5% → ~$11,70/bu
   - S/U 4% (quebra) → $12,50+/bu (cenário atípico)

6. **Far/Soj ratio** (preço farelo ÷ preço soja em USD/ton):
   - 77% = farelo abundante (esmagamento alto, oferta sobra)
   - 82% = equilíbrio
   - 87%+ = farelo apertado (Argentina/EUA quebra)
   - Em 2024 chegou a 100%+ (quebra Argentina)
   - **Atualmente ~83%** (próximo do equilíbrio)

7. **Oil share** (% do valor do crush vindo do óleo):
   - Histórico pré-2020: ~33%
   - Pós-2020 (políticas verdes): 40-55%
   - **Atualmente 52,7%** (próximo do teto)
   - >55% começa a desincentivar (excesso de farelo sem comprador)

8. **Crush margin Chicago:**
   - >$2/bu = verde (esmagamento forte continua)
   - <$2/bu = vermelho (esmagamento aperta, reduz turno)
   - **Atualmente $3,47/bu** (zona muito confortável)

9. **Cenário-base do Fabio para próximos 20-30 dias** (filtros aplicados):
   - Soja CBOT: $11,00 - $12,00/bu (descarta quebra EUA agora)
   - Far/Soj: ~82% (descarta 87% que pede Argentina quebrar de novo)
   - Oil share: 50-53% (descarta 47% que pede biocombustível enfraquecer)
   - Crush margin: ≥$2/bu sustentado pela demanda biodiesel
   - **Sobra ~6 células da matriz 36 como cenário plausível**

10. **Validação importante (43:14):** Fabio confirmou que paridade soja CBOT → R$/saca usa multiplicador 2,2046 (não 2,0462). Soja $11,96/bu × 5,014 USD/BRL × 2,2046 ≈ R$ 132/sc. **Bug do sistema corrigido nessa mesma sessão.**

---

## Tese atual do Fabio sobre óleo soja

> *"O que mais tem força hoje no Chicago é a margem de combustível americano. Petróleo/heating oil é a proxy do diesel lá nos Estados Unidos. Esse é o principal fator que faz o óleo ficar caro hoje."*

**Fatores bullish atuais:**
- Isenções RIN retroativas voltando ao mercado (acelera demanda crédito)
- Mandato RFS 2026 esperado elevado
- Section 45Z PTC influenciando margens
- Petróleo ainda em patamar que sustenta HO

**Fatores bearish (gatilhos de reversão):**
- Petróleo cai sustentadamente → HO cai → margem aperta → óleo cai
- EPA revisa mandato pra diluir cota retroativa (alívio político por inflação combustível)
- Oil share passa de 55% → excesso farelo derruba crush → reduz esmagamento

---

## Ação operacional pro usuário (comprador de farelo)

**Níveis pra ficar de olho:**

| Cenário | Preço farelo Chicago (USD/sht) | Ação |
|---|---|---|
| Farelo abundante (Far/Soj 77%) | ~$280-301 | **🟢 ZONA DE COMPRA** (travar preço com bolsa) |
| Equilíbrio (Far/Soj 82%) | ~$301-328 | observar |
| Farelo apertado (Far/Soj 87%+) | $330-340+ | **🔴 ZONA DE VENDA** (descobrir posições se for vendedor) |

**Atualmente** (~$331,90/sht, Far/Soj 83%) → zona de observação, levemente acima do equilíbrio.

---

## Insights para desenvolvimento do sistema

A reunião gerou roadmap concreto:

### Fase 1 — Coleta (em andamento)
- [x] **Heating Oil (HO) Chicago** — adicionado ao `cme_cbot.py` ($3,77/gal hoje)
- [ ] **RIN D4 price** — EPA tem dado semanal (CSV via export); coletor a fazer ou input manual
- [ ] **Custo industrial assumível** — parâmetro configurável (~$0,8/gal)

### Fase 2 — Indicador derivado
- [ ] **Margem biodiesel americano** em `indicators.py`:
  ```python
  margem = (HO + 1.5 × RIN) − (7.5 × óleo_cts/100 + custo_industrial)
  ```
- [ ] Salvar em `dados_publicos` com commodity='biodiesel_us_margin'

### Fase 3 — Visual no HTML
- [ ] Card "Margem biodiesel US" com:
  - Margem atual por galão (verde >$0,5, vermelho <$0)
  - Decomposição visual (HO + RIN − óleo − custo)
  - Sensibilidade: "se óleo subir 5 cts/lb → margem cai X"
  - Alerta: margem <$0,5 = tese bullish óleo em risco

### Fase 4 — Sinais de compra/venda farelo
- [ ] No card de Mercado Físico, calcular níveis de compra/venda do farelo em R$/ton baseado nos buckets 77/82/87% e mostrar onde o atual cai.

### Fase 5 — Tabela S/U × preço CBOT
- [ ] Pegar S/U atual do USDA WASDE + tabela histórica 20 anos → faixa de preço esperada da soja.

---

## Citações úteis para próximas conversas

> *"Como o farelo é exportado por EUA e Brasil, a cotação Chicago digere melhor questões do mundo. Já o óleo de soja, como EUA não exporta, perde correlação com o mundo — quem manda é o mercado interno."* (08:36)

> *"O óleo de soja não pode subir para sempre, porque tem o teto da margem biodiesel. Se margem zera, esmagamento reduz, óleo cai."* (28:40)

> *"O ioshare passou de 55% começa a se tornar desincentivado, porque o esmagamento produz 4 partes de farelo pra 1 de óleo. Se eu esmago só pra produzir óleo, em algum momento o farelo cai porque não tem demanda."* (36:50)

> *"Eu já filtrei bastante. Cenário base: oil share 50-53%, crush ≥$2, far/soj ~82%, soja 11-12 USD/bu."* (58:56)

---

## Transcrição completa

(Original em `D:\Downloads\Meeting Transcription.txt` — Tactiq AI)

Trechos importantes inline para busca rápida:

**00:00-02:50 — Setup, ideia do sistema, foco curto prazo (20-30 dias)**

**03:30-06:38 — Privacidade dados StoneX, compartilhamento via Cloud**

**07:00-10:30 — Por que óleo CBOT perdeu correlação com mundo**
> "Você tem produtos exportados que têm dependência do mercado externo. O óleo de soja Chicago, hoje, com mercado americano demandado, perde muito a correlação."

**11:00-15:00 — Mecânica RFS/RIN, isenções retroativas**

**15:30-21:00 — Cebio brasileiro vs RIN americano, mandato direto vs indireto**

**21:30-24:50 — Conta margem biodiesel: HO + RIN − óleo × 7,5 − custo industrial**

**26:00-30:00 — Como RIN sustenta a margem; sensibilidade ao petróleo**

**32:00-35:00 — Cenários de queda óleo (petróleo cai, RIN sobe, política revisa)**

**36:00-38:30 — Oil share como termômetro; piso/teto histórico**

**40:30-43:00 — Conversão paridade soja CBOT → R$/saca (validação bug)**

**43:20-47:00 — Far/Soj 77-87% explicado**

**47:30-50:30 — Como ler a matriz: soja > far_pct > oil share > óleo implícito**

**51:00-56:00 — Decisão pro consumidor de farelo (zonas de compra/venda)**

**56:00-59:30 — Filtros mentais do cenário-base, descarte de extremos**

---

*Salvo automaticamente em 2026-05-25 pelo Commodities Radar — sessão de absorção da reunião com Fabio Cruz.*


---


---

# Fila de julgamento — 2026-06-17

**2 item(ns).** Frase-gatilho: "lê a fila de julgamento e trata"

## 🟡 [release] NOPA novo (2026-06-16)
- id: `release-nopa-2026-06-16`
- fato: fonte nopa com data 2026-06-16 — coletado, ainda nao interpretado
- refs: complexo_soja
- leitura: O numero muda o balanco/tese? Algo relevante pro farelo?

## 🟡 [revisao] Revisao D+7 em 1d: Ratio Far/Soj 81,4% + FOB export zerado — spread far÷so
- id: `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
- fato: D+7 2026-06-18 — ratio fechou <80%? WASDE mudou o quadro? NOPA confirmou crush?
- refs: farelo,ratio-far-soj,spread
- leitura: A tese se confirmou? Atualizar status/insight.

---
Trate só 🔴/🟡. Saída = `insights/*.md` (formato de generate_insights.txt, com `vies:`). Cite o `id` da fila no corpo do insight. Máx 1-3. Não duplicar insight recente.
