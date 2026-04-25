Set-Location "C:\Users\andre\Desktop\EURO MAIN"

git add .

$status = git status --porcelain
if (-not $status) {
    Write-Host "Nothing to commit — repository is up to date." -ForegroundColor Green
    exit 0
}

$count = ($status | Measure-Object -Line).Lines
$date = Get-Date -Format "yyyy-MM-dd"
$message = "Euru OS — $date — $count files updated"

git commit -m $message

$pushResult = git push 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "SUCCESS: $message" -ForegroundColor Green
} else {
    Write-Host "ERROR: Push failed — $pushResult" -ForegroundColor Red
    exit 1
}
