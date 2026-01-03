# Idempotent requests

The API supports [idempotency](https://en.wikipedia.org/wiki/Idempotence) for safely retrying requests without accidentally performing the same operation twice. When creating or updating an object, use an idempotency key. Then, if a connection error occurs, you can safely repeat the request without risk of creating a second object or performing the update twice.

To perform an idempotent request, provide an additional `IdempotencyKey` element to the request options.

Stripe’s idempotency works by saving the resulting status code and body of the first request made for any given idempotency key, regardless of whether it succeeds or fails. Subsequent requests with the same key return the same result, including `500` errors.

A client generates an idempotency key, which is a unique key that the server uses to recognize subsequent retries of the same request. How you create unique keys is up to you, but we suggest using V4 UUIDs, or another random string with enough entropy to avoid collisions. Idempotency keys are up to 255 characters long.

You can remove keys from the system automatically after they’re at least 24 hours old. We generate a new request if a key is reused after the original is pruned. The idempotency layer compares incoming parameters to those of the original request and errors if they’re not the same to prevent accidental misuse.

We save results only after the execution of an endpoint begins. If incoming parameters fail validation, or the request conflicts with another request that’s executing concurrently, we don’t save the idempotent result because no API endpoint initiates the execution. You can retry these requests. Learn more about when you can [retry idempotent requests](https://docs.stripe.com/error-low-level.md#idempotency).

All `POST` requests accept idempotency keys. Don’t send idempotency keys in `GET` and `DELETE` requests because it has no effect. These requests are idempotent by definition.

```sh
curl https://api.stripe.com/v1/customers \
  -u sk_test_xLhH7sntJEJFllhPZwbGU0Sj: \
  -H "Idempotency-Key: KG5LxwFBepaKHyUD" \
  -d description="My First Test Customer (created for API docs at https://docs.stripe.com/api)"
```

### Global API Key

```ruby
require 'stripe'
Stripe.api_key = 'sk_test_xLhH7sntJEJFllhPZwbGU0Sj'

customer = Stripe::Customer.create({
  description: 'My First Test Customer (created for API docs at https://docs.stripe.com/api)',
}, {
  idempotency_key: 'KG5LxwFBepaKHyUD',
})
```

```sh
stripe customers create \
    --idempotency=TvqqU7glUbURMzQT \
    --description="My First Test Customer (created for API docs at https://docs.stripe.com/api)" \
```

```python
import stripe
stripe.api_key = 'sk_test_xLhH7sntJEJFllhPZwbGU0Sj'

customer = stripe.Customer.create(
  description='My First Test Customer',
  idempotency_key='KG5LxwFBepaKHyUD',
)
```

```php
$stripe = new \Stripe\StripeClient('sk_test_xLhH7sntJEJFllhPZwbGU0Sj');
$customer = $stripe->customers->create([
  'description' => 'My First Test Customer (created for API docs at https://docs.stripe.com/api)',
], [
  'idempotency_key' => 'KG5LxwFBepaKHyUD'
]);
```

```java
Stripe.apiKey = "sk_test_xLhH7sntJEJFllhPZwbGU0Sj";

Map<String, Object> customerParams = new HashMap<>();
customerParams.put("description", "My First Test Customer (created for API docs at https://docs.stripe.com/api)");

RequestOptions options =
  RequestOptions.builder()
    .setIdempotencyKey("KG5LxwFBepaKHyUD")
    .build();

Customer customer = Customer.create(customerParams, options);
```

```javascript
const Stripe = require('stripe');
const stripe = Stripe('sk_test_xLhH7sntJEJFllhPZwbGU0Sj');
const customer = await stripe.customers.create(
  {
    description: 'My First Test Customer (created for API docs at https://docs.stripe.com/api)',
  },
  {
    idempotencyKey: 'KG5LxwFBepaKHyUD',
  }
);
```

```go
stripe.Key = "sk_test_xLhH7sntJEJFllhPZwbGU0Sj"

params := &stripe.CustomerParams{
  Description: stripe.String("My First Test Customer (created for API docs at https://docs.stripe.com/api)"),
}
params.SetIdempotencyKey("KG5LxwFBepaKHyUD")
cus, err := customer.New(params)
```

```dotnet
StripeConfiguration.ApiKey = "sk_test_xLhH7sntJEJFllhPZwbGU0Sj";

var options = new CustomerCreateOptions
{
  Description = "My First Test Customer (created for API docs at https://docs.stripe.com/api)",
};
var requestOptions = new RequestOptions
{
  IdempotencyKey = "KG5LxwFBepaKHyUD",
};
var service = new CustomerService();
var customer = service.Create(options, requestOptions);
```