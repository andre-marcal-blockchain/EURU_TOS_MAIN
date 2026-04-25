# Padrão Unificado de Status — Euru OS (Revisado)
Este padrão define um vocabulário comum para estados do sistema, fluxo, risco, execução, infraestrutura, notícias e modos. A utilização consistente desses termos ajuda a comunicação entre agentes e humanos.
## Estados estruturais
- **NO_TRADE** – nenhum setup observável.
- **WATCHLIST** – activo em observação.
- **SETUP** – configuração com potencial de trade.
## Estados de fluxo
- **CONFIRMS** – o fluxo confirma a hipótese.
- **CONTRADICTS** – o fluxo contradiz a hipótese.
- **INCONCLUSIVE** – sinal inconclusivo.
## Estados de risco
- **APPROVE** – parâmetros de risco aceitáveis.
- **REJECT** – parâmetros inaceitáveis.
- **REVIEW** – dados insuficientes, requer revisão.
## Estados de execução
- **EXECUTION_ALLOWED** – envio de ordens permitido.
- **EXECUTION_BLOCKED** – ordens bloqueadas.
- **MANUAL_REVIEW_REQUIRED** – revisão humana necessária.
## Estados de infraestrutura
- **HEALTHY** – sistema operacional.
- **DEGRADED** – perda parcial de funcionalidade.
- **CRITICAL** – deve entrar em modo READ_ONLY.
## Severidade de notícias
Utilizar uma escala simples: **LOW**, **MEDIUM**, **HIGH** ou **CRITICAL** para classificar o impacto de eventos externos.
## Modos do sistema
- **READ_ONLY** – observar, registar e aprender; sem ordens reais.
- **SIMULATE** – simular decisões sem capital real.
- **EXECUTE** – enviar ordens reais (somente em fase futura com aprovação formal).
## Hierarquia de resolução de conflitos
1. DevOps Guardião  
2. Execution Orchestrator  
3. Quant/Risk Officer  
4. News Sentinel  
5. Flow Analyst  
6. Scout  
Seguir esta ordem garante que incidentes são tratados pela pessoa ou agente com maior responsabilidade e contexto técnico.