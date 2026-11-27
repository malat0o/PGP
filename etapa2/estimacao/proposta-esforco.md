# Proposta inicial de esforço por item

**Isto é um ponto de partida para a equipa rever, não a estimativa da equipa.** O enunciado pede que o esforço seja estimado pela equipa. Na sessão de estimação, cada responsável revê os valores dos seus itens, altera os que não concordar e copia-os para a folha "Esforço" do livro (`estimacao-etapa2.xlsx`). No relatório deve aparecer a estimativa revista.

## Como foi feita

Segue a estimação por decomposição com três valores da T06. Cada item foi classificado numa classe de tamanho, a partir da decomposição das user stories (dados e API, ecrã, serviço externo, testes) e da complexidade da tarefa. Cada classe tem três valores, e o esforço esperado é (O + 4M + P) ÷ 6. Os valores contam com uma equipa que ainda está a aprender a stack MEAN e a infraestrutura distribuída (riscos R02 e R03).

**Tabela 1 — Classes de tamanho**

| Classe | Otimista (h) | Provável (h) | Pessimista (h) | Esperado (h) | Exemplo |
|---|---|---|---|---|---|
| XS | 3 | 5 | 8 | 5.2 | Criar lista (US15), dashboard (US19) |
| S | 5 | 8 | 13 | 8.3 | Iniciar sessão (US2), ver carrinho (US27) |
| M | 8 | 13 | 20 | 13.3 | Criar conta (US1), responder a pedido (US24) |
| L | 13 | 20 | 32 | 20.8 | Página de álbum (US9), registar álbum (US22), pagar o carrinho (US28), estatísticas (US29) |
| XL | 20 | 32 | 50 | 33.0 | Nenhum item, depois de separar a integração com os serviços de pagamento da US28 |

Os itens de gestão e os testes automáticos foram estimados pelo número de vezes que acontecem (coluna "Base").

## Esforço por item

**Tabela 2 — Proposta de esforço por item**

| ID | Item | Pacote | Classe | O | M | P | Esperado (h) | Base |
|---|---|---|---|---|---|---|---|---|
| US.01 | Criar conta | WP.3 | M | 8 | 13 | 20 | 13.3 |  |
| US.02 | Iniciar sessão | WP.3 | S | 5 | 8 | 13 | 8.3 |  |
| US.03 | Visualizar perfil | WP.3 | S | 5 | 8 | 13 | 8.3 |  |
| US.04 | Gerir perfil | WP.3 | M | 8 | 13 | 20 | 13.3 |  |
| US.05 | Pesquisar artistas | WP.4 | S | 5 | 8 | 13 | 8.3 |  |
| US.06 | Visualizar página de artista | WP.4 | S | 5 | 8 | 13 | 8.3 |  |
| US.07 | Adicionar artista como favorito | WP.4 | XS | 3 | 5 | 8 | 5.2 |  |
| US.08 | Pesquisar álbuns | WP.4 | XS | 3 | 5 | 8 | 5.2 |  |
| US.09 | Visualizar página de álbum | WP.4 | L | 13 | 20 | 32 | 20.8 |  |
| US.10 | Adicionar versão à coleção | WP.5 | XS | 3 | 5 | 8 | 5.2 |  |
| US.11 | Visualizar coleção | WP.5 | S | 5 | 8 | 13 | 8.3 |  |
| US.12 | Submeter pedido de nova versão | WP.6 | S | 5 | 8 | 13 | 8.3 |  |
| US.13 | Ver estado dos pedidos | WP.6 | S | 5 | 8 | 13 | 8.3 |  |
| US.14 | Ser notificado da resposta a um pedido | WP.6 | S | 5 | 8 | 13 | 8.3 |  |
| US.15 | Criar lista personalizada | WP.5 | XS | 3 | 5 | 8 | 5.2 |  |
| US.16 | Visualizar listas personalizadas | WP.5 | S | 5 | 8 | 13 | 8.3 |  |
| US.17 | Adicionar álbum a uma lista | WP.5 | XS | 3 | 5 | 8 | 5.2 |  |
| US.18 | Visualizar conteúdo de uma lista | WP.5 | S | 5 | 8 | 13 | 8.3 |  |
| US.19 | Aceder ao dashboard | WP.3 | XS | 3 | 5 | 8 | 5.2 |  |
| US.20 | Registar artista | WP.4 | S | 5 | 8 | 13 | 8.3 |  |
| US.21 | Gerir dados de um artista | WP.4 | XS | 3 | 5 | 8 | 5.2 |  |
| US.22 | Registar álbum ou versão | WP.4 | L | 13 | 20 | 32 | 20.8 |  |
| US.23 | Gerir dados de um álbum | WP.4 | M | 8 | 13 | 20 | 13.3 |  |
| US.24 | Responder a pedido de nova versão | WP.6 | M | 8 | 13 | 20 | 13.3 |  |
| US.25 | Aumentar ou diminuir unidades | WP.7 | S | 5 | 8 | 13 | 8.3 |  |
| US.26 | Colocar álbum no carrinho | WP.7 | XS | 3 | 5 | 8 | 5.2 |  |
| US.27 | Visualizar carrinho | WP.7 | S | 5 | 8 | 13 | 8.3 |  |
| US.28 | Pagar o carrinho | WP.7 | L | 13 | 20 | 32 | 20.8 |  |
| US.29 | Visualizar estatísticas | WP.8 | L | 13 | 20 | 32 | 20.8 |  |
| GES.01 | Configurar o Planner: buckets (Backlog, Sprint 1 a 3, Em curso, Feito) e etiquetas | WP.1 | XS | 3 | 5 | 8 | 5.2 |  |
| GES.02 | Sprint planning (uma por sprint) | WP.1 | — | 10 | 15 | 20 | 15.0 | 3 sprint plannings × 5 pessoas × 1 h |
| GES.03 | Reuniões de acompanhamento da equipa (contínuo) | WP.1 | — | 15 | 25 | 40 | 25.8 | 1 reunião/semana × 20 a 30 min × 5 pessoas × 13 semanas |
| GES.04 | Sprint review com demonstração ao cliente (M.1, M.2, M.3) | WP.1 | — | 10 | 15 | 25 | 15.8 | 3 reviews × 5 pessoas × 1 h (demos nas aulas) |
| GES.05 | Retrospetiva do sprint (uma por sprint) | WP.1 | — | 5 | 8 | 12 | 8.2 | 3 retrospetivas × 5 pessoas × 30 min |
| GES.06 | Acompanhar o progresso: atualizar o Gantt e calcular a earned value analysis | WP.1 | — | 8 | 12 | 20 | 12.7 | Gantt e earned value analysis, cerca de 1 h por semana |
| GES.07 | Rever estimativas entre sprints (planning poker de ajuste) | WP.1 | — | 5 | 8 | 12 | 8.2 | 2 planning pokers de ajuste × 5 pessoas × 50 min |
| GES.08 | Relatórios e entregas de PTIR | WP.1 | — | 5 | 10 | 20 | 10.8 | Relatórios e entregas de PTIR |
| INF.01 | Repositório Git, ramos e regras de pull request; licença de código aberto | WP.2 | XS | 3 | 5 | 8 | 5.2 |  |
| INF.02 | Esqueleto do frontend em Angular, com rotas e serviços | WP.2 | S | 5 | 8 | 13 | 8.3 |  |
| INF.03 | Esqueleto do backend em Express: estrutura da API REST, erros e códigos HTTP | WP.2 | S | 5 | 8 | 13 | 8.3 |  |
| INF.04 | Base de dados MongoDB para desenvolvimento (local ou em container) e esquemas Mongoose a partir do modelo de classes | WP.2 | M | 8 | 13 | 20 | 13.3 |  |
| INF.05 | Validações comuns das restrições de integridade (RI-01 a RI-52) | WP.2 | M | 8 | 13 | 20 | 13.3 |  |
| INF.06 | Autenticação com token e palavras-passe cifradas | WP.2 | M | 8 | 13 | 20 | 13.3 |  |
| INF.07 | Conta do gestor pré-configurada e dados de teste (seed) | WP.2 | S | 5 | 8 | 13 | 8.3 |  |
| INF.08 | Integração contínua: build e testes automáticos em cada push | WP.2 | S | 5 | 8 | 13 | 8.3 |  |
| INF.09 | Pipeline de lançamento em produção: GitHub Actions que usa os scripts de Redes | WP.2 | M | 8 | 13 | 20 | 13.3 |  |
| INF.10 | Manter a especificação OpenAPI da API atualizada | WP.2 | S | 5 | 8 | 13 | 8.3 |  |
| INF.11 | Layout base responsivo: navegação, mensagens de sucesso e de erro | WP.2 | S | 5 | 8 | 13 | 8.3 |  |
| INT.01 | Geocodificação com o Nominatim (1 pedido por segundo, uma vez por morada) | WP.9 | S | 5 | 8 | 13 | 8.3 |  |
| INT.02 | Mapas com Leaflet e OpenStreetMap | WP.9 | S | 5 | 8 | 13 | 8.3 |  |
| INT.03 | Pagamento com Stripe em modo de teste: checkout e webhook | WP.9 | L | 13 | 20 | 32 | 20.8 |  |
| INT.04 | Pagamento com PayPal em modo de teste | WP.9 | M | 8 | 13 | 20 | 13.3 |  |
| INT.05 | Capas: sugestão do Cover Art Archive e envio para o Cloudinary | WP.9 | M | 8 | 13 | 20 | 13.3 |  |
| INT.06 | Importação de faixas e canções da API do MusicBrainz | WP.9 | M | 8 | 13 | 20 | 13.3 |  |
| QUA.01 | Política de testes e testes unitários e de integração ao longo do projeto | WP.10 | — | 20 | 35 | 55 | 35.8 | Testes unitários e de integração ao longo do projeto |
| QUA.02 | Testes à API | WP.10 | M | 8 | 13 | 20 | 13.3 |  |
| QUA.05 | Preparar os testes com utilizadores: tarefas, guião e questionário SUS | WP.10 | S | 5 | 8 | 13 | 8.3 |  |
| QUA.06 | Realizar os testes com utilizadores e analisar os resultados SUS | WP.10 | M | 8 | 13 | 20 | 13.3 |  |
| QUA.07 | Iteração de melhoria da usabilidade | WP.10 | M | 8 | 13 | 20 | 13.3 |  |
| QUA.08 | Política de backup e procedimento de restauro | WP.10 | S | 5 | 8 | 13 | 8.3 |  |
| QUA.09 | Informação sobre tratamento de dados; consulta e eliminação dos dados pessoais | WP.10 | S | 5 | 8 | 13 | 8.3 |  |
| QUA.11 | Verificação em telemóvel dos ecrãs principais | WP.10 | S | 5 | 8 | 13 | 8.3 |  |
| RED.01 | Relatório de design: visão geral do sistema (1 página) | WP.11 | XS | 3 | 5 | 8 | 5.2 |  |
| RED.02 | Relatório de design: 7 requisitos não funcionais (disponibilidade, escalabilidade, desempenho, tolerância a faltas, segurança, operação e manutenção, isolamento de rede), cada um com requisito, métrica e mecanismo | WP.11 | S | 5 | 8 | 13 | 8.3 |  |
| RED.03 | Diagrama de sistema: componentes e redes | WP.11 | S | 5 | 8 | 13 | 8.3 |  |
| RED.04 | Estratégia de redundância e tolerância a falhas | WP.11 | XS | 3 | 5 | 8 | 5.2 |  |
| RED.05 | Estratégia de escalabilidade (passiva) | WP.11 | XS | 3 | 5 | 8 | 5.2 |  |
| RED.06 | Tabela de comunicações entre componentes (portos e protocolos) | WP.11 | XS | 3 | 5 | 8 | 5.2 |  |
| RED.07 | Arquitetura de segurança: exposição de serviços, controlo de acesso, comunicação segura, acesso administrativo | WP.11 | S | 5 | 8 | 13 | 8.3 |  |
| RED.08 | Conta e projeto na cloud (GCP, AWS ou Azure) e IP público estático reservado | WP.11 | S | 5 | 8 | 13 | 8.3 |  |
| RED.09 | Redes: rede externa e rede interna | WP.11 | S | 5 | 8 | 13 | 8.3 |  |
| RED.10 | Servidores aplicacionais: pelo menos 2 máquinas virtuais com a aplicação | WP.11 | M | 8 | 13 | 20 | 13.3 |  |
| RED.11 | Bases de dados: MongoDB principal e de reserva, em máquinas virtuais | WP.11 | L | 13 | 20 | 32 | 20.8 |  |
| RED.12 | Balanceadores de carga: LB1 e LB2 em ativo-passivo (por exemplo, HAProxy) | WP.11 | L | 13 | 20 | 32 | 20.8 |  |
| RED.13 | Nome de domínio registado e associado ao IP estático | WP.11 | S | 5 | 8 | 13 | 8.3 |  |
| RED.14 | HTTPS com certificado TLS assinado por uma autoridade certificadora (por exemplo, Let's Encrypt) | WP.11 | S | 5 | 8 | 13 | 8.3 |  |
| RED.15 | Firewall: regras entre componentes (security groups ou iptables) | WP.11 | M | 8 | 13 | 20 | 13.3 |  |
| RED.16 | Acesso administrativo por SSH com chaves e restrição por IP | WP.11 | XS | 3 | 5 | 8 | 5.2 |  |
| RED.17 | Scripts do servidor aplicacional: `create_app_server.sh`, `kill_app_server.sh` | WP.11 | S | 5 | 8 | 13 | 8.3 |  |
| RED.18 | Scripts da base de dados: `create_db_primary.sh`, `create_db_backup.sh`, `kill_db_primary.sh`, `promote_db_backup.sh` | WP.11 | M | 8 | 13 | 20 | 13.3 |  |
| RED.19 | Scripts dos balanceadores: `create_lb.sh`, `create_lb_backup.sh`, `kill_lb_primary.sh`, `promote_lb_backup.sh` | WP.11 | M | 8 | 13 | 20 | 13.3 |  |
| RED.20 | Testes de carga (por exemplo, Locust): tempo de resposta, vários clientes, balanceamento | WP.11 | M | 8 | 13 | 20 | 13.3 |  |
| RED.21 | Testes de vulnerabilidades (por exemplo, nmap e OWASP ZAP) | WP.11 | S | 5 | 8 | 13 | 8.3 |  |
| RED.22 | Preparar a demonstração final: lançar servidores, falha da base de dados principal, falha do LB1 | WP.11 | S | 5 | 8 | 13 | 8.3 |  |
| | **Total** | | | | | | **901** | |

## Totais por pacote de trabalho

**Tabela 3 — Esforço esperado por pacote**

| Pacote | Esforço esperado (h) | % |
|---|---|---|
| WP.1 Gestão do projeto | 102 | 11% |
| WP.2 Infraestrutura e arquitetura | 108 | 12% |
| WP.3 Conta e perfil | 48 | 5% |
| WP.4 Catálogo de música | 96 | 11% |
| WP.5 Coleção e listas | 40 | 4% |
| WP.6 Pedidos de nova versão | 38 | 4% |
| WP.7 Loja | 43 | 5% |
| WP.8 Estatísticas | 21 | 2% |
| WP.9 Integrações externas | 78 | 9% |
| WP.10 Qualidade, testes e RNF | 109 | 12% |
| WP.11 Tecnologias de Redes | 218 | 24% |
| **Total** | **901** | 100% |

## Comparação com o esforço disponível

**Tabela 4 — Necessário vs. disponível**

| Cenário | Disponível para planear (h) | Necessário (h) | Diferença (h) |
|---|---|---|---|
| 4,5 h por pessoa por semana | 249 | 901 | -652 |
| 12 h por pessoa por semana (PTIR = 6 ECTS ≈ 156 h) | 663 | 901 | -238 |
| 14 h por pessoa por semana (2 h por dia) | 774 | 901 | -127 |

- As 29 user stories somam cerca de **286 h** e o software no seu conjunto (pacotes WP.2 a WP.9) cerca de **472 h**. É menos do que a estimativa de controlo (1 400 a 1 870 h), porque esta proposta conta com uma implementação simples de cada ecrã. A T06 manda perceber diferenças grandes entre estimativas: na sessão de estimação, a equipa deve decidir se os valores estão otimistas.
- Mesmo com 10 h por semana, o necessário passa do disponível. O enunciado não o permite, por isso o product owner tem de **reduzir o âmbito**: ficam nos 3 sprints as funcionalidades prioritárias, e as restantes passam para um incremento posterior (T07).

## Candidatos a sair do âmbito (decisão do product owner)

Itens que podem sair sem pôr em causa o fluxo principal (conta, catálogo, coleção, carrinho e pagamento) nem a parte obrigatória de Redes:

| ID | Item | Esperado (h) | Porque pode sair |
|---|---|---|---|
| INT.04 | Pagamento com PayPal em modo de teste | 13.3 | A US28 b) só exige poder escolher um serviço; o Stripe chega |
| US.29 | Visualizar estatísticas | 20.8 | Estatísticas do gestor, sem dependentes |
| US.15 | Criar lista personalizada | 5.2 | Listas personalizadas não são precisas para comprar nem colecionar |
| US.16 | Visualizar listas personalizadas | 8.3 | Idem |
| US.17 | Adicionar álbum a uma lista | 5.2 | Idem |
| US.18 | Visualizar conteúdo de uma lista | 8.3 | Idem |
| US.07 | Adicionar artista como favorito | 5.2 | Favorito não é usado por outras funcionalidades além do perfil |
| INT.06 | Importação de faixas e canções da API do MusicBrainz | 13.3 | As faixas podem ser introduzidas nos dados de teste |
| US.21 | Gerir dados de um artista | 5.2 | Alterar artista pode ser feito na base de dados nesta fase |
| US.23 | Gerir dados de um álbum | 13.3 | Idem para o álbum |
| QUA.09 | Informação sobre tratamento de dados; consulta e eliminação dos dados pessoais | 8.3 | RNF-16 está em "Outros" (menos prioritário) |
| | **Total** | **106** | |

Tirando todos estes, o necessário desce para cerca de **794 h**.

## Correções feitas a esta proposta

- **US28 sem contagem a dobrar:** a integração com o Stripe e o PayPal está nos itens INT.03 e INT.04, por isso a US28 conta só a lógica da aplicação (classe L em vez de XL).
- **Scripts de Redes sem contagem a dobrar:** a infraestrutura é montada logo com os scripts, por isso RED.17 a RED.19 contam só o que falta (parametrizar, scripts de falha e de promoção, ensaios).
- **Gestão mais leve:** uma reunião curta por semana, sprint planning de 1 h, e demonstrações durante as aulas. A gestão fica em cerca de 10% do esforço.

## Horas por semana que o plano exige

| Cenário | Necessário (h) | Horas por pessoa por semana (com 15% de margem) |
|---|---|---|
| Âmbito completo | 901 | 16.3 |
| Sem os candidatos acima | 794 | 14.4 |

PTIR tem **6 ECTS**: 6 × 26 h ≈ 156 h por pessoa no semestre, incluindo as aulas, ou seja, cerca de **12 h por semana**. Com 5 pessoas são 780 h, das quais 663 h para planear. O âmbito completo (901 h) não cabe; sem os candidatos acima (794 h) ainda faltam cerca de 131 h. Para fechar o plano, o product owner tem de cortar mais âmbito e a equipa deve rever as estimativas, que contam com uma equipa a aprender a tecnologia.
