# Retrieve a person

Retrieves an existing person.

## Returns

Returns a [`person`](https://docs.stripe.com/api/persons/object.md) object.

```curl
curl https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/persons/person_1MqjB62eZvKYlo2CaeEJzKVR \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe persons retrieve acct_1032D82eZvKYlo2C person_1MqjB62eZvKYlo2CaeEJzKVR
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

person = client.v1.accounts.persons.retrieve(
  'acct_1032D82eZvKYlo2C',
  'person_1MqjB62eZvKYlo2CaeEJzKVR',
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

person = client.v1.accounts.persons.retrieve(
  "acct_1032D82eZvKYlo2C",
  "person_1MqjB62eZvKYlo2CaeEJzKVR",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$person = $stripe->accounts->retrievePerson(
  'acct_1032D82eZvKYlo2C',
  'person_1MqjB62eZvKYlo2CaeEJzKVR',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AccountPersonRetrieveParams params = AccountPersonRetrieveParams.builder().build();

Person person =
  client.v1().accounts().persons().retrieve(
    "acct_1032D82eZvKYlo2C",
    "person_1MqjB62eZvKYlo2CaeEJzKVR",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const person = await stripe.accounts.retrievePerson(
  'acct_1032D82eZvKYlo2C',
  'person_1MqjB62eZvKYlo2CaeEJzKVR'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PersonRetrieveParams{
  Account: stripe.String("acct_1032D82eZvKYlo2C"),
}
result, err := sc.V1Persons.Retrieve(
  context.TODO(), "person_1MqjB62eZvKYlo2CaeEJzKVR", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Accounts.Persons;
Person person = service.Get(
    "acct_1032D82eZvKYlo2C",
    "person_1MqjB62eZvKYlo2CaeEJzKVR");
```

### Response

```json
{
  "id": "person_1N9XNb2eZvKYlo2CjPX7xF6F",
  "object": "person",
  "account": "acct_1032D82eZvKYlo2C",
  "created": 1684518375,
  "dob": {
    "day": null,
    "month": null,
    "year": null
  },
  "first_name": null,
  "future_requirements": {
    "alternatives": [],
    "currently_due": [],
    "errors": [],
    "eventually_due": [],
    "past_due": [],
    "pending_verification": []
  },
  "id_number_provided": false,
  "last_name": null,
  "metadata": {},
  "relationship": {
    "director": false,
    "executive": false,
    "owner": false,
    "percent_ownership": null,
    "representative": false,
    "title": null
  },
  "requirements": {
    "alternatives": [],
    "currently_due": [],
    "errors": [],
    "eventually_due": [],
    "past_due": [],
    "pending_verification": []
  },
  "ssn_last_4_provided": false,
  "verification": {
    "additional_document": {
      "back": null,
      "details": null,
      "details_code": null,
      "front": null
    },
    "details": null,
    "details_code": null,
    "document": {
      "back": null,
      "details": null,
      "details_code": null,
      "front": null
    },
    "status": "unverified"
  }
}
```