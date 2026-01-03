# The Crypto Onramp Quote object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `destination_network_quotes` (object)
  A list of destination cryptocurrency networks we can generate quotes for current as of `created`. We currently support: `{ethereum, solana, polygon, bitcoin}`

  - `destination_network_quotes.avalanche` (array of objects, nullable)
    Quotes for Avalanche

    - `destination_network_quotes.avalanche.destination_amount` (string)
      The amount of `destination_currency` that will be settled to the user

    - `destination_network_quotes.avalanche.destination_currency` (enum)
      The currency of the destination amount

    - `destination_network_quotes.avalanche.destination_network` (enum)
      The specific crypto network the `destination_currency` is settled on. If `supported_destination_networks` is set, it must be a value in that array.

    - `destination_network_quotes.avalanche.fees` (object)
      The fees associated with the quote, if it were to be used

    - `destination_network_quotes.avalanche.source_total_amount` (string)
      The total amount of fiat that will be charged to the user, including fees

  - `destination_network_quotes.base_network` (array of objects, nullable)
    Quotes for Base

    - `destination_network_quotes.base_network.destination_amount` (string)
      The amount of `destination_currency` that will be settled to the user

    - `destination_network_quotes.base_network.destination_currency` (enum)
      The currency of the destination amount

    - `destination_network_quotes.base_network.destination_network` (enum)
      The specific crypto network the `destination_currency` is settled on. If `supported_destination_networks` is set, it must be a value in that array.

    - `destination_network_quotes.base_network.fees` (object)
      The fees associated with the quote, if it were to be used

    - `destination_network_quotes.base_network.source_total_amount` (string)
      The total amount of fiat that will be charged to the user, including fees

  - `destination_network_quotes.bitcoin` (array of objects, nullable)
    Quotes for Bitcoin

    - `destination_network_quotes.bitcoin.destination_amount` (string)
      The amount of `destination_currency` that will be settled to the user

    - `destination_network_quotes.bitcoin.destination_currency` (enum)
      The currency of the destination amount

    - `destination_network_quotes.bitcoin.destination_network` (enum)
      The specific crypto network the `destination_currency` is settled on. If `supported_destination_networks` is set, it must be a value in that array.

    - `destination_network_quotes.bitcoin.fees` (object)
      The fees associated with the quote, if it were to be used

    - `destination_network_quotes.bitcoin.source_total_amount` (string)
      The total amount of fiat that will be charged to the user, including fees

  - `destination_network_quotes.ethereum` (array of objects, nullable)
    Quotes for Ethereum

    - `destination_network_quotes.ethereum.destination_amount` (string)
      The amount of `destination_currency` that will be settled to the user

    - `destination_network_quotes.ethereum.destination_currency` (enum)
      The currency of the destination amount

    - `destination_network_quotes.ethereum.destination_network` (enum)
      The specific crypto network the `destination_currency` is settled on. If `supported_destination_networks` is set, it must be a value in that array.

    - `destination_network_quotes.ethereum.fees` (object)
      The fees associated with the quote, if it were to be used

    - `destination_network_quotes.ethereum.source_total_amount` (string)
      The total amount of fiat that will be charged to the user, including fees

  - `destination_network_quotes.optimism` (array of objects, nullable)
    Quotes for Optimism

    - `destination_network_quotes.optimism.destination_amount` (string)
      The amount of `destination_currency` that will be settled to the user

    - `destination_network_quotes.optimism.destination_currency` (enum)
      The currency of the destination amount

    - `destination_network_quotes.optimism.destination_network` (enum)
      The specific crypto network the `destination_currency` is settled on. If `supported_destination_networks` is set, it must be a value in that array.

    - `destination_network_quotes.optimism.fees` (object)
      The fees associated with the quote, if it were to be used

    - `destination_network_quotes.optimism.source_total_amount` (string)
      The total amount of fiat that will be charged to the user, including fees

  - `destination_network_quotes.polygon` (array of objects, nullable)
    Quotes for Polygon

    - `destination_network_quotes.polygon.destination_amount` (string)
      The amount of `destination_currency` that will be settled to the user

    - `destination_network_quotes.polygon.destination_currency` (enum)
      The currency of the destination amount

    - `destination_network_quotes.polygon.destination_network` (enum)
      The specific crypto network the `destination_currency` is settled on. If `supported_destination_networks` is set, it must be a value in that array.

    - `destination_network_quotes.polygon.fees` (object)
      The fees associated with the quote, if it were to be used

    - `destination_network_quotes.polygon.source_total_amount` (string)
      The total amount of fiat that will be charged to the user, including fees

  - `destination_network_quotes.solana` (array of objects, nullable)
    Quotes for Solana

    - `destination_network_quotes.solana.destination_amount` (string)
      The amount of `destination_currency` that will be settled to the user

    - `destination_network_quotes.solana.destination_currency` (enum)
      The currency of the destination amount

    - `destination_network_quotes.solana.destination_network` (enum)
      The specific crypto network the `destination_currency` is settled on. If `supported_destination_networks` is set, it must be a value in that array.

    - `destination_network_quotes.solana.fees` (object)
      The fees associated with the quote, if it were to be used

    - `destination_network_quotes.solana.source_total_amount` (string)
      The total amount of fiat that will be charged to the user, including fees

  - `destination_network_quotes.stellar` (array of objects, nullable)
    Quotes for Stellar

    - `destination_network_quotes.stellar.destination_amount` (string)
      The amount of `destination_currency` that will be settled to the user

    - `destination_network_quotes.stellar.destination_currency` (enum)
      The currency of the destination amount

    - `destination_network_quotes.stellar.destination_network` (enum)
      The specific crypto network the `destination_currency` is settled on. If `supported_destination_networks` is set, it must be a value in that array.

    - `destination_network_quotes.stellar.fees` (object)
      The fees associated with the quote, if it were to be used

    - `destination_network_quotes.stellar.source_total_amount` (string)
      The total amount of fiat that will be charged to the user, including fees

  - `destination_network_quotes.worldchain` (array of objects, nullable)
    Quotes for Worldchain

    - `destination_network_quotes.worldchain.destination_amount` (string)
      The amount of `destination_currency` that will be settled to the user

    - `destination_network_quotes.worldchain.destination_currency` (enum)
      The currency of the destination amount

    - `destination_network_quotes.worldchain.destination_network` (enum)
      The specific crypto network the `destination_currency` is settled on. If `supported_destination_networks` is set, it must be a value in that array.

    - `destination_network_quotes.worldchain.fees` (object)
      The fees associated with the quote, if it were to be used

    - `destination_network_quotes.worldchain.source_total_amount` (string)
      The total amount of fiat that will be charged to the user, including fees

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `rate_fetched_at` (float)
  The time at which this quote was created (when the prices in `quotes` are applicable)

- `source_amount` (string)
  The amount of fiat we intend to onramp

- `source_currency` (enum)
  A fiat currency code

### The Crypto Onramp Quote object

```json
{
  "id": "610a15d980d48eeaabc3e7375127cd10c8e7a6aad03ecf77d42dfd4c4f881faa",
  "object": "crypto.onramp.quotes",
  "destination_network_quotes": {
    "avalanche": [
      {
        "id": "dec31b3a2ef646c0bbf525774fa767097a334d51567cab715523b19e2d4a83f1",
        "destination_amount": "3.474296399973076273",
        "destination_currency": "avax",
        "destination_network": "avalanche",
        "fees": {
          "network_fee_monetary": "0.03",
          "transaction_fee_monetary": "4.04"
        },
        "source_total_amount": "104.07"
      },
      {
        "id": "3d56a9b2fdf3e5b9666461d5c28ea82ebb24287a8ece19869b02778dc70497e1",
        "destination_amount": "100.000000",
        "destination_currency": "usdc",
        "destination_network": "avalanche",
        "fees": {
          "network_fee_monetary": "0.06",
          "transaction_fee_monetary": "4.04"
        },
        "source_total_amount": "104.10"
      }
    ],
    "base_network": [
      {
        "id": "b2e849efda961116b180c9da75d7f852b9e46593f06a95e1ccd0893099579a9e",
        "destination_amount": "0.029133919178255537",
        "destination_currency": "eth",
        "destination_network": "base",
        "fees": {
          "network_fee_monetary": "0.07",
          "transaction_fee_monetary": "4.04"
        },
        "source_total_amount": "104.11"
      },
      {
        "id": "e8bc97d01c0fbf0d0b18cf5a25f7da6b2f98183fd223ebb866b691bc652109ac",
        "destination_amount": "100.000000",
        "destination_currency": "usdc",
        "destination_network": "base",
        "fees": {
          "network_fee_monetary": "0.17",
          "transaction_fee_monetary": "4.04"
        },
        "source_total_amount": "104.21"
      }
    ],
    "bitcoin": [
      {
        "id": "2a83796a355cfc311aec441170e2448b678828d336828c3ebb427e180e552091",
        "destination_amount": "0.00160673",
        "destination_currency": "btc",
        "destination_network": "bitcoin",
        "fees": {
          "network_fee_monetary": "11.89",
          "transaction_fee_monetary": "4.27"
        },
        "source_total_amount": "116.16"
      }
    ],
    "ethereum": [
      {
        "id": "52670639e0db4e969e472b1e7e1a219fb70d8674200a5ca30bfc941a73200c82",
        "destination_amount": "0.029111240079494021",
        "destination_currency": "eth",
        "destination_network": "ethereum",
        "fees": {
          "network_fee_monetary": "1.25",
          "transaction_fee_monetary": "4.06"
        },
        "source_total_amount": "105.31"
      },
      {
        "id": "1fdae4939338d2ac2fdd2a18909cd570bdb7f412109304fb6965b826741e6f0f",
        "destination_amount": "100.000000",
        "destination_currency": "usdc",
        "destination_network": "ethereum",
        "fees": {
          "network_fee_monetary": "3.76",
          "transaction_fee_monetary": "4.11"
        },
        "source_total_amount": "107.87"
      }
    ],
    "polygon": [
      {
        "id": "3a039af52bb8d7aaab7ce3c89f9445dc58b0a3ef5cf8a5c9ce3e20cc030e1a07",
        "destination_amount": "174.481810700000000000",
        "destination_currency": "matic",
        "destination_network": "polygon",
        "fees": {
          "network_fee_monetary": "0.01",
          "transaction_fee_monetary": "4.04"
        },
        "source_total_amount": "104.05"
      },
      {
        "id": "cce3462ecd4dc451e8ac16af79ada6997e969620547995bb2911e14e95903d6a",
        "destination_amount": "100.000000",
        "destination_currency": "usdc",
        "destination_network": "polygon",
        "fees": {
          "network_fee_monetary": "0.01",
          "transaction_fee_monetary": "4.04"
        },
        "source_total_amount": "104.05"
      }
    ],
    "solana": [
      {
        "id": "733e3fa8578e38020a78c6f45ea5f1da1210bc04b12e554841768ac4f5c505db",
        "destination_amount": "0.653551160",
        "destination_currency": "sol",
        "destination_network": "solana",
        "fees": {
          "network_fee_monetary": "0.01",
          "transaction_fee_monetary": "4.04"
        },
        "source_total_amount": "104.05"
      },
      {
        "id": "c270e59f3e9aaa52662d18699cdff4112568b0dad888d56f37d05dfdedbc76c5",
        "destination_amount": "100.000000",
        "destination_currency": "usdc",
        "destination_network": "solana",
        "fees": {
          "network_fee_monetary": "0.01",
          "transaction_fee_monetary": "4.04"
        },
        "source_total_amount": "104.05"
      }
    ],
    "stellar": [
      {
        "id": "a0c754b8d68155e13318643d71ea1b0d00eba8614f3778d3ddcfe6e8c5ec711e",
        "destination_amount": "1064.71823580",
        "destination_currency": "xlm",
        "destination_network": "stellar",
        "fees": {
          "network_fee_monetary": "0.18",
          "transaction_fee_monetary": "4.04"
        },
        "source_total_amount": "104.22"
      },
      {
        "id": "3e66d98654933b753971ba75f99f7e7fb47e03c5db1b0a4d02e8ec189842ab5b",
        "destination_amount": "100.000000",
        "destination_currency": "usdc",
        "destination_network": "stellar",
        "fees": {
          "network_fee_monetary": "0.18",
          "transaction_fee_monetary": "4.04"
        },
        "source_total_amount": "104.22"
      }
    ]
  },
  "livemode": false,
  "rate_fetched_at": 1719947634.6564176,
  "source_amount": "100.00",
  "source_currency": "usd"
}
```