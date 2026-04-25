Documento: EURU_OPERATIONS_PROMPT_PostTrade
Owner: Governança Euru
Status: OFFICIAL
Versão: v1.0
Última atualização: 2026-04-11
Documento pai: EURU_MASTER_DOCUMENTO_OFFICIAL_v1.1
Substitui: PROMPT_POST_TRADE.md (legacy-unversioned)
Escopo: Prompt de revisão e registro imediatamente após o encerramento de
        qualquer operação real ou paper trade.

---

# EURU — Prompt Pós-Trade

---

## Changelog

v1.0 — 2026-04-11
- Normalizado de PROMPT_POST_TRADE.md para formato canônico.
- Aplicado cabeçalho conforme EURU_DOCUMENT_POLICY_OFFICIAL_v1.0.
- Conteúdo preservado integralmente do artefato de origem.

---

## Instrução de uso

Executar este prompt **imediatamente após** o encerramento de cada operação.
Não encerrar a sessão sem completar o registro.

---

## Prompt

```
Você está no ciclo de revisão pós-trade do Euru OS.

Preencha cada seção abaixo para a operação encerrada.

DADOS DA OPERAÇÃO
- Ativo: [símbolo]
- Direção: [LONG | SHORT]
- Entrada: [preço]
- Stop original: [preço]
- Alvo original: [preço]
- Saída efetiva: [preço]
- Motivo de saída: [stop / alvo / saída manual / expiração]
- Resultado: [% ganho ou perda]
- Score de decisão na entrada: [valor]

ANÁLISE DE EXECUÇÃO

1. O setup foi executado conforme o plano?
   [ ] Sim — sem desvios
   [ ] Não — descrever desvio: [...]

2. O stop foi respeitado?
   [ ] Sim
   [ ] Não — descrever o que aconteceu: [...]

3. O gerenciamento durante a operação foi correto?
   [ ] Sim
   [ ] Não — o que poderia ter sido diferente: [...]

ANÁLISE DE RESULTADO

4. O resultado foi consistente com o que o setup oferecia?
   [ ] Sim
   [ ] Não — por quê: [...]

5. Houve algum sinal que deveria ter impedido a entrada?
   [ ] Não
   [ ] Sim — o que foi ignorado: [...]

APRENDIZADO

6. O que este trade ensina ao sistema?
   [texto livre — uma linha mínima obrigatória]

AÇÃO DO JOURNAL AUDITOR
- Gerar entrada PT-[AAAA-MM-DD]-[NNN] com todos os dados acima.
- Atualizar watchlist se o ativo mostrou comportamento relevante.
- Registrar aprendizado em nota de sessão.
```
