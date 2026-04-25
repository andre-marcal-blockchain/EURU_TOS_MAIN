Documento: EURU_SETUP_TREND_CONTINUATION
Owner: Governança Euru
Status: OFFICIAL
Versão: v1.0
Última atualização: 2026-04-12
Documento pai: EURU_GOVERNANCE_RULES_MasterRules_OFFICIAL_v1.1
Substitui: N/A
Escopo: Define os critérios obrigatórios, disqualificadores e checklist
        de validação para o setup trend_continuation no Euru OS.
        Responde ao pedido de revisão do Friday Cycle de 2026-04-12.

---

# EURU — Setup: Trend Continuation
## Definição Operacional Canônica

---

## Changelog

v1.0 — 2026-04-12
- Criação do documento em resposta ao REVIEW_REQUIRED do Friday Cycle.
- Critérios baseados em dados reais dos PAPER_TRADE_001, 002, 003
  e SCOUT_REPORT_2026-04-06 a 2026-04-11.
- Aprovado pelo operador como Opção A (validar com regras mínimas).

---

## 1. Definição do setup

**Trend Continuation** é um setup de entrada na direcção de uma tendência
já estabelecida, após confirmação técnica de continuação pelo pipeline
de agentes do Euru OS.

Não é uma entrada em qualquer movimento de alta ou baixa.
É uma entrada com múltiplas confirmações alinhadas.

---

## 2. Critérios obrigatórios — todos devem ser verdadeiros

### 2.1 Filtro macro BTC (Gate 1 — bloqueante)

| Critério | Condição obrigatória |
|---|---|
| BTC Trend | BULLISH (para longs) / BEARISH (para shorts) |
| BTC vs 7D_AVG | Acima (para longs) / Abaixo (para shorts) |
| BTC Master Filter | INACTIVE (não bloqueado) |

Se o BTC Master Filter estiver ACTIVE, todos os sinais de altcoin
são automaticamente rebaixados para WATCHLIST.
**Nenhuma entrada trend_continuation é permitida com filtro activo.**

---

### 2.2 Confirmação técnica da altcoin (Gate 2 — bloqueante)

| Indicador | Condição obrigatória |
|---|---|
| Tendência (Trend) | BULLISH (long) / BEARISH (short) |
| Estrutura | ABOVE_7D_AVG (long) / BELOW_7D_AVG (short) |
| MACD_TREND | BULLISH (long) / BEARISH (short) |
| OBV_TREND | RISING (long) / FALLING (short) |
| RSI_14 | Entre 45 e 70 para long / Entre 30 e 55 para short |

Todos os 5 indicadores devem estar alinhados.
Se qualquer um contradizer, o setup é INCONCLUSIVE — não é trend_continuation.

---

### 2.3 Score mínimo (Gate 3 — bloqueante)

| Parâmetro | Mínimo obrigatório |
|---|---|
| Score Engine (0–35) | ≥ 20 / 35 |
| Tier | BOA ou superior |
| MAC_VALID | YES |
| PLAYBOOK_STATE | PLAYBOOK_OK |

Score abaixo de 20 = setup rejeitado automaticamente pelo Quant/Risk Officer.

---

### 2.4 Volume e liquidez (Gate 4 — bloqueante)

| Parâmetro | Condição obrigatória |
|---|---|
| VOLUME_FLOW | STRONG ou MODERATE |
| Ativo na Watchlist | Tier 1 ou Tier 2 |
| Ativo na Lista Proibida | NÃO pode estar |

Volume WEAK = setup rejeitado.

---

## 3. Disqualificadores — qualquer um bloqueia a entrada

| # | Disqualificador |
|---|---|
| D-01 | BTC Master Filter ACTIVE |
| D-02 | RSI acima de 75 (sobrecompra extrema para long) |
| D-03 | RSI abaixo de 25 (sobrevenda extrema para short) |
| D-04 | MACD_TREND e OBV_TREND em direcções opostas |
| D-05 | Preço de entrada acima da resistência imediata (sem pullback) |
| D-06 | News Sentinel com severidade HIGH ou CRITICAL |
| D-07 | Score abaixo de 20/35 |
| D-08 | Ativo na Lista Proibida da Watchlist |
| D-09 | DevOps Guardião com INFRA_DEGRADED ou pior |
| D-10 | Quality Control com DATA_WARNING ou DATA_BLOCKED |

---

## 4. Checklist de validação pré-entrada

Todos os campos devem estar marcados antes de qualquer entrada
com setup trend_continuation:

```
□ BTC Master Filter INACTIVE
□ BTC acima da 7D_AVG (para long)
□ Altcoin com Trend BULLISH (para long)
□ Altcoin ABOVE_7D_AVG
□ MACD_TREND BULLISH
□ OBV_TREND RISING
□ RSI entre 45 e 70
□ Score ≥ 20/35
□ VOLUME_FLOW STRONG ou MODERATE
□ MAC_VALID YES
□ PLAYBOOK_STATE PLAYBOOK_OK
□ Nenhum disqualificador presente
□ Stop definido antes da entrada (ATR × 1.5)
□ Risco ≤ 1% do capital
```

14/14 obrigatórios. Qualquer campo não marcado = NO_TRADE.

---

## 5. Outputs esperados dos agentes

Para uma entrada trend_continuation ser válida, o pipeline deve
produzir exactamente estes outputs:

| Agente | Output obrigatório |
|---|---|
| Scout (01) | `SETUP` |
| Flow Analyst (02) | `CONFIRMS` |
| News Sentinel (03) | `CLEAR` ou `CAUTION` administrável |
| MAC/Playbook Analyst (10) | `PLAYBOOK_OK` |
| Quant/Risk Officer (04) | `APPROVE` |
| Quality Control (11) | `DATA_OK` |
| Execution Orchestrator (05) | `EXECUTION_ALLOWED` |

Qualquer desvio = setup inválido para este tipo.

---

## 6. Gestão durante a operação

| Condição | Acção obrigatória |
|---|---|
| MACD inverte para BEARISH | Reduzir 50% da posição |
| OBV inverte para FALLING | Avaliar saída — reavaliar em próximo candle |
| Preço cai abaixo da 7D_AVG | Saída por invalidação de tese |
| Stop atingido | Saída imediata — sem excepções |
| RSI ultrapassa 80 | Considerar saída parcial (50%) |

---

## 7. Critério de sucesso do setup

Após 20+ trades com setup trend_continuation, o learning engine
avaliará este setup com os seguintes targets mínimos:

| Métrica | Target |
|---|---|
| Win rate | ≥ 55% |
| Average R:R | ≥ 2.5:1 |
| Expectancy | > 0.3 |
| Prediction accuracy | ≥ 65% |

Se o setup não atingir estes valores em 30+ trades,
abrir revisão Type 3 (48h estratégica).

---

## 8. Relação com outros documentos

| Documento | Relação |
|---|---|
| EURU_GOVERNANCE_RULES_MasterRules_OFFICIAL_v1.1 | Limites absolutos de risco |
| EURU_RISK_FRAMEWORK_RiskMatrix_OFFICIAL_v1.0 | Cálculo de posição |
| EURU_DATA_WATCHLIST_OfficialWatchlist_OFFICIAL_v1.2 | Lista de ativos elegíveis |
| EURU_GOVERNANCE_STANDARD_StatusDefinitions_OFFICIAL_v1.0 | Vocabulário de outputs |
| EURU_OPERATIONS_PROMPT_PreTrade_OFFICIAL_v1.0 | Gate pré-trade |
