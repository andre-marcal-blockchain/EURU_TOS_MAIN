# BREAKOUT_LEARNING_LOOP.md
# Version: 1.0.0 | Layer: BREAKOUT_LAYER | Module: 08_LEARNING
# Created: 2026-04-15 | Status: ACTIVE

---

## PURPOSE

This document defines the learning loop for the Euru Breakout Intelligence Layer — what data is fed in, what structured learning outputs are produced, how outputs are segmented (by score band, regime, session, and BTC alignment), and how the Friday Cycle integrates these outputs into governance decisions.

The learning loop is the mechanism by which Euru converts trade history into actionable knowledge. Without it, the system repeats the same mistakes indefinitely.

---

## LEARNING LOOP OVERVIEW

```
[Pipeline Events] ──→ Journal Learning (08) ──→ Learning Engine
                                            ──→ Score Band Analysis
                                            ──→ Regime Performance Analysis
                                            ──→ Session Performance Analysis
                                            ──→ BTC Alignment Analysis
                                            ──→ Friday Cycle Package
                                                       ↓
                                               [Human Review]
                                                       ↓
                                         Score Engine weight adjustment
                                         Classification band calibration
                                         Compounding Governor re-calibration
                                         Promise Auditor flag resolution
```

---

## INPUTS TO THE LEARNING LOOP

The following event types feed the learning loop. All are stored by Journal Learning (`08_JOURNAL_LEARNING`).

### Primary Inputs (per-event)

| Input Type | Source | Required Fields |
|---|---|---|
| TRADE_ENTRY | Tactical Execution | All 30+ feature fields, all agent verdicts, session, regime |
| TRADE_EXIT | Trade close event | r_achieved, outcome, exit_type, exit_price |
| NON_EXECUTION | Any blocking agent | reason_code, blocking_agent, session, regime |
| ALERT_RECEIVED | Alert Radar | alert_status, asset, timeframe |
| SCALING_DECISION | Compounding Governor | verdict, previous/new factor, performance_snapshot |

### Derived Inputs (computed on exit)

| Derived Field | Computation |
|---|---|
| `r_delta` | Planned R at T1 minus actual R achieved |
| `process_followed` | Boolean: did execution match the plan? |
| `outcome_vs_expectation` | WIN/LOSS relative to score band expectation |
| `post_mortem_tags` | Learning tags assigned during post-mortem review |

---

## WEEKLY LEARNING OUTPUTS

The learning loop produces four structured output families every Friday Cycle. Each must be computed and reviewed.

---

### OUTPUT FAMILY 1 — SCORE BAND PERFORMANCE

**Segment:** `breakout_final_score` classification band (DISCARD / WATCH / VALID / STRONG / PREMIUM)

**Computed metrics per band:**
```
count               : int     — number of closed trades in this band
win_rate_pct        : float   — % of trades that were profitable
avg_r_achieved      : float   — mean R multiple across all trades in band
avg_r_winners       : float   — mean R on winning trades only
avg_r_losers        : float   — mean R on losing trades only (negative)
expectancy          : float   — (win_rate × avg_r_winners) + (loss_rate × avg_r_losers)
median_score        : float   — median breakout_final_score within band
score_range         : tuple   — min and max score observed in band this period
premium_flag_accuracy : float — only for PREMIUM band: % of time PREMIUM outperformed STRONG
```

**Required analysis:**
- Does band ordering hold? (PREMIUM > STRONG > VALID expectancy)
- Is any band showing negative expectancy? → mandatory Promise Auditor flag
- Are score distributions shifting within bands? (e.g., STRONG band average score declining from 78 to 72 may indicate drift)

**Friday Cycle action:** Human reviews band table and confirms whether band thresholds remain appropriate. Changes require Type 3 governance approval.

---

### OUTPUT FAMILY 2 — REGIME PERFORMANCE

**Segment:** `regime_at_entry` from Market Regime output

**Regime segments:**
- `TREND_BULL`
- `TREND_BEAR`
- `CHOPPY`
- `SIDEWAYS_RANGE`
- `SIDEWAYS_COMPRESSION`
- `REGIME_TRANSITION`

**Computed metrics per regime:**
```
count               : int
win_rate_pct        : float
avg_r_achieved      : float
expectancy          : float
fakeout_rate_pct    : float   — NON_EXECUTIONS tagged FAKEOUT / total routed in this regime
breakout_quality_avg : float  — average breakout_quality_score for events in this regime
avg_final_score     : float
```

**Required analysis:**
- Which regime produces the highest expectancy? Should routing be restricted during low-expectancy regimes?
- Does CHOPPY regime consistently underperform? (Expected: yes — architecture assumes this)
- Does SIDEWAYS_COMPRESSION regime predict good breakout setups? (Expected: yes — compression precedes expansion)
- Does fakeout rate correlate with regime? (Expected: CHOPPY has highest fakeout rate)

**Learning action:** If a regime consistently shows negative expectancy across ≥ 15 events, the Score Engine's context score should be reviewed to ensure regime is penalized sufficiently in that segment.

---

### OUTPUT FAMILY 3 — SESSION PERFORMANCE

**Segment:** `session_tag` (MORNING / ASIAN / OVERLAP / MANUAL)

**Computed metrics per session:**
```
count               : int
win_rate_pct        : float
avg_r_achieved      : float
expectancy          : float
avg_breakout_quality_score : float
avg_final_score     : float
volume_ratio_avg    : float   — average volume_ratio in this session
fakeout_rate_pct    : float
```

**Required analysis:**
- Does the MORNING session outperform ASIAN? (Expected: MORNING has stronger institutional volume)
- Are ASIAN session setups characterized by lower volume ratios? (Expected: yes — thinner market)
- Does OVERLAP session (London/NY) produce highest quality breakouts? (Expected: yes — peak liquidity)
- Are MANUAL session trades (outside scheduled windows) performing differently? Flag if > 20% of trade volume.

**Learning action:** If ASIAN session consistently shows lower expectancy, the `session_tag` weight in the context score may need recalibration. Alternatively, ASIAN session-specific classification band thresholds may be warranted.

---

### OUTPUT FAMILY 4 — BTC ALIGNMENT PERFORMANCE

**Segment:** `btc_alignment_score` bucketed into ranges

**BTC alignment buckets:**
```
high_alignment      : btc_alignment_score 0.80–1.0
moderate_alignment  : btc_alignment_score 0.50–0.79
low_alignment       : btc_alignment_score 0.20–0.49
opposed             : btc_alignment_score 0.00–0.19
```

**Computed metrics per bucket:**
```
count               : int     — altcoin trades only (BTC self excluded)
win_rate_pct        : float
avg_r_achieved      : float
expectancy          : float
fakeout_rate_pct    : float
```

**Required analysis:**
- Does high BTC alignment significantly outperform low alignment? (Expected: yes — this is a design assumption)
- If the `opposed` bucket shows positive expectancy across ≥ 10 events, the BTC filter logic should be revisited
- Does the altcoin_modifier penalty (applied at btc_alignment_score < 0.5) produce the expected effect on final scores?

**Learning action:** BTC alignment is a hard filter and a soft weight. If the data shows that `low_alignment` altcoin setups are profitable, the architecture assumption should be reviewed through the governance process (Type 2 minimum).

---

## FRIDAY CYCLE INTEGRATION REQUIREMENTS

The Friday Cycle (`07_OPERACAO/SOP_SEMANAL.txt`) must integrate the following learning outputs as mandatory agenda items:

### Mandatory Friday Cycle Agenda Items

1. **Trade Summary Review**
   - Total trades, wins, losses, overall win rate, avg R, total expectancy
   - Comparison to prior 4 weeks

2. **Score Band Performance Table**
   - All four families reviewed
   - Any negative expectancy band must be addressed before cycle closes

3. **Regime Performance Review**
   - Identify the top-performing and worst-performing regimes this week
   - Flag if CHOPPY regime was not penalized (setups in CHOPPY executed = process violation)

4. **Session Distribution Check**
   - Confirm trade distribution across sessions is intentional
   - Flag if MANUAL session trades exceed 20% of weekly volume

5. **BTC Alignment Check**
   - Review altcoin performance segmented by BTC alignment bucket
   - Confirm altcoin_modifier is functioning as intended

6. **Promise Auditor Report Review**
   - All findings reviewed (see `BREAKOUT_AUDIT_RULES.md`)
   - Any HIGH or CRITICAL finding requires a documented response before cycle closes

7. **Compounding Governor Status**
   - Review current scaling factor and freeze state
   - Review scaling decisions made this week and their performance context

8. **Open Governance Items**
   - Any unresolved findings from prior Friday Cycles
   - Any pending Type 2 or Type 3 change proposals

### Friday Cycle Outputs (required before cycle closes)

```
weekly_summary_confirmed  : bool    — human confirms Journal Learning summary is accurate
band_table_reviewed       : bool    — human confirms score band performance reviewed
promise_auditor_response  : string  — ACCEPTED | DISPUTED | DEFERRED for each HIGH/CRITICAL finding
decisions_logged          : bool    — any governance decisions logged in DECISOES_ESTRATEGICAS_REVISADO.md
compounding_posture_set   : bool    — Compounding Governor posture confirmed for next week
```

---

## LEARNING ENGINE FEED

The Learning Engine (standalone module, outside BREAKOUT_LAYER scope) receives a structured data feed from Journal Learning weekly. The feed includes:

```yaml
learning_engine_feed:
  period: string               # ISO-8601 date range
  feature_performance:
    - feature: string          # e.g., "zone_touch_count"
      correlation_to_win: float  # Pearson correlation, all trades in period
      percentile_winners: float  # avg feature value in winning trades
      percentile_losers: float   # avg feature value in losing trades
      signal_strength: string    # STRONG | MODERATE | WEAK | NOISE

  top_predictive_features: list[string]   # top 5 features by correlation to win
  weakest_features: list[string]           # bottom 3 features — candidates for weight reduction

  regime_edge_ranking: list[string]        # regimes ranked by expectancy (best → worst)
  session_edge_ranking: list[string]       # sessions ranked by expectancy
  btc_alignment_validation: bool           # does high alignment predict better outcomes?
```

The Learning Engine uses this feed to propose weight adjustments, which are then reviewed through the governance process before any change to `breakout_weights_v1.yaml`.

---

## MINIMUM SAMPLE REQUIREMENTS FOR LEARNING CLAIMS

| Claim Type | Minimum Events |
|---|---|
| Feature correlation claim | 20 trades |
| Score band validity claim | 10 trades per band |
| Regime performance claim | 10 trades per regime |
| Session performance claim | 5 trades per session |
| BTC alignment claim | 10 trades per bucket |
| Pattern identification | 5 events |
| Weight adjustment proposal | 30 trades in affected segment |

Claims with insufficient data are logged but not acted upon. They remain in the evidence base for the next cycle when more data is available.
