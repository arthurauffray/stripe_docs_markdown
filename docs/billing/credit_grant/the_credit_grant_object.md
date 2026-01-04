# The Credit Grant object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `amount` (object)
  Amount of this credit grant.

  - `amount.monetary` (object, nullable)
    The monetary amount.

    - `amount.monetary.currency` (string)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

    - `amount.monetary.value` (integer)
      A positive integer representing the amount.

  - `amount.type` (enum)
    The type of this amount. We currently only support `monetary` billing credits.
Possible enum values:
    - `monetary`
      The amount is a monetary amount.

- `applicability_config` (object)
  Configuration specifying what this credit grant applies to. We currently only support `metered` prices that have a [Billing Meter](https://docs.stripe.com/api/billing/meter.md) attached to them.

  - `applicability_config.scope` (object)
    Specify the scope of this applicability config.

    - `applicability_config.scope.billable_items` (array of objects, nullable)
      The billable items that credit grants can apply to. We currently only support metered billable items. Cannot be used in combination with `price_type` or `prices`.

      - `applicability_config.scope.billable_items.id` (string, nullable)
        Unique identifier for the object.

    - `applicability_config.scope.price_type` (enum, nullable)
      The price type that credit grants can apply to. We currently only support the `metered` price type. This refers to prices that have a [Billing Meter](https://docs.stripe.com/api/billing/meter.md) attached to them. Cannot be used in combination with `prices`.
Possible enum values:
      - `metered`
        Credit grants being created can only apply to metered prices.

    - `applicability_config.scope.prices` (array of objects, nullable)
      The prices that credit grants can apply to. We currently only support `metered` prices. This refers to prices that have a [Billing Meter](https://docs.stripe.com/api/billing/meter.md) attached to them. Cannot be used in combination with `price_type`.

      - `applicability_config.scope.prices.id` (string, nullable)
        Unique identifier for the object.

- `category` (enum)
  The category of this credit grant. This is for tracking purposes and isn’t displayed to the customer.
Possible enum values:
  - `paid`
    The credit grant was purchased by the customer for some amount.

  - `promotional`
    The credit grant was given to the customer for free.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `customer` (string)
  ID of the customer receiving the billing credits.

- `customer_account` (string, nullable)
  ID of the account representing the customer receiving the billing credits

- `effective_at` (timestamp, nullable)
  The time when the billing credits become effective-when they’re eligible for use.

- `expires_at` (timestamp, nullable)
  The time when the billing credits expire. If not present, the billing credits don’t expire.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `name` (string, nullable)
  A descriptive name shown in dashboard.

- `priority` (integer, nullable)
  The priority for applying this credit grant. The highest priority is 0 and the lowest is 100.

- `test_clock` (string, nullable)
  ID of the test clock this credit grant belongs to.

- `updated` (timestamp)
  Time at which the object was last updated. Measured in seconds since the Unix epoch.

- `voided_at` (timestamp, nullable)
  The time when this credit grant was voided. If not present, the credit grant hasn’t been voided.

### The Credit Grant object

```json
{
  "id": "credgr_test_61R9a6NUWsRmOW3RM41L6nFOS1ekDGHo",
  "object": "billing.credit_grant",
  "amount": {
    "monetary": {
      "currency": "usd",
      "value": 1000
    },
    "type": "monetary"
  },
  "applicability_config": {
    "scope": {
      "price_type": "metered"
    }
  },
  "category": "paid",
  "created": 1726620803,
  "customer": "cus_QrvQguzkIK8zTj",
  "effective_at": 1729297860,
  "expires_at": null,
  "livemode": false,
  "metadata": {},
  "name": "Purchased Credits",
  "priority": 50,
  "test_clock": null,
  "updated": 1726620803,
  "voided_at": null
}
```