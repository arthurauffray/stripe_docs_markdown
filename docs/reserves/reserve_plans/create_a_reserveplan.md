# Create a ReservePlan

Create a ReservePlan for a given account of a given type.

## Returns

Returns a ReservePlan object.

## Parameters

- `percent` (integer, required)
  The percentage of each Charge to reserve.

- `type` (enum, required)
  The type of the ReservePlan.
Possible enum values:
  - `fixed_release`
    The ReservePlan releases funds after a fixed duration.

  - `rolling_release`
    The ReservePlan releases funds on a rolling basis.

- `currency` (enum, optional)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). Leave unset to create a ReservePlan for all currencies.

- `fixed_release` (object, optional)
  When to release all funds for a fixed release ReservePlan.

  - `fixed_release.release_after` (timestamp, required)
    The time after which reserved funds are released. This must be at least 3 days and at most 180 days in the future.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `rolling_release` (object, optional)
  How long to hold reserves for a rolling release ReservePlan.

  - `rolling_release.days_after_charge` (integer, required)
    The number of days to reserve funds. This must be at least 3 days and at most 180 days.

  - `rolling_release.expires_on` (timestamp, optional)
    Time at which this rolling release ReservePlan expires. If not set, the ReservePlan continues indefinitely.

```curl
curl https://api.stripe.com/v1/reserve/plans \
  -u "<<YOUR_SECRET_KEY>>" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d type=rolling_release \
  -d percent=15 \
  -d currency=usd \
  -d "rolling_release[days_after_charge]"=30 \
  -d "rolling_release[expires_on]"=1755972438
```

### Response

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