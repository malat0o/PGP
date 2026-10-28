# Modelo de dados

*Secção do relatório da Etapa 1 · Autor: Rodrigo · Para entregar ao Reis até 4/nov*

> **Para o Reis:** as figuras estão em `etapa1/classes/img/`. Usem os ficheiros `.svg` no Word (não perdem qualidade) ou os `.png` se preferirem.

---

## 1. Objetivo

O modelo de dados define a informação que a aplicação web tem de guardar de forma persistente: as classes, os seus atributos, as associações entre elas e as restrições de integridade. Foi construído a partir do universo do discurso (secção 2 do enunciado), das restrições de integridade RI-01 a RI-30 e dos dados que as 29 user stories precisam de mostrar ou alterar.

Como o modelo completo não cabe numa página A4, foi dividido em cinco agrupamentos lógicos. A Figura 1 mostra a visão geral (só classes e associações, com os agrupamentos identificados por cores) e as Figuras 2 a 6 mostram cada agrupamento com os atributos e as restrições.

## 2. Visão geral

**Figura 1 — Diagrama de classes de topo** (`img/01-topo.svg`)

| Cor | Agrupamento | Classes |
|---|---|---|
| Azul | Catálogo | Artista, Solista, Grupo, Album, Cancao, Faixa, VersaoAlbum |
| Verde | Loja e vendas | DisponibilidadeLoja, ItemCarrinho, Fatura, LinhaFatura |
| Amarelo | Utilizadores | Conta, Utilizador, Gestor |
| Roxo | Coleções e listas | ItemColecao, ListaPersonalizada, ItemLista |
| Vermelho | Pedidos | PedidoNovaVersao, Notificacao |

A classe central do modelo é a **VersaoAlbum**: é a versão concreta de um álbum num suporte físico (identificada pelo código EAN-13) que o utilizador compra, coloca no carrinho e adiciona à coleção, e é a ela que se associam o stock e o preço na loja.

## 3. Agrupamentos

### 3.1 Catálogo

**Figura 2 — Catálogo** (`img/02-catalogo.svg`)

Representa a informação musical: artistas, álbuns, canções e versões físicas.

- **Artista** é uma classe abstrata com duas especializações, **Solista** e **Grupo**. Os membros de um grupo são representados pela associação `membros` entre Grupo e Solista; como esta associação só liga grupos a solistas, o próprio modelo garante que um grupo não pode ter outros grupos como membros, nem a si próprio.
- **Album** é interpretado por no máximo um artista (`0..1`). Os álbuns de compilação não têm artista associado e a aplicação mostra um texto por omissão, como "Vários artistas".
- **Cancao** é interpretada por um ou mais artistas e pode aparecer em vários álbuns. Por isso, a posição de uma canção num álbum é representada pela classe **Faixa**, que tem o número de ordem e liga um álbum a uma canção. Por exemplo, a canção "Last Resort" corresponde a uma faixa no álbum "Infest" e a outra faixa, com outro número, no álbum "Now 4".
- **VersaoAlbum** representa o álbum num suporte físico (CD, vinil ou cassete) e numa versão com designação própria (por exemplo, a cor do vinil). Cada álbum tem uma ou mais versões.

### 3.2 Loja e vendas

**Figura 3 — Loja e vendas** (`img/03-loja-vendas.svg`)

- **DisponibilidadeLoja** guarda, para cada versão que alguma vez esteve à venda, a data em que ficou disponível, o número de unidades, o preço e, quando esgota, a data da última venda. Por ser opcional (`0..1`), permite distinguir as três situações mostradas na página do álbum (US9): nunca esteve na loja (não existe), está disponível (unidades maiores que zero) e esgotou (zero unidades e data da última venda preenchida).
- **ItemCarrinho** representa uma versão colocada no carrinho, com a data de adição para mostrar os itens mais recentes primeiro (US27).
- **Fatura** é emitida quando o pagamento no serviço externo tem sucesso (US28). O número tem o ano seguido de um sequencial que recomeça em cada ano (por exemplo, 20270001). Cada fatura tem uma ou mais **LinhaFatura**, que guardam o preço pago por cada versão, uma vez que o preço na loja pode mudar depois da compra.

### 3.3 Utilizadores

**Figura 4 — Utilizadores** (`img/04-utilizadores.svg`)

- **Conta** é uma classe abstrata com os dados de acesso comuns: username, e-mail e palavra-passe. A palavra-passe é guardada cifrada (`passwordHash`), como recomenda a RNF-12.
- **Utilizador** acrescenta os dados pessoais: NIF, nome, género, morada e data de nascimento. A **Morada** é um tipo de dados com o texto e as coordenadas geográficas, que são opcionais porque só existem quando o serviço de geocodificação consegue converter a morada (US3).
- **Gestor** representa a conta do gestor da loja, que já existe pré-configurada.
- Cada utilizador pode ter no máximo um artista favorito (US7).

### 3.4 Coleções e listas

**Figura 5 — Coleções e listas** (`img/05-colecoes-listas.svg`)

- **ItemColecao** regista uma versão que o utilizador tem, com a data de registo. Os itens são criados por adição manual (US10) ou automaticamente depois de uma compra (US28).
- **ListaPersonalizada** tem um nome e a data da última modificação. Cada **ItemLista** liga a lista a um **álbum** (e não a uma versão), com a data de adição, porque as listas organizam álbuns independentemente das versões (US15, US17).

### 3.5 Pedidos

**Figura 6 — Pedidos** (`img/06-pedidos.svg`)

- **PedidoNovaVersao** guarda o pedido de um utilizador para acrescentar uma versão a um álbum existente: o identificador, a data, o estado e os dados da versão pedida (EAN-13, suporte físico e designação).
- O estado é **emAnalise** quando o pedido é criado e passa a **aceite** ou **recusado** quando o gestor responde (US24). Quando o pedido é aceite, é criada uma nova VersaoAlbum, que fica associada ao pedido.
- **Notificacao** é criada quando o pedido é respondido (US14). Está ligada ao pedido, de onde se obtêm o destinatário (o utilizador que fez o pedido) e a resposta (o estado).

## 4. Principais decisões de modelação

| Decisão | Justificação |
|---|---|
| Solista e Grupo como subclasses de Artista | O modelo impede, por construção, que um grupo tenha grupos como membros |
| Faixa como classe própria | A mesma canção pode estar em vários álbuns com números de faixa diferentes |
| Álbum com `0..1` artista | Os álbuns de compilação não têm artista (nota 10 do enunciado) |
| Álbum com `0..*` faixas | O registo de álbuns (US22) não inclui as canções, que podem ser importadas mais tarde |
| VersaoAlbum separada de Album | O que se compra, coleciona e põe no carrinho é uma versão concreta, identificada pelo EAN-13 |
| DisponibilidadeLoja separada e opcional | Distingue "nunca esteve na loja", "disponível" e "esgotado" (US9) |
| Preço guardado na LinhaFatura | A fatura tem de manter o preço pago, mesmo que o preço na loja mude |
| Coleção guarda versões, listas guardam álbuns | Segue a US10 e as US15/US17 |
| Conta como superclasse de Utilizador e Gestor | Ambos iniciam sessão; só o utilizador tem dados pessoais, coleção e compras |
| Palavra-passe cifrada | RNF-12; no perfil (US3) é mostrada mascarada |
| Notificação ligada ao pedido | Evita repetir o destinatário e a resposta, que já estão no pedido |

## 5. Suposições

1. O carrinho e as faturas não têm quantidades: cada linha corresponde a uma unidade de uma versão, porque o enunciado não refere quantidades.
2. O estado de um pedido recusado chama-se "recusado", como na US13 e na US14 (a US24 usa "rejeitado").
3. Os membros de um grupo são opcionais (`0..*`), porque o seu registo é uma funcionalidade extra (nota 11 do enunciado).

## 6. Restrições de integridade

As restrições RI-01 a RI-30 do enunciado estão representadas nas notas das classes a que se aplicam (Figuras 2 a 6). As restrições que envolvem várias classes são:

- **RI-06:** se um álbum é interpretado por um artista, esse artista interpreta todas as canções das faixas do álbum.
- **RI-10:** o ano de lançamento de um álbum é igual ou posterior ao ano de início de atividade do artista que o interpreta.
- **RI-11:** o ano de lançamento de um álbum é igual ou posterior ao ano de início de atividade de todos os artistas que interpretam as canções das suas faixas.
- **RI-14, RI-25, RI-27:** as datas de disponibilidade, de adição à coleção e das faturas não podem ser anteriores ao ano de lançamento do álbum.

Além das restrições do enunciado, foram identificadas 17 restrições novas (RI-31 a RI-47) a partir do universo do discurso, das notas de rodapé e dos critérios de aceitação das user stories. Também estão nas notas dos diagramas:

| ID | Restrição |
|---|---|
| RI-31 | Os membros de um grupo só podem ser artistas solistas. |
| RI-32 | Um álbum é interpretado por, no máximo, um artista. |
| RI-33 a RI-37 | MBID, ISRC, ISNI, EAN-13 e número da fatura identificam univocamente, respetivamente, o álbum, a canção, o artista, a versão e a fatura. |
| RI-38 | O número de faixa é único dentro de cada álbum. |
| RI-39 | Versões do mesmo álbum no mesmo suporte físico têm designações distintas. |
| RI-40 | Um utilizador tem, no máximo, um artista favorito. |
| RI-41 | Uma versão só pode constar uma vez na coleção de um utilizador. |
| RI-42 | Um álbum só pode constar uma vez em cada lista personalizada. |
| RI-43 | O identificador de um pedido é único. |
| RI-44 | O estado de um pedido é "em análise", "aceite" ou "recusado", e começa em "em análise". |
| RI-45 | Um pedido só pode ser aceite se o EAN-13 pedido ainda não existir. |
| RI-46 | Só se pode pôr no carrinho uma versão com unidades disponíveis na loja. |
| RI-47 | Uma versão registada com unidades tem de ter a data de início de disponibilidade preenchida. |

A origem de cada restrição e a sua associação às classes estão detalhadas em `etapa1/servicos/restricoes.md`.
