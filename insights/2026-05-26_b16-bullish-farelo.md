---
data: 2026-05-26
titulo: B16 → bullish farelo (comprador)
tags: [biodiesel, farelo, oleo_soja, politica, esmagamento]
fontes:
  - StoneX dashboard Exportação Óleo (visualizado 26mai)
  - Reunião Fabio Cruz (StoneX) 25mai - transcrição em shared/from_consultor/notas_call/
  - ABIOVE consumo diesel B15 público
  - Discussão CNPE cronograma B16
status: ativa
---

## Resumo executivo

- **B15 → B16 = +600 mi L biodiesel/ano no Brasil** (sobre base consumo diesel ~60 bi L)
- **Conversão: +436 mil ton de óleo de soja/ano de demanda interna** (80% do biodiesel BR vem de óleo soja, yield 1.100 L/ton)
- **Impacto = ~32% da exportação BR de óleo soja 2025** (que foi 1,36 mi ton) seria absorvida domesticamente
- **Cadeia de efeitos**: óleo BR sobe → crush margin sobe → esmagadora roda 100% → MAIS farelo no mercado → preço farelo cai
- **Você é comprador de farelo** → cenário BULLISH (preço farelo cai pra zona de compra Far/Soj 77%)
- Dado de exportação 2026 (jan-jun): +12,1% acumulado vs 2025, com pico fev-abr (+59% a +109% mês) — já reflete óleo BR descolado da paridade CBOT (-R$ 2.378/t hoje no sistema)

## Contexto / dados

**Premissas do cálculo B15 → B16:**

| Variável | Valor |
|---|---|
| Consumo diesel A no Brasil/ano | ~60 bilhões L |
| Biodiesel atual (B15) | 9,0 bi L/ano |
| Biodiesel se B16 | 9,6 bi L/ano |
| Δ biodiesel | **+600 mi L/ano** |
| % do biodiesel BR feito de óleo soja | ~80% (resto: sebo, palma, óleos usados) |
| Yield biodiesel | 1.100 L biodiesel/ton óleo |

**Conta:** 600 mi L ÷ 1.100 L/ton = 545k ton óleo total × 80% (share soja) = **+436k ton óleo soja/ano**.

**Cadeia de efeitos esperada:**

```
B16 implementado
  ↓
Demanda óleo soja interna +436k ton/ano (~32% da exportação atual)
  ↓
Óleo BR sobe (fecha gap com paridade CBOT, hoje em -R$ 2.378/t)
  ↓
Crush margin BR sobe (óleo paga mais conta no esmagamento)
  ↓
Esmagadora roda 100% (já em $3,46/bu hoje no CBOT — bem acima do piso $2)
  ↓
Oferta de farelo BR aumenta (subproduto)
  ↓
Preço farelo cai → Far/Soj migra de 82-83% atual pra ~77% (zona verde)
  ↓
🟢 ZONA DE COMPRA pra farelo (paridade CBOT ~R$ 1.700/t, hoje R$ 1.834/t)
```

**Confirmação cruzada com tese Fabio (25mai):**
- Fabio: óleo BR perdeu correlação com mundo, exportador crescente, descolado de CBOT
- Dado: BR exportou +12% acumulado 2026 vs 2025 (jan-jun: 910k ton)
- Fabio mencionou óleo subindo internamente por pressão biodiesel — antecipa B16
- StoneX projeta exportação 2026 ~1,7-1,8 mi ton (recorde), mas B16 pode QUEBRAR essa curva

## Pergunta-tese

O que precisa ser verdadeiro pra essa tese se confirmar:

- **CNPE/CONAMA aprovar cronograma B16** com data efetiva nos próximos 6-12 meses (ou já implementado)
- **Câmbio USD/BRL não disparar pra cima** (>R$ 6) — se disparar, exportação continua viável mesmo com B16, atenuando efeito
- **Safra americana 2026/27 normal** (não quebra) — caso contrário CBOT soja vai pra $13+, puxa farelo pra cima independente do B16
- **Argentina manter ritmo de esmagamento** — se Argentina quebrar de novo, farelo global aperta e o efeito B16 fica neutralizado

## Próximas ações

- [ ] Monitorar agenda **CNPE/MME sobre B16** — buscar próxima reunião e cronograma
- [ ] Acompanhar mensalmente o **dashboard StoneX de exportação óleo** — sinal antecipado: se a exportação MAI/JUN cair forte, indica óleo sendo absorvido internamente
- [ ] Quando confirmação B16 sair: **avaliar travamento de farelo** nos níveis ATUAIS de compra (curva pode subir um pouco antes de cair pelo crush sazonal)
- [ ] Conversar com Fabio na próxima call: pedir **série histórica de FAR/SOJ ratio quando B mudou** (B11→B12→B14→B15) — quanto cada ponto mexeu o ratio?
- [ ] Implementar no sistema: **coletor automático de exportação óleo (ABIOVE/ANEC)** + **card "Sensibilidade B16" na aba Análise Quantitativa** com cálculo dinâmico

## Revisão programada

- **D+90: 2026-08-24** — revisar status:
  - CNPE divulgou cronograma B16? Data efetiva?
  - Exportação BR de óleo em jul-ago cresceu ou começou a cair?
  - Far/Soj ratio mexeu de 82-83% pra qual nível?
- **D+180: 2026-11-22** — fechar ciclo:
  - Tese acertou (farelo caiu pra zona verde)?
  - Errou (farelo subiu ou ficou estável)?
  - Marcar `status: revisada` ou `arquivada` no frontmatter

## Notas adicionais

**Por que `comprador de farelo` é a perspectiva relevante:**
- Usuário não opera direto (operações via consultor)
- Dependência principal é compra de farelo de soja pra ração (B2B)
- Preço farelo cai = margem do negócio sobe = tese boa
- Se fosse vendedor (esmagadora), tese seria invertida — farelo caindo = ruim
