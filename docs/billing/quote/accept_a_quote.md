# Accept a quote

Accepts the specified quote.

## Returns

Returns an accepted quote and creates an invoice, subscription or subscription schedule. Raises [an error](https://docs.stripe.com/api/quotes/accept.md#errors) otherwise.

```curl
curl -X POST https://api.stripe.com/v1/quotes/qt_1Mr7YsLkdIwHu7ixoRgFs97D/accept \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe quotes accept qt_1Mr7YsLkdIwHu7ixoRgFs97D
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

quote = client.v1.quotes.accept('qt_1Mr7YsLkdIwHu7ixoRgFs97D')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

quote = client.v1.quotes.accept("qt_1Mr7YsLkdIwHu7ixoRgFs97D")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$quote = $stripe->quotes->accept('qt_1Mr7YsLkdIwHu7ixoRgFs97D', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

QuoteAcceptParams params = QuoteAcceptParams.builder().build();

Quote quote = client.v1().quotes().accept("qt_1Mr7YsLkdIwHu7ixoRgFs97D", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const quote = await stripe.quotes.accept('qt_1Mr7YsLkdIwHu7ixoRgFs97D');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.QuoteAcceptParams{}
result, err := sc.V1Quotes.Accept(
  context.TODO(), "qt_1Mr7YsLkdIwHu7ixoRgFs97D", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Quotes;
Quote quote = service.Accept("qt_1Mr7YsLkdIwHu7ixoRgFs97D");
```

### Response

```json
{
  "id": "qt_1Mr7YsLkdIwHu7ixoRgFs97D",
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
  "created": 1680129226,
  "currency": "usd",
  "customer": "cus_NcMHflMGStIAoB",
  "default_tax_rates": [],
  "description": null,
  "discounts": [],
  "expires_at": 1682721226,
  "footer": null,
  "from_quote": null,
  "header": null,
  "invoice": "in_1Mr7YtLkdIwHu7ixzgJJpJ3L",
  "invoice_settings": {
    "days_until_due": null,
    "issuer": {
      "type": "self"
    }
  },
  "livemode": false,
  "metadata": {},
  "number": "QT-7F68F7D2-0001-1",
  "on_behalf_of": null,
  "status": "accepted",
  "status_transitions": {
    "accepted_at": 1680129227,
    "canceled_at": null,
    "finalized_at": 1680129227
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