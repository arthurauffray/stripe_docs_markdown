# Update a Reader

Updates a `Reader` object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

## Returns

Returns an updated `Reader` object if a valid identifier was provided.

## Parameters

- `label` (string, optional)
  The new label of the reader.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/terminal/readers/tmr_FDOt2wlRZEdpd7 \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
```

```cli
stripe terminal readers update tmr_FDOt2wlRZEdpd7 \
  -d "metadata[order_id]"=6735
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

reader = client.v1.terminal.readers.update(
  'tmr_FDOt2wlRZEdpd7',
  {metadata: {order_id: '6735'}},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

reader = client.v1.terminal.readers.update(
  "tmr_FDOt2wlRZEdpd7",
  {"metadata": {"order_id": "6735"}},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$reader = $stripe->terminal->readers->update(
  'tmr_FDOt2wlRZEdpd7',
  ['metadata' => ['order_id' => '6735']]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ReaderUpdateParams params =
  ReaderUpdateParams.builder().putMetadata("order_id", "6735").build();

Reader reader =
  client.v1().terminal().readers().update("tmr_FDOt2wlRZEdpd7", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const reader = await stripe.terminal.readers.update(
  'tmr_FDOt2wlRZEdpd7',
  {
    metadata: {
      order_id: '6735',
    },
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TerminalReaderUpdateParams{}
params.AddMetadata("order_id", "6735")
result, err := sc.V1TerminalReaders.Update(
  context.TODO(), "tmr_FDOt2wlRZEdpd7", params)
```

```dotnet
var options = new Stripe.Terminal.ReaderUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Terminal.Readers;
Stripe.Terminal.Reader reader = service.Update("tmr_FDOt2wlRZEdpd7", options);
```

### Response

```json
{
  "id": "tmr_FDOt2wlRZEdpd7",
  "object": "terminal.reader",
  "action": null,
  "device_sw_version": "2.37.2.0",
  "device_type": "simulated_wisepos_e",
  "ip_address": "0.0.0.0",
  "label": "Blue Rabbit",
  "last_seen_at": 1681320543815,
  "livemode": false,
  "location": "tml_FDOtHwxAAdIJOh",
  "metadata": {
    "order_id": "6735"
  },
  "serial_number": "259cd19c-b902-4730-96a1-09183be6e7f7",
  "status": "online"
}
```