# Retrieve a credit balance transaction

Retrieves a credit balance transaction.

## Returns

Returns a credit balance transaction.

## Parameters

- `id` (string, required)
  Unique identifier for the object.

```curl
curl https://api.stripe.com/v1/billing/credit_balance_transactions/cbtxn_test_61R9ZljjaFmdidb6e41L6nFOS1ekD9Ue \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe billing credit_balance_transactions retrieve cbtxn_test_61R9ZljjaFmdidb6e41L6nFOS1ekD9Ue
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

credit_balance_transaction = client.v1.billing.credit_balance_transactions.retrieve('cbtxn_test_61R9ZljjaFmdidb6e41L6nFOS1ekD9Ue')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

credit_balance_transaction = client.v1.billing.credit_balance_transactions.retrieve(
  "cbtxn_test_61R9ZljjaFmdidb6e41L6nFOS1ekD9Ue",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$creditBalanceTransaction = $stripe->billing->creditBalanceTransactions->retrieve(
  'cbtxn_test_61R9ZljjaFmdidb6e41L6nFOS1ekD9Ue',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CreditBalanceTransactionRetrieveParams params =
  CreditBalanceTransactionRetrieveParams.builder().build();

CreditBalanceTransaction creditBalanceTransaction =
  client.v1().billing().creditBalanceTransactions().retrieve(
    "cbtxn_test_61R9ZljjaFmdidb6e41L6nFOS1ekD9Ue",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const creditBalanceTransaction = await stripe
  .billing
  .creditBalanceTransactions
  .retrieve('cbtxn_test_61R9ZljjaFmdidb6e41L6nFOS1ekD9Ue');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.BillingCreditBalanceTransactionRetrieveParams{}
result, err := sc.V1BillingCreditBalanceTransactions.Retrieve(
  context.TODO(), "cbtxn_test_61R9ZljjaFmdidb6e41L6nFOS1ekD9Ue", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Billing.CreditBalanceTransactions;
Stripe.Billing.CreditBalanceTransaction creditBalanceTransaction = service.Get(
    "cbtxn_test_61R9ZljjaFmdidb6e41L6nFOS1ekD9Ue");
```

### Response

```json
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
}
```