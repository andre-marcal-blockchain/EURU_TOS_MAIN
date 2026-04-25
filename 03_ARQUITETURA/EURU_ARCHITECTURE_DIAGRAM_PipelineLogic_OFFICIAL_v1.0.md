Documento: EURU_ARCHITECTURE_DIAGRAM_PipelineLogic
Owner: Governança Euru
Status: OFFICIAL
Versão: v1.0
Última atualização: 2026-04-11
Documento pai: EURU_MASTER_DOCUMENTO_OFFICIAL_v1.1
Substitui: PIPELINE_DIAGRAM.md (legacy-unversioned)
Escopo: Diagrama lógico do pipeline de decisão do Euru OS. Representa o fluxo
        sequencial de agentes, gates de bloqueio e condições de interrupção.

---

# EURU — Diagrama Lógico do Pipeline

---

## Changelog

v1.0 — 2026-04-11
- Normalizado de PIPELINE_DIAGRAM.md para formato canônico.
- Aplicado cabeçalho conforme EURU_DOCUMENT_POLICY_OFFICIAL_v1.0.
- Numeração dos agentes atualizada para refletir sequência canônica v1.1
  (01–11 conforme Master Documento OFFICIAL v1.1 §6.1).
- Conteúdo estrutural preservado do artefato de origem.

---

## 1. Diagrama do pipeline principal

```
INÍCIO DO CICLO
      │
      ▼
┌─────────────────────────────────┐
│ PRÉ-CONDIÇÃO                    │
│ DevOps Guardião (06)            │
│ INFRA_OK? ──── NÃO ──► HOLD    │
└──────────────┬──────────────────┘
               │ SIM
               ▼
┌─────────────────────────────────┐
│ AGT-01 SCOUT                    │
│ Estrutura de mercado + BTC      │
│ Output: NO_TRADE / WATCHLIST /  │
│         SETUP                   │
└──────────────┬──────────────────┘
               │ SETUP
               ▼
┌─────────────────────────────────┐
│ AGT-02 FLOW ANALYST             │
│ Confirmação técnica             │
│ Output: CONFIRMS /              │
│         CONTRADICTS /           │
│         INCONCLUSIVE            │
└──────────────┬──────────────────┘
               │ CONFIRMS
               ▼
┌─────────────────────────────────┐
│ AGT-03 NEWS SENTINEL            │
│ Contexto informacional          │
│ Output: CLEAR / CAUTION / VETO  │
└──────────────┬──────────────────┘
               │ CLEAR ou CAUTION
               ▼
┌─────────────────────────────────┐
│ AGT-10 MAC / PLAYBOOK ANALYST   │
│ Aderência metodológica          │
│ Output: PLAYBOOK_OK /           │
│         PLAYBOOK_FAIL           │
└──────────────┬──────────────────┘
               │ PLAYBOOK_OK
               ▼
┌─────────────────────────────────┐
│ AGT-04 QUANT / RISK OFFICER     │
│ Dimensionamento e limites       │
│ Output: APPROVE / REJECT        │
└──────────────┬──────────────────┘
               │ APPROVE
               ▼
┌─────────────────────────────────┐
│ AGT-11 QUALITY CONTROL          │
│ Integridade dos dados           │
│ Output: DATA_OK / DATA_WARNING  │
│         / DATA_BLOCKED          │
└──────────────┬──────────────────┘
               │ DATA_OK
               ▼
┌─────────────────────────────────┐
│ AGT-05 EXECUTION ORCHESTRATOR   │
│ Síntese e decisão final         │
│ Output: EXECUTION_ALLOWED /     │
│         NO_TRADE / HOLD         │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ AGT-07 JOURNAL AUDITOR          │
│ Registro obrigatório do ciclo   │
│ (sempre executado, independente │
│  do output anterior)            │
└─────────────────────────────────┘
```

---

## 2. Camada transversal (fora do pipeline sequencial)

```
┌─────────────────────────────────────────────────────┐
│ CAMADA TRANSVERSAL — sempre ativa                   │
│                                                     │
│  AGT-08 SCORE ENGINE                                │
│  Consolida sinais quantitativos em score único      │
│  Alimenta AGT-04 com score para dimensionamento     │
│                                                     │
│  AGT-09 WATCHDOG                                    │
│  Monitora heartbeat e falhas silenciosas            │
│  Pode interromper qualquer ponto do pipeline        │
│                                                     │
│  AGT-06 DEVOPS GUARDIÃO                             │
│  Monitora infraestrutura continuamente              │
│  Gate de entrada + veto a qualquer momento          │
└─────────────────────────────────────────────────────┘
```

---

## 3. Regras de interrupção do pipeline

| Condição | Ponto de interrupção | Output forçado |
|---|---|---|
| Scout retorna NO_TRADE ou WATCHLIST | Após AGT-01 | NO_TRADE |
| Flow retorna CONTRADICTS ou INCONCLUSIVE | Após AGT-02 | NO_TRADE |
| News retorna VETO | Após AGT-03 | NO_TRADE |
| Playbook retorna PLAYBOOK_FAIL | Após AGT-10 | NO_TRADE |
| Risk retorna REJECT | Após AGT-04 | NO_TRADE |
| Quality retorna DATA_BLOCKED | Após AGT-11 | NO_TRADE |
| Watchdog detecta falha silenciosa | Qualquer ponto | PIPELINE_BREAK |
| DevOps reporta SYSTEM_DEGRADED | Qualquer ponto | FORCE_READ_ONLY |

---

## 4. Princípio de design

O pipeline foi desenhado para **favorecer o bloqueio**. O caminho até
`EXECUTION_ALLOWED` requer que todos os gates passem positivamente.
Qualquer saída negativa em qualquer gate resulta em `NO_TRADE` para o ciclo.
