# Create a reversal transaction

Partially or fully reverses a previously created `Transaction`.

## Returns

A new Tax `Transaction` object representing the reversal.

## Parameters

- `mode` (enum, required)
  If `partial`, the provided line item or shipping cost amounts are reversed. If `full`, the original transaction is fully reversed.
Possible enum values:
  - `full`
    The original transaction is fully reversed.

  - `partial`
    The provided line item amounts are reversed.

- `original_transaction` (string, required)
  The ID of the Transaction to partially or fully reverse.

- `reference` (string, required)
  A custom identifier for this reversal, such as `myOrder_123-refund_1`, which must be unique across all transactions. The reference helps identify this reversal transaction in exported [tax reports](https://docs.stripe.com/docs/tax/reports.md).

  The maximum length is 500 characters.

- `flat_amount` (integer, required if mode=partial and line_items nor shipping_cost provided)
  A flat amount to reverse across the entire transaction, in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal) in negative. This value represents the total amount to refund from the transaction, including taxes.

- `line_items` (array of objects, required if mode=partial and neither shipping_cost nor flat_amount is provided)
  The line item amounts to reverse.

  - `line_items.amount` (integer, required)
    The amount to reverse, in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal) in negative.

  - `line_items.amount_tax` (integer, required)
    The amount of tax to reverse, in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal) in negative.

  - `line_items.original_line_item` (string, required)
    The `id` of the line item to reverse in the original transaction.

  - `line_items.reference` (string, required)
    A custom identifier for this line item in the reversal transaction, such as ‘L1-refund’.

    The maximum length is 500 characters.

  - `line_items.metadata` (object, optional)
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

  - `line_items.quantity` (integer, optional)
    The quantity reversed. Appears in [tax exports](https://docs.stripe.com/docs/tax/reports.md), but does not affect the amount of tax reversed.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `shipping_cost` (object, required if mode=partial and neither line_items nor flat_amount is provided)
  The shipping cost to reverse.

  - `shipping_cost.amount` (integer, required)
    The amount to reverse, in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal) in negative.

  - `shipping_cost.amount_tax` (integer, required)
    The amount of tax to reverse, in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal) in negative.

```curl
curl https://api.stripe.com/v1/tax/transactions/create_reversal \
  -u "<<YOUR_SECRET_KEY>>" \
  -d mode=partial \
  -d original_transaction=tax_1NaTVd2eZvKYlo2CoOX2Nf7P \
  -d reference=myOrder_123-refund_1 \
  -d "line_items[0][amount]"=-1499 \
  -d "line_items[0][amount_tax]"=-148 \
  -d "line_items[0][original_line_item]"=tax_li_ONDxh8JZw14sP8 \
  -d "line_items[0][reference]"="refund of Pepperoni Pizza" \
  -d "expand[0]"=line_items
```

```cli
stripe tax transactions create_reversal  \
  --mode=partial \
  --original-transaction=tax_1NaTVd2eZvKYlo2CoOX2Nf7P \
  --reference=myOrder_123-refund_1 \
  -d "line_items[0][amount]"=-1499 \
  -d "line_items[0][amount_tax]"=-148 \
  -d "line_items[0][original_line_item]"=tax_li_ONDxh8JZw14sP8 \
  -d "line_items[0][reference]"="refund of Pepperoni Pizza" \
  -d "expand[0]"=line_items
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

transaction = client.v1.tax.transactions.create_reversal({
  mode: 'partial',
  original_transaction: 'tax_1NaTVd2eZvKYlo2CoOX2Nf7P',
  reference: 'myOrder_123-refund_1',
  line_items: [
    {
      amount: -1499,
      amount_tax: -148,
      original_line_item: 'tax_li_ONDxh8JZw14sP8',
      reference: 'refund of Pepperoni Pizza',
    },
  ],
  expand: ['line_items'],
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

transaction = client.v1.tax.transactions.create_reversal({
  "mode": "partial",
  "original_transaction": "tax_1NaTVd2eZvKYlo2CoOX2Nf7P",
  "reference": "myOrder_123-refund_1",
  "line_items": [
    {
      "amount": -1499,
      "amount_tax": -148,
      "original_line_item": "tax_li_ONDxh8JZw14sP8",
      "reference": "refund of Pepperoni Pizza",
    },
  ],
  "expand": ["line_items"],
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$transaction = $stripe->tax->transactions->createReversal([
  'mode' => 'partial',
  'original_transaction' => 'tax_1NaTVd2eZvKYlo2CoOX2Nf7P',
  'reference' => 'myOrder_123-refund_1',
  'line_items' => [
    [
      'amount' => -1499,
      'amount_tax' => -148,
      'original_line_item' => 'tax_li_ONDxh8JZw14sP8',
      'reference' => 'refund of Pepperoni Pizza',
    ],
  ],
  'expand' => ['line_items'],
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TransactionCreateReversalParams params =
  TransactionCreateReversalParams.builder()
    .setMode(TransactionCreateReversalParams.Mode.PARTIAL)
    .setOriginalTransaction("tax_1NaTVd2eZvKYlo2CoOX2Nf7P")
    .setReference("myOrder_123-refund_1")
    .addLineItem(
      TransactionCreateReversalParams.LineItem.builder()
        .setAmount(-1499L)
        .setAmountTax(-148L)
        .setOriginalLineItem("tax_li_ONDxh8JZw14sP8")
        .setReference("refund of Pepperoni Pizza")
        .build()
    )
    .addExpand("line_items")
    .build();

Transaction transaction = client.v1().tax().transactions().createReversal(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const transaction = await stripe.tax.transactions.createReversal({
  mode: 'partial',
  original_transaction: 'tax_1NaTVd2eZvKYlo2CoOX2Nf7P',
  reference: 'myOrder_123-refund_1',
  line_items: [
    {
      amount: -1499,
      amount_tax: -148,
      original_line_item: 'tax_li_ONDxh8JZw14sP8',
      reference: 'refund of Pepperoni Pizza',
    },
  ],
  expand: ['line_items'],
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TaxTransactionCreateReversalParams{
  Mode: stripe.String("partial"),
  OriginalTransaction: stripe.String("tax_1NaTVd2eZvKYlo2CoOX2Nf7P"),
  Reference: stripe.String("myOrder_123-refund_1"),
  LineItems: []*stripe.TaxTransactionCreateReversalLineItemParams{
    &stripe.TaxTransactionCreateReversalLineItemParams{
      Amount: stripe.Int64(-1499),
      AmountTax: stripe.Int64(-148),
      OriginalLineItem: stripe.String("tax_li_ONDxh8JZw14sP8"),
      Reference: stripe.String("refund of Pepperoni Pizza"),
    },
  },
}
params.AddExpand("line_items")
result, err := sc.V1TaxTransactions.CreateReversal(context.TODO(), params)
```

```dotnet
var options = new Stripe.Tax.TransactionCreateReversalOptions
{
    Mode = "partial",
    OriginalTransaction = "tax_1NaTVd2eZvKYlo2CoOX2Nf7P",
    Reference = "myOrder_123-refund_1",
    LineItems = new List<Stripe.Tax.TransactionLineItemOptions>
    {
        new Stripe.Tax.TransactionLineItemOptions
        {
            Amount = -1499,
            AmountTax = -148,
            OriginalLineItem = "tax_li_ONDxh8JZw14sP8",
            Reference = "refund of Pepperoni Pizza",
        },
    },
    Expand = new List<string> { "line_items" },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Tax.Transactions;
Stripe.Tax.Transaction transaction = service.CreateReversal(options);
```

### Response

```json
{
  "id": "tax_1NaTVd2eZvKYlo2CoOX2Nf7P",
  "object": "tax.transaction",
  "created": 1690938353,
  "currency": "usd",
  "customer": null,
  "customer_details": {
    "address": {
      "city": null,
      "country": "US",
      "line1": "354 Oyster Point Blvd",
      "line2": "",
      "postal_code": "94080",
      "state": "CA"
    },
    "address_source": "shipping",
    "ip_address": null,
    "tax_ids": [],
    "taxability_override": "none"
  },
  "line_items": {
    "object": "list",
    "data": [
      {
        "id": "tax_li_ONDxh8JZw14sP8",
        "object": "tax.transaction_line_item",
        "amount": 1499,
        "amount_tax": 148,
        "livemode": false,
        "metadata": null,
        "product": null,
        "quantity": 1,
        "reference": "Pepperoni Pizza",
        "reversal": null,
        "tax_behavior": "exclusive",
        "tax_code": "txcd_40060003",
        "type": "transaction"
      }
    ],
    "has_more": false,
    "url": "/v1/tax/transactions/tax_1NaTVd2eZvKYlo2CoOX2Nf7P/line_items"
  },
  "livemode": false,
  "metadata": null,
  "posted_at": 1690932566,
  "reference": "myOrder_123",
  "reversal": null,
  "shipping_cost": {
    "amount": 300,
    "amount_tax": 0,
    "tax_behavior": "exclusive",
    "tax_code": "txcd_92010001"
  },
  "tax_date": 1690938353,
  "type": "transaction"
}
```