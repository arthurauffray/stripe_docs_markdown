# Retrieve an invoice rendering template

Retrieves an invoice rendering template with the given ID. It by default returns the latest version of the template. Optionally, specify a version to see previous versions.

## Returns

Returns an [invoice_payment](https://docs.stripe.com/docs/api/invoices/payments.md) object if a valid invoice payment ID and matching invoice ID were provided. Otherwise, this call raises [an error](https://docs.stripe.com/api/invoice-rendering-template/retrieve.md#errors).

```curl
curl https://api.stripe.com/v1/invoice_rendering_templates/inrtem_abc \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe invoice_rendering_templates retrieve inrtem_abc
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

invoice_rendering_template = client.v1.invoice_rendering_templates.retrieve('inrtem_abc')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

invoice_rendering_template = client.v1.invoice_rendering_templates.retrieve(
  "inrtem_abc",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$invoiceRenderingTemplate = $stripe->invoiceRenderingTemplates->retrieve(
  'inrtem_abc',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

InvoiceRenderingTemplateRetrieveParams params =
  InvoiceRenderingTemplateRetrieveParams.builder().build();

InvoiceRenderingTemplate invoiceRenderingTemplate =
  client.v1().invoiceRenderingTemplates().retrieve("inrtem_abc", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const invoiceRenderingTemplate = await stripe.invoiceRenderingTemplates.retrieve(
  'inrtem_abc'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.InvoiceRenderingTemplateRetrieveParams{}
result, err := sc.V1InvoiceRenderingTemplates.Retrieve(
  context.TODO(), "inrtem_abc", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.InvoiceRenderingTemplates;
InvoiceRenderingTemplate invoiceRenderingTemplate = service.Get("inrtem_abc");
```

### Response

```json
{
  "id": "inrtem_abc",
  "object": "invoice_rendering_template",
  "nickname": "My Invoice Template",
  "status": "active",
  "version": 1,
  "created": 1678942624,
  "livemode": false
}
```