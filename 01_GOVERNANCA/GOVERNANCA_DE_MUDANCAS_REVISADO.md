# Governança de Mudanças — Euru OS (Revisado)
Este documento define como as mudanças são classificadas e aprovadas no Euru OS. Cada tipo de mudança tem exemplos, tempo de espera e responsáveis claramente definidos, promovendo transparência e controlo.
## Tipo 1 – Operacional leve
- **Exemplos:** ajustes de texto em prompts, renomear campos, melhorar a clareza de scorecards.
- **Tempo de espera:** nenhum (pode ser executado imediatamente).
- **Aprovação:** Risk/Product Owner (auto‑aprovação).
- **Registo:** adicione a mudança ao **CHANGELOG.md**.
## Tipo 2 – Estrutural moderado
- **Exemplos:** modificar lógica de agentes, alterar activos da watchlist, adaptar rotinas diárias.
- **Tempo de espera:** 24 horas a partir da proposta.
- **Aprovação:** ambas as funções (Risk/Product Owner e Automation Engineer) devem revisar e aprovar separadamente.
- **Registo:** **CHANGELOG.md** e **DECISOES_ESTRATEGICAS.md**.
## Tipo 3 – Estratégico crítico
- **Exemplos:** transição de fase (READ_ONLY → SIMULATE → EXECUTE), alterações nas regras de risco, remoção de agentes.
- **Tempo de espera:** mínimo de 48 horas.
- **Aprovação:** checklist formal completo com assinatura de ambos os responsáveis.
- **Registo:** **CHANGELOG.md**, **DECISOES_ESTRATEGICAS.md** e um arquivo dedicado que descreva a decisão em detalhes.
## Regra de ouro
Qualquer mudança que afecte **risco**, **modo do sistema** ou **execução** **só ocorre após o preenchimento completo do checklist**. Isso garante que nenhum ajuste crítico seja feito de forma impulsiva.