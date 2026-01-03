# List orders

Lists all Climate order objects. The orders are returned sorted by creation date, with the most recently created orders appearing first.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` orders, starting after order `starting_after`. Each entry in the array is a separate order object. If no more orders are available, the resulting array is empty.

## Parameters

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/climate/orders \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe climate orders list  \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

orders = client.v1.climate.orders.list({limit: 3})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

orders = client.v1.climate.orders.list({"limit": 3})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$orders = $stripe->climate->orders->all(['limit' => 3]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

OrderListParams params = OrderListParams.builder().setLimit(3L).build();

StripeCollection<Order> stripeCollection =
  client.v1().climate().orders().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const orders = await stripe.climate.orders.list({
  limit: 3,
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.ClimateOrderListParams{}
params.Limit = stripe.Int64(3)
result := sc.V1ClimateOrders.List(context.TODO(), params)
```

```dotnet
var options = new Stripe.Climate.OrderListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Climate.Orders;
StripeList<Stripe.Climate.Order> orders = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/climate/orders",
  "has_more": false,
  "data": [
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
  ]
}
```