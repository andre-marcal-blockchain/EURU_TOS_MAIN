# AGuia Asian Session Scan

- Generated UTC: 2026-06-09T19:06:54+00:00
- Market data: Binance futures
- Mode: READ_ONLY
- Top verdict: **WAIT**

## Pair Verdicts

| Pair | Decision | Reason | Direction | BTC Filter | Setup | 4H Trend | MAC | RSI 4H | MACD Hist 4H | Vol Ratio | Risk % | Room R |
|---|---|---|---:|---|---|---|---|---:|---:|---:|---:|---:|
| BTCUSDT | WAIT | mac_incomplete | SHORT | SELF | None | BEARISH | Y/N/Y | 42.47 | 72.605577 | 1.50 | 2.94 | 0.91 |
| ETHUSDT | WAIT | mac_incomplete | SHORT | INACTIVE | None | BEARISH | Y/N/Y | 44.85 | 7.831443 | 1.12 | 3.83 | 1.86 |
| SOLUSDT | WAIT | mac_incomplete | SHORT | INACTIVE | None | BEARISH | Y/N/Y | 44.24 | 0.286751 | 1.18 | 4.29 | 1.47 |

## Decision Summary

- mac_incomplete: 3

## Trade Plans

### BTCUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: SHORT
- Setup: None
- MAC pillars: {'Movimento': True, 'Aceleracao': False, 'Confirmacao': True}
- Entry: 61795.6000
- Stop: 63610.4929
- Target 1: 58165.8143
- Target 2: 56350.9214
- Live execution: BLOCKED

### ETHUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: SHORT
- Setup: None
- MAC pillars: {'Movimento': True, 'Aceleracao': False, 'Confirmacao': True}
- Entry: 1650.9400
- Stop: 1714.2389
- Target 1: 1524.3421
- Target 2: 1461.0432
- Live execution: BLOCKED

### SOLUSDT - WAIT

- Decision reason: mac_incomplete
- Direction: SHORT
- Setup: None
- MAC pillars: {'Movimento': True, 'Aceleracao': False, 'Confirmacao': True}
- Entry: 65.2400
- Stop: 68.0386
- Target 1: 59.6429
- Target 2: 56.8443
- Live execution: BLOCKED

## Execution Rule

This report can authorize PAPER_ENTRY only. Live Binance Futures execution remains blocked until paper trading, risk, and API safety gates are complete.
