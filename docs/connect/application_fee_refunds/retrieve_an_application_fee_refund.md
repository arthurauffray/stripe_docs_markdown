# Retrieve an application fee refund

By default, you can see the 10 most recent refunds stored directly on the application fee object, but you can also retrieve details about a specific refund stored on the application fee.

## Returns

Returns the application fee refund object.

```curl
curl https://api.stripe.com/v1/application_fees/fee_1B73DOKbnvuxQXGuhY8Aw0TN/refunds/fr_1MtJRpKbnvuxQXGuM6Ww0D24 \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe fee_refunds retrieve fee_1B73DOKbnvuxQXGuhY8Aw0TN fr_1MtJRpKbnvuxQXGuM6Ww0D24
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

application_fee_refund = client.v1.application_fees.refunds.retrieve(
  'fee_1B73DOKbnvuxQXGuhY8Aw0TN',
  'fr_1MtJRpKbnvuxQXGuM6Ww0D24',
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

application_fee_refund = client.v1.application_fees.refunds.retrieve(
  "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
  "fr_1MtJRpKbnvuxQXGuM6Ww0D24",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$applicationFeeRefund = $stripe->applicationFees->retrieveRefund(
  'fee_1B73DOKbnvuxQXGuhY8Aw0TN',
  'fr_1MtJRpKbnvuxQXGuM6Ww0D24',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ApplicationFeeRefundRetrieveParams params =
  ApplicationFeeRefundRetrieveParams.builder().build();

FeeRefund feeRefund =
  client.v1().applicationFees().refunds().retrieve(
    "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
    "fr_1MtJRpKbnvuxQXGuM6Ww0D24",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const feeRefund = await stripe.applicationFees.retrieveRefund(
  'fee_1B73DOKbnvuxQXGuhY8Aw0TN',
  'fr_1MtJRpKbnvuxQXGuM6Ww0D24'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.FeeRefundRetrieveParams{
  Fee: stripe.String("fee_1B73DOKbnvuxQXGuhY8Aw0TN"),
}
result, err := sc.V1FeeRefunds.Retrieve(
  context.TODO(), "fr_1MtJRpKbnvuxQXGuM6Ww0D24", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.ApplicationFees.Refunds;
ApplicationFeeRefund applicationFeeRefund = service.Get(
    "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
    "fr_1MtJRpKbnvuxQXGuM6Ww0D24");
```

### Response

```json
{
  "id": "fr_1MtJRpKbnvuxQXGuM6Ww0D24",
  "object": "fee_refund",
  "amount": 100,
  "balance_transaction": null,
  "created": 1680651573,
  "currency": "usd",
  "fee": "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
  "metadata": {}
}
```