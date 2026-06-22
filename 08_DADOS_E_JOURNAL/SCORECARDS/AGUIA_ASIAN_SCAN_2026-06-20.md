# AGuia Asian Session Scan

- Generated UTC: 2026-06-20T19:06:14+00:00
- Market data: Binance futures
- Mode: READ_ONLY
- Top verdict: **WAIT**

## Pair Verdicts

| Pair | Decision | Reason | Direction | BTC Filter | Setup | 4H Trend | MAC | RSI 4H | MACD Hist 4H | Vol Ratio | Risk % | Room R |
|---|---|---|---:|---|---|---|---|---:|---:|---:|---:|---:|
| BTCUSDT | WAIT | mac_incomplete | LONG | SELF | None | SIDEWAYS | N/N/N | 49.06 | 119.413960 | 0.76 | 1.82 | 2.25 |
| ETHUSDT | WAIT | mac_incomplete | LONG | ACTIVE_SIDEWAYS | Continuation | BULLISH | Y/N/N | 50.02 | 1.892180 | 0.72 | 2.37 | 1.73 |
| SOLUSDT | WAIT | mac_incomplete | LONG | ACTIVE_SIDEWAYS | Continuation | BULLISH | Y/N/Y | 55.55 | 0.240914 | 0.98 | 3.02 | 1.38 |

## Decision Summary

- mac_incomplete: 3

## Trade Plans

### BTCUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: LONG
- Setup: None
- MAC pillars: {'Movimento': False, 'Aceleracao': False, 'Confirmacao': False}
- Entry: 63801.7000
- Stop: 62640.7000
- Target 1: 66123.7000
- Target 2: 67284.7000
- Live execution: BLOCKED

### ETHUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: LONG
- Setup: Continuation
- MAC pillars: {'Movimento': True, 'Aceleracao': False, 'Confirmacao': False}
- Entry: 1724.7600
- Stop: 1683.8079
- Target 1: 1806.6643
- Target 2: 1847.6164
- Live execution: BLOCKED

### SOLUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: LONG
- Setup: Continuation
- MAC pillars: {'Movimento': True, 'Aceleracao': False, 'Confirmacao': True}
- Entry: 71.6800
- Stop: 69.5179
- Target 1: 76.0043
- Target 2: 78.1664
- Live execution: BLOCKED

## Execution Rule

This report can authorize PAPER_ENTRY only. Live Binance Futures execution remains blocked until paper trading, risk, and API safety gates are complete.
