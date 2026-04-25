Documento: EURU_RISK_FRAMEWORK_RiskMatrix
Owner: Governança Euru
Status: OFFICIAL
Versão: v1.0
Última atualização: 2026-04-11
Documento pai: EURU_GOVERNANCE_RULES_MasterRules_OFFICIAL_v1.1
Substitui: RISK_MATRIX.md (legacy-unversioned)
Escopo: Fórmula e matriz de dimensionamento de risco do Euru OS. Define como
        calcular tamanho de posição, stop e relação risco/retorno para cada
        nível de score de decisão.

---

# EURU — Matriz de Risco

---

## Changelog

v1.0 — 2026-04-11
- Normalizado de RISK_MATRIX.md para formato canônico.
- Aplicado cabeçalho conforme EURU_DOCUMENT_POLICY_OFFICIAL_v1.0.
- Conteúdo preservado integralmente do artefato de origem.

---

## 1. Fórmula base de dimensionamento

```
Tamanho da posição = (Capital × Risco por operação) ÷ (Entrada − Stop)

Onde:
- Risco por operação = máximo 1% do capital total
- (Entrada − Stop) = distância em valor absoluto até o stop
```

**Exemplo:**
- Capital: $10.000
- Risco por operação: 1% = $100
- Entrada: $1.000 | Stop: $950 | Distância: $50
- Tamanho = $100 ÷ $50 = 2 unidades do ativo

---

## 2. Matriz de risco por score de decisão

| Score | Nível de confiança | Risco permitido | Alavancagem máxima |
|---|---|---|---|
| 90–100 | Alto | até 1,0% | conforme exchange |
| 75–89 | Médio-alto | até 0,75% | reduzida |
| 60–74 | Médio | até 0,50% | mínima |
| < 60 | Insuficiente | `NO_TRADE` | — |

**Regra:** o score é calculado pelo Score Engine (AGT-08). Quant / Risk Officer
aplica o limite correspondente ao score recebido.

---

## 3. Relação risco/retorno mínima

| Modo operacional | R:R mínimo |
|---|---|
| `READ_ONLY` (paper) | 2:1 recomendado |
| `SIMULATE` | 2:1 obrigatório |
| `EXECUTE` | 2,5:1 obrigatório |

Operações com R:R abaixo do mínimo são rejeitadas pelo Quant / Risk Officer
com output `REJECT`.

---

## 4. Limites de risco acumulado

| Janela | Limite |
|---|---|
| Por operação | 1% do capital |
| Diário | 3% do capital |
| Semanal | 5% do capital |
| Drawdown máximo acumulado | 10% — acionar modo seguro |

Se o drawdown acumulado atingir 10%, o sistema retorna a `READ_ONLY` e permanece
nesse modo até revisão semanal formal com decisão documentada.

---

## 5. Regra de stop obrigatório

Nenhuma operação pode ser iniciada sem stop definido antes da entrada.
Stop definido após a entrada é tratado como ausência de stop — operação rejeitada.

---

## 6. Relação com outros documentos

- Limites absolutos: EURU_GOVERNANCE_RULES_MasterRules_OFFICIAL_v1.1
- Cálculo de score: AGT-08 Score Engine
- Aprovação final: AGT-04 Quant / Risk Officer
