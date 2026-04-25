# ALERT_RADAR — OUTPUT_FORMAT.md
# Version: 1.0.0 | Layer: BREAKOUT_LAYER | Agent: 04_ALERT_RADAR
# Created: 2026-04-15 | Status: ACTIVE

---

## OUTPUT SCHEMA

```yaml
alert_radar_report:
  version: "1.0.0"
  received_at: string              # ISO-8601 UTC
  processing_latency_ms: int

  alert_status: string             # see STATUS VALUES
  routed_to: string | null         # "STRUCTURE_HUNTER" | null
  rejection_reason: string | null

  normalized_alert:
    alert_id: string               # UUID
    source: string                 # TRADINGVIEW | CUSTOM_SCRIPT | MANUAL
    asset: string
    alert_type: string             # BREAKOUT | SETUP | STRUCTURE | REGIME
    direction: string              # LONG | SHORT | NEUTRAL
    timeframe: string              # 1D | 4H | 1H | 15M
    trigger_price: float
    trigger_timestamp: string      # ISO-8601 UTC
    zone_id: string | null
    age_candle_periods: float
    raw_message: string

  validation_checks:
    symbol_on_watchlist:
      status: string               # PASS | FAIL
      asset: string

    asset_not_prohibited:
      status: string               # PASS | FAIL — FAIL = immediate reject
      list_name: string            # "LISTA_PROIBIDA" | "NONE"

    payload_complete:
      status: string               # PASS | FAIL
      missing_fields: list[string]

    alert_type_parseable:
      status: string               # PASS | FAIL
      detected_type: string | null

    staleness_check:
      status: string               # PASS | FAIL
      age_candle_periods: float
      threshold: float             # 2.0

    duplicate_check:
      status: string               # PASS | FAIL
      cooldown_window_min: int
      last_match_at: string | null # ISO-8601 UTC | null

    system_mode_check:
      status: string               # PASS | OBSERVATION_ONLY | FREEZE_BLOCK
      system_mode: string

  failure_flags: list[FailureFlag]
  notes: string                    # optional, max 60 words
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
| `ROUTED` | Alert passed all checks — forwarded to Structure Hunter |
| `REJECTED` | One or more validation checks failed — not forwarded |
| `OBSERVATION_ONLY` | System in READ_ONLY mode — logged but pipeline not activated |
| `DUPLICATE` | Identical alert within cooldown window — suppressed |
| `FREEZE_BLOCK` | Pipeline in FREEZE state — alert logged, routing blocked |
| `INVALID` | Payload missing required fields — cannot normalize |

---

## ROUTING TABLE

| alert_type | Destination |
|---|---|
| `BREAKOUT` | Structure Hunter (02_STRUCTURE_HUNTER) |
| `SETUP` | Structure Hunter (02_STRUCTURE_HUNTER) |
| `STRUCTURE` | Structure Hunter (02_STRUCTURE_HUNTER) |
| `REGIME` | Not routed within BREAKOUT_LAYER — log only |

---

## COOLDOWN DEFAULTS (configurable)

| Timeframe | Cooldown Window |
|---|---|
| 15M | 15 min |
| 1H | 60 min |
| 4H | 60 min |
| 1D | 240 min |

---

## CONFIDENCE LEVELS

Alert Radar does not assign a confidence score to signals — confidence assessment is downstream (Breakout Confirmation). Alert Radar outputs only a binary routing decision per check (PASS/FAIL).

---

## FAILURE FLAG CODES

| Code | Meaning |
|---|---|
| `ASSET_NOT_WATCHLISTED` | Symbol not on WATCHLIST_OFICIAL |
| `ASSET_PROHIBITED` | Symbol on LISTA_PROIBIDA |
| `PAYLOAD_INCOMPLETE` | Required fields missing |
| `ALERT_TYPE_UNKNOWN` | Type cannot be parsed from payload |
| `ALERT_STALE` | Age > 2 candle periods |
| `DUPLICATE_SUPPRESSED` | Identical alert within cooldown |
| `FREEZE_BLOCK` | Pipeline in FREEZE state |
| `READ_ONLY_BLOCK` | System in READ_ONLY mode |
| `HIGH_FREQUENCY_WINDOW` | > 5 alerts in 30 min — anomaly flagged |

---

## EXAMPLE — ROUTED

```yaml
alert_radar_report:
  version: "1.0.0"
  received_at: "2026-04-15T09:03:12Z"
  processing_latency_ms: 44
  alert_status: "ROUTED"
  routed_to: "STRUCTURE_HUNTER"
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
    zone_id: "Z001"
    age_candle_periods: 0.22
    raw_message: "ETH broke above 3200 resistance on 4H"
  validation_checks:
    symbol_on_watchlist:
      status: "PASS"
      asset: "ETHUSDT"
    asset_not_prohibited:
      status: "PASS"
      list_name: "NONE"
    payload_complete:
      status: "PASS"
      missing_fields: []
    alert_type_parseable:
      status: "PASS"
      detected_type: "BREAKOUT"
    staleness_check:
      status: "PASS"
      age_candle_periods: 0.22
      threshold: 2.0
    duplicate_check:
      status: "PASS"
      cooldown_window_min: 60
      last_match_at: null
    system_mode_check:
      status: "PASS"
      system_mode: "SIMULATE"
  failure_flags: []
  notes: "All checks passed. Forwarding to Structure Hunter."
```
