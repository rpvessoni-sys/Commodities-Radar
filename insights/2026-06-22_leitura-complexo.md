---
data: 2026-06-22
titulo: "Óleo despenca -4% no primeiro pregão pós-Juneteenth — roll de soja para novembro mascara estabilidade do grão, ratio Far/Soj cruza <80% no horizonte de novo-safra e crush aperta mais 17%"
tags: [complexo, auto-claude]
fontes:
  - CBOT CME (ZS=F/ZSN26/ZSX26/ZM=F/ZMN26/ZL=F/ZLN26/HO=F) — fechamentos 2026-06-22
  - BCB PTAX — 2026-06-19 (USD/BRL 5,1442 — último disponível; Juneteenth + fim de semana ausentam 20-22/jun)
  - CEPEA/ESALQ Paranaguá — 2026-06-19 (R$ 132,84/sc)
  - NAG Físico BR (farelo MT/RS/Rondonópolis, prêmio export PGUA) — 2026-06-19
  - CFTC COT Managed Money — 2026-06-09 (13 dias de defasagem)
  - USDA WASDE junho — 2026-06-11
  - USDA Crop Progress — 2026-06-14
  - NOAA CPC ENSO — 2026-06-22 (El Niño Advisory)
  - ABIOVE projeções mensais — coleta 2026-06-22
  - Indicadores sintéticos (Índice Sobra Farelo 100/100, Índice Suporte Óleo 80/100) — 2026-06-22
  - Margem biodiesel US calculada pelo sistema — 2026-06-22
  - FarmProgress headline 2026-06-22 ("The fork in the road looming for the soybean market")
  - Inmet previsão — 2026-06-22 (para 23/jun)
status: ativa
vies: [neutral-soja, bear-farelo, bear-oleo_curto_prazo]
---

## Visão geral

O complexo retornou de um longo fim de semana de três dias — o feriado americano de Juneteenth (sexta-feira, 19/jun) fechou a CBOT, e o primeiro pregão de volta, na segunda-feira 22/jun, trouxe o movimento mais expressivo do ciclo recente: o óleo de soja CBOT afundou -4,02% em um único pregão, de 69,69 para 66,89 ¢/lb (CBOT, 22/jun/2026), enquanto o farelo ficou praticamente estável, com queda marginal de -0,23% (de 301,30 para 300,60 USD/short ton). A soja, nominalmente, "subiu +1,85%", mas essa leitura merece qualificação imediata: o contrato referência ZS=F rolou de Julho (N26, que fechou em 1.120,75 ¢/bu — praticamente idêntico ao último pregão em 18/jun de 1.122,75 ¢/bu) para Novembro (X26, 1.143,50 ¢/bu). O salto aparente de +20,75 ¢/bu no spot é, em sua quase totalidade, um artefato de rollover de contrato, não uma alta real do grão. Grão velho-safra (Julho) ficou essencialmente no mesmo patamar.

Essa distinção importa para a leitura operacional: o que o dia 22/jun realmente registrou foi **óleo caindo com força** e **farelo/soja estáveis no old-crop**. O único movimento genuíno e dominante foi o colapso do óleo. O heating oil, proxy da receita dos produtores de biodiesel americanos, também cedeu -3,2% no mesmo pregão (de 3,187 para 3,079 USD/galão), adicionando um driver de fundamentos ao movimento técnico do óleo de soja. 

A crush margin calculada pelo sistema caiu de 3,067 para 2,536 USD/bu (-17% no período; fila `alerta-movimento_forte-complexo_soja-2026-06-22`). Uma parte dessa compressão é real (óleo menor) e parte é calculística (a roll do ZS=F para um contrato de soja mais caro, o novembro). O dado que devemos reter: com a soja-novembro em 1.143,50 e farelo em 300,60, o ratio Far/Soj cruzou abaixo de 80% pela primeira vez neste ciclo, chegando a 78,86% (fila `ratio-zona-2026-06-22`). Com a soja-julho (1.120,75), o ratio seria 80,48% — praticamente imóvel. A entrada na zona "comprimida" é real no horizonte de novo-safra, e real para qualquer operador que esteja planejando crush forward de agosto em diante; ainda não completada no velho-safra imediato.

O Índice Sobra Farelo está em 100/100 pelo quarto dia consecutivo (18, 19, 20, 21 e 22/jun/2026). O Índice Suporte Óleo segue em 80/100. O oil share cedeu para 52,67% — ainda acima do pivot de 50%, mas em trajetória de queda contínua desde 55,18% em 12/jun (-2,51 pontos percentuais em dez pregões). A manchete do FarmProgress de 22/jun ("The fork in the road looming for the soybean market") captura bem o tom: o mercado está diante de uma bifurcação, e a direção do óleo nas próximas sessões determinará qual caminho o complexo toma.

---

## Soja

**Viés: neutro (velho-safra, Julho N26) / levemente baixista (novo-safra, Novembro X26)**

### O que sustenta a tese e como lê-la hoje

A leitura de soja no dia 22/jun começa necessariamente pelo entendimento do roll. O contrato ZS=F, que os sistemas de coleta usam como referência de "preço spot", migrou de Julho (N26) para Novembro (X26) durante o longo fim de semana de Juneteenth. A razão é simplesmente técnica: o contrato de Julho de soja tem first notice day em 30/jun e os grandes players (comerciais e fundos) já rolaram suas posições para meses à frente. Com isso, o ZS=F passou a espelhar o X26 (Novembro), que em 18/jun estava em 1.142,75 ¢/bu (dado implícito na análise de 21/jun) e fechou em 22/jun em 1.143,50 ¢/bu — alta de meros +0,75 ¢/bu, ou +0,07%. O July (N26) saiu de 1.122,75 ¢/bu (18/jun) para 1.120,75 ¢/bu (22/jun), queda de -2 ¢/bu ou -0,18%. Operacionalmente: o velho-safra está levemente mais fraco, o novo-safra está praticamente estável. Não houve evento de mercado que justifique uma alta real em nenhum dos contratos.

**Estrutura de curva nova-safra revela o que o mercado pensa do 2S26.** A curva CBOT em 22/jun/2026: N26 (Jul) 1.120,75 → Q26 (Ago) 1.128,00 → U26 (Set) 1.129,25 → X26 (Nov) 1.143,50 → F27 (Jan) 1.157,50 → H27 (Mar) 1.164,50 ¢/bu. A estrutura é um contango suave no velho-safra (N26 a U26, diferença de apenas +8,50 ¢/bu) e uma descontinuidade mais ampla de X26 para F27 (+14 ¢/bu), que precifica o período entre o carryover de safra BR (pesado) e o início do novo-safra americano. O H27 (março/2027) em 1.164,50 ¢/bu é o contrato de nova-safra EUA — ele está +43,75 ¢/bu acima do N26, o que indica que o mercado espera tensão no balanço no primeiro semestre de 2027 (entre o fim da safra sul-americana e o início da norte-americana). Isso não é altista para o curto prazo: é o mercado dizendo "agora está farto, mas em 2027 pode apertar".

**Lavoura americana em boas condições sem prêmio de risco.** O USDA Crop Progress de 14/jun/2026 registrou: 95% da área de soja plantada, 88% emergida, condição 9% excelente + 57% boa = 66% boa/excelente. A média histórica neste período para lavouras em boa/excelente condição gira em torno de 60-62%, então os EUA estão levemente acima da média. Com El Niño Advisory ativo (NOAA CPC, 22/jun/2026 — status = 0,0, que no sistema é categorizado como "El Niño Advisory"), a tendência histórica do fenômeno é de chuvas acima do normal no Corn Belt americano durante o verão. Isso não é garantia, mas é bear marginal para risco climático de curto prazo.

**A grande "acreage surprise" ainda não está no briefing como número.** A manchete do FarmProgress de 18/jun ("Soybean market at crossroads with USDA acreage boost") indica que o USDA revisou a estimativa de área plantada de soja EUA para cima — o que, se confirmado no relatório oficial de Acreage (programado para 30/jun/2026), adiciona oferta potencial ao balanço 2026/27. O número exato da área revisada não consta no briefing. Quando confirmado, essa revisão é bear estrutural para o novo-safra.

**Posicionamento de fundos em soja: moderado, sem extremo que force desmonte.** COT de 09/jun/2026: managed money soja net long = +97.859 contratos (long 179.591, short 81.732; open interest total 1.016.125). A proporção de longs vs. short (2,2:1) é elevada mas não em nível extremo histórico para este contrato. Não há motivo para um desmonte abrupto de posição de fundos em soja no curto prazo — diferente do óleo, que tem posição muito mais apertada. Isso é levemente estabilizador para a soja.

**Câmbio e paridade BR.** O PTAX disponível é de 19/jun/2026 (5,1442 BRL/USD), último antes do Juneteenth e do fim de semana. O sistema calculou a paridade de 22/jun usando esse câmbio com o CBOT novembro (1.143,50): 1.143,50 × 5,1442 / 100 × (60/27,2155) = ~R$ 129,68/sc (indicadores sistema, 22/jun/2026). Com o July (1.120,75), a paridade seria de ~R$ 127,12/sc (cálculo próprio). O físico em Paranaguá estava em R$ 132,84/sc em 19/jun (CEPEA/ESALQ via NAG) — basis implícito de +R$ 3-5/sc sobre a paridade de novembro ou +R$ 5-6/sc sobre a paridade de julho. A praça interior do Paraná estava em R$ 124,65/sc (NAG, 19/jun) — abaixo de qualquer paridade, confirmando o desconto de frete e oferta abundante no interior. Com a PTAX de 22/jun não disponível (feriado, fim de semana), é preciso aguardar o dado de segunda-feira do BCB para recalibrar a paridade com precisão.

### O que invalida / risco para a soja

- **Calor ou seca no Corn Belt em julho**: a lavoura está em fase de enchimento de vagens, janela crítica. Uma onda de calor severa no Corn Belt (Iowa, Illinois, Indiana) entre meados de julho e início de agosto pode deteriorar a condição de 66% good/excellent rapidamente — e isso inverteria o viés de curto prazo de bear para bull com violência. O El Niño Advisory oferece proteção estatística, mas não é garantia.
- **WASDE de julho (previsto ~10/jul)**: se o USDA cortar a área ou produção projetada de soja EUA para 2026/27, será catalisador altista. Contudo, o viés atual do USDA é de "acreage boost" — a revisão seria uma surpresa.
- **China destrava compras de soja EUA em volume**: compras acima de 3-5 milhões de toneladas anunciadas de uma vez levariam o mercado para cima com force. A China mantém tarifa de 13% sobre soja americana e seus estoques internos estão elevados — o incentivo para compra em volume não existe agora, mas pode mudar se os estoques domésticos rodarem abaixo do esperado.
- **PTAX com depreciação relevante do BRL**: um retorno a 5,18-5,20 BRL/USD tornaria a soja BR mais competitiva, estimularia fixação e sustentaria os preços internos. Não há sinal atual para esse movimento, mas o quadro fiscal BR está sempre presente como risco cambial.

### Leitura operacional — soja

O trader que negocia old-crop (julho) não tem driver claro para entrar comprado ou vendido: o July está praticamente parado (-0,18% em 4 pregões de feriado) e sem catalisador imediato. O setup de calendário Jul/Nov (+22,75 ¢/bu) é operável para quem quer capturar a transição de velho-safra para novo-safra: long X26 (Nov) / short N26 (Jul) captura a declinação da oferta de carryover à medida que o mercado avança em direção à nova-safra. O risco do calendário: se o USDA lançar uma surpresa bearish no relatório de 30/jun (acreage muito acima do esperado), o X26 cede junto. A posição é longa novo-safra, não isenta de risco direcional.

---

## Farelo

**Viés: bear forte — consolidado, sem sinal de reversão**

Esta é a terceira leitura diária consecutiva com o Índice Sobra Farelo em 100/100 (todas as cinco condições estruturais de pressão baixista ativas simultaneamente). O farelo é o membro mais fraco do complexo de forma estrutural, e os dados de 22/jun reforçam isso sem nenhuma contradição.

### O que sustenta a tese bear

**Índice Sobra Farelo: 100/100 pelo quinto dia consecutivo de medição.** O indicador sintético do sistema fechou em 100 em 18, 19, 20, 21 e 22/jun/2026 (indicators/DB). Cinco condições negativas simultâneas: (1) ratio Far/Soj em zona de compressão; (2) oil share acima de 50% (óleo paga o crush, farelo é subproduto); (3) prêmio de exportação Paranaguá praticamente zerado; (4) esmagamento em ritmo elevado; (5) demanda de ração sem absorção imediata. Quando um indicador complexo permanece em seu extremo por cinco dias seguidos, não é ruído — é um sinal estrutural consolidado. O farelo não tem alívio da sobra em nenhuma das suas cinco frentes.

**O ratio Far/Soj: 78,86% pela perspectiva de novo-safra — zona comprimida confirmada.** Trata o item `ratio-zona-2026-06-22` da fila. O sistema calculou o ratio usando ZS=F = X26 (novembro, 1.143,50 ¢/bu) e farelo = 300,60 USD/sht: ratio = 300,60 / (1.143,50 × 33,33) = 300,60 / 38.112 = 0,7886 = **78,86%**, abaixo do threshold de 80% que define a "zona comprimida". 

Aqui cabe a qualificação operacional essencial: esse ratio de 78,86% usa a soja de **novembro** (novo-safra) como denominador. Se usarmos a soja de **julho** (velho-safra, N26 = 1.120,75 ¢/bu): ratio = 300,60 / (1.120,75 × 33,33) = 300,60 / 37.353 = **80,48%** — praticamente idêntico ao de 18/jun (80,51%). Qual é o ratio "correto" para o trader? Depende do horizonte. Para quem negocia esmagamento spot ou crush de julho-agosto, o ratio relevante é o de velho-safra (80,48%), que segue na zona de transição mas ainda acima de 80%. Para quem está planejando crush de setembro em diante, comprando soja nova-safra, o ratio de 78,86% já está na zona comprimida e o setup de mean-reversion começa a ganhar relevância.

A revisão do insight de 11/jun ([[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]], item `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7` da fila): a previsão de "ratio cruzar <80% em 1-2 semanas" se confirma pelo ratio de novo-safra em 22/jun (semana 22-28/jun). No velho-safra, o ratio saiu de 81,4% (11/jun) para 80,5% (22/jun) — comprimindo na direção prevista, mas não cruzando 80% ainda. O padrão de compressão é consistente com a tese, mas o timing é mais lento no contrato imediato do que o previsto.

**A estrutura de crush segue gerando farelo como subproduto — e isso não vai mudar enquanto o óleo pagar a conta.** O oil share em 52,67% significa que, de cada dólar de receita do crush, o óleo responde por 52,67 centavos e o farelo por 47,33 centavos. Enquanto o oil share estiver acima de 50%, a esmagadora compra soja primariamente para extrair óleo e aceita vender o farelo ao preço de mercado, por mais baixo que seja. A ABIOVE projeta esmagamento de soja no Brasil em 2.203,5 mil t em dezembro/2026 (ABIOVE projeções mensais, coleta 2026-06-22). Com esse ritmo de esmagamento contínuo, o farelo será gerado em volume ininterrupto.

O WASDE de junho (11/jun/2026) para o Brasil projeta produção de farelo 2026/27 em 8,0 milhões de toneladas — número inalterado em relação a maio/2026. Para a Argentina, a produção de farelo 2026/27 foi levemente reduzida de 33,33 mi t (maio) para 33,11 mi t (junho). Mas o estoque inicial argentino de farelo 2026/27 foi revisado para CIMA de forma mais expressiva: 2,73 mi t em junho vs. 2,47 mi t em maio — diferença de +260 mil t. Mais carryover argentino entrando no ciclo é bear marginal para o mercado global de farelo, pois reduz a dependência de nova produção para atender a demanda. A leitura do WASDE de 11/jun, portanto, é levemente bearish para o farelo global, não neutra.

**Curva forward do farelo CBOT em 22/jun: mercado não precifica aperto em 6 meses.** N26 (Jul) 300,60 → Q26 (Ago) 300,40 → U26 (Set) 300,20 → V26 (Out) 299,90 → Z26 (Dez) 303,60 → F27 (Jan/27) 305,70 USD/sht. A curva é praticamente plana do julho ao outubro, com um leve saltinho em dezembro-janeiro (possivelmente sazonalidade de demanda invernal no hemisfério norte). A diferença máxima entre o contrato mais caro (F27, 305,70) e o mais barato (V26, 299,90) é de apenas 5,80 USD/sht em 6 meses — menos de 2%. Um mercado em backwardation íngreme sinalizaria escassez de curto prazo e incentivaria desestoque. Uma curva em contango acentuado sinalizaria sobra e pressionaria o spot. Nenhum dos dois: a curva plana com leve alta no Z26-F27 diz que o mercado está cômodo com a oferta ao longo de todo o horizonte, sem antecipar nem aperto nem alívio dramático. Para o bear no farelo, isso é confirmação de que não há catalisador de alta precificado.

**Prêmio de exportação Paranaguá praticamente zero — físico BR sem saída competitiva.** O prêmio de exportação do farelo em Paranaguá estava em +0,05 USD/short ton (NAG, 19/jun/2026) — valor irrisório, abaixo de qualquer custo operacional relevante. Na prática, o exportador de farelo pelo porto de Paranaguá não tem margem. O excedente que não encontra destino de exportação flui de volta para o mercado interno, pressionando os preços físicos. Praças físicas de 19/jun/2026 (NAG): Mato Grosso/IMEA R$ 1.535/t (-0,7% no dia); Rondonópolis/MT R$ 1.560/t (estável); Rio Grande do Sul R$ 1.640/t (-4,09% no dia). O RS mostrou a maior queda em dias recentes — depois de semanas travado em R$ 1.710/t, a quebra para R$ 1.640/t é sinal de que o excedente está chegando ao mercado sul-gaúcho.

**Demanda de ração lenta para absorver excedente — mecanismo de defasagem.** O CEPEA publicou em 18/jun/2026 ("Do farelo à ração: o efeito existe, é relevante, mas não é imediato") que o preço mais baixo do farelo transmite-se à formulação das rações animais, mas com defasagem de semanas a meses — porque os nutricionistas precisam reformular dietas, as compras têm contratos e a substituição de ingredientes não é imediata. Isso significa que, mesmo com farelo barato, a demanda de ração não absorve o excedente no curto prazo. O mercado não tem o mecanismo de "chão de preço imediato" via demanda de ração; o ajuste é lento.

**Posicionamento COT — fundos com exposição longa moderada em farelo.** COT de 09/jun/2026: managed money em farelo net long = +55.447 contratos (long 114.445, short 58.998; open interest 610.926). A proporção long/short de 1,94:1 não está em extremo histórico (diferente do óleo), mas com o preço caindo e o ratio comprimindo, os longs marginais tendem a sair. Uma redução de posição de MM em 10-15k contratos ao longo das próximas duas semanas empurraria o farelo na direção de 290-295 USD/sht. O próximo COT (data de referência ~24/jun) será divulgado na sexta-feira ~27/jun e dará melhor visibilidade sobre esse processo.

### O que invalida / risco para o farelo

- **Crush margin cair abaixo de 2,00 USD/bu**: se a crush derreter para níveis de breakeven das esmagadoras (historicamente 1,50-2,00 USD/bu), parte das plantas menos eficientes pode reduzir o ritmo de esmagamento. Com menos soja processada, a oferta de farelo recua. Esse é o mecanismo paradoxal: o único driver altista do farelo é um colapso do crush que force paralisação das esmagadoras. A crush atual de 2,536 USD/bu ainda está longe desse threshold.
- **China destravar compras massivas de soja EUA**: a China é a maior importadora mundial de soja. Um reingresso em volume (compras acima de 5 mi t anunciadas) puxaria o grão para cima, expandindo o ratio Far/Soj de volta para a zona neutra (83%+) e aliviando a pressão sobre o farelo. Improvável no curto prazo dado os estoques elevados chineses.
- **Ratio cair para <77% sem recuperação**: abaixo de 77%, o farelo torna-se historicamente tão barato em relação à soja que a assimetria de reversão aumenta significativamente. Nesse ponto, o setup operacional muda: deixa de ser "short farelo" e passa a ser "long spread Far/Soj aguardando mean-reversion". A entrada para essa reversão precisa de catalysador (NOPA fraco, corte de esmagamento) para sustentar.
- **NOPA maio (item `release-nopa-2026-06-22`)**: se o esmagamento americano de maio ficou abaixo das expectativas (dado não disponível no sistema), é um sinal de que a oferta de farelo EUA pode estar arrefecendo. A fila registra coleta do item NOPA em 22/jun mas sem conteúdo acessível — ver seção Honestidade.

### Leitura operacional — farelo

O bear no farelo está consolidado mas não acelerado — o preço do contrato julho está em 300,60 USD/sht, praticamente o mesmo dos últimos 5 pregões. A pressão não está sendo precificada em queda de preço agora; está precificada na estrutura (ratio comprimido, curva plana, prêmio export zerado, índice 100/100). Para o trader:

**Regime atual (ratio velho-safra 80,5%):** short farelo direto com stop acima de 305 USD/sht (máxima da semana foi 303,50 em 22/jun) ou short spread Far/Soj velho-safra. O alvo de downside no curto prazo é a zona 288-293 USD/sht (central do modelo estatístico de 7d é 288,82, gerado em 22/jun).

**Regime iminente (ratio new-crop <80%):** o ratio de novembro já está em 78,86%. Quem planeja operações de crush para o novo-safra enfrenta a situação onde o farelo já está "comprimido" e o mean-reversion começará a ter assimetria positiva. Long crush (compra soja Nov + vende farelo F27 + vende óleo F27) pode começar a ter uma relação risco/retorno melhor — mas o timing de entrada requer confirmação de que o mercado não vai continuar afundando em direção a 77% ou menos.

---

## Óleo

**Viés: bear de curto prazo forte — o evento dominante do dia**

O óleo degomado foi o protagonista absoluto do dia 22/jun. A queda de -4,02% em um único pregão (de 69,69 para 66,89 ¢/lb; abertura 66,04, máxima 67,25, mínima 66,02; volume 52.879 contratos; CBOT, 22/jun/2026) representa o movimento de baixa mais intenso em um único pregão no ciclo recente. O suporte de 72,00 ¢/lb havia sido rompido em 18/jun; hoje o óleo consolidou abaixo desse nível e aprofundou a queda para testar a zona de 66-67 ¢/lb, que é exatamente onde os contratos deferred (Z26 66,88, F27 66,60) estão precificados. Trata os itens da fila: `alerta-quebra_suporte-oleo_cbot-2026-06-22` e `alerta-movimento_forte-oleo_cbot-2026-06-22`.

### O que sustenta a tese bear de curto prazo

**O gap de longo fim de semana foi o catalisador.** O mercado americano esteve fechado de quinta-feira (18/jun, último pregão) até segunda-feira (22/jun, Juneteenth na sexta-feira 19/jun + fim de semana). O mercado global de energia seguiu funcionando nesse intervalo — em particular, o crude oil, o heating oil e derivados são negociados em Chicago de forma eletrônica e podem ter tido movimentações na sexta e no fim de semana que o CBOT "engoliu" ao reabrir na segunda. O heating oil fechou em 3,079 USD/galão em 22/jun (abertura 3,180, máxima 3,200, mínima 3,066), queda de -3,2% vs. 3,187 do fechamento de sexta (21/jun conforme dado do sistema). A queda do HO ao longo do holiday weekend carregou o óleo de soja como proxy de derivado vegetal no mecanismo de precificação do biodiesel.

**Posicionamento extremo de fundos em óleo — desmonte em curso.** O COT de 09/jun/2026 registrou managed money em óleo net long = **+128.746 contratos** (long 157.169, short 28.423; open interest 690.051). Esse é o posicionamento mais concentrado do complexo soja tanto em valor absoluto quanto em proporção do open interest. Quando um mercado com posição de fundos nesse nível começa a ceder, o desmonte pode ser amplificado: os longs marginalistas saem primeiro, o que pressiona o preço, o que força os próximos longs a saírem, e assim por diante. Com o óleo já em -6,3% de 15 a 18/jun (de 74,37 para 69,69 ¢/lb) e mais -4,02% hoje, estimamos que parte expressiva desses longs já foi liquidada. O próximo COT (~27/jun) confirmará o tamanho do desmonte.

**Ruptura técnica do suporte de 72,00 ¢/lb — suporte virou resistência.** O óleo havia sustentado o nível de 72,00 ¢/lb como piso durante várias semanas antes do rompimento em 18/jun. Em análise técnica, quando um suporte é rompido, ele tende a se tornar resistência — i.e., tentativas de recuperação acima de 72,00 encontram vendedores posicionados naquele nível. A máxima do dia 22/jun foi apenas 67,25 ¢/lb, muito abaixo de 72,00. O mercado nem tentou recuperar a resistência. O próximo suporte técnico relevante está na zona de 64-65 ¢/lb, que historicamente correspondeu ao piso de demanda de biodiesel nos períodos de margem comprimida.

**Backwardation: N26 70,85 → Z26 66,88 → F27 66,60 ¢/lb.** A curva de óleo está em backwardation acentuada nos contratos próximos, com o julho (N26) em 70,85 ¢/lb — muito acima do contrato "spot" que o sistema rastreia (ZL=F = 66,89, provavelmente refletindo o contrato de maior liquidez atual, possivelmente dezembro). O prêmio do julho (N26 70,85) sobre dezembro (Z26 66,88) é de 3,97 ¢/lb. Isso significa que quem tem estoque físico de óleo imediato recebe um prêmio por entrega agora — mas que o mercado precifica relaxamento expressivo da pressão de demanda ao longo do 2S26. A backwardation nos deferred (Z26 a F27 praticamente plana) confirma que o piso de demanda estrutural existe, mas está a um nível mais baixo do que o preço atual.

**A queda do heating oil encurtou a receita do biodiesel — mas a margem curiosamente melhorou.** Aqui está a nuance mais contraintuitiva do dia: a margem de biodiesel americana calculada pelo sistema em 22/jun é de **0,427 USD/galão** (receita 6,244 USD/galão: HO 3,079 + 1,5×RIN 2,11 = 6,244; custo 5,817 USD/galão: óleo 5,017 + indiretos 0,80; indicadores sistema, 22/jun/2026). Isso é uma **melhora expressiva** em relação a 18/jun (0,266 USD/galão) e inclusive acima de 17/jun (0,194 USD/galão). A explicação: o custo do óleo caiu mais (-0,210 USD/galão, de 5,227 para 5,017) do que a receita caiu (-0,048 USD/galão, de 6,292 para 6,244). Em outras palavras, a queda no preço do óleo está beneficiando o produtor de biodiesel nos EUA — o blender tem margem melhor agora do que quando o óleo estava em 71 ¢/lb.

Por que isso importa? Porque a narrativa de que "heating oil cai → biodiesel margem comprime → demanda de óleo soja cai → óleo soja cai" **não está se verificando no dado de margem**. A margem está se expandindo, o que significa que o incentivo para produzir biodiesel está maior agora do que estava na semana passada. Se o mandato RFS 2026/2027 (BBD em 9,07 bi RINs, +61% a/a, em vigor desde 15/jun) está em ação, os blenders têm mandato E margem melhorada. Isso é um suporte para a demanda de óleo que está sendo ignorado pela ação de preço de curto prazo — o mercado parece estar vendendo o óleo por posicionamento (fundos saindo) mais do que por fundamentos de demanda.

**Oil share em 52,67% — óleo ainda domina, mas beira a zona crítica de 50%.** Série: 15/jun 55,18% → 16/jun 54,47% → 17/jun 53,99% → 18/jun 53,63% → 22/jun 52,67%. Queda de -2,51 pontos percentuais em dez pregões (12 a 22/jun). Se o oil share cruzar 50%, a dinâmica do crush inverte: o farelo volta a ser o produto principal, a esmagadora passa a comprar soja "para extrair farelo" em vez de "para extrair óleo". Esse crossing point é o maior driver estrutural a monitorar — e ele está a menos de 3 pontos percentuais de distância no ritmo atual de declínio.

**Índice Suporte Óleo em 80/100 — 4 das 5 condições estruturais ainda ativas.** O índice se mantém em 80 (4/5 condições de suporte ao óleo) pelos últimos dias. A quinta condição que falta (possivelmente relacionada ao spread óleo vs. heating oil ou ao nível relativo ao carregamento de posição) ainda não foi atingida. Com o óleo em 66,89 ¢/lb, a pressão sobre essa quinta condição deve aumentar.

### O que sustenta o óleo no médio prazo (invalida a tese bear)

O bear de curto prazo existe dentro de uma estrutura de suporte de médio/longo prazo que não desapareceu:

- **RFS 2026/2027 em vigor (15/jun)**: o mandato de BBD em 9,07 bi RINs (+61% a/a) é um piso de demanda garantido por regulação. Os blenders precisam produzir biodiesel independentemente do preço do óleo ou do heating oil. Esse mandato não foi alterado.
- **45Z (crédito fiscal proposto)**: se aprovado na forma proposta, beneficia o óleo soja doméstico americano com ~0,50 USD/galão de crédito fiscal adicional, diferenciando-o de óleos importados. Seria um suporte estrutural que torna o óleo soja US competitivamente superior ao importado para biodiesel.
- **RIN D4 implícito em 2,11 USD/RIN**: o valor do crédito de biodiesel avançado se mantém constante no sistema. No mercado real (ICE/OPIS, acesso pago), o RIN flutua. Um aumento do RIN D4 pelo mercado secundário (demanda por créditos > oferta) expandiria a receita do blender imediatamente e seria bullish para óleo soja.
- **El Niño e geopolítica**: El Niño Advisory ativo pode associar-se a seca no Sudeste Asiático (palma indonésia/malaia), reduzindo a oferta de substitutos do óleo vegetal. A geopolítica no Oriente Médio (conflito EUA-Irã citado no insight de 05/jun) mantém o crude/heating oil em patamar elevado — qualquer escalada eleva a receita do biodiesel e expande a margem do blender.

### Leitura operacional — óleo

A situação do óleo hoje é tecnicamente a mais clara do complexo: curto prazo inequivocamente bearish por técnico (ruptura de suporte, fundos saindo) e por preço (em queda livre), mas médio prazo com suporte estrutural (RFS, 45Z, mandato). O trader precisa separar horizonte:

**Curto prazo (1-4 semanas):** short N26 (Jul) ou Q26 (Ago) com alvo na zona de 64-66 ¢/lb. Stop acima de 69,69 ¢/lb (fechamento de 18/jun que se torna resistência imediata). O downside técnico está confirmado. Atenção: a margem de biodiesel melhorando é um sinal contraintuitivo que pode limitar a queda se os blenders decidirem aumentar produção aproveitando a margem favorável — o que aumentaria a demanda de óleo e funcionaria como "piso natural de margem".

**Calendário spread:** a backwardation de N26 (70,85) para Z26 (66,88) é de -3,97 ¢/lb. Quem está short N26 e long Z26 captura a estrutura da curva ao longo do rolamento — mas a backwardation pode se aprofundar se a pressão vendedora continuar no spot. Verificar com precaução.

**Evitar long de curto prazo:** os 128k contratos de net long de MM em 09/jun (COT) estão em processo de desmonte. Posição extrema em liquidação é o setup mais perigoso para o comprador — a saída dos fundos pode ser violenta e não se esgota em um único pregão.

---

## Spreads e crush — leitura de complexo

### Crush margin: 2,536 USD/bu — compressão acumulada de -43% em 10 pregões

A série completa da crush margin nos últimos 10 pregões (sistema indicators/DB):  
15/jun: 3,632 → 16/jun: 3,427 → 17/jun: 3,255 → 18/jun: 3,067 → 22/jun: 2,536 USD/bu.

A queda de 3,632 para 2,536 em 5 pregões é de -1,096 USD/bu, ou -30%. Se olharmos desde 11/jun (crush estimada em ~3,78 USD/bu, citada no insight de 11/jun): a compressão acumulada é de ~-33% em 10 pregões. **Trata o item `alerta-movimento_forte-complexo_soja-2026-06-22` da fila.**

Qual parte da queda de hoje (-0,531 USD/bu, de 3,067 para 2,536) é óleo e qual é o roll da soja? O óleo contribuiu com a queda do custo do insumo de produção de óleo (2,80 ¢/lb × coeficiente de conversão por bushel). O roll da soja do July para o November eleva o "custo" da soja no denominador do crush — com soja em 1.143,50 vs. 1.122,75 (anterior ZS=F), o custo por bushel sobe em ~0,2075 USD/bu (20,75 ¢/bu / 100), o que, por si só, comprimiria a crush em ~0,21 USD/bu mesmo sem mudança nos produtos. A outra parte do -0,531 é a queda real do óleo. Ou seja: **a crush real, medida em termos de old-crop soja (July), comprimiu menos do que o número nominal indica** — o -0,531 do sistema é parcialmente artefato de roll.

Independentemente disso, a crush de 2,536 USD/bu é ainda lucrativa para praticamente todas as esmagadoras (breakeven estimado em 1,50-2,00 USD/bu). Nenhuma planta vai parar. O esmagamento segue, o farelo continua sendo produzido, e a oferta de subprodutos persiste no mercado.

**O paradoxo do farelo:** a única coisa que poderia reverter o bear estrutural no farelo é justamente uma crush margin que force paralisação do esmagamento — o que exigiria ou que o óleo continuasse caindo agressivamente (até o ponto de tornar a crush não rentável) ou que a soja subisse com tal velocidade que elevasse o custo a ponto de apertar a margem. Estamos a ~0,54-1,04 USD/bu acima do breakeven — o paradoxo está distante mas começa a aparecer no horizonte.

### Oil share: 52,67% — 3 pontos do pivô de 50%

O oil share caiu 0,96 ponto percentual só no dia 22/jun (de 53,63% para 52,67%). A série desde 12/jun (indicadores sistema): 55,21% → 55,18% → 54,47% → 53,99% → 53,63% → 52,67%. Queda de -2,54 pp em 5 pregões. O oil share mede a participação do valor do óleo no valor total dos produtos da crush (óleo + farelo). Sua queda significa que o óleo está perdendo participação na receita do esmagador, o que tem três implicações:

1. **Para o esmagador:** a margem do crush está ficando mais dependente do preço do farelo para compensar a queda do óleo. Se o farelo não subir ao mesmo tempo, o crush aperta por dois lados.
2. **Para o mercado:** se o oil share cruzar 50%, o mecanismo de incentivo do crush inverte — o esmagador passa a comprar soja "para fazer farelo" em vez de "para fazer óleo". Isso mudaria a dinâmica de preços dos três produtos.
3. **Para o calendário:** ao ritmo de -0,5 pp por pregão, o oil share cruzaria 50% em ~5-6 pregões. Isso não é linha reta — o oil share pode se estabilizar se o óleo parar de cair. Mas a trajetória atual apontaria para esse crossing em torno de 29/jun-3/jul.

### Oil-meal spread: 0,745 USD/bu — óleo perde força relativa

O spread óleo-farelo caiu de 1,037 USD/bu (18/jun) para 0,745 USD/bu (22/jun) — queda de -0,292 USD/bu em um pregão. Série histórica recente: 15/jun 1,537 → 16/jun 1,316 → 17/jun 1,164 → 18/jun 1,037 → 22/jun 0,745. Queda acumulada de -0,792 USD/bu em 5 pregões, ou -51,5%. Quando esse spread estiver negativo (farelo gerando mais receita por bushel que o óleo), o complexo terá reequilibrado completamente. Estamos a 0,745 USD/bu de distância desse ponto.

### Ratio Far/Soj: dois mundos — old-crop 80,48%, new-crop 78,86%

O dado mais importante para o operador de crush é a dualidade de ratio neste momento. O old-crop (July) mostra 80,48%, praticamente idêntico ao de 18/jun (80,51%) — sem movimento. O new-crop (November) mostra 78,86% — abaixo de 80% pela primeira vez neste ciclo. O mercado está dizendo que, na perspectiva do novo-safra (quando as esmagadoras vão comprar soja de nova-safra para processar a partir de setembro), a relação farelo/soja já está na zona de barato histórico. O setup de mean-reversion (long farelo/short soja no horizonte de novo-safra) começa a ter mais atratividade estrutural, mas ainda não há trigger imediato.

---

## Lente fiscal e regulatória BR

O quadro regulatório brasileiro não mudou desde a última leitura, mas três eventos de curto prazo merecem atenção crescente:

**Isenção PIS/Cofins biodiesel — vencimento em 31/jul/2026 (38 dias).** O decreto de prorrogação de 29/mai/2026 estica a isenção até 31/jul/2026. Após essa data, se não houver nova prorrogação, o custo do biodiesel para as distribuidoras sobe — PIS/Cofins sobre biodiesel é da ordem de R$ 0,35-0,50/litro, o que tornaria a blenda B15 economicamente menos atrativa para distribuidoras que não estejam no mandato. O efeito para o trader de óleo soja BR: sem renovação da isenção, a demanda de óleo para biodiesel BR pode arrefecer na margem. O prazo está próximo e nenhuma sinalização de nova prorrogação consta no briefing. Esse é um risco real de curto prazo para o óleo BR.

**B16 sem data — mandato de biodiesel estagnado em B15.** O aumento do mandato de biodiesel de B14% (atual) para B16% (proposto) está parado desde o cancelamento da reunião do CNPE em 11/mai/2026. Os testes técnicos de compatibilidade (R$ 30 mi do FNDCT, prazo de 6 meses) provavelmente só entregarão resultados em novembro/dezembro de 2026. Sem B16, o crescimento marginal da demanda de óleo de soja para biodiesel BR não acontece. Para o trader de óleo, B16 é bull de médio prazo (2027), não de curto prazo.

**MP 1.363/2026 (subvenção ao diesel fóssil) — em vigor até 31/dez/2026.** O subsidio de R$ 1,12/litro para o diesel fóssil mantém o diesel artificialmente barato, o que elimina qualquer demanda "voluntária" de biodiesel por parte das distribuidoras além do mandato obrigatório. O biodiesel BR está 100% ancorado no mandato — sem crescimento marginal. Bear para óleo BR além do mandato.

**STJ REsp 2.165.276/2026 — favorável às esmagadoras, sem efeito imediato nos preços.** A decisão do STJ em 21/mai/2026 foi favorável ao direito das esmagadoras de creditar PIS/Cofins sobre soja comprada sob suspensão de imposto. Positivo para margem das esmagadoras no médio prazo, mas não vinculante (não é recurso repetitivo), e não tem impacto imediato nos preços de mercado.

**Conclusão fiscal BR:** o quadro regulatório é neutro a levemente bearish para o óleo interno no curto prazo. O único prazo crítico iminente é a expiração da isenção PIS/Cofins em 31/jul/2026. B16 e qualquer driver bull de mandato mais alto ficam para 2027.

---

## Riscos e eventos próximos

**Fila de eventos que o trader deve monitorar:**

**USDA Crop Progress — semana de 23/jun (publicação ~23-24/jun):** a próxima publicação semanal de condição de lavoura de soja EUA chegará ainda esta semana. Com a lavoura em 66% boa/excelente e a janela de risco climático de julho se abrindo (estágio de florescimento e enchimento de vagens), qualquer deterioração de 5 pontos percentuais ou mais (para 60% ou menos) seria catalisadora de alta. O El Niño Advisory oferece proteção estatística, mas não é seguro.

**USDA Acreage + Quarterly Grain Stocks — 30/jun:** dois relatórios simultâneos de grande impacto. O Acreage deve confirmar (ou reverter) o "acreage boost" mencionado pela FarmProgress em 18/jun. O Grain Stocks fornecerá o estoque de final de trimestre em 01/jun — se o estoque de soja estiver abaixo da expectativa, é altista para o contrato velho-safra (July). Ambos os dados ainda não estão no sistema.

**WASDE julho (~10/jul):** revisão mensal de área, produção e estoques mundiais. Pontos-chave para o complexo: soja EUA 2026/27 (confirma o acreage boost?), farelo Argentina (carryover ainda em alta?), óleo soja US (estoques e consumo doméstico com RFS em vigor), Brasil soja 2026/27 (base para o crush planning 2S26).

**COT CFTC próximo (~27/jun):** o posicionamento de managed money em óleo (128k net long em 09/jun) estava em extremo. O COT de ~27/jun refletirá a posição de ~23-24/jun — ou seja, captura parte do desmonte dos últimos dias. Se a posição MM óleo cair para abaixo de 80k contratos, confirma o ciclo de saída; se mantiver, indica força residual.

**NOPA (fila `release-nopa-2026-06-22`):** o esmagamento americano de maio é uma peça crítica do quebra-cabeça do farelo. O sistema registra coleta de dado NOPA em 22/jun, mas o conteúdo não está acessível (membership pago). O número de esmagamento de maio EUA (se +10% a/a confirma oversupply; se abaixo do esperado, é sinal de alívio).

**WASDE (fila `release-usda_wasde-2026-06-22`):** o sistema sinalizou um item novo do WASDE datado de 22/jun. A leitura mais provável é que o scraper atualizou a base USDA em 22/jun com os dados já publicados do WASDE de 11/jun (o USDA às vezes reprocessa tabelas). Não há WASDE mensal previsto para 22/jun no calendário regular. Os dados numéricos no briefing continuam referenciando 11/jun — não há novos números interpretativos disponíveis.

**Isenção PIS/Cofins biodiesel (31/jul):** faltam 38 dias para o vencimento. Qualquer declaração do governo federal sobre renovação (ou silêncio) é sinal para o óleo BR.

**B16 (CNPE):** qualquer convocação de reunião do CNPE é evento de alta relevância para o óleo de médio prazo. Sem data.

**El Niño → Watch/Warning:** o Advisory atual (NOAA, 22/jun/2026) indica El Niño em desenvolvimento. Se o status subir para Watch ou Warning nas próximas semanas, as implicações para a safra BR 26/27 (plantio em set/out) e argentina (florescimento em dez/jan) começam a entrar no pricing. El Niño tipicamente associa-se a seca no Sul do Brasil e na Argentina durante o florescimento — o que seria altista para soja e farelo do novo-safra.

---

## Honestidade

O que não foi possível validar ou está ausente no briefing de 22/jun/2026:

**1. PTAX de 20-22/jun ausente.** O BCB não divulga PTAX em fins de semana e o Juneteenth fechou o mercado americano na sexta (19/jun). O último PTAX disponível é de 19/jun/2026 (5,1442 BRL/USD). A paridade de soja BR calculada pelo sistema usa esse câmbio de 3 dias atrás — pode estar desatualizada se o real se moveu na sexta-feira nos mercados internacionais.

**2. NOPA maio (item `release-nopa-2026-06-22`):** o sistema registra coleta do dado NOPA em 22/jun, mas o relatório mensal de esmagamento da NOPA (National Oilseed Processors Association) requer membership pago. O conteúdo efetivo não está disponível. Toda a tese de oversupply de farelo depende parcialmente da continuidade do esmagamento americano em ritmo elevado — sem o NOPA de maio, há lacuna real.

**3. WASDE 22/jun (item `release-usda_wasde-2026-06-22`):** o sistema sinalizou novo item do WASDE com data de 22/jun. Os dados WASDE no briefing são do relatório de 11/jun (dados reais, confirmados). O item da fila provavelmente reflete uma atualização de scraper/coleta, não um novo relatório mensal — mas sem confirmar o conteúdo, não é possível saber se há dados novos e relevantes.

**4. Palma MPOB:** o parser do MPOB segue sem extrair números por 12+ dias consecutivos (ao menos de 11 a 22/jun/2026). Sem preço ou estoque de palma da Malásia, não é possível calibrar a competição óleo soja vs palma no mercado global de biodiesel e alimentício — um driver relevante para o óleo.

**5. BCBA Argentina:** acessível mas sem links de relatório detectados por múltiplos dias. Sem dados de esmagamento, exportação ou produção argentinos atualizados no sistema além do WASDE de 11/jun.

**6. COT com 13 dias de defasagem:** o último dado disponível é o COT de 09/jun. Dada a magnitude das movimentações no óleo nos últimos dias (queda de 74 para 66 ¢/lb = -10,7%), o posicionamento real de managed money hoje certamente difere dos +128k net long do COT de 09/jun. A dimensão do desmonte é desconhecida até o COT de ~27/jun.

**7. RIN D4 preço de mercado:** o sistema usa RIN D4 implícito de 2,11 USD/RIN como constante. O preço real do RIN D4 flutua diariamente no mercado secundário (CME/OPIS, acesso pago). A margem de biodiesel calculada (0,427 USD/galão) pode diferir da real se o RIN D4 se moveu nos últimos dias.

**8. Basis Paranaguá óleo:** prêmio de +0,08 ¢/lb (NAG, 19/jun) — série muito curta e dado de 3 dias atrás. Sem contexto histórico para avaliar se é mínimo ou valor normal.

*Nenhum número foi inventado. Todas as estimativas e mecanismos descritos são derivados dos dados disponíveis no briefing. As incertezas acima são lacunas reais e materiais do conjunto de dados disponível em 22/jun/2026.*
