# Retrieve a physical bundle

Retrieves a physical bundle object.

## Returns

Returns the physical bundle object.

```curl
curl https://api.stripe.com/v1/issuing/physical_bundles/ics_NLuXJPDYSTjFON \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe issuing physical_bundles retrieve ics_NLuXJPDYSTjFON
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

physical_bundle = client.v1.issuing.physical_bundles.retrieve('ics_NLuXJPDYSTjFON')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

physical_bundle = client.v1.issuing.physical_bundles.retrieve("ics_NLuXJPDYSTjFON")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$physicalBundle = $stripe->issuing->physicalBundles->retrieve(
  'ics_NLuXJPDYSTjFON',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PhysicalBundleRetrieveParams params = PhysicalBundleRetrieveParams.builder().build();

PhysicalBundle physicalBundle =
  client.v1().issuing().physicalBundles().retrieve("ics_NLuXJPDYSTjFON", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const physicalBundle = await stripe.issuing.physicalBundles.retrieve(
  'ics_NLuXJPDYSTjFON'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.IssuingPhysicalBundleRetrieveParams{}
result, err := sc.V1IssuingPhysicalBundles.Retrieve(
  context.TODO(), "ics_NLuXJPDYSTjFON", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Issuing.PhysicalBundles;
Stripe.Issuing.PhysicalBundle physicalBundle = service.Get("ics_NLuXJPDYSTjFON");
```

### Response

```json
{
  "id": "ics_NLuXJPDYSTjFON",
  "object": "issuing.physical_bundle",
  "livemode": false,
  "name": "US Visa Credit White",
  "features": {
    "card_logo": "required",
    "carrier_text": "optional"
  },
  "status": "active",
  "type": "standard"
}
```