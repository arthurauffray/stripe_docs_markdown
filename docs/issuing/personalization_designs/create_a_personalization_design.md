# Create a personalization design

Creates a personalization design object.

## Returns

Returns the created personalization design object.

## Parameters

- `physical_bundle` (string, required)
  The physical bundle object belonging to this personalization design.

- `card_logo` (string, optional)
  The file for the card logo, for use with physical bundles that support card logos. Must have a `purpose` value of `issuing_logo`.

- `carrier_text` (object, optional)
  Hash containing carrier text, for use with physical bundles that support carrier text.

  - `carrier_text.footer_body` (string, optional)
    The footer body text of the carrier letter.

    The maximum length is 200 characters.

  - `carrier_text.footer_title` (string, optional)
    The footer title text of the carrier letter.

    The maximum length is 30 characters.

  - `carrier_text.header_body` (string, optional)
    The header body text of the carrier letter.

    The maximum length is 200 characters.

  - `carrier_text.header_title` (string, optional)
    The header title text of the carrier letter.

    The maximum length is 30 characters.

- `lookup_key` (string, optional)
  A lookup key used to retrieve personalization designs dynamically from a static string. This may be up to 200 characters.

  The maximum length is 200 characters.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `name` (string, optional)
  Friendly display name.

  The maximum length is 200 characters.

- `preferences` (object, optional)
  Information on whether this personalization design is used to create cards when one is not specified.

  - `preferences.is_default` (boolean, required)
    Whether we use this personalization design to create cards when one isn’t specified. A connected account uses the Connect platform’s default design if no personalization design is set as the default design.

- `transfer_lookup_key` (boolean, optional)
  If set to true, will atomically remove the lookup key from the existing personalization design, and assign it to this personalization design.

```curl
curl https://api.stripe.com/v1/issuing/personalization_designs \
  -u "<<YOUR_SECRET_KEY>>" \
  -d name="My personalization design name" \
  -d "preferences[is_default]"=false \
  -d card_logo=file_1LzR9L2eZvKYlo2CelTpcvKu \
  -d physical_bundle=ics_Oiw9ahglMfql0U
```

```cli
stripe issuing personalization_designs create  \
  --name="My personalization design name" \
  -d "preferences[is_default]"=false \
  --card-logo=file_1LzR9L2eZvKYlo2CelTpcvKu \
  --physical-bundle=ics_Oiw9ahglMfql0U
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

personalization_design = client.v1.issuing.personalization_designs.create({
  name: 'My personalization design name',
  preferences: {is_default: false},
  card_logo: 'file_1LzR9L2eZvKYlo2CelTpcvKu',
  physical_bundle: 'ics_Oiw9ahglMfql0U',
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

personalization_design = client.v1.issuing.personalization_designs.create({
  "name": "My personalization design name",
  "preferences": {"is_default": False},
  "card_logo": "file_1LzR9L2eZvKYlo2CelTpcvKu",
  "physical_bundle": "ics_Oiw9ahglMfql0U",
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$personalizationDesign = $stripe->issuing->personalizationDesigns->create([
  'name' => 'My personalization design name',
  'preferences' => ['is_default' => false],
  'card_logo' => 'file_1LzR9L2eZvKYlo2CelTpcvKu',
  'physical_bundle' => 'ics_Oiw9ahglMfql0U',
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PersonalizationDesignCreateParams params =
  PersonalizationDesignCreateParams.builder()
    .setName("My personalization design name")
    .setPreferences(
      PersonalizationDesignCreateParams.Preferences.builder()
        .setIsDefault(false)
        .build()
    )
    .setCardLogo("file_1LzR9L2eZvKYlo2CelTpcvKu")
    .setPhysicalBundle("ics_Oiw9ahglMfql0U")
    .build();

PersonalizationDesign personalizationDesign =
  client.v1().issuing().personalizationDesigns().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const personalizationDesign = await stripe.issuing.personalizationDesigns.create({
  name: 'My personalization design name',
  preferences: {
    is_default: false,
  },
  card_logo: 'file_1LzR9L2eZvKYlo2CelTpcvKu',
  physical_bundle: 'ics_Oiw9ahglMfql0U',
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.IssuingPersonalizationDesignCreateParams{
  Name: stripe.String("My personalization design name"),
  Preferences: &stripe.IssuingPersonalizationDesignCreatePreferencesParams{
    IsDefault: stripe.Bool(false),
  },
  CardLogo: stripe.String("file_1LzR9L2eZvKYlo2CelTpcvKu"),
  PhysicalBundle: stripe.String("ics_Oiw9ahglMfql0U"),
}
result, err := sc.V1IssuingPersonalizationDesigns.Create(context.TODO(), params)
```

```dotnet
var options = new Stripe.Issuing.PersonalizationDesignCreateOptions
{
    Name = "My personalization design name",
    Preferences = new Stripe.Issuing.PersonalizationDesignPreferencesOptions
    {
        IsDefault = false,
    },
    CardLogo = "file_1LzR9L2eZvKYlo2CelTpcvKu",
    PhysicalBundle = "ics_Oiw9ahglMfql0U",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Issuing.PersonalizationDesigns;
Stripe.Issuing.PersonalizationDesign personalizationDesign = service.Create(options);
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