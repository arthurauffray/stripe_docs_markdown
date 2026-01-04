# Refund a Charge or a PaymentIntent in-person

Initiates an in-person refund on a Reader. See [Refund an Interac Payment](https://docs.stripe.com/docs/terminal/payments/regional.md?integration-country=CA#refund-an-interac-payment) for more details.

## Returns

Returns an updated `Reader` resource

## Parameters

- `amount` (integer, optional)
  A positive integer in **cents** representing how much of this charge to refund.

- `charge` (string, optional)
  ID of the Charge to refund.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `payment_intent` (string, optional)
  ID of the PaymentIntent to refund.

- `refund_application_fee` (boolean, optional)
  Boolean indicating whether the application fee should be refunded when refunding this charge. If a full charge refund is given, the full application fee will be refunded. Otherwise, the application fee will be refunded in an amount proportional to the amount of the charge refunded. An application fee can be refunded only by the application that created the charge.

- `refund_payment_config` (object, optional)
  Configuration overrides for this refund, such as customer cancellation settings.

  - `refund_payment_config.enable_customer_cancellation` (boolean, optional)
    Enables cancel button on transaction screens.

- `reverse_transfer` (boolean, optional)
  Boolean indicating whether the transfer should be reversed when refunding this charge. The transfer will be reversed proportionally to the amount being refunded (either the entire or partial amount). A transfer can be reversed only by the application that created the charge.

```curl
curl https://api.stripe.com/v1/terminal/readers/tmr_njDFG9Z5k7y7KeQI8RmZYDYT/refund_payment \
  -u "<<YOUR_SECRET_KEY>>" \
  -d payment_intent=pi_1NrpbFBHO5VeT9SUiCEDMdc8
```

```cli
stripe terminal readers refund_payment tmr_njDFG9Z5k7y7KeQI8RmZYDYT \
  --payment-intent=pi_1NrpbFBHO5VeT9SUiCEDMdc8
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

reader = client.v1.terminal.readers.refund_payment(
  'tmr_njDFG9Z5k7y7KeQI8RmZYDYT',
  {payment_intent: 'pi_1NrpbFBHO5VeT9SUiCEDMdc8'},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

reader = client.v1.terminal.readers.refund_payment(
  "tmr_njDFG9Z5k7y7KeQI8RmZYDYT",
  {"payment_intent": "pi_1NrpbFBHO5VeT9SUiCEDMdc8"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$reader = $stripe->terminal->readers->refundPayment(
  'tmr_njDFG9Z5k7y7KeQI8RmZYDYT',
  ['payment_intent' => 'pi_1NrpbFBHO5VeT9SUiCEDMdc8']
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ReaderRefundPaymentParams params =
  ReaderRefundPaymentParams.builder()
    .setPaymentIntent("pi_1NrpbFBHO5VeT9SUiCEDMdc8")
    .build();

Reader reader =
  client.v1().terminal().readers().refundPayment(
    "tmr_njDFG9Z5k7y7KeQI8RmZYDYT",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const reader = await stripe.terminal.readers.refundPayment(
  'tmr_njDFG9Z5k7y7KeQI8RmZYDYT',
  {
    payment_intent: 'pi_1NrpbFBHO5VeT9SUiCEDMdc8',
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TerminalReaderRefundPaymentParams{
  PaymentIntent: stripe.String("pi_1NrpbFBHO5VeT9SUiCEDMdc8"),
}
result, err := sc.V1TerminalReaders.RefundPayment(
  context.TODO(), "tmr_njDFG9Z5k7y7KeQI8RmZYDYT", params)
```

```dotnet
var options = new Stripe.Terminal.ReaderRefundPaymentOptions
{
    PaymentIntent = "pi_1NrpbFBHO5VeT9SUiCEDMdc8",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Terminal.Readers;
Stripe.Terminal.Reader reader = service.RefundPayment(
    "tmr_njDFG9Z5k7y7KeQI8RmZYDYT",
    options);
```

### Response

```json
{
  "id": "tmr_njDFG9Z5k7y7KeQI8RmZYDYT",
  "object": "terminal.reader",
  "action": {
    "failure_code": null,
    "failure_message": null,
    "refund_payment": {
      "payment_intent": "pi_1NrpbFBHO5VeT9SUiCEDMdc8",
      "amount": 1000
    },
    "status": "in_progress",
    "type": "refund_payment"
  },
  "device_deploy_group": null,
  "device_sw_version": null,
  "device_type": "bbpos_wisepos_e",
  "ip_address": "192.168.2.2",
  "label": "Blue Rabbit",
  "livemode": false,
  "location": null,
  "metadata": {},
  "serial_number": "123-456-789",
  "software": null,
  "status": "online"
}
```