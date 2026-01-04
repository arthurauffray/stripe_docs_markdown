# Update a personalization design

Updates a card personalization object.

## Returns

Returns the updated personalization design object.

## Parameters

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
  Friendly display name. Providing an empty string will set the field to null.

  The maximum length is 200 characters.

- `physical_bundle` (string, optional)
  The physical bundle object belonging to this personalization design.

- `preferences` (object, optional)
  Information on whether this personalization design is used to create cards when one is not specified.

  - `preferences.is_default` (boolean, required)
    Whether we use this personalization design to create cards when one isn’t specified. A connected account uses the Connect platform’s default design if no personalization design is set as the default design.

- `transfer_lookup_key` (boolean, optional)
  If set to true, will atomically remove the lookup key from the existing personalization design, and assign it to this personalization design.

```curl
curl https://api.stripe.com/v1/issuing/personalization_designs/ipcd_Oiw9GXcFRE81LZ \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
```

```cli
stripe issuing personalization_designs update ipcd_Oiw9GXcFRE81LZ \
  -d "metadata[order_id]"=6735
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

personalization_design = client.v1.issuing.personalization_designs.update(
  'ipcd_Oiw9GXcFRE81LZ',
  {metadata: {order_id: '6735'}},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

personalization_design = client.v1.issuing.personalization_designs.update(
  "ipcd_Oiw9GXcFRE81LZ",
  {"metadata": {"order_id": "6735"}},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$personalizationDesign = $stripe->issuing->personalizationDesigns->update(
  'ipcd_Oiw9GXcFRE81LZ',
  ['metadata' => ['order_id' => '6735']]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PersonalizationDesignUpdateParams params =
  PersonalizationDesignUpdateParams.builder()
    .putMetadata("order_id", "6735")
    .build();

PersonalizationDesign personalizationDesign =
  client.v1().issuing().personalizationDesigns().update(
    "ipcd_Oiw9GXcFRE81LZ",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const personalizationDesign = await stripe.issuing.personalizationDesigns.update(
  'ipcd_Oiw9GXcFRE81LZ',
  {
    metadata: {
      order_id: '6735',
    },
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.IssuingPersonalizationDesignUpdateParams{}
params.AddMetadata("order_id", "6735")
result, err := sc.V1IssuingPersonalizationDesigns.Update(
  context.TODO(), "ipcd_Oiw9GXcFRE81LZ", params)
```

```dotnet
var options = new Stripe.Issuing.PersonalizationDesignUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Issuing.PersonalizationDesigns;
Stripe.Issuing.PersonalizationDesign personalizationDesign = service.Update(
    "ipcd_Oiw9GXcFRE81LZ",
    options);
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
  "metadata": {
    "order_id": "6735"
  },
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