# Fase 2 — Status de Implementacao das Fontes Publicas

> Estado em 2026-05-21. 14 coletores totais: 2 funcionais, 12 esqueletos.

---

## Coletores funcionais (rodam end-to-end)

### ✅ usda_wasde (NOVO 2026-05-22)
- **Fonte**: Cornell archive XLS (estavel ao longo dos anos)
- **Cadencia**: mensal (9-12)
- **Dados**: Brasil/Argentina/EUA/China x soja/farelo/oleo x 3 anos-safra x 7 metricas (estoque ini, producao, import, crush, total, export, estoque fim)
- **Validado**: 200+ datapoints; producao soja BR 26/27 May = 186 mi t

### ✅ abiove (NOVO 2026-05-22)
- **Fonte**: https://abiove.org.br/abiove_content/Abiove/YYYY.MM-producao_entrega.xlsx
- **Cadencia**: mensal
- **Dados**: balanco BR mensal soja/farelo/oleo (estoque ini/fim, esmagamento, exportacao, etc)
- **Validado**: 147 registros — projecao Brasil 12 meses ate dez/2026

### ✅ cme_cbot
- **Fonte**: Yahoo Finance API (proxy do CME)
- **Cadencia**: diaria
- **Dados**: futuros CBOT — Soja (ZS=F), Farelo (ZM=F), Oleo (ZL=F), Milho (ZC=F), Trigo (ZW=F)
- **Metricas**: abertura, maxima, minima, fechamento, volume
- **Validado**: 2026-05-21 — 300 registros (15 dias x 5 tickers x 4-5 metricas)
- **Exemplo**: soja CBOT 21/05 fechamento 1198.50 cents/bu

### ✅ bcb
- **Fonte**: API publica BCB SGS
- **Cadencia**: diaria
- **Dados**: USD/BRL PTAX (1), Selic diaria (11), IPCA 12m (433), EUR/BRL (21619)
- **Validado**: 2026-05-21 — 40 registros
- **Exemplo**: USD/BRL 20/05 = 5.0301

---

## Esqueletos (estrutura + URL alvo + TODO)

Cada modulo tem docstring com:
- URL/endpoint alvo
- Cadencia esperada
- Dados-chave a extrair
- Plano de implementacao (numeradinho)

Quando precisar de um deles, implementar a partir do TODO.

### ⏳ cftc_cot (semanal sex)
- Fonte: https://www.cftc.gov/files/dea/history/fut_disagg_txt_2026.zip
- Dados: posicao fundos em S/SM/BO
- Esforco estimado: 4-6h

### ✅ cepea_rss (diario) — RESOLVIDO! (2026-05-25)
- **Fonte**: https://www.cepea.org.br/rss.php
- **Cadencia**: diario
- **Dados**: noticias diarias por commodity (soja, milho, boi, etanol, etc) — titulo + descricao + data + valores numericos extraidos por regex
- **Acesso**: via ScraperAPI sem render (1 credit/req)
- **Validado 25/05/2026**: 91 registros (16 commodities, 6 noticias soja)
- **Limitacao**: cobre **sentimento e contexto**, nao preco diario exato. Para preco numerico continuamos com StoneX/ABIOVE/CME

### ❌ cepea (pagina /indicador/) — BLOQUEADO permanente
- Pagina individual de cada indicador bloqueia mesmo via ScraperAPI render+premium
- Substituido pelo cepea_rss para sentimento de mercado
- Para preco numerico exato, depender de StoneX ou ABIOVE

### ⏳ nopa (mensal ~15)
- Fonte: https://www.nopa.org/press_releases/
- Dados: crush EUA + estoque oleo
- Esforco: 4-6h

### ⏳ usda_wasde (mensal 9-12)  ✅ IMPLEMENTADO
- Ver secao "Funcionais" acima.

### ⏳ usda_crop_progress (semanal seg ~16h NY)
- Fonte: API NASS Quick Stats
- Requer: NASS API key (gratuito, registro)
- Dados: estagio + condicao lavoura EUA
- Esforco: 2-4h (API simples)

### ⏳ conab (mensal)  → SUBSTITUIDO POR ABIOVE+WASDE
- Site usa JS dinamico para listar boletins — HTML estatico nao tem URLs
- Cobertura ja atendida: ABIOVE (mensal balanco BR) + WASDE (anual por pais)
- Conab fica como redundancia/refino futuro (producao por UF)

### ⏳ abiove (mensal)  ✅ IMPLEMENTADO
- Ver secao "Funcionais" acima.

### ⏳ anec (semanal sex)
- Fonte: https://anec.com.br/estatisticas/
- Dados: embarques BR por porto
- Esforco: 3-4h

### ⏳ bcba (semanal/quinzenal)
- Fonte: https://www.bolsadecereales.com/
- Dados: lavoura Argentina
- Esforco: 4-6h (provavelmente PDF parser)

### ⏳ noaa_cpc (mensal/diario)
- Fonte: cpc.ncep.noaa.gov
- Dados: outlooks + status ENSO
- Esforco: 4-8h (scraping + analise de texto)

### ⏳ inmet (diario)
- Fonte: https://apitempo.inmet.gov.br/
- Dados: clima BR (chuva, temp)
- Esforco: 3-4h (API estavel)

### ⏳ mpob (mensal ~10)
- Fonte: https://bepi.mpob.gov.my/
- Dados: palma Malasia (producao, estoque, export)
- Esforco: 4-6h

---

## Prioridade sugerida para implementar os esqueletos

### Top 4 (impacto alto, esforco baixo-medio)
1. **usda_crop_progress** — 2-4h, API estavel — rapido
2. **inmet** — 3-4h, API estavel — rapido
3. **cepea** — preco fisico BR diario (cruzamento com StoneX)
4. **cftc_cot** — semanal, sinal tecnico crucial

### Tier 2 (alta complexidade, alto valor)
5. **usda_wasde** — mensal, driver-mestre
6. **nopa** — mensal, dado proprietario industria
7. **conab** — mensal, equivalente brasileiro do WASDE

### Tier 3 (depois)
8. abiove, anec, bcba, noaa_cpc, mpob

---

## Setup tecnico aprendido (Fase 2)

### SSL no Windows
Python 3.12 via winget vem com cert bundle desatualizado. Solucao:
```python
import truststore
truststore.inject_into_ssl()
```
Usa o cert store nativo do Windows. Implementado em `sources/base.py`.

### Estrutura BaseCollector
- Subclass define: `source_name`, `cadence`, `description`, `enabled`
- Implementa: `fetch() -> Iterable[dict]`
- Base provê: `save_to_db()`, `run()` com log + try/except + retorno padronizado

### Schema das tabelas novas
```sql
dados_publicos (fonte, data_referencia, tipo, commodity, metrica, valor, unidade, contexto, raw_json)
coletas_log    (fonte, inicio, fim, status, registros_fetched/saved, erro)
```

Unique constraint em `dados_publicos`: (fonte, data, tipo, metrica, commodity) — evita duplicatas em re-coletas.

### Comandos main.py
```powershell
python main.py public --list         # lista todos coletores
python main.py public --source bcb   # rodar um so
python main.py public                # rodar todos habilitados
python main.py run                   # ingest + synth + dump + check + public
```

---

## Como habilitar um esqueleto quando implementar

1. Editar `system/sources/{nome}.py`
2. Implementar `fetch()` retornando lista de dicts no schema padrao
3. Mudar `enabled = True` na classe
4. Testar: `python main.py public --source {nome}`
5. Verificar no DB: `SELECT * FROM dados_publicos WHERE fonte='{nome}'`

Nenhuma outra alteracao necessaria — registry e CLI ja conhecem todos.
