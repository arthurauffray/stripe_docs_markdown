# Update a ReserveRelease

Update a ReserveRelease’s metadata.

## Returns

Returns the updated ReserveRelease object.

## Parameters

- `id` (string, required)
  The identifier of the ReserveRelease to update.

- `metadata` (object, required)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/reserve/releases/resrel_61SxyHbQOe90T6sLB41Q8rCFhzAUW \
  -u "<<YOUR_SECRET_KEY>>" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d "metadata[test_key]"=test_value
```

### Response

```json
{
  "id": "resrel_61SxyHbQOe90T6sLB41Q8rCFhzAUW",
  "object": "reserve.release",
  "amount": 500,
  "created": 1753406491,
  "created_by": "application",
  "currency": "usd",
  "livemode": false,
  "metadata": {
    "test_key": "test_value"
  },
  "reason": "hold_released_early",
  "released_at": 1753406491,
  "reserve_hold": "reshold_61SxrUZH1aQJj97WT41Q8rCFhzAUW",
  "reserve_plan": null
}
```