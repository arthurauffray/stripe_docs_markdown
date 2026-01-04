# Confirm a PaymentIntent on the Reader

Finalizes a payment on a Reader. See [Confirming a Payment](https://docs.stripe.com/docs/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven&process=inspect#confirm-the-paymentintent) for more details.

## Returns

Returns an updated `Reader` resource.

## Parameters

- `payment_intent` (string, required)
  The ID of the PaymentIntent to confirm.

- `confirm_config` (object, optional)
  Configuration overrides for this confirmation, such as surcharge settings and return URL.

  - `confirm_config.return_url` (string, optional)
    The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method’s app or site. If you’d prefer to redirect to a mobile application, you can alternatively supply an application URI scheme.

```curl
curl https://api.stripe.com/v1/terminal/readers/tmr_FDOt2wlRZEdpd7/confirm_payment_intent \
  -u "<<YOUR_SECRET_KEY>>" \
  -d payment_intent=pi_1NrpbFBHO5VeT9SUiCEDMdc8
```

```cli
stripe terminal readers confirm_payment_intent tmr_FDOt2wlRZEdpd7 \
  --payment-intent=pi_1NrpbFBHO5VeT9SUiCEDMdc8
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

reader = client.v1.terminal.readers.confirm_payment_intent(
  'tmr_FDOt2wlRZEdpd7',
  {payment_intent: 'pi_1NrpbFBHO5VeT9SUiCEDMdc8'},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

reader = client.v1.terminal.readers.confirm_payment_intent(
  "tmr_FDOt2wlRZEdpd7",
  {"payment_intent": "pi_1NrpbFBHO5VeT9SUiCEDMdc8"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$reader = $stripe->terminal->readers->confirmPaymentIntent(
  'tmr_FDOt2wlRZEdpd7',
  ['payment_intent' => 'pi_1NrpbFBHO5VeT9SUiCEDMdc8']
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ReaderConfirmPaymentIntentParams params =
  ReaderConfirmPaymentIntentParams.builder()
    .setPaymentIntent("pi_1NrpbFBHO5VeT9SUiCEDMdc8")
    .build();

Reader reader =
  client.v1().terminal().readers().confirmPaymentIntent(
    "tmr_FDOt2wlRZEdpd7",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const reader = await stripe.terminal.readers.confirmPaymentIntent(
  'tmr_FDOt2wlRZEdpd7',
  {
    payment_intent: 'pi_1NrpbFBHO5VeT9SUiCEDMdc8',
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TerminalReaderConfirmPaymentIntentParams{
  PaymentIntent: stripe.String("pi_1NrpbFBHO5VeT9SUiCEDMdc8"),
}
result, err := sc.V1TerminalReaders.ConfirmPaymentIntent(
  context.TODO(), "tmr_FDOt2wlRZEdpd7", params)
```

```dotnet
var options = new Stripe.Terminal.ReaderConfirmPaymentIntentOptions
{
    PaymentIntent = "pi_1NrpbFBHO5VeT9SUiCEDMdc8",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Terminal.Readers;
Stripe.Terminal.Reader reader = service.ConfirmPaymentIntent(
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
    "collect_payment_method": {
      "payment_intent": "pi_1NrpbFBHO5VeT9SUiCEDMdc8"
    },
    "status": "in_progress",
    "type": "confirm_payment_intent"
  },
  "device_sw_version": "2.37.2.0",
  "device_type": "simulated_wisepos_e",
  "ip_address": "0.0.0.0",
  "label": "Blue Rabbit",
  "last_seen_at": 1681320543815,
  "livemode": false,
  "location": "tml_FDOtHwxAAdIJOh",
  "metadata": {},
  "serial_number": "259cd19c-b902-4730-96a1-09183be6e7f7",
  "status": "online"
}
```