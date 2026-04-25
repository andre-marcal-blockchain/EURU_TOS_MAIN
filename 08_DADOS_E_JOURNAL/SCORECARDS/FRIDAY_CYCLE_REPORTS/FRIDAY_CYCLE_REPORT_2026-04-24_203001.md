# EURU Friday Cycle Report

- cycle_started_at: 2026-04-24T18:30:00Z
- cycle_finished_at: 2026-04-24T18:30:01Z
- overall_status: CLOSED_BLOCKED

## Step Summary

| step | status | started_at | ended_at | artifacts |
|---|---|---|---|---:|
| github_sync | PASS | 2026-04-24T18:30:00Z | 2026-04-24T18:30:01Z | 0 |
| schema_validation | BLOCKED | 2026-04-24T18:30:01Z | 2026-04-24T18:30:01Z | 1 |

## github_sync

- status: PASS
- started_at: 2026-04-24T18:30:00Z
- ended_at: 2026-04-24T18:30:01Z

### Details

```json
{
  "root": "C:\\Users\\andre\\Desktop\\EURO MAIN",
  "git_pull": false,
  "branch": "main",
  "commit": "0612f31b2e5b2fb22ad75a179ca1e9c88035b5f8",
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
- started_at: 2026-04-24T18:30:01Z
- ended_at: 2026-04-24T18:30:01Z

### Details

```json
{
  "total_files": 66,
  "valid_files": 47,
  "invalid_files": 19,
  "warning_count": 0,
  "error_count": 25,
  "by_schema": {
    "daily_journal": {
      "total": 12,
      "valid": 12,
      "invalid": 0
    },
    "paper_trade": {
      "total": 4,
      "valid": 3,
      "invalid": 1
    },
    "scorecard": {
      "total": 18,
      "valid": 18,
      "invalid": 0
    },
    "asian_scan_report": {
      "total": 4,
      "valid": 4,
      "invalid": 0
    },
    "unknown": {
      "total": 18,
      "valid": 0,
      "invalid": 18
    },
    "breakout_scan_report": {
      "total": 1,
      "valid": 1,
      "invalid": 0
    },
    "learning_report": {
      "total": 3,
      "valid": 3,
      "invalid": 0
    },
    "scout_report": {
      "total": 4,
      "valid": 4,
      "invalid": 0
    },
    "trade_monitor_report": {
      "total": 2,
      "valid": 2,
      "invalid": 0
    }
  }
}
```

### Artifacts

- `C:\Users\andre\Desktop\EURO MAIN\08_DADOS_E_JOURNAL\SCORECARDS\SCHEMA_VALIDATION_REPORT_2026-04-24.md`
