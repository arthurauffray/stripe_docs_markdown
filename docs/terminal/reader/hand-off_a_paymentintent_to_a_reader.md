# Hand-off a PaymentIntent to a Reader

Initiates a payment flow on a Reader. See [process the payment](https://docs.stripe.com/docs/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven&process=immediately#process-payment) for more details.

## Returns

Returns an updated `Reader` resource.

## Parameters

- `payment_intent` (string, required)
  The ID of the PaymentIntent to process on the reader.

- `process_config` (object, optional)
  Configuration overrides for this transaction, such as tipping and customer cancellation settings.

  - `process_config.allow_redisplay` (enum, optional)
    This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow.
Possible enum values:
    - `always`
      Use `always` to indicate that this payment method can always be shown to a customer in a checkout flow.

    - `limited`
      Use `limited` to indicate that this payment method can’t always be shown to a customer in a checkout flow. For example, it can only be shown in the context of a specific subscription.

    - `unspecified`
      This is the default value for payment methods where `allow_redisplay` wasn’t set.

  - `process_config.enable_customer_cancellation` (boolean, optional)
    Enables cancel button on transaction screens.

  - `process_config.return_url` (string, optional)
    The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method’s app or site. If you’d prefer to redirect to a mobile application, you can alternatively supply an application URI scheme.

  - `process_config.skip_tipping` (boolean, optional)
    Override showing a tipping selection screen on this transaction.

  - `process_config.tipping` (object, optional)
    Tipping configuration for this transaction.

    - `process_config.tipping.amount_eligible` (integer, optional)
      Amount used to calculate tip suggestions on tipping selection screen for this transaction. Must be a positive integer in the smallest currency unit (e.g., 100 cents to represent $1.00 or 100 to represent ¥100, a zero-decimal currency).

```curl
curl https://api.stripe.com/v1/terminal/readers/tmr_FDOt2wlRZEdpd7/process_payment_intent \
  -u "<<YOUR_SECRET_KEY>>" \
  -d payment_intent=pi_3NtEKRLkdIwHu7ix3crEirSx
```

```cli
stripe terminal readers process_payment_intent tmr_FDOt2wlRZEdpd7 \
  --payment-intent=pi_3NtEKRLkdIwHu7ix3crEirSx
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

reader = client.v1.terminal.readers.process_payment_intent(
  'tmr_FDOt2wlRZEdpd7',
  {payment_intent: 'pi_3NtEKRLkdIwHu7ix3crEirSx'},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

reader = client.v1.terminal.readers.process_payment_intent(
  "tmr_FDOt2wlRZEdpd7",
  {"payment_intent": "pi_3NtEKRLkdIwHu7ix3crEirSx"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$reader = $stripe->terminal->readers->processPaymentIntent(
  'tmr_FDOt2wlRZEdpd7',
  ['payment_intent' => 'pi_3NtEKRLkdIwHu7ix3crEirSx']
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ReaderProcessPaymentIntentParams params =
  ReaderProcessPaymentIntentParams.builder()
    .setPaymentIntent("pi_3NtEKRLkdIwHu7ix3crEirSx")
    .build();

Reader reader =
  client.v1().terminal().readers().processPaymentIntent(
    "tmr_FDOt2wlRZEdpd7",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const reader = await stripe.terminal.readers.processPaymentIntent(
  'tmr_FDOt2wlRZEdpd7',
  {
    payment_intent: 'pi_3NtEKRLkdIwHu7ix3crEirSx',
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TerminalReaderProcessPaymentIntentParams{
  PaymentIntent: stripe.String("pi_3NtEKRLkdIwHu7ix3crEirSx"),
}
result, err := sc.V1TerminalReaders.ProcessPaymentIntent(
  context.TODO(), "tmr_FDOt2wlRZEdpd7", params)
```

```dotnet
var options = new Stripe.Terminal.ReaderProcessPaymentIntentOptions
{
    PaymentIntent = "pi_3NtEKRLkdIwHu7ix3crEirSx",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Terminal.Readers;
Stripe.Terminal.Reader reader = service.ProcessPaymentIntent(
    "tmr_FDOt2wlRZEdpd7",
    options);
```

### Response

```json
{
  "id": "tmr_FDOt2wlRZEdpd7",
  "object": "terminal.reader",
  "action": {
    "failure_code": null,
    "failure_message": null,
    "process_payment_intent": {
      "payment_intent": "pi_3NtEKRLkdIwHu7ix3crEirSx"
    },
    "status": "in_progress",
    "type": "process_payment_intent"
  },
  "device_sw_version": "2.37.2.0",
  "device_type": "simulated_wisepos_e",
  "ip_address": "0.0.0.0",
  "label": "Blue Rabbit",
  "last_seen_at": 1695408232226,
  "livemode": false,
  "location": "tml_FDOtHwxAAdIJOh",
  "metadata": {},
  "serial_number": "259cd19c-b902-4730-96a1-09183be6e7f7",
  "status": "online"
}
```