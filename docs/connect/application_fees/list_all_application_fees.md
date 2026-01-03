# List all application fees

Returns a list of application fees you’ve previously collected. The application fees are returned in sorted order, with the most recent fees appearing first.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` application fees, starting after application fee `starting_after`. Each entry in the array is a separate application fee object. If no more fees are available, the resulting array will be empty.

## Parameters

- `charge` (string, optional)
  Only return application fees for the charge specified by this charge ID.

- `created` (object, optional)
  Only return applications fees that were created during the given date interval.

  - `created.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `created.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `created.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `created.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/application_fees \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe application_fees list  \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

application_fees = client.v1.application_fees.list({limit: 3})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

application_fees = client.v1.application_fees.list({"limit": 3})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$applicationFees = $stripe->applicationFees->all(['limit' => 3]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ApplicationFeeListParams params =
  ApplicationFeeListParams.builder().setLimit(3L).build();

StripeCollection<ApplicationFee> stripeCollection =
  client.v1().applicationFees().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const applicationFees = await stripe.applicationFees.list({
  limit: 3,
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.ApplicationFeeListParams{}
params.Limit = stripe.Int64(3)
result := sc.V1ApplicationFees.List(context.TODO(), params)
```

```dotnet
var options = new ApplicationFeeListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.ApplicationFees;
StripeList<ApplicationFee> applicationFees = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/application_fees",
  "has_more": false,
  "data": [
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
  ]
}
```