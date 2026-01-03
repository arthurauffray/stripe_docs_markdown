# Update a tax rate

Updates an existing tax rate.

## Returns

The updated tax rate.

## Parameters

- `active` (boolean, optional)
  Flag determining whether the tax rate is active or inactive (archived). Inactive tax rates cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.

- `country` (string, optional)
  Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

- `description` (string, optional)
  An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.

- `display_name` (string, optional)
  The display name of the tax rate, which will be shown to users.

  The maximum length is 50 characters.

- `jurisdiction` (string, optional)
  The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.

  The maximum length is 50 characters.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `state` (string, optional)
  [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2), without country prefix. For example, “NY” for New York, United States.

- `tax_type` (enum, optional)
  The high-level tax type, such as `vat` or `sales_tax`.
Possible enum values:
  - `amusement_tax`
    Amusement Tax

  - `communications_tax`
    Communications Tax

  - `gst`
    Goods and Services Tax

  - `hst`
    Harmonized Sales Tax

  - `igst`
    Integrated Goods and Services Tax

  - `jct`
    Japanese Consumption Tax

  - `lease_tax`
    Chicago Lease Tax

  - `pst`
    Provincial Sales Tax

  - `qst`
    Quebec Sales Tax

  - `retail_delivery_fee`
    Retail Delivery Fee

  - `rst`
    Retail Sales Tax

  - `sales_tax`
    Sales Tax

  - `service_tax`
    Service Tax

  - `vat`
    Value-Added Tax

```curl
curl https://api.stripe.com/v1/tax_rates/txr_1MzS4RLkdIwHu7ixwvpZ9c2i \
  -u "<<YOUR_SECRET_KEY>>" \
  -d active=false
```

```cli
stripe tax_rates update txr_1MzS4RLkdIwHu7ixwvpZ9c2i \
  --active=false
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

tax_rate = client.v1.tax_rates.update(
  'txr_1MzS4RLkdIwHu7ixwvpZ9c2i',
  {active: false},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

tax_rate = client.v1.tax_rates.update(
  "txr_1MzS4RLkdIwHu7ixwvpZ9c2i",
  {"active": False},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$taxRate = $stripe->taxRates->update(
  'txr_1MzS4RLkdIwHu7ixwvpZ9c2i',
  ['active' => false]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TaxRateUpdateParams params = TaxRateUpdateParams.builder().setActive(false).build();

TaxRate taxRate =
  client.v1().taxRates().update("txr_1MzS4RLkdIwHu7ixwvpZ9c2i", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const taxRate = await stripe.taxRates.update(
  'txr_1MzS4RLkdIwHu7ixwvpZ9c2i',
  {
    active: false,
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TaxRateUpdateParams{Active: stripe.Bool(false)}
result, err := sc.V1TaxRates.Update(
  context.TODO(), "txr_1MzS4RLkdIwHu7ixwvpZ9c2i", params)
```

```dotnet
var options = new TaxRateUpdateOptions { Active = false };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.TaxRates;
TaxRate taxRate = service.Update("txr_1MzS4RLkdIwHu7ixwvpZ9c2i", options);
```

### Response

```json
{
  "id": "txr_1MzS4RLkdIwHu7ixwvpZ9c2i",
  "object": "tax_rate",
  "active": false,
  "country": null,
  "created": 1682114687,
  "description": "VAT Germany",
  "display_name": "VAT",
  "effective_percentage": 16,
  "inclusive": false,
  "jurisdiction": "DE",
  "livemode": false,
  "metadata": {},
  "percentage": 16,
  "state": null,
  "tax_type": null
}
```