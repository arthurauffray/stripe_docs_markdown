# The ReservePlan object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `created_by` (enum)
  Indicates which party created this ReservePlan.
Possible enum values:
  - `application`
    The object was created by an application.

  - `stripe`
    The object was created by Stripe.

- `currency` (enum, nullable)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). An unset currency indicates that the plan applies to all currencies.

- `disabled_at` (timestamp, nullable)
  Time at which the ReservePlan was disabled.

- `fixed_release` (object, nullable)
  When to release all funds for a fixed release plan.

  - `fixed_release.release_after` (integer)
    The time after which all reserved funds are requested for release.

  - `fixed_release.scheduled_release` (timestamp)
    The time at which reserved funds are scheduled for release, automatically set to midnight UTC of the day after `release_after`.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (object, nullable)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `percent` (integer)
  The percent of each Charge to reserve.

- `rolling_release` (object, nullable)
  How long to hold reserves for a rolling release plan.

  - `rolling_release.days_after_charge` (integer)
    The number of days to reserve funds before releasing.

  - `rolling_release.expires_on` (integer, nullable)
    The time at which the ReservePlan expires.

- `status` (enum)
  The current status of the ReservePlan. The ReservePlan only affects charges if it is `active`.
Possible enum values:
  - `active`
    The ReservePlan is active and reserving funds.

  - `disabled`
    The ReservePlan has been manually disabled and is no longer reserving funds, and its associated funds have been released.

  - `expired`
    The ReservePlan has expired automatically and is no longer reserving funds, and its associated funds have been released.

- `type` (enum)
  The type of the ReservePlan.
Possible enum values:
  - `fixed_release`
    The ReservePlan releases funds after a fixed duration.

  - `rolling_release`
    The ReservePlan releases funds on a rolling basis.

### The ReservePlan object

```json
{
  "id": "resplan_61SxrVOzQu6XIJSCx41Q8rCFhzAUW",
  "object": "reserve.plan",
  "created": 1753380438,
  "created_by": "application",
  "currency": "usd",
  "disabled_at": null,
  "livemode": false,
  "metadata": {},
  "percent": 15,
  "rolling_release": {
    "days_after_charge": 30,
    "expires_on": 1755972438
  },
  "status": "active",
  "type": "rolling_release"
}
```