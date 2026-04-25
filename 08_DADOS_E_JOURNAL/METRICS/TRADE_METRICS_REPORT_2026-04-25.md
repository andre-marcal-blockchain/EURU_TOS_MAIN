---
schema_type: trade_metrics_report
schema_version: 1.0
report_date: '2026-04-25'
---

# Euru Trade Metrics Report — 2026-04-25

## Executive Summary

- Total trade files: 4
- Official trades included: 3
- Trades excluded from official stats: 1
- Official P&L: 2.83 USDT
- Official win rate: 100%
- Official average RR: 0.9033R
- Average days held: 6.67

## North Star Note

Monthly 5-8% benchmark requires official capital curve definition.

## Trade Table

| Trade | Symbol | Status | Included | P&L USDT | RR | Exit | Days | Exclusion |
|---|---|---|---|---:|---:|---|---:|---|
| PT1 | AVAXUSDT | closed | yes | 0.29 | 0.29 | time_stop | 7 | - |
| PT2 | NEARUSDT | closed | yes | 0.62 | 0.62 | time_stop | 7 | - |
| PT3 | ARBUSDT | closed | yes | 1.92 | 1.8 | time_stop | 6 | - |
| PT4 | XRPUSDT | closed | no | 0.01 | 0.06 | system_rule | 0 | governance_breach_or_excluded_tag |

## By Symbol

| Group | Count | Win Rate | P&L USDT | Avg RR | Avg Days |
|---|---:|---:|---:|---:|---:|
| ARBUSDT | 1 | 100 | 1.92 | 1.8 | 6 |
| AVAXUSDT | 1 | 100 | 0.29 | 0.29 | 7 |
| NEARUSDT | 1 | 100 | 0.62 | 0.62 | 7 |

## By Setup Type

| Group | Count | Win Rate | P&L USDT | Avg RR | Avg Days |
|---|---:|---:|---:|---:|---:|
| trend_continuation | 3 | 100 | 2.83 | 0.9033 | 6.67 |

## By News Severity

| Group | Count | Win Rate | P&L USDT | Avg RR | Avg Days |
|---|---:|---:|---:|---:|---:|
| low | 3 | 100 | 2.83 | 0.9033 | 6.67 |

## By Exit Reason

| Group | Count | Win Rate | P&L USDT | Avg RR | Avg Days |
|---|---:|---:|---:|---:|---:|
| time_stop | 3 | 100 | 2.83 | 0.9033 | 6.67 |

## Interpretation

Current sample is too small for statistical confidence. PT004 is preserved as an incident record but excluded from official performance metrics due to governance breach tags.

## Next Metric Improvements

- Define official capital curve rules for monthly 5-8% benchmark.
- Add fees, funding, and slippage assumptions.
- Add max drawdown calculation once capital curve is canonical.
