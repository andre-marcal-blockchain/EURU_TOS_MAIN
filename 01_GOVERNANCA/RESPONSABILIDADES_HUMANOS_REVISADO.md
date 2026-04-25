# Papéis e Responsabilidades — Euru OS (Revisado)
Este documento descreve os papéis humanos que supervisionam o Euru OS e as respectivas obrigações e restrições. A separação de responsabilidades reduz riscos e promove decisões ponderadas.
## Risk/Product Owner
**Responsável:** Andre (no momento).  
**Função:** definir a visão estratégica e as regras de risco.
### Responsabilidades
- Estabelecer missão, visão e objectivos do projecto.
- Definir e actualizar limites de risco e regras de gestão.
- Aprovar transições de fase (READ_ONLY → SIMULATE → EXECUTE).
- Congelar activos, agentes ou estratégias em caso de incidentes ou desvios.
- Aprovar mudanças críticas (tipos 2 e 3) e validar checklists.
- Realizar revisão semanal de governança e assegurar conformidade com leis e regulamentos.
### Restrições
- Não tomar decisões de infraestrutura de forma impulsiva.
- Não aprovar transições de fase na mesma sessão em que são propostas.
- Nunca ignorar o período de espera de 24 horas para alterações críticas.
## Automation Engineer
**Responsável:** Andre (mesma pessoa, contexto distinto).  
**Função:** garantir a operacionalidade técnica e a organização do repositório.
### Responsabilidades
- Organizar a estrutura de pastas e arquivos.
- Gerir chaves de API, segredos e conectividade com a exchange.
- Manter logs, snapshots e backups.
- Assegurar a estabilidade técnica e monitorar saúde da infraestrutura.
- Implementar e reforçar o modo READ_ONLY a nível de infraestrutura.
- Responder prontamente a incidentes técnicos e registar acções de mitigação.
### Restrições
- Nunca habilitar execução sem aprovação do Risk/Product Owner.
- Não armazenar segredos em texto plano; utilizar cofres de segredos.
- Não aceitar como satisfatória uma condição instável ou “works more or less”.
## Operação Solo
Quando a mesma pessoa ocupa ambos os papéis, devem ser seguidas regras adicionais:
- Realizar decisões estratégicas e técnicas em sessões separadas, com intervalo adequado.
- Respeitar o período de espera de 24 h para mudanças críticas, mesmo em operação solo.
- Executar revisão semanal de si próprio, documentando conclusões e acções de melhoria.
- Redigir documentação que possa ser entendida por um auditor externo, assegurando transparência.