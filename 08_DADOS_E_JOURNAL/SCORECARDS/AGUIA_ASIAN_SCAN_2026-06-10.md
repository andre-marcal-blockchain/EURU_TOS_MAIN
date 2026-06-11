# AGuia Asian Session Scan

- Generated UTC: 2026-06-10T19:31:27+00:00
- Market data: Binance futures
- Mode: READ_ONLY
- Top verdict: **WAIT**

## Pair Verdicts

| Pair | Decision | Reason | Direction | BTC Filter | Setup | 4H Trend | MAC | RSI 4H | MACD Hist 4H | Vol Ratio | Risk % | Room R |
|---|---|---|---:|---|---|---|---|---:|---:|---:|---:|---:|
| BTCUSDT | WAIT | mac_incomplete | LONG | SELF | None | BEARISH | N/N/Y | 45.87 | 34.470461 | 1.30 | 2.58 | 1.50 |
| ETHUSDT | WAIT | mac_incomplete | LONG | ACTIVE_BEARISH | None | BEARISH | N/N/Y | 43.45 | 1.471236 | 1.29 | 3.32 | 1.73 |
| SOLUSDT | WAIT | mac_incomplete | LONG | ACTIVE_BEARISH | None | BEARISH | N/N/Y | 41.30 | 0.008634 | 1.29 | 3.81 | 1.83 |

## Decision Summary

- mac_incomplete: 3

## Trade Plans

### BTCUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: LONG
- Setup: None
- MAC pillars: {'Movimento': False, 'Aceleracao': False, 'Confirmacao': True}
- Entry: 61846.6000
- Stop: 60247.9321
- Target 1: 65043.9357
- Target 2: 66642.6036
- Live execution: BLOCKED

### ETHUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: LONG
- Setup: None
- MAC pillars: {'Movimento': False, 'Aceleracao': False, 'Confirmacao': True}
- Entry: 1627.9800
- Stop: 1573.8654
- Target 1: 1736.2093
- Target 2: 1790.3239
- Live execution: BLOCKED

### SOLUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: LONG
- Setup: None
- MAC pillars: {'Movimento': False, 'Aceleracao': False, 'Confirmacao': True}
- Entry: 63.7200
- Stop: 61.2911
- Target 1: 68.5779
- Target 2: 71.0068
- Live execution: BLOCKED

## Execution Rule

This report can authorize PAPER_ENTRY only. Live Binance Futures execution remains blocked until paper trading, risk, and API safety gates are complete.
