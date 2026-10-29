# Pesquisa de serviços externos

*Etapa 1 · Preços e condições consultados a 27/out/2026 (mapas, geocodificação, pagamentos) e a 29/out/2026 (imagens de capa, importação de faixas); ver fontes no fim*

A aplicação precisa de três serviços externos:

| Necessidade | User stories | Serviço escolhido | Alternativa comparada |
|---|---|---|---|
| Mostrar mapas | US3 (morada no perfil), US29 (moradas dos 5 maiores colecionadores) | **Leaflet + OpenStreetMap** | Google Maps, Mapbox |
| Converter moradas em coordenadas (geocodificação) | US3, US29 | **Nominatim** | Google Geocoding, Mapbox Geocoding |
| Pagamentos online | US28 (pagar o carrinho, escolhendo o serviço) | **Stripe** e **PayPal** (os dois) | — (comparados entre si) |
| Imagens de capa | US9 a) (mostrar a capa), US22 f) (associar a capa) | **Cloudinary** (armazenamento), com o **Cover Art Archive** para sugerir a capa | MongoDB (documento ou GridFS) |
| Importar faixas e canções em bloco | US9 b) (mostrar as faixas), nota 12 | **API do MusicBrainz** | Introdução manual pelo gestor |

---

## 1. Mapas

| Critério | **Leaflet + OpenStreetMap** ✅ | Google Maps JavaScript API | Mapbox GL JS |
|---|---|---|---|
| Custo | Gratuito | 10 000 carregamentos/mês grátis; depois 7 USD por 1000 | Cerca de 50 000 carregamentos/mês grátis; depois cerca de 5 USD por 1000 |
| Conta / cartão de crédito | Não precisa | Precisa de conta Google Cloud com faturação ativa | Precisa de conta e token |
| Código aberto (RNF-05) | Sim (Leaflet, licença BSD) | Não | Biblioteca com licença proprietária |
| Integração com Angular | Simples (há wrappers como `ngx-leaflet`) | Simples (`@angular/google-maps`) | Média |
| Funcionalidades necessárias | Mapa, marcadores e popups: chega para a US3 e a US29 | Tudo e muito mais | Tudo e muito mais |
| Condições | Atribuição "© OpenStreetMap" obrigatória; os mosaicos públicos do OSM são para uso moderado | Termos restritivos sobre guardar dados | Termos restritivos sobre guardar dados |

**Escolha: Leaflet + OpenStreetMap.** Vantagens:
- É gratuito, sem conta nem cartão de crédito, o que importa num projeto académico (RNF-15).
- É de código aberto, coerente com a RNF-05.
- As user stories só precisam de mostrar marcadores num mapa, e o Leaflet faz isso com poucas linhas de código. As funcionalidades extra do Google Maps e do Mapbox não seriam usadas.
- É a biblioteca sugerida no próprio enunciado (nota 9).

## 2. Geocodificação (morada → coordenadas)

| Critério | **Nominatim (OpenStreetMap)** ✅ | Google Geocoding API | Mapbox Geocoding |
|---|---|---|---|
| Custo | Gratuito | 10 000 pedidos/mês grátis; depois 5 USD por 1000 | 100 000 pedidos/mês grátis, **mas só para resultados temporários** |
| Guardar as coordenadas na base de dados | Permitido (licença ODbL, com atribuição) | Restrito pelos termos | Exige a modalidade "permanente", que é paga |
| Limite de utilização | 1 pedido por segundo, para toda a aplicação | Por quota | Por quota |
| Qualidade em Portugal | Boa para ruas e localidades | Muito boa | Boa |
| Conta | Não precisa (basta identificar a aplicação no User-Agent) | Conta Google Cloud com faturação | Conta e token |

**Escolha: Nominatim.** Vantagens:
- O modelo de dados guarda as coordenadas na Morada do utilizador. O Nominatim permite guardá-las; no Google e no Mapbox isso é restrito ou pago.
- A aplicação só geocodifica quando o utilizador cria a conta ou altera a morada (US1, US4). É muito pouco tráfego, bem dentro do limite de 1 pedido por segundo.
- É gratuito e é o serviço sugerido no enunciado (nota 9).

**Cuidados obrigatórios (política de utilização do Nominatim):**
- Fazer **um pedido por morada**, guardar o resultado e nunca repetir o mesmo pedido.
- **Não usar no preenchimento automático** do campo da morada, que é proibido pela política.
- Identificar a aplicação no cabeçalho User-Agent e mostrar a atribuição ao OpenStreetMap.
- A política pede para não enviar dados pessoais. Por isso envia-se **só a rua, o código postal e a localidade**, sem o nome do utilizador.
- Se o uso crescer, pode instalar-se uma instância própria do Nominatim. Fica como alternativa a considerar no planeamento da Etapa 2.

## 3. Pagamentos online

A US28 pede que o utilizador possa **escolher** um serviço externo de pagamentos e, se o pagamento falhar, escolher outro. Por isso a aplicação integra **dois serviços**, comparados aqui entre si.

| Critério | **Stripe** ✅ | **PayPal** ✅ |
|---|---|---|
| Taxa por transação (Portugal) | Cartões padrão do EEE: 1,5% + 0,25 € · cartões premium do EEE: 2,8% + 0,25 € | Pagamento com conta PayPal: 2,9% + 0,35 € · cartões (plano misto): 1,2% + 0,35 € |
| Mensalidade / configuração | Não tem | Não tem |
| Métodos de pagamento | Cartões, **MB WAY**, Apple Pay, Google Pay e outros | Saldo e conta PayPal, cartões |
| Modo de testes | Sim (chaves de teste e cartões de teste) | Sim (ambiente *sandbox*) |
| Integração com Node.js | SDK oficial `stripe` + página de pagamento alojada (Stripe Checkout) | SDK oficial e botões JavaScript |
| Confirmação do resultado (US28 c) | *Webhooks* que avisam o backend | *Webhooks* que avisam o backend |
| Documentação | Muito completa, com exemplos em Node.js | Completa |

**Escolha: Stripe como serviço principal e PayPal como alternativa.** Vantagens:
- **Stripe:**
  - Taxas mais baixas para cartões europeus.
  - Suporta **MB WAY**, muito usado em Portugal.
  - A página de pagamento alojada (Stripe Checkout) evita que a aplicação trate dados de cartão, o que ajuda na segurança (RNF-12).
  - Tem modo de testes completo e documentação considerada das melhores da área.
- **PayPal:**
  - É a opção para quem já tem conta PayPal e não quer introduzir dados do cartão.
  - Tem ambiente *sandbox* para testes.
- Os dois avisam o backend do resultado através de *webhooks*. Assim cumpre-se a US28 c), em que a aplicação espera pela confirmação do serviço externo antes de emitir a fatura.

**Nota para o desenvolvimento em PTIR:** durante o projeto usam-se apenas os modos de teste. Não há pagamentos reais nem custos.

---

## 4. Imagens de capa

A página de cada álbum mostra a imagem de capa (US9 a), e o gestor associa uma capa ao registar o álbum (US22 f). É preciso decidir **onde guardar as imagens** e **de onde podem vir**.

| Critério | **Cloudinary** ✅ | MongoDB (documento ou GridFS) | Cover Art Archive (só ligar) |
|---|---|---|---|
| O que é | Serviço de armazenamento e entrega de imagens | As imagens ficam na própria base de dados da aplicação | Arquivo público de capas, indexado pelo MBID |
| Custo | Plano gratuito com 25 créditos/mês; 1 crédito = 1 GB de armazenamento, 1 GB de tráfego ou 1000 transformações | Sem custo extra, mas ocupa o espaço da base de dados (o plano gratuito do MongoDB Atlas, M0, tem 512 MB) | Gratuito |
| Imagens enviadas pelo gestor (US22 f) | Sim | Sim (abaixo de 16 MB cabe num documento; acima disso usa-se GridFS) | Não: só tem as capas que a comunidade carregou |
| Miniaturas e tamanhos para telemóvel (RNF-04) | Gera automaticamente, por URL | Têm de ser feitas pela aplicação | 250, 500 e 1200 px |
| Entrega rápida (RNF-08) | CDN global | Passa pelo backend | Servido pelo Internet Archive |
| Dependência externa | Sim (conta gratuita) | Não | Sim; e nem todos os álbuns têm capa |
| Integração com Node.js | SDK oficial | Driver do MongoDB | Pedido HTTP ao URL `/release-group/{mbid}/front` |

**Escolha: Cloudinary para guardar as capas, com o Cover Art Archive para as sugerir.** Vantagens:
- O gestor pode carregar qualquer capa (US22 f), mesmo de edições que não estão no Cover Art Archive.
- O plano gratuito chega para o projeto: centenas de capas de 200 a 500 KB ocupam menos de 1 GB, enquanto o MongoDB Atlas gratuito tem só 512 MB para todos os dados.
- As miniaturas para listas e para telemóvel são geradas automaticamente, e a entrega por CDN ajuda o desempenho (RNF-08).
- Ao registar um álbum, a aplicação pode pedir ao Cover Art Archive a capa associada ao MBID e mostrá-la como **sugestão**; o gestor confirma antes de a guardar.

**Cuidados:**
- A documentação do Cover Art Archive não define a licença das imagens: os direitos pertencem aos titulares (normalmente as editoras). A aplicação usa a capa só para identificar o álbum que está à venda; a equipa deve confirmar com o professor se esta utilização é aceitável no âmbito do projeto.
- O Cover Art Archive não tem limite de pedidos definido, mas pode responder 503; a sugestão de capa não pode bloquear o registo do álbum.

## 5. Importar faixas e canções em bloco

Nenhuma user story obrigatória regista as canções, mas a US9 b) mostra as faixas de cada álbum. A nota 12 do enunciado sugere um script ou endpoint para registar as canções em bloco (suposição Q4 do relatório).

| Critério | **API do MusicBrainz** ✅ | Introdução manual pelo gestor |
|---|---|---|
| Custo | Gratuito | Gratuito, mas exige trabalho do gestor e user stories extra |
| Dados disponíveis | Faixas (número e título), duração, artistas e ISRC das gravações | Os que o gestor escrever |
| Ligação ao nosso modelo | O MBID do álbum é o identificador do MusicBrainz (o enunciado usa o MBID) | — |
| Licença | Os dados centrais (artistas, releases, gravações, faixas e ISRCs) são **CC0**, sem restrições; os dados complementares (tags, avaliações, anotações) são CC BY-NC-SA 3.0 e não são usados | — |
| Limites de utilização | Cerca de 1 pedido por segundo por IP; o User-Agent tem de identificar a aplicação e um contacto (ex.: `DiscoLoja/1.0 ( email@exemplo.pt )`); acima do limite responde 503 | — |
| Pedido usado | `GET /ws/2/release/{mbid}?inc=recordings+isrcs+artist-credits&fmt=json` | — |

**Escolha: API do MusicBrainz, num script de importação.** Vantagens:
- Usa o MBID que o modelo já guarda, por isso não é preciso procurar o álbum por título.
- Os dados de que precisamos são CC0 e podem ser usados sem restrições.
- Um álbum inteiro vem num só pedido, por isso o limite de 1 pedido por segundo não é problema para uma importação em bloco.
- Evita criar user stories extra para registar canções.

**Cuidados e pontos a decidir pela equipa:**
- No MusicBrainz, o **release group** corresponde ao nosso Album (tem o tipo single, EP ou LP) e o **release** corresponde a uma edição concreta, com código de barras, que é a nossa VersaoAlbum. As faixas pertencem a um release; o script tem de escolher um release do grupo para importar a lista de faixas.
- Nem todas as gravações têm ISRC no MusicBrainz, e no nosso modelo o ISRC identifica a canção (RI-34): essas canções não podem ser importadas automaticamente sem uma regra para esse caso.
- A duração vem em milissegundos e tem de ser convertida em segundos (RI-05).
- O script deve respeitar a política de utilização: um pedido por segundo, User-Agent identificado e sem consultas periódicas.

## 6. Impacto nos outros artefactos

- **Casos de uso (Reis):** atores externos "Serviço de Mapas (OpenStreetMap)", "Serviço de Geocodificação (Nominatim)" e "Serviço de Pagamentos (Stripe / PayPal)", ligados aos casos de uso das US3, US29 e US28.
- **Esboços (Miguel):**
  - o ecrã de pagamento mostra a escolha entre Stripe e PayPal;
  - os mapas mostram a atribuição "© OpenStreetMap";
  - o campo da morada não tem sugestões automáticas.
- **Atividades (Edson):** no fluxo de compra, o pagamento é feito na página do serviço externo e a confirmação chega por *webhook*.
- **Casos de uso (Reis):** o Cover Art Archive e o MusicBrainz ligam-se ao UC-18 (Gerir álbuns e versões): sugestão da capa e importação das faixas ao registar o álbum.
- **Modelo de dados:** `Album.imagemCapa` passa a guardar o endereço da imagem no Cloudinary.

## Fontes

- [Leaflet — exemplo de início rápido](https://leafletjs.com/examples/quick-start)
- [Política de utilização do Nominatim](https://operations.osmfoundation.org/policies/nominatim/)
- [Documentação da API de pesquisa do Nominatim](https://nominatim.org/release-docs/develop/api/Search)
- [Preços do Google Maps Platform (resumo)](https://developers.google.com/maps/billing/overview/)
- [Google Maps Platform — limites gratuitos por SKU](https://developers.google.com/maps/billing-and-pricing/pricing-categories)
- [Preços do Mapbox (análise de terceiros)](https://storerocket.io/learn/mapbox-pricing)
- [Preços do Stripe em Portugal](https://stripe.com/pt/pricing)
- [Stripe — MB WAY](https://docs.stripe.com/payments/mb-way)
- [Comissões para comerciantes PayPal (Portugal)](https://www.paypal.com/pt/webapps/mpp/merchant-fees)
- [Cover Art Archive — API](https://musicbrainz.org/doc/Cover_Art_Archive/API)
- [Cloudinary — planos e créditos](https://cloudinary.com/documentation/developer_onboarding_faq_credits)
- [MongoDB — GridFS](https://www.mongodb.com/docs/manual/core/gridfs/)
- [MongoDB Atlas — preços (M0 com 512 MB)](https://www.mongodb.com/pricing)
- [MusicBrainz API](https://musicbrainz.org/doc/MusicBrainz_API)
- [MusicBrainz API — limites de utilização](https://musicbrainz.org/doc/MusicBrainz_API/Rate_Limiting)
- [MusicBrainz — licença dos dados](https://musicbrainz.org/doc/About/Data_License)
- [MusicBrainz — dados centrais e complementares](https://musicbrainz.org/doc/MusicBrainz_Database)
