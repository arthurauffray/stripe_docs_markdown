# Retrieve a plan

Retrieves the plan with the given ID.

## Returns

Returns a plan if a valid plan ID was provided. Raises [an error](https://docs.stripe.com/api/plans/retrieve.md#errors) otherwise.

```curl
curl https://api.stripe.com/v1/plans/plan_NjpIbv3g3ZibnD \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe plans retrieve plan_NjpIbv3g3ZibnD
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

plan = client.v1.plans.retrieve('plan_NjpIbv3g3ZibnD')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

plan = client.v1.plans.retrieve("plan_NjpIbv3g3ZibnD")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$plan = $stripe->plans->retrieve('plan_NjpIbv3g3ZibnD', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PlanRetrieveParams params = PlanRetrieveParams.builder().build();

Plan plan = client.v1().plans().retrieve("plan_NjpIbv3g3ZibnD", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const plan = await stripe.plans.retrieve('plan_NjpIbv3g3ZibnD');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PlanRetrieveParams{}
result, err := sc.V1Plans.Retrieve(context.TODO(), "plan_NjpIbv3g3ZibnD", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Plans;
Plan plan = service.Get("plan_NjpIbv3g3ZibnD");
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
  "metadata": {},
  "nickname": null,
  "product": "prod_NjpI7DbZx6AlWQ",
  "tiers_mode": null,
  "transform_usage": null,
  "trial_period_days": null,
  "usage_type": "licensed"
}
```