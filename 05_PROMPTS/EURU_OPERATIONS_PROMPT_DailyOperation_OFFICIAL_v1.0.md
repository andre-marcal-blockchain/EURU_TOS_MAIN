Documento: EURU_OPERATIONS_PROMPT_DailyOperation
Owner: Governança Euru
Status: OFFICIAL
Versão: v1.0
Última atualização: 2026-04-11
Documento pai: EURU_MASTER_DOCUMENTO_OFFICIAL_v1.1
Substitui: PROMPT_DAILY_OPERATION.md (legacy-unversioned)
Escopo: Prompt de orquestração do ciclo operacional diário do Euru OS.
        Ativa e sequencia todos os agentes da sessão morning.

---

# EURU — Prompt de Operação Diária

---

## Changelog

v1.0 — 2026-04-11
- Normalizado de PROMPT_DAILY_OPERATION.md para formato canônico.
- Aplicado cabeçalho conforme EURU_DOCUMENT_POLICY_OFFICIAL_v1.0.
- Conteúdo preservado integralmente do artefato de origem.

---

## Instrução de uso

Este prompt é o ponto de entrada da sessão diária. Deve ser enviado após
confirmação de infraestrutura pelo DevOps Guardião (`INFRA_OK`).

---

## Prompt

```
Você está iniciando o ciclo operacional diário do Euru OS.

Estado operacional canônico: READ_ONLY
Data: [AAAA-MM-DD]
Ciclo: morning

Execute o pipeline na seguinte sequência:

1. SCOUT
   - Leia a estrutura de mercado atual.
   - Identifique tendência, suporte, resistência e compressão.
   - Aplique filtro BTC: o mercado macro favorece ou contradiz operações altcoin?
   - Output: NO_TRADE | WATCHLIST | SETUP

2. FLOW ANALYST (apenas se Scout retornou SETUP)
   - Confirme ou invalide o setup via RSI, MACD, OBV, ATR e aderência à MAC.
   - Output: CONFIRMS | CONTRADICTS | INCONCLUSIVE

3. NEWS SENTINEL
   - Classifique o ambiente informacional das últimas 24h.
   - Identifique narrativas dominantes e eventos de risco.
   - Output: CLEAR | CAUTION | VETO

4. QUANT / RISK OFFICER (apenas se Flow retornou CONFIRMS e News não vetou)
   - Calcule tamanho de posição, stop e alvo.
   - Confirme aderência aos limites das Regras-Mãe.
   - Output: APPROVE | REJECT

5. MAC / PLAYBOOK ANALYST (apenas se Risk retornou APPROVE)
   - Verifique aderência do setup à metodologia MAC.
   - Output: PLAYBOOK_OK | PLAYBOOK_FAIL

6. EXECUTION ORCHESTRATOR
   - Integre todos os outputs anteriores.
   - Emita a decisão final.
   - Output: EXECUTION_ALLOWED | NO_TRADE | HOLD

7. JOURNAL AUDITOR
   - Registre todos os outputs do ciclo.
   - Gere entrada de journal diário.
   - Registre qualquer anomalia ou incidente.

Regras:
- Se qualquer agente emitir veto ou bloqueio, interromper o pipeline naquele ponto.
- O output final do ciclo deve sempre ser registrado, mesmo que seja NO_TRADE.
- Em READ_ONLY, EXECUTION_ALLOWED significa "setup validado para paper trade",
  não "executar ordem real".
```
