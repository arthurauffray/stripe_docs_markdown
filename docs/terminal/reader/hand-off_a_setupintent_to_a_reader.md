# Hand-off a SetupIntent to a Reader

Initiates a SetupIntent flow on a Reader. See [Save directly without charging](https://docs.stripe.com/docs/terminal/features/saving-payment-details/save-directly.md) for more details.

## Returns

Returns an updated `Reader` resource.

## Parameters

- `allow_redisplay` (enum, required)
  This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow.
Possible enum values:
  - `always`
    Use `always` to indicate that this payment method can always be shown to a customer in a checkout flow.

  - `limited`
    Use `limited` to indicate that this payment method can’t always be shown to a customer in a checkout flow. For example, it can only be shown in the context of a specific subscription.

  - `unspecified`
    This is the default value for payment methods where `allow_redisplay` wasn’t set.

- `setup_intent` (string, required)
  The ID of the SetupIntent to process on the reader.

- `process_config` (object, optional)
  Configuration overrides for this setup, such as MOTO and customer cancellation settings.

  - `process_config.enable_customer_cancellation` (boolean, optional)
    Enables cancel button on transaction screens.

```curl
curl https://api.stripe.com/v1/terminal/readers/tmr_FDOt2wlRZEdpd7/process_setup_intent \
  -u "<<YOUR_SECRET_KEY>>" \
  -d allow_redisplay=always \
  -d setup_intent=seti_1NtEXHLkdIwHu7ixcBcUmqfe
```

```cli
stripe terminal readers process_setup_intent tmr_FDOt2wlRZEdpd7 \
  --allow-redisplay=always \
  --setup-intent=seti_1NtEXHLkdIwHu7ixcBcUmqfe
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

reader = client.v1.terminal.readers.process_setup_intent(
  'tmr_FDOt2wlRZEdpd7',
  {
    allow_redisplay: 'always',
    setup_intent: 'seti_1NtEXHLkdIwHu7ixcBcUmqfe',
  },
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

reader = client.v1.terminal.readers.process_setup_intent(
  "tmr_FDOt2wlRZEdpd7",
  {"allow_redisplay": "always", "setup_intent": "seti_1NtEXHLkdIwHu7ixcBcUmqfe"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$reader = $stripe->terminal->readers->processSetupIntent(
  'tmr_FDOt2wlRZEdpd7',
  [
    'allow_redisplay' => 'always',
    'setup_intent' => 'seti_1NtEXHLkdIwHu7ixcBcUmqfe',
  ]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ReaderProcessSetupIntentParams params =
  ReaderProcessSetupIntentParams.builder()
    .setAllowRedisplay(ReaderProcessSetupIntentParams.AllowRedisplay.ALWAYS)
    .setSetupIntent("seti_1NtEXHLkdIwHu7ixcBcUmqfe")
    .build();

Reader reader =
  client.v1().terminal().readers().processSetupIntent("tmr_FDOt2wlRZEdpd7", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const reader = await stripe.terminal.readers.processSetupIntent(
  'tmr_FDOt2wlRZEdpd7',
  {
    allow_redisplay: 'always',
    setup_intent: 'seti_1NtEXHLkdIwHu7ixcBcUmqfe',
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TerminalReaderProcessSetupIntentParams{
  AllowRedisplay: stripe.String("always"),
  SetupIntent: stripe.String("seti_1NtEXHLkdIwHu7ixcBcUmqfe"),
}
result, err := sc.V1TerminalReaders.ProcessSetupIntent(
  context.TODO(), "tmr_FDOt2wlRZEdpd7", params)
```

```dotnet
var options = new Stripe.Terminal.ReaderProcessSetupIntentOptions
{
    AllowRedisplay = "always",
    SetupIntent = "seti_1NtEXHLkdIwHu7ixcBcUmqfe",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Terminal.Readers;
Stripe.Terminal.Reader reader = service.ProcessSetupIntent(
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
    "process_setup_intent": {
      "setup_intent": "seti_1NtEXHLkdIwHu7ixcBcUmqfe"
    },
    "status": "in_progress",
    "type": "process_setup_intent"
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