# Create a subscription item

Adds a new item to an existing subscription. No existing items will be changed or replaced.

## Returns

Returns the created `Subscription Item` object, if successful. Otherwise, this call raises [an error](https://docs.stripe.com/api/subscription_items/create.md#errors).

## Parameters

- `subscription` (string, required)
  The identifier of the subscription to modify.

- `billing_thresholds` (object, optional)
  Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. Pass an empty string to remove previously-defined thresholds.

  - `billing_thresholds.usage_gte` (integer, required)
    Number of units that meets the billing threshold to advance the subscription to a new billing period (e.g., it takes 10 $5 units to meet a $50 [monetary threshold](https://docs.stripe.com/docs/api/subscriptions/update.md#update_subscription-billing_thresholds-amount_gte))

- `discounts` (array of objects, optional)
  The coupons to redeem into discounts for the subscription item.

  - `discounts.coupon` (string, optional)
    ID of the coupon to create a new discount for.

  - `discounts.discount` (string, optional)
    ID of an existing discount on the object (or one of its ancestors) to reuse.

  - `discounts.promotion_code` (string, optional)
    ID of the promotion code to create a new discount for.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `payment_behavior` (enum, optional)
  Use `allow_incomplete` to transition the subscription to `status=past_due` if a payment is required but cannot be paid. This allows you to manage scenarios where additional user actions are needed to pay a subscription’s invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the [SCA Migration Guide](https://docs.stripe.com/docs/billing/migration/strong-customer-authentication.md) for Billing to learn more. This is the default behavior.

  Use `default_incomplete` to transition the subscription to `status=past_due` when payment is required and await explicit confirmation of the invoice’s payment intent. This allows simpler management of scenarios where additional user actions are needed to pay a subscription’s invoice. Such as failed payments, [SCA regulation](https://docs.stripe.com/docs/billing/migration/strong-customer-authentication.md), or collecting a mandate for a bank debit payment method.

  Use `pending_if_incomplete` to update the subscription using [pending updates](https://docs.stripe.com/docs/billing/subscriptions/pending-updates.md). When you use `pending_if_incomplete` you can only pass the parameters [supported by pending updates](https://docs.stripe.com/docs/billing/pending-updates-reference.md#supported-attributes).

  Use `error_if_incomplete` if you want Stripe to return an HTTP 402 status code if a subscription’s invoice cannot be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further user action is needed, this parameter does not update the subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the [changelog](https://docs.stripe.com/changelog/2019-03-14.md) to learn more.
Possible enum values:
  - `allow_incomplete`
  - `default_incomplete`
  - `error_if_incomplete`
  - `pending_if_incomplete`

- `price` (string, optional)
  The ID of the price object.

- `price_data` (object, optional)
  Data used to generate a new [Price](https://docs.stripe.com/docs/api/prices.md) object inline.

  - `price_data.currency` (enum, required)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `price_data.product` (string, required)
    The ID of the [Product](https://docs.stripe.com/api/products.md) that this [Price](https://docs.stripe.com/api/prices.md) will belong to.

  - `price_data.recurring` (object, required)
    The recurring components of a price such as `interval` and `interval_count`.

    - `price_data.recurring.interval` (enum, required)
      Specifies billing frequency. Either `day`, `week`, `month` or `year`.
Possible enum values:
      - `day`
      - `month`
      - `week`
      - `year`

    - `price_data.recurring.interval_count` (integer, optional)
      The number of intervals between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of three years interval allowed (3 years, 36 months, or 156 weeks).

  - `price_data.tax_behavior` (enum, recommended if calculating taxes)
    Only required if a [default tax behavior](https://docs.stripe.com/docs/tax/products-prices-tax-categories-tax-behavior.md#setting-a-default-tax-behavior-\(recommended\)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
Possible enum values:
    - `exclusive`
    - `inclusive`
    - `unspecified`

  - `price_data.unit_amount` (integer, optional)
    A positive integer in cents (or 0 for a free price) representing how much to charge.

  - `price_data.unit_amount_decimal` (string, required conditionally)
    Same as `unit_amount`, but accepts a decimal value in cents with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.

- `proration_behavior` (enum, optional)
  Determines how to handle [prorations](https://docs.stripe.com/docs/billing/subscriptions/prorations.md) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item’s `quantity` changes. The default value is `create_prorations`.
Possible enum values:
  - `always_invoice`
    Always invoice immediately for prorations.

  - `create_prorations`
    Will cause proration invoice items to be created when applicable. These proration items will only be invoiced immediately under [certain conditions](https://docs.stripe.com/docs/subscriptions/upgrading-downgrading.md#immediate-payment).

  - `none`
    Disable creating prorations in this request.

- `proration_date` (timestamp, optional)
  If set, the proration will be calculated as though the subscription was updated at the given time. This can be used to apply the same proration that was previewed with the [upcoming invoice](https://docs.stripe.com/api/subscription_items/create.md#retrieve_customer_invoice) endpoint.

- `quantity` (integer, optional)
  The quantity you’d like to apply to the subscription item you’re creating.

- `tax_rates` (array of strings, optional)
  A list of [Tax Rate](https://docs.stripe.com/docs/api/tax_rates.md) ids. These Tax Rates will override the [`default_tax_rates`](https://docs.stripe.com/docs/api/subscriptions/create.md#create_subscription-default_tax_rates) on the Subscription. When updating, pass an empty string to remove previously-defined tax rates.

```curl
curl https://api.stripe.com/v1/subscription_items \
  -u "<<YOUR_SECRET_KEY>>" \
  -d subscription=sub_1Mr6rbLkdIwHu7ix4Xm9Ahtd \
  -d price=price_1Mr6rdLkdIwHu7ixwPmiybbR \
  -d quantity=2
```

```cli
stripe subscription_items create  \
  --subscription=sub_1Mr6rbLkdIwHu7ix4Xm9Ahtd \
  --price=price_1Mr6rdLkdIwHu7ixwPmiybbR \
  --quantity=2
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

subscription_item = client.v1.subscription_items.create({
  subscription: 'sub_1Mr6rbLkdIwHu7ix4Xm9Ahtd',
  price: 'price_1Mr6rdLkdIwHu7ixwPmiybbR',
  quantity: 2,
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

subscription_item = client.v1.subscription_items.create({
  "subscription": "sub_1Mr6rbLkdIwHu7ix4Xm9Ahtd",
  "price": "price_1Mr6rdLkdIwHu7ixwPmiybbR",
  "quantity": 2,
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$subscriptionItem = $stripe->subscriptionItems->create([
  'subscription' => 'sub_1Mr6rbLkdIwHu7ix4Xm9Ahtd',
  'price' => 'price_1Mr6rdLkdIwHu7ixwPmiybbR',
  'quantity' => 2,
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

SubscriptionItemCreateParams params =
  SubscriptionItemCreateParams.builder()
    .setSubscription("sub_1Mr6rbLkdIwHu7ix4Xm9Ahtd")
    .setPrice("price_1Mr6rdLkdIwHu7ixwPmiybbR")
    .setQuantity(2L)
    .build();

SubscriptionItem subscriptionItem = client.v1().subscriptionItems().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const subscriptionItem = await stripe.subscriptionItems.create({
  subscription: 'sub_1Mr6rbLkdIwHu7ix4Xm9Ahtd',
  price: 'price_1Mr6rdLkdIwHu7ixwPmiybbR',
  quantity: 2,
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.SubscriptionItemCreateParams{
  Subscription: stripe.String("sub_1Mr6rbLkdIwHu7ix4Xm9Ahtd"),
  Price: stripe.String("price_1Mr6rdLkdIwHu7ixwPmiybbR"),
  Quantity: stripe.Int64(2),
}
result, err := sc.V1SubscriptionItems.Create(context.TODO(), params)
```

```dotnet
var options = new SubscriptionItemCreateOptions
{
    Subscription = "sub_1Mr6rbLkdIwHu7ix4Xm9Ahtd",
    Price = "price_1Mr6rdLkdIwHu7ixwPmiybbR",
    Quantity = 2,
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.SubscriptionItems;
SubscriptionItem subscriptionItem = service.Create(options);
```

### Response

```json
{
  "id": "si_NcLYdDxLHxlFo7",
  "object": "subscription_item",
  "created": 1680126546,
  "metadata": {},
  "price": {
    "id": "price_1Mr6rdLkdIwHu7ixwPmiybbR",
    "object": "price",
    "active": true,
    "billing_scheme": "per_unit",
    "created": 1680126545,
    "currency": "usd",
    "custom_unit_amount": null,
    "discounts": null,
    "livemode": false,
    "lookup_key": null,
    "metadata": {},
    "nickname": null,
    "product": "prod_NcLYGKH0eY5b8s",
    "recurring": {
      "interval": "month",
      "interval_count": 1,
      "trial_period_days": null,
      "usage_type": "licensed"
    },
    "tax_behavior": "unspecified",
    "tiers_mode": null,
    "transform_quantity": null,
    "type": "recurring",
    "unit_amount": 1000,
    "unit_amount_decimal": "1000"
  },
  "quantity": 2,
  "subscription": "sub_1Mr6rbLkdIwHu7ix4Xm9Ahtd",
  "tax_rates": []
}
```