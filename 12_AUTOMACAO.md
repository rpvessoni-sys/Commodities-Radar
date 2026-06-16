# Automacao — Task Scheduler + File Watcher

> Implementado 2026-05-21. Cobre 90% da rotina diaria sem comando manual.

---

## Visao geral

```
                     ┌─────────────────────────────┐
                     │ Voce baixa relatorio StoneX │
                     │ (bookmarklet ou consultor)  │
                     └────────────┬────────────────┘
                                  │
                                  ▼
                     ┌─────────────────────────────┐
                     │   inbox/  (arquivo aparece)  │
                     └────────────┬────────────────┘
                                  │
                  ┌───────────────┼───────────────┐
                  │                                │
                  ▼                                ▼
        ┌──────────────────┐         ┌──────────────────────┐
        │ File Watcher     │         │ Task Scheduler        │
        │ (sempre rodando) │         │ (cron diario)         │
        │                  │         │                       │
        │ detecta arquivo  │         │  07:00 — run completo │
        │ → dispara ingest │         │  19:00 — coletor CME  │
        │                  │         │  sex 18:00 — CFTC COT │
        └────────┬─────────┘         └──────────┬───────────┘
                 │                                │
                 ▼                                ▼
                 ┌─────────────────────────────────┐
                 │  python main.py ingest / run    │
                 │  → SQLite atualizado            │
                 │  → reports/ + dump + alerts     │
                 └─────────────────────────────────┘
```

---

## 1. Task Scheduler (cron diario)

### Setup (1 vez)

```powershell
cd commodities-radar/system
.\setup_scheduler.ps1
```

Cria 3 tasks:
| Task | Quando | O que faz |
|---|---|---|
| `CommoditiesRadar_Morning` | Diario 07:00 | `main.py run` (pipeline completo) |
| `CommoditiesRadar_Evening` | Diario 19:00 | `main.py public --source cme_cbot` (pos-fechamento CBOT) |
| `CommoditiesRadar_Friday` | Sex 18:00 | `main.py public --source cftc_cot` (release ~15:30 NY) |

### Comandos uteis

```powershell
.\setup_scheduler.ps1 -List     # listar tasks criadas + ultima execucao
.\setup_scheduler.ps1 -Remove   # remover tasks
.\setup_scheduler.ps1           # criar/atualizar (idempotente)
```

### Logs

Em `commodities-radar/data/logs/radar_*.log`.

Cada execucao gera 1 arquivo com timestamp. Limpe periodicamente (>30 dias) ou implemente rotacao.

---

## 2. File Watcher (auto-ingest)

### Modo foreground (terminal aberto)

```powershell
cd commodities-radar/system
.\daemon_watcher.ps1
```

Observa `inbox/` e `shared/from_consultor/inbox/`. Quando arquivo aparece:
1. Detecta evento (created/modified)
2. Espera 5s para arquivo estabilizar
3. Verifica tamanho 2x para garantir que escrita terminou
4. Dispara `python main.py ingest`

CTRL+C para parar.

### Modo background (janela escondida)

```powershell
.\daemon_watcher.ps1 -Background
```

Inicia processo PowerShell escondido. Continua mesmo se voce fechar o terminal.

Para parar:
```powershell
Get-Process python | Where-Object { $_.Path -like '*commodities-radar*' } | Stop-Process
```

### Modo "rodar uma vez"

```powershell
.\daemon_watcher.ps1 -Once
```

Processa o que ja esta em `inbox/` e sai. Util para testes.

### Watcher na inicializacao do Windows

Opcao A — Task Scheduler:
1. Abrir Task Scheduler
2. Create Basic Task → "CommoditiesRadar_Watcher"
3. Trigger: When the computer starts
4. Action: Start a program → `powershell.exe`
5. Arguments: `-WindowStyle Hidden -ExecutionPolicy Bypass -File "C:\caminho\system\daemon_watcher.ps1"`

Opcao B — pasta Startup:
1. Win+R → `shell:startup`
2. Criar atalho para `daemon_watcher.ps1` com `-Background`

---

## 3. Fluxo na pratica

### Cenario A — voce baixa relatorio agora
1. Bookmarklet baixa HTML para Downloads
2. Voce move para `inbox/`
3. **Watcher detecta em ~5s** → ingest automatico
4. DB atualizado sem voce digitar nada
5. (Opcional) abre Claude Code e pede sintese

### Cenario B — voce dorme, sistema acorda 7h
1. 07:00 — task `Morning` dispara `main.py run`
2. Ingest processa o que tiver na inbox
3. Synth gera relatorio estruturado
4. Dump consolida ultimos 14 dias
5. Check alerta atrasos
6. Public coleta CME + BCB + CFTC + Inmet
7. Voce levanta, abre Claude Code, pede sintese — tudo ja preparado

### Cenario C — sexta a noite, CFTC sai
1. 18:00 sex — task `Friday` dispara coletor CFTC
2. Posicao fundos atualizada no DB
3. Proxima `Morning` (segunda 7h) incorpora COT na sintese

---

## 4. Troubleshooting

| Problema | Solucao |
|---|---|
| Task nao executa | Abrir Task Scheduler GUI, ver "Last Run Result". Verificar se PowerShell ExecutionPolicy permite scripts |
| Watcher consome muita CPU | Aumentar `time.sleep(2)` em daemon_watcher.py para `5` ou mais |
| Logs ficam pesados | Limpar `data/logs/` periodicamente. Considerar log rotation |
| Watcher nao detecta arquivo | Verificar se nome tem extensao suportada: .html, .htm, .pdf, .txt |
| Conflito de execucao | Watcher e Task Scheduler podem disparar ingest simultaneo. SQLite gerencia lock — em testes funcionou OK |

---

## 5. O que ainda e manual

- **Baixar relatorios StoneX** (bookmarklet) — manual por design (ToS)
- **Pedir sintese ao Claude Code** — voce abre, pede
- **Atualizar teses pessoais** — manual no markdown
- **Confirmar cadencias do catalog** — depende de voce

Tudo o resto e automatico.
