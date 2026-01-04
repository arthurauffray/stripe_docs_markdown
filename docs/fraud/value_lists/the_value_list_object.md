# The Value List object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `alias` (string)
  The name of the value list for use in rules.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `created_by` (string)
  The name or email address of the user who created this value list.

- `item_type` (enum)
  The type of items in the value list. One of `card_fingerprint`, `card_bin`, `email`, `ip_address`, `country`, `string`, `case_sensitive_string`, `customer_id`, `sepa_debit_fingerprint`, or `us_bank_account_fingerprint`.
Possible enum values:
  - `card_bin`
  - `card_fingerprint`
  - `case_sensitive_string`
  - `country`
  - `customer_id`
  - `email`
  - `ip_address`
  - `sepa_debit_fingerprint`
  - `string`
  - `us_bank_account_fingerprint`

- `list_items` (object)
  List of items contained within this value list.

  - `list_items.object` (string)
    String representing the object’s type. Objects of the same type share the same value. Always has the value `list`.

  - `list_items.data` (array of objects)
    Details about each object.

    - `list_items.data.id` (string)
      Unique identifier for the object.

    - `list_items.data.object` (string)
      String representing the object’s type. Objects of the same type share the same value.

    - `list_items.data.created` (timestamp)
      Time at which the object was created. Measured in seconds since the Unix epoch.

    - `list_items.data.created_by` (string)
      The name or email address of the user who added this item to the value list.

    - `list_items.data.livemode` (boolean)
      Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

    - `list_items.data.value` (string)
      The value of the item.

    - `list_items.data.value_list` (string)
      The identifier of the value list this item belongs to.

  - `list_items.has_more` (boolean)
    True if this list has another page of items after this one that can be fetched.

  - `list_items.url` (string)
    The URL where this list can be accessed.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `name` (string)
  The name of the value list.

### The Value List object

```json
{
  "id": "rsl_1MrQSwLkdIwHu7ixWOGS5c8M",
  "object": "radar.value_list",
  "alias": "custom_ip_blocklist",
  "created": 1680201894,
  "created_by": "API",
  "item_type": "ip_address",
  "list_items": {
    "object": "list",
    "data": [],
    "has_more": false,
    "total_count": 0,
    "url": "/v1/radar/value_list_items?value_list=rsl_1MrQSwLkdIwHu7ixWOGS5c8M"
  },
  "livemode": false,
  "metadata": {},
  "name": "Custom IP Blocklist"
}
```