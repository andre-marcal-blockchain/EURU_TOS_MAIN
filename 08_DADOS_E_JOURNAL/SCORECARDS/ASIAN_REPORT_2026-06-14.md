---
schema_type: asian_scan_report
schema_version: 1.0
---
# Euru OS — Asian Session Scan Report
**Date:** 2026-06-14  
**Time:** 00:00 UTC  
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
| BTCUSDT |  64,458.0100 | **WATCHLIST** |
| ETHUSDT |   1,681.1800 | **NO_TRADE** |
| SOLUSDT |      68.9200 | **NO_TRADE** |
| BNBUSDT |     609.6600 | **WATCHLIST** |
| AVAXUSDT |       6.7180 | **WATCHLIST** |
| DOTUSDT |       0.9810 | **WATCHLIST** |
| LINKUSDT |       7.9860 | **WATCHLIST** |
| ADAUSDT |       0.1717 | **WATCHLIST** |
| XRPUSDT |       1.1505 | **WATCHLIST** |
| WLDUSDT |       0.5021 | **WATCHLIST** |
| SUIUSDT |       0.7679 | **WATCHLIST** |
| NEARUSDT |       2.1270 | **WATCHLIST** |
| INJUSDT |       5.2730 | **WATCHLIST** |
| ARBUSDT |       0.0852 | **WATCHLIST** |
| OPUSDT |       0.1070 | **WATCHLIST** |
| FETUSDT |       0.2080 | **WATCHLIST** |
| TAOUSDT |     263.1000 | **WATCHLIST** |
| RENDERUSDT |       1.7730 | **WATCHLIST** |

---

## Asian Session Assessments

### BTCUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: BTCUSDT
TIMEFRAME: 4H
DATE: 2026-06-14 00:00 UTC
PRICE: 64,458.0100
STATE: WATCHLIST
SIGNAL: Volume exhaustion only: ratio=0.64, no range compression detected
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: Volume exhaustion confirmed: last-3 avg 1,082 is 0.64x prior-5 avg 1,699 (threshold ≤0.7)
```

### ETHUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: ETHUSDT
TIMEFRAME: 4H
DATE: 2026-06-14 00:00 UTC
PRICE: 1,681.1800
STATE: NO_TRADE
SIGNAL: No compression or volume exhaustion (compression_pairs=1, vol_ratio=0.72)
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: No volume exhaustion: last-3 avg 11,965 is 0.72x prior-5 avg 16,626 (need ≤0.7)
```

### SOLUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: SOLUSDT
TIMEFRAME: 4H
DATE: 2026-06-14 00:00 UTC
PRICE: 68.9200
STATE: NO_TRADE
SIGNAL: No compression or volume exhaustion (compression_pairs=1, vol_ratio=0.72)
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: No volume exhaustion: last-3 avg 175,710 is 0.72x prior-5 avg 245,575 (need ≤0.7)
```

### BNBUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: BNBUSDT
TIMEFRAME: 4H
DATE: 2026-06-14 00:00 UTC
PRICE: 609.6600
STATE: WATCHLIST
SIGNAL: Volume exhaustion only: ratio=0.32, no range compression detected
REASON: Lateralization: No qualifying compression: 1 consecutive compressing pairs (need 2) | Volume: Volume exhaustion confirmed: last-3 avg 4,349 is 0.32x prior-5 avg 13,596 (threshold ≤0.7)
```

### AVAXUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: AVAXUSDT
TIMEFRAME: 4H
DATE: 2026-06-14 00:00 UTC
PRICE: 6.7180
STATE: WATCHLIST
SIGNAL: [BTC filter] Downgraded from GEM_ALERT — BTC state is WATCHLIST. COIL: 3 shrinking candles (0.0% compression) + volume at 0.65x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 3 consecutive compressing pairs (need 2), tightest range is 0.0% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 102,101 is 0.65x prior-5 avg 158,001 (threshold ≤0.7)
```

### DOTUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: DOTUSDT
TIMEFRAME: 4H
DATE: 2026-06-14 00:00 UTC
PRICE: 0.9810
STATE: WATCHLIST
SIGNAL: [BTC filter] Downgraded from GEM_ALERT — BTC state is WATCHLIST. COIL: 2 shrinking candles (0.0% compression) + volume at 0.42x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 2 consecutive compressing pairs (need 2), tightest range is 0.0% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 499,547 is 0.42x prior-5 avg 1,198,205 (threshold ≤0.7)
```

### LINKUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: LINKUSDT
TIMEFRAME: 4H
DATE: 2026-06-14 00:00 UTC
PRICE: 7.9860
STATE: WATCHLIST
SIGNAL: Compression only: 2 shrinking candles (0.9%), volume not yet exhausted (ratio=1.00)
REASON: Lateralization: Compression confirmed: 2 consecutive compressing pairs (need 2), tightest range is 0.9% of widest in window | Volume: No volume exhaustion: last-3 avg 149,912 is 1.00x prior-5 avg 150,094 (need ≤0.7)
```

### ADAUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: ADAUSDT
TIMEFRAME: 4H
DATE: 2026-06-14 00:00 UTC
PRICE: 0.1717
STATE: WATCHLIST
SIGNAL: [BTC filter] Downgraded from GEM_ALERT — BTC state is WATCHLIST. COIL: 2 shrinking candles (1.9% compression) + volume at 0.58x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 2 consecutive compressing pairs (need 2), tightest range is 1.9% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 10,570,212 is 0.58x prior-5 avg 18,093,811 (threshold ≤0.7)
```

### XRPUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: XRPUSDT
TIMEFRAME: 4H
DATE: 2026-06-14 00:00 UTC
PRICE: 1.1505
STATE: WATCHLIST
SIGNAL: [BTC filter] Downgraded from GEM_ALERT — BTC state is WATCHLIST. COIL: 3 shrinking candles (2.0% compression) + volume at 0.69x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 3 consecutive compressing pairs (need 2), tightest range is 2.0% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 4,977,620 is 0.69x prior-5 avg 7,196,390 (threshold ≤0.7)
```

### WLDUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: WLDUSDT
TIMEFRAME: 4H
DATE: 2026-06-14 00:00 UTC
PRICE: 0.5021
STATE: WATCHLIST
SIGNAL: [BTC filter] Downgraded from GEM_ALERT — BTC state is WATCHLIST. COIL: 3 shrinking candles (1.1% compression) + volume at 0.56x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 3 consecutive compressing pairs (need 2), tightest range is 1.1% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 26,653,110 is 0.56x prior-5 avg 47,233,719 (threshold ≤0.7)
```

### SUIUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: SUIUSDT
TIMEFRAME: 4H
DATE: 2026-06-14 00:00 UTC
PRICE: 0.7679
STATE: WATCHLIST
SIGNAL: [BTC filter] Downgraded from GEM_ALERT — BTC state is WATCHLIST. COIL: 5 shrinking candles (2.1% compression) + volume at 0.64x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 5 consecutive compressing pairs (need 2), tightest range is 2.1% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 2,758,984 is 0.64x prior-5 avg 4,337,157 (threshold ≤0.7)
```

### NEARUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: NEARUSDT
TIMEFRAME: 4H
DATE: 2026-06-14 00:00 UTC
PRICE: 2.1270
STATE: WATCHLIST
SIGNAL: Compression only: 3 shrinking candles (2.1%), volume not yet exhausted (ratio=0.78)
REASON: Lateralization: Compression confirmed: 3 consecutive compressing pairs (need 2), tightest range is 2.1% of widest in window | Volume: No volume exhaustion: last-3 avg 2,154,564 is 0.78x prior-5 avg 2,767,649 (need ≤0.7)
```

### INJUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: INJUSDT
TIMEFRAME: 4H
DATE: 2026-06-14 00:00 UTC
PRICE: 5.2730
STATE: WATCHLIST
SIGNAL: [BTC filter] Downgraded from GEM_ALERT — BTC state is WATCHLIST. COIL: 2 shrinking candles (0.0% compression) + volume at 0.40x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 2 consecutive compressing pairs (need 2), tightest range is 0.0% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 71,952 is 0.40x prior-5 avg 178,013 (threshold ≤0.7)
```

### ARBUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: ARBUSDT
TIMEFRAME: 4H
DATE: 2026-06-14 00:00 UTC
PRICE: 0.0852
STATE: WATCHLIST
SIGNAL: [BTC filter] Downgraded from GEM_ALERT — BTC state is WATCHLIST. COIL: 5 shrinking candles (4.5% compression) + volume at 0.63x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 5 consecutive compressing pairs (need 2), tightest range is 4.5% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 3,864,545 is 0.63x prior-5 avg 6,088,037 (threshold ≤0.7)
```

### OPUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: OPUSDT
TIMEFRAME: 4H
DATE: 2026-06-14 00:00 UTC
PRICE: 0.1070
STATE: WATCHLIST
SIGNAL: [BTC filter] Downgraded from GEM_ALERT — BTC state is WATCHLIST. COIL: 3 shrinking candles (1.3% compression) + volume at 0.31x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 3 consecutive compressing pairs (need 2), tightest range is 1.3% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 3,027,518 is 0.31x prior-5 avg 9,817,568 (threshold ≤0.7)
```

### FETUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: FETUSDT
TIMEFRAME: 4H
DATE: 2026-06-14 00:00 UTC
PRICE: 0.2080
STATE: WATCHLIST
SIGNAL: [BTC filter] Downgraded from GEM_ALERT — BTC state is WATCHLIST. COIL: 4 shrinking candles (1.9% compression) + volume at 0.56x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 4 consecutive compressing pairs (need 2), tightest range is 1.9% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 9,471,236 is 0.56x prior-5 avg 16,913,166 (threshold ≤0.7)
```

### TAOUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: TAOUSDT
TIMEFRAME: 4H
DATE: 2026-06-14 00:00 UTC
PRICE: 263.1000
STATE: WATCHLIST
SIGNAL: Compression only: 3 shrinking candles (1.5%), volume not yet exhausted (ratio=0.94)
REASON: Lateralization: Compression confirmed: 3 consecutive compressing pairs (need 2), tightest range is 1.5% of widest in window | Volume: No volume exhaustion: last-3 avg 42,169 is 0.94x prior-5 avg 44,797 (need ≤0.7)
```

### RENDERUSDT

```
AGENT: Scout (Asian Session)
SYMBOL: RENDERUSDT
TIMEFRAME: 4H
DATE: 2026-06-14 00:00 UTC
PRICE: 1.7730
STATE: WATCHLIST
SIGNAL: [BTC filter] Downgraded from GEM_ALERT — BTC state is WATCHLIST. COIL: 3 shrinking candles (1.1% compression) + volume at 0.65x baseline — breakout candidate
REASON: Lateralization: Compression confirmed: 3 consecutive compressing pairs (need 2), tightest range is 1.1% of widest in window | Volume: Volume exhaustion confirmed: last-3 avg 431,280 is 0.65x prior-5 avg 659,474 (threshold ≤0.7)
```

---

*Generated by euru_asian_scan.py — Euru OS READ_ONLY phase*