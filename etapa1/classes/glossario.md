# Glossário de entidades

**Responsável:** Rodrigo · **Versão:** v2 (29/out)

Este glossário define os nomes que **toda a equipa** usa nos casos de uso, atividades, esboços, restrições e relatório. Se precisarem de uma entidade ou atributo que não esteja aqui, falem com o Rodrigo antes de o inventar.

Convenções:
- Classes em PascalCase sem acentos (`VersaoAlbum`); atributos em camelCase (`anoLancamento`).
- `[0..1]` = atributo opcional.
- RI-xx = restrição de integridade do enunciado (secção 3).

---

## Catálogo

| Entidade | Descrição | Atributos | RIs |
|---|---|---|---|
| **Artista** | Quem interpreta canções e álbuns. É um `Solista` ou um `Grupo`. | `isni` (identificador, 16 dígitos), `nome`, `anoInicioAtividade` | RI-07, RI-08 |
| **Solista** | Artista individual. Pode ser membro de grupos. | (herda de Artista) | — |
| **Grupo** | Artista com vários membros. Os membros só podem ser solistas (um grupo não contém grupos nem a si próprio). | (herda de Artista) | — |
| **Album** | Obra musical com uma sequência de faixas. Interpretado por no máximo um artista; as compilações não têm artista (mostram "Vários artistas"). | `mbid` (identificador, 36 carateres), `titulo`, `anoLancamento`, `tipo` (TipoAlbum), `imagemCapa` [0..1] (endereço da imagem no serviço de imagens) | RI-01, RI-02, RI-06, RI-09, RI-10, RI-11 |
| **Cancao** | Gravação musical, interpretada por um ou mais artistas. Pode aparecer em vários álbuns. | `isrc` (identificador, 12 carateres), `titulo`, `duracao` (segundos) | RI-04, RI-05 |
| **Faixa** | Posição de uma canção num álbum. | `numero` (1, 2, …) | RI-03 |
| **VersaoAlbum** | Um álbum num suporte físico e numa versão concreta (ex.: vinil vermelho). É o que se compra, coleciona e põe no carrinho. | `ean13` (identificador, 13 dígitos), `suporte` (SuporteFisico), `designacao` [0..1] | RI-12, RI-13 |

**Enumerações:**
- **TipoAlbum:** `single`, `EP`, `LP`
- **SuporteFisico:** `CD`, `vinil`, `cassete`

## Loja e vendas

| Entidade | Descrição | Atributos | RIs |
|---|---|---|---|
| **DisponibilidadeLoja** | Dados da versão na loja. Só existe se a versão alguma vez esteve à venda. | `dataInicio`, `unidades`, `preco`, `dataUltimaVenda` [0..1] (preenchida quando esgota; é a "data de fim de disponibilidade" da RI-17) | RI-14, RI-15, RI-16, RI-17, RI-47 |
| **ItemCarrinho** | Uma versão colocada no carrinho de compras de um utilizador. | `dataAdicao` (para ordenar, mais recente primeiro) | — |
| **Fatura** | Documento emitido quando um pagamento tem sucesso. Guarda uma cópia dos dados do comprador nesse momento, que não muda se o utilizador alterar o perfil ou apagar a conta. | `numero` (identificador, formato AAAA + sequencial, ex.: 20270001), `data`, `nifFaturacao`, `nomeFaturacao`, `moradaFaturacao` (Morada) | RI-27, RI-28, RI-37, RI-48 |
| **LinhaFatura** | Uma versão comprada numa fatura, com o preço praticado nesse momento. | `preco` | RI-16 |

## Utilizadores

| Entidade | Descrição | Atributos | RIs |
|---|---|---|---|
| **Conta** | Dados de acesso comuns a utilizadores e gestor. | `username` (identificador), `email` (único), `passwordHash` (palavra-passe cifrada) | RI-18 a RI-21 |
| **Utilizador** | Colecionador e potencial cliente da loja. | `nif`, `nome`, `genero` (Genero), `morada` (Morada), `dataNascimento` | RI-22, RI-23, RI-24 |
| **Gestor** | Gestor da loja. A conta já existe pré-configurada. | (herda de Conta) | — |
| **Morada** (tipo de dados) | Morada do utilizador, com coordenadas para o mapa. | `texto`, `latitude` [0..1], `longitude` [0..1] | — |

**Enumerações:**
- **Genero:** `feminino`, `masculino`

**Associações importantes:**
- Um utilizador tem **no máximo um** artista favorito.
- Uma fatura pertence a **zero ou um** utilizador (0..1): se a conta for apagada (RNF-16), a fatura mantém-se com a cópia dos dados de faturação.

## Coleções e listas

| Entidade | Descrição | Atributos | RIs |
|---|---|---|---|
| **ItemColecao** | Uma versão de álbum que o utilizador tem. Entra por adição manual ou automaticamente depois de uma compra; neste caso fica ligado (0..1) à **LinhaFatura** de origem. | `dataRegisto` | RI-25, RI-26, RI-41, RI-51 |
| **ListaPersonalizada** | Lista de álbuns criada pelo utilizador (ex.: "favoritos", "quero ter"). | `nome`, `dataUltimaModificacao` | RI-29, RI-30 |
| **ItemLista** | Um **álbum** (não uma versão) dentro de uma lista. | `dataAdicao` | — |

## Pedidos

| Entidade | Descrição | Atributos | RIs |
|---|---|---|---|
| **PedidoNovaVersao** | Pedido de um utilizador para acrescentar uma versão a um álbum existente. | `id` (identificador), `dataPedido`, `estado` (EstadoPedido), `ean13`, `suporte` (SuporteFisico), `designacao` [0..1], `dataResposta` [0..1] | RI-12, RI-13, RI-43, RI-44, RI-45, RI-49 |
| **Notificacao** | Aviso ao utilizador de que o seu pedido foi respondido. A resposta é o estado do pedido. | `dataEmissao`, `lida` (Boolean, para o contador do sino no dashboard) | RI-50 |

**Enumerações:**
- **EstadoPedido:** `emAnalise`, `aceite`, `recusado` (o enunciado também diz "rejeitado" na US24; ver pergunta P2 ao professor)

---

## Termos que **não** são entidades

- **Dashboard, pesquisa, estatísticas:** são ecrãs e consultas, calculados a partir das entidades acima. Não guardam dados próprios.
- **Pagamento:** é feito pelo serviço externo. Na base de dados só fica a `Fatura`, quando o pagamento tem sucesso.
- **Coleção:** é o conjunto dos `ItemColecao` de um utilizador; não há uma entidade "Colecao" separada.
- **Carrinho:** é o conjunto dos `ItemCarrinho` de um utilizador.
