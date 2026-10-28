# Fluxos de trabalho (diagramas de atividades)

*Secção do relatório da Etapa 1 · Autor: Edson · Para entregar ao Reis até 4/nov*

> **Para o Reis:** as figuras estão em `etapa1/atividades/img/`. Usem os `.svg` no Word ou os `.png`.

---

## 1. Objetivo

Os diagramas de atividades mostram os passos dos fluxos de trabalho que a aplicação web tem de suportar e quem executa cada passo. Cada diagrama está dividido em raias, uma por ator: o utilizador, o gestor da loja, a aplicação web e os serviços externos (pagamentos e geocodificação).

Foram escolhidos os fluxos que envolvem vários atores ou várias user stories, porque são os mais difíceis de implementar e os que mais beneficiam de ser desenhados antes do desenvolvimento. O fluxo de compra, o mais complexo, foi representado num diagrama de alto nível, com o pagamento decomposto num diagrama de subatividade.

| Figura | Fluxo | User stories |
|---|---|---|
| 7 | Comprar álbuns (alto nível) | US8, US9, US26, US27, US28 |
| 8 | Pagar o carrinho (subatividade) | US28 |
| 9 | Pedido de nova versão de um álbum | US9, US10, US12, US13, US14, US24 |
| 10 | Criar conta e iniciar sessão | US1, US2, US19 |
| 11 | Gerir o catálogo | US20, US22, US25 |

## 2. Comprar álbuns

**Figura 7** (`img/01-comprar.svg`) e **Figura 8** (`img/01-1-pagar.svg`)

O utilizador pesquisa um álbum, abre a sua página, escolhe uma versão e, se estiver disponível na loja, coloca-a no carrinho. Pode repetir estes passos para vários álbuns e remover itens antes de pagar.

O pagamento (Figura 8) envolve o serviço externo escolhido pelo utilizador (Stripe ou PayPal):
1. A aplicação calcula o total e inicia o pagamento no serviço.
2. O utilizador introduz os dados de pagamento na página do serviço. Assim, a aplicação nunca trata os dados do cartão.
3. O serviço envia o resultado à aplicação, que espera por ele antes de continuar (US28 c).
4. **Se o pagamento tiver sucesso:** a aplicação emite a fatura, adiciona as versões à coleção do utilizador, desconta as unidades vendidas e, se tiver sido vendida a última unidade, regista a data da última venda (RI-17). No fim mostra um resumo.
5. **Se o pagamento falhar:** o utilizador pode tentar com outro serviço ou cancelar (US28 g).

## 3. Pedido de nova versão de um álbum

**Figura 9** (`img/02-pedido-nova-versao.svg`)

Este fluxo junta quatro user stories e três atores:
1. O utilizador escolhe um álbum e preenche os dados da nova versão. A aplicação valida o EAN-13 e o suporte físico (RI-12, RI-13) e guarda o pedido com o estado "em análise" (US12).
2. O gestor abre o pedido e decide. Se a versão for nova e interessante para a loja, a aplicação cria a versão no álbum e muda o estado para "aceite"; caso contrário, muda-o para "recusado" (US24).
3. Em ambos os casos é criada uma notificação, que o utilizador vê no dashboard (US14).
4. Se o pedido foi aceite, a nova versão aparece na página do álbum e o utilizador pode adicioná-la à coleção (US9, US10).

## 4. Criar conta e iniciar sessão

**Figura 10** (`img/03-conta-sessao.svg`)

Na criação de conta, a aplicação mostra os requisitos do username e da palavra-passe e valida os dados (RI-18 a RI-24). Se forem válidos:
- a palavra-passe é cifrada antes de ser guardada (RNF-12);
- a morada é enviada ao serviço de geocodificação.

Se a morada for encontrada, a conta é guardada com as coordenadas; caso contrário, é guardada sem elas, e o perfil não mostra o mapa (US3).

No início de sessão, se as credenciais estiverem erradas, a mensagem de erro é genérica e não revela se o username existe (US2 b). Se estiverem certas, a aplicação mostra o dashboard.

## 5. Gerir o catálogo

**Figura 11** (`img/04-gerir-catalogo.svg`)

O gestor regista o artista, se ainda não existir (US20). Depois regista um álbum novo, com a primeira versão, ou acrescenta uma versão a um álbum existente (US22). Se a versão for registada com unidades, a aplicação preenche automaticamente a data de início de disponibilidade (US22 g).

Mais tarde, na página do álbum, o gestor pode alterar as unidades de uma versão. Se for a primeira vez que essa versão é posta à venda, a aplicação pede o preço e regista a data de disponibilidade (US25 b).
