# 04_QUANT/RISK OFFICER — Output Format Revisado (versão definitiva)

## Standard Output

AGENT: Quant/Risk Officer
SYMBOL: [ex: NEARUSDT]
DATE: [YYYY-MM-DD HH:MM UTC]
CONFIDENCE: [0-10]

ATR_14: [valor numérico]
CAPITAL_TOTAL: [USDT disponível]
CATEGORY: [Core | Growth | Asymmetric | Speculative]
CATEGORY_ALLOCATION: [% usado / % permitido]

POSITION_SIZE: [unidades do activo]
POSITION_VALUE_USDT: [valor em USDT]
STOP_DISTANCE: [ATR × 1.5 ou nível técnico]
STOP_LOSS: [preço]
TAKE_PROFIT:
  TARGET_1: [preço — rácio 1:2]
  TARGET_2: [preço — rácio 1:3]
FIBONACCI_EXITS:
  0.382: [preço]
  0.500: [preço]
  0.618: [preço]

RISK_REWARD_RATIO: [ex: 1:2.5]
DAILY_RISK_USED: [% do limite 2%]
WEEKLY_RISK_USED: [% do limite 5%]

RISK_STATE: [APPROVE | REJECT | REVIEW]
REASON: [breve justificação — ex: risco 0.8% e R/R 2.5:1, categoria dentro dos limites]
NEXT_AGENT: [MAC Analyst | None]

## Rules
- Use only official risk states: APPROVE, REJECT, REVIEW.
- Fill ATR_14 from Flow Analyst output — never estimate.
- POSITION_SIZE = CAPITAL_TOTAL × 1% / (ATR_14 × 1.5).
- STOP_DISTANCE must reference ATR or a specific technical level.
- TAKE_PROFIT must reference Fibonacci matrix or equivalent method.
- REASON must be one concise sentence explaining the decision.
- CONFIDENCE: 0-3 data missing or limits critical | 4-6 marginal parameters | 7-8 all within limits | 9-10 ideal R/R >= 1:3.

## Example

AGENT: Quant/Risk Officer
SYMBOL: NEARUSDT
DATE: 2026-04-05 07:00 UTC
CONFIDENCE: 8

ATR_14: 0.0712
CAPITAL_TOTAL: 100 USDT
CATEGORY: Asymmetric
CATEGORY_ALLOCATION: 0% used / 15% allowed

POSITION_SIZE: 9.36 NEAR
POSITION_VALUE_USDT: 11.79 USDT
STOP_DISTANCE: 0.1068 (ATR × 1.5)
STOP_LOSS: 1.1512
TAKE_PROFIT:
  TARGET_1: 1.4720 (1:2)
  TARGET_2: 1.5828 (1:3)
FIBONACCI_EXITS:
  0.382: 1.3800
  0.500: 1.4200
  0.618: 1.5500

RISK_REWARD_RATIO: 1:2.5
DAILY_RISK_USED: 1% of 2% limit
WEEKLY_RISK_USED: 1% of 5% limit

RISK_STATE: APPROVE
REASON: Risk 1% of capital, R/R 2.5:1 above minimum 2:1, category allocation within 15% limit.
NEXT_AGENT: MAC Analyst
