# Sistema Automatizado de Correção de Redações com IA

Este projeto visa desenvolver um sistema distribuído inovador para a correção automatizada de redações, utilizando múltiplos agentes de Inteligência Artificial. O foco principal é a avaliação das competências exigidas pelo Exame Nacional do Ensino Médio (ENEM), fornecendo feedback personalizado e recomendações de conteúdo para aprimoramento da escrita dos usuários. A arquitetura distribuída garante escalabilidade, robustez e a aplicação de conceitos avançados de segurança e comunicação entre os componentes.




## Objetivos Principais

- Desenvolver um sistema distribuído utilizando múltiplos agentes de Inteligência Artificial.
- Implementar comunicação distribuída eficiente e segura entre os agentes.
- Aplicar conceitos avançados de segurança e arquitetura de sistemas distribuídos.
- Fornecer feedback personalizado e recomendações de conteúdo para melhoria da escrita, com base nas competências do ENEM.




## Requisitos Técnicos

### 1. Agentes de IA

- Mínimo de dois agentes (modelos) de IA.
- Pelo menos um modelo deve ser local e containerizado (Docker).

### 2. Comunicação

- Implementar comunicação entre IAs utilizando MCP (Message Passing Interface) ou A2A (Agent-to-Agent).
- As IAs devem funcionar como microserviços.
- Implementação de uma API na solução.

### 3. Controle de Versão

- Utilização obrigatória do GitHub para desenvolvimento.
- O GitHub servirá como comprovação de participação nas atividades em grupo.

### 4. Documentação Arquitetônica

- Entrega de duas visões arquitetônicas:
  - Visão inicial pré-modelagem de ameaças.
  - Visão final após implementação das medidas de mitigação.

### 5. Validação do Problema

- Necessária comprovação da relevância do problema abordado.
- Documentação clara da "dor" que o projeto pretende resolver.




## Validação do Problema

A correção de redações, especialmente em larga escala como no ENEM, é um processo complexo, demorado e suscetível a vieses humanos. A demanda por feedback rápido e consistente para milhões de estudantes anualmente é um desafio significativo para o sistema educacional. A falta de feedback detalhado e personalizado impede que os estudantes compreendam suas deficiências e melhorem sua escrita de forma eficaz.

Neste contexto, a "dor" que este projeto pretende resolver é a **ineficiência e a subjetividade na correção de redações, que limitam o desenvolvimento da escrita dos estudantes e sobrecarregam os educadores.** Um sistema automatizado de correção de redações com IA pode:

- **Reduzir o tempo de correção:** Permitindo que os estudantes recebam feedback quase instantaneamente.
- **Aumentar a consistência:** Minimizando a variação na avaliação entre diferentes corretores.
- **Fornecer feedback detalhado e personalizado:** Identificando pontos fortes e fracos específicos em relação às competências do ENEM, e sugerindo materiais de estudo relevantes.
- **Escalar o processo:** Atendendo a um grande volume de redações sem comprometer a qualidade do feedback.

Isso empodera os estudantes com ferramentas para autoaprendizagem e alivia a carga de trabalho dos professores, permitindo que se concentrem em aspectos mais estratégicos do ensino. A relevância do problema é corroborada pela crescente busca por soluções tecnológicas na educação e pela importância da proficiência em escrita para o sucesso acadêmico e profissional.




## Documentação Arquitetônica

A documentação arquitetônica deste projeto será dividida em duas visões principais, refletindo a evolução da segurança e do design do sistema:

1. **Visão Inicial (Pré-Modelagem de Ameaças):** Esta visão descreverá a arquitetura proposta do sistema antes da análise e mitigação de ameaças. Ela incluirá os componentes principais, suas interações e as tecnologias planejadas, sem considerar inicialmente as vulnerabilidades de segurança.

2. **Visão Final (Pós-Implementação de Medidas de Mitigação):** Após a realização da modelagem de ameaças e a definição de medidas de mitigação, esta visão apresentará a arquitetura revisada. Ela detalhará como as preocupações de segurança foram endereçadas, as medidas de proteção implementadas e as mudanças arquitetônicas resultantes para garantir um sistema robusto e seguro.

Ambas as visões serão entregues como documentos separados, complementando este `README.md`.





## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.



