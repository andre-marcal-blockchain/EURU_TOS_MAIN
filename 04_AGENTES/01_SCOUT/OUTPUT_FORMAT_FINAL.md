# 01_SCOUT — Output Format Revisado (versão definitiva)

## Standard Output

AGENT: Scout
SYMBOL: [ex: NEARUSDT]
TIMEFRAME: [1D | 4H]
DATE: [YYYY-MM-DD HH:MM UTC]
CONFIDENCE: [0-10]

TREND: [bullish | bearish | sideways | mixed]
STRUCTURE: [trend | range | channel | at_weekly_high | at_weekly_low]
COMPRESSION: [compression | expansion]

MOVIMENTO: [up | down | neutral]
ACELERACAO: [increasing | decreasing | flat]
CONFIRMACAO: [strong | weak | none]

KEY_LEVELS:
  R: [resistência]
  S: [suporte]
  7D_AVG: [média 7 dias]

INVALIDATION: [preço ou condição que invalida o setup]
BTC_FILTER: [ACTIVE | INACTIVE] — [efeito aplicado se ACTIVE]

STATE: [NO_TRADE | WATCHLIST | SETUP | REVIEW]
SIGNAL: [breakout | pullback | compression_break | none]
REASON: [explicação concisa 1-3 frases]
NEXT_AGENT: [Flow Analyst | None]

## Rules
- Every field must be completed; use the options provided for enumerated fields.
- Do not include free-form text outside the defined fields.
- Status values must match PADRAO_UNIFICADO_DE_STATUS_REVISADO.md.
- Keep REASON short (1-3 sentences) and objective.
- CONFIDENCE: 0-3 insufficient data | 4-6 moderate signal | 7-8 clear signal | 9-10 multiple confirmations.
- If BTC_FILTER is ACTIVE and STATE would be SETUP → change STATE to WATCHLIST and note in REASON.

## Example

AGENT: Scout
SYMBOL: NEARUSDT
TIMEFRAME: 1D
DATE: 2026-04-05 07:00 UTC
CONFIDENCE: 7

TREND: bullish
STRUCTURE: at_weekly_high
COMPRESSION: expansion

MOVIMENTO: up
ACELERACAO: increasing
CONFIRMACAO: strong

KEY_LEVELS:
  R: 1.34
  S: 1.18
  7D_AVG: 1.20

INVALIDATION: Close below 7D_AVG (1.20)
BTC_FILTER: ACTIVE — downgraded SETUP to WATCHLIST (BTC SIDEWAYS)

STATE: WATCHLIST
SIGNAL: breakout
REASON: Price +6.74% above 7D avg with aligned bullish trend and strong volume. Downgraded from SETUP by BTC Master Filter (BTC SIDEWAYS). Monitor for BTC confirmation above $72K.
NEXT_AGENT: Flow Analyst (activate when BTC filter lifts)
