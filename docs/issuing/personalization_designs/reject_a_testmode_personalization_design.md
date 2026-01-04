# Reject a testmode personalization design

Updates the `status` of the specified testmode personalization design object to `rejected`.

## Returns

Returns the updated personalization design object.

## Parameters

- `rejection_reasons` (object, required)
  The reason(s) the personalization design was rejected.

  - `rejection_reasons.card_logo` (array of enums, optional)
    The reason(s) the card logo was rejected.
Possible enum values:
    - `geographic_location`
      It improperly uses the name of a geographic location.

    - `inappropriate`
      It contains inappropriate text or images.

    - `network_name`
      It improperly uses the name of a credit card network.

    - `non_binary_image`
      The file uploaded is a non-binary image.

    - `non_fiat_currency`
      It contains a reference to non-fiat currency.

    - `other`
      Other

    - `other_entity`
      It improperly uses the name of another entity.

    - `promotional_material`
      It contains advertising, promotional material, or a tagline.

  - `rejection_reasons.carrier_text` (array of enums, optional)
    The reason(s) the carrier text was rejected.
Possible enum values:
    - `geographic_location`
      It improperly uses the name of a geographic location.

    - `inappropriate`
      It contains inappropriate text or images.

    - `network_name`
      It improperly uses the name of a credit card network.

    - `non_fiat_currency`
      It contains a reference to non-fiat currency.

    - `other`
      Other

    - `other_entity`
      It improperly uses the name of another entity.

    - `promotional_material`
      It contains advertising, promotional material, or a tagline.

```curl
curl https://api.stripe.com/v1/test_helpers/issuing/personalization_designs/ipcd_Oiw9GXcFRE81LZ/reject \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "rejection_reasons[card_logo][]"=network_name \
  -d "rejection_reasons[card_logo][]"=inappropriate \
  -d "rejection_reasons[carrier_text][]"=other
```

```cli
stripe test_helpers issuing personalization_designs reject ipcd_Oiw9GXcFRE81LZ \
  -d "rejection_reasons[card_logo][0]"=network_name \
  -d "rejection_reasons[card_logo][1]"=inappropriate \
  -d "rejection_reasons[carrier_text][0]"=other
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

personalization_design = client.v1.test_helpers.issuing.personalization_designs.reject(
  'ipcd_Oiw9GXcFRE81LZ',
  {
    rejection_reasons: {
      card_logo: ['network_name', 'inappropriate'],
      carrier_text: ['other'],
    },
  },
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

personalization_design = client \
  .v1 \
  .test_helpers \
  .issuing \
  .personalization_designs \
  .reject(
  "ipcd_Oiw9GXcFRE81LZ",
  {
    "rejection_reasons": {
      "card_logo": ["network_name", "inappropriate"],
      "carrier_text": ["other"],
    },
  },
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$personalizationDesign = $stripe->testHelpers->issuing->personalizationDesigns->reject(
  'ipcd_Oiw9GXcFRE81LZ',
  [
    'rejection_reasons' => [
      'card_logo' => ['network_name', 'inappropriate'],
      'carrier_text' => ['other'],
    ],
  ]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PersonalizationDesignRejectParams params =
  PersonalizationDesignRejectParams.builder()
    .setRejectionReasons(
      PersonalizationDesignRejectParams.RejectionReasons.builder()
        .addCardLogo(
          PersonalizationDesignRejectParams.RejectionReasons.CardLogo.NETWORK_NAME
        )
        .addCardLogo(
          PersonalizationDesignRejectParams.RejectionReasons.CardLogo.INAPPROPRIATE
        )
        .addCarrierText(
          PersonalizationDesignRejectParams.RejectionReasons.CarrierText.OTHER
        )
        .build()
    )
    .build();

PersonalizationDesign personalizationDesign =
  client.v1().testHelpers().issuing().personalizationDesigns().reject(
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
  .reject(
  'ipcd_Oiw9GXcFRE81LZ',
  {
    rejection_reasons: {
      card_logo: ['network_name', 'inappropriate'],
      carrier_text: ['other'],
    },
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TestHelpersIssuingPersonalizationDesignRejectParams{
  RejectionReasons: &stripe.TestHelpersIssuingPersonalizationDesignRejectRejectionReasonsParams{
    CardLogo: []*string{
      stripe.String(stripe.IssuingPersonalizationDesignRejectionReasonsCardLogoNetworkName),
      stripe.String(stripe.IssuingPersonalizationDesignRejectionReasonsCardLogoInappropriate),
    },
    CarrierText: []*string{
      stripe.String(stripe.IssuingPersonalizationDesignRejectionReasonsCarrierTextOther),
    },
  },
}
result, err := sc.V1TestHelpersIssuingPersonalizationDesigns.Reject(
  context.TODO(), "ipcd_Oiw9GXcFRE81LZ", params)
```

```dotnet
var options = new Stripe.TestHelpers.Issuing.PersonalizationDesignRejectOptions
{
    RejectionReasons = new Stripe.TestHelpers.Issuing.PersonalizationDesignRejectionReasonsOptions
    {
        CardLogo = new List<string> { "network_name", "inappropriate" },
        CarrierText = new List<string> { "other" },
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.TestHelpers.Issuing.PersonalizationDesigns;
Stripe.Issuing.PersonalizationDesign personalizationDesign = service.Reject(
    "ipcd_Oiw9GXcFRE81LZ",
    options);
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
    "card_logo": [
      "network_name",
      "inappropriate"
    ],
    "carrier_text": [
      "other"
    ]
  },
  "status": "rejected"
}
```