# Apresentação da Etapa 2: guião dos slides

O enunciado exige que todas as pessoas do grupo estejam presentes na apresentação. Este guião propõe 13 slides e distribui-os pelos cinco membros. O apresentador de cada bloco deve ser quem fica com o papel correspondente, por isso confirmem a distribuição depois de atribuir os papéis na reunião.

Os slides marcados "depois da reunião" precisam dos dados da equipa. A apresentação (`.pptx`) gera-se no fim, quando tudo estiver preenchido.

**Tabela 1 — Slides**

| # | Título | Conteúdo | Fonte | Apresentador (proposta) | Estado |
|---|---|---|---|---|---|
| 1 | Planeamento do projeto | Capa: grupo 12, nomes, Etapa 2 | — | — | Pronto |
| 2 | Pessoas, produto, processo e projeto | Os 4P da T05 como estrutura do planeamento; o que foi planeado | Relatório, cap. 1 | Gestor de projeto | Pronto |
| 3 | Equipa e papéis | Organização horizontal (comparação da T09); papéis e reservas | Relatório, cap. 2 | Gestor de projeto | Depois da reunião |
| 4 | Ferramentas e software | Desenvolvimento vs. funcionamento; stack MEAN; peças de Redes; sem serviços geridos | Relatório, 3.1 | Arquiteto | Pronto |
| 5 | API REST | 46 operações em OpenAPI 3.0; `/utilizadores/eu`; códigos HTTP; pagamento em dois passos | Relatório, 3.2 e Anexo A | Programador de backend | Pronto |
| 6 | Processo | Scrum, 3 sprints, demos no fim de março, abril e maio; 4 reuniões de Redes; Planner PLANO-PTIR-12 | Relatório, cap. 4 | Gestor de projeto | Faltam datas |
| 7 | Backlog e WBS | 84 itens, 11 pacotes, decomposição das US, dependências | Relatório, 5.1 | Arquiteto | Pronto |
| 8 | Esforço disponível e planning poker | Horas por sprint com margem de 15%; como correu o planning poker; total de story points | Relatório, 5.2 e 5.3 | Responsável de testes | Depois da reunião |
| 9 | Esforço necessário e estimativa de controlo | Decomposição com três valores; pontos de função e COCOMO; COCOMO sobrestima (exemplo da T06); necessário ≤ disponível | Relatório, 5.4 | Consultor de dados | Controlo pronto |
| 10 | Sprints e Gantt | Ocupação de cada sprint; Gantt com caminho crítico; esforço por pessoa | Relatório, 5.5 e 5.6 | Gestor de projeto | Depois das estimativas |
| 11 | Componente de Redes | Arquitetura distribuída (2 LB, 2 servidores, 2 BD, 2 redes); segurança; 10 scripts; testes | Backlog, secção 5 | Especialista de segurança e redes | Pronto |
| 12 | Gestão de risco | Tabela ordenada; linha de corte (76% da exposição); RMMM de 2 ou 3 riscos de topo (R01, R03, R07) | Relatório, cap. 6 | Especialista de segurança e redes | Pronto |
| 13 | Obrigado | — | — | — | Pronto |

## Mensagens principais para levar à apresentação

1. **O planeamento segue os métodos das aulas:**
   - a WBS e os pacotes de trabalho (T07);
   - o planning poker e a decomposição com três valores (T06);
   - a matriz de competências e a de responsabilidades (T09);
   - a tabela de riscos com plano RMMM (T08).
2. **O esforço necessário cabe no disponível**, com 15% de margem. Mostrar o número final.
3. **O COCOMO sem calibração não serve:** dá 45 pessoa.mês. Por isso a equipa usou a produtividade histórica do projeto de PTI que aparece na T06.
4. **O enunciado de Redes mudou o plano da Etapa 1:** a base de dados passa a correr em máquinas virtuais, e não no MongoDB Atlas, porque o enunciado proíbe serviços geridos.
5. **Os maiores riscos** são as estimativas, a pouca experiência com MEAN e com infraestrutura distribuída, e o failover da base de dados. Cada um tem um plano.
