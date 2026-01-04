# Simulate a top up

Simulates an external bank transfer and adds funds to an Issuing balance. This method can only be called in test mode.

## Returns

Returns testmode funding instructions for an Issuing balance

## Parameters

- `amount` (integer, required)
  The amount to top up

- `currency` (enum, required)
  The currency to top up

```curl
curl https://api.stripe.com/v1/test_helpers/issuing/fund_balance \
  -u "<<YOUR_SECRET_KEY>>" \
  -d amount=4242 \
  -d currency=eur
```

### Response

```json
{
  "object": "funding_instructions",
  "bank_transfer": {
    "country": "DE",
    "financial_addresses": [
      {
        "iban": {
          "account_holder_name": "Stripe Technology Europe Limited",
          "bic": "SXPYDEHH",
          "country": "DE",
          "iban": "DE00000000000000000001"
        },
        "supported_networks": [
          "sepa"
        ],
        "type": "iban"
      }
    ],
    "type": "eu_bank_transfer"
  },
  "currency": "eur",
  "funding_type": "bank_transfer",
  "livemode": false
}
```