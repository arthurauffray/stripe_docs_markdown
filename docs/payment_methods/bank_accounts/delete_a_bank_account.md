# Delete a bank account

You can delete bank accounts from a Customer.

## Returns

```curl
curl -X DELETE https://api.stripe.com/v1/customers/cus_9s6XKzkNRiz8i3/sources/ba_1NkxyL2eZvKYlo2CwZgb2mzO \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe bank_accounts delete cus_9s6XKzkNRiz8i3 ba_1NkxyL2eZvKYlo2CwZgb2mzO
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

result = client.v1.sources.detach(
  'cus_9s6XKzkNRiz8i3',
  'ba_1NkxyL2eZvKYlo2CwZgb2mzO',
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

payment_source = client.v1.sources.detach(
  "cus_9s6XKzkNRiz8i3",
  "ba_1NkxyL2eZvKYlo2CwZgb2mzO",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentSource = $stripe->customers->deleteSource(
  'cus_9s6XKzkNRiz8i3',
  'ba_1NkxyL2eZvKYlo2CwZgb2mzO',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

SourceDetachParams params = SourceDetachParams.builder().build();

PaymentSource paymentSource =
  client.v1().sources().detach(
    "cus_9s6XKzkNRiz8i3",
    "ba_1NkxyL2eZvKYlo2CwZgb2mzO",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customerSource = await stripe.customers.deleteSource(
  'cus_9s6XKzkNRiz8i3',
  'ba_1NkxyL2eZvKYlo2CwZgb2mzO'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CardDeleteParams{Customer: stripe.String("cus_9s6XKzkNRiz8i3")}
result, err := sc.V1Cards.Delete(
  context.TODO(), "ba_1NkxyL2eZvKYlo2CwZgb2mzO", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Sources;
IPaymentSource iPaymentSource = service.Detach(
    "cus_9s6XKzkNRiz8i3",
    "ba_1NkxyL2eZvKYlo2CwZgb2mzO");
```

### Response

```json
{
  "customer": "cus_9s6XKzkNRiz8i3",
  "id": "ba_1NkxyL2eZvKYlo2CwZgb2mzO",
  "object": "bank_account",
  "deleted": true
}
```