# Delete a person

Deletes an existing person’s relationship to the account’s legal entity. Any person with a relationship for an account can be deleted through the API, except if the person is the `account_opener`. If your integration is using the `executive` parameter, you cannot delete the only verified `executive` on file.

## Returns

Returns the deleted [`person`](https://docs.stripe.com/api/persons/object.md) object.

```curl
curl -X DELETE https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/persons/person_1MqjB62eZvKYlo2CaeEJzKVR \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe persons delete acct_1032D82eZvKYlo2C person_1MqjB62eZvKYlo2CaeEJzKVR
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

deleted = client.v1.accounts.persons.delete(
  'acct_1032D82eZvKYlo2C',
  'person_1MqjB62eZvKYlo2CaeEJzKVR',
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

deleted = client.v1.accounts.persons.delete(
  "acct_1032D82eZvKYlo2C",
  "person_1MqjB62eZvKYlo2CaeEJzKVR",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$deleted = $stripe->accounts->deletePerson(
  'acct_1032D82eZvKYlo2C',
  'person_1MqjB62eZvKYlo2CaeEJzKVR',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

Person person =
  client.v1().accounts().persons().delete(
    "acct_1032D82eZvKYlo2C",
    "person_1MqjB62eZvKYlo2CaeEJzKVR"
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const deleted = await stripe.accounts.deletePerson(
  'acct_1032D82eZvKYlo2C',
  'person_1MqjB62eZvKYlo2CaeEJzKVR'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PersonDeleteParams{Account: stripe.String("acct_1032D82eZvKYlo2C")}
result, err := sc.V1Persons.Delete(
  context.TODO(), "person_1MqjB62eZvKYlo2CaeEJzKVR", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Accounts.Persons;
Person deleted = service.Delete(
    "acct_1032D82eZvKYlo2C",
    "person_1MqjB62eZvKYlo2CaeEJzKVR");
```

### Response

```json
{
  "id": "person_1MqjB62eZvKYlo2CaeEJzKVR",
  "object": "person",
  "deleted": true
}
```