# AGuia Asian Session Scan

- Generated UTC: 2026-06-21T20:02:42+00:00
- Market data: Binance futures
- Mode: READ_ONLY
- Top verdict: **WAIT**

## Pair Verdicts

| Pair | Decision | Reason | Direction | BTC Filter | Setup | 4H Trend | MAC | RSI 4H | MACD Hist 4H | Vol Ratio | Risk % | Room R |
|---|---|---|---:|---|---|---|---|---:|---:|---:|---:|---:|
| BTCUSDT | WAIT | mac_incomplete | LONG | SELF | None | SIDEWAYS | N/N/N | 52.13 | 119.389073 | 0.31 | 1.17 | 0.54 |
| ETHUSDT | WAIT | mac_incomplete | LONG | ACTIVE_SIDEWAYS | Continuation | BULLISH | Y/N/N | 51.93 | 1.936379 | 0.43 | 1.51 | 0.75 |
| SOLUSDT | WAIT | mac_incomplete | LONG | ACTIVE_SIDEWAYS | Continuation | BULLISH | Y/N/N | 65.79 | 0.397194 | 0.64 | 2.62 | 0.23 |

## Decision Summary

- mac_incomplete: 3

## Trade Plans

### BTCUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: LONG
- Setup: None
- MAC pillars: {'Movimento': False, 'Aceleracao': False, 'Confirmacao': False}
- Entry: 64164.2000
- Stop: 63416.3643
- Target 1: 65659.8714
- Target 2: 66407.7071
- Live execution: BLOCKED

### ETHUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: LONG
- Setup: Continuation
- MAC pillars: {'Movimento': True, 'Aceleracao': False, 'Confirmacao': False}
- Entry: 1732.8400
- Stop: 1706.6361
- Target 1: 1785.2479
- Target 2: 1811.4518
- Live execution: BLOCKED

### SOLUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: LONG
- Setup: Continuation
- MAC pillars: {'Movimento': True, 'Aceleracao': False, 'Confirmacao': False}
- Entry: 74.3500
- Stop: 72.4032
- Target 1: 78.2436
- Target 2: 80.1904
- Live execution: BLOCKED

## Execution Rule

This report can authorize PAPER_ENTRY only. Live Binance Futures execution remains blocked until paper trading, risk, and API safety gates are complete.
