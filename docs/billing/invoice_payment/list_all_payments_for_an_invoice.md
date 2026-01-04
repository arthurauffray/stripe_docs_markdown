# List all payments for an invoice

When retrieving an invoice, there is an includable payments property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of payments.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` invoice payments, starting after invoice payment `starting_after`. Each entry in the array is a separate [invoice_payment object](https://docs.stripe.com/docs/api/invoices/payments.md). If no more invoice payments are available, the resulting array will be empty.

## Parameters

- `created` (object, optional)
  Only return invoice payments that were created during the given date interval.

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

- `invoice` (string, optional)
  The identifier of the invoice whose payments to return.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `payment` (object, optional)
  The payment details of the invoice payments to return.

  - `payment.type` (enum, required)
    Only return invoice payments associated by this payment type.
Possible enum values:
    - `payment_intent`
      Indicates that a `PaymentIntent` object is being associated with this invoice payment.

    - `payment_record`
      Indicates that an `PaymentRecord` object is being associated with this invoice payment.

  - `payment.payment_intent` (string, optional)
    Only return invoice payments associated by this payment intent ID.

  - `payment.payment_record` (string, optional)
    Only return invoice payments associated by this payment record ID.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `status` (enum, optional)
  The status of the invoice payments to return.
Possible enum values:
  - `canceled`
    The payment has been canceled; it will not be credited to the invoice.

  - `open`
    The payment is incomplete and isn’t credited to the invoice. More fine-grained information available on the payment intent

  - `paid`
    The payment is complete and has been credited to the invoice.

```curl
curl -G https://api.stripe.com/v1/invoice_payments \
  -u "<<YOUR_SECRET_KEY>>" \
  -d invoice=in_103Q0w2eZvKYlo2C5PYwf6Wf
```

```cli
stripe invoice_payments list  \
  --invoice=in_103Q0w2eZvKYlo2C5PYwf6Wf
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

invoice_payments = client.v1.invoice_payments.list({
  invoice: 'in_103Q0w2eZvKYlo2C5PYwf6Wf',
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

invoice_payments = client.v1.invoice_payments.list({
  "invoice": "in_103Q0w2eZvKYlo2C5PYwf6Wf",
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$invoicePayments = $stripe->invoicePayments->all([
  'invoice' => 'in_103Q0w2eZvKYlo2C5PYwf6Wf',
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

InvoicePaymentListParams params =
  InvoicePaymentListParams.builder()
    .setInvoice("in_103Q0w2eZvKYlo2C5PYwf6Wf")
    .build();

StripeCollection<InvoicePayment> stripeCollection =
  client.v1().invoicePayments().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const invoicePayments = await stripe.invoicePayments.list({
  invoice: 'in_103Q0w2eZvKYlo2C5PYwf6Wf',
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.InvoicePaymentListParams{
  Invoice: stripe.String("in_103Q0w2eZvKYlo2C5PYwf6Wf"),
}
result := sc.V1InvoicePayments.List(context.TODO(), params)
```

```dotnet
var options = new InvoicePaymentListOptions
{
    Invoice = "in_103Q0w2eZvKYlo2C5PYwf6Wf",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.InvoicePayments;
StripeList<InvoicePayment> invoicePayments = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/invoice_payments",
  "has_more": false,
  "data": [
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
  ]
}
```