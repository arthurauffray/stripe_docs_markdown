# Retrieve CryptoOnrampQuotes

Retrieves CryptoOnrampQuotes.

Related guide: [Quotes API](https://docs.stripe.com/docs/crypto/quotes-api.md)

## Returns

Returns the CryptoOnrampQuotes object

## Parameters

- `destination_amount` (string, optional)
  A string representation of the amount of `destination_currency` to be purchased. If `destination_amount` is set, `source_amount` must be null. When specifying this field, you must also set a single value for `destination_currencies` and a single value for `destination_networks` (so we know what cryptocurrency to quote).

- `destination_currencies` (array of enums, optional)
  The list of cryptocurrencies you want to generate quotes for. If left null, we retrieve quotes for all `destination_currencies` that `destination_networks` supports.

  Currencies: `btc, eth, sol, matic, usdc`

- `destination_networks` (array of enums, optional)
  The list of cryptocurrency networks you want to generate quotes for. If left null, we retrieve quotes for `destination_currencies` in all networks.

  Networks: `bitcoin, ethereum, solana, polygon`

- `source_amount` (string, optional)
  A string representation of the fiat amount that you need to onramp. If `source_amount` is set, `destination_amount` must be null (they’re mutually exclusive because you can only set a fixed amount for one end of the trade).

- `source_currency` (enum, optional)
  The [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) Currency code. We only support `usd` currently.

```curl
curl https://api.stripe.com/v1/crypto/onramp/quotes \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

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