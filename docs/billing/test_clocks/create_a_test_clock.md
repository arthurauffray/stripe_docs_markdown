# Create a test clock

Creates a new test clock that can be attached to new customers and quotes.

## Returns

The newly created `TestClock` object is returned upon success. Otherwise, this call raises [an error](https://docs.stripe.com/api/test_clocks/create.md#errors).

## Parameters

- `frozen_time` (timestamp, required)
  The initial frozen time for this test clock.

- `name` (string, optional)
  The name for this test clock.

  The maximum length is 300 characters.

```curl
curl https://api.stripe.com/v1/test_helpers/test_clocks \
  -u "<<YOUR_SECRET_KEY>>" \
  -d frozen_time=1577836800
```

```cli
stripe test_helpers test_clocks create  \
  --frozen-time=1577836800
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

test_clock = client.v1.test_helpers.test_clocks.create({frozen_time: 1577836800})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

test_clock = client.v1.test_helpers.test_clocks.create({"frozen_time": 1577836800})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$testClock = $stripe->testHelpers->testClocks->create(['frozen_time' => 1577836800]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

TestClockCreateParams params =
  TestClockCreateParams.builder().setFrozenTime(1577836800L).build();

TestClock testClock = client.v1().testHelpers().testClocks().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const testClock = await stripe.testHelpers.testClocks.create({
  frozen_time: 1577836800,
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.TestHelpersTestClockCreateParams{
  FrozenTime: stripe.Int64(1577836800),
}
result, err := sc.V1TestHelpersTestClocks.Create(context.TODO(), params)
```

```dotnet
var options = new Stripe.TestHelpers.TestClockCreateOptions
{
    FrozenTime = DateTimeOffset.FromUnixTimeSeconds(1577836800).UtcDateTime,
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.TestHelpers.TestClocks;
Stripe.TestHelpers.TestClock testClock = service.Create(options);
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