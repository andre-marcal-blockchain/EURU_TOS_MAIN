Documento: EURU_GOVERNANCE_LEGACY_TRIAGE
Owner: Governança Euru
Status: OFFICIAL
Versão: v1.0
Última atualização: 2026-04-11
Documento pai: EURU_DOCUMENT_REGISTRY_OFFICIAL_v1.0
Substitui: N/A
Escopo: Triagem formal dos 14 artefatos legacy-unversioned do snapshot Euru_TOS.zip,
        mais os 2 prompts de agentes convertidos nesta sessão. Define nome canônico,
        status de normalização e impacto no Registry para cada item.

---

# EURU — Triagem de Artefatos Legados
## Legacy Artifact Triage v1.0

---

## Changelog

v1.0 — 2026-04-11
- Triagem inicial dos 14 artefatos legacy-unversioned do Registry v1.0.
- Adicionados 2 prompts de agentes convertidos nesta sessão (AGT-06, AGT-07).
- Definido nome canônico, status e próxima ação para cada item.
- Base para atualização do Registry para v1.1.

---

## 1. Critérios de triagem

Cada artefato foi avaliado segundo três perguntas:

1. **Conteúdo canônico?** — O conteúdo ainda é válido e deve ser preservado.
2. **Nome normalizado?** — O nome segue a convenção `EURU_[AREA]_[SUBAREA]_[NOME]_[STATUS]_vX.Y.ext`.
3. **Cabeçalho aplicado?** — Contém metadados: Owner, Status, Versão, Data, Documento pai.

**Status resultante de cada artefato:**

| Código | Significado |
|---|---|
| `NORMALIZE` | Conteúdo ok — precisa de renomeação e cabeçalho |
| `REVIEW_THEN_NORMALIZE` | Conteúdo deve ser revisado antes de normalizar |
| `CONVERTED` | Já convertido nesta sessão — OFFICIAL |
| `SPLIT_RESOLVED` | Duplicidade resolvida por ADR — aguarda migração física |

---

## 2. Tabela de triagem completa

### GOVERNANÇA (L-01 a L-05)

| ID | Nome atual (legado) | Nome canônico proposto | Status de conteúdo | Ação |
|---|---|---|---|---|
| L-01 | `REGRAS_MAE_REVISADO.md` | `EURU_GOVERNANCE_RULES_MasterRules_OFFICIAL_v1.1.md` | ✅ Canônico | `NORMALIZE` |
| L-02 | `GOVERNANCA_DE_MUDANCAS_REVISADO.md` | `EURU_GOVERNANCE_POLICY_ChangeManagement_OFFICIAL_v1.0.md` | ✅ Canônico | `NORMALIZE` |
| L-03 | `PADRAO_UNIFICADO_DE_STATUS_REVISADO.md` | `EURU_GOVERNANCE_STANDARD_StatusDefinitions_OFFICIAL_v1.0.md` | ✅ Canônico | `NORMALIZE` |
| L-04 | `RESPONSABILIDADES_HUMANOS_REVISADO.md` | `EURU_GOVERNANCE_POLICY_HumanResponsibilities_OFFICIAL_v1.0.md` | ✅ Canônico | `NORMALIZE` |

### PROMPTS OPERACIONAIS (L-05 a L-08)

| ID | Nome atual (legado) | Nome canônico proposto | Status de conteúdo | Ação |
|---|---|---|---|---|
| L-05 | `PROMPT_DAILY_OPERATION.md` | `EURU_OPERATIONS_PROMPT_DailyOperation_OFFICIAL_v1.0.md` | ✅ Canônico | `NORMALIZE` |
| L-06 | `PROMPT_PRE_TRADE.md` | `EURU_OPERATIONS_PROMPT_PreTrade_OFFICIAL_v1.0.md` | ✅ Canônico | `NORMALIZE` |
| L-07 | `PROMPT_POST_TRADE.md` | `EURU_OPERATIONS_PROMPT_PostTrade_OFFICIAL_v1.0.md` | ✅ Canônico | `NORMALIZE` |
| L-08 | `PROMPT_WEEKLY_REVIEW.md` | `EURU_OPERATIONS_PROMPT_WeeklyReview_OFFICIAL_v1.0.md` | ✅ Canônico | `NORMALIZE` |

### RISCO E OPERAÇÃO (L-09 a L-11)

| ID | Nome atual (legado) | Nome canônico proposto | Status de conteúdo | Ação |
|---|---|---|---|---|
| L-09 | `RISK_MATRIX.md` | `EURU_RISK_FRAMEWORK_RiskMatrix_OFFICIAL_v1.0.md` | ✅ Canônico | `NORMALIZE` |
| L-10 | `MODO_READ_ONLY.txt` | `EURU_OPERATIONS_POLICY_ReadOnlyMode_OFFICIAL_v1.0.md` | ⚠️ Revisar: `.txt` → `.md`, verificar alinhamento com State doc | `REVIEW_THEN_NORMALIZE` |
| L-11 | `Politica_Saida_Completa_Euru.txt` | `EURU_RISK_POLICY_ExitPolicy_OFFICIAL_v1.0.md` | ⚠️ Revisar: `.txt` → `.md`, verificar completude | `REVIEW_THEN_NORMALIZE` |

### ARQUITETURA E DADOS (L-12 a L-14)

| ID | Nome atual (legado) | Nome canônico proposto | Status de conteúdo | Ação |
|---|---|---|---|---|
| L-12 | `PIPELINE_DIAGRAM.md` | `EURU_ARCHITECTURE_DIAGRAM_PipelineLogic_OFFICIAL_v1.0.md` | ✅ Canônico | `NORMALIZE` |
| L-13 | `WATCHLIST_OFICIAL.md` | `EURU_DATA_WATCHLIST_OfficialWatchlist_OFFICIAL_v1.0.md` | ⚠️ Revisar: documento vivo — verificar se critérios ainda são válidos | `REVIEW_THEN_NORMALIZE` |
| L-14 | `INCIDENTES.md` | `EURU_LOGS_REGISTRY_IncidentLog_OFFICIAL_v1.0.md` | ✅ Canônico | `NORMALIZE` |

### PROMPTS DE AGENTES CONVERTIDOS NESTA SESSÃO

| ID | Nome legado | Nome canônico | Status |
|---|---|---|---|
| A06-P | `06_DEVOPS_GUARDIAO_PROMPT_REVISADO.docx` | `EURU_AGENTS_DEVOPS_GUARDIAO_PROMPT_OFFICIAL_v1.0.md` | `CONVERTED` ✅ |
| A07-P | `07_JOURNAL_AUDITOR_PROMPT_REVISADO.docx` | `EURU_AGENTS_JOURNAL_AUDITOR_PROMPT_OFFICIAL_v1.0.md` | `CONVERTED` ✅ |

---

## 3. Resumo por ação necessária

| Ação | Quantidade | Artefatos |
|---|---|---|
| `NORMALIZE` (rename + cabeçalho) | 11 | L-01,02,03,04,05,06,07,08,09,12,14 |
| `REVIEW_THEN_NORMALIZE` | 3 | L-10, L-11, L-13 |
| `CONVERTED` (concluído) | 2 | A06-P, A07-P |
| `SPLIT_RESOLVED` (aguarda migração física) | 1 | A11 (ADR_0002) |

---

## 4. Regra de priorização para normalização

Ordem recomendada quando a normalização for executada:

1. **Primeiro:** L-01 a L-04 (Governança) — são os documentos de maior autoridade.
2. **Segundo:** L-09, L-10, L-11 (Risco e Operação) — impacto direto na operação.
3. **Terceiro:** L-05 a L-08 (Prompts) — uso diário, mas conteúdo estável.
4. **Quarto:** L-12, L-13, L-14 (Arquitetura e Dados) — importantes, mas menos urgentes.

---

## 5. Impacto sobre o Registry

O Document Registry deve ser atualizado para v1.1 refletindo:
- substitução dos nomes legados pelos nomes canônicos na coluna "Documento canônico atual";
- atualização de status de `legacy-unversioned` para `OFFICIAL` conforme normalização ocorre;
- adição dos 2 prompts convertidos (A06-P, A07-P) na seção de agentes;
- atualização da entrada A11 conforme ADR_0002.
