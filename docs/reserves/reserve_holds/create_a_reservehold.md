# Create a ReserveHold

Create a ReserveHold.

## Returns

Returns a ReserveHold object.

## Parameters

- `amount` (integer, required)
  Amount to reserve. A positive integer representing how much to reserve in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal) (e.g., 100 cents to reserve $1.00 or 100 to reserve ¥100, a zero-decimal currency).

- `currency` (enum, required)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `release_schedule` (object, required)
  Configure when to release the ReserveHold.

  - `release_schedule.release_after` (timestamp, required)
    The time after which the ReserveHold releases. This must be at least 3 days and at most 180 days in the future.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `source_type` (string, optional)
  Which source balance type this ReserveHold reserves funds from. One of `bank_account`, `card`, or `fpx`. If not provided, this defaults to `card`.

```curl
curl https://api.stripe.com/v1/reserve/holds \
  -u "<<YOUR_SECRET_KEY>>" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d amount=1000 \
  -d currency=usd \
  -d "release_schedule[release_after]"=1755972386
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