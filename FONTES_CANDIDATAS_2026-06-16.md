# Fontes públicas candidatas — pesquisa 2026-06-16

> Varredura multi-agente (5 categorias) + verificação adversarial ao vivo (cada URL
> testada: existe? grátis? acessível de datacenter/ScraperAPI? viola ToS?).
> Foco: complexo soja, lente do COMPRADOR de farelo, sem aumentar carga manual,
> sem violar termos (mesma régua do StoneX).

## ✅ RECOMENDADAS (verificadas)

### 1ª leva — alto valor / baixo esforço (sem chave, sem scraper)
| Fonte | Leitura nova | Formato | Esforço |
|---|---|---|---|
| **Argentina FOB oficial** (datos.gob.ar) | preço FOB **diário** de farelo/óleo/soja argentinos → **spread Brasil-Argentina no farelo** (concorrente nº1) | CSV (URL estável) | baixo |
| **ANP biodiesel matéria-prima** | óleo de soja consumido em biodiesel BR por mês/estado → elo **B15→esmagamento→oferta de farelo** + share óleo vs sebo | CSV | baixo |
| **CONAB safra soja BR** | balanço soberano BR (crush doméstico, estoque de passagem) ao lado do WASDE | XLS | baixo |
| **NOAA ONI** | número oficial do ENSO (La Niña/El Niño = driver nº1 da safra argentina/Sul) | HTML tabela | baixo |
| **BCB Focus + SGS** | expectativa de câmbio/Selic (a "curva" do risco em R$) — hoje só temos PTAX realizado | JSON (sem chave) | baixo |

### 2ª leva — alto valor, esforço médio ou chave grátis
| Fonte | Leitura nova | Nota |
|---|---|---|
| **USDA FAS Export Sales (ESR)** | vendas semanais de soja+farelo US **por destino (China!)** — apetite chinês + concorrência de export US | JSON, **chave grátis** (vira secret) |
| **USDA FAS PSD** | balanço **mundial** estruturado de farelo/óleo (substitui extrair do WASDE-PDF) | JSON, chave grátis |
| **Comex Stat (SECEX)** | exportação de farelo BR **por PORTO (Paranaguá)** e país, oficial | POST JSON, WAF → ScraperAPI |
| **SIFRECA frete** | frete rodoviário interior→Paranaguá (R$/t) — explica seu **preço posto PR** que o CBOT não explica | HTML parse |
| **FRED (dólar amplo)** | separa "macro/dólar" de "fundamento soja" no movimento do farelo | JSON, chave grátis |
| **US Drought Monitor** | seca no soybean belt US, semanal (D0-D4) | JSON (testar egress no Actions) |
| **BCR Rosario (GEA)** | zona núcleo argentina (granular; sazonal soja nov-abr) | HTML |
| **BCRA câmbio AR** | câmbio do concorrente (peso retido/vendido = oferta de farelo) | API REST grátis |
| **USDA NASS crush** | crush/estoque farelo US oficial (delta pequeno vs NOPA) | JSON, chave grátis |

## 🟡 TALVEZ (escopo corrigido pelos verificadores)
- **B3** — só tem soja-grão (NÃO farelo) + carregado por JS/token. Serve pra basis nacional da soja.
- **Matba-Rofex AR** — NÃO tem harina/aceite, só soja. Serve como proxy de crush argentino.
- **USDA AMS farelo físico US** — links TXT mortos; via MARS API (chave) ou parse de PDF.
- **Comissão Europeia (farelo UE)** — API de importação não confirmada; provável parse de XLS.
- **ANP vendas diesel** — derivada/apoio (consumo implícito de biodiesel = diesel × mistura).
- **GACC China customs** — TLS quebrado, frágil, alto custo de manutenção.
- **Monitor de Secas BR (ANA)** — shapefile (geopandas), foco histórico no NE; custo/benefício fraco vs INMET.

## ❌ REJEITADAS (não passam — compliance/paywall/bloqueio)
- **CME settlements de opções + CVOL** — HTTP 403 por IP **e os Data Terms of Use da CME proíbem scraping**. Mesmo risco do StoneX → fora. (O dado de skew/vol implícita do farelo seria ótimo, mas não por via legítima.)
- **BiodieselBR** — paywall "exclusivo assinantes".
- **Preço do RIN D4 (EPA)** — dashboard Qlik (JS), sem CSV estável. **Manter RIN D4 como input manual** (já é). O *volume* de RINs D4 (EPA, CSV) entra como proxy.
- **Mysteel (crush China)** — paywall; só headline livre.

## Sequência sugerida
1ª leva (5 acima) primeiro — todas CSV/HTML simples, sem chave, encaixam direto no padrão dos coletores atuais. Depois ESR/PSD (pedem 1 chave grátis cada → secret no GitHub) e Comex/SIFRECA (a peça BR/logística). O resto conforme apetite.
