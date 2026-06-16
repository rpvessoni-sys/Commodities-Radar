# Atalho interativo para criar um novo insight de estudo.
#
# Roda main.py insight new <titulo> e abre o arquivo no Notepad.
# Como criar atalho no Desktop:
#   1. Botao direito Desktop -> Novo -> Atalho
#   2. Local: powershell -ExecutionPolicy Bypass -File "C:\Users\Usuario\OneDrive\Desktop\Program\commodities-radar\system\new_insight.ps1"
#   3. Nome: Novo Insight

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
Write-Host "  RADAR  -  Novo Insight de Estudo" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "  Insight = resumo executivo de uma analise/estudo/conversa" -ForegroundColor White
Write-Host "  com o consultor, com lifecycle (data, revisao D+90/D+180)." -ForegroundColor White
Write-Host ""
Write-Host "  Como funciona:" -ForegroundColor White
Write-Host "    1. Voce digita o titulo (ex: 'B16 bullish farelo')" -ForegroundColor Gray
Write-Host "    2. Sistema cria arquivo .md com template em insights/" -ForegroundColor Gray
Write-Host "    3. Notepad abre pra voce preencher" -ForegroundColor Gray
Write-Host "    4. Salva o arquivo, fecha o Notepad" -ForegroundColor Gray
Write-Host "    5. HTML diario sera regerado automaticamente" -ForegroundColor Gray
Write-Host ""
Write-Host "  Aparece na aba 'Insights' do HTML, ordenado por data DESC." -ForegroundColor Yellow
Write-Host ""
Write-Host "------------------------------------------------------------" -ForegroundColor Cyan

$titulo = Read-Host "  Titulo do insight"
if ([string]::IsNullOrWhiteSpace($titulo)) {
    Write-Host "[cancelado] sem titulo, nada feito." -ForegroundColor Yellow
    Read-Host "Aperte Enter pra fechar"
    exit 0
}

Write-Host ""
Write-Host "  Criando..." -ForegroundColor Cyan
& $pythonExe main.py insight new --open $titulo

Write-Host ""
Write-Host "------------------------------------------------------------" -ForegroundColor Cyan
Write-Host "  Quando terminar de editar e salvar o .md," -ForegroundColor Yellow
Write-Host "  feche o Notepad e aperte ENTER aqui pra regenerar o HTML" -ForegroundColor Yellow
Write-Host "------------------------------------------------------------" -ForegroundColor Cyan
Read-Host "  Aperte Enter quando salvar"

Write-Host ""
Write-Host "  Regenerando HTML diario..." -ForegroundColor Cyan
& $pythonExe -c "from notify_html import gerar_html; p = gerar_html(); print(f'OK: {p}')"

Write-Host ""
Write-Host "  Insight criado! Abra 'Radar Daily' e va na aba 'Insights'" -ForegroundColor Green
Write-Host "  (ou aperte 6 pra ir direto)" -ForegroundColor Green
Write-Host ""
Read-Host "Aperte Enter pra fechar"
