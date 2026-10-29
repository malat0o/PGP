# Casos de uso

**Responsável:** Reis · Diagramas em [`img/`](img): [Utilizador](img/casos-uso-utilizador.png) e [Gestor](img/casos-uso-gestor.png)

Com 21 casos de uso, um só diagrama ficava com linhas cruzadas e difícil de ler. Por isso há um diagrama por ator humano. O UC-02 (Iniciar sessão) e o UC-09 (Visualizar página de álbum) aparecem nos dois porque são partilhados.

## 1. Atores

| Ator | Tipo | Descrição |
|---|---|---|
| **Utilizador** | Humano | Colecionador de álbuns e potencial cliente da loja. |
| **Gestor** | Humano | Gestor da loja de música. A conta já existe pré-configurada. |
| **Serviço de Geocodificação** (Nominatim) | Sistema externo | Converte a morada do utilizador em coordenadas. |
| **Serviço de Mapas** (Leaflet + OpenStreetMap) | Sistema externo | Mostra moradas num mapa. |
| **Serviço de Pagamentos** (Stripe / PayPal) | Sistema externo | Processa o pagamento do carrinho. |

## 2. Lista de casos de uso

| ID | Caso de uso | Atores | User stories |
|---|---|---|---|
| UC-01 | Criar conta | Utilizador, Serviço de Geocodificação | US1 |
| UC-02 | Iniciar sessão | Utilizador, Gestor | US2 |
| UC-03 | Aceder ao dashboard | Utilizador | US19 |
| UC-04 | Visualizar perfil | Utilizador, Serviço de Mapas | US3 |
| UC-05 | Gerir perfil | Utilizador, Serviço de Geocodificação | US4 |
| UC-06 | Pesquisar artistas e álbuns | Utilizador | US5, US8 |
| UC-07 | Visualizar página de artista | Utilizador | US6 |
| UC-08 | Gerir artista favorito (estende UC-07) | Utilizador | US7 |
| UC-09 | Visualizar página de álbum | Utilizador, Gestor | US9, US25 a) |
| UC-10 | Gerir coleção (adicionar, ver, ordenar e remover versões) | Utilizador | US10, US11 |
| UC-11 | Gerir listas personalizadas (criar, ver, ordenar e remover) | Utilizador | US15, US16 |
| UC-12 | Gerir conteúdo de uma lista (adicionar, ver e remover álbuns) | Utilizador | US17, US18 |
| UC-13 | Submeter pedido de nova versão | Utilizador | US12 |
| UC-14 | Consultar pedidos e notificações | Utilizador | US13, US14 |
| UC-15 | Gerir carrinho de compras (colocar, ver e remover) | Utilizador | US26, US27 |
| UC-16 | Pagar carrinho | Utilizador, Serviço de Pagamentos | US28 |
| UC-17 | Gerir artistas (registar e alterar) | Gestor | US20, US21 |
| UC-18 | Gerir álbuns e versões (registar e alterar) | Gestor | US22, US23 |
| UC-19 | Responder a pedido de nova versão | Gestor | US24 |
| UC-20 | Gerir stock («extend» UC-09) | Gestor | US25 |
| UC-21 | Visualizar estatísticas | Gestor, Serviço de Mapas | US29 |

As user stories parecidas foram agrupadas num só caso de uso quando atuam sobre os mesmos dados (por exemplo, criar, ver e remover listas), para o diagrama ficar legível.

## 3. Matriz US ↔ UC

Confirma que as 29 user stories estão cobertas.

| US | UC | US | UC | US | UC |
|---|---|---|---|---|---|
| US1 | UC-01 | US11 | UC-10 | US21 | UC-17 |
| US2 | UC-02 | US12 | UC-13 | US22 | UC-18 |
| US3 | UC-04 | US13 | UC-14 | US23 | UC-18 |
| US4 | UC-05 | US14 | UC-14 | US24 | UC-19 |
| US5 | UC-06 | US15 | UC-11 | US25 | UC-20 |
| US6 | UC-07 | US16 | UC-11 | US26 | UC-15 |
| US7 | UC-08 | US17 | UC-12 | US27 | UC-15 |
| US8 | UC-06 | US18 | UC-12 | US28 | UC-16 |
| US9 | UC-09 | US19 | UC-03 | US29 | UC-21 |
| US10 | UC-10 | US20 | UC-17 | | |

**Cobertura:** 29 de 29 user stories ✅

## 4. Relações entre casos de uso

- **UC-08 «extend» UC-07:** adicionar ou remover um artista dos favoritos é uma opção dentro da página do artista (US7 a).
- **UC-20 «extend» UC-09:** o gestor altera as unidades a partir da página do álbum (US25 a), por isso gerir o stock é uma extensão dessa página.
