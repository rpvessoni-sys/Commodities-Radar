---
data: 2026-09-11
titulo: "Terceiro pregão pós-pausa resolve o empate: soja rompe para nova máxima da janela com volume voltando a 90% do normal, farelo sobe em dólar mas perde terreno no ratio Far/Soj (78,93%, se afastando de 80% de novo), e o óleo salta com a maior margem de biodiesel americana da série — puxada por um heating oil que subiu ~7% em um único dia — ficando a só 0,76% de reconquistar o suporte de 72,00"
tags: [complexo, auto-claude]
fontes:
  - CME CBOT (ZSX26 soja / ZMV26 farelo / ZLV26 óleo) — sessão de 2026-09-10 (quinta-feira), terceiro pregão pleno desde a reabertura de 08/09. Soja: abertura 1.309,50, máxima 1.333,50, mínima 1.305,00, fechamento 1.331,75 USD cts/bushel, volume 151.466 contratos (ticker ZSX26.CBT, venc. nov/26). Farelo: abertura 344,50, máxima 350,70, mínima 343,40, fechamento 350,40 USD/short ton, volume 27.147 contratos (ticker ZMV26.CBT, venc. out/26). Óleo: abertura 70,22, máxima 71,54, mínima 69,41, fechamento 71,45 USD cts/lb, volume 23.831 contratos (ticker ZLV26.CBT, venc. out/26). Curva futura em 10/09 — soja: set/26 1.318,25, nov/26 (base) 1.331,75, jan/27 1.347,00, mar/27 1.352,50, mai/27 1.356,75, jul/27 1.358,75; farelo: set/26 349,00, out/26 (base) 350,40, dez/26 356,80, jan/27 358,70, mar/27 359,70, mai/27 360,30; óleo: set/26 71,00, out/26 (base) 71,45, dez/26 71,97, jan/27 72,24, mar/27 72,37, mai/27 72,33
  - CME CBOT 2026-09-09 (quarta-feira) — farelo fechamento bruto 345,10 USD/short ton (volume 28.688, linha própria presente no dump). Soja (fechamento 1.309,50) e óleo (fechamento 70,08) **não têm linha bruta de CME CBOT nesta janela do dump** — os dois valores usados como base de comparação são reconstruídos a partir das fórmulas dos indicadores sintéticos de 09/09 (`complexo_soja.crush_margin_usd_bu` e `biodiesel_us.custo_oleo_usd_galao`, indicators); ver seção Honestidade para a pequena divergência frente aos valores brutos (70,04 óleo / 1.308,75 soja) citados por [[2026-09-10_leitura-complexo]], que dispunha de outra janela de dump
  - CME NYMEX heating oil (HO=F) — 2026-09-10: abertura 5,1481, máxima 5,1525, mínima 5,1290, fechamento 5,1422 USD/galão, volume 389 contratos — salto implícito de aproximadamente **+7,1%** frente aos ~4,80 USD/galão embutidos no cálculo de receita de biodiesel de 09/09 (linha bruta de 09/09 no dump está truncada em "abertura 4,6205", sem fechamento próprio)
  - Indicadores sintéticos internos (crush margin, ratio Far/Soj, oil share, oil-meal spread, ISF, ISO, margem biodiesel, paridade BR) — 2026-09-10, terceiro recálculo com insumo de preço fresco desde a reabertura
  - BCB PTAX — 2026-09-10: USD/BRL 5,1149, EUR/BRL 5,9481, Selic diária 0,05166% a.a. (séries SGS 1, 21619, 11); 2026-09-09: USD/BRL 5,0979, EUR/BRL 5,9278
  - CEPEA/ESALQ Soja Paranaguá via NAG — última leitura disponível 2026-09-09: R$ 160,12/saca (var -0,21%); sem atualização própria para 10/09 nesta janela do dump (defasagem de publicação normal da fonte)
  - CEPEA/ESALQ Soja Paraná interior via NAG — última leitura disponível 2026-09-09: R$ 152,43/saca (var +0,13%); mesma ausência de atualização para 10/09
  - NAG Físico BR — última leitura disponível 2026-09-09: farelo MT/IMEA R$ 1.875,45/ton (var 0,0%, congelado desde 04/09 — agora 6º dia corrido sem variação até 09/09, 7º até hoje 11/09), Rondonópolis/MT R$ 1.900,00/ton (congelado), RS média R$ 1.860,00/ton (congelado); prêmios export Paranaguá farelo +0,12 USD/short ton e óleo +0,10 cts/lb, ambos congelados desde 27/08 (14 dias corridos até 09/09, 15 até hoje 11/09)
  - CFTC COT Managed Money, Swap Dealers e Producer/Merchant — corte de 2026-09-01 (terça-feira), sem atualização nesta janela; 9 dias corridos de defasagem frente ao dado mais fresco do dump (10/09), **10 dias corridos frente a hoje (11/09)** — o próximo corte (posições de 08/09), estimado pela leitura de ontem para sair "amanhã, sexta-feira 11/09", ainda não aparece nesta janela
  - USDA Crop Progress — corte mais recente, semana encerrada em 2026-09-06: 12% excelente / 46% boa / 9% ruim (G/E 58%), inalterado desde 30/08; defasagem de 5 dias corridos frente a hoje (11/09)
  - USDA WASDE — ausente da janela deste briefing
  - NOPA — fila `release-nopa-2026-09-10`; `monthly_status` segue em 0,0 bool (paywall) em todas as datas do dump, de 2026-08-27 a 2026-09-10 — quarto dia seguido do mesmo falso positivo na fila
  - ABIOVE projeções mensais — balanços set-dez/2026, sem revisão nesta janela (mesmos números já usados em 09 e 10/09)
  - NOAA CPC ENSO — El Niño Advisory, inalterado até 2026-09-10
  - MPOB — carimbo 2026-09-10, parser sem números extraídos (mesma barreira, 3.457 caracteres, praticamente idêntico ao carimbo anterior)
  - BCBA (Argentina) — carimbo 2026-09-09, scraper acessa a página mas não encontra links de relatório
  - INMET — previsão para 2026-09-11 (HOJE): chuva e trovoadas seguem no núcleo produtor de Mato Grosso e no Sul, com calor intenso em MT (Cuiabá 37°C/26°C, Sinop 38°C/23°C, Sorriso 37°C/23°C, Lucas do Rio Verde 37°C/23°C, Rio Verde/GO 33°C/20°C) e chuva/trovoada no Sul sem menção de geada (Cascavel/PR 24°C/15°C, Maringá/PR 27°C/18°C, Passo Fundo/RS 24°C/14°C)
  - Notícias Agrícolas/Canal Rural + FarmProgress RSS — 2026-09-10: "0 items lidos, 0 mantidos (soja/farelo/oleo)" — falha ou pausa total de coleta nesta data, sem manchete nova
  - CEPEA RSS — última leitura 2026-09-09: 109 itens parseados (ante 103 em 08/09); última manchete de preço disponível permanece a de 04/09 ("Alta dos preços ganha força no início de setembro")
  - system/tributario_watch.toml (lido como referência, não editado) — `atualizado_em` 2026-06-05 em todos os 10 eventos catalogados, agora **98 dias corridos** sem revisão humana frente a hoje (11/09)
  - Forecasts estatísticos internos (bandas 7d/30d, MA20+volatilidade+slope) — geração de 2026-09-10, alvos 17/09 (7d) e 10/10 (30d); viés "altista" em soja e farelo nos dois horizontes, "lateral" no óleo em 7d e "altista" no óleo em 30d, calculado sobre o fechamento de 10/09
  - Fila de julgamento (carimbada 2026-09-10 no briefing, 7 itens) — tratados nesta leitura: `alerta-quebra_resistencia-soja_cbot-2026-09-10`, `alerta-quebra_suporte-oleo_cbot-2026-09-10`, `alerta-quebra_resistencia-farelo_cbot-2026-09-10`, `alerta-quebra_suporte-complexo_soja-2026-09-10`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`, `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`, `release-nopa-2026-09-10`
  - Cruza com [[2026-09-10_leitura-complexo]] (leitura de ontem, que documentou o segundo pregão de reversão parcial farelo↑/óleo↓ e o segundo dia seguido de queda de volume em soja) e com [[2026-09-09_d90-ratio-far-soj-reverte-na-vespera]] (veredito da revisão D+90 da tese original do ratio Far/Soj, aberta em [[2026-06-11_ratio-81-prepara-janela-de-tranches-farelo]])
status: ativa
vies: [bull-soja, bear-farelo, bull-oleo_soja]
---

## Visão geral

Hoje, sexta-feira 11/09/2026, o dado mais fresco do briefing é o fechamento de
quinta-feira 10/09 — o terceiro pregão pleno na CBOT (bolsa de grãos de Chicago,
onde soja, farelo e óleo de soja são negociados em contratos futuros) desde a
reabertura de terça-feira 08/09, depois da pausa de quatro dias por feriado duplo
(Labor Day nos EUA e Independência do Brasil). Para quem não acompanha o dia a dia:
quando a soja em grão é esmagada ("crush", o processo industrial que separa o grão em
farelo e óleo), ela vira dois produtos com demandas muito diferentes — farelo
(concentrado de proteína usado em ração animal) e óleo (usado em alimentação humana e,
cada vez mais, em biodiesel). O "crush margin" mede, em dólares por bushel (unidade
agrícola americana de ~27,2 kg de soja), quanto sobra para a esmagadora depois de
vender farelo + óleo e pagar a soja — é a rentabilidade do negócio de processar grão. O
"oil share" (fatia do valor total do crush que vem do óleo, com farelo+óleo somando
100%) diz qual dos dois produtos está "pagando a conta": oil share alto significa que o
óleo manda e o farelo vira insumo residual, mais barato, "sobra" — daí o índice
sintético interno "Índice de Sobra de Farelo" (ISF, 0-100, quanto mais alto mais
baixista para o farelo). Oil share baixo significa o contrário: o farelo sustenta o
crush e o óleo perde força relativa, o que o índice espelhado "Índice de Suporte do
Óleo" (ISO) capta pelo lado inverso. O ratio Far/Soj (preço do farelo dividido pelo
preço da soja, normalizado em percentual) é a métrica clássica de mercado para a mesma
ideia: abaixo de 80% o farelo está "abundante" (barato relativo à soja, viés
baixista); a partir de 87% ele está "apertado" (caro relativo à soja, viés altista).

As duas últimas leituras descreveram um empate técnico: no primeiro pregão pós-pausa
(08/09) o farelo caiu e o óleo subiu; no segundo (09/09) o movimento se inverteu quase
espelhado. O terceiro pregão, o de hoje (10/09), rompeu esse padrão de vaivém e trouxe
o primeiro dia em que os três produtos do complexo subiram juntos em dólar: soja
+1,70% (1.309,50 → 1.331,75, CME CBOT), farelo +1,54% (345,10 → 350,40) e óleo +1,95%
(70,08 → 71,45, valores de 09/09 reconstruídos via indicadores — ver Honestidade). Mas
"subir junto" não significa "subir igual", e é exatamente a diferença de magnitude que
conta a história do dia: a soja subiu mais rápido que o farelo, então o ratio Far/Soj
**recuou** de 79,06% para **78,93%** (indicators, 10/09) — se afastando de novo do
patamar de 80% depois de ter chegado à menor distância da série (0,92 ponto percentual)
ontem. Ao mesmo tempo, o óleo subiu mais rápido que a soja e muito mais rápido que o
farelo, então tanto o oil share (50,38% → 50,48%) quanto o oil-meal spread (+0,1166 →
+0,1507 USD/bushel, uma alta de +29,3% no spread) se moveram a favor do óleo. O evento
isolado mais importante da sessão, porém, veio de fora do complexo da soja: o heating
oil americano (diesel de aquecimento, cujo preço entra direto na conta de receita do
biodiesel) saltou cerca de **+7,1%** em um único dia (de ~4,80 para 5,1422 USD/galão,
CME NYMEX), levando a margem de biodiesel americana a um novo recorde da série — US$
**2,1485/galão**, ante US$ 1,91 em 09/09 (indicators), uma alta de **+12,5%**. Esse é o
segundo dia seguido de recorde na margem de biodiesel, o que começa a parecer menos
ruído e mais uma tendência de fundo genuína de demanda por óleo como insumo. E o dado
que resolve a dúvida da leitura de ontem sobre "convicção do mercado": o volume de soja
voltou a **151.466 contratos** (CME CBOT, 10/09), uma alta de **+51,4%** sobre os
100.017 de 09/09 e a apenas -9,4% do volume da última sessão plena pré-pausa (167.214
em 04/09) — a queda de dois dias seguidos que preocupou a leitura de ontem foi
revertida com folga. **Leitura de uma linha**: o pivô do complexo continua sendo a
realocação de valor entre farelo e óleo dentro do crush, mas hoje o óleo venceu essa
disputa de forma mais clara do que em qualquer sessão desde a reabertura — puxado por
um driver externo (heating oil) que não tem relação direta com a safra de soja — mesmo
enquanto o farelo também subiu em dólar bruto. Confiança **moderada**: o retorno do
volume ao normal dá mais peso à leitura de preço de hoje do que às duas sessões
anteriores, mas o COT (posicionamento dos fundos) que era esperado para hoje ainda não
apareceu no dump, e isso segue sendo a maior lacuna para validar qualquer uma das teses.

## Soja

**Viés: bull, forte — o terceiro pregão pós-pausa trouxe nova máxima da janela, o
primeiro dia com volume próximo do normal desde a reabertura, e a preocupação de ontem
(volume caindo por dois dias seguidos) foi revertida com folga.**

O que sustenta a tese:

- **Novo fechamento máximo da janela, com folga técnica ampliada sobre a resistência de
  referência.** Soja CBOT fechou em **1.331,75** USD cts/bushel em 10/09/2026 (CME
  CBOT), **+1,70%** sobre os 1.309,50 (fechamento reconstruído) de 09/09 — o maior
  fechamento nominal de toda a série desde a reabertura, superando os 1.320,75 de
  máxima intraday do pregão de 09/09. A folga sobre a resistência de 1.180,00
  monitorada pela fila (`alerta-quebra_resistencia-soja_cbot-2026-09-10`) saltou para
  **12,86%**, ante 10,91% no dia anterior — a maior distância desde a abertura do
  rompimento. O contrato negociou entre 1.305,00 e 1.333,50 (mínima/máxima, CME CBOT) e
  fechou a apenas **1,45%** de distância do topo do range (1.331,75 de fechamento contra
  1.333,50 de máxima) — o fechamento mais forte, relativo ao próprio range do dia, de
  toda a série pós-pausa, o oposto exato do fechamento fraco perto do fundo observado
  ontem.
- **O volume voltou com força, resolvendo a dúvida mais importante deixada pela leitura
  de ontem.** 151.466 contratos em 10/09 (CME CBOT, ZSX26), uma alta de **+51,4%** sobre
  os 100.017 de 09/09 — o primeiro aumento de participação desde a reabertura, depois de
  duas quedas seguidas (-24,5% e -20,8%). Frente à última sessão plena pré-pausa
  (167.214 contratos em 04/09), a distância caiu de -40,2% para apenas **-9,4%** — ou
  seja, o book está, pela primeira vez desde a reabertura, perto do volume "normal" de
  antes da pausa. O mecanismo a observar: um rompimento técnico sustentado por volume
  crescente é estruturalmente mais confiável do que um sustentado por volume
  decrescente — a leitura de ontem havia marcado a possibilidade de que a queda de
  volume por dois dias seguidos virasse "falta de convicção estrutural" num terceiro
  pregão; o que aconteceu foi o oposto, e isso é o principal motivo para subir a
  convicção do viés de hoje de "moderado" para "forte".
- **O câmbio trabalhou contra o produtor brasileiro nesta sessão, mas não o suficiente
  para impedir uma paridade em reais recorde da janela.** USD/BRL fechou 10/09 em
  **5,1149** (BCB PTAX), **+0,33%** sobre os 5,0979 de 09/09 — o real se desvalorizou.
  Ainda assim, como o CBOT em dólar subiu muito mais (+1,70%) do que o câmbio se
  desvalorizou, a paridade em reais da soja (CBOT × câmbio, sem basis) fechou em **R$
  150,17/saca** (indicators, 10/09), uma alta de **+2,04%** frente aos R$ 147,17 do dia
  anterior — o maior valor de paridade de toda a série recente. É o mesmo lembrete de
  sempre: para quem vende em reais, a combinação dos dois preços manda, não cada um
  isolado; hoje os dois jogaram juntos a favor do vendedor brasileiro em dólar
  convertido, mesmo com o real mais fraco reduzindo ligeiramente o ganho líquido.
- **A estrutura da curva futura segue em contango saudável e sem distorção, mesmo após
  a alta forte.** Set/26 1.318,25 → nov/26 (base) 1.331,75 → jan/27 1.347,00 → mar/27
  1.352,50 → mai/27 1.356,75 → jul/27 1.358,75 (CME CBOT, 10/09) — uma progressão de
  carry regular, sem inversão nem distorção pontual, e sem sinal de que o mercado esteja
  precificando escassez imediata que justificasse um prêmio anormal no contrato mais
  próximo. O mecanismo: contango consistente ao longo de toda a curva costuma refletir
  custo de carregamento normal — um pano de fundo saudável para um rompimento de alta,
  não um sinal de estresse.
- **A condição da lavoura americana segue estável, sem novidade nesta janela.** USDA
  Crop Progress permanece no corte da semana encerrada em 06/09 (12% excelente + 46%
  boa, "ruim" 9%, G/E 58%), idêntico ao corte de 30/08. A defasagem frente a hoje
  (11/09) é de **5 dias corridos**. O próximo corte é esperado na segunda-feira 14/09 —
  se a condição da lavoura piorar, isso reforçaria o viés de alta atual; se melhorar,
  seria o primeiro contraponto fundamentalista real ao rompimento técnico.

**O que invalida / risco:**

- **O crush margin segue comprimido, mesmo com a soja subindo.** Fechou em **US$
  2,2508/bushel** em 10/09 (indicators), **-9,97%** abaixo do referencial de US$ 2,50
  monitorado pela fila (`alerta-quebra_suporte-complexo_soja-2026-09-10`) — uma melhora
  frente aos -11,72% de ontem, mas ainda a décima sessão seguida abaixo do referencial.
  Uma margem de esmagamento comprimida por período prolongado tende a reduzir o
  incentivo da indústria para processar soja, o que no médio prazo pode pesar sobre a
  demanda física por grão, mesmo com o preço em alta.
- **Nível técnico a vigiar:** um fechamento de volta abaixo de 1.180 desfaria o
  rompimento; com a folga em 12,86% e o fechamento de hoje perto do topo do range, esse
  risco parece hoje mais distante do que em qualquer ponto da série pós-pausa.
- **O COT que era esperado para hoje (posições de 08/09) ainda não aparece no dump** —
  se os fundos tiverem reduzido posição comprada na semana, isso poderia contrastar com
  a força de preço e volume observada hoje; sem esse dado, a leitura de "convicção"
  desta sessão se apoia inteiramente em preço e volume, não em posicionamento.

**Leitura operacional:** o terceiro pregão pós-pausa é o primeiro que junta alta de
preço, fechamento forte dentro do range e volume em recuperação — a combinação mais
favorável ao lado comprado desde a reabertura. Para quem está comprado, não há motivo
para reduzir; há argumento razoável para tratar o nível de hoje como confirmado, não
apenas testado. Para quem opera o lado vendido isoladamente, o nível a vigiar continua
sendo 1.180, mas a folga de 12,86% e o padrão de volume tornam esse cenário mais remoto
no curto prazo do que ontem. Para quem opera a paridade em reais, hoje foi o melhor dia
da série para quem vende soja física em reais, mesmo com o real mais fraco corroendo
uma fração pequena do ganho em dólar.

## Farelo

**Viés: bear, moderado — o preço subiu em dólar pela segunda sessão seguida, mas o
ratio Far/Soj voltou a se afastar de 80% depois de ter chegado à menor distância da
série ontem, porque a soja subiu ainda mais rápido. O farelo está subindo em termos
absolutos, mas perdendo força relativa dentro do crush — exatamente o mecanismo que
sustenta a tese de abundância desde junho.**

O que pesa a favor e contra a tese, em direções diferentes:

- **O preço subiu em dólar, mas menos do que soja e óleo — e é essa diferença de
  velocidade que importa, não o sinal isolado.** Farelo CBOT fechou em **350,40** USD/
  short ton em 10/09/2026 (CME CBOT), **+1,54%** sobre os 345,10 de 09/09 — a segunda
  alta seguida, acumulando +2,08% desde 08/09. Isoladamente, isso pareceria um sinal
  altista. O contrato negociou entre 343,40 e 350,70 (mínima/máxima, CME CBOT) e fechou
  a 97% de distância do fundo do range — um fechamento muito forte dentro do próprio
  pregão. A folga sobre a resistência de 325,00
  (`alerta-quebra_resistencia-farelo_cbot-2026-09-10`) subiu para **7,82%**, ante 6,15%
  no dia anterior. Mas o preço absoluto do farelo, sozinho, não é a métrica que a tese
  de junho usa — o que importa é o preço do farelo *relativo* à soja, e é aí que a
  imagem muda.
- **O ratio Far/Soj recuou, se afastando de 80% pela primeira vez em duas sessões.**
  Fechou em **78,93%** em 10/09 (indicators), ante 79,06% em 09/09 — um recuo de **-0,13
  ponto percentual**, revertendo parte do avanço de +0,83 p.p. registrado ontem. A
  distância até 80% voltou a abrir, de 0,92 para **1,07 ponto percentual**. O mecanismo
  é simples e é o ponto central desta seção: o ratio é farelo dividido por soja
  (normalizado); quando os dois sobem juntos mas a soja sobe mais rápido (+1,70% vs
  +1,54% do farelo), o ratio cai mesmo com o farelo em alta nominal. Na definição do
  próprio indicador (<80% = "abundante", >=87% = "apertado"), o farelo segue na zona de
  abundância, e hoje ficou um pouco mais dentro dela, não mais perto da borda.
- **Os índices sintéticos permanecem parados pela terceira sessão seguida.** O Índice de
  Sobra de Farelo (ISF) permaneceu em **80/100** ("forte pressão baixista no farelo", 4
  de 5 condições, indicators, 10/09) — o mesmo valor de 08 e 09/09. Três sessões
  consecutivas de preço em direções diferentes (queda, alta, alta) não moveram a
  contagem de condições nenhuma vez, reforçando a leitura de que o ISF é uma métrica
  discreta e "pesada", que reage a mudanças estruturais, não a oscilações diárias de
  preço.
- **O oil-meal spread se ampliou de forma acentuada, o sinal mais claro da sessão de que
  o óleo "venceu" a disputa por valor dentro do crush hoje.** Fechou em **+0,1507**
  USD/bushel em 10/09 (indicators), ante +0,1166 em 09/09 — uma alta de **+29,3%** no
  valor do spread. O óleo subiu 1,95% contra 1,54% do farelo — uma diferença de 0,41
  ponto percentual de velocidade que, multiplicada pelo tamanho dos contratos, é
  suficiente para abrir o spread nessa magnitude. O mecanismo de fundo: quando o óleo
  sobe mais rápido que o farelo dentro do mesmo crush, a esmagadora captura mais valor
  pela perna do óleo, reforçando o incentivo a processar soja "pelo óleo" e tratar o
  farelo, de novo, como subproduto.
- **O físico brasileiro segue completamente congelado — a última leitura disponível é
  ainda a de 09/09, sem atualização própria para 10/09 nesta janela.** Farelo MT/IMEA
  (NAG) permaneceu em R$ 1.875,45/ton na última leitura (09/09, var 0,0%), o mesmo nível
  desde 04/09 — agora 6 dias corridos sem variação até aquela data. O prêmio de
  exportação em Paranaguá segue travado em +0,12 USD/short ton há 14 dias corridos
  (desde 27/08, NAG, leitura de 09/09). Nem a alta de dólar dos últimos dois pregões em
  Chicago teve qualquer contrapartida visível no físico doméstico até a última leitura
  disponível — reforça a leitura de que o físico brasileiro de farelo está, por ora,
  isolado das oscilações diárias de Chicago.

**Trata a fila `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+7`
(recorrente 🔴, o mesmo item sinalizado como "vencido" há semanas):** nenhuma mudança na
leitura de fundo — o ratio passou a esmagadora maioria dos 90+ dias desde 11/06/2026
abaixo de 80%, e o dado de hoje (78,93%, se afastando do patamar) é mais uma
confirmação do que uma contradição dessa leitura.

**Trata também `revisao-2026-06-11_ratio-81-prepara-janela-de-tranches-farelo-D+90`
(recorrente, o mesmo marco já vencido e julgado em 09/09):** o veredito de fundo já foi
entregue em profundidade em
[[2026-09-09_d90-ratio-far-soj-reverte-na-vespera]] — a tese original de abundância de
farelo **não foi invalidada** pelos 90 dias corridos. O dado de hoje reforça esse
veredito em vez de contestá-lo: depois de uma aproximação a 79,08% (09/09, a menor
distância de 80% de toda a série), o ratio recuou de novo para 78,93% no primeiro
pregão em que a soja teve um dia de alta mais forte que o farelo. Em três sessões
completas desde a reabertura, o ratio oscilou entre 78,25% e 79,08% sem nunca tocar
80% — um padrão de oscilação dentro da zona de abundância, não uma tendência de ruptura
dela. A leitura operacional prática permanece a mesma de ontem: quem está short farelo
(ou vendido no spread Far/Soj, ou seja, comprado em farelo e vendido em soja — não é o
caso aqui, é o oposto: vendido em farelo e comprado em soja) não tem, com os dados de
hoje, motivo para fechar a posição; o gatilho concreto continua sendo um fechamento
acima de 80% pela primeira vez desde 11/06/2026, o que ainda não aconteceu.

**O que invalida / risco:** o COT segue sendo o contraponto mais relevante, agora com
**10 dias corridos de defasagem** frente a hoje — o corte de 01/09 mostrava o net long
de managed money em farelo tendo saltado +63,83% na semana anterior (95.953 → 157.179
contratos, CFTC COT). O corte seguinte (posições de 08/09), que a leitura de ontem
esperava para hoje, ainda não apareceu nesta janela — enquanto ele não sair, não há como
saber se os fundos ampliaram, mantiveram ou reduziram essa convicção comprada ao longo
da semana de reabertura, e qualquer uma das três sessões de preço observadas até aqui
poderia ser ruído dentro de uma tendência de posicionamento maior que os dados ainda não
capturam.

**Leitura operacional:** para quem está vendido em farelo, a sessão de hoje é uma
confirmação parcial a favor da posição depois do susto de ontem — o ratio voltou a se
afastar de 80%, e mesmo com o preço nominal do farelo subindo, a métrica relevante para
a tese (o ratio) foi na direção esperada. Não é motivo para aumentar posição
agressivamente sem o COT fresco, mas reduz a urgência de apertar stop que a leitura de
ontem havia sinalizado. Para quem opera o spread Far/Soj (long soja / short farelo,
apostando que a soja sobe mais que o farelo), o dia de hoje foi o mais favorável a essa
perna desde a reabertura, com o spread de valor dentro do crush (oil-meal spread)
também se ampliando na mesma direção geral (a favor do óleo/soja, contra o farelo).

## Óleo

**Viés: bull, moderado — o contrato subiu com força, ficando a apenas 0,76% de
reconquistar o suporte técnico rompido em agosto, e a margem de biodiesel americana
bateu novo recorde da série, puxada por um salto de ~7% no heating oil. É o quadro mais
construtivo para o óleo desde a reabertura.**

O que sustenta a tese:

- **Alta forte, aproximando o preço da reconquista do nível técnico rompido em
  agosto.** Óleo CBOT fechou em **71,45** USD cts/lb em 10/09/2026 (CME CBOT),
  **+1,95%** sobre os 70,08 de 09/09 (valor reconstruído via indicadores — ver
  Honestidade) — a maior alta diária do óleo em toda a série pós-pausa. O contrato
  negociou entre 69,41 e 71,54 (mínima/máxima, CME CBOT) e fechou a 96% de distância do
  fundo do range — um fechamento muito forte, próximo da máxima do dia. O fechamento de
  71,45 está agora apenas **-0,76%** abaixo do suporte de 72,00 rompido em agosto
  (`alerta-quebra_suporte-oleo_cbot-2026-09-10`) — a menor distância desse nível em toda
  a série, ante -2,72% ontem e -2,44% anteontem. Um fechamento acima de 72,00 na próxima
  sessão seria a primeira reconquista genuína do suporte desde o rompimento de agosto.
- **A margem de biodiesel americana bateu novo recorde da série, e o mecanismo por trás
  reforça a leitura estrutural, não a contradiz.** Margem de **US$ 2,1485/galão** em
  10/09, ante US$ 1,91 em 09/09 (indicators) — uma alta de **+12,5%** em uma única
  sessão, o segundo recorde consecutivo da janela (09/09 já havia sido recorde frente a
  08/09). Decompondo o mecanismo: a receita do biodiesel (heating oil + 1,5× crédito RIN
  D4, o crédito de biocombustível concedido pela EPA americana) subiu para US$
  8,3072/galão (ante US$ 7,966 em 09/09), puxada quase inteiramente pelo heating oil, que
  fechou em **5,1422 USD/galão** em 10/09 (CME NYMEX HO=F) — um salto de
  aproximadamente **+7,1%** frente ao valor (~4,80 USD/galão) embutido no cálculo de
  receita do dia anterior — enquanto o crédito RIN D4 (1,5× = 2,11 USD/galão) permaneceu
  estável. Ao mesmo tempo, o custo do óleo como insumo subiu para US$ 5,3587/galão (7,5
  lb × 71,45 cts/lb), ante US$ 5,256 em 09/09 — uma alta de +1,96%, coerente com a
  própria alta do óleo em Chicago hoje. Ou seja: mesmo com o custo do insumo subindo, a
  receita subiu ainda mais rápido (puxada pelo heating oil), e o resultado foi a maior
  margem de biodiesel observada em toda esta série de leituras. **O mecanismo de fundo
  para o trader:** dois dias seguidos de margem recorde é um sinal mais forte de
  demanda futura por óleo de soja como insumo de biodiesel do que um único dia isolado —
  a probabilidade de que produtores de biodiesel acelerem compras de óleo nas próximas
  semanas aumenta a cada sessão em que essa margem se sustenta ou se amplia.
- **Oil share e oil-meal spread avançaram, capturando a força relativa do óleo dentro do
  crush.** O oil share fechou em **50,48%** em 10/09 (indicators), ante 50,38% em 09/09
  — uma alta de +0,10 p.p., a segunda sessão seguida acima de 50% e recuperando parte do
  terreno perdido no giveback de ontem. O oil-meal spread, como descrito na seção
  Farelo, se ampliou de +0,1166 para **+0,1507** USD/bushel (+29,3%) — o óleo "pagando
  mais" que o farelo dentro do crush com folga maior que em qualquer sessão anterior da
  janela.
- **O Índice de Suporte do Óleo (ISO) permanece no teto da escala pela terceira sessão
  seguida.** Em **100/100** — "óleo domina o crush", 5 de 5 condições atendidas
  (indicators, 10/09), o mesmo nível máximo de 08 e 09/09. Diferente do farelo, aqui o
  índice estrutural e o preço estão remando na mesma direção há três dias, o que dá mais
  peso à leitura de que o domínio do óleo dentro do crush não é um evento de um único
  dia.
- **O RIN D4 segue estável, e o arcabouço regulatório segue intacto.** 1,5×RIN = 2,11
  USD/galão embutido no cálculo de receita em 10/09 (indicators) — o EPA RFS 2026/2027
  (`EPA-RFS-2026-2027`, vigente desde 15/06/2026) permanece sem novidade, e é justamente
  essa estabilidade que permite que 100% do salto de margem de hoje seja atribuído ao
  heating oil, sem ruído regulatório concorrente.
- **A curva futura segue em contango moderado, sem distorção pontual mesmo após a
  alta.** Set/26 71,00 → out/26 (base) 71,45 → dez/26 71,97 → jan/27 72,24 → mar/27
  72,37 → mai/27 72,33 (CME CBOT, 10/09) — note que a curva de médio prazo (dez/26 em
  diante) já negocia **acima** de 72,00, o suporte que o contrato mais próximo ainda não
  reconquistou — um detalhe que sugere que o mercado futuro já trata a reconquista desse
  nível como mais provável que não, mesmo com o contrato-base ainda technicamente abaixo
  dele.

**O que invalida / risco:**

- **Nível técnico a vigiar:** a reconquista e sustentação de fechamento acima de 72,00
  seria a confirmação técnica que falta; a distância de apenas -0,76% torna esse cenário
  o mais próximo de se realizar em toda a série pós-pausa — mas também significa que uma
  reversão amanhã devolveria rapidamente o ganho de hoje.
- **O salto de heating oil de +7,1% em um único dia é grande o suficiente para levantar
  a pergunta genuína de sustentabilidade** — não há, nos dados disponíveis, nenhuma
  notícia ou evento específico (geopolítico, climático, de oferta) que explique o
  tamanho do movimento; tratá-lo como novo patamar permanente antes de uma segunda
  confirmação seria prematuro.
- **O COT de 01/09, com 10 dias corridos de defasagem, ainda mostra os fundos líquidos
  compradores em óleo (+17,28% net long na semana anterior, CFTC COT), um dado anterior
  a todas as quatro últimas sessões de preço (04, 08, 09 e 10/09).** Sem o corte
  seguinte, não há como saber se essa posição comprada já capturou o vaivém recente ou
  se os fundos ajustaram exposição de forma que os dados de preço ainda não refletem.

**Leitura operacional:** para quem está comprado em óleo direcional, hoje é o melhor dia
da série pós-pausa — preço em alta forte, fechamento próximo da máxima, margem de
biodiesel em novo recorde e ISO no teto da escala pela terceira sessão seguida. A
distância de -0,76% até o suporte de 72,00 torna esse nível o gatilho técnico mais
imediato de todo o complexo para a próxima sessão. Para quem está vendido em óleo
direcional, a tese perdeu força hoje — não há mais argumento de "preço fraco
confirmando o rompimento baixista"; o argumento que resta é técnico (o nível ainda não
foi reconquistado) e regulatório-doméstico BR (a MP 1.363/2026, tratada na lente fiscal
abaixo), não mais de preço ou de margem americana. Para quem opera o spread
farelo-óleo dentro do crush, o dia de hoje foi o mais favorável ao óleo de toda a
janela.

## Spreads e crush (leitura de complexo)

O terceiro pregão pleno desde a reabertura foi o primeiro em que os três produtos do
complexo se moveram na mesma direção nominal (todos em alta), mas a leitura de complexo
não se resume a "todos subiram" — o que importa é a velocidade relativa, e aí o
resultado foi inequívoco a favor do óleo. O oil share avançou de 50,38% (09/09) para
**50,48%** (10/09, indicators), a segunda sessão seguida acima de 50% depois do recuo
de ontem. O oil-meal spread se ampliou de +0,1166 para **+0,1507** USD/bushel
(+29,3%) — a maior expansão de uma sessão para a outra em toda a janela recente. E o
ratio Far/Soj, tratado em detalhe na seção Farelo, recuou de 79,06% para **78,93%**,
se afastando 0,15 ponto percentual de 80% depois de ter chegado à menor distância da
série ontem (0,92 p.p.). Juntando os três sinais: o crush de hoje distribuiu o valor do
complexo mais a favor do óleo do que em qualquer sessão desde a reabertura, mesmo com o
farelo também subindo em termos absolutos — o tipo de dia que confirma, e não contesta,
o mecanismo central da tese de junho (o crush "paga a conta" pelo óleo, e o farelo
sobra como subproduto, mesmo quando o preço absoluto do farelo sobe).

O índices sintéticos ISF/ISO, por sua vez, seguem exatamente parados: **80/100** e
**100/100** pela terceira sessão consecutiva (08, 09 e 10/09, indicators) — nenhuma das
três sessões de oscilação de preço (farelo caindo depois subindo duas vezes; óleo
subindo, caindo, depois subindo com força) foi suficiente para mover a contagem de
condições que compõe esses índices. Essa estabilidade, mantida agora por três sessões
inteiras de dados frescos com movimentos de preço relevantes em ambas as direções,
começa a parecer menos uma coincidência passageira e mais uma característica genuína do
método de cálculo: o ISF/ISO parece calibrado para capturar mudanças estruturais de
médio prazo no crush, não a volatilidade diária de preço — um ponto relevante para quem
usa esses índices como gatilho de entrada/saída de curto prazo, versus quem os usa como
bússola de tendência de fundo.

O crush margin fechou em US$ 2,2508/bushel em 10/09 (**+2,03%** sobre 09/09), a décima
sessão seguida abaixo do referencial de US$ 2,50
(`alerta-quebra_suporte-complexo_soja-2026-09-10`), com a distância percentual
encolhendo de -11,72% para **-9,97%** — a melhora veio da combinação de farelo e óleo
subindo mais rápido, em conjunto, do que a soja: farelo +5,30 e óleo +1,37 (em suas
respectivas unidades) somaram mais valor ao numerador da margem (farelo + óleo) do que
a soja tirou dele. É o mecanismo inverso do observado ontem, quando a melhora veio
principalmente da soja caindo mais rápido que farelo+óleo — hoje a melhora veio dos
produtos subindo mais que o insumo, um sinal mais saudável para a indústria de
esmagamento porque reflete demanda pelos produtos, não fraqueza do grão.

O ratio Far/Soj encerrou a sessão em 78,93%, a **1,07 ponto percentual** de 80% —
reabrindo parcialmente a distância que havia se fechado para 0,92 p.p. ontem. Isso
confirma, com um terceiro ponto de dado, o padrão descrito no veredito da revisão D+90
([[2026-09-09_d90-ratio-far-soj-reverte-na-vespera]]): desde a reabertura, o ratio
oscilou em uma faixa estreita — 78,25% (08/09), 79,06% (09/09), 78,93% (10/09) — sempre
abaixo de 80%, sem nunca cruzar o patamar, e com a aproximação mais próxima (79,08% em
09/09, valor levemente diferente do 79,06% aqui recalculado — ver Honestidade) tendo
sido revertida no pregão seguinte. Três sessões de dados frescos é ainda uma amostra
pequena, mas o padrão de oscilação dentro da zona de abundância, sem ruptura, é
consistente o suficiente para tratar a tese original como estruturalmente intacta.

Do lado dos fundamentos brasileiros de médio prazo (ABIOVE, projeções mensais para
set-dez/2026, sem revisão nesta janela), o balanço projetado continua mostrando o
esvaziamento sazonal esperado: estoque final de soja recuando de 7.912 mil toneladas
(set/26) para 5.721 (out/26), 3.659 (nov/26) e 1.890 mil toneladas (dez/26), a produção
de farelo caindo de 2.129 para 1.659 mil toneladas no mesmo período, e a exportação de
farelo recuando de 1.100 para 700 mil toneladas — uma trajetória que, se confirmada,
tende a aliviar a oferta doméstica de farelo ao longo do próximo trimestre e apoiar uma
recuperação futura do ratio Far/Soj por razões estruturais, independentemente de qual
lado vencer a oscilação diária de curto prazo.

## Lente fiscal/regulatória BR

Antes de fechar qualquer tese de preço BR, os vetores tributários/regulatórios vivos que
pesam no complexo — todos do `system/tributario_watch.toml`, cujo carimbo mais recente
(`atualizado_em`) em todos os 10 eventos catalogados é 2026-06-05, ou seja, **98 dias
sem revisão humana** frente a hoje (11/09):

- **MP 1.363/2026** (id `MP-1363-2026`, subvenção diesel fóssil R$ 1,12/L, vigente até
  31/12/2026): barateia o diesel fóssil no mix B15 (mistura obrigatória de 15% de
  biodiesel no diesel vendido no Brasil), reduzindo a competitividade relativa do
  biodiesel e a demanda doméstica por óleo de soja — vetor estrutural de baixa para
  óleo, direção "baixa" no cadastro, sem mudança de status. Importante não confundir com
  a margem de biodiesel AMERICANA (mercado e mecanismo diferentes), que hoje bateu novo
  recorde da série (+12,5%) por causa do heating oil, não por qualquer efeito desta MP
  brasileira — os dois mercados de biodiesel (EUA e BR) estão, neste momento, se movendo
  por razões completamente distintas.
- **B16 (id `B16-CNPE-2026`, elevação da mistura obrigatória de biodiesel para 16%)**
  segue "adiado" — resultado dos testes técnicos esperado por volta de novembro/2026.
  Upside represado (~436 mil toneladas de demanda potencial adicional de óleo, direção
  "alta" no cadastro), não corrente. Com o oil share hoje em 50,48% (subindo pela
  segunda sessão seguida) e o ISO no teto de 100/100, um estímulo futuro de demanda por
  óleo via B16 encontraria, quando chegar, um cenário estrutural já favorável ao óleo —
  reforçando, não contradizendo, o upside represado.
- **Isenção de PIS/Cofins do biodiesel na mistura** (id `PISCOFINS-BIODIESEL-ISENCAO`):
  vigência registrada até 31/07/2026 — já **42 dias corridos vencida** frente a
  11/09/2026, sem qualquer registro de prorrogação ou expiração no arquivo. Status
  tratado como "desconhecido pós-vigência", não como fato de vigência ou caducidade.
- **MP 1.358/2026** (subvenção gasolina R$ 0,89/L): vigência registrada até 11/07/2026,
  agora **62 dias corridos vencida**, mesma lacuna de informação sobre renovação.
- **STJ REsp 2.165.276** (id `STJ-RESP-2165276`, crédito de PIS/Cofins sobre soja em
  biodiesel sob suspensão tributária, direção "alta" para soja/óleo): alívio de custo
  pontual, não vinculante, sem novidade nesta janela.
- **EPA RFS 2026/2027** (id `EPA-RFS-2026-2027`, mandato de biocombustível americano,
  vigente desde 15/06/2026, direção "alta" para óleo): sustenta o RIN D4, estável — o
  arcabouço regulatório segue intacto e ajuda a explicar por que a margem de biodiesel
  americana pôde saltar +12,5% hoje sem qualquer risco de mudança de crédito.
- **Crédito 45Z** (id `45Z-CLEAN-FUEL`, em tramitação, direção "mista"): sem novidade.
- **Indonésia — Danantara** (id `DANANTARA-INDONESIA`) e **levy de exportação PMK
  9/2026** (id `INDONESIA-LEVY-PMK9`): a assunção plena da centralização da exportação
  de palma pela Indonésia tinha alvo 01/09/2026 — já se passaram **10 dias** sem
  qualquer notícia neste dump confirmando execução. Catalisador de alta represado para
  óleo (via substituição com palma), não invalidado nem confirmado.
- **Indonésia B50** (id `INDONESIA-B50`, monitorando, direção "alta"): sem novidade
  nesta janela.

## Riscos e eventos próximos

- **COT (CFTC) das posições de 08/09, ainda não publicado** — a leitura de ontem
  esperava esse corte para hoje, sexta-feira 11/09; ele ainda não aparece nesta janela
  do dump. É o dado mais aguardado desta janela: mostraria se os fundos acompanharam a
  força de farelo (dois dias de alta) ou de óleo (alta forte hoje), ou se reduziram
  exposição em ambos depois do net long recorde de +63,83%/+17,28% do corte de 01/09.
- **Reconquista (ou não) de 72,00 no óleo** — a apenas -0,76% de distância, é o gatilho
  técnico mais próximo de todo o complexo para a próxima sessão.
- **Quarto pregão de confirmação (ou não) da força do óleo/fraqueza relativa do
  farelo** — três sessões desde a reabertura mostraram o ratio Far/Soj oscilando sem
  romper 80%; um quarto ponto de dado na mesma faixa reforçaria a leitura estrutural,
  enquanto uma ruptura de 80% encerraria formalmente a tese de junho.
- **USDA Crop Progress semanal**: próximo corte esperado na segunda-feira 14/09.
- **USDA WASDE**: ausente da janela; catalisador potencial de revisão de balanço
  mundial.
- **NOPA mensal** (`release-nopa-2026-09-10`): quarto dia seguido do mesmo falso
  positivo de paywall na fila — o gap de dado de crush americano segue sem solução.
- **Sustentabilidade do salto de heating oil (+7,1% em um dia)** — sem notícia
  específica no briefing que explique o tamanho do movimento; um recuo na próxima
  sessão reduziria a margem de biodiesel de volta para níveis mais próximos dos dias
  anteriores.
- **Confirmação (ou não) da centralização plena da exportação de palma pela Danantara**
  — marco-alvo era 01/09, já se passaram 10 dias.
- **Vigência da isenção PIS/Cofins do biodiesel** (42 dias vencida) e **MP 1.358/2026 da
  gasolina** (62 dias vencida) — checar notícia de renovação/expiração antes de assumir
  qualquer tese de custo de combustível BR.
- **Clima**: previsão de 11/09 (hoje) mantém chuva e trovoadas no núcleo produtor de
  Mato Grosso e no Sul, com calor intenso em MT (Cuiabá, Sinop, Sorriso, Lucas do Rio
  Verde entre 37-38°C de máxima) e sem menção de geada no Sul — pano de fundo relevante
  para a janela de plantio da safra 2026/27 que se aproxima, ainda sem impacto direto
  sobre a soja em si (ainda não plantada na região).

## Honestidade

- **O dump de hoje não contém as linhas brutas de CME CBOT para soja e óleo na data de
  09/09** — apenas farelo e (parcialmente) heating oil têm linha própria de preço para
  aquele dia (farelo fechamento 345,10, volume 28.688; heating oil só com abertura
  registrada, 4,6205, sem fechamento próprio nesta janela). Os valores de soja (1.309,50)
  e óleo (70,08) usados nas comparações desta leitura foram reconstruídos a partir das
  fórmulas dos indicadores sintéticos de 09/09 (`complexo_soja.crush_margin_usd_bu` e
  `biodiesel_us.custo_oleo_usd_galao`), não de uma linha de preço bruta própria — o
  mesmo tipo de gap identificado por [[2026-09-10_leitura-complexo]] no dia anterior,
  mas desta vez recaindo sobre a data de 09/09 em vez de 08/09.
- **Há uma pequena divergência entre os valores de 09/09 reconstruídos nesta janela do
  dump e os valores brutos citados por [[2026-09-10_leitura-complexo]]**, que dispunha
  de uma janela de dump diferente com a linha bruta própria daquele dia: óleo 70,08
  (aqui) vs 70,04 (lá); soja 1.309,50 (aqui) vs 1.308,75 (lá); farelo 345,10 (aqui,
  igual à linha bruta) vs 345,00 (lá, arredondado). As diferenças são pequenas (dentro
  de 0,1%) e não mudam nenhuma conclusão direcional desta leitura, mas são registradas
  aqui por transparência — a fonte primária de fechamento bruto de um pregão pode
  divergir ligeiramente da reconstrução via fórmula de indicador quando a linha bruta
  já não está mais na janela de 14 dias do dump.
- **Não há comparação direta de volume dia-a-dia para óleo em 09/09 nesta janela do
  dump** — o número de 70,08 usado como base de preço vem da reconstrução via
  indicadores, mas nenhuma linha de volume bruto para óleo em 09/09 está presente aqui;
  o volume citado nesta leitura para 09/09 (23.814, usado apenas para contexto, não para
  cálculo de variação percentual do dia de hoje) vem citado via
  [[2026-09-10_leitura-complexo]], não desta janela do dump.
- **O COT de 01/09 tem agora 10 dias corridos de defasagem frente a hoje, e o corte
  seguinte (esperado pela leitura de ontem para hoje) ainda não apareceu nesta
  janela** — não há como confirmar a expectativa de calendário citada ontem; trata-se de
  uma inferência do calendário semanal do CFTC, não de um dado confirmado no briefing.
- **Percentil histórico de posicionamento COT não está disponível no briefing** — toda
  leitura de "fundos comprando/vendendo" usa variação semana a semana de contratos
  absolutos, não percentil histórico.
- **A estabilidade total do ISF/ISO ao longo de três sessões de preço com movimentos
  relevantes em ambas as direções é, ela mesma, um dado que merece registro, não apenas
  uma observação de passagem** — não há, nos dados disponíveis, uma forma de saber qual
  seria a magnitude de movimento de preço/ratio necessária para de fato deslocar esses
  índices discretos de seus patamares atuais (80/100 e 100/100).
- **`tributario_watch.toml` sem atualização há 98 dias** — pelo menos dois vetores
  (isenção PIS/Cofins do biodiesel, MP 1.358/2026) já passaram da data de vigência
  registrada sem nota de renovação ou expiração. Tratados como "status desconhecido
  pós-vigência", não como fato de caducidade real.
- **NOPA segue inacessível** (paywall) — nova "release" carimbada em 10/09 é o quarto
  falso positivo seguido na fila, sem dado novo de fato.
- **USDA WASDE ausente** da janela — nenhuma leitura de balanço mundial oficial
  atualizado disponível.
- **A ausência de itens de notícia em 10/09 ("0 items lidos, 0 mantidos")** é registrada
  como uma falha ou pausa de coleta da fonte RSS naquela data, não como ausência real de
  notícia relevante no mercado — não deve ser interpretada como "dia sem notícias".
- **A previsão INMET para 11/09 é previsão meteorológica, não medição de precipitação
  real** — a ausência de menção a "geada" no boletim de hoje para Passo Fundo/RS é
  tratada como sinal indicativo, não como confirmação de que a geada efetivamente
  cessou.
- **Prêmios de exportação (Paranaguá, farelo e óleo) e o físico de Paraná/Paranaguá
  seguem sem atualização própria para 10/09** — a última leitura disponível de todas
  essas séries é 09/09; não é possível afirmar se isso reflete mercado físico
  genuinamente parado ou apenas defasagem normal de publicação da fonte (NAG/CEPEA).
- **O salto de +7,1% no heating oil em um único dia não tem, nos dados disponíveis,
  nenhuma explicação de evento específico** — é tratado aqui como um fato de preço
  observado, não como um movimento cujo mecanismo causal foi identificado.
- **MPOB (palma Malásia) segue com parser quebrado** — nenhum dado de produção/estoque
  de palma malaia disponível para cruzar com a tese de substituição via Indonésia.
- **BCBA (Argentina) segue sem links de relatório detectados pelo scraper** — nenhum
  dado de safra ou exportação argentina disponível nesta janela.
- **A fila de julgamento repete os dois itens de revisão do ratio Far/Soj (D+7 e D+90)
  como "vencidos" pela quarta vez seguida, mesmo depois de o marco D+90 já ter sido
  tratado em profundidade em 09/09** — isto parece ser um eco do sistema de geração de
  fila (que provavelmente não lê de volta os insights já escritos em `insights/*.md`
  para marcar a revisão como encerrada), não uma nova revisão genuína. Tratado aqui,
  como nos dois dias anteriores, como continuidade do mesmo veredito, com o dado novo de
  hoje (ratio recuando para 78,93%) incorporado como atualização.
