# Retrieve a product

Retrieves the details of an existing product. Supply the unique product ID from either a product creation request or the product list, and Stripe will return the corresponding product information.

## Returns

Returns a product object if a valid identifier was provided.

```curl
curl https://api.stripe.com/v1/products/prod_NWjs8kKbJWmuuc \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe products retrieve prod_NWjs8kKbJWmuuc
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

product = client.v1.products.retrieve('prod_NWjs8kKbJWmuuc')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

product = client.v1.products.retrieve("prod_NWjs8kKbJWmuuc")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$product = $stripe->products->retrieve('prod_NWjs8kKbJWmuuc', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ProductRetrieveParams params = ProductRetrieveParams.builder().build();

Product product = client.v1().products().retrieve("prod_NWjs8kKbJWmuuc", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const product = await stripe.products.retrieve('prod_NWjs8kKbJWmuuc');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.ProductRetrieveParams{}
result, err := sc.V1Products.Retrieve(context.TODO(), "prod_NWjs8kKbJWmuuc", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Products;
Product product = service.Get("prod_NWjs8kKbJWmuuc");
```

### Response

```json
{
  "id": "prod_NWjs8kKbJWmuuc",
  "object": "product",
  "active": true,
  "created": 1678833149,
  "default_price": null,
  "description": null,
  "images": [],
  "marketing_features": [],
  "livemode": false,
  "metadata": {},
  "name": "Gold Plan",
  "package_dimensions": null,
  "shippable": null,
  "statement_descriptor": null,
  "tax_code": null,
  "unit_label": null,
  "updated": 1678833149,
  "url": null
}
```