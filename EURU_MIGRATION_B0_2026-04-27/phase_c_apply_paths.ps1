$Apply = $true  # Dry-run by default. Set to $true only after operator review.

$tasks = @(
    "Euru_Morning_Scan",
    "Euru_Asian_Scan",
    "Euru_Journal_Auditor",
    "Euru_Smoke_Test_Night",
    "Euru_GitHub_Sync",
    "Euru_Friday_Cycle",
    "EuruLearningEngine",
    "Euru_Daily_Audit",
    "Euru_Weekly_Audit"
)

$oldPaths = @(
    "C:\Users\andre\Desktop\EURO MAIN",
    "C:\Users\andre\Desktop\Euru_TOS"
)

$newPath = "C:\Users\andre\Desktop\EURU TOS MAIN"

foreach ($taskName in $tasks) {
    $task = Get-ScheduledTask -TaskName $taskName
    $originalState = $task.State

    if ($originalState -eq "Running") {
        throw "ABORT: $taskName is Running. Stop migration and retry after task finishes."
    }

    if (($task.Actions | Measure-Object).Count -ne 1) {
        throw "ABORT: $taskName has multiple actions. Manual review required."
    }

    $action = $task.Actions | Select-Object -First 1

    $newExecute = $action.Execute
    $newArguments = $action.Arguments
    $newWorkingDirectory = $action.WorkingDirectory

    foreach ($oldPath in $oldPaths) {
        $escaped = [regex]::Escape($oldPath)
        $newExecute = $newExecute -replace $escaped, $newPath
        $newArguments = $newArguments -replace $escaped, $newPath
        $newWorkingDirectory = $newWorkingDirectory -replace $escaped, $newPath
    }

    Write-Host "`n=== $taskName ==="
    Write-Host "Original state:    $originalState"
    Write-Host "Execute:           $($action.Execute) -> $newExecute"
    Write-Host "Arguments:         $($action.Arguments) -> $newArguments"
    Write-Host "WorkingDirectory:  $($action.WorkingDirectory) -> $newWorkingDirectory"

    if (
        $newExecute -eq $action.Execute -and
        $newArguments -eq $action.Arguments -and
        $newWorkingDirectory -eq $action.WorkingDirectory
    ) {
        Write-Host "No path change detected."
    }

    $params = @{ Execute = $newExecute }

    if (-not [string]::IsNullOrWhiteSpace($newArguments)) {
        $params.Argument = $newArguments
    }

    if (-not [string]::IsNullOrWhiteSpace($newWorkingDirectory)) {
        $params.WorkingDirectory = $newWorkingDirectory
    }

    $newAction = New-ScheduledTaskAction @params

    if ($Apply) {
        Set-ScheduledTask -TaskName $taskName -TaskPath $task.TaskPath -Action $newAction | Out-Null

        $after = Get-ScheduledTask -TaskName $taskName -TaskPath $task.TaskPath

        if ($after.State -ne $originalState) {
            throw "ABORT: $taskName state changed from $originalState to $($after.State). Manual rollback from XML required."
        }

        Write-Host "Applied. State preserved: $($after.State)"
    } else {
        Write-Host "DRY-RUN only. No changes applied."
    }
}
