# Retrieve a Customer tax ID

Retrieves the `tax_id` object with the given identifier.

## Returns

Returns a `tax_id` object if a valid identifier was provided.

```curl
curl https://api.stripe.com/v1/customers/cus_NZKoSNZZ58qtO0/tax_ids/txi_1MoC8zLkdIwHu7ixEhgWcHzJ \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe tax_ids retrieve cus_NZKoSNZZ58qtO0 txi_1MoC8zLkdIwHu7ixEhgWcHzJ
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

tax_id = client.v1.customers.tax_ids.retrieve(
  'cus_NZKoSNZZ58qtO0',
  'txi_1MoC8zLkdIwHu7ixEhgWcHzJ',
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

tax_id = client.v1.customers.tax_ids.retrieve(
  "cus_NZKoSNZZ58qtO0",
  "txi_1MoC8zLkdIwHu7ixEhgWcHzJ",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$taxId = $stripe->customers->retrieveTaxId(
  'cus_NZKoSNZZ58qtO0',
  'txi_1MoC8zLkdIwHu7ixEhgWcHzJ',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CustomerTaxIdRetrieveParams params = CustomerTaxIdRetrieveParams.builder().build();

TaxId taxId =
  client.v1().customers().taxIds().retrieve(
    "cus_NZKoSNZZ58qtO0",
    "txi_1MoC8zLkdIwHu7ixEhgWcHzJ",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const taxId = await stripe.customers.retrieveTaxId(
  'cus_NZKoSNZZ58qtO0',
  'txi_1MoC8zLkdIwHu7ixEhgWcHzJ'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TaxIDRetrieveParams{Customer: stripe.String("cus_NZKoSNZZ58qtO0")}
result, err := sc.V1TaxIDs.Retrieve(
  context.TODO(), "txi_1MoC8zLkdIwHu7ixEhgWcHzJ", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Customers.TaxIds;
TaxId taxId = service.Get("cus_NZKoSNZZ58qtO0", "txi_1MoC8zLkdIwHu7ixEhgWcHzJ");
```

### Response

```json
{
  "id": "txi_1MoC8zLkdIwHu7ixEhgWcHzJ",
  "object": "tax_id",
  "country": "DE",
  "created": 1679431857,
  "customer": "cus_NZKoSNZZ58qtO0",
  "livemode": false,
  "type": "eu_vat",
  "value": "DE123456789",
  "verification": {
    "status": "pending",
    "verified_address": null,
    "verified_name": null
  }
}
```