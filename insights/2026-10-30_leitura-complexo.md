---
data: 2026-10-30
titulo: "Sex 30/10: o complexo segue em deriva baixista fraca (soja 1.234,00, farelo 329,20, óleo 65,81) e o ratio Far/Soj encostou exatamente no piso de 80% (80,03%) — o oil share em 49,99% mostra óleo e farelo valendo o mesmo no crush, com o óleo preso ao diesel (heating oil 4,57) e o farelo com fundo super-lotado; confiança baixa porque o dump de 30/10 repete quase por inteiro as barras de 29/10 no farelo e no heating oil e porque os fechamentos de 29/10 foram reescritos de novo"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT via briefing 2026-10-30 — sessão **2026-10-30**. Soja ZSF27 jan/27 abertura 1.234,50 · máxima 1.236,75 · mínima 1.230,75 · fechamento **1.234,00** US¢/bu · volume 3.667 (curva X26 nov/26 1.222,00 · H27 1.242,50 · K27 1.252,25 · N27 1.259,50 · Q27 1.245,25). Farelo ZMZ26 dez/26 abertura 329,30 · máxima 330,10 · mínima 328,30 · fechamento **329,20** US$/sht · volume 1.528 (curva F27 329,50 · H27 330,70 · K27 334,00 · N27 338,20). Óleo ZLZ26 dez/26 abertura 65,66 · máxima 65,90 · mínima 65,64 · fechamento **65,81** US¢/lb · volume 1.709 (curva F27 66,04 · H27 66,47 · K27 66,77 · N27 66,84). Heating oil HO=F abertura 4,5800 · máxima 4,5919 · mínima 4,5700 · fechamento **4,5738** US$/galão · volume 491
  - CME CBOT via briefing — sessões 2026-10-29 (soja 1.234,50 · farelo 329,20 · óleo 65,69 · HO 4,5805), 2026-10-28 (soja 1.238,00 · farelo 335,70 · óleo 65,56 · HO 4,82), 2026-10-27 (soja 1.243,00 · farelo 334,60 · óleo 66,71 · HO 4,78) e 2026-10-26 (soja 1.252,50 · farelo 340,20 · óleo 67,01 · HO 4,91), conforme `indicators` do briefing de 30/10
  - Indicadores do robô (`indicators`, 2026-10-30 e anteriores) — crush margin, Far/Soj, oil share, spread óleo−farelo, margem de biodiesel EUA, índices de Sobra de Farelo e Suporte do Óleo, paridade BRL
  - BCB PTAX (sgs 1 e 21619) 2026-10-16 a **2026-10-29** (USD/BRL 5,3744 em 29/10; não há PTAX de 30/10)
  - CFTC COT (managed money) data-base **2026-10-20** — o relatório de 27/10 não está no dump
  - USDA Crop Progress 2026-10-25 (colheita de soja EUA 79%) e 2026-10-18 (64%)
  - ABIOVE projeções mensais nov/2026 e dez/2026 (esmagamento, produção, exportação, estoques)
  - INMET 2026-10-30 (previsão por praça), NOAA CPC 2026-10-30 (El Niño Advisory), MPOB 2026-10-30 (página lida, sem números extraídos), NOPA 2026-10-30 (sem número, paywall)
  - Forecasts estatísticos do robô gerados em 2026-10-30 (7d e 30d)
  - `system/tributario_watch.toml` (vetores registrados, `atualizado_em = 2026-06-05`)
status: ativa
vies: [bear-soja, bear-farelo, bear-oleo_soja]
---

## Visão geral

O complexo da soja é, na prática, **uma fábrica**: a indústria compra o grão (soja), esmaga e vende duas coisas — o **farelo** (a proteína, que vira ração) e o **óleo** (que vai para alimentação e, cada vez mais, para biodiesel). A margem dessa fábrica é o **crush margin** (margem de esmagamento): valor do farelo mais valor do óleo menos o custo da soja. Em 30/10, segundo os indicadores do robô, essa margem é de **US$ 2,14 por bushel** (CBOT, `indicators` 2026-10-30), um pouco abaixo dos US$ 2,33 de 26/10 e dos US$ 2,27 de 27/10. A margem encolhe porque o *produto* (farelo e óleo) cai mais do que o *insumo* (soja): em cinco pregões a soja perdeu 1,5% (1.252,50 → 1.234,00), o farelo perdeu 3,2% (340,20 → 329,20) e o óleo recuou 1,8% (67,01 → 65,81).

O número mais didático do dia é o **oil share** — a fatia do óleo no valor total que sai do esmagamento: **49,99%** (valor do óleo 7,24 de um total de 14,48 por bushel, `indicators` 2026-10-30). Isso significa que, em dinheiro, o óleo vale o mesmo que o farelo. É uma situação incomum para quem conhece o complexo "clássico", em que o farelo respondia pela maior parte da receita; hoje o óleo é puxado pela demanda de biocombustíveis e "paga" metade do crush. O reverso é que o **farelo virou a sobra**: como o esmagamento é movido pela margem total e o óleo carrega metade dela, a indústria processa soja mesmo com o farelo barato, e o excedente de proteína pressiona o preço do farelo. É isso que o índice de **Sobra de Farelo** (75 em 100, "3 de 4 condições", `indicators` 2026-10-30) tenta capturar.

O **ratio Far/Soj** compara o preço de uma tonelada de farelo com o da soja equivalente: 329,20 ÷ (1.234,00 × 33,33 ÷ 100) = **80,03%**. Abaixo de 80% o robô classifica o farelo como "abundante"; a partir de 87% como "apertado". Em linguagem simples: o farelo está custando só 80% do que custaria se valesse o mesmo que a soja que o originou — ele está **barato em relação ao grão**, no limite inferior da faixa. Isso é um ponto de atenção para os dois lados: quem opera short de farelo enfrenta um preço já comprimido (o risco passa a ser de retorno à média), e quem opera long enfrenta uma sobra estrutural que não some por decreto.

O que mudou hoje: (i) o ratio, que ontem a leitura descrevia como "afastado do piso" (81,54%), está agora em **80,03%** — mas isso é em grande parte **correção de dados**: o `indicators` reescreveu o fechamento de 29/10 do farelo de 335,40 para 329,20, e o ratio de 29/10 passou a 80,00%; (ii) o heating oil (diesel de aquecimento, o "primo" fóssil do biodiesel) continua no fundo da semana (4,5738, queda de 6,9% desde 4,91 em 26/10), segurando o óleo de soja; (iii) o dólar em R$ subiu para 5,3744 (PTAX 29/10), o que amortece em reais a queda do CBOT.

**Leitura de uma linha:** o pivô do complexo é o **diesel/heating oil, via óleo de soja**, a maior convicção é **baixista fraca no farelo** (sobra + fundos muito comprados), e a confiança do dia é **baixa**, porque o dump repete barras de ontem e há dados revisados e ausentes (WASDE e NOPA sem número; COT de 20/10).

## Soja

**Viés:** baixista **fraco** (de preço), confiança baixa.

**O que sustenta a tese**

*Nível e momentum.* A soja (ZSF27, jan/27) fechou em **1.234,00 US¢/bu** em 30/10, contra 1.268,50 em 23/10 (conforme leitura de ontem) e 1.252,50 em 26/10: queda de cerca de 2,7% em uma semana, em degraus pequenos (1.243,00 → 1.238,00 → 1.234,50 → 1.234,00). O movimento do dia é praticamente nulo (−0,50), o que combina com o volume baixo (3.667 contratos): a soja está andando de lado sobre o patamar de 1.234, sem comprador agressivo nem vendedor agressivo. A mínima do dia (1.230,75) ficou apenas 3 centavos abaixo do fechamento; sem fôlego para romper para baixo, sem fôlego para devolver.

*Curva a termo.* A curva é de **carregamento** (contango) até julho: nov/26 1.222,00 · jan/27 1.234,00 · mar/27 1.242,50 · mai/27 1.252,25 · jul/27 1.259,50 (CBOT, 2026-10-30), com agosto/27 recuando para 1.245,25. Um carry de ~37,5 US¢ entre nov e jul (3,1%) indica mercado **sem escassez imediata**: ninguém paga prêmio por soja disponível agora. O recuo de ago/27 abaixo de jul/27 insinua expectativa de safra nova mais folgada. Curva assim é coerente com viés baixista fraco — não com corrida de alta.

*Colheita nos EUA.* O USDA (Crop Progress) mostra **79% colhido em 25/10**, contra 64% em 18/10 — 15 pontos em uma semana. Colheita avançada elimina o principal prêmio de risco climático/de logística do hemisfério norte: o que estava no campo está virando oferta física. O briefing não traz a média de cinco anos nem o ritmo de exportação, então não consigo dizer se 79% é adiantado ou normal; só o fato de que a janela de risco de safra EUA está se fechando.

*Câmbio e paridade em reais.* O USD/BRL (PTAX) foi a **5,3744 em 29/10**, versus 5,0377 em 23/10 (BCB sgs 1). Com o câmbio mais alto, a paridade de exportação em reais é **R$ 146,21/saca de 60 kg** (CBOT 1.234,00 × 5,3744, sem basis, `indicators` 2026-10-30), contra R$ 140,9/saca no dia 23 pela mesma conta. Mecanismo: o produtor brasileiro e o exportador recebem em dólar; real mais fraco sobe o preço em reais e **estimula a venda**, o que adiciona oferta de soja brasileira ao mercado e limita o que o CBOT poderia subir; ao mesmo tempo protege o produtor BR de uma queda do CBOT. Em resumo, o dólar alto é um amortecedor para o preço interno, mas empurra a pressão de oferta para o exterior. **Ressalva forte:** a série PTAX do dump mostra saltos que parecem irreais (5,0377 em 23/10 → 5,5007 em 26/10, +9,2% num pregão útil, depois 5,3346 em 27/10; o EUR/BRL foi de 5,64 para 6,15 e de volta a 5,95) — veja Honestidade. Por isso trato o câmbio como **direção** (real mais fraco que na semana passada), não como número exato.

*Posicionamento dos fundos.* O COT (CFTC) mais recente do dump é de **20/10**: managed money em soja com **259.970 contratos comprados e 38.645 vendidos, net long de 221.325** (CFTC COT 2026-10-20), sobre open interest de 1.093.612 — os fundos detêm cerca de 24% do OI na ponta comprada. Posição grande e unilateral é combustível de queda: se o preço cede, o fundo que está comprado precisa vender para reduzir, e não há short grande para recomprar. O briefing não traz o **percentil** histórico dessa posição, e os dados têm 10 dias; então o que afirmo é que o net long é grande em termos absolutos, não que seja extremo na história.

*Margem de esmagamento e demanda.* O crush de US$ 2,14/bu ainda é positivo e robusto; a indústria tem incentivo para continuar moendo, o que sustenta a demanda pela soja. As projeções da ABIOVE para o Brasil trazem esmagamento de **2.626,6 mil t em novembro/2026 e 2.203,5 mil t em dezembro/2026**, com estoque final de soja de 3.659 mil t em nov e 1.890 mil t em dez (ABIOVE projeções mensais). Isso mostra a safra velha sendo consumida e a oferta doméstica se apertando no fim do ano calendário, o que é suporte sazonal — mas são *projeções*, não resultado, e não tenho o balanço US nem o WASDE de 28/10 em números.

**Fatores que não consigo medir hoje:** exportação para a China, ritmo de vendas dos EUA, prêmio de exportação em Paranaguá e basis nas praças físicas (o dump de hoje não traz seção de físico BR), safra Brasil/Argentina em número (só o clima).

*Clima na América do Sul.* O NOAA CPC mantém **El Niño Advisory** (`noaa_cpc`, 2026-10-30). Como regra geral de mercado (conhecimento geral, não vem do briefing), El Niño tende a favorecer chuva no Sul do Brasil e na Argentina e a trazer risco de irregularidade no Norte/Nordeste. O INMET de 30/10 prevê **pancadas de chuva isoladas** em Sorriso (máx. 35 °C), Sinop (34 °C), Lucas do Rio Verde e Cuiabá (33 °C), Rio Verde/GO (30 °C), Maringá (27 °C), Cascavel, Passo Fundo (24 °C). Chuva distribuída no Centro-Oeste na fase de semeadura/emergência é benigna; nada no dump indica estresse hídrico. Clima, portanto, **não** sustenta prêmio de risco hoje.

**O que INVALIDA / risco**

- Fechamento da soja **acima de ~1.252** (a máxima semanal de 26/10) com volume — recuperaria a tendência de queda da semana.
- Um WASDE (28/10) ou dado de exportação que reduza estoques finais: **não consigo avaliar** sem os números (fila `release-usda_wasde-2026-10-28`).
- Falha climática no Centro-Oeste do Brasil ou no sul argentino (o El Niño Advisory vira variável).
- Fundos: se o COT de 27/10 (publicado hoje, fora do dump) mostrar liquidação grande, o viés baixista ganha força; se mostrar aumento, o risco de *squeeze* de baixa aparece.
- Câmbio: BRL forte devolve pressão ao preço interno em reais.

**Leitura operacional**

*Long:* não há gatilho técnico nem fundamental claro; carregar long de soja contra uma curva em contango, colheita fechando e fundo comprado exige stop curto. *Short:* faz sentido tático, mas com alvos modestos — o forecast mecânico do robô (7d central 1.206,22, faixa 1.182,56–1.229,89; 30d central 1.105,98) é extrapolação estatística de MA20 + volatilidade + inclinação; o topo da banda de 7 dias (1.229,89) está *abaixo* do spot (1.234,00), sinal de que o modelo está só projetando a inclinação recente. Eu **não** adoto os −10% de 30d; um viés baixista fraco com alvo na região de 1.200–1.210 é mais defensável. O melhor uso da soja hoje é como **perna do crush** (veja Spreads).

*Fila tratada:* `alerta-quebra_resistencia-soja_cbot-2026-10-30` — a soja fechou em 1.234,00, acima do nível 1.180,00 do alerta. Esse nível é **antigo**: a soja está 4,6% acima dele há semanas; o alerta "confirma" que o preço está acima de um piso/resistência antigo, mas **não muda a tese** — o que importa é que o preço está recuando *dentro* de uma faixa acima de 1.180, sem romper nenhum suporte relevante. Sugiro recalibrar o nível (é tarefa da camada de calibração, não minha).

## Farelo

**Viés:** baixista **fraco-moderado**, confiança baixa.

**O que sustenta a tese**

*Nível e momentum.* O farelo (ZMZ26, dez/26) fechou em **329,20 US$/sht** (30/10; faixa do dia 328,30–330,10). Em 26/10 estava em 340,20: queda de **3,2% em quatro pregões** (340,20 → 334,60 → 335,70 → 329,20 → 329,20). É a perna que mais cai em termos percentuais no complexo, o que confirma a leitura de "sobra". **Atenção:** a barra de 30/10 do farelo (abertura 329,30, máxima 330,10, mínima 328,30, fechamento 329,20, volume 1.528) é **praticamente idêntica** à de 29/10 no dump; o mesmo vale para a máxima/mínima do heating oil. Isso sugere que parte dos dados de 30/10 é cópia ou carry da sessão anterior (provável captura parcial); o "fechamento" de 329,20 pode não ser o fechamento definitivo.

*Curva a termo.* dez/26 329,20 · jan/27 329,50 · mar/27 330,70 · mai/27 334,00 · jul/27 338,20 (CBOT, 2026-10-30): carry de apenas ~9 US$/sht em sete meses (2,7%) — curva praticamente plana. Em mercado de proteína apertada o prompt seria mais caro que o diferido; aqui o oposto, sem prêmio de escassez.

*Ratio Far/Soj em 80,03%.* É o termômetro mais direto da tese. O farelo vale 80% do que valeria pela paridade com a soja (`indicators` 2026-10-30; no `indicators` de 29/10, 80,00%; 28/10, 81,35%; 27/10, 80,76%; 26/10, 81,49%). Quando o ratio está baixo, o farelo é **barato relativamente ao grão**, e isso acontece quando o óleo está pagando o esmagamento — a indústria mói por causa do óleo e o farelo "sobra". Nos últimos cinco pregões o ratio oscilou numa faixa estreita de 80,0–81,5%, ou seja, **ele está sendo defendido nessa região**, mas cada toque do piso foi de baixo para cima; hoje ele encostou de novo em 80%.

*Oil share e spread óleo−farelo.* Oil share de **49,99%** e spread óleo−farelo de **−0,0033 US$/bu** (`indicators` 2026-10-30): em 28/10 o spread era −0,1738 e em 26/10 −0,1133; ele **fechou** de forma quase total, ou seja, o óleo ganhou peso relativo no crush porque o farelo caiu 3,2% enquanto o óleo caiu só 1,8%. Quanto mais o óleo manda, mais o farelo é subproduto — a tese estrutural continua intacta.

*Índice de Sobra de Farelo.* **75/100** ("sobra relevante, 3 de 4 condições", `indicators` 2026-10-30), o mesmo valor em todos os dias de 26 a 30/10. Constante ao longo da semana quer dizer que as condições estruturais estão ativas, mas que o índice **não informa direção diária** — não o uso como gatilho de entrada.

*Posicionamento dos fundos — o ponto mais sensível.* CFTC COT em 20/10: managed money em farelo com **213.717 contratos comprados e apenas 12.839 vendidos, net long de 200.878** (CFTC COT 2026-10-20), sobre OI de 635.401 — a ponta comprada dos fundos é ~34% do open interest, mais que a soja (~24%) e o óleo (~18%). O lado vendido dos fundos é quase inexistente (12,8 mil). Do outro lado, os **produtores** têm 414.822 vendidos contra 66.804 comprados (hedge da indústria). Interpretação: o mercado de farelo está **assimétrico**: os fundos estão muito comprados numa proteína que o fundamento diz estar sobrando. Se o preço continua recuando, a liquidação desses longs alimenta a queda (não há short de fundo para ser recomprado e amortecer). Esse é o mecanismo que dá sustentação à tese baixista **além** do fundamento. Limitações: o dado tem 10 dias e o briefing não traz o percentil histórico.

*Oferta e exportação do Brasil.* ABIOVE (projeções mensais): produção de farelo de **1.977,6 mil t em nov/2026** e **1.659,0 mil t em dez/2026**; exportação de 800,0 mil t (nov) e 700,0 mil t (dez); estoque final de **1.101,4 mil t** (nov) e **1.015,5 mil t** (dez). O estoque projetado cai ~86 mil t em dezembro, o que é um viés levemente de apertamento da oferta brasileira no fim do ano. Mas os valores são projeções e pouco dizem sobre o ritmo real de embarques; o dump também não traz o prêmio de exportação (Paranaguá), nem a oferta argentina, o principal concorrente do farelo brasileiro.

*Lado da ração.* O briefing não traz milho nem proteína concorrente, então não consigo avaliar a demanda via ração.

**O que INVALIDA / risco**

- **Retorno à média do ratio**: um fechamento do ratio acima de ~82% (o topo da faixa de cinco dias é 81,5%) com o farelo subindo mais que a soja desfaz o argumento de "sobra".
- **Short squeeze técnico**: o farelo já recuou 3,2% e o ratio está no piso; um repique de 5–8 US$ pode ocorrer mesmo sem notícia.
- **NOPA** (fila `release-nopa-2026-10-30`): se o esmagamento mensal vier fraco, o excesso de farelo diminui e a tese se enfraquece. O dump de hoje **não traz o número** (paywall), então não posso julgar.
- **Dados**: uma reescrita adicional dos fechamentos de 29 e 30/10 mudaria o ratio e, com ele, a conclusão (o ratio de 29/10 já mudou de 81,54% para 80,00% por revisão).

**Leitura operacional**

*Short:* a tese estrutural e o posicionamento sustentam, mas o ratio no piso de 80% reduz o prêmio de entrada — operar short de farelo *outright* é pagar caro; prefiro operar o short como **spread** (veja Spreads). *Long:* só tático e curto, com gatilho no ratio voltando acima de 81,5%/82%; contra a tendência da semana. O forecast do robô (7d central 315,91; faixa 301,11–330,71; 30d central 267,01) é extrapolação mecânica de tendência e inclinação — **−19% em 30 dias é um número que o fundamento não sustenta** e eu não o adoto.

*Fila tratada:* `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` e `-D+90`: a tese de junho partia de um ratio de 81,4%. Hoje o ratio é 80,03% — o spread **seguiu comprimindo** (−1,4 pp) e agora encosta no limiar de 80%, de modo que a direção da tese ("viés baixista no farelo contra a soja") se confirma, mas o *tamanho* é pequeno e não tenho o preço do farelo em junho no briefing para dizer se a operação ganhou dinheiro. O D+7 (18/06) e o D+90 (09/09) estão vencidos; recomendo fechar a revisão como "direção confirmada, ganho de preço não verificável".

## Óleo

**Viés:** baixista **fraco** (de preço), confiança baixa.

**O que sustenta a tese**

*Nível e momentum.* O óleo (ZLZ26, dez/26) fechou em **65,81 US¢/lb** em 30/10 (faixa 65,64–65,90), alta de 0,12 sobre os 65,69 de 29/10 e de 0,25 sobre os 65,56 de 28/10, mas abaixo dos **67,01 de 26/10** (−1,8%) e dos 66,71 de 27/10. O óleo está **ficando de lado** em 65,5–66, depois de ter perdido 1,15 centavo entre 27/10 (66,71) e 28/10 (65,56). Ele cai menos que o farelo, e é por isso que o oil share sobe.

*Curva a termo.* dez/26 65,81 · jan/27 66,04 · mar/27 66,47 · mai/27 66,77 · jul/27 66,84 (CBOT 2026-10-30): contango leve (+1,03 US¢, ou 1,6%, até julho). Sem escassez, mas com um carregamento um pouco maior que o do farelo — o mercado reconhece alguma sustentação futura (biocombustível), sem pagar prêmio imediato.

*Heating oil e a margem de biodiesel — o fator dominante.* O heating oil (HO=F) fechou em **4,5738 US$/galão** em 30/10, contra 4,91 em 26/10: **−6,9% em cinco pregões** (`indicators` 2026-10-30; leitura de ontem: 4,98 em 23/10, −8,2% desde então). Mecanismo: o biodiesel compete com o diesel; quando o diesel fica barato, o biodiesel precisa de óleo mais barato para ser competitivo e a demanda por óleo de soja se enfraquece. A margem de biodiesel dos EUA calculada pelo robô é de **US$ 2,0031/galão** (receita 7,74 = HO 4,57 + 1,5 × RIN 2,11; custo 5,74 = óleo 4,94 + 0,80 de custos industriais), contra **US$ 2,2513 em 26/10** (−11%). A margem **ainda é grande** em termos absolutos, portanto o biodiesel americano continua rentável e não há sinal de colapso da demanda; mas a direção é de piora, e foi o heating oil (−0,34 US$/gal) que fez isso, parcialmente compensado pelo barateamento do óleo (custo −0,09). **Ressalva:** o RIN está fixo em 2,11 em todos os dias do dump, o que sugere que não é uma cotação diária — então a *variação* da margem é confiável (vem do HO e do óleo), mas o *nível* não.

*Oil share em 49,99% e Índice de Suporte do Óleo.* O óleo vale metade do crush (`indicators` 2026-10-30). Oil share alto é, por um lado, a prova de que o óleo está sustentado pela demanda de biocombustível; por outro, expõe o complexo inteiro a esse único vetor: se o óleo cede, o oil share cai e a margem da indústria também. O **Índice de Suporte do Óleo** está em **60/100** ("suporte relevante, 3 de 5 condições"), o mesmo valor de 26 a 30/10 — a base está ativa, mas o índice **não indica direção** de curto prazo.

*Posicionamento dos fundos.* CFTC COT em 20/10: managed money em óleo com **104.484 comprados, 32.966 vendidos, net long 71.518** sobre OI de 570.462 (CFTC 2026-10-20). É uma posição comprada mais **moderada** que a do farelo (~18% do OI na ponta comprada) e com short de fundo maior (33 mil), o que torna o óleo menos vulnerável a liquidação forçada. Os *swaps* estão comprados em 97.172 contra apenas 4.819 vendidos — compradores comerciais/índices de longo prazo, tipicamente estáveis. Nota: o dado tem 10 dias.

*Demanda brasileira e oferta.* ABIOVE (projeções): produção de óleo de **494,9 mil t em nov/2026** e **415,2 mil t em dez/2026**; **exportação de apenas 21 mil t em novembro**; estoque final de **315,3 mil t** (nov) e **291,9 mil t** (dez). O Brasil exporta quase nada de óleo — toda a produção fica no mercado interno, majoritariamente biodiesel. Por isso o óleo brasileiro é muito mais sensível a **política de mistura** (B15/B16) do que ao mercado externo. A queda projetada dos estoques em dezembro (−23 mil t) é um viés levemente altista para o óleo interno, mas o dump não traz basis nem preço de praça.

*Palma e demais fatores.* A página do MPOB (palma da Malásia) foi lida em todos os dias do dump, mas o **parser não extraiu números** (`mpob`, 2026-10-30) — não tenho estoque nem exportação de palma, que são o principal substituto do óleo de soja. Também não tenho RIN D4 diário (o valor de 2,11 é fixo), nem o diesel brasileiro.

**O que INVALIDA / risco**

- **Heating oil recuperando** para ~4,80–4,90 (nível de 27/10 e 26/10): reverte a pressão e leva o óleo de volta a ~67.
- **Anúncio do B16** (CNPE) ou qualquer sinal da EPA (RFS) / crédito 45Z nos EUA — os gatilhos altistas mais fortes; nada no dump os confirma.
- **Fechamento do óleo abaixo de ~65,50** (mínima da semana é 65,56 em 28/10) com HO caindo: abre espaço para 64–63,9.
- Sobre o forecast: o robô projeta 7d central de 64,96 (faixa 62,88–67,04) e 30d central de 61,89; a banda inclui o spot, então é compatível com lateralidade; eu espero **lateral-baixista** em 64,5–66,5 para os próximos dias, e não os −6% do central de 30d.

**Leitura operacional**

*Short:* o fluxo do diesel é favorável, mas o óleo vem **resistindo** (65,81 contra 65,69 ontem enquanto o HO estava no mesmo patamar), e os fundos não estão tão comprados quanto no farelo — o short outright de óleo tem convicção menor que o do farelo. *Long:* oil share de 50% e margem de biodiesel de US$ 2/gal mostram que a demanda estrutural é forte, e o ponto de entrada tático é perto de 65,5 com stop abaixo de 65,0; o catalisador (B16, EPA, 45Z) precisa vir de fora. *Spread:* **óleo contra farelo** (long óleo / short farelo) é a expressão mais limpa da tese do complexo; ver Spreads.

*Fila tratada:* `alerta-quebra_suporte-oleo_cbot-2026-10-30` — o óleo fechou em 65,81, "abaixo do suporte 72,00". O nível de 72 é **claramente defasado**: o preço está 8,6% abaixo dele, e o suporte já foi rompido há tempos (não é evento de hoje). O alerta confirma que a tese de pressão sobre o óleo está em curso, mas não acrescenta informação nova; o que importa hoje é o patamar de 65,5 e o heating oil. Recomendo recalibrar o nível.

## Spreads e crush (leitura de complexo)

*Crush margin.* **US$ 2,1415/bu** em 30/10 (farelo 329,20 + óleo 65,81 − soja 1.234,00; `indicators`), contra 2,1233 (29/10), 2,2170 (28/10), 2,2693 (27/10) e 2,3305 (26/10). Em quatro dias a margem perdeu **19 centavos (−8,1%)**: a indústria continua ganhando bem, mas menos. A margem ainda é alta o bastante para sustentar o esmagamento (a ABIOVE projeta 2,63 milhões de t em novembro), de modo que a oferta de farelo e óleo **continua chegando ao mercado** — e é isso que mantém a pressão de preços nos produtos.

*Far/Soj (mean-reversion, os dois lados).* O ratio de 80,03% está no piso da faixa recente (80,0–81,5%). Para short de farelo contra soja (ou seja, short do ratio), o prêmio restante é pequeno; para long do ratio (long farelo/short soja), o ponto de entrada é bom do ponto de vista da média, mas **vai contra** o fundamento de sobra e contra o posicionamento (fundos muito comprados em farelo). Eu leio como **assimetria desfavorável para o short do ratio e neutra para o long**: a tese baixista do farelo hoje deve ser operada mais por spread com o óleo do que contra a soja.

*Oil share e spread óleo−farelo.* O oil share em 49,99% e o spread óleo−farelo em −0,0033 US$/bu significam que, no mundo atual, **os dois produtos valem a mesma coisa**. Em 28/10 o spread era −0,1738: o farelo estava valendo mais que o óleo. A correção veio mais do farelo caindo do que do óleo subindo. O spread óleo−farelo em zero é um ponto de **equilíbrio**, sem direção própria; qualquer tese de long óleo/short farelo é, portanto, uma aposta de **continuidade** do movimento da semana, não de reversão.

*Os índices sintéticos juntos.* Sobra de Farelo 75 e Suporte do Óleo 60, **ambos inalterados** desde 26/10. Dizem: "o farelo está estruturalmente sobrando (3 de 4 condições) e o óleo está estruturalmente sustentado (3 de 5 condições)". A combinação é consistente com o oil share de 50% — o óleo manda. Mas, como não mudaram, **não explicam o movimento da semana**; quem explica é o heating oil.

*Em conjunto.* O complexo está em **deriva baixista comum**, com o diesel como pivô via óleo, o farelo como a perna mais frágil e a soja como a mais estável. O crush margin em queda e o ratio no piso dizem que o mercado já descontou boa parte da sobra de farelo; o risco, portanto, vira **tático** (repique) mais do que estrutural.

## Lente fiscal/regulatória BR

O monitor tributário (`system/tributario_watch.toml`) tem `atualizado_em = 2026-06-05` nos vetores principais — **quase cinco meses sem atualização**. Trago-os como registrados, sem validação nova (o briefing de hoje não traz seção do monitor).

- **MP 1.363/2026** — subvenção de R$ 1,12/L ao diesel fóssil, vigente até **31/12/2026**. Barateia o diesel dentro do mix B15, reduz a competitividade do biodiesel e a demanda interna por óleo de soja. Efeito **baixista para o óleo** e, indiretamente, para o farelo (menos esmagamento puxado por óleo). Coerente com a fraqueza do diesel/heating oil, embora aqui seja política e lá seja mercado. Fica uma pergunta de calendário: a vigência até 31/12 abre risco de **renovação ou fim** da subvenção em dezembro — o fim seria altista para o biodiesel e o óleo.
- **MP 1.358/2026** — subvenção à gasolina/diesel com vigência até 11/07/2026: **expirada**; o desfecho (conversão ou caducidade) não está no briefing.
- **B16 (CNPE)** — mistura de biodiesel a 16%, adiada; os testes técnicos de seis meses teriam resultado perto de **nov/2026**, e cada +1 pp de mistura puxaria ~436 mil t de óleo. Novembro é o próximo marco; **nada no dump indica convocação** do CNPE. É o principal gatilho altista doméstico para o óleo e, indiretamente, para o farelo (mais esmagamento, mais sobra de proteína — efeito misto).
- **PIS/Cofins do biodiesel** e **STJ REsp 2165276** (crédito de PIS/Cofins sobre soja em biodiesel): vetores de custo da cadeia; sem atualização desde junho.
- **EUA/Indonésia:** EPA RFS 2026/2027, crédito 45Z, Indonésia B50, levy e Danantara — marcos vencidos no catálogo e sem validação. São o principal potencial de sustentação do óleo, mas **não valido nenhum**.

Aplicação: antes de concluir tese de preço BR, o filtro fiscal vai no **sentido baixista para o óleo interno** (MP 1.363 vigente, B16 parado) e **neutro para a soja**. Eu não concluo nada além disso sem atualizar o catálogo.

## Riscos e eventos próximos

- **COT de 27/10:** publicado pela CFTC em 30/10, **não está no dump**. Principal dado a checar: se os fundos reduziram o net long de farelo (200,9 mil em 20/10).
- **WASDE (28/10)** e **NOPA (30/10):** ambos entraram na fila (`release-usda_wasde-2026-10-28`, `release-nopa-2026-10-30`) como "coletado, ainda não interpretado" — mas **o briefing não traz nenhum número**: o NOPA exige assinatura paga (`nopa`, status 0) e o WASDE não aparece na lista de seções do dump. Não consigo dizer se mudam o balanço; o que posso dizer é que uma leitura do NOPA de esmagamento acima do esperado seria baixista para o farelo (mais sobra) e altista para o óleo (mais oferta, porém mais biodiesel).
- **Próximos WASDE, COT e NOPA:** o COT é semanal (divulgado às sextas) e o WASDE e o NOPA são mensais; as datas exatas não constam no briefing e vêm de conhecimento geral de calendário.
- **Novembro:** possível convocação do CNPE para o B16 (testes técnicos), fim do prazo da MP 1.363 em 31/12, e avanço da safra sul-americana sob El Niño.
- **Diesel/heating oil:** o pivô diário do óleo; um repique para 4,80+ muda a leitura.
- **Dados:** monitorar se o dump de 31/10 reescreve novamente os fechamentos de 29 e 30/10.

## Honestidade

- **Dump de 30/10 parcial ou com carry:** a barra de 30/10 do farelo (abertura 329,30, máxima 330,10, mínima 328,30, fechamento 329,20, volume 1.528) é idêntica à de 29/10 no dump, e a máxima/mínima do heating oil também. O fechamento "329,20" pode não ser definitivo. Soja e óleo têm barras diferentes.
- **Revisão de fechamentos:** a leitura de 29/10 registrou farelo 335,40, óleo 65,17 e ratio 81,54% para 29/10; o `indicators` de hoje mostra farelo 329,20, óleo 65,69 e ratio 80,00% para o mesmo dia (soja passou de 1.234,00 para 1.234,50). A conclusão de ontem de que o ratio "se afastou do piso" **foi desfeita** pela revisão: hoje o ratio está no piso. A fonte que muda de dia para dia reduz a confiança em tudo o que depende de fechamento de um dia só.
- **Câmbio com saltos suspeitos:** PTAX 5,0377 (23/10) → 5,5007 (26/10) → 5,3346 (27/10) e EUR/BRL 5,64 → 6,15 → 5,94 não são movimentos plausíveis de um dia para outro. Trato o câmbio como direcional. A fila (`alerta-quebra_resistencia-usd_brl_ptax-2026-10-29`) marca o PTAX de 29/10 (5,3744) acima da resistência 5,30: o fato é real conforme a série, mas **não valido a magnitude**; a tese de soja em reais depende do câmbio, então a confiança é baixa.
- **Sem WASDE e sem NOPA em números**, sem físico BR (Paranaguá, basis, praças), sem CEPEA, sem exportação semanal dos EUA, sem palma (parser do MPOB falhou), sem notícias (`noticias_rss`: 0 itens lidos), sem milho/ração, sem RIN diário (fixo em 2,11) e sem percentil do COT.
- **COT de 20/10:** tem 10 dias; as posições mudaram.
- **Níveis das alertas da fila:** soja 1.180 e óleo 72,00 estão defasados em relação ao mercado atual — os alertas não trazem informação nova.
- **Forecasts do robô:** são extrapolações estatísticas de tendência e volatilidade. Os centrais de 30 dias (soja 1.105,98; farelo 267,01; óleo 61,89) implicam quedas de 10%, 19% e 6%, que **não** estão sustentadas pelo fundamento disponível; mantive apenas a direção baixista fraca.
- **Calendário:** as datas de próximos WASDE/COT são regulares, não confirmadas no briefing.
- **Conviçção geral:** baixa. A direção (baixista fraca) é coerente entre soja, farelo e óleo, e o ratio no piso é um fato robusto no `indicators`; tudo o mais depende de dados que não consegui validar.
