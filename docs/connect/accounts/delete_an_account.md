# Delete an account

With [Connect](https://docs.stripe.com/connect.md), you can delete accounts you manage.

Test-mode accounts can be deleted at any time.

Live-mode accounts that have access to the standard dashboard and Stripe is responsible for negative account balances cannot be deleted, which includes Standard accounts. All other Live-mode accounts, can be deleted when all [balances](https://docs.stripe.com/api/balance/balance_object.md) are zero.

If you want to delete your own account, use the [account information tab in your account settings](https://dashboard.stripe.com/settings/account) instead.

## Returns

Returns an object with a deleted parameter if the call succeeds. If the account ID does not exist, this call raises [an error](https://docs.stripe.com/api/accounts/delete.md#errors).

```curl
curl -X DELETE https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe accounts delete acct_1032D82eZvKYlo2C
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

deleted = client.v1.accounts.delete('acct_1032D82eZvKYlo2C')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

deleted = client.v1.accounts.delete("acct_1032D82eZvKYlo2C")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$deleted = $stripe->accounts->delete('acct_1032D82eZvKYlo2C', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

Account account = client.v1().accounts().delete("acct_1032D82eZvKYlo2C");
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const deleted = await stripe.accounts.del('acct_1032D82eZvKYlo2C');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.AccountDeleteParams{}
result, err := sc.V1Accounts.Delete(context.TODO(), "acct_1032D82eZvKYlo2C", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Accounts;
Account deleted = service.Delete("acct_1032D82eZvKYlo2C");
```

### Response

```json
{
  "id": "acct_1Nv0FGQ9RKHgCVdK",
  "object": "account",
  "deleted": true
}
```