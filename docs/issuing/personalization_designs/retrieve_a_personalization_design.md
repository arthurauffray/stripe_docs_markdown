# Retrieve a personalization design

Retrieves a personalization design object.

## Returns

Returns the personalization design object.

```curl
curl https://api.stripe.com/v1/issuing/personalization_designs/ipcd_Oiw9GXcFRE81LZ \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe issuing personalization_designs retrieve ipcd_Oiw9GXcFRE81LZ
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

personalization_design = client.v1.issuing.personalization_designs.retrieve('ipcd_Oiw9GXcFRE81LZ')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

personalization_design = client.v1.issuing.personalization_designs.retrieve(
  "ipcd_Oiw9GXcFRE81LZ",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$personalizationDesign = $stripe->issuing->personalizationDesigns->retrieve(
  'ipcd_Oiw9GXcFRE81LZ',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PersonalizationDesignRetrieveParams params =
  PersonalizationDesignRetrieveParams.builder().build();

PersonalizationDesign personalizationDesign =
  client.v1().issuing().personalizationDesigns().retrieve(
    "ipcd_Oiw9GXcFRE81LZ",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const personalizationDesign = await stripe.issuing.personalizationDesigns.retrieve(
  'ipcd_Oiw9GXcFRE81LZ'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.IssuingPersonalizationDesignRetrieveParams{}
result, err := sc.V1IssuingPersonalizationDesigns.Retrieve(
  context.TODO(), "ipcd_Oiw9GXcFRE81LZ", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Issuing.PersonalizationDesigns;
Stripe.Issuing.PersonalizationDesign personalizationDesign = service.Get(
    "ipcd_Oiw9GXcFRE81LZ");
```

### Response

```json
{
  "id": "ipcd_Oiw9GXcFRE81LZ",
  "object": "issuing.personalization_design",
  "livemode": true,
  "card_logo": "file_1LzR9L2eZvKYlo2CelTpcvKu",
  "carrier_text": null,
  "lookup_key": "my_card_design_lookup_key",
  "metadata": {},
  "name": "My personalization design name",
  "physical_bundle": "ics_Oiw9ahglMfql0U",
  "preferences": {
    "is_default": false
  },
  "rejection_reasons": {
    "card_logo": [],
    "carrier_text": []
  },
  "status": "review"
}
```