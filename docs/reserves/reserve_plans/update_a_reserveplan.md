# Update a ReservePlan

Update a ReservePlan’s configuration, percentage, or metadata.

## Returns

Returns the updated ReservePlan object.

## Parameters

- `id` (string, required)
  The identifier of the ReservePlan to update.

- `fixed_release` (object, optional)
  When to release all funds for a fixed release ReservePlan.

  - `fixed_release.release_after` (timestamp, required)
    The time after which reserved funds are released. This must be at least 3 days and at most 180 days in the future. This updates existing and future ReserveHolds for this ReservePlan.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `percent` (integer, optional)
  The percentage of each Charge to reserve.

- `rolling_release` (object, optional)
  How long to hold reserves for a rolling release ReservePlan.

  - `rolling_release.days_after_charge` (integer, optional)
    The number of days to reserve funds. This must be at least 3 days and at most 180 days. This only updates future ReserveHolds for this ReservePlan, existing ReserveHolds are not updated.

  - `rolling_release.expires_on` (timestamp, optional)
    Time at which this rolling release ReservePlan expires. If not set, the ReservePlan continues indefinitely.

```curl
curl https://api.stripe.com/v1/reserve/plans/resplan_61SxxwCbZ70gJfcoy41Q8rCFhzAUW \
  -u "<<YOUR_SECRET_KEY>>" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d percent=20 \
  -d "rolling_release[days_after_charge]"=40 \
  -d "rolling_release[expires_on]"=1755997558 \
  -d "metadata[test_key]"=test_value
```

### Response

```json
{
  "id": "resplan_61SxxwCbZ70gJfcoy41Q8rCFhzAUW",
  "object": "reserve.plan",
  "created": 1753405164,
  "created_by": "application",
  "currency": "usd",
  "disabled_at": null,
  "livemode": false,
  "metadata": {
    "test_key": "test_value"
  },
  "percent": 20,
  "rolling_release": {
    "days_after_charge": 40,
    "expires_on": 1755997675
  },
  "status": "active",
  "type": "rolling_release"
}
```