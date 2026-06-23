# AGuia Asian Session Scan

- Generated UTC: 2026-06-22T19:06:36+00:00
- Market data: Binance futures
- Mode: READ_ONLY
- Top verdict: **WAIT**

## Pair Verdicts

| Pair | Decision | Reason | Direction | BTC Filter | Setup | 4H Trend | MAC | RSI 4H | MACD Hist 4H | Vol Ratio | Risk % | Room R |
|---|---|---|---:|---|---|---|---|---:|---:|---:|---:|---:|
| BTCUSDT | WAIT | mac_incomplete | LONG | SELF | None | SIDEWAYS | N/N/Y | 52.43 | 105.929079 | 1.69 | 1.62 | 1.23 |
| ETHUSDT | WAIT | mac_incomplete | SHORT | ACTIVE_SIDEWAYS | Sweep+Reversal | SIDEWAYS | N/N/Y | 49.89 | 2.192565 | 1.74 | 2.20 | 1.39 |
| SOLUSDT | WAIT | mac_incomplete | SHORT | ACTIVE_SIDEWAYS | Sweep+Reversal | SIDEWAYS | N/N/Y | 51.30 | 0.007031 | 1.33 | 3.21 | 2.01 |

## Decision Summary

- mac_incomplete: 3

## Trade Plans

### BTCUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: LONG
- Setup: None
- MAC pillars: {'Movimento': False, 'Aceleracao': False, 'Confirmacao': True}
- Entry: 64309.7000
- Stop: 63266.7607
- Target 1: 66395.5786
- Target 2: 67438.5179
- Live execution: BLOCKED

### ETHUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: SHORT
- Setup: Sweep+Reversal
- MAC pillars: {'Movimento': False, 'Aceleracao': False, 'Confirmacao': True}
- Entry: 1731.0400
- Stop: 1769.0800
- Target 1: 1654.9600
- Target 2: 1616.9200
- Live execution: BLOCKED

### SOLUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: SHORT
- Setup: Sweep+Reversal
- MAC pillars: {'Movimento': False, 'Aceleracao': False, 'Confirmacao': True}
- Entry: 72.5400
- Stop: 74.8671
- Target 1: 67.8857
- Target 2: 65.5586
- Live execution: BLOCKED

## Execution Rule

This report can authorize PAPER_ENTRY only. Live Binance Futures execution remains blocked until paper trading, risk, and API safety gates are complete.
