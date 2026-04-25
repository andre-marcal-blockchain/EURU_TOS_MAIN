---
schema_type: paper_trade
schema_version: 1.0

trade_id: PT1
status: closed
system_phase: simulate

symbol: AVAXUSDT
venue: binance_futures
contract_type: perpetual
market_type: usds_m
asset_class: altcoin_future

side: long
intent_type: open
setup_type: trend_continuation

entry_datetime: 2026-04-08T00:00:00Z
entry_price: 9.22
entry_score: 0.0
mac_state_at_entry: bullish
risk_state_at_entry: medium
news_severity_at_entry: low

margin_mode: cross
position_mode: hedge
leverage: 5
quantity: 0
notional_usdt: 0.0

stop_loss: 8.501
take_profit: 0.0
planned_rr: 0.0

exit_datetime: 2026-04-15T09:00:00Z
exit_price: 9.43
pnl_usdt: 0.29
pnl_pct: 0.29
rr_achieved: 0.29
exit_reason: time_stop

days_held: 7
score_prediction_label: winner_candidate
score_prediction_confidence: 0.0

linked_trade_ids: []
tags:
  - mac
  - legacy_migrated
---

# Trade Summary

## Thesis
Migrated from legacy format. See original content below.

## Entry Reasoning
See original content below.

## Risk Plan
See original content below.

## Management Notes
See original content below.

## Exit Notes
- Time stop expired 2026-04-15 (7 days). Price at 9.43 vs entry 9.22. Small profit +0.29 USDT (+0.29R). Neither stop nor T1 were reached.

## Lessons Learned
- Trade moved in the right direction but lacked momentum to reach T1 (10.658). OBV went from RISING at entry to FLAT — volume conviction faded. Time stop discipline preserved capital and locked a small gain.

---

## Original Content (Legacy)

# PAPER TRADE 001 â€” AVAXUSDT
**Euru OS â€” Simulate Phase Entry**

---

## Trade Header

```
TRADE_ID:           PAPER_TRADE_001
ASSET:              AVAXUSDT
DATE_IDENTIFIED:    2026-04-06
TIME_IDENTIFIED:    04:47 UTC
DATE_ENTERED:       2026-04-08
ENTRY_PRICE:        9.22
SOURCE_REPORT:      SCOUT_REPORT_2026-04-06.md / SCOUT_REPORT_2026-04-08.md
EXECUTION_STATE:    SIMULATE_ACTIVE
GOVERNANCE_NOTE:    SIMULATE mode formally activated 2026-04-08 after 48h governance period (started 2026-04-06). Type 3 sign-off complete.
SYSTEM_MODE:        SIMULATE (ACTIVE â€” 2026-04-08)
OPERATOR:           Andre Marcal
```

---

## Market Data at Identification (Morning Scan â€” 2026-04-06 04:47 UTC)

```
PRICE:              9.49 USDT
24H_CHANGE:         +6.03%
7D_DEV:             +6.19% vs 7D avg (8.94)
RSI_14:             54.86
MACD_TREND:         BULLISH
MACD_HISTOGRAM:     0.031767
OBV_TREND:          RISING
VOLUME_FLOW:        STRONG
ATR_14:             0.4794
STOP_DIST (ATRÃ—1.5): 0.7190
SUGGESTED_STOP:     8.7710
SCORE:              25/35 (71%) â€” Tier BOA
SCOUT_STATE:        SETUP
STRUCTURE:          AT_WEEKLY_HIGH â€” resistance zone
TREND:              BULLISH
KEY_LEVELS:
  R: 9.48
  S: 8.56
  7D_AVG: 8.94
INVALIDATION:       Close below 7D_AVG (8.94)
BTC_MASTER_FILTER:  INACTIVE (BTC BULLISH â€” altcoin signals unmodified)
```

---

## Market Data at Entry (Morning Scan â€” 2026-04-08 16:23 UTC)

```
PRICE:              9.22 USDT
24H_CHANGE:         +7.46%
7D_DEV:             +2.15% vs 7D avg (9.03)
RSI_14:             50.62
MACD_TREND:         BULLISH
MACD_HISTOGRAM:     0.041133
OBV_TREND:          RISING
VOLUME_FLOW:        STRONG
ATR_14:             0.4790
STOP_DIST (ATRÃ—1.5): 0.7190
SUGGESTED_STOP:     8.5010
SCORE:              25/35 (71%) â€” Tier BOA
SCOUT_STATE:        WATCHLIST
STRUCTURE:          ABOVE_7D_AVG â€” upper half of range
TREND:              BULLISH
KEY_LEVELS:
  R: 9.66
  S: 8.46
  7D_AVG: 9.03
INVALIDATION:       Close below 7D_AVG (9.03)
BTC_MASTER_FILTER:  INACTIVE (BTC BULLISH â€” altcoin signals unmodified)
NOTE:               Price pulled back from 9.49 to 9.22 during governance period. Flow signals
                    remain aligned (MACD BULLISH, OBV RISING, VOLUME STRONG). State moved from
                    SETUP to WATCHLIST but entry thesis intact â€” stop recalculated from 9.22.
```

---

## Score Breakdown (25/35)

```
CRITERIA       SCORE  MAX   NOTES
Liquidity        3     5    Mid-cap L1; updated from 2/5 to 3/5 on 2026-04-08 scan
Volume           5     5    STRONG volume flow confirmed by OBV RISING
Structure        2     5    WATCHLIST on entry day (pulled back from SETUP on 2026-04-06)
Narrative        4     5    AVAX L1 ecosystem narrative active
Relative Str.    4     5    +2.15% vs 7D avg; top-10 leaderboard rank
Execution        5     5    Binance spot available, standard spread
Potential        2     5    SIMULATE phase â€” partial scoring active
TOTAL           25    35    71% â€” Tier BOA
```

---

## Position Sizing

```
CAPITAL:            100.00 USDT
RISK_PCT:           1.00%
RISK_AMOUNT:        1.00 USDT
ENTRY_PRICE:        9.22
STOP_LOSS:          8.501  (entry âˆ’ ATRÃ—1.5 = 9.22 âˆ’ 0.719)
STOP_DISTANCE:      0.719 USDT

POSITION_SIZE:      1.39 AVAX  (risk Ã· stop_dist = 1.00 Ã· 0.719)
POSITION_VALUE:     12.82 USDT (1.39 Ã— 9.22)
CAPITAL_DEPLOYED:   12.82%     (12.82 of 100 USDT)
MAX_LOSS_USDT:      1.00 USDT  (confirmed = 1% of capital)
```

---

## Exit Rules

```
ENTRY_PRICE:        9.220
STOP_LOSS:          8.501   (ATR Ã— 1.5 below entry â€” absolute stop, no exceptions)
TARGET_1 (1:2):     10.658  (entry + stop_dist Ã— 2 = 9.220 + 1.438)
TARGET_2 (1:3):     11.377  (entry + stop_dist Ã— 3 = 9.220 + 2.157)
FIBONACCI_0.382:    10.118  (R=9.66 + rangeÃ—0.382, range=9.66âˆ’8.46=1.20)
FIBONACCI_0.618:    10.402  (R=9.66 + rangeÃ—0.618)
FIBONACCI_1.000:    10.860  (R=9.66 + rangeÃ—1.000 â€” full extension)
RR_RATIO:           1:2 minimum / 1:3 preferred
TIME_STOP:          7 days from entry (expires 2026-04-15)

TRAILING_STOP_RULES:
  +1R (price â‰¥ 9.939) â†’ stop moves to break-even (9.220)
  +2R (price â‰¥ 10.658) â†’ stop moves to +1R (9.939)
  +3R (price â‰¥ 11.377) â†’ stop moves to +2R (10.658)
  Update every closed 4H candle. Stop never moves down.

PARTIAL_EXIT_RULES:
  50% Securing:     liquidate 50% of position when ROI â‰¥ 50% on risk
                    (~$0.50 gain = AVAX at â‰ˆ9.580, approaching Fib 0.382 zone)
  Fib 0.382 (10.12): first partial + prepare for resistance
  Fib 0.618 (10.40): second partial â€” let core run
  Fib 1.000 (10.86): full extension from Sâ†’R range

ABSOLUTE_EXIT_TRIGGERS:
  1. Stop-loss hit (8.501) â†’ EXIT IMMEDIATELY
  2. Close below 7D_AVG (9.03) â†’ EXIT (invalidation)
  3. Close below support (8.46) â†’ EXIT IMMEDIATELY
  4. OBV + RSI bearish divergence simultaneously â†’ EXIT
  5. MACD crossover negative â†’ REDUCE 50%
  6. News Sentinel HIGH severity adverse (AVAX-specific) â†’ REEVALUATE
  7. Time stop: 7 days no development â†’ CLOSE (2026-04-15)
```

---

## MAC Assessment

```
AGENT: MAC/Playbook Analyst
SYMBOL: AVAXUSDT
DATE: 2026-04-06 04:47 UTC
CONFIDENCE: 7

MOVIMENTO:    alta
ACELERACAO:   positiva
CONFIRMACAO:  confirmada
MAC_VALID:    YES

SETUP_IDENTIFIED: Breakout
SETUP_QUALITY:    CLEAN

PLAYBOOK_CHECKLIST:
  PONTO_1_NARRATIVA:         OK    â€” AVAX L1 ecosystem narrative active; top leaderboard scorer today
  PONTO_2_BTC_CONTEXT:       OK    â€” BTC BULLISH, master filter INACTIVE; altcoin signals unmodified
  PONTO_3_MAJORS:            OK    â€” ETH WATCHLIST (+3.70%), SOL WATCHLIST (+2.08%); majors supporting
  PONTO_4_ESTRUTURA:         OK    â€” Scout confirms SETUP; TREND BULLISH; AT_WEEKLY_HIGH with break
  PONTO_5_ROMPIMENTO:        OK    â€” Price at 9.49 broke above R=9.48; OBV RISING confirms volume
  PONTO_6_VOLUME:            OK    â€” OBV RISING; VOLUME_FLOW STRONG; 24h range 9.69% vs 5.01% avg
  PONTO_7_LIQUIDEZ:          OK    â€” AVAX top-20 asset on Binance; standard spread; Liq score 3/5
  PONTO_8_INVALIDACAO:       OK    â€” Stop defined at 8.501 (ATRÃ—1.5); invalidation at 7D_AVG 9.03
  PONTO_9_RISCO:             OK    â€” 1.39 AVAX; risk $1.00; 12.82% capital deployed; within limits
  PONTO_10_ALVO:             OK    â€” Target 1 at 10.658 (1:2); Target 2 at 11.377 (1:3)
  PONTO_11_RR_RATIO:         OK    â€” RR = 1:2 minimum met; 1:3 preferred achievable at 11.377
  PONTO_12_PLANO_NAO_EMOCAO: OK    â€” Systematic scanner entry; plan-driven; governance period respected
  CHECKLIST_SCORE: 12/12

RISK_NOTE: Overall news severity on entry day is HIGH (BTC/Iran ceasefire, SEC enforcement).
           None directly impact AVAX L1 narrative. SIMULATE activation proceeds per governance schedule.

EXIT_POLICY:
  STOP_LOSS:     8.501 (ATR Ã— 1.5 = 0.719 below entry 9.22)
  TAKE_PROFIT:   10.658 (1:2) | 11.377 (1:3)
  FIBONACCI:     10.118 (0.382) | 10.402 (0.618) â€” Fibonacci Matrix partials
  TRAILING_STOP: activate at +1R (â‰¥9.939) â†’ move stop to break-even; escalate with each R gained
  TIME_STOP:     2026-04-15 (7 days from entry)
  50_SECURING:   liquidate 50% at â‰ˆ9.580 when ROI â‰¥ 50% on risk capital
  RR_RATIO:      1:2 (minimum) / 1:3 (preferred)

PLAYBOOK_STATE: PLAYBOOK_OK
REASON: All 3 MAC pillars confirmed at identification. 12/12 checklist. Flow signals remain
        aligned at entry (MACD BULLISH, OBV RISING). Entry price 9.22 recalculates stops
        and targets â€” RR ratio preserved. Governance period completed as required.
NEXT_AGENT: Execution Orchestrator
```

---

## Pipeline Status at Entry (2026-04-08)

```
SCOUT:              WATCHLIST â€” AVAXUSDT (25/35 BOA); pullback from SETUP on 2026-04-06
FLOW_ANALYST:       CONFIRMS â€” RSI 50.62 / MACD BULLISH / OBV RISING / VOLUME STRONG
NEWS_SENTINEL:      OVERALL_SEVERITY HIGH â€” no AVAX-specific adverse event identified
SCORE_ENGINE:       25/35 BOA â€” Tier qualifies for SIMULATE entry
MAC_ANALYST:        PLAYBOOK_OK â€” 12/12 checklist / Breakout CLEAN / MAC_VALID YES
QUANT_RISK:         APPROVED â€” 1% risk / 12.82% capital / ATR-based stop / within limits
EXECUTION_ORCH:     EXECUTION_ALLOWED â€” governance cleared; flow aligned; entry at 9.22
DEVOPS_GUARDIAN:    PIPELINE_STATUS HEALTHY â€” infrastructure OK at entry time
QUALITY_CONTROL:    VALIDATED â€” all outputs schema-compliant; entry recorded
```

---

## Governance & Execution Gate

```
EXECUTION_STATE:    SIMULATE_ACTIVE
GOVERNANCE_TYPE:    Type 3 â€” SIMULATE phase activation
48H_PERIOD_START:   2026-04-06
48H_PERIOD_END:     2026-04-08
REQUIRED_APPROVAL:  Formal Type 3 checklist sign-off (GOVERNANCA_DE_MUDANCAS_REVISADO.md)

ACTIONS COMPLETED ON 2026-04-08:
  [x] Confirmed Type 3 governance approval signed off â€” SIMULATE mode ACTIVE
  [x] Re-ran morning scan â€” AVAXUSDT WATCHLIST / BULLISH / MACD+OBV aligned
  [x] Re-checked news severity â€” no AVAX-specific HIGH adverse event
  [x] Ran Quant/Risk Officer (04) structured risk scoring â€” APPROVED
  [x] Ran Execution Orchestrator (05) â€” EXECUTION_ALLOWED
  [x] Ran Quality Control (10) â€” outputs validated
  [x] Opened simulated position at 9.22 (market price on 2026-04-08)
```

---

## Journal Notes

```
RATIONALE: AVAXUSDT identified as top-ranked asset on 2026-04-06 morning scan (Score 25/35, BOA).
           Breakout above R=9.48 with SETUP state, full OBV+MACD alignment, and #1 leaderboard
           position met all playbook entry criteria. 48h governance period initiated for SIMULATE
           phase activation.

ENTRY_EXECUTION_NOTE (2026-04-08): SIMULATE mode formally activated after 48h governance period.
           Price has pulled back from 9.49 to 9.22 during the governance window (-2.8%). State
           moved from SETUP to WATCHLIST but all flow signals remain aligned (MACD BULLISH,
           OBV RISING, VOLUME STRONG). Stop and targets recalculated from new entry price 9.22:
           stop 8.501, T1 10.658, T2 11.377. Entry executed at 9.22 per SIMULATE protocol.

AVAX_CONTEXT: Layer-1 smart contract platform competing with ETH/SOL. Narrative driven by
              ecosystem growth, DeFi TVL, and institutional interest in alternative L1s. No
              AVAX-specific adverse news detected at entry.

SIMULATE_NOTE: This is Euru OS Paper Trade 001 â€” first live simulation entry. No real capital
               deployed. All figures are for simulation tracking and learning purposes only.
               Results feed into the Paperclip evaluation and pre-EXECUTE phase assessment.

RISK_PARAMETERS_CONFIRMED:
  Max loss if stop hit: -1.00 USDT (-1.00% of 100 USDT capital)
  Position is 12.82% of capital â€” within single-asset exposure limits
  ATR-based stop provides systematic invalidation independent of emotion

NEXT_REVIEW: 2026-04-09 â€” daily scan + check price action vs key levels
TIME_STOP:   2026-04-15 â€” close if no development after 7 days
```

---

*Generated: 2026-04-06 | Updated: 2026-04-08 â€” SIMULATE_ACTIVE | Source: SCOUT_REPORT_2026-04-06.md / SCOUT_REPORT_2026-04-08.md*
