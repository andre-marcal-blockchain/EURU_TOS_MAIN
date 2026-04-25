Documento: EURU_GOVERNANCE_STANDARD_StatusDefinitions
Owner: Governança Euru
Status: OFFICIAL
Versão: v1.0
Última atualização: 2026-04-11
Documento pai: EURU_MASTER_DOCUMENTO_OFFICIAL_v1.1
Substitui: PADRAO_UNIFICADO_DE_STATUS_REVISADO.md (legacy-unversioned)
Escopo: Vocabulário oficial de todos os estados e outputs do Euru OS. Define
        o significado exato de cada status usado por agentes, documentos e
        no modo operacional do sistema.

---

# EURU — Padrão Unificado de Status e Outputs

---

## Changelog

v1.0 — 2026-04-11
- Normalizado de PADRAO_UNIFICADO_DE_STATUS_REVISADO.md para formato canônico.
- Aplicado cabeçalho conforme EURU_DOCUMENT_POLICY_OFFICIAL_v1.0.
- Conteúdo preservado integralmente do artefato de origem.

---

## 1. Status do modo operacional do sistema

| Status | Significado |
|---|---|
| `READ_ONLY` | Análise apenas. Nenhuma execução ou simulação formal. Estado canônico atual. |
| `SIMULATE` | Paper trading ativo. Nenhuma ordem real na exchange. Requer documento OFFICIAL. |
| `EXECUTE` | Ordens reais. Requer aprovação formal e progressão documentada. |

**Estado canônico atual: `READ_ONLY`**
(conforme EURU_GOVERNANCE_OPERATIONAL_STATE_OFFICIAL_v1.0)

---

## 2. Outputs dos agentes de análise

### Scout
| Output | Significado |
|---|---|
| `NO_TRADE` | Estrutura não favorável. Não montar setup. |
| `WATCHLIST` | Ativo em observação. Sem entrada ainda. |
| `SETUP` | Setup identificado. Passar para validação. |

### Flow Analyst
| Output | Significado |
|---|---|
| `CONFIRMS` | Indicadores técnicos confirmam o setup. |
| `CONTRADICTS` | Indicadores contradizem o setup. Bloquear. |
| `INCONCLUSIVE` | Sinais mistos. Tratar como `NO_TRADE` conservador. |

### News Sentinel
| Output | Significado |
|---|---|
| `CLEAR` | Ambiente informacional favorável. |
| `CAUTION` | Evento relevante. Reduzir tamanho ou aguardar. |
| `VETO` | Evento de alta severidade. Bloquear operação. |

### Quant / Risk Officer
| Output | Significado |
|---|---|
| `APPROVE` | Risco calculado. Tamanho, stop e alvo definidos. |
| `REJECT` | Risco fora do limite ou dados insuficientes para cálculo. |

### MAC / Playbook Analyst
| Output | Significado |
|---|---|
| `PLAYBOOK_OK` | Setup aderente à metodologia MAC. |
| `PLAYBOOK_FAIL` | Setup não reconhecido ou fora do método. Bloquear. |

### Execution Orchestrator
| Output | Significado |
|---|---|
| `EXECUTION_ALLOWED` | Todos os gates aprovados. Operação autorizada. |
| `NO_TRADE` | Um ou mais gates bloquearam. Operação não autorizada. |
| `HOLD` | Aguardar confirmação adicional antes de decidir. |

### DevOps Guardião
| Output | Significado |
|---|---|
| `INFRA_OK` | Infraestrutura íntegra. |
| `INFRA_DEGRADED` | Problemas menores. Operar com cautela. |
| `SYSTEM_DEGRADED` | Problemas relevantes. Suspender operação. |
| `CRITICAL_FAILURE` | Falha crítica. Forçar `READ_ONLY`. |
| `PIPELINE_BREAK` | Script ou automação falhou. Investigar antes de prosseguir. |

### Quality Control
| Output | Significado |
|---|---|
| `DATA_OK` | Dados válidos e completos. |
| `DATA_WARNING` | Dados parciais ou com inconsistências menores. |
| `DATA_BLOCKED` | Dados inválidos ou corrompidos. Bloquear pipeline. |

### Watchdog
| Output | Significado |
|---|---|
| `HEARTBEAT_OK` | Sistema operacional e respondendo. |
| `SILENT_FAILURE` | Componente parou sem erro visível. Investigar. |
| `RECOVERY_NEEDED` | Falha confirmada. Acionar recuperação. |

---

## 3. Status documentais

| Status | Significado | Localização |
|---|---|---|
| `DRAFT` | Em elaboração. | `WORKING_DRAFTS/` |
| `REVIEW` | Pronto para revisão. | `WORKING_DRAFTS/` |
| `OFFICIAL` | Aprovado e estável. | `OFFICIAL/` |
| `SUPERSEDED` | Substituído por versão mais recente. | `archive/` |
| `DEPRECATED` | Não mais relevante. | `archive/` |
| `legacy-unversioned` | Conteúdo válido, ainda não normalizado. | snapshot original |

---

## 4. Regra geral de interpretação

Quando um output não estiver listado neste documento, ele deve ser tratado como
não reconhecido e o agente deve ser instruído a reemitir usando o vocabulário
canônico acima.
