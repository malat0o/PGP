# Casos de uso

**Responsável:** Reis · Diagramas em [`img/`](img): [topo](img/casos-uso-00-topo.png), [Conta e perfil](img/casos-uso-01-conta.png), [Catálogo de música](img/casos-uso-02-catalogo.png), [Coleção e listas](img/casos-uso-03-colecao-listas.png), [Pedidos de nova versão](img/casos-uso-04-pedidos.png), [Loja](img/casos-uso-05-loja.png) e [Estatísticas](img/casos-uso-06-estatisticas.png)

Com 21 casos de uso, um só diagrama não cabia numa página A4. Como indicou o professor, os casos de uso estão organizados em **packages**, um por agrupamento lógico: há um **diagrama de topo** com os packages e os atores envolvidos em cada um, e um diagrama por package com os seus casos de uso.

| Package | Casos de uso | Atores |
|---|---|---|
| Conta e perfil | UC-01 a UC-05 | Utilizador, Gestor (só UC-02), Serviço de Geocodificação, Serviço de Mapas |
| Catálogo de música | UC-06 a UC-09, UC-17, UC-18 | Utilizador, Gestor, Cover Art Archive, MusicBrainz |
| Coleção e listas | UC-10 a UC-12 | Utilizador |
| Pedidos de nova versão | UC-13, UC-14, UC-19 | Utilizador, Gestor |
| Loja | UC-15, UC-16, UC-20 | Utilizador, Gestor, Serviço de Pagamentos |
| Estatísticas | UC-21 | Gestor, Serviço de Mapas |

Cores nos diagramas dos packages: azul = só Utilizador; vermelho = só Gestor; roxo = os dois atores. Um caso de uso de outro package aparece a tracejado (o UC-09 no package Loja, por causa do «extend» do UC-20).

## 1. Atores

| Ator | Tipo | Descrição |
|---|---|---|
| **Utilizador** | Humano | Colecionador de álbuns e potencial cliente da loja. |
| **Gestor** | Humano | Gestor da loja de música. A conta já existe pré-configurada. |
| **Serviço de Geocodificação** (Nominatim) | Sistema externo | Converte a morada do utilizador em coordenadas. |
| **Serviço de Mapas** (Leaflet + OpenStreetMap) | Sistema externo | Mostra moradas num mapa. |
| **Serviço de Pagamentos** (Stripe / PayPal) | Sistema externo | Processa o pagamento do carrinho. |
| **Cover Art Archive** | Sistema externo | Sugere a capa do álbum a partir do MBID. |
| **MusicBrainz** | Sistema externo | Fornece as faixas e canções para importação em bloco. |

## 2. Lista de casos de uso

| ID | Caso de uso | Package | Atores | User stories |
|---|---|---|---|---|
| UC-01 | Criar conta | Conta e perfil | Utilizador, Serviço de Geocodificação | US1 |
| UC-02 | Iniciar sessão | Conta e perfil | Utilizador, Gestor | US2 |
| UC-03 | Aceder ao dashboard | Conta e perfil | Utilizador | US19 |
| UC-04 | Visualizar perfil | Conta e perfil | Utilizador, Serviço de Mapas | US3 |
| UC-05 | Gerir perfil | Conta e perfil | Utilizador, Serviço de Geocodificação | US4 |
| UC-06 | Pesquisar artistas e álbuns | Catálogo de música | Utilizador | US5, US8 |
| UC-07 | Visualizar página de artista | Catálogo de música | Utilizador | US6 |
| UC-08 | Gerir artista favorito (estende UC-07) | Catálogo de música | Utilizador | US7 |
| UC-09 | Visualizar página de álbum | Catálogo de música | Utilizador, Gestor | US9, US25 a) |
| UC-10 | Gerir coleção (adicionar, ver, ordenar e remover versões) | Coleção e listas | Utilizador | US10, US11 |
| UC-11 | Gerir listas personalizadas (criar, ver, ordenar e remover) | Coleção e listas | Utilizador | US15, US16 |
| UC-12 | Gerir conteúdo de uma lista (adicionar, ver e remover álbuns) | Coleção e listas | Utilizador | US17, US18 |
| UC-13 | Submeter pedido de nova versão | Pedidos de nova versão | Utilizador | US12 |
| UC-14 | Consultar pedidos e notificações | Pedidos de nova versão | Utilizador | US13, US14 |
| UC-15 | Gerir carrinho de compras (colocar, ver e remover) | Loja | Utilizador | US26, US27 |
| UC-16 | Pagar carrinho | Loja | Utilizador, Serviço de Pagamentos | US28 |
| UC-17 | Gerir artistas (registar e alterar) | Catálogo de música | Gestor | US20, US21 |
| UC-18 | Gerir álbuns e versões (registar e alterar) | Catálogo de música | Gestor, Cover Art Archive, MusicBrainz | US22, US23 |
| UC-19 | Responder a pedido de nova versão | Pedidos de nova versão | Gestor | US24 |
| UC-20 | Gerir stock («extend» UC-09) | Loja | Gestor | US25 |
| UC-21 | Visualizar estatísticas | Estatísticas | Gestor, Serviço de Mapas | US29 |

**Critério de agrupamento:** as user stories que atuam sobre os mesmos dados e pelo mesmo ator formam um só caso de uso (por exemplo, criar, ver e remover listas). Por isso alguns casos de uso correspondem a duas user stories e outros a uma só; a secção 5 conta os cenários de cada um.

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

## 5. Cenários dos casos de uso

Derivados dos critérios de aceitação das user stories. Servem de medida de tamanho para a estimação da Etapa 2 (Use Case Points e decomposição por funcionalidade).

| Caso de uso | Cenário principal | Cenários alternativos | N.º de cenários |
|---|---|---|---|
| UC-01 | Conta criada com coordenadas da morada | Dados inválidos: erro com o motivo (US1 g); Morada não encontrada: conta guardada sem coordenadas | 3 |
| UC-02 | Sessão iniciada: mostra o dashboard | Credenciais erradas: erro genérico (US2 b) | 2 |
| UC-03 | Acesso às funcionalidades a partir do dashboard | Há notificações por ler: contador no sino | 2 |
| UC-04 | Perfil com mapa da morada | Morada sem coordenadas: perfil sem mapa; Sem artista favorito | 3 |
| UC-05 | Alterações guardadas | Palavra-passe atual errada (US4 b); Dados inválidos: erro com o motivo | 3 |
| UC-06 | Sugestões e resultados de artistas ou de álbuns | Sem resultados: mensagem (US5 c, US8 c) | 2 |
| UC-07 | Página do artista com os álbuns mais recentes | Lista completa de álbuns, ordenada por ano (US6 b, c) | 2 |
| UC-08 | Artista adicionado como favorito | Já tem outro favorito: erro (US7 c); Deixar de ter o artista como favorito (US7 d) | 3 |
| UC-09 | Página do álbum com faixas, versões e disponibilidade | Álbum nunca esteve na loja: mensagem discreta (US9 e); Versão esgotada: data da última venda (US9 d) | 3 |
| UC-10 | Versão adicionada à coleção | Versão já está na coleção: erro (US10 c); Ver e ordenar a coleção (US11 c); Remover um álbum (US11 f) | 4 |
| UC-11 | Lista criada | Nome repetido ou com mais de 100 carateres: erro; Ainda não há listas: mensagem (US16 d); Ordenar as listas (US16 b); Remover uma lista (US16 e) | 5 |
| UC-12 | Álbum adicionado a uma lista | Álbum já está na lista: erro (US17 c); Lista vazia: mensagem (US18 d); Ordenar o conteúdo (US18 b); Remover um álbum (US18 e) | 5 |
| UC-13 | Pedido guardado com estado "em análise" | Dados inválidos: erro com o motivo | 2 |
| UC-14 | Lista dos pedidos do utilizador | Filtrar por estado (US13 e); Abrir a notificação de um pedido aceite ou recusado (US14) | 3 |
| UC-15 | Versão colocada no carrinho | Versão sem unidades: botão inativo (US26 a); Ver o carrinho (US27); Remover um álbum (US27 d) | 4 |
| UC-16 | Pagamento com sucesso: fatura, coleção e stock | Uma versão esgotou entretanto: sai do carrinho; Pagamento recusado e nova tentativa com outro serviço (US28 g); Sem resposta no tempo limite: reserva libertada; Cancelamento pelo utilizador (US28 g) | 5 |
| UC-17 | Artista registado | Dados inválidos: erro com o motivo (US20 b, c); Alterar os dados de um artista (US21) | 3 |
| UC-18 | Álbum novo registado com a primeira versão | Nova versão de um álbum existente (US22 b); Dados inválidos: erro com o motivo (US22 i); Alterar os dados do álbum e das versões (US23); Capa sugerida pelo Cover Art Archive; Faixas importadas do MusicBrainz | 6 |
| UC-19 | Pedido aceite: versão criada e utilizador notificado | Pedido recusado: utilizador notificado (US24 d) | 2 |
| UC-20 | Unidades de uma versão alteradas | Primeira vez à venda: pede o preço e regista a data (US25 b) | 2 |
| UC-21 | Estatísticas com as três tabelas e o mapa | Abrir a página de um utilizador ou álbum das estatísticas (US29 e) | 2 |
| **Total** | 21 | 45 | **66** |
