# List ReserveHolds

Returns a list of ReserveHolds previously created. The ReserveHolds are returned in sorted order, with the most recent ReserveHolds appearing first.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` ReserveHolds, starting after ReserveHold `starting_after` and ending before ReserveHold `ending_before`.       Each entry in the array is a separate ReserveHold object. If no more ReserveHolds are available, the resulting array will be empty.

## Parameters

- `currency` (enum, optional)
  Only return ReserveHolds associated with the currency specified by this currency code. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `is_releasable` (boolean, optional)
  Only return ReserveHolds that are releasable.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `reserve_plan` (string, optional)
  Only return ReserveHolds associated with the ReservePlan specified by this ReservePlan ID.

- `reserve_release` (string, optional)
  Only return ReserveHolds associated with the ReserveRelease specified by this ReserveRelease ID.

- `source_charge` (string, optional)
  Only return ReserveHolds associated with the Charge specified by this source charge ID.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl https://api.stripe.com/v1/reserve/holds \
  -u "<<YOUR_SECRET_KEY>>" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"
```

```cli
stripe reserve holds list  \
  --stripe-account {{CONNECTED_ACCOUNT_ID}}
```

### Response

```json
{
  "object": "list",
  "data": [
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
    },
    {
      "id": "reshold_61SxrVXoFxfur37Dn41Q8rCFhzAUW",
      "object": "reserve.hold",
      "amount": 500,
      "amount_releasable": 500,
      "created": 1753380371,
      "created_by": "application",
      "currency": "usd",
      "is_releasable": true,
      "livemode": false,
      "metadata": {},
      "reason": "charge",
      "release_schedule": {
        "release_after": null,
        "scheduled_release": 1755993600
      },
      "reserve_plan": "resplan_61SxrVOzQu6XIJSCx41Q8rCFhzAUW",
      "source_charge": "ch_1RoTYAQ8rCFhzAUW6hEROA88",
      "source_type": "card"
    }
  ],
  "has_more": false,
  "url": "/v1/reserve/holds"
}
```