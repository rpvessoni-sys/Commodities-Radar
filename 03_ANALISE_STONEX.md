# Analise do Relatorio StoneX — Semanal de Combustiveis 18/05/2026

> **Atencao de escopo:** Esse e o "Semanal de Combustiveis" — cobre diesel, biodiesel, gasolina, etanol. **NAO cobre soja em grao nem farelo direto.** Cobre oleo de soja so indiretamente (como input do biodiesel/HVO).
> Decidir: temos outros relatorios StoneX disponiveis (Semanal de Soja? Mensal de Graos?) ou esse e a unica porta de entrada?

---

## 1. Estrutura do relatorio

Padrao por secao:
1. **Manchete + vies** (curto e direto, ex: "Estoques globais seguem sazonalmente baixos", "Subvencao do governo pode estender queda")
2. **Movimento da semana** (preco, %, fechamento)
3. **Fatores explicativos** (oferta, demanda, estoques, eventos)
4. **Grafico de referencia** (1-2 por secao)
5. **Outlook / proximos eventos**

4 secoes fixas (provavelmente):
- DIESEL (NY Harbor ULSD, crack-spread vs Brent, estoques EUA/ARA/Singapura)
- BIODIESEL (BR doméstico, RIN D4, EIA projecoes, 45Z)
- GASOLINA (RBOB, crack-spread, estoques, subvencao BR)
- ETANOL (hidratado/anidro BR, E32, ANP, UNICA)

---

## 2. Dados-chave extraidos (data-base 16/05/2026 e correlatos)

### Diesel
- **NY Harbor ULSD**: USD 4,053/galão (+4,0% semana, fechamento sex 24 mai... ✱ inconsistencia de data, ver §5)
- **Diferencial Heating Oil vs Brent**: USD 60,98/bbl (-2,4%)
- **Estoques diesel EUA**: leve avanco semanal
- **Importacoes EUA**: +74% semana (Europa pos-manutencao)
- **Estoques ARA Europa**: -14,1% YoY
- **Estoques Singapura**: +4,7% YoY (China retomou exportacoes)
- **Estoques globais**: -4% YoY (conflito Oriente Medio)

### Biodiesel
- **Biodiesel BR**: R$ 5.263/m³ (-0,9% semana)
- **Margem implicita usinas BR**: R$ 146/ton (**-27% semana**) ★ relevante
- **RIN D4 EUA**: > US¢ 200 (leve alta)
- **EIA projecao BD+HVO 2026**: +175 mil t vs projecao de abril ★
- **EIA projecao BD+HVO 2027**: -106 mil t vs projecao anterior (mas ainda crescimento)
- **Crescimento BD+HVO esperado 2026**: +28% YoY
- **RFS requirement 2026**: 6 bi galoes (insuficiente — EIA projeta producao para atender 4,6 bi)

### Gasolina
- **RBOB**: USD 3,7/galão (+5% semana, **maior nivel desde jun/22**)
- **Crack-spread RBOB vs Brent**: USD 46,4 (-1,3%)
- **Estoques comerciais EUA**: -4,1 mi barris (projecao era -2,9 mi)
- **Importacoes EUA**: 800 → 300 kbpd (colapso)
- **Subvencao gasolina BR**: ate **R$ 0,89/L** (teto tributos federais)
- **PPI gasolina (StoneX)**: R$ 1,59/L no anuncio
- **Preco revenda gasolina C SP**: R$ 6,53/L (4a semana em queda)

### Etanol
- **Hidratado SP Ribeirao Preto**: R$ 2,72/L com impostos (-2,2%)
- **Anidro**: R$ 2,75/L (-0,5%)
- **Anidro abr → mai**: R$ 2,95 → R$ 2,56/L (queda forte)
- **E30 → E32 proposta**: +1 bi litros/ano (estimativa UNICA)
- **ANP**: consulta publica para extinguir estoques obrigatorios entressafra (vigor 2027/28)
- **Etanol revenda**: -2,8% bombas / Gasolina: -0,8% bombas
- **Paridade etanol/gasolina SP**: 63,9% (menor do ano — incentivo a abastecer com etanol)

---

## 3. Jargao do consultor (padroes notaveis)

**Termos tecnicos especificos:**
- **Crack-spread** — diferenca entre derivado refinado e petroleo bruto
- **PPI** — Paridade de Preco de Importacao
- **RIN D4** — Renewable Identification Number, categoria 4 (biodiesel)
- **RFS** — Renewable Fuel Standard (EUA)
- **RVO** — Renewable Volume Obligation (volume anual obrigatorio EUA)
- **HVO** — Hydrotreated Vegetable Oil (renewable diesel)
- **45Z** — Credito federal EUA por baixa intensidade carbono (IRA)
- **ARA** — Amsterdam-Rotterdam-Antwerp hub de estoque Europa
- **kbpd** — mil barrels per day
- **Mix etanoleiro** — % da cana destinada a etanol vs acucar
- **E30/E32** — mistura % anidro na gasolina C

**Linguagem estilistica:**
- "compasso de espera"
- "destruicao de demanda"
- "pressao baixista/altista"
- "magnitude distintas"
- "blindar o mercado interno"
- "vetores apontam direcoes opostas"

**Padrao narrativo:** consultor usa muito **causa → efeito**, explicando movimento de preco por dinamica de oferta/demanda. Bom estilo analitico.

---

## 4. Conexao com nosso escopo (soja/farelo/oleo)

**Forte:**
- **Biodiesel BR** consome oleo de soja como insumo principal. Margem usinas BR -27% semana **deveria sinalizar enfraquecimento da demanda de oleo de soja no Brasil** (vies baixista oleo BR). Mas o relatorio cita "recuperacao dos precos internos do oleo de soja" sem detalhar.
- **HVO/Renewable diesel EUA** puxa oleo de soja CBOT. EIA projecao +175k t em 2026 = sustentacao do oil share alto.
- **45Z (IRA EUA)** premia oleo de soja com baixa intensidade carbono = driver estrutural CBOT BO.
- **RIN D4 > 200 cts** = biodiesel rentavel = demanda oleo sustentada.

**Indireto:**
- Mistura E32 (gasolina+anidro) = mais cana para etanol = menos cana para acucar = pode mudar mix agro BR (mas nao impacta soja direto)

**Nao cobre:**
- Soja em grao (CBOT S, fisico BR, China demanda, Argentina, clima)
- Farelo (CBOT SM, fisico Rondonopolis, esmagamento)
- Oleo de soja em si (preco CBOT BO, fisico Santos, exportacao)
- Crush margin (EUA ou BR)
- Estoques (WASDE, NOPA)

---

## 5. Inconsistencias / pontos a verificar

- **Datas**: texto diz "fechamento da sexta-feira (24)" mas o periodo aparente e 12-16/maio. Possivel erro do relatorio ou ele esta cobrindo periodo diferente. Confirmar data-base com voce.
- **PPI gasolina R$ 1,59/L** parece muito baixo (preco internacional). Mas e PPI sem impostos, ok.

---

## 6. Insights criticos a anotar

### 6.1 Sinal contraditorio biodiesel/oleo BR
Margem biodiesel BR caiu **27% na semana**, mas oleo de soja BR "se recuperou" no periodo. Significa que:
- Preco do oleo subindo + preco BD caindo = margem comprimida → **usinas vao reduzir compra de oleo** → pressao baixista para oleo BR nas proximas semanas
- **Investigar:** o que fez biodiesel BR cair se demanda esta firme com o B14? Possivel: estoque alto na cadeia / leilao da ANP com preco fraco / spot vs contrato

### 6.2 EIA projecao = bullish estrutural pro oleo CBOT
+175k t de BD+HVO em 2026, +28% YoY — sustenta oil share alto, mantem demanda firme pelo oleo de soja EUA. **Driver de longo prazo positivo.**

### 6.3 Crack-spread alto significa refinaria feliz, mas distorce sinal
USD 60+/bbl no diferencial diesel-petroleo e historicamente muito alto. Refinarias com margem gorda = max processamento de cru = + diesel, + gasolina, + oleo combustivel. **Mexe indiretamente em complexo agro via:**
- Custo de frete (diesel)
- Demanda de biodiesel (substituicao)

### 6.4 Subvencao gasolina BR e marca politica de intervencao
R$ 0,89/L de subsidio + politica diesel jah existente. Sinal: **governo brasileiro intervem fortemente em precos**. Pode-se especular sobre uso semelhante em **acucar/etanol** ou outros — mas dificilmente em soja (commodity exportavel sem teto domestico).

### 6.5 E32 mexe etanol, nao soja
Aumento de mistura E30→E32 = +1 bi L anidro/ano. Importante pro complexo etanol/acucar, **mas nao direto na soja**. Marcar como **out-of-scope** salvo cruzamento eventual com complexo agro.

---

## 7. Gaps identificados (o que o sistema precisa preencher)

Esse relatorio sozinho deixa de fora **80% do que importa para nossa tese soja/farelo/oleo**. Precisamos cruzar com:

| Gap | Fonte publica para preencher |
|---|---|
| Preco CBOT S/SM/BO | CME (cotacao publica) |
| WASDE mensal | USDA (publico) |
| Crop Progress USA | USDA NASS (publico) |
| NOPA Crush | NOPA (publico, mensal) |
| Conab BR | Conab (publico) |
| CEPEA/ESALQ soja/oleo | Cepea (publico, diario) |
| Clima MT/IL/Argentina | NOAA / Inmet / Climatempo |
| China importacoes soja | Customs China (publico) |
| Bolsa Cereales Argentina | BCBA (publico) |
| COT/Fundos posicao | CFTC (publico) |
| Premio Paranagua | StoneX **ou** outras consultorias (Agrural, Safras) |

---

## 8. Perguntas para voce

### 8.1 Voce tem acesso a OUTROS relatorios StoneX?
StoneX provavelmente publica:
- **Semanal de Soja** — onde estaria a tese de soja/farelo/oleo direto
- **Mensal de Graos** — visao consolidada
- **Boletins diarios** — comentario CBOT
- **Especiais** (relatorio pos-WASDE, pos-Conab, etc)

**Confirma:** voce ve **so o Semanal de Combustiveis**, ou tem acesso a outros relatorios via portal/email?

### 8.2 Sobre o consultor
Voce mencionou que opera via consultor StoneX. Esse consultor:
- Te manda relatorios + recomendacoes especificas (operacao a operacao)?
- Esses relatorios sao redacao texto dele ou copia do publico StoneX?
- Frequencia de contato?

Isso muda **muito** o que o sistema precisa cobrir.

### 8.3 Sobre o foco do projeto
Dado o conteudo do relatorio, vejo dois caminhos:

**Caminho A** — manter escopo soja/farelo/oleo, usar **fontes publicas como base** + StoneX combustivel como driver biodiesel/HVO.

**Caminho B** — expandir escopo para **complexo agro + biocombustivel** (soja + biodiesel + etanol + acucar). Faz sentido se voce trabalha em area que cobre os dois (ex: industria que processa cana/soja, trading que opera ambos).

**Qual faz mais sentido para sua empresa/funcao?**
