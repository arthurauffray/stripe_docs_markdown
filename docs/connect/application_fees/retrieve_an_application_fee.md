# Retrieve an application fee

Retrieves the details of an application fee that your account has collected. The same information is returned when refunding the application fee.

## Returns

Returns an application fee object if a valid identifier was provided, and raises [an error](https://docs.stripe.com/api/application_fees/retrieve.md#errors) otherwise.

```curl
curl https://api.stripe.com/v1/application_fees/fee_1B73DOKbnvuxQXGuhY8Aw0TN \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe application_fees retrieve fee_1B73DOKbnvuxQXGuhY8Aw0TN
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

application_fee = client.v1.application_fees.retrieve('fee_1B73DOKbnvuxQXGuhY8Aw0TN')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

application_fee = client.v1.application_fees.retrieve("fee_1B73DOKbnvuxQXGuhY8Aw0TN")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$applicationFee = $stripe->applicationFees->retrieve(
  'fee_1B73DOKbnvuxQXGuhY8Aw0TN',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ApplicationFeeRetrieveParams params = ApplicationFeeRetrieveParams.builder().build();

ApplicationFee applicationFee =
  client.v1().applicationFees().retrieve("fee_1B73DOKbnvuxQXGuhY8Aw0TN", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const applicationFee = await stripe.applicationFees.retrieve(
  'fee_1B73DOKbnvuxQXGuhY8Aw0TN'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.ApplicationFeeRetrieveParams{}
result, err := sc.V1ApplicationFees.Retrieve(
  context.TODO(), "fee_1B73DOKbnvuxQXGuhY8Aw0TN", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.ApplicationFees;
ApplicationFee applicationFee = service.Get("fee_1B73DOKbnvuxQXGuhY8Aw0TN");
```

### Response

```json
{
  "id": "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
  "object": "application_fee",
  "account": "acct_164wxjKbnvuxQXGu",
  "amount": 105,
  "amount_refunded": 105,
  "application": "ca_32D88BD1qLklliziD7gYQvctJIhWBSQ7",
  "balance_transaction": "txn_1032HU2eZvKYlo2CEPtcnUvl",
  "charge": "ch_1B73DOKbnvuxQXGurbwPqzsu",
  "created": 1506609734,
  "currency": "gbp",
  "livemode": false,
  "originating_transaction": null,
  "refunded": true,
  "refunds": {
    "object": "list",
    "data": [
      {
        "id": "fr_1MBoU0KbnvuxQXGu2wCCz4Bb",
        "object": "fee_refund",
        "amount": 38,
        "balance_transaction": null,
        "created": 1670284441,
        "currency": "usd",
        "fee": "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
        "metadata": {}
      },
      {
        "id": "fr_D0s7fGBKB40Twy",
        "object": "fee_refund",
        "amount": 100,
        "balance_transaction": "txn_1CaqNg2eZvKYlo2C75cA3Euk",
        "created": 1528486576,
        "currency": "usd",
        "fee": "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
        "metadata": {}
      }
    ],
    "has_more": false,
    "url": "/v1/application_fees/fee_1B73DOKbnvuxQXGuhY8Aw0TN/refunds"
  },
  "fee_source": {
    "charge": "ch_1B73DOKbnvuxQXGurbwPqzsu",
    "type": "charge"
  }
}
```