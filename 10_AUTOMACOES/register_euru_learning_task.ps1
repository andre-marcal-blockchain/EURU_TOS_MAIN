param(
    [string]$EuruRoot = (Split-Path -Parent $MyInvocation.MyCommand.Path),
    [string]$TaskName = "Euru_Learning_Engine_Friday_2030",
    [string]$PythonExe = "python"
)

$scriptPath = Join-Path $EuruRoot "euru_learning_engine.py"
if (-not (Test-Path $scriptPath)) {
    throw "Script not found: $scriptPath"
}

$action = New-ScheduledTaskAction -Execute $PythonExe -Argument "`"$scriptPath`" --root `"$EuruRoot`""
$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Friday -At 8:30PM
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries
$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Highest

Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Settings $settings -Principal $principal -Force
Write-Host "Scheduled task registered:" $TaskName
