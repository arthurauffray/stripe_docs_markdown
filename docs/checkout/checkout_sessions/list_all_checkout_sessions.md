# List all Checkout Sessions

Returns a list of Checkout Sessions.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` Checkout Sessions, starting after Checkout Session `starting_after`. Each entry in the array is a separate Checkout Session object. If no more Checkout Sessions are available, the resulting array will be empty.

## Parameters

- `created` (object, optional)
  Only return Checkout Sessions that were created during the given date interval.

  - `created.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `created.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `created.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `created.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `customer` (string, optional)
  Only return the Checkout Sessions for the Customer specified.

- `customer_account` (string, optional)
  Only return the Checkout Sessions for the Account specified.

- `customer_details` (object, optional)
  Only return the Checkout Sessions for the Customer details specified.

  - `customer_details.email` (string, required)
    Customer’s email address.

    The maximum length is 800 characters.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `payment_intent` (string, optional)
  Only return the Checkout Session for the PaymentIntent specified.

- `payment_link` (string, optional)
  Only return the Checkout Sessions for the Payment Link specified.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `status` (enum, optional)
  Only return the Checkout Sessions matching the given status.
Possible enum values:
  - `complete`
    The checkout session is complete. Payment processing may still be in progress

  - `expired`
    The checkout session has expired. No further processing will occur

  - `open`
    The checkout session is still in progress. Payment processing has not started

- `subscription` (string, optional)
  Only return the Checkout Session for the subscription specified.

```curl
curl -G https://api.stripe.com/v1/checkout/sessions \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe checkout sessions list  \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

sessions = client.v1.checkout.sessions.list({limit: 3})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

sessions = client.v1.checkout.sessions.list({"limit": 3})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$sessions = $stripe->checkout->sessions->all(['limit' => 3]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

SessionListParams params = SessionListParams.builder().setLimit(3L).build();

StripeCollection<Session> stripeCollection =
  client.v1().checkout().sessions().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const sessions = await stripe.checkout.sessions.list({
  limit: 3,
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.CheckoutSessionListParams{}
params.Limit = stripe.Int64(3)
result := sc.V1CheckoutSessions.List(context.TODO(), params)
```

```dotnet
var options = new Stripe.Checkout.SessionListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Checkout.Sessions;
StripeList<Stripe.Checkout.Session> sessions = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/checkout/sessions",
  "has_more": false,
  "data": [
    {
      "id": "cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u",
      "object": "checkout.session",
      "after_expiration": null,
      "allow_promotion_codes": null,
      "amount_subtotal": 2198,
      "amount_total": 2198,
      "automatic_tax": {
        "enabled": false,
        "liability": null,
        "status": null
      },
      "billing_address_collection": null,
      "cancel_url": null,
      "client_reference_id": null,
      "consent": null,
      "consent_collection": null,
      "created": 1679600215,
      "currency": "usd",
      "custom_fields": [],
      "custom_text": {
        "shipping_address": null,
        "submit": null
      },
      "customer": null,
      "customer_creation": "if_required",
      "customer_details": null,
      "customer_email": null,
      "expires_at": 1679686615,
      "invoice": null,
      "invoice_creation": {
        "enabled": false,
        "invoice_data": {
          "account_tax_ids": null,
          "custom_fields": null,
          "description": null,
          "footer": null,
          "issuer": null,
          "metadata": {},
          "rendering_options": null
        }
      },
      "livemode": false,
      "locale": null,
      "metadata": {},
      "mode": "payment",
      "payment_intent": null,
      "payment_link": null,
      "payment_method_collection": "always",
      "payment_method_options": {},
      "payment_method_types": [
        "card"
      ],
      "payment_status": "unpaid",
      "phone_number_collection": {
        "enabled": false
      },
      "recovered_from": null,
      "setup_intent": null,
      "shipping_address_collection": null,
      "shipping_cost": null,
      "shipping_details": null,
      "shipping_options": [],
      "status": "open",
      "submit_type": null,
      "subscription": null,
      "success_url": "https://example.com/success",
      "total_details": {
        "amount_discount": 0,
        "amount_shipping": 0,
        "amount_tax": 0
      },
      "url": "https://checkout.stripe.com/c/pay/cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u#fidkdWxOYHwnPyd1blpxYHZxWjA0SDdPUW5JbmFMck1wMmx9N2BLZjFEfGRUNWhqTmJ%2FM2F8bUA2SDRySkFdUV81T1BSV0YxcWJcTUJcYW5rSzN3dzBLPUE0TzRKTTxzNFBjPWZEX1NKSkxpNTVjRjN8VHE0YicpJ2N3amhWYHdzYHcnP3F3cGApJ2lkfGpwcVF8dWAnPyd2bGtiaWBabHFgaCcpJ2BrZGdpYFVpZGZgbWppYWB3dic%2FcXdwYHgl"
    }
  ]
}
```