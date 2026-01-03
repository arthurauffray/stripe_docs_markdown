# List all SetupIntents

Returns a list of SetupIntents.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` SetupIntents, starting after SetupIntent `starting_after`. Each entry in the array is a separate SetupIntent object. If no more SetupIntents are available, the resulting array will be empty.

## Parameters

- `attach_to_self` (boolean, optional)
  If present, the SetupIntent’s payment method will be attached to the in-context Stripe Account.

  It can only be used for this Stripe Account’s own money movement flows like InboundTransfer and OutboundTransfers. It cannot be set to true when setting up a PaymentMethod for a Customer, and defaults to false when attaching a PaymentMethod to a Customer.

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

- `customer` (string, optional)
  Only return SetupIntents for the customer specified by this customer ID.

- `customer_account` (string, optional)
  Only return SetupIntents for the account specified by this customer ID.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `payment_method` (string, optional)
  Only return SetupIntents that associate with the specified payment method.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/setup_intents \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe setup_intents list  \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

setup_intents = client.v1.setup_intents.list({limit: 3})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

setup_intents = client.v1.setup_intents.list({"limit": 3})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$setupIntents = $stripe->setupIntents->all(['limit' => 3]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

SetupIntentListParams params = SetupIntentListParams.builder().setLimit(3L).build();

StripeCollection<SetupIntent> stripeCollection =
  client.v1().setupIntents().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntents = await stripe.setupIntents.list({
  limit: 3,
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.SetupIntentListParams{}
params.Limit = stripe.Int64(3)
result := sc.V1SetupIntents.List(context.TODO(), params)
```

```dotnet
var options = new SetupIntentListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.SetupIntents;
StripeList<SetupIntent> setupIntents = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/setup_intents",
  "has_more": false,
  "data": [
    {
      "id": "seti_1Mm8s8LkdIwHu7ix0OXBfTRG",
      "object": "setup_intent",
      "application": null,
      "cancellation_reason": null,
      "client_secret": "seti_1Mm8s8LkdIwHu7ix0OXBfTRG_secret_NXDICkPqPeiBTAFqWmkbff09lRmSVXe",
      "created": 1678942624,
      "customer": null,
      "description": null,
      "flow_directions": null,
      "last_setup_error": null,
      "latest_attempt": null,
      "livemode": false,
      "mandate": null,
      "metadata": {},
      "next_action": null,
      "on_behalf_of": null,
      "payment_method": null,
      "payment_method_options": {
        "card": {
          "mandate_options": null,
          "network": null,
          "request_three_d_secure": "automatic"
        }
      },
      "payment_method_types": [
        "card"
      ],
      "single_use_mandate": null,
      "status": "requires_payment_method",
      "usage": "off_session"
    }
  ]
}
```