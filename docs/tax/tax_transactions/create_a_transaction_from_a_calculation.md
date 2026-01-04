# Create a transaction from a calculation

Creates a Tax Transaction from a calculation, if that calculation hasn’t expired. Calculations expire after 90 days.

## Returns

A Tax `Transaction` object.

## Parameters

- `calculation` (string, required)
  Tax Calculation ID to be used as input when creating the transaction.

- `reference` (string, required)
  A custom order or sale identifier, such as ‘myOrder_123’. Must be unique across all transactions, including reversals.

  The maximum length is 500 characters.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `posted_at` (timestamp, optional)
  The Unix timestamp representing when the tax liability is assumed or reduced, which determines the liability posting period and handling in tax liability reports. The timestamp must fall within the `tax_date` and the current time, unless the `tax_date` is scheduled in advance. Defaults to the current time.

```curl
curl https://api.stripe.com/v1/tax/transactions/create_from_calculation \
  -u "<<YOUR_SECRET_KEY>>" \
  -d calculation=taxcalc_1NaTVT2eZvKYlo2CsqGeLeU2 \
  -d reference=myOrder_123 \
  -d "expand[]"=line_items
```

```cli
stripe tax transactions create_from_calculation  \
  --calculation=taxcalc_1NaTVT2eZvKYlo2CsqGeLeU2 \
  --reference=myOrder_123 \
  -d "expand[0]"=line_items
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

transaction = client.v1.tax.transactions.create_from_calculation({
  calculation: 'taxcalc_1NaTVT2eZvKYlo2CsqGeLeU2',
  reference: 'myOrder_123',
  expand: ['line_items'],
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

transaction = client.v1.tax.transactions.create_from_calculation({
  "calculation": "taxcalc_1NaTVT2eZvKYlo2CsqGeLeU2",
  "reference": "myOrder_123",
  "expand": ["line_items"],
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$transaction = $stripe->tax->transactions->createFromCalculation([
  'calculation' => 'taxcalc_1NaTVT2eZvKYlo2CsqGeLeU2',
  'reference' => 'myOrder_123',
  'expand' => ['line_items'],
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TransactionCreateFromCalculationParams params =
  TransactionCreateFromCalculationParams.builder()
    .setCalculation("taxcalc_1NaTVT2eZvKYlo2CsqGeLeU2")
    .setReference("myOrder_123")
    .addExpand("line_items")
    .build();

Transaction transaction =
  client.v1().tax().transactions().createFromCalculation(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const transaction = await stripe.tax.transactions.createFromCalculation({
  calculation: 'taxcalc_1NaTVT2eZvKYlo2CsqGeLeU2',
  reference: 'myOrder_123',
  expand: ['line_items'],
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TaxTransactionCreateFromCalculationParams{
  Calculation: stripe.String("taxcalc_1NaTVT2eZvKYlo2CsqGeLeU2"),
  Reference: stripe.String("myOrder_123"),
}
params.AddExpand("line_items")
result, err := sc.V1TaxTransactions.CreateFromCalculation(context.TODO(), params)
```

```dotnet
var options = new Stripe.Tax.TransactionCreateFromCalculationOptions
{
    Calculation = "taxcalc_1NaTVT2eZvKYlo2CsqGeLeU2",
    Reference = "myOrder_123",
    Expand = new List<string> { "line_items" },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Tax.Transactions;
Stripe.Tax.Transaction transaction = service.CreateFromCalculation(options);
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