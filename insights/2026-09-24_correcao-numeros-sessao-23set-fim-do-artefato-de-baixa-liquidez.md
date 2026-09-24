---
data: 2026-09-24
titulo: "Auditoria da sessão de 23/09: os fechamentos e volumes usados pela leitura de ontem eram parciais nos três produtos — o dump de hoje traz, para a mesma data, farelo e soja mais BAIXOS (não mais altos), volumes 30 vezes maiores em soja/farelo/óleo (encerrando o 'regime de baixa liquidez' de cinco sessões), e uma margem de biodiesel que caiu -13,2% (não subiu +1,17%) porque o heating oil realmente despencou -6,24%, não ficou estável como sugeria o dado duplicado"
tags: [farelo, soja, oleo_soja, dados, auto-claude]
fontes:
  - CME CBOT — linhas brutas da sessão de 2026-09-23 presentes no dump de hoje (`briefing/latest.md`, seção `cme_cbot`): soja (ZSX26.CBT) abertura 1.324,75, máxima 1.327,25, mínima 1.311,00, **fechamento 1.317,50**, volume **117.139** contratos; farelo (ZMZ26.CBT) abertura 370,70, máxima 373,40, mínima 367,70, **fechamento 370,20**, volume **89.807** contratos; óleo (ZLZ26.CBT) abertura 67,95, máxima 68,21, mínima 67,03, **fechamento 67,71**, volume **89.625** contratos; heating oil (HO=F) abertura 4,6777, máxima 4,6875, mínima 4,6266, **fechamento 4,6336**, volume **859** contratos (ver seção final — aqui a divergência vai na direção oposta às outras quatro)
  - Indicadores sintéticos internos, 2026-09-23 (seção `indicators` do dump de hoje): crush margin **2,4175** USD/bushel ("farelo 370,20 + óleo 67,71 − soja 1.317,50"), far_soj_ratio_pct **84,3%** ("farelo 370,20/sht ÷ (soja 1.317,50cts × 33,33)"), oil_share_pct **47,77%**, oil_meal_spread_usd_bu **-0,6963**, paridade BR soja **R$149,34/saca** ("CBOT 1.317,50 × USD/BRL 5,1414"); biodiesel_us: custo_óleo **5,0782** USD/galão, receita **7,7986** USD/galão ("HO 4,63 + 1,5×RIN 2,11"), margem **1,9204** USD/galão
  - Fila de julgamento — 2026-09-24 (a mesma que acompanha o dump de hoje), itens `alerta-quebra_resistencia-soja_cbot-2026-09-23` ("soja_cbot fechou em **1317.50**"), `alerta-quebra_resistencia-farelo_cbot-2026-09-23` ("farelo_cbot fechou em **370.20**"), `alerta-quebra_suporte-oleo_cbot-2026-09-23` ("oleo_cbot fechou em **67.71**") e `alerta-quebra_suporte-complexo_soja-2026-09-23` ("complexo_soja fechou em **2.42**") — os quatro gerados automaticamente pelo robô a partir do banco de indicadores, e os quatro confirmam de forma independente os números do dump de hoje, não os da leitura de ontem
  - Comparação: [[2026-09-23_leitura-complexo]], que usou para a mesma sessão de 23/09 fechamento soja 1.326,25 (volume 3.843), farelo 372,60 (volume 2.996), óleo 67,72 (volume 2.986), heating oil 4,6920 (volume 2.189), ratio Far/Soj 84,28%, oil share 47,61%, oil-meal spread -0,748, crush margin 2,3839, paridade BR R$149,59, margem de biodiesel US$1,978
  - Precedentes diretos: [[2026-09-13_correcao-numeros-sessao-11set-farelo-oleo]] e [[2026-09-16_correcao-numeros-sessao-15set-ratio-salta-para-8191]] — mesma classe de problema (fechamentos/volumes de uma sessão revisados na geração seguinte do briefing), mesma fonte CME CBOT, mesma metodologia de verificação cruzada via fila autogerada; também [[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]] e [[2026-09-22_leitura-complexo]], que haviam documentado três e depois uma quarta ocorrência de um padrão de OHLC/volume duplicado especificamente em farelo e heating oil nas sessões de 19-22/09
status: ativa
vies: [bull-farelo, bear-oleo_soja, neutral-soja]
---

## Por que este insight existe separado da leitura diária

Ao preparar a leitura de hoje (24/09), cruzei os números usados pela leitura de ontem
([[2026-09-23_leitura-complexo]]) contra as linhas brutas que o dump de hoje efetivamente traz
para a mesma sessão de 23/09. Os números não batem em nenhum dos três produtos principais, e a
divergência é grande o suficiente para mudar duas conclusões centrais da leitura de ontem: (1) a
ideia de que farelo subiu pela terceira sessão seguida (+0,43%) é o oposto do que os dados de
hoje mostram (farelo **caiu** -0,13% frente a 22/09); e (2) a margem de biodiesel americana não
teve um "pequeno repique" de +1,17% — ela **despencou -13,2%**, porque o heating oil (HO=F) que
alimenta essa fórmula caiu de verdade -6,24%, e não ficou estável como sugeria o par de valores
idênticos usado ontem. Este é o terceiro episódio desta classe específica de problema
(fechamentos/volumes de uma sessão sendo revisados na geração seguinte do dump), depois dos
episódios de 11/09 e 15/09, e a boa notícia é que ele também resolve, de uma vez, o "regime de
baixa liquidez" que as leituras de 21, 22 e 23/09 vinham descrevendo como um fato de mercado —
o dado de hoje mostra que não era.

## O que diverge, produto por produto

| Métrica (sessão 23/09) | Usado na leitura de 23/09 | No dump de hoje (24/09) | Fonte que corrobora o valor correto |
|---|---|---|---|
| Soja CBOT fechamento | 1.326,25 | **1.317,50** | `alerta-quebra_resistencia-soja_cbot-2026-09-23` (fila, autogerado) e `soja_paridade_br` (indicators) |
| Soja CBOT volume | 3.843 | **117.139** (30,5×) | linha bruta `cme_cbot` |
| Soja variação vs 22/09 | +0,09% | **-0,60%** | recalculado de 1.325,50→1.317,50 |
| Farelo CBOT fechamento | 372,60 | **370,20** | `alerta-quebra_resistencia-farelo_cbot-2026-09-23` (fila, autogerado) e `complexo_soja.crush_margin_usd_bu` (indicators) |
| Farelo CBOT volume | 2.996 | **89.807** (30,0×) | linha bruta `cme_cbot` |
| Farelo variação vs 22/09 | +0,43% | **-0,13%** | recalculado de 370,70→370,20 — **muda de sinal** |
| Óleo CBOT fechamento | 67,72 | **67,71** | `alerta-quebra_suporte-oleo_cbot-2026-09-23` (fila, autogerado) e `biodiesel_us.custo_oleo_usd_galao` (indicators) |
| Óleo CBOT volume | 2.986 | **89.625** (30,0×) | linha bruta `cme_cbot` |
| Óleo variação vs 22/09 | -0,24% | **-0,31%** | recalculado de 67,92→67,71 (mesma direção, magnitude próxima) |
| Heating oil (HO=F) fechamento | 4,6920 | **4,6336** | linha bruta `cme_cbot` (heating_oil_cbot) — muda -6,24% de verdade, não fica estável |
| Heating oil volume | 2.189 | **859** (0,39×) | linha bruta — aqui a correção vai na direção OPOSTA: o volume real é ainda mais baixo (ver seção final) |
| Ratio Far/Soj | 84,28% | **84,30%** | `complexo_soja.far_soj_ratio_pct` (indicators) — coincidência: farelo e soja caíram em proporção quase igual, então o ratio calculado bate por acidente |
| Oil share | 47,61% | **47,77%** | `complexo_soja.oil_share_pct` (indicators) |
| Oil-meal spread | -0,748 | **-0,6963** | `complexo_soja.oil_meal_spread_usd_bu` (indicators) |
| Crush margin | 2,3839 (dist. -4,64%) | **2,4175** (dist. -3,30%) | `alerta-quebra_suporte-complexo_soja-2026-09-23` (fila arredonda p/ "2.42") |
| Paridade BR soja | R$149,59 | **R$149,34** | `soja_paridade_br.brl_saca_paridade` (indicators) |
| Margem biodiesel US | US$1,978 (+1,17% vs 22/09) | **US$1,9204 (-13,23% vs 22/09)** | `biodiesel_us.margem_usd_galao` (indicators) — **muda de sinal e de magnitude** |

O ISF (60/100) e o ISO (80/100) são, de novo, as duas únicas métricas que batem exatamente
entre as duas leituras — a mesma constatação já feita nas auditorias de 13/09 e 16/09: esses
índices compostos não reagem a revisões de sessão porque dependem de contagem de condições
estruturais, não do fechamento diário em si.

## Por que confio nos números do dump de hoje, e não nos de ontem

A mesma lógica de verificação cruzada usada nas auditorias de 13/09 e 16/09 se aplica aqui:

1. **A fila de julgamento é gerada automaticamente pelo robô a partir do banco de
   indicadores**, não por este analista. Os itens `alerta-quebra_resistencia-soja_cbot-2026-09-23`,
   `alerta-quebra_resistencia-farelo_cbot-2026-09-23` e `alerta-quebra_suporte-oleo_cbot-2026-09-23`
   citam literalmente 1.317,50 / 370,20 / 67,71 — se a leitura de ontem estivesse certa
   (1.326,25 / 372,60 / 67,72), a fila teria gerado números diferentes. Ela não gerou.
2. **Os volumes corrigidos caem dentro da faixa histórica recente desta mesma janela do dump**
   (soja 100-120 mil, farelo 90-115 mil, óleo 67-90 mil, todos citados em leituras anteriores
   como referência de sessão plenamente líquida, ex. 18/09: 108.222/113.303/67.046) — os
   volumes de ontem (3.843/2.996/2.986) eram órfãos desse padrão, exatamente o sinal de alerta
   que a própria leitura de 23/09 já havia registrado, sem conseguir confirmá-lo, como possível
   artefato de captura.
3. **As três fórmulas internas (crush margin, ratio, paridade BR, margem de biodiesel) fecham
   de forma consistente com os novos fechamentos**, e não fechariam com os antigos — por
   exemplo, o crush margin de 2,4175 só bate com "farelo 370,20 + óleo 67,71 − soja 1.317,50"
   descrito literalmente na nota de fonte do próprio indicador, e a margem de biodiesel de
   1,9204 só bate com receita "HO 4,63 + 1,5×RIN 2,11" — usando o HO=F **corrigido**, não o
   valor de 4,6920 usado ontem.
4. **A sessão de 22/09 também aparece no dump de hoje, com valores plausíveis e consistentes
   com o que já vinha sendo reportado** (farelo abertura 367,60, fechamento 370,70, máxima
   374,10, mínima 365,90, volume 93.810; heating oil fechamento 4,9421, volume 27.344) — ou
   seja, o problema era específico da leitura mais recente do dump (23/09) no momento em que
   ontem escrevi a leitura, não um problema generalizado de todas as sessões.

## O que muda na leitura do complexo

A mudança mais importante não é de direção do ratio Far/Soj (ele segue subindo, agora
82,53%→83,22%→83,90%→**84,30%**, uma trajetória de três altas consecutivas real, não uma
suposição construída sobre dado parcial) — é de **duas outras coisas**:

- **O "regime de baixa liquidez" das sessões de 21-23/09, descrito nas três últimas leituras
  diárias como um fato de mercado que reduzia a confiança em qualquer leitura de volume, não
  existiu em soja, farelo e óleo.** Os volumes reais de 23/09 (117.139 / 89.807 / 89.625) são
  saudáveis e comparáveis aos de sessões plenas anteriores — o que existiu foi uma falha de
  captura que, por três dias seguidos, gravou uma fração de ~2,6%-4,8% do volume real
  encontrada tarde demais no pregão (provavelmente uma leitura intraday parcial em vez do
  fechamento consolidado), e que só é corrigida na geração seguinte do dump. Isso não significa
  que a liquidez nunca tenha sido um problema real nesta série — significa que, especificamente
  nesta janela de três dias, a leitura de "baixa liquidez" era do dado, não do mercado.
- **A margem de biodiesel americana não deu um pequeno repique dentro de uma tendência de
  queda — ela aprofundou a queda de forma acentuada**: 2,2927 (17/09) → 2,3063 (18/09) → 2,0908
  (21/09) → 2,2131 (22/09) → **1,9204 (23/09, -13,23% em um dia, a maior queda diária desta
  janela)**. Isso muda o peso do argumento contra a tese bear-óleo: o contraponto de "a margem
  de biodiesel está se recuperando" que a leitura de ontem registrava como um sinal fraco a
  favor do lado comprado simplesmente não existe nos dados reais — o sinal real é o oposto,
  reforço adicional ao bear-óleo.
- **Farelo caiu, não subiu, na sessão de 23/09** (-0,13%, não +0,43%) — isso não desfaz a tese
  bull-farelo (o ratio Far/Soj, que é o indicador que efetivamente rege essa tese, segue subindo
  porque a soja caiu ainda mais que o farelo, -0,60% vs -0,13%), mas muda a leitura de "força
  absoluta do farelo" para "força relativa do farelo dentro do crush" — uma distinção
  importante para quem opera o produto direcionalmente vs. quem opera o spread Far/Soj.

## O que ainda não está resolvido

- **O volume do heating oil (HO=F) em 23/09 é genuinamente baixo mesmo depois da correção geral
  dos outros três instrumentos — apenas 859 contratos, 0,39× o valor (já incorreto) usado
  ontem, e apenas 3,1% do volume real de 22/09 (27.344).** Diferente de soja, farelo e óleo, que
  se revelaram plenamente líquidos assim que os dados corretos chegaram, o HO=F específico
  parece ter tido uma sessão de fato pouco negociada em 23/09 — ou o mesmo problema de captura
  que afeta os outros contratos ainda não foi corrigido para este ticker em particular. Como o
  fechamento de HO=F (4,6336) alimenta diretamente a margem de biodiesel usada na tese de óleo,
  esse ponto específico ainda merece o mesmo ceticismo metodológico que as leituras anteriores
  já vinham aplicando — mas agora apenas para este instrumento, não para o complexo inteiro.
- **Este é o terceiro episódio desta classe de problema em duas semanas** (11/09, 15/09 e agora
  23/09), sempre na mesma direção quanto a soja/farelo/óleo (dado inicial com volume muito
  abaixo do normal, correção posterior recupera o volume real) — mas desta vez a direção do
  fechamento também mudou de sinal em farelo e na margem de biodiesel, o que é novo frente aos
  dois episódios anteriores (onde a correção sempre apontava para o MESMO sentido direcional,
  só com magnitude maior). Isso eleva o nível de cautela recomendado: a partir de hoje, o
  fechamento do dia mais recente do dump deveria ser tratado como sujeito a possível revisão de
  sinal, não apenas de magnitude, até a geração seguinte confirmar.

Cruza com [[2026-09-24_leitura-complexo]] (leitura diária de hoje, que incorpora esta correção
em todas as seções e trata os itens de fila `alerta-quebra_resistencia-soja_cbot-2026-09-23`,
`alerta-quebra_resistencia-farelo_cbot-2026-09-23`, `alerta-quebra_suporte-oleo_cbot-2026-09-23`
e `alerta-quebra_suporte-complexo_soja-2026-09-23`).
