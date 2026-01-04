# Retrieve a ReservePlan

Retrieve a ReservePlan.

## Returns

Returns a ReservePlan object.

## Parameters

- `id` (string, required)
  The identifier of the ReservePlan to retrieve.

```curl
curl https://api.stripe.com/v1/reserve/plans/resplan_61SxrVOzQu6XIJSCx41Q8rCFhzAUW \
  -u "<<YOUR_SECRET_KEY>>" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"
```

```cli
stripe reserve plans retrieve resplan_61SxrVOzQu6XIJSCx41Q8rCFhzAUW \
  --stripe-account {{CONNECTED_ACCOUNT_ID}}
```

```ruby
# This example uses the beta SDK. See https://github.com/stripe/stripe-ruby#public-preview-sdks
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

plan = client.v1.reserve.plans.retrieve(
  'resplan_61SxrVOzQu6XIJSCx41Q8rCFhzAUW',
  {},
  {stripe_account: '{{CONNECTED_ACCOUNT_ID}}'},
)
```

```python
# This example uses the beta SDK. See https://github.com/stripe/stripe-python#public-preview-sdks
client = StripeClient("<<YOUR_SECRET_KEY>>")

plan = client.v1.reserve.plans.retrieve(
  "resplan_61SxrVOzQu6XIJSCx41Q8rCFhzAUW",
  options={"stripe_account": "{{CONNECTED_ACCOUNT_ID}}"},
)
```

```php
// This example uses the beta SDK. See https://github.com/stripe/stripe-php#public-preview-sdks
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$plan = $stripe->reserve->plans->retrieve(
  'resplan_61SxrVOzQu6XIJSCx41Q8rCFhzAUW',
  [],
  ['stripe_account' => '{{CONNECTED_ACCOUNT_ID}}']
);
```

```java
// This example uses the beta SDK. See https://github.com/stripe/stripe-java#public-preview-sdks
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PlanRetrieveParams params = PlanRetrieveParams.builder().build();

RequestOptions requestOptions =
  RequestOptions.builder()
    .setStripeAccount("{{CONNECTED_ACCOUNT_ID}}")
    .build();

Plan plan =
  client.v1().reserve().plans().retrieve(
    "resplan_61SxrVOzQu6XIJSCx41Q8rCFhzAUW",
    params,
    requestOptions
  );
```

```node
// This example uses the beta SDK. See https://github.com/stripe/stripe-node#public-preview-sdks
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const plan = await stripe.reserve.plans.retrieve(
  'resplan_61SxrVOzQu6XIJSCx41Q8rCFhzAUW',
  {
    stripeAccount: '{{CONNECTED_ACCOUNT_ID}}',
  }
);
```

```go
// This example uses the beta SDK. See https://github.com/stripe/stripe-go#public-preview-sdks
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.ReservePlanRetrieveParams{}
params.SetStripeAccount("{{CONNECTED_ACCOUNT_ID}}")
result, err := sc.V1ReservePlans.Retrieve(
  context.TODO(), "resplan_61SxrVOzQu6XIJSCx41Q8rCFhzAUW", params)
```

```dotnet
// This example uses the beta SDK. See https://github.com/stripe/stripe-dotnet#public-preview-sdks
var requestOptions = new RequestOptions
{
    StripeAccount = "{{CONNECTED_ACCOUNT_ID}}",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Reserve.Plans;
Stripe.Reserve.Plan plan = service.Get(
    "resplan_61SxrVOzQu6XIJSCx41Q8rCFhzAUW",
    null,
    requestOptions);
```

### Response

```json
{
  "id": "resplan_61SxrVOzQu6XIJSCx41Q8rCFhzAUW",
  "object": "reserve.plan",
  "created": 1753380438,
  "created_by": "application",
  "currency": "usd",
  "disabled_at": null,
  "livemode": false,
  "metadata": {},
  "percent": 15,
  "rolling_release": {
    "days_after_charge": 30,
    "expires_on": 1755972438
  },
  "status": "active",
  "type": "rolling_release"
}
```