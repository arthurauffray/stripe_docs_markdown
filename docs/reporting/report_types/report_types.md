# Report Types

The Report Type resource corresponds to a particular type of report, such as the “Activity summary” or “Itemized payouts” reports. These objects are identified by an ID belonging to a set of enumerated values. See [API Access to Reports documentation](https://docs.stripe.com/docs/reporting/statements/api.md) for those Report Type IDs, along with required and optional parameters.

Note that certain report types can only be run based on your live-mode data (not test-mode data), and will error when queried without a [live-mode API key](https://docs.stripe.com/docs/keys.md#test-live-modes).

## Endpoints

### Retrieve a Report Type

- [GET /v1/reporting/report_types/:id](https://docs.stripe.com/api/reporting/report_type/retrieve.md)

### List all Report Types

- [GET /v1/reporting/report_types](https://docs.stripe.com/api/reporting/report_type/list.md)