# Retrieve a ReserveRelease

Retrieve a ReserveRelease.

## Returns

Returns a ReserveRelease object.

## Parameters

- `id` (string, required)
  The identifier of the ReserveRelease to retrieve.

```curl
curl https://api.stripe.com/v1/reserve/releases/resrel_61SxyHbQOe90T6sLB41Q8rCFhzAUW \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe reserve releases retrieve resrel_61SxyHbQOe90T6sLB41Q8rCFhzAUW
```

```ruby
# This example uses the beta SDK. See https://github.com/stripe/stripe-ruby#public-preview-sdks
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

release = client.v1.reserve.releases.retrieve('resrel_61SxyHbQOe90T6sLB41Q8rCFhzAUW')
```

```python
# This example uses the beta SDK. See https://github.com/stripe/stripe-python#public-preview-sdks
client = StripeClient("<<YOUR_SECRET_KEY>>")

release = client.v1.reserve.releases.retrieve("resrel_61SxyHbQOe90T6sLB41Q8rCFhzAUW")
```

```php
// This example uses the beta SDK. See https://github.com/stripe/stripe-php#public-preview-sdks
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$release = $stripe->reserve->releases->retrieve(
  'resrel_61SxyHbQOe90T6sLB41Q8rCFhzAUW',
  []
);
```

```java
// This example uses the beta SDK. See https://github.com/stripe/stripe-java#public-preview-sdks
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ReleaseRetrieveParams params = ReleaseRetrieveParams.builder().build();

Release release =
  client.v1().reserve().releases().retrieve(
    "resrel_61SxyHbQOe90T6sLB41Q8rCFhzAUW",
    params
  );
```

```node
// This example uses the beta SDK. See https://github.com/stripe/stripe-node#public-preview-sdks
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const release = await stripe.reserve.releases.retrieve(
  'resrel_61SxyHbQOe90T6sLB41Q8rCFhzAUW'
);
```

```go
// This example uses the beta SDK. See https://github.com/stripe/stripe-go#public-preview-sdks
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.ReserveReleaseRetrieveParams{}
result, err := sc.V1ReserveReleases.Retrieve(
  context.TODO(), "resrel_61SxyHbQOe90T6sLB41Q8rCFhzAUW", params)
```

```dotnet
// This example uses the beta SDK. See https://github.com/stripe/stripe-dotnet#public-preview-sdks
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Reserve.Releases;
Stripe.Reserve.Release release = service.Get("resrel_61SxyHbQOe90T6sLB41Q8rCFhzAUW");
```

### Response

```json
{
  "id": "resrel_61SxyHbQOe90T6sLB41Q8rCFhzAUW",
  "object": "reserve.release",
  "amount": 500,
  "created": 1753406491,
  "created_by": "application",
  "currency": "usd",
  "livemode": false,
  "metadata": {},
  "reason": "hold_released_early",
  "released_at": 1753406491,
  "reserve_hold": "reshold_61SxrUZH1aQJj97WT41Q8rCFhzAUW",
  "reserve_plan": null
}
```