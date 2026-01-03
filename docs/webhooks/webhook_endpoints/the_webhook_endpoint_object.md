# The Webhook Endpoint object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `api_version` (string, nullable)
  The API version events are rendered as for this webhook endpoint.

- `application` (string, nullable)
  The ID of the associated Connect application.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `description` (string, nullable)
  An optional description of what the webhook is used for.

- `enabled_events` (array of strings)
  The list of events to enable for this endpoint. `['*']` indicates that all events are enabled, except those that require explicit selection.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `secret` (string)
  The endpoint’s secret, used to generate [webhook signatures](https://docs.stripe.com/webhooks/signatures.md). Only returned at creation.

- `status` (string)
  The status of the webhook. It can be `enabled` or `disabled`.

- `url` (string)
  The URL of the webhook endpoint.

### The Webhook Endpoint object

```json
{
  "id": "we_1Mr5jULkdIwHu7ix1ibLTM0x",
  "object": "webhook_endpoint",
  "api_version": null,
  "application": null,
  "created": 1680122196,
  "description": null,
  "enabled_events": [
    "charge.succeeded",
    "charge.failed"
  ],
  "livemode": false,
  "metadata": {},
  "secret": "whsec_wRNftLajMZNeslQOP6vEPm4iVx5NlZ6z",
  "status": "enabled",
  "url": "https://example.com/my/webhook/endpoint"
}
```