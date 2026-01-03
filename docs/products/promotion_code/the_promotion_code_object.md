# The Promotion Code object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `active` (boolean)
  Whether the promotion code is currently active. A promotion code is only active if the coupon is also valid.

- `code` (string)
  The customer-facing code. Regardless of case, this code must be unique across all active promotion codes for each customer. Valid characters are lower case letters (a-z), upper case letters (A-Z), and digits (0-9).

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `customer` (string, nullable)
  The customer who can use this promotion code.

- `customer_account` (string, nullable)
  The account representing the customer who can use this promotion code.

- `expires_at` (timestamp, nullable)
  Date at which the promotion code can no longer be redeemed.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `max_redemptions` (integer, nullable)
  Maximum number of times this promotion code can be redeemed.

- `metadata` (object, nullable)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `promotion` (object)
  The promotion referenced by this promotion code.

  - `promotion.coupon` (string, nullable)
    If promotion `type` is `coupon`, the coupon for this promotion.

  - `promotion.type` (enum)
    The type of promotion.
Possible enum values:
    - `coupon`
      Coupon promotion type.

- `restrictions` (object)
  Settings that restrict the redemption of the promotion code.

  - `restrictions.currency_options` (object, nullable)
    Promotion code restrictions defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).

    - `restrictions.currency_options.<currency>.minimum_amount` (integer)
      Minimum amount required to redeem this Promotion Code into a Coupon (e.g., a purchase must be $100 or more to work).

  - `restrictions.first_time_transaction` (boolean)
    A Boolean indicating if the Promotion Code should only be redeemed for Customers without any successful payments or invoices

  - `restrictions.minimum_amount` (integer, nullable)
    Minimum amount required to redeem this Promotion Code into a Coupon (e.g., a purchase must be $100 or more to work).

  - `restrictions.minimum_amount_currency` (string, nullable)
    Three-letter [ISO code](https://stripe.com/docs/currencies) for minimum_amount

- `times_redeemed` (integer)
  Number of times this promotion code has been used.

### The Promotion Code object

```json
{
  "id": "promo_1MiM6KLkdIwHu7ixrIaX4wgn",
  "object": "promotion_code",
  "active": true,
  "code": "A1H1Q1MG",
  "promotion": {
    "type": "coupon",
    "coupon": "nVJYDOag"
  },
  "created": 1678040164,
  "customer": null,
  "expires_at": null,
  "livemode": false,
  "max_redemptions": null,
  "metadata": {},
  "restrictions": {
    "first_time_transaction": false,
    "minimum_amount": null,
    "minimum_amount_currency": null
  },
  "times_redeemed": 0
}
```