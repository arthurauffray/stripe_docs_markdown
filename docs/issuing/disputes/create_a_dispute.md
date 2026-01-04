# Create a dispute

Creates an Issuing `Dispute` object. Individual pieces of evidence within the `evidence` object are optional at this point. Stripe only validates that required evidence is present during submission. Refer to [Dispute reasons and evidence](https://docs.stripe.com/docs/issuing/purchases/disputes.md#dispute-reasons-and-evidence) for more details about evidence requirements.

## Returns

Returns an Issuing `Dispute` object in `unsubmitted` status if creation succeeds.

## Parameters

- `amount` (integer, optional)
  The dispute amount in the card’s currency and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal). If not set, defaults to the full transaction amount.

- `evidence` (object, optional)
  Evidence provided for the dispute.

  - `evidence.canceled` (object, optional)
    Evidence provided when `reason` is ‘canceled’.

    - `evidence.canceled.additional_documentation` (string, optional)
      (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.

    - `evidence.canceled.canceled_at` (timestamp, optional)
      Date when order was canceled.

    - `evidence.canceled.cancellation_policy_provided` (boolean, optional)
      Whether the cardholder was provided with a cancellation policy.

    - `evidence.canceled.cancellation_reason` (string, optional)
      Reason for canceling the order.

    - `evidence.canceled.expected_at` (timestamp, optional)
      Date when the cardholder expected to receive the product.

    - `evidence.canceled.explanation` (string, optional)
      Explanation of why the cardholder is disputing this transaction.

    - `evidence.canceled.product_description` (string, optional)
      Description of the merchandise or service that was purchased.

    - `evidence.canceled.product_type` (enum, optional)
      Whether the product was a merchandise or service.
Possible enum values:
      - `merchandise`
        Tangible goods such as groceries and furniture.

      - `service`
        Intangible goods such as domain name registration, flights and lessons.

    - `evidence.canceled.return_status` (enum, optional)
      Result of cardholder’s attempt to return the product.
Possible enum values:
      - `merchant_rejected`
        The merchant rejected the return.

      - `successful`
        The merchant accepted the return.

    - `evidence.canceled.returned_at` (timestamp, optional)
      Date when the product was returned or attempted to be returned.

  - `evidence.duplicate` (object, optional)
    Evidence provided when `reason` is ‘duplicate’.

    - `evidence.duplicate.additional_documentation` (string, optional)
      (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.

    - `evidence.duplicate.card_statement` (string, optional)
      (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Copy of the card statement showing that the product had already been paid for.

    - `evidence.duplicate.cash_receipt` (string, optional)
      (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Copy of the receipt showing that the product had been paid for in cash.

    - `evidence.duplicate.check_image` (string, optional)
      (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Image of the front and back of the check that was used to pay for the product.

    - `evidence.duplicate.explanation` (string, optional)
      Explanation of why the cardholder is disputing this transaction.

    - `evidence.duplicate.original_transaction` (string, optional)
      Transaction (e.g., ipi_…) that the disputed transaction is a duplicate of. Of the two or more transactions that are copies of each other, this is original undisputed one.

  - `evidence.fraudulent` (object, optional)
    Evidence provided when `reason` is ‘fraudulent’.

    - `evidence.fraudulent.additional_documentation` (string, optional)
      (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.

    - `evidence.fraudulent.explanation` (string, optional)
      Explanation of why the cardholder is disputing this transaction.

  - `evidence.merchandise_not_as_described` (object, optional)
    Evidence provided when `reason` is ‘merchandise_not_as_described’.

    - `evidence.merchandise_not_as_described.additional_documentation` (string, optional)
      (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.

    - `evidence.merchandise_not_as_described.explanation` (string, optional)
      Explanation of why the cardholder is disputing this transaction.

    - `evidence.merchandise_not_as_described.received_at` (timestamp, optional)
      Date when the product was received.

    - `evidence.merchandise_not_as_described.return_description` (string, optional)
      Description of the cardholder’s attempt to return the product.

    - `evidence.merchandise_not_as_described.return_status` (enum, optional)
      Result of cardholder’s attempt to return the product.
Possible enum values:
      - `merchant_rejected`
        The merchant rejected the return.

      - `successful`
        The merchant accepted the return.

    - `evidence.merchandise_not_as_described.returned_at` (timestamp, optional)
      Date when the product was returned or attempted to be returned.

  - `evidence.no_valid_authorization` (object, optional)
    Evidence provided when `reason` is ‘no_valid_authorization’.

    - `evidence.no_valid_authorization.additional_documentation` (string, optional)
      (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.

    - `evidence.no_valid_authorization.explanation` (string, optional)
      Explanation of why the cardholder is disputing this transaction.

  - `evidence.not_received` (object, optional)
    Evidence provided when `reason` is ‘not_received’.

    - `evidence.not_received.additional_documentation` (string, optional)
      (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.

    - `evidence.not_received.expected_at` (timestamp, optional)
      Date when the cardholder expected to receive the product.

    - `evidence.not_received.explanation` (string, optional)
      Explanation of why the cardholder is disputing this transaction.

    - `evidence.not_received.product_description` (string, optional)
      Description of the merchandise or service that was purchased.

    - `evidence.not_received.product_type` (enum, optional)
      Whether the product was a merchandise or service.
Possible enum values:
      - `merchandise`
        Tangible goods such as groceries and furniture.

      - `service`
        Intangible goods such as domain name registration, flights and lessons.

  - `evidence.other` (object, optional)
    Evidence provided when `reason` is ‘other’.

    - `evidence.other.additional_documentation` (string, optional)
      (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.

    - `evidence.other.explanation` (string, optional)
      Explanation of why the cardholder is disputing this transaction.

    - `evidence.other.product_description` (string, optional)
      Description of the merchandise or service that was purchased.

    - `evidence.other.product_type` (enum, optional)
      Whether the product was a merchandise or service.
Possible enum values:
      - `merchandise`
        Tangible goods such as groceries and furniture.

      - `service`
        Intangible goods such as domain name registration, flights and lessons.

  - `evidence.reason` (enum, optional)
    The reason for filing the dispute. The evidence should be submitted in the field of the same name.
Possible enum values:
    - `canceled`
      Service or merchandise was canceled.

    - `duplicate`
      There were multiple copies of a charge for a single purchase, or the charge was paid by other means.

    - `fraudulent`
      The cardholder’s details were compromised and the cardholder claims to not have participated in the transaction.

    - `merchandise_not_as_described`
      The merchandise was not as described.

    - `no_valid_authorization`
      The merchant processed a transaction without first obtaining a correct and valid authorization approval.

    - `not_received`
      Merchandise or service was not received.

    - `other`
      All other types of disputes.

    - `service_not_as_described`
      The service was not as described.

  - `evidence.service_not_as_described` (object, optional)
    Evidence provided when `reason` is ‘service_not_as_described’.

    - `evidence.service_not_as_described.additional_documentation` (string, optional)
      (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.

    - `evidence.service_not_as_described.canceled_at` (timestamp, optional)
      Date when order was canceled.

    - `evidence.service_not_as_described.cancellation_reason` (string, optional)
      Reason for canceling the order.

    - `evidence.service_not_as_described.explanation` (string, optional)
      Explanation of why the cardholder is disputing this transaction.

    - `evidence.service_not_as_described.received_at` (timestamp, optional)
      Date when the product was received.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `transaction` (string, optional)
  The ID of the issuing transaction to create a dispute for. For transaction on Treasury FinancialAccounts, use `treasury.received_debit`.

```curl
curl https://api.stripe.com/v1/issuing/disputes \
  -u "<<YOUR_SECRET_KEY>>" \
  -d transaction=ipi_1MykXhFtDWhhyHE1UjsZZ3xQ \
  -d "evidence[reason]"=fraudulent \
  -d "evidence[fraudulent][explanation]"="This transaction is fraudulent."
```

```cli
stripe issuing disputes create  \
  --transaction=ipi_1MykXhFtDWhhyHE1UjsZZ3xQ \
  -d "evidence[reason]"=fraudulent \
  -d "evidence[fraudulent][explanation]"="This transaction is fraudulent."
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

dispute = client.v1.issuing.disputes.create({
  transaction: 'ipi_1MykXhFtDWhhyHE1UjsZZ3xQ',
  evidence: {
    reason: 'fraudulent',
    fraudulent: {explanation: 'This transaction is fraudulent.'},
  },
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

dispute = client.v1.issuing.disputes.create({
  "transaction": "ipi_1MykXhFtDWhhyHE1UjsZZ3xQ",
  "evidence": {
    "reason": "fraudulent",
    "fraudulent": {"explanation": "This transaction is fraudulent."},
  },
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$dispute = $stripe->issuing->disputes->create([
  'transaction' => 'ipi_1MykXhFtDWhhyHE1UjsZZ3xQ',
  'evidence' => [
    'reason' => 'fraudulent',
    'fraudulent' => ['explanation' => 'This transaction is fraudulent.'],
  ],
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

DisputeCreateParams params =
  DisputeCreateParams.builder()
    .setTransaction("ipi_1MykXhFtDWhhyHE1UjsZZ3xQ")
    .setEvidence(
      DisputeCreateParams.Evidence.builder()
        .setReason(DisputeCreateParams.Evidence.Reason.FRAUDULENT)
        .setFraudulent(
          DisputeCreateParams.Evidence.Fraudulent.builder()
            .setExplanation("This transaction is fraudulent.")
            .build()
        )
        .build()
    )
    .build();

Dispute dispute = client.v1().issuing().disputes().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const dispute = await stripe.issuing.disputes.create({
  transaction: 'ipi_1MykXhFtDWhhyHE1UjsZZ3xQ',
  evidence: {
    reason: 'fraudulent',
    fraudulent: {
      explanation: 'This transaction is fraudulent.',
    },
  },
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.IssuingDisputeCreateParams{
  Transaction: stripe.String("ipi_1MykXhFtDWhhyHE1UjsZZ3xQ"),
  Evidence: &stripe.IssuingDisputeCreateEvidenceParams{
    Reason: stripe.String(stripe.IssuingDisputeEvidenceReasonFraudulent),
    Fraudulent: &stripe.IssuingDisputeCreateEvidenceFraudulentParams{
      Explanation: stripe.String("This transaction is fraudulent."),
    },
  },
}
result, err := sc.V1IssuingDisputes.Create(context.TODO(), params)
```

```dotnet
var options = new Stripe.Issuing.DisputeCreateOptions
{
    Transaction = "ipi_1MykXhFtDWhhyHE1UjsZZ3xQ",
    Evidence = new Stripe.Issuing.DisputeEvidenceOptions
    {
        Reason = "fraudulent",
        Fraudulent = new Stripe.Issuing.DisputeEvidenceFraudulentOptions
        {
            Explanation = "This transaction is fraudulent.",
        },
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Issuing.Disputes;
Stripe.Issuing.Dispute dispute = service.Create(options);
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