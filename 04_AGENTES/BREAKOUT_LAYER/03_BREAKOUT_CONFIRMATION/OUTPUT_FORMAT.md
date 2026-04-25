# BREAKOUT_CONFIRMATION — OUTPUT_FORMAT.md
# Version: 1.0.0 | Layer: BREAKOUT_LAYER | Agent: 03_BREAKOUT_CONFIRMATION
# Created: 2026-04-15 | Status: ACTIVE

---

## OUTPUT SCHEMA

```yaml
breakout_confirmation_verdict:
  version: "1.0.0"
  timestamp: string              # ISO-8601 UTC
  asset: string
  timeframe: string              # 1D | 4H | 1H
  trigger_source: string         # ALERT_RADAR | MANUAL | SCHEDULED_SCAN

  verdict: string                # see VERDICT VALUES
  quality_score: int             # 0–10
  confirmation_confidence: float # 0.0–1.0

  candle_analysis:
    open: float
    high: float
    low: float
    close: float
    body_pct_of_range: float     # body / total range * 100
    upper_wick_pct_of_body: float
    lower_wick_pct_of_body: float
    close_vs_zone_boundary: string   # ABOVE | BELOW | AT
    close_distance_atr_multiple: float
    candle_quality: string       # STRONG | MODERATE | WEAK

  volume_analysis:
    breakout_volume: float
    volume_ma20: float
    volume_ratio: float          # breakout_volume / volume_ma20
    volume_verdict: string       # ABOVE_THRESHOLD | BELOW_THRESHOLD
    volume_spike: bool           # true if ratio > 2.0

  wick_check:
    wick_pct_of_body: float      # upper wick for longs, lower for shorts
    threshold: float             # 40.0
    status: string               # PASS | FAIL

  post_break_behavior:
    candles_evaluated: int
    follow_through: string       # STRONG | MODERATE | WEAK | REVERSED | INSUFFICIENT_DATA
    zone_reentry_detected: bool

  zone_reference:
    zone_id: string
    zone_quality: string         # PREMIUM | STANDARD | WEAK
    zone_score: int
    prior_failed_breaks: int

  external_context:
    news_severity: string        # LOW | MEDIUM | HIGH | CRITICAL | NOT_CHECKED
    news_clear: bool
    market_regime_checked: bool

  failure_flags: list[FailureFlag]
  notes: string                  # optional, max 80 words
```

**FailureFlag object:**
```yaml
flag: string
detail: string
```

---

## VERDICT VALUES

| Value | Meaning |
|---|---|
| `CONFIRMED` | All checks pass — route to Market Regime and Risk Guardian |
| `WEAK_BREAKOUT` | Close above zone but wick or volume borderline — proceed with caution flags |
| `FAKEOUT` | Close inside zone, wick-only break, or post-break reversal |
| `PENDING` | Insufficient candle evidence — re-evaluate on next close |
| `HOLD` | Active CRITICAL news — defer until cleared |
| `CONDITIONAL_CONFIRM` | Confirmed but BTC misaligned — downgraded confidence |
| `INVALID` | Missing required input fields |

---

## QUALITY SCORE RUBRIC (0–10)

| Criterion | Points |
|---|---|
| Close above zone boundary (not wick) | +2 |
| Volume ≥ 1.5x MA20 | +2 |
| Volume ≥ 0.8x MA20 (minimum threshold met) | +1 |
| Body ≥ 60% of candle range | +1 |
| Upper wick ≤ 40% of body (bullish) | +1 |
| Follow-through candle confirms | +1 |
| Retest detected and held | +1 |
| Prior failed break on zone | +1 |

---

## CONFIDENCE LEVELS

| confirmation_confidence | Condition |
|---|---|
| 0.90–1.0 | All checks pass, post-break follow-through present |
| 0.70–0.89 | All checks pass, no post-break data yet |
| 0.50–0.69 | WEAK_BREAKOUT or one borderline check |
| < 0.50 | FAKEOUT or PENDING |

---

## FAILURE FLAG CODES

| Code | Meaning |
|---|---|
| `WICK_ONLY_BREAK` | Close inside zone — not a real breakout |
| `VOLUME_INSUFFICIENT` | Volume < 0.8x MA20 |
| `WICK_REJECTION` | Upper/lower wick > 40% of body |
| `POST_BREAK_REVERSAL` | Next candle closed back inside zone |
| `NEWS_HOLD` | CRITICAL news prevents confirmation |
| `REGIME_NOT_CHECKED` | Market Regime absent — altcoin not safe to confirm |
| `ZONE_EXHAUSTED` | Two+ consecutive fakeouts at this zone |
| `WATCHLIST_ZONE_CEILING` | Zone was WATCHLIST — max verdict = WEAK_BREAKOUT |
| `INVALID_INPUT` | Required fields missing |

---

## DECISION MATRIX

| Close vs Zone | Volume Ratio | Wick % of Body | News | Verdict |
|---|---|---|---|---|
| ABOVE | ≥ 1.5x | ≤ 40% | CLEAR | `CONFIRMED` |
| ABOVE | 0.8–1.5x | ≤ 40% | CLEAR | `WEAK_BREAKOUT` |
| ABOVE | < 0.8x | ANY | CLEAR | `PENDING` |
| ABOVE | ≥ 1.5x | > 40% | CLEAR | `WEAK_BREAKOUT` |
| BELOW | ANY | ANY | ANY | `FAKEOUT` |
| ANY | ANY | ANY | CRITICAL | `HOLD` |
