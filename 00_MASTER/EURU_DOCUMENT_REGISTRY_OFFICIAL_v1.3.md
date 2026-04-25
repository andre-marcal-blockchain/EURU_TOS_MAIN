Documento: EURU_DOCUMENT_REGISTRY
Owner: Governança Euru
Status: OFFICIAL
Versão: v1.3
Última atualização: 2026-04-11
Documento pai: EURU_MASTER_DOCUMENTO_OFFICIAL_v1.1
Substitui: EURU_DOCUMENT_REGISTRY_OFFICIAL_v1.2.md
Escopo: Índice único dos documentos canônicos. Estado final após execução
        completa de todos os tracks de normalização e produção do Runbook.

---

# EURU — DOCUMENT REGISTRY
## Catálogo Operacional — Estado Final

---

## Changelog

v1.3 — 2026-04-11
- A11 Quality Control: 3 artefatos canônicos produzidos em 11_QUALITY_CONTROL/.
  Status: OFFICIAL ✅. Migração física documentada e pronta para execução.
- L-13 Watchlist: promovida para v1.1. Critérios validados. Ativos marcados
  como PENDING_OPERATOR_REVIEW para o próximo ciclo.
- Runbook do Operador adicionado ao registry (G-14).
- Backlog opcional formalizado na secção 10.

v1.2 — 2026-04-11
- Tracks 01, 02 e 03 completos. 14 legados normalizados.

v1.1 — 2026-04-11
- ADR_0002, Migration Policy, Legacy Triage e AGT-06/07 incorporados.

v1.0 — 2026-04-11
- Criação inicial.

---

## 1. Regra de uso

Este Registry é a **primeira consulta obrigatória** antes de qualquer
acção documental. Toda IA que entre no projecto começa aqui.

---

## 2. Legenda de localização

| Alias | Caminho real |
|---|---|
| `PKG-MR/` | `euru_master_registry_package_v1_1/` |
| `PKG-GOV/` | `euru_documentation_pack_v1_0/` |
| `PKG-STATE/` | `euru_operational_state_package_v1_0/` |
| `PKG-BL/` | `EURU_BACKLOG_RESOLVED/` |
| `PKG-NORM/T01/` | `EURU_NORMALIZED/T01/` |
| `PKG-NORM/T02/` | `EURU_NORMALIZED/T02/` |
| `PKG-NORM/T03/` | `EURU_NORMALIZED/T03/` |
| `PKG-FINAL/` | `EURU_FINAL/` |
| `SNAP/` | `Euru_TOS_extracted/Euru_TOS/` |

---

## 3. Core de governança

| ID | Documento | Status | Localização |
|---|---|---|---|
| G-01 | Master Documento | OFFICIAL v1.1 | `PKG-MR/EURU_MASTER_DOCUMENTO_OFFICIAL_v1.1.md` |
| G-02 | Document Policy | OFFICIAL v1.0 | `PKG-GOV/EURU_DOCUMENT_POLICY_OFFICIAL_v1.0.md` |
| G-03 | Template Header + Changelog | OFFICIAL v1.0 | `PKG-GOV/EURU_DOCUMENT_TEMPLATE_HEADER_CHANGELOG.md` |
| G-04 | Prompt Mestre para Outra IA | OFFICIAL v1.0 | `PKG-GOV/EURU_MASTER_PROMPT_OTHER_IA.md` |
| G-05 | Estado Operacional Canônico | OFFICIAL v1.0 | `PKG-STATE/EURU_GOVERNANCE_OPERATIONAL_STATE_OFFICIAL_v1.0.md` |
| G-06 | ADR_0001 — Canonical State READ_ONLY | OFFICIAL v1.0 | `PKG-STATE/ADR_0001_EURU_CANONICAL_OPERATIONAL_STATE_READ_ONLY.md` |
| G-07 | ADR_0002 — QC Canonical Folder | OFFICIAL v1.0 | `PKG-BL/ADR_0002_EURU_QUALITY_CONTROL_CANONICAL_FOLDER.md` |
| G-08 | Handoff Prompt — Canonical State | OFFICIAL v1.0 | `PKG-STATE/EURU_HANDOFF_PROMPT_CANONICAL_STATE_OTHER_IA.md` |
| G-09 | Handoff Prompt — Master + Registry | OFFICIAL v1.0 | `PKG-MR/EURU_HANDOFF_PROMPT_MASTER_REGISTRY_OTHER_IA.md` |
| G-10 | Normalization Snippets | OFFICIAL v1.0 | `PKG-STATE/EURU_NORMALIZATION_TEXT_SNIPPETS.md` |
| G-11 | Migration Policy for Legacy Artifacts | OFFICIAL v1.0 | `PKG-BL/EURU_GOVERNANCE_POLICY_LegacyMigration_OFFICIAL_v1.0.md` |
| G-12 | Legacy Artifact Triage | OFFICIAL v1.0 | `PKG-BL/EURU_GOVERNANCE_LEGACY_TRIAGE_OFFICIAL_v1.0.md` |
| G-13 | Document Registry | OFFICIAL v1.3 | `PKG-FINAL/EURU_DOCUMENT_REGISTRY_OFFICIAL_v1.3.md` |
| G-14 | Runbook do Operador | OFFICIAL v1.0 | `PKG-FINAL/RUNBOOK/EURU_OPERATIONS_RUNBOOK_DocumentalBacklog_OFFICIAL_v1.0.md` |

---

## 4. Governança normalizada

| ID | Documento canônico | Status | Localização |
|---|---|---|---|
| L-01 | EURU_GOVERNANCE_RULES_MasterRules | OFFICIAL v1.1 | `PKG-NORM/T01/` |
| L-02 | EURU_GOVERNANCE_POLICY_ChangeManagement | OFFICIAL v1.0 | `PKG-NORM/T01/` |
| L-03 | EURU_GOVERNANCE_STANDARD_StatusDefinitions | OFFICIAL v1.0 | `PKG-NORM/T01/` |
| L-04 | EURU_GOVERNANCE_POLICY_HumanResponsibilities | OFFICIAL v1.0 | `PKG-NORM/T01/` |

---

## 5. Prompts operacionais normalizados

| ID | Documento canônico | Status | Localização |
|---|---|---|---|
| L-05 | EURU_OPERATIONS_PROMPT_DailyOperation | OFFICIAL v1.0 | `PKG-NORM/T01/` |
| L-06 | EURU_OPERATIONS_PROMPT_PreTrade | OFFICIAL v1.0 | `PKG-NORM/T01/` |
| L-07 | EURU_OPERATIONS_PROMPT_PostTrade | OFFICIAL v1.0 | `PKG-NORM/T01/` |
| L-08 | EURU_OPERATIONS_PROMPT_WeeklyReview | OFFICIAL v1.0 | `PKG-NORM/T01/` |

---

## 6. Risco, arquitetura e logs

| ID | Documento canônico | Status | Localização |
|---|---|---|---|
| L-09 | EURU_RISK_FRAMEWORK_RiskMatrix | OFFICIAL v1.0 | `PKG-NORM/T01/` |
| L-10 | EURU_OPERATIONS_POLICY_ReadOnlyMode | OFFICIAL v1.0 | `PKG-NORM/T02/` |
| L-11 | EURU_RISK_POLICY_ExitPolicy | OFFICIAL v1.0 | `PKG-NORM/T02/` |
| L-12 | EURU_ARCHITECTURE_DIAGRAM_PipelineLogic | OFFICIAL v1.0 | `PKG-NORM/T01/` |
| L-13 | EURU_DATA_WATCHLIST_OfficialWatchlist | OFFICIAL v1.1 | `PKG-FINAL/` — ativos PENDING_OPERATOR_REVIEW |
| L-14 | EURU_LOGS_REGISTRY_IncidentLog | OFFICIAL v1.0 | `PKG-NORM/T01/` |

---

## 7. Matriz canônica dos agentes

| Agente | Nº | Briefing | Output Format | Prompt | Status |
|---|---:|---|---|---|---|
| Scout | 01 | `A01/BRIEFING_FINAL.md` | `A01/OUTPUT_FORMAT_FINAL.md` | `A01/PROMPT_REVISADO.md` | REVIEW-NAME / CANONICAL-CONTENT |
| Flow Analyst | 02 | `A02/BRIEFING_FINAL.md` | `A02/OUTPUT_FORMAT_FINAL.md` | `A02/PROMPT_REVISADO.md` | REVIEW-NAME / CANONICAL-CONTENT |
| News Sentinel | 03 | `A03/BRIEFING_FINAL.md` | `A03/OUTPUT_FORMAT_FINAL.md` | `A03/PROMPT_REVISADO.md` | REVIEW-NAME / CANONICAL-CONTENT |
| Quant / Risk Officer | 04 | `A04/BRIEFING_FINAL.md` | `A04/OUTPUT_FORMAT_FINAL.md` | `A04/PROMPT_REVISADO.md` | REVIEW-NAME / CANONICAL-CONTENT |
| Execution Orchestrator | 05 | `A05/BRIEFING_FINAL.md` | `A05/OUTPUT_FORMAT_FINAL.md` | `A05/PROMPT_REVISADO.md` | REVIEW-NAME / CANONICAL-CONTENT |
| DevOps Guardião | 06 | `A06/BRIEFING_FINAL.md` | `A06/OUTPUT_FORMAT_FINAL.md` | `PKG-BL/EURU_AGENTS_DEVOPS_GUARDIAO_PROMPT_OFFICIAL_v1.0.md` | **OFFICIAL ✅** |
| Journal Auditor | 07 | `A07/BRIEFING_FINAL.md` | `A07/OUTPUT_FORMAT_FINAL.md` | `PKG-BL/EURU_AGENTS_JOURNAL_AUDITOR_PROMPT_OFFICIAL_v1.0.md` | **OFFICIAL ✅** |
| Score Engine | 08 | `A08/BRIEFING_FINAL.md` | `A08/OUTPUT_FORMAT_FINAL.md` | `A08/PROMPT_REVISADO.md` | REVIEW-NAME / CANONICAL-CONTENT |
| Watchdog | 09 | `A09/BRIEFING_FINAL.md` | `A09/OUTPUT_FORMAT_FINAL.md` | `A09/08_WATCHDOG_PROMPT_REVISADO.txt` | REVIEW-NAME / CANONICAL-CONTENT |
| MAC / Playbook Analyst | 10 | `A10/BRIEFING_FINAL.md` | `A10/OUTPUT_FORMAT_FINAL.md` | `A10/PROMPT_REVISADO.md` | REVIEW-NAME / CANONICAL-CONTENT |
| Quality Control | 11 | `PKG-FINAL/11_QUALITY_CONTROL/BRIEFING_FINAL.md` | `PKG-FINAL/11_QUALITY_CONTROL/OUTPUT_FORMAT_FINAL.md` | `PKG-FINAL/11_QUALITY_CONTROL/EURU_AGENTS_QUALITY_CONTROL_PROMPT_OFFICIAL_v1.0.md` | **OFFICIAL ✅** — migração física pendente |

---

## 8. Itens de backlog opcional (não bloqueiam operação)

| Item | PROC | Prioridade |
|---|---|---|
| AGT-01 a 05, 08, 10: renomear prompts `_REVISADO` | PROC-01 | Baixa |
| AGT-09 Watchdog: converter prompt `.txt` → `.md` | PROC-02 | Baixa |
| AGT-11: executar migração física no repositório | PROC-03 | Média — quando repositório for reorganizado |
| L-13 Watchlist: operador valida ativos no próximo ciclo | Manual | Alta — antes do próximo ciclo |

---

## 9. Estado operacional canônico

**READ_ONLY** — conforme ADR_0001 e G-05.
Nenhuma IA altera este estado sem novo documento OFFICIAL.
