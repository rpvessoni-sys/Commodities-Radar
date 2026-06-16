---
data: 2026-05-26
titulo: Esmagamento BR em recorde reforça tese bullish farelo
tags: [esmagamento, farelo, oleo_soja, abiove, b16, brasil]
fontes:
  - StoneX dashboard Esmagamento e Produção Óleo de Soja (visualizado 26mai)
  - ABIOVE histórico série esmagamento BR
  - Insight 2026-05-26_b16-bullish-farelo (referência cruzada)
status: ativa
---

## Resumo executivo

- **Mar/2026 = 5.575 mil ton esmagadas no Brasil** — RECORDE histórico (+5,9% vs mar/25, +14,6% vs mar/24)
- **Acumulado temporada 25/26 = 59,6 mi ton vs 55,7 mi ton em 24/25 → +7,1% no ano** (+3,96 mi ton a mais)
- **Geração extra de subprodutos em 25/26**: +713 mil ton de óleo + **3.049 mil ton de farelo** (yields 18%/77% da soja)
- **Destino do óleo extra**: exportação cresceu só ~150 mil ton (12% de 1,36 mi ton base). **As outras 560 mil ton ficaram no Brasil — B15 absorveu via biodiesel** (não foi estoque, ABIOVE estoques estáveis)
- **Farelo gerou 3 mi ton extras com destino MAIS DIFÍCIL** — exportação BR não tem demanda elástica equivalente, ração interna cresce lento. Pressão estrutural sobre preço farelo BR.
- **Tendência multi-ano confirma trajetória**: 2024/25 → 25/26 → 26/27 subindo cada vez, indicando capacidade esmagadora BR rodando mais perto do limite.
- **REFORÇA insight B16 (2026-05-26_b16-bullish-farelo)**: B16 acelera o que JÁ está acontecendo. Cada +1pp de mistura puxa mais óleo interno → mais esmagamento → ainda mais farelo no mercado.

## Contexto / dados

### Série esmagamento BR (mil ton/mês, do dashboard StoneX)

| Mês | 2024/25 | 2025/26 | 2026/27 | YoY% |
|---|---|---|---|---|
| **mar** | **4.863** | **5.263** | **5.575** | **+5,9%** |
| abr | 4.835 | 5.325 | — | |
| mai | 4.764 | 5.463 | — | |
| jun | 4.755 | 5.080 | — | |
| jul | 4.929 | 5.256 | — | |
| ago | 4.852 | 5.090 | — | |
| set | 4.659 | 4.665 | — | |
| out | 4.940 | 4.897 | — | |
| nov | 4.605 | 4.853 | — | |
| dez | 4.689 | 4.990 | — | |
| jan | 3.763 | 4.325 | — | |
| fev | 4.024 | 4.431 | — | |
| **Total** | **55.678** | **59.639** | — | **+7,1%** |

### Conta de geração de subprodutos (yields padrão)

```
Soja esmagada 25/26: 59,6 mi ton
Geração óleo (18%):   10,73 mi ton  (vs 10,02 em 24/25 = +713k ton)
Geração farelo (77%): 45,90 mi ton  (vs 42,87 em 24/25 = +3.049k ton)
```

### Balanço óleo BR

```
+713 mil ton óleo extra gerado em 25/26
−150 mil ton exportação extra (1,36 → ~1,51 mi ton)
−~10 mil ton estoque (ABIOVE estoques estáveis)
= +553 mil ton absorvidas internamente → biodiesel B15 + indústria + consumo
```

Confirma que mesmo SEM B16, o sistema brasileiro já está consumindo internamente quase 75% do óleo extra que esmaga.

### Balanço farelo BR (estimativa)

```
+3.049 mil ton farelo extra gerado
Exportação BR farelo cresce ~150-250 mil ton/ano (média histórica)
Ração interna cresce ~5%/ano = ~1 mi ton (BR consome ~20 mi ton/ano)
= sobra ~1,5-1,8 mi ton sem destino claro → pressão sobre preço
```

### Cadeia de efeitos atualizada (vs insight B16 original)

```
2024/25 → 2025/26: já temos esmagamento +7,1% (4 mi ton de soja a mais)
  ↓ subproduto óleo: +713k → 75% absorvido B15 + 25% exportação
  ↓ subproduto farelo: +3.049k → exportação + ração não cobrem
  ↓ ESTOQUE FARELO BR sobe → preço pressionado pra baixo

2026 + B16 (cenário):
  +436k ton óleo demanda interna adicional (calculado no insight B16)
  → esmagamento ainda MAIS forte
  → ainda mais farelo no mercado
  → preço farelo cai mais rápido pra zona Far/Soj 77% (verde)
```

## Pergunta-tese

O que precisa ser verdadeiro pra essa tese se confirmar:

- **ABIOVE confirmar trajetória ascendente em jun-dez/26** (próximas releases mensais). Coletor `abiove` já está no sistema, falta visualização dedicada.
- **Estoque farelo BR subir** nos boletins ABIOVE mensais — sinal claro de oversupply.
- **Demanda chinesa de farelo não explodir** — se China comprar BR farelo (raro mas possível em quebra Argentina), absorve o excesso e tira pressão.
- **Esmagadoras NÃO cortarem turno** — se margem cair muito, esmagamento reduz e tese sai do trilho. Atualmente margem está em $3,46/bu CBOT (muito acima do piso $2), risco baixo.

## Próximas ações

- [ ] **Visualizar série esmagamento BR no HTML** — criar card na aba 🧮 Análise Quantitativa com gráfico mensal (3-4 temporadas). Coletor ABIOVE já roda, falta o renderer.
- [ ] **Trackear estoque farelo BR** mensal — verificar se ABIOVE publica e está sendo coletado; se não, adicionar ao coletor.
- [ ] **Monitorar próximo boletim ABIOVE** (geralmente sai dia 12-15 do mês seguinte) — vai trazer abr/26 oficial.
- [ ] **Conversar com Fabio na próxima call**: validar se a leitura de "75% do óleo extra absorvido por B15" está correta vs dados internos StoneX. Pergunta direta: quando o sistema deixa de digerir o esmagamento crescente?
- [ ] **Atualizar insight B16** com referência cruzada a este (dados de esmagamento confirmam tese).

## Revisão programada

- **D+90: 2026-08-24** — revisar:
  - 3 boletins ABIOVE adicionais (mai/jun/jul) saíram. Esmagamento continuou subindo?
  - Estoque farelo BR subiu ou ficou estável?
  - Preço farelo CEPEA Paranaguá deu sinal de cair?
- **D+180: 2026-11-22** — fechar ciclo:
  - Trajetória 26/27 vs 25/26 mantém tendência ou inflexionou?
  - Marcar status final (acerto/erro/parcial)

## Notas adicionais

**Por que esse dado é mais "operacional" que o B16:**
- B16 depende de decisão política (CNPE/MME) — pode levar 6-18 meses
- Esmagamento crescente é DADO REALIZADO, está acontecendo já
- Pra você (comprador de farelo): o piso de preço já está sendo construído pelo esmagamento atual; B16 é o "extra" que potencializa
- **Janela de compra**: se ABIOVE confirmar abr/mai/jun em alta, o estoque farelo começa a sobrar fisicamente em jul-ago → preço deve ceder antes da decisão política do B16
