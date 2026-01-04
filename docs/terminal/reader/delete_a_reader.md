# Delete a Reader

Deletes a `Reader` object.

## Returns

Returns the `Reader` object that was deleted.

```curl
curl -X DELETE https://api.stripe.com/v1/terminal/readers/tmr_FDOt2wlRZEdpd7 \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe terminal readers delete tmr_FDOt2wlRZEdpd7
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

deleted = client.v1.terminal.readers.delete('tmr_FDOt2wlRZEdpd7')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

deleted = client.v1.terminal.readers.delete("tmr_FDOt2wlRZEdpd7")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$deleted = $stripe->terminal->readers->delete('tmr_FDOt2wlRZEdpd7', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

Reader reader = client.v1().terminal().readers().delete("tmr_FDOt2wlRZEdpd7");
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const deleted = await stripe.terminal.readers.del('tmr_FDOt2wlRZEdpd7');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TerminalReaderDeleteParams{}
result, err := sc.V1TerminalReaders.Delete(
  context.TODO(), "tmr_FDOt2wlRZEdpd7", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Terminal.Readers;
Stripe.Terminal.Reader deleted = service.Delete("tmr_FDOt2wlRZEdpd7");
```

### Response

```json
{
  "id": "tmr_FDOt2wlRZEdpd7",
  "object": "terminal.reader",
  "deleted": true
}
```