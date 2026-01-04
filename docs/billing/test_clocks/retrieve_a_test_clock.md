# Retrieve a test clock

Retrieves a test clock.

## Returns

Returns the `TestClock` object. Otherwise, this call raises [an error](https://docs.stripe.com/api/test_clocks/retrieve.md#errors).

```curl
curl https://api.stripe.com/v1/test_helpers/test_clocks/clock_1Mr3I22eZvKYlo2Ck0rgMqd7 \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe test_helpers test_clocks retrieve clock_1Mr3I22eZvKYlo2Ck0rgMqd7
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

test_clock = client.v1.test_helpers.test_clocks.retrieve('clock_1Mr3I22eZvKYlo2Ck0rgMqd7')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

test_clock = client.v1.test_helpers.test_clocks.retrieve(
  "clock_1Mr3I22eZvKYlo2Ck0rgMqd7",
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$testClock = $stripe->testHelpers->testClocks->retrieve(
  'clock_1Mr3I22eZvKYlo2Ck0rgMqd7',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TestClockRetrieveParams params = TestClockRetrieveParams.builder().build();

TestClock testClock =
  client.v1().testHelpers().testClocks().retrieve(
    "clock_1Mr3I22eZvKYlo2Ck0rgMqd7",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const testClock = await stripe.testHelpers.testClocks.retrieve(
  'clock_1Mr3I22eZvKYlo2Ck0rgMqd7'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TestHelpersTestClockRetrieveParams{}
result, err := sc.V1TestHelpersTestClocks.Retrieve(
  context.TODO(), "clock_1Mr3I22eZvKYlo2Ck0rgMqd7", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.TestHelpers.TestClocks;
Stripe.TestHelpers.TestClock testClock = service.Get(
    "clock_1Mr3I22eZvKYlo2Ck0rgMqd7");
```

### Response

```json
{
  "id": "clock_1Mr3I22eZvKYlo2Ck0rgMqd7",
  "object": "test_helpers.test_clock",
  "created": 1680112806,
  "deletes_after": 1680717606,
  "frozen_time": 1577836800,
  "livemode": false,
  "name": null,
  "status": "ready"
}
```