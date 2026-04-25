---
schema_type: paper_trade
schema_version: 1.0

trade_id: PT2
status: closed
system_phase: simulate

symbol: NEARUSDT
venue: binance_futures
contract_type: perpetual
market_type: usds_m
asset_class: altcoin_future

side: long
intent_type: open
setup_type: trend_continuation

entry_datetime: 2026-04-09T00:00:00Z
entry_price: 1.2450
entry_score: 0.0
mac_state_at_entry: bullish
risk_state_at_entry: medium
news_severity_at_entry: low

margin_mode: cross
position_mode: hedge
leverage: 5
quantity: 0
notional_usdt: 0.0

stop_loss: 1.2272
take_profit: 0.0
planned_rr: 0.0

exit_datetime: 2026-04-15T09:00:00Z
exit_price: 1.41
pnl_usdt: 0.62
pnl_pct: 0.62
rr_achieved: 0.62
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
- Time stop expired 2026-04-15 (7 days). Price at 1.41 vs entry 1.34. Profit +0.62 USDT (+0.62R). Neither stop nor T1 were reached.

## Lessons Learned
- Entry at AT_WEEKLY_HIGH (R=1.34) proved valid — price held above resistance and converted it to support. However, momentum was insufficient to reach T1 (1.5656). OBV dropped from RISING to FLAT during the hold period. Time stop discipline effective — exited with profit instead of waiting for reversal.

---

## Original Content (Legacy)

# PAPER TRADE 002 â€” NEARUSDT
**Euru OS â€” Simulate Phase Entry**

---

## Trade Header

```
TRADE_ID:           PAPER_TRADE_002
ASSET:              NEARUSDT
DATE_IDENTIFIED:    2026-04-08
TIME_IDENTIFIED:    16:23 UTC
DATE_ENTERED:       2026-04-08
ENTRY_PRICE:        1.34
SOURCE_REPORT:      SCOUT_REPORT_2026-04-08.md
EXECUTION_STATE:    SIMULATE_ACTIVE
GOVERNANCE_NOTE:    SIMULATE mode active (Type 3 sign-off completed 2026-04-08). Same-day entry
                    permitted under active SIMULATE phase â€” no additional governance wait required.
SYSTEM_MODE:        SIMULATE (ACTIVE â€” 2026-04-08)
OPERATOR:           Andre Marcal
```

---

## Market Data at Entry (Morning Scan â€” 2026-04-08 16:23 UTC)

```
PRICE:              1.34 USDT
24H_CHANGE:         +8.47%
7D_DEV:             +9.18% vs 7D avg (1.23)
RSI_14:             61.57
MACD_TREND:         BULLISH
MACD_HISTOGRAM:     0.012261
OBV_TREND:          RISING
VOLUME_FLOW:        STRONG
ATR_14:             0.0752
STOP_DIST (ATRÃ—1.5): 0.1128
SUGGESTED_STOP:     1.2272
SCORE:              25/35 (71%) â€” Tier BOA
SCOUT_STATE:        SETUP
STRUCTURE:          AT_WEEKLY_HIGH â€” resistance zone
TREND:              BULLISH
KEY_LEVELS:
  R: 1.34
  S: 1.14
  7D_AVG: 1.23
INVALIDATION:       Close below 7D_AVG (1.23)
BTC_MASTER_FILTER:  INACTIVE (BTC BULLISH â€” altcoin signals unmodified)
```

---

## Score Breakdown (25/35)

```
CRITERIA       SCORE  MAX   NOTES
Liquidity        3     5    Mid-cap L1; NEAR Protocol â€” adequate but not BTC/ETH depth
Volume           5     5    STRONG volume flow confirmed by OBV RISING
Structure        5     5    SETUP confirmed; AT_WEEKLY_HIGH breakout structure
Narrative        3     5    NEAR Protocol AI/L1 ecosystem narrative; moderate strength
Relative Str.    4     5    +9.18% vs 7D avg â€” top-10 rank (11th leaderboard); strong momentum
Execution        5     5    Binance spot available, standard spread
Potential        0     5    Potential score 0 in current scoring snapshot
TOTAL           25    35    71% â€” Tier BOA
```

*Score source: SCOUT_REPORT_2026-04-08.md leaderboard rank 11.*

---

## Position Sizing

```
CAPITAL:            100.00 USDT
RISK_PCT:           1.00%
RISK_AMOUNT:        1.00 USDT
ENTRY_PRICE:        1.3400
STOP_LOSS:          1.2272  (entry âˆ’ ATRÃ—1.5 = 1.340 âˆ’ 0.1128)
STOP_DISTANCE:      0.1128 USDT

POSITION_SIZE:      8.87 NEAR  (risk Ã· stop_dist = 1.00 Ã· 0.1128)
POSITION_VALUE:     11.89 USDT (8.87 Ã— 1.34)
CAPITAL_DEPLOYED:   11.89%     (11.89 of 100 USDT)
MAX_LOSS_USDT:      1.00 USDT  (confirmed = 1% of capital)

TOTAL_CAPITAL_AT_RISK (PT001 + PT002): 24.71% â€” within multi-position exposure limits
```

---

## Exit Rules

```
ENTRY_PRICE:        1.3400
STOP_LOSS:          1.2272  (ATR Ã— 1.5 below entry â€” absolute stop, no exceptions)
TARGET_1 (1:2):     1.5656  (entry + stop_dist Ã— 2 = 1.340 + 0.2256)
TARGET_2 (1:3):     1.6784  (entry + stop_dist Ã— 3 = 1.340 + 0.3384)
FIBONACCI_0.382:    1.4164  (R=1.34 + rangeÃ—0.382, range=1.34âˆ’1.14=0.20)
FIBONACCI_0.618:    1.4636  (R=1.34 + rangeÃ—0.618)
FIBONACCI_1.000:    1.5400  (R=1.34 + rangeÃ—1.000 â€” full extension from Sâ†’R)
RR_RATIO:           1:2 minimum / 1:3 preferred
TIME_STOP:          7 days from entry (expires 2026-04-15)

TRAILING_STOP_RULES:
  +1R (price â‰¥ 1.4528) â†’ stop moves to break-even (1.3400)
  +2R (price â‰¥ 1.5656) â†’ stop moves to +1R (1.4528)
  +3R (price â‰¥ 1.6784) â†’ stop moves to +2R (1.5656)
  Update every closed 4H candle. Stop never moves down.

PARTIAL_EXIT_RULES:
  50% Securing:     liquidate 50% of position when ROI â‰¥ 50% on risk
                    (~$0.50 gain = NEAR at â‰ˆ1.396, approaching Fib 0.382 zone)
  Fib 0.382 (1.416): first partial + prepare for resistance
  Fib 0.618 (1.464): second partial â€” let core run
  Fib 1.000 (1.540): full extension from Sâ†’R range

ABSOLUTE_EXIT_TRIGGERS:
  1. Stop-loss hit (1.2272) â†’ EXIT IMMEDIATELY
  2. Close below 7D_AVG (1.23) â†’ EXIT (invalidation)
  3. Close below support (1.14) â†’ EXIT IMMEDIATELY
  4. OBV + RSI bearish divergence simultaneously â†’ EXIT
  5. MACD crossover negative â†’ REDUCE 50%
  6. News Sentinel HIGH severity adverse (NEAR-specific) â†’ REEVALUATE
  7. Time stop: 7 days no development â†’ CLOSE (2026-04-15)

RESISTANCE_NOTE:    Entry is AT_WEEKLY_HIGH (R=1.34 = entry price). A clean close above 1.34
                    on volume is required for full breakout confirmation. If price stalls at
                    1.34â€“1.42 zone without a high-volume close, reassess before T1.
```

---

## MAC Assessment

```
AGENT: MAC/Playbook Analyst
SYMBOL: NEARUSDT
DATE: 2026-04-08 16:23 UTC
CONFIDENCE: 7

MOVIMENTO:    alta
ACELERACAO:   positiva
CONFIRMACAO:  confirmada
MAC_VALID:    YES

SETUP_IDENTIFIED: Breakout
SETUP_QUALITY:    CLEAN

PLAYBOOK_CHECKLIST:
  PONTO_1_NARRATIVA:         OK    â€” NEAR Protocol AI/L1 narrative; moderate ecosystem strength
  PONTO_2_BTC_CONTEXT:       OK    â€” BTC BULLISH, master filter INACTIVE; altcoin signals unmodified
  PONTO_3_MAJORS:            OK    â€” BTC SETUP (+4.84%), ETH SETUP (+6.78%); macro environment supportive
  PONTO_4_ESTRUTURA:         OK    â€” Scout confirms SETUP; TREND BULLISH; AT_WEEKLY_HIGH breakout
  PONTO_5_ROMPIMENTO:        OK    â€” Price at 1.34 at/breaking weekly high R; OBV RISING confirms volume
  PONTO_6_VOLUME:            OK    â€” OBV RISING; VOLUME_FLOW STRONG; 24h range 11.75% vs 5.79% avg
  PONTO_7_LIQUIDEZ:          OK    â€” NEAR listed Binance; standard spread; Liq score 3/5 acceptable
  PONTO_8_INVALIDACAO:       OK    â€” Stop at 1.2272 (ATRÃ—1.5); hard invalidation at 7D_AVG 1.23
  PONTO_9_RISCO:             OK    â€” 8.87 NEAR; risk $1.00; 11.89% capital deployed; within limits
  PONTO_10_ALVO:             OK    â€” T1 at 1.566 (1:2); T2 at 1.678 (1:3)
  PONTO_11_RR_RATIO:         OK    â€” RR = 1:2 minimum met; 1:3 preferred achievable at 1.678
  PONTO_12_PLANO_NAO_EMOCAO: OK    â€” Systematic scanner entry; plan-driven; SIMULATE active
  CHECKLIST_SCORE: 12/12

RISK_NOTE: Overall news severity on entry day is HIGH (BTC/Iran ceasefire, SEC enforcement).
           None directly impact NEAR Protocol narrative. RSI at 61.57 is elevated â€” monitor
           for overbought extension above 70. Entry at AT_WEEKLY_HIGH requires clean breakout
           confirmation; failure to hold 1.34 on volume â†’ reduce exposure.

EXIT_POLICY:
  STOP_LOSS:     1.2272 (ATR Ã— 1.5 = 0.1128 below entry 1.34)
  TAKE_PROFIT:   1.5656 (1:2) | 1.6784 (1:3)
  FIBONACCI:     1.416 (0.382) | 1.464 (0.618) â€” Fibonacci Matrix partials
  TRAILING_STOP: activate at +1R (â‰¥1.4528) â†’ move stop to break-even; escalate with each R gained
  TIME_STOP:     2026-04-15 (7 days from entry)
  50_SECURING:   liquidate 50% at â‰ˆ1.396 when ROI â‰¥ 50% on risk capital
  RR_RATIO:      1:2 (minimum) / 1:3 (preferred)

PLAYBOOK_STATE: PLAYBOOK_OK
REASON: All 3 MAC pillars confirmed. 12/12 checklist. Breakout structure clean with full volume
        confirmation (OBV RISING + VOLUME STRONG). BTC filter inactive (supportive). RSI 61.57
        is elevated but not overbought â€” room for continuation. +9.18% vs 7D avg is the strongest
        deviation on the watchlist. Narrative score 3/5 noted â€” offset by strong flow alignment.
NEXT_AGENT: Execution Orchestrator
```

---

## Pipeline Status at Entry (2026-04-08)

```
SCOUT:              SETUP â€” NEARUSDT (25/35 BOA); AT_WEEKLY_HIGH; +9.18% vs 7D avg
FLOW_ANALYST:       CONFIRMS â€” RSI 61.57 / MACD BULLISH / OBV RISING / VOLUME STRONG
NEWS_SENTINEL:      OVERALL_SEVERITY HIGH â€” no NEAR-specific adverse event identified
SCORE_ENGINE:       25/35 BOA â€” Tier qualifies for SIMULATE entry
MAC_ANALYST:        PLAYBOOK_OK â€” 12/12 checklist / Breakout CLEAN / MAC_VALID YES
QUANT_RISK:         APPROVED â€” 1% risk / 11.89% capital / ATR-based stop / within limits
EXECUTION_ORCH:     EXECUTION_ALLOWED â€” SIMULATE phase active; flow aligned; entry at 1.34
DEVOPS_GUARDIAN:    PIPELINE_STATUS HEALTHY â€” infrastructure OK at entry time
QUALITY_CONTROL:    VALIDATED â€” all outputs schema-compliant; entry recorded
```

---

## Journal Notes

```
RATIONALE: NEARUSDT ranks 11th on the 2026-04-08 morning scan with Score 25/35 (BOA). The
           +9.18% deviation from the 7D average is the highest momentum reading among all
           BOA-tier SETUP assets on this scan. Structure is AT_WEEKLY_HIGH â€” a clean breakout
           candidate with full flow alignment (MACD BULLISH, OBV RISING, VOLUME STRONG).
           Entry is coincident with SIMULATE mode activation on 2026-04-08.

NEAR_CONTEXT: NEAR Protocol is a Layer-1 smart contract platform with a focus on AI-native
              infrastructure and developer experience. Narrative moderate â€” ecosystem growing
              but below ETH/SOL prominence. No NEAR-specific adverse news detected at entry.

AT_WEEKLY_HIGH_NOTE: Entry at the exact resistance level (R=1.34) means price must prove
              breakout strength. If price rejects 1.34 and closes below 7D_AVG (1.23),
              trade is invalidated. Monitor first 2â€“3 daily closes closely.

SIMULATE_NOTE: Paper Trade 002. No real capital deployed. Euru OS SIMULATE phase is now
               active with two concurrent paper positions (PT001 AVAX + PT002 NEAR).
               Total simulated capital at risk: 24.71% â€” within exposure guidelines.

RISK_PARAMETERS_CONFIRMED:
  Max loss if stop hit: -1.00 USDT (-1.00% of 100 USDT capital)
  Position is 11.89% of capital â€” within single-asset exposure limits
  Combined with PT001 (12.82%): total deployed 24.71% â€” acceptable
  ATR-based stop provides systematic invalidation independent of emotion

NEXT_REVIEW: 2026-04-09 â€” daily scan + verify NEAR holding above 7D_AVG 1.23 + breakout volume
TIME_STOP:   2026-04-15 â€” close if no development after 7 days
```

---

*Generated: 2026-04-08 | Euru OS â€” SIMULATE_ACTIVE | Source: SCOUT_REPORT_2026-04-08.md*
