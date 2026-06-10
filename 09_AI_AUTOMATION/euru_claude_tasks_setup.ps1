# euru_claude_tasks_setup.ps1  (v1.8, ASCII-only for PS 5.1)
# Registers the two scheduled tasks for headless Claude reviews.
# Run ONCE from an elevated PowerShell:
#   powershell -ExecutionPolicy Bypass -File .\euru_claude_tasks_setup.ps1
# Optional: if PowerShell 7 is installed, replace $PsExe with the
# path to pwsh.exe. Not required: all scripts are ASCII-only.

$ErrorActionPreference = "Stop"

$Identity = [Security.Principal.WindowsIdentity]::GetCurrent()
$Principal = New-Object Security.Principal.WindowsPrincipal($Identity)
if (-not $Principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    throw "Administrator privileges are required. Run PowerShell as Administrator."
}

$Repo   = "C:\Users\andre\Desktop\EURU TOS MAIN"
$AutoMa = Join-Path $Repo "09_AI_AUTOMATION"

$DailyScript  = Join-Path $AutoMa "euru_claude_daily_review.ps1"
$WeeklyScript = Join-Path $AutoMa "euru_claude_weekly_review.ps1"

foreach ($s in @($DailyScript, $WeeklyScript)) {
    if (-not (Test-Path $s)) {
        throw "Missing script: $s -- copy the 09_AI_AUTOMATION folder into the repo first."
    }
}

$PsExe = (Get-Command powershell.exe).Source

$Settings = New-ScheduledTaskSettingsSet `
    -StartWhenAvailable `
    -ExecutionTimeLimit (New-TimeSpan -Minutes 25) `
    -RestartCount 1 -RestartInterval (New-TimeSpan -Minutes 5)

# Task 1: daily 21:35 local time.
$ActionD  = New-ScheduledTaskAction -Execute $PsExe `
    -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$DailyScript`""
$TriggerD = New-ScheduledTaskTrigger -Daily -At 21:35

Register-ScheduledTask -TaskName "EURU Claude Daily Review" `
    -Action $ActionD -Trigger $TriggerD -Settings $Settings `
    -Description "Headless Claude post-scan verification (Type 1, advisory, read-only AI)" -Force

# Task 2: Sunday 10:45 local time.
$ActionW  = New-ScheduledTaskAction -Execute $PsExe `
    -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$WeeklyScript`""
$TriggerW = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Sunday -At 10:45

Register-ScheduledTask -TaskName "EURU Claude Weekly Learning Review" `
    -Action $ActionW -Trigger $TriggerW -Settings $Settings `
    -Description "Headless Claude weekly learning review (Type 1, advisory, read-only AI)" -Force

Write-Host ""
Write-Host "Registered:"
Get-ScheduledTask -TaskName "EURU Claude*" | Format-Table TaskName, State

Write-Host "Test now with:"
Write-Host '  Start-ScheduledTask -TaskName "EURU Claude Daily Review"'
