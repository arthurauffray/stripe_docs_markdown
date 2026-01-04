# Update a source

Updates the specified source by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

This request accepts the `metadata` and `owner` as arguments. It is also possible to update type specific information for selected payment methods. Please refer to our [payment method guides](https://docs.stripe.com/docs/sources.md) for more detail.

## Returns

Returns the source object if the update succeeded. This call will raise [an error](https://docs.stripe.com/api/sources/update.md#errors) if update parameters are invalid.

## Parameters

- `amount` (integer, optional)
  Amount associated with the source.

- `mandate` (object, optional)
  Information about a mandate possibility attached to a source object (generally for bank debits) as well as its acceptance status.

  - `mandate.acceptance` (object, optional)
    The parameters required to notify Stripe of a mandate acceptance or refusal by the customer.

    - `mandate.acceptance.status` (string, required)
      The status of the mandate acceptance. Either `accepted` (the mandate was accepted) or `refused` (the mandate was refused).

    - `mandate.acceptance.date` (timestamp, required)
      The Unix timestamp (in seconds) when the mandate was accepted or refused by the customer.

    - `mandate.acceptance.ip` (string, optional)
      The IP address from which the mandate was accepted or refused by the customer.

    - `mandate.acceptance.offline` (object, optional)
      The parameters required to store a mandate accepted offline. Should only be set if `mandate[type]` is `offline`

      - `mandate.acceptance.offline.contact_email` (string, required)
        An email to contact you with if a copy of the mandate is requested, required if `type` is `offline`.

        The maximum length is 800 characters.

    - `mandate.acceptance.online` (object, optional)
      The parameters required to store a mandate accepted online. Should only be set if `mandate[type]` is `online`

      - `mandate.acceptance.online.date` (timestamp, required)
        The Unix timestamp (in seconds) when the mandate was accepted or refused by the customer.

      - `mandate.acceptance.online.ip` (string, required)
        The IP address from which the mandate was accepted or refused by the customer.

      - `mandate.acceptance.online.user_agent` (string, required)
        The user agent of the browser from which the mandate was accepted or refused by the customer.

    - `mandate.acceptance.type` (string, optional)
      The type of acceptance information included with the mandate. Either `online`  or `offline`

    - `mandate.acceptance.user_agent` (string, optional)
      The user agent of the browser from which the mandate was accepted or refused by the customer.

  - `mandate.amount` (integer, optional)
    The amount specified by the mandate. (Leave null for a mandate covering all amounts)

  - `mandate.currency` (enum, optional)
    The currency specified by the mandate. (Must match `currency` of the source)

  - `mandate.interval` (string, optional)
    The interval of debits permitted by the mandate. Either `one_time` (just permitting a single debit), `scheduled` (with debits on an agreed schedule or for clearly-defined events), or `variable`(for debits with any frequency)

  - `mandate.notification_method` (string, optional)
    The method Stripe should use to notify the customer of upcoming debit instructions and/or mandate confirmation as required by the underlying debit network. Either `email` (an email is sent directly to the customer), `manual` (a `source.mandate_notification` event is sent to your webhooks endpoint and you should handle the notification) or `none` (the underlying debit network does not require any notification).

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `owner` (object, optional)
  Information about the owner of the payment instrument that may be used or required by particular source types.

  - `owner.address` (object, optional)
    Owner’s address.

    - `owner.address.city` (string, optional)
      City, district, suburb, town, or village.

    - `owner.address.country` (string, optional)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `owner.address.line1` (string, optional)
      Address line 1, such as the street, PO Box, or company name.

    - `owner.address.line2` (string, optional)
      Address line 2, such as the apartment, suite, unit, or building.

    - `owner.address.postal_code` (string, optional)
      ZIP or postal code.

    - `owner.address.state` (string, optional)
      State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

  - `owner.email` (string, optional)
    Owner’s email address.

    The maximum length is 800 characters.

  - `owner.name` (string, optional)
    Owner’s full name.

  - `owner.phone` (string, optional)
    Owner’s phone number.

- `source_order` (object, optional)
  Information about the items and shipping associated with the source. Required for transactional credit (for example Klarna) sources before you can charge it.

  - `source_order.items` (array of objects, optional)
    List of items constituting the order.

    - `source_order.items.parent` (string, optional)
      The ID of the SKU being ordered.

    - `source_order.items.quantity` (integer, optional)
      The quantity of this order item. When type is `sku`, this is the number of instances of the SKU to be ordered.

  - `source_order.shipping` (object, optional)
    Shipping address for the order. Required if any of the SKUs are for products that have `shippable` set to true.

    - `source_order.shipping.address` (object, required)
      Shipping address.

      - `source_order.shipping.address.line1` (string, required)
        Address line 1, such as the street, PO Box, or company name.

      - `source_order.shipping.address.city` (string, optional)
        City, district, suburb, town, or village.

      - `source_order.shipping.address.country` (string, optional)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `source_order.shipping.address.line2` (string, optional)
        Address line 2, such as the apartment, suite, unit, or building.

      - `source_order.shipping.address.postal_code` (string, optional)
        ZIP or postal code.

      - `source_order.shipping.address.state` (string, optional)
        State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

    - `source_order.shipping.carrier` (string, optional)
      The delivery service that shipped a physical product, such as Fedex, UPS, USPS, etc.

    - `source_order.shipping.name` (string, optional)
      Recipient name.

    - `source_order.shipping.phone` (string, optional)
      Recipient phone (including extension).

    - `source_order.shipping.tracking_number` (string, optional)
      The tracking number for a physical product, obtained from the delivery service. If multiple tracking numbers were generated for this purchase, please separate them with commas.

```curl
curl https://api.stripe.com/v1/sources/src_1N3lxdLkdIwHu7ixPHXy8UcI \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
```

```cli
stripe sources update src_1N3lxdLkdIwHu7ixPHXy8UcI \
  -d "metadata[order_id]"=6735
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

source = client.v1.sources.update(
  'src_1N3lxdLkdIwHu7ixPHXy8UcI',
  {metadata: {order_id: '6735'}},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

source = client.v1.sources.update(
  "src_1N3lxdLkdIwHu7ixPHXy8UcI",
  {"metadata": {"order_id": "6735"}},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$source = $stripe->sources->update(
  'src_1N3lxdLkdIwHu7ixPHXy8UcI',
  ['metadata' => ['order_id' => '6735']]
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

SourceUpdateParams params =
  SourceUpdateParams.builder().putMetadata("order_id", "6735").build();

Source source = client.v1().sources().update("src_1N3lxdLkdIwHu7ixPHXy8UcI", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const source = await stripe.sources.update(
  'src_1N3lxdLkdIwHu7ixPHXy8UcI',
  {
    metadata: {
      order_id: '6735',
    },
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.SourceUpdateParams{}
params.AddMetadata("order_id", "6735")
result, err := sc.V1Sources.Update(
  context.TODO(), "src_1N3lxdLkdIwHu7ixPHXy8UcI", params)
```

```dotnet
var options = new SourceUpdateOptions
{
    Metadata = new Dictionary<string, string> { { "order_id", "6735" } },
};
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Sources;
Source source = service.Update("src_1N3lxdLkdIwHu7ixPHXy8UcI", options);
```

### Response

```json
{
  "id": "src_1N3lxdLkdIwHu7ixPHXy8UcI",
  "object": "source",
  "ach_credit_transfer": {
    "account_number": "test_eb829353ed79",
    "bank_name": "TEST BANK",
    "fingerprint": "kBQsBk9KtfCgjEYK",
    "refund_account_holder_name": null,
    "refund_account_holder_type": null,
    "refund_routing_number": null,
    "routing_number": "110000000",
    "swift_code": "TSTEZ122"
  },
  "amount": null,
  "client_secret": "src_client_secret_ZaOIRUD8a9uGmQobLxGvqKSr",
  "created": 1683144457,
  "currency": "usd",
  "flow": "receiver",
  "livemode": false,
  "metadata": {
    "order_id": "6735"
  },
  "owner": {
    "address": null,
    "email": "jenny.rosen@example.com",
    "name": null,
    "phone": null,
    "verified_address": null,
    "verified_email": null,
    "verified_name": null,
    "verified_phone": null
  },
  "receiver": {
    "address": "110000000-test_eb829353ed79",
    "amount_charged": 0,
    "amount_received": 0,
    "amount_returned": 0,
    "refund_attributes_method": "email",
    "refund_attributes_status": "missing"
  },
  "statement_descriptor": null,
  "status": "pending",
  "type": "ach_credit_transfer",
  "usage": "reusable"
}
```