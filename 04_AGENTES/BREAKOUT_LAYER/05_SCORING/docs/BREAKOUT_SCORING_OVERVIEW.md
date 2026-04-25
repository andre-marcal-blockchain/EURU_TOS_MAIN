# BREAKOUT_SCORING_OVERVIEW.md
# Version: 1.0.0 | Layer: BREAKOUT_LAYER | Module: 05_SCORING/docs
# Created: 2026-04-15 | Status: ACTIVE

---

## PURPOSE

This document explains the Euru Breakout Scoring System — what it measures, why it is structured in four score families, how scores map to classification bands, and which downstream agents consume each score type.

Reference files:
- Schema: `05_SCORING/schemas/euru_breakout_feature_schema.yaml`
- Weights: `05_SCORING/configs/breakout_weights_v1.yaml`

---

## THE FOUR SCORE FAMILIES

The Euru Breakout Score Engine computes four distinct scores for every breakout event. Each score family answers a different question. Together they produce the `breakout_final_score` that drives classification.

---

### FAMILY 1 — `breakout_raw_score` (0–100)

**Question answered:** *Is the breakout signal itself high quality?*

**Feature groups:**
- `structure_features` (25%) — zone maturity, touches, compression, failed breaks
- `breakout_candle_features` (30%) — body size, wick, close position, volume
- `impulse_features` (20%) — distance beyond zone, speed, momentum alignment
- `volume_features` (25%) — volume trend, OBV, breakout volume ratio

**Intent:** The raw score evaluates the mechanical quality of the breakout event — the zone that was broken, the candle that broke it, and the momentum and volume behind the move. A high raw score means the signal looks convincing on paper. It does not mean the setup is contextually appropriate or tradeable.

**Example of a high raw score, low final score:** Perfect candle on a PREMIUM zone during a BTC CHOPPY regime with a 1.4:1 R:R due to overhead resistance. Raw = 88, Context = 31, Tradeability = 22 → Final = 51 (WATCH).

---

### FAMILY 2 — `breakout_context_score` (0–100)

**Question answered:** *Is the environment favorable for follow-through?*

**Feature groups:**
- `post_break_features` (35%) — retest quality, bars above zone, close acceptance
- `multi_timeframe_features` (65%) — HTF trend, HTF structure, BTC alignment, session

**Intent:** The context score measures whether the breakout is happening in an environment that supports continuation. A breakout during a BTC SIDEWAYS regime, in the ASIAN session, with no post-break acceptance, scores poorly here even if the raw signal is excellent. The HTF features are weighted more heavily (65%) because they are knowable before the breakout candle closes and are the dominant environmental factor.

**Key design note:** BTC alignment score carries 35% of the multi_timeframe_features group weight. For altcoin setups, BTC alignment is the single most important environmental variable.

---

### FAMILY 3 — `breakout_tradeability_score` (0–100)

**Question answered:** *Can this setup actually be executed safely and profitably?*

**Feature groups:**
- `tradeability_features` — stop distance, target distance, R:R, resistance proximity, liquidity, spread, slippage, liquidation distance

**Intent:** The tradeability score measures execution feasibility. A setup can score 90 on raw quality and 85 on context, but if the stop must be placed inside a noisy region (< 1x ATR), there is no room to T1 before major resistance, and the spread consumes 40% of the expected edge — the setup cannot be traded well.

**Critical design principle:** A STRONG or PREMIUM raw score does not imply tradeability. Tradeability is an independent evaluation. It has equal weight to context in the final blend (30% each) precisely to prevent inflated final scores for mechanically unviable setups.

**Hard disqualifiers in tradeability:**
- R:R < 2.0 → DISCARD regardless of other scores
- Liquidation distance < 2x ATR → DISCARD regardless of other scores

---

### FAMILY 4 — `breakout_final_score` (0–100)

**Question answered:** *What is the overall quality of this opportunity?*

**Blend:**
- Raw: 40%
- Context: 30%
- Tradeability: 30%

**Intent:** The final score is the primary routing signal. It determines which classification band the event falls into and what pipeline action is taken. The 40/30/30 split reflects the view that signal quality is the largest factor, but a strong signal in a bad environment with no execution feasibility is worthless.

---

## CLASSIFICATION BANDS

| Band | Score Range | Label | Pipeline Action |
|---|---|---|---|
| Discard | 0–39 | `DISCARD` | Do not route. Log only. |
| Watch | 40–54 | `WATCH` | Watchlist only. No execution. |
| Valid | 55–69 | `VALID` | Route to Risk Guardian, standard parameters. |
| Strong | 70–84 | `STRONG` | Route with STRONG flag, eligible for scaled entry. |
| Premium | 85–100 | `PREMIUM` | Route with PREMIUM flag, maximum approved risk eligible. |

**Important:** Classification bands are not static. The Promise Auditor audits whether each band's actual win rate and expectancy justify its label. A PREMIUM band with negative expectancy triggers mandatory governance review.

---

## DESIGN RULE: STRONG RAW DOES NOT MEAN TRADEABLE

This is the most important architectural principle of the scoring system.

A breakout can score 95 on raw quality (perfect zone, perfect candle, volume = 2.8x, momentum aligned) and still be classified DISCARD or WATCH if:
- BTC is in a SIDEWAYS or BEARISH regime (devastates context_score)
- There is major resistance 0.4x ATR above entry (destroys R:R and tradeability)
- The spread is 0.4% (consumes edge)
- The session is ASIAN with no institutional participation

The final score weighting (40/30/30) is designed so that a raw_score of 95 with context_score of 20 and tradeability_score of 15 produces:

```
Final = (95 × 0.40) + (20 × 0.30) + (15 × 0.30)
      = 38.0 + 6.0 + 4.5
      = 48.5 → WATCH
```

This is intentional. The system must not be fooled by beautiful candles in the wrong environment.

---

## DOWNSTREAM CONSUMERS

| Agent | Score Used | Purpose |
|---|---|---|
| **Risk Guardian** (01) | `breakout_final_score` + band | Classification determines routing priority. PREMIUM setups receive maximum approved risk allocation. VALID setups receive standard. |
| **Tactical Execution** (06) | `breakout_tradeability_score` + individual tradeability features | Stop placement, target selection, entry type, and warning_flags are calibrated using raw tradeability feature values (not just the score). |
| **Compounding Governor** (07) | `breakout_final_score` + band at entry | Performance is tracked by classification band — Governor evaluates whether PREMIUM setups outperform STRONG, etc. |
| **Journal Learning** (08) | Full feature row + all four scores | Every trade record stores the complete feature snapshot at time of entry. Score values at entry are immutable once stored. |
| **Friday Cycle** (human) | `breakout_final_score` distribution, band win rates | Human governance reviews whether band performance matches design expectations. |
| **Promise Auditor** (09) | All four scores + outcomes | Audits score inflation, band predictive validity, negative expectancy, and PREMIUM classification integrity. Primary consumer for score integrity. |

---

## GOVERNANCE NOTES

- Weight changes require **Type 2 governance approval** (24h wait + separate session sign-off).
- Band threshold changes require **Type 3 governance approval** (48h wait + formal checklist).
- The `conservative_v1` weight profile is the only active profile. New profiles must be created as new YAML files, not by overwriting this one.
- Promise Auditor will flag `PREMIUM_PERFORMANCE_UNSUPPORTED` if the PREMIUM band fails to outperform the STRONG band over any 20-trade window.
- Feature schema changes (adding or removing features) require a full scoring system re-validation cycle before going live.
