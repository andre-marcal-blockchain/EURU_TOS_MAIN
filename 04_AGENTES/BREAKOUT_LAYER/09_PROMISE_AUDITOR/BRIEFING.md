# PROMISE_AUDITOR — BRIEFING.md
# Version: 1.0.0 | Layer: BREAKOUT_LAYER | Agent: 09_PROMISE_AUDITOR
# Created: 2026-04-15 | Status: ACTIVE

---

## INPUTS

Promise Auditor receives an **Audit Request** as part of the Friday Cycle or on threshold breach. It pulls data from Journal Learning.

**Audit Request:**
```
audit_period_start      : ISO-8601 date
audit_period_end        : ISO-8601 date
trigger                 : FRIDAY_CYCLE | THRESHOLD_BREACH | MANUAL
minimum_sample_size     : int          # default: 10
system_phase            : string
```

**From Journal Learning (on request):**
```
trade_records           : list[TradeRecord]
non_execution_records   : list[NonExecutionRecord]
scorecard_feed          : ScorecardFeed    # score band performance data
weekly_summaries        : list[WeeklySummary]  # last 4 weeks minimum
compounding_decisions   : list[ScalingDecision]
```

---

## OUTPUTS

An **Audit Report** delivered to the Governance layer (Friday Cycle, human operators). See OUTPUT_FORMAT.md for full schema.

**Audit verdict values:** `CLEAN`, `FLAGS_DETECTED`, `INSUFFICIENT_DATA`

---

## VALID SITUATIONS

**Scenario A — Score inflation detected:**
- Over 4 weeks, average score at entry rose from 24.5 to 29.2 (+4.7 pts). Win rate over same period: dropped from 61% to 49%.
- Scores rising, outcomes falling → `SCORE_INFLATION` flag. Severity: HIGH.
- Recommendation: Audit breakout_quality and structure weighting. Criteria may be inflating without validation.

**Scenario B — Negative expectancy band:**
- Score band 25–29: 14 trades. Win rate 43%. Avg win R = 1.8. Avg loss R = -1.2. Expectancy = (0.43 × 1.8) − (0.57 × 1.2) = 0.774 − 0.684 = +0.09 (positive — OK).
- Score band 20–24: 11 trades. Win rate 36%. Avg win R = 1.5. Avg loss R = -1.3. Expectancy = (0.36 × 1.5) − (0.64 × 1.3) = 0.54 − 0.832 = **−0.29** (negative).
- → `NEGATIVE_EXPECTANCY_BAND` on 20–24 band. Mandatory report.

**Scenario C — Score drift over 2 weeks:**
- Week 1 expectancy: +0.42R. Week 2 expectancy: +0.31R. Week 3 expectancy: +0.18R.
- Two consecutive weeks of decline → `SCORE_DRIFT_DETECTED`. Not yet negative but trend is clear.

**Scenario D — PREMIUM classification unsupported:**
- PREMIUM setups (score ≥ 30): 12 trades, win rate 52%. STANDARD setups (score 20–29): 18 trades, win rate 56%.
- PREMIUM win rate ≤ STANDARD → `PREMIUM_PERFORMANCE_UNSUPPORTED`. Classification is not predictive.

**Scenario E — Clean audit:**
- PREMIUM win rate 68%, STANDARD 55%, score band 30–35 has positive expectancy +0.72R, no drift detected, no inflation.
- → `CLEAN`. Document as validation. No flags.

---

## INVALID SITUATIONS

**Statistical claim from 6 trades:**
- "Wedge formations always fail — we lost 6 in a row."
- Invalid. Minimum 10 events for any statistical claim. Log events, do not surface as finding.

**Retroactive record modification:**
- Governance requests that poor-performing trades be re-classified to remove them from PREMIUM sample.
- Invalid. Records are append-only. Audit findings reference records as-is. Add governance note, never alter.

**Suppressing a negative expectancy finding:**
- A score band shows negative expectancy but operator requests it be omitted because "sample is small (12 events)."
- Invalid. 12 events ≥ 10 minimum. Negative expectancy must be reported. If operator disagrees, add dissent as a governance note — finding stands.

**Claiming drift from one week:**
- Single week of expectancy decline.
- Not a `SCORE_DRIFT_DETECTED` event. Requires 2 consecutive weeks. Note the single-week decline but do not flag.

---

## NOTES

- Promise Auditor runs **weekly during Friday Cycle** and on-demand when `THRESHOLD_BREACH` is triggered.
- It is a **read-only audit agent** — it cannot modify any record, verdict, or score.
- `REPEAT_FINDING` severity escalates automatically: LOW → MEDIUM after 2 cycles, MEDIUM → HIGH after 3 cycles unresolved.
- Compounding accuracy audit requires at least 3 completed scaling events to produce a meaningful finding.
- Promise Auditor produces one report per audit cycle — not per trade.
