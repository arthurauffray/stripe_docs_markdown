# Retrieve an event

Retrieves the details of an event.

## Parameters

- `id` (string, required)
  Unique identifier for the object.

## Returns

## Response attributes

- `id` (string)
  Unique identifier for the event.

- `object` (string, value is "v2.core.event")
  String representing the object’s type. Objects of the same type share the same value of the object field.

- `changes` (object, nullable)
  Before and after changes for the primary related object.

- `context` (string, nullable)
  Authentication context needed to fetch the event or related object.

- `created` (timestamp)
  Time at which the object was created.

- `data` (object, nullable)
  Additional data about the event.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `reason` (object, nullable)
  Reason for the event.

  - `reason.request` (object, nullable)
    Information on the API request that instigated the event.

    - `reason.request.id` (string)
      ID of the API request that caused the event.

    - `reason.request.idempotency_key` (string)
      The idempotency key transmitted during the request.

  - `reason.type` (enum)
    Event reason type.
Possible enum values:
    - `request`
      The event was published as the result of an API request.

- `related_object` (object, nullable)
  Object containing the reference to API resource relevant to the event.

  - `related_object.id` (string)
    Unique identifier for the object relevant to the event.

  - `related_object.type` (string)
    Object tag of the resource relevant to the event.

  - `related_object.url` (string)
    URL to retrieve the resource.

- `type` (string)
  The type of the event.

## Error Codes

| HTTP status code | Code      | Description                |
| ---------------- | --------- | -------------------------- |
| 404              | not_found | The resource wasn’t found. |

```curl
curl https://api.stripe.com/v2/core/events/evt_test_65RCjj4EqW1sabcjs2Z16RCMoNQdSQkOWvfL6L5uU2K40u \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: {{STRIPE_API_VERSION}}"
```

```cli
stripe v2 core events retrieve evt_test_65RCjj4EqW1sabcjs2Z16RCMoNQdSQkOWvfL6L5uU2K40u
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

event = client.v2.core.events.retrieve('evt_test_65RCjj4EqW1sabcjs2Z16RCMoNQdSQkOWvfL6L5uU2K40u')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

event = client.v2.core.events.retrieve(
  "evt_test_65RCjj4EqW1sabcjs2Z16RCMoNQdSQkOWvfL6L5uU2K40u",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$event = $stripe->v2->core->events->retrieve(
  'evt_test_65RCjj4EqW1sabcjs2Z16RCMoNQdSQkOWvfL6L5uU2K40u',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

EventRetrieveParams params = EventRetrieveParams.builder().build();

Event event =
  client.v2().core().events().retrieve(
    "evt_test_65RCjj4EqW1sabcjs2Z16RCMoNQdSQkOWvfL6L5uU2K40u",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const event = await stripe.v2.core.events.retrieve(
  'evt_test_65RCjj4EqW1sabcjs2Z16RCMoNQdSQkOWvfL6L5uU2K40u'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.V2CoreEventRetrieveParams{}
result, err := sc.V2CoreEvents.Retrieve(
  context.TODO(), "evt_test_65RCjj4EqW1sabcjs2Z16RCMoNQdSQkOWvfL6L5uU2K40u", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V2.Core.Events;
Stripe.V2.Core.Event result = service.Get(
    "evt_test_65RCjj4EqW1sabcjs2Z16RCMoNQdSQkOWvfL6L5uU2K40u");
```

### Response

```json
{
  "id": "evt_test_65RCjj4EqW1sabcjs2Z16RCMoNQdSQkOWvfL6L5uU2K40u",
  "object": "v2.core.event",
  "context": null,
  "created": "2024-09-26T17:46:22.134Z",
  "data": {
    "developer_message_summary": "There is 1 invalid event",
    "reason": {
      "error_count": 1,
      "error_types": [
        {
          "code": "meter_event_no_customer_defined",
          "error_count": 1,
          "sample_errors": [
            {
              "error_message": "Customer mapping key stripe_customer_id not found in payload.",
              "request": {
                "identifier": "cb447754-6880-45c2-8f2f-ef19b6ce81e9"
              }
            }
          ]
        }
      ]
    },
    "validation_end": "2024-09-26T17:46:20.000Z",
    "validation_start": "2024-09-26T17:46:10.000Z"
  },
  "livemode": false,
  "reason": null,
  "related_object": {
    "id": "mtr_test_61RCjiqdTDC91zgip41IqPCzPnxqqSVc",
    "type": "billing.meter",
    "url": "/v1/billing/meters/mtr_test_61RCjiqdTDC91zgip41IqPCzPnxqqSVc"
  },
  "type": "v1.billing.meter.error_report_triggered"
}
```