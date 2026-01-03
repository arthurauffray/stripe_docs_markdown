# List financing offers

Retrieves the financing offers available for Connected accounts that belong to your platform.

## Returns

Returns a list of financing offers for Connected accounts on your platform.

## Parameters

- `connected_account` (string, optional)
  limit list to offers belonging to given connected account

- `created` (object, optional)
  Only return offers that were created during the given date interval.

  - `created.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `created.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `created.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `created.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `status` (string, optional)
  limit list to offers with given status

```curl
curl -G https://api.stripe.com/v1/capital/financing_offers \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe capital financing_offers list  \
  --limit=3
```

```ruby
# This example uses the beta SDK. See https://github.com/stripe/stripe-ruby#public-preview-sdks
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

financing_offers = client.v1.capital.financing_offers.list({limit: 3})
```

```python
# This example uses the beta SDK. See https://github.com/stripe/stripe-python#public-preview-sdks
client = StripeClient("<<YOUR_SECRET_KEY>>")

financing_offers = client.v1.capital.financing_offers.list({"limit": 3})
```

```php
// This example uses the beta SDK. See https://github.com/stripe/stripe-php#public-preview-sdks
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$financingOffers = $stripe->capital->financingOffers->all(['limit' => 3]);
```

```java
// This example uses the beta SDK. See https://github.com/stripe/stripe-java#public-preview-sdks
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

FinancingOfferListParams params =
  FinancingOfferListParams.builder().setLimit(3L).build();

StripeCollection<FinancingOffer> stripeCollection =
  client.v1().capital().financingOffers().list(params);
```

```node
// This example uses the beta SDK. See https://github.com/stripe/stripe-node#public-preview-sdks
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const financingOffers = await stripe.capital.financingOffers.list({
  limit: 3,
});
```

```go
// This example uses the beta SDK. See https://github.com/stripe/stripe-go#public-preview-sdks
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CapitalFinancingOfferListParams{}
params.Limit = stripe.Int64(3)
result := sc.V1CapitalFinancingOffers.List(context.TODO(), params)
```

```dotnet
// This example uses the beta SDK. See https://github.com/stripe/stripe-dotnet#public-preview-sdks
var options = new Stripe.Capital.FinancingOfferListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Capital.FinancingOffers;
StripeList<Stripe.Capital.FinancingOffer> financingOffers = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/capital/financing_offers",
  "has_more": false,
  "data": [
    {
      "id": "financingoffer_1Nn7FV2eZvKYlo2CcGGcdZ6L",
      "object": "capital.financing_offer",
      "account": "acct_1Nn7FVGy17qyuPVN",
      "created": 1693951049,
      "expires_after": 1696464000,
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
      "status": "undelivered"
    }
  ]
}
```