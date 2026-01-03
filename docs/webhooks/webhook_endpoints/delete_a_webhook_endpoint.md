# Delete a webhook endpoint

You can also delete webhook endpoints via the [webhook endpoint management](https://dashboard.stripe.com/account/webhooks) page of the Stripe dashboard.

## Returns

An object with the deleted webhook endpoints’s ID. Otherwise, this call raises [an error](https://docs.stripe.com/api/webhook_endpoints/delete.md#errors), such as if the webhook endpoint has already been deleted.

```curl
curl -X DELETE https://api.stripe.com/v1/webhook_endpoints/we_1Mr5jULkdIwHu7ix1ibLTM0x \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe webhook_endpoints delete we_1Mr5jULkdIwHu7ix1ibLTM0x
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

deleted = client.v1.webhook_endpoints.delete('we_1Mr5jULkdIwHu7ix1ibLTM0x')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

deleted = client.v1.webhook_endpoints.delete("we_1Mr5jULkdIwHu7ix1ibLTM0x")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$deleted = $stripe->webhookEndpoints->delete('we_1Mr5jULkdIwHu7ix1ibLTM0x', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

WebhookEndpoint webhookEndpoint =
  client.v1().webhookEndpoints().delete("we_1Mr5jULkdIwHu7ix1ibLTM0x");
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const deleted = await stripe.webhookEndpoints.del('we_1Mr5jULkdIwHu7ix1ibLTM0x');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.WebhookEndpointDeleteParams{}
result, err := sc.V1WebhookEndpoints.Delete(
  context.TODO(), "we_1Mr5jULkdIwHu7ix1ibLTM0x", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.WebhookEndpoints;
WebhookEndpoint deleted = service.Delete("we_1Mr5jULkdIwHu7ix1ibLTM0x");
```

### Response

```json
{
  "id": "we_1Mr5jULkdIwHu7ix1ibLTM0x",
  "object": "webhook_endpoint",
  "deleted": true
}
```