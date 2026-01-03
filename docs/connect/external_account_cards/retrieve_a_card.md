# Retrieve a card

By default, you can see the 10 most recent external accounts stored on a [connected account](https://docs.stripe.com/docs/connect/accounts.md) directly on the object. You can also retrieve details about a specific card stored on the account.

## Returns

Returns the card object.

## Parameters

- `id` (string, required)
  Unique identifier for the external account to be retrieved.

```curl
curl https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts/card_1NAinb2eZvKYlo2C1Fm9mZsu \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe external_accounts retrieve acct_1032D82eZvKYlo2C card_1NAinb2eZvKYlo2C1Fm9mZsu
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

result = client.v1.accounts.external_accounts.retrieve(
  'acct_1032D82eZvKYlo2C',
  'card_1NAinb2eZvKYlo2C1Fm9mZsu',
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

external_account = client.v1.accounts.external_accounts.retrieve(
  "acct_1032D82eZvKYlo2C",
  "card_1NAinb2eZvKYlo2C1Fm9mZsu",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$externalAccount = $stripe->accounts->retrieveExternalAccount(
  'acct_1032D82eZvKYlo2C',
  'card_1NAinb2eZvKYlo2C1Fm9mZsu',
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
    "card_1NAinb2eZvKYlo2C1Fm9mZsu",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const externalAccount = await stripe.accounts.retrieveExternalAccount(
  'acct_1032D82eZvKYlo2C',
  'card_1NAinb2eZvKYlo2C1Fm9mZsu'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.BankAccountRetrieveParams{
  Account: stripe.String("acct_1032D82eZvKYlo2C"),
}
result, err := sc.V1BankAccounts.Retrieve(
  context.TODO(), "card_1NAinb2eZvKYlo2C1Fm9mZsu", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Accounts.ExternalAccounts;
IExternalAccount iExternalAccount = service.Get(
    "acct_1032D82eZvKYlo2C",
    "card_1NAinb2eZvKYlo2C1Fm9mZsu");
```

### Response

```json
{
  "id": "card_1NAinb2eZvKYlo2C1Fm9mZsu",
  "object": "card",
  "address_city": null,
  "address_country": null,
  "address_line1": null,
  "address_line1_check": null,
  "address_line2": null,
  "address_state": null,
  "address_zip": null,
  "address_zip_check": null,
  "brand": "Visa",
  "country": "US",
  "cvc_check": "pass",
  "dynamic_last4": null,
  "exp_month": 8,
  "exp_year": 2024,
  "fingerprint": "Xt5EWLLDS7FJjR1c",
  "funding": "credit",
  "last4": "4242",
  "metadata": {},
  "name": null,
  "redaction": null,
  "tokenization_method": null,
  "wallet": null,
  "account": "acct_1032D82eZvKYlo2C"
}
```