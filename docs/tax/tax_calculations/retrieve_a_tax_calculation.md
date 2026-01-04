# Retrieve a Tax Calculation

Retrieves a Tax `Calculation` object, if the calculation hasn’t expired.

## Returns

A Tax `Calculation` object if the Tax calculation is found. Otherwise returns a ‘not found’ error.

```curl
curl https://api.stripe.com/v1/tax/calculations/taxcalc_1OduxkBUZ691iUZ4iWvpMApI \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe tax calculations retrieve taxcalc_1OduxkBUZ691iUZ4iWvpMApI
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

calculation = client.v1.tax.calculations.retrieve('taxcalc_1OduxkBUZ691iUZ4iWvpMApI')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

calculation = client.v1.tax.calculations.retrieve("taxcalc_1OduxkBUZ691iUZ4iWvpMApI")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$calculation = $stripe->tax->calculations->retrieve(
  'taxcalc_1OduxkBUZ691iUZ4iWvpMApI',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CalculationRetrieveParams params = CalculationRetrieveParams.builder().build();

Calculation calculation =
  client.v1().tax().calculations().retrieve(
    "taxcalc_1OduxkBUZ691iUZ4iWvpMApI",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const calculation = await stripe.tax.calculations.retrieve(
  'taxcalc_1OduxkBUZ691iUZ4iWvpMApI'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TaxCalculationRetrieveParams{}
result, err := sc.V1TaxCalculations.Retrieve(
  context.TODO(), "taxcalc_1OduxkBUZ691iUZ4iWvpMApI", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Tax.Calculations;
Stripe.Tax.Calculation calculation = service.Get("taxcalc_1OduxkBUZ691iUZ4iWvpMApI");
```

### Response

```json
{
  "id": "taxcalc_1OduxkBUZ691iUZ4iWvpMApI",
  "object": "tax.calculation",
  "amount_total": 1953,
  "currency": "usd",
  "customer": null,
  "customer_details": {
    "address": {
      "city": "Seattle",
      "country": "US",
      "line1": "920 5th Ave",
      "line2": null,
      "postal_code": "98104",
      "state": "WA"
    },
    "address_source": "shipping",
    "ip_address": null,
    "tax_ids": [],
    "taxability_override": "none"
  },
  "expires_at": 1706708005,
  "line_items": {
    "object": "list",
    "data": [
      {
        "id": "tax_li_PSqf3RMNZa23H4",
        "object": "tax.calculation_line_item",
        "amount": 1499,
        "amount_tax": 154,
        "livemode": false,
        "product": null,
        "quantity": 1,
        "reference": "Music Streaming Coupon",
        "tax_behavior": "exclusive",
        "tax_code": "txcd_10000000"
      }
    ],
    "has_more": false,
    "total_count": 1,
    "url": "/v1/tax/calculations/taxcalc_1OduxkBUZ691iUZ4iWvpMApI/line_items"
  },
  "livemode": false,
  "ship_from_details": null,
  "shipping_cost": {
    "amount": 300,
    "amount_tax": 0,
    "tax_behavior": "exclusive",
    "tax_code": "txcd_92010001"
  },
  "tax_amount_exclusive": 154,
  "tax_amount_inclusive": 0,
  "tax_breakdown": [
    {
      "amount": 154,
      "inclusive": false,
      "tax_rate_details": {
        "country": "US",
        "percentage_decimal": "10.25",
        "state": "WA",
        "tax_type": "sales_tax"
      },
      "taxability_reason": "standard_rated",
      "taxable_amount": 1499
    },
    {
      "amount": 0,
      "inclusive": false,
      "tax_rate_details": {
        "country": "DE",
        "percentage_decimal": "0.0",
        "state": null,
        "tax_type": "vat"
      },
      "taxability_reason": "zero_rated",
      "taxable_amount": 300
    }
  ],
  "tax_date": 1706535204
}
```