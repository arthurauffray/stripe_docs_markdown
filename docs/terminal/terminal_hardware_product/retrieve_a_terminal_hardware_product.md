# Retrieve a Terminal Hardware Product

Retrieves a `TerminalHardwareProduct` object.

## Returns

Returns a `TerminalHardwareProduct` object if a valid identifier was provided.

```curl
curl https://api.stripe.com/v1/terminal/hardware_products/thpr_MJfotcxYT5Hwsm \
  -u "<<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2025-12-15.clover; terminal_hardware_orders_beta=v5"
```

### Response

```json
{
  "id": "thpr_MJfotcxYT5Hwsm",
  "object": "terminal.hardware_product",
  "status": "available",
  "type": "bbpos_wisepos_e",
  "unavailable_after": null
}
```