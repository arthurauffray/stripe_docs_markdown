# Retrieve a quote

Retrieves the quote with the given ID.

## Returns

Returns a quote if a valid quote ID was provided. Raises [an error](https://docs.stripe.com/api/quotes/retrieve.md#errors) otherwise.

```curl
curl https://api.stripe.com/v1/quotes/qt_1Mr7wVLkdIwHu7ixJYSiPTGq \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe quotes retrieve qt_1Mr7wVLkdIwHu7ixJYSiPTGq
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

quote = client.v1.quotes.retrieve('qt_1Mr7wVLkdIwHu7ixJYSiPTGq')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

quote = client.v1.quotes.retrieve("qt_1Mr7wVLkdIwHu7ixJYSiPTGq")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$quote = $stripe->quotes->retrieve('qt_1Mr7wVLkdIwHu7ixJYSiPTGq', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

QuoteRetrieveParams params = QuoteRetrieveParams.builder().build();

Quote quote = client.v1().quotes().retrieve("qt_1Mr7wVLkdIwHu7ixJYSiPTGq", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const quote = await stripe.quotes.retrieve('qt_1Mr7wVLkdIwHu7ixJYSiPTGq');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.QuoteRetrieveParams{}
result, err := sc.V1Quotes.Retrieve(
  context.TODO(), "qt_1Mr7wVLkdIwHu7ixJYSiPTGq", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Quotes;
Quote quote = service.Get("qt_1Mr7wVLkdIwHu7ixJYSiPTGq");
```

### Response

```json
{
  "id": "qt_1Mr7wVLkdIwHu7ixJYSiPTGq",
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
  "created": 1680130691,
  "currency": "usd",
  "customer": "cus_NcMfB0SSFHINCV",
  "default_tax_rates": [],
  "description": null,
  "discounts": [],
  "expires_at": 1682722691,
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
  "number": null,
  "on_behalf_of": null,
  "status": "draft",
  "status_transitions": {
    "accepted_at": null,
    "canceled_at": null,
    "finalized_at": null
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
```