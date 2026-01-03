# Retrieve a CryptoOnrampSession

Retrieves the details of a CryptoOnrampSession that was previously created.

## Returns

Returns a CryptoOnrampSession object

```curl
curl https://api.stripe.com/v1/crypto/onramp_sessions/cos_1NamBL2eZvKYlo2CP38sZVEW \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "cos_1NamBL2eZvKYlo2CP38sZVEW",
  "object": "crypto.onramp_session",
  "client_secret": "cos_1NamBL2eZvKYlo2CP38sZVEW_secret_B5faamUkzHbcpjy6NndGq1mMZGGCo8FhK2P",
  "created": 1691010131,
  "kyc_details_provided": false,
  "livemode": true,
  "metadata": {},
  "redirect_url": null,
  "status": "initialized",
  "transaction_details": {
    "destination_amount": null,
    "destination_currencies": [
      "btc",
      "eth",
      "matic",
      "sol",
      "xlm",
      "avax",
      "usdc"
    ],
    "destination_currency": null,
    "destination_network": null,
    "destination_networks": [
      "bitcoin",
      "ethereum",
      "base",
      "polygon",
      "solana",
      "stellar",
      "avalanche"
    ],
    "fees": null,
    "lock_wallet_address": false,
    "source_amount": null,
    "source_currency": null,
    "transaction_id": null,
    "wallet_address": null,
    "wallet_addresses": null
  }
}
```