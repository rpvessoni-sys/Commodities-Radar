---
data: 2026-06-18
titulo: Óleo CBOT quebra suporte 72.00 (-2.59%) — backwardation confirma bear, spec position vulnerável
tags: [oleo_soja, crush, cot, biodiesel, cambio, auto-claude]
fontes:
  - Sistema commodities-radar — CBOT/indicators/COT 18/jun/2026
  - BCB PTAX USD/BRL 18/jun/2026 (sgs=1)
  - CFTC COT óleo CBOT 09/jun/2026
  - Notícias Agrícolas (NAG) — físico soja Paranaguá 18/jun/2026
status: ativa
vies: [bear-oleo_soja]
---

## Resumo executivo

- **Óleo CBOT N26 fechou 69.69 cts/lb (−2.59% no dia), rompendo o suporte técnico de 72.00** (trata fila `alerta-quebra_suporte-oleo_cbot-2026-06-18` e `alerta-movimento_forte-oleo_cbot-2026-06-18`). Mínima do dia: 68.00 cts/lb.
- **Curva em backwardation acentuada**: N26=69.69 / Q26=68.43 / U26=67.38 / Z26=65.80 / F27=65.51 cts/lb — mercado precifica oferta crescente de óleo pelo menos até jan/27. Não é ruído técnico, é estrutura de curva.
- **Oil share recuou de 55.2% (15/jun) para 53.6% (18/jun) em três pregões**: óleo perdeu prematura no crush. Oil/meal spread comprimiu de 1.54 → 1.04 USD/bu no mesmo período.
- **Posição especulativa net long em óleo CBOT: 128.746 contratos (COT 09/jun)**: posição carregada, longa, sem comprador novo à vista. Cada queda abaixo de suporte aumenta risco de liquidação em cascata.
- **Mitigante cambial** (trata fila `alerta-movimento_forte-usd_brl_ptax-2026-06-18`): USD/BRL PTAX subiu +1.92% (5.0641 → 5.1613) em 18/jun. A paridade soja BR chegou a 127.75 BRL/sc — com físico Paranaguá a 133.39 BRL/sc (NAG 18/jun), a janela de exportação de soja em BRL permanece aberta. O câmbio suaviza a queda do CBOT no físico BR, mas não reverte o sinal bear no óleo CBOT.
- **Leitura operacional**: bear-oleo_soja. A combinação quebra de suporte + backwardation + spec position longa cria assimetria de queda. Para o crush, a margem recuou a 3.07 USD/bu (18/jun) — ainda lucrativa, mas o óleo já não "paga" o crush com a folga de antes. Pressão de farelo continua máxima (índice 5/5).

## Contexto / dados

| Métrica | 15/jun | 17/jun | 18/jun | Leitura |
|---|---|---|---|---|
| Óleo CBOT front (cts/lb) | 74.37 | 71.54 | 69.69 | −2.59% no dia, −6.3% em 3 dias |
| Oil share crush (%) | 55.18 | 53.99 | 53.63 | perda de prematura acelerada |
| Oil/meal spread (USD/bu) | 1.54 | 1.16 | 1.04 | compressão acentuada |
| Crush margin (USD/bu) | 3.63 | 3.26 | 3.07 | ainda positiva, ritmo de queda |
| Biodiesel margin US (USD/gal) | 0.054 | 0.194 | 0.266 | melhorou — HO cedeu menos |
| USD/BRL PTAX | 5.043 | 5.064 | 5.161 | +1.92% em 18/jun |
| Soja paridade BR (BRL/sc) | 124.44 | 126.38 | 127.75 | câmbio compensa queda CBOT |

Curva óleo CBOT em 18/jun (sistema commodities-radar): N26=69.69 / Q26=68.43 / U26=67.38 / V26=66.40 / Z26=65.80 / F27=65.51 cts/lb.

COT CFTC óleo (09/jun): managed money long 157.169 / short 28.423 / **net +128.746 contratos**. Open interest = 690.051. Posição especulativa acima do percentil histórico recente — liquidação retroalimenta a queda.

Biodiesel US: margem melhorou porque HO (3.13 USD/gal em 18/jun vs 3.19 em 17/jun) cedeu menos do que o óleo de soja. RIN 2.11 USD. Contexto: NOAA/CPC mantém El Niño Advisory (desde ≥15/jun), que pode reduzir produção de palma na Malásia — MPOB não extraível via scraper no momento (parser sem resultado).

Lente tributária BR: óleo degomado dentro da cadeia biodiesel no Brasil tem debate do B16 (sem data CNPE — ver [[2026-05-26_subvencao-fossil-aperta-biodiesel]]). Enquanto B16 não tem data, o gatilho altista de demanda interna de óleo BR não se materializa. O câmbio fraco (5.16) eleva custo de importação de palma, mas MPOB sem dados disponíveis impede confirmar spread.

Cruzamento com [[2026-06-05_varredura-completa-complexo-soja]] (tese do complexo partido — óleo x farelo divergindo). O índice suporte_oleo ainda marca 80.0 (4/5 condições) apesar do preço spot ter quebrado o suporte — sinal de que as condições estruturais de demanda de óleo seguem, mas o preço está descolado para baixo.

## Pergunta-tese

O que precisa ser verdadeiro pra essa tese (bear-oleo_soja) se confirmar:

- Backwardation na curva óleo se aprofunda ou mantém (oferta crescente sem absorção nova)
- Biodiesel demand US não absorve excesso (RIN estável ou abaixo, heating oil sem spike)
- Especuladores continuam liquidando (COT net long reduz na próxima leitura CFTC)
- MPOB não publica estoque baixo de palma (competidor direto do óleo de soja)

## Gatilhos que invalidam

- B16 ganha data de vigência: demanda de óleo degomado BR dispara → inverteria para bull-oleo_soja
- MPOB divulga estoque abaixo do esperado: palma sobe, arrasta óleo soja junto
- Secas no Center-West BR 26/27 (El Niño Advisory em desenvolvimento — NOAA 19/jun): reduz esmagamento e oferta de óleo
- Heating oil (HO) spike geopolítico: biodiesel margin melhora, puxa demanda de óleo soja US

## Revisão programada

- **D+7**: 2026-06-25 — oil/meal spread voltou a abrir? COT mostra liquidação de longs?
- **D+30**: 2026-07-18 — backwardation se aprofundou? Oil share recuperou ou caiu mais?
- **D+90**: 2026-09-16
