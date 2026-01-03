# The Transfer object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `amount` (integer)
  Amount in cents to be transferred.

- `amount_reversed` (integer)
  Amount in cents reversed (can be less than the amount attribute on the transfer if a partial reversal was issued).

- `balance_transaction` (string, nullable)
  Balance transaction that describes the impact of this transfer on your account balance.

- `created` (timestamp)
  Time that this record of the transfer was first created.

- `currency` (enum)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `description` (string, nullable)
  An arbitrary string attached to the object. Often useful for displaying to users.

- `destination` (string, nullable)
  ID of the Stripe account the transfer was sent to.

- `destination_payment` (string, nullable)
  If the destination is a Stripe account, this will be the ID of the payment that the destination account received for the transfer.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `reversals` (object)
  A list of reversals that have been applied to the transfer.

  - `reversals.object` (string)
    String representing the object’s type. Objects of the same type share the same value. Always has the value `list`.

  - `reversals.data` (array of objects)
    Details about each object.

    - `reversals.data.id` (string)
      Unique identifier for the object.

    - `reversals.data.object` (string)
      String representing the object’s type. Objects of the same type share the same value.

    - `reversals.data.amount` (integer)
      Amount, in cents.

    - `reversals.data.balance_transaction` (string, nullable)
      Balance transaction that describes the impact on your account balance.

    - `reversals.data.created` (timestamp)
      Time at which the object was created. Measured in seconds since the Unix epoch.

    - `reversals.data.currency` (enum)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

    - `reversals.data.destination_payment_refund` (string, nullable)
      Linked payment refund for the transfer reversal.

    - `reversals.data.metadata` (object, nullable)
      Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

    - `reversals.data.source_refund` (string, nullable)
      ID of the refund responsible for the transfer reversal.

    - `reversals.data.transfer` (string)
      ID of the transfer that was reversed.

  - `reversals.has_more` (boolean)
    True if this list has another page of items after this one that can be fetched.

  - `reversals.url` (string)
    The URL where this list can be accessed.

- `reversed` (boolean)
  Whether the transfer has been fully reversed. If the transfer is only partially reversed, this attribute will still be false.

- `source_transaction` (string, nullable)
  ID of the charge that was used to fund the transfer. If null, the transfer was funded from the available balance.

- `source_type` (string, nullable)
  The source balance this transfer came from. One of `card`, `fpx`, or `bank_account`.

- `transfer_group` (string, nullable)
  A string that identifies this transaction as part of a group. See the [Connect documentation](https://docs.stripe.com/docs/connect/separate-charges-and-transfers.md#transfer-options) for details.

### The Transfer object

```json
{
  "id": "tr_1MiN3gLkdIwHu7ixNCZvFdgA",
  "object": "transfer",
  "amount": 400,
  "amount_reversed": 0,
  "balance_transaction": "txn_1MiN3gLkdIwHu7ixxapQrznl",
  "created": 1678043844,
  "currency": "usd",
  "description": null,
  "destination": "acct_1MTfjCQ9PRzxEwkZ",
  "destination_payment": "py_1MiN3gQ9PRzxEwkZWTPGNq9o",
  "livemode": false,
  "metadata": {},
  "reversals": {
    "object": "list",
    "data": [],
    "has_more": false,
    "total_count": 0,
    "url": "/v1/transfers/tr_1MiN3gLkdIwHu7ixNCZvFdgA/reversals"
  },
  "reversed": false,
  "source_transaction": null,
  "source_type": "card",
  "transfer_group": "ORDER_95"
}
```