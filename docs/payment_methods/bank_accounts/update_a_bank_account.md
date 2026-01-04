# Update a bank account

Updates the `account_holder_name`, `account_holder_type`, and `metadata` of a bank account belonging to a customer. Other bank account details are not editable, by design.

## Returns

Returns the bank account object.

## Parameters

- `account_holder_name` (string, optional)
  The name of the person or business that owns the bank account.

- `account_holder_type` (string, optional)
  The type of entity that holds the account. This can be either `individual` or `company`.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/customers/cus_9s6XI9OFIdpjIg/sources/ba_1MvoIJ2eZvKYlo2CO9f0MabO \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
```

```cli
stripe bank_accounts update cus_9s6XI9OFIdpjIg ba_1MvoIJ2eZvKYlo2CO9f0MabO \
  -d "metadata[order_id]"=6735
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

result = client.v1.customers.payment_sources.update(
  'cus_9s6XI9OFIdpjIg',
  'ba_1MvoIJ2eZvKYlo2CO9f0MabO',
  {metadata: {order_id: '6735'}},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

payment_source = client.v1.customers.payment_sources.update(
  "cus_9s6XI9OFIdpjIg",
  "ba_1MvoIJ2eZvKYlo2CO9f0MabO",
  {"metadata": {"order_id": "6735"}},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentSource = $stripe->customers->updateSource(
  'cus_9s6XI9OFIdpjIg',
  'ba_1MvoIJ2eZvKYlo2CO9f0MabO',
  ['metadata' => ['order_id' => '6735']]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CustomerPaymentSourceUpdateParams params =
  CustomerPaymentSourceUpdateParams.builder()
    .putMetadata("order_id", "6735")
    .build();

PaymentSource paymentSource =
  client.v1().customers().paymentSources().update(
    "cus_9s6XI9OFIdpjIg",
    "ba_1MvoIJ2eZvKYlo2CO9f0MabO",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customerSource = await stripe.customers.updateSource(
  'cus_9s6XI9OFIdpjIg',
  'ba_1MvoIJ2eZvKYlo2CO9f0MabO',
  {
    metadata: {
      order_id: '6735',
    },
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CardUpdateParams{Customer: stripe.String("cus_9s6XI9OFIdpjIg")}
params.AddMetadata("order_id", "6735")
result, err := sc.V1Cards.Update(
  context.TODO(), "ba_1MvoIJ2eZvKYlo2CO9f0MabO", params)
```

```dotnet
var options = new CustomerPaymentSourceUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Customers.PaymentSources;
IPaymentSource iPaymentSource = service.Update(
    "cus_9s6XI9OFIdpjIg",
    "ba_1MvoIJ2eZvKYlo2CO9f0MabO",
    options);
```

### Response

```json
{
  "id": "ba_1MvoIJ2eZvKYlo2CO9f0MabO",
  "object": "bank_account",
  "account_holder_name": "Jane Austen",
  "account_holder_type": "company",
  "account_type": null,
  "bank_name": "STRIPE TEST BANK",
  "country": "US",
  "currency": "usd",
  "customer": "cus_9s6XI9OFIdpjIg",
  "fingerprint": "1JWtPxqbdX5Gamtc",
  "last4": "6789",
  "metadata": {
    "order_id": "6735"
  },
  "routing_number": "110000000",
  "status": "new"
}
```