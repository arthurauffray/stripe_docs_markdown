# Create funding instructions

Create or retrieve funding instructions for an Issuing balance. If funding instructions don’t yet exist for the account, we’ll create new funding instructions. If we’ve already created funding instructions for the account, we’ll retrieve the same funding instructions. In other words, we’ll return the same funding instructions each time.

## Returns

Returns funding instructions for an Issuing balance

## Parameters

- `bank_transfer` (object, required)
  Additional parameters for `bank_transfer` funding types

  - `bank_transfer.type` (enum, required)
    The type of the `bank_transfer`
Possible enum values:
    - `eu_bank_transfer`
      A bank transfer to an EU bank account

    - `gb_bank_transfer`
      A bank transfer to a GB bank account

- `currency` (enum, required)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `funding_type` (enum, required)
  The `funding_type` to get the instructions for.
Possible enum values:
  - `bank_transfer`
    Use a bank_transfer hash to define the bank transfer type

```curl
curl https://api.stripe.com/v1/issuing/funding_instructions \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "bank_transfer[type]"=eu_bank_transfer \
  -d currency=eur \
  -d funding_type=bank_transfer
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