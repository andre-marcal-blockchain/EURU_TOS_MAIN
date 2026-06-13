# AGuia Asian Session Scan

- Generated UTC: 2026-06-13T01:46:00+00:00
- Market data: Binance futures
- Mode: READ_ONLY
- Top verdict: **WAIT**

## Pair Verdicts

| Pair | Decision | Reason | Direction | BTC Filter | Setup | 4H Trend | MAC | RSI 4H | MACD Hist 4H | Vol Ratio | Risk % | Room R |
|---|---|---|---:|---|---|---|---|---:|---:|---:|---:|---:|
| BTCUSDT | WAIT | mac_incomplete | LONG | SELF | None | SIDEWAYS | N/Y/N | 56.92 | 138.189916 | 0.33 | 1.88 | 0.50 |
| ETHUSDT | WAIT | mac_incomplete | LONG | ACTIVE_SIDEWAYS | Sweep+Reversal | SIDEWAYS | N/Y/N | 52.90 | 3.083627 | 0.32 | 2.41 | 0.51 |
| SOLUSDT | WAIT | mac_incomplete | LONG | ACTIVE_SIDEWAYS | None | SIDEWAYS | N/Y/N | 56.87 | 0.253502 | 0.49 | 2.93 | 0.72 |

## Decision Summary

- mac_incomplete: 3

## Trade Plans

### BTCUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: LONG
- Setup: None
- MAC pillars: {'Movimento': False, 'Aceleracao': True, 'Confirmacao': False}
- Entry: 63769.1000
- Stop: 62572.8929
- Target 1: 66161.5143
- Target 2: 67357.7214
- Live execution: BLOCKED

### ETHUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: LONG
- Setup: Sweep+Reversal
- MAC pillars: {'Movimento': False, 'Aceleracao': True, 'Confirmacao': False}
- Entry: 1673.0000
- Stop: 1632.7207
- Target 1: 1753.5586
- Target 2: 1793.8379
- Live execution: BLOCKED

### SOLUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: LONG
- Setup: None
- MAC pillars: {'Movimento': False, 'Aceleracao': True, 'Confirmacao': False}
- Entry: 67.3500
- Stop: 65.3764
- Target 1: 71.2971
- Target 2: 73.2707
- Live execution: BLOCKED

## Execution Rule

This report can authorize PAPER_ENTRY only. Live Binance Futures execution remains blocked until paper trading, risk, and API safety gates are complete.
