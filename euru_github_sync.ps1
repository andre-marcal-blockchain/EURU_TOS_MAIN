Set-Location "C:\Users\andre\Desktop\EURU TOS MAIN"

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

$remote = git remote get-url origin 2>$null
if (-not $remote) {
    Write-Host "Committed locally — no origin remote configured." -ForegroundColor Yellow
    exit 0
}

$branch = git branch --show-current
$pushResult = git push origin $branch 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "SUCCESS: $message" -ForegroundColor Green
} else {
    Write-Host "ERROR: Push failed — $pushResult" -ForegroundColor Red
    exit 1
}
