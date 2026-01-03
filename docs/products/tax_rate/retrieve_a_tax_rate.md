# Retrieve a tax rate

Retrieves a tax rate with the given ID

## Returns

Returns an tax rate if a valid tax rate ID was provided. Raises [an error](https://docs.stripe.com/api/tax_rates/retrieve.md#errors) otherwise.

```curl
curl https://api.stripe.com/v1/tax_rates/txr_1MzS4RLkdIwHu7ixwvpZ9c2i \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe tax_rates retrieve txr_1MzS4RLkdIwHu7ixwvpZ9c2i
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

tax_rate = client.v1.tax_rates.retrieve('txr_1MzS4RLkdIwHu7ixwvpZ9c2i')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

tax_rate = client.v1.tax_rates.retrieve("txr_1MzS4RLkdIwHu7ixwvpZ9c2i")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$taxRate = $stripe->taxRates->retrieve('txr_1MzS4RLkdIwHu7ixwvpZ9c2i', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TaxRateRetrieveParams params = TaxRateRetrieveParams.builder().build();

TaxRate taxRate =
  client.v1().taxRates().retrieve("txr_1MzS4RLkdIwHu7ixwvpZ9c2i", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const taxRate = await stripe.taxRates.retrieve('txr_1MzS4RLkdIwHu7ixwvpZ9c2i');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TaxRateRetrieveParams{}
result, err := sc.V1TaxRates.Retrieve(
  context.TODO(), "txr_1MzS4RLkdIwHu7ixwvpZ9c2i", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.TaxRates;
TaxRate taxRate = service.Get("txr_1MzS4RLkdIwHu7ixwvpZ9c2i");
```

### Response

```json
{
  "id": "txr_1MzS4RLkdIwHu7ixwvpZ9c2i",
  "object": "tax_rate",
  "active": true,
  "country": null,
  "created": 1682114687,
  "description": "VAT Germany",
  "display_name": "VAT",
  "inclusive": false,
  "jurisdiction": "DE",
  "livemode": false,
  "metadata": {},
  "percentage": 16,
  "state": null,
  "tax_type": null
}
```