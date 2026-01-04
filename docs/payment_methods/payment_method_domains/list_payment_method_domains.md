# List payment method domains

Lists the details of existing payment method domains.

## Returns

Returns a list of payment method domain objects.

## Parameters

- `domain_name` (string, optional)
  The domain name that this payment method domain object represents.

- `enabled` (boolean, optional)
  Whether this payment method domain is enabled. If the domain is not enabled, payment methods will not appear in Elements or Embedded Checkout

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/payment_method_domains \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe payment_method_domains list  \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

payment_method_domains = client.v1.payment_method_domains.list({limit: 3})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

payment_method_domains = client.v1.payment_method_domains.list({"limit": 3})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentMethodDomains = $stripe->paymentMethodDomains->all(['limit' => 3]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PaymentMethodDomainListParams params =
  PaymentMethodDomainListParams.builder().setLimit(3L).build();

StripeCollection<PaymentMethodDomain> stripeCollection =
  client.v1().paymentMethodDomains().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentMethodDomains = await stripe.paymentMethodDomains.list({
  limit: 3,
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PaymentMethodDomainListParams{}
params.Limit = stripe.Int64(3)
result := sc.V1PaymentMethodDomains.List(context.TODO(), params)
```

```dotnet
var options = new PaymentMethodDomainListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.PaymentMethodDomains;
StripeList<PaymentMethodDomain> paymentMethodDomains = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/payment_method_domains",
  "has_more": false,
  "data": [
    {
      "id": "pmd_1Nnrer2eZvKYlo2Cips79tWl",
      "object": "payment_method_domain",
      "apple_pay": {
        "status": "active"
      },
      "created": 1694129445,
      "domain_name": "example.com",
      "enabled": true,
      "google_pay": {
        "status": "active"
      },
      "link": {
        "status": "active"
      },
      "livemode": false,
      "paypal": {
        "status": "active"
      }
    }
  ]
}
```