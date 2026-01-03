# Report Runs

The Report Run object represents an instance of a report type generated with specific run parameters. Once the object is created, Stripe begins processing the report. When the report has finished running, it will give you a reference to a file where you can retrieve your results. For an overview, see [API Access to Reports](https://docs.stripe.com/docs/reporting/statements/api.md).

Note that certain report types can only be run based on your live-mode data (not test-mode data), and will error when queried without a [live-mode API key](https://docs.stripe.com/docs/keys.md#test-live-modes).

## Endpoints

### Create a Report Run

- [POST /v1/reporting/report_runs](https://docs.stripe.com/api/reporting/report_run/create.md)

### Retrieve a Report Run

- [GET /v1/reporting/report_runs/:id](https://docs.stripe.com/api/reporting/report_run/retrieve.md)

### List all Report Runs

- [GET /v1/reporting/report_runs](https://docs.stripe.com/api/reporting/report_run/list.md)