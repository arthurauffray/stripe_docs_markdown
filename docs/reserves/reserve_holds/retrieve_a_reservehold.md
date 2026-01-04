# Retrieve a ReserveHold

Retrieve a ReserveHold.

## Returns

Returns a ReserveHold object.

## Parameters

- `id` (string, required)
  The identifier of the ReserveHold to retrieve.

```curl
curl https://api.stripe.com/v1/reserve/holds/reshold_61SxrUZH1aQJj97WT41Q8rCFhzAUW \
  -u "<<YOUR_SECRET_KEY>>" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"
```

```cli
stripe reserve holds retrieve reshold_61SxrUZH1aQJj97WT41Q8rCFhzAUW \
  --stripe-account {{CONNECTED_ACCOUNT_ID}}
```

```ruby
# This example uses the beta SDK. See https://github.com/stripe/stripe-ruby#public-preview-sdks
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

hold = client.v1.reserve.holds.retrieve(
  'reshold_61SxrUZH1aQJj97WT41Q8rCFhzAUW',
  {},
  {stripe_account: '{{CONNECTED_ACCOUNT_ID}}'},
)
```

```python
# This example uses the beta SDK. See https://github.com/stripe/stripe-python#public-preview-sdks
client = StripeClient("<<YOUR_SECRET_KEY>>")

hold = client.v1.reserve.holds.retrieve(
  "reshold_61SxrUZH1aQJj97WT41Q8rCFhzAUW",
  options={"stripe_account": "{{CONNECTED_ACCOUNT_ID}}"},
)
```

```php
// This example uses the beta SDK. See https://github.com/stripe/stripe-php#public-preview-sdks
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$hold = $stripe->reserve->holds->retrieve(
  'reshold_61SxrUZH1aQJj97WT41Q8rCFhzAUW',
  [],
  ['stripe_account' => '{{CONNECTED_ACCOUNT_ID}}']
);
```

```java
// This example uses the beta SDK. See https://github.com/stripe/stripe-java#public-preview-sdks
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

HoldRetrieveParams params = HoldRetrieveParams.builder().build();

RequestOptions requestOptions =
  RequestOptions.builder()
    .setStripeAccount("{{CONNECTED_ACCOUNT_ID}}")
    .build();

Hold hold =
  client.v1().reserve().holds().retrieve(
    "reshold_61SxrUZH1aQJj97WT41Q8rCFhzAUW",
    params,
    requestOptions
  );
```

```node
// This example uses the beta SDK. See https://github.com/stripe/stripe-node#public-preview-sdks
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const hold = await stripe.reserve.holds.retrieve(
  'reshold_61SxrUZH1aQJj97WT41Q8rCFhzAUW',
  {
    stripeAccount: '{{CONNECTED_ACCOUNT_ID}}',
  }
);
```

```go
// This example uses the beta SDK. See https://github.com/stripe/stripe-go#public-preview-sdks
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.ReserveHoldRetrieveParams{}
params.SetStripeAccount("{{CONNECTED_ACCOUNT_ID}}")
result, err := sc.V1ReserveHolds.Retrieve(
  context.TODO(), "reshold_61SxrUZH1aQJj97WT41Q8rCFhzAUW", params)
```

```dotnet
// This example uses the beta SDK. See https://github.com/stripe/stripe-dotnet#public-preview-sdks
var requestOptions = new RequestOptions
{
    StripeAccount = "{{CONNECTED_ACCOUNT_ID}}",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Reserve.Holds;
Stripe.Reserve.Hold hold = service.Get(
    "reshold_61SxrUZH1aQJj97WT41Q8rCFhzAUW",
    null,
    requestOptions);
```

### Response

```json
{
  "id": "reshold_61SxrUZH1aQJj97WT41Q8rCFhzAUW",
  "object": "reserve.hold",
  "amount": 1000,
  "amount_releasable": 1000,
  "created": 1753380387,
  "created_by": "application",
  "currency": "usd",
  "is_releasable": true,
  "livemode": false,
  "metadata": {},
  "reason": "standalone",
  "release_schedule": {
    "release_after": 1755972386,
    "scheduled_release": 1755993600
  },
  "reserve_plan": null,
  "source_charge": null,
  "source_type": "card"
}
```