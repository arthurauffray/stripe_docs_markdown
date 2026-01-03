# Delete a product

Delete a product. Deleting a product is only possible if it has no prices associated with it. Additionally, deleting a product with `type=good` is only possible if it has no SKUs associated with it.

## Returns

Returns a deleted object on success. Otherwise, this call raises [an error](https://docs.stripe.com/api/products/delete.md#errors).

```curl
curl -X DELETE https://api.stripe.com/v1/products/prod_NWjs8kKbJWmuuc \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe products delete prod_NWjs8kKbJWmuuc
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

deleted = client.v1.products.delete('prod_NWjs8kKbJWmuuc')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

deleted = client.v1.products.delete("prod_NWjs8kKbJWmuuc")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$deleted = $stripe->products->delete('prod_NWjs8kKbJWmuuc', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

Product product = client.v1().products().delete("prod_NWjs8kKbJWmuuc");
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const deleted = await stripe.products.del('prod_NWjs8kKbJWmuuc');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.ProductDeleteParams{}
result, err := sc.V1Products.Delete(context.TODO(), "prod_NWjs8kKbJWmuuc", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Products;
Product deleted = service.Delete("prod_NWjs8kKbJWmuuc");
```

### Response

```json
{
  "id": "prod_NWjs8kKbJWmuuc",
  "object": "product",
  "deleted": true
}
```