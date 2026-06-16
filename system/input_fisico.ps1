# Atalho interativo pra inputar precos fisicos.
#
# Roda 'main.py fisico add' no modo interativo, com janela do console
# que fica aberta apos terminar (pra ver o resumo).
#
# Como criar atalho no Desktop:
#   1. Botao direito no Desktop -> Novo -> Atalho
#   2. Local: powershell -ExecutionPolicy Bypass -File "C:\Users\Usuario\OneDrive\Desktop\Program\commodities-radar\system\input_fisico.ps1"
#   3. Nome: Input Fisico
#
# Ou rode direto:
#   .\input_fisico.ps1

$ErrorActionPreference = "Continue"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $here

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$pythonExe = Join-Path $here ".venv\Scripts\python.exe"
if (-not (Test-Path $pythonExe)) {
    Write-Host "[ERRO] venv nao encontrado em $pythonExe" -ForegroundColor Red
    Read-Host "Aperte Enter pra fechar"
    exit 1
}

Clear-Host
Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  RADAR  -  Input de PRECOS DE COMPRA do complexo soja" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "  Matriz: 2 pracas x 3 produtos = ate 6 cotacoes por dia" -ForegroundColor White
Write-Host ""
Write-Host "  Pracas:" -ForegroundColor White
Write-Host "    1. Rancharia/SP   - compra no interior oeste paulista" -ForegroundColor Gray
Write-Host "    2. Paranagua/PR   - compra no porto (ref. exportacao)" -ForegroundColor Gray
Write-Host ""
Write-Host "  Produtos (cada um na sua unidade):" -ForegroundColor White
Write-Host "    a. Soja em grao           - R`$/saca 60kg     ex: 129,50" -ForegroundColor Gray
Write-Host "    b. Farelo de soja         - R`$/tonelada      ex: 1.850 ou 1850" -ForegroundColor Gray
Write-Host "    c. Oleo de soja degomado  - R`$/tonelada      ex: 5.200 ou 5200" -ForegroundColor Gray
Write-Host ""
Write-Host "  Para CADA combo praca/produto o sistema vai pedir:" -ForegroundColor White
Write-Host "    - Preco em R`$ na unidade do produto    (obrigatorio)" -ForegroundColor Gray
Write-Host "    - Preco em US`$ opcional                 (so Paranagua)" -ForegroundColor Gray
Write-Host "    - Observacao opcional                   (fonte/contexto)" -ForegroundColor Gray
Write-Host ""
Write-Host "  ENTER pula qualquer campo. Rancharia nao tem farelo/oleo? pula." -ForegroundColor Yellow
Write-Host "  Sistema calcula automatico: premio fisico vs paridade CBOT," -ForegroundColor Yellow
Write-Host "  spread Paranagua-Rancharia, e compara com indicador CEPEA." -ForegroundColor Yellow
Write-Host "  Tudo gravado no historico imutavel (audit preservado)." -ForegroundColor Yellow
Write-Host ""
Write-Host "------------------------------------------------------------" -ForegroundColor Cyan

& $pythonExe main.py fisico add

Write-Host ""
Write-Host "------------------------------------------------------------" -ForegroundColor Cyan
Write-Host "  Ultimos 7 dias registrados:" -ForegroundColor Cyan
Write-Host "------------------------------------------------------------" -ForegroundColor Cyan
& $pythonExe main.py fisico list --days 7

Write-Host ""
Write-Host "------------------------------------------------------------" -ForegroundColor Cyan
Write-Host "  Regenerando HTML diario..." -ForegroundColor Cyan
Write-Host "------------------------------------------------------------" -ForegroundColor Cyan
& $pythonExe -c "from notify_html import gerar_html; p = gerar_html(); print(f'OK: {p}')"
Write-Host ""
Write-Host "  Para ver: abra o atalho 'Radar Daily' no Desktop (Ctrl+F5 se ja estiver aberto)" -ForegroundColor Yellow

Write-Host ""
Read-Host "Aperte Enter pra fechar"
