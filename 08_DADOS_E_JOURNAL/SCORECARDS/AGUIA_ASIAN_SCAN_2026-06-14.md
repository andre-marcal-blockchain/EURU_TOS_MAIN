# AGuia Asian Session Scan

- Generated UTC: 2026-06-14T19:07:16+00:00
- Market data: Binance futures
- Mode: READ_ONLY
- Top verdict: **WAIT**

## Pair Verdicts

| Pair | Decision | Reason | Direction | BTC Filter | Setup | 4H Trend | MAC | RSI 4H | MACD Hist 4H | Vol Ratio | Risk % | Room R |
|---|---|---|---:|---|---|---|---|---:|---:|---:|---:|---:|
| BTCUSDT | WAIT | mac_incomplete | SHORT | SELF | None | BEARISH | Y/N/N | 51.26 | -12.588310 | 0.62 | 1.20 | 1.84 |
| ETHUSDT | WAIT | mac_incomplete | SHORT | INACTIVE | Continuation | BEARISH | Y/Y/N | 46.95 | -0.916290 | 0.63 | 1.38 | 1.30 |
| SOLUSDT | WAIT | mac_incomplete | SHORT | INACTIVE | Sweep+Reversal | BEARISH | Y/N/N | 51.38 | -0.025797 | 0.66 | 2.25 | 1.63 |

## Decision Summary

- mac_incomplete: 3

## Trade Plans

### BTCUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: SHORT
- Setup: None
- MAC pillars: {'Movimento': True, 'Aceleracao': False, 'Confirmacao': False}
- Entry: 63722.5000
- Stop: 64487.2429
- Target 1: 62193.0143
- Target 2: 61428.2714
- Live execution: BLOCKED

### ETHUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: SHORT
- Setup: Continuation
- MAC pillars: {'Movimento': True, 'Aceleracao': True, 'Confirmacao': False}
- Entry: 1661.0600
- Stop: 1683.9757
- Target 1: 1615.2286
- Target 2: 1592.3129
- Live execution: BLOCKED

### SOLUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: SHORT
- Setup: Sweep+Reversal
- MAC pillars: {'Movimento': True, 'Aceleracao': False, 'Confirmacao': False}
- Entry: 67.3200
- Stop: 68.8371
- Target 1: 64.2857
- Target 2: 62.7686
- Live execution: BLOCKED

## Execution Rule

This report can authorize PAPER_ENTRY only. Live Binance Futures execution remains blocked until paper trading, risk, and API safety gates are complete.
