# Update a dispute

When you get a dispute, contacting your customer is always the best first step. If that doesn’t work, you can submit evidence to help us resolve the dispute in your favor. You can do this in your [dashboard](https://dashboard.stripe.com/disputes), but if you prefer, you can use the API to submit evidence programmatically.

Depending on your dispute type, different evidence fields will give you a better chance of winning your dispute. To figure out which evidence fields to provide, see our [guide to dispute types](https://docs.stripe.com/docs/disputes/categories.md).

## Returns

Returns the dispute object.

## Parameters

- `evidence` (object, optional)
  Evidence to upload, to respond to a dispute. Updating any field in the hash will submit all fields in the hash for review. The combined character count of all fields is limited to 150,000.

  - `evidence.access_activity_log` (string, optional)
    Any server or activity logs showing proof that the customer accessed or downloaded the purchased digital product. This information should include IP addresses, corresponding timestamps, and any detailed recorded activity. Has a maximum character count of 20,000.

  - `evidence.billing_address` (string, optional)
    The billing address provided by the customer.

  - `evidence.cancellation_policy` (string, optional)
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Your subscription cancellation policy, as shown to the customer.

  - `evidence.cancellation_policy_disclosure` (string, optional)
    An explanation of how and when the customer was shown your refund policy prior to purchase. Has a maximum character count of 20,000.

  - `evidence.cancellation_rebuttal` (string, optional)
    A justification for why the customer’s subscription was not canceled. Has a maximum character count of 20,000.

  - `evidence.customer_communication` (string, optional)
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Any communication with the customer that you feel is relevant to your case. Examples include emails proving that the customer received the product or service, or demonstrating their use of or satisfaction with the product or service.

  - `evidence.customer_email_address` (string, optional)
    The email address of the customer.

  - `evidence.customer_name` (string, optional)
    The name of the customer.

  - `evidence.customer_purchase_ip` (string, optional)
    The IP address that the customer used when making the purchase.

  - `evidence.customer_signature` (string, optional)
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) A relevant document or contract showing the customer’s signature.

  - `evidence.duplicate_charge_documentation` (string, optional)
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Documentation for the prior charge that can uniquely identify the charge, such as a receipt, shipping label, work order, etc. This document should be paired with a similar document from the disputed payment that proves the two payments are separate.

  - `evidence.duplicate_charge_explanation` (string, optional)
    An explanation of the difference between the disputed charge versus the prior charge that appears to be a duplicate. Has a maximum character count of 20,000.

  - `evidence.duplicate_charge_id` (string, optional)
    The Stripe ID for the prior charge which appears to be a duplicate of the disputed charge.

  - `evidence.enhanced_evidence` (object, optional)
    Additional evidence for qualifying evidence programs.

    - `evidence.enhanced_evidence.visa_compelling_evidence_3` (object, optional)
      Evidence provided for Visa Compelling Evidence 3.0 evidence submission.

      - `evidence.enhanced_evidence.visa_compelling_evidence_3.disputed_transaction` (object, optional)
        Disputed transaction details for Visa Compelling Evidence 3.0 evidence submission.

        - `evidence.enhanced_evidence.visa_compelling_evidence_3.disputed_transaction.customer_account_id` (string, optional)
          User Account ID used to log into business platform. Must be recognizable by the user.

        - `evidence.enhanced_evidence.visa_compelling_evidence_3.disputed_transaction.customer_device_fingerprint` (string, optional)
          Unique identifier of the cardholder’s device derived from a combination of at least two hardware and software attributes. Must be at least 20 characters.

        - `evidence.enhanced_evidence.visa_compelling_evidence_3.disputed_transaction.customer_device_id` (string, optional)
          Unique identifier of the cardholder’s device such as a device serial number (e.g., International Mobile Equipment Identity [IMEI]). Must be at least 15 characters.

        - `evidence.enhanced_evidence.visa_compelling_evidence_3.disputed_transaction.customer_email_address` (string, optional)
          The email address of the customer.

        - `evidence.enhanced_evidence.visa_compelling_evidence_3.disputed_transaction.customer_purchase_ip` (string, optional)
          The IP address that the customer used when making the purchase.

        - `evidence.enhanced_evidence.visa_compelling_evidence_3.disputed_transaction.merchandise_or_services` (enum, optional)
          Categorization of disputed payment.
Possible enum values:
          - `merchandise`
            Disputed payment was for a physical product.

          - `services`
            Disputed payment was for a service.

        - `evidence.enhanced_evidence.visa_compelling_evidence_3.disputed_transaction.product_description` (string, optional)
          A description of the product or service that was sold.

        - `evidence.enhanced_evidence.visa_compelling_evidence_3.disputed_transaction.shipping_address` (object, optional)
          The address to which a physical product was shipped. All fields are required for Visa Compelling Evidence 3.0 evidence submission.

          - `evidence.enhanced_evidence.visa_compelling_evidence_3.disputed_transaction.shipping_address.city` (string, optional)
            City, district, suburb, town, or village.

          - `evidence.enhanced_evidence.visa_compelling_evidence_3.disputed_transaction.shipping_address.country` (string, optional)
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

          - `evidence.enhanced_evidence.visa_compelling_evidence_3.disputed_transaction.shipping_address.line1` (string, optional)
            Address line 1, such as the street, PO Box, or company name.

          - `evidence.enhanced_evidence.visa_compelling_evidence_3.disputed_transaction.shipping_address.line2` (string, optional)
            Address line 2, such as the apartment, suite, unit, or building.

          - `evidence.enhanced_evidence.visa_compelling_evidence_3.disputed_transaction.shipping_address.postal_code` (string, optional)
            ZIP or postal code.

          - `evidence.enhanced_evidence.visa_compelling_evidence_3.disputed_transaction.shipping_address.state` (string, optional)
            State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

      - `evidence.enhanced_evidence.visa_compelling_evidence_3.prior_undisputed_transactions` (array of objects, optional)
        List of exactly two prior undisputed transaction objects for Visa Compelling Evidence 3.0 evidence submission.

        - `evidence.enhanced_evidence.visa_compelling_evidence_3.prior_undisputed_transactions.charge` (string, required)
          Stripe charge ID for the Visa Compelling Evidence 3.0 eligible prior charge.

        - `evidence.enhanced_evidence.visa_compelling_evidence_3.prior_undisputed_transactions.customer_account_id` (string, optional)
          User Account ID used to log into business platform. Must be recognizable by the user.

        - `evidence.enhanced_evidence.visa_compelling_evidence_3.prior_undisputed_transactions.customer_device_fingerprint` (string, optional)
          Unique identifier of the cardholder’s device derived from a combination of at least two hardware and software attributes. Must be at least 20 characters.

        - `evidence.enhanced_evidence.visa_compelling_evidence_3.prior_undisputed_transactions.customer_device_id` (string, optional)
          Unique identifier of the cardholder’s device such as a device serial number (e.g., International Mobile Equipment Identity [IMEI]). Must be at least 15 characters.

        - `evidence.enhanced_evidence.visa_compelling_evidence_3.prior_undisputed_transactions.customer_email_address` (string, optional)
          The email address of the customer.

        - `evidence.enhanced_evidence.visa_compelling_evidence_3.prior_undisputed_transactions.customer_purchase_ip` (string, optional)
          The IP address that the customer used when making the purchase.

        - `evidence.enhanced_evidence.visa_compelling_evidence_3.prior_undisputed_transactions.product_description` (string, optional)
          A description of the product or service that was sold.

        - `evidence.enhanced_evidence.visa_compelling_evidence_3.prior_undisputed_transactions.shipping_address` (object, optional)
          The address to which a physical product was shipped. All fields are required for Visa Compelling Evidence 3.0 evidence submission.

          - `evidence.enhanced_evidence.visa_compelling_evidence_3.prior_undisputed_transactions.shipping_address.city` (string, optional)
            City, district, suburb, town, or village.

          - `evidence.enhanced_evidence.visa_compelling_evidence_3.prior_undisputed_transactions.shipping_address.country` (string, optional)
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

          - `evidence.enhanced_evidence.visa_compelling_evidence_3.prior_undisputed_transactions.shipping_address.line1` (string, optional)
            Address line 1, such as the street, PO Box, or company name.

          - `evidence.enhanced_evidence.visa_compelling_evidence_3.prior_undisputed_transactions.shipping_address.line2` (string, optional)
            Address line 2, such as the apartment, suite, unit, or building.

          - `evidence.enhanced_evidence.visa_compelling_evidence_3.prior_undisputed_transactions.shipping_address.postal_code` (string, optional)
            ZIP or postal code.

          - `evidence.enhanced_evidence.visa_compelling_evidence_3.prior_undisputed_transactions.shipping_address.state` (string, optional)
            State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

    - `evidence.enhanced_evidence.visa_compliance` (object, optional)
      Evidence provided for Visa compliance evidence submission.

      - `evidence.enhanced_evidence.visa_compliance.fee_acknowledged` (boolean, optional)
        A field acknowledging the fee incurred when countering a Visa compliance dispute. If this field is set to true, evidence can be submitted for the compliance dispute. Stripe collects a 500 USD (or local equivalent) amount to cover the network costs associated with resolving compliance disputes. Stripe refunds the 500 USD network fee if you win the dispute.

  - `evidence.product_description` (string, optional)
    A description of the product or service that was sold. Has a maximum character count of 20,000.

  - `evidence.receipt` (string, optional)
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Any receipt or message sent to the customer notifying them of the charge.

  - `evidence.refund_policy` (string, optional)
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Your refund policy, as shown to the customer.

  - `evidence.refund_policy_disclosure` (string, optional)
    Documentation demonstrating that the customer was shown your refund policy prior to purchase. Has a maximum character count of 20,000.

  - `evidence.refund_refusal_explanation` (string, optional)
    A justification for why the customer is not entitled to a refund. Has a maximum character count of 20,000.

  - `evidence.service_date` (string, optional)
    The date on which the customer received or began receiving the purchased service, in a clear human-readable format.

  - `evidence.service_documentation` (string, optional)
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Documentation showing proof that a service was provided to the customer. This could include a copy of a signed contract, work order, or other form of written agreement.

  - `evidence.shipping_address` (string, optional)
    The address to which a physical product was shipped. You should try to include as complete address information as possible.

  - `evidence.shipping_carrier` (string, optional)
    The delivery service that shipped a physical product, such as Fedex, UPS, USPS, etc. If multiple carriers were used for this purchase, please separate them with commas.

  - `evidence.shipping_date` (string, optional)
    The date on which a physical product began its route to the shipping address, in a clear human-readable format.

  - `evidence.shipping_documentation` (string, optional)
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Documentation showing proof that a product was shipped to the customer at the same address the customer provided to you. This could include a copy of the shipment receipt, shipping label, etc. It should show the customer’s full shipping address, if possible.

  - `evidence.shipping_tracking_number` (string, optional)
    The tracking number for a physical product, obtained from the delivery service. If multiple tracking numbers were generated for this purchase, please separate them with commas.

  - `evidence.uncategorized_file` (string, optional)
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Any additional evidence or statements.

  - `evidence.uncategorized_text` (string, optional)
    Any additional evidence or statements. Has a maximum character count of 20,000.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `submit` (boolean, optional)
  Whether to immediately submit evidence to the bank. If `false`, evidence is staged on the dispute. Staged evidence is visible in the API and Dashboard, and can be submitted to the bank by making another request with this attribute set to `true` (the default).

```curl
curl https://api.stripe.com/v1/disputes/du_1MtJUT2eZvKYlo2CNaw2HvEv \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
```

```cli
stripe disputes update du_1MtJUT2eZvKYlo2CNaw2HvEv \
  -d "metadata[order_id]"=6735
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

dispute = client.v1.disputes.update(
  'du_1MtJUT2eZvKYlo2CNaw2HvEv',
  {metadata: {order_id: '6735'}},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

dispute = client.v1.disputes.update(
  "du_1MtJUT2eZvKYlo2CNaw2HvEv",
  {"metadata": {"order_id": "6735"}},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$dispute = $stripe->disputes->update(
  'du_1MtJUT2eZvKYlo2CNaw2HvEv',
  ['metadata' => ['order_id' => '6735']]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

DisputeUpdateParams params =
  DisputeUpdateParams.builder().putMetadata("order_id", "6735").build();

Dispute dispute =
  client.v1().disputes().update("du_1MtJUT2eZvKYlo2CNaw2HvEv", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const dispute = await stripe.disputes.update(
  'du_1MtJUT2eZvKYlo2CNaw2HvEv',
  {
    metadata: {
      order_id: '6735',
    },
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.DisputeUpdateParams{}
params.AddMetadata("order_id", "6735")
result, err := sc.V1Disputes.Update(
  context.TODO(), "du_1MtJUT2eZvKYlo2CNaw2HvEv", params)
```

```dotnet
var options = new DisputeUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Disputes;
Dispute dispute = service.Update("du_1MtJUT2eZvKYlo2CNaw2HvEv", options);
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
  "metadata": {
    "order_id": "6735"
  },
  "payment_intent": null,
  "reason": "general",
  "status": "warning_needs_response"
}
```