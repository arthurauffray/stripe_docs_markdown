# Retrieve a supplier

Retrieves a Climate supplier object.

## Returns

A Climate supplier object.

```curl
curl https://api.stripe.com/v1/climate/suppliers/climsup_charm_industrial \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe climate suppliers retrieve climsup_charm_industrial
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

supplier = client.v1.climate.suppliers.retrieve('climsup_charm_industrial')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

supplier = client.v1.climate.suppliers.retrieve("climsup_charm_industrial")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$supplier = $stripe->climate->suppliers->retrieve('climsup_charm_industrial', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

SupplierRetrieveParams params = SupplierRetrieveParams.builder().build();

Supplier supplier =
  client.v1().climate().suppliers().retrieve("climsup_charm_industrial", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const supplier = await stripe.climate.suppliers.retrieve('climsup_charm_industrial');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.ClimateSupplierRetrieveParams{}
result, err := sc.V1ClimateSuppliers.Retrieve(
  context.TODO(), "climsup_charm_industrial", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Climate.Suppliers;
Stripe.Climate.Supplier supplier = service.Get("climsup_charm_industrial");
```

### Response

```json
{
  "id": "climsup_charm_industrial",
  "object": "climate.supplier",
  "info_url": "https://frontierclimate.com/portfolio/charm-industrial",
  "livemode": false,
  "locations": [
    {
      "city": "San Francisco",
      "country": "US",
      "latitude": 37.7749,
      "longitude": -122.4194,
      "region": "CA"
    }
  ],
  "name": "Charm Industrial",
  "removal_pathway": "biomass_carbon_removal_and_storage"
}
```