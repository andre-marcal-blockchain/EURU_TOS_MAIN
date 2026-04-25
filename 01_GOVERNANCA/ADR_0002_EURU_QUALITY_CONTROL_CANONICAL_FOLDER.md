Documento: ADR_0002_EURU_QUALITY_CONTROL_CANONICAL_FOLDER
Owner: Governança Euru
Status: OFFICIAL
Versão: v1.0
Última atualização: 2026-04-11
Documento pai: EURU_MASTER_DOCUMENTO_OFFICIAL_v1.1
Substitui: N/A
Escopo: Definir a pasta física canônica do agente Quality Control e resolver o split-source documentado no Registry v1.0.

---

# ADR_0002 — Pasta Canônica do Agente Quality Control

## Contexto

O Document Registry v1.0 registrou que o agente 11 (Quality Control) possui
split-source: seus artefatos estão distribuídos entre duas pastas do snapshot:

- `SNAP/04_AGENTES/09_QUALITY_CONTROL`
- `SNAP/04_AGENTES/10_QUALITY_CONTROL`

Essa duplicidade resulta de inconsistência de numeração no repositório original,
documentada no Master Documento v1.1 §6.2.

## Decisão

A pasta canônica oficial do agente Quality Control é:

```
04_AGENTES/11_QUALITY_CONTROL/
```

## Justificativa

1. A numeração canônica 01–11 foi formalizada no Master Documento v1.1 §6.1.
2. Quality Control ocupa a posição 11 nessa sequência — portanto a pasta deve
   refletir esse número.
3. O prefixo `11_` elimina qualquer ambiguidade com as pastas legadas `09_` e `10_`.

## Regra de migração física

Quando o repositório for normalizado:

1. Criar pasta `04_AGENTES/11_QUALITY_CONTROL/`.
2. Consolidar o conteúdo canônico de `09_QUALITY_CONTROL` e `10_QUALITY_CONTROL`
   nessa pasta, mantendo os três artefatos oficiais:
   - `BRIEFING_FINAL.md`
   - `OUTPUT_FORMAT_FINAL.md`
   - `PROMPT.md` → renomear para `PROMPT_FINAL.md` após revisão de conteúdo.
3. Mover as pastas originais `09_` e `10_` para `99_ARQUIVO_E_NOTAS/` com
   nota: `SUPERSEDED by 11_QUALITY_CONTROL — ADR_0002`.
4. Atualizar o Registry: entrada A11 passa de `SPLIT-SOURCE` para `OFFICIAL`.

## Impacto sobre o Registry

- Entrada A11 deve ser atualizada para refletir:
  - Localização: `SNAP/04_AGENTES/11_QUALITY_CONTROL/`
  - Status: `REVIEW-NAME / CANONICAL-CONTENT` → `OFFICIAL` após migração física

## Critério para revisão futura

Esta ADR só pode ser substituída por nova ADR com status OFFICIAL, versão,
data, changelog e declaração explícita de substituição.

---

## Changelog

v1.0 — 2026-04-11
- Definida pasta canônica 11_QUALITY_CONTROL.
- Documentada regra de migração física das pastas legadas.
- Registrado impacto sobre o Document Registry.
