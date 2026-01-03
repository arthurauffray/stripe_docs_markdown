# Update a customer

Updates the specified customer by setting the values of the parameters passed. Any parameters not provided will be left unchanged.  For example, if you pass the **source** parameter, that becomes the customer’s active source (e.g., a card) to be used for all charges in the future. When you update a customer to a new valid card source by passing the **source** parameter: for each of the customer’s current subscriptions, if the subscription bills automatically and is in the `past_due` state, then the latest open invoice for the subscription with automatic collection enabled will be retried. This retry will not count as an automatic retry, and will not affect the next regularly scheduled payment for the invoice. Changing the **default\_source** for a customer will not trigger this behavior.

This request accepts mostly the same arguments as the customer creation call.

## Returns

Returns the customer object if the update succeeded. Raises [an error](https://docs.stripe.com/api/customers/update.md#errors) if update parameters are invalid (e.g. specifying an invalid coupon or an invalid source).

## Parameters

- `address` (object, required if calculating taxes)
  The customer’s address. Learn about [country-specific requirements for calculating tax](https://docs.stripe.com/invoicing/taxes.md?dashboard-or-api=dashboard#set-up-customer).

  - `address.city` (string, optional)
    City, district, suburb, town, or village.

  - `address.country` (string, optional)
    A freeform text field for the country. However, in order to activate some tax features, the format should be a two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

  - `address.line1` (string, optional)
    Address line 1, such as the street, PO Box, or company name.

  - `address.line2` (string, optional)
    Address line 2, such as the apartment, suite, unit, or building.

  - `address.postal_code` (string, optional)
    ZIP or postal code.

  - `address.state` (string, optional)
    State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

- `balance` (integer, optional)
  An integer amount in cents that represents the customer’s current balance, which affect the customer’s future invoices. A negative amount represents a credit that decreases the amount due on an invoice; a positive amount increases the amount due on an invoice.

- `business_name` (string, optional)
  The customer’s business name. This may be up to *150 characters*.

  The maximum length is 150 characters.

- `cash_balance` (object, optional)
  Balance information and default balance settings for this customer.

  - `cash_balance.settings` (object, optional)
    Settings controlling the behavior of the customer’s cash balance, such as reconciliation of funds received.

    - `cash_balance.settings.reconciliation_mode` (enum, optional)
      Controls how funds transferred by the customer are applied to payment intents and invoices. Valid options are `automatic`, `manual`, or `merchant_default`. For more information about these reconciliation modes, see [Reconciliation](https://docs.stripe.com/docs/payments/customer-balance/reconciliation.md).
Possible enum values:
      - `automatic`
      - `manual`
      - `merchant_default`

- `default_source` (string, optional)
  If you are using payment methods created via the PaymentMethods API, see the [invoice_settings.default_payment_method](https://docs.stripe.com/docs/api/customers/update.md#update_customer-invoice_settings-default_payment_method) parameter.

  Provide the ID of a payment source already attached to this customer to make it this customer’s default payment source.

  If you want to add a new payment source and make it the default, see the [source](https://docs.stripe.com/docs/api/customers/update.md#update_customer-source) property.

  The maximum length is 500 characters.

- `description` (string, optional)
  An arbitrary string that you can attach to a customer object. It is displayed alongside the customer in the dashboard.

- `email` (string, optional)
  Customer’s email address. It’s displayed alongside the customer in your dashboard and can be useful for searching and tracking. This may be up to *512 characters*.

  The maximum length is 512 characters.

- `individual_name` (string, optional)
  The customer’s full name. This may be up to *150 characters*.

  The maximum length is 150 characters.

- `invoice_prefix` (string, optional)
  The prefix for the customer used to generate unique invoice numbers. Must be 3–12 uppercase letters or numbers.

- `invoice_settings` (object, optional)
  Default invoice settings for this customer.

  - `invoice_settings.custom_fields` (array of objects, optional)
    The list of up to 4 default custom fields to be displayed on invoices for this customer. When updating, pass an empty string to remove previously-defined fields.

    - `invoice_settings.custom_fields.name` (string, required)
      The name of the custom field. This may be up to 40 characters.

      The maximum length is 40 characters.

    - `invoice_settings.custom_fields.value` (string, required)
      The value of the custom field. This may be up to 140 characters.

      The maximum length is 140 characters.

  - `invoice_settings.default_payment_method` (string, optional)
    ID of a payment method that’s attached to the customer, to be used as the customer’s default payment method for subscriptions and invoices.

  - `invoice_settings.footer` (string, optional)
    Default footer to be displayed on invoices for this customer.

  - `invoice_settings.rendering_options` (object, optional)
    Default options for invoice PDF rendering for this customer.

    - `invoice_settings.rendering_options.amount_tax_display` (enum, optional)
      How line-item prices and amounts will be displayed with respect to tax on invoice PDFs. One of `exclude_tax` or `include_inclusive_tax`. `include_inclusive_tax` will include inclusive tax (and exclude exclusive tax) in invoice PDF amounts. `exclude_tax` will exclude all tax (inclusive and exclusive alike) from invoice PDF amounts.
Possible enum values:
      - `exclude_tax`
      - `include_inclusive_tax`

    - `invoice_settings.rendering_options.template` (string, optional)
      ID of the invoice rendering template to use for future invoices.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `name` (string, optional)
  The customer’s full name or business name.

  The maximum length is 256 characters.

- `next_invoice_sequence` (integer, optional)
  The sequence to be used on the customer’s next invoice. Defaults to 1.

- `phone` (string, optional)
  The customer’s phone number.

  The maximum length is 20 characters.

- `preferred_locales` (array of strings, optional)
  Customer’s preferred languages, ordered by preference.

- `shipping` (object, optional)
  The customer’s shipping information. Appears on invoices emailed to this customer.

  - `shipping.address` (object, required)
    Customer shipping address.

    - `shipping.address.city` (string, optional)
      City, district, suburb, town, or village.

    - `shipping.address.country` (string, optional)
      A freeform text field for the country. However, in order to activate some tax features, the format should be a two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `shipping.address.line1` (string, optional)
      Address line 1, such as the street, PO Box, or company name.

    - `shipping.address.line2` (string, optional)
      Address line 2, such as the apartment, suite, unit, or building.

    - `shipping.address.postal_code` (string, optional)
      ZIP or postal code.

    - `shipping.address.state` (string, optional)
      State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

  - `shipping.name` (string, required)
    Customer name.

  - `shipping.phone` (string, optional)
    Customer phone (including extension).

- `source` (string, optional)
  When using payment sources created via the Token or Sources APIs, passing `source` will create a new source object, make it the new customer default source, and delete the old customer default if one exists. If you want to add additional sources instead of replacing the existing default, use the [card creation API](https://docs.stripe.com/docs/api.md#create_card). Whenever you attach a card to a customer, Stripe will automatically validate the card.

- `tax` (object, recommended if calculating taxes)
  Tax details about the customer.

  - `tax.ip_address` (string, optional)
    A recent IP address of the customer used for tax reporting and tax location inference. Stripe recommends updating the IP address when a new PaymentMethod is attached or the address field on the customer is updated. We recommend against updating this field more frequently since it could result in unexpected tax location/reporting outcomes.

  - `tax.validate_location` (enum, recommended if calculating taxes)
    A flag that indicates when Stripe should validate the customer tax location. Defaults to `auto`.
Possible enum values:
    - `auto`
      Validate the customer’s tax location immediately if it has automatic tax enabled subscriptions. **Recommended. Default.**

    - `deferred`
      Defer the validation of the customer’s tax location until needed, such as when Stripe Tax is calculating taxes on an Invoice. **Deprecated.**

    - `immediately`
      Validate the customer’s tax location immediately. An error is returned and the customer is not created/updated if the tax location is invalid.

- `tax_exempt` (enum, optional)
  The customer’s tax exemption. One of `none`, `exempt`, or `reverse`.
Possible enum values:
  - `exempt`
  - `none`
  - `reverse`

```curl
curl https://api.stripe.com/v1/customers/cus_NffrFeUfNV2Hib \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
```

```cli
stripe customers update cus_NffrFeUfNV2Hib \
  -d "metadata[order_id]"=6735
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

customer = client.v1.customers.update(
  'cus_NffrFeUfNV2Hib',
  {metadata: {order_id: '6735'}},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

customer = client.v1.customers.update(
  "cus_NffrFeUfNV2Hib",
  {"metadata": {"order_id": "6735"}},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$customer = $stripe->customers->update(
  'cus_NffrFeUfNV2Hib',
  ['metadata' => ['order_id' => '6735']]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CustomerUpdateParams params =
  CustomerUpdateParams.builder().putMetadata("order_id", "6735").build();

Customer customer = client.v1().customers().update("cus_NffrFeUfNV2Hib", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customer = await stripe.customers.update(
  'cus_NffrFeUfNV2Hib',
  {
    metadata: {
      order_id: '6735',
    },
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CustomerUpdateParams{}
params.AddMetadata("order_id", "6735")
result, err := sc.V1Customers.Update(context.TODO(), "cus_NffrFeUfNV2Hib", params)
```

```dotnet
var options = new CustomerUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Customers;
Customer customer = service.Update("cus_NffrFeUfNV2Hib", options);
```

### Response

```json
{
  "id": "cus_NffrFeUfNV2Hib",
  "object": "customer",
  "address": null,
  "balance": 0,
  "created": 1680893993,
  "currency": null,
  "default_source": null,
  "delinquent": false,
  "description": null,
  "email": "jennyrosen@example.com",
  "invoice_prefix": "0759376C",
  "invoice_settings": {
    "custom_fields": null,
    "default_payment_method": null,
    "footer": null,
    "rendering_options": null
  },
  "livemode": false,
  "metadata": {
    "order_id": "6735"
  },
  "name": "Jenny Rosen",
  "next_invoice_sequence": 1,
  "phone": null,
  "preferred_locales": [],
  "shipping": null,
  "tax_exempt": "none",
  "test_clock": null
}
```