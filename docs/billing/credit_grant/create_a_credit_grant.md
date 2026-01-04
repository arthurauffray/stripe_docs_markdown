# Create a credit grant

Creates a credit grant.

## Returns

Returns a credit grant.

## Parameters

- `amount` (object, required)
  Amount of this credit grant.

  - `amount.type` (enum, required)
    The type of this amount. We currently only support `monetary` billing credits.
Possible enum values:
    - `monetary`
      The amount is a monetary amount.

  - `amount.monetary` (object, optional)
    The monetary amount.

    - `amount.monetary.currency` (enum, required)
      Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) of the `value` parameter.

    - `amount.monetary.value` (integer, required)
      A positive integer representing the amount of the credit grant.

- `applicability_config` (object, required)
  Configuration specifying what this credit grant applies to. We currently only support `metered` prices that have a [Billing Meter](https://docs.stripe.com/api/billing/meter.md) attached to them.

  - `applicability_config.scope` (object, required)
    Specify the scope of this applicability config.

    - `applicability_config.scope.billable_items` (array of objects, optional)
      A list of billable items that the credit grant can apply to. We currently only support metered billable items. Cannot be used in combination with `price_type` or `prices`.

      - `applicability_config.scope.billable_items.id` (string, required)
        The billable item ID this credit grant should apply to.

    - `applicability_config.scope.price_type` (enum, optional)
      The price type that credit grants can apply to. We currently only support the `metered` price type. Cannot be used in combination with `prices`.
Possible enum values:
      - `metered`
        Credit grants being created can only apply to metered prices.

    - `applicability_config.scope.prices` (array of objects, optional)
      A list of prices that the credit grant can apply to. We currently only support the `metered` prices. Cannot be used in combination with `price_type`.

      - `applicability_config.scope.prices.id` (string, required)
        The price ID this credit grant should apply to.

- `category` (enum, optional)
  The category of this credit grant. It defaults to `paid` if not specified.
Possible enum values:
  - `paid`
    The credit grant was purchased by the customer for some amount.

  - `promotional`
    The credit grant was given to the customer for free.

- `customer` (string, optional)
  ID of the customer receiving the billing credits.

- `customer_account` (string, optional)
  ID of the account representing the customer receiving the billing credits.

- `effective_at` (timestamp, optional)
  The time when the billing credits become effective-when they’re eligible for use. It defaults to the current timestamp if not specified.

- `expires_at` (timestamp, optional)
  The time when the billing credits expire. If not specified, the billing credits don’t expire.

- `metadata` (object, optional)
  Set of key-value pairs that you can attach to an object. You can use this to store additional information about the object (for example, cost basis) in a structured format.

- `name` (string, optional)
  A descriptive name shown in the Dashboard.

  The maximum length is 100 characters.

- `priority` (integer, optional)
  The desired priority for applying this credit grant. If not specified, it will be set to the default value of 50. The highest priority is 0 and the lowest is 100.

```curl
curl https://api.stripe.com/v1/billing/credit_grants \
  -u "<<YOUR_SECRET_KEY>>" \
  -d name="Purchased Credits" \
  -d customer=cus_QrvQguzkIK8zTj \
  -d "amount[monetary][currency]"=usd \
  -d "amount[monetary][value]"=1000 \
  -d "amount[type]"=monetary \
  -d "applicability_config[scope][price_type]"=metered \
  -d category=paid
```

```cli
stripe billing credit_grants create  \
  --name="Purchased Credits" \
  --customer=cus_QrvQguzkIK8zTj \
  -d "amount[monetary][currency]"=usd \
  -d "amount[monetary][value]"=1000 \
  -d "amount[type]"=monetary \
  -d "applicability_config[scope][price_type]"=metered \
  --category=paid
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

credit_grant = client.v1.billing.credit_grants.create({
  name: 'Purchased Credits',
  customer: 'cus_QrvQguzkIK8zTj',
  amount: {
    monetary: {
      currency: 'usd',
      value: 1000,
    },
    type: 'monetary',
  },
  applicability_config: {scope: {price_type: 'metered'}},
  category: 'paid',
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

credit_grant = client.v1.billing.credit_grants.create({
  "name": "Purchased Credits",
  "customer": "cus_QrvQguzkIK8zTj",
  "amount": {"monetary": {"currency": "usd", "value": 1000}, "type": "monetary"},
  "applicability_config": {"scope": {"price_type": "metered"}},
  "category": "paid",
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$creditGrant = $stripe->billing->creditGrants->create([
  'name' => 'Purchased Credits',
  'customer' => 'cus_QrvQguzkIK8zTj',
  'amount' => [
    'monetary' => [
      'currency' => 'usd',
      'value' => 1000,
    ],
    'type' => 'monetary',
  ],
  'applicability_config' => ['scope' => ['price_type' => 'metered']],
  'category' => 'paid',
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CreditGrantCreateParams params =
  CreditGrantCreateParams.builder()
    .setName("Purchased Credits")
    .setCustomer("cus_QrvQguzkIK8zTj")
    .setAmount(
      CreditGrantCreateParams.Amount.builder()
        .setMonetary(
          CreditGrantCreateParams.Amount.Monetary.builder()
            .setCurrency("usd")
            .setValue(1000L)
            .build()
        )
        .setType(CreditGrantCreateParams.Amount.Type.MONETARY)
        .build()
    )
    .setApplicabilityConfig(
      CreditGrantCreateParams.ApplicabilityConfig.builder()
        .setScope(
          CreditGrantCreateParams.ApplicabilityConfig.Scope.builder()
            .setPriceType(
              CreditGrantCreateParams.ApplicabilityConfig.Scope.PriceType.METERED
            )
            .build()
        )
        .build()
    )
    .setCategory(CreditGrantCreateParams.Category.PAID)
    .build();

CreditGrant creditGrant = client.v1().billing().creditGrants().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const creditGrant = await stripe.billing.creditGrants.create({
  name: 'Purchased Credits',
  customer: 'cus_QrvQguzkIK8zTj',
  amount: {
    monetary: {
      currency: 'usd',
      value: 1000,
    },
    type: 'monetary',
  },
  applicability_config: {
    scope: {
      price_type: 'metered',
    },
  },
  category: 'paid',
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.BillingCreditGrantCreateParams{
  Name: stripe.String("Purchased Credits"),
  Customer: stripe.String("cus_QrvQguzkIK8zTj"),
  Amount: &stripe.BillingCreditGrantCreateAmountParams{
    Monetary: &stripe.BillingCreditGrantCreateAmountMonetaryParams{
      Currency: stripe.String(stripe.CurrencyUSD),
      Value: stripe.Int64(1000),
    },
    Type: stripe.String("monetary"),
  },
  ApplicabilityConfig: &stripe.BillingCreditGrantCreateApplicabilityConfigParams{
    Scope: &stripe.BillingCreditGrantCreateApplicabilityConfigScopeParams{
      PriceType: stripe.String("metered"),
    },
  },
  Category: stripe.String(stripe.BillingCreditGrantCategoryPaid),
}
result, err := sc.V1BillingCreditGrants.Create(context.TODO(), params)
```

```dotnet
var options = new Stripe.Billing.CreditGrantCreateOptions
{
    Name = "Purchased Credits",
    Customer = "cus_QrvQguzkIK8zTj",
    Amount = new Stripe.Billing.CreditGrantAmountOptions
    {
        Monetary = new Stripe.Billing.CreditGrantAmountMonetaryOptions
        {
            Currency = "usd",
            Value = 1000,
        },
        Type = "monetary",
    },
    ApplicabilityConfig = new Stripe.Billing.CreditGrantApplicabilityConfigOptions
    {
        Scope = new Stripe.Billing.CreditGrantApplicabilityConfigScopeOptions
        {
            PriceType = "metered",
        },
    },
    Category = "paid",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Billing.CreditGrants;
Stripe.Billing.CreditGrant creditGrant = service.Create(options);
```

### Response

```json
{
  "id": "credgr_test_61R9a6NUWsRmOW3RM41L6nFOS1ekDGHo",
  "object": "billing.credit_grant",
  "amount": {
    "monetary": {
      "currency": "usd",
      "value": 1000
    },
    "type": "monetary"
  },
  "applicability_config": {
    "scope": {
      "price_type": "metered"
    }
  },
  "category": "paid",
  "created": 1726620803,
  "customer": "cus_QrvQguzkIK8zTj",
  "effective_at": 1729297860,
  "expires_at": null,
  "livemode": false,
  "metadata": {},
  "name": "Purchased Credits",
  "priority": null,
  "test_clock": null,
  "updated": 1726620803
}
```