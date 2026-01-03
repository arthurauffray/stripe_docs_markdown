# Create a ForwardingRequest

Creates a ForwardingRequest object.

## Returns

Returns a ForwardingRequest object.

## Parameters

- `payment_method` (string, required)
  The PaymentMethod to insert into the forwarded request. Forwarding previously consumed PaymentMethods is allowed.

- `replacements` (array of enums, required)
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

- `request` (object, required)
  The request body and headers to be sent to the destination endpoint.

  - `request.body` (string, optional)
    The body payload to send to the destination endpoint.

  - `request.headers` (array of objects, optional)
    The headers to include in the forwarded request. Can be omitted if no additional headers (excluding Stripe-generated ones such as the Content-Type header) should be included.

    - `request.headers.name` (string, required)
      The header name.

    - `request.headers.value` (string, required)
      The header value.

- `url` (string, required)
  The destination URL for the forwarded request. Must be supported by the config.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/forwarding/requests \
  -u "<<YOUR_SECRET_KEY>>" \
  --data-urlencode url="https://endpoint-url/v1/payments" \
  -d payment_method=pm_card_visa \
  -d "replacements[0]"=card_number \
  -d "replacements[1]"=card_expiry \
  -d "replacements[2]"=card_cvc \
  -d "replacements[3]"=cardholder_name \
  --data-urlencode "request[body]"="{\"amount\":{\"value\":1000,\"currency\":\"usd\"},\"paymentMethod\":{\"number\":\"\",\"expiryMonth\":\"\",\"expiryYear\":\"\",\"cvc\":\"\",\"holderName\":\"\"},\"reference\":\"{{REFERENCE_ID}}\"}" \
  -d "request[headers][0][name]"=Destination-API-Key \
  -d "request[headers][0][value]"={{DESTINATION_API_KEY}} \
  -d "request[headers][1][name]"=Destination-Idempotency-Key \
  -d "request[headers][1][value]"={{DESTINATION_IDEMPOTENCY_KEY}}
```

```cli
stripe forwarding requests create  \
  --url="https://endpoint-url/v1/payments" \
  --payment-method=pm_card_visa \
  -d "replacements[0]"=card_number \
  -d "replacements[1]"=card_expiry \
  -d "replacements[2]"=card_cvc \
  -d "replacements[3]"=cardholder_name \
  -d "request[body]"="{\"amount\":{\"value\":1000,\"currency\":\"usd\"},\"paymentMethod\":{\"number\":\"\",\"expiryMonth\":\"\",\"expiryYear\":\"\",\"cvc\":\"\",\"holderName\":\"\"},\"reference\":\"{{REFERENCE_ID}}\"}" \
  -d "request[headers][0][name]"=Destination-API-Key \
  -d "request[headers][0][value]"={{DESTINATION_API_KEY}} \
  -d "request[headers][1][name]"=Destination-Idempotency-Key \
  -d "request[headers][1][value]"={{DESTINATION_IDEMPOTENCY_KEY}}
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

request = client.v1.forwarding.requests.create({
  url: 'https://endpoint-url/v1/payments',
  payment_method: 'pm_card_visa',
  replacements: ['card_number', 'card_expiry', 'card_cvc', 'cardholder_name'],
  request: {
    body: '{"amount":{"value":1000,"currency":"usd"},"paymentMethod":{"number":"","expiryMonth":"","expiryYear":"","cvc":"","holderName":""},"reference":"{{REFERENCE_ID}}"}',
    headers: [
      {
        name: 'Destination-API-Key',
        value: '{{DESTINATION_API_KEY}}',
      },
      {
        name: 'Destination-Idempotency-Key',
        value: '{{DESTINATION_IDEMPOTENCY_KEY}}',
      },
    ],
  },
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

request = client.v1.forwarding.requests.create({
  "url": "https://endpoint-url/v1/payments",
  "payment_method": "pm_card_visa",
  "replacements": ["card_number", "card_expiry", "card_cvc", "cardholder_name"],
  "request": {
    "body":
    "{\"amount\":{\"value\":1000,\"currency\":\"usd\"},\"paymentMethod\":{\"number\":\"\",\"expiryMonth\":\"\",\"expiryYear\":\"\",\"cvc\":\"\",\"holderName\":\"\"},\"reference\":\"{{REFERENCE_ID}}\"}",
    "headers": [
      {"name": "Destination-API-Key", "value": "{{DESTINATION_API_KEY}}"},
      {
        "name": "Destination-Idempotency-Key",
        "value": "{{DESTINATION_IDEMPOTENCY_KEY}}",
      },
    ],
  },
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$request = $stripe->forwarding->requests->create([
  'url' => 'https://endpoint-url/v1/payments',
  'payment_method' => 'pm_card_visa',
  'replacements' => ['card_number', 'card_expiry', 'card_cvc', 'cardholder_name'],
  'request' => [
    'body' => '{"amount":{"value":1000,"currency":"usd"},"paymentMethod":{"number":"","expiryMonth":"","expiryYear":"","cvc":"","holderName":""},"reference":"{{REFERENCE_ID}}"}',
    'headers' => [
      [
        'name' => 'Destination-API-Key',
        'value' => '{{DESTINATION_API_KEY}}',
      ],
      [
        'name' => 'Destination-Idempotency-Key',
        'value' => '{{DESTINATION_IDEMPOTENCY_KEY}}',
      ],
    ],
  ],
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

RequestCreateParams params =
  RequestCreateParams.builder()
    .setUrl("https://endpoint-url/v1/payments")
    .setPaymentMethod("pm_card_visa")
    .addReplacement(RequestCreateParams.Replacement.CARD_NUMBER)
    .addReplacement(RequestCreateParams.Replacement.CARD_EXPIRY)
    .addReplacement(RequestCreateParams.Replacement.CARD_CVC)
    .addReplacement(RequestCreateParams.Replacement.CARDHOLDER_NAME)
    .setRequest(
      RequestCreateParams.Request.builder()
        .setBody(
          "{\"amount\":{\"value\":1000,\"currency\":\"usd\"},\"paymentMethod\":{\"number\":\"\",\"expiryMonth\":\"\",\"expiryYear\":\"\",\"cvc\":\"\",\"holderName\":\"\"},\"reference\":\"{{REFERENCE_ID}}\"}"
        )
        .addHeader(
          RequestCreateParams.Request.Header.builder()
            .setName("Destination-API-Key")
            .setValue("{{DESTINATION_API_KEY}}")
            .build()
        )
        .addHeader(
          RequestCreateParams.Request.Header.builder()
            .setName("Destination-Idempotency-Key")
            .setValue("{{DESTINATION_IDEMPOTENCY_KEY}}")
            .build()
        )
        .build()
    )
    .build();

Request request = client.v1().forwarding().requests().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const request = await stripe.forwarding.requests.create({
  url: 'https://endpoint-url/v1/payments',
  payment_method: 'pm_card_visa',
  replacements: ['card_number', 'card_expiry', 'card_cvc', 'cardholder_name'],
  request: {
    body: '{"amount":{"value":1000,"currency":"usd"},"paymentMethod":{"number":"","expiryMonth":"","expiryYear":"","cvc":"","holderName":""},"reference":"{{REFERENCE_ID}}"}',
    headers: [
      {
        name: 'Destination-API-Key',
        value: '{{DESTINATION_API_KEY}}',
      },
      {
        name: 'Destination-Idempotency-Key',
        value: '{{DESTINATION_IDEMPOTENCY_KEY}}',
      },
    ],
  },
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.ForwardingRequestCreateParams{
  URL: stripe.String("https://endpoint-url/v1/payments"),
  PaymentMethod: stripe.String("pm_card_visa"),
  Replacements: []*string{
    stripe.String(stripe.ForwardingRequestReplacementCardNumber),
    stripe.String(stripe.ForwardingRequestReplacementCardExpiry),
    stripe.String(stripe.ForwardingRequestReplacementCardCVC),
    stripe.String(stripe.ForwardingRequestReplacementCardholderName),
  },
  Request: &stripe.ForwardingRequestCreateParams{
    Body: stripe.String("{\"amount\":{\"value\":1000,\"currency\":\"usd\"},\"paymentMethod\":{\"number\":\"\",\"expiryMonth\":\"\",\"expiryYear\":\"\",\"cvc\":\"\",\"holderName\":\"\"},\"reference\":\"{{REFERENCE_ID}}\"}"),
    Headers: []*stripe.ForwardingRequestCreateRequestHeaderParams{
      &stripe.ForwardingRequestCreateRequestHeaderParams{
        Name: stripe.String("Destination-API-Key"),
        Value: stripe.String("{{DESTINATION_API_KEY}}"),
      },
      &stripe.ForwardingRequestCreateRequestHeaderParams{
        Name: stripe.String("Destination-Idempotency-Key"),
        Value: stripe.String("{{DESTINATION_IDEMPOTENCY_KEY}}"),
      },
    },
  },
}
result, err := sc.V1ForwardingRequests.Create(context.TODO(), params)
```

```dotnet
var options = new Stripe.Forwarding.RequestCreateOptions
{
    Url = "https://endpoint-url/v1/payments",
    PaymentMethod = "pm_card_visa",
    Replacements = new List<string>
    {
        "card_number",
        "card_expiry",
        "card_cvc",
        "cardholder_name",
    },
    Request = new Stripe.Forwarding.RequestRequestOptions
    {
        Body = "{\"amount\":{\"value\":1000,\"currency\":\"usd\"},\"paymentMethod\":{\"number\":\"\",\"expiryMonth\":\"\",\"expiryYear\":\"\",\"cvc\":\"\",\"holderName\":\"\"},\"reference\":\"{{REFERENCE_ID}}\"}",
        Headers = new List<Stripe.Forwarding.RequestRequestHeaderOptions>
        {
            new Stripe.Forwarding.RequestRequestHeaderOptions
            {
                Name = "Destination-API-Key",
                Value = "{{DESTINATION_API_KEY}}",
            },
            new Stripe.Forwarding.RequestRequestHeaderOptions
            {
                Name = "Destination-Idempotency-Key",
                Value = "{{DESTINATION_IDEMPOTENCY_KEY}}",
            },
        },
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Forwarding.Requests;
Stripe.Forwarding.Request request = service.Create(options);
```

### Response

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