-- Histórico de relatórios StoneX já ingeridos (série ENCERRADA em 2026-06-05 —
-- extração proibida; tabela fica só-leitura com os 13 registros históricos).
CREATE TABLE IF NOT EXISTS relatorios_stonex (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  tipo TEXT NOT NULL,
  data_publicacao DATE,
  data_ingestao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  raw_html_path TEXT,
  texto_extraido TEXT,
  resumo_llm TEXT,
  UNIQUE(tipo, data_publicacao)
);

-- Limpeza 2026-06-11: removidas as tabelas-fantasma do design original
-- (dados_extraidos, precos, teses, eventos) — 0 linhas e 0 referências em
-- código. Preços vivem em dados_publicos; teses em tese_journal/*.md;
-- eventos fiscais em eventos_tributarios.

-- Monitor Tributário/Regulatório: vetores fiscais que afetam o complexo soja.
-- Sincronizado a partir de system/tributario_watch.toml (fonte da verdade).
CREATE TABLE IF NOT EXISTS eventos_tributarios (
  id TEXT PRIMARY KEY,            -- id estável do catálogo (ex 'MP-1363-2026')
  titulo TEXT NOT NULL,
  tipo TEXT,                      -- MP | lei | decisao_judicial | regulatorio | programa
  jurisdicao TEXT,                -- BR | EUA | Indonesia | Argentina | global
  status TEXT,                    -- vigente | tramitacao | adiado | monitorando | encerrado
  impacto TEXT,                   -- direto | indireto
  direcao TEXT,                   -- alta | baixa | neutro | misto (efeito líquido no complexo)
  produtos TEXT,                  -- csv: soja,farelo,oleo_soja
  mecanismo TEXT,
  vigencia_ate DATE,
  proximo_marco TEXT,
  proximo_data DATE,
  fonte_url TEXT,
  atualizado_em DATE,
  dados_json TEXT
);

CREATE TABLE IF NOT EXISTS dados_publicos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  fonte TEXT NOT NULL,
  data_referencia DATE NOT NULL,
  data_coleta TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  tipo TEXT NOT NULL,
  commodity TEXT,
  metrica TEXT NOT NULL,
  valor REAL,
  unidade TEXT,
  contexto TEXT,
  raw_json TEXT,
  UNIQUE(fonte, data_referencia, tipo, metrica, commodity)
);

CREATE TABLE IF NOT EXISTS coletas_log (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  fonte TEXT NOT NULL,
  inicio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  fim TIMESTAMP,
  status TEXT,
  registros_fetched INTEGER DEFAULT 0,
  registros_saved INTEGER DEFAULT 0,
  erro TEXT
);

-- Previsoes (forecasts) 7d/30d para acompanhar e calibrar
CREATE TABLE IF NOT EXISTS forecasts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  data_geracao DATE NOT NULL,
  horizonte_dias INTEGER NOT NULL,             -- 7 ou 30
  data_alvo DATE NOT NULL,                     -- data_geracao + horizonte_dias
  commodity TEXT NOT NULL,
  metrica TEXT NOT NULL,                       -- 'fechamento' geralmente
  -- Banda de previsao
  valor_baixo REAL,                            -- limite inferior
  valor_central REAL,                          -- ponto central
  valor_alto REAL,                             -- limite superior
  vies TEXT,                                   -- 'altista' | 'baixista' | 'lateral'
  metodo TEXT NOT NULL,                        -- 'ma20_vol_bands', 'llm_narrativa', etc
  premissas TEXT,                              -- texto/JSON com premissas
  -- Realizado (preenchido pelo backtest quando data_alvo chega)
  valor_realizado REAL,
  hit BOOLEAN,                                 -- realizado dentro da banda?
  hit_direcional BOOLEAN,                      -- direcao acertou (cima/baixo)?
  erro_pct REAL,                               -- (real - central) / central
  data_realizacao DATE,
  notas TEXT,
  UNIQUE(data_geracao, horizonte_dias, commodity, metrica, metodo)
);

CREATE INDEX IF NOT EXISTS idx_forecasts_alvo ON forecasts(data_alvo, commodity);
CREATE INDEX IF NOT EXISTS idx_forecasts_pending ON forecasts(data_alvo) WHERE valor_realizado IS NULL;

-- Precos do mercado fisico BR — input manual via CLI 'main.py fisico add'
-- Praças acompanhadas: rancharia_sp (compra interior), paranagua_pr (exportação).
-- Produtos: soja (sc60kg), farelo (ton), oleo_soja (ton).
-- 1 linha por (data, praca, produto, tipo_posicao). Update via INSERT OR REPLACE.
--
-- NOTA HISTORICA: campos valor_brl_sc/valor_usd_sc mantiveram o nome legado
-- por compatibilidade. Agora guardam "valor na unidade canonica do produto",
-- definida pela coluna unidade_medida:
--   - soja      → sc60kg (saca 60kg)
--   - farelo    → ton    (tonelada metrica)
--   - oleo_soja → ton    (tonelada metrica)
CREATE TABLE IF NOT EXISTS precos_fisicos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  data DATE NOT NULL,
  praca TEXT NOT NULL,                -- 'rancharia_sp' | 'paranagua_pr' | outros
  produto TEXT NOT NULL DEFAULT 'soja', -- 'soja' | 'farelo' | 'oleo_soja'
  tipo_posicao TEXT NOT NULL DEFAULT 'compra',  -- 'compra' | 'venda' | 'indicador'
  valor_brl_sc REAL,                  -- valor BRL na unidade canonica (ver unidade_medida)
  valor_usd_sc REAL,                  -- valor USD na unidade canonica (relevante p/ porto)
  unidade_medida TEXT DEFAULT 'sc60kg', -- 'sc60kg' (soja) | 'ton' (farelo/oleo)
  observacao TEXT,
  criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(data, praca, produto, tipo_posicao)
);

CREATE INDEX IF NOT EXISTS idx_fisicos_praca ON precos_fisicos(praca, data DESC);
CREATE INDEX IF NOT EXISTS idx_fisicos_data ON precos_fisicos(data DESC);

-- Log de auditoria imutável: TODA mudança em precos_fisicos vira linha aqui.
-- Edits sobrescrevem o registro "vivo" mas o valor anterior fica preservado aqui.
-- Nada nesta tabela é apagado em uso normal.
CREATE TABLE IF NOT EXISTS precos_fisicos_historico (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  registro_id INTEGER,                 -- FK fraco para precos_fisicos.id (NULL se deletado)
  data DATE NOT NULL,
  praca TEXT NOT NULL,
  produto TEXT NOT NULL,
  tipo_posicao TEXT NOT NULL,
  valor_brl_sc REAL,
  valor_usd_sc REAL,
  unidade_medida TEXT,
  observacao TEXT,
  acao TEXT NOT NULL,                  -- 'INSERT' | 'UPDATE_OLD' | 'UPDATE_NEW' | 'DELETE'
  capturado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_fisicos_hist_praca ON precos_fisicos_historico(praca, data DESC);
CREATE INDEX IF NOT EXISTS idx_fisicos_hist_registro ON precos_fisicos_historico(registro_id);

-- Curvas de predicao (alem da CBOT real, que fica em dados_publicos):
-- - fonte='stonex': curva indicativa do consultor (input manual via CLI)
-- - fonte='claude': curva heuristica auditavel (gerada por claude_forecast.py)
-- A "curva media" e calculada on-the-fly no HTML, nao armazenada.
CREATE TABLE IF NOT EXISTS curvas_predicao (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  data_geracao DATE NOT NULL,
  fonte TEXT NOT NULL,                 -- 'stonex' | 'claude'
  commodity TEXT NOT NULL,             -- 'soja_cbot' | 'farelo_cbot' | 'oleo_cbot'
  vencimento TEXT NOT NULL,            -- 'N26', 'Q26', 'X26' etc
  valor REAL NOT NULL,
  ajuste_vs_cbot_pct REAL,             -- delta percentual vs CBOT real do mesmo venc
  razoes TEXT,                         -- JSON list das razoes (so Claude usa)
  observacao TEXT,
  fonte_detalhe TEXT,                  -- ex: 'Fabio call 25mai' (StoneX) ou 'heuristica v1' (Claude)
  criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(data_geracao, fonte, commodity, vencimento)
);

CREATE INDEX IF NOT EXISTS idx_curvas_fonte ON curvas_predicao(fonte, commodity, data_geracao DESC);
CREATE INDEX IF NOT EXISTS idx_curvas_venc ON curvas_predicao(commodity, vencimento, data_geracao DESC);

-- Premios de exportacao por porto (extraidos do PDF diario StoneX
-- "Premios nos Portos - Resumido"). Sao os pontos de basis em unidade nativa
-- do mercado (cents/bu pra soja, USD/sht pra farelo, cents/lb pra oleo).
-- Combinados com a curva forward CBOT, dao o preco fisico real esperado por
-- praca/contrato/operacao.
CREATE TABLE IF NOT EXISTS premios_portos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  data DATE NOT NULL,
  produto TEXT NOT NULL,           -- 'soja' | 'farelo' | 'oleo_soja'
  praca TEXT NOT NULL,             -- 'paranagua' | 'golfo_eua' | 'argentina'
  mes_label TEXT NOT NULL,         -- 'jul-2026'
  codigo_stonex TEXT NOT NULL,     -- 'SN6' (soja), 'SMN6' (farelo), 'BON6' (oleo)
  contrato TEXT NOT NULL,          -- 'N26' (normalizado, bate com curvas_predicao/CBOT)
  tipo_op TEXT NOT NULL,           -- 'venda' | 'compra'
  valor REAL NOT NULL,             -- cents/bu, USD/sht, cents/lb conforme produto
  variacao_diaria REAL,            -- variacao vs dia anterior (entre parenteses)
  unidade TEXT NOT NULL,           -- 'cents/bushel' | 'USD/short_ton' | 'cents/lb'
  fonte_pdf TEXT,                  -- path do PDF parseado
  criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(data, produto, praca, codigo_stonex, tipo_op)
);

CREATE INDEX IF NOT EXISTS idx_premios_produto_data ON premios_portos(produto, data DESC);
CREATE INDEX IF NOT EXISTS idx_premios_contrato ON premios_portos(produto, praca, contrato, data DESC);

-- Parametros manuais editaveis pelo usuario (RIN D4, custo industrial,
-- premissas que nao tem coletor automatico mas o consultor manda periodicamente).
CREATE TABLE IF NOT EXISTS params_user (
  chave TEXT PRIMARY KEY,
  valor REAL,
  unidade TEXT,
  descricao TEXT,
  fonte TEXT,                          -- ex: 'StoneX 25mai', 'EPA semanal', 'manual'
  atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Trigger AFTER INSERT: registra a inclusão
CREATE TRIGGER IF NOT EXISTS trg_fisicos_insert
AFTER INSERT ON precos_fisicos
BEGIN
  INSERT INTO precos_fisicos_historico
    (registro_id, data, praca, produto, tipo_posicao, valor_brl_sc, valor_usd_sc, unidade_medida, observacao, acao)
  VALUES
    (NEW.id, NEW.data, NEW.praca, NEW.produto, NEW.tipo_posicao,
     NEW.valor_brl_sc, NEW.valor_usd_sc, NEW.unidade_medida, NEW.observacao, 'INSERT');
END;

-- Trigger AFTER UPDATE: registra valor antigo (UPDATE_OLD) e novo (UPDATE_NEW)
-- Dispara em qualquer campo material (valores, observacao, tipo, produto, unidade).
CREATE TRIGGER IF NOT EXISTS trg_fisicos_update
AFTER UPDATE ON precos_fisicos
WHEN OLD.valor_brl_sc IS NOT NEW.valor_brl_sc
  OR OLD.valor_usd_sc IS NOT NEW.valor_usd_sc
  OR OLD.observacao IS NOT NEW.observacao
  OR OLD.tipo_posicao IS NOT NEW.tipo_posicao
  OR OLD.produto IS NOT NEW.produto
  OR OLD.unidade_medida IS NOT NEW.unidade_medida
BEGIN
  INSERT INTO precos_fisicos_historico
    (registro_id, data, praca, produto, tipo_posicao, valor_brl_sc, valor_usd_sc, unidade_medida, observacao, acao)
  VALUES
    (OLD.id, OLD.data, OLD.praca, OLD.produto, OLD.tipo_posicao,
     OLD.valor_brl_sc, OLD.valor_usd_sc, OLD.unidade_medida, OLD.observacao, 'UPDATE_OLD');
  INSERT INTO precos_fisicos_historico
    (registro_id, data, praca, produto, tipo_posicao, valor_brl_sc, valor_usd_sc, unidade_medida, observacao, acao)
  VALUES
    (NEW.id, NEW.data, NEW.praca, NEW.produto, NEW.tipo_posicao,
     NEW.valor_brl_sc, NEW.valor_usd_sc, NEW.unidade_medida, NEW.observacao, 'UPDATE_NEW');
END;

-- Trigger AFTER DELETE: registra o valor que foi apagado
CREATE TRIGGER IF NOT EXISTS trg_fisicos_delete
AFTER DELETE ON precos_fisicos
BEGIN
  INSERT INTO precos_fisicos_historico
    (registro_id, data, praca, produto, tipo_posicao, valor_brl_sc, valor_usd_sc, unidade_medida, observacao, acao)
  VALUES
    (OLD.id, OLD.data, OLD.praca, OLD.produto, OLD.tipo_posicao,
     OLD.valor_brl_sc, OLD.valor_usd_sc, OLD.unidade_medida, OLD.observacao, 'DELETE');
END;

-- Dedup do "alerta na hora" (alerts_push): cada sinal da fila avisa 1x no Telegram.
CREATE TABLE IF NOT EXISTS alertas_enviados (
  fingerprint TEXT PRIMARY KEY,        -- id estavel do item da fila (queue_emit)
  enviado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_rel_data ON relatorios_stonex(data_publicacao);
CREATE INDEX IF NOT EXISTS idx_pub_data ON dados_publicos(fonte, data_referencia);
CREATE INDEX IF NOT EXISTS idx_pub_commodity ON dados_publicos(commodity, metrica);
CREATE INDEX IF NOT EXISTS idx_log_fonte ON coletas_log(fonte, inicio DESC);
