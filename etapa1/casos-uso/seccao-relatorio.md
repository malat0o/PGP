# Casos de uso

*Secção do relatório da Etapa 1 · Autor: Reis*

O diagrama de casos de uso mostra, numa perspetiva de alto nível, as funcionalidades da aplicação web e os atores que as usam.

## Atores

Há dois atores humanos, como define o enunciado:
- **Utilizador:** colecionador de álbuns e potencial cliente da loja.
- **Gestor da loja:** a sua conta já existe pré-configurada.

Há também três **sistemas externos**, escolhidos na pesquisa de serviços:
- **Serviço de Geocodificação** (Nominatim): converte a morada em coordenadas quando o utilizador cria a conta ou altera o perfil.
- **Serviço de Mapas** (Leaflet + OpenStreetMap): mostra a morada no perfil e as moradas dos maiores colecionadores nas estatísticas.
- **Serviço de Pagamentos** (Stripe ou PayPal): processa o pagamento do carrinho.

## Diagramas

As 29 user stories foram agrupadas em 21 casos de uso. User stories que atuam sobre os mesmos dados ficaram num só caso de uso: por exemplo, "Gerir coleção" junta adicionar uma versão (US10) e ver, ordenar e remover a coleção (US11).

Com 21 casos de uso, um só diagrama não cabia numa página A4. Por isso foram organizados em seis packages, um por agrupamento lógico:
- **Figura 1:** diagrama de topo, com os packages e os atores envolvidos em cada um.
- **Figuras 2 a 7:** um diagrama por package (Conta e perfil, Catálogo de música, Coleção e listas, Pedidos de nova versão, Loja e Estatísticas).

Há duas relações entre casos de uso: **UC-08 «extend» UC-07**, porque gerir o artista favorito é uma opção dentro da página do artista (US7 a); e **UC-20 «extend» UC-09**, porque o gestor altera as unidades a partir da página do álbum (US25 a), por isso gerir o stock é uma extensão dessa página.

## Rastreabilidade

A Tabela 1 associa cada user story ao caso de uso que a implementa. As 29 user stories estão cobertas.

*(Tabela 1: matriz US ↔ UC, em `casos-uso.md`.)*
