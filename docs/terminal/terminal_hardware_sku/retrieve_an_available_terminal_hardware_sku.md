# Retrieve an available Terminal Hardware SKU

Retrieves an available `TerminalHardwareSKU` object.

## Returns

Returns an available `TerminalHardwareSKU` object if a valid identifier was provided.

```curl
curl https://api.stripe.com/v1/terminal/hardware_skus/thsku_OEu70OWVaQ0DG3 \
  -u "<<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2025-12-15.clover; terminal_hardware_orders_beta=v5"
```

### Response

```json
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
```