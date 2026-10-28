# Pesquisa de serviços externos

*Etapa 1 · Preços e condições consultados a 27/out/2026 (ver fontes no fim)*

A aplicação precisa de três serviços externos:

| Necessidade | User stories | Serviço escolhido | Alternativa comparada |
|---|---|---|---|
| Mostrar mapas | US3 (morada no perfil), US29 (moradas dos 5 maiores colecionadores) | **Leaflet + OpenStreetMap** | Google Maps, Mapbox |
| Converter moradas em coordenadas (geocodificação) | US3, US29 | **Nominatim** | Google Geocoding, Mapbox Geocoding |
| Pagamentos online | US28 (pagar o carrinho, escolhendo o serviço) | **Stripe** e **PayPal** (os dois) | — (comparados entre si) |

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

## 4. Impacto nos outros artefactos

- **Casos de uso (Reis):** atores externos "Serviço de Mapas (OpenStreetMap)", "Serviço de Geocodificação (Nominatim)" e "Serviço de Pagamentos (Stripe / PayPal)", ligados aos casos de uso das US3, US29 e US28.
- **Esboços (Miguel):**
  - o ecrã de pagamento mostra a escolha entre Stripe e PayPal;
  - os mapas mostram a atribuição "© OpenStreetMap";
  - o campo da morada não tem sugestões automáticas.
- **Atividades (Edson):** no fluxo de compra, o pagamento é feito na página do serviço externo e a confirmação chega por *webhook*.

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
