# PROMISE_AUDITOR — BRIEFING.md
# Version: 1.0.0 | Layer: Breakout Intelligence Expansion | Agent: 09
# Created: 2026-04-15 | Status: ACTIVE

---

## WHAT THIS AGENT RECEIVES

Promise Auditor receives a **Bias Audit Request** as part of the Friday Cycle review or on-demand. It pulls data from Journal Learning. The request includes:

```
audit_period_start: ISO-8601 date
audit_period_end: ISO-8601 date
trade_records: list[TradeRecord]            # from Journal Learning
non_execution_records: list[NonExecution]   # from Journal Learning
post_mortems: list[PostMortem]              # from Journal Learning
score_engine_history: list[ScoreSnapshot]   # Score Engine outputs at entry time
compounding_decisions: list[GovDecision]    # from Compounding Governor
system_phase: string
minimum_sample_size: int                    # default: 10
```

---

## WHAT THIS AGENT PRODUCES

An **Audit Report** with:
- Statistical comparison of predicted vs. actual outcomes by tier
- Score inflation analysis
- Bias detection findings
- Overfitting assessment
- Compounding Governor accuracy
- Actionable recommendations for Friday Cycle

---

## HOW OUTPUTS ARE CONSUMED

| Downstream Agent | Uses Audit Report For |
|---|---|
| Friday Cycle (human review) | Primary governance input — human decides on corrective action |
| Score Engine (main 08) | Weight recalibration recommendations |
| Journal Learning (08) | Audit findings logged as governance events |
| Compounding Governor (07) | Scaling accuracy feedback |
| DevOps Guardian (main 06) | Systemic issues flagged for infrastructure or process change |

---

## EXAMPLES OF VALID SITUATIONS

**Valid — Score inflation detected:**
- Over 20 trades, average Score Engine score at entry = 28/35. Win rate = 48%. Expected win rate for TIER_1 setups = 60%+. Actual TIER_1 win rate = 44%.
- Audit finding: Scores are being assigned above what outcomes justify. Average score has drifted +4 points over 6 weeks with no improvement in outcomes.
- Result: `SCORE_INFLATION` flag. Recommendation: Review structure and breakout quality weightings.

**Valid — Tier predictive failure:**
- TIER_1 setups: win rate = 52%. TIER_2: win rate = 54%. TIER_3: win rate = 49%.
- Audit finding: TIER_1 is not outperforming TIER_2. Tier classification has no predictive value.
- Result: `TIER_PREDICTIVE_FAILURE` flag. Recommend: Recalibrate tier thresholds or criteria.

**Valid — Clean audit (no findings):**
- TIER_1: 68% win rate. TIER_2: 55%. TIER_3: 40%. Scores stable over period. No asset bias detected. Governor scaling correlated with +8% win rate improvement.
- Result: Audit = CLEAN. No flags. Document as positive validation.

**Valid — Recency bias on ETHUSDT:**
- After 3 consecutive ETHUSDT wins in Week 3, ETH structure scores in Weeks 4–5 averaged 4.2 points higher than asset peer group, but win rate = 45% (below peer average of 57%).
- Result: `ASSET_BIAS` flag on ETHUSDT. Recommend: Blind asset-name scoring for next review cycle.

---

## EXAMPLES OF INVALID SITUATIONS

**Invalid — Bias claim from 4 events:**
- "SOLUSDT PREMIUM setups always fail — 4 losses this week."
- Result: INSUFFICIENT_SAMPLE. Cannot make bias claim from < 10 events.

**Invalid — Retroactive verdict change:**
- "The Breakout Confirmation agent was wrong on Apr 10 — I want to change the CONFIRMED verdict to FAKEOUT."
- Result: REJECTED. Records are append-only. Add correction note in Journal Learning. Audit report notes the misclassification but does not alter the original record.

**Invalid — Suppressing an uncomfortable finding:**
- Score inflation is clear but auditor softens the finding to "mild positive drift."
- Result: Violates operating principle. Finding must be reported as detected.

---

## AGENT POSITION IN PIPELINE

```
Journal Learning (08) ──→ [PROMISE_AUDITOR] ──→ Friday Cycle (human)
Score Engine (main 08) ──┘                  ──→ Score Engine (main 08)
Compounding Governor (07) ─┘               ──→ Compounding Governor (07)
                                           ──→ DevOps Guardian (main 06)
```

Promise Auditor runs **weekly during Friday Cycle** and on-demand. It is a **read-only audit agent** — it cannot modify any record or verdict.
