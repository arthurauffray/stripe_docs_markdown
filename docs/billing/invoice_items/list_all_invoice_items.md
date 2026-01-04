# List all invoice items

Returns a list of your invoice items. Invoice items are returned sorted by creation date, with the most recently created invoice items appearing first.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` invoice items, starting after invoice item `starting_after`. Each entry in the array is a separate invoice item object. If no more invoice items are available, the resulting array will be empty.

## Parameters

- `created` (object, optional)
  Only return invoice items that were created during the given date interval.

  - `created.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `created.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `created.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `created.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `customer` (string, optional)
  The identifier of the customer whose invoice items to return. If none is provided, returns all invoice items.

- `customer_account` (string, optional)
  The identifier of the account representing the customer whose invoice items to return. If none is provided, returns all invoice items.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `invoice` (string, optional)
  Only return invoice items belonging to this invoice. If none is provided, all invoice items will be returned. If specifying an invoice, no customer identifier is needed.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `pending` (boolean, optional)
  Set to `true` to only show pending invoice items, which are not yet attached to any invoices. Set to `false` to only show invoice items already attached to invoices. If unspecified, no filter is applied.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/invoiceitems \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe invoiceitems list  \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

invoice_items = client.v1.invoice_items.list({limit: 3})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

invoice_items = client.v1.invoice_items.list({"limit": 3})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$invoiceItems = $stripe->invoiceItems->all(['limit' => 3]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

InvoiceItemListParams params = InvoiceItemListParams.builder().setLimit(3L).build();

StripeCollection<InvoiceItem> stripeCollection =
  client.v1().invoiceItems().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const invoiceItems = await stripe.invoiceItems.list({
  limit: 3,
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.InvoiceItemListParams{}
params.Limit = stripe.Int64(3)
result := sc.V1InvoiceItems.List(context.TODO(), params)
```

```dotnet
var options = new InvoiceItemListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.InvoiceItems;
StripeList<InvoiceItem> invoiceItems = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/invoiceitems",
  "has_more": false,
  "data": [
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
      "metadata": {},
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
  ]
}
```