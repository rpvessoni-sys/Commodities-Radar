# Insights de estudo — Commodities Radar

Pasta com 1 arquivo `.md` por **insight pessoal** decorrente de estudo/análise/conversa com consultor. Aparece automaticamente na aba 💡 Insights do HTML diário, ordenado por data (mais recente primeiro).

## Diferença vs "Insights" do Dashboard

| Onde | O que é | Origem |
|---|---|---|
| **Dashboard → Insights críticos** | bullets auto-gerados por heurística sobre dados do DB | Sistema |
| **Aba Insights** | resumos executivos de estudos/análises pessoais com lifecycle (data, fonte, revisão) | Usuário |

## Como criar um novo

```powershell
python main.py insight new "B16 bullish farelo"
# cria insights/2026-05-26_b16-bullish-farelo.md com template
```

Ou crie o arquivo `.md` direto seguindo a convenção abaixo.

## Convenção de nome do arquivo

`YYYY-MM-DD_<slug-kebab-case>.md`

Exemplos:
- `2026-05-26_b16-bullish-farelo.md`
- `2026-06-01_china-acordo-soja-trump.md`
- `2026-06-15_quebra-safra-argentina.md`

## Estrutura do arquivo (frontmatter + markdown)

```markdown
---
data: 2026-05-26
titulo: B16 → bullish farelo (comprador)
tags: [biodiesel, farelo, oleo_soja, politica]
fontes:
  - StoneX dashboard Exportação Óleo (25mai)
  - Reunião Fabio Cruz (StoneX) 25mai
  - ABIOVE consumo diesel B15
status: ativa    # ativa | revisada | arquivada
---

## Resumo executivo

- Ponto 1 em uma linha curta
- Ponto 2
- Ponto 3
- Conclusão / ação sugerida

## Contexto / dados

(texto livre, opcional — destrincha cálculos, números, racional)

## Pergunta-tese

O que precisa ser verdadeiro pra essa tese se confirmar.

## Próximas ações

- [ ] Ação 1 com data
- [ ] Ação 2

## Revisão programada

- **D+90**: 2026-08-26 — revisar se mercado moveu na direção prevista
- **D+180**: 2026-11-26 — fechar o ciclo, marcar status (acerto/erro/parcial)
```

## Status do insight (frontmatter)

- `ativa` — tese em curso, ainda válida
- `revisada` — passou pela data D+90, mantida
- `arquivada` — tese fechou (acerto, erro ou desatualizada)

Sistema mostra todos por padrão. Filtros por tag/status virão se a pasta crescer muito.

## Por que `.md` em vez de banco

- Editável em qualquer editor (VS Code, Notepad, etc)
- Versionável via OneDrive
- Compartilhável com consultor (pasta `shared/` pode receber subset)
- Diff visual quando você revisa
- Sem dependência de DB pra esse fluxo simples
