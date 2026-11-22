# Gestão de risco

Segue a aproximação **proativa** da aula T08 (Pressman, capítulo 35): identificar os riscos antes do trabalho técnico, analisar a probabilidade e o impacto, ordenar, traçar uma linha de corte e preparar um plano RMMM (mitigação, monitorização e gestão) para os riscos acima da linha.

As probabilidades e os impactos são uma **proposta para a equipa rever** na reunião. A T08 diz que estes valores vêm de dados históricos ou da opinião dos elementos da equipa, e a equipa não tem dados históricos.

## 1. Identificação

Os riscos foram identificados com a **checklist de categorias** da T08, a partir do âmbito do produto (Etapa 1), do backlog (`etapa2/backlog/backlog-wbs.md`) e do enunciado de Redes de PTIR.

**Tabela 1 — Categorias de risco usadas**

| Sigla | Categoria (checklist da T08) | Tipo (T08) |
|---|---|---|
| DI | Dimensão do produto | Projeto |
| IN | Impacto do negócio | Negócio |
| CC | Caraterísticas dos clientes | Projeto |
| DF | Definição do processo | Projeto |
| AD | Ambiente de desenvolvimento | Técnico |
| TC | Tecnologia a construir | Técnico |
| EX | Experiência da equipa | Projeto |

Respostas às perguntas de **avaliação global do projeto** da T08 que mais pesaram na identificação:

| Pergunta da T08 | Resposta | Risco |
|---|---|---|
| Os requisitos são estáveis? | Não totalmente: o enunciado diz que o cliente pode pedir alterações e já houve uma versão nova (4/nov). | R04 |
| A equipa tem experiência com a tecnologia que vai ser usada? | Pouca, tanto na stack MEAN como em infraestrutura distribuída. | R02, R03 |
| A equipa tem a combinação certa de aptidões? | Por confirmar com a matriz de competências (T09). | R02, R03, R10 |
| O número de elementos da equipa é adequado? | Sim: 5 pessoas, dentro dos 3 a 9 do Scrum, mas todas em part-time. | R06 |

## 2. Análise

Escalas usadas, como na T08:
- **Probabilidade:** escala quantitativa de 0% a 100%.
- **Impacto:** 1 = catastrófico, 2 = crítico, 3 = marginal, 4 = negligenciável. É estimado nas quatro componentes da T08 (**D**esempenho, **S**uporte, **C**usto e **P**laneamento), e o impacto do risco é a média.

**Tabela 2 — Tabela de riscos ordenada**

A tabela está ordenada como manda a T08: maiores probabilidades e impactos em cima, e a probabilidade pesa mais do que o impacto. Por isso a ordem é por probabilidade e, dentro da mesma probabilidade, pelo impacto mais grave.

| # | Risco | Cat. | Prob. | D | S | C | P | Impacto (média) | Itens afetados |
|---|---|---|---|---|---|---|---|---|---|
| R01 | Estimativas de esforço demasiado baixas: a equipa não tem dados históricos de projetos anteriores | DI | 70% | 3 | 3 | 2 | 1 | 2,25 (Crítico) | Todos os sprints |
| R02 | Pouca experiência da equipa com a stack MEAN (Angular, Express, MongoDB) | EX | 60% | 2 | 2 | 3 | 2 | 2,25 (Crítico) | WP.2 a WP.8 |
| R03 | Pouca experiência com infraestrutura distribuída: balanceadores, replicação da base de dados, firewall | EX | 60% | 2 | 3 | 3 | 1 | 2,25 (Crítico) | WP.11 |
| R04 | O cliente altera os requisitos durante o projeto (o enunciado prevê-o e já mudou a 4/nov) | CC | 50% | 2 | 3 | 3 | 2 | 2,50 (Crítico) | Backlog |
| R05 | Testes com utilizadores deixados para o fim, sem tempo para a iteração de melhoria | DF | 50% | 2 | 3 | 4 | 2 | 2,75 (Marginal) | QUA.05 a QUA.07 |
| R06 | Membros da equipa indisponíveis em épocas de avaliação de outras cadeiras ou por doença | EX | 50% | 3 | 4 | 3 | 2 | 3,00 (Marginal) | Todos os sprints |
| R07 | A passagem da base de dados de reserva a principal não funciona como esperado (MongoDB com só duas instâncias) | TC | 40% | 1 | 3 | 3 | 2 | 2,25 (Crítico) | RED.11, RED.18 |
| R08 | Integração do pagamento mais difícil do que previsto (webhooks, reserva de unidades, falhas a meio) | TC | 40% | 1 | 3 | 3 | 2 | 2,25 (Crítico) | US.28, INT.03, INT.04 |
| R09 | Frontend e backend desencontrados porque a API não está bem definida | DF | 40% | 3 | 2 | 3 | 2 | 2,50 (Crítico) | INF.10, todas as US |
| | **— linha de corte —** | | | | | | | | |
| R10 | Responsabilidades mal definidas: tarefas sem dono ou feitas em duplicado | DF | 30% | 3 | 3 | 3 | 2 | 2,75 (Marginal) | WP.1 |
| R11 | Custo da cloud acima dos créditos gratuitos (pelo menos 6 máquinas virtuais) | IN | 30% | 3 | 4 | 1 | 3 | 2,75 (Marginal) | RED.08, RNF-15 |
| R12 | Vulnerabilidades de segurança descobertas só no fim | TC | 30% | 2 | 2 | 4 | 3 | 2,75 (Marginal) | RED.21, INF.06 |
| R13 | Limites e indisponibilidade dos serviços externos (Nominatim e MusicBrainz a 1 pedido/s, Cover Art Archive) | TC | 30% | 3 | 3 | 4 | 3 | 3,25 (Marginal) | INT.01, INT.05, INT.06 |
| R14 | Dificuldade em obter um nome de domínio gratuito e o certificado TLS | AD | 30% | 3 | 4 | 3 | 3 | 3,25 (Marginal) | RED.13, RED.14 |
| R15 | Perda de código ou de dados por má utilização do Git ou falta de backups | AD | 20% | 2 | 3 | 4 | 2 | 2,75 (Marginal) | INF.01, QUA.08 |
| R16 | Prazo das demonstrações antecipado pelos docentes | IN | 10% | 3 | 4 | 4 | 1 | 3,00 (Marginal) | M.1 a M.3 |

**Linha de corte.** A T08 propõe o princípio de Pareto adaptado ao risco: 80% do risco vem de 20% dos riscos. Para medir isto, calculou-se para cada risco a exposição *probabilidade × (5 − impacto médio)*, em que 5 − impacto converte a escala (1 = catastrófico) num valor que cresce com a gravidade. Os **9 riscos com probabilidade igual ou superior a 40%** (R01 a R09) concentram cerca de **76% da exposição total**. Ficam acima da linha e têm plano RMMM. Os restantes são monitorizados nas reuniões de acompanhamento.

## 3. Plano RMMM

Para cada risco acima da linha, a T08 pede três partes:
- **Mitigação:** como evitar o risco?
- **Monitorização:** que fatores seguir para saber se o risco se aproxima?
- **Gestão:** que plano de contingência existe se o risco se concretizar?

### R01 — Estimativas de esforço demasiado baixas (70%, crítico)

- **Mitigação:**
  - Estimar por decomposição de cada user story em subtarefas (T06), com três valores (otimista, provável, pessimista).
  - Comparar com a estimativa por pontos de função e COCOMO (`etapa2/estimacao/estimativa-controlo.md`).
  - Não planear os sprints a 100% do esforço disponível: deixar uma margem (por exemplo, 15%) para imprevistos.
  - A T08 avisa que o teste, a integração e a revisão costumam ser mal estimados, por isso têm itens próprios no backlog (QUA, RED.20 a RED.22).
- **Monitorização:**
  - Comparar o esforço planeado com o realizado no fim de cada semana, com timesheets (T09).
  - Calcular a earned value analysis (T07) em cada sprint review: SPI e CPI abaixo de 1 indicam que o risco se concretiza.
- **Gestão:**
  - Rever as estimativas no planning poker de ajuste entre sprints (GES.07, nota 21 do enunciado).
  - Passar as user stories de menor prioridade para o sprint seguinte, como propõe a T07 para prazos irrealistas, em vez de acrescentar horas sem limite.

### R02 — Pouca experiência com a stack MEAN (60%, crítico)

- **Mitigação:**
  - Formação no início do sprint 1: cada pessoa faz o tutorial oficial do Angular ou do Express, conforme o seu papel.
  - O esqueleto do frontend e do backend (INF.02, INF.03) é feito em conjunto, para servir de modelo.
  - Revisão de código por pull request: cada alteração é vista por outra pessoa.
- **Monitorização:**
  - Número de pull requests parados há mais de 3 dias.
  - Tarefas técnicas que ultrapassam a estimativa pessimista.
- **Gestão:**
  - Trabalho em pares nas tarefas bloqueadas, juntando quem tem mais experiência com quem tem menos.
  - Pedir ajuda aos docentes nas aulas de PTIR.

### R03 — Pouca experiência com infraestrutura distribuída (60%, crítico)

- **Mitigação:**
  - Fazer o relatório de design de Redes (RED.01 a RED.07) logo no início, para pensar a arquitetura antes de a construir, como pede o enunciado de Redes.
  - Seguir os guiões indicados no enunciado de Redes: guião de HAProxy de PTR, documentação do Nginx e Let's Encrypt.
  - Montar cedo uma versão mínima da infraestrutura (1 balanceador, 1 servidor, 1 base de dados) e só depois a redundância.
- **Monitorização:**
  - Resultado das reuniões de avaliação de Redes (M.R1 a M.R4).
  - Scripts de criação (RED.17 a RED.19) que ainda não correm do início ao fim.
- **Gestão:**
  - Concentrar o especialista de segurança e redes e mais uma pessoa nas tarefas RED atrasadas.
  - Usar containers para simplificar a instalação, o que o enunciado de Redes permite.

### R04 — Alterações aos requisitos (50%, crítico)

- **Mitigação:**
  - Scrum: o sprint backlog não muda durante o sprint; as alterações entram no product backlog e são ordenadas pelo product owner.
  - Mostrar o produto ao cliente no fim de cada sprint (M.1 a M.3) para detetar cedo diferenças de entendimento.
  - Manter as suposições documentadas (capítulo 7 da Etapa 1).
- **Monitorização:**
  - Versões novas do enunciado no Moodle.
  - Pedidos de alteração nas demonstrações e número de itens novos no backlog por sprint.
- **Gestão:**
  - Estimar a alteração em planning poker e retirar do sprint seguinte itens de esforço equivalente, para não ultrapassar o esforço disponível (regra do enunciado).

### R05 — Testes com utilizadores no fim, sem tempo para melhorar (50%, marginal)

- **Mitigação:**
  - Preparar o guião e o questionário SUS (QUA.05) no sprint 2.
  - Fazer os testes (QUA.06) no início do sprint 3, ou no fim do sprint 2, deixando a iteração de melhoria (QUA.07) para o resto do sprint 3, como recomenda a RNF-03.
- **Monitorização:**
  - Data prevista dos testes no Gantt e percentagem das user stories necessárias já concluídas.
- **Gestão:**
  - Testar com as funcionalidades que existirem (protótipo parcial) e limitar a iteração de melhoria aos problemas mais graves encontrados.

### R06 — Membros indisponíveis (50%, marginal)

- **Mitigação:**
  - Recolher as datas de avaliação de todas as cadeiras no início do semestre e reduzir o esforço disponível dessas semanas no planeamento.
  - Cada tarefa crítica tem uma pessoa de reserva que acompanha o trabalho. A T08 dá este exemplo para a rotatividade de pessoal.
  - Documentação e código no repositório, para que outra pessoa consiga continuar.
- **Monitorização:**
  - Reuniões de acompanhamento (GES.03): quem está atrasado e porquê.
  - Horas registadas abaixo das planeadas.
- **Gestão:**
  - A pessoa de reserva assume a tarefa e o gestor de projeto reorganiza a semana. Se a falta for longa, o product owner adia itens de menor prioridade.

### R07 — Falha na passagem da base de dados de reserva a principal (40%, crítico)

- **Mitigação:**
  - Fazer uma prova de conceito da replicação do MongoDB logo no sprint 1, antes da aplicação depender dela.
  - Com só duas instâncias não há maioria para eleger a principal de forma automática, por isso a passagem é manual (o script `promote_db_backup.sh` do enunciado de Redes). Ensaiar este script cedo.
- **Monitorização:**
  - Ensaio do cenário de falha (`kill_db_primary.sh` seguido de `promote_db_backup.sh`) no fim de cada sprint, com verificação de que os dados ficaram iguais.
- **Gestão:**
  - Repor a base de dados a partir do backup (QUA.08) e rever a configuração da replicação com os guiões de Redes ou com os docentes.

### R08 — Integração do pagamento mais difícil (40%, crítico)

- **Mitigação:**
  - Prova de conceito do Stripe em modo de teste (INT.03) antes da US28, incluindo o webhook.
  - Seguir o fluxo já desenhado na Etapa 1 (Figuras 14 e 15): reserva das unidades, versão esgotada a meio, falha e cancelamento.
- **Monitorização:**
  - Casos de teste do pagamento (aceite, recusado, versão esgotada) a passar na integração contínua.
- **Gestão:**
  - Entregar primeiro só o Stripe e passar o PayPal (INT.04) para o sprint seguinte. A US28 b) só exige poder escolher um serviço externo.

### R09 — Frontend e backend desencontrados (40%, crítico)

- **Mitigação:**
  - A especificação OpenAPI (`etapa2/api/api.yaml`) é o contrato entre frontend e backend, e qualquer mudança passa primeiro por ela (INF.10).
  - Testes à API (QUA.02) contra a especificação.
- **Monitorização:**
  - Erros de integração encontrados nos testes de fumo diários (T10).
  - Endpoints implementados que não estão na especificação.
- **Gestão:**
  - Revisão técnica conjunta (T09) entre quem faz o frontend e quem faz o backend da funcionalidade, para acertar o contrato e atualizar a especificação.

## 4. Riscos abaixo da linha de corte

Não têm plano RMMM completo, mas são revistos em cada revisão de gestão (T09).

| # | Fator a monitorizar |
|---|---|
| R10 | Tarefas sem responsável no Planner; matriz de responsabilidades (T09) atualizada |
| R11 | Consumo de créditos na consola da cloud; desligar máquinas que não estão a ser usadas |
| R12 | Resultados do OWASP ZAP e do nmap corridos a meio do projeto, e não só no fim |
| R13 | Respostas 429 ou 503 dos serviços; cache das respostas e respeito pelos limites (capítulo 6 da Etapa 1) |
| R14 | Escolher o fornecedor do domínio no arranque do projeto, como recomenda o enunciado de Redes |
| R15 | Proteção do ramo principal no GitHub; ensaio do procedimento de restauro (QUA.08) |
| R16 | Avisos no Moodle; a ordem por dependências do backlog já põe o essencial nos primeiros sprints |

## 5. Avaliação de custos

A T08 pede que se avalie se as medidas RMMM têm um custo relevante. As medidas acima custam sobretudo **tempo da equipa**: formação, provas de conceito, ensaios dos cenários de falha e a margem de 15% nos sprints. Este tempo tem de entrar no esforço necessário, para que não ultrapasse o esforço disponível. Não há custos em dinheiro, desde que se usem os modos de teste dos pagamentos e os créditos de estudante da cloud (RNF-15). Nenhum dos riscos, se se concretizar, põe em causa a viabilidade do projeto: no pior caso, adiam-se user stories de menor prioridade para manter as demonstrações.

## 6. Processo contínuo

A gestão de risco é contínua (princípio 5 da T08). A tabela é revista em cada **revisão de gestão**, no fim de cada sprint (GES.04 e GES.05):
- atualizar as probabilidades;
- acrescentar riscos novos;
- retirar os que deixaram de existir.
