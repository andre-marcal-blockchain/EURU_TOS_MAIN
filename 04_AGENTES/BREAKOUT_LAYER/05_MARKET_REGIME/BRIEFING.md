# MARKET_REGIME — BRIEFING.md
# Version: 1.0.0 | Layer: BREAKOUT_LAYER | Agent: 05_MARKET_REGIME
# Created: 2026-04-15 | Status: ACTIVE

---

## INPUTS

Market Regime receives the Breakout Confirmation verdict plus OHLCV series and indicator data for the asset and for BTC.

**Required input fields:**

```
breakout_confirmation:
  verdict                 : CONFIRMED | WEAK_BREAKOUT   # only these reach Market Regime
  asset                   : string
  timeframe               : string
  direction               : LONG | SHORT

asset_data:
  price_series            : list[OHLCV]    # last 50 candles on primary TF
  adx14                   : float
  atr14_current           : float
  atr14_10bars_ago        : float
  ema20_value             : float
  ema50_value             : float
  current_price           : float

btc_data:
  price_series            : list[OHLCV]    # required for all altcoin assets
  btc_adx14               : float
  btc_atr14               : float
  btc_ema20               : float
  btc_ema50               : float
  btc_current_price       : float

macro_data:                               # optional — mark NOT_CHECKED if absent
  dxy_trend               : UP | DOWN | FLAT
  btc_dominance_trend     : UP | DOWN | FLAT
  risk_sentiment          : RISK_ON | RISK_OFF | NEUTRAL

session                   : MORNING | ASIAN | MANUAL
```

**Note:** If `asset = "BTCUSDT"`, btc_data is not required. Set `btc_alignment: NOT_APPLICABLE`.

---

## OUTPUTS

A **Regime Report** appended to the evaluation package sent to Risk Guardian. See OUTPUT_FORMAT.md for full schema.

**Regime values:** `TREND_BULL`, `TREND_BEAR`, `CHOPPY`, `SIDEWAYS_RANGE`, `SIDEWAYS_COMPRESSION`, `REGIME_TRANSITION`, `UNKNOWN`

**Breakout favorability values:** `FAVORABLE`, `CONDITIONAL`, `UNFAVORABLE`, `PENDING_EXPANSION`

---

## VALID SITUATIONS

**Scenario A — TREND_BULL, favorable:**
- ETHUSDT 4H: ADX = 32, rising. Price above EMA20/50. ATR expanding +14%. BTC ADX = 28 (TREND_BULL). Risk sentiment = RISK_ON.
- Result: `TREND_BULL`, confidence = 0.91, btc_alignment = ALIGNED, breakout_favorability = FAVORABLE

**Scenario B — CHOPPY, unfavorable:**
- SOLUSDT 4H: ADX = 13, flat. Price oscillating in range. ATR flat. BTC ADX = 17 (CHOPPY).
- Result: `CHOPPY`, confidence = 0.82, btc_alignment = NEUTRAL, breakout_favorability = UNFAVORABLE

**Scenario C — BTC SIDEWAYS blocks TREND_BULL for altcoin:**
- LINKUSDT 4H: own ADX = 26, price above EMAs, good structure. But BTC ADX = 15 (SIDEWAYS).
- Result: Cannot output TREND_BULL. Output `CONDITIONAL` with `BTC_SIDEWAYS_WARNING`. Breakout_favorability = CONDITIONAL.

**Scenario D — Compression state:**
- BNBUSDT 4H: ADX = 17, ATR declining 24% over 10 bars. Price narrowing.
- Result: `SIDEWAYS_COMPRESSION`, confidence = 0.80, breakout_favorability = PENDING_EXPANSION

---

## INVALID SITUATIONS

**BTC check skipped for altcoin:**
- Market Regime output for MATICUSDT without btc_data fields populated.
- Invalid. BTC alignment is mandatory for all altcoins. Return `INVALID_INPUT`.

**Regime without confidence:**
- Output `TREND_BULL` but confidence field is null or absent.
- Invalid. Confidence is required for every regime output. If ADX is near boundary, reflect that in a lower confidence value.

**Reusing stale regime from prior session:**
- Session = MORNING. Prior session regime data from yesterday's ASIAN scan is used without refresh.
- Invalid. Regime must be computed from current session data.

---

## NOTES

- Market Regime runs once per breakout event — it is not a background process in this layer.
- BTC alignment score is a required field for all altcoin outputs. Missing = `INVALID_INPUT`.
- `REGIME_TRANSITION` outputs always include both `from_regime` and `to_regime` fields.
- Macro alignment is informational — it does not block signals but is used by Tactical Execution for target calibration.
