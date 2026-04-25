param(
    [Parameter(Mandatory=$true)]
    [string]$EuruRoot,

    [string]$PythonExe = "python",

    [string]$TaskName = "Euru_Friday_Cycle",

    [string]$TaskFolder = "\\Euru\\"
)

$scriptPath = Join-Path $EuruRoot "euru_friday_cycle.py"
if (-not (Test-Path $scriptPath)) {
    throw "Could not find orchestrator script at $scriptPath"
}

$action = New-ScheduledTaskAction -Execute $PythonExe -Argument "`"$scriptPath`" --root `"$EuruRoot`""
$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Friday -At 8:30PM
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable

if (-not (Get-ScheduledTask -TaskName $TaskName -TaskPath $TaskFolder -ErrorAction SilentlyContinue)) {
    Register-ScheduledTask -TaskName $TaskName -TaskPath $TaskFolder -Action $action -Trigger $trigger -Settings $settings -Description "Runs the official EURU Friday cycle orchestrator."
} else {
    Set-ScheduledTask -TaskName $TaskName -TaskPath $TaskFolder -Action $action -Trigger $trigger -Settings $settings
}

Write-Host "Scheduled task registered/updated: $TaskFolder$TaskName"
