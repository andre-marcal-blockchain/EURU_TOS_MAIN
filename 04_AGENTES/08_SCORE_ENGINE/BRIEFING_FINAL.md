# 08_SCORE ENGINE — Briefing Revisado (versão definitiva)

## Purpose
Transform qualitative assessments from all agents into a single quantitative score (0-10) that represents the attractiveness of a potential trade. This score serves as the primary reference for the Execution Orchestrator's go/no-go decision.

## Role in pipeline
The Score Engine is the synthesis layer. It receives outputs from five agents and produces one number. A score >= 7 is required for EXECUTION_ALLOWED — but a high score alone does not override a REJECT from Quant/Risk Officer or PLAYBOOK_REJECT from MAC Analyst.

Scout + Flow + News + Quant/Risk + MAC Analyst → Score Engine → Execution Orchestrator

## Scoring methodology

Five components with standard weights:

Structure — Scout — 25% — NO_TRADE=0, WATCHLIST=5, SETUP=8
Indicators — Flow Analyst — 25% — CONTRADICTS=0, INCONCLUSIVE=3, CONFIRMS=7
News — News Sentinel — 20% — ALTA_SEV=-3, NEUTRA=3, MEDIA_SEV=5, INFO=1, SEM_NOV=0
Risk — Quant/Risk — 20% — REJECT=0, REVIEW=4, APPROVE=8
Playbook — MAC Analyst — 10% — REJECT=0, REVIEW=4, OK=8

Score classifications:
- 0-3 → Baixo
- 4-6 → Médio
- 7-8 → Alto
- 9-10 → Muito Alto

## Constraints
- Use defined weights unless Risk Owner authorises a change.
- Normalise all component values to 0-10 scale before combining.
- A high score does not supersede a REJECT from Quant/Risk Officer or MAC Analyst.
- If any required input is missing → output Score inconclusivo + REVIEW.
- Record all scores in Journal for future analysis and calibration.
- Inform Execution Orchestrator and Quant/Risk Officer of the result.
