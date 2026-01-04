# The Value List Item object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `created_by` (string)
  The name or email address of the user who added this item to the value list.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `value` (string)
  The value of the item.

- `value_list` (string)
  The identifier of the value list this item belongs to.

### The Value List Item object

```json
{
  "id": "rsli_1MxxosLkdIwHu7ixxvA1yKiZ",
  "object": "radar.value_list_item",
  "created": 1681760074,
  "created_by": "API",
  "livemode": false,
  "value": "1.2.3.4",
  "value_list": "rsl_1MxxosLkdIwHu7ixNiiD01Kj"
}
```