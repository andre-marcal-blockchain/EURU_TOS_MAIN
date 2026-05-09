---
schema_type: asian_scan_report
schema_version: 1.0
---
# Euru OS — Asian Session Scan Report
**Date:** 2026-05-09  
**Time:** 00:00 UTC  
**Session:** Asian (00:00 UTC open)  
**Protocol:** Aguiar Protocol Module 05 — Lateralization & Compression  
**Assets scanned:** 18  
**Mode:** READ_ONLY  
**BTC Master Filter (Module 01):** INACTIVE — BTC 4H state is GEM_ALERT; signals unmodified  

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
| BTCUSDT |  80,193.1800 | **GEM_ALERT** |
| ETHUSDT |   2,307.0700 | **GEM_ALERT** |
| SOLUSDT |      92.0200 | **WATCHLIST** |
| BNBUSDT |     649.3700 | **GEM_ALERT** |
| AVAXUSDT |       9.9100 | **WATCHLIST** |
| DOTUSDT |       1.3740 | **WATCHLIST** |
| LINKUSDT |      10.3400 | **WATCHLIST** |
| ADAUSDT |       0.2736 | **NO_TRADE** |
| XRPUSDT |       1.4182 | **WATCHLIST** |
| WLDUSDT |       0.2736 | **WATCHLIST** |
| SUIUSDT |       1.0217 | **WATCHLIST** |
| NEARUSDT |       1.5980 | **GEM_ALERT** |
| INJUSDT |       4.2280 | **GEM_ALERT** |
| ARBUSDT |       0.1428 | **WATCHLIST** |
| OPUSDT |       0.1720 | **NO_TRADE** |
| FETUSDT |       0.2337 | **WATCHLIST** |
| TAOUSDT |     316.5000 | **GEM_ALERT** |
| RENDERUSDT |       2.0500 | **WATCHLIST** |

---

## Asian Session Assessments

### BTCUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: BTCUSDT
TIMEFRAME: 4H
DATE: 2026-05-09 00:00 UTC
PRICE: 80,193.1800
STATE: GEM_ALERT
SIGNAL: COIL: 3 shrinking candles (0.0% compression) + volume at 0.56x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 3 consecutive compressing pairs (need 2), tightest range is 0.0% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 1,469 is 0.56x prior-5 avg 2,627 (threshold ≤0.7)
```

### ETHUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: ETHUSDT
TIMEFRAME: 4H
DATE: 2026-05-09 00:00 UTC
PRICE: 2,307.0700
STATE: GEM_ALERT
SIGNAL: COIL: 3 shrinking candles (0.0% compression) + volume at 0.67x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 3 consecutive compressing pairs (need 2), tightest range is 0.0% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 47,286 is 0.67x prior-5 avg 70,256 (threshold ≤0.7)
```

### SOLUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: SOLUSDT
TIMEFRAME: 4H
DATE: 2026-05-09 00:00 UTC
PRICE: 92.0200
STATE: WATCHLIST
SIGNAL: Compression only: 2 shrinking candles (0.3%), volume not yet exhausted (ratio=1.16)
REASON: Lateralization: Compression confirmed: 2 consecutive compressing pairs (need 2), tightest range is 0.3% of widest in window | Volume: No volume exhaustion: last-3 avg 407,258 is 1.16x prior-5 avg 352,204 (need ≤0.7)
```

### BNBUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: BNBUSDT
TIMEFRAME: 4H
DATE: 2026-05-09 00:00 UTC
PRICE: 649.3700
STATE: GEM_ALERT
SIGNAL: COIL: 5 shrinking candles (0.0% compression) + volume at 0.44x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 5 consecutive compressing pairs (need 2), tightest range is 0.0% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 9,339 is 0.44x prior-5 avg 21,199 (threshold ≤0.7)
```

### AVAXUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: AVAXUSDT
TIMEFRAME: 4H
DATE: 2026-05-09 00:00 UTC
PRICE: 9.9100
STATE: WATCHLIST
SIGNAL: Compression only: 3 shrinking candles (0.0%), volume not yet exhausted (ratio=1.15)
REASON: Lateralization: Compression confirmed: 3 consecutive compressing pairs (need 2), tightest range is 0.0% of widest in window | Volume: No volume exhaustion: last-3 avg 410,402 is 1.15x prior-5 avg 357,793 (need ≤0.7)
```

### DOTUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: DOTUSDT
TIMEFRAME: 4H
DATE: 2026-05-09 00:00 UTC
PRICE: 1.3740
STATE: WATCHLIST
SIGNAL: Compression only: 3 shrinking candles (0.0%), volume not yet exhausted (ratio=1.01)
REASON: Lateralization: Compression confirmed: 3 consecutive compressing pairs (need 2), tightest range is 0.0% of widest in window | Volume: No volume exhaustion: last-3 avg 1,062,938 is 1.01x prior-5 avg 1,052,798 (need ≤0.7)
```

### LINKUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: LINKUSDT
TIMEFRAME: 4H
DATE: 2026-05-09 00:00 UTC
PRICE: 10.3400
STATE: WATCHLIST
SIGNAL: Compression only: 2 shrinking candles (2.1%), volume not yet exhausted (ratio=2.16)
REASON: Lateralization: Compression confirmed: 2 consecutive compressing pairs (need 2), tightest range is 2.1% of widest in window | Volume: No volume exhaustion: last-3 avg 909,854 is 2.16x prior-5 avg 421,567 (need ≤0.7)
```

### ADAUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: ADAUSDT
TIMEFRAME: 4H
DATE: 2026-05-09 00:00 UTC
PRICE: 0.2736
STATE: NO_TRADE
SIGNAL: No compression or volume exhaustion (compression_pairs=1, vol_ratio=1.55)
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: No volume exhaustion: last-3 avg 17,267,141 is 1.55x prior-5 avg 11,116,243 (need ≤0.7)
```

### XRPUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: XRPUSDT
TIMEFRAME: 4H
DATE: 2026-05-09 00:00 UTC
PRICE: 1.4182
STATE: WATCHLIST
SIGNAL: Compression only: 2 shrinking candles (0.3%), volume not yet exhausted (ratio=1.07)
REASON: Lateralization: Compression confirmed: 2 consecutive compressing pairs (need 2), tightest range is 0.3% of widest in window | Volume: No volume exhaustion: last-3 avg 9,782,629 is 1.07x prior-5 avg 9,120,087 (need ≤0.7)
```

### WLDUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: WLDUSDT
TIMEFRAME: 4H
DATE: 2026-05-09 00:00 UTC
PRICE: 0.2736
STATE: WATCHLIST
SIGNAL: Compression only: 3 shrinking candles (1.2%), volume not yet exhausted (ratio=1.59)
REASON: Lateralization: Compression confirmed: 3 consecutive compressing pairs (need 2), tightest range is 1.2% of widest in window | Volume: No volume exhaustion: last-3 avg 9,849,508 is 1.59x prior-5 avg 6,187,786 (need ≤0.7)
```

### SUIUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: SUIUSDT
TIMEFRAME: 4H
DATE: 2026-05-09 00:00 UTC
PRICE: 1.0217
STATE: WATCHLIST
SIGNAL: Compression only: 3 shrinking candles (0.5%), volume not yet exhausted (ratio=1.05)
REASON: Lateralization: Compression confirmed: 3 consecutive compressing pairs (need 2), tightest range is 0.5% of widest in window | Volume: No volume exhaustion: last-3 avg 5,781,748 is 1.05x prior-5 avg 5,522,044 (need ≤0.7)
```

### NEARUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: NEARUSDT
TIMEFRAME: 4H
DATE: 2026-05-09 00:00 UTC
PRICE: 1.5980
STATE: GEM_ALERT
SIGNAL: COIL: 4 shrinking candles (0.0% compression) + volume at 0.54x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 4 consecutive compressing pairs (need 2), tightest range is 0.0% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 2,285,200 is 0.54x prior-5 avg 4,229,502 (threshold ≤0.7)
```

### INJUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: INJUSDT
TIMEFRAME: 4H
DATE: 2026-05-09 00:00 UTC
PRICE: 4.2280
STATE: GEM_ALERT
SIGNAL: COIL: 3 shrinking candles (1.1% compression) + volume at 0.55x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 3 consecutive compressing pairs (need 2), tightest range is 1.1% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 194,859 is 0.55x prior-5 avg 352,360 (threshold ≤0.7)
```

### ARBUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: ARBUSDT
TIMEFRAME: 4H
DATE: 2026-05-09 00:00 UTC
PRICE: 0.1428
STATE: WATCHLIST
SIGNAL: Compression only: 2 shrinking candles (1.7%), volume not yet exhausted (ratio=1.45)
REASON: Lateralization: Compression confirmed: 2 consecutive compressing pairs (need 2), tightest range is 1.7% of widest in window | Volume: No volume exhaustion: last-3 avg 19,387,941 is 1.45x prior-5 avg 13,349,759 (need ≤0.7)
```

### OPUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: OPUSDT
TIMEFRAME: 4H
DATE: 2026-05-09 00:00 UTC
PRICE: 0.1720
STATE: NO_TRADE
SIGNAL: No compression or volume exhaustion (compression_pairs=1, vol_ratio=3.45)
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: No volume exhaustion: last-3 avg 36,761,517 is 3.45x prior-5 avg 10,656,815 (need ≤0.7)
```

### FETUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: FETUSDT
TIMEFRAME: 4H
DATE: 2026-05-09 00:00 UTC
PRICE: 0.2337
STATE: WATCHLIST
SIGNAL: Compression only: 2 shrinking candles (1.1%), volume not yet exhausted (ratio=1.03)
REASON: Lateralization: Compression confirmed: 2 consecutive compressing pairs (need 2), tightest range is 1.1% of widest in window | Volume: No volume exhaustion: last-3 avg 8,567,415 is 1.03x prior-5 avg 8,355,574 (need ≤0.7)
```

### TAOUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: TAOUSDT
TIMEFRAME: 4H
DATE: 2026-05-09 00:00 UTC
PRICE: 316.5000
STATE: GEM_ALERT
SIGNAL: COIL: 4 shrinking candles (2.9% compression) + volume at 0.63x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 4 consecutive compressing pairs (need 2), tightest range is 2.9% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 12,217 is 0.63x prior-5 avg 19,516 (threshold ≤0.7)
```

### RENDERUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: RENDERUSDT
TIMEFRAME: 4H
DATE: 2026-05-09 00:00 UTC
PRICE: 2.0500
STATE: WATCHLIST
SIGNAL: Compression only: 2 shrinking candles (1.4%), volume not yet exhausted (ratio=1.56)
REASON: Lateralization: Compression confirmed: 2 consecutive compressing pairs (need 2), tightest range is 1.4% of widest in window | Volume: No volume exhaustion: last-3 avg 572,552 is 1.56x prior-5 avg 367,191 (need ≤0.7)
```

---

*Generated by euru_asian_scan.py — Euru OS READ_ONLY phase*