# Create a Report Run

Creates a new object and begin running the report. (Certain report types require a [live-mode API key](https://stripe.com/docs/keys#test-live-modes).)

## Returns

Returns the new `ReportRun` object.

## Parameters

- `report_type` (string, required)
  The ID of the [report type](https://docs.stripe.com/docs/reporting/statements/api.md#report-types) to run, such as `"balance.summary.1"`.

- `parameters` (object, optional)
  Parameters specifying how the report should be run. Different Report Types have different required and optional parameters, listed in the [API Access to Reports](https://docs.stripe.com/docs/reporting/statements/api.md) documentation.

  - `parameters.columns` (array of strings, optional)
    The set of report columns to include in the report output. If omitted, the Report Type is run with its default column set.

  - `parameters.connected_account` (string, optional)
    Connected account ID to filter for in the report run.

  - `parameters.currency` (enum, optional)
    Currency of objects to be included in the report run.

  - `parameters.interval_end` (timestamp, optional)
    Ending timestamp of data to be included in the report run (exclusive).

  - `parameters.interval_start` (timestamp, optional)
    Starting timestamp of data to be included in the report run.

  - `parameters.payout` (string, optional)
    Payout ID by which to filter the report run.

  - `parameters.reporting_category` (string, optional)
    Category of balance transactions to be included in the report run.

  - `parameters.timezone` (string, optional)
    Defaults to `Etc/UTC`. The output timezone for all timestamps in the report. A list of possible time zone values is maintained at the [IANA Time Zone Database](http://www.iana.org/time-zones). Has no effect on `interval_start` or `interval_end`.

```curl
curl https://api.stripe.com/v1/reporting/report_runs \
  -u "<<YOUR_SECRET_KEY>>" \
  -d report_type="balance.summary.1" \
  -d "parameters[interval_start]"=1680000000 \
  -d "parameters[interval_end]"=1680100000
```

```cli
stripe reporting report_runs create  \
  --report-type="balance.summary.1" \
  -d "parameters[interval_start]"=1680000000 \
  -d "parameters[interval_end]"=1680100000
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

report_run = client.v1.reporting.report_runs.create({
  report_type: 'balance.summary.1',
  parameters: {
    interval_start: 1680000000,
    interval_end: 1680100000,
  },
})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

report_run = client.v1.reporting.report_runs.create({
  "report_type": "balance.summary.1",
  "parameters": {"interval_start": 1680000000, "interval_end": 1680100000},
})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$reportRun = $stripe->reporting->reportRuns->create([
  'report_type' => 'balance.summary.1',
  'parameters' => [
    'interval_start' => 1680000000,
    'interval_end' => 1680100000,
  ],
]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ReportRunCreateParams params =
  ReportRunCreateParams.builder()
    .setReportType("balance.summary.1")
    .setParameters(
      ReportRunCreateParams.Parameters.builder()
        .setIntervalStart(1680000000L)
        .setIntervalEnd(1680100000L)
        .build()
    )
    .build();

ReportRun reportRun = client.v1().reporting().reportRuns().create(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const reportRun = await stripe.reporting.reportRuns.create({
  report_type: 'balance.summary.1',
  parameters: {
    interval_start: 1680000000,
    interval_end: 1680100000,
  },
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.ReportingReportRunCreateParams{
  ReportType: stripe.String("balance.summary.1"),
  Parameters: &stripe.ReportingReportRunCreateParametersParams{
    IntervalStart: stripe.Int64(1680000000),
    IntervalEnd: stripe.Int64(1680100000),
  },
}
result, err := sc.V1ReportingReportRuns.Create(context.TODO(), params)
```

```dotnet
var options = new Stripe.Reporting.ReportRunCreateOptions
{
    ReportType = "balance.summary.1",
    Parameters = new Stripe.Reporting.ReportRunParametersOptions
    {
        IntervalStart = DateTimeOffset.FromUnixTimeSeconds(1680000000).UtcDateTime,
        IntervalEnd = DateTimeOffset.FromUnixTimeSeconds(1680100000).UtcDateTime,
    },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Reporting.ReportRuns;
Stripe.Reporting.ReportRun reportRun = service.Create(options);
```

### Response

```json
{
  "id": "frr_1MrQwrLkdIwHu7ixUov4x2b3",
  "object": "reporting.report_run",
  "created": 1680203749,
  "error": null,
  "livemode": false,
  "parameters": {
    "interval_end": 1680100000,
    "interval_start": 1680000000
  },
  "report_type": "balance.summary.1",
  "result": null,
  "status": "pending",
  "succeeded_at": null
}
```