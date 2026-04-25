# BREAKOUT_CONFIRMATION — OUTPUT_FORMAT.md
# Version: 1.0.0 | Layer: Breakout Intelligence Expansion | Agent: 03
# Created: 2026-04-15 | Status: ACTIVE

---

## OUTPUT STRUCTURE

```yaml
breakout_confirmation_verdict:
  version: "1.0.0"
  timestamp: "<ISO-8601 UTC>"
  asset: "<SYMBOL>"
  timeframe: "<1D | 4H | 1H>"
  trigger_source: "<ALERT_RADAR | MANUAL | SCHEDULED_SCAN>"

  verdict: "<CONFIRMED | FAKEOUT | PENDING | HOLD | CONDITIONAL_CONFIRM | INVALID>"
  quality_score: <0–10>
  confirmation_confidence: <0.0–1.0>

  candle_analysis:
    body_pct_of_range: <float>          # body size / total range * 100
    wick_upper_pct_of_range: <float>
    wick_lower_pct_of_range: <float>
    close_vs_zone_boundary: "<ABOVE | BELOW | AT>"
    close_distance_atr_multiple: <float>
    candle_size_vs_avg: <float>         # ratio: candle_range / ATR(14)
    candle_quality: "<STRONG | MODERATE | WEAK>"

  volume_analysis:
    breakout_volume: <float>
    volume_ma20: <float>
    volume_ratio: <float>               # breakout_volume / volume_ma20
    volume_verdict: "<ABOVE_AVG | AVERAGE | BELOW_AVG>"
    volume_spike: <true | false>        # true if volume_ratio > 2.0

  post_break_behavior:
    candles_evaluated: <int>
    follow_through: "<STRONG | MODERATE | WEAK | REVERSED | INSUFFICIENT_DATA>"
    retest_detected: <true | false>
    retest_held: "<true | false | null>"

  zone_context:
    zone_id: "<ZONE_ID>"
    zone_quality: "<PREMIUM | STANDARD | WEAK>"
    zone_touch_count: <int>
    prior_failed_breaks: <int>

  external_filters:
    news_sentinel_status: "<LOW | MEDIUM | HIGH | CRITICAL | NOT_CHECKED>"
    news_clear: <true | false>
    btc_flow_status: "<CONFIRMS | CONTRADICTS | INCONCLUSIVE | NOT_CHECKED>"
    btc_aligned: <true | false>

  failure_flags:
    - flag: "<FLAG_CODE>"
      detail: "<short description>"

  notes: "<optional — max 100 words>"
```

---

## FIELD DEFINITIONS

| Field | Type | Allowed Values |
|---|---|---|
| `verdict` | enum | `CONFIRMED`, `FAKEOUT`, `PENDING`, `HOLD`, `CONDITIONAL_CONFIRM`, `INVALID` |
| `quality_score` | int | 0 – 10 |
| `confirmation_confidence` | float | 0.0 – 1.0 |
| `candle_quality` | enum | `STRONG`, `MODERATE`, `WEAK` |
| `close_vs_zone_boundary` | enum | `ABOVE`, `BELOW`, `AT` |
| `volume_verdict` | enum | `ABOVE_AVG`, `AVERAGE`, `BELOW_AVG` |
| `follow_through` | enum | `STRONG`, `MODERATE`, `WEAK`, `REVERSED`, `INSUFFICIENT_DATA` |

---

## QUALITY SCORE RUBRIC (0–10)

| Criterion | Points |
|---|---|
| Close > zone boundary (not wick) | +2 |
| Volume ≥ 1.5x MA20 | +2 |
| Volume ≥ 2.0x MA20 | +1 bonus |
| Body ≥ 60% of candle range | +1 |
| Upper wick ≤ 30% of range (bullish) | +1 |
| Follow-through candle confirms | +1 |
| Retest detected and held | +1 |
| Prior failed break on zone | +1 |
| BTC flow CONFIRMS | +1 bonus (max 10) |

---

## FAILURE FLAG CODES

| Code | Meaning |
|---|---|
| `WICK_ONLY_BREAK` | Close is below zone boundary — not a real breakout |
| `VOLUME_INSUFFICIENT` | Volume below MA20 — conviction absent |
| `POST_BREAK_REVERSAL` | Next candle closed back inside zone |
| `NEWS_HOLD` | Breakout held pending News Sentinel clearance |
| `BTC_MISALIGNED` | Altcoin breakout while BTC CONTRADICTS |
| `ZONE_EXHAUSTED` | Two or more consecutive fakeouts on this zone |
| `VOLUME_WITHOUT_STRUCTURE` | Volume spike but poor candle body quality |
| `INVALID_INPUT` | Missing required fields in evaluation request |
| `BELOW_AVG_CANDLE` | Candle range below average — no expansion signal |

---

## VERDICT DECISION MATRIX

| Close vs Zone | Volume | Candle Quality | News | Verdict |
|---|---|---|---|---|
| ABOVE | ≥ 1.5x | STRONG | CLEAR | CONFIRMED |
| ABOVE | ≥ 1.0x | MODERATE | CLEAR | PENDING (wait 1 candle) |
| ABOVE | < 1.0x | ANY | CLEAR | PENDING |
| BELOW | ANY | ANY | ANY | FAKEOUT |
| ABOVE | ≥ 1.5x | STRONG | HIGH/CRITICAL | HOLD |
| ABOVE | ≥ 1.5x | STRONG | CLEAR | CONDITIONAL_CONFIRM (if BTC CONTRADICTS) |
