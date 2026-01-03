# Retrieve a Report Type

Retrieves the details of a Report Type. (Certain report types require a [live-mode API key](https://stripe.com/docs/keys#test-live-modes).)

## Returns

Returns the specified `ReportType` object if found, and raises [an error](https://docs.stripe.com/api/reporting/report_type/retrieve.md#errors) otherwise.

```curl
curl https://api.stripe.com/v1/reporting/report_types/balance.summary.1 \
  -u "<<YOUR_SECRET_KEY>>"
```

```cli
stripe reporting report_types retrieve balance.summary.1
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

report_type = client.v1.reporting.report_types.retrieve('balance.summary.1')
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

report_type = client.v1.reporting.report_types.retrieve("balance.summary.1")
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$reportType = $stripe->reporting->reportTypes->retrieve('balance.summary.1', []);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ReportTypeRetrieveParams params = ReportTypeRetrieveParams.builder().build();

ReportType reportType =
  client.v1().reporting().reportTypes().retrieve("balance.summary.1", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const reportType = await stripe.reporting.reportTypes.retrieve('balance.summary.1');
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.ReportingReportTypeRetrieveParams{}
result, err := sc.V1ReportingReportTypes.Retrieve(
  context.TODO(), "balance.summary.1", params)
```

```dotnet
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Reporting.ReportTypes;
Stripe.Reporting.ReportType reportType = service.Get("balance.summary.1");
```

### Response

```json
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
```