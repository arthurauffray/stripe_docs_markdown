# List suppliers

Lists all available Climate supplier objects.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` suppliers, starting after supplier `starting_after`. Each entry in the array is a separate supplier object. If no more suppliers are available, the resulting array is empty.

## Parameters

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/climate/suppliers \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe climate suppliers list  \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

suppliers = client.v1.climate.suppliers.list({limit: 3})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

suppliers = client.v1.climate.suppliers.list({"limit": 3})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$suppliers = $stripe->climate->suppliers->all(['limit' => 3]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

SupplierListParams params = SupplierListParams.builder().setLimit(3L).build();

StripeCollection<Supplier> stripeCollection =
  client.v1().climate().suppliers().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const suppliers = await stripe.climate.suppliers.list({
  limit: 3,
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.ClimateSupplierListParams{}
params.Limit = stripe.Int64(3)
result := sc.V1ClimateSuppliers.List(context.TODO(), params)
```

```dotnet
var options = new Stripe.Climate.SupplierListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Climate.Suppliers;
StripeList<Stripe.Climate.Supplier> suppliers = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/climate/suppliers",
  "has_more": false,
  "data": [
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
  ]
}
```