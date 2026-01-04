# Update a transaction

Updates the specified Issuing `Transaction` object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

## Returns

Returns an updated Issuing `Transaction` object if a valid identifier was provided.

## Parameters

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/issuing/transactions/ipi_1MzFN1K8F4fqH0lBmFq8CjbU \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
```

```cli
stripe issuing transactions update ipi_1MzFN1K8F4fqH0lBmFq8CjbU \
  -d "metadata[order_id]"=6735
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

transaction = client.v1.issuing.transactions.update(
  'ipi_1MzFN1K8F4fqH0lBmFq8CjbU',
  {metadata: {order_id: '6735'}},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

transaction = client.v1.issuing.transactions.update(
  "ipi_1MzFN1K8F4fqH0lBmFq8CjbU",
  {"metadata": {"order_id": "6735"}},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$transaction = $stripe->issuing->transactions->update(
  'ipi_1MzFN1K8F4fqH0lBmFq8CjbU',
  ['metadata' => ['order_id' => '6735']]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TransactionUpdateParams params =
  TransactionUpdateParams.builder().putMetadata("order_id", "6735").build();

Transaction transaction =
  client.v1().issuing().transactions().update(
    "ipi_1MzFN1K8F4fqH0lBmFq8CjbU",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const transaction = await stripe.issuing.transactions.update(
  'ipi_1MzFN1K8F4fqH0lBmFq8CjbU',
  {
    metadata: {
      order_id: '6735',
    },
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.IssuingTransactionUpdateParams{}
params.AddMetadata("order_id", "6735")
result, err := sc.V1IssuingTransactions.Update(
  context.TODO(), "ipi_1MzFN1K8F4fqH0lBmFq8CjbU", params)
```

```dotnet
var options = new Stripe.Issuing.TransactionUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Issuing.Transactions;
Stripe.Issuing.Transaction transaction = service.Update(
    "ipi_1MzFN1K8F4fqH0lBmFq8CjbU",
    options);
```

### Response

```json
{
  "id": "ipi_1MzFN1K8F4fqH0lBmFq8CjbU",
  "object": "issuing.transaction",
  "amount": -100,
  "amount_details": {
    "atm_fee": null
  },
  "authorization": "iauth_1MzFMzK8F4fqH0lBc9VdaZUp",
  "balance_transaction": "txn_1MzFN1K8F4fqH0lBQPtqUmJN",
  "card": "ic_1MzFMxK8F4fqH0lBjIUITRYi",
  "cardholder": "ich_1MzFMxK8F4fqH0lBXnFW0ROG",
  "created": 1682065867,
  "currency": "usd",
  "dispute": null,
  "livemode": false,
  "merchant_amount": -100,
  "merchant_currency": "usd",
  "merchant_data": {
    "category": "computer_software_stores",
    "category_code": "5734",
    "city": "SAN FRANCISCO",
    "country": "US",
    "name": "WWWW.BROWSEBUG.BIZ",
    "network_id": "1234567890",
    "postal_code": "94103",
    "state": "CA"
  },
  "metadata": {
    "order_id": "6735"
  },
  "type": "capture",
  "wallet": null
}
```