# Equipa e papéis

Este documento prepara a atribuição de papéis, que o enunciado pede na Etapa 2 e que tem de ser decidida pela equipa. Segue a aula T09 (Gestão de Equipas) e a parte "Pessoas" da T05.

**O que está feito:** a estrutura da equipa, os papéis e as responsabilidades, a matriz de responsabilidades por pacote de trabalho e o processo de comunicação.

**O que falta, na reunião:**
- preencher a matriz de competências (cada pessoa avalia-se);
- atribuir os papéis às pessoas;
- confirmar as horas disponíveis por semana.

## 1. Estrutura da equipa

**Equipa:** Rodrigo, Reis, Miguel, Ze e Edson (5 pessoas, dentro dos 3 a 9 do Scrum).

**Organização horizontal.** A T09 compara três tipos de organização:

| Fator (T09) | Hierárquica | Matricial | Horizontal | O nosso projeto |
|---|---|---|---|---|
| Inovação | baixa | baixa | alta | Precisa de alguma: integrações externas e infraestrutura nova para a equipa |
| Dimensão | grande | grande | pequena | Equipa de 5 |
| Vida da equipa | curta | curta | longa | A mesma equipa em PGP e PTIR |
| Modularidade | elevada | elevada | baixa | Média: os pacotes de trabalho separam bem as partes |
| Sociabilidade | baixa | baixa | alta | Muita comunicação entre frontend, backend e redes |

A organização **horizontal** é a que encaixa: todos contribuem para as decisões, e o gestor de projeto coordena sem ser um superior hierárquico. Na terminologia da T05, corresponde ao paradigma **aberto**: muita comunicação e decisões por consenso, bom para problemas com um misto de controlo e inovação. É também a organização das equipas ágeis (auto-organizadas, com coordenação frequente).

**Amplitude da comunicação.** Segundo a T09, cada programador deve interagir com frequência com 3 a 7 pessoas. Numa equipa de 5, cada pessoa fala com as outras 4, o que está dentro da amplitude ideal.

## 2. Papéis

O enunciado sugere os papéis abaixo. Com 5 pessoas, cada pessoa acumula papéis. A coluna "Competências principais" serve para escolher quem fica com cada papel: a T09 diz que o papel vai para a pessoa com melhor pontuação nas competências que ele exige.

**Tabela 1 — Papéis, responsabilidades e competências**

| Papel | Responsabilidades | Competências principais |
|---|---|---|
| Gestor de projeto (e, em parte, product owner) | Ordena o backlog e distribui os itens pelos sprints (nota 20 do enunciado); planeia e acompanha (Gantt, earned value analysis); gere os riscos; conduz as reuniões | Liderança, planeamento, comunicação |
| Arquiteto de sistema | Decide a arquitetura da aplicação e a estrutura do código; mantém a especificação OpenAPI | Desenho de software, REST |
| Programador de frontend | Implementa os ecrãs em Angular (subtarefas .2), com design responsivo | Angular, HTML/CSS |
| Programador de backend | Implementa a API em Express (subtarefas .1) e as integrações externas | Node.js, Express, APIs externas |
| Consultor de dados | Garante que o modelo de dados e as restrições de integridade são respeitados (RNF-02) | Modelação de dados |
| Administrador da base de dados | Instala e configura o MongoDB principal e de reserva; backup e restauro (RNF-14) | MongoDB, replicação |
| Especialista de segurança e redes | Lidera o pacote de Redes: balanceadores, redes, firewall, TLS e scripts | Redes, Linux, segurança |
| Técnico de manutenção | Integração contínua, lançamento em produção e monitorização | GitHub Actions, Linux |
| Responsável de testes com utilizadores | Prepara e conduz os testes com utilizadores e analisa o questionário SUS (RNF-03) | Usabilidade, comunicação |

## 3. Matriz de competências (preencher na reunião)

Matriz da T09: para cada competência necessária ao projeto, cada pessoa indica a **capacidade** (C) e o **interesse** (I), de 1 a 5. As competências cobrem as três famílias da T09: técnicas, de gestão e de comunicação.

**Tabela 2 — Matriz de competências**

| Competência | Rodrigo (C/I) | Reis (C/I) | Miguel (C/I) | Ze (C/I) | Edson (C/I) |
|---|---|---|---|---|---|
| Angular, HTML e CSS | / | / | / | / | / |
| Node.js e Express | / | / | / | / | / |
| MongoDB e modelação de dados | / | / | / | / | / |
| Redes, Linux e cloud | / | / | / | / | / |
| Segurança (TLS, firewall) | / | / | / | / | / |
| Testes automáticos | / | / | / | / | / |
| Planeamento e gestão | / | / | / | / | / |
| Comunicação e escrita | / | / | / | / | / |
| Usabilidade e testes com utilizadores | / | / | / | / | / |

Regra para atribuir os papéis: cada papel vai para a pessoa com a maior soma de capacidade e interesse nas competências principais do papel (Tabela 1). Em caso de empate, decide a equipa, por consenso. O objetivo é que cada pessoa tenha um papel técnico e que o trabalho fique equilibrado.

## 4. Matriz de responsabilidades: papéis por pacote de trabalho

A T09 relaciona as tarefas da WBS com os papéis. Legenda: **R** = responsável (lidera e responde pelo resultado); **P** = participa.

**Tabela 3 — Responsabilidades por pacote de trabalho**

| Pacote | Gestor | Arquiteto | Frontend | Backend | Dados | BD | Seg. e redes | Manutenção | Testes utiliz. |
|---|---|---|---|---|---|---|---|---|---|
| WP.1 Gestão do projeto | R | P | P | P | P | P | P | P | P |
| WP.2 Infraestrutura e arquitetura | | R | P | P | P | P | | P | |
| WP.3 a WP.8 Funcionalidades | P | P | R (.2) | R (.1) | P | | | | |
| WP.9 Integrações externas | | P | P | R | | | | | |
| WP.10 Qualidade, testes e RNF | | P | P | P | P | P | | R | R (QUA.05 a QUA.07) |
| WP.11 Tecnologias de Redes | | P | | | | R (RED.11, RED.18) | R | P | |

## 5. Matriz de responsabilidades: pessoas por papel (preencher na reunião)

**Tabela 4 — Pessoas por papel**

| Papel | Pessoa | Reserva (risco R06) |
|---|---|---|
| Gestor de projeto | | |
| Arquiteto de sistema | | |
| Programador de frontend | | |
| Programador de backend | | |
| Consultor de dados | | |
| Administrador da base de dados | | |
| Especialista de segurança e redes | | |
| Técnico de manutenção | | |
| Responsável de testes com utilizadores | | |

A coluna "Reserva" aplica a mitigação do risco R06 (`etapa2/riscos/gestao-risco.md`): cada papel crucial tem uma segunda pessoa que acompanha o trabalho.

## 6. Comunicação e coordenação

Técnicas da T09 aplicadas ao projeto:

**Tabela 5 — Comunicação e coordenação**

| Técnica (T09) | Como se aplica | Quando | Item do backlog |
|---|---|---|---|
| Reunião de comunicação | Reunião curta da equipa: o que cada um fez, o que vai fazer, o que o bloqueia | 2 vezes por semana | GES.03 |
| Revisão conjunta | Revisão de cada pull request por outra pessoa, com critérios definidos (testes a passar, especificação OpenAPI respeitada) | Em cada alteração | INF.01 |
| Revisão técnica | Verificação e validação do sprint: testes automáticos e demonstração | Fim de cada sprint | GES.04 |
| Revisão de gestão | Estado do projeto: esforço gasto, earned value analysis, alterações e reavaliação dos riscos | Fim de cada sprint | GES.05, GES.06 |
| Relatório de progresso | Resumo do estado para o cliente e para medição | Em cada demonstração | GES.04 |
| Relatório de tempo (timesheet) | Cada pessoa regista as horas por tarefa no Planner; a T09 diz que é indispensável para medir o esforço | Semanal | GES.06 |
| Documentos e código | Repositório GitHub, issues e Planner como fonte única de informação | Contínuo | GES.01 |
