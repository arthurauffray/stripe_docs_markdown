# Retrieve a calculation's line items

Retrieves the line items of a tax calculation as a collection, if the calculation hasn’t expired.

## Returns

A list of Line Item objects if the Tax calculation is found. Otherwise returns a ‘not found’ error.

## Parameters

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

  The maximum length is 500 characters.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

  The maximum length is 500 characters.

```curl
curl -G https://api.stripe.com/v1/tax/calculations/taxcalc_1NpJD42eZvKYlo2CUti522cz/line_items \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe tax calculations list_line_items taxcalc_1NpJD42eZvKYlo2CUti522cz \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

calculation_line_items = client.v1.tax.calculations.line_items.list(
  'taxcalc_1NpJD42eZvKYlo2CUti522cz',
  {limit: 3},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

calculation_line_items = client.v1.tax.calculations.line_items.list(
  "taxcalc_1NpJD42eZvKYlo2CUti522cz",
  {"limit": 3},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$calculationLineItems = $stripe->tax->calculations->allLineItems(
  'taxcalc_1NpJD42eZvKYlo2CUti522cz',
  ['limit' => 3]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CalculationLineItemListParams params =
  CalculationLineItemListParams.builder().setLimit(3L).build();

StripeCollection<CalculationLineItem> stripeCollection =
  client.v1().tax().calculations().lineItems().list(
    "taxcalc_1NpJD42eZvKYlo2CUti522cz",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const calculationLineItems = await stripe.tax.calculations.listLineItems(
  'taxcalc_1NpJD42eZvKYlo2CUti522cz',
  {
    limit: 3,
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TaxCalculationListLineItemsParams{
  Calculation: stripe.String("taxcalc_1NpJD42eZvKYlo2CUti522cz"),
}
params.Limit = stripe.Int64(3)
result := sc.V1TaxCalculations.ListLineItems(context.TODO(), params)
```

```dotnet
var options = new Stripe.Tax.CalculationLineItemListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Tax.Calculations.LineItems;
StripeList<Stripe.Tax.CalculationLineItem> calculationLineItems = service.List(
    "taxcalc_1NpJD42eZvKYlo2CUti522cz",
    options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/tax/calculations/taxcalc_1NpJD42eZvKYlo2CUti522cz/line_items",
  "has_more": false,
  "data": [
    {
      "id": "tax_li_OcYJb5mQOSSSWD",
      "object": "tax.calculation_line_item",
      "amount": 1499,
      "amount_tax": 148,
      "livemode": false,
      "product": null,
      "quantity": 1,
      "reference": "Pepperoni Pizza",
      "tax_behavior": "exclusive",
      "tax_code": "txcd_40060003"
    }
  ]
}
```