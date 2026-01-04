# Release a schedule

Releases the subscription schedule immediately, which will stop scheduling of its phases, but leave any existing subscription in place. A schedule can only be released if its status is `not_started` or `active`. If the subscription schedule is currently associated with a subscription, releasing it will remove its `subscription` property and set the subscription’s ID to the `released_subscription` property.

## Returns

The released `subscription_schedule` object. Its status will be `released`, `released_at` will be the current time, and `released_subscription` will be the ID of the subscription the subscription schedule managed prior to being released.

## Parameters

- `preserve_cancel_date` (boolean, optional)
  Keep any cancellation on the subscription that the schedule has set

```curl
curl -X POST https://api.stripe.com/v1/subscription_schedules/sub_sched_1Mr3hWLkdIwHu7ixA5zxZvNI/release \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe subscription_schedules release sub_sched_1Mr3hWLkdIwHu7ixA5zxZvNI
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

subscription_schedule = client.v1.subscription_schedules.release('sub_sched_1Mr3hWLkdIwHu7ixA5zxZvNI')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

subscription_schedule = client.v1.subscription_schedules.release(
  "sub_sched_1Mr3hWLkdIwHu7ixA5zxZvNI",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$subscriptionSchedule = $stripe->subscriptionSchedules->release(
  'sub_sched_1Mr3hWLkdIwHu7ixA5zxZvNI',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

SubscriptionScheduleReleaseParams params =
  SubscriptionScheduleReleaseParams.builder().build();

SubscriptionSchedule subscriptionSchedule =
  client.v1().subscriptionSchedules().release(
    "sub_sched_1Mr3hWLkdIwHu7ixA5zxZvNI",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const subscriptionSchedule = await stripe.subscriptionSchedules.release(
  'sub_sched_1Mr3hWLkdIwHu7ixA5zxZvNI'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.SubscriptionScheduleReleaseParams{}
result, err := sc.V1SubscriptionSchedules.Release(
  context.TODO(), "sub_sched_1Mr3hWLkdIwHu7ixA5zxZvNI", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.SubscriptionSchedules;
SubscriptionSchedule subscriptionSchedule = service.Release(
    "sub_sched_1Mr3hWLkdIwHu7ixA5zxZvNI");
```

### Response

```json
{
  "id": "sub_sched_1Mr3hWLkdIwHu7ixA5zxZvNI",
  "object": "subscription_schedule",
  "application": null,
  "canceled_at": null,
  "completed_at": null,
  "created": 1680114386,
  "current_phase": null,
  "customer": "cus_NcII9GZkTPAnor",
  "default_settings": {
    "application_fee_percent": null,
    "automatic_tax": {
      "enabled": false,
      "liability": null
    },
    "billing_cycle_anchor": "automatic",
    "collection_method": "charge_automatically",
    "default_payment_method": null,
    "default_source": null,
    "description": null,
    "invoice_settings": {
      "issuer": {
        "type": "self"
      }
    },
    "on_behalf_of": null,
    "transfer_data": null
  },
  "end_behavior": "release",
  "livemode": false,
  "metadata": {},
  "phases": [
    {
      "add_invoice_items": [],
      "application_fee_percent": null,
      "billing_cycle_anchor": null,
      "collection_method": null,
      "currency": "usd",
      "default_payment_method": null,
      "default_tax_rates": [],
      "description": null,
      "discounts": null,
      "end_date": 1712339228,
      "invoice_settings": null,
      "items": [
        {
          "metadata": {},
          "plan": "price_1Mr3hVLkdIwHu7ixWuJp9ew0",
          "price": "price_1Mr3hVLkdIwHu7ixWuJp9ew0",
          "quantity": 1,
          "tax_rates": []
        }
      ],
      "metadata": {},
      "on_behalf_of": null,
      "proration_behavior": "create_prorations",
      "start_date": 1680716828,
      "transfer_data": null,
      "trial_end": null
    }
  ],
  "released_at": 1680114386,
  "released_subscription": null,
  "renewal_interval": null,
  "status": "released",
  "subscription": null,
  "test_clock": null
}
```