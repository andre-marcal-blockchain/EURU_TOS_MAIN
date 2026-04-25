# EURU_TOS — Official Schema for Trade and Journal Files
Version: 1.0
Status: Active
Owner: EURU_TOS Governance
Applies to:
- 08_DADOS_E_JOURNAL/JOURNAL_TRADES/
- 08_DADOS_E_JOURNAL/JOURNAL_DAILY/
- euru_learning_engine.py
- all AI agents writing trade or journal records

## 1. Purpose

This document defines the official schema for:

1. Paper trade files
2. Daily journal files

The objective is to make Euru_TOS:
- machine-readable
- governance-friendly
- auditable
- consistent across agents
- reliable for the learning engine

This schema is the source of truth.

## 2. Core Principles

1. Every file must be valid Markdown (`.md`)
2. Every file must start with YAML front matter
3. Front matter is the machine-readable layer
4. Markdown body is the human-readable layer
5. Required fields must never be omitted
6. Unknown values must be written as `null`, never guessed
7. Dates must use ISO 8601 format
8. Numeric fields must be stored as numbers, without symbols
9. Enum values must use lowercase_snake_case
10. Agents must not rename keys, headings, or enums

## 3. Global Rules

### 3.1 Encoding
- UTF-8

### 3.2 Decimal format
- Use dot as decimal separator
- Example: `1.75`, `-3.42`, `0.50`

### 3.3 Percent fields
- Store numeric value only
- Example:
  - `pnl_pct: 12.5`
  - not `pnl_pct: "12.5%"`

### 3.4 Null values
- Use `null`
- Never use:
  - `""`
  - `N/A`
  - `unknown`
  - `-`

### 3.5 Dates
- Date only: `YYYY-MM-DD`
- Datetime: `YYYY-MM-DDTHH:MM:SSZ`
- If local timezone is needed, use ISO 8601 with offset
- Example: `2026-04-12T20:30:00+02:00`

### 3.6 Arrays
Use YAML lists.

### 3.7 Boolean values
Use:
- `true`
- `false`

## 4. Folder Scope

### 4.1 Trade files
Folder:
`08_DADOS_E_JOURNAL/JOURNAL_TRADES/`

### 4.2 Daily journal files
Folder:
`08_DADOS_E_JOURNAL/JOURNAL_DAILY/`

> If `JOURNAL_DAILY/` does not yet exist, it should be created.
> Legacy `JOURNAL_*.md` files outside this folder may still be read by fallback logic, but this schema defines the official location.

## 5. File Naming Convention

### 5.1 Paper trade files
Pattern:
`PAPER_TRADE_<trade_id>_<symbol>_<entry_date>.md`

Example:
`PAPER_TRADE_PT002_FETUSDT_2026-04-10.md`

### 5.2 Daily journal files
Pattern:
`JOURNAL_<date>.md`

Example:
`JOURNAL_2026-04-12.md`

## 6. Official Enum Dictionary

### 6.1 Trade status
- `planned`
- `open`
- `closed`
- `cancelled`
- `invalidated`

### 6.2 Side
- `long`
- `short`

### 6.3 Intent type
- `open`
- `add`
- `hedge`
- `reduce`
- `close`
- `recovery_3x`
- `unwind`

### 6.4 Margin mode
- `cross`
- `isolated`

### 6.5 Position mode
- `one_way`
- `hedge`

### 6.6 Risk state
- `low`
- `medium`
- `high`
- `critical`

### 6.7 News severity
- `none`
- `low`
- `medium`
- `high`
- `critical`

### 6.8 MAC state
- `bullish`
- `bearish`
- `neutral`
- `transition`
- `countertrend`
- `invalid`

### 6.9 Setup type
- `trend_continuation`
- `trend_reversal`
- `breakout`
- `pullback`
- `range_reclaim`
- `range_rejection`
- `mean_reversion`
- `news_reaction`
- `hedge_management`
- `recovery_3x`
- `unwind_exit`
- `custom`

### 6.10 Exit reason
- `take_profit`
- `stop_loss`
- `manual_close`
- `time_stop`
- `thesis_invalidated`
- `hedge_adjustment`
- `recovery_3x_exit`
- `unwind_exit`
- `risk_off`
- `news_risk`
- `system_rule`
- `other`

### 6.11 System phase
- `simulate`
- `execute`

### 6.12 Market regime
- `bull_trend`
- `bear_trend`
- `range`
- `volatile`
- `unclear`
- `event_driven`

## 7. PAPER TRADE Schema

Every paper trade file must follow this structure.

### 7.1 Required front matter fields

```yaml
---
schema_type: paper_trade
schema_version: 1.0

trade_id: PT002
status: closed
system_phase: simulate

symbol: FETUSDT
venue: binance_futures
contract_type: perpetual
market_type: usds_m
asset_class: altcoin_future

side: long
intent_type: open
setup_type: trend_reversal

entry_datetime: 2026-04-10T09:15:00Z
entry_price: 0.8421
entry_score: 8.4
mac_state_at_entry: bullish
risk_state_at_entry: medium
news_severity_at_entry: low

margin_mode: cross
position_mode: hedge
leverage: 5
quantity: 1200
notional_usdt: 1010.52

stop_loss: 0.7910
take_profit: 1.0240
planned_rr: 3.56

exit_datetime: 2026-04-14T16:40:00Z
exit_price: 1.0135
pnl_usdt: 205.68
pnl_pct: 20.35
rr_achieved: 3.35
exit_reason: take_profit

days_held: 4
score_prediction_label: winner_candidate
score_prediction_confidence: 0.81

linked_trade_ids: []
tags:
  - mac
  - reversal
  - high_conviction
---
```

### 7.2 Optional trade fields

```yaml
parent_trade_id: null
hedge_for_trade_id: null
recovery_group_id: null
unwind_group_id: null
max_drawdown_pct: null
max_profit_pct: null
funding_cost_usdt: null
fees_usdt: null
slippage_estimate_usdt: null
agent_name: null
agent_version: null
human_approval_required: false
human_approval_status: null
```

### 7.3 Body structure for PAPER TRADE files

```md
# Trade Summary

## Thesis
Short explanation of the trade idea.

## Entry Reasoning
Why the trade was taken, including setup logic and context.

## Risk Plan
Initial stop, target, invalidation logic, and portfolio risk context.

## Management Notes
Optional updates while trade was open.

## Exit Notes
Why the trade was closed and whether execution matched the original plan.

## Lessons Learned
What worked, what failed, and what should be improved.
```

### 7.4 Rules by trade status

If `status: open`, the following fields must be `null`:
- `exit_datetime`
- `exit_price`
- `pnl_usdt`
- `pnl_pct`
- `rr_achieved`
- `exit_reason`
- `days_held`

If `status: closed`, all exit fields must be filled.

## 8. JOURNAL Schema

### 8.1 Required front matter fields

```yaml
---
schema_type: daily_journal
schema_version: 1.0

journal_date: 2026-04-12
system_phase: simulate
system_status: healthy

market_regime: volatile
btc_macro_state: bearish
portfolio_risk_state: medium
news_severity_max: medium

open_positions_count: 4
new_trades_count: 2
closed_trades_count: 1
watchlist_changes_count: 3
blockers_count: 1

key_theme_of_day: capital_preservation
summary_score: 7.8

tags:
  - volatility
  - learning
  - discipline
---
```

### 8.2 Required journal body structure

```md
# Daily Summary

## Daily Observations
- Market observations
- Behavioral observations
- Execution observations

## Lessons Learned
- Clear lessons extracted from the day

## Deviations
- Any process deviation, agent deviation, or governance breach
- If none, write: `- none`

## Watchlist Changes
- Added assets
- Removed assets
- Assets moved to caution or blocked state
- If none, write: `- none`

## Pending Decisions for Human Approval
- Anything requiring human governance
- If none, write: `- none`

## Next-Day Focus
- Top priorities for the next trading day
```

## 9. Parser Contract for Euru Learning Engine

1. Attempt to parse YAML front matter.
2. Validate `schema_type` and `schema_version`.
3. If valid, trust front matter as source of truth and use body only for qualitative analysis.
4. If front matter is missing, fallback to legacy flexible parsing and mark file as `legacy_format_detected`.
5. If required fields are missing, mark file as `invalid_schema` and do not silently infer critical values.
6. Log validation warnings to the learning report.

## 10. Readiness Check Rules

After 20 or more closed trades, suggest `execute_candidate` only if:
- `win_rate >= 50`
- `average_rr >= 2.0`
- `expectancy > 0`

Otherwise remain in `simulate` and provide concrete improvement actions.

## 11. Governance Suggestion Types

### Type 1 — immediate_adjustment
Use for:
- watchlist removal
- hard blocking repeated failing asset
- fixing broken parser assumptions
- urgent checklist additions

### Type 2 — review_24h
Use for:
- score threshold refinement
- setup rule tuning
- news filter adjustment
- risk parameter review

### Type 3 — strategic_48h
Use for:
- framework redesign
- setup taxonomy changes
- portfolio allocation changes
- major governance changes

## 12. Official PAPER TRADE Template

```md
---
schema_type: paper_trade
schema_version: 1.0

trade_id: PTXXX
status: open
system_phase: simulate

symbol: ASSETUSDT
venue: binance_futures
contract_type: perpetual
market_type: usds_m
asset_class: altcoin_future

side: long
intent_type: open
setup_type: trend_continuation

entry_datetime: 2026-04-12T00:00:00Z
entry_price: 0.0000
entry_score: 0.0
mac_state_at_entry: neutral
risk_state_at_entry: medium
news_severity_at_entry: none

margin_mode: cross
position_mode: hedge
leverage: 1
quantity: 0
notional_usdt: 0.0

stop_loss: 0.0000
take_profit: 0.0000
planned_rr: 0.0

exit_datetime: null
exit_price: null
pnl_usdt: null
pnl_pct: null
rr_achieved: null
exit_reason: null

days_held: null
score_prediction_label: winner_candidate
score_prediction_confidence: 0.0

linked_trade_ids: []
tags: []
---

# Trade Summary

## Thesis
...

## Entry Reasoning
...

## Risk Plan
...

## Management Notes
...

## Exit Notes
...

## Lessons Learned
...
```

## 13. Official JOURNAL Template

```md
---
schema_type: daily_journal
schema_version: 1.0

journal_date: 2026-04-12
system_phase: simulate
system_status: healthy

market_regime: unclear
btc_macro_state: neutral
portfolio_risk_state: medium
news_severity_max: none

open_positions_count: 0
new_trades_count: 0
closed_trades_count: 0
watchlist_changes_count: 0
blockers_count: 0

key_theme_of_day: discipline
summary_score: 0.0

tags: []
---

# Daily Summary

## Daily Observations
- ...

## Lessons Learned
- ...

## Deviations
- none

## Watchlist Changes
- none

## Pending Decisions for Human Approval
- none

## Next-Day Focus
- ...
```

## 14. Non-Negotiable Rules for All Agents

1. Do not invent missing required numeric values
2. Do not change enum labels
3. Do not rename official headings
4. Do not mix Portuguese and English in enum fields
5. Do not write percentages with `%` inside numeric YAML fields
6. Do not close a trade without filling exit data
7. Do not use body text as substitute for front matter
8. Do not treat legacy format as official format

## 15. Migration Rule

Legacy files may continue to exist.

However:
- all new files must follow this schema
- legacy files should be migrated gradually
- once migrated, YAML front matter becomes authoritative

## 16. Final Authority

If there is any conflict between old flexible parsing, agent assumptions, or legacy markdown habits, this schema wins.
