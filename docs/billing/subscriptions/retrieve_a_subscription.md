# Retrieve a subscription

Retrieves the subscription with the given ID.

## Returns

Returns the subscription object.

```curl
curl https://api.stripe.com/v1/subscriptions/sub_1MowQVLkdIwHu7ixeRlqHVzs \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe subscriptions retrieve sub_1MowQVLkdIwHu7ixeRlqHVzs
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

subscription = client.v1.subscriptions.retrieve('sub_1MowQVLkdIwHu7ixeRlqHVzs')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

subscription = client.v1.subscriptions.retrieve("sub_1MowQVLkdIwHu7ixeRlqHVzs")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$subscription = $stripe->subscriptions->retrieve('sub_1MowQVLkdIwHu7ixeRlqHVzs', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

SubscriptionRetrieveParams params = SubscriptionRetrieveParams.builder().build();

Subscription subscription =
  client.v1().subscriptions().retrieve("sub_1MowQVLkdIwHu7ixeRlqHVzs", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const subscription = await stripe.subscriptions.retrieve(
  'sub_1MowQVLkdIwHu7ixeRlqHVzs'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.SubscriptionRetrieveParams{}
result, err := sc.V1Subscriptions.Retrieve(
  context.TODO(), "sub_1MowQVLkdIwHu7ixeRlqHVzs", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Subscriptions;
Subscription subscription = service.Get("sub_1MowQVLkdIwHu7ixeRlqHVzs");
```

### Response

```json
{
  "id": "sub_1MowQVLkdIwHu7ixeRlqHVzs",
  "object": "subscription",
  "application": null,
  "application_fee_percent": null,
  "automatic_tax": {
    "enabled": false,
    "liability": null
  },
  "billing_cycle_anchor": 1679609767,
  "cancel_at": null,
  "cancel_at_period_end": false,
  "canceled_at": null,
  "cancellation_details": {
    "comment": null,
    "feedback": null,
    "reason": null
  },
  "collection_method": "charge_automatically",
  "created": 1679609767,
  "currency": "usd",
  "customer": "cus_Na6dX7aXxi11N4",
  "days_until_due": null,
  "default_payment_method": null,
  "default_source": null,
  "default_tax_rates": [],
  "description": null,
  "discounts": null,
  "ended_at": null,
  "invoice_settings": {
    "issuer": {
      "type": "self"
    }
  },
  "items": {
    "object": "list",
    "data": [
      {
        "id": "si_Na6dzxczY5fwHx",
        "object": "subscription_item",
        "created": 1679609768,
        "current_period_end": 1682288167,
        "current_period_start": 1679609767,
        "metadata": {},
        "plan": {
          "id": "price_1MowQULkdIwHu7ixraBm864M",
          "object": "plan",
          "active": true,
          "amount": 1000,
          "amount_decimal": "1000",
          "billing_scheme": "per_unit",
          "created": 1679609766,
          "currency": "usd",
          "discounts": null,
          "interval": "month",
          "interval_count": 1,
          "livemode": false,
          "metadata": {},
          "nickname": null,
          "product": "prod_Na6dGcTsmU0I4R",
          "tiers_mode": null,
          "transform_usage": null,
          "trial_period_days": null,
          "usage_type": "licensed"
        },
        "price": {
          "id": "price_1MowQULkdIwHu7ixraBm864M",
          "object": "price",
          "active": true,
          "billing_scheme": "per_unit",
          "created": 1679609766,
          "currency": "usd",
          "custom_unit_amount": null,
          "livemode": false,
          "lookup_key": null,
          "metadata": {},
          "nickname": null,
          "product": "prod_Na6dGcTsmU0I4R",
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
        "quantity": 1,
        "subscription": "sub_1MowQVLkdIwHu7ixeRlqHVzs",
        "tax_rates": []
      }
    ],
    "has_more": false,
    "total_count": 1,
    "url": "/v1/subscription_items?subscription=sub_1MowQVLkdIwHu7ixeRlqHVzs"
  },
  "latest_invoice": "in_1MowQWLkdIwHu7ixuzkSPfKd",
  "livemode": false,
  "metadata": {},
  "next_pending_invoice_item_invoice": null,
  "on_behalf_of": null,
  "pause_collection": null,
  "payment_settings": {
    "payment_method_options": null,
    "payment_method_types": null,
    "save_default_payment_method": "off"
  },
  "pending_invoice_item_interval": null,
  "pending_setup_intent": null,
  "pending_update": null,
  "schedule": null,
  "start_date": 1679609767,
  "status": "active",
  "test_clock": null,
  "transfer_data": null,
  "trial_end": null,
  "trial_settings": {
    "end_behavior": {
      "missing_payment_method": "create_invoice"
    }
  },
  "trial_start": null
}
```