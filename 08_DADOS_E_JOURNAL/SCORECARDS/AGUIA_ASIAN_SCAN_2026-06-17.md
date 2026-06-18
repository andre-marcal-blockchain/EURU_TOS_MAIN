# AGuia Asian Session Scan

- Generated UTC: 2026-06-17T20:20:17+00:00
- Market data: Binance futures
- Mode: READ_ONLY
- Top verdict: **WAIT**

## Pair Verdicts

| Pair | Decision | Reason | Direction | BTC Filter | Setup | 4H Trend | MAC | RSI 4H | MACD Hist 4H | Vol Ratio | Risk % | Room R |
|---|---|---|---:|---|---|---|---|---:|---:|---:|---:|---:|
| BTCUSDT | WAIT | mac_incomplete | SHORT | SELF | None | SIDEWAYS | N/N/Y | 43.14 | -291.432745 | 1.73 | 2.13 | 0.46 |
| ETHUSDT | WAIT | mac_incomplete | SHORT | ACTIVE_SIDEWAYS | None | SIDEWAYS | N/N/Y | 48.16 | -8.798308 | 1.41 | 3.09 | 1.60 |
| SOLUSDT | WAIT | mac_incomplete | SHORT | ACTIVE_SIDEWAYS | None | SIDEWAYS | N/N/Y | 50.89 | -0.430980 | 1.45 | 3.48 | 1.98 |

## Decision Summary

- mac_incomplete: 3

## Trade Plans

### BTCUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: SHORT
- Setup: None
- MAC pillars: {'Movimento': False, 'Aceleracao': False, 'Confirmacao': True}
- Entry: 64286.1000
- Stop: 65655.4607
- Target 1: 61547.3786
- Target 2: 60178.0179
- Live execution: BLOCKED

### ETHUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: SHORT
- Setup: None
- MAC pillars: {'Movimento': False, 'Aceleracao': False, 'Confirmacao': True}
- Entry: 1739.1500
- Stop: 1792.8404
- Target 1: 1631.7693
- Target 2: 1578.0789
- Live execution: BLOCKED

### SOLUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: SHORT
- Setup: None
- MAC pillars: {'Movimento': False, 'Aceleracao': False, 'Confirmacao': True}
- Entry: 71.8400
- Stop: 74.3418
- Target 1: 66.8364
- Target 2: 64.3346
- Live execution: BLOCKED

## Execution Rule

This report can authorize PAPER_ENTRY only. Live Binance Futures execution remains blocked until paper trading, risk, and API safety gates are complete.
