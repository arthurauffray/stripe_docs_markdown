# Retrieve a transaction's line items

Retrieves the line items of a committed standalone transaction as a collection.

## Returns

A list of Line Item objects if the Tax Transaction is found. Otherwise returns a ‘not found’ error.

## Parameters

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

  The maximum length is 500 characters.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

  The maximum length is 500 characters.

```curl
curl https://api.stripe.com/v1/tax/transactions/tax_1NaTVd2eZvKYlo2CoOX2Nf7P/line_items \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe tax transactions list_line_items tax_1NaTVd2eZvKYlo2CoOX2Nf7P
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

transaction_line_items = client.v1.tax.transactions.line_items.list('tax_1NaTVd2eZvKYlo2CoOX2Nf7P')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

transaction_line_items = client.v1.tax.transactions.line_items.list(
  "tax_1NaTVd2eZvKYlo2CoOX2Nf7P",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$transactionLineItems = $stripe->tax->transactions->allLineItems(
  'tax_1NaTVd2eZvKYlo2CoOX2Nf7P',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TransactionLineItemListParams params =
  TransactionLineItemListParams.builder().build();

StripeCollection<TransactionLineItem> stripeCollection =
  client.v1().tax().transactions().lineItems().list(
    "tax_1NaTVd2eZvKYlo2CoOX2Nf7P",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const transactionLineItems = await stripe.tax.transactions.listLineItems(
  'tax_1NaTVd2eZvKYlo2CoOX2Nf7P'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TaxTransactionListLineItemsParams{
  Transaction: stripe.String("tax_1NaTVd2eZvKYlo2CoOX2Nf7P"),
}
result := sc.V1TaxTransactions.ListLineItems(context.TODO(), params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Tax.Transactions.LineItems;
StripeList<Stripe.Tax.TransactionLineItem> transactionLineItems = service.List(
    "tax_1NaTVd2eZvKYlo2CoOX2Nf7P");
```

### Response

```json
{
  "id": "tax_1NaTVd2eZvKYlo2CoOX2Nf7P",
  "object": "list",
  "url": "/v1/tax/transactions/tax_1NaTVd2eZvKYlo2CoOX2Nf7P/line_items",
  "has_more": false,
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
  ]
}
```