# Retrieve a tax ID

Retrieves an account or customer `tax_id` object.

## Returns

Returns a `tax_id` object if a valid identifier was provided.

```curl
curl https://api.stripe.com/v1/tax_ids/txi_1NuMB12eZvKYlo2CMecoWkZd \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe tax_ids retrieve txi_1NuMB12eZvKYlo2CMecoWkZd
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

tax_id = client.v1.tax_ids.retrieve('txi_1NuMB12eZvKYlo2CMecoWkZd')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

tax_id = client.v1.tax_ids.retrieve("txi_1NuMB12eZvKYlo2CMecoWkZd")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$taxId = $stripe->taxIds->retrieve('txi_1NuMB12eZvKYlo2CMecoWkZd', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TaxIdRetrieveParams params = TaxIdRetrieveParams.builder().build();

TaxId taxId = client.v1().taxIds().retrieve("txi_1NuMB12eZvKYlo2CMecoWkZd", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const taxId = await stripe.taxIds.retrieve('txi_1NuMB12eZvKYlo2CMecoWkZd');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TaxIDRetrieveParams{}
result, err := sc.V1TaxIDs.Retrieve(
  context.TODO(), "txi_1NuMB12eZvKYlo2CMecoWkZd", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.TaxIds;
TaxId taxId = service.Get("txi_1NuMB12eZvKYlo2CMecoWkZd");
```

### Response

```json
{
  "id": "txi_1NuMB12eZvKYlo2CMecoWkZd",
  "object": "tax_id",
  "country": "DE",
  "created": 123456789,
  "customer": null,
  "livemode": false,
  "type": "eu_vat",
  "value": "DE123456789",
  "verification": null,
  "owner": {
    "type": "self",
    "customer": null
  }
}
```