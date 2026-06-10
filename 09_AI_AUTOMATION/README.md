# 09_AI_AUTOMATION - Headless Claude Reviews (v1.8)

Type 1 automation. Advisory output only. The AI is READ-ONLY; the wrapper
script writes the review file to `08_DADOS_E_JOURNAL/AI_REVIEWS/` and
performs a narrowly scoped git commit and push. The AI never modifies
scanner logic, thresholds, schemas, journals, or governance documents -
and as of v1.2 it cannot, by tool allowlist.

## Architecture (v1.2)

```text
Task Scheduler (21:35 daily / Sunday 10:45)
  -> wrapper .ps1
       gates: idempotency, shared repo lock, prompt present, branch main
       runs schema validator itself, injects output into the prompt
       claude -p (allowlist: Read, Glob, Grep ONLY) -> JSON result
       wrapper writes DAILY_REVIEW_/WEEKLY_REVIEW_<date>.md
       wrapper does git add (that file only), commit, push
       try/finally guarantees lock release
```

## What runs

| Task | Schedule (local) | Script | Output |
|---|---|---|---|
| EURU Claude Daily Review | daily 21:35 | euru_claude_daily_review.ps1 | DAILY_REVIEW_<date>.md |
| EURU Claude Weekly Learning Review | Sunday 10:45 | euru_claude_weekly_review.ps1 | WEEKLY_REVIEW_<date>.md |

## Exit-code contract (v1.2, precedence order)

| Code | Stage | Meaning |
|---|---|---|
| 0 | - | Generated+published, resumed+published, or already synced |
| 5 | pre | Shared repo lock active (prior run in progress) |
| 2 | pre | Prompt file missing |
| 3 | pre | Repo not on main branch |
| 6 | claude | Claude failed: nonzero exit, JSON parse error, is_error, or empty result. Claude's own exit code is in the log. |
| 4 | write | Claude succeeded but the review file could not be written |
| 7 | git | Review file written but commit/push failed (file kept locally) |
| 1 | any | Unexpected wrapper exception (logged with stack trace) |
| 8 | pre | Preexisting staged changes in index (checked BEFORE generation) |

Precedence: pre-run gates first; 6 always beats 4 (write is never attempted
after a Claude failure); 7 means the artifact exists locally and only
synchronization failed. Missing output therefore always surfaces as 4 or 6,
never silently.

## Concurrency and timing

- ONE shared lock (`LOGS/euru_repo.lock`) is used by both daily and weekly
  wrappers, so delayed StartWhenAvailable runs can never perform git
  operations simultaneously. Stale threshold: 60 minutes.
- Task Scheduler ExecutionTimeLimit: 25 minutes per run - a hung process is
  killed long before the stale-lock threshold.
- Idempotency (v1.7): an existing review only counts as success when it is
  tracked, clean, AND present in origin/main. A file that exists but was
  never committed (e.g. after exit 7/8) triggers RESUME: the wrapper
  publishes the existing file without invoking Claude. A committed but
  unpushed file triggers push-only resume.

## One-time setup

1. Install Claude Code if not present (requires Node.js 18+):
   `npm install -g @anthropic-ai/claude-code`
   Run `claude` once interactively inside the repo to authenticate and
   trust the folder. Headless `-p` mode reuses that login.
   Docs: https://docs.claude.com/en/docs/claude-code/overview
2. Copy this folder to
   `C:\Users\andre\Desktop\EURU TOS MAIN\09_AI_AUTOMATION`.
3. From elevated PowerShell:
   `powershell -ExecutionPolicy Bypass -File .\euru_claude_tasks_setup.ps1`
4. Smoke test:
   `Start-ScheduledTask -TaskName "EURU Claude Daily Review"`
   then check `LOGS\` and `08_DADOS_E_JOURNAL\AI_REVIEWS\`.

## Guardrails

- AI allowlist: `Read,Glob,Grep` - no Write, no Bash, no network tools.
  The write boundary is enforced by the wrapper, not by instructions.
- All `.ps1` files are ASCII-only and run under Windows PowerShell 5.1
  without BOM or encoding issues. (PowerShell 7 also works.)
- Trust verification is disabled in `-p` mode by design; with a read-only
  allowlist the blast radius is reading repository files only.
- Widening the allowlist or the wrapper's git scope = Type 2 decision.

## Governance note

Activation is a Type 1 change (reporting only; no decision logic touched).
Record it in `01_GOVERNANCA/DECISOES_ESTRATEGICAS_REVISADO.md` so the audit
trail shows when AI reviews joined the daily loop.

## Repo-level requirement (apply once, Codex/operator)

Add to the repository .gitignore so locks and logs never enter git scope:

```text
09_AI_AUTOMATION/LOGS/
```

## Changelog

- v1.8 (2026-06-10): response to fourth Codex REJECT (single P1, final).
  Sync check is now content-level: git diff --quiet origin/main -- <file>
  replaces cat-file -e, so SKIP 0 requires the local committed review to
  be byte-identical to the remote; any difference (newer local commit or
  absence upstream) triggers push-only resume. git fetch failure is now
  fatal (exit 7) instead of silently comparing against a stale remote ref.

- v1.7 (2026-06-10): response to third Codex REJECT (single P1).
  Staged-index guard moved BEFORE generation: a dirty index now blocks the
  run with exit 8 before Claude is invoked and before any file is written.
  Idempotency rewritten to be sync-aware: existing review => SKIP only if
  tracked+clean+in origin/main; committed-but-unpushed => push-only resume;
  written-but-uncommitted => publish-only resume (no Claude call). A
  temporary failure can no longer masquerade as permanent success.
  Lock acquisition moved to the very start (resume paths touch git).
  Wrappers rewritten whole-file; weekly generated from daily via asserted
  substitutions (no silent patch misses possible).

- v1.6 (2026-06-10): response to second Codex REJECT.
  F1 (P1): weekly wrapper git block now uses GitRun like the daily
  (v1.4 patch had silently failed to match the weekly file; this patch
  asserted the match).
  F2 (P1): both wrappers now refuse to commit when the git index already
  contains staged changes (new exit 8), guaranteeing the "only the review
  file" contract; the offending staged list is logged.
  F3 (P2): repo-level .gitignore line documented above (LOGS/ including
  lock files) - to be applied by Codex with the activation commit.
  F4 (P2): daily prompt verdict validation scoped to AGUIA_ASIAN_SCAN
  reports only; WATCHLIST/GEM_ALERT/NO_TRADE documented as legitimate
  vocabulary of the other report types.

- v1.5 (2026-06-10): findings from the first real review artifact.
  Wrapper now strips any model preamble before the YAML front matter
  (output contract enforced mechanically, not just by instruction).
  Wrapper injects current local time; daily prompt gained a timing guard
  so midday/manual triggers evaluate the morning cycle only instead of
  flagging the not-yet-due evening scan as OPERATIONAL_FAILURE.
  Prompts now require plain ASCII punctuation in review output to avoid
  encoding garble when PS 5.1 tooling reads the files.

- v1.4 (2026-06-10): first full end-to-end run reached the git stage and
  exposed the same PS 5.1 stderr gotcha there: git add wrote a harmless
  LF/CRLF warning to stderr and EAP=Stop turned it into exit 7. All git
  operations now go through a GitRun helper (EAP relaxed, output logged,
  success judged only by the real exit code, per-step error messages).
  Run header label fixed to report the actual version.

- v1.3 (2026-06-10): fixes from first real Task Scheduler run (exit -1).
  Bug 1: PS 5.1 turns redirected native stderr into terminating errors
  under ErrorActionPreference=Stop; the claude call now runs with EAP
  relaxed locally, stderr captured to its own file, prompt passed via
  stdin (no command-line quoting/length issues).
  Bug 2: claude invocation wrapped in try/catch so failures honor exit 6
  instead of crashing with -1; explicit Get-Command pre-check logs the
  PATH when claude is not resolvable in the scheduler context.
  New: outer catch-all returns exit 1 with stack trace in the log, so the
  exit-code contract can no longer be bypassed by an unexpected exception.

- v1.2 (2026-06-10): response to Codex REJECT.
  P0 fixed: all .ps1 ASCII-only (parsed clean under PS 5.1).
  Allowlist reduced to Read/Glob/Grep; wrapper now writes the file and
  performs git (write boundary enforced, Bash pattern question mooted).
  try/finally guarantees lock release on every termination path.
  Single shared repo lock for daily + weekly (no concurrent git ops).
  Exit-code precedence contract documented (0/5/2/3/6/4/7).
  Self-referential COMMIT field removed from review files; git evidence
  lives in the wrapper log.
  Schema validator now executed by the wrapper, output injected into the
  prompt (AI no longer needs Bash).
- v1.1 (2026-06-10): idempotency, per-job locks, exit codes (superseded).
- v1.0 (2026-06-10): initial package.
