# ALERT_RADAR — OUTPUT_FORMAT.md
# Version: 1.0.0 | Layer: Breakout Intelligence Expansion | Agent: 04
# Created: 2026-04-15 | Status: ACTIVE

---

## OUTPUT STRUCTURE

```yaml
alert_radar_report:
  version: "1.0.0"
  received_at: "<ISO-8601 UTC>"
  processing_latency_ms: <int>

  alert_status: "<ROUTED | REJECTED | OBSERVATION_ONLY | DUPLICATE | INVALID>"
  routed_to: "<agent_name | null>"
  rejection_reason: "<string | null>"

  normalized_alert:
    alert_id: "<UUID>"
    source: "<TRADINGVIEW | CUSTOM_SCRIPT | MANUAL>"
    asset: "<SYMBOL>"
    alert_type: "<BREAKOUT | SETUP | STRUCTURE | REGIME | TEST>"
    direction: "<LONG | SHORT | NEUTRAL>"
    timeframe: "<1D | 4H | 1H | 15M>"
    trigger_price: <float>
    trigger_timestamp: "<ISO-8601 UTC>"
    zone_id: "<ZONE_ID | null>"
    age_candle_periods: <float>
    watchlist_confirmed: <true | false>
    raw_message: "<original alert message>"

  validation_checks:
    asset_on_watchlist:
      status: "<PASS | FAIL>"
      value: "<SYMBOL>"

    alert_type_recognized:
      status: "<PASS | FAIL>"
      value: "<type_detected>"

    payload_complete:
      status: "<PASS | FAIL>"
      missing_fields: ["<field_name>"]

    staleness_check:
      status: "<PASS | FAIL>"
      age_candle_periods: <float>
      threshold: 2.0

    duplicate_check:
      status: "<PASS | FAIL>"
      cooldown_window_min: <int>
      last_identical_alert_at: "<ISO-8601 UTC | null>"

    system_mode_check:
      status: "<PASS | OBSERVATION_ONLY>"
      system_mode: "<READ_ONLY | SIMULATE | EXECUTE>"

    zone_validity_check:
      status: "<PASS | FAIL | SKIPPED>"
      zone_id: "<ZONE_ID | null>"
      zone_active: "<true | false | null>"

  failure_flags:
    - flag: "<FLAG_CODE>"
      detail: "<short description>"

  notes: "<optional — max 60 words>"
```

---

## FIELD DEFINITIONS

| Field | Type | Allowed Values |
|---|---|---|
| `alert_status` | enum | `ROUTED`, `REJECTED`, `OBSERVATION_ONLY`, `DUPLICATE`, `INVALID` |
| `alert_type` | enum | `BREAKOUT`, `SETUP`, `STRUCTURE`, `REGIME`, `TEST` |
| `direction` | enum | `LONG`, `SHORT`, `NEUTRAL` |
| `timeframe` | enum | `1D`, `4H`, `1H`, `15M` |
| `source` | enum | `TRADINGVIEW`, `CUSTOM_SCRIPT`, `MANUAL` |

---

## ROUTING TABLE

| alert_type | Routed To |
|---|---|
| `BREAKOUT` | Breakout Confirmation (03) |
| `SETUP` | Structure Hunter (02) |
| `STRUCTURE` | Structure Hunter (02) |
| `REGIME` | Market Regime (05) |
| `TEST` | Journal Learning (08) only — no pipeline activation |

---

## FAILURE FLAG CODES

| Code | Meaning |
|---|---|
| `ASSET_NOT_WATCHLISTED` | Asset not in WATCHLIST_OFICIAL.md |
| `ALERT_TYPE_UNKNOWN` | Alert type cannot be mapped to known types |
| `PAYLOAD_INCOMPLETE` | Required fields missing from payload |
| `ALERT_STALE` | Alert age > 2 candle periods |
| `DUPLICATE_SUPPRESSED` | Identical alert within cooldown window |
| `READ_ONLY_BLOCK` | System in READ_ONLY mode — observation only |
| `FREEZE_BLOCK` | Pipeline in FREEZE state — routing blocked |
| `ZONE_INVALID` | Zone referenced in alert no longer active |
| `HIGH_VOLUME_ALERT_WINDOW` | >5 alerts in 30 min — anomaly flagged |

---

## EXAMPLE OUTPUT — ROUTED

```yaml
alert_radar_report:
  version: "1.0.0"
  received_at: "2026-04-15T09:03:12Z"
  processing_latency_ms: 48
  alert_status: "ROUTED"
  routed_to: "BREAKOUT_CONFIRMATION"
  rejection_reason: null
  normalized_alert:
    alert_id: "a7f3c1d2-4e88-4b01-9a7f-00e2b3c4d5e6"
    source: "TRADINGVIEW"
    asset: "ETHUSDT"
    alert_type: "BREAKOUT"
    direction: "LONG"
    timeframe: "4H"
    trigger_price: 3202.50
    trigger_timestamp: "2026-04-15T09:00:00Z"
    zone_id: "ZONE_001"
    age_candle_periods: 0.22
    watchlist_confirmed: true
    raw_message: "ETH broke above 3200 resistance on 4H"
  validation_checks:
    asset_on_watchlist:
      status: "PASS"
      value: "ETHUSDT"
    alert_type_recognized:
      status: "PASS"
      value: "BREAKOUT"
    payload_complete:
      status: "PASS"
      missing_fields: []
    staleness_check:
      status: "PASS"
      age_candle_periods: 0.22
      threshold: 2.0
    duplicate_check:
      status: "PASS"
      cooldown_window_min: 60
      last_identical_alert_at: null
    system_mode_check:
      status: "PASS"
      system_mode: "SIMULATE"
    zone_validity_check:
      status: "PASS"
      zone_id: "ZONE_001"
      zone_active: true
  failure_flags: []
  notes: "Clean alert. Routed to Breakout Confirmation for evaluation."
```
