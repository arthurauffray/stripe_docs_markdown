# Verify a bank account

Verify a specified bank account for a given customer.

## Returns

## Parameters

- `amounts` (array of integers, optional)
  Two positive integers, in *cents*, equal to the values of the microdeposits sent to the bank account.

```curl
curl https://api.stripe.com/v1/customers/cus_9s6XGDTHzA66Po/sources/ba_1NAiwl2eZvKYlo2CRdCLZSxO/verify \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "amounts[]"=32 \
  -d "amounts[]"=45
```

```cli
stripe bank_accounts verify cus_9s6XGDTHzA66Po ba_1NAiwl2eZvKYlo2CRdCLZSxO \
  -d "amounts[0]"=32 \
  -d "amounts[1]"=45
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

bank_account = client.v1.customers.payment_sources.verify(
  'cus_9s6XGDTHzA66Po',
  'ba_1NAiwl2eZvKYlo2CRdCLZSxO',
  {amounts: [32, 45]},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentSource = $stripe->customers->verifySource(
  'cus_9s6XGDTHzA66Po',
  'ba_1NAiwl2eZvKYlo2CRdCLZSxO',
  ['amounts' => [32, 45]]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CustomerPaymentSourceVerifyParams params =
  CustomerPaymentSourceVerifyParams.builder().addAmount(32L).addAmount(45L).build();

BankAccount bankAccount =
  client.v1().customers().paymentSources().verify(
    "cus_9s6XGDTHzA66Po",
    "ba_1NAiwl2eZvKYlo2CRdCLZSxO",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const bankAccount = await stripe.customers.verifySource(
  'cus_9s6XGDTHzA66Po',
  'ba_1NAiwl2eZvKYlo2CRdCLZSxO',
  {
    amounts: [32, 45],
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PaymentSourceVerifyParams{
  Amounts: []*int64{stripe.Int64(32), stripe.Int64(45)},
  Customer: stripe.String("cus_9s6XGDTHzA66Po"),
}
result, err := sc.V1PaymentSources.Verify(
  context.TODO(), "ba_1NAiwl2eZvKYlo2CRdCLZSxO", params)
```

```dotnet
var options = new CustomerPaymentSourceVerifyOptions
{
    Amounts = new List<long?> { 32, 45 },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Customers.PaymentSources;
BankAccount bankAccount = service.Verify(
    "cus_9s6XGDTHzA66Po",
    "ba_1NAiwl2eZvKYlo2CRdCLZSxO",
    options);
```

### Response

```json
{
  "id": "ba_1NAiwl2eZvKYlo2CRdCLZSxO",
  "object": "bank_account",
  "account_holder_name": "Jane Austen",
  "account_holder_type": "company",
  "account_type": null,
  "bank_name": "STRIPE TEST BANK",
  "country": "US",
  "currency": "usd",
  "customer": "cus_9s6XGDTHzA66Po",
  "fingerprint": "1JWtPxqbdX5Gamtc",
  "last4": "6789",
  "metadata": {},
  "routing_number": "110000000",
  "status": "new",
  "name": "Jenny Rosen"
}
```