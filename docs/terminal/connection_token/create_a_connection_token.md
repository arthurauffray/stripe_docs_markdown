# Create a Connection Token

To connect to a reader the Stripe Terminal SDK needs to retrieve a short-lived connection token from Stripe, proxied through your server. On your backend, add an endpoint that creates and returns a connection token.

## Returns

Returns a Connection Token.

## Parameters

- `location` (string, optional)
  The id of the location that this connection token is scoped to. If specified the connection token will only be usable with readers assigned to that location, otherwise the connection token will be usable with all readers. Note that location scoping only applies to internet-connected readers. For more details, see [the docs on scoping connection tokens](https://docs.stripe.com/terminal/fleet/locations-and-zones.md?dashboard-or-api=api#connection-tokens).

```curl
curl -X POST https://api.stripe.com/v1/terminal/connection_tokens \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe terminal connection_tokens create
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

connection_token = client.v1.terminal.connection_tokens.create()
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

connection_token = client.v1.terminal.connection_tokens.create()
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$connectionToken = $stripe->terminal->connectionTokens->create([]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ConnectionTokenCreateParams params = ConnectionTokenCreateParams.builder().build();

ConnectionToken connectionToken =
  client.v1().terminal().connectionTokens().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const connectionToken = await stripe.terminal.connectionTokens.create();
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TerminalConnectionTokenCreateParams{}
result, err := sc.V1TerminalConnectionTokens.Create(context.TODO(), params)
```

```dotnet
var options = new Stripe.Terminal.ConnectionTokenCreateOptions();
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Terminal.ConnectionTokens;
Stripe.Terminal.ConnectionToken connectionToken = service.Create(options);
```

### Response

```json
{
  "object": "terminal.connection_token",
  "secret": "pst_test_YWNjdF8xTTJKVGtMa2RJd0h1N2l4LE81ZEdIalZ6NlVuMUdjM3c3WkRnN0ZYRHZxRURwTXo_00gNK2DWAV"
}
```