# Fluxo da camada de julgamento (Fato vs Leitura) — 2026-06-16

> Duas camadas com fronteira dura. O **robô** mede o FATO (determinístico, nuvem).
> O **Claude** produz a LEITURA (julgamento, em sessão paga — sem API). A leitura
> entra no dash como texto rotulado, **nunca** como número/indicador → calibração intacta.

## O fluxo (Fase 1 — dirigido por sessão, custo zero)

```
ROBÔ (GitHub Actions, FATO)                          CLAUDE (sessão, LEITURA)
  coleta → indicadores → dash (Pages)
        │
        ├─ main.py queue  →  FILA de julgamento  ──► você vê "🔔 N pendentes"
        │  (queue_emit.py, determinístico)           (badge no dash + Telegram)
        │                                                     │
        │                                            abre o Claude no repo:
        │                                            "lê a fila de julgamento e trata"
        │                                                     │
        │                                            escreve SÓ insights/*.md (vies:)
        │                                                     │
        └──────────────  git push → Actions → synth ◄─────────┘
                         → Drivers + aba Insights atualizam → Pages (1-2 min)
```

## Peças (Fase 1 — implementadas)
- **`system/queue_emit.py`** — emissor determinístico (sem LLM). `build_queue()` aplica 5 regras
  sobre o que já existe: ratio cruzou zona · nível de tese rompido (alerts_config) · tributário
  ≤7d · release de fundamento inédito (WASDE/NOPA/ABIOVE/COT) ≤3d · revisão D+N de insight ≤7d.
  Cada item = `{id, tipo, severidade, fato, refs, pergunta}`. Conservador de propósito (só sinal alto).
- **`main.py queue`** — imprime a fila no terminal (início da sessão). Não grava no git (efêmera).
- **`prompts/treat_queue.txt`** — a convenção da rotina ("lê a fila e trata"): o que ler, critério,
  contrato de saída (só `insights/*.md`), citar o `id` da fila no corpo, máx 1-3, lente tributária BR.
- **Gatilho no dash + Telegram** — banner "🔔 N leituras pendentes" no topo do Dashboard
  (`_render_fila_banner`) e linha no resumo diário (`daily_summary`). É o que te avisa no celular.

## Separação Fato vs Leitura (já existe, reforçada)
- **FATO** = abas Dashboard/Físico/Análise/Forecasts (100% robô; números, gráficos).
- **LEITURA** = aba 💡 Insights + linhas de Driver vindas de insight (ícone 💡, tag `auto-claude`).
- O Claude **nunca** escreve em `radar.db`, `indicators.py`, `alerts_config.toml` ou `inputs_manuais.toml`.
  A opinião só entra via `insights/*.md` (`vies:` = direção, nunca preço).

## Por que a fila é efêmera (não versionada)
A nuvem é **mão-única** (Actions só publica HTML, nunca faz commit de volta; DB via cache).
E `data/` é gitignored. Então a fila é gerada **localmente** (`main.py queue`) e/ou só renderizada
read-only no dash. O "já tratei" mora no próprio insight (cita o `id` da fila no corpo).

## Decisões em aberto
- **Cadência**: hoje a leitura só existe quando você abre a sessão (latência em dia de evento forte,
  mitigada pelo badge + Telegram). Se incomodar → gatilho pra Fase 2.
- **Calibração das regras**: começamos conservadores (só alta/média). Afrouxar com o uso, igual ao alerts_config.

## Automação ativa (2026-06-16)
- **Alerta na hora** (`alerts_push.py`): o intraday (a cada 30 min no pregão) pinga o Telegram quando
  surge um sinal 🔴 NOVO na fila (dedup por id → avisa 1×, não a cada run). No-op sem Telegram.
- **Auto-fallback de coleta** (`cme_cbot._fetch_chart`): se o Yahoo bloquear o IP da nuvem, tenta a
  mesma URL via ScraperAPI sozinho; só registra erro se os dois falharem.

## Fase 2 (PRONTA p/ ativar — Claude autônomo na nuvem)
**Claude Code Routine**: agente agendado na assinatura Max (sem API), 1×/dia após o robô, lê o briefing,
escreve `insights/*.md` e abre **PR numa branch `claude/`** que você aprova do celular (humano-no-loop).
Cap ~15 runs/dia compartilhado com seu uso interativo. Já no repo: `prompts/routine_julgamento.txt` (o
prompt) e `.github/workflows/guard-leitura.yml` (CI que reprova PR `claude/` que toque algo fora de
`insights/` — cinto de segurança). **Checklist de ativação (quando quiser):**
1. Instalar o **Claude GitHub App** no repo `rpvessoni-sys/Commodities-Radar` + habilitar Claude Code web.
2. Criar a Routine apontando pro repo, prompt = `system/prompts/routine_julgamento.txt`, schedule 1×/dia
   ~1h após o cron daily do robô.
3. Ligar o **briefing-publish** (a Routine roda em clone fresco SEM o DB, então precisa do briefing em git):
   no `radar.yml`, no job `radar`, adicionar `permissions: contents: write` e, no modo daily, escrever
   `briefing/latest.md` (= o `last_dump.md`) e commitar:
   ```yaml
   - name: Publicar briefing (daily)
     if: steps.mode.outputs.mode == 'daily'
     working-directory: ${{ github.workspace }}
     run: |
       cp data/last_dump.md briefing/latest.md 2>/dev/null || mkdir -p briefing && cp data/last_dump.md briefing/latest.md
       git config user.name radar-bot && git config user.email radar-bot@users.noreply.github.com
       git add briefing/latest.md
       git diff --cached --quiet || (git commit -m "briefing $(date -u +%F)" && git push) || true
   ```
4. Manter o PR revisável (default) — você aprova; auto-merge só se confiar.
Só ligar depois da Fase 1 provar valor.

## Limpeza do dump (feito 2026-06-16)
`synth_daily.generate_full_dump()` e `prompts/synthesize_daily.txt` foram limpos: o briefing que o Claude
lê na sessão agora reflete só a base pública (CBOT/BCB/CEPEA/NAG/USDA/COT/clima + notas manuais do
consultor) e aponta pro fluxo atual (fila + treat_queue.txt). Saíram: leitura de relatórios StoneX,
"marcar consultor vs StoneX", pergunta de WhatsApp e comparação com tese_journal (abandonado). Menções
residuais a "StoneX" no dump são só conteúdo factual (nota de contexto do NOPA + as suas notas de call),
não instrução.
