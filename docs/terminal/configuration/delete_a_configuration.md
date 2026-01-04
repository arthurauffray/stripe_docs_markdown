# Delete a Configuration

Deletes a `Configuration` object.

## Returns

Returns the `Configuration` object that was deleted.

```curl
curl -X DELETE https://api.stripe.com/v1/terminal/configurations/tmc_FQqbaQCiy0m1xc \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe terminal configurations delete tmc_FQqbaQCiy0m1xc
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

deleted = client.v1.terminal.configurations.delete('tmc_FQqbaQCiy0m1xc')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

deleted = client.v1.terminal.configurations.delete("tmc_FQqbaQCiy0m1xc")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$deleted = $stripe->terminal->configurations->delete('tmc_FQqbaQCiy0m1xc', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

Configuration configuration =
  client.v1().terminal().configurations().delete("tmc_FQqbaQCiy0m1xc");
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const deleted = await stripe.terminal.configurations.del('tmc_FQqbaQCiy0m1xc');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TerminalConfigurationDeleteParams{}
result, err := sc.V1TerminalConfigurations.Delete(
  context.TODO(), "tmc_FQqbaQCiy0m1xc", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Terminal.Configurations;
Stripe.Terminal.Configuration deleted = service.Delete("tmc_FQqbaQCiy0m1xc");
```

### Response

```json
{
  "id": "tmc_FQqbaQCiy0m1xc",
  "object": "terminal.configuration",
  "deleted": true
}
```