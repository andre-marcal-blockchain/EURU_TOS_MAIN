# 07_JOURNAL AUDITOR — Output Format Revisado (versão definitiva)

## Daily Entry Format

AGENT: Journal Auditor
DATE: [YYYY-MM-DDTHH:MM:SS+02:00 — Europe/Madrid]
CONFIDENCE: [0-10]

AGENT_OUTPUTS:
  SYMBOL:           [ex: NEARUSDT]
  STRUCTURAL_STATE: [NO_TRADE | WATCHLIST | SETUP]
  FLOW_STATE:       [CONTRADICTS | INCONCLUSIVE | CONFIRMS]
  NEWS_SEVERITY:    [INFO | NEUTRA | MEDIA_SEVERIDADE | ALTA_SEVERIDADE]
  RISK_STATE:       [APPROVE | REJECT | REVIEW]
  PLAYBOOK_STATE:   [PLAYBOOK_OK | PLAYBOOK_REJECT | REVIEW]
  SCORE:            [0-10]
  EXECUTION_STATE:  [EXECUTION_ALLOWED | EXECUTION_BLOCKED | MANUAL_REVIEW_REQUIRED]

INCIDENTS: [lista de incidentes técnicos ou de segurança | none]
TIME_STOP_TRIGGERED: [YES — symbol | NO]
COMPLIANCE: [OK | INCOMPLETE | NON_COMPLIANT]
COMPLIANCE_NOTES: [se INCOMPLETE ou NON_COMPLIANT — detalhe]

SUMMARY: [2-3 frases resumindo actividades e resultados do dia]
NOTES: [observações adicionais, pendências, comentários para o dia seguinte]

## Weekly Scorecard Format (every Friday)

WEEK: [YYYY-MM-DD] to [YYYY-MM-DD]
TOTAL_SETUPS_ANALYSED: [n]
TOTAL_TRADES_EXECUTED: [n]
WINNERS: [n] | LOSERS: [n]
WIN_RATE: [%]
GROSS_PROFIT: [USDT]
GROSS_LOSS: [USDT]
NET_RESULT: [USDT]
AVG_RISK_REWARD: [ratio]
TRADES_OFF_PLAYBOOK: [n]
TRADES_BY_FOMO: [n — should be 0]

QUALITATIVE_SCORES (0-10):
  Discipline:         [score]
  Patience:           [score]
  Structure_reading:  [score]
  Risk_respect:       [score]
  Playbook_adherence: [score]

BEST_TRADE: [descrição]
WORST_TRADE: [descrição]
CHAMPION_SETUP: [nome do setup]
MAIN_ERROR_PATTERN: [padrão identificado]
NEXT_WEEK_ADJUSTMENTS: [acções de melhoria]

## Rules
- Use INCOMPLETE for any field with missing data — never guess.
- Dates must use ISO 8601 with Europe/Madrid timezone.
- COMPLIANCE must reflect actual state — never mark OK if violations exist.
- SUMMARY must be factual and neutral — no market predictions.
- Weekly scorecard mandatory every Friday.
- CONFIDENCE: 0-3 many missing fields | 4-6 some gaps | 7-8 complete with minor notes | 9-10 fully complete no issues.
