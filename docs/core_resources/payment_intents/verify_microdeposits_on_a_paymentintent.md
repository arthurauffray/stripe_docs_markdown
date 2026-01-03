# Verify microdeposits on a PaymentIntent

Verifies microdeposits on a PaymentIntent object.

## Returns

Returns a PaymentIntent object.

## Parameters

- `amounts` (array of integers, optional)
  Two positive integers, in *cents*, equal to the values of the microdeposits sent to the bank account.

- `descriptor_code` (string, optional)
  A six-character code starting with SM present in the microdeposit sent to the bank account.

```curl
curl https://api.stripe.com/v1/payment_intents/pi_1DtBRR2eZvKYlo2CmCVxxvd7/verify_microdeposits \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "amounts[]"=32 \
  -d "amounts[]"=45
```

```cli
stripe payment_intents verify_microdeposits pi_1DtBRR2eZvKYlo2CmCVxxvd7 \
  -d "amounts[0]"=32 \
  -d "amounts[1]"=45
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

payment_intent = client.v1.payment_intents.verify_microdeposits(
  'pi_1DtBRR2eZvKYlo2CmCVxxvd7',
  {amounts: [32, 45]},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

payment_intent = client.v1.payment_intents.verify_microdeposits(
  "pi_1DtBRR2eZvKYlo2CmCVxxvd7",
  {"amounts": [32, 45]},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentIntent = $stripe->paymentIntents->verifyMicrodeposits(
  'pi_1DtBRR2eZvKYlo2CmCVxxvd7',
  ['amounts' => [32, 45]]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PaymentIntentVerifyMicrodepositsParams params =
  PaymentIntentVerifyMicrodepositsParams.builder()
    .addAmount(32L)
    .addAmount(45L)
    .build();

PaymentIntent paymentIntent =
  client.v1().paymentIntents().verifyMicrodeposits(
    "pi_1DtBRR2eZvKYlo2CmCVxxvd7",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.verifyMicrodeposits(
  'pi_1DtBRR2eZvKYlo2CmCVxxvd7',
  {
    amounts: [32, 45],
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PaymentIntentVerifyMicrodepositsParams{
  Amounts: []*int64{stripe.Int64(32), stripe.Int64(45)},
}
result, err := sc.V1PaymentIntents.VerifyMicrodeposits(
  context.TODO(), "pi_1DtBRR2eZvKYlo2CmCVxxvd7", params)
```

```dotnet
var options = new PaymentIntentVerifyMicrodepositsOptions
{
    Amounts = new List<long?> { 32, 45 },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.PaymentIntents;
PaymentIntent paymentIntent = service.VerifyMicrodeposits(
    "pi_1DtBRR2eZvKYlo2CmCVxxvd7",
    options);
```

### Response

```json
{
  "id": "pi_1DtBRR2eZvKYlo2CmCVxxvd7",
  "object": "payment_intent",
  "amount": 1099,
  "amount_capturable": 0,
  "amount_details": {
    "tip": {}
  },
  "amount_received": 0,
  "application": null,
  "application_fee_amount": null,
  "automatic_payment_methods": null,
  "canceled_at": null,
  "cancellation_reason": null,
  "capture_method": "automatic",
  "client_secret": "pi_1DtBRR2eZvKYlo2CmCVxxvd7_secret_l80vlOGz9kZQwnzocExJQUsJx",
  "confirmation_method": "automatic",
  "created": 1680800210,
  "currency": "usd",
  "customer": null,
  "description": null,
  "last_payment_error": null,
  "latest_charge": null,
  "livemode": false,
  "metadata": {},
  "next_action": null,
  "on_behalf_of": null,
  "payment_method": "pm_1Mtw7C2eZvKYlo2CPsW0F8g0",
  "payment_method_options": {
    "acss_debit": {
      "mandate_options": {
        "interval_description": "First day of every month",
        "payment_schedule": "interval",
        "transaction_type": "personal"
      },
      "verification_method": "automatic"
    }
  },
  "payment_method_types": [
    "acss_debit"
  ],
  "processing": null,
  "receipt_email": null,
  "redaction": null,
  "review": null,
  "setup_future_usage": null,
  "shipping": null,
  "statement_descriptor": null,
  "statement_descriptor_suffix": null,
  "status": "succeeded",
  "transfer_data": null,
  "transfer_group": null
}
```