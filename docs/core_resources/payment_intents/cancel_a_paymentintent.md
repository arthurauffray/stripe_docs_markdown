# Cancel a PaymentIntent

You can cancel a PaymentIntent object when it’s in one of these statuses: `requires_payment_method`, `requires_capture`, `requires_confirmation`, `requires_action` or, [in rare cases](https://docs.stripe.com/docs/payments/intents.md), `processing`.

After it’s canceled, no additional charges are made by the PaymentIntent and any operations on the PaymentIntent fail with an error. For PaymentIntents with a `status` of `requires_capture`, the remaining `amount_capturable` is automatically refunded.

You can’t cancel the PaymentIntent for a Checkout Session. [Expire the Checkout Session](https://docs.stripe.com/docs/api/checkout/sessions/expire.md) instead.

## Returns

Returns a PaymentIntent object if the cancellation succeeds. Returns an error if the PaymentIntent is already canceled or isn’t in a cancelable state.

## Parameters

- `cancellation_reason` (string, optional)
  Reason for canceling this PaymentIntent. Possible values are: `duplicate`, `fraudulent`, `requested_by_customer`, or `abandoned`

```curl
curl -X POST https://api.stripe.com/v1/payment_intents/pi_3MtwBwLkdIwHu7ix28a3tqPa/cancel \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe payment_intents cancel pi_3MtwBwLkdIwHu7ix28a3tqPa
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

payment_intent = client.v1.payment_intents.cancel('pi_3MtwBwLkdIwHu7ix28a3tqPa')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

payment_intent = client.v1.payment_intents.cancel("pi_3MtwBwLkdIwHu7ix28a3tqPa")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentIntent = $stripe->paymentIntents->cancel('pi_3MtwBwLkdIwHu7ix28a3tqPa', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PaymentIntentCancelParams params = PaymentIntentCancelParams.builder().build();

PaymentIntent paymentIntent =
  client.v1().paymentIntents().cancel("pi_3MtwBwLkdIwHu7ix28a3tqPa", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.cancel(
  'pi_3MtwBwLkdIwHu7ix28a3tqPa'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PaymentIntentCancelParams{}
result, err := sc.V1PaymentIntents.Cancel(
  context.TODO(), "pi_3MtwBwLkdIwHu7ix28a3tqPa", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.PaymentIntents;
PaymentIntent paymentIntent = service.Cancel("pi_3MtwBwLkdIwHu7ix28a3tqPa");
```

### Response

```json
{
  "id": "pi_3MtwBwLkdIwHu7ix28a3tqPa",
  "object": "payment_intent",
  "amount": 2000,
  "amount_capturable": 0,
  "amount_details": {
    "tip": {}
  },
  "amount_received": 0,
  "application": null,
  "application_fee_amount": null,
  "automatic_payment_methods": {
    "enabled": true
  },
  "canceled_at": 1680801569,
  "cancellation_reason": null,
  "capture_method": "automatic",
  "client_secret": "pi_3MtwBwLkdIwHu7ix28a3tqPa_secret_YrKJUKribcBjcG8HVhfZluoGH",
  "confirmation_method": "automatic",
  "created": 1680800504,
  "currency": "usd",
  "customer": null,
  "description": null,
  "last_payment_error": null,
  "latest_charge": null,
  "livemode": false,
  "metadata": {},
  "next_action": null,
  "on_behalf_of": null,
  "payment_method": null,
  "payment_method_options": {
    "card": {
      "installments": null,
      "mandate_options": null,
      "network": null,
      "request_three_d_secure": "automatic"
    },
    "link": {
      "persistent_token": null
    }
  },
  "payment_method_types": [
    "card",
    "link"
  ],
  "processing": null,
  "receipt_email": null,
  "review": null,
  "setup_future_usage": null,
  "shipping": null,
  "source": null,
  "statement_descriptor": null,
  "statement_descriptor_suffix": null,
  "status": "canceled",
  "transfer_data": null,
  "transfer_group": null
}
```