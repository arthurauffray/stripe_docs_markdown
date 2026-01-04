# Submit a dispute

Submits an Issuing `Dispute` to the card network. Stripe validates that all evidence fields required for the dispute’s reason are present. For more details, see [Dispute reasons and evidence](https://docs.stripe.com/docs/issuing/purchases/disputes.md#dispute-reasons-and-evidence).

## Returns

Returns an Issuing `Dispute` object in `submitted` status if submission succeeds.

## Parameters

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl -X POST https://api.stripe.com/v1/issuing/disputes/idp_1MykdxFtDWhhyHE1BFAV3osZ/submit \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe issuing disputes submit idp_1MykdxFtDWhhyHE1BFAV3osZ
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

dispute = client.v1.issuing.disputes.submit('idp_1MykdxFtDWhhyHE1BFAV3osZ')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

dispute = client.v1.issuing.disputes.submit("idp_1MykdxFtDWhhyHE1BFAV3osZ")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$dispute = $stripe->issuing->disputes->submit('idp_1MykdxFtDWhhyHE1BFAV3osZ', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

DisputeSubmitParams params = DisputeSubmitParams.builder().build();

Dispute dispute =
  client.v1().issuing().disputes().submit("idp_1MykdxFtDWhhyHE1BFAV3osZ", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const dispute = await stripe.issuing.disputes.submit('idp_1MykdxFtDWhhyHE1BFAV3osZ');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.IssuingDisputeSubmitParams{}
result, err := sc.V1IssuingDisputes.Submit(
  context.TODO(), "idp_1MykdxFtDWhhyHE1BFAV3osZ", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Issuing.Disputes;
Stripe.Issuing.Dispute dispute = service.Submit("idp_1MykdxFtDWhhyHE1BFAV3osZ");
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
  "status": "submitted",
  "transaction": "ipi_1MykXhFtDWhhyHE1UjsZZ3xQ"
}
```