# Pagination

All top-level API resources have support for bulk fetches through “list” API methods. For example, you can [list charges](https://docs.stripe.com/api/charges/list.md), [list customers](https://docs.stripe.com/api/customers/list.md), and [list invoices](https://docs.stripe.com/api/invoices/list.md). These list API methods share a common structure and accept, at a minimum, the following three parameters: `limit`, `starting_after`, and `ending_before`.

Stripe’s list API methods use cursor-based [pagination](https://docs.stripe.com/pagination.md) through the `starting_after` and `ending_before` parameters. Both parameters accept an existing object ID value (see below) and return objects in reverse chronological order. The `ending_before` parameter returns objects listed before the named object. The `starting_after` parameter returns objects listed after the named object. These parameters are mutually exclusive. You can use either the `starting_after` or `ending_before` parameter, but not both simultaneously.

Our client libraries offer [auto-pagination helpers](https://docs.stripe.com/pagination.md#auto-pagination) to traverse all pages of a list.

## Parameters

- `limit` (optional, default is 10)
  This specifies a limit on the number of objects to return, ranging between 1 and 100.

- `starting_after` (optional object ID)
  A cursor to use in pagination. `starting_after` is an object ID that defines your place in the list. For example, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` to fetch the next page of the list.

- `ending_before` (optional object ID)
  A cursor to use in pagination. `ending_before` is an object ID that defines your place in the list. For example, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` to fetch the previous page of the list.

## List Response Format

- `object` (string, value is "list")
  A string that provides a description of the object type that returns.

- `data` (array)
  An array containing the actual response elements, paginated by any request parameters.

- `has_more` (boolean)
  Whether or not there are more elements available after this set. If `false`, this set comprises the end of the list.

- `url` (url)
  The URL for accessing this list.

## v2 API pagination

APIs within the `/v2` namespace contain a different [pagination](https://docs.stripe.com/api-v2-overview.md#list-pagination) interface than the `v1` namespace.

### Response

```json
{
  "object": "list",
  "url": "/v1/customers",
  "has_more": false,
  "data": [
    {
      "id": "cus_4QFJOjw2pOmAGJ",
      "object": "customer",
      "address": null,
      "balance": 0,
      "created": 1405641735,
      "currency": "usd",
      "default_source": "card_14HOpG2eZvKYlo2Cz4u5AJG5",
      "delinquent": false,
      "description": "New customer",
      "discount": null,
      "email": null,
      "invoice_prefix": "7D11B54",
      "invoice_settings": {
        "custom_fields": null,
        "default_payment_method": null,
        "footer": null,
        "rendering_options": null
      },
      "livemode": false,
      "metadata": {
        "order_id": "6735"
      },
      "name": "cus_4QFJOjw2pOmAGJ",
      "next_invoice_sequence": 25,
      "phone": null,
      "preferred_locales": [],
      "shipping": null,
      "tax_exempt": "none",
      "test_clock": null
    },
  ]
}
```