---
data: 2026-09-20
titulo: "Fim de semana sem novo pregão (o último fechamento de Chicago segue sendo o de sexta-feira, 18/09) — mas dois achados estruturais novos justificam a leitura: o contrato de referência de farelo e óleo rolou de outubro/26 (V26) para dezembro/26 (Z26), elevando o nível absoluto de preço e do ratio Far/Soj sem que isso seja um movimento real de mercado; e o heating oil (HO=F) de 18/09 sofreu pela quarta vez nesta série uma revisão para cima (de US$4,8367 para US$5,0578, +4,57%), corrigindo a narrativa de ontem de que a margem de biodiesel americana estaria caindo — na realidade ela subiu ligeiramente, para US$2,3063/galão"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT — sessão de **2026-09-18** (sexta-feira; é o fechamento mais recente existente, porque hoje, 2026-09-20, é domingo e não há pregão em Chicago desde então): soja (ticker ZSX26.CBT, venc. nov/26 — **sem rolagem**, mesmo contrato usado em todas as leituras recentes) abertura 1.317,50, máxima 1.322,00, mínima 1.300,00, fechamento **1.303,50**, volume 145.289 contratos; farelo (ticker **ZMZ26.CBT, venc. dez/26 — CONTRATO ROLADO**, ver Visão geral) abertura 370,00, máxima 372,30, mínima 356,60, fechamento **358,60**, volume 141.412 contratos; óleo (ticker **ZLZ26.CBT, venc. dez/26 — também rolado**) abertura 69,17, máxima 69,20, mínima 68,01, fechamento **68,22**, volume 95.649 contratos. Curva futura em 18/09 — soja: nov/26 (base) 1.303,50 → jan/27 1.320,00 → mar/27 1.329,50 → mai/27 1.336,50 → jul/27 1.340,50; farelo: out/26 354,60 → dez/26 (base, novo front) 358,60 → jan/27 360,40 → mar/27 361,70 → mai/27 362,30; óleo: out/26 67,70 → dez/26 (base, novo front) 68,22 → jan/27 68,52 → mar/27 68,69 → mai/27 68,75
  - CME CBOT — sessão de **2026-09-17, como aparece no dump de hoje** (mesmo ticker Z26 já usado para farelo, retido nesta janela): farelo abertura 366,80, máxima 375,60, mínima 364,60, fechamento **371,30**, volume **141.412 contratos** — número de volume **idêntico, dígito a dígito**, ao de 18/09 (ver Honestidade); nenhuma linha de 17/09 está disponível nesta seção do dump para soja ou óleo (lacuna, ver Honestidade) — para esses dois, uso os valores gravados nas fórmulas da seção `indicators` (ver abaixo)
  - CME NYMEX heating oil (HO=F) — **2026-09-18**: abertura 5,0470, máxima 5,1710, mínima 4,9935, fechamento **5,0578** USD/galão, volume **45.315** contratos
  - CME NYMEX heating oil (HO=F) — **2026-09-17, como aparece no dump de hoje**: fechamento **5,1139** USD/galão, volume **45.315 contratos** — outra vez o mesmo número de volume do dia seguinte, dígito a dígito (ver Honestidade); este fechamento de 17/09 é o mesmo já usado na leitura de ontem, sem nova revisão desta vez
  - Indicadores sintéticos internos — série completa dos últimos cinco fechamentos com fórmula publicada (`indicators`, 14 a 18/09, valores-fonte de farelo/óleo/soja embutidos em cada fórmula, usados aqui como a série mais confiável de preço dia a dia porque não dependem da tabela `cme_cbot`, que tem lacunas nesta janela): farelo 356,20 → 365,40 → 365,60 → 371,30 → **358,60**; óleo 70,19 → 70,35 → 69,67 → 69,15 → **68,22**; soja 1.304,25 → 1.318,75 → 1.320,50 → 1.319,75 → **1.303,50**; ratio Far/Soj 81,93% → 83,12% → 83,06% → 84,40% → **82,53%**; oil share 49,05% → 48,79% → 48,22% → **48,75%** (14/09 sem registro); oil-meal spread -0,1155 → -0,3003 → -0,3795 → -0,5621 → **-0,385** USD/bushel; crush margin 2,5148 → 2,5898 → 2,5019 → 2,5776 → **2,3584** USD/bushel; paridade BR soja 149,70 → 150,00 → 149,90 → **148,21** BRL/saca (15 a 18/09; 14/09 sem registro); margem biodiesel US 2,0622 → 2,3508 → 2,3863 → 2,2927 → **2,3063** USD/galão; ISF (Índice de Sobra de Farelo) e ISO (Índice de Suporte do Óleo) travados em 60/100 e 80/100 desde 11/09, e novamente atualizados (sem mudança) em **2026-09-19**
  - BCB PTAX — **2026-09-18** (última publicação; sem PTAX no fim de semana): USD/BRL **5,1575** (+0,10% vs 5,1521 de 17/09), EUR/BRL 5,9126, Selic diária 0,050788% a.a. (séries SGS 1, 21619, 11)
  - CFTC COT Managed Money — corte de posições de **2026-09-15** (sem corte novo nesta janela; próximo corte é o de 22/09, esperado por volta de 25-26/09): farelo net long managed money 183.111 contratos (+16,12% vs 08/09), long 195.227 (+12,80%), short 12.116 (-21,29%), OI 683.474; óleo net long 101.480 (+10,65%), long 126.365, short 24.885, OI 605.960; soja net long 241.501 (-6,13%), long 282.581 (-3,63%), short 41.080 (+14,25%), OI 1.104.880; producer (comercial) farelo: short 445.202 (+4,53%), long 93.936 (-12,18%); producer soja long 323.727 (+11,04%)
  - USDA Crop Progress — corte de **2026-09-13** (sem corte novo nesta janela; próximo corte esperado na tarde de **segunda-feira, 2026-09-21**, horário americano, padrão semanal do USDA): 12% excelente / 46% boa / 9% ruim (G/E 58%, inalterado desde 30/08), colheita 2025/26 em **6% concluída**
  - USDA WASDE — edição de **2026-09-11** (sem edição nova nesta janela; tabelas de soja em grão e óleo ainda ausentes desta edição): farelo Argentina 2026/27 exportação **2,99 milhões de toneladas** (revisão ago→set já registrada), produção 33,11 mi t; farelo Brasil 2025/26 exportação estável em 0,2 milhão de toneladas, produção 2026/27 8,0 mi t
  - NOPA — item de fila `release-nopa-2026-09-19`: `monthly_status` em 0,0 bool (paywall, sem dado novo, quinto dia seguido de repetição vazia)
  - ABIOVE projeções mensais — balanços out-dez/2026, sem revisão nesta janela: produção de farelo recuando de 2.143 (out) para 1.978 (nov) e 1.659 mil t (dez); exportação de farelo de 850 para 800 e 700 mil t no mesmo período; óleo produção de 536 para 495 e 415 mil t; estoque final de soja de 5.721 para 3.659 e 1.890 mil t
  - NOAA CPC ENSO — El Niño Advisory, inalterado (carimbo 2026-09-19)
  - MPOB — carimbo 2026-09-19, parser sem números extraídos (mesma barreira há semanas)
  - BCBA (Argentina) — carimbo 2026-09-09, scraper acessa a página mas não encontra links de relatório
  - INMET — previsão para **2026-09-20 (HOJE)**: Cascavel/PR 31°C/18°C nublado com pancadas de chuva e trovoadas (sem menção de granizo, ao contrário da previsão de ontem para 19/09); Maringá/PR 31°C/21°C muitas nuvens com possibilidade de chuva isolada; Passo Fundo/RS 25°C/17°C nublado com pancadas de chuva e trovoadas isoladas (mínima seguiu subindo, de 14°C ontem para 17°C hoje, sem menção de geada); no núcleo produtor de Mato Grosso, Cuiabá 41°C/24°C, Sinop 40°C/24°C, Sorriso 40°C/24°C, Lucas do Rio Verde 40°C/24°C (todos com pancadas/chuva isolada), Rio Verde/GO 35°C/21°C (poucas nuvens)
  - Notícias Agrícolas/Canal Rural + FarmProgress RSS — "0 items lidos, 0 mantidos" por dez dias corridos consecutivos (10 a 19/09), sem visibilidade ainda sobre 20/09 nesta janela do dump
  - system/tributario_watch.toml (lido como referência, não editado) — `atualizado_em` 2026-06-05 em todos os 10 eventos catalogados, **107 dias corridos** sem revisão humana frente a hoje (20/09)
  - Forecasts estatísticos internos (bandas 7d/30d) — geração de **2026-09-19**, sobre o fechamento de 18/09 (já com o farelo/óleo no contrato Z26 novo), alvos 26/09 e 19/10: viés "altista" em soja, farelo e óleo nos dois horizontes
  - Fila de julgamento (carimbada 2026-09-19 no briefing, 8 itens, todos 🔴/🟡, todos tratados nesta leitura): `alerta-quebra_resistencia-soja_cbot-2026-09-18`, `alerta-quebra_suporte-oleo_cbot-2026-09-18`, `alerta-quebra_resistencia-farelo_cbot-2026-09-18`, `alerta-movimento_forte-farelo_cbot-2026-09-18`, `alerta-quebra_suporte-complexo_soja-2026-09-18`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`, `release-nopa-2026-09-19`
  - Código-fonte `system/sources/cme_cbot.py` (lido apenas como referência técnica, para confirmar o mecanismo de rolagem de contrato — NÃO editado; nenhuma alteração foi feita fora de `insights/`): função `_front_contract`, com `ROLL_DIAS = 12` — o contrato líquido mais próximo deixa de ser "front" quando faltam ≤12 dias corridos para o primeiro dia do mês de entrega
  - Cruza com [[2026-09-19_leitura-complexo]] (leitura de ontem, cujos números de farelo/óleo eram baseados no contrato de outubro/26, hoje substituído), [[2026-09-17_ratio-far-soj-supera-nivel-de-abertura-da-tese-original-quarta-sessao]] (veredito de invalidação da tese baixista de junho, hoje com uma ressalva de comparabilidade — ver Farelo), [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]] (tese original, nível de abertura do ratio 81,4%, contrato de julho/26), e [[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]] (as três ocorrências anteriores do padrão de revisão do HO=F, hoje com uma quarta ocorrência documentada)
status: ativa
vies: [bull-farelo, neutral-soja, bear-oleo_soja]
---

## Visão geral

O complexo soja gira em torno do "crush" (esmagamento industrial): a soja em grão é
triturada e separada em farelo (concentrado proteico para ração animal, sobretudo aves e
suínos) e óleo (alimentação humana e, cada vez mais, biodiesel). Quem "manda" no crush é
definido pelo "oil share" — a fatia do valor total gerado pelo esmagamento que vem do óleo.
Oil share alto significa que a indústria esmaga atrás do valor do óleo, e o farelo "sobra"
como subproduto que precisa ser escoado a qualquer preço. Oil share baixo é o oposto: o
farelo passa a pagar a conta do esmagamento e o óleo perde protagonismo relativo. O
termômetro mais direto dessa disputa é o ratio Far/Soj — preço do farelo dividido pelo preço
da soja, em percentual: abaixo de 80% o farelo está "abundante" (baixista); entre 80% e 87%
ele está "neutro"; acima de 87% ele fica "apertado" (altista).

**Hoje, 2026-09-20, é domingo — não há pregão novo em Chicago desde a sexta-feira, 18/09.**
Isso muda a natureza desta leitura em relação às anteriores: não há um novo "dia de mercado"
para narrar, e qualquer leitura de "o que mudou hoje" seria inventada se tratasse os números
de sexta como se fossem de um novo pregão. Dito isso, dois achados genuinamente novos surgem
comparando o dump de hoje com o de ontem — nenhum deles é uma variação de preço, mas ambos
mudam COMO os números devem ser lidos, e por isso merecem uma leitura completa em vez de uma
simples repetição do fechamento de sexta.

**Achado 1 — rolagem de contrato em farelo e óleo, confirmada no código-fonte.** Até a
leitura de ontem, o preço "de referência" (front-month) de farelo e óleo vinha do contrato de
outubro/2026 (tickers ZMV26 e ZLV26). No dump de hoje, o contrato de referência de ambos
passou a ser o de **dezembro/2026** (ZMZ26 e ZLZ26) — farelo saltou, na aparência, de 354,70
para 358,60 (+1,10%) e óleo de 67,58 para 68,22 (+0,95%) entre uma leitura e outra, mas isso
**não é uma alta de mercado**: é a mesma coisa que comparar o preço de duas gasolinas de
datas de validade diferentes. O sistema que coleta esses dados (`system/sources/cme_cbot.py`)
tem uma regra explícita para isso — `_front_contract`, com `ROLL_DIAS = 12` — que troca o
contrato de referência para o próximo vencimento líquido assim que faltam 12 dias corridos ou
menos para o primeiro dia do mês de entrega do contrato atual. Outubro/2026 começa em
01/10/2026; 12 dias antes disso é 19/09/2026 — exatamente a data em que esta rolagem passou a
valer. A soja não rolou porque seu próximo vencimento (novembro/2026, ticker ZSX26) ainda está
longe o suficiente da janela de troca. O motivo prático de existir essa regra, segundo o
próprio comentário no código, é evitar o problema oposto (o símbolo contínuo do Yahoo Finance
"rolando errado" perto do vencimento e devolvendo um contrato desatualizado) — ou seja, a
rolagem em si é um comportamento correto e esperado do sistema, não um bug. O que importa para
a leitura é a implicação prática: **os níveis absolutos de farelo e óleo citados a partir de
hoje não são diretamente comparáveis, ponto a ponto, aos níveis citados nas leituras
anteriores a 19/09**, porque o contrato de dezembro historicamente cota com um pequeno prêmio
de contango sobre o de outubro (a curva de 18/09 mostra exatamente isso: outubro 354,60 vs.
dezembro 358,60 em farelo, uma diferença de +1,13% que é estrutura de curva, não notícia).
Isso tem uma consequência concreta para uma tese em acompanhamento há meses nesta série — o
ratio Far/Soj da tese de 11/06 (ver seção Farelo) — porque o "nível de abertura" de 81,4%
daquela tese foi calculado sobre o contrato de julho/2026, que já rolou pelo menos duas vezes
(para outubro e agora para dezembro) até chegar ao ratio de hoje. A comparação direta entre os
dois nunca foi rigorosamente "maçã com maçã", mas a rolagem de hoje reabre essa ressalva de
forma mais visível do que nunca.

**Achado 2 — quarta confirmação do padrão de revisão do heating oil (HO=F), e ele muda a
narrativa da margem de biodiesel.** A leitura de ontem usou o fechamento de 18/09 do HO=F como
US$4,8367/galão, concluindo que a margem de biodiesel americana havia caído para
US$2,1332/galão (uma queda adicional depois do pico revisado de 16/09). No dump de hoje, esse
mesmo fechamento de 18/09 aparece revisado para **US$5,0578/galão** (+4,57%) — a quarta
ocorrência documentada do mesmo padrão estrutural identificado no insight dedicado
[[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]] (as três ocorrências anteriores:
11/09 +3,77%, 16/09 +5,65%, 17/09 +5,91%; agora 18/09 +4,57% — sempre revisão para cima, na
mesma faixa de magnitude). Com o valor revisado, a margem de biodiesel de 18/09 não caiu para
US$2,1332 como se pensava ontem: ela ficou em **US$2,3063/galão**, uma leve **alta** de +0,59%
sobre os US$2,2927 de 17/09 — o oposto direcional do que a leitura de ontem descrevia. O
mecanismo por trás dessa pequena alta, uma vez corrigido o dado: o custo do óleo caiu junto
com o preço do óleo em Chicago (-1,35%, de US$5,1863 para US$5,1165 por galão-equivalente),
uma queda de custo ligeiramente maior do que a queda de receita do HO revisado (-1,10%, de
US$5,1139 para US$5,0578), então a margem, que é receita menos custo, se sustentou. Isso muda
a leitura fundamentalista do óleo: o principal contra-argumento à tese baixista (a margem de
biodiesel comprimindo) está, com o dado corrigido, mais estável do que parecia ontem — ver
seção Óleo para o detalhamento completo.

Com essas duas ressalvas registradas, o retrato de sexta-feira (18/09) que efetivamente
prevalece até a reabertura de amanhã (segunda-feira, 21/09) é o seguinte: farelo caiu -3,42%
(371,30 → 358,60, mesma base de contrato Z26 nos dois dias — este é o único ponto em que a
comparação dia a dia É válida, porque o dado da fila usa consistentemente o mesmo ticker),
óleo caiu -1,34% (69,15 → 68,22, usando os valores gravados nas fórmulas de indicadores) e
soja caiu -1,23% (1.319,75 → 1.303,50). O ratio Far/Soj, calculado já sobre o novo contrato de
dezembro, fechou em **82,53%** — abaixo do pico de 84,40% de quinta-feira, mas ainda dentro da
zona "neutra" (80-87%) e ainda acima do nível de abertura da tese de junho (81,4%), embora com
a ressalva de comparabilidade explicada acima. O crush margin caiu -8,51% (2,5776 → 2,3584
USD/bushel), voltando a ficar abaixo do piso de referência de US$2,50 citado pela fila
(`alerta-quebra_suporte-complexo_soja-2026-09-18`).

**Leitura de uma linha**: nada de novo aconteceu no mercado desde sexta — é fim de semana —,
mas dois achados de qualidade de dado (rolagem de contrato em farelo/óleo, quarta revisão do
HO=F) mudam como os números de sexta devem ser lidos, e a correção da margem de biodiesel (de
"caindo" para "estável, levemente em alta") é relevante o suficiente para manter o viés
bear-óleo como "moderado", não "reforçado". O pivô do complexo segue sendo o ratio Far/Soj: em
82,53% (base dezembro), ainda dentro da zona neutra, ainda tecnicamente acima do nível de
abertura da tese de junho — mas essa comparação específica carrega, a partir de hoje, uma
ressalva de contrato que deve ser lembrada antes de tratá-la como um número absoluto e
definitivo. Maior convicção: bull-farelo moderado (mantido de sexta, sem informação nova para
mudar). Confiança reduzida para **neutro** em soja: o fechamento de sexta foi o primeiro
negativo da semana, os fundos já vinham reduzindo convicção no COT de 15/09, e não há pregão
novo que confirme ou desminta a continuidade do rali antes de segunda-feira. Bear-óleo mantido
em moderado, mas com o contra-argumento fundamentalista (margem de biodiesel) ligeiramente mais
forte do que se pensava ontem.

## Soja

**Viés: neutro, com viés residual de alta — o fechamento de sexta-feira foi o segundo dado
seguido (depois do doji de quinta e da própria queda de sexta) que pede cautela, e o fim de
semana não traz nenhuma informação nova capaz de resolver essa dúvida antes da reabertura de
segunda-feira.**

O que sustenta a tese (lado altista):

- **A soja segue acima da resistência de referência de 1.180,00** (fila
  `alerta-quebra_resistencia-soja_cbot-2026-09-18`: fechamento 1.303,50 vs. nível 1.180,00),
  uma folga de **+10,47%** — ainda uma distância confortável do nível de invalidação formal da
  tese, mesmo depois de dois dias sem fechamento em alta.
- **A curva futura permanece em contango regular**: nov/26 (base) 1.303,50 → jan/27 1.320,00
  → mar/27 1.329,50 → mai/27 1.336,50 → jul/27 1.340,50 (CME CBOT, 18/09) — incrementos de
  +16,50 → +9,50 → +7,00 → +4,00 pontos entre vencimentos consecutivos, sem sinal de que o
  mercado a termo esteja precificando a queda de sexta como um repricing estrutural. Isso
  importa porque, se o mercado esperasse uma reversão de tendência mais profunda, seria comum
  ver o contango se esticar (contratos distantes caindo menos, relativamente, que o próximo) —
  isso não ocorreu.
- **A condição da lavoura americana segue estável**, sem novo corte nesta janela. USDA Crop
  Progress, corte de 13/09: 12% excelente + 46% boa (G/E 58%, inalterado desde 30/08) e **6%
  da safra 2025/26 colhida**. O próximo corte semanal do USDA é esperado na tarde de
  **segunda-feira, 21/09** (horário americano) — o mesmo dia em que Chicago reabre, o que pode
  produzir uma combinação de dois catalisadores no mesmo pregão.
- **O câmbio segue levemente desfavorável ao vendido em reais**: USD/BRL fechou em **5,1575**
  (BCB PTAX, 18/09), a maior cotação da semana, uma alta de +0,10% frente aos 5,1521 de 17/09.
  Com a soja em dólar caindo -1,23% no mesmo dia, a paridade brasileira (CBOT × câmbio, sem
  basis) recuou -1,13%, de R$149,90 para **R$148,21/saca** (indicators, 18/09) — o câmbio
  absorveu cerca de um décimo da queda em dólar, um amortecedor parcial e recorrente que já
  apareceu em leituras anteriores.
- **A previsão climática de hoje (20/09) traz uma leitura mais morna do que a de ontem no
  Sul**: Cascavel/PR sobe de 22°C/16°C (previsão de ontem para 19/09) para **31°C/18°C**
  hoje, sem qualquer menção ao risco de granizo que constava na previsão anterior — o que pode
  indicar tanto que o sistema convectivo mais intenso já passou quanto que a previsão apenas
  mudou de leitura entre gerações (o boletim é uma previsão, não uma medição confirmada, ver
  Honestidade). Passo Fundo/RS segue sem menção a geada, com a mínima subindo pela segunda vez
  seguida (8°C → 14°C → **17°C**), o que remove qualquer risco de frio tardio do radar por
  ora. No núcleo produtor de Mato Grosso, o padrão de calor extremo (40-41°C) com chuva
  isolada persiste praticamente sem mudança em Cuiabá, Sinop, Sorriso e Lucas do Rio Verde —
  uma combinação que, como já discutido em leituras anteriores, tende a favorecer a germinação
  da safra 2026/27 em plantio, desde que a chuva isolada realmente se converta em precipitação
  e não fique só no boletim.

**O que invalida / risco:**

- **A soja fechou em queda pela segunda sessão seguida na prática** (o doji de quinta seguido
  da queda real de sexta), o primeiro par de sessões desfavoráveis desde a reabertura de
  11/09. Usando a série de fechamentos gravados na fórmula dos indicadores (mais confiável que
  a tabela `cme_cbot`, que tem lacunas nesta janela — ver Honestidade): 1.304,25 (14/09) →
  1.318,75 (+1,11%) → 1.320,50 (+0,13%) → 1.319,75 (-0,06%) → **1.303,50 (-1,23%)** — uma
  desaceleração clara de momentum ao longo da semana, culminando na primeira queda percentual
  relevante.
- **O COT de 15/09 (`release-cftc_cot-2026-09-15`), ainda o mais recente disponível cinco
  dias depois, já mostrava os fundos reduzindo net long em soja em -6,13%** (de 257.258 para
  241.501 contratos), com long caindo -3,63% e short subindo +14,25% — uma combinação de
  realização de lucro e posicionamento vendido novo que antecede e ajuda a explicar a queda de
  sexta-feira. O próximo corte (posições de 22/09, esperado por volta de 25-26/09) é o
  primeiro capaz de dizer se esse movimento se acentuou durante a queda desta semana.
- **Nível técnico a vigiar:** um fechamento de volta abaixo de 1.180 desfaria formalmente o
  rompimento; com a folga ainda em +10,47%, esse cenário segue distante.
- **Nenhuma linha nova de WASDE para soja em grão ou balanço mundial nesta janela** — a tabela
  de 11/09 ainda só traz farelo, o que deixa a leitura de oferta/demanda mundial de soja sem
  atualização própria há mais de uma semana.

**Leitura operacional:** com o mercado fechado até segunda-feira, não há ação de preço nova
para reagir — mas a combinação de dois fechamentos desfavoráveis seguidos com o COT já
mostrando fundos mais cautelosos antes da queda é o conjunto de evidências mais fraco para o
lado comprado desde a reabertura de 11/09. Para quem está comprado, este é um bom momento
para revisar o dimensionamento da posição e definir de antemão o comportamento diante de dois
cenários de abertura de segunda-feira: um gap de continuação da queda (reforça a cautela, sem
ainda quebrar 1.180) ou um gap de recuperação (devolveria parte da confiança perdida). Para
quem opera vendido, a mínima de sexta (1.300,00) e a máxima de sexta (1.322,00) são as
referências naturais de entrada/stop para uma operação tática de reversão de curto prazo, mas
sem quebra de 1.180 a tese estrutural de alta segue tecnicamente intacta.

## Farelo

**Viés: bull, moderado (mantido de sexta-feira, sem informação nova de fim de semana que
justifique mudança) — com uma ressalva de comparabilidade nova e relevante sobre o próprio
ratio Far/Soj que sustenta a tese, decorrente da rolagem de contrato explicada na Visão
geral.**

O que sustenta a tese:

- **O ratio Far/Soj fechou em 82,53% em 18/09** (indicators, já sobre o contrato de referência
  de dezembro/26) — dentro da zona "neutra" (80% a 87%), acima do limiar de 80% pela sétima
  sessão seguida desde a reabertura de 11/09, e ainda acima do nível de abertura da tese
  baixista original de 11/06/2026 (81,4%, [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]]),
  uma folga de **+1,13 pontos percentuais**. O veredito de invalidação técnica dessa tese,
  fechado em [[2026-09-17_ratio-far-soj-supera-nivel-de-abertura-da-tese-original-quarta-sessao]],
  segue de pé — mas com uma ressalva que não existia até ontem: o nível de abertura de 81,4%
  foi calculado sobre o contrato de julho/2026 (front em junho), enquanto o ratio de hoje usa
  o contrato de dezembro/2026 — dois rolagens de contrato depois. Como a curva de farelo está
  normalmente em contango (contratos mais distantes cotando mais caro), uma parte do "avanço"
  do ratio ao longo dos últimos três meses pode refletir esse efeito mecânico de rolagem, não
  apenas aperto real de oferta e demanda. Isso não desfaz o veredito — a direção (o ratio subiu
  de forma consistente desde 11/09, atravessando três zonas de classificação) é real e vem
  acompanhada de fundamentos coerentes (crush margin em queda, ABIOVE mostrando esvaziamento
  sazonal de oferta) — mas recomenda tratar a comparação numérica ponto a ponto contra 81,4%
  com mais cautela do que as leituras anteriores trataram.
- **O farelo segue acima da resistência histórica de 325,00** (fila
  `alerta-quebra_resistencia-farelo_cbot-2026-09-18`: 358,60 vs. 325,00), uma folga de
  **+10,34%** — mas aqui também vale o mesmo alerta: o nível de 325,00 provavelmente foi
  calibrado sobre um contrato de vencimento mais próximo do que o dezembro/26 atual, então
  parte dessa folga reflete o mesmo efeito de rolagem, não apenas a alta de preço em si.
- **A queda de sexta-feira, de -3,42% (371,30 → 358,60), é uma comparação válida "maçã com
  maçã"** — ambos os dias, 17 e 18/09, usam o mesmo ticker de dezembro/26 no dump de hoje —, o
  que a torna a leitura de curto prazo mais confiável desta seção: o farelo efetivamente caiu
  de forma expressiva na última sessão disponível, ecoando (em outro nível de contrato) a
  mesma correção que a leitura de 19/09 já havia descrito usando os números do contrato de
  outubro (-3,80%, de 368,70 para 354,70). As duas séries, apesar de basear-se em contratos
  diferentes, contam a mesma história qualitativa: uma correção real e de magnitude semelhante
  na sessão de sexta-feira.
- **A trajetória sazonal da ABIOVE para o Brasil continua apontando para alívio de oferta
  doméstica de farelo, sem revisão nesta janela**: produção projetada caindo de 2.143 mil t
  (out/26) para 1.978 (nov/26) e 1.659 mil t (dez/26); exportação de 850 para 800 e 700 mil t
  no mesmo período — o pano de fundo estrutural de médio prazo não muda com o fim de semana.
- **O COT de 15/09 (pré-reversão) mostrou os fundos ampliando net long em farelo em
  +16,12%** (de 157.689 para 183.111 contratos) — a maior variação percentual de net long de
  toda a série de COT disponível até aqui, ainda o dado mais recente de posicionamento cinco
  dias depois. O próximo corte (posições de 22/09) é o primeiro capaz de dizer se os mesmos
  fundos realizaram lucro com a correção de sexta.
- **A curva futura mantém a mesma inclinação achatada de curto prazo**: out/26 354,60 →
  dez/26 (base) 358,60 (+1,13%) → jan/27 360,40 (+0,50%) → mar/27 361,70 (+0,36%) → mai/27
  362,30 (+0,17%) — contango regular, incrementos decrescentes, sem sinal de reprecificação
  estrutural da queda de sexta.

**O que invalida / risco:**

- **A rolagem de contrato explicada acima é, em si, um risco de leitura, não de mercado**: até
  que o gráfico de dezembro/26 acumule um histórico próprio mais longo dentro desta série, é
  prudente não tratar comparações absolutas de nível (contra 325,00 ou contra 81,4%) com a
  mesma confiança que se tinha quando o contrato de referência era estável há semanas.
- **A queda de -3,42% de sexta-feira, mesmo numa base de contrato consistente, é a maior
  queda percentual de todo o histórico recente do ratio e do preço absoluto do farelo em
  qualquer contrato observado nesta série** — o tipo de movimento que normalmente pede pelo
  menos uma sessão de confirmação antes de se assumir retomada da alta.
- **O volume de farelo de 17/09 e 18/09 é, dígito a dígito, o mesmo número (141.412
  contratos) no dump de hoje** — estatisticamente improvável para duas sessões distintas de um
  contrato líquido como o farelo CBOT, e um sinal de que o dado de volume nesta janela de
  transição de contrato pode não ser confiável (ver Honestidade). Isso não muda a leitura de
  preço, mas reduz a confiança em qualquer inferência baseada em volume para essas duas datas
  específicas.
- **Os índices sintéticos ISF e ISO seguem travados em 60/100 e 80/100**, agora nove dias
  corridos sem qualquer mudança desde 11/09.
- **O físico brasileiro segue completamente congelado — agora onze dias corridos.** Última
  leitura ainda 09/09 (farelo MT/IMEA R$1.875,45/ton; prêmio export Paranaguá +0,12 USD/short
  ton, congelado desde 27/08, já 24 dias corridos).

**Leitura operacional:** sem pregão novo até segunda-feira, a postura recomendada é a mesma
definida na leitura de sexta: para quem está comprado em farelo (ou no spread Far/Soj
comprado), a extensão já alcançada e a magnitude da correção de sexta pedem cautela e
dimensionamento reduzido, não reforço de posição, até uma segunda sessão confirmar a
continuidade da tese. Para quem está vendido, a correção de sexta é uma janela tática, mas com
o mesmo aviso de sempre: o nível estrutural do ratio (ainda >80%, ainda tecnicamente acima da
zona de abertura da tese de junho, ainda que com a ressalva de comparabilidade de contrato) e o
calendário sazonal da ABIOVE não mudaram — uma entrada vendida aqui é mais defensável como
operação tática do que como aposta de que a tese de fundo esteja invalidada.

## Óleo

**Viés: bear, moderado — mantido, mas com o principal contra-argumento fundamentalista
(margem de biodiesel americana) revisto de "caindo" para "estável, levemente em alta" depois
da quarta correção do heating oil, o que reduz ligeiramente a força da tese em relação à
leitura de ontem.**

O que sustenta a tese (preço e estrutura de crush):

- **Óleo fechou em 68,22 USD cts/lb em 18/09** (já sobre o contrato de dezembro/26, ver Visão
  geral), uma queda de -1,34% frente aos 69,15 usados na fórmula de indicadores para 17/09. A
  fila confirma a permanência abaixo do suporte de referência de 72,00
  (`alerta-quebra_suporte-oleo_cbot-2026-09-18`), com a distância em **-5,25%** — como o nível
  de 72,00 provavelmente foi calibrado num contrato de vencimento diferente do atual, essa
  distância percentual também carrega a mesma ressalva de comparabilidade discutida na seção
  Farelo, mas a direção (abaixo do suporte) é inequívoca de qualquer forma.
- **O padrão intradiário de sexta-feira, no contrato de dezembro (ZLZ26)**: abertura 69,17,
  máxima do dia 69,20 (praticamente a própria abertura, uma extensão de apenas +0,04%), mínima
  68,01, fechamento 68,22 — o mercado abriu perto do topo e devolveu a maior parte do ganho ao
  longo do pregão, ecoando (embora em outro contrato) o padrão "abre na máxima, vende o dia
  inteiro" que as leituras de 17, 18 e 19/09 já haviam identificado como assinatura de pressão
  vendedora persistente no contrato de outubro.
- **O ISO (Índice de Suporte do Óleo) segue em 80/100**, sem recuperação nem novo recuo desde
  10/09 — os índices compostos continuam sem sinalizar qualquer mudança de regime.
- **Usando a série de fechamentos embutida nas fórmulas de indicadores (mais confiável que a
  tabela `cme_cbot` nesta janela, que não tem linha de óleo para 17/09)**: 70,19 (14/09) →
  70,35 (+0,23%) → 69,67 (-0,97%) → 69,15 (-0,75%) → **68,22 (-1,34%)** — uma trajetória de
  queda que se acelera ao longo da semana, com quatro das últimas quatro variações diárias
  sendo negativas ou marginais.

**O que sustenta um piso parcial para a tese — e por que a correção de hoje reduz um pouco a
força do argumento contrário:**

- **A margem de biodiesel americana NÃO caiu em 18/09 como a leitura de ontem descreveu — ela
  subiu ligeiramente.** O heating oil (HO=F) de 18/09, usado ontem como US$4,8367/galão
  (implicando margem de US$2,1332/galão, uma "queda adicional de -8,36%"), aparece hoje
  revisado para **US$5,0578/galão** (+4,57%) — a quarta ocorrência documentada do mesmo padrão
  estrutural (11/09: +3,77%; 16/09: +5,65%; 17/09: +5,91%; agora 18/09: +4,57%). Com o valor
  revisado, a margem de biodiesel de 18/09 foi **US$2,3063/galão** — uma alta de +0,59% sobre
  os US$2,2927 de 17/09, não uma queda. O mecanismo: o custo do óleo caiu -1,35% (acompanhando
  a queda do próprio óleo em Chicago), uma queda de custo ligeiramente maior do que a queda de
  receita do heating oil revisado (-1,10%, de 5,1139 para 5,0578), então a margem — que é
  receita menos custo — se sustentou. Este é um contra-argumento fundamentalista que fica
  ligeiramente mais forte do que a leitura de ontem indicava, ainda que continue distante dos
  recordes revisados de 15-16/09 (US$2,35 e US$2,39/galão).
- **Ainda assim, o volume do HO=F de 17/09 e 18/09 é, dígito a dígito, idêntico (45.315
  contratos)** no dump de hoje — o mesmo tipo de anomalia observada no volume do farelo (ver
  Farelo e Honestidade), o que reduz a confiança na precisão desse dado específico mesmo
  depois de "normalizado" nas últimas leituras. A recomendação prática seguida desde
  [[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]] permanece: tratar o fechamento
  de HO=F do dia mais recente do dump sempre como provisório até a geração seguinte confirmar
  o valor — e agora, adicionalmente, desconfiar de qualquer leitura de volume do HO=F ou do
  farelo em datas adjacentes quando os números aparecerem repetidos.
- **A curva futura de médio prazo segue em contango regular**: out/26 67,70 → dez/26 (base)
  68,22 (+0,77%) → jan/27 68,52 (+0,44%) → mar/27 68,69 (+0,25%) → mai/27 68,75 (+0,09%) —
  incrementos decrescentes, sem sinal de reprecificação estrutural.
- **O RIN D4 (crédito de biocombustível renovável americano) continua constante na fórmula
  interna** — toda a variação da margem de biodiesel nesta janela vem de heating oil e do
  próprio óleo, não de qualquer mudança real no valor do crédito RIN.

**Leitura operacional:** com o mercado fechado até segunda-feira, o quadro técnico (fechamento
abaixo do suporte de 72,00, padrão intradiário vendedor, ISO travado em 80) segue favorável ao
lado vendido direcional, mas a correção da margem de biodiesel (de "caindo" para "estável")
tira um pouco de força do argumento de que o óleo está fundamentalmente mais fraco a cada dia
— o contra-argumento não desapareceu, apenas ficou menos dramático do que parecia ontem. Para
quem está vendido, a máxima de sexta-feira (69,20, no contrato de dezembro) é a referência
natural de stop; para quem está comprado, aguardar uma quebra clara do padrão vendedor (por
exemplo, um fechamento de segunda-feira acima da abertura do dia) antes de considerar reforçar
posição segue sendo a leitura mais defensável. Para quem opera o spread farelo-óleo dentro do
crush, o oil-meal spread fechou em -0,385 USD/bushel em 18/09 (indicators), mais negativo que
os -0,3696 usados na leitura de ontem sob a base antiga — outra métrica que carrega a mesma
ressalva de rolagem de contrato, então comparações de nível absoluto dessa métrica ao longo do
tempo devem ser lidas com a mesma cautela.

## Spreads e crush (leitura de complexo)

A rolagem de contrato em farelo e óleo (explicada na Visão geral) afeta diretamente todas as
métricas de complexo que combinam os três produtos — crush margin, ratio Far/Soj, oil share e
oil-meal spread —, porque farelo e óleo agora vêm do contrato de dezembro/26 enquanto a soja
continua no de novembro/26. Isso não invalida essas métricas (elas continuam sendo calculadas
de forma consistente dentro de um mesmo dia, o que é o que importa para a leitura de "quem
manda no crush hoje"), mas significa que comparações de nível absoluto contra dias anteriores à
rolagem (antes de 19/09) carregam uma margem de erro adicional que não existia quando o
contrato de referência era estável.

Dentro da janela mais recente, usando a série de fechamentos gravada nas fórmulas de
indicadores (14 a 18/09, já a série mais internamente consistente disponível): o ratio Far/Soj
percorreu 81,93% → 83,12% → 83,06% → 84,40% → **82,53%**, uma trajetória de aperto seguida de
uma correção real na última sessão — mas TODA essa série já inclui, nos seus dois últimos
pontos, o efeito da rolagem que hoje ficou visível na tabela bruta de preços. O oil share
percorreu 49,05% → 48,79% → 48,22% → **48,75%**, subindo na última sessão porque o farelo caiu
proporcionalmente mais que o óleo (-3,42% vs. -1,34%) — o mesmo mecanismo de "quem lidera o
movimento do dia domina essas métricas" já descrito em leituras anteriores. O oil-meal spread
percorreu -0,1155 → -0,3003 → -0,3795 → -0,5621 → **-0,385** USD/bushel, comprimindo (menos
negativo) pelo mesmo motivo.

O crush margin fechou em **US$2,3584/bushel** em 18/09, uma queda de -8,51% frente aos
US$2,5776 de 17/09 — a distância abaixo do piso de referência de US$2,50 monitorado pela fila
(`alerta-quebra_suporte-complexo_soja-2026-09-18`) ficou em -5,66%. O mecanismo: farelo caindo
-3,42% sozinho foi suficiente para superar a queda simultânea, porém menor, do óleo (-1,34%) e
da soja (-1,23%) — a esmagadora ficou, na margem, menos remunerada nesta sessão do que na
anterior, ainda que dentro de uma faixa (US$2,35-2,60/bushel) que se repete há duas semanas
sem uma tendência direcional clara de médio prazo.

Os dois índices compostos por contagem de condições — ISF (60/100) e ISO (80/100) —
permanecem travados no mesmo patamar desde 11/09, agora o nono dia corrido sem qualquer
mudança, apesar de o ratio e o crush margin terem oscilado de forma expressiva nesse mesmo
período — o contraponto de sempre nesta série: os limiares desses índices específicos não
reagem a oscilações de curto prazo.

O COT de 15/09 (`release-cftc_cot-2026-09-15`), ainda o dado de posicionamento mais recente
cinco dias depois, retrata os fundos ampliando net long em farelo (+16,12%) e óleo (+10,65%) e
reduzindo em soja (-6,13%) — um instantâneo de terça-feira que precede a correção de sexta e
estabelece a base de comparação para o próximo corte (posições de 22/09, esperado por volta de
25-26/09), o primeiro capaz de dizer se os mesmos fundos já começaram a realizar lucro. Do
lado dos fundamentos brasileiros de médio prazo (ABIOVE, sem revisão nesta janela), o balanço
projetado continua mostrando o esvaziamento sazonal esperado de oferta de farelo entre outubro
e dezembro/26 — uma trajetória que segue apoiando um ratio estruturalmente mais alto no médio
prazo, independentemente da rolagem de contrato ou da correção de curto prazo de sexta-feira.

## Lente fiscal/regulatória BR

Antes de fechar qualquer tese de preço BR, os vetores tributários/regulatórios vivos que pesam
no complexo — todos do `system/tributario_watch.toml`, cujo carimbo mais recente
(`atualizado_em`) em todos os 10 eventos catalogados é 2026-06-05, ou seja, **107 dias
corridos sem revisão humana** frente a hoje (20/09):

- **MP 1.363/2026** (id `MP-1363-2026`, subvenção diesel fóssil R$1,12/L, vigente até
  31/12/2026): barateia o diesel fóssil no mix B15 (mistura obrigatória de 15% de biodiesel),
  reduzindo a competitividade relativa do biodiesel e a demanda doméstica por óleo de soja —
  vetor estrutural de baixa para óleo, sem mudança de status, plenamente vigente.
- **B16 (id `B16-CNPE-2026`, elevação da mistura obrigatória de biodiesel para 16%)** segue
  "adiado", resultado esperado por volta de novembro/2026. Upside represado (~436 mil
  toneladas de demanda potencial adicional de óleo), não corrente.
- **Isenção de PIS/Cofins do biodiesel na mistura** (id `PISCOFINS-BIODIESEL-ISENCAO`):
  vigência registrada até 31/07/2026 — já **51 dias corridos vencida** frente a 20/09/2026,
  sem registro de prorrogação ou expiração.
- **MP 1.358/2026** (subvenção gasolina R$0,89/L): vigência registrada até 11/07/2026, agora
  **71 dias corridos vencida**.
- **STJ REsp 2.165.276** (id `STJ-RESP-2165276`, crédito de PIS/Cofins sobre soja em
  biodiesel, direção "alta" para soja/óleo): sem novidade nesta janela.
- **EPA RFS 2026/2027** (id `EPA-RFS-2026-2027`, mandato de biocombustível americano, direção
  "alta" para óleo): sustenta o RIN D4, estável, e o RIN permanece constante na fórmula
  interna de margem de biodiesel usada por este sistema.
- **Crédito 45Z** (id `45Z-CLEAN-FUEL`, em tramitação, direção "mista"): sem novidade.
- **Indonésia — Danantara** (id `DANANTARA-INDONESIA`) e **levy de exportação PMK 9/2026**
  (id `INDONESIA-LEVY-PMK9`): a assunção plena da centralização da exportação de palma pela
  Indonésia tinha alvo 01/09/2026 — já se passaram **19 dias** sem confirmação. Catalisador de
  alta represado para óleo (via substituição com palma) — sem dado de MPOB disponível para
  monitorar diretamente (parser continua quebrado, ver Honestidade).
- **Indonésia B50** (id `INDONESIA-B50`, monitorando, direção "alta"): sem novidade.

Nenhum desses vetores muda a leitura de preço de hoje isoladamente — mas, em conjunto, eles
reforçam a mesma assimetria já descrita em leituras anteriores: o mercado interno brasileiro
tem múltiplos desincentivos correntes ao óleo (MP 1.363 plenamente vigente, isenção PIS/Cofins
já 51 dias vencida sem sinal de renovação) e múltiplos catalisadores de alta represados, não
correntes (B16, Danantara, B50). O óleo brasileiro segue mais fraco estruturalmente até que
algum dos vetores represados vire fato concreto — uma leitura que é independente tanto da
rolagem de contrato quanto da correção de margem de biodiesel discutidas acima, e que continua
válida com o fim de semana.

## Riscos e eventos próximos

- **Reabertura de Chicago amanhã, segunda-feira, 21/09** — o primeiro pregão desde a queda
  de sexta em todas as três pernas. Um segundo dia seguido de queda seria o primeiro sinal
  técnico de que a correção é o início de algo mais persistente; uma recuperação devolveria
  parte da confiança perdida em soja e reforçaria a tese em farelo.
- **USDA Crop Progress semanal**: próximo corte esperado na tarde de segunda-feira, 21/09
  (horário americano) — cai no mesmo dia da reabertura, o que pode produzir dois catalisadores
  simultâneos no primeiro pregão da semana.
- **Próximo corte de COT (posições de 22/09), esperado por volta de 25-26/09.** Será o
  primeiro capaz de confirmar se os fundos que ampliaram net long em farelo e óleo (COT de
  15/09) já realizaram lucro com a correção de sexta, e se a redução de net long em soja se
  acentuou.
- **Nível técnico a vigiar em farelo:** volta abaixo de 325,00 desfaria o rompimento — mas
  esse nível, calibrado antes da rolagem de contrato, deve ser reavaliado com cautela nas
  próximas leituras (ver ressalva na seção Farelo).
- **Nível técnico a vigiar em soja:** volta abaixo de 1.180,00 desfaria o rompimento (folga
  atual +10,47%).
- **Reação (ou ausência) do físico brasileiro de farelo e óleo**, congelado desde 09/09 (onze
  dias) e 27/08 (prêmios export, 24 dias) — a rolagem de contrato e a correção do heating oil
  ainda não têm qualquer contrapartida observável no mercado físico doméstico.
- **USDA WASDE**: a tabela de setembro (11/09) ainda só traz farelo — monitorar se as tabelas
  de soja em grão e óleo aparecem em atualização posterior, ou apenas na edição de outubro.
- **NOPA mensal**: mais um "release" sem dado novo de fato (paywall), agora referenciado como
  `release-nopa-2026-09-19`.
- **Confirmação da centralização plena da exportação de palma pela Danantara** — alvo 01/09,
  já 19 dias passados sem confirmação.
- **Vigência da isenção PIS/Cofins do biodiesel** (51 dias vencida) e **MP 1.358/2026 da
  gasolina** (71 dias vencida) — checar notícia de renovação/expiração.
- **Estabilidade do contrato de dezembro/26 (Z26) como novo front de farelo e óleo** —
  monitorar se o dump de amanhã mantém a mesma rolagem (o que seria o esperado e confirmaria
  que a mudança é estrutural, não um evento isolado) e se os valores de 17-18/09 permanecem
  estáveis nas próximas gerações (ou sofrem nova revisão, como o HO=F já fez quatro vezes).
- **Marco de 107 dias sem revisão humana do `tributario_watch.toml`** — pelo menos dois
  vetores (isenção PIS/Cofins biodiesel, MP 1.358/2026) já vencidos sem registro de renovação.
- **Duplicação de volume em farelo (141.412 contratos em 17 e 18/09) e heating oil (45.315
  contratos em 17 e 18/09)** — monitorar se esse padrão se repete na próxima geração; se
  persistir, é evidência mais forte de um problema sistemático na captura de volume durante
  transições de contrato, não uma coincidência isolada.

## Honestidade

- **Hoje, 2026-09-20, é domingo — não há pregão novo em Chicago desde sexta-feira, 18/09.**
  Esta leitura não descreve "o que aconteceu hoje no mercado" porque nada aconteceu no mercado
  hoje; ela consolida o fechamento de sexta à luz de duas informações novas de qualidade de
  dado (a rolagem de contrato e a quarta revisão do HO=F) e prepara o terreno para a reabertura
  de amanhã. O cabeçalho do dump usado por este sistema ainda está rotulado "Briefing
  consolidado — 2026-09-19", um dia atrás da data desta leitura — o mesmo padrão de defasagem
  de um dia observado em todas as leituras anteriores desta série, agora combinado com o fato
  de que sábado e domingo não geram pregão.
- **A rolagem de contrato de farelo e óleo (de outubro/26 para dezembro/26) foi verificada
  diretamente no código-fonte** (`system/sources/cme_cbot.py`, função `_front_contract`,
  `ROLL_DIAS = 12`), não apenas inferida a partir dos números — essa é uma leitura de alta
  confiança. O que segue sendo incerto é o efeito acumulado dessa e de rolagens anteriores
  (de julho para outubro, por exemplo) sobre a comparabilidade de longo prazo de níveis como o
  ratio de abertura da tese de junho (81,4%) e a resistência de 325,00 em farelo — não há, no
  briefing, um registro de quando essas rolagens anteriores ocorreram, então não é possível
  quantificar com precisão quanto do "avanço" de meses do ratio é rolagem de contrato e quanto
  é aperto real de oferta e demanda. Esta leitura optou por manter o veredito qualitativo já
  fechado ([[2026-09-17_ratio-far-soj-supera-nivel-de-abertura-da-tese-original-quarta-sessao]])
  em vez de reabri-lo, mas registra a ressalva para as próximas leituras considerarem.
- **A seção `cme_cbot` do dump de hoje está incompleta para 17/09**: só farelo e heating oil
  têm uma linha registrada para essa data; soja e óleo não têm nenhuma linha de 17/09 na tabela
  bruta de preços. Para não inventar um número, esta leitura usou os valores de soja e óleo de
  17/09 gravados dentro das fórmulas da seção `indicators` (que cita explicitamente "soja
  1319,75" e "óleo 69,15" na descrição do cálculo de crush margin e ratio daquele dia) como a
  fonte mais confiável disponível — mas não é possível confirmar de forma independente, via a
  tabela bruta, se esses valores já refletem o contrato de dezembro ou ainda o de outubro.
- **O volume de farelo (141.412 contratos) e de heating oil (45.315 contratos) aparece
  idêntico, dígito a dígito, entre as linhas de 17/09 e 18/09 no dump de hoje.** Isso é
  estatisticamente muito improvável para duas sessões distintas de contratos líquidos como
  esses, e mais provável de ser um artefato da transição de contrato (por exemplo, a mesma
  resposta de consulta sendo reaproveitada para rotular duas datas) do que um fato de mercado.
  Esta leitura trata os números de preço dessas duas datas como válidos (eles diferem entre si
  de forma coerente com o padrão de correção observado), mas trata os números de volume dessas
  duas datas especificamente como não confiáveis.
- **Quarta ocorrência confirmada do padrão de revisão do heating oil (HO=F)**: 18/09 revisado
  de US$4,8367 para US$5,0578 (+4,57%), na mesma faixa das três ocorrências anteriores
  documentadas em [[2026-09-19_ho-f-padrao-estrutural-de-revisao-confirmado]]. Como já
  recomendado naquele insight, o fechamento de HO=F do dia mais recente do dump deve continuar
  sendo tratado como provisório — e o valor de hoje para 18/09 (5,0578) também deve ser tratado
  como potencialmente sujeito a nova revisão na próxima geração.
- **O corte de COT `release-cftc_cot-2026-09-15` segue sendo o dado de posicionamento mais
  recente**, agora cinco dias corridos depois do corte e a três dias da correção de sexta-feira
  — não há como confirmar se os fundos que ampliaram farelo/óleo e reduziram soja mantiveram
  essa postura durante a semana. O próximo corte (22/09, esperado 25-26/09) resolve essa
  lacuna.
- **Percentil histórico de posicionamento COT não está disponível no briefing** — toda leitura
  de "fundos comprando/vendendo" nesta série usa variação absoluta semana a semana de
  contratos, não percentil histórico.
- **O item de fila `release-nopa-2026-09-19` é mais uma repetição sem dado novo** — o mesmo
  padrão de todas as leituras anteriores desde que este monitoramento começou (paywall,
  `monthly_status` em 0,0 bool).
- **`tributario_watch.toml` sem atualização há 107 dias corridos** — pelo menos dois vetores
  (isenção PIS/Cofins do biodiesel, MP 1.358/2026) já passaram da vigência registrada sem nota
  de renovação ou expiração.
- **A ausência de itens de notícia com qualquer conteúdo chega a dez dias corridos
  consecutivos (10 a 19/09)**, sem visibilidade ainda sobre a coleta de 20/09 nesta janela do
  dump — registrado como falha ou pausa de coleta da fonte RSS, não como ausência real de
  notícia relevante no mercado.
- **A previsão INMET para 20/09 é previsão meteorológica, não medição de precipitação ou
  temperatura real** — as menções a "chuva", "chuva isolada" e "nublado" são indicativas do
  boletim, não confirmação de que ocorreram efetivamente. A ausência de menção a granizo em
  Cascavel/PR hoje, depois de ter aparecido na previsão de ontem para o mesmo local, também não
  é confirmação de que o evento não ocorreu — apenas que o boletim de hoje não o repete.
- **Prêmios de exportação (Paranaguá) e o físico de farelo/soja BR seguem sem atualização
  própria desde 09/09** (onze dias corridos) — não é possível afirmar se isso reflete mercado
  físico genuinamente parado ou apenas defasagem normal de publicação da fonte NAG.
- **MPOB (palma Malásia) segue com parser quebrado** — nenhum dado de produção/estoque de
  palma malaia disponível, o que impede monitorar diretamente o catalisador represado da
  centralização de exportação indonésia (Danantara).
- **BCBA (Argentina) segue sem links de relatório detectados** — nenhum dado de safra ou
  exportação argentina disponível além do que já vem consolidado pelo WASDE.
- **Os forecasts estatísticos internos (bandas 7d/30d) foram gerados em 19/09 sobre o
  fechamento de 18/09** (já incorporando os valores de farelo/óleo pós-rolagem) — o viés
  "altista" nos três produtos reflete extrapolação estatística de tendência (MA20 +
  volatilidade + slope), não uma reavaliação fundamentalista; esta leitura mantém farelo em
  bull, soja rebaixada para neutro e óleo em bear a partir da análise qualitativa, não das
  bandas estatísticas.
- **A fila de julgamento voltou a listar os dois itens de revisão do ratio Far/Soj (D+7 e
  D+90) como "vencidos"**, o mesmo eco de geração já documentado em leituras anteriores (09,
  12, 15, 16, 17, 18 e 19/09) — o sistema de fila não lê de volta os insights já publicados
  para marcar a revisão como encerrada. O veredito de invalidação técnica dado em
  [[2026-09-17_ratio-far-soj-supera-nivel-de-abertura-da-tese-original-quarta-sessao]] segue
  válido, com a ressalva de comparabilidade de contrato registrada nesta leitura. A revisão de
  D+180, programada para 08/12/2026 pela tese original, ainda não venceu.
