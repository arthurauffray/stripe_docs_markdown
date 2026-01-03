# Mark that a financing offer has been delivered

Acknowledges that platform has received and delivered the financing_offer to the intended merchant recipient.

## Returns

Returns the financing offer object

```curl
curl -X POST https://api.stripe.com/v1/capital/financing_offers/financingoffer_1NPvKg2eZvKYlo2CnEEmlCVh/mark_delivered \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe capital financing_offers mark_delivered financingoffer_1NPvKg2eZvKYlo2CnEEmlCVh
```

```ruby
# This example uses the beta SDK. See https://github.com/stripe/stripe-ruby#public-preview-sdks
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

financing_offer = client.v1.capital.financing_offers.mark_delivered('financingoffer_1NPvKg2eZvKYlo2CnEEmlCVh')
```

```python
# This example uses the beta SDK. See https://github.com/stripe/stripe-python#public-preview-sdks
client = StripeClient("<<YOUR_SECRET_KEY>>")

financing_offer = client.v1.capital.financing_offers.mark_delivered(
  "financingoffer_1NPvKg2eZvKYlo2CnEEmlCVh",
)
```

```php
// This example uses the beta SDK. See https://github.com/stripe/stripe-php#public-preview-sdks
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$financingOffer = $stripe->capital->financingOffers->markDelivered(
  'financingoffer_1NPvKg2eZvKYlo2CnEEmlCVh',
  []
);
```

```java
// This example uses the beta SDK. See https://github.com/stripe/stripe-java#public-preview-sdks
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

FinancingOfferMarkDeliveredParams params =
  FinancingOfferMarkDeliveredParams.builder().build();

FinancingOffer financingOffer =
  client.v1().capital().financingOffers().markDelivered(
    "financingoffer_1NPvKg2eZvKYlo2CnEEmlCVh",
    params
  );
```

```node
// This example uses the beta SDK. See https://github.com/stripe/stripe-node#public-preview-sdks
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const financingOffer = await stripe.capital.financingOffers.markDelivered(
  'financingoffer_1NPvKg2eZvKYlo2CnEEmlCVh'
);
```

```go
// This example uses the beta SDK. See https://github.com/stripe/stripe-go#public-preview-sdks
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CapitalFinancingOfferMarkDeliveredParams{}
result, err := sc.V1CapitalFinancingOffers.MarkDelivered(
  context.TODO(), "financingoffer_1NPvKg2eZvKYlo2CnEEmlCVh", params)
```

```dotnet
// This example uses the beta SDK. See https://github.com/stripe/stripe-dotnet#public-preview-sdks
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Capital.FinancingOffers;
Stripe.Capital.FinancingOffer financingOffer = service.MarkDelivered(
    "financingoffer_1NPvKg2eZvKYlo2CnEEmlCVh");
```

### Response

```json
{
  "id": "financingoffer_1NPvKg2eZvKYlo2CnEEmlCVh",
  "object": "capital.financing_offer",
  "account": "acct_1NPvKgBY65lDjjDk",
  "created": 1688423699,
  "expires_after": 1690934400,
  "financing_type": "flex_loan",
  "livemode": true,
  "offered_terms": {
    "advance_amount": 10000,
    "campaign_type": "newly_eligible_user",
    "currency": "usd",
    "fee_amount": 1000,
    "previous_financing_fee_discount_rate": null,
    "withhold_rate": 0.05
  },
  "product_type": "standard",
  "status": "delivered"
}
```