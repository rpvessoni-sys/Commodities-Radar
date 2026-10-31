---
data: 2026-10-31
titulo: "Sáb 31/10 (dados do pregão de sex 30/10): o farelo vira o elo mais fraco — ratio Far/Soj em 78,94% (zona 'comprimido'), Sobra de Farelo no máximo (100/100) e crush em US$ 2,04/bu — enquanto o óleo, já na metade do crush (oil share 50,33%), segura melhor que o farelo; fundos liquidaram posição na semana (COT 27/10), o que alivia o 'fundo lotado', mas não inverte a tendência; confiança baixa-média por falta de WASDE/NOPA em número e PTAX instável"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT via briefing 2026-10-31 — sessão **2026-10-30**. Soja ZSF27 (jan/27) abertura 1.234,50 · máxima 1.242,00 · mínima 1.230,75 · fechamento **1.234,00** US¢/bu · volume 115.283 (curva X26 1.221,50 · H27 1.243,50 · K27 1.253,25 · N27 1.260,25 · Q27 1.245,50). Farelo ZMZ26 (dez/26) abertura 329,30 · máxima 330,30 · mínima 324,40 · fechamento **324,70** US$/sht · volume 68.188 (curva F27 325,40 · H27 327,30 · K27 330,90 · N27 335,30). Óleo ZLZ26 (dez/26) abertura 65,66 · máxima 66,59 · mínima 65,64 · fechamento **65,81** US¢/lb · volume 63.997 (curva F27 66,07 · H27 66,55 · K27 66,93 · N27 67,02). Heating oil HO=F abertura 4,58 · máxima 4,7182 · mínima 4,57 · fechamento **4,655** US$/galão · volume 35.213
  - CME CBOT via briefing — sessões 2026-10-29 (soja 1.234,75 · farelo 329,30 · óleo 65,64 · HO 4,736), 10-28 (soja 1.238,00 · farelo 335,70 · óleo 65,56 · HO 4,82), 10-27 (soja 1.243,00 · farelo 334,60 · óleo 66,71 · HO 4,78) e 10-26 (soja 1.252,50 · farelo 340,20 · óleo 67,01 · HO 4,91), conforme `indicators` do briefing de 31/10
  - Indicadores do robô (`indicators`, 2026-10-26 a 2026-10-31) — crush margin, Far/Soj, oil share, spread óleo−farelo, margem de biodiesel EUA, índices de Sobra de Farelo e Suporte do Óleo, paridade BRL
  - BCB PTAX (sgs 1 e 21619) 2026-10-19 a **2026-10-30** (USD/BRL 5,4212 em 30/10)
  - CFTC COT (managed money) data-base **2026-10-27** e 2026-10-20
  - USDA Crop Progress 2026-10-25 (colheita de soja EUA 79%) e 2026-10-18 (64%)
  - ABIOVE projeções mensais nov/2026 e dez/2026
  - INMET 2026-10-31 (previsão por praça), NOAA CPC 2026-10-31 (El Niño Advisory), MPOB 2026-10-31 (página lida, sem números), NOPA 2026-10-31 (sem número, paywall)
  - Forecasts estatísticos do robô gerados em 2026-10-31 (7d e 30d)
  - `system/tributario_watch.toml` (vetores registrados, `atualizado_em = 2026-06-05`)
status: ativa
vies: [bear-soja, bear-farelo, bear-oleo_soja]
---

## Visão geral

Pense no complexo da soja como **uma fábrica**: a indústria compra o grão (soja), esmaga e vende dois produtos — o **farelo** (a proteína, que vira ração) e o **óleo** (alimentação e, cada vez mais, biodiesel). A margem da fábrica é o **crush margin** (margem de esmagamento): valor do farelo + valor do óleo − custo da soja, por bushel (unidade de volume do grão, ~27 kg). Em 30/10 essa margem foi de **US$ 2,04/bu** (`indicators` 2026-10-30), contra US$ 2,33 em 26/10 (−12,4% em cinco pregões). A margem encolhe porque os *produtos* caem mais que o *insumo*: no mesmo intervalo a soja perdeu 1,5% (1.252,50 → 1.234,00 US¢/bu), o óleo 1,8% (67,01 → 65,81 US¢/lb) e o farelo **4,6%** (340,20 → 324,70 US$/short ton). Quem manda no crush hoje é o óleo, e a razão é aritmética: o **oil share** (fatia do óleo no valor total gerado pelo esmagamento) está em **50,33%** (óleo 7,24 de um total de 14,38 US$/bu, `indicators` 2026-10-30). O óleo "paga" metade da conta da fábrica porque tem uma demanda extra — biocombustíveis — que o farelo não tem. Consequência: a indústria mói soja pelo óleo, e o farelo, que vem junto como subproduto, **sobra**. Quando um produto sobra e o outro não, o que sobra fica barato.

É exatamente isso que o **ratio Far/Soj** mostra. Ele compara o valor de uma tonelada de farelo com o da soja que a originou (farelo ÷ soja em US$/short ton): em 30/10 está em **78,94%** (324,70 ÷ (1.234,00 × 33,33 ÷ 100), `indicators`), abaixo do limiar de 80% a partir do qual o robô classifica o farelo como "abundante" (≥87% seria "apertado"). Em linguagem simples: o farelo vale hoje menos de 79% do que o grão vale, e o ratio **entrou na zona 'comprimido'** (fila `ratio-zona-2026-10-30`; ontem estava em 80,0%). O índice de **Sobra de Farelo** saltou de 75 para **100/100** (4 de 4 condições, `indicators` 2026-10-31) e o de **Suporte do Óleo** de 60 para **80/100** (4 de 5): os dois lados da mesma moeda, "o farelo é a sobra, o óleo domina o crush", agora com todas as condições estruturais acesas.

O que mudou hoje: (i) o farelo rompeu para baixo — mínima de 324,40 e fechamento 324,70, contra 329,30 na véspera, num pregão de volume grande (68.188 contratos); (ii) o óleo teve máxima de 66,59 mas devolveu e fechou em 65,81, mostrando que não consegue subir, mas também não cede; (iii) o **COT** (relatório semanal de posição dos fundos da CFTC) de 27/10 chegou e mostra os fundos **reduzindo** posição comprada nas três pernas — o "fundo lotado" no farelo, que era o grande risco, está um pouco menos lotado (net long de 200,9 mil para 168,7 mil contratos); (iv) o dólar subiu para R$ 5,4212 (PTAX de 30/10), amortecendo em reais a queda do CBOT. **Leitura de uma linha:** o pivô do complexo é o **óleo (via diesel/heating oil)**, a maior convicção é **baixista no farelo** (sobra estrutural + ratio comprimido, mas com risco de repique tático), e a confiança do dia é **baixa-média** — a direção é coerente entre as três pernas, mas faltam WASDE e NOPA em número e a série de câmbio tem saltos suspeitos.

## Soja

**Viés:** baixista **fraco** (de preço), confiança baixa-média. A soja é a perna mais estável do complexo; cai pouco e devagar.

**O que SUSTENTA a tese**

*Nível e momentum.* A soja (ZSF27, jan/27) fechou em **1.234,00 US¢/bu** em 30/10, contra 1.234,75 (29/10), 1.238,00 (28/10), 1.243,00 (27/10) e 1.252,50 (26/10) — `indicators`. São cinco degraus pequenos, queda acumulada de 1,5%. O pregão de 30/10 teve amplitude de 11,25 centavos (1.230,75–1.242,00) e fechou praticamente onde abriu (1.234,50): houve tentativa de alta até 1.242,00 que foi vendida de volta. Mecanismo: um mercado que sobe no intraday e devolve tudo está dizendo que há vendedor em cima — oferta física (colheita) e fundos reduzindo exposição. O volume alto (115.283) torna o sinal mais confiável que o das barras "mortas" de dias anteriores.

*Curva a termo.* nov/26 1.221,50 · jan/27 1.234,00 · mar/27 1.243,50 · mai/27 1.253,25 · jul/27 1.260,25, com ago/27 recuando para 1.245,50 (CBOT 2026-10-30). Carry de 38,75 US¢ entre nov e jul (3,2%): é **contango**, o mercado paga para guardar soja, ou seja, não há escassez imediata. O recuo de ago/27 abaixo de jul/27 sugere expectativa de safra nova (2027/28) mais folgada. Curva assim é coerente com viés baixista fraco, não com corrida de alta.

*Colheita nos EUA.* USDA Crop Progress: **79% colhido em 25/10**, contra 64% em 18/10 (+15 pp numa semana). Colheita avançada elimina o principal prêmio de risco do hemisfério norte: o que estava no campo virou oferta física. O briefing não traz a média de cinco anos nem o ritmo de exportação, então não digo se 79% é adiantado ou normal; digo apenas que a janela de risco de safra EUA está se fechando — e que o próximo dado (de 01/11, ainda fora do dump) deve mostrar números acima de 85%.

*Câmbio e paridade em reais.* PTAX USD/BRL **5,4212 em 30/10**, contra 5,3744 (29/10), 5,3420 (28/10) e 5,0377 em 23/10 (BCB sgs 1). A paridade de exportação em reais é **R$ 147,48/saca de 60 kg** (CBOT 1.234,00 × 5,4212, sem basis; `indicators` 2026-10-30), contra R$ 146,30 em 29/10 e R$ 145,80 em 28/10. Ou seja: o CBOT caiu, mas o dólar mais caro **mais do que compensou** em reais. Mecanismo: o produtor brasileiro recebe em dólar; real mais fraco eleva o preço interno e estimula a venda, o que adiciona oferta ao mercado e limita o que o CBOT poderia subir. É amortecedor para o preço doméstico, mas empurra a pressão de oferta para fora. Fila: `alerta-quebra_resistencia-usd_brl_ptax-2026-10-30` — o PTAX (5,42) está acima da "resistência" de 5,30. O fato é real na série, mas o nível está claramente defasado (o dólar já estava em 5,33–5,34 em 27–28/10, e foi a 5,50 em 26/10); o alerta confirma o real mais fraco, não acrescenta direção nova. **Ressalva:** a série mostra saltos que parecem irreais (5,0377 em 23/10 → 5,5007 em 26/10, +9,2% em um pregão útil; EUR/BRL de 5,64 para 6,15) — trato o câmbio como direção, não como número exato (ver Honestidade).

*Posicionamento dos fundos.* COT (CFTC) de **27/10**: managed money (fundos) em soja com **226.215 comprados e 32.434 vendidos, net long de 193.781** sobre open interest (OI, contratos em aberto) de 979.414. Uma semana antes (20/10): 259.970 / 38.645, net 221.325, OI 1.093.612. Ou seja, **−27,5 mil contratos de net long (−12,4%)** e o OI caiu 10,4%: é **liquidação clássica** — fundo vendendo posição comprada e saindo do mercado, não fundo virando vendido. A ponta comprada dos fundos ainda é ~23% do OI, posição grande. Mecanismo: ainda há combustível de queda (quem está comprado precisa vender se o preço ceder), mas parte do combustível já foi queimado, o que explica por que a soja cai devagar. O briefing não traz o percentil histórico; afirmo "grande em termos absolutos", não "extrema".

*Demanda e margem.* O crush de US$ 2,04/bu ainda é positivo e sustenta o esmagamento. ABIOVE (projeções mensais): esmagamento de **2.626,6 mil t em nov/2026** e **2.203,5 mil t em dez/2026**; estoque final de soja de 3.659 mil t (nov) e 1.890 mil t (dez); exportação projetada de apenas 108 mil t em novembro. Lê-se: safra velha sendo consumida, oferta doméstica apertando no fim do ano — suporte sazonal à soja no Brasil. São *projeções*, não resultado.

*Clima.* NOAA CPC mantém **El Niño Advisory** (2026-10-31). Regra geral de mercado (conhecimento geral, não vem do briefing): El Niño tende a favorecer chuva no Sul do Brasil/Argentina e a trazer irregularidade no Norte/Nordeste. INMET 31/10: pancadas de chuva e trovoadas isoladas em Sorriso (33 °C), Sinop (35 °C), Lucas do Rio Verde (34 °C), Cuiabá (33 °C), Rio Verde/GO (28 °C); chuva isolada em Maringá (29 °C), Cascavel (28 °C) e Passo Fundo (25 °C). Chuva no Centro-Oeste na fase de plantio/emergência é benigna; nada no dump indica estresse hídrico. Clima **não** sustenta prêmio de risco hoje.

**O que INVALIDA / risco**
- Fechamento da soja **acima de ~1.252** (máxima semanal de 26/10) com volume: devolve a tendência da semana.
- Número de WASDE (28/10, fila `release-usda_wasde-2026-10-28`) que reduza estoques finais — **não consigo avaliar**, o dump não traz o relatório.
- Falha climática no Centro-Oeste ou no sul argentino (o El Niño vira variável).
- Fundos: se o COT de 03/11 mostrar nova liquidação forte, o viés baixista ganha força; se mostrar recompra, o risco de squeeze aparece.
- Real forte devolve pressão ao preço interno em reais.

**Leitura operacional**
*Short:* tático, alvos modestos. O forecast mecânico do robô (7d central 1.206,26, faixa 1.182,63–1.229,89; 30d central 1.106,11) é extrapolação de MA20 + volatilidade + inclinação; o topo da banda de 7 dias (1.229,89) está abaixo do spot, sinal de que o modelo só projeta a inclinação. **Não adoto −10% em 30 dias**; alvo defensável na região de 1.200–1.210. *Long:* sem gatilho técnico nem fundamental; contra curva em contango, colheita fechando e fundo ainda grande, exige stop curto (acima de 1.242, a máxima do dia). O melhor uso da soja é como **perna do crush** (ver Spreads).

*Fila tratada:* `alerta-quebra_resistencia-soja_cbot-2026-10-30` — fechou em 1.234,00, acima do nível 1.180,00. O nível é antigo (preço 4,6% acima dele há semanas); o alerta não muda a tese. Sugiro recalibrar o nível (tarefa da camada de calibração).

## Farelo

**Viés:** baixista **moderado**, confiança média. É a perna com a maior convicção do dia, mas com a ressalva de que o ratio já está comprimido.

**O que SUSTENTA a tese**

*Nível e momentum.* O farelo (ZMZ26, dez/26) fechou em **324,70 US$/sht** em 30/10 (faixa 324,40–330,30), contra 329,30 (29/10), 335,70 (28/10), 334,60 (27/10) e 340,20 (26/10). Queda de **4,6% em quatro pregões**, a maior do complexo. O pregão de 30/10 abriu em 329,30 e fechou praticamente na mínima (324,70 vs 324,40) com volume forte (68.188): fechar na mínima com volume é o padrão de pressão vendedora que persiste, ao contrário de "queda sem convicção".

*Curva a termo.* dez/26 324,70 · jan/27 325,40 · mar/27 327,30 · mai/27 330,90 · jul/27 335,30 (CBOT 2026-10-30): carry de ~10,60 US$/sht em sete meses (3,3%). Em mercado de proteína apertada o prompt seria mais caro que o diferido; aqui é o oposto — sem prêmio de escassez.

*Ratio Far/Soj em 78,94% — a fila do dia.* O ratio estava em 81,49% (26/10), 80,76% (27/10), 81,35% (28/10), 80,01% (29/10) e agora 78,94% (30/10), `indicators`. Pela primeira vez na janela o ratio **fecha abaixo de 80%**: o piso que vinha sendo "defendido" foi rompido (fila `ratio-zona-2026-10-30`). Isso muda a leitura do spread de duas formas. Primeiro, **confirma** a tese de que o farelo está barato em relação ao grão por causa da sobra (óleo pagando o crush). Segundo, reduz o prêmio restante para quem opera short do ratio: quanto mais baixo o ratio, mais perto de uma zona de retorno à média (o farelo "barato demais" atrai demanda de ração e desestimula esmagamento só pelo óleo). Em mean-reversion, abaixo de 80% o risco passa a ser bilateral: a tendência (momentum + sobra) empurra para baixo, a média puxa para cima. Ainda não há evidência de reversão — o fechamento na mínima com volume diz que o mercado continua pagando para vender.

*Oil share e spread óleo−farelo.* Oil share **50,33%** e spread óleo−farelo de **+0,0957 US$/bu** (`indicators` 2026-10-30), contra −0,1738 em 28/10 e −0,0242 em 29/10. O spread **virou positivo**: pela primeira vez na janela o óleo vale mais que o farelo no crush. Quanto mais o óleo manda, mais o farelo é subproduto — a tese estrutural se aprofunda.

*Índice de Sobra de Farelo.* **100/100** ("forte pressão baixista no farelo, 4/4 condições", `indicators` 2026-10-31; era 75 de 26 a 29/10). A diferença em relação a ontem é real: uma condição a mais acendeu (consistente com ratio <80%). É o máximo da escala, mas lembro que é um índice de *estado*, não de timing — mostra que as condições estruturais estão todas presentes, não que o preço cairá amanhã.

*Posicionamento dos fundos — o ponto mais sensível, agora melhor.* COT 27/10: managed money em farelo com **184.371 comprados e 15.657 vendidos, net long de 168.714**, sobre OI de 609.960 (a ponta comprada é ~30% do OI, o net é ~27,7%). Em 20/10 eram 213.717 / 12.839, net 200.878, OI 635.401. Variação: **−32,2 mil contratos de net long (−16,0%)**, com compradores saindo (−29,3 mil) e vendidos crescendo pouco (+2,8 mil). Do outro lado, os produtores/indústria têm 387.753 vendidos contra 69.776 comprados (hedge), e os swaps estão comprados em 133.898 contra 13.251 vendidos. Interpretação: o farelo continua com posição de fundo **grande e unilateral** — 168 mil líquidos comprados numa proteína que o fundamento diz estar sobrando —, mas a liquidação já começou. Se o preço continua recuando, os longs restantes alimentam a queda (quase não há short de fundo para ser recomprado e amortecer). Esse é o mecanismo que sustenta a tese baixista *além* do fundamento. Limitação: o dado tem 4 dias (data-base de terça) e não há percentil histórico no briefing.

*Oferta e exportação do Brasil.* ABIOVE (projeções): produção de farelo de **1.977,6 mil t em nov/2026** e **1.659,0 mil t em dez/2026**; exportação de 800 mil t (nov) e 700 mil t (dez); estoque final de **1.101,4 mil t** (nov) e **1.015,5 mil t** (dez). Estoque cai ~86 mil t em dezembro — leve aperto da oferta brasileira no fim do ano, insuficiente para contrapor a sobra via esmagamento forte (2,63 milhões de t de soja em nov). O dump não traz prêmio de exportação em Paranaguá, oferta argentina (principal concorrente) nem preços de praça.

*Lado da ração.* Sem milho nem proteína concorrente no briefing, não avalio a demanda via ração.

**O que INVALIDA / risco**
- **Repique do ratio**: fechamento do ratio acima de ~80,5–81% com farelo subindo mais que a soja desfaz o rompimento do piso; acima de ~82% encerra a tese de curto prazo.
- **Short squeeze técnico**: com ratio em 78,94% e farelo −4,6% na semana, um repique de 5–8 US$/sht pode ocorrer sem notícia (rebalanceamento de spread, fechamento de posições de fim de mês/semana).
- **NOPA** (fila `release-nopa-2026-10-31`): esmagamento mensal fraco reduziria a sobra e enfraqueceria a tese. O dump marca `monthly_status = 0` (paywall) — **sem número, não julgo**.
- **Qualidade de dado**: os fechamentos de dias anteriores já foram reescritos pelo robô em outros ciclos (o 29/10 do farelo apareceu como 335,40, 329,20 e agora 329,30 em briefings diferentes); uma nova revisão mudaria o ratio.

**Leitura operacional**
*Short:* a tese estrutural, o ratio comprimido e a liquidação em curso sustentam o viés, mas operar short de farelo *outright* a 324,70 depois de −4,6% em quatro pregões é entrar atrasado; prefiro a expressão em **spread contra o óleo** (long óleo/short farelo; ver Spreads) ou entradas em repiques para 328–330 (zona da abertura de 30/10 e máxima do dia). *Long:* só tático e curto, com gatilho no ratio recuperando 80,5%/81%; contra a tendência. O forecast do robô (7d central 311,54, faixa 296,82–326,26; 30d central 262,04) é extrapolação — **−19% em 30 dias não é sustentado pelo fundamento** e não o adoto; o alvo de curto prazo defensável é a região de 315–320.

*Filas tratadas:* `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` e `...-D+90`. A tese de junho partia de ratio 81,4%; hoje o ratio é 78,94% — o spread **seguiu comprimindo** (−2,5 pp) e agora rompeu o limiar de 80%. Direção da tese ("viés baixista no farelo contra a soja") **confirmada**; o ganho de preço não é verificável, pois o briefing não traz o preço do farelo em junho. Recomendo fechar as duas revisões (D+7 vencida em 18/06, D+90 vencida em 09/09) como "direção confirmada, resultado financeiro não verificável".

## Óleo

**Viés:** baixista **fraco**, confiança baixa-média. É a perna mais "teimosa": o fundamento (diesel) pressiona, mas o oil share e os índices sustentam.

**O que SUSTENTA a tese**

*Nível e momentum.* O óleo (ZLZ26, dez/26) fechou em **65,81 US¢/lb** em 30/10 (faixa 65,64–66,59), contra 65,64 (29/10), 65,56 (28/10), 66,71 (27/10) e 67,01 (26/10): −1,8% na semana, mas **lateral em 65,5–66** desde 28/10. Em 30/10 o óleo chegou a 66,59 e devolveu 0,78 US¢ até o fechamento: tentativa de alta rejeitada, o que mantém o viés baixista fraco (teto em ~66,6, piso em ~65,5).

*Curva a termo.* dez/26 65,81 · jan/27 66,07 · mar/27 66,55 · mai/27 66,93 · jul/27 67,02 (CBOT 2026-10-30): contango leve (+1,21 US¢, ou 1,8%, até julho). O mercado reconhece alguma sustentação futura (biocombustível), sem pagar prêmio imediato.

*Heating oil e margem de biodiesel — o fator dominante.* O heating oil (HO=F, diesel de aquecimento, "primo" fóssil do biodiesel) fechou em **4,655 US$/galão** em 30/10, contra 4,736 (29/10), 4,82 (28/10), 4,78 (27/10) e 4,91 (26/10): **−5,2% em cinco pregões**. Mecanismo: o biodiesel compete com o diesel; diesel barato exige óleo mais barato para o biodiesel continuar competitivo, o que enfraquece a demanda por óleo de soja. A margem de biodiesel dos EUA calculada pelo robô é de **US$ 2,0843/galão** (receita 7,82 = HO 4,66 + 1,5 × RIN 2,11; custo 5,74 = óleo 4,94 + 0,80 de custos industriais; `indicators` 2026-10-30), contra US$ 2,1780 em 29/10 e **US$ 2,2513 em 26/10** (−7,4%). A margem ainda é larga em termos absolutos — biodiesel americano segue rentável, sem sinal de colapso da demanda —, mas a direção é de piora e foi o heating oil que a puxou. **Ressalva:** o RIN está fixo em 2,11 em todos os dias, sugerindo que não é cotação diária; a *variação* da margem é confiável (vem de HO e óleo), o *nível* não.

*Oil share em 50,33% e Índice de Suporte do Óleo em 80/100.* O óleo agora vale **mais** que o farelo no crush (spread +0,0957 US$/bu). O Índice de Suporte do Óleo subiu de 60 para **80** ("óleo domina o crush, 4/5 condições", `indicators` 2026-10-31). Duas leituras: (a) o óleo está estruturalmente sustentado pelo biocombustível; (b) o complexo inteiro depende desse único vetor — se o óleo ceder, o oil share cai e a margem da indústria, também. Cuidado com a armadilha: o oil share sobe **porque o farelo cai**, não porque o óleo suba; "óleo sustentado" aqui é relativo ao farelo, não um sinal de alta de preço absoluto.

*Posicionamento dos fundos.* COT 27/10: managed money em óleo com **97.309 comprados, 36.978 vendidos, net long 60.331**, sobre OI de 573.736. Em 20/10: 104.484 / 32.966, net 71.518, OI 570.462. Variação: **−11,2 mil de net long (−15,6%)**, com compradores saindo (−7,2 mil) **e vendidos entrando (+4,0 mil)** — ao contrário da soja e do farelo, há venda nova (short) de fundo no óleo, e o OI subiu. A ponta comprada é ~17% do OI, bem mais moderada que a do farelo (~30%); logo o óleo é menos vulnerável a liquidação forçada, mas já tem fundo apostando contra. Swaps comprados em 98.096 contra 5.266 vendidos (compradores comerciais/índices de longo prazo, tipicamente estáveis).

*Demanda brasileira e oferta.* ABIOVE (projeções): produção de óleo de **494,9 mil t em nov/2026** e **415,2 mil t em dez/2026**; **exportação de apenas 21 mil t em novembro**; estoque final de **315,3 mil t** (nov) e **291,9 mil t** (dez). Brasil exporta quase nada de óleo: a produção fica no mercado interno, majoritariamente biodiesel. O óleo brasileiro é, por isso, muito mais sensível a **política de mistura** (B15/B16) do que ao mercado externo. A queda projetada de estoques em dezembro (−23 mil t) é viés levemente altista interno. O dump não traz basis nem preço de praça.

*Palma e demais fatores.* O parser do MPOB (palma da Malásia) não extraiu números em nenhum dos dias (`mpob`, 2026-10-31) — sem estoque/exportação de palma, principal substituto. Também sem RIN D4 diário nem diesel brasileiro.

*Fila tratada:* `alerta-quebra_suporte-oleo_cbot-2026-10-30` — fechou em 65,81, "abaixo do suporte 72,00". O nível está 8,6% acima do preço e foi rompido há tempos; o alerta apenas confirma que o óleo opera em patamar inferior ao da calibração. Não acrescenta informação nova; recomendo recalibrar.

**O que INVALIDA / risco**
- **Heating oil recuperando** para 4,80–4,90 (níveis de 27–28/10): reverte a pressão e leva o óleo de volta a ~67.
- **Anúncio do B16** (CNPE), sinal da EPA (RFS) ou do crédito 45Z nos EUA — gatilhos altistas mais fortes; nada no dump os confirma.
- **Fechamento do óleo abaixo de ~65,50** (mínima de 28/10 é 65,56) com HO caindo: abre espaço para 64–63,9.
- **Fechamento acima de ~66,60** (máxima de 30/10): invalida a rejeição e reabre 67.
- Forecast do robô: 7d central 64,95 (faixa 62,87–67,04), 30d central 61,87. A banda inclui o spot, compatível com lateralidade; espero **lateral-baixista em 64,5–66,6**, e não os −6% do central de 30d.

**Leitura operacional**
*Short:* o fluxo do diesel é favorável, mas o óleo resiste e já mostrou rejeição de alta, não de baixa; short *outright* tem convicção menor que o do farelo. *Long:* oil share >50%, margem de biodiesel acima de US$ 2/gal e Suporte do Óleo em 80 mostram demanda estrutural forte; entrada tática perto de 65,5 com stop abaixo de 65,0; o catalisador (B16, EPA, 45Z) precisa vir de fora. *Spread:* **long óleo / short farelo** é a expressão mais limpa da tese do complexo hoje.

## Spreads e crush (leitura de complexo)

*Crush margin.* **US$ 2,0425/bu** em 30/10 (farelo 324,70 + óleo 65,81 − soja 1.234,00; `indicators`), contra 2,1175 (29/10), 2,2170 (28/10), 2,2693 (27/10) e 2,3305 (26/10). Em quatro pregões perdeu **29 centavos (−12,4%)**, aceleração em relação ao ritmo de dias anteriores (−7,5 centavos só em 30/10). A fila trouxe `alerta-quebra_suporte-complexo_soja-2026-10-30` ("2,04 abaixo do suporte 2,50"): o fato é verdadeiro, mas o nível 2,50 é defasado (o crush está abaixo dele desde o início da janela, 2,33 em 26/10), então o alerta confirma uma margem em queda, sem informação nova de nível. Ainda assim US$ 2,04/bu é uma margem **alta** o suficiente para a indústria continuar moendo (ABIOVE: 2,63 milhões de t em novembro), de modo que a oferta de farelo e óleo continua chegando ao mercado — é isso que sustenta a pressão nos produtos. O risco de médio prazo é o reverso: margem em queda contínua eventualmente desacelera o esmagamento, o que seria o mecanismo natural de correção da sobra de farelo (mas não é gatilho para os próximos dias).

*Far/Soj (mean-reversion, os dois lados).* 78,94%, abaixo do piso de 80% pela primeira vez na janela de cinco pregões. Para **short do ratio** (short farelo/long soja): a tendência e a sobra favorecem, mas o prêmio restante diminuiu e a assimetria piora a cada décimo abaixo de 80%; entrar agora é seguir momentum, não capturar valor. Para **long do ratio** (long farelo/short soja): o ponto de entrada é bom pela média, mas vai contra o fundamento (sobra 100/100) e o fundo ainda está comprado (168 mil líquidos), então só vale com gatilho de confirmação (ratio voltando >80,5% com farelo subindo). Leitura: assimetria **desfavorável ao short do ratio e neutra a levemente favorável ao long tático**; não é gatilho de entrada, é aviso de risco de repique.

*Oil share e spread óleo−farelo.* Oil share **50,33%**, spread **+0,0957 US$/bu**: o óleo passa o farelo em valor no crush pela primeira vez na janela (era −0,1738 em 28/10). A virada veio do farelo caindo mais que o óleo. Isso é um ponto de **inflexão estrutural**, não de equilíbrio — ao contrário de ontem, em que o spread estava em zero. Qualquer tese de long óleo/short farelo agora é aposta de **continuidade**; o risco é que a continuidade já esteja precificada em parte.

*Os índices sintéticos juntos.* Sobra de Farelo **100** e Suporte do Óleo **80** (ambos subiram de 75 e 60 de 29/10 para 30–31/10). Dizem, juntos: "o farelo sobra com todas as condições acesas, e o óleo domina o crush com quatro das cinco". Consistente com oil share >50%, ratio <80% e spread positivo. Diferente de ontem, os índices mudaram e coincidem com o movimento de preço — mas índices de estado não dão timing, e nível máximo de um índice de pressão costuma coincidir com fase tardia da queda.

*Em conjunto.* Deriva baixista comum, com o **óleo/diesel como pivô**, o **farelo como perna mais frágil** e a soja como a mais estável. O crush em queda e o ratio abaixo de 80% dizem que o mercado já desconta bastante da sobra de farelo; o risco passa a ser **tático** (repique) mais do que estrutural. O melhor risco/retorno está no spread (long óleo/short farelo), e não nas pernas outright.

## Lente fiscal/regulatória BR

O monitor tributário (`system/tributario_watch.toml`) tem `atualizado_em = 2026-06-05` em todos os vetores — **quase cinco meses sem atualização**. Trago-os como registrados, **sem validação nova** (o briefing de hoje não traz seção do monitor).

- **MP 1.363/2026** — subvenção de R$ 1,12/L ao diesel fóssil, vigente até **31/12/2026** (status registrado "vigente"). Barateia o diesel dentro do mix B15, reduz a competitividade do biodiesel e a demanda interna por óleo de soja. Efeito **baixista para o óleo** e indiretamente para o farelo (menos esmagamento puxado por óleo). Coerente com a fraqueza do heating oil, embora aqui seja política e lá seja mercado. O risco de calendário: fim da vigência em dezembro (renovação ou caducidade); o fim seria altista para o biodiesel e o óleo.
- **MP 1.358/2026** — subvenção à gasolina/diesel, vigência até 11/07/2026; no catálogo está como "tramitação", mas o prazo venceu — desfecho (conversão ou caducidade) **não está no briefing**.
- **B16 (CNPE)** — mistura de biodiesel a 16%, **adiada**; os testes técnicos de seis meses teriam resultado perto de **nov/2026**; cada +1 pp de mistura puxaria ~436 mil t de óleo (registro do catálogo). Novembro é o próximo marco; **nada no dump indica convocação do CNPE**. Principal gatilho altista doméstico para o óleo e, indiretamente, para o farelo (mais esmagamento, mais sobra de proteína — efeito misto).
- **Isenção de PIS/Cofins do biodiesel** — prorrogada até 31/07/2026 (registro de junho); o que aconteceu depois **não consta**. **STJ REsp 2.165.276** (crédito de PIS/Cofins sobre soja em biodiesel, não vinculante): vetor de custo da cadeia, sem atualização.
- **EUA/Indonésia:** EPA RFS 2026/2027, crédito 45Z, Indonésia B50, levy de exportação de palma e Danantara — marcos no catálogo sem validação; são o principal potencial de sustentação externa do óleo, **mas não valido nenhum**.

Aplicação: o filtro fiscal vai no **sentido baixista para o óleo interno** (MP 1.363 vigente, B16 parado) e **neutro para a soja**. Não concluo mais que isso sem atualizar o catálogo. Em reais, o dólar a 5,42 mais do que compensa o efeito da queda do CBOT, de modo que a fraqueza do CBOT chega atenuada ao preço interno.

## Riscos e eventos próximos

- **WASDE (28/10)** — entrou na fila (`release-usda_wasde-2026-10-28`) como "coletado, ainda não interpretado", mas **o dump não traz o relatório em números**. Não consigo dizer se mexe no balanço (produtividade, estoques finais EUA, exportação). O que se sabe: o complexo caiu nos dois pregões seguintes (28 e 29/10) e em 30/10, o que é compatível com um WASDE sem surpresa altista — **inferência**, não fato.
- **NOPA** — a fila marca `release-nopa-2026-10-31` (coleta de hoje, sábado), mas o status é `monthly_status = 0` (paywall); o relatório mensal efetivo não está no briefing. Um esmagamento acima do esperado seria baixista para o farelo (mais sobra) e ambíguo para o óleo (mais oferta, mas também mais biodiesel). Não trato como informação até haver número.
- **COT:** próximo relatório (data-base 03/11) é o termômetro de se a liquidação continua. Atenção especial: net long de farelo (168,7 mil) e a entrada de short no óleo.
- **USDA Crop Progress:** próxima leitura de colheita EUA; já deve estar acima de 85%.
- **Fim de semana e segunda-feira:** o briefing de hoje reflete a sexta-feira (30/10). Gaps de abertura na segunda dependem de notícias de fim de semana não capturadas (sem RSS: 0 itens).
- **Diesel/heating oil:** pivô diário do óleo; repique para 4,80+ muda a leitura.
- **Novembro:** possível convocação do CNPE para o B16, evolução da safra sul-americana sob El Niño, e o prazo da MP 1.363 (31/12).
- **Datas de próximos WASDE/COT/NOPA:** são calendário regular de conhecimento geral, não confirmado no briefing.

## Honestidade

- **Sem WASDE e sem NOPA em números.** Os dois entram na fila como "coletado, não interpretado", mas o dump não os contém (NOPA: paywall). Qualquer afirmação sobre o balanço americano ou sobre o esmagamento mensal seria invenção; não faço.
- **Sem físico BR:** sem Paranaguá, basis, praças, CEPEA, sem exportação semanal dos EUA, sem palma (parser do MPOB falhou), sem notícias (`noticias_rss`: 0 itens lidos), sem milho/ração, sem RIN diário (valor fixo em 2,11) e sem percentil do COT.
- **Câmbio instável:** a série PTAX tem saltos suspeitos (5,0377 em 23/10 → 5,5007 em 26/10 → 5,3346 em 27/10; EUR/BRL 5,64 → 6,15 → 5,94). Uso o câmbio como direção (real mais fraco que na semana passada); a paridade em R$ 147,48/saca é aritmeticamente correta dado o PTAX, mas o PTAX pode estar errado.
- **Dados que mudam entre briefings:** nos dias anteriores houve reescrita dos fechamentos de 29/10 (farelo, óleo, ratio) e as barras de 30/10 mudaram de volume e extremos de um briefing para outro (ex.: volume do farelo em 30/10 era 1.528 e hoje é 68.188; a mínima do farelo era 328,30 e hoje é 324,40). A série "congelada" do robô parece corrigir-se ao longo do tempo; as conclusões de hoje dependem dos valores do briefing de 31/10, e um novo ajuste pode alterar o ratio (78,94%) e o crush.
- **Data do briefing:** 31/10/2026 é sábado; todos os preços são do pregão de sexta (30/10). Nenhum dado novo de mercado até segunda.
- **COT de 27/10** tem 4 dias; posições mudaram desde então. O percentil histórico não está no briefing, então não classifico posições como "extremas".
- **Níveis dos alertas da fila:** soja 1.180, óleo 72,00, crush 2,50 e PTAX 5,30 estão defasados em relação ao mercado atual — os alertas confirmam o fato, mas não trazem informação nova de direção.
- **Forecasts do robô:** extrapolação estatística (MA20 + volatilidade + inclinação). Os centrais de 30 dias (soja 1.106,11; farelo 262,04; óleo 61,87) implicam quedas de 10%, 19% e 6%, **não sustentadas** pelo fundamento disponível; mantive apenas a direção.
- **Inferências marcadas:** a leitura sobre o WASDE de 28/10 (sem surpresa altista) é inferência do comportamento de preço, não dado; o efeito do El Niño é regra geral de mercado, não do briefing.
- **Convicção geral:** baixa-média. A direção (baixista) é coerente entre soja, farelo e óleo; ratio comprimido, crush em queda, Sobra de Farelo em 100 e liquidação de fundos são fatos robustos no `indicators`/COT. O tamanho do movimento e o timing dependem de dados que não consegui validar.
