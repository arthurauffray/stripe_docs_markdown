# Meter Event Summary

A billing meter event summary represents an aggregated view of a customer’s billing meter events within a specified timeframe. It indicates how much usage was accrued by a customer for that period.

Note: Meters events are aggregated asynchronously so the meter event summaries provide an eventually consistent view of the reported usage.

## Endpoints

### List billing meter event summaries

- [GET /v1/billing/meters/:id/event_summaries](https://docs.stripe.com/api/billing/meter-event-summary/list.md)