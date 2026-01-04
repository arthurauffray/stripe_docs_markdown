# Create a card

When you create a new credit card, you must specify a customer or recipient on which to create it.

If the card’s owner has no default card, then the new card will become the default. However, if the owner already has a default, then it will not change. To change the default, you should [update the customer](https://docs.stripe.com/docs/api.md#update_customer) to have a new `default_source`.

## Returns

Returns the `Card` object.

## Parameters

- `source` (object | string, required)
  A token, like the ones returned by [Stripe.js](https://docs.stripe.com/docs/js.md) or a dictionary containing a user’s card details (with the options shown below). Stripe will automatically validate the card.

  - `source.exp_month` (integer, required)
    Two-digit number representing the card’s expiration month.

  - `source.exp_year` (integer, required)
    Two- or -four-digit number representing the card’s expiration year.

  - `source.number` (string, required)
    The card number, as a string without any separators.

  - `source.object` (string, required)
    The type of payment source. It should be `card`.

  - `source.address_city` (string, optional)
    City / District / Suburb / Town / Village.

  - `source.address_country` (string, optional)
    Billing address country, if provided.

  - `source.address_line1` (string, optional)
    Address line 1 (Street address / PO Box / Company name).

  - `source.address_line2` (string, optional)
    Address line 2 (Apartment / Suite / Unit / Building).

  - `source.address_state` (string, optional)
    State / County / Province / Region.

  - `source.address_zip` (string, optional)
    ZIP or postal code.

  - `source.currency` (string, optional)
    Required when adding a card to an account (not applicable to customers or recipients). The card (which must be a debit card) can be used as a transfer destination for funds in this currency.

  - `source.cvc` (string, optional)
    Card security code. Highly recommended to always include this value, but it’s required only for accounts based in European countries.

  - `source.default_for_currency` (boolean, optional)
    Applicable only on accounts (not customers or recipients). If you set this to `true` (or if this is the first external account being added in this currency), this card will become the default external account for its currency.

  - `source.metadata` (object, optional)
    A set of key-value pairs that you can attach to a card object. This can be useful for storing additional information about the card in a structured format.

  - `source.name` (string, optional)
    Cardholder’s full name.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/customers/cus_9s6XGDTHzA66Po/sources \
  -u "<<YOUR_SECRET_KEY>>" \
  -d source=tok_visa
```

```cli
stripe payment_sources create cus_9s6XGDTHzA66Po \
  --source=tok_visa
```

```ruby
client = Stripe::StripeClient.new("<<YOUR_SECRET_KEY>>")

result = client.v1.customers.payment_sources.create(
  'cus_9s6XGDTHzA66Po',
  {source: 'tok_visa'},
)
```

```python
client = StripeClient("<<YOUR_SECRET_KEY>>")

payment_source = client.v1.customers.payment_sources.create(
  "cus_9s6XGDTHzA66Po",
  {"source": "tok_visa"},
)
```

```php
$stripe = new \Stripe\StripeClient('<<YOUR_SECRET_KEY>>');

$paymentSource = $stripe->customers->createSource(
  'cus_9s6XGDTHzA66Po',
  ['source' => 'tok_visa']
);
```

```java
StripeClient client = new StripeClient("<<YOUR_SECRET_KEY>>");

CustomerPaymentSourceCreateParams params =
  CustomerPaymentSourceCreateParams.builder().setSource("tok_visa").build();

PaymentSource paymentSource =
  client.v1().customers().paymentSources().create("cus_9s6XGDTHzA66Po", params);
```

```node
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customerSource = await stripe.customers.createSource(
  'cus_9s6XGDTHzA66Po',
  {
    source: 'tok_visa',
  }
);
```

```go
sc := stripe.NewClient("<<YOUR_SECRET_KEY>>")
params := &stripe.PaymentSourceCreateParams{
  Source: stripe.String("tok_visa"),
  Customer: stripe.String("cus_9s6XGDTHzA66Po"),
}
result, err := sc.V1PaymentSources.Create(context.TODO(), params)
```

```dotnet
var options = new CustomerPaymentSourceCreateOptions { Source = "tok_visa" };
var client = new StripeClient("<<YOUR_SECRET_KEY>>");
var service = client.V1.Customers.PaymentSources;
IPaymentSource iPaymentSource = service.Create("cus_9s6XGDTHzA66Po", options);
```

### Response

```json
{
  "id": "card_1NGTaT2eZvKYlo2CZWSctn5n",
  "object": "card",
  "address_city": null,
  "address_country": null,
  "address_line1": null,
  "address_line1_check": null,
  "address_line2": null,
  "address_state": null,
  "address_zip": null,
  "address_zip_check": null,
  "brand": "Visa",
  "country": "US",
  "customer": "cus_9s6XGDTHzA66Po",
  "cvc_check": "pass",
  "dynamic_last4": null,
  "exp_month": 8,
  "exp_year": 2024,
  "fingerprint": "Xt5EWLLDS7FJjR1c",
  "funding": "credit",
  "last4": "4242",
  "metadata": {},
  "name": null,
  "redaction": null,
  "tokenization_method": null,
  "wallet": null
}
```