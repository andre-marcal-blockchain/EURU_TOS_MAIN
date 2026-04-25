# STRUCTURE_HUNTER — OUTPUT_FORMAT.md
# Version: 1.0.0 | Layer: BREAKOUT_LAYER | Agent: 02_STRUCTURE_HUNTER
# Created: 2026-04-15 | Status: ACTIVE

---

## OUTPUT SCHEMA

```yaml
structure_hunter_report:
  version: "1.0.0"
  timestamp: string              # ISO-8601 UTC
  asset: string
  timeframe: string              # 1D | 4H | 1H
  session: string                # MORNING | ASIAN | MANUAL

  structural_status: string      # see STATUS VALUES
  structure_confidence: float    # 0.0–1.0

  zones:
    - zone_id: string            # e.g., "Z001"
      type: string               # RESISTANCE | SUPPORT
      price_level: float
      price_band_low: float
      price_band_high: float
      quality: string            # PREMIUM | STANDARD | WEAK
      zone_score: int            # 0–10
      touch_count: int
      zone_age_bars: int
      last_retest_bars_ago: int | null
      compression_at_zone: bool
      compression_candle_count: int
      failed_break_count: int
      last_failed_break_date: string | null  # ISO-8601 date
      distance_from_price_atr: float
      status: string             # ACTIVE | EXPIRED | WATCH_ONLY

  formation:
    type: string                 # see FORMATION TYPES
    maturity: string             # FORMING | MATURE | COMPLETE
    score: int                   # 0–10

  compression:
    active: bool
    candle_count: int            # consecutive contracting candles
    strength: string             # STRONG | MODERATE | WEAK | NONE
    atr_change_pct_10bars: float

  btc_context:
    alignment: string            # ALIGNED | MISALIGNED | NEUTRAL | NOT_CHECKED
    warning: string              # BTC_STRUCTURE_MISSING | BTC_BEARISH | NONE

  failure_flags: list[FailureFlag]
  notes: string                  # optional, max 80 words
```

**FailureFlag object:**
```yaml
flag: string
detail: string
```

---

## STATUS VALUES

| Value | Meaning |
|---|---|
| `BREAKOUT_READY` | Valid zone (score ≥ 5), compression active, BTC aligned |
| `WATCHLIST` | Valid zone but compression absent or BTC neutral |
| `NO_STRUCTURE` | No zone meets minimum criteria — do not route to Breakout Confirmation |
| `INSUFFICIENT_DATA` | Less than 30 candles available for analysis |

---

## FORMATION TYPES

`ASCENDING_TRIANGLE`, `DESCENDING_TRIANGLE`, `SYMMETRICAL_TRIANGLE`, `FLAT_TOP`, `FLAT_BASE`, `BULL_FLAG`, `BEAR_FLAG`, `PENNANT`, `WEDGE_UP`, `WEDGE_DOWN`, `HORIZONTAL_RANGE`, `NONE`

---

## ZONE SCORE RUBRIC (0–10)

| Criterion | Points |
|---|---|
| Touch count ≥ 4 | +3 |
| Touch count = 3 | +2 |
| Touch count = 2 | +1 |
| Compression ≥ 3 candles (STRONG) | +2 |
| Compression ≥ 3 candles (MODERATE) | +1 |
| Failed break on record | +2 |
| Zone age ≤ 20 bars | +1 |
| Clean zone (no overlap) | +1 |
| BTC aligned (bonus, capped at 10) | +1 |

---

## CONFIDENCE LEVELS

| structure_confidence | Condition |
|---|---|
| 0.85–1.0 | Zone score ≥ 8, compression strong, BTC aligned |
| 0.65–0.84 | Zone score 6–7, moderate compression |
| 0.45–0.64 | Zone score 5, no compression or BTC neutral |
| < 0.45 | Zone score < 5 — should not reach BREAKOUT_READY |

---

## FAILURE FLAG CODES

| Code | Meaning |
|---|---|
| `INSUFFICIENT_TOUCHES` | Zone has < 2 touches |
| `NO_STRUCTURE` | No valid zone found |
| `ZONE_EXPIRED` | Zone older than 30 bars, no retest |
| `STRUCTURE_CONFLICT` | Overlapping S/R zones create ambiguity |
| `BTC_STRUCTURE_MISSING` | BTC series or status unavailable |
| `INSUFFICIENT_DATA` | < 30 candles in series |
| `DATA_GAPS_DETECTED` | OHLCV series has gaps |
| `ZONE_ALREADY_BROKEN` | Price has closed > 1.5x ATR beyond zone |
| `COMPRESSION_BELOW_MINIMUM` | Fewer than 3 contracting candles |

---

## EXAMPLE OUTPUT

```yaml
structure_hunter_report:
  version: "1.0.0"
  timestamp: "2026-04-15T08:45:00Z"
  asset: "ETHUSDT"
  timeframe: "4H"
  session: "MORNING"
  structural_status: "BREAKOUT_READY"
  structure_confidence: 0.88
  zones:
    - zone_id: "Z001"
      type: "RESISTANCE"
      price_level: 3200.00
      price_band_low: 3192.00
      price_band_high: 3208.00
      quality: "PREMIUM"
      zone_score: 9
      touch_count: 4
      zone_age_bars: 18
      last_retest_bars_ago: 6
      compression_at_zone: true
      compression_candle_count: 5
      failed_break_count: 1
      last_failed_break_date: "2026-04-08"
      distance_from_price_atr: 0.6
      status: "ACTIVE"
  formation:
    type: "ASCENDING_TRIANGLE"
    maturity: "MATURE"
    score: 8
  compression:
    active: true
    candle_count: 5
    strength: "STRONG"
    atr_change_pct_10bars: -19.2
  btc_context:
    alignment: "ALIGNED"
    warning: "NONE"
  failure_flags: []
  notes: "Premium zone. 4 touches, 1 failed break, strong compression. Route to Breakout Confirmation."
```
