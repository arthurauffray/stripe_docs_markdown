# Terminal Hardware Order

A TerminalHardwareOrder represents an order for Terminal hardware, containing information such as the price, shipping information and the items ordered.

## Endpoints

### Create a Terminal Hardware Order

- [POST /v1/terminal/hardware_orders](https://docs.stripe.com/api/terminal/hardware_orders/create.md)

### Retrieve a Terminal Hardware Order

- [GET /v1/terminal/hardware_orders/:id](https://docs.stripe.com/api/terminal/hardware_orders/retrieve.md)

### List all Terminal Hardware Orders

- [GET /v1/terminal/hardware_orders](https://docs.stripe.com/api/terminal/hardware_orders/list.md)

### Cancel a Terminal Hardware Order

- [POST /v1/terminal/hardware_orders/:id/cancel](https://docs.stripe.com/api/terminal/hardware_orders/cancel.md)

### Preview a Terminal Hardware Order

- [GET /v1/terminal/hardware_orders/preview](https://docs.stripe.com/api/terminal/hardware_orders/preview.md)

### Test mode: Mark a Terminal Hardware Order as Ready To Ship

- [POST /v1/test_helpers/terminal/hardware_orders/:id/mark_ready_to_ship](https://docs.stripe.com/api/terminal/hardware_orders/test_mode_mark_ready_to_ship.md)

### Test mode: Mark a Terminal Hardware Order as Delivered

- [POST /v1/test_helpers/terminal/hardware_orders/:id/deliver](https://docs.stripe.com/api/terminal/hardware_orders/test_mode_deliver.md)

### Test mode: Mark a Terminal Hardware Order as Shipped

- [POST /v1/test_helpers/terminal/hardware_orders/:id/ship](https://docs.stripe.com/api/terminal/hardware_orders/test_mode_ship.md)

### Test mode: Mark a Terminal Hardware Order as Undeliverable

- [POST /v1/test_helpers/terminal/hardware_orders/:id/mark_undeliverable](https://docs.stripe.com/api/terminal/hardware_orders/test_mode_mark_undeliverable.md)