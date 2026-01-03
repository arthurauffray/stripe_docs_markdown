# Retrieve a webhook endpoint

Retrieves the webhook endpoint with the given ID.

## Returns

Returns a webhook endpoint if a valid webhook endpoint ID was provided. Raises [an error](https://docs.stripe.com/api/webhook_endpoints/retrieve.md#errors) otherwise.

```curl
curl https://api.stripe.com/v1/webhook_endpoints/we_1Mr5jULkdIwHu7ix1ibLTM0x \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe webhook_endpoints retrieve we_1Mr5jULkdIwHu7ix1ibLTM0x
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

webhook_endpoint = client.v1.webhook_endpoints.retrieve('we_1Mr5jULkdIwHu7ix1ibLTM0x')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

webhook_endpoint = client.v1.webhook_endpoints.retrieve(
  "we_1Mr5jULkdIwHu7ix1ibLTM0x",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$webhookEndpoint = $stripe->webhookEndpoints->retrieve(
  'we_1Mr5jULkdIwHu7ix1ibLTM0x',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

WebhookEndpointRetrieveParams params =
  WebhookEndpointRetrieveParams.builder().build();

WebhookEndpoint webhookEndpoint =
  client.v1().webhookEndpoints().retrieve("we_1Mr5jULkdIwHu7ix1ibLTM0x", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const webhookEndpoint = await stripe.webhookEndpoints.retrieve(
  'we_1Mr5jULkdIwHu7ix1ibLTM0x'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.WebhookEndpointRetrieveParams{}
result, err := sc.V1WebhookEndpoints.Retrieve(
  context.TODO(), "we_1Mr5jULkdIwHu7ix1ibLTM0x", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.WebhookEndpoints;
WebhookEndpoint webhookEndpoint = service.Get("we_1Mr5jULkdIwHu7ix1ibLTM0x");
```

### Response

```json
{
  "id": "we_1Mr5jULkdIwHu7ix1ibLTM0x",
  "object": "webhook_endpoint",
  "api_version": null,
  "application": null,
  "created": 1680122196,
  "description": null,
  "enabled_events": [
    "charge.succeeded",
    "charge.failed"
  ],
  "livemode": false,
  "metadata": {},
  "status": "enabled",
  "url": "https://example.com/my/webhook/endpoint"
}
```