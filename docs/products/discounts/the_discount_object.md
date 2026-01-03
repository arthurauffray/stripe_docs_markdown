# The Discount object

## Attributes

- `id` (string)
  The ID of the discount object. Discounts cannot be fetched by ID. Use `expand[]=discounts` in API calls to expand discount IDs in an array.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `checkout_session` (string, nullable)
  The Checkout session that this coupon is applied to, if it is applied to a particular session in payment mode. Will not be present for subscription mode.

- `customer` (string, nullable)
  The ID of the customer associated with this discount.

- `customer_account` (string, nullable)
  The ID of the account representing the customer associated with this discount.

- `end` (timestamp, nullable)
  If the coupon has a duration of `repeating`, the date that this discount will end. If the coupon has a duration of `once` or `forever`, this attribute will be null.

- `invoice` (string, nullable)
  The invoice that the discount’s coupon was applied to, if it was applied directly to a particular invoice.

- `invoice_item` (string, nullable)
  The invoice item `id` (or invoice line item `id` for invoice line items of type=‘subscription’) that the discount’s coupon was applied to, if it was applied directly to a particular invoice item or invoice line item.

- `promotion_code` (string, nullable)
  The promotion code applied to create this discount.

- `source` (object)
  The source of the discount.

  - `source.coupon` (string, nullable)
    The coupon that was redeemed to create this discount.

  - `source.type` (enum)
    The source type of the discount.
Possible enum values:
    - `coupon`
      Coupon source type

- `start` (timestamp)
  Date that the coupon was applied.

- `subscription` (string, nullable)
  The subscription that this coupon is applied to, if it is applied to a particular subscription.

- `subscription_item` (string, nullable)
  The subscription item that this coupon is applied to, if it is applied to a particular subscription item.

### The Discount object

```json
{
  "id": "di_1M6vk22eZvKYlo2CYMGIhk14",
  "object": "discount",
  "checkout_session": "cs_test_b1mywbZHtQCQW2ncaItVPFqupwmfqNU4IMMdw3lArEBGt0QD0CZDrNQswR",
  "source": {
    "type": "coupon",
    "coupon": "nVJYDOag"
  },
  "customer": "cus_9s6XKzkNRiz8i3",
  "end": null,
  "invoice": null,
  "invoice_item": null,
  "promotion_code": null,
  "start": 1669120702,
  "subscription": null
}
```