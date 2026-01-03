# List products

Lists all available Climate product objects.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` products, starting after product `starting_after`. Each entry in the array is a separate product object. If no more products are available, the resulting array is empty.

## Parameters

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/climate/products \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe climate products list  \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

products = client.v1.climate.products.list({limit: 3})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

products = client.v1.climate.products.list({"limit": 3})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$products = $stripe->climate->products->all(['limit' => 3]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ProductListParams params = ProductListParams.builder().setLimit(3L).build();

StripeCollection<Product> stripeCollection =
  client.v1().climate().products().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const products = await stripe.climate.products.list({
  limit: 3,
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.ClimateProductListParams{}
params.Limit = stripe.Int64(3)
result := sc.V1ClimateProducts.List(context.TODO(), params)
```

```dotnet
var options = new Stripe.Climate.ProductListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Climate.Products;
StripeList<Stripe.Climate.Product> products = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/climate/products",
  "has_more": false,
  "data": [
    {
      "id": "climsku_frontier_offtake_portfolio_2027",
      "object": "climate.product",
      "created": 1881439203,
      "current_prices_per_metric_ton": {
        "usd": {
          "amount_fees": 1650,
          "amount_subtotal": 55000,
          "amount_total": 56650
        }
      },
      "delivery_year": 2027,
      "livemode": false,
      "metric_tons_available": "18000",
      "name": "Frontier's 2027 offtake portfolio",
      "suppliers": [
        {
          "id": "climsup_charm_industrial",
          "object": "climate.supplier",
          "info_url": "https://frontierclimate.com/portfolio/charm-industrial",
          "livemode": false,
          "locations": [
            {
              "city": "San Francisco",
              "country": "US",
              "latitude": 37.7749,
              "longitude": -122.4194,
              "region": "CA"
            }
          ],
          "name": "Charm Industrial",
          "removal_pathway": "biomass_carbon_removal_and_storage"
        }
      ]
    }
  ]
}
```