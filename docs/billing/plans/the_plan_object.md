# The Plan object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `active` (boolean)
  Whether the plan can be used for new purchases.

- `amount` (integer, nullable)
  The unit amount in cents to be charged, represented as a whole integer if possible. Only set if `billing_scheme=per_unit`.

- `amount_decimal` (decimal string, nullable)
  The unit amount in cents to be charged, represented as a decimal string with at most 12 decimal places. Only set if `billing_scheme=per_unit`.

- `billing_scheme` (enum)
  Describes how to compute the price per period. Either `per_unit` or `tiered`. `per_unit` indicates that the fixed amount (specified in `amount`) will be charged per unit in `quantity` (for plans with `usage_type=licensed`), or per unit of total usage (for plans with `usage_type=metered`). `tiered` indicates that the unit pricing will be computed using a tiering strategy as defined using the `tiers` and `tiers_mode` attributes.
Possible enum values:
  - `per_unit`
  - `tiered`

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (enum)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `interval` (enum)
  The frequency at which a subscription is billed. One of `day`, `week`, `month` or `year`.

- `interval_count` (integer)
  The number of intervals (specified in the `interval` attribute) between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (object, nullable)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `meter` (string, nullable)
  The meter tracking the usage of a metered price

- `nickname` (string, nullable)
  A brief description of the plan, hidden from customers.

- `product` (string, nullable)
  The product whose pricing this plan determines.

- `tiers` (array of objects, nullable)
  Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`.

  - `tiers.flat_amount` (integer, nullable)
    Price for the entire tier.

  - `tiers.flat_amount_decimal` (decimal string, nullable)
    Same as `flat_amount`, but contains a decimal value with at most 12 decimal places.

  - `tiers.unit_amount` (integer, nullable)
    Per unit price for units relevant to the tier.

  - `tiers.unit_amount_decimal` (decimal string, nullable)
    Same as `unit_amount`, but contains a decimal value with at most 12 decimal places.

  - `tiers.up_to` (integer, nullable)
    Up to and including to this quantity will be contained in the tier.

- `tiers_mode` (enum, nullable)
  Defines if the tiering price should be `graduated` or `volume` based. In `volume`-based tiering, the maximum quantity within a period determines the per unit price. In `graduated` tiering, pricing can change as the quantity grows.
Possible enum values:
  - `graduated`
  - `volume`

- `transform_usage` (object, nullable)
  Apply a transformation to the reported usage or set quantity before computing the amount billed. Cannot be combined with `tiers`.

  - `transform_usage.divide_by` (integer)
    Divide usage by this number.

  - `transform_usage.round` (enum)
    After division, either round the result `up` or `down`.

- `trial_period_days` (integer, nullable)
  Default number of trial days when subscribing a customer to this plan using [`trial_from_plan=true`](https://docs.stripe.com/docs/api.md#create_subscription-trial_from_plan).

- `usage_type` (enum)
  Configures how the quantity per period should be determined. Can be either `metered` or `licensed`. `licensed` automatically bills the `quantity` set when adding it to a subscription. `metered` aggregates the total usage based on usage records. Defaults to `licensed`.

### The Plan object

```json
{
  "id": "plan_NjpIbv3g3ZibnD",
  "object": "plan",
  "active": true,
  "amount": 1200,
  "amount_decimal": "1200",
  "billing_scheme": "per_unit",
  "created": 1681851647,
  "currency": "usd",
  "interval": "month",
  "interval_count": 1,
  "livemode": false,
  "metadata": {},
  "nickname": null,
  "product": "prod_NjpI7DbZx6AlWQ",
  "tiers_mode": null,
  "transform_usage": null,
  "trial_period_days": null,
  "usage_type": "licensed"
}
```