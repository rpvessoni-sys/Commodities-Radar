# Fontes Confiaveis — Alem do StoneX

> Curadoria > quantidade. Cada fonte adicional aumenta custo, ruido, manutencao.
> So entra se trouxer **dado unico que move preco**. Sem redundancia.

---

## 1. Principio de selecao

- **1 fonte primaria por tipo de dado** (se WASDE diz X, nao precisamos 3 consultorias repetindo)
- **Tier 1 sempre primeiro**: dado oficial > industria > bolsa > consultoria privada > imprensa
- **Cobertura geografica obrigatoria**: EUA + Brasil + Argentina + Asia (China, India, Indonesia, Malasia)
- **Tudo gratuito sempre que possivel**; pagos so se cobrirem gap real
- **Imprensa entra para CONTEXTO, nao para dado primario**

---

## 2. Cobertura por dimensao — fontes recomendadas

### A) OFERTA — producao, area, estoque, esmagamento

| Fonte | Tier | Cobertura | Cadencia | Acesso |
|---|---|---|---|---|
| **USDA WASDE** ★★★ | 1 | Global S&D, oficial | Mensal (10-12) | Livre |
| **USDA NASS — Crop Progress** ★★★ | 1 | EUA lavoura | Seg ~16h NY (abr-nov) | Livre |
| **USDA NASS — Acreage / Plantings** ★★★ | 1 | Area plantada EUA | Mar e jun | Livre |
| **USDA NASS — Crush Report** ★★ | 1 | Esmagamento oficial EUA | Mensal | Livre |
| **NOPA Crush** ★★★ | 2 | Esmagamento EUA (industria) | Mensal ~dia 15 | Livre (nopa.org) |
| **Conab — Acompanhamento de Safra** ★★★ | 1 | Producao BR | Mensal | Livre |
| **ABIOVE — Estatisticas** ★★★ | 2 | Esmagamento, export, estoque BR | Mensal | Livre (abiove.org.br) |
| **ANEC — Embarques** ★★ | 2 | Exportacao graos BR | Semanal | Livre (anec.com.br) |
| **Bolsa de Cereales BCBA** ★★ | 1 | Lavoura Argentina | Semanal/quinzenal | Livre |
| **Bolsa de Comercio Rosario (BCR)** ★★ | 2 | Industria + mercado AR | Mensal | Livre |
| **MPOB (Malasia)** ★★ | 1 | Palma producao/estoque/export | Mensal (~dia 10) | Livre |
| **GAPKI (Indonesia)** ★ | 2 | Palma producao Indonesia | Mensal | Livre |
| **IBGE — LSPA** | 1 | Safra BR (oficial estatistico) | Mensal | Livre |

### B) DEMANDA — importacoes, crush externo, biocombustivel

| Fonte | Tier | Cobertura | Cadencia | Acesso |
|---|---|---|---|---|
| **USDA Export Sales** ★★★ | 1 | Vendas externas EUA | Semanal Qui 8:30 NY | Livre |
| **USDA Export Inspections** ★★ | 1 | Embarques EUA | Semanal Seg 11h NY | Livre |
| **China Customs (GACC)** ★★★ | 1 | Import China por origem | Mensal (~dia 20) | Livre (en inglês) |
| **MARA China** ★ | 1 | Producao + politica China | Mensal | Livre |
| **EIA — Biocombustiveis** ★★ | 1 | Producao BD/HVO + projecoes EUA | Mensal STEO + anual | Livre |
| **EPA — RFS/RVO/RIN** ★★★ | 1 | Regulamentacao biocombustivel EUA | Pontual | Livre |
| **ANP — Combustiveis** ★★ | 1 | BR biodiesel/B15/preco | Continuo | Livre |
| **MPOB — Exportacao palma** ★★ | 1 | Demanda externa palma | Mensal | Livre |
| **Comex Stat (MDIC)** ★★ | 1 | Exportacao/importacao BR | Mensal | Livre |
| **GMK / China Crush Margin (publico)** ★ | 4 | Margem esmagadora China | Variavel | Livre limitado |

### C) PRECO — futuros e fisico

| Fonte | Tier | Cobertura | Cadencia | Acesso |
|---|---|---|---|---|
| **CME Group (CBOT)** ★★★ | 3 | Soja S, farelo SM, oleo BO | Diario | Web delay 10min livre; real-time pago |
| **B3** ★★ | 3 | SFI soja Brasil | Diario | Web delay; data feeds pagos |
| **Bursa Malaysia (BMD)** ★★ | 3 | Palma FCPO | Diario | Web livre |
| **DCE Dalian (China)** ★ | 3 | Farelo + oleo de soja China | Diario | Web livre limitado |
| **MATBA-Rofex (Argentina)** ★ | 3 | Soja AR | Diario | Web livre |
| **CEPEA/ESALQ** ★★★ | 2 | Indicadores fisicos BR (soja, milho, oleo, etc) | Diario | Livre |
| **Aboissa** ★★ | 4 | Precos fisicos oleos BR (StoneX usa) | Semanal | Web livre limitado |
| **AgRural Daily** ★ | 4 | Comentario CBOT + premios BR | Diario | Pago (assinatura) |

**Notas sobre precos:**
- CME Group oferece cotacao delay 10min gratuita via web — suficiente para nosso uso (nao operamos direto)
- yfinance (lib Python) tem cotacoes CBOT decentes para historico
- Real-time exige feed pago (TradingView Pro, eSignal, Refinitiv)

### D) CLIMA

| Fonte | Tier | Cobertura | Cadencia | Acesso |
|---|---|---|---|---|
| **NOAA CPC — 6-10 day outlook** ★★★ | 1 | EUA + global | Diario | Livre |
| **NOAA — ENSO Diagnostic** ★★★ | 1 | El Nino / La Nina | Mensal (1a quinta) | Livre |
| **NOAA Climate.gov** ★★ | 1 | Analises | Continuo | Livre |
| **Inmet** ★★ | 1 | Brasil (oficial) | Diario | Livre |
| **CPTEC/INPE** ★★ | 1 | Modelos Brasil | Diario | Livre |
| **GFS / ECMWF (modelos)** ★★ | 1 | Modelos numericos globais | 4x/dia | Livre via varios sites |
| **Climatempo Pro** ★ | 4 | BR detalhado | Diario | Pago |
| **Maxar Weather** ★ | 4 | Global (tradings usam) | Diario | Pago |

### E) MACRO

| Fonte | Tier | Cobertura | Cadencia | Acesso |
|---|---|---|---|---|
| **BCB — SGS / focus** ★★★ | 1 | Cambio, juros, expectativas BR | Diario | Livre (api) |
| **FRED (St Louis Fed)** ★★ | 1 | Macro EUA | Diario | Livre (api) |
| **Baltic Exchange — Baltic Dry Index** ★★ | 2 | Frete maritimo global | Diario | Livre (delay) |
| **EIA — Petroleo + diesel + gasolina** ★★ | 1 | Energia EUA | Semanal | Livre |
| **OPEC Monthly Report** ★ | 2 | Petroleo global | Mensal | Livre |
| **Tesouro Nacional** ★ | 1 | Divida BR, politica fiscal | Variado | Livre |

### F) POLITICA E REGULACAO

| Fonte | Tier | Cobertura | Cadencia | Acesso |
|---|---|---|---|---|
| **Diario Oficial da Uniao (DOU)** ★★ | 1 | Regulacao BR | Diario | Livre |
| **EPA / EIA EUA** ★★★ | 1 | RFS/RVO/RIN/45Z | Pontual | Livre |
| **MAPA BR** ★ | 1 | Politica agricola BR | Pontual | Livre |
| **ANP — consultas/resolucoes** ★★ | 1 | Mistura combustiveis BR | Pontual | Livre |
| **USTR / China Trade** ★ | 1 | Acordos comerciais | Pontual | Livre |

### G) POSICIONAMENTO DE MERCADO

| Fonte | Tier | Cobertura | Cadencia | Acesso |
|---|---|---|---|---|
| **CFTC COT report** ★★★ | 1 | Posicao fundos EUA | Sex 15:30 NY | Livre |
| **CME Open Interest** ★★ | 3 | OI por contrato | Diario | Livre |
| **NYMEX/ICE COT** ★ | 1 | Petroleo, combustiveis | Sex | Livre |

### H) IMPRENSA ESPECIALIZADA (contexto, baixa frequencia)

| Fonte | Tier | Uso |
|---|---|---|
| **Noticias Agricolas (BR)** | 5 | Contexto + opinioes |
| **Globo Rural** | 5 | Popular |
| **Valor Economico — Agro** | 5 | Financeiro BR |
| **Reuters Agriculture** | 5 | Global, ingles |
| **Bloomberg Agriculture** | 5 | Premium (cobertura larga) |
| **AgriCensus** | 4 | Mercados fisicos globais (pago) |
| **World Grain** | 5 | Industria moinhos |
| **Hellenic Shipping News** | 5 | Frete maritimo |

---

## 3. Stack core proposto (Tier 1+2 obrigatorios, todos gratuitos)

**Imediato (Fase 1):**
- StoneX (email) — fonte primaria privada
- USDA WASDE + NASS + Export Sales — base oficial global
- NOPA Crush — esmagamento EUA industria
- Conab + ABIOVE + ANEC — Brasil
- Bolsa de Cereales (BCBA) — Argentina
- CEPEA/ESALQ — preco fisico BR
- CME (yfinance) — preco CBOT
- CFTC COT — posicionamento
- NOAA CPC — clima EUA + ENSO
- Inmet — clima BR
- BCB — cambio/juros
- EPA + ANP — regulacao biocombustivel
- China Customs — importacao
- MPOB — palma Malasia

**Total: 14 fontes core, todas gratuitas.**

**Fase 2 (se relevante):**
- Bursa Malaysia preco
- DCE Dalian preco
- GAPKI (Indonesia palma)
- BCR (Rosario AR)
- Baltic Dry Index
- FRED

**Fase 3+ (opcional, pago):**
- Climatempo Pro (se clima virar gap critico)
- AgriCensus (mercados fisicos globais)

---

## 4. O que decidimos NAO usar (e por que)

- **Twitter/X de "analistas"**: ruido alto, dificil curar. Talvez fase 3+ com lista curada
- **Newsletters terceirizadas que recapitulam dados publicos**: pagamos ou pegamos direto na fonte
- **Sites de cotacao agregadora (Investing.com, etc)**: dados sao da CME, melhor pegar direto
- **Forums e grupos WhatsApp**: alta variancia de qualidade
- **Bloomberg Agriculture (premium)**: USD 24k/ano. Nao justifica para nosso escopo
- **Refinitiv Eikon**: USD 22k/ano. Mesmo motivo
- **AgRural Daily**: pago, recapitula CBOT — StoneX ja cobre

---

## 5. Status de acesso por fonte (a confirmar)

**Voce ja tem conta/cadastro em:**
- [ ] USDA (gratuito, so cadastro)
- [ ] NOPA (livre, sem cadastro)
- [ ] Conab (livre)
- [ ] ABIOVE (livre)
- [ ] CEPEA (livre)
- [ ] CFTC (livre)
- [ ] NOAA (livre)
- [ ] BCB (livre, com API)
- [ ] EPA (livre)
- [ ] ANP (livre)
- [ ] China Customs (livre)
- [ ] MPOB (livre)

**Pagos que voce tem (alem do StoneX corporativo)?**
- [ ] Climatempo Pro?
- [ ] AgRural?
- [ ] AgriCensus?
- [ ] Outro?

---

## 6. Padrao de acesso programatico (por tipo)

| Tipo | Como integrar | Estabilidade |
|---|---|---|
| **API oficial** (BCB, FRED, USDA via API) | requests / SDK | Altissima |
| **CSV/Excel download** (Conab, NOPA reports) | requests + pandas | Alta |
| **HTML scrape** (BCBA, Aboissa) | requests + BeautifulSoup | Media |
| **RSS** (alguns blogs USDA) | feedparser | Alta |
| **Email subscription** (StoneX, alertas) | IMAP / Gmail API | Alta |
| **Twitter/X** | API V2 (limitado, pago) | Baixa |

---

## 7. Antipadroes de fonte (NAO fazer)

- ❌ Adicionar 5 consultorias dizendo a mesma coisa do WASDE — vira ruido
- ❌ Coletar dado horario que so atualiza diariamente — desperdicio
- ❌ Usar agregador como fonte (Investing.com, etc) — perde confiabilidade
- ❌ Confiar em fonte unica para decisao critica — sempre cruzar 2-3 fontes
- ❌ Misturar opiniao com dado (relatorio com bullets nao e fonte primaria, e analise)

---

## 8. Acao do usuario

**Quando confirmar a lista de fontes:**

1. Validar que as 14 do "core" fazem sentido para sua realidade
2. Marcar se ja tem cadastro/acesso em alguma
3. Marcar se assina algo pago alem do StoneX (Climatempo? AgRural? algo da empresa que voce possa usar?)
4. Listar nomes especificos de analistas Twitter/X que voce gostaria de monitorar (mesmo que seja fase 3+)
