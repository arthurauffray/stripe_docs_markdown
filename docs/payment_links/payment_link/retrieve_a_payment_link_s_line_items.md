# Retrieve a payment link's line items

When retrieving a payment link, there is an includable **line\_items** property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` payment link line items, starting after Line Item `starting_after`. Each entry in the array is a separate Line Item object. If no more line items are available, the resulting array will be empty.

## Parameters

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl https://api.stripe.com/v1/payment_links/plink_1N4CWjLkdIwHu7ix2Y2F1kqb/line_items \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe payment_links list_line_items plink_1N4CWjLkdIwHu7ix2Y2F1kqb
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

line_items = client.v1.payment_links.line_items.list('plink_1N4CWjLkdIwHu7ix2Y2F1kqb')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

line_items = client.v1.payment_links.line_items.list(
  "plink_1N4CWjLkdIwHu7ix2Y2F1kqb",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$lineItems = $stripe->paymentLinks->allLineItems(
  'plink_1N4CWjLkdIwHu7ix2Y2F1kqb',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PaymentLinkLineItemListParams params =
  PaymentLinkLineItemListParams.builder().build();

StripeCollection<LineItem> stripeCollection =
  client.v1().paymentLinks().lineItems().list(
    "plink_1N4CWjLkdIwHu7ix2Y2F1kqb",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const lineItems = await stripe.paymentLinks.listLineItems(
  'plink_1N4CWjLkdIwHu7ix2Y2F1kqb'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PaymentLinkListLineItemsParams{
  PaymentLink: stripe.String("plink_1N4CWjLkdIwHu7ix2Y2F1kqb"),
}
result := sc.V1PaymentLinks.ListLineItems(context.TODO(), params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.PaymentLinks.LineItems;
StripeList<LineItem> lineItems = service.List("plink_1N4CWjLkdIwHu7ix2Y2F1kqb");
```

### Response

```json
{
  "object": "list",
  "data": [
    {
      "id": "li_NpsHNiHSaDeU0X",
      "object": "item",
      "amount_discount": 0,
      "amount_subtotal": 1099,
      "amount_tax": 0,
      "amount_total": 1099,
      "currency": "usd",
      "description": "T-shirt",
      "price": {
        "id": "price_1N4AEsLkdIwHu7ix7Ssho8Cl",
        "object": "price",
        "active": true,
        "billing_scheme": "per_unit",
        "created": 1683237782,
        "currency": "usd",
        "custom_unit_amount": null,
        "livemode": false,
        "lookup_key": null,
        "metadata": {},
        "nickname": null,
        "product": "prod_NppuJWzzNnD5Ut",
        "recurring": null,
        "tax_behavior": "unspecified",
        "tiers_mode": null,
        "transform_quantity": null,
        "type": "one_time",
        "unit_amount": 1099,
        "unit_amount_decimal": "1099"
      },
      "quantity": 1
    }
  ],
  "has_more": false,
  "url": "/v1/payment_links/plink_1N4CWjLkdIwHu7ix2Y2F1kqb/line_items"
}
```