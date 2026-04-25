# Regras Mãe — Playbook de Trading (Revisado)
Este documento resume, em linguagem clara, as regras de risco e comportamento que todos os agentes e operadores do Euru OS devem seguir. Ele complementa o YAML `REGRAS_MAE_REVISADO.yaml` e facilita a leitura por humanos.
## Princípios
- **Preservação de capital** é a prioridade absoluta.  
- Em caso de dúvida ou ausência de contexto, adopte o estado `NO_TRADE`.
## Limites de risco
- Máximo de **3 trades por dia** e **2 posições abertas simultâneas**.  
- Risco por operação limitado a **1 %** do capital disponível.  
- Perdas máximas de **2 % ao dia** e **5 % na semana**.  
- É **obrigatório** usar **stop‑loss** em todas as posições.
## Proibições
- **Revenge trade:** não operar para recuperar perdas.  
- **Operar sem stop:** todas as ordens devem ter limite de perda pré‑definido.  
- **Negociar fora do playbook:** apenas setups documentados podem ser executados.
## Condições para não operar
- O operador está cansado ou sem foco.  
- Há uma sequência recente de stops.  
- Emoções fortes estão presentes (vingança ou euforia).  
- O BTC apresenta volatilidade errática ou sem direcção.  
- A watchlist não é clara ou insuficiente.
## Parâmetros de execução
- **Execução ao vivo** e modo **hedge** são proibidos até nova fase.  
- Não realizar entradas de recuperação (martingale) ou aumentar lote para recuperar perdas.  
- Antes de entrar, verificar invalidadores do setup, custos (taxas) e riscos de liquidação.
## Registos e governança
- Manter **diário de trades**, **changelog** e **registo de incidentes** actualizados.  
- Mudanças de fase (por exemplo, habilitar execução real) só ocorrem com aprovação do Risk/Product Owner e após a conclusão do checklist.
## Distribuição de capital
- **50 % Core:** ETH, SOL, BNB, LINK, AVAX, SUI, NEAR.  
- **25 % Crescimento:** ARB, OP, TIA, POL, SEI, ATOM, STX.  
- **15 % Assimétrico:** TAO, RENDER, FET, INJ, PYTH, ONDO.  
- **10 % Especulativo:** DOGE, PEPE, BONK — nunca exceder 10 % do capital.
Estas regras devem ser lidas e compreendidas antes de qualquer sessão de trading. O não cumprimento delas acarreta suspensão de estratégias e revisão do plano.