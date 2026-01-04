# Retrieve a Terminal Hardware Shipping Method

Retrieves a `TerminalHardwareShippingMethod` object.

## Returns

Returns a `TerminalHardwareShippingMethod` object if a valid identifier was provided.

```curl
curl https://api.stripe.com/v1/terminal/hardware_shipping_methods/thsm_MfuTjLaPEgXMa4 \
  -u "<<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2025-12-15.clover; terminal_hardware_orders_beta=v5"
```

### Response

```json
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
```