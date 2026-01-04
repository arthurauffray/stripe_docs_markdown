# Retrieve a Configuration

Retrieves a `Configuration` object.

## Returns

Returns a `Configuration` object if a valid identifier was provided.

```curl
curl https://api.stripe.com/v1/terminal/configurations/tmc_FQqbaQCiy0m1xc \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe terminal configurations retrieve tmc_FQqbaQCiy0m1xc
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

configuration = client.v1.terminal.configurations.retrieve('tmc_FQqbaQCiy0m1xc')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

configuration = client.v1.terminal.configurations.retrieve("tmc_FQqbaQCiy0m1xc")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$configuration = $stripe->terminal->configurations->retrieve(
  'tmc_FQqbaQCiy0m1xc',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ConfigurationRetrieveParams params = ConfigurationRetrieveParams.builder().build();

Configuration configuration =
  client.v1().terminal().configurations().retrieve("tmc_FQqbaQCiy0m1xc", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const configuration = await stripe.terminal.configurations.retrieve(
  'tmc_FQqbaQCiy0m1xc'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TerminalConfigurationRetrieveParams{}
result, err := sc.V1TerminalConfigurations.Retrieve(
  context.TODO(), "tmc_FQqbaQCiy0m1xc", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Terminal.Configurations;
Stripe.Terminal.Configuration configuration = service.Get("tmc_FQqbaQCiy0m1xc");
```

### Response

```json
{
  "id": "tmc_FQqbaQCiy0m1xc",
  "object": "terminal.configuration",
  "is_account_default": false,
  "livemode": false
}
```