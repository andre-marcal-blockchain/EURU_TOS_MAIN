# EURU Friday Cycle Report

- cycle_started_at: 2026-04-17T18:30:01Z
- cycle_finished_at: 2026-04-17T18:30:02Z
- overall_status: CLOSED_BLOCKED

## Step Summary

| step | status | started_at | ended_at | artifacts |
|---|---|---|---|---:|
| github_sync | PASS | 2026-04-17T18:30:02Z | 2026-04-17T18:30:02Z | 0 |
| schema_validation | BLOCKED | 2026-04-17T18:30:02Z | 2026-04-17T18:30:02Z | 1 |

## github_sync

- status: PASS
- started_at: 2026-04-17T18:30:02Z
- ended_at: 2026-04-17T18:30:02Z

### Details

```json
{
  "root": "C:\\Users\\andre\\Desktop\\EURO MAIN",
  "git_pull": false,
  "branch": "main",
  "commit": "6d2150eb3bc2c08db222f3f71fda918bcb667bf6",
  "dirty_files": [
    " ? Euru_TOSOld_02026-04-10",
    " ? Euru_TOS_GITHUB"
  ],
  "dirty_count": 2,
  "reason": "git repository inspected successfully"
}
```

### Artifacts

- none

## schema_validation

- status: BLOCKED
- started_at: 2026-04-17T18:30:02Z
- ended_at: 2026-04-17T18:30:02Z

### Details

```json
{
  "total_files": 41,
  "valid_files": 25,
  "invalid_files": 16,
  "warning_count": 0,
  "error_count": 16,
  "by_schema": {
    "daily_journal": {
      "total": 5,
      "valid": 5,
      "invalid": 0
    },
    "unknown": {
      "total": 16,
      "valid": 0,
      "invalid": 16
    },
    "scorecard": {
      "total": 18,
      "valid": 18,
      "invalid": 0
    },
    "learning_report": {
      "total": 2,
      "valid": 2,
      "invalid": 0
    }
  }
}
```

### Artifacts

- `C:\Users\andre\Desktop\EURO MAIN\08_DADOS_E_JOURNAL\SCORECARDS\SCHEMA_VALIDATION_REPORT_2026-04-17.md`
