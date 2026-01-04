# Retrieve a Reader

Retrieves a `Reader` object.

## Returns

Returns a `Reader` object if a valid identifier was provided.

```curl
curl https://api.stripe.com/v1/terminal/readers/tmr_FDOt2wlRZEdpd7 \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe terminal readers retrieve tmr_FDOt2wlRZEdpd7
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

reader = client.v1.terminal.readers.retrieve('tmr_FDOt2wlRZEdpd7')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

reader = client.v1.terminal.readers.retrieve("tmr_FDOt2wlRZEdpd7")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$reader = $stripe->terminal->readers->retrieve('tmr_FDOt2wlRZEdpd7', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ReaderRetrieveParams params = ReaderRetrieveParams.builder().build();

Reader reader =
  client.v1().terminal().readers().retrieve("tmr_FDOt2wlRZEdpd7", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const reader = await stripe.terminal.readers.retrieve('tmr_FDOt2wlRZEdpd7');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TerminalReaderRetrieveParams{}
result, err := sc.V1TerminalReaders.Retrieve(
  context.TODO(), "tmr_FDOt2wlRZEdpd7", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Terminal.Readers;
Stripe.Terminal.Reader reader = service.Get("tmr_FDOt2wlRZEdpd7");
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
  "metadata": {},
  "serial_number": "259cd19c-b902-4730-96a1-09183be6e7f7",
  "status": "online"
}
```