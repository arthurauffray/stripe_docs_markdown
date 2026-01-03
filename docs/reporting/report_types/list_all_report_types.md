# List all Report Types

Returns a full list of Report Types.

## Returns

A dictionary with a `data` property that contains an array of Report Types. Each entry is a separate `ReportType` object.

```curl
curl https://api.stripe.com/v1/reporting/report_types \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe reporting report_types list
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

report_types = client.v1.reporting.report_types.list()
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

report_types = client.v1.reporting.report_types.list()
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$reportTypes = $stripe->reporting->reportTypes->all([]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ReportTypeListParams params = ReportTypeListParams.builder().build();

StripeCollection<ReportType> stripeCollection =
  client.v1().reporting().reportTypes().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const reportTypes = await stripe.reporting.reportTypes.list();
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.ReportingReportTypeListParams{}
result := sc.V1ReportingReportTypes.List(context.TODO(), params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Reporting.ReportTypes;
StripeList<Stripe.Reporting.ReportType> reportTypes = service.List();
```

### Response

```json
{
  "object": "list",
  "url": "/v1/reporting/report_types",
  "has_more": false,
  "data": [
    {
      "id": "balance.summary.1",
      "object": "reporting.report_type",
      "data_available_end": 1695081600,
      "data_available_start": 1667952000,
      "default_columns": [
        "category",
        "description",
        "net_amount",
        "currency"
      ],
      "livemode": false,
      "name": "Balance summary",
      "updated": 1695109133,
      "version": 1
    }
  ]
}
```