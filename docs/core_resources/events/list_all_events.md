# List all events

List events, going back up to 30 days. Each event data is rendered according to Stripe API version at its creation time, specified in [event object](https://docs.stripe.com/api/events/object.md) `api_version` attribute (not according to your current Stripe API version or `Stripe-Version` header).

## Returns

A dictionary with a `data` property that contains an array of up to `limit` events, starting after event `starting_after`. Each entry in the array is a separate event object. If no more events are available, the resulting array will be empty.

## Parameters

- `created` (object, optional)
  Only return events that were created during the given date interval.

  - `created.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `created.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `created.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `created.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `delivery_success` (boolean, optional)
  Filter events by whether all webhooks were successfully delivered. If false, events which are still pending or have failed all delivery attempts to a webhook endpoint will be returned.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `type` (string, optional)
  A string containing a specific event name, or group of events using * as a wildcard. The list will be filtered to include only events with a matching event property.

- `types` (array of strings, optional)
  An array of up to 20 strings containing specific event names. The list will be filtered to include only events with a matching event property. You may pass either `type` or `types`, but not both.

```curl
curl -G https://api.stripe.com/v1/events \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe events list  \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

events = client.v1.events.list({limit: 3})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

events = client.v1.events.list({"limit": 3})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$events = $stripe->events->all(['limit' => 3]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

EventListParams params = EventListParams.builder().setLimit(3L).build();

StripeCollection<Event> stripeCollection = client.v1().events().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const events = await stripe.events.list({
  limit: 3,
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.EventListParams{}
params.Limit = stripe.Int64(3)
result := sc.V1Events.List(context.TODO(), params)
```

```dotnet
var options = new EventListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Events;
StripeList<Event> events = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/events",
  "has_more": false,
  "data": [
    {
      "id": "evt_1NG8Du2eZvKYlo2CUI79vXWy",
      "object": "event",
      "api_version": "2019-02-19",
      "created": 1686089970,
      "data": {
        "object": {
          "id": "seti_1NG8Du2eZvKYlo2C9XMqbR0x",
          "object": "setup_intent",
          "application": null,
          "automatic_payment_methods": null,
          "cancellation_reason": null,
          "client_secret": "seti_1NG8Du2eZvKYlo2C9XMqbR0x_secret_O2CdhLwGFh2Aej7bCY7qp8jlIuyR8DJ",
          "created": 1686089970,
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
          "payment_method": "pm_1NG8Du2eZvKYlo2CYzzldNr7",
          "payment_method_options": {
            "acss_debit": {
              "currency": "cad",
              "mandate_options": {
                "interval_description": "First day of every month",
                "payment_schedule": "interval",
                "transaction_type": "personal"
              },
              "verification_method": "automatic"
            }
          },
          "payment_method_types": [
            "acss_debit"
          ],
          "single_use_mandate": null,
          "status": "requires_confirmation",
          "usage": "off_session"
        }
      },
      "livemode": false,
      "pending_webhooks": 0,
      "request": {
        "id": null,
        "idempotency_key": null
      },
      "type": "setup_intent.created"
    }
  ]
}
```