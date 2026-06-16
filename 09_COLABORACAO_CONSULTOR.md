# Colaboracao com Consultor StoneX

> Arquitetura de pasta compartilhada via OneDrive.
> Voce (usuario) mantem TUDO do sistema na maquina + Claude Max.
> Consultor enxerga apenas a pasta `shared/` com material curado e pode contribuir com inputs.

---

## Principios

1. **Sistema fica privado** — `commodities-radar/system/`, `data/`, `inbox/`, `00-08 docs` ficam SOMENTE com voce
2. **Claude Max e seu** — consultor NUNCA acessa o assistente, so arquivos texto/PDF
3. **Bidirecional** — consultor pode mandar material que entra no pipeline (inbox dedicado pra ele)
4. **Sintese e sua** — voce gera, consultor consome (e comenta)
5. **Sem custo pro consultor** — ele so usa explorador de arquivo + Word/PDF reader

---

## Estrutura de pastas

```
commodities-radar/                       ← privado (voce)
├── 00-09 docs                           privado
├── system/                              privado (codigo)
├── data/                                privado (DB, raw HTML)
├── inbox/                               privado (sua ingestao StoneX)
├── reports/                             privado (geração interna)
├── tese_journal/                        privado (suas teses)
│
└── shared/                              ← COMPARTILHADO via OneDrive
    ├── README.md                        instrucoes para o consultor
    │
    ├── from_consultor/                  consultor LARGA material aqui
    │   ├── inbox/                       relatorios extras (HTML/PDF) que ele queira voce processar
    │   ├── insights/                    insights/anotacoes em markdown
    │   └── notas_call/                  anotacoes das calls semanais
    │
    ├── to_consultor/                    sistema entrega material aqui (automatico)
    │   ├── snapshots_diarios/           sintese diaria do dia
    │   ├── teses_ativas/                copia das teses em andamento
    │   ├── alerts/                      relatorios em atraso (alerts.json + .md)
    │   └── perguntas_pendentes/         coisas pra abordar na proxima call
    │
    └── colaboracao/                     markdown editado pelos dois lados
        ├── perguntas_para_call.md
        ├── topicos_em_discussao.md
        └── feedback_consultor.md
```

---

## Permissionamento OneDrive

1. No File Explorer, botao direito em `commodities-radar/shared/`
2. "Share" / "Compartilhar" → "OneDrive"
3. Adicionar email do consultor com permissao **Pode editar**
4. Enviar link

**O que ele ve:**
- ✅ Pasta `shared/` completa com sub-pastas
- ❌ Nao ve `system/`, `data/`, `inbox/`, etc (acima do nivel compartilhado)
- ❌ Nao tem acesso ao Claude Max nem ao codigo

---

## Fluxo de uso

### Voce (rotina diaria)

```
1. Bookmarklet baixa relatorio StoneX
2. Joga em inbox/ (privado)
3. python main.py run
   → ingest do inbox/ + from_consultor/inbox/
   → synth + dump
   → escreve em shared/to_consultor/snapshots_diarios/
   → check de cadencia
4. Abre Claude Code, pede sintese narrativa do dump
5. Salva sintese em shared/to_consultor/snapshots_diarios/
6. (semanal) atualiza teses, copia versao publica para shared/to_consultor/teses_ativas/
```

### Consultor (quando quiser contribuir)

```
1. Recebe relatorio StoneX especial → larga em shared/from_consultor/inbox/
2. Quer compartilhar insight → cria .md em shared/from_consultor/insights/
3. Pos-call semanal → registra notas em shared/from_consultor/notas_call/YYYY-MM-DD_call.md
```

### Consultor (consumo)

```
1. Abre shared/to_consultor/snapshots_diarios/ → le sintese do dia
2. Comenta em shared/colaboracao/feedback_consultor.md
3. Sugere topicos pra call em shared/colaboracao/perguntas_para_call.md
```

---

## Que arquivos entram no contexto da sintese

O sistema processa **tanto** o inbox privado quanto `shared/from_consultor/inbox/`. 

Para os outros arquivos do consultor (insights, notas_call):
- Sao **lidos como contexto** no `dump`
- Voce pode pedir ao Claude: "considere tambem os insights do consultor em shared/from_consultor/insights/"

---

## Boas praticas

### Para voce
- **Nunca exponha** sua API key, dados internos da empresa, ou material da memoria Claude no `shared/`
- **Versione manualmente** suas teses antes de copiar pro shared — assim mantem o original privado
- **Edite localmente** primeiro, depois copie pro shared
- Considere git pra controlar versoes do `shared/` localmente (sem push)

### Para o consultor (incluir no README dele)
- **Sempre datar arquivos**: `2026-05-21_insight_oleo_brl.md`
- **Markdown ou PDF**, evitar Word doc (formatacao quebra)
- **Avise no Whatsapp** quando jogar algo no inbox dele
- **Nao apague** arquivos da pasta `to_consultor/` (so leitura conceitual, mesmo que tecnicamente possa)

---

## Riscos e mitigacoes

| Risco | Mitigacao |
|---|---|
| Consultor apaga arquivo importante | OneDrive guarda versoes; restaurar facil |
| Conflito de edicao em colaboracao/ | OneDrive resolve com "Copy" automatica; comunicar via Whatsapp |
| Consultor vaza material seu | Confiar no profissional; ToS StoneX ja impede dele redistribuir relatorios |
| Pasta cresce demais | Limpar `snapshots_diarios/` mais antigos que 90 dias |
| Sincronizacao OneDrive lenta | Marcar pasta como "Always keep on this device" |

---

## Quando ativar

**Hoje**: estrutura criada vazia, sistema integrado com `shared/from_consultor/inbox/`.
**Amanha** (apos preencher catalog): voce testa fluxo com 1 relatorio.
**Quando der**: clica direito em `shared/` → compartilha com consultor.

Nao precisa ativar hoje. Sistema funciona com a pasta vazia.
