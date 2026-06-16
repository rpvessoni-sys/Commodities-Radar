# Backup do SQLite radar.db.
#
# Copia data/radar.db para data/backups/radar_YYYY-MM-DD.db.
# Mantem os ultimos 8 backups (~2 meses se rodar semanal) e apaga os mais antigos.
#
# Uso direto:
#   .\backup_db.ps1
#
# Recomendado: agendar semanal pelo setup_scheduler.ps1 (Sat 23:00).

$ErrorActionPreference = "Stop"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = Split-Path -Parent $here

$dbPath = Join-Path $projectRoot "data\radar.db"
$backupDir = Join-Path $projectRoot "data\backups"

if (-not (Test-Path $dbPath)) {
    Write-Host "[backup_db] ERRO: $dbPath nao encontrado" -ForegroundColor Red
    exit 1
}

if (-not (Test-Path $backupDir)) {
    New-Item -ItemType Directory -Path $backupDir -Force | Out-Null
}

$timestamp = Get-Date -Format "yyyy-MM-dd"
$backupPath = Join-Path $backupDir "radar_${timestamp}.db"

# Usa o comando .backup do SQLite (atomico, consistente mesmo com escritas concorrentes)
$pythonExe = Join-Path $here ".venv\Scripts\python.exe"
if (Test-Path $pythonExe) {
    & $pythonExe -c "import sqlite3, sys; src = sqlite3.connect(r'$dbPath'); dst = sqlite3.connect(r'$backupPath'); src.backup(dst); dst.close(); src.close(); print('OK')"
} else {
    # Fallback: copia simples
    Copy-Item $dbPath $backupPath -Force
}

$srcSize = (Get-Item $dbPath).Length / 1MB
$bkpSize = (Get-Item $backupPath).Length / 1MB
Write-Host "[backup_db] OK: $backupPath ($([math]::Round($bkpSize,2)) MB, source $([math]::Round($srcSize,2)) MB)"

# Rotacao: mantem os 8 backups mais recentes
$keep = 8
$todos = Get-ChildItem $backupDir -Filter "radar_*.db" | Sort-Object LastWriteTime -Descending
if ($todos.Count -gt $keep) {
    $apagar = $todos | Select-Object -Skip $keep
    foreach ($f in $apagar) {
        Remove-Item $f.FullName -Force
        Write-Host "[backup_db] rotacionado (apagado): $($f.Name)"
    }
}

Write-Host "[backup_db] backups atuais: $($todos.Count)"
