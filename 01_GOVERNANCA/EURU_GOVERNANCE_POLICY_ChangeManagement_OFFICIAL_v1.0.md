Documento: EURU_GOVERNANCE_POLICY_ChangeManagement
Owner: Governança Euru
Status: OFFICIAL
Versão: v1.0
Última atualização: 2026-04-11
Documento pai: EURU_MASTER_DOCUMENTO_OFFICIAL_v1.1
Substitui: GOVERNANCA_DE_MUDANCAS_REVISADO.md (legacy-unversioned)
Escopo: Política formal de gestão de mudanças do Euru OS. Define o que constitui
        uma mudança crítica, quem pode aprovar, e como registar de forma rastreável.

---

# EURU — Política de Gestão de Mudanças

---

## Changelog

v1.0 — 2026-04-11
- Normalizado de GOVERNANCA_DE_MUDANCAS_REVISADO.md para formato canônico.
- Aplicado cabeçalho conforme EURU_DOCUMENT_POLICY_OFFICIAL_v1.0.
- Conteúdo preservado integralmente do artefato de origem.

---

## 1. O que constitui uma mudança crítica

Uma mudança é crítica quando afeta qualquer um dos seguintes elementos:

- modo operacional do sistema (`READ_ONLY`, `SIMULATE`, `EXECUTE`);
- regras de risco (limites, stops, tamanho de posição);
- numeração, papel ou prompt de qualquer agente;
- estrutura de pastas canônicas do repositório;
- hierarquia documental ou política de versionamento;
- integração com exchange (chaves, permissões, endpoints).

Mudanças não críticas (correções tipográficas, formatação, clareza de texto)
podem ser aplicadas com registro `[minor fix]` no changelog, sem aprovação formal.

---

## 2. Fluxo obrigatório para mudanças críticas

```
1. IDENTIFICAR — descrever a mudança e classificá-la como crítica
2. RASCUNHAR   — criar versão DRAFT do documento afetado
3. REVISAR     — verificar conflito com documentos de autoridade superior
4. APROVAR     — decisão do proprietário (Andrezão / Governança Euru)
5. PROMOVER    — atualizar status para OFFICIAL, bump de versão
6. REGISTRAR   — changelog + atualização do Document Registry
7. COMUNICAR   — handoff para IAs e operadores via prompt atualizado
```

Nenhuma etapa pode ser pulada em mudanças críticas.

---

## 3. Documentos que requerem atualização em cascata

| Mudança | Documentos que devem ser atualizados |
|---|---|
| Novo agente ou renumeração | Master Documento + Registry + Triage |
| Mudança de modo operacional | State Doc + ADR + Master Documento + Registry |
| Nova regra de risco | Regras-Mãe + Risk Matrix |
| Nova pasta canônica | ADR + Registry + Migration Policy |
| Nova convenção de nomes | Document Policy + Template + Registry |

---

## 4. Registro de mudanças

Toda mudança crítica deve gerar pelo menos uma das seguintes entradas:

- **Changelog** no documento alterado;
- **ADR** quando a decisão for arquitetural ou irreversível;
- **Entrada em DECISOES_ESTRATEGICAS** quando afetar direção do sistema.

---

## 5. Critério de reversão

Se uma mudança crítica gerar consequências não previstas:

1. O documento alterado retorna ao status `REVIEW`.
2. A versão anterior é reativada como canônica.
3. Um registro de reversão é adicionado ao changelog.
4. Uma ADR documenta a razão da reversão.
