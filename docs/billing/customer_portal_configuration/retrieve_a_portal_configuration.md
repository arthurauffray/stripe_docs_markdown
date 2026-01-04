# Retrieve a portal configuration

Retrieves a configuration that describes the functionality of the customer portal.

## Returns

Returns a portal configuration object.

```curl
curl https://api.stripe.com/v1/billing_portal/configurations/bpc_1MrnZsLkdIwHu7ixNiQL1xPM \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe billing_portal configurations retrieve bpc_1MrnZsLkdIwHu7ixNiQL1xPM
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

configuration = client.v1.billing_portal.configurations.retrieve('bpc_1MrnZsLkdIwHu7ixNiQL1xPM')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

configuration = client.v1.billing_portal.configurations.retrieve(
  "bpc_1MrnZsLkdIwHu7ixNiQL1xPM",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$configuration = $stripe->billingPortal->configurations->retrieve(
  'bpc_1MrnZsLkdIwHu7ixNiQL1xPM',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ConfigurationRetrieveParams params = ConfigurationRetrieveParams.builder().build();

Configuration configuration =
  client.v1().billingPortal().configurations().retrieve(
    "bpc_1MrnZsLkdIwHu7ixNiQL1xPM",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const configuration = await stripe.billingPortal.configurations.retrieve(
  'bpc_1MrnZsLkdIwHu7ixNiQL1xPM'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.BillingPortalConfigurationRetrieveParams{}
result, err := sc.V1BillingPortalConfigurations.Retrieve(
  context.TODO(), "bpc_1MrnZsLkdIwHu7ixNiQL1xPM", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.BillingPortal.Configurations;
Stripe.BillingPortal.Configuration configuration = service.Get(
    "bpc_1MrnZsLkdIwHu7ixNiQL1xPM");
```

### Response

```json
{
  "id": "bpc_1MrnZsLkdIwHu7ixNiQL1xPM",
  "object": "billing_portal.configuration",
  "active": true,
  "application": null,
  "business_profile": {
    "headline": null,
    "privacy_policy_url": null,
    "terms_of_service_url": null
  },
  "created": 1680290736,
  "default_return_url": null,
  "features": {
    "customer_update": {
      "allowed_updates": [
        "email",
        "tax_id"
      ],
      "enabled": true
    },
    "invoice_history": {
      "enabled": true
    },
    "payment_method_update": {
      "enabled": false
    },
    "subscription_cancel": {
      "cancellation_reason": {
        "enabled": false,
        "options": [
          "too_expensive",
          "missing_features",
          "switched_service",
          "unused",
          "other"
        ]
      },
      "enabled": false,
      "mode": "at_period_end",
      "proration_behavior": "none"
    },
    "subscription_update": {
      "default_allowed_updates": [],
      "enabled": false,
      "proration_behavior": "none"
    }
  },
  "is_default": false,
  "livemode": false,
  "login_page": {
    "enabled": false,
    "url": null
  },
  "metadata": {},
  "updated": 1680290736
}
```