# The Transfer Reversal object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `amount` (integer)
  Amount, in cents.

- `balance_transaction` (string, nullable)
  Balance transaction that describes the impact on your account balance.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (enum)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `destination_payment_refund` (string, nullable)
  Linked payment refund for the transfer reversal.

- `metadata` (object, nullable)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `source_refund` (string, nullable)
  ID of the refund responsible for the transfer reversal.

- `transfer` (string)
  ID of the transfer that was reversed.

### The Transfer Reversal object

```json
{
  "id": "trr_1Mio2eLkdIwHu7ixN5LPJS4a",
  "object": "transfer_reversal",
  "amount": 400,
  "balance_transaction": "txn_1Mio2eLkdIwHu7ixosfrbjhW",
  "created": 1678147568,
  "currency": "usd",
  "destination_payment_refund": "pyr_1Mio2eQ9PRzxEwkZYewpaIFB",
  "metadata": {},
  "source_refund": null,
  "transfer": "tr_1Mio2dLkdIwHu7ixsUuCxJpu"
}
```