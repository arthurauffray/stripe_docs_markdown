# Retrieve a tax code

Retrieves the details of an existing tax code. Supply the unique tax code ID and Stripe will return the corresponding tax code information.

## Returns

Returns a tax code object if a valid identifier was provided.

```curl
curl https://api.stripe.com/v1/tax_codes/txcd_99999999 \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe tax_codes retrieve txcd_99999999
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

tax_code = client.v1.tax_codes.retrieve('txcd_99999999')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

tax_code = client.v1.tax_codes.retrieve("txcd_99999999")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$taxCode = $stripe->taxCodes->retrieve('txcd_99999999', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TaxCodeRetrieveParams params = TaxCodeRetrieveParams.builder().build();

TaxCode taxCode = client.v1().taxCodes().retrieve("txcd_99999999", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const taxCode = await stripe.taxCodes.retrieve('txcd_99999999');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TaxCodeRetrieveParams{}
result, err := sc.V1TaxCodes.Retrieve(context.TODO(), "txcd_99999999", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.TaxCodes;
TaxCode taxCode = service.Get("txcd_99999999");
```

### Response

```json
{
  "id": "txcd_99999999",
  "object": "tax_code",
  "description": "Any tangible or physical good. For jurisdictions that impose a tax, the standard rate is applied.",
  "name": "General - Tangible Goods"
}
```