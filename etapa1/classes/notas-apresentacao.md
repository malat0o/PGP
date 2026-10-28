# Notas para a apresentação: modelo de dados

*Rodrigo · Cerca de 2–3 minutos*

## O que dizer (por esta ordem)

1. **Visão geral (Figura 1).** "O modelo tem 19 classes em 5 agrupamentos: catálogo, loja e vendas, utilizadores, coleções e listas, e pedidos. A classe central é a VersaoAlbum, porque é ela que se compra, coleciona e tem stock."
2. **Catálogo (Figura 2).** Destacar três decisões:
   - Solista e Grupo são subclasses de Artista, e os membros de um grupo só podem ser solistas.
   - A Faixa é uma classe própria, porque a mesma canção aparece em vários álbuns (exemplo do enunciado: "Last Resort").
   - O álbum separa-se das versões: o mesmo álbum pode existir em CD, em vinil e em várias edições.
3. **Loja (Figura 3).** A disponibilidade é opcional e distingue "nunca esteve na loja", "disponível" e "esgotado". A linha da fatura guarda o preço pago.
4. **Restrições.** As RI-01 a RI-30 estão nas notas de cada classe; as novas (RI-31 em diante) vieram das user stories.

## Perguntas prováveis e respostas

| Pergunta | Resposta |
|---|---|
| Porque é que o álbum pode não ter artista? | As compilações (ex.: "Now 4") têm canções de vários artistas; o enunciado diz que nesse caso o artista não é guardado. |
| Como garantem que um grupo não tem grupos como membros? | A associação `membros` liga Grupo a Solista, por isso um grupo nunca pode ter outro grupo como membro. |
| Porque é que a coleção guarda versões e as listas guardam álbuns? | A coleção regista o que o utilizador tem fisicamente (o CD ou o vinil); as listas, como "álbuns que gostaria de ter", são independentes das versões (US15). |
| Porque é que a disponibilidade é uma classe separada? | Nem todas as versões estiveram na loja; assim não ficam atributos vazios na versão e distinguem-se os três estados da US9. |
| Porque é que guardam o preço na fatura se ele já está na disponibilidade? | O preço na loja pode mudar; a fatura tem de guardar o preço pago no momento da compra. |
| Como mostram a palavra-passe no perfil se está cifrada? | Não se mostra: aparece mascarada. Guardá-la cifrada é exigido pela RNF-12. |
| Onde estão as coordenadas da morada? | No tipo de dados Morada; são opcionais porque nem todas as moradas podem ser geocodificadas (US3). |
| Porque é que o álbum pode ter zero faixas? | O registo do álbum pelo gestor (US22) não inclui as canções; as faixas são acrescentadas depois. |
| Quantas unidades se podem comprar de uma versão? | Assumimos uma por linha, porque o enunciado não fala de quantidades. |
| Como é que o utilizador recebe a notificação? | A notificação está ligada ao pedido, e o pedido ao utilizador que o fez. |
