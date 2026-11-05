# Perguntas ao professor (rascunho de email)

*Responsável: Reis · Enviar o mais cedo possível. Se o professor responder antes de 4/nov, atualizar a Tabela 19 do relatório (capítulo 7).*

---

**Assunto:** PGP 2026/27 · Grupo 12 · Dúvidas sobre o enunciado do projeto

Boa tarde, professor,

Ao fazer o desenho inicial da aplicação, encontrámos alguns pontos do enunciado que queríamos esclarecer:

1. **US28 f):** o critério está incompleto ("Caso tenha sido vendida a última unidade de algum álbum, deve"). Assumimos que se regista a data da última venda dessa versão (RI-17). Está correto?
2. **Estado dos pedidos:** as US13 e US14 usam "recusado" e a US24 usa "rejeitado". Podemos usar apenas "recusado"?
3. **Palavra-passe no perfil (US3 a):** a US3 pede para mostrar a palavra-passe, mas a RNF-12 recomenda guardá-la cifrada, o que impede mostrá-la. Podemos mostrá-la mascarada?
4. **Canções e faixas:** nenhuma user story obrigatória regista as canções, mas a US9 mostra as faixas. Podemos fazer a importação em bloco por script ou endpoint, como sugere a nota 12?

Obrigado,
Grupo 12 (Rodrigo, Reis, Miguel, Ze, Edson)

---

## Resposta do professor sobre os diagramas (pergunta de outro grupo, partilhada)

- **Casos de uso:** se não couberem numa página A4, desenha-se um diagrama por agrupamento lógico (por exemplo, compra de álbuns) e um **diagrama de topo com packages**, um por agrupamento, com os atores envolvidos em cada package (exemplo: figura 3 de "UML Use Case Diagrams: An Agile Introduction", primeiro link da nota 17 do enunciado).
- **Atividades:** nem um só diagrama para todos os fluxos, nem um por user story. Cada diagrama é um fluxo de trabalho, que pode abranger várias user stories (como a compra numa loja do enunciado). Os fluxos não devem ter quebras.

**O que mudámos:** os casos de uso passaram a ter um diagrama de topo com 6 packages (Figura 1) e um diagrama por package (Figuras 2 a 7). No capítulo dos fluxos, o relatório explica como os diagramas se encadeiam sem quebras.

## Enunciado atualizado (versão de 4 de novembro de 2026)

- **US24 d):** passou a dizer "recusado" → resolve a pergunta 2 (como assumimos).
- **US28 f):** completada: quando se vende a última unidade de uma versão, a data de fim de disponibilidade é atualizada segundo a RI-17 → resolve a pergunta 1 (como assumimos).
- **Diagrama de casos de uso:** o texto do enunciado passou a incluir a indicação dos packages, que já seguimos.

As perguntas 3 e 4 continuam por responder.
