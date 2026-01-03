# Search PaymentIntents

Search for PaymentIntents you’ve previously created using Stripe’s [Search Query Language](https://docs.stripe.com/docs/search.md#search-query-language). Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up to an hour behind during outages. Search functionality is not available to merchants in India.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` PaymentIntents. If no objects match the query, the resulting array will be empty. See the related guide on [expanding properties in lists](https://docs.stripe.com/docs/expand.md#lists).

## Parameters

- `query` (string, required)
  The search query string. See [search query language](https://docs.stripe.com/docs/search.md#search-query-language) and the list of supported [query fields for payment intents](https://docs.stripe.com/docs/search.md#query-fields-for-payment-intents).

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `page` (string, optional)
  A cursor for pagination across multiple pages of results. Don’t include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.

```curl
curl -G https://api.stripe.com/v1/payment_intents/search \
  -u "<<YOUR_SECRET_KEY>>" \
  -d query="amount>1000"
```

```cli
stripe payment_intents search  \
  --query="amount>1000"
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

payment_intents = client.v1.payment_intents.search({query: 'amount>1000'})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

payment_intents = client.v1.payment_intents.search({"query": "amount>1000"})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentIntents = $stripe->paymentIntents->search(['query' => 'amount>1000']);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PaymentIntentSearchParams params =
  PaymentIntentSearchParams.builder().setQuery("amount>1000").build();

StripeSearchResult<PaymentIntent> stripeSearchResult =
  client.v1().paymentIntents().search(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntents = await stripe.paymentIntents.search({
  query: 'amount>1000',
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PaymentIntentSearchParams{
  SearchParams: stripe.SearchParams{Query: "amount>1000"},
}
result := sc.V1PaymentIntents.Search(context.TODO(), params)
```

```dotnet
var options = new PaymentIntentSearchOptions { Query = "amount>1000" };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.PaymentIntents;
StripeSearchResult<PaymentIntent> paymentIntents = service.Search(options);
```

### Response

```json
{
  "object": "search_result",
  "url": "/v1/payment_intents/search",
  "has_more": false,
  "data": [
    {
      "id": "pi_3MtwBwLkdIwHu7ix28a3tqPa",
      "object": "payment_intent",
      "amount": 2000,
      "amount_capturable": 0,
      "amount_details": {
        "tip": {}
      },
      "amount_received": 0,
      "application": null,
      "application_fee_amount": null,
      "automatic_payment_methods": {
        "enabled": true
      },
      "canceled_at": null,
      "cancellation_reason": null,
      "capture_method": "automatic",
      "client_secret": "pi_3MtwBwLkdIwHu7ix28a3tqPa_secret_YrKJUKribcBjcG8HVhfZluoGH",
      "confirmation_method": "automatic",
      "created": 1680800504,
      "currency": "usd",
      "customer": null,
      "description": null,
      "last_payment_error": null,
      "latest_charge": null,
      "livemode": false,
      "metadata": {},
      "next_action": null,
      "on_behalf_of": null,
      "payment_method": null,
      "payment_method_options": {
        "card": {
          "installments": null,
          "mandate_options": null,
          "network": null,
          "request_three_d_secure": "automatic"
        },
        "link": {
          "persistent_token": null
        }
      },
      "payment_method_types": [
        "card",
        "link"
      ],
      "processing": null,
      "receipt_email": null,
      "review": null,
      "setup_future_usage": null,
      "shipping": null,
      "source": null,
      "statement_descriptor": null,
      "statement_descriptor_suffix": null,
      "status": "requires_payment_method",
      "transfer_data": null,
      "transfer_group": null
    }
  ]
}
```