# 06_DEVOPS GUARDIÃO — Output Format Revisado (versão definitiva)

## Standard Output

AGENT: DevOps Guardião
DATE: [YYYY-MM-DD HH:MM UTC]
CONFIDENCE: [0-10]

API_CONNECTIVITY: [ex: latência média 200ms, 0.2% erros | DISCONNECTED]
SYSTEM_HEALTH: [ex: CPU 60%, memória 65%, logs íntegros | DEGRADED: componente X]
FEED_LATENCY: [ex: REST 150ms, WebSocket 1s | HIGH: >500ms]
SECURITY_EVENTS: [lista de eventos | none]

SCRIPTS_STATUS:
  Morning scan (07:00): [OK | FAILED | NOT_RUN]
  Asian scan (00:00):   [OK | FAILED | NOT_RUN]

ASSETS_STATUS:
  Total requested: [n]
  Total fetched:   [n]
  Stale:           [lista | none]
  Anomalous:       [lista | none]
  Failed:          [lista | none]

INFRASTRUCTURE_STATE: [HEALTHY | DEGRADED | CRITICAL]
MITIGATION: [acções tomadas ou recomendadas | none]
INCIDENT_LOGGED: [YES | NO]
INCIDENT_ID: [ID se YES]
NOTES: [observações adicionais]

## Rules
- Keep all field names exactly as shown.
- Use only official infrastructure states: HEALTHY, DEGRADED, CRITICAL.
- MITIGATION must describe specific actions, not generic statements.
- SECURITY_EVENTS must list all detected events, even if minor.
- CONFIDENCE: 0-3 multiple failures unstable | 4-6 some failures recovered | 7-8 minor issues resolved | 9-10 all OK zero failures.

## Example

AGENT: DevOps Guardião
DATE: 2026-04-05 07:05 UTC
CONFIDENCE: 9

API_CONNECTIVITY: latência média 185ms, 0.1% erros — OK
SYSTEM_HEALTH: CPU 45%, memória 58%, logs íntegros
FEED_LATENCY: REST 160ms, CoinTelegraph RSS 320ms
SECURITY_EVENTS: none

SCRIPTS_STATUS:
  Morning scan (07:00): OK
  Asian scan (00:00):   NOT_RUN (PC offline at midnight)

ASSETS_STATUS:
  Total requested: 20
  Total fetched:   19
  Stale:           MATICUSDT (last update >10 min)
  Anomalous:       none
  Failed:          none

INFRASTRUCTURE_STATE: HEALTHY
MITIGATION: MATICUSDT excluded from report automatically by staleness check.
INCIDENT_LOGGED: NO
NOTES: Asian scan not running due to PC being offline. Cloud hosting required for 24/7 coverage in EXECUTE phase.
