# Search prices

Search for prices you’ve previously created using Stripe’s [Search Query Language](https://docs.stripe.com/docs/search.md#search-query-language). Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up to an hour behind during outages. Search functionality is not available to merchants in India.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` prices. If no objects match the query, the resulting array will be empty. See the related guide on [expanding properties in lists](https://docs.stripe.com/docs/expand.md#lists).

## Parameters

- `query` (string, required)
  The search query string. See [search query language](https://docs.stripe.com/docs/search.md#search-query-language) and the list of supported [query fields for prices](https://docs.stripe.com/docs/search.md#query-fields-for-prices).

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `page` (string, optional)
  A cursor for pagination across multiple pages of results. Don’t include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.

```curl
curl -G https://api.stripe.com/v1/prices/search \
  -u "<<YOUR_SECRET_KEY>>" \
  --data-urlencode query="active:'true' AND metadata['order_id']:'6735'"
```

```cli
stripe prices search  \
  --query="active:'true' AND metadata['order_id']:'6735'"
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

prices = client.v1.prices.search({
  query: 'active:\'true\' AND metadata[\'order_id\']:\'6735\'',
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

prices = client.v1.prices.search({
  "query": "active:'true' AND metadata['order_id']:'6735'",
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$prices = $stripe->prices->search([
  'query' => 'active:\'true\' AND metadata[\'order_id\']:\'6735\'',
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PriceSearchParams params =
  PriceSearchParams.builder()
    .setQuery("active:'true' AND metadata['order_id']:'6735'")
    .build();

StripeSearchResult<Price> stripeSearchResult = client.v1().prices().search(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const prices = await stripe.prices.search({
  query: 'active:\'true\' AND metadata[\'order_id\']:\'6735\'',
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PriceSearchParams{
  SearchParams: stripe.SearchParams{
    Query: "active:'true' AND metadata['order_id']:'6735'",
  },
}
result := sc.V1Prices.Search(context.TODO(), params)
```

```dotnet
var options = new PriceSearchOptions
{
    Query = "active:'true' AND metadata['order_id']:'6735'",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Prices;
StripeSearchResult<Price> prices = service.Search(options);
```

### Response

```json
{
  "object": "search_result",
  "url": "/v1/prices/search",
  "has_more": false,
  "data": [
    {
      "id": "price_1MoBy5LkdIwHu7ixZhnattbh",
      "object": "price",
      "active": true,
      "billing_scheme": "per_unit",
      "created": 1679431181,
      "currency": "usd",
      "custom_unit_amount": null,
      "livemode": false,
      "lookup_key": null,
      "metadata": {
        "order_id": "6735"
      },
      "nickname": null,
      "product": "prod_NZKdYqrwEYx6iK",
      "recurring": {
        "interval": "month",
        "interval_count": 1,
        "trial_period_days": null,
        "usage_type": "licensed"
      },
      "tax_behavior": "unspecified",
      "tiers_mode": null,
      "transform_quantity": null,
      "type": "recurring",
      "unit_amount": 1000,
      "unit_amount_decimal": "1000"
    }
  ]
}
```