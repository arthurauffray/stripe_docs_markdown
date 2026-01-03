# The Crypto Onramp Session object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `client_secret` (string)
  A client secret that can be used to drive a single session using our embedded widget.

  Related guide: [Set up an onramp integration](https://docs.stripe.com/crypto/integrate-the-onramp.md)

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `kyc_details_provided` (boolean)
  Has the value `true` if any user kyc details were provided during the creation of the onramp session. Otherwise, has the value `false`.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (object, nullable)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `redirect_url` (string, nullable)
  Redirect your users to the URL for a prebuilt frontend integration of the crypto onramp on the standalone hosted onramp.

  Related guide: [Mint a session with a redirect url](https://docs.stripe.com/crypto/standalone-hosted-onramp.md#mint-a-session-with-a-redirect-url)

- `status` (string)
  The status of the Onramp Session. One of = `{initialized, rejected, requires_payment, fulfillment_processing, fulfillment_complete}`

- `transaction_details` (object)
  A hash representing monetary details of the transaction this session represents.

  - `transaction_details.destination_amount` (string, nullable)
    The amount of crypto the customer will get deposited into their wallet

  - `transaction_details.destination_currencies` (array of enums, nullable)
    If a platform wants to lock the currencies an session will support, they can add supported currencies to this array. If left null, the experience will allow selection of all supported destination currencies.

  - `transaction_details.destination_currency` (enum, nullable)
    The selected `destination_currency` to convert the `source` to. This should be a crypto currency code. If `supported_destination_currencies` is set, it must be a value in that array.

  - `transaction_details.destination_network` (enum, nullable)
    The specific crypto network the `destination_currency` is settled on. If `supported_destination_networks` is set, it must be a value in that array.

  - `transaction_details.destination_networks` (array of enums, nullable)
    If a platform wants to lock the supported networks, they can do so through this array. If left null, the experience will allow selection of all supported networks.

  - `transaction_details.fees` (object, nullable)
    Details about the fees associated with this transaction

    - `transaction_details.fees.network_fee_amount` (string, nullable)
      The cost associated with moving crypto from Stripe to the end consumer’s wallet. e.g: for ETH, this is called ‘gas fee’, for BTC this is a ‘miner’s fee’.

    - `transaction_details.fees.transaction_fee_amount` (string, nullable)
      Fee for processing the transaction.

  - `transaction_details.lock_wallet_address` (boolean, nullable)
    Whether or not to lock the suggested wallet address.

  - `transaction_details.source_amount` (string, nullable)
    The amount of fiat we intend to onramp - excluding fees

  - `transaction_details.source_currency` (enum, nullable)
    A fiat currency code

  - `transaction_details.transaction_id` (string, nullable)
    The transaction id of the transaction that was sent to the customer’s wallet. This will only be set if the sessions hits the `status=fulfillment_complete` and we’ve transferred the crypto successfully to the external wallet. e.g: https://etherscan.io/tx/0xc2573af6b3a18e6f7c0e1cccc187a483f61d72cbb421f7166970d3ab45731a95

  - `transaction_details.wallet_address` (string, nullable)
    The consumer’s wallet address (where crypto will be sent to)

  - `transaction_details.wallet_addresses` (object, nullable)
    The end customer’s crypto wallet address (for each network) to use for this transaction.

    - `transaction_details.wallet_addresses.base_network` (string, nullable)
      A base address

    - `transaction_details.wallet_addresses.bitcoin` (string, nullable)
      A bitcoin address

    - `transaction_details.wallet_addresses.destination_tags` (object, nullable)
      The end customer’s crypto wallet destination tag (for each network) to use for this transaction.

      - `transaction_details.wallet_addresses.destination_tags.stellar` (string, nullable)
        A stellar destination tag

    - `transaction_details.wallet_addresses.ethereum` (string, nullable)
      An ethereum address

    - `transaction_details.wallet_addresses.optimism` (string, nullable)
      An optimism address

    - `transaction_details.wallet_addresses.polygon` (string, nullable)
      A polygon address

    - `transaction_details.wallet_addresses.solana` (string, nullable)
      A solana address

    - `transaction_details.wallet_addresses.stellar` (string, nullable)
      A stellar address

    - `transaction_details.wallet_addresses.worldchain` (string, nullable)
      A worldchain address

### The Crypto Onramp Session object

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