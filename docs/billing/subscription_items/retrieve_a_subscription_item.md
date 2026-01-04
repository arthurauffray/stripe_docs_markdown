# Retrieve a subscription item

Retrieves the subscription item with the given ID.

## Returns

Returns a subscription item if a valid subscription item ID was provided. Raises [an error](https://docs.stripe.com/api/subscription_items/retrieve.md#errors) otherwise.

```curl
curl https://api.stripe.com/v1/subscription_items/si_NcLYdDxLHxlFo7 \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe subscription_items retrieve si_NcLYdDxLHxlFo7
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

subscription_item = client.v1.subscription_items.retrieve('si_NcLYdDxLHxlFo7')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

subscription_item = client.v1.subscription_items.retrieve("si_NcLYdDxLHxlFo7")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$subscriptionItem = $stripe->subscriptionItems->retrieve('si_NcLYdDxLHxlFo7', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

SubscriptionItemRetrieveParams params =
  SubscriptionItemRetrieveParams.builder().build();

SubscriptionItem subscriptionItem =
  client.v1().subscriptionItems().retrieve("si_NcLYdDxLHxlFo7", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const subscriptionItem = await stripe.subscriptionItems.retrieve(
  'si_NcLYdDxLHxlFo7'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.SubscriptionItemRetrieveParams{}
result, err := sc.V1SubscriptionItems.Retrieve(
  context.TODO(), "si_NcLYdDxLHxlFo7", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.SubscriptionItems;
SubscriptionItem subscriptionItem = service.Get("si_NcLYdDxLHxlFo7");
```

### Response

```json
{
  "id": "si_NcLYdDxLHxlFo7",
  "object": "subscription_item",
  "created": 1680126546,
  "metadata": {},
  "price": {
    "id": "price_1Mr6rdLkdIwHu7ixwPmiybbR",
    "object": "price",
    "active": true,
    "billing_scheme": "per_unit",
    "created": 1680126545,
    "currency": "usd",
    "custom_unit_amount": null,
    "discounts": null,
    "livemode": false,
    "lookup_key": null,
    "metadata": {},
    "nickname": null,
    "product": "prod_NcLYGKH0eY5b8s",
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
  },
  "quantity": 2,
  "subscription": "sub_1Mr6rbLkdIwHu7ix4Xm9Ahtd",
  "tax_rates": []
}
```