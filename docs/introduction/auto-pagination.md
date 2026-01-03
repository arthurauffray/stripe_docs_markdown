# Auto-pagination

Our libraries support auto-pagination. This feature allows you to easily iterate through large lists of resources without having to manually perform the requests to fetch subsequent pages.

Since curl simply emits raw HTTP requests, it doesn’t support auto-pagination.

Since the CLI simply emits raw HTTP requests, it doesn’t support auto-pagination.

To use the auto-pagination feature in Ruby, simply issue an initial “list” call with the parameters you need, then call `auto_paging_each` on the returned list object to iterate over all objects matching your initial parameters.

To use the auto-pagination feature in Python, simply issue an initial “list” call with the parameters you need, then call `auto_paging_iter()` on the returned list object to iterate over all objects matching your initial parameters.

To use the auto-pagination feature in PHP, simply issue an initial “list” call with the parameters you need, then call `autoPagingIterator()` on the returned list object to iterate over all objects matching your initial parameters.

To use the auto-pagination feature in Java, simply issue an initial “list” call with the parameters you need, then call `autoPagingIterable()` on the returned list object to iterate over all objects matching your initial parameters.

To use the auto-pagination feature in Node 10+, simply iterate over a “list” call with the parameters you need in a `for await` loop.

To use the auto-pagination feature in older versions of Node, issue a “list” call with the parameters you need, then call `autoPagingEach(onItem)` on the returned list object to iterate over all objects matching your initial parameters.

Full docs are on the [stripe-node GitHub repository](https://github.com/stripe/stripe-node#auto-pagination).

Auto-pagination in Go is enabled by default. It can be disabled by setting the Single option to true in any ListParams struct.

To use the auto-pagination feature in .NET, simply callListAutoPaging with the same parameters that you would use in a regular List call and iterate over the results.

```sh
# The auto-pagination feature is specific to Stripe's
# libraries and cannot be used directly with curl.
```

```ruby
require 'stripe'
Stripe.api_key = 'sk_test_xLhH7sntJEJFllhPZwbGU0Sj'

customers = Stripe::Customer.list({limit: 3})
customers.auto_paging_each do |customer|
  # Do something with customer
end
```

```sh
# The auto-pagination feature is specific to Stripe's
# libraries and cannot be used directly with the CLI.
```

```python
import stripe
stripe.api_key = "sk_test_xLhH7sntJEJFllhPZwbGU0Sj"

customers = stripe.Customer.list(limit=3)
for customer in customers.auto_paging_iter():
  # Do something with customer
```

```php
$stripe = new \Stripe\StripeClient("sk_test_xLhH7sntJEJFllhPZwbGU0Sj");
$customers = $stripe->customers->all([
  'limit' => 3,
]);
foreach ($customers->autoPagingIterator() as $customer) {
  // Do something with $customer
}
```

```java
Stripe.apiKey = "sk_test_xLhH7sntJEJFllhPZwbGU0Sj";

Map<String, Object> customerParams = new HashMap<>();
customerParams.put("limit", 3);

Iterable<Customers> itCustomers = Customer.list(customerParams).autoPagingIterable();

for (Customer customer : itCustomers) {
  // Do something with customer
}
```

```javascript
const Stripe = require('stripe');
const stripe = Stripe('sk_test_xLhH7sntJEJFllhPZwbGU0Sj');
// In Node 10+:
for await (const customer of stripe.customers.list({limit: 3})) {
  // Do something with customer
}

// In other environments:
stripe.customers.list({limit: 3})
  .autoPagingEach(function(customer) {
    // Do something with customer
  });
```

```go
stripe.Key = "sk_test_xLhH7sntJEJFllhPZwbGU0Sj"

params := &stripe.CustomerListParams{}
params.Filters.AddFilter("limit", "", "3")
i := customer.List(params)
for i.Next() {
  customer := i.Customer()
  // Do something with customer
}
```

```dotnet
StripeConfiguration.ApiKey = "sk_test_xLhH7sntJEJFllhPZwbGU0Sj";

var service = new CustomerService();
var options = new CustomerListOptions {
  Limit = 3
};

// Synchronously paginate
foreach (var customer in service.ListAutoPaging(options)) {
  // Do something with customer
}

// Asynchronously paginate
await foreach (var customer in service.ListAutoPagingAsync(options)) {
  // Do something with customer
}
```