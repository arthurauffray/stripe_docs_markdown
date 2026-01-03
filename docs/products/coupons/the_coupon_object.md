# The Coupon object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `amount_off` (integer, nullable)
  Amount (in the `currency` specified) that will be taken off the subtotal of any invoices for this customer.

- `applies_to` (object, nullable)
  Contains information about what this coupon applies to.

  - `applies_to.products` (array of strings)
    A list of product IDs this coupon applies to

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (enum, nullable)
  If `amount_off` has been set, the three-letter [ISO code for the currency](https://stripe.com/docs/currencies) of the amount to take off.

- `currency_options` (object, nullable)
  Coupons defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).

  - `currency_options.<currency>.amount_off` (integer)
    Amount (in the `currency` specified) that will be taken off the subtotal of any invoices for this customer.

- `duration` (enum)
  One of `forever`, `once`, or `repeating`. Describes how long a customer who applies this coupon will get the discount.
Possible enum values:
  - `forever`
    Applies to all charges from a subscription with this coupon applied.

  - `once`
    Applies to the first charge from a subscription with this coupon applied.

  - `repeating`
    Applies to charges in the first `duration_in_months` months from a subscription with this coupon applied.

- `duration_in_months` (integer, nullable)
  If `duration` is `repeating`, the number of months the coupon applies. Null if coupon `duration` is `forever` or `once`.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `max_redemptions` (integer, nullable)
  Maximum number of times this coupon can be redeemed, in total, across all customers, before it is no longer valid.

- `metadata` (object, nullable)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `name` (string, nullable)
  Name of the coupon displayed to customers on for instance invoices or receipts.

- `percent_off` (float, nullable)
  Percent that will be taken off the subtotal of any invoices for this customer for the duration of the coupon. For example, a coupon with percent_off of 50 will make a $100 invoice $50 instead.

- `redeem_by` (timestamp, nullable)
  Date after which the coupon can no longer be redeemed.

- `times_redeemed` (integer)
  Number of times this coupon has been applied to a customer.

- `valid` (boolean)
  Taking account of the above properties, whether this coupon can still be applied to a customer.

### The Coupon object

```json
{
  "id": "jMT0WJUD",
  "object": "coupon",
  "amount_off": null,
  "created": 1678037688,
  "currency": null,
  "duration": "repeating",
  "duration_in_months": 3,
  "livemode": false,
  "max_redemptions": null,
  "metadata": {},
  "name": null,
  "percent_off": 25.5,
  "redeem_by": null,
  "times_redeemed": 0,
  "valid": true
}
```