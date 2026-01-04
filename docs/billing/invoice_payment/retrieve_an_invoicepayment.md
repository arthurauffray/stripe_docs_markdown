# Retrieve an InvoicePayment

Retrieves the invoice payment with the given ID.

## Returns

Returns an [invoice_payment](https://docs.stripe.com/docs/api/invoices/payments.md) object if a valid invoice payment ID was provided. Otherwise, this call raises [an error](https://docs.stripe.com/api/invoice-payment/retrieve.md#errors).

```curl
curl https://api.stripe.com/v1/invoice_payments/inpay_1M3USa2eZvKYlo2CBjuwbq0N \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe invoice_payments retrieve inpay_1M3USa2eZvKYlo2CBjuwbq0N
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

invoice_payment = client.v1.invoice_payments.retrieve('inpay_1M3USa2eZvKYlo2CBjuwbq0N')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

invoice_payment = client.v1.invoice_payments.retrieve(
  "inpay_1M3USa2eZvKYlo2CBjuwbq0N",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$invoicePayment = $stripe->invoicePayments->retrieve(
  'inpay_1M3USa2eZvKYlo2CBjuwbq0N',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

InvoicePaymentRetrieveParams params = InvoicePaymentRetrieveParams.builder().build();

InvoicePayment invoicePayment =
  client.v1().invoicePayments().retrieve("inpay_1M3USa2eZvKYlo2CBjuwbq0N", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const invoicePayment = await stripe.invoicePayments.retrieve(
  'inpay_1M3USa2eZvKYlo2CBjuwbq0N'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.InvoicePaymentRetrieveParams{}
result, err := sc.V1InvoicePayments.Retrieve(
  context.TODO(), "inpay_1M3USa2eZvKYlo2CBjuwbq0N", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.InvoicePayments;
InvoicePayment invoicePayment = service.Get("inpay_1M3USa2eZvKYlo2CBjuwbq0N");
```

### Response

```json
{
  "id": "inpay_1M3USa2eZvKYlo2CBjuwbq0N",
  "object": "invoice_payment",
  "amount_paid": 2000,
  "amount_requested": 2000,
  "created": 1391288554,
  "currency": "usd",
  "invoice": "in_103Q0w2eZvKYlo2C5PYwf6Wf",
  "is_default": true,
  "livemode": false,
  "payment": {
    "type": "payment_intent",
    "payment_intent": "pi_103Q0w2eZvKYlo2C364X582Z"
  },
  "status": "paid",
  "status_transitions": {
    "canceled_at": null,
    "paid_at": 1391288554
  }
}
```