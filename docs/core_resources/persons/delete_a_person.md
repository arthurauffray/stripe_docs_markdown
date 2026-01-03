# Delete a person

Delete a Person associated with an Account.

## Parameters

- `account_id` (string, required)
  The Account the Person is associated with.

- `id` (string, required)
  The ID of the Person to delete.

## Returns

## Response attributes

- `id` (string)
  Person deleted.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `deleted` (boolean)
  Always true for a deleted object.

## Error Codes

| HTTP status code | Code                               | Description                                       |
| ---------------- | ---------------------------------- | ------------------------------------------------- |
| 400              | account_not_yet_compatible_with_v2 | Account is not yet compatible with V2 APIs.       |
| 400              | accounts_v2_access_blocked         | Accounts v2 is not enabled for your platform.     |
| 400              | v1_account_instead_of_v2_account   | V1 Account ID cannot be used in V2 Account APIs.  |
| 400              | v1_customer_instead_of_v2_account  | V1 Customer ID cannot be used in V2 Account APIs. |
| 404              | not_found                          | The resource wasn’t found.                        |

```curl
curl -X DELETE https://api.stripe.com/v2/core/accounts/acct_1Nv0FGQ9RKHgCVdK/persons/person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: {{STRIPE_API_VERSION}}"
```

```cli
stripe v2 core accounts persons delete acct_1Nv0FGQ9RKHgCVdK person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

deleted = client.v2.core.accounts.persons.delete(
  'acct_1Nv0FGQ9RKHgCVdK',
  'person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY',
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

deleted = client.v2.core.accounts.persons.delete(
  "acct_1Nv0FGQ9RKHgCVdK",
  "person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$deleted = $stripe->v2->core->accounts->persons->delete(
  'acct_1Nv0FGQ9RKHgCVdK',
  'person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

DeletedObject deletedObject =
  client.v2().core().accounts().persons().delete(
    "acct_1Nv0FGQ9RKHgCVdK",
    "person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY"
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const deleted = await stripe.v2.core.accounts.persons.del(
  'acct_1Nv0FGQ9RKHgCVdK',
  'person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.V2CoreAccountsPersonDeleteParams{
  AccountID: stripe.String("acct_1Nv0FGQ9RKHgCVdK"),
}
result, err := sc.V2CoreAccountsPersons.Delete(
  context.TODO(), "person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V2.Core.Accounts.Persons;
Stripe.V2.DeletedObject deleted = service.Delete(
    "acct_1Nv0FGQ9RKHgCVdK",
    "person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY");
```

### Response

```json
{
  "id": "person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY",
  "object": "v2.core.account_person",
  "deleted": true
}
```