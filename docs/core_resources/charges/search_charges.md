# Search charges

Search for charges you’ve previously created using Stripe’s [Search Query Language](https://docs.stripe.com/docs/search.md#search-query-language). Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up to an hour behind during outages. Search functionality is not available to merchants in India.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` charges. If no objects match the query, the resulting array will be empty. See the related guide on [expanding properties in lists](https://docs.stripe.com/docs/expand.md#lists).

## Parameters

- `query` (string, required)
  The search query string. See [search query language](https://docs.stripe.com/docs/search.md#search-query-language) and the list of supported [query fields for charges](https://docs.stripe.com/docs/search.md#query-fields-for-charges).

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `page` (string, optional)
  A cursor for pagination across multiple pages of results. Don’t include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.

```curl
curl -G https://api.stripe.com/v1/charges/search \
  -u "<<YOUR_SECRET_KEY>>" \
  --data-urlencode query="amount>999 AND metadata['order_id']:'6735'"
```

```cli
stripe charges search  \
  --query="amount>999 AND metadata['order_id']:'6735'"
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

charges = client.v1.charges.search({
  query: 'amount>999 AND metadata[\'order_id\']:\'6735\'',
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

charges = client.v1.charges.search({
  "query": "amount>999 AND metadata['order_id']:'6735'",
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$charges = $stripe->charges->search([
  'query' => 'amount>999 AND metadata[\'order_id\']:\'6735\'',
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ChargeSearchParams params =
  ChargeSearchParams.builder()
    .setQuery("amount>999 AND metadata['order_id']:'6735'")
    .build();

StripeSearchResult<Charge> stripeSearchResult = client.v1().charges().search(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const charges = await stripe.charges.search({
  query: 'amount>999 AND metadata[\'order_id\']:\'6735\'',
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.ChargeSearchParams{
  SearchParams: stripe.SearchParams{
    Query: "amount>999 AND metadata['order_id']:'6735'",
  },
}
result := sc.V1Charges.Search(context.TODO(), params)
```

```dotnet
var options = new ChargeSearchOptions
{
    Query = "amount>999 AND metadata['order_id']:'6735'",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Charges;
StripeSearchResult<Charge> charges = service.Search(options);
```

### Response

```json
{
  "object": "search_result",
  "url": "/v1/charges/search",
  "has_more": false,
  "data": [
    {
      "id": "ch_3MrVHGLkdIwHu7ix3VP9P8qH",
      "object": "charge",
      "amount": 1000,
      "amount_captured": 1000,
      "amount_refunded": 0,
      "application": null,
      "application_fee": null,
      "application_fee_amount": null,
      "balance_transaction": "txn_3MrVHGLkdIwHu7ix33fWgyw1",
      "billing_details": {
        "address": {
          "city": null,
          "country": null,
          "line1": null,
          "line2": null,
          "postal_code": null,
          "state": null
        },
        "email": null,
        "name": null,
        "phone": null
      },
      "calculated_statement_descriptor": "Stripe",
      "captured": true,
      "created": 1680220390,
      "currency": "usd",
      "customer": null,
      "description": null,
      "disputed": false,
      "failure_balance_transaction": null,
      "failure_code": null,
      "failure_message": null,
      "fraud_details": {},
      "livemode": false,
      "metadata": {
        "order_id": "6735"
      },
      "on_behalf_of": null,
      "outcome": {
        "network_status": "approved_by_network",
        "reason": null,
        "risk_level": "normal",
        "risk_score": 28,
        "seller_message": "Payment complete.",
        "type": "authorized"
      },
      "paid": true,
      "payment_intent": null,
      "payment_method": "card_1MrVHGLkdIwHu7ixi93aSYS2",
      "payment_method_details": {
        "card": {
          "brand": "visa",
          "checks": {
            "address_line1_check": null,
            "address_postal_code_check": null,
            "cvc_check": null
          },
          "country": "US",
          "exp_month": 3,
          "exp_year": 2024,
          "fingerprint": "mToisGZ01V71BCos",
          "funding": "credit",
          "installments": null,
          "last4": "4242",
          "mandate": null,
          "network": "visa",
          "network_token": {
            "used": false
          },
          "three_d_secure": null,
          "wallet": null
        },
        "type": "card"
      },
      "receipt_email": null,
      "receipt_number": null,
      "receipt_url": "https://pay.stripe.com/receipts/payment/CAcaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KOfBmKEGMgY6smXCZpA6LBZYyAwZTSPplSpB7KwcptJiKqQfv6nQiL75NRCxebjOIiABDK3odR96wc2r",
      "refunded": false,
      "review": null,
      "shipping": null,
      "source_transfer": null,
      "statement_descriptor": null,
      "statement_descriptor_suffix": null,
      "status": "succeeded",
      "transfer_data": null,
      "transfer_group": null
    }
  ]
}
```