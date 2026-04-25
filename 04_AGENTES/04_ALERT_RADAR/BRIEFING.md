# ALERT_RADAR — BRIEFING.md
# Version: 1.0.0 | Layer: Breakout Intelligence Expansion | Agent: 04
# Created: 2026-04-15 | Status: ACTIVE

---

## WHAT THIS AGENT RECEIVES

Alert Radar receives raw webhook payloads from external alert systems. The payloads arrive in varying formats but must be normalizable to the Euru standard. Common source formats:

**TradingView Webhook (raw):**
```json
{
  "ticker": "ETHUSDT",
  "close": "3198.50",
  "volume": "182450",
  "time": "2026-04-15T09:00:00Z",
  "alert_name": "Breakout_Alert_ETH_4H",
  "message": "ETH broke above 3200 resistance"
}
```

**Custom Script Alert (raw):**
```json
{
  "asset": "BTCUSDT",
  "alert_type": "BREAKOUT",
  "zone_id": "ZONE_001",
  "timeframe": "4H",
  "direction": "LONG",
  "price": 71250.00,
  "timestamp": "2026-04-15T09:15:00Z",
  "source": "euru_morning_scan"
}
```

---

## WHAT THIS AGENT PRODUCES

A **Normalized Alert** in Euru standard format, plus a routing decision:

```
alert_status: ROUTED | REJECTED | OBSERVATION_ONLY | INVALID | DUPLICATE
routed_to: agent_name | null
normalized_alert: <Euru standard alert object>
rejection_reason: string | null
```

---

## HOW OUTPUTS ARE CONSUMED

| Downstream Agent | Receives From Alert Radar |
|---|---|
| Breakout Confirmation (03) | BREAKOUT alerts after normalization |
| Structure Hunter (02) | SETUP / STRUCTURE alerts |
| Market Regime (05) | REGIME / MACRO alerts |
| Journal Learning (08) | All alerts (including rejected) for pattern logging |
| DevOps Guardian (main 06) | High-volume or anomalous alert reports |

---

## NORMALIZATION MAPPING

Alert Radar translates external formats to this standard schema:

```yaml
euru_alert:
  alert_id: "<UUID>"
  received_at: "<ISO-8601 UTC>"
  source: "<TRADINGVIEW | CUSTOM_SCRIPT | MANUAL>"
  asset: "<SYMBOL>"
  alert_type: "<BREAKOUT | SETUP | STRUCTURE | REGIME | TEST>"
  direction: "<LONG | SHORT | NEUTRAL>"
  timeframe: "<1D | 4H | 1H | 15M>"
  trigger_price: <float>
  trigger_timestamp: "<ISO-8601 UTC>"
  zone_id: "<ZONE_ID | null>"
  raw_message: "<original message>"
  age_candle_periods: <float>        # how old is alert in candle units
  watchlist_confirmed: <true | false>
```

---

## EXAMPLES OF VALID SITUATIONS

**Valid — ROUTED BREAKOUT:**
- TradingView alert arrives for ETHUSDT, 4H timeframe. Asset is on WATCHLIST_OFICIAL.md. Alert timestamp = 9 minutes ago (< 1 candle period old). Structure Hunter has an active ZONE_001 at 3,200. Alert type maps to BREAKOUT. System mode = SIMULATE.
- Result: ROUTED → Breakout Confirmation (03)

**Valid — OBSERVATION_ONLY:**
- Same alert arrives, but system_mode = READ_ONLY.
- Result: OBSERVATION_ONLY — alert logged, not routed. No pipeline activation.

**Valid — REJECTED (not on watchlist):**
- Alert arrives for "DOGEUSDT". Asset not on WATCHLIST_OFICIAL.md.
- Result: REJECTED. Log: "Asset DOGEUSDT not on official watchlist."

---

## EXAMPLES OF INVALID SITUATIONS

**Invalid — Stale alert:**
- Alert for BTCUSDT 4H arrives with timestamp 10 hours ago (= 2.5 candle periods)
- Result: REJECTED. Log: "Alert age = 2.5 candle periods. Threshold = 2.0. Stale."

**Invalid — Duplicate within cooldown:**
- ETHUSDT BREAKOUT alert received at 09:00. Identical alert (same asset, zone, direction) arrives at 09:45. Cooldown window = 60 min.
- Result: DUPLICATE — suppressed. Not routed.

**Invalid — Missing required fields:**
- Payload arrives with `asset` and `time` but no `alert_type`
- Result: INVALID — return error. Cannot normalize without alert_type.

---

## AGENT POSITION IN PIPELINE

```
[External Alert Source] → [ALERT_RADAR] → Breakout Confirmation (03)
                                        → Structure Hunter (02)
                                        → Market Regime (05)
                                        → Journal Learning (08) [always]
```

Alert Radar is the **pipeline entry point** for all external signals. It has no upstream agent dependencies.
