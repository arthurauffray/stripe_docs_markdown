# Retrieve a payout

Retrieves the details of an existing payout. Supply the unique payout ID from either a payout creation request or the payout list. Stripe returns the corresponding payout information.

## Returns

Returns a payout object if a you provide a valid identifier. raises [An error](https://docs.stripe.com/api/payouts/retrieve.md#errors) occurs otherwise.

```curl
curl https://api.stripe.com/v1/payouts/po_1OaFDbEcg9tTZuTgNYmX0PKB \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe payouts retrieve po_1OaFDbEcg9tTZuTgNYmX0PKB
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

payout = client.v1.payouts.retrieve('po_1OaFDbEcg9tTZuTgNYmX0PKB')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

payout = client.v1.payouts.retrieve("po_1OaFDbEcg9tTZuTgNYmX0PKB")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$payout = $stripe->payouts->retrieve('po_1OaFDbEcg9tTZuTgNYmX0PKB', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PayoutRetrieveParams params = PayoutRetrieveParams.builder().build();

Payout payout =
  client.v1().payouts().retrieve("po_1OaFDbEcg9tTZuTgNYmX0PKB", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const payout = await stripe.payouts.retrieve('po_1OaFDbEcg9tTZuTgNYmX0PKB');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PayoutRetrieveParams{}
result, err := sc.V1Payouts.Retrieve(
  context.TODO(), "po_1OaFDbEcg9tTZuTgNYmX0PKB", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Payouts;
Payout payout = service.Get("po_1OaFDbEcg9tTZuTgNYmX0PKB");
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
  "metadata": {},
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