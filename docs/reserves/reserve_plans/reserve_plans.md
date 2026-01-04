# Reserve Plans

ReservePlans are used to automatically place holds on a merchant’s funds until the plan expires.       It takes a portion of each incoming Charge (including those resulting from a Transfer from a platform account).

## Endpoints

### Create a ReservePlan

- [POST /v1/reserve/plans](https://docs.stripe.com/api/reserve/plan/create.md)

### Update a ReservePlan

- [POST /v1/reserve/plans/:id](https://docs.stripe.com/api/reserve/plan/update.md)

### Retrieve a ReservePlan

- [GET /v1/reserve/plans/:id](https://docs.stripe.com/api/reserve/plan/retrieve.md)

### List ReservePlans

- [GET /v1/reserve/plans](https://docs.stripe.com/api/reserve/plan/list.md)

### Disable a ReservePlan

- [POST /v1/reserve/plans/:id/disable](https://docs.stripe.com/api/reserve/plan/disable.md)