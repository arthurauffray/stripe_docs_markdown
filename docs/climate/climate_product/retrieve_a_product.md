# Retrieve a product

Retrieves the details of a Climate product with the given ID.

## Returns

Returns a Climate product object if a valid identifier was provided. Throws an error otherwise.

```curl
curl https://api.stripe.com/v1/climate/products/climsku_frontier_offtake_portfolio_2027 \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe climate products retrieve climsku_frontier_offtake_portfolio_2027
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

product = client.v1.climate.products.retrieve('climsku_frontier_offtake_portfolio_2027')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

product = client.v1.climate.products.retrieve(
  "climsku_frontier_offtake_portfolio_2027",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$product = $stripe->climate->products->retrieve(
  'climsku_frontier_offtake_portfolio_2027',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ProductRetrieveParams params = ProductRetrieveParams.builder().build();

Product product =
  client.v1().climate().products().retrieve(
    "climsku_frontier_offtake_portfolio_2027",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const product = await stripe.climate.products.retrieve(
  'climsku_frontier_offtake_portfolio_2027'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.ClimateProductRetrieveParams{}
result, err := sc.V1ClimateProducts.Retrieve(
  context.TODO(), "climsku_frontier_offtake_portfolio_2027", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Climate.Products;
Stripe.Climate.Product product = service.Get(
    "climsku_frontier_offtake_portfolio_2027");
```

### Response

```json
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
```