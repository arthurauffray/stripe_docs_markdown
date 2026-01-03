# Reverse a payout

Reverses a payout by debiting the destination bank account. At this time, you can only reverse payouts for connected accounts to US and Canadian bank accounts. If the payout is manual and in the `pending` status, use `/v1/payouts/:id/cancel` instead.

By requesting a reversal through `/v1/payouts/:id/reverse`, you confirm that the authorized signatory of the selected bank account authorizes the debit on the bank account and that no other authorization is required.

## Returns

Returns the reversing payout object if the reversal is successful. Returns an error if the payout is already reversed or can’t be reversed.

## Parameters

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl -X POST https://api.stripe.com/v1/payouts/po_1OaFDbEcg9tTZuTgNYmX0PKB/reverse \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe payouts reverse po_1OaFDbEcg9tTZuTgNYmX0PKB
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

payout = client.v1.payouts.reverse('po_1OaFDbEcg9tTZuTgNYmX0PKB')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

payout = client.v1.payouts.reverse("po_1OaFDbEcg9tTZuTgNYmX0PKB")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$payout = $stripe->payouts->reverse('po_1OaFDbEcg9tTZuTgNYmX0PKB', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PayoutReverseParams params = PayoutReverseParams.builder().build();

Payout payout = client.v1().payouts().reverse("po_1OaFDbEcg9tTZuTgNYmX0PKB", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const payout = await stripe.payouts.reverse('po_1OaFDbEcg9tTZuTgNYmX0PKB');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PayoutReverseParams{}
result, err := sc.V1Payouts.Reverse(
  context.TODO(), "po_1OaFDbEcg9tTZuTgNYmX0PKB", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Payouts;
Payout payout = service.Reverse("po_1OaFDbEcg9tTZuTgNYmX0PKB");
```

### Response

```json
{
  "id": "po_1Oj6B8rU4sY9X3L2mQ6T5fZ1",
  "object": "payout",
  "amount": -1100,
  "arrival_date": 1680652800,
  "automatic": false,
  "balance_transaction": "txn_1O5G7H8k1p2Q9a6c0N8elkI0",
  "created": 1680648691,
  "currency": "usd",
  "description": null,
  "destination": "ba_1MtIhL2eZvKYlo2CAElKwKu2",
  "failure_balance_transaction": null,
  "failure_code": null,
  "failure_message": null,
  "livemode": false,
  "metadata": {},
  "method": "standard",
  "original_payout": "po_1OaFDbEcg9tTZuTgNYmX0PKB",
  "reconciliation_status": "not_applicable",
  "reversed_by": null,
  "source_type": "card",
  "statement_descriptor": null,
  "status": "pending",
  "type": "bank_account"
}
```