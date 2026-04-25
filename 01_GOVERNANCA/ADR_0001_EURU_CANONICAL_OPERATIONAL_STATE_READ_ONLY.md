# ADR_0001_EURU_CANONICAL_OPERATIONAL_STATE_READ_ONLY

**Status:** Accepted  
**Data:** 2026-04-11  
**Decisor:** Governança documental Euru  
**Relacionado a:** EURU_GOVERNANCE_OPERATIONAL_STATE_OFFICIAL_v1.0

## Contexto

Foram encontradas referências conflitantes aos estados operacionais `READ_ONLY` e `SIMULATE` em diferentes partes da documentação do Euru OS.

## Decisão

O estado operacional canônico atual do Euru OS é `READ_ONLY`.

## Justificativa

- É o modo mais conservador.
- Não existe evidência documental formal suficiente para promover `SIMULATE` a estado oficial.
- Menções dispersas não substituem decisão formal versionada.

## Consequências

- Outra IA deve tratar `READ_ONLY` como verdade operacional vigente.
- `SIMULATE` deve ser tratado como proposta, experimento ou referência não canônica.
- O repositório pode ser normalizado sem paralisar o avanço.

## Critério para revisão futura

Esta ADR só pode ser substituída por nova ADR ou política oficial com:
- status OFFICIAL
- nova versão
- data
- changelog
- declaração explícita de substituição
