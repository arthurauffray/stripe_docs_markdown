# Cancel a SetupIntent

You can cancel a SetupIntent object when it’s in one of these statuses: `requires_payment_method`, `requires_confirmation`, or `requires_action`.

After you cancel it, setup is abandoned and any operations on the SetupIntent fail with an error. You can’t cancel the SetupIntent for a Checkout Session. [Expire the Checkout Session](https://docs.stripe.com/docs/api/checkout/sessions/expire.md) instead.

## Returns

Returns a SetupIntent object if the cancellation succeeds. Returns an error if the SetupIntent is already canceled or isn’t in a cancelable state.

## Parameters

- `cancellation_reason` (string, optional)
  Reason for canceling this SetupIntent. Possible values are: `abandoned`, `requested_by_customer`, or `duplicate`

```curl
curl -X POST https://api.stripe.com/v1/setup_intents/seti_1Mm8s8LkdIwHu7ix0OXBfTRG/cancel \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe setup_intents cancel seti_1Mm8s8LkdIwHu7ix0OXBfTRG
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

setup_intent = client.v1.setup_intents.cancel('seti_1Mm8s8LkdIwHu7ix0OXBfTRG')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

setup_intent = client.v1.setup_intents.cancel("seti_1Mm8s8LkdIwHu7ix0OXBfTRG")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$setupIntent = $stripe->setupIntents->cancel('seti_1Mm8s8LkdIwHu7ix0OXBfTRG', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

SetupIntentCancelParams params = SetupIntentCancelParams.builder().build();

SetupIntent setupIntent =
  client.v1().setupIntents().cancel("seti_1Mm8s8LkdIwHu7ix0OXBfTRG", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.cancel(
  'seti_1Mm8s8LkdIwHu7ix0OXBfTRG'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.SetupIntentCancelParams{}
result, err := sc.V1SetupIntents.Cancel(
  context.TODO(), "seti_1Mm8s8LkdIwHu7ix0OXBfTRG", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.SetupIntents;
SetupIntent setupIntent = service.Cancel("seti_1Mm8s8LkdIwHu7ix0OXBfTRG");
```

### Response

```json
{
  "id": "seti_1Mm8s8LkdIwHu7ix0OXBfTRG",
  "object": "setup_intent",
  "application": null,
  "cancellation_reason": null,
  "client_secret": "seti_1Mm8s8LkdIwHu7ix0OXBfTRG_secret_NXDICkPqPeiBTAFqWmkbff09lRmSVXe",
  "created": 1678942624,
  "customer": null,
  "description": null,
  "flow_directions": null,
  "last_setup_error": null,
  "latest_attempt": null,
  "livemode": false,
  "mandate": null,
  "metadata": {},
  "next_action": null,
  "on_behalf_of": null,
  "payment_method": null,
  "payment_method_options": {
    "card": {
      "mandate_options": null,
      "network": null,
      "request_three_d_secure": "automatic"
    }
  },
  "payment_method_types": [
    "card"
  ],
  "single_use_mandate": null,
  "status": "canceled",
  "usage": "off_session"
}
```