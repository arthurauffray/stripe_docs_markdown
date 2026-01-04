# Delete a card

You can delete cards from a customer. If you delete a card that is currently the default source, then the most recently added source will become the new default. If you delete a card that is the last remaining source on the customer, then the default_source attribute will become null.

For recipients: if you delete the default card, then the most recently added card will become the new default. If you delete the last remaining card on a recipient, then the default_card attribute will become null.

Note that for cards belonging to customers, you might want to prevent customers on paid subscriptions from deleting all cards on file, so that there is at least one default card for the next invoice payment attempt.

## Returns

```curl
curl -X DELETE https://api.stripe.com/v1/customers/acct_1032D82eZvKYlo2C/sources/card_1NGTaT2eZvKYlo2CZWSctn5n \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe bank_accounts delete acct_1032D82eZvKYlo2C card_1NGTaT2eZvKYlo2CZWSctn5n
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

result = client.v1.sources.detach(
  'acct_1032D82eZvKYlo2C',
  'card_1NGTaT2eZvKYlo2CZWSctn5n',
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

payment_source = client.v1.sources.detach(
  "acct_1032D82eZvKYlo2C",
  "card_1NGTaT2eZvKYlo2CZWSctn5n",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentSource = $stripe->customers->deleteSource(
  'acct_1032D82eZvKYlo2C',
  'card_1NGTaT2eZvKYlo2CZWSctn5n',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

SourceDetachParams params = SourceDetachParams.builder().build();

PaymentSource paymentSource =
  client.v1().sources().detach(
    "acct_1032D82eZvKYlo2C",
    "card_1NGTaT2eZvKYlo2CZWSctn5n",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customerSource = await stripe.customers.deleteSource(
  'acct_1032D82eZvKYlo2C',
  'card_1NGTaT2eZvKYlo2CZWSctn5n'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CardDeleteParams{Customer: stripe.String("acct_1032D82eZvKYlo2C")}
result, err := sc.V1Cards.Delete(
  context.TODO(), "card_1NGTaT2eZvKYlo2CZWSctn5n", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Sources;
IPaymentSource iPaymentSource = service.Detach(
    "acct_1032D82eZvKYlo2C",
    "card_1NGTaT2eZvKYlo2CZWSctn5n");
```

### Response

```json
{
  "id": "card_1NGTaT2eZvKYlo2CZWSctn5n",
  "object": "card",
  "deleted": true
}
```