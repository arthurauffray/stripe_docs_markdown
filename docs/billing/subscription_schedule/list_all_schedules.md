# List all schedules

Retrieves the list of your subscription schedules.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` subscription schedules, starting after subscription schedule `starting_after`. Each entry in the array is a separate subscription schedule object. If no more subscription schedules are available, the resulting array will be empty.

## Parameters

- `canceled_at` (object, optional)
  Only return subscription schedules that were created canceled the given date interval.

  - `canceled_at.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `canceled_at.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `canceled_at.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `canceled_at.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `completed_at` (object, optional)
  Only return subscription schedules that completed during the given date interval.

  - `completed_at.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `completed_at.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `completed_at.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `completed_at.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `created` (object, optional)
  Only return subscription schedules that were created during the given date interval.

  - `created.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `created.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `created.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `created.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `customer` (string, optional)
  Only return subscription schedules for the given customer.

- `customer_account` (string, optional)
  Only return subscription schedules for the given account.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `released_at` (object, optional)
  Only return subscription schedules that were released during the given date interval.

  - `released_at.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `released_at.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `released_at.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `released_at.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `scheduled` (boolean, optional)
  Only return subscription schedules that have not started yet.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/subscription_schedules \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe subscription_schedules list  \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

subscription_schedules = client.v1.subscription_schedules.list({limit: 3})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

subscription_schedules = client.v1.subscription_schedules.list({"limit": 3})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$subscriptionSchedules = $stripe->subscriptionSchedules->all(['limit' => 3]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

SubscriptionScheduleListParams params =
  SubscriptionScheduleListParams.builder().setLimit(3L).build();

StripeCollection<SubscriptionSchedule> stripeCollection =
  client.v1().subscriptionSchedules().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const subscriptionSchedules = await stripe.subscriptionSchedules.list({
  limit: 3,
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.SubscriptionScheduleListParams{}
params.Limit = stripe.Int64(3)
result := sc.V1SubscriptionSchedules.List(context.TODO(), params)
```

```dotnet
var options = new SubscriptionScheduleListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.SubscriptionSchedules;
StripeList<SubscriptionSchedule> subscriptionSchedules = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/subscription_schedules",
  "has_more": false,
  "data": [
    {
      "id": "sub_sched_1Mr3YdLkdIwHu7ixjop3qtff",
      "object": "subscription_schedule",
      "application": null,
      "canceled_at": null,
      "completed_at": null,
      "created": 1724058651,
      "current_phase": null,
      "customer": "cus_NcI8FsMbh0OeFs",
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
          "end_date": 1818666418,
          "invoice_settings": null,
          "items": [
            {
              "discounts": null,
              "metadata": {},
              "plan": "price_1Mr3YcLkdIwHu7ixYCFhXHNb",
              "price": "price_1Mr3YcLkdIwHu7ixYCFhXHNb",
              "quantity": 1,
              "tax_rates": []
            }
          ],
          "metadata": {},
          "on_behalf_of": null,
          "proration_behavior": "create_prorations",
          "start_date": 1787130418,
          "transfer_data": null,
          "trial_end": null
        }
      ],
      "released_at": null,
      "released_subscription": null,
      "renewal_interval": null,
      "status": "not_started",
      "subscription": null,
      "test_clock": null
    }
  ]
}
```