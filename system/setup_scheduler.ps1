# Setup das tarefas agendadas do Commodities Radar no Windows Task Scheduler.
#
# Cria/atualiza tasks:
#   CommoditiesRadar_Morning  — diario 7h00 — pipeline completo (run)
#   CommoditiesRadar_Evening  — diario 19h00 — coletor CME pos-fechamento
#   CommoditiesRadar_Friday   — sex 18h00 — coletor CFTC COT (release ~15:30 NY)
#
# Uso:
#   .\setup_scheduler.ps1            # cria/atualiza tasks
#   .\setup_scheduler.ps1 -Remove    # remove tasks
#   .\setup_scheduler.ps1 -List      # lista tasks ja criadas

param(
    [switch]$Remove,
    [switch]$List
)

$ErrorActionPreference = "Stop"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$runScript = Join-Path $here "run_radar.ps1"

$weekdays = "Monday,Tuesday,Wednesday,Thursday,Friday"

$tasks = @(
    @{
        Name = "CommoditiesRadar_Morning"
        Description = "Manha (seg-sex 07h): pipeline completo + forecast 7d/30d"
        Time = "07:00"
        Days = $weekdays
        Args = "-Cmd run"
    },
    @{
        Name = "CommoditiesRadar_Evening"
        Description = "Pos-fechamento CBOT (seg-sex 19h): coletor CME"
        Time = "19:00"
        Days = $weekdays
        Args = "-Cmd public -Source cme_cbot"
    },
    @{
        Name = "CommoditiesRadar_Indicators"
        Description = "Indicadores derivados (seg-sex 20h): crush margin, oil share, spreads"
        Time = "20:00"
        Days = $weekdays
        Args = "-Cmd indicators"
    },
    @{
        Name = "CommoditiesRadar_Alerts"
        Description = "Alertas tecnicos (seg-sex 20h15): niveis quebrados, movimentos fortes"
        Time = "20:15"
        Days = $weekdays
        Args = "-Cmd alerts"
    },
    @{
        Name = "CommoditiesRadar_Night"
        Description = "Noite (seg-sex 22h): pipeline completo + forecast + noticias CEPEA RSS"
        Time = "22:00"
        Days = $weekdays
        Args = "-Cmd run"
    },
    @{
        Name = "CommoditiesRadar_Friday"
        Description = "Sex 18h: coleta CFTC COT (release sexta ~15:30 NY)"
        Time = "18:00"
        Days = "Friday"
        Args = "-Cmd public -Source cftc_cot"
    },
    @{
        Name = "CommoditiesRadar_Backup"
        Description = "Sab 23h: backup semanal do SQLite (mantem 8 ultimos)"
        Time = "23:00"
        Days = "Saturday"
        Args = "-Backup"
    }
)

if ($List) {
    Get-ScheduledTask | Where-Object { $_.TaskName -like "CommoditiesRadar_*" } | Format-Table -AutoSize TaskName, State, @{Label="LastRunTime"; Expression={(Get-ScheduledTaskInfo $_).LastRunTime}}
    exit 0
}

if ($Remove) {
    foreach ($t in $tasks) {
        $existing = Get-ScheduledTask -TaskName $t.Name -ErrorAction SilentlyContinue
        if ($existing) {
            Unregister-ScheduledTask -TaskName $t.Name -Confirm:$false
            Write-Output "Removed: $($t.Name)"
        } else {
            Write-Output "Not found: $($t.Name)"
        }
    }
    exit 0
}

# Cria/atualiza tasks
$backupScript = Join-Path $here "backup_db.ps1"
foreach ($t in $tasks) {
    if ($t.Args -eq "-Backup") {
        # Task de backup chama backup_db.ps1 direto
        $action = New-ScheduledTaskAction `
            -Execute "powershell.exe" `
            -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$backupScript`""
    } else {
        $action = New-ScheduledTaskAction `
            -Execute "powershell.exe" `
            -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$runScript`" $($t.Args)"
    }

    if ($t.Days -eq "Daily") {
        $trigger = New-ScheduledTaskTrigger -Daily -At $t.Time
    } else {
        # Days pode ser uma string com multiplos dias separados por virgula
        $daysArray = $t.Days -split ","
        $trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek $daysArray -At $t.Time
    }

    $settings = New-ScheduledTaskSettingsSet `
        -AllowStartIfOnBatteries `
        -DontStopIfGoingOnBatteries `
        -StartWhenAvailable `
        -ExecutionTimeLimit (New-TimeSpan -Hours 1)

    $principal = New-ScheduledTaskPrincipal `
        -UserId $env:USERNAME `
        -LogonType Interactive `
        -RunLevel Limited

    # Remove se ja existe
    $existing = Get-ScheduledTask -TaskName $t.Name -ErrorAction SilentlyContinue
    if ($existing) {
        Unregister-ScheduledTask -TaskName $t.Name -Confirm:$false
    }

    Register-ScheduledTask `
        -TaskName $t.Name `
        -Description $t.Description `
        -Action $action `
        -Trigger $trigger `
        -Settings $settings `
        -Principal $principal | Out-Null

    Write-Output "Created: $($t.Name)  ($($t.Days) $($t.Time))"
}

Write-Output ""
Write-Output "OK. Para listar: .\setup_scheduler.ps1 -List"
Write-Output "Para remover:    .\setup_scheduler.ps1 -Remove"
Write-Output "Logs ficarao em: $((Resolve-Path $here).Path)\..\data\logs\"
