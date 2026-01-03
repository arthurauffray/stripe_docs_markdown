# Retrieve a ForwardingRequest

Retrieves a ForwardingRequest object.

## Returns

Returns a ForwardingRequest object.

```curl
curl https://api.stripe.com/v1/forwarding/requests/fwdreq_123 \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe forwarding requests retrieve fwdreq_123
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

request = client.v1.forwarding.requests.retrieve('fwdreq_123')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

request = client.v1.forwarding.requests.retrieve("fwdreq_123")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$request = $stripe->forwarding->requests->retrieve('fwdreq_123', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

RequestRetrieveParams params = RequestRetrieveParams.builder().build();

Request request = client.v1().forwarding().requests().retrieve("fwdreq_123", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const request = await stripe.forwarding.requests.retrieve('fwdreq_123');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.ForwardingRequestRetrieveParams{}
result, err := sc.V1ForwardingRequests.Retrieve(context.TODO(), "fwdreq_123", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Forwarding.Requests;
Stripe.Forwarding.Request request = service.Get("fwdreq_123");
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