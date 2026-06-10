# EURU v1.2 - Response to Codex REJECT (2026-06-10)

DATE: 2026-06-10
AI: Claude (chat session)
OBJECTIVE: Address all 7 findings from Codex review of 09_AI_AUTOMATION v1.1.

| # | Finding | Severity | Resolution in v1.2 |
|---|---|---|---|
| 1 | UTF-8 no BOM + em dashes break PS 5.1; setup had 4 parser errors | P0 | All .ps1 rewritten ASCII-only (verified byte-by-byte: no chars > 0x7F). No pwsh dependency introduced. |
| 2 | Allowlist not a strong write boundary; Bash pattern syntax doubt | P1 | Architecture changed: Claude allowlist is now Read,Glob,Grep only. Wrapper writes the review file and performs git. Schema validator is executed by the wrapper and its output injected into the prompt. Bash pattern question is moot - no Bash granted. |
| 3 | Lock cleanup not guaranteed | P1 | Entire run body wrapped in try/finally; finally removes the lock on every termination path including exit inside try. |
| 4 | Exit-code contract inconsistent | P1 | Precedence documented: 0/5/2/3/6/4/7. Claude failure = 6 (its exit code logged); write failure = 4; git failure = 7 with artifact kept. Missing output can never masquerade as success. |
| 5 | Self-referential commit hash impossible | P1 | COMMIT/GIT STATUS fields removed from the review file format. Git evidence (status before, hash, push result) is recorded in the wrapper log. |
| 6 | Delayed runs can overlap on git | P2 | Single shared lock (euru_repo.lock) for both jobs, 60 min stale threshold, 25 min ExecutionTimeLimit. |
| 7 | Tests blocked | - | Unblocked by P0 fix. Re-run all five cases; add case 6: simulate claude failure (rename claude on PATH or disconnect network) and confirm exit 6 with no file written and no commit. |

REVIEW REQUIRED: YES - Codex re-review of v1.2 with the six test cases.
NEXT ACTION: Codex re-runs tests; on APPROVE, governance registration,
SIMULATE correction in AGUIA master, commit, push, then operator activates.
