# List all transactions

Returns a list of Issuing `Transaction` objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` transactions, starting after transaction `starting_after`. Each entry in the array is a separate Issuing `Transaction` object. If no more transactions are available, the resulting array will be empty.

## Parameters

- `card` (string, optional)
  Only return transactions that belong to the given card.

- `cardholder` (string, optional)
  Only return transactions that belong to the given cardholder.

- `created` (object, optional)
  Only return transactions that were created during the given date interval.

  - `created.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `created.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `created.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `created.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `type` (enum, optional)
  Only return transactions that have the given type. One of `capture` or `refund`.
Possible enum values:
  - `capture`
    Funds were captured by the acquirer. `amount` will be negative because funds are moving out of your balance. Not all captures will be linked to an authorization, as acquirers [can force capture in some cases](https://stripe.com/docs/issuing/purchases/transactions).

  - `refund`
    An acquirer initiated a refund. This transaction might not be linked to an original capture, for example credits are original transactions. `amount` will be positive for refunds and negative for refund reversals (very rare).

```curl
curl -G https://api.stripe.com/v1/issuing/transactions \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe issuing transactions list  \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

transactions = client.v1.issuing.transactions.list({limit: 3})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

transactions = client.v1.issuing.transactions.list({"limit": 3})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$transactions = $stripe->issuing->transactions->all(['limit' => 3]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TransactionListParams params = TransactionListParams.builder().setLimit(3L).build();

StripeCollection<Transaction> stripeCollection =
  client.v1().issuing().transactions().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const transactions = await stripe.issuing.transactions.list({
  limit: 3,
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.IssuingTransactionListParams{}
params.Limit = stripe.Int64(3)
result := sc.V1IssuingTransactions.List(context.TODO(), params)
```

```dotnet
var options = new Stripe.Issuing.TransactionListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Issuing.Transactions;
StripeList<Stripe.Issuing.Transaction> transactions = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/issuing/transactions",
  "has_more": false,
  "data": [
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
  ]
}
```