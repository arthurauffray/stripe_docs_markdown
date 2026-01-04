# Retrieve a source

Retrieves an existing source object. Supply the unique source ID from a source creation request and Stripe will return the corresponding up-to-date source object information.

## Returns

Returns a source if a valid identifier was provided.

## Parameters

- `client_secret` (string, optional)
  The client secret of the source. Required if a publishable key is used to retrieve the source.

```curl
curl https://api.stripe.com/v1/sources/src_1N3lxdLkdIwHu7ixPHXy8UcI \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe sources retrieve src_1N3lxdLkdIwHu7ixPHXy8UcI
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

source = client.v1.sources.retrieve('src_1N3lxdLkdIwHu7ixPHXy8UcI')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

source = client.v1.sources.retrieve("src_1N3lxdLkdIwHu7ixPHXy8UcI")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$source = $stripe->sources->retrieve('src_1N3lxdLkdIwHu7ixPHXy8UcI', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

SourceRetrieveParams params = SourceRetrieveParams.builder().build();

Source source =
  client.v1().sources().retrieve("src_1N3lxdLkdIwHu7ixPHXy8UcI", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const source = await stripe.sources.retrieve('src_1N3lxdLkdIwHu7ixPHXy8UcI');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.SourceRetrieveParams{}
result, err := sc.V1Sources.Retrieve(
  context.TODO(), "src_1N3lxdLkdIwHu7ixPHXy8UcI", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Sources;
Source source = service.Get("src_1N3lxdLkdIwHu7ixPHXy8UcI");
```

### Response

```json
{
  "id": "src_1N3lxdLkdIwHu7ixPHXy8UcI",
  "object": "source",
  "ach_credit_transfer": {
    "account_number": "test_eb829353ed79",
    "bank_name": "TEST BANK",
    "fingerprint": "kBQsBk9KtfCgjEYK",
    "refund_account_holder_name": null,
    "refund_account_holder_type": null,
    "refund_routing_number": null,
    "routing_number": "110000000",
    "swift_code": "TSTEZ122"
  },
  "amount": null,
  "client_secret": "src_client_secret_ZaOIRUD8a9uGmQobLxGvqKSr",
  "created": 1683144457,
  "currency": "usd",
  "flow": "receiver",
  "livemode": false,
  "metadata": {},
  "owner": {
    "address": null,
    "email": "jenny.rosen@example.com",
    "name": null,
    "phone": null,
    "verified_address": null,
    "verified_email": null,
    "verified_name": null,
    "verified_phone": null
  },
  "receiver": {
    "address": "110000000-test_eb829353ed79",
    "amount_charged": 0,
    "amount_received": 0,
    "amount_returned": 0,
    "refund_attributes_method": "email",
    "refund_attributes_status": "missing"
  },
  "statement_descriptor": null,
  "status": "pending",
  "type": "ach_credit_transfer",
  "usage": "reusable"
}
```