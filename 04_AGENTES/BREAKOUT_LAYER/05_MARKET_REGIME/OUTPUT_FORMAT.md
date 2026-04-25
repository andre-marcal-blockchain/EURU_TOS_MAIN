# MARKET_REGIME — OUTPUT_FORMAT.md
# Version: 1.0.0 | Layer: BREAKOUT_LAYER | Agent: 05_MARKET_REGIME
# Created: 2026-04-15 | Status: ACTIVE

---

## OUTPUT SCHEMA

```yaml
market_regime_report:
  version: "1.0.0"
  timestamp: string              # ISO-8601 UTC
  asset: string
  timeframe: string              # 1D | 4H | 1H
  session: string                # MORNING | ASIAN | MANUAL

  regime: string                 # see REGIME VALUES
  regime_confidence: float       # 0.0–1.0  — REQUIRED on every output
  regime_duration_bars: int      # how many bars current regime has been active

  volatility:
    state: string                # EXPANDING | NEUTRAL | CONTRACTING | SPIKE
    atr14_current: float
    atr14_10bars_ago: float
    atr_change_pct: float
    volatility_percentile_20bar: float   # 0–100

  trend_metrics:
    adx14: float
    adx_trend: string            # RISING | FALLING | FLAT
    price_above_ema20: bool
    price_above_ema50: bool
    ema20_above_ema50: bool

  btc_alignment:
    applicable: bool             # false only if asset = BTCUSDT
    btc_regime: string           # same enum as regime
    btc_adx14: float | null
    btc_aligned: bool
    btc_alignment_score: float   # 0.0–1.0 — REQUIRED for all altcoins
    warning: string              # BTC_SIDEWAYS_WARNING | BTC_BEARISH_WARNING | NONE

  macro_alignment:
    checked: bool
    dxy_trend: string            # UP | DOWN | FLAT | NOT_CHECKED
    btc_dominance_trend: string  # UP | DOWN | FLAT | NOT_CHECKED
    risk_sentiment: string       # RISK_ON | RISK_OFF | NEUTRAL | NOT_CHECKED
    macro_verdict: string        # SUPPORTIVE | HEADWIND | NEUTRAL | NOT_CHECKED

  breakout_favorability:
    verdict: string              # FAVORABLE | CONDITIONAL | UNFAVORABLE | PENDING_EXPANSION
    reason: string               # max 60 words

  regime_transition:
    detected: bool
    from_regime: string | null
    to_regime: string | null
    confirming_bars: int
    confidence: float

  failure_flags: list[FailureFlag]
  notes: string                  # optional, max 80 words
```

**FailureFlag object:**
```yaml
flag: string
detail: string
```

---

## REGIME VALUES

| Value | ADX Condition | Notes |
|---|---|---|
| `TREND_BULL` | ADX ≥ 20, rising, price above EMAs | Not assignable to altcoin when BTC = SIDEWAYS/BEAR |
| `TREND_BEAR` | ADX ≥ 20, rising, price below EMAs | |
| `CHOPPY` | ADX < 20, oscillating | breakout_favorability always UNFAVORABLE |
| `SIDEWAYS_RANGE` | ADX < 20, bounded | |
| `SIDEWAYS_COMPRESSION` | ADX < 20, ATR contracting | breakout_favorability = PENDING_EXPANSION |
| `REGIME_TRANSITION` | ADX crossing boundary, 3+ bars | Requires from/to fields |
| `UNKNOWN` | Insufficient data | Low confidence — flag |

---

## CONFIDENCE LEVELS

| regime_confidence | Condition |
|---|---|
| 0.85–1.0 | ADX clearly above/below threshold, ATR trend clear, BTC aligned |
| 0.65–0.84 | Moderate clarity, one borderline indicator |
| 0.45–0.64 | Mixed signals, near ADX boundary |
| < 0.45 | Conflicting indicators — output `UNKNOWN` or `REGIME_TRANSITION` |

---

## BTC ALIGNMENT SCORE

| btc_alignment_score | Meaning |
|---|---|
| 0.8–1.0 | BTC strongly supports the setup direction |
| 0.5–0.79 | BTC neutral — no strong confirmation or contradiction |
| 0.2–0.49 | BTC mildly opposed — apply CONDITIONAL classification |
| 0.0–0.19 | BTC strongly opposed — TREND_BULL blocked for altcoin longs |

---

## FAILURE FLAG CODES

| Code | Meaning |
|---|---|
| `INSUFFICIENT_DATA` | < 20 candles available |
| `ADX_UNAVAILABLE` | ADX could not be computed |
| `BTC_DATA_MISSING` | BTC series absent for altcoin analysis |
| `BTC_SIDEWAYS_WARNING` | BTC in SIDEWAYS — altcoin TREND_BULL blocked |
| `BTC_BEARISH_WARNING` | BTC in TREND_BEAR — altcoin longs elevated risk |
| `MACRO_NOT_CHECKED` | Macro inputs absent |
| `LOW_CONFIDENCE_REGIME` | ADX near boundary, conflicting signals |
| `EXPANSION_SPIKE` | Sudden ATR spike > 50% — possible news-driven move |
| `STALE_REGIME_DATA` | Regime computed from prior session — not valid |

---

## EXAMPLE OUTPUT

```yaml
market_regime_report:
  version: "1.0.0"
  timestamp: "2026-04-15T09:05:00Z"
  asset: "ETHUSDT"
  timeframe: "4H"
  session: "MORNING"
  regime: "SIDEWAYS_COMPRESSION"
  regime_confidence: 0.84
  regime_duration_bars: 14
  volatility:
    state: "CONTRACTING"
    atr14_current: 48.2
    atr14_10bars_ago: 62.1
    atr_change_pct: -22.4
    volatility_percentile_20bar: 18.0
  trend_metrics:
    adx14: 16.3
    adx_trend: "FALLING"
    price_above_ema20: true
    price_above_ema50: true
    ema20_above_ema50: true
  btc_alignment:
    applicable: true
    btc_regime: "SIDEWAYS_COMPRESSION"
    btc_adx14: 18.1
    btc_aligned: true
    btc_alignment_score: 0.72
    warning: "NONE"
  macro_alignment:
    checked: true
    dxy_trend: "DOWN"
    btc_dominance_trend: "FLAT"
    risk_sentiment: "RISK_ON"
    macro_verdict: "SUPPORTIVE"
  breakout_favorability:
    verdict: "PENDING_EXPANSION"
    reason: "Compression on both ETH and BTC. ATR contracting. Regime primed but not yet expanding. Favorable once volume confirms."
  regime_transition:
    detected: false
    from_regime: null
    to_regime: null
    confirming_bars: 0
    confidence: 0.0
  failure_flags: []
  notes: "Both ETH and BTC coiling. Macro supportive. Watch for volume expansion as expansion trigger."
```
