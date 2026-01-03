# Retrieve a SetupIntent

Retrieves the details of a SetupIntent that has previously been created.

Client-side retrieval using a publishable key is allowed when the `client_secret` is provided in the query string.

When retrieved with a publishable key, only a subset of properties will be returned. Please refer to the [SetupIntent](https://docs.stripe.com/api/setup_intents/retrieve.md#setup_intent_object) object reference for more details.

## Returns

Returns a SetupIntent if a valid identifier was provided.

## Parameters

- `client_secret` (string, Required if using publishable key)
  The client secret of the SetupIntent. We require this string if you use a publishable key to retrieve the SetupIntent.

```curl
curl https://api.stripe.com/v1/setup_intents/seti_1Mm8s8LkdIwHu7ix0OXBfTRG \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe setup_intents retrieve seti_1Mm8s8LkdIwHu7ix0OXBfTRG
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

setup_intent = client.v1.setup_intents.retrieve('seti_1Mm8s8LkdIwHu7ix0OXBfTRG')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

setup_intent = client.v1.setup_intents.retrieve("seti_1Mm8s8LkdIwHu7ix0OXBfTRG")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$setupIntent = $stripe->setupIntents->retrieve('seti_1Mm8s8LkdIwHu7ix0OXBfTRG', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

SetupIntentRetrieveParams params = SetupIntentRetrieveParams.builder().build();

SetupIntent setupIntent =
  client.v1().setupIntents().retrieve("seti_1Mm8s8LkdIwHu7ix0OXBfTRG", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.retrieve(
  'seti_1Mm8s8LkdIwHu7ix0OXBfTRG'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.SetupIntentRetrieveParams{}
result, err := sc.V1SetupIntents.Retrieve(
  context.TODO(), "seti_1Mm8s8LkdIwHu7ix0OXBfTRG", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.SetupIntents;
SetupIntent setupIntent = service.Get("seti_1Mm8s8LkdIwHu7ix0OXBfTRG");
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
  "status": "requires_payment_method",
  "usage": "off_session"
}
```