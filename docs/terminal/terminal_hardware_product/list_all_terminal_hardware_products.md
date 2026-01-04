# List all Terminal Hardware Products

List all `TerminalHardwareProduct` objects.

## Returns

A dictionary with a `data` property that contains an array of terminal hardware products. Each entry in the array is a separate Product object.

## Parameters

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `status` (enum, optional)
  Only return products that have the given status. Defaults to available.
Possible enum values:
  - `available`
    Available for new orders.

  - `unavailable`
    Can no longer be used for order creation.

```curl
curl https://api.stripe.com/v1/terminal/hardware_products \
  -u "<<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2025-12-15.clover; terminal_hardware_orders_beta=v5"
```

### Response

```json
{
  "object": "list",
  "url": "/v1/terminal/hardware_products",
  "has_more": false,
  "data": [
    {
      "id": "thpr_MJfotcxYT5Hwsm",
      "object": "terminal.hardware_product",
      "status": "available",
      "type": "bbpos_wisepos_e",
      "unavailable_after": null
    }
  ]
}
```