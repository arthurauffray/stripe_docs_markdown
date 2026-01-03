# Capture a PaymentIntent

Capture the funds of an existing uncaptured PaymentIntent when its status is `requires_capture`.

Uncaptured PaymentIntents are cancelled a set number of days (7 by default) after their creation.

Learn more about [separate authorization and capture](https://docs.stripe.com/docs/payments/capture-later.md).

## Returns

Returns a PaymentIntent object with `status="succeeded"` if the PaymentIntent is capturable. Returns an error if the PaymentIntent isn’t capturable or if an invalid amount to capture is provided.

## Parameters

- `amount_details` (object, optional)
  Provides industry-specific information about the amount.

  - `amount_details.discount_amount` (integer, optional)
    The total discount applied on the transaction represented in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal). An integer greater than 0.

    This field is mutually exclusive with the `amount_details[line_items][#][discount_amount]` field.

  - `amount_details.line_items` (array of objects, optional)
    A list of line items, each containing information about a product in the PaymentIntent. There is a maximum of 200 line items.

    - `amount_details.line_items.product_name` (string, required)
      The product name of the line item. Required for L3 rates. At most 1024 characters long.

      For Cards, this field is truncated to 26 alphanumeric characters before being sent to the card networks. For Paypal, this field is truncated to 127 characters.

    - `amount_details.line_items.quantity` (integer, required)
      The quantity of items. Required for L3 rates. An integer greater than 0.

    - `amount_details.line_items.unit_cost` (integer, required)
      The unit cost of the line item represented in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal). Required for L3 rates. An integer greater than or equal to 0.

    - `amount_details.line_items.discount_amount` (integer, optional)
      The discount applied on this line item represented in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal). An integer greater than 0.

      This field is mutually exclusive with the `amount_details[discount_amount]` field.

    - `amount_details.line_items.payment_method_options` (object, optional)
      Payment method-specific information for line items.

      - `amount_details.line_items.payment_method_options.card` (object, optional)
        This sub-hash contains line item details that are specific to `card` payment method."

        - `amount_details.line_items.payment_method_options.card.commodity_code` (string, optional)
          Identifier that categorizes the items being purchased using a standardized commodity scheme such as (but not limited to) UNSPSC, NAICS, NAPCS, etc.

          The maximum length is 12 characters.

      - `amount_details.line_items.payment_method_options.card_present` (object, optional)
        This sub-hash contains line item details that are specific to `card_present` payment method."

        - `amount_details.line_items.payment_method_options.card_present.commodity_code` (string, optional)
          Identifier that categorizes the items being purchased using a standardized commodity scheme such as (but not limited to) UNSPSC, NAICS, NAPCS, etc.

          The maximum length is 12 characters.

      - `amount_details.line_items.payment_method_options.klarna` (object, optional)
        This sub-hash contains line item details that are specific to `klarna` payment method."

        - `amount_details.line_items.payment_method_options.klarna.image_url` (string, optional)
          URL to an image for the product. Max length, 4096 characters.

        - `amount_details.line_items.payment_method_options.klarna.product_url` (string, optional)
          URL to the product page. Max length, 4096 characters.

        - `amount_details.line_items.payment_method_options.klarna.reference` (string, optional)
          Unique reference for this line item to correlate it with your system’s internal records. The field is displayed in the Klarna Consumer App if passed.

          The maximum length is 255 characters.

        - `amount_details.line_items.payment_method_options.klarna.subscription_reference` (string, optional)
          Reference for the subscription this line item is for.

          The maximum length is 255 characters.

      - `amount_details.line_items.payment_method_options.paypal` (object, optional)
        This sub-hash contains line item details that are specific to `paypal` payment method."

        - `amount_details.line_items.payment_method_options.paypal.category` (enum, optional)
          Type of the line item.
Possible enum values:
          - `digital_goods`
            Goods that are stored, delivered, and used in their electronic format.

          - `donation`
            A contribution or gift for which no good or service is exchanged, usually to a not for profit organization.

          - `physical_goods`
            A tangible item that can be shipped with proof of delivery.

        - `amount_details.line_items.payment_method_options.paypal.description` (string, optional)
          Description of the line item.

          The maximum length is 127 characters.

        - `amount_details.line_items.payment_method_options.paypal.sold_by` (string, optional)
          The Stripe account ID of the connected account that sells the item.

          The maximum length is 127 characters.

    - `amount_details.line_items.product_code` (string, optional)
      The product code of the line item, such as an SKU. Required for L3 rates. At most 12 characters long.

      The maximum length is 12 characters.

    - `amount_details.line_items.tax` (object, optional)
      Contains information about the tax on the item.

      - `amount_details.line_items.tax.total_tax_amount` (integer, required)
        The total amount of tax on a single line item represented in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal). Required for L3 rates. An integer greater than or equal to 0.

        This field is mutually exclusive with the `amount_details[tax][total_tax_amount]` field.

    - `amount_details.line_items.unit_of_measure` (string, optional)
      A unit of measure for the line item, such as gallons, feet, meters, etc.

      The maximum length is 12 characters.

  - `amount_details.shipping` (object, optional)
    Contains information about the shipping portion of the amount.

    - `amount_details.shipping.amount` (integer, optional)
      If a physical good is being shipped, the cost of shipping represented in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal). An integer greater than or equal to 0.

    - `amount_details.shipping.from_postal_code` (string, optional)
      If a physical good is being shipped, the postal code of where it is being shipped from. At most 10 alphanumeric characters long, hyphens are allowed.

      The maximum length is 10 characters.

    - `amount_details.shipping.to_postal_code` (string, optional)
      If a physical good is being shipped, the postal code of where it is being shipped to. At most 10 alphanumeric characters long, hyphens are allowed.

      The maximum length is 10 characters.

  - `amount_details.tax` (object, optional)
    Contains information about the tax portion of the amount.

    - `amount_details.tax.total_tax_amount` (integer, required)
      The total amount of tax on the transaction represented in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal). Required for L2 rates. An integer greater than or equal to 0.

      This field is mutually exclusive with the `amount_details[line_items][#][tax][total_tax_amount]` field.

- `amount_to_capture` (integer, optional)
  The amount to capture from the PaymentIntent, which must be less than or equal to the original amount. Defaults to the full `amount_capturable` if it’s not provided.

- `application_fee_amount` (integer, optional)
  The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner’s Stripe account. The amount of the application fee collected will be capped at the total amount captured. For more information, see the PaymentIntents [use case for connected accounts](https://docs.stripe.com/docs/payments/connected-accounts.md).

- `final_capture` (boolean, optional)
  Defaults to `true`. When capturing a PaymentIntent, setting `final_capture` to `false` notifies Stripe to not release the remaining uncaptured funds to make sure that they’re captured in future requests. You can only use this setting when [multicapture](https://docs.stripe.com/docs/payments/multicapture.md) is available for PaymentIntents.

- `hooks` (object, optional)
  Automations to be run during the PaymentIntent lifecycle

  - `hooks.inputs` (object, optional)
    Arguments passed in automations

    - `hooks.inputs.tax` (object, optional)
      Tax arguments for automations

      - `hooks.inputs.tax.calculation` (string, required)
        The [TaxCalculation](https://docs.stripe.com/docs/api/tax/calculations.md) id

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `payment_details` (object, optional)
  Provides industry-specific information about the charge.

  - `payment_details.customer_reference` (string, optional)
    A unique value to identify the customer. This field is available only for card payments.

    This field is truncated to 25 alphanumeric characters, excluding spaces, before being sent to card networks.

  - `payment_details.order_reference` (string, optional)
    A unique value assigned by the business to identify the transaction. Required for L2 and L3 rates.

    Required when the Payment Method Types array contains `card`, including when [automatic_payment_methods.enabled](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-automatic_payment_methods-enabled) is set to `true`.

    For Cards, this field is truncated to 25 alphanumeric characters, excluding spaces, before being sent to card networks. For Klarna, this field is truncated to 255 characters and is visible to customers when they view the order in the Klarna app.

- `statement_descriptor` (string, optional)
  Text that appears on the customer’s statement as the statement descriptor for a non-card charge. This value overrides the account’s default statement descriptor. For information about requirements, including the 22-character limit, see [the Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors.md).

  Setting this value for a card charge returns an error. For card charges, set the [statement_descriptor_suffix](https://docs.stripe.com/get-started/account/statement-descriptors.md#dynamic) instead.

- `statement_descriptor_suffix` (string, optional)
  Provides information about a card charge. Concatenated to the account’s [statement descriptor prefix](https://docs.stripe.com/get-started/account/statement-descriptors.md#static) to form the complete statement descriptor that appears on the customer’s statement.

- `transfer_data` (object, optional)
  The parameters that you can use to automatically create a transfer after the payment is captured. Learn more about the [use case for connected accounts](https://docs.stripe.com/docs/payments/connected-accounts.md).

  - `transfer_data.amount` (integer, optional)
    The amount that will be transferred automatically when a charge succeeds.

```curl
curl -X POST https://api.stripe.com/v1/payment_intents/pi_3MrPBM2eZvKYlo2C1TEMacFD/capture \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe payment_intents capture pi_3MrPBM2eZvKYlo2C1TEMacFD
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

payment_intent = client.v1.payment_intents.capture('pi_3MrPBM2eZvKYlo2C1TEMacFD')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

payment_intent = client.v1.payment_intents.capture("pi_3MrPBM2eZvKYlo2C1TEMacFD")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentIntent = $stripe->paymentIntents->capture('pi_3MrPBM2eZvKYlo2C1TEMacFD', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PaymentIntentCaptureParams params = PaymentIntentCaptureParams.builder().build();

PaymentIntent paymentIntent =
  client.v1().paymentIntents().capture("pi_3MrPBM2eZvKYlo2C1TEMacFD", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.capture(
  'pi_3MrPBM2eZvKYlo2C1TEMacFD'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PaymentIntentCaptureParams{}
result, err := sc.V1PaymentIntents.Capture(
  context.TODO(), "pi_3MrPBM2eZvKYlo2C1TEMacFD", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.PaymentIntents;
PaymentIntent paymentIntent = service.Capture("pi_3MrPBM2eZvKYlo2C1TEMacFD");
```

### Response

```json
{
  "id": "pi_3MrPBM2eZvKYlo2C1TEMacFD",
  "object": "payment_intent",
  "amount": 1000,
  "amount_capturable": 0,
  "amount_details": {
    "tip": {}
  },
  "amount_received": 1000,
  "application": null,
  "application_fee_amount": null,
  "automatic_payment_methods": null,
  "canceled_at": null,
  "cancellation_reason": null,
  "capture_method": "automatic",
  "client_secret": "pi_3MrPBM2eZvKYlo2C1TEMacFD_secret_9J35eTzWlxVmfbbQhmkNbewuL",
  "confirmation_method": "automatic",
  "created": 1524505326,
  "currency": "usd",
  "customer": null,
  "description": "One blue fish",
  "last_payment_error": null,
  "latest_charge": "ch_1EXUPv2eZvKYlo2CStIqOmbY",
  "livemode": false,
  "metadata": {},
  "next_action": null,
  "on_behalf_of": null,
  "payment_method": "pm_1EXUPv2eZvKYlo2CUkqZASBe",
  "payment_method_options": {},
  "payment_method_types": [
    "card"
  ],
  "processing": null,
  "receipt_email": null,
  "redaction": null,
  "review": null,
  "setup_future_usage": null,
  "shipping": null,
  "statement_descriptor": null,
  "statement_descriptor_suffix": null,
  "status": "succeeded",
  "transfer_data": null,
  "transfer_group": null
}
```