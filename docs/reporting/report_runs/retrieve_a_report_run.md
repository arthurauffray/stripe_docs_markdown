# Retrieve a Report Run

Retrieves the details of an existing Report Run.

## Returns

Returns the specified `ReportRun` object if found, and raises [an error](https://docs.stripe.com/api/reporting/report_run/retrieve.md#errors) otherwise.

```curl
curl https://api.stripe.com/v1/reporting/report_runs/frr_1MrQwrLkdIwHu7ixUov4x2b3 \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe reporting report_runs retrieve frr_1MrQwrLkdIwHu7ixUov4x2b3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

report_run = client.v1.reporting.report_runs.retrieve('frr_1MrQwrLkdIwHu7ixUov4x2b3')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

report_run = client.v1.reporting.report_runs.retrieve("frr_1MrQwrLkdIwHu7ixUov4x2b3")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$reportRun = $stripe->reporting->reportRuns->retrieve(
  'frr_1MrQwrLkdIwHu7ixUov4x2b3',
  []
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ReportRunRetrieveParams params = ReportRunRetrieveParams.builder().build();

ReportRun reportRun =
  client.v1().reporting().reportRuns().retrieve(
    "frr_1MrQwrLkdIwHu7ixUov4x2b3",
    params
  );
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const reportRun = await stripe.reporting.reportRuns.retrieve(
  'frr_1MrQwrLkdIwHu7ixUov4x2b3'
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.ReportingReportRunRetrieveParams{}
result, err := sc.V1ReportingReportRuns.Retrieve(
  context.TODO(), "frr_1MrQwrLkdIwHu7ixUov4x2b3", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Reporting.ReportRuns;
Stripe.Reporting.ReportRun reportRun = service.Get("frr_1MrQwrLkdIwHu7ixUov4x2b3");
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