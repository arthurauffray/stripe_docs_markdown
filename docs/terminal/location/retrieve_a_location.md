# Retrieve a Location

Retrieves a `Location` object.

## Returns

Returns a `Location` object if a valid identifier was provided.

```curl
curl https://api.stripe.com/v1/terminal/locations/tml_FBakXQG8bQk4Mm \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe terminal locations retrieve tml_FBakXQG8bQk4Mm
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

location = client.v1.terminal.locations.retrieve('tml_FBakXQG8bQk4Mm')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

location = client.v1.terminal.locations.retrieve("tml_FBakXQG8bQk4Mm")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$location = $stripe->terminal->locations->retrieve('tml_FBakXQG8bQk4Mm', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

LocationRetrieveParams params = LocationRetrieveParams.builder().build();

Location location =
  client.v1().terminal().locations().retrieve("tml_FBakXQG8bQk4Mm", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const location = await stripe.terminal.locations.retrieve('tml_FBakXQG8bQk4Mm');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TerminalLocationRetrieveParams{}
result, err := sc.V1TerminalLocations.Retrieve(
  context.TODO(), "tml_FBakXQG8bQk4Mm", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Terminal.Locations;
Stripe.Terminal.Location location = service.Get("tml_FBakXQG8bQk4Mm");
```

### Response

```json
{
  "id": "tml_FBakXQG8bQk4Mm",
  "object": "terminal.location",
  "address": {
    "city": "San Francisco",
    "country": "US",
    "line1": "1234 Main Street",
    "line2": "",
    "postal_code": "94111",
    "state": "CA"
  },
  "display_name": "My First Store",
  "livemode": false,
  "metadata": {}
}
```