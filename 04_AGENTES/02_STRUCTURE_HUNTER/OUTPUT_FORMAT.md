# STRUCTURE_HUNTER — OUTPUT_FORMAT.md
# Version: 1.0.0 | Layer: Breakout Intelligence Expansion | Agent: 02
# Created: 2026-04-15 | Status: ACTIVE

---

## OUTPUT STRUCTURE

```yaml
structure_hunter_report:
  version: "1.0.0"
  timestamp: "<ISO-8601 UTC>"
  asset: "<SYMBOL>"
  primary_timeframe: "<1D | 4H | 1H>"
  session: "<MORNING | ASIAN | MANUAL>"

  structural_status: "<BREAKOUT_READY | WATCHLIST | NO_STRUCTURE | DATA_UNAVAILABLE>"
  structure_confidence: <0.0–1.0>

  primary_zones:
    - zone_id: "<ZONE_001>"
      type: "<RESISTANCE | SUPPORT>"
      price_level: <float>
      price_band_low: <float>
      price_band_high: <float>
      quality: "<PREMIUM | STANDARD | WEAK>"
      zone_score: <0–10>
      touch_count: <int>
      zone_age_bars: <int>
      compression_detected: <true | false>
      compression_strength: "<STRONG | MODERATE | WEAK | NONE>"
      failed_break_attempts: <int>
      last_failed_break_date: "<ISO-8601 date | null>"
      distance_from_current_price_atr: <float>
      notes: "<optional>"

  formation:
    type: "<ASCENDING_TRIANGLE | DESCENDING_TRIANGLE | SYMMETRICAL_TRIANGLE | FLAT_TOP | FLAT_BASE | BULL_FLAG | BEAR_FLAG | PENNANT | WEDGE_UP | WEDGE_DOWN | HORIZONTAL_RANGE | NONE>"
    maturity: "<FORMING | MATURE | COMPLETE>"
    formation_score: <0–10>

  compression_assessment:
    active: <true | false>
    atr_trend: "<EXPANDING | NEUTRAL | CONTRACTING>"
    atr_change_pct_10bars: <float>
    range_width_pct: <float>

  btc_structural_alignment: "<ALIGNED | MISALIGNED | NEUTRAL | NOT_CHECKED>"

  failure_flags:
    - flag: "<FLAG_CODE>"
      detail: "<short description>"

  notes: "<optional — max 100 words>"
```

---

## FIELD DEFINITIONS

| Field | Type | Allowed Values |
|---|---|---|
| `structural_status` | enum | `BREAKOUT_READY`, `WATCHLIST`, `NO_STRUCTURE`, `DATA_UNAVAILABLE` |
| `structure_confidence` | float | 0.0 – 1.0 |
| `zone quality` | enum | `PREMIUM`, `STANDARD`, `WEAK` |
| `zone_score` | int | 0 – 10 |
| `compression_strength` | enum | `STRONG`, `MODERATE`, `WEAK`, `NONE` |
| `formation.type` | enum | See list above |
| `formation.maturity` | enum | `FORMING`, `MATURE`, `COMPLETE` |
| `atr_trend` | enum | `EXPANDING`, `NEUTRAL`, `CONTRACTING` |
| `btc_structural_alignment` | enum | `ALIGNED`, `MISALIGNED`, `NEUTRAL`, `NOT_CHECKED` |

---

## ZONE SCORE RUBRIC (0–10)

| Criterion | Points |
|---|---|
| Touch count ≥ 4 | +3 |
| Touch count = 3 | +2 |
| Touch count = 2 | +1 |
| Compression present (STRONG) | +2 |
| Compression present (MODERATE) | +1 |
| Failed break attempt recorded | +2 |
| Zone age ≤ 30 bars | +1 |
| Clean zone (no overlap with other zones) | +1 |
| BTC aligned | +1 bonus (does not exceed 10) |

---

## FAILURE FLAG CODES

| Code | Meaning |
|---|---|
| `INSUFFICIENT_TOUCHES` | Zone has fewer than 2 touches — not tradeable |
| `NO_STRUCTURE` | No valid zone or formation detected on this asset |
| `STRUCTURE_CONFLICT` | Overlapping support/resistance zones create ambiguity |
| `BTC_STRUCTURE_MISSING` | BTC structural status unavailable — altcoin analysis unreliable |
| `DATA_UNAVAILABLE` | Price series missing or insufficient for analysis |
| `INVALID_TIMEFRAME` | Sub-1H timeframe passed for zone construction |
| `ZONE_ALREADY_BROKEN` | Current price has closed beyond zone by > 1.5x ATR |

---

## EXAMPLE OUTPUT

```yaml
structure_hunter_report:
  version: "1.0.0"
  timestamp: "2026-04-15T08:45:00Z"
  asset: "ETHUSDT"
  primary_timeframe: "4H"
  session: "MORNING"
  structural_status: "BREAKOUT_READY"
  structure_confidence: 0.87
  primary_zones:
    - zone_id: "ZONE_001"
      type: "RESISTANCE"
      price_level: 3200.00
      price_band_low: 3192.00
      price_band_high: 3208.00
      quality: "PREMIUM"
      zone_score: 9
      touch_count: 4
      zone_age_bars: 18
      compression_detected: true
      compression_strength: "STRONG"
      failed_break_attempts: 1
      last_failed_break_date: "2026-04-08"
      distance_from_current_price_atr: 0.6
      notes: "Ascending triangle with 4 touches. Single wick break on Apr-08 rejected. Compression strong."
  formation:
    type: "ASCENDING_TRIANGLE"
    maturity: "MATURE"
    formation_score: 8
  compression_assessment:
    active: true
    atr_trend: "CONTRACTING"
    atr_change_pct_10bars: -18.5
    range_width_pct: 3.2
  btc_structural_alignment: "ALIGNED"
  failure_flags: []
  notes: "High-quality breakout candidate. Recommend routing to Breakout Confirmation."
```
