# Verify microdeposits on a SetupIntent

Verifies microdeposits on a SetupIntent object.

## Returns

Returns a SetupIntent object.

## Parameters

- `amounts` (array of integers, optional)
  Two positive integers, in *cents*, equal to the values of the microdeposits sent to the bank account.

- `descriptor_code` (string, optional)
  A six-character code starting with SM present in the microdeposit sent to the bank account.

```curl
curl https://api.stripe.com/v1/setup_intents/seti_1Mm5yZLkdIwHu7ixm0sPzrx4/verify_microdeposits \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "amounts[]"=32 \
  -d "amounts[]"=45
```

```cli
stripe setup_intents verify_microdeposits seti_1Mm5yZLkdIwHu7ixm0sPzrx4 \
  -d "amounts[0]"=32 \
  -d "amounts[1]"=45
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

setup_intent = client.v1.setup_intents.verify_microdeposits(
  'seti_1Mm5yZLkdIwHu7ixm0sPzrx4',
  {amounts: [32, 45]},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

setup_intent = client.v1.setup_intents.verify_microdeposits(
  "seti_1Mm5yZLkdIwHu7ixm0sPzrx4",
  {"amounts": [32, 45]},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$setupIntent = $stripe->setupIntents->verifyMicrodeposits(
  'seti_1Mm5yZLkdIwHu7ixm0sPzrx4',
  ['amounts' => [32, 45]]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

SetupIntentVerifyMicrodepositsParams params =
  SetupIntentVerifyMicrodepositsParams.builder()
    .addAmount(32L)
    .addAmount(45L)
    .build();

SetupIntent setupIntent =
  client.v1().setupIntents().verifyMicrodeposits(
    "seti_1Mm5yZLkdIwHu7ixm0sPzrx4",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.verifyMicrodeposits(
  'seti_1Mm5yZLkdIwHu7ixm0sPzrx4',
  {
    amounts: [32, 45],
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.SetupIntentVerifyMicrodepositsParams{
  Amounts: []*int64{stripe.Int64(32), stripe.Int64(45)},
}
result, err := sc.V1SetupIntents.VerifyMicrodeposits(
  context.TODO(), "seti_1Mm5yZLkdIwHu7ixm0sPzrx4", params)
```

```dotnet
var options = new SetupIntentVerifyMicrodepositsOptions
{
    Amounts = new List<long?> { 32, 45 },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.SetupIntents;
SetupIntent setupIntent = service.VerifyMicrodeposits(
    "seti_1Mm5yZLkdIwHu7ixm0sPzrx4",
    options);
```

### Response

```json
{
  "id": "seti_1Mm5yZLkdIwHu7ixm0sPzrx4",
  "object": "setup_intent",
  "application": null,
  "cancellation_reason": null,
  "client_secret": "seti_1Mm5yZLkdIwHu7ixm0sPzrx4_secret_NXAJ5iPM38ITW1pI7o8VZZhoZyDrrWR",
  "created": 1678931491,
  "customer": null,
  "description": null,
  "flow_directions": null,
  "last_setup_error": null,
  "latest_attempt": "setatt_1Mm5yZLkdIwHu7ix7QtOkLAu",
  "livemode": false,
  "mandate": "mandate_1Mm5yaLkdIwHu7ixmNoLkKLC",
  "metadata": {},
  "next_action": null,
  "on_behalf_of": null,
  "payment_method": "pm_1Mm5yZLkdIwHu7ixf89jW57b",
  "payment_method_options": {
    "acss_debit": {
      "currency": "cad",
      "mandate_options": {
        "interval_description": "First of every month",
        "payment_schedule": "interval",
        "transaction_type": "personal"
      },
      "verification_method": "automatic"
    }
  },
  "payment_method_types": [
    "acss_debit"
  ],
  "single_use_mandate": null,
  "status": "succeeded",
  "usage": "off_session"
}
```