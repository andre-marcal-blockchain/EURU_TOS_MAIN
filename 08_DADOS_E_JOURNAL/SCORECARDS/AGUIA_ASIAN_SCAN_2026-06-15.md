# AGuia Asian Session Scan

- Generated UTC: 2026-06-15T19:07:49+00:00
- Market data: Binance futures
- Mode: READ_ONLY
- Top verdict: **WAIT**

## Pair Verdicts

| Pair | Decision | Reason | Direction | BTC Filter | Setup | 4H Trend | MAC | RSI 4H | MACD Hist 4H | Vol Ratio | Risk % | Room R |
|---|---|---|---:|---|---|---|---|---:|---:|---:|---:|---:|
| BTCUSDT | WAIT | mac_incomplete | LONG | SELF | Continuation | BULLISH | Y/N/Y | 69.06 | 249.025895 | 1.82 | 1.52 | 0.44 |
| ETHUSDT | WAIT | mac_incomplete | LONG | INACTIVE | Continuation | BULLISH | Y/N/Y | 76.05 | 16.946123 | 3.21 | 2.24 | 0.45 |
| SOLUSDT | NO_ENTRY | room_r_below_1_5 | LONG | INACTIVE | Breakout | BULLISH | Y/Y/Y | 80.17 | 0.720988 | 2.05 | 2.75 | -0.16 |

## Decision Summary

- mac_incomplete: 2
- room_r_below_1_5: 1

## Trade Plans

### BTCUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: LONG
- Setup: Continuation
- MAC pillars: {'Movimento': True, 'Aceleracao': False, 'Confirmacao': True}
- Entry: 66803.1000
- Stop: 65785.2107
- Target 1: 68838.8786
- Target 2: 69856.7679
- Live execution: BLOCKED

### ETHUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: LONG
- Setup: Continuation
- MAC pillars: {'Movimento': True, 'Aceleracao': False, 'Confirmacao': True}
- Entry: 1830.2900
- Stop: 1789.3229
- Target 1: 1912.2243
- Target 2: 1953.1914
- Live execution: BLOCKED

### SOLUSDT - NO_ENTRY

- Decision reason: room_r_below_1_5
- Direction: LONG
- Setup: Breakout
- MAC pillars: {'Movimento': True, 'Aceleracao': True, 'Confirmacao': True}
- Entry: 75.5500
- Stop: 73.4704
- Target 1: 79.7093
- Target 2: 81.7889
- Live execution: BLOCKED

## Execution Rule

This report can authorize PAPER_ENTRY only. Live Binance Futures execution remains blocked until paper trading, risk, and API safety gates are complete.
