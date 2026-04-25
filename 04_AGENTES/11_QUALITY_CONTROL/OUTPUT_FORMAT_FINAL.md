Documento: EURU_AGENTS_QUALITY_CONTROL_OUTPUT_FORMAT
Owner: Governança Euru
Status: OFFICIAL
Versão: v1.0
Última atualização: 2026-04-11
Documento pai: EURU_AGENTS_QUALITY_CONTROL_BRIEFING
Substitui: OUTPUT_FORMAT_FINAL.md de 09_QUALITY_CONTROL e 10_QUALITY_CONTROL (legacy-unversioned)
Escopo: Formato de saída obrigatório do agente 11 — Quality Control.
        Define estrutura exacta dos outputs DATA_OK, DATA_WARNING e DATA_BLOCKED.

---

# EURU — AGT-11 Quality Control
## Output Format Canônico

---

## Changelog

v1.0 — 2026-04-11
- Consolidado a partir das pastas 09_QUALITY_CONTROL e 10_QUALITY_CONTROL.
- Aplicado cabeçalho canônico conforme Migration Policy.
- Formato padronizado e alinhado com StatusDefinitions v1.0.

---

## Output: DATA_OK

```
=== QUALITY CONTROL — VALIDAÇÃO DE DADOS ===
Data/hora: [AAAA-MM-DD HH:MM UTC]
Ciclo: [morning | asian | manual]
Ativo analisado: [símbolo]
Fonte de dados: [exchange | script | manual]

RESULTADO: DATA_OK

Campos validados:
  ✅ Timestamp: [valor] — dentro da janela de 15 min
  ✅ Preço: [valor] — dentro de faixa plausível
  ✅ Volume: [valor] — presente e coerente
  ✅ Indicadores: [lista] — todos presentes
  ✅ Consistência com ciclo anterior: OK

Campos com problema: nenhum

Ação: pipeline pode prosseguir para Execution Orchestrator
===
```

---

## Output: DATA_WARNING

```
=== QUALITY CONTROL — VALIDAÇÃO DE DADOS ===
Data/hora: [AAAA-MM-DD HH:MM UTC]
Ciclo: [morning | asian | manual]
Ativo analisado: [símbolo]
Fonte de dados: [exchange | script | manual]

RESULTADO: DATA_WARNING

Campos validados: [lista dos campos ok]

Campo com problema:
  ⚠️ [nome do campo]: [descrição do problema]
  Severidade: [BAIXA | MÉDIA]
  Impacto estimado: [descrição]

Ação: encaminhar para Execution Orchestrator com warning
Recomendação: reduzir tamanho de posição ou aguardar confirmação adicional
===
```

---

## Output: DATA_BLOCKED

```
=== QUALITY CONTROL — VALIDAÇÃO DE DADOS ===
Data/hora: [AAAA-MM-DD HH:MM UTC]
Ciclo: [morning | asian | manual]
Ativo analisado: [símbolo]
Fonte de dados: [exchange | script | manual]

RESULTADO: DATA_BLOCKED

Campo bloqueado:
  ❌ [nome do campo]: [descrição do problema]
  Tipo de falha: [ausente | corrompido | fora de faixa | desatualizado | duplicado]
  Origem provável: [exchange | script | coleta manual | desconhecida]

Ação: NO_TRADE obrigatório para este ciclo
Próximo passo: investigar fonte antes do próximo ciclo
Registrar: incidente INC-[AAAA-MM-DD]-[NNN] em EURU_LOGS_REGISTRY_IncidentLog
===
```

---

## Regras de formato

1. O bloco `=== QUALITY CONTROL ===` é sempre emitido, mesmo que seja DATA_OK.
2. Campos validados são sempre listados explicitamente — nunca apenas "todos ok".
3. Em DATA_BLOCKED, o campo "Origem provável" é obrigatório, mesmo que seja "desconhecida".
4. O timestamp é sempre em UTC.
