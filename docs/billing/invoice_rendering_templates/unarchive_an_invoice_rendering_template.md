# Unarchive an invoice rendering template

Unarchive an invoice rendering template so it can be used on new Stripe objects again.

## Returns

The updated template object is returned if successful. Otherwise, this call raises [an error](https://docs.stripe.com/api/invoice-rendering-template/unarchive.md#errors).

```curl
curl -X POST https://api.stripe.com/v1/invoice_rendering_templates/inrtem_abc/unarchive \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe invoice_rendering_templates unarchive inrtem_abc
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

invoice_rendering_template = client.v1.invoice_rendering_templates.unarchive('inrtem_abc')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

invoice_rendering_template = client.v1.invoice_rendering_templates.unarchive(
  "inrtem_abc",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$invoiceRenderingTemplate = $stripe->invoiceRenderingTemplates->unarchive(
  'inrtem_abc',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

InvoiceRenderingTemplateUnarchiveParams params =
  InvoiceRenderingTemplateUnarchiveParams.builder().build();

InvoiceRenderingTemplate invoiceRenderingTemplate =
  client.v1().invoiceRenderingTemplates().unarchive("inrtem_abc", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const invoiceRenderingTemplate = await stripe.invoiceRenderingTemplates.unarchive(
  'inrtem_abc'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.InvoiceRenderingTemplateUnarchiveParams{}
result, err := sc.V1InvoiceRenderingTemplates.Unarchive(
  context.TODO(), "inrtem_abc", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.InvoiceRenderingTemplates;
InvoiceRenderingTemplate invoiceRenderingTemplate = service.Unarchive("inrtem_abc");
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