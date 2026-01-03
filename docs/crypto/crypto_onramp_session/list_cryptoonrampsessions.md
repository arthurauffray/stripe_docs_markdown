# List CryptoOnrampSessions

Returns a list of onramp sessions that match the filter criteria. The onramp sessions are returned in sorted order, with the most recent onramp sessions appearing first.

## Returns

A dictionary with a data property that contains an array of up to `limit` onramp sessions, starting after onramp session `starting_after`. Each entry in the array is a separate onramp session object. If no more onramp sessions are available, the resulting array will be empty.

## Parameters

- `created` (object, optional)
  Only return onramp sessions that were created during the given date interval.

  - `created.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `created.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `created.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `created.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `destination_currency` (enum, optional)
  The destination cryptocurrency to filter by.

- `destination_network` (enum, optional)
  The destination blockchain network to filter by.

- `ending_before` (string, optional)
  An object ID cursor for use in pagination.

- `limit` (integer, optional)
  A limit ranging from 1 to 100 (defaults to 10).

- `starting_after` (string, optional)
  An object ID cursor for use in pagination.

- `status` (enum, optional)
  The status of the Onramp Session. One of = `{initialized, rejected, requires_payment, fulfillment_processing, fulfillment_complete}`

```curl
curl -G https://api.stripe.com/v1/crypto/onramp_sessions \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

### Response

```json
{
  "object": "list",
  "url": "/v1/crypto/onramp_sessions",
  "has_more": false,
  "data": [
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
  ]
}
```