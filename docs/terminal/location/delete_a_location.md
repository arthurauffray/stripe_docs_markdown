# Delete a Location

Deletes a `Location` object.

## Returns

Returns the `Location` object that was deleted.

```curl
curl -X DELETE https://api.stripe.com/v1/terminal/locations/tml_FBakXQG8bQk4Mm \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe terminal locations delete tml_FBakXQG8bQk4Mm
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

deleted = client.v1.terminal.locations.delete('tml_FBakXQG8bQk4Mm')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

deleted = client.v1.terminal.locations.delete("tml_FBakXQG8bQk4Mm")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$deleted = $stripe->terminal->locations->delete('tml_FBakXQG8bQk4Mm', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

Location location = client.v1().terminal().locations().delete("tml_FBakXQG8bQk4Mm");
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const deleted = await stripe.terminal.locations.del('tml_FBakXQG8bQk4Mm');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TerminalLocationDeleteParams{}
result, err := sc.V1TerminalLocations.Delete(
  context.TODO(), "tml_FBakXQG8bQk4Mm", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Terminal.Locations;
Stripe.Terminal.Location deleted = service.Delete("tml_FBakXQG8bQk4Mm");
```

### Response

```json
{
  "id": "tml_FBakXQG8bQk4Mm",
  "object": "terminal.location",
  "deleted": true
}
```