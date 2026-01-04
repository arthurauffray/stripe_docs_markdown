# List billing meter event summaries

Retrieve a list of billing meter event summaries.

## Returns

Returns a list of billing meter event summaries.

## Parameters

- `customer` (string, required)
  The customer for which to fetch event summaries.

- `end_time` (timestamp, required)
  The timestamp from when to stop aggregating meter events (exclusive). Must be aligned with minute boundaries.

- `id` (string, required)
  Unique identifier for the object.

- `start_time` (timestamp, required)
  The timestamp from when to start aggregating meter events (inclusive). Must be aligned with minute boundaries.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `value_grouping_window` (enum, optional)
  Specifies what granularity to use when generating event summaries. If not specified, a single event summary would be returned for the specified time range. For hourly granularity, start and end times must align with hour boundaries (e.g., 00:00, 01:00, …, 23:00). For daily granularity, start and end times must align with UTC day boundaries (00:00 UTC).
Possible enum values:
  - `day`
    Generate event summaries per day.

  - `hour`
    Generate event summaries per hour.

```curl
curl -G https://api.stripe.com/v1/billing/meters/mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA/event_summaries \
  -u "<<YOUR_SECRET_KEY>>" \
  -d customer=cus_Pp40waj64hdRxb \
  -d start_time=1711584000 \
  -d end_time=1711666800 \
  -d value_grouping_window=hour
```

```cli
stripe billing meter_event_summaries list mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA \
  --customer=cus_Pp40waj64hdRxb \
  --start-time=1711584000 \
  --end-time=1711666800 \
  --value-grouping-window=hour
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

meter_event_summaries = client.v1.billing.meters.event_summaries.list(
  'mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA',
  {
    customer: 'cus_Pp40waj64hdRxb',
    start_time: 1711584000,
    end_time: 1711666800,
    value_grouping_window: 'hour',
  },
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

meter_event_summaries = client.v1.billing.meters.event_summaries.list(
  "mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA",
  {
    "customer": "cus_Pp40waj64hdRxb",
    "start_time": 1711584000,
    "end_time": 1711666800,
    "value_grouping_window": "hour",
  },
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$meterEventSummaries = $stripe->billing->meters->allEventSummaries(
  'mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA',
  [
    'customer' => 'cus_Pp40waj64hdRxb',
    'start_time' => 1711584000,
    'end_time' => 1711666800,
    'value_grouping_window' => 'hour',
  ]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

MeterEventSummaryListParams params =
  MeterEventSummaryListParams.builder()
    .setCustomer("cus_Pp40waj64hdRxb")
    .setStartTime(1711584000L)
    .setEndTime(1711666800L)
    .setValueGroupingWindow(MeterEventSummaryListParams.ValueGroupingWindow.HOUR)
    .build();

StripeCollection<MeterEventSummary> stripeCollection =
  client.v1().billing().meters().eventSummaries().list(
    "mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const meterEventSummaries = await stripe.billing.meters.listEventSummaries(
  'mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA',
  {
    customer: 'cus_Pp40waj64hdRxb',
    start_time: 1711584000,
    end_time: 1711666800,
    value_grouping_window: 'hour',
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.BillingMeterEventSummaryListParams{
  Customer: stripe.String("cus_Pp40waj64hdRxb"),
  StartTime: stripe.Int64(1711584000),
  EndTime: stripe.Int64(1711666800),
  ValueGroupingWindow: stripe.String("hour"),
  ID: stripe.String("mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA"),
}
result := sc.V1BillingMeterEventSummaries.List(context.TODO(), params)
```

```dotnet
var options = new Stripe.Billing.MeterEventSummaryListOptions
{
    Customer = "cus_Pp40waj64hdRxb",
    StartTime = DateTimeOffset.FromUnixTimeSeconds(1711584000).UtcDateTime,
    EndTime = DateTimeOffset.FromUnixTimeSeconds(1711666800).UtcDateTime,
    ValueGroupingWindow = "hour",
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Billing.Meters.EventSummaries;
StripeList<Stripe.Billing.MeterEventSummary> meterEventSummaries = service.List(
    "mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA",
    options);
```

### Response

```json
{
  "object": "list",
  "data": [
    {
      "id": "mtrusg_test_6041CMAXJrFdZ56U76ce6L35Hz7xA3Tn58z5sY7bq6gM3XN5bx5Y459D4Xt2E17ko6M86kt7kV3bl5PM7LV59l4sY50b6oU5QD7bY3HP58z5sY7bq6gM3Y57LF2Dr7od3Hb8927gh4Tt4Lo4xO4ge60T81C6Y53gl4QS2D33ft3HC3Xl3bk3Cy3Cy",
      "object": "billing.meter_event_summary",
      "aggregated_value": 15,
      "end_time": 1711663200,
      "livemode": false,
      "meter": "mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA",
      "start_time": 1711659600
    },
    {
      "id": "mtrusg_test_6041CMAXJrFdZ56U76ce6L35Hz7xA3Tn58z5sY7bq6gM3XN5bx5Y459D4Xt2E17ko6M86kt7kV3bl5PM7LV59l4sY50b6oU5QD7bY3HP58z5sY7bq6gM3Y57LF2Dr7od3Hb8927gh4Tt4Lo4xO4ge60T81C6Y53gl4QS2D33ft3HC3Xi3Cy3Cy3Cy",
      "object": "billing.meter_event_summary",
      "aggregated_value": 10,
      "end_time": 1711659600,
      "livemode": false,
      "meter": "mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA",
      "start_time": 1711656000
    }
  ],
  "has_more": false,
  "url": "/v1/billing/meters/:id/event_summaries"
}
```