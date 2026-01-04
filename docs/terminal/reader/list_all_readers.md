# List all Readers

Returns a list of `Reader` objects.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` readers, starting after reader `starting_after`. Each entry in the array is a separate Terminal `Reader` object. If no more readers are available, the resulting array will be empty.

## Parameters

- `device_type` (enum, optional)
  Filters readers by device type
Possible enum values:
  - `bbpos_chipper2x`
    BBPOS Chipper 2X BT reader.

  - `bbpos_wisepad3`
    BBPOS WisePad 3 reader.

  - `bbpos_wisepos_e`
    BBPOS WisePOS E reader.

  - `mobile_phone_reader`
    Tap to Pay device.

  - `simulated_stripe_s700`
    Simulated Stripe S700 reader.

  - `simulated_wisepos_e`
    Simulated BBPOS WisePOS E reader.

  - `stripe_m2`
    Stripe M2 reader.

  - `stripe_s700`
    Stripe S700 reader.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `location` (string, optional)
  A location ID to filter the response list to only readers at the specific location

- `serial_number` (string, optional)
  Filters readers by serial number

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `status` (enum, optional)
  A status filter to filter readers to only offline or online readers

```curl
curl -G https://api.stripe.com/v1/terminal/readers \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe terminal readers list  \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

readers = client.v1.terminal.readers.list({limit: 3})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

readers = client.v1.terminal.readers.list({"limit": 3})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$readers = $stripe->terminal->readers->all(['limit' => 3]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ReaderListParams params = ReaderListParams.builder().setLimit(3L).build();

StripeCollection<Reader> stripeCollection =
  client.v1().terminal().readers().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const readers = await stripe.terminal.readers.list({
  limit: 3,
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TerminalReaderListParams{}
params.Limit = stripe.Int64(3)
result := sc.V1TerminalReaders.List(context.TODO(), params)
```

```dotnet
var options = new Stripe.Terminal.ReaderListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Terminal.Readers;
StripeList<Stripe.Terminal.Reader> readers = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/terminal/readers",
  "has_more": false,
  "data": [
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
  ]
}
```