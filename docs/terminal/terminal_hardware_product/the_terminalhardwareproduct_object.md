# The TerminalHardwareProduct object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `status` (enum)
  The status of the terminal hardware product.
Possible enum values:
  - `available`
    Available for new orders.

  - `unavailable`
    Can no longer be used for order creation.

- `type` (string)
  The type of product.

- `unavailable_after` (integer, nullable)
  If all the SKUs for this product have an unavailable_after then this is the max unavailable_after in UNIX timestamp. Otherwise, null.

### The TerminalHardwareProduct object

```json
{
  "id": "thpr_MJfotcxYT5Hwsm",
  "object": "terminal.hardware_product",
  "status": "available",
  "type": "bbpos_wisepos_e",
  "unavailable_after": null
}
```