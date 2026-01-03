# Create a login link

Creates a login link for a connected account to access the Express Dashboard.

**You can only create login links for accounts that use the [Express Dashboard](https://docs.stripe.com/connect/express-dashboard.md) and are connected to your platform**.

## Returns

Returns a login link object if the call succeeded.

```curl
curl -X POST https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/login_links \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe login_links create acct_1032D82eZvKYlo2C
```

```ruby
Stripe.api_key = "<<YOUR_SECRET_KEY>>"

Stripe::Account.create_login_link(
  "acct_1032D82eZvKYlo2C"
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

login_link = client.v1.accounts.login_links.create("acct_1032D82eZvKYlo2C")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$loginLink = $stripe->accounts->createLoginLink('acct_1032D82eZvKYlo2C', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AccountLoginLinkCreateParams params = AccountLoginLinkCreateParams.builder().build();

LoginLink loginLink =
  client.v1().accounts().loginLinks().create("acct_1032D82eZvKYlo2C", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const loginLink = await stripe.accounts.createLoginLink('acct_1032D82eZvKYlo2C');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.LoginLinkCreateParams{
  Account: stripe.String("acct_1032D82eZvKYlo2C"),
}
result, err := sc.V1LoginLinks.Create(context.TODO(), params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Accounts.LoginLinks;
LoginLink loginLink = service.Create("acct_1032D82eZvKYlo2C");
```

### Response

```json
{
  "object": "login_link",
  "created": 1686084879,
  "url": "https://connect.stripe.com/express/acct_1032D82eZvKYlo2C/F44eiGHh5sEV"
}
```