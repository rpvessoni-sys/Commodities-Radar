# Wrapper para executar comandos do radar via Task Scheduler.
#
# Uso direto:
#   .\run_radar.ps1 run               # pipeline completo
#   .\run_radar.ps1 public            # so coletores publicos
#   .\run_radar.ps1 public cftc_cot   # so 1 coletor
#
# Variaveis de ambiente:
#   $env:RADAR_LOG_DIR  pasta para logs (default: ../data/logs)

param(
    [string]$Cmd = "run",
    [string]$Source = ""
)

$ErrorActionPreference = "Continue"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $here

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
# Sem isso, Python escreve cp1252 quando stdout e pipe (Task Scheduler) e
# quebra com acento/emoji — caveat #1 do projeto.
$env:PYTHONIOENCODING = "utf-8"

# Diretorio de logs
$logDir = if ($env:RADAR_LOG_DIR) { $env:RADAR_LOG_DIR } else { Join-Path $here "..\data\logs" }
if (-not (Test-Path $logDir)) {
    New-Item -ItemType Directory -Path $logDir -Force | Out-Null
}

$timestamp = Get-Date -Format "yyyy-MM-dd_HHmmss"
$logFile = Join-Path $logDir "radar_${Cmd}_${timestamp}.log"

# Args para o python
$pyArgs = @($Cmd)
if ($Source) {
    $pyArgs += "--source"
    $pyArgs += $Source
}

$pythonExe = Join-Path $here ".venv\Scripts\python.exe"
if (-not (Test-Path $pythonExe)) {
    Write-Output "[run_radar] ERRO: venv nao encontrado em $pythonExe"
    "[run_radar] ERRO: venv nao encontrado em $pythonExe" | Out-File $logFile -Encoding utf8
    exit 1
}

Write-Output "[run_radar] $timestamp | $Cmd $Source"
"[run_radar] $timestamp | $Cmd $Source" | Out-File $logFile -Encoding utf8 -Append

& $pythonExe main.py @pyArgs 2>&1 | Tee-Object -FilePath $logFile -Append

$exitCode = $LASTEXITCODE
"[run_radar] exit code: $exitCode" | Out-File $logFile -Encoding utf8 -Append
exit $exitCode
