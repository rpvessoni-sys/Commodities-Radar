# Arquitetura Tecnica — Commodities Radar

> Stack tecnico preliminar. Validar antes de comecar a codar.
> Atualizado: 2026-05-20.

---

## 1. Decisao de acesso ao StoneX

> **ATUALIZACAO 2026-05-20**: caminho A (email parsing) INVALIDADO. StoneX so envia notificacao dizendo "relatorio saiu", nao o conteudo. Ver `08_CAMINHO_INGESTAO.md` para alternativas detalhadas.

### Principal — Drop manual via bookmarklet (caminho C+)
- Usuario clica num bookmarklet no portal → download automatico do HTML
- Arquivo cai em `commodities-radar/inbox/` (ou Downloads e ele move)
- Watcher monitora pasta, processa novos arquivos automaticamente
- Tempo: ~30-60s por relatorio

### Nivel 2 — Claude in Chrome MCP (sob demanda)
- Usuario abre StoneX no Chrome (sessao logada)
- Invoca o assistente via Claude Code
- Sistema usa MCP `Claude_in_Chrome` para extrair conteudo da pagina ativa
- Mais ergonomico que copy-paste, mas requer invocacao manual

### Email de notificacao — uso secundario
- Sistema le notificacoes via IMAP
- Quando chegar notificacao, envia alerta para o usuario (Telegram/console)
- Usuario clica no bookmarklet
- Pipeline processa o HTML baixado

### Por que NAO scraping autenticado (caminho B)
- Conta corporativa → risco de banimento por ToS
- Layout HTML pode mudar → manutencao alta
- 2FA / detecao de bot
- Risco profissional > ganho tecnico

---

## 2. Stack tecnologico

### Linguagem
**Python 3.11+** — padrao para data + LLM + scraping leve

### Bibliotecas core
- `imaplib` ou `google-api-python-client` (Gmail)
- `beautifulsoup4` + `lxml` (parse HTML)
- `anthropic` (LLM Claude para sintese)
- `pandas` (dados estruturados)
- `sqlite3` (storage local, sem precisar de servidor)
- `playwright` (apenas para fontes publicas que precisam JS, NAO StoneX)
- `feedparser` (RSS de USDA, Conab quando disponivel)
- `schedule` ou `apscheduler` (cron interno)

### Bibliotecas de UI/saida (decidir)
- Opcao 1: **Markdown diario** em pasta + visualizador (Obsidian, VS Code)
- Opcao 2: **Email diario** auto-enviado as 7h
- Opcao 3: **Telegram bot** push
- Opcao 4: **Streamlit** dashboard local (porta 8501)

**Recomendacao**: comecar com **Markdown diario** (mais simples, integra com tese journal). Adicionar email/Telegram depois.

---

## 3. Estrutura de pastas

```
commodities-radar/
├── README.md
├── 00_MAPA_INICIAL.md
├── 01_GLOSSARIO.md
├── 02_CALENDARIO_RELEASES.md
├── 03_ANALISE_STONEX.md
├── 04_ANALISE_OLEOS_VEGETAIS.md
├── 05_INSIGHTS_CRUZADOS.md
├── 06_ARQUITETURA_TECNICA.md
│
├── tese_journal/                  ← teses pre/pos-evento
│   ├── README.md
│   ├── _TEMPLATE_TESE.md
│   └── 2026-05-20_oleo-soja-cbot-N26-range-correcao.md
│
├── inbox/                          ← drop manual fallback
│   └── (HTMLs colados pelo usuario)
│
├── data/
│   ├── stonex_raw/                 ← HTMLs originais por email/inbox
│   ├── stonex_parsed/              ← JSON estruturado pos-extracao
│   ├── public_sources/             ← USDA, Conab, CEPEA cached
│   ├── prices/                     ← series historicas CBOT, B3
│   └── radar.db                    ← SQLite com schema unico
│
├── system/                         ← codigo
│   ├── __init__.py
│   ├── ingest/                     ← coletores por fonte
│   │   ├── stonex_email.py
│   │   ├── stonex_inbox.py
│   │   ├── usda.py
│   │   ├── conab.py
│   │   ├── cepea.py
│   │   └── cme.py
│   ├── parse/                      ← extracao de dados de HTML/PDF
│   │   ├── stonex_parser.py
│   │   └── ...
│   ├── synth/                      ← sintese com LLM
│   │   ├── daily_report.py
│   │   └── prompts/
│   │       ├── synthesize_daily.txt
│   │       └── thesis_review.txt
│   ├── store/                      ← persistencia
│   │   ├── schema.sql
│   │   └── db.py
│   ├── notify/                     ← saida
│   │   └── markdown_writer.py
│   └── main.py                     ← orquestrador
│
├── reports/                        ← saida diaria
│   └── 2026-05-20_daily.md
│
└── config/
    ├── settings.toml               ← credenciais (gitignored), cadencias
    └── sources.yml                 ← lista de fontes ativas
```

---

## 4. Fluxo de dados (alto nivel)

```
                   ┌──────────────────┐
                   │  StoneX (email)  │
                   └────────┬─────────┘
                            │
                   ┌────────▼─────────┐
                   │  ingest/stonex   │
                   └────────┬─────────┘
                            │
   ┌────────────┐  ┌────────▼─────────┐  ┌─────────────┐
   │   USDA     ├──►   storage SQLite ◄──┤   CEPEA     │
   │  WASDE     │  │    + raw files   │  │   Conab     │
   └────────────┘  └────────┬─────────┘  └─────────────┘
                            │
                   ┌────────▼─────────┐
                   │ synth/daily LLM  │  ← Claude API
                   └────────┬─────────┘
                            │
                   ┌────────▼─────────┐
                   │ reports/daily.md │
                   └────────┬─────────┘
                            │
                            ▼ (futuro: email/Telegram)
```

---

## 5. Cadencias por fonte (preliminar)

| Fonte | Cadencia | Trigger |
|---|---|---|
| StoneX email (todos relatorios) | Imediato no recebimento | IMAP push ou polling 30min |
| Drop manual inbox/ | Tempo real | File watcher |
| USDA WASDE | Mensal (10-12) | Cron + scrape oficial |
| USDA Crop Progress | Semanal Seg 16h NY (abr-nov) | Cron |
| NOPA Crush | Mensal (~dia 15) | Cron |
| CBOT prices (CME) | Diario apos fechamento | Cron 17h NY |
| CEPEA/ESALQ | Diario | Cron 17h BRT |
| Conab | Mensal | Cron |
| NOAA 6-10 dia | Diario | Cron 9h BRT |
| Sintese diaria | 1x/dia 6h BRT | Cron |
| Resumo semanal | Seg 7h BRT | Cron |

---

## 6. LLM (sintese narrativa) — via Claude Code, sem API

**ATUALIZACAO 2026-05-20**: usuario NAO quer usar API key Anthropic separada. Decisao: Claude Code (que ele ja paga via assinatura) e o cerebro de sintese.

### Fluxo
1. `python main.py ingest` → parser + DB
2. `python main.py dump` → gera `data/last_dump.md` (texto completo dos relatorios da semana)
3. Usuario abre Claude Code no diretorio `commodities-radar/`
4. Usuario pede: "le data/last_dump.md e gera sintese diaria seguindo system/prompts/synthesize_daily.txt"
5. Claude Code (este modelo) tem acesso a TODA a memoria do projeto + arquivos 00-08 + tese_journal — gera sintese cruzada de qualidade
6. Salva resultado em `reports/YYYY-MM-DD_daily.md`

### Vantagens
- Zero custo adicional (subscription Claude Code ja paga)
- Privacidade: dados nao saem do ambiente que ele ja autorizou
- Qualidade: Opus 4.7 com contexto completo do projeto
- Memoria persistente: aprendizado acumula

### Templates / prompts
- `system/prompts/synthesize_daily.txt` — estrutura da sintese diaria
- Futuro: `thesis_review.txt`, `weekly_overview.txt`

---

## 7. Storage (SQLite)

### Tabelas principais
```sql
CREATE TABLE relatorios_stonex (
  id INTEGER PRIMARY KEY,
  tipo TEXT,           -- 'combustiveis' / 'oleos_vegetais' / 'soja' / etc
  data_publicacao DATE,
  data_ingestao TIMESTAMP,
  raw_html_path TEXT,
  texto_extraido TEXT,
  resumo_llm TEXT
);

CREATE TABLE dados_extraidos (
  id INTEGER PRIMARY KEY,
  relatorio_id INTEGER REFERENCES relatorios_stonex(id),
  commodity TEXT,      -- 'oleo_soja_cbot' / 'oleo_palma' / etc
  metric TEXT,         -- 'preco' / 'basis' / 'estoque' / etc
  valor REAL,
  unidade TEXT,
  data_referencia DATE
);

CREATE TABLE precos (
  id INTEGER PRIMARY KEY,
  commodity TEXT,
  mercado TEXT,        -- 'CBOT' / 'B3' / 'Paranagua' / etc
  vencimento TEXT,
  data DATE,
  abertura REAL,
  maxima REAL,
  minima REAL,
  fechamento REAL,
  fonte TEXT
);

CREATE TABLE teses (
  id INTEGER PRIMARY KEY,
  titulo TEXT,
  data_registro DATE,
  data_horizonte DATE,
  arquivo_md TEXT,
  status TEXT,         -- 'ativa' / 'em-revisao' / 'concluida'
  hit BOOLEAN          -- TRUE/FALSE pos-revisao
);
```

---

## 8. Fase de implementacao (proposta)

### Fase 1 — MVP (2 semanas, apos lista de relatorios confirmada)
- [ ] Setup Python env + estrutura de pastas
- [ ] Modulo `ingest/stonex_email.py` (IMAP)
- [ ] Modulo `parse/stonex_parser.py` (BeautifulSoup HTML)
- [ ] Storage SQLite + schema
- [ ] Modulo `synth/daily_report.py` com Claude
- [ ] Cron 1x/dia gera `reports/YYYY-MM-DD_daily.md`
- [ ] Watcher `inbox/` para drop manual

### Fase 2 — Fontes publicas (2 semanas)
- [ ] USDA WASDE scraper
- [ ] NOPA scraper
- [ ] CBOT prices (CME API ou yahoo finance)
- [ ] CEPEA/ESALQ
- [ ] Conab
- [ ] Sintese cruzada StoneX + publico

### Fase 3 — Journaling e tese (1 semana)
- [ ] Comando `criar_tese` que abre template novo
- [ ] Modulo `synth/thesis_review.py` que cruza tese ativa com eventos
- [ ] Alerta D+7 / D+30 automatico

### Fase 4 — Refino + ML (mes 3+)
- [ ] Sistema de feedback (voce marca insight util/inutil)
- [ ] Treino de classificador simples (sklearn) sobre feedback acumulado

---

## 9. Decisoes pendentes

- [ ] Lista completa de relatorios StoneX que o usuario recebe (esperando — usuario faz a noite)
- [ ] Confirmar que email do StoneX e recebido (ou ativar newsletter)
- [ ] Decidir entre Gmail API (mais limpo) ou IMAP generico (mais simples)
- [ ] Escolher formato de saida final (Markdown diario + posterior email/Telegram?)
- [ ] Definir orcamento mensal Claude API (estimativa: ~USD 5-20/mes com caching)

---

## 10. Riscos e mitigacoes

| Risco | Mitigacao |
|---|---|
| StoneX nao envia por email | Fallback C (drop manual) |
| Layout HTML do email muda | Parser tolerante; alert quando extracao falha |
| Conta StoneX bloqueada por erro de uso | Nao automatizar login no portal (so email) |
| Custo Claude API alto | Prompt caching agressivo + Sonnet para tarefas simples |
| Falsa sensacao de expertise (sistema cospe, usuario nao revisa) | Journaling forcado + revisao obrigatoria D+7/D+30 |
| Vazamento de dado proprietario | Nao integrar com nada externo; storage 100% local |
