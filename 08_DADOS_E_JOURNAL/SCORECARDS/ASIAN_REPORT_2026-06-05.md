---
schema_type: asian_scan_report
schema_version: 1.0
---
# Euru OS — Asian Session Scan Report
**Date:** 2026-06-05  
**Time:** 06:04 UTC  
**Session:** Asian (00:00 UTC open)  
**Protocol:** Aguiar Protocol Module 05 — Lateralization & Compression  
**Assets scanned:** 18  
**Mode:** READ_ONLY  
**BTC Master Filter (Module 01):** ACTIVE — BTC 4H state is WATCHLIST; altcoin GEM_ALERTs downgraded to WATCHLIST  

---

## System Health

```
TOTAL_ASSETS_REQUESTED:  18
TOTAL_ASSETS_FETCHED:    18
TOTAL_ASSETS_EXCLUDED:   0
FAILED_ASSETS:           none
STALE_ASSETS:            none
ANOMALOUS_ASSETS:        none
PIPELINE_STATUS:         HEALTHY
```

---

## Asset Summary

| Symbol | Price (USDT) | State |
|--------|-------------|-------|
| BTCUSDT |  62,169.9900 | **WATCHLIST** |
| ETHUSDT |   1,672.4200 | **NO_TRADE** |
| SOLUSDT |      65.9200 | **WATCHLIST** |
| BNBUSDT |     581.6000 | **WATCHLIST** |
| AVAXUSDT |       7.2210 | **NO_TRADE** |
| DOTUSDT |       0.9920 | **WATCHLIST** |
| LINKUSDT |       7.6130 | **WATCHLIST** |
| ADAUSDT |       0.1644 | **NO_TRADE** |
| XRPUSDT |       1.1204 | **WATCHLIST** |
| WLDUSDT |       0.5072 | **WATCHLIST** |
| SUIUSDT |       0.7244 | **WATCHLIST** |
| NEARUSDT |       2.1760 | **NO_TRADE** |
| INJUSDT |       5.2600 | **WATCHLIST** |
| ARBUSDT |       0.0840 | **WATCHLIST** |
| OPUSDT |       0.1055 | **WATCHLIST** |
| FETUSDT |       0.2093 | **WATCHLIST** |
| TAOUSDT |     201.0000 | **WATCHLIST** |
| RENDERUSDT |       1.7660 | **WATCHLIST** |

---

## Asian Session Assessments

### BTCUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: BTCUSDT
TIMEFRAME: 4H
DATE: 2026-06-05 06:04 UTC
PRICE: 62,169.9900
STATE: WATCHLIST
SIGNAL: Volume exhaustion only: ratio=0.43, no range compression detected
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: Volume exhaustion confirmed: last-3 avg 3,461 is 0.43x prior-5 avg 8,093 (threshold ≤0.7)
```

### ETHUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: ETHUSDT
TIMEFRAME: 4H
DATE: 2026-06-05 06:04 UTC
PRICE: 1,672.4200
STATE: NO_TRADE
SIGNAL: No compression or volume exhaustion (compression_pairs=0, vol_ratio=0.76)
REASON: Lateralization: No qualifying compression: 0 consecutive compressing pairs (need 2) | Volume: No volume exhaustion: last-3 avg 90,349 is 0.76x prior-5 avg 119,293 (need ≤0.7)
```

### SOLUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: SOLUSDT
TIMEFRAME: 4H
DATE: 2026-06-05 06:04 UTC
PRICE: 65.9200
STATE: WATCHLIST
SIGNAL: Volume exhaustion only: ratio=0.64, no range compression detected
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: Volume exhaustion confirmed: last-3 avg 570,250 is 0.64x prior-5 avg 896,950 (threshold ≤0.7)
```

### BNBUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: BNBUSDT
TIMEFRAME: 4H
DATE: 2026-06-05 06:04 UTC
PRICE: 581.6000
STATE: WATCHLIST
SIGNAL: Volume exhaustion only: ratio=0.48, no range compression detected
REASON: Lateralization: No qualifying compression: 0 consecutive compressing pairs (need 2) | Volume: Volume exhaustion confirmed: last-3 avg 36,566 is 0.48x prior-5 avg 76,285 (threshold ≤0.7)
```

### AVAXUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: AVAXUSDT
TIMEFRAME: 4H
DATE: 2026-06-05 06:04 UTC
PRICE: 7.2210
STATE: NO_TRADE
SIGNAL: No compression or volume exhaustion (compression_pairs=1, vol_ratio=0.71)
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: No volume exhaustion: last-3 avg 619,505 is 0.71x prior-5 avg 872,555 (need ≤0.7)
```

### DOTUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: DOTUSDT
TIMEFRAME: 4H
DATE: 2026-06-05 06:04 UTC
PRICE: 0.9920
STATE: WATCHLIST
SIGNAL: [BTC filter] Downgraded from GEM_ALERT — BTC state is WATCHLIST. COIL: 2 shrinking candles (60.0% compression) + volume at 0.61x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 2 consecutive compressing pairs (need 2), tightest range is 60.0% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 1,292,194 is 0.61x prior-5 avg 2,123,298 (threshold ≤0.7)
```

### LINKUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: LINKUSDT
TIMEFRAME: 4H
DATE: 2026-06-05 06:04 UTC
PRICE: 7.6130
STATE: WATCHLIST
SIGNAL: Volume exhaustion only: ratio=0.56, no range compression detected
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: Volume exhaustion confirmed: last-3 avg 675,278 is 0.56x prior-5 avg 1,202,845 (threshold ≤0.7)
```

### ADAUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: ADAUSDT
TIMEFRAME: 4H
DATE: 2026-06-05 06:04 UTC
PRICE: 0.1644
STATE: NO_TRADE
SIGNAL: No compression or volume exhaustion (compression_pairs=1, vol_ratio=1.36)
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: No volume exhaustion: last-3 avg 87,770,615 is 1.36x prior-5 avg 64,474,867 (need ≤0.7)
```

### XRPUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: XRPUSDT
TIMEFRAME: 4H
DATE: 2026-06-05 06:04 UTC
PRICE: 1.1204
STATE: WATCHLIST
SIGNAL: Volume exhaustion only: ratio=0.62, no range compression detected
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: Volume exhaustion confirmed: last-3 avg 21,174,333 is 0.62x prior-5 avg 34,145,251 (threshold ≤0.7)
```

### WLDUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: WLDUSDT
TIMEFRAME: 4H
DATE: 2026-06-05 06:04 UTC
PRICE: 0.5072
STATE: WATCHLIST
SIGNAL: Volume exhaustion only: ratio=0.64, no range compression detected
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: Volume exhaustion confirmed: last-3 avg 57,210,910 is 0.64x prior-5 avg 89,392,009 (threshold ≤0.7)
```

### SUIUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: SUIUSDT
TIMEFRAME: 4H
DATE: 2026-06-05 06:04 UTC
PRICE: 0.7244
STATE: WATCHLIST
SIGNAL: Volume exhaustion only: ratio=0.68, no range compression detected
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: Volume exhaustion confirmed: last-3 avg 16,686,926 is 0.68x prior-5 avg 24,533,157 (threshold ≤0.7)
```

### NEARUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: NEARUSDT
TIMEFRAME: 4H
DATE: 2026-06-05 06:04 UTC
PRICE: 2.1760
STATE: NO_TRADE
SIGNAL: No compression or volume exhaustion (compression_pairs=1, vol_ratio=0.71)
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: No volume exhaustion: last-3 avg 10,493,431 is 0.71x prior-5 avg 14,858,509 (need ≤0.7)
```

### INJUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: INJUSDT
TIMEFRAME: 4H
DATE: 2026-06-05 06:04 UTC
PRICE: 5.2600
STATE: WATCHLIST
SIGNAL: Volume exhaustion only: ratio=0.62, no range compression detected
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: Volume exhaustion confirmed: last-3 avg 394,355 is 0.62x prior-5 avg 631,932 (threshold ≤0.7)
```

### ARBUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: ARBUSDT
TIMEFRAME: 4H
DATE: 2026-06-05 06:04 UTC
PRICE: 0.0840
STATE: WATCHLIST
SIGNAL: Volume exhaustion only: ratio=0.47, no range compression detected
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: Volume exhaustion confirmed: last-3 avg 8,922,999 is 0.47x prior-5 avg 18,807,076 (threshold ≤0.7)
```

### OPUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: OPUSDT
TIMEFRAME: 4H
DATE: 2026-06-05 06:04 UTC
PRICE: 0.1055
STATE: WATCHLIST
SIGNAL: [BTC filter] Downgraded from GEM_ALERT — BTC state is WATCHLIST. COIL: 2 shrinking candles (44.9% compression) + volume at 0.37x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 2 consecutive compressing pairs (need 2), tightest range is 44.9% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 6,824,528 is 0.37x prior-5 avg 18,658,662 (threshold ≤0.7)
```

### FETUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: FETUSDT
TIMEFRAME: 4H
DATE: 2026-06-05 06:04 UTC
PRICE: 0.2093
STATE: WATCHLIST
SIGNAL: [BTC filter] Downgraded from GEM_ALERT — BTC state is WATCHLIST. COIL: 5 shrinking candles (59.9% compression) + volume at 0.37x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 5 consecutive compressing pairs (need 2), tightest range is 59.9% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 13,480,326 is 0.37x prior-5 avg 36,696,844 (threshold ≤0.7)
```

### TAOUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: TAOUSDT
TIMEFRAME: 4H
DATE: 2026-06-05 06:04 UTC
PRICE: 201.0000
STATE: WATCHLIST
SIGNAL: Compression only: 2 shrinking candles (59.8%), volume not yet exhausted (ratio=0.90)
REASON: Lateralization: Compression confirmed: 2 consecutive compressing pairs (need 2), tightest range is 59.8% of widest in window | Volume: No volume exhaustion: last-3 avg 31,147 is 0.90x prior-5 avg 34,428 (need ≤0.7)
```

### RENDERUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: RENDERUSDT
TIMEFRAME: 4H
DATE: 2026-06-05 06:04 UTC
PRICE: 1.7660
STATE: WATCHLIST
SIGNAL: Volume exhaustion only: ratio=0.39, no range compression detected
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: Volume exhaustion confirmed: last-3 avg 856,386 is 0.39x prior-5 avg 2,171,395 (threshold ≤0.7)
```

---

*Generated by euru_asian_scan.py — Euru OS READ_ONLY phase*