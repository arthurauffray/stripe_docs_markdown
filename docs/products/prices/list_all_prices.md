# List all prices

Returns a list of your active prices, excluding [inline prices](https://docs.stripe.com/docs/products-prices/pricing-models.md#inline-pricing). For the list of inactive prices, set `active` to false.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` prices, starting after prices `starting_after`. Each entry in the array is a separate price object. If no more prices are available, the resulting array will be empty.

## Parameters

- `active` (boolean, optional)
  Only return prices that are active or inactive (e.g., pass `false` to list all inactive prices).

- `created` (object, optional)
  A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.

  - `created.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `created.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `created.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `created.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `currency` (enum, optional)
  Only return prices for the given currency.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `lookup_keys` (array of strings, optional)
  Only return the price with these lookup_keys, if any exist. You can specify up to 10 lookup_keys.

- `product` (string, optional)
  Only return prices for the given product.

- `recurring` (object, optional)
  Only return prices with these recurring fields.

  - `recurring.interval` (enum, optional)
    Filter by billing frequency. Either `day`, `week`, `month` or `year`.
Possible enum values:
    - `day`
    - `month`
    - `week`
    - `year`

  - `recurring.meter` (string, optional)
    Filter by the price’s meter.

  - `recurring.usage_type` (enum, optional)
    Filter by the usage type for this price. Can be either `metered` or `licensed`.
Possible enum values:
    - `licensed`
    - `metered`

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `type` (enum, optional)
  Only return prices of type `recurring` or `one_time`.
Possible enum values:
  - `one_time`
  - `recurring`

```curl
curl -G https://api.stripe.com/v1/prices \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe prices list  \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

prices = client.v1.prices.list({limit: 3})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

prices = client.v1.prices.list({"limit": 3})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$prices = $stripe->prices->all(['limit' => 3]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

PriceListParams params = PriceListParams.builder().setLimit(3L).build();

StripeCollection<Price> stripeCollection = client.v1().prices().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const prices = await stripe.prices.list({
  limit: 3,
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PriceListParams{}
params.Limit = stripe.Int64(3)
result := sc.V1Prices.List(context.TODO(), params)
```

```dotnet
var options = new PriceListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Prices;
StripeList<Price> prices = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/prices",
  "has_more": false,
  "data": [
    {
      "id": "price_1MoBy5LkdIwHu7ixZhnattbh",
      "object": "price",
      "active": true,
      "billing_scheme": "per_unit",
      "created": 1679431181,
      "currency": "usd",
      "custom_unit_amount": null,
      "livemode": false,
      "lookup_key": null,
      "metadata": {},
      "nickname": null,
      "product": "prod_NZKdYqrwEYx6iK",
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
    }
  ]
}
```