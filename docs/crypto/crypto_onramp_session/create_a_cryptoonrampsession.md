# Create a CryptoOnrampSession

Creates a CryptoOnrampSession object.

After the CryptoOnrampSession is created, display the onramp session modal using the `client_secret`.

Related guide: [Set up an onramp integration](https://docs.stripe.com/docs/crypto/integrate-the-onramp.md)

## Returns

Returns the created CryptoOnrampSession object

## Parameters

- `customer_ip_address` (string, optional)
  The IP address of the customer the platform intends to onramp.

  If the user’s IP is in a region we can’t support, we return an `HTTP 400` with an appropriate error code.

  We support IPv4 and IPv6 addresses. Geographic supportability is checked again later in the onramp flow, which provides a way to hide the onramp option from ineligible users for a better user experience.

- `destination_amount` (string, optional)
  The default amount of crypto to exchange into.

  - When left null, a default value is computed if `source_amount`, `destination_currency`, and `destination_network` are set.
  - When set, both `destination_currency` and `destination_network` must also be set. All cryptocurrencies are supported to their full precisions (for example, 18 decimal places for `eth`). We validate and generate an error if the amount exceeds the supported precision based on the exchange currency. Setting `source_amount` is mutually exclusive with setting `destination_amount` (only one or the other is supported). Users can update the amount in the onramp UI.

- `destination_currencies` (array of enums, optional)
  The list of destination cryptocurrencies a user can choose from.

  - When left null, all supported cryptocurrencies are shown in the onramp UI subject to `destination_networks` if set.
  - When set, it must be a non-empty array where all values in the array are valid cryptocurrencies. You can use it to lock users to a specific cryptocurrency by passing a single value array. Users **cannot** override this parameter.

- `destination_currency` (enum, optional)
  The default destination cryptocurrency.

  - When left null, the first value of `destination_currencies` is selected.
  - When set, if `destination_currencies` is also set, the value of `destination_currency` must be present in that array. To lock a `destination_currency`, specify that value as the single value for `destination_currencies`. Users can select a different cryptocurrency in the onramp UI subject to `destination_currencies` if set.

- `destination_network` (enum, optional)
  The default destination crypto network.

  - When left null, the first value of `destination_networks` is selected.
  - When set, if `destination_networks` is also set, the value of `destination_network` must be present in that array. To lock a `destination_network`, specify that value as the single value for `destination_networks`. Users can select a different network in the onramp UI subject to `destination_networks` if set.

- `destination_networks` (array of enums, optional)
  The list of destination crypto networks user can choose from.

  - When left null, all supported crypto networks are shown in the onramp UI.
  - When set, it must be a non-empty array where values in the array are each a valid crypto network. It can be used to lock users to a specific network by passing a single value array. Users **cannot** override this parameter.

- `kyc_details` (object, optional)
  Pre-populate some of the required KYC information for the user if you’ve already collected it within your application.

  Related guide: [Using the API](https://docs.stripe.com/docs/crypto/using-the-api.md#how-to-pre-populate-customer-information)

- `lock_wallet_address` (boolean, optional)
  Whether or not to lock the suggested wallet address. If destination tags are provided, this will also lock the destination tags.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `source_amount` (string, optional)
  The default amount of fiat (in decimal) to exchange into crypto.

  - When left null, a default value is computed if `destination_amount` is set.
  - When set, setting `source_amount` is mutually exclusive with setting `destination_amount` (only one or the other is supported). We don’t support fractional pennies. If fractional minor units of a currency are passed in, it generates an error. Users can update the value in the onramp UI.

- `source_currency` (enum, optional)
  The default source fiat currency for the onramp session.

  - When left null, a default currency is selected based on user locale.
  - When set, it must be one of the fiat currencies supported by onramp. Users can still select a different currency in the onramp UI.

- `wallet_addresses` (object, optional)
  The end customer’s crypto wallet address (for each network) to use for this transaction.

  - When left null, the user enters their wallet in the onramp UI.
  - When set, the platform must set either `destination_networks` or `destination_network` and we perform address validation. Users can still select a different wallet in the onramp UI.

  - `wallet_addresses.destination_tags` (object, optional)
    The end customer’s crypto wallet destination tag (for each network) to use for this transaction. This only applies for tag-based assets such as XLM.

    - When left null, the user enters their wallet in the onramp UI.

```curl
curl -X POST https://api.stripe.com/v1/crypto/onramp_sessions \
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