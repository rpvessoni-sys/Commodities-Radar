# Revisão "lente de trader" — 2026-06-11

> Revisão multi-agente (5 lentes: timing de compra, risco/cenários, clareza,
> dados de mesa, processo/disciplina) + poda crítica. 35 propostas → 18 aprovadas
> em 3 ondas. Princípio: o sistema deve responder **"compro hoje? quanto? por quê?"**
> — não só descrever o mercado.

## Veredito em uma frase

O radar virou um **analista competente** (lê preço, estrutura fiscal, drivers,
honestidade de calibração), mas a **mesa de compra não existe**: o sistema não
sabe o consumo do usuário, não registra compras com volume, não tem plano de
tranches como artefato, e nenhuma tela responde "o que eu faço hoje".

## 🐛 Bugs encontrados pela revisão (consertar antes de qualquer feature)

1. **"Tese ativa" do HTML está errada há 3 semanas** — `_get_tese_ativa()` lê o
   tese_journal (abandonado, último arquivo 22/mai) em vez do insight vivo de
   11/jun. Informação errada na cara do decisor.
2. **Snapshot do consultor entrega stub vazio** — a cópia pra `shared/` (ligada
   hoje) copia um relatório que só consulta a tabela `relatorios_stonex`
   (encerrada): o arquivo diz "Sem relatorios novos". Reescrever
   `generate_structured_report()` pra montar o snapshot do DB público.
3. **KPI do crush com nível hard-coded** — "⚠ Quebrou resistência $2,00" fixo em
   `_render_kpis` (a 3ª rodada corrigiu o resumo executivo mas esqueceu o KPI);
   reconciliar também o `alerts_technical.json` antigo com a config viva antes
   de renderizar.

## Onda P0 — fazer o sistema DECIDIR (1ª prioridade)

| # | Entrega | O que muda | Dados |
|---|---|---|---|
| P0.1 | **Exposição do comprador**: `consumo_farelo_ton_mes` (param) + coluna `volume_ton`/tipo `executada` no físico + card "Posição & Cobertura" (cobertura em semanas: 🔴<4 🟡4-8 🟢>8) | Todo sinal ganha tamanho: "exposto 3 semanas" muda a urgência de qualquer queda | 3 números que o usuário sabe de cabeça |
| P0.2 | **Plano de tranches como artefato**: `plano_compra.toml` (volume alvo, tranches com gatilho e %, ex: 25% se ratio<82, 25% se <80, 30% se CBOT<293, 20% pós-call) + card com progresso e distância do próximo gatilho + histórico INSERT-only (anti-FOMO leve) | "Compra em tranches" deixa de ser frase e vira régua auditável; D+90 do insight vira respondível | plano decidido 1x com o consultor + indicadores já no DB |
| P0.3 | **Card "Ação do dia"** no topo do Dashboard (COMPRAR TRANCHE / ARMAR / ESPERAR, regra determinística sobre ratio+níveis+plano, 1 frase de justificativa + 1 de invalidação) + **sinal composto 0-4 gravado no DB** (ratio, percentil 52s, prêmio export ≤0, momentum) + **resumo executivo em 3 frases rotuladas** (Mercado / Pro comprador / Ação) | A primeira tela responde "o que eu faço?" em 10 segundos; o sinal fica auditável ("estava em 3 quando não comprei") | 100% DB existente |
| P0.4 | Bugs 1-3 acima | Confiança no produto | — |

## Onda P1 — contexto que muda o tamanho do cheque

| # | Entrega | Por quê | Dados |
|---|---|---|---|
| P1.1 | **Backfill 5 anos CBOT** (Yahoo `range=5y`, mesma API, idempotente) → percentil 52s nos KPIs ("303,60 = p4"), mín/máx 52s CALCULADO (mata o "293" de comentário), vol realizada como regime no forecast | "Raro ou normal?" é o input nº1 de tamanho de tranche | Yahoo já usado |
| P1.2 | **Spreads de calendário** no card curva (N26−Z26 etc., regra: inversão = antecipar / carry = sem pressa) + gravado como indicador | Estrutura é o termômetro de escassez; hoje a curva flat do farelo vs backwardation do óleo está invisível como sinal | 6 vencimentos JÁ no DB |
| P1.3 | **Card COT farelo/óleo** (managed money net + percentil histórico via ZIPs anuais públicos da CFTC + open interest) | Fundos em extremo + preço caindo = risco de cascata → paciência; fundos vendidos ao máximo = chão próximo → acelerar | 22 sem. no DB + backfill grátis |
| P1.4 | **Histórico do prêmio export PGUA** (14d colapsável) + alerta de virada (prêmio>4 USD/sht = export voltou a disputar = chão no interno) + driver automático | É a evidência central da tese "farelo despejado" — a virada é gatilho de aceleração | nag_fisico já coleta |
| P1.5 | **Carrego**: spread forward anualizado vs custo de carregar físico (params: custo capital ~CDI + armazenagem) → "mercado paga/não paga esperar" em 1 linha | A decisão central do tranching hoje é feita no olho | curva no DB + 2 params |
| P1.6 | **Stress cambial 3×3** (farelo 290/atual/325 × PTAX 4,90/atual/5,30 em R$/t, breakeven FX explícito) + **matriz crush com linha em R$/t e Δ orçamento/mês** (consumo × Δpreço) | Farelo caindo + dólar subindo pode anular a tese em R$ — hoje o sistema ficaria mudo; matriz fala a língua da esmagadora, não do comprador | CBOT+PTAX+níveis, tudo no DB |
| P1.7 | **Fila de revisões D+N** (parsear "Revisão programada" dos insights; cobrar no Dashboard e no `status`) + **pauta da call gerada por dados** (proposta de tranche, divergências curva StoneX vs CBOT >3%, marcos fiscais ≤14d, revisões vencendo → `shared/to_consultor/pauta_call.md`) | D+7 do insight do ratio vence 18/jun e nada avisa; a call é o canal de execução e a pauta hoje morre no HANDOFF | tudo no DB/arquivos |
| P1.8 | **Semântica de cor única** (verde = a favor do comprador; âmbar = dado velho; vermelho = contra) + KPIs com variação D-1 + ratio Far/Soj no grid do Dashboard | 3 inversões de cor achadas na aba Físico; "compra abaixo do indicador CEPEA" está VERMELHA hoje | só CSS/lógica |

## Onda P2 — refinamento (depois que P0-P1 assentarem)

- **Sazonalidade 10 anos** (farelo + ratio, mensal; com aviso de viés de rolagem do contrato contínuo)
- **Oil share com percentil histórico** + gatilho de rotação (queda >3pp vs MA20 = janela fechando) — depende do backfill P1.1
- **Cenários nomeados quantificados** (`cenarios_watch.toml`: China destrava / B16 sai / crush <2,50 → Δ R$/t e Δ orçamento; choques curados em sessão com analogia histórica verificável)
- **Scorecard das 4 curvas** (erro médio StoneX vs Claude vs CBOT a 30d — vira pergunta de pauta)
- **Relatório de captura** (preço médio das tranches vs 3 benchmarks: média do período / dia-1 / mínima)
- **Aposentar tese_journal** (migrar 2 arquivos pra insights/ como arquivados; religar backtest.py lendo `vies:` dos insights; incluir na run de sexta)
- **Banner "automação parada"** no topo se coletas_log não registrar execução nas janelas do scheduler

## ❌ Rejeitados na poda crítica (e por quê)

- **Frete SIFRECA/ESALQ-LOG** (arbitragem MT+frete vs PR): valor real mas scraping mensal de tabela instável e rota exata incerta — entrar via `param set frete_mt_pr` manual se a necessidade se confirmar na prática.
- **Banner anti-FOMO com motivo obrigatório**: teatro de governança num sistema de 1 pessoa (ele edita o TOML direto). Fica só o histórico imutável + "registrado há N dias".
- **Range orçamentário 30d via banda do forecast**: a banda tem 46% de cobertura observada — construir orçamento sobre ela institucionalizaria um número fraco. O stress 3×3 (P1.6) + drawup empírico cobrem melhor.
- Tudo que envolvesse: nova aba, servidor/app, API paga, ou qualquer extração StoneX.

## Sequência sugerida de implementação

1. P0.4 (bugs — 1 sessão curta)
2. P0.1 + P0.2 (fundação de exposição + plano — pedem 3-4 inputs seus e 1 conversa com o consultor pra definir a régua de tranches)
3. P0.3 (Ação do dia — só código)
4. P1.1 + P1.2 (backfill + spreads — destravam metade do P1)
5. Resto do P1 por conveniência; P2 quando P0-P1 estiverem rodando há 2+ semanas
