# AGuia Asian Session Scan

- Generated UTC: 2026-06-19T19:07:03+00:00
- Market data: Binance futures
- Mode: READ_ONLY
- Top verdict: **WAIT**

## Pair Verdicts

| Pair | Decision | Reason | Direction | BTC Filter | Setup | 4H Trend | MAC | RSI 4H | MACD Hist 4H | Vol Ratio | Risk % | Room R |
|---|---|---|---:|---|---|---|---|---:|---:|---:|---:|---:|
| BTCUSDT | WAIT | mac_incomplete | SHORT | SELF | Continuation | BEARISH | Y/Y/N | 40.92 | -165.025707 | 0.76 | 2.29 | 0.55 |
| ETHUSDT | WAIT | mac_incomplete | SHORT | INACTIVE | Continuation | BEARISH | Y/Y/N | 43.75 | -7.266746 | 0.56 | 2.83 | 0.65 |
| SOLUSDT | WAIT | mac_incomplete | SHORT | INACTIVE | None | SIDEWAYS | N/Y/N | 43.01 | -0.435369 | 0.75 | 3.50 | 0.48 |

## Decision Summary

- mac_incomplete: 3

## Trade Plans

### BTCUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: SHORT
- Setup: Continuation
- MAC pillars: {'Movimento': True, 'Aceleracao': True, 'Confirmacao': False}
- Entry: 63020.1000
- Stop: 64460.5929
- Target 1: 60139.1143
- Target 2: 58698.6214
- Live execution: BLOCKED

### ETHUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: SHORT
- Setup: Continuation
- MAC pillars: {'Movimento': True, 'Aceleracao': True, 'Confirmacao': False}
- Entry: 1701.8000
- Stop: 1749.9329
- Target 1: 1605.5343
- Target 2: 1557.4014
- Live execution: BLOCKED

### SOLUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: SHORT
- Setup: None
- MAC pillars: {'Movimento': False, 'Aceleracao': True, 'Confirmacao': False}
- Entry: 69.0100
- Stop: 71.4229
- Target 1: 64.1843
- Target 2: 61.7714
- Live execution: BLOCKED

## Execution Rule

This report can authorize PAPER_ENTRY only. Live Binance Futures execution remains blocked until paper trading, risk, and API safety gates are complete.
