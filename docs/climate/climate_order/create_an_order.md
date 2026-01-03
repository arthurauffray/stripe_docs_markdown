# Create an order

Creates a Climate order object for a given Climate product. The order will be processed immediately after creation and payment will be deducted your Stripe balance.

## Returns

The new Climate order object.

## Parameters

- `product` (string, required)
  Unique identifier of the Climate product.

- `amount` (integer, optional)
  Requested amount of carbon removal units. Either this or `metric_tons` must be specified.

- `beneficiary` (object, optional)
  Publicly sharable reference for the end beneficiary of carbon removal. Assumed to be the Stripe account if not set.

  - `beneficiary.public_name` (string, required)
    Publicly displayable name for the end beneficiary of carbon removal.

- `currency` (string, optional)
  Request currency for the order as a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a supported [settlement currency for your account](https://stripe.com/docs/currencies). If omitted, the account’s default currency will be used.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `metric_tons` (string, optional)
  Requested number of tons for the order. Either this or `amount` must be specified.

```curl
curl https://api.stripe.com/v1/climate/orders \
  -u "<<YOUR_SECRET_KEY>>" \
  -d metric_tons="0.01" \
  -d product=climsku_frontier_offtake_portfolio_2027
```

```cli
stripe climate orders create  \
  --metric-tons="0.01" \
  --product=climsku_frontier_offtake_portfolio_2027
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

order = client.v1.climate.orders.create({
  metric_tons: '0.01',
  product: 'climsku_frontier_offtake_portfolio_2027',
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

order = client.v1.climate.orders.create({
  "metric_tons": "0.01",
  "product": "climsku_frontier_offtake_portfolio_2027",
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$order = $stripe->climate->orders->create([
  'metric_tons' => '0.01',
  'product' => 'climsku_frontier_offtake_portfolio_2027',
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

OrderCreateParams params =
  OrderCreateParams.builder()
    .setMetricTons(new BigDecimal("0.01"))
    .setProduct("climsku_frontier_offtake_portfolio_2027")
    .build();

Order order = client.v1().climate().orders().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const order = await stripe.climate.orders.create({
  metric_tons: '0.01',
  product: 'climsku_frontier_offtake_portfolio_2027',
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.ClimateOrderCreateParams{
  MetricTons: stripe.Float64(0.01),
  Product: stripe.String("climsku_frontier_offtake_portfolio_2027"),
}
result, err := sc.V1ClimateOrders.Create(context.TODO(), params)
```

```dotnet
var options = new Stripe.Climate.OrderCreateOptions
{
    MetricTons = 0.01M,
    Product = "climsku_frontier_offtake_portfolio_2027",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Climate.Orders;
Stripe.Climate.Order order = service.Create(options);
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