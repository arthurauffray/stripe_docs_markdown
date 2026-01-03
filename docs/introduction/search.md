# Search

Some top-level API resource have support for retrieval via “search” API methods. For example, you can [search charges](https://docs.stripe.com/api/charges/search.md), [search customers](https://docs.stripe.com/api/customers/search.md), and [search subscriptions](https://docs.stripe.com/api/subscriptions/search.md).

Stripe’s search API methods utilize cursor-based pagination via the `page` request parameter and `next_page` response parameter. For example, if you make a search request and receive `"next_page": "pagination_key"` in the response, your subsequent call can include `page=pagination_key` to fetch the next page of results.

Our client libraries offer [auto-pagination](https://docs.stripe.com/api/pagination/auto.md) helpers to easily traverse all pages of a search result.

## Search request format

- `query` (required)
  The search query string. See [search query language](https://docs.stripe.com/search.md#search-query-language).

- `limit` (optional)
  A limit on the number of objects returned. Limit can range between 1 and 100, and the default is 10.

- `page` (optional)
  A cursor for pagination across multiple pages of results. Don’t include this parameter on the first call. Use the `next_page` value returned in a previous response to request subsequent results.

## Search response format

- `object` (string, value is "search_result")
  A string describing the object type returned.

- `url` (string)
  The URL for accessing this list.

- `has_more` (boolean)
  Whether or not there are more elements available after this set. If `false`, this set comprises the end of the list.

- `data` (array)
  An array containing the actual response elements, paginated by any request parameters.

- `next_page` (string)
  A cursor for use in pagination. If `has_more` is true, you can pass the value of `next_page` to a subsequent call to fetch the next page of results.

- `total_count` (optional positive integer or zero)
  The total number of objects that match the query, only accurate up to 10,000. This field isn’t included by default. To include it in the response, [expand](https://docs.stripe.com/api/expanding_objects.md) the `total_count` field.

### Response

```json
{
  "object": "search_result",
  "url": "/v1/customers/search",
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
      "description": "someone@example.com for Coderwall",
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
        "foo": "bar"
      },
      "name": "fakename",
      "next_invoice_sequence": 25,
      "phone": null,
      "preferred_locales": [],
      "shipping": null,
      "tax_exempt": "none",
      "test_clock": null
    }
  ]
}
```