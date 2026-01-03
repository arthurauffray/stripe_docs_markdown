# Delete an event destination

Delete an event destination.

## Parameters

- `id` (string, required)
  Identifier for the event destination to delete.

## Returns

## Response attributes

- `id` (string)
  Identifier for the deleted event destination.

## Error Codes

| HTTP status code | Code              | Description                                                     |
| ---------------- | ----------------- | --------------------------------------------------------------- |
| 404              | not_found         | The resource wasn’t found.                                      |
| 409              | idempotency_error | An idempotent retry occurred with different request parameters. |

```curl
curl -X DELETE https://api.stripe.com/v2/core/event_destinations/ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6 \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: {{STRIPE_API_VERSION}}"
```

```cli
stripe v2 core event_destinations delete ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

deleted = client.v2.core.event_destinations.delete('ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

deleted = client.v2.core.event_destinations.delete(
  "ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$deleted = $stripe->v2->core->eventDestinations->delete(
  'ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

DeletedObject deletedObject =
  client.v2().core().eventDestinations().delete(
    "ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6"
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const deleted = await stripe.v2.core.eventDestinations.del(
  'ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.V2CoreEventDestinationDeleteParams{}
result, err := sc.V2CoreEventDestinations.Delete(
  context.TODO(), "ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V2.Core.EventDestinations;
Stripe.V2.DeletedObject deleted = service.Delete(
    "ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6");
```

### Response

```json
{
  "id": "ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6"
}
```