# 08_SCORE ENGINE — Output Format Revisado (versão definitiva)

## Standard Output

AGENT: Score Engine
SYMBOL: [ex: NEARUSDT]
DATE: [YYYY-MM-DD HH:MM UTC]
CONFIDENCE: [0-10]

STRUCTURE_SCORE:  [0-10] — Scout: [STATE]
INDICATORS_SCORE: [0-10] — Flow: [FLOW_STATE]
NEWS_SCORE:       [0-10] — Sentinel: [SEVERITY]
RISK_SCORE:       [0-10] — Quant: [RISK_STATE]
PLAYBOOK_SCORE:   [0-10] — MAC: [PLAYBOOK_STATE]

WEIGHTED_SCORE:   [0-10 | INCONCLUSIVE]
CLASSIFICATION:   [Baixo | Médio | Alto | Muito Alto | REVIEW]

POSITIVE_FACTORS: [componentes que aumentaram o score]
NEGATIVE_FACTORS: [componentes que reduziram o score]
SCORE_RATIONALE:  [1-2 frases explicando o score]
EXECUTION_THRESHOLD: [ABOVE 7 — eligible | BELOW 7 — blocked]

SCORE_STATE: [ALTO_SUFICIENTE | INSUFICIENTE | Score inconclusivo]
NEXT_AGENT: [Execution Orchestrator]

## Rules
- If inputs are missing or inconsistent → WEIGHTED_SCORE: INCONCLUSIVE + CLASSIFICATION: REVIEW.
- Score does not override REJECT from Quant/Risk or PLAYBOOK_REJECT from MAC Analyst.
- SCORE_RATIONALE must reference specific components in 1-2 sentences.
- NEWS_SCORE can reduce total score (ALTA_SEVERIDADE = -3 contribution).
- CONFIDENCE: 0-3 missing inputs | 4-6 some components incomplete | 7-8 all inputs present | 9-10 full inputs and clear result.

## Example

AGENT: Score Engine
SYMBOL: NEARUSDT
DATE: 2026-04-05 07:00 UTC
CONFIDENCE: 7

STRUCTURE_SCORE:  6.0 — Scout: WATCHLIST (downgraded from SETUP)
INDICATORS_SCORE: 4.0 — Flow: INCONCLUSIVE
NEWS_SCORE:       0.0 — Sentinel: ALTA_SEVERIDADE (negative contribution)
RISK_SCORE:       8.0 — Quant: APPROVE
PLAYBOOK_SCORE:   4.0 — MAC: REVIEW

WEIGHTED_SCORE:   4.8
CLASSIFICATION:   Médio

POSITIVE_FACTORS: Quant APPROVE (8.0), OBV accumulation via Flow, RSI crossing 50
NEGATIVE_FACTORS: HIGH severity news (0.0 contribution adverse), Scout downgraded by BTC filter, MAC REVIEW
SCORE_RATIONALE: Strong risk approval and accumulation signals offset by adverse macro news and BTC filter limiting structural score.
EXECUTION_THRESHOLD: BELOW 7 — blocked

SCORE_STATE: INSUFICIENTE
NEXT_AGENT: Execution Orchestrator
