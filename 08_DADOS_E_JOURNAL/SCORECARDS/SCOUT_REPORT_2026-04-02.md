---
schema_type: scorecard
schema_version: 1.0

scorecard_id: SC_ASSET_scout_2026-04-02
scorecard_date: 2026-04-02
period_type: daily
period_ref: 2026-W14
period_start: 2026-04-02
period_end: 2026-04-02

system_phase: simulate
scope: system
subject_id: euru_tos
subject_label: EURU_TOS — Scout Report

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
  - scout_report
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

# Euru OS — Morning Scan Report
**Date:** 2026-04-02  
**Time:** 08:20 UTC  
**Mode:** READ_ONLY  
**BTC Master Filter (Module 01):** ACTIVE — BTC trend is SIDEWAYS; altcoin SETUP signals downgraded to WATCHLIST  

---

## Price Summary

| Symbol | Price (USDT) | 24h Change | vs 7D Avg | State |
|--------|-------------|------------|-----------|-------|
| BTCUSDT |    66,692.88 | -2.76% | -0.84% | **NO_TRADE** |
| ETHUSDT |     2,049.93 | -3.82% | +0.31% | **NO_TRADE** |
| SOLUSDT |        79.44 | -5.11% | -4.14% | **WATCHLIST** |
| BNBUSDT |       590.04 | -4.18% | -3.89% | **WATCHLIST** |
| AVAXUSDT |         8.70 | -6.25% | -1.93% | **WATCHLIST** |
| DOTUSDT |         1.22 | -4.53% | -3.64% | **WATCHLIST** |
| LINKUSDT |         8.54 | -5.84% | -1.48% | **WATCHLIST** |
| ADAUSDT |         0.24 | -3.47% | -2.74% | **WATCHLIST** |
| XRPUSDT |         1.31 | -2.89% | -1.66% | **WATCHLIST** |
| MATICUSDT |         0.38 | -0.29% | +0.56% | **NO_TRADE** |

---

## Scout Assessments

### BTCUSDT

```
AGENT: Scout
SYMBOL: BTCUSDT
TIMEFRAME: 1D
DATE: 2026-04-02 08:20 UTC
TREND: SIDEWAYS
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 71,436.82 | S: 65,000.00 | 7D_AVG: 67,258.76
INVALIDATION: Break outside week range (65,000.00 – 71,436.82)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 66,692.88 is -0.84% vs 7D avg 67,258.76. 24h change: -2.76%. Trend: SIDEWAYS. 24h range: 4.43% vs avg daily range 3.63%.
```

### ETHUSDT

```
AGENT: Scout
SYMBOL: ETHUSDT
TIMEFRAME: 1D
DATE: 2026-04-02 08:20 UTC
TREND: SIDEWAYS
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 2,172.19 | S: 1,938.82 | 7D_AVG: 2,043.55
INVALIDATION: Break outside week range (1,938.82 – 2,172.19)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 2,049.93 is +0.31% vs 7D avg 2,043.55. 24h change: -3.82%. Trend: SIDEWAYS. 24h range: 6.30% vs avg daily range 4.82%.
```

### SOLUSDT

```
AGENT: Scout
SYMBOL: SOLUSDT
TIMEFRAME: 1D
DATE: 2026-04-02 08:20 UTC
TREND: BEARISH
STRUCTURE: AT_WEEKLY_LOW — support zone
COMPRESSION: NO — normal range
KEY_LEVELS: R: 91.98 | S: 78.96 | 7D_AVG: 82.87
INVALIDATION: Close above 7D_AVG (82.87)
STATE: WATCHLIST
SIGNAL: [BTC filter] Downgraded from SETUP — BTC trend is SIDEWAYS. Price -4.14% from 7D avg with aligned trend
REASON: Current price 79.44 is -4.14% vs 7D avg 82.87. 24h change: -5.11%. Trend: BEARISH. 24h range: 10.51% vs avg daily range 5.65%.
```

### BNBUSDT

```
AGENT: Scout
SYMBOL: BNBUSDT
TIMEFRAME: 1D
DATE: 2026-04-02 08:20 UTC
TREND: BEARISH
STRUCTURE: AT_WEEKLY_LOW — support zone
COMPRESSION: NO — normal range
KEY_LEVELS: R: 648.47 | S: 596.42 | 7D_AVG: 613.93
INVALIDATION: Close above 7D_AVG (613.93)
STATE: WATCHLIST
SIGNAL: [BTC filter] Downgraded from SETUP — BTC trend is SIDEWAYS. Price -3.89% from 7D avg with aligned trend
REASON: Current price 590.04 is -3.89% vs 7D avg 613.93. 24h change: -4.18%. Trend: BEARISH. 24h range: 5.45% vs avg daily range 3.00%.
```

### AVAXUSDT

```
AGENT: Scout
SYMBOL: AVAXUSDT
TIMEFRAME: 1D
DATE: 2026-04-02 08:20 UTC
TREND: BEARISH
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 9.69 | S: 8.37 | 7D_AVG: 8.87
INVALIDATION: Close above 7D_AVG (8.87)
STATE: WATCHLIST
SIGNAL: Price -1.93% from 7D avg — monitoring for continuation
REASON: Current price 8.70 is -1.93% vs 7D avg 8.87. 24h change: -6.25%. Trend: BEARISH. 24h range: 7.59% vs avg daily range 5.52%.
```

### DOTUSDT

```
AGENT: Scout
SYMBOL: DOTUSDT
TIMEFRAME: 1D
DATE: 2026-04-02 08:20 UTC
TREND: BEARISH
STRUCTURE: AT_WEEKLY_LOW — support zone
COMPRESSION: NO — normal range
KEY_LEVELS: R: 1.37 | S: 1.22 | 7D_AVG: 1.27
INVALIDATION: Close above 7D_AVG (1.27)
STATE: WATCHLIST
SIGNAL: [BTC filter] Downgraded from SETUP — BTC trend is SIDEWAYS. Price -3.64% from 7D avg with aligned trend
REASON: Current price 1.22 is -3.64% vs 7D avg 1.27. 24h change: -4.53%. Trend: BEARISH. 24h range: 6.87% vs avg daily range 4.60%.
```

### LINKUSDT

```
AGENT: Scout
SYMBOL: LINKUSDT
TIMEFRAME: 1D
DATE: 2026-04-02 08:20 UTC
TREND: BEARISH
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 9.39 | S: 8.20 | 7D_AVG: 8.67
INVALIDATION: Close above 7D_AVG (8.67)
STATE: WATCHLIST
SIGNAL: Price -1.48% from 7D avg — monitoring for continuation
REASON: Current price 8.54 is -1.48% vs 7D avg 8.67. 24h change: -5.84%. Trend: BEARISH. 24h range: 7.49% vs avg daily range 5.23%.
```

### ADAUSDT

```
AGENT: Scout
SYMBOL: ADAUSDT
TIMEFRAME: 1D
DATE: 2026-04-02 08:20 UTC
TREND: BEARISH
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 0.27 | S: 0.23 | 7D_AVG: 0.25
INVALIDATION: Close above 7D_AVG (0.25)
STATE: WATCHLIST
SIGNAL: Price -2.74% from 7D avg — monitoring for continuation
REASON: Current price 0.24 is -2.74% vs 7D avg 0.25. 24h change: -3.47%. Trend: BEARISH. 24h range: 6.95% vs avg daily range 5.58%.
```

### XRPUSDT

```
AGENT: Scout
SYMBOL: XRPUSDT
TIMEFRAME: 1D
DATE: 2026-04-02 08:20 UTC
TREND: BEARISH
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 1.42 | S: 1.30 | 7D_AVG: 1.34
INVALIDATION: Close above 7D_AVG (1.34)
STATE: WATCHLIST
SIGNAL: Price -1.66% from 7D avg — monitoring for continuation
REASON: Current price 1.31 is -1.66% vs 7D avg 1.34. 24h change: -2.89%. Trend: BEARISH. 24h range: 4.81% vs avg daily range 3.79%.
```

### MATICUSDT

```
AGENT: Scout
SYMBOL: MATICUSDT
TIMEFRAME: 1D
DATE: 2026-04-02 08:20 UTC
TREND: SIDEWAYS
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: YES — range contracting
KEY_LEVELS: R: 0.41 | S: 0.35 | 7D_AVG: 0.38
INVALIDATION: Break outside week range (0.35 – 0.41)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 0.38 is +0.56% vs 7D avg 0.38. 24h change: -0.29%. Trend: SIDEWAYS. 24h range: 0.84% vs avg daily range 6.16%.
```

---

*Generated by euru_morning_scan.py — Euru OS READ_ONLY phase*
