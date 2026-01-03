# The ForwardingRequest object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `metadata` (object, nullable)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `payment_method` (string)
  The PaymentMethod to insert into the forwarded request. Forwarding previously consumed PaymentMethods is allowed.

- `replacements` (array of enums)
  The field kinds to be replaced in the forwarded request.
Possible enum values:
  - `card_cvc`
    Replace the card cvc field

  - `card_expiry`
    Replace the card expiry fields like month and year

  - `card_number`
    Replace the card number field

  - `cardholder_name`
    Replace the cardholder name field

  - `request_signature`
    Calculate and replace the request signature field

- `request_context` (object, nullable)
  Context about the request from Stripe’s servers to the destination endpoint.

  - `request_context.destination_duration` (integer)
    The time it took in milliseconds for the destination endpoint to respond.

  - `request_context.destination_ip_address` (string)
    The IP address of the destination.

- `request_details` (object, nullable)
  The request that was sent to the destination endpoint. We redact any sensitive fields.

  - `request_details.body` (string)
    The body payload to send to the destination endpoint.

  - `request_details.headers` (array of objects)
    The headers to include in the forwarded request. Can be omitted if no additional headers (excluding Stripe-generated ones such as the Content-Type header) should be included.

    - `request_details.headers.name` (string)
      The header name.

    - `request_details.headers.value` (string)
      The header value.

  - `request_details.http_method` (enum)
    The HTTP method used to call the destination endpoint.
Possible enum values:
    - `POST`
      The HTTP POST method

- `response_details` (object, nullable)
  The response that the destination endpoint returned to us. We redact any sensitive fields.

  - `response_details.body` (string)
    The response body from the destination endpoint to Stripe.

  - `response_details.headers` (array of objects)
    HTTP headers that the destination endpoint returned.

    - `response_details.headers.name` (string)
      The header name.

    - `response_details.headers.value` (string)
      The header value.

  - `response_details.status` (integer)
    The HTTP status code that the destination endpoint returned.

- `url` (string, nullable)
  The destination URL for the forwarded request. Must be supported by the config.

### The ForwardingRequest object

```json
{
  "id": "fwdreq_123",
  "object": "forwarding.request",
  "created": 1234567890,
  "livemode": false,
  "payment_method": "pm_456",
  "request_details": {
    "body": "{\"amount\":{\"value\":1000,\"currency\":\"usd\"},\"paymentMethod\":{\"number\":\"424242******4242\",\"expiryMonth\":\"03\",\"expiryYear\":\"2030\",\"cvc\":\"***\",\"holderName\":\"First Last\"},\"reference\":\"{{REFERENCE_ID}}\"}",
    "headers": [
      {
        "name": "Destination-API-Key",
        "value": "{{DESTINATION_API_KEY}}"
      },
      {
        "name": "Destination-Idempotency-Key",
        "value": "{{DESTINATION_IDEMPOTENCY_KEY}}"
      },
      {
        "name": "Content-Type",
        "value": "application/json"
      }
    ],
    "http_method": "POST"
  },
  "request_context": {
    "destination_ip_address": "35.190.113.80",
    "destination_duration": 234
  },
  "response_details": {
    "body": "{\"transactionId\":\"example1234\"}",
    "headers": [
      {
        "name": "Content-Type",
        "value": "application/json;charset=UTF-8"
      }
    ],
    "status": 200
  },
  "url": "https://endpoint-url/v1/payments",
  "replacements": [
    "card_number",
    "card_expiry",
    "card_cvc",
    "cardholder_name"
  ]
}
```