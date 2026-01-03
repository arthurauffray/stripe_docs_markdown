# List all PaymentIntent LineItems

Lists all LineItems of a given PaymentIntent.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` line items of the given PaymentIntent, starting after line item `starting_after`. Each entry in the array is a separate line item object. If no other line items are available, the resulting array is empty.

## Parameters

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl https://api.stripe.com/v1/payment_intents/pi_3MtwBwLkdIwHu7ix28a3tqPa/amount_details_line_items \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe payment_intent_amount_details_line_items list pi_3MtwBwLkdIwHu7ix28a3tqPa
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

payment_intent_amount_details_line_items = client.v1.payment_intents.amount_details_line_items.list('pi_3MtwBwLkdIwHu7ix28a3tqPa')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

payment_intent_amount_details_line_items = client \
  .v1 \
  .payment_intents \
  .amount_details_line_items \
  .list("pi_3MtwBwLkdIwHu7ix28a3tqPa")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentIntentAmountDetailsLineItems = $stripe->paymentIntents->allAmountDetailsLineItems(
  'pi_3MtwBwLkdIwHu7ix28a3tqPa',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PaymentIntentAmountDetailsLineItemListParams params =
  PaymentIntentAmountDetailsLineItemListParams.builder().build();

StripeCollection<PaymentIntentAmountDetailsLineItem> stripeCollection =
  client.v1().paymentIntents().amountDetailsLineItems().list(
    "pi_3MtwBwLkdIwHu7ix28a3tqPa",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntentAmountDetailsLineItems = await stripe
  .paymentIntents
  .listAmountDetailsLineItems('pi_3MtwBwLkdIwHu7ix28a3tqPa');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PaymentIntentAmountDetailsLineItemListParams{
  Intent: stripe.String("pi_3MtwBwLkdIwHu7ix28a3tqPa"),
}
result := sc.V1PaymentIntentAmountDetailsLineItems.List(context.TODO(), params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.PaymentIntents.AmountDetailsLineItems;
StripeList<PaymentIntentAmountDetailsLineItem> paymentIntentAmountDetailsLineItems = service
    .List("pi_3MtwBwLkdIwHu7ix28a3tqPa");
```

### Response

```json
{
  "object": "list",
  "url": "/v1/payment_intents/pi_3MtwBwLkdIwHu7ix28a3tqPa/amount_details_line_items",
  "has_more": false,
  "data": [
    {
      "id": "uli_T1KmwLEvkprqQb",
      "object": "payment_intent_amount_details_line_item",
      "discount_amount": 50,
      "payment_method_options": null,
      "product_code": "SKU001",
      "product_name": "Product 001",
      "quantity": 1,
      "tax": {
        "total_tax_amount": 20
      },
      "unit_cost": 2000,
      "unit_of_measure": "each"
    }
  ]
}
```