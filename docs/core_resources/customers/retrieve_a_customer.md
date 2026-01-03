# Retrieve a customer

Retrieves a Customer object.

## Returns

Returns the Customer object for a valid identifier. If it’s for a deleted Customer, a subset of the customer’s information is returned, including a `deleted` property that’s set to true.

```curl
curl https://api.stripe.com/v1/customers/cus_NffrFeUfNV2Hib \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe customers retrieve cus_NffrFeUfNV2Hib
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

customer = client.v1.customers.retrieve('cus_NffrFeUfNV2Hib')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

customer = client.v1.customers.retrieve("cus_NffrFeUfNV2Hib")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$customer = $stripe->customers->retrieve('cus_NffrFeUfNV2Hib', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CustomerRetrieveParams params = CustomerRetrieveParams.builder().build();

Customer customer = client.v1().customers().retrieve("cus_NffrFeUfNV2Hib", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customer = await stripe.customers.retrieve('cus_NffrFeUfNV2Hib');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CustomerRetrieveParams{}
result, err := sc.V1Customers.Retrieve(context.TODO(), "cus_NffrFeUfNV2Hib", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Customers;
Customer customer = service.Get("cus_NffrFeUfNV2Hib");
```

### Response

```json
{
  "id": "cus_NffrFeUfNV2Hib",
  "object": "customer",
  "address": null,
  "balance": 0,
  "created": 1680893993,
  "currency": null,
  "default_source": null,
  "delinquent": false,
  "description": null,
  "email": "jennyrosen@example.com",
  "invoice_prefix": "0759376C",
  "invoice_settings": {
    "custom_fields": null,
    "default_payment_method": null,
    "footer": null,
    "rendering_options": null
  },
  "livemode": false,
  "metadata": {},
  "name": "Jenny Rosen",
  "next_invoice_sequence": 1,
  "phone": null,
  "preferred_locales": [],
  "shipping": null,
  "tax_exempt": "none",
  "test_clock": null
}
```