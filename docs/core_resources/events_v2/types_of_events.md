# Types of events

This is a list of all public [thin events](https://docs.stripe.com/event-destinations.md#thin-events) we currently send for /v1 and /v2 resources, which are continually evolving and expanding. The payload of thin events is unversioned. During processing, you must fetch the versioned event from the API or fetch the resource’s current state.

## API event types

### `v1.billing.meter.error_report_triggered`

Occurs when a Meter has invalid async usage events.

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

- `type` (string, value is "v1.billing.meter.error_report_triggered")
  The type of the event.

## Fetched attributes

- `changes` (object, nullable)
  Before and after changes for the primary related object.

- `data` (object)
  Additional data about the event.

  - `data.developer_message_summary` (string)
    Extra field included in the event’s `data` when fetched from /v2/events.

  - `data.reason` (object)
    This contains information about why meter error happens.

    - `data.reason.error_count` (integer)
      The total error count within this window.

    - `data.reason.error_types` (array of objects)
      The error details.

      - `data.reason.error_types.code` (enum)Possible enum values:
        - `archived_meter`
          Enum value: archived_meter.

        - `meter_event_customer_not_found`
          Enum value: meter_event_customer_not_found.

        - `meter_event_dimension_count_too_high`
          Enum value: meter_event_dimension_count_too_high.

        - `meter_event_invalid_value`
          Enum value: meter_event_invalid_value.

        - `meter_event_no_customer_defined`
          Enum value: meter_event_no_customer_defined.

        - `missing_dimension_payload_keys`
          Enum value: missing_dimension_payload_keys.

        - `no_meter`
          Enum value: no_meter.

        - `timestamp_in_future`
          Enum value: timestamp_in_future.

        - `timestamp_too_far_in_past`
          Enum value: timestamp_too_far_in_past.

      - `data.reason.error_types.error_count` (integer)
        The number of errors of this type.

      - `data.reason.error_types.sample_errors` (array of objects)
        A list of sample errors of this type.

        - `data.reason.error_types.sample_errors.error_message` (string)
          The error message.

        - `data.reason.error_types.sample_errors.request` (object)
          The request causes the error.

          - `data.reason.error_types.sample_errors.request.identifier` (string)
            The request idempotency key.

  - `data.validation_end` (timestamp)
    The end of the window that is encapsulated by this summary.

  - `data.validation_start` (timestamp)
    The start of the window that is encapsulated by this summary.

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

### `v1.billing.meter.no_meter_found`

Occurs when a Meter's id is missing or invalid in async usage events.

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

- `type` (string, value is "v1.billing.meter.no_meter_found")
  The type of the event.

## Fetched attributes

- `changes` (object, nullable)
  Before and after changes for the primary related object.

- `data` (object)
  Additional data about the event.

  - `data.developer_message_summary` (string)
    Extra field included in the event’s `data` when fetched from /v2/events.

  - `data.reason` (object)
    This contains information about why meter error happens.

    - `data.reason.error_count` (integer)
      The total error count within this window.

    - `data.reason.error_types` (array of objects)
      The error details.

      - `data.reason.error_types.code` (enum)Possible enum values:
        - `archived_meter`
          Enum value: archived_meter.

        - `meter_event_customer_not_found`
          Enum value: meter_event_customer_not_found.

        - `meter_event_dimension_count_too_high`
          Enum value: meter_event_dimension_count_too_high.

        - `meter_event_invalid_value`
          Enum value: meter_event_invalid_value.

        - `meter_event_no_customer_defined`
          Enum value: meter_event_no_customer_defined.

        - `missing_dimension_payload_keys`
          Enum value: missing_dimension_payload_keys.

        - `no_meter`
          Enum value: no_meter.

        - `timestamp_in_future`
          Enum value: timestamp_in_future.

        - `timestamp_too_far_in_past`
          Enum value: timestamp_too_far_in_past.

      - `data.reason.error_types.error_count` (integer)
        The number of errors of this type.

      - `data.reason.error_types.sample_errors` (array of objects)
        A list of sample errors of this type.

        - `data.reason.error_types.sample_errors.error_message` (string)
          The error message.

        - `data.reason.error_types.sample_errors.request` (object)
          The request causes the error.

          - `data.reason.error_types.sample_errors.request.identifier` (string)
            The request idempotency key.

  - `data.validation_end` (timestamp)
    The end of the window that is encapsulated by this summary.

  - `data.validation_start` (timestamp)
    The start of the window that is encapsulated by this summary.

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

### `v2.core.account_link.returned`

Occurs when the generated AccountLink is completed.

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

- `type` (string, value is "v2.core.account_link.returned")
  The type of the event.

## Fetched attributes

- `changes` (object, nullable)
  Before and after changes for the primary related object.

- `data` (object)
  Additional data about the event.

  - `data.account_id` (string)
    The ID of the v2 account.

  - `data.configurations` (array of enums)
    Configurations on the Account that was onboarded via the account link.
Possible enum values:
    - `customer`
      The Account can be used as a customer.

    - `merchant`
      The Account can be used as a merchant.

    - `recipient`
      The Account can be used as a recipient.

  - `data.use_case` (enum)
    The use case type of the account link that has been completed.
Possible enum values:
    - `account_onboarding`
      Refers to the `account_onboarding` use case.

    - `account_update`
      Refers to the `account_update` use case.

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

### `v2.core.account_person.created`

Occurs when a Person is created.

Related object: [Person](https://docs.stripe.com/api/v2/core/persons/object.md)

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

- `type` (string, value is "v2.core.account_person.created")
  The type of the event.

## Fetched attributes

- `changes` (object, nullable)
  Before and after changes for the primary related object.

- `data` (object)
  Additional data about the event.

  - `data.account_id` (string)
    The ID of the v2 account.

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

### `v2.core.account_person.deleted`

Occurs when a Person is deleted.

Related object: [Person](https://docs.stripe.com/api/v2/core/persons/object.md)

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

- `type` (string, value is "v2.core.account_person.deleted")
  The type of the event.

## Fetched attributes

- `changes` (object, nullable)
  Before and after changes for the primary related object.

- `data` (object)
  Additional data about the event.

  - `data.account_id` (string)
    The ID of the v2 account.

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

### `v2.core.account_person.updated`

Occurs when a Person is updated.

Related object: [Person](https://docs.stripe.com/api/v2/core/persons/object.md)

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

- `type` (string, value is "v2.core.account_person.updated")
  The type of the event.

## Fetched attributes

- `changes` (object, nullable)
  Before and after changes for the primary related object.

- `data` (object)
  Additional data about the event.

  - `data.account_id` (string)
    The ID of the v2 account.

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

### `v2.core.account.closed`

This event occurs when an account is closed.

Related object: [Account](https://docs.stripe.com/api/v2/core/accounts/object.md)

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

- `type` (string, value is "v2.core.account.closed")
  The type of the event.

## Fetched attributes

- `changes` (object, nullable)
  Before and after changes for the primary related object.

- `data` (object)
  Additional data about the event.

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

### `v2.core.account.created`

Occurs when an Account is created.

Related object: [Account](https://docs.stripe.com/api/v2/core/accounts/object.md)

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

- `type` (string, value is "v2.core.account.created")
  The type of the event.

## Fetched attributes

- `changes` (object, nullable)
  Before and after changes for the primary related object.

- `data` (object)
  Additional data about the event.

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

### `v2.core.account.updated`

Occurs when an Account is updated.

Related object: [Account](https://docs.stripe.com/api/v2/core/accounts/object.md)

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

- `type` (string, value is "v2.core.account.updated")
  The type of the event.

## Fetched attributes

- `changes` (object, nullable)
  Before and after changes for the primary related object.

- `data` (object)
  Additional data about the event.

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

### `v2.core.account[configuration.customer].capability_status_updated`

Occurs when the status of an Account's customer configuration capability is updated.

Related object: [Account](https://docs.stripe.com/api/v2/core/accounts/object.md)

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

- `type` (string, value is "v2.core.account[configuration.customer].capability_status_updated")
  The type of the event.

## Fetched attributes

- `changes` (object, nullable)
  Before and after changes for the primary related object.

- `data` (object)
  Additional data about the event.

  - `data.updated_capability` (enum)
    The capability which had its status updated.
Possible enum values:
    - `automatic_indirect_tax`
      Refers to the `customer.capabilities.card_payments` capability.

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

### `v2.core.account[configuration.customer].updated`

Occurs when an Account's customer configuration is updated.

Related object: [Account](https://docs.stripe.com/api/v2/core/accounts/object.md)

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

- `type` (string, value is "v2.core.account[configuration.customer].updated")
  The type of the event.

## Fetched attributes

- `changes` (object, nullable)
  Before and after changes for the primary related object.

- `data` (object)
  Additional data about the event.

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

### `v2.core.account[configuration.merchant].capability_status_updated`

Occurs when the status of an Account's merchant configuration capability is updated.

Related object: [Account](https://docs.stripe.com/api/v2/core/accounts/object.md)

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

- `type` (string, value is "v2.core.account[configuration.merchant].capability_status_updated")
  The type of the event.

## Fetched attributes

- `changes` (object, nullable)
  Before and after changes for the primary related object.

- `data` (object)
  Additional data about the event.

  - `data.updated_capability` (enum)
    The capability which had its status updated.
Possible enum values:
    - `ach_debit_payments`
      Refers to the `merchant.capabilities.ach_debit_payments` capability.

    - `acss_debit_payments`
      Refers to the `merchant.capabilities.acss_debit_payments` capability.

    - `affirm_payments`
      Refers to the `merchant.capabilities.affirm_payments` capability.

    - `afterpay_clearpay_payments`
      Refers to the `merchant.capabilities.afterpay_clearpay_payments` capability.

    - `alma_payments`
      Refers to the `merchant.capabilities.alma_payments` capability.

    - `amazon_pay_payments`
      Refers to the `merchant.capabilities.amazon_pay_payments` capability.

    - `au_becs_debit_payments`
      Refers to the `merchant.capabilities.au_becs_debit_payments` capability.

    - `bacs_debit_payments`
      Refers to the `merchant.capabilities.bacs_debit_payments` capability.

    - `bancontact_payments`
      Refers to the `merchant.capabilities.bancontact_payments` capability.

    - `blik_payments`
      Refers to the `merchant.capabilities.blik_payments` capability.

    - `boleto_payments`
      Refers to the `merchant.capabilities.boleto_payments` capability.

    - `card_payments`
      Refers to the `merchant.capabilities.card_payments` capability.

    - `cartes_bancaires_payments`
      Refers to the `merchant.capabilities.cartes_bancaires_payments` capability.

    - `cashapp_payments`
      Refers to the `merchant.capabilities.cashapp_payments` capability.

    - `eps_payments`
      Refers to the `merchant.capabilities.eps_payments` capability.

    - `fpx_payments`
      Refers to the `merchant.capabilities.fpx_payments` capability.

    - `gb_bank_transfer_payments`
      Refers to the `merchant.capabilities.gb_bank_transfer_payments` capability.

    - `grabpay_payments`
      Refers to the `merchant.capabilities.grabpay_payments` capability.

    - `ideal_payments`
      Refers to the `merchant.capabilities.ideal_payments` capability.

    - `jcb_payments`
      Refers to the `merchant.capabilities.jcb_payments` capability.

    - `jp_bank_transfer_payments`
      Refers to the `merchant.capabilities.jp_bank_transfer_payments` capability.

    - `kakao_pay_payments`
      Refers to the `merchant.capabilities.kakao_pay_payments` capability.

    - `klarna_payments`
      Refers to the `merchant.capabilities.klarna_payments` capability.

    - `konbini_payments`
      Refers to the `merchant.capabilities.konbini_payments` capability.

    - `kr_card_payments`
      Refers to the `merchant.capabilities.kr_card_payments` capability.

    - `link_payments`
      Refers to the `merchant.capabilities.link_payments` capability.

    - `mobilepay_payments`
      Refers to the `merchant.capabilities.mobilepay_payments` capability.

    - `multibanco_payments`
      Refers to the `merchant.capabilities.multibanco_payments` capability.

    - `mx_bank_transfer_payments`
      Refers to the `merchant.capabilities.mx_bank_transfer_payments` capability.

    - `naver_pay_payments`
      Refers to the `merchant.capabilities.naver_pay_payments` capability.

    - `oxxo_payments`
      Refers to the `merchant.capabilities.oxxo_payments` capability.

    - `p24_payments`
      Refers to the `merchant.capabilities.p24_payments` capability.

    - `pay_by_bank_payments`
      Refers to the `merchant.capabilities.pay_by_bank_payments` capability.

    - `payco_payments`
      Refers to the `merchant.capabilities.payco_payments` capability.

    - `paynow_payments`
      Refers to the `merchant.capabilities.paynow_payments` capability.

    - `promptpay_payments`
      Refers to the `merchant.capabilities.promptpay_payments` capability.

    - `revolut_pay_payments`
      Refers to the `merchant.capabilities.revolut_pay_payments` capability.

    - `samsung_pay_payments`
      Refers to the `merchant.capabilities.samsung_pay_payments` capability.

    - `sepa_bank_transfer_payments`
      Refers to the `merchant.capabilities.sepa_bank_transfer_payments` capability.

    - `sepa_debit_payments`
      Refers to the `merchant.capabilities.sepa_debit_payments` capability.

    - `stripe_balance.payouts`
      Refers to the `merchant.capabilities.stripe_balance.payouts` capability.

    - `swish_payments`
      Refers to the `merchant.capabilities.swish_payments` capability.

    - `twint_payments`
      Refers to the `merchant.capabilities.twint_payments` capability.

    - `us_bank_transfer_payments`
      Refers to the `merchant.capabilities.us_bank_transfer_payments` capability.

    - `zip_payments`
      Refers to the `merchant.capabilities.zip_payments` capability.

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

### `v2.core.account[configuration.merchant].updated`

Occurs when an Account's merchant configuration is updated.

Related object: [Account](https://docs.stripe.com/api/v2/core/accounts/object.md)

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

- `type` (string, value is "v2.core.account[configuration.merchant].updated")
  The type of the event.

## Fetched attributes

- `changes` (object, nullable)
  Before and after changes for the primary related object.

- `data` (object)
  Additional data about the event.

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

### `v2.core.account[configuration.recipient].capability_status_updated`

Occurs when the status of an Account's recipient configuration capability is updated.

Related object: [Account](https://docs.stripe.com/api/v2/core/accounts/object.md)

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

- `type` (string, value is "v2.core.account[configuration.recipient].capability_status_updated")
  The type of the event.

## Fetched attributes

- `changes` (object, nullable)
  Before and after changes for the primary related object.

- `data` (object)
  Additional data about the event.

  - `data.updated_capability` (enum)
    The capability which had its status updated.
Possible enum values:
    - `bank_accounts.local`
      Refers to the `recipient.capabilities.bank_accounts.local` capability.

    - `bank_accounts.wire`
      Refers to the `recipient.capabilities.bank_accounts.wire` capability.

    - `cards`
      Refers to the `recipient.capabilities.cards` capability.

    - `stripe.transfers`
      DEPRECATED: use RECIPIENT_CONFIG__STRIPE_TRANSFERS_CAPABILITY instead – Refers to the `recipient.capabilities.stripe.transfers` capability.

    - `stripe_balance.payouts`
      Refers to the `recipient.capabilities.stripe_balance.payouts` capability.

    - `stripe_balance.stripe_transfers`
      Refers to the `recipient.capabilities.stripe_balance.stripe_transfers` capability.

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

### `v2.core.account[configuration.recipient].updated`

Occurs when a Recipient's configuration is updated.

Related object: [Account](https://docs.stripe.com/api/v2/core/accounts/object.md)

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

- `type` (string, value is "v2.core.account[configuration.recipient].updated")
  The type of the event.

## Fetched attributes

- `changes` (object, nullable)
  Before and after changes for the primary related object.

- `data` (object)
  Additional data about the event.

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

### `v2.core.account[defaults].updated`

This event occurs when account defaults are created or updated.

Related object: [Account](https://docs.stripe.com/api/v2/core/accounts/object.md)

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

- `type` (string, value is "v2.core.account[defaults].updated")
  The type of the event.

## Fetched attributes

- `changes` (object, nullable)
  Before and after changes for the primary related object.

- `data` (object)
  Additional data about the event.

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

### `v2.core.account[future_requirements].updated`

Occurs when an Account's future requirements are updated.

Related object: [Account](https://docs.stripe.com/api/v2/core/accounts/object.md)

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

- `type` (string, value is "v2.core.account[future_requirements].updated")
  The type of the event.

## Fetched attributes

- `changes` (object, nullable)
  Before and after changes for the primary related object.

- `data` (object)
  Additional data about the event.

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

### `v2.core.account[identity].updated`

Occurs when an Identity is updated.

Related object: [Account](https://docs.stripe.com/api/v2/core/accounts/object.md)

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

- `type` (string, value is "v2.core.account[identity].updated")
  The type of the event.

## Fetched attributes

- `changes` (object, nullable)
  Before and after changes for the primary related object.

- `data` (object)
  Additional data about the event.

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

### `v2.core.account[requirements].updated`

Occurs when an Account's requirements are updated.

Related object: [Account](https://docs.stripe.com/api/v2/core/accounts/object.md)

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

- `type` (string, value is "v2.core.account[requirements].updated")
  The type of the event.

## Fetched attributes

- `changes` (object, nullable)
  Before and after changes for the primary related object.

- `data` (object)
  Additional data about the event.

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