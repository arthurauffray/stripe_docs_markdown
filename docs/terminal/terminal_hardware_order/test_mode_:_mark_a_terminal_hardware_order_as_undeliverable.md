# Test mode: Mark a Terminal Hardware Order as Undeliverable

Updates a test mode `TerminalHardwareOrder` object’s status as undeliverable.

## Returns

Returns a `TerminalHardwareOrder` object.

```curl
curl -X POST https://api.stripe.com/v1/test_helpers/terminal/hardware_orders/thor_1Nj6mu2eZvKYlo2CRG74vB9n/mark_undeliverable \
  -u "<<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2025-12-15.clover; terminal_hardware_orders_beta=v5"
```

### Response

```json
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
  "status": "undeliverable",
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
```