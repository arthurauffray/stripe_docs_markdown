# List credit balance transactions

Retrieve a list of credit balance transactions.

## Returns

Returns a list of credit balance transactions.

## Parameters

- `credit_grant` (string, optional)
  The credit grant for which to fetch credit balance transactions.

- `customer` (string, optional)
  The customer whose credit balance transactions you’re retrieving.

- `customer_account` (string, optional)
  The account representing the customer whose credit balance transactions you’re retrieving.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/billing/credit_balance_transactions \
  -u "<<YOUR_SECRET_KEY>>" \
  -d customer=cus_QrvQguzkIK8zTj \
  -d credit_grant=credgr_test_61R9ZkIkIzLSp0xze41L6nFOS1ekDTPE
```

```cli
stripe billing credit_balance_transactions list  \
  --customer=cus_QrvQguzkIK8zTj \
  --credit-grant=credgr_test_61R9ZkIkIzLSp0xze41L6nFOS1ekDTPE
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

credit_balance_transactions = client.v1.billing.credit_balance_transactions.list({
  customer: 'cus_QrvQguzkIK8zTj',
  credit_grant: 'credgr_test_61R9ZkIkIzLSp0xze41L6nFOS1ekDTPE',
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

credit_balance_transactions = client.v1.billing.credit_balance_transactions.list({
  "customer": "cus_QrvQguzkIK8zTj",
  "credit_grant": "credgr_test_61R9ZkIkIzLSp0xze41L6nFOS1ekDTPE",
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$creditBalanceTransactions = $stripe->billing->creditBalanceTransactions->all([
  'customer' => 'cus_QrvQguzkIK8zTj',
  'credit_grant' => 'credgr_test_61R9ZkIkIzLSp0xze41L6nFOS1ekDTPE',
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CreditBalanceTransactionListParams params =
  CreditBalanceTransactionListParams.builder()
    .setCustomer("cus_QrvQguzkIK8zTj")
    .setCreditGrant("credgr_test_61R9ZkIkIzLSp0xze41L6nFOS1ekDTPE")
    .build();

StripeCollection<CreditBalanceTransaction> stripeCollection =
  client.v1().billing().creditBalanceTransactions().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const creditBalanceTransactions = await stripe
  .billing
  .creditBalanceTransactions
  .list({
  customer: 'cus_QrvQguzkIK8zTj',
  credit_grant: 'credgr_test_61R9ZkIkIzLSp0xze41L6nFOS1ekDTPE',
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.BillingCreditBalanceTransactionListParams{
  Customer: stripe.String("cus_QrvQguzkIK8zTj"),
  CreditGrant: stripe.String("credgr_test_61R9ZkIkIzLSp0xze41L6nFOS1ekDTPE"),
}
result := sc.V1BillingCreditBalanceTransactions.List(context.TODO(), params)
```

```dotnet
var options = new Stripe.Billing.CreditBalanceTransactionListOptions
{
    Customer = "cus_QrvQguzkIK8zTj",
    CreditGrant = "credgr_test_61R9ZkIkIzLSp0xze41L6nFOS1ekDTPE",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Billing.CreditBalanceTransactions;
StripeList<Stripe.Billing.CreditBalanceTransaction> creditBalanceTransactions = service
    .List(options);
```

### Response

```json
{
  "object": "list",
  "data": [
    {
      "id": "cbtxn_test_61R9ZljjaFmdidb6e41L6nFOS1ekD9Ue",
      "object": "billing.credit_balance_transaction",
      "created": 1726619524,
      "credit": null,
      "credit_grant": "credgr_test_61R9ZkIkIzLSp0xze41L6nFOS1ekDTPE",
      "debit": {
        "amount": {
          "monetary": {
            "currency": "usd",
            "value": 1000
          },
          "type": "monetary"
        },
        "credits_applied": {
          "invoice": "in_1Q0BoLL6nFOS1ekDbwBM5ER1",
          "invoice_line_item": "il_1QB443L6nFOS1ekDwRiN3Z4n"
        },
        "type": "credits_applied"
      },
      "effective_at": 1729211351,
      "livemode": false,
      "test_clock": "clock_1Q0BoJL6nFOS1ekDbyYYuseM",
      "type": "debit"
    },
    {
      "id": "cbtxn_test_61R9ZkIbb17ze4b2s41L6nFOS1ekDXHs",
      "object": "billing.credit_balance_transaction",
      "created": 1726619434,
      "credit": {
        "amount": {
          "monetary": {
            "currency": "usd",
            "value": 1000
          },
          "type": "monetary"
        },
        "type": "credits_granted"
      },
      "credit_grant": "credgr_test_61R9ZkIkIzLSp0xze41L6nFOS1ekDTPE",
      "debit": null,
      "effective_at": 1726619434,
      "livemode": false,
      "test_clock": "clock_1Q0BoJL6nFOS1ekDbyYYuseM",
      "type": "credit"
    }
  ],
  "has_more": false,
  "url": "/v1/billing/credit_grants"
}
```