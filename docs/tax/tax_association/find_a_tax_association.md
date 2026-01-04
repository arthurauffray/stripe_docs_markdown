# Find a Tax Association

Finds a tax association object by PaymentIntent id.

## Returns

A `Tax Association` object.

## Parameters

- `payment_intent` (string, required)
  Valid [PaymentIntent](https://docs.stripe.com/docs/api/payment_intents/object.md) id

```curl
curl -G https://api.stripe.com/v1/tax/associations/find \
  -u "<<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2025-12-15.clover; payment_intent_with_tax_api_beta=v1" \
  -d payment_intent=pi_3PY55JRw02rhjhAj04XgRlJF
```

```ruby
client = Stripe::StripeClient.new(
  "<<YOUR_SECRET_KEY>>",
  stripe_version: '2025-12-15.clover; payment_intent_with_tax_api_beta=v1',
)

association = client.v1.tax.associations.find({
  payment_intent: 'pi_3PY55JRw02rhjhAj04XgRlJF',
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

association = client.v1.tax.associations.find(
  {"payment_intent": "pi_3PY55JRw02rhjhAj04XgRlJF"},
  {
    "stripe_version":
    "2025-12-15.clover; payment_intent_with_tax_api_beta=v1",
  },
)
```

```php
$stripe = new \Stripe\StripeClient([
  'api_key' => '<<YOUR_SECRET_KEY>>',
  'stripe_version' => '2025-12-15.clover; payment_intent_with_tax_api_beta=v1',
]);

$association = $stripe->tax->associations->find([
  'payment_intent' => 'pi_3PY55JRw02rhjhAj04XgRlJF',
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

AssociationFindParams params =
  AssociationFindParams.builder()
    .setPaymentIntent("pi_3PY55JRw02rhjhAj04XgRlJF")
    .build();

Association association = client.v1().tax().associations().find(params);
```

```node
const stripe = require('stripe')(
  '<<YOUR_SECRET_KEY>>',
  {
    // @ts-ignore overrides the pinned API version
    apiVersion: '2025-12-15.clover; payment_intent_with_tax_api_beta=v1',
  }
);

const association = await stripe.tax.associations.find({
  payment_intent: 'pi_3PY55JRw02rhjhAj04XgRlJF',
});
```

```go
// Only public preview releases of stripe-go support setting the beta version. See https://github.com/stripe/stripe-go/blob/master/README.md#public-preview-sdks for more information.
stripe.AddBetaVersion("payment_intent_with_tax_api_beta", "v1")

sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TaxAssociationFindParams{
  PaymentIntent: stripe.String("pi_3PY55JRw02rhjhAj04XgRlJF"),
}
result, err := sc.V1TaxAssociations.Find(context.TODO(), params)
```

```dotnet
// Only public preview releases of stripe-dotnet support setting the beta version. See https://github.com/stripe/stripe-dotnet/blob/master/README.md#public-preview-sdks for more information.
StripeConfiguration.AddBetaVersion("payment_intent_with_tax_api_beta", "v1");

var options = new Stripe.Tax.AssociationFindOptions
{
    PaymentIntent = "pi_3PY55JRw02rhjhAj04XgRlJF",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Tax.Associations;
Stripe.Tax.Association association = service.Find(options);
```

### Response

```json
{
  "id": "taxa_1PYP5RRw02rhjhAjNemx66hC",
  "object": "tax.association",
  "calculation": "taxcalc_1PYP4vRw02rhjhAjPfzylM7p",
  "payment_intent": "pi_3PYP4zRw02rhjhAj1UotslTI",
  "tax_transaction_attempts": [
    {
      "source": "pi_1PXmsSE5ebw4kUHWK7FIhQlS",
      "status": "committed",
      "committed": {
        "transaction": "tax_1PXmsRE5ebw4kUHWLyVEiMis"
      }
    },
    {
      "source": "re_1PXmsSE5ebw4kUHWK7FIhQlS",
      "status": "committed",
      "committed": {
        "transaction": "tax_1PXmsgE5ebw4kUHW7Gg8jvpX"
      }
    }
  ]
}
```