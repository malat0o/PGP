# Modelo de dados: diagrama de classes

**Responsável:** Rodrigo · **Versão:** v1 (30/out) · Os nomes seguem o [glossário](glossario.md).

Os diagramas estão escritos em Mermaid: aparecem desenhados diretamente no GitHub. Para os passar para o draw.io: **Organizar → Inserir → Avançado → Mermaid**, colar o código do bloco e depois ajustar o layout e exportar em PNG/PDF para o relatório.

**Notação usada:**
- `«id»` = identificador (único); `«único»` = valor único mas não é o identificador.
- `[0..1]` = atributo opcional.
- Seta simples (`-->`) = associação navegável; losango cheio (`*--`) = composição (a parte não existe sem o todo); triângulo (`<|--`) = generalização.
- As restrições de integridade (RI-xx) aparecem em notas junto à classe a que se aplicam.

---

## 1. Diagrama de topo

Só classes e associações, sem atributos. As cores identificam os 5 agrupamentos.

| Cor | Agrupamento |
|---|---|
| 🟦 Azul | Catálogo |
| 🟩 Verde | Loja e vendas |
| 🟨 Amarelo | Utilizadores |
| 🟪 Roxo | Coleções e listas |
| 🟥 Vermelho | Pedidos |

```mermaid
classDiagram
  direction LR
  class Artista
  class Solista
  class Grupo
  class Album
  class Cancao
  class Faixa
  class VersaoAlbum
  class DisponibilidadeLoja
  class ItemCarrinho
  class Fatura
  class LinhaFatura
  class Conta
  class Utilizador
  class Gestor
  class ItemColecao
  class ListaPersonalizada
  class ItemLista
  class PedidoNovaVersao
  class Notificacao

  Artista <|-- Solista
  Artista <|-- Grupo
  Grupo "0..*" -- "0..*" Solista : membros
  Album "0..*" --> "0..1" Artista : interpretado por
  Cancao "0..*" --> "1..*" Artista : interpretada por
  Album "1" *-- "0..*" Faixa
  Faixa "0..*" --> "1" Cancao
  Album "1" *-- "1..*" VersaoAlbum

  VersaoAlbum "1" *-- "0..1" DisponibilidadeLoja
  Utilizador "1" *-- "0..*" ItemCarrinho
  ItemCarrinho "0..*" --> "1" VersaoAlbum
  Utilizador "1" -- "0..*" Fatura
  Fatura "1" *-- "1..*" LinhaFatura
  LinhaFatura "0..*" --> "1" VersaoAlbum

  Conta <|-- Utilizador
  Conta <|-- Gestor
  Utilizador "0..*" --> "0..1" Artista : favorito

  Utilizador "1" *-- "0..*" ItemColecao
  ItemColecao "0..*" --> "1" VersaoAlbum
  Utilizador "1" *-- "0..*" ListaPersonalizada
  ListaPersonalizada "1" *-- "0..*" ItemLista
  ItemLista "0..*" --> "1" Album

  Utilizador "1" -- "0..*" PedidoNovaVersao
  PedidoNovaVersao "0..*" --> "1" Album
  PedidoNovaVersao "0..1" --> "0..1" VersaoAlbum : versão criada
  PedidoNovaVersao "1" *-- "0..1" Notificacao

  style Artista fill:#dbeafe,stroke:#1d4ed8
  style Solista fill:#dbeafe,stroke:#1d4ed8
  style Grupo fill:#dbeafe,stroke:#1d4ed8
  style Album fill:#dbeafe,stroke:#1d4ed8
  style Cancao fill:#dbeafe,stroke:#1d4ed8
  style Faixa fill:#dbeafe,stroke:#1d4ed8
  style VersaoAlbum fill:#dbeafe,stroke:#1d4ed8
  style DisponibilidadeLoja fill:#dcfce7,stroke:#15803d
  style ItemCarrinho fill:#dcfce7,stroke:#15803d
  style Fatura fill:#dcfce7,stroke:#15803d
  style LinhaFatura fill:#dcfce7,stroke:#15803d
  style Conta fill:#fef9c3,stroke:#a16207
  style Utilizador fill:#fef9c3,stroke:#a16207
  style Gestor fill:#fef9c3,stroke:#a16207
  style ItemColecao fill:#f3e8ff,stroke:#7e22ce
  style ListaPersonalizada fill:#f3e8ff,stroke:#7e22ce
  style ItemLista fill:#f3e8ff,stroke:#7e22ce
  style PedidoNovaVersao fill:#fee2e2,stroke:#b91c1c
  style Notificacao fill:#fee2e2,stroke:#b91c1c
```

---

## 2. Catálogo

Artistas, álbuns, canções, faixas e versões físicas.

```mermaid
classDiagram
  direction TB
  class Artista {
    <<abstract>>
    isni : String «id»
    nome : String
    anoInicioAtividade : Integer
  }
  class Solista
  class Grupo
  class Album {
    mbid : String «id»
    titulo : String
    anoLancamento : Integer
    tipo : TipoAlbum
    imagemCapa : Imagem [0..1]
  }
  class Cancao {
    isrc : String «id»
    titulo : String
    duracao : Integer
  }
  class Faixa {
    numero : Integer
  }
  class VersaoAlbum {
    ean13 : String «id»
    suporte : SuporteFisico
    designacao : String [0..1]
  }
  class TipoAlbum {
    <<enumeration>>
    single
    EP
    LP
  }
  class SuporteFisico {
    <<enumeration>>
    CD
    vinil
    cassete
  }

  Artista <|-- Solista
  Artista <|-- Grupo
  Grupo "0..*" -- "0..*" Solista : membros
  Album "0..*" --> "0..1" Artista : interpretado por
  Cancao "0..*" --> "1..*" Artista : interpretada por
  Album "1" *-- "0..*" Faixa : faixas
  Faixa "0..*" --> "1" Cancao
  Album "1" *-- "1..*" VersaoAlbum : versões

  note for Artista "RI-07: isni tem 16 dígitos<br>RI-08: anoInicioAtividade entre 1900 e 2100<br>RI-35: isni único"
  note for Grupo "RI-31: membros só podem ser solistas"
  note for Album "RI-01: mbid tem 36 carateres<br>RI-02: tipo é single, EP ou LP<br>RI-09: anoLancamento entre 1900 e 2100<br>RI-06, RI-10, RI-11: coerência com os artistas<br>RI-32: no máximo 1 artista<br>RI-33: mbid único"
  note for Cancao "RI-04: isrc tem 12 carateres<br>RI-05: duracao (segundos) positiva<br>RI-34: isrc único"
  note for Faixa "RI-03: numero começa em 1<br>RI-38: numero único no álbum"
  note for VersaoAlbum "RI-12: suporte é CD, vinil ou cassete<br>RI-13: ean13 tem 13 dígitos<br>RI-36: ean13 único<br>RI-39: versões no mesmo suporte<br>com designações distintas"
```

**Restrições que envolvem várias classes (descritas no relatório, não cabem como nota):**
- **RI-06:** se o álbum tem artista, esse artista interpreta todas as canções das faixas do álbum.
- **RI-10:** `Album.anoLancamento` ≥ `anoInicioAtividade` do artista que o interpreta.
- **RI-11:** `Album.anoLancamento` ≥ `anoInicioAtividade` de todos os artistas das canções das faixas.

---

## 3. Loja e vendas

Stock e preço de cada versão, carrinho e faturas.

```mermaid
classDiagram
  direction LR
  class VersaoAlbum
  class Utilizador
  class DisponibilidadeLoja {
    dataInicio : Date
    unidades : Integer
    preco : Decimal
    dataUltimaVenda : Date [0..1]
  }
  class ItemCarrinho {
    dataAdicao : DateTime
  }
  class Fatura {
    numero : Integer «id»
    data : Date
  }
  class LinhaFatura {
    preco : Decimal
  }

  VersaoAlbum "1" *-- "0..1" DisponibilidadeLoja : disponibilidade
  Utilizador "1" *-- "0..*" ItemCarrinho : carrinho
  ItemCarrinho "0..*" --> "1" VersaoAlbum
  Utilizador "1" -- "0..*" Fatura : compras
  Fatura "1" *-- "1..*" LinhaFatura : linhas
  LinhaFatura "0..*" --> "1" VersaoAlbum

  note for DisponibilidadeLoja "RI-14: ano de dataInicio ≥ anoLancamento do álbum<br>RI-15: unidades ≥ 0<br>RI-16: preco positivo, com 2 casas decimais<br>RI-17: fim da disponibilidade = dataUltimaVenda<br>RI-47: dataInicio preenchida se houver unidades"
  note for Fatura "numero = ano + sequencial (ex.: 20270001)<br>RI-27: ano de data ≥ anoLancamento dos álbuns<br>RI-28: sequencial recomeça em 1 cada ano<br>RI-37: numero único"
  note for ItemCarrinho "RI-46: só versões com unidades disponíveis"

  style VersaoAlbum fill:#f1f5f9,stroke:#94a3b8
  style Utilizador fill:#f1f5f9,stroke:#94a3b8
```

As classes a cinzento pertencem a outros agrupamentos e aparecem só para mostrar as ligações.

---

## 4. Utilizadores

Contas de acesso, dados pessoais e artista favorito.

```mermaid
classDiagram
  direction TB
  class Conta {
    <<abstract>>
    username : String «id»
    email : String «único»
    passwordHash : String
  }
  class Utilizador {
    nif : String
    nome : String
    genero : Genero
    morada : Morada
    dataNascimento : Date
  }
  class Gestor
  class Morada {
    <<dataType>>
    texto : String
    latitude : Decimal [0..1]
    longitude : Decimal [0..1]
  }
  class Genero {
    <<enumeration>>
    feminino
    masculino
  }
  class Artista

  Conta <|-- Utilizador
  Conta <|-- Gestor
  Utilizador "0..*" --> "0..1" Artista : favorito

  note for Conta "RI-18, RI-20: username e email únicos<br>RI-19: username só com letras e dígitos<br>RI-21: palavra-passe com 8+ carateres,<br>1 maiúscula, 1 minúscula e 1 algarismo<br>(validada antes de ser cifrada)"
  note for Utilizador "RI-22: nif com 9 dígitos, positivo<br>RI-23: genero feminino ou masculino<br>RI-24: pelo menos 16 anos<br>RI-40: no máximo 1 artista favorito"

  style Artista fill:#f1f5f9,stroke:#94a3b8
```

---

## 5. Coleções e listas

A coleção guarda **versões** (o que o utilizador tem fisicamente); as listas guardam **álbuns** (independentemente da versão).

```mermaid
classDiagram
  direction LR
  class Utilizador
  class VersaoAlbum
  class Album
  class ItemColecao {
    dataRegisto : Date
  }
  class ListaPersonalizada {
    nome : String
    dataUltimaModificacao : DateTime
  }
  class ItemLista {
    dataAdicao : Date
  }

  Utilizador "1" *-- "0..*" ItemColecao : coleção
  ItemColecao "0..*" --> "1" VersaoAlbum
  Utilizador "1" *-- "0..*" ListaPersonalizada : listas
  ListaPersonalizada "1" *-- "0..*" ItemLista : álbuns
  ItemLista "0..*" --> "1" Album

  note for ItemColecao "RI-25: ano de dataRegisto ≥ anoLancamento do álbum<br>RI-26: dataRegisto ≥ data em que o utilizador fez 16 anos<br>RI-41: cada versão só uma vez por utilizador"
  note for ListaPersonalizada "RI-29: nome com no máximo 100 carateres<br>RI-30: nome único para cada utilizador"
  note for ItemLista "RI-42: cada álbum só uma vez por lista"

  style Utilizador fill:#f1f5f9,stroke:#94a3b8
  style VersaoAlbum fill:#f1f5f9,stroke:#94a3b8
  style Album fill:#f1f5f9,stroke:#94a3b8
```

---

## 6. Pedidos

Pedidos de novas versões e respetivas notificações.

```mermaid
classDiagram
  direction LR
  class Utilizador
  class Album
  class VersaoAlbum
  class PedidoNovaVersao {
    id : Integer «id»
    dataPedido : DateTime
    estado : EstadoPedido
    ean13 : String
    suporte : SuporteFisico
    designacao : String [0..1]
  }
  class EstadoPedido {
    <<enumeration>>
    emAnalise
    aceite
    recusado
  }
  class Notificacao {
    dataEmissao : DateTime
  }

  Utilizador "1" -- "0..*" PedidoNovaVersao : pedidos
  PedidoNovaVersao "0..*" --> "1" Album : álbum
  PedidoNovaVersao "0..1" --> "0..1" VersaoAlbum : versão criada
  PedidoNovaVersao "1" *-- "0..1" Notificacao : resposta

  note for PedidoNovaVersao "RI-12: suporte é CD, vinil ou cassete<br>RI-13: ean13 tem 13 dígitos<br>RI-43: id único<br>RI-44: estado inicial emAnalise<br>RI-45: só aceite se o ean13 ainda não existir"

  style Utilizador fill:#f1f5f9,stroke:#94a3b8
  style Album fill:#f1f5f9,stroke:#94a3b8
  style VersaoAlbum fill:#f1f5f9,stroke:#94a3b8
```

---

## 7. Decisões de modelação (para a secção "Modelo de dados" do relatório)

1. **Solista e Grupo como subclasses de Artista.** A associação `membros` liga `Grupo` a `Solista`, por isso o próprio modelo impede que um grupo tenha grupos como membros (ou a si próprio). A multiplicidade é `0..*` porque o registo de membros é uma funcionalidade extra (nota 11 do enunciado).
2. **Faixa como classe própria.** A mesma canção pode estar em vários álbuns (ex.: "Last Resort" em "Infest" e em "Now 4"), e o número da faixa depende do álbum. `Faixa` liga um álbum a uma canção numa posição.
3. **Álbum com `0..1` artista.** As compilações não têm artista (nota 10); a aplicação mostra "Vários artistas".
4. **Álbum com `0..*` faixas.** Nenhuma user story obrigatória regista canções (US22 regista o álbum sem faixas), por isso um álbum pode existir sem faixas até elas serem importadas (pergunta P4 ao professor).
5. **VersaoAlbum separada de Album.** O que se compra, coleciona e põe no carrinho é uma versão concreta (identificada pelo EAN-13), não o álbum abstrato.
6. **DisponibilidadeLoja separada de VersaoAlbum (`0..1`).** Distingue as três situações da US9: nunca esteve na loja (não existe), está disponível (`unidades > 0`) e esgotou (`unidades = 0` e `dataUltimaVenda` preenchida).
7. **LinhaFatura guarda o preço.** O preço da versão pode mudar depois; a fatura tem de guardar o preço pago.
8. **Coleção guarda versões, listas guardam álbuns.** É o que dizem a US10 ("adicionar uma versão à coleção") e a US15/US17 ("listas de álbuns, independentemente das versões").
9. **Conta como superclasse de Utilizador e Gestor.** Ambos iniciam sessão com username e palavra-passe; só o utilizador tem dados pessoais, coleção, listas, carrinho e pedidos.
10. **Morada como tipo de dados com coordenadas opcionais.** O enunciado pede coordenadas, mas a US3 só mostra o mapa "se for possível" geocodificar a morada.
11. **A palavra-passe é guardada cifrada (`passwordHash`).** Segue a RNF-12. A US3 pede para a mostrar no perfil, o que não é possível depois de cifrada (pergunta P3 ao professor); proposta: mostrar mascarada.
12. **Notificação ligada ao pedido.** O destinatário é o utilizador do pedido e a resposta é o estado do pedido, por isso não se repetem esses dados.
13. **Pedido aceite liga-se à versão criada.** Quando o gestor aceita (US24 c), cria-se uma `VersaoAlbum` com os dados do pedido e fica registada a ligação.

## 8. Pontos para alinhar com a equipa

**Restrições novas (RI-31 a RI-47).** Estão definidas, com a origem de cada uma, em [`etapa1/servicos/restricoes.md`](../servicos/restricoes.md), e já aparecem nas notas dos diagramas acima.

**Com todos (suposições a confirmar):**
- O carrinho e as faturas não têm quantidade: cada linha é uma unidade de uma versão, porque o enunciado não fala em quantidades.
- O nome do estado é `recusado` (US13/US14) e não `rejeitado` (US24), até o professor responder (P2).
