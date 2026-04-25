Documento: EURU_LOGS_REGISTRY_IncidentLog
Owner: Governança Euru
Status: OFFICIAL
Versão: v1.0
Última atualização: 2026-04-11
Documento pai: EURU_MASTER_DOCUMENTO_OFFICIAL_v1.1
Substitui: INCIDENTES.md (legacy-unversioned)
Escopo: Registro oficial de incidentes do Euru OS. Documento vivo — cada
        incidente novo adiciona uma entrada; nunca substitui entradas anteriores.

---

# EURU — Log de Incidentes

---

## Changelog

v1.0 — 2026-04-11
- Normalizado de INCIDENTES.md para formato canônico.
- Aplicado cabeçalho conforme EURU_DOCUMENT_POLICY_OFFICIAL_v1.0.
- Estrutura de entrada padronizada conforme AGT-07 Journal Auditor.
- Entradas históricas preservadas integralmente do artefato de origem.
- Nota: este é um documento vivo. Versão reflete a normalização, não o conteúdo.

---

## Regras de uso

1. Nenhuma entrada pode ser apagada ou editada retroativamente sem registro
   da correção.
2. Toda entrada deve ter ID único no formato `INC-AAAA-MM-DD-NNN`.
3. Toda entrada deve ter severidade, tipo, agente reportador e resolução.
4. Entradas geradas pelo Journal Auditor são inseridas no topo (mais recente primeiro).
5. Entradas retroativas devem ser marcadas `[RETROATIVO — inserido em AAAA-MM-DD]`.

---

## Formato padrão de entrada

```
=== INC-AAAA-MM-DD-NNN ===
Tipo: [INFRA | DADOS | GOVERNANÇA | SEGURANÇA | OPERACIONAL]
Severidade: [LOW | MEDIUM | HIGH | CRITICAL]
Agente reportador: [nome]
Data/hora: [AAAA-MM-DD HH:MM UTC]
Descrição: [texto]
Impacto no pipeline: [descrição]
Ação tomada: [descrição]
Resolução: [RESOLVIDO | PENDENTE | MONITORANDO]
Data resolução: [AAAA-MM-DD ou PENDENTE]
===
```

---

## Registro de incidentes

*(entradas históricas do snapshot preservadas abaixo — inserir novas entradas acima desta linha)*

---
