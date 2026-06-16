# Caminho de Ingestao dos Relatorios StoneX

> Email parsing INVALIDADO (2026-05-20) — StoneX so envia notificacao, nao o conteudo.
> Este documento mapeia as alternativas viaveis e recomendacao por nivel de ergonomia.

---

## Realidade descoberta

StoneX entrega:
- ❌ Conteudo do relatorio **NAO vem por email**
- ✅ Notificacao por email avisando "relatorio X publicado"
- ✅ Conteudo so acessivel via portal `stonex.digital` (login + HTML)
- ❌ Sem PDF para download direto
- ❌ Sem API publica conhecida

## Opcoes viaveis

### Opcao 1 — Drop manual SIMPLES
**Fluxo:**
1. Receber notificacao
2. Abrir relatorio no portal
3. Ctrl+A → Ctrl+C
4. Criar `.txt` em `commodities-radar/inbox/` e colar
5. Rodar `python main.py ingest`

**Tempo:** ~90s por relatorio
**Pros:** zero setup
**Cons:** repetitivo

### Opcao 2 — Drop manual via BOOKMARKLET (RECOMENDADO INICIAL) ★
**Setup uma vez:**
1. Arrastar bookmarklet (em `system/bookmarklet.html`) para a barra de favoritos
2. Configurar Chrome para baixar em `commodities-radar/inbox/` (ou aceitar Downloads)

**Fluxo:**
1. Receber notificacao
2. Abrir relatorio no portal
3. Clicar no bookmarklet
4. HTML do relatorio baixa automaticamente com nome padronizado
5. Mover para `inbox/` se nao baixou ali direto
6. Sistema (watcher ou comando `ingest`) processa

**Tempo:** ~15-30s por relatorio
**Pros:** simples, sem dependencias, sem ToS risk
**Cons:** ainda manual, depende dele acessar o portal

### Opcao 3 — Claude in Chrome MCP (NIVEL 2, sob demanda)
**Setup uma vez:**
1. Instalar extensao Claude for Chrome
2. Logar no StoneX no Chrome
3. Manter aba aberta

**Fluxo:**
1. Receber notificacao
2. Abrir relatorio no portal (Chrome)
3. Invocar Claude Code: "extrai o conteudo do StoneX que esta aberto"
4. Sistema usa MCP `Claude_in_Chrome` para ler a pagina ativa
5. Salva em inbox/ e processa

**Tempo:** ~20s (mas exige assistente rodando)
**Pros:** ergonomico, conversacional
**Cons:** requer Chrome + extensao + invocacao

### Opcao 4 — Notification-aware (futuro, opcional)
**Fluxo:**
1. Sistema le emails de notificacao StoneX via IMAP
2. Detecta novo relatorio liberado
3. Envia alerta para Telegram/email do usuario
4. Usuario clica no bookmarklet
5. Sistema processa

**Pros:** alerta automatico em qualquer device
**Cons:** apenas notifica, nao ingere

---

## Recomendacao

**Fase 1 (agora):** Opcao 2 (bookmarklet) + watcher na inbox  
**Fase 2 (mes 2):** Opcao 4 (alerta via IMAP de notificacao)  
**Fase 3 (opcional):** Opcao 3 (Claude in Chrome) para usuario "Power"

---

## Por que NAO scraping autenticado (decisao firme)

Mesmo se for tecnicamente possivel (Playwright com sessao salva):
- Conta StoneX e **corporativa** — empresa do usuario paga
- ToS provavelmente proibe automacao
- Banimento = constrangimento profissional + impacto na empresa
- Layout muda → manutencao alta
- Risco > beneficio

Se a empresa do usuario explicitamente autorizar (escrito), revisita. Por enquanto: nao.

---

## Frequencia esperada (a definir)

A definir com usuario:
- Quantos relatorios distintos ele recebe por semana?
- Distribuicao de dias (todos seg? espalhado?)

Pra estimar:
- Se < 5/semana: drop manual e plenamente ok
- Se 5-15/semana: bookmarklet vira essencial
- Se > 15/semana: avaliar Claude in Chrome ou negociar API com StoneX
