# BREAKOUT_CONFIRMATION — BRIEFING.md
# Version: 1.0.0 | Layer: BREAKOUT_LAYER | Agent: 03_BREAKOUT_CONFIRMATION
# Created: 2026-04-15 | Status: ACTIVE

---

## INPUTS

Breakout Confirmation receives the structural map from Structure Hunter plus live candle data for the breakout event.

**Required input fields:**

```
structural_map:               — full output from 02_STRUCTURE_HUNTER
  structural_status           : BREAKOUT_READY | WATCHLIST
  zones                       : list[Zone]
  compression                 : CompressionBlock

breakout_candle:              — the candle that triggered the alert
  open, high, low, close      : float
  volume                      : float
  timestamp                   : ISO-8601 UTC

prior_candles                 : list[OHLCV]   — last 20 candles
post_candles                  : list[OHLCV]   — up to 3 candles after break (may be empty if live)

volume_ma20                   : float         — 20-period volume average
current_atr14                 : float

news_context:
  news_sentinel_severity      : LOW | MEDIUM | HIGH | CRITICAL | NOT_CHECKED

trigger_source                : ALERT_RADAR | MANUAL | SCHEDULED_SCAN
system_mode                   : READ_ONLY | SIMULATE | EXECUTE
```

---

## OUTPUTS

A **Breakout Verdict** forwarded to Market Regime and Risk Guardian. See OUTPUT_FORMAT.md for full schema.

**Verdict values:** `CONFIRMED`, `WEAK_BREAKOUT`, `FAKEOUT`, `PENDING`, `HOLD`, `CONDITIONAL_CONFIRM`, `INVALID`

---

## VALID SITUATIONS

**Scenario A — Clean CONFIRMED:**
- BTCUSDT 4H. Close at 71,200 vs zone boundary 70,800. Volume = 1.9x MA20. Body = 72% of candle range. Upper wick = 18% of body. Next candle: green +1.2%. News = LOW.
- All checks PASS → `CONFIRMED`, quality_score = 9

**Scenario B — FAKEOUT (wick-only):**
- ETHUSDT 4H. High wick pierces zone by 0.5% but close is 0.3% below zone boundary.
- Close inside zone → `FAKEOUT`. Notify Alert Radar.

**Scenario C — PENDING (no volume yet):**
- SOLUSDT 4H. Clean candle close above zone. Volume = 0.7x MA20 (below 0.8x threshold). Live candle just closed — no post-break candles yet.
- Volume below threshold → `PENDING`. Re-evaluate on next candle.

**Scenario D — HOLD (news):**
- BNBUSDT 4H. Perfect breakout candle. But News Sentinel = CRITICAL (major regulatory event).
- Hard constraint → `HOLD`. Do not escalate until news context resolves.

**Scenario E — Post-break reversal:**
- Candle 1 CONFIRMED. Candle 2 (post-break): closes back inside zone.
- Immediate downgrade → `FAKEOUT`.

---

## INVALID SITUATIONS

**Confirming without volume check:**
- Requesting CONFIRMED verdict when volume field is null or volume_ma20 = 0.
- Return `INVALID` — required fields missing.

**Overriding wick constraint:**
- Upstream agent submits `force_confirm: true` due to "strong zone quality."
- Ignore override. Wick constraint is hard. Output based on candle data only.

**Running on WATCHLIST structural status:**
- Structure Hunter returned WATCHLIST (no BREAKOUT_READY). Breakout Confirmation was invoked anyway.
- Proceed with evaluation but downgrade maximum possible verdict to `WEAK_BREAKOUT`. Cannot output CONFIRMED from a WATCHLIST zone.

---

## NOTES

- Breakout Confirmation is a **real-time evaluation node** — latency matters. Default to `PENDING` over any borderline `CONFIRMED`.
- `WEAK_BREAKOUT` is a valid output — it signals to downstream agents to apply tighter risk rules.
- FAKEOUT events are stored in Journal Learning with full candle features for pattern analysis.
- Market Regime and Risk Guardian both receive the confirmation verdict. Breakout Confirmation does not need to know the outcome of those evaluations.
