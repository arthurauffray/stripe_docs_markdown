# Attach a source

Attaches a Source object to a Customer. The source must be in a chargeable or pending state.

## Returns

Returns the attached Source object.

## Parameters

- `source` (string, required)
  The identifier of the source to be attached.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/customers/cus_9s6XKzkNRiz8i3/sources \
  -u "<<YOUR_SECRET_KEY>>" \
  -d source=src_1NfRGv2eZvKYlo2Cv7NAImBL
```

```cli
stripe payment_sources create cus_9s6XKzkNRiz8i3 \
  --source=src_1NfRGv2eZvKYlo2Cv7NAImBL
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

result = client.v1.customers.payment_sources.create(
  'cus_9s6XKzkNRiz8i3',
  {source: 'src_1NfRGv2eZvKYlo2Cv7NAImBL'},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

payment_source = client.v1.customers.payment_sources.create(
  "cus_9s6XKzkNRiz8i3",
  {"source": "src_1NfRGv2eZvKYlo2Cv7NAImBL"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentSource = $stripe->customers->createSource(
  'cus_9s6XKzkNRiz8i3',
  ['source' => 'src_1NfRGv2eZvKYlo2Cv7NAImBL']
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CustomerPaymentSourceCreateParams params =
  CustomerPaymentSourceCreateParams.builder()
    .setSource("src_1NfRGv2eZvKYlo2Cv7NAImBL")
    .build();

PaymentSource paymentSource =
  client.v1().customers().paymentSources().create("cus_9s6XKzkNRiz8i3", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customerSource = await stripe.customers.createSource(
  'cus_9s6XKzkNRiz8i3',
  {
    source: 'src_1NfRGv2eZvKYlo2Cv7NAImBL',
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PaymentSourceCreateParams{
  Source: stripe.String("src_1NfRGv2eZvKYlo2Cv7NAImBL"),
  Customer: stripe.String("cus_9s6XKzkNRiz8i3"),
}
result, err := sc.V1PaymentSources.Create(context.TODO(), params)
```

```dotnet
var options = new CustomerPaymentSourceCreateOptions
{
    Source = "src_1NfRGv2eZvKYlo2Cv7NAImBL",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Customers.PaymentSources;
IPaymentSource iPaymentSource = service.Create("cus_9s6XKzkNRiz8i3", options);
```

### Response

```json
{
  "id": "src_1NfRGv2eZvKYlo2Cv7NAImBL",
  "object": "source",
  "ach_credit_transfer": {
    "account_number": "test_52796e3294dc",
    "routing_number": "110000000",
    "fingerprint": "ecpwEzmBOSMOqQTL",
    "bank_name": "TEST BANK",
    "swift_code": "TSTEZ122"
  },
  "amount": 1000,
  "client_secret": "src_client_secret_sBqfX18eq6GPfGxGvVfMByCp",
  "created": 1692121393,
  "currency": "usd",
  "customer": "cus_9s6XKzkNRiz8i3",
  "flow": "receiver",
  "livemode": false,
  "metadata": {},
  "owner": {
    "address": null,
    "email": "jenny.rosen@example.com",
    "name": null,
    "phone": null,
    "verified_address": null,
    "verified_email": null,
    "verified_name": null,
    "verified_phone": null
  },
  "receiver": {
    "address": "121042882-38381234567890123",
    "amount_received": 1000,
    "amount_charged": 0,
    "amount_returned": 0,
    "refund_attributes_status": "missing",
    "refund_attributes_method": "email"
  },
  "redaction": null,
  "statement_descriptor": null,
  "status": "chargeable",
  "type": "ach_credit_transfer",
  "usage": "reusable"
}
```