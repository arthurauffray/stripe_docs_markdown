# Activate a testmode personalization design

Updates the `status` of the specified testmode personalization design object to `active`.

## Returns

Returns the updated personalization design object.

```curl
curl -X POST https://api.stripe.com/v1/test_helpers/issuing/personalization_designs/ipcd_Oiw9GXcFRE81LZ/activate \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe test_helpers issuing personalization_designs activate ipcd_Oiw9GXcFRE81LZ
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

personalization_design = client.v1.test_helpers.issuing.personalization_designs.activate('ipcd_Oiw9GXcFRE81LZ')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

personalization_design = client \
  .v1 \
  .test_helpers \
  .issuing \
  .personalization_designs \
  .activate("ipcd_Oiw9GXcFRE81LZ")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$personalizationDesign = $stripe->testHelpers->issuing->personalizationDesigns->activate(
  'ipcd_Oiw9GXcFRE81LZ',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PersonalizationDesignActivateParams params =
  PersonalizationDesignActivateParams.builder().build();

PersonalizationDesign personalizationDesign =
  client.v1().testHelpers().issuing().personalizationDesigns().activate(
    "ipcd_Oiw9GXcFRE81LZ",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const personalizationDesign = await stripe
  .testHelpers
  .issuing
  .personalizationDesigns
  .activate('ipcd_Oiw9GXcFRE81LZ');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TestHelpersIssuingPersonalizationDesignActivateParams{}
result, err := sc.V1TestHelpersIssuingPersonalizationDesigns.Activate(
  context.TODO(), "ipcd_Oiw9GXcFRE81LZ", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.TestHelpers.Issuing.PersonalizationDesigns;
Stripe.Issuing.PersonalizationDesign personalizationDesign = service.Activate(
    "ipcd_Oiw9GXcFRE81LZ");
```

### Response

```json
{
  "id": "ipcd_Oiw9GXcFRE81LZ",
  "object": "issuing.personalization_design",
  "livemode": false,
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
  "status": "active"
}
```