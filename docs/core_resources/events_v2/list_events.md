# List events

List events, going back up to 30 days.

## Parameters

- `created` (object, optional)
  Set of filters to query events within a range of `created` timestamps.

  - `created.gt` (timestamp, optional)
    Filter for events created after the specified timestamp.

  - `created.gte` (timestamp, optional)
    Filter for events created at or after the specified timestamp.

  - `created.lt` (timestamp, optional)
    Filter for events created before the specified timestamp.

  - `created.lte` (timestamp, optional)
    Filter for events created at or before the specified timestamp.

- `limit` (integer, optional)
  The page size.

- `object_id` (string, optional)
  Primary object ID used to retrieve related events.

- `page` (string, optional)
  The requested page.

- `types` (array of strings, optional)
  An array of up to 20 strings containing specific event names.

## Returns

## Response attributes

- `data` (array of objects)
  List of events.

  - `data.id` (string)
    Unique identifier for the event.

  - `data.object` (string, value is "v2.core.event")
    String representing the object’s type. Objects of the same type share the same value of the object field.

  - `data.changes` (object, nullable)
    Before and after changes for the primary related object.

  - `data.context` (string, nullable)
    Authentication context needed to fetch the event or related object.

  - `data.created` (timestamp)
    Time at which the object was created.

  - `data.data` (object, nullable)
    Additional data about the event.

  - `data.livemode` (boolean)
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

  - `data.reason` (object, nullable)
    Reason for the event.

    - `data.reason.request` (object, nullable)
      Information on the API request that instigated the event.

      - `data.reason.request.id` (string)
        ID of the API request that caused the event.

      - `data.reason.request.idempotency_key` (string)
        The idempotency key transmitted during the request.

    - `data.reason.type` (enum)
      Event reason type.
Possible enum values:
      - `request`
        The event was published as the result of an API request.

  - `data.related_object` (object, nullable)
    Object containing the reference to API resource relevant to the event.

    - `data.related_object.id` (string)
      Unique identifier for the object relevant to the event.

    - `data.related_object.type` (string)
      Object tag of the resource relevant to the event.

    - `data.related_object.url` (string)
      URL to retrieve the resource.

  - `data.type` (string)
    The type of the event.

- `next_page_url` (string, nullable)
  The next page url.

- `previous_page_url` (string, nullable)
  The previous page url.

```curl
curl -G https://api.stripe.com/v2/core/events \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: {{STRIPE_API_VERSION}}" \
  -d object_id=mtr_test_61RCjiqdTDC91zgip41IqPCzPnxqqSVc
```

```cli
stripe v2 core events list  \
  --object-id=mtr_test_61RCjiqdTDC91zgip41IqPCzPnxqqSVc
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

events = client.v2.core.events.list({
  object_id: 'mtr_test_61RCjiqdTDC91zgip41IqPCzPnxqqSVc',
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

events = client.v2.core.events.list({
  "object_id": "mtr_test_61RCjiqdTDC91zgip41IqPCzPnxqqSVc",
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$events = $stripe->v2->core->events->all([
  'object_id' => 'mtr_test_61RCjiqdTDC91zgip41IqPCzPnxqqSVc',
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");
EventListParams params =
  EventListParams.builder()
    .setObjectId("mtr_test_61RCjiqdTDC91zgip41IqPCzPnxqqSVc")
    .build();
StripeCollection<Event> events = client.v2().core().events().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const events = await stripe.v2.core.events.list({
  object_id: 'mtr_test_61RCjiqdTDC91zgip41IqPCzPnxqqSVc',
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.V2CoreEventListParams{
  ObjectID: stripe.String("mtr_test_61RCjiqdTDC91zgip41IqPCzPnxqqSVc"),
}
result := sc.V2CoreEvents.List(context.TODO(), params)
```

```dotnet
var options = new Stripe.V2.Core.EventListOptions
{
    ObjectId = "mtr_test_61RCjiqdTDC91zgip41IqPCzPnxqqSVc",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V2.Core.Events;
Stripe.V2.StripeList<Stripe.V2.Core.Event> events = service.List(options);
```

### Response

```json
{
  "data": [
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
  ],
  "next_page_url": null,
  "previous_page_url": null
}
```