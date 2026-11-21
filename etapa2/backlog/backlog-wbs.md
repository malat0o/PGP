# Product backlog e WBS

Este documento é a base do planeamento da Etapa 2. A partir dele faz-se o planning poker, a estimação do esforço, a distribuição pelos sprints e o mapa de Gantt.

Segue os métodos das aulas:
- **T07 (Calendarização):** Work Breakdown Structure (WBS) e pacotes de trabalho coerentes, coesos e contínuos, separados em horizontais (gestão) e de conteúdo (produto).
- **T06 (Estimação):** em projetos ágeis, cada user story é decomposta em tarefas, e a estimativa da user story é a soma das estimativas das tarefas.
- **TP do Planner:** identificadores curtos e multinível (`US.01`, `US.01.1`), que permitem agrupar e filtrar as tarefas.

As colunas de story points e de esforço estão vazias de propósito. São preenchidas pela equipa no planning poker e na estimação.

## 1. Convenções

**Tabela 1 — Identificadores do backlog**

| Prefixo | Significado | Exemplo |
|---|---|---|
| `WP.n` | Pacote de trabalho da WBS | `WP.4` Catálogo de música |
| `US.xx` | User story do enunciado | `US.22` Registar álbum |
| `US.xx.y` | Subtarefa de uma user story | `US.22.3` Formulário de registo |
| `GES.xx` | Tarefa de gestão do projeto | `GES.04` Sprint review |
| `INF.xx` | Infraestrutura e arquitetura | `INF.06` Autenticação |
| `INT.xx` | Integração com um serviço externo | `INT.03` Stripe |
| `QUA.xx` | Qualidade, testes e requisitos não funcionais | `QUA.06` Testes com utilizadores |
| `RED.xx` | Atividades de Tecnologias de Redes de PTIR | `RED.12` Balanceadores de carga |
| `M.n` | Milestone | `M.1` Demo do sprint 1 |

## 2. WBS

O projeto divide-se em 11 pacotes de trabalho. Os pacotes WP.3 a WP.8 correspondem aos **packages de casos de uso da Etapa 1**. Assim, cada pacote junta user stories com o mesmo objetivo (coerência). As integrações externas estão num pacote próprio porque são as tarefas tecnicamente mais arriscadas, servem vários pacotes e convém fazê-las cedo.

```
0  Aplicação web de gestão de coleções de álbuns (PTIR)
├── WP.1  Gestão do projeto ............... horizontal
├── WP.2  Infraestrutura e arquitetura .... conteúdo
├── WP.3  Conta e perfil .................. conteúdo (UC-01 a UC-05)
├── WP.4  Catálogo de música .............. conteúdo (UC-06 a UC-09, UC-17, UC-18)
├── WP.5  Coleção e listas ................ conteúdo (UC-10 a UC-12)
├── WP.6  Pedidos de nova versão .......... conteúdo (UC-13, UC-14, UC-19)
├── WP.7  Loja ............................ conteúdo (UC-15, UC-16, UC-20)
├── WP.8  Estatísticas .................... conteúdo (UC-21)
├── WP.9  Integrações externas ............ conteúdo
├── WP.10 Qualidade, testes e RNF ......... conteúdo
└── WP.11 Tecnologias de Redes ............ conteúdo (enunciado da componente Redes de PTIR)
    ├── Conceção: relatório de design
    ├── Arquitetura distribuída: balanceadores, servidores, bases de dados, redes
    ├── Segurança: TLS, domínio, firewall, SSH
    └── Automação e testes: scripts, testes de carga e de vulnerabilidades

Milestones: M.1 demo do sprint 1 (final de março)
            M.2 demo do sprint 2 (final de abril)
            M.3 demo do sprint 3 e entrega final (final de maio)
            M.R1 a M.R4 reuniões de avaliação de Redes (design; progresso; datas a confirmar)
```

**Tabela 2 — Pacotes de trabalho**

| Pacote | Tipo | Objetivo | Itens | Resultado | Depende de |
|---|---|---|---|---|---|
| WP.1 Gestão do projeto | Horizontal | Planear, acompanhar e rever cada sprint | GES.01 a GES.08 | Planner atualizado, Gantt revisto, atas das reviews | — |
| WP.2 Infraestrutura e arquitetura | Conteúdo | Base técnica em que assentam todas as funcionalidades | INF.01 a INF.11 | Repositório, frontend e backend a correr em produção, base de dados, autenticação | — |
| WP.3 Conta e perfil | Conteúdo | Criar conta, iniciar sessão, perfil e dashboard | US.01 a US.04, US.19 | Utilizador consegue registar-se, entrar e gerir o perfil | WP.2, INT.01, INT.02 |
| WP.4 Catálogo de música | Conteúdo | Registar e consultar artistas, álbuns e versões | US.05 a US.09, US.20 a US.23 | Catálogo navegável e gerido pelo gestor | WP.2, INT.05, INT.06 |
| WP.5 Coleção e listas | Conteúdo | Coleção pessoal e listas personalizadas | US.10, US.11, US.15 a US.18 | Utilizador gere a coleção e as listas | WP.4 |
| WP.6 Pedidos de nova versão | Conteúdo | Pedido do utilizador, resposta do gestor e notificação | US.12 a US.14, US.24 | Fluxo completo do pedido | WP.4 |
| WP.7 Loja | Conteúdo | Stock, carrinho e pagamento | US.25 a US.28 | Compra completa com fatura | WP.4, WP.5, INT.03, INT.04 |
| WP.8 Estatísticas | Conteúdo | Estatísticas para o gestor | US.29 | Página de estatísticas com mapa | WP.5, WP.7, INT.02 |
| WP.9 Integrações externas | Conteúdo | Ligar os serviços escolhidos na Etapa 1 | INT.01 a INT.06 | Cada serviço integrado e testado em modo de teste | WP.2 |
| WP.10 Qualidade, testes e RNF | Conteúdo | Cumprir e comprovar os requisitos não funcionais | QUA.01, QUA.02, QUA.05 a QUA.09, QUA.11 | Testes automáticos, testes com utilizadores, SUS, backup, privacidade | WP.2 a WP.8 |
| WP.11 Tecnologias de Redes | Conteúdo | Pôr a aplicação a correr num sistema distribuído redundante e seguro, em máquinas virtuais | RED.01 a RED.22 | Relatório de design, infraestrutura em produção, 10 scripts, testes de carga e de vulnerabilidades | WP.2 |

## 3. Product backlog: user stories

**Tabela 3 — User stories do backlog**

| ID | User story | Pacote | Caso de uso | Depende de | SP | Esforço (h) |
|---|---|---|---|---|---|---|
| US.01 | Criar conta | WP.3 | UC-01 | INF.06, INT.01 | | |
| US.02 | Iniciar sessão | WP.3 | UC-02 | INF.06 | | |
| US.03 | Visualizar perfil | WP.3 | UC-04 | US.01, INT.02 | | |
| US.04 | Gerir perfil | WP.3 | UC-05 | US.03, INT.01 | | |
| US.05 | Pesquisar artistas | WP.4 | UC-06 | US.20 | | |
| US.06 | Visualizar página de artista | WP.4 | UC-07 | US.20, US.22 | | |
| US.07 | Adicionar artista como favorito | WP.4 | UC-08 | US.06 | | |
| US.08 | Pesquisar álbuns | WP.4 | UC-06 | US.22 | | |
| US.09 | Visualizar página de álbum | WP.4 | UC-09 | US.22, INT.06 | | |
| US.10 | Adicionar versão à coleção | WP.5 | UC-10 | US.09 | | |
| US.11 | Visualizar coleção | WP.5 | UC-10 | US.10 | | |
| US.12 | Submeter pedido de nova versão | WP.6 | UC-13 | US.22 | | |
| US.13 | Ver estado dos pedidos | WP.6 | UC-14 | US.12 | | |
| US.14 | Ser notificado da resposta a um pedido | WP.6 | UC-14 | US.24, US.19 | | |
| US.15 | Criar lista personalizada | WP.5 | UC-11 | US.02 | | |
| US.16 | Visualizar listas personalizadas | WP.5 | UC-11 | US.15 | | |
| US.17 | Adicionar álbum a uma lista | WP.5 | UC-12 | US.09, US.15 | | |
| US.18 | Visualizar conteúdo de uma lista | WP.5 | UC-12 | US.17 | | |
| US.19 | Aceder ao dashboard | WP.3 | UC-03 | US.02 | | |
| US.20 | Registar artista | WP.4 | UC-17 | INF.06, INF.07 | | |
| US.21 | Gerir dados de um artista | WP.4 | UC-17 | US.20 | | |
| US.22 | Registar álbum ou versão | WP.4 | UC-18 | US.20, INT.05 | | |
| US.23 | Gerir dados de um álbum | WP.4 | UC-18 | US.22 | | |
| US.24 | Responder a pedido de nova versão | WP.6 | UC-19 | US.12 | | |
| US.25 | Aumentar ou diminuir unidades | WP.7 | UC-20 | US.09 | | |
| US.26 | Colocar álbum no carrinho | WP.7 | UC-15 | US.09, US.25 | | |
| US.27 | Visualizar carrinho | WP.7 | UC-15 | US.26 | | |
| US.28 | Pagar o carrinho | WP.7 | UC-16 | US.27, US.10, INT.03, INT.04 | | |
| US.29 | Visualizar estatísticas | WP.8 | UC-21 | US.11, US.28, INT.02 | | |

## 4. Product backlog: tarefas que não são user stories

O enunciado pede que o backlog inclua "todo um leque de tarefas necessárias à execução do projeto", não só as user stories. A Tabela 4 lista essas tarefas e o requisito que as justifica.

**Tabela 4 — Tarefas técnicas, de gestão e de qualidade**

| ID | Tarefa | Pacote | Origem | Depende de | Esforço (h) |
|---|---|---|---|---|---|
| GES.01 | Configurar o Planner: buckets (Backlog, Sprint 1 a 3, Em curso, Feito) e etiquetas | WP.1 | TP do Planner | — | |
| GES.02 | Sprint planning (uma por sprint) | WP.1 | Scrum | GES.01 | |
| GES.03 | Reuniões de acompanhamento da equipa (contínuo) | WP.1 | Scrum, T07 | — | |
| GES.04 | Sprint review com demonstração ao cliente (M.1, M.2, M.3) | WP.1 | Enunciado, secção 1 | Itens do sprint | |
| GES.05 | Retrospetiva do sprint (uma por sprint) | WP.1 | Scrum | GES.04 | |
| GES.06 | Acompanhar o progresso: atualizar o Gantt e calcular a earned value analysis | WP.1 | T07 | GES.02 | |
| GES.07 | Rever estimativas entre sprints (planning poker de ajuste) | WP.1 | Enunciado, nota 21 | GES.05 | |
| GES.08 | Relatórios e entregas de PTIR | WP.1 | A confirmar em PTIR | — | |
| INF.01 | Repositório Git, ramos e regras de pull request; licença de código aberto | WP.2 | RNF-05, RNF-06 | — | |
| INF.02 | Esqueleto do frontend em Angular, com rotas e serviços | WP.2 | RNF-01 | INF.01 | |
| INF.03 | Esqueleto do backend em Express: estrutura da API REST, erros e códigos HTTP | WP.2 | RNF-01, RNF-09 | INF.01 | |
| INF.04 | Base de dados MongoDB para desenvolvimento (local ou em container) e esquemas Mongoose a partir do modelo de classes | WP.2 | Modelo da Etapa 1 | INF.03 | |
| INF.05 | Validações comuns das restrições de integridade (RI-01 a RI-52) | WP.2 | RNF-02 | INF.04 | |
| INF.06 | Autenticação com token e palavras-passe cifradas | WP.2 | RNF-10, RNF-12 | INF.04 | |
| INF.07 | Conta do gestor pré-configurada e dados de teste (seed) | WP.2 | Enunciado, secção 4 | INF.04 | |
| INF.08 | Integração contínua: build e testes automáticos em cada push | WP.2 | RNF-06, RNF-13 | INF.02, INF.03 | |
| INF.09 | Pipeline de lançamento em produção: GitHub Actions que usa os scripts de Redes | WP.2 | RNF-07 | INF.08, RED.17 | |
| INF.10 | Manter a especificação OpenAPI da API atualizada | WP.2 | RNF-09 | INF.03 | |
| INF.11 | Layout base responsivo: navegação, mensagens de sucesso e de erro | WP.2 | RNF-04 | INF.02 | |
| INT.01 | Geocodificação com o Nominatim (1 pedido por segundo, uma vez por morada) | WP.9 | Capítulo 6 da Etapa 1 | INF.03 | |
| INT.02 | Mapas com Leaflet e OpenStreetMap | WP.9 | Capítulo 6 da Etapa 1 | INF.02 | |
| INT.03 | Pagamento com Stripe em modo de teste: checkout e webhook | WP.9 | Capítulo 6 da Etapa 1 | INF.03 | |
| INT.04 | Pagamento com PayPal em modo de teste | WP.9 | Capítulo 6 da Etapa 1 | INT.03 | |
| INT.05 | Capas: sugestão do Cover Art Archive e envio para o Cloudinary | WP.9 | Capítulo 6 da Etapa 1 | INF.03 | |
| INT.06 | Importação de faixas e canções da API do MusicBrainz | WP.9 | Nota 12, capítulo 6 da Etapa 1 | INF.04 | |
| QUA.01 | Política de testes e testes unitários e de integração ao longo do projeto | WP.10 | RNF-13 | INF.08 | |
| QUA.02 | Testes à API | WP.10 | RNF-09 | INF.03 | |
| QUA.05 | Preparar os testes com utilizadores: tarefas, guião e questionário SUS | WP.10 | RNF-03 | — | |
| QUA.06 | Realizar os testes com utilizadores e analisar os resultados SUS | WP.10 | RNF-03 | QUA.05, maioria das US | |
| QUA.07 | Iteração de melhoria da usabilidade | WP.10 | RNF-03 | QUA.06 | |
| QUA.08 | Política de backup e procedimento de restauro | WP.10 | RNF-14 | INF.04 | |
| QUA.09 | Informação sobre tratamento de dados; consulta e eliminação dos dados pessoais | WP.10 | RNF-16 | US.03 | |
| QUA.11 | Verificação em telemóvel dos ecrãs principais | WP.10 | RNF-04 | INF.11 | |

A QUA.09 é a única funcionalidade que não vem de uma user story: a RNF-16 pede que o utilizador possa consultar e eliminar os seus dados pessoais.

Os testes de carga, a análise de vulnerabilidades e a redundância (antes QUA.03, QUA.04 e QUA.10) passaram para o pacote de Redes (RED.20, RED.21 e RED.10 a RED.12), porque o enunciado de Redes os pede com mais detalhe. Assim o mesmo esforço não é contado duas vezes.

## 5. Tecnologias de Redes

O enunciado da componente Redes de PTIR (versão de 2025/26) organiza o trabalho em quatro fases e pede um relatório, uma infraestrutura em máquinas virtuais e 10 scripts. A Tabela 5 decompõe-no em tarefas. A coluna "Peso" é o peso de cada parte na avaliação de Redes, útil para o product owner dar prioridade.

**Tabela 5 — Tarefas de Tecnologias de Redes**

| ID | Tarefa | Fase | Peso | Depende de | Esforço (h) |
|---|---|---|---|---|---|
| RED.01 | Relatório de design: visão geral do sistema (1 página) | Conceção | 3% | — | |
| RED.02 | Relatório de design: 7 requisitos não funcionais (disponibilidade, escalabilidade, desempenho, tolerância a faltas, segurança, operação e manutenção, isolamento de rede), cada um com requisito, métrica e mecanismo | Conceção | 7% | — | |
| RED.03 | Diagrama de sistema: componentes e redes | Conceção | 5% | RED.02 | |
| RED.04 | Estratégia de redundância e tolerância a falhas | Conceção | 2% | RED.03 | |
| RED.05 | Estratégia de escalabilidade (passiva) | Conceção | 2% | RED.03 | |
| RED.06 | Tabela de comunicações entre componentes (portos e protocolos) | Conceção | 2% | RED.03 | |
| RED.07 | Arquitetura de segurança: exposição de serviços, controlo de acesso, comunicação segura, acesso administrativo | Conceção | 4% | RED.03 | |
| RED.08 | Conta e projeto na cloud (GCP, AWS ou Azure) e IP público estático reservado | Arquitetura | — | M.R1 | |
| RED.09 | Redes: rede externa e rede interna | Arquitetura | — | RED.08 | |
| RED.10 | Servidores aplicacionais: pelo menos 2 máquinas virtuais com a aplicação | Arquitetura | 10% | RED.09, INF.03 | |
| RED.11 | Bases de dados: MongoDB principal e de reserva, em máquinas virtuais | Arquitetura | 7,5% | RED.09, INF.04 | |
| RED.12 | Balanceadores de carga: LB1 e LB2 em ativo-passivo (por exemplo, HAProxy) | Arquitetura | 7,5% | RED.10 | |
| RED.13 | Nome de domínio registado e associado ao IP estático | Segurança | 5% | RED.08 | |
| RED.14 | HTTPS com certificado TLS assinado por uma autoridade certificadora (por exemplo, Let's Encrypt) | Segurança | 5% | RED.12, RED.13 | |
| RED.15 | Firewall: regras entre componentes (security groups ou iptables) | Segurança | 10% | RED.09 | |
| RED.16 | Acesso administrativo por SSH com chaves e restrição por IP | Segurança | (em RED.07) | RED.08 | |
| RED.17 | Scripts do servidor aplicacional: `create_app_server.sh`, `kill_app_server.sh` | Automação | 4% | RED.10, RED.12 | |
| RED.18 | Scripts da base de dados: `create_db_primary.sh`, `create_db_backup.sh`, `kill_db_primary.sh`, `promote_db_backup.sh` | Automação | 8% | RED.11 | |
| RED.19 | Scripts dos balanceadores: `create_lb.sh`, `create_lb_backup.sh`, `kill_lb_primary.sh`, `promote_lb_backup.sh` | Automação | 8% | RED.12 | |
| RED.20 | Testes de carga (por exemplo, Locust): tempo de resposta, vários clientes, balanceamento | Testes | 5% | RED.12, maioria das US | |
| RED.21 | Testes de vulnerabilidades (por exemplo, nmap e OWASP ZAP) | Testes | 5% | RED.14, RED.15 | |
| RED.22 | Preparar a demonstração final: lançar servidores, falha da base de dados principal, falha do LB1 | Testes | — | RED.17 a RED.19 | |

Consequências para o resto do planeamento:
- **Base de dados em máquinas virtuais.** O enunciado de Redes proíbe serviços geridos que deem tolerância a falhas de forma automática. Por isso a base de dados de produção não pode ser o MongoDB Atlas, que a Etapa 1 usou como referência para o tamanho dos dados. Em produção fica num par de máquinas virtuais (RED.11) e em desenvolvimento corre localmente (INF.04).
- **Sem PaaS nem Kubernetes.** O lançamento em produção (INF.09) usa os scripts de Redes, e não uma plataforma que faça o deploy sozinha. Pode usar containers.
- **Custo.** São pelo menos 6 máquinas virtuais (2 balanceadores, 2 servidores, 2 bases de dados). Para cumprir a RNF-15, convém usar os créditos de estudante da plataforma escolhida.
- **Reuniões de avaliação de Redes.** São 4 (M.R1 a M.R4): a primeira é sobre o design, as outras mostram o progresso. O relatório de design (RED.01 a RED.07) tem de estar pronto no início do semestre, antes de qualquer máquina virtual.

## 6. Decomposição das user stories

Segundo a técnica de decomposição (T06), cada user story divide-se em subtarefas:
- `.1` dados e API (backend);
- `.2` ecrã (frontend);
- `.3` integração com um serviço externo, quando existe;
- `.4` testes.

A estimativa de esforço da user story é a soma das estimativas das subtarefas. Os nomes dos endpoints são provisórios: ficam definidos no ficheiro OpenAPI.

**Tabela 6 — Decomposição das user stories em subtarefas**

| ID | .1 Dados e API | .2 Ecrã | .3 Externo | .4 Testes |
|---|---|---|---|---|
| US.01 | Criar utilizador: validar RI-18 a RI-24, cifrar a palavra-passe | Formulário com requisitos visíveis e erros junto ao campo (E03) | Geocodificar a morada (INT.01) | Cada validação, conta criada |
| US.02 | Iniciar sessão e devolver o token | Formulário; erro que não revela se o username existe | — | Sucesso e falha |
| US.03 | Devolver os dados do utilizador autenticado | Página de perfil (E04) | Mapa da morada (INT.02) | Com e sem coordenadas |
| US.04 | Alterar dados, pedindo a palavra-passe atual | Formulário preenchido | Geocodificar a nova morada | Palavra-passe errada, validações da US1 |
| US.05 | Sugestões de artistas por nome parcial (até 300 ms) | Campo com sugestões e opção artista/álbum (E05) | — | Correspondência parcial, sem resultados |
| US.06 | Artista com os 5 álbuns mais recentes; lista completa ordenada por ano | Página do artista e página da lista completa | — | Ordenação, ligações |
| US.07 | Marcar e desmarcar o favorito; só um por utilizador | Botão e mensagens na página do artista | — | Já existe outro favorito |
| US.08 | Sugestões de álbuns por título parcial | O mesmo campo da US.05 | — | Correspondência parcial, sem resultados |
| US.09 | Álbum com faixas, versões e disponibilidade na loja | Página do álbum (E01) | Faixas importadas (INT.06) | Esgotado, nunca à venda, designação |
| US.10 | Adicionar versão à coleção (RI-41) | Botão por versão; "✓ Na coleção" inativo | — | Versão repetida |
| US.11 | Coleção ordenável; remover item | Tabela ordenável com ligações (E06) | — | Ordenar por cada campo, remover |
| US.12 | Criar pedido em análise (RI-12, RI-13) | Formulário de novo pedido (E07) | — | EAN inválido, suporte inválido |
| US.13 | Listar pedidos do utilizador, com filtro por estado | Tabela com filtro (E07) | — | Cada estado |
| US.14 | Criar notificação quando o pedido é respondido; listar notificações | Painel de notificações e acesso no dashboard | — | Aceite, recusado |
| US.15 | Criar lista (RI-29, RI-30) | Formulário de nova lista | — | Nome repetido ou inválido |
| US.16 | Listar listas ordenáveis; remover lista | Página das listas; mensagem quando não há listas | — | Ordenar, vazio, remover |
| US.17 | Adicionar álbum a uma lista, sem repetir | Botão "Adicionar a uma lista" (E01) | — | Álbum repetido |
| US.18 | Conteúdo da lista ordenável; remover álbum | Página da lista; mensagem quando está vazia | — | Ordenar, vazio, remover |
| US.19 | — | Dashboard com acesso às funcionalidades (E10) | — | Acessos depois de iniciar sessão |
| US.20 | Criar artista (RI-07, RI-08) | Formulário do gestor | — | ISNI e ano inválidos |
| US.21 | Alterar artista | Formulário preenchido | — | Validações da US20 |
| US.22 | Criar álbum ou versão (RI-01, RI-02, RI-09, RI-12 a RI-16); data automática | Formulário novo álbum / nova versão (E08) | Capa (INT.05) | Validações, compilação sem artista |
| US.23 | Alterar álbum e todas as versões | Formulário preenchido com as versões | Trocar a capa | Validações da US22 |
| US.24 | Aceitar (cria a versão) ou recusar o pedido; notificar o utilizador | Página do pedido para o gestor | — | Aceite cria versão, recusado não |
| US.25 | Alterar unidades; preço e data na primeira vez | Coluna do gestor na página do álbum (E01) | — | Primeira venda, diminuir até zero |
| US.26 | Colocar versão no carrinho (só com unidades) | Botão por versão; contador no topo | — | Versão esgotada |
| US.27 | Carrinho por ordem de inserção; remover | Página do carrinho (E02) | — | Ordem, remover |
| US.28 | Reservar unidades, emitir fatura (RI-27, RI-28), atualizar coleção (RI-52) e stock (RI-17) | Escolha do serviço; mensagens de sucesso e falha (E02) | Stripe e PayPal (INT.03, INT.04) | Pagamento aceite, recusado, versão esgotada a meio |
| US.29 | Três agregações: top colecionadores, mais adicionados, mais vendidos | Página de estatísticas (E09) | Mapa das moradas (INT.02) | Valores com dados de teste |

## 7. Dependências principais

Estas dependências são as que vão para a rede de tarefas e o mapa de Gantt (T07).

**Tabela 7 — Cadeias de dependências**

| Cadeia | Porquê |
|---|---|
| INF.01 → INF.02 e INF.03 → INF.04 → INF.06 | Sem repositório, esqueleto, base de dados e autenticação não há funcionalidades (a RNF-12 exige sessão autenticada) |
| INF.08 → INF.09 | O lançamento automático em produção usa o build da integração contínua |
| US.20 → US.22 → US.09 | Um álbum precisa de artista (exceto compilações), e a página do álbum precisa de álbuns |
| US.09 → US.10, US.17, US.25, US.26 | Os botões da coleção, das listas, do stock e do carrinho estão na página do álbum |
| US.26 → US.27 → US.28 | O carrinho vem antes do pagamento |
| US.12 → US.24 → US.14 | Só há notificação depois de o gestor responder a um pedido |
| US.15 → US.16 e US.17 → US.18 | As listas vêm antes do seu conteúdo |
| US.11 e US.28 → US.29 | As estatísticas usam as coleções e as vendas |
| Maioria das US → QUA.06 → QUA.07 | Os testes com utilizadores precisam da aplicação quase completa, e a melhoria precisa de tempo depois dos testes |
| RED.01 a RED.07 → M.R1 → RED.08 → RED.09 → RED.10 e RED.11 → RED.12 | O design é avaliado antes de se criar infraestrutura; os balanceadores precisam dos servidores para onde encaminham |
| RED.13 → RED.14 | O certificado TLS é emitido para o nome de domínio |
| RED.10 a RED.12 → RED.17 a RED.19 → RED.22 | Os scripts automatizam a infraestrutura e são usados na demonstração final |

Duas notas para o Gantt:
- **Dados de teste (INF.07):** permitem desenvolver a página do álbum, a coleção e a loja antes de os formulários do gestor estarem prontos, o que corta parte da cadeia US.20 → US.22.
- **Testes com utilizadores (QUA.06):** devem acontecer no início do sprint 3, ou no fim do sprint 2. Senão, não há tempo para a iteração de melhoria que a RNF-03 recomenda.

## 8. Ordem sugerida pelas dependências

A ordem final das user stories e a distribuição pelos sprints são decididas pelo gestor de projeto, no papel de product owner, depois do planning poker e das estimativas. A Tabela 8 é só um ponto de partida que respeita as dependências.

**Tabela 8 — Ordem sugerida**

| Nível | Itens | Razão |
|---|---|---|
| 1. Fundações | INF.01 a INF.08, INF.11, GES.01, US.02, US.19, US.20, US.22, INT.05, RED.01 a RED.09, RED.13, RED.16 | Base técnica, autenticação, catálogo mínimo e design de Redes |
| 2. Núcleo do produto | US.01, US.05, US.06, US.08, US.09, US.10, US.11, US.25, US.26, US.27, INT.01, INT.06, RED.10 a RED.12, RED.14, RED.15 | Navegar o catálogo, coleção e carrinho; infraestrutura distribuída e segura |
| 3. Fluxos completos | US.28, INT.03, INT.04, US.12, US.13, US.24, US.14, US.03, US.04, INT.02, US.07, US.15 a US.18, US.21, US.23, QUA.05, RED.17 a RED.19, INF.09 | Pagamento, pedidos, perfil e listas; preparar os testes com utilizadores; scripts de automação |
| 4. Fecho | US.29, QUA.06, QUA.07, QUA.08, QUA.09, RED.20 a RED.22 | Estatísticas, testes de carga e de vulnerabilidades, demonstração final |

As tarefas contínuas (GES.02 a GES.08, INF.10, QUA.01, QUA.02, QUA.11) repetem-se em todos os sprints.

## 9. Em aberto

| Ponto | Quem resolve | Quando |
|---|---|---|
| Datas das 4 reuniões de avaliação de Redes e versão de 2026/27 do enunciado (pode ter diferenças) | Docentes de PTIR | Início do semestre |
| Plataforma cloud (GCP, AWS ou Azure) e créditos de estudante | Equipa, com o responsável de redes | Antes do relatório de design |
| Data de início do semestre e de cada sprint | Calendário de PTIR | Antes do Gantt |
| Story points das 29 user stories | Toda a equipa, em planning poker | Reunião de equipa |
| Esforço de cada subtarefa (otimista, provável, pessimista) | Toda a equipa | Depois do planning poker |
| Pessoa responsável por cada item | Gestor de projeto, depois de atribuir os papéis | Antes do Gantt |
