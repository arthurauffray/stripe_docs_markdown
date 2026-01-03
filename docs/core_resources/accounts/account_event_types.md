# Account event types

This is a list of all public [thin events](https://docs.stripe.com/event-destinations.md#thin-events) we currently send for updates to Account, which are continually evolving and expanding. The payload of thin events is unversioned. During processing, you must fetch the versioned event from the API or fetch the resource’s current state.

## API event types

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