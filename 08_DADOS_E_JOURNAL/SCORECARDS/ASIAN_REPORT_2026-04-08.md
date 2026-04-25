---
schema_type: scorecard
schema_version: 1.0

scorecard_id: SC_ASSET_asian_2026-04-08
scorecard_date: 2026-04-08
period_type: daily
period_ref: 2026-W15
period_start: 2026-04-08
period_end: 2026-04-08

system_phase: simulate
scope: system
subject_id: euru_tos
subject_label: EURU_TOS — Asian Session Report

health_status: healthy
decision_status: keep
deviation_severity: none

closed_trades_count: 0
win_rate_pct: 0.0
average_rr: 0.0
expectancy: 0.0
prediction_accuracy_pct: 0.0

average_entry_score: 0.0
average_entry_score_winners: 0.0
average_entry_score_losers: 0.0

threshold_breach_count: 0
deviation_count: 0
blocked_trades_count: 0
watchlist_alert_count: 0

human_approval_required: false
linked_learning_report: null

tags:
  - asian_report
  - legacy_migrated
---

# Scorecard Snapshot

## Subject Summary
- Migrated from legacy format. See original content below.

## KPI Table
| metric | value | target | status |
|---|---:|---:|---|
| win_rate_pct | 0.0 | 50.0 | pending |
| average_rr | 0.0 | 2.0 | pending |
| expectancy | 0.0 | 0.01 | pending |

## Threshold Review
- none

## Deviations
- none

## Decision
- keep

## Action Plan
- Review and update from original content below.

---

## Original Content (Legacy)

# Euru OS — Asian Session Scan Report
**Date:** 2026-04-08  
**Time:** 22:00 UTC  
**Session:** Asian (00:00 UTC open)  
**Protocol:** Aguiar Protocol Module 05 — Lateralization & Compression  
**Assets scanned:** 17  
**Mode:** READ_ONLY  
**BTC Master Filter (Module 01):** ACTIVE — BTC 4H state is NO_TRADE; altcoin GEM_ALERTs downgraded to WATCHLIST  

---

## System Health

```
TOTAL_ASSETS_REQUESTED:  18
TOTAL_ASSETS_FETCHED:    17
TOTAL_ASSETS_EXCLUDED:   1
FAILED_ASSETS:           none
STALE_ASSETS:            MATICUSDT
ANOMALOUS_ASSETS:        none
PIPELINE_STATUS:         HEALTHY
```

---

## Asset Summary

| Symbol | Price (USDT) | State |
|--------|-------------|-------|
| BTCUSDT |  71,541.3000 | **NO_TRADE** |
| ETHUSDT |   2,213.6600 | **NO_TRADE** |
| SOLUSDT |      83.3700 | **NO_TRADE** |
| BNBUSDT |     606.4200 | **NO_TRADE** |
| AVAXUSDT |       9.1900 | **NO_TRADE** |
| DOTUSDT |       1.2860 | **NO_TRADE** |
| LINKUSDT |       9.0100 | **NO_TRADE** |
| ADAUSDT |       0.2542 | **NO_TRADE** |
| XRPUSDT |       1.3523 | **NO_TRADE** |
| SUIUSDT |       0.9282 | **NO_TRADE** |
| NEARUSDT |       1.3520 | **NO_TRADE** |
| INJUSDT |       2.9410 | **NO_TRADE** |
| ARBUSDT |       0.1052 | **NO_TRADE** |
| OPUSDT |       0.1166 | **NO_TRADE** |
| FETUSDT |       0.2412 | **NO_TRADE** |
| TAOUSDT |     325.6000 | **NO_TRADE** |
| RENDERUSDT |       2.0230 | **NO_TRADE** |

---

## Asian Session Assessments

### BTCUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: BTCUSDT
TIMEFRAME: 4H
DATE: 2026-04-08 22:00 UTC
PRICE: 71,541.3000
STATE: NO_TRADE
SIGNAL: NOT IMPLEMENTED — placeholder result
REASON: Lateralization detected: False (0 candles). Volume exhaustion detected: False (ratio=1.00).
```

### ETHUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: ETHUSDT
TIMEFRAME: 4H
DATE: 2026-04-08 22:00 UTC
PRICE: 2,213.6600
STATE: NO_TRADE
SIGNAL: NOT IMPLEMENTED — placeholder result
REASON: Lateralization detected: False (0 candles). Volume exhaustion detected: False (ratio=1.00).
```

### SOLUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: SOLUSDT
TIMEFRAME: 4H
DATE: 2026-04-08 22:00 UTC
PRICE: 83.3700
STATE: NO_TRADE
SIGNAL: NOT IMPLEMENTED — placeholder result
REASON: Lateralization detected: False (0 candles). Volume exhaustion detected: False (ratio=1.00).
```

### BNBUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: BNBUSDT
TIMEFRAME: 4H
DATE: 2026-04-08 22:00 UTC
PRICE: 606.4200
STATE: NO_TRADE
SIGNAL: NOT IMPLEMENTED — placeholder result
REASON: Lateralization detected: False (0 candles). Volume exhaustion detected: False (ratio=1.00).
```

### AVAXUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: AVAXUSDT
TIMEFRAME: 4H
DATE: 2026-04-08 22:00 UTC
PRICE: 9.1900
STATE: NO_TRADE
SIGNAL: NOT IMPLEMENTED — placeholder result
REASON: Lateralization detected: False (0 candles). Volume exhaustion detected: False (ratio=1.00).
```

### DOTUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: DOTUSDT
TIMEFRAME: 4H
DATE: 2026-04-08 22:00 UTC
PRICE: 1.2860
STATE: NO_TRADE
SIGNAL: NOT IMPLEMENTED — placeholder result
REASON: Lateralization detected: False (0 candles). Volume exhaustion detected: False (ratio=1.00).
```

### LINKUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: LINKUSDT
TIMEFRAME: 4H
DATE: 2026-04-08 22:00 UTC
PRICE: 9.0100
STATE: NO_TRADE
SIGNAL: NOT IMPLEMENTED — placeholder result
REASON: Lateralization detected: False (0 candles). Volume exhaustion detected: False (ratio=1.00).
```

### ADAUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: ADAUSDT
TIMEFRAME: 4H
DATE: 2026-04-08 22:00 UTC
PRICE: 0.2542
STATE: NO_TRADE
SIGNAL: NOT IMPLEMENTED — placeholder result
REASON: Lateralization detected: False (0 candles). Volume exhaustion detected: False (ratio=1.00).
```

### XRPUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: XRPUSDT
TIMEFRAME: 4H
DATE: 2026-04-08 22:00 UTC
PRICE: 1.3523
STATE: NO_TRADE
SIGNAL: NOT IMPLEMENTED — placeholder result
REASON: Lateralization detected: False (0 candles). Volume exhaustion detected: False (ratio=1.00).
```

### SUIUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: SUIUSDT
TIMEFRAME: 4H
DATE: 2026-04-08 22:00 UTC
PRICE: 0.9282
STATE: NO_TRADE
SIGNAL: NOT IMPLEMENTED — placeholder result
REASON: Lateralization detected: False (0 candles). Volume exhaustion detected: False (ratio=1.00).
```

### NEARUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: NEARUSDT
TIMEFRAME: 4H
DATE: 2026-04-08 22:00 UTC
PRICE: 1.3520
STATE: NO_TRADE
SIGNAL: NOT IMPLEMENTED — placeholder result
REASON: Lateralization detected: False (0 candles). Volume exhaustion detected: False (ratio=1.00).
```

### INJUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: INJUSDT
TIMEFRAME: 4H
DATE: 2026-04-08 22:00 UTC
PRICE: 2.9410
STATE: NO_TRADE
SIGNAL: NOT IMPLEMENTED — placeholder result
REASON: Lateralization detected: False (0 candles). Volume exhaustion detected: False (ratio=1.00).
```

### ARBUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: ARBUSDT
TIMEFRAME: 4H
DATE: 2026-04-08 22:00 UTC
PRICE: 0.1052
STATE: NO_TRADE
SIGNAL: NOT IMPLEMENTED — placeholder result
REASON: Lateralization detected: False (0 candles). Volume exhaustion detected: False (ratio=1.00).
```

### OPUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: OPUSDT
TIMEFRAME: 4H
DATE: 2026-04-08 22:00 UTC
PRICE: 0.1166
STATE: NO_TRADE
SIGNAL: NOT IMPLEMENTED — placeholder result
REASON: Lateralization detected: False (0 candles). Volume exhaustion detected: False (ratio=1.00).
```

### FETUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: FETUSDT
TIMEFRAME: 4H
DATE: 2026-04-08 22:00 UTC
PRICE: 0.2412
STATE: NO_TRADE
SIGNAL: NOT IMPLEMENTED — placeholder result
REASON: Lateralization detected: False (0 candles). Volume exhaustion detected: False (ratio=1.00).
```

### TAOUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: TAOUSDT
TIMEFRAME: 4H
DATE: 2026-04-08 22:00 UTC
PRICE: 325.6000
STATE: NO_TRADE
SIGNAL: NOT IMPLEMENTED — placeholder result
REASON: Lateralization detected: False (0 candles). Volume exhaustion detected: False (ratio=1.00).
```

### RENDERUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: RENDERUSDT
TIMEFRAME: 4H
DATE: 2026-04-08 22:00 UTC
PRICE: 2.0230
STATE: NO_TRADE
SIGNAL: NOT IMPLEMENTED — placeholder result
REASON: Lateralization detected: False (0 candles). Volume exhaustion detected: False (ratio=1.00).
```

---

*Generated by euru_asian_scan.py — Euru OS READ_ONLY phase*
