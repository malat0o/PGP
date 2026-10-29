# Restrições de integridade

*Etapa 1 · Complementa as RI-01 a RI-30 do enunciado*

## 1. Restrições novas (RI-31 em diante)

Cada restrição nova vem de uma frase do enunciado: do universo do discurso (secção 2), das notas de rodapé ou dos critérios de aceitação das user stories. A coluna "Origem" indica de onde.

| ID | Restrição | Origem |
|---|---|---|
| **RI-31** | Os membros de um grupo só podem ser artistas solistas: um grupo não pode ter como membros outros grupos, nem a si próprio. | Secção 2 ("um grupo não pode ter como membros outros grupos") |
| **RI-32** | Um álbum é interpretado por, no máximo, um artista. Os álbuns de compilação não têm artista. | Secção 2 e nota 10 |
| **RI-33** | O código MBID identifica univocamente um álbum. | Secção 2 ("cada álbum tem um código MBID") |
| **RI-34** | O código ISRC identifica univocamente uma canção. | Secção 2 ("cada canção é identificada por um código ISRC") |
| **RI-35** | O código ISNI identifica univocamente um artista. | Secção 2 |
| **RI-36** | O código EAN-13 identifica univocamente uma versão de um álbum (num suporte físico e versão). | Secção 2 ("é identificado pelo seu código de barras") |
| **RI-37** | O número de uma fatura identifica univocamente a fatura. | Nota 7 ("as faturas têm um número identificador") |
| **RI-38** | O número de faixa é único dentro de cada álbum. | Secção 2 (número de faixa = ordem no álbum) |
| **RI-39** | Se um álbum tiver mais do que uma versão no mesmo suporte físico, todas essas versões têm designação, e as designações são diferentes entre si. | Secção 2 e US9 c) |
| **RI-40** | Um utilizador tem, no máximo, um artista favorito. | US7 c) |
| **RI-41** | Uma versão de um álbum só pode constar uma vez na coleção de um utilizador. | US10 c) |
| **RI-42** | Um álbum só pode constar uma vez em cada lista personalizada. | US17 c) |
| **RI-43** | O identificador de um pedido de nova versão é único. | US13 c) |
| **RI-44** | O estado de um pedido só pode ser "em análise", "aceite" ou "recusado", e o estado inicial é "em análise". | US12 d), US13 d), US24 b) |
| **RI-45** | Um pedido só pode ser aceite se o EAN-13 pedido não corresponder a uma versão já existente. | US24 c) ("corresponderem a uma nova versão") |
| **RI-46** | Só pode ser colocada no carrinho uma versão que esteja disponível na loja (com unidades maiores que zero). | US26 a) |
| **RI-47** | Quando uma versão é registada com um número de unidades maior que zero, a data de início de disponibilidade na loja tem de estar preenchida. | US22 g), US25 b) |
| **RI-48** | Os dados de faturação de uma fatura (NIF, nome e morada) são copiados do utilizador no momento da emissão e não são alterados depois, mesmo que o utilizador mude o perfil ou apague a conta. | US28 d), RNF-16 |
| **RI-49** | A data de resposta de um pedido existe se e só se o estado for "aceite" ou "recusado", e é igual ou posterior à data do pedido. | US24 c) e d) |
| **RI-50** | Uma notificação é criada como não lida (`lida` = falso). | US14 a) |
| **RI-51** | Um item da coleção com origem numa linha de fatura refere-se à mesma versão dessa linha, pertence ao utilizador da fatura e tem como data de registo a data da fatura. | US28 d) |

**Nota sobre a RI-44:** a US24 d) usa a palavra "rejeitado" e as US13 e US14 usam "recusado". Usamos "recusado" até o professor esclarecer.

## 2. Restrições por classe do modelo de dados

Associação de todas as restrições às classes do [diagrama de classes](../classes/modelo-classes.md).

| Classe | Atributo / associação | Restrições |
|---|---|---|
| **Artista** | `isni` | RI-07, RI-35 |
| | `anoInicioAtividade` | RI-08 |
| **Grupo** | associação `membros` | RI-31 |
| **Album** | `mbid` | RI-01, RI-33 |
| | `tipo` | RI-02 |
| | `anoLancamento` | RI-09, RI-10, RI-11 |
| | associação com Artista | RI-06, RI-32 |
| **Faixa** | `numero` | RI-03, RI-38 |
| **Cancao** | `isrc` | RI-04, RI-34 |
| | `duracao` | RI-05 |
| **VersaoAlbum** | `suporte` | RI-12 |
| | `ean13` | RI-13, RI-36 |
| | `designacao` | RI-39 |
| **DisponibilidadeLoja** | `dataInicio` | RI-14, RI-47 |
| | `unidades` | RI-15 |
| | `preco` | RI-16 |
| | `dataUltimaVenda` | RI-17 |
| **ItemCarrinho** | associação com VersaoAlbum | RI-46 |
| **Fatura** | `numero` | RI-28, RI-37 |
| | `data` | RI-27 |
| | `nifFaturacao`, `nomeFaturacao`, `moradaFaturacao` | RI-48 |
| **LinhaFatura** | `preco` | RI-16 |
| **Conta** | `username` | RI-18, RI-19 |
| | `email` | RI-20 |
| | `passwordHash` (validada antes de cifrar) | RI-21 |
| **Utilizador** | `nif` | RI-22 |
| | `genero` | RI-23 |
| | `dataNascimento` | RI-24 |
| | associação `favorito` | RI-40 |
| **ItemColecao** | `dataRegisto` | RI-25, RI-26 |
| | associação com VersaoAlbum | RI-41 |
| | associação `origem` com LinhaFatura | RI-51 |
| **ListaPersonalizada** | `nome` | RI-29, RI-30 |
| **ItemLista** | associação com Album | RI-42 |
| **PedidoNovaVersao** | `id` | RI-43 |
| | `estado` | RI-44, RI-45 |
| | `suporte` | RI-12 |
| | `ean13` | RI-13 |
| | `dataResposta` | RI-49 |
| **Notificacao** | `lida` | RI-50 |

Todas as restrições, da RI-01 à RI-51, estão associadas a pelo menos uma classe.
