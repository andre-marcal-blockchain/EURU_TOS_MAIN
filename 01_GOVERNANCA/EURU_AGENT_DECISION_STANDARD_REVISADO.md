# Padrão de Decisão do Euru — Agentes (Revisado)
Para garantir que as respostas dos agentes sejam claras, consistentes e úteis, use o modelo a seguir em todas as saídas.
## Passos a seguir
1. **O que foi observado:** descreva brevemente o contexto, sinal ou evento detectado.
2. **Confiança na leitura:** informe a fiabilidade da leitura usando a escala padronizada.
3. **Recomendação:** indique a acção sugerida (por exemplo, `NO_TRADE`, `WATCHLIST`, `SETUP`, `SIMULATE`, `APPROVE`, `REJECT` ou `EXECUTION_BLOCKED`).
4. **Justificativa:** explique de forma concisa por que essa recomendação é apropriada, citando indicadores ou regras relevantes.
## Escala de Confiança
- **0–3 (baixa):** a informação é pouco fiável ou contraditória.
- **4–6 (média):** moderada fiabilidade; requer confirmação adicional.
- **7–8 (alta):** sinais claros e consistentes.
- **9–10 (muito alta):** forte convicção, suportada por múltiplos indicadores.
## Estados Operacionais
As recomendações devem referir‑se a um destes estados:
- `NO_TRADE` — não há setup válido.
- `WATCHLIST` — observar activo com atenção.
- `SETUP` — identificar um potencial trade.
- `SIMULATE` — executar em modo de simulação.
- `APPROVE` — os parâmetros de risco são aceitáveis.
- `REJECT` — os parâmetros de risco são inaceitáveis.
- `EXECUTION_BLOCKED` — a execução está bloqueada até nova fase.
## Linguagem e Estilo
Mantenha a comunicação **curta**, **objectiva** e **neutra**:
- Utilize frases curtas e vocabulário simples.
- Evite promoções, garantias ou linguagem emocional.
- Não faça promessas de resultado; foque nas evidências.