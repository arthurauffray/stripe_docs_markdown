# List all charges

Returns a list of charges you’ve previously created. The charges are returned in sorted order, with the most recent charges appearing first.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` charges, starting after charge `starting_after`. Each entry in the array is a separate charge object. If no more charges are available, the resulting array will be empty. If you provide a non-existent customer ID, this call raises [an error](https://docs.stripe.com/api/charges/list.md#errors).

## Parameters

- `created` (object, optional)
  Only return charges that were created during the given date interval.

  - `created.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `created.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `created.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `created.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `customer` (string, optional)
  Only return charges for the customer specified by this customer ID.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `payment_intent` (string, optional)
  Only return charges that were created by the PaymentIntent specified by this PaymentIntent ID.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `transfer_group` (string, optional)
  Only return charges for this transfer group, limited to 100.

```curl
curl -G https://api.stripe.com/v1/charges \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

```cli
stripe charges list  \
  --limit=3
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

charges = client.v1.charges.list({limit: 3})
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

charges = client.v1.charges.list({"limit": 3})
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$charges = $stripe->charges->all(['limit' => 3]);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

ChargeListParams params = ChargeListParams.builder().setLimit(3L).build();

StripeCollection<Charge> stripeCollection = client.v1().charges().list(params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const charges = await stripe.charges.list({
  limit: 3,
});
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.ChargeListParams{}
params.Limit = stripe.Int64(3)
result := sc.V1Charges.List(context.TODO(), params)
```

```dotnet
var options = new ChargeListOptions { Limit = 3 };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Charges;
StripeList<Charge> charges = service.List(options);
```

### Response

```json
{
  "object": "list",
  "url": "/v1/charges",
  "has_more": false,
  "data": [
    {
      "id": "ch_3MmlLrLkdIwHu7ix0snN0B15",
      "object": "charge",
      "amount": 1099,
      "amount_captured": 1099,
      "amount_refunded": 0,
      "application": null,
      "application_fee": null,
      "application_fee_amount": null,
      "balance_transaction": "txn_3MmlLrLkdIwHu7ix0uke3Ezy",
      "billing_details": {
        "address": {
          "city": null,
          "country": null,
          "line1": null,
          "line2": null,
          "postal_code": null,
          "state": null
        },
        "email": null,
        "name": null,
        "phone": null
      },
      "calculated_statement_descriptor": "Stripe",
      "captured": true,
      "created": 1679090539,
      "currency": "usd",
      "customer": null,
      "description": null,
      "disputed": false,
      "failure_balance_transaction": null,
      "failure_code": null,
      "failure_message": null,
      "fraud_details": {},
      "livemode": false,
      "metadata": {},
      "on_behalf_of": null,
      "outcome": {
        "network_status": "approved_by_network",
        "reason": null,
        "risk_level": "normal",
        "risk_score": 32,
        "seller_message": "Payment complete.",
        "type": "authorized"
      },
      "paid": true,
      "payment_intent": null,
      "payment_method": "card_1MmlLrLkdIwHu7ixIJwEWSNR",
      "payment_method_details": {
        "card": {
          "brand": "visa",
          "checks": {
            "address_line1_check": null,
            "address_postal_code_check": null,
            "cvc_check": null
          },
          "country": "US",
          "exp_month": 3,
          "exp_year": 2024,
          "fingerprint": "mToisGZ01V71BCos",
          "funding": "credit",
          "installments": null,
          "last4": "4242",
          "mandate": null,
          "network": "visa",
          "three_d_secure": null,
          "wallet": null
        },
        "type": "card"
      },
      "receipt_email": null,
      "receipt_number": null,
      "receipt_url": "https://pay.stripe.com/receipts/payment/CAcaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KOvG06AGMgZfBXyr1aw6LBa9vaaSRWU96d8qBwz9z2J_CObiV_H2-e8RezSK_sw0KISesp4czsOUlVKY",
      "refunded": false,
      "review": null,
      "shipping": null,
      "source_transfer": null,
      "statement_descriptor": null,
      "statement_descriptor_suffix": null,
      "status": "succeeded",
      "transfer_data": null,
      "transfer_group": null
    }
  ]
}
```