# The Physical Bundle object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `features` (object)
  Information about the features available for this physical bundle.

  - `features.card_logo` (enum)
    The policy for how to use card logo images in a card design with this physical bundle.
Possible enum values:
    - `optional`
      You can use the feature in a personalization design or card with this physical bundle.

    - `required`
      You must use the feature in a personalization design or card with this physical bundle.

    - `unsupported`
      You can’t use the feature in a personalization design or card with this physical bundle.

  - `features.carrier_text` (enum)
    The policy for how to use carrier letter text in a card design with this physical bundle.
Possible enum values:
    - `optional`
      You can use the feature in a personalization design or card with this physical bundle.

    - `required`
      You must use the feature in a personalization design or card with this physical bundle.

    - `unsupported`
      You can’t use the feature in a personalization design or card with this physical bundle.

  - `features.second_line` (enum)
    The policy for how to use a second line on a card with this physical bundle.
Possible enum values:
    - `optional`
      You can use the feature in a personalization design or card with this physical bundle.

    - `required`
      You must use the feature in a personalization design or card with this physical bundle.

    - `unsupported`
      You can’t use the feature in a personalization design or card with this physical bundle.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `name` (string)
  Friendly display name.

- `status` (enum)
  Whether this physical bundle can be used to create cards.
Possible enum values:
  - `active`
    Can be used to create cards that fulfill immediately.

  - `inactive`
    Cannot be used to create cards.

  - `review`
    Can be used to create cards but cards will only be fulfilled when this physical bundle is activated.

- `type` (enum)
  Whether this physical bundle is a standard Stripe offering or custom-made for you.
Possible enum values:
  - `custom`
    Available only to you, you manage design and inventory.

  - `standard`
    Publicly available, Stripe manages design and inventory.

### The Physical Bundle object

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