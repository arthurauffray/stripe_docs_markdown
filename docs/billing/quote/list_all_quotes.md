# List all quotes

Returns a list of your quotes.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` quotes, starting after quote `starting_after`. Each entry in the array is a separate quote object. If no more quotes are available, the resulting array will be empty.

## Parameters

- `customer` (string, optional)
  The ID of the customer whose quotes you’re retrieving.

- `customer_account` (string, optional)
  The ID of the account representing the customer whose quotes you’re retrieving.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `status` (enum, optional)
  The status of the quote.

- `test_clock` (string, optional)
  Provides a list of quotes that are associated with the specified test clock. The response will not include quotes with test clocks if this and the customer parameter is not set.

```curl
curl -G https://api.stripe.com/v1/quotes \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe quotes list  \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

quotes = client.v1.quotes.list({limit: 3})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

quotes = client.v1.quotes.list({"limit": 3})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$quotes = $stripe->quotes->all(['limit' => 3]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

QuoteListParams params = QuoteListParams.builder().setLimit(3L).build();

StripeCollection<Quote> stripeCollection = client.v1().quotes().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const quotes = await stripe.quotes.list({
  limit: 3,
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.QuoteListParams{}
params.Limit = stripe.Int64(3)
result := sc.V1Quotes.List(context.TODO(), params)
```

```dotnet
var options = new QuoteListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Quotes;
StripeList<Quote> quotes = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/quotes",
  "has_more": false,
  "data": [
    {
      "id": "qt_1Mr7SqLkdIwHu7ixpI1ClZ6z",
      "object": "quote",
      "amount_subtotal": 2198,
      "amount_total": 2198,
      "application": null,
      "application_fee_amount": null,
      "application_fee_percent": null,
      "automatic_tax": {
        "enabled": false,
        "liability": null,
        "status": null
      },
      "collection_method": "charge_automatically",
      "computed": {
        "recurring": null,
        "upfront": {
          "amount_subtotal": 2198,
          "amount_total": 2198,
          "total_details": {
            "amount_discount": 0,
            "amount_shipping": 0,
            "amount_tax": 0
          }
        }
      },
      "created": 1680128852,
      "currency": "usd",
      "customer": "cus_NcMBZUWCIOEgEW",
      "default_tax_rates": [],
      "description": null,
      "discounts": [],
      "expires_at": 1682720852,
      "footer": null,
      "from_quote": null,
      "header": null,
      "invoice": null,
      "invoice_settings": {
        "days_until_due": null,
        "issuer": {
          "type": "self"
        }
      },
      "livemode": false,
      "metadata": {},
      "number": "QT-5B9DA057-0001-1",
      "on_behalf_of": null,
      "status": "open",
      "status_transitions": {
        "accepted_at": null,
        "canceled_at": null,
        "finalized_at": 1680128853
      },
      "subscription": null,
      "subscription_data": {
        "description": null,
        "effective_date": null,
        "trial_period_days": null
      },
      "subscription_schedule": null,
      "test_clock": null,
      "total_details": {
        "amount_discount": 0,
        "amount_shipping": 0,
        "amount_tax": 0
      },
      "transfer_data": null
    }
  ]
}
```