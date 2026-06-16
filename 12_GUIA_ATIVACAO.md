# Guia de Ativacao — Inputs Pendentes (~30 min total)

Passo-a-passo pra ativar os 4 inputs que dependem so de voce.

---

## 1. NASS_API_KEY — USDA Crop Progress (5 min)

**O que e**: chave gratuita do USDA pra acessar API Quick Stats. Sem ela, coletor `usda_crop_progress` fica off.

### Passos

1. Abrir https://quickstats.nass.usda.gov/api
2. Procurar secao **"Request an API Key"** (geralmente topo ou lateral direita)
3. Preencher formulario:
   - First name / Last name
   - Email (pode ser corporativo)
   - Use: "Personal / Research" ou similar
4. Submeter. **Resposta vem por email em segundos** com a key (formato: 8-segmentos hexadecimais tipo `ABCD1234-EFGH-5678-...`)
5. Abrir `C:\Users\Usuario\OneDrive\Desktop\Program\commodities-radar\system\.env` num editor de texto
6. Adicionar linha no final:
   ```
   NASS_API_KEY=cole_aqui_a_key_recebida
   ```
7. Salvar arquivo

### Validar

```powershell
cd C:\Users\Usuario\OneDrive\Desktop\Program\commodities-radar\system
.\.venv\Scripts\python.exe main.py public --source usda_crop_progress
```

Deve mostrar `fetched: N | saved: N` com N > 0. Se der erro `NASS_API_KEY nao configurado`, conferir se salvou correto no .env.

---

## 2. CEPEA — RESOLVIDO via RSS! ✅

**Atualizacao 2026-05-25**: voce nao precisa mais cadastrar email do CEPEA nem configurar App Password Gmail.

Encontramos o RSS feed publico do CEPEA em `https://www.cepea.org.br/rss.php`. Coletor `cepea_rss` ja esta ativo e funcionando — 91 noticias salvas no primeiro run, cobrindo soja, milho, boi, etanol, etc.

**O que NAO precisa fazer**:
- ~~Subscrever no CEPEA~~ desnecessario
- ~~App Password Gmail~~ desnecessario
- ~~Configurar IMAP_USER no .env~~ desnecessario

**Como funciona**:
- Sistema busca o RSS via ScraperAPI 1x/dia (custa 1 credit)
- Parse XML, identifica commodity pelo titulo
- Salva noticias + extrai valores numericos quando aparecem
- 30 requests/mes = trivial no free tier (1000)

**Limitacao conhecida**: o RSS tem TITULOS + RESUMOS, nao precos diarios exatos. Pra preco numerico de soja diario, ainda dependemos do StoneX ou ABIOVE.

Mas pra CONTEXTO/SENTIMENTO ("Soja: futuros recuperam") + EVENTOS importantes (releases CONAB, decisoes USDA) — RSS e perfeito.

---

## ~~2-original. Email CEPEA — substituido pelo RSS~~

**Mantido abaixo so para historico:**

CEPEA envia indicadores diarios por email gratuitamente. Sistema leria os emails via IMAP e extrairia os valores. **Nao e mais necessario** porque o RSS resolve o problema sem precisar de Gmail App Password etc.

### Passo A — Subscrever no CEPEA

1. Abrir https://www.cepea.esalq.usp.br/
2. Rolar ate o **rodape** ou **lateral** procurando "Newsletter", "Receba indicadores", "Cadastre-se"
3. Preencher cadastro:
   - Nome
   - Email (recomendo um Gmail novo dedicado ou seu Gmail principal com filtro)
   - Selecionar indicadores: **Soja, Milho, Boi Gordo** (pelo menos)
4. Confirmar cadastro via email de validacao
5. Aguardar primeiro email (vem geralmente no proximo dia util a tarde)

### Passo B — Configurar IMAP no Gmail

Pra sistema ler os emails automaticamente:

1. Ativar 2FA na conta Google (caso ja nao tenha):
   - https://myaccount.google.com/security
   - Liga "Verificacao em duas etapas"

2. Criar **App Password** especifico:
   - https://myaccount.google.com/apppasswords
   - Selecionar app: "Mail"
   - Selecionar device: "Other" → digite "Commodities Radar"
   - Clicar "Generate"
   - **Copiar a senha de 16 digitos** que aparecer (so aparece uma vez!)

3. (Opcional) Criar label/filtro dedicado:
   - No Gmail web: Settings → Filters → Create new filter
   - From: `cepea` ou `*@cepea.esalq.usp.br`
   - Aplica label "cepea" automaticamente

### Passo C — Adicionar credenciais no .env

Editar `system/.env`:
```
IMAP_HOST=imap.gmail.com
IMAP_PORT=993
IMAP_USER=seuemail@gmail.com
IMAP_PASS=app_password_de_16_digitos_sem_espacos
CEPEA_SENDER=cepea
IMAP_FOLDER=INBOX
```

### Passo D — Habilitar coletor

Editar `system/sources/cepea_email.py`, linha 25:
```python
enabled = True   # mudar de False pra True
```

### Validar

```powershell
.\.venv\Scripts\python.exe main.py public --source cepea_email
```

Se ainda nao tem emails do CEPEA na caixa, vai dar 0 fetched (esperado). Quando primeiro email chegar, rodar de novo deve trazer dados.

**Troubleshooting**:
- Erro "IMAP login": App Password errada (recopiar sem espacos) ou 2FA nao ativado
- Erro "no folder": ajustar IMAP_FOLDER se voce criou label especifica
- 0 fetched: aguardar primeiro email do CEPEA chegar

---

## 3. Task Scheduler — automatizar tudo (5 min)

**O que faz**: cria 5 tarefas no Windows pra rodar pipeline automatico em horarios fixos. Voce nao precisa mais digitar comandos.

### Tarefas criadas

| Nome | Horario | Comando |
|---|---|---|
| `CommoditiesRadar_Morning` | 07:00 diario | `run` completo |
| `CommoditiesRadar_Evening` | 19:00 diario | `public --source cme_cbot` (pos-fechamento CBOT) |
| `CommoditiesRadar_Indicators` | 20:00 diario | `indicators` (recalcula crush margin) |
| `CommoditiesRadar_Alerts` | 20:15 diario | `alerts` (checa niveis tecnicos) |
| `CommoditiesRadar_Friday` | sex 18:00 | CFTC COT (apos release 15:30 NY) |

### Passos

1. Abrir **PowerShell** (Win+R → "powershell" → Enter). **Nao precisa ser admin**.
2. Navegar pra pasta:
   ```powershell
   cd C:\Users\Usuario\OneDrive\Desktop\Program\commodities-radar\system
   ```
3. Rodar setup:
   ```powershell
   powershell -ExecutionPolicy Bypass -File .\setup_scheduler.ps1
   ```
4. Deve imprimir 5 linhas "Created: ComRadar_..."

### Validar

```powershell
.\setup_scheduler.ps1 -List
```
Mostra tabela com 5 tasks e seus estados (State: Ready).

Tambem pode abrir o **Agendador de Tarefas do Windows** (Win+R → `taskschd.msc`) e procurar tasks `CommoditiesRadar_*`.

### Outros comandos uteis

```powershell
.\setup_scheduler.ps1 -Remove    # remove todas as tasks
.\setup_scheduler.ps1            # roda dnv (atualiza)
```

### Troubleshooting

- "execution of scripts is disabled": ja resolvido pelo `-ExecutionPolicy Bypass`
- Task nao roda no horario: verificar se PC esta ligado no horario; tasks tem `StartWhenAvailable=true` entao se acordar depois, roda assim que ligar

---

## 4. Compartilhar pasta `shared/` no OneDrive (5 min)

**O que faz**: consultor StoneX recebe link, abre, ve a pasta `shared/` no navegador (e/ou sincroniza). Nao tem acesso a NADA fora dela (system/, data/, inbox/).

### Passos

1. Abrir **File Explorer** (Win+E)
2. Navegar pra: `C:\Users\Usuario\OneDrive\Desktop\Program\commodities-radar\`
3. **Botao direito** em `shared` (so na pasta `shared`, nao no pai!)
4. Menu de contexto → procurar:
   - "Share" (se em ingles)
   - "Compartilhar" (se em portugues)
   - Pode ter icone de OneDrive (nuvem azul)
5. Clicar — abre dialog OneDrive
6. **Configurar permissoes** (antes de adicionar email):
   - Mudar para "**Pessoas especificas**" (NAO "qualquer um com o link")
   - Marcar "**Pode editar**" (pra consultor poder largar arquivos no `from_consultor/`)
   - **DESmarcar** "Permitir download" se quiser limitar (opcional)
7. **Adicionar email do consultor** no campo "Para"
8. (Opcional) Adicionar mensagem:
   ```
   Olá! Esta pasta é nosso espaço de trabalho compartilhado.
   Veja o README.md dentro pra entender a estrutura.
   ```
9. Clicar **"Enviar"** ou "Send"

### Validar

- Voce recebe email de confirmacao: "Voce compartilhou shared com [nome consultor]"
- Consultor recebe email com link "OneDrive folder shared with you"

### Verificar o que o consultor ve

1. Em outro browser (incognito) ou pedindo pro consultor confirmar
2. Ele deve ver:
   - `shared/README.md`
   - `shared/from_consultor/` (com subpastas inbox/, insights/, notas_call/)
   - `shared/to_consultor/` (com snapshots_diarios/, teses_ativas/, alerts/, perguntas_pendentes/)
   - `shared/colaboracao/` (3 arquivos .md)
3. Ele **NAO deve conseguir subir** para `commodities-radar/` (pai) — se conseguir, voce compartilhou pasta errada, refazer.

### Troubleshooting

- "Nao consigo compartilhar — pasta nao esta no OneDrive": verificar se OneDrive esta sincronizando essa pasta. Olhar icone de nuvem na barra de tarefas — se estiver pausado, retomar.
- Consultor nao recebeu email: verificar spam dele, ou copiar link e enviar via WhatsApp/Telegram
- Quer revogar acesso: botao direito em `shared/` → Manage Access → Stop Sharing

---

## Checklist final

Apos completar os 4 passos, voce tem:

- [ ] USDA Crop Progress rodando automatico (segunda a noite atualiza)
- [ ] CEPEA email entrando automatico (apos primeiro email chegar)
- [ ] 5 tasks Windows rodando pipeline diariamente
- [ ] Consultor StoneX com acesso a `shared/`

E pode validar com 1 comando que **tudo esta certo**:

```powershell
cd C:\Users\Usuario\OneDrive\Desktop\Program\commodities-radar\system
.\.venv\Scripts\python.exe main.py public --list
```

Todos coletores com `[ON ]` (exceto cepea scraping que fica off permanente).

---

## Tempo total estimado

| Passo | Tempo |
|---|---|
| 1. NASS_API_KEY | 5 min |
| 2. Email CEPEA (subscrever + IMAP) | 10 min |
| 3. Task Scheduler | 5 min |
| 4. Compartilhar OneDrive | 5 min |
| **TOTAL** | **~25 min** |

Pode fazer tudo de uma vez ou um por dia.
