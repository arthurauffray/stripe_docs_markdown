# The Product object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `active` (boolean)
  Whether the product is currently available for purchase.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `default_price` (string, nullable)
  The ID of the [Price](https://docs.stripe.com/docs/api/prices.md) object that is the default price for this product.

- `description` (string, nullable)
  The product’s description, meant to be displayable to the customer. Use this field to optionally store a long form explanation of the product being sold for your own rendering purposes.

- `images` (array of strings)
  A list of up to 8 URLs of images for this product, meant to be displayable to the customer.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `marketing_features` (array of objects)
  A list of up to 15 marketing features for this product. These are displayed in [pricing tables](https://docs.stripe.com/docs/payments/checkout/pricing-table.md).

  - `marketing_features.name` (string, nullable)
    The marketing feature name. Up to 80 characters long.

- `metadata` (object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `name` (string)
  The product’s name, meant to be displayable to the customer.

- `package_dimensions` (object, nullable)
  The dimensions of this product for shipping purposes.

  - `package_dimensions.height` (float)
    Height, in inches.

  - `package_dimensions.length` (float)
    Length, in inches.

  - `package_dimensions.weight` (float)
    Weight, in ounces.

  - `package_dimensions.width` (float)
    Width, in inches.

- `shippable` (boolean, nullable)
  Whether this product is shipped (i.e., physical goods).

- `statement_descriptor` (string, nullable)
  Extra information about a product which will appear on your customer’s credit card statement. In the case that multiple products are billed at once, the first statement descriptor will be used. Only used for subscription payments.

- `tax_code` (string, nullable)
  A [tax code](https://docs.stripe.com/docs/tax/tax-categories.md) ID.

- `unit_label` (string, nullable)
  A label that represents units of this product. When set, this will be included in customers’ receipts, invoices, Checkout, and the customer portal.

- `updated` (timestamp)
  Time at which the object was last updated. Measured in seconds since the Unix epoch.

- `url` (string, nullable)
  A URL of a publicly-accessible webpage for this product.

### The Product object

```json
{
  "id": "prod_NWjs8kKbJWmuuc",
  "object": "product",
  "active": true,
  "created": 1678833149,
  "default_price": null,
  "description": null,
  "images": [],
  "marketing_features": [],
  "livemode": false,
  "metadata": {},
  "name": "Gold Plan",
  "package_dimensions": null,
  "shippable": null,
  "statement_descriptor": null,
  "tax_code": null,
  "unit_label": null,
  "updated": 1678833149,
  "url": null
}
```