# Delete a plan

Deleting plans means new subscribers can’t be added. Existing subscribers aren’t affected.

## Returns

An object with the deleted plan’s ID and a deleted flag upon success. Otherwise, this call raises [an error](https://docs.stripe.com/api/plans/delete.md#errors), such as if the plan has already been deleted.

```curl
curl -X DELETE https://api.stripe.com/v1/plans/plan_NjpIbv3g3ZibnD \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe plans delete plan_NjpIbv3g3ZibnD
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

deleted = client.v1.plans.delete('plan_NjpIbv3g3ZibnD')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

deleted = client.v1.plans.delete("plan_NjpIbv3g3ZibnD")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$deleted = $stripe->plans->delete('plan_NjpIbv3g3ZibnD', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

Plan plan = client.v1().plans().delete("plan_NjpIbv3g3ZibnD");
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const deleted = await stripe.plans.del('plan_NjpIbv3g3ZibnD');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PlanDeleteParams{}
result, err := sc.V1Plans.Delete(context.TODO(), "plan_NjpIbv3g3ZibnD", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Plans;
Plan deleted = service.Delete("plan_NjpIbv3g3ZibnD");
```

### Response

```json
{
  "id": "plan_NjpIbv3g3ZibnD",
  "object": "plan",
  "deleted": true
}
```