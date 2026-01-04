# Update a ReserveHold

Update a ReserveHold’s release schedule or metadata.

## Returns

Returns the updated ReserveHold object.

## Parameters

- `id` (string, required)
  The identifier of the ReserveHold to update.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `release_schedule` (object, optional)
  Configure when to release the ReserveHold.

  - `release_schedule.release_after` (timestamp, required)
    The time after which the ReserveHold releases.

```curl
curl https://api.stripe.com/v1/reserve/holds/reshold_61SxrUZH1aQJj97WT41Q8rCFhzAUW \
  -u "<<YOUR_SECRET_KEY>>" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d "release_schedule[release_after]"=1758588150 \
  -d "metadata[test_key]"=test_value
```

### Response

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
  "metadata": {
    "test_key": "test_value"
  },
  "reason": "standalone",
  "release_schedule": {
    "release_after": 1758588150,
    "scheduled_release": 1758672000
  },
  "reserve_plan": null,
  "source_charge": null,
  "source_type": "card"
}
```