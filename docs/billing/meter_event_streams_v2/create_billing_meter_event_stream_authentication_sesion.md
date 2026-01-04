# Create billing meter event stream authentication session

Creates a meter event session to send usage on the high-throughput meter event stream. Authentication tokens are only valid for 15 minutes, so you will need to create a new meter event session when your token expires.

## Returns

## Response attributes

- `id` (string)
  The unique id of this auth session.

- `object` (string, value is "v2.billing.meter_event_session")
  String representing the object’s type. Objects of the same type share the same value of the object field.

- `authentication_token` (string)
  The authentication token for this session.  Use this token when calling the high-throughput meter event API.

- `created` (timestamp)
  The creation time of this session.

- `expires_at` (timestamp)
  The time at which this session will expire.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

```curl
curl -X POST https://api.stripe.com/v2/billing/meter_event_session \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: {{STRIPE_API_VERSION}}"
```

```cli
stripe v2 billing meter_event_sessions create
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

meter_event_session = client.v2.billing.meter_event_session.create()
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

meter_event_session = client.v2.billing.meter_event_session.create()
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$meterEventSession = $stripe->v2->billing->meterEventSession->create([]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

MeterEventSession meterEventSession =
  client.v2().billing().meterEventSession().create();
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const meterEventSession = await stripe.v2.billing.meterEventSession.create();
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.V2BillingMeterEventSessionCreateParams{}
result, err := sc.V2BillingMeterEventSessions.Create(context.TODO(), params)
```

```dotnet
var options = new Stripe.V2.Billing.MeterEventSessionCreateOptions();
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V2.Billing.MeterEventSession;
Stripe.V2.Billing.MeterEventSession meterEventSession = service.Create(options);
```

### Response

```json
{
  "id": "<AUTH_SESSION_ID>",
  "livemode": "false",
  "object": "v2.billing.meter_event_session",
  "authentication_token": "token_12345678",
  "created": "2024-06-01T12:00:00.000Z",
  "expires_at": "2024-06-01T12:15:00.000Z"
}
```