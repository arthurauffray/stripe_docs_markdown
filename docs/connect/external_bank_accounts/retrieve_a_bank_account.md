# Retrieve a bank account

By default, you can see the 10 most recent external accounts stored on a [connected account](https://docs.stripe.com/connect/accounts.md) directly on the object. You can also retrieve details about a specific bank account stored on the account.

## Returns

Returns the bank account object.

## Parameters

- `id` (string, required)
  Unique identifier for the external account to be retrieved.

```curl
curl https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts/ba_1NAinX2eZvKYlo2CpFGcuuEG \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe external_accounts retrieve acct_1032D82eZvKYlo2C ba_1NAinX2eZvKYlo2CpFGcuuEG
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

result = client.v1.accounts.external_accounts.retrieve(
  'acct_1032D82eZvKYlo2C',
  'ba_1NAinX2eZvKYlo2CpFGcuuEG',
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

external_account = client.v1.accounts.external_accounts.retrieve(
  "acct_1032D82eZvKYlo2C",
  "ba_1NAinX2eZvKYlo2CpFGcuuEG",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$externalAccount = $stripe->accounts->retrieveExternalAccount(
  'acct_1032D82eZvKYlo2C',
  'ba_1NAinX2eZvKYlo2CpFGcuuEG',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AccountExternalAccountRetrieveParams params =
  AccountExternalAccountRetrieveParams.builder().build();

ExternalAccount externalAccount =
  client.v1().accounts().externalAccounts().retrieve(
    "acct_1032D82eZvKYlo2C",
    "ba_1NAinX2eZvKYlo2CpFGcuuEG",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const externalAccount = await stripe.accounts.retrieveExternalAccount(
  'acct_1032D82eZvKYlo2C',
  'ba_1NAinX2eZvKYlo2CpFGcuuEG'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.BankAccountRetrieveParams{
  Account: stripe.String("acct_1032D82eZvKYlo2C"),
}
result, err := sc.V1BankAccounts.Retrieve(
  context.TODO(), "ba_1NAinX2eZvKYlo2CpFGcuuEG", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Accounts.ExternalAccounts;
IExternalAccount iExternalAccount = service.Get(
    "acct_1032D82eZvKYlo2C",
    "ba_1NAinX2eZvKYlo2CpFGcuuEG");
```

### Response

```json
{
  "id": "ba_1NAinX2eZvKYlo2CpFGcuuEG",
  "object": "bank_account",
  "account_holder_name": "Jane Austen",
  "account_holder_type": "company",
  "account_type": null,
  "bank_name": "STRIPE TEST BANK",
  "country": "US",
  "currency": "usd",
  "customer": null,
  "fingerprint": "1JWtPxqbdX5Gamtc",
  "last4": "6789",
  "metadata": {},
  "routing_number": "110000000",
  "status": "new"
}
```