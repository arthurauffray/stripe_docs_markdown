# List all bank accounts

You can see a list of the bank accounts that belong to a [connected account](https://docs.stripe.com/docs/connect/accounts.md). Note that the 10 most recent external accounts are always available by default on the corresponding Stripe object. If you need more than those 10, you can use this API method and the `limit` and `starting_after` parameters to page through additional bank accounts.

## Returns

Returns a list of the bank accounts stored on the account.

## Parameters

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `object` (string, optional)
  Filter external accounts according to a particular object type.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts \
  -u "<<YOUR_SECRET_KEY>>" \
  -d object=bank_account
```

```cli
stripe external_accounts list acct_1032D82eZvKYlo2C \
  --object=bank_account
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

result = client.v1.accounts.external_accounts.list(
  'acct_1032D82eZvKYlo2C',
  {object: 'bank_account'},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

external_accounts = client.v1.accounts.external_accounts.list(
  "acct_1032D82eZvKYlo2C",
  {"object": "bank_account"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$externalAccounts = $stripe->accounts->allExternalAccounts(
  'acct_1032D82eZvKYlo2C',
  ['object' => 'bank_account']
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AccountExternalAccountListParams params =
  AccountExternalAccountListParams.builder().setObject("bank_account").build();

StripeCollection<ExternalAccount> stripeCollection =
  client.v1().accounts().externalAccounts().list("acct_1032D82eZvKYlo2C", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const externalAccounts = await stripe.accounts.listExternalAccounts(
  'acct_1032D82eZvKYlo2C',
  {
    object: 'bank_account',
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.BankAccountListParams{
  Object: stripe.String("bank_account"),
  Account: stripe.String("acct_1032D82eZvKYlo2C"),
}
result := sc.V1BankAccounts.List(context.TODO(), params)
```

```dotnet
var options = new AccountExternalAccountListOptions { Object = "bank_account" };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Accounts.ExternalAccounts;
StripeList<IExternalAccount> iExternalAccounts = service.List(
    "acct_1032D82eZvKYlo2C",
    options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts",
  "has_more": false,
  "data": [
    {
      "id": "ba_1NB1IV2eZvKYlo2CByiLrMWv",
      "object": "bank_account",
      "account_holder_name": "Jane Austen",
      "account_holder_type": "company",
      "account_type": null,
      "bank_name": "STRIPE TEST BANK",
      "country": "US",
      "currency": "usd",
      "fingerprint": "1JWtPxqbdX5Gamtc",
      "last4": "6789",
      "metadata": {},
      "routing_number": "110000000",
      "status": "new",
      "account": "acct_1032D82eZvKYlo2C"
    }
  ]
}
```