# AGuia Asian Session Scan

- Generated UTC: 2026-06-18T19:07:13+00:00
- Market data: Binance futures
- Mode: READ_ONLY
- Top verdict: **WAIT**

## Pair Verdicts

| Pair | Decision | Reason | Direction | BTC Filter | Setup | 4H Trend | MAC | RSI 4H | MACD Hist 4H | Vol Ratio | Risk % | Room R |
|---|---|---|---:|---|---|---|---|---:|---:|---:|---:|---:|
| BTCUSDT | WAIT | mac_incomplete | SHORT | SELF | Continuation | BEARISH | Y/N/Y | 35.52 | -409.310324 | 1.58 | 2.46 | 0.29 |
| ETHUSDT | WAIT | mac_incomplete | SHORT | INACTIVE | None | SIDEWAYS | N/N/Y | 37.96 | -14.021342 | 1.15 | 3.20 | 0.13 |
| SOLUSDT | WAIT | mac_incomplete | SHORT | INACTIVE | None | SIDEWAYS | N/N/Y | 38.47 | -0.747828 | 1.27 | 3.86 | 0.12 |

## Decision Summary

- mac_incomplete: 3

## Trade Plans

### BTCUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: SHORT
- Setup: Continuation
- MAC pillars: {'Movimento': True, 'Aceleracao': False, 'Confirmacao': True}
- Entry: 62676.8000
- Stop: 64216.8929
- Target 1: 59596.6143
- Target 2: 58056.5214
- Live execution: BLOCKED

### ETHUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: SHORT
- Setup: None
- MAC pillars: {'Movimento': False, 'Aceleracao': False, 'Confirmacao': True}
- Entry: 1684.8000
- Stop: 1738.6596
- Target 1: 1577.0807
- Target 2: 1523.2211
- Live execution: BLOCKED

### SOLUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: SHORT
- Setup: None
- MAC pillars: {'Movimento': False, 'Aceleracao': False, 'Confirmacao': True}
- Entry: 68.6500
- Stop: 71.3018
- Target 1: 63.3464
- Target 2: 60.6946
- Live execution: BLOCKED

## Execution Rule

This report can authorize PAPER_ENTRY only. Live Binance Futures execution remains blocked until paper trading, risk, and API safety gates are complete.
