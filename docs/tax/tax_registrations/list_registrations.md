# List registrations

Returns a list of Tax `Registration` objects.

## Returns

A list of Tax `Registration` objects.

## Parameters

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `status` (enum, optional)
  The status of the Tax Registration.
Possible enum values:
  - `active`
    Return all active Tax Registrations.

  - `all`
    Return all Tax Registrations (default).

  - `expired`
    Return all expired Tax Registrations.

  - `scheduled`
    Return all scheduled Tax Registrations.

```curl
curl -G https://api.stripe.com/v1/tax/registrations \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe tax registrations list  \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

registrations = client.v1.tax.registrations.list({limit: 3})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

registrations = client.v1.tax.registrations.list({"limit": 3})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$registrations = $stripe->tax->registrations->all(['limit' => 3]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

RegistrationListParams params =
  RegistrationListParams.builder().setLimit(3L).build();

StripeCollection<Registration> stripeCollection =
  client.v1().tax().registrations().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const registrations = await stripe.tax.registrations.list({
  limit: 3,
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TaxRegistrationListParams{}
params.Limit = stripe.Int64(3)
result := sc.V1TaxRegistrations.List(context.TODO(), params)
```

```dotnet
var options = new Stripe.Tax.RegistrationListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Tax.Registrations;
StripeList<Stripe.Tax.Registration> registrations = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/tax/registrations",
  "has_more": false,
  "data": [
    {
      "id": "taxreg_NkyGPRPytKq66j",
      "object": "tax.registration",
      "active_from": 1682036640,
      "country": "US",
      "country_options": {
        "us": {
          "state": "CA",
          "type": "state_sales_tax"
        }
      },
      "created": 1682006400,
      "expires_at": null,
      "livemode": false,
      "status": "active",
      "state": "CA",
      "type": "standard"
    }
  ]
}
```