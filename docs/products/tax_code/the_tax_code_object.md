# The Tax Code object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `description` (string)
  A detailed description of which types of products the tax code represents.

- `name` (string)
  A short name for the tax code.

### The Tax Code object

```json
{
  "id": "txcd_99999999",
  "object": "tax_code",
  "description": "Any tangible or physical good. For jurisdictions that impose a tax, the standard rate is applied.",
  "name": "General - Tangible Goods"
}
```