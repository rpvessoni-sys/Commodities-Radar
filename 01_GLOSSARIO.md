# Glossario Operacional — Soja, Farelo e Oleo

> Termos organizados por categoria. Referencia para destravar relatorios StoneX e fontes publicas.
> Estrela (★) = termo critico, voce vai cruzar com ele todo dia.

---

## 1. Unidades e equivalencias

| Termo | Definicao |
|---|---|
| **Bushel (bu)** ★ | Unidade USA. Soja: 60 lbs = 27,2 kg. Milho/trigo: 56 lbs. **Soja: 1 bu ≈ 0,4536 sacas de 60 kg** (ou 1 saca ≈ 2,2046 bu) |
| **Short ton** ★ | 2.000 lbs = 907 kg. Unidade do farelo no CBOT |
| **Metric ton (MT)** | 1.000 kg = 2.204,6 lbs. Usado fora dos EUA |
| **Pound (lb)** | 0,4536 kg. Unidade do oleo no CBOT (60.000 lbs/contrato) |
| **Saca (BR)** ★ | 60 kg |
| **Hectare (ha)** | 10.000 m² (Brasil/Argentina) |
| **Acre (USA)** | 4.046 m² (1 ha ≈ 2,471 acres) |
| **Cent / point** | Cent = 1/100 dolar. Em soja CBOT cotacao em cents/bu (ex: 1.350 = US$ 13,50/bu) |

**Conversoes rapidas:**
- Soja $/bu → $/saca: × 1,3228 (1 saca / 0,4536 = 1,3228)
- Soja $/bu → $/ton: × 36,7437
- Farelo $/short ton → $/MT: × 1,1023
- Oleo cts/lb → $/MT: × 22,046

---

## 2. Mercado fisico (cash market)

| Termo | Definicao |
|---|---|
| **Basis** ★ | Diferenca entre preco fisico local e futuro CBOT do vencimento proximo. Positivo = premio, negativo = desconto |
| **Premio porto** ★ | Versao brasileira do basis: quanto FOB Paranagua paga acima/abaixo do CBOT. Cotado em cts/bu |
| **Spot** | Preco a vista, entrega imediata |
| **Forward** | Compra com entrega futura (sem ser via bolsa). Comum em contratos com produtor |
| **FOB** ★ | Free On Board. Preco entregue no navio em porto de origem. Comprador paga o frete maritimo |
| **CFR / CIF** | Cost and Freight / Cost, Insurance, Freight. Preco entregue no porto destino |
| **Paranagua FOB** ★ | Referencia de exportacao brasileira |
| **CFR China** | Preco entregue na China. = FOB Brasil + frete Panamax + outros |
| **Originacao** | Atividade de comprar soja do produtor (origina o gao para tradings/esmagadoras) |
| **Truck premium / spread** | Diferencial pago para entrega via caminhao vs ferrovia |
| **Calado** | Profundidade do rio. Mississippi (EUA) e Tapajos (BR) tem epoca de calado baixo que sobe frete |

---

## 3. Mercado futuro (CBOT / B3)

| Termo | Definicao |
|---|---|
| **Contrato** | Padronizado. Soja CBOT = 5.000 bu, farelo = 100 ston, oleo = 60.000 lbs |
| **Tick / tick size** | Menor variacao de preco. Soja = 1/4 cent ($12,50 por contrato) |
| **Vencimento** ★ | Data em que contrato expira. Soja: F H K N Q U X (jan, mar, mai, jul, ago, set, nov) |
| **Front month** | Vencimento mais proximo, geralmente mais liquido |
| **Rollover** | Trocar posicao do front month para o proximo vencimento antes de expirar |
| **Open interest** | Numero de contratos em aberto. Indicador de liquidez |
| **Margin / margem** | Garantia depositada na corretora para manter posicao aberta |
| **Limit move / circuit breaker** | Variacao maxima diaria permitida (ex: 60 cents na soja). Se atingir, mercado para temporariamente |
| **Settlement** | Preco de fechamento oficial usado para ajuste de margem |
| **Contango** ★ | Vencimentos distantes mais caros. Sinaliza estoque folgado, custo de carrego |
| **Backwardation** ★ | Vencimentos distantes mais baratos. Sinaliza aperto, urgencia |
| **Inversao** | Sinonimo de backwardation |
| **Spread** ★ | Diferenca entre dois vencimentos ou dois ativos |
| **Crush spread** ★ | Long farelo + long oleo + short soja. Replica margem de esmagamento |
| **Inter-month spread** | Ex: comprar julho/26 e vender novembro/26 |
| **Hedge** ★ | Trava de preco. Produtor vende futuro para fixar preco da safra |
| **Especulador** | Quem opera sem posicao fisica, busca lucro com variacao |
| **Long / short** | Comprado / vendido |

---

## 4. Fundamentos (oferta e demanda)

| Termo | Definicao |
|---|---|
| **Crush margin / Board crush** ★ | (Preco farelo × 0,022) + (Preco oleo × 11) − Preco soja. Em $/bu |
| **Oil share** ★ | % do valor crush vindo do oleo. Historico ~33%, atual ~45-50% |
| **Esmagamento** ★ | Processo de quebrar soja em farelo + oleo |
| **Capacidade ociosa** | Esmagadoras param/voltam conforme margem |
| **Ending stocks** ★ | Estoque final projetado para o ano-safra. Variavel mais olhada do WASDE |
| **Stocks-to-use** ★ | Estoque final / consumo anual. <5% = apertado, >15% = folgado |
| **Carryover / estoque de passagem** | Estoque que sobra da safra anterior |
| **Ano-safra** | EUA: set/ago. Brasil: fev/jan. Argentina: abr/mar |
| **Producao** | Area × produtividade |
| **Produtividade (yield)** ★ | bu/acre (EUA) ou sacas/ha (BR). Soja BR media ~58 sc/ha; EUA ~50 bu/ac |
| **Area plantada** | Hectares ou acres |
| **Crop year** | Sinonimo de ano-safra |
| **Velha safra / nova safra** | Old crop / new crop. Importante na transicao |

---

## 5. Releases e fontes de dados

| Termo | Definicao |
|---|---|
| **WASDE** ★ | World Agricultural Supply and Demand Estimates. USDA, mensal |
| **Crop Progress** ★ | USDA NASS, semanal. Estagio e condicao da lavoura EUA |
| **Prospective Plantings** | USDA, fim de marco. Intencao de plantio EUA (move muito) |
| **Acreage** | USDA, fim de junho. Area plantada confirmada |
| **NOPA Crush** ★ | National Oilseed Processors Association. Mensal, ~dia 15. Esmagamento EUA |
| **NASS Crush** | USDA oficial. Mensal, ~dia 1-3 |
| **Export Sales** ★ | USDA FAS. Semanal, quintas. Vendas EUA |
| **Export Inspections** | Embarques EUA. Segunda |
| **Cattle on Feed** | Demanda de farelo via pecuaria EUA |
| **COT report** ★ | Commitments of Traders, CFTC, sexta. Posicao de fundos |
| **Conab** ★ | Companhia Nacional de Abastecimento, BR. Mensal |
| **CEPEA/ESALQ** | Centro de Estudos Avancados em Economia Aplicada. Indicadores diarios |
| **BCBA / Bolsa de Cereales** | Argentina. Semanal/quinzenal |
| **MARA / China customs** | Importacao da China por origem |

---

## 6. Macro e politica

| Termo | Definicao |
|---|---|
| **Tarifa** | Taxa sobre importacao. Trump 2018-19 tarifou soja USA → China comprou Brasil |
| **Retenciones** ★ | Imposto argentino sobre exportacao de soja/farelo/oleo. Alta retencion freia exportador |
| **RFS / RIN** | Renewable Fuel Standard / Renewable Identification Number. EUA biodiesel |
| **B14 / B15** | Mandato brasileiro de % de biodiesel no diesel. Move demanda de oleo |
| **HVO / renewable diesel** ★ | Hydrotreated vegetable oil. Demanda crescente, puxou oil share |
| **Baltic Dry Index** | Indice de frete maritimo a granel |
| **Panamax / Capesize** | Tipos de navio. Soja viaja em Panamax |
| **DXY / dollar index** | Forca do dolar. Dolar forte = commodities pressionadas |
| **DCE (Dalian)** | Bolsa chinesa. Cota farelo e oleo de soja em yuan |

---

## 7. Tecnicalidades de negociacao

| Termo | Definicao |
|---|---|
| **Limit up / limit down** | Variacao maxima diaria atingida |
| **Gap** | Abertura significativamente acima/abaixo do fechamento anterior |
| **Volume** | Numero de contratos negociados |
| **Pit / electronic / Globex** | Pregao viva-voz (extinto) vs eletronico (atual) |
| **Spec / spec money** | Dinheiro especulativo (fundos) |
| **Trend follower** | Fundos que seguem tendencia (CTAs) — movem muito o mercado |
| **Funds net long/short** | Posicao liquida dos fundos no COT |

---

## 8. Climaticos

| Termo | Definicao |
|---|---|
| **El Nino** ★ | Aquecimento Pacifico Equatorial. Em geral: chuvas no Sul BR/ARG, seca no Norte BR |
| **La Nina** ★ | Resfriamento Pacifico. Em geral: seca Sul BR/ARG, chuva Norte BR |
| **ENSO** | El Nino / Southern Oscillation (o ciclo) |
| **Polinizacao (EUA, jul)** | Janela critica para soja USA. Seca em jul = perda direta de produtividade |
| **Enchimento de vagem (BR, jan-fev)** | Janela critica para soja BR |
| **Veranico** | Periodo seco no meio da estacao chuvosa |
| **Geada** | Mais perigosa para milho safrinha (jul); soja BR sai antes da geada |
| **GFS / ECMWF** | Modelos meteorologicos (americano e europeu) |

---

## 9. Aspectos contratuais brasileiros

| Termo | Definicao |
|---|---|
| **CPR** | Cedula de Produto Rural. Titulo de venda antecipada da safra |
| **Barter** | Troca: insumo agora por soja na colheita. Modelo comum |
| **Soja verde** | Venda antes de plantar/durante o ciclo |
| **Soja entregue** | Compra na hora da colheita |
| **Premio fixado** | Operacao em que ja se travou o basis mas nao o futuro CBOT (ou vice-versa) |
| **Embarque** | Confirmacao de chegada no porto/navio |
| **Murcho** | Termo gaucho para soja com baixa umidade ou perdida |

---

## 10. Termos do biodiesel

| Termo | Definicao |
|---|---|
| **B100** | Biodiesel puro |
| **HVO** | Oleo vegetal hidrogenado (renewable diesel) — virou demanda gigante 2023-25 |
| **SAF** | Sustainable Aviation Fuel — proximo mercado, ainda incipiente |
| **CARB** | California Air Resources Board — credito de carbono que premia oleo de baixa intensidade |
| **LCFS** | Low Carbon Fuel Standard California |
| **RIN D4** | Credito biodiesel especifico |

---

> **Convencao:** quando ler um relatorio StoneX e topar com termo nao listado aqui, **adicione na proxima revisao**. Esse glossario cresce com voce.
