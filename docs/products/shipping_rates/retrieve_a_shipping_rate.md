# Retrieve a shipping rate

Returns the shipping rate object with the given ID.

## Returns

Returns a shipping rate object if a valid identifier was provided.

```curl
curl https://api.stripe.com/v1/shipping_rates/shr_1MrRx2LkdIwHu7ixikgEA6Wd \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe shipping_rates retrieve shr_1MrRx2LkdIwHu7ixikgEA6Wd
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

shipping_rate = client.v1.shipping_rates.retrieve('shr_1MrRx2LkdIwHu7ixikgEA6Wd')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

shipping_rate = client.v1.shipping_rates.retrieve("shr_1MrRx2LkdIwHu7ixikgEA6Wd")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$shippingRate = $stripe->shippingRates->retrieve('shr_1MrRx2LkdIwHu7ixikgEA6Wd', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ShippingRateRetrieveParams params = ShippingRateRetrieveParams.builder().build();

ShippingRate shippingRate =
  client.v1().shippingRates().retrieve("shr_1MrRx2LkdIwHu7ixikgEA6Wd", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const shippingRate = await stripe.shippingRates.retrieve(
  'shr_1MrRx2LkdIwHu7ixikgEA6Wd'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.ShippingRateRetrieveParams{}
result, err := sc.V1ShippingRates.Retrieve(
  context.TODO(), "shr_1MrRx2LkdIwHu7ixikgEA6Wd", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.ShippingRates;
ShippingRate shippingRate = service.Get("shr_1MrRx2LkdIwHu7ixikgEA6Wd");
```

### Response

```json
{
  "id": "shr_1MrRx2LkdIwHu7ixikgEA6Wd",
  "object": "shipping_rate",
  "active": true,
  "created": 1680207604,
  "delivery_estimate": null,
  "display_name": "Ground shipping",
  "fixed_amount": {
    "amount": 500,
    "currency": "usd"
  },
  "livemode": false,
  "metadata": {},
  "tax_behavior": "unspecified",
  "tax_code": null,
  "type": "fixed_amount"
}
```