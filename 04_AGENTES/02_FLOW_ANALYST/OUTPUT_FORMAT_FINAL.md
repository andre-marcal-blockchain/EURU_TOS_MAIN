# 02_FLOW_ANALYST — Output Format Revisado (versão definitiva)

## Standard Output

AGENT: Flow Analyst
SYMBOL: [ex: NEARUSDT]
TIMEFRAME: [1D | 4H]
DATE: [YYYY-MM-DD HH:MM UTC]
CONFIDENCE: [0-10]

RSI_14: [valor 0-100]
RSI_STATE: [OVERBOUGHT >70 | OVERSOLD <30 | BULLISH_MOMENTUM >50 | BEARISH_MOMENTUM <50]
MACD_12_26_9:
  histogram: [valor numérico]
  signal: [valor numérico]
  trend: [BULLISH | BEARISH | NEUTRAL]
OBV_TREND: [up | down | flat]
VOLUME_FLOW: [STRONG | WEAK | DIVERGENCE]
ATR_14: [valor numérico]
STOP_DIST: [ATR × 1.5]
SUGGESTED_STOP: [preço]

MAC_ASSESSMENT:
  MOVIMENTO: [up | down | neutral]
  ACELERACAO: [increasing | decreasing | flat]
  CONFIRMACAO: [strong | weak | none]

FLOW_STATE: [CONFIRMS | CONTRADICTS | INCONCLUSIVE | REVIEW]
INDICATOR_SUMMARY: [nota breve sobre alinhamento dos indicadores]
REASON: [justificação concisa do flow state]
NEXT_AGENT: [Quant/Risk Officer | None]

## Rules
- Fill every field; use numeric values for indicators where appropriate.
- Do not add free-form text outside the defined fields.
- State must be one of the official flow states.
- INDICATOR_SUMMARY and REASON should be brief and factual (1-3 sentences).
- CONFIDENCE: 0-3 severe divergence | 4-6 mixed signals | 7-8 three of four aligned | 9-10 all four agree.
- Always include STOP_DIST and SUGGESTED_STOP for Quant/Risk Officer.

## Example

AGENT: Flow Analyst
SYMBOL: NEARUSDT
TIMEFRAME: 1D
DATE: 2026-04-05 07:00 UTC
CONFIDENCE: 7

RSI_14: 52.41
RSI_STATE: BULLISH_MOMENTUM
MACD_12_26_9:
  histogram: -0.006148
  signal: 0.012
  trend: BEARISH
OBV_TREND: up
VOLUME_FLOW: STRONG
ATR_14: 0.0712
STOP_DIST: 0.1068
SUGGESTED_STOP: 1.1512

MAC_ASSESSMENT:
  MOVIMENTO: up
  ACELERACAO: increasing
  CONFIRMACAO: strong

FLOW_STATE: INCONCLUSIVE
INDICATOR_SUMMARY: OBV rising with strong volume confirms accumulation. RSI just crossed 50 (early bullish). MACD still slightly bearish — lagging indicator catching up.
REASON: Two of three MAC pillars confirmed. MACD lags but histogram near zero. Mixed picture — monitor for MACD crossover.
NEXT_AGENT: Quant/Risk Officer
