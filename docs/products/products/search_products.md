# Search products

Search for products you’ve previously created using Stripe’s [Search Query Language](https://docs.stripe.com/docs/search.md#search-query-language). Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up to an hour behind during outages. Search functionality is not available to merchants in India.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` products. If no objects match the query, the resulting array will be empty. See the related guide on [expanding properties in lists](https://docs.stripe.com/docs/expand.md#lists).

## Parameters

- `query` (string, required)
  The search query string. See [search query language](https://docs.stripe.com/docs/search.md#search-query-language) and the list of supported [query fields for products](https://docs.stripe.com/docs/search.md#query-fields-for-products).

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `page` (string, optional)
  A cursor for pagination across multiple pages of results. Don’t include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.

```curl
curl -G https://api.stripe.com/v1/products/search \
  -u "<<YOUR_SECRET_KEY>>" \
  --data-urlencode query="active:'true' AND metadata['order_id']:'6735'"
```

```cli
stripe products search  \
  --query="active:'true' AND metadata['order_id']:'6735'"
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

products = client.v1.products.search({
  query: 'active:\'true\' AND metadata[\'order_id\']:\'6735\'',
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

products = client.v1.products.search({
  "query": "active:'true' AND metadata['order_id']:'6735'",
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$products = $stripe->products->search([
  'query' => 'active:\'true\' AND metadata[\'order_id\']:\'6735\'',
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ProductSearchParams params =
  ProductSearchParams.builder()
    .setQuery("active:'true' AND metadata['order_id']:'6735'")
    .build();

StripeSearchResult<Product> stripeSearchResult =
  client.v1().products().search(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const products = await stripe.products.search({
  query: 'active:\'true\' AND metadata[\'order_id\']:\'6735\'',
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.ProductSearchParams{
  SearchParams: stripe.SearchParams{
    Query: "active:'true' AND metadata['order_id']:'6735'",
  },
}
result := sc.V1Products.Search(context.TODO(), params)
```

```dotnet
var options = new ProductSearchOptions
{
    Query = "active:'true' AND metadata['order_id']:'6735'",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Products;
StripeSearchResult<Product> products = service.Search(options);
```

### Response

```json
{
  "object": "search_result",
  "url": "/v1/products/search",
  "has_more": false,
  "data": [
    {
      "id": "prod_NZOkxQ8eTZEHwN",
      "object": "product",
      "active": true,
      "created": 1679446501,
      "default_price": null,
      "description": null,
      "images": [],
      "livemode": false,
      "metadata": {
        "order_id": "6735"
      },
      "name": "Gold Plan",
      "package_dimensions": null,
      "shippable": null,
      "statement_descriptor": null,
      "tax_code": null,
      "unit_label": null,
      "updated": 1679446501,
      "url": null
    }
  ]
}
```