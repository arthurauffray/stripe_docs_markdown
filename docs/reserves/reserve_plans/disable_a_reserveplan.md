# Disable a ReservePlan

Disables a ReservePlan by transitioning it to a `disabled` state.

All associated ReserveHolds release asynchronously.

Note: This action is irreversible - a disabled ReservePlan cannot be re-enabled.

## Returns

Returns the updated ReservePlan object.

## Parameters

- `id` (string, required)
  The identifier of the ReservePlan to disable.

```curl
curl -X POST https://api.stripe.com/v1/reserve/plans/resplan_61SxrVOzQu6XIJSCx41Q8rCFhzAUW/disable \
  -u "<<YOUR_SECRET_KEY>>" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"
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
  "status": "disabling",
  "type": "rolling_release"
}
```