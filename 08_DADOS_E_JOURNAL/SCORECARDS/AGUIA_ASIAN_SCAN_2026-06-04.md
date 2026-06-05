# AGuia Asian Session Scan

- Generated UTC: 2026-06-04T19:27:49+00:00
- Market data: Binance futures
- Mode: READ_ONLY
- Top verdict: **WAIT**

## Pair Verdicts

| Pair | Decision | Direction | BTC Filter | Setup | 4H Trend | MAC | RSI 4H | MACD Hist 4H | Vol Ratio | Risk % | Room R |
|---|---|---:|---|---|---|---|---:|---:|---:|---:|---:|
| BTCUSDT | WAIT | LONG | SELF | Sweep+Reversal | BEARISH | N/N/Y | 28.59 | -176.484828 | 1.31 | 4.00 | 3.54 |
| ETHUSDT | WAIT | LONG | ACTIVE_BEARISH | Sweep+Reversal | BEARISH | N/N/Y | 29.70 | -7.976763 | 1.07 | 5.07 | 2.54 |
| SOLUSDT | NO_ENTRY | SHORT | INACTIVE | Continuation | BEARISH | Y/Y/Y | 25.97 | -0.444686 | 1.24 | 5.84 | 0.72 |

## Trade Plans

### BTCUSDT - WAIT

- Direction: LONG
- Setup: Sweep+Reversal
- MAC pillars: {'Movimento': False, 'Aceleracao': False, 'Confirmacao': True}
- Entry: 64019.8000
- Stop: 61456.9964
- Target 1: 69145.4071
- Target 2: 71708.2107
- Live execution: BLOCKED

### ETHUSDT - WAIT

- Direction: LONG
- Setup: Sweep+Reversal
- MAC pillars: {'Movimento': False, 'Aceleracao': False, 'Confirmacao': True}
- Entry: 1780.2900
- Stop: 1690.0286
- Target 1: 1960.8129
- Target 2: 2051.0743
- Live execution: BLOCKED

### SOLUSDT - NO_ENTRY

- Direction: SHORT
- Setup: Continuation
- MAC pillars: {'Movimento': True, 'Aceleracao': True, 'Confirmacao': True}
- Entry: 69.5000
- Stop: 73.5575
- Target 1: 61.3850
- Target 2: 57.3275
- Live execution: BLOCKED

## Execution Rule

This report can authorize PAPER_ENTRY only. Live Binance Futures execution remains blocked until paper trading, risk, and API safety gates are complete.
