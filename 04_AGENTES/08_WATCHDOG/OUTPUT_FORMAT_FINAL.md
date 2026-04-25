# 08_WATCHDOG — Output Format Revisado (versão definitiva)

## Standard Output

AGENT: Watchdog
DATE: [YYYY-MM-DD HH:MM UTC]
CYCLE: [morning | asian | hourly]
CONFIDENCE: [0-10]

AGENT_HEARTBEATS:
  01_Scout:               [OK | TIMEOUT | FAILED | NO_OUTPUT]
  02_Flow_Analyst:        [OK | TIMEOUT | FAILED | NO_OUTPUT]
  03_News_Sentinel:       [OK | TIMEOUT | FAILED | NO_OUTPUT]
  04_Quant_Risk:          [OK | TIMEOUT | FAILED | NO_OUTPUT]
  05_Execution_Orch:      [OK | TIMEOUT | FAILED | NO_OUTPUT]
  06_DevOps_Guardiao:     [OK | TIMEOUT | FAILED | NO_OUTPUT]
  07_Journal_Auditor:     [OK | TIMEOUT | FAILED | NO_OUTPUT]
  08_Score_Engine:        [OK | TIMEOUT | FAILED | NO_OUTPUT]
  09_MAC_Analyst:         [OK | TIMEOUT | FAILED | NO_OUTPUT]

FAILED_AGENTS: [lista | none]
RECOVERY_ATTEMPTED: [YES | NO]
RECOVERY_ACTIONS:
  [lista de acções tomadas | none]
RECOVERY_SUCCESS: [YES | NO | PARTIAL]

BACKUP_SOURCE_ACTIVE: [YES | NO]
BACKUP_SOURCE_DETAILS: [se YES | N/A]

PIPELINE_CONTINUITY: [MAINTAINED | INTERRUPTED]
OPERATOR_ALERT_SENT: [YES | NO]
ALERT_REASON: [se YES | N/A]

WATCHDOG_STATE: [HEALTHY | DEGRADED | CRITICAL]
READ_ONLY_FORCED: [YES | NO]

## Rules
- Every agent must have a heartbeat status — never leave blank.
- RECOVERY_ACTIONS must list specific steps taken, not generic descriptions.
- WATCHDOG_STATE CRITICAL → READ_ONLY_FORCED must be YES.
- CONFIDENCE: 0-3 multiple agents failed unrecoverable | 4-6 some failures recovered | 7-8 minor failures resolved | 9-10 zero failures all agents OK.

## Example

AGENT: Watchdog
DATE: 2026-04-05 07:15 UTC
CYCLE: morning
CONFIDENCE: 9

AGENT_HEARTBEATS:
  01_Scout:           OK
  02_Flow_Analyst:    OK
  03_News_Sentinel:   OK
  04_Quant_Risk:      OK
  05_Execution_Orch:  OK
  06_DevOps_Guardiao: OK
  07_Journal_Auditor: OK
  08_Score_Engine:    OK
  09_MAC_Analyst:     OK

FAILED_AGENTS: none
RECOVERY_ATTEMPTED: NO
RECOVERY_ACTIONS: none
RECOVERY_SUCCESS: N/A

BACKUP_SOURCE_ACTIVE: NO
BACKUP_SOURCE_DETAILS: N/A

PIPELINE_CONTINUITY: MAINTAINED
OPERATOR_ALERT_SENT: NO
ALERT_REASON: N/A

WATCHDOG_STATE: HEALTHY
READ_ONLY_FORCED: NO
