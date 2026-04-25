param(
    [Parameter(Mandatory=$true)]
    [string]$EuruRoot,

    [string]$PythonExe = "python"
)

$TaskName = "Euru_Learning_Preflight"
$ScriptPath = Join-Path $EuruRoot "euru_learning_preflight.py"
$Arguments = "`"$ScriptPath`" --root `"$EuruRoot`" --write-report"

$Action = New-ScheduledTaskAction -Execute $PythonExe -Argument $Arguments -WorkingDirectory $EuruRoot
$Trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Friday -At 8:30PM
$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable
$Principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Highest

Register-ScheduledTask -TaskName $TaskName -Action $Action -Trigger $Trigger -Settings $Settings -Principal $Principal -Force
Write-Host "Scheduled task '$TaskName' created/updated successfully."
