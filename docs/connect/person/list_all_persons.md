# List all persons

Returns a list of people associated with the account’s legal entity. The people are returned sorted by creation date, with the most recent people appearing first.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` people, starting after person `starting_after`. Each entry in the array is a separate [`person`](https://docs.stripe.com/api/persons/object.md) object. If no more people are available, the resulting array will be empty.

## Parameters

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `relationship` (object, optional)
  Filters on the list of people returned based on the person’s relationship to the account’s company.

  - `relationship.authorizer` (boolean, optional)
    A filter on the list of people returned based on whether these people are authorizers of the account’s representative.

  - `relationship.director` (boolean, optional)
    A filter on the list of people returned based on whether these people are directors of the account’s company.

  - `relationship.executive` (boolean, optional)
    A filter on the list of people returned based on whether these people are executives of the account’s company.

  - `relationship.legal_guardian` (boolean, optional)
    A filter on the list of people returned based on whether these people are legal guardians of the account’s representative.

  - `relationship.owner` (boolean, optional)
    A filter on the list of people returned based on whether these people are owners of the account’s company.

  - `relationship.representative` (boolean, optional)
    A filter on the list of people returned based on whether these people are the representative of the account’s company.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/persons \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe accounts persons acct_1032D82eZvKYlo2C \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

persons = client.v1.accounts.persons.list('acct_1032D82eZvKYlo2C', {limit: 3})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

persons = client.v1.accounts.persons.list(
  "acct_1032D82eZvKYlo2C",
  {"limit": 3},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$persons = $stripe->accounts->allPersons('acct_1032D82eZvKYlo2C', ['limit' => 3]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AccountPersonListParams params =
  AccountPersonListParams.builder().setLimit(3L).build();

StripeCollection<Person> stripeCollection =
  client.v1().accounts().persons().list("acct_1032D82eZvKYlo2C", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const persons = await stripe.accounts.listPersons(
  'acct_1032D82eZvKYlo2C',
  {
    limit: 3,
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PersonListParams{Account: stripe.String("acct_1032D82eZvKYlo2C")}
params.Limit = stripe.Int64(3)
result := sc.V1Persons.List(context.TODO(), params)
```

```dotnet
var options = new AccountPersonListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Accounts.Persons;
StripeList<Person> persons = service.List("acct_1032D82eZvKYlo2C", options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/accounts/acct_1032D82eZvKYlo2C/persons",
  "has_more": false,
  "data": [
    {
      "id": "person_1MqjB62eZvKYlo2CaeEJzKVR",
      "person": "person_1MqjB62eZvKYlo2CaeEJzKVR",
      "object": "person",
      "account": "acct_1032D82eZvKYlo2C",
      "created": 1680035496,
      "dob": {
        "day": null,
        "month": null,
        "year": null
      },
      "first_name": "Jane",
      "future_requirements": {
        "alternatives": [],
        "currently_due": [],
        "errors": [],
        "eventually_due": [],
        "past_due": [],
        "pending_verification": []
      },
      "id_number_provided": false,
      "last_name": "Diaz",
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
  ]
}
```