# Create a quote

A quote models prices and services for a customer. Default options for `header`, `description`, `footer`, and `expires_at` can be set in the dashboard via the [quote template](https://dashboard.stripe.com/settings/billing/quote).

## Returns

Returns the quote object.

## Parameters

- `application_fee_amount` (integer, optional)
  The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner’s Stripe account. There cannot be any line items with recurring prices when using this field.

- `application_fee_percent` (float, optional)
  A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner’s Stripe account. There must be at least 1 line item with a recurring price to use this field.

- `automatic_tax` (object, optional)
  Settings for automatic tax lookup for this quote and resulting invoices and subscriptions.

  - `automatic_tax.enabled` (boolean, required)
    Controls whether Stripe will automatically compute tax on the resulting invoices or subscriptions as well as the quote itself.

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

- `collection_method` (enum, optional)
  Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay invoices at the end of the subscription cycle or at invoice finalization using the default payment method attached to the subscription or customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`.
Possible enum values:
  - `charge_automatically`
  - `send_invoice`

- `customer` (string, optional)
  The customer for which this quote belongs to. A customer is required before finalizing the quote. Once specified, it cannot be changed.

- `customer_account` (string, optional)
  The account for which this quote belongs to. A customer or account is required before finalizing the quote. Once specified, it cannot be changed.

- `default_tax_rates` (array of strings, optional)
  The tax rates that will apply to any line item that does not have `tax_rates` set.

- `description` (string, optional)
  A description that will be displayed on the quote PDF. If no value is passed, the default description configured in your [quote template settings](https://dashboard.stripe.com/settings/billing/quote) will be used.

  The maximum length is 500 characters.

- `discounts` (array of objects, optional)
  The discounts applied to the quote.

  - `discounts.coupon` (string, optional)
    ID of the coupon to create a new discount for.

  - `discounts.discount` (string, optional)
    ID of an existing discount on the object (or one of its ancestors) to reuse.

  - `discounts.promotion_code` (string, optional)
    ID of the promotion code to create a new discount for.

- `expires_at` (timestamp, optional)
  A future timestamp on which the quote will be canceled if in `open` or `draft` status. Measured in seconds since the Unix epoch. If no value is passed, the default expiration date configured in your [quote template settings](https://dashboard.stripe.com/settings/billing/quote) will be used.

- `footer` (string, optional)
  A footer that will be displayed on the quote PDF. If no value is passed, the default footer configured in your [quote template settings](https://dashboard.stripe.com/settings/billing/quote) will be used.

  The maximum length is 500 characters.

- `from_quote` (object, optional)
  Clone an existing quote. The new quote will be created in `status=draft`. When using this parameter, you cannot specify any other parameters except for `expires_at`.

  - `from_quote.quote` (string, required)
    The `id` of the quote that will be cloned.

  - `from_quote.is_revision` (boolean, optional)
    Whether this quote is a revision of the previous quote.

- `header` (string, optional)
  A header that will be displayed on the quote PDF. If no value is passed, the default header configured in your [quote template settings](https://dashboard.stripe.com/settings/billing/quote) will be used.

  The maximum length is 50 characters.

- `invoice_settings` (object, optional)
  All invoices will be billed using the specified settings.

  - `invoice_settings.days_until_due` (integer, optional)
    Number of days within which a customer must pay the invoice generated by this quote. This value will be `null` for quotes where `collection_method=charge_automatically`.

  - `invoice_settings.issuer` (object, optional)
    The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.

    - `invoice_settings.issuer.type` (enum, required)
      Type of the account referenced in the request.
Possible enum values:
      - `account`
        Indicates that the account being referenced is a connected account which is different from the account making the API request but related to it.

      - `self`
        Indicates that the account being referenced is the account making the API request.

    - `invoice_settings.issuer.account` (string, required only if type is account)
      The connected account being referenced when `type` is `account`.

- `line_items` (array of objects, optional)
  A list of line items the customer is being quoted for. Each line item includes information about the product, the quantity, and the resulting cost.

  - `line_items.discounts` (array of objects, optional)
    The discounts applied to this line item.

    - `line_items.discounts.coupon` (string, optional)
      ID of the coupon to create a new discount for.

    - `line_items.discounts.discount` (string, optional)
      ID of an existing discount on the object (or one of its ancestors) to reuse.

    - `line_items.discounts.promotion_code` (string, optional)
      ID of the promotion code to create a new discount for.

  - `line_items.price` (string, optional)
    The ID of the price object. One of `price` or `price_data` is required.

  - `line_items.price_data` (object, optional)
    Data used to generate a new [Price](https://docs.stripe.com/docs/api/prices.md) object inline. One of `price` or `price_data` is required.

    - `line_items.price_data.currency` (enum, required)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

    - `line_items.price_data.product` (string, required)
      The ID of the [Product](https://docs.stripe.com/api/products.md) that this [Price](https://docs.stripe.com/api/prices.md) will belong to.

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

    - `line_items.price_data.unit_amount` (integer, optional)
      A positive integer in cents (or 0 for a free price) representing how much to charge.

    - `line_items.price_data.unit_amount_decimal` (string, required conditionally)
      Same as `unit_amount`, but accepts a decimal value in cents with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.

  - `line_items.quantity` (integer, optional)
    The quantity of the line item.

  - `line_items.tax_rates` (array of strings, optional)
    The tax rates which apply to the line item. When set, the `default_tax_rates` on the quote do not apply to this line item.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `on_behalf_of` (string, optional)
  The account on behalf of which to charge.

- `subscription_data` (object, optional)
  When creating a subscription or subscription schedule, the specified configuration data will be used. There must be at least one line item with a recurring price for a subscription or subscription schedule to be created. A subscription schedule is created if `subscription_data[effective_date]` is present and in the future, otherwise a subscription is created.

  - `subscription_data.billing_mode` (object, optional)
    Controls how prorations and invoices for subscriptions are calculated and orchestrated.

    - `subscription_data.billing_mode.type` (enum, required)
      Controls the calculation and orchestration of prorations and invoices for subscriptions. If no value is passed, the default is `flexible`.
Possible enum values:
      - `classic`
        Calculations for subscriptions and invoices are based on legacy defaults.

      - `flexible`
        Supports more flexible calculation and orchestration options for subscriptions and invoices.

    - `subscription_data.billing_mode.flexible` (object, optional)
      Configure behavior for flexible billing mode.

      - `subscription_data.billing_mode.flexible.proration_discounts` (enum, optional)
        Controls how invoices and invoice items display proration amounts and discount amounts.
Possible enum values:
        - `included`
          Amounts are net of discounts, and discount amounts are zero.

        - `itemized`
          Amounts are gross of discounts, and discount amounts are accurate.

  - `subscription_data.description` (string, optional)
    The subscription’s description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.

    The maximum length is 500 characters.

  - `subscription_data.effective_date` (string | timestamp, optional)
    When creating a new subscription, the date of which the subscription schedule will start after the quote is accepted. The `effective_date` is ignored if it is in the past when the quote is accepted.

  - `subscription_data.metadata` (object, optional)
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that will set metadata on the subscription or subscription schedule when the quote is accepted. If a recurring price is included in `line_items`, this field will be passed to the resulting subscription’s `metadata` field. If `subscription_data.effective_date` is used, this field will be passed to the resulting subscription schedule’s `phases.metadata` field. Unlike object-level metadata, this field is declarative. Updates will clear prior values.

  - `subscription_data.trial_period_days` (integer, optional)
    Integer representing the number of trial period days before the customer is charged for the first time.

- `test_clock` (string, optional)
  ID of the test clock to attach to the quote.

- `transfer_data` (object, optional)
  The data with which to automatically create a Transfer for each of the invoices.

  - `transfer_data.destination` (string, required)
    ID of an existing, connected Stripe account.

  - `transfer_data.amount` (integer, optional)
    The amount that will be transferred automatically when the invoice is paid. If no amount is set, the full amount is transferred. There cannot be any line items with recurring prices when using this field.

  - `transfer_data.amount_percent` (float, optional)
    A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the destination account. By default, the entire amount is transferred to the destination. There must be at least 1 line item with a recurring price to use this field.

```curl
curl https://api.stripe.com/v1/quotes \
  -u "<<YOUR_SECRET_KEY>>" \
  -d customer=cus_NcMfB0SSFHINCV \
  -d "line_items[0][price]"=price_1Mr7wULkdIwHu7ixhPkIEN2w \
  -d "line_items[0][quantity]"=2
```

```cli
stripe quotes create  \
  --customer=cus_NcMfB0SSFHINCV \
  -d "line_items[0][price]"=price_1Mr7wULkdIwHu7ixhPkIEN2w \
  -d "line_items[0][quantity]"=2
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

quote = client.v1.quotes.create({
  customer: 'cus_NcMfB0SSFHINCV',
  line_items: [
    {
      price: 'price_1Mr7wULkdIwHu7ixhPkIEN2w',
      quantity: 2,
    },
  ],
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

quote = client.v1.quotes.create({
  "customer": "cus_NcMfB0SSFHINCV",
  "line_items": [{"price": "price_1Mr7wULkdIwHu7ixhPkIEN2w", "quantity": 2}],
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$quote = $stripe->quotes->create([
  'customer' => 'cus_NcMfB0SSFHINCV',
  'line_items' => [
    [
      'price' => 'price_1Mr7wULkdIwHu7ixhPkIEN2w',
      'quantity' => 2,
    ],
  ],
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

QuoteCreateParams params =
  QuoteCreateParams.builder()
    .setCustomer("cus_NcMfB0SSFHINCV")
    .addLineItem(
      QuoteCreateParams.LineItem.builder()
        .setPrice("price_1Mr7wULkdIwHu7ixhPkIEN2w")
        .setQuantity(2L)
        .build()
    )
    .build();

Quote quote = client.v1().quotes().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const quote = await stripe.quotes.create({
  customer: 'cus_NcMfB0SSFHINCV',
  line_items: [
    {
      price: 'price_1Mr7wULkdIwHu7ixhPkIEN2w',
      quantity: 2,
    },
  ],
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.QuoteCreateParams{
  Customer: stripe.String("cus_NcMfB0SSFHINCV"),
  LineItems: []*stripe.QuoteCreateLineItemParams{
    &stripe.QuoteCreateLineItemParams{
      Price: stripe.String("price_1Mr7wULkdIwHu7ixhPkIEN2w"),
      Quantity: stripe.Int64(2),
    },
  },
}
result, err := sc.V1Quotes.Create(context.TODO(), params)
```

```dotnet
var options = new QuoteCreateOptions
{
    Customer = "cus_NcMfB0SSFHINCV",
    LineItems = new List<QuoteLineItemOptions>
    {
        new QuoteLineItemOptions
        {
            Price = "price_1Mr7wULkdIwHu7ixhPkIEN2w",
            Quantity = 2,
        },
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Quotes;
Quote quote = service.Create(options);
```

### Response

```json
{
  "id": "qt_1Mr7wVLkdIwHu7ixJYSiPTGq",
  "object": "quote",
  "amount_subtotal": 2198,
  "amount_total": 2198,
  "application": null,
  "application_fee_amount": null,
  "application_fee_percent": null,
  "automatic_tax": {
    "enabled": false,
    "liability": null,
    "status": null
  },
  "collection_method": "charge_automatically",
  "computed": {
    "recurring": null,
    "upfront": {
      "amount_subtotal": 2198,
      "amount_total": 2198,
      "total_details": {
        "amount_discount": 0,
        "amount_shipping": 0,
        "amount_tax": 0
      }
    }
  },
  "created": 1680130691,
  "currency": "usd",
  "customer": "cus_NcMfB0SSFHINCV",
  "default_tax_rates": [],
  "description": null,
  "discounts": [],
  "expires_at": 1682722691,
  "footer": null,
  "from_quote": null,
  "header": null,
  "invoice": null,
  "invoice_settings": {
    "days_until_due": null,
    "issuer": {
      "type": "self"
    }
  },
  "livemode": false,
  "metadata": {},
  "number": null,
  "on_behalf_of": null,
  "status": "draft",
  "status_transitions": {
    "accepted_at": null,
    "canceled_at": null,
    "finalized_at": null
  },
  "subscription": null,
  "subscription_data": {
    "description": null,
    "effective_date": null,
    "trial_period_days": null
  },
  "subscription_schedule": null,
  "test_clock": null,
  "total_details": {
    "amount_discount": 0,
    "amount_shipping": 0,
    "amount_tax": 0
  },
  "transfer_data": null
}
```