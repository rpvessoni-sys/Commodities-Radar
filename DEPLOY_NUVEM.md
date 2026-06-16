# Rodar o Radar na nuvem (sem o seu PC)

> Objetivo: o pipeline roda sozinho nos servidores do GitHub (de graça), publica
> o relatório num **link que abre no celular**, e te manda um **resumo diário no
> Telegram**. Você usa o Claude só pra interpretar. Seu computador pode ficar desligado.

## Como funciona (arquitetura)

```
GitHub Actions (cron grátis)              GitHub Pages            Você
  ├─ a cada 30 min (pregão):  CBOT+câmbio ──┐
  │   CEPEA/NAG só se houver fechamento novo │──► HTML publicado ──► link no celular
  └─ 1×/dia (~19h BRT): varredura completa ──┘                  └─► resumo no Telegram
       + forecast + resumo                                          (cole no Claude p/ interpretar)
```

- **Compute:** `.github/workflows/radar.yml` (dois crons: intraday 30 min + daily).
- **Entrypoint:** `system/cloud_run.py --mode intraday|daily` (faz a divisão grátis/pago).
- **Estado:** o banco `radar.db` viaja por cache entre execuções + backup diário.
- **Resumo:** `system/daily_summary.py` (Telegram opcional).

Sobre "tudo a cada 30 min": CBOT e câmbio (grátis) atualizam de fato a cada 30 min.
CEPEA/NAG **publicam 1×/dia** — o sistema verifica sempre, mas só baixa (gasta crédito
ScraperAPI) quando há fechamento novo. Assim você tem o dado mais fresco possível sem
queimar ~5 mil créditos/mês nem estourar a cota (estourar daria MENOS dado). Pra forçar
busca paga mais frequente, baixe a variável `PAID_MIN_HORAS` (passo 3).

---

## Passo a passo (≈ 20 min, uma vez)

### 1. Conta + repositório
1. Crie conta em https://github.com (se não tiver).
2. Crie um repositório **privado** vazio, ex.: `commodities-radar` (sem README).

### 2. Subir o projeto
No PowerShell, na pasta do projeto:
```powershell
cd C:\Users\Usuario\OneDrive\Desktop\Program\commodities-radar
git add -A
git commit -m "Deploy nuvem: workflow + cloud_run + resumo Telegram"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/commodities-radar.git
# SEED do histórico: o banco é ignorado pelo git; force 1 envio pra nuvem já
# começar com os 5 anos de backfill (depois ele vive no cache, não precisa repetir):
git add -f data/radar.db
git commit -m "Seed inicial do banco (5y backfill)"
git push -u origin main
```
> O `.env` (suas chaves) **não sobe** — está no .gitignore de propósito. As chaves
> vão pros Secrets no passo 3.

### 3. Secrets (chaves protegidas)
No GitHub: **Settings → Secrets and variables → Actions → New repository secret**.
Copie os valores do seu `system/.env`:

| Secret | De onde | Obrigatório |
|---|---|---|
| `SCRAPER_API_KEY` | linha SCRAPER_API_KEY do .env | sim (CEPEA/NAG) |
| `NASS_API_KEY` | linha NASS_API_KEY do .env | sim (USDA) |
| `TELEGRAM_BOT_TOKEN` | passo 5 | só p/ resumo |
| `TELEGRAM_CHAT_ID` | passo 5 | só p/ resumo |

Opcional, em **Variables** (não Secrets): `PAID_MIN_HORAS` = `4` (quão raro buscar as fontes pagas).

### 4. Ligar o Pages (o link)
**Settings → Pages → Source: GitHub Actions.** Salve.
Depois do 1º run (passo 6), o link aparece em **Settings → Pages** e no fim do log do
job *deploy* — algo como `https://SEU_USUARIO.github.io/commodities-radar/`.

> **Privacidade:** no plano grátis, repo privado mas a *página* fica pública (quem tiver
> a URL vê). O conteúdo é dado público de mercado + histórico de prêmios — provavelmente ok.
> Se quiser fechar: (a) GitHub Pro (~US$4/mês) deixa o Pages privado, ou (b) Cloudflare
> Pages grátis + Cloudflare Access (PIN/login). Dá pra começar simples e fechar depois.

### 5. Telegram (opcional, ~2 min) — pro resumo diário
1. No Telegram, fale com **@BotFather** → `/newbot` → escolha um nome → ele te dá um **TOKEN**.
2. Mande qualquer mensagem pro seu bot novo (abre a conversa).
3. Abra `https://api.telegram.org/bot<TOKEN>/getUpdates` no navegador → copie o número em `"chat":{"id": ...}`.
4. Salve `TELEGRAM_BOT_TOKEN` e `TELEGRAM_CHAT_ID` nos Secrets (passo 3).

### 6. Testar
**Actions** (aba do repo) → se pedir, clique "I understand my workflows, enable them" →
selecione **Commodities Radar (nuvem)** → **Run workflow** → mode `daily` → Run.
Em ~2-3 min: o job fica verde, o link do Pages abre o relatório no celular, e (se
configurou) o resumo cai no Telegram. Pronto — daí em diante roda sozinho.

---

## Manutenção e cuidados

- **Custo:** GitHub Actions é grátis até 2.000 min/mês em repo privado. O intraday é
  limitado ao pregão (seg-sex 9h-18h30 BRT) justamente pra caber folgado.
- **Risco a validar no 1º run:** o Yahoo (preço CBOT) às vezes limita IPs de datacenter.
  Se o `cme_cbot` aparecer com erro no card "Saúde das fontes" do HTML, a saída é
  rotear o CBOT pelo ScraperAPI (ajuste pequeno — me avise que eu faço).
- **Inputs físicos manuais** (`fisico add`) continuam sendo seus, locais. Pra refletir
  na nuvem, rode local e dê `git push` quando atualizar — ou me peça um formulário simples.
- **Não precisa mais do Task Scheduler local** depois que a nuvem estiver de pé.
- **Validação local antes do push** (quando o shell voltar):
  `.venv\Scripts\python.exe cloud_run.py --mode intraday` e `--mode daily`.
