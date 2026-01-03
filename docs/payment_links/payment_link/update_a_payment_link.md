# Update a payment link

Updates a payment link.

## Returns

Updated payment link.

## Parameters

- `active` (boolean, optional)
  Whether the payment link’s `url` is active. If `false`, customers visiting the URL will be shown a page saying that the link has been deactivated.

- `after_completion` (object, optional)
  Behavior after the purchase is complete.

  - `after_completion.type` (enum, required)
    The specified behavior after the purchase is complete. Either `redirect` or `hosted_confirmation`.
Possible enum values:
    - `hosted_confirmation`
      Displays a message on the hosted surface after the purchase is complete.

    - `redirect`
      Redirects the customer to the specified `url` after the purchase is complete.

  - `after_completion.hosted_confirmation` (object, optional)
    Configuration when `type=hosted_confirmation`.

    - `after_completion.hosted_confirmation.custom_message` (string, optional)
      A custom message to display to the customer after the purchase is complete.

      The maximum length is 500 characters.

  - `after_completion.redirect` (object, optional)
    Configuration when `type=redirect`.

    - `after_completion.redirect.url` (string, required)
      The URL the customer will be redirected to after the purchase is complete. You can embed `{CHECKOUT_SESSION_ID}` into the URL to have the `id` of the completed [checkout session](https://docs.stripe.com/docs/api/checkout/sessions/object.md#checkout_session_object-id) included.

- `allow_promotion_codes` (boolean, optional)
  Enables user redeemable promotion codes.

- `automatic_tax` (object, optional)
  Configuration for automatic tax collection.

  - `automatic_tax.enabled` (boolean, required)
    Set to `true` to [calculate tax automatically](https://docs.stripe.com/tax.md) using the customer’s location.

    Enabling this parameter causes the payment link to collect any billing address information necessary for tax calculation.

  - `automatic_tax.liability` (object, optional)
    The account that’s liable for tax. If set, the business address and tax registrations required to perform the tax calculation are loaded from this account. The tax transaction is returned in the report of the connected account.

    - `automatic_tax.liability.type` (enum, required)
      Type of the account referenced in the request.
Possible enum values:
      - `account`
        Indicates that the account being referenced is a connected account which is different from the account making the API request but related to it.

      - `self`
        Indicates that the account being referenced is the account making the API request.

    - `automatic_tax.liability.account` (string, required only if type is account)
      The connected account being referenced when `type` is `account`.

- `billing_address_collection` (enum, optional)
  Configuration for collecting the customer’s billing address. Defaults to `auto`.
Possible enum values:
  - `auto`
    Checkout will only collect the billing address when necessary. When using [automatic_tax](https://docs.stripe.com/docs/api/checkout/sessions/object.md#checkout_session_object-automatic_tax-enabled), Checkout will collect the minimum number of fields required for tax calculation.

  - `required`
    Checkout will always collect the customer’s billing address.

- `custom_fields` (array of objects, optional)
  Collect additional information from your customer using custom fields. Up to 3 fields are supported.

  - `custom_fields.key` (string, required)
    String of your choice that your integration can use to reconcile this field. Must be unique to this field, alphanumeric, and up to 200 characters.

    The maximum length is 200 characters.

  - `custom_fields.label` (object, required)
    The label for the field, displayed to the customer.

    - `custom_fields.label.custom` (string, required)
      Custom text for the label, displayed to the customer. Up to 50 characters.

      The maximum length is 50 characters.

    - `custom_fields.label.type` (enum, required)
      The type of the label.
Possible enum values:
      - `custom`
        Set a custom label for the field.

  - `custom_fields.type` (enum, required)
    The type of the field.
Possible enum values:
    - `dropdown`
      Provide a list of options for your customer to select.

    - `numeric`
      Collect a numbers-only field from your customer.

    - `text`
      Collect a string field from your customer.

  - `custom_fields.dropdown` (object, optional)
    Configuration for `type=dropdown` fields.

    - `custom_fields.dropdown.options` (array of objects, required)
      The options available for the customer to select. Up to 200 options allowed.

      - `custom_fields.dropdown.options.label` (string, required)
        The label for the option, displayed to the customer. Up to 100 characters.

        The maximum length is 100 characters.

      - `custom_fields.dropdown.options.value` (string, required)
        The value for this option, not displayed to the customer, used by your integration to reconcile the option selected by the customer. Must be unique to this option, alphanumeric, and up to 100 characters.

        The maximum length is 100 characters.

    - `custom_fields.dropdown.default_value` (string, optional)
      The value that will pre-fill the field on the payment page.Must match a `value` in the `options` array.

      The maximum length is 100 characters.

  - `custom_fields.numeric` (object, optional)
    Configuration for `type=numeric` fields.

    - `custom_fields.numeric.default_value` (string, optional)
      The value that will pre-fill the field on the payment page.

      The maximum length is 255 characters.

    - `custom_fields.numeric.maximum_length` (integer, optional)
      The maximum character length constraint for the customer’s input.

    - `custom_fields.numeric.minimum_length` (integer, optional)
      The minimum character length requirement for the customer’s input.

  - `custom_fields.optional` (boolean, optional)
    Whether the customer is required to complete the field before completing the Checkout Session. Defaults to `false`.

  - `custom_fields.text` (object, optional)
    Configuration for `type=text` fields.

    - `custom_fields.text.default_value` (string, optional)
      The value that will pre-fill the field on the payment page.

      The maximum length is 255 characters.

    - `custom_fields.text.maximum_length` (integer, optional)
      The maximum character length constraint for the customer’s input.

    - `custom_fields.text.minimum_length` (integer, optional)
      The minimum character length requirement for the customer’s input.

- `custom_text` (object, optional)
  Display additional text for your customers using custom text.

  - `custom_text.after_submit` (object, optional)
    Custom text that should be displayed after the payment confirmation button.

    - `custom_text.after_submit.message` (string, required)
      Text may be up to 1200 characters in length.

  - `custom_text.shipping_address` (object, optional)
    Custom text that should be displayed alongside shipping address collection.

    - `custom_text.shipping_address.message` (string, required)
      Text may be up to 1200 characters in length.

  - `custom_text.submit` (object, optional)
    Custom text that should be displayed alongside the payment confirmation button.

    - `custom_text.submit.message` (string, required)
      Text may be up to 1200 characters in length.

  - `custom_text.terms_of_service_acceptance` (object, optional)
    Custom text that should be displayed in place of the default terms of service agreement text.

    - `custom_text.terms_of_service_acceptance.message` (string, required)
      Text may be up to 1200 characters in length.

- `customer_creation` (enum, optional)
  Configures whether [checkout sessions](https://docs.stripe.com/docs/api/checkout/sessions.md) created by this payment link create a [Customer](https://docs.stripe.com/docs/api/customers.md).
Possible enum values:
  - `always`
    The Checkout Session will always create a [Customer](https://docs.stripe.com/docs/api/customers.md) when a Session confirmation is attempted.

  - `if_required`
    The Checkout Session will only create a [Customer](https://docs.stripe.com/docs/api/customers.md) if it is required for Session confirmation. Currently, only `subscription` mode Sessions and `payment` mode Sessions with [post-purchase invoices enabled](https://docs.stripe.com/docs/receipts.md?payment-ui=checkout#paid-invoices) require a Customer.

- `inactive_message` (string, optional)
  The custom message to be displayed to a customer when a payment link is no longer active.

  The maximum length is 500 characters.

- `invoice_creation` (object, optional)
  Generate a post-purchase Invoice for one-time payments.

  - `invoice_creation.enabled` (boolean, required)
    Whether the feature is enabled

  - `invoice_creation.invoice_data` (object, optional)
    Invoice PDF configuration.

    - `invoice_creation.invoice_data.account_tax_ids` (array of strings, optional)
      The account tax IDs associated with the invoice.

    - `invoice_creation.invoice_data.custom_fields` (array of objects, optional)
      Default custom fields to be displayed on invoices for this customer.

      - `invoice_creation.invoice_data.custom_fields.name` (string, required)
        The name of the custom field. This may be up to 40 characters.

        The maximum length is 40 characters.

      - `invoice_creation.invoice_data.custom_fields.value` (string, required)
        The value of the custom field. This may be up to 140 characters.

        The maximum length is 140 characters.

    - `invoice_creation.invoice_data.description` (string, optional)
      An arbitrary string attached to the object. Often useful for displaying to users.

    - `invoice_creation.invoice_data.footer` (string, optional)
      Default footer to be displayed on invoices for this customer.

    - `invoice_creation.invoice_data.issuer` (object, optional)
      The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.

      - `invoice_creation.invoice_data.issuer.type` (enum, required)
        Type of the account referenced in the request.
Possible enum values:
        - `account`
          Indicates that the account being referenced is a connected account which is different from the account making the API request but related to it.

        - `self`
          Indicates that the account being referenced is the account making the API request.

      - `invoice_creation.invoice_data.issuer.account` (string, required only if type is account)
        The connected account being referenced when `type` is `account`.

    - `invoice_creation.invoice_data.metadata` (object, optional)
      Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

    - `invoice_creation.invoice_data.rendering_options` (object, optional)
      Default options for invoice PDF rendering for this customer.

      - `invoice_creation.invoice_data.rendering_options.amount_tax_display` (enum, optional)
        How line-item prices and amounts will be displayed with respect to tax on invoice PDFs. One of `exclude_tax` or `include_inclusive_tax`. `include_inclusive_tax` will include inclusive tax (and exclude exclusive tax) in invoice PDF amounts. `exclude_tax` will exclude all tax (inclusive and exclusive alike) from invoice PDF amounts.
Possible enum values:
        - `exclude_tax`
        - `include_inclusive_tax`

      - `invoice_creation.invoice_data.rendering_options.template` (string, optional)
        ID of the invoice rendering template to use for this invoice.

- `line_items` (array of objects, optional)
  The line items representing what is being sold. Each line item represents an item being sold. Up to 20 line items are supported.

  - `line_items.id` (string, required)
    The ID of an existing line item on the payment link.

  - `line_items.adjustable_quantity` (object, optional)
    When set, provides configuration for this item’s quantity to be adjusted by the customer during checkout.

    - `line_items.adjustable_quantity.enabled` (boolean, required)
      Set to true if the quantity can be adjusted to any non-negative Integer.

    - `line_items.adjustable_quantity.maximum` (integer, optional)
      The maximum quantity the customer can purchase. By default this value is 99. You can specify a value up to 999999.

    - `line_items.adjustable_quantity.minimum` (integer, optional)
      The minimum quantity the customer can purchase. By default this value is 0. If there is only one item in the cart then that item’s quantity cannot go down to 0.

  - `line_items.quantity` (integer, optional)
    The quantity of the line item being purchased.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. Metadata associated with this Payment Link will automatically be copied to [checkout sessions](https://docs.stripe.com/docs/api/checkout/sessions.md) created by this payment link.

- `name_collection` (object, optional)
  Controls settings applied for collecting the customer’s name.

  - `name_collection.business` (object, optional)
    Controls settings applied for collecting the customer’s business name.

    - `name_collection.business.enabled` (boolean, required)
      Enable business name collection on the payment link. Defaults to `false`.

    - `name_collection.business.optional` (boolean, optional)
      Whether the customer is required to provide their business name before checking out. Defaults to `false`.

  - `name_collection.individual` (object, optional)
    Controls settings applied for collecting the customer’s individual name.

    - `name_collection.individual.enabled` (boolean, required)
      Enable individual name collection on the payment link. Defaults to `false`.

    - `name_collection.individual.optional` (boolean, optional)
      Whether the customer is required to provide their full name before checking out. Defaults to `false`.

- `payment_intent_data` (object, optional)
  A subset of parameters to be passed to PaymentIntent creation for Checkout Sessions in `payment` mode.

  - `payment_intent_data.description` (string, optional)
    An arbitrary string attached to the object. Often useful for displaying to users.

  - `payment_intent_data.metadata` (object, optional)
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that will declaratively set metadata on [Payment Intents](https://docs.stripe.com/docs/api/payment_intents.md) generated from this payment link. Unlike object-level metadata, this field is declarative. Updates will clear prior values.

  - `payment_intent_data.statement_descriptor` (string, optional)
    Text that appears on the customer’s statement as the statement descriptor for a non-card charge. This value overrides the account’s default statement descriptor. For information about requirements, including the 22-character limit, see [the Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors.md).

    Setting this value for a card charge returns an error. For card charges, set the [statement_descriptor_suffix](https://docs.stripe.com/get-started/account/statement-descriptors.md#dynamic) instead.

  - `payment_intent_data.statement_descriptor_suffix` (string, optional)
    Provides information about a card charge. Concatenated to the account’s [statement descriptor prefix](https://docs.stripe.com/get-started/account/statement-descriptors.md#static) to form the complete statement descriptor that appears on the customer’s statement.

  - `payment_intent_data.transfer_group` (string, optional)
    A string that identifies the resulting payment as part of a group. See the PaymentIntents [use case for connected accounts](https://docs.stripe.com/docs/connect/separate-charges-and-transfers.md) for details.

- `payment_method_collection` (enum, optional)
  Specify whether Checkout should collect a payment method. When set to `if_required`, Checkout will not collect a payment method when the total due for the session is 0.This may occur if the Checkout Session includes a free trial or a discount.

  Can only be set in `subscription` mode. Defaults to `always`.

  If you’d like information on how to collect a payment method outside of Checkout, read the guide on [configuring subscriptions with a free trial](https://docs.stripe.com/docs/payments/checkout/free-trials.md).
Possible enum values:
  - `always`
    The Checkout Session will always collect a PaymentMethod.

  - `if_required`
    The Checkout Session will only collect a PaymentMethod if there is an amount due.

- `payment_method_types` (array of enums, optional)
  The list of payment method types that customers can use. Pass an empty string to enable dynamic payment methods that use your [payment method settings](https://dashboard.stripe.com/settings/payment_methods).

- `phone_number_collection` (object, optional)
  Controls phone number collection settings during checkout.

  We recommend that you review your privacy policy and check with your legal contacts.

  - `phone_number_collection.enabled` (boolean, required)
    Set to `true` to enable phone number collection.

- `restrictions` (object, optional)
  Settings that restrict the usage of a payment link.

  - `restrictions.completed_sessions` (object, required)
    Configuration for the `completed_sessions` restriction type.

    - `restrictions.completed_sessions.limit` (integer, required)
      The maximum number of checkout sessions that can be completed for the `completed_sessions` restriction to be met.

- `shipping_address_collection` (object, optional)
  Configuration for collecting the customer’s shipping address.

  - `shipping_address_collection.allowed_countries` (array of enums, required)
    An array of two-letter ISO country codes representing which countries Checkout should provide as options for shipping locations.
Possible enum values:
    - `AC`
    - `AD`
    - `AE`
    - `AF`
    - `AG`
    - `AI`
    - `AL`
    - `AM`
    - `AO`
    - `AQ`
    - `AR`
    - `AT`
    - `AU`
    - `AW`
    - `AX`
    - `AZ`
    - `BA`
    - `BB`
    - `BD`
    - `BE`
    - `BF`
    - `BG`
    - `BH`
    - `BI`
    - `BJ`
    - `BL`
    - `BM`
    - `BN`
    - `BO`
    - `BQ`
    - `BR`
    - `BS`
    - `BT`
    - `BV`
    - `BW`
    - `BY`
    - `BZ`
    - `CA`
    - `CD`
    - `CF`
    - `CG`
    - `CH`
    - `CI`
    - `CK`
    - `CL`
    - `CM`
    - `CN`
    - `CO`
    - `CR`
    - `CV`
    - `CW`
    - `CY`
    - `CZ`
    - `DE`
    - `DJ`
    - `DK`
    - `DM`
    - `DO`
    - `DZ`
    - `EC`
    - `EE`
    - `EG`
    - `EH`
    - `ER`
    - `ES`
    - `ET`
    - `FI`
    - `FJ`
    - `FK`
    - `FO`
    - `FR`
    - `GA`
    - `GB`
    - `GD`
    - `GE`
    - `GF`
    - `GG`
    - `GH`
    - `GI`
    - `GL`
    - `GM`
    - `GN`
    - `GP`
    - `GQ`
    - `GR`
    - `GS`
    - `GT`
    - `GU`
    - `GW`
    - `GY`
    - `HK`
    - `HN`
    - `HR`
    - `HT`
    - `HU`
    - `ID`
    - `IE`
    - `IL`
    - `IM`
    - `IN`
    - `IO`
    - `IQ`
    - `IS`
    - `IT`
    - `JE`
    - `JM`
    - `JO`
    - `JP`
    - `KE`
    - `KG`
    - `KH`
    - `KI`
    - `KM`
    - `KN`
    - `KR`
    - `KW`
    - `KY`
    - `KZ`
    - `LA`
    - `LB`
    - `LC`
    - `LI`
    - `LK`
    - `LR`
    - `LS`
    - `LT`
    - `LU`
    - `LV`
    - `LY`
    - `MA`
    - `MC`
    - `MD`
    - `ME`
    - `MF`
    - `MG`
    - `MK`
    - `ML`
    - `MM`
    - `MN`
    - `MO`
    - `MQ`
    - `MR`
    - `MS`
    - `MT`
    - `MU`
    - `MV`
    - `MW`
    - `MX`
    - `MY`
    - `MZ`
    - `NA`
    - `NC`
    - `NE`
    - `NG`
    - `NI`
    - `NL`
    - `NO`
    - `NP`
    - `NR`
    - `NU`
    - `NZ`
    - `OM`
    - `PA`
    - `PE`
    - `PF`
    - `PG`
    - `PH`
    - `PK`
    - `PL`
    - `PM`
    - `PN`
    - `PR`
    - `PS`
    - `PT`
    - `PY`
    - `QA`
    - `RE`
    - `RO`
    - `RS`
    - `RU`
    - `RW`
    - `SA`
    - `SB`
    - `SC`
    - `SD`
    - `SE`
    - `SG`
    - `SH`
    - `SI`
    - `SJ`
    - `SK`
    - `SL`
    - `SM`
    - `SN`
    - `SO`
    - `SR`
    - `SS`
    - `ST`
    - `SV`
    - `SX`
    - `SZ`
    - `TA`
    - `TC`
    - `TD`
    - `TF`
    - `TG`
    - `TH`
    - `TJ`
    - `TK`
    - `TL`
    - `TM`
    - `TN`
    - `TO`
    - `TR`
    - `TT`
    - `TV`
    - `TW`
    - `TZ`
    - `UA`
    - `UG`
    - `US`
    - `UY`
    - `UZ`
    - `VA`
    - `VC`
    - `VE`
    - `VG`
    - `VN`
    - `VU`
    - `WF`
    - `WS`
    - `XK`
    - `YE`
    - `YT`
    - `ZA`
    - `ZM`
    - `ZW`
    - `ZZ`

- `submit_type` (enum, optional)
  Describes the type of transaction being performed in order to customize relevant text on the page, such as the submit button. Changing this value will also affect the hostname in the [url](https://docs.stripe.com/docs/api/payment_links/payment_links/object.md#url) property (example: `donate.stripe.com`).
Possible enum values:
  - `auto`
    Default value. `pay` will used in all scenarios

  - `book`
    Recommended when offering bookings. Submit button includes a ‘Book’ label and URLs use the `book.stripe.com` hostname

  - `donate`
    Recommended when accepting donations. Submit button includes a ‘Donate’ label and URLs use the `donate.stripe.com` hostname

  - `pay`
    Submit button includes a ‘Buy’ label and URLs use the `buy.stripe.com` hostname

  - `subscribe`
    Submit button includes a ‘Subscribe’ label and URLs use the `buy.stripe.com` hostname

- `subscription_data` (object, optional)
  When creating a subscription, the specified configuration data will be used. There must be at least one line item with a recurring price to use `subscription_data`.

  - `subscription_data.invoice_settings` (object, optional)
    All invoices will be billed using the specified settings.

    - `subscription_data.invoice_settings.issuer` (object, optional)
      The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.

      - `subscription_data.invoice_settings.issuer.type` (enum, required)
        Type of the account referenced in the request.
Possible enum values:
        - `account`
          Indicates that the account being referenced is a connected account which is different from the account making the API request but related to it.

        - `self`
          Indicates that the account being referenced is the account making the API request.

      - `subscription_data.invoice_settings.issuer.account` (string, required only if type is account)
        The connected account being referenced when `type` is `account`.

  - `subscription_data.metadata` (object, optional)
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that will declaratively set metadata on [Subscriptions](https://docs.stripe.com/docs/api/subscriptions.md) generated from this payment link. Unlike object-level metadata, this field is declarative. Updates will clear prior values.

  - `subscription_data.trial_period_days` (integer, optional)
    Integer representing the number of trial period days before the customer is charged for the first time. Has to be at least 1.

  - `subscription_data.trial_settings` (object, optional)
    Settings related to subscription trials.

    - `subscription_data.trial_settings.end_behavior` (object, required)
      Defines how the subscription should behave when the user’s free trial ends.

      - `subscription_data.trial_settings.end_behavior.missing_payment_method` (enum, required)
        Indicates how the subscription should change when the trial ends if the user did not provide a payment method.
Possible enum values:
        - `cancel`
          Cancel the subscription if a payment method is not attached when the trial ends.

        - `create_invoice`
          Create an invoice when the trial ends, even if the user did not set up a payment method.

        - `pause`
          Pause the subscription if a payment method is not attached when the trial ends.

- `tax_id_collection` (object, optional)
  Controls tax ID collection during checkout.

  - `tax_id_collection.enabled` (boolean, required)
    Enable tax ID collection during checkout. Defaults to `false`.

  - `tax_id_collection.required` (enum, optional)
    Describes whether a tax ID is required during checkout. Defaults to `never`.
Possible enum values:
    - `if_supported`
      A tax ID will be required if collection is [supported](https://docs.stripe.com/tax/checkout/tax-ids.md#supported-types) for the selected billing address country.

    - `never`
      Tax ID collection is never required.

```curl
curl https://api.stripe.com/v1/payment_links/plink_1MoC3ULkdIwHu7ixZjtGpVl2 \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
```

```cli
stripe payment_links update plink_1MoC3ULkdIwHu7ixZjtGpVl2 \
  -d "metadata[order_id]"=6735
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

payment_link = client.v1.payment_links.update(
  'plink_1MoC3ULkdIwHu7ixZjtGpVl2',
  {metadata: {order_id: '6735'}},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

payment_link = client.v1.payment_links.update(
  "plink_1MoC3ULkdIwHu7ixZjtGpVl2",
  {"metadata": {"order_id": "6735"}},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentLink = $stripe->paymentLinks->update(
  'plink_1MoC3ULkdIwHu7ixZjtGpVl2',
  ['metadata' => ['order_id' => '6735']]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PaymentLinkUpdateParams params =
  PaymentLinkUpdateParams.builder().putMetadata("order_id", "6735").build();

PaymentLink paymentLink =
  client.v1().paymentLinks().update("plink_1MoC3ULkdIwHu7ixZjtGpVl2", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentLink = await stripe.paymentLinks.update(
  'plink_1MoC3ULkdIwHu7ixZjtGpVl2',
  {
    metadata: {
      order_id: '6735',
    },
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PaymentLinkUpdateParams{}
params.AddMetadata("order_id", "6735")
result, err := sc.V1PaymentLinks.Update(
  context.TODO(), "plink_1MoC3ULkdIwHu7ixZjtGpVl2", params)
```

```dotnet
var options = new PaymentLinkUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.PaymentLinks;
PaymentLink paymentLink = service.Update("plink_1MoC3ULkdIwHu7ixZjtGpVl2", options);
```

### Response

```json
{
  "id": "plink_1MoC3ULkdIwHu7ixZjtGpVl2",
  "object": "payment_link",
  "active": true,
  "after_completion": {
    "hosted_confirmation": {
      "custom_message": null
    },
    "type": "hosted_confirmation"
  },
  "allow_promotion_codes": false,
  "application_fee_amount": null,
  "application_fee_percent": null,
  "automatic_tax": {
    "enabled": false,
    "liability": null
  },
  "billing_address_collection": "auto",
  "consent_collection": null,
  "currency": "usd",
  "custom_fields": [],
  "custom_text": {
    "shipping_address": null,
    "submit": null
  },
  "customer_creation": "if_required",
  "invoice_creation": {
    "enabled": false,
    "invoice_data": {
      "account_tax_ids": null,
      "custom_fields": null,
      "description": null,
      "footer": null,
      "issuer": null,
      "metadata": {},
      "rendering_options": null
    }
  },
  "livemode": false,
  "metadata": {
    "order_id": "6735"
  },
  "on_behalf_of": null,
  "payment_intent_data": null,
  "payment_method_collection": "always",
  "payment_method_types": null,
  "phone_number_collection": {
    "enabled": false
  },
  "shipping_address_collection": null,
  "shipping_options": [],
  "submit_type": "auto",
  "subscription_data": {
    "description": null,
    "invoice_settings": {
      "issuer": {
        "type": "self"
      }
    },
    "trial_period_days": null
  },
  "tax_id_collection": {
    "enabled": false
  },
  "transfer_data": null,
  "url": "https://buy.stripe.com/test_cN25nr0iZ7bUa7meUY"
}
```