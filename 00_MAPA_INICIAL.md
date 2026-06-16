# Mapa Inicial — Mercado de Soja, Farelo e Oleo

> Baseline conceitual para calibrar vocabulario antes de mergulhar nos relatorios StoneX.
> Foco: o que um outsider do mercado financeiro precisa saber pra entender uma tese.

---

## 1. Como ler este documento

Voce ja conhece o lado fisico do agro. O que provavelmente falta e:
- Como **os 3 produtos se conectam** (crush)
- Como **se forma o preco** (CBOT + basis + macro)
- Quem **publica os dados** que movem o mercado
- Como **ler uma tese** semanal de consultor

Esse documento responde isso. Volume: ~15min de leitura.

---

## 2. Os 3 produtos sao 1 produto

A soja **so vale a pena se for processada**. O mercado real e o crush:

```
1 bushel de soja (60 lbs / ~27,2 kg)
         │
         ▼  esmagamento
         │
    ┌────┴────┬─────────────┐
    ▼         ▼             ▼
  44 lbs    11 lbs       ~5 lbs
  FARELO    OLEO         cascas/perdas
  (73%)     (18%)        (9%)
```

**Por isso, qualquer tese de soja precisa olhar os 3 simultaneamente.** Se o oleo dispara (biodiesel forte), o esmagador esmaga mais → sobra farelo no mercado → farelo cai. E vice-versa.

A variavel mestre que conecta tudo:

### Crush margin (Board Crush)

```
Crush ($/bu) = (Preco farelo $/short ton × 0,022) 
             + (Preco oleo $/lb × 11) 
             − Preco soja $/bu
```

**Quanto maior o crush, mais incentivo para esmagar.** Em 2023-24 chegou a $2/bu (gordo). Historico longo gira em $0,40-0,80/bu. Esmagadora hedga essa margem comprando soja futuro e vendendo farelo + oleo futuro simultaneamente.

### Oil share
Percentual do valor do crush que vem do oleo:
- Historico longo: ~33%
- Atual (mandato biodiesel): ~45-50%
- Importa porque mostra **quem manda no preco da soja**: se oil share alto, demanda de oleo (biodiesel) puxa esmagamento, o que pressiona farelo

---

## 3. Onde se forma o preco

### 3.1 CBOT (Chicago Board of Trade — hoje CME Group)
**A referencia global.** Tudo se precifica em relacao a Chicago.

| Produto | Ticker | Unidade do contrato | Tick size | Vencimentos |
|---|---|---|---|---|
| Soja | **ZS** (eletronico) / S | 5.000 bushels | 1/4 cent = $12,50 | F H K N Q U X (jan-mar-mai-jul-ago-set-nov) |
| Farelo | **ZM** / SM | 100 short tons | $0,10/ton = $10 | F H K N Q U V Z (jan-mar-mai-jul-ago-set-out-dez) |
| Oleo | **ZL** / BO | 60.000 lbs | 0,01 cent/lb = $6 | F H K N Q U V Z (mesmo do farelo) |

> **Codigo de mes** (padrao futuros): F=jan, G=fev, H=mar, J=abr, K=mai, M=jun, N=jul, Q=ago, U=set, V=out, X=nov, Z=dez.

**Contrato mais negociado em cada momento** ("front month") rola conforme se aproxima do vencimento. Liquidez concentra em poucos vencimentos por vez.

### 3.2 B3 (Brasil)
- **SFI** — Soja em graos Sul, contrato B3. Liquidez baixa comparada a CBOT. Maioria do hedge brasileiro e feito direto em Chicago.
- Tem tambem milho (CCM) que serve de proxy para custo de racao (compete com farelo na pecuaria).

### 3.3 Mercado fisico (cash market)
Preco real pago em porto/interior. Sempre cotado como **basis** em relacao a CBOT:

```
Preco fisico = CBOT (futuro proximo) ± basis
```

- **Basis positivo (premio)**: comprador disposto a pagar acima de Chicago. Sinal de demanda forte ou oferta apertada.
- **Basis negativo (desconto)**: oferta excedente, escoamento dificil.

Principais "praças" no Brasil:
- **Paranagua FOB** — referencia de exportacao
- **Rio Grande FOB** — segundo porto, RS
- **Santos** — mais oleo e farelo
- **Rondonopolis** — hub do interior MT, base para farelo
- **Sorriso/MT** — referencia preco no produtor

CFR China = preco entregue na China (inclui frete maritimo). Quando China compra, FOB Brasil + frete Panamax determina paridade.

### 3.4 Spread inter-commodity
- **Crush spread**: posicao comprada em farelo+oleo e vendida em soja (replica crush margin)
- **Oil/Meal spread**: relativo entre oleo e farelo
- **Soy/Corn ratio**: razao soja/milho — produtor americano decide plantio em fev/mar baseado nisso

---

## 4. Quem move o preco (drivers)

### 4.1 OFERTA
**EUA (~35% da producao mundial)**
- Plantio: abril-maio
- Janela critica: **julho** (polinizacao e enchimento de vagem) — clima quente/seco no Midwest mexe preco brutalmente
- Colheita: set-nov
- Estados-chave: Iowa, Illinois, Indiana, Minnesota, Nebraska

**Brasil (~40% da producao mundial, maior exportador)**
- Plantio: set-dez (depende do regime de chuvas)
- Janela critica: **janeiro-fevereiro** (enchimento de vagem)
- Colheita: jan-mai (MT/MS/GO antes; PR/RS depois)
- Estados-chave: MT (35% nacional), PR, RS, GO, MS

**Argentina (~12% da producao)**
- Plantio: nov-jan
- Colheita: mar-jun
- Diferencia: e o **maior exportador de farelo e oleo** (esmagadora gigante em Rosario)

### 4.2 DEMANDA
**China = ~60% da importacao global de soja**
- Importa graos, esmaga internamente (politica de seguranca alimentar)
- Demanda puxada por **plantel de suinos** (gripe suina africana 2018-2019 derrubou demanda, retomou)
- Crush margin chines e termometro: quando esta gordo, China esta esmagando muito, comprando muito

**Biodiesel / biocombustivel**
- EUA: RFS (Renewable Fuel Standard), RIN credits, expansao do "renewable diesel" 2023-24
- Brasil: B14 (atual 14% biodiesel no diesel), mandato sobe progressivamente
- UE: regulacao limita oleo de palma → soja entra

**Trituracao domestica (crush)**
- Esmagadoras precisam de margem positiva pra rodar capacidade
- EUA/Argentina/Brasil tem capacidade ociosa que entra/sai conforme margem

### 4.3 MACRO
- **Dolar / Real**: Brasil exportador → real fraco = exportador feliz, premio cai
- **Frete maritimo (Baltic Dry Index)** e fluvial (calado Mississippi nos EUA, hidrovia Tapajos no Brasil)
- **Frete interno** (ferrovias EUA, custo de caminhao no MT)
- **Energia** (custo de plantio, fertilizante, e bio: input do biodiesel)
- **Juros EUA**: dolar forte = commodities pressionadas
- **Politica**: tarifas (guerra comercial EUA-China 2018-19), retenciones argentinas, restricoes ambientais UE

### 4.4 Clima
- **NOAA** (EUA): previsao 6-10 dias, El Nino/La Nina
- La Nina => seca Sul do Brasil e Argentina; chuva EUA
- El Nino => o oposto
- Em jul (EUA) e jan-fev (BR/ARG), cada front frio ou seco movimenta CBOT

---

## 5. Calendario dos releases que movem preco

> Lista completa no `02_CALENDARIO_RELEASES.md` (proximo). Resumo:

| Release | Fonte | Frequencia | Quando | Foco |
|---|---|---|---|---|
| **WASDE** | USDA | Mensal | 9-12 do mes ~12h NY | Oferta/demanda global, ending stocks |
| **Crop Progress** | USDA | Semanal | Seg ~16h NY (abr-nov) | Estagio + condicao da lavoura EUA |
| **NOPA Crush** | NOPA (industria) | Mensal | ~dia 15 | Esmagamento EUA, estoque de oleo |
| **NASS Crush** | USDA | Mensal | ~dia 1-3 | Esmagamento oficial EUA |
| **Export Sales** | USDA FAS | Semanal | Qui 8:30 NY | Vendas externas EUA |
| **Conab** | Conab BR | Mensal | Meio do mes | Producao Brasil |
| **CONAB Custos** | Conab BR | Pontual | — | Custo de producao |
| **Bolsa Cereales** | BCBA Argentina | Semanal/quinz | — | Lavoura Argentina |
| **China customs** | Aduana China | Mensal | ~dia 20 | Importacao por origem |

**Os 2 grandes choques previsiveis:**
1. **WASDE em janeiro** (anual production report) — historicamente o mais volatil
2. **Prospective Plantings (USDA)** — fim de marco, define area EUA

---

## 6. Como ler uma tese de mercado

Uma tese boa responde 4 perguntas:

### 6.1 Onde estamos no ciclo?
- Safra EUA terminou? Safra BR plantando? Argentina colhendo?
- Estoques globais em que nivel (apertados ou folgados)?
- Crush margin gorda ou apertada?

### 6.2 Qual o vies dos fundamentos?
- Oferta: clima, area, produtividade, estoques
- Demanda: China, biodiesel, esmagamento
- Estoque/uso (stocks-to-use ratio) — abaixo de 5% e MUITO apertado

### 6.3 O que o mercado ja precificou?
- Se WASDE vem amanha esperando estoque apertado, e o preco ja subiu 10% nos ultimos 15 dias, surpresa positiva pode dar venda ("buy the rumor, sell the news")
- COT report (CFTC, sexta) mostra posicao de fundos especulativos — extremos indicam reversao

### 6.4 Onde o risco esta?
- Cenarios alternativos (clima, China cancela, retenciones mudam)
- Niveis tecnicos (suporte/resistencia)
- Eventos calendarizados nos proximos 30 dias

---

## 7. Vocabulario de bolso (essencial)

- **Bushel (bu)**: unidade USA. Soja: 1 bu = 60 lbs = 27,2 kg ≈ 0,453 sacas de 60 kg
- **Short ton**: 2.000 lbs = 907 kg (farelo)
- **Saca (BR)**: 60 kg
- **Basis**: diferenca preco fisico vs futuro CBOT
- **Premio porto**: equivalente ao basis para venda FOB
- **FOB / CFR / CIF**: termos de entrega (Free On Board / Cost and Freight / Cost Insurance Freight)
- **Hedge**: trava de preco via futuros
- **Crush margin / Board crush**: margem de esmagamento
- **Oil share**: % do valor crush vinda do oleo
- **Stocks-to-use**: estoque final / consumo anual
- **Ending stocks**: estoque final projetado
- **WASDE**: World Agricultural Supply and Demand Estimates
- **NOPA**: National Oilseed Processors Association (EUA)
- **CFTC / COT**: Commodity Futures Trading Commission / Commitments of Traders
- **Rollover**: trocar posicao do vencimento proximo para o seguinte
- **Contango**: vencimentos distantes mais caros que proximos (mercado normal/folgado)
- **Backwardation**: vencimentos distantes mais baratos (mercado apertado, urgencia)

---

## 8. Mapa dos players principais

### Tradings globais ("ABCD+")
- **ADM** (USA)
- **Bunge** — fusao com Viterra/Glencore anunciada em 2023
- **Cargill** (USA, privada)
- **Louis Dreyfus** (LDC)
- **COFCO** (China, estatal)

### Brasil
- **Amaggi** (Maggi family, MT)
- **ALZ Graos** (Alianca)
- **Caramuru, Coamo, C.Vale** (cooperativas e regionais)
- COFCO BR, Bunge BR, Cargill BR — dominam exportacao

### Esmagamento BR (principais)
- Bunge, Cargill, ADM, COFCO, Caramuru, Coamo, C.Vale

---

## 9. Fontes publicas de referencia (gratuitas)

- **USDA WASDE**: https://www.usda.gov/oce/commodity/wasde
- **USDA NASS Crop Progress**: https://www.nass.usda.gov/Publications/National_Crop_Progress/
- **NOPA**: https://www.nopa.org/
- **Conab**: https://www.conab.gov.br/info-agro/safras
- **CEPEA/ESALQ**: https://www.cepea.esalq.usp.br/
- **CFTC COT**: https://www.cftc.gov/MarketReports/CommitmentsofTraders
- **Bolsa de Cereales Argentina**: https://www.bolsadecereales.com/
- **NOAA Climate Prediction Center**: https://www.cpc.ncep.noaa.gov/
- **CME Group (CBOT cotacoes)**: https://www.cmegroup.com/markets/agriculture/oilseeds.html

---

## 10. Proximos passos

1. **Voce me envia 1-2 relatorios StoneX completos** (cola texto ou screenshot). Vou:
   - Mapear estrutura (secoes fixas, dados-chave)
   - Identificar jargao do consultor
   - Marcar **o que e proprietario StoneX** vs o que e consenso publico
   - Identificar **gaps que sistema precisa preencher** (fontes publicas)

2. **Eu produzo o `02_CALENDARIO_RELEASES.md`** com datas exatas dos releases dos proximos 60-90 dias — calendario que voce instala no seu calendario pessoal.

3. **Eu produzo o `01_GLOSSARIO.md`** expandido (este e bolso, glossario sera referencia).

4. **Depois disso**: Ficha de Tese estrategica + decisao de arquitetura tecnica.

---

> Documento vivo. Atualizar conforme aprende. Marcar duvidas no `_DUVIDAS.md` (criar quando surgir a primeira).
