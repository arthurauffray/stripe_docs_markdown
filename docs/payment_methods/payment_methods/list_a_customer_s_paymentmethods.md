# List a Customer's PaymentMethods

Returns a list of PaymentMethods for a given Customer

## Returns

A dictionary with a `data` property that contains an array of up to `limit` PaymentMethods of type `type`, starting after PaymentMethods `starting_after`. Each entry in the array is a separate PaymentMethod object. If no more PaymentMethods are available, the resulting array will be empty.

## Parameters

- `allow_redisplay` (enum, optional)
  This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow.
Possible enum values:
  - `always`
    Use `always` to indicate that this payment method can always be shown to a customer in a checkout flow.

  - `limited`
    Use `limited` to indicate that this payment method can’t always be shown to a customer in a checkout flow. For example, it can only be shown in the context of a specific subscription.

  - `unspecified`
    This is the default value for payment methods where `allow_redisplay` wasn’t set.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `type` (enum, optional)
  An optional filter on the list, based on the object `type` field. Without the filter, the list includes all current and future payment method types. If your integration expects only one type of payment method in the response, make sure to provide a type value in the request.

```curl
curl -G https://api.stripe.com/v1/customers/cus_9s6XKzkNRiz8i3/payment_methods \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe customers list_payment_methods cus_9s6XKzkNRiz8i3 \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

payment_methods = client.v1.customers.payment_methods.list(
  'cus_9s6XKzkNRiz8i3',
  {limit: 3},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

payment_methods = client.v1.customers.payment_methods.list(
  "cus_9s6XKzkNRiz8i3",
  {"limit": 3},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentMethods = $stripe->customers->allPaymentMethods(
  'cus_9s6XKzkNRiz8i3',
  ['limit' => 3]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CustomerPaymentMethodListParams params =
  CustomerPaymentMethodListParams.builder().setLimit(3L).build();

StripeCollection<PaymentMethod> stripeCollection =
  client.v1().customers().paymentMethods().list("cus_9s6XKzkNRiz8i3", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentMethods = await stripe.customers.listPaymentMethods(
  'cus_9s6XKzkNRiz8i3',
  {
    limit: 3,
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CustomerListPaymentMethodsParams{
  Customer: stripe.String("cus_9s6XKzkNRiz8i3"),
}
params.Limit = stripe.Int64(3)
result := sc.V1Customers.ListPaymentMethods(context.TODO(), params)
```

```dotnet
var options = new CustomerPaymentMethodListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Customers.PaymentMethods;
StripeList<PaymentMethod> paymentMethods = service.List(
    "cus_9s6XKzkNRiz8i3",
    options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/customers/cus_9s6XKzkNRiz8i3/payment_methods",
  "has_more": false,
  "data": [
    {
      "id": "pm_1NVChw2eZvKYlo2CHxiM5E2E",
      "object": "payment_method",
      "billing_details": {
        "address": {
          "city": null,
          "country": null,
          "line1": null,
          "line2": null,
          "postal_code": null,
          "state": null
        },
        "email": null,
        "name": null,
        "phone": null
      },
      "card": {
        "brand": "visa",
        "checks": {
          "address_line1_check": null,
          "address_postal_code_check": null,
          "cvc_check": "pass"
        },
        "country": "US",
        "exp_month": 12,
        "exp_year": 2034,
        "fingerprint": "Xt5EWLLDS7FJjR1c",
        "funding": "credit",
        "generated_from": null,
        "last4": "4242",
        "networks": {
          "available": [
            "visa"
          ],
          "preferred": null
        },
        "three_d_secure_usage": {
          "supported": true
        },
        "wallet": null
      },
      "created": 1689682128,
      "customer": "cus_9s6XKzkNRiz8i3",
      "livemode": false,
      "metadata": {},
      "redaction": null,
      "type": "card"
    }
  ]
}
```