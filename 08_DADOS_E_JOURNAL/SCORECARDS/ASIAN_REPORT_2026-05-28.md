---
schema_type: asian_scan_report
schema_version: 1.0
---
# Euru OS — Asian Session Scan Report
**Date:** 2026-05-28  
**Time:** 00:00 UTC  
**Session:** Asian (00:00 UTC open)  
**Protocol:** Aguiar Protocol Module 05 — Lateralization & Compression  
**Assets scanned:** 18  
**Mode:** READ_ONLY  
**BTC Master Filter (Module 01):** ACTIVE — BTC 4H state is NO_TRADE; altcoin GEM_ALERTs downgraded to WATCHLIST  

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
| BTCUSDT |  74,438.8200 | **NO_TRADE** |
| ETHUSDT |   2,024.9800 | **NO_TRADE** |
| SOLUSDT |      82.4600 | **NO_TRADE** |
| BNBUSDT |     648.8300 | **WATCHLIST** |
| AVAXUSDT |       9.0450 | **NO_TRADE** |
| DOTUSDT |       1.2300 | **WATCHLIST** |
| LINKUSDT |       9.1360 | **WATCHLIST** |
| ADAUSDT |       0.2373 | **NO_TRADE** |
| XRPUSDT |       1.3076 | **NO_TRADE** |
| WLDUSDT |       0.3408 | **WATCHLIST** |
| SUIUSDT |       0.9599 | **WATCHLIST** |
| NEARUSDT |       2.4890 | **WATCHLIST** |
| INJUSDT |       5.4740 | **WATCHLIST** |
| ARBUSDT |       0.1071 | **NO_TRADE** |
| OPUSDT |       0.1236 | **NO_TRADE** |
| FETUSDT |       0.2433 | **WATCHLIST** |
| TAOUSDT |     266.7000 | **WATCHLIST** |
| RENDERUSDT |       2.1220 | **WATCHLIST** |

---

## Asian Session Assessments

### BTCUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: BTCUSDT
TIMEFRAME: 4H
DATE: 2026-05-28 00:00 UTC
PRICE: 74,438.8200
STATE: NO_TRADE
SIGNAL: No compression or volume exhaustion (compression_pairs=1, vol_ratio=0.77)
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: No volume exhaustion: last-3 avg 1,925 is 0.77x prior-5 avg 2,490 (need ≤0.7)
```

### ETHUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: ETHUSDT
TIMEFRAME: 4H
DATE: 2026-05-28 00:00 UTC
PRICE: 2,024.9800
STATE: NO_TRADE
SIGNAL: No compression or volume exhaustion (compression_pairs=1, vol_ratio=1.04)
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: No volume exhaustion: last-3 avg 37,017 is 1.04x prior-5 avg 35,538 (need ≤0.7)
```

### SOLUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: SOLUSDT
TIMEFRAME: 4H
DATE: 2026-05-28 00:00 UTC
PRICE: 82.4600
STATE: NO_TRADE
SIGNAL: No compression or volume exhaustion (compression_pairs=1, vol_ratio=0.97)
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: No volume exhaustion: last-3 avg 275,906 is 0.97x prior-5 avg 285,177 (need ≤0.7)
```

### BNBUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: BNBUSDT
TIMEFRAME: 4H
DATE: 2026-05-28 00:00 UTC
PRICE: 648.8300
STATE: WATCHLIST
SIGNAL: [BTC filter] Downgraded from GEM_ALERT — BTC state is NO_TRADE. COIL: 2 shrinking candles (1.0% compression) + volume at 0.64x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 2 consecutive compressing pairs (need 2), tightest range is 1.0% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 10,128 is 0.64x prior-5 avg 15,745 (threshold ≤0.7)
```

### AVAXUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: AVAXUSDT
TIMEFRAME: 4H
DATE: 2026-05-28 00:00 UTC
PRICE: 9.0450
STATE: NO_TRADE
SIGNAL: No compression or volume exhaustion (compression_pairs=1, vol_ratio=0.91)
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: No volume exhaustion: last-3 avg 211,075 is 0.91x prior-5 avg 232,819 (need ≤0.7)
```

### DOTUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: DOTUSDT
TIMEFRAME: 4H
DATE: 2026-05-28 00:00 UTC
PRICE: 1.2300
STATE: WATCHLIST
SIGNAL: Compression only: 3 shrinking candles (5.0%), volume not yet exhausted (ratio=0.73)
REASON: Lateralization: Compression confirmed: 3 consecutive compressing pairs (need 2), tightest range is 5.0% of widest in window | Volume: No volume exhaustion: last-3 avg 832,069 is 0.73x prior-5 avg 1,140,497 (need ≤0.7)
```

### LINKUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: LINKUSDT
TIMEFRAME: 4H
DATE: 2026-05-28 00:00 UTC
PRICE: 9.1360
STATE: WATCHLIST
SIGNAL: Compression only: 3 shrinking candles (1.6%), volume not yet exhausted (ratio=0.79)
REASON: Lateralization: Compression confirmed: 3 consecutive compressing pairs (need 2), tightest range is 1.6% of widest in window | Volume: No volume exhaustion: last-3 avg 247,844 is 0.79x prior-5 avg 312,589 (need ≤0.7)
```

### ADAUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: ADAUSDT
TIMEFRAME: 4H
DATE: 2026-05-28 00:00 UTC
PRICE: 0.2373
STATE: NO_TRADE
SIGNAL: No compression or volume exhaustion (compression_pairs=1, vol_ratio=0.92)
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: No volume exhaustion: last-3 avg 13,324,303 is 0.92x prior-5 avg 14,424,770 (need ≤0.7)
```

### XRPUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: XRPUSDT
TIMEFRAME: 4H
DATE: 2026-05-28 00:00 UTC
PRICE: 1.3076
STATE: NO_TRADE
SIGNAL: No compression or volume exhaustion (compression_pairs=1, vol_ratio=0.88)
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: No volume exhaustion: last-3 avg 9,674,782 is 0.88x prior-5 avg 10,971,687 (need ≤0.7)
```

### WLDUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: WLDUSDT
TIMEFRAME: 4H
DATE: 2026-05-28 00:00 UTC
PRICE: 0.3408
STATE: WATCHLIST
SIGNAL: [BTC filter] Downgraded from GEM_ALERT — BTC state is NO_TRADE. COIL: 2 shrinking candles (2.1% compression) + volume at 0.36x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 2 consecutive compressing pairs (need 2), tightest range is 2.1% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 10,211,018 is 0.36x prior-5 avg 28,680,284 (threshold ≤0.7)
```

### SUIUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: SUIUSDT
TIMEFRAME: 4H
DATE: 2026-05-28 00:00 UTC
PRICE: 0.9599
STATE: WATCHLIST
SIGNAL: Compression only: 2 shrinking candles (2.3%), volume not yet exhausted (ratio=0.98)
REASON: Lateralization: Compression confirmed: 2 consecutive compressing pairs (need 2), tightest range is 2.3% of widest in window | Volume: No volume exhaustion: last-3 avg 9,517,683 is 0.98x prior-5 avg 9,698,586 (need ≤0.7)
```

### NEARUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: NEARUSDT
TIMEFRAME: 4H
DATE: 2026-05-28 00:00 UTC
PRICE: 2.4890
STATE: WATCHLIST
SIGNAL: [BTC filter] Downgraded from GEM_ALERT — BTC state is NO_TRADE. COIL: 2 shrinking candles (1.7% compression) + volume at 0.69x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 2 consecutive compressing pairs (need 2), tightest range is 1.7% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 6,569,146 is 0.69x prior-5 avg 9,586,875 (threshold ≤0.7)
```

### INJUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: INJUSDT
TIMEFRAME: 4H
DATE: 2026-05-28 00:00 UTC
PRICE: 5.4740
STATE: WATCHLIST
SIGNAL: [BTC filter] Downgraded from GEM_ALERT — BTC state is NO_TRADE. COIL: 5 shrinking candles (1.3% compression) + volume at 0.50x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 5 consecutive compressing pairs (need 2), tightest range is 1.3% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 248,081 is 0.50x prior-5 avg 500,920 (threshold ≤0.7)
```

### ARBUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: ARBUSDT
TIMEFRAME: 4H
DATE: 2026-05-28 00:00 UTC
PRICE: 0.1071
STATE: NO_TRADE
SIGNAL: No compression or volume exhaustion (compression_pairs=1, vol_ratio=0.96)
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: No volume exhaustion: last-3 avg 5,340,189 is 0.96x prior-5 avg 5,588,189 (need ≤0.7)
```

### OPUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: OPUSDT
TIMEFRAME: 4H
DATE: 2026-05-28 00:00 UTC
PRICE: 0.1236
STATE: NO_TRADE
SIGNAL: No compression or volume exhaustion (compression_pairs=1, vol_ratio=1.14)
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: No volume exhaustion: last-3 avg 4,042,589 is 1.14x prior-5 avg 3,556,679 (need ≤0.7)
```

### FETUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: FETUSDT
TIMEFRAME: 4H
DATE: 2026-05-28 00:00 UTC
PRICE: 0.2433
STATE: WATCHLIST
SIGNAL: [BTC filter] Downgraded from GEM_ALERT — BTC state is NO_TRADE. COIL: 4 shrinking candles (2.6% compression) + volume at 0.54x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 4 consecutive compressing pairs (need 2), tightest range is 2.7% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 9,713,798 is 0.54x prior-5 avg 18,144,479 (threshold ≤0.7)
```

### TAOUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: TAOUSDT
TIMEFRAME: 4H
DATE: 2026-05-28 00:00 UTC
PRICE: 266.7000
STATE: WATCHLIST
SIGNAL: [BTC filter] Downgraded from GEM_ALERT — BTC state is NO_TRADE. COIL: 2 shrinking candles (1.6% compression) + volume at 0.70x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 2 consecutive compressing pairs (need 2), tightest range is 1.6% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 9,971 is 0.70x prior-5 avg 14,248 (threshold ≤0.7)
```

### RENDERUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: RENDERUSDT
TIMEFRAME: 4H
DATE: 2026-05-28 00:00 UTC
PRICE: 2.1220
STATE: WATCHLIST
SIGNAL: [BTC filter] Downgraded from GEM_ALERT — BTC state is NO_TRADE. COIL: 5 shrinking candles (2.5% compression) + volume at 0.44x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 5 consecutive compressing pairs (need 2), tightest range is 2.5% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 665,049 is 0.44x prior-5 avg 1,507,528 (threshold ≤0.7)
```

---

*Generated by euru_asian_scan.py — Euru OS READ_ONLY phase*