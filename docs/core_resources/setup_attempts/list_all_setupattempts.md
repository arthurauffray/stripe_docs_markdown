# List all SetupAttempts

Returns a list of SetupAttempts that associate with a provided SetupIntent.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` SetupAttempts that are created by the specified SetupIntent, which start after SetupAttempts `starting_after`. Each entry in the array is a separate SetupAttempts object. If no other SetupAttempts are available, the resulting array is be empty. This request should never raise an error.

## Parameters

- `setup_intent` (string, required)
  Only return SetupAttempts created by the SetupIntent specified by this ID.

- `created` (object, optional)
  A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp or a dictionary with a number of different query options.

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

```curl
curl -G https://api.stripe.com/v1/setup_attempts \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3 \
  -d setup_intent=seti_1ErTsG2eZvKYlo2CKaT8MITz
```

```cli
stripe setup_attempts list  \
  --limit=3 \
  --setup-intent=seti_1ErTsG2eZvKYlo2CKaT8MITz
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

setup_attempts = client.v1.setup_attempts.list({
  limit: 3,
  setup_intent: 'seti_1ErTsG2eZvKYlo2CKaT8MITz',
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

setup_attempts = client.v1.setup_attempts.list({
  "limit": 3,
  "setup_intent": "seti_1ErTsG2eZvKYlo2CKaT8MITz",
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$setupAttempts = $stripe->setupAttempts->all([
  'limit' => 3,
  'setup_intent' => 'seti_1ErTsG2eZvKYlo2CKaT8MITz',
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

SetupAttemptListParams params =
  SetupAttemptListParams.builder()
    .setLimit(3L)
    .setSetupIntent("seti_1ErTsG2eZvKYlo2CKaT8MITz")
    .build();

StripeCollection<SetupAttempt> stripeCollection =
  client.v1().setupAttempts().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupAttempts = await stripe.setupAttempts.list({
  limit: 3,
  setup_intent: 'seti_1ErTsG2eZvKYlo2CKaT8MITz',
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.SetupAttemptListParams{
  SetupIntent: stripe.String("seti_1ErTsG2eZvKYlo2CKaT8MITz"),
}
params.Limit = stripe.Int64(3)
result := sc.V1SetupAttempts.List(context.TODO(), params)
```

```dotnet
var options = new SetupAttemptListOptions
{
    Limit = 3,
    SetupIntent = "seti_1ErTsG2eZvKYlo2CKaT8MITz",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.SetupAttempts;
StripeList<SetupAttempt> setupAttempts = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/setup_attempts",
  "has_more": false,
  "data": [
    {
      "id": "setatt_1ErTsH2eZvKYlo2CI7ukcoF7",
      "object": "setup_attempt",
      "application": null,
      "created": 1562004309,
      "customer": null,
      "flow_directions": null,
      "livemode": false,
      "on_behalf_of": null,
      "payment_method": "pm_1ErTsG2eZvKYlo2CH0DNen59",
      "payment_method_details": {
        "card": {
          "three_d_secure": null
        },
        "type": "card"
      },
      "setup_error": null,
      "setup_intent": "seti_1ErTsG2eZvKYlo2CKaT8MITz",
      "status": "succeeded",
      "usage": "off_session"
    }
  ]
}
```