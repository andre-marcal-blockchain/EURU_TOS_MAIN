# 05_EXECUTION ORCHESTRATOR — Output Format Revisado (versão definitiva)

## Standard Output

AGENT: Execution Orchestrator
SYMBOL: [ex: NEARUSDT]
DATE: [YYYY-MM-DD HH:MM UTC]
CONFIDENCE: [0-10]

STRUCTURAL_STATE:  [NO_TRADE | WATCHLIST | SETUP]
FLOW_STATE:        [CONTRADICTS | INCONCLUSIVE | CONFIRMS]
NEWS_SEVERITY:     [INFO | NEUTRA | MEDIA_SEVERIDADE | ALTA_SEVERIDADE | SEM_NOVIDADE]
RISK_STATE:        [APPROVE | REJECT | REVIEW]
PLAYBOOK_STATE:    [PLAYBOOK_OK | PLAYBOOK_REJECT | REVIEW]
SCORE:             [0-10]
SCORE_CLASS:       [Baixo | Médio | Alto | Muito Alto]

CONFLICTS_DETECTED: [YES | NO]
CONFLICT_DETAILS:   [descrição se YES | none]
CONFLICT_RESOLUTION:[como foi resolvido]

EXECUTION_STATE: [EXECUTION_ALLOWED | EXECUTION_BLOCKED | MANUAL_REVIEW_REQUIRED]

EXIT_RULES:
  ENTRY:       [preço | N/A]
  STOP_LOSS:   [preço]
  TARGET_1:    [preço — 1:2]
  TARGET_2:    [preço — 1:3]
  TRAILING:    [regra ou N/A]
  TIME_STOP:   [dias ou N/A]
  50_SECURING: [nível de ROI]

RATIONALE: [explicação concisa citando cada agente e justificando a decisão]
NEXT_AGENT: [Journal/Auditor]

## Rules
- Do not alter field names; use official state nomenclature only.
- RATIONALE must mention each agent input — do not hide conflicting information.
- EXIT_RULES must be populated when EXECUTION_ALLOWED; N/A allowed for fields not applicable.
- CONFIDENCE: 0-3 major conflicts unresolved | 4-6 partial conflicts | 7-8 minor conflicts resolved | 9-10 full alignment.

## Example

AGENT: Execution Orchestrator
SYMBOL: NEARUSDT
DATE: 2026-04-05 07:00 UTC
CONFIDENCE: 6

STRUCTURAL_STATE:  WATCHLIST
FLOW_STATE:        INCONCLUSIVE
NEWS_SEVERITY:     ALTA_SEVERIDADE
RISK_STATE:        APPROVE
PLAYBOOK_STATE:    REVIEW
SCORE:             5.5
SCORE_CLASS:       Médio

CONFLICTS_DETECTED: YES
CONFLICT_DETAILS:   Score 5.5 below threshold 7.0. HIGH severity news. BTC filter active.
CONFLICT_RESOLUTION: Per hierarchy — News Sentinel elevated concern + score below threshold block execution.

EXECUTION_STATE: EXECUTION_BLOCKED

EXIT_RULES:
  ENTRY:       N/A
  STOP_LOSS:   1.1512 (defined for reference)
  TARGET_1:    1.4720
  TARGET_2:    1.5828
  TRAILING:    N/A
  TIME_STOP:   7 days
  50_SECURING: 50% ROI

RATIONALE: Scout WATCHLIST (BTC filter active). Flow INCONCLUSIVE (OBV strong but MACD lagging). News ALTA_SEVERIDADE blocks execution. Quant APPROVE but score 5.5 below 7.0 threshold. PLAYBOOK REVIEW due to incomplete exit rules. Revisit when BTC confirms direction and news normalises.
NEXT_AGENT: Journal/Auditor
