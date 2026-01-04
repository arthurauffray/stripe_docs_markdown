# List all Terminal Hardware SKUs

List all `TerminalHardwareSKU` objects.

## Returns

A dictionary with a `data` property that contains an array of terminal hardware SKUs. Each entry in the array is a separate SKU object.

## Parameters

- `country` (string, required)
  The ISO 3166-1 alpha-2 country code representing the country associated with the SKUs to be retrieved. Available country codes can be listed with the [List Country Specs](https://docs.stripe.com/docs/api.md#list_country_specs) endpoint.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `product` (string, optional)
  Only return SKUs for the product specified by this product ID.

- `provider` (enum, optional)
  The provider associated with this SKU.
Possible enum values:
  - `stripe`
    The Stripe provider

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `status` (enum, optional)
  Only return SKUs that have the given status. Defaults to available.
Possible enum values:
  - `available`
    Available for new orders.

  - `unavailable`
    Can no longer be used for order creation.

```curl
curl https://api.stripe.com/v1/terminal/hardware_skus \
  -u "<<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2025-12-15.clover; terminal_hardware_orders_beta=v5"
```

### Response

```json
{
  "object": "list",
  "url": "/v1/terminal/hardware_skus",
  "has_more": false,
  "data": [
    {
      "id": "thsku_OEu70OWVaQ0DG3",
      "object": "terminal.hardware_sku",
      "amount": 450,
      "country": "US",
      "currency": "usd",
      "orderable": 100,
      "product": "thpr_NGubNsbUoS1oik",
      "status": "available",
      "unavailable_after": null
    }
  ]
}
```