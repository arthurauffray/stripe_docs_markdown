# List all Terminal Hardware Shipping Methods

List all `TerminalHardwareShippingMethod` objects.

## Returns

A dictionary with a `data` property that contains an array of terminal hardware shipping methods. Each entry in the array is a separate ShippingMethod object.

## Parameters

- `country` (string, required)
  Only return Shipping Methods that have the given country. If provided, country must be a two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `name` (enum, optional)
  Only return Shipping Methods that have the given name.
Possible enum values:
  - `express`
    Express

  - `priority`
    Priority

  - `standard`
    Standard

- `provider` (enum, optional)
  The provider associated with this ShippingMethod.
Possible enum values:
  - `stripe`
    The Stripe provider

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `status` (enum, optional)
  Only return Shipping Methods that have the given status. Defaults to Available.
Possible enum values:
  - `available`
    Available for new orders.

  - `unavailable`
    Can no longer be used for order creation.

```curl
curl https://api.stripe.com/v1/terminal/hardware_shipping_methods \
  -u "<<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2025-12-15.clover; terminal_hardware_orders_beta=v5"
```

### Response

```json
{
  "object": "list",
  "url": "/v1/terminal/hardware_shipping_methods",
  "has_more": false,
  "data": [
    {
      "id": "thsm_MfuTjLaPEgXMa4",
      "object": "terminal.hardware_shipping_method",
      "country": "US",
      "estimated_delivery_window": {
        "maximum_date": "2023-10-03",
        "minimum_date": "2023-10-03"
      },
      "name": "standard",
      "status": "available",
      "unavailable_after": null
    }
  ]
}
```