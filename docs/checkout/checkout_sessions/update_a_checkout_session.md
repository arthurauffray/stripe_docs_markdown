# Update a Checkout Session

Updates a Checkout Session object.

Related guide: [Dynamically update Checkout](https://docs.stripe.com/payments/checkout/dynamic-updates.md)

## Returns

Returns a Checkout Session object.

## Parameters

- `collected_information` (object, optional)
  Information about the customer collected within the Checkout Session. Can only be set when updating `embedded` or `custom` sessions.

  - `collected_information.shipping_details` (object, optional)
    The shipping details to apply to this Session.

    - `collected_information.shipping_details.address` (object, required)
      The address of the customer

      - `collected_information.shipping_details.address.country` (string, required)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `collected_information.shipping_details.address.line1` (string, required)
        Address line 1, such as the street, PO Box, or company name.

      - `collected_information.shipping_details.address.city` (string, optional)
        City, district, suburb, town, or village.

      - `collected_information.shipping_details.address.line2` (string, optional)
        Address line 2, such as the apartment, suite, unit, or building.

      - `collected_information.shipping_details.address.postal_code` (string, optional)
        ZIP or postal code.

      - `collected_information.shipping_details.address.state` (string, optional)
        State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

    - `collected_information.shipping_details.name` (string, required)
      The name of customer

      The maximum length is 255 characters.

- `line_items` (array of objects, optional)
  A list of items the customer is purchasing.

  When updating line items, you must retransmit the entire array of line items.

  To retain an existing line item, specify its `id`.

  To update an existing line item, specify its `id` along with the new values of the fields to update.

  To add a new line item, specify one of `price` or `price_data` and `quantity`.

  To remove an existing line item, omit the line item’s ID from the retransmitted array.

  To reorder a line item, specify it at the desired position in the retransmitted array.

  - `line_items.adjustable_quantity` (object, optional)
    When set, provides configuration for this item’s quantity to be adjusted by the customer during Checkout.

    - `line_items.adjustable_quantity.enabled` (boolean, required)
      Set to true if the quantity can be adjusted to any positive integer. Setting to false will remove any previously specified constraints on quantity.

    - `line_items.adjustable_quantity.maximum` (integer, optional)
      The maximum quantity the customer can purchase for the Checkout Session. By default this value is 99. You can specify a value up to 999999.

    - `line_items.adjustable_quantity.minimum` (integer, optional)
      The minimum quantity the customer must purchase for the Checkout Session. By default this value is 0.

  - `line_items.id` (string, optional)
    ID of an existing line item.

  - `line_items.metadata` (object, optional)
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

  - `line_items.price` (string, required conditionally)
    The ID of the [Price](https://docs.stripe.com/docs/api/prices.md). One of `price` or `price_data` is required when creating a new line item.

  - `line_items.price_data` (object, required conditionally)
    Data used to generate a new [Price](https://docs.stripe.com/docs/api/prices.md) object inline. One of `price` or `price_data` is required when creating a new line item.

    - `line_items.price_data.currency` (enum, required)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

    - `line_items.price_data.product` (string, required conditionally)
      The ID of the [Product](https://docs.stripe.com/api/products.md) that this [Price](https://docs.stripe.com/api/prices.md) will belong to. One of `product` or `product_data` is required.

    - `line_items.price_data.product_data` (object, required conditionally)
      Data used to generate a new [Product](https://docs.stripe.com/api/products.md) object inline. One of `product` or `product_data` is required.

      - `line_items.price_data.product_data.name` (string, required)
        The product’s name, meant to be displayable to the customer.

      - `line_items.price_data.product_data.description` (string, optional)
        The product’s description, meant to be displayable to the customer. Use this field to optionally store a long form explanation of the product being sold for your own rendering purposes.

      - `line_items.price_data.product_data.images` (array of strings, optional)
        A list of up to 8 URLs of images for this product, meant to be displayable to the customer.

      - `line_items.price_data.product_data.metadata` (object, optional)
        Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

      - `line_items.price_data.product_data.tax_code` (string, recommended if calculating taxes)
        A [tax code](https://docs.stripe.com/docs/tax/tax-categories.md) ID.

      - `line_items.price_data.product_data.unit_label` (string, optional)
        A label that represents units of this product. When set, this will be included in customers’ receipts, invoices, Checkout, and the customer portal.

        The maximum length is 12 characters.

    - `line_items.price_data.recurring` (object, optional)
      The recurring components of a price such as `interval` and `interval_count`.

      - `line_items.price_data.recurring.interval` (enum, required)
        Specifies billing frequency. Either `day`, `week`, `month` or `year`.
Possible enum values:
        - `day`
        - `month`
        - `week`
        - `year`

      - `line_items.price_data.recurring.interval_count` (integer, optional)
        The number of intervals between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of three years interval allowed (3 years, 36 months, or 156 weeks).

    - `line_items.price_data.tax_behavior` (enum, recommended if calculating taxes)
      Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
Possible enum values:
      - `exclusive`
      - `inclusive`
      - `unspecified`

    - `line_items.price_data.unit_amount` (integer, required conditionally)
      A non-negative integer in cents representing how much to charge. One of `unit_amount` or `unit_amount_decimal` is required.

    - `line_items.price_data.unit_amount_decimal` (string, required conditionally)
      Same as `unit_amount`, but accepts a decimal value in cents with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.

  - `line_items.quantity` (integer, required conditionally)
    The quantity of the line item being purchased. Quantity should not be defined when `recurring.usage_type=metered`.

  - `line_items.tax_rates` (array of strings, optional)
    The [tax rates](https://docs.stripe.com/docs/api/tax_rates.md) which apply to this line item.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `shipping_options` (array of objects, optional)
  The shipping rate options to apply to this Session. Up to a maximum of 5.

  - `shipping_options.shipping_rate` (string, required unless shipping_rate_data is provided)
    The ID of the Shipping Rate to use for this shipping option.

  - `shipping_options.shipping_rate_data` (object, required unless shipping_rate is provided)
    Parameters to be passed to Shipping Rate creation for this shipping option.

    - `shipping_options.shipping_rate_data.display_name` (string, required)
      The name of the shipping rate, meant to be displayable to the customer. This will appear on CheckoutSessions.

      The maximum length is 100 characters.

    - `shipping_options.shipping_rate_data.delivery_estimate` (object, optional)
      The estimated range for how long shipping will take, meant to be displayable to the customer. This will appear on CheckoutSessions.

      - `shipping_options.shipping_rate_data.delivery_estimate.maximum` (object, optional)
        The upper bound of the estimated range. If empty, represents no upper bound i.e., infinite.

        - `shipping_options.shipping_rate_data.delivery_estimate.maximum.unit` (enum, required)
          A unit of time.
Possible enum values:
          - `business_day`
            The delivery estimate is in business days.

          - `day`
            The delivery estimate is in days.

          - `hour`
            The delivery estimate is in hours.

          - `month`
            The delivery estimate is in months.

          - `week`
            The delivery estimate is in weeks.

        - `shipping_options.shipping_rate_data.delivery_estimate.maximum.value` (integer, required)
          Must be greater than 0.

      - `shipping_options.shipping_rate_data.delivery_estimate.minimum` (object, optional)
        The lower bound of the estimated range. If empty, represents no lower bound.

        - `shipping_options.shipping_rate_data.delivery_estimate.minimum.unit` (enum, required)
          A unit of time.
Possible enum values:
          - `business_day`
            The delivery estimate is in business days.

          - `day`
            The delivery estimate is in days.

          - `hour`
            The delivery estimate is in hours.

          - `month`
            The delivery estimate is in months.

          - `week`
            The delivery estimate is in weeks.

        - `shipping_options.shipping_rate_data.delivery_estimate.minimum.value` (integer, required)
          Must be greater than 0.

    - `shipping_options.shipping_rate_data.fixed_amount` (object, optional)
      Describes a fixed amount to charge for shipping. Must be present if type is `fixed_amount`.

      - `shipping_options.shipping_rate_data.fixed_amount.amount` (integer, required)
        A non-negative integer in cents representing how much to charge.

      - `shipping_options.shipping_rate_data.fixed_amount.currency` (enum, required)
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

      - `shipping_options.shipping_rate_data.fixed_amount.currency_options` (object, optional)
        Shipping rates defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).

        - `shipping_options.shipping_rate_data.fixed_amount.currency_options.<currency>.amount` (integer, required)
          A non-negative integer in cents representing how much to charge.

        - `shipping_options.shipping_rate_data.fixed_amount.currency_options.<currency>.tax_behavior` (enum, recommended if calculating taxes)
          Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`.
Possible enum values:
          - `exclusive`
          - `inclusive`
          - `unspecified`

    - `shipping_options.shipping_rate_data.metadata` (object, optional)
      Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

    - `shipping_options.shipping_rate_data.tax_behavior` (enum, recommended if calculating taxes)
      Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`.
Possible enum values:
      - `exclusive`
      - `inclusive`
      - `unspecified`

    - `shipping_options.shipping_rate_data.tax_code` (string, recommended if calculating taxes)
      A [tax code](https://docs.stripe.com/docs/tax/tax-categories.md) ID. The Shipping tax code is `txcd_92010001`.

    - `shipping_options.shipping_rate_data.type` (enum, required)
      The type of calculation to use on the shipping rate.
Possible enum values:
      - `fixed_amount`
        The shipping rate is a fixed amount.

```curl
curl https://api.stripe.com/v1/checkout/sessions/cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
```

```cli
stripe checkout sessions update cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u \
  -d "metadata[order_id]"=6735
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

session = client.v1.checkout.sessions.update(
  'cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u',
  {metadata: {order_id: '6735'}},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

session = client.v1.checkout.sessions.update(
  "cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u",
  {"metadata": {"order_id": "6735"}},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$session = $stripe->checkout->sessions->update(
  'cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u',
  ['metadata' => ['order_id' => '6735']]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

SessionUpdateParams params =
  SessionUpdateParams.builder().putMetadata("order_id", "6735").build();

Session session =
  client.v1().checkout().sessions().update(
    "cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.update(
  'cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u',
  {
    metadata: {
      order_id: '6735',
    },
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CheckoutSessionUpdateParams{}
params.AddMetadata("order_id", "6735")
result, err := sc.V1CheckoutSessions.Update(
  context.TODO(), "cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u", params)
```

```dotnet
var options = new Stripe.Checkout.SessionUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Checkout.Sessions;
Stripe.Checkout.Session session = service.Update(
    "cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u",
    options);
```

### Response

```json
{
  "id": "cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u",
  "object": "checkout.session",
  "after_expiration": null,
  "allow_promotion_codes": null,
  "amount_subtotal": 2198,
  "amount_total": 2198,
  "automatic_tax": {
    "enabled": false,
    "liability": null,
    "status": null
  },
  "billing_address_collection": null,
  "cancel_url": null,
  "client_reference_id": null,
  "consent": null,
  "consent_collection": null,
  "created": 1679600215,
  "currency": "usd",
  "custom_fields": [],
  "custom_text": {
    "shipping_address": null,
    "submit": null
  },
  "customer": null,
  "customer_creation": "if_required",
  "customer_details": null,
  "customer_email": null,
  "expires_at": 1679686615,
  "invoice": null,
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
  "locale": null,
  "metadata": {
    "order_id": "6735"
  },
  "mode": "payment",
  "payment_intent": null,
  "payment_link": null,
  "payment_method_collection": "always",
  "payment_method_options": {},
  "payment_method_types": [
    "card"
  ],
  "payment_status": "unpaid",
  "phone_number_collection": {
    "enabled": false
  },
  "recovered_from": null,
  "setup_intent": null,
  "shipping_address_collection": null,
  "shipping_cost": null,
  "shipping_details": null,
  "shipping_options": [],
  "status": "open",
  "submit_type": null,
  "subscription": null,
  "success_url": "https://example.com/success",
  "total_details": {
    "amount_discount": 0,
    "amount_shipping": 0,
    "amount_tax": 0
  },
  "url": "https://checkout.stripe.com/c/pay/cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u#fidkdWxOYHwnPyd1blpxYHZxWjA0SDdPUW5JbmFMck1wMmx9N2BLZjFEfGRUNWhqTmJ%2FM2F8bUA2SDRySkFdUV81T1BSV0YxcWJcTUJcYW5rSzN3dzBLPUE0TzRKTTxzNFBjPWZEX1NKSkxpNTVjRjN8VHE0YicpJ2N3amhWYHdzYHcnP3F3cGApJ2lkfGpwcVF8dWAnPyd2bGtiaWBabHFgaCcpJ2BrZGdpYFVpZGZgbWppYWB3dic%2FcXdwYHgl"
}
```