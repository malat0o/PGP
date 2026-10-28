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

Com 21 casos de uso, um só diagrama ficava com muitas linhas cruzadas. Por isso foram feitos dois diagramas, um por ator humano:
- **Figura 1:** casos de uso do Utilizador (16 casos de uso).
- **Figura 2:** casos de uso do Gestor (6 casos de uso).

O caso de uso "Iniciar sessão" (UC-02) é comum aos dois atores.

A única relação entre casos de uso é **UC-08 «extend» UC-07**: gerir o artista favorito é uma opção que aparece dentro da página do artista (US7 a).

## Rastreabilidade

A Tabela 1 associa cada user story ao caso de uso que a implementa. As 29 user stories estão cobertas.

*(Tabela 1: matriz US ↔ UC, em `casos-uso.md`.)*
