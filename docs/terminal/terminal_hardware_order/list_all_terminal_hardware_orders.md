# List all Terminal Hardware Orders

List all `TerminalHardwareOrder` objects.

## Returns

A dictionary with a `data` property that contains an array of terminal hardware orders. Each entry in the array is a separate order object.

## Parameters

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `status` (enum, optional)
  Only return orders that have the given status.
Possible enum values:
  - `canceled`
    Order was canceled. Please create a new order to receive these items.

  - `delivered`
    Order has been delivered!

  - `pending`
    Order has been received and can still be canceled.

  - `ready_to_ship`
    Order has been confirmed and is pending shipment. It cannot be canceled.

  - `shipped`
    Order has been shipped, and can no longer be canceled.

  - `undeliverable`
    One or more of the order’s items could not be delivered.

```curl
curl -G https://api.stripe.com/v1/terminal/hardware_orders \
  -u "<<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2025-12-15.clover; terminal_hardware_orders_beta=v5" \
  -d limit=3
```

### Response

```json
{
  "object": "list",
  "url": "/v1/terminal/hardware_orders",
  "has_more": false,
  "data": [
    {
      "id": "thor_1Nj6mu2eZvKYlo2CRG74vB9n",
      "object": "terminal.hardware_order",
      "amount": 13602,
      "created": 1692995962,
      "currency": "usd",
      "hardware_order_items": [
        {
          "amount": 11800,
          "currency": "usd",
          "quantity": 2,
          "terminal_hardware_sku": {
            "id": "thsku_OEu70OWVaQ0DG3",
            "amount": 450,
            "country": "US",
            "currency": "usd",
            "product": "thpr_NGubNsbUoS1oik"
          }
        }
      ],
      "livemode": true,
      "metadata": {},
      "payment_type": "monthly_invoice",
      "po_number": null,
      "shipment_tracking": [],
      "shipping": {
        "address": {
          "city": "San Francisco",
          "country": "US",
          "line1": "1234 Main Street",
          "line2": "",
          "postal_code": "94111",
          "state": "CA"
        },
        "amount": 800,
        "company": "Rocket Rides",
        "currency": "usd",
        "email": "test@example.com",
        "name": "Jenny Rosen",
        "phone": "15555555555"
      },
      "shipping_method": "standard",
      "status": "pending",
      "tax": 1002,
      "total_tax_amounts": [
        {
          "amount": 1002,
          "inclusive": false,
          "rate": {
            "display_name": "Sales Tax",
            "jurisdiction": "LOS ANGELES",
            "percentage": 8.25
          }
        }
      ],
      "updated": null
    }
  ]
}
```