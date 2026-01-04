# Retrieve settings

Retrieves Tax `Settings` for a merchant.

## Returns

A Tax `Settings` object.

```curl
curl https://api.stripe.com/v1/tax/settings \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe tax settings retrieve
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

settings = client.v1.tax.settings.retrieve()
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

settings = client.v1.tax.settings.retrieve()
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$settings = $stripe->tax->settings->retrieve([]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

SettingsRetrieveParams params = SettingsRetrieveParams.builder().build();

Settings settings = client.v1().tax().settings().retrieve(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const settings = await stripe.tax.settings.retrieve();
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TaxSettingsRetrieveParams{}
result, err := sc.V1TaxSettings.Retrieve(context.TODO(), params)
```

```dotnet
var options = new Stripe.Tax.SettingsGetOptions();
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Tax.Settings;
Stripe.Tax.Settings settings = service.Get(options);
```

### Response

```json
{
  "object": "tax.settings",
  "defaults": {
    "tax_behavior": null,
    "tax_code": "txcd_10000000"
  },
  "head_office": {
    "address": {
      "city": null,
      "country": "US",
      "line1": null,
      "line2": null,
      "postal_code": null,
      "state": "CA"
    }
  },
  "livemode": false,
  "status": "active",
  "status_details": {
    "active": {}
  }
}
```