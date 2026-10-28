# Esboços da interface

*Secção do relatório da Etapa 1 · Autor: Miguel · Para entregar ao Reis até 4/nov*

> **Para o Reis:** as imagens estão em `etapa1/esbocos/img/` (PNG). A fonte é o ficheiro `esbocos.html`, que abre em qualquer browser.

---

## 1. Objetivo

Os esboços mostram como o utilizador e o gestor interagem com a aplicação web, e ajudam a perceber a complexidade das user stories antes de as implementar. Como pede o enunciado, o foco está nas funcionalidades mais complexas: as que juntam várias user stories no mesmo ecrã ou envolvem serviços externos.

Os esboços são de baixa fidelidade: mostram a estrutura, os dados e as ações de cada ecrã, mas não o aspeto gráfico final. Cada esboço tem notas numeradas que indicam a user story ou a restrição que justifica cada elemento.

| Figura | Ecrã | User stories |
|---|---|---|
| 12 | E01 · Página de álbum | US9, US10, US17, US25, US26 |
| 13 | E02 · Carrinho e pagamento | US27, US28 |
| 14 | E03 · Criar conta | US1 |
| 15 | E04 · Perfil | US3, US4 |
| 16 | E05 · Pesquisa | US5, US8 |
| 17 | E06 · Coleção | US11 |
| 18 | E07 · Pedidos e notificações | US12, US13, US14 |
| 19 | E08 · Registar álbum ou versão (gestor) | US22, US23 |
| 20 | E09 · Estatísticas (gestor) | US29 |
| 21 | E10 · Dashboard | US19, US2 |
| 22 | E11 · Página de álbum (telemóvel) | RNF-04 |
| 23 | E12 · Carrinho (telemóvel) | RNF-04, US27, US28 |

## 2. Ecrãs principais

**Página de álbum (E01).** É o ecrã mais complexo, porque junta cinco user stories. Mostra os dados do álbum, as faixas e uma tabela de versões. Para cada versão aparecem o EAN-13, o suporte, a designação (só quando há mais do que uma versão no mesmo suporte) e o estado na loja: disponível, esgotada (com a data da última venda) ou "nunca esteve disponível". Os botões "Coleção" e "Carrinho" atuam sobre a versão; o botão do carrinho só fica ativo se houver unidades. O gestor vê uma coluna adicional para alterar as unidades. O botão "Adicionar a uma lista" atua sobre o álbum, porque as listas guardam álbuns e não versões.

**Carrinho e pagamento (E02).** Os álbuns aparecem do mais recente para o mais antigo, com o total no fim. Ao pagar, o utilizador escolhe entre Stripe e PayPal e é redirecionado para a página segura do serviço. O esboço mostra também as mensagens de falha (com a opção de escolher outro serviço) e de sucesso (com o número da fatura).

**Criar conta e perfil (E03, E04).** Os requisitos do username e da palavra-passe estão sempre visíveis, e os erros aparecem junto ao campo. O campo da morada não tem sugestões automáticas, por causa da política de utilização do Nominatim. No perfil, a palavra-passe aparece mascarada e o mapa só aparece se a morada tiver coordenadas.

**Pesquisa (E05).** Um único campo serve para álbuns e artistas, com uma opção para escolher. As sugestões aparecem à medida que se escreve, e há uma mensagem própria quando não há resultados.

**Coleção (E06).** É uma tabela que se pode ordenar por qualquer coluna, com ligações para as páginas do álbum e do artista e um botão para remover.

**Pedidos e notificações (E07).** Lista de pedidos com filtro por estado, formulário para um pedido novo e painel de notificações. As notificações mostram os dados do pedido e a resposta.

**Ecrãs do gestor (E08, E09).** O formulário de registo alterna entre "novo álbum" e "nova versão de um álbum existente". A data de disponibilidade é preenchida automaticamente quando há unidades. As estatísticas mostram as três tabelas pedidas e um mapa com as moradas dos cinco maiores colecionadores.

## 3. Adaptação a telemóvel (RNF-04)

Os esboços E11 e E12 mostram como os dois ecrãs mais carregados se adaptam a ecrãs pequenos:
- as tabelas passam a **cartões empilhados**;
- as faixas ficam numa **secção que se expande**;
- o total do carrinho e o botão Pagar ficam numa **barra fixa** no fundo do ecrã.
