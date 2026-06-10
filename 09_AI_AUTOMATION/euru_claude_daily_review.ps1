# euru_claude_daily_review.ps1  (v1.8)
# Headless Claude Code daily post-scan review for EURU TOS.
# Architecture: Claude is READ-ONLY. The wrapper writes the review file and
# performs the git commit/push deterministically. ASCII-only for PS 5.1.
#
# Exit codes (precedence order):
#   0 = review generated+published, resumed+published, or already synced
#   5 = shared repo lock active (prior run still in progress)
#   2 = prompt file missing
#   3 = repo not on main branch
#   8 = preexisting staged changes in git index (checked BEFORE generation)
#   6 = claude failed (nonzero exit, parse error, or empty result)
#   4 = claude succeeded but review file could not be written
#   7 = review exists locally but commit/push failed (resume next run)
#   1 = unexpected wrapper exception (caught and logged)
#
# Idempotency (v1.8): an existing review file only counts as success when
# it is tracked, clean, AND present in origin/main. Otherwise the wrapper
# RESUMES publication of the existing file without calling Claude.

$ErrorActionPreference = "Stop"

$Repo      = "C:\Users\andre\Desktop\EURU TOS MAIN"
$PromptMd  = Join-Path $Repo "09_AI_AUTOMATION\EURU_DAILY_REVIEW_PROMPT.md"
$LogDir    = Join-Path $Repo "09_AI_AUTOMATION\LOGS"
$Lock      = Join-Path $LogDir "euru_repo.lock"   # SHARED lock (daily + weekly)
$Stamp     = Get-Date -Format "yyyy-MM-dd_HHmm"
$Today     = Get-Date -Format "yyyy-MM-dd"
$LogFile   = Join-Path $LogDir "daily_review_$Stamp.log"
$ReviewRel = "08_DADOS_E_JOURNAL/AI_REVIEWS/DAILY_REVIEW_$Today.md"
$ReviewDir = Join-Path $Repo "08_DADOS_E_JOURNAL\AI_REVIEWS"
$Review    = Join-Path $ReviewDir ("DAILY_REVIEW_" + $Today + ".md")
$CommitMsg = "Euru OS - $Today - claude daily review"

New-Item -ItemType Directory -Force -Path $LogDir, $ReviewDir | Out-Null
Set-Location $Repo

function Log([string]$Msg) { $Msg | Tee-Object -FilePath $LogFile -Append }

# Run git with EAP relaxed: PS 5.1 turns redirected native stderr into
# terminating errors under EAP=Stop, and git writes WARNINGS to stderr
# (e.g. LF/CRLF notices). Only the real exit code decides success.
function GitRun {
    param([string[]]$GitArgs)
    $Prev = $ErrorActionPreference
    $ErrorActionPreference = "Continue"
    $Out = (& git @GitArgs 2>&1 | Out-String).Trim()
    $Code = $LASTEXITCODE
    $ErrorActionPreference = $Prev
    if ($Out) { $Out | Out-File -FilePath $LogFile -Append -Encoding utf8 }
    return $Code
}

Log "=== EURU Claude daily review v1.8 started $Stamp ==="

# Shared repository lock FIRST: every later step may touch git state.
if (Test-Path $Lock) {
    $LockAge = (Get-Date) - (Get-Item $Lock).LastWriteTime
    if ($LockAge.TotalMinutes -lt 60) {
        Log ("ABORT: shared lock present ({0} min old). Exit 5." -f [int]$LockAge.TotalMinutes)
        exit 5
    }
    Log "WARN: stale shared lock (over 60 min). Removing."
    Remove-Item $Lock -Force
}
New-Item -ItemType File -Path $Lock -Force | Out-Null

try {
    # Gates.
    if (-not (Test-Path $PromptMd)) { Log "FATAL: prompt file missing. Exit 2."; exit 2 }

    if ((GitRun @("fetch","origin")) -ne 0) {
        Log "ERROR: git fetch failed; cannot trust remote state. Exit 7."
        exit 7
    }
    $Branch = (git rev-parse --abbrev-ref HEAD).Trim()
    if ($Branch -ne "main") { Log "FATAL: repo on '$Branch', not main. Exit 3."; exit 3 }
    Log ("GIT STATUS BEFORE: " + ((git status --short) -join " | "))

    # Staged-index guard BEFORE any generation or publication (Codex P1):
    # git commit includes everything staged; a dirty index would violate
    # the "only the review file" contract and must block the whole run.
    if ((GitRun @("diff","--cached","--quiet")) -ne 0) {
        Log "ABORT: preexisting staged changes in index. Exit 8. Staged list:"
        [void](GitRun @("diff","--cached","--name-only"))
        exit 8
    }

    # Idempotency v1.7: existing file is only success if committed AND synced.
    $Generate = $true
    if (Test-Path $Review) {
        $Porcelain = (git status --porcelain -- $Review | Out-String).Trim()
        if ([string]::IsNullOrWhiteSpace($Porcelain)) {
            # Tracked and clean locally. Content-level sync check against
            # the just-fetched origin/main: diff --quiet returns 0 only when
            # the file is identical to the remote (absence or any content
            # difference returns nonzero -> push-only resume).
            if ((GitRun @("diff","--quiet","origin/main","--",$ReviewRel)) -eq 0) {
                Log "SKIP: review for $Today is committed and identical to origin/main. Exit 0."
                exit 0
            }
            Log "RESUME: local committed review differs from (or is absent in) origin/main. Pushing."
            if ((GitRun @("push","origin","main")) -ne 0) {
                Log "ERROR: git push failed. Sync still pending. Exit 7."
                exit 7
            }
            Log "PUSH: ok (resume). Exit 0."
            exit 0
        }
        Log "RESUME: review exists but is not committed ($Porcelain). Publishing existing file without regenerating."
        $Generate = $false
    }

    if ($Generate) {
        # Wrapper-side evidence: schema validator (best effort).
        $ValidatorOut = "schema validator not present or not run"
        if (Test-Path (Join-Path $Repo "euru_schema_validator.py")) {
            try {
                $ValidatorOut = (& python (Join-Path $Repo "euru_schema_validator.py") 2>&1 | Out-String).Trim()
                Log "Validator executed by wrapper."
            } catch {
                $ValidatorOut = "validator FAILED to run: $($_.Exception.Message)"
                Log $ValidatorOut
            }
        }

        $Template = Get-Content -Raw -Encoding UTF8 $PromptMd
        $Prompt = $Template + "`n`n## Wrapper-provided evidence`n" +
                  "Date today: $Today`n" +
                  "Current local time: " + (Get-Date -Format "HH:mm") + " Europe/Madrid`n" +
                  "Schema validator output:`n" + $ValidatorOut + "`n"

        # Pre-check: claude must resolve in THIS (Task Scheduler) context.
        $ClaudeCmd = Get-Command claude -ErrorAction SilentlyContinue
        if (-not $ClaudeCmd) {
            Log "FATAL: 'claude' not found in PATH of this context. Exit 6."
            Log ("PATH was: " + $env:Path)
            exit 6
        }
        Log ("Claude CLI: " + $ClaudeCmd.Source)

        # Headless run. READ-ONLY allowlist. Prompt via stdin; stderr to its
        # own file; EAP relaxed around the native call (PS 5.1 gotcha).
        $StderrFile = Join-Path $LogDir ("claude_stderr_" + $Stamp + ".log")
        $RawText = ""
        $ClaudeExit = -1
        try {
            $PrevEAP = $ErrorActionPreference
            $ErrorActionPreference = "Continue"
            $RawOut = $Prompt | & $ClaudeCmd.Source -p --allowedTools "Read,Glob,Grep" --output-format json 2> $StderrFile
            $ClaudeExit = $LASTEXITCODE
            $ErrorActionPreference = $PrevEAP
            $RawText = ($RawOut | Out-String).Trim()
        } catch {
            $ErrorActionPreference = $PrevEAP
            Log "FATAL: claude invocation threw: $($_.Exception.Message). Exit 6."
            exit 6
        }

        if ($ClaudeExit -ne 0 -or [string]::IsNullOrWhiteSpace($RawText)) {
            Log "FATAL: claude exit=$ClaudeExit, output empty=$([string]::IsNullOrWhiteSpace($RawText)). Exit 6."
            Log "See stderr capture: $StderrFile"
            exit 6
        }

        $Result = $null
        try {
            $Json = $RawText | ConvertFrom-Json
            if ($Json.is_error -eq $true) { Log "FATAL: claude reported is_error=true. Exit 6."; exit 6 }
            $Result = [string]$Json.result
        } catch {
            Log "FATAL: could not parse claude JSON output. Exit 6. Raw saved to log."
            $RawText | Out-File -FilePath $LogFile -Append -Encoding utf8
            exit 6
        }
        if ([string]::IsNullOrWhiteSpace($Result)) { Log "FATAL: empty result field. Exit 6."; exit 6 }

        # Enforce output contract: strip preamble before YAML front matter.
        $Idx = $Result.IndexOf("---")
        if ($Idx -gt 0) {
            Log ("Contract enforcement: stripped " + $Idx + " preamble chars before front matter.")
            $Result = $Result.Substring($Idx)
        } elseif ($Idx -lt 0) {
            Log "WARN: no front matter found in result; saving as-is."
        }

        try {
            $Enc = New-Object System.Text.UTF8Encoding($false)
            [System.IO.File]::WriteAllText($Review, $Result, $Enc)
            Log "Review written: $Review"
        } catch {
            Log "FATAL: failed to write review file: $($_.Exception.Message). Exit 4."
            exit 4
        }
    }

    # Publication stage (shared by generate and resume paths).
    if ((GitRun @("add","--",$Review)) -ne 0) {
        Log "ERROR: git add failed. Review kept locally. Exit 7."
        exit 7
    }
    if ((GitRun @("commit","-m",$CommitMsg)) -ne 0) {
        Log "ERROR: git commit failed. Review kept locally. Exit 7."
        exit 7
    }
    $Hash = (git rev-parse --short HEAD).Trim()
    Log "COMMIT: $Hash"
    if ((GitRun @("push","origin","main")) -ne 0) {
        Log "ERROR: git push failed. Commit exists locally ($Hash); resume will push next run. Exit 7."
        exit 7
    }
    Log "PUSH: ok"
    Log "=== Success. Exit 0. ==="
    exit 0
}
catch {
    Log "UNEXPECTED wrapper exception: $($_.Exception.Message)"
    Log ($_.ScriptStackTrace)
    exit 1
}
finally {
    Remove-Item $Lock -Force -ErrorAction SilentlyContinue
}
