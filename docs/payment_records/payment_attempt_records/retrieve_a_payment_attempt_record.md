# Retrieve a Payment Attempt Record

Retrieves a Payment Attempt Record with the given ID

## Returns

Returns a Payment Attempt Record object if a valid ID was provided. Otherwise, this call raises an error.

## Parameters

- `id` (string, required)
  The ID of the Payment Attempt Record.

```curl
curl https://api.stripe.com/v1/payment_attempt_records/par_4sdDKj23235s \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "par_4sdDKj23235s",
  "object": "payment_attempt_record",
  "amount_canceled": {
    "currency": "usd",
    "value": 0
  },
  "amount_failed": {
    "currency": "usd",
    "value": 0
  },
  "amount_guaranteed": {
    "currency": "usd",
    "value": 0
  },
  "amount_refunded": {
    "currency": "usd",
    "value": 0
  },
  "amount_requested": {
    "currency": "usd",
    "value": 1000
  },
  "created": 1730211363,
  "customer_details": null,
  "customer_presence": "on_session",
  "description": "computer software",
  "livemode": true,
  "metadata": {},
  "payment_method_details": {
    "billing_details": null,
    "custom": {
      "display_name": "newpay",
      "type": "cpmt_125kjj3hn3sdf"
    },
    "payment_method": "pm_5j23kjksibjlks",
    "type": "custom"
  },
  "payment_record": "pr_5RV730PrHyAEi",
  "processor_details": {
    "type": "custom",
    "custom": {
      "payment_reference": "npp2358872734k"
    }
  },
  "shipping_details": null
}
```