# Preview a Terminal Hardware Order

Get a preview of a TerminalHardwareOrder without creating it.

## Returns

Returns a `TerminalHardwareOrder` object (that has not been created) if the preview succeeds.

## Parameters

- `hardware_order_items` (array of objects, required)
  An array of line items to order.

  - `hardware_order_items.quantity` (integer, required)
    The quantity of the `TerminalHardwareSKU` to order.

  - `hardware_order_items.terminal_hardware_sku` (string, required)
    The ID of a `TerminalHardwareSKU`.

- `payment_type` (enum, required)
  The method of payment for this order.
Possible enum values:

- `shipping` (object, required)
  Shipping address for the order.

  - `shipping.address` (object, required)
    Shipping address.

    - `shipping.address.country` (string, required)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `shipping.address.line1` (string, required)
      Address line 1 (e.g., street, or company name). At least 3 and no more than 40 characters.

    - `shipping.address.postal_code` (string, required)
      ZIP or postal code. No more than 10 characters.

    - `shipping.address.city` (string, optional)
      City, district, suburb, town, or village. No more than 35 characters.

    - `shipping.address.line2` (string, optional)
      Address line 2, such as the apartment, suite, unit, or building. No more than 40 characters.

    - `shipping.address.state` (string, optional)
      State, county, province, or region. For US states, use two-letter state abbreviation in uppercase. For other states, county, province or region, use the full name. No more than 29 characters.

  - `shipping.email` (string, required)
    Customer email. This email will receive Stripe-branded update emails when the status of the order changes.

    The maximum length is 800 characters.

  - `shipping.name` (string, required)
    Customer name. At least 3. First name must be no more than 15 characters and last name must be no more than 20 characters.

  - `shipping.phone` (string, required)
    Customer phone (including extension). No more than 14 characters.

  - `shipping.company` (string, optional)
    Company name. At least 3 and no more than 40 characters.

- `shipping_method` (string, required)
  The [Shipping Method](https://docs.stripe.com/docs/api/terminal/hardware_shipping_methods/object.md) for the order.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `po_number` (string, optional)
  The purchase order number will appear on the packing slip, shipping label, and monthly billing invoice. No more than 15 characters.

```curl
curl -G https://api.stripe.com/v1/terminal/hardware_orders/preview \
  -u "<<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2025-12-15.clover; terminal_hardware_orders_beta=v5" \
  -d "shipping[name]"="Jenny Rosen" \
  -d "shipping[address][line1]"="1234 Main Street" \
  -d "shipping[address][city]"="San Francisco" \
  -d "shipping[address][state]"=CA \
  -d "shipping[address][country]"=US \
  -d "shipping[address][postal_code]"=94111 \
  -d "shipping[company]"="Rocket Rides" \
  -d "shipping[phone]"=15555555555 \
  --data-urlencode "shipping[email]"="test@example.com" \
  -d shipping_method=thsm_MfuTjLaPEgXMa4 \
  -d payment_type=monthly_invoice \
  -d "hardware_order_items[0][terminal_hardware_sku]"=thsku_L5fys7HZ5o02Nc \
  -d "hardware_order_items[0][quantity]"=2
```

### Response

```json
{
  "object": "terminal.hardware_order",
  "amount": 13602,
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
  ]
}
```