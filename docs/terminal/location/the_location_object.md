# The Location object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `address` (object)
  The full address of the location.

  - `address.city` (string, nullable)
    City, district, suburb, town, or village.

  - `address.country` (string, nullable)
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

  - `address.line1` (string, nullable)
    Address line 1, such as the street, PO Box, or company name.

  - `address.line2` (string, nullable)
    Address line 2, such as the apartment, suite, unit, or building.

  - `address.postal_code` (string, nullable)
    ZIP or postal code.

  - `address.state` (string, nullable)
    State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

- `address_kana` (object, nullable)
  The Kana variation of the full address of the location (Japan only).

  - `address_kana.city` (string, nullable)
    City/Ward.

  - `address_kana.country` (string, nullable)
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

  - `address_kana.line1` (string, nullable)
    Block/Building number.

  - `address_kana.line2` (string, nullable)
    Building details.

  - `address_kana.postal_code` (string, nullable)
    ZIP or postal code.

  - `address_kana.state` (string, nullable)
    Prefecture.

  - `address_kana.town` (string, nullable)
    Town/cho-me.

- `address_kanji` (object, nullable)
  The Kanji variation of the full address of the location (Japan only).

  - `address_kanji.city` (string, nullable)
    City/Ward.

  - `address_kanji.country` (string, nullable)
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

  - `address_kanji.line1` (string, nullable)
    Block/Building number.

  - `address_kanji.line2` (string, nullable)
    Building details.

  - `address_kanji.postal_code` (string, nullable)
    ZIP or postal code.

  - `address_kanji.state` (string, nullable)
    Prefecture.

  - `address_kanji.town` (string, nullable)
    Town/cho-me.

- `configuration_overrides` (string, nullable)
  The ID of a configuration that will be used to customize all readers in this location.

- `display_name` (string)
  The display name of the location.

- `display_name_kana` (string, nullable)
  The Kana variation of the display name of the location.

- `display_name_kanji` (string, nullable)
  The Kanji variation of the display name of the location.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `phone` (string, nullable)
  The phone number of the location.

### The Location object

```json
{
  "id": "tml_FBakXQG8bQk4Mm",
  "object": "terminal.location",
  "address": {
    "city": "San Francisco",
    "country": "US",
    "line1": "1234 Main Street",
    "line2": "",
    "postal_code": "94111",
    "state": "CA"
  },
  "display_name": "My First Store",
  "livemode": false,
  "metadata": {}
}
```