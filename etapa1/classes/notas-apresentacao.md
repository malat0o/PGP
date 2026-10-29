# Notas para a apresentação: modelo de dados

*Rodrigo · Cerca de 2–3 minutos*

## O que dizer (por esta ordem)

1. **Visão geral (Figura 1).** "O modelo tem 19 classes em 5 agrupamentos: catálogo, loja e vendas, utilizadores, coleções e listas, e pedidos. A classe central é a VersaoAlbum, porque é ela que se compra, coleciona e tem stock."
2. **Catálogo (Figura 2).** Destacar três decisões:
   - Solista e Grupo são subclasses de Artista, e os membros de um grupo só podem ser solistas.
   - A Faixa é uma classe própria, porque a mesma canção aparece em vários álbuns (exemplo do enunciado: "Last Resort").
   - O álbum separa-se das versões: o mesmo álbum pode existir em CD, em vinil e em várias edições.
3. **Loja (Figura 3).** A disponibilidade é opcional e distingue "nunca esteve na loja", "disponível" e "esgotado". A linha da fatura guarda o preço pago.
4. **Restrições.** As RI-01 a RI-30 estão nas notas de cada classe; as 21 novas (RI-31 a RI-51) vieram das user stories e de requisitos como a RNF-16. São 51 no total.
5. **Se houver tempo:** a fatura guarda uma cópia dos dados de faturação e sobrevive se a conta for apagada (Utilizador 0..1 do lado da fatura).

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
| Como é que o utilizador recebe a notificação? | A notificação está ligada ao pedido, e o pedido ao utilizador que o fez. O atributo `lida` permite mostrar no dashboard quantas há por ler. |
| Porque é que a fatura guarda o NIF, o nome e a morada, se já estão no utilizador? | A US28 d) exige esses dados na fatura e eles não podem mudar depois. Se o utilizador alterar o perfil ou apagar a conta (RNF-16), a fatura mantém os dados do momento da compra (RI-48). |
| Porque é que a ligação Utilizador–Fatura é 0..1? | Para se poder apagar a conta sem apagar as faturas. |
| Para que serve a ligação ItemColecao → LinhaFatura? | Distingue os álbuns comprados na loja dos adicionados à mão, o que é útil nas estatísticas (US29). |
| O que é a "data de fim de disponibilidade" da RI-17? | É a `dataUltimaVenda`: só é preenchida quando a versão esgota. |
| Porque é que o pedido tem `dataResposta`? | Para registar quando o gestor respondeu; só existe depois de o pedido ser aceite ou recusado (RI-49). |
| Onde ficam as imagens de capa? | O atributo `imagemCapa` guarda o endereço da imagem no Cloudinary; o Cover Art Archive sugere a capa pelo MBID. |
