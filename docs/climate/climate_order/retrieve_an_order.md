# Retrieve an order

Retrieves the details of a Climate order object with the given ID.

## Returns

Returns a Climate order object if a valid identifier was provided. Throws an error otherwise.

## Parameters

- `order` (string, required)
  Unique identifier of the order.

```curl
curl https://api.stripe.com/v1/climate/orders/climorder_1aTnU0B63jkB3XAQKUbA5yyl \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe climate orders retrieve climorder_1aTnU0B63jkB3XAQKUbA5yyl
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

order = client.v1.climate.orders.retrieve('climorder_1aTnU0B63jkB3XAQKUbA5yyl')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

order = client.v1.climate.orders.retrieve("climorder_1aTnU0B63jkB3XAQKUbA5yyl")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$order = $stripe->climate->orders->retrieve(
  'climorder_1aTnU0B63jkB3XAQKUbA5yyl',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

OrderRetrieveParams params = OrderRetrieveParams.builder().build();

Order order =
  client.v1().climate().orders().retrieve(
    "climorder_1aTnU0B63jkB3XAQKUbA5yyl",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const order = await stripe.climate.orders.retrieve(
  'climorder_1aTnU0B63jkB3XAQKUbA5yyl'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.ClimateOrderRetrieveParams{}
result, err := sc.V1ClimateOrders.Retrieve(
  context.TODO(), "climorder_1aTnU0B63jkB3XAQKUbA5yyl", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Climate.Orders;
Stripe.Climate.Order order = service.Get("climorder_1aTnU0B63jkB3XAQKUbA5yyl");
```

### Response

```json
{
  "id": "climorder_1aTnU0B63jkB3XAQKUbA5yyl",
  "object": "climate.order",
  "amount_fees": 17,
  "amount_subtotal": 550,
  "amount_total": 567,
  "beneficiary": {
    "public_name": "{{YOUR_BUSINESS_NAME}}"
  },
  "canceled_at": null,
  "cancellation_reason": null,
  "certificate": null,
  "confirmed_at": 1881439205,
  "created": 1881439205,
  "currency": "usd",
  "delayed_at": null,
  "delivered_at": null,
  "delivery_details": [],
  "expected_delivery_year": 2027,
  "livemode": false,
  "metadata": {},
  "metric_tons": "0.01",
  "product": "climsku_frontier_offtake_portfolio_2027",
  "product_substituted_at": null,
  "status": "confirmed"
}
```