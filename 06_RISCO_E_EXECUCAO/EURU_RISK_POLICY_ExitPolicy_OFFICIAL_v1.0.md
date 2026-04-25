Documento: EURU_RISK_POLICY_ExitPolicy
Owner: Governança Euru
Status: OFFICIAL
Versão: v1.0
Última atualização: 2026-04-11
Documento pai: EURU_GOVERNANCE_RULES_MasterRules_OFFICIAL_v1.1
Substitui: Politica_Saida_Completa_Euru.txt (legacy-unversioned)
Escopo: Política completa de saída de operações do Euru OS. Define todos os
        cenários de encerramento: stop, alvo, saída parcial, saída forçada
        e saída por deterioração de contexto.

---

# EURU — Política de Saída de Operações

---

## Changelog

v1.0 — 2026-04-11
- Normalizado de Politica_Saida_Completa_Euru.txt (.txt → .md) para formato canônico.
- Aplicado cabeçalho conforme EURU_DOCUMENT_POLICY_OFFICIAL_v1.0.
- Conteúdo revisado para verificar completude — estrutura expandida para cobrir
  todos os cenários de saída identificados no ecossistema.
- Alinhado com limites da EURU_GOVERNANCE_RULES_MasterRules_OFFICIAL_v1.1.

---

## 1. Princípio fundamental de saída

**O plano de saída é definido antes da entrada.** Qualquer operação sem saída
pré-definida viola as Regras-Mãe e deve ser encerrada imediatamente.

---

## 2. Tipos de saída

### 2.1 Saída por stop (perda planejada)
- O stop é atingido pelo preço.
- A operação é encerrada imediatamente, sem hesitação.
- **Não existe "aguardar para ver se volta".**
- O stop é uma decisão tomada antes da entrada — não se renegocia durante a operação.

### 2.2 Saída por alvo (lucro planejado)
- O alvo é atingido pelo preço.
- A operação é encerrada imediatamente, ou parte da posição é reduzida.
- Manter posição além do alvo requer novo setup com novo stop e novo alvo definidos
  antes de continuar — não é extensão automática.

### 2.3 Saída parcial (gestão de posição)
- Quando o preço atinge 60–70% do caminho até o alvo, é permitido reduzir
  a posição em até 50%.
- O stop do saldo remanescente é movido para o ponto de entrada (breakeven).
- Esta ação deve ser registrada no journal com justificativa.

### 2.4 Saída por deterioração de contexto
Encerrar a operação antes do stop ou alvo quando:
- News Sentinel emite `VETO` durante a operação;
- DevOps Guardião emite `SYSTEM_DEGRADED` ou `CRITICAL_FAILURE`;
- estrutura de mercado muda significativamente (reversão de tendência macro);
- o ativo apresenta spike de volatilidade sem narrativa identificável.

Nestes casos, a saída é registrada como "saída por contexto" no journal.

### 2.5 Saída forçada por modo seguro
Quando o sistema entra em modo seguro (drawdown 10% ou `CRITICAL_FAILURE`):
- avaliar saída conservadora da posição aberta;
- priorizar preservação de capital em detrimento de recuperação de posição;
- registrar como "saída forçada — modo seguro" no journal.

---

## 3. O que nunca fazer ao sair

| Comportamento proibido | Razão |
|---|---|
| Mover stop para baixo (ampliar perda) | Viola limite de risco |
| Adicionar à posição perdedora (average down) | Proibido pelas Regras-Mãe |
| Aguardar depois que o stop foi atingido | Stop é para ser respeitado |
| Sair sem registrar no journal | Viola política de rastreabilidade |
| Reentrar no mesmo ativo no mesmo ciclo após stop | Requer novo setup em novo ciclo |

---

## 4. Registro obrigatório de saída

Toda saída gera entrada no Journal Auditor com:
- tipo de saída (stop / alvo / parcial / contexto / forçada);
- preço de saída;
- resultado em % do capital;
- motivo se for saída não-planejada;
- aprendizado mínimo de uma linha.

---

## 5. Relação com outros documentos

- Limites de risco: EURU_GOVERNANCE_RULES_MasterRules_OFFICIAL_v1.1
- Dimensionamento da posição: EURU_RISK_FRAMEWORK_RiskMatrix_OFFICIAL_v1.0
- Registro: AGT-07 Journal Auditor
- Modo seguro: EURU_OPERATIONS_POLICY_ReadOnlyMode_OFFICIAL_v1.0
