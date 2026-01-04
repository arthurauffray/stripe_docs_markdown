# List all tax codes

A list of [all tax codes available](https://stripe.com/docs/tax/tax-categories) to add to Products in order to allow specific tax calculations.

## Returns

A dictionary with a data property that contains an array of up to limit tax codes, starting after tax code starting_after. Each entry in the array is a separate tax code object. If no more tax codes are available, the resulting array will be empty. This request should never return an error.

## Parameters

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/tax_codes \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe tax_codes list  \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

tax_codes = client.v1.tax_codes.list({limit: 3})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

tax_codes = client.v1.tax_codes.list({"limit": 3})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$taxCodes = $stripe->taxCodes->all(['limit' => 3]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TaxCodeListParams params = TaxCodeListParams.builder().setLimit(3L).build();

StripeCollection<TaxCode> stripeCollection = client.v1().taxCodes().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const taxCodes = await stripe.taxCodes.list({
  limit: 3,
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TaxCodeListParams{}
params.Limit = stripe.Int64(3)
result := sc.V1TaxCodes.List(context.TODO(), params)
```

```dotnet
var options = new TaxCodeListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.TaxCodes;
StripeList<TaxCode> taxCodes = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/tax_codes",
  "has_more": false,
  "data": [
    {
      "id": "txcd_99999999",
      "object": "tax_code",
      "description": "Any tangible or physical good. For jurisdictions that impose a tax, the standard rate is applied.",
      "name": "General - Tangible Goods"
    }
  ]
}
```