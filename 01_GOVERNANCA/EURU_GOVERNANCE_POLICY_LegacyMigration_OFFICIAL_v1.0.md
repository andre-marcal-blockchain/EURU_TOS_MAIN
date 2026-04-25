Documento: EURU_GOVERNANCE_POLICY_LegacyMigration
Owner: Governança Euru
Status: OFFICIAL
Versão: v1.0
Última atualização: 2026-04-11
Documento pai: EURU_DOCUMENT_POLICY_OFFICIAL_v1.0
Substitui: N/A
Escopo: Regra única para qualquer IA ou humano transformar artefatos legados em
        documentos canônicos do Euru, sem abrir novas decisões de governança.

---

# EURU — Migration Policy for Legacy Artifacts
## Política de Migração de Artefatos Legados v1.0

---

## Changelog

v1.0 — 2026-04-11
- Criação da política com 5 passos obrigatórios e 4 regras de contenção.
- Baseada na triagem EURU_GOVERNANCE_LEGACY_TRIAGE_OFFICIAL_v1.0.
- Compatível com EURU_DOCUMENT_POLICY_OFFICIAL_v1.0.

---

## 1. Quando aplicar esta política

Aplique esta política sempre que encontrar um artefato com qualquer uma das
condições abaixo:

- status `legacy-unversioned` no Registry;
- nome com sufixo `_REVISADO`, `_FINAL`, `_v2` sem padrão canônico;
- extensão `.txt` ou `.docx` em conteúdo que deveria ser `.md`;
- ausência de cabeçalho com Owner, Status, Versão e Documento pai;
- localização fora das pastas canônicas definidas no Registry.

---

## 2. Os 5 passos obrigatórios

### Passo 1 — Verificar o conteúdo antes de qualquer ação
Ler o artefato completo. Responder:
- O conteúdo ainda é válido para o sistema atual?
- Há conflito com algum documento de autoridade superior?

Se houver conflito com nível superior da hierarquia: **parar, registrar o conflito,
não migrar até resolução humana**.

Se não houver conflito: **prosseguir**.

### Passo 2 — Definir o nome canônico
Aplicar o padrão da Document Policy:

```
EURU_[AREA]_[SUBAREA]_[Nome]_[STATUS]_vX.Y.md
```

Usar a tabela de triagem (`EURU_GOVERNANCE_LEGACY_TRIAGE_OFFICIAL_v1.0`) como
referência de nomes já aprovados. Se o artefato não estiver na triagem, definir
o nome e registrá-lo como proposta antes de aplicar.

### Passo 3 — Aplicar o cabeçalho de metadados
Usar o template exato de `EURU_DOCUMENT_TEMPLATE_HEADER_CHANGELOG.md`:

```
Documento: [nome canônico sem extensão]
Owner: Governança Euru
Status: OFFICIAL
Versão: v1.0
Última atualização: [AAAA-MM-DD]
Documento pai: [documento de autoridade superior]
Substitui: [nome do arquivo legado] (legacy-unversioned)
Escopo: [uma linha descrevendo o que o documento cobre]
```

### Passo 4 — Adicionar o bloco de Changelog
Imediatamente após o cabeçalho:

```
## Changelog

v1.0 — [AAAA-MM-DD]
- Migrado de [nome legado] para formato canônico.
- Aplicado cabeçalho conforme EURU_DOCUMENT_POLICY_OFFICIAL_v1.0.
- Conteúdo preservado integralmente / [ou: ajustado em: descrição].
```

### Passo 5 — Atualizar o Registry
Após a migração, o Document Registry deve ser atualizado no mesmo ciclo:

- substituir o nome legado pelo nome canônico;
- atualizar status de `legacy-unversioned` para `OFFICIAL`;
- registrar a versão e a data;
- incrementar a versão do Registry (ex: v1.0 → v1.1).

---

## 3. Regras de contenção — o que nunca fazer

| Proibição | Razão |
|---|---|
| Alterar conteúdo durante a migração sem registrar | Torna a migração uma decisão disfarçada |
| Migrar sem atualizar o Registry | Quebra a rastreabilidade |
| Criar novo nome canônico sem consultar a triagem | Gera nomes divergentes |
| Promover a OFFICIAL sem cabeçalho completo | Viola a Document Policy |

---

## 4. Casos especiais

### Artefato em `.txt`
Converter para `.md`. O conteúdo é preservado integralmente. A conversão de
formato não é alteração de conteúdo — não requer decisão de governança.

### Artefato em `.docx`
Extrair o conteúdo para `.md` via conversão. O `.docx` original é movido para
`99_ARQUIVO_E_NOTAS/` com nota `SUPERSEDED by [nome canônico]`.

### Artefato com conteúdo desatualizado
Não migrar diretamente para OFFICIAL. Migrar para `REVIEW` com nota no changelog:
`Conteúdo requer revisão antes de promoção a OFFICIAL — [motivo]`.

### Artefato duplicado
Consolidar em um único arquivo antes de migrar. Registrar a consolidação no
changelog. Mover duplicatas para `99_ARQUIVO_E_NOTAS/`.

---

## 5. Verificação final antes de concluir

Antes de declarar a migração completa, confirmar:

- [ ] Nome do arquivo segue o padrão canônico
- [ ] Cabeçalho completo com todos os campos obrigatórios
- [ ] Changelog presente e descritivo
- [ ] Conteúdo preservado ou alteração documentada
- [ ] Registry atualizado
- [ ] Arquivo legado movido para arquivo ou marcado como SUPERSEDED
