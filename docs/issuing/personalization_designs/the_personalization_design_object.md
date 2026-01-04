# The Personalization Design object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `card_logo` (string, nullable)
  The file for the card logo to use with physical bundles that support card logos. Must have a `purpose` value of `issuing_logo`.

- `carrier_text` (object, nullable)
  Hash containing carrier text, for use with physical bundles that support carrier text.

  - `carrier_text.footer_body` (string, nullable)
    The footer body text of the carrier letter.

  - `carrier_text.footer_title` (string, nullable)
    The footer title text of the carrier letter.

  - `carrier_text.header_body` (string, nullable)
    The header body text of the carrier letter.

  - `carrier_text.header_title` (string, nullable)
    The header title text of the carrier letter.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `lookup_key` (string, nullable)
  A lookup key used to retrieve personalization designs dynamically from a static string. This may be up to 200 characters.

- `metadata` (object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `name` (string, nullable)
  Friendly display name.

- `physical_bundle` (string)
  The physical bundle object belonging to this personalization design.

- `preferences` (object)
  Hash containing information on whether this personalization design is used to create cards when one is not specified.

  - `preferences.is_default` (boolean)
    Whether we use this personalization design to create cards when one isn’t specified. A connected account uses the Connect platform’s default design if no personalization design is set as the default design.

  - `preferences.is_platform_default` (boolean, nullable)
    Whether this personalization design is used to create cards when one is not specified and a default for this connected account does not exist.

- `rejection_reasons` (object)
  Hash containing reasons why the personalization design was rejected.

  - `rejection_reasons.card_logo` (array of enums, nullable)
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

  - `rejection_reasons.carrier_text` (array of enums, nullable)
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

- `status` (enum)
  Whether this personalization design can be used to create cards.
Possible enum values:
  - `active`
    Personalization design can be used to create cards that fulfill immediately.

  - `inactive`
    Personalization design cannot be used to create cards because it was deactivated.

  - `rejected`
    Personalization design cannot be used to create cards because it was rejected by design review.

  - `review`
    Personalization design can be used to create cards but cards will only be fulfilled once the personalization design is activated.

### The Personalization Design object

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