Documento: EURU_OPERATIONS_RUNBOOK_DocumentalBacklog
Owner: Governança Euru
Status: OFFICIAL
Versão: v1.0
Última atualização: 2026-04-11
Documento pai: EURU_GOVERNANCE_POLICY_LegacyMigration_OFFICIAL_v1.0
Substitui: N/A
Escopo: Runbook fixo para execução de backlog documental do Euru OS.
        Passos determinísticos que qualquer operador ou IA pode seguir
        sem depender de memória humana ou contexto de sessões anteriores.

---

# EURU — Runbook do Operador
## Execução de Backlog Documental

---

## Changelog

v1.0 — 2026-04-11
- Criação do runbook com 4 procedimentos cobertos: normalização de artefato
  legado, promoção de documento a OFFICIAL, migração de pasta de agente,
  e actualização de Registry.
- Baseado na Migration Policy e na experiência de normalização desta sessão.

---

## Como usar este runbook

Cada procedimento abaixo é autossuficiente. Não requer leitura de sessões
anteriores. Antes de executar qualquer procedimento:

1. Abrir o **Document Registry** (versão mais recente).
2. Identificar o item pelo ID (ex: L-01, A11, G-07).
3. Seleccionar o procedimento correspondente abaixo.
4. Executar passo a passo sem pular etapas.
5. Actualizar o Registry ao final.

---

## PROC-01 — Normalizar artefato legado (`NORMALIZE`)

**Quando usar:** item com status `NORMALIZE` no Registry ou na Triage.

```
PASSO 1 — LOCALIZAR
  Abrir: EURU_DOCUMENT_REGISTRY_OFFICIAL_v1.2.md
  Encontrar o item pelo ID.
  Confirmar: nome legado actual e nome canônico proposto.

PASSO 2 — LER O ARTEFATO
  Abrir o ficheiro legado na sua localização original.
  Responder: o conteúdo ainda é válido para o sistema actual?
  → Se NÃO: usar PROC-02 (revisar antes de normalizar).
  → Se SIM: continuar.

PASSO 3 — APLICAR CABEÇALHO
  Copiar o template de:
    EURU_DOCUMENT_TEMPLATE_HEADER_CHANGELOG.md
  Preencher todos os campos:
    - Documento: [nome canônico sem extensão]
    - Owner: Governança Euru
    - Status: OFFICIAL
    - Versão: v1.0
    - Última atualização: [data de hoje]
    - Documento pai: [conforme Registry]
    - Substitui: [nome legado] (legacy-unversioned)
    - Escopo: [uma linha descrevendo o conteúdo]

PASSO 4 — ADICIONAR CHANGELOG
  Imediatamente após o cabeçalho:
    ## Changelog
    v1.0 — [data]
    - Normalizado de [nome legado] para formato canônico.
    - Aplicado cabeçalho conforme EURU_DOCUMENT_POLICY_OFFICIAL_v1.0.
    - Conteúdo preservado integralmente do artefato de origem.

PASSO 5 — SALVAR COM NOME CANÔNICO
  Salvar como: [nome canônico proposto no Registry]
  Localização: pasta correcta conforme estrutura do repositório.

PASSO 6 — ARQUIVAR LEGADO
  Mover ficheiro original para: 99_ARQUIVO_E_NOTAS/
  Não apagar.

PASSO 7 — ACTUALIZAR REGISTRY
  Abrir Registry versão actual.
  Linha do item: actualizar status de legacy-unversioned para OFFICIAL.
  Actualizar localização se mudou.
  Incrementar versão do Registry (+0.1).
  Adicionar entrada no changelog do Registry.
```

---

## PROC-02 — Revisar e normalizar artefato (`REVIEW_THEN_NORMALIZE`)

**Quando usar:** item com status `REVIEW_THEN_NORMALIZE` no Registry ou na Triage.

```
PASSO 1 — LOCALIZAR
  Igual ao PROC-01 Passo 1.

PASSO 2 — LER E REVISAR
  Abrir o ficheiro legado.
  Verificar:
    □ Conteúdo alinhado com documentos de autoridade superior?
    □ Formato compatível com o sistema actual? (.txt → .md se necessário)
    □ Campos ou secções em falta vs. documentos equivalentes normalizados?

  Para conflito com documento superior:
    → PARAR. Registar o conflito. Não normalizar até decisão do proprietário.

  Para conversão de formato (.txt/.docx → .md):
    → Converter conteúdo sem alterar sentido. Registar no changelog.

  Para conteúdo incompleto:
    → Expandir apenas com base em documentos OFFICIAL existentes.
    → Qualquer adição deve ser marcada no changelog como "expandido".

PASSO 3 A 7 — Igual ao PROC-01 Passos 3 a 7.
  No changelog, adicionar:
    - Conteúdo revisado: [descrever o que foi verificado/ajustado].
```

---

## PROC-03 — Migrar pasta de agente

**Quando usar:** item com status `MIGRATION_READY` ou `SPLIT_RESOLVED` no Registry.

```
PASSO 1 — LOCALIZAR MANIFESTO
  Abrir o manifesto do agente em: PKG-NORM/T03/ ou PKG-BL/
  Confirmar: pasta de destino canônica e pastas de origem.

PASSO 2 — CRIAR PASTA CANÔNICA
  mkdir 04_AGENTES/[NN]_[NOME_CANONICO]/

PASSO 3 — CONSOLIDAR ARTEFATOS
  Para cada artefato (BRIEFING, OUTPUT_FORMAT, PROMPT):
    - Se as pastas de origem têm versões idênticas: copiar uma.
    - Se divergentes: usar a versão mais recente como base.
      Registar diferenças no changelog do documento resultante.

PASSO 4 — APLICAR CABEÇALHOS
  Aplicar PROC-01 Passos 3 e 4 a cada artefato consolidado.

PASSO 5 — ARQUIVAR PASTAS LEGADAS
  Para cada pasta de origem:
    mv 04_AGENTES/[pasta_legada]/ 99_ARQUIVO_E_NOTAS/[pasta_legada]_SUPERSEDED/
  Criar README em cada pasta arquivada:
    "SUPERSEDED by [pasta canônica] — [ADR relevante] — [data]"

PASSO 6 — ACTUALIZAR REFERÊNCIAS
  Verificar documentos listados no manifesto como "referências a actualizar".
  Substituir caminhos legados pelo caminho canônico novo.

PASSO 7 — ACTUALIZAR REGISTRY
  Entrada do agente: status → OFFICIAL ✅
  Localização: caminho canônico novo.
  Incrementar versão do Registry. Changelog.
```

---

## PROC-04 — Actualizar o Document Registry

**Quando usar:** após qualquer PROC-01, 02 ou 03, ou após qualquer mudança
documental relevante.

```
PASSO 1 — ABRIR VERSÃO ACTUAL DO REGISTRY
  Confirmar número de versão actual.

PASSO 2 — LOCALIZAR A LINHA DO ITEM
  Encontrar pelo ID (G-xx, L-xx, ou número do agente).

PASSO 3 — ACTUALIZAR CAMPOS
  - Documento canônico: nome canônico final
  - Status / Versão: OFFICIAL vX.Y
  - Localização: caminho actualizado

PASSO 4 — ADICIONAR AO CHANGELOG DO REGISTRY
  Formato:
    vX.Y — [data]
    - [ID]: [o que mudou] (ex: "L-01: normalizado para OFFICIAL v1.1")

PASSO 5 — INCREMENTAR VERSÃO DO REGISTRY
  Minor bump: v1.2 → v1.3 para normalizações individuais.
  Major bump: v1.x → v2.0 apenas se estrutura do Registry mudar.

PASSO 6 — SALVAR COM NOVO NÚMERO DE VERSÃO NO NOME
  Ex: EURU_DOCUMENT_REGISTRY_OFFICIAL_v1.3.md
  Mover versão anterior para 99_ARQUIVO_E_NOTAS/ com status SUPERSEDED.
```

---

## PROC-05 — Verificação de consistência pré-ciclo

**Quando usar:** antes de iniciar qualquer sessão operacional.
**Tempo estimado:** 5 minutos.

```
□ 1. Abrir Registry versão mais recente — confirmar que é a mais recente.
□ 2. Confirmar estado canônico: READ_ONLY (até ADR posterior que mude isso).
□ 3. Verificar se há itens MIGRATION_READY ou REVIEW_THEN_NORMALIZE
     pendentes que possam impactar o ciclo.
□ 4. Confirmar que DevOps Guardião e Quality Control têm prompts OFFICIAL.
□ 5. Confirmar que Journal Auditor está pronto para registrar o ciclo.
□ 6. Se tudo ok: iniciar ciclo com Prompt DailyOperation.
□ 7. Se há pendências bloqueantes: resolver antes de iniciar ciclo.
```

---

## PROC-06 — Backlog opcional (sem urgência operacional)

**Quando usar:** quando houver tempo disponível fora de ciclos operacionais.
**Itens actuais:**

| Item | Tipo | PROC a usar |
|---|---|---|
| AGT-01 a AGT-05, AGT-08, AGT-10: renomear prompts `_REVISADO` | Rename + cabeçalho | PROC-01 |
| AGT-09 Watchdog: converter prompt de `.txt` para `.md` | Conversão + cabeçalho | PROC-02 |

**Regra:** estes itens não bloqueiam operação. Executar apenas quando não
houver ciclo operacional activo ou revisão semanal pendente.

---

## Referências rápidas

| Documento | Função | Localização no Registry |
|---|---|---|
| Document Registry | índice de tudo | G-13 |
| Document Policy | regras de nomenclatura | G-02 |
| Template Header | cabeçalho padrão | G-03 |
| Migration Policy | regras de normalização | G-11 |
| Legacy Triage | nomes canônicos propostos | G-12 |
| State Doc | confirmar READ_ONLY | G-05 |
