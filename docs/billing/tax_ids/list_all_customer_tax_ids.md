# List all Customer tax IDs

Returns a list of tax IDs for a customer.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` tax IDs, starting after tax ID `starting_after`. Each entry in the array is a separate `tax_id` object. If no more tax IDs are available, the resulting array will be empty. Raises [an error](https://docs.stripe.com/api/tax_ids/customer_list.md#errors) if the customer ID is invalid.

## Parameters

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/customers/cus_NZKoSNZZ58qtO0/tax_ids \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe tax_ids list cus_NZKoSNZZ58qtO0 \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

tax_ids = client.v1.customers.tax_ids.list('cus_NZKoSNZZ58qtO0', {limit: 3})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

tax_ids = client.v1.customers.tax_ids.list(
  "cus_NZKoSNZZ58qtO0",
  {"limit": 3},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$taxIds = $stripe->customers->allTaxIds('cus_NZKoSNZZ58qtO0', ['limit' => 3]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CustomerTaxIdListParams params =
  CustomerTaxIdListParams.builder().setLimit(3L).build();

StripeCollection<TaxId> stripeCollection =
  client.v1().customers().taxIds().list("cus_NZKoSNZZ58qtO0", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const taxIds = await stripe.customers.listTaxIds(
  'cus_NZKoSNZZ58qtO0',
  {
    limit: 3,
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TaxIDListParams{Customer: stripe.String("cus_NZKoSNZZ58qtO0")}
params.Limit = stripe.Int64(3)
result := sc.V1TaxIDs.List(context.TODO(), params)
```

```dotnet
var options = new CustomerTaxIdListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Customers.TaxIds;
StripeList<TaxId> taxIds = service.List("cus_NZKoSNZZ58qtO0", options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/customers/cus_NZKoSNZZ58qtO0/tax_ids",
  "has_more": false,
  "data": [
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
  ]
}
```