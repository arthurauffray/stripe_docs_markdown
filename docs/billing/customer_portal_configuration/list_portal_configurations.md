# List portal configurations

Returns a list of configurations that describe the functionality of the customer portal.

## Returns

Returns a list of portal configuration objects.

## Parameters

- `active` (boolean, optional)
  Only return configurations that are active or inactive (e.g., pass `true` to only list active configurations).

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `is_default` (boolean, optional)
  Only return the default or non-default configurations (e.g., pass `true` to only list the default configuration).

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/billing_portal/configurations \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe billing_portal configurations list  \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

configurations = client.v1.billing_portal.configurations.list({limit: 3})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

configurations = client.v1.billing_portal.configurations.list({"limit": 3})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$configurations = $stripe->billingPortal->configurations->all(['limit' => 3]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ConfigurationListParams params =
  ConfigurationListParams.builder().setLimit(3L).build();

StripeCollection<Configuration> stripeCollection =
  client.v1().billingPortal().configurations().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const configurations = await stripe.billingPortal.configurations.list({
  limit: 3,
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.BillingPortalConfigurationListParams{}
params.Limit = stripe.Int64(3)
result := sc.V1BillingPortalConfigurations.List(context.TODO(), params)
```

```dotnet
var options = new Stripe.BillingPortal.ConfigurationListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.BillingPortal.Configurations;
StripeList<Stripe.BillingPortal.Configuration> configurations = service.List(
    options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/billing_portal/configurations",
  "has_more": false,
  "data": [
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
  ]
}
```