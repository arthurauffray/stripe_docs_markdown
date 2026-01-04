# Migrate a subscription

Upgrade the billing_mode of an existing subscription.

## Returns

The newly migrated `Subscription` object, if the call succeeded.

## Parameters

- `billing_mode` (object, required)
  Controls how prorations and invoices for subscriptions are calculated and orchestrated.

  - `billing_mode.type` (enum, required)
    Controls the calculation and orchestration of prorations and invoices for subscriptions.
Possible enum values:
    - `flexible`
      Supports more flexible calculation and orchestration options for subscriptions and invoices.

  - `billing_mode.flexible` (object, optional)
    Configure behavior for flexible billing mode.

    - `billing_mode.flexible.proration_discounts` (enum, optional)
      Controls how invoices and invoice items display proration amounts and discount amounts.
Possible enum values:
      - `included`
        Amounts are net of discounts, and discount amounts are zero.

      - `itemized`
        Amounts are gross of discounts, and discount amounts are accurate.

```curl
curl https://api.stripe.com/v1/subscriptions/sub_1MowQVLkdIwHu7ixeRlqHVzs/migrate \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "billing_mode[type]"=flexible
```

```cli
stripe subscriptions migrate sub_1MowQVLkdIwHu7ixeRlqHVzs \
  -d "billing_mode[type]"=flexible
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

subscription = client.v1.subscriptions.migrate(
  'sub_1MowQVLkdIwHu7ixeRlqHVzs',
  {billing_mode: {type: 'flexible'}},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

subscription = client.v1.subscriptions.migrate(
  "sub_1MowQVLkdIwHu7ixeRlqHVzs",
  {"billing_mode": {"type": "flexible"}},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$subscription = $stripe->subscriptions->migrate(
  'sub_1MowQVLkdIwHu7ixeRlqHVzs',
  ['billing_mode' => ['type' => 'flexible']]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

SubscriptionMigrateParams params =
  SubscriptionMigrateParams.builder()
    .setBillingMode(
      SubscriptionMigrateParams.BillingMode.builder()
        .setType(SubscriptionMigrateParams.BillingMode.Type.FLEXIBLE)
        .build()
    )
    .build();

Subscription subscription =
  client.v1().subscriptions().migrate("sub_1MowQVLkdIwHu7ixeRlqHVzs", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const subscription = await stripe.subscriptions.migrate(
  'sub_1MowQVLkdIwHu7ixeRlqHVzs',
  {
    billing_mode: {
      type: 'flexible',
    },
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.SubscriptionMigrateParams{
  BillingMode: &stripe.SubscriptionMigrateBillingModeParams{
    Type: stripe.String("flexible"),
  },
}
result, err := sc.V1Subscriptions.Migrate(
  context.TODO(), "sub_1MowQVLkdIwHu7ixeRlqHVzs", params)
```

```dotnet
var options = new SubscriptionMigrateOptions
{
    BillingMode = new SubscriptionBillingModeOptions { Type = "flexible" },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Subscriptions;
Subscription subscription = service.Migrate("sub_1MowQVLkdIwHu7ixeRlqHVzs", options);
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
  "billing_mode": "flexible",
  "billing_mode_details": {
    "updated_at": 1679609768
  },
  "billing_thresholds": null,
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
        "billing_thresholds": null,
        "created": 1679609768,
        "current_period_end": 1682288167,
        "current_period_start": 1679609767,
        "metadata": {},
        "plan": {
          "id": "price_1MowQULkdIwHu7ixraBm864M",
          "object": "plan",
          "active": true,
          "aggregate_usage": null,
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
            "aggregate_usage": null,
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
  "metadata": {
    "order_id": "6735"
  },
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