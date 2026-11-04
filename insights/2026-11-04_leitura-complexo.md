---
data: 2026-11-04
titulo: "Qua 04/11: o complexo desliza devagar nas três pernas (soja 1.207, farelo 316,40, óleo 64,87) com o crush estável em US$ 2,03/bu e o Far/Soj em 78,6%; o diesel NÃO desabou como parecia ontem (heating oil revisado para ~4,54, margem de biodiesel ~US$ 2,04) — farelo segue o elo mais fraco, óleo o pivô, soja a perna lenta; confiança baixa-média (volumes minúsculos e dados do dia aparentemente parciais)"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT via briefing 2026-11-04, sessão **2026-11-04** (volumes baixos, ver Honestidade). Soja ZSF27 (jan/27) abertura 1.212,50 · máxima 1.212,50 · mínima 1.206,25 · fechamento **1.207,00** US¢/bu (curva X26 1.195,50 · H27 1.214,50 · K27 1.224,25 · N27 1.232,75 · Q27 1.218,50). Farelo ZMZ26 (dez/26) abertura 317,50 · máxima 317,90 · mínima 316,10 · fechamento **316,40** US$/sht (F27 316,50 · H27 317,30 · K27 320,80 · N27 325,70 · Q27 326,00). Óleo ZLZ26 (dez/26) abertura 65,28 · máxima 65,37 · mínima 64,75 · fechamento **64,87** US¢/lb (F27 65,08 · H27 65,46 · K27 65,83 · N27 65,89 · Q27 65,56). Heating oil HO=F abertura 4,5700 · máxima 4,5709 · mínima 4,5342 · fechamento **4,5421** US$/gal
  - CME CBOT via briefing 2026-11-03 (versão revisada no dump de hoje) — farelo fechamento 317,60 · soja/óleo nos indicadores (1.213,50 e 65,26)
  - Indicadores do robô (`indicators`, 2026-10-29 a 2026-11-04) — crush margin, Far/Soj, oil share, spread óleo−farelo, margem de biodiesel EUA, índices de Sobra de Farelo e Suporte do Óleo, paridade BRL
  - BCB PTAX (sgs 1 e 21619) até **2026-11-03** (USD/BRL 5,4935 · EUR/BRL 6,15)
  - CFTC COT (managed money) data-base **2026-10-27** (último disponível no dump)
  - USDA Crop Progress **2026-11-01** (colheita de soja EUA 88%) e 2026-10-25 (79%)
  - ABIOVE projeções mensais nov/2026 e dez/2026
  - NOAA CPC (El Niño Advisory, 2026-11-04) e INMET 2026-11-04
  - Forecasts estatísticos do robô gerados em 2026-11-04 (7d e 30d)
  - `system/tributario_watch.toml` (vetores registrados, `atualizado_em = 2026-06-05`)
status: ativa
vies: [bear-soja, bear-farelo, bear-oleo_soja]
---

## Visão geral

Pense no complexo da soja como **uma fábrica**. A indústria compra o grão (soja), esmaga e vende dois produtos: o **farelo** (proteína para ração animal, cerca de três quartos do peso) e o **óleo** (alimentação e, cada vez mais, biodiesel). O que sobra para a fábrica é o **crush margin** (margem de esmagamento, em US$ por bushel — unidade de medida do grão, ~27 kg): valor do farelo + valor do óleo − preço da soja. Hoje ele é de **US$ 2,03/bu** (`indicators` 2026-11-04: 2,0265), praticamente igual a ontem (2,0308) e a 02/11 (2,0225), depois de ter vindo de 2,1175 em 29/10. Ou seja: a descida forte da semana passada **estacionou** em torno de US$ 2,00–2,05.

Quem manda nessa conta é o óleo, e isso é aritmética, não opinião. O **oil share** (fatia do óleo no valor total do esmagamento) está em **50,62%** (óleo US$ 7,14 de um total de US$ 14,10/bu). O óleo vale mais que o farelo porque tem uma demanda que o farelo não tem — o biodiesel, que cria um "piso" ligado ao diesel e a políticas de mistura. Consequência prática: a indústria mói soja **pelo óleo**, e o farelo sai junto como subproduto. Quando se mói muito pelo óleo, sobra farelo no mercado, e o que sobra fica barato. É o que o **ratio Far/Soj** mede: compara o valor de uma tonelada de farelo com o da soja que a originou. Hoje está em **78,64%**, abaixo do limiar de 80% que o robô chama de farelo "abundante" (≥ 87% seria "apertado"). Na prática: o farelo vale menos de 79% do grão que o gerou. Comprimido assim, o spread diz que o mercado já embute muita sobra; o risco passa a ser dos dois lados (a tendência empurra para baixo, a média histórica puxa para cima).

**O que mudou hoje (e uma correção de ontem):** (1) as três pernas recuaram de novo, pouco e em degraus — soja −0,5%, farelo −0,4%, óleo −0,6% contra 03/11 — e as três fecharam **perto da mínima do dia**, tom levemente vendedor; (2) o dump de hoje **revisou** o quadro de 03/11: o heating oil (diesel de aquecimento, "primo" fóssil do biodiesel) que ontem lia ~4,42 aparece agora nos indicadores a ~4,56 em 03/11 e **4,54 hoje**, e a margem de biodiesel dos EUA, que eu li ontem como 1,90, é **US$ 2,04/gal** hoje (2,03 em 03/11). O "desabamento do diesel" foi, em boa parte, uma queda concentrada em 02/11 (4,42) com **repique parcial** depois; o óleo de soja, portanto, não tem a "dívida de ajuste" que eu via ontem — a defasagem diesel→óleo é bem menor; (3) o **Índice de Sobra de Farelo** voltou a 75/100 (ontem eu lia 50), o que desfaz o sinal de esgotamento tático; (4) o **câmbio** ganhou dado novo: PTAX de 03/11 em **R$ 5,4935** (era 5,4212 em 30/10), real mais fraco, o que amortece em reais a queda do CBOT.

**Leitura de uma linha:** o pivô do complexo continua sendo o **óleo via biodiesel/diesel**; a maior convicção é **baixista no farelo** (sobra estrutural + ratio comprimido + fundo muito comprado), soja é a perna lenta e baixista fraca; confiança **baixa-média** (volumes do dia minúsculos, dados que o próprio dump revisa de um dia para o outro, sem WASDE/NOPA/físico em número).

## Soja

**Viés:** baixista **fraco** (de preço), confiança baixa-média.

**O que SUSTENTA a tese**

*Nível e momentum.* A soja de referência do robô (ZSF27, jan/27) fecha em **1.207,00 US¢/bu** em 04/11, contra 1.213,50 (03/11), 1.216,75 (02/11), 1.234,25 (30/10) e 1.234,75 (29/10) (`indicators`). Saldo: **−2,2% desde 30/10** e −6,5 centavos no dia, em degraus pequenos. A faixa de hoje foi de só 6,25 centavos (1.206,25–1.212,50), abertura na máxima e fechamento a 0,75 centavo da mínima: dia de venda lenta, sem pânico e sem volume (5.436 contratos). O contrato mais curto (nov/26, X26) fecha em **1.195,50**, abaixo do jan/27 — o dinheiro à vista está mais barato que o diferido.

*Curva a termo.* nov/26 1.195,50 · jan/27 1.207,00 · mar/27 1.214,50 · mai/27 1.224,25 · jul/27 1.232,75, com ago/27 recuando a 1.218,50 (CBOT 2026-11-04). Carry (prêmio dos meses futuros) de 37,25 US¢ entre nov e jul (3,1%): **contango**, o mercado paga para armazenar, sem escassez imediata. O recuo de ago/27 abaixo de jul/27 (−14,25) sugere expectativa de safra nova mais folgada. Curva assim é coerente com viés baixista fraco, não com corrida de alta.

*Colheita nos EUA.* USDA Crop Progress: **88% colhido em 01/11**, contra 79% em 25/10 (+9 pontos em uma semana). Colheita praticamente encerrada: o prêmio de risco do hemisfério norte desaparece e o que estava no campo virou oferta física. O briefing não traz média de cinco anos nem exportações semanais, então não digo se o ritmo é adiantado ou normal.

*Câmbio e paridade em reais — dado novo.* PTAX (BCB sgs 1): **5,4935 em 03/11**, contra 5,4212 (30/10), 5,3744 (29/10), 5,3420 (28/10), 5,3346 (27/10), 5,5007 (26/10) e 5,0377 (23/10). A paridade de exportação (CBOT × câmbio, sem basis) é **R$ 146,18/saca de 60 kg** hoje (`indicators` 2026-11-04), contra R$ 146,97 em 03/11 e R$ 147,51 em 30/10. Leitura: o CBOT perdeu 2,2% desde 30/10 mas a paridade em reais perdeu só ~0,9%, porque o real enfraqueceu +1,3% no período e compensou parte. Mecanismo: real fraco eleva o preço interno do produtor, estimula a venda e adiciona oferta, o que limita a recuperação do CBOT — e protege o preço em reais, reduzindo a dor do produtor (mais disposto a vender, menos a segurar). Uma checagem de qualidade: o EUR/BRL no mesmo dia foi 6,15 contra 5,6422 em 23/10, e a razão implícita EUR/USD (6,15 ÷ 5,4935 = 1,12) é a mesma de 23/10 (5,6422 ÷ 5,0377 = 1,12). Ou seja, o salto de ~9% do dólar contra o real entre 23 e 26/10 aparece de forma **consistente** nas duas séries e se sustentou por cinco prints seguidos entre 5,33 e 5,50 — é movimento do **real**, não do dólar globalmente, e não parece erro de coleta. Fila `alerta-quebra_resistencia-usd_brl_ptax-2026-11-03`: PTAX 5,49 acima da "resistência" 5,30. Fato verdadeiro e agora corroborado; o nível 5,30 virou piso do regime atual, não mais resistência.

*Posicionamento dos fundos.* COT (CFTC) de **27/10**: managed money (fundos) em soja com **226.215 comprados e 32.434 vendidos, net long 193.781**, sobre open interest (OI, contratos em aberto) de 979.414 — a ponta comprada é ~23% do OI e a razão comprado/vendido é de ~7:1. Na leitura anterior (insight de 03/11, COT de 20/10) o net era 221.325: **−27,5 mil (−12,4%)**, liquidação, não virada para vendido. Mecanismo: o fundo ainda tem muito a vender se o preço seguir caindo, mas parte da correção já ocorreu, o que explica a descida em degraus pequenos. Sem percentil histórico no briefing, digo "grande", não "extrema". Dado de oito dias atrás.

*Demanda e oferta BR.* ABIOVE (projeções mensais): esmagamento de **2.626,6 mil t em nov/2026** e **2.203,5 mil t em dez/2026** (−16%, entressafra); estoque de soja de 5.720,8 (início de nov) para 3.659,0 (fim de nov) e 1.889,9 mil t (fim de dez); exportação projetada de só 108 mil t em novembro. Safra velha escoando, oferta doméstica encurtando até a colheita nova — suporte sazonal no Brasil, que pouco influencia o CBOT. São *projeções*, não resultado.

*Clima.* NOAA CPC mantém **El Niño Advisory** (2026-11-04). Regra geral (conhecimento geral, não do briefing): El Niño tende a trazer chuva acima da média ao Sul do Brasil/Argentina e irregularidade no Norte/Nordeste. INMET (previsão de 04/11): Sorriso/MT máx. 36 °C e mín. 23 °C, Sinop/MT 37/24, Lucas do Rio Verde/MT 36/25, Cuiabá/MT 35/27, Rio Verde/GO 34/22, Maringá/PR 30/23, Cascavel/PR 31/20 e Passo Fundo/RS 28/17, todas com pancadas de chuva ou possibilidade de chuva isolada. Calor com chuva na fase inicial do plantio no Centro-Oeste é benigno; nada no dump indica estresse hídrico. Clima **não** sustenta prêmio de risco hoje.

**O que INVALIDA / risco**
- Fechamento do jan/27 **acima de ~1.234–1.235** (topo de 29–30/10) com volume real: devolve a tendência de antes da liquidação; 1.216–1.217 (02/11) é o primeiro teste.
- WASDE (relatório mensal de oferta/demanda do USDA) que corte estoque final — **não consigo avaliar**, o dump não traz o relatório.
- Falha climática no Centro-Oeste ou no sul argentino (o El Niño vira variável).
- Novo COT com recompra de fundos (risco de squeeze).
- Real voltando a ~5,05–5,30 reduz a paridade em reais e remove o amortecedor.

**Leitura operacional**
*Short:* tático e com alvos modestos. O forecast do robô (gerado 2026-11-04: 7d central 1.180,10, faixa 1.155,76–1.204,43; 30d central 1.078,12) é extrapolação de média móvel + volatilidade + inclinação; o spot (1.207,00) está **acima do topo** da banda de 7 dias, o que indica que a banda está esticada. **Não adoto −10,7% em 30 dias**; alvo defensável na região de 1.195–1.205 (X26 já em 1.195,50). *Long:* sem gatilho técnico ou fundamental; contra contango, colheita fechando e fundo ainda grande, exige stop curto (acima de ~1.235). O melhor uso da soja é como **perna do crush** (ver Spreads).

*Fila tratada:* `alerta-quebra_resistencia-soja_cbot-2026-11-04` — fechou em 1.207,00, "acima da resistência 1.180,00". O fato é verdadeiro, mas o nível está 2,2% abaixo do preço e defasado: o preço está acima da "resistência" *e* mesmo assim em queda de 2,2% em quatro pregões, o que mostra que o nível não descreve a dinâmica atual. Curiosamente 1.180 coincide com o centro do forecast de 7 dias; só vira informação se a soja o perder com volume. Recomendo recalibrar (fora do escopo desta camada).

## Farelo

**Viés:** baixista **moderado**, confiança média. Maior convicção do dia, com a ressalva de que o ratio já está comprimido e de que o dado de hoje parece parcial.

**O que SUSTENTA a tese**

*Nível e momentum.* O farelo (ZMZ26, dez/26) fecha em **316,40 US$/sht** (short ton, 907 kg) em 04/11 (faixa 316,10–317,90), contra 317,60 (03/11), 319,60 (02/11), 324,60 (30/10) e 329,30 (29/10): **−3,9% em quatro pregões**, a maior queda do complexo. O preço foi arrastando para baixo em degraus de 1–5 dólares, sem a liquidação em bloco de 02/11 e sem repique. Fechar a 0,30 da mínima do dia reforça o tom vendedor, mas o volume reportado (1.758 contratos) é o mesmo número exato de ontem, e máxima/mínima do dia (317,90/316,10) idênticas às de 03/11 — ver Honestidade: o retrato do farelo hoje pode ser um molde parcial, não um dia completo.

*Curva a termo.* dez/26 316,40 · jan/27 316,50 · mar/27 317,30 · mai/27 320,80 · jul/27 325,70 · ago/27 326,00 (CBOT 2026-11-04): carry de ~9,3 US$/sht até jul (2,9%). Em proteína apertada o prompt seria mais caro que o diferido; aqui é o oposto — a curva é quase plana nos primeiros 3 meses e sobe depois, sem prêmio de escassez.

*Ratio Far/Soj em 78,64%.* Série (`indicators`): 80,01% (29/10), 78,90% (30/10), 78,80% (02/11), 78,52% (03/11), **78,64% (04/11)**. Quinto pregão seguido na zona de 78–79% e o terceiro dia abaixo de 80% sem ainda aceleração: o ratio subiu 0,12 ponto hoje porque a soja caiu (−0,5%) um pouco mais que o farelo (−0,4%) — ruído, não reversão. A matemática do ratio ajuda a dimensionar o risco: com a soja em 1.207 (US$ 12,07/bu), o farelo "valeria" ~321,8 a 80% de ratio, ~325,9 a 81% e ~329,9 a 82% (conta minha sobre a fórmula do robô; ratio = farelo ÷ (soja em US$/bu × 33,33)). Ou seja, para o ratio voltar a 80,5% sem mexer na soja, o farelo precisaria subir ~2,3% (para ~323,8). Isso dá a régua do repique tático.

*Oil share e spread óleo−farelo.* Oil share **50,62%** e spread **+0,1749 US$/bu** (04/11), contra 50,68% / +0,1914 (03/11), 50,45% / +0,1276 (02/11) e 50,37% / +0,1078 (30/10). Hoje o spread **encolheu** (−0,0165) porque o óleo caiu mais (−0,60%) que o farelo (−0,38%): primeiro pregão em que a perna "óleo" cede mais, ainda que pouco. O óleo segue valendo mais que o farelo (US$ 7,14 contra 6,96/bu); a ordem de grandeza mostra o quanto o complexo gira em torno do biocombustível. (Conhecimento geral, não do briefing: historicamente o óleo costuma responder por fatia menor que a metade do crush; quando passa de 50%, é sinal de regime com demanda de biodiesel forte.)

*Índice de Sobra de Farelo.* **75/100** em 04/11 ("sobra relevante, 3/4 condições", `indicators`), igual a 03/11 (versão revisada) e 02/11, e abaixo dos 100 de 30–31/10 (4/4 condições). O briefing não detalha qual condição apagou, então **não invento causa**. Leitura: a tese estrutural segue em pé, mas sem a pressão máxima de 30/10; é o nível que permite manter viés baixista sem alarme de saturação. (Ontem eu lia 50 para 03/11; o dump atual mostra 75 — a série foi revista, e eu uso a nova.)

*Posicionamento dos fundos.* COT 27/10: managed money em farelo com **184.371 comprados e 15.657 vendidos, net long 168.714**, sobre OI de 609.960 — ponta comprada ~30% do OI e razão comprado/vendido de ~11,8:1, a posição **mais unilateral do complexo**. Na leitura anterior (COT de 20/10, citado no insight de 03/11) o net era 200.878: **−32,2 mil (−16,0%)**, ou seja, compradores já saindo. Produtores/indústria têm 387.753 vendidos contra 69.776 comprados (hedge) e swaps 133.898 comprados contra 13.251 vendidos. Interpretação: posição de fundo grande e unilateral numa proteína que o fundamento diz estar sobrando — receita clássica de liquidação continuada; como o preço caiu mais depois da data-base (de 324,60 para 316,40), o COT vivo provavelmente já está mais liquidado. Limitação: oito dias de defasagem, sem percentil.

*Oferta e exportação BR.* ABIOVE (projeções): produção de farelo de **1.977,6 mil t em nov/2026** e **1.659,0 mil t em dez/2026**; exportação de 800 mil t (nov) e 700 mil t (dez); estoque final **1.101,4 mil t** (nov, inicial 1.100,1) e **1.015,5 mil t** (dez). Conta minha sobre as linhas do dump: estoque inicial + produção − exportação − estoque final implica consumo doméstico de ~1.176 mil t em novembro e ~1.045 mil t em dezembro (−11%). O estoque fica estável em novembro e cai 86 mil t em dezembro — oferta brasileira estável a levemente apertada no fim do ano, insuficiente para compensar a sobra via esmagamento forte (2,63 milhões de t de soja em nov). O dump não traz prêmio de exportação em Paranaguá, oferta argentina, nem praças. Sem milho nem proteína concorrente, não avalio a demanda via ração.

**O que INVALIDA / risco**
- **Repique do ratio**: fechamento acima de ~80,5–81% com farelo subindo mais que a soja (farelo > ~324–326 com soja estável) desfaz o rompimento; acima de ~82% (~330) encerra a tese de curto prazo.
- **Short squeeze técnico**: após −3,9% em quatro pregões e com fundo ainda comprado, há espaço para repique de 5–8 US$/sht (322–326) sem notícia.
- **NOPA** (esmagamento mensal dos EUA, fila `release-nopa-2026-11-04`): esmagamento fraco reduziria a sobra; forte a aumentaria. O dump marca `monthly_status = 0` (paywall) — **sem número, não julgo**.
- **Qualidade de dado**: volume idêntico ao de ontem e faixa idêntica; uma revisão do fechamento muda o ratio.

**Leitura operacional**
*Short:* tese estrutural + ratio comprimido + fundo ainda comprado sustentam; mas short outright a 316,40, depois de −3,9%, é entrar com o movimento já feito — prefiro entradas em repiques para 322–326 (stop acima de ~330) ou a expressão em **spread contra o óleo** (long óleo/short farelo; ver abaixo). *Long:* só tático e curto, com gatilho no ratio recuperando 80,5%/81%; contra a tendência e contra o fundamento. Forecast do robô (2026-11-04: 7d central 302,03, faixa 288,62–315,44; 30d central 247,67): o spot está **acima** do topo da banda de 7 dias e o central de 30d (−21,7%) **não é sustentado pelo fundamento** — mantenho só a direção, alvo de curto prazo 308–315.

*Filas tratadas:* `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` e `...-D+90`. A tese de junho partia de ratio 81,4%; hoje 78,64% — o spread **seguiu comprimindo** (~−2,8 pontos) e está abaixo de 80% desde 30/10 (resposta ao D+7, "ratio fechou <80%?": sim, só em 30/10, bem depois da janela de 18/06; ao D+90, "o spread reverteu ou seguiu comprimindo?": seguiu). Direção **confirmada**; ganho de preço não verificável, pois o briefing não traz o preço do farelo em junho, nem WASDE/NOPA em número. Recomendo encerrar as duas revisões como "direção confirmada, resultado financeiro não verificável". O D+90 venceu em 09/09; a leitura é tardia, não nova.

## Óleo

**Viés:** baixista **fraco**, confiança baixa-média. Perna mais "teimosa": oil share e Suporte do Óleo seguram, a margem de biodiesel segue larga, mas o diesel enfraqueceu e o fundo está saindo.

**O que SUSTENTA a tese**

*Nível e momentum.* O óleo (ZLZ26, dez/26) fecha em **64,87 US¢/lb** em 04/11 (faixa 64,75–65,37), contra 65,26 (03/11, versão revista), 65,08 (02/11), 65,90 (30/10) e 65,64 (29/10): −1,6% desde 30/10, **lateral em 65–66 e agora furando levemente para baixo** (64,87 é o menor fechamento da janela de seis pregões). Abertura em 65,28 e fechamento perto da mínima (0,12 acima) — dia vendedor no óleo, o mais "limpo" dos três. Piso a testar: 64,75 (mínima de hoje).

*Curva a termo.* dez/26 64,87 · jan/27 65,08 · mar/27 65,46 · mai/27 65,83 · jul/27 65,89 · ago/27 65,56 (CBOT 2026-11-04): contango leve (+1,02 US¢, 1,6% até julho). Reconhece alguma sustentação futura (biocombustível) sem pagar prêmio imediato.

*Heating oil e margem de biodiesel — o fator dominante, agora com a correção.* O heating oil fechou em **4,5421 US$/galão** em 04/11 (faixa 4,5342–4,5709), contra ~4,56 em 03/11 e ~4,42 em 02/11 (ambos inferidos da receita de biodiesel nos `indicators`, HO = receita − 1,5 × RIN 2,11), 4,79 em 30/10 e 4,74 em 29/10. O quadro correto, portanto: o diesel caiu forte em **02/11** (−0,37 contra 30/10), repicou em 03/11 (+0,14) e está estável agora (−0,02). Diesel −5,2% sobre 30/10, não os −7,7% ou pior que eu apontava ontem. (A linha crua do heating oil de 03/11 no dump está truncada; leio o valor só pelos indicadores.)

Mecanismo: o biodiesel compete com o diesel; diesel barato exige óleo mais barato para o biodiesel continuar competitivo. A **margem de biodiesel** dos EUA (`indicators` 2026-11-04) é **US$ 2,0418/galão** (receita 7,71 = HO 4,54 + 1,5 × RIN 2,11; custo 5,67 = óleo 4,87 + 0,80 industrial), contra 2,0281 em 03/11, 1,9056 em 02/11 e 2,213 em 30/10: queda de 17 centavos (−7,7%) desde 30/10, com **recuperação parcial desde o fundo de 02/11**. Decomposição: o HO perdeu 25 centavos de receita; o óleo, ao cair 1,03 US¢/lb (7,5 lb por galão = 7,7 centavos de custo), devolveu só um terço. Ressalva: o RIN (crédito de combustível renovável) está fixo em 2,11 todos os dias (provavelmente não é cotação diária); a *variação* da margem é confiável (vem de HO e óleo), o *nível* não. Para a margem voltar a 2,213 com HO a 4,54, o óleo precisaria cair para ~62,6 US¢/lb (conta minha com as premissas do robô: 7,7071 − 0,80 − 2,213 = 4,694/gal ÷ 7,5 lb). São −2,3 US¢/lb (−3,5%), perto do centro do forecast de 7 dias (64,04) e da base da banda (62,02). Trato como referência do "gap" restante, não previsão: o mercado não precisa restaurar a margem anterior. Com margem acima de US$ 2,00/gal e o óleo custando 4,87 do galão, não há sinal de que a demanda de biodiesel desligue.

*Oil share 50,62% e Suporte do Óleo 80/100.* O óleo vale mais que o farelo no crush (spread +0,1749 US$/bu) e o Índice de Suporte do Óleo está em **80** ("óleo domina o crush, 4/5 condições", `indicators`), estável de 30/10 a 04/11. Duas leituras: (a) o óleo é estruturalmente sustentado pelo biocombustível; (b) o complexo inteiro depende desse vetor — se o óleo ceder, oil share e margem caem juntos. Armadilha: o oil share subiu na semana **porque o farelo caiu**, não porque o óleo subisse; "sustentado" é relativo ao farelo, não sinal de alta absoluta. Sensibilidade útil: 1 US¢/lb no óleo = US$ 0,11/bu no crush (~5% da margem de 2,03); US$ 10/sht no farelo = US$ 0,22/bu.

*Posicionamento dos fundos.* COT 27/10: managed money em óleo com **97.309 comprados, 36.978 vendidos, net long 60.331**, OI 573.736 — ponta comprada ~17% do OI, razão ~2,6:1, a mais equilibrada do complexo. Leitura anterior (COT de 20/10): net 71.518, ou seja **−11,2 mil (−15,6%)**, com compradores saindo e **vendidos entrando** — diferente de soja e farelo, há venda nova de fundo no óleo. Menos vulnerável a liquidação forçada, porém já há aposta contra. O recuo do diesel posterior à data-base provavelmente aprofundou essa tendência.

*Demanda e oferta BR.* ABIOVE (projeções): produção de óleo de **494,9 mil t em nov/2026** e **415,2 mil t em dez/2026**; **exportação de apenas 21 mil t em novembro** (o dump não traz exportação de óleo para dezembro); estoque de 306,4 mil t (início de nov) → **315,3 mil t** (fim de nov) → **291,9 mil t** (fim de dez). Conta minha: consumo doméstico implícito de ~465 mil t em novembro e ~439 mil t em dezembro (assumindo exportação nula). O Brasil exporta quase nada de óleo: a produção fica no mercado interno, majoritariamente biodiesel, tornando o óleo brasileiro muito mais sensível a **política de mistura** (B15/B16) do que ao mercado externo. A queda de estoque em dezembro é viés levemente altista interno. Sem basis nem praça no dump.

*Palma e demais.* O parser do MPOB (palma da Malásia, principal substituto do óleo de soja) não extraiu números em nenhum dia da janela (`mpob`, 2026-11-04) — sem estoque/exportação de palma. Sem RIN D4 diário nem diesel brasileiro.

**O que INVALIDA / risco**
- **Heating oil** recuperando para 4,70+ em pregão com volume: leva a margem de biodiesel de volta acima de ~2,15 e dá combustível ao óleo.
- **B16 (CNPE), sinal da EPA (RFS) ou crédito 45Z** nos EUA — gatilhos altistas fortes; nada no dump os confirma.
- **Fechamento do óleo abaixo de ~64,75** (mínima de hoje) com HO caindo: abre espaço para 63–64.
- **Fechamento acima de ~65,90–66,00** (topo de 30/10): invalida a lateralidade baixista e reabre 67.
- Forecast do robô (2026-11-04): 7d central 64,04 (faixa 62,02–66,07), 30d central 60,89 (−6,1%). A banda de 7d inclui o spot; espero **lateral-baixista em 64,0–66,0**, não os −6% de 30d.

**Leitura operacional**
*Short:* o argumento é mais modesto que ontem. Diesel 5% abaixo de 30/10 e fundo vendendo dão fundamento direcional, mas o óleo está em 64,87 com margem de biodiesel acima de 2,00 e o suporte de 64,75 logo abaixo; short outright de baixa convicção, entrada em repique para ~65,3–65,6, stop acima de 65,9. *Long:* oil share > 50%, margem larga e Suporte do Óleo em 80 mostram demanda estrutural; entrada tática perto de 64,75–64,90 com stop curto abaixo de 64,3; o catalisador (B16, EPA, 45Z) precisa vir de fora. A expressão long óleo / short farelo tem a perna "óleo" menos confortável que na semana passada, mas hoje não pior que ontem.

*Fila tratada:* `alerta-quebra_suporte-oleo_cbot-2026-11-04` — fechou em 64,87, "abaixo do suporte 72,00". O nível está 11% acima do preço e foi rompido há tempos; confirma que o óleo opera abaixo da calibração, sem informação nova. Recomendo recalibrar.

## Spreads e crush (leitura de complexo)

*Crush margin.* **US$ 2,0265/bu** em 04/11 (farelo 316,40 + óleo 64,87 − soja 1.207,00; `indicators`), contra 2,0308 (03/11), 2,0225 (02/11), 2,0477 (30/10) e 2,1175 (29/10): ~−9 centavos (−4,3%) em quatro pregões e **estável há três**. Os três preços caem na mesma proporção (soja −0,5%, farelo −0,4%, óleo −0,6% no dia), então o diferencial que forma a margem quase não mexe: queda de preços de modo geral, não compressão específica da indústria. Fila `alerta-quebra_suporte-complexo_soja-2026-11-04` ("2,03 abaixo do suporte 2,50"): fato verdadeiro, mas o nível 2,50 é defasado; confirma margem em queda desde o início da série sem informação nova de nível. US$ 2,03/bu ainda é margem **alta** o bastante para a indústria seguir moendo (ABIOVE: 2,63 milhões de t em novembro), logo a oferta de farelo e óleo continua chegando, o que sustenta a pressão nos produtos. O mecanismo de correção de longo prazo é o inverso: margem em queda desacelera o esmagamento e reduz a sobra de farelo (não é gatilho para os próximos dias).

*Far/Soj (mean-reversion, os dois lados).* 78,64%. **Short do ratio** (short farelo/long soja): tendência, sobra e fundo comprado favorecem, mas o prêmio já foi coletado em boa parte; entrar agora é seguir momentum, não capturar valor. **Long do ratio** (long farelo/short soja): bom ponto pela média (precisaria de +2,3% no farelo para 80,5%), mas contra o fundamento e contra um fundo comprado (168,7 mil líquidos em 27/10); só com confirmação (ratio > 80,5% com farelo subindo). Leitura: assimetria **desfavorável a entrar no short do ratio agora e neutra a levemente favorável ao long tático**; aviso de risco de repique, não gatilho.

*Oil share e spread óleo−farelo.* 50,62% e +0,1749 US$/bu: óleo à frente do farelo, mas o spread encolheu hoje pela primeira vez na janela (de +0,1914). Long óleo/short farelo é aposta de **continuidade** e parte já pode estar precificada; com o diesel ainda abaixo de 30/10 e o fundo vendendo óleo, o lado "óleo" não tem apoio externo forte, enquanto o lado "farelo" tem a sobra. Spread continua preferível às pernas soltas, com a perna long menos confortável.

*Índices sintéticos juntos.* Sobra de Farelo **75** e Suporte do Óleo **80**: "o farelo sobra de forma relevante (3 de 4 condições) e o óleo domina o crush (4 de 5)". Ambos estáveis há quatro dias (Sobra em 75 desde 01/11, Suporte em 80 desde 30/10): o complexo está em **regime estável**, e quem decide entradas é o preço do dia, não o índice (índices de estado não dão timing).

*Em conjunto.* Deriva baixista lenta e comum, **óleo/diesel como pivô**, **farelo como perna mais frágil**, soja como a mais estável. Crush a 2,03 e ratio a 78,6% dizem que o mercado já desconta boa parte da sobra; o risco passa a ser **tático** (repique no farelo, ajuste do óleo ao diesel) mais que estrutural.

## Lente fiscal/regulatória BR

O monitor tributário (`system/tributario_watch.toml`) tem `atualizado_em = 2026-06-05` — **cinco meses sem atualização**; o briefing de hoje não traz seção do monitor. Trago os vetores como registrados, **sem validação nova**.

- **MP 1.363/2026** — subvenção de R$ 1,12/L ao diesel fóssil, vigente até **31/12/2026**. Barateia o diesel dentro do mix B15, reduz a competitividade do biodiesel e a demanda interna por óleo de soja: efeito **baixista para o óleo** e, indiretamente, para o farelo (menos esmagamento puxado por óleo). Risco de calendário: fim da vigência em dezembro seria altista para biodiesel e óleo.
- **MP 1.358/2026** — subvenção à **gasolina** (R$ 0,89/L), vigência até 11/07/2026; catalogada como "tramitação" e com prazo vencido — desfecho **não consta no briefing**. Efeito sobre soja é indireto (etanol/mix de combustíveis).
- **B16 (CNPE)** — mistura a 16%, **adiada** no catálogo; cada +1 ponto percentual de mistura puxaria ~436 mil t de óleo (registro do catálogo). **Nada no dump indica convocação do CNPE.** Principal gatilho altista doméstico para o óleo; para o farelo, efeito misto (mais esmagamento = mais proteína sobrando).
- **PIS/Cofins do biodiesel** — isenção registrada até 31/07/2026; o que veio depois **não consta**. **STJ REsp 2.165.276** (crédito de PIS/Cofins sobre soja em biodiesel, não vinculante): custo da cadeia, sem atualização.
- **EUA/Indonésia:** EPA RFS 2026/2027, crédito 45Z, Indonésia B50 e levy de exportação de palma (PMK 9/2026) — marcos do catálogo sem validação; seriam o principal potencial de sustentação externa do óleo, mas **não valido nenhum**.

Aplicação: filtro fiscal no sentido **baixista para o óleo interno** (MP 1.363 vigente, B16 parado) e **neutro para a soja**; não concluo além disso sem atualizar o catálogo. Em reais, o dólar a R$ 5,49 (PTAX de 03/11) atenua a fraqueza do CBOT no preço interno, como visto na paridade (R$ 146,18/saca).

## Riscos e eventos próximos

- **NOPA** — fila `release-nopa-2026-11-04`: o robô registra "release novo", mas o relatório mensal está atrás de paywall e o dump marca `monthly_status = 0` — **sem número, não trato como informação**. Esmagamento acima do esperado seria baixista para o farelo e ambíguo para o óleo (mais óleo ofertado, mas demanda forte de esmagamento). Referência: a mesma mensagem aparece todos os dias da janela, então "release novo" aqui é só a data do robô.
- **WASDE** — sem números no dump; não avalio.
- **COT** (CFTC): próxima divulgação, normalmente sexta-feira com data-base terça (conhecimento geral, não confirmado no briefing); mostra se a liquidação continuou após a queda de 02/11. Atenção ao net long de farelo (168,7 mil em 27/10) e à entrada de short no óleo.
- **USDA Crop Progress:** colheita de soja nos EUA em 88% (01/11); a próxima leitura praticamente encerra o tema.
- **Diesel/heating oil:** pivô diário do óleo; 4,42 (02/11) e 4,70 são as fronteiras que importam.
- **PTAX:** novo dado em 03/11 (5,4935); acompanhar se o real estabiliza em 5,3–5,5 ou volta a 5,0–5,3.
- **Novembro/dezembro:** possível convocação do CNPE (B16), safra sul-americana sob El Niño, fim da MP 1.363 (31/12).
- Datas de próximos WASDE/COT/NOPA são calendário regular de conhecimento geral, não confirmado no briefing.

## Honestidade

- **Dados do dia parecem parciais.** Volumes de 04/11 minúsculos (soja 5.436, farelo 1.758, óleo 5.249, heating oil 332 contratos). Pior: o farelo de hoje tem **volume (1.758), máxima (317,90) e mínima (316,10) idênticos aos de 03/11**, e a abertura de ontem era 317,50 como a de hoje — sugere que o retrato intradiário está sendo reaproveitado e que o fechamento (316,40) pode ser parcial. Os indicadores de hoje foram calculados sobre esses números.
- **O dump revisa o passado.** O que eu li ontem para 03/11 (soja 1.219,50; farelo 319,50; óleo 65,14; HO 4,4218; margem de biodiesel 1,90; Índice de Sobra 50) difere do que o dump de hoje mostra para 03/11 (soja 1.213,50 nos indicadores; farelo 317,60; óleo 65,26; HO ~4,56 e margem 2,03 inferidos; Sobra 75). Uso os valores novos e desfaço a narrativa de "diesel em colapso". Mas isso reforça que **fechamentos recentes são instáveis** e minha leitura pode se revisar de novo amanhã.
- **Heating oil de 03/11:** a linha crua está truncada no dump; o valor (~4,56) é inferido por mim dos `indicators` (receita − 1,5 × RIN 2,11). O de 02/11 (~4,42) idem.
- **Sem WASDE e sem NOPA em número.** Qualquer afirmação sobre balanço americano ou esmagamento mensal seria invenção.
- **Sem físico BR:** sem Paranaguá, basis, praças, CEPEA, exportação semanal EUA, palma (MPOB falhou), notícias (0 itens lidos), milho/ração, RIN diário (fixo 2,11) e percentil do COT.
- **Câmbio:** agora há PTAX de 03/11, mas a paridade de 04/11 usa esse mesmo câmbio com o CBOT de hoje; a série teve salto de 9% em 23→26/10 que a checagem EUR/BRL sugere real, mas que não consigo confirmar por fonte independente.
- **Selic:** o campo `selic_diaria` mostra 0,050788 rotulado "% a.a."; a magnitude é de taxa **diária**. Não uso.
- **Aritmética minha, não indicador do briefing:** preço do óleo que restauraria a margem de biodiesel (~62,6), farelo equivalente a 80/81/82% de ratio (~321,8/325,9/329,9), consumo doméstico implícito da ABIOVE, sensibilidades por US¢/lb e por US$/sht.
- **Causa da mudança do Índice de Sobra** (100 → 75): não identificada; não especulo.
- **COT de 27/10** tem oito dias; as variações semanais citadas vêm do COT de 20/10 registrado no meu insight de 03/11, não do dump de hoje.
- **Níveis dos alertas da fila** (soja 1.180, óleo 72,00, crush 2,50, PTAX 5,30) estão defasados; confirmam fatos sem direção nova.
- **Forecasts do robô** (soja 30d 1.078,12; farelo 247,67; óleo 60,89) implicam −10,7%, −21,7% e −6,1%, **não sustentados** pelo fundamento; para soja e farelo o spot já está acima do topo da banda de 7 dias. Mantive só a direção.
- **Inferências marcadas:** efeito do El Niño e padrão histórico do oil share são conhecimento geral. Fiscal: catálogo de junho, sem atualização.
- **Convicção geral:** baixa-média. Direção baixista coerente nas três pernas; ratio comprimido, crush ~2,03 estável, fundo grande liquidando e diesel mais fraco que em 30/10 são fatos robustos em `indicators`/COT. Tamanho e timing dependem de dados que não consegui validar.
