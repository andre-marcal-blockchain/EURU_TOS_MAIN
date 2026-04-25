# MARKET_REGIME — OUTPUT_FORMAT.md
# Version: 1.0.0 | Layer: Breakout Intelligence Expansion | Agent: 05
# Created: 2026-04-15 | Status: ACTIVE

---

## OUTPUT STRUCTURE

```yaml
market_regime_report:
  version: "1.0.0"
  timestamp: "<ISO-8601 UTC>"
  asset: "<SYMBOL>"
  timeframe: "<1D | 4H | 1H>"
  session: "<MORNING | ASIAN | MANUAL>"

  regime: "<TRENDING_BULLISH | TRENDING_BEARISH | CHOPPY | SIDEWAYS_RANGE | SIDEWAYS_COMPRESSION | REGIME_TRANSITION | UNKNOWN>"
  regime_confidence: <0.0–1.0>
  regime_duration_bars: <int>             # how many bars current regime has been active

  volatility:
    state: "<EXPANDING | NEUTRAL | CONTRACTING | SPIKE>"
    atr14_current: <float>
    atr14_10bars_ago: <float>
    atr_change_pct: <float>
    volatility_percentile_20bar: <float>  # 0–100, where current ATR sits vs last 20 bars

  trend_metrics:
    adx14: <float>
    adx_trend: "<RISING | FALLING | FLAT>"
    price_above_ema20: <true | false>
    price_above_ema50: <true | false>
    ema20_above_ema50: <true | false>

  btc_alignment:
    applicable: <true | false>            # false if asset = BTC itself
    btc_regime: "<TRENDING_BULLISH | TRENDING_BEARISH | CHOPPY | SIDEWAYS_RANGE | SIDEWAYS_COMPRESSION | UNKNOWN>"
    btc_adx14: <float>
    btc_aligned: <true | false>
    btc_warning: "<BTC_CHOPPY_WARNING | BTC_BEARISH_WARNING | NONE>"

  macro_alignment:
    checked: <true | false>
    dxy_trend: "<UP | DOWN | FLAT | NOT_CHECKED>"
    btc_dominance_trend: "<UP | DOWN | FLAT | NOT_CHECKED>"
    risk_sentiment: "<RISK_ON | RISK_OFF | NEUTRAL | NOT_CHECKED>"
    macro_verdict: "<SUPPORTIVE | HEADWIND | NEUTRAL | NOT_CHECKED>"

  breakout_favorability:
    verdict: "<FAVORABLE | CONDITIONAL | UNFAVORABLE | PENDING_EXPANSION>"
    reason: "<short explanation — max 50 words>"

  regime_transition:
    detected: <true | false>
    from_regime: "<prior_regime | null>"
    to_regime: "<emerging_regime | null>"
    confirming_bars: <int>
    confidence: <0.0–1.0>

  failure_flags:
    - flag: "<FLAG_CODE>"
      detail: "<short description>"

  notes: "<optional — max 80 words>"
```

---

## FIELD DEFINITIONS

| Field | Type | Allowed Values |
|---|---|---|
| `regime` | enum | `TRENDING_BULLISH`, `TRENDING_BEARISH`, `CHOPPY`, `SIDEWAYS_RANGE`, `SIDEWAYS_COMPRESSION`, `REGIME_TRANSITION`, `UNKNOWN` |
| `volatility.state` | enum | `EXPANDING`, `NEUTRAL`, `CONTRACTING`, `SPIKE` |
| `adx_trend` | enum | `RISING`, `FALLING`, `FLAT` |
| `btc_warning` | enum | `BTC_CHOPPY_WARNING`, `BTC_BEARISH_WARNING`, `NONE` |
| `macro_verdict` | enum | `SUPPORTIVE`, `HEADWIND`, `NEUTRAL`, `NOT_CHECKED` |
| `breakout_favorability.verdict` | enum | `FAVORABLE`, `CONDITIONAL`, `UNFAVORABLE`, `PENDING_EXPANSION` |

---

## REGIME CLASSIFICATION RULES

| ADX(14) | Price Structure | ATR Trend | Regime |
|---|---|---|---|
| ≥ 25, rising | Directional | Expanding | TRENDING |
| 20–25 | Mixed | Flat/Expanding | REGIME_TRANSITION |
| < 20 | Oscillating | Flat | CHOPPY |
| < 20 | Bounded | Flat | SIDEWAYS_RANGE |
| < 20 | Narrowing | Contracting | SIDEWAYS_COMPRESSION |
| Any | Any | Spike | May indicate REGIME_TRANSITION |

---

## FAILURE FLAG CODES

| Code | Meaning |
|---|---|
| `INSUFFICIENT_DATA` | Less than 20 candles available for regime detection |
| `ADX_UNAVAILABLE` | ADX could not be computed — regime unreliable |
| `BTC_DATA_MISSING` | BTC series absent — altcoin alignment not possible |
| `MACRO_DATA_MISSING` | Macro inputs absent — macro alignment not checked |
| `REGIME_UNSTABLE` | High variability in signals — low-confidence classification |
| `BTC_CHOPPY_WARNING` | BTC regime is CHOPPY — altcoin breakouts at elevated risk |
| `BTC_BEARISH_WARNING` | BTC regime is TRENDING_BEARISH — altcoin longs at elevated risk |
| `MACRO_HEADWIND` | Macro conditions (DXY/risk sentiment) contradict setup direction |

---

## EXAMPLE OUTPUT

```yaml
market_regime_report:
  version: "1.0.0"
  timestamp: "2026-04-15T08:00:00Z"
  asset: "ETHUSDT"
  timeframe: "4H"
  session: "MORNING"
  regime: "SIDEWAYS_COMPRESSION"
  regime_confidence: 0.83
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
    btc_warning: "NONE"
  macro_alignment:
    checked: true
    dxy_trend: "DOWN"
    btc_dominance_trend: "FLAT"
    risk_sentiment: "RISK_ON"
    macro_verdict: "SUPPORTIVE"
  breakout_favorability:
    verdict: "PENDING_EXPANSION"
    reason: "Compression active on both ETH and BTC. ATR contracting. Regime primed for breakout but not yet expanding."
  regime_transition:
    detected: false
    from_regime: null
    to_regime: null
    confirming_bars: 0
    confidence: 0.0
  failure_flags: []
  notes: "Coiling structure on both ETH and BTC. Macro supportive. Watch for volume expansion as trigger."
```
