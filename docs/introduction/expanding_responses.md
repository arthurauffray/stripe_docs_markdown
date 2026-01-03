# Expanding Responses

Many objects allow you to request additional information as an expanded response by using the `expand` request parameter. This parameter is available on all API requests, and applies to the response of that request only. You can expand responses in two ways.

In many cases, an object contains the ID of a related object in its response properties. For example, a `Charge` might have an associated Customer ID. You can expand these objects in line with the expand request parameter. The `expandable` label in this documentation indicates ID fields that you can expand into objects.

Some available fields aren’t included in the responses by default, such as the `number` and `cvc` fields for the Issuing Card object. You can request these fields as an expanded response by using the `expand` request parameter.

You can expand recursively by specifying nested fields after a dot (`.`). For example, requesting `payment_intent.customer` on a charge expands the `payment_intent` property into a full PaymentIntent object, then expands the `customer` property on that payment intent into a full Customer object.

You can use the `expand` parameter on any endpoint that returns expandable fields, including list, create, and update endpoints.

Expansions on list requests start with the `data` property. For example, you can expand `data.customers` on a request to list charges and associated customers. Performing deep expansions on numerous list requests might result in slower processing times.

Expansions have a maximum depth of four levels (for example, the deepest expansion allowed when listing charges is `data.payment_intent.customer.default_source`).

You can expand multiple objects at the same time by identifying multiple items in the `expand` array.

- Related guide: [Expanding responses](https://docs.stripe.com/expand.md)
- Related video: [Expand](https://www.youtube.com/watch?v=m8Vj_CEWyQc)

```sh
curl https://api.stripe.com/v1/charges/ch_3LmzzQ2eZvKYlo2C0XjzUzJV \
  -u sk_test_xLhH7sntJEJFllhPZwbGU0Sj: \
  -d "expand[]"=customer \
  -d "expand[]"="payment_intent.customer" \
  -G
```

### Global API Key

```ruby
require 'stripe'
Stripe.api_key = 'sk_test_xLhH7sntJEJFllhPZwbGU0Sj'

Stripe::Charge.retrieve({
  id: 'ch_3Ln0gP2eZvKYlo2C1Dnjwdpu',
  expand: ['customer', 'payment_intent.customer'],
})
```

```sh
stripe charges retrieve ch_3Ln0gE2eZvKYlo2C053ToesO \
    --expand=customer \
    --expand=payment_intent.customer
```

```python
import stripe
stripe.api_key = "sk_test_xLhH7sntJEJFllhPZwbGU0Sj"

stripe.Charge.retrieve(
  'ch_3Ln0cK2eZvKYlo2C1QmvaARY',
  expand=['customer', 'payment_intent.customer']
)
```

```php
$stripe = new \Stripe\StripeClient("sk_test_xLhH7sntJEJFllhPZwbGU0Sj");
$stripe->charges->retrieve(
  'ch_3Ln0WI2eZvKYlo2C1PO0FwVL',
  ['expand' => ['customer', 'payment_intent.customer']]
);
```

```java
Stripe.apiKey = "sk_test_xLhH7sntJEJFllhPZwbGU0Sj";

List<String> expandList = new ArrayList<>();
expandList.add("customer");
expandList.add("payment_intent.customer");

Map<String, Object> params = new HashMap<>();
params.put("expand", expandList);

Charge charge = Charge.retrieve("ch_3Ln0Z82eZvKYlo2C0Ldu2duz", params, null);
```

```javascript
const Stripe = require('stripe');
const stripe = Stripe('sk_test_xLhH7sntJEJFllhPZwbGU0Sj');
stripe.charges.retrieve('ch_3Ln0H22eZvKYlo2C0tgkG5bn', {
  expand: ['customer', 'payment_intent.customer'],
});
```

```go
stripe.Key = "sk_test_xLhH7sntJEJFllhPZwbGU0Sj"

params := &stripe.ChargeParams{}
params.AddExpand("customer")
params.AddExpand("payment_intent.customer")
ch, err := charge.Get("ch_3Ln0Ma2eZvKYlo2C1XyBAcDu", params)
```

```dotnet
StripeConfiguration.ApiKey = "sk_test_xLhH7sntJEJFllhPZwbGU0Sj";

var service = new ChargeService();
var options = new ChargeGetOptions();
options.AddExpand("customer");
options.AddExpand("payment_intent.customer");

var charge = service.Get("ch_3Ln0Z72eZvKYlo2C0cMcdZfa", options);
```

### Response

```json
{
  "id": "ch_3LmzzQ2eZvKYlo2C0XjzUzJV",
  "object": "charge",
  "customer": {
    "id": "cu_14HOpH2eZvKYlo2CxXIM7Pb2",
    "object": "customer",
    // ...
  },
  "payment_intent": {
    "id": "pi_3MtwBwLkdIwHu7ix28a3tqPa",
    "object": "payment_intent",
    "customer": {
      "id": "cus_NffrFeUfNV2Hib",
      "object": "customer",
      // ...
    },
    // ...
  },
  // ...
}
```