# List event destinations

Lists all event destinations.

## Parameters

- `include` (array of enums, optional)
  Additional fields to include in the response. Currently supports `webhook_endpoint.url`.
Possible enum values:
  - `webhook_endpoint.url`
    Include parameter to expose `webhook_endpoint.url`.

- `limit` (integer, optional)
  The page size.

- `page` (string, optional)
  The requested page.

## Returns

## Response attributes

- `data` (array of objects)
  List of event destinations.

  - `data.id` (string)
    Unique identifier for the object.

  - `data.object` (string, value is "v2.core.event_destination")
    String representing the object’s type. Objects of the same type share the same value of the object field.

  - `data.amazon_eventbridge` (object, nullable)
    Amazon EventBridge configuration.

    - `data.amazon_eventbridge.aws_account_id` (string)
      The AWS account ID.

    - `data.amazon_eventbridge.aws_event_source_arn` (string)
      The ARN of the AWS event source.

    - `data.amazon_eventbridge.aws_event_source_status` (enum)
      The state of the AWS event source.
Possible enum values:
      - `active`
        The event source is in active state.

      - `deleted`
        The event source is in deleted state.

      - `pending`
        The event source is in pending state.

      - `unknown`
        The event source state cannot be retrieved.

  - `data.created` (timestamp)
    Time at which the object was created.

  - `data.description` (string)
    An optional description of what the event destination is used for.

  - `data.enabled_events` (array of strings)
    The list of events to enable for this endpoint.

  - `data.event_payload` (enum)
    Payload type of events being subscribed to.
Possible enum values:
    - `snapshot`
      Events from v1 APIs.

    - `thin`
      Events from v2 APIs.

  - `data.events_from` (array of enums, nullable)
    Where events should be routed from.
Possible enum values:
    - `other_accounts`
      Receive events from accounts connected to the account that owns the event destination.

    - `self`
      Receive events from the account that owns the event destination.

  - `data.livemode` (boolean)
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

  - `data.metadata` (map, nullable)
    Metadata.

  - `data.name` (string)
    Event destination name.

  - `data.snapshot_api_version` (string, nullable)
    If using the snapshot event payload, the API version events are rendered as.

  - `data.status` (enum)
    Status. It can be set to either enabled or disabled.
Possible enum values:
    - `disabled`
      Event destination is disabled.

    - `enabled`
      Event destination is enabled.

  - `data.status_details` (object, nullable)
    Additional information about event destination status.

    - `data.status_details.disabled` (object, nullable)
      Details about why the event destination has been disabled.

      - `data.status_details.disabled.reason` (enum)
        Reason event destination has been disabled.
Possible enum values:
        - `no_aws_event_source_exists`
          Event destination has been disabled because the underlying AWS event source does not exist.

        - `user`
          Event destination has been disabled by user.

  - `data.type` (enum)
    Event destination type.
Possible enum values:
    - `amazon_eventbridge`
      Amazon EventBridge.

    - `webhook_endpoint`
      Webhook endpoint.

  - `data.updated` (timestamp)
    Time at which the object was last updated.

  - `data.webhook_endpoint` (object, nullable)
    Webhook endpoint configuration.

    - `data.webhook_endpoint.signing_secret` (string, nullable)
      The signing secret of the webhook endpoint, only includable on creation.

    - `data.webhook_endpoint.url` (string, nullable)
      The URL of the webhook endpoint, includable.

- `next_page_url` (string, nullable)
  The next page url.

- `previous_page_url` (string, nullable)
  The previous page url.

```curl
curl -G https://api.stripe.com/v2/core/event_destinations \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: {{STRIPE_API_VERSION}}" \
  -d "include[0]"="webhook_endpoint.url"
```

```cli
stripe v2 core event_destinations list  \
  --include="webhook_endpoint.url"
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

event_destinations = client.v2.core.event_destinations.list({
  include: ['webhook_endpoint.url'],
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

event_destinations = client.v2.core.event_destinations.list({
  "include": ["webhook_endpoint.url"],
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$eventDestinations = $stripe->v2->core->eventDestinations->all([
  'include' => ['webhook_endpoint.url'],
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

EventDestinationListParams params =
  EventDestinationListParams.builder()
    .addInclude(EventDestinationListParams.Include.WEBHOOK_ENDPOINT__URL)
    .build();

StripeCollection<EventDestination> stripeCollection =
  client.v2().core().eventDestinations().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const eventDestinations = await stripe.v2.core.eventDestinations.list({
  include: ['webhook_endpoint.url'],
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.V2CoreEventDestinationListParams{
  Include: []*string{stripe.String("webhook_endpoint.url")},
}
result := sc.V2CoreEventDestinations.List(context.TODO(), params)
```

```dotnet
var options = new Stripe.V2.Core.EventDestinationListOptions
{
    Include = new List<string> { "webhook_endpoint.url" },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V2.Core.EventDestinations;
Stripe.V2.StripeList<Stripe.V2.Core.EventDestination> eventDestinations = service
    .List(options);
```

### Response

```json
{
  "data": [
    {
      "id": "ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6",
      "object": "v2.core.event_destination",
      "created": "2024-10-22T16:20:09.931Z",
      "description": "This is my event destination, I like it a lot",
      "enabled_events": [
        "v1.billing.meter.error_report_triggered"
      ],
      "event_payload": "thin",
      "events_from": [
        "self"
      ],
      "livemode": false,
      "metadata": {},
      "name": "My Event Destination",
      "snapshot_api_version": null,
      "status": "disabled",
      "status_details": {
        "disabled": {
          "reason": "user"
        }
      },
      "type": "webhook_endpoint",
      "updated": "2024-10-22T16:22:02.524Z",
      "webhook_endpoint": {
        "signing_secret": null,
        "url": null
      }
    }
  ],
  "next_page_url": null,
  "previous_page_url": null
}
```