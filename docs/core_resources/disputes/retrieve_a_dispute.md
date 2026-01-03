# Retrieve a dispute

Retrieves the dispute with the given ID.

## Returns

Returns a dispute if a valid dispute ID was provided. Raises [an error](https://docs.stripe.com/api/disputes/retrieve.md#errors) otherwise.

```curl
curl https://api.stripe.com/v1/disputes/du_1MtJUT2eZvKYlo2CNaw2HvEv \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe disputes retrieve du_1MtJUT2eZvKYlo2CNaw2HvEv
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

dispute = client.v1.disputes.retrieve('du_1MtJUT2eZvKYlo2CNaw2HvEv')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

dispute = client.v1.disputes.retrieve("du_1MtJUT2eZvKYlo2CNaw2HvEv")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$dispute = $stripe->disputes->retrieve('du_1MtJUT2eZvKYlo2CNaw2HvEv', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

DisputeRetrieveParams params = DisputeRetrieveParams.builder().build();

Dispute dispute =
  client.v1().disputes().retrieve("du_1MtJUT2eZvKYlo2CNaw2HvEv", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const dispute = await stripe.disputes.retrieve('du_1MtJUT2eZvKYlo2CNaw2HvEv');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.DisputeRetrieveParams{}
result, err := sc.V1Disputes.Retrieve(
  context.TODO(), "du_1MtJUT2eZvKYlo2CNaw2HvEv", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Disputes;
Dispute dispute = service.Get("du_1MtJUT2eZvKYlo2CNaw2HvEv");
```

### Response

```json
{
  "id": "du_1MtJUT2eZvKYlo2CNaw2HvEv",
  "object": "dispute",
  "amount": 1000,
  "balance_transactions": [],
  "charge": "ch_1AZtxr2eZvKYlo2CJDX8whov",
  "created": 1680651737,
  "currency": "usd",
  "evidence": {
    "access_activity_log": null,
    "billing_address": null,
    "cancellation_policy": null,
    "cancellation_policy_disclosure": null,
    "cancellation_rebuttal": null,
    "customer_communication": null,
    "customer_email_address": null,
    "customer_name": null,
    "customer_purchase_ip": null,
    "customer_signature": null,
    "duplicate_charge_documentation": null,
    "duplicate_charge_explanation": null,
    "duplicate_charge_id": null,
    "product_description": null,
    "receipt": null,
    "refund_policy": null,
    "refund_policy_disclosure": null,
    "refund_refusal_explanation": null,
    "service_date": null,
    "service_documentation": null,
    "shipping_address": null,
    "shipping_carrier": null,
    "shipping_date": null,
    "shipping_documentation": null,
    "shipping_tracking_number": null,
    "uncategorized_file": null,
    "uncategorized_text": null
  },
  "evidence_details": {
    "due_by": 1682294399,
    "has_evidence": false,
    "past_due": false,
    "submission_count": 0
  },
  "is_charge_refundable": true,
  "livemode": false,
  "metadata": {},
  "payment_intent": null,
  "reason": "general",
  "status": "warning_needs_response"
}
```