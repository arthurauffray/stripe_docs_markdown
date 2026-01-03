# EventDestination event types

This is a list of all public [thin events](https://docs.stripe.com/event-destinations.md#thin-events) we currently send for updates to EventDestination, which are continually evolving and expanding. The payload of thin events is unversioned. During processing, you must fetch the versioned event from the API or fetch the resource’s current state.

## API event types

### `v2.core.event_destination.ping`

A ping event used to test the connection to an EventDestination.

Related object: [EventDestination](https://docs.stripe.com/api/v2/core/event_destinations/object.md)

## Attributes

- `id` (string)
  Unique identifier for the event.

- `object` (string, value is "v2.core.event")
  String representing the object’s type. Objects of the same type share the same value of the object field.

- `context` (string, nullable)
  Authentication context needed to fetch the event or related object.

- `created` (timestamp)
  Time at which the object was created.

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

- `type` (string, value is "v2.core.event_destination.ping")
  The type of the event.

## Fetched attributes

- `changes` (object, nullable)
  Before and after changes for the primary related object.

- `data` (object)
  Additional data about the event.

### Event payload

```json
{
  "context": null,
  "created": "2025-01-01T00:00:00.000Z",
  "id": "evt_65RCjj4EqW1sabcjs2Z16RCMoNQdSQkOWvfL6L5uU2K40u",
  "object": "v2.core.event",
  "reason": {
    "type": "request",
    "request": {
      "id": "req_v24sUK2aV6o01RdVU",
      "idempotency_key": "fe21992d-e123-3f8c-bc90-fec93712bcb2"
    }
  },
  "related_object": {
    "id": "ed_65SDS7HTasdQYsDClFT16CGd2aE2kBpeAvvRnBUcS2me",
    "type": "v2.core.event_destination",
    "url": "/v2/core/event_destinations/ed_65SDS7HTasdQYsDClFT16CGd2aE2kBpeAvvRnBUcS2me"
  },
  "type": "v2.core.event_destination.ping",
  "livemode": true
}
```

### Event handler

```curl
# Select a client library to see examples of
# parsing and retrieving event details.
```

### Event handler

```bash
# Select a client library to see examples of
# parsing and retrieving event details.
```

### Event handler

```ruby
client = Stripe::StripeClient.new("{{YOUR_API_KEY}}")

endpoint_secret = 'whsec_...'
signature_header = request.env['HTTP_STRIPE_SIGNATURE']

thin_event = client.parse_thin_event(
  payload,
  signature_header,
  endpoint_secret
)

event = client.v2.core.events.retrieve(thin_event.id)
```

### Event handler

```python
client = StripeClient("{{YOUR_API_KEY}}")

endpoint_secret = 'whsec_...'
signature_header = ''

thin_event = client.parse_thin_event(
  payload,
  signature_header,
  endpoint_secret
)

event = client.v2.core.events.retrieve(thin_event.id)
```

### Event handler

```php
$stripe = new StripeStripeClient('{{YOUR_API_KEY}}');

$endpoint_secret = 'whsec_...';
$signature_header = $_SERVER['HTTP_STRIPE_SIGNATURE'];

$thin_event = $client->parseThinEvent(
  $payload,
  $signature_header,
  $endpoint_secret
);

$event = $client->v2->core->events->retrieve($thin_event->id);
```

### Event handler

```java
StripeClient client = new StripeClient("{{YOUR_API_KEY}}");

String signatureHeader = request.headers("Stripe-Signature");
String endpointSecret = "whsec_...";

com.stripe.model.ThinEvent thinEvent = client.parseThinEvent(
  payload,
  signatureHeader,
  endpointSecret
);

com.stripe.model.v2.Event event = client.v2().core().events().retrieve(
  thinEvent.getId()
);
```

### Event handler

```javascript
const stripe = require('stripe')('{{YOUR_API_KEY}}');

const endpoint_secret = 'whsec_...'
const signature_header = '...'

const thinEvent = stripe.parseThinEvent(
  payload,
  signature_header,
  endpoint_secret
);

const event = await stripe.v2.core.events.retrieve(thinEvent.id);

```

### Event handler

```go
err = webhook.ValidatePayload(
  payload,
  signatureHeader,
  endpointSecret
)

if err != nil {
    fmt.Fprintf(os.Stderr, "Error reading request body: %v
", err)
    return
}

var thinEvent map[string]interface{}

if err := json.Unmarshal(payload, &thinEvent); err != nil {
    fmt.Fprintf(
      os.Stderr,
      "Failed to parse thin event body json: %v
", err.Error()
    )
    return
}

eventID := thinEvent["id"].(string)

var event map[string]interface{}
resp, err := client.RawRequest(
  http.MethodGet,
  "/v2/core/events/"+eventID,
  "",
  nil
)
if err != nil {
    fmt.Fprintf(
      os.Stderr,
      "Failed to get pull event: %v
",
      err.Error()
    )
    return
}

if err := json.Unmarshal(resp.RawJSON, &event); err != nil {
    fmt.Fprintf(
      os.Stderr,
      "Failed to parse pull event body json: %v
",
      err.Error()
    )
    return
}
```

### Event handler

```dotnet
var client = new StripeClient("{{YOUR_API_KEY}}");

string endpointSecret = "whsec_...";
string signatureHeader = Request.Headers["Stripe-Signature"];

var thinEvent = client.ParseThinEvent(
  payload,
  signatureHeader,
  endpointSecret
);

var event = await client.V2.Core.Events.GetAsync(thinEvent.Id);
```

### Fetched payload

```json
{
  "context": null,
  "created": "2025-01-01T00:00:00.000Z",
  "id": "evt_65RCjj4EqW1sabcjs2Z16RCMoNQdSQkOWvfL6L5uU2K40u",
  "object": "v2.core.event",
  "reason": {
    "type": "request",
    "request": {
      "id": "req_v24sUK2aV6o01RdVU",
      "idempotency_key": "fe21992d-e123-3f8c-bc90-fec93712bcb2"
    }
  },
  "related_object": {
    "id": "ed_65SDS7HTasdQYsDClFT16CGd2aE2kBpeAvvRnBUcS2me",
    "type": "v2.core.event_destination",
    "url": "/v2/core/event_destinations/ed_65SDS7HTasdQYsDClFT16CGd2aE2kBpeAvvRnBUcS2me"
  },
  "type": "v2.core.event_destination.ping",
  "livemode": true,
  "changes": {},
  "data": {}
}
```