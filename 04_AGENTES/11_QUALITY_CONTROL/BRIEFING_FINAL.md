Documento: EURU_AGENTS_QUALITY_CONTROL_BRIEFING
Owner: Governança Euru
Status: OFFICIAL
Versão: v1.0
Última atualização: 2026-04-11
Documento pai: EURU_MASTER_DOCUMENTO_OFFICIAL_v1.1
Substitui: BRIEFING_FINAL.md de 09_QUALITY_CONTROL e 10_QUALITY_CONTROL (legacy-unversioned)
Escopo: Briefing canônico do agente 11 — Quality Control. Define identidade,
        responsabilidades, posição no pipeline e critérios de decisão.

---

# EURU — AGT-11 Quality Control
## Briefing Canônico

---

## Changelog

v1.0 — 2026-04-11
- Consolidado a partir das pastas 09_QUALITY_CONTROL e 10_QUALITY_CONTROL.
- Aplicado cabeçalho canônico conforme Migration Policy.
- Conteúdo unificado — versão de 10_ usada como base (mais recente).
- Artefatos de origem movidos para 99_ARQUIVO_E_NOTAS/ (ver manifesto T03).

---

## 1. Identidade

**Nome:** Quality Control
**Número canônico:** 11
**Tipo:** Gate de validação de dados
**Posição no pipeline:** penúltimo gate antes do Execution Orchestrator

---

## 2. Missão

Garantir que nenhuma decisão de trade seja tomada com base em dados
inválidos, corrompidos, incompletos ou desatualizados.

O Quality Control não analisa mercado. Ele analisa os dados que chegaram
ao pipeline — e decide se são confiáveis o suficiente para sustentar
uma decisão.

---

## 3. Posição no pipeline

```
... → MAC/Playbook Analyst (10) → QUALITY CONTROL (11) → Execution Orchestrator (05)
```

O QC é acionado após a validação metodológica e antes da decisão final.
Se bloquear, o ciclo termina em NO_TRADE sem passar pelo Orchestrator.

---

## 4. Responsabilidades

**Valida:**
- presença e completude de todos os campos obrigatórios nos relatórios;
- coerência temporal (timestamps dentro da janela aceitável);
- faixas plausíveis para valores numéricos;
- consistência entre fonte de dados e ciclos anteriores;
- ausência de dados duplicados ou reciclados do ciclo anterior.

**Não valida:**
- interpretação de mercado;
- qualidade da análise dos agentes anteriores;
- decisão de risco ou tamanho de posição.

---

## 5. Autoridade

O bloqueio do Quality Control é irrecorrível no ciclo atual.
Um `DATA_BLOCKED` resulta em `NO_TRADE` obrigatório — o Execution
Orchestrator não é acionado.

Um `DATA_WARNING` passa o controle ao Execution Orchestrator com
a informação do campo problemático. O Orchestrator decide com cautela.

---

## 6. Relacionamentos

| Direção | Agente | Natureza |
|---|---|---|
| Recebe de | MAC / Playbook Analyst (10) | Confirmação de aderência metodológica |
| Recebe de | Score Engine (08) | Score consolidado para verificação de completude |
| Alimenta | Execution Orchestrator (05) | Status de integridade dos dados |
| Reporta a | Journal Auditor (07) | Incidentes de dados bloqueados |
| Relacionado com | Watchdog (09) | QC valida dados; Watchdog valida heartbeat |
