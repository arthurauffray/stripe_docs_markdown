# The ReserveRelease object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `amount` (integer)
  Amount released. A positive integer representing how much is released in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `created_by` (enum)
  Indicates which party created this ReserveRelease.
Possible enum values:
  - `application`
    The object was created by an application.

  - `stripe`
    The object was created by Stripe.

- `currency` (enum)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (object, nullable)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `reason` (enum)
  The reason for the ReserveRelease, indicating why the funds were released.
Possible enum values:
  - `bulk_hold_expiry`
    The ReserveHold expired automatically according to its schedule.

  - `hold_released_early`
    The ReserveHold was manually released before its scheduled release.

  - `hold_reversed`
    The ReserveHold was reversed due to a refund or dispute.

  - `plan_disabled`
    The ReserveHold was released due to its associated plan being disabled.

- `released_at` (timestamp)
  The release timestamp of the funds.

- `reserve_hold` (string, nullable)
  The ReserveHold this ReserveRelease is associated with.

- `reserve_plan` (string, nullable)
  The ReservePlan ID this ReserveRelease is associated with. This field is only populated if a ReserveRelease is created by a ReservePlan disable operation, or from a scheduled ReservedHold expiry.

- `source_transaction` (object, nullable)
  The transaction which triggered this ReserveRelease.

  - `source_transaction.dispute` (string, nullable)
    The ID of the dispute.

  - `source_transaction.refund` (string, nullable)
    The ID of the refund.

  - `source_transaction.type` (enum)
    The type of source transaction.
Possible enum values:
    - `dispute`
      The source transaction is a dispute.

    - `refund`
      The source transaction is a refund.

### The ReserveRelease object

```json
{
  "id": "resrel_61SxyHbQOe90T6sLB41Q8rCFhzAUW",
  "object": "reserve.release",
  "amount": 500,
  "created": 1753406491,
  "created_by": "application",
  "currency": "usd",
  "livemode": false,
  "metadata": {},
  "reason": "hold_released_early",
  "released_at": 1753406491,
  "reserve_hold": "reshold_61SxrUZH1aQJj97WT41Q8rCFhzAUW",
  "reserve_plan": null
}
```