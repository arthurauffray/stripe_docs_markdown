# Retrieve a dispute

Retrieves an Issuing `Dispute` object.

## Returns

Returns an Issuing `Dispute` object if a valid identifier was provided.

```curl
curl https://api.stripe.com/v1/issuing/disputes/idp_1MykdxFtDWhhyHE1BFAV3osZ \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe issuing disputes retrieve idp_1MykdxFtDWhhyHE1BFAV3osZ
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

dispute = client.v1.issuing.disputes.retrieve('idp_1MykdxFtDWhhyHE1BFAV3osZ')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

dispute = client.v1.issuing.disputes.retrieve("idp_1MykdxFtDWhhyHE1BFAV3osZ")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$dispute = $stripe->issuing->disputes->retrieve('idp_1MykdxFtDWhhyHE1BFAV3osZ', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

DisputeRetrieveParams params = DisputeRetrieveParams.builder().build();

Dispute dispute =
  client.v1().issuing().disputes().retrieve("idp_1MykdxFtDWhhyHE1BFAV3osZ", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const dispute = await stripe.issuing.disputes.retrieve(
  'idp_1MykdxFtDWhhyHE1BFAV3osZ'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.IssuingDisputeRetrieveParams{}
result, err := sc.V1IssuingDisputes.Retrieve(
  context.TODO(), "idp_1MykdxFtDWhhyHE1BFAV3osZ", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Issuing.Disputes;
Stripe.Issuing.Dispute dispute = service.Get("idp_1MykdxFtDWhhyHE1BFAV3osZ");
```

### Response

```json
{
  "id": "idp_1MykdxFtDWhhyHE1BFAV3osZ",
  "object": "issuing.dispute",
  "amount": 100,
  "created": 1681947753,
  "currency": "usd",
  "evidence": {
    "fraudulent": {
      "additional_documentation": null,
      "dispute_explanation": null,
      "explanation": "This transaction is fraudulent.",
      "uncategorized_file": null
    },
    "reason": "fraudulent"
  },
  "livemode": false,
  "metadata": {},
  "status": "unsubmitted",
  "transaction": "ipi_1MykXhFtDWhhyHE1UjsZZ3xQ"
}
```