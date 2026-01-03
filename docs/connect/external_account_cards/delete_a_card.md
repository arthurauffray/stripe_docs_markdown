# Delete a card

You can delete cards from a connected account where [controller.requirement_collection](https://docs.stripe.com/api/accounts/object.md#account_object-controller-requirement_collection) is `application` (includes [Custom accounts](https://docs.stripe.com/connect/custom-accounts.md)).

There are restrictions for deleting a card with `default_for_currency` set to true. You cannot delete a card if any of the following apply:

- The card’s `currency` is the same as the connected account’s [default_currency](https://docs.stripe.com/api/accounts/object.md#account_object-default_currency).
- There is another external account (card or bank account) with the same currency as the card.

To delete a card, you must first replace the default external account by setting `default_for_currency` with another external account in the same currency.

## Returns

Returns the deleted card object.

## Parameters

- `id` (string, required)
  Unique identifier for the external account to be deleted.

```curl
curl -X DELETE https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts/card_1NAz2x2eZvKYlo2C75wJ1YUs \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe external_accounts delete acct_1032D82eZvKYlo2C card_1NAz2x2eZvKYlo2C75wJ1YUs
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

deleted = client.v1.accounts.external_accounts.delete(
  'acct_1032D82eZvKYlo2C',
  'card_1NAz2x2eZvKYlo2C75wJ1YUs',
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

deleted = client.v1.accounts.external_accounts.delete(
  "acct_1032D82eZvKYlo2C",
  "card_1NAz2x2eZvKYlo2C75wJ1YUs",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$deleted = $stripe->accounts->deleteExternalAccount(
  'acct_1032D82eZvKYlo2C',
  'card_1NAz2x2eZvKYlo2C75wJ1YUs',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ExternalAccount externalAccount =
  client.v1().accounts().externalAccounts().delete(
    "acct_1032D82eZvKYlo2C",
    "card_1NAz2x2eZvKYlo2C75wJ1YUs"
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const deleted = await stripe.accounts.deleteExternalAccount(
  'acct_1032D82eZvKYlo2C',
  'card_1NAz2x2eZvKYlo2C75wJ1YUs'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.BankAccountDeleteParams{
  Account: stripe.String("acct_1032D82eZvKYlo2C"),
}
result, err := sc.V1BankAccounts.Delete(
  context.TODO(), "card_1NAz2x2eZvKYlo2C75wJ1YUs", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Cards;
IExternalAccount deleted = service.Delete(
    "acct_1032D82eZvKYlo2C",
    "card_1NAz2x2eZvKYlo2C75wJ1YUs");
```

### Response

```json
{
  "id": "card_1NAz2x2eZvKYlo2C75wJ1YUs",
  "object": "card",
  "deleted": true
}
```