# The ReserveHold object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `amount` (integer)
  Amount reserved. A positive integer representing how much is reserved in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

- `amount_releasable` (integer, nullable)
  Amount in cents that can be released from this ReserveHold

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `created_by` (enum)
  Indicates which party created this ReserveHold.
Possible enum values:
  - `application`
    The object was created by an application.

  - `stripe`
    The object was created by Stripe.

- `currency` (enum)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `is_releasable` (boolean, nullable)
  Whether there are any funds available to release on this ReserveHold. Note that if the ReserveHold is in the process of being released, this could be false, even though the funds haven’t been fully released yet.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (object, nullable)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `reason` (enum)
  The reason for the ReserveHold.
Possible enum values:
  - `charge`
    The ReserveHold was automatically created on pay-in based on an active ReservePlan.

  - `standalone`
    The ReserveHold was created by an API call and is not associated with a charge.

- `release_schedule` (object)
  Information about the release schedule of the ReserveHold.

  - `release_schedule.release_after` (timestamp, nullable)
    The time after which the ReserveHold is requested to be released.

  - `release_schedule.scheduled_release` (timestamp, nullable)
    The time at which the ReserveHold is scheduled to be released, automatically set to midnight UTC of the day after `release_after`.

- `reserve_plan` (string, nullable)
  The ReservePlan which produced this ReserveHold (i.e., resplan_123)

- `source_charge` (string, nullable)
  The Charge which funded this ReserveHold (e.g., ch_123)

- `source_type` (enum)
  Which source balance type this ReserveHold reserves funds from. One of `bank_account`, `card`, or `fpx`.

### The ReserveHold object

```json
{
  "id": "reshold_61SxrUZH1aQJj97WT41Q8rCFhzAUW",
  "object": "reserve.hold",
  "amount": 1000,
  "amount_releasable": 1000,
  "created": 1753380387,
  "created_by": "application",
  "currency": "usd",
  "is_releasable": true,
  "livemode": false,
  "metadata": {},
  "reason": "standalone",
  "release_schedule": {
    "release_after": 1755972386,
    "scheduled_release": 1755993600
  },
  "reserve_plan": null,
  "source_charge": null,
  "source_type": "card"
}
```