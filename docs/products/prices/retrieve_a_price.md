# Retrieve a price

Retrieves the price with the given ID.

## Returns

Returns a price if a valid price or plan ID was provided. Raises [an error](https://docs.stripe.com/api/prices/retrieve.md#errors) otherwise.

```curl
curl https://api.stripe.com/v1/prices/price_1MoBy5LkdIwHu7ixZhnattbh \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe prices retrieve price_1MoBy5LkdIwHu7ixZhnattbh
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

price = client.v1.prices.retrieve('price_1MoBy5LkdIwHu7ixZhnattbh')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

price = client.v1.prices.retrieve("price_1MoBy5LkdIwHu7ixZhnattbh")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$price = $stripe->prices->retrieve('price_1MoBy5LkdIwHu7ixZhnattbh', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PriceRetrieveParams params = PriceRetrieveParams.builder().build();

Price price =
  client.v1().prices().retrieve("price_1MoBy5LkdIwHu7ixZhnattbh", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const price = await stripe.prices.retrieve('price_1MoBy5LkdIwHu7ixZhnattbh');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PriceRetrieveParams{}
result, err := sc.V1Prices.Retrieve(
  context.TODO(), "price_1MoBy5LkdIwHu7ixZhnattbh", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Prices;
Price price = service.Get("price_1MoBy5LkdIwHu7ixZhnattbh");
```

### Response

```json
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
  "metadata": {},
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
```