# Simulate presenting a payment method

Presents a payment method on a simulated reader. Can be used to simulate accepting a payment, saving a card or refunding a transaction.

## Returns

Returns an updated `Reader` resource.

## Parameters

- `amount_tip` (integer, optional)
  Simulated on-reader tip amount.

- `card` (object, optional)
  Simulated data for the card payment method.

  - `card.exp_month` (integer, required)
    Two-digit number representing the card’s expiration month.

  - `card.exp_year` (integer, required)
    Two- or four-digit number representing the card’s expiration year.

  - `card.number` (string, required)
    The card number, as a string without any separators.

  - `card.cvc` (string, optional)
    Card security code.

- `card_present` (object, optional)
  Simulated data for the card_present payment method.

  - `card_present.number` (string, optional)
    The card number, as a string without any separators.

- `interac_present` (object, optional)
  Simulated data for the interac_present payment method.

  - `interac_present.number` (string, optional)
    The Interac card number.

- `type` (enum, optional)
  Simulated payment type.
Possible enum values:
  - `card`
    Simulate a `card` payment method

  - `card_present`
    Simulate a `card_present` payment method

  - `interac_present`
    Simulate a `interac_present` payment method

```curl
curl -X POST https://api.stripe.com/v1/test_helpers/terminal/readers/tmr_gLeqlF03xvlBympS9RfZqdpF/present_payment_method \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe test_helpers terminal readers present_payment_method tmr_gLeqlF03xvlBympS9RfZqdpF
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

reader = client.v1.test_helpers.terminal.readers.present_payment_method('tmr_gLeqlF03xvlBympS9RfZqdpF')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

reader = client.v1.test_helpers.terminal.readers.present_payment_method(
  "tmr_gLeqlF03xvlBympS9RfZqdpF",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$reader = $stripe->testHelpers->terminal->readers->presentPaymentMethod(
  'tmr_gLeqlF03xvlBympS9RfZqdpF',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ReaderPresentPaymentMethodParams params =
  ReaderPresentPaymentMethodParams.builder().build();

Reader reader =
  client.v1().testHelpers().terminal().readers().presentPaymentMethod(
    "tmr_gLeqlF03xvlBympS9RfZqdpF",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const reader = await stripe.testHelpers.terminal.readers.presentPaymentMethod(
  'tmr_gLeqlF03xvlBympS9RfZqdpF'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TestHelpersTerminalReaderPresentPaymentMethodParams{}
result, err := sc.V1TestHelpersTerminalReaders.PresentPaymentMethod(
  context.TODO(), "tmr_gLeqlF03xvlBympS9RfZqdpF", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.TestHelpers.Terminal.Readers;
Stripe.Terminal.Reader reader = service.PresentPaymentMethod(
    "tmr_gLeqlF03xvlBympS9RfZqdpF");
```

### Response

```json
{
  "id": "tmr_gLeqlF03xvlBympS9RfZqdpF",
  "object": "terminal.reader",
  "action": {
    "failure_code": null,
    "failure_message": null,
    "process_payment_intent": {
      "payment_intent": "pi_1Gt0582eZvKYlo2CGSidzWqK"
    },
    "status": "succeeded",
    "type": "process_payment_intent"
  },
  "device_sw_version": null,
  "device_type": "bbpos_wisepos_e",
  "ip_address": "192.168.2.2",
  "label": "Blue Rabbit",
  "last_seen_at": null,
  "livemode": false,
  "location": null,
  "metadata": {},
  "serial_number": "123-456-789",
  "status": "online"
}
```