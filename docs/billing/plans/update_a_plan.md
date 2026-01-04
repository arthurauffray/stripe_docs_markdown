# Update a plan

Updates the specified plan by setting the values of the parameters passed. Any parameters not provided are left unchanged. By design, you cannot change a plan’s ID, amount, currency, or billing cycle.

## Returns

The updated plan object is returned upon success. Otherwise, this call raises [an error](https://docs.stripe.com/api/plans/update.md#errors).

## Parameters

- `active` (boolean, optional)
  Whether the plan is currently available for new subscriptions.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `nickname` (string, optional)
  A brief description of the plan, hidden from customers.

- `product` (string, optional)
  The product the plan belongs to. This cannot be changed once it has been used in a subscription or subscription schedule.

- `trial_period_days` (integer, optional)
  Default number of trial days when subscribing a customer to this plan using [`trial_from_plan=true`](https://docs.stripe.com/docs/api.md#create_subscription-trial_from_plan).

```curl
curl https://api.stripe.com/v1/plans/plan_NjpIbv3g3ZibnD \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
```

```cli
stripe plans update plan_NjpIbv3g3ZibnD \
  -d "metadata[order_id]"=6735
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

plan = client.v1.plans.update('plan_NjpIbv3g3ZibnD', {metadata: {order_id: '6735'}})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

plan = client.v1.plans.update(
  "plan_NjpIbv3g3ZibnD",
  {"metadata": {"order_id": "6735"}},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$plan = $stripe->plans->update(
  'plan_NjpIbv3g3ZibnD',
  ['metadata' => ['order_id' => '6735']]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PlanUpdateParams params =
  PlanUpdateParams.builder().putMetadata("order_id", "6735").build();

Plan plan = client.v1().plans().update("plan_NjpIbv3g3ZibnD", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const plan = await stripe.plans.update(
  'plan_NjpIbv3g3ZibnD',
  {
    metadata: {
      order_id: '6735',
    },
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PlanUpdateParams{}
params.AddMetadata("order_id", "6735")
result, err := sc.V1Plans.Update(context.TODO(), "plan_NjpIbv3g3ZibnD", params)
```

```dotnet
var options = new PlanUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Plans;
Plan plan = service.Update("plan_NjpIbv3g3ZibnD", options);
```

### Response

```json
{
  "id": "plan_NjpIbv3g3ZibnD",
  "object": "plan",
  "active": true,
  "amount": 1200,
  "amount_decimal": "1200",
  "billing_scheme": "per_unit",
  "created": 1681851647,
  "currency": "usd",
  "interval": "month",
  "interval_count": 1,
  "livemode": false,
  "metadata": {
    "order_id": "6735"
  },
  "nickname": null,
  "product": "prod_NjpI7DbZx6AlWQ",
  "tiers_mode": null,
  "transform_usage": null,
  "trial_period_days": null,
  "usage_type": "licensed"
}
```