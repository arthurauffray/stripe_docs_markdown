# Retrieve a transaction

Retrieves an Issuing `Transaction` object.

## Returns

Returns an Issuing `Transaction` object if a valid identifier was provided.

```curl
curl https://api.stripe.com/v1/issuing/transactions/ipi_1MzFN1K8F4fqH0lBmFq8CjbU \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe issuing transactions retrieve ipi_1MzFN1K8F4fqH0lBmFq8CjbU
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

transaction = client.v1.issuing.transactions.retrieve('ipi_1MzFN1K8F4fqH0lBmFq8CjbU')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

transaction = client.v1.issuing.transactions.retrieve("ipi_1MzFN1K8F4fqH0lBmFq8CjbU")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$transaction = $stripe->issuing->transactions->retrieve(
  'ipi_1MzFN1K8F4fqH0lBmFq8CjbU',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TransactionRetrieveParams params = TransactionRetrieveParams.builder().build();

Transaction transaction =
  client.v1().issuing().transactions().retrieve(
    "ipi_1MzFN1K8F4fqH0lBmFq8CjbU",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const transaction = await stripe.issuing.transactions.retrieve(
  'ipi_1MzFN1K8F4fqH0lBmFq8CjbU'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.IssuingTransactionRetrieveParams{}
result, err := sc.V1IssuingTransactions.Retrieve(
  context.TODO(), "ipi_1MzFN1K8F4fqH0lBmFq8CjbU", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Issuing.Transactions;
Stripe.Issuing.Transaction transaction = service.Get("ipi_1MzFN1K8F4fqH0lBmFq8CjbU");
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
  "metadata": {},
  "type": "capture",
  "wallet": null
}
```