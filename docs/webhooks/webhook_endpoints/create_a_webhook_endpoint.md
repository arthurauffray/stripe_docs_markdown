# Create a webhook endpoint

A webhook endpoint must have a `url` and a list of `enabled_events`. You may optionally specify the Boolean `connect` parameter. If set to true, then a Connect webhook endpoint that notifies the specified `url` about events from all connected accounts is created; otherwise an account webhook endpoint that notifies the specified `url` only about events from your account is created. You can also create webhook endpoints in the [webhooks settings](https://dashboard.stripe.com/account/webhooks) section of the Dashboard.

## Returns

Returns the webhook endpoint object with the `secret` field populated.

## Parameters

- `enabled_events` (array of enums, required)
  The list of events to enable for this endpoint. You may specify `['*']` to enable all events, except those that require explicit selection.
Possible enum values:
  - `account.application.authorized`
    Occurs whenever a user authorizes an application. Sent to the related application only.

  - `account.application.deauthorized`
    Occurs whenever a user deauthorizes an application. Sent to the related application only.

  - `account.external_account.created`
    Occurs whenever an external account is created.

  - `account.external_account.deleted`
    Occurs whenever an external account is deleted.

  - `account.external_account.updated`
    Occurs whenever an external account is updated.

  - `account.updated`
    Occurs whenever an account status or property has changed.

  - `application_fee.created`
    Occurs whenever an application fee is created on a charge.

  - `application_fee.refund.updated`
    Occurs whenever an application fee refund is updated.

  - `application_fee.refunded`
    Occurs whenever an application fee is refunded, whether from refunding a charge or from [refunding the application fee directly](https://docs.stripe.com/api/webhook_endpoints/create.md#fee_refunds). This includes partial refunds.

  - `balance.available`
    Occurs whenever your Stripe balance has been updated (e.g., when a charge is available to be paid out). By default, Stripe automatically transfers funds in your balance to your bank account on a daily basis. This event is not fired for negative transactions.

  - `balance_settings.updated`
    Occurs whenever a balance settings status or property has changed.

  - `billing.alert.triggered`
    Occurs whenever your custom alert threshold is met.

  - `billing_portal.configuration.created`
    Occurs whenever a portal configuration is created.

  - `billing_portal.configuration.updated`
    Occurs whenever a portal configuration is updated.

  - `billing_portal.session.created`
    Occurs whenever a portal session is created.

  - `capability.updated`
    Occurs whenever a capability has new requirements or a new status.

  - `cash_balance.funds_available`
    Occurs whenever there is a positive remaining cash balance after Stripe automatically reconciles new funds into the cash balance. If you enabled manual reconciliation, this webhook will fire whenever there are new funds into the cash balance.

  - `charge.captured`
    Occurs whenever a previously uncaptured charge is captured.

  - `charge.dispute.closed`
    Occurs when a dispute is closed and the dispute status changes to `lost`, `warning_closed`, or `won`.

  - `charge.dispute.created`
    Occurs whenever a customer disputes a charge with their bank.

  - `charge.dispute.funds_reinstated`
    Occurs when funds are reinstated to your account after a dispute is closed. This includes [partially refunded payments](https://docs.stripe.com/disputes.md#disputes-on-partially-refunded-payments).

  - `charge.dispute.funds_withdrawn`
    Occurs when funds are removed from your account due to a dispute.

  - `charge.dispute.updated`
    Occurs when the dispute is updated (usually with evidence).

  - `charge.expired`
    Occurs whenever an uncaptured charge expires.

  - `charge.failed`
    Occurs whenever a failed charge attempt occurs.

  - `charge.pending`
    Occurs whenever a pending charge is created.

  - `charge.refund.updated`
    Occurs whenever a refund is updated on selected payment methods. For updates on all refunds, listen to `refund.updated` instead.

  - `charge.refunded`
    Occurs whenever a charge is refunded, including partial refunds. Listen to `refund.created` for information about the refund.

  - `charge.succeeded`
    Occurs whenever a charge is successful.

  - `charge.updated`
    Occurs whenever a charge description or metadata is updated, or upon an asynchronous capture.

  - `checkout.session.async_payment_failed`
    Occurs when a payment intent using a delayed payment method fails.

  - `checkout.session.async_payment_succeeded`
    Occurs when a payment intent using a delayed payment method finally succeeds.

  - `checkout.session.completed`
    Occurs when a Checkout Session has been successfully completed.

  - `checkout.session.expired`
    Occurs when a Checkout Session is expired.

  - `climate.order.canceled`
    Occurs when a Climate order is canceled.

  - `climate.order.created`
    Occurs when a Climate order is created.

  - `climate.order.delayed`
    Occurs when a Climate order is delayed.

  - `climate.order.delivered`
    Occurs when a Climate order is delivered.

  - `climate.order.product_substituted`
    Occurs when a Climate order’s product is substituted for another.

  - `climate.product.created`
    Occurs when a Climate product is created.

  - `climate.product.pricing_updated`
    Occurs when a Climate product is updated.

  - `coupon.created`
    Occurs whenever a coupon is created.

  - `coupon.deleted`
    Occurs whenever a coupon is deleted.

  - `coupon.updated`
    Occurs whenever a coupon is updated.

  - `credit_note.created`
    Occurs whenever a credit note is created.

  - `credit_note.updated`
    Occurs whenever a credit note is updated.

  - `credit_note.voided`
    Occurs whenever a credit note is voided.

  - `customer.created`
    Occurs whenever a new customer is created.

  - `customer.deleted`
    Occurs whenever a customer is deleted.

  - `customer.discount.created`
    Occurs whenever a coupon is attached to a customer.

  - `customer.discount.deleted`
    Occurs whenever a coupon is removed from a customer.

  - `customer.discount.updated`
    Occurs whenever a customer is switched from one coupon to another.

  - `customer.source.created`
    Occurs whenever a new source is created for a customer.

  - `customer.source.deleted`
    Occurs whenever a source is removed from a customer.

  - `customer.source.expiring`
    Occurs whenever a card or source will expire at the end of the month. This event only works with legacy integrations using Card or Source objects. If you use the PaymentMethod API, this event won’t occur.

  - `customer.source.updated`
    Occurs whenever a source’s details are changed.

  - `customer.subscription.created`
    Occurs whenever a customer is signed up for a new plan.

  - `customer.subscription.deleted`
    Occurs whenever a customer’s subscription ends.

  - `customer.subscription.paused`
    Occurs whenever a customer’s subscription is paused. Only applies when subscriptions enter `status=paused`, not when [payment collection](https://docs.stripe.com/billing/subscriptions/pause.md) is paused.

  - `customer.subscription.pending_update_applied`
    Occurs whenever a customer’s subscription’s pending update is applied, and the subscription is updated.

  - `customer.subscription.pending_update_expired`
    Occurs whenever a customer’s subscription’s pending update expires before the related invoice is paid.

  - `customer.subscription.resumed`
    Occurs whenever a customer’s subscription is no longer paused. Only applies when a `status=paused` subscription is [resumed](https://docs.stripe.com/api/subscriptions/resume.md), not when [payment collection](https://docs.stripe.com/billing/subscriptions/pause.md) is resumed.

  - `customer.subscription.trial_will_end`
    Occurs three days before a subscription’s trial period is scheduled to end, or when a trial is ended immediately (using `trial_end=now`).

  - `customer.subscription.updated`
    Occurs whenever a subscription changes (e.g., switching from one plan to another, or changing the status from trial to active).

  - `customer.tax_id.created`
    Occurs whenever a tax ID is created for a customer.

  - `customer.tax_id.deleted`
    Occurs whenever a tax ID is deleted from a customer.

  - `customer.tax_id.updated`
    Occurs whenever a customer’s tax ID is updated.

  - `customer.updated`
    Occurs whenever any property of a customer changes.

  - `customer_cash_balance_transaction.created`
    Occurs whenever a new customer cash balance transactions is created.

  - `entitlements.active_entitlement_summary.updated`
    Occurs whenever a customer’s entitlements change.

  - `file.created`
    Occurs whenever a new Stripe-generated file is available for your account.

  - `financial_connections.account.account_numbers_updated`
    Occurs when a Financial Connections account’s account numbers are updated.

  - `financial_connections.account.created`
    Occurs when a new Financial Connections account is created.

  - `financial_connections.account.deactivated`
    Occurs when a Financial Connections account’s status is updated from `active` to `inactive`.

  - `financial_connections.account.disconnected`
    Occurs when a Financial Connections account is disconnected.

  - `financial_connections.account.reactivated`
    Occurs when a Financial Connections account’s status is updated from `inactive` to `active`.

  - `financial_connections.account.refreshed_balance`
    Occurs when an Account’s `balance_refresh` status transitions from `pending` to either `succeeded` or `failed`.

  - `financial_connections.account.refreshed_ownership`
    Occurs when an Account’s `ownership_refresh` status transitions from `pending` to either `succeeded` or `failed`.

  - `financial_connections.account.refreshed_transactions`
    Occurs when an Account’s `transaction_refresh` status transitions from `pending` to either `succeeded` or `failed`.

  - `financial_connections.account.upcoming_account_number_expiry`
    Occurs when an Account’s tokenized account number is about to expire.

  - `identity.verification_session.canceled`
    Occurs whenever a VerificationSession is canceled

  - `identity.verification_session.created`
    Occurs whenever a VerificationSession is created

  - `identity.verification_session.processing`
    Occurs whenever a VerificationSession transitions to processing

  - `identity.verification_session.redacted`
    Occurs whenever a VerificationSession is redacted.

  - `identity.verification_session.requires_input`
    Occurs whenever a VerificationSession transitions to require user input

  - `identity.verification_session.verified`
    Occurs whenever a VerificationSession transitions to verified

  - `invoice.created`
    Occurs whenever a new invoice is created. To learn how webhooks can be used with this event, and how they can affect it, see [Using Webhooks with Subscriptions](https://docs.stripe.com/subscriptions/webhooks.md).

  - `invoice.deleted`
    Occurs whenever a draft invoice is deleted. Note: This event is not sent for [invoice previews](https://docs.stripe.com/api/invoices/create_preview.md).

  - `invoice.finalization_failed`
    Occurs whenever a draft invoice cannot be finalized. See the invoice’s [last finalization error](https://docs.stripe.com/api/invoices/object.md#invoice_object-last_finalization_error) for details.

  - `invoice.finalized`
    Occurs whenever a draft invoice is finalized and updated to be an open invoice.

  - `invoice.marked_uncollectible`
    Occurs whenever an invoice is marked uncollectible.

  - `invoice.overdue`
    Occurs X number of days after an invoice becomes due—where X is determined by Automations

  - `invoice.overpaid`
    Occurs when an invoice transitions to paid with a non-zero amount_overpaid.

  - `invoice.paid`
    Occurs whenever an invoice payment attempt succeeds or an invoice is marked as paid out-of-band.

  - `invoice.payment_action_required`
    Occurs whenever an invoice payment attempt requires further user action to complete.

  - `invoice.payment_attempt_required`
    Occurs when an invoice requires a payment using a payment method that cannot be processed by Stripe.

  - `invoice.payment_failed`
    Occurs whenever an invoice payment attempt fails, due to either a declined payment, including soft decline, or to the lack of a stored payment method.

  - `invoice.payment_succeeded`
    Occurs whenever an invoice payment attempt succeeds.

  - `invoice.sent`
    Occurs whenever an invoice email is sent out.

  - `invoice.upcoming`
    Occurs X number of days before a subscription is scheduled to create an invoice that is automatically charged—where X is determined by your [subscriptions settings](https://dashboard.stripe.com/account/billing/automatic). Note: The received `Invoice` object will not have an invoice ID.

  - `invoice.updated`
    Occurs whenever an invoice changes (e.g., the invoice amount).

  - `invoice.voided`
    Occurs whenever an invoice is voided.

  - `invoice.will_be_due`
    Occurs X number of days before an invoice becomes due—where X is determined by Automations

  - `invoice_payment.paid`
    Occurs when an InvoicePayment is successfully paid.

  - `invoiceitem.created`
    Occurs whenever an invoice item is created.

  - `invoiceitem.deleted`
    Occurs whenever an invoice item is deleted.

  - `issuing_authorization.created`
    Occurs whenever an authorization is created.

  - `issuing_authorization.request`
    Represents a synchronous request for authorization, see [Using your integration to handle authorization requests](https://docs.stripe.com/issuing/purchases/authorizations.md#authorization-handling).

  - `issuing_authorization.updated`
    Occurs whenever an authorization is updated.

  - `issuing_card.created`
    Occurs whenever a card is created.

  - `issuing_card.updated`
    Occurs whenever a card is updated.

  - `issuing_cardholder.created`
    Occurs whenever a cardholder is created.

  - `issuing_cardholder.updated`
    Occurs whenever a cardholder is updated.

  - `issuing_dispute.closed`
    Occurs whenever a dispute is won, lost or expired.

  - `issuing_dispute.created`
    Occurs whenever a dispute is created.

  - `issuing_dispute.funds_reinstated`
    Occurs whenever funds are reinstated to your account for an Issuing dispute.

  - `issuing_dispute.funds_rescinded`
    Occurs whenever funds are deducted from your account for an Issuing dispute.

  - `issuing_dispute.submitted`
    Occurs whenever a dispute is submitted.

  - `issuing_dispute.updated`
    Occurs whenever a dispute is updated.

  - `issuing_personalization_design.activated`
    Occurs whenever a personalization design is activated following the activation of the physical bundle that belongs to it.

  - `issuing_personalization_design.deactivated`
    Occurs whenever a personalization design is deactivated following the deactivation of the physical bundle that belongs to it.

  - `issuing_personalization_design.rejected`
    Occurs whenever a personalization design is rejected by design review.

  - `issuing_personalization_design.updated`
    Occurs whenever a personalization design is updated.

  - `issuing_token.created`
    Occurs whenever an issuing digital wallet token is created.

  - `issuing_token.updated`
    Occurs whenever an issuing digital wallet token is updated.

  - `issuing_transaction.created`
    Occurs whenever an issuing transaction is created.

  - `issuing_transaction.purchase_details_receipt_updated`
    Occurs whenever an issuing transaction is updated with receipt data.

  - `issuing_transaction.updated`
    Occurs whenever an issuing transaction is updated.

  - `mandate.updated`
    Occurs whenever a Mandate is updated.

  - `payment_intent.amount_capturable_updated`
    Occurs when a PaymentIntent has funds to be captured. Check the `amount_capturable` property on the PaymentIntent to determine the amount that can be captured. You may capture the PaymentIntent with an `amount_to_capture` value up to the specified amount. [Learn more about capturing PaymentIntents.](https://docs.stripe.com/api/payment_intents/capture.md)

  - `payment_intent.canceled`
    Occurs when a PaymentIntent is canceled.

  - `payment_intent.created`
    Occurs when a new PaymentIntent is created.

  - `payment_intent.partially_funded`
    Occurs when funds are applied to a customer_balance PaymentIntent and the ‘amount_remaining’ changes.

  - `payment_intent.payment_failed`
    Occurs when a PaymentIntent has failed the attempt to create a payment method or a payment.

  - `payment_intent.processing`
    Occurs when a PaymentIntent has started processing.

  - `payment_intent.requires_action`
    Occurs when a PaymentIntent transitions to requires_action state

  - `payment_intent.succeeded`
    Occurs when a PaymentIntent has successfully completed payment.

  - `payment_link.created`
    Occurs when a payment link is created.

  - `payment_link.updated`
    Occurs when a payment link is updated.

  - `payment_method.attached`
    Occurs whenever a new payment method is attached to a customer.

  - `payment_method.automatically_updated`
    Occurs whenever a payment method’s details are automatically updated by the network.

  - `payment_method.detached`
    Occurs whenever a payment method is detached from a customer.

  - `payment_method.updated`
    Occurs whenever a payment method is updated via the [PaymentMethod update API](https://docs.stripe.com/api/payment_methods/update.md).

  - `payout.canceled`
    Occurs whenever a payout is canceled.

  - `payout.created`
    Occurs whenever a payout is created.

  - `payout.failed`
    Occurs whenever a payout attempt fails.

  - `payout.paid`
    Occurs whenever a payout is *expected* to be available in the destination account. If the payout fails, a `payout.failed` notification is also sent, at a later time.

  - `payout.reconciliation_completed`
    Occurs whenever balance transactions paid out in an automatic payout can be queried.

  - `payout.updated`
    Occurs whenever a payout is updated.

  - `person.created`
    Occurs whenever a person associated with an account is created.

  - `person.deleted`
    Occurs whenever a person associated with an account is deleted.

  - `person.updated`
    Occurs whenever a person associated with an account is updated.

  - `plan.created`
    Occurs whenever a plan is created.

  - `plan.deleted`
    Occurs whenever a plan is deleted.

  - `plan.updated`
    Occurs whenever a plan is updated.

  - `price.created`
    Occurs whenever a price is created.

  - `price.deleted`
    Occurs whenever a price is deleted.

  - `price.updated`
    Occurs whenever a price is updated.

  - `product.created`
    Occurs whenever a product is created.

  - `product.deleted`
    Occurs whenever a product is deleted.

  - `product.updated`
    Occurs whenever a product is updated.

  - `promotion_code.created`
    Occurs whenever a promotion code is created.

  - `promotion_code.updated`
    Occurs whenever a promotion code is updated.

  - `quote.accepted`
    Occurs whenever a quote is accepted.

  - `quote.canceled`
    Occurs whenever a quote is canceled.

  - `quote.created`
    Occurs whenever a quote is created.

  - `quote.finalized`
    Occurs whenever a quote is finalized.

  - `radar.early_fraud_warning.created`
    Occurs whenever an early fraud warning is created.

  - `radar.early_fraud_warning.updated`
    Occurs whenever an early fraud warning is updated.

  - `refund.created`
    Occurs whenever a refund is created.

  - `refund.failed`
    Occurs whenever a refund has failed.

  - `refund.updated`
    Occurs whenever a refund is updated.

  - `reporting.report_run.failed`
    Occurs whenever a requested `ReportRun` failed to complete.

  - `reporting.report_run.succeeded`
    Occurs whenever a requested `ReportRun` completed successfully.

  - `reporting.report_type.updated`
    Occurs whenever a `ReportType` is updated (typically to indicate that a new day’s data has come available).

  - `review.closed`
    Occurs whenever a review is closed. The review’s `reason` field indicates why: `approved`, `disputed`, `refunded`, `refunded_as_fraud`, or `canceled`.

  - `review.opened`
    Occurs whenever a review is opened.

  - `setup_intent.canceled`
    Occurs when a SetupIntent is canceled.

  - `setup_intent.created`
    Occurs when a new SetupIntent is created.

  - `setup_intent.requires_action`
    Occurs when a SetupIntent is in requires_action state.

  - `setup_intent.setup_failed`
    Occurs when a SetupIntent has failed the attempt to setup a payment method.

  - `setup_intent.succeeded`
    Occurs when an SetupIntent has successfully setup a payment method.

  - `sigma.scheduled_query_run.created`
    Occurs whenever a Sigma scheduled query run finishes.

  - `source.canceled`
    Occurs whenever a source is canceled.

  - `source.chargeable`
    Occurs whenever a source transitions to chargeable.

  - `source.failed`
    Occurs whenever a source fails.

  - `source.mandate_notification`
    Occurs whenever a source mandate notification method is set to manual.

  - `source.refund_attributes_required`
    Occurs whenever the refund attributes are required on a receiver source to process a refund or a mispayment.

  - `source.transaction.created`
    Occurs whenever a source transaction is created.

  - `source.transaction.updated`
    Occurs whenever a source transaction is updated.

  - `subscription_schedule.aborted`
    Occurs whenever a subscription schedule is canceled due to the underlying subscription being canceled because of delinquency.

  - `subscription_schedule.canceled`
    Occurs whenever a subscription schedule is canceled.

  - `subscription_schedule.completed`
    Occurs whenever a new subscription schedule is completed.

  - `subscription_schedule.created`
    Occurs whenever a new subscription schedule is created.

  - `subscription_schedule.expiring`
    Occurs 7 days before a subscription schedule will expire.

  - `subscription_schedule.released`
    Occurs whenever a new subscription schedule is released.

  - `subscription_schedule.updated`
    Occurs whenever a subscription schedule is updated.

  - `tax.settings.updated`
    Occurs whenever tax settings is updated.

  - `tax_rate.created`
    Occurs whenever a new tax rate is created.

  - `tax_rate.updated`
    Occurs whenever a tax rate is updated.

  - `terminal.reader.action_failed`
    Occurs whenever an action sent to a Terminal reader failed.

  - `terminal.reader.action_succeeded`
    Occurs whenever an action sent to a Terminal reader was successful.

  - `terminal.reader.action_updated`
    Occurs whenever an action sent to a Terminal reader is updated.

  - `test_helpers.test_clock.advancing`
    Occurs whenever a test clock starts advancing.

  - `test_helpers.test_clock.created`
    Occurs whenever a test clock is created.

  - `test_helpers.test_clock.deleted`
    Occurs whenever a test clock is deleted.

  - `test_helpers.test_clock.internal_failure`
    Occurs whenever a test clock fails to advance its frozen time.

  - `test_helpers.test_clock.ready`
    Occurs whenever a test clock transitions to a ready status.

  - `topup.canceled`
    Occurs whenever a top-up is canceled.

  - `topup.created`
    Occurs whenever a top-up is created.

  - `topup.failed`
    Occurs whenever a top-up fails.

  - `topup.reversed`
    Occurs whenever a top-up is reversed.

  - `topup.succeeded`
    Occurs whenever a top-up succeeds.

  - `transfer.created`
    Occurs whenever a transfer is created.

  - `transfer.reversed`
    Occurs whenever a transfer is reversed, including partial reversals.

  - `transfer.updated`
    Occurs whenever a transfer’s description or metadata is updated.

- `url` (string, required)
  The URL of the webhook endpoint.

- `api_version` (string, optional)
  Events sent to this endpoint will be generated with this Stripe Version instead of your account’s default Stripe Version.

- `connect` (boolean, optional)
  Whether this endpoint should receive events from connected accounts (`true`), or from your account (`false`). Defaults to `false`.

- `description` (string, optional)
  An optional description of what the webhook is used for.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/webhook_endpoints \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "enabled_events[]"="charge.succeeded" \
  -d "enabled_events[]"="charge.failed" \
  --data-urlencode url="https://example.com/my/webhook/endpoint"
```

```cli
stripe webhook_endpoints create  \
  -d "enabled_events[0]"="charge.succeeded" \
  -d "enabled_events[1]"="charge.failed" \
  --url="https://example.com/my/webhook/endpoint"
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

webhook_endpoint = client.v1.webhook_endpoints.create({
  enabled_events: ['charge.succeeded', 'charge.failed'],
  url: 'https://example.com/my/webhook/endpoint',
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

webhook_endpoint = client.v1.webhook_endpoints.create({
  "enabled_events": ["charge.succeeded", "charge.failed"],
  "url": "https://example.com/my/webhook/endpoint",
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$webhookEndpoint = $stripe->webhookEndpoints->create([
  'enabled_events' => ['charge.succeeded', 'charge.failed'],
  'url' => 'https://example.com/my/webhook/endpoint',
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

WebhookEndpointCreateParams params =
  WebhookEndpointCreateParams.builder()
    .addEnabledEvent(WebhookEndpointCreateParams.EnabledEvent.CHARGE__SUCCEEDED)
    .addEnabledEvent(WebhookEndpointCreateParams.EnabledEvent.CHARGE__FAILED)
    .setUrl("https://example.com/my/webhook/endpoint")
    .build();

WebhookEndpoint webhookEndpoint = client.v1().webhookEndpoints().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const webhookEndpoint = await stripe.webhookEndpoints.create({
  enabled_events: ['charge.succeeded', 'charge.failed'],
  url: 'https://example.com/my/webhook/endpoint',
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.WebhookEndpointCreateParams{
  EnabledEvents: []*string{
    stripe.String("charge.succeeded"),
    stripe.String("charge.failed"),
  },
  URL: stripe.String("https://example.com/my/webhook/endpoint"),
}
result, err := sc.V1WebhookEndpoints.Create(context.TODO(), params)
```

```dotnet
var options = new WebhookEndpointCreateOptions
{
    EnabledEvents = new List<string> { "charge.succeeded", "charge.failed" },
    Url = "https://example.com/my/webhook/endpoint",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.WebhookEndpoints;
WebhookEndpoint webhookEndpoint = service.Create(options);
```

### Response

```json
{
  "id": "we_1Mr5jULkdIwHu7ix1ibLTM0x",
  "object": "webhook_endpoint",
  "api_version": null,
  "application": null,
  "created": 1680122196,
  "description": null,
  "enabled_events": [
    "charge.succeeded",
    "charge.failed"
  ],
  "livemode": false,
  "metadata": {},
  "secret": "whsec_wRNftLajMZNeslQOP6vEPm4iVx5NlZ6z",
  "status": "enabled",
  "url": "https://example.com/my/webhook/endpoint"
}
```