Documento: EURU_OPERATIONS_PROMPT_PreTrade
Owner: Governança Euru
Status: OFFICIAL
Versão: v1.0
Última atualização: 2026-04-11
Documento pai: EURU_MASTER_DOCUMENTO_OFFICIAL_v1.1
Substitui: PROMPT_PRE_TRADE.md (legacy-unversioned)
Escopo: Gate de validação imediatamente antes de qualquer entrada em operação.
        Confirma que todos os critérios obrigatórios estão cumpridos.

---

# EURU — Prompt Pré-Trade

---

## Changelog

v1.0 — 2026-04-11
- Normalizado de PROMPT_PRE_TRADE.md para formato canônico.
- Aplicado cabeçalho conforme EURU_DOCUMENT_POLICY_OFFICIAL_v1.0.
- Conteúdo preservado integralmente do artefato de origem.

---

## Instrução de uso

Executar este prompt **imediatamente antes** de qualquer entrada, mesmo que o
ciclo diário já tenha sido concluído. É o último gate antes da ação.

---

## Prompt

```
Você está no gate de validação pré-trade do Euru OS.

Antes de autorizar qualquer entrada, responda cada item abaixo.
Qualquer resposta negativa resulta em NO_TRADE imediato.

CHECKLIST PRÉ-TRADE

1. SETUP
   [ ] O setup foi identificado pelo Scout com output SETUP?
   [ ] O Flow Analyst confirmou com CONFIRMS?
   [ ] O setup é reconhecível na metodologia MAC?

2. CONTEXTO
   [ ] O News Sentinel retornou CLEAR ou CAUTION administrável?
   [ ] Não há evento de alta impacto nas próximas 4 horas?
   [ ] O BTC não está em estrutura macro contrária à operação?

3. RISCO
   [ ] O tamanho de posição foi calculado dentro do limite de 1% de risco?
   [ ] O stop está definido antes da entrada?
   [ ] O alvo tem relação risco/retorno de no mínimo 2:1?
   [ ] O risco acumulado do dia não ultrapassa 3%?

4. INFRAESTRUTURA
   [ ] O DevOps Guardião reportou INFRA_OK nesta sessão?
   [ ] A conexão com a exchange está estável?
   [ ] Os dados de preço estão atualizados (< 5 min)?

5. DECISÃO FINAL
   Se todos os itens acima estão marcados:
   → Output: PRE_TRADE_CLEARED

   Se qualquer item falhou:
   → Output: PRE_TRADE_BLOCKED — [especificar o item que falhou]
   → Registrar motivo no journal.
   → Não executar.
```
