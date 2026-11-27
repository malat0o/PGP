# Introdução

Este relatório apresenta a segunda etapa do projeto de Planeamento e Gestão de Projeto de 2026/2027: o **planeamento do desenvolvimento**, no próximo semestre, em PTIR, da aplicação web de gestão de coleções de álbuns de música em formato físico desenhada na Etapa 1.

A aula T05 diz que um bom gestor de projetos se foca em quatro aspetos, por esta ordem: **pessoas, produto, processo e projeto**. O enunciado da Etapa 2 pede o planeamento tendo em conta esses mesmos quatro aspetos, por isso o relatório segue essa ordem.

## Organização do relatório

- **Capítulo 2 — Pessoas:** equipa, organização, papéis e comunicação.
- **Capítulo 3 — Produto:** ferramentas de desenvolvimento, software da aplicação e descrição preliminar da API REST.
- **Capítulo 4 — Processo:** Scrum, sprints e acompanhamento.
- **Capítulo 5 — Projeto:** backlog e WBS, esforço disponível, planning poker, esforço necessário, distribuição pelos sprints e mapa de Gantt.
- **Capítulo 6 — Gestão de risco:** tabela de riscos e plano de mitigação, monitorização e gestão.
- **Anexos:** lista dos endpoints da API e decomposição das user stories.

A especificação completa da API está no ficheiro `api.yaml`, entregue no ZIP.

# Pessoas

## Equipa e organização

A equipa tem cinco pessoas: Rodrigo, Reis, Miguel, Ze e Edson. Este número está dentro dos 3 a 9 elementos recomendados para equipas Scrum (T05).

A aula T09 compara três tipos de organização. A Tabela 1 resume a comparação e a escolha.

**Tabela 1 — Escolha da organização da equipa (T09)**

| Fator | Hierárquica | Matricial | Horizontal | O nosso projeto |
|---|---|---|---|---|
| Inovação | baixa | baixa | alta | Precisa de alguma: integrações externas e infraestrutura nova para a equipa |
| Dimensão | grande | grande | pequena | Equipa de 5 |
| Vida da equipa | curta | curta | longa | A mesma equipa em PGP e PTIR |
| Sociabilidade | baixa | baixa | alta | Muita comunicação entre frontend, backend e redes |

A equipa adota uma **organização horizontal**: todos contribuem para as decisões, e o gestor de projeto coordena sem ser um superior hierárquico. Corresponde ao paradigma **aberto** da T05, adequado a problemas que misturam controlo e inovação, e às equipas ágeis, que são auto-organizadas. Numa equipa de 5, cada pessoa comunica regularmente com as outras quatro, dentro da amplitude ideal de 3 a 7 pessoas indicada na T09.

## Papéis

Os papéis são os sugeridos no enunciado. Com 5 pessoas, cada pessoa acumula papéis. Para os atribuir, a equipa preencheu a **matriz de competências** da T09: para cada competência necessária, cada pessoa indicou a sua capacidade e o seu interesse, de 1 a 5. Cada papel foi para a pessoa com melhor pontuação nas competências que o papel exige.

**[A PREENCHER NA REUNIÃO: matriz de competências, Tabela 2 de `etapa2/equipa/papeis.md`]**

**[NOMES PROVISÓRIOS: Pessoa A a E, até cada um escolher o papel]**

**Tabela 2 — Papéis, responsabilidades e pessoas**

| Papel | Responsabilidades | Pessoa | Reserva |
|---|---|---|---|
| Gestor de projeto (e, em parte, product owner) | Ordena o backlog e distribui os itens pelos sprints; planeia e acompanha (Gantt, earned value analysis); gere os riscos | Pessoa A | Pessoa C |
| Arquiteto de sistema | Arquitetura da aplicação e estrutura do código; especificação OpenAPI | Pessoa C | Pessoa B |
| Programador de frontend | Ecrãs em Angular, com design responsivo | Pessoa B | Pessoa A |
| Programador de backend | API em Express e integrações externas | Pessoa C | Pessoa E |
| Consultor de dados | Modelo de dados e restrições de integridade (RNF-02) | Pessoa C | Pessoa E |
| Administrador da base de dados | MongoDB principal e de reserva; backup e restauro (RNF-14) | Pessoa E | Pessoa D |
| Especialista de segurança e redes | Componente de Redes: balanceadores, redes, firewall, TLS, scripts | Pessoa D | Pessoa E |
| Técnico de manutenção | Integração contínua, lançamento em produção, monitorização | Pessoa D | Pessoa C |
| Responsável de testes com utilizadores | Testes com utilizadores e questionário SUS (RNF-03) | Pessoa A | Pessoa B |

A coluna "Reserva" aplica a mitigação do risco R06 (capítulo 6): cada papel crucial tem uma segunda pessoa que acompanha o trabalho.

A Tabela 3 é a **matriz de responsabilidades** da T09, que liga os papéis aos pacotes de trabalho da WBS (capítulo 5). R = responsável; P = participa.

**Tabela 3 — Matriz de responsabilidades: papéis por pacote de trabalho**

| Pacote | Gestor | Arquiteto | Frontend | Backend | Dados | BD | Seg. e redes | Manutenção | Testes utiliz. |
|---|---|---|---|---|---|---|---|---|---|
| WP.1 Gestão do projeto | R | P | P | P | P | P | P | P | P |
| WP.2 Infraestrutura e arquitetura | | R | P | P | P | P | | P | |
| WP.3 a WP.8 Funcionalidades | P | P | R | R | P | | | | |
| WP.9 Integrações externas | | P | P | R | | | | | |
| WP.10 Qualidade, testes e RNF | | P | P | P | P | P | | R | R |
| WP.11 Tecnologias de Redes | | P | | | | R | R | P | |

## Comunicação e coordenação

A Tabela 4 aplica as técnicas de comunicação e coordenação da T09.

**Tabela 4 — Comunicação e coordenação**

| Técnica (T09) | Como se aplica | Quando |
|---|---|---|
| Reunião de comunicação | Reunião curta: o que cada um fez, vai fazer e o que o bloqueia | 2 vezes por semana |
| Revisão conjunta | Cada pull request é revista por outra pessoa, com critérios definidos | Em cada alteração |
| Revisão técnica | Verificação e validação do sprint: testes e demonstração | Fim de cada sprint |
| Revisão de gestão | Esforço gasto, earned value analysis, alterações e reavaliação dos riscos | Fim de cada sprint |
| Relatório de progresso | Resumo do estado para o cliente | Em cada demonstração |
| Relatório de tempo (timesheet) | Horas por tarefa registadas no Planner, para medir o esforço | Semanal |

# Produto

O produto foi desenhado na Etapa 1: 29 user stories, 21 casos de uso, um modelo de dados com 19 classes e 52 restrições de integridade, 12 esboços e 6 serviços externos. Este capítulo descreve os recursos necessários para o construir e a API que o vai suportar.

## Ferramentas e software

Segundo a T06, os recursos de um projeto são as pessoas (capítulo 2), o software reutilizável e o ambiente de desenvolvimento. O enunciado pede que se distingam as ferramentas de desenvolvimento do software necessário ao funcionamento da aplicação.

**Tabela 5 — Ferramentas de desenvolvimento**

| Ferramenta | Propósito | Documentação |
|---|---|---|
| Visual Studio Code | Editor de código | https://code.visualstudio.com/docs |
| Git e GitHub | Controlo de versões, pull requests e revisão de código (RNF-05, RNF-06) | https://git-scm.com/doc · https://docs.github.com |
| GitHub Actions | Integração contínua e lançamento em produção (RNF-06, RNF-07) | https://docs.github.com/actions |
| npm e Angular CLI | Dependências e compilação do frontend e do backend | https://docs.npmjs.com · https://angular.dev/tools/cli |
| Swagger Editor | Especificação OpenAPI da API (RNF-09) | https://editor.swagger.io |
| Postman | Testar os pedidos à API | https://learning.postman.com |
| Jest e ferramentas de teste do Angular | Testes unitários e de integração (RNF-13) | https://jestjs.io/docs/getting-started · https://angular.dev/guide/testing |
| Playwright | Testes de regressão no browser (T10) | https://playwright.dev/docs/intro |
| Docker e MongoDB Compass | Base de dados em desenvolvimento e consulta dos dados | https://docs.docker.com · https://www.mongodb.com/docs/compass/ |
| Locust | Testes de carga (enunciado de Redes) | https://docs.locust.io |
| nmap e OWASP ZAP | Testes de vulnerabilidades (enunciado de Redes) | https://nmap.org/docs.html · https://www.zaproxy.org/docs/ |
| Microsoft Planner e Teams | Backlog, sprints e acompanhamento no plano partilhado PLANO-PTIR-12 | https://support.microsoft.com/planner |
| Microsoft Project | Mapa de Gantt, dependências e caminho crítico | https://support.microsoft.com/project |
| draw.io | Diagramas, incluindo a arquitetura distribuída | https://www.drawio.com/doc/ |

**Tabela 6 — Software necessário ao funcionamento da aplicação**

Todos são COTS (classificação da T06): software de terceiros, pronto a usar e gratuito ou com plano gratuito (RNF-15).

| Software | Propósito | Documentação |
|---|---|---|
| Node.js e Express | Execução do backend e API REST (RNF-01, RNF-09) | https://nodejs.org/docs/latest/api/ · https://expressjs.com |
| Mongoose | Esquemas e validações dos dados (RNF-02) | https://mongoosejs.com/docs/ |
| bcrypt e jsonwebtoken | Palavras-passe cifradas e tokens de sessão (RNF-10, RNF-12) | https://www.npmjs.com/package/bcrypt · https://www.npmjs.com/package/jsonwebtoken |
| Angular | Interface com o utilizador (RNF-01, RNF-04) | https://angular.dev |
| Leaflet e OpenStreetMap | Mapas no perfil e nas estatísticas | https://leafletjs.com/reference.html |
| MongoDB | Base de dados, principal e de reserva | https://www.mongodb.com/docs/manual/ |
| HAProxy | Balanceadores de carga em ativo-passivo | https://docs.haproxy.org |
| Nginx | Servir o frontend nos servidores aplicacionais | https://nginx.org/en/docs/ |
| Ubuntu Server | Sistema operativo das máquinas virtuais | https://ubuntu.com/server/docs |
| GCP, AWS ou Azure | Máquinas virtuais e IP estático **[A PREENCHER: plataforma escolhida]** | https://cloud.google.com/compute/docs · https://docs.aws.amazon.com/ec2/ · https://learn.microsoft.com/azure/virtual-machines/ |
| Let's Encrypt e Certbot | Certificado TLS para o HTTPS | https://letsencrypt.org/docs/ · https://certbot.eff.org |
| Nominatim | Moradas em coordenadas | https://nominatim.org/release-docs/latest/api/Search/ |
| Stripe e PayPal | Pagamentos online | https://docs.stripe.com · https://developer.paypal.com/docs/ |
| Cloudinary e Cover Art Archive | Guardar e sugerir as capas | https://cloudinary.com/documentation · https://musicbrainz.org/doc/Cover_Art_Archive/API |
| API do MusicBrainz | Importar faixas e canções | https://musicbrainz.org/doc/MusicBrainz_API |

O enunciado da componente de Redes de PTIR proíbe serviços geridos que deem balanceamento, escalabilidade ou tolerância a falhas automáticos. Por isso, ao contrário da referência usada na Etapa 1, a base de dados de produção não é o MongoDB Atlas: é instalada pela equipa em duas máquinas virtuais. Os componentes construídos de raiz (classe *new* da T06) são o frontend, o backend, os esquemas de dados, o importador de faixas, os 10 scripts de infraestrutura e os testes.

## API REST

A API foi descrita segundo a especificação **OpenAPI 3.0**, no ficheiro `api.yaml`, e validada com o `openapi-spec-validator`. Tem 31 recursos e 46 operações, agrupados pelos mesmos packages dos casos de uso da Etapa 1. A lista completa está no Anexo A.

Decisões principais, seguindo as boas práticas indicadas na RNF-09:
- **Recursos com nomes no plural e sem verbos** (`/albuns`, `/pedidos`). As operações exprimem-se pelos métodos HTTP: GET consulta, POST cria, PUT substitui, PATCH altera parte, DELETE remove.
- **Dados do próprio utilizador em `/utilizadores/eu`:** coleção, listas, carrinho e notificações. O backend sabe quem é o utilizador pelo token, sem o identificador no caminho.
- **Sessão por token** (`Authorization: Bearer`), exceto para criar conta, iniciar sessão e os avisos dos serviços de pagamento (RNF-12). O backend não guarda estado da sessão, o que permite acrescentar servidores (RNF-10).
- **Validações iguais às restrições de integridade:** por exemplo, o EAN-13 tem 13 dígitos (RI-13) e o preço é positivo com duas casas decimais (RI-16).
- **Códigos de estado HTTP coerentes:** 200 e 201 para sucesso, 204 sem conteúdo, 400 para dados inválidos (com o campo e o motivo, como pedem a US1 g e a US22 i), 401 sem sessão, 403 sem permissão (operações só do gestor), 404 recurso inexistente e 409 conflito com uma restrição (por exemplo, versão já na coleção, RI-41).
- **Pagamento em dois passos:** POST `/pagamentos` cria o pagamento e devolve o endereço da página do serviço. O serviço avisa o resultado em `/webhooks/{servico}`, que emite a fatura e atualiza a coleção e o stock (US28 c, d, f).

# Processo

O desenvolvimento segue o **Scrum**, como pede o enunciado, com **três sprints de cerca de um mês** e uma demonstração ao cliente no fim de cada um: final de março, de abril e de maio. A componente de Redes acrescenta **quatro reuniões de avaliação**: a primeira avalia o design e as outras três o progresso.

**[A PREENCHER: datas de início e fim de cada sprint e das reuniões de Redes, a confirmar no calendário de PTIR]**

**Tabela 7 — Eventos de cada sprint**

| Evento | Objetivo | Item do backlog |
|---|---|---|
| Sprint planning | Escolher os itens do sprint a partir do product backlog ordenado | GES.02 |
| Reuniões de acompanhamento | Coordenação da equipa, 2 vezes por semana | GES.03 |
| Sprint review | Demonstração ao cliente (M.1, M.2, M.3) e revisão técnica | GES.04 |
| Retrospetiva | Melhorar o processo e rever os riscos | GES.05 |
| Acompanhamento | Atualizar o Gantt e calcular a earned value analysis (T07) | GES.06 |
| Revisão de estimativas | Novo planning poker com a experiência do sprint (nota 21 do enunciado) | GES.07 |

O plano partilhado **PLANO-PTIR-12** no Microsoft Planner é a ferramenta de acompanhamento, organizado como recomenda a aula prática do Planner:
- buckets `Backlog`, `Sprint 1`, `Sprint 2`, `Sprint 3` e `Feito`;
- etiquetas por pacote de trabalho;
- nomes de tarefas começados pelo identificador do backlog (`US.22`, `RED.12`);
- as subtarefas de cada user story na checklist.

# Projeto

## Backlog e WBS

O product backlog tem **84 itens**:
- as 29 user stories do enunciado;
- 8 tarefas de gestão;
- 11 de infraestrutura e arquitetura;
- 6 de integração com serviços externos;
- 8 de qualidade e requisitos não funcionais;
- 22 da componente de Redes.

Estes itens foram organizados numa **Work Breakdown Structure** com 11 pacotes de trabalho, seguindo os critérios da T07: coerência, coesão e continuidade, separados em pacotes horizontais (gestão) e de conteúdo (produto).

**Tabela 8 — Pacotes de trabalho**

| Pacote | Tipo | Itens | Resultado |
|---|---|---|---|
| WP.1 Gestão do projeto | Horizontal | GES.01 a GES.08 | Planner e Gantt atualizados, reviews |
| WP.2 Infraestrutura e arquitetura | Conteúdo | INF.01 a INF.11 | Repositório, esqueleto, base de dados, autenticação, integração contínua |
| WP.3 Conta e perfil | Conteúdo | US1 a US4, US19 | Registo, sessão, perfil e dashboard |
| WP.4 Catálogo de música | Conteúdo | US5 a US9, US20 a US23 | Catálogo navegável e gerido |
| WP.5 Coleção e listas | Conteúdo | US10, US11, US15 a US18 | Coleção e listas |
| WP.6 Pedidos de nova versão | Conteúdo | US12 a US14, US24 | Fluxo completo do pedido |
| WP.7 Loja | Conteúdo | US25 a US28 | Compra com fatura |
| WP.8 Estatísticas | Conteúdo | US29 | Estatísticas com mapa |
| WP.9 Integrações externas | Conteúdo | INT.01 a INT.06 | Serviços integrados em modo de teste |
| WP.10 Qualidade, testes e RNF | Conteúdo | QUA.01, QUA.02, QUA.05 a QUA.09, QUA.11 | Testes, SUS, backup, privacidade |
| WP.11 Tecnologias de Redes | Conteúdo | RED.01 a RED.22 | Relatório de design, infraestrutura distribuída, scripts, testes de carga e de vulnerabilidades |

Os pacotes WP.3 a WP.8 correspondem aos packages de casos de uso da Etapa 1. As integrações externas têm um pacote próprio porque são as tarefas tecnicamente mais arriscadas e servem vários pacotes. O pacote de Redes decompõe o enunciado da componente de Redes de PTIR nas suas quatro fases: conceção, arquitetura distribuída, segurança, e automação e testes.

Cada user story foi decomposta em quatro subtarefas (dados e API, ecrã, serviço externo e testes), como pede a estimação por decomposição em projetos ágeis (T06). A decomposição está no Anexo B. As dependências principais entre itens são as da Tabela 9 e foram passadas para o mapa de Gantt.

**Tabela 9 — Dependências principais**

| Cadeia | Porquê |
|---|---|
| INF.01 → INF.02, INF.03 → INF.04 → INF.06 | Sem repositório, esqueleto, base de dados e autenticação não há funcionalidades |
| US20 → US22 → US9 → US10, US17, US25, US26 | Um álbum precisa de artista; os botões da coleção, das listas, do stock e do carrinho estão na página do álbum |
| US26 → US27 → US28 → US29 | Carrinho antes do pagamento; as estatísticas usam as vendas |
| US12 → US24 → US14 | A notificação só existe depois de o gestor responder |
| RED.01 a RED.07 → M.R1 → RED.08 a RED.12 → RED.17 a RED.19 → RED.22 | Design de Redes avaliado antes de criar infraestrutura; scripts usados na demonstração final |
| Maioria das US → QUA.06 → QUA.07 | Testes com utilizadores com a aplicação quase completa, com tempo para a iteração de melhoria |

## Esforço disponível

O esforço disponível foi calculado como no exercício 1 do TP5: a duração vezes a dedicação de cada pessoa, aqui em horas por semana. Nas semanas de avaliação de outras cadeiras, cada pessoa indicou quanto reduz. Para o planeamento usa-se 85% do esforço disponível: a margem de 15% é a mitigação do risco R01 (estimativas baixas).

**[A PREENCHER NA REUNIÃO: folha "Disponibilidade" do livro `estimacao-etapa2.xlsx`]**

**Tabela 10 — Esforço disponível**

| Sprint | Disponível (h) | Para planear (h) | Pessoa.mês |
|---|---|---|---|
| S1 | | | |
| S2 | | | |
| S3 | | | |
| **Total** | | | |

## Story points

Os story points das 29 user stories resultaram de uma sessão de **planning poker** (T06):
- cartas da sequência de Fibonacci (1, 2, 3, 5, 8, 13, 21 e café);
- todos mostram a carta ao mesmo tempo;
- quem dá o valor mais baixo e quem dá o mais alto justificam-se, e faz-se nova ronda até haver consenso.

A US15 (criar lista) foi usada como referência de 2 pontos.

**[A PREENCHER NA REUNIÃO: data da sessão, Tabela 11 com as rondas e os story points finais, folha "Planning poker" do livro]**

**Tabela 11 — Story points das user stories**

| US | User story | Rondas | SP |
|---|---|---|---|
| US1 | Criar conta | | |
| … | … | | |
| **Total** | | | |

## Esforço necessário

O esforço de cada item foi estimado por **decomposição** (T06):
- para cada subtarefa, três valores: otimista (O), provável (M) e pessimista (P);
- esforço esperado = (O + 4 × M + P) ÷ 6;
- esforço de uma user story = soma das suas subtarefas.

**[A PREENCHER: totais por pacote de trabalho, folha "Esforço" do livro]**

**Tabela 12 — Esforço necessário por pacote de trabalho**

| Pacote | Esforço esperado (h) |
|---|---|
| WP.1 a WP.11 | |
| **Total** | |

**Estimativa de controlo.** Para verificar a estimativa por decomposição, fez-se uma segunda estimativa com os modelos da T05 e da T06:
- **Pontos de função:** 285 pontos não ajustados e um fator de ajuste de 1,06 dão **302 pontos de função**.
- **Linhas de código:** com 54 a 72 linhas de JavaScript por ponto de função, são cerca de **16 300 a 21 800 linhas**.
- **COCOMO básico (modo orgânico):** prevê 45 a 61 pessoa.mês, o que é impossível num semestre. A própria T06 mostra que, num projeto real de PTI de 2018/19, o COCOMO sobrestimou o esforço cerca de 5,6 vezes.
- **Produtividade histórica desse projeto (2 050 linhas por pessoa.mês):** o software exige **1 400 a 1 870 horas**, ou seja, 280 a 375 horas por pessoa. As tarefas de Redes e de gestão vêm por cima.

**[A PREENCHER: comparação entre a estimativa por decomposição e a de controlo, e com o esforço disponível. O enunciado exige esforço necessário ≤ esforço disponível]**

## Distribuição pelos sprints

Os itens foram distribuídos pelos três sprints:
- respeitando as dependências da Tabela 9;
- de forma a cada sprint ser fazível (esforço planeado ≤ esforço disponível para planear);
- com os sprints equilibrados.

A ordem de partida foi a do backlog, por níveis: fundações; núcleo do produto; fluxos completos; fecho.

**Tabela 13 — Proposta de distribuição pelos sprints (por dependências)**

| Sprint | Itens | Foco | Itens do backlog |
|---|---|---|---|
| S1 | 26 | Fundações: repositório, esqueleto, base de dados, autenticação, integração contínua; sessão, dashboard e catálogo mínimo (registar artista e álbum, capa); relatório de design de Redes, cloud, redes, domínio e SSH | US.02, US.19, US.20, US.22, GES.01, INF.01, INF.02, INF.03, INF.04, INF.05, INF.06, INF.07, INF.08, INF.11, INT.05, RED.01, RED.02, RED.03, RED.04, RED.05, RED.06, RED.07, RED.08, RED.09, RED.13, RED.16 |
| S2 | 26 | Núcleo do produto e pedidos: conta e perfil com mapa, pesquisa, páginas de artista e álbum, coleção, stock e carrinho, pedidos e notificações; importação de faixas; servidores, bases de dados, balanceadores, HTTPS e firewall; preparar testes com utilizadores; deploy automático | US.01, US.03, US.04, US.05, US.06, US.08, US.09, US.10, US.11, US.12, US.13, US.14, US.24, US.25, US.26, US.27, INF.09, INT.01, INT.02, INT.06, QUA.05, RED.10, RED.11, RED.12, RED.14, RED.15 |
| S3 | 21 | Fluxos finais: pagamento (Stripe e PayPal), favorito, listas, alteração de artista e álbum, estatísticas; scripts de Redes; testes com utilizadores e melhoria; backup, privacidade; testes de carga e de vulnerabilidades; demonstração final | US.07, US.15, US.16, US.17, US.18, US.21, US.23, US.28, US.29, INT.03, INT.04, QUA.06, QUA.07, QUA.08, QUA.09, RED.17, RED.18, RED.19, RED.20, RED.21, RED.22 |
| Todos | 11 | Contínuos: planeamento, reuniões, reviews, retrospetivas, acompanhamento, re-estimação, OpenAPI, testes automáticos e à API, verificação em telemóvel | GES.02, GES.03, GES.04, GES.05, GES.06, GES.07, GES.08, INF.10, QUA.01, QUA.02, QUA.11 |

Os itens contínuos repetem-se em todos os sprints e o seu esforço divide-se pelos três. A proposta respeita as dependências da Tabela 9; o equilíbrio do esforço ajusta-se quando houver estimativas.

**[A PREENCHER: Tabela 14, folha "Sprints" do livro]**

**Tabela 14 — Equilíbrio dos sprints**

| Sprint | Para planear (h) | Planeado (h) | Ocupação | Story points |
|---|---|---|---|---|
| S1 | | | | |
| S2 | | | | |
| S3 | | | | |

## Mapa de Gantt e esforço por pessoa

O mapa de Gantt foi feito no Microsoft Project, como na aula prática de planeamento, a partir da folha "MS Project" do livro de estimação. Essa folha tem o trabalho, as predecessoras e o recurso de cada item. O Gantt mostra:
- os três sprints;
- as milestones das demonstrações (M.1 a M.3) e das reuniões de Redes (M.R1 a M.R4);
- as pessoas atribuídas a cada tarefa e as dependências;
- o **caminho crítico** (T07).

**[A PREENCHER: figura do Gantt e Tabela 15, folha "Pessoas" do livro]**

**Tabela 15 — Esforço total previsto por pessoa**

| Pessoa | S1 (h) | S2 (h) | S3 (h) | Total (h) |
|---|---|---|---|---|
| Pessoa A | | | | |
| Pessoa B | | | | |
| Pessoa C | | | | |
| Pessoa D | | | | |
| Pessoa E | | | | |

# Gestão de risco

A gestão de risco segue a aproximação **proativa** da T08: identificar os riscos antes do trabalho técnico, analisar a sua probabilidade e o seu impacto, ordená-los e preparar um plano para os mais importantes.

Os riscos foram identificados com a checklist de categorias da T08:
- dimensão do produto (DI);
- impacto do negócio (IN);
- caraterísticas dos clientes (CC);
- definição do processo (DF);
- ambiente de desenvolvimento (AD);
- tecnologia a construir (TC);
- experiência da equipa (EX).

A probabilidade está em percentagem. O impacto está na escala 1 = catastrófico, 2 = crítico, 3 = marginal, 4 = negligenciável: foi estimado nas quatro componentes da T08 (desempenho, suporte, custo e planeamento), e o impacto do risco é a média.

A tabela está ordenada por probabilidade e, dentro da mesma probabilidade, pelo impacto mais grave, porque a T08 diz que a probabilidade deve pesar mais.

**Tabela 16 — Tabela de riscos**

| # | Risco | Cat. | Prob. | D | S | C | P | Impacto |
|---|---|---|---|---|---|---|---|---|
| R01 | Estimativas de esforço demasiado baixas, por falta de dados históricos | DI | 70% | 3 | 3 | 2 | 1 | 2,25 |
| R02 | Pouca experiência com a stack MEAN | EX | 60% | 2 | 2 | 3 | 2 | 2,25 |
| R03 | Pouca experiência com infraestrutura distribuída | EX | 60% | 2 | 3 | 3 | 1 | 2,25 |
| R04 | O cliente altera os requisitos durante o projeto | CC | 50% | 2 | 3 | 3 | 2 | 2,50 |
| R05 | Testes com utilizadores no fim, sem tempo para melhorar | DF | 50% | 2 | 3 | 4 | 2 | 2,75 |
| R06 | Membros indisponíveis em épocas de avaliação ou por doença | EX | 50% | 3 | 4 | 3 | 2 | 3,00 |
| R07 | Falha na passagem da base de dados de reserva a principal | TC | 40% | 1 | 3 | 3 | 2 | 2,25 |
| R08 | Integração do pagamento mais difícil do que previsto | TC | 40% | 1 | 3 | 3 | 2 | 2,25 |
| R09 | Frontend e backend desencontrados por API mal definida | DF | 40% | 3 | 2 | 3 | 2 | 2,50 |
| | **— linha de corte —** | | | | | | | |
| R10 | Responsabilidades mal definidas | DF | 30% | 3 | 3 | 3 | 2 | 2,75 |
| R11 | Custo da cloud acima dos créditos gratuitos | IN | 30% | 3 | 4 | 1 | 3 | 2,75 |
| R12 | Vulnerabilidades descobertas só no fim | TC | 30% | 2 | 2 | 4 | 3 | 2,75 |
| R13 | Limites e indisponibilidade dos serviços externos | TC | 30% | 3 | 3 | 4 | 3 | 3,25 |
| R14 | Dificuldade em obter domínio e certificado TLS | AD | 30% | 3 | 4 | 3 | 3 | 3,25 |
| R15 | Perda de código ou de dados | AD | 20% | 2 | 3 | 4 | 2 | 2,75 |
| R16 | Prazo das demonstrações antecipado | IN | 10% | 3 | 4 | 4 | 1 | 3,00 |

**Linha de corte.** A T08 propõe o princípio de Pareto: 80% do risco vem de 20% dos riscos. Calculou-se a exposição de cada risco como probabilidade × (5 − impacto). Os 9 riscos com probabilidade igual ou superior a 40% concentram cerca de **76% da exposição total**, por isso ficam acima da linha e têm plano RMMM.

**Tabela 17 — Plano RMMM dos riscos acima da linha de corte**

| # | Mitigação | Monitorização | Gestão (contingência) |
|---|---|---|---|
| R01 | Decomposição com três valores; estimativa de controlo; 15% de margem nos sprints; itens próprios para teste e integração | Esforço planeado vs. realizado (timesheets); SPI e CPI em cada sprint | Re-estimar entre sprints; adiar as user stories de menor prioridade |
| R02 | Formação no início do sprint 1; esqueleto feito em conjunto; revisão de código | Pull requests parados; tarefas acima da estimativa pessimista | Trabalho em pares; ajuda dos docentes |
| R03 | Relatório de design de Redes logo no início; guiões indicados; versão mínima antes da redundância | Avaliações de Redes; scripts que ainda não correm | Duas pessoas nas tarefas atrasadas; containers |
| R04 | Sprint backlog fixo durante o sprint; demonstrações frequentes; suposições documentadas | Novas versões do enunciado; pedidos nas demonstrações | Estimar a alteração e retirar itens de esforço equivalente |
| R05 | Preparar os testes no sprint 2 e fazê-los no início do sprint 3 | Data no Gantt; user stories concluídas | Testar com o que existir; corrigir só os problemas graves |
| R06 | Datas de avaliação no planeamento; reserva para cada papel; documentação no repositório | Reuniões de acompanhamento; horas abaixo do previsto | A reserva assume; o product owner adia itens |
| R07 | Prova de conceito da replicação no sprint 1; ensaio cedo de `promote_db_backup.sh` | Ensaio do cenário de falha em cada sprint | Restaurar do backup; rever a configuração |
| R08 | Prova de conceito do Stripe com webhook antes da US28 | Testes do pagamento na integração contínua | Entregar primeiro só o Stripe; PayPal no sprint seguinte |
| R09 | Especificação OpenAPI como contrato; testes à API | Erros nos testes de fumo diários | Revisão técnica conjunta entre frontend e backend |

**Avaliação de custos.** As medidas custam sobretudo tempo da equipa (formação, provas de conceito, ensaios, margem de 15%), que entra no esforço necessário. Não há custos em dinheiro, porque se usam os modos de teste dos pagamentos e os créditos de estudante da cloud. Nenhum risco, se se concretizar, põe em causa a viabilidade do projeto.

A tabela é revista na revisão de gestão do fim de cada sprint: probabilidades atualizadas, riscos novos acrescentados e os ultrapassados retirados.

# Anexo A — Endpoints da API REST

**Tabela 18 — Endpoints da API**

| Package | Método | Caminho | Operação | Só gestor |
|---|---|---|---|---|
| Conta e perfil | POST | `/sessoes` | Iniciar sessão (US2) | |
| Conta e perfil | POST | `/utilizadores` | Criar conta (US1) | |
| Conta e perfil | GET | `/utilizadores/eu` | Visualizar o perfil (US3) | |
| Conta e perfil | PUT | `/utilizadores/eu` | Gerir o perfil (US4) | |
| Conta e perfil | DELETE | `/utilizadores/eu` | Eliminar a conta e os dados pessoais (RNF-16) | |
| Catálogo | PUT | `/utilizadores/eu/artista-favorito` | Adicionar artista como favorito (US7) | |
| Catálogo | DELETE | `/utilizadores/eu/artista-favorito` | Deixar de ter o artista como favorito (US7 d) | |
| Catálogo | GET | `/artistas` | Pesquisar artistas (US5) | |
| Catálogo | POST | `/artistas` | Registar artista (US20) | Sim |
| Catálogo | GET | `/artistas/{isni}` | Visualizar página de artista (US6) | |
| Catálogo | PUT | `/artistas/{isni}` | Gerir dados de um artista (US21) | Sim |
| Catálogo | GET | `/artistas/{isni}/albuns` | Lista completa dos álbuns do artista (US6 b, c) | |
| Catálogo | GET | `/albuns` | Pesquisar álbuns (US8) | |
| Catálogo | POST | `/albuns` | Registar novo álbum com a primeira versão (US22 a) | Sim |
| Catálogo | GET | `/albuns/{mbid}` | Visualizar página de álbum (US9) | |
| Catálogo | PUT | `/albuns/{mbid}` | Gerir dados de um álbum (US23) | Sim |
| Catálogo | POST | `/albuns/{mbid}/versoes` | Registar versão de um álbum existente (US22 b) | Sim |
| Catálogo | GET | `/albuns/{mbid}/capa` | Sugestão de capa do Cover Art Archive (US22 f) | Sim |
| Catálogo | PUT | `/albuns/{mbid}/capa` | Associar imagem de capa (US22 f, US23 a) | Sim |
| Catálogo | POST | `/albuns/{mbid}/faixas/importacao` | Importar faixas do MusicBrainz (nota 12) | Sim |
| Catálogo | PUT | `/versoes/{ean13}` | Alterar os dados de uma versão (US23) | Sim |
| Coleção e listas | GET | `/utilizadores/eu/colecao` | Visualizar a coleção (US11) | |
| Coleção e listas | POST | `/utilizadores/eu/colecao` | Adicionar versão à coleção (US10) | |
| Coleção e listas | DELETE | `/utilizadores/eu/colecao/{ean13}` | Remover versão da coleção (US11 f) | |
| Coleção e listas | GET | `/utilizadores/eu/listas` | Visualizar as listas (US16) | |
| Coleção e listas | POST | `/utilizadores/eu/listas` | Criar lista personalizada (US15) | |
| Coleção e listas | GET | `/utilizadores/eu/listas/{idLista}` | Visualizar o conteúdo de uma lista (US18) | |
| Coleção e listas | DELETE | `/utilizadores/eu/listas/{idLista}` | Remover uma lista (US16 e) | |
| Coleção e listas | POST | `/utilizadores/eu/listas/{idLista}/albuns` | Adicionar álbum a uma lista (US17) | |
| Coleção e listas | DELETE | `/utilizadores/eu/listas/{idLista}/albuns/{mbid}` | Remover álbum de uma lista (US18 e) | |
| Pedidos | GET | `/pedidos` | Listar pedidos (US13; US24 para o gestor) | |
| Pedidos | POST | `/pedidos` | Submeter pedido de nova versão (US12) | |
| Pedidos | GET | `/pedidos/{idPedido}` | Ver os dados de um pedido (US24 a) | |
| Pedidos | PATCH | `/pedidos/{idPedido}` | Responder a um pedido (US24 c, d) | Sim |
| Pedidos | GET | `/utilizadores/eu/notificacoes` | Ver as notificações (US14) | |
| Pedidos | PATCH | `/utilizadores/eu/notificacoes/{idNotificacao}` | Marcar notificação como lida (RI-50) | |
| Loja | PATCH | `/versoes/{ean13}/disponibilidade` | Aumentar ou diminuir unidades (US25) | Sim |
| Loja | GET | `/utilizadores/eu/carrinho` | Visualizar o carrinho (US27) | |
| Loja | POST | `/utilizadores/eu/carrinho` | Colocar versão no carrinho (US26) | |
| Loja | DELETE | `/utilizadores/eu/carrinho/{ean13}` | Remover álbum do carrinho (US27 d) | |
| Loja | POST | `/pagamentos` | Iniciar o pagamento do carrinho (US28 a, b) | |
| Loja | GET | `/pagamentos/{idPagamento}` | Consultar o resultado do pagamento (US28 c, d, g) | |
| Loja | DELETE | `/pagamentos/{idPagamento}` | Cancelar o pagamento (US28 g) | |
| Loja | POST | `/webhooks/{servico}` | Aviso do serviço de pagamentos (US28 c) | |
| Loja | GET | `/faturas/{numero}` | Ver uma fatura (US28 d) | |
| Estatísticas | GET | `/estatisticas` | Visualizar estatísticas da loja (US29) | Sim |

# Anexo B — Decomposição das user stories

Cada user story divide-se nas subtarefas `.1` dados e API, `.2` ecrã, `.3` serviço externo (quando existe) e `.4` testes. A tabela completa, com o conteúdo de cada subtarefa, está na Tabela 6 do documento de backlog (`etapa2/backlog/backlog-wbs.md`).

**[A DECIDIR: copiar aqui a Tabela 6 do backlog, ou deixar só a referência]**

# Referências

- Enunciado do projeto PGP 2026/27, versão de 4 de novembro de 2026.
- Enunciado da componente de Redes de PTIR 2025/26 (v2.0).
- Aulas teóricas T05 (Planeamento), T06 (Estimação), T07 (Calendarização), T08 (Gestão de Riscos), T09 (Gestão de Equipas) e T10 (Testes), e aulas práticas de Planner, Microsoft Project, Métricas, Estimação e Riscos de PGP 2026/27.
- Pressman, R. S., e Maxim, B. R. (2014). *Software Engineering: A Practitioner's Approach* (8.ª edição). McGraw-Hill. Capítulos 30 a 35.
- OpenAPI Initiative. OpenAPI Specification 3.0. https://swagger.io/specification/
- Scrum Guide. https://scrumguides.org/scrum-guide.html
