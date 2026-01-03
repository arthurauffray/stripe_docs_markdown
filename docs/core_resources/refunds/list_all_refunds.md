# List all refunds

Returns a list of all refunds you created. We return the refunds in sorted order, with the most recent refunds appearing first. The 10 most recent refunds are always available by default on the Charge object.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` refunds, starting after the `starting_after` refund. Each entry in the array is a separate Refund object. If no other refunds are available, the resulting array is empty. If you provide a non-existent charge ID, this call raises [an error](https://docs.stripe.com/api/refunds/list.md#errors).

## Parameters

- `charge` (string, optional)
  Only return refunds for the charge specified by this charge ID.

- `created` (object, optional)
  Only return refunds that were created during the given date interval.

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

- `payment_intent` (string, optional)
  Only return refunds for the PaymentIntent specified by this ID.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/refunds \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe refunds list  \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

refunds = client.v1.refunds.list({limit: 3})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

refunds = client.v1.refunds.list({"limit": 3})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$refunds = $stripe->refunds->all(['limit' => 3]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

RefundListParams params = RefundListParams.builder().setLimit(3L).build();

StripeCollection<Refund> stripeCollection = client.v1().refunds().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const refunds = await stripe.refunds.list({
  limit: 3,
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.RefundListParams{}
params.Limit = stripe.Int64(3)
result := sc.V1Refunds.List(context.TODO(), params)
```

```dotnet
var options = new RefundListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Refunds;
StripeList<Refund> refunds = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/refunds",
  "has_more": false,
  "data": [
    {
      "id": "re_1Nispe2eZvKYlo2Cd31jOCgZ",
      "object": "refund",
      "amount": 1000,
      "balance_transaction": "txn_1Nispe2eZvKYlo2CYezqFhEx",
      "charge": "ch_1NirD82eZvKYlo2CIvbtLWuY",
      "created": 1692942318,
      "currency": "usd",
      "destination_details": {
        "card": {
          "reference": "123456789012",
          "reference_status": "available",
          "reference_type": "acquirer_reference_number",
          "type": "refund"
        },
        "type": "card"
      },
      "metadata": {},
      "payment_intent": "pi_1GszsK2eZvKYlo2CfhZyoZLp",
      "reason": null,
      "receipt_number": null,
      "source_transfer_reversal": null,
      "status": "succeeded",
      "transfer_reversal": null
    }
  ]
}
```