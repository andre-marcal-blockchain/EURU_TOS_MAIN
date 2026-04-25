# euru_schedule_setup.ps1
# Run this script ONCE as Administrator to register the Euru_GitHub_Sync scheduled task.
# Right-click PowerShell -> "Run as administrator", then execute this file.

#Requires -RunAsAdministrator

$taskName   = "Euru_GitHub_Sync"
$scriptPath = "C:\Users\andre\Desktop\Euru_TOS\euru_github_sync.ps1"
$runAsUser  = $env:USERNAME   # runs as the current (logged-in) user

$action = New-ScheduledTaskAction `
    -Execute   "powershell.exe" `
    -Argument  "-NonInteractive -WindowStyle Hidden -ExecutionPolicy Bypass -File `"$scriptPath`""

$trigger = New-ScheduledTaskTrigger -Daily -At "20:00"

$settings = New-ScheduledTaskSettingsSet `
    -ExecutionTimeLimit    (New-TimeSpan -Hours 1) `
    -StartWhenAvailable `
    -RunOnlyIfNetworkAvailable `
    -MultipleInstances     IgnoreNew

$principal = New-ScheduledTaskPrincipal `
    -UserId    $runAsUser `
    -LogonType Interactive `
    -RunLevel  Highest

Register-ScheduledTask `
    -TaskName   $taskName `
    -Action     $action `
    -Trigger    $trigger `
    -Settings   $settings `
    -Principal  $principal `
    -Description "Daily Euru OS GitHub sync at 20:00 — commits and pushes all changes." `
    -Force

Write-Host ""
Write-Host "Scheduled task '$taskName' registered successfully." -ForegroundColor Green
Write-Host "  Runs daily at 20:00 as user: $runAsUser" -ForegroundColor Cyan
Write-Host ""
Write-Host "Verify with: Get-ScheduledTask -TaskName '$taskName'" -ForegroundColor Yellow
Write-Host "Run manually: Start-ScheduledTask -TaskName '$taskName'" -ForegroundColor Yellow
