# The Application Fee object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `account` (string)
  ID of the Stripe account this fee was taken from.

- `amount` (integer)
  Amount earned, in cents.

- `amount_refunded` (integer)
  Amount in cents refunded (can be less than the amount attribute on the fee if a partial refund was issued)

- `application` (string)
  ID of the Connect application that earned the fee.

- `balance_transaction` (string, nullable)
  Balance transaction that describes the impact of this collected application fee on your account balance (not including refunds).

- `charge` (string)
  ID of the charge that the application fee was taken from.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (enum)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `fee_source` (object, nullable)
  Polymorphic source of the application fee. Includes the ID of the object the application fee was created from.

  - `fee_source.charge` (string, nullable)
    Charge ID that created this application fee.

  - `fee_source.payout` (string, nullable)
    Payout ID that created this application fee.

  - `fee_source.type` (enum)
    Type of object that created the application fee.
Possible enum values:
    - `charge`
      `charge` objects are used to [accept payments](https://docs.stripe.com/docs/connect/charges.md).

    - `payout`
      `payout` objects are used to [pay funds to an external account](https://docs.stripe.com/docs/connect/payouts-connected-accounts.md).

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `originating_transaction` (string, nullable)
  ID of the corresponding charge on the platform account, if this fee was the result of a charge using the `destination` parameter.

- `refunded` (boolean)
  Whether the fee has been fully refunded. If the fee is only partially refunded, this attribute will still be false.

- `refunds` (object)
  A list of refunds that have been applied to the fee.

  - `refunds.object` (string)
    String representing the object’s type. Objects of the same type share the same value. Always has the value `list`.

  - `refunds.data` (array of objects)
    Details about each object.

    - `refunds.data.id` (string)
      Unique identifier for the object.

    - `refunds.data.object` (string)
      String representing the object’s type. Objects of the same type share the same value.

    - `refunds.data.amount` (integer)
      Amount, in cents.

    - `refunds.data.balance_transaction` (string, nullable)
      Balance transaction that describes the impact on your account balance.

    - `refunds.data.created` (timestamp)
      Time at which the object was created. Measured in seconds since the Unix epoch.

    - `refunds.data.currency` (enum)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

    - `refunds.data.fee` (string)
      ID of the application fee that was refunded.

    - `refunds.data.metadata` (object, nullable)
      Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

  - `refunds.has_more` (boolean)
    True if this list has another page of items after this one that can be fetched.

  - `refunds.url` (string)
    The URL where this list can be accessed.

### The Application Fee object

```json
{
  "id": "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
  "object": "application_fee",
  "account": "acct_164wxjKbnvuxQXGu",
  "amount": 105,
  "amount_refunded": 105,
  "application": "ca_32D88BD1qLklliziD7gYQvctJIhWBSQ7",
  "balance_transaction": "txn_1032HU2eZvKYlo2CEPtcnUvl",
  "charge": "ch_1B73DOKbnvuxQXGurbwPqzsu",
  "created": 1506609734,
  "currency": "gbp",
  "livemode": false,
  "originating_transaction": null,
  "refunded": true,
  "refunds": {
    "object": "list",
    "data": [
      {
        "id": "fr_1MBoU0KbnvuxQXGu2wCCz4Bb",
        "object": "fee_refund",
        "amount": 38,
        "balance_transaction": null,
        "created": 1670284441,
        "currency": "usd",
        "fee": "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
        "metadata": {}
      },
      {
        "id": "fr_D0s7fGBKB40Twy",
        "object": "fee_refund",
        "amount": 100,
        "balance_transaction": "txn_1CaqNg2eZvKYlo2C75cA3Euk",
        "created": 1528486576,
        "currency": "usd",
        "fee": "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
        "metadata": {}
      }
    ],
    "has_more": false,
    "url": "/v1/application_fees/fee_1B73DOKbnvuxQXGuhY8Aw0TN/refunds"
  },
  "fee_source": {
    "charge": "ch_1B73DOKbnvuxQXGurbwPqzsu",
    "type": "charge"
  }
}
```