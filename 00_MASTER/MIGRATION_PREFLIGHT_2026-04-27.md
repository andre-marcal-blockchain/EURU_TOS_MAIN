---
schema_type: migration_preflight_report
schema_version: 1.0
document_status: B0A_PREFLIGHT_OUTPUT
created_at: 2026-04-27 13:31:02 +02:00
author: Codex (OpenAI)
operator_approval_required_for_next_phase: true
---

# MIGRATION PREFLIGHT 2026-04-27

## Verdict

**B0a artifacts produced.** Backups are validated and checkpoint artifacts exist. Proceed to Phase B only after operator review of warnings and the delta inventory.

## Canonical Artifact Paths

- B0 artifacts root: $artifactRoot
- Scheduled task XML exports: $tasksDir
- PowerShell profile backups: $profilesDir
- Inventory files: $inventoryDir
- Preflight report: $preflightPath
- Migration manifest placeholder for Phase B: $manifestPath

## Backup Validation

| Backup | SHA256 |
|---|---|
| `C:\Users\andre\Desktop\BACKUP_EURO_MAIN_2026-04-27_0934.zip` | `1216223F5434ED19EDCA7A9FD1A953475A5FC8E36E138274BAE6C61A82D39A99` |
| `C:\Users\andre\Desktop\BACKUP_EURU_TOS_MAIN_2026-04-27_0936.zip` | `115D749B6303661E5B859D89C377598A03EDA34C7364A65A4531D34EF2C09EBA` |

Previous stream-read integrity check: GREEN for both backups, 0 read errors.

## Git Checkpoints

| Repo | HEAD | Tag | Result |
|---|---:|---|---|
| `C:\Users\andre\Desktop\EURO MAIN` | `aaf5ec9` | `pre-migration-2026-04-27-euro-main` | CREATED |
| `C:\Users\andre\Desktop\EURU TOS MAIN` | `d3c40c4` | `pre-migration-2026-04-27-euru-tos-main` | CREATED |

## Git Status

| Repo | Branch | HEAD | Status |
|---|---|---:|---|
| `C:\Users\andre\Desktop\EURO MAIN` | `main` | `aaf5ec9` | ` ? Euru_TOSOld_02026-04-10 /  ? Euru_TOS_GITHUB` |
| `C:\Users\andre\Desktop\EURU TOS MAIN` | `main` | `d3c40c4` | `` |

## Scheduled Tasks Snapshot

| Task | State | StartWhenAvailable | WakeToRun | NextRunTime | LastResult | MissedRuns |
|---|---|---:|---:|---|---:|---:|
| Euru_Morning_Scan | Disabled | True | False | 04/28/2026 07:00:00 | 0 | 2 |
| Euru_Asian_Scan | Disabled | True | False | 04/28/2026 02:00:00 | 0 | 2 |
| Euru_Journal_Auditor | Ready | True | False | 04/28/2026 07:30:00 | 0 | 0 |
| Euru_Smoke_Test_Night | Ready | True | True | 04/27/2026 18:21:16 | 1 | 0 |
| Euru_GitHub_Sync | Disabled | True | False | 04/27/2026 20:00:00 | 1 | 2 |
| Euru_Friday_Cycle | Disabled | True | False | 05/01/2026 20:30:00 | 1 | 0 |
| EuruLearningEngine | Disabled | True | False | 05/01/2026 20:30:00 | 2 | 0 |
| Euru_Daily_Audit | Ready | True | False | 04/28/2026 08:30:00 | 0 | 0 |
| Euru_Weekly_Audit | Ready | True | False | 05/02/2026 09:00:00 | 0 | 0 |

Task XML files were exported before migration. Rollback R4 should use:

$tasksDir

Important: rollback verification should preserve the original states shown above. It should not require every task to be Ready because several tasks are intentionally Disabled at preflight.

## PowerShell Profile Backups

| Source | Exists | Backup | SHA256 |
|---|---:|---|---|
| `C:\Users\andre\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1` | True | `C:\Users\andre\Desktop\EURU_MIGRATION_B0_2026-04-27\powershell_profiles\WindowsPowerShell_profile.ps1` | `857B1A744352E3FF5DC7FAAA88EE66B9019E1090513F20318E3697C7E6448643` |
| `C:\Users\andre\Documents\PowerShell\Microsoft.PowerShell_profile.ps1` | False | `` | `` |

## Delta Inventory Summary

| Category | Count |
|---|---:|
| EURO MAIN inventory files | 2423 |
| EURU TOS MAIN inventory files | 337 |
| Source-only files | 2123 |
| Destination-only files | 37 |
| Same relative path, different size | 38 |

Detailed CSV: $deltaPath

### Source-only Sample

- `__pycache__\euru_breakout_scanner.cpython-314.pyc` (45395 bytes)
- `__pycache__\euru_flow_analyst.cpython-314.pyc` (29571 bytes)
- `__pycache__\euru_learning_engine.cpython-312.pyc` (50659 bytes)
- `__pycache__\euru_learning_preflight.cpython-312.pyc` (10256 bytes)
- `__pycache__\euru_schema_validator.cpython-312.pyc` (30884 bytes)
- `__pycache__\euru_score_engine.cpython-314.pyc` (29038 bytes)
- `_EURU_TOS_MAIN_BUILD\.gitignore` (68 bytes)
- `_EURU_TOS_MAIN_BUILD\00_GOVERNANCA\EURU_HANDOFF_FILE_INDEX.md` (2033 bytes)
- `_EURU_TOS_MAIN_BUILD\00_GOVERNANCA\PIPELINES\EURU_FRIDAY_CYCLE.md` (8619 bytes)
- `_EURU_TOS_MAIN_BUILD\00_GOVERNANCA\SCHEMAS\EURU_SCHEMA_GOVERNANCE_THRESHOLDS.md` (9374 bytes)
- `_EURU_TOS_MAIN_BUILD\00_GOVERNANCA\SCHEMAS\EURU_SCHEMA_LEARNING_REPORT_AND_SCORECARD.md` (10325 bytes)
- `_EURU_TOS_MAIN_BUILD\00_GOVERNANCA\SCHEMAS\EURU_SCHEMA_TRADE_AND_JOURNAL.md` (10324 bytes)
- `_EURU_TOS_MAIN_BUILD\00_GOVERNANCA\SCHEMAS\EURU_SETUP_TREND_CONTINUATION_OFFICIAL_v1.0.md` (5838 bytes)
- `_EURU_TOS_MAIN_BUILD\00_GOVERNANCA\THRESHOLDS\CHANGELOGS\THRESHOLDS_CHANGELOG_system_default_v1.0.0_to_v1.1.0.md` (1068 bytes)
- `_EURU_TOS_MAIN_BUILD\00_GOVERNANCA\THRESHOLDS\PROFILES\THRESHOLDS_PROFILE_system_default_v1.0.0.md` (2065 bytes)
- `_EURU_TOS_MAIN_BUILD\00_GOVERNANCA\THRESHOLDS\PROFILES\THRESHOLDS_PROFILE_system_default_v1.1.0.md` (2503 bytes)
- `_EURU_TOS_MAIN_BUILD\00_MASTER\EURU_AGENT_MAP.md` (12221 bytes)
- `_EURU_TOS_MAIN_BUILD\00_MASTER\EURU_COMPLETE_SYSTEM_AUDIT_2026-04-15.md` (48447 bytes)
- `_EURU_TOS_MAIN_BUILD\00_MASTER\EURU_CONSOLIDATION_ROADMAP.md` (2264 bytes)
- `_EURU_TOS_MAIN_BUILD\00_MASTER\EURU_DOCUMENT_REGISTRY_OFFICIAL_v1.3.md` (7441 bytes)
- `_EURU_TOS_MAIN_BUILD\00_MASTER\EURU_HANDOFF_PROMPT_MASTER_REGISTRY_OTHER_IA.md` (1116 bytes)
- `_EURU_TOS_MAIN_BUILD\00_MASTER\EURU_MASTER_DOCUMENTO_OFFICIAL_v1.1.md` (6535 bytes)
- `_EURU_TOS_MAIN_BUILD\00_MASTER\EURU_MASTER_INDEX.md` (1774 bytes)
- `_EURU_TOS_MAIN_BUILD\00_MASTER\EURU_MASTER_SESSION_LOG_2026-04-25.md` (55175 bytes)
- `_EURU_TOS_MAIN_BUILD\00_MASTER\EURU_MIGRATION_MANIFEST_2026-04-25.md` (1812 bytes)

### Size-diff Sample

- `__pycache__\euru_asian_scan.cpython-314.pyc` EURO=21663 EURU=26863
- `__pycache__\euru_git_sync.cpython-314.pyc` EURO=2047 EURU=3013
- `__pycache__\euru_learning_engine.cpython-314.pyc` EURO=58124 EURU=58128
- `__pycache__\euru_learning_preflight.cpython-314.pyc` EURO=11386 EURU=11390
- `__pycache__\euru_morning_scan.cpython-314.pyc` EURO=34589 EURU=36456
- `__pycache__\euru_schema_validator.cpython-314.pyc` EURO=37575 EURU=37579
- `__pycache__\euru_trade_monitor.cpython-314.pyc` EURO=26447 EURU=26499
- `.gitignore` EURO=417 EURU=68
- `01_GOVERNANCA\DECISOES_ESTRATEGICAS_REVISADO.md` EURO=26404 EURU=32100
- `08_DADOS_E_JOURNAL\JOURNAL_TRADES\PAPER_TRADE_004.md` EURO=20683 EURU=21669
- `08_DADOS_E_JOURNAL\SCORECARDS\ASIAN_REPORT_2026-04-18.md` EURO=10444 EURU=10215
- `08_DADOS_E_JOURNAL\SCORECARDS\ASIAN_REPORT_2026-04-20.md` EURO=10604 EURU=10375
- `08_DADOS_E_JOURNAL\SCORECARDS\ASIAN_REPORT_2026-04-22.md` EURO=9687 EURU=9458
- `08_DADOS_E_JOURNAL\SCORECARDS\ASIAN_REPORT_2026-04-23.md` EURO=10134 EURU=9905
- `08_DADOS_E_JOURNAL\SCORECARDS\ASIAN_REPORT_2026-04-25.md` EURO=10094 EURU=9865
- `08_DADOS_E_JOURNAL\SCORECARDS\SCOUT_REPORT_2026-04-18.md` EURO=20937 EURU=20352
- `08_DADOS_E_JOURNAL\SCORECARDS\SCOUT_REPORT_2026-04-19.md` EURO=21333 EURU=20746
- `08_DADOS_E_JOURNAL\SCORECARDS\SCOUT_REPORT_2026-04-20.md` EURO=20821 EURU=20260
- `08_DADOS_E_JOURNAL\SCORECARDS\SCOUT_REPORT_2026-04-21.md` EURO=21923 EURU=21331
- `08_DADOS_E_JOURNAL\SCORECARDS\SCOUT_REPORT_2026-04-22.md` EURO=21543 EURU=20955
- `08_DADOS_E_JOURNAL\SCORECARDS\SCOUT_REPORT_2026-04-23.md` EURO=21125 EURU=20550
- `08_DADOS_E_JOURNAL\SCORECARDS\SCOUT_REPORT_2026-04-24.md` EURO=20874 EURU=20313
- `08_DADOS_E_JOURNAL\SCORECARDS\SCOUT_REPORT_2026-04-25.md` EURO=21163 EURU=20587
- `08_DADOS_E_JOURNAL\SCORECARDS\TRADE_MONITOR_REPORT_2026-04-18.md` EURO=131 EURU=186
- `08_DADOS_E_JOURNAL\SCORECARDS\TRADE_MONITOR_REPORT_2026-04-19.md` EURO=131 EURU=186

## Scheduler C1 Technical Notes

- StartWhenAvailable is already True for the inspected tasks.
- Euru_Morning_Scan and Euru_Asian_Scan are currently Disabled, have WakeToRun=False, and show missed runs.
- C1 should diagnose before applying settings, preserve existing trigger cadence, preserve MultipleInstances=IgnoreNew, and avoid promising catch-up when the machine is fully powered off.
- If the operational decision is that Morning/Asian scans must run automatically, Phase C/C1 must explicitly enable them after migration and document that state change.

## Warnings / Review Items

- EURO MAIN has non-clean git status; review untracked/modified entries before Phase B.
- Disabled tasks at preflight: Euru_Morning_Scan, Euru_Asian_Scan, Euru_GitHub_Sync, Euru_Friday_Cycle, EuruLearningEngine

## B0a Status

- Backup hashes recorded: GREEN
- Scheduled task XML export: GREEN
- PowerShell profile backup: GREEN for existing profiles
- Git checkpoint tags: GREEN
- Delta inventory: GENERATED
- Running Euru tasks at preflight: 0

**Recommendation:** B0a is technically ready for operator review. Do not proceed to Phase B until the operator confirms the warnings and approves the migration manifest discipline.
