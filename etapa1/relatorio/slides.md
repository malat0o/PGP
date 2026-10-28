# Slides da apresentação: Etapa 1

*Responsável: Edson · Cerca de 10 minutos no total · Apresentação final: `PGP-2627-G12-E1-apresentacao.pptx`*

Cada pessoa apresenta a sua parte. O que dizer em cada slide está nas notas do orador da apresentação.

| # | Slide | Conteúdo | Imagem | Apresenta |
|---|---|---|---|---|
| 1 | **Título** | "Gestão de coleções de álbuns físicos": PGP 2026/27, grupo 12, nomes dos 5 | — | Reis |
| 2 | **O problema** | Aplicação web para uma loja de música: colecionar, comprar e organizar álbuns físicos (CD, vinil, cassete). Dois atores: utilizador e gestor. Stack MEAN. | — | Reis |
| 3 | **Casos de uso** | Visão geral das funcionalidades e dos serviços externos | `casos-uso/img/casos-uso-utilizador.png` e `casos-uso-gestor.png` | Reis |
| 4 | **Modelo de dados: visão geral** | 19 classes em 5 agrupamentos; a VersaoAlbum é a classe central | `classes/img/01-topo.png` | Rodrigo |
| 5 | **Modelo de dados: decisões** | Solista/Grupo, Faixa, Versão vs Álbum, disponibilidade opcional | `classes/img/02-catalogo.png` | Rodrigo |
| 6 | **Restrições de integridade** | 30 do enunciado + 17 novas (RI-31 a RI-47), cada uma com origem | Tabela resumida de `servicos/restricoes.md` | Ze |
| 7 | **Serviços externos** | Leaflet + OSM, Nominatim, Stripe + PayPal: porquê cada um | Tabela comparativa de `servicos/servicos-externos.md` | Ze |
| 8 | **Fluxo de compra** | Do carrinho ao pagamento, e o que acontece em caso de sucesso ou de falha | `atividades/img/01-1-pagar.png` | Edson |
| 9 | **Pedido de nova versão** | Utilizador → gestor → notificação | `atividades/img/02-pedido-nova-versao.png` | Edson |
| 10 | **Esboços: página de álbum** | O ecrã mais complexo: versões, stock, coleção, listas e carrinho | `esbocos/img/E01-pagina-album.png` | Miguel |
| 11 | **Esboços: carrinho e pagamento** | Inclui a versão para telemóvel | `esbocos/img/E02-carrinho-pagamento.png` e `E12-telemovel-carrinho.png` | Miguel |
| 12 | **Dúvidas e suposições** | O que perguntámos ao professor e o que assumimos | — | Reis |

## Notas

- Os diagramas grandes (fluxos de pagamento e catálogo) são altos: no slide, mostrar só a parte central e ter o diagrama completo no relatório.
- Ensaio a 5/nov: cada pessoa fala cerca de 2 minutos.
