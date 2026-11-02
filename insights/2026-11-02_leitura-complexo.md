---
data: 2026-11-02
titulo: "Seg 02/11 (preços de soja, farelo e óleo ainda são o fechamento de sex 30/10; só o heating oil tem leitura nova, e é mais fraca): farelo segue o elo mais fraco (Far/Soj 78,9%, 'comprimido'), óleo é o pivô via diesel, soja cai devagar; confiança baixa-média"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT via briefing 2026-11-02 — sessão **2026-10-30**. Soja ZSF27 (jan/27) abertura 1.234,50 · máxima 1.242,00 · mínima 1.230,75 · fechamento **1.234,25** US¢/bu (curva X26 1.222,25 · H27 1.243,75 · K27 1.253,50 · N27 1.260,25 · Q27 1.245,50). Farelo ZMZ26 (dez/26) abertura 329,30 · máxima 330,30 · mínima 324,40 · fechamento **324,60** US$/sht (F27 325,20 · H27 327,00 · K27 330,80 · N27 335,30 · Q27 334,70). Óleo ZLZ26 (dez/26) abertura 65,66 · máxima 66,65 · mínima 65,64 · fechamento **65,90** US¢/lb (F27 66,17 · H27 66,63 · K27 67,01 · N27 67,11 · Q27 66,74)
  - Heating oil HO=F (CME/CBOT via briefing) sessões 2026-11-02 (fech. 4,6117 · abertura 4,6746 · mín. 4,6093 · volume 517), 2026-11-01 (fech. 4,6106 · volume 411) e 2026-10-30 (fech. 4,7905 · máx. 4,8572 · volume 16.221)
  - Indicadores do robô (`indicators`, 2026-10-26 a 2026-11-02) — crush margin, Far/Soj, oil share, spread óleo−farelo, margem de biodiesel EUA, índices de Sobra de Farelo e Suporte do Óleo, paridade BRL
  - BCB PTAX (sgs 1 e 21619) 2026-10-19 a **2026-10-30** (USD/BRL 5,4212)
  - CFTC COT (managed money) data-base **2026-10-27** e 2026-10-20
  - USDA Crop Progress 2026-10-25 (colheita de soja EUA 79%)
  - ABIOVE projeções mensais nov/2026 e dez/2026
  - NOAA CPC (El Niño Advisory, 2026-11-02) e INMET 2026-11-02
  - Forecasts estatísticos do robô gerados em 2026-11-02 (7d e 30d)
  - `system/tributario_watch.toml` (vetores registrados, `atualizado_em = 2026-06-05`)
status: ativa
vies: [bear-soja, bear-farelo, bear-oleo_soja]
---

## Visão geral

Hoje é segunda-feira, 02/11, e o briefing chega **sem pregão novo de soja, farelo e óleo**: os preços desses três continuam sendo o fechamento de sexta, 30/10 (o dump só traz heating oil para 01 e 02/11). Isso importa para a leitura: o que "mudou" hoje não é preço do complexo, e sim (i) o heating oil, que aparece mais baixo, e (ii) a fila de julgamento. Qualquer conclusão sobre a abertura de hoje seria especulação.

Para quem não acompanha o dia a dia: pense no complexo da soja como **uma fábrica**. A indústria compra o grão (soja), esmaga e vende dois produtos, o **farelo** (proteína para ração) e o **óleo** (alimentação e, cada vez mais, biodiesel). A margem da fábrica é o **crush margin** (margem de esmagamento): valor do farelo + valor do óleo − custo da soja, por bushel (unidade de medida do grão, cerca de 27 kg). Em 30/10 ela foi de **US$ 2,05/bu** (`indicators` 2026-10-30: 2,0477), contra US$ 2,33 em 26/10 (2,3305): **−12,1% em quatro pregões**. A margem encolhe porque os produtos caíram mais que o insumo: no intervalo a soja perdeu 1,5% (1.252,50 → 1.234,25 US¢/bu), o óleo 1,7% (67,01 → 65,90 US¢/lb) e o farelo **4,6%** (340,20 → 324,60 US$/short ton).

Quem manda no crush é o óleo, por aritmética: o **oil share** (fatia do óleo no valor total gerado pelo esmagamento) está em **50,37%** (óleo 7,25 de um total de 14,39 US$/bu, `indicators` 2026-10-30). O óleo paga metade da conta porque tem uma demanda que o farelo não tem: biocombustíveis. Consequência: a indústria esmaga soja *pelo óleo*, e o farelo, que sai junto como subproduto, **sobra**; e o que sobra fica barato. O **ratio Far/Soj** mede isso: compara o valor de uma tonelada de farelo com o da soja que a originou. Em 30/10 está em **78,9%**, abaixo do limiar de 80% que o robô chama de farelo "abundante" (≥87% seria "apertado"). Na prática, o farelo vale menos de 79% do grão que o gerou (fila `ratio-zona-2026-10-30`; era 80,0% na véspera), e o óleo vale mais que o farelo dentro da fábrica (spread óleo−farelo +0,1078 US$/bu).

O que há de novo hoje: o **heating oil** (diesel de aquecimento, "primo" fóssil do biodiesel) fechou em **4,6117 US$/galão** em 02/11, contra 4,7905 em 30/10 (**−3,7%**). Cautela: os volumes de 01 e 02/11 são ínfimos (411 e 517 contratos, contra 16.221 em 30/10), típicos de sessão sem negociação real; trato como **sinal fraco** até o pregão cheio confirmar. Se confirmado, é pressão adicional sobre o óleo de soja (diesel barato exige óleo mais barato para o biodiesel competir). Os índices do robô seguem: **Sobra de Farelo 75/100** e **Suporte do Óleo 80/100** (`indicators` 2026-11-02), ambos iguais a 01/11.

**Leitura de uma linha:** o pivô do complexo continua sendo o **óleo (via diesel/biocombustível)**; a maior convicção é **baixista no farelo** (sobra estrutural + ratio comprimido), a soja é a perna lenta e estável; confiança **baixa-média** (direção coerente nas três pernas, mas sem preço novo, sem WASDE/NOPA em número e com câmbio instável).

## Soja

**Viés:** baixista **fraco** (de preço), confiança baixa-média. A perna mais estável: cai pouco, devagar e com amortecimento do câmbio em reais.

**O que SUSTENTA a tese**

*Nível e momentum.* A soja (ZSF27, jan/27) fechou em **1.234,25 US¢/bu** em 30/10, contra 1.234,75 (29/10), 1.238,00 (28/10), 1.243,00 (27/10) e 1.252,50 (26/10) — `indicators`. São cinco degraus pequenos, −1,5% acumulado. Em 30/10 a amplitude foi de 11,25 centavos (1.230,75–1.242,00) e o fechamento ficou praticamente na abertura (1.234,50): houve tentativa de alta até 1.242,00 que foi vendida de volta. Mecanismo: mercado que sobe no intraday e devolve tudo indica vendedor em cima, seja oferta física da colheita, seja fundo reduzindo exposição.

*Curva a termo.* nov/26 1.222,25 · jan/27 1.234,25 · mar/27 1.243,75 · mai/27 1.253,50 · jul/27 1.260,25, com ago/27 recuando a 1.245,50 (CBOT 2026-10-30). Carry de 38 US¢ entre nov e jul (3,1%): **contango**, o mercado paga para armazenar, ou seja, não há escassez imediata. O recuo de ago/27 abaixo de jul/27 sugere expectativa de safra nova mais folgada. Curva assim combina com viés baixista fraco, não com corrida de alta.

*Colheita nos EUA.* USDA Crop Progress: **79% colhido em 25/10**. Colheita avançada elimina o prêmio de risco do hemisfério norte: o que estava no campo virou oferta física. O briefing não traz média de cinco anos nem exportações semanais, então não digo se 79% é adiantado ou normal.

*Câmbio e paridade em reais.* PTAX USD/BRL **5,4212 em 30/10**, contra 5,3744 (29/10), 5,3420 (28/10) e 5,0377 em 23/10 (BCB sgs 1). Paridade de exportação **R$ 147,51/saca de 60 kg** (CBOT 1.234,25 × 5,4212, sem basis; `indicators` 2026-10-30), contra R$ 146,30 em 29/10 e R$ 145,80 em 28/10. O CBOT caiu, mas o dólar mais caro **mais do que compensou** em reais. Mecanismo: o produtor brasileiro recebe em dólar; real mais fraco eleva o preço interno e estimula a venda, o que adiciona oferta e limita a recuperação do CBOT, mas amortece a queda para o produtor. Fila `alerta-quebra_resistencia-usd_brl_ptax-2026-10-30`: PTAX (5,42) acima da "resistência" de 5,30. O fato é real na série, mas o nível está defasado e a série tem saltos suspeitos (5,0377 em 23/10 → 5,5007 em 26/10, +9,2% num pregão útil; EUR/BRL 5,64 → 6,15); uso o câmbio como **direção**, não como número exato.

*Posicionamento dos fundos.* COT (CFTC) de **27/10**: managed money (fundos) em soja com **226.215 comprados e 32.434 vendidos, net long 193.781**, sobre open interest (OI, contratos em aberto) de 979.414. Em 20/10: 259.970 / 38.645, net 221.325, OI 1.093.612. Variação: **−27,5 mil de net long (−12,4%)** e OI −10,4%: liquidação clássica, fundo vendendo posição comprada e saindo, não virando vendido. A ponta comprada ainda é ~23% do OI, grande. Mecanismo: ainda há combustível de queda, mas parte já foi queimada, o que explica a queda lenta. Sem percentil histórico no briefing: digo "grande em termos absolutos", não "extrema".

*Demanda e oferta BR.* ABIOVE (projeções mensais): esmagamento de **2.626,6 mil t em nov/2026** e **2.203,5 mil t em dez/2026**; estoque de soja caindo de 5.720,8 (início de nov) para 3.659,0 (fim de nov) e 1.889,9 mil t (fim de dez); exportação projetada de apenas 108 mil t em novembro. Leitura: safra velha sendo consumida, oferta doméstica ficando curta no fim do ano, suporte sazonal à soja no Brasil. São *projeções*, não resultado.

*Clima.* NOAA CPC mantém **El Niño Advisory** (2026-11-02). Regra geral de mercado (conhecimento geral, não do briefing): El Niño tende a favorecer chuva no Sul do Brasil/Argentina e irregularidade no Norte/Nordeste. INMET 02/11: Sorriso/MT máx. 38 °C, Sinop/MT 37 °C, Lucas do Rio Verde/MT e Cuiabá/MT 36 °C, Rio Verde/GO 31 °C, Maringá/PR 32 °C (granizo possível), Cascavel/PR 29 °C (granizo possível), Passo Fundo/RS 24 °C, com pancadas em quase todas as praças. Chuva no Centro-Oeste na fase de plantio/emergência é benigna; granizo no PR/RS é risco localizado, não sistêmico. Nada no dump indica estresse hídrico; clima **não** sustenta prêmio de risco hoje.

**O que INVALIDA / risco**
- Fechamento da soja **acima de ~1.252** (máxima de 26/10) com volume: devolve a tendência da semana.
- Número de WASDE (relatório mensal do USDA) que reduza estoques finais — **não consigo avaliar**, o dump não traz o relatório.
- Falha climática no Centro-Oeste ou no sul argentino (o El Niño vira variável).
- COT de 03/11: nova liquidação forte reforça a tese; recompra indica risco de squeeze.
- Real forte devolve pressão ao preço interno em reais.

**Leitura operacional**
*Short:* tático, alvos modestos. O forecast do robô (gerado 2026-11-02: 7d central 1.206,50, faixa 1.182,82–1.230,18; 30d central 1.106,39) é extrapolação de média móvel + volatilidade + inclinação; o topo da banda de 7 dias (1.230,18) já está abaixo do spot. **Não adoto −10% em 30 dias**; alvo defensável na região de 1.200–1.210. *Long:* sem gatilho técnico nem fundamental; contra contango, colheita fechando e fundo ainda grande, exige stop curto (acima de 1.242, máxima de 30/10). O melhor uso da soja é como **perna do crush** (ver Spreads).

*Fila tratada:* `alerta-quebra_resistencia-soja_cbot-2026-10-30` — fechou em 1.234,25, "acima da resistência 1.180,00". O nível está 4,6% abaixo do preço; o alerta não muda a tese. Recomendo recalibrar o nível (tarefa fora do escopo desta camada).

## Farelo

**Viés:** baixista **moderado**, confiança média. Maior convicção do dia, com a ressalva de que o ratio já está comprimido e o Índice de Sobra recuou de 100 para 75 desde 31/10.

**O que SUSTENTA a tese**

*Nível e momentum.* O farelo (ZMZ26, dez/26) fechou em **324,60 US$/sht** em 30/10 (faixa 324,40–330,30), contra 329,30 (29/10), 335,70 (28/10), 334,60 (27/10) e 340,20 (26/10): **−4,6% em cinco pregões**, a maior queda do complexo. Em 30/10 abriu em 329,30 e fechou praticamente na mínima (324,60 vs 324,40): fechar na mínima é padrão de pressão vendedora que persiste.

*Curva a termo.* dez/26 324,60 · jan/27 325,20 · mar/27 327,00 · mai/27 330,80 · jul/27 335,30 · ago/27 334,70 (CBOT 2026-10-30): carry de ~10,70 US$/sht em sete meses (3,3%). Em proteína apertada o prompt seria mais caro que o diferido; aqui é o oposto, sem prêmio de escassez.

*Ratio Far/Soj em 78,9% — gatilho da fila.* Série (`indicators`): 81,35% (28/10), 80,01% (29/10), **78,9% (30/10)** (26/10 e 27/10: 81,49% e 80,76%, pelo briefing anterior e pelos preços do dump). Pela primeira vez na janela fecha abaixo de 80% (trata fila `ratio-zona-2026-10-30`). Isso faz duas coisas. Primeiro, **confirma** que o farelo está barato em relação ao grão por causa da sobra (óleo pagando o crush). Segundo, reduz o prêmio de quem opera short do ratio: quanto mais baixo, mais perto da zona em que o farelo "barato demais" atrai demanda de ração e desestimula esmagamento só pelo óleo. Em mean-reversion (retorno à média), abaixo de 80% o risco fica bilateral: tendência e sobra empurram para baixo, a média puxa para cima. Ainda não há evidência de reversão.

*Oil share e spread óleo−farelo.* Oil share **50,37%** e spread **+0,1078 US$/bu** (30/10), contra −0,1738 em 28/10 e −0,0242 em 29/10. O spread virou positivo: óleo vale mais que farelo no crush pela primeira vez na janela. Quanto mais o óleo manda, mais o farelo é subproduto.

*Índice de Sobra de Farelo.* **75/100** em 01 e 02/11 (3/4 condições, "sobra relevante", `indicators`), depois de 100/100 em 30 e 31/10 (4/4). É o mesmo patamar de 26–29/10. O briefing não detalha qual condição apagou, então **não invento causa**. Leitura prudente: a tese estrutural continua, mas o selo de "pressão máxima" não vale mais, um argumento de cautela contra short farelo outright depois de −4,6%.

*Posicionamento dos fundos.* COT 27/10: managed money em farelo com **184.371 comprados e 15.657 vendidos, net long 168.714**, sobre OI de 609.960 (ponta comprada ~30% do OI). Em 20/10: 213.717 / 12.839, net 200.878, OI 635.401. Variação: **−32,2 mil de net long (−16,0%)**, compradores saindo (−29,3 mil) e vendidos crescendo pouco (+2,8 mil). Produtores/indústria têm 387.753 vendidos contra 69.776 comprados (hedge) e swaps 133.898 comprados contra 13.251 vendidos. Interpretação: posição de fundo **grande e unilateral** numa proteína que o fundamento diz estar sobrando; a liquidação já começou. Se o preço seguir recuando, os longs restantes alimentam a queda (quase não há short de fundo para recomprar e amortecer). Limitação: dado de 27/10, sem percentil.

*Oferta e exportação BR.* ABIOVE (projeções): produção de farelo de **1.977,6 mil t em nov/2026** e **1.659,0 mil t em dez/2026**; exportação de 800 mil t (nov) e 700 mil t (dez); estoque final de **1.101,4 mil t** (nov, inicial 1.100,1) e **1.015,5 mil t** (dez). Estoque quase estável em novembro e −86 mil t em dezembro: oferta brasileira estável a levemente apertada no fim do ano, insuficiente para compensar a sobra via esmagamento forte (2,63 milhões de t de soja em nov). O dump não traz prêmio de exportação em Paranaguá, oferta argentina, nem praças.

*Ração.* Sem milho nem proteína concorrente no briefing, não avalio a demanda via ração.

**O que INVALIDA / risco**
- **Repique do ratio**: fechamento acima de ~80,5–81% com farelo subindo mais que a soja desfaz o rompimento; acima de ~82% encerra a tese de curto prazo.
- **Short squeeze técnico**: com ratio em 78,9% e −4,6% na semana, repique de 5–8 US$/sht pode ocorrer sem notícia (rebalanceamento, virada de mês).
- **NOPA** (esmagamento mensal dos EUA, fila `release-nopa-2026-11-02`): esmagamento fraco reduziria a sobra. O dump marca `monthly_status = 0` (paywall) — **sem número, não julgo**.
- **Qualidade de dado**: fechamentos de 30/10 foram reescritos pelo robô mais de uma vez (ver Honestidade); nova revisão muda o ratio.

**Leitura operacional**
*Short:* tese estrutural + ratio comprimido + liquidação em curso sustentam, mas short de farelo *outright* a 324,60 após −4,6% é entrar atrasado, e o Índice de Sobra em 75 pede disciplina; prefiro a expressão em **spread contra o óleo** (long óleo/short farelo) ou entradas em repiques para 328–330 (abertura e máxima de 30/10). *Long:* só tático e curto, com gatilho no ratio recuperando 80,5%/81%; contra a tendência. Forecast do robô (2026-11-02: 7d central 311,44, faixa 296,71–326,18; 30d central 261,93): **−19% em 30 dias não é sustentado pelo fundamento** e não o adoto; alvo de curto prazo defensável 315–320.

*Filas tratadas:* `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` e `...-D+90`. A tese de junho partia de ratio 81,4%; hoje 78,9% — o spread **seguiu comprimindo** (~−2,5 pp) e rompeu o limiar de 80% (resposta à pergunta do D+7, "ratio fechou <80%?": sim, em 30/10, bem depois da janela de 18/06; a do D+90, "reverteu ou seguiu comprimindo?": seguiu). Direção **confirmada**; ganho de preço não verificável, pois o briefing não traz o preço do farelo em junho, nem WASDE/NOPA em número. Recomendo fechar as duas revisões como "direção confirmada, resultado financeiro não verificável".

## Óleo

**Viés:** baixista **fraco**, confiança baixa-média. A perna mais "teimosa": o diesel pressiona, mas oil share, margem de biodiesel e o índice de suporte seguram.

**O que SUSTENTA a tese**

*Nível e momentum.* O óleo (ZLZ26, dez/26) fechou em **65,90 US¢/lb** em 30/10 (faixa 65,64–66,65), contra 65,64 (29/10), 65,56 (28/10), 66,71 (27/10) e 67,01 (26/10): −1,7% na semana, mas **lateral em 65,5–66** desde 28/10, e 30/10 fechou *acima* de 29/10. Chegou a 66,65 e devolveu 0,75 US¢: tentativa de alta rejeitada. Teto ~66,65, piso ~65,5.

*Curva a termo.* dez/26 65,90 · jan/27 66,17 · mar/27 66,63 · mai/27 67,01 · jul/27 67,11 · ago/27 66,74 (CBOT 2026-10-30): contango leve (+1,21 US¢, 1,8% até julho). O mercado reconhece alguma sustentação futura (biocombustível) sem pagar prêmio imediato.

*Heating oil e margem de biodiesel — fator dominante e o dado novo de hoje.* O heating oil fechou em **4,6117 US$/galão** em 02/11 (4,6106 em 01/11), contra **4,7905 em 30/10**, 4,736 (29/10), 4,82 (28/10), 4,78 (27/10) e 4,91 (26/10): **−6,1% desde 26/10 e −3,7% sobre a sexta**. Ressalva importante: 01 e 02/11 negociaram 411 e 517 contratos (sexta: 16.221), então o preço é de sessão rala; pode ser ruído de livro vazio, não consenso de mercado. Mecanismo geral: o biodiesel compete com o diesel; diesel barato exige óleo mais barato para o biodiesel continuar competitivo. Faço uma conta de sensibilidade, **não dado do briefing**: com o RIN e o custo industrial fixos como no robô (RIN 2,11 ×1,5; 0,80), um HO de 4,61 (−0,18 vs sexta) reduziria a receita do biodiesel em ~0,18 US$/gal, levando a margem de US$ 2,213 para algo perto de US$ 2,03 com o óleo parado em 65,90. Segue larga. A margem oficial do robô em 30/10 é **US$ 2,213/galão** (receita 7,96 = HO 4,79 + 1,5 × RIN 2,11; custo 5,74 = óleo 4,94 + 0,80; `indicators`), contra 2,178 em 29/10, 2,2632 em 28/10 e 2,2513 em 26/10. **Ressalva:** o RIN fica fixo em 2,11 todos os dias (provavelmente não é cotação diária); a *variação* da margem é confiável (vem de HO e óleo), o *nível* não.

*Oil share 50,37% e Suporte do Óleo 80/100.* O óleo vale mais que o farelo no crush (spread +0,1078 US$/bu) e o Índice de Suporte do Óleo está em **80** ("óleo domina o crush, 4/5 condições", `indicators`), estável de 30/10 a 02/11. Duas leituras: (a) o óleo é estruturalmente sustentado pelo biocombustível; (b) o complexo inteiro depende desse vetor — se o óleo ceder, oil share e margem caem juntos. Armadilha: o oil share sobe **porque o farelo cai**, não porque o óleo suba; "sustentado" aqui é relativo ao farelo, não sinal de alta absoluta.

*Posicionamento dos fundos.* COT 27/10: managed money em óleo com **97.309 comprados, 36.978 vendidos, net long 60.331**, OI 573.736. Em 20/10: 104.484 / 32.966, net 71.518, OI 570.462. Variação: **−11,2 mil de net long (−15,6%)**, compradores saindo (−7,2 mil) **e vendidos entrando (+4,0 mil)** — diferente de soja e farelo, há venda nova de fundo no óleo, e o OI subiu. Ponta comprada ~17% do OI, bem mais moderada que no farelo (~30%): menos vulnerável a liquidação forçada, mas já há fundo apostando contra. Swaps comprados em 98.096 contra 5.266 vendidos.

*Demanda e oferta BR.* ABIOVE (projeções): produção de óleo de **494,9 mil t em nov/2026** e **415,2 mil t em dez/2026**; **exportação de apenas 21 mil t em novembro**; estoque de 306,4 mil t (início de nov) → **315,3 mil t** (fim de nov) → **291,9 mil t** (fim de dez). O Brasil exporta quase nada de óleo: a produção fica no mercado interno, majoritariamente biodiesel. O óleo brasileiro é muito mais sensível a **política de mistura** (B15/B16) do que ao mercado externo. A queda de estoque em dezembro (−23 mil t) é viés levemente altista interno. Sem basis nem praça no dump.

*Palma e demais.* O parser do MPOB (palma da Malásia) não extraiu números em nenhum dia (`mpob`, 2026-11-02) — sem estoque/exportação de palma, principal substituto. Sem RIN D4 diário nem diesel brasileiro.

**O que INVALIDA / risco**
- **Heating oil** recuperando para 4,90+ (nível de 26/10) em pregão com volume: reverte a pressão e leva o óleo a ~67.
- **B16 (CNPE), sinal da EPA (RFS) ou crédito 45Z** nos EUA — gatilhos altistas fortes; nada no dump os confirma.
- **Fechamento do óleo abaixo de ~65,50** (mínima de 28/10 é 65,56) com HO caindo: abre espaço para 64–63,9.
- **Fechamento acima de ~66,65** (máxima de 30/10): invalida a rejeição e reabre 67.
- Forecast do robô (2026-11-02): 7d central 65,04 (faixa 62,94–67,14), 30d central 61,97. A banda inclui o spot, compatível com lateralidade; espero **lateral-baixista em 64,5–66,7**, não os −6% do central de 30d.

**Leitura operacional**
*Short:* o HO mais baixo em 02/11 dá um argumento a mais para viés de baixa na abertura, mas é sinal ralo (517 contratos), e o óleo mostrou rejeição de alta, não de baixa, na semana; short *outright* tem convicção menor que no farelo. *Long:* oil share >50%, margem de biodiesel acima de US$ 2/gal e Suporte do Óleo em 80 mostram demanda estrutural forte; entrada tática perto de 65,5 com stop abaixo de 65,0; o catalisador (B16, EPA, 45Z) precisa vir de fora. *Spread:* **long óleo / short farelo** continua a expressão mais limpa da tese.

*Fila tratada:* `alerta-quebra_suporte-oleo_cbot-2026-10-30` — fechou em 65,90, "abaixo do suporte 72,00". O nível está 9% acima do preço e foi rompido há tempos; confirma que o óleo opera abaixo da calibração, sem informação nova. Recomendo recalibrar.

## Spreads e crush (leitura de complexo)

*Crush margin.* **US$ 2,0477/bu** em 30/10 (farelo 324,60 + óleo 65,90 − soja 1.234,25; `indicators`), contra 2,1175 (29/10), 2,2170 (28/10), 2,2693 (27/10) e 2,3305 (26/10): −28 centavos (−12,1%) em quatro pregões, −7 centavos só em 30/10. Fila `alerta-quebra_suporte-complexo_soja-2026-10-30` ("2,05 abaixo do suporte 2,50"): fato verdadeiro, mas o nível 2,50 é defasado (o crush já estava em 2,33 em 26/10), então confirma margem em queda sem informação nova de nível. US$ 2,05/bu ainda é margem **alta** o bastante para a indústria seguir moendo (ABIOVE: 2,63 milhões de t em novembro), logo a oferta de farelo e óleo continua chegando, o que sustenta a pressão nos produtos. O risco de médio prazo é o reverso: margem em queda contínua desacelera o esmagamento, o mecanismo natural de correção da sobra de farelo (não é gatilho para os próximos dias).

*Far/Soj (mean-reversion, os dois lados).* 78,9%, abaixo do piso de 80% pela primeira vez na janela. **Short do ratio** (short farelo/long soja): tendência e sobra favorecem, mas o prêmio restante diminuiu; entrar agora é seguir momentum, não capturar valor. **Long do ratio** (long farelo/short soja): bom ponto pela média, mas contra o fundamento e contra um fundo ainda comprado (168 mil líquidos); só com confirmação (ratio voltando >80,5% com farelo subindo). Leitura: assimetria **desfavorável ao short do ratio e neutra a levemente favorável ao long tático**; é aviso de risco de repique, não gatilho de entrada.

*Oil share e spread óleo−farelo.* 50,37% e +0,1078 US$/bu: óleo passa o farelo no crush pela primeira vez na janela (era −0,1738 em 28/10). Ponto de **inflexão estrutural**. Long óleo/short farelo agora é aposta de **continuidade**, e parte dela já pode estar precificada. Com o HO em queda, o lado "óleo" do spread perde um pouco de suporte externo; o lado "farelo" continua com a sobra. O spread continua preferível às pernas soltas, mas com a perna long menos confortável que na semana passada.

*Índices sintéticos juntos.* Sobra de Farelo **75** e Suporte do Óleo **80**: "o farelo sobra (3 de 4 condições) e o óleo domina o crush (4 de 5)". Índices de estado não dão timing.

*Em conjunto.* Deriva baixista comum, **óleo/diesel como pivô**, **farelo como perna mais frágil**, soja como a mais estável. Crush em queda e ratio <80% dizem que o mercado já desconta boa parte da sobra; o risco passa a ser **tático** (repique) mais que estrutural.

## Lente fiscal/regulatória BR

O monitor tributário (`system/tributario_watch.toml`) tem `atualizado_em = 2026-06-05` — **quase cinco meses sem atualização**; o briefing de hoje não traz seção do monitor. Trago os vetores como registrados, **sem validação nova**.

- **MP 1.363/2026** — subvenção de R$ 1,12/L ao diesel fóssil, vigente até **31/12/2026** (status registrado "vigente"). Barateia o diesel dentro do mix B15, reduz a competitividade do biodiesel e a demanda interna por óleo de soja: efeito **baixista para o óleo** e indiretamente para o farelo (menos esmagamento puxado por óleo). Risco de calendário: fim da vigência em dezembro; o fim seria altista para biodiesel e óleo.
- **MP 1.358/2026** — subvenção com vigência até 11/07/2026; catalogada como "tramitação" mas o prazo já venceu — desfecho **não consta no briefing**.
- **B16 (CNPE)** — mistura a 16%, **adiada**; testes técnicos de seis meses teriam resultado perto de **nov/2026** (estamos nele); cada +1 pp de mistura puxaria ~436 mil t de óleo (registro do catálogo). **Nada no dump indica convocação do CNPE.** Principal gatilho altista doméstico para o óleo; para o farelo, efeito misto (mais esmagamento = mais proteína sobrando).
- **PIS/Cofins do biodiesel** — isenção prorrogada até 31/07/2026 (registro de junho); o que veio depois **não consta**. **STJ REsp 2.165.276** (crédito de PIS/Cofins sobre soja em biodiesel, não vinculante): custo da cadeia, sem atualização.
- **EUA/Indonésia:** EPA RFS 2026/2027, crédito 45Z, Indonésia B50, levy de exportação de palma — marcos do catálogo sem validação; seriam o principal potencial de sustentação externa do óleo, mas **não valido nenhum**.

Aplicação: filtro fiscal no sentido **baixista para o óleo interno** (MP 1.363 vigente, B16 parado) e **neutro para a soja**; não concluo além disso sem atualizar o catálogo. Em reais, o dólar a 5,42 atenua a fraqueza do CBOT no preço interno.

## Riscos e eventos próximos

- **Abertura de hoje (02/11):** o briefing não traz soja/farelo/óleo de segunda; `noticias_rss` traz 0 itens (sem notícias). O HO ralo já sinaliza um viés de abertura mais fraco para o óleo, mas é inferência. Virada de mês pode gerar rebalanceamento.
- **NOPA** — fila `release-nopa-2026-11-02`: o robô registra "release novo", mas o relatório mensal está atrás de paywall e não há número no dump. Esmagamento acima do esperado seria baixista para o farelo e ambíguo para o óleo. **Não trato como informação até haver número.**
- **WASDE** — sem números no dump; não avalio.
- **COT** (data-base 03/11): mostra se a liquidação continua; atenção ao net long de farelo (168,7 mil) e à entrada de short no óleo.
- **USDA Crop Progress:** próxima leitura da colheita nos EUA (último dado: 79% em 25/10).
- **Diesel/heating oil:** pivô diário do óleo; precisa de pregão com volume para confirmar os 4,61.
- **Novembro:** possível convocação do CNPE (B16), safra sul-americana sob El Niño, MP 1.363 (31/12).
- Datas de próximos WASDE/COT/NOPA são calendário regular de conhecimento geral, não confirmado no briefing.

## Honestidade

- **Sem preço novo de soja, farelo e óleo:** tudo vem de 30/10. O único dado de 01 e 02/11 é o heating oil, com volume de poucas centenas de contratos; não o trato como pregão confirmado.
- **Dados reescritos:** os volumes de 30/10 no briefing de hoje (soja 115.283, farelo 68.188, óleo 63.997) diferem dos do briefing anterior (180.972, 111.076, 92.601); o HO de 30/10 vale 4,7905 em ambos. Preços de fechamento batem; volume não é evidência utilizável.
- **Sem WASDE e sem NOPA em número.** Qualquer afirmação sobre balanço americano ou esmagamento mensal seria invenção.
- **Sem físico BR:** sem Paranaguá, basis, praças, CEPEA, exportação semanal EUA, palma (MPOB falhou), notícias, milho/ração, RIN diário (fixo 2,11) e percentil do COT.
- **Câmbio instável:** saltos suspeitos na série PTAX (5,0377 → 5,5007 → 5,3346 entre 23 e 27/10). A paridade de R$ 147,51/saca é aritmética correta dado o PTAX, mas o PTAX pode estar errado. Último PTAX é de 30/10.
- **Cálculo de sensibilidade da margem de biodiesel** com HO 4,61 é minha aritmética sobre as premissas fixas do robô, não indicador do briefing.
- **Causa da oscilação do Índice de Sobra** (100 → 75): não identificada; não especulo.
- **COT de 27/10** tem 6 dias; posições mudaram desde então.
- **Níveis dos alertas da fila** (soja 1.180, óleo 72,00, crush 2,50, PTAX 5,30) estão defasados; os alertas confirmam fatos sem direção nova.
- **Forecasts do robô** (soja 30d 1.106,39; farelo 261,93; óleo 61,97) implicam −10%, −19% e −6%, **não sustentados** pelo fundamento; mantive só a direção.
- **Inferências marcadas:** efeito do El Niño é regra geral, não dado do briefing. Fiscal: catálogo de junho, sem atualização.
- **Convicção geral:** baixa-média. Direção baixista coerente nas três pernas; ratio comprimido, crush em queda e liquidação de fundos são fatos robustos em `indicators`/COT. Tamanho e timing dependem de dados que não consegui validar.
