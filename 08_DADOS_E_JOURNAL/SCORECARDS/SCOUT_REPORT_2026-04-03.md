---
schema_type: scorecard
schema_version: 1.0

scorecard_id: SC_ASSET_scout_2026-04-03
scorecard_date: 2026-04-03
period_type: daily
period_ref: 2026-W14
period_start: 2026-04-03
period_end: 2026-04-03

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
**Date:** 2026-04-03  
**Time:** 05:22 UTC  
**Mode:** READ_ONLY  
**BTC Master Filter (Module 01):** ACTIVE — BTC trend is SIDEWAYS; altcoin SETUP signals downgraded to WATCHLIST  

---

## Price Summary

| Symbol | Price (USDT) | 24h Change | vs 7D Avg | State |
|--------|-------------|------------|-----------|-------|
| BTCUSDT |    66,509.43 | +0.04% | -0.71% | **NO_TRADE** |
| ETHUSDT |     2,050.88 | +0.14% | +0.38% | **NO_TRADE** |
| SOLUSDT |        79.20 | +0.48% | -3.16% | **WATCHLIST** |
| BNBUSDT |       585.53 | -0.83% | -3.61% | **WATCHLIST** |
| AVAXUSDT |         8.82 | +1.38% | +0.00% | **NO_TRADE** |
| DOTUSDT |         1.24 | +1.97% | -1.36% | **WATCHLIST** |
| LINKUSDT |         8.66 | +1.64% | +0.36% | **NO_TRADE** |
| ADAUSDT |         0.24 | +2.10% | -0.43% | **NO_TRADE** |
| XRPUSDT |         1.32 | +0.48% | -1.02% | **WATCHLIST** |
| MATICUSDT |         0.38 | -0.29% | +0.56% | **NO_TRADE** |

---

## News Sentinel

```
AGENT: News Sentinel
DATE: 2026-04-03 05:22 UTC
OVERALL_SEVERITY: HIGH
TOP_HEADLINES:
  1. [HIGH] Rocky US economy, private credit stress, war, impact Bitcoin’s odds for $75K rally
  2. [HIGH] Canada’s bid to ban crypto donations highlights transparency issue
  3. [LOW] Tokenization makes finance more efficient but introduces risks: IMF
```

---

## Scout Assessments

### BTCUSDT

```
AGENT: Scout
SYMBOL: BTCUSDT
TIMEFRAME: 1D
DATE: 2026-04-03 05:22 UTC
TREND: SIDEWAYS
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 69,310.00 | S: 65,000.00 | 7D_AVG: 66,984.71
INVALIDATION: Break outside week range (65,000.00 – 69,310.00)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 66,509.43 is -0.71% vs 7D avg 66,984.71. 24h change: +0.04%. Trend: SIDEWAYS. 24h range: 2.58% vs avg daily range 3.57%.
```

### ETHUSDT

```
AGENT: Scout
SYMBOL: ETHUSDT
TIMEFRAME: 1D
DATE: 2026-04-03 05:22 UTC
TREND: SIDEWAYS
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: YES — range contracting
KEY_LEVELS: R: 2,167.85 | S: 1,938.82 | 7D_AVG: 2,043.08
INVALIDATION: Break outside week range (1,938.82 – 2,167.85)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 2,050.88 is +0.38% vs 7D avg 2,043.08. 24h change: +0.14%. Trend: SIDEWAYS. 24h range: 2.95% vs avg daily range 4.86%.
```

### SOLUSDT

```
AGENT: Scout
SYMBOL: SOLUSDT
TIMEFRAME: 1D
DATE: 2026-04-03 05:22 UTC
TREND: MIXED
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 87.04 | S: 76.70 | 7D_AVG: 81.79
INVALIDATION: Break outside week range (76.70 – 87.04)
STATE: WATCHLIST
SIGNAL: Price -3.16% from 7D avg — monitoring for continuation
REASON: Current price 79.20 is -3.16% vs 7D avg 81.79. 24h change: +0.48%. Trend: MIXED. 24h range: 4.02% vs avg daily range 5.49%.
```

### BNBUSDT

```
AGENT: Scout
SYMBOL: BNBUSDT
TIMEFRAME: 1D
DATE: 2026-04-03 05:22 UTC
TREND: BEARISH
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 631.87 | S: 570.31 | 7D_AVG: 607.45
INVALIDATION: Close above 7D_AVG (607.45)
STATE: WATCHLIST
SIGNAL: [BTC filter] Downgraded from SETUP — BTC trend is SIDEWAYS. Price -3.61% from 7D avg with aligned trend
REASON: Current price 585.53 is -3.61% vs 7D avg 607.45. 24h change: -0.83%. Trend: BEARISH. 24h range: 3.79% vs avg daily range 3.48%.
```

### AVAXUSDT

```
AGENT: Scout
SYMBOL: AVAXUSDT
TIMEFRAME: 1D
DATE: 2026-04-03 05:22 UTC
TREND: SIDEWAYS
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: YES — range contracting
KEY_LEVELS: R: 9.48 | S: 8.37 | 7D_AVG: 8.82
INVALIDATION: Break outside week range (8.37 – 9.48)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 8.82 is +0.00% vs 7D avg 8.82. 24h change: +1.38%. Trend: SIDEWAYS. 24h range: 2.61% vs avg daily range 5.35%.
```

### DOTUSDT

```
AGENT: Scout
SYMBOL: DOTUSDT
TIMEFRAME: 1D
DATE: 2026-04-03 05:22 UTC
TREND: MIXED
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: YES — range contracting
KEY_LEVELS: R: 1.34 | S: 1.20 | 7D_AVG: 1.26
INVALIDATION: Break outside week range (1.20 – 1.34)
STATE: WATCHLIST
SIGNAL: Price -1.36% from 7D avg — monitoring for continuation
REASON: Current price 1.24 is -1.36% vs 7D avg 1.26. 24h change: +1.97%. Trend: MIXED. 24h range: 3.23% vs avg daily range 4.61%.
```

### LINKUSDT

```
AGENT: Scout
SYMBOL: LINKUSDT
TIMEFRAME: 1D
DATE: 2026-04-03 05:22 UTC
TREND: SIDEWAYS
STRUCTURE: ABOVE_7D_AVG — upper half of range
COMPRESSION: YES — range contracting
KEY_LEVELS: R: 9.20 | S: 8.20 | 7D_AVG: 8.63
INVALIDATION: Break outside week range (8.20 – 9.20)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 8.66 is +0.36% vs 7D avg 8.63. 24h change: +1.64%. Trend: SIDEWAYS. 24h range: 3.12% vs avg daily range 5.28%.
```

### ADAUSDT

```
AGENT: Scout
SYMBOL: ADAUSDT
TIMEFRAME: 1D
DATE: 2026-04-03 05:22 UTC
TREND: SIDEWAYS
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: YES — range contracting
KEY_LEVELS: R: 0.26 | S: 0.23 | 7D_AVG: 0.24
INVALIDATION: Break outside week range (0.23 – 0.26)
STATE: NO_TRADE
SIGNAL: Price within ±1.0% of 7D avg — no clear bias
REASON: Current price 0.24 is -0.43% vs 7D avg 0.24. 24h change: +2.10%. Trend: SIDEWAYS. 24h range: 3.55% vs avg daily range 5.50%.
```

### XRPUSDT

```
AGENT: Scout
SYMBOL: XRPUSDT
TIMEFRAME: 1D
DATE: 2026-04-03 05:22 UTC
TREND: MIXED
STRUCTURE: BELOW_7D_AVG — lower half of range
COMPRESSION: NO — normal range
KEY_LEVELS: R: 1.37 | S: 1.28 | 7D_AVG: 1.33
INVALIDATION: Break outside week range (1.28 – 1.37)
STATE: WATCHLIST
SIGNAL: Price -1.02% from 7D avg — monitoring for continuation
REASON: Current price 1.32 is -1.02% vs 7D avg 1.33. 24h change: +0.48%. Trend: MIXED. 24h range: 3.32% vs avg daily range 3.78%.
```

### MATICUSDT

```
AGENT: Scout
SYMBOL: MATICUSDT
TIMEFRAME: 1D
DATE: 2026-04-03 05:22 UTC
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
