# AGuia Asian Session Scan

- Generated UTC: 2026-06-07T19:08:00+00:00
- Market data: Binance futures
- Mode: READ_ONLY
- Top verdict: **WAIT**

## Pair Verdicts

| Pair | Decision | Reason | Direction | BTC Filter | Setup | 4H Trend | MAC | RSI 4H | MACD Hist 4H | Vol Ratio | Risk % | Room R |
|---|---|---|---:|---|---|---|---|---:|---:|---:|---:|---:|
| BTCUSDT | WAIT | mac_incomplete | SHORT | SELF | None | BEARISH | Y/N/N | 39.14 | 463.452101 | 0.55 | 3.07 | 1.36 |
| ETHUSDT | WAIT | mac_incomplete | SHORT | INACTIVE | None | BEARISH | Y/N/N | 36.50 | 15.974604 | 0.53 | 4.45 | 1.57 |
| SOLUSDT | WAIT | mac_incomplete | SHORT | INACTIVE | None | BEARISH | Y/N/N | 35.82 | 0.693007 | 0.62 | 5.19 | 1.29 |

## Decision Summary

- mac_incomplete: 3

## Trade Plans

### BTCUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: SHORT
- Setup: None
- MAC pillars: {'Movimento': True, 'Aceleracao': False, 'Confirmacao': False}
- Entry: 61660.5000
- Stop: 63552.9000
- Target 1: 57875.7000
- Target 2: 55983.3000
- Live execution: BLOCKED

### ETHUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: SHORT
- Setup: None
- MAC pillars: {'Movimento': True, 'Aceleracao': False, 'Confirmacao': False}
- Entry: 1616.6000
- Stop: 1688.5250
- Target 1: 1472.7500
- Target 2: 1400.8250
- Live execution: BLOCKED

### SOLUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: SHORT
- Setup: None
- MAC pillars: {'Movimento': True, 'Aceleracao': False, 'Confirmacao': False}
- Entry: 64.3400
- Stop: 67.6775
- Target 1: 57.6650
- Target 2: 54.3275
- Live execution: BLOCKED

## Execution Rule

This report can authorize PAPER_ENTRY only. Live Binance Futures execution remains blocked until paper trading, risk, and API safety gates are complete.
