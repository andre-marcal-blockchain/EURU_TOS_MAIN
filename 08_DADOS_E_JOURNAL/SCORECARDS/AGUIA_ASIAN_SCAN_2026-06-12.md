# AGuia Asian Session Scan

- Generated UTC: 2026-06-12T07:06:20+00:00
- Market data: Binance futures
- Mode: READ_ONLY
- Top verdict: **WAIT**

## Pair Verdicts

| Pair | Decision | Reason | Direction | BTC Filter | Setup | 4H Trend | MAC | RSI 4H | MACD Hist 4H | Vol Ratio | Risk % | Room R |
|---|---|---|---:|---|---|---|---|---:|---:|---:|---:|---:|
| BTCUSDT | WAIT | mac_incomplete | LONG | SELF | None | SIDEWAYS | N/N/N | 52.38 | 204.256956 | 0.47 | 2.24 | 0.60 |
| ETHUSDT | WAIT | mac_incomplete | LONG | ACTIVE_SIDEWAYS | None | SIDEWAYS | N/N/N | 49.85 | 5.080704 | 0.45 | 2.90 | 1.13 |
| SOLUSDT | WAIT | mac_incomplete | LONG | ACTIVE_SIDEWAYS | None | SIDEWAYS | N/N/N | 52.32 | 0.351957 | 0.49 | 3.27 | 0.87 |

## Decision Summary

- mac_incomplete: 3

## Trade Plans

### BTCUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: LONG
- Setup: None
- MAC pillars: {'Movimento': False, 'Aceleracao': False, 'Confirmacao': False}
- Entry: 63069.7000
- Stop: 61659.1214
- Target 1: 65890.8571
- Target 2: 67301.4357
- Live execution: BLOCKED

### ETHUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: LONG
- Setup: None
- MAC pillars: {'Movimento': False, 'Aceleracao': False, 'Confirmacao': False}
- Entry: 1659.7600
- Stop: 1611.5971
- Target 1: 1756.0857
- Target 2: 1804.2486
- Live execution: BLOCKED

### SOLUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: LONG
- Setup: None
- MAC pillars: {'Movimento': False, 'Aceleracao': False, 'Confirmacao': False}
- Entry: 66.2800
- Stop: 64.1104
- Target 1: 70.6193
- Target 2: 72.7889
- Live execution: BLOCKED

## Execution Rule

This report can authorize PAPER_ENTRY only. Live Binance Futures execution remains blocked until paper trading, risk, and API safety gates are complete.
