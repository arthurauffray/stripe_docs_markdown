# Update an invoice item

Updates the amount or description of an invoice item on an upcoming invoice. Updating an invoice item is only possible before the invoice it’s attached to is closed.

## Returns

The updated invoice item object is returned upon success. Otherwise, this call raises [an error](https://docs.stripe.com/api/invoiceitems/update.md#errors).

## Parameters

- `amount` (integer, optional)
  The integer amount in cents of the charge to be applied to the upcoming invoice. If you want to apply a credit to the customer’s account, pass a negative amount.

- `description` (string, optional)
  An arbitrary string which you can attach to the invoice item. The description is displayed in the invoice for easy tracking.

- `discountable` (boolean, optional)
  Controls whether discounts apply to this invoice item. Defaults to false for prorations or negative invoice items, and true for all other invoice items. Cannot be set to true for prorations.

- `discounts` (array of objects, optional)
  The coupons, promotion codes & existing discounts which apply to the invoice item or invoice line item. Item discounts are applied before invoice discounts. Pass an empty string to remove previously-defined discounts.

  - `discounts.coupon` (string, optional)
    ID of the coupon to create a new discount for.

  - `discounts.discount` (string, optional)
    ID of an existing discount on the object (or one of its ancestors) to reuse.

  - `discounts.promotion_code` (string, optional)
    ID of the promotion code to create a new discount for.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `period` (object, optional)
  The period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you have [Stripe Revenue Recognition](https://docs.stripe.com/docs/revenue-recognition.md) enabled, the period will be used to recognize and defer revenue. See the [Revenue Recognition documentation](https://docs.stripe.com/docs/revenue-recognition/methodology/subscriptions-and-invoicing.md) for details.

  - `period.end` (timestamp, required)
    The end of the period, which must be greater than or equal to the start. This value is inclusive.

  - `period.start` (timestamp, required)
    The start of the period. This value is inclusive.

- `price_data` (object, optional)
  Data used to generate a new [Price](https://docs.stripe.com/docs/api/prices.md) object inline.

  - `price_data.currency` (enum, required)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `price_data.product` (string, required)
    The ID of the [Product](https://docs.stripe.com/api/products.md) that this [Price](https://docs.stripe.com/api/prices.md) will belong to.

  - `price_data.tax_behavior` (enum, recommended if calculating taxes)
    Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
Possible enum values:
    - `exclusive`
    - `inclusive`
    - `unspecified`

  - `price_data.unit_amount` (integer, optional)
    A positive integer in cents (or 0 for a free price) representing how much to charge.

  - `price_data.unit_amount_decimal` (string, required conditionally)
    Same as `unit_amount`, but accepts a decimal value in cents with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.

- `pricing` (object, optional)
  The pricing information for the invoice item.

  - `pricing.price` (string, optional)
    The ID of the price object.

- `quantity` (integer, optional)
  Non-negative integer. The quantity of units for the invoice item.

- `tax_behavior` (enum, recommended if calculating taxes)
  Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
Possible enum values:
  - `exclusive`
  - `inclusive`
  - `unspecified`

- `tax_code` (string, recommended if calculating taxes)
  A [tax code](https://docs.stripe.com/docs/tax/tax-categories.md) ID.

- `tax_rates` (array of strings, optional)
  The tax rates which apply to the invoice item. When set, the `default_tax_rates` on the invoice do not apply to this invoice item. Pass an empty string to remove previously-defined tax rates.

- `unit_amount_decimal` (string, optional)
  The decimal unit amount in cents of the charge to be applied to the upcoming invoice. This `unit_amount_decimal` will be multiplied by the quantity to get the full amount. Passing in a negative `unit_amount_decimal` will reduce the `amount_due` on the invoice. Accepts at most 12 decimal places.

```curl
curl https://api.stripe.com/v1/invoiceitems/ii_1MtGUtLkdIwHu7ixBYwjAM00 \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
```

```cli
stripe invoiceitems update ii_1MtGUtLkdIwHu7ixBYwjAM00 \
  -d "metadata[order_id]"=6735
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

invoice_item = client.v1.invoice_items.update(
  'ii_1MtGUtLkdIwHu7ixBYwjAM00',
  {metadata: {order_id: '6735'}},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

invoice_item = client.v1.invoice_items.update(
  "ii_1MtGUtLkdIwHu7ixBYwjAM00",
  {"metadata": {"order_id": "6735"}},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$invoiceItem = $stripe->invoiceItems->update(
  'ii_1MtGUtLkdIwHu7ixBYwjAM00',
  ['metadata' => ['order_id' => '6735']]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

InvoiceItemUpdateParams params =
  InvoiceItemUpdateParams.builder().putMetadata("order_id", "6735").build();

InvoiceItem invoiceItem =
  client.v1().invoiceItems().update("ii_1MtGUtLkdIwHu7ixBYwjAM00", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const invoiceItem = await stripe.invoiceItems.update(
  'ii_1MtGUtLkdIwHu7ixBYwjAM00',
  {
    metadata: {
      order_id: '6735',
    },
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.InvoiceItemUpdateParams{}
params.AddMetadata("order_id", "6735")
result, err := sc.V1InvoiceItems.Update(
  context.TODO(), "ii_1MtGUtLkdIwHu7ixBYwjAM00", params)
```

```dotnet
var options = new InvoiceItemUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.InvoiceItems;
InvoiceItem invoiceItem = service.Update("ii_1MtGUtLkdIwHu7ixBYwjAM00", options);
```

### Response

```json
{
  "id": "ii_1MtGUtLkdIwHu7ixBYwjAM00",
  "object": "invoiceitem",
  "amount": 1099,
  "currency": "usd",
  "customer": "cus_NeZei8imSbMVvi",
  "date": 1680640231,
  "description": "T-shirt",
  "discountable": true,
  "discounts": [],
  "invoice": null,
  "livemode": false,
  "metadata": {
    "order_id": "6735"
  },
  "parent": null,
  "period": {
    "end": 1680640231,
    "start": 1680640231
  },
  "pricing": {
    "price_details": {
      "price": "price_1MtGUsLkdIwHu7ix1be5Ljaj",
      "product": "prod_NeZe7xbBdJT8EN"
    },
    "type": "price_details",
    "unit_amount_decimal": "1099"
  },
  "proration": false,
  "quantity": 1,
  "tax_rates": [],
  "test_clock": null
}
```