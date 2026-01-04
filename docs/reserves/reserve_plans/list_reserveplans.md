# List ReservePlans

Returns a list of ReservePlans previously created. The ReservePlans are returned in sorted order, with the most recent ReservePlans appearing first.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` ReservePlans, starting after ReservePlan `starting_after` and ending before ReservePlan `ending_before`.       Each entry in the array is a separate ReservePlan object. If no more ReservePlans are available, the resulting array will be empty.

## Parameters

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl https://api.stripe.com/v1/reserve/plans \
  -u "<<YOUR_SECRET_KEY>>" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"
```

### Response

```json
{
  "object": "list",
  "data": [
    {
      "id": "resplan_61SxxwCbZ70gJfcoy41Q8rCFhzAUW",
      "object": "reserve.plan",
      "created": 1753405164,
      "created_by": "application",
      "currency": "usd",
      "disabled_at": null,
      "livemode": false,
      "metadata": {},
      "percent": 15,
      "rolling_release": {
        "days_after_charge": 30,
        "expires_on": 1755997163
      },
      "status": "active",
      "type": "rolling_release"
    },
    {
      "id": "resplan_61SxrVOzQu6XIJSCx41Q8rCFhzAUW",
      "object": "reserve.plan",
      "created": 1753380438,
      "created_by": "application",
      "currency": "usd",
      "disabled_at": 1753405108,
      "livemode": false,
      "metadata": {},
      "percent": 15,
      "rolling_release": {
        "days_after_charge": 30,
        "expires_on": 1755972438
      },
      "status": "disabled",
      "type": "rolling_release"
    }
  ],
  "has_more": false,
  "url": "/v1/reserve/plans"
}
```