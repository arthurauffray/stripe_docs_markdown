# Finalize a quote

Finalizes the quote.

## Returns

Returns an open quote. Raises [an error](https://docs.stripe.com/api/quotes/finalize.md#errors) otherwise.

## Parameters

- `expires_at` (timestamp, optional)
  A future timestamp on which the quote will be canceled if in `open` or `draft` status. Measured in seconds since the Unix epoch.

```curl
curl -X POST https://api.stripe.com/v1/quotes/qt_1Mr7SqLkdIwHu7ixpI1ClZ6z/finalize \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe quotes finalize_quote qt_1Mr7SqLkdIwHu7ixpI1ClZ6z
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

quote = client.v1.quotes.finalize_quote('qt_1Mr7SqLkdIwHu7ixpI1ClZ6z')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

quote = client.v1.quotes.finalize_quote("qt_1Mr7SqLkdIwHu7ixpI1ClZ6z")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$quote = $stripe->quotes->finalizeQuote('qt_1Mr7SqLkdIwHu7ixpI1ClZ6z', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

QuoteFinalizeQuoteParams params = QuoteFinalizeQuoteParams.builder().build();

Quote quote =
  client.v1().quotes().finalizeQuote("qt_1Mr7SqLkdIwHu7ixpI1ClZ6z", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const quote = await stripe.quotes.finalizeQuote('qt_1Mr7SqLkdIwHu7ixpI1ClZ6z');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.QuoteFinalizeQuoteParams{}
result, err := sc.V1Quotes.FinalizeQuote(
  context.TODO(), "qt_1Mr7SqLkdIwHu7ixpI1ClZ6z", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Quotes;
Quote quote = service.FinalizeQuote("qt_1Mr7SqLkdIwHu7ixpI1ClZ6z");
```

### Response

```json
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
```