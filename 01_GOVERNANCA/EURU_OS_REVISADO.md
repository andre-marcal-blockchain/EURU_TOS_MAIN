# Visão Geral do Euru OS (Revisado)
## Missão e Objectivos
O Euru OS visa construir um sistema de negociação de criptomoedas que **observa**, **simula** e eventualmente **executa** operações com disciplina e gestão rigorosa de risco. O objectivo principal é preservar o capital e aprender com dados, evoluindo progressivamente até a execução real.
## Princípios Negociáveis
- **Preservação de capital acima de lucro.**
- **Cálculo do risco antes de cada trade.**
- **Registo completo de operações e decisões.**
- **Nenhuma decisão relevante sem contexto claro.**
## Modos do Sistema
- **READ\_ONLY:** fase actual; observa o mercado, regista dados e responde a incidentes.  
- **SIMULATE:** testa estratégias sem dinheiro real, registando resultados para avaliação.  
- **EXECUTE:** envia ordens reais com base em decisões validadas; requer aprovação formal e demonstração de robustez.
## Agentes e Papéis
- **Scout:** avalia o contexto de mercado (tendências, médias móveis, filtro BTC).
- **Flow Analyst:** aplica indicadores técnicos (RSI, MACD, OBV, ATR) para confirmar ou invalidar setups.
- **News Sentinel:** filtra notícias e eventos relevantes, classificando a severidade.
- **Quant/Risk Officer:** calcula tamanho de posição e verifica regras de risco (por exemplo, posição = capital × 1 % / (ATR × 1,5)).
- **Execution Orchestrator:** combina outputs dos agentes e decide o estado final (APPROVE, REJECT, REVIEW).
- **DevOps Guardião:** mantém a integridade da infra‑estrutura, logs e monitoramento.
- **Journal Auditor:** garante que registos, diários e auditorias estejam em ordem e detecta desvios.
## Estrutura de Pastas
O repositório do Euru OS é organizado por módulos:
1. **01_GOVERNANCA:** documentos de constituição, regras mãe, governaça de mudanças e papéis.  
2. **02_BINANCE_SETUP:** guias de configuração da conta, KYC, segurança, API e conectividade.  
3. **03_ARQUITETURA:** arquitectura geral, fluxos de dados, modos do sistema e diagramas de agentes.  
4. **04_AGENTES:** pastas dedicadas para cada agente com briefing, prompts e esquemas de output.  
5. **05_PROMPTS:** templates de prompts para operações diárias, pré‑trade, pós‑trade e revisões.  
6. **06_RISCO_E_EXECUCAO:** matriz de risco, dimensionamento de posição, limites de perda, política de hedge e checklists.  
7. **07_OPERACAO:** SOP diário, SOP semanal, playbook de incidentes e modos do sistema.  
8. **08_DADOS_E_JOURNAL:** diários de trade, scorecards, watchlists e snapshots.  
9. **09_LOGS_E_INCIDENTES:** registo de incidentes, changelog, post‑mortems e alertas.  
10. **10_TEMPLATES:** modelos para documentos e reuniões.  
11. **99_PRIVATE_NOTES:** notas internas, ideias e backlog.
Esta estrutura ajuda a localizar rapidamente a documentação e a separar áreas de responsabilidade.
## Primeiros Passos
1. Criar conta demo na exchange e concluir KYC/2FA.  
2. Configurar as chaves API (somente leitura) e guardá‑las em local seguro.  
3. Configurar watchlist inicial (BTC, ETH) e preparar o *morning scan*.  
4. Executar o *morning scan* manual seguindo o checklist diário revisado.  
5. Documentar todas as acções no diário de trading e checklist apropriado.  
6. Revisar semanalmente o progresso, ajustando rotinas e identificando áreas de melhoria.
## Regras de Ouro
- **Sem capital real até aprovação explícita.**  
- **Qualquer hedge ou estratégia avançada requer aprovação formal.**  
- **Em caso de incidentes ou degradação, retornar imediatamente ao modo READ\_ONLY.**
## Critérios de Sucesso e Próximas Etapas
- Checklist diário executável em 30 minutos, sem necessidade de consulta externa.  
- Actualizar o *morning scan* para incluir alt‑coins conforme o plano estratégico.  
- Implementar os indicadores do Flow Analyst e validar a fórmula de dimensionamento de posição.  
- Integrar o News Sentinel e quantificar o impacto das notícias sobre decisões de trading.  
- Criar e testar o módulo de execução em modo SIMULATE, garantindo que as decisões estejam alinhadas com o playbook.  
- Após pelo menos 3 meses de simulação consistente e rentável, considerar a transição gradual para o modo EXECUTE, com aprovação formal.