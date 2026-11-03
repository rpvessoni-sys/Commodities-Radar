---
data: 2026-11-03
titulo: "Ter 03/11: o diesel (heating oil) desaba para ~4,42 e leva a margem de biodiesel de US$ 2,21 para 1,90/gal; crush cai a US$ 2,00/bu e Far/Soj vai a 78,6% — farelo segue o elo mais fraco, óleo é o pivô (lateral em 65, mas sem o apoio do diesel), soja cai devagar; confiança baixa-média (preços de 03/11 com volume ralo, provavelmente parciais)"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT via briefing 2026-11-03, sessão **2026-11-03** (volume baixo, ver Honestidade). Soja ZSF27 (jan/27) abertura 1.217,00 · máxima 1.219,50 · mínima 1.216,00 · fechamento **1.219,50** US¢/bu (curva X26 1.205,50 · H27 1.228,50 · K27 1.238,75 · N27 1.247,00 · Q27 1.233,25). Farelo ZMZ26 (dez/26) abertura 320,30 · máxima 320,50 · mínima 319,00 · fechamento **319,50** US$/sht (F27 319,90 · H27 321,20 · K27 325,50 · N27 330,70 · Q27 330,90). Óleo ZLZ26 (dez/26) abertura 65,12 · máxima 65,25 · mínima 64,96 · fechamento **65,14** US¢/lb (F27 65,35 · H27 65,82 · K27 66,21 · N27 66,34 · Q27 65,96)
  - CME CBOT via briefing 2026-11-02 — farelo abertura 324,60 · máxima 326,00 · mínima 318,80 · fechamento 319,60 · volume 74.254
  - Heating oil HO=F 2026-11-03 (abertura 4,6746 · máxima 4,4488 · mínima 4,4052 · fechamento **4,4218** · volume 700)
  - Indicadores do robô (`indicators`, 2026-10-28 a 2026-11-03) — crush margin, Far/Soj, oil share, spread óleo−farelo, margem de biodiesel EUA, índices de Sobra de Farelo e Suporte do Óleo, paridade BRL
  - BCB PTAX (sgs 1 e 21619) até **2026-10-30** (USD/BRL 5,4212)
  - CFTC COT (managed money) data-base **2026-10-27** e 2026-10-20
  - USDA Crop Progress **2026-11-01** (colheita de soja EUA 88%) e 2026-10-25 (79%)
  - ABIOVE projeções mensais nov/2026 e dez/2026
  - NOAA CPC (El Niño Advisory, 2026-11-03) e INMET 2026-11-03/04
  - Forecasts estatísticos do robô gerados em 2026-11-03 (7d e 30d)
  - `system/tributario_watch.toml` (vetores registrados, `atualizado_em = 2026-06-05`)
status: ativa
vies: [bear-soja, bear-farelo, bear-oleo_soja]
---

## Visão geral

Hoje, terça-feira 03/11, há **pregão novo** nas três pernas (diferente de ontem, quando só o heating oil tinha leitura nova), mas com uma ressalva: os volumes de 03/11 são minúsculos (soja 12.351 contratos, farelo 1.503, óleo 2.357, contra 74.254 do farelo em 02/11), o que sugere um retrato **parcial ou intradiário** do dia, que pode ser reescrito. Trato os números como direção, não como fechamento definitivo.

Para quem não acompanha o dia a dia: pense no complexo da soja como **uma fábrica**. A indústria compra o grão (soja), esmaga e vende dois produtos: o **farelo** (proteína para ração animal) e o **óleo** (alimentação e, cada vez mais, biodiesel). A margem da fábrica é o **crush margin** (margem de esmagamento): valor do farelo + valor do óleo − custo da soja, por bushel (unidade de medida do grão, cerca de 27 kg). Hoje ela é de **US$ 2,00/bu** (`indicators` 2026-11-03: 1,9994), contra 2,0225 em 02/11 e 2,0477 em 30/10. Contra 26/10 (2,3305), a perda é de **−14,2%** em seis pregões. A margem encolhe porque os produtos caem mais que o insumo: desde 26/10 a soja perdeu 2,6% (1.252,50 → 1.219,50 US¢/bu), o óleo 2,8% (67,01 → 65,14 US¢/lb) e o farelo **6,1%** (340,20 → 319,50 US$/short ton).

Quem manda no crush é o óleo, por aritmética: o **oil share** (fatia do óleo no valor total do esmagamento) está em **50,48%** (óleo 7,17 de um total de 14,19 US$/bu, `indicators` 2026-11-03). O óleo paga metade da conta porque tem uma demanda que o farelo não tem: biocombustíveis. Consequência: a indústria esmaga soja *pelo óleo*, e o farelo, que sai junto como subproduto, **sobra**, e o que sobra fica barato. O **ratio Far/Soj** mede isso: compara o valor de uma tonelada de farelo com o da soja que a originou. Hoje está em **78,6%**, o menor da janela (80,0% em 29/10, 78,9% em 30/10, 78,8% em 02/11), abaixo do limiar de 80% que o robô chama de farelo "abundante" (≥87% seria "apertado"). Na prática, o farelo vale menos de 79% do grão que o gerou.

**O que mudou hoje:** o **heating oil** (diesel de aquecimento, "primo" fóssil do biodiesel) fechou em **4,4218 US$/galão**, contra 4,7905 em 30/10 (**−7,7%**). A **margem de biodiesel** dos EUA caiu de US$ 2,213/gal (30/10) para **US$ 1,9013** (03/11). O óleo de soja em si ficou parado (65,14, contra 65,08 em 02/11), ou seja, o diesel já piorou a conta do biodiesel sem que o óleo tenha ajustado para baixo. Esse é o dado de risco do dia. Em compensação, o **Índice de Sobra de Farelo** recuou de 75 para **50/100** ("pressão moderada, 2/4 condições"), o que pede cautela com short outright de farelo. O Índice de Suporte do Óleo segue em 80.

**Leitura de uma linha:** o pivô do complexo continua sendo o **óleo via diesel**; a maior convicção é **baixista no farelo** (sobra estrutural + ratio comprimido), mas com selo de pressão máxima já desligado; soja é a perna lenta; confiança **baixa-média** (preços parciais, sem WASDE/NOPA em número, câmbio defasado em 30/10).

## Soja

**Viés:** baixista **fraco** (de preço), confiança baixa-média.

**O que SUSTENTA a tese**

*Nível e momentum.* A soja (ZSF27, jan/27) está em **1.219,50 US¢/bu** em 03/11, contra 1.216,75 (02/11), 1.234,25 (30/10), 1.234,75 (29/10), 1.238,00 (28/10) e 1.252,50 (26/10) (`indicators` e briefings anteriores). Saldo: **−2,6% desde 26/10**, em degraus pequenos. Hoje a amplitude foi só 3,5 centavos (1.216,00–1.219,50), abertura 1.217,00 e fechamento na máxima do dia: um leve repique de +2,75 sobre ontem, sem força (volume baixo). Um quase-empate depois de uma queda lenta é compatível com mercado sem pressa, não com virada.

*Curva a termo.* nov/26 1.205,50 · jan/27 1.219,50 · mar/27 1.228,50 · mai/27 1.238,75 · jul/27 1.247,00, com ago/27 recuando a 1.233,25 (CBOT 2026-11-03). Carry de 41,5 US¢ entre nov e jul (3,4%): **contango**, o mercado paga para armazenar, sem escassez imediata. O recuo de ago/27 abaixo de jul/27 (−13,75) sugere expectativa de safra nova mais folgada. Curva assim é coerente com viés baixista fraco, não com corrida de alta.

*Colheita nos EUA.* USDA Crop Progress: **88% colhido em 01/11**, contra 79% em 25/10 (+9 pontos em uma semana). A colheita está praticamente encerrada; o prêmio de risco do hemisfério norte desaparece e o que estava no campo virou oferta física. O briefing não traz a média de cinco anos nem exportações semanais, então não digo se é adiantado ou normal.

*Câmbio e paridade em reais.* Último PTAX disponível: USD/BRL **5,4212 em 30/10** (BCB sgs 1), contra 5,3744 (29/10) e 5,0377 (23/10). Paridade de exportação **R$ 145,75/saca de 60 kg** (CBOT 1.219,50 × 5,4212, sem basis; `indicators` 2026-11-03), contra R$ 145,42 em 02/11 e R$ 147,51 em 30/10. Importante: a paridade de 02 e 03/11 usa o PTAX *congelado* de 30/10 (o BCB não trouxe dado mais novo), então a variação em reais reflete só o CBOT. Mecanismo geral: real fraco eleva o preço interno e estimula a venda do produtor, o que adiciona oferta e limita a recuperação do CBOT. Fila `alerta-quebra_resistencia-usd_brl_ptax-2026-10-30`: PTAX 5,42 acima da "resistência" 5,30. É fato real, mas a série tem saltos suspeitos (5,0377 em 23/10 → 5,5007 em 26/10, +9,2% em um pregão útil), então uso o câmbio como **direção** (real mais fraco que há duas semanas), não como número exato.

*Posicionamento dos fundos.* COT (CFTC) de **27/10**: managed money (fundos) em soja com **226.215 comprados e 32.434 vendidos, net long 193.781**, sobre open interest (OI, contratos em aberto) de 979.414; em 20/10: 259.970 / 38.645, net 221.325, OI 1.093.612. Variação: **−27,5 mil de net long (−12,4%)** e OI −10,4%: liquidação, fundo vendendo posição comprada e saindo, não virando vendido. A ponta comprada ainda é ~23% do OI, grande em termos absolutos. Mecanismo: ainda há combustível de queda, mas parte já foi queimada, o que explica a descida lenta. O briefing não tem percentil histórico: digo "grande", não "extrema". O dado é de seis dias atrás.

*Demanda e oferta BR.* ABIOVE (projeções mensais): esmagamento de **2.626,6 mil t em nov/2026** e **2.203,5 mil t em dez/2026**; estoque de soja de 5.720,8 (início de nov) para 3.659,0 (fim de nov) e 1.889,9 mil t (fim de dez); exportação projetada de só 108 mil t em novembro. Leitura: safra velha sendo consumida, oferta doméstica encurtando no fim do ano, suporte sazonal à soja no Brasil. São *projeções*, não resultado.

*Clima.* NOAA CPC mantém **El Niño Advisory** (2026-11-03). Regra geral de mercado (conhecimento geral, não do briefing): El Niño tende a favorecer chuva no Sul do Brasil/Argentina e irregularidade no Norte/Nordeste. INMET (previsão para 04/11): Sorriso/MT máx. 38 °C e mín. 25 °C, Cuiabá/MT 38 °C, Sinop e Lucas do Rio Verde/MT 37 °C, Rio Verde/GO 33 °C, Maringá/PR 30 °C, Cascavel/PR 30 °C, Passo Fundo/RS 23 °C, em geral com chuva ou chuvisco em todas as praças. Calor forte com chuva na fase de desenvolvimento inicial no Centro-Oeste é, em si, benigno; nada no dump indica estresse hídrico. Clima **não** sustenta prêmio de risco hoje.

**O que INVALIDA / risco**
- Fechamento da soja **acima de ~1.242** (máxima de 30/10) ou 1.252 (26/10) com volume real: devolve a tendência da semana passada.
- Número de WASDE (relatório mensal do USDA) que reduza estoques finais — **não consigo avaliar**, o dump não traz o relatório.
- Falha climática no Centro-Oeste ou no sul argentino (o El Niño vira variável).
- Novo COT: recompra de fundos indica risco de squeeze.
- Real forte devolve pressão ao preço interno em reais.

**Leitura operacional**
*Short:* tático, alvos modestos. O forecast do robô (gerado 2026-11-03: 7d central 1.192,23, faixa 1.166,02–1.218,45; 30d central 1.091,39) é extrapolação de média móvel + volatilidade + inclinação; o spot já está no topo da banda de 7 dias. **Não adoto −10% em 30 dias**; alvo defensável na região de 1.200–1.210. *Long:* sem gatilho técnico nem fundamental; contra contango, colheita fechando e fundo ainda grande, exige stop curto (acima de 1.242). O melhor uso da soja é como **perna do crush** (ver Spreads).

*Fila tratada:* `alerta-quebra_resistencia-soja_cbot-2026-11-03` — fechou em 1.219,50, "acima da resistência 1.180,00". O nível está 3,3% abaixo do preço; o fato é verdadeiro, mas o nível está defasado e o alerta não muda a tese baixista fraca (o preço está acima da resistência *e* mesmo assim em queda de 2,6% em seis pregões, o que mostra que o nível não descreve a dinâmica atual). Recomendo recalibrar (fora do escopo desta camada).

## Farelo

**Viés:** baixista **moderado**, confiança média. Maior convicção do dia, com a ressalva de que o Índice de Sobra desceu para 50 e o ratio já está comprimido.

**O que SUSTENTA a tese**

*Nível e momentum.* O farelo (ZMZ26, dez/26) está em **319,50 US$/sht** em 03/11 (faixa 319,00–320,50), contra 319,60 (02/11), 324,60 (30/10), 329,30 (29/10), 335,70 (28/10) e 340,20 (26/10): **−6,1% em seis pregões**, a maior queda do complexo. O dia de 02/11 foi o do tombo (abertura 324,60, máxima 326,00, mínima 318,80, fechamento 319,60, volume 74.254); hoje o preço ficou parado perto dessa mínima (abertura 320,30, fechamento 319,50). Parar na mínima da liquidação depois de uma queda forte pode ser tanto digestão quanto vendedor persistente; o volume de hoje é pequeno demais para decidir.

*Curva a termo.* dez/26 319,60 · jan/27 319,90 · mar/27 321,20 · mai/27 325,50 · jul/27 330,70 · ago/27 330,90 (CBOT 2026-11-03): carry de ~11,3 US$/sht em sete meses (3,5%). Em proteína apertada o prompt seria mais caro que o diferido; aqui é o oposto, sem prêmio de escassez.

*Ratio Far/Soj em 78,6%.* Série (`indicators`): 81,35% (28/10), 80,01% (29/10), 78,9% (30/10), 78,8% (02/11), **78,6% (03/11)**. É o quarto pregão de queda consecutiva do ratio, o menor da janela, e o terceiro seguido abaixo de 80%. Isso faz duas coisas. Primeiro, **confirma** que o farelo está barato em relação ao grão por causa da sobra (óleo pagando o crush). Segundo, reduz o prêmio de quem opera short do ratio: quanto mais baixo, mais perto da zona em que o farelo "barato demais" atrai demanda de ração e desestimula esmagamento só pelo óleo. Em mean-reversion (retorno à média), abaixo de 80% o risco fica bilateral: tendência e sobra empurram para baixo, a média puxa para cima. O ratio caiu pouco (−0,2 ponto em dois dias) e vem sendo mantido; ainda sem evidência de reversão, mas também sem aceleração nova.

*Oil share e spread óleo−farelo.* Oil share **50,48%** e spread **+0,1364 US$/bu** (03/11), contra +0,1276 em 02/11, +0,1078 em 30/10 e −0,0242 em 29/10. O óleo segue valendo mais que o farelo no crush e a distância aumenta, porém por causa do **farelo caindo**, não do óleo subindo. Quanto mais o óleo manda, mais o farelo é subproduto.

*Índice de Sobra de Farelo.* **50/100** em 03/11 ("pressão moderada, 2/4 condições", `indicators`), contra 75 em 01 e 02/11 e 100 em 30 e 31/10 (4/4). É a menor leitura da série do briefing (25 pontos abaixo de ontem). O briefing não detalha qual condição apagou, então **não invento causa**. Leitura prudente: a tese estrutural segue em pé (ratio < 80%, oil share > 50%), mas o indicador sintético de "sobra" perdeu metade das condições, argumento de cautela contra short farelo outright depois de −6,1%.

*Posicionamento dos fundos.* COT 27/10: managed money em farelo com **184.371 comprados e 15.657 vendidos, net long 168.714**, sobre OI de 609.960 (ponta comprada ~30% do OI). Em 20/10: 213.717 / 12.839, net 200.878, OI 635.401. Variação: **−32,2 mil de net long (−16,0%)**, compradores saindo (−29,3 mil) e vendidos crescendo pouco (+2,8 mil). Produtores/indústria têm 387.753 vendidos contra 69.776 comprados (hedge) e swaps 133.898 comprados contra 13.251 vendidos. Interpretação: posição de fundo **grande e unilateral** numa proteína que o fundamento diz estar sobrando; a liquidação já começou, e como o preço caiu mais **depois** da data-base de 27/10 (de 324,60 para 319,50), é provável que o COT atual esteja mais liquidado ainda. Limitação: dado de seis dias atrás, sem percentil.

*Oferta e exportação BR.* ABIOVE (projeções): produção de farelo de **1.977,6 mil t em nov/2026** e **1.659,0 mil t em dez/2026**; exportação de 800 mil t (nov) e 700 mil t (dez); estoque final de **1.101,4 mil t** (nov, inicial 1.100,1) e **1.015,5 mil t** (dez). Estoque quase estável em novembro e −86 mil t em dezembro: oferta brasileira estável a levemente apertada no fim do ano, insuficiente para compensar a sobra via esmagamento forte (2,63 milhões de t de soja em nov). O dump não traz prêmio de exportação em Paranaguá, oferta argentina, nem praças. Sem milho nem proteína concorrente no briefing, não avalio a demanda via ração.

**O que INVALIDA / risco**
- **Repique do ratio**: fechamento acima de ~80,5–81% com farelo subindo mais que a soja desfaz o rompimento; acima de ~82% encerra a tese de curto prazo.
- **Short squeeze técnico**: o Índice de Sobra em 50 e −6,1% em seis pregões abrem espaço para repique de 5–8 US$/sht (326–328, máxima de 02/11) sem notícia.
- **NOPA** (esmagamento mensal dos EUA, fila `release-nopa-2026-11-03`): esmagamento fraco reduziria a sobra. O dump marca `monthly_status = 0` (paywall) — **sem número, não julgo**.
- **Qualidade de dado**: volumes baixos de hoje; nova revisão do fechamento muda o ratio.

**Leitura operacional**
*Short:* tese estrutural + ratio comprimido + liquidação em curso sustentam, mas short outright a 319,50 após −6,1% e com Sobra em 50 é entrar atrasado; prefiro a expressão em **spread contra o óleo** (long óleo/short farelo, com a ressalva do diesel abaixo) ou entradas em repiques para 324–326. *Long:* só tático e curto, com gatilho no ratio recuperando 80,5%/81%; contra a tendência. Forecast do robô (2026-11-03: 7d central 305,36, faixa 291,32–319,40; 30d central 252,13): o spot já está **no topo** da banda de 7 dias; **−21% em 30 dias não é sustentado pelo fundamento** e não o adoto; alvo de curto prazo defensável 312–318.

*Filas tratadas:* `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` e `...-D+90`. A tese de junho partia de ratio 81,4%; hoje 78,6% — o spread **seguiu comprimindo** (~−2,8 pp) e permanece abaixo do limiar de 80% desde 30/10 (resposta ao D+7, "ratio fechou <80%?": sim, só em 30/10, bem depois da janela de 18/06; ao D+90, "reverteu ou seguiu comprimindo?": seguiu). Direção **confirmada**; ganho de preço não verificável, pois o briefing não traz o preço do farelo em junho, nem WASDE/NOPA em número. Recomendo fechar as duas revisões como "direção confirmada, resultado financeiro não verificável".

## Óleo

**Viés:** baixista **fraco**, confiança baixa-média. Perna mais "teimosa": o diesel agora pressiona forte, mas o óleo ainda não ajustou, e oil share e Suporte do Óleo seguram.

**O que SUSTENTA a tese**

*Nível e momentum.* O óleo (ZLZ26, dez/26) está em **65,14 US¢/lb** em 03/11 (faixa 64,96–65,25), contra 65,08 (02/11), 65,90 (30/10), 65,64 (29/10), 65,56 (28/10) e 67,01 (26/10): −2,8% desde 26/10, **lateral em 65–66** desde 28/10. A amplitude de hoje foi de 0,29 US¢, muito estreita. Piso a testar: ~64,96 (mínima de hoje).

*Curva a termo.* dez/26 65,14 · jan/27 65,35 · mar/27 65,82 · mai/27 66,21 · jul/27 66,34 · ago/27 65,96 (CBOT 2026-11-03): contango leve (+1,20 US¢, 1,8% até julho). Reconhece alguma sustentação futura (biocombustível) sem pagar prêmio imediato.

*Heating oil e margem de biodiesel — fator dominante e dado central de hoje.* O heating oil fechou em **4,4218 US$/galão** em 03/11 (faixa 4,4052–4,4488), contra 4,7905 em 30/10, 4,74 (29/10), 4,82 (28/10), 4,78 (27/10) e 4,91 (26/10): **−7,7% sobre a sexta e −9,9% desde 26/10**. A abertura de 4,6746 reportada no briefing está fora da faixa do dia (a máxima foi 4,4488) e é idêntica à de 02/11, então é dado velho/inválido; ignoro-a. Em 02/11 os indicadores do robô já usavam HO ≈ 4,42 (receita 7,5866 − 1,5 × RIN 2,11 ≈ 4,42), o que mostra que o HO de 02/11 foi revisado do 4,61 que eu vi ontem para ~4,42. Ou seja, a queda do diesel é consistente em dois pregões, ainda que de volume baixo (700 contratos hoje).

Mecanismo: o biodiesel compete com o diesel; diesel barato exige óleo mais barato para o biodiesel continuar competitivo. A **margem de biodiesel dos EUA** (`indicators` 2026-11-03) foi a **US$ 1,9013/galão** (receita 7,59 = HO 4,42 + 1,5 × RIN 2,11; custo 5,69 = óleo 4,89 + 0,80 industrial), contra 1,9056 em 02/11, 2,213 em 30/10, 2,178 em 29/10 e 2,2632 em 28/10: **−14% em dois pregões úteis**. Ressalva: o RIN (crédito de combustível renovável) fica fixo em 2,11 todos os dias (provavelmente não é cotação diária); a *variação* da margem é confiável (vem de HO e óleo), o *nível* não. A margem segue larga (acima de US$ 1,90/gal) e o óleo de soja só custou 4,89 do galão, por isso não há sinal de que a demanda de biodiesel desligue. Mas a **pressão marginal** é baixista: o diesel caiu 37 centavos e o óleo, em termos de custo, caiu só 5,7 centavos (4,9425 → 4,8855), isto é, o óleo **não acompanhou** o combustível fóssil. Para a margem voltar a 2,21 com HO a 4,42, o óleo precisaria cair para perto de ~61,0 US¢/lb (aritmética minha sobre as premissas do robô: receita de 7,5868 menos 0,80 industrial menos 2,213 de margem deixa custo de óleo de 4,57/gal, ou 61,0 US¢/lb); trato isso como referência de tamanho do "gap", não previsão, porque o mercado não precisa restaurar a margem anterior.

*Oil share 50,48% e Suporte do Óleo 80/100.* O óleo vale mais que o farelo no crush (spread +0,1364 US$/bu) e o Índice de Suporte do Óleo está em **80** ("óleo domina o crush, 4/5 condições", `indicators`), estável de 30/10 a 03/11. Duas leituras: (a) o óleo é estruturalmente sustentado pelo biocombustível; (b) o complexo inteiro depende desse vetor — se o óleo ceder, oil share e margem caem juntos. Armadilha: o oil share sobe **porque o farelo cai**, não porque o óleo suba; "sustentado" aqui é relativo ao farelo, não sinal de alta absoluta. Além disso, o índice é de estado e não incorpora ainda a deterioração da margem de biodiesel que apareceu hoje.

*Posicionamento dos fundos.* COT 27/10: managed money em óleo com **97.309 comprados, 36.978 vendidos, net long 60.331**, OI 573.736; em 20/10: 104.484 / 32.966, net 71.518, OI 570.462. Variação: **−11,2 mil de net long (−15,6%)**, compradores saindo (−7,2 mil) **e vendidos entrando (+4,0 mil)** — diferente de soja e farelo, há venda nova de fundo no óleo. Ponta comprada ~17% do OI, bem mais moderada que no farelo (~30%): menos vulnerável a liquidação forçada, mas já há fundo apostando contra. A queda do diesel posterior a 27/10 provavelmente aprofundou essa tendência.

*Demanda e oferta BR.* ABIOVE (projeções): produção de óleo de **494,9 mil t em nov/2026** e **415,2 mil t em dez/2026**; **exportação de apenas 21 mil t em novembro**; estoque de 306,4 mil t (início de nov) → **315,3 mil t** (fim de nov) → **291,9 mil t** (fim de dez). O Brasil exporta quase nada de óleo: a produção fica no mercado interno, majoritariamente biodiesel, tornando o óleo brasileiro muito mais sensível a **política de mistura** (B15/B16) do que ao mercado externo. A queda de estoque em dezembro (−23 mil t) é viés levemente altista interno. Sem basis nem praça no dump.

*Palma e demais.* O parser do MPOB (palma da Malásia) não extraiu números em nenhum dia (`mpob`, 2026-11-03) — sem estoque/exportação de palma, principal substituto. Sem RIN D4 diário nem diesel brasileiro.

**O que INVALIDA / risco**
- **Heating oil** recuperando para 4,70+ em pregão com volume: reverte a pressão e leva a margem de biodiesel de volta acima de 2,10.
- **B16 (CNPE), sinal da EPA (RFS) ou crédito 45Z** nos EUA — gatilhos altistas fortes; nada no dump os confirma.
- **Fechamento do óleo abaixo de ~64,95** (mínima de hoje) com HO caindo: abre espaço para 63–64.
- **Fechamento acima de ~66,00–66,65** (topo da faixa de 28–30/10): invalida a lateralidade para baixo e reabre 67.
- Forecast do robô (2026-11-03): 7d central 64,30 (faixa 62,23–66,36), 30d central 61,13. A banda inclui o spot; espero **lateral-baixista em 64,0–66,0**, não os −6% do central de 30d.

**Leitura operacional**
*Short:* mais argumento que ontem: o diesel perdeu ~8% e o óleo ainda não acompanhou, então há "dívida" de ajuste. Mas o óleo vem lateral por seis pregões, com suporte aparente em 64,95, e o dado do diesel tem volume ralo (700 contratos); short outright com convicção menor que no farelo e stop acima de 65,6. *Long:* oil share >50%, margem de biodiesel ainda acima de US$ 1,90/gal e Suporte do Óleo em 80 mostram demanda estrutural; entrada tática perto de 64,9–65,0 com stop curto abaixo de 64,5; o catalisador (B16, EPA, 45Z) precisa vir de fora, e a expressão long óleo / short farelo agora tem a perna "óleo" **menos confortável** que na semana passada.

*Fila tratada:* `alerta-quebra_suporte-oleo_cbot-2026-11-03` — fechou em 65,14, "abaixo do suporte 72,00". O nível está 10% acima do preço e foi rompido há tempos; confirma que o óleo opera abaixo da calibração, sem informação nova. Recomendo recalibrar.

## Spreads e crush (leitura de complexo)

*Crush margin.* **US$ 1,9994/bu** em 03/11 (farelo 319,50 + óleo 65,14 − soja 1.219,50; `indicators`), contra 2,0225 (02/11), 2,0477 (30/10), 2,1175 (29/10), 2,2170 (28/10) e 2,3305 (26/10): −33 centavos (−14,2%) em seis pregões; rompeu o patamar de US$ 2,00 pela primeira vez na janela. Fila `alerta-quebra_suporte-complexo_soja-2026-11-03` ("2,00 abaixo do suporte 2,50"): fato verdadeiro, mas o nível 2,50 é defasado, então confirma margem em queda sem informação nova de nível. US$ 2,00/bu ainda é margem **alta** o bastante para a indústria seguir moendo (ABIOVE: 2,63 milhões de t em novembro), logo a oferta de farelo e óleo continua chegando, o que sustenta a pressão nos produtos. O risco de médio prazo é o reverso: margem em queda contínua desacelera o esmagamento, o mecanismo natural de correção da sobra de farelo (não é gatilho para os próximos dias).

*Far/Soj (mean-reversion, os dois lados).* 78,6%, o menor da janela. **Short do ratio** (short farelo/long soja): tendência e sobra favorecem, mas o prêmio restante diminuiu e o Índice de Sobra caiu a 50; entrar agora é seguir momentum, não capturar valor. **Long do ratio** (long farelo/short soja): bom ponto pela média, mas contra o fundamento e contra um fundo ainda comprado (168 mil líquidos em 27/10); só com confirmação (ratio voltando >80,5% com farelo subindo). Leitura: assimetria **desfavorável ao short do ratio e neutra a levemente favorável ao long tático**; é aviso de risco de repique, não gatilho de entrada.

*Oil share e spread óleo−farelo.* 50,48% e +0,1364 US$/bu: óleo à frente do farelo, distância crescendo (−0,0242 em 29/10 → +0,1364 hoje). Long óleo/short farelo é aposta de **continuidade**, e parte dela já pode estar precificada. Com o heating oil em queda e a margem de biodiesel caindo para 1,90, o lado "óleo" perde apoio externo; o lado "farelo" continua com a sobra, mas a Sobra recuou para 50. O spread continua preferível às pernas soltas, com a perna long menos confortável.

*Índices sintéticos juntos.* Sobra de Farelo **50** e Suporte do Óleo **80**: "o farelo sobra moderadamente (2 de 4 condições) e o óleo domina o crush (4 de 5)". A divergência entre os dois (sobra esfriando, suporte estável) sugere um complexo que já descontou boa parte da pressão no farelo, enquanto o risco novo vem da margem de biodiesel. Índices de estado não dão timing.

*Em conjunto.* Deriva baixista comum, **óleo/diesel como pivô**, **farelo como perna mais frágil mas com sinal de esgotamento tático**, soja como a mais estável. Crush abaixo de 2,00 e ratio a 78,6% dizem que o mercado já desconta boa parte da sobra; o risco passa a ser **tático** (repique no farelo, ajuste do óleo ao diesel) mais que estrutural.

## Lente fiscal/regulatória BR

O monitor tributário (`system/tributario_watch.toml`) tem `atualizado_em = 2026-06-05` — **quase cinco meses sem atualização**; o briefing de hoje não traz seção do monitor. Trago os vetores como registrados, **sem validação nova**.

- **MP 1.363/2026** — subvenção de R$ 1,12/L ao diesel fóssil, vigente até **31/12/2026** (status registrado "vigente"). Barateia o diesel dentro do mix B15, reduz a competitividade do biodiesel e a demanda interna por óleo de soja: efeito **baixista para o óleo** e indiretamente para o farelo (menos esmagamento puxado por óleo). Risco de calendário: fim da vigência em dezembro seria altista para biodiesel e óleo.
- **MP 1.358/2026** — subvenção com vigência até 11/07/2026; catalogada como "tramitação" mas o prazo já venceu — desfecho **não consta no briefing**.
- **B16 (CNPE)** — mistura a 16%, **adiada**; testes técnicos de seis meses teriam resultado perto de **nov/2026** (estamos nele); cada +1 pp de mistura puxaria ~436 mil t de óleo (registro do catálogo). **Nada no dump indica convocação do CNPE.** Principal gatilho altista doméstico para o óleo; para o farelo, efeito misto (mais esmagamento = mais proteína sobrando).
- **PIS/Cofins do biodiesel** — isenção prorrogada até 31/07/2026 (registro de junho); o que veio depois **não consta**. **STJ REsp 2.165.276** (crédito de PIS/Cofins sobre soja em biodiesel, não vinculante): custo da cadeia, sem atualização.
- **EUA/Indonésia:** EPA RFS 2026/2027, crédito 45Z, Indonésia B50, levy de exportação de palma — marcos do catálogo sem validação; seriam o principal potencial de sustentação externa do óleo, mas **não valido nenhum**.

Aplicação: filtro fiscal no sentido **baixista para o óleo interno** (MP 1.363 vigente, B16 parado) e **neutro para a soja**; não concluo além disso sem atualizar o catálogo. Em reais, o dólar a ~5,42 (PTAX de 30/10) atenua a fraqueza do CBOT no preço interno.

## Riscos e eventos próximos

- **Confirmação dos preços de hoje:** volumes baixos; o próximo briefing pode reescrever os fechamentos de 03/11.
- **NOPA** — fila `release-nopa-2026-11-03`: o robô registra "release novo", mas o relatório mensal está atrás de paywall e o dump marca `monthly_status = 0`, sem número. Esmagamento acima do esperado seria baixista para o farelo e ambíguo para o óleo. **Não trato como informação até haver número.**
- **WASDE** — sem números no dump; não avalio.
- **COT** (próximo relatório): mostra se a liquidação continuou após a queda de 02/11; atenção ao net long de farelo (168,7 mil em 27/10) e à entrada de short no óleo.
- **USDA Crop Progress:** colheita de soja nos EUA em 88% (01/11); a próxima leitura praticamente encerra o tema.
- **Diesel/heating oil:** pivô diário do óleo; precisa de pregão com volume para confirmar os 4,42.
- **PTAX:** o último dado no briefing é de 30/10; câmbio novo pode mudar a paridade em reais.
- **Novembro/dezembro:** possível convocação do CNPE (B16), safra sul-americana sob El Niño, fim da MP 1.363 (31/12).
- Datas de próximos WASDE/COT/NOPA são calendário regular de conhecimento geral, não confirmado no briefing.

## Honestidade

- **Preços de 03/11 com volume ralo** (soja 12.351, farelo 1.503, óleo 2.357 contratos, contra 74.254 do farelo em 02/11): provavelmente retrato parcial do dia. Os "fechamentos" podem ser reescritos. Os indicadores do robô de hoje foram calculados sobre eles.
- **Heating oil:** a abertura de 4,6746 está fora da faixa do dia e é idêntica à de 02/11, logo é dado inválido, que descartei. O HO de 02/11 que eu li ontem (4,6117) foi revisado para ~4,42 (inferido da receita de biodiesel no `indicators`); a linha crua de 02/11 está truncada no dump de hoje, então essa inferência é minha. Volume de 700 contratos: sinal ainda ralo.
- **Sem WASDE e sem NOPA em número.** Qualquer afirmação sobre balanço americano ou esmagamento mensal seria invenção.
- **Sem físico BR:** sem Paranaguá, basis, praças, CEPEA, exportação semanal EUA, palma (MPOB falhou), notícias (0 itens), milho/ração, RIN diário (fixo 2,11) e percentil do COT.
- **Câmbio:** o último PTAX é de 30/10; a paridade de 02 e 03/11 usa esse valor congelado. A série tem saltos suspeitos (5,0377 → 5,5007 → 5,3346 entre 23 e 27/10), então o número em reais pode estar errado.
- **Cálculo do preço do óleo que restauraria a margem de biodiesel** é aritmética minha sobre premissas fixas do robô, não indicador do briefing.
- **Causa da oscilação do Índice de Sobra** (100 → 75 → 50): não identificada; não especulo.
- **COT de 27/10** tem seis dias; posições mudaram desde então (o farelo e o diesel caíram depois).
- **Níveis dos alertas da fila** (soja 1.180, óleo 72,00, crush 2,50, PTAX 5,30) estão defasados; os alertas confirmam fatos sem direção nova.
- **Forecasts do robô** (soja 30d 1.091,39; farelo 252,13; óleo 61,13) implicam −10,5%, −21% e −6%, **não sustentados** pelo fundamento; mantive só a direção.
- **Inferências marcadas:** efeito do El Niño é regra geral, não dado do briefing. Fiscal: catálogo de junho, sem atualização.
- **Convicção geral:** baixa-média. Direção baixista coerente nas três pernas; ratio comprimido, crush abaixo de 2,00, margem de biodiesel em queda e liquidação de fundos são fatos robustos em `indicators`/COT. Tamanho e timing dependem de dados que não consegui validar.
