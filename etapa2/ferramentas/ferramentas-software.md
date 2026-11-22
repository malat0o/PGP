# Ferramentas de desenvolvimento e software da aplicação

O enunciado da Etapa 2 pede que se distingam as **ferramentas de desenvolvimento** (necessárias para construir a aplicação, como um editor de código) do **software necessário ao funcionamento** da aplicação. Para cada um indica-se o propósito e um link para a documentação.

A organização segue a **definição de recursos** da aula T06:
- recursos de **ambiente de desenvolvimento** (secção 1);
- recursos de **software reutilizável** (secção 2), classificados como COTS, full-experience, partial-experience ou new;
- **componentes novos** (secção 3);
- **recursos humanos**, que estão em `etapa2/equipa/papeis.md`.

Para cada recurso, a T06 pede também quando vai ser necessário. A coluna "Quando" usa os sprints (S1, S2, S3) e os pacotes de trabalho do backlog.

## 1. Ferramentas de desenvolvimento

Não fazem parte da aplicação em produção: servem para a construir, testar e gerir.

**Tabela 1 — Ferramentas de desenvolvimento**

| Ferramenta | Propósito | Quando | Documentação |
|---|---|---|---|
| Visual Studio Code | Editor de código usado por toda a equipa | S1 a S3 | https://code.visualstudio.com/docs |
| Git | Controlo de versões do código (RNF-06) | S1 a S3 | https://git-scm.com/doc |
| GitHub | Repositório partilhado, pull requests e revisão de código, issues (RNF-05, RNF-06) | S1 a S3 | https://docs.github.com |
| GitHub Actions | Integração contínua (build e testes em cada push) e lançamento em produção a partir do repositório (RNF-06, RNF-07; INF.08, INF.09) | S1 a S3 | https://docs.github.com/actions |
| npm | Gestão das dependências JavaScript do frontend e do backend | S1 a S3 | https://docs.npmjs.com |
| Angular CLI | Criar, compilar e testar o projeto Angular | S1 a S3 | https://angular.dev/tools/cli |
| Swagger Editor | Escrever e validar a especificação OpenAPI da API (RNF-09; INF.10) | S1 a S3 | https://editor.swagger.io |
| Postman | Experimentar e testar os pedidos à API (QUA.02) | S1 a S3 | https://learning.postman.com |
| Jest | Testes unitários e de integração do backend (RNF-13; QUA.01) | S1 a S3 | https://jestjs.io/docs/getting-started |
| Ferramentas de teste do Angular | Testes unitários dos componentes do frontend (RNF-13; QUA.01) | S1 a S3 | https://angular.dev/guide/testing |
| Playwright | Testes de regressão automáticos no browser, sugeridos na T10 (QUA.01, QUA.11) | S2, S3 | https://playwright.dev/docs/intro |
| Docker | Correr o MongoDB em desenvolvimento e empacotar os serviços (INF.04) | S1 a S3 | https://docs.docker.com |
| MongoDB Compass | Consultar e corrigir os dados durante o desenvolvimento | S1 a S3 | https://www.mongodb.com/docs/compass/ |
| Locust | Testes de carga (RED.20), recomendado pelo enunciado de Redes | S3 | https://docs.locust.io |
| nmap | Análise de portas abertas e serviços expostos (RED.21) | S3 | https://nmap.org/docs.html |
| OWASP ZAP | Testes de vulnerabilidades da aplicação web (RED.21) | S2, S3 | https://www.zaproxy.org/docs/ |
| Microsoft Planner | Backlog, sprints e acompanhamento das tarefas, como na aula prática do Planner (WP.1) | S1 a S3 | https://support.microsoft.com/planner |
| Microsoft Project | Mapa de Gantt, dependências e caminho crítico, como na aula prática do Project (GES.06) | S1 a S3 | https://support.microsoft.com/project |
| Microsoft Teams | Comunicação da equipa e acesso ao Planner | S1 a S3 | https://support.microsoft.com/teams |
| draw.io | Diagramas: arquitetura distribuída para o relatório de design de Redes (RED.03) e diagramas UML | S1 | https://www.drawio.com/doc/ |

## 2. Software necessário ao funcionamento da aplicação

Sem este software a aplicação não funciona. Seguindo a T06, cada item é classificado como:
- **COTS:** existe no mercado e está pronto a usar;
- **full-experience:** existe internamente e é de baixo risco;
- **partial-experience:** existe internamente, mas com mais risco de adaptação;
- **new:** é construído de raiz.

Todos os itens desta secção são COTS: são software de terceiros, gratuito ou com planos gratuitos (RNF-15).

**Tabela 2 — Software reutilizável da aplicação**

| Software | Camada | Propósito | Classe (T06) | Documentação |
|---|---|---|---|---|
| Node.js | Backend | Ambiente de execução do JavaScript no servidor | COTS | https://nodejs.org/docs/latest/api/ |
| Express | Backend | Framework da API REST (RNF-01, RNF-09) | COTS | https://expressjs.com |
| Mongoose | Backend | Esquemas e validações dos dados no MongoDB (RNF-02) | COTS | https://mongoosejs.com/docs/ |
| bcrypt | Backend | Cifrar as palavras-passe antes de as guardar (RNF-12) | COTS | https://www.npmjs.com/package/bcrypt |
| jsonwebtoken | Backend | Tokens de sessão, para o backend não guardar estado (RNF-10, RNF-12) | COTS | https://www.npmjs.com/package/jsonwebtoken |
| Angular | Frontend | Framework da interface com o utilizador (RNF-01, RNF-04) | COTS | https://angular.dev |
| Leaflet | Frontend | Mostrar mapas no perfil e nas estatísticas (US3, US29) | COTS | https://leafletjs.com/reference.html |
| MongoDB | Dados | Base de dados, com instância principal e de reserva (RED.11) | COTS | https://www.mongodb.com/docs/manual/ |
| HAProxy | Infraestrutura | Balanceadores de carga em ativo-passivo (RED.12) | COTS | https://docs.haproxy.org |
| Nginx | Infraestrutura | Servir os ficheiros do frontend nos servidores aplicacionais | COTS | https://nginx.org/en/docs/ |
| Ubuntu Server | Infraestrutura | Sistema operativo das máquinas virtuais | COTS | https://ubuntu.com/server/docs |
| GCP, AWS ou Azure | Infraestrutura | Máquinas virtuais e IP estático; o enunciado de Redes deixa escolher uma destas três (RED.08) | COTS | https://cloud.google.com/compute/docs · https://docs.aws.amazon.com/ec2/ · https://learn.microsoft.com/azure/virtual-machines/ |
| Let's Encrypt e Certbot | Infraestrutura | Certificado TLS gratuito, assinado por uma autoridade certificadora, para o HTTPS (RED.14) | COTS | https://letsencrypt.org/docs/ · https://certbot.eff.org |
| OpenStreetMap (mosaicos) | Serviço externo | Imagens dos mapas mostrados pelo Leaflet | COTS | https://operations.osmfoundation.org/policies/tiles/ |
| Nominatim | Serviço externo | Converter moradas em coordenadas (US1, US4; INT.01) | COTS | https://nominatim.org/release-docs/latest/api/Search/ |
| Stripe | Serviço externo | Pagamento online, serviço principal (US28; INT.03) | COTS | https://docs.stripe.com |
| PayPal | Serviço externo | Pagamento online, serviço alternativo (US28; INT.04) | COTS | https://developer.paypal.com/docs/ |
| Cloudinary | Serviço externo | Guardar e entregar as imagens de capa (US22 f; INT.05) | COTS | https://cloudinary.com/documentation |
| Cover Art Archive | Serviço externo | Sugerir a capa de um álbum pelo MBID (INT.05) | COTS | https://musicbrainz.org/doc/Cover_Art_Archive/API |
| API do MusicBrainz | Serviço externo | Importar as faixas e canções de um álbum (nota 12; INT.06) | COTS | https://musicbrainz.org/doc/MusicBrainz_API |

A escolha de cada serviço externo foi justificada na Etapa 1 (capítulo 6), com comparação com um concorrente. A stack MEAN é a sugerida no enunciado. As peças de infraestrutura vêm do enunciado de Redes: balanceadores com HAProxy, máquinas virtuais numa das três clouds e certificados Let's Encrypt.

**Restrição do enunciado de Redes:** não se podem usar serviços geridos que deem balanceamento, escalabilidade ou tolerância a falhas automáticos (por exemplo, App Engine ou Kubernetes). Por isso o MongoDB e o HAProxy são instalados e configurados nas máquinas virtuais pela equipa, e não contratados como serviço.

## 3. Componentes novos

Construídos de raiz pela equipa (classe **new** da T06):

**Tabela 3 — Componentes novos**

| Componente | Propósito | Itens do backlog |
|---|---|---|
| Frontend Angular | Ecrãs das 29 user stories, desenhados nos esboços da Etapa 1 | INF.02, INF.11, subtarefas .2 das US |
| Backend Express | API REST especificada em `etapa2/api/api.yaml` | INF.03, INF.05, INF.06, subtarefas .1 das US |
| Esquemas de dados | Tradução das 19 classes do modelo da Etapa 1 para Mongoose | INF.04 |
| Importador de faixas | Endpoint que importa faixas do MusicBrainz | INT.06 |
| Scripts de infraestrutura | Os 10 scripts pedidos no enunciado de Redes | RED.17 a RED.19 |
| Testes | Testes unitários, de integração, de regressão, de carga e de vulnerabilidades | QUA.01, QUA.02, RED.20, RED.21 |
