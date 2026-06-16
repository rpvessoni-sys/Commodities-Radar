---
data: 2026-05-26
titulo: PIS/COFINS biodiesel — isenção 2026 vira custo, explica mercado físico fraco e cria resistência
tags: [fiscal, biodiesel, oleo_soja, pis_cofins, b16, regulatorio, brasil]
fontes:
  - MP do governo federal (abr/2026) que isentou biodiesel + querosene de aviação de PIS/COFINS — Diário do Transporte 06/abr/2026
  - STJ 2ª Turma 21/mai/2026 — crédito de PIS/Cofins sobre soja em biodiesel sob suspensão tributária (Lei 12.865/2013)
  - Lei 14.943/2024 + MP 1.227/24 (rejeição parcial pelo Congresso em 12/jun/2024)
  - Conversa com usuário em 26/mai/2026 — observação de mercado físico desaquecido
  - Cruz-referência [[2026-05-26_b16-bullish-farelo]]
  - Cruz-referência [[2026-05-26_curva-forward-cbot-oleo-desacopla]]
status: revisada
---

> ## ⚠️ ATUALIZAÇÃO 2026-06-05 (correções factuais da varredura completa)
> Ver síntese em [[2026-06-05_varredura-completa-complexo-soja]]. Correções:
> 1. **Isenção PIS/Cofins do biodiesel foi PRORROGADA até 31/jul/2026** (decreto 29/mai), não revogada. O ônus pra indústria é mais nuançado do que "virou custo direto": a isenção na saída foi mantida (temporária, renovações sucessivas geram incerteza de planejamento).
> 2. **STJ 21/mai = vitória da indústria** (REsp 2.165.276, 2ª Turma, unânime): crédito de PIS/Cofins sobre soja adquirida com suspensão tributária. Porém **não é vinculante** (não foi julgado como repetitivo).
> 3. **"Leilão ANP biodiesel" NÃO EXISTE** desde 2022 — modelo virou contratação bilateral direta distribuidora↔produtor. Toda menção a "leilão ANP jun/26" como gatilho está inválida. Sinal de margem deve vir do spread óleo-soja vs preço bilateral + produção mensal ANP.
> 4. **Mecanismo do esmagamento corrigido:** o aperto fiscal do biodiesel NÃO trava o esmagamento BR (que segue recorde, crush margin US$ 4,00/bu) porque o óleo encontra destino na EXPORTAÇÃO (+105% YoY) puxada pelo óleo CBOT forte. O aperto pesa no físico do óleo BR, não na geração de farelo.

## Resumo executivo

- **MP de abr/2026 isentou biodiesel de PIS/COFINS na saída.** Parece pró-indústria, mas tem efeito perverso: saída isenta = perde direito de creditar PIS/Cofins da entrada (óleo soja). Crédito que era recuperável vira **custo efetivo**.
- **Magnitude estimada setor:** R$ 1,35 bi/ano em créditos acumulados viram custo → **+3,4% sobre preço do biodiesel** atualmente praticado.
- **STJ 21/mai/2026** deu vitória parcial à indústria — permitiu crédito na compra de soja sob **regime de suspensão tributária** (Lei 12.865/2013), por unanimidade na 2ª Turma. Mas é caso específico, **não revoga a MP de abril**.
- **Tradução cadeia de preço:** indústria biodiesel BR menos competitiva → reduz produção OU pressiona governo por subsídio → **demanda industrial por óleo soja BR enfraquece** → mercado físico desaquece → preços atuais ganham **resistência** (teto justificado).
- **Conflito com tese B16** ([[2026-05-26_b16-bullish-farelo]]): se indústria biodiesel BR está com margem comprometida fiscalmente, o efeito de absorção interna do óleo via biodiesel fica **adiado ou neutralizado**. B16 chega mas indústria sem fôlego pra responder à demanda projetada.
- **Conflito com tese bullish farelo** ([[2026-05-26_esmagamento-br-recorde-reforça-bullish-farelo]]): se óleo BR não tem destino industrial forte, esmagadora perde estímulo a rodar 100% → menos farelo extra gerado → tese bullish farelo PERDE FORÇA.

## Contexto / dados

### Linha do tempo regulatória

| Data | Evento | Efeito |
|---|---|---|
| 2024 | **MP 1.227/24** tentou revogar ressarcimento/compensação de saldo credor PIS/Cofins pra setores (incl. biodiesel/soja) | Choque inicial — risco fiscal aberto |
| **12/jun/2024** | Congresso Nacional **REJEITA** incisos III e IV do art. 1º e arts. 5º e 6º da MP 1.227/24 | Vigência encerrada, efeito retroativo. Vitória temporária pra indústria. |
| 2024 | **Lei 14.943/2024** publicada | Marco legal do regime de créditos pós-MP |
| **abr/2026** | Nova MP do governo federal **isenta biodiesel + querosene aviação de PIS/COFINS** | "Isenção" elimina ônus na saída, mas elimina crédito da entrada → custo efetivo +3,4% pra indústria |
| **21/mai/2026** | STJ 2ª Turma (unânime) — crédito PIS/Cofins sobre soja em regime suspensão tributária | Vitória parcial — só pra operações sob Lei 12.865/2013, não revoga MP de abr |
| **26/mai/2026** | Observação operador: **mercado físico de óleo soja BR desaqueceu** + resistência nos preços | Sinal coerente com cenário regulatório |

### Por que "isenção" virou custo (mecânica tributária)

```
Regime ANTES (até abr/2026):
  Compra óleo soja → paga PIS/Cofins (entrada)
  Vende biodiesel → recolhe PIS/Cofins (saída)
  Diferença = crédito recuperável (não-cumulatividade)

Regime DEPOIS (MP abr/2026):
  Compra óleo soja → paga PIS/Cofins (entrada) → SEM crédito a recuperar
  Vende biodiesel → ISENTO de PIS/Cofins (saída)
  Diferença = CUSTO EFETIVO (PIS/Cofins da entrada vira despesa)
```

**Por que a indústria recebeu como "desastrosa":**
- Fecombustíveis publicou nota chamando o pacote de "MP das compensações desastrosa"
- Estimativa: R$ 1,35 bi/ano vira custo direto
- Repasse parcial pro preço final → biodiesel encarece → distribuidoras compram menos → indústria reduz produção

### Conexão com mercado físico óleo BR

- Insight B16 calculou +436k ton/ano de demanda interna adicional por óleo (se B16 sair)
- Esse cálculo assume **margem industrial saudável** pra indústria absorver o óleo
- Com custo +3,4% (sem repasse pleno), margem fica **menor** → indústria reduz turno ou pressiona ANP/CNPE por cronograma B16 mais lento
- Sinal observável: **basis físico óleo BR já em −R$ 2.378/t vs paridade CBOT** — pode ser parcialmente explicado por demanda industrial enfraquecida, não só fluxo de exportação

### Por que essa leitura pode DOMINAR as outras (A/B/C do insight curva forward)

[[2026-05-26_curva-forward-cbot-oleo-desacopla]] apresentou 3 leituras pro desacoplamento óleo:
- **A** — CBOT mundo, BR descolado (reforça bullish farelo)
- **B** — esmagadoras globais reduzem (questiona bullish farelo)
- **C** — volatilidade política US (RIN/EPA), sem reflexo BR

**Esta nova leitura é a Leitura D:**
- **D — Risco fiscal/regulatório BR:** isenção PIS/Cofins biodiesel (abr/2026) aperta margem industrial BR → demanda óleo interno enfraquece → mercado físico fica fraco com resistência nos preços atuais.

A leitura D é **estrutural e específica do BR** (as outras são CBOT global). Pode estar dominando o que vemos no físico hoje, independente do que o CBOT precifica pra dez/26.

## Pergunta-tese

O que precisa ser verdadeiro pra essa leitura se confirmar:

- **MP abr/2026 mantida sem reversão** — Congresso pode rejeitar (precedente da MP 1.227/24 em jun/2024) ou STF derrubar via ADI
- **Indústria biodiesel BR NÃO absorver o +3,4% sem repasse** — se margem comportar, efeito é nulo no fluxo físico
- **Subsídio compensatório (MP cria R$ 1,20 de subsídio ao diesel + linha de R$ 9 bi pra aéreas) NÃO chegar ao biodiesel** — se pacote inclui via lateral pra indústria de biodiesel, neutraliza
- **CNPE/MME confirmar cronograma B16 sem ajuste** — se governo recuar no B16 pra equilibrar pressão setorial, tese B16 (bullish farelo) também enfraquece

## Próximas ações

- [ ] **Validar com Fabio na próxima call** — perguntar se StoneX vê o efeito PIS/Cofins refletindo no físico BR e qual % do desaquecimento atual o consultor atribui a esse fator vs sazonalidade
- [ ] **Monitorar Câmara/Senado** — verificar se há MP de reversão sendo articulada (caminho similar à MP 1.227/24)
- [ ] **Acompanhar Boletins ABIOVE** — esmagamento e estoque óleo BR jun/jul vão dizer se indústria reduziu turno
- [ ] **Trackear preço biodiesel ANP** mensal — repasse do custo aparece no leilão ANP de biodiesel (próximo: jun/2026). Custo médio do leilão deve subir +R$ 0,05-0,10/L
- [ ] **Atualizar insight B16** com ressalva crítica de risco fiscal — se indústria não consegue absorver economicamente, premissa B16 → +436k ton óleo demanda interna FRAGILIZA
- [ ] **Atualizar insight curva forward** com Leitura D como dominante BR

## Revisão programada

- **D+45: 2026-07-10** — checagem rápida:
  - Congresso votou reversão da MP de abr/2026?
  - Leilão ANP biodiesel jun saiu? Preço médio subiu o esperado?
  - Boletim ABIOVE mai/jun mostrou queda de esmagamento ou continuou recorde?
  - Fabio confirmou leitura em call?
- **D+90: 2026-08-24** — revisão formal:
  - STF/STJ moveu posição sobre crédito PIS/Cofins biodiesel?
  - Demanda industrial óleo soja BR continua fraca ou recuperou?
  - Marcar status `revisada` se mercado validou leitura
- **D+180: 2026-11-22** — fechar ciclo:
  - Indústria biodiesel BR reduziu produção? Cresceu? Estável?
  - B16 saiu (e indústria conseguiu acompanhar)?
  - Marcar status final (acerto/erro/parcial)

## Notas adicionais

**Por que essa observação importa mais que o desacoplamento CBOT (insight curva forward):**
- Desacoplamento CBOT é sinal de mercado externo — útil pra entender mundo, mas BR opera com basis próprio
- Risco fiscal BR é mecanismo CAUSAL específico, com endereço (MP, ANP, CNPE) e cronograma (leilões mensais ANP, votação Congresso)
- Pra operador BR (comprador de farelo), risco fiscal é **driver direto** de preço físico — não passa por CBOT

**Por que o impacto é NEGATIVO pra tese bullish farelo (importante revisão crítica):**
- Tese bullish farelo depende de: esmagamento alto → mais farelo subproduto → preço cai
- Esmagamento alto depende de: demanda óleo (export OU biodiesel interno) puxando crush margin
- Se biodiesel BR aperta por custo fiscal → demanda óleo interno cai → crush margin pode ceder → esmagamento reduz turno → menos farelo extra → tese **PERDE FORÇA**
- Esse insight, portanto, deve ser lido como **CONTRA-PESO** aos insights B16 e esmagamento recorde
- **Resultado líquido depende de QUAL FORÇA VENCE**: B16 + esmagamento histórico (puxam farelo pra baixo) vs aperto fiscal biodiesel (segura demanda óleo → reduz esmagamento futuro)

**Por que o usuário levantou isso AGORA:**
- Está vendo no físico (mercado dele, contato diário)
- Antes do CBOT precificar
- Antes dos boletins ABIOVE confirmarem
- Esse é um sinal raro de **realidade microeconômica** chegando antes do macro estatístico — vale dobrar atenção
