# Update a payout

Updates the specified payout by setting the values of the parameters you pass. We don’t change parameters that you don’t provide. This request only accepts the metadata as arguments.

## Returns

Returns the payout object if the update succeeds. This call raises [an error](https://docs.stripe.com/api/payouts/update.md#errors) if update parameters are invalid.

## Parameters

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/payouts/po_1OaFDbEcg9tTZuTgNYmX0PKB \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
```

```cli
stripe payouts update po_1OaFDbEcg9tTZuTgNYmX0PKB \
  -d "metadata[order_id]"=6735
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

payout = client.v1.payouts.update(
  'po_1OaFDbEcg9tTZuTgNYmX0PKB',
  {metadata: {order_id: '6735'}},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

payout = client.v1.payouts.update(
  "po_1OaFDbEcg9tTZuTgNYmX0PKB",
  {"metadata": {"order_id": "6735"}},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$payout = $stripe->payouts->update(
  'po_1OaFDbEcg9tTZuTgNYmX0PKB',
  ['metadata' => ['order_id' => '6735']]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PayoutUpdateParams params =
  PayoutUpdateParams.builder().putMetadata("order_id", "6735").build();

Payout payout = client.v1().payouts().update("po_1OaFDbEcg9tTZuTgNYmX0PKB", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const payout = await stripe.payouts.update(
  'po_1OaFDbEcg9tTZuTgNYmX0PKB',
  {
    metadata: {
      order_id: '6735',
    },
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PayoutUpdateParams{}
params.AddMetadata("order_id", "6735")
result, err := sc.V1Payouts.Update(
  context.TODO(), "po_1OaFDbEcg9tTZuTgNYmX0PKB", params)
```

```dotnet
var options = new PayoutUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Payouts;
Payout payout = service.Update("po_1OaFDbEcg9tTZuTgNYmX0PKB", options);
```

### Response

```json
{
  "id": "po_1OaFDbEcg9tTZuTgNYmX0PKB",
  "object": "payout",
  "amount": 1100,
  "arrival_date": 1680652800,
  "automatic": false,
  "balance_transaction": "txn_1OaFDcEcg9tTZuTgYMR25tSe",
  "created": 1680648691,
  "currency": "usd",
  "description": null,
  "destination": "ba_1MtIhL2eZvKYlo2CAElKwKu2",
  "failure_balance_transaction": null,
  "failure_code": null,
  "failure_message": null,
  "livemode": false,
  "metadata": {
    "order_id": "6735"
  },
  "method": "standard",
  "original_payout": null,
  "reconciliation_status": "not_applicable",
  "reversed_by": null,
  "source_type": "card",
  "statement_descriptor": null,
  "status": "pending",
  "type": "bank_account"
}
```