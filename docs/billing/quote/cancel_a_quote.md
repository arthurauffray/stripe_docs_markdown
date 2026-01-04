# Cancel a quote

Cancels the quote.

## Returns

Returns a canceled quote. Raises [an error](https://docs.stripe.com/api/quotes/cancel.md#errors) otherwise.

```curl
curl -X POST https://api.stripe.com/v1/quotes/qt_1Mr7ZYLkdIwHu7ixvsdZr97I/cancel \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe quotes cancel qt_1Mr7ZYLkdIwHu7ixvsdZr97I
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

quote = client.v1.quotes.cancel('qt_1Mr7ZYLkdIwHu7ixvsdZr97I')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

quote = client.v1.quotes.cancel("qt_1Mr7ZYLkdIwHu7ixvsdZr97I")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$quote = $stripe->quotes->cancel('qt_1Mr7ZYLkdIwHu7ixvsdZr97I', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

QuoteCancelParams params = QuoteCancelParams.builder().build();

Quote quote = client.v1().quotes().cancel("qt_1Mr7ZYLkdIwHu7ixvsdZr97I", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const quote = await stripe.quotes.cancel('qt_1Mr7ZYLkdIwHu7ixvsdZr97I');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.QuoteCancelParams{}
result, err := sc.V1Quotes.Cancel(
  context.TODO(), "qt_1Mr7ZYLkdIwHu7ixvsdZr97I", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Quotes;
Quote quote = service.Cancel("qt_1Mr7ZYLkdIwHu7ixvsdZr97I");
```

### Response

```json
{
  "id": "qt_1Mr7ZYLkdIwHu7ixvsdZr97I",
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
  "created": 1680129268,
  "currency": "usd",
  "customer": "cus_NcMIIkPfQZQEHR",
  "default_tax_rates": [],
  "description": null,
  "discounts": [],
  "expires_at": 1682721268,
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
  "number": "QT-FF4741D9-0001-1",
  "on_behalf_of": null,
  "status": "canceled",
  "status_transitions": {
    "accepted_at": null,
    "canceled_at": 1680129269,
    "finalized_at": 1680129269
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